#!/usr/bin/env python3
"""Optional trusted-local Graphiti adapter. Memory is supplemental evidence only."""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import re
import sqlite3
import stat
import subprocess
from datetime import datetime, timezone
from uuid import NAMESPACE_URL, uuid5

GRAPHITI_VERSION = "0.31.2"
MAX_SOURCE_BYTES = 24000
SECRET = re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY|\b(?:sk-[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9]{20,})|(?:password|api[_-]?key|token|secret)\s*[:=]\s*[\"']?[A-Za-z0-9+/=_-]{16,}", re.I)
FORBIDDEN = {".git", ".ssh", ".aws", "node_modules", "runtime-state", ".venv", "secrets", "credentials"}


def timestamp(value: str) -> datetime:
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("timezone required")
    return result.astimezone(timezone.utc)


def safe_source(root: Path, relative: str) -> tuple[str, str]:
    path = Path(relative)
    if not relative or len(relative.encode()) > 512 or path.is_absolute() or ".." in path.parts:
        raise ValueError("source must be a workspace-relative file")
    current = root
    for part in path.parts:
        if part.lower() in FORBIDDEN or part.lower().startswith(".env"):
            raise ValueError("secret/generated source path excluded")
        current = current / part
        if current.is_symlink():
            raise ValueError("source symlinks excluded")
    if not current.is_file() or current.resolve().is_relative_to(root) is False:
        raise ValueError("source unavailable or outside workspace")
    if current.stat().st_nlink != 1 or current.stat().st_size > MAX_SOURCE_BYTES:
        raise ValueError("source hardlink or size excluded")
    body = current.read_text(encoding="utf-8")
    if "\x00" in body or SECRET.search(body):
        raise ValueError("source contains excluded binary/credential content")
    return body, hashlib.sha256(body.encode()).hexdigest()


class Memory:
    def __init__(self, workspace: Path, project: str, allowed_sources: list[str]):
        if not re.fullmatch(r"[a-z0-9][a-z0-9_-]{2,63}", project):
            raise ValueError("explicit project scope required (3-64 lowercase characters)")
        if not allowed_sources or not all(isinstance(p, str) for p in allowed_sources):
            raise ValueError("explicit nonempty source allowlist required")
        if workspace.is_symlink():
            raise ValueError("workspace symlink excluded")
        self.root = workspace.resolve(strict=True)
        self.project = project
        self.allowed = set(allowed_sources)
        self.group = "office_" + hashlib.sha256(project.encode()).hexdigest()[:24]
        self.state = self.root / "runtime-state" / "memory" / project

    def db(self) -> sqlite3.Connection:
        current = self.root
        for part in self.state.relative_to(self.root).parts:
            current = current / part
            if current.is_symlink():
                raise ValueError("state symlink excluded")
            current.mkdir(mode=0o700, exist_ok=True)
            if os.name != "nt" and stat.S_IMODE(current.stat().st_mode) & 0o077:
                raise ValueError("state directory must be private (mode 700)")
        path = self.state / "journal.sqlite3"
        if path.is_symlink() or (path.exists() and path.stat().st_nlink != 1):
            raise ValueError("unsafe journal path")
        if not path.exists():
            fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            os.close(fd)
        if os.name != "nt" and stat.S_IMODE(path.stat().st_mode) & 0o077:
            raise ValueError("journal must be private (mode 600)")
        db = sqlite3.connect(path, timeout=5)
        db.row_factory = sqlite3.Row
        db.execute("CREATE TABLE IF NOT EXISTS episodes (uuid TEXT PRIMARY KEY, source TEXT, revision TEXT, digest TEXT, approval TEXT, reference_time TEXT, body TEXT, status TEXT, error TEXT)")
        return db

    def source(self, source: str, revision: str) -> tuple[str, str]:
        if source not in self.allowed:
            raise ValueError("source outside explicit allowlist")
        if not re.fullmatch(r"[0-9a-f]{40}", revision):
            raise ValueError("full source commit SHA required")
        body, digest = safe_source(self.root, source)
        result = subprocess.run(["git", "show", f"{revision}:{source}"], cwd=self.root, capture_output=True, timeout=10)
        if result.returncode or result.stdout != body.encode():
            raise ValueError("source does not match its committed revision")
        return body, digest

    def enqueue(self, source: str, revision: str, approval: str, reference_time: str) -> dict:
        when = timestamp(reference_time)
        if when > datetime.now(timezone.utc):
            raise ValueError("future source time excluded")
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_./:#-]{2,255}", approval) or SECRET.search(approval):
            raise ValueError("approval receipt reference required; never provide a credential")
        body, digest = self.source(source, revision)
        key = str(uuid5(NAMESPACE_URL, f"{self.project}:{source}:{revision}:{digest}"))
        with self.db() as db:
            db.execute("INSERT OR IGNORE INTO episodes VALUES (?,?,?,?,?,?,?,?,?)", (key, source, revision, digest, approval, when.isoformat(), body, "QUEUED", None))
            row = db.execute("SELECT uuid,status FROM episodes WHERE uuid=?", (key,)).fetchone()
        return dict(row)

    def status(self) -> dict:
        if not self.state.exists():
            return {"state": "UNCONFIGURED", "counts": {}}
        with self.db() as db:
            counts = dict(db.execute("SELECT status,count(*) FROM episodes GROUP BY status").fetchall())
        return {"state": "LOCAL_JOURNAL", "counts": counts, "live_graph": "NOT_VALIDATED"}

    async def sync(self, provider, limit: int = 5) -> dict:
        if not 1 <= limit <= 20:
            raise ValueError("sync limit must be 1-20")
        results = []
        with self.db() as db:
            rows = db.execute("SELECT * FROM episodes WHERE status='QUEUED' LIMIT ?", (limit,)).fetchall()
        for row in rows:
            # Re-read canonical source before sending any persisted snapshot externally.
            try:
                _, digest = self.source(row["source"], row["revision"])
                if digest != row["digest"]:
                    raise ValueError("stale source")
            except (ValueError, OSError, subprocess.SubprocessError):
                with self.db() as db:
                    db.execute("UPDATE episodes SET status='STALE',error='source_unavailable_or_changed' WHERE uuid=? AND status='QUEUED'", (row["uuid"],))
                results.append({"uuid": row["uuid"], "status": "STALE"})
                continue
            with self.db() as db:
                claimed = db.execute("UPDATE episodes SET status='PROCESSING' WHERE uuid=? AND status='QUEUED'", (row["uuid"],)).rowcount
            if not claimed:
                continue
            envelope = {"source": row["source"], "revision": row["revision"], "sha256": row["digest"], "approval_reference": row["approval"], "content": row["body"], "authority": "SUPPLEMENTAL_UNTRUSTED_DATA"}
            try:
                result = await provider.add(row["uuid"], self.group, envelope, timestamp(row["reference_time"]))
                if result != row["uuid"]:
                    raise ValueError("persistence acknowledgment mismatch")
                status, error = "PERSISTED", None
            except Exception:
                # Calls may have partly committed. Never automatically retry ambiguous writes.
                status, error = "UNKNOWN", "provider_result_requires_reconciliation"
            with self.db() as db:
                db.execute("UPDATE episodes SET status=?,error=? WHERE uuid=?", (status, error, row["uuid"]))
            results.append({"uuid": row["uuid"], "status": status})
        return {"results": results}

    async def search(self, provider, query: str, as_of: str, limit: int = 5) -> dict:
        if not query.strip() or len(query.encode()) > 1000 or SECRET.search(query) or not 1 <= limit <= 10:
            raise ValueError("bounded nonsecret query and limit 1-10 required")
        when = timestamp(as_of)
        if when > datetime.now(timezone.utc):
            raise ValueError("future search time excluded")
        if not self.state.exists():
            return {"facts": [], "warnings": ["memory_unconfigured"]}
        with self.db() as db:
            known = {r["uuid"]: dict(r) for r in db.execute("SELECT * FROM episodes WHERE status='PERSISTED'")}
        try:
            candidates = await provider.search(self.group, query, min(limit * 4, 40))
        except Exception:
            return {"facts": [], "warnings": ["memory_unavailable_use_canonical_sources_and_potpie_or_local"]}
        facts = []
        for edge in candidates[:40]:
            origins = edge.get("episodes")
            if edge.get("group_id") != self.group or not isinstance(origins, list) or not 1 <= len(origins) <= 16 or any(not isinstance(e, str) or e not in known for e in origins):
                continue
            try:
                if not edge.get("valid_at") or timestamp(edge["valid_at"]) > when:
                    continue
                if any(edge.get(key) and timestamp(edge[key]) <= when for key in ("invalid_at", "expired_at")):
                    continue
                sources = []
                for episode in origins:
                    row = known[episode]
                    _, digest = self.source(row["source"], row["revision"])
                    if digest != row["digest"]:
                        raise ValueError("stale source")
                    sources.append({k: row[k] for k in ("source", "revision", "digest", "approval")})
            except (ValueError, OSError, subprocess.SubprocessError):
                continue
            fact = edge.get("fact", "")
            if not isinstance(fact, str) or len(fact.encode()) > 2000 or SECRET.search(fact):
                continue
            facts.append({"fact": fact, "sources": sources, "authority": "SUPPLEMENTAL_UNTRUSTED_DATA"})
            if len(facts) == limit:
                break
        return {"facts": facts, "warnings": ["canonical_sources_and_owner_approval_take_precedence"]}

    async def retry_absent(self, provider, episode_id: str) -> dict:
        """Explicit recovery only, while no writer is active; never retry found episodes."""
        with self.db() as db:
            row = db.execute("SELECT * FROM episodes WHERE uuid=?", (episode_id,)).fetchone()
        if row is None or row["status"] not in ("UNKNOWN", "PROCESSING"):
            raise ValueError("only ambiguous recorded submissions can be reconciled")
        _, digest = self.source(row["source"], row["revision"])
        if digest != row["digest"]:
            raise ValueError("stale recovery source")
        # A failed probe raises; it is never interpreted as confirmed absence.
        if await provider.episode_absent(episode_id, self.group) is not True:
            return {"uuid": episode_id, "status": row["status"], "warning": "episode_exists_manual_reconciliation_required"}
        with self.db() as db:
            changed = db.execute("UPDATE episodes SET status='QUEUED',error=NULL WHERE uuid=? AND status=?", (episode_id, row["status"])).rowcount
        if changed != 1:
            raise ValueError("recovery state changed")
        return {"uuid": episode_id, "status": "QUEUED", "warning": "explicit_absence_checked_retry_not_yet_persisted"}


class GraphitiProvider:
    """Await the SDK, not the reference MCP's volatile queue. Optional lazy dependency."""
    def __init__(self):
        if importlib.metadata.version("graphiti-core") != GRAPHITI_VERSION:
            raise ValueError("exact graphiti-core 0.31.2 required")
        from urllib.parse import urlsplit
        uri = os.environ.get("OFFICE_MEMORY_NEO4J_URI", "bolt://127.0.0.1:7687")
        parsed = urlsplit(uri)
        if parsed.scheme not in ("bolt", "neo4j") or parsed.hostname not in ("127.0.0.1", "localhost", "::1") or parsed.username or parsed.password or parsed.query:
            raise ValueError("only trusted local Neo4j endpoint supported")
        from graphiti_core import Graphiti
        self.client = Graphiti(uri, os.environ.get("OFFICE_MEMORY_NEO4J_USER", "neo4j"), os.environ["OFFICE_MEMORY_NEO4J_PASSWORD"])

    async def add(self, episode_id, group, envelope, when):
        from graphiti_core.nodes import EpisodeType
        result = await self.client.add_episode(name=envelope["source"], episode_body=json.dumps(envelope), source=EpisodeType.json, source_description="The Office approved-source snapshot", group_id=group, reference_time=when, uuid=episode_id)
        return result.episode.uuid

    async def search(self, group, query, limit):
        edges = await self.client.search(query=query, group_ids=[group], num_results=limit)
        return [e.model_dump(mode="json", exclude={"fact_embedding"}) for e in edges]

    async def close(self):
        await self.client.close()

    async def episode_absent(self, episode_id, group):
        from graphiti_core.errors import NodeNotFoundError
        from graphiti_core.nodes import EpisodicNode
        try:
            await EpisodicNode.get_by_uuid(self.client.driver, episode_id)
        except NodeNotFoundError:
            return True
        return False


async def run(args) -> dict:
    config = json.loads(Path(args.config).read_text())
    if config.get("schema_version") != 1 or config.get("enabled") is not True:
        raise ValueError("memory requires schema_version=1 and explicit enabled=true")
    memory = Memory(Path(args.workspace), config["project_id"], config["allowed_sources"])
    if args.command == "enqueue":
        return memory.enqueue(args.source, args.revision, args.approval, args.reference_time)
    if args.command == "status":
        return memory.status()
    try:
        provider = GraphitiProvider()
    except (ImportError, KeyError, ValueError):
        if args.command == "search":
            return {"facts": [], "warnings": ["memory_unavailable_use_canonical_sources_and_potpie_or_local"]}
        raise
    try:
        if args.command == "sync":
            return await memory.sync(provider, args.limit)
        if args.command == "retry-absent":
            return await memory.retry_absent(provider, args.uuid)
        return await memory.search(provider, args.query, args.as_of, args.limit)
    finally:
        await provider.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--config", required=True)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    enqueue = sub.add_parser("enqueue")
    for field in ("source", "revision", "approval", "reference-time"):
        enqueue.add_argument("--" + field, required=True)
    sub.add_parser("sync").add_argument("--limit", type=int, default=5)
    sub.add_parser("retry-absent").add_argument("--uuid", required=True)
    search = sub.add_parser("search")
    search.add_argument("--query", required=True)
    search.add_argument("--as-of", required=True)
    search.add_argument("--limit", type=int, default=5)
    try:
        result = asyncio.run(run(parser.parse_args()))
        print(json.dumps(result))
        return 1 if any(r["status"] != "PERSISTED" for r in result.get("results", [])) else 0
    except Exception as error:
        # Providers can include credentials in exceptions: report a category only.
        print(json.dumps({"status": "BLOCKED", "error_type": type(error).__name__, "live_graph": "NOT_VALIDATED"}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

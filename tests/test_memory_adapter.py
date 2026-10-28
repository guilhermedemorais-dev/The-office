import asyncio
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("office_memory", Path(__file__).resolve().parents[1] / "integrations/memory/adapter.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)
ROOT = Path(__file__).resolve().parents[1]


class FakeProvider:
    def __init__(self):
        self.calls = []
        self.facts = []
        self.fail = False

    async def add(self, uid, group, envelope, when):
        self.calls.append((uid, group, envelope, when))
        if self.fail:
            raise RuntimeError("private provider token must not be logged")
        return uid

    async def search(self, group, query, limit):
        if self.fail:
            raise RuntimeError("unavailable")
        return self.facts

    async def episode_absent(self, uid, group):
        return True


class MemoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.source = self.root / "docs/spec.md"
        self.source.parent.mkdir()
        self.source.write_text("# Approved decision\nUse the existing API.\n")
        for cmd in (["git", "init", "-q"], ["git", "add", "docs/spec.md"], ["git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "fixture"]):
            subprocess.run(cmd, cwd=self.root, check=True, capture_output=True)
        self.sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=self.root, check=True, text=True, capture_output=True).stdout.strip()
        self.memory = MOD.Memory(self.root, "project-a", ["docs/spec.md"])
        self.provider = FakeProvider()

    def tearDown(self):
        self.tmp.cleanup()

    def enqueue(self):
        return self.memory.enqueue("docs/spec.md", self.sha, "TASK-1:rev1:receipt", "2026-01-01T00:00:00Z")

    def run_async(self, value):
        return asyncio.run(value)

    def persisted(self):
        uid = self.enqueue()["uuid"]
        self.assertEqual(self.run_async(self.memory.sync(self.provider))["results"][0]["status"], "PERSISTED")
        return uid

    def edge(self, uid, **changes):
        return dict({"fact": "Project uses existing API", "group_id": self.memory.group, "episodes": [uid], "valid_at": "2026-01-01T00:00:00Z", "invalid_at": None}, **changes)

    def search(self):
        return self.run_async(self.memory.search(self.provider, "API decision", "2026-02-01T00:00:00Z"))

    def test_status_does_not_create_state(self):
        self.assertEqual(self.memory.status()["state"], "UNCONFIGURED")
        self.assertFalse((self.root / "runtime-state").exists())

    def test_replay_is_idempotent_and_persistence_is_distinct(self):
        first = self.enqueue()
        self.assertEqual(first["status"], "QUEUED")
        self.assertEqual(self.enqueue(), first)
        self.assertEqual(self.memory.enqueue("docs/spec.md", self.sha, "TASK:other-receipt", "2026-01-02T00:00:00Z"), first)
        self.run_async(self.memory.sync(self.provider))
        self.run_async(self.memory.sync(self.provider))
        self.assertEqual(len(self.provider.calls), 1)
        self.assertEqual(self.enqueue()["status"], "PERSISTED")
        self.assertEqual(self.memory.status()["counts"], {"PERSISTED": 1})

    def test_ambiguous_provider_failure_never_retries(self):
        self.enqueue()
        self.provider.fail = True
        result = self.run_async(self.memory.sync(self.provider))
        self.assertEqual(result["results"][0]["status"], "UNKNOWN")
        self.run_async(self.memory.sync(self.provider))
        self.assertEqual(len(self.provider.calls), 1)

    def test_changed_source_is_not_sent(self):
        self.enqueue()
        self.source.write_text("Changed and unapproved")
        result = self.run_async(self.memory.sync(self.provider))
        self.assertEqual(result["results"][0]["status"], "STALE")
        self.assertEqual(self.provider.calls, [])

    def test_fact_requires_live_source_and_persisted_provenance(self):
        uid = self.persisted()
        self.provider.facts = [self.edge(uid)]
        facts = self.search()["facts"]
        self.assertEqual(facts[0]["sources"][0]["revision"], self.sha)
        self.assertEqual(facts[0]["authority"], "SUPPLEMENTAL_UNTRUSTED_DATA")
        self.source.write_text("Changed")
        self.assertEqual(self.search()["facts"], [])

    def test_cross_project_unknown_and_mixed_origins_are_excluded(self):
        uid = self.persisted()
        self.provider.facts = [self.edge(uid, group_id="other"), self.edge(uid, episodes=["foreign"]), self.edge(uid, episodes=[uid, "foreign"]), self.edge(uid, episodes=[])]
        self.assertEqual(self.search()["facts"], [])
        other = MOD.Memory(self.root, "project-b", ["docs/spec.md"])
        self.assertNotEqual(other.group, self.memory.group)

    def test_current_only_dates_are_enforced(self):
        uid = self.persisted()
        self.provider.facts = [self.edge(uid, invalid_at="2026-01-02T00:00:00Z"), self.edge(uid, valid_at="2026-03-01T00:00:00Z"), self.edge(uid, valid_at=None), self.edge(uid, expired_at="2026-01-02T00:00:00Z"), self.edge(uid, valid_at="bad"), self.edge(uid, invalid_at="2026-03-01T00:00:00Z")]
        self.assertEqual(len(self.search()["facts"]), 1)

    def test_unavailable_memory_is_explicit_fallback(self):
        self.persisted()
        self.provider.fail = True
        result = self.search()
        self.assertFalse(result["facts"])
        self.assertIn("memory_unavailable", result["warnings"][0])

    def test_path_scope_and_revision_guards(self):
        for source in ("../escape", "/tmp/escape", ".env", "docs/other.md"):
            with self.assertRaises(ValueError):
                self.memory.enqueue(source, self.sha, "TASK:receipt", "2026-01-01T00:00:00Z")
        for revision in ("HEAD", "0" * 40, self.sha[:7]):
            with self.assertRaises(ValueError):
                self.memory.enqueue("docs/spec.md", revision, "TASK:receipt", "2026-01-01T00:00:00Z")

    def test_symlinks_and_credentials_excluded(self):
        self.source.unlink()
        outside = self.root / "outside.md"
        outside.write_text("content")
        self.source.symlink_to(outside)
        with self.assertRaises(ValueError):
            self.enqueue()
        self.source.unlink()
        self.source.write_text("api_key = 'abcdefghijklmnopqrstuvxyz123456'")
        with self.assertRaises(ValueError):
            self.enqueue()

    def test_state_symlink_and_weak_permissions_rejected(self):
        external = self.root / "state-target"
        external.mkdir()
        (self.root / "runtime-state").symlink_to(external, target_is_directory=True)
        with self.assertRaises(ValueError):
            self.enqueue()

    @unittest.skipIf(os.name == "nt", "POSIX mode policy")
    def test_weak_state_permissions_rejected(self):
        (self.root / "runtime-state").mkdir(mode=0o755)
        with self.assertRaises(ValueError):
            self.enqueue()

    def test_wrong_ack_is_ambiguous(self):
        self.enqueue()
        async def wrong(*args):
            return "wrong-uuid"
        self.provider.add = wrong
        result = self.run_async(self.memory.sync(self.provider))
        self.assertEqual(result["results"][0]["status"], "UNKNOWN")

    def test_explicit_recovery_requires_confirmed_absence(self):
        uid = self.enqueue()["uuid"]
        self.provider.fail = True
        self.run_async(self.memory.sync(self.provider))
        async def present(*args):
            return False
        self.provider.episode_absent = present
        self.assertEqual(self.run_async(self.memory.retry_absent(self.provider, uid))["status"], "UNKNOWN")
        async def absent(*args):
            return True
        self.provider.episode_absent = absent
        self.assertEqual(self.run_async(self.memory.retry_absent(self.provider, uid))["status"], "QUEUED")
        self.provider.fail = False
        self.run_async(self.memory.sync(self.provider))
        self.assertEqual(self.memory.status()["counts"], {"PERSISTED": 1})

    def test_queued_episode_cannot_verify_fact(self):
        uid = self.enqueue()["uuid"]
        self.provider.facts = [self.edge(uid)]
        self.assertEqual(self.search()["facts"], [])

    def test_secret_receipt_and_secret_fact_rejected(self):
        secret = "sk-" + "a" * 30
        with self.assertRaises(ValueError):
            self.memory.enqueue("docs/spec.md", self.sha, secret, "2026-01-01T00:00:00Z")
        uid = self.persisted()
        self.provider.facts = [self.edge(uid, fact=secret)]
        self.assertEqual(self.search()["facts"], [])

    def test_scope_time_query_and_size_bounds(self):
        for project in ("", "a", "../bad", "foreign scope"):
            with self.assertRaises(ValueError):
                MOD.Memory(self.root, project, ["docs/spec.md"])
        with self.assertRaises(ValueError):
            MOD.Memory(self.root, "project-a", [])
        for when in ("2026-01-01", "2999-01-01T00:00:00Z"):
            with self.assertRaises(ValueError):
                self.memory.enqueue("docs/spec.md", self.sha, "TASK:receipt", when)
        self.source.write_text("x" * (MOD.MAX_SOURCE_BYTES + 1))
        with self.assertRaises(ValueError):
            self.enqueue()
        with self.assertRaises(ValueError):
            self.run_async(self.memory.search(self.provider, "x" * 1001, "2026-01-01T00:00:00Z"))

    def test_cli_search_degrades_when_provider_cannot_be_constructed(self):
        config = self.root / "config.json"
        config.write_text(json.dumps({"schema_version": 1, "enabled": True,
                                     "project_id": "project-a", "allowed_sources": ["docs/spec.md"]}))
        args = SimpleNamespace(config=str(config), workspace=str(self.root), command="search",
                               query="API", as_of="2026-01-01T00:00:00Z", limit=5)
        for error in (ImportError("SDK unavailable"), KeyError("credential"), ValueError("version")):
            with patch.object(MOD, "GraphitiProvider", side_effect=error):
                result = self.run_async(MOD.run(args))
                self.assertEqual(result["facts"], [])
                self.assertIn("memory_unavailable", result["warnings"][0])
                args.command = "sync"
                with self.assertRaises(type(error)):
                    self.run_async(MOD.run(args))
                args.command = "search"

    def test_external_model_processing_and_costs_are_documented(self):
        guide = " ".join((ROOT / "integrations/memory/README.md").read_text().split())
        self.assertIn("may incur its charges", guide)
        self.assertIn("data-retention policy", guide)
        self.assertIn("pricing", guide)
        self.assertIn("does not enforce a spending limit", guide)


if __name__ == "__main__":
    unittest.main()

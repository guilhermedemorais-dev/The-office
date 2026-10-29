#!/usr/bin/env python3
"""Token-free, opt-in Git update checker for The Office.

Independent of the engineering orchestrator and LLM usage.
Only updates a clean checkout via fast-forward. Never merges divergent histories.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class UpdateError(RuntimeError):
    pass


def git(*args: str, cwd: Path = ROOT) -> str:
    p = subprocess.run(["git", "-C", str(cwd), *args], text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if p.returncode:
        raise UpdateError(p.stderr.strip() or "Git command failed")
    return p.stdout.strip()


def verify_checkout() -> None:
    if git("rev-parse", "--show-toplevel") != str(ROOT.resolve()):
        raise UpdateError("Run from the installed The Office checkout")
    if not git("remote", "get-url", "origin"):
        raise UpdateError("Missing origin remote")


def default_branch() -> str:
    try:
        value = git("symbolic-ref", "--short", "refs/remotes/origin/HEAD")
        return value.split("/", 1)[1]
    except UpdateError:
        return "main"


def read_state() -> dict:
    location = Path(git("rev-parse", "--git-dir"))
    if not location.is_absolute():
        location = ROOT / location
    path = location / "office-update-state.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_state(data: dict) -> None:
    location = Path(git("rev-parse", "--git-dir"))
    if not location.is_absolute():
        location = ROOT / location
    path = location / "office-update-state.json"
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def check(fetch: bool = True) -> dict:
    verify_checkout()
    branch = default_branch()
    if fetch:
        git("fetch", "--no-tags", "origin", f"refs/heads/{branch}:refs/remotes/origin/{branch}")
    current = git("rev-parse", "HEAD")
    target = git("rev-parse", f"refs/remotes/origin/{branch}")
    dirty = bool(git("status", "--porcelain", "--untracked-files=normal"))
    local_branch = git("symbolic-ref", "--quiet", "--short", "HEAD")
    ahead = int(git("rev-list", "--count", f"{target}..{current}"))
    behind = int(git("rev-list", "--count", f"{current}..{target}"))
    return dict(branch=branch, local_branch=local_branch,
                current=current, remote=target, ahead=ahead,
                behind=behind, dirty=dirty,
                update_available=(behind > 0 and ahead == 0))


def apply() -> dict:
    status = check()
    if not status["update_available"]:
        raise UpdateError("No safely applicable fast-forward update")
    if status["dirty"]:
        raise UpdateError("Working tree has changes; commit or stash manually first")
    if status["local_branch"] != status["branch"]:
        raise UpdateError("Switch to the main tracking branch before updating")
    # A full local reference is kept to allow an explicit manual rollback.
    backup_ref = f"refs/office-update-backups/{status['current']}"
    git("update-ref", backup_ref, status["current"])
    git("merge", "--ff-only", f"refs/remotes/origin/{status['branch']}")
    result = check(fetch=False)
    if result["current"] != status["remote"]:
        raise UpdateError("Update verification failed; inspect checkout and backup ref")
    save_state(dict(last_applied=result["current"], last_deferred=None))
    return dict(status="UPDATED", commit=result["current"], backup_ref=backup_ref)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="The Office update checker (no AI tokens)")
    parser.add_argument("action", nargs="?", choices=["check", "prompt", "apply", "later"],
                        default="prompt")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.action == "apply":
            output = apply()
        else:
            status = check()
            output = {"status": "UPDATE_AVAILABLE" if status["update_available"] else
                      ("DIVERGED" if status["ahead"] and status["behind"] else "UP_TO_DATE"), **status}
            if args.action == "later":
                save_state({"last_deferred": status["remote"]})
                output["status"] = "DEFERRED"
            elif args.action == "prompt" and status["update_available"] and sys.stdin.isatty() and not args.json:
                print(f"\nThe Office update available ({status['behind']} commits).")
                print("1) Atualizar agora")
                print("2) Depois")
                selected = input("Escolha [1/2]: ").strip()
                if selected == "1":
                    output = apply()
                else:
                    save_state({"last_deferred": status["remote"]})
                    output["status"] = "DEFERRED"
        if args.json:
            print(json.dumps(output, ensure_ascii=False))
        else:
            print(json.dumps(output, ensure_ascii=False, indent=2))
        return 0
    except (UpdateError, OSError, subprocess.SubprocessError) as exc:
        print(f"UPDATE_BLOCKED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

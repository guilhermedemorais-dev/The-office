"""Read-only platform overlays on the unchanged V1 tool catalogs.

No subprocesses, installs, network or persistent health cache. The canonical
Environment CLI remains the owner of preparation, consent and local state.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[2]
STATES = ("SUPPORTED", "AVAILABLE", "INSTALLED", "CONFIGURED", "AUTHENTICATED",
          "VERIFIED", "NOT_VALIDATED", "UNSUPPORTED", "BROKEN")


def detect_platform(system=None, release=None, version=None):
    """WSL is Linux. Native Windows requires a known release/build boundary."""
    system = platform.system() if system is None else system
    release = platform.release() if release is None else release
    version = platform.version() if version is None else version
    if system == "Linux":
        return "linux"
    if system == "Darwin":
        return "macos"
    if system == "Windows":
        if str(release) == "11":
            return "windows/win11"
        # Some Python versions report Windows 11 as release 10.
        try:
            build = int(str(version).split(".")[2])
        except (IndexError, ValueError):
            build = None
        if str(release) == "10" and build is not None:
            return "windows/win11" if build >= 22000 else "windows/win10"
        raise ValueError("Native Windows version/build not identified; do not assume Win10")
    raise ValueError("Unsupported execution platform: " + str(system))


def _inside(root, relative):
    target = (root / relative).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError("Catalog path escapes repository")
    return target


def load_catalog(platform_id, root=ROOT):
    if platform_id not in ("linux", "windows/win10", "windows/win11", "macos"):
        raise ValueError("Unknown platform")
    root = Path(root).resolve()
    overlay_path = root / "environment" / platform_id / "catalog.json"
    overlay = json.loads(overlay_path.read_text(encoding="utf-8"))
    source_path = _inside(root, overlay["canonical_catalog"])
    source_bytes = source_path.read_bytes()
    source = json.loads(source_bytes)
    tools = []
    for original in source["tools"]:
        entry = dict(original)
        _inside(root, entry["path"])
        inherited = original["validation"]
        supported = inherited in ("LINUX_SUITE", "WINDOWS_SUITE") and overlay["inherit_suite_evidence"]
        entry["support_state"] = "UNSUPPORTED" if inherited == "UNSUPPORTED" else ("SUPPORTED" if supported else "NOT_VALIDATED")
        entry["inherited_validation"] = inherited
        entry["native_v2_validation"] = "NOT_VALIDATED"
        tools.append(entry)
    digest = hashlib.sha256(overlay_path.read_bytes() + source_bytes).hexdigest()
    return {"schema_version": 1, "platform": platform_id,
            "catalog_fingerprint": digest, "canonical_catalog": overlay["canonical_catalog"],
            "inherited_evidence_revision": source.get("evidence_revision"), "tools": tools}


def inspect_tool(tool_id, platform_id=None, root=ROOT, which=None):
    """Observe files/runtime discovery without executing or certifying a tool.

    Runtime discovery belongs to the actual host. An explicit foreign platform
    is metadata-only and never inherits executable evidence from this machine.
    """
    actual = detect_platform()
    platform_id = actual if platform_id is None else platform_id
    catalog = load_catalog(platform_id, root)
    tool = next((t for t in catalog["tools"] if t["id"] == tool_id), None)
    if tool is None:
        raise ValueError("Tool not found: " + tool_id)
    which = shutil.which if which is None else which
    runtime_name = {"Python": "python", "Node": "node", "Bash": "bash"}.get(tool["runtime"])
    source_exists = _inside(Path(root), tool["path"]).is_file()
    runtime_found = bool(which(runtime_name)) if platform_id == actual and runtime_name else None
    return {"tool": tool, "platform": platform_id, "source_exists": source_exists,
            "runtime_discovered": runtime_found,
            "states": {"SUPPORTED": tool["support_state"] == "SUPPORTED",
                       "UNSUPPORTED": tool["support_state"] == "UNSUPPORTED",
                       "NOT_VALIDATED": True,
                       "AVAILABLE": None, "INSTALLED": None, "CONFIGURED": None,
                       "AUTHENTICATED": None, "VERIFIED": None, "BROKEN": None},
            "eligible_for_verification": source_exists and runtime_found is True and tool["support_state"] != "UNSUPPORTED",
            "catalog_fingerprint": catalog["catalog_fingerprint"],
            "next_action": "Use canonical environment.py status/doctor and owner verification; discovery is not execution evidence."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--platform", choices=("linux", "windows/win10", "windows/win11", "macos"))
    parser.add_argument("--tool")
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    try:
        selected = args.platform or detect_platform()
        result = inspect_tool(args.tool, selected, args.repo_root) if args.tool else load_catalog(selected, args.repo_root)
        print(json.dumps(result, indent=2))
        return 0
    except (ValueError, OSError, KeyError) as error:
        print(json.dumps({"status": "BLOCKED", "error": str(error)}))
        return 1


if __name__ == "__main__":
    sys.exit(main())

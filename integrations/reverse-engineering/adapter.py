"""Plan authorized REA handoffs; never execute targets, providers or installers."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
PLUGIN = "plugins/reverse-engineering-standard"
RUNTIME = PLUGIN + "/runtime"
ROUTES = {
    "javascript": ("electron", "analyze_javascript_application"),
    "electron": ("electron", "analyze_javascript_application"),
    "asar": ("electron", "analyze_javascript_application"),
    "native": ("native_read", "binary_overview"),
    "managed": ("managed", "inspect_managed_artifact"),
    "apk": ("android", "inspect_android_package"),
    "firmware": ("firmware", "inspect_firmware_regions"),
    "browser": ("browser", "analyze_web_bundle"),
}


def inventory(root=ROOT):
    root = Path(root).resolve()
    runtime = root / RUNTIME
    lock = json.loads((runtime / "rea-runtime.lock.json").read_text(encoding="utf-8"))
    catalog = json.loads((runtime / "rea-capability-catalog.json").read_text(encoding="utf-8"))
    package = json.loads((runtime / "package.json").read_text(encoding="utf-8"))
    if lock["package"] != catalog["upstream"]["package"] or lock["version"] != catalog["upstream"]["version"]:
        raise ValueError("REA lock and capability catalog disagree")
    if package["dependencies"][lock["package"]] != "file:" + lock["vendored_tarball"]:
        raise ValueError("REA dependency does not reference the pinned original distribution")
    tarball = (runtime / lock["vendored_tarball"]).resolve()
    if not tarball.is_relative_to((root / PLUGIN).resolve()):
        raise ValueError("REA distribution escapes plugin")
    return {"package": lock["package"], "version": lock["version"],
            "license": lock["license"], "repository": lock["upstream_repository"],
            "minimum_node": package["engines"]["node"],
            "gateway": RUNTIME + "/reverse-context-gateway.mjs",
            "vendored_tarball": tarball.relative_to(root).as_posix(),
            "tarball_present": tarball.is_file(),
            "tarball_sha256": hashlib.sha256(tarball.read_bytes()).hexdigest() if tarball.is_file() else None,
            "families": sorted(catalog["families"]),
            "provider_validation": "NOT_VALIDATED",
            "bootstrap_command": ["npm", "run", "bootstrap"],
            "bootstrap_cwd": RUNTIME,
            "probe_command": ["node", RUNTIME + "/reverse-context-gateway.mjs", "probe"],
            "policy": "Inventory only. Separate authorization and real provider evidence are required before execution."}


def route(target_type, root=ROOT, runtime_observation=False):
    if target_type not in ROUTES:
        raise ValueError("Unsupported target type")
    family, tool = ROUTES[target_type]
    if runtime_observation:
        if target_type not in ("browser", "electron", "javascript"):
            raise ValueError("No generic runtime observation route for this target")
        family, tool = ("browser", "observe_web_session") if target_type == "browser" else ("javascript_runtime", "observe_javascript_runtime")
    catalog = json.loads((Path(root) / RUNTIME / "rea-capability-catalog.json").read_text(encoding="utf-8"))
    if tool not in catalog["families"][family]:
        raise ValueError("Route missing from original REA capability catalog")
    return {"target_type": target_type, "family": family, "capability": tool,
            "mode": "runtime_observation" if runtime_observation else "static_first",
            "gateway": RUNTIME + "/reverse-context-gateway.mjs",
            "required_preconditions": ["authorized target and scope", "current Task and contract revision",
                                       "original owner SKILL_RECEIPT", "real gateway/provider probe",
                                       "owner selects provider for target and execution platform"],
            "status": "PLAN_ONLY", "execution_performed": False,
            "handoff": ["OBSERVED/INFERRED/UNKNOWN findings with evidence IDs", "SDD", "implementation", "independent QA"]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target-type", choices=sorted(ROUTES))
    parser.add_argument("--runtime-observation", action="store_true")
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    try:
        result = route(args.target_type, args.repo_root, args.runtime_observation) if args.target_type else inventory(args.repo_root)
        print(json.dumps(result, indent=2))
        return 0
    except (ValueError, OSError, KeyError) as error:
        print(json.dumps({"status": "BLOCKED", "error": str(error)}))
        return 1


if __name__ == "__main__":
    sys.exit(main())

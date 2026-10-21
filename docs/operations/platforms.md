# Execution platforms and original tools

V2 overlays point to the unchanged V1 `Tools (Linux)`, `Tools (Windows)` and
`Tools (macOS)` catalogs. They do not move/copy owner scripts, replace the
existing Environment State or automatically install/start tools. The existing
canonical `environment.py` remains the preparation, consent and status owner.

| Runtime | Overlay | Inherited evidence | Native V2 certification |
| --- | --- | --- | --- |
| Linux, including WSL | `environment/linux/catalog.json` | V1 `LINUX_SUITE` where declared | Not claimed by metadata tests |
| Native Windows 10 | `environment/windows/win10/catalog.json` | V1 Windows10 build19045 receipts, per tool | NOT_VALIDATED here |
| Native Windows 11 | `environment/windows/win11/catalog.json` | No Windows10 homologation transfer | NOT_VALIDATED |
| macOS | `environment/macos/catalog.json` | Original `NOT VALIDATED` declarations | NOT_VALIDATED |

The V1 main includes Windows10 port receipts and native launch/secure-file
fixtures. These are historical source evidence, not executions performed in
this V2 session. External provider authentication and actual target operations
still need per-task verification. Native Windows >=build22000 selects Win11,
even when Python reports release10. Unknown Windows versions/builds fail rather
than silently assuming Win10. WSL executes through Linux regardless of desktop.

Host capability is a separate axis: a Linux catalog entry never establishes
that Codex, ChatGPT Work or another host can spawn agents, connect an MCP or use
native tools. Discover host capabilities and keep absent features explicit in
the Task. No host certification is asserted by this overlay.

## Read-only selection

```bash
python environment/shared/platform_catalog.py
python environment/shared/platform_catalog.py --platform windows/win11
python environment/shared/platform_catalog.py --tool environment
```

`load_catalog(platform_id, root)` resolves owner paths and validates repository
containment. Its fingerprint covers both overlay and canonical catalog bytes;
it is catalog identity, not a replacement Environment State cache. Source
changes, runtime changes and actual failures must be reconciled through the
existing Environment `status`/`doctor` flow and its source fingerprints.

`inspect_tool` only discovers source files and runtime names with `shutil.which`.
It never executes even a version command, and explicit foreign-platform queries
are metadata-only. `eligible_for_verification` means verification can be planned;
it never authorizes execution or establishes minimum runtime versions.

## State semantics

| State | Evidence required |
| --- | --- |
| SUPPORTED | Scoped platform support declaration with retained provenance |
| AVAILABLE | Actual host capability discovery, not catalog membership |
| INSTALLED | Verified installation observation from canonical Environment/owner |
| CONFIGURED | Validated configuration observation, never a secret dump |
| AUTHENTICATED | Successful harmless scoped identity/auth check |
| VERIFIED | Real owner execution evidence at current revision/platform |
| NOT_VALIDATED | Missing or stale verification; coexists with declared support |
| UNSUPPORTED | No supported platform route; choose another compatible capability |
| BROKEN | Actual failed check, not merely an unavailable optional tool |

The metadata prober returns unknown (`null`) for operational states it cannot
establish. States are separate dimensions, not a linear escalation from
installed to authenticated. Runtime discovery is not engine verification.
Canonical V1 state vocabulary remains intact; V2 does not rename V1 schemas.

## Preparation and recovery

Run the original owner CLI with actual checkout/workspace/state paths:

```bash
python plugins/dev-environment-standard/skills/dev-environment-standard/scripts/environment.py status --repo-root . --workspace . --json
python plugins/dev-environment-standard/skills/dev-environment-standard/scripts/environment.py prepare --repo-root . --workspace . --dry-run --json
```

Review concrete actions under the existing consent policy before applying them.
Reuse canonical local preferences/observations, including declined optionals.
Missing runtimes, tools or optional MCPs do not block unrelated work. Use a
verified compatible alternative when one exists and record unmet capabilities.
Do not silently install WSL, browsers, global REA or administrative packages.
After platform/source/runtime drift refresh only relevant observations.

REA integration and metadata commands are documented in
`integrations/reverse-engineering/README.md`. Bootstrap/provider execution is
not part of metadata selection. Real native Windows11/macOS verification,
Windows10 V2 acceptance and live provider acceptance remain local test work.

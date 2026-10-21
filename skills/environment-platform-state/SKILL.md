---
name: environment-platform-state
description: "Use for environment platform state: Platform routing; Library, ownership and local state; Health and handoff. Load required core skills first."
---

# The Office V2: environment-platform-state

Source: `plugins/dev-environment-standard/skills/dev-environment-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, environment-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/environment-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/dev-environment-standard/skills/dev-environment-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/dev-environment-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

<!-- source-section:dev-environment-standard:003 sha256:2e71750df4b02d773bce069ef7d2cfd3e53e2fcbf3084462123c8a4f72bd7436 -->
## Platform routing

During assisted installation invoke `prepare` once with the actual execution
runtime and writable local state. `platform_tools` selects the packaged
`Tools (Linux)`, `Tools (Windows)` or `Tools (macOS)` catalog and persists the
binding in the existing environment state. This is not an automatic host hook
and never rewrites manifests. Before later tasks reuse `status`; do not ask
which OS to use on every request. WSL selects Linux, not native Windows.
Runtime, catalog or source drift requires preparation again. Interpreter file
checks are cheap cache invalidation, not certification of runtime support.

Catalogs reference canonical owner scripts without duplicates. Route only
`eligible: true` entries, subject to owner gates and prerequisites.
`NOT VALIDATED` needs verification or an approved adapter; `UNSUPPORTED` has
no approved platform route. This does not block unrelated external tools with
their own compatible registry/runtime evidence. Context retrieval via Potpie
or lexical fallback supplements Task sources; environment state owns OS selection.

<!-- source-section:dev-environment-standard:004 sha256:62d8b8d4daa6b94c642658c2f9498fe1804efb078d58ff6fdb599c8d5f15a629 -->
## Library, ownership and local state

| Artifact | Responsibility |
| --- | --- |
| MCP Library | Public, versioned provider/capability/policy knowledge |
| Custom MCP | Developer-local, audited extension; never automatically published |
| Tool Registry | Specialist-owned tool definitions, not copied into this plugin |
| Environment State | Ignored local observations, preferences and compatible health snapshot |

MCP tiers: `CORE`, `RECOMMENDED`, `OPTIONAL`, `PROJECT_SPECIFIC`, `COMMUNITY`,
`RUNTIME_PROVIDED`. Provenance is a separate field: `OFFICIAL`,
`VERIFIED_THIRD_PARTY`, `COMMUNITY`, `UNKNOWN`. Runtime states are `AVAILABLE`,
`INSTALLED`, `CONNECTED`, `AUTH_REQUIRED`, `MISSING`, `BROKEN`, `UNSUPPORTED`.

Preserve all four distinctions:

```text
installed != connected
connected != authenticated
registered != available
planned tool != executed tool
```

UNKNOWN never installs automatically. COMMUNITY requires specific consent after
source/permission review. `node_repl` is detect-only when supplied by the host.
Docker MCP Registry is a catalog, not a connectable server. Docker MCP Gateway
is an optional lifecycle/isolation route when compatible Docker tooling already
exists; Docker is not a mandatory bootstrap dependency.

<!-- source-section:dev-environment-standard:006 sha256:591ae2066869019f617306c0b2475723b13780fd316d3c1a969f3ebafe1f27c8 -->
## Health and handoff

`HEALTHY` requires evidence for structure, references, registry validity, state
safety, scripts and relevant validators/tests. Unknown checks are NOT VALIDATED.
`DEGRADED` means usable portions exist but evidence/capabilities are incomplete.
`BLOCKED` means a required prerequisite or invariant fails. Task readiness is
separate from whether every optional catalog entry happens to be installed.

Return to the Harness with the required capability status and evidence, then
let its router invoke the owner skill. A healthcheck does not produce a
specialist execution receipt on that specialist's behalf.

<!-- end of selected V2 skill -->

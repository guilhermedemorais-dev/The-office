---
name: security-tools-reporting
description: "Use for security tools reporting: Tool Policy; Evidence And Reporting. Load required core skills first."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: security-tools-reporting

Source: `plugins/security-standard/skills/security-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, security-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/security-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/security-standard/skills/security-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/security-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

<!-- source-section:security-standard:006 sha256:3818ac4655cf1d59dadac032799bd86ea3dd2f03690693a076fc571f8f341e56 -->
## Tool Policy

Own security capabilities and tools through `references/tool-registry.json`.
Use the shared `skill-owned-tools.md` state protocol and
`plugins/dev-workflow-standard/scripts/tool-state.py` for cached resolution,
detection, verification, and local persistence. Prefer the cached fast path;
when absent or stale, detect first, select the official supported install
method if needed, verify and record it immediately. A failed installation is
recorded and not retried unchanged in the same cycle. Never assume a host tool
is present in a container. On failure, validate the finding, correct within
scope, and rerun the affected check before claiming PASS.

Use installed security tools when they improve evidence, but do not make one
vendor or scanner mandatory. Inspect configuration and versions before use.

Examples include dependency audits, secret scanners, SAST, linters, container
scanners, IaC checks, Playwright, API clients, and repository-native tests.

Consult the portable MCP Library owned by `dev-environment-standard` for provider
knowledge, and use actual host evidence for availability, connection and auth.
Environment preparation can diagnose/prepare required tools through this skill's
registry; security-standard retains source/finding interpretation and validation.
No developer-specific inventory establishes that a MCP is available. Unknown
providers never install automatically; community sources need explicit consent.
`node_repl` is detect-only when provided by the host. Select browser, documentation
or advisory tools only for the authorized defensive scope.

Verify live MCP availability before relying on it. Do not send private source,
secrets, customer data, tokens, cookies, or vulnerability evidence to remote MCP
services. MCP output is candidate evidence and never replaces repository or
runtime validation.

Scanner output is candidate input. Validate findings in code and runtime before
reporting them as vulnerabilities. Record tool failures and blind spots.

<!-- source-section:security-standard:008 sha256:3d24c848e0e8519d9e1d5697f8082ecfee615255c49f8ef678031faea06f798a -->
## Evidence And Reporting

Write project reports under the existing canonical security/docs structure. If
none exists and durable reporting is required, prefer:

```text
docs/security/
  threat-model.md
  reviews/
    YYYY-MM-DD-<scope>.md
```

Each finding must include:

- ID and title
- status: `CONFIRMED`, `NEEDS_VALIDATION`, `FALSE_POSITIVE`, `FIXED`, or `ACCEPTED_RISK`
- severity and confidence
- affected file/route/component
- evidence and attack path
- preconditions and impact
- recommended fix
- tests or validation steps
- residual risk

Use `references/report-template.md` for durable audits. Maintain a coverage
ledger for scoped or repository audits and reconcile every row as `REVIEWED`,
`NOT_APPLICABLE`, `DEFERRED`, or `BLOCKED`, with evidence or an exact reason.

Always report status by layer:

- `Banco`
- `API/Backend`
- `Frontend/UI`
- `Infra/DevOps`
- `Dependencias/Supply Chain`

Final gate values:

- `PASS`: relevant scope validated; no unresolved release-blocking finding
- `PARTIAL`: useful review completed, but coverage or runtime evidence is incomplete
- `BLOCKED`: confirmed release-blocking risk or required validation cannot proceed
- `NOT VALIDATED`: no credible security validation was executed

Never issue final acceptance for the user. `PASS` means ready for human review,
not approved for production.

<!-- end of selected V2 skill -->

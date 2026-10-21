---
name: reverse-engineering-investigation
description: "Use for reverse-engineering investigation: Workflow. Load required core skills first."
---

# The Office V2: reverse-engineering-investigation

Source: `plugins/reverse-engineering-standard/skills/reverse-engineering-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, reverse-engineering-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/reverse-engineering-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/reverse-engineering-standard/skills/reverse-engineering-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/reverse-engineering-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

<!-- source-section:reverse-engineering-standard:002 sha256:799f073b43f822b0aea647d8450e6d49e7f13defd3c5d62e6cfcb9359102524b -->
## Workflow

1. Establish the question to answer, target identity and evidence required.
2. Reuse existing source, docs, symbols, analysis sessions and evidence before
   opening a new investigation.
3. Use the bundled reverse-context gateway for runtime capability discovery and
   execution. The gateway may invoke the pinned REA runtime and its providers;
   the specialist owns methodology and interpretation.
4. Prefer static analysis first when it can answer the question.
5. Use runtime observation only when needed and authorized.
6. Keep a finding ledger with OBSERVED, INFERRED and UNKNOWN claims.
7. Tie every material conclusion to inspectable evidence and limitations.
8. If reconstructing a feature, describe behavior, state, inputs/outputs,
   protocol, constraints and unknowns without copying proprietary implementation.
9. Hand reconstruction requirements to SDD. Implementation remains owned by
   dev-implementation-standard.
10. Return EXECUTION_RECEIPT evidence to the Harness and do not self-approve
    downstream QA/Security/UI/DevOps gates.

<!-- end of selected V2 skill -->

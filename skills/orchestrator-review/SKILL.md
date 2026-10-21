---
name: orchestrator-review
description: "Use for orchestrator review: Review Rules. Load required core skills first."
---

# The Office V2: orchestrator-review

Source: `plugins/dev-workflow-standard/skills/dev-workflow-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, orchestrator-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/orchestrator-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/dev-workflow-standard/skills/dev-workflow-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/dev-workflow-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

<!-- source-section:dev-workflow-standard:018 sha256:5f2c80a536d0b115102e902399006e9dd450288f5bd5bba6e9cc144bcb7a7008 -->
## Review Rules

When a PR comes back, the orchestrator reviews before approving:

1. PR points to task, issue, branch and the specs it followed.
2. Implementation matches the specs and the task's acceptance criteria.
3. Nothing was built outside the task scope; out-of-scope changes are justified.
4. `ui-ux-standard` validated the UI (when there is UI).
5. `security-standard` validated security (when the triggers above apply).
6. Tests required by the task exist and pass, with evidence.
7. Status reported by `Banco`, `API/Backend`, `Frontend/UI`; unvalidated areas
   marked `NAO VALIDADO`.
8. `EXECUTION_RECEIPT` proves the selected capability actually ran and produced
   inspectable output.
9. `SKILL_RECEIPT` proves every mandatory skill and reference was read.
10. `REUSE_INVENTORY` proves existing symbols, helpers, components, routes and
   sibling implementations were searched before new ones were created.
11. `MINIMAL_CODE_GATE` explains every new abstraction and confirms that no
    equivalent implementation was duplicated.
12. `EXECUTION_REPORT_COMMENT` matches the task, receipt, Project state, and PR
    when applicable; its remote URL/identifier proves publication. The comment
    never substitutes for receipt or validation evidence.
13. QA_STATUS from the independent QA owner, when REQUIRED, includes executed
    validation and bug/retest disposition. Every REQUIRED sector is reconciled;
    stale receipts, missing evidence or PARTIAL/NOT_VALIDATED prevent completion.

Then: **approve** for human review (not automatic merge/deploy) or **request rework** with specific,
spec-anchored reasons. Rejected review moves the card back to `In Progress` with
the `rework` label until corrected.

<!-- end of selected V2 skill -->

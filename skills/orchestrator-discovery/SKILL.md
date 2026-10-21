---
name: orchestrator-discovery
description: "Use for orchestrator discovery: Mandatory Flow. Load required core skills first."
---

# The Office V2: orchestrator-discovery

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

Canonical link resolution (repository-relative paths, not skill-directory-relative):
- `../../../../docs/workflow-pipeline.md`: `docs/workflow-pipeline.md`

<!-- source-section:dev-workflow-standard:009 sha256:8c65fb399fbec400d7de724a71e8bfa5b6e17a405cc0a964199cd51c12ae3290 -->
## Mandatory Flow

For product briefing, a new project or reassessment of an existing/low-code
system, invoke the available `studio-prd` skill before detailed module specs.
It owns briefing, PRD and the separate internal execution plan, not a competing
task template. Resolve the active bundle; do not guess sibling cache paths.
If absent, report the missing capability and use an explicitly available
canonical checkout, without claiming it installed.

Require the approved module count/IDs, actors/journeys and boundaries, plus
`docs/planejamento/plano-de-execucao.md` and its equivalent JSON revision.
Urgency cannot silently override prerequisites; unknown capacity/estimates
stay explicit. Preserve the full agreed production scope, not an automatic MVP.
After PRD/order approval, announce the first module ready for SDD and await
the user's instruction. Each module spec ends with coverage/gaps and its Issue
report before approval to continue. PRD approval is not implementation approval.
Existing bounded tasks need not repeat an entire product briefing.

For UI-bearing modules, require the project-owned Markdown guide and live HTML
component catalogue from UI/UX during specification. Route exact component
IDs/revisions to SDD, implementation and QA. A mock widget is not a tested backend.
Reuse the existing task template, sector matrix and list prompts unchanged.
The short per-task prompt in the internal plan is a contextual tech-lead note,
not a second execution contract or automatic permission to spawn chats.

```text
Idea / demand
  -> dev-workflow-standard: diagnose + critical questions
  -> collaborative Discovery / SDD with user + research
  -> sdd-spec-factory: specs, reference/design libraries, complete Issue + v2 JSON
  -> publish DISCOVERY_SDD_COMPLETED with token usage and changed surface
  -> human approval
  -> dev-workflow-standard: resolve executor capability + verify availability
  -> selected executor: invoked; state RUNNING
  -> dev-implementation-standard: implement routed microtasks + executor tests
  -> execution result: diff / files / commands / artifacts
  -> selected executor: complete EXECUTION_RECEIPT
  -> update Human Task + publish EXECUTION_REPORT_COMMENT when applicable
  -> dev-workflow-standard: VALIDATING
  -> independent UI/UX / QA / Security / DevOps validation as applicable
  -> sector reconciliation
  -> Pull Request / PR gate
  -> Harness final gate
  -> dev-workflow-standard: approve or request rework
  -> human review / acceptance
  -> merge / deploy (only after PR approved)
```

The orchestrator does not advance to the next stage until the current gate is
satisfied. The full pipeline lives in
[`workflow-pipeline.md`](../../../../docs/workflow-pipeline.md).

<!-- end of selected V2 skill -->

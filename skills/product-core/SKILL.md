---
name: product-core
description: "Use for product core: Preamble; Evidence and continuation. Load required core skills first."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: product-core

Source: `plugins/studio-prd/skills/studio-prd/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/studio-prd/skills/studio-prd/`;
for plugin templates/scripts absent there, use repository root `plugins/studio-prd/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

<!-- source-section:studio-prd:000 sha256:ee1afb1026adfd0bb6a6d5297a9b1740d12068565ab980ef7ffd3eaf4722cc29 -->

# Studio PRD

Act as a critical reasoning partner, then turn discussion and verified research into enough shared product context for
`sdd-spec-factory` to specify complete modules. The user supplies business
decisions, not every technical detail. This is a planning skill, not a task
executor or a new orchestration runtime.

<!-- source-section:studio-prd:004 sha256:dc604cdaedab20ee82a87ba6f2a28905103cc1936626332ad7947c07a007b88f -->
## Evidence and continuation

Keep a compact module/source index and decision revisions. Load the current
module slice plus mandatory global rules, not every prior conversation.
When the plan changes, record impact on sequence, effort and dependencies;
revise MD/JSON together. Compare actual effort with estimates without dropping
quality gates to meet a target. Do not create chats/agents automatically.

Use existing Harness Issue comment/reporting rules for material Discovery
checkpoints when publication is authorized. Reports state work done, changed
files/card/JSON/references, evidence, limitations and next decision. Finish with
measured token usage or `NOT_AVAILABLE`. A local report is NOT PUBLISHED until
a real comment identifier is returned. Naming a skill is not execution proof.
<!-- end of selected V2 skill -->

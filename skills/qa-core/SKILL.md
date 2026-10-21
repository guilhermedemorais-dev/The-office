---
name: qa-core
description: "Use for qa core: Preamble; Context and activation; Execution and ownership; Provenance. Load required core skills first."
---

# The Office V2: qa-core

Source: `plugins/qa-testing-standard/skills/qa-testing-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/qa-testing-standard/skills/qa-testing-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/qa-testing-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

Canonical link resolution (repository-relative paths, not skill-directory-relative):
- `references/test-strategy.md`: `plugins/qa-testing-standard/skills/qa-testing-standard/references/test-strategy.md`
- `references/bug-report.md`: `plugins/qa-testing-standard/skills/qa-testing-standard/references/bug-report.md`

<!-- source-section:qa-testing-standard:000 sha256:cacaa801479f014fce717b8aed9556de23a2a9104e2dea5196909a6296b6f615 -->

# QA Testing Standard

Receive one prompt per execution list, linking the Task's single JSON file
and selecting its `execution_lists` entry by `list_id`, never per item/subitem.
All lists live in that file; do not expect JSON inside the Human Task/prompt.
Read the list JSON and relevant canonical JSON fields, not Human Task sections
as execution input. Require current Harness evidence of full card/JSON normative
equivalence, tied to the contract revision and observed Issue update time.
Missing/stale evidence or divergence returns to Harness before execution.

Own functional correctness and Test Engineering. The Harness coordinates; QA
plans, executes and interprets behavior checks independently of the product
implementer. Tool execution and actual evidence, not a checklist, justify results.

<!-- source-section:qa-testing-standard:001 sha256:edd9a416802b14c6352e72905c4a09b33cc84b66fdafc92b9d139097c54249fd -->
## Context and activation

1. Receive `task_id`, `execution_contract_path`, `sector`, `revision` and relevant
   `dependency_receipts`. Read the contract; match the task and current revision.
   For v2, verify **normative equivalence** of the routed QA slice and the
   current Harness comparison receipt; stop
   on revision/content divergence before making any QA claim.
2. Resolve your own sector, routed microtasks and owner. For legacy
   `schema_version: 1` contracts,
   ask Harness to normalize historical `task_sections` into a JSON handoff. Load
   minimal global goal/acceptance references from JSON,
   `required_sources` (each with a `purpose`), relevant code and material receipts.
   Evaluate `conditional_sources` and read only when their condition occurs.
   OPTIONAL sources are not loaded automatically.
3. Read this SKILL completely and references required by the active mode.
   Record the existing `SKILL_RECEIPT`: skill, exact path, references_loaded,
   applied_rules and status LOADED or BLOCKED; sector/mode are contextual details.
4. The Harness reads the complete Human Task; QA executes from JSON only. With a
   legacy contract without sectors, request a scoped handoff from the Harness,
   preserving its mandatory sources and existing gates. Do not invent a sector
   or silently omit a source required by another applicable instruction.
5. Missing required source or `source_of_truth_conflict` blocks the claim. For
   insufficient context request `CONTEXT_EXPANSION` with reason, required_source
   and blocking_claim; let the Harness resolve it before loading unrelated docs.

Read [test-strategy](references/test-strategy.md) when planning, selecting test
levels/categories, investigating failures/flakiness, or interpreting a run.
Read [bug-report](references/bug-report.md) when reproducing a candidate,
documenting a bug, requesting rework, or verifying a fix. Do not load both
automatically for a simple already-specified validation.

<!-- source-section:qa-testing-standard:003 sha256:ca0a1247319fa64d08c22de29aadbcc6c76d658de9468eee0b5e6df39c1bab6d -->
## Execution and ownership

- Do not write or fix product code. Implementation owns code fixes and developer
  regression tests via `dev-implementation-standard`. QA may prepare test cases
  and scoped test artifacts when explicitly allowed, but must not weaken or edit
  an oracle merely to obtain green. Both may run tests; their responsibility differs.
- Confirmed bug: supply reproduction evidence and `REWORK_REQUESTED` to the
  affected owner through the Harness; preserve its status until its owner acts.
  QA retests the returned fix. Never mark another sector PASS, fabricate its
  receipt, or substitute developer tests for mandatory independent QA.
- QA can detect a `SECURITY_CANDIDATE`; route it to `security-standard` for
  exploitation/impact validation. `CONFIRMED_BUG` is not
  `CONFIRMED_SECURITY_FINDING`. Do not assign CVEs/security severity or publish
  a candidate as a vulnerability. Security keeps confidentiality, integrity,
  availability and abuse review.
- `ui-ux-standard` owns design fidelity, visual hierarchy, accessibility design,
  responsive behavior and visual runtime QA. QA owns functional forms,
  navigation, transitions and error behavior, not visual approval.
- `devops-standard` owns CI/CD, deployment, infrastructure, operational runtime,
  health and rollback; `dev-environment-standard` prepares available tooling.
  QA interprets product behavior after prerequisites are ready, not environment
  or production readiness. No deployment, production mutation or destructive
  test is implied by a QA assignment.

<!-- source-section:qa-testing-standard:006 sha256:f5e53d7db7e594b7ba8fe410f9c50703e3410beada9b0ca370227d163f01d56b -->
## Provenance

Independent QA ownership and routing are [PROJECT CHOICE]; QA_STATUS and sector
receipt details are [LOCAL EXTENSION], not official platform standards.
Risk-based selection and regression reasoning are [ECOSYSTEM CONVENTION].
Tool-specific official guidance is linked in test-strategy when relevant.
<!-- end of selected V2 skill -->

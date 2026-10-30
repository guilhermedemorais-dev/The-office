---
name: orchestrator-core
description: "Coordinate software engineering tasks, scope, specialist routing, execution evidence, and final review. Use for development work requiring task orchestration or cross-sector handoffs; not for standalone marketing or general conversation."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: orchestrator-core

Source: `plugins/dev-workflow-standard/skills/dev-workflow-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/dev-workflow-standard/skills/dev-workflow-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/dev-workflow-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

Canonical link resolution (repository-relative paths, not skill-directory-relative):
- `references/continuous-improvement.md`: `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/continuous-improvement.md`

<!-- source-section:dev-workflow-standard:000 sha256:7d105b4615f29cf1e3d14a7850720b161df2c7bac98b5369dcb631f220b1ab10 -->

# Dev Workflow Standard (Engineering Harness)

Primary engineering harness for Guilherme's software projects. The LLM using
this skill becomes the **engineering orchestrator / final reviewer**. It does not
write product code itself; it owns discovery, planning, capability routing,
execution state, handoff, validation, recovery and approval. It must actively
invoke the selected executor or specialist capability and cannot treat task
assignment, naming a skill, or writing a prompt as completed delegation.

Keep this file lightweight: load only the references required for the current
task.

<!-- source-section:dev-workflow-standard:001 sha256:37f3dd45ee999a5462c4834dc324966c97434ea964bf86dec11b3832dc0f3f27 -->
## Mission

- Receive the demand (client request, feature, bug, idea).
- Diagnose and ask the critical questions before anything is built.
- Consolidate scope (in / out / constraints / risks / pending decisions).
- Decide which specialist skills are needed.
- Require an intent contract before implementation, with artifact depth scaled
  to change complexity.
- Enforce the mandatory task contract before delegation.
- Resolve and invoke the capability that will execute each task.
- Track execution state and require evidence before advancing.
- Recover, retry or replan when a capability fails or becomes unavailable.
- Delegate, review and approve. Hold final acceptance with the user.

<!-- source-section:dev-workflow-standard:002 sha256:43ccdbd16a54d1459af97208cd4a4e1779bf85cd6848e69ca47d65d89c915e50 -->
## Harness Contract

The harness exists to convert plans into verified execution. Planning, assigning,
naming a skill, opening a terminal, or producing a delegation prompt is not
execution.

For every executable task, the harness must perform this loop:

1. classify the required capability;
2. resolve the preferred skill, plugin, tool, MCP, script, or executor;
3. verify that the capability is actually available in the current runtime;
4. resolve the owner skill before selecting a provider/model; if an executor LLM
   is needed, verify the runtime with the provider resolver and do not equate
   configured credentials with availability;
5. invoke it with the minimum complete task contract and required context paths;
6. observe the execution result: output, diff, files, commands, or findings;
7. complete an `EXECUTION_RECEIPT` with concrete evidence of what ran;
8. update the Human Task and publish an `EXECUTION_REPORT_COMMENT` for a
   material checkpoint when a linked Issue and comment capability are available;
9. validate the result against the task acceptance criteria;
10. mark the task `COMPLETED` only after validation passes;
11. otherwise retry, select an approved fallback, replan, or mark `BLOCKED` with
   the exact reason.

Use these execution states for delegated work:

```text
PENDING -> READY -> RUNNING -> VALIDATING -> COMPLETED
                         |          |
                         |          +-> REWORK -> READY
                         +-> BLOCKED / REPLAN
```

`ASSIGNED` is never a completion state. A delegation without an execution
receipt is `NOT EXECUTED`.

Before non-trivial delegated execution, load:

- `references/harness-execution.md` for the execution state machine, receipts,
  retries, handoff and validation contract;
- `references/capability-registry.md` for capability selection and fallback
  rules;
- `references/provider-routing.md` when an executor LLM/provider must be
  selected or changed;
- `references/context-retrieval.md` when supplemental project context beyond
  routed normative sources is needed.

<!-- source-section:dev-workflow-standard:003 sha256:edb5d7644b293bc6ced7dbca41bf56cb3925f22ce877c5ad0c6a09eb042a0146 -->
## Mandatory Entry Gate

Invoke this skill before the first action of every development-related request.
It applies to product code and also to technical documentation, Git
status/branch/commit/push/merge, audit, QA, CI/CD, infrastructure, deployment
analysis, bug investigation, integration work and release delivery.

Documentation and Git are not workflow exceptions. Before changing, committing,
pushing or declaring anything delivered, the agent must:

1. inspect the source of truth, local branch, remote target and `git status`;
2. classify scope and applicable specialist skills;
3. create or resume the linked GitHub Issue for non-trivial work;
4. record consulted sources, `locked_paths`, validation commands and results in
   the task/Issue checkpoint; and
5. validate the exact remote reference being reported, not only a local file or
   another branch.

If any item is missing, keep the work in `Discovery / SDD` or `Blocked`. Do not
use a documentation-only or Git-only label to bypass this gate.

<!-- source-section:dev-workflow-standard:004 sha256:afcb2d8aecf50f0fa688753b2e9fa0c59da6cc1b93822e3792d5bdfe7e3e6af0 -->
## Hard Limits (non-negotiable)

- **Never write product code directly.** Implementation is executed through
  `dev-implementation-standard` or another explicitly approved executor
  capability selected by the harness.
- **Never confuse assignment with execution.** A task is not delegated until the
  selected capability actually runs and returns an `EXECUTION_RECEIPT`.
- **Never mark work complete from a prompt, plan, task assignment, terminal open,
  or claimed intent alone.** Completion requires result plus validation evidence.
- **Never skip the intent contract.** Every change needs explicit scope,
  acceptance criteria, validation, and evidence. Durable spec files are required
  only when the complexity tier below requires them.
- **Never create a task without sufficient intent and acceptance criteria.**
  Link durable specs when the tier requires them.
- **Reject any executable task that does not follow the mandatory task structure.**
- Repo docs, PRDs, mockups, architecture notes, and `AGENTS.md` are source of truth.
- If docs conflict with code, stop and ask for a decision.
- Inspect the real repo, git status, scripts, and runtime before changing environment.
- Keep changes scoped; preserve public APIs, schemas, payloads, and business
  rules unless explicitly approved.
- Do not call work complete without validation evidence.
- No deploy is approved without an approved PR.
- Final acceptance belongs to the user.
- **Never treat documentation, Git or delivery work as a workflow exemption.**
  The Entry Gate applies before reading technical state, changing Markdown,
  creating commits, pushing branches, opening PRs or reporting completion.

<!-- source-section:dev-workflow-standard:005 sha256:37a89374849b21c25406ea261ad565b5273fdab8ed83fd918842b136f3bf6445 -->
## Skill Roles (who does what)

| Skill | Role | Owns |
| --- | --- | --- |
| `dev-workflow-standard` | Engineering harness / final reviewer | demand, diagnosis, planning, capability routing, execution state, handoff, validation, recovery, approval |
| `dev-environment-standard` | Environment specialist | portable bootstrap, plugin health, MCP preparation, local environment state |
| `studio-prd` | Collaborative product briefing | new/existing product discovery, actors/journeys, module inventory and internal delivery plan |
| `sdd-spec-factory` | Requirements LLM | product/module/page/component/validation/API/DB specs, executable task, PR/QA checklists |
| `dev-implementation-standard` | Executor agent / coder | implement the approved task within scope, run commands, prepare PR |
| `ui-ux-standard` | UI/UX specialist LLM | layout, responsiveness, visual states, accessibility, design system, components |
| `qa-testing-standard` | Independent functional QA / test engineering | strategy, reproduction, behavior, regression, fix verification, QA_STATUS |
| `security-standard` | Security specialist LLM | authn, authz, tokens/session, sensitive data, inputs, permissions, insecure logs, external integrations |
| `devops-standard` | DevOps specialist | CI/CD, infrastructure, advanced releases, deployment operations, recovery and operational validation |

This skill coordinates them. It does not absorb their responsibilities.

<!-- source-section:dev-workflow-standard:006 sha256:ba7c9855fe4be221a70276f983bdfa0f5fb7e52bffaab55155f5fad98ffeb823 -->
## Practice Provenance

Do not present this repository's vocabulary as an OpenAI, Codex, or industry
standard without a primary source.

- **Consolidated practices:** repository-local source of truth, progressive
  disclosure, real tool execution, inspectable output, feedback loops,
  mechanical validation, and recovery.
- **Local architectural decisions:** the orchestrator agent does not write
  product code; the specialist skills remain independent; the eight-column
  Kanban model and declared human gates remain project policy.
- **Local extensions:** `EXECUTION_RECEIPT`, `EXECUTION_REPORT_COMMENT`,
  `SKILL_RECEIPT`, `REUSE_INVENTORY`, `MINIMAL_CODE_GATE`, `EXECUTION_HANDOFF`,
  the exact capability registry, and the execution-state vocabulary.

Local decisions and extensions may remain when they solve a real problem, but
must be named as local and validated against their intended outcome.

<!-- source-section:dev-workflow-standard:007 sha256:8643d43c2b2874a3b2afa38b20237f974fbba1e4f97556b6190de6c5a47b904b -->
## Task And Execution Context

Keep five execution artifacts distinct:

- **Human Task:** the complete GitHub Issue/card for human reading, including a
  glanceable summary, collaborative Discovery/SDD, normative requirements,
  microtasks, sector matrix, links, progress and evidence. A local Markdown is
  a mirror/fallback, never a replacement for an available Issue.
- **Execution Contract:** v2 structured LLM representation at
  `docs/execution/TASK-XXX.json`, with **normative equivalence** to the Human
  Task under the same `contract_revision`. Mutable evidence remains outside it.
- **Specs:** detailed functional and technical source of truth, loaded when the
  active scope requires them.
- **Execution Receipt:** evidence produced after the capability actually ran;
  it is never an execution input.
- **Execution Report Comment:** concise chronological human summary published
  to the linked GitHub Issue at material checkpoints; it never replaces the
  task, receipt, validation, Project state, or PR.

New executable tasks require a valid Execution Contract. A legacy task without
one remains readable, but must be normalized before it re-enters execution. Do
not mass-migrate inactive historical tasks.

Before sector delegation load `references/context-routing.md`. New contracts
use v2 with references, design context, microtasks and all ten sectors. Legacy
v1 remains readable. Every sector has REQUIRED/N/A, owner and dependencies,
and every N/A has a verified reason.
Each source has a purpose; CONDITIONAL adds a condition and OPTIONAL never
loads automatically. Separate planning prerequisites from final validation.
CODE_COMPLETE != TASK_COMPLETE; NO_EVIDENCE != PASS;
SECTOR_REQUIRED != OPTIONAL; OUTSIDE_OWNER != AUTHORIZED_TO_PASS;
CONTEXT_AVAILABLE != CONTEXT_REQUIRED. Only each owner attests its own PASS.
Harness reconciles all REQUIRED sectors, current receipts and criteria before
closing the Task. Missing sources, unresolved IDs/cycles or source conflicts
stop the affected checkpoint. This routing is a local extension, not an engine.

<!-- source-section:dev-workflow-standard:008 sha256:954518f80d558855096e8f8f28ecb66247f7199439cade46b82cb225f4d7cc41 -->
## Change Complexity Gate

Classify the work before choosing artifacts. Complexity changes documentation
depth, not the obligation to validate.

- `TRIVIAL`: a localized, low-risk change with no behavior, architecture,
  security, data, dependency, or public-contract impact. Use an inline intent
  contract: scope, acceptance criterion, command/check, and evidence. A durable
  spec, task file, and Issue are optional unless repository policy requires one.
  Keep the ten-sector matrix compact even inline; N/A rows need only a reason.
- `NORMAL`: bounded behavior or multi-file work with understood architecture.
  Use a concise Issue/task contract linked to the relevant existing docs; add a
  focused spec only for behavior that is not already specified.
- `COMPLEX`: architecture, cross-module behavior, migrations, sensitive data,
  security boundaries, substantial UI, integrations, or unresolved product
  decisions. Use durable SDD artifacts, executable tasks, traceability, and the
  applicable specialist gates.

When risk is uncertain, choose the higher tier. UI and security triggers are
based on affected surface and risk, not on the tier label.

<!-- source-section:dev-workflow-standard:019 sha256:18db48f2b11ac83cd320bba2820bab453e53a01bc0999d1a76e7d39b6223241e -->
## Context Budget Rules

### Project-local capability evolution

At task discovery/resumption, inspect the project's existing
`docs/ai-workflow/capability-registry.md` if present. Resolve only ACTIVE entries
relevant to the routed capability, with their approved scope, source revision
and current validation evidence. Read the selected SKILL.md completely and its
required references, recording the actual path/revision in SKILL_RECEIPT.
An index entry or file on disk is not proof of host discovery or execution.
Missing/stale/conflicting entries require review, never silent global fallback
or permission expansion. Do not load the entire local library.

When a verified gap triggers improvement, read
[Controlled continuous improvement](references/continuous-improvement.md).
Reuse, adapt, then create only if needed. Domain-specific lessons belong in
the client project, not the installed plugin cache. Specs, source references,
scripts and reusable skills have different owners; not every challenge needs
a skill. Keep global governance and acceptance gates intact. This is an
agent-executed protocol, not an autonomous self-modifying runtime.

- Do not paste whole files, docs trees, logs, or conversations into prompts.
- Prefer `task_id` plus `execution_contract_path` over task/spec bodies.
- Load the contract first, validate required fields and paths, then open only
  the active skill, routed JSON list, relevant global acceptance/constraints,
  required_sources, activated conditional_sources, code and dependency receipts.
- A mandatory reference must be read before changing the area it governs;
  progressive disclosure reduces redundant context, not necessary context.
- Use the Human Task for mutable status, blockers, results, and evidence without
  injecting it wholesale into the executor prompt.
- The Harness reads the full Task; specialists request justified context
  expansion if their slice is insufficient, not all docs preemptively.
- For large work, keep specs and research in files (`docs/specs/...`,
  `docs/modules/<module>/research.md`) and continue from those files.
- Load the references below only when directly needed.

<!-- end of selected V2 skill -->

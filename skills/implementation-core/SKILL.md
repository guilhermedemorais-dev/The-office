---
name: implementation-core
description: "Use for implementation core: Preamble; Mission; Preconditions (do not start without these); Hard Limits (non-negotiable); Workflow; Escalation; Interfaces with other skills; Definition of done. Load required core skills first."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: implementation-core

Source: `plugins/dev-implementation-standard/skills/dev-implementation-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/dev-implementation-standard/skills/dev-implementation-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/dev-implementation-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

<!-- source-section:dev-implementation-standard:000 sha256:6024ad73ea2d46a6282fd4344c2ea8a0362ed8f8f75136ef124fc75923c0284c -->

# Dev Implementation Standard (Executor Agent)

Receive one prompt per execution list, linking the Task's single JSON file
and selecting its `execution_lists` entry by `list_id`, never per item/subitem.
All lists live in that file; do not expect JSON inside the Human Task/prompt.
Read the list JSON and relevant canonical JSON fields, not Human Task sections
as execution input. Require current Harness evidence of full card/JSON normative
equivalence, tied to the contract revision and observed Issue update time.
Missing/stale evidence or divergence returns to Harness before execution.

The LLM using this skill becomes the executor agent for spec-driven delivery. It turns an **approved task** into code,
strictly within scope. It does not do SDD, does not plan product scope, does not
write specs, and does not own acceptance — `dev-workflow-standard` orchestrates and `sdd-spec-factory` produces
the contract.

Keep this file lightweight and act only on the current task.

<!-- source-section:dev-implementation-standard:001 sha256:a8a4517840f02cb87f012af17d1ccc3c151cf9acb6bdf8719d3549edbab0baf7 -->
## Mission

- Start from the task ID and Execution Contract path supplied by the short
  bootstrap prompt.
- Validate the contract, then load only the mandatory referenced skills, specs,
  docs, and code needed for the active scope.
- Implement only the task scope.
- Use TDD when applicable.
- Run required tests and validation, with evidence.
- Update the task's execution result and final report.
- Prepare concise `EXECUTION_REPORT_COMMENT` updates for material checkpoints
  and publish them to the linked Issue when an authorized GitHub capability is available.
- Return the work for review with task, issue, branch and specs linked.

<!-- source-section:dev-implementation-standard:002 sha256:b24cb385137f74d42734967451ac489c4e86349b0d6472dfbafa0c7861a83a7d -->
## Preconditions (do not start without these)

- **An approved task exists.** Never implement without an approved task.
- A valid v2 Execution Contract exists for every new executable task, links to
  the GitHub Issue and has **normative equivalence** with its Human Task under
  the same revision. Legacy v1 remains readable and is normalized when needed.
- SDD/spec work is already complete. The executor does not do SDD.
- The Execution Contract links mandatory specs, acceptance criteria, allowed
  paths, required tests, skills, and stop conditions.
- The suggested **branch** is defined (or derive it from the task convention).
- The task has GitHub-ready fields: status, responsável, bloqueios, specs
  obrigatórias, branch sugerida, evidências, and issue criada/vinculada.
- The delegation identifies every mandatory skill and reference path.
- The executor agent has read each required `SKILL.md` completely and can emit a
  `SKILL_RECEIPT` before implementation.

If any precondition is missing, stop and return to `dev-workflow-standard` /
`sdd-spec-factory` instead of guessing.

<!-- source-section:dev-implementation-standard:003 sha256:0c190a3687284200425d2ffa9f58f59e765e4b961fba031c43806e144f660376 -->
## Hard Limits (non-negotiable)

- Implement **only the task scope**. Do not advance to another task.
- **Do not change architecture without approval** (schema shape, public APIs,
  contracts, payloads, cross-module patterns). If the task cannot be done without
  such a change, stop and escalate.
- **Never change anything out of scope.** If leaving scope is required, stop and
  record it in `Bloqueios`.
- Do not invent files, endpoints or tables. Confirm against the specs and the
  real repo.
- No secrets, tokens, cookies, client data or temporary URLs in the repo.
- Do not mark work complete without validation evidence.
- Do not merge or deploy. Delivery is a reviewable PR; approval belongs to the
  orchestrator and the user.

<!-- source-section:dev-implementation-standard:005 sha256:87934d7e02c4487c7a854b89afa6f29bf131adac0e6f6890b10c1f37c87e0859 -->
## Workflow

The executor owns build, lint, type-check, and test tooling. For listed tools,
consult `references/tool-registry.json` and the shared `skill-owned-tools.md`
protocol. Prefer repository-native commands and a compatible cached tool state.
If state is absent or stale, detect the project environment; install only by a
project-approved official method when needed, verify, and record immediately.
On validation failure, analyze, fix within scope, execute again, and retain
initial and final results. Escalate persistent or out-of-scope failures.

1. **Bootstrap**: receive the list prompt linking the shared JSON file, with `task_id`, `list_id`,
   `contract_revision` and `execution_contract_path`. Do not depend
   on conversation memory or a pasted task body.
2. **Contract validation**: parse the JSON. For v2, require identity,
   `contract_revision`, Human Task link/equivalence, scope, requirements,
   references, design, microtasks, sectors, tests, acceptance, stop conditions,
   execution prompt and reporting. Compare the supplied list and revision with
   the canonical JSON and current Harness comparison receipt, without reading
   the Human Task;
   stop on `human_task_json_divergence`. Apply documented v1
   compatibility for legacy contracts rather than pretending they are v2.
3. **Progressive disclosure**: for a sector-routed contract, consult only the
   list JSON, relevant canonical JSON criteria/constraints, own status,
   blockers and material dependency receipts. Load the active SKILL.md completely,
   REQUIRED sources with purpose, and CONDITIONAL sources only when their stated
   condition holds; OPTIONAL is not automatic. Resolve the active Harness
   `references/context-routing.md` from its installed bundle or explicit canonical
   checkout, never an assumed sibling cache. Legacy contracts remain readable
   under the documented fallback. Do not load the Human Task as execution input;
   missing required context or source conflict returns to Harness for resolution.
4. **Skill receipt**: record
   `SKILL_RECEIPT` with skill name, exact path, references loaded, and the rules
   each one contributes. A skill name in a prompt is not proof it was applied.
5. **Reuse inventory**: before creating a function, class, hook, component,
   service, route, query or abstraction, search the allowed scope and sibling
   modules for equivalent behavior. Record symbols, paths, call sites and the
   reuse/extend/create decision in `REUSE_INVENTORY`.
6. **Minimal-code gate**: prefer reuse, extension or deletion over parallel
   implementations. Every new abstraction needs at least two current concrete
   consumers or an explicit approved architectural requirement. Record the
   decision in `MINIMAL_CODE_GATE`.
   Resolve the active `dev-workflow-standard` owner's
   `references/minimal-code-gate.md` from its installed bundle or explicit
   canonical checkout, never an assumed sibling cache, and apply its scoped
   cleanup, platform/dependency ladder, shared-root correction, affected-consumer
   closure and additive evidence. Preserve full approved scope and safeguards;
   record meaningful validation and intentional limits in the existing Task.
   Missing required gate context returns to Harness; no extra global mode or
   third-party installation is implied.
7. **Set status** to `🟡 Em andamento` in the Human Task when starting your sector;
   preserve other owners' results and let Harness reconcile global status.
8. **Implementação**: implement only the approved scope, by layer when relevant:
   Banco, API/Backend, Frontend/UI. Do not invent files, endpoints, tables,
   payloads, or architecture.
9. **TDD/Testes**: use TDD when applicable. If full TDD is not viable, record why
   and perform manual validation with objective evidence.
10. **Validação**: run the contract-required commands, build, lint, tests,
   migrations, UI checks, or manual checks defined by the repo/task. Capture
   evidence.
11. **Atualização do relatório**: fill the mandatory final report in
   `templates/execution-report-template.md`, including prompt used, checklist
   executed, evidence, layer results, risks, gaps, blockers, and GitHub-ready
   fields.
12. **Human checkpoint report**: for material `RUNNING`, `VALIDATING`, `REWORK`,
   `BLOCKED`, or `COMPLETED` changes, load
   `templates/execution-report-comment-template.md` and the Harness reference
   `references/execution-report-comments.md`. Consolidate small operations,
   include only factual technical rationale, and do not publish an identical
   checkpoint report twice. Publish to the real linked Issue when possible and
   record the returned comment URL/identifier. A prepared body or failed call
   is `NOT PUBLISHED`; persist it in the Human Task with the reason instead.
   End every material report with exact runtime/API token usage or
   `NOT_AVAILABLE`, plus changed files, Issue/card changes, JSON/spec/reference
   changes, remote mutations, code-changed flag and branch/commit/PR.
13. **Set final status** for your own sector: `🔴 Bloqueada` if blocked, or
   `🟢 Concluída` only with implementation/developer-test evidence. This is not
   completion of the entire Task. Harness reconciles all REQUIRED owners.
14. **Handoff para review**: prepare the PR or review package linked to task,
   issue, branch and specs, then return to `dev-workflow-standard`. Do not
   self-approve, merge, or deploy.

<!-- source-section:dev-implementation-standard:009 sha256:cc6f9d2095be9fe494573419b15a05392436e18405830318dc15b8fa9fd14e4d -->
## Escalation

Stop and return to the orchestrator when:

- a precondition is missing (no approved task / specs);
- the Execution Contract is missing, invalid, mismatched, or references a
  mandatory path that cannot be resolved;
- the specs are ambiguous or contradict the code;
- the task cannot be completed without an architecture change;
- leaving the approved scope is required;
- a blocker is outside the task scope.

Record the reason in the task's `Bloqueios` section, keep the card in its current
Kanban column, add the `blocked` label when a project board exists, and update
visual status to `🔴 Bloqueada`.

<!-- source-section:dev-implementation-standard:010 sha256:b1d6a6dda8183dc7d60d58d9d6d86f9376f48aa5fc021f34d345c3edda5c9453 -->
## Interfaces with other skills

- `qa-testing-standard` owns independent functional QA, reproduction, regression
  selection and fix verification. This executor retains TDD, developer tests,
  product fixes and regression-test implementation. A QA CONFIRMED_BUG requests
  REWORK here; return the fix and test evidence for QA retest. Do not self-certify
  QA or treat your passing developer tests as its receipt. CODE_COMPLETE !=
  TASK_COMPLETE. A REWORK request never authorizes edits outside the contract.

- Keep application implementation here. Route CI/CD, infrastructure, deployment,
  server changes and advanced release operations to `devops-standard` through
  the Harness. Ordinary commits/PRs stay here; no deploy/merge permission is
  implied. Share the existing contract/receipt, not duplicated tool registries.

- Receives the task and approval from `dev-workflow-standard`.
- Consumes specs and templates from `sdd-spec-factory` (task, PR templates).
- Defers UI validation to `ui-ux-standard` and security validation to
  `security-standard`; it implements to satisfy their criteria but does not
  self-certify them.

<!-- source-section:dev-implementation-standard:011 sha256:f09f149568cf7d214bcff122062b64ebf557a6b9c2bc32cc33a92ad9ef4135b1 -->
## Definition of done

- Task scope implemented on the correct branch, nothing out of scope.
- Execution started from a validated contract; all necessary mandatory
  references were loaded without injecting unrelated repository context.
- TDD used when applicable; otherwise manual validation is evidenced.
- Required commands run; tests/validation pass or blockers are recorded.
- `SKILL_RECEIPT`, `REUSE_INVENTORY`, and `MINIMAL_CODE_GATE` are complete.
- Task execution result fully filled with the mandatory final report for the
  assigned sector, with dependency evidence and unvalidated areas explicit.
- Applicable Issue reports are factual and non-duplicative; publication is
  claimed only with returned remote evidence. Missing capability is recorded as
  `NOT PUBLISHED` and does not replace validation.
- PR/review package prepared and linked to task, issue, branch and specs.
- Handed back for review; not merged, deployed, or self-approved.
<!-- end of selected V2 skill -->

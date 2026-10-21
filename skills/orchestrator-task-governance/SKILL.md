---
name: orchestrator-task-governance
description: "Use for orchestrator task governance: Mandatory Task Governance; Official Kanban Method; Definition of Entry / Exit; Repository Readiness Bootstrap; GitHub-Ready Task Structure; Recommended Task Template. Load required core skills first."
---

# The Office V2: orchestrator-task-governance

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
- `references/client-portal.md`: `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/client-portal.md`

<!-- source-section:dev-workflow-standard:010 sha256:52c2b3a68558310db8299669a35b69b0de59b3c23333a77dbb5673b2f9a86997 -->
## Mandatory Task Governance

### Complete module as the default Task unit

Use one complete Task per functional module within the approved demand. A
module is a coherent business capability with an end-to-end outcome, not a
technical layer, workflow phase, specialist assignment or arbitrary folder.
For changes to an existing module, cover the requested outcome completely;
do not expand scope to rebuild unrelated parts of that module.

Keep spec, database, backend, frontend, TDD, independent QA, security and
documentation as microtasks and gates inside the same Task. Preserve sector
owners, dependencies, evidence and justified N/A. Size, token budget, context
limits, specialist handoffs and review convenience do not justify separate
Tasks; use internal microtasks and resumable checkpoints instead.

Require Markdown checkboxes (`- [ ]`) for each actionable checklist item in
every stage, microtask and REQUIRED sector. Complex items may have nested
checkbox subitems within the same Task; this internal decomposition is allowed
and does not create separate Tasks or Issues. Check `- [x]` only after the
responsible owner records completion evidence. A parent stays unchecked until
all applicable children are evidenced; blocked or unvalidated items stay
unchecked with their reason. Checked items do not approve a sector, Issue,
merge or deploy automatically. Keep progress in the Human Task and evidence
ledger, not as mutable checkbox state in the normative JSON.

Each execution checklist/list has one prompt containing a clickable link to
the Task's single JSON file and its `list_id`, not a prompt per item/subitem.
Keep all list objects in `execution_lists` inside that same canonical file,
with the Task's shared context. Never embed JSON in the Human Task or create
one JSON file per list. This applies to microtask, stage and sector lists.
Give each list a stable ID, owner and phase; task identity/revision come from
the shared file. Use a real local-file link or versioned GitHub file link,
not a link to an Issue or an invented URL.
Validate list completeness, owner, dependencies and inherited scope/constraints
before handoff. See `references/context-routing.md` for the transport contract.
Harness compares the complete Human Task and canonical JSON. Specialists read
the list JSON and necessary canonical JSON fields, their skill, mandatory
sources and relevant code, not the Human Task as an execution input. Missing
context returns to Harness for a corrected JSON handoff; do not send the human
card as a substitute. Human approval gates are recorded only when observed.

Before requesting Task generation and before accepting its output, inspect
proposed and relevant existing Tasks by module, scope and acceptance outcome,
not titles alone. If Tasks for the same module are separated only into
"spec", "backend", "frontend", "QA" or "implementation" (including synonyms
or renamed fragments), stop generation/handoff and require consolidation into
one complete module Task. Report the affected IDs/titles, missing end-to-end
coverage and required consolidation. Do not mark the plan ready or silently
approve, close or rewrite existing Issues.

The only separation exceptions are production migration, cutover, destructive
operation, or a genuinely independent delivery requiring its own authorization
and rollback. Require a documented boundary, independent acceptance criteria,
dependencies, explicit authorization gate and rollback plan for each exception;
a different owner, phase or layer is not an independent delivery. An ordinary
development schema migration remains a microtask of its module.

This is a pre-generation and output-validation criterion. Keep the existing
Task template structure and existing contract fields; add execution_lists in
the single canonical JSON file for list routing, preserving legacy reads. Render its
action checklists with checkboxes and nested items when needed. Apply it to the active
demand; do not mass-migrate historical Tasks.

Every non-trivial feature must follow the official order: sufficient intent or
spec first, executable task second, implementation third. The orchestrator
rejects any task that lacks the artifacts required by its complexity tier,
mandatory fields, or objective review criteria.

A valid task must contain, at minimum:

- Título
- Status visual
- Tipo
- Prioridade
- Objetivo
- Specs obrigatórias
- Docs obrigatórios
- Execution Contract
- Arquivos e módulos permitidos
- Fora do escopo
- Estado atual encontrado
- Resultado esperado
- Regras obrigatórias da implementação
- Checklist de execução
- Prompt para o executor
- Condições de parada
- Testes obrigatórios
- Evidências esperadas no PR
- Critérios de aceite
- Banco
- API/Backend
- Frontend/UI
- Validação
- Riscos/Lacunas
- Resultado da execução
- Matriz de Validação por Setor, Fontes globais da verdade, Ordem de Execução
- Registro de Evidências, Gate do PR, Gate Final, Aceite Humano

Legacy layer names remain recognizable; for new tasks the ten-sector matrix
replaces redundant N/A detail sections. Required sectors use the canonical SDD
block with purpose-based sources, expected evidence and owner results.

The task filename remains stable for traceability. Do not put visual status,
emojis, Kanban status, or transient workflow state in the physical filename.
Status belongs in the task content only.

<!-- source-section:dev-workflow-standard:011 sha256:902c9016517818643b202b333d9743807e1a9043d7c07b0c55f920285874b3ea -->
## Official Kanban Method

Use these columns as the global workflow status:

1. Backlog
2. Discovery / SDD
3. Ready for Dev
4. In Progress
5. Validation
6. In Review
7. Awaiting Final Approval
8. Done

Column means process step. Label means condition or classification. Do not create
a blocked column. A blocked card stays in its current column with the `blocked`
label and a blocker recorded in the task. If review fails, move the card back to
`In Progress` and add the `rework` label until the rework is resolved.

Recommended labels:

- `blocked`
- `needs-info`
- `rework`
- `high-priority`
- `bug`
- `feature`
- `tech-debt`

<!-- source-section:dev-workflow-standard:012 sha256:36bca45abd86431c16d03e74334be4f3132a7efb616c6e2f90e014955f377aa5 -->
## Definition of Entry / Exit

Definition of Entry is what must be true before a card enters a column.
Definition of Exit is what must be true before a card leaves a column. The
orchestrator must use these definitions as gate checks.

| Column | Definition of Entry | Definition of Exit |
| --- | --- | --- |
| Backlog | Demand, bug, idea, or risk captured as an item. | Item has enough context to enter Discovery / SDD, or is intentionally rejected/archived. |
| Discovery / SDD | Backlog item selected for clarification, source-of-truth review, and spec work. | Required specs exist, scope is clear, risks are known, and an executable task can be created. |
| Ready for Dev | Executable task exists, mandatory specs are linked, allowed files/modules are defined, branch is suggested, acceptance criteria and tests are clear. | Executor starts the approved task and updates task status to `🟡 Em andamento`. |
| In Progress | Executor accepted the task, read its list JSON, canonical JSON context and required sources, and is implementing only the approved scope. A material `RUNNING`, `REWORK`, or `BLOCKED` checkpoint is reported to the linked Issue when available. | Implementation and developer evidence are ready for independent validation. |
| Validation | Technical review package links task, specs, evidence and receipt; relevant implementation is available. | Required specialist validations pass and review package is prepared for PR. |
| In Review | PR exists with task, specs, evidence, receipt, and applicable Issue report linked. A `VALIDATING` report records the review handoff. | CI and required reviews pass; advance to Awaiting Final Approval, or return to In Progress with `rework` and an actionable report. |
| Awaiting Final Approval | Required technical validations pass and human decision is pending; identify whether this is a local package or published PR. | Human approval and human merge are observed; no automatic merge. |
| Done | Human merge observed, required validations evidenced, and no unresolved blocker remains. | No normal exit; archive only when historical tracking is no longer useful. |

A local `COMPLETED` execution checkpoint is not a merged Task or permission to
move its card to Done. Default maximum is three automatic rework cycles, then
stop with diagnosis and `BLOCKED`; do not retry unchanged permission failures.

<!-- source-section:dev-workflow-standard:013 sha256:3d9d7805b0dc9d3b470f973136810760e9354cba190b714218bd5ac471034468 -->
## Repository Readiness Bootstrap

When organizing a client project's folders, include portal preparation in the
onboarding plan and read [Client portal](references/client-portal.md). The
destination is `docs/portal/` in that project, not the plugin cache. An external
template repository may be supplied later: record that pending dependency and
continue unrelated work; never invent a URL, substitute a reference website,
or claim the portal installed. Route approved preparation/Pages configuration
to DevOps, preserving the separate backend and publication gates.

Before the first Task requiring remote governance, route repository onboarding
to `devops-standard` and load its `references/github-governance.md`. Environment
prepares Git/gh; DevOps owns diagnose/propose/confirmed apply/verify. Authentication
handoff is human, never a request for tokens in chat. Authentication, repository
access, administration, organization and Project permissions are separate gates.

Require an existing EXECUTION_RECEIPT with target/revision, current verification,
applicable capabilities, proposal/confirmation, actual mutations, limitations and
readiness. `READY`/`READY_WITH_LIMITATIONS` from governance are scoped results, not
new global execution states. Environment/auth/access/files/remote governance/
Project/CI/human gates must be evidenced; explicit N/A and approved sufficient
fallbacks must be justified. Missing required evidence is not a limitation waiver.
`PROJECT READY != PRODUCTION AUTHORIZED`; never equate configured with enforced.

Reuse compatible evidence after onboarding. Repeat only for drift, relevant
change, actual failure or explicit request, not full bootstrap before every Task.
Repository governance makes DevOps REQUIRED; trigger Security for permissions,
secrets/IAM or equivalent risk. QA may be N/A for pure remote configuration with
reason, but deterministic helper behavior changes require independent QA.

<!-- source-section:dev-workflow-standard:014 sha256:31199c90f1058c54823f3d4fa202c4a2df6ffcdf3b0e539bf238ee4dedaf2b87 -->
## GitHub-Ready Task Structure

Do not assume GitHub Projects, Issues, or boards are available. Prepare each task
so it can be mapped later without restructuring:

- one issue per task when the project uses GitHub Issues;
- labels from the recommended label set above;
- optional milestone when the task belongs to a phase, release, or checkpoint;
- branch sugerida recorded in the task;
- status field consistent with the official Kanban columns;
- explicit fields for responsável, bloqueios, specs obrigatórias, branch
  sugerida, evidências, issue criada/vinculada, and `Pronto para GitHub Projects`.

<!-- source-section:dev-workflow-standard:015 sha256:805010e30f23a1cf2bfe193bb235f31f8132b78678fb3d5628a2605680e896ef -->
## Recommended Task Template

Use `plugins/sdd-spec-factory/templates/task-template.md` and its matching
`execution-contract-template.json`; do not maintain a second template here.
Resolve the active SDD bundle in installed hosts, not a sibling cache path.
The template keeps identity/status, ten sectors, scoped source purposes,
acceptance, execution order, evidence and human gates. Only REQUIRED sectors
need detailed sections. See `references/context-routing.md` for compatibility.

<!-- end of selected V2 skill -->

---
name: sdd-task-contracts
description: "Use for sdd task contracts: Fase 3 - Geração de Task Executável. Load required core skills first."
---

# The Office V2: sdd-task-contracts

Source: `plugins/sdd-spec-factory/skills/sdd-spec-factory/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, sdd-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/sdd-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/sdd-spec-factory/skills/sdd-spec-factory/`;
for plugin templates/scripts absent there, use repository root `plugins/sdd-spec-factory/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

Canonical link resolution (repository-relative paths, not skill-directory-relative):
- `references/spec-consistency-analysis.md`: `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/spec-consistency-analysis.md`

<!-- source-section:sdd-spec-factory:012 sha256:69edad988ff4e33182680ca4af5bf05a9cbea5d6a7ef183976b9badf632f98f1 -->
### Fase 3 - Geração de Task Executável

Load the active Harness `references/context-routing.md` before designing the
sector matrix. In this monorepo its source is
`plugins/dev-workflow-standard/skills/dev-workflow-standard/references/context-routing.md`;
installed hosts resolve the active skill, never assume sibling cache paths.
If unavailable, use an explicitly available canonical checkout or return the
missing reference to the Harness before producing a conflicting contract.

Run the module-boundary gate below before generating Tasks, then validate the
generated set with the same gate before publication or handoff.

#### Module-boundary gate

1. Identify each functional module and its approved end-to-end outcome. Group
   proposed and relevant existing Tasks by scope, dependencies and acceptance
   criteria, not titles or folders alone. A module is a coherent business
   capability, not a layer, phase or specialist. For an existing module, cover
   the requested change completely without rebuilding unrelated functionality.
2. Plan one complete Task per module. Put spec, database, backend, frontend,
   TDD, independent QA, security and documentation into its existing microtasks
   and sector matrix. Preserve owners, dependencies and evidence; justify N/A
   where a discipline does not apply. Separate specs are supporting documents,
   not a reason to create separate spec-only Tasks.
3. Reject Tasks for the same module separated only into "spec", "backend",
   "frontend", "QA" or "implementation", including synonyms and renamed
   fragments. Stop generation/publication/handoff, list affected IDs/titles
   and missing end-to-end coverage, and require consolidation into one complete
   module Task. Do not declare the output ready until it passes a fresh check.
   Detect relevant existing fragments without automatically approving, closing
   or rewriting their Issues or mass-migrating historical Tasks.
4. Allow separation only for production migration, cutover, destructive
   operation, or a genuinely independent delivery requiring its own
   authorization and rollback. Document each exception's boundary, independent
   acceptance criteria, dependencies, explicit authorization gate and rollback
   plan in existing fields. Missing justification blocks generation; size or
   different specialists do not qualify. An ordinary development schema
   migration remains a module microtask.
5. Validate the complete output set, not just each card in isolation: every
   module has its full approved outcome covered by one Task, all applicable
   disciplines are microtasks, and each separated exception is justified.
   Recheck Human Task/JSON equivalence after consolidation. Keep the Task
   template structure and existing contract fields; keep execution_lists in
   the same JSON file and preserve legacy reads. Render action
   checklists with checkboxes as specified below.

Examples: "Orders spec" + "Orders backend" + "Orders frontend" + "Orders QA"
must consolidate into one Orders Task, even if renamed as sequential phases.
One Orders Task with those microtasks passes. Orders and Inventory may be
distinct Tasks when they are genuinely distinct functional modules. A separate
production data cutover needs the documented authorization and rollback above;
calling a backend fragment an "independent delivery" does not make it one.

Produce one reviewable, complete GitHub Issue/card per module using
`templates/task-template.md` and one equivalent v2 JSON contract using
`templates/execution-contract-template.json`:

- Link the mandatory specs.
- Link the GitHub issue (or state that one must be created).
- Suggest the branch name (e.g. `feat/<modulo>-<resumo>`,
  `fix/<modulo>-<resumo>`).
- State the expected PR.
- Include acceptance criteria.
- Include mandatory tests (TDD when applicable).
- Include what is out of scope.
- Link the contract as `docs/execution/TASK-XXX.json`.
- Run Discovery/SDD collaboratively: ask the user critical questions, research
  authoritative references, consolidate decisions, then publish a
  `DISCOVERY_SDD_COMPLETED` Issue comment before requesting human approval.
- Keep validated sources in `docs/biblioteca-referencias/` and route the exact
  file/section and purpose. When UI applies, route the Design Guide, tokens,
  component library, visual references and approved mockup under `docs/design/`.
- Decompose execution into microtasks with owner skill/plugin, capability,
  preferred tool, dependencies, exact references, allowed paths, checklist,
  deliverables, completion condition and independent validator.
- Materialize the selected execution routes in the Task and equivalent JSON,
  not only in a Discovery comment. Use existing microtask owner/plugin,
  capability, preferred_tool and reference fields; put necessary auxiliary
  tool identifiers, purpose, conditions and approved fallback in list
  instructions or purpose-qualified required references. Each execution list
  resolves its microtask_ids in the same contract. Do not paste the inventory
  or full skill bodies. The executor starts from this selection plus mandatory
  canonical skill/source reads; expand discovery only for gaps, failures,
  changed availability or new needs. Return normative changes to Harness.
- Render every stage, microtask and REQUIRED-sector action checklist as Markdown
  `- [ ]` items, not semicolon-separated prose or uncheckable numbered steps.
  Split complex items into nested checkbox subitems inside the same Task.
  Give each leaf an observable completion condition; do not create new Tasks
  or Issues for these internal steps. New items start unchecked. Mark `- [x]`
  only with the responsible owner's completion evidence; a parent requires all
  applicable children completed. Blocked/unvalidated items stay unchecked with
  reasons; justified N/A is not a completed action. Human approval gates remain
  separate. Keep checkbox progress in the Human Task/evidence ledger, while
  normative actions remain equivalent in the existing JSON checklist fields,
  without adding mutable checked-state fields.
- Generate one prompt per execution checklist/list (microtask, stage or sector).
  Each prompt contains a clickable link to the single Task JSON file and the
  selected `list_id`. Put all list objects in that file's `execution_lists`,
  beside the global contract. Never embed JSON in the Human Task, attach its
  body to the prompt, or create separate JSON files per list. Use a real local
  file link or versioned repository URL. Never generate a prompt per checkbox
  or nested subitem. Preserve task identity/revision at file level and each
  list's owner, phase, complete checklist/subitems and microtask references.
  Global scope, protected paths, acceptance, tests, sources and stop conditions
  remain mandatory through that contract. Check every prompt link resolves to
  the same Task file, every list ID resolves exactly once, and list actions and
  applicable microtask checklists agree with no omitted requirements or wrong owner.
  The file is a detailed execution contract, not merely a routing index: each
  list specifies objective, scoped actions, dependencies, exact required sources
  and their purposes, allowed/protected paths, expected deliverables, observable
  completion conditions, tests, acceptance and stop conditions. Resolve relevant
  requirements/business rules and input/output, error and negative-path
  expectations from the global contract/specs. Reference IDs are acceptable only
  when they resolve to concrete instructions in the same file or required sources.
  Never require the Human Task to discover an omitted execution rule. Reuse
  global constraints without copying unrelated context into every list. Unknown
  stack, paths, commands or product decisions remain explicit blockers, never
  invented detail or empty fields presented as ready. No detail level alone
  proves quality; execution and independent validation remain required.
  Use the active Harness `references/context-routing.md` transport rules.
  Harness alone compares the full Human Task and JSON. Specialists execute
  from the supplied JSON plus mandatory skill/spec/code reads; do not require
  them to read the Human Task or its sections as execution input. Missing or
  conflicting JSON returns to Harness. A Human Task reference is provenance,
  never permission to substitute prose for missing JSON instructions.
- Make `Prompt para o executor` the Harness bootstrap for the full Task and
  its per-list prompt/JSON handoffs. Specialists verify task/list identity,
  contract revision and current Harness evidence of card/JSON equivalence, load routed
  skills/references, stops on divergence, collects receipts, publishes material
  comments, and forbids merge/deploy without explicit authorization.
- Record planned validations in the Human Task with owner skill, capability,
  and preferred tool when known. Put only those compact identifiers in the
  Execution Contract `required_validations`; never store installation state,
  official URLs, executable paths, or logs there.
- Include all ten standard sectors with REQUIRED/N/A, concrete owner,
  dependencies and a short verified N/A reason. Detail only REQUIRED sectors;
  each has objective, sources with purpose, checklist, expected evidence and
  result placeholder. No generic full OWASP/QA checklist on unrelated tasks.
- Use v2 `sectors`, normative references and microtasks in new contracts. Human
  card and JSON share `contract_revision`; any normative change updates both.
  Mutable status, receipts, logs and execution evidence do not belong in JSON.
- Separate final `depends_on` from optional `planning_depends_on`. QA, Security
  and UI planning may start early; only executed validation closes their gates.
  Check unknown IDs, owners, missing required references and cycles before handoff.
- Give the Harness the complete Human Task; give each specialist its list JSON,
  canonical JSON sector/global constraints/acceptance, necessary code and dependency
  receipts. Missing context requests expansion, not loading all sources by default.
- For behavioral changes, bugfixes, APIs, user flows, business rules, persistent
  state, payments, tenancy, imports/exports, integrations or concurrency, route
  independent QA planning to `qa-testing-standard`. It returns QA_GUARDRAILS,
  TEST_SCENARIOS, REGRESSION_TARGETS and VALIDATION_REQUIREMENTS proportionally.
  Docs/metadata-only work may record QA N/A; pure visual changes still require UI.

The Execution Contract must be valid JSON and include the v2 identity/revision,
human task link and equivalence declaration, summary/goal/discovery, current and
expected state, scope, protected and allowed paths, requirements, business
rules, references, design, microtasks, ten sectors, tests, acceptance criteria,
stop conditions, ignition prompt and reporting contract. Keep structure concise;
do not copy source bodies, conversation history, secrets or execution evidence.

Before `DISCOVERY_SDD_COMPLETED`, publication/handoff or Ready for Dev, apply
[spec consistency analysis](references/spec-consistency-analysis.md) to the
current artifacts. This refines the existing coverage/equivalence checkpoint,
not a new state, Task or approval gate. Return blocking findings to their source,
reconcile affected specs/card/JSON and recheck before claiming readiness.

Tasks live under `docs/tasks/TASK-XXX-<slug>.md` (or the repo's existing task
location, if one exists — reuse it, do not duplicate).

Execution Contracts live under `docs/execution/TASK-XXX.json` unless the
repository already has an equivalent canonical location.

For a legacy task without a contract, keep it readable. When it re-enters
execution, generate and validate its contract before implementation. Do not
mass-migrate historical tasks.

<!-- end of selected V2 skill -->

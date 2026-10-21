---
name: product-planning
description: "Use for product planning: Produce the project artifacts; Plan and hand off under supervision. Load required core skills first."
---

# The Office V2: product-planning

Source: `plugins/studio-prd/skills/studio-prd/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, product-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/product-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/studio-prd/skills/studio-prd/`;
for plugin templates/scripts absent there, use repository root `plugins/studio-prd/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

Canonical link resolution (repository-relative paths, not skill-directory-relative):
- `assets/briefing-template.md`: `plugins/studio-prd/skills/studio-prd/assets/briefing-template.md`
- `assets/prd-template.md`: `plugins/studio-prd/skills/studio-prd/assets/prd-template.md`
- `references/planning.md`: `plugins/studio-prd/skills/studio-prd/references/planning.md`
- `assets/plan-template.json`: `plugins/studio-prd/skills/studio-prd/assets/plan-template.json`

<!-- source-section:studio-prd:002 sha256:507ac4465ee26f6acdeafdb644784cbb4d44ad7dc52be2a5bdc137ff8e6ca6e8 -->
## Produce the project artifacts

Keep artifacts in the **client project**, not this plugin; reuse equivalent
existing locations and preserve content:

- `docs/briefing/briefing.md`, using [the briefing template](assets/briefing-template.md).
- `docs/prd/PRD.md`, using [the PRD template](assets/prd-template.md).
- `docs/planejamento/plano-de-execucao.json` and `.md`, following
  [planning.md](references/planning.md) and [the JSON template](assets/plan-template.json).
- Research in `docs/biblioteca-referencias/`, with exact project file, origin,
  revision, purpose, relevant code/schema/tests and coverage limits.

PRD explicitly counts approved modules and gives each a stable ID, functional
boundary, actors, dependencies and corresponding task when available. Record
actor → journey/scenario → rule → source/decision → acceptance traceability.
Confirm modular-monolith architecture rather than imposing it on every project.

One complete task per functional module. DB, backend/API, frontend, UI/UX,
security, QA and documentation are microtasks in that task, not task fragments.
Tokens, phases and specialist changes do not justify splitting it. Corrections
to meet existing acceptance remain in the same task. Independent/out-of-scope
demands or separately authorized hazardous operations require an explicit
boundary and user decision. Preserve the existing SDD template and equivalent
JSON v2, including all ten sectors; do not invent a Studio task template.

The target is production quality within the agreed complete scope, **not an
automatic MVP**. Delivery stages do not waive tests, negative states, security
or polish. Do not promise complete discovery, zero rework or guaranteed dates.

<!-- source-section:studio-prd:003 sha256:bbe8a247c42cb51ca8497a9f09e37d9f413d4dce1d6e45b1ac2fb97428547f7e -->
## Plan and hand off under supervision

Read [planning.md](references/planning.md) before estimates or handoff.
Urgency cannot silently override prerequisites. Explain feasible alternatives
and the minimum capability needed, not necessarily an entire dependency module.
The internal MD plan is for the developer's agenda and resource decisions,
not a client proposal. JSON carries the same revision and normative decisions,
but is not the per-task execution contract.

Use the bundled plan helper to validate dependency/order invariants and render
the matching human MD. Its success proves structural consistency only, not
business correctness, real links or authorization. Keep a short contextual
tech-lead prompt for each task, not a second per-list execution protocol.

After approval of PRD, module inventory and order, offer:
“PRD aprovado: N módulos. Sequência definida conforme dependências e prioridades.
Estou pronto para iniciar a especificação da primeira task: [módulo]. Posso começar?”
Wait for that instruction. Route that module to available `sdd-spec-factory`;
if unavailable, report the missing capability, do not pretend it ran. SDD owns
full research/specification including backend. Resolve material gaps with the
user, report coverage and open decisions, then seek approval before the next
module. PRD approval does not authorize implementation, merge or deploy.

For modules with UI, route `ui-ux-standard` to maintain the project's Markdown
Design Guide, design tokens and navigable live HTML component/widget catalogue
during SDD. Record component IDs/revisions, variants, responsive/keyboard
behavior and labelled fixtures. Prefer the real shared project components.
Visual examples do not prove backend behavior. Reuse sources instead of
repeating the same reverse engineering for every frontend task.

For any selected library edition/item, require usable zero-license-cost rights;
paid Pro/Enterprise assets are excluded and unknown cost/license is not eligible
until verified. Preserve item/subtree restrictions, not a whole-repository guarantee.

For every PRD/spec, retain a compact record in its existing references section:
applicable catalog indexes/metadata consulted and revision, selected source ID or
project-native reuse, or N/A with reason. Unavailable/stale evidence is NOT_VALIDATED,
never an invented consultation. Metadata review does not load every source body;
only selected necessary sources become REQUIRED. Preserve the Harness whole-inventory rule.

When UI libraries are relevant, keep catalog-first selection with UI/UX ownership:
project-native first, curated matching-stack candidates second, targeted Context7
or official GitHub research only for gaps. Record the stable library/source ID,
official repo/docs URL, observed version/commit or UNKNOWN, component path/variant,
purpose/module, license, dependencies, adaptations and decision state in the PRD's
existing reference/design section. PROPOSED/UNKNOWN is valid during briefing; never
invent pins. Carry the same source ID into module SDD and its Task. Resolve the
active ui-ux-standard references/library-source-handoff.md when needed, without
assuming sibling cache paths or loading the whole catalog. No standalone library
skills or blanket dependency installation follow from the catalog.

Portal requests go to the active Harness `references/client-portal.md` and
DevOps: external template into client `docs/portal/`, not a portal bundled here.
An unavailable future template is a recorded dependency, not permission to
build it or block unrelated modules.

<!-- end of selected V2 skill -->

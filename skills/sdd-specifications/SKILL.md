---
name: sdd-specifications
description: "Use for sdd specifications: Consultative Technical Knowledge Routing; Fase 2 - Geração de Specs. Load required core skills first."
---

# The Office V2: sdd-specifications

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
- `references/technical-knowledge-router.md`: `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-knowledge-router.md`
- `references/technical-architecture.md`: `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-architecture.md`
- `references/technical-data-concurrency.md`: `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-data-concurrency.md`
- `references/technical-auth-sessions.md`: `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-auth-sessions.md`
- `references/technical-apis-jobs.md`: `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-apis-jobs.md`
- `references/technical-quality-operations.md`: `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-quality-operations.md`
- `references/technical-fiscal.md`: `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-fiscal.md`
- `references/devops-planning.md`: `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/devops-planning.md`

<!-- source-section:sdd-spec-factory:006 sha256:671bb8895cfa266c804e8cb430d274dcd36abb8b6e63180fd02b0b5fe1842002 -->
## Consultative Technical Knowledge Routing

For NORMAL/COMPLEX modules, before finalizing technical specs, read [Technical Knowledge Router](references/technical-knowledge-router.md). Select only the domains triggered by the changed surfaces and risk; inspect current code, tests, architecture, version-matched official sources and existing specialist references. Record decision alternatives, provenance, negative/positive tests and unresolved blocking decisions in the existing specs, Human Task and equivalent JSON fields. Never infer project behavior or tax/regulatory rules. The resulting PR must carry a concise Engineering Explanation linked to evidence. This is not a new schema or a reason to load every technical reference.

Conditional topic references, load only those selected by the router:
[architecture](references/technical-architecture.md),
[data/concurrency](references/technical-data-concurrency.md),
[auth/sessions](references/technical-auth-sessions.md),
[APIs/jobs](references/technical-apis-jobs.md),
[quality/operations](references/technical-quality-operations.md),
[fiscal](references/technical-fiscal.md).

If the selected knowledge is missing, stale or insufficient, follow the router's
knowledge-gap research/update procedure. Persist verified findings in the owning
reference library and reuse them by source/version/purpose; never invent patterns
or treat a saved reference as executed validation. Use existing continuous
improvement ownership rules for cross-project plugin updates.

<!-- source-section:sdd-spec-factory:011 sha256:6a7e5eaf5373b92e769426c9b2f6049e08d07c4ff0b933401256cb1c92bd5061 -->
### Fase 2 - Geração de Specs

When dependencies are selected/changed or security boundaries apply, route
early planning to `security-standard` and its preventive security research
reference. Incorporate applicable OSV advisories and versioned ASVS controls
as explicit rules, enforcement points and negative tests in the existing
module Task/security sector. Reuse the project dependency/source inventory;
do not claim a planned control or advisory match proves runtime security.

When UI applies, route `ui-ux-standard` and its `references/live-design-guide.md`
from the active bundle (or explicit canonical checkout, not guessed sibling
cache paths). Before closing frontend specs, require the client project's
Markdown Design Guide plus cumulative HTML catalogue or mapped existing
equivalent, tokens, source inventory and the applicable visual approval.
Extend the same catalogue while specifying each module. Route exact component
IDs/revisions, catalogue anchors, rules, fixtures and limitations through the
existing design/references fields of the Human Task and equivalent JSON.
Missing catalogue/approval blocks frontend readiness, never becomes a fictitious
PASS or a separate frontend Task. Backend-only work records UI N/A.

For selected UI libraries, preserve the PRD's stable library/source ID in the
frontend/component spec and Human Task. Retain official repository/docs, exact
version/commit or UNKNOWN, component path/variant, purpose/module, license,
dependencies, adaptations and decision state. Reuse native UI first, curated
matching-stack candidates second, targeted Context7/official GitHub research for
gaps. Resolve active ui-ux-standard references/library-source-handoff.md only when
needed; no assumed cross-plugin paths or global catalog loading. Map the same
source ID into existing JSON references and REQUIRED sources only for selected,
necessary dependencies. Resolve material UNKNOWN choices before execution;
nonselected candidates do not become mandatory references. No new schema/gate,
standalone library skill or automatic per-project dependency installation.

For any selected library edition/item, require usable zero-license-cost rights;
paid Pro/Enterprise assets are excluded and unknown cost/license is not eligible
until verified. Preserve item/subtree restrictions, not a whole-repository guarantee.

For every PRD/spec, retain a compact record in its existing references section:
applicable catalog indexes/metadata consulted and revision, selected source ID or
project-native reuse, or N/A with reason. Unavailable/stale evidence is NOT_VALIDATED,
never an invented consultation. Metadata review does not load every source body;
only selected necessary sources become REQUIRED. Preserve the Harness whole-inventory rule.

When the requested surface includes CI/CD, containers, IaC, servers, deployment,
cloud, GitOps, observability, backup/DR, incidents or advanced release strategy,
load [DevOps planning](references/devops-planning.md) and add
`devops-standard` to the required skills. Identify target_environment,
validation, rollback_strategy and human gates in the spec/task. Do not add
DevOps to unrelated application changes, UI-only work or routine Git commits.
Keep tool availability, logs and installation state out of the normative contract.

Generate the specs the request needs, following the hierarchy:

- Create specs per module, page/screen, component and rule.
- Always separate **Banco**, **API/Backend** and **Frontend/UI** (plus the other
  mandatory dimensions).
- Mark hypotheses explicitly (`HIPÓTESE:`).
- Do not invent existing architecture; reference real files/paths only when
  verified.
- Use the templates:
  - `templates/product-spec-template.md`
  - `templates/module-spec-template.md`
  - `templates/page-spec-template.md`
  - `templates/component-spec-template.md`
  - `templates/validation-rules-spec-template.md`
  - `templates/database-spec-template.md` (only with DB impact)
  - `templates/api-spec-template.md` (only with backend)

Suggested location for generated specs (create only what is needed):

```text
docs/specs/<modulo>/
  module-spec.md
  pages/<pagina>.md
  components/<componente>.md
  validation-rules.md
  database.md
  api.md
```

<!-- end of selected V2 skill -->

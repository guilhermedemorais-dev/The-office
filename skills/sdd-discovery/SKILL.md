---
name: sdd-discovery
description: "Use for sdd discovery: Phases; Studio PRD handoff; Fase 0 - Diagnóstico; Fase 1 - Consolidação. Load required core skills first."
---

# The Office V2: sdd-discovery

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
- `references/api-research-library.md`: `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/api-research-library.md`

<!-- source-section:sdd-spec-factory:007 sha256:09d270ef6bcdf2c99a76f2055775d95b3e45e2c26a3387b62b703c39bd283f67 -->
## Phases

<!-- source-section:sdd-spec-factory:008 sha256:8c55768fcf3babe1fc76e5eafb47bfbd8d9059abd1c44a9e3084e9f439304afd -->
### Studio PRD handoff

When briefed through `studio-prd`, consume the approved briefing, PRD module
inventory and matching-revision internal plan MD/JSON. Reuse decisions and
research instead of repeating the interview. Approval of the PRD is not
implementation authorization. The handoff proposes the first module in the
approved dependency/urgency order and waits for the user's instruction to
start its specification; do not silently specify all modules in a batch.
Unspecified module cards remain awaiting Discovery/SDD, not Ready for Dev.

Work through that module's actors, journeys, business rules, database, backend,
frontend, integrations, observability, security and tests using the existing
templates below. Research relevant source implementation/tests, not README
alone; record exact source/revision/purpose in the project's reference library.
Ask material gaps as they arise. Finish with coverage, pending decisions and
the existing `DISCOVERY_SDD_COMPLETED` Issue report, then request approval
before the next module. Report publication only with the returned comment URL.
Update the plan's real task/contract links after creation; its short task
prompt is not a replacement for the execution-list prompts or authorization.

An in-scope discovery or acceptance fix updates the same module Task and
equivalent JSON with revision/impact. A genuinely independent or out-of-scope
demand needs a scoped decision; do not fragment by layer or specialist.

<!-- source-section:sdd-spec-factory:009 sha256:16fee6e566212c6381836db5d34822989a82ca010120b7cfc5fcdc9c772ecf21 -->
### Fase 0 - Diagnóstico

Before writing any spec, produce a short diagnosis:

- **O que está claro** — what is unambiguous in the request.
- **O que falta** — missing information needed to spec safely.
- **Riscos iniciais** — early risks (technical, scope, security, data).
- **Perguntas críticas numeradas** — numbered, specific blocking questions.
- **Aguardar resposta humana** when critical scope is missing. Do not proceed to
  specs that depend on unanswered critical questions. Non-blocking gaps may
  continue as marked hypotheses.

<!-- source-section:sdd-spec-factory:010 sha256:e72635eb0e6824d443b24e539ce79d5f391358c35fecedecb8da65634dd3c916 -->
### Fase 1 - Consolidação

When planning/spec discovery requires an API, external integration or validation
endpoint, read [API Research Library](references/api-research-library.md).
Prioritize free APIs or a suitable free tier to validate application features
and test the application when relevant, with verified limits and synthetic data.
Use its relevant discovery sources or curated provider candidates, verify them against
official documentation and record the decision plus validation plan/evidence.
An API listing is neither an approved dependency nor an available MCP. Do not
install or send real customer data during research; untested claims remain
NOT VALIDATED. Skip directory research when the task does not need it.

Consolidate the closed scope (becomes the basis of the product/module spec):

- Objetivo
- Escopo incluído
- Fora de escopo
- Restrições
- Usuários impactados
- Dependências
- Riscos
- Decisões pendentes

<!-- end of selected V2 skill -->

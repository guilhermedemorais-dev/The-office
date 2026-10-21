---
name: sdd-review
description: "Use for sdd review: Fase 4 - Checklist de PR/QA. Load required core skills first."
---

# The Office V2: sdd-review

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

<!-- source-section:sdd-spec-factory:013 sha256:772140e98e42c6af3fd23c0b6719c99a22cf44b2f80c94591c05062f68043b17 -->
### Fase 4 - Checklist de PR/QA

Provide the delivery gates using `templates/pr-template.md`,
`templates/qa-review-template.md` and `templates/review-template.md`:

- Code review
- QA funcional (delegated to `qa-testing-standard` when behavioral triggers apply)
- QA visual (delegated to `ui-ux-standard`)
- Segurança (delegated to `security-standard`)
- Testes
- Evidências
- Aprovação / reprovação

<!-- end of selected V2 skill -->

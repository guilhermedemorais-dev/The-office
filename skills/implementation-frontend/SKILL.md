---
name: implementation-frontend
description: "Use for implementation frontend: Frontend design sources. Load required core skills first."
---

# The Office V2: implementation-frontend

Source: `plugins/dev-implementation-standard/skills/dev-implementation-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, implementation-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/implementation-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/dev-implementation-standard/skills/dev-implementation-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/dev-implementation-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

<!-- source-section:dev-implementation-standard:006 sha256:f32ea2a24291a611ba811cce23e0832785f8cbe8e562c3dc50d81e64a269cf37 -->
## Frontend design sources

For frontend work, resolve the routed project Design Guide Markdown, live HTML
catalogue (or documented equivalent), tokens, component source inventory and
exact component IDs/revisions from the JSON contract. Require the applicable
visual approval evidence before implementing that surface. Missing, stale or
conflicting sources return to Harness; do not invent a replacement style.
Reuse real approved components, and keep the same client-project catalogue
and guide coherent with authorized changes. Never edit the installed plugin
to store a client's widgets. A catalogue fixture remains a labelled simulation;
it cannot satisfy backend/integration acceptance. Return changed component
revisions and actual developer-test evidence to UI/UX and QA for independent
validation, including final application rendering rather than catalogue alone.

<!-- end of selected V2 skill -->

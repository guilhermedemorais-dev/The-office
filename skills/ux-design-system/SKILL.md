---
name: ux-design-system
description: "Use for ux design system: Default Design Structure. Load required core skills first."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: ux-design-system

Source: `plugins/ui-ux-standard/skills/ui-ux-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, ux-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/ux-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/ui-ux-standard/skills/ui-ux-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/ui-ux-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

Canonical link resolution (repository-relative paths, not skill-directory-relative):
- `references/live-design-guide.md`: `plugins/ui-ux-standard/skills/ui-ux-standard/references/live-design-guide.md`

<!-- source-section:ui-ux-standard:006 sha256:e241ad018f9fc7bc2a2c15010d4061a45f0946da44ca977637cceb9c358b928c -->
## Default Design Structure

For module discovery/specification with frontend, read
[Live design guide](references/live-design-guide.md). Maintain both a Markdown
guide and a cumulative, navigable HTML component/widget catalogue in the client
project, or explicitly map its existing equivalent. This is not an optional
Markdown-only deliverable. Backend-only work records UI N/A without scaffolding.

Create only the applicable parts:

```text
docs/design/
  design-guide.md
  index.html
  design.json
  design-tokens.json
  component-standards.md
  component-source-inventory.md
  references/
  mockups/
  media-prompts/
  assets/
  visual-qa/
```

Do not initialize the full tree blindly.

<!-- end of selected V2 skill -->

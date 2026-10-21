---
name: ux-visual-validation
description: "Use for ux visual validation: Visual Quality Gate; Visual QA Checklist. Load required core skills first."
---

# The Office V2: ux-visual-validation

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

<!-- source-section:ui-ux-standard:007 sha256:51d2ecdba921a4571e74d7d719049e5cc7c16b1c283fffa71dec9c160a5fa6ff -->
## Visual Quality Gate

Reject the UI for rework when one or more of these materially apply:

- generic assembly of cards, gradients, pills, glows, and oversized headings
  without product rationale
- hierarchy or density inconsistent with the actual workflow
- visually impressive component that damages usability, accessibility, or
  performance
- several libraries mixed without a clear design-system normalization layer
- external component copied without adaptation to project tokens and states
- desktop-only composition with mobile behavior treated as an afterthought
- missing loading, empty, error, disabled, permission, destructive, or success
  states where the product flow requires them
- visual language conflicts between adjacent screens
- decorative motion that competes with task completion

<!-- source-section:ui-ux-standard:008 sha256:11da6a06aa6583267b4e95a874e3f362b96903010ff5b730a9617c7433a554d5 -->
## Visual QA Checklist

- fidelity against approved mockup/reference
- consistency with design tokens and existing product language
- desktop and mobile responsiveness
- text overflow and overlap
- spacing, alignment, hierarchy, and component states
- loading, empty, error, success, destructive, and permission states when
  relevant
- keyboard accessibility, focus behavior, semantics, and contrast
- images and assets render correctly
- animation respects usability and reduced-motion expectations
- route/auth context is stated accurately
- selected external component dependencies are actually present and compatible

Report untested items as `NAO VALIDADO`.

<!-- end of selected V2 skill -->

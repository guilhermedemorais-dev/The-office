---
name: seo-core
description: "Use for seo core: Preamble; Preconditions; Ownership boundaries. Load required core skills first."
---

# The Office V2: seo-core

Source: `plugins/seo-standard/skills/seo-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/seo-standard/skills/seo-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/seo-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

Canonical link resolution (repository-relative paths, not skill-directory-relative):
- `references/site-delivery.md`: `plugins/seo-standard/skills/seo-standard/references/site-delivery.md`
- `references/beyondseo-integration.md`: `plugins/seo-standard/skills/seo-standard/references/beyondseo-integration.md`
- `references/tool-registry.json`: `plugins/seo-standard/skills/seo-standard/references/tool-registry.json`

<!-- source-section:seo-standard:000 sha256:c42686e2c1c55ba69ed99a7cf9cc9dc5a43c38edaafa603efd35b6306c97a323 -->

# SEO Standard

Own SEO/AEO/GEO and conversion-readiness analysis inside the Engineering Harness.

Read [site-delivery.md](references/site-delivery.md) for website delivery work.
Read [beyondseo-integration.md](references/beyondseo-integration.md) when using
the BeyondSEO runtime. Load only the relevant vendored BeyondSEO playbooks for
technical SEO, on-page, schema, AEO/GEO, search intent or conversion copy.
Consult
[tool-registry.json](references/tool-registry.json) for runtime ownership.

<!-- source-section:seo-standard:001 sha256:9efe80e9d826102d579dd2a5274cdb68ebd63c5f235e90f21914ece0f3bfde22 -->
## Preconditions

1. Identify the target website/page, business goal and intended conversion.
2. Confirm authorized crawl/edit scope.
3. Load this SKILL and emit the normal SKILL_RECEIPT.
4. Distinguish public evidence from business facts supplied by the user.
5. Never promise rankings or fabricate traffic/search-volume evidence.

<!-- source-section:seo-standard:004 sha256:a9a363d0400780f273157a92cc3a0a9b6067d9ed06c80d2500d456950ec21420 -->
## Ownership boundaries

- sdd-spec-factory turns validated findings into specs/Task requirements.
- dev-implementation-standard owns code changes.
- ui-ux-standard owns visual hierarchy/accessibility.
- qa-testing-standard owns functional behavior.
- security-standard owns AppSec.
- dev-workflow-standard owns routing and final gate reconciliation.

SEO Standard may write proposed copy/content, metadata and structured-data
requirements, but does not self-approve product implementation.
<!-- end of selected V2 skill -->

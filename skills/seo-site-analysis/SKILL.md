---
name: seo-site-analysis
description: "Use for seo site analysis: Workflow; Commercial site standard. Load required core skills first."
---

# The Office V2: seo-site-analysis

Source: `plugins/seo-standard/skills/seo-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, seo-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/seo-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/seo-standard/skills/seo-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/seo-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

<!-- source-section:seo-standard:002 sha256:6dc915d00e4c6697c34910187b8ac942d87aaf2e49b9b8a05524e96accf463da -->
## Workflow

1. Inspect the site/project and current business intent.
2. Run the bounded BeyondSEO audit needed for the Task.
3. Classify findings by evidence, impact and priority.
4. Cover technical SEO, AEO/GEO, schema, intent/content and conversion copy when applicable.
5. Produce exact recommended changes, affected URLs/files and acceptance checks.
6. Route implementation to dev-implementation-standard.
7. Re-run fresh validation after changes.
8. Return EXECUTION_RECEIPT with before/after evidence and unresolved limitations.

<!-- source-section:seo-standard:003 sha256:e961c41015b03b891678f4186b50cadd812d22904e20cecd1ac2f406e537cf4e -->
## Commercial site standard

For landing pages and sites sold to clients, treat these as default concerns:

- indexability and crawlability;
- metadata and canonical correctness;
- headings and semantic structure;
- schema;
- mobile/performance evidence;
- search-intent alignment;
- AEO/GEO answer-friendly structure;
- persuasive but factual copy;
- clear CTA and objection handling;
- revalidation before delivery.

Backlinks, reputation, competitor research and editorial planning are available
but should not be forced into every small site.

<!-- end of selected V2 skill -->

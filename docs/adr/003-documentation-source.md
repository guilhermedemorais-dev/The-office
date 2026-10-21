# ADR-003: one versioned documentation source per product

Date: 2026-10-16. Status: accepted. Classification: LOCAL DECISION.

The Documentation owner selects templates from the shared library and writes about the current implemented product only. Tutorials, how-to instructions, reference and explanation are distinct information needs, informed by Diátaxis. Procedural clarity and actual UI interactions are informed by Microsoft Writing Style Guide. Docusaurus is an optional existing rendering example, not a new mandatory dependency.

Use one versioned article tree as the source for repository docs and an optional existing Help Center renderer. No Help Center application is introduced in this Harness migration. Application integration is contextual, requiring its product scope. Actual captures must identify product revision, fixture and capture evidence; unavailable media remain a documented gap. Validate article links, role/permission statements, actual commands and changed functionality before publication.

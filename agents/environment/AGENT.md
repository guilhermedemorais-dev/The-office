# environment agent contract

## Responsibility

Discover the real host/runtime and prepare compatible capabilities.

Reuse dev-environment-standard and existing shared scripts. Keep supported, installed, configured, authenticated and verified distinct. WSL is Linux; no native platform homologation by inference.

## Inputs and activation

Accept Task ID, contract revision, sector, objective, list ID, constraints, dependency receipt paths and relevant evidence. Resolve the selected list from the single canonical Task JSON. Read this contract, required global/core prerequisites, selected capability SKILL.md files completely and their mandatory references. Select procedural skills through `library/indexes/skill-routes.json`; do not preload the sector. Canonical fallback: `plugins/dev-environment-standard/skills/dev-environment-standard/SKILL.md`.

## Authority and boundaries

Inherit global allowed/protected paths, acceptance, stop conditions and human gates. Ask Harness for missing context or contract conflict. Catalog availability is not execution evidence. Only the responsible sector owner may attest its result. Do not copy unrelated PRDs/catalog bodies into handoffs. Do not create another Task per layer or skill.

## Outputs

Readiness checks, tool-state evidence and bounded fallback. Return canonical SKILL_RECEIPT and EXECUTION_RECEIPT with task/revision, loaded sources, actual operations, results, limitations, affected artifacts and next action. Runtime evidence stays outside normative JSON. Missing evidence is NOT_VALIDATED; failure is REWORK or BLOCKED. Human final acceptance remains separate.

## Stack CLI routing

Check existing project commands, then `library/tools/stack-clis.json`. Follow
`library/tools/stack-cli-policy.md` to research official docs for the selected
technology, choose a suitable CLI and prepare it under existing authorization.
Frontend/Backend own suitability; Environment owns installation and tool-state
verification. Reuse installed compatible tools; never bulk-install the catalog.

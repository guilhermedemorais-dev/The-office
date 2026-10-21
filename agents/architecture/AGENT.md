# architecture agent contract

## Responsibility

Choose boundaries and evaluate technical tradeoffs within approved requirements.

Use SDD technical-architecture reference and actual code; compare reuse, modular monolith and distributed alternatives only where relevant. Record ADRs with failure modes, costs and reversibility.

## Inputs and activation

Accept Task ID, contract revision, sector, objective, list ID, constraints, dependency receipt paths and relevant evidence. Resolve the selected list from the single canonical Task JSON. Read this contract, required global/core prerequisites, selected capability SKILL.md files completely and their mandatory references. Select procedural skills through `library/indexes/skill-routes.json`; do not preload the sector. Canonical fallback: `plugins/sdd-spec-factory/skills/sdd-spec-factory/SKILL.md`.

## Authority and boundaries

Inherit global allowed/protected paths, acceptance, stop conditions and human gates. Ask Harness for missing context or contract conflict. Catalog availability is not execution evidence. Only the responsible sector owner may attest its result. Do not copy unrelated PRDs/catalog bodies into handoffs. Do not create another Task per layer or skill.

## Outputs

Architecture, ADRs and implementation constraints. Return canonical SKILL_RECEIPT and EXECUTION_RECEIPT with task/revision, loaded sources, actual operations, results, limitations, affected artifacts and next action. Runtime evidence stays outside normative JSON. Missing evidence is NOT_VALIDATED; failure is REWORK or BLOCKED. Human final acceptance remains separate.

## Architecture and infrastructure CLIs

Consult `library/tools/stack-clis.json` and the shared
`library/tools/stack-cli-policy.md` before selecting tools. Nx can generate structures and check configured module boundaries; domain ownership remains an architecture decision. Use the existing framework generator when sufficient. OpenTofu models deployment infrastructure, not application module design.

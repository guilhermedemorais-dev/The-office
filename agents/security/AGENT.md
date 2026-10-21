# security agent contract

## Responsibility

Independently assess threat boundaries, authorization, secrets, dependencies and attack surfaces.

Reuse security-standard, OSV and applicable versioned controls. Distinguish advisory lookup from executed validation. Return only own sector result with evidence and residual risk.

## Inputs and activation

Accept Task ID, contract revision, sector, objective, list ID, constraints, dependency receipt paths and relevant evidence. Resolve the selected list from the single canonical Task JSON. Read this contract, required global/core prerequisites, selected capability SKILL.md files completely and their mandatory references. Select procedural skills through `library/indexes/skill-routes.json`; do not preload the sector. Canonical fallback: `plugins/security-standard/skills/security-standard/SKILL.md`.

## Authority and boundaries

Inherit global allowed/protected paths, acceptance, stop conditions and human gates. Ask Harness for missing context or contract conflict. Catalog availability is not execution evidence. Only the responsible sector owner may attest its result. Do not copy unrelated PRDs/catalog bodies into handoffs. Do not create another Task per layer or skill.

## Outputs

Scoped security review and executed validation evidence. Return canonical SKILL_RECEIPT and EXECUTION_RECEIPT with task/revision, loaded sources, actual operations, results, limitations, affected artifacts and next action. Runtime evidence stays outside normative JSON. Missing evidence is NOT_VALIDATED; failure is REWORK or BLOCKED. Human final acceptance remains separate.

## Second audit: Cloudflare

Consult the sector index first. Select `security-audit` for Cloudflare's audit
procedure as the second audit after the existing Security review, within the approved scope. Keep separate results, use fresh reviewers and reconcile findings only after independent investigation. Read its selected skill completely;
load domain companions conditionally. Keep focused guidance separate from full
audits and preserve existing OSV, independent validation and publication gates.
The central record is `library/skills/external-skills.json`; generated sector
views live in `library/indexes/skill-routes.json`. Catalog presence proves no audit.

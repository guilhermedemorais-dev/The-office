# governance agent contract

## Responsibility

Maintain Issue/contract equivalence, history, PR integrity and human gates.

Reuse canonical Harness/SDD contracts and receipts. Record material scope change and revision before affected work. Never approve another owner sector or merge/deploy from green checks alone.

## Inputs and activation

Accept Task ID, contract revision, sector, objective, list ID, constraints, dependency receipt paths and relevant evidence. Resolve the selected list from the single canonical Task JSON. Read this contract, required global/core prerequisites, selected capability SKILL.md files completely and their mandatory references. Select procedural skills through `library/indexes/skill-routes.json`; do not preload the sector. Canonical fallback: `plugins/dev-workflow-standard/skills/dev-workflow-standard/SKILL.md`.

## Authority and boundaries

Inherit global allowed/protected paths, acceptance, stop conditions and human gates. Ask Harness for missing context or contract conflict. Catalog availability is not execution evidence. Only the responsible sector owner may attest its result. Do not copy unrelated PRDs/catalog bodies into handoffs. Do not create another Task per layer or skill.

## Outputs

Issue ledger, reviewable PR and final reconciliation. Return canonical SKILL_RECEIPT and EXECUTION_RECEIPT with task/revision, loaded sources, actual operations, results, limitations, affected artifacts and next action. Runtime evidence stays outside normative JSON. Missing evidence is NOT_VALIDATED; failure is REWORK or BLOCKED. Human final acceptance remains separate.

## Delivery metrics

Select `delivery-metrics` for checkpoint/Task closure reports. Reconcile the
approved plan with evidence, include unfinished work in the denominator and
separate closure readiness from actual Done and publication. Reuse the inspected
Portal do Cliente adapter. Do not publish customer reports without authorization.

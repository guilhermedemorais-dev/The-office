---
name: sdd-core
description: "Use for sdd core: Preamble; Mission; Vocabulary (non-negotiable); Mandatory hierarchy; Mandatory separation of concerns; Operating principles; Integration with the other plugins; Definition of done for this skill. Load required core skills first."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: sdd-core

Source: `plugins/sdd-spec-factory/skills/sdd-spec-factory/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/sdd-spec-factory/skills/sdd-spec-factory/`;
for plugin templates/scripts absent there, use repository root `plugins/sdd-spec-factory/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

Canonical link resolution (repository-relative paths, not skill-directory-relative):
- `references/backend-component-sources.md`: `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/backend-component-sources.md`
- `references/public-code-discovery.md`: `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/public-code-discovery.md`

<!-- source-section:sdd-spec-factory:000 sha256:ef11d0a1d6bb70af7850a6241a69ebd6780e5cb162290081dfb7bc3d800b38aa -->

# SDD Spec Factory

Specialist workflow for **Spec-Driven Development (SDD)**. It converts an idea,
client request, feature or problem into detailed specs and one complete
executable Task per functional module, then hands execution back to `dev-workflow-standard` and the review
specialists. Keep this file lightweight: create only the specs and the task the
current request actually needs, and load the templates on demand.

The LLM using this skill acts as the requirements LLM. Before producing specs,
it must read this `SKILL.md` completely and return a `SKILL_RECEIPT`. Naming the
skill in a prompt is not evidence of activation.

For applicable backend/library, payments, fiscal or commerce needs, consult
[Backend component sources](references/backend-component-sources.md) metadata
before targeted new research. Select eligible free editions only, preserving
license obligations and separate provider/infrastructure costs. This adds
candidates, not dependencies or a stack decision.

When the user/project declares a Next.js/NestJS preference and stack is undecided,
assess that reference pair through existing catalog IDs, then confirm the PRD.
Preserve approved stacks; do not apply this preference to undeclared projects. Next server/BFF adapters may call
Nest-owned domain APIs; do not duplicate business rules or assume Next cannot run backend code.

<!-- source-section:sdd-spec-factory:001 sha256:826f120f888d4b111648a67031cd4c27199a1b834c7203351f124bd2eee8f16d -->
## Mission

Transform NORMAL work with unspecified behavior and COMPLEX work into, when
applicable:

- product spec (only when the request defines or changes the product itself)
- module spec
- page/feature spec
- component specs
- validation/business rules spec
- database spec (only when there is database impact)
- api/backend spec (only when there is a backend)
- frontend/ui spec (only when there is UI)
- one executable task
- one v2 machine-readable execution contract with normative equivalence to the
  complete GitHub Issue/card for each new executable task
- a PR checklist
- a QA/review checklist

This plugin **does not implement product code**. It produces the contract and the
order of execution. `dev-workflow-standard` orchestrates; implementation is
carried out by `dev-implementation-standard`, reviewed with `security-standard`,
functionally validated with `qa-testing-standard` when required, and visually
validated with `ui-ux-standard`.

<!-- source-section:sdd-spec-factory:002 sha256:41af71533d262e3eabe2b71067488fb7adb9ace72c212ad4267d2176242a8336 -->
## Vocabulary (non-negotiable)

- **Spec is not a PR.** A spec is the contract of what must be built.
- **Task is the order of execution.** Its default unit is a complete functional
  module, with reviewable internal microtasks and end-to-end acceptance.
- **PR is the reviewable delivery.**
- **Issue is the complete human task/card.** A local Markdown may mirror it but
  does not replace it when GitHub Issues is available.
- **Review is approval or rejection.**
- **Deploy only happens after the PR is approved.**

A spec describes intent and acceptance. The Human Task tells people everything
needed to understand and govern the work. The v2 Execution Contract expresses
the same normative content as structured JSON for the LLM. This **normative
equivalence** is deliberate, while runtime status, evidence and discussion stay
in Issue comments and receipts.

<!-- source-section:sdd-spec-factory:003 sha256:87f8030dc914cbbf6f6f845df59f2a8ee36e0f8c30c70dd06917f183c303d3d0 -->
## Mandatory hierarchy

For work routed to this skill, respect this top-down order. Do not create every
artifact mechanically: reuse an existing parent or record an explicit,
traceable parent intent when a new product/module/page document would add no
information.

```text
Product Spec
  -> Module Spec
    -> Page/Feature Spec
      -> Component Specs
        -> Human Task
          -> Execution Contract
            -> Branch
            -> Pull Request
              -> Review / QA
                -> Merge / Deploy
```

<!-- source-section:sdd-spec-factory:004 sha256:7bb9c3bccedd21c534fb3a7ced32955e2c52491d74b9f4485c9a609adcf48707 -->
## Mandatory separation of concerns

Every spec and every task must keep these dimensions visibly separated. Do not
collapse them into one prose blob; if a dimension does not apply, write
"N/A" with a one-line reason.

1. **Banco** (database / data model / migrations)
2. **API/Backend** (endpoints, contracts, services, jobs)
3. **Frontend/UI** (screens, components, states)
4. **Testes** (unit, integration, e2e, what must be covered)
5. **Segurança** (authz/authn, tenant boundaries, secrets, sensitive data)
6. **Observabilidade/logs** (events, metrics, audit trail)
7. **Decisões pendentes** (open decisions waiting for a human)
8. **Riscos** (what can break, regressions, unknowns)
9. **Critérios de aceite** (objective, testable acceptance)

<!-- source-section:sdd-spec-factory:005 sha256:0c96306a6847da60be05fa3080000d9f1d0827bb36eb73df309eb08d2f2c84b3 -->
## Operating principles

- The repo, PRD, existing architecture, approved mockups and `AGENTS.md` are the
  source of truth. Inspect the real repo before writing specs.
- Before external research, apply the active Harness capability registry's
  whole-inventory consultation and research routing. Inspect the MCP Library,
  all active specialist tool-registry metadata and actual host tools,
  prefer suitable available documentation/code/extraction/search capabilities,
  and record the reason for generic fallbacks. Reuse existing source records.
- **Do not invent existing architecture.** If you do not know whether a table,
  endpoint, service or component exists, do not assert it. Mark it as a
  hypothesis (`HIPÓTESE:`) or as a pending decision.
- Mark every assumption explicitly. Unverified facts are hypotheses, not specs.
- Generate one complete Task per functional module in the approved demand.
  Decompose large work into internal microtasks and resumable checkpoints,
  never separate Tasks merely by layer, phase or specialist. Size, token budget,
  context limits and review convenience are not exceptions.
- Before specifying a new service, helper, component, route, abstraction or
  subsystem, search the source-of-truth repository for an existing equivalent.
  Prefer reuse or extension and record the decision in `REUSE_INVENTORY`.
- When an unresolved implementation question needs public code examples, read
  [public code discovery](references/public-code-discovery.md). Prefer the
  official Grep service when available; validate candidates at their source.
- Reject speculative abstractions and duplicated responsibilities. New
  abstractions require two current concrete consumers or an explicit approved
  architectural requirement.
- Stop and ask when critical scope is missing. Do not guess core scope.
- Final acceptance belongs to the user.
- Planning depth is selected by `dev-workflow-standard`: TRIVIAL changes remain
  outside full SDD and use an inline intent contract; NORMAL changes use the
  smallest focused spec needed; COMPLEX changes use durable layered specs and
  traceability. This skill must not inflate a bounded change into a full
  document tree.

<!-- source-section:sdd-spec-factory:014 sha256:d75a190dc2d9917bb62421da93a51f41039e23b00e42bac391f424b733612e0f -->
## Integration with the other plugins

- `dev-workflow-standard` is the Engineering Harness. It owns discovery, scope,
  delegation, gates and approval. SDD Spec Factory feeds it the specs and the
  executable task; it does not replace it.
- `dev-implementation-standard` is the executor. It implements the approved task
  strictly within the scope these specs define; it consumes the task and PR
  templates produced here.
- `ui-ux-standard` owns design systems, mockups and visual QA. Page/component/UI
  specs should reference approved mockups and design tokens instead of inventing
  visuals.
- `qa-testing-standard` owns independent test strategy, functional validation,
  reproduction, regression and fix verification. It receives the QA Task slice
  and relevant sources; it neither writes product fixes nor attests UI/Security/
  DevOps PASS. Those owners return their own evidence.
- `security-standard` owns the security review and release gate. The security
  dimension of each spec and the security checklist of each PR are validated by
  it.

<!-- source-section:sdd-spec-factory:015 sha256:37a9ef006d013ffa80995989eab1be52960b2f54dc7aab8b9b549c5f7e275d8a -->
## Definition of done for this skill

- The needed specs exist and follow the hierarchy.
- Banco, API/Backend, Frontend/UI, Testes, Segurança, Observabilidade,
  Decisões pendentes, Riscos and Critérios de aceite are separated.
- There is one complete executable Task per module linking specs, issue, branch
  and PR, with applicable disciplines as microtasks. The module-boundary gate
  passed for the entire output set and every separation exception is justified.
- Every new executable task has a valid v2 Execution Contract with normative
  equivalence to the complete Issue/card and a copy-ready ignition prompt;
  legacy tasks have the compatibility fallback above.
- PR and QA/review checklists are provided.
- Sector matrix, microtasks, purpose-based routing, phase dependencies and
  explicit N/A reasons are consistent; legacy v1 contracts remain readable.
- Spec consistency analysis maps approved in-scope requirements to microtasks,
  acceptance and planned validation; blocking gaps/conflicts are resolved.
- No product code was implemented and no existing architecture was invented.
<!-- end of selected V2 skill -->

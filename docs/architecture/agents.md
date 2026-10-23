# Sector ownership

The 14 logical sectors plus transversal librarian have contracts under `agents/`. These are responsibility contracts, not permanently running processes. Every activated engineering sector must run through its corresponding registered host subagent. The principal coordinates and consolidates; it does not simulate sector owners.

| Agent | Output | Canonical procedural owner |
| --- | --- | --- |
| orchestrator | Task/list routing and consolidated owner evidence | dev-workflow-standard |
| product | Approved PRD and scoped module inventory | studio-prd |
| architecture | Architecture, ADRs and implementation constraints | sdd-spec-factory |
| sdd | Specs, Human Task, equivalent JSON and requirement coverage | sdd-spec-factory |
| ux-design | Design artifacts and independent visual evidence | ui-ux-standard |
| frontend | Implemented frontend and executor test evidence | dev-implementation-standard |
| backend | Implemented backend and executor test evidence | dev-implementation-standard |
| data | Data contracts, safe migration plan and integrity evidence | dev-implementation-standard |
| security | Scoped security review and executed validation evidence | security-standard |
| qa | Test plan, executed results and reproduction evidence | qa-testing-standard |
| devops | Operational plans and environment-specific executed evidence | devops-standard |
| environment | Readiness checks, tool-state evidence and bounded fallback | dev-environment-standard |
| documentation | Technical docs, task tutorials and source-linked help articles | dev-implementation-standard |
| governance | Issue ledger, reviewable PR and final reconciliation | dev-workflow-standard |
| librarian | Purpose-qualified source IDs, compatibility notes and cache provenance | dev-workflow-standard |

The canonical JSON sector IDs remain database, backend, frontend, ui_ux, qa, security, devops, observability, documentation and harness. Do not rename schema fields to match agent directory names. Final Harness reconciliation depends on every other REQUIRED sector and current owner evidence.

## Codex host roles

The registration helper maps each contract directory to one role:

| Contract directory | Codex role |
| --- | --- |
| orchestrator | `office_orchestrator` |
| product | `office_product` |
| sdd | `office_sdd` |
| architecture | `office_architecture` |
| data | `office_data` |
| backend | `office_backend` |
| frontend | `office_frontend` |
| ux-design | `office_ux_design` |
| qa | `office_qa` |
| security | `office_security` |
| devops | `office_devops` |
| environment | `office_environment` |
| governance | `office_governance` |
| documentation | `office_documentation` |
| librarian | `office_librarian` |

Select only the required sectors, respecting slots and exclusive file ownership.
The principal must not spawn a second orchestrator merely to duplicate its own
coordination. If a profile/tool is unavailable, record NOT_EXECUTED for that sector
and NOT_VALIDATED for its affected claims. Registration/checking does not prove
invocation or review. The contracts remain the procedural source, not a second
agent methodology. See the [Codex guide](../operations/codex-agents.md).

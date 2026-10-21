# Sector ownership

The 14 logical sectors plus transversal librarian have contracts under `agents/`. These are responsibility contracts, not permanently running processes. An LLM host instantiates real agents only where available and useful.

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

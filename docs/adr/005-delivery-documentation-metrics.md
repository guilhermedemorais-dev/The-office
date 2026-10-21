# ADR 005: Task documentation and evidence-based delivery reports

Status: accepted owner request, 2026-10-21.

Existing V2 has Documentation core/templates, Studio PRD stages and JSON v2
contracts, but no explicit documentation-plus-metrics closure protocol. V1 portal
reference incorrectly says the owner's source is still pending.

Decision: extend the existing Documentation owner with technical/usability impact
assessment on every Task, Diátaxis authoring from pinned github/awesome-copilot,
and a Governance capability for derived stage/project progress and safe client
reports. Preserve TRIVIAL inline execution and canonical ten-sector JSON v2.
Reconcile future contracts with necessary criteria before implementation; do not
silently add incompatible normative fields or another Task store.

The existing portal has a different done/eligible metric that excludes backlog.
Provide a compatible preparation adapter and disclose this difference. Do not
replace the portal or change that separate repository in this Task. A whole-scope
portal dashboard remains a scoped follow-up, not claimed implemented here.

Alternatives: adding a new management service/Redis/database duplicates existing
Task truth; installing several writers duplicates context; using the upstream
writer verbatim would repeatedly stop for outline approval. Reject these for
maintenance/context cost. Adapt only governance/research; retain original guide.

Metric formula is a LOCAL decision: accepted approved scope units / all baseline
scope units. It is not earned value, time completion, developer productivity or
predicted finish date. Content hashes detect source drift, not semantic approval.

Validation: deterministic fixtures for blocked/unstarted scope, stale files,
malformed snapshots, docs pending, portal mapping and separate closure readiness;
real forward-use of selected skills and full inherited regression. Browser/native
client installation and real portal/API synchronization remain NOT_VALIDATED.

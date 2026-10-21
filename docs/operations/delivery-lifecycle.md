# Delivery lifecycle and Task closure

Owner-approved V2 extension, 2026-10-21. Reuse the existing Studio PRD plan
(`plugins/studio-prd/skills/studio-prd/references/planning.md`) and SDD JSON v2.
Stages already exist. This overlay makes documentation and progress handoff
explicit; it does not replace the canonical ten-sector schema or create a second
Task system. V2 policy takes precedence over historical workflow wording.

| Phase | Entry | Exit evidence | Responsible |
| --- | --- | --- | --- |
| Product and plan | New demand, or existing approved scope | PRD/scope, module inventory, priorities and baseline | Product + owner |
| Architecture and specification | Relevant product decisions settled | Focused specs, dependencies, criteria, one Task per module | Architecture + SDD + sectors |
| Implementation | Authorized current contract and prerequisites | Actual changes, executor checks and handoff | Selected sector |
| Validation and rework | Reviewable artifact revision | Applicable independent QA, Security, UX and operational evidence | Required validators |
| Documentation | Changed behavior/code and validation evidence | Technical docs + real user procedure, or justified no-change/N/A | Documentation |
| Delivery report and review | Evidence reconciled | Stage/total metric, blockers, safe client report, PR review | Governance + metrics + orchestrator |
| Acceptance and release | Existing explicit human gates | Actual acceptance/merge, deployment only if separately authorized | Owner + authorized DevOps |

Plan documentation needs during specification, write alongside implementation,
then finalize after validation. A documentation correction that changes product
behavior returns to the affected validator. Do not force a waterfall or repeat
Discovery for existing scoped work. A phase may be N/A only with a recorded reason.
One coherent Task includes its phase/layer/specialist microtasks; do not create an
Issue per phase. Reuse the current approval, execution and integration order.

## Mandatory closure checkpoint, every Task

Before declaring work ready for final review, the orchestrator routes the changed
scope and evidence to `documentation-core`, then `delivery-metrics` under
Governance. These are logical responsibilities, not mandatory separate processes.
If real agents are unavailable execute serially, without claiming independent
execution. Reuse current owner receipts; never approve on behalf of another owner.

1. Documentation records technical impact and usability impact independently:
   UPDATED, UNCHANGED, NOT_APPLICABLE or PENDING, with reason and source evidence.
   New user-visible behavior needs an updated tutorial/how-to. A fix may update
   an existing article. A purely internal change can justify user N/A.
2. Missing screenshots alone do not block truthful text docs: mark capture
   NOT_AVAILABLE and UI runtime verification NOT_VALIDATED. Never fabricate media.
   Missing required behavior verification or required docs leaves readiness pending.
3. Metrics reconciles baseline, current criteria, actual tests, unresolved work,
   documentation and human gates. Record prepared vs published report separately.
4. Update existing Task comments/receipts and approved project documentation.
   Client Portal receives only reviewed client-safe content; internal evidence
   remains linked internally. No automatic remote message, merge or deployment.

For TRIVIAL work, satisfy both responsibilities in the existing compact outcome:
`Documentation: technical/user UNCHANGED or N/A, reason; progress: existing
criterion/check evidence or N/A`. Load only needed procedure; no extra Issue,
contract, persistent agent, snapshot or full-phase documentation package.
For NORMAL/COMPLEX work use the existing execution contract and owner evidence;
if an approved contract lacks necessary closure criteria, reconcile Human Task
and JSON with a documented revision before changing normative obligations.

## Baseline discipline

Define the project baseline from approved modules and acceptance deliverables.
Keep planned work, blockers, validation and applicable documentation in scope.
Update after each material checkpoint and Task closure. Percentages report
accepted scope units, not guessed elapsed time or effort. No measured telemetry
means NOT_AVAILABLE. The calculator is optional for a trivial outcome and never
substitutes semantic owner review or observed remote state.

Operational instructions and draft snapshot shape: `delivery-report-guide.md`.
The installed Portal template belongs to the client project's `docs/portal/`
and is linked from its docs home/navigation using the existing renderer.

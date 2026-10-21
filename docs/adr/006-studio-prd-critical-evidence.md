# ADR 006: Evolve canonical Studio with evidence-based critical discovery

Status: owner-approved proposal and technical research refinement, 2026-10-21.
Task STUDIO-PRD-002, Issue #4, contract revision 1.

Studio already owns adaptive briefing, module PRD and equivalent internal plan.
Global critical-thinking rules exist, but the product workflow does not make
assumption testing, evidence/applicability and phase advancement explicit enough.

Decision: evolve that canonical skill with bounded critical conversation, explicit
product diagnosis/debate/PRD phases and conceptual Data/Backend/UI triage. Reuse
existing tables, source library, plan and JSON v2, not another CTO or memory store.
Official version-matched technology docs support material recommendations; source
facts, hypotheses, preferences and decisions stay distinct from approval status.
Unavailable evidence limits dependent conclusions; it does not block all work.

Sources: CMU SEI QAW 3rd edition (2003) and NN/g Discovery in Agile (2023), read
2026-10-21. They support early qualities/targeted inquiry; this workflow is a local
adaptation. Concrete technology claims still need that technology's primary docs.
Docs do not prove observed runtime performance, security or product correctness.

Compatibility: six affected original files are archived byte-for-byte under
`docs/migration/v1-frozen/`, with explicit ADAPTED paths in the existing verifier.
The source inventory and its hashes remain unchanged. Live canonical source and
its generated V2 slices evolve together; archives never become active routes.
This is a documented exception to ADR 001's original freeze, not a weakened test.
Preserved old snapshots represent historical versions, not another owner skill.

Alternatives rejected: a second CTO skill duplicates responsibility; large global
rule additions inflate every task; keeping Studio frozen would leave legacy
entrypoints without the approved improvements. Only local procedures are expanded.

Keep plan.py, planning schema v1, execution JSON v2, Tasks and SDD procedure
unchanged. Product contract permits discovery before a downstream Task exists.
QA combines structural regressions with actual independent skill-use scenarios;
these do not guarantee behavior of every model or future prompt. Native host
activation and owner acceptance remain independent gates. No product code,
external installation, build, deployment or merge is authorized by this change.

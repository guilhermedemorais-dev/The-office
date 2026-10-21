# Measurement contract

Use schema_version 1 for a **derived snapshot**, outside normative execution JSON.
The approved plan/Issue/JSON remain authoritative. Update a snapshot when any of
those revisions changes; never edit source contracts to reflect runtime progress.

Snapshot keys: `schema_version`, `project`, `baseline_revision`, `baseline_source`
(`path`, `sha256`), `stages` (`id`, `title`), `tasks` and `items`.
Each task has `id`, `contract_revision`, `source` (path/hash), `issue_url` (or null),
`title`, and `documentation`: `technical` and `user` assessments. Each assessment
has `status` UPDATED/UNCHANGED/NOT_APPLICABLE/PENDING, `reason` and `evidence`
(path/hash list). UPDATED needs article evidence; UNCHANGED and NOT_APPLICABLE
need scoped justification and inspection evidence. PENDING is never closure.
Each item is an existing criterion/deliverable from the approved baseline:
`id`, `task_id`, `stage_id`, `status`, `evidence` and optional positive `weight`
(default 1). Only ACCEPTED earns credit and requires owner evidence.
Other states: PLANNED, IN_PROGRESS, BLOCKED, REWORK, NOT_VALIDATED. Do not split
criteria to inflate completion. The calculator checks references/hashes, not the
meaning, provenance or completeness of the claimed approval. Owners reconcile
coverage, scope, validation and authorizations before client use.

Formula: 100 * sum(weight of ACCEPTED items) / sum(weight of all baseline items).
No denominator => null/NOT_AVAILABLE. All planned/backlog items remain included;
never remove a blocker to improve the number. Weights are approved scope units,
not time estimates. Equal weights measure criterion completion, not effort.
Scope/weight changes require plan/contract review and a new baseline comparison;
show old/new denominators and reason. Never silently maintain a monotonic graph.

Keep implementation, documentation, review, owner acceptance and authorized
release as separate criteria when applicable. A Task is closure-ready only when
its criteria are accepted AND both documentation assessments resolve. Existing
merge/deploy/final human gates still apply; closure-ready is not observed Done.
Record observations at a commit/time; content hashes detect local drift but are
not proof a remotely referenced Issue or approval is still current.

Optional telemetry belongs to existing receipts: actual elapsed/active time,
measured tokens input/output/cache, tool calls, delegations, retries/rework and
human interventions. Missing measurements are null/NOT_AVAILABLE, never zero.
Do not infer duration or token savings from criterion percentages.

Portal export prepares only task ID/Issue mapping, safe summary titles, stage,
status and computed criterion percentage. The owner reviews this content for
client suitability. IDs/revisions/hashes and internal evidence stay internal.
The portal's own done/eligible percentage is a **different metric** and excludes
backlog; identify it separately. Its existing API cannot display our weighted
whole-baseline metric without a future portal change. Do not overwrite or label
that existing dashboard as a full-process measurement.

# Documentation, phases and delivery metrics integration

Date: 2026-10-21. Parent V2 commit: 7f42f0d9348ca0f50133067ebe259a576617b64c.
Task: THEOFFICE-V2-001, existing contract revision 1. This adds approved
Documentation/library/metrics capabilities; no canonical JSON field/sector rename.

## Implemented

- Extended existing Documentation core and owner contract; separate technical
  and user impact at each Task closure. NEW behavior needs real usability
  instructions, not a generic release note. Existing docs/help remain canonical.
- Selected github/awesome-copilot documentation-writer (Diátaxis), pinned at
  613efc8c21d9b3ce642dff361d17006cd9967e28. Preserved its 2,748-byte original and
  MIT license with hashes. Adapted repeated outline approval/external research
  restrictions explicitly to existing Task authorization and official-source work.
- Compared the same repository's `agents/se-technical-writer.agent.md`: useful
  broad developer/blog/architecture guidance, but includes model/tool choices and
  more editorial context. Kept it as inspected alternative, not another installed
  writer. No universal best-skill ranking or effectiveness benchmark claimed.
- Reused Studio PRD's existing stage plan and one-Task-per-module rule. The local
  lifecycle overlay adds documentation and metrics before final review while
  preserving TRIVIAL compact execution and independent validators/human gates.
- Added Governance `delivery-metrics`, routed also through the orchestrator alias;
  no persistent agent/service. Read-only Python calculator, JSON/Markdown reports,
  compatible Portal task payload preparation and draft snapshot template.
- Whole-baseline scope metric includes unstarted/blocked work; no credit for
  rework/unverified states. Local source hashes, IDs, documentation assessments,
  path/duplicate/weight/Issue mapping validation. Owner semantic approval remains
  necessary. No token, duration or developer productivity inference.
- Inspected owner's portal-clientes at 82226fbb2385639d7812b2de929b435e6480fbbc.
  It exists and contains React/Vite UI, backend, OpenAPI and sync-template script.
  New adapter supersedes the frozen V1 statement that source publication is pending.
  Template destination is **the client project's docs/portal/**, linked from that
  project's existing docs home/navigation. No portal copy into shared Harness.

## Executed validation

- `OFFICE_PLOP_BINARY=/tmp/office-plop-validation/node_modules/.bin/plop python -m unittest discover -s tests -v`
  exit 0: **721 discovered, 714 passed, 7 native-Windows skips**, 11.206 seconds.
  Includes actual Plop generation and the 16 new reporting/routing/provenance
  tests; report CLI JSON/Markdown/Portal formats execute against synthetic files.
- `python scripts/build_skill_routes.py --check`: PASS, 41 generated skills;
  local and external capabilities are registered separately (44 total skill IDs).
- `python scripts/verify_preservation.py`: PASS, all 342 frozen V1 files intact.
- skill-creator quick_validate: documentation-core and delivery-metrics PASS.
- `git diff --check`: PASS. No unknown dependencies installed for this change.
- Real independent skill usage by agent `/root/documentation_delivery_usage`:
  requested Task closure for a Save draft UI change with unit checks complete,
  browser unavailable, missing tutorial and human review pending; also a README
  typo. Agent read required skills/references, returned truthful pending docs/
  runtime/human gates, no fabricated percent/media and bounded TRIVIAL handling.
  This was read-only scenario handoff validation, not a real client product test.
  Later destination clarification is documentation-only; no code behavior changed.

## Not validated / remaining gaps

- The current Portal dashboard measures done/eligible and excludes backlog.
  Prepared task payloads are compatible, but whole-baseline dashboard display
  requires a separate scoped change in portal-clientes. No portal source modified.
- No live Portal API/OAuth/customer project installation, HTTP publication,
  deployment or browser replay was executed. Payloads are PREPARED_NOT_PUBLISHED.
- Offline source hash checks do not establish semantic approval, completeness or
  current remote Issue state. Snapshot is a disposable read model, never Task truth.
- The routing policy is an instruction protocol; it does not create host scheduler
  hooks. Missing native agent support uses serial responsibility with honest evidence.
- Native Windows/macOS validation, real token/cost savings and actual user tutorial
  acceptance remain NOT_VALIDATED. All missing telemetry stays NOT_AVAILABLE.

## Owner smoke check

1. From the V2 checkout run `python scripts/office.py plan documentation`, then
   `python scripts/office.py plan governance --capability delivery-metrics`.
2. Use `docs/operations/delivery-report-guide.md` with an actual approved project
   baseline and evidence. Confirm unstarted work is counted and docs pending blocks
   closure; stale file content must fail before refreshing reviewed evidence.
3. Confirm template preparation targets CLIENT_ROOT/docs/portal/, preserves edits
   and uses the existing renderer/navigation. Review compatible payloads locally.
4. Complete project-specific owner API/auth/publication setup and read-back only
   under its actual authorization. Final acceptance/merge/deploy gates remain.

Sources: https://github.com/github/awesome-copilot/tree/613efc8c21d9b3ce642dff361d17006cd9967e28/skills/documentation-writer
and its se-technical-writer agent; https://diataxis.fr/ ;
https://learn.microsoft.com/en-us/style-guide/procedures-instructions/ .
These guide structure; actual product behavior comes from its implementation.

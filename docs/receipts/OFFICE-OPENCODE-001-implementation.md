# OFFICE-OPENCODE-001: implementation evidence

Date: 2026-10-27. Branch: `feat/replica-opencode-graphiti`.
User directly authorized actual alterations and separate install/update prompts.
Source baseline: `60e2e35501ee1e3c1ad77f8beb7a015b6c905e62`.

## Executed work

Real generic executors implemented the scoped source changes. The principal
regenerated V2 skills/routes and the resource index, inspected diffs, and ran tests.
Registered `office_*` profiles were not available: their formal owner execution
is NOT_EXECUTED and dependent approval claims remain NOT_VALIDATED. Supporting
research, implementation and code review are not mislabeled registered owners.

## Checks

- `python scripts/build_skill_routes.py --check`: PASS, 41 generated skills.
- `python scripts/verify_preservation.py`: PASS, 342 preserved source files.
- `python -m unittest discover -s tests -v`: exit 0, 793 tests, 8 skips,
  11.632 seconds. Focused additions: 14 reconstruction, 13 OpenCode and 18 memory tests.
- `git diff --check`: PASS.
- Independent generic read-only reviews inspected host/spec helpers and memory.
  Memory review found missing provider-initialization fallback; corrected with a
  regression test. Host/spec review found no concrete blocker in its checked scope.

## Limits and closure

Checks prove local code/fixture behavior and preservation, not successful real
OpenCode dispatch, live Graphiti/Neo4j/inference, multiuser isolation, native OS
homologation, secret-filter completeness or token savings. No host configuration,
live memory ingestion, dependency installation, merge or deployment performed.
Formal required owner gates and target-host validation remain pending; Task is
not closed or certified ready for release.

Documentation: technical UPDATED; user procedures UPDATED, including independent
installation/update prompts. UI screenshots N/A (CLI/protocol scope). No measured
completion percentage or token savings. Publication evidence is the GitHub branch
and review PR, to be returned after remote tree verification.

## Follow-up validation 2026-10-27

Validated implementation commit: `6d60d35bea29acca18481e73ddc1600982142615`.
The installed CLI reports OpenCode `1.4.0`; the documented schema baseline is
`1.19.4`. In an isolated synthetic project, registration `plan`, `apply`, and
`check` returned exit 0; `opencode agent list` recognized all 15 generated
profiles, including `office_orchestrator` as primary and specialists as
subagents. No profile was installed into the active checkout or global config;
`opencode agent list` in the active checkout showed no `office_*` profiles.

A synthetic read-only `office_orchestrator` → `office_qa` dispatch using the
officially listed free `opencode/big-pickle` model did not return within 120
seconds. Dispatch and the formal registered-owner validations therefore remain
NOT_VALIDATED. No real project/customer data was used and no configuration was
changed. Focused OpenCode tests PASS (14); full suite PASS (795 tests, 8 skips).
The installation and update prompts remain separate, with a regression test.
Issues #10, #11 and #12 exactly match their local task mirrors at comparison.

The task contract requires an Issue comment for publication evidence. This
follow-up updated the implementation receipt and PR description only; the Issue
comment and Task closure remain pending.

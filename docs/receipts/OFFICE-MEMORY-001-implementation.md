# OFFICE-MEMORY-001: implementation evidence

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
Focused memory tests PASS (19); full suite PASS (795 tests, 8 skips). The local
environment has no `graphiti-core==0.31.2`, Neo4j service on loopback ports 7474/
7687, Neo4j executable, or cached Neo4j container image.

An isolated Git workspace and synthetic source were used for the adapter CLI:
`enqueue` returned QUEUED; `sync` exited 2 with `PackageNotFoundError` and
`live_graph: NOT_VALIDATED`; `search` exited 0 with the documented local fallback.
No source was sent to a graph or inference provider. Real Graphiti/Neo4j/model
integration remains NOT_VALIDATED. Documentation now states that sync/search can
send source/query content to the configured inference provider and may incur
charges; no spending limit is enforced by this adapter. Issues #10, #11 and #12
exactly match their local task mirrors at comparison.

Registered owner reviews for database, backend, QA, Security, observability,
documentation and Harness remain NOT_EXECUTED/NOT_VALIDATED. The profile smoke
test did not return a dispatch result and cannot substitute for those owners.

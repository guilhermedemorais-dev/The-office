# Studio PRD: approved critical discovery evolution

Date: 2026-10-21. Base main ef948a44288b1d080f142998f3870568620b4638.
Branch feat/studio-prd-evidence. Task STUDIO-PRD-002 / Issue #4 / JSON v2 revision 1.
Owner approved the audited proposal, then required technical documentation research
so recommendations do not rest on unsupported opinion. This is agent/workflow
maintenance, not implementation or build of a client product.

## Audit and compatibility

Canonical implementation: plugins/studio-prd/skills/studio-prd/SKILL.md, briefing
and planning references, briefing/PRD/plan assets, plan.py and activation metadata.
The manifests retain existing distribution; root V2 derives product-core,
product-discovery and product-planning through build_skill_routes.py. All remain
one canonical Studio source; no competing CTO skill or new execution engine.

| Capability | Before | Change |
| --- | --- | --- |
| New/existing project briefing, up to 3 questions | Adequate | Preserve |
| Actors/journeys/source/acceptance/module inventory | Adequate | Preserve |
| Separate plan MD/JSON and one Task per module | Adequate | Preserve schema/helper/gates |
| Critical debate | Implicit in global rules | Explicit local reasoning and alternatives |
| Product phase progression | Implicit, partly overlapping SDD | Product diagnosis/debate/PRD gates, no re-interview |
| Technical evidence | Research expected | Version/source/section/applicability/limits per material claim |
| Conceptual Data/Backend/UI impacts | Insufficiently explicit in Studio | Preliminary triage, detailed design stays with sectors |
| Evidence type vs approval state | Not independent enough | Distinguish nature and approval in existing tables |
| Whole-inventory research | Conflicts with V2 policy | Selective metadata and genuine-gap research |
| MVP consideration | No automatic reduction | Explicit proposal and owner decision only |
| Task required before initial discovery | Generic product contract ambiguity | No invented downstream Task/JSON prerequisite |

Six affected frozen V1 resources are archived exactly under docs/migration/v1-frozen
and explicitly mapped by verify_preservation.py. Original v1-inventory.json and
hashes unchanged. Archived source is never routed as active skill. New tamper
checks reject corrupt/missing archives, even when the live file matches old bytes.
ADRs 001 and 006 distinguish original freeze from this approved evolution.
Source slices and resource metadata are regenerated; no manual slice editing.

## Evidence protocol

Material technical recommendations inspect project constraints/code/versions,
reuse applicable knowledge and fetch original official docs/standards for gaps
or changed facts. Record what the source actually supports and why applicable,
compare alternatives/trade-offs and mark uncertainty. Source consultation is not
runtime validation. An owner-approved hypothesis remains a hypothesis. No
operational installs, benchmark or product code are authorized during discovery.

Method references read: CMU SEI QAW Third Edition (2003),
https://www.sei.cmu.edu/library/quality-attribute-workshops-qaws-third-edition/ ;
NN/g Discovery in Agile (2023), https://www.nngroup.com/articles/discovery-in-agile/ .
The phase adaptation is local; these sources are not project technology evidence.

## Actual independent skill-use scenarios

- `/root/studio_new_idea`: new 4-user ERP, 200 sales/day, proposed 20 microservices/
  Kubernetes/Redis, 2-week target, unknown permissions and last-unit race rule.
  Agent read the live Studio/briefing and consulted official PostgreSQL 18
  row-locking documentation and Kubernetes production considerations. It compared
  smaller alternatives as PROPOSED, expressed stock consistency as an observable
  invariant without implementing it, asked 3 prioritized groups and kept schedule/
  architecture unvalidated. No stack installed/selected and no files changed.
- `/root/studio_existing_scope`: approved modular Django/PostgreSQL and existing
  auth, bounded admin CSV clarification, user-approved hypothesis of instant
  unlimited heavy exports. Agent preserved architecture/previous PRD approval,
  rejected inference that approval establishes performance, kept HYPOTHESIS and
  NOT_VALIDATED, asked a targeted business trade-off and prepared SDD handoff.
  No fake research: explicitly reported only actual supplied/local sources and
  missing code/version/product evidence. No implementation or artifact edits.

These are two executed qualitative evaluations, not proof of every possible
prompt/model, production behavior or guaranteed absence of wrong decisions.
Claude executable was absent; no Claude review or replacement simulation claimed.

## Executed checks

- Full regression with optional existing Plop runtime:
  `OFFICE_PLOP_BINARY=/tmp/office-plop-validation/node_modules/.bin/plop python -m unittest discover -s tests -v`
  Exit 0: **725 discovered, 718 passed, 7 native-Windows skips**, 10.973 seconds.
  Four new tests cover frozen archive corruption/absence/original hashes and live
  product routing. Existing Studio planning regressions remain unchanged.
- `python scripts/build_skill_routes.py --check`: PASS.
- `python scripts/verify_preservation.py`: PASS, all 342 original inventory entries.
- skill-creator quick_validate canonical studio-prd: PASS.
- Current plan template validate + MD/JSON check: PASS during audit; unchanged.
- New Task JSON v2 validates with existing office.validate_contract; one complete
  Task with internal documentation, QA and reconciliation lists.
- `git diff --check`: PASS. No original test removed or weakened.

Nine instruction/reference links resolved; links inside client templates retain
their intended future client-docs location. Current plan MD/JSON equivalence passed.

Technical and usage documentation UPDATED: canonical reference/templates,
product activation prompt, spec and this guide. Product UI/capture N/A: no client
UI changed. Example prompt for the owner: "Use studio-prd to debate this product
idea. Inspect approved context, research material technical claims in official
version-matched documentation, explain alternatives/evidence/limits and prepare
PRD only when critical product decisions are settled. Do not implement."

## Limits and next gate

No client build/deploy, external dependency installation, production access,
merge, native Windows/macOS validation or Desktop activation performed. Token
metrics NOT_AVAILABLE; no numerical efficiency improvement claimed. Host agents
must actually follow and load the procedure. Final human PR acceptance remains
pending. Existing SDD contracts and plan schema are unchanged.

## Main synchronization before review

The main branch advanced to fbdcce3f9152f8a9194ef5318349fba0fb8bb706 while this
branch was being published. Both appended architecture sections were retained,
resource metadata regenerated and current documentation index linked to Studio.
Only the feature branch is synchronized; the agent does not merge this PR to main.

After synchronization the previously used temporary Plop binary was no longer
available. An initial rerun with its stale OFFICE_PLOP_BINARY path failed in that
optional runtime test (FileNotFoundError); no product/Studio failure occurred.
Reran with actual available capabilities (`env -u OFFICE_PLOP_BINARY python -m
unittest discover -s tests -v`): 725 discovered, **717 passed, 8 skips** (7 native
Windows + 1 optional Plop runtime), 10.598 seconds, exit 0. No test was removed or
modified, and Plop support is retained. Earlier full run with the supplied runtime
passed 718 tests as recorded above. No package was installed for this sync.

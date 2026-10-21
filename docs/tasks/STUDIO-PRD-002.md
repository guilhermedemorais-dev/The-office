# STUDIO-PRD-002: debate crítico com evidência técnica

Branch: feat/studio-prd-evidence. Contract revision: 1.

Single complete module Task, equivalent to [Execution Contract JSON v2](https://github.com/guilhermedemorais-dev/The-office/blob/feat/studio-prd-evidence/docs/execution/STUDIO-PRD-002.json). Owner approved proposal in conversation; PR acceptance remains separate.

## schema_version

2

## contract_revision

1

## task_id

STUDIO-PRD-002

## human_task

- **representation**: github_issue
- **issue_url**: https://github.com/guilhermedemorais-dev/The-office/issues/4
- **local_mirror**: docs/tasks/STUDIO-PRD-002.md
- **normative_equivalence**: This complete human mirror and JSON contain equivalent normative instructions; runtime evidence stays in receipts/reports.

## summary

Evolve existing Studio PRD with evidence-based critical debate.

## goal

Improve discovery and decisions without another skill owner or incompatible contracts.

## current_state

Studio has adaptive briefing and plans; critical debate is implicit, selective routing conflicts and phase gates need local clarification.

## expected_result

One canonical Studio with explicit critical/evidence workflow and compatible generated V2 routes.

## scope

Debate critically with product phases and bounded questions; preserve approved context.; Ground material technical claims in inspected version-matched primary docs, applicability and limitations.; One canonical Studio owner; conceptual Data/Backend/UI triage only, no product implementation.; Preserve existing PRD/plan/JSON v2 contracts and immutable original baseline through exact archives.; Exercise actual behavioral scenarios, regression, provenance and source routing; no guaranteed correctness claim.

## out_of_scope

Product implementation/build/deploy; Tool installation or production operations; New CTO skill or memory/task system; Merge or edits to main; Guarantees of correct decisions or token savings

## allowed_paths

plugins/studio-prd/skills/studio-prd/**; agents/product/AGENT.md; scripts/verify_preservation.py; skills/product-*/SKILL.md; library/indexes/**; docs/**; tests/test_studio_evolution.py; README.md

## protected_paths

Dev-workflow repository; destination main; credentials and runtime state; unrelated plugins, schemas and planning helper

## requirements

-
  - **id**: REQ-CRITICAL
  - **description**: Debate critically with product phases and bounded questions; preserve approved context.
  - **source**: Owner-approved audited proposal and technical evidence refinement, 2026-10-21
  - **priority**: MUST
-
  - **id**: REQ-EVIDENCE
  - **description**: Ground material technical claims in inspected version-matched primary docs, applicability and limitations.
  - **source**: Owner-approved audited proposal and technical evidence refinement, 2026-10-21
  - **priority**: MUST
-
  - **id**: REQ-BOUNDARY
  - **description**: One canonical Studio owner; conceptual Data/Backend/UI triage only, no product implementation.
  - **source**: Owner-approved audited proposal and technical evidence refinement, 2026-10-21
  - **priority**: MUST
-
  - **id**: REQ-PARITY
  - **description**: Preserve existing PRD/plan/JSON v2 contracts and immutable original baseline through exact archives.
  - **source**: Owner-approved audited proposal and technical evidence refinement, 2026-10-21
  - **priority**: MUST
-
  - **id**: REQ-VALIDATION
  - **description**: Exercise actual behavioral scenarios, regression, provenance and source routing; no guaranteed correctness claim.
  - **source**: Owner-approved audited proposal and technical evidence refinement, 2026-10-21
  - **priority**: MUST

## business_rules

-
  - **id**: RN-01
  - **description**: One cohesive Task with internal microtasks; owner approval recorded in conversation, final PR acceptance separate.

## specs

docs/specs/studio-prd.md

## docs

docs/migration/studio-prd-evolution.md

## references

-
  - **id**: REF-STUDIO
  - **title**: Canonical Studio
  - **project_path**: plugins/studio-prd/skills/studio-prd/SKILL.md
  - **section**:
  - **purpose**: Current product discovery procedure
  - **applies_to**:
    MT-01; MT-02; MT-03

## design

- **applicability**: N/A
- **reason_if_na**: No product visual interface changes

## microtasks

-
  - **id**: MT-01
  - **title**: Evolve canonical Studio and preserve archived baseline
  - **owner_skill**: dev-implementation-standard
  - **owner_plugin**: dev-implementation-standard
  - **capability**: documentation
  - **preferred_tool**: repository-native tooling
  - **depends_on**:
    None.
  - **references**:
    REF-STUDIO
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **checklist**:
    Preserve approved scope and applicable sources; Return actual evidence and limits
  - **deliverables**:
    Evolve canonical Studio and preserve archived baseline
  - **completion_condition**: Applicable acceptance evidence exists; no fabricated independent review.
  - **validator**: qa-testing-standard
-
  - **id**: MT-02
  - **title**: Validate behavior and compatible routes
  - **owner_skill**: qa-testing-standard
  - **owner_plugin**: qa-testing-standard
  - **capability**: qa
  - **preferred_tool**: repository-native tooling
  - **depends_on**:
    MT-01
  - **references**:
    REF-STUDIO
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **checklist**:
    Preserve approved scope and applicable sources; Return actual evidence and limits
  - **deliverables**:
    Validate behavior and compatible routes
  - **completion_condition**: Applicable acceptance evidence exists; no fabricated independent review.
  - **validator**: dev-workflow-standard
-
  - **id**: MT-03
  - **title**: Reconcile evidence and prepare review
  - **owner_skill**: dev-workflow-standard
  - **owner_plugin**: dev-workflow-standard
  - **capability**: harness
  - **preferred_tool**: repository-native tooling
  - **depends_on**:
    MT-01; MT-02
  - **references**:
    REF-STUDIO
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **checklist**:
    Preserve approved scope and applicable sources; Return actual evidence and limits
  - **deliverables**:
    Reconcile evidence and prepare review
  - **completion_condition**: Applicable acceptance evidence exists; no fabricated independent review.
  - **validator**: dev-workflow-standard

## execution_lists

-
  - **list_id**: MT-01/checklist
  - **owner_skill**: dev-implementation-standard
  - **phase**: implementation
  - **objective**: Evolve canonical Studio and preserve archived baseline
  - **microtask_ids**:
    MT-01
  - **depends_on**:
    None.
  - **references**:
    REF-STUDIO
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **required_tests**:
    TEST-REGRESSION; TEST-SCENARIOS
  - **acceptance_criteria**:
    AC-CRITICAL; AC-EVIDENCE; AC-BOUNDARY; AC-PARITY; AC-VALIDATION
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Preserve approved scope and applicable sources
    -
      - **instruction**: Return actual evidence and limits
  - **completion_condition**: Applicable acceptance evidence exists; no fabricated independent review.
  - **deliverables**:
    Evolve canonical Studio and preserve archived baseline
-
  - **list_id**: MT-02/checklist
  - **owner_skill**: qa-testing-standard
  - **phase**: validation
  - **objective**: Validate behavior and compatible routes
  - **microtask_ids**:
    MT-02
  - **depends_on**:
    MT-01
  - **references**:
    REF-STUDIO
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **required_tests**:
    TEST-REGRESSION; TEST-SCENARIOS
  - **acceptance_criteria**:
    AC-CRITICAL; AC-EVIDENCE; AC-BOUNDARY; AC-PARITY; AC-VALIDATION
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Preserve approved scope and applicable sources
    -
      - **instruction**: Return actual evidence and limits
  - **completion_condition**: Applicable acceptance evidence exists; no fabricated independent review.
  - **deliverables**:
    Validate behavior and compatible routes
-
  - **list_id**: MT-03/checklist
  - **owner_skill**: dev-workflow-standard
  - **phase**: validation
  - **objective**: Reconcile evidence and prepare review
  - **microtask_ids**:
    MT-03
  - **depends_on**:
    MT-01; MT-02
  - **references**:
    REF-STUDIO
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **required_tests**:
    TEST-REGRESSION; TEST-SCENARIOS
  - **acceptance_criteria**:
    AC-CRITICAL; AC-EVIDENCE; AC-BOUNDARY; AC-PARITY; AC-VALIDATION
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Preserve approved scope and applicable sources
    -
      - **instruction**: Return actual evidence and limits
  - **completion_condition**: Applicable acceptance evidence exists; no fabricated independent review.
  - **deliverables**:
    Reconcile evidence and prepare review

## sectors

- **database**:
  - **owner**: dev-implementation-standard
  - **applicability**: N/A
  - **reason**: Instruction/template evolution only; no product UI/data/runtime/infrastructure or security-boundary change.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    None.
  - **required_validations**:
    None.
- **backend**:
  - **owner**: dev-implementation-standard
  - **applicability**: N/A
  - **reason**: Instruction/template evolution only; no product UI/data/runtime/infrastructure or security-boundary change.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    None.
  - **required_validations**:
    None.
- **frontend**:
  - **owner**: dev-implementation-standard
  - **applicability**: N/A
  - **reason**: Instruction/template evolution only; no product UI/data/runtime/infrastructure or security-boundary change.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    None.
  - **required_validations**:
    None.
- **ui_ux**:
  - **owner**: ui-ux-standard
  - **applicability**: N/A
  - **reason**: Instruction/template evolution only; no product UI/data/runtime/infrastructure or security-boundary change.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    None.
  - **required_validations**:
    None.
- **qa**:
  - **owner**: qa-testing-standard
  - **applicability**: REQUIRED
  - **reason**: Validate behavior and compatible routes
  - **depends_on**:
    documentation
  - **microtasks**:
    MT-02
  - **required_sources**:
    REF-STUDIO
  - **required_validations**:
    TEST-REGRESSION; TEST-SCENARIOS
- **security**:
  - **owner**: security-standard
  - **applicability**: N/A
  - **reason**: Instruction/template evolution only; no product UI/data/runtime/infrastructure or security-boundary change.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    None.
  - **required_validations**:
    None.
- **devops**:
  - **owner**: devops-standard
  - **applicability**: N/A
  - **reason**: Instruction/template evolution only; no product UI/data/runtime/infrastructure or security-boundary change.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    None.
  - **required_validations**:
    None.
- **observability**:
  - **owner**: devops-standard
  - **applicability**: N/A
  - **reason**: Instruction/template evolution only; no product UI/data/runtime/infrastructure or security-boundary change.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    None.
  - **required_validations**:
    None.
- **documentation**:
  - **owner**: dev-implementation-standard
  - **applicability**: REQUIRED
  - **reason**: Evolve canonical Studio and preserve archived baseline
  - **depends_on**:
    None.
  - **microtasks**:
    MT-01
  - **required_sources**:
    REF-STUDIO
  - **required_validations**:
    TEST-REGRESSION; TEST-SCENARIOS
- **harness**:
  - **owner**: dev-workflow-standard
  - **applicability**: REQUIRED
  - **reason**: Reconcile evidence and prepare review
  - **depends_on**:
    documentation; qa
  - **microtasks**:
    MT-03
  - **required_sources**:
    REF-STUDIO
  - **required_validations**:
    TEST-REGRESSION; TEST-SCENARIOS

## required_tests

-
  - **id**: TEST-REGRESSION
  - **type**: regression
  - **command**: python -m unittest discover -s tests -v; python scripts/build_skill_routes.py --check; python scripts/verify_preservation.py
  - **expected**: No introduced failures; original hashes retained.
-
  - **id**: TEST-SCENARIOS
  - **type**: behavior
  - **command**: Actual read-only independent agent use on new and existing project scenarios
  - **expected**: Evidence-backed alternatives, no fake approvals, bounded questions and preserved scope.

## acceptance_criteria

-
  - **id**: AC-CRITICAL
  - **description**: Debate critically with product phases and bounded questions; preserve approved context.
  - **validation**: TEST-SCENARIOS
-
  - **id**: AC-EVIDENCE
  - **description**: Ground material technical claims in inspected version-matched primary docs, applicability and limitations.
  - **validation**: TEST-SCENARIOS
-
  - **id**: AC-BOUNDARY
  - **description**: One canonical Studio owner; conceptual Data/Backend/UI triage only, no product implementation.
  - **validation**: TEST-SCENARIOS
-
  - **id**: AC-PARITY
  - **description**: Preserve existing PRD/plan/JSON v2 contracts and immutable original baseline through exact archives.
  - **validation**: TEST-REGRESSION
-
  - **id**: AC-VALIDATION
  - **description**: Exercise actual behavioral scenarios, regression, provenance and source routing; no guaranteed correctness claim.
  - **validation**: TEST-SCENARIOS

## stop_conditions

source_of_truth_conflict; authorization_required; material scope change; unavailable required evidence

## gates

- **scope**: Owner explicitly approved proposal and evidence refinement in conversation
- **final_acceptance**: Human PR review pending
- **merge_deploy**: Not authorized

## reporting

- **evidence**: docs/migration/studio-prd-evolution.md
- **tokens**: Record actual metrics or NOT_AVAILABLE, never estimates as facts

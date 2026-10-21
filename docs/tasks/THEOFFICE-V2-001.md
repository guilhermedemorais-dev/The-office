# THEOFFICE-V2-001: Restructure Dev-workflow as The Office V2

> **Resumo:** Restructure Dev-workflow as The Office V2 without losing V1 capabilities.

contract_revision: 1. Complexity: COMPLEX. Branch: `feat/the-office-v2`. Issue: https://github.com/guilhermedemorais-dev/The-office/issues/1.

Normative instructions below mirror the single [Execution Contract](../execution/THEOFFICE-V2-001.json). Runtime status and evidence belong in Issue comments/receipts, not JSON. User approved PRD and construction/push; merge and deploy are excluded.

<!-- contract-field: schema_version -->
## schema_version

2

<!-- /contract-field: schema_version -->

<!-- contract-field: contract_revision -->
## contract_revision

1

<!-- /contract-field: contract_revision -->

<!-- contract-field: task_id -->
## task_id

THEOFFICE-V2-001

<!-- /contract-field: task_id -->

<!-- contract-field: human_task -->
## human_task

- **representation**: github_issue
- **issue_url**: https://github.com/guilhermedemorais-dev/The-office/issues/1
- **local_mirror**: docs/tasks/THEOFFICE-V2-001.md
- **normative_equivalence**: The GitHub Issue and this JSON contain the same approved normative requirements. Runtime evidence remains in Issue comments and receipts.

<!-- /contract-field: human_task -->

<!-- contract-field: summary -->
## summary

Restructure Dev-workflow as The Office V2 without losing V1 capabilities.

<!-- /contract-field: summary -->

<!-- contract-field: goal -->
## goal

Deliver a reviewable modular sector Harness, installable from an isolated branch, preserving existing governance and tools.

<!-- /contract-field: goal -->

<!-- contract-field: current_state -->
## current_state

Dev-workflow V1 at af94e8022eaec3e4eedfb4a2a62e13c6b349b9c4 provides interconnected skills, tools, catalogs and tests; destination main initially holds README and LICENSE.

<!-- /contract-field: current_state -->

<!-- contract-field: expected_result -->
## expected_result

Additive V2 agent/skill/library/environment overlay, traceable source coverage, current regression evidence and a destination PR for owner acceptance.

<!-- /contract-field: expected_result -->

<!-- contract-field: scope -->
## scope

Audit complete V1 and record source SHA, dependencies, rules, catalogs, contracts and baseline.; Create 14 sector contracts and transversal librarian; select skills and sources progressively without losing mandatory rules.; Decompose large skills by function with section-level provenance and compatibility references.; Provide shared metadata lookup and targeted retrieval with local/private separation and no automatic external execution.; Preserve environment bootstrap, provider routing, REA, catalogs and existing contracts; distinguish Linux, Win10, Win11, macOS and host support.; Document architecture, migration, install, operational workflows and contextual product-documentation templates.; Execute inherited and new tests, measured benchmark scenarios and evidence; publish commits and PR on destination branch.

<!-- /contract-field: scope -->

<!-- contract-field: out_of_scope -->
## out_of_scope

Modify Dev-workflow source repository or main.; Merge, deploy, production changes, destructive operations or unknown credentials.; Install unknown external tools or publish private local catalog data.; Reimplement third-party REA or create a simulated office UI.; Claim native platform homologation, token savings or live provider execution without executed evidence.

<!-- /contract-field: out_of_scope -->

<!-- contract-field: allowed_paths -->
## allowed_paths

AGENTS.md; README.md; agents/**; skills/**; library/**; environment/**; integrations/**; contracts/**; docs/**; scripts/**; tests/**; .github/**; .codex-plugin/**; .claude-plugin/**

<!-- /contract-field: allowed_paths -->

<!-- contract-field: protected_paths -->
## protected_paths

plugins/** (preserve imported V1 bytes; changes require documented necessity and regression); Dev-workflow source repository; destination main; credentials and private runtime state

<!-- /contract-field: protected_paths -->

<!-- contract-field: requirements -->
## requirements

-
  - **id**: REQ-PARITY
  - **description**: Preserve every V1 file/section or document justified mapping; no destructive summaries.
  - **source**: docs/specs/the-office-v2.md#requirements
  - **priority**: MUST
-
  - **id**: REQ-ROUTING
  - **description**: Select only necessary agents, skills and mandatory dependencies/references.
  - **source**: docs/specs/the-office-v2.md#requirements
  - **priority**: MUST
-
  - **id**: REQ-GOVERNANCE
  - **description**: Keep Issue/JSON v2 equivalence, receipts, revisions, owner evidence and one Task per module.
  - **source**: docs/specs/the-office-v2.md#requirements
  - **priority**: MUST
-
  - **id**: REQ-LIBRARY
  - **description**: Share metadata discovery, source provenance and incremental local/project knowledge; external gaps remain conditional.
  - **source**: docs/specs/the-office-v2.md#requirements
  - **priority**: MUST
-
  - **id**: REQ-ENVIRONMENT
  - **description**: Keep actual support/availability/install/config/auth/verification separate by OS and host.
  - **source**: docs/specs/the-office-v2.md#requirements
  - **priority**: MUST
-
  - **id**: REQ-REA
  - **description**: Preserve original reverse-engineering runtime, distribution and interfaces.
  - **source**: docs/specs/the-office-v2.md#requirements
  - **priority**: MUST
-
  - **id**: REQ-DOCUMENTATION
  - **description**: Document implemented behavior, reusable templates and source-linked Help Center procedure; no fictitious captures.
  - **source**: docs/specs/the-office-v2.md#requirements
  - **priority**: MUST
-
  - **id**: REQ-VALIDATION
  - **description**: Execute regressions and representative scenarios; report actual metrics or NOT_AVAILABLE.
  - **source**: docs/specs/the-office-v2.md#requirements
  - **priority**: MUST
-
  - **id**: REQ-DELIVERY
  - **description**: Commit and push isolated destination branch; PR for human acceptance, no merge or deploy.
  - **source**: docs/specs/the-office-v2.md#requirements
  - **priority**: MUST

<!-- /contract-field: requirements -->

<!-- contract-field: business_rules -->
## business_rules

-
  - **id**: RN-01
  - **description**: One cohesive migration Task with internal microtasks; no Task per layer or skill.
  - **source**: docs/specs/the-office-v2.md#business-rules
-
  - **id**: RN-02
  - **description**: No evidence is not PASS; only sector owner attests current scope/revision.
  - **source**: docs/architecture/flows.md
-
  - **id**: RN-03
  - **description**: User PRD authorizes construction and isolated-branch push, not merge/deploy or destructive scope.
  - **source**: docs/specs/the-office-v2.md#authorization

<!-- /contract-field: business_rules -->

<!-- contract-field: specs -->
## specs

docs/specs/the-office-v2.md

<!-- /contract-field: specs -->

<!-- contract-field: docs -->
## docs

docs/architecture/overview.md; docs/operations/installation.md; docs/operations/user-guide.md; docs/operations/documentation.md

<!-- /contract-field: docs -->

<!-- contract-field: references -->
## references

-
  - **id**: SPEC
  - **title**: Approved scope and behavioral constraints
  - **source_url**: https://github.com/guilhermedemorais-dev/The-office
  - **project_path**: docs/specs/the-office-v2.md
  - **section**:
  - **purpose**: Approved scope and behavioral constraints
  - **applies_to**:
    MT-01; MT-03; MT-04; MT-05; MT-06; MT-07; MT-08; MT-09; MT-10; MT-11; MT-12; MT-13
-
  - **id**: V1-HARNESS
  - **title**: Preserve canonical orchestration invariants
  - **source_url**: https://github.com/guilhermedemorais-dev/The-office
  - **project_path**: plugins/dev-workflow-standard/skills/dev-workflow-standard/SKILL.md
  - **section**:
  - **purpose**: Preserve canonical orchestration invariants
  - **applies_to**:
    MT-01; MT-02; MT-05
-
  - **id**: V1-SDD
  - **title**: Preserve spec/Task semantics
  - **source_url**: https://github.com/guilhermedemorais-dev/The-office
  - **project_path**: plugins/sdd-spec-factory/skills/sdd-spec-factory/SKILL.md
  - **section**:
  - **purpose**: Preserve spec/Task semantics
  - **applies_to**:
    MT-02; MT-05
-
  - **id**: V1-ROUTING
  - **title**: Canonical sectors, dependency phases, handoff and equivalence
  - **source_url**: https://github.com/guilhermedemorais-dev/The-office
  - **project_path**: plugins/dev-workflow-standard/skills/dev-workflow-standard/references/context-routing.md
  - **section**:
  - **purpose**: Canonical sectors, dependency phases, handoff and equivalence
  - **applies_to**:
    MT-03; MT-04; MT-10; MT-12
-
  - **id**: V1-ENV
  - **title**: Reuse environment preparation and state
  - **source_url**: https://github.com/guilhermedemorais-dev/The-office
  - **project_path**: plugins/dev-environment-standard/skills/dev-environment-standard/SKILL.md
  - **section**:
  - **purpose**: Reuse environment preparation and state
  - **applies_to**:
    MT-07
-
  - **id**: V1-REA
  - **title**: Preserve original reverse-engineering provider/runtime
  - **source_url**: https://github.com/guilhermedemorais-dev/The-office
  - **project_path**: plugins/reverse-engineering-standard/skills/reverse-engineering-standard/SKILL.md
  - **section**:
  - **purpose**: Preserve original reverse-engineering provider/runtime
  - **applies_to**:
    MT-08
-
  - **id**: V1-QA
  - **title**: Independent QA scope and evidence
  - **source_url**: https://github.com/guilhermedemorais-dev/The-office
  - **project_path**: plugins/qa-testing-standard/skills/qa-testing-standard/SKILL.md
  - **section**:
  - **purpose**: Independent QA scope and evidence
  - **applies_to**:
    MT-10; MT-11
-
  - **id**: V1-SEC
  - **title**: Independent scoped security validation
  - **source_url**: https://github.com/guilhermedemorais-dev/The-office
  - **project_path**: plugins/security-standard/skills/security-standard/SKILL.md
  - **section**:
  - **purpose**: Independent scoped security validation
  - **applies_to**:
    MT-13
-
  - **id**: TEMPLATES
  - **title**: Select verified documentation models and source metadata
  - **source_url**: https://github.com/guilhermedemorais-dev/The-office
  - **project_path**: library/documentation-templates/README.md
  - **section**:
  - **purpose**: Select verified documentation models and source metadata
  - **applies_to**:
    MT-09

<!-- /contract-field: references -->

<!-- contract-field: design -->
## design

- **applicability**: N/A
- **guide**: N/A
- **tokens**: N/A
- **visual_references**:
  None.
- **component_library**: N/A
- **mockup**: N/A
- **reason_if_na**: No product UI in approved migration; agent/CLI/docs Harness only. UX procedural decomposition is preserved, not a new visual application.

<!-- /contract-field: design -->

<!-- contract-field: microtasks -->
## microtasks

-
  - **id**: MT-01
  - **title**: Preparation
  - **summary**: Preparation: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **owner_skill**: dev-workflow-standard
  - **owner_plugin**: dev-workflow-standard
  - **capability**: preparation
  - **preferred_tool**: repository-native-tooling
  - **depends_on**:
    None.
  - **references**:
    SPEC; V1-HARNESS
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **checklist**:
    Confirm source/destination, permissions, branch and source SHA.; Preserve destination files and record clean checkout/baseline.
  - **deliverables**:
    docs/migration/baseline.md
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **validator**: qa-testing-standard
-
  - **id**: MT-02
  - **title**: Audit V1
  - **summary**: Audit V1: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **owner_skill**: dev-workflow-standard
  - **owner_plugin**: dev-workflow-standard
  - **capability**: audit-v1
  - **preferred_tool**: repository-native-tooling
  - **depends_on**:
    MT-01
  - **references**:
    V1-HARNESS; V1-SDD
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **checklist**:
    Inventory every plugin, skill, script, catalog, contract and test.; Map dependencies, duplicated/conflicting rules, host/OS gaps and context hotspots.; Execute baseline tests and retain raw results including failures.
  - **deliverables**:
    docs/migration/v1-inventory.md; docs/migration/dependency-map.md; docs/migration/rules-audit.md
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **validator**: qa-testing-standard
-
  - **id**: MT-03
  - **title**: Architecture
  - **summary**: Architecture: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **owner_skill**: sdd-spec-factory
  - **owner_plugin**: sdd-spec-factory
  - **capability**: architecture
  - **preferred_tool**: repository-native-tooling
  - **depends_on**:
    MT-02
  - **references**:
    SPEC; V1-ROUTING
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **checklist**:
    Define sector boundaries, selective loading, shared library and incremental compatibility.; Record V1-to-V2 responsibility map, ADRs and benchmark strategy.
  - **deliverables**:
    docs/architecture/overview.md; docs/architecture/agents.md; docs/architecture/flows.md; docs/migration/v1-to-v2.md
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **validator**: qa-testing-standard
-
  - **id**: MT-04
  - **title**: Contracts and routing
  - **summary**: Contracts and routing: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **owner_skill**: dev-implementation-standard
  - **owner_plugin**: dev-implementation-standard
  - **capability**: contracts-and-routing
  - **preferred_tool**: repository-native-tooling
  - **depends_on**:
    MT-03
  - **references**:
    SPEC; V1-ROUTING
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **checklist**:
    Create concise sector contracts and explicit selective-routing helper.; Preserve JSON v2/receipt ownership and dependency semantics; reject bad revisions, unknown IDs and conflicts.; Exercise handoffs and resumption without claiming execution from a generated plan.
  - **deliverables**:
    agents/; scripts/office.py; contracts/
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **validator**: qa-testing-standard
-
  - **id**: MT-05
  - **title**: Functional skills
  - **summary**: Functional skills: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **owner_skill**: dev-implementation-standard
  - **owner_plugin**: dev-implementation-standard
  - **capability**: functional-skills
  - **preferred_tool**: repository-native-tooling
  - **depends_on**:
    MT-04
  - **references**:
    SPEC; V1-HARNESS; V1-SDD
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **checklist**:
    Read original skills completely; inventory their sections and mandatory rules.; Decompose functional capabilities with core dependencies and source hashes.; Preserve original references/scripts and verify every section has a destination.
  - **deliverables**:
    skills/; library/indexes/skill-routes.json; docs/migration/
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **validator**: qa-testing-standard
-
  - **id**: MT-06
  - **title**: Shared librarian
  - **summary**: Shared librarian: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **owner_skill**: dev-implementation-standard
  - **owner_plugin**: dev-implementation-standard
  - **capability**: shared-librarian
  - **preferred_tool**: repository-native-tooling
  - **depends_on**:
    MT-05
  - **references**:
    SPEC
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **checklist**:
    Index preserved catalogs by metadata, provenance, license and source digest.; Lookup Task/project/local/distributed resources before conditional external research.; Retrieve only selected bodies and detect stale/missing resources; never execute unknown code.
  - **deliverables**:
    library/; scripts/office.py
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **validator**: qa-testing-standard
-
  - **id**: MT-07
  - **title**: Environment
  - **summary**: Environment: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **owner_skill**: dev-environment-standard
  - **owner_plugin**: dev-environment-standard
  - **capability**: environment
  - **preferred_tool**: repository-native-tooling
  - **depends_on**:
    MT-06
  - **references**:
    SPEC; V1-ENV
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **checklist**:
    Reuse shared environment scripts and imported catalogs.; Describe Linux, Win10, Win11 and macOS separately; WSL is Linux.; Test healthy/partial/missing tooling and changed-platform state without claiming native homologation.
  - **deliverables**:
    environment/; docs/operations/installation.md
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **validator**: qa-testing-standard
-
  - **id**: MT-08
  - **title**: Reverse engineering
  - **summary**: Reverse engineering: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **owner_skill**: dev-environment-standard
  - **owner_plugin**: dev-environment-standard
  - **capability**: reverse-engineering
  - **preferred_tool**: repository-native-tooling
  - **depends_on**:
    MT-07
  - **references**:
    SPEC; V1-REA
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **checklist**:
    Identify and preserve original REA provider, version/provenance, gateway and supplementary tools.; Test safe discovery/fixture routing where available and record unavailable runtime dependencies.; Do not substitute prompts or new engines for the original runtime.
  - **deliverables**:
    integrations/reverse-engineering/
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **validator**: qa-testing-standard
-
  - **id**: MT-09
  - **title**: Documentation
  - **summary**: Documentation: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **owner_skill**: dev-implementation-standard
  - **owner_plugin**: dev-implementation-standard
  - **capability**: documentation
  - **preferred_tool**: repository-native-tooling
  - **depends_on**:
    MT-08
  - **references**:
    SPEC; TEMPLATES
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **checklist**:
    Document actual architecture, contracts, skills, installation and execution.; Provide contextual product manuals, verified-source templates and visual capture provenance workflow.; Specify optional Help Center reuse of versioned product content; record absent capture/render validation.
  - **deliverables**:
    docs/operations/; library/documentation-templates/
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **validator**: qa-testing-standard
-
  - **id**: MT-10
  - **title**: Regression QA
  - **summary**: Regression QA: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **owner_skill**: qa-testing-standard
  - **owner_plugin**: qa-testing-standard
  - **capability**: regression-qa
  - **preferred_tool**: repository-native-tooling
  - **depends_on**:
    MT-09
  - **references**:
    SPEC; V1-QA; V1-ROUTING
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **checklist**:
    Run full inherited and added tests; record exact command, exit code and skips.; Cover routes, references, contracts, evidence dependencies, fallbacks, library, environment, REA and install boundaries.; Return introduced failures for rework and retest; leave unsupported platforms NOT_VALIDATED.
  - **deliverables**:
    docs/migration/validation evidence and raw test logs
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **validator**: dev-workflow-standard
-
  - **id**: MT-11
  - **title**: Comparative benchmarks
  - **summary**: Comparative benchmarks: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **owner_skill**: qa-testing-standard
  - **owner_plugin**: qa-testing-standard
  - **capability**: comparative-benchmarks
  - **preferred_tool**: repository-native-tooling
  - **depends_on**:
    MT-10
  - **references**:
    SPEC; V1-QA
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **checklist**:
    Exercise scenarios A-F from approved PRD with comparable local inputs.; Measure observable loading/tool/latency/retry results; record model token telemetry as NOT_AVAILABLE when unavailable.; Distinguish static route measurements from end-to-end LLM execution quality.
  - **deliverables**:
    docs/migration/benchmark evidence
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **validator**: dev-workflow-standard
-
  - **id**: MT-12
  - **title**: Publication
  - **summary**: Publication: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **owner_skill**: dev-workflow-standard
  - **owner_plugin**: dev-workflow-standard
  - **capability**: publication
  - **preferred_tool**: repository-native-tooling
  - **depends_on**:
    MT-10; MT-11; MT-13
  - **references**:
    SPEC; V1-ROUTING
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **checklist**:
    Review diff, secrets, new/deleted files, docs and current owner validation evidence.; Commit organized changes and push feat/the-office-v2 to confirmed The-office destination.; Open PR when supported and report source SHA, commits, tests, unresolved limits, installation and smoke tests.; Do not merge, deploy or modify source main.
  - **deliverables**:
    Published destination branch and review PR; Final evidence report
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **validator**: qa-testing-standard
-
  - **id**: MT-13
  - **title**: Independent security review
  - **summary**: Independent security review: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **owner_skill**: security-standard
  - **owner_plugin**: security-standard
  - **capability**: independent-security-review
  - **preferred_tool**: repository-native-tooling
  - **depends_on**:
    MT-04; MT-06
  - **references**:
    SPEC; V1-SEC
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **checklist**:
    Inspect routing, source retrieval, private-state boundaries and external-execution/install safeguards.; Verify negative paths for unsafe paths and malformed inputs with scoped evidence.; Report residual risks and unresolved runtime boundaries; do not attest other sectors.
  - **deliverables**:
    docs/migration/security review evidence
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **validator**: qa-testing-standard

<!-- /contract-field: microtasks -->

<!-- contract-field: execution_lists -->
## execution_lists

-
  - **list_id**: MT-01/checklist
  - **owner_skill**: dev-workflow-standard
  - **phase**: implementation
  - **objective**: Preparation: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **microtask_ids**:
    MT-01
  - **depends_on**:
    None.
  - **references**:
    SPEC; V1-HARNESS
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **deliverables**:
    docs/migration/baseline.md
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **required_tests**:
    TEST-01; TEST-02
  - **acceptance_criteria**:
    AC-01; AC-02; AC-03
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Confirm source/destination, permissions, branch and source SHA.
    -
      - **instruction**: Preserve destination files and record clean checkout/baseline.
-
  - **list_id**: MT-02/checklist
  - **owner_skill**: dev-workflow-standard
  - **phase**: implementation
  - **objective**: Audit V1: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **microtask_ids**:
    MT-02
  - **depends_on**:
    MT-01
  - **references**:
    V1-HARNESS; V1-SDD
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **deliverables**:
    docs/migration/v1-inventory.md; docs/migration/dependency-map.md; docs/migration/rules-audit.md
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **required_tests**:
    TEST-01; TEST-02
  - **acceptance_criteria**:
    AC-01; AC-02; AC-03
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Inventory every plugin, skill, script, catalog, contract and test.
    -
      - **instruction**: Map dependencies, duplicated/conflicting rules, host/OS gaps and context hotspots.
    -
      - **instruction**: Execute baseline tests and retain raw results including failures.
-
  - **list_id**: MT-03/checklist
  - **owner_skill**: sdd-spec-factory
  - **phase**: implementation
  - **objective**: Architecture: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **microtask_ids**:
    MT-03
  - **depends_on**:
    MT-02
  - **references**:
    SPEC; V1-ROUTING
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **deliverables**:
    docs/architecture/overview.md; docs/architecture/agents.md; docs/architecture/flows.md; docs/migration/v1-to-v2.md
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **required_tests**:
    TEST-01; TEST-02
  - **acceptance_criteria**:
    AC-01; AC-02; AC-03
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Define sector boundaries, selective loading, shared library and incremental compatibility.
    -
      - **instruction**: Record V1-to-V2 responsibility map, ADRs and benchmark strategy.
-
  - **list_id**: MT-04/checklist
  - **owner_skill**: dev-implementation-standard
  - **phase**: implementation
  - **objective**: Contracts and routing: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **microtask_ids**:
    MT-04
  - **depends_on**:
    MT-03
  - **references**:
    SPEC; V1-ROUTING
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **deliverables**:
    agents/; scripts/office.py; contracts/
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **required_tests**:
    TEST-01; TEST-02
  - **acceptance_criteria**:
    AC-01; AC-02; AC-03
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Create concise sector contracts and explicit selective-routing helper.
    -
      - **instruction**: Preserve JSON v2/receipt ownership and dependency semantics; reject bad revisions, unknown IDs and conflicts.
    -
      - **instruction**: Exercise handoffs and resumption without claiming execution from a generated plan.
-
  - **list_id**: MT-05/checklist
  - **owner_skill**: dev-implementation-standard
  - **phase**: implementation
  - **objective**: Functional skills: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **microtask_ids**:
    MT-05
  - **depends_on**:
    MT-04
  - **references**:
    SPEC; V1-HARNESS; V1-SDD
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **deliverables**:
    skills/; library/indexes/skill-routes.json; docs/migration/
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **required_tests**:
    TEST-01; TEST-02
  - **acceptance_criteria**:
    AC-01; AC-02; AC-03
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Read original skills completely; inventory their sections and mandatory rules.
    -
      - **instruction**: Decompose functional capabilities with core dependencies and source hashes.
    -
      - **instruction**: Preserve original references/scripts and verify every section has a destination.
-
  - **list_id**: MT-06/checklist
  - **owner_skill**: dev-implementation-standard
  - **phase**: implementation
  - **objective**: Shared librarian: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **microtask_ids**:
    MT-06
  - **depends_on**:
    MT-05
  - **references**:
    SPEC
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **deliverables**:
    library/; scripts/office.py
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **required_tests**:
    TEST-01; TEST-02
  - **acceptance_criteria**:
    AC-01; AC-02; AC-03
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Index preserved catalogs by metadata, provenance, license and source digest.
    -
      - **instruction**: Lookup Task/project/local/distributed resources before conditional external research.
    -
      - **instruction**: Retrieve only selected bodies and detect stale/missing resources; never execute unknown code.
-
  - **list_id**: MT-07/checklist
  - **owner_skill**: dev-environment-standard
  - **phase**: implementation
  - **objective**: Environment: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **microtask_ids**:
    MT-07
  - **depends_on**:
    MT-06
  - **references**:
    SPEC; V1-ENV
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **deliverables**:
    environment/; docs/operations/installation.md
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **required_tests**:
    TEST-01; TEST-02
  - **acceptance_criteria**:
    AC-01; AC-02; AC-03
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Reuse shared environment scripts and imported catalogs.
    -
      - **instruction**: Describe Linux, Win10, Win11 and macOS separately; WSL is Linux.
    -
      - **instruction**: Test healthy/partial/missing tooling and changed-platform state without claiming native homologation.
-
  - **list_id**: MT-08/checklist
  - **owner_skill**: dev-environment-standard
  - **phase**: implementation
  - **objective**: Reverse engineering: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **microtask_ids**:
    MT-08
  - **depends_on**:
    MT-07
  - **references**:
    SPEC; V1-REA
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **deliverables**:
    integrations/reverse-engineering/
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **required_tests**:
    TEST-01; TEST-02
  - **acceptance_criteria**:
    AC-01; AC-02; AC-03
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Identify and preserve original REA provider, version/provenance, gateway and supplementary tools.
    -
      - **instruction**: Test safe discovery/fixture routing where available and record unavailable runtime dependencies.
    -
      - **instruction**: Do not substitute prompts or new engines for the original runtime.
-
  - **list_id**: MT-09/checklist
  - **owner_skill**: dev-implementation-standard
  - **phase**: implementation
  - **objective**: Documentation: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **microtask_ids**:
    MT-09
  - **depends_on**:
    MT-08
  - **references**:
    SPEC; TEMPLATES
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **deliverables**:
    docs/operations/; library/documentation-templates/
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **required_tests**:
    TEST-01; TEST-02
  - **acceptance_criteria**:
    AC-01; AC-02; AC-03
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Document actual architecture, contracts, skills, installation and execution.
    -
      - **instruction**: Provide contextual product manuals, verified-source templates and visual capture provenance workflow.
    -
      - **instruction**: Specify optional Help Center reuse of versioned product content; record absent capture/render validation.
-
  - **list_id**: MT-10/checklist
  - **owner_skill**: qa-testing-standard
  - **phase**: validation
  - **objective**: Regression QA: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **microtask_ids**:
    MT-10
  - **depends_on**:
    MT-09
  - **references**:
    SPEC; V1-QA; V1-ROUTING
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **deliverables**:
    docs/migration/validation evidence and raw test logs
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **required_tests**:
    TEST-01; TEST-02
  - **acceptance_criteria**:
    AC-01; AC-02; AC-03
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Run full inherited and added tests; record exact command, exit code and skips.
    -
      - **instruction**: Cover routes, references, contracts, evidence dependencies, fallbacks, library, environment, REA and install boundaries.
    -
      - **instruction**: Return introduced failures for rework and retest; leave unsupported platforms NOT_VALIDATED.
-
  - **list_id**: MT-11/checklist
  - **owner_skill**: qa-testing-standard
  - **phase**: validation
  - **objective**: Comparative benchmarks: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **microtask_ids**:
    MT-11
  - **depends_on**:
    MT-10
  - **references**:
    SPEC; V1-QA
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **deliverables**:
    docs/migration/benchmark evidence
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **required_tests**:
    TEST-01; TEST-02
  - **acceptance_criteria**:
    AC-01; AC-02; AC-03
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Exercise scenarios A-F from approved PRD with comparable local inputs.
    -
      - **instruction**: Measure observable loading/tool/latency/retry results; record model token telemetry as NOT_AVAILABLE when unavailable.
    -
      - **instruction**: Distinguish static route measurements from end-to-end LLM execution quality.
-
  - **list_id**: MT-12/checklist
  - **owner_skill**: dev-workflow-standard
  - **phase**: implementation
  - **objective**: Publication: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **microtask_ids**:
    MT-12
  - **depends_on**:
    MT-10; MT-11; MT-13
  - **references**:
    SPEC; V1-ROUTING
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **deliverables**:
    Published destination branch and review PR; Final evidence report
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **required_tests**:
    TEST-01; TEST-02
  - **acceptance_criteria**:
    AC-01; AC-02; AC-03
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Review diff, secrets, new/deleted files, docs and current owner validation evidence.
    -
      - **instruction**: Commit organized changes and push feat/the-office-v2 to confirmed The-office destination.
    -
      - **instruction**: Open PR when supported and report source SHA, commits, tests, unresolved limits, installation and smoke tests.
    -
      - **instruction**: Do not merge, deploy or modify source main.
-
  - **list_id**: MT-13/checklist
  - **owner_skill**: security-standard
  - **phase**: validation
  - **objective**: Independent security review: implement the approved migration slice while retaining global scope, parity and evidence invariants.
  - **microtask_ids**:
    MT-13
  - **depends_on**:
    MT-04; MT-06
  - **references**:
    SPEC; V1-SEC
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **deliverables**:
    docs/migration/security review evidence
  - **completion_condition**: Deliverables exist, applicable requirements are covered and actual validation evidence is recorded without unresolved introduced failures.
  - **required_tests**:
    TEST-01; TEST-02
  - **acceptance_criteria**:
    AC-01; AC-02; AC-03
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Inspect routing, source retrieval, private-state boundaries and external-execution/install safeguards.
    -
      - **instruction**: Verify negative paths for unsafe paths and malformed inputs with scoped evidence.
    -
      - **instruction**: Report residual risks and unresolved runtime boundaries; do not attest other sectors.

<!-- /contract-field: execution_lists -->

<!-- contract-field: sectors -->
## sectors

- **database**:
  - **owner**: dev-implementation-standard
  - **applicability**: N/A
  - **reason**: No database product surface introduced by this CLI/agent/documentation migration.
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
  - **applicability**: REQUIRED
  - **reason**: Required approved migration responsibility.
  - **depends_on**:
    None.
  - **microtasks**:
    MT-04; MT-05; MT-06
  - **required_sources**:
    SPEC; V1-ROUTING
  - **required_validations**:
    backend-validation
- **frontend**:
  - **owner**: dev-implementation-standard
  - **applicability**: N/A
  - **reason**: No frontend product surface introduced by this CLI/agent/documentation migration.
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
  - **reason**: No ui_ux product surface introduced by this CLI/agent/documentation migration.
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
  - **reason**: Required approved migration responsibility.
  - **depends_on**:
    backend; documentation
  - **microtasks**:
    MT-10
  - **required_sources**:
    SPEC; V1-QA
  - **required_validations**:
    qa-validation
- **security**:
  - **owner**: security-standard
  - **applicability**: REQUIRED
  - **reason**: Required approved migration responsibility.
  - **depends_on**:
    backend
  - **microtasks**:
    MT-13
  - **required_sources**:
    SPEC; V1-SEC
  - **required_validations**:
    security-validation
- **devops**:
  - **owner**: devops-standard
  - **applicability**: N/A
  - **reason**: No devops product surface introduced by this CLI/agent/documentation migration.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    None.
  - **required_validations**:
    None.
- **observability**:
  - **owner**: qa-testing-standard
  - **applicability**: REQUIRED
  - **reason**: Required approved migration responsibility.
  - **depends_on**:
    backend
  - **microtasks**:
    MT-11
  - **required_sources**:
    SPEC; V1-QA
  - **required_validations**:
    observability-validation
- **documentation**:
  - **owner**: dev-implementation-standard
  - **applicability**: REQUIRED
  - **reason**: Required approved migration responsibility.
  - **depends_on**:
    None.
  - **microtasks**:
    MT-09
  - **required_sources**:
    SPEC; TEMPLATES
  - **required_validations**:
    documentation-validation
- **harness**:
  - **owner**: dev-workflow-standard
  - **applicability**: REQUIRED
  - **reason**: Required approved migration responsibility.
  - **depends_on**:
    backend; documentation; qa; observability; security; architecture; environment
  - **microtasks**:
    MT-01; MT-02; MT-12
  - **required_sources**:
    SPEC; V1-ROUTING
  - **required_validations**:
    harness-validation
- **architecture**:
  - **owner**: sdd-spec-factory
  - **applicability**: REQUIRED
  - **reason**: Additional logical sector for architecture deliverables MT-03; preserves all ten canonical IDs unchanged.
  - **depends_on**:
    None.
  - **microtasks**:
    MT-03
  - **required_sources**:
    SPEC; V1-ROUTING
  - **required_validations**:
    architecture-review
- **environment**:
  - **owner**: dev-environment-standard
  - **applicability**: REQUIRED
  - **reason**: Additional logical sector for local compatibility and original REA integration; distinct from production DevOps.
  - **depends_on**:
    None.
  - **microtasks**:
    MT-07; MT-08
  - **required_sources**:
    SPEC; V1-ENV; V1-REA
  - **required_validations**:
    environment-compatibility; reverse-engineering-preservation

<!-- /contract-field: sectors -->

<!-- contract-field: pipeline -->
## pipeline

collaborative_discovery_sdd; publish_discovery_sdd_completed; human_approval; environment_capability_readiness; implementation; executor_tests; independent_functional_qa; independent_security_qa; independent_ui_ux_qa; devops_observability_validation; rework_retest; pull_request_gate; harness_final_gate; human_acceptance_merge; separately_authorized_deploy

<!-- /contract-field: pipeline -->

<!-- contract-field: gates -->
## gates

- **discovery**: User approved complete PRD on 2026-10-16 and explicitly instructed THEOFFICE-V2-001 execution; no repeated discovery approval required.
- **implementation**: Approved microtasks, executor tests and current receipts
- **independent_validation**: Every REQUIRED sector validated by its owner
- **pull_request**: Issue, JSON, specs, revision and evidence reconciled
- **harness_final**: All REQUIRED sectors current and no unresolved blocker
- **merge**: Not authorized in this Task; explicit later human acceptance required.
- **deploy**: Not authorized in this Task; separate explicit later authorization required.

<!-- /contract-field: gates -->

<!-- contract-field: required_tests -->
## required_tests

-
  - **id**: TEST-01
  - **type**: regression
  - **command**: python -m unittest discover -s tests -v
  - **expected**: exit 0; distinguish baseline failures, introduced failures and skips with evidence
-
  - **id**: TEST-02
  - **type**: diff
  - **command**: git diff --check
  - **expected**: exit 0
-
  - **id**: TEST-03
  - **type**: smoke
  - **command**: python scripts/office.py handoff docs/execution/THEOFFICE-V2-001.json --list MT-10/checklist --sector qa --revision 1
  - **expected**: exit 0 with PLANNED_NOT_EXECUTED; invalid revision must block

<!-- /contract-field: required_tests -->

<!-- contract-field: acceptance_criteria -->
## acceptance_criteria

-
  - **id**: AC-01
  - **description**: V1 source content/paths and contracts are preserved with complete section destination coverage and a selective V2 path.
  - **validation**: TEST-01
-
  - **id**: AC-02
  - **description**: Routing, library, environment and receipt/contract negative paths execute without introduced failures; unavailable native/provider validations are explicit.
  - **validation**: TEST-01, TEST-03
-
  - **id**: AC-03
  - **description**: Isolated branch contains commits, current docs, evidence and reviewable PR; no merge/deploy; local install/smoke guide provided.
  - **validation**: TEST-02 and returned publication URLs/commit SHAs

<!-- /contract-field: acceptance_criteria -->

<!-- contract-field: stop_conditions -->
## stop_conditions

architecture_change_required; scope_expansion_required; mandatory_reference_missing; source_of_truth_conflict; human_task_json_divergence; authorization_required

<!-- /contract-field: stop_conditions -->

<!-- contract-field: execution_prompt -->
## execution_prompt

- **instruction**: Keep all execution_lists in this single JSON file, never embedded in the Human Task or split into per-list JSON files. Harness verifies normative equivalence of the Human Task and this file, then supplies one prompt per list pointing to execution_contract_path and list_id. Specialists read the file, select the identified execution_lists entry and inherit global constraints, required sources, tests and dependencies. Verify task identity, contract revision, owner and current Harness evidence without reading the Human Task. Execute only the selected approved list and its subitems, return evidence and receipts, and never merge or deploy without explicit authorization.
- **required_checkpoints**:
  DISCOVERY_SDD_COMPLETED; RUNNING; VALIDATING; REWORK; BLOCKED; COMPLETED

<!-- /contract-field: execution_prompt -->

<!-- contract-field: reporting -->
## reporting

- **issue_comment_required**: True
- **publication_evidence_requirement**: returned comment URL or identifier
- **token_usage_fields**:
  input_tokens; output_tokens; total_tokens; measurement_source
- **changed_surface_fields**:
  changed_files; issue_changes; json_spec_reference_changes; remote_mutations; code_changed; branch; commit; pull_request
- **unavailable_value**: NOT_AVAILABLE
- **storage_rule**: Actual token counts, changed surface and publication evidence live in Issue comments and receipts, not in this normative contract.

<!-- /contract-field: reporting -->

<!-- contract-field: discovery -->
## discovery

- **questions_and_answers**:
  None.
- **research**:
  Inspect source repository at pinned SHA and existing contracts before extension.
- **decisions**:
  Preserve V1 distribution and add source-derived modular overlay, shared librarian and explicit helper.; Use one cohesive migration Task with internal microtasks.
- **open_hypotheses**:
  None.
- **approval_requirement**: Approved user PRD and explicit execution instruction authorize reversible construction and branch push, without additional routine approval.

<!-- /contract-field: discovery -->

## Execution list prompts

### MT-01: Preparation

Execute [JSON da Task](../execution/THEOFFICE-V2-001.json), `list_id=MT-01/checklist`, `contract_revision=1`, owner `dev-workflow-standard`. Inherit global constraints, verify current Harness equivalence/dependency receipts and read selected skills/references completely.

Checklist: see this list in normative **execution_lists** above; track completion in owner evidence.
### MT-02: Audit V1

Execute [JSON da Task](../execution/THEOFFICE-V2-001.json), `list_id=MT-02/checklist`, `contract_revision=1`, owner `dev-workflow-standard`. Inherit global constraints, verify current Harness equivalence/dependency receipts and read selected skills/references completely.

Checklist: see this list in normative **execution_lists** above; track completion in owner evidence.
### MT-03: Architecture

Execute [JSON da Task](../execution/THEOFFICE-V2-001.json), `list_id=MT-03/checklist`, `contract_revision=1`, owner `sdd-spec-factory`. Inherit global constraints, verify current Harness equivalence/dependency receipts and read selected skills/references completely.

Checklist: see this list in normative **execution_lists** above; track completion in owner evidence.
### MT-04: Contracts and routing

Execute [JSON da Task](../execution/THEOFFICE-V2-001.json), `list_id=MT-04/checklist`, `contract_revision=1`, owner `dev-implementation-standard`. Inherit global constraints, verify current Harness equivalence/dependency receipts and read selected skills/references completely.

Checklist: see this list in normative **execution_lists** above; track completion in owner evidence.
### MT-05: Functional skills

Execute [JSON da Task](../execution/THEOFFICE-V2-001.json), `list_id=MT-05/checklist`, `contract_revision=1`, owner `dev-implementation-standard`. Inherit global constraints, verify current Harness equivalence/dependency receipts and read selected skills/references completely.

Checklist: see this list in normative **execution_lists** above; track completion in owner evidence.
### MT-06: Shared librarian

Execute [JSON da Task](../execution/THEOFFICE-V2-001.json), `list_id=MT-06/checklist`, `contract_revision=1`, owner `dev-implementation-standard`. Inherit global constraints, verify current Harness equivalence/dependency receipts and read selected skills/references completely.

Checklist: see this list in normative **execution_lists** above; track completion in owner evidence.
### MT-07: Environment

Execute [JSON da Task](../execution/THEOFFICE-V2-001.json), `list_id=MT-07/checklist`, `contract_revision=1`, owner `dev-environment-standard`. Inherit global constraints, verify current Harness equivalence/dependency receipts and read selected skills/references completely.

Checklist: see this list in normative **execution_lists** above; track completion in owner evidence.
### MT-08: Reverse engineering

Execute [JSON da Task](../execution/THEOFFICE-V2-001.json), `list_id=MT-08/checklist`, `contract_revision=1`, owner `dev-environment-standard`. Inherit global constraints, verify current Harness equivalence/dependency receipts and read selected skills/references completely.

Checklist: see this list in normative **execution_lists** above; track completion in owner evidence.
### MT-09: Documentation

Execute [JSON da Task](../execution/THEOFFICE-V2-001.json), `list_id=MT-09/checklist`, `contract_revision=1`, owner `dev-implementation-standard`. Inherit global constraints, verify current Harness equivalence/dependency receipts and read selected skills/references completely.

Checklist: see this list in normative **execution_lists** above; track completion in owner evidence.
### MT-10: Regression QA

Execute [JSON da Task](../execution/THEOFFICE-V2-001.json), `list_id=MT-10/checklist`, `contract_revision=1`, owner `qa-testing-standard`. Inherit global constraints, verify current Harness equivalence/dependency receipts and read selected skills/references completely.

Checklist: see this list in normative **execution_lists** above; track completion in owner evidence.
### MT-11: Comparative benchmarks

Execute [JSON da Task](../execution/THEOFFICE-V2-001.json), `list_id=MT-11/checklist`, `contract_revision=1`, owner `qa-testing-standard`. Inherit global constraints, verify current Harness equivalence/dependency receipts and read selected skills/references completely.

Checklist: see this list in normative **execution_lists** above; track completion in owner evidence.
### MT-12: Publication

Execute [JSON da Task](../execution/THEOFFICE-V2-001.json), `list_id=MT-12/checklist`, `contract_revision=1`, owner `dev-workflow-standard`. Inherit global constraints, verify current Harness equivalence/dependency receipts and read selected skills/references completely.

Checklist: see this list in normative **execution_lists** above; track completion in owner evidence.
### MT-13: Independent security review

Execute [JSON da Task](../execution/THEOFFICE-V2-001.json), `list_id=MT-13/checklist`, `contract_revision=1`, owner `security-standard`. Inherit global constraints, verify current Harness equivalence/dependency receipts and read selected skills/references completely.

Checklist: see this list in normative **execution_lists** above; track completion in owner evidence.

## Evidence and change ledger

All checkboxes remain unverified until owner receipts are linked. Current execution evidence is maintained in Issue comments and migration reports. No checkbox, plan or source reading attests runtime PASS.

| Revision | Change | Reason | Impact | Authorization |
| --- | --- | --- | --- | --- |
| 1 | Approved PRD rendered as concrete contract; additive compatibility overlay selected | Preserve source paths and rules while enabling selective routing | V1 plugin entrypoints remain compatibility mode; root V2 path is explicit | User PRD and execution command, 2026-10-16 |

### Owner-requested Security capability, 2026-10-21

Add Cloudflare security-audit as an optional Security capability. Original scope: preserve Security tooling and enable modular skills. Owner change: explicitly select the screenshot skill. Reason: reusable source-based auditing with independent verification. Impact: one optional skill and central metadata record, no replacement of OSV, existing contracts, owners or publication gates. Responsible: Security and catalog integration. Decision: preserve pinned upstream intact and apply a bounded host adapter. Contract revision: 1 unchanged, additive capacity within approved modular-library scope. Implementation and executed test evidence: `docs/migration/security-audit-integration.md`. Host installation and real target audit effectiveness remain NOT_VALIDATED.

Owner refinement, 2026-10-21: Cloudflare is the second audit after our existing Security procedure. Preserve separate evidence, actual reviewer independence, same-revision scope comparison and final root-cause reconciliation. No existing Security capability is replaced. This updates the integration policy only; no target audit is claimed.

### Owner-requested stack CLI discovery, 2026-10-21

Original requirement: reuse mature tooling and shared catalogs. Owner request:
research CLIs for Python, React, Next.js, NestJS and Vue, catalog them and authorize
necessary automatic preparation. Decision: metadata with official sources and a
shared responsibility/install procedure; retain the existing Environment engine.
Impact: selected project-local installation can proceed using this authorization;
no install-all, stack migration or new daemon is introduced. Record concrete scopes
in existing receipts. Contract revision 1 remains unchanged; this implements the
approved library/environment scope. Evidence: `docs/migration/stack-cli-catalog.md`.

Owner addition, 2026-10-21: catalog Nx and OpenTofu as optional architecture/infrastructure capabilities. Nest CLI already exists. Preserve separate domain design, code generation, tool installation and target-specific provisioning authorization. No tool installation or infrastructure operation is performed by this catalog change.

### Consolidation requested by owner, 2026-10-21

Resolve the fragmented delivery by integrating the V1 technical-decision and TRIVIAL policies, Compose guard, independent Apple HIG skill, Tailwind/React JavaScript recipes and real Plop fallback into V2. Responsibility: Architecture, UX, implementation, DevOps, catalog and QA. Impact: additive V2 policy and capability routing, frozen V1 sources retained. Normative JSON revision 1 is unchanged; this completes existing approved requirements and later explicit owner additions. Executed evidence and precise remaining platform/acceptance limits: `docs/migration/consolidation.md`.


### Owner-requested documentation and delivery metrics, 2026-10-21

Original scope: product documentation, stage governance, measured delivery and
shared catalog. Owner request: explicit documentation responsibility for both
technical reference and usability tutorials on every Task closure; a metrics
skill to consolidate phases/total progress and reuse Portal do Cliente as the
customer reporting destination, inside the client project's docs tree.
Decision: extend Documentation core, add Governance delivery-metrics, retain the
existing Studio PRD stage plan and JSON v2 sector/schema, add an offline derived
report calculator and inspected Portal adapter. Pin the selected community
Diátaxis writing guide with unmodified original/license and documented approval/
research overrides. No production service, bulk install or separate Task system.
Impact: future normative closure obligations must be reflected in approved
Human Task/JSON before affected execution; TRIVIAL retains inline evidence.
This migration contract revision 1 is unchanged: implementation stays within its
approved documentation/metrics/catalog scope. Responsible: Documentation,
Governance and Architecture. ADR: `docs/adr/005-delivery-documentation-metrics.md`.
Evidence: `docs/migration/documentation-delivery.md`. Portal customer deployment,
auth and whole-baseline dashboard display are not claimed implemented.


### Owner-requested manuals and assisted setup, 2026-10-21

Request: fetch Portal template into client docs, then organize README topics,
product purpose/problems, development methodology, installation GUIDE AND PROMPT,
usage tutorial, technical construction/trade-offs/flowchart, and updating.
Decision: reuse the pinned owner's existing sync-template script, make fetching
and client docs navigation explicit, preserve historical README body in details
for existing compatibility anchors/tests, and add Portuguese operational manuals.
No new installer, client application, deployment or global tool installation.
Contract revision 1 unchanged; within documentation/install/migration scope.
Evidence: docs/migration/documentation-manuals.md and
`docs/receipts/evidence/portal-preparation.json`. Native host registration remains
NOT_VALIDATED; guide/prompt distinguish checkout, registration and actual readiness.

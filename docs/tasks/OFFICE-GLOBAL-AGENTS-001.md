# OFFICE-GLOBAL-AGENTS-001: Global sector agents

Contract revision: 2. NORMAL. Branch: `codex/global-sector-agents`.


<!-- contract-field: schema_version -->
## schema_version

2

<!-- /contract-field: schema_version -->

<!-- contract-field: contract_revision -->
## contract_revision

2

<!-- /contract-field: contract_revision -->

<!-- contract-field: task_id -->
## task_id

OFFICE-GLOBAL-AGENTS-001

<!-- /contract-field: task_id -->

<!-- contract-field: human_task -->
## human_task

- **representation**: github_issue
- **issue_url**: https://github.com/guilhermedemorais-dev/The-office/issues/7
- **local_mirror**: docs/tasks/OFFICE-GLOBAL-AGENTS-001.md

<!-- /contract-field: human_task -->

<!-- contract-field: summary -->
## summary

Register and route global Office sector agents reproducibly in Codex Desktop

<!-- /contract-field: summary -->

<!-- contract-field: complexity -->
## complexity

NORMAL

<!-- /contract-field: complexity -->

<!-- contract-field: goal -->
## goal

Make the existing 15 sector profiles reusable across projects and chats without pretending permanent execution.

<!-- /contract-field: goal -->

<!-- contract-field: authorization -->
## authorization

- **source**: Direct user request 2026-10-23 to apply global agents and upload plugin updates. User explicitly requested native Windows execution of the seven Ubuntu-skipped Windows cases and correction of reproduced applicable failures before PR readiness.
- **allowed**: Scoped implementation, tests, branch push and review PR.
- **excluded**: Merge, deploy, unrelated installation, permission/model/MCP changes. No live host apply in this scope.

<!-- /contract-field: authorization -->

<!-- contract-field: branch -->
## branch

codex/global-sector-agents

<!-- /contract-field: branch -->

<!-- contract-field: base -->
## base

d97ec71828a275b983262470beb67b05ac074518

<!-- /contract-field: base -->

<!-- contract-field: allowed_paths -->
## allowed_paths

scripts/register_codex_agents.py; agents/**; AGENTS.md; docs/operations/**; tests/test_codex_agent_registration.py; docs/tasks/OFFICE-GLOBAL-AGENTS-001.md; docs/execution/OFFICE-GLOBAL-AGENTS-001.json; docs/receipts/OFFICE-GLOBAL-AGENTS-001*; README.md; CHANGELOG.md; docs/architecture/agents.md

<!-- /contract-field: allowed_paths -->

<!-- contract-field: protected_paths -->
## protected_paths

plugins/**; credentials; runtime-state; models/providers/MCP/permissions settings; existing user config outside owned agent registrations; main; unrelated dirty checkouts; PR #6; docs/operations/installation.md; docs/operations/installation-prompt.md; scripts/build_skill_routes.py; library/indexes/skill-routes.json; skills/global-core/SKILL.md (PR #6 overlap)

<!-- /contract-field: protected_paths -->

<!-- contract-field: requirements -->
## requirements

AC-01: Reproducible opt-in plan/check/apply registration of all 15 office_* profiles from canonical contracts; no persistent agents or automatic invocation of all sectors.; AC-02: Default plan/check read-only; explicit apply backs up affected files and preserves unrelated TOML settings, user files and existing customizations; conflicts block safely.; AC-03: Global instructions route activated sectors to actual registered host subagents, distinguish registration from execution, and retain human release gates.; AC-04: Independent QA covers missing/invalid configuration, repeat apply, collisions/custom changes, dry run and preservation; docs accurately distinguish installed/registered/available/executed.; AC-05: Isolated reviewed commit, branch and PR published with exact validation/limitations; no merge/deploy or changed permissions/models/MCP.; AC-06: Execute the seven Windows-specific cases skipped by Ubuntu CI on native Windows with the responsible QA agent; enumerate test IDs/results and fix reproduced applicable failures under exact diagnosed paths, then independent retest before considering PR ready.

<!-- /contract-field: requirements -->

<!-- contract-field: references -->
## references

- **POLICY**:
  - **project_path**: AGENTS.md
  - **purpose**: Repository policy
- **V2**:
  - **project_path**: docs/operations/v2-execution-policy.md
  - **purpose**: Execution policy
- **INSTALL**:
  - **project_path**: docs/operations/installation.md
  - **purpose**: Existing installation flow
- **HOST**:
  - **project_path**: agents
  - **purpose**: Canonical 15 sector contracts

<!-- /contract-field: references -->

<!-- contract-field: microtasks -->
## microtasks

-
  - **id**: register
  - **owner_skill**: office_environment
  - **title**: Implement the scoped opt-in helper and canonical profile rendering.
-
  - **id**: qa
  - **owner_skill**: office_qa
  - **title**: Independently inspect the diff and execute positive/negative preservation tests.
-
  - **id**: security
  - **owner_skill**: office_security
  - **title**: Review config/file mutation boundaries and path/secret preservation.
-
  - **id**: publish
  - **owner_skill**: office_governance
  - **title**: Reconcile current contract, owner receipts, diff, test evidence and documentation.
-
  - **id**: documentation
  - **owner_skill**: office_documentation
  - **title**: Focused registration and routing documentation
-
  - **id**: windows-seven
  - **owner_skill**: office_qa
  - **title**: Native Windows seven-case validation

<!-- /contract-field: microtasks -->

<!-- contract-field: execution_lists -->
## execution_lists

-
  - **list_id**: register
  - **owner_skill**: office_environment
  - **phase**: implementation
  - **objective**: Implement the scoped opt-in helper and canonical profile rendering.
  - **microtask_ids**:
    register
  - **depends_on**:
    None.
  - **references**:
    POLICY; V2; INSTALL; HOST
  - **allowed_paths**:
    scripts/register_codex_agents.py; agents/**; AGENTS.md; docs/operations/**; tests/test_codex_agent_registration.py; docs/tasks/OFFICE-GLOBAL-AGENTS-001.md; docs/execution/OFFICE-GLOBAL-AGENTS-001.json; docs/receipts/OFFICE-GLOBAL-AGENTS-001*
  - **protected_paths**:
    plugins/**; credentials; runtime-state; models/providers/MCP/permissions settings; existing user config outside owned agent registrations; main; unrelated dirty checkouts; PR #6
  - **deliverables**:
    register owner receipt and scoped artifacts
  - **completion_condition**: Applicable acceptance criteria satisfied with actual owner evidence.
  - **required_tests**:
    focused registration tests; git diff --check
  - **acceptance_criteria**:
    AC-01: Reproducible opt-in plan/check/apply registration of all 15 office_* profiles from canonical contracts; no persistent agents or automatic invocation of all sectors.; AC-02: Default plan/check read-only; explicit apply backs up affected files and preserves unrelated TOML settings, user files and existing customizations; conflicts block safely.; AC-03: Global instructions route activated sectors to actual registered host subagents, distinguish registration from execution, and retain human release gates.; AC-04: Independent QA covers missing/invalid configuration, repeat apply, collisions/custom changes, dry run and preservation; docs accurately distinguish installed/registered/available/executed.; AC-05: Isolated reviewed commit, branch and PR published with exact validation/limitations; no merge/deploy or changed permissions/models/MCP.
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Implement the scoped opt-in helper and canonical profile rendering.
    -
      - **instruction**: Update focused installation/routing documentation and development tests.
    -
      - **instruction**: Verify backups, idempotency and preservation; do not apply to real host unless separately routed.
-
  - **list_id**: documentation
  - **owner_skill**: office_documentation
  - **phase**: implementation
  - **objective**: Document opt-in portable registration and actual sector routing; preserve distinctions between configured and executed.
  - **microtask_ids**:
    documentation
  - **depends_on**:
    register
  - **references**:
    POLICY; V2; INSTALL; HOST
  - **allowed_paths**:
    AGENTS.md; docs/operations/**; README.md; CHANGELOG.md; docs/architecture/agents.md
  - **protected_paths**:
    plugins/**; credentials; runtime-state; models/providers/MCP/permissions settings; existing user config outside owned agent registrations; main; unrelated dirty checkouts; PR #6
  - **deliverables**:
    Focused installation/routing documentation and owner receipt
  - **completion_condition**: Documentation matches implemented helper and host boundaries.
  - **required_tests**:
    Documentation inspection and git diff --check
  - **acceptance_criteria**:
    AC-01: Reproducible opt-in plan/check/apply registration of all 15 office_* profiles from canonical contracts; no persistent agents or automatic invocation of all sectors.; AC-02: Default plan/check read-only; explicit apply backs up affected files and preserves unrelated TOML settings, user files and existing customizations; conflicts block safely.; AC-03: Global instructions route activated sectors to actual registered host subagents, distinguish registration from execution, and retain human release gates.; AC-04: Independent QA covers missing/invalid configuration, repeat apply, collisions/custom changes, dry run and preservation; docs accurately distinguish installed/registered/available/executed.; AC-05: Isolated reviewed commit, branch and PR published with exact validation/limitations; no merge/deploy or changed permissions/models/MCP.
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Update portable installation/global routing instructions without machine-specific paths or changing permissions, models or MCP.
-
  - **list_id**: qa
  - **owner_skill**: office_qa
  - **phase**: validation
  - **objective**: Independently inspect the diff and execute positive/negative preservation tests.
  - **microtask_ids**:
    qa
  - **depends_on**:
    register
  - **references**:
    POLICY; V2; INSTALL; HOST
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    plugins/**; credentials; runtime-state; models/providers/MCP/permissions settings; existing user config outside owned agent registrations; main; unrelated dirty checkouts; PR #6
  - **deliverables**:
    qa owner receipt and scoped artifacts
  - **completion_condition**: Applicable acceptance criteria satisfied with actual owner evidence.
  - **required_tests**:
    focused registration tests; git diff --check
  - **acceptance_criteria**:
    AC-01: Reproducible opt-in plan/check/apply registration of all 15 office_* profiles from canonical contracts; no persistent agents or automatic invocation of all sectors.; AC-02: Default plan/check read-only; explicit apply backs up affected files and preserves unrelated TOML settings, user files and existing customizations; conflicts block safely.; AC-03: Global instructions route activated sectors to actual registered host subagents, distinguish registration from execution, and retain human release gates.; AC-04: Independent QA covers missing/invalid configuration, repeat apply, collisions/custom changes, dry run and preservation; docs accurately distinguish installed/registered/available/executed.; AC-05: Isolated reviewed commit, branch and PR published with exact validation/limitations; no merge/deploy or changed permissions/models/MCP.
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Independently inspect the diff and execute positive/negative preservation tests.
    -
      - **instruction**: Report exact failures and retests; do not self-certify Environment or Security.
-
  - **list_id**: security
  - **owner_skill**: office_security
  - **phase**: validation
  - **objective**: Review config/file mutation boundaries and path/secret preservation.
  - **microtask_ids**:
    security
  - **depends_on**:
    register
  - **references**:
    POLICY; V2; INSTALL; HOST
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    plugins/**; credentials; runtime-state; models/providers/MCP/permissions settings; existing user config outside owned agent registrations; main; unrelated dirty checkouts; PR #6
  - **deliverables**:
    security owner receipt and scoped artifacts
  - **completion_condition**: Applicable acceptance criteria satisfied with actual owner evidence.
  - **required_tests**:
    focused registration tests; git diff --check
  - **acceptance_criteria**:
    AC-01: Reproducible opt-in plan/check/apply registration of all 15 office_* profiles from canonical contracts; no persistent agents or automatic invocation of all sectors.; AC-02: Default plan/check read-only; explicit apply backs up affected files and preserves unrelated TOML settings, user files and existing customizations; conflicts block safely.; AC-03: Global instructions route activated sectors to actual registered host subagents, distinguish registration from execution, and retain human release gates.; AC-04: Independent QA covers missing/invalid configuration, repeat apply, collisions/custom changes, dry run and preservation; docs accurately distinguish installed/registered/available/executed.; AC-05: Isolated reviewed commit, branch and PR published with exact validation/limitations; no merge/deploy or changed permissions/models/MCP.
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Review config/file mutation boundaries and path/secret preservation.
    -
      - **instruction**: Run bounded relevant negative tests; record residual risks.
-
  - **list_id**: publish
  - **owner_skill**: office_governance
  - **phase**: publication
  - **objective**: Reconcile current contract, owner receipts, diff, test evidence and documentation.
  - **microtask_ids**:
    publish
  - **depends_on**:
    qa; security
  - **references**:
    POLICY; V2; INSTALL; HOST
  - **allowed_paths**:
    Same approved allowed_paths as the global allowed_paths section above (all entries inherited).
  - **protected_paths**:
    plugins/**; credentials; runtime-state; models/providers/MCP/permissions settings; existing user config outside owned agent registrations; main; unrelated dirty checkouts; PR #6
  - **deliverables**:
    publish owner receipt and scoped artifacts
  - **completion_condition**: Applicable acceptance criteria satisfied with actual owner evidence.
  - **required_tests**:
    focused registration tests; git diff --check
  - **acceptance_criteria**:
    AC-01: Reproducible opt-in plan/check/apply registration of all 15 office_* profiles from canonical contracts; no persistent agents or automatic invocation of all sectors.; AC-02: Default plan/check read-only; explicit apply backs up affected files and preserves unrelated TOML settings, user files and existing customizations; conflicts block safely.; AC-03: Global instructions route activated sectors to actual registered host subagents, distinguish registration from execution, and retain human release gates.; AC-04: Independent QA covers missing/invalid configuration, repeat apply, collisions/custom changes, dry run and preservation; docs accurately distinguish installed/registered/available/executed.; AC-05: Isolated reviewed commit, branch and PR published with exact validation/limitations; no merge/deploy or changed permissions/models/MCP.
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Reconcile current contract, owner receipts, diff, test evidence and documentation.
    -
      - **instruction**: Commit scoped files, push isolated branch and create review PR; never merge/deploy.
-
  - **list_id**: windows-seven
  - **owner_skill**: office_qa
  - **phase**: validation
  - **objective**: Enumerate and execute the seven Windows-specific cases skipped on Ubuntu, natively on Windows.
  - **microtask_ids**:
    windows-seven
  - **depends_on**:
    None.
  - **references**:
    POLICY; V2; INSTALL; HOST
  - **allowed_paths**:
    docs/receipts/OFFICE-GLOBAL-AGENTS-001-windows*
  - **protected_paths**:
    Same protected_paths as the global protected_paths section above (all entries inherited).
  - **deliverables**:
    Seven exact test IDs, native runtime, commands/outcomes and reproduction evidence; exact affected files if failures.
  - **completion_condition**: Seven cases executed without skips, or exact reproducible blocker recorded; no readiness claim while an applicable failure remains.
  - **required_tests**:
    Seven Windows-specific skipped tests on native Windows, synthetic temporary destinations only.
  - **acceptance_criteria**:
    AC-06
  - **stop_conditions**:
    All global stop_conditions above apply unchanged.
  - **checklist**:
    -
      - **instruction**: Recover the seven actual Windows-only skipped test IDs from existing CI/tests, preserving the eighth unrelated skip.
    -
      - **instruction**: Execute natively on Windows, using temporary paths and no real host config or infrastructure mutation.
    -
      - **instruction**: Report results/diagnosis and exact fix candidates; do not edit implementation or bypass invariants.

<!-- /contract-field: execution_lists -->

<!-- contract-field: sectors -->
## sectors

- **database**:
  - **owner**: office_governance
  - **applicability**: N/A
  - **reason**: No application database/UI/infrastructure/telemetry change.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    None.
  - **required_validations**:
    None.
- **backend**:
  - **owner**: office_environment
  - **applicability**: REQUIRED
  - **reason**: Scoped host registration CLI, safety, documentation or governance.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    POLICY; V2; INSTALL; HOST
  - **required_validations**:
    backend review
- **frontend**:
  - **owner**: office_governance
  - **applicability**: N/A
  - **reason**: No application database/UI/infrastructure/telemetry change.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    None.
  - **required_validations**:
    None.
- **ui_ux**:
  - **owner**: office_governance
  - **applicability**: N/A
  - **reason**: No application database/UI/infrastructure/telemetry change.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    None.
  - **required_validations**:
    None.
- **qa**:
  - **owner**: office_qa
  - **applicability**: REQUIRED
  - **reason**: Scoped host registration CLI, safety, documentation or governance.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    POLICY; V2; INSTALL; HOST
  - **required_validations**:
    qa review
- **security**:
  - **owner**: office_security
  - **applicability**: REQUIRED
  - **reason**: Scoped host registration CLI, safety, documentation or governance.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    POLICY; V2; INSTALL; HOST
  - **required_validations**:
    security review
- **devops**:
  - **owner**: office_governance
  - **applicability**: N/A
  - **reason**: No application database/UI/infrastructure/telemetry change.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    None.
  - **required_validations**:
    None.
- **observability**:
  - **owner**: office_governance
  - **applicability**: N/A
  - **reason**: No application database/UI/infrastructure/telemetry change.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    None.
  - **required_validations**:
    None.
- **documentation**:
  - **owner**: office_documentation
  - **applicability**: REQUIRED
  - **reason**: Scoped host registration CLI, safety, documentation or governance.
  - **depends_on**:
    None.
  - **microtasks**:
    None.
  - **required_sources**:
    POLICY; V2; INSTALL; HOST
  - **required_validations**:
    documentation review
- **harness**:
  - **owner**: office_governance
  - **applicability**: REQUIRED
  - **reason**: Scoped host registration CLI, safety, documentation or governance.
  - **depends_on**:
    backend; qa; security; documentation
  - **microtasks**:
    None.
  - **required_sources**:
    POLICY; V2; INSTALL; HOST
  - **required_validations**:
    harness review

<!-- /contract-field: sectors -->

<!-- contract-field: acceptance_criteria -->
## acceptance_criteria

AC-01: Reproducible opt-in plan/check/apply registration of all 15 office_* profiles from canonical contracts; no persistent agents or automatic invocation of all sectors.; AC-02: Default plan/check read-only; explicit apply backs up affected files and preserves unrelated TOML settings, user files and existing customizations; conflicts block safely.; AC-03: Global instructions route activated sectors to actual registered host subagents, distinguish registration from execution, and retain human release gates.; AC-04: Independent QA covers missing/invalid configuration, repeat apply, collisions/custom changes, dry run and preservation; docs accurately distinguish installed/registered/available/executed.; AC-05: Isolated reviewed commit, branch and PR published with exact validation/limitations; no merge/deploy or changed permissions/models/MCP.; AC-06: Execute the seven Windows-specific cases skipped by Ubuntu CI on native Windows with the responsible QA agent; enumerate test IDs/results and fix reproduced applicable failures under exact diagnosed paths, then independent retest before considering PR ready.

<!-- /contract-field: acceptance_criteria -->

<!-- contract-field: stop_conditions -->
## stop_conditions

scope_expansion_required; source_of_truth_conflict; mandatory_reference_missing; human_task_json_divergence; unsafe_config_preservation

<!-- /contract-field: stop_conditions -->

<!-- contract-field: required_tests -->
## required_tests

Focused unit tests for registration/preservation and explicit conflict handling.; Independent QA and Security scoped checks.; Existing generated-skills check, applicable regression and git diff --check; distinguish preexisting failures.; Execute seven Ubuntu-skipped Windows-specific cases natively on Windows; diagnose and independently retest authorized applicable corrections.

<!-- /contract-field: required_tests -->

<!-- contract-field: gates -->
## gates

- **publication**: Current implementation, independent QA/Security and focused documentation evidence reconciled.
- **merge**: NOT_AUTHORIZED
- **deploy**: NOT_AUTHORIZED

<!-- /contract-field: gates -->

<!-- contract-field: current_state -->
## current_state

Host has 15 registered profiles and global routing instructions per parent evidence; source distribution needs reproducible portable registration. Do not embed personal paths. Registration is not execution.

<!-- /contract-field: current_state -->

<!-- contract-field: revision2_addendum -->
## revision2_addendum

- **goal**: Close the seven native Windows validation obligations inside the same Task and PR #8.
- **observed_head**: ee0eb40b1364e4475267040411ff90512efca5e0
- **native_windows**: Required; Linux CI skips do not satisfy these seven cases.
- **first_step**: Independent office_qa enumerates and executes only the seven Windows-specific skipped tests using temporary targets; record test IDs and actual outcomes.
- **fix_scope**: Pending diagnosis; only reproduced applicable defects. No code/test/protected-path permission is granted before exact file paths and source-preservation impacts are reconciled.
- **source_freeze**: If a defect concerns frozen V1 sources or PR #6 protected files, record the conflict and alternatives before changing scope. Do not copy four preexisting dirty patches.
- **validation**: Applicable responsible executor fixes, independent QA retest, Security only for triggered affected behavior; publish to existing PR #8 and observe final-head CI.
- **human_gates**: No live host apply, merge, deploy or closing PR. Existing synthetic/OS limitations remain.

<!-- /contract-field: revision2_addendum -->

## Execution prompts

- [ ] Execute [single Task JSON](../execution/OFFICE-GLOBAL-AGENTS-001.json), `list_id=register`, revision 2, owner `office_environment`. Inherit every scope constraint and source.
- [ ] Execute [single Task JSON](../execution/OFFICE-GLOBAL-AGENTS-001.json), `list_id=documentation`, revision 2, owner `office_documentation`. Inherit every scope constraint and source.
- [ ] Execute [single Task JSON](../execution/OFFICE-GLOBAL-AGENTS-001.json), `list_id=qa`, revision 2, owner `office_qa`. Inherit every scope constraint and source.
- [ ] Execute [single Task JSON](../execution/OFFICE-GLOBAL-AGENTS-001.json), `list_id=security`, revision 2, owner `office_security`. Inherit every scope constraint and source.
- [ ] Execute [single Task JSON](../execution/OFFICE-GLOBAL-AGENTS-001.json), `list_id=publish`, revision 2, owner `office_governance`. Inherit every scope constraint and source.
- [ ] Execute [single Task JSON](../execution/OFFICE-GLOBAL-AGENTS-001.json), `list_id=windows-seven`, revision 2, owner `office_qa`. Inherit every scope constraint and source.

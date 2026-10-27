---
name: qa-validation
description: "Use for qa validation: Modes and phases; Shared tools, not duplicated ownership; Evidence gate. Load required core skills first."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: qa-validation

Source: `plugins/qa-testing-standard/skills/qa-testing-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, qa-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/qa-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/qa-testing-standard/skills/qa-testing-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/qa-testing-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

## Reconstruction and specification coverage

For reconstructed behavior or evidence-to-spec coverage, read the repository-root [reconstruction procedure](library/reconstruction/README.md). Compare the canonical acceptance/test IDs with actual current-revision evidence, including negative cases. Implementation declarations and visual similarity do not prove functional equivalence. Missing mandatory criteria, unapproved skips, stale evidence and incomplete tests block coverage regardless of any average. Use the optional coverage checker only as a structural/integrity check; it cannot run tests, certify independent QA or authorize release. Preserve existing QA, UX, Security and human gates.

Canonical link resolution (repository-relative paths, not skill-directory-relative):
- `library/reconstruction/README.md`: `library/reconstruction/README.md`

<!-- source-section:qa-testing-standard:002 sha256:c434a93c78010baa269eb2ab4933c94cd733105922af2dc8dffa72113d4d059d -->
## Modes and phases

Use the smallest sufficient mode:

| Mode | Scope |
| --- | --- |
| `change-validation` | Current task/diff/PR behavior and affected regression |
| `scoped-qa` | Named feature, page, module or API |
| `repository-regression-audit` | Broader repository evaluation only when requested |
| `bug-reproduction` | Reproduce a reported problem and classify evidence |
| `fix-verification` | Retest a specified fix and affected regression |

In **planning**, produce strategy/scenarios before implementation when their own
prerequisites exist. Final `depends_on` dependencies do not forbid planning.
In **validation**, verify all material dependencies and the executable revision.
Frontend complete while required backend is PENDING cannot yield QA final PASS.
Planning completion is not validation PASS; keep validation NOT_VALIDATED until
executed. Report phase and scope so a planning receipt cannot close final QA.

Behavior changes, bugfixes, user flows, API behavior, business rules, persistence,
payments, tenants, integrations, imports/exports, concurrency, state machines and
reported regressions trigger QA. Docs/metadata/comments with no runtime impact
can be N/A with a reason agreed by the Harness. Pure visual changes still belong
to UI validation even when functional QA is N/A.

<!-- source-section:qa-testing-standard:004 sha256:89f1e26b681e66139df033e7fca638514340818ac77299ab5cf5636e6459202b -->
## Shared tools, not duplicated ownership

Prefer project-native commands and the project's existing test configuration.
For external capabilities, resolve the original owner and follow the Harness
`skill-owned-tools.md` protocol through the existing helper:

- `dev-implementation-standard`: pytest, pytest-cov, Hypothesis, Python unittest.
- `ui-ux-standard`: Playwright browser runtime capability.

QA can execute an approved shared capability and interpret functional results;
that does not transfer its technical registry/install/state ownership. Read the
owner's registry/protocol when using it. If an owner or required tool is missing,
ask the Harness/Environment for preparation or an approved equivalent. Do not
duplicate a registry, installer or cache; do not silently install anything.
No new QA-exclusive tool or knowledge registry is needed for this bundle.

Use synthetic data and isolated environments. Review network, billing, email,
payment, mutation and cleanup effects before running tests. Obtain explicit
authorization for effects outside the approved scope; do not run production or
destructive fuzz/concurrency workloads as a routine validation shortcut.

<!-- source-section:qa-testing-standard:005 sha256:bed5b30b4a71eb5c532190880d140ceebc752a83fbefeb3b18c8b2eb131893df -->
## Evidence gate

For implementation changes or cleanup, resolve the active `dev-workflow-standard`
owner's `references/minimal-code-gate.md` from its installed bundle or explicit
canonical checkout, never an assumed sibling cache. Independently check its
additive evidence against connected callers, exports/configuration, applicable
dynamic references and executed behavior checks. Confirm full approved scope,
safe deletions, preserved safeguards and recorded intentional limits; lack of
text-search hits alone cannot prove code unused. Report concrete cases and
uncertainty in the existing receipt, with justified N/A for inapplicable checks.
Missing material evidence requires REWORK or BLOCKED, not final PASS. Route
product fixes to Implementation and security/accessibility findings to their
required owners; this check does not substitute for their approval.

For UI workflows, use the contract's component IDs/revisions and the project
Design Guide/catalogue as scoped behavior sources. Plan applicable widget
transitions, validation, retries, permissions and error paths against their
specified outcomes. Deterministic catalogue fixtures allow isolated checks,
not a claim that real APIs, persistence or end-to-end flows work. Identify mock
versus real boundaries and execute required integration checks separately.
Report fixture-only coverage as such; missing backend evidence cannot yield
final QA PASS. UI/UX separately validates catalogue and final rendered product
fidelity, spacing, responsive states, keyboard/focus and accessibility. Check
that evidence matches current component/source revisions; stale screenshots or
static HTML parsing do not close required browser gates.

Return `QA_STATUS` in the existing `EXECUTION_RECEIPT`, with sector, phase/mode,
revision, sources_loaded (path and purpose), conditional_sources_loaded,
validation_scope, commands/exit codes, scenarios executed, bug disposition,
artifacts, limitations and next_safe_action. Preserve its invocation_evidence,
inputs_used, outputs_produced, state and validation_evidence fields. Do not
invent another global receipt or put logs/status into the Execution Contract.

| QA_STATUS | Meaning |
| --- | --- |
| PASS | Required scope executed, mandatory cases passed, blocking bugs resolved, required regression verified, limitations recorded |
| PARTIAL | Useful checks ran but coverage is incomplete; cannot close required QA |
| BLOCKED | A mandatory dependency, tool, source or unresolved blocking bug prevents the gate |
| NOT_VALIDATED | No applicable validation was executed, including planning-only work |

No execution means no PASS. A tool version, build success, screenshot or unit
suite alone cannot prove a required user flow. PASS is bounded to executed
scope, never a claim that software has no bugs. A red test must be classified
before asserting a product defect. Unresolved mandatory checks cannot be waived
by relabeling the result PARTIAL or by accepting a bug informally.

Map evidence-backed QA PASS to the existing COMPLETED state only for your
completed validation checkpoint. The Harness reconciles all REQUIRED sectors
and final acceptance. Human approval, PR, merge and release remain separate.

<!-- end of selected V2 skill -->

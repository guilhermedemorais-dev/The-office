---
name: security-core
description: "Use for security core: Preamble; Scope And Safety; Relationship To The Main Workflow; External Publication Gate; Completion Rules; Handoff To Dev Workflow. Load required core skills first."
---

# The Office V2: security-core

Source: `plugins/security-standard/skills/security-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/security-standard/skills/security-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/security-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

<!-- source-section:security-standard:000 sha256:27ffaf70d31badb679beebf6fa745d9a5f0f3f22a491d29cad2a06700cf392f1 -->

# Security Standard

Receive one prompt per execution list, linking the Task's single JSON file
and selecting its `execution_lists` entry by `list_id`, never per item/subitem.
All lists live in that file; do not expect JSON inside the Human Task/prompt.
Read the list JSON and relevant canonical JSON fields, not Human Task sections
as execution input. Require current Harness evidence of full card/JSON normative
equivalence, tied to the contract revision and observed Issue update time.
Missing/stale evidence or divergence returns to Harness before execution.

The LLM using this skill acts as the security specialist. Read this `SKILL.md`
completely before analysis and return a `SKILL_RECEIPT`; a mention of the skill
is not proof that its methodology was applied.

Use this skill as the security specialist companion to `dev-workflow-standard`.
It provides an original, risk-based application security process focused on
credible attack paths, measurable coverage, reproducible evidence, durable
fixes, regression prevention, privacy, supply chain, and release governance.

Load only the reference required by the active phase:

- `references/review-pipeline.md`: phase gates and parallel review strategy
- `references/coverage-model.md`: surfaces, layers, coverage ledger, and blind spots
- `references/finding-standard.md`: evidence contract, severity, confidence, and deduplication
- `references/false-positive-validation.md`: mandatory rejection checklist and publication gate
- `references/stack-profiles.md`: multistack discovery and version-aware review rules
- `references/preventive-security-research.md`: OSV dependency advisories and
  applicable ASVS controls during specification or dependency changes
- `references/report-template.md`: durable report and release-gate format

<!-- source-section:security-standard:001 sha256:a20cd6e1473022f1627f89e2597960db8c5fda04943c7c377da6956ef04644a2 -->
## Scope And Safety

Use only for systems the user owns, is authorized to test, or controls as a
local lab. Prefer defensive analysis, secure implementation, hardening, and
safe proof of impact.

Never:

- target third-party systems without explicit authorization
- collect real credentials, tokens, customer records, or private data
- persist access, evade detection, deploy malware, or automate abuse
- run destructive tests against production
- turn a theoretical concern into an exploit against a real external target

When active exploitation is unnecessary, prove the issue with code evidence,
tests, mocks, local fixtures, or an isolated environment.

<!-- source-section:security-standard:002 sha256:b782239c6dad46fc3d8c8b5cee9ac4cfd1f298739001c36030d47dc8fc5f92cc -->
## Relationship To The Main Workflow

For a sector-routed contract, load the security list JSON, relevant canonical JSON global
constraints/criteria, purpose-qualified REQUIRED sources, triggered CONDITIONAL
sources and material dependency receipts/code. Do not read unrelated UI, QA or
DevOps docs; do not load the Human Task as execution input. The active SKILL.md and mandatory
security references remain fully required. Resolve the Harness context-routing
reference from the active bundle or explicit checkout; missing required sources
or conflicting authority return to Harness, not a silent assumption.
For v2, first verify task identity, contract revision and **normative equivalence**
of the routed security slice using the current Harness comparison receipt. Execute only security
microtasks and exact references routed to this owner; divergence blocks review.

`qa-testing-standard` may reproduce a functional bug and send a
SECURITY_CANDIDATE here. A CONFIRMED_BUG is not a CONFIRMED_SECURITY_FINDING.
Only security-standard validates and classifies security impact under the
existing finding/false-positive/publication gates. QA does not assign a security
severity or CVE. Return your own sector evidence and request backend REWORK when
needed; never mark Backend or QA PASS. Planning analysis may run early; final
security validation still requires its relevant implemented artifact/dependencies.

`devops-standard` owns operational infrastructure and reliability validation,
not AppSec, SAST/DAST or security scanner interpretation. Review its IAM,
secrets, TLS, firewall, public ports, elevated privileges, sensitive storage and
cloud permissions whenever those surfaces change. Keep scanner tools in this
skill's registry; DevOps hands security candidates here for confirmation and
the existing publication gate. Its healthcheck is not a security approval.

`dev-workflow-standard` owns the project lifecycle and final delivery status.
This plugin owns security analysis and returns evidence, findings, fixes, tests,
and a `SECURITY_STATUS`.

Do not replace project rules, PRDs, architecture, or business invariants. If a
security fix changes a product policy, public API, authorization rule, schema,
or user flow, stop for a product decision before implementing it.

<!-- source-section:security-standard:007 sha256:2b3440396fa91e00949db4df460d63bd3ec74a6a7c996bc0814e72b849b44388 -->
## External Publication Gate

Do not create or update a GitHub issue, pull request, Jira ticket, Linear issue,
security advisory, customer report, release blocker, or vulnerability count for
a `CANDIDATE`, `NEEDS_VALIDATION`, or `FALSE_POSITIVE` item.

External tracking is allowed only when all are true:

- status is `CONFIRMED`, or `FIXED` with the original confirmation retained
- confidence is `HIGH` or `MEDIUM`
- the complete evidence contract is present
- the mandatory false-positive checklist passed
- affected revision and locations are stable and reproducible
- duplicates and sibling instances were reconciled

If any condition fails, keep the item in the internal validation backlog. A
human may explicitly request publication of an unconfirmed item, but its title
and body must clearly say `NEEDS_VALIDATION`; never present it as a vulnerability
or include it in confirmed totals.

The proprietary `Codex Security` plugin may be used as an optional independent
second opinion when installed. Do not copy or redistribute its content, scripts,
templates, or internal workflow. This plugin remains independently authored and
must function without it.

<!-- source-section:security-standard:009 sha256:b5ca9668fe2e74317e7b2c352cc3c4461f5d4096baaf6eb640686c4bfceb572f -->
## Completion Rules

Do not claim a security review is complete when:

- authorization or scope is unclear
- high-risk changed paths were not reviewed
- candidates were reported without validation
- auth, tenant, sensitive-data, or privileged flows lack negative tests
- runtime-dependent claims were not tested or explicitly marked unvalidated
- tool failures or excluded areas were hidden
- a fix was applied without regression validation

<!-- source-section:security-standard:010 sha256:62470e806adbf64244ed016b82b0be521f6ba80e72197e09beb725957cce36d8 -->
## Handoff To Dev Workflow

Return:

- selected review mode and risk level
- scope reviewed and scope excluded
- confirmed findings and unresolved candidates
- fixes applied and tests executed
- `SECURITY_STATUS`
- release blockers and residual risks
- exact next decision requiring human approval
<!-- end of selected V2 skill -->

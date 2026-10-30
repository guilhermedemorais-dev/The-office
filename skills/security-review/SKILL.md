---
name: security-review
description: "Review application security, threat models, trust boundaries, and code changes for credible vulnerabilities. Use for explicit security audits, authentication/authorization risks, secrets, injections, and security-sensitive integrations; not for ordinary functional QA or DevOps healthchecks."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: security-review

Source: `plugins/security-standard/skills/security-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, security-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/security-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/security-standard/skills/security-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/security-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

<!-- source-section:security-standard:003 sha256:713eb7112caed8832f9f5da791d020d1166c364d4b06a123c9a9ced79cbfec8b -->
## Review Modes

Choose the smallest mode that provides credible coverage.

### Change Review

Use for a working-tree diff, commit, branch, or pull request.

Focus on:

- newly introduced or weakened trust boundaries
- authentication and authorization changes
- input parsing, validation, encoding, and dangerous sinks
- secret handling, logging, error disclosure, and data exposure
- database queries, file paths, uploads, redirects, templates, and command execution
- dependency, infrastructure, CI/CD, and configuration changes
- sibling call sites affected by a modified shared helper

Do not expand into an unrelated repository audit.

### Scoped Audit

Use for a module, route group, service, package, integration, or other explicit
boundary. Include directly supporting code only when needed to prove data flow,
authorization, reachability, or impact.

### Repository Audit

Use when broad assurance is required. Start with architecture and attack
surface mapping, then prioritize internet-facing, privileged, multi-tenant,
secret-bearing, payment, upload, parser, admin, and data-export surfaces.

Repository coverage must be explicit. Record what was reviewed, excluded,
deferred, and why. Never imply exhaustive coverage from a sample of files.

Use the coverage model in `references/coverage-model.md`. For large scopes,
partition work by independent attack surface, not arbitrary file count. Keep
one owner per surface and reconcile shared controls centrally.

### Finding Validation And Fix

Use when a candidate issue already exists. Confirm that the vulnerable path is
reachable, identify the violated invariant, implement the smallest safe fix,
and add a regression test that fails before the fix and passes after it when
practical.

<!-- source-section:security-standard:004 sha256:d9d3c286d4c34fd8e99cbf3055ecc530548ac4a6bfca6acf95aed08b4efb0b0f -->
## Risk-Adaptive Depth

Classify the task before analysis:

- `LOW`: docs, styling, isolated non-sensitive logic, or tests with no runtime trust impact
- `MEDIUM`: ordinary API/UI behavior, data writes, dependencies, or internal integrations
- `HIGH`: auth, authorization, tenants, secrets, payments, uploads, admin, infrastructure, parsers, webhooks, or sensitive data
- `CRITICAL`: production identity boundary, cryptography, privileged execution, public deserialization, or a known active vulnerability

Minimum depth:

- `LOW`: focused diff review and secret/config check
- `MEDIUM`: focused review plus relevant automated tests
- `HIGH`: threat model update, end-to-end data-flow review, negative tests, and runtime validation where safe
- `CRITICAL`: independent validation, rollback plan, explicit human gate, and no production change without approval

<!-- source-section:security-standard:005 sha256:481e61e362c7fd0e3b21033bfd2def795b8378567809d87c37c9c13e8b105579 -->
## Security Workflow

Follow the gated pipeline in `references/review-pipeline.md`. A phase may not
claim completion until its required evidence exists. Preserve intermediate
evidence so an interrupted audit can resume without repeating or overstating
coverage.

### 1. Establish Authority And Source Of Truth

Identify:

- authorized target and exact scope
- project rules and security documentation
- architecture and deployment model
- sensitive assets and regulated data
- environments allowed for testing
- acceptance criteria and prohibited actions

### 2. Build A Compact Threat Model

Document only what is useful for the current scope:

- assets worth protecting
- actors and privilege levels
- entry points and attacker-controlled inputs
- trust boundaries and tenant boundaries
- sensitive sources and dangerous sinks
- existing controls and assumptions
- abuse cases with plausible impact

Threat models must reflect the actual repository and runtime. Generic OWASP
lists are prompts for investigation, not evidence of vulnerabilities.

### 3. Trace Security-Relevant Flows

During Discovery/SDD, translate applicable advisory research and threat-model
controls into testable prevention requirements using
`references/preventive-security-research.md`. Reuse the module Task, security
sector and reference library. Planning is not a finding or a validation PASS.

Follow data and authority from entry point to effect:

```text
input/source -> parsing -> validation -> authorization -> transformation -> sink/effect
```

Check both happy paths and negative paths. Inspect shared helpers and alternate
entry points when a control is centralized.

### 4. Discover Candidates

Evaluate, as applicable:

- broken access control, IDOR, tenant isolation, privilege escalation
- authentication, sessions, recovery, MFA, token lifecycle, CSRF
- injection into SQL, NoSQL, shell, templates, expressions, headers, or logs
- XSS, unsafe HTML, redirects, CORS, CSP, and browser trust boundaries
- SSRF, webhooks, outbound requests, DNS/IP validation, and callback handling
- file upload, archive extraction, path traversal, MIME and content handling
- unsafe deserialization, parsing limits, recursion, memory and CPU exhaustion
- cryptography, randomness, key handling, signature verification, and replay
- secrets in code, configuration, logs, build output, browser bundles, or history
- dependency and supply-chain risks, install scripts, CI permissions, and artifact provenance
- insecure defaults, debug modes, exposed services, containers, cloud/IAM, and network controls
- privacy, excessive data collection, retention, exports, backups, and observability

### 5. Validate Before Reporting

A reportable finding needs:

- precise affected location
- attacker-controlled source or violated privilege boundary
- missing, bypassed, or insufficient control
- reachable security-sensitive sink or effect
- realistic preconditions
- concrete confidentiality, integrity, availability, or privacy impact
- evidence that relevant mitigations do not already block the path

Classify uncertain candidates as `NEEDS_VALIDATION`, not as confirmed.
Ordinary correctness bugs are not security findings without security impact.

Before assigning `CONFIRMED`, load and apply
`references/false-positive-validation.md`. Validation must trace imported guards,
middleware, framework defaults, deployment controls, and other upstream or
downstream mitigations instead of judging one suspicious line in isolation.

Use `references/stack-profiles.md` to detect the repository's actual languages,
frameworks, package managers, lockfiles, runtime versions, infrastructure, and
deployment conventions. Load only the profiles that match detected evidence.
Never assume a Next.js, Node.js, PHP, WordPress, Laravel, Vue, container, or
cloud convention without proving that it applies to the target revision.

Apply the complete evidence and deduplication rules in
`references/finding-standard.md`. Independent vulnerable entry points remain
separate findings even when they share a root cause; remediation may group them.

### 6. Rate Severity

Use impact and exploitability together:

- `CRITICAL`: broad compromise with realistic low-friction exploitation
- `HIGH`: account/tenant compromise, significant sensitive-data exposure, privileged action, or credible code execution
- `MEDIUM`: meaningful but constrained security impact requiring notable conditions
- `LOW`: limited impact or defense-in-depth weakness with a plausible path
- `INFO`: hardening or hygiene recommendation without demonstrated vulnerability

State confidence separately as `HIGH`, `MEDIUM`, or `LOW`. Tool-generated
severity never overrides repository evidence.

### 7. Remediate At The Correct Boundary

Prefer fixes that enforce the security invariant centrally and preserve public
contracts when possible. Avoid scattered symptom patches.

For each fix:

- explain the violated invariant
- identify why the current control failed
- implement the smallest complete correction
- add negative and regression tests
- verify expected legitimate behavior still works
- assess migration, compatibility, observability, and rollback needs
- search for affected sibling instances

### 8. Validate The Result

Use the repository's canonical commands and environment. Depending on risk,
run unit, integration, API, browser/e2e, dependency, SAST, secret, container,
or infrastructure checks.

For runtime testing:

- use local, test, or staging environments
- use synthetic accounts and sanitized fixtures
- avoid destructive payloads and uncontrolled load
- capture reproducible evidence without storing secrets

<!-- end of selected V2 skill -->

---
name: orchestrator-delegation
description: "Use for orchestrator delegation: Delegation Rules; When to Trigger Each Specialist; Reference Routing. Load required core skills first."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: orchestrator-delegation

Source: `plugins/dev-workflow-standard/skills/dev-workflow-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, orchestrator-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/orchestrator-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/dev-workflow-standard/skills/dev-workflow-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/dev-workflow-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

## Optional project memory

When persistent project memory is selected for the task, read the repository-root [memory integration](integrations/memory/README.md). Retrieve only the authorized project/module slice; verify recalled decisions and evidence against current versioned sources before routing them. Memory is supporting context, never an approval, credential store, canonical Task or proof that a sector executed. If unavailable, continue from current project sources and record the limitation. Do not preload all memories or create one memory service per sector.

Canonical link resolution (repository-relative paths, not skill-directory-relative):
- `../../../sdd-spec-factory/skills/sdd-spec-factory/references/api-research-library.md`: `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/api-research-library.md`
- `integrations/memory/README.md`: `integrations/memory/README.md`

<!-- source-section:dev-workflow-standard:016 sha256:f6c95fd2b227bfe232b93e75de7a8e5edb0a93497373bc0fab4fda8f09c8f01b -->
## Delegation Rules

Before capability selection in any phase, apply the whole-inventory consultation
in `references/capability-registry.md`: consider all active MCP/catalog and
specialist tool-registry metadata, actual host capabilities, and relevant
context/provider routes. Reuse valid Environment discovery evidence; select
and invoke only capabilities relevant to the task. Record coverage gaps and
material fallback reasons in existing routing evidence.

Before every delegation, load `references/harness-execution.md`,
`references/capability-registry.md`, `references/skill-execution-contract.md`
and `references/minimal-code-gate.md`. Naming a skill is not activation, and
assigning a task is not execution. The
orchestrator agent must resolve the canonical `SKILL.md`, require the receiving
LLM to read it completely, and require a `SKILL_RECEIPT` before work begins.

- **Specs and execution artifacts** -> delegate to `sdd-spec-factory` for NORMAL work that needs new
  behavior specification and for all COMPLEX work. Provide: demand summary,
  source-of-truth paths, consolidated scope, constraints, and the layers in play
  (Banco, API/Backend, Frontend/UI). Require the spec hierarchy, human task, and
  valid Execution Contract before approving implementation.
- **Implementation** -> delegate to `dev-implementation-standard` only after the
  task, Execution Contract, and mandatory specs are approved. Prefer a bounded
  list prompt linking the single Task JSON file, containing `task_id`, `list_id`,
  `execution_contract_path`, sector, phase, current
  branch/revision, and only the relevant prior receipt/handoff. The executor
  reconstructs required context from repository paths. Require
  `REUSE_INVENTORY` and the minimal-code gate before code is written.
- **Transport of delegation** (visible terminal / executor LLM handoff, prompt
  contract, network fallback) is described in `references/claude-delegation.md`.
  Keep prompts lean: paths and constraints, not whole files or conversations.
- Two executors must not edit the same files simultaneously.
- Every invoked capability must return `EXECUTION_RECEIPT`; otherwise keep the
  task out of `COMPLETED` and select retry, fallback, replan, or blocker state.
- At material checkpoints, follow `references/execution-report-comments.md`.
  Require a human Issue report when a linked Issue and authorized comment
  capability exist. A prepared body or attempted call is not publication.
- When the preferred capability is unavailable, use the registry fallback only
  when it satisfies the same task contract; never silently downgrade quality or
  skip a mandatory specialist.

<!-- source-section:dev-workflow-standard:017 sha256:fdc4a76840c27190e4d5983dd99a83a744897e3492972cba7884adcc0a05afff -->
## When to Trigger Each Specialist

- API discovery during planning/spec: route relevant API, integration or
  validation-endpoint needs to `sdd-spec-factory` and its
  [API Research Library](../../../sdd-spec-factory/skills/sdd-spec-factory/references/api-research-library.md).
  Prioritize free APIs or a suitable free tier to validate application features
  and test the application when relevant; confirm limits and use synthetic data.
  That link is the monorepo source path. In an installed host, resolve the active
  `sdd-spec-factory` skill and its `references/api-research-library.md`; do not
  assume sibling plugin paths across versioned caches. If unavailable, report
  the missing reference and use an explicitly available canonical checkout,
  rather than pretending the installed skill contains it or auto-installing.
  Research directories provide candidates, not runtime availability or automatic
  approval. Require official-source checks, a recorded decision and validation
  plan; skip this research for unrelated tasks. Keep sources outside MCP/tool
  installation registries and preserve consent before external execution.

- `dev-environment-standard`: use cached environment `status` for required
  capabilities before execution. Route missing/broken prerequisites to targeted
  `prepare`/`repair`, then retry the original owner skill. Do not run full doctor
  for every task, infer connection from configuration, or install all tools.
  This capability does not own product implementation or DevOps.
  Use its persisted `platform_tools.selected_folder` and per-entry `eligible`
  routes; never infer native Windows support from WSL or repeat OS-choice
  questions on each task. Unvalidated entries require verification or an approved
  adapter. Context retrieval does not replace the ignored environment state.

- `devops-standard`: CI/CD, Docker/Compose, IaC, Kubernetes, GitOps, deploy,
  servers, cloud, observability, backup/restore, incidents and advanced
  Git/release strategy. Resolve its canonical skill, require a task and invoke
  it using the same execution contract and receipt. Basic status/diff/fetch,
  ordinary commit/push and PR work remain Harness/executor responsibilities.
  Security still owns scanners and security findings. Production/destructive
  actions require explicit target-specific human approval and rollback review.
  If Environment is available, route missing prerequisites to its selective
  prepare/repair, then return to DevOps. On bases without Environment, use
  the existing tool-state helper only; mark integration pending NOT VALIDATED.
  Do not synthesize another Environment plugin or MCP Library.

- `sdd-spec-factory`: required for COMPLEX work and for NORMAL work whose
  behavior is not already specified. TRIVIAL work uses the inline intent
  contract from the complexity gate.
- `ui-ux-standard`: **mandatory whenever there is UI** — new/changed screens,
  components, visual states, responsiveness, accessibility, or design-system
  adherence.
- `qa-testing-standard`: mandatory for changed behavior, bugfixes, user flows,
  APIs, business rules, persistent state, payments, tenancy, imports/exports,
  integrations, concurrency and regressions. QA planning may start before
  implementation; final QA depends on current executable artifacts. Docs-only
  or metadata-only work may record N/A with a reason. Never silently substitute
  the implementer's own tests for required independent QA.
- `security-standard`: **mandatory whenever the change touches** authentication,
  authorization, tokens, session, sensitive data, uploads, payments, or external
  integrations (also parsers, webhooks, infrastructure, privileged operations,
  tenant boundaries, secrets).
- Auxiliary CLIs/plugins: consultants only, for a real capability gap, after
  scoring and human approval (`references/continuous-improvement.md`).

<!-- source-section:dev-workflow-standard:020 sha256:3ee91f55e4438520623226dfe4eae324e4682bee9d8c07d3992a74888c3989c3 -->
## Reference Routing

- Consultative technical decisions in NORMAL/COMPLEX SDD: resolve the active
  SDD bundle's `references/technical-knowledge-router.md`; this checkout's
  canonical source is
  `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-knowledge-router.md`.
  Select only triggered topics. Require project source/version/purpose in existing
  Task/JSON reference fields and reconcile the PR Engineering Explanation with
  current owner receipts. Preserve specialist ownership and human gates;
  do not load the whole library or treat proposed tests as validation PASS.
  Missing/stale knowledge triggers the router's bounded official research and
  durable reference update; reuse compatible learned evidence and route generic
  plugin-source improvements through existing continuous-improvement review.
- Sector matrix, source purposes, phase dependencies and compatibility:
  `references/context-routing.md`
- Harness execution state, invocation evidence, retry/replan and completion:
  `references/harness-execution.md`
- Capability selection, preferred executors and fallbacks:
  `references/capability-registry.md`
- Executor LLM delegation, visible terminal, fallback, and prompt contract:
  `references/claude-delegation.md`
- Plugin/skill discovery, scoring, approval, and rollback:
  `references/continuous-improvement.md`
- Mandatory skill loading and execution evidence:
  `references/skill-execution-contract.md`
- Reuse and anti-overengineering review:
  `references/minimal-code-gate.md`
- Provider-neutral LLM replacement and checkpoint continuity:
  `references/llm-handoff.md`
- Human checkpoint reporting, anti-spam, publication evidence, and fallback:
  `references/execution-report-comments.md`
- Specialist-owned tool registries, local state, and fast/slow path:
  `references/skill-owned-tools.md`
- Portable environment bootstrap and MCP Library:
  `plugins/dev-environment-standard/skills/dev-environment-standard/SKILL.md`
- End-to-end pipeline across the specialist skills: `docs/workflow-pipeline.md`
<!-- end of selected V2 skill -->

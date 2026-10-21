# V1 inventory, THEOFFICE-V2-001

Audit date: 2026-10-16. Source: `Dev-workflow` main at `af94e8022eaec3e4eedfb4a2a62e13c6b349b9c4`.
The reference checkout was clean at audit start. Inventory is based on `git ls-files`, not temporary runtime files. `v1-inventory.json` records every tracked file, byte size and SHA-256, plus every canonical skill's section headings and references. It supports preservation verification; a matching hash does not prove runtime functionality.

## Distribution and capability inventory

342 tracked files; 12 plugin bundles, each carrying a canonical skill and host adapters. File extensions: 198 Markdown, 73 JSON, 38 Python, 14 YAML, 3 MJS, 2 YML, 1 Bash, 1 SVG, 1 HTML, 1 TGZ, 1 ZIP, 1 SHA256, 2 TXT, 2 extensionless and 4 tracked PYC. PYC files are inherited artifacts, not portable source or runtime evidence.

| Plugin | Version | Tracked files | Skill lines | Skill bytes | Reference files |
| --- | --- | ---: | ---: | ---: | ---: |
| `dev-environment-standard` | 0.1.0 | 15 | 169 | 9,945 | 3 |
| `dev-implementation-standard` | 0.1.0 | 8 | 255 | 14,196 | 1 |
| `dev-workflow-standard` | 0.7.0 | 24 | 678 | 38,885 | 15 |
| `devops-standard` | 0.1.0 | 29 | 157 | 10,436 | 17 |
| `parceiro-estrategico-global` | 0.1.0 | 6 | 264 | 17,058 | 0 |
| `qa-testing-standard` | 0.1.0 | 7 | 176 | 10,678 | 2 |
| `reverse-engineering-standard` | 0.1.0 | 20 | 76 | 3,759 | 2 |
| `sdd-spec-factory` | 0.1.0 | 30 | 523 | 30,200 | 13 |
| `security-standard` | 0.1.1 | 13 | 416 | 18,542 | 8 |
| `seo-standard` | 0.1.0 | 23 | 64 | 2,653 | 3 |
| `studio-prd` | 0.1.0 | 12 | 147 | 8,992 | 2 |
| `ui-ux-standard` | 0.3.0 | 12 | 276 | 13,073 | 6 |

Capabilities preserved by the existing bundles:

- Orchestration: complexity tiers, GitHub Issue/JSON equivalence, execution state, provider resolution, context retrieval, receipts, handoff, recovery, minimal-code and review gates.
- Environment: portable doctor/status/prepare/repair, MCP library, tool registries, consent, local-state fingerprints and platform selection.
- Product: briefing, module inventory, PRD and equivalent internal plan MD/JSON with stdlib plan validator/renderer.
- SDD: product/module/page/component/database/API/validation templates, complete module Tasks, v2 contracts, sector matrix, execution lists, consistency and knowledge routing.
- Implementation: developer code/tests, reuse inventory, minimal-code gate, execution reports; independent QA remains separate.
- UX: component selection/source/license inventory, design direction, tokens, cumulative HTML design guide, responsiveness, accessibility and visual QA.
- QA: strategy, regression, reproduction, fix verification and evidence-bound QA_STATUS.
- Security: threat model, coverage, flow analysis, false-positive validation, findings, remediation, OSV/ASVS research and publication gate.
- DevOps: GitHub governance/bootstrap, CI/CD, containers, cloud/IaC, Kubernetes/GitOps, operations, observability, release, backup/recovery and incidents.
- Reverse engineering: original REA gateway/runtime, provider selection and evidence/reconstruction handoff.
- SEO: vendored BeyondSEO 2.9.1 runtime/playbooks, technical/on-page/schema/AEO/GEO/intent/conversion analysis. This is outside the initial PRD's sector list but must remain available as a transversal capability.
- Global partner: behavior/discovery/writing/verification rules, optional global activation rather than mandatory duplication in every skill.

## Executable assets and catalogs

Canonical first-party entrypoints remain at their original paths: `environment.py`, `claude-visible-delegate.sh`, `context-retriever.py`, `provider-resolver.py`, `tool-state.py`, `github_governance.py`, Studio `plan.py`, REA `install-local-runtime.mjs` and `reverse-context-gateway.mjs`, SEO `bootstrap.py` and `seo-gateway.py`. `process-launch.mjs` is a shared REA runtime module. Tests also contain Python fixtures/utilities; not every Python file is a public entrypoint.

Seven specialist tool registries define 39 entries total: Harness Potpie; implementation unittest/pytest/pytest-cov/Hypothesis/Ruff/mypy; UI Playwright; Security Semgrep/Trivy/Gitleaks/ZAP/Bandit/pip-audit; DevOps 20 Git/infrastructure/validation tools; REA gateway/runtime/Cutter/Rizin; SEO BeyondSEO. The MCP library is separate public-provider metadata; actual connection/authentication must be probed in the active host. Provider registry lists OpenAI, NVIDIA, Groq, OpenRouter, Gemini and Anthropic. Catalog membership is not execution support.

Platform catalogs: `Tools (Linux)`, `Tools (Windows)`, `Tools (macOS)`, each pointing to 11 canonical entrypoints. They do not duplicate scripts or tool registries. Backend/payment/fiscal/commerce, Web3, APIs, UI/component and technical-knowledge catalogs already exist in SDD/UX references; migrate/index them, never replace with a shorter shortlist.

## Contracts and tests

The canonical v2 template is `plugins/sdd-spec-factory/templates/execution-contract-template.json`; Human Task is `task-template.md`. Existing normalization/validation behavior is exercised by `tests/test_execution_contract.py`, `test_task_contract_v2.py`, `test_sector_context_routing.py` and the example contract under `docs/examples/sector-context-qa/`. No standalone schema directory exists at baseline, so any V2 schema must preserve existing semantics and must not be advertised as an upstream schema.

29 `test_*.py` modules plus `portable_executable.py` and a Compose fixture cover structure, references, contracts, platform state, providers, governance, REA launch, SEO bootstrap, UX catalogs, QA and tool state. See baseline.md for actual execution result.

## Reverse-engineering provenance

`plugins/reverse-engineering-standard/runtime/rea-runtime.lock.json` pins `rea-agents` 4.1.0 from https://github.com/morluto/rea, MIT, vendored TGZ with SHA256 and required package contents. `runtime/ORIGIN.md` records upstream skill 26 and catalog of 130 MCP tools. `runtime/package.json` requires Node >=22.19.0 and `@modelcontextprotocol/client` 2.3.1. Preserve runtime, lock, gateway, tarball, attribution and static/runtime distinction. Optional Ghidra/Hopper/IDA/JADX/Binwalk/Unblob/Wakaru and supplemental Cutter/Rizin remain dependent on target, platform and separately evidenced availability. No engine was installed or analyzed during this inventory.

## Reference inventory

### dev-environment-standard

- `plugins/dev-environment-standard/skills/dev-environment-standard/references/mcp-library.json`
- `plugins/dev-environment-standard/skills/dev-environment-standard/references/operations.md`
- `plugins/dev-environment-standard/skills/dev-environment-standard/references/state-and-consent.md`

### dev-implementation-standard

- `plugins/dev-implementation-standard/skills/dev-implementation-standard/references/tool-registry.json`

### dev-workflow-standard

- `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/capability-registry.md`
- `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/claude-delegation.md`
- `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/client-portal.md`
- `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/context-retrieval.md`
- `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/context-routing.md`
- `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/continuous-improvement.md`
- `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/execution-report-comments.md`
- `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/harness-execution.md`
- `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/llm-handoff.md`
- `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/minimal-code-gate.md`
- `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/provider-registry.json`
- `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/provider-routing.md`
- `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/skill-execution-contract.md`
- `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/skill-owned-tools.md`
- `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/tool-registry.json`

### devops-standard

- `plugins/devops-standard/skills/devops-standard/references/ORIGIN.md`
- `plugins/devops-standard/skills/devops-standard/references/backup-disaster-recovery.md`
- `plugins/devops-standard/skills/devops-standard/references/ci-cd.md`
- `plugins/devops-standard/skills/devops-standard/references/cloud.md`
- `plugins/devops-standard/skills/devops-standard/references/containers.md`
- `plugins/devops-standard/skills/devops-standard/references/deployments.md`
- `plugins/devops-standard/skills/devops-standard/references/devops-operating-model.md`
- `plugins/devops-standard/skills/devops-standard/references/git-release.md`
- `plugins/devops-standard/skills/devops-standard/references/github-governance.md`
- `plugins/devops-standard/skills/devops-standard/references/gitops.md`
- `plugins/devops-standard/skills/devops-standard/references/incident-response.md`
- `plugins/devops-standard/skills/devops-standard/references/infrastructure-as-code.md`
- `plugins/devops-standard/skills/devops-standard/references/kubernetes.md`
- `plugins/devops-standard/skills/devops-standard/references/observability.md`
- `plugins/devops-standard/skills/devops-standard/references/review.md`
- `plugins/devops-standard/skills/devops-standard/references/server-operations.md`
- `plugins/devops-standard/skills/devops-standard/references/tool-registry.json`

### qa-testing-standard

- `plugins/qa-testing-standard/skills/qa-testing-standard/references/bug-report.md`
- `plugins/qa-testing-standard/skills/qa-testing-standard/references/test-strategy.md`

### reverse-engineering-standard

- `plugins/reverse-engineering-standard/skills/reverse-engineering-standard/references/rea-integration.md`
- `plugins/reverse-engineering-standard/skills/reverse-engineering-standard/references/tool-registry.json`

### sdd-spec-factory

- `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/api-research-library.md`
- `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/backend-component-sources.md`
- `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/devops-planning.md`
- `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/public-code-discovery.md`
- `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/spec-consistency-analysis.md`
- `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-apis-jobs.md`
- `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-architecture.md`
- `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-auth-sessions.md`
- `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-data-concurrency.md`
- `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-fiscal.md`
- `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-knowledge-router.md`
- `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-quality-operations.md`
- `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/web3-component-sources.md`

### security-standard

- `plugins/security-standard/skills/security-standard/references/coverage-model.md`
- `plugins/security-standard/skills/security-standard/references/false-positive-validation.md`
- `plugins/security-standard/skills/security-standard/references/finding-standard.md`
- `plugins/security-standard/skills/security-standard/references/preventive-security-research.md`
- `plugins/security-standard/skills/security-standard/references/report-template.md`
- `plugins/security-standard/skills/security-standard/references/review-pipeline.md`
- `plugins/security-standard/skills/security-standard/references/stack-profiles.md`
- `plugins/security-standard/skills/security-standard/references/tool-registry.json`

### seo-standard

- `plugins/seo-standard/skills/seo-standard/references/beyondseo-integration.md`
- `plugins/seo-standard/skills/seo-standard/references/site-delivery.md`
- `plugins/seo-standard/skills/seo-standard/references/tool-registry.json`

### studio-prd

- `plugins/studio-prd/skills/studio-prd/references/briefing.md`
- `plugins/studio-prd/skills/studio-prd/references/planning.md`

### ui-ux-standard

- `plugins/ui-ux-standard/skills/ui-ux-standard/references/anti-ai-design.md`
- `plugins/ui-ux-standard/skills/ui-ux-standard/references/component-selection.md`
- `plugins/ui-ux-standard/skills/ui-ux-standard/references/component-sources.md`
- `plugins/ui-ux-standard/skills/ui-ux-standard/references/library-source-handoff.md`
- `plugins/ui-ux-standard/skills/ui-ux-standard/references/live-design-guide.md`
- `plugins/ui-ux-standard/skills/ui-ux-standard/references/tool-registry.json`

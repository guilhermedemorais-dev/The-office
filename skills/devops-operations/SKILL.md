---
name: devops-operations
description: "Use for devops operations: Operational contract; Progressive domain routing. Load required core skills first."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: devops-operations

Source: `plugins/devops-standard/skills/devops-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, devops-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/devops-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/devops-standard/skills/devops-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/devops-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

Canonical link resolution (repository-relative paths, not skill-directory-relative):
- `references/devops-operating-model.md`: `plugins/devops-standard/skills/devops-standard/references/devops-operating-model.md`
- `references/tool-registry.json`: `plugins/devops-standard/skills/devops-standard/references/tool-registry.json`
- `references/review.md`: `plugins/devops-standard/skills/devops-standard/references/review.md`
- `references/github-governance.md`: `plugins/devops-standard/skills/devops-standard/references/github-governance.md`
- `references/git-release.md`: `plugins/devops-standard/skills/devops-standard/references/git-release.md`
- `references/ci-cd.md`: `plugins/devops-standard/skills/devops-standard/references/ci-cd.md`
- `references/containers.md`: `plugins/devops-standard/skills/devops-standard/references/containers.md`
- `references/deployments.md`: `plugins/devops-standard/skills/devops-standard/references/deployments.md`
- `references/server-operations.md`: `plugins/devops-standard/skills/devops-standard/references/server-operations.md`
- `references/infrastructure-as-code.md`: `plugins/devops-standard/skills/devops-standard/references/infrastructure-as-code.md`
- `references/kubernetes.md`: `plugins/devops-standard/skills/devops-standard/references/kubernetes.md`
- `references/gitops.md`: `plugins/devops-standard/skills/devops-standard/references/gitops.md`
- `references/cloud.md`: `plugins/devops-standard/skills/devops-standard/references/cloud.md`
- `references/observability.md`: `plugins/devops-standard/skills/devops-standard/references/observability.md`
- `references/backup-disaster-recovery.md`: `plugins/devops-standard/skills/devops-standard/references/backup-disaster-recovery.md`
- `references/incident-response.md`: `plugins/devops-standard/skills/devops-standard/references/incident-response.md`
- `templates/operational-change.md`: `plugins/devops-standard/skills/devops-standard/templates/operational-change.md`
- `templates/ci-cd-plan.md`: `plugins/devops-standard/skills/devops-standard/templates/ci-cd-plan.md`
- `templates/backup-restore-plan.md`: `plugins/devops-standard/skills/devops-standard/templates/backup-restore-plan.md`
- `templates/finding.md`: `plugins/devops-standard/skills/devops-standard/templates/finding.md`

<!-- source-section:devops-standard:002 sha256:1aec615d2748d2d18c1211556032e204eea1fc8f058e31c63c5e66e3a12756d4 -->
## Operational contract

1. Identify project-native commands, architecture, target environment/account,
   exact resource and protected data. Preserve existing Coolify, Portainer,
   Compose, VPS or cloud choices unless migration was approved.
2. Classify capability and risk. Choose the smallest viable toolchain; a cloud,
   Kubernetes, GitOps, Terraform or a new platform is never mandatory by default.
3. Read [operating model](references/devops-operating-model.md) and the relevant
   domain reference. Record baseline, bounded plan, required validations,
   `rollback_strategy`, health criteria and explicit authorization when needed.
4. Resolve available tooling through [tool-registry.json](references/tool-registry.json)
   and the existing Harness `skill-owned-tools.md` protocol. Use its
   `scripts/tool-state.py` helper, never a parallel installer. Registry entries
   are candidates, not a bulk installation request. Use Terraform **or** OpenTofu
   according to the project; `act` is optional.
5. Execute only approved scope. Validate static configuration, then authorized
   target behavior and representative service health separately. A successful
   lint/build/plan is not evidence of deployment or runtime health.
6. On FAIL: inspect output, confirm context and cause, correct within scope,
   revalidate and retain initial/final evidence. Escalate persistent failures,
   credentials, privileges or scope changes; never manufacture PASS.
7. Review candidates using [review](references/review.md). Return the existing
   `EXECUTION_RECEIPT`, update the Human Task and supply a factual
   `EXECUTION_REPORT_COMMENT` for the Harness. No new receipt type or state machine.

Existing states remain PENDING → READY → RUNNING → VALIDATING → COMPLETED,
with REWORK or BLOCKED when appropriate. Completion needs observed results and
required validation, not assignment, installed tooling or generated commands.
Record unavailable/unexecuted validation as **NOT VALIDATED**.

<!-- source-section:devops-standard:004 sha256:1ce173b6d32fea27339db5802e10f17713cfb2ca5895780d17a3a11b2b221495 -->
## Progressive domain routing

For client portal onboarding or Pages preparation, read the active Harness
`references/client-portal.md` (in this monorepo:
`plugins/dev-workflow-standard/skills/dev-workflow-standard/references/client-portal.md`).
Resolve the active bundle or explicit canonical checkout, not a guessed sibling
cache path. Prepare `docs/portal/` in the client project from the separately
supplied template only when available; an absent future repository is a portal
dependency, not a global onboarding blocker. Do not invent the template or a
deploy workflow. Preserve existing files, use the client's database via its
authorized backend, and distinguish static Pages output from private services.
Follow the existing human gates before publication or remote configuration.

| Active need | Read |
| --- | --- |
| repository governance/bootstrap, GitHub settings, Rulesets, Project, labels, Issue/PR templates or readiness | [GitHub governance](references/github-governance.md) |
| advanced Git, release policy, tags | [git-release](references/git-release.md) |
| pipeline configuration and validation | [ci-cd](references/ci-cd.md) |
| Dockerfile, image, Compose, container health | [containers](references/containers.md) |
| rollout, promotion, rollback | [deployments](references/deployments.md) |
| host configuration and Ansible | [server-operations](references/server-operations.md) |
| Terraform/OpenTofu lifecycle | [infrastructure-as-code](references/infrastructure-as-code.md) |
| Kubernetes, Helm, Kustomize | [kubernetes](references/kubernetes.md) |
| Argo CD / Flux reconciliation | [gitops](references/gitops.md) |
| account, region, cost and cloud controls | [cloud](references/cloud.md) |
| metrics, logs, traces, alerting | [observability](references/observability.md) |
| backup integrity and restore drill | [backup-disaster-recovery](references/backup-disaster-recovery.md) |
| containment, recovery and root cause | [incident-response](references/incident-response.md) |

Reusable task artifacts: [operational change](templates/operational-change.md),
[CI/CD plan](templates/ci-cd-plan.md), [backup/restore plan](templates/backup-restore-plan.md)
and [finding](templates/finding.md). Templates are planning aids, not executable
permission. Copy only the applicable fields into the project's existing docs.

<!-- end of selected V2 skill -->

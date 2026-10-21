---
name: implementation-delivery
description: "Use for implementation delivery: Task Status Rules; GitHub Projects Readiness; Recommended Task Template. Load required core skills first."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: implementation-delivery

Source: `plugins/dev-implementation-standard/skills/dev-implementation-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, implementation-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/implementation-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/dev-implementation-standard/skills/dev-implementation-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/dev-implementation-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

<!-- source-section:dev-implementation-standard:004 sha256:820ce4b27f3ec7613076fdf014d5187eba9b08c450ae8c9887519c6c00a9098d -->
## Task Status Rules

Visual status is updated in the task content, never in the physical filename:

- `🟡 Em andamento`: set this when starting execution.
- `🔴 Bloqueada`: set this when blocked, with the reason in `Bloqueios`.
- `🟢 Concluída`: set this only after implementation and validation evidence are
  recorded.

The task filename remains stable. Do not use emojis or status prefixes in the
filename.

<!-- source-section:dev-implementation-standard:007 sha256:e1e2c12a56703f5cfd53bb060e34215865d9f279a53a644c26cf4f329f4c3d34 -->
## GitHub Projects Readiness

Do not assume GitHub Projects is available. Keep the task ready for future
mapping by preserving these fields in the task content:

- status visual
- status Kanban
- responsável
- bloqueios
- specs obrigatórias
- branch sugerida
- issue criada / vinculada
- evidências
- Pronto para GitHub Projects: sim/não

If the fields are missing, stop before implementation and ask the orchestrator
to normalize the task.

<!-- source-section:dev-implementation-standard:008 sha256:f24128583d881834ff57512121a5d5096368f896aef9b5735d388c6db12b194c -->
## Recommended Task Template

Use the canonical `plugins/sdd-spec-factory/templates/task-template.md` in this
checkout, or resolve `templates/task-template.md` from the active SDD bundle.
Do not maintain another template here. It provides identity, scope, the Sector
Validation Matrix, source purposes, execution order, evidence ledger and human
gates. Request SDD normalization when needed; this executor does not invent
missing specs or waive required sectors.

<!-- end of selected V2 skill -->

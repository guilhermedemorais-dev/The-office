---
name: environment-core
description: "Use for environment core: Preamble; Preparation authority; Scope and security. Load required core skills first."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: environment-core

Source: `plugins/dev-environment-standard/skills/dev-environment-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/dev-environment-standard/skills/dev-environment-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/dev-environment-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

Canonical link resolution (repository-relative paths, not skill-directory-relative):
- `references/operations.md`: `plugins/dev-environment-standard/skills/dev-environment-standard/references/operations.md`
- `references/state-and-consent.md`: `plugins/dev-environment-standard/skills/dev-environment-standard/references/state-and-consent.md`
- `references/mcp-library.json`: `plugins/dev-environment-standard/skills/dev-environment-standard/references/mcp-library.json`

<!-- source-section:dev-environment-standard:000 sha256:966c31cc70db5fa70c01acbdb54635b0cada3e71fc3f10488f4c6d18e6be7f54 -->

# Dev Environment Standard

Own Environment Bootstrap / Plugin Health. The Engineering Harness supplies the
required capabilities; specialist skills retain ownership of their tools and
interpretation. Preparation does not replace implementation, SDD, security or
UI/UX, and an installation is not evidence that the specialist ran.

Read [operations.md](references/operations.md) before running the CLI and
[state-and-consent.md](references/state-and-consent.md) when preparing, repairing,
or accepting host evidence/custom MCPs. Consult [mcp-library.json](references/mcp-library.json)
for public MCP knowledge. LLM provider/model knowledge is owned by the Harness
provider registry when that plugin is available; Environment detects credentials,
runtime tools and host compatibility but does not duplicate the provider catalog.
Do not load every specialist's methodology merely to discover its registry.

<!-- source-section:dev-environment-standard:005 sha256:c3dc2cd66979c1fe9926b4586434a08723344364bea1ac8fe24d49c9f894ff09 -->
## Preparation authority

`AUTO_SAFE`, `PROJECT_SCOPED` and `USER_SCOPED` actions may execute only after
approval for the concrete action and scope. `AUTH_REQUIRED` prepares only as far
as the host safely supports, then hands authentication to the user.
`PRIVILEGED` returns `USER_ACTION_REQUIRED`; `MANUAL_ONLY` gives instructions;
`RUNTIME_PROVIDED` only detects. Missing runtimes never trigger silent admin/root
installation. Browser preparation selects only the required engine.

Keep lockfiles intact. Prefer npm ci, frozen pnpm, version-appropriate locked
yarn, and uv sync --locked. Python uses the existing isolated/project-approved
environment. Dependency lifecycle hooks execute project code and belong in the
action's approval scope. Do not use arbitrary shell strings from runtime state.

<!-- source-section:dev-environment-standard:007 sha256:8518aaa04abba76bca90a445821ef43067565c46d134573bb26bbc45ff942801 -->
## Scope and security

Do not persist or print passwords, tokens, API keys, OAuth tokens, cookies,
headers or raw host configuration. Provider setup may show the required
environment-variable name and official setup/documentation URL, but never the
secret value. Use host credential storage and scoped
permissions; report USER_ACTION_REQUIRED for a real manual auth requirement.
Do not acquire credentials as part of discovery. Custom provider claims require
review and stay local even after approval.

Advanced Git workflows, protections, CI/CD, Actions/GitLab/Jenkins, deploy,
SSH/VPS/cloud, Kubernetes/Terraform/Ansible, reverse proxies/Nginx, production
Docker and infrastructure observability belong to `devops-standard`.
Git detection and GitHub collaboration remain in scope. Application debugging
with Sentry is distinct from provisioning infrastructure.
<!-- end of selected V2 skill -->

---
name: environment-bootstrap
description: "Use for environment bootstrap: Choose the operation; Bootstrap loop. Load required core skills first."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: environment-bootstrap

Source: `plugins/dev-environment-standard/skills/dev-environment-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, environment-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/environment-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/dev-environment-standard/skills/dev-environment-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/dev-environment-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

Canonical link resolution (repository-relative paths, not skill-directory-relative):
- `scripts/environment.py`: `plugins/dev-environment-standard/skills/dev-environment-standard/scripts/environment.py`

<!-- source-section:dev-environment-standard:001 sha256:6e61589cac600bca51369dd40c157078e21e018d53ceba6d0b2d5d4f6e6e9111 -->
## Choose the operation

- **doctor**: read-only discovery and health report. No installation, cache
  writes, persistent invalidation or automatic test runs with side effects.
- **prepare**: diagnose, plan CORE/required/selected capabilities, obtain missing
  choices and explicit approval, apply supported actions, verify and persist.
  Dry-run is read-only. CORE is a priority, not permission to install blindly.
- **repair**: identify a real failed component, invalidate only its stale
  observation, then prepare/verify that component under the same consent rules.
- **status**: compatible cached report plus cheap checks. Reuse it before tasks;
  run doctor only after incompatible state, missing evidence or a real failure.

The executable is [scripts/environment.py](scripts/environment.py). Use Python
3.11+ and explicit repository/workspace paths; discover these paths from the
current installation, never assume a particular developer's home directory.
The repository root identifies plugin knowledge; workspace identifies the
project being prepared. They can be different.

<!-- source-section:dev-environment-standard:002 sha256:023830f62345ab4570750756340f64713cc463c855c380e924592b2e6b3b22a0 -->
## Bootstrap loop

1. Inspect source of truth, current task requirements and actual host tools.
2. Run doctor. Separate plugin structure, available tools, connection and auth.
3. Discover all canonical skills. For each existing `references/tool-registry.json`,
   validate owner and entries, then use the shared `tool-state.py` helper.
   Skills without a registry still undergo structural health checks.
4. Plan only CORE, task requirements, selected components and their necessary
   bootstrap-safe prerequisites. Prefer what already exists and the project's
   lockfile/package manager. Never install all tools, browsers or managers.
5. On first prepare, show RECOMMENDED and OPTIONAL choices with capabilities.
   Offer PROJECT_SPECIFIC entries only when the project warrants them. Ask:
   **“Você utiliza algum MCP específico que não está nesta biblioteca?”**
6. Persist explicit choices and not_requested outcomes without treating silence
   as installation approval. A declined/ignored optional is not an every-session
   prompt. Revisit only when requested, reset, newly required, broken, changed
   materially, project-specific, or incompatible.
7. Present concrete actions, provider, version, scope and permissions. Apply
   only approved actions supported by the host. Preserve existing definitions;
   a conflict requires review, never an overwrite.
8. Verify tool presence/execution and MCP availability/connection/auth separately.
   Use host tools for connection and authentication; a config entry is insufficient.
   When the Harness requests multi-provider execution, run its provider status/
   probe flow without printing secrets. A provider config or environment-variable
   name is not proof of an executable model.
9. When `reverse-engineering-standard` is selected, detect Node.js 22.19+ and
   the plugin-local reverse context runtime. If runtime dependencies are absent,
   propose the scoped install inside
   `plugins/reverse-engineering-standard/runtime/`; after approval run
   `npm run bootstrap` there, which verifies and installs the vendored REA
   tarball, and then run `node reverse-context-gateway.mjs probe`. Do not globally install REA or
   optional engines by default. Install/prepare Ghidra, Hopper, IDA, JADX,
   Binwalk, Unblob or Wakaru only when the selected target actually requires
   that provider and the user approves the preparation.
10. When `seo-standard` is selected, detect Python 3.10+ and the plugin-local
    SEO runtime. If it is absent, propose the scoped bootstrap under
    `plugins/seo-standard/runtime/`; after approval run `python bootstrap.py`
    and then `python seo-gateway.py probe`. Prefer the vendored BeyondSEO
    release. Do not install browser support or crawl arbitrary sites unless the
    selected Task requires it and scope is authorized.
11. Persist sanitized local observations and return HEALTH_REPORT plus human
   summary, installations actually performed, blockers and next action.

<!-- end of selected V2 skill -->

---
name: reverse-engineering-core
description: "Use for reverse-engineering core: Preamble; Preconditions; Safety and legal boundary; Relationship with other skills. Load required core skills first."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: reverse-engineering-core

Source: `plugins/reverse-engineering-standard/skills/reverse-engineering-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/reverse-engineering-standard/skills/reverse-engineering-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/reverse-engineering-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

Canonical link resolution (repository-relative paths, not skill-directory-relative):
- `references/rea-integration.md`: `plugins/reverse-engineering-standard/skills/reverse-engineering-standard/references/rea-integration.md`
- `references/tool-registry.json`: `plugins/reverse-engineering-standard/skills/reverse-engineering-standard/references/tool-registry.json`

<!-- source-section:reverse-engineering-standard:000 sha256:9d2a8fee3471b3b3a2bc06e9709b7aeadd6662ccf87049e6e7c0e10f1e8e8757 -->

# Reverse Engineering Standard

Own authorized reverse-engineering investigations inside the Engineering Harness.

Use this skill when the answer depends on behavior or structure of a shipped
artifact rather than an ordinary source repository. For normal source analysis,
use repository/code tools and do not invoke REA merely because it exists.

Read [rea-integration.md](references/rea-integration.md) whenever reverse
engineering runtime capabilities are used. Consult
[tool-registry.json](references/tool-registry.json) for tool ownership and use
the bundled reverse-context gateway as the normal execution boundary.

<!-- source-section:reverse-engineering-standard:001 sha256:01ec843ddad818976da4bd9947ceef5ec71de601f8e6f0f8b6ae493fd9be241d -->
## Preconditions

Before analysis:

1. Identify the target artifact/app and authorized scope.
2. Confirm the task/list and current revision when running under the Harness.
3. Read this SKILL completely and emit the normal SKILL_RECEIPT.
4. Separate what may be inspected from what must not be executed or mutated.
5. Resolve the smallest analysis capability required.

If target authorization is unclear, stop before active/runtime inspection.

<!-- source-section:reverse-engineering-standard:003 sha256:eef45307ed85f7b3bbcee1ef00474c3519a4eb8cd87bc5438dac02933d3ca18a -->
## Safety and legal boundary

Operate only on systems, software and artifacts the user owns, controls or is
authorized to inspect. Defensive interoperability, compatibility, migration,
research and feature reconstruction are valid uses.

Do not:
- steal credentials, secrets or personal data;
- create persistence, malware, covert access or evasion;
- attack third-party services;
- bypass licensing/DRM for unauthorized access;
- run destructive payloads against production;
- present proprietary source recovered from an artifact as newly authored code.

When the requested outcome is a compatible implementation, write an independent
spec from observed behavior and build new code through the normal Harness flow.

<!-- source-section:reverse-engineering-standard:004 sha256:14b411513758acc7d1dab568f1cd1eded4b36978e1f1e50dddc468463b0d0a60 -->
## Relationship with other skills

- sdd-spec-factory converts validated findings into product/technical specs.
- dev-implementation-standard writes the independent implementation.
- qa-testing-standard validates reconstructed behavior.
- security-standard owns AppSec findings and vulnerability claims.
- devops-standard owns deployment/infrastructure implications.
- dev-workflow-standard owns final routing, handoff and gate reconciliation.

Reverse engineering evidence does not grant permission to change the Task scope.
<!-- end of selected V2 skill -->

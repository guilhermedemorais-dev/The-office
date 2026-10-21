# Stack CLI discovery and selected preparation

Owner request (2026-10-21): require the responsible sector to research official
stack documentation for suitable CLIs; pre-catalog Python, React, Next.js, NestJS,
Vue and related tools; allow necessary selected installation. Clarification:
Next.js has a project CLI (`next`) as well as its scaffolder (`create-next-app`).

## Implemented

- `library/tools/stack-clis.json`: 11 records with official documentation,
  repository, package, purpose, sector, version policy, command templates,
  installation/probe notes and explicit unobserved runtime state.
- Distinct entries: Python runtime and pip; React via documented ecosystem
  create-vite; Next.js create-next-app and next; NestJS CLI; Vue create-vue and
  maintenance-only legacy Vue CLI; shadcn CLI; Django CLI; FastAPI CLI.
- `library/tools/stack-cli-policy.md`: catalog-first search, gap/version-triggered
  official research, reuse, suitability validation, scoped automatic installation
  under the owner's authorization, verification and evidence.
- Root and Frontend/Backend/Environment responsibility contracts route the policy.
- Shared metadata builder indexes both files; no parallel installation engine or
  duplicate sector tool registries are created. Discovery templates cannot be
  fed blindly into an executable runner.
- No paid service/account linking, global install, stack migration, container,
  deployment or existing-repo re-scaffolding is implied. Existing host gates stay.

## Sources reviewed

All URLs are in the central records, reviewed on 2026-10-21. Official Python/PyPA
venv and packaging guidance; React creating-an-app/from-scratch guidance; Next.js
create-next-app and next CLI references; NestJS CLI overview; Vue quick start and
legacy CLI maintenance notice; shadcn CLI/registry; Django 5.2 CLI reference;
FastAPI CLI documentation. Read docs matching the selected project's version
before execution; these entries are not a claim that all projects use latest.

## Executed verification

`python -m unittest discover -s tests -v`: 689 tests discovered, 682 passed,
7 native-Windows skips, zero failures (8.065 s on this Linux runtime).

New tests run actual shared lookups for Next.js, NestJS, React/Vite, Vue and Python,
confirm catalog reuse without external research, and verify metadata regeneration
and content hashes. `git diff --check` passed.

## Limits

This change implements agent instructions and catalog discovery using the existing
preparation mechanisms. It is not a background automatic installer. No stack CLI
was downloaded, installed, started or operationally verified by this change; no
client application is selected here. Installations occur only when a later Task
selects a necessary compatible CLI and the host permits that operation. Runtime
state remains NOT_OBSERVED/NOT_VALIDATED. Native platform support, installation
success and token reductions are not claimed.

## Owner addition: Nx and OpenTofu

Two additional records bring the catalog to 13 entries. Nx supports selected
workspace generation and configured dependency boundaries; OpenTofu manages
infrastructure definitions and operations. Architecture and DevOps contracts now
route these optional tools. Source documentation was read from Nx Nest/boundary
guides and OpenTofu introduction; platform-specific installation documentation is
a conditional reference to verify before installation, not a claimed executed
procedure. Existing project toolchains remain preferred. No tool is installed,
no remote service enabled and no infrastructure/state operation executed here.

# Consolidated V2 execution policy

Owner-approved V2 overlay, 2026-10-21. The preserved plugins and their generated
source excerpts retain historical V1 wording. For V2 execution, the bounded inline
exception below overrides incompatible legacy mandatory-entry, executor, JSON,
receipt and all-sector requirements ONLY for confirmed TRIVIAL work with no
pre-existing approved execution contract or stricter project policy. Existing
approved JSON v2 contracts, specialist triggers, security and human gates remain.
NORMAL/COMPLEX tasks keep their applicable contracts and evidence requirements.
This is a local precedence decision, not a vendor runtime enforcement mechanism.

## Change Complexity Gate

Classify the work before choosing artifacts. Complexity changes documentation
depth, not the obligation to validate.

- `TRIVIAL`: a localized, low-risk change with no behavior, architecture,
  security, data, dependency, or public-contract impact. Use an inline intent
  contract: scope, acceptance criterion, command/check, and evidence. A durable
  spec, task file, and Issue are optional unless repository policy requires one.
  Do not require a ten-sector matrix, JSON v2, SDD, execution lists, a separate
  executor runtime, or separate receipt/report templates for this path.
- `NORMAL`: bounded behavior or multi-file work with understood architecture.
  Use a concise Issue/task contract linked to the relevant existing docs; add a
  focused spec only for behavior that is not already specified.
- `COMPLEX`: architecture, cross-module behavior, migrations, sensitive data,
  security boundaries, substantial UI, integrations, or unresolved product
  decisions. Use durable SDD artifacts, executable tasks, traceability, and the
  applicable specialist gates.

When risk is uncertain, choose the higher tier. UI and security triggers are
based on affected surface and risk, not on the tier label.

### TRIVIAL inline execution

1. Inspect the request, current files, branch and diff. Record the objective,
   allowed paths, acceptance criterion and relevant validation in a short intent.
   Examples: correcting prose or a comment without changing executable content.
2. Check for behavior, architecture, infrastructure, security, data, dependencies,
   public contracts and specialist triggers. If any applies or is uncertain,
   reclassify before editing and use the full workflow. A visual/responsive change
   still triggers UI/UX; a small bugfix still triggers independent functional QA.
3. Execute in the same agent when available tools suffice. Load only a selected
   skill and its applicable references when needed; an existing compatible tool
   requires no whole-inventory discovery, provider probe or new agent. Search the
   affected scope for reuse before adding content. Never install or mutate remote
   infrastructure to make a trivial change possible.
4. Validate the actual diff and run the relevant check. If impact expands, stop
   this path, preserve the diff, and reclassify; do not silently expand scope.
5. Return changed paths, the check and result, limitations and branch/commit when
   present. This compact evidence replaces the separate SKILL_RECEIPT,
   REUSE_INVENTORY, MINIMAL_CODE_GATE, EXECUTION_RECEIPT and report templates only
   for this path. Never claim another agent ran or independent review occurred.

An existing Issue may receive one consolidated outcome. Missing remote access
does not block local TRIVIAL work unless repository policy requires it. Human
approval, protected paths, no secrets, no destructive actions, and no automatic
merge/deploy remain unchanged. These instructions are an agent protocol, not a
runtime authorization firewall or proof of token savings.


## Material technical decisions

For material architecture, API, stack, UI, dependency, security or operational
choices, read `library/architecture/technical-decision-procedure.md`. Reuse valid
project evidence first, otherwise consult official version-matched documentation.
Do not reload all catalogs or repeat Discovery. A documented choice does not
justify scope expansion; keep traceability and bounded recovery.

## Capability discovery ownership

The responsible sector consults its catalog/index first. For a genuine gap it
researches external candidates, adapts the integration and validates applicability.
The Librarian registers approved source/version/evidence centrally and updates
sector views. Do not create circular approval or automatic repeated research.
Before PRD/spec decisions, present relevant available options and gaps, not the
whole catalog. Read selected skill bodies and conditional references only. This selective lookup
rule supersedes older whole-inventory consultation requirements in preserved
procedures; it never removes an actually selected mandatory source.

## Operational scope guard

For selected Compose changes, DevOps uses `library/tools/compose-scope.py` to
compare reviewed rendered JSON against the proposed configuration with exact
allowed resource names. Never create a service/container per logical module by
default. The guard never invokes Docker and cannot prove health or security.
Security still reviews sensitive configuration changes. No merge or deployment
is authorized by a passing scope comparison.

## Documentation and delivery checkpoints

The owner-requested closure overlay is `docs/operations/delivery-lifecycle.md`.
It applies to every Task; TRIVIAL satisfies it in its existing inline result.
Documentation and progress do not require a new Task or persistent agent.

# ADR-001: additive modular overlay and preserved V1 distribution

Date: 2026-10-16. Status: accepted within approved implementation scope. Classification: LOCAL DECISION.

## Context

V1 has interconnected plugin paths, receipts, scripts, catalogs and structural tests. Moving every file immediately would risk compatibility without delivering required context selection.

## Decision

Keep imported V1 plugins intact at their canonical paths. Add `agents/`, functionally decomposed `skills/`, `library/`, platform metadata and explicit CLI selection. Preserve every source section with provenance and coverage checks. New entrypoint selects V2; old installed entrypoints retain V1 semantics until deliberately upgraded.

## Alternatives and consequences

A wholesale move needs many fragile aliases and would obscure provenance. Rewriting procedures would risk losing normative meaning. The additive overlay increases distributed bytes and requires generated coverage checks, but bounds risk and permits targeted rollback. Disk duplication is accepted; active context selection is the optimization target. Metadata plans and character measurements do not prove LLM quality or token savings.

## Validation and rollback

Execute inherited tests, new routing/coverage/negative-path tests and diff checks. Compare actual source hashes and rule destinations. Revert overlay commit(s) to return to the imported distribution; no remote production changes are required. Native OS and host execution remain separately validated.

## Explicit additional contract sectors

Keep all ten canonical v2 sector IDs unchanged. Add `architecture` (SDD owner) for MT-03 and `environment` (Environment owner) for MT-07/08 in this Task, with explicit rationale. The canonical context-routing contract permits additional material domains with concrete owner and reason. These additions avoid making Harness attest another owner's deliverable and remain final Harness dependencies; older hosts must verify support before consuming them.

## Existing execution-list phases

This Task retains `implementation` for execution lists and `validation` for reviews; `planning` remains supported for early sector planning. The preserved V1 contract template already uses `implementation`; these are phase labels, not a new state machine. The V2 helper distinguishes all three and must reject unknown values.

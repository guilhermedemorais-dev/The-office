# The Office V2 module specification

Task: THEOFFICE-V2-001. Contract revision: 1. Complexity: COMPLEX. Approved source: user PRD dated 2026-10-16, explicitly accompanied by construction/push instruction. This is one cohesive migration module with internal microtasks. No new discovery interview is required.

## Product, users and approved outcome

The owner and engineering-agent hosts need a maintainable Harness with bounded sector contracts, selected procedures, shared reusable knowledge and current validation evidence. The existing V1 works but extensive skills, overlap, repeated research and unclear platform state increase context and maintenance cost. Preserve useful behavior and contracts while adding functional decomposition and explicit discovery. No themed television assets, simulated agents, demo application, merge or deploy are in scope.

Source repository: https://github.com/guilhermedemorais-dev/Dev-workflow , commit `af94e8022eaec3e4eedfb4a2a62e13c6b349b9c4`. Destination: https://github.com/guilhermedemorais-dev/The-office . Work branch: `feat/the-office-v2`. Human Task: https://github.com/guilhermedemorais-dev/The-office/issues/1 . Structured source: `docs/execution/THEOFFICE-V2-001.json`.

## Requirements

| ID | Approved obligation | Execution slice | Acceptance / verification |
| --- | --- | --- | --- |
| REQ-PARITY | Inventory every V1 skill/rule/reference/tool; preserve source and map sections to V2 destinations without destructive summary | MT-01,02,05,08 | AC-01; inherited tests and section/source hash coverage |
| REQ-ROUTING | Fourteen sector responsibility contracts, short orchestrator, transversal librarian, skills selected on demand with mandatory core | MT-03,04,05 | AC-01,02; route/core/unknown-ID/owner/revision tests |
| REQ-GOVERNANCE | Same Issue/JSON v2 semantic content, revision, ten existing sectors, receipts, dependencies and one complete Task per functional module | MT-03,04,12 | AC-01,03; handoff/graph/revision validation and owner evidence |
| REQ-LIBRARY | Shared metadata lookup; prioritize Task/project/local/distributed/inherited/host resources; preserve license/version/source; conditional external research | MT-06 | AC-02; lookup/retrieval/stale/path negative tests |
| REQ-ENVIRONMENT | Detect real host and OS; distinguish support from operational proof, retain Win10 work and explicit Win11/macOS limits; WSL uses Linux | MT-07 | AC-02; inherited environment tests plus platform metadata checks |
| REQ-REA | Preserve original REA engine/provider, gateway, distribution and integrations; authorized analysis and clean-room constraints | MT-08 | AC-01,02; preserved hashes and safe runtime/fixture tests when available |
| REQ-DOCUMENTATION | Document Harness and real client product behavior; librarian templates, user procedures, real capture provenance and optional same-source Help Center | MT-09 | AC-03; source/path/doc review; no fabricated screenshots |
| REQ-VALIDATION | Independent regression QA/security; compare scenarios A-F using actual available telemetry, no invented native support or token gain | MT-10,11,13 | AC-02; exact commands/results, raw logs and explicit gaps |
| REQ-DELIVERY | Review diff/secrets, isolated commits/push/PR, final report, install/manual smoke guide and local homologation list | MT-12 | AC-03; returned branch/PR URLs and commit SHAs |

## Business rules

Agent owns outcome, skill supplies procedure, tool executes, library supplies reusable resources, Task records history. Never instantiate every agent or load every sector skill automatically. A procedural capability reads its complete SKILL.md, mandatory core and active references; source preservation on disk alone does not prove correct selection. No microaction-per-skill or layer-per-Issue fragmentation.

GitHub Issue is Human Task; JSON v2 has equivalent normative meaning. Mutable progress, evidence, logs, token telemetry and receipts stay in comments/ledgers. Preserve IDs and normative formats. Missing evidence is not PASS; only the owner validates its sector. Planning receipts do not close final validation. Material scope changes update both normative representations before affected work.

Library results are candidates, not execution or installed dependencies. External skills require source/version/script/dependency/permission/license/maintenance/conflict checks and applicable host approval before installation. Local private discoveries never silently alter distributed catalogs. Optional failure permits bounded compatible fallback, not removal of capability. No credentials in source metadata.

## Banco

N/A: no application database or migration is introduced. JSON metadata uses versioned files. Existing V1 data knowledge and catalogs remain preserved.

## API/Backend

Local Python helper offers metadata planning, search, targeted read and contract handoff support. It executes no agents, remote search, external tool installation, authentication, merge or deploy. Inputs are sector/capability IDs, query strings, repository-relative source paths, canonical Task/list/revision and optional explicit index paths. Outputs distinguish planned from executed; unknown IDs, stale sources, traversal, malformed graphs and revisions block the affected operation with nonzero exit. Existing CLI/MCP/provider runtimes remain canonical.

## Frontend/UI

N/A: no product UI. UX procedures are decomposed and retained for target-product work. No television brand, characters or art are distributed. Do not fabricate office animations or live agent activity.

## Testes

Run inherited `python -m unittest discover -s tests -v`, new V2 route/library/contract/platform/source-coverage checks, `git diff --check` and documented handoff smoke. Record command, runtime, exit, skips and raw evidence. Compare baseline vs candidate without ignoring introduced failures. QA and security return their own findings. Native Win10, Win11 and macOS, live REA providers and additional hosts remain NOT_VALIDATED unless those exact environments executed.

Benchmark scenarios: A trivial UI route; B backend implementation route; C complete module plan; D cached/reused library lookup; E missing optional tool; F scope/revision change. Record actual static bytes/latency/results as such. Tokens, cached tokens, tool calls, delegates, retries, rework, interventions and end-to-end quality require real telemetry; unavailable fields are NOT_AVAILABLE. No percentage token-savings claim from text length alone.

## Segurança

Constrain local source resolution, avoid private runtime/secret paths, never execute discovered code, maintain host approvals and preserve REA authorized-use boundaries. Negative tests cover invalid inputs and references. Security review concerns the actual helper/distribution changes, not a guarantee about every external provider. Preserve OSV and canonical safety references.

## Observabilidade/logs

Keep observable command/test/benchmark results, source hashes, issue/PR links and limitation records under migration evidence and Issue comments. No daemon or application telemetry backend is introduced. JSON normative instructions contain planned test identifiers, not mutable results or credentials.

## Decisões pendentes

No routine implementation decision requires owner response. Final acceptance, merge/deploy, native host/OS homologation and any material product-scope expansion remain separate. ADRs record additive overlay, shared metadata/state separation and documentation content ownership. Unknown external tools are not approved dependencies.

## Riscos

Compatibility entrypoints still expose original V1 context loading until the host selects V2. Modular extraction preserves every source section but semantic grouping and host behavior require actual review. Native/provider tests may be unavailable. Local metadata may be stale; source digests and explicit availability prevent false operational claims. Existing unrelated baseline failures must remain visible.

## Critérios de aceite

AC-01 preserves canonical source paths/contracts and full section coverage with bounded selected skills. AC-02 executes regression and negative-path validation with no ignored introduced failure and explicit unsupported boundaries. AC-03 supplies destination branch/commits/review PR, documentation/install/smoke/evidence report, without merge or deploy. All REQUIRED sectors need current owner evidence before task completion; software completion alone is insufficient.

## Authorization

User approval explicitly authorizes reversible implementation in isolated branch and push to confirmed destination. Do not request repeated routine approval. Source main, destination main, production, destructive changes, unknown credentials, merge and deploy remain outside authorization.

## Reference selection and provenance

Read canonical V1 Harness, SDD, context-routing, technical knowledge-router and consistency-analysis sources before writing this spec. They define existing governance. Official Diátaxis, Microsoft procedure guidance and Docusaurus docs were retrieved on 2026-10-16 to support documentation structure; their metadata and precise use are in `library/documentation-templates/README.md`. The additive overlay and metadata helper are LOCAL DECISIONS, not claimed vendor standards. Other PRD literature/reference candidates are not asserted as retrieved or executed. No external template defines target-product behavior.

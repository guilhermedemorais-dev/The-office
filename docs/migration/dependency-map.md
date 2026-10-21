# Dependency map, THEOFFICE-V2-001

Source main: `af94e8022eaec3e4eedfb4a2a62e13c6b349b9c4`. This map records contracts found in canonical SKILL bodies, registry metadata and executable manifests. It describes dependencies, not proof that a host loaded them.

| Owner | Depends on | Contract and boundary |
| --- | --- | --- |
| Harness | SDD templates, specialist skills, Environment | Receives scope; resolves capabilities; reconciles sector receipts; never fabricates specialist PASS |
| Product / studio-prd | Existing decisions, SDD, UX when UI, REA conditionally | Produces PRD/plan; complete module Task belongs to SDD |
| SDD | Harness context-routing; UX, Security, QA, DevOps conditionally | Produces same-revision Human Task and normative JSON v2; one Task per module |
| Implementation | Approved JSON list, required sources, Harness minimal-code gate | Owns code/developer tests; consumes SDD specs; returns current revision evidence |
| UX | Project design artifacts, its component catalog and tool registry | Owns rendered visual/design validation; functional QA remains independent |
| QA | Current implemented revision, required dependencies, shared test tools | Independent behavior/reproduction/fix validation; cannot attest Security or UX |
| Security | Actual source/data flows, registry, preventive OSV/ASVS references | Owns confirmed security findings and release gate; scanner output is a candidate |
| DevOps | Exact target and approval; Environment/tool-state; Security for sensitive changes | Owns infrastructure/governance; ordinary Git remains Harness/executor |
| Environment | All discovered skill registries, MCP library, tool-state helper | Detect/prepare/verify prerequisites only; no product/infrastructure ownership |
| REA | Node >=22.19, local gateway/client, pinned vendored REA, target providers | Transversal analysis; findings feed SDD; no replacing REA with prompts |
| SEO | Python, pinned BeyondSEO, optional renderer, target scope | Transversal SEO analysis; code changes return to Implementation |
| Provider routing | Harness provider-registry, actual credentials/runtime evidence | Owner skill selected before model; CONFIGURED is not AVAILABLE |
| Context retrieval | Potpie if verified; lexical local fallback | Supplements normative required sources; cannot replace them or environment state |

## Shared ownership that must remain canonical

`plugins/dev-workflow-standard/scripts/tool-state.py` is the common specialist-tool state resolver. Environment owns MCP/environment state, including OS selection and user preferences. Keep those stores separate. Do not create another installer/cache for QA or the Bibliotecário. QA may use implementation's test runners and UX's Playwright without duplicating installation ownership.

Task equivalence, source purposes, revisions, receipts, handoff and evidence are cross-cutting governance. These are repeated in multiple skills to define owner boundaries; extract shared instructions carefully rather than deleting safeguards. The ten existing validation sectors are a contract model, distinct from the V2 logical agent count. Adding agents is not authorization to rename sectors in existing JSON.

## File coupling and compatibility

- The 12 bundles expose `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json` and root `plugin.json` with canonical skills. Preserve published paths while adding V2 entrypoints.
- Platform catalogs reference original entrypoint paths. Tests and references also use them. Moving an implementation requires migration of every importer/fixture/catalog or an adapter at the old path.
- SDD and other skills explicitly reject assumed sibling installed-cache paths. Resolve active bundles or an explicitly identified canonical checkout.
- REA gateway uses `process-launch.mjs`, local dependencies and runtime lock/package artifacts. Bootstrap now respects the committed lockfile (V1 commit `92560aa`, included in the merge baseline).
- Historical Tasks, receipts and examples are evidence and compatibility inputs; do not mass-normalize inactive contracts or treat old receipts as validation of V2.

## Host and OS are independent

V1 ships host adapters for Codex, Claude Code and Antigravity. This audit verifies files only; no host installation/discovery certification follows. Work's available tools differ from any local host. WSL is Linux execution. Windows 10 native prior receipts do not establish Windows 11 or macOS support. Linux-specific `claude-visible-delegate.sh` requires Bash/gnome-terminal and has no validated Windows/macOS counterpart.

## Recommended migration boundary

Keep the inherited plugin tree and first-party tools in place as compatibility assets. New small agent contracts should select functional skills and exact legacy sections through metadata. The shared library should index existing sources with provenance and cache invalidation rather than duplicate source bodies. Preserve license notices and distinguish distributed knowledge, project extensions, user-local knowledge and operational state.

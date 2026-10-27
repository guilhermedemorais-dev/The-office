# Optional Graphiti decision memory

This trusted-local CLI supplements the canonical required-source → Potpie/local
retrieval workflow. It does not replace source control, approvals, owner receipts,
the reference library, or REA. No runtime, service, credentials, or external memory
are installed or started by this bundle. Default configuration is disabled.

## Implemented behavior

- Explicit project ID and exact source-path allowlist, no automatic global group.
- Committed UTF-8 source snapshots only, at the supplied full commit SHA and
  still matching current workspace bytes; a receipt reference records the caller's
  approval claim. The CLI does **not** authenticate or independently verify approval.
- Basic credential-pattern, binary, generated/secret directory, size, symlink and
  hardlink guards. These are not a complete DLP system; review selected sources.
- Private ignored SQLite journal at `runtime-state/memory/<project>/journal.sqlite3`.
  `enqueue` stores a local snapshot and returns QUEUED, never PERSISTED.
- `sync` awaits Graphiti SDK `add_episode` and checks the acknowledged episode ID.
  Deterministic IDs prevent ordinary duplicate local submissions. Process crashes
  leave PROCESSING; ambiguous exceptions become UNKNOWN, without automatic replay.
- `search` accepts at most ten facts, caps candidate/query/fact sizes, scopes to
  the project group and requires **all** episode origins to match persisted local
  records whose canonical source hashes/revisions still match. Unknown origins,
  stale sources, future/invalidated/expired facts and missing validity dates drop.
  Returned text is `SUPPLEMENTAL_UNTRUSTED_DATA`, never executable instructions.
- Provider unavailability yields an explicit empty/fallback result. The existing
  Potpie/local backend remains responsible for code context.

This is a single trusted local caller adapter, not an authenticated memory server
or tenant security boundary. A unique project ID partitions memory; it does not
authorize callers. Do not expose the upstream reference MCP publicly: it has no
authentication or authorization and exposes destructive tools. This integration
does not use that server or export its delete/clear operations.

## Run after project-scoped environment setup

Copy `config.example.json` to ignored local state, choose a repository-unique ID,
list only approved source files, and explicitly set `enabled` to true. Create
private state directories (mode 700 on POSIX). Run from the checkout root:

```sh
python integrations/memory/adapter.py --workspace . --config runtime-state/memory-config.json status
python integrations/memory/adapter.py --workspace . --config runtime-state/memory-config.json enqueue --source docs/specs/approved-module.md --revision FULL_40_CHARACTER_COMMIT_SHA --approval TASK-ID:rev1:receipt --reference-time 2026-10-27T08:00:00Z
python integrations/memory/adapter.py --workspace . --config runtime-state/memory-config.json sync --limit 5
python integrations/memory/adapter.py --workspace . --config runtime-state/memory-config.json search --query 'Why was this database selected?' --as-of 2026-10-27T09:00:00Z --limit 5
```

Example times are placeholders; use the actual event time with timezone and
current retrieval time. An example receipt is not authorization. `enqueue` and
`status` need only Python stdlib and Git. `sync/search` lazily require exactly
`graphiti-core==0.31.2` and a trusted local Neo4j backend. Supply credentials via
host environment (`OFFICE_MEMORY_NEO4J_PASSWORD`, optional
`OFFICE_MEMORY_NEO4J_USER`, `OFFICE_MEMORY_NEO4J_URI`); only loopback bolt/neo4j URIs
are accepted. Graphiti's default model/embedding clients separately require their
provider configuration, ordinarily `OPENAI_API_KEY`. Secrets never enter config
examples or journal diagnostics. This CLI does not acquire or print them.

Before actual use, Environment prepares an isolated locked runtime and DevOps
prepares the database under existing authorization. Pin the source SHA, resolved
core dependency graph, database image digest, and selected inference/embedding
models. Do not use `latest`. Initialize graph indices with the official Graphiti
SDK setup procedure and verify models, embedding dimensions and DB independently.
Dependency installation and database provisioning are not performed by the CLI.

Exit 0 is a completed local operation, not global operational readiness. `sync`
returns 1 if any attempted record was not PERSISTED; malformed/config/dependency
failures return 2 and only the exception category. Inspect search warnings even
when exit is zero. Status never claims a live graph probe.

## Recovery and limits

Back up the private journal and graph together. A journal contains approved source
snapshots and must not be committed or shared as a general diagnostic. Abrupt
shutdown after the SDK writes but before SQLite acknowledgment leaves PROCESSING;
reconcile the exact UUID and graph contents before an authorized operator repairs
that row. UNKNOWN is similarly ambiguous, not automatically retryable. Once all
writers are stopped, an operator can invoke `retry-absent --uuid EPISODE_UUID`
with the same global CLI options. It probes the exact SDK episode UUID and only
returns the local row to QUEUED on confirmed absence; probe failures block recovery.
Existing episodes stay ambiguous and require manual inspection; existence alone
does not certify fully completed extraction. `sync` is a separate explicit step.
Concurrent writer recovery is unsupported. Partial entity writes can still exist
after a failed episode; inspect them before retrying. No automated reset,
retention, deletion propagation, graph backup or retraction workflow is claimed.
Canonical deletions/changes immediately stop affected facts from being returned,
but do not erase their remote graph storage. Disabling this adapter never erases
upstream data. A retraction/forget implementation is required before importing
personal/sensitive data or operating retention-regulated workloads.

The adapter and filesystem checks assume a trusted, quiescent workspace. They do
not defend against concurrent hostile filesystem mutation or compromised Git,
local state, DB, LLM or caller. Ordinary idempotency is tested locally; Graphiti's
behavior after partial remote writes/replay is not homologated. Query instructions
and summaries remain untrusted. LLM extraction may misrepresent source facts;
read canonical sources before technical decisions or spec approval.

## Provenance and verification

Official Graphiti source reviewed: release `v0.31.2`, commit
`d72407dcedac911e1be9fc15b55e8c05a3efcc36`, especially `graphiti_core/graphiti.py`
(`AddEpisodeResults`, `add_episode`, `search`) and MCP source/README for queue and
security limitations. The release MCP package is 1.1.2 but its committed MCP lock
resolves core 0.31.1; do not equate an MCP tag with the SDK version checked here.

- https://github.com/getzep/graphiti/tree/d72407dcedac911e1be9fc15b55e8c05a3efcc36
- https://github.com/getzep/graphiti/blob/d72407dcedac911e1be9fc15b55e8c05a3efcc36/mcp_server/README.md

Run `python -m unittest discover -s tests -p 'test_memory*.py' -v` for local
behavior with an injected provider. These tests do not prove a real Graphiti,
Neo4j, model, host, Windows/macOS, or OpenCode connection. Live integration:
NOT_VALIDATED until the exact configured runtime actually runs.

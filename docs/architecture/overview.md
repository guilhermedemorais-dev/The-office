# The Office V2 architecture

Status: implemented compatibility overlay, subject to executed validation and human acceptance. Source: Dev-workflow commit `af94e8022eaec3e4eedfb4a2a62e13c6b349b9c4`.

The V1 `plugins/` tree remains the canonical compatibility distribution. V2 adds concise sector contracts, source-derived functional skills, metadata indexes, an explicit routing CLI and platform descriptions. It does not replace provider runtimes or promise an autonomous background service. A host executes the plan with its own tools and real agent facilities; producing a plan does not prove those agents ran.

## Boundaries

- Agent: owns a sector outcome and decisions, see `agents/<sector>/AGENT.md`.
- Skill: supplies a selected procedure; dependencies retain mandatory shared rules.
- Tool: executes an operation through the existing CLI/MCP/runtime.
- Library: owns reusable metadata, references and template discovery.
- Task: GitHub Issue, equivalent JSON v2 and external evidence ledger.

The V2 entrypoint reads root AGENTS, selects a bounded route through `scripts/office.py`, then loads only selected skills and mandatory references. The preserved V1 entrypoints remain valid for installed bundles; see ADR-001 for the deliberate compatibility tradeoff. The helper is deterministic local orchestration support, not a replacement LLM engine, new MCP server or simulated agent workforce.

## Preserved interfaces

Execution Contract v2, ten canonical validation sector IDs, Human Task equivalence, skill/execution receipts, REA gateway, provider resolution, tool-state and environment bootstrap retain their existing locations and semantics. Logical agents need not have a one-to-one relationship with those schema sectors: for example, frontend and backend may share the implementation executor; librarian is transversal. New runtime state never belongs in the normative Task contract.

## Extensibility and failure

Register source-derived capabilities in the metadata index and retain their core prerequisites. Validate routes and coverage before use. Missing required references block the affected claim. Optional tool failures use compatible cataloged alternatives; do not delete functionality or mark it verified. Handoffs carry IDs/revision/receipts rather than full source bodies. Revalidation follows material artifact changes.

# Rules audit, THEOFFICE-V2-001

Source main: `af94e8022eaec3e4eedfb4a2a62e13c6b349b9c4`. All 12 top-level canonical skills were inspected at section/capability level; canonical Harness, SDD, UX, implementation, Environment, Product, QA, Security, DevOps, REA and SEO bodies were read in full, together with repository AGENTS, pipeline, platform notes and REA integration/provenance. The global partner skill was read from the active host; the baseline copy is inventoried. Every tracked file is hashed in `v1-inventory.json`. This is a structural and instruction audit, not exhaustive dynamic verification of every third-party tool or every reference claim.

## Invariants to preserve

| Rule family | Canonical source | Migration requirement |
| --- | --- | --- |
| Complete module Task | SDD SKILL, Harness Mandatory Task Governance | Specs/layers/specialists remain microtasks; independent authorization/rollback exception only |
| Normative equivalence | Harness context-routing + SDD template | Human Issue and JSON v2 share revision and normative scope; evidence remains outside normative JSON |
| Execution evidence | Harness harness-execution + skill-execution-contract | Skill read, invocation, output and validation evidence; no assignment-as-execution |
| Sector ownership | Harness context-routing + specialist SKILL bodies | Only owner attests own gate; QA independent; required unresolved sectors block final completion |
| Context | Harness Context Budget + each specialist's activation | Selected SKILL fully read, references purpose-qualified; required source is never silently omitted |
| Reuse | Harness minimal-code-gate + implementation | Existing code/catalog/components searched before abstractions; additive validation, no test weakening |
| Operational consent | Environment state-and-consent + DevOps | Installation/configuration/authentication/execution distinct; target-specific production/destructive gates |
| Findings | Security finding-standard + false-positive-validation | Candidate is not a confirmed vulnerability; external publication has explicit gate |
| Recovery | Harness execution/handoff | Preserve task/revision/checkpoints; bounded rework; unavailable preferred tool triggers evidenced equivalent or blocker |
| REA | REA integration/runtime locks | Preserve mature engine, gateway and licenses; static evidence never described as runtime observation |

## Observed duplication and policy tensions

1. Harness `Mandatory Entry Gate` says non-trivial work must link an Issue, while `Change Complexity Gate` makes Issue optional for TRIVIAL work. Preserve the latter scope boundary; a compact intent/evidence record still applies. Do not make every small edit use full SDD.
2. Every specialist repeats list routing, same-revision equivalence, full skill read, required/conditional/optional source rules and owner limits. This duplication is governance coupling, suitable for a shared policy with explicit routing, not independent modified copies.
3. Studio/SDD describe supervised per-module approvals and no automatic chat creation. This execution has explicit user approval for the full PRD, isolated implementation, branch push and parallel agents. Record that authorization; do not globally remove normal supervision or merge/deploy gates.
4. Harness requires whole-inventory metadata consultation while each specialist requires minimal scoped source loading. These are compatible if inventory metadata is consulted once per relevant state and bodies are loaded only after selection. A metadata-only shared index can prevent repetitive research.
5. README/platform-tools call Windows changes unpublished/local, but actual source main includes PR #50. These are stale publication statements. Historical native test claims remain historical evidence, not current-host certification. New V2 notes must use the commit as provenance.
6. Linux/macOS/Windows catalogs share script paths intentionally. Windows 10 and 11 share a baseline catalog but have different validation evidence. Add separate logical V2 catalogs without copying executables or implying Windows 11 validation.
7. README calls all catalog libraries candidates, while some skill instructions require consultation for every PRD/spec. Preserve compact consulted/N/A records; do not force unrelated library research or install candidates.
8. `SKILL.md` says keep control planes lightweight, yet Harness is 678 lines/38,885 bytes and SDD 523 lines/30,200 bytes. Significant bodies include governance, artifact generation, catalog routing and review. Functional decomposition should follow existing headings/capabilities; line-count splitting alone has no semantic justification.

## Actual reference and runtime risks

- Plugin manifest versions often remain 0.1.0 despite extensive source changes. Pins by Git SHA/hashes are necessary; version fields alone do not identify the baseline content.
- Four tracked `.pyc` artifacts are inherited. They must not become a source-of-truth substitute for Python source or portable support claims.
- Source hashes can prove preservation and section coverage, not behavioral equivalence of decomposed skill execution. Require routing tests plus manual host acceptance.
- External MCPs/providers, renderer/browser binaries and native REA engines remain runtime-dependent. Unit tests do not establish connection/authentication or full target coverage.
- SEO and the optional global partner bundle are real V1 capabilities omitted from the PRD's principal sector list. Keep them available through transversal routing.
- Documentation templates are guidance. Manuals/tutorial captures must come from actual target behavior; no real application UI exists in this instruction/CLI Harness to justify fabricated screenshots.

## Inspection limitations

No user-local machine, unpublished local checkout, Windows 11/macOS host or remote MCP credential was accessed. The audit does not assert that every historical runtime integration is healthy today. Baseline tests supply structural/fixture evidence only. Source-reference body verification beyond the listed reads remains scoped to selected owners during implementation.

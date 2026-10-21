# Canonical compatibility aliases

These are pointers, not replacement schemas. The V1 distribution did not supply a standalone JSON Schema for Execution Contract v2. The template and validation tests remain canonical; do not invent a schema and claim equivalence.

| Contract | Canonical source |
| --- | --- |
| Execution Contract v2 template | `plugins/sdd-spec-factory/templates/execution-contract-template.json` |
| Human Task template | `plugins/sdd-spec-factory/templates/task-template.md` |
| Context/sector/list semantics | `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/context-routing.md` |
| Skill and execution receipts | `plugins/dev-workflow-standard/skills/dev-workflow-standard/references/skill-execution-contract.md` |
| Execution report | `plugins/dev-implementation-standard/templates/execution-report-template.md` |
| Execution comment | `plugins/dev-implementation-standard/templates/execution-report-comment-template.md` |
| Compatibility regression | `tests/test_task_contract_v2.py`, `tests/test_sector_context_routing.py` |

V2 agent names are routing metadata; they do not replace the existing ten sector IDs or mutable receipt formats. Legacy tasks remain readable; migrate only resumed material work deliberately.

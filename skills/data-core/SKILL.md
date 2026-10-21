---
name: data-core
description: "Design or validate data models, migrations, queries and concurrency constraints."
---

# data-core

Local V2 capability addition. Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT. Read the routed JSON, required sources with purpose and current revision before work; return SKILL_RECEIPT and your own evidence.

Inspect actual schemas, migrations, database/runtime versions and existing transactions before changes. Identify invariants, uniqueness, ownership, isolation and concurrency boundaries. Reuse repository migration and query conventions. Plan negative cases, rollback and recovery; route product implementation through the selected executor. A production migration or destructive operation requires its explicit target-specific gate. Return schema/query evidence and executed validation, never infer data integrity from lint success.

Load these canonical references only when their domain is active:
- `plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-data-concurrency.md`

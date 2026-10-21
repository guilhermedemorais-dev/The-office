# The Office V2

This checkout is the canonical V2 bundle, not a running agent server. Read
`docs/specs/the-office-v2.md` and the active Task JSON for material work.

1. Inspect branch, remote and working tree. Preserve approved scope and human gates.
2. First apply `docs/operations/v2-execution-policy.md`, including its bounded
   TRIVIAL exception and material-decision procedure. Then start with `agents/orchestrator/AGENT.md`; read the chosen sector's AGENT.md.
3. Use `python scripts/office.py plan <sector>` to inspect capability IDs. Select
   necessary capabilities with repeated `--capability <id>`. A core-only plan
   with candidates is incomplete. Read every selected SKILL.md fully, then its
   active mandatory references, before acting. Record actual skill receipts.
4. V2 functional skills live in `skills/`; their original source sections and
   hashes live in `library/indexes/skill-routes.json`. Relative legacy references
   resolve against the explicit `reference_base` in the original plugin bundle.
   A missing reference blocks the affected claim. Never read the whole legacy
   SKILL.md solely to resolve a referenced file, unless legacy mode is selected.
5. Shared lookup: `python scripts/office.py search '<need>'`. Consult Task-selected
   resources and project/local metadata first (`--index` in priority order).
   Read selected resources only. On gaps follow `agents/librarian/AGENT.md` and
   canonical research registries; no automatic install or unknown-code execution.
6. Keep GitHub Issue = Human Task, JSON v2 = equivalent normative instructions,
   comments/receipts = mutable evidence. Preserve the ten canonical sector IDs;
   logical V2 agents may share executors. One Task per functional module.
7. Handoff plans do not prove execution, equivalence, approval or dependencies.
   Verify current Issue/contract revision and owner receipts before execution.
   Never self-certify independent QA or fabricate invocation/validation evidence.
8. Reuse canonical Environment, provider resolver, context retriever, tool-state,
   governance and REA gateway. Read-only V2 adapters do not install or run them.
   Installation, configuration, authentication, availability and verified operation
   remain separate. WSL is Linux. Windows 11/macOS are not natively validated here.
9. Scale process TRIVIAL/NORMAL/COMPLEX using the routed orchestrator skill.
   Task THEOFFICE-V2-001 already has owner-approved scope and autonomy; do not
   restart Discovery. Other tasks retain their actual authorization gates.
10. Never merge or deploy without explicit separate authorization.

## Compatibility

The 12 original `plugins/` bundles and marketplaces remain usable in legacy
mode, without loading all V2 skills as well. V2 uses this root bundle/checkout.
Host registration is distinct from filesystem validity and must be smoke tested
on the actual host. V2 does not launch persistent background agents or servers.

## Validation

```bash
python scripts/build_skill_routes.py --check
python scripts/build_library.py
python -m unittest discover -s tests -v
git diff --check
```

Record commands, exit statuses, limitations and current artifact revision.
Do not declare native OS homologation or token savings without executed evidence.

## Canonical compatibility references

- Product and historical entrypoints: `README.md`.
- Lifecycle: `docs/workflow-pipeline.md`.
- Original orchestration: `plugins/dev-workflow-standard/skills/dev-workflow-standard/SKILL.md`.
- Provenance: `docs/engineering-harness-audit.md`.
- Operations owner: `devops-standard`, distinct from Environment and Security.
- A missing runtime integration is NOT VALIDATED, never an inferred PASS.

## Stack CLI discovery

For technology work, the responsible sector checks existing project tools and
`library/tools/stack-clis.json` before manual scaffolding or new tool code. Read
`library/tools/stack-cli-policy.md` for selected CLI discovery/installation. Consult
official docs for gaps/version changes; preserve PRD/stack and reuse the project's
manager. Necessary selected project-local installations are owner-authorized;
Environment executes under existing host gates and records verification. Catalog
presence never triggers bulk install or proves operational readiness.

## Consolidated V2 procedures

For material technical decisions use `library/architecture/technical-decision-procedure.md`.
UX selects `apple-hig-designer` only when the approved design direction calls for it.
For repetitive code, reuse project/native generators first, then the Plop fallback
in `library/templates/codegen/README.md`; never impose its template on every stack.

## Delivery closure

Apply `docs/operations/delivery-lifecycle.md` at each Task checkpoint/closure.
Route technical and usability documentation assessment to `documentation-core`,
then verified progress/client reporting to Governance's `delivery-metrics`.
TRIVIAL retains a compact inline outcome. Skills are agent protocols, not running
hooks. Preserve one Task per module, JSON v2 and explicit human release gates.

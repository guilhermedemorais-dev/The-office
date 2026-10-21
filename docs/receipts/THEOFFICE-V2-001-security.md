# THEOFFICE-V2-001 bounded independent security receipt

Date: 2026-10-16. Contract revision: 1. List: `MT-13/checklist`. Owner: `security-standard`.
Mode: change/scoped review. Risk: MEDIUM (local metadata parsers and filesystem boundaries).
`SECURITY_STATUS: PASS` for the bounded changed helper/manifests scope after final revalidation below. No confirmed exploitable vulnerability, no final human acceptance, no production approval. Historical PARTIAL checkpoints are retained below for traceability.

## Authority and skill receipt

User explicitly authorized local construction and validation, isolated branch publication, no merge/deploy. Review delegated by Harness; reviewer owns only this receipt and applied no fixes or commits. Original `security-standard/SKILL.md` read fully, SHA-256 `da2e3fd55998735ba1a641a968610d13514998dee43e1a40f49ca669d50616cb`. Active references read fully: review-pipeline, finding-standard, false-positive-validation, coverage-model, report-template, stack-profiles. Also read root AGENTS, global strategic skill, canonical context-routing, approved module spec and selected security JSON list/global constraints. No live scanner/advisory service was needed for these dependency-free Python changes; no dependency vulnerability claim is made.

At initial review no current THEOFFICE Harness comparison receipt or Backend dependency receipt was available. Bounded code/fixture review continued; final execution gate is not claimed closed. Harness must reconcile current Issue/JSON equivalence, revision, Issue update timestamp and dependency evidence before final validation.

## Scope and threat summary

Reviewed: `scripts/office.py`, `scripts/build_library.py`, `scripts/build_skill_routes.py`, `environment/shared/platform_catalog.py`, `integrations/reverse-engineering/adapter.py`, root `plugin.json`, `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json` and preserved marketplace registration. Source hashes of reviewed versions:

| File | SHA-256 |
| --- | --- |
| scripts/office.py | 68dad9c6cab268a18a5fd60c387d54867554a711fae4c1f304525efd5f474277 |
| scripts/build_library.py | e0ba1019810ef6d75aeb478e9d7d5e28c2dc92b4acdfbd92b4de9c05ae3f2a69 |
| scripts/build_skill_routes.py | d4d6075a6ca27bfea40087ced24fa3bc8618446ee07b9e363036a58df3cf8dda |
| environment/shared/platform_catalog.py | 28d17faafacccf1dfb4eb29b8afa01dc21064ffd63c1cad47723f9e964d34bf2 |
| integrations/reverse-engineering/adapter.py | 1ef59a35d0793f736c583674e279f32fb324116f7141fe8993c692e4430dd64c |

Assets: private checkout/runtime state, catalog integrity, accurate routing and evidence. Inputs: explicitly selected local indexes, catalog paths, contract IDs/revisions, repository symlinks. Actor: local CLI caller and potentially untrusted project/catalog contributors. CLI runs with the caller's existing filesystem permissions, not as an elevated service. Hashes detect drift relative to metadata, not authentic publisher signatures. No network listener, account/session boundary, database or product UI is introduced.

## Coverage ledger

| Surface | Layer | Status | Evidence / boundary |
| --- | --- | --- | --- |
| Catalog resource paths | API/Backend | REVIEWED | Canonical resolve confines traversal/outside symlinks; two narrow hardening gaps below |
| Handoff and capability plans | API/Backend | REVIEWED | Plans explicitly do not execute or authorize work; bad revision, unknown/cyclic skill IDs rejected; additional validator gaps exposed by QA tests |
| Environment observations | Infra/DevOps | REVIEWED | File presence and shutil.which do not set AVAILABLE, INSTALLED, AUTHENTICATED or VERIFIED true |
| REA inventory/routing | Dependencias/Supply Chain | REVIEWED | Pinned original package checked, tarball confined to plugin, no bootstrap/target execution performed |
| Generators and host manifests | Dependencias/Supply Chain | REVIEWED | Only fixed git rev-parse subprocess in skill builder, no shell; manifests add no executable startup hooks |
| Secrets / private data | Privacidade/Observabilidade | REVIEWED | Synthetic path fixtures only; no real credentials inspected; metadata extraction caveat below |
| Database/auth/UI | Banco; Frontend/UI | NOT_APPLICABLE | No new DB, server authentication or frontend |
| Native hosts/providers, V1 engine internals | Infra/DevOps; Supply Chain | DEFERRED | Not in bounded new-code review; no live provider or native Windows/macOS validation claimed |

## Findings and counterevidence

Confirmed security vulnerability count: 0. The following reproducible defects remain INFO hardening/correctness observations, not published vulnerability findings: independent hostile privilege boundary and a secret-bearing deployment path were not established. Reported promptly to Harness for repair.

**INFO-PATH-1: private path checks use unresolved spelling.** `safe_path` rejects literal `.git/config`, runtime-state, `.env` and key suffixes and rejects symlinks escaping root. However, a synthetic `alias.md -> root/.git/config` passes because private component checks inspect caller spelling. Reproduction returned `.git/config`. It does not directly disclose a real secret: resource reads additionally require matching index SHA, and local actors capable of altering this checkout already have same-user access. Recommend private checks on resolved repository-relative components too. No arbitrary command execution or remote exploit claimed.

**INFO-PATH-2: metadata builder follows symlinked source outside root.** A synthetic `plugins/p/skills/p/references/external.md -> outside.md` whose body is `# SYNTHETIC_PRIVATE_TITLE` causes `build_library.build(root)` to return that title in metadata. It does not execute code, transmit data or itself commit/push the resulting index. Operational risk is accidental inclusion of local text in distributed metadata if the index is later published. Recommend refusing out-of-root/private symlink targets before text extraction. Same-user fixture proves local metadata behavior, not an exploitable external service boundary.

**Handoff validator gaps are correctness findings.** At the tested revision `test_v2_adversarial` failed phase, missing checklist, changed microtask owner, required anchor (path and section), and unknown microtask dependency checks. A returned plan remains `PLANNED_NOT_EXECUTED` and lists receipt blockers. Upstream canonical protocol still requires full equivalence/receipt verification; no enforcement bypass into a tool executor was demonstrated. Harness/QA own repair and regression disposition.

## Executed evidence

Runtime: Python 3.12.14, Linux container.

- `python -m unittest discover -s tests -p 'test_v2_*.py' -v`: exit 1, 42 tests, 6 failures in handoff adversarial validation and 36 passes at reviewed hashes. Other agents were editing concurrently; this receipt is bound to hashes above, not subsequent files.
- Safe isolated tempfile Python fixtures importing `office` and `build_library`: exit 0. REJECT results for `../outside.md`, `/tmp/file`, `.git/config`, `runtime-state/tool.json`, `.env`, `.env.local`, `x.pem` and outside-root symlink. Private alias accepted; builder synthetic outside title included. All temporary inputs removed by TemporaryDirectory. No real private files read.

Reproduction of the two INFO observations (run from repository root):

```python
import importlib.util, tempfile
from pathlib import Path

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

office = load("office", "scripts/office.py")
builder = load("builder", "scripts/build_library.py")
with tempfile.TemporaryDirectory() as temporary:
    root = Path(temporary) / "repo"
    root.mkdir()
    (root / ".git").mkdir()
    (root / ".git/config").write_text("SYNTHETIC_PRIVATE_CONFIG")
    (root / "alias.md").symlink_to(root / ".git/config")
    print(office.safe_path(root, "alias.md").relative_to(root))
    outside = Path(temporary) / "outside.md"
    outside.write_text("# SYNTHETIC_PRIVATE_TITLE\n")
    refs = root / "plugins/p/skills/p/references"
    refs.mkdir(parents=True)
    (refs / "external.md").symlink_to(outside)
    print(builder.build(root)["resources"][0]["title"])
```

## Residual risks and gate

Instructional authorization, independent sector receipts, external skill permission/license review and real provider execution remain host/protocol responsibilities. These helpers do not enforce a sandbox or cryptographically authenticate local metadata. Agent instruction compliance and prompt-injection resistance are not proven by unit tests. New arbitrary file/capability contents must remain untrusted until reviewed under the preserved policy. No automatic installation, network call, credential collection, subprocess invocation from catalog values, merge or deploy was found in the bounded helpers.

No human decision is requested by this reviewer. Harness may repair local defects and request bounded retest. Current PARTIAL status reflects missing current gate receipts, six unresolved validation failures and private-path hardening gaps; it must not be interpreted as final Task completion or attestation of other sectors.

## Independent revalidation after Harness repairs

The preceding initial-review findings/results are historical and superseded for current technical disposition by this revalidation. No code fix was applied by this reviewer.

- Read repaired office.py and build_library.py fully. Current `office.py` SHA-256: `e1acdcdd2e6a1d4afea459edbd5f62259998ca00b91627e1fd7e63b93ae5d31d`. Current builder SHA-256: `e0ba1019810ef6d75aeb478e9d7d5e28c2dc92b4acdfbd92b4de9c05ae3f2a69`. Remaining reviewed helper hashes above unchanged. Hash capture and initial review overlapped other agents' edits; these current hashes and executed retest are authoritative for repaired behavior.
- Reran `python -m unittest discover -s tests -p 'test_v2_*.py' -v`: **exit 0, 45 tests, all passed, no skips**, including 16 adversarial and 2 privacy regression cases. This independently covers original six failures plus fenced-example anchor rejection.
- Independently recreated synthetic temp files rather than relying only on the new tests: private alias to `.git/config` now raises ValueError; outside symlink contributes no index record; ordinary `public.md` remains indexed with title `Public fixture`. Fixture script exited 0. INFO-PATH-1 and INFO-PATH-2: **FIXED**, confidence HIGH for these exact local paths. They remain hardening observations and are not reclassified into vulnerability totals.
- Read `THEOFFICE-V2-001-equivalence.json`: revision 1, Issue update `2026-10-16T07:06:13Z`, 58,448-character remote/local equality asserted by Harness. At time of this review its deterministic normative comparison was still marked pending and no Backend owner receipt existed. These are workflow evidence dependencies, not code vulnerabilities.

**Bounded technical result: PASS** for the reviewed new helper/manifests, ready for human review. **Contract execution-gate result: PARTIAL** pending current Harness normative-comparison completion and Backend owner receipt. No unresolved confirmed security finding or reproduced hardening defect remains in reviewed paths. No assertion is made about external REA execution, installed-host behavior, native Windows/macOS, total repository security or other owners' acceptance. Harness must reconcile workflow evidence before marking the required sector/Task complete.

## Final current-revision evidence reconciliation

Current `SECURITY_STATUS: PASS`, contract revision 1, `MT-13/checklist`, bounded changed helper/manifests scope. Earlier PARTIAL workflow state is superseded by this section.

Read current `THEOFFICE-V2-001-implementation.json` and `THEOFFICE-V2-001-documentation.json`. Implementation dependency evidence explicitly covers the local read-only backend helper/adapters and their execution, not independent acceptance or external runtime. Recomputed all six implementation artifact hashes, including task_mirror.py: every value matches its receipt and the reviewed code hashes. Root and delegated executors are identified by their actual session invocation evidence. No new artifact drift was detected.

Read completed Harness `THEOFFICE-V2-001-equivalence.json`. Independently executed `python scripts/task_mirror.py --check`: **exit 0**, LOCAL_MIRROR_MATCH, 29 canonical fields, 58,448 characters, no failures. Independently verified contract and mirror SHA-256 against the completed receipt. Contract: `962b25b7d3c26975db0d03c59d713c70d1274cdf04312794368ee2bf21d2b36a`; mirror: `e53449ae737a64158e8e5eaab79acff9e1c2fadf1c3343ce4a1c2a71cb341c5c`.

Remote Issue equivalence is supplied by Harness's recorded returned GitHub body and update time `2026-10-16T07:06:13Z`; this reviewer did not re-fetch the remote Issue. The local formatter accurately reports that it does not perform remote comparison. Current available owner/dependency and Harness receipts satisfy this bounded review's previously pending evidence gates. Any subsequent material artifact or normative revision requires fresh applicability/hash reconciliation.

Final technical outcome: 45/45 V2 tests passed; both synthetic path defects repaired and independently retested; zero unresolved confirmed security findings in reviewed scope; no remaining security review blocker for the isolated-branch review PR. Full inherited suite and final Harness reconciliation remain their respective owners' evidence. Native host/OS homologation, arbitrary external-provider security, sandbox enforcement and user production approval remain outside this PASS. No merge/deploy authorization is implied. Reviewer modified only this receipt and made no code fix or commit.

## Packaging-only final reconciliation

`SECURITY_STATUS: PASS` remains unchanged for bounded scope. Reviewed final generator/formatter updates: generated skill source chunks are unchanged and followed by a fixed end-of-skill HTML comment; Task presentation rendering removes line-ending whitespace via `rstrip()`, leaving canonical JSON unchanged. These formatting changes introduce no executable input sink, installation, authentication or external side effect.

Independently reran `python scripts/build_skill_routes.py --check`: exit 0, all 41 outputs current. Independently reran `python scripts/task_mirror.py --check`: exit 0, 29 fields, 58,296 characters, no failures. Refreshed implementation hashes all recomputed and matched. Current generator SHA-256: `f4dc3cbc5cb751b1e2e3c6cbb36b709b3b4536b5c2f9db543187b5a7546340e3`. Formatter: `cd60797eb33d91813139b7718ddd09778892ff96b2c2db674eb8c7dcdd4680c1`. Planner, metadata builder, platform and REA adapter hashes remain unchanged from successful security retest.

Current equivalence receipt matches contract SHA `962b25b7d3c26975db0d03c59d713c70d1274cdf04312794368ee2bf21d2b36a` and final mirror SHA `688911070ffce9494cf8f0700c358482b63423ae6bf4a42fa846d4ab0dc14f68`; Harness records exact final GitHub returned-body equality and Issue update `2026-10-16T07:11:40Z`. Remote comparison remains Harness evidence, not an independent remote fetch by this reviewer. Previous mirror character count/hash above is historical and superseded. No full test-suite rerun was necessary for this formatting-only reconciliation; prior 45-test security/V2 run remains bound to unchanged runtime logic. No new unresolved finding or blocker.

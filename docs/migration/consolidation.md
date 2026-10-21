# V2 consolidation, 2026-10-21

Owner correction: changes discussed and implemented in separate revisions must be
integrated in The Office V2, rather than remain an unfulfilled delivery list.
This is implementation under THEOFFICE-V2-001, not a new discovery or permission
request. V1 canonical files stay frozen and verifiable; V2 precedence is explicit.

## Consolidated implementation

- Port the exact V1 technical-decision procedure (local revision 354349c) to
  `library/architecture/technical-decision-procedure.md`.
- Port confirmed TRIVIAL inline execution and scope/recovery rules into
  `docs/operations/v2-execution-policy.md`. Root/sector contracts and generated
  skill adapters reference this actual precedence, including bounded exceptions
  to legacy entry/receipt rules. Existing approved contracts and stricter project
  requirements remain applicable. NORMAL/COMPLEX work keeps its gates.
- Preserve the canonical V1 bundles; generate source slices without changing the
  embedded historical sections. The new V2 policy overrides the specifically
  incompatible legacy process requirements, rather than rewriting their history.
- Add exact Apple-Hig-Designer source ff17b91ff2903ecd52940afabf97de5a73c9cd1b
  as independent optional `apple-hig-designer` capability under UX/ux-design.
  Upstream guide/resources, license and original provenance are byte-preserved.
  Adapter preserves project PRD/tokens/stack and scopes community guidance.
- Port Compose scope guard and its original tests, with the V2 canonical path
  `library/tools/compose-scope.py`. It compares JSON only, never runs Docker.
- Extend shared CLI catalog to 17 records: Tailwind Vite plugin/standalone CLI,
  Plop fallback and local Compose scope guard; React generator selects JavaScript
  `react` or TypeScript `react-ts` according to the project, without implicit major
  upgrades. Nx/OpenTofu and Cloudflare second-audit integration remain available.
- Add a real reusable Plop JavaScript/JSX component starter and project adaptation
  guide. Native/project generators precede it. No invented business module or demo
  application is introduced. Generated files remain project-owned and reviewed.
- Correct Desktop handoff: branch already published, clone from GitHub directly.
  Remove the stale implementation backlog now resolved in this consolidation.
  Qwen Code remains excluded by explicit owner instruction.

## Verification actually executed

- Python 3.12/Linux: `OFFICE_PLOP_BINARY=/tmp/office-plop-validation/node_modules/.bin/plop python -m unittest discover -s tests -v`:
  **705 discovered, 698 passed, 7 native-Windows skips**, 12.657 s, zero failures.
- Includes original Compose adversarial tests, actual HIG alias/selection and hash
  tests, real shared catalog lookup, and real Plop generation in a temporary dir.
- Plop 4.0.5 installed only in the disposable validation prefix with install scripts
  disabled. A real first run found an unsupported API assumption; corrected it and
  reran actual generation, existing-file protection and traversal-name rejection.
  No project/customer host was modified or tool marked operational by metadata.
- `python scripts/build_skill_routes.py --check`: passed.
- `python scripts/verify_preservation.py`: 342 V1 files, zero failures, PASS.
- `git diff --check`: passed before commit.
- A fresh real agent selected procedures for a prose-only typo, a non-Apple web
  review, and Apple macOS design planning. It respected the inline TRIVIAL path,
  excluded HIG from unrelated web work, and selected the guide plus only relevant
  navigation/macOS references for Apple planning. No design implementation or
  runtime review was claimed. The analysis identified upstream compliance/output
  language and example blur/numeric assumptions; the adapter explicitly scopes
  those claims. These are selection acceptance results, not UI homologation.

## Remaining external acceptance

Actual Codex Desktop installation/automatic discovery, native Win10/Win11/macOS,
real product visual/functional acceptance and live optional-provider execution
must be exercised in their actual environments. No percentage token savings,
full end-to-end benchmark or actual target security audit is claimed. The 7 native
skips are visible, not waived as platform passes. Merge/deploy and final owner
acceptance remain separate. The old bundle is historical; use the published PR
branch for current installation/testing.

# Cloudflare security-audit integration

Owner request: add the exact security-audit-skill shown in the screenshot to the Security sector (2026-10-21). This additive capability is part of THEOFFICE-V2-001; no new functional Task, schema migration, merge or deploy is introduced. Existing normative contract revision 1 is unchanged because no existing criterion, sector or permission is replaced. This request supplies explicit authorization for the additional reusable skill.

## Source and architecture decision

- Upstream: https://github.com/cloudflare/security-audit-skill
- Pinned commit: `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8`.
- License: MIT, original Cloudflare copyright retained.
- Complete upstream skill directory and license preserved byte-for-byte in `skills/security-audit/upstream/`, including companion guides, schema, validators and upstream tests.
- Central canonical integration record: `library/skills/external-skills.json`, with per-file SHA-256 and origin/revision.
- Local adapter: `skills/security-audit/SKILL.md`. Generated Security index: `library/indexes/skill-routes.json`.
- Local decision: separate optional capability rather than append all instructions to Security core. Selected skill reads upstream SKILL.md fully; domain guides remain conditional. No upstream procedure was deleted or rewritten.
- The capability keeps existing Security ownership, OSV and publication gates. Guidance and full audit modes remain distinct. Independent agents, sandbox enforcement, coverage and structured validation are required when upstream says so; unavailable capabilities yield incomplete/not validated rather than simulated approval.
- Source provenance fix: route regeneration retains the recorded migration baseline instead of silently adopting a later commit from a sibling V1 working tree.

## Verification performed on Linux

- `python -m unittest discover -s tests -v`: 687 discovered, 680 passed, 7 native-Windows skips.
- `node --test skills/security-audit/upstream/validate-findings.test.cjs skills/security-audit/upstream/validate-coverage-ledger.test.cjs`: 65 passed, zero failed/skipped.
- `python scripts/build_skill_routes.py --check`: passed.
- Skill-creator `quick_validate.py skills/security-audit`: passed.
- `git diff --check`: passed before commit.
- New integration tests verify exact vendored hashes, source pin/license, central metadata hash, relative companion links, selection/prerequisites, exclusion from default loading and rejection by an unrelated sector.

These checks validate packaging, selection and record validators. They do not establish audit effectiveness, target vulnerability absence, native Windows/macOS compatibility, real token savings or host installation. No actual target audit, deployed endpoint probe, container creation or external dependency installation was performed.

## Independent selection acceptance

A fresh agent read the adapter and prerequisites against two bounded requests. For an API authorization explanation without audit/artifacts, it selected guidance mode and returned only a review method. For a full audit on a hypothetical host without independent agents or enforceable isolation, it reported NOT_VALIDATED/incomplete and limited continuation to scoped static analysis and a validation plan. No target code or actual full audit was run.

## Usage

Inspect `python scripts/office.py plan security`, then select explicitly:

```bash
python scripts/office.py plan security --capability security-audit
```

The command returns a plan, not execution. Follow the listed skill and prerequisite reads. For a focused question use guidance mode; for an explicitly requested comprehensive audit use full mode with upstream prerequisites and budget. Guidance may continue read-only where execution sandboxing is unavailable; never claim full independent validation under those conditions.

## Owner decision: second audit

The owner explicitly selected Cloudflare as a second audit, preserving our existing
Security procedure as the first. The adapter and sector contract now order the
reviews, retain separate evidence, prevent initial anchoring on first-pass findings,
and require reconciliation by root cause after independent investigation. Both
passes must identify the reviewed revision/scope. Missing independence or missing
first-pass evidence prevents a completed-second-audit claim. Original upstream
prior-run requirements and full-audit prerequisites remain intact. No target audit
was executed by this configuration change; no new containers or services are added.

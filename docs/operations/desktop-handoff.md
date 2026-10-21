# Desktop handoff, 2026-10-21

Destination: https://github.com/guilhermedemorais-dev/The-office
Branch: `feat/the-office-v2`. No merge or deployment is authorized.

The base V2 was merged through PR #2 (observed during the documentation update):
https://github.com/guilhermedemorais-dev/The-office/pull/2

On Desktop, clone the published branch directly. The earlier bundle is an optional
historical snapshot, not the required transfer path and not the latest revision.

```bash
git clone --branch feat/the-office-v2 https://github.com/guilhermedemorais-dev/The-office.git
cd The-office
python scripts/office.py plan ux-design --capability apple-hig-designer
```

Read `docs/migration/consolidation.md` for the current consolidated changes and
executed verification. Do not merge or deploy as part of the smoke test.

## Current executed checks

Consolidated Linux Python regression: 721 tests discovered, 714 passed, 7 native-Windows skips
(11.206 s), including the real optional Plop runtime. Skill-route generation check and whitespace check passed. Earlier
Cloudflare Node validator suite: 65 passed, not rerun after metadata/doc-only edits.
The worktree was clean before adding this handoff. These are packaging/helper
checks, not completed audits of a target application or proof of token savings.

## Implemented in this V2 branch

Modular V1 overlay, selected skill routing, sector contracts and shared metadata.
Cloudflare security-audit, configured as second audit after our Security review.
Seventeen CLI metadata entries, including Nx and OpenTofu, with a shared procedure
for official documentation research and selected authorized project preparation.
No CLI was installed or infrastructure provisioned merely because it was cataloged.

## Open acceptance items

- Codex Desktop registration/discovery and native Windows execution require smoke
  tests. Follow the installation and user-guide checks on the actual host.
- Native Win10/Win11/macOS, live external providers, visual HIG behavior and full
  owner acceptance remain NOT_VALIDATED unless separately evidenced.
- No end-to-end token savings benchmark or real target application audit exists.
- Qwen Code remains excluded by the owner's decision.

Apple HIG, the decision/complexity/scope procedures, Plop fallback and Tailwind /
React JavaScript recipes are now consolidated; see the dedicated evidence report.
Publication and helper tests do not close the remaining acceptance gaps.

Current docs index: `docs/README.md`. Assisted setup prompt: `docs/operations/installation-prompt.md`.
Documentation/metrics closure evidence: `docs/migration/documentation-delivery.md`.
Portal source preparation was rehearsed in a disposable client fixture only.

The latest manuals on feat/the-office-v2 require their own review after PR #2.
No agent merge/deploy action was performed.

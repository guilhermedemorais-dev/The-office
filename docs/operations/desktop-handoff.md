# Desktop handoff, 2026-10-21

Destination: https://github.com/guilhermedemorais-dev/The-office
Branch: `feat/the-office-v2`. No merge or deployment is authorized.

The web checkout does not automatically appear in Desktop. Transfer the updated
`The-office-v2.bundle` first. In a new directory (do not overwrite a checkout):

```bash
git clone --branch feat/the-office-v2 ./The-office-v2.bundle The-office-v2
git -C The-office-v2 remote set-url origin https://github.com/guilhermedemorais-dev/The-office.git
git -C The-office-v2 status --short --branch
git -C The-office-v2 push -u origin feat/the-office-v2
```

Use an authenticated Desktop Git session. If the remote branch exists and rejects
a non-fast-forward push, fetch and review before resolving; do not force push.
The bundle includes branch history and changes up to this handoff commit.

## Current executed checks

Linux Python regression: 689 tests discovered, 682 passed, 7 native-Windows skips
(8.593 s). Skill-route generation check and whitespace check passed. Earlier
Cloudflare Node validator suite: 65 passed, not rerun after metadata/doc-only edits.
The worktree was clean before adding this handoff. These are packaging/helper
checks, not completed audits of a target application or proof of token savings.

## Implemented in this V2 branch

Modular V1 overlay, selected skill routing, sector contracts and shared metadata.
Cloudflare security-audit, configured as second audit after our Security review.
Thirteen CLI metadata entries, including Nx and OpenTofu, with a shared procedure
for official documentation research and selected authorized project preparation.
No CLI was installed or infrastructure provisioned merely because it was cataloged.

## Open acceptance items

- Remote publication and PR creation remain unconfirmed until Desktop push.
- Codex Desktop registration/discovery and Windows native execution require smoke
  tests. Run the installation/user-guide checks on the actual host.
- Apple-Hig-Designer integration exists in the separate Dev-workflow revision/PR60,
  not this V2 branch. Port it with provenance and selected-skill routing before
  claiming all conversation additions are consolidated in V2.
- Plop was agreed as a fallback concept, not installed or implemented with project
  templates. Tailwind CLI/plugin and a distinct React JavaScript/JSX recipe were
  researched but not yet added to this V2 CLI catalog (current React entry uses
  the react-ts template). Preserve the actual project's JavaScript choice.
- No representative end-to-end token benchmark or current target audit exists.
- Native Win10/Win11/macOS, live external providers and full owner acceptance are
  still NOT_VALIDATED unless separately evidenced.

Publication makes the branch reviewable; it does not close these acceptance gaps.

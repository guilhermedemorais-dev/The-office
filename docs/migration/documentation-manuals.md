# User-facing manuals and Portal preparation evidence

2026-10-21. Parent published V2: f05373381428ecc20d78348212b71af250cc1db0.
Task THEOFFICE-V2-001, existing documentation/install scope, JSON v2 revision 1.

## Documentation delivered

README now starts with current V2 topics, purpose, problems, methodology,
installation guide/prompt, usage, technical documentation/diagram and updating.
Historical content stays intact within a collapsed details section, retaining
legacy anchors and tests; it is explicitly historical rather than current guidance.

`docs/README.md` is the current index. `installation.md` is the Portuguese guide;
`installation-prompt.md` is a separate ready-to-copy agent prompt linked both ways.
`methodology.md`, `tutorial.md`, `updating.md` and `client-portal.md` document the
implemented responsibilities and supported commands. Technical guide maps actual
files/contracts and trade-offs; native SVG flow diagram is included and rendered
for visual inspection. No fake app screenshots or simulated client UI.

Portal preparation rule: responsible sector obtains/pins the source in a separate
tools checkout, reviews the existing script's dry-run and prepares authorized
files at CLIENT_ROOT/docs/portal/, preserves edits and links the project's docs
navigation. Once adopted, reuse installation on later Tasks; no repeated copy.
Backend/auth/deploy are separate and remain project-specific.

## Executed checks

- Portal source: guilhermedemorais-dev/portal-clientes at
  82226fbb2385639d7812b2de929b435e6480fbbc, confirmed checkout hash.
- `node --test scripts/sync-template.test.mjs` in that source: 3 passed, exit 0.
- Actual script dry-run/apply/repeat/customization rehearsal in a disposable Git
  client fixture: 36 files prepared under docs/portal/, 36 unchanged on repeat,
  one client modification preserved; PASS. Evidence JSON alongside receipts.
  Fixture removed afterwards; no real customer files or repository changed.
- Checked 54 relative links in the new README/current manuals: all resolved.
  Historical README links remain the original body and are outside this new-links check.
- Current routes/sample handoff and Environment `--help` inspected. Docs use
  actual supported flags, not a guessed universal installer command.
- `OFFICE_PLOP_BINARY=/tmp/office-plop-validation/node_modules/.bin/plop python -m unittest discover -s tests -v`:
  **721 discovered, 714 passed, 7 native Windows skips**, 10.943 seconds, exit 0.
- `python scripts/build_skill_routes.py --check`: PASS.
- `python scripts/verify_preservation.py`: PASS, 342 frozen V1 files intact.
- `git diff --check`: PASS. SVG rendered using PyMuPDF and visually inspected.

## Truth and limitations

Technical docs and usage docs UPDATED. Runtime claims come from code and executed
local fixtures; the tutorial's example prompts are not claimed product executions.
The setup prompt is an instruction artifact, not an installation already performed.
No customer Portal installation/build, actual backend/API/OAuth, Pages/deploy,
Desktop registration, native Windows/macOS or real token benchmark was executed.
Existing portal dashboard's metric mismatch remains explicitly documented.

Official host documentation consulted:
https://developers.openai.com/plugins/build/plugins (2026-10-21).
This source describes local package/marketplace registration and updating the
active copy; it does not certify this user's Desktop setup. The simplified
root manifest's portable-schema limitations are disclosed in installation.md;
compatible host registration must be validated before claiming installation.

## Owner review path

Read README current topics, then docs/README.md. Copy the installation prompt
into the actual host, follow the guide and record the active revision/real smoke
checks. In a client project that adopts Portal, inspect the pinned template
plan before preparation, confirm docs/portal/ and verify the actual docs link.
Continue only through the project-specific auth/publication gates when required.

## Concurrent repository update

While publishing these manuals, GitHub reported PR #2 merged at 2026-10-21T19:43:35Z
with main at ef948a44288b1d080f142998f3870568620b4638. The agent did not invoke
merge/deploy. This documentation delta requires a new PR; current installation
text now distinguishes merged V2 base from manuals still under review.

# Use and smoke-test the Harness

## Route a small UI correction

```bash
python scripts/office.py plan ux-design
```

Inspect `candidate_capabilities`, then request the needed capability with `--capability <id>` from the actual registry. The result includes core prerequisites, selected files, hashes and `PLANNED_NOT_EXECUTED`. Read every returned file fully. For a responsiveness correction, do not select unrelated research or full design-system methodology. UX validation still needs real target application evidence.

## Reuse a resource

```bash
python scripts/office.py search "OSV"
```

Choose a returned resource ID, then run `python scripts/office.py read <resource-id>`. Search returns metadata; `read` retrieves only the selected body. A stale digest or unavailable reference must not be treated as a current source. Supply project/local metadata explicitly with `--index <file>` when appropriate; private catalogs are not promoted to the shared distribution.

## Route a list and recover

```bash
python scripts/office.py handoff docs/execution/THEOFFICE-V2-001.json --list MT-10/checklist --sector qa --revision 1
```

The output is a handoff plan requiring current Human Task/JSON equivalence and dependency receipts. It does not approve execution or attest PASS. Change revision to an invalid value and expect a blocked result. Resume only after verifying the current revision, artifact hashes, required sources, owner and dependency evidence. Contract changes belong in the Issue and JSON; actual results belong in comments/receipts.

## Manual acceptance checklist

- [ ] Open this checkout in your real Codex host and confirm root V2 instructions are active.
- [ ] Run a minimal route and confirm only selected capability plus mandatory core are loaded.
- [ ] Search a known preserved resource, read it and confirm provenance.
- [ ] Route the QA list above; wrong revision and unknown list must block.
- [ ] Run an authorized small Task in a disposable client-project fixture, preserving Issue/JSON/receipt identity.
- [ ] Remove an optional tool from that fixture's reported availability; confirm a compatible fallback or explicit BLOCKED result, never fake PASS.
- [ ] Review independent QA/security evidence, then request a PR without merge or deploy.
- [ ] Verify actual Linux/Windows/macOS environment catalogs locally and record executed commands; catalog presence alone is not homologation.

No application UI is shipped in this migration. Consequently there are no real product screenshots or GIFs to capture here. Test visual-documentation workflows only against an actual authorized application.

## Aprendizado e metodologia

Para o passo a passo em português use [tutorial](tutorial.md),
[metodologia](methodology.md) e [instalação assistida](installation-prompt.md).
Após cada Task aplique [fechamento](delivery-lifecycle.md). O template fica em
[docs/portal/ do cliente](client-portal.md), não neste Harness.

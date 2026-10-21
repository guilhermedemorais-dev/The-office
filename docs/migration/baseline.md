# Baseline, THEOFFICE-V2-001

Audit date: 2026-10-16.

| Item | Observed evidence |
| --- | --- |
| Origin | https://github.com/guilhermedemorais-dev/Dev-workflow |
| Source branch/revision | main, `af94e8022eaec3e4eedfb4a2a62e13c6b349b9c4` |
| Latest source change | Merge PR #50, platform-tool-routing; includes `92560aa` REA lockfile fix |
| Source working tree | Clean at audit start |
| Source tracked files | 342, hashes in v1-inventory.json |
| Execution OS | Linux kernel 6.18.44 |
| Python | 3.12.14 |
| Node | v24.19.0 |

## Executed baseline

The coordinating agent ran `python -m unittest discover -s tests -v` in the unchanged source checkout. The audit inspected the resulting log at `/workspace/scratch/591ea5883473/baseline.log`.

```text
Ran 638 tests in 8.204s
OK (skipped=7)
```

Result: 631 executed test cases passed, 7 skipped, no failures/errors. This is a V1 baseline, not V2 validation. Skips concern native Windows adapter behavior; native Windows handles/DACL/junction behavior cannot be certified on this Linux host. Node-dependent fixture tests did run in this environment, unlike prior WSL reports with missing Node.

## Prior platform evidence, not reproduced here

README and `docs/platform-tools.md` describe Windows 10 build 19045 native runs with 626 tests and WSL/Linux runs with skips. Existing receipts under `docs/receipts/LOCAL-windows-port-*` provide provenance. These counts are historical and cannot replace the current 638-case baseline. Their 'unpublished' wording is stale relative to the merged current source SHA. Windows 11 and macOS remain NOT_VALIDATED. Linux Mint original use is reported by the maintainer, not newly tested here.

## Not executed by this audit

No target-host plugin install, MCP authentication, external provider model call, live Potpie query, REA runtime bootstrap/binary analysis, SEO live crawl, browser rendering, production deploy, Windows native or macOS tests. Catalog and adapter presence are not proof of operational availability. Full source baseline command output remains the coordinating agent's evidence to copy into the V2 receipt bundle.

## Comparison protocol

Compare V2 against this immutable source, keeping inherited tests intact. Every added/decomposed skill needs section traceability; every new runtime route needs positive/negative validation. For scenario benchmarks record bytes/source counts, elapsed time and calls only when measured. Token input/output/cache metrics are NOT_AVAILABLE unless the host provides actual counters. No percentage token saving is established by this baseline.

## V2 packaging note

Root README/AGENTS are adapted and their original bytes archived. Four tracked
V1 CPython3.11 `.pyc` files are archived in `docs/migration/v1-bytecode/`, rather
than kept as active immutable interpreter caches. The preservation checker still
verifies all342 inventory hashes at their canonical/archive destinations.
`.gitattributes` preserves LF text on Windows; native OS validation remains pending.

# Executed routing microbenchmark

Run `python scripts/benchmark_routes.py` from the checkout. Recorded results are
in `routing-results.json`. Six scenarios executed successfully with repository
fixtures and real file reads. This is not six end-to-end product development
runs. Byte counts include generated skill wrappers and mandatory global/core
skills, but exclude external references, Task context, tool output and LLM calls.

| Scenario | V1 canonical skill bytes | V2 selected skill bytes | Scope |
| --- | ---: | ---: | --- |
| A: trivial visual validation | 30,131 | 24,018 | global + UX visual route |
| B: backend implementation | 31,254 | 29,452 | global + implementation route |
| C: complete module routing | 151,624 | 177,060 | broad multi-sector selection |
| D: library reuse | N/A | N/A | identical metadata results, zero external calls |
| E: missing tool | N/A | N/A | absent-runtime fixture, no VERIFIED claim |
| F: contract change | N/A | N/A | stale revision rejected |

The broad scenario increases context because of added local procedures and
per-skill provenance wrappers. The narrow cases reduce these measured source
bytes. Neither result proves token savings, latency improvement or equal LLM
quality. Input/output/cached tokens are NOT_AVAILABLE; actual product quality,
rework rates and human-intervention counts require comparable end-to-end runs
on the owner's host. No savings percentage is promised.

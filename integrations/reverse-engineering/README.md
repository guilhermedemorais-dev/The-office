# Original REA runtime integration

This cross-sector capability retains the V1 `reverse-engineering-standard`
plugin, canonical gateway, launch adapters, tool registry, MIT notices, pinned
`rea-agents` 4.1.0 tarball and dependency lockfiles without relocation or changes.
REA is the engine, not a replacement prompt. See the original owner's full
`SKILL.md` and `references/rea-integration.md` before execution.

Run metadata inventory (no provider execution or installation):

```bash
python integrations/reverse-engineering/adapter.py
python integrations/reverse-engineering/adapter.py --target-type managed
```

The adapter validates the lock/catalog/package agreement and returns canonical
paths, tarball hash and the smallest matching capability. It does not infer
provider availability from a catalog. The gateway supports `probe`, `catalog`,
`analyze-javascript` and `cli`; its package's historical `call` npm script is not
used because the current gateway implements no `call` action.

After scope/target authorization and scoped runtime preparation through the
original Environment flow, run the returned gateway `probe` command and retain
its actual results. Missing Node >=22.19 or provider dependencies is a blocker
for that route, not permission to install a global engine or silently select a
different provider. No provider bootstrap is performed by the V2 adapter.

JavaScript/Electron/ASAR uses static application analysis; native binaries use
the original native family; .NET uses managed inspection; APK uses Android;
firmware uses region inspection. Optional runtime observation is a distinct
explicit plan with authorization, never represented as static evidence.

Clean-room findings carry OBSERVED, INFERRED and UNKNOWN classifications,
artifact revision/hash and provider/tool evidence into the existing execution
receipt, then SDD, independent implementation and QA. They never authorize
copying proprietary code or changing the approved Task scope.

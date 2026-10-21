# Generate a delivery report

Audience: project owner/Governance. Applies to the read-only V2 calculator in
`scripts/delivery_report.py`. Evidence: `tests/test_delivery_report.py` exercises
JSON, Markdown and Portal output using synthetic projects and content hashes.

1. Inspect the current approved Studio PRD plan, Issue/JSON v2, acceptance
   criteria and owner receipts. Confirm their revisions and approved scope.
2. Copy `library/templates/delivery/snapshot.json` to the **client project's**
   internal evidence directory. It is a DRAFT shape, not an approved real Task.
   Replace every placeholder with source facts; the calculator rejects the draft.
3. Map existing criteria/deliverables to phase IDs and Task IDs. Keep all approved
   work including not started/blocked work. Record documentation's technical and
   user assessments. For each source/evidence file use its SHA-256 hex digest
   (Python `hashlib.sha256(Path(path).read_bytes()).hexdigest()`, or the existing
   project tool). Remote approvals need a current authorized local evidence
   capture and semantic owner review; local hashes do not verify remote truth.
4. Run from the Harness checkout:

```sh
python scripts/delivery_report.py /client/docs/evidence/snapshot.json --root /client --format markdown
python scripts/delivery_report.py /client/docs/evidence/snapshot.json --root /client --format json
python scripts/delivery_report.py /client/docs/evidence/snapshot.json --root /client --format portal
```

Use actual OS-appropriate paths. Commands print to stdout only, with no writes,
network, installation or publication. Save reviewed output in the client docs
using the host's normal authorized file operations. Never overwrite an existing
report without reviewing changes. Link its approved client view in docs navigation.

Expected result: accepted scope percentage per phase and overall, denominator,
blockers/unverified counts, separate documentation status and closure readiness.
The fixture with one accepted and one planned equal-weight criterion yields 50%,
with false closure readiness. Missing time/tokens remain NOT_AVAILABLE. Final
review/merge/deploy and live Portal sync are not inferred from this result.

Errors: `stale evidence` means inspect changed source, reconcile scope/revision
and review the evidence before updating its hash. `missing evidence` means find
or regenerate the real artifact, not fabricate a passing receipt. Invalid path,
ID, status, weight or Issue mapping requires fixing the snapshot against its
source. Unknown denominator produces NOT_AVAILABLE, not a guessed percent.

Portal JSON prepares existing task upsert payloads. Review public titles/stages,
correct configured repository/project and publication approval, then use the
existing authenticated owner API. Verify read-back. The current portal's
`done / eligible` excludes backlog and differs from this scope-unit measurement;
whole-baseline dashboard display requires a separate portal implementation.

Screenshots: NOT_AVAILABLE, this calculator produces CLI text, not a product UI.

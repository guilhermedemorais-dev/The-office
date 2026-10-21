---
name: security-audit
description: "Use Cloudflare security-audit as the second security audit after the existing Security review. Select for the approved audit scope, reconcile independent results afterward, and never run full audits for ordinary development tasks."
---

# Security audit, Security sector capability

Before acting, read repository-root `skills/global-core/SKILL.md` and
`skills/security-core/SKILL.md` fully and include them in SKILL_RECEIPT.
Read [the complete upstream skill](upstream/SKILL.md), then only the companion
files required by its selected mode and target domain. All upstream relative
references resolve inside `upstream/`. Its original files are preserved verbatim.

## Second-audit sequencing

1. Run the existing Security procedure first, retaining OSV and applicable controls.
   Record its source revision, scope, evidence and completion state in the Task.
2. Run Cloudflare as the second audit over the same source revision and approved
   scope. Select its full/guidance mode according to the authorized audit request;
   this sequencing rule does not turn an ordinary task into a full audit.
3. Give a fresh reviewer the scope, source and constraints, without the first
   audit's findings or conclusions during initial investigation. Supply compatible
   prior Cloudflare run ledgers/findings when upstream requires them; preserve
   all upstream verifier independence and budget requirements.
4. Retain separate audit results. After the second investigation, reconcile by
   root cause, deduplicate counts, and explicitly validate disagreements. Preserve
   each audit's evidence and coverage gaps; neither overwrites the other's result.
5. If the source changed, record distinct revisions and revalidate affected claims
   before comparison. If the first audit did not run, do not call this a completed
   second audit. If fresh reviewers or other required capabilities are unavailable,
   record incomplete/NOT_VALIDATED; a sequential reread by the same agent does not
   establish independence. Return the remaining gap to the Security owner.

## Integration contract

- The Security sector owns selection, scope, conclusions and handoff. This skill
  supplies an audit procedure; it does not replace the sector owner or OSV.
- Default to upstream guidance mode for questions, triage and focused reviews.
  Use full mode only for an explicit full audit or report-artifact request.
  Adding/installing this skill does not authorize auditing a target.
- Keep approved PRD/spec/Task scope and the existing publication gates. Never
  publish an unconfirmed candidate as a confirmed vulnerability. Findings JSON
  is an evidence artifact, not a replacement Execution Contract JSON v2.
- Respect the upstream quick/standard/deep profiles and strict invocation budget.
  Do not preload domain companions, create persistent agents or containers, or
  launch a complete audit as routine overhead for an unrelated task.
- Use real host delegation for required independent verification. If unavailable,
  report full-audit independence as NOT_VALIDATED/incomplete; never impersonate
  independent agents. Source guidance may continue within its bounded scope.
- Enforce every upstream OS sandbox control before executing target-controlled
  code. A disposable folder or Docker installation alone proves no isolation.
  If unavailable, retain static analysis and the explicit validation blocker.
- Run the two bundled Node validators only on explicitly selected local audit
  artifacts, with trusted paths and a supported local runtime. They validate
  record structure, not exploitability, coverage truth or absence of vulnerabilities.
- Keep audit run files outside the target unless upstream's explicit ignored-path
  exception applies. No automatic install, deployed endpoint probing or publication.
- Return source revision, selected mode/profile, loaded references, operations,
  validator results, coverage limits and your own SECURITY_STATUS to the Task.

---
name: product-discovery
description: "Use for product discovery: Start from evidence. Load required core skills first."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: product-discovery

Source: `plugins/studio-prd/skills/studio-prd/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, product-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/product-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/studio-prd/skills/studio-prd/`;
for plugin templates/scripts absent there, use repository root `plugins/studio-prd/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

## Reference products and user feedback

When the request uses a reference app, screenshots, an existing workflow or user reviews, read the repository-root [reconstruction procedure](library/reconstruction/README.md). Reuse approved discoveries; map observed behavior separately from proposed and approved requirements. Review evidence-backed complaints before fixing scope when differentiation matters. Keyword themes are research candidates, never proof of sentiment or a validated market trend. Do not activate a competing eleven-stage pipeline or impose a new stack.

Canonical link resolution (repository-relative paths, not skill-directory-relative):
- `references/briefing.md`: `plugins/studio-prd/skills/studio-prd/references/briefing.md`
- `library/reconstruction/README.md`: `library/reconstruction/README.md`

<!-- source-section:studio-prd:001 sha256:cf2a00de3cefd070f715a7832b4d5d151121b1f6d13a6d4015764eaec354cfe3 -->
## Start from evidence

Read existing brief, PRD, decisions, architecture and reference index first.
Confirm the project root and whether this is a new product or an existing
system, including low-code. Preserve established decisions; reopen one only
with a concrete conflict or requested change. Read [briefing.md](references/briefing.md)
for the interview and existing-system inventory.

Use the active Harness selective research routing. Inspect Task-selected and
project evidence, then relevant catalog/index metadata and actual required host
capabilities. For a concrete gap use official, version-matched technical docs or
primary standards. Read the original source, not only a search snippet. Reuse
applicable records; do not scan the whole inventory or repeat settled research.
Never install the whole catalog or claim an unavailable MCP was invoked.

Apply the critical-discovery phases and evidence protocol in
[briefing.md](references/briefing.md). Investigate the problem before endorsing a
solution. Challenge consequential assumptions with reasons, useful alternatives
and a recommendation; do not manufacture disagreement or certainty. Research
technical facts instead of asking the owner to guess them. A recommendation
without sufficient evidence stays PROPOSED/UNKNOWN, never an established fact.

For applicable backend/payments/fiscal/commerce library needs, resolve the active
SDD owner and its references/backend-component-sources.md catalog metadata.
Select eligible free editions only, preserving license obligations and separate
provider/infrastructure costs. Preserve the PRD consultation/selection record; missing or stale evidence remains
NOT_VALIDATED. Do not assume sibling cache paths or select architecture/install packages.

When the user/project declares a Next.js/NestJS preference and stack is undecided,
assess that reference pair through existing catalog IDs, then confirm the PRD.
Preserve approved stacks; do not apply this preference to undeclared projects. Next server/BFF adapters may call
Nest-owned domain APIs; do not duplicate business rules or assume Next cannot run backend code.

Ask at most three useful questions per round. Research what can be discovered
from authorized sources before asking. Separate APPROVED, PROPOSED, UNKNOWN
and EXCLUDED requirements with source and rationale. Reference functionality
is a candidate, never automatic scope. Do not fill business gaps silently.

Use `reverse-engineering-standard` when authorized inspection is needed.
Differentiate visible UI, source implementation and behavior actually tested.
Unknown backend access remains unknown. Reading PHP as a reference does not
choose PHP as the target stack. Do not run unknown software, transmit real
data, delete, migrate or replace a system as part of an interview.

<!-- end of selected V2 skill -->

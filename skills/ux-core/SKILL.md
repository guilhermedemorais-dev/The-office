---
name: ux-core
description: "Use for ux core: Preamble; Ownership; Non-Negotiables; Registry and MCP Policy; Minimal Workflow; Handoff Output. Load required core skills first."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: ux-core

Source: `plugins/ui-ux-standard/skills/ui-ux-standard/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/ui-ux-standard/skills/ui-ux-standard/`;
for plugin templates/scripts absent there, use repository root `plugins/ui-ux-standard/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

Canonical link resolution (repository-relative paths, not skill-directory-relative):
- `../cinematic-web-standard/SKILL.md`: `plugins/ui-ux-standard/skills/cinematic-web-standard/SKILL.md`
- `../cinematic-web-standard/references/dev-workflow-integration.md`: `plugins/ui-ux-standard/skills/cinematic-web-standard/references/dev-workflow-integration.md`

<!-- source-section:ui-ux-standard:000 sha256:5e87b738422aa904bb8df167a99fa9fe00424275c155efc9f225928b38e835bc -->

# UI/UX Standard

Receive one prompt per execution list, linking the Task's single JSON file
and selecting its `execution_lists` entry by `list_id`, never per item/subitem.
All lists live in that file; do not expect JSON inside the Human Task/prompt.
Read the list JSON and relevant canonical JSON fields, not Human Task sections
as execution input. Require current Harness evidence of full card/JSON normative
equivalence, tied to the contract revision and observed Issue update time.
Missing/stale evidence or divergence returns to Harness before execution.

Act as the UI/UX specialist. Read this `SKILL.md` completely before review and
return a `SKILL_RECEIPT`; a mention of the skill is not proof that its
methodology was applied.

Keep this control plane compact. Create only the design docs and artifacts that
are needed for the current task.

<!-- source-section:ui-ux-standard:001 sha256:649b24cf59c843c354f861a884f2b846fa349289a937326a78424d7b05872531 -->
## Ownership

Own:

- design discovery and design-system rules
- component and template discovery before custom UI invention
- mockup-first workflow when visual direction is not already approved
- `docs/design` organization when needed
- visual assets and media prompts
- accessibility, responsiveness, interaction states, and runtime visual QA

Do not own backend architecture, database design, deployment, or final user
approval.

`qa-testing-standard` owns functional flows, form submission, navigation and
duplicate/retry behavior. This skill retains design fidelity, visual hierarchy,
accessibility design, responsiveness and visual runtime QA. Share relevant
evidence without claiming the other owner's PASS. A misaligned button routes
here; a button submitting twice routes to QA; unauthorized action routes to
security-standard. Playwright tool ownership remains here, even when QA uses it.

For sector-routed handoffs, read the list JSON and canonical Execution Contract,
relevant global criteria, REQUIRED sources with purpose and triggered CONDITIONAL
sources. Do not load the Human Task as execution input or OPTIONAL sources by default. Read this
SKILL.md fully and required active-mode references. Resolve context-routing from
the active Harness or explicit canonical checkout; missing required context goes
back to Harness. Planning/design may precede frontend completion; final visual
validation requires the relevant rendered artifact and current revision evidence.
For v2, verify **normative equivalence** and `contract_revision` for the routed
UI/UX slice using the current Harness comparison receipt. Load the exact
Design Guide, tokens, component library, visual references, mockup and sections
named by the contract; divergence blocks a design or validation claim.

For cinematic/scrollytelling, scroll-scrubbed sequences or motion-heavy pages,
select the sibling [Cinematic Web Standard](../cinematic-web-standard/SKILL.md)
and its [integration handoff](../cinematic-web-standard/references/dev-workflow-integration.md).
Use it only when triggered by approved scope. UI/UX remains the design/visual
owner; the cinematic specialist defines scenes, media budgets, reduced motion
and motion/performance evidence. `dev-implementation-standard` implements.
Do not load the cinematic methodology for ordinary UI changes.

<!-- source-section:ui-ux-standard:002 sha256:7d5aa27943bd70c330bf530991be75bde2a31701422b4b75621249c4f0bbbd1a -->
## Non-Negotiables

- Inspect existing UI, routes, components, styling stack, dependencies, design
  docs, and approved references before proposing new UI.
- Treat approved Figma, mockups, screenshots, brand docs, project design files,
  and the project's existing design system as source of truth.
- If design docs and production code conflict materially, stop and surface the
  conflict before redesigning.
- Reuse project components and design tokens before importing or creating new
  ones.
- Before inventing a new visual component, search approved component sources or
  registries when the project stack and task make that practical.
- Do not combine several component libraries merely for visual novelty. Prefer
  one coherent foundation plus narrowly selected specialist components.
- External components are references or implementation candidates, not a new
  design system. Adapt them to the project's tokens, typography, spacing,
  states, accessibility rules, and product context.
- Do not copy a complete third-party product visual identity or proprietary
  template without an applicable license and explicit project justification.
- Review third-party code, dependencies, maintenance status, license, runtime
  cost, accessibility, and compatibility before adoption.
- Do not redesign unrelated surfaces.
- Do not use unlicensed external assets as final assets.
- Frontend/UI is not complete until runtime behavior and visual fidelity are
  checked where practical.

<!-- source-section:ui-ux-standard:004 sha256:dd571ff2f99b5ecee0168d83124494a778350be2cf50bbde872c1da736b7bd34 -->
## Registry and MCP Policy

Own browser, visual, and accessibility tooling through
`references/tool-registry.json`. Follow the shared `skill-owned-tools.md`
protocol: consult ignored per-skill runtime state, use its compatible fast
path, or detect, install from an official supported source when required,
verify, and persist. Revalidate after a failed visual check or fix. A cached
Playwright CLI does not prove browser binaries or the project's runtime are
ready; validate those in the active workspace before claiming coverage.

When a shadcn-compatible project is detected, prefer registry-aware discovery
instead of generating JSX from memory.

- If shadcn MCP is already available, use it to browse and search configured
  registries before installing candidate components.
- If MCP is unavailable, use official documentation, the project's shadcn CLI,
  or public source repositories as discovery fallback.
- Do not silently modify global MCP configuration or install a new global tool.
  Propose that environment change separately when it is actually needed.
- Treat community registries as third-party code. Inspect source and license
  before adoption.
- When `components.json` defines registries, inspect those project-approved
  registries before unrelated public sources.

<!-- source-section:ui-ux-standard:005 sha256:efb4497b01e348beefd3874a2f039c524df69b4d27bf11509705051f2f5227b5 -->
## Minimal Workflow

1. Discover current UI, routes, design system, frontend stack, reusable
   components, and approved visual references.
2. Classify the task: preserve, extend, redesign, or create a new surface.
3. Identify the smallest set of UI patterns and components required.
4. Build `COMPONENT_SOURCE_INVENTORY` using project-native sources first and
   approved external sources second.
5. If visual direction is missing, establish a concise direction or mockup
   before implementation.
6. Define visual acceptance criteria for hierarchy, layout, states,
   responsiveness, accessibility, assets, motion, and interaction behavior.
7. Hand implementation to the main development workflow with exact component
   choices, adaptation notes, and acceptance criteria.
8. Validate rendered output in runtime with Playwright, Browser, Chrome
   DevTools, or the repository's existing test setup when available.
9. Reject visual regressions, generic template assembly, unjustified library
   mixing, and implementation that diverges from the approved design direction.

<!-- source-section:ui-ux-standard:009 sha256:26122437ba3a4459ad25b671fd4ee94093a498e8511f7825602c4b93e56dcd11 -->
## Handoff Output

Return concise handoff data:

- `SKILL_RECEIPT`
- mockup/design reference path
- changed design docs or tokens
- `COMPONENT_SOURCE_INVENTORY`
- selected component/library/template sources and adaptation notes
- assets/media prompt status
- visual acceptance criteria
- runtime validation evidence
- unresolved decisions
<!-- end of selected V2 skill -->

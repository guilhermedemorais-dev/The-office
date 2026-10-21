# Lossless V1 to V2 skill migration

This is a local functional migration, not a replacement execution engine. Original V1 resources remain preserved at canonical paths or explicit byte-identical archives. Studio PRD evolves under approved STUDIO-PRD-002 / ADR 006; its current slices cover the evolved canonical source, while the original remains in docs/migration/v1-frozen/. The vendored REA skill stays with its upstream runtime; it is not split or rewritten.

Each V1 body section is assigned once. Registry offsets are 1-based inclusive and SHA-256 hashes cover exact UTF-8 text. Frontmatter remains in the canonical source and is covered by the full source hash. Generated skills contain source text verbatim after an explicit reference-base adapter. Regenerate with `python scripts/build_skill_routes.py`; validate with `python scripts/build_skill_routes.py --check`.

Select global core, relevant sector core, and only capabilities required by the Task. A selected capability depends on its core. Explicit IDs take priority over lexical trigger hints; ambiguous matching must be resolved from Task scope, not treated as authorization. Shared executor aliases do not create duplicate skills.

Full behavioral parity across arbitrary agent hosts is NOT VALIDATED. Exact text coverage proves no section was dropped; it does not prove all models follow the instructions, nor tokens saved. SDD task-contract generation and implementation workflow remain deliberately cohesive and relatively large to preserve coupled gates. Legacy bundles continue loading their original monolithic SKILL.md, so selective-loading gains require the V2 router.

| V1 source | Section and original lines | V2 skill |
| --- | --- | --- |
| `dev-workflow-standard` | Preamble (5–17) | `orchestrator-core` |
| `dev-workflow-standard` | Mission (18–31) | `orchestrator-core` |
| `dev-workflow-standard` | Harness Contract (32–78) | `orchestrator-core` |
| `dev-workflow-standard` | Mandatory Entry Gate (79–99) | `orchestrator-core` |
| `dev-workflow-standard` | Hard Limits (non-negotiable) (100–126) | `orchestrator-core` |
| `dev-workflow-standard` | Skill Roles (who does what) (127–142) | `orchestrator-core` |
| `dev-workflow-standard` | Practice Provenance (143–160) | `orchestrator-core` |
| `dev-workflow-standard` | Task And Execution Context (161–196) | `orchestrator-core` |
| `dev-workflow-standard` | Change Complexity Gate (197–217) | `orchestrator-core` |
| `dev-workflow-standard` | Mandatory Flow (218–269) | `orchestrator-discovery` |
| `dev-workflow-standard` | Mandatory Task Governance (270–376) | `orchestrator-task-governance` |
| `dev-workflow-standard` | Official Kanban Method (377–404) | `orchestrator-task-governance` |
| `dev-workflow-standard` | Definition of Entry / Exit (405–425) | `orchestrator-task-governance` |
| `dev-workflow-standard` | Repository Readiness Bootstrap (426–455) | `orchestrator-task-governance` |
| `dev-workflow-standard` | GitHub-Ready Task Structure (456–468) | `orchestrator-task-governance` |
| `dev-workflow-standard` | Recommended Task Template (469–477) | `orchestrator-task-governance` |
| `dev-workflow-standard` | Delegation Rules (478–518) | `orchestrator-delegation` |
| `dev-workflow-standard` | When to Trigger Each Specialist (519–576) | `orchestrator-delegation` |
| `dev-workflow-standard` | Review Rules (577–606) | `orchestrator-review` |
| `dev-workflow-standard` | Context Budget Rules (607–642) | `orchestrator-core` |
| `dev-workflow-standard` | Reference Routing (643–678) | `orchestrator-delegation` |
| `ui-ux-standard` | Preamble (5–22) | `ux-core` |
| `ui-ux-standard` | Ownership (23–55) | `ux-core` |
| `ui-ux-standard` | Non-Negotiables (56–81) | `ux-core` |
| `ui-ux-standard` | Component Intelligence (82–159) | `ux-components` |
| `ui-ux-standard` | Registry and MCP Policy (160–183) | `ux-core` |
| `ui-ux-standard` | Minimal Workflow (184–202) | `ux-core` |
| `ui-ux-standard` | Default Design Structure (203–229) | `ux-design-system` |
| `ui-ux-standard` | Visual Quality Gate (230–246) | `ux-visual-validation` |
| `ui-ux-standard` | Visual QA Checklist (247–263) | `ux-visual-validation` |
| `ui-ux-standard` | Handoff Output (264–276) | `ux-core` |
| `sdd-spec-factory` | Preamble (5–28) | `sdd-core` |
| `sdd-spec-factory` | Mission (29–53) | `sdd-core` |
| `sdd-spec-factory` | Vocabulary (non-negotiable) (54–70) | `sdd-core` |
| `sdd-spec-factory` | Mandatory hierarchy (71–90) | `sdd-core` |
| `sdd-spec-factory` | Mandatory separation of concerns (91–106) | `sdd-core` |
| `sdd-spec-factory` | Operating principles (107–140) | `sdd-core` |
| `sdd-spec-factory` | Consultative Technical Knowledge Routing (141–158) | `sdd-specifications` |
| `sdd-spec-factory` | Phases (159–160) | `sdd-discovery` |
| `sdd-spec-factory` | Studio PRD handoff (161–184) | `sdd-discovery` |
| `sdd-spec-factory` | Fase 0 - Diagnóstico (185–196) | `sdd-discovery` |
| `sdd-spec-factory` | Fase 1 - Consolidação (197–219) | `sdd-discovery` |
| `sdd-spec-factory` | Fase 2 - Geração de Specs (220–298) | `sdd-specifications` |
| `sdd-spec-factory` | Fase 3 - Geração de Task Executável (299–474) | `sdd-task-contracts` |
| `sdd-spec-factory` | Fase 4 - Checklist de PR/QA (475–487) | `sdd-review` |
| `sdd-spec-factory` | Integration with the other plugins (488–506) | `sdd-core` |
| `sdd-spec-factory` | Definition of done for this skill (507–523) | `sdd-core` |
| `dev-implementation-standard` | Preamble (5–22) | `implementation-core` |
| `dev-implementation-standard` | Mission (23–36) | `implementation-core` |
| `dev-implementation-standard` | Preconditions (do not start without these) (37–55) | `implementation-core` |
| `dev-implementation-standard` | Hard Limits (non-negotiable) (56–70) | `implementation-core` |
| `dev-implementation-standard` | Task Status Rules (71–82) | `implementation-delivery` |
| `dev-implementation-standard` | Workflow (83–163) | `implementation-core` |
| `dev-implementation-standard` | Frontend design sources (164–177) | `implementation-frontend` |
| `dev-implementation-standard` | GitHub Projects Readiness (178–195) | `implementation-delivery` |
| `dev-implementation-standard` | Recommended Task Template (196–204) | `implementation-delivery` |
| `dev-implementation-standard` | Escalation (205–220) | `implementation-core` |
| `dev-implementation-standard` | Interfaces with other skills (221–240) | `implementation-core` |
| `dev-implementation-standard` | Definition of done (241–255) | `implementation-core` |
| `dev-environment-standard` | Preamble (5–20) | `environment-core` |
| `dev-environment-standard` | Choose the operation (21–38) | `environment-bootstrap` |
| `dev-environment-standard` | Bootstrap loop (39–81) | `environment-bootstrap` |
| `dev-environment-standard` | Platform routing (82–99) | `environment-platform-state` |
| `dev-environment-standard` | Library, ownership and local state (100–128) | `environment-platform-state` |
| `dev-environment-standard` | Preparation authority (129–142) | `environment-core` |
| `dev-environment-standard` | Health and handoff (143–154) | `environment-platform-state` |
| `dev-environment-standard` | Scope and security (155–169) | `environment-core` |
| `devops-standard` | Preamble (5–23) | `devops-core` |
| `devops-standard` | Responsibility boundaries (24–56) | `devops-core` |
| `devops-standard` | Operational contract (57–86) | `devops-operations` |
| `devops-standard` | Human safety gates (87–101) | `devops-core` |
| `devops-standard` | Progressive domain routing (102–135) | `devops-operations` |
| `devops-standard` | Evidence handoff (136–157) | `devops-core` |
| `qa-testing-standard` | Preamble (5–19) | `qa-core` |
| `qa-testing-standard` | Context and activation (20–50) | `qa-core` |
| `qa-testing-standard` | Modes and phases (51–75) | `qa-validation` |
| `qa-testing-standard` | Execution and ownership (76–99) | `qa-core` |
| `qa-testing-standard` | Shared tools, not duplicated ownership (100–120) | `qa-validation` |
| `qa-testing-standard` | Evidence gate (121–170) | `qa-validation` |
| `qa-testing-standard` | Provenance (171–176) | `qa-core` |
| `security-standard` | Preamble (5–35) | `security-core` |
| `security-standard` | Scope And Safety (36–52) | `security-core` |
| `security-standard` | Relationship To The Main Workflow (53–88) | `security-core` |
| `security-standard` | Review Modes (89–134) | `security-review` |
| `security-standard` | Risk-Adaptive Depth (135–150) | `security-review` |
| `security-standard` | Security Workflow (151–287) | `security-review` |
| `security-standard` | Tool Policy (288–322) | `security-tools-reporting` |
| `security-standard` | External Publication Gate (323–347) | `security-core` |
| `security-standard` | Evidence And Reporting (348–393) | `security-tools-reporting` |
| `security-standard` | Completion Rules (394–405) | `security-core` |
| `security-standard` | Handoff To Dev Workflow (406–416) | `security-core` |
| `studio-prd` | Preamble (5–12) | `product-core` |
| `studio-prd` | Start from evidence (13–56) | `product-discovery` |
| `studio-prd` | Produce the project artifacts (57–87) | `product-planning` |
| `studio-prd` | Plan and hand off under supervision (88–144) | `product-planning` |
| `studio-prd` | Evidence and continuation (145–157) | `product-core` |
| `reverse-engineering-standard` | Preamble (5–18) | `reverse-engineering-core` |
| `reverse-engineering-standard` | Preconditions (19–30) | `reverse-engineering-core` |
| `reverse-engineering-standard` | Workflow (31–49) | `reverse-engineering-investigation` |
| `reverse-engineering-standard` | Safety and legal boundary (50–66) | `reverse-engineering-core` |
| `reverse-engineering-standard` | Relationship with other skills (67–76) | `reverse-engineering-core` |
| `seo-standard` | Preamble (5–16) | `seo-core` |
| `seo-standard` | Preconditions (17–24) | `seo-core` |
| `seo-standard` | Workflow (25–35) | `seo-site-analysis` |
| `seo-standard` | Commercial site standard (36–53) | `seo-site-analysis` |
| `seo-standard` | Ownership boundaries (54–64) | `seo-core` |
| `parceiro-estrategico-global` | Preamble (5–7) | `global-core` |
| `parceiro-estrategico-global` | Papel e responsabilidade (8–15) | `global-core` |
| `parceiro-estrategico-global` | Estilo obrigatório (16–27) | `global-core` |
| `parceiro-estrategico-global` | Formato padrão (28–39) | `global-core` |
| `parceiro-estrategico-global` | Classificação da demanda (40–49) | `global-core` |
| `parceiro-estrategico-global` | Descoberta adaptativa (50–75) | `global-discovery` |
| `parceiro-estrategico-global` | Comando `SemPerguntas` (76–86) | `global-discovery` |
| `parceiro-estrategico-global` | Briefing estruturado (87–107) | `global-discovery` |
| `parceiro-estrategico-global` | Tecnologia e software (108–119) | `global-discovery` |
| `parceiro-estrategico-global` | Marketing (120–142) | `global-marketing-sales` |
| `parceiro-estrategico-global` | Vendas (143–166) | `global-marketing-sales` |
| `parceiro-estrategico-global` | Verificação e precisão (167–180) | `global-core` |
| `parceiro-estrategico-global` | Práticas consolidadas antes de extensões locais (181–209) | `global-core` |
| `parceiro-estrategico-global` | Execução (210–223) | `global-core` |
| `parceiro-estrategico-global` | Descoberta e roteamento dinâmico de capacidades (224–252) | `global-core` |
| `parceiro-estrategico-global` | Modos especiais (253–261) | `global-core` |
| `parceiro-estrategico-global` | Missão (262–264) | `global-core` |

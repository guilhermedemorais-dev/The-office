# Studio PRD e guia visual vivo

## Requisitos

### REQ-01

Studio PRD conduz briefing adaptativo com até três perguntas, pesquisa prévia, atores/jornadas/regras e inventário autorizado de software existente; sugestões não são requisitos aprovados.

### REQ-02

PRD explicita quantidade, IDs e limites dos módulos; uma task completa por módulo, sem fragmentar por camada, especialista ou tokens; sem redução automática a MVP.

### REQ-03

Planejamento interno separado em MD e JSON com mesma revisão e decisões, etapas, urgência versus dependências, esforço versus calendário, recursos, riscos, capacidade e incerteza explícita.

### REQ-04

Cada task no plano possui prompt curto específico com links reais; contrato inexistente indica especificação, não implementação. SDD mantém template completo e JSON equivalente; aguarda autorização por módulo.

### REQ-05

Guia visual vivo no projeto atendido: Markdown, HTML navegável, tokens e fontes, componentes identificados por revisão, estados e fixtures rotuladas; catálogo não prova backend pronto.

### REQ-06

Harness, SDD, UI, implementação e QA compartilham roteamento e gates; comentários da Issue registram evidência, superfícies e tokens apenas medidos.

### REQ-07

Adicionar plugin nos marketplaces, atualizar README/pipeline, incorporar correção de metadata/runtime existente, preservar credenciais e verificar instalação separadamente do carregamento.

### REQ-08

Portal somente regras já existentes de fonte externa para docs/portal; não construir portal, hospedar, configurar banco ou publicar dados privados.

## Limites de validação

Testes estruturais e revisão de cenários não garantem comportamento de toda LLM futura. Instalação, descoberta na nova sessão e autenticação de MCP são verificações diferentes.


## Approved strategic discovery evolution, 2026-10-21

REQ-09: debate problem/solution assumptions, alternatives and contradictions before
consolidation; retain one canonical Studio owner and generated V2 slices.
REQ-10: explicit product diagnosis/debate/PRD phases, distinct from SDD phases;
critical blockers prevent false completion, not independent work or honest drafts.
REQ-11: technical recommendations require applicable evidence or explicit unknown,
version-matched primary docs for gaps, rationale/trade-offs and traceable sources.
REQ-12: separate evidence nature from approval state in existing tables; approved
hypothesis stays hypothesis. No new normative execution schema or memory store.
REQ-13: conceptual Data/Backend/UI triage only when relevant; details stay with
Architecture/SDD/UX. No product code, install, build, deploy or operational mutation.
REQ-14: preserve original frozen files by exact archives with immutable baseline
hashes and explicit migration mapping; test archive and evolved source separately.

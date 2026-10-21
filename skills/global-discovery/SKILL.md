---
name: global-discovery
description: "Use for global discovery: Descoberta adaptativa; Comando `SemPerguntas`; Briefing estruturado; Tecnologia e software. Load required core skills first."
---

V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.

# The Office V2: global-discovery

Source: `plugins/parceiro-estrategico-global/skills/parceiro-estrategico-global/SKILL.md`. Read this selected skill in full and emit SKILL_RECEIPT.
Required skill IDs: global-core, global-core.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT.
The exact source sections follow unchanged. In those sections, “this SKILL”
means this selected V2 skill plus its required core, not the entire V1 control plane.
Resolve original relative references and backticked resource paths from repository root `plugins/parceiro-estrategico-global/skills/parceiro-estrategico-global/`;
for plugin templates/scripts absent there, use repository root `plugins/parceiro-estrategico-global/`.
Never resolve inherited relative paths against this generated directory.
Load only the references whose conditions hold; retain all explicit mandatory gates.

<!-- source-section:parceiro-estrategico-global:005 sha256:10c440a108882abaa5181067acdbb3a163577b552b348bb4182b5169cdba8fe5 -->
## Descoberta adaptativa

Para demandas complexas, não avançar imediatamente para planejamento ou execução. Primeiro, compreender exatamente onde o usuário quer chegar.

Aceitar contexto por texto, áudio transcrito, imagem, captura de tela, arquivo, link, exemplo, ideia incompleta ou conversa iniciada do zero. Não perguntar previamente em qual formato as informações serão fornecidas. Analisar o material recebido e começar pelo que já estiver disponível.

Durante a descoberta:

- Extrair e preservar todas as informações fornecidas.
- Identificar problema real, objetivo e resultado esperado.
- Separar fatos, hipóteses, preferências, restrições e decisões pendentes.
- Detectar lacunas, ambiguidades, contradições, dependências e riscos.
- Não repetir perguntas já respondidas no contexto acessível.
- Não aplicar questionário genérico ou sequência fixa.
- Fazer preferencialmente uma pergunta por rodada.
- Escolher a próxima pergunta com base na resposta anterior.
- Priorizar perguntas capazes de alterar objetivo, escopo, estratégia, custo, prazo, arquitetura, segurança, qualidade ou critério de sucesso.
- Agrupar no máximo três perguntas quando forem independentes e isso reduzir retrabalho.
- Apresentar alternativas concretas quando o usuário não conhecer as opções ou quando existir uma decisão relevante.
- Explicar consequências e recomendar um caminho, sem transferir toda a decisão ao usuário.
- Fazer suposições apenas quando forem seguras, reversíveis e declaradas.
- Não transformar detalhes secundários em bloqueios.
- Continuar investigando enquanto existirem lacunas capazes de alterar materialmente o resultado.

Não produzir plano definitivo enquanto o problema estiver mal definido.

<!-- source-section:parceiro-estrategico-global:006 sha256:f5083b42b539846e60b43bdb0616865e703a93079c1e8615531324b725f3d198 -->
## Comando `SemPerguntas`

Quando o usuário escrever `SemPerguntas`:

- Não conduzir entrevista de descoberta.
- Adotar no máximo duas hipóteses necessárias.
- Declarar as hipóteses.
- Identificar os riscos gerados pela falta de informação.
- Prosseguir com a melhor solução possível.
- Nunca inventar silenciosamente contexto que somente o usuário poderia fornecer.

<!-- source-section:parceiro-estrategico-global:007 sha256:c1710681193ec4c9680551c12e0bb9d61526d9ba7e009a54063fb81d828023aa -->
## Briefing estruturado

Quando houver contexto suficiente, consolidar:

1. Contexto.
2. Problema ou oportunidade.
3. Objetivo principal.
4. Resultado esperado.
5. Público, usuários ou envolvidos.
6. Escopo preliminar.
7. Restrições e prioridades.
8. Necessidades identificadas.
9. Decisões já tomadas.
10. Riscos e dependências.
11. Dúvidas pendentes.
12. Suposições adotadas.
13. Critérios de sucesso e aprovação.
14. Próxima etapa recomendada.

Não inventar conteúdo para preencher campos. Marcar o que permanecer indefinido. Apresentar o briefing para correção ou confirmação antes de iniciar pesquisa aprofundada, requisitos, planejamento, arquitetura ou execução. Ao receber correções, atualizar somente as partes afetadas.

<!-- source-section:parceiro-estrategico-global:008 sha256:486c85ed5efe1fabf3ab741501bffa72bc78034147d2e1b76cb9513b3596a8ac -->
## Tecnologia e software

Em projetos de software, realizar a Descoberta antes do levantamento formal de requisitos.

Esclarecer problema, oportunidade, proposta de valor, usuários, processos atuais, resultados de negócio, restrições técnicas, financeiras, operacionais e regulatórias, integrações, dependências, riscos e critérios mensuráveis de sucesso.

Somente depois do briefing confirmado avançar para requisitos funcionais e não funcionais, escopo, arquitetura, prioridades, roadmap, tarefas, implementação e validação.

Não confundir ideia de solução com problema validado. Não escolher stack ou arquitetura antes de entender os requisitos que justificam a decisão.

Antes de introduzir uma arquitetura, padrão de engenharia, workflow, framework ou convenção nova, inspecionar a fonte de verdade do projeto e verificar práticas consolidadas equivalentes. Adaptar ao contexto somente depois; identificar explicitamente qualquer extensão local.

<!-- end of selected V2 skill -->

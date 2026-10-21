# Debater uma ideia e consolidar o PRD

Use o Studio PRD existente para descoberta de produto. O agente de Produto é
responsável; os recortes product-core/discovery/planning são gerados da mesma
implementação, não outros consultores ou uma segunda skill CTO.

## Prompt de uso

> Use studio-prd para debater esta ideia antes de fechar o PRD. Comece pelo
> contexto já disponível. Questione premissas materiais, pesquise as afirmações
> técnicas nas fontes oficiais compatíveis com a stack/versão e compare soluções
> menores. Explique o que é evidência, hipótese, preferência e decisão. Mostre
> fontes consultadas, aplicabilidade, trade-offs e limitações. Faça poucas
> perguntas prioritárias. Não implemente, instale ferramentas ou altere produção.

Informe o problema, quem é afetado, resultado desejado, restrições e caminhos do
projeto/PRD se existirem. Não é necessário saber responder arquitetura ou detalhes
de infraestrutura: o agente deve pesquisar o que for tecnicamente verificável.
Dados de negócio privados e decisões materiais ainda precisam do proprietário.

## O que esperar

1. Diagnóstico: conhecido, lacunas, hipóteses, riscos e perguntas essenciais.
2. Debate: alternativas, consequências, recomendação e decisões fundamentadas.
3. PRD: documento canônico e plano interno coerentes, submetidos à sua aprovação.

Em projeto existente, preservar a arquitetura e decisões aprovadas e investigar
somente a mudança. Não repetir toda a entrevista. Banco, API/Backend e Frontend/UI
recebem triagem conceitual pertinente; detalhes vão a Arquitetura/SDD/UX.
Uma proposta de MVP é uma opção de escopo para decisão, nunca redução automática.

## Conferir a fundamentação

Uma recomendação técnica material deve apontar o trecho/caminho ou documentação
original efetivamente lida, versão ou UNKNOWN, relação com seu requisito e
limitações. Link de catálogo ou resultado de busca sozinho não demonstra consulta.
O agente deve distinguir a afirmação da fonte de sua inferência/recomendação.

Sua aprovação não transforma hipótese em fato nem comprova desempenho. Se faltar
fonte crítica, a conclusão fica NOT_VALIDATED e o restante independente continua.
Um rascunho pode expor dúvidas; o agente não pode declarar descoberta concluída
ou aprovação humana inexistente. Aprovar PRD não autoriza implementação/merge/deploy.

## Artefatos e limites

Briefing e PRD ficam no docs do cliente, usando os templates existentes. Fontes
ficam na biblioteca de referências desse projeto; decisões e justificativas usam
as tabelas existentes. Plano MD/JSON permanece equivalente, uma Task por módulo.
Não há memória paralela nem consulta obrigatória ao catálogo inteiro.

Dois ensaios independentes e a regressão do Harness exercitaram o comportamento;
eles não garantem decisões corretas em toda situação. Confira evidências reais e
limites de cada entrega em `docs/migration/studio-prd-evolution.md`.

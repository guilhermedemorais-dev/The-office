# Metodologia de desenvolvimento

A V2 organiza responsabilidade setorial, especificação e execução por entrega
funcional. O host executa; as regras não criam agentes persistentes nem garantem
que um modelo seguirá o processo. O orquestrador verifica evidência e corrige desvios.

## Fonte de verdade

GitHub Issue é a Human Task. Execution Contract JSON v2 contém instruções
normativas equivalentes; comentários e receipts registram execução. PR é o pacote
revisável. O plano do Studio PRD organiza módulos, fases, dependências e estimativas,
sem substituir o contrato. Não criar uma Issue para cada endpoint, camada ou setor.

## Etapas e decisões

1. **Produto e plano:** para produto novo, esclarecer problema, atores, jornadas,
   restrições, módulos e sucesso. Reutilizar PRD aprovado em continuidade. Oferecer
   opções pertinentes do arsenal existente, sem despejar catálogo inteiro.
2. **Arquitetura e SDD:** inspecionar sistema/versões, consultar padrões e docs
   oficiais quando necessário e comparar alternativas. Definir comportamento,
   dados, API, UI, aceite, dependências e validações. Registrar trade-offs em ADR.
3. **Execução:** conferir contrato/revisão, branch e fontes. Reutilizar componentes,
   CLIs oficiais e geradores da stack; preparar somente ferramentas necessárias.
   Cada setor consulta índice antes de ler skill ou pesquisar externamente.
4. **Validação:** executor testa; validators independentes atuam conforme escopo.
   UI aciona UX, risco sensível Segurança, operação DevOps e defeitos QA funcional.
   Uma ferramenta indisponível exige alternativa compatível ou limitação explícita.
5. **Documentação:** atualizar referência técnica e tutorial/how-to real. Registrar
   separadamente UPDATED, UNCHANGED, NOT_APPLICABLE ou PENDING com evidência.
6. **Métricas e revisão:** consolidar escopo aprovado, fases, resultados, bloqueios,
   documentação e próximos passos. Preparar relatório seguro e PR para o proprietário.
7. **Aceite e release:** verificar decisão humana real. Merge e deploy precisam de
   gates próprios; readiness local não é Done remoto nem autorização de produção.

Documentação começa no planejamento e evolui durante execução; a fase final confere
coerência com o software validado. Corrigir comportamento após QA exige reteste
afetado. Estimativa de horas é diferente de prazo calendário e percentual de escopo.

## Complexidade proporcional

| Nível | Aplicação | Registro |
| --- | --- | --- |
| TRIVIAL | Correção localizada sem impacto funcional/contratual/sensível | Intenção, aceite, check e resultado inline, salvo contrato/política existente |
| NORMAL | Comportamento delimitado e arquitetura conhecida | Task/contrato conciso, spec focada se necessária, validações aplicáveis |
| COMPLEX | Fronteiras, arquitetura, migração, integração ou decisões materiais | PRD/spec/contrato duráveis, rastreabilidade e gates setoriais |

Risco incerto sobe de nível. Poucas linhas não tornam um bug ou mudança visual
TRIVIAL. A regra completa está em [política V2](v2-execution-policy.md).

## Consulta e autonomia

O responsável consulta decisões/recursos já validados, índice do projeto e catálogo
central. Se faltar recurso adequado, pesquisa fontes primárias, avalia/adapta e
valida, depois encaminha registro ao Bibliotecário e atualização dos índices.
O catálogo contém metadados/proveniência; ferramentas continuam no executor real.
Pesquisar não autoriza mudar escopo ou instalar qualquer pacote encontrado.

Decisões reversíveis dentro do contrato seguem a autorização existente. Mudanças
materiais exigem registro de razão/impacto e revisão equivalente Issue/JSON antes
da execução afetada. Perguntas devem explicar contexto, opções e recomendação,
sem transferir detalhes técnicos rotineiros ao proprietário.

## Concluir e retomar

Antes de revisão final, conferir a [regra de fechamento](delivery-lifecycle.md).
Não omitir trabalho planejado para melhorar percentual. Registre tokens/tempo
somente quando medidos. Para retomar, confira Task/revisão, branch, artifact hash,
checkpoints e próxima ação; invalide apenas evidência afetada por mudanças.
[Fluxograma visual](../architecture/delivery-flow.svg).

---
name: office-creator-skill-agentes
description: "Manutenção MANUAL de skills e agentes do repositório The Office. Ativar somente com pedido explícito para criar, corrigir, auditar, atualizar ou reparar uma skill/agente do próprio The Office. Não ativar durante execução normal de projetos."
---

# Office Creator Skill & Agentes

## Identidade e isolamento
Esta é uma capacidade de **manutenção sob demanda** do repositório The Office, não um agente de setor, nem parte do runtime de orquestração. Não registrar em `library/indexes/skill-routes.json`, no DAG, nos perfis `office_*` de tarefas ou nos disparadores automáticos de desenvolvimento. Nunca interceptar solicitações normais dos setores.

**Não confundir** com a Skill Creator V2 global/avulsa de Codex ou ChatGPT. Nenhuma delas substitui a outra. Não copiar uma implementação antiga para dentro do The Office como fallback.

## Gatilho de ativação
Somente uma solicitação explícita do mantenedor sobre skills, agentes, referências, contratos ou geradores do próprio The Office. Não executar manutenção autônoma, agendada ou em background.

## Fonte de metodologia
Quando disponível, ler a **Skill Creator V2 global verificada**, incluindo seus contratos e avaliações. Antes de confiar nela, registrar caminho, origem, revisão ou hash e compatibilidade. Havendo versões conflitantes, não selecionar silenciosamente a antiga: informar o bloqueio e solicitar a fonte aprovada. Esta skill local define o processo operacional do Office, sem clonar nem substituir a Skill Creator global.

## Fluxo obrigatório de manutenção
1. Identificar o pedido e evidência de falha; mapear os arquivos, dependências, agentes e impactos.
2. Registrar estado de base: branch, commit, alterações locais, fonte canônica e testes existentes. Não sobrescrever trabalho não commitado.
3. Conferir duplicações e a versão atual antes de adicionar ou modificar qualquer skill/agente.
4. Corrigir a causa raiz na **fonte canônica/gerador** quando os arquivos forem gerados. Preservar V1 e contratos existentes; não editar o catálogo gerado como fonte primária.
5. Avaliar regressões: validação estática, testes do repositório e casos comportamentais positivos/negativos quando o host suportar. Reportar o que não foi executado.
6. Trabalhar em branch própria `fix/office-maintenance-<tema>` ou `feat/office-maintenance-<tema>`. Nunca aplicar mudanças diretamente em `main`.
7. Quando o usuário solicitar a atualização/publicação no GitHub, fazer **commit + push da branch**, verificar o SHA remoto e apresentar arquivos, resumo, testes e link. Se push falhar, declarar falha; não fingir sucesso.
8. Criar PR apenas quando pedido ou claramente incluído no escopo autorizado. **Não fazer merge nem deploy** sem solicitação específica.

## Regras de segurança
- Não permitir autoalteração durante uma task comum do The Office.
- Não alterar identidade, política global ou setup da Skill Creator avulsa.
- Nunca expor credenciais, artefatos privados ou `runtime-state`.
- Antes de mudanças destrutivas ou incompatíveis, exigir autorização explícita.
- Falha em testes bloqueantes impede marcar a entrega como validada; commit/push só com estado e ressalvas transparentes.
- Respeitar permissões do host e limites de ferramentas; não simular comandos executados.

## Contrato de saída
Informar gatilho, origem da implementação/método, branch, base commit, alterações, testes PASS/FAIL/NOT_RUN, riscos, commit SHA, confirmação de push e URL de PR (quando existir). Evidência verificável é obrigatória para alegar execução.

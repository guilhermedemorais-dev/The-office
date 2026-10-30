# Usar o The Office no OpenCode

Este adaptador registra agentes e descoberta de skills no **projeto escolhido**.
Não instala OpenCode, não altera providers/modelos/configuração global, não inicia
Graphiti e não substitui os contratos dos setores. Requer Python 3.11+ por reusar
as verificações e a escrita com backup do helper Codex existente.

## Instalação inicial

Use um bundle revisado em localização estável, separado do código do cliente.
Não registre caminhos de scratch ou uma cópia descartável como instalação final.
O projeto cliente deve existir. Troque os caminhos de exemplo pelos reais:

```sh
python scripts/register_opencode_agents.py plan --bundle-root /ferramentas/the-office --project-root /projetos/cliente
python scripts/register_opencode_agents.py check --bundle-root /ferramentas/the-office --project-root /projetos/cliente
```

`plan` é somente leitura. `check` retorna 1 quando faltam alterações; isso não é
falha de execução do host. Depois de revisar o plano e dentro da autorização
existente para esse destino, aplique e confira:

```sh
python scripts/register_opencode_agents.py apply --bundle-root /ferramentas/the-office --project-root /projetos/cliente
python scripts/register_opencode_agents.py check --bundle-root /ferramentas/the-office --project-root /projetos/cliente
```

O helper cria `.opencode/agents/office_*.md`: orquestrador `primary`, demais
setores `subagent`. Cria `.opencode/skills/<id>/SKILL.md` com metadados de descoberta,
origem absoluta e hash. Esses adaptadores mandam ler a skill canônica completa e
suas referências antes de agir; não duplicam a implementação das skills. O
diretório `skills/` na raiz do bundle, sozinho, não garante descoberta pelo host.

Selecione `office_orchestrator` no OpenCode do projeto. Execute uma tarefa
descartável delimitada, delegue ao setor necessário e registre operação/recibo
reais. Perfil em disco, `check` e planejamento não comprovam dispatch do host.
Se a versão instalada não reconhecer o formato, pare e confronte seu schema,
sem modificar configurações do usuário para esconder a incompatibilidade.

## Atualização separada

Use o [prompt de atualização](update-prompt.md), não repita a instalação inicial.
Registre versões e revise o diff da fonte antes de atualizar o bundle ativo.
Com a fonte revisada, repita `plan`, `check`, `apply`, `check` nos mesmos caminhos.
Skills com fonte alterada ganham novo hash no adaptador. Não regenere índices para
esconder drift; o bundle deve passar seus checks antes de registrar.

Somente adaptadores anteriormente gerenciados e intactos podem ser atualizados.
Arquivos customizados, ausentes ou divergentes bloqueiam a operação. Fontes
removidas exigem revisão manual dos adaptadores antigos; o helper não apaga dados
nem arquivos por inferência. A reinstalação não é mecanismo de resolução de conflito.

## Preservação e recuperação

- `opencode.json`, providers, modelos, MCPs, configurações globais e arquivos do
  cliente não são escritos pelo helper. Overrides `agent.office_*` nesse JSON
  bloqueiam para não criar duas definições divergentes.
- `opencode.jsonc` existente e não vazio exige revisão manual de colisões; este
  helper stdlib não interpreta JSONC nem o reescreve.
- O estado gerenciado fica em `.opencode/office-registration.json`. Hashes são
  consistência local, não assinatura de origem ou autenticação.
- Antes de alterações, a escrita compartilhada cria backup privado em
  `.opencode/.office-agent-backups/<id>/`, com manifest e arquivos anteriores.
  A repetição sem mudanças não cria outro backup. Falha parcial tenta rollback.
- Revise o manifest e restaure somente os caminhos gerenciados afetados. Um
  arquivo anteriormente inexistente pode ser removido apenas se ainda tiver o
  conteúdo gerenciado esperado; preserve alterações posteriores. Depois use `check`.
- Não versione estado/backup privado em repositórios compartilhados. Revise o
  `.gitignore` do cliente no processo de adoção; este helper não o modifica.
- O destino deve ser confiável, pertencente ao usuário e sem escrita simultânea.
  Symlinks, reparse points e hardlinks são recusados; não é sandbox contra ator
  com escrita concorrente na mesma máquina.

## Memória opcional

O registro não conecta o MCP de referência Graphiti. Use o adaptador documentado
em [memória](../../integrations/memory/README.md), com origem/escopo e backend
selecionados separadamente. Required sources continuam primeiro, Potpie/local
continua disponível, e memória não concede aprovação ou execução.

Preserve banco, ledger, configuração local e backups de memória durante update.
Não reimporte chats/arquivos, recrie banco ou migre embeddings automaticamente.
Uma mudança de backend/modelo exige plano e verificação próprios. As permissões
geradas negam chamadas destrutivas Graphiti conhecidas, mas nomes podem variar
com o servidor: confira os schemas efetivos. Isso não impede comandos equivalentes
via shell/rede nem acrescenta autorização ao servidor.

## Versão e limites da validação

Baseline documental/código: OpenCode v1.19.4,
`148842ef7cb1bc34192b3fff57d0f9721ab9c801`, documentação oficial de
[agentes](https://opencode.ai/docs/agents/) e
[skills](https://opencode.ai/docs/skills/). A versão instalada deve ser observada
no host; o helper apenas registra essa baseline, não inventa detecção.

Fixtures cobrem plano somente leitura, idempotência, atualização, conflitos,
preservação de configuração e bloqueios de path. Execução no binário OpenCode,
descoberta/dispatch real, autenticação, conexão de memória e homologação nativa
permanecem NOT_VALIDATED até observação no host escolhido.

Prompts independentes: [instalação](installation-prompt.md) e
[atualização](update-prompt.md).

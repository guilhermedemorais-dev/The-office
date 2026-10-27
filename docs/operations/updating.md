# Atualização do Harness e do Portal

Responsáveis: Ambiente verifica ferramentas/host; Governança controla revisão;
DevOps prepara Portal/infra conforme o destino. Não atualizar caches à força nem
executar scripts remotos sem inspecionar a origem/revisão.

Use o [prompt de atualização](update-prompt.md) para conduzir este procedimento.
O [prompt de instalação](installation-prompt.md) é apenas para instalação inicial;
não reinstale por cima para resolver atualização ou conflito.

## 1. Identificar o que está ativo

Registre checkout/remoto/branch/commit da fonte e localização da cópia usada pelo
host. Confira alterações com `git status --short`, inclusive arquivos não
versionados. Um plugin instalado pode ser uma cópia diferente do repositório.
Preserve trabalho local; não resetar, limpar ou sobrescrever para facilitar update.

## 2. Buscar e revisar

Na fonte correta, com Git já configurado:

```sh
git fetch origin
git log --oneline HEAD..origin/main
git diff --stat HEAD..origin/main
```

Os comandos usam main como exemplo. Quando a atualização solicitada aponta a
outra branch/commit revisados, use essa referência confirmada, sem misturar versões.
Revise mudanças materiais em skills,
referências, scripts e dependências. Se o checkout estiver limpo e sua branch
local puder avançar sem divergência, `git merge --ff-only origin/main`
é uma atualização local da cópia de trabalho; não é merge do PR na main.
Divergência exige revisar commits e preservar customizações, não force/reset.

## 3. Conferir e ativar

```sh
python scripts/build_skill_routes.py --check
python scripts/verify_preservation.py
python -m unittest discover -s tests -v
git diff --check
```

Revisar falhas/skips no ambiente real. Não regenerar fontes só para esconder drift.
Atualize a cópia de plugin ativa pelo mecanismo documentado pelo host, preservando
configurações/marketplace e extensões locais. Recarregue/reinicie a sessão quando
necessário e confira o commit/conteúdo ativo; teste uma seleção e operação pequena.
Registro no host e testes nativos continuam exigindo evidência local.

No OpenCode, siga [registro e atualização](opencode.md): use o helper nativo
`register_opencode_agents.py` em plan/check antes de apply, contra bundle estável
e projeto explícitos. Ele preserva opencode.json, providers/modelos e configurações
de MCP. Hashes anteriores precisam corresponder aos adaptadores gerenciados;
customizações/JSONC conflitantes não podem ser sobrescritas.

Preserve memória existente: banco, ledger de ingestão, configuração local,
escopos e backups não pertencem à atualização de arquivos do Harness. Não faça
reset/reimportação/migração ou troca de embeddings por efeito colateral. Mudança
de esquema/backend exige plano próprio. [Memória](../../integrations/memory/README.md)
permanece opcional e seu estado operacional deve ser conferido separadamente.

## 4. Atualizar o template do cliente separadamente

No checkout da origem Portal, revisar o novo commit antes de fixá-lo. Usar o
sincronizador existente contra CLIENT_ROOT, primeiro dry-run e depois apply
aprovado. Arquivos ficam em CLIENT_ROOT/docs/portal/; customizações e conflitos
são preservados. Não apagar arquivos antigos automaticamente. Rever a navegação
de docs, API/configuração e comandos da versão escolhida. Atualizar Harness não
atualiza automaticamente todos os clientes ou publica seus portais.

## 5. Registrar e recuperar

Registre revisão anterior/nova, ações, escopo, checks e pendências na Task/evidência
existente. Atualize manuais afetados. Para voltar à revisão anterior, use uma cópia
separada preservando o estado/configuração do host; planeje a restauração conforme
a instalação real. Migração de dados, segredo/OAuth, produção ou operação destrutiva
precisam de decisão própria. Não prometer rollback universal por `git checkout`.

Versões e decisões históricas ficam em CHANGELOG/ADRs e relatórios de migração.
Documentação de host consultada em 2026-10-21:
https://developers.openai.com/plugins/build/plugins . O documento confirma
empacotamento, registro local e atualização da cópia usada pelo host; não comprova
que a instalação deste Harness já foi homologada no Desktop do usuário.

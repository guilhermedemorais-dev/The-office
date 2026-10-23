# Guia de instalação e configuração do The Office V2

Use este guia para entender e conferir a instalação. Na versão `2.0.0-alpha.2`
deste branch, instale o plugin e execute a ação **Setup** para iniciar o onboarding.
Essa versão ainda aguarda integração/publicação; o plugin atualmente disponível
no marketplace não oferece essa ação. Para hosts sem esse fluxo, use o
[prompt manual de instalação](installation-prompt.md). O guia explica requisitos,
limites e critérios de aceitação.

## 1. Identificar a máquina e o host

Confirme SO/versão/arquitetura, local do projeto, host de IA e ferramentas já
instaladas. O conjunto Environment exige **Python 3.11+**; esta entrega foi testada
com Python 3.12. O roteador isolado usa Python stdlib. Git serve para obter a fonte.
Node é necessário para recursos específicos, como preparar o template do Portal;
REA e demais capacidades têm requisitos próprios. Docker não é obrigatório.

No Linux/macOS o executável pode se chamar `python3`; no Windows, `py -3`.
Verifique `--version` antes de usar. WSL é Linux. A existência de catálogo nativo
não homologa Windows 10, Windows 11 ou macOS nesta revisão.

## 2. Obter a distribuição correta

Em pasta nova, separada do código do cliente:

```sh
git clone --branch codex/add-public-apis-discovery https://github.com/guilhermedemorais-dev/The-office.git
cd The-office
git rev-parse HEAD
python scripts/office.py --help
```

Se houver checkout existente, confira remoto, branch e mudanças; siga
[atualização](updating.md), sem sobrescrever trabalho. A base V2 já está na main após o PR #2; este branch contém os manuais e o onboarding ainda em revisão. Os marketplaces herdados distribuem V1 e não ativam a V2 da raiz.
Leia `AGENTS.md` e a política de execução desta versão.

## 3. Registrar ou usar pelo checkout

O bundle raiz contém `.codex-plugin/plugin.json` e `skills/`; há manifestos de
compatibilidade para outros hosts. No host que suporta instalação local, use o
mecanismo atual documentado para registrar a raiz da V2, preservando entradas
existentes. Um marketplace local deve apontar à cópia correta. Recarregue o host
quando necessário e verifique reconhecimento e execução real.

A documentação oficial consultada em 2026-10-21 descreve registro local e atualização
da cópia ativa: https://developers.openai.com/plugins/build/plugins . O formato
suportado depende do host; este guia não presume homologação do Desktop do usuário.
O root `plugin.json` simplificado é histórico deste overlay; não assuma que já
constitui o manifest portable Agent Plugins atual. Valide o manifest compatível
real selecionado e seu comportamento no host antes de afirmar instalação.

Alternativa de trabalho: abrir este checkout e fornecer ao agente sua localização
canônica e a do projeto cliente. Isso permite roteamento explícito por `AGENTS.md`,
mas deve ser chamado **uso por checkout**, não registro confirmado do plugin.
Não copie todas as skills para o prompt nem use V1 e V2 simultaneamente.

### Regra global de delegação no Codex

O manifesto Codex associa a ação **Setup** à skill `skills/setup/SKILL.md`. O
onboarding só roda quando iniciado pelo usuário depois da instalação; a instalação
do plugin não executa comandos de escrita. A skill localiza o `AGENTS.md` global em
`$CODEX_HOME/AGENTS.md` ou no diretório padrão Codex do usuário, mostra o diff,
obtém aprovação para alterar o escopo global, faz backup datado e valida a mesclagem
marcada. Se o bloco já estiver idêntico, não escreve nem cria backup; conflito nos
marcadores ou falha de backup interrompe a alteração.

Perfis nativos do host e contratos `agents/<setor>/AGENT.md` são artefatos
distintos. A skill inspeciona `config.toml` e perfis existentes sem expor segredos,
mas não cria perfis nem altera configuração por inferência. Ela verifica em
separado se a sessão pode delegar e se um dispatch real retorna resposta.
`AGENTS_GLOBAL_RULE`, `AGENT_PROFILES_DISCOVERED` e `AGENT_DISPATCH_VERIFIED`
exigem evidência distinta; diretório, perfil, flag ou regra escrita não provam
invocação. Sessões já abertas podem precisar ser reiniciadas para carregar a regra.

## 4. Diagnosticar e preparar seletivamente

Leia a skill Environment selecionada e suas referências antes de operações.
O entrypoint existente diferencia raiz do Harness e workspace do cliente:

```sh
python plugins/dev-environment-standard/skills/dev-environment-standard/scripts/environment.py doctor --repo-root . --workspace /projetos/cliente --json
python plugins/dev-environment-standard/skills/dev-environment-standard/scripts/environment.py prepare --repo-root . --workspace /projetos/cliente --dry-run --json
```

Substitua caminhos reais e executável Python conforme o SO. `doctor` e dry-run
não instalam. Defina seleções conforme requisitos/stack já aprovados; catálogo
não significa instalação. Reuse Git/runtimes/gerenciador/lockfiles disponíveis.

As ações concretas são aprovadas pelo mecanismo já existente do Environment,
com comando/componente/escopo exatos; consulte a [referência de operações](../../plugins/dev-environment-standard/skills/dev-environment-standard/references/operations.md).
A autorização já dada para preparo local necessário dispensa repetir perguntas
rotineiras, mas não amplia permissões do host ou autoriza ações privilegiadas.
Estado privado pode ficar em `--state-dir` gravável/ignorado quando o bundle for
somente leitura. Nunca commitar credenciais, preferências ou estado de runtime.

Depois reutilize `status` compatível e faça reparo pontual em falha/drift. Não
instale todas as stacks/CLIs/MCPs nem execute bootstrap completo antes de cada Task.
Autenticação é conduzida pelo host/usuário e verificada separadamente da configuração.

### Roteamento proativo de MCPs por projeto

No início de um projeto ou quando uma Task mudar materialmente, traduza o objetivo
em capacidades necessárias e pesquise cada necessidade no catálogo MCP. Informe
quais opções relevantes já estão disponíveis e quais exigiriam instalação,
configuração, autenticação ou validação. Explique em linguagem concreta o problema
que cada opção resolve, acesso solicitado, escopo, custo conhecido e alternativa
sem MCP. `CORE` no catálogo significa prioridade para avaliar, não requisito global:
nenhum MCP de terceiros é obrigatório para o plugin básico funcionar.

Quando não houver opção adequada no catálogo, faça descoberta externa delimitada,
começando pela documentação oficial/registro do provedor; use GitHub/grep.app para
exemplos de código quando isso ajudar. Antes de recomendar a instalação, informe
fonte, compatibilidade e limitações. Não instale ou conecte silenciosamente. Para
autenticação, indique a URL e o fluxo seguro oferecido pelo host; não solicite token
no chat nem o grave em arquivo versionado.

Relate a prontidão com evidência separada: plugin reconhecido, ferramentas exigidas
disponíveis, MCP configurado, autenticação concluída e operação verificada. Estado
não observado é `UNKNOWN`; entrada no catálogo ou arquivo de configuração não prova
conexão. Só declare uma Task pronta quando suas capacidades necessárias estiverem
disponíveis e verificadas no nível exigido.

## 5. Confirmar operação básica

```sh
python scripts/office.py plan documentation
python scripts/office.py plan ux-design --capability ux-visual-validation
python scripts/office.py search "OSV"
python scripts/build_skill_routes.py --check
python scripts/verify_preservation.py
python -m unittest discover -s tests -v
git diff --check
```

Anote comando, exit code e skips. O Plop real tem um teste opcional ativado por
`OFFICE_PLOP_BINARY` quando esse runtime já estiver preparado para validação;
a ausência é um skip, não execução inventada. Não instalar Plop em toda máquina.
Os planos retornam caminhos/hashes e `PLANNED_NOT_EXECUTED`. O host precisa ler
as skills e realizar uma operação segura real para demonstrar o fluxo.

## 6. Preparar o projeto cliente

O tutorial está em [utilização](tutorial.md); o plano aprovado organiza módulos e
Tasks. Quando Portal foi adotado, siga [busca/preparação](client-portal.md) para
copiar o template versionado a **CLIENT_ROOT/docs/portal/** e ligá-lo à home docs.
Não instalar o portal dentro do Harness. Preparação não inicia backend ou deploy.

## 7. Aceitar e manter

Confirme revisão do bundle ativo, ferramentas realmente verificadas, preferência
local reutilizada e uma Task descartável com evidência. Registre o que depende de
login, ferramenta ausente ou homologação. “Plugin instalado” e “Task pronta” são
estados diferentes. Consulte o [smoke test](user-guide.md).
Leia [atualização](updating.md) antes de atualizar fonte/cópia ativa/Portal.

Para deixar de usar, selecione o entrypoint anterior ou feche o checkout. Preserve
trabalho e configurações antes de remover qualquer cópia; não há desinstalação
universal automática. O clone deste guia não substitui cache V1 instalado.

## Integridade e limites

`.gitattributes` conserva LF para comparar hashes. Os quatro caches Python
herdados arquivados em `docs/migration/v1-bytecode/` são evidência de migração,
não caches para regenerar. Fonte local íntegra, registro no host e execução nativa
são verificações distintas. Não afirme homologação ou economia de tokens com
base apenas na cópia dos arquivos ou nos testes estruturais.

# Registrar e usar agentes globais no Codex

Aplica-se ao helper desta revisão do The Office V2, Task
`OFFICE-GLOBAL-AGENTS-001`, contrato revisão 3. Público: mantenedor ou agente
Environment com autorização de escrita no diretório Codex escolhido. O helper
exige Python 3.11+ (`tomllib` da biblioteca padrão), sem dependências adicionais.

## O que cada verificação comprova

| Estado | Evidência necessária | Limite |
| --- | --- | --- |
| Fonte disponível | Checkout/revisão e contratos `agents/*/AGENT.md` | Não comprova plugin instalado |
| Bundle instalado | Cópia ativa e revisão reconhecidas pelo host | Não comprova registro de papéis |
| Perfis registrados | `check` sem diferenças no Codex home escolhido | Não comprova disponibilidade nesta sessão |
| Perfis disponíveis | Host expõe os papéis e ferramenta de subagentes nesta sessão | Não comprova execução |
| Agente executado | Invocação real, operação e recibo do responsável na revisão atual | Não aprova outros setores |

O helper registra configurações, não instala o plugin nem inicia processos
permanentes. `office.py plan` seleciona skills e retorna `PLANNED_NOT_EXECUTED`.
Só uma invocação real pela ferramenta de subagentes demonstra execução.

## Escolher fonte e destino

Use `--bundle-root` para a raiz absoluta da cópia V2 que os perfis devem ler e
`--codex-home` para o diretório absoluto de configuração do host. Ambos são
obrigatórios, sem destino implícito. Não confunda:

- Checkout fonte, onde a alteração é revisada e versionada.
- Bundle instalado/ativo, que o host realmente deve usar.
- Diretório de ensaio, descartável, usado nos testes de registro.

Uma cópia somente para ensaio não deve virar referência permanente do host.
Confira revisão e existência dos 15 contratos antes de qualquer aplicação.
Atualizar o Git não atualiza automaticamente o bundle instalado ou as sessões.

## Planejar, conferir e aplicar

Substitua os caminhos abaixo pelos caminhos absolutos escolhidos. Em Windows,
use caminhos como `C:/ferramentas/the-office` e aspas quando houver espaços; use
o executável Python compatível já instalado (`python`, `python3` ou `py -3`).

```sh
python scripts/register_codex_agents.py plan --bundle-root /caminho/absoluto/the-office --codex-home /caminho/absoluto/codex-home
python scripts/register_codex_agents.py check --bundle-root /caminho/absoluto/the-office --codex-home /caminho/absoluto/codex-home
```

1. Leia o plano e os conflitos. `plan` e `check` não escrevem nem criam pastas.
2. Se há conflito, preserve a configuração existente e resolva a divergência
   com o owner. Não apague instruções, perfis ou overrides para forçar aprovação.
3. Somente quando a aplicação ao destino escolhido estiver autorizada, execute:

```sh
python scripts/register_codex_agents.py apply --bundle-root /caminho/absoluto/the-office --codex-home /caminho/absoluto/codex-home
python scripts/register_codex_agents.py check --bundle-root /caminho/absoluto/the-office --codex-home /caminho/absoluto/codex-home
```

4. Confira o resultado, o backup e a revisão do bundle. Recarregue o host ou abra
   uma nova sessão se os perfis ainda não estiverem visíveis. Chats abertos podem
   manter instruções anteriores; não presuma recarga global imediata.
5. Pela ferramenta real do host, acione um setor necessário com escopo seguro e
   limitado. Registre perfil, tarefa, fontes lidas, operação, resultado e limites.
   Não execute todos os setores só para testar o cadastro.

## Contrato do comando

| Operação/estado | Exit code | Significado |
| --- | --- | --- |
| `plan`, `CHANGES_REQUIRED` | 0 | Plano calculado; diferenças encontradas |
| `check`, `CHANGES_REQUIRED` | 1 | Cadastro ainda diverge do esperado |
| `CONFIGURED` | 0 | Sem diferenças detectadas |
| `apply`, `APPLIED` | 0 | Alterações aplicadas ao destino explícito |
| `BLOCKED` | 2 | Entrada, configuração ou conflito impede operação |

A saída é JSON de diagnóstico sanitizado. Erros de uso do parser também podem
sair com código 2; leia a mensagem, não interprete qualquer exit 2 como cadastro
válido. Os perfis são derivados dos 15 contratos canônicos e o mapeamento está
em [responsabilidades](../architecture/agents.md).

## Preservação e recuperação

Use um Codex home confiável, pertencente ao usuário e sem alterações simultâneas.
As checagens de paths não eliminam todas as corridas de filesystem hostil.

`apply` é opt-in e modifica somente os artefatos de cadastro gerenciados. Não
altera modelo, provider, permissões, MCPs ou limite `max_threads` existente.
Antes de trocar arquivos existentes, salva originais e manifesto em diretório
exclusivo `CODEX_HOME/.office-agent-backups/<uuid>/`. Uma repetição sem diferenças
não cria novo backup. Ausência anterior de arquivo deve ser considerada ao
restaurar; não remova arquivos não relacionados.

A aplicação não é uma transação atômica entre vários arquivos. Em falha parcial,
o helper tenta restaurar arquivos já trocados; confira o diagnóstico e o backup
antes de repetir. Para recuperação manual, revise o manifesto e restaure apenas
os artefatos afetados, preservando alterações posteriores. Reexecute `check`.

Conflitos bloqueiam a escrita, incluindo TOML inválido, papel/perfil divergente,
bloco gerenciado alterado ou inválido, `AGENTS.override.md` não vazio, arquivos
conhecidos de instruções globais customizados e `multi_agent = false` explícito.
Links simbólicos, reparse points e hardlinks nos alvos são recusados. Não há
flag de força para sobrescrever customizações. Um host já registrado com perfis
próprios pode exigir reconciliação manual, mesmo quando seu registro funciona.

## Atualizar perfis gerenciados

Depois de atualizar o bundle revisado, execute os mesmos `plan`, `check` e,
quando autorizado, `apply` com as raízes explícitas. O helper guarda estado local
em `CODEX_HOME/.office-agent-profiles.json`, com `schema_version`, identificador
`generator` e, por perfil, `sha256`, `description` e `config_file`. Cada perfil
TOML gerado recebe o envelope `# THE-OFFICE-CODEX-PROFILE v1 sha256=...`, cujo hash
cobre o payload abaixo do cabeçalho. O estado registra o hash do arquivo completo.

- Com estado válido, o perfil existente deve coincidir com o hash anteriormente
  registrado, ter envelope íntegro e nome/descrição compatíveis. Se permanecer
  intacto, `apply` pode atualizá-lo para a geração corrente do bundle. A descrição
  gerada no registro TOML também pode ser atualizada; layouts divergentes bloqueiam.
- Perfil alterado, ausente quando esperado, estado inválido ou caminho/registro
  divergente resultam em `BLOCKED`. Não há adoção forçada de customizações.
- Sem estado, um perfil legado só é adotado quando seus bytes forem exatamente
  iguais à geração corrente, com envelope, ou ao payload corrente sem envelope.
  `apply` acrescenta envelope/estado. Um perfil de geração antiga que já diverge
  do bundle corrente exige backup e reconciliação manual, mesmo sem edição local.
- O arquivo de estado participa do mesmo plano, backup e tentativa de rollback
  dos demais artefatos. Na recuperação, preserve um conjunto consistente de
  perfis, estado e registro. Não edite hashes para contornar um conflito.

Hash, envelope e estado são controles locais de consistência, **não são assinatura
nem autenticação de origem**. Quem controla `CODEX_HOME` pode editar tanto os
perfis como o estado e seus hashes. O mecanismo pressupõe diretório confiável,
pertencente ao usuário e quiescente; não oferece proteção contra falsificação por
um ator com escrita nesse diretório. Esses registros não comprovam execução de
agentes nem ampliam permissões do host.

## Responsabilidade em cada chat

O principal coordena, escolhe apenas setores exigidos pelo escopo/gatilhos V2,
respeita concorrência e ownership, e consolida recibos reais. Cada setor acionado
usa o `office_*` correspondente, lê seu contrato, seleciona capacidades e lê as
skills/referências obrigatórias com o `reference_base` correto. Não crie outro
orquestrador para duplicar a coordenação. Perfil/ferramenta ausente significa setor
`NOT_EXECUTED` e alegações dependentes `NOT_VALIDATED`, sem parecer simulado.

O registro global permite reutilizar os perfis em projetos e chats; não mantém
instâncias rodando nem garante exposição imediata no Desktop. Conversa comum não
exige pipeline. Configuração compatível e testes em fixture não homologam o
Desktop, todo sistema operacional ou a execução de especialistas no host real.

## Fontes e verificação

- Código: [`register_codex_agents.py`](../../scripts/register_codex_agents.py).
- Contratos: [`agents/`](../../agents/) e política [`AGENTS.md`](../../AGENTS.md).
- Documentação oficial consultada na Task: [subagentes](https://learn.chatgpt.com/docs/agent-configuration/subagents)
  e [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

O helper e o bloco de roteamento são decisões locais sobre mecanismos de
configuração do host, sem garantia de execução por parte do fornecedor.
Verificação documental: comandos e semântica confrontados com o helper desta
Task; QA/Security e execução no host têm recibos próprios. Não foi aplicado ao
Codex home real nesta Task. Capturas de UI: NOT_APPLICABLE, procedimento CLI;
smoke de execução real no Desktop: NOT_VALIDATED por este artigo.

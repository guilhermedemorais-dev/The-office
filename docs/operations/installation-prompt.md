# Prompt de instalação inicial e configuração assistida

Copie o bloco para o agente com acesso à máquina. Substitua os caminhos ou peça
a ele para identificar o workspace aberto. O prompt autoriza preparação local
necessária, sem substituir permissões do host. Não instala todas as stacks.
Este é o fallback manual, não um script executado pelo botão de instalação. No
Codex, prefira instalar o plugin e iniciar seu onboarding pela ação **Setup**.
Para uma instalação existente, use exclusivamente o
[prompt de atualização](update-prompt.md), preservando configuração e memória.

```text
Instale e configure o The Office V2 nesta máquina para o workspace atual.
Fonte: https://github.com/guilhermedemorais-dev/The-office.git
Use a revisão explicitamente solicitada; se nenhuma foi indicada, confira a
main atual e registre commit, branch e estado do checkout antes de instalar.

1. Identifique sistema/versão/arquitetura e runtime real, host do agente,
   workspace cliente, Git e Python existentes. WSL é Linux. Preserve arquivos,
   instalações, plugins e configurações. Reutilize checkout correto se existir.
2. Obtenha a branch em pasta separada do software cliente e registre o commit.
   Leia AGENTS.md e docs/operations/v2-execution-policy.md. Selecione Ambiente
   pelo roteador; leia integralmente as skills retornadas e referências ativas.
3. Separe registro do plugin, ferramentas instaladas, configuração, conexão,
   autenticação e operação verificada. Consulte a documentação atual do host
   para registrar o bundle raiz; preserve marketplace/configuração existente.
   Não usar marketplace V1 para afirmar ativação V2. Se o host não permitir
   registro, documente a alternativa por checkout sem afirmar plugin instalado.
   Ao concluir, informe separadamente PLUGIN_RECOGNIZED, REQUIRED_TOOLS_AVAILABLE,
   MCP_CONFIGURED, AUTHENTICATED e OPERATION_VERIFIED, com evidência ou UNKNOWN.
   Nunca diga “pronto” só porque copiou/registrou o plugin.
4. No Codex, depois de instalar o plugin, execute a ação **Setup** do onboarding
   The Office V2. Ela usa `skills/setup/SKILL.md` para verificar os agentes,
   propor a regra global, fazer backup antes da edição aprovada e validar o arquivo.
   A instalação do plugin não executa Setup automaticamente. Se o host não expuser
   o onboarding, abra essa skill no bundle ativo ou siga o procedimento documentado
   em `skills/setup/references/agent-routing-block.md`. Não replique o bloco em
   prompts paralelos. Sem acesso ao arquivo ou ferramenta real de delegação, registre
   USER_ACTION_REQUIRED/UNKNOWN; não declare agentes registrados ou invocados.
   No OpenCode, confira a versão real e siga docs/operations/opencode.md. Use
   scripts/register_opencode_agents.py plan/check com --bundle-root estável e
   --project-root absolutos; revise o plano antes de apply e rode check depois.
   Ele registra agentes e adaptadores de descoberta em .opencode do projeto,
   sem alterar modelos/providers/MCPs ou configuração global. Preserve colisões;
   não copie a pasta skills/ supondo descoberta automática e não confunda os
   comandos /plugin do Claude com instalação no OpenCode. Registro não comprova
   dispatch; execute uma tarefa sintética limitada no host escolhido.
   Em outros hosts, não escreva em configurações do Codex; siga o adaptador nativo.
5. Use o Environment existente: doctor e prepare --dry-run com repo-root do
   Harness e workspace do cliente. Confira requirements/lockfile e catálogo
   da stack. Use status compatível depois; não repetir diagnóstico completo
   antes de cada Task. Python 3.11+ é o mínimo do Environment; Node só se preciso.
6. Mapeie as capacidades que a tarefa/projeto realmente exige e pesquise cada
   uma no catálogo The Office. Informe proativamente MCPs/ferramentas relevantes,
   o problema que resolvem, disponibilidade real, pré-requisitos, permissões,
   escopo e custo conhecido. CORE no catálogo significa prioridade reutilizável,
   não dependência universal. Não instalar tudo nem bloquear tarefas sem relação.
7. Para capacidade ausente, explique a lacuna e ofereça a configuração compatível
   com o host. Mostre fonte oficial, URL exata de cadastro/documentação, nome do
   campo/variável e arquivo ou tela de configuração confirmados. Se exigir token,
   direcione a autenticação para o fluxo seguro do host; nunca peça o segredo no
   chat, leia/repita seu valor ou grave-o em arquivo versionado. Não instale,
   conecte ou autentique em silêncio. Use o consentimento/autoridade do host.
   Se não houver opção adequada no catálogo, faça descoberta externa delimitada,
   priorizando documentação oficial e registrando fonte, compatibilidade e limites.
8. Para ações privilegiadas, mudança material ou autenticação que exige pessoa,
   use o mecanismo legítimo do host e explique o bloqueio. Reutilize preferências
   e permissões já registradas. Não migrar stack, criar serviços, mudar produção
   ou remover instalações.
9. Verifique cada ação executada. Rode rotas e checks pertinentes; valide no
   host real se a V2 é reconhecida e usada. Teste uma demanda descartável pequena
   sem merge/deploy; plano gerado sozinho não é ativação nem execução da skill.
10. Se o projeto cliente adotou Portal, siga docs/operations/client-portal.md:
   busque a origem fixada, revise plano e prepare em docs/portal/ do CLIENTE,
   preserve customizações e vincule à home de docs. Não iniciar backend,
   containers, OAuth ou publicação apenas para copiar o template.
11. Entregue revisão da fonte e da cópia ativa, host/SO, ações/versões/escopos,
   matriz de prontidão, estados AGENTS_GLOBAL_RULE, AGENT_PROFILES_DISCOVERED e
   AGENT_DISPATCH_VERIFIED, verificações realizadas, backup criado, limitações e
   como atualizar. Marque explicitamente o que ficou sem validação. Não merge/deploy.
12. Se memória persistente Graphiti foi selecionada, siga integrations/memory/README.md.
    Registre projeto, origem, versões efetivas e local privado dos dados/ledger.
    Não exponha o MCP de referência nem instale banco/modelos/credenciais sem o
    escopo correspondente. Preserve fontes versionadas e fallback Potpie/local.
    Comece com dados sintéticos; ACK/enfileirado não significa memória persistida.
    Se não selecionada ou sem dependências, reporte NOT_CONFIGURED/NOT_VALIDATED
    sem bloquear o uso básico. Não importe chats ou segredos automaticamente.
```

O agente precisa de capacidades reais de filesystem/terminal ou ferramentas
compatíveis. Este documento não executa a instalação. Em host sem acesso local,
prepare o handoff; a máquina do usuário continua pendente.

## Conferir o resultado

Receba evidência do registro no host, `office.py` respondendo, skills efetivamente
lidas e uma operação segura executada. `AUTH_REQUIRED`, conexão ausente ou
operação não verificada impedem afirmar prontidão daquela capacidade. Consulte o
[guia de instalação](installation.md) para o fluxo inicial e use o
[prompt separado de atualização](update-prompt.md) somente para atualizar uma
instalação existente. A preparação de ferramentas permanece seletiva conforme o projeto.

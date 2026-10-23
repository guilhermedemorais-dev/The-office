# Prompt de instalação e configuração assistida

Copie o bloco para o agente com acesso à máquina. Substitua os caminhos ou peça
a ele para identificar o workspace aberto. O prompt autoriza preparação local
necessária, sem substituir permissões do host. Não instala todas as stacks.

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
4. Se o host for Codex, localize CODEX_HOME; use o valor configurado ou, na
   ausência dele, o diretório padrão do Codex do usuário. Inspecione sem expor
   segredos o AGENTS.md global, config.toml e os perfis existentes em agents/.
   Faça backup datado do AGENTS.md antes de editar. Mescle o bloco abaixo de
   forma idempotente, preservando todo o conteúdo alheio e sem duplicar blocos.
   Não altere config.toml nem crie perfis por inferência: arquivos de contrato
   `agents/*/AGENT.md` do plugin não são automaticamente perfis registrados.
   Confirme a configuração de delegação suportada pelo host e a disponibilidade
   real dos agentes; só ajuste configuração existente após apresentar a mudança
   concreta e obter a aprovação exigida pelo host. Não declare dispatch ativo sem
   observar uma chamada e resposta reais nesta sessão.

   ~~~~markdown
   <!-- the-office-v2:agent-routing:start -->
   ## Delegação obrigatória aos agentes responsáveis

   Em tarefas de projeto que envolvam setores especializados, consulte o roteador
   e os agentes responsáveis disponíveis no plugin ativo e delegue a análise ou
   execução de cada setor pertinente ao agente dono daquele domínio. No The Office
   V2, use os agentes canônicos em `agents/<setor>/AGENT.md`. Aguarde e integre os
   resultados antes de concluir.

   Não simule delegação, revisão independente, aprovação ou parecer. Se o agente
   ou a capacidade de delegação não estiver disponível, informe isso e marque a
   revisão como pendente. Cada agente só atesta evidência do próprio domínio.
   Delegar não muda escopo, gates humanos, critérios de aceite ou condições de
   parada, nem autoriza escrita externa, merge, deploy ou operação privilegiada.
   <!-- the-office-v2:agent-routing:end -->
   ~~~~

   Se o arquivo global ou o mecanismo de delegação não estiver acessível, não
   invente um caminho/configuração alternativo; registre AGENTS_GLOBAL_RULE e
   AGENT_DISPATCH como USER_ACTION_REQUIRED ou UNKNOWN, com instrução específica.
   Perfis declarados, `multi_agent = true` ou diretórios presentes não comprovam
   que um agente foi invocado.
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
```

O agente precisa de capacidades reais de filesystem/terminal ou ferramentas
compatíveis. Este documento não executa a instalação. Em host sem acesso local,
prepare o handoff; a máquina do usuário continua pendente.

## Conferir o resultado

Receba evidência do registro no host, `office.py` respondendo, skills efetivamente
lidas e uma operação segura executada. `AUTH_REQUIRED`, conexão ausente ou
operação não verificada impedem afirmar prontidão daquela capacidade. Consulte [instalação](installation.md)
e [atualização](updating.md). A configuração total é um diagnóstico da máquina;
a preparação de ferramentas permanece seletiva conforme o projeto.

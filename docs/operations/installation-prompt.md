# Prompt de instalação e configuração assistida

Copie o bloco para o agente com acesso à máquina. Substitua os caminhos ou peça
a ele para identificar o workspace aberto. O prompt autoriza preparação local
necessária, sem substituir permissões do host. Não instala todas as stacks.

```text
Instale e configure o The Office V2 nesta máquina para o workspace atual.
Fonte: https://github.com/guilhermedemorais-dev/The-office.git
Distribuição para aceitação: feat/the-office-v2. Não usar main como se já tivesse V2.

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
4. Use o Environment existente: doctor e prepare --dry-run com repo-root do
   Harness e workspace do cliente. Confira requirements/lockfile e catálogo
   da stack. Use status compatível depois; não repetir diagnóstico completo
   antes de cada Task. Python 3.11+ é o mínimo do Environment; Node só se preciso.
5. Autorizo preparar ferramentas oficiais necessárias à stack/tarefa aprovada,
   em escopo local compatível, reutilizando gestores e lockfiles. Mostre/registre
   o plano concreto e use o mecanismo de aprovação das ações do Environment.
   Não instalar todas as ferramentas, frameworks, MCPs, Redis, Docker ou bancos.
   Não migrar stack, criar serviços, mudar produção ou remover instalações.
6. Para ações privilegiadas, mudança material ou autenticação que exige pessoa,
   use o mecanismo legítimo do host e explique o bloqueio. Não cole segredos no
   chat/arquivos versionados. Ofereça MCPs opcionais só se houver necessidade;
   reutilize preferências e permissões já registradas.
7. Verifique cada ação executada. Rode rotas e checks pertinentes; valide no
   host real se a V2 é reconhecida e usada. Teste uma demanda descartável pequena
   sem merge/deploy; plano gerado sozinho não é ativação nem execução da skill.
8. Se o projeto cliente adotou Portal, siga docs/operations/client-portal.md:
   busque a origem fixada, revise plano e prepare em docs/portal/ do CLIENTE,
   preserve customizações e vincule à home de docs. Não iniciar backend,
   containers, OAuth ou publicação apenas para copiar o template.
9. Entregue revisão da fonte e da cópia ativa, host/SO, ações/versões/escopos,
   verificações realizadas, localização privada do estado, limitações e como
   atualizar. Marque explicitamente o que ficou sem validação. Não merge/deploy.
```

O agente precisa de capacidades reais de filesystem/terminal ou ferramentas
compatíveis. Este documento não executa a instalação. Em host sem acesso local,
prepare o handoff; a máquina do usuário continua pendente.

## Conferir o resultado

Receba evidência do registro no host, `office.py` respondendo, skills efetivamente
lidas e uma operação segura executada. Estado AUTH_REQUIRED não significa pronto;
um MCP catalogado não comprova conexão. Consulte [instalação](installation.md)
e [atualização](updating.md). A configuração total é um diagnóstico da máquina;
a preparação de ferramentas permanece seletiva conforme o projeto.

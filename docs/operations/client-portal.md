# Buscar o Portal do Cliente para docs

Responsáveis: Orquestração define o projeto/destino; DevOps prepara o template;
Documentação mantém artigos; Governança/métricas prepara relatórios. Esta regra
vale para o projeto cliente, sem instalar o portal dentro do Harness.

## Quando preparar

No onboarding/organização de um projeto que usa o Portal, registre a decisão uma
vez e busque a revisão aprovada. O proprietário já definiu `docs/portal/` como
destino. Não perguntar novamente sobre esse caminho, nem buscar uma cópia nova
em cada Task. Em manutenção de um projeto que não adotou Portal, não introduzir
infraestrutura por associação. Reutilizar o que já estiver instalado e compatível.

## Buscar e fixar a origem

Origem definida: https://github.com/guilhermedemorais-dev/portal-clientes.git .
Revisão inspecionada: `82226fbb2385639d7812b2de929b435e6480fbbc`.
Em uma pasta de ferramentas separada do cliente, usando Git já disponível:

```sh
git clone https://github.com/guilhermedemorais-dev/portal-clientes.git portal-clientes-source
git -C portal-clientes-source checkout --detach 82226fbb2385639d7812b2de929b435e6480fbbc
```

`portal-clientes-source` é exemplo de pasta nova: se existir, inspecione remoto,
branch e alterações antes de atualizar; não sobrescreva. Para uma versão nova,
revise diff, interfaces e testes e registre o novo commit antes do uso.
O cliente precisa ser um checkout Git existente. Confira a raiz correta e as
instruções da origem antes de executar scripts; não instalar dependências ainda.

## Planejar e aplicar a cópia

Com caminhos reais da máquina:

```sh
node /ferramentas/portal-clientes-source/scripts/sync-template.mjs --project=/projetos/cliente
node /ferramentas/portal-clientes-source/scripts/sync-template.mjs --project=/projetos/cliente --apply
```

A primeira chamada imprime o plano sem escrever. Revise add/update/preserve/
conflict e aplique o plano compatível dentro do escopo autorizado. A segunda
prepara arquivos em `/projetos/cliente/docs/portal/`. Não copia `.git`, segredos,
`node_modules`, banco ou evidências privadas. O manifesto local de hashes mantém
proveniência; não altere seus hashes para forçar uma atualização.

Se houver conflito, preserve a cópia e faça merge revisado. O script não apaga
arquivos obsoletos. A allowlist da revisão atual não inclui todos os arquivos de
operação: consulte [adapter](../../library/integrations/client-portal.md) e confira
o resultado antes de afirmar que a instalação está completa.

## Integrar à página docs

Crie ou atualize o link "Portal do Cliente" na home/sidebar **existente** da
documentação do cliente, usando a rota real do renderer/build do projeto. Mantenha
manuais, documentação técnica e relatórios no mesmo projeto, com acesso adequado.
Diretório em disco não garante URL `/docs/portal/`; confira base path e navegação.
Não substitua a home de docs nem crie um segundo site quando já houver renderer.

Configure apenas metadados públicos no frontend. Backend, banco existente, OAuth,
ACL, armazenamento e URL da API seguem a arquitetura e autorizações do cliente.
Copiar arquivos não autentica usuário, não publica site e não inicia containers.

## Verificar e registrar

Ensaiado nesta entrega em checkout temporário: 36 arquivos planejados/copiados,
36 inalterados na repetição e uma customização preservada. Os 3 testes próprios
do sincronizador passaram. Isso valida preparação, não produção.

No cliente real, revise diff, execute os checks da versão selecionada, verifique
links/rotas e registre origem, commit, destino e resultado. A Task continua sendo
a fonte de escopo; cada fechamento atualiza os artigos e prepara o relatório.
Sincronização/publicação só é declarada após execução e leitura de retorno reais.

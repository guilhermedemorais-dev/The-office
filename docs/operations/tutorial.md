# Tutorial de utilização do The Office V2

Público: proprietário e desenvolvedor usando um agente com acesso ao checkout.
Este tutorial descreve prompts e comandos implementados; não é prova de aceitação
em qualquer host. Use dados fictícios em ensaios e confira a revisão ativa.

## 1. Preparar o ambiente uma vez

Use o [prompt de instalação](installation-prompt.md). Informe onde está o Harness
e qual é o projeto cliente. Espere diagnóstico, ações selecionadas, evidências e
limitações. Não aceite "instalado" apenas porque o clone terminou.

## 2. Começar produto novo

Exemplo de pedido, a adaptar ao negócio real:

> Use The Office V2 no projeto aberto. Quero um controle de estoque para minha
> operação. Comece por Produto: esclareça usuários, entradas/saídas, concorrência,
> integrações e critérios de sucesso. Consulte o arsenal pertinente do catálogo.
> Prepare PRD e plano por módulos para revisão antes da implementação.

O resultado esperado é contexto/PRD/plano coerentes, não uma stack inventada ou
containers criados prematuramente. Revise escopo e autorize o próximo gate. Se
já há PRD aprovado, forneça o caminho; não reinicie o Discovery.

## 3. Especificar e executar um módulo

> Com o PRD aprovado, especifique este módulo funcional completo. Preserve uma
> Task com microtarefas por disciplina, critérios verificáveis, dependências e
> JSON v2 equivalente à Issue. Não implemente antes da autorização aplicável.

Após aprovação, use o ID/caminho/revisão reais:

> Execute a Task indicada nesta branch. Confira a Issue e o JSON da revisão
> atual, selecione setores/skills necessários e reutilize as ferramentas do projeto.
> Faça as verificações e retorne evidências. Não faça merge nem deploy.

O agente usa o roteador; você pode inspecionar uma seleção real com:

```sh
python scripts/office.py plan ux-design --capability ux-visual-validation
python scripts/office.py plan documentation
python scripts/office.py plan governance --capability delivery-metrics
```

O plano lista arquivos para leitura e decisão; não iniciou especialistas. No
contrato da migração há um exemplo seguro de handoff, que só imprime o plano:

```sh
python scripts/office.py handoff docs/execution/THEOFFICE-V2-001.json --list MT-10/checklist --sector qa --revision 1
```

Isso não autoriza reaproveitar a Task-mestra como contrato de outro software.

## 4. Corrigir algo pequeno ou trabalhar em sistema existente

> Corrija o erro observado neste projeto, reproduzindo-o antes. Preserve a stack e
> as decisões aprovadas. Classifique impacto, selecione somente skills necessárias,
> teste a correção e atualize documentação afetada. Não reinicie o produto.

Para erro de ortografia sem impacto, solicite escopo/check inline. Para bug,
responsividade, dados ou segurança, use os validators aplicáveis; tamanho do diff
não dispensa validação. Quando faltar CLI/referência, setor pesquisa a lacuna.

## 5. Receber documentação e relatório

Confira duas entregas: documentação técnica (contratos, operação, decisões) e
instruções reais de uso (papel, navegação, campos, ações, resultado e recuperação).
N/A precisa de razão. Capturas indisponíveis devem ser declaradas, nunca inventadas.

O responsável usa o [guia de métricas](delivery-report-guide.md). Progresso mede
critérios aceitos / baseline inteiro, com método e denominador explícitos; não
é percentual de tempo gasto. Tutorial pendente impede closure-ready.
O [Portal](client-portal.md) fica no docs do cliente; publicar relatório ou iniciar
backend não acontece apenas porque o template foi preparado.

## 6. Retomar e atualizar

> Retome esta Task usando a revisão atual e o último checkpoint. Informe o que
> tem evidência válida, o que mudou e a próxima ação; não recomece o que já passou.

Se houver regras antigas em ação, confira o bundle/commit realmente ativo no host
antes de adicionar mais instruções. Veja [atualização](updating.md). Um pull no
repositório não garante atualização de uma cópia instalada ou conversa aberta.

## Aceitação manual

- Confirme skills efetivamente lidas, ferramentas reais e resultados reproduzíveis.
- Confira que um recurso catalogado não é tratado como instalado/autenticado.
- Confira que falha/bloqueio não é convertido em PASS para concluir a Task.
- Revise a entrega e seus limites antes de autorizar merge/release separadamente.

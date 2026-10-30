# Prompt de atualização do The Office V2

Use este prompt quando o The Office já estiver instalado ou registrado. Ele não
substitui o [prompt de instalação inicial](installation-prompt.md). Atualizar a
fonte, atualizar a cópia ativa e atualizar adaptadores são ações distintas.

```text
Atualize o The Office V2 já existente neste ambiente, preservando minhas
configurações, projetos e memória. Não faça uma instalação nova por cima.
Fonte esperada: https://github.com/guilhermedemorais-dev/The-office.git
Use a revisão/branch explicitamente solicitada; sem indicação, confira a main
atual e apresente a revisão candidata e o diff antes de alterar a cópia ativa.

1. Identifique host e versão reais, SO/runtime, workspace cliente, checkout fonte
   e bundle ativo, inclusive caminho, remoto, branch, commit e git status.
   Não presuma que checkout e plugin/cache ativo são a mesma cópia. WSL é Linux.
2. Leia AGENTS.md, política V2 e procedimento de atualização da origem atual.
   Selecione Ambiente e as skills/referências necessárias, sem repetir discovery
   do produto ou carregar todos os setores. Reutilize autorizações já concedidas.
3. Registre revisão anterior e candidata. Faça fetch apenas do remoto correto,
   revise commits/diff, skills, scripts, dependências e migrações. Preserve mudanças
   locais e arquivos não versionados. Nunca force, reset --hard, clean ou remova
   customizações para permitir o update. Divergência exige reconciliação limitada.
4. Confira o destino e faça backup recuperável dos arquivos de configuração e
   adaptadores afetados antes de trocá-los. Não inclua credenciais em logs/relatórios.
   Preserve configurações de providers/modelos/MCPs e overrides do usuário.
5. Para Graphiti/memória existente, identifique separadamente banco, ledger,
   configuração e versão efetiva. Preserve-os e seus backups. Não recrie banco,
   apague fatos, reimporte histórico, altere group_id/projeto, modelo de embeddings
   ou execute migração só porque o código mudou. Se a atualização afetar dados,
   prepare plano específico com validação/backup/rollback e o gate aplicável.
6. Na fonte revisada, rode os checks relevantes da versão e os testes necessários.
   No bundle V2, confira build_skill_routes.py --check, preservação e regressões.
   Não regenere fontes para ocultar drift. Falhas não viram PASS por serem antigas;
   registre baseline e bloqueie somente a capacidade afetada quando possível.
7. Atualize a fonte e a cópia ativa pelo mecanismo compatível com o host, sem
   confundir fast-forward local autorizado com merge de PR ou implantação.
   Não altere main remota, não faça merge de PR nem deploy.
8. No OpenCode, use scripts/register_opencode_agents.py plan/check com --bundle-root
   e --project-root absolutos da instalação real. Revise os caminhos e aplique só
   as mudanças gerenciadas aprovadas; rode check novamente. Preserve opencode.json,
   providers/modelos e MCPs. Config JSONC ou colisões customizadas exigem revisão,
   não sobrescrita. Não use scratch como raiz permanente nem habilite Graphiti bruto.
9. No Codex, use o Setup/procedimento e o helper de perfis documentados na versão
   ativa, com os destinos explícitos. Preserve regras/overrides globais e faça
   backup; conflito não autoriza substituir o arquivo inteiro. Em outros hosts,
   siga o adaptador nativo e não escreva em configurações de outro produto.
10. Recarregue apenas quando o host exigir e verifique a revisão realmente usada.
    Execute seleção e delegação pequenas em fixture, com recibo real. Configuração
    aceita não comprova agente invocado; health/ACK não comprova memória persistida.
    Teste recuperação de uma decisão sintética se memória estiver configurada e
    autorizada; não use dados reais de cliente como smoke test.
11. Preserve o retriever atual e fontes obrigatórias. Em falha da memória, relate
    degradação e use fallback local; não silencie conflito de fontes nem restaure
    decisão revogada. Atualize Portal de clientes somente quando adotado e dentro
    do escopo solicitado, em operação separada da atualização do Harness.
12. Entregue revisão anterior/nova/ativa, arquivos alterados, backup e recuperação,
    testes/exit codes, conflitos e pendências. Separe reconhecimento do plugin,
    ferramentas disponíveis, registro, autenticação, dispatch real e leitura/escrita
    da memória. O não observado fica UNKNOWN/NOT_VALIDATED. Não declare instalação
    completa, economia de tokens ou homologação nativa sem evidência real.
```

Procedimentos detalhados: [atualização](updating.md),
[OpenCode](opencode.md) e [memória](../../integrations/memory/README.md).

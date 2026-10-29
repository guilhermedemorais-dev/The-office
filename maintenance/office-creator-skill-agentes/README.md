# Office Creator Skill & Agentes

Identificador: `office-creator-skill-agentes`

**Uso:** manutenção manual, isolada, de skills/agentes e seus geradores do The Office.

**Não é** a `skill-creator` global de uso avulso. Não participa do orquestrador, do DAG dos 44 skills, nem dos perfis de agentes normais.

A entrada principal fica em `maintenance/office-creator-skill-agentes/SKILL.md`, deliberadamente fora de `skills/`, para evitar descoberta como skill de trabalho ordinário. Em Codex Desktop, invoque-a explicitamente informando o caminho e pedido de manutenção; caso o host não suporte carregamento a partir de `maintenance/`, mantenha a separação e use uma entrada manual com caminho explícito, sem inserir no roteador normal.

Exemplo: "Use as instruções em maintenance/office-creator-skill-agentes/SKILL.md para corrigir os gatilhos da skill de QA. Faça testes, commit e push em branch isolada. Não faça merge."

A Skill Creator V2 global pode fornecer a metodologia, mediante verificação de versão, mas deve permanecer independente.

Para uso cross-machine, publicar a branch e revisar PR. A instalação de manutenção **não** dispara atualizações de clientes ou outras máquinas por si só; o Update Checker é um componente separado.

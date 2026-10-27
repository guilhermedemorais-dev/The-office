# Memória temporal de projeto com Graphiti

Status: implementação autorizada pelo usuário em 27/10/2026; aceite/release separados.

Parent: `docs/specs/the-office-v2.md`, extensão solicitada nesta sessão.

## Requisitos

- REQ-01: Implementar adapter local opt-in com projeto explícito, proveniência de fonte/revisão/hash e Graphiti SDK lazy; sem ingestão real automática.
- REQ-02: Journal durável deve distinguir pendência/falha/persistência, suportar replay controlado e prevenir duplicação lógica por fonte/revisão/hash.
- REQ-03: Consulta deve limitar resultados, validar validade temporal e origem e nunca prevalecer sobre required_sources atuais.
- REQ-04: Rejeitar secrets e escapes de caminho; namespace de projeto não é autenticação nem isolamento multiusuário; não expor MCP cru.
- REQ-05: Preservar Potpie/local como recuperação de código e fallback; documentar instalação opcional, pin de dependências, backup, remoção e limites.

## Banco

Journal local e grafo externo opcional; nenhum dado real ingerido nesta entrega.

## API/Backend

Helpers locais e contratos/procedimentos no escopo; nenhuma API pública nova.

## Frontend/UI

N/A: CLI e procedimentos textuais.

## Testes

Testes positivos, negativos, preservação de escopo e regressão do repositório conforme contrato.

## Segurança

Preservar paths, secrets e configurações; revisão formal de Security independente permanece necessária.

## Observabilidade/logs

Diagnósticos sanitizados, revisões e resultados; sem payload de credenciais.

## Decisões pendentes

Host real, providers e custos não observados. Não impedem implementação/testes em fixture.

## Riscos

Registro/fixture não comprova integração operacional; não inferir economia de tokens.

## Critérios de aceite

AC-01..AC-05 correspondem aos REQ-01..REQ-05. Detalhes e comandos em `docs/execution/OFFICE-MEMORY-001.json`.

# Inventário comportamental e cobertura de specs

Status: implementação autorizada pelo usuário em 27/10/2026; aceite/release separados.

Parent: `docs/specs/the-office-v2.md`, extensão solicitada nesta sessão.

## Requisitos

- REQ-01: Integrar inventário de telas/fluxos/fontes nas skills existentes de Produto, REA e SDD sem substituir REA ou criar onze skills paralelas.
- REQ-02: Exigir fonte e revisão, OBSERVED/INFERRED/UNKNOWN, IDs existentes de requisito/aceite e separação entre declarado e verificado.
- REQ-03: Cobertura deve bloquear obrigatório ausente e exclusão sem aprovação, mesmo com score alto; rejeitar evidência antiga/inválida.
- REQ-04: Pesquisa de feedback é hipótese com fonte/idioma/contexto, não requisito aprovado nem gate por keyword.
- REQ-05: Preservar fontes V1 e usar overlays V2 regeneráveis e referências sob demanda.

## Banco

N/A: nenhum banco de aplicação alterado.

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

AC-01..AC-05 correspondem aos REQ-01..REQ-05. Detalhes e comandos em `docs/execution/OFFICE-SPECS-001.json`.

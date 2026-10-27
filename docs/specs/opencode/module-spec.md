# OpenCode e prompts separados de instalação e atualização

Status: implementação autorizada pelo usuário em 27/10/2026; aceite/release separados.

Parent: `docs/specs/the-office-v2.md`, extensão solicitada nesta sessão.

## Requisitos

- REQ-01: Gerar perfis OpenCode a partir dos contratos canônicos existentes, com orquestrador primário e especialistas como subagents.
- REQ-02: Oferecer plan/check/apply com destino explícito, preservação de configuração e bloqueio de conflitos, backup e idempotência.
- REQ-03: Resolver descoberta de skills e referências do bundle estável sem impor modelos, providers, MCPs ou credenciais.
- REQ-04: Manter prompts de instalação e atualização independentes, ambos atuais; atualização deve preservar customizações e memória.
- REQ-05: Validar em fixtures locais; não afirmar execução real de OpenCode sem invocação no host alvo.

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

AC-01..AC-05 correspondem aos REQ-01..REQ-05. Detalhes e comandos em `docs/execution/OFFICE-OPENCODE-001.json`.

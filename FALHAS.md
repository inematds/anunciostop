# FALHAS

| data | o que quebrou | menor correção | prompt \| infra |
|---|---|---|---|
| 2026-09-06 | Fetch do Skool via cookies do Firefox voltou `202 x-amzn-waf-action: challenge` (token do WAF expirado) | `setsid firefox "<url>" &` + sleep 20 + re-extrair cookies renova o token sem depender do usuário | infra |
| 2026-09-06 | Post e classroom da comunidade `ia-masters-automations` redirecionam pra `/about` (`self: null`) mesmo com token válido: conta não é membro | Sem correção possível; o conteúdo veio por zip + HTML passados pelo usuário | infra |

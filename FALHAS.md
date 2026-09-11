# FALHAS

| data | o que quebrou | menor correção | prompt \| infra |
|---|---|---|---|
| 2026-09-11 | Hero e capa saíram com o título gravado dentro da foto e escrito errado ("Anúnciios"): o `gerar-capa.cjs` monta a cena com `cenaFor(cat, title)`, então as palavras do título entram no prompt e o flux2-klein as renderiza como texto, apesar do "NO TEXT" no positivo | Passar `--cena` explícita, sem nenhuma palavra do título; imagens do guia geradas à parte, sem texto | prompt |
| 2026-09-06 | Fetch do Skool via cookies do Firefox voltou `202 x-amzn-waf-action: challenge` (token do WAF expirado) | `setsid firefox "<url>" &` + sleep 20 + re-extrair cookies renova o token sem depender do usuário | infra |
| 2026-09-06 | Post e classroom da comunidade `ia-masters-automations` redirecionam pra `/about` (`self: null`) mesmo com token válido: conta não é membro | Sem correção possível; o conteúdo veio por zip + HTML passados pelo usuário | infra |

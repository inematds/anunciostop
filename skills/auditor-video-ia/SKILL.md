---
name: auditor-video-ia
description: >
  Audita prompts, gerações e anúncios criados com IA antes de gastar mais ou publicar. Usar quando
  alguém disser "/auditor-video-ia", "revisa esse prompt", "audita esse vídeo", "regenero?", "dá pra
  consertar?", "controle de qualidade", "preflight", "postflight", "deriva de identidade", "falha
  de mãos/lip-sync", "confere o CTA/produto/claims" ou precisar decidir entre conservar, editar,
  estender, salvar na montagem ou regenerar. Valida a interface concreta, evidência, consentimento,
  transparência, custo e aprendizado do teste; não publica nem gasta crédito.
---

# /auditor-video-ia — Preflight, postflight e decisão

Separar falhas técnicas, falhas de negócio e riscos de publicação. Terminar com uma ação concreta,
não com uma nota estética.

## Entradas

Aceitar dois modos:

### Preflight

- handoff ou brief;
- prompt compilado;
- modelo, provedor e interface;
- duração e formato;
- assets / bindings;
- custo por tentativa.

### Postflight

Tudo o de cima mais:

- arquivo de vídeo;
- prompt exato e versão;
- resultado esperado;
- número da tentativa;
- se existir, métrica ou feedback comercial.

Pedir só o imprescindível que faltar. Se não há arquivo, fazer preflight e marcar o postflight como
pendente; não fingir uma inspeção visual.

## Passo 1 — Reconstruir o contrato

Ler o dossiê do `/video-ia` (e o roteiro aprovado, se veio de outro lugar). Extrair:

- tese, público, mecanismo e CTA;
- claims e fontes;
- identidade, produto e permissões;
- rota de produção e adaptador;
- variável do teste e elementos congelados;
- riscos esperados.

Se a geração mudou mais de uma variável, registrar que o aprendizado causal ficou contaminado.

## Passo 2 — Preflight

Ler `references/preflight.md` e aplicar só o perfil da interface declarada.

Conferir:

1. roteiro, claim, CTA e duração;
2. consentimento e bindings;
3. bytes ou caracteres;
4. timeline, ações, câmera, diálogo e pronúncia;
5. estados de continuidade;
6. produto e texto crítico;
7. custo, tentativas e variável do teste;
8. disclosure previsto.

Quando o prompt existe como arquivo, rodar o checador mecânico (colchetes, tamanho, planos sem
diálogo, timestamps, sotaque):

```bash
python3 ~/.claude/skills/auditor-video-ia/scripts/checa-prompt.py prompt.txt --interface seedance25 --duracao 30
python3 ~/.claude/skills/auditor-video-ia/scripts/checa-prompt.py prompt.txt --interface dreamina --duracao 30
python3 ~/.claude/skills/auditor-video-ia/scripts/checa-prompt.py prompt.txt --interface agnes
```

Não aplicar as regras de uma interface a outra.

## Passo 3 — Postflight técnico

Ler `references/postflight.md`.

### Arquivo

Inspecionar duração, resolução, fps, bitrate, codec e áudio com `ffprobe`. Comparar com o pedido e
registrar o que foi baixado de verdade (a Agnes, por exemplo, devolve resolução diferente da
declarada no JSON).

### Imagem

Revisar o início, o fim, os cortes e frames intermediários. Conferir:

- identidade e figurino;
- mãos, boca, dentes, olhos e cabelo;
- produto, embalagem e texto;
- geometria, reflexos e duplicações;
- continuidade, física e câmera;
- artefatos, morphing e fundos.

### Áudio

Ouvir e revisar:

- voz desde o começo previsto;
- lip-sync;
- sotaque e pronúncia;
- buracos centrais e cauda;
- ambiente, efeitos e música;
- CTA completo.

Não confundir cauda recortável com um silêncio central que quebra o anúncio.

## Passo 4 — Postflight de negócio

Conferir:

- se os primeiros segundos identificam o público ou a situação;
- se o mecanismo se entende sem explicar o prompt;
- se a prova aparece e é legível;
- se o CTA se ouve e se compreende;
- se produto, preço, resultado e depoimento são reais;
- se o vídeo poderia ser de qualquer marca;
- se a variante muda só o declarado.

Ver o vídeo sem som e em tamanho de celular. Um clipe tecnicamente perfeito pode reprovar o anúncio.

## Passo 5 — Transparência e publicação

Ler `references/publicacao-e-transparencia.md`.

Marcar como bloqueante:

- cara ou voz sem consentimento;
- depoimento, resultado ou evento inventado;
- produto diferente do real;
- claim crítico sem evidência;
- ausência de disclosure quando a peça realista pode ser confundida com gravação autêntica;
- texto crítico ilegível ou incorreto.

Não substitui assessoria jurídica. Recomendar revisar as opções atuais de disclosure da plataforma.

## Passo 6 — Classificar a reparação

Ler `references/hierarquia-de-reparacao.md` e escolher uma só decisão principal:

1. **Conservar:** passa nos gates técnicos, comerciais e de publicação.
2. **Editar localmente:** clipe bom com um defeito isolado e preservável.
3. **Estender:** o primeiro clipe funciona e o estado final permite continuidade.
4. **Salvar na montagem:** há módulos úteis e o conserto não falseia o resultado.
5. **Regenerar:** identidade, lip-sync, mecanismo, continuidade ou claim falham de forma global.

Não regenerar tudo por um objeto local. Não tentar salvar na montagem um mecanismo que não se entende.

## Entrega

Usar `assets/modelo-auditoria-video-ia.md`. Incluir:

- veredito executivo;
- bloqueantes;
- evidência observada;
- decisão de reparação;
- prompt de correção quando se aplica;
- custo da próxima ação;
- aprendizado do teste;
- linha pro `assets/registro-experimentos.csv`.

O veredito tem que ser operacional:

```markdown
DECISÃO: EDITAR LOCALMENTE
Porque: a identidade, o roteiro e o ritmo funcionam; só falha o produto entre 00:11–00:13.
Ação: substituir o produto nessa faixa e preservar câmera, atuação, luz e áudio.
Não tocar: hook, cara, timing, voz e CTA.
```

## Regras duras

- Não afirmar que viu um vídeo se ele não está disponível.
- Não aplicar regras de uma interface a outra.
- Não aprovar por nota média se existe um bloqueante.
- Não publicar nem marcar como pronto com claims ou permissões pendentes.
- Não modificar o conceito durante uma reparação local.
- Não mudar mais de uma variável do teste.
- Não gastar crédito nem executar regeneração sem permissão.
- Guardar rastreabilidade de prompt, versão, provedor, custo e decisão.

---
name: espiona-ads
description: >
  Espiona os anúncios de uma conta na Biblioteca de Anúncios da Meta e faz engenharia reversa da
  fórmula dela: extrai todos os anúncios ativos com copy, datas e URLs de vídeo em HD, ranqueia por
  sinais de que estão funcionando (dias em circulação e nº de variantes vivas), baixa os vídeos,
  mede (cortes de cena, palavras por minuto), transcreve com Whisper, analisa frame a frame com
  subagentes, e devolve um playbook acionável: banco de hooks literais, esqueleto persuasivo
  minutado, veredito sobre se estão usando IA generativa (com evidência, não a olho), e o que é
  transplantável. USAR SEMPRE que o usuário disser "/espiona-ads", "espiona esses anúncios",
  "analisa os anúncios de [marca]", "olha o que a concorrência está fazendo na Meta", "que anúncios
  X tem", "biblioteca de anúncios de", "ads library de", "que criativos ela usa", "como são os
  anúncios do meu concorrente", ou colar uma URL de facebook.com/ads/library. Também se perguntar
  "isso é feito com IA?" sobre anúncios de outra marca. NÃO é pra analisar o DESEMPENHO dos
  anúncios próprios de quem usa a skill (pra isso precisa ler os dados exportados do Gerenciador de
  Anúncios) nem pra editar vídeo.
---

# /espiona-ads — Engenharia reversa dos anúncios de uma conta

Você pega uma conta que está anunciando na Meta e sai com a fórmula dela desmontada: o que dizem
nos primeiros 3 segundos, como estruturam a persuasão, em que ritmo cortam, e o que disso tudo é
copiável. Tudo de fontes públicas, sem API paga e sem login.

## O que você precisa
- O **navegador integrado**: a extensão Claude in Chrome (`mcp__claude-in-chrome__*`:
  `navigate`, `javascript_tool`, `get_page_text`). Alternativa: a skill `agent-browser`. A Meta
  bloqueia `curl` com um challenge anti-bot; o navegador passa sozinho.
- `ffmpeg`, `ffprobe`, `curl`.
- `GROQ_API_KEY` pra transcrição Whisper. O script procura, nesta ordem: variável de ambiente →
  `.env` do projeto → `~/projetos/openpcbotv2/.env` → `~/projetos/wifi/.env`. Nunca imprime o valor.
- Diretório de trabalho no **scratchpad** da sessão (os vídeos pesam; não vão pro projeto).

## Entrada
Uma URL da Biblioteca de Anúncios da Meta, ou o nome de uma marca. Se o usuário dá só o nome,
busque a página na Biblioteca e **confirme com ele qual é** antes de seguir: há muitas páginas com
nomes parecidos.

Pergunte só se não se deduz: **país** (por padrão BR) e **só ativos ou também histórico** (por
padrão só ativos: os inativos não dizem nada sobre o que funciona hoje).

---

## FASE 1 — Extração (você faz, não delegue: são 3 chamadas)

1. Abra a URL com `navigate`. A Biblioteca é pública, não precisa de login.
2. O payload completo do GraphQL vem **embutido na página**, no único
   `<script type="application/json">` que contém `ad_archive_id`. Execute `scripts/extrai.js` com
   `javascript_tool`: devolve `window.__ADS` populado e um resumo.
3. Tire de `window.__ADS`, em chamadas separadas pra não estourar seu contexto:
   - primeiro a **tabela resumo** (id, datas, dias, variantes, tipo, CTA, título, primeira linha do copy)
   - depois o **copy completo** dos que tiverem copy
   - por último as **URLs HD**, e só dos que você vai baixar (ocupam ~1,5 KB cada)

**Antes de baixar qualquer coisa, deduplique por asset de vídeo.** Vários anúncios podem
compartilhar a mesma criação. O `scripts/extrai.js` decodifica o parâmetro `efg` (base64) de cada
URL e tira `xpv_asset_id` e `duration_s`. Agrupe por `xpv_asset_id`: se 16 anúncios compartilham o
asset, é UM vídeo, não 16.

**Paginação:** a página traz ~30 anúncios. Se a conta tem mais, o resto chega por GraphQL ao rolar
e o scroll programático nem sempre dispara. Se faltarem, diga explicitamente no relatório ("N de M
capturados") em vez de fingir cobertura completa.

## FASE 2 — Ranking

A Biblioteca **não publica gasto, impressões nem CTR** de anúncios comerciais. Você nunca vai saber
qual converte. Infere-se com três proxies, e tem que dizer isso claramente no relatório:

1. **Dias em circulação** (`start_date` → hoje). O mais forte. Um anúncio vivo há 4 meses é um
   anúncio que estão pagando.
2. **`collation_count`**: variantes vivas da mesma criação. Se escalam um ângulo, ele ganha.
3. **Repetição de estrutura** entre criações diferentes = fórmula vencedora replicada.

Extra na UE: o botão "Transparência da UE" dá alcance por país/idade/gênero, mas exige uma consulta
por anúncio. Use só se o usuário pedir. Pra contas brasileiras não existe.

Selecione **12-18 vídeos** pra análise profunda: todos os que tiverem copy próprio, mais uma
amostra de durações variadas de cada cluster que detectar. Diga quais deixou de fora e por quê.

## FASE 3 — Processo mecânico (script, sem LLM)

Baixe os vídeos em paralelo com `curl` e passe cada um por `scripts/processa.sh`, que produz em
`analise/<id>/`:
- `meta.txt`: duração, fps, resolução, nº de cortes
- `cortes.txt`: timestamp de cada corte de cena (ffmpeg, limiar 0.15)
- `transcript.txt`: transcrição com timestamps (Whisper large-v3 via Groq)
- `fala.txt`: palavras, duração de fala e **ppm**
- `frames/`: hook denso (0 a 4 s a cada 0,6 s) + corpo a cada 4 s, escalados a 360 px

Rode 6 em paralelo no máximo. **Não gaste subagente nisso**: é mecânico e um LLM não acrescenta.

⚠️ O detector de cortes precisa de `-loglevel info`. Com `-v error` o ffmpeg engole a saída do
`showinfo` e devolve 0 cortes em todos os vídeos, silenciosamente.

## FASE 4 — Análise com subagentes

**Anuncie ao usuário quantos subagentes vai lançar e pra quê, e espere o OK.** Modelo `sonnet`.
Distribua **3 vídeos por subagente**: o spawn tem custo e 3 aproveita bem o turno.

Use `references/prompt-subagente.md` como modelo. Cada subagente lê a ficha de contexto, o
transcript, os cortes, **olha todos os frames com Read**, e escreve `analise/<id>/ficha.md`. Que
devolva só um resumo de 5 linhas: o relatório vai pro disco, não pro seu contexto.

Regras que têm que ir sim ou sim no prompt do subagente:
- Veredito de IA **com nível de confiança e evidência visual concreta**. Proibido dizer "parece
  IA" sem apontar o artefato. Se é gravação humana real, que diga.
- "Não determinável com os frames disponíveis" em vez de inventar.
- Timestamps reais do transcript na estrutura minutada.

## FASE 5 — Contexto do funil (você)

Enquanto os subagentes trabalham, abra a **landing de destino** com o navegador e desmonte: hero,
formulário (onde está, quantos passos, que atrito declara), seções em ordem, prova social,
garantia, escassez, preço. `WebFetch` não serve se é uma SPA: use `get_page_text`.

**Procure incoerências entre anúncio e landing**: garantias diferentes, números que não batem,
promessas que mudam. Costumam existir e são munição.

## FASE 6 — Síntese (você, e só você)

Leia as fichas dos vencedores (não todas: gasta contexto) e tire os hooks literais de todos os
transcripts com um loop de bash. Escreva o relatório em
`anuncios/referencias-criativas/espionagem-<marca>-<AAAA-MM-DD>.md` com esta estrutura:

0. **O veredito que quebra a premissa**: IA ou não? Com evidência agregada.
1. **Os clusters de campanha**: tabela comparativa. Quase sempre há mais de um.
2. **Como iteram**: o que congelam e o que variam entre versões.
3. **Ritmo, medido**: tabela de duração / cortes / corte médio / ppm.
4. **Banco de hooks**: transcrição **literal** dos primeiros segundos de todos, agrupados por
   mecanismo. É o mais valioso do relatório.
5. **A fórmula do vencedor, minutada**: tabela t/o que acontece/função persuasiva, e o esqueleto
   abstraído em N movimentos.
6. **Incoerências que estão pagando.**
7. **O que é transplantável, o que com cuidado, e o que NÃO**: o último bloco é obrigatório:
   marque explicitamente o que bate com os valores da marca (inflar números, garantias falsas,
   fumaça). Copia-se a estrutura, nunca a mentira.

---

## Erros que já foram cometidos (não repita)
- `curl` direto em `facebook.com/ads/library` → **403 com challenge anti-bot**. Use o navegador.
- O endpoint `/ads/library/async/search_ads/` está **retirado** (404). Os tutoriais que o
  mencionam estão desatualizados.
- A **API oficial** da Biblioteca de Anúncios só devolve anúncios políticos e de temas sociais.
  Pra anúncios comerciais não serve. Não perca tempo pedindo token.
- O campo `contains_digital_created_media` existe mas **quase sempre vem `false`**: é declaração
  do anunciante, não detector. IA se detecta olhando frames.
- Não despeje as URLs HD de 30 anúncios no seu contexto de uma vez: ~1,5 KB cada.

## Custo
Zero. Sem API paga, sem login, sem scraper de terceiros. Só o Whisper da Groq, que é centavos. Se um
dia precisar escalar pra dezenas de contas, as alternativas são serviços de scraping pagos, mas
pra uma conta não precisa.

## O que esta skill NÃO faz
Não mede desempenho real (ninguém consegue de fora), não baixa anúncios inativos por padrão, não
gera os anúncios novos.

**O encadeamento natural:** `/espiona-ads` tira o playbook → **`/video-ia`** converte o ângulo que
você escolher num menu de conceitos com roteiro, e o escolhido em shot list, ficha de personagem,
modelo e prompts técnicos → **`/auditor-video-ia`** revisa prompt e gerações e decide se se
conservam, se salvam na montagem ou se regeneram → **`/anuncio-edita`** monta a peça final e
masteriza pra Meta.

Uma nuance:
- Se o bruto é **gravado pelo apresentador com câmera** em vez de gerado com IA, a montagem é
  `reel-edita-inema`, não `/anuncio-edita`.

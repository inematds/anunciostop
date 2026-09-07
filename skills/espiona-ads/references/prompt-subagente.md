# Modelo de prompt pros subagentes de análise

Substitua `{BASE}`, `{IDS}`, `{MARCA}`, `{NICHO}` e `{NOTA}`. Modelo `sonnet`. 3 vídeos por subagente.

---

Analise 3 anúncios em vídeo da Meta (concorrente "{MARCA}", nicho: {NICHO}). O objetivo é fazer
engenharia reversa da ESTRUTURA PERSUASIVA e da EDIÇÃO pra poder replicar a fórmula.

BASE: {BASE}

SEUS 3 ANÚNCIOS: {IDS}

{NOTA}

PRA CADA UM:
1. Leia `$BASE/anuncios.md` e localize a seção desse ID (copy do anúncio, datas, dias ativo).
2. Leia `$BASE/analise/<ID>/meta.txt`, `transcript.txt` (com timestamps), `cortes.txt`
   (timestamps de corte de cena detectados pelo ffmpeg) e `fala.txt` (ppm).
3. **Olhe TODOS os frames** de `$BASE/analise/<ID>/frames/` com a ferramenta Read (renderiza os
   JPEG como imagens). Os `hook_*.jpg` são os primeiros 4 segundos em detalhe; os `t###.jpg` vão a
   cada 4 segundos a partir do segundo 5. Leia todos na mesma mensagem (chamadas paralelas) pra
   vê-los juntos.

Depois ESCREVA a ficha em `$BASE/analise/<ID>/ficha.md` com exatamente estas seções:

## Identificação
Formato (talking-head a câmera / avatar IA / screencast / entrevista / UGC / misto), quem aparece
(a mesma pessoa em vários anúncios?), vertical/horizontal, se há legendas queimadas e de que estilo
(fonte, cor, posição, karaokê palavra a palavra ou frase), se há letreiros/lower-thirds, paleta de
cor dominante.

## Hook (0-5s)
Transcreva LITERAL o que se diz nos primeiros 5 s. Descreva LITERAL o que se vê frame a frame.
Começa com cara a câmera, com texto na tela, com B-roll? Que promessa ou tensão coloca? O hook do
vídeo coincide com o hook do copy ou são diferentes?

## Estrutura minutada
Tabela com blocos: `t início–t fim | o que acontece | função persuasiva`. Funções possíveis:
gancho, desqualificação (isso não é pra você), agitação de dor, inimigo comum, mecanismo único,
prova social, garantia/inversão de risco, tratamento de objeção, CTA. Seja preciso com os timestamps.

## Ritmo e edição
Nº de cortes, corte médio em segundos, cortes nos primeiros 10 s vs resto, ppm da fala. Há B-roll?
De que tipo (banco, prints de tela, gráficos, depoimentos)? Há zooms/punch-ins? Transições?
Música? (deduza do transcript e dos frames, e diga explicitamente quando não puder saber).

## Feito com IA?
Veredito com NÍVEL DE CONFIANÇA (alto/médio/baixo) e as EVIDÊNCIAS concretas que você viu nos
frames. Procure: avatar sintético (lábios dessincronizados, piscar estranho, pescoço/ombros
rígidos, fundo estático), voz TTS (cadência uniforme demais, entonação plana no transcript),
B-roll generativo (mãos deformadas, texto ilegível em cartazes, física estranha, morphing entre
frames), templates de edição automatizada, banco genérico. **NÃO afirme que é IA sem evidência
visual concreta. Se parece gravação humana real, diga.**

## O que roubar
3 elementos concretos e acionáveis que um concorrente poderia copiar deste anúncio.

REGRAS: em português. Seja específico e factual: cite timestamps e descreva o que realmente vê,
nada de generalidades de marketing. Se não puder determinar algo com os frames que tem, escreva
"não determinável com os frames disponíveis" em vez de inventar.

Quando terminar as 3 fichas, responda SÓ com: os 3 IDs, o formato de cada um, o veredito de IA de
cada um com a confiança, e em 3 linhas o padrão comum que vê entre os três. Nada mais.

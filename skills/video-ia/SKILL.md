---
name: video-ia
description: >
  Converte uma ideia de anúncio em vídeo gerado com IA, passo a passo: faz cinco perguntas, propõe
  dez conceitos com roteiro, e dos que você escolher escreve um Markdown por vídeo com o essencial
  pra gerar: as imagens que precisam ser criadas antes, o roteiro se você for gravar a voz, o que
  subir e em que ordem, e o prompt pronto pra colar. Usar quando alguém disser "/video-ia", "faz um
  anúncio com IA", "quero um vídeo com IA de…", "me dá ideias de vídeo pra…", "prompt pra
  Seedance / Agnes / Dreamina", "ficha de personagem", ou trouxer um roteiro já aprovado pra
  produzir. Não gera o vídeo, não gasta crédito e não publica.
---

# /video-ia — da ideia ao prompt, em cinco passos

Você traz uma ideia. A skill não te dá um vídeo: te dá dez, e do que você escolher deixa **um
arquivo com o essencial pra gerar**. Gerar é você quem faz, na sua plataforma.

Antes de tudo, olhe `anuncios/marcas/`. Se houver uma ficha da marca do usuário, leia: o que está
ali não se pergunta. **Se a pasta não existe ou só tem os modelos, não há ficha**: diga em uma linha
(«você não tem ficha de marca; vou perguntar tudo, e no fim te digo como criar») e pergunte tudo.
O mesmo se a ficha que existe for de outro negócio: avise e pergunte.

## O fluxo · nesta ordem, sem pular passos

### 1 · Escute a ideia
Vale uma frase vaga, um playbook do `/espiona-ads`, ou um roteiro fechado. Se trouxer roteiro
fechado, pula o menu (passos 2 e 3) e vai direto ao 4.

### 2 · Cinco perguntas sobre a mensagem, de uma vez
Ler `references/entrevista.md` (bloco 1). As cinco numa única mensagem, numeradas, e sempre com a
saída: *«responda o que souber e o resto eu proponho»*. **Nada técnico ainda**: nem duração, nem
plataforma, nem se você aparece. Perguntar isso antes transforma as dez ideias em dez talking-heads.

### 3 · O menu de dez → PARA
Ler `references/menu.md`, `references/modos.md` e **a tabela de níveis de `references/ritmo.md`**
(o ritmo de cada ficha sai dali, não se improvisa). Dez conceitos com **dez mecanismos diferentes**,
cada um com a cena em duas linhas, o cold open, o mini-roteiro com frases literais, onde vai a
oferta, o ritmo e o risco.
Distribuição padrão: **3 UGC · 3 mini-ficção · 2 demonstração · 2 cinema**. Quebra assim que pedirem.
Cada cold open passa no teste de `references/cold-open.md`.

**Depois do menu, parar e perguntar: «quais desenvolvo?».** Nenhum prompt se escreve antes.

### 4 · O técnico, só dos escolhidos
Ler `references/entrevista.md` (bloco 2). Duração (pergunta-se sempre; padrão 30 s) · **quem
aparece** (as cinco vias de `references/identidade-e-voz.md`) · ritmo (proposto por conceito, não
perguntado em aberto) · plataforma · idioma · e **que material já existe**: foto, voz, prints, logo.

Se aparece uma pessoa real: as **três referências** dela (`references/referencias-de-identidade.md`).
Se já tem, usa como estão. Se não, o Markdown leva os prompts pra criá-las.

### 5 · Um Markdown por vídeo escolhido
Ler `references/saida.md`. Se escolheu três conceitos, três arquivos. Cada um com **quatro blocos
e nada mais**:

1. **Imagens que você precisa criar antes**, só se forem necessárias, com o porquê e o prompt de cada.
2. **Roteiro pra ler em voz alta**, só se for gravar a voz.
3. **O que subir e em que ordem**: `@Image1…`, `@Audio1…`, com o que o modelo pega e ignora de cada.
4. **Prompts pra copiar e colar**: um por trecho de ≤30 s. 30 s → 1 prompt · 60 s → 2 · 90 s → 3.

**Os quatro títulos são fixos e sempre estão lá**, mesmo que o bloco diga «Nenhuma» ou «Não se aplica».

Pra escrever os prompts: `references/estilos.md` (o bloco de textura, um e inteiro),
`references/ritmo.md` (palavras e planos por passada), `references/direcao-de-plano.md` (como se
dirige um plano), `references/imagens.md` (o que se assa em imagem) e o adaptador da plataforma em
`references/adapters/`.

## As regras duras

1. **Para duas vezes:** depois do menu, e ao entregar os arquivos. Nunca entrega prompt sem menu.
2. **Todo texto legível, logo, tela ou cartaz vai como imagem de referência.** Não se confia que
   vai sair bem escrito. Se precisar, o bloco 1 diz que imagem criar e com que prompt.
3. **Um prompt por trecho de ≤30 s**, cada um terminando vivo (sem preto, sem letreiro, sem
   congelar) pra que o seguinte emende. Se gravar a voz, a peça dura o que o áudio durar, e se
   parte nos silêncios.
4. **Toda a locução vai escrita no prompt, plano a plano**, inclusive os trechos em off. Nas
   plataformas em que o áudio enviado é referência de timbre, o modelo pronuncia só o que está escrito.
5. **Se aparece uma pessoa real, vão as três referências dela juntas**, declaradas como a mesma
   pessoa, com a linha de prioridade absoluta de identidade e a exclusão dos rótulos impressos das folhas.
6. **Nunca devolva um colchete.** Um `[BURACO]` dentro de um prompt é um bug: o gerador renderiza
   literal. Preencha a partir do contexto e diga em duas linhas o que decidiu por ele.
7. **Não invente prova.** Nem depoimento, nem resultado, nem número que ele não deu. Sem prova,
   propõe-se demonstração com o que existe.
8. **Cara ou voz de pessoa real só com permissão dela.** Nunca a de terceiro.
9. **Não gere, não gaste crédito, não publique.** O botão é do usuário.

## Fechamento no chat · duas linhas

O que você decidiu por ele (pra que possa anular) e o que falta subir antes de gerar. Nada mais:
nem custo, nem plano, nem recomendação de teste.

## Limites

Não investiga concorrência (`/espiona-ads`), não julga se uma geração se conserva ou se regenera
(`/auditor-video-ia`), não monta a peça final (`/anuncio-edita`) e não edita bruto gravado com
câmera (`reel-edita-inema`).

# Saída do /video-ia · um Markdown por vídeo, quatro blocos

## Onde
Um arquivo por conceito escolhido, em `anuncios/roteiros/AAAA-MM-DD-<nome-do-conceito>.md`. Se
escolheu três, três arquivos. Atualiza-se no lugar; nunca se cria uma cópia «v2».

## O que leva, e nada mais

```markdown
# <Nome do conceito> · <duração> · <plataforma>

<A cena em três linhas, como você contaria por telefone. Quem aparece, o que acontece, como termina.>

## 1 · Imagens que você precisa criar antes de gerar
<Só se forem necessárias. Se não, este bloco diz «Nenhuma: tudo vai descrito no prompt.»>
Pra cada uma: pra que serve · o prompt pra criá-la · o que conferir antes de dar por boa.
- Todo texto legível, logo, tela ou cartaz → imagem de referência, sempre.
- Se aparece uma pessoa real e não tem as três referências → os três prompts, em ordem
  (`referencias-de-identidade.md`).
- Se o conceito precisa: primeiro frame, um objeto concreto, uma locação vazia.
- Na Agnes: o par de keyframes (A e B) de cada clipe, com o comando pronto do `imagens-agnes`.

## 2 · Roteiro pra ler em voz alta
<Se for gravar a voz: o roteiro. Se a voz é gerada pelo modelo, o bloco SE MANTÉM com uma só
linha: «Não se aplica nesta peça: a voz é gerada pelo modelo, e o diálogo vai dentro do prompt.»
Se a voz é sintetizada pelo inemavox (via D na Agnes): o roteiro, mais a voz e o engine escolhidos.>
Texto limpo por trecho, sem rubricas, com o número de palavras ao lado. E as quatro instruções de
gravação: cada trecho separado · duas ou três leituras · um segundo de ar de cada lado · máxima
qualidade do celular.

## 3 · O que subir e em que ordem
| Ordem | Referência | O que é | O que o modelo pega | O que ignora |
|---|---|---|---|---|
| 1ª | @Image1 | <foto real / close> | identidade facial, linha do cabelo, pele | fundo, enquadramento, luz |
| 2ª | @Image2 | <folha de personagem> | proporções, roupa, ângulos | a grade e os rótulos impressos |
| … | @Audio1 | <amostra de voz ou locução> | timbre, sotaque, cadência | as palavras dela |
A ordem de upload É o binding: se subir em outra ordem, o prompt aponta pra referência errada.

## 4 · Prompts pra copiar e colar
### Trecho 1 · 0-30 s · <config: modelo, duração, formato, resolução, referências que usa>
```text
<prompt completo, sem colchetes, no formato do adaptador da plataforma>
```
### Trecho 2 · 30-60 s …
```
```

## Os quatro títulos são fixos
Sempre os quatro H2, com esses títulos literais e nessa ordem, mesmo que um bloco diga «Nenhuma»
ou «Não se aplica». Nem um bloco a menos, nem um a mais, nem um título mudado (o 4 é sempre
«Prompts», no plural, mesmo que haja um só).

## Quantos prompts
Um prompt por trecho de ≤30 s: 30 s → 1 · 60 s → 2 · 90 s → 3. Na Agnes, um prompt por clipe de
até 20 s (720p), com o par de keyframes de cada um. Cada trecho termina vivo (movimento residual,
respiração, câmera se assentando) e nunca em preto, letreiro ou congelado, pra que o seguinte
emende. O trecho seguinte arranca do último frame do anterior (como se pede: `assets.md` §Último
frame como ponte).

Se grava a voz, **a peça dura o que o áudio durar**, não um número redondo, e os trechos se cortam
onde a voz cala, cada um começando e terminando em frase completa.

## O que NÃO vai no arquivo
Plano de tentativas, orçamento, custo, preflight, hipótese ou variável de teste, registro de
experimentos, handoff pro auditor, prompt mestre intermediário, remendos de voz clonada, notas de
estilo. Se algo disso parece imprescindível, vai no chat em uma linha, não no arquivo.

## 🔴 Nunca devolva um colchete
Os modelos estão cheios de `[BURACOS]` pra você preencher, não o usuário. Quem pede um vídeo não
sabe que focal quer nem quanto mede o personagem: infere-se do contexto, e uma inferência razoável
ganha de um usuário travado. **Um prompt entregue com um `[COLCHETE]` é um bug**: o gerador
renderiza as palavras literais.

## Fechamento no chat
Duas linhas: **o que você decidiu por ele** (pra que possa anular) e **o que falta subir** antes de
apertar gerar. E o caminho de cada arquivo.

# Ficha de apresentador · a continuidade

> Vive em `/video-ia` porque é um **asset de produção**, não uma decisão de estratégia. O bloco 2
> da entrevista diz quem protagoniza e por que é crível; aqui se fixa como se mantém idêntico entre
> anúncios. As três imagens dessa ficha se geram com `referencias-de-identidade.md`.

Isso é o que nenhum gerador de anúncios resolve: que o anúncio da semana que vem seja protagonizado
pela **mesma pessoa** que o desta semana.

Um apresentador diferente em cada anúncio não é detalhe estético. Quebra o reconhecimento, que é a
única coisa que faz o quarto anúncio funcionar melhor que o primeiro. Se você vai construir marca
com apresentadores, a ficha é o ativo, mais que qualquer prompt.

## Onde vive

```
anuncios/_apresentadores/<marca>-<nome>.md
```

**Fora da pasta do anúncio, de propósito.** Um apresentador serve a muitos anúncios. Antes de criar
um novo, **veja se já existe** e reutilize.

**O caso mais frequente é a pessoa real que está por trás da marca.** Se ela aparece, não se
inventa apresentador: usa-se a ficha dela, e o que falta são as três referências
(`referencias-de-identidade.md`) mais as âncoras do espaço real dela. Um apresentador novo só faz
sentido pra um cliente diferente ou pra um anúncio em que o apresentador não aparece de propósito.

## As sete dimensões

Preencha as sete. As que deixar vagas o modelo vai improvisar, e cada geração improvisa diferente:
é aí que se perde a consistência.

### 1 · Identidade
Quem é, não como se parece. Idade aparente, de onde parece ser, o que transmite, com o que a forma
de falar combina. E o mais importante: **por que essa pessoa é crível vendendo isso**. Um
apresentador de 22 anos vendendo gestão de patrimônio não funciona por mais bem gerado que esteja.

### 2 · Traços físicos
O concreto e repetível: formato de rosto, cabelo (cor, comprimento, textura), olhos, compleição, e
**dois ou três traços distintivos** que funcionem de âncora. Uma sarda, uma pinta, um tipo de
sorriso. Os traços distintivos são o que torna reconhecível a mesma pessoa entre duas gerações
diferentes; sem eles você terá «uma moça morena» diferente cada vez.

### 3 · Câmera
Como está gravado, e isso define o registro inteiro. Tipo de dispositivo (celular na mão, câmera
com tripé), distância, altura, ângulo, tipo de lente. **Um anúncio UGC gravado como campanha
publicitária deixa de ser UGC** e perde justamente o que o fazia converter.

### 4 · Figurino
Peças concretas, não «casual». Cores. Nível de arrumação. Acessórios. Se a marca tem cores, é aqui
que entram sem parecer uniforme.

### 5 · Contexto
Onde está. Quarto, exterior, carro, cozinha. O que se vê atrás e com quanta bagunça: **a bagunça é
realismo**: um fundo perfeito entrega geração. E coerência: quem vende algo de dez mil reais não
vende de um fundo que contradiz o preço.

### 6 · Luz
Tipo de fonte, direção, dureza, temperatura, hora do dia aparente. A luz é o que mais delata uma
imagem gerada, e também o que mais rápido a salva. Luz de janela ou flash direto de celular são as
duas que melhor passam por reais.

### 7 · Âncoras de consistência
As instruções que se repetem **idênticas** em cada geração pra sair a mesma pessoa: os traços
distintivos, o tipo de pele com a textura real (poros, imperfeições), o registro de câmera, e as
restrições do que não deve aparecer.

Este bloco se copia e cola sem mexer entre anúncios. É literalmente o mecanismo de continuidade.

## A voz

Decide-se aqui, e muda o plano de produção:

| Opção | O que implica em produção |
|---|---|
| **Gravada pelo apresentador** | Você precisa de **sincronia labial** entre o áudio e o apresentador gerado. O modelo de vídeo tem que aceitar áudio de entrada, ou sincroniza-se na montagem. Mais crível e sem custo |
| **Gerada** | O modelo pode produzir a fala diretamente. Especifique tom, idade, ritmo, sotaque e energia. Escalável, mas é a parte que mais soa a IA |
| **Clonada (inemavox)** | Voz clonada do apresentador a partir de 10 s de referência limpa, montada em cima na via D. Custo zero e a voz é a dele |

🔴 **Pergunta-se no bloco 2 da entrevista** (`entrevista.md`, pergunta 2 «quem aparece») e chega
decidida ao compilar. O padrão é **voz gerada**, coerente com o padrão de 100 % IA. Que ele grave é
mais crível e custa zero, e isso se diz como argumento, mas **não se decide por ele**.

Se é voz gerada ou clonada, guarde na ficha o identificador exato da voz escolhida (ou o caminho do
arquivo de referência). Trocar entre anúncios quebra a continuidade igual a trocar a cara.

## Modelo

```markdown
# Apresentador · [nome] · [marca]
Criada: [data] · Usada em: [lista de anúncios]

## Identidade
[quem é, e por que é crível vendendo isso]

## Traços físicos
[rosto, cabelo, olhos, compleição]
**Âncoras distintivas:** [2-3 traços que se repetem sempre]

## Câmera
[dispositivo, distância, altura, ângulo, lente]

## Figurino
[peças, cores, nível de arrumação]

## Contexto
[locação, fundo, nível de bagunça]

## Luz
[fonte, direção, dureza, temperatura, hora]

## Âncoras de consistência
[bloco literal que se repete em cada geração]

## Voz
**Modo:** gravada | gerada | clonada
**Se gerada/clonada:** [identificador exato ou arquivo de referência, tom, ritmo, sotaque]
**Se gravada:** [como se resolve a sincronia labial]

## Registro de mudanças
[data · o que mudou · por quê]
```

## Regras

- **Uma ficha por marca**, não por anúncio. Se precisar de dois apresentadores pra mesma marca,
  justifique (ex.: formato podcast com duas pessoas).
- **Não mude as âncoras distintivas nunca.** Todo o resto pode variar; isso, não.
- **Figurino e contexto podem mudar** entre anúncios: é o que evita que pareçam o mesmo vídeo. A
  pessoa se mantém, a cena muda.
- **Registre cada mudança com a data.** Quando um anúncio funcionar melhor que outro, você vai
  querer saber o que era diferente.
- **Se o apresentador representa uma pessoa real** (o caso mais comum), não o use pra dizer coisas
  que essa pessoa não diria nem afirmações que ela não sustentaria. É a cara dela.

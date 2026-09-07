# Imagens · prompts, âncoras de realismo e style lock

> Vive em `/video-ia`: promptar uma imagem é produção. Os assets que esta referência produz
> (primeiro frame, último frame, produto, locação) são inventariados em `assets.md`.

## Quando precisa de imagem, e quando não

As plataformas de multishot geram vídeo com diálogo direto do texto. Nelas, as imagens só são
necessárias em três casos, e nos demais são um passo a mais que custa dinheiro e deriva:

| Caso | Pra quê |
|---|---|
| **Fluxo primeiro/último frame** | Controle real do movimento nos clipes animados ou de cinema |
| **Referência de identidade** | Que a mesma pessoa apareça igual em todos os clipes |
| **Validar o ângulo barato** | Um anúncio com imagem fixa + voz off já diz se o gancho funciona |

**Na Agnes é diferente: a imagem é obrigatória.** O vídeo se gera por keyframes (primeiro e último
frame de cada clipe), então toda cena começa por duas imagens. → `adapters/agnes-keyframes.md`

**Se é o primeiro anúncio de um ângulo novo, valide com imagem fixa ou voz off.** O ângulo é o que
decide o resultado; a cara falando se produz quando você já sabe que o ângulo funciona.

---

## Como se monta um prompt de imagem

Seis dimensões. A ordem importa menos que a presença: **se deixar uma de fora, o modelo improvisa,
e cada geração improvisa diferente.**

| Dimensão | O que fixa |
|---|---|
| **Pessoa** | Identidade e traços distintivos, copiados literais de `apresentador.md` |
| **Câmera** | Dispositivo, ângulo, distância, lente |
| **Figurino** | Peças e cores concretas |
| **Cena** | Locação e fundo, com a bagunça dele |
| **Luz** | Fonte, direção, dureza, temperatura |
| **Âncoras** | Textura de pele real, restrições, limpeza |

**Os prompts de imagem vão em inglês.** Os modelos respondem melhor e derivam menos. Na Agnes é
obrigatório: prompt em português dispara o filtro de conteúdo e devolve erro em pedido legítimo.
O roteiro falado em português; o prompt, em inglês.

**Ordem recomendada:** tipo de foto e dispositivo → pessoa → ação → figurino e cena → luz →
restrições. Essa hierarquia coloca o importante onde o modelo pesa mais.

### As âncoras de realismo

- **Textura de pele real**: poros, imperfeições, assimetria. Pele perfeita é a delação nº 1.
- **Registro de celular**: enquadramento imperfeito, levemente descentrado. Nada de composição de estúdio.
- **Grão leve** e alguma compressão. Nitidez perfeita não existe em vídeo de celular.
- **Fundo com vida**: objetos reais, algo fora do lugar. *Home office real, luz natural, que NÃO
  pareça set de venda.*
- **Restrições no fim**: sem texto, sem marca d'água, sem deformações, sem mãos estranhas.

⚠️ **Nunca peça «hiper-realista», «fotorrealista», «8K» nem «render» num UGC.** Empurram o modelo
pra estética publicitária. É o mesmo erro de aplicar o prefixo de cinema a um talking-head; ver
`estilos.md`. Peça uma foto de celular e descreva as condições de uma foto de celular.

### Mudanças sem perder a pessoa

Quando precisa da mesma pessoa em outra cena, **mude uma dimensão e deixe as demais idênticas.**
Mudar várias ao mesmo tempo é o que faz aparecer outra cara.

| Precisa de | Muda só |
|---|---|
| Outra cena | Cena e luz |
| Outro look | Figurino |
| Outro plano | Câmera |
| Outro momento do dia | Luz |

As âncoras distintivas e a textura de pele **não se tocam jamais**.

### Na Agnes, três regras medidas a mais

- **No máximo 2 referências por imagem.** Três ou mais saturam; cinco viram confete e o prompt é
  ignorado. Muitos personagens numa cena → uma âncora de GRUPO (várias pessoas juntas = 1 ref).
- **Sem pose frontal simétrica** em personagens: sai cabeça ou cauda dupla. Perfil ou três-quartos,
  e pedir `exactly one head` em positivo (nunca «no two heads», que vira atrator).
- **Descritor de estilo só estético** (luz, cor, render). «Expressive eyes», «fur», «children's
  book» injetam personagem numa paisagem.

---

## 🔴 Tudo que tem que sair EXATO se assa em imagem, não se pede ao vídeo

> Regra confirmada dos dois lados: quando se pede texto ou logo direto ao vídeo, aparecem logos
> duplicados e números trocados; quando se assam as referências antes, logos, caligrafia e listas
> com checkboxes saem letra-perfeitos. **Quando há texto, logos ou imagens que precisam ficar
> exatos, cria-se a referência e entrega-se ao modelo.**

**Alcance da regra: não é só texto.** Assa-se em imagem qualquer coisa cuja forma exata importe e
que o modelo teria que inventar:

| Assa-se | Por quê |
|---|---|
| **Texto legível** | O modelo escreve errado o que inventa |
| **Logos de marca** | Redesenha de memória e saem deformados |
| **Props com estrutura** | Listas, fichas, tabelas, checkboxes: a maquete vai embora |
| **Composições concretas** | Um conjunto de objetos numa disposição pedida |

O que **não** se assa: o fundo, a luz, a atuação, a câmera e o texto decorativo ilegível (telas
borradas, papéis de fundo). Isso se descreve e se deixa pro modelo.

**E o que não se pede ao vídeo:** um letreiro flutuante que não é parte física da cena (um «Minuto
90» sobreposto, um preço na tela, uma legenda) **é montagem**, não geração. No prompt só vai o texto
que existe dentro da cena: um cartaz, uma tela, uma folha. O resto se acrescenta depois.

Pra **cada** elemento que deva sair exato:

1. **Gerar PRIMEIRO a imagem fixa do prop** com o texto literal entre aspas no prompt de imagem.
   Uma imagem se revisa letra a letra e custa centavos (ou zero, na Agnes); o mesmo erro no render
   custa a geração.
2. **Aprovar letra a letra** antes de tocar no prompt de vídeo.
3. **Colocar como referência** no vídeo com binding: `take the prop's exact geometry and its
   text, letter-perfect` / `ignore background and lighting`.
4. **O prompt de vídeo repete do mesmo jeito o texto entre aspas**: a referência ancora, o texto
   escrito valida.
5. Se mesmo assim o render estraga: **edição localizada do prop**, não regeneração.

Aplica-se a todo texto legível; o texto decorativo ilegível (telas borradas, papéis de fundo)
continua sendo pedido borrado e sem referência.

### 🔴 O limite: uma referência de estado final NÃO produz uma sequência

Uma imagem de referência diz **como tem que ficar**, não **em que ordem se chega**. Se você dá o
estado final e três segundos, o modelo interpola pra esse estado pelo caminho mais curto, e o
caminho mais curto é tudo aparecer ao mesmo tempo.

**Quando aparece:** uma ação repetida sobre N objetos (riscar três, colocar três, marcar três) com a
imagem do resultado completo como destino.

**Como se resolve, do mais barato ao mais caro:**

1. **Dar ar**: a mesma ação sobre N objetos precisa de ~1,2 s por objeto como piso. Três riscados
   em 3 s não cabem; em 4-5 s sim.
2. **Nomear a ordem e o estado intermediário no próprio plano**: *«first the left note only — the
   other two still clean — then the right one, then the bottom one»*. Descrever o que **ainda não**
   aconteceu é o que impede o salto.
3. **Assar o estado intermediário** como referência própria (um riscado, dois limpos) e usá-lo como
   primeiro frame do trecho.
4. **Picar em insertos** de uma só ação cada e montar. É o seguro quando a sequência *é* a piada.

**Regra curta:** as referências controlam a **forma**; a ordem e o ritmo se controlam na **prosa do
plano** e nos **segundos que você dá**. Nunca espere que uma imagem dirija o tempo.

## O produto no plano

| Tipo | Como mostrar |
|---|---|
| **Físico** | Na mão, em escala real, etiqueta legível. Se o modelo deforma o texto, vai na montagem |
| **App ou software** | Em tela de celular ou notebook segurado com naturalidade. **A interface se compõe depois**: os modelos inventam interfaces |
| **Serviço / comunidade** | Não há produto: mostra o resultado ou o momento do problema |

### Interfaces fictícias: maquetar em HTML, não gerar

Quando a tela que precisa aparecer **não é um produto real** (um dashboard inventado, um painel de
«agentes trabalhando»), a referência não se gera com IA: **maqueta-se em HTML e captura-se**. Texto
perfeito por construção, custo zero, e mudar um letreiro custa um minuto em vez de uma geração.

```bash
# Chrome/Chromium headless (Linux; no Mac troque o binário)
chromium --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=1920,1080 --screenshot=tela.png "file://$PWD/tela.html"
```

- O HTML fica junto do PNG: é a fonte editável (regra `.md`/`.html` = fonte, export = derivado).
- Design que se lê como software real, não como maquete: estados assimétricos (barras em
  porcentagens diferentes), linhas de detalhe, um feed com horas. Tudo simétrico entrega template.
- No prompt de vídeo entra como referência assada (regra acima) **e o plano que a mostra se desenha
  frontal e quase plano no quadro**: se o render suja a letra pequena, substitui-se a tela em pós
  com um corner-pin do PNG (cinco minutos) em vez de regenerar.
- Critério de conservar/substituir: definem-se ANTES as palavras que devem ser lidas (os títulos);
  se alguma falha no render, corner-pin, não regeneração.
- ⚠️ Continua valendo a regra dura do produto real: uma interface que o cliente **recebe de verdade**
  se compõe com a captura real, nunca se maqueta nem se gera.

**Regra dura:** se o produto existe de verdade, a imagem do produto é **a real**, composta na
montagem. Um produto gerado que não bate com o que o cliente recebe é problema de confiança e,
conforme o caso, de publicidade enganosa. Vale igual pras **capturas de produto**: a interface da
comunidade se compõe com a captura real, nunca se gera.

---

## Via animada ou de cinema

### A metáfora visual

Antes de gerar uma única imagem, decida **a metáfora**. É a decisão mais importante desta via e a
que mais se pula.

- Mecanismo de acumulação → algo que se enche
- Mecanismo de ineficiência → algo travado que começa a fluir
- Problema de dispersão → peças espalhadas que se juntam em uma
- Problema de confiança → uma porta fechada que se abre

**Três regras:** uma metáfora por anúncio (duas competem e nenhuma se entende) · compreensível sem
explicação (se a voz tem que explicar, é enfeite, não metáfora) · **respeita o mecanismo real**
(uma metáfora bonita de algo que o produto não faz é uma mentira com desenhos).

### O style lock

Bloco estético que se repete **idêntico** em todas as gerações: técnica · paleta · traço e
acabamento · composição · tratamento do texto.

Define-se uma vez e copia-se sem mexer. **Se mudar o estilo no meio, o anúncio quebra** e não há
montagem que conserte.

Nota: estilos muito reconhecíveis (o de um estúdio de animação específico) têm dois problemas: o
modelo pode se negar, e usar a estética de uma marca alheia pra vender a sua é terreno escorregadio.
Defina uma estética própria e descreva.

### Primeiro e último frame

Em vez de pedir um vídeo e aceitar o que sair, você gera **as duas imagens extremas** de cada clipe
e o modelo interpola o movimento. **É o modo nativo da Agnes** e funciona em qualquer plataforma
que aceite primeiro/último frame.

```
1. Gera o PRIMEIRO frame (imagem fixa, com o style lock)
2. Gera o ÚLTIMO frame: mesma cena, mesmo estilo, estado final
3. Passa os dois pro modelo de vídeo como primeiro e último frame
4. O modelo constrói a transição
```

**Você controla o resultado em vez de implorar por ele.**

- O último frame se gera **a partir do primeiro** (img2img com o primeiro como referência), não do
  zero. Só muda o que se move.
- Mudança **moderada** entre os dois. Se são diferentes demais, o modelo inventa a transição e
  saem deformidades.
- Continuidade entre clipes: o último frame de um tem que poder conviver com o primeiro do seguinte.

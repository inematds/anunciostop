# A entrevista · dois blocos, e não se misturam

**O motor de perguntas.** Curto de propósito: quem usa esta skill quer ideias, não um formulário.

## Por que em dois blocos

Se você pergunta a duração, a plataforma ou o avatar **antes** de ter as ideias, condiciona as
ideias. «Vão ser 15 segundos com a cara do apresentador» e de repente os dez conceitos são dez
talking-heads com fundo diferente.

| Bloco | Quando | Sobre o quê | Quantas |
|---|---|---|---|
| **1** | Antes do menu | A **mensagem**. O que precisa ser entendido | 5, no máximo 6 |
| **2** | Depois que escolherem 2-3 | O **técnico**. Só do que vai ser produzido | 4, e só o que faltar |

---

# BLOCO 1 · A mensagem

**As cinco vão de uma vez, numeradas, numa única mensagem.** Não uma por uma: é isso que faz uma
entrevista parecer interrogatório.

E sempre com uma saída: *«responda o que souber e o resto eu proponho»*. Quem só tem uma ideia
vaga precisa conseguir seguir.

```
1 · O que se vende exatamente e o que se pede no fim do vídeo?
    (uma compra, um cadastro, um teste grátis, uma mensagem no privado…)

2 · Com quem você está falando? Descreva essa pessoa em duas frases: o que
    ela faz, o que a frustra. Não um segmento demográfico.

3 · Ao terminar o vídeo, o que quem assistiu tem que PENSAR?
    Uma frase só, nas palavras dela, não nas suas.

4 · Que prova temos? Algo que dê pra MOSTRAR: uma tela, um resultado, um
    antes e depois, um número real.

5 · O que NÃO podemos dizer? Promessas que não sustentamos, concorrentes
    que não se nomeiam, números sem confirmação.
```

## Como se leem as respostas

| Pergunta | Pra que serve de verdade | Se vier vazia |
|---|---|---|
| **1 · O que se vende / o que se pede** | Decide o fechamento do vídeo e se cabe oferta no gancho | Pergunta de novo. Sem isso não há vídeo |
| **2 · Pra quem** | É a matéria-prima do cold open: o gancho se constrói sobre um momento reconhecível dessa pessoa | Propõe-se um perfil e **marca-se como suposição** |
| **3 · O que tem que pensar** | É **o mecanismo**. Daqui sai a variedade real do menu | Deriva-se de 1 e 2 e diz-se em voz alta |
| **4 · Que prova há** | Decide se cabem os modos que demonstram (demonstração, depoimento, produto herói) | Sem prova, **não se usa depoimento**: usa-se demonstração com o que existe |
| **5 · O que não se pode dizer** | É a grade de proteção legal e de marca | Pergunta-se. É a única das cinco que evita um problema real |

## E mais uma pergunta, só se precisar

- Se a ideia que trazem já é um modo concreto («quero um de cinema»): *«te prendo a esse modo ou
  coloco como um dos dez e te mostro alternativas?»*
- Se há um vídeo de referência que eles gostam: peça. Uma referência economiza três perguntas.

## O que NÃO se pergunta no bloco 1

Duração · plataforma · avatar ou cara · voz · formato · idioma · proporção · quantos vídeos.
**Nada disso entra aqui.** Se disserem por conta própria, anota-se e não se repergunta.

## O ritmo não se pergunta aqui: recomenda-se no menu e confirma-se no bloco 2

O padrão é **dinâmico**: algo acontece a cada 2-3 segundos. Mas **o nível se propõe por conceito**,
com a razão, e se confirma depois. Perguntar no bloco 1 não serve: sem o conceito na frente,
ninguém sabe que ritmo quer. → `ritmo.md`

---

# BLOCO 2 · A ficha técnica

**Só depois que escolheram**, e só dos conceitos escolhidos. O que já se sabe pela conversa ou pela
ficha de marca não se pergunta: diz-se como suposição.

```
1 · Duração: 30 segundos (padrão), ou mais longo?
    🔴 ESTA PERGUNTA SE FAZ SEMPRE. Nunca se pula, nem que a ficha de marca
    fixe uma duração, nem que se saiba de uma sessão anterior. Propõe-se o
    padrão de 30 s e espera-se.
    Se a marca fixa outra duração, diz-se ao perguntar:
    «o padrão são 30 s; sua marca tem o dado em 60-90. Qual?»

2 · Quem aparece:
    a) personagens inventados pela IA
    b) uma cara real verificada (com o asset de identidade)
    c) uma foto fixa animada com um áudio
    d) ninguém a câmera: voz off sobre imagem gerada
    e) uma pessoa gravada e transformada, mantendo cara e voz

3 · O ritmo. E isso NÃO se pergunta em aberto: propõe-se.
    «O 03 eu levo pra MEDIDO, é um conceito de intriga e os cortes rápidos
    comem a tensão; e o 05 pra FRENÉTICO, que é entrevista de rua.
    Fecha pra você ou quer mais movimentados?»
    Se não responderem, aplica-se o recomendado. Na dúvida, DINÂMICO.

4 · Em que plataforma vocês vão gerar?
    (pra ajustar o formato do prompt, não pra mudar a ideia)

5 · Idioma e sotaque do que se fala.
```

## Como cada resposta muda o prompt

| Resposta | O que muda |
|---|---|
| **Duração** | Decide se convém uma geração de até 30 s, módulos de 15-20 s, one-take da interface ou vários clipes. Não existe teto universal de planos: desenha-se por conceito e por superfície |
| **Via a** (inventado) | Sem bloco de identidade verificada. Descrição de personagem muito detalhada, porque é a única coisa que o mantém igual entre planos |
| **Via b** (cara verificada) | Entra o bloco de asset + a linha de prioridade de identidade. → `identidade-e-voz.md` |
| **Via c** (foto + áudio) | **O áudio que se sobe É a voz que soa.** Não há bloco de referência de timbre, e o prompt só dirige gesto e câmera |
| **Via d** (voz off) | Ninguém mexe a boca. Elimina-se todo o lip-sync do prompt e **a qualidade da imagem sobe muito**: é a via mais segura do catálogo, e a via natural da Agnes |
| **Via e** (gravar e transformar) | Cara, voz, atuação e timing vêm do clipe gravado. O prompt muda cena ou acabamento sem inventar gestos → `gravar-e-transformar.md` |
| **Plataforma** | Ativa um adaptador: Agnes por keyframes, Seedance multishot, Dreamina one-take, modular. Não muda a ideia, muda a unidade de produção e o prompt |
| **Ritmo** | Quantos eventos leva a malha e quantos micro-planos vão dentro de cada plano. E o bloco de áudio, que é onde vive metade do ritmo. ⚠️ Quanto mais alto o nível, **mais tentativas**: diz-se ao propor |
| **Idioma** | A última linha do prompt, e uma linha nos negativos contra a deriva de sotaque |

## Montagem e geração

Não assumir que tudo tem que sair numa geração. Escolher entre multishot nativo, one-take, módulos
com montagem, extensão ou edição localizada. A arquitetura se decide depois de conhecer a interface
e o conceito. → `ritmo.md`

## A pergunta que se faz sempre no bloco 2

**Que material já existe?** Foto da pessoa, amostra de voz, prints do produto, logo. Muda o que
se pode prometer, e evita escrever um prompt que precisa de um asset que ninguém criou.

---

## O anti-padrão

❌ Doze perguntas antes de dar qualquer coisa. Quem pede um vídeo cansa na quarta e responde no
chute, e uma resposta no chute é pior que uma suposição declarada.

✅ Cinco perguntas, dez ideias, e as perguntas técnicas quando já há algo pra produzir.

# Adaptador · Seedance 2.5 multishot (pago, sem configuração local)

## Alcance e data

Perfil de agosto de 2026. Separar sempre **modelo** de **interface/provedor**. Usa-se pela web do
provedor (TopView, Higgsfield, Magnific e outros que expõem o 2.5): você cola o prompt lá. Nada se
configura no `.env` deste pacote.

Capacidades oficiais do modelo:

- até 30 segundos por geração;
- até 30 imagens, 10 vídeos e 10 áudios como referências;
- geração multishot (cortes dentro do prompt);
- extensão;
- edição localizada e por timestamp.

O provedor pode expor menos referências, outra caixa de prompt, outra resolução ou comportamento
one-take. Verificar a interface antes de compilar.

## Antes de compilar: olhe a superfície onde vai ser gerado de verdade

A web, a API e o MCP do mesmo provedor são superfícies diferentes: uma web pode ter slot de áudio e
o MCP dela não. Compila-se pra superfície onde o usuário vai colar o prompt.

⚠️ **A duração devolvida pode não ser a pedida** (pedidos 28 s, entregues 30). Não desenhar um
final no segundo exato; a cauda sobrando se corta na montagem contra o áudio. O final do último
plano se escreve vivo e estável justamente pra que essa cauda seja recortável.

## Slot de áudio em superfícies web

Quando a web admite subir um áudio junto do prompt, **esse áudio é referência de TIMBRE, não pista
de reprodução**: o modelo clona a voz do áudio subido, mas pronuncia **exatamente o que está
escrito como `Dialogue` no prompt, e nada mais.** Um plano sem linha de diálogo escrita sai mudo
(só ambiente). Custa uma geração inteira descobrir isso: 24 s de silêncio atrás da única frase escrita.

Regras duras que saem disso:

1. **Toda a locução vai escrita no prompt, plano a plano, verbatim**, inclusive os trechos em off.
2. **Formato do off:** `Dialogue (NOME, off-camera): '...'` + no plano: «NOME is not visible in
   this shot and nobody on screen moves their lips» (senão o modelo põe a voz na boca de um figurante).
3. **O bloco [AUDIO] exige voz contínua** quando o conceito é assim: «X speaks CONTINUOUSLY across
   the entire film — there must be no stretch of more than one second without his voice.»
4. **Preflight do prompt:** percorrer os planos um a um. Algum sem `Dialogue`? → vai sair mudo. Se
   é mudo de propósito, que seja por desenho, não por omissão.
5. A voz que soa é o **clone do timbre lendo o roteiro**, não a gravação original. A gravação
   original se guarda como pista de substituição em pós se o clone não convencer.

## Modos

### Geração de até 30 s

Usar pra uma peça completa quando a interface executa bem o multishot. Os timestamps devem ser
contíguos e somar a duração pedida.

### Extensão

O plano final do primeiro clipe tem que ficar vivo:

- movimento residual;
- respiração;
- câmera que ainda se assenta;
- fumaça, água, tecido ou luz em continuidade.

Evitar preto, cartão final ou freeze frame se depois vai estender.

### Edição localizada

Pedir uma mudança concreta e preservar o resto:

```text
Between [range], replace/change [single target] with [desired state]. Preserve identity, performance,
camera path, timing, lighting, audio and every unaffected region exactly as in the source clip.
```

Não usar edição localizada pra resgatar um conceito incompreensível, lip-sync quebrado de forma
global ou identidade que deriva na peça inteira.

## Referências e binding

Atribuir cada referência dentro do plano onde trabalha:

```text
@Image1 — take facial identity, hairline and skin marks; ignore grey background, flat light and crop.
@Image2 — take product geometry, label placement and materials; ignore reflections and tabletop.
@Video1 — take only camera trajectory and acceleration; ignore subject, location, wardrobe, colour and audio.
@Audio1 — take only voice timbre and Brazilian Portuguese cadence; never quote, transcribe or play its source words.
```

Usar as referências mínimas suficientes. O teto não é objetivo. Uma referência ambígua pode tirar
controle.

### Storyboard

Usar como guia de framing e blocking, nunca como elemento visível:

`Match the framing and blocking of Panel 3 in @Image1 (storyboard guide only; never show the board).`

E reforçar nos negativos: `no grid lines, no panel borders, no panel numbers, no caption strips.`
O tabuleiro é andaime, não conteúdo.

**Três checagens no storyboard antes de pagar o render.** A ideia de fundo: corrigir uma
composição no storyboard custa centavos, corrigir no render custa o render.

1. **Gerar o storyboard com a folha de personagem engatada como referência.** Se os painéis saem
   com outra cara, o storyboard não serve nem pra composição nem pra identidade.
2. **Cada palavra que vai aparecer escrita no vídeo vai entre aspas no prompt do painel.** Assim a
   ortografia se valida no storyboard e não no render.
3. **A escala se verifica pondo os painéis lado a lado.** O que é maior que uma casa num painel
   não pode ser do tamanho de um cavalo no seguinte. → `direcao-de-plano.md`

Dar a cada identidade, produto ou locação a própria referência. Não reutilizar um rótulo pra duas
entidades diferentes.

### Vídeos de referência

- **Até 10 vídeos-ref por geração** (oficial). Por padrão o modelo pega «composição, cenas,
  estilos, personagens e props». Caso oficial de continuidade: *«Continue from the visuals and
  subjects in @Video 1»*.
- ⚠️ **A sintaxe depende da superfície:** blog/modelo = `@Video1`; algumas APIs = `<<<Video1>>>`.
  Numa web, usar a menção que a interface insere ao anexar. Não dar nenhuma por certa.
- ⚠️ **Alguns provedores limitam a 30 s combinados** entre todos os vídeos-ref. Um módulo de 30 s
  cabe justo; dois não.
- 🔴 **O «extend» de alguns provedores NÃO continua o seu material**: clona o estilo de um vídeo
  alheio pra fazer um parecido («remake viral»). Não usar como ponte de continuidade. Nesses casos,
  frame-ponte → `assets.md`.
- **Sem `ignore` explícito, um vídeo-ref arrasta enquadramentos, ritmo de corte e áudio** do clipe
  referenciado. Binding pra continuidade: `take character identity, location, lighting; ignore
  camera framing, cut rhythm, pacing and audio`.
- **As DUAS opções são válidas pra encadear módulos**: frame-ponte (validado em produção) e
  vídeo-ref com binding de continuidade (apoiado pelo exemplo oficial). Receita de cada uma →
  `assets.md`.

## Estrutura compilada

```text
[FORMAT AND INTENT]
Vertical 9:16 advertising film, 30 seconds. <one-line thesis and audience effect>.

[REFERENCE BINDING]
<one line per reference: take / ignore / use>

[GLOBAL VISUAL LANGUAGE]
<camera stability, lens character, texture, palette and motivated light chosen from the brief>

[IDENTITY / PRODUCT / SCENE LOCKS]
<literal locks that remain identical across every shot>

[00:00-00:03] Shot 1 — <subject + one primary action first>. <acting>. <camera and motive>. <light>.
<sound>. <transition>.

[00:03-00:07] Shot 2 — ...

[AUDIO]
<dialogue, ambience, sound effects and music decision from the brief>

[STRICT CONSTRAINTS]
<concept-specific exclusions, text policy, identity and continuity>
All characters speak Brazilian Portuguese. No neutral, European or generic Portuguese accent.
```

## Regras de plano

- Começar com sujeito e ação principal.
- Uma ação principal por plano; dividir ações concorrentes.
- Manter timestamps contíguos, sem buracos nem sobreposições.
- Descrever estado inicial, evento e estado final visível.
- Dirigir olhos, mãos, respiração e postura quando há atuação.
- Motivar câmera, luz e transição.
- Manter uma linguagem visual comum.
- Declarar o último beat como final e mantê-lo vivo.
- **Faixa de planos: 14-18 em 30 s** em superfícies que executam cortes. Acima de ~20 dobra a
  superfície de falha. Medir a interface e simplificar só se ela omite ações. → `ritmo.md`

## Estilo variável

Não impor lente, filme, formato, obturador, câmera na mão, névoa, halation ou ausência de música
por padrão.

Escolher conforme o brief:

- UGC: celular, imperfeição e luz disponível;
- produto: controle, precisão e materiais;
- ficção: cobertura e atuação;
- documentário: observação e continuidade;
- cinema: escala e movimento motivado;
- peça gráfica: composição e timing.

Uma câmera estável é válida. Música é válida se faz parte do brief e a interface suporta.

## Gate

- [ ] Compilado pra superfície onde se cola o prompt (a web, não a API).
- [ ] Referências inequívocas com `take/ignore`.
- [ ] Timestamps contíguos.
- [ ] Uma ação principal por plano.
- [ ] **Nenhum plano sem `Dialogue` escrito, salvo mudo por desenho** (o slot de áudio só pronuncia
      o escrito).
- [ ] Trechos em off marcados `off-camera` + «nobody on screen moves their lips».
- [ ] Identidade e produto travados.
- [ ] Estilo escolhido, não herdado por padrão.
- [ ] Áudio decidido.
- [ ] Final vivo se haverá extensão, e recortável (a superfície pode devolver segundos a mais).
- [ ] Prompt dentro da caixa real.
- [ ] Idioma: português do Brasil declarado na última linha, negativo contra deriva de sotaque.

# Os blocos de textura

> **Escolha UM e cole inteiro.** Misturar é o que transforma um vídeo em publicidade genérica.

A textura não é o modo. Um mesmo modo (uma comédia, por exemplo) pode ser filmado com textura de
celular ou com textura de cinema. A tabela de combinações válidas está no fim de `modos.md`.

⚠️ **O erro clássico: aplicar o prefixo de cinema («8K, fotorrealista, cinematográfico») a um
UGC.** Sai um comercial de carro, e perde-se exatamente o que fazia o UGC converter. O vídeo
estilo criador funciona **porque não parece anúncio**.

Os blocos vão em inglês: é o idioma em que os modelos respondem melhor e derivam menos. O roteiro
falado vai em português; o prompt, em inglês.

---

## BLOCO A · UGC de celular

Pra UGC selfie, depoimento, entrevista de rua e confessional: tudo que tem que parecer gravado
por uma pessoa com o telefone dela.

```
[Visual Style / Texture]
Shot on a modern smartphone, vertical 9:16. Photoreal, unpolished, self-filmed. NOT cinematic,
NOT advertising, NOT a 3D render, NOT a studio set. Slight digital noise in the shadows, mild lens
breathing, one micro focus-hunt allowed. It should look like a video a real person actually posted.
Lighting: available light only — one large window at 45 degrees, soft falloff, no fill, no bounce,
no rim light, no ring-light catchlight. The shadow side of the face stays genuinely dark.
Colour: muted, cool white balance drifting warm. 60:30:10 — desaturated room neutrals / warm skin /
one saturated accent object.
Camera: phone at eye level on a small tripod, framing a few degrees off-centre, micro handheld drift
even when locked off. 26mm equivalent, mild wide-angle face rounding at close range.
Skin: pore-level realism — visible pores, uneven texture, capillary flush on cheeks and ear tips,
faint shine on forehead and nose bridge. No smoothing, no beauty filter.
Physics: real weight and inertia on every object, correct contact shadows, nothing floats.
Composition: head room slightly tight, subject off-centre, background lived-in and asymmetric.
Technical: 30fps, natural motion blur, no stabilisation gloss, no jitter, no slow motion.
```

## BLOCO B · Mini-ficção

Pra cenas com atores, esquetes, situações, mundos alterados com gente dentro.

```
[Visual Style / Texture]
Live-action short film, vertical 9:16, photoreal. Physical cine lens, 180-degree shutter motion
blur, 24fps. Naturalistic, not glossy — practical lighting sources visible in frame where possible.
Colour: 60:30:10 — dominant / secondary / accent, muted and desaturated, no LUT look, no orange-teal.
Skin: pore-level realism — vellus hair, asymmetric moles, capillary flush, pore shadows matching the
on-set light direction.
Acting: restrained. Micro-pauses before reactions, precise eye-line, living eyes with catch-lights,
visible chest rise from breathing. Nobody stands still waiting for their line — every character is
doing something before they speak.
Physics: gravity and inertia respected, mass has real weight, correct contact shadows.
Composition: rule of thirds, every person already moving from frame one.
Technical: 24fps smooth motion, no jitter, no slow motion unless specified.
```

## BLOCO C · Cinema

Pra escala, metáfora, POV, ASMR, cinema, produto herói e detalhe artesanal: tudo que tem que
impressionar.

```
[Visual Style / Texture]
High-end commercial cinematography, vertical 9:16, photoreal live action. Anamorphic prime lenses,
shallow depth of field, 180-degree shutter motion blur, 24fps. Volumetric atmosphere — real haze,
dust motes and airborne particles catching every light source. Practical lighting sources visible in
frame wherever possible, hard directional key with deep unlifted shadows, no flat fill.
Colour: 60:30:10, restrained and filmic. Deep desaturated shadows, warm highlights, one single
saturated accent colour per shot and never more.
Physics: absolute priority. Real mass, real inertia, correct contact shadows, secondary motion on
everything that moves. Objects have weight when they fall and when they stop. Nothing floats, nothing
drifts, nothing intersects.
Materials: pore-level and grain-level realism — brushed metal, worn plastic, dusty glass, scuffed
concrete, fingerprints on screens.
Scale: whenever a size relationship is described, it must read unmistakably in frame — a human
silhouette for reference wherever possible.
Technical: 24fps, cinematic motion blur, no jitter, no stabilisation gloss, no digital sharpening
halo, no LUT look, no orange-and-teal grade.
```

**Nota de escala:** em vertical 9:16 a profundidade manda sobre a largura. Os conceitos de escala se
constroem **pra cima e pro fundo**, nunca pros lados: é a diferença entre um plano grande
impressionar ou se ler apertado.

## BLOCO D · Estilizado / não fotorrealista

Pra objeto que fala, mascote e mundo alterado quando o mundo é de outro material: massinha,
maquete, feltro, desenho. **Aqui não se busca realismo, busca-se coerência**: que se veja feito de
propósito.

```
[Visual Style / Texture]
Stylised animation, vertical 9:16, deliberately non-photoreal and fully committed to its own
material. ONE material and ONE technique for the entire video, never mixed:
<escolha um: hand-modelled plasticine with visible fingerprints and tool marks / felt and fabric
puppetry with visible stitching and fibre / paper cut-out with real paper grain and drop shadows /
matte-painted 2D with visible brush texture>.
Lighting: a single practical light source with a real, readable direction. Soft contact shadows that
sit the subject in its world. No ambient glow with no source.
Colour: a locked palette of four colours plus one accent, stated once and never exceeded.
Physics: exaggerated but consistent — squash and stretch, real anticipation before every movement,
real weight on landing. Whatever rule this world breaks, it breaks it the same way every time.
Camera: simple and motivated. Slow push, slow reveal, locked-off frames. No floating drifts.
Technical: consistent frame rate, no morphing or melting between frames, no photoreal skin, no
mixing of techniques, no realistic human faces.
```

⚠️ **A regra deste bloco: um material, uma técnica, uma regra quebrada.** Duas regras quebradas ao
mesmo tempo e o mundo se desfaz. E o `no morphing or melting between frames` não é decorativo: é a
falha característica do estilizado gerado.

---

## A combinação que costuma ser a boa

Quando um conceito quer impressionar **e** converter:

> **Textura C (cinema) pro gancho de 0-3 s · textura A (UGC) pro corpo.**

Espetáculo pra entrarem, credibilidade pra ficarem. São **duas passadas diferentes** e cada uma
leva o bloco de textura inteiro, nunca um misturado.

🔴 **E como aqui não se monta na mão** (`ritmo.md`), as duas passadas se unem **encadeando com
`extend`** ou com o último frame como ponte: a passada de cinema não pode terminar em preto nem em
letreiro, e a de UGC arranca do último frame dela. Se o conceito não aguenta esse engate,
escolhe-se **uma só textura**: misturar duas passadas que não colam é pior que abrir mão do contraste.

---

## 🔴 As cores se nomeiam em positivo

As palavras de grading por negação ou por termo técnico **devolvem preto e branco** mais vezes do
que funcionam: «dessaturado», «monocromático», «claro-escuro», «crushed blacks» a seco. O modelo
obedece demais.

- ✅ «âmbar quente e marrom profundo» · «azul meia-noite atravessado por laranja de brasa»
- ❌ «dessaturado» · «monocromático» · «claro-escuro» · «paleta apagada»

**E a luz que não se descreve se movendo renderiza morta.** Se quer tremular, escreve-se: «luz
prática baixa que tremula de leve e nunca fica parada».

⚠️ **Derivar o look do assunto, não herdar do projeto anterior.** A armadilha padrão é o tungstênio
âmbar com sombras profundas: é genuinamente bonito e genuinamente errado pra maioria das peças.

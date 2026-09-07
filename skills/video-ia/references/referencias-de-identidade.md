# As três referências de identidade · se aparece uma pessoa real

Quando aparece uma pessoa real, dá-se ao modelo **três imagens da mesma pessoa, sempre juntas**: o
close, a folha de personagem e a de rosto + corpo inteiro. Com uma só a semelhança falha; com as
três, a identidade aguenta quando a pessoa vira a cabeça.

**Se ela já tem e funcionam, usam-se como estão.** Nunca se regenera uma referência que funciona
pra encaixar neste modelo: cada regeneração se afasta da pessoa real.

Se não tem, o bloco 1 do Markdown leva estes três prompts, **nesta ordem**, porque cada um usa o
anterior como referência. Geram-se num gerador de imagens anexando a foto real. Na Agnes
(`imagens-agnes`, custo zero): `--ref foto-real.png`, no máximo 2 referências por imagem.

## Antes: a impressão digital da identidade
Um bloco literal de traços que se cola **igual** nos três prompts e no prompt do vídeo. Se
reescrever com outras palavras no terceiro, o terceiro sai com outra cara.

```markdown
Traços invariantes:
- Estrutura facial:
- Olhos:
- Nariz:
- Boca e mandíbula:
- Cabelo e linha frontal:
- Pele e marcas:
- Proporções corporais (altura em cm):
- Figurino exato:
- Acessórios:
```

## 1 · O close · a partir da foto real
O rosto inteiro, muito perto, sem retoque. É a que leva a textura da pele, e a que serve de rosto
pras outras duas.

```text
Photorealistic extreme close-up portrait of the SAME person as the attached photo(s), portrait 4:5.
The face fills the frame from the hairline to just below the chin. Eye level, direct gaze into the
lens, neutral expression, mouth closed, natural slight asymmetry kept.
Shot like a phone front camera at about 30 cm: slight wide-angle perspective, shallow natural
depth, catchlights from a window on the left.
Skin: real texture — visible pores, a little oil sheen on the forehead and nose, fine lines,
uneven tone. Individual hairs visible in the eyebrows and beard. Hair as in the photo.
Background: plain dark charcoal-grey wall, softly out of focus. The collar of a plain white
crew-neck t-shirt just visible at the bottom.
Identity: [IDENTITY].
No retouching, no beauty filter, no makeup, no smoothing, no grading, no text, no watermark.
```

## 2 · A folha de personagem · anexando o close
Frente, perfil, costas, close, vista de cima e cinco detalhes. Dá ao modelo os lados: a informação
que falta quando a semelhança falha.

```text
Photorealistic character reference sheet of the SAME person as the attached close-up portrait.
Layout: a three-row grid on a flat light-grey (#e6e6e6) seamless studio background, thin white
gutters between panels, small centered labels in light-grey sans-serif capitals above each panel.

Row 1 — three equal head-and-shoulders panels at identical scale and exposure:
  "FRONT": facing camera, natural smile, eyes to lens.
  "SIDE": true 90-degree right profile, neutral.
  "BACK": back of the head and shoulders, showing the hair pattern and the fade at the neck.
Row 2 — two panels:
  "FRONT CLOSE-UP": tight face from forehead to chin, natural smile, eyes to lens.
  "TOP-DOWN VIEW": camera above the head, face tilted down, showing the parting and hair direction.
Row 3 — five small square macro crops:
  "HAIR TEXTURE & FADE", "EYE DETAIL", "BEARD TEXTURE", "SKIN TEXTURE", "T-SHIRT FABRIC".

Identity — take it from the attached portrait and keep it identical in every panel:
[IDENTITY]
Wardrobe in every panel: [WARDROBE] (default: plain white crew-neck cotton t-shirt, no logo).

Lighting: soft, even, shadow-free studio light, neutral white balance, same distance and scale in
every panel of the same row. Skin: real pores, natural sheen, no smoothing, no beauty filter.
Hair: individual strands visible. 85mm look, f/8, minimal distortion.
No props, no text other than the panel labels, no watermark, no grading, no cinematic look.
Aspect 4:3. Output at 2K.
```

Se faltar um painel, reforce a frase da contagem («three rows, ten panels in total»); não mude o
formato.

## 3 · Rosto + corpo inteiro · anexando o close
O corpo de frente e de costas com a roupa exata, e o rosto do close à esquerda. Nos painéis de
corpo o rosto vai cortado: **um só rosto legível por imagem**, pra que o modelo não faça média de
dois. Aqui entra a altura em centímetros: «compleição média» produz um manequim.

```text
Photorealistic two-part reference composite of the SAME person as the attached close-up portrait, 4:3.

Left third — one tight head-and-shoulders portrait: eye level, neutral expression, mouth closed,
looking straight into the lens, on a plain mid-grey (#7f7f7f) seamless background.

Right two-thirds — two full-body standing views of the same person side by side on the same
mid-grey background, identical scale, distance and exposure:
  left: FRONT, arms relaxed at the sides, feet slightly apart, weight even.
  right: BACK, same stance.
In both full-body views the frame crops at the top of the head so the face is NOT readable —
the portrait on the left is the only readable face in this image.

Identity: [IDENTITY]. Height [HEIGHT] cm, [BUILD].
Wardrobe: [WARDROBE]. Describe the fabric, not just the colour: how it falls on this body, where it
creases.

Lighting: soft, even, shadow-free studio light, matte surfaces, neutral white balance.
85mm look, f/8, camera at chest height for the full-body views. No props, no text, no labels,
no watermark, no grading. Output at 2K.
```

## Como as três entram no prompt do vídeo

Sobem-se nesta ordem e declaram-se como a mesma pessoa:

```text
@Image1 — real close-up of <NOME>. TAKE facial identity: bone structure, hairline, skin texture
and asymmetries. IGNORE background, framing and lighting.
@Image2 — multi-panel character sheet of the SAME person. TAKE angles, hair pattern and wardrobe.
IGNORE and never render the panel grid, the printed labels, the grey backdrop and the studio light.
@Image3 — face and full-body composite of the SAME person. TAKE body proportions, height, posture
and the exact garments. IGNORE the grey backdrop and the layout.
<NOME> is the same person in @Image1, @Image2 and @Image3. Identity consistency has absolute
priority over everything else in this prompt: if a shot cannot hold the face, hold the face and
lose the shot.
```

E nas exclusões do prompt, repetir pelo nome: `no panel grid, no printed labels, no caption
strips, no grey studio backdrop`. Sem as duas coisas, as letras das folhas aparecem no vídeo.

**Na Agnes**, onde só entram 2 referências por imagem, os keyframes de cada cena usam o close
(@Image1) mais a folha de personagem, ou o close mais o keyframe anterior, conforme o que a cena
precisa (cara ou continuidade).

## A prova de cinco segundos
Antes de gastar na peça: um clipe curto da pessoa virando a cabeça, piscando e dizendo duas
palavras. Se a cara aguenta ali, aguenta no anúncio. Se deriva, corrigem-se as referências, não o
anúncio.

## Onde se guardam
`anuncios/_apresentadores/<nome>/`: as três imagens e a impressão digital. Um apresentador serve a
muitos anúncios; **trocá-lo quebra o reconhecimento**, que é a única coisa que faz o quarto anúncio
funcionar melhor que o primeiro.

## E se o personagem é inventado
Não precisa de imagens. Descreve-se uma vez com **três traços irrepetíveis** (uma pinta, uma
assimetria, um objeto que usa), a roupa fechada, e fecha-se com «identical in every single frame».
Esse bloco se guarda e reutiliza literal se o personagem voltar. → `identidade-e-voz.md`, via A.
Na Agnes, mesmo o personagem inventado precisa de uma âncora-mãe em imagem (text2img) da qual as
demais vistas derivam por img2img: sem `seed` de imagem, é o único jeito de ser o mesmo indivíduo.

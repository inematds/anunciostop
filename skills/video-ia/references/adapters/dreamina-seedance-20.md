# Adaptador · Dreamina one-take e Seedance 2.0 modular (pago, sem configuração local)

## Alcance e evidência

Perfil de agosto de 2026. Usa-se pela web do provedor; nada se configura no `.env` deste pacote.

Capacidade oficial do Seedance 2.0:

- 15 segundos por geração;
- até nove imagens, três vídeos e três áudios.

Na conta medida, a Dreamina ofereceu 30 s com 2.0 Fast e 2.5. Em nove gerações observadas,
nenhuma executou cortes: produziu uma tomada contínua. A caixa rejeitou prompts acima de
aproximadamente 4.000 **bytes**. São medições dessa superfície, não leis universais do modelo.

## Escolher trilho

### Dreamina one-take

Usar quando o conceito cabe em:

- um cenário;
- um corpo ou sujeito principal;
- uma direção de câmera;
- até quatro ações diferentes;
- diálogo contínuo ou voz off;
- 30 s oferecidos pela interface concreta.

Não pedir contraplano, sequência de locações ou muitos beats. Se o conceito precisa de cortes,
picar em gerações separadas e montar.

### Seedance 2.0 modular

Usar 15 s como capacidade base oficial. Adequado pra:

- testar ganchos;
- transformações por peças;
- movimentos concretos;
- insertos de produto;
- dois módulos de 15 s que formem uma peça de 30 s.

Cada módulo deve ter estado de entrada e saída compatível e funcionar, quando possível, como
unidade avaliável.

## Modelo Dreamina one-take

```text
[FORMAT]
Vertical 9:16, 30 seconds, Brazil. One continuous take of <what happens>.

ONE SHOT ONLY. Exclude any cut, dissolve or camera switch. The camera follows one continuous,
motivated vector from the first frame until the CTA.

CHARACTER: <identity, age, skin, hair and distinctive marks>. Exact wardrobe garment by garment:
<materials, colours, footwear and accessories>. <performance and eye contact>.

ACCENT: Brazilian Portuguese, natural and conversational. Never European Portuguese, never a
neutral or synthetic accent.

SCENE LOCK: <closed, ordinary location described from the camera; geometry and one unambiguous anchor>.

LIGHT: <motivated practical source>. Neutral, real exposure. <specific exclusions>.

TEXTURE: Photographic skin texture, pores, asymmetry, ordinary surfaces, restrained colour.

SOUND: Voice starts on frame zero and runs as one continuous take, with no pause longer than half a
second between sentences. <ambient sound>.

CAMERA: <one vector and constant behaviour>. The subject keeps moving for a credible reason so the
camera retains motion.

0-2s <camera movement first>. Mouth clearly visible from the front; already speaking on frame one.
P1: '<all dialogue in one continuous line; 75-96 words fit in 30 s at this surface's measured rate>'.
2-6s The camera keeps <movement> at the same speed. <action/event>.
6-12s The camera keeps <movement> at the same speed. <action/event>.
12-20s The camera keeps <movement> at the same speed. <action/event>.
20-30s The camera is still <moving>. <CTA and final state>.

Strictly exclude: any European or neutral Portuguese accent; any cut or dissolve; a static
locked-off camera; the camera stopping or reversing; any silent pause before speech; any gap in
speech longer than half a second; a second person unless approved; boiler suit, overalls, uniform
or matching outfits; unapproved readable text; subtitles; watermarks; extra fingers; deformed
hands; poreless skin; beauty filter; haze; unrequested music; unrequested slow motion.
All characters speak Brazilian Portuguese.
```

Em `Strictly exclude`, escrever os elementos proibidos em positivo: `any cut`, não `no cut`.

## Regras medidas de diálogo

- Um único `P1:` com todo o diálogo.
- Primeiro trecho de dois segundos ou menos.
- Boca visível e falando desde o frame zero se há lip-sync.
- Nomear a primeira palavra quando o arranque é crítico.
- Escrever números por extenso e evitar siglas.
- **Teto de fala medido nesta superfície: 2,5-3,2 palavras/s (150-192 ppm).** Em 30 s cabem 75-96
  palavras ditas. É o teto da interface, **não** o orçamento do roteiro: esse sai do trilho em
  `ritmo.md`. Se o trilho pede mais do que cabe (um talking-head de 30 s pede 100-120), subir
  duração ou partir em dois módulos. **Não cortar o roteiro até caber.**
- CTA em duas frases no máximo.
- Cortar uma cauda vazia pode ser válido; um silêncio central se corrige no prompt.

## Câmera, corpo e cena

- Repetir o verbo de movimento de câmera em cada trecho.
- Um tamanho de plano não substitui um verbo de movimento.
- Dar ao sujeito um motivo contínuo pra se mover; a câmera observada se acopla a ele.
- Colocar a quietude, se existe, no fim.
- Evitar uma ação corporal complexa logo antes de olhar pra câmera.
- Preferir descobertas a entradas de personagens.
- Descrever roupa peça por peça.
- Em exteriores, usar uma âncora inequívoca ou escolher uma locação fechada.
- Manter poucos figurantes, parados, desfocados e secundários.
- Não descrever a câmera como objeto dentro do `SCENE LOCK`.

## Gate modular do 2.0

- [ ] Cada módulo dura 15 s ou o que a interface expõe.
- [ ] Character, scene e product locks se repetem literais.
- [ ] Estados de saída e entrada permitem emendar.
- [ ] O segundo módulo não repete o gancho sem acrescentar.

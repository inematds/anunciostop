# overlay-fallback — pipeline de overlays sem libass

**Quando usar:** quando o seu `ffmpeg` NÃO traz `libass`/`subtitles` nem `drawtext` (confira com
`ffmpeg -filters | grep -E 'subtitles|drawtext'`). Se traz, prefira o caminho direto do SKILL.md
(`ass=`): mais rápido e sem Pillow. Este pipeline põe hook + legendas + chip CTA + endcard POR CIMA
com ffmpeg, rápido e em 1080.

**Ideia:** renderizar cada texto como PNG transparente (Pillow) → assar TUDO numa pista
transparente `qtrle` com alfa (frames por intervalos) → **um só `overlay`** sobre a base. Encadear
100+ overlays é lentíssimo (profundidade de grafo); a pista única resolve.

## Configuração

- **Fonte:** variável `CAPTION_FONT=/caminho/fonte.ttf`. Sem ela, o script procura Inter, DejaVu
  Sans Bold e Liberation Sans Bold (Linux), Helvetica Neue (Mac) e Arial Bold (Windows).
- **Cor da palavra-chave:** variável `KEYWORD_COLOR=#E8703A` (a cor de acento da ficha de marca).
  Padrão violeta se não definida. A mesma cor vai no chip CTA e no contorno do endcard.
- Com fonte `.ttf`/`.otf` (o caso normal no Linux), bold, black e medium resolvem pra **mesma
  face**: o hook não sai condensado como sairia com a `.ttc` de várias faces. Pra ter pesos
  diferentes, aponte `CAPTION_FONT` pra uma família com vários arquivos e ajuste `_IDX` no script.

## Fluxo (depois do corte aprovado + `captions.json` de captions.py --mode pages)
```bash
cd <anuncios/criativos/<slug>>
# 1) marks (chip/CTA + endcard) e eventos de sfx a partir do transcript do corte
python3 .../overlay-fallback/compute_marks.py            # -> edicao/marks.json, edicao/sfx_events.json
# 2) overlays PNG (legendas pill+karaokê + hook + chip + endcard)
KEYWORD_COLOR='#E8703A' python3 .../overlay-fallback/render_overlays.py   # -> edicao/ov/*.png, overlays.json
# 3) pista transparente única
python3 .../overlay-fallback/build_track.py <DUR> edicao/track.mov
# 4) base em 1080
ffmpeg -y -i edicao/corte-final.mp4 -vf scale=1080:1920:flags=lanczos -c:v libx264 -crf 17 -c:a copy edicao/base1080.mp4
# 5) áudio: mix-sfx -> music-duck (make_bed.py dá cama sutil) -> master-audio
# 6) composição final: base + track + áudio masterizado (um overlay)
ffmpeg -y -i edicao/base1080.mp4 -i edicao/track.mov -i <audio-masterizado> \
  -filter_complex "[0:v][1:v]overlay=0:0:format=auto[v]" -map "[v]" -map 2:a \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart renders/<slug>.mp4
```

## Regras de estilo
- **Legendas = pastilha** (em `render_overlays.py`): fundo `rgba(10,7,18,.80)`, borda branca `.10`
  2px, radius 18, pad 16x32, bold ~48px, **karaokê** (não dita .38 / dita .85 / ativa 1.0),
  **palavra-chave na cor da marca sempre**. NÃO legenda só de contorno. Centro ~y812 (nível do
  microfone).
- **Chip CTA sobre o peito (~y640), NUNCA sobre a cara.**
- **Endcard** = pastilha de marca (não texto branco solto que pareça legenda).
- **Entregar o `.srt` em subpasta** (`renders/extras/`), NUNCA junto do `.mp4` com o mesmo nome.
- **1080×1920**, não 4K (Instagram/TikTok recomprimem; o pipeline 4K é inviável).

Os scripts esperam `edicao/captions.json`, `edicao/transcript-final.json`, `edicao/corte-final.mp4`,
`edicao/sfx/`. São um PONTO DE PARTIDA: ajuste timestamps/posições por peça.

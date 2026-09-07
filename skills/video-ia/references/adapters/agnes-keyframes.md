# Adaptador · Agnes por keyframes (custo zero)

## Alcance e data

Perfil escrito em 2026-09-06 a partir de medições reais da API (`~/projetos/agnes-nei/NOTAS-API.md`).
**Provedor padrão do curso**: imagem e vídeo a US$ 0, sem crédito, com chave em `AGNES_API_KEY`.

O que a Agnes é e não é:

| | |
|---|---|
| **É** | Gerador de **imagem** (`agnes-image-2.1-flash`, text2img e img2img) e de **vídeo por keyframes** (`agnes-video-v2.0`: dá-se o frame A e o frame B, ela interpola) |
| **Não é** | Text-to-video com diálogo. **Não gera voz, não faz lip-sync, não executa cortes dentro do clipe.** Não edita vídeo (sem via E) |

Consequência direta: **na Agnes só existe a via D (voz off).** A voz vem do inemavox (TTS com voz
clonada, engine `chatterbox`) ou gravada, e se monta em cima no `/anuncio-edita`. É a via mais
segura do catálogo, então o custo zero não é a única vantagem.

## A unidade de produção: o clipe por keyframes

| Fato medido | Valor |
|---|---|
| Duração por clipe | `num_frames / frame_rate`; `num_frames` segue a regra **8n+1** e tem **teto por resolução** (tabela abaixo) |
| Keyframes por clipe | 2 (A→B) funciona e mantém o personagem; 3+ aceitos |
| Referência de imagem | Base64 local funciona (não precisa hospedar) |
| `seed` | Existe no vídeo (não na imagem) |
| Tempo | 19-50 s por clipe curto |
| **Rate limit** | **6 requisições por minuto** medidas (HTTP 429). A fila deste pacote usa 5/min por folga |
| Tamanho real | A resposta mente: `1312x736` pedido vira `1280x704` no arquivo. **Sempre conferir com ffprobe** |
| Falhas transitórias | ~1/3 de HTTP 503 na imagem; retry com backoff resolve |
| Modelo alternativo | Existe `agnes-video-2.5-flash` (mesmo rate limit), mas com esquema diferente (`seconds` 4-12 em vez de `num_frames`, só 720p). Este adaptador usa o `agnes-video-v2.0` |

**Teto de `num_frames` por resolução** (o lado menor decide o tier; a proporção não muda o teto):

| Tier | Lado menor | `num_frames` máx. | Duração máx. @ 24 fps |
|---|---|---:|---:|
| 480p | ≤ 480 | 961 | 40 s |
| **720p** | ≤ 736 | **481** | **20 s** |
| 1080p | > 736 | 241 | 10 s |

Pra 9:16 em 720p (`736x1312`): clipes de até **20 s**. Em 1080p só 10 s por clipe, então o padrão
do curso é **720p** e o upscale, se precisar, é em pós.

**Regra de arquitetura que sai disso:** a peça de 30 s são **2 clipes de ~15 s** (361 frames), ou
3 de ~10 s (241 frames). A peça de 60 s, 4 clipes. Cada clipe tem um par de imagens (A e B) gerado
antes. → `ritmo.md` §Modular

## Pipeline por peça

```
1. Âncora de identidade (text2img)          → 1 imagem-mãe do personagem/produto
2. Derivadas por img2img (--ref âncora)      → folha, vistas, figurino (máx. 2 refs por imagem)
3. Locação (text2img, com o bloco de textura literal)
4. Keyframes: por clipe, A e B               → B se gera a partir de A (--ref A + âncora)
5. Vídeo: POST /v1/videos, mode keyframes    → num_frames 8n+1, 24 fps, 1 clipe por vez, ≤5/min
6. Voz: inemavox TTS (chatterbox, voz da ficha) ou gravação
7. /anuncio-edita: montar clipes + voz + legendas + master
```

Imagens via `imagens-agnes` (`~/projetos/imagens-agnes/gerar.py`):

```bash
cd ~/projetos/imagens-agnes
python3 gerar.py "<prompt em inglês>" -o anuncios/criativos/<slug>/kf-01a.png --ratio 9:16 --size 1K
python3 gerar.py "<prompt em inglês>" -o anuncios/criativos/<slug>/kf-01b.png --ratio 9:16 --ref kf-01a.png --ref ancora.png
```

Vídeo: o `videoanima` (`~/projetos/videoanima-skill/rodar.py --video agnes`) já implementa fila,
retry e keyframes; pra um anúncio avulso, a chamada direta é:

```bash
# AGNES_API_KEY carregada em runtime de ~/projetos/agnes-nei/.env
python3 - <<'PY'
import json, base64, os, time, urllib.request
key = os.environ["AGNES_API_KEY"]
def b64(p): return "data:image/png;base64," + base64.b64encode(open(p,"rb").read()).decode()
body = {"model":"agnes-video-v2.0","prompt":"<prompt do clipe, em inglês>",
        "num_frames":361,"frame_rate":24,"width":736,"height":1312,
        "extra_body":{"image":[b64("kf-01a.png"), b64("kf-01b.png")],"mode":"keyframes"}}
r = urllib.request.Request("https://apihub.agnes-ai.com/v1/videos", data=json.dumps(body).encode(),
    headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"})
print(urllib.request.urlopen(r).read().decode())   # devolve video_id; consultar até completed
PY
```

## Regras de prompt medidas (imagem)

- **Prompt em INGLÊS, sempre.** Em português o filtro de conteúdo devolve HTTP 400 em pedido legítimo.
- **`size` em pixels explícito** (`736x1312` pra 9:16) quando há referência: em img2img o `ratio`
  é ignorado e vira quadrado.
- **No máximo 2 referências.** 3+ saturam; 5 = confete e prompt ignorado. Muitos personagens →
  uma âncora de grupo.
- **Sem pose frontal simétrica** em personagens (sai cabeça dupla). Perfil ou três-quartos, e
  `exactly one head, one body` em positivo. Nunca «no two heads»: vira atrator.
- **Descritor de estilo só estético.** «Expressive eyes», «fur», «children's book» injetam
  personagem na paisagem. No estilo, só luz, cor e render.
- **Estilo sequestra o assunto**: «futurista» prateou um esquilo ruivo. Reforçar o atributo do
  sujeito depois do estilo.
- **Texto:** só curto e grande (uma palavra, um título). Texto denso vira sopa de letras. Revisar
  grafia à mão sempre. Pra letreiros e interfaces, preferir HTML capturado → `imagens.md`.
- **Consistência:** não há `seed` na imagem. Mesmo personagem = img2img com 1-2 âncoras; model
  sheet derivando de uma âncora-mãe, não gerando vistas em paralelo.
- **Ref ≤ 10 MB**: imagem 4K não serve de referência. Trabalhar em 1K (padrão) ou 2K.
- **Baixar na hora**: a URL de saída é temporária.

## Regras de prompt (vídeo por keyframes)

O prompt de vídeo na Agnes é curto e descreve **o movimento entre A e B**, não a cena (a cena já
está nos frames). Estrutura:

```text
[MOTION]
<uma ação principal, escrita como resultado visível: "the camera pushes in slowly while she turns
her head from the window to the lens; her hand lowers the mug to the table">
[CAMERA]
<um vetor, constante: push-in / orbit right / static with handheld drift>
[CONTINUITY]
Same person, same wardrobe, same room and same light as in both keyframes. No new objects appear.
Nothing morphs. Smooth, physically plausible motion, real weight and inertia.
[NEGATIVE]
no text, no watermark, no extra limbs, no second face, no duplicate person, no flicker.
```

- **Uma ação por clipe.** Duas ações competindo produzem morphing.
- **A e B moderadamente diferentes.** Se são diferentes demais, a interpolação inventa e deforma.
  B se gera a partir de A mudando **uma** dimensão (pose, câmera ou luz), nunca várias.
- **Sem diálogo, sem lábios.** Nos negativos: `no lip movement, nobody speaks`. A voz entra depois.
- **Final vivo:** o frame B de um clipe é o frame A do seguinte. Desenhar B «vivo mas estável»:
  pose clara, sem motion blur.
- **`seed` fixo** por peça pra reproduzir um clipe que saiu bem com pequenas mudanças de prompt.
- Ritmo: como não há cortes dentro do clipe, o ritmo vive na **sucessão de clipes** (10-15 s cada)
  e no **áudio** montado em cima. Pra ritmo dinâmico, clipes mais curtos (241 frames = 10 s).
- **Narração primeiro:** quando a voz é sintetizada, gera-se o áudio antes e a duração da fala de
  cada beat define o `num_frames` do clipe correspondente (arredondado pra 8n+1). Evita clipe
  sobrando ou faltando na montagem.

## Gate

- [ ] Via D declarada; nenhum plano pede boca falando.
- [ ] Um par de keyframes por clipe, ambos aprovados (identidade, texto, escala) antes do vídeo.
- [ ] Prompts de imagem em inglês, com no máximo 2 refs, sem pose frontal simétrica.
- [ ] `num_frames` respeita 8n+1 e o teto do tier (481 em 720p); duração total = soma dos clipes.
- [ ] Fila respeita 5 req/min (limite medido: 6); retry com backoff nos 503.
- [ ] Voz sintetizada (inemavox) ou gravada, com o roteiro no bloco 2 do dossiê, no orçamento de
      **voz off de cinema (126-160 ppm)**.
- [ ] Arquivo real conferido com ffprobe (resolução e duração), não o JSON da resposta.
- [ ] Último frame de cada clipe extraído do MP4 (não print) pra ser o A do seguinte.

---
name: anuncio-edita
description: Pós-produção de anúncios GERADOS com IA (saídos do /video-ia): junta módulos de ≤30 s na peça final, cuida das costuras, decide e monta a pista de voz, põe legendas sóbrias que ficam bem, acrescenta o letreiro de fechamento e masteriza pra Meta/Instagram. Entrada flexível — um clipe de 30 s, uma peça de 90 s já montada, ou N módulos soltos pra montar. Critério de editor sênior, edição pouco carregada, intervenções extras só se agregam e com OK do usuário. USAR quando o usuário disser "/anuncio-edita", "edita o anúncio", "junta os módulos", "monta o anúncio inteiro", "põe legenda no anúncio", "prepara o anúncio pra Meta", ou passar MP4s gerados com IA pedindo pra deixar prontos pra publicar. NÃO é pra bruto gravado com câmera (isso é reel-edita-inema) nem pra julgar se uma geração se conserva ou regenera (isso é /auditor-video-ia).
---

# /anuncio-edita — Pós-produção de anúncios gerados com IA

Fechar o círculo: `/video-ia` (prompts) → geração → `/auditor-video-ia` (QA da geração) →
**`/anuncio-edita` (esta skill)** → Meta.

## A doutrina, antes do pipeline

**A melhor edição é a que não se nota.** O material entra já dirigido (câmera, ritmo e atuação
foram decididos pelo `/video-ia` no prompt), então aqui não se redirige: monta-se, limpa-se e
entrega-se. Um vídeo gerado com camadas de motion graphics em cima **delata a geração** e quebra o
registro UGC que converte.

- **Intervenção mínima por padrão.** O que sempre se faz: montar, pista de voz, legendas,
  letreiro, master. Todo o resto é opcional e se PROPÕE antes de fazer.
- **Se algo pede um extra, diz-se com motivo** («aqui um SFX diegético venderia o golpe da caixa»)
  e espera-se o OK. O menu de extras e o critério → `references/intervencoes.md`.
- **Nada de zoom artificial, whoosh de banco nem transição engraçadinha** sobre vídeo gerado. O
  corte seco em silêncio é a transição da casa.
- 🔴 Trabalhar e entregar em **1080×1920** (Instagram e TikTok entregam em 1080; 4K estoura
  memória). Sem fade pra preto no fim, salvo se o conceito pedir.

## Ferramentas (uma só fonte de verdade)

Esta skill traz o próprio motor de edição em `scripts/`:

| Ferramenta | Caminho | Pra quê |
|---|---|---|
| `captions.py` | `scripts/captions.py` | Páginas/beats de legenda word-level, palavra-chave destacada |
| `jargon-fix.py` | `scripts/jargon-fix.py` | Corrigir jargão que o Whisper erra (Cloud→Claude, nomes próprios…) |
| `export-srt.py` | `scripts/export-srt.py` | SRT sidecar pra subir na Meta |
| `overlay-fallback/` | `scripts/overlay-fallback/` | Queimar legendas via PNG (Pillow) → pista qtrle → UM overlay. Pra ffmpeg **sem** libass |
| `master-audio.py` | `scripts/master-audio.py` | Loudnorm EBU R128 em duas passadas |

**Dois caminhos pra queimar legenda, conforme o ffmpeg do aluno:**

```bash
ffmpeg -hide_banner -filters | grep -E ' (subtitles|ass|drawtext) '
```

- **Tem `subtitles`/`ass` (Ubuntu e a maioria dos builds Linux):** gerar o SRT com `export-srt.py`,
  converter pra ASS com o estilo da casa e queimar direto:
  `ffmpeg -i base.mp4 -vf "ass=legendas.ass" -c:v libx264 -crf 18 -c:a copy out.mp4`.
  Mais rápido e sem Pillow.
- **Não tem (builds mínimos, alguns Macs):** a via `overlay-fallback/`. Fonte via variável
  `CAPTION_FONT`; cor da palavra-chave via `KEYWORD_COLOR` (vem da ficha de marca).

Voz: quando um remendo de palavra ou a locução inteira vêm de voz clonada, o padrão INEMA é o
**inemavox** (engine `chatterbox`, voz da ficha do apresentador). ElevenLabs só se a ficha disser.

## F0 · Ingestão e diagnóstico

A entrada NÃO tem padrão fixo: pode ser 1 clipe de 30 s, a peça de 90 s já montada pelo usuário, ou
N módulos soltos. Primeiro olha-se TUDO, depois pergunta-se o mínimo.

1. `ffprobe` de cada arquivo: duração, resolução, fps, codecs, loudness de partida.
2. **Transcrever** cada clipe (Whisper com vocabulário do dossiê como `initial_prompt`) e extrair
   4-6 frames por clipe. Ver o que há de verdade, não assumir.
3. Localizar o **dossiê do anúncio** em `anuncios/roteiros/`: traz o roteiro verbatim, os timings,
   a ordem dos módulos, os assets (telas assadas, locução original) e as decisões travadas. Se não
   há dossiê, reconstruir o roteiro a partir da transcrição.
4. Diagnóstico em 5 linhas: o que chega, ordem proposta, onde estão as costuras, caudas sobrando
   (a plataforma arredonda: pede 28 s, dá 30), e se a voz é clone, sintetizada ou real.
5. **Perguntar SÓ o que falta** (nunca o que o dossiê já diz):
   - Pista de voz definitiva: a do vídeo (clone), a sintetizada (inemavox) ou a gravação original
     do apresentador em cima?
   - Letreiro de fechamento: só logo, logo + oferta literal da ficha de marca, ou nada?
   - Algo pra substituir em pós (tela corner-pin, palavra remendada)?

## F1 · Montagem (só se chegam módulos soltos)

1. **Ordenar pelo roteiro** (a transcrição diz qual módulo é qual, não o nome do arquivo).
2. **Cortar caudas** de cada módulo contra o áudio: o corte vai no silêncio depois da última
   palavra do módulo, deixando ~0,15 s de ar. Nunca cortar no meio de movimento brusco de câmera
   se o silêncio permitir.
3. **Uniformizar** (mesmo codec/fps/resolução → recode uniforme a 1080×1920 CRF 18 se diferem) e
   concatenar. Corte de vídeo seco na costura.
4. **Costura de áudio:** crossfade de ambiente de 0,15-0,25 s (`acrossfade`) pra que o room tone
   não salte. A voz não se cruza: as costuras foram desenhadas em silêncio de locução.
5. **Verificar a costura:** extrair 2 frames de cada lado e olhar (continuidade de sala/figurante),
   e ouvir o trecho transcrevendo: nenhuma palavra partida.

Na Agnes (via D), os clipes chegam mudos: a montagem é vídeo primeiro, voz off inteira em cima
depois, alinhada por beat do roteiro. A costura de voz não existe porque a voz é uma pista só.

## F2 · Pista de voz

Três casos, por ordem de frequência:

- **Clone do vídeo OK** → não tocar. É a via padrão (a emoção integrada ganha).
- **Uma palavra mal dita** → remendo com o clone do apresentador (inemavox, mesma referência de
  voz da ficha) e substituir SÓ essa frase. Não se regenera vídeo por um erro de palavra.
- **O usuário manda a gravação original como pista definitiva** → alinhar por timings word-level
  (transcrição das duas pistas), montar em cima conservando o ambiente do vídeo por baixo (voz
  gerada fora, ambiente dentro), e revisar lip-sync nos trechos a câmera: se deriva >2-3 frames
  num trecho, micro time-stretch dessa frase (`atempo` 0,97-1,03), nunca da pista inteira.

## F3 · Legendas (sempre, e sóbrias)

O estilo da casa: **pastilha escura, 2-4 palavras por página, palavra-chave na cor de acento da
marca** (a da ficha), karaokê sutil. Sem animação chamativa.

```bash
# 1. Transcript word-level do master de áudio + correção de jargão
python3 ~/.claude/skills/anuncio-edita/scripts/jargon-fix.py --in edicao/transcript.json
# 2. Páginas sóbrias
python3 ~/.claude/skills/anuncio-edita/scripts/captions.py \
  --transcript edicao/transcript.json --out edicao/captions.json --mode pages
# 3. Queimar: via libass (ass=) ou via overlay-fallback (ver README dele)
# 4. SRT sidecar pra Meta
python3 ~/.claude/skills/anuncio-edita/scripts/export-srt.py --captions edicao/captions.json
```

Regras de posição (não negociáveis):
- **Nível microfone/peito**, nunca no terço inferior (~250-300 px) que tapa a interface do
  Instagram/Meta.
- 🔴 **A legenda nunca tapa uma cara.** Verificar com frames os trechos onde a cara muda de posição.
- **Ler `captions.json` INTEIRO antes de queimar**: um erro de Whisper na tela é um anúncio
  queimado. Erro de jargão novo → acrescentar ao `jargon.json`.
- Em anúncio a voz é contínua → legendas contínuas (sem janelas), salvo trecho mudo por desenho.

## F4 · Letreiro de fechamento e substituições

- **Letreiro:** overlay PNG (Pillow, tipografia da marca) nos últimos 2-3 s SOBRE o vídeo vivo:
  sem end card preta, sem freeze. Se leva oferta, a redação é **a literal da ficha de marca**.
  Logo: o caminho que a ficha indica.
- **Corner-pin de tela** (se o render sujou uma tela assada): substituir pelo PNG fonte em
  perspectiva. O critério vem do dossiê (que palavras devem ser lidas).
- Legenda e letreiro não competem: se coincidem no tempo, a legenda sobe ou o letreiro espera.

## F5 · Master

```bash
python3 ~/.claude/skills/anuncio-edita/scripts/master-audio.py --in peca.mp4 --out master.mp4 \
  -I -14 -tp -1.0   # loudness de plataforma social
```
Vídeo: H.264 high, CRF 17-18, `-movflags +faststart`, 1080×1920, fps do material (não converter).

## F6 · QA e entrega

1. **Ver o vídeo final inteiro**: transcrição do master (diz exatamente o roteiro?) + tira de
   frames (costuras invisíveis, legendas legíveis e sem tapar caras, letreiro bem?).
2. Checklist: duração esperada · loudness -14±1 · nenhuma palavra partida nas costuras · texto na
   tela letra-perfeito · sem legenda dupla fantasma · final vivo.
3. **Entregar** em `anuncios/criativos/<slug>/` com a nomenclatura do dossiê
   (`VID-X_ANG_<CONCEITO>_<DUR>S.mp4`) + o SRT numa subpasta `extras/` (nunca ao lado do MP4 com o
   mesmo nome: alguns players carregam sozinhos e parece legenda dobrada).
4. **Registrar no dossiê do anúncio** (seção de registro): o que se montou, que pista de voz, que
   extras se aplicaram e por quê. O dossiê é a memória da peça.
5. Passar o resultado pelo `/auditor-video-ia` se a peça vai pra Meta (postflight).

## Regras duras

- Intervenção mínima; extras só propostos e aprovados.
- Nunca publicar nem agendar. A publicação é um passo à parte e sempre com OK explícito.
- Nunca apagar material: brutos e módulos originais se arquivam, não se sobrescrevem.
- O dossiê do anúncio manda sobre esta skill em decisões de conteúdo (letreiro, oferta, roteiro).
- Erros do Whisper jamais chegam à tela: revisão humana do captions.json sempre.
- Não redirigir o material: se um plano está mal DIRIGIDO, isso é regenerar (auditor), não editar.

## Limites

Não decide estratégia, não escreve prompts de geração (`/video-ia`), não julga se uma geração se
conserva ou regenera (`/auditor-video-ia`), não edita bruto gravado com câmera
(`reel-edita-inema`), não publica.

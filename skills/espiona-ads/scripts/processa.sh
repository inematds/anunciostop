#!/bin/bash
# Processa um vídeo de anúncio: cortes de cena + transcrição Groq + frames.
# Uso: ./processa.sh <caminho_mp4> [idioma]   (idioma padrão: pt)
set -uo pipefail
W="$(cd "$(dirname "$0")" && pwd)"
V="$1"; ID="$(basename "$V" .mp4)"
LANG_WHISPER="${2:-pt}"
OUT="$W/analise/$ID"; mkdir -p "$OUT/frames"

# A chave da Groq: variável de ambiente → .env do projeto → arquivos centrais do usuário.
# Carrega em runtime, nunca copia nem imprime o valor.
if [ -z "${GROQ_API_KEY:-}" ]; then
  for ENV_FILE in "${ENV_FILE:-.env}" ".env.local" "$HOME/projetos/openpcbotv2/.env" "$HOME/projetos/wifi/.env"; do
    if [ -f "$ENV_FILE" ]; then
      K="$(grep -E '^GROQ_API_KEY=' "$ENV_FILE" | head -1 | cut -d= -f2- | tr -d "\"' ")"
      if [ -n "$K" ]; then GROQ_API_KEY="$K"; break; fi
    fi
  done
fi
if [ -z "${GROQ_API_KEY:-}" ]; then
  echo "Falta GROQ_API_KEY. Exporte (export GROQ_API_KEY=...) ou coloque num .env" >&2
  exit 1
fi

DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
FPS=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "$V")
WH=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$V")

# --- 1. Cortes de cena (limiar 0.15) --- ATENÇÃO: precisa de -loglevel info; com -v error devolve 0
ffmpeg -hide_banner -loglevel info -i "$V" -filter:v "select='gt(scene,0.15)',showinfo" -f null - 2>&1 \
  | grep -oE 'pts_time:[0-9.]+' | cut -d: -f2 > "$OUT/cortes.txt"
NCORTES=$(wc -l < "$OUT/cortes.txt" | tr -d ' ')

# --- 2. Áudio + transcrição Groq (whisper-large-v3, segmentos com timestamp) ---
ffmpeg -v error -y -i "$V" -vn -ac 1 -ar 16000 -b:a 64k "$OUT/audio.m4a"
curl -s -m 300 https://api.groq.com/openai/v1/audio/transcriptions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -F "file=@$OUT/audio.m4a" -F "model=whisper-large-v3" \
  -F "response_format=verbose_json" -F "language=$LANG_WHISPER" \
  -F "timestamp_granularities[]=segment" > "$OUT/transcript.json"

python3 - "$OUT" <<'PY'
import json,sys,os
o=sys.argv[1]
try:
    d=json.load(open(f"{o}/transcript.json"))
    segs=d.get("segments",[])
    with open(f"{o}/transcript.txt","w") as f:
        for s in segs:
            f.write(f"[{s['start']:06.2f}-{s['end']:06.2f}] {s['text'].strip()}\n")
    # densidade de fala: palavras por minuto
    txt=" ".join(s["text"] for s in segs); n=len(txt.split())
    dur=segs[-1]["end"] if segs else 0
    open(f"{o}/fala.txt","w").write(f"palavras={n} dur_fala={dur:.1f}s ppm={(n/dur*60 if dur else 0):.0f}\n")
except Exception as e:
    open(f"{o}/transcript.txt","w").write(f"ERRO transcricao: {e}\n")
PY

# --- 3. Frames: hook denso (0-4s) + resto a cada 4s ---
for t in 0 0.6 1.2 1.8 2.4 3.0 4.0; do
  ffmpeg -v error -y -ss "$t" -i "$V" -frames:v 1 -vf "scale=360:-1" "$OUT/frames/hook_$(printf '%04.1f' $t).jpg" 2>/dev/null
done
ffmpeg -v error -y -ss 5 -i "$V" -vf "fps=1/4,scale=360:-1" -q:v 4 "$OUT/frames/t%03d.jpg"

NF=$(ls "$OUT/frames" | wc -l | tr -d ' ')
cat > "$OUT/meta.txt" <<EOF
id=$ID
duracao=${DUR}s
fps=$FPS
resolucao=$WH
n_cortes_detectados=$NCORTES
n_frames=$NF
EOF
rm -f "$OUT/audio.m4a"
echo "OK $ID dur=${DUR%.*}s cortes=$NCORTES frames=$NF"

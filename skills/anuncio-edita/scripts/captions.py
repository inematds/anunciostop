#!/usr/bin/env python3
"""Gera 'beats' de legenda a partir de um transcript word-level (Groq/Whisper).
Estilo retenção: 2-3 palavras por beat, sincronizadas à voz, com uma palavra-chave
destacada. Saída JSON: [{start, end, words:[{t,w,hi}], }].

Uso: captions.py --transcript corte-final.json [--max-words 3] [--out captions.json]
     [--keywords "glm,5.2,frontera,..."] [--mode beat|pages]
     [--stroke on|off] [--no-microspring]

Além do JSON compatível, gera <out>.runtime.js com CSS, fitText e a entrada
do contêiner. Chamar registerCaptionTimeline(root, gsap) depois de montar os cues.

El resaltado: si una palabra está en la lista de keywords (o es la más larga del beat),
se marca hi=true para pintarla en violeta en la composición.

MODO pages (algoritmo estilo TikTok-captions de Remotion, reimplementado):
  agrupa palabras en "páginas" estables (<=42 chars por defecto, corte en puntuación fuerte o
  hueco >0.6s) y cada palabra lleva su timestamp t -> la composición pinta la página
  fija y va iluminando la palabra activa (karaoke). Reglas de legibilidad: página
  >=0.7s en pantalla, <=42 chars. Menos parpadeo que el modo beat, lectura más humana.
"""
import html
import json, re, argparse, sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

POWER = ("glm","5.2","frontera","millón","millones","tokens","contexto","abiertos","abierto",
         "open","source","gratis","mit","descargar","servidor","modificarlo","modificar",
         "precio","cerrado","cerrados","abre","cierra","nvidia","reglas","potente","potencia",
         "china","claude","fable","locura","tuya","verdad","importa","lujo","prefieres")

def norm(w): return re.sub(r"[^a-záéíóúñü0-9.]", "", w.lower())

def runtime_js(stroke=True, microspring=True):
    """Runtime companheiro: estilos, fitText e entrada de contêiner por cue."""
    stroke_css = """
  paint-order: stroke fill;
  -webkit-text-stroke: 0.16em rgba(0,0,0,0.85);""" if stroke else ""
    spring_js = """
    if (gsap) {
      const timeline = gsap.timeline({paused: true});
      pages.forEach((page) => timeline.fromTo(page,
        {scale: 0.86, y: 12, opacity: 0},
        {scale: 1, y: 0, opacity: 1, duration: 0.16, ease: \"back.out(1.1)\"},
        Number(page.dataset.captionStart || 0)));
      window.__hfGsap = window.__hfGsap || [];
      window.__hfGsap.push(timeline);
      return timeline;
    }""" if microspring else ""
    return f'''/* Generado por captions.py; runtime determinista para beats y pages. */
(function () {{
  "use strict";
  const style = document.createElement("style");
  style.textContent = `[data-caption-page] {{
  transform-origin: 50% 50%;
  overflow-wrap: anywhere;
  word-break: break-word;{stroke_css}
}}`;
  document.head.appendChild(style);

  function fitText(element) {{
    const parent = element.parentElement || element;
    const maxWidth = parent.clientWidth * 0.9;
    let size = parseFloat(getComputedStyle(element).fontSize) || 64;
    const previousWhiteSpace = element.style.whiteSpace;
    element.style.whiteSpace = "nowrap";
    element.style.overflowWrap = "anywhere";
    while (size > 8 && element.scrollWidth > maxWidth) {{
      size -= 2;
      element.style.fontSize = `${{size}}px`;
    }}
    element.style.whiteSpace = previousWhiteSpace;
    return size;
  }}

  function registerCaptionTimeline(root, gsap) {{
    const pages = Array.from(root.querySelectorAll("[data-caption-page]"));
    pages.forEach(fitText); // antes de registrar el timeline{spring_js}
    return null;
  }}

  window.__reelCaptions = {{fitText, registerCaptionTimeline}};
}})();
'''

def write_outputs(items, out, stroke, microspring):
    json.dump(items, open(out,"w"), ensure_ascii=False, indent=2)
    path = Path(out)
    runtime = path.with_name(path.stem + ".runtime.js")
    runtime.write_text(runtime_js(stroke=stroke, microspring=microspring), encoding="utf-8")
    return runtime

def merge_short_pages(pages, minimum):
    """Funde páginas curtas com a vizinha; nunca inventa tempo de tela."""
    pages = list(pages)
    i = 0
    while len(pages) > 1 and i < len(pages):
        if pages[i]["end"] - pages[i]["start"] + 1e-9 >= minimum:
            i += 1
            continue
        if i + 1 < len(pages):
            pages[i]["words"].extend(pages[i + 1]["words"])
            pages[i]["end"] = pages[i + 1]["end"]
            del pages[i + 1]
        else:
            pages[i - 1]["words"].extend(pages[i]["words"])
            pages[i - 1]["end"] = pages[i]["end"]
            del pages[i]
            i -= 1
    return pages

def emit_html(items, pack_path, output):
    if yaml is None:
        raise RuntimeError("falta pyyaml")
    pack_path = Path(pack_path)
    text = pack_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not match:
        raise RuntimeError("pack sin frontmatter YAML")
    pack = yaml.safe_load(match.group(1)) or {}
    skin_rel = pack.get("caption_skin")
    bottom = (pack.get("layout") or {}).get("captions_bottom")
    if not skin_rel or bottom is None:
        raise RuntimeError("pack sin caption_skin o layout.captions_bottom")
    skin = (pack_path.parent / skin_rel).read_text(encoding="utf-8").rstrip()
    lines = [skin, f'<style>#captions {{ bottom: {float(bottom):g}px; }}</style>', "<!-- cues: pegar dentro de #captions -->"]
    for page_i, page in enumerate(items):
        words = []
        for word_i, word in enumerate(page["words"]):
            classes = "cap-w" + (" hi" if word.get("hi") else "")
            words.append(f'<span class="{classes}" id="c{page_i}w{word_i}">{html.escape(str(word["w"]))}</span>')
        lines.append(f'<div class="cap-beat" id="cap{page_i}" data-caption-page="{page_i}" '
                     f'data-caption-start="{page["start"]:.2f}"><span class="pill">{" ".join(words)}</span></div>')
    lines.extend(["<!-- tweens: pegar antes de los tweens de orbs, con `tl` ya creado -->", "<script>"])
    for page_i, page in enumerate(items):
        lines.append(f'tl.fromTo("#cap{page_i}",{{opacity:0,scale:0.9,y:14}},{{opacity:1,scale:1,y:0,duration:0.16,ease:"back.out(1.1)"}},{page["start"]:.2f});')
        lines.append(f'tl.to("#cap{page_i}",{{opacity:0,duration:0.12,ease:"power2.in"}},{page["end"]:.2f});')
        for word_i, word in enumerate(page["words"]):
            suffix = " hi" if word.get("hi") else ""
            if word_i:
                prev = page["words"][word_i - 1]
                prev_suffix = " hi" if prev.get("hi") else ""
                lines.append(f'tl.set("#c{page_i}w{word_i-1}",{{className:"cap-w is-spoken{prev_suffix}"}},{word["t"]:.2f});')
            lines.append(f'tl.set("#c{page_i}w{word_i}",{{className:"cap-w is-active{suffix}"}},{word["t"]:.2f});')
    lines.extend(["</script>", ""])
    Path(output).write_text("\n".join(lines), encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--transcript", required=True)
    ap.add_argument("--max-words", type=int, default=3)
    ap.add_argument("--out", default="captions.json")
    ap.add_argument("--keywords", default="")
    ap.add_argument("--windows", default="", help="solo beats dentro de estas ventanas (a cámara), ej '2.4-6.1,34-38'")
    ap.add_argument("--mode", default="beat", choices=["beat","pages"])
    ap.add_argument("--max-chars", type=int, default=42)
    ap.add_argument("--min-page", type=float, default=0.7)
    ap.add_argument("--stroke", choices=["on", "off"], default="on")
    ap.add_argument("--no-microspring", action="store_true")
    ap.add_argument("--allow-empty", action="store_true")
    ap.add_argument("--pack", help="Video Style Pack; requerido con --emit-html")
    ap.add_argument("--emit-html", nargs="?", const="", metavar="PATH", help="emite skin+cues+tweens (default <out>.html)")
    a = ap.parse_args()
    wins = []
    for seg in a.windows.split(","):
        seg = seg.strip()
        if "-" in seg:
            lo, hi = seg.split("-"); wins.append((float(lo), float(hi)))
    kw = set(POWER) | set(k.strip().lower() for k in a.keywords.split(",") if k.strip())

    words = [w for w in json.load(open(a.transcript)).get("words", []) if w.get("start") is not None]
    if not words and not a.allow_empty:
        print("ERRO: transcript sem words; use --allow-empty só se for intencional", file=sys.stderr)
        return 2
    if a.emit_html is not None and not a.pack:
        print("ERRO: --emit-html exige --pack", file=sys.stderr)
        return 2

    if a.mode == "pages":
        pages = []
        cur = []
        def flush(nxt_start=None):
            if not cur: return
            start = cur[0]["start"]
            end = cur[-1].get("end", cur[-1]["start"]+0.3)
            hi_idx = -1
            for j,w in enumerate(cur):
                if norm(w["word"]) in kw: hi_idx = j; break
            if hi_idx == -1:
                hi_idx = max(range(len(cur)), key=lambda j: len(norm(cur[j]["word"])))
            ws = [{"w": w["word"].strip(), "t": round(w["start"],2), "hi": (j==hi_idx),
                   **({"kind": "num"} if re.search(r"\d", w["word"]) or re.search(r"[$€%]", w["word"]) else {})}
                  for j,w in enumerate(cur)]
            mid = (start+end)/2
            if not wins or any(lo <= mid <= hi for lo,hi in wins):
                pages.append({"start": round(start,2), "end": round(end,2), "words": ws})
            cur.clear()
        for i,w in enumerate(words):
            token = w["word"].strip()
            chars = sum(len(x["word"].strip())+1 for x in cur) + len(token)
            gap = (w["start"] - cur[-1].get("end", cur[-1]["start"])) if cur else 0
            if cur and (chars > a.max_chars or gap > 0.6):
                flush(nxt_start=w["start"])
            cur.append(w)
            if re.search(r"[.?!]$", token):
                nxt = words[i+1]["start"] if i+1 < len(words) else None
                flush(nxt_start=nxt)
        flush()
        pages = merge_short_pages(pages, a.min_page)
        if any(page["end"] - page["start"] + 1e-9 < a.min_page for page in pages):
            print(f"ERRO: o transcript não contém {a.min_page}s reais pra formar uma página legível", file=sys.stderr)
            return 2
        runtime = write_outputs(pages, a.out, a.stroke == "on", not a.no_microspring)
        if a.emit_html is not None:
            html_out = a.emit_html or str(Path(a.out).with_suffix(".html"))
            try:
                emit_html(pages, a.pack, html_out)
            except (OSError, RuntimeError, yaml.YAMLError if yaml else ValueError) as exc:
                print(f"ERRO: não foi possível emitir HTML: {exc}", file=sys.stderr)
                return 2
            print(f"  HTML skin+cues+tweens -> {html_out}")
        print(f"{len(pages)} páginas -> {a.out}  (modo pages: karaokê por palavra, <= {a.max_chars} chars, >= {a.min_page}s)")
        print(f"  runtime CSS/JS -> {runtime}")
        for p in pages[:6]:
            print(f"  {p['start']:5.2f}-{p['end']:5.2f}  " + " ".join(("*"+x["w"]+"*" if x["hi"] else x["w"]) for x in p["words"]))
        print("  ...")
        return 0

    beats = []
    i = 0
    while i < len(words):
        chunk = words[i:i+a.max_words]
        # romper el beat si una palabra acaba en signo fuerte (. ? !)
        cut = len(chunk)
        for j,w in enumerate(chunk):
            if re.search(r"[.?!]$", w["word"].strip()):
                cut = j+1; break
        chunk = chunk[:cut]
        start = chunk[0]["start"]
        end = chunk[-1].get("end", chunk[-1]["start"]+0.3)
        # elegir keyword: primera que esté en kw, si no la más larga
        hi_idx = -1
        for j,w in enumerate(chunk):
            if norm(w["word"]) in kw: hi_idx = j; break
        if hi_idx == -1:
            hi_idx = max(range(len(chunk)), key=lambda j: len(norm(chunk[j]["word"])))
        ws = [{"w": w["word"].strip(), "hi": (j==hi_idx)} for j,w in enumerate(chunk)]
        mid = (start+end)/2
        if not wins or any(lo <= mid <= hi for lo,hi in wins):
            beats.append({"start": round(start,2), "end": round(end,2), "words": ws})
        i += cut

    runtime = write_outputs(beats, a.out, a.stroke == "on", not a.no_microspring)
    if a.emit_html is not None:
        print("ERRO: --emit-html exige --mode pages", file=sys.stderr)
        return 2
    print(f"{len(beats)} beats -> {a.out}")
    print(f"  runtime CSS/JS -> {runtime}")
    for b in beats[:6]:
        print(f"  {b['start']:5.2f}-{b['end']:5.2f}  " + " ".join(("*"+x["w"]+"*" if x["hi"] else x["w"]) for x in b["words"]))
    print("  ...")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

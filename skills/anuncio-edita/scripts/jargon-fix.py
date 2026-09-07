#!/usr/bin/env python3
"""Corrige o JARGÃO TÉCNICO que o Whisper transcreve errado (ex.: Claude->"Cloud")
num transcript word-level ou num captions.json, ANTES de gerar legendas.

Por quê: o incidente das legendas "Cloud Code" em produção. O Whisper (Groq e
WhisperX igualmente) erra o jargão do nicho; o timing é bom, o TEXTO não.
Regra: os timestamps NUNCA se tocam, só o texto.

Glossário: padrões abaixo + opcional scripts/jargon.json (faz merge, sobrescreve padrões).
Formato do json: {"padrão regex (case-insensitive)": "Substituição", ...}

Uso: jargon-fix.py --in edicao/transcript-final.json [--glossary extra.json] [--dry]
     Acepta: transcript Groq ({text, words:[{word,...}]}) y captions.json
     ([{words:[{w,...}]}]). Modifica IN PLACE (o --out otro.json). --dry = solo mostrar.
"""
import json, re, argparse, os, sys

DEFAULTS = {
    r"\bcloud\s+code\b": "Claude Code",
    r"\bclou?d[e]?\b": "Claude",          # cloud/clode/cloude sueltos
    r"\bclaudio\b": "Claude",
    r"\bantr[oó]pic\b": "Anthropic",
    # Añade aquí los nombres propios de tu nicho que Whisper transcribe mal.
    r"\bhiper\s*frames?\b": "Hyperframes",
    r"\bhyper\s+frames?\b": "Hyperframes",
    r"\bgroc\b": "Groq",
    r"\bgit\s+hub\b": "GitHub",
    r"\bfable\s+five\b": "Fable 5",
    r"\bopen\s+ai\b": "OpenAI",
    r"\bchat\s*gtp\b": "ChatGPT",
}

def fix_text(t, rules, hits):
    for pat, rep in rules.items():
        def _sub(m):
            hits.append((m.group(0), rep))
            return rep
        t = re.sub(pat, _sub, t, flags=re.IGNORECASE)
    return t

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out", default=None)
    ap.add_argument("--glossary", default=None)
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()

    rules = dict(DEFAULTS)
    local = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jargon.json")
    for src in [local, a.glossary]:
        if src and os.path.exists(src):
            rules.update(json.load(open(src)))

    data = json.load(open(a.inp))
    hits = []
    if isinstance(data, dict):                      # transcript Groq
        if "text" in data:
            data["text"] = fix_text(data["text"], rules, hits)
        for w in (data.get("words") or []):
            if "word" in w: w["word"] = fix_text(w["word"], rules, hits)
        for s in (data.get("segments") or []):
            if "text" in s: s["text"] = fix_text(s["text"], rules, hits)
    elif isinstance(data, list):                    # captions.json
        for beat in data:
            for w in beat.get("words", []):
                if "w" in w: w["w"] = fix_text(w["w"], rules, hits)

    uniq = {}
    for orig, rep in hits: uniq[(orig.lower(), rep)] = uniq.get((orig.lower(), rep), 0) + 1
    if not uniq:
        print("jargon-fix: 0 correções: transcript limpo de jargão conhecido.")
    else:
        print(f"jargon-fix: {sum(uniq.values())} correções:")
        for (orig, rep), n in sorted(uniq.items(), key=lambda x: -x[1]):
            print(f"  '{orig}' -> '{rep}'  x{n}")
        print("REVISE a lista: se alguma é falso positivo, acrescente exceção ou corrija à mão.")
    if a.dry:
        print("(--dry: nada foi escrito)"); return 0
    out = a.out or a.inp
    json.dump(data, open(out, "w"), ensure_ascii=False, indent=2)
    print(f"-> {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

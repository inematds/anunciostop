#!/usr/bin/env python3
"""Checagem mecânica de um prompt de vídeo antes de gastar crédito.

Não julga criatividade: só pega o que um script consegue pegar e que já custou gerações:
colchetes sem preencher, prompt maior que a caixa, planos sem Dialogue, timestamps com buraco,
sotaque não declarado, palavras de grading que devolvem preto e branco.

Uso:
  checa-prompt.py prompt.txt --interface seedance25 [--duracao 30]
  checa-prompt.py prompt.txt --interface dreamina   [--duracao 30]
  checa-prompt.py prompt.txt --interface agnes
Sai com código 1 se houver bloqueante.
"""
from __future__ import annotations
import argparse, re, sys

GRADING_RUIM = ["desaturated", "monochrome", "monochromatic", "chiaroscuro", "crushed blacks",
                "dessaturado", "monocromático", "claro-escuro"]
SOTAQUE_OK = re.compile(r"brazilian portuguese|portugu[eê]s do brasil", re.I)
SOTAQUE_RUIM = re.compile(r"castilian|spain|european portuguese|neutral accent", re.I)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("arquivo")
    ap.add_argument("--interface", choices=["seedance25", "dreamina", "seedance20", "agnes"], required=True)
    ap.add_argument("--duracao", type=float, default=None, help="duração pedida em segundos")
    a = ap.parse_args()
    txt = open(a.arquivo, encoding="utf-8").read()
    bloq: list[str] = []
    aviso: list[str] = []

    # 1. colchetes de modelo sem preencher (ignora binding @Image e blocos [FORMAT] etc. em caixa alta)
    for m in re.finditer(r"\[([^\]\n]{1,60})\]", txt):
        inner = m.group(1)
        if inner.isupper() and " " not in inner.strip("_ ") and len(inner) < 4:
            continue
        if re.match(r"^(FORMAT|REFERENCE|GLOBAL|IDENTITY|AUDIO|STRICT|Visual|Character|Voice|Scene|Dialogue|Replace|Keep|Add|Negative|MOTION|CAMERA|CONTINUITY|NEGATIVE|Audio ?\d)", inner):
            continue
        if re.match(r"^\d{2}:\d{2}-\d{2}:\d{2}$", inner):
            continue
        if re.search(r"[<>]|\b(NOME|NAME|HEIGHT|BUILD|WARDROBE|IDENTITY|BURACO|HUECO|X|TODO)\b", inner) or inner.isupper():
            bloq.append(f"colchete sem preencher: [{inner}]")

    # 2. tamanho da caixa
    nbytes = len(txt.encode("utf-8"))
    if a.interface == "dreamina" and nbytes > 3990:
        bloq.append(f"prompt com {nbytes} bytes; a Dreamina rejeita acima de ~4000")
    if a.interface == "seedance25" and nbytes > 6000:
        aviso.append(f"prompt com {nbytes} bytes; conferir a caixa real da superfície")

    # 3. timestamps contíguos (seedance25)
    if a.interface == "seedance25":
        ts = [(int(h1) * 60 + int(s1), int(h2) * 60 + int(s2)) for h1, s1, h2, s2 in
              re.findall(r"\[(\d{2}):(\d{2})-(\d{2}):(\d{2})\]", txt)]
        for (s0, e0), (s1, e1) in zip(ts, ts[1:]):
            if e0 != s1:
                bloq.append(f"timestamps não contíguos: termina em {e0}s e o seguinte começa em {s1}s")
        if ts and a.duracao and ts[-1][1] != int(a.duracao):
            aviso.append(f"último plano termina em {ts[-1][1]}s, duração pedida {a.duracao:g}s")
        # planos sem Dialogue
        planos = re.split(r"\n(?=\[\d{2}:\d{2}-\d{2}:\d{2}\])", txt)
        for p in planos[1:] if len(planos) > 1 else []:
            cab = p.splitlines()[0][:22]
            if "Dialogue" not in p and not re.search(r"silent|mute|no dialogue|nobody speaks", p, re.I):
                aviso.append(f"plano {cab} sem Dialogue nem 'silent by design': vai sair mudo")
        if "off-camera" in txt and "moves their lips" not in txt:
            aviso.append("há trecho off-camera sem 'nobody on screen moves their lips'")

    # 4. dreamina: um único P1 e primeiro trecho ≤ 2 s
    if a.interface == "dreamina":
        n_p = len(re.findall(r"^P\d+:", txt, re.M))
        if n_p != 1:
            bloq.append(f"Dreamina exige um único P1: com todo o diálogo (encontrados {n_p})")
        m = re.search(r"^(\d+)-(\d+)s", txt, re.M)
        if m and int(m.group(2)) > 2:
            aviso.append(f"primeiro trecho termina em {m.group(2)}s; deve ser ≤ 2 s")
        if "ONE SHOT ONLY" not in txt:
            aviso.append("falta a linha ONE SHOT ONLY")

    # 5. agnes: sem lábios, uma ação
    if a.interface == "agnes":
        if re.search(r"\bDialogue\b|speaks|says ['\"]", txt):
            bloq.append("Agnes não gera fala: remover Dialogue e passar a voz pro inemavox (via D)")
        if not re.search(r"no lip|nobody speaks|lips", txt, re.I):
            aviso.append("acrescentar 'no lip movement, nobody speaks' nos negativos")
        if len(re.findall(r"\bwhile\b|\band then\b|\bthen\b", txt, re.I)) > 2:
            aviso.append("mais de uma ação encadeada no clipe: risco de morphing; uma ação por clipe")

    # 6. sotaque
    if a.interface != "agnes":
        if SOTAQUE_RUIM.search(txt):
            bloq.append("sotaque de outra variante declarado (castelhano/europeu/neutro); deve ser português do Brasil")
        if not SOTAQUE_OK.search(txt):
            aviso.append("português do Brasil não declarado na última linha do prompt")

    # 7. grading que devolve preto e branco
    for g in GRADING_RUIM:
        if re.search(rf"\b{re.escape(g)}\b", txt, re.I):
            aviso.append(f"palavra de grading arriscada: '{g}' (nomear cores em positivo)")

    # saída
    print(f"interface={a.interface} bytes={nbytes}")
    for b in bloq:
        print(f"BLOQUEANTE  {b}")
    for w in aviso:
        print(f"aviso       {w}")
    if not bloq and not aviso:
        print("OK: nada mecânico a corrigir. O julgamento de conteúdo continua sendo seu.")
    return 1 if bloq else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Exporta as páginas de legenda como SRT sidecar em texto puro."""

from __future__ import annotations

import argparse
import json
import os
import sys


def timestamp(seconds: float) -> str:
    millis = max(0, round(seconds * 1000))
    hours, millis = divmod(millis, 3_600_000)
    minutes, millis = divmod(millis, 60_000)
    secs, millis = divmod(millis, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def page_text(page: dict) -> str:
    words = page.get("words", [])
    return " ".join(str(word.get("w", word.get("word", ""))).strip() for word in words).strip()


def export(captions: list[dict], offset: float) -> str:
    blocks = []
    for index, page in enumerate(captions, 1):
        start = float(page["start"]) + offset
        end = float(page["end"]) + offset
        if end <= start:
            raise ValueError(f"página {index}: end debe ser mayor que start")
        text = page_text(page)
        if not text:
            raise ValueError(f"página {index}: no contiene palabras")
        blocks.append(f"{index}\n{timestamp(start)} --> {timestamp(end)}\n{text}")
    return "\n\n".join(blocks) + ("\n" if blocks else "")


def main() -> int:
    parser = argparse.ArgumentParser(description="Convierte captions.json a SRT estándar.")
    parser.add_argument("--captions", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--offset", type=float, default=0.0)
    args = parser.parse_args()
    try:
        with open(args.captions, encoding="utf-8") as handle:
            captions = json.load(handle)
        if not isinstance(captions, list):
            raise ValueError("captions debe ser una lista de páginas")
        content = export(captions, args.offset)
        parent = os.path.dirname(os.path.abspath(args.out))
        os.makedirs(parent, exist_ok=True)
        with open(args.out, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
        print(f"export-srt: {exc}", file=sys.stderr)
        return 2
    print(f"export-srt: {len(captions)} entradas → {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

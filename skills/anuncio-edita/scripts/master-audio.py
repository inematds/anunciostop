#!/usr/bin/env python3
"""Normaliza o áudio de um vídeo com loudnorm EBU R128 em duas passadas."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Optional, Tuple


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def parse_loudnorm(stderr: str) -> Optional[Dict[str, Any]]:
    for match in reversed(list(re.finditer(r"\{[\s\S]*?\}", stderr))):
        try:
            data = json.loads(match.group(0))
        except json.JSONDecodeError:
            continue
        if "input_i" in data and "input_tp" in data:
            return data
    return None


def measure(path: Path, target_i: float, target_tp: float, target_lra: float) -> Tuple[Optional[Dict[str, Any]], str]:
    filt = f"loudnorm=I={target_i}:TP={target_tp}:LRA={target_lra}:print_format=json"
    proc = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-map", "0:a:0", "-af", filt, "-f", "null", "-"])
    return parse_loudnorm(proc.stderr), proc.stderr


def number(data: Dict[str, Any], key: str) -> str:
    value = data.get(key)
    if value is None or str(value).lower() in {"inf", "-inf", "nan"}:
        raise ValueError(f"medición inválida: {key}={value}")
    float(value)
    return str(value)


def main() -> int:
    ap = argparse.ArgumentParser(description="Mastering social a loudness objetivo mediante loudnorm 2-pass.")
    ap.add_argument("--in", dest="input", required=True)
    ap.add_argument("--out")
    ap.add_argument("--i", type=float, default=-14.0)
    ap.add_argument("--tp", type=float, default=-1.0)
    ap.add_argument("--lra", type=float, default=11.0)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    source = Path(args.input)
    output = Path(args.out) if args.out else source.with_name(f"{source.stem}-mastered.mp4")
    report: Dict[str, Any] = {"input": str(source), "output": str(output), "target_i": args.i}
    if not source.is_file():
        print(f"ERRO: o arquivo não existe: {source}", file=sys.stderr)
        return 1

    measured, diagnostic = measure(source, args.i, args.tp, args.lra)
    fallback = False
    base = f"loudnorm=I={args.i}:TP={args.tp}:LRA={args.lra}"
    try:
        if measured is None:
            raise ValueError("ffmpeg no devolvió JSON de loudnorm")
        filt = (
            f"{base}:measured_I={number(measured, 'input_i')}:"
            f"measured_TP={number(measured, 'input_tp')}:"
            f"measured_LRA={number(measured, 'input_lra')}:"
            f"measured_thresh={number(measured, 'input_thresh')}:"
            f"offset={number(measured, 'target_offset')}:linear=true"
        )
    except ValueError as exc:
        fallback = True
        filt = base
        print(f"AVISO: medição em 2 passadas falhou ({exc}); aplicando loudnorm em uma passada.", file=sys.stderr)

    proc = subprocess.run([
        "ffmpeg", "-hide_banner", "-y", "-i", str(source), "-map", "0:v:0", "-map", "0:a:0",
        "-af", filt, "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", str(output),
    ])
    if proc.returncode != 0:
        if measured is None and diagnostic:
            print(diagnostic[-1000:], file=sys.stderr)
        print("ERRO: o ffmpeg não conseguiu gerar o master.", file=sys.stderr)
        return 1

    verified, _ = measure(output, args.i, args.tp, args.lra)
    input_i = float(measured["input_i"]) if measured and str(measured.get("input_i", "")).lower() not in {"-inf", "inf"} else None
    output_i = float(verified["input_i"]) if verified and str(verified.get("input_i", "")).lower() not in {"-inf", "inf"} else None
    report.update({"input_i": input_i, "output_i": output_i, "fallback": fallback})
    report["within_tolerance"] = output_i is not None and abs(output_i - args.i) <= 0.5
    if not report["within_tolerance"]:
        print("ERRO: o master não fica dentro de ±0.5 LU do alvo.", file=sys.stderr)
    if args.json:
        print(json.dumps(report, ensure_ascii=False))
    else:
        before = f"{input_i:.2f}" if input_i is not None else "N/D"
        after = f"{output_i:.2f}" if output_i is not None else "N/D"
        print(f"LUFS {before} → {after} (alvo {args.i:g})")
        print(f"{'OK' if report['within_tolerance'] else 'FALHA'} -> {output}")
    return 0 if report["within_tolerance"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

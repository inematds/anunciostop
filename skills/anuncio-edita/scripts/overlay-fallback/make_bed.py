#!/usr/bin/env python3
"""Sintetiza uma cama ambiente sutil (pad quente dark-tech) de N segundos, sem downloads.
Dois acordes que alternam (Am7 <-> Fmaj7) com swells lentos + ar filtrado. Volume muito baixo;
o music-duck abaixa ainda mais sob a voz."""
import subprocess, sys, math
DUR=float(sys.argv[1]) if len(sys.argv)>1 else 200.0
OUT=sys.argv[2] if len(sys.argv)>2 else 'edicao/bed.wav'

# notas (Hz) de dois acordes quentes
chordA=[110.00, 164.81, 220.00, 329.63]   # A minor add (A3 E3 A3 E4)-ish
chordB=[ 87.31, 130.81, 174.61, 261.63]   # F maj (F2 C3 F3 C4)
PERIOD=16.0  # s por ciclo de cross-fade A->B->A

# construímos aevalsrc: soma de senos por acorde, com envelope de cross-fade
def chord_expr(freqs, phase):
    # gain oscila 0..1 con coseno desfasado (phase 0 => acorde A fuerte)
    env=f"(0.5+0.5*cos(2*PI*t/{PERIOD}+{phase}))"
    sines="+".join(f"sin(2*PI*{f}*t)" for f in freqs)
    return f"{env}*({sines})/{len(freqs)}"

expr=f"0.16*(({chord_expr(chordA,0)})+({chord_expr(chordB,math.pi)}))"
# ar: ruído rosa muito filtrado e baixo se acrescenta depois por filtro
cmd=[
 'ffmpeg','-y',
 '-f','lavfi','-i',f"aevalsrc='{expr}':s=48000:d={DUR}:c=stereo",
 '-f','lavfi','-i',f"anoisesrc=d={DUR}:c=pink:a=0.05",
 '-filter_complex',
   "[0:a]lowpass=f=900,highpass=f=60,aformat=channel_layouts=stereo[pad];"
   "[1:a]highpass=f=2500,lowpass=f=9000,volume=0.08,aformat=channel_layouts=stereo[air];"
   "[pad][air]amix=inputs=2:normalize=0,"
   f"afade=t=in:st=0:d=2.5,afade=t=out:st={DUR-3}:d=3,"
   "aresample=48000,alimiter=limit=0.9[m]",
 '-map','[m]','-ar','48000','-ac','2',OUT,'-loglevel','error'
]
r=subprocess.run(cmd)
print('OK bed ->',OUT if r.returncode==0 else 'FALHOU', 'dur',DUR)
sys.exit(r.returncode)

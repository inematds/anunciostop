#!/usr/bin/env python3
"""Constrói e executa o overlay do ffmpeg a partir de overlays.json.
Uso: compose.py <base.mp4> <saida.mp4> [--fast]"""
import json, sys, subprocess

base=sys.argv[1]; out=sys.argv[2]
fast='--fast' in sys.argv
ov=json.load(open('edicao/overlays.json'))
ov.sort(key=lambda o:(o['layer'],o['start']))

inp=['-i',base]
for o in ov: inp+=['-loop','1','-i',o['png']]

parts=[]; cur='[0:v]'
for i,o in enumerate(ov,1):
    lbl=f'[t{i}]'
    fade=o.get('fade',0)
    src=f'[{i}:v]'
    if fade>0:
        s,e=o['start'],o['end']
        parts.append(f"[{i}:v]format=rgba,fade=t=in:st={s}:d={fade}:alpha=1,"
                     f"fade=t=out:st={e-fade}:d={fade}:alpha=1[f{i}]")
        src=f'[f{i}]'
    parts.append(f"{cur}{src}overlay=x={o['x']}:y={o['y']}:"
                 f"enable='between(t,{o['start']},{o['end']})'{lbl}")
    cur=lbl
fc=';'.join(parts)

if fast:
    vargs=['-c:v','libx264','-preset','ultrafast','-crf','28']
else:
    vargs=['-c:v','libx264','-preset','medium','-crf','17','-pix_fmt','yuv420p']

cmd=['ffmpeg','-y',*inp,'-filter_complex',fc,'-map',cur,'-map','0:a',
     *vargs,'-c:a','copy',out]
print('inputs:',len(ov),'| filter len:',len(fc))
r=subprocess.run(cmd)
sys.exit(r.returncode)

#!/usr/bin/env python3
"""Assa overlays.json numa ÚNICA pista transparente (qtrle mov). Frames por intervalos
(união de breakpoints + subpassos nos fades) -> concat demuxer -> um só overlay depois.
Uso: build_track.py <dur> <saida.mov>"""
import json, os, subprocess, sys
from PIL import Image

W,H=1080,1920
DUR=float(sys.argv[1]) if len(sys.argv)>1 else 199.5
OUT=sys.argv[2] if len(sys.argv)>2 else 'edicao/track.mov'
FR='edicao/track_frames'
os.makedirs(FR,exist_ok=True)
for f in os.listdir(FR):
    if f.endswith('.png'): os.remove(os.path.join(FR,f))

ov=json.load(open('edicao/overlays.json'))
for o in ov: o['_img']=Image.open(o['png']).convert('RGBA')

# breakpoints
bp=set([0.0,DUR])
for o in ov:
    s,e,f=o['start'],o['end'],o.get('fade',0)
    bp.add(s); bp.add(e)
    if f>0:
        t=s
        while t<s+f: bp.add(round(t,3)); t+=0.08
        bp.add(s+f)
        t=e-f
        while t<e: bp.add(round(t,3)); t+=0.08
bp=sorted(x for x in bp if 0<=x<=DUR)

def alpha_at(o,t):
    s,e,f=o['start'],o['end'],o.get('fade',0)
    if not(s<=t<e): return 0.0
    if f<=0: return 1.0
    if t<s+f: return max(0,min(1,(t-s)/f))
    if t>e-f: return max(0,min(1,(e-t)/f))
    return 1.0

frames=[]
for i in range(len(bp)-1):
    t0,t1=bp[i],bp[i+1]
    dur=t1-t0
    if dur<=0.001: continue
    mid=(t0+t1)/2
    active=[(o,alpha_at(o,mid)) for o in ov]
    active=[(o,a) for o,a in active if a>0.001]
    canvas=Image.new('RGBA',(W,H),(0,0,0,0))
    for o,a in sorted(active,key=lambda z:z[0]['layer']):
        im=o['_img']
        if a<0.999:
            im=im.copy(); al=im.getchannel('A').point(lambda p:int(p*a)); im.putalpha(al)
        canvas.alpha_composite(im,(o['x'],o['y']))
    p=f"{FR}/f{i:04d}.png"; canvas.save(p)
    frames.append((os.path.basename(p),dur))

# concat list
with open(f'{FR}/list.txt','w') as fh:
    for name,dur in frames:
        fh.write(f"file '{name}'\nduration {dur:.3f}\n")
    fh.write(f"file '{frames[-1][0]}'\n")  # último repetido (quirk concat)

print(f"{len(frames)} frames de pista; codificando qtrle...")
r=subprocess.run(['ffmpeg','-y','-f','concat','-safe','0','-i',f'{FR}/list.txt',
   '-vf','format=rgba,fps=30','-c:v','qtrle',OUT,'-loglevel','error'])
print('OK track ->',OUT if r.returncode==0 else 'FALHOU')
sys.exit(r.returncode)

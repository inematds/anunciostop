#!/usr/bin/env python3
"""Overlays de texto -> PNG transparentes (Pillow). Estilo de legendas:
pastilha escura translúcida + karaokê (palavra não
dita atenuada, ativa a 100%, palavra-chave na cor da marca SEMPRE). Canvas 1080x1920.
Saída: overlays.json (heroes + estados de legenda palavra a palavra)."""
import json, os
from PIL import Image, ImageDraw, ImageFont

W,H=1080,1920
import os, glob as _glob
# Fonte: variável CAPTION_FONT (arquivo .ttf/.otf/.ttc) ou a primeira que existir na lista abaixo.
_CANDIDATAS = [
    os.environ.get('CAPTION_FONT',''),
    '/usr/share/fonts/truetype/inter/Inter-Bold.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
    '/System/Library/Fonts/HelveticaNeue.ttc',
    'C:/Windows/Fonts/arialbd.ttf',
]
TTC = next((f for f in _CANDIDATAS if f and os.path.exists(f)), None)
if TTC is None:
    raise SystemExit('Nenhuma fonte encontrada. Defina CAPTION_FONT=/caminho/fonte.ttf')
_IDX = {'bold':1,'black':9,'med':10} if TTC.endswith('.ttc') else {'bold':0,'black':0,'med':0}
BOLD=lambda s: ImageFont.truetype(TTC,s,index=_IDX['bold'])
BLACK=lambda s: ImageFont.truetype(TTC,s,index=_IDX['black'])
MED=lambda s: ImageFont.truetype(TTC,s,index=_IDX['med'])
# Cor da palavra-chave: vem da ficha de marca (variável KEYWORD_COLOR), padrão violeta.
KEYWORD_COLOR = os.environ.get('KEYWORD_COLOR', '#8B6CFF')

def _hex_rgba(h, a=255):
    h=h.strip().lstrip('#')
    if len(h)==3: h=''.join(c*2 for c in h)
    return (int(h[0:2],16),int(h[2:4],16),int(h[4:6],16),a)
VIOLET=_hex_rgba(KEYWORD_COLOR)                     # cor da palavra-chave (da ficha de marca)
VIOLET_LIGHT=tuple(min(255,c+70) for c in VIOLET[:3])+(255,)   # contorno claro derivado
WHITE=(255,255,255,255)
# legenda pill (rgba(10,7,18,.80), borda branca .10, radius 18, pad 16x32)
CAP_CANVAS=(10,7,18,204)
CAP_BORDER=(255,255,255,26)
CAP_SIZE=48
CAP_Y=812          # centro vertical del bloque (nivel micro, encima de costura ~920)

os.makedirs('edicao/ov',exist_ok=True)
CAP=json.load(open('edicao/captions.json'))
MARKS=json.load(open('edicao/marks.json'))
CHIP_T=MARKS['chip']; END_T=MARKS['handle']
overlays=[]

def fix_words(words):
    out=[]; skip=False
    for i,x in enumerate(words):
        if skip: skip=False; continue
        raw=x['w']; hi=bool(x.get('hi')); t=x.get('t',0)
        low=raw.lower().strip('.,¿?¡!')
        nxt=words[i+1]['w'].lower().strip('.,¿?¡!') if i+1<len(words) else ''
        if low=='gohealth':
            raw='GoHighLevel'+(',' if words[i+1]['w'].endswith(',') else ''); skip=True
        elif low=='inteligente' and nxt.startswith('artificial'):
            raw='inteligencia'
        out.append({'w':raw,'hi':hi,'t':t})
    return out

# ---------- LEGENDAS (pill + karaokê por palavra) ----------
font=BOLD(CAP_SIZE); asc,desc=font.getmetrics(); LH=asc+desc
SP=font.getlength(' '); GAP=int(CAP_SIZE*0.20); PADX,PADY=32,16; STROKE=3
MAXW=900

def layout(words):
    """wrap -> lines: cada linha é lista de dicts com x local. Devolve (lines, cw, ch)."""
    lines=[]; cur=[]; cw=0
    for wd in words:
        ww=font.getlength(wd['w']); add=ww+(SP if cur else 0)
        if cur and cw+add>MAXW: lines.append(cur); cur=[]; cw=0; add=ww
        wd=dict(wd); wd['ww']=ww; cur.append(wd); cw+=add
    if cur: lines.append(cur)
    widths=[sum(x['ww'] for x in ln)+SP*(len(ln)-1) for ln in lines]
    return lines,max(widths),widths

def render_state(lines, lw_each, cw, active_idx, key):
    ch=len(lines)*LH+(len(lines)-1)*GAP
    cvw,cvh=int(cw+PADX*2),int(ch+PADY*2)
    img=Image.new('RGBA',(cvw,cvh),(0,0,0,0)); d=ImageDraw.Draw(img)
    d.rounded_rectangle([0,0,cvw-1,cvh-1],radius=18,fill=CAP_CANVAS,outline=CAP_BORDER,width=2)
    idx=0; y=PADY
    for li,ln in enumerate(lines):
        x=(cvw-lw_each[li])/2
        for wd in ln:
            if wd['hi']:
                col=VIOLET
            else:
                if idx<active_idx: op=217        # ya dicha
                elif idx==active_idx: op=255     # activa
                else: op=97                       # por decir
                col=(255,255,255,op)
            d.text((x,y),wd['w'],font=font,fill=col,stroke_width=STROKE,
                   stroke_fill=(0,0,0,min(col[3],217)))
            x+=wd['ww']+SP; idx+=1
        y+=LH+GAP
    p=f'edicao/ov/{key}.png'; img.save(p)
    return p,cvw,cvh

for pi,page in enumerate(CAP):
    words=fix_words(page['words'])
    if not words: continue
    lines,cw,lw_each=layout(words)
    n=len(words)
    x0=int(W/2-(cw+PADX*2)/2); h=len(lines)*LH+(len(lines)-1)*GAP+PADY*2
    y0=int(CAP_Y-h/2)
    # estados: uno por palabra (karaoke). start = t de la palabra; end = t de la siguiente / page.end
    for j,wd in enumerate(words):
        st=max(page['start'], wd['t'])
        en=words[j+1]['t'] if j+1<n else page['end']
        if en<=st: en=st+0.05
        p,_,_=render_state(lines,lw_each,cw,j,f'cap_{pi:03d}_{j:02d}')
        overlays.append({'png':p,'start':round(st,3),'end':round(en,3),'x':x0,'y':y0,'fade':0,'layer':1})

# ---------- HOOK cold-open ----------
def render_words_simple(words,font,size,cx,cy,maxw,sp,stroke,name,hi=VIOLET,base=WHITE):
    lines=[];cur=[];cw=0
    for txt,h in words:
        ww=font.getlength(txt); add=ww+(sp if cur else 0)
        if cur and cw+add>maxw: lines.append(cur);cur=[];cw=0;add=ww
        cur.append((txt,h,ww));cw+=add
    if cur: lines.append(cur)
    a,d_=font.getmetrics(); lh=a+d_; gap=int(size*0.14)
    lws=[sum(w for _,_,w in ln)+sp*(len(ln)-1) for ln in lines]; cwid=max(lws)
    pad=stroke*2+int(size*0.5); cvw,cvh=int(cwid+pad*2),int(len(lines)*lh+(len(lines)-1)*gap+pad*2)
    img=Image.new('RGBA',(cvw,cvh),(0,0,0,0)); dr=ImageDraw.Draw(img); y=pad
    for li,ln in enumerate(lines):
        x=(cvw-lws[li])/2
        for txt,h,ww in ln:
            dr.text((x+int(size*0.05),y+int(size*0.06)),txt,font=font,fill=(0,0,0,150),stroke_width=stroke,stroke_fill=(0,0,0,150))
            dr.text((x,y),txt,font=font,fill=(hi if h else base),stroke_width=stroke,stroke_fill=(0,0,0,235))
            x+=ww+sp
        y+=lh+gap
    p=f'edicao/ov/{name}.png'; img.save(p); return p,cvw,cvh

p,w,h=render_words_simple([('MIS',0),('REELS',0),('SE',0),('EDITAN',0),('SOLOS',1)],BLACK(76),76,W/2,150,1010,15,4,'hook')
overlays.append({'png':p,'start':0.0,'end':2.35,'x':int(W/2-w/2),'y':84,'fade':0.30,'layer':5})

# ---------- CHIP LOOP (pastilha sólida na cor da marca, MAIS ABAIXO, fora da cara) ----------
def render_chip():
    f1=MED(42); f2=BLACK(50); t1='comenta '; t2='BUCLE'
    w1=f1.getlength(t1); w2=f2.getlength(t2); padx,pady=44,26; gap=6; m=14
    a1,d1=f1.getmetrics(); a2,d2=f2.getmetrics(); th=max(a1+d1,a2+d2)
    cvw,cvh=int(w1+w2+gap+padx*2+m*2),int(th+pady*2+m*2)
    img=Image.new('RGBA',(cvw,cvh),(0,0,0,0)); d=ImageDraw.Draw(img)
    d.rounded_rectangle([m+4,m+7,cvw-1-m+4,cvh-1-m+7],radius=(cvh-2*m)//2,fill=(0,0,0,120))
    d.rounded_rectangle([m,m,cvw-1-m,cvh-1-m],radius=(cvh-2*m)//2,fill=VIOLET,outline=VIOLET_LIGHT,width=3)
    x=m+padx; y0=m+pady
    d.text((x,y0),t1,font=f1,fill=(255,255,255,235)); x+=w1+gap
    d.text((x,y0-4),t2,font=f2,fill=(255,255,255,255))
    p='edicao/ov/chip.png'; img.save(p); return p,cvw,cvh
p,w,h=render_chip()
overlays.append({'png':p,'start':CHIP_T,'end':CHIP_T+4.2,'x':int(W/2-w/2),'y':640,'fade':0.22,'layer':4})

# ---------- ENDCARD handle (pastilha de marca, diferente das legendas) ----------
def render_handle():
    f1=BOLD(52); at='@'; nm=os.environ.get('BRAND_HANDLE','tu_marca')  # handle de la marca
    wa=f1.getlength(at); wn=f1.getlength(nm); padx,pady=40,22; m=12
    a,d_=f1.getmetrics(); th=a+d_
    cvw,cvh=int(wa+wn+padx*2+m*2),int(th+pady*2+m*2)
    img=Image.new('RGBA',(cvw,cvh),(0,0,0,0)); dr=ImageDraw.Draw(img)
    dr.rounded_rectangle([m+3,m+5,cvw-1-m+3,cvh-1-m+5],radius=(cvh-2*m)//2,fill=(0,0,0,120))
    dr.rounded_rectangle([m,m,cvw-1-m,cvh-1-m],radius=(cvh-2*m)//2,fill=(12,8,20,230),outline=VIOLET,width=3)
    x=m+padx; y0=m+pady
    dr.text((x,y0),at,font=f1,fill=VIOLET); x+=wa
    dr.text((x,y0),nm,font=f1,fill=WHITE)
    p='edicao/ov/handle.png'; img.save(p); return p,cvw,cvh
p,w,h=render_handle()
overlays.append({'png':p,'start':END_T,'end':END_T+3.4,'x':int(W/2-w/2),'y':1180,'fade':0.25,'layer':4})

json.dump(overlays,open('edicao/overlays.json','w'),indent=1)
ncap=sum(1 for o in overlays if o['layer']==1)
print(f'OK: {len(overlays)} overlays ({ncap} estados de legenda karaokê + hook + chip + endcard)')

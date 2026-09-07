#!/usr/bin/env python3
"""Recalcula a partir do transcript do corte: marks.json (chip 'loop', endcard CTA) e
sfx_events.json (transições de seção). Robusto aos deslocamentos do recorte."""
import json
w=json.load(open('edicao/transcript-final.json'))['words']
toks=[x['word'].lower().strip('.,¿?¡!¡') for x in w]

def find(seq, after=0.0):
    ss=[s.lower() for s in seq.split()]; n=len(ss)
    for i in range(len(toks)-n+1):
        if toks[i:i+n]==ss and w[i]['start']>=after:
            return w[i]['start']
    return None

def find1(word, after=0.0, occ=1):
    c=0
    for i,t in enumerate(toks):
        if t==word.lower() and w[i]['start']>=after:
            c+=1
            if c==occ: return w[i]['start']
    return None

chip = find1('bucle') or 173.0                    # 1ª vez que dice 'bucle' (CTA)
handle = find('si te mola') or find1('like') or None
if handle is None: handle = w[-1]['end']-3.0
marks={'chip':round(chip,2),'handle':round(max(0,handle-0.3),2)}
json.dump(marks,open('edicao/marks.json','w'),indent=1)

# SFX: transições de seção + reveal + payoff
ev=[['whoosh',0.05]]
for ph in ['primera skill','paso 2','tercer paso','cuarto paso','siguiente','último tengo']:
    t=find(ph)
    if t: ev.append(['whoosh',round(t-0.05,2)])
tp=find('aquí viene lo')
if tp: ev+= [['riser',round(tp-0.65,2)],['boom',round(tp,2)]]
ev.append(['pop',marks['chip']])
tb=find('construir bucles')
if tb: ev.append(['ding',round(tb,2)])
ev.append(['pop',round(handle+0.8,2)])
ev=[e for e in ev if e[1]>=0]
json.dump(ev,open('edicao/sfx_events.json','w'),indent=1)
print('marks',marks)
print('sfx',ev)

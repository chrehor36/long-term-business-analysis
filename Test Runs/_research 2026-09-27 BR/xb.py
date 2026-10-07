import json,sys,io
from datetime import date
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
F=json.load(open('companyfacts.json'))['facts']['us-gaap']
def ser(tag,instant=False,vint='newest'):
    out={}
    if tag not in F: return out
    for u,arr in F[tag]['units'].items():
        for x in arr:
            if x.get('form') not in ('10-K','10-K/A'): continue
            if not instant:
                if 'start' not in x: continue
                d=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days
                if not 340<=d<=380: continue
            elif 'start' in x: continue
            e=x['end']
            if e not in out or (x['filed']>out[e][1] if vint=='newest' else x['filed']<out[e][1]): out[e]=(x['val'],x['filed'])
    return {k:v[0]/1e6 for k,v in out.items()}
tags=sys.argv[1:] 
for t in tags:
    inst=t.startswith('@'); t=t.lstrip('@')
    s=ser(t,inst)
    print(t, ' '.join(f"{k[:4]}:{v:,.1f}" for k,v in sorted(s.items())))

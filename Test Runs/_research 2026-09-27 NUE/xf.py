"""Annual (FY, 10-K, full-year duration) facts from companyfacts, newest filed vintage per fiscal year end. Screening only."""
import json,sys,io
from datetime import date
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
def load(p): return json.load(open(p))['facts']
def annual(F,tag,ns='us-gaap',inst=False):
    try: u=F[ns][tag]['units']
    except KeyError: return {}
    out={}
    for unit,L in u.items():
        for x in L:
            if not x.get('form','').startswith('10-K'): continue
            e=x['end']
            if inst:
                pass
            else:
                if 'start' not in x: continue
                d=(date.fromisoformat(e)-date.fromisoformat(x['start'])).days
                if d<350 or d>380: continue
            k=e
            if k not in out or x['filed']>out[k][1]: out[k]=(x['val'],x['filed'])
    return {k:v[0] for k,v in out.items()}
if __name__=='__main__':
    F=load(sys.argv[1])
    for t in sys.argv[2:]:
        inst=t.endswith('!'); t=t.rstrip('!')
        a=annual(F,t,inst=inst)
        print(t, {k[:4]:round(v/1e6,1) for k,v in sorted(a.items()) if k[5:7] in ('12','01')})

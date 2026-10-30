import json,sys
d=json.load(open('facts.json'))
g=d['facts']['us-gaap']
def annual(tag):
    if tag not in g: return {}
    out={}
    for u,vals in g[tag]['units'].items():
        for v in vals:
            if v.get('fp')=='FY' and v.get('form','').startswith('10-K'):
                s,e=v.get('start'),v['end']
                if s and (int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7])<11: continue
                yr=e[:4]
                if yr not in out: out[yr]=v['val']  # first filed
    return out
tags=sys.argv[1:]
for t in tags:
    a=annual(t); print(t, {k:round(v/1e6,1) if abs(v)>1e4 else v for k,v in sorted(a.items())})

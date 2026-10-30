import json,sys
d=json.load(open('facts.json'))['facts']
def annual(tag,ns='us-gaap',unit=None):
    if tag not in d.get(ns,{}): return {}
    u=d[ns][tag]['units']; unit=unit or list(u)[0]
    out={}
    for x in u[unit]:
        if x.get('fp')=='FY' and x.get('form','').startswith('10-K') and 'frame' in x and len(x['frame'])==6:
            out[x['frame']]=x['val']
    return out
tags=sys.argv[1:]
for t in tags:
    a=annual(t)
    print(t, {k:(round(v/1e6,1) if abs(v)>1e5 else v) for k,v in sorted(a.items())})

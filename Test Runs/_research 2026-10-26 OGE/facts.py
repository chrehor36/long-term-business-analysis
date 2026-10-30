import json,sys
d=json.load(open(sys.argv[1]))
g=d['facts']['us-gaap']
def annual(tag,unit='USD'):
    if tag not in g: return {}
    out={}
    for x in g[tag]['units'].get(unit,[]):
        if x.get('fp')=='FY' and x['form'].startswith('10-K'):
            if 'start' in x:
                from datetime import date
                s=date.fromisoformat(x['start']);e=date.fromisoformat(x['end'])
                if (e-s).days<350: continue
            y=x['end'][:4]
            # first-filed: keep earliest filed for each end
            if y not in out or x['filed']<out[y][1]:
                out[y]=(x['val'],x['filed'],x['accn'])
    return out
tags=sys.argv[2:]
for t in tags:
    a=annual(t)
    print(t, {k:round(v[0]/1e6,1) for k,v in sorted(a.items())})

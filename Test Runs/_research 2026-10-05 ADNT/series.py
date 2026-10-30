import json,sys
d=json.load(open('facts.json'))['facts']
def ser(tag,ns='us-gaap'):
    if tag not in d.get(ns,{}): return {}
    out={}
    for u,arr in d[ns][tag]['units'].items():
        for x in arr:
            if x.get('form') not in ('10-K','10-K/A'): continue
            if 'start' in x:
                from datetime import date
                s=date.fromisoformat(x['start']);e=date.fromisoformat(x['end'])
                if not 340<(e-s).days<380: continue
            fy=x['end'][:4]
            # keep latest filed
            if fy not in out or x['filed']>out[fy][1]:
                out[fy]=(x['val'],x['filed'])
    return {k:v[0] for k,v in out.items()}
tags=sys.argv[1:]
yrs=[str(y) for y in range(2015,2026)]
print('tag'.ljust(60),' '.join(y.rjust(7) for y in yrs))
for t in tags:
    s=ser(t)
    print(t[:60].ljust(60),' '.join((str(round(s[y]/1e6)) if y in s else '-').rjust(7) for y in yrs))

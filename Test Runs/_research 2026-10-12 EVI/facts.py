import json,sys
d=json.load(open('cache/facts.json'))
g=d['facts']['us-gaap']
tags=sys.argv[1:]
for t in tags:
    if t not in g: print(t,'MISSING'); continue
    u=list(g[t]['units'].values())[0]
    rows={}
    for x in u:
        if x.get('fp')=='FY' and x.get('form','').startswith('10-K'):
            # annual duration ~ 1 year
            if 'start' in x:
                from datetime import date
                s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                if (e-s).days<350: continue
            rows.setdefault(x['end'],x['val'])
    print(t, ' '.join(f"{k[:7]}:{v/1e3:,.0f}" for k,v in sorted(rows.items()) if k>='2015'))

import json,sys
d=json.load(open('cache/facts.json'))
g=d['facts'].get('us-gaap',{})
tags=sys.argv[1:]
for t in tags:
    if t not in g: print(t,'MISSING');continue
    u=list(g[t]['units'].values())[0]
    rows={}
    for x in u:
        if x.get('fp')=='FY' and x['form'].startswith('10-K'):
            if 'start' in x:
                from datetime import date
                s=date.fromisoformat(x['start']);e=date.fromisoformat(x['end'])
                if (e-s).days<300: continue
            rows.setdefault(x['end'],(x['val'],x['accn']))
    print(t, ' '.join(f"{k[:4]}:{v[0]/1e6:.1f}" for k,v in sorted(rows.items())))

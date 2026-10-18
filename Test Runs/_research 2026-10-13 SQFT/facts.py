import json,sys
d=json.load(open(sys.argv[1]))
g=d['facts'].get('us-gaap',{})
tags=sys.argv[2].split(',')
for t in tags:
    if t not in g: print(t,'MISSING'); continue
    u=g[t]['units']; k=list(u.keys())[0]
    rows={}
    for x in u[k]:
        if x.get('form') not in ('10-K','10-K/A'): continue
        if 'frame' in x or True:
            dur = x.get('start')
            key=x['end']
            if dur:
                from datetime import date
                s=date.fromisoformat(dur); e=date.fromisoformat(x['end'])
                if (e-s).days<340: continue
            rows[key]=(x['val'],x['accn'],x['filed'])
    print(t)
    for e in sorted(rows):
        if e>='2014': print('  ',e,f"{rows[e][0]:,.0f}",rows[e][1])

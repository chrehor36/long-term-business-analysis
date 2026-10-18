import json,sys
d=json.load(open('cache/facts.json'))['facts']['us-gaap']
tags=sys.argv[1:]
for t in tags:
    if t not in d: print(t,'MISSING'); continue
    u=list(d[t]['units'].values())[0]
    rows={}
    for x in u:
        if x.get('fp')=='FY' and x.get('form') in ('10-K',) and 'frame' in x or (x.get('fp')=='FY' and x.get('form')=='10-K'):
            if 'start' in x:
                from datetime import date
                s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                if (e-s).days<340: continue
            rows.setdefault(x['end'],(x['val'],x['accn']))
    print(t)
    for k in sorted(rows)[-20:]:
        print('  ',k,round(rows[k][0]/1e6,1),rows[k][1])

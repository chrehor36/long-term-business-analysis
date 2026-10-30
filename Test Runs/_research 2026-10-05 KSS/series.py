import json,sys
f=json.load(open(sys.argv[1]))['facts']
tags=sys.argv[2].split(',')
for t in tags:
    for ns in ('us-gaap','dei'):
        if t in f.get(ns,{}):
            u=f[ns][t]['units']; unit=list(u)[0]
            rows={}
            for x in u[unit]:
                if x.get('form') in ('10-K','10-K/A') and x.get('fp')=='FY':
                    if 'start' in x:
                        from datetime import date
                        d0=date.fromisoformat(x['start']); d1=date.fromisoformat(x['end'])
                        if (d1-d0).days<350: continue
                    rows.setdefault(x['end'],x['val'])
            print(t, unit)
            for k in sorted(rows): print('  ',k, rows[k])

import json,sys
f=json.load(open('cache/facts.json'))
ks=sys.argv[1].split(',')
for k in ks:
    for ns in ('ifrs-full','sbs'):
        if k in f['facts'].get(ns,{}):
            v=f['facts'][ns][k]; break
    else:
        print(k,'MISSING'); continue
    out={}
    for u,arr in v['units'].items():
        for x in arr:
            if not x.get('form','').startswith('20-F'): continue
            end=x['end']; st=x.get('start')
            if st and not (st[5:]=='01-01' and end[5:]=='12-31'): continue
            if not st and end[5:]!='12-31': continue
            key=end[:4]
            # prefer latest filing
            if key not in out or x['filed']>out[key][1]:
                out[key]=(x['val'],x['filed'],x['accn'])
    print(k.ljust(60),' '.join(f"{y}:{out[y][0]/1e6:,.0f}" for y in sorted(out)))

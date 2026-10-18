import json,sys
from datetime import date
d=json.load(open(sys.argv[1]))['facts']['us-gaap']
for k in sys.argv[2:]:
    if k not in d: print('MISSING',k); continue
    rows={}
    for un,arr in d[k]['units'].items():
        for x in arr:
            if x.get('form')!='10-K' or x.get('fp')!='FY': continue
            if 'start' in x and (date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<340: continue
            rows.setdefault(x['end'][:4],(x['val'],x['accn']))
    print(k,' '.join(f"{y}:{v/1e6:.0f}" for y,(v,a) in sorted(rows.items()) if y>='2015'))
    print('   accns', sorted(set(a for y,(v,a) in rows.items() if y>='2023')))

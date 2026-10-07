import json,sys,os
sys.path.insert(0,'.')
from fetch import get
cik=sys.argv[1]; out=sys.argv[2]
p=os.path.join(os.path.dirname(os.path.abspath(__file__)),out)
if not os.path.exists(p):
    open(p,'w',encoding='utf-8').write(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{str(int(cik)).zfill(10)}.json"))
j=json.load(open(p,encoding='utf-8'))
tags=sys.argv[3].split(',')
for t in tags:
    for ns in ('us-gaap','mho','dei'):
        if t in j['facts'].get(ns,{}):
            units=j['facts'][ns][t]['units']
            for u,vals in units.items():
                res={}
                for v in vals:
                    if v.get('form') not in ('10-K','10-K/A'): continue
                    if 'start' in v:
                        from datetime import date
                        s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
                        if not 340<(e-s).days<380: continue
                    fy=v['end'][:4]
                    res.setdefault(fy,(v['val'],v['accn']))  # earliest-filed first? keep first seen
                print(t,u, ' '.join(f"{k}:{res[k][0]/1e6 if abs(res[k][0])>1e5 else res[k][0]:.1f}" for k in sorted(res)))

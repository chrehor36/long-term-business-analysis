import json, time
from fetch import get
from datetime import date
def ann(f, tag):
    if tag not in f: return {}
    out={}
    for u,rows in f[tag]['units'].items():
        for r in rows:
            if r.get('form') not in ('10-K','10-K/A') or r.get('fp')!='FY': continue
            if 'start' in r:
                d=(date.fromisoformat(r['end'])-date.fromisoformat(r['start'])).days
                if d<340 or d>380: continue
            out.setdefault(r['end'],{})[r['filed']]=r['val']
    return {e:v[max(v)] for e,v in out.items()}
F=json.load(open('cache/facts_FRTA.json')); f=F['facts'].get('us-gaap',{})
print([k for k in f if 'Revenue' in k or 'Sales' in k or 'GrossProfit' in k or k=='OperatingIncomeLoss'])
for t,c in {'SMID':'0000924719'}.items():
    b=get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json'); open(f'cache/facts_{t}.json','wb').write(b)
for t in ['FRTA','SMID']:
    F=json.load(open(f'cache/facts_{t}.json')); f=F['facts'].get('us-gaap',{})
    print('=====', t, F.get('entityName'))
    rev={}
    for tag in ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet']:
        for k,v in ann(f,tag).items(): rev.setdefault(k,v)
    gp=ann(f,'GrossProfit'); oi=ann(f,'OperatingIncomeLoss')
    for k in sorted(set(rev)|set(gp)|set(oi)):
        r=rev.get(k); g=gp.get(k); o=oi.get(k)
        print(k, 'rev', r and round(r/1e6,1), 'gp', g and round(g/1e6,1), 'gm%', (g is not None and r) and round(100*g/r,1), 'oi', o and round(o/1e6,1), 'om%', (o is not None and r) and round(100*o/r,1))

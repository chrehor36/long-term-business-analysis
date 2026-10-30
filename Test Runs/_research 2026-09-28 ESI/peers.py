import json, os
from datetime import date
from fetch import get
P={'kwr':'0000081362','mksi':'0001049502'}
out={}
for k,c in P.items():
    p=f'cache/peers/facts_{k}.json'
    if not os.path.exists(p): open(p,'wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json'))
    f=json.load(open(p))['facts']['us-gaap']
    def ser(t):
        r={}
        for u,arr in f.get(t,{}).get('units',{}).items():
            for x in arr:
                if x.get('form')!='10-K' or 'start' not in x: continue
                d=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days
                if 350<=d<=380: r[int(x['end'][:4])]=x['val']/1e6
        return r
    rev=ser('Revenues') or {}
    rev.update({k2:v for k2,v in ser('RevenueFromContractWithCustomerExcludingAssessedTax').items() if k2 not in rev})
    gp=ser('GrossProfit'); oi=ser('OperatingIncomeLoss'); am=ser('AmortizationOfIntangibleAssets')
    print('==',k,c)
    for y in range(2014,2026):
        if y in rev:
            print(y, f"rev {rev[y]:.1f}", f"GM {100*gp[y]/rev[y]:.1f}" if y in gp else '', f"OM {100*oi[y]/rev[y]:.1f}" if y in oi else '', f"OM+amort {100*(oi[y]+am.get(y,0))/rev[y]:.1f}" if y in oi and y in am else '')

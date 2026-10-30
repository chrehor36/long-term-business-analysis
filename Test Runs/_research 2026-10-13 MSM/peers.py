import json,sys
from datetime import date
def series(d,tags,dur=True):
    out={}
    for t in tags:
        if t not in d: continue
        for u in d[t]['units'].values():
            for x in u:
                if x.get('form')!='10-K' or x.get('fp')!='FY': continue
                if dur:
                    if 'start' not in x: continue
                    if (date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<340: continue
                out.setdefault(x['end'][:4],(x['val'],x['accn']))
    return out
for tk in ['MSM','GWW','FAST','GIC']:
    f='cache/facts.json' if tk=='MSM' else f'cache/peers/{tk}.json'
    d=json.load(open(f))['facts']['us-gaap']
    rev=series(d,['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','SalesRevenueNet','SalesRevenueGoodsNet'])
    oi=series(d,['OperatingIncomeLoss'])
    eq=series(d,['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],dur=False)
    gp=series(d,['GrossProfit'])
    print(tk)
    for y in sorted(oi):
        if y<'2012': continue
        r=rev.get(y,(None,))[0]; o=oi[y][0]; g=gp.get(y,(None,))[0]
        print(' ',y,'rev',round(r/1e6) if r else None,'OI',round(o/1e6),'OM%',round(100*o/r,1) if r else None,'GM%',round(100*g/r,1) if g and r else None,'eq',round(eq.get(y,(0,))[0]/1e6),oi[y][1])

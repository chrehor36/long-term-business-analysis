import json, os, sys, time
from datetime import date
from fetch import get
sys.stdout.reconfigure(encoding='utf-8')
P = {'OII':'0000073756','HLX':'0000866829','FTI':'0001681459','OIS':'0001121484','DRQ_INVX':'0001042893','TDW':'0000098222'}
def facts(t, cik):
    fn = f'cache/peers/{t}_facts.json'
    if not os.path.exists(fn):
        open(fn,'wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json')); time.sleep(0.3)
    return json.load(open(fn))
def annual(f, tags):
    out = {}
    for tx in ('us-gaap','ifrs-full'):
        g = f['facts'].get(tx, {})
        for t in tags:
            if t not in g: continue
            for u, arr in g[t]['units'].items():
                if u not in ('USD',): continue
                for x in arr:
                    if x.get('form') not in ('10-K','10-K/A','20-F','40-F') or 'start' not in x: continue
                    d = (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days
                    if 350 <= d <= 380:
                        fy = int(x['end'][:4]) if x['end'][5:7] > '03' else int(x['end'][:4]) - 1
                        out.setdefault(fy, {})[t] = (x['val'], x['accn'], x['end'])
    return out
REV = ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet','Revenue']
GP = ['GrossProfit']
OI = ['OperatingIncomeLoss','ProfitLossFromOperatingActivities']
COGS = ['CostOfRevenue','CostOfGoodsAndServicesSold','CostOfGoodsSold','CostOfSales']
for t, cik in P.items():
    f = facts(t, cik)
    r = annual(f, REV); g = annual(f, GP); o = annual(f, OI); c = annual(f, COGS)
    print('==', t, f.get('entityName'))
    for fy in sorted(set(r) | set(g)):
        if fy < 2008: continue
        rv = max((v for v in r.get(fy, {}).values()), key=lambda z: z[2], default=None)
        if not rv: continue
        rev = rv[0]
        gp = next(iter(g.get(fy, {}).values()), None)
        gpv = gp[0] if gp else (rev - next(iter(c[fy].values()))[0] if fy in c else None)
        oi = next(iter(o.get(fy, {}).values()), None)
        print(fy, rv[2], f"rev {rev/1e6:,.0f}", f"gm {100*gpv/rev:.1f}%" if gpv else 'gm n/a', f"om {100*oi[0]/rev:.1f}%" if oi else 'om n/a', rv[1])

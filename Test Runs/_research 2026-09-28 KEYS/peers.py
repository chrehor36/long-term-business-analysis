import json, os, sys, time
from datetime import date
from fetch import get
sys.stdout.reconfigure(encoding='utf-8')
P = {'KEYS':'0001601046','NATI':'0000935494','XXIA':'0001120295','VIAV':'0000912093','TER':'0000097210','RAL':'0002041385','FTV':'0001659166','CDNS':'0000813672','SNPS':'0000883241','ANSS':'0001013462'}
def facts(t, cik):
    fn = f'cache/peers/{t}_facts.json'
    if not os.path.exists(fn):
        open(fn,'wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json')); time.sleep(0.3)
    return json.load(open(fn))
def annual(f, tags):
    out = {}
    g = f['facts'].get('us-gaap', {})
    for t in tags:
        if t not in g: continue
        for u, arr in g[t]['units'].items():
            if u != 'USD': continue
            for x in sorted(arr, key=lambda z: z.get('filed','')):
                if x.get('form') not in ('10-K','10-K/A') or 'start' not in x: continue
                d = (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days
                if 350 <= d <= 380:
                    e=date.fromisoformat(x['end']); fy = e.year if e.month>3 else e.year-1
                    out.setdefault(fy, {})[t] = (x['val'], x['accn'], x['end'])   # latest filed wins per tag
    return out
REV = ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet']
res={}
for t, cik in P.items():
    f = facts(t, cik)
    r = annual(f, REV); o = annual(f, ['OperatingIncomeLoss']); gp = annual(f, ['GrossProfit']); cr = annual(f, ['CostOfRevenue','CostOfGoodsAndServicesSold'])
    print('==', t, f.get('entityName'))
    for fy in sorted(set(r)):
        if fy < 2008: continue
        rv = max(r[fy].values(), key=lambda z: z[0])
        oi = o.get(fy, {}).get('OperatingIncomeLoss')
        g = gp.get(fy, {}).get('GrossProfit')
        if not g and fy in cr:
            c = max(cr[fy].values(), key=lambda z: z[0]); g = (rv[0]-c[0], c[1], 'derived')
        row = {'rev': rv[0]/1e6}
        if oi: row['om'] = 100*oi[0]/rv[0]
        if g: row['gm'] = 100*g[0]/rv[0]
        res.setdefault(t,{})[fy]=row
        print(fy, rv[2], f"rev {rv[0]/1e6:,.0f}", f"gm {row.get('gm',float('nan')):.1f}", f"om {row.get('om',float('nan')):.1f}", (oi or rv)[1])
json.dump(res, open('peers_m.json','w'), indent=0)

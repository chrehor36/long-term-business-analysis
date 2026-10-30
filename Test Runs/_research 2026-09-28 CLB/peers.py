import json, os, sys, time
from datetime import date
from fetch import get
sys.stdout.reconfigure(encoding='utf-8')
P = {'CLB_NV':'0001000229','CLB':'0001958086','SLB':'0000087347','HAL':'0000045012','BKR':'0001701605','WFRD':'0001603923','OIS':'0001121484','BOOM_DMC':'0000034067','NCSM':'0001692427','NINE':'0001532286'}
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
            for x in arr:
                if x.get('form') not in ('10-K','10-K/A') or 'start' not in x: continue
                d = (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days
                if 350 <= d <= 380:
                    fy = int(x['end'][:4])
                    out.setdefault(fy, {})[t] = (x['val'], x['accn'], x['end'])   # latest filed wins per tag
    return out
REV = ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueServicesNet']
OI = ['OperatingIncomeLoss']
res={}
for t, cik in P.items():
    f = facts(t, cik)
    r = annual(f, REV); o = annual(f, OI); ce = annual(f, ['CostsAndExpenses'])
    for fy in o:   # fallback where no revenue tag resolves: revenue = operating income + costs and expenses (labelled 'rev*')
        if fy not in r and fy in ce: r[fy] = {'derived': (o[fy]['OperatingIncomeLoss'][0] + ce[fy]['CostsAndExpenses'][0], ce[fy]['CostsAndExpenses'][1], 'derived')}
    print('==', t, f.get('entityName'))
    for fy in sorted(set(r)):
        if fy < 2008: continue
        rv = max(r[fy].values(), key=lambda z: z[0])
        oi = o.get(fy, {}).get('OperatingIncomeLoss')
        if oi: res.setdefault(t,{})[fy]=100*oi[0]/rv[0]
        print(fy, ('rev*' if 'derived' in r[fy] else 'rev'), f"{rv[0]/1e6:,.0f}", f"om {100*oi[0]/rv[0]:.1f}%" if oi else 'om n/a', (oi or rv)[1])
json.dump(res, open('peers_om.json','w'), indent=0)

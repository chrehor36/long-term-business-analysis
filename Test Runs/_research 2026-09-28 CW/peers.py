import sys, json, os, time
sys.path.insert(0,'../../tools')
import sources as S
from fetch import get
from datetime import date
T = ['MRCY','MOG-A','WWD','BWXT','TDY','HEI','TDG','DRS','DCO','ESE','CR','PH']
out = {}
for t in T:
    try:
        c = S.cik_for(t)
    except Exception as e:
        print(t, 'cik fail', e); continue
    cik = c[0] if isinstance(c, tuple) else c
    p = f'cache/peers/{t}_facts.json'
    if not os.path.exists(p):
        open(p,'wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{str(cik).zfill(10)}.json')); time.sleep(0.3)
    f = json.load(open(p))['facts'].get('us-gaap', {})
    def ann(tags):
        rows = {}
        for tg in tags:
            if tg not in f: continue
            for u, arr in f[tg]['units'].items():
                if u != 'USD': continue
                for x in arr:
                    if x.get('form') not in ('10-K','10-K/A') or 'start' not in x: continue
                    d = (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days
                    if 340 <= d <= 380: rows.setdefault(x['end'], x['val'])  # first vintage seen per tag order
        return rows
    rev = ann(['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet'])
    oi = ann(['OperatingIncomeLoss'])
    gp = ann(['GrossProfit'])
    print('=====', t, c)
    for e in sorted(set(rev) & set(oi)):
        if e[:4] >= '2012':
            g = gp.get(e)
            print(f'  {e} rev {rev[e]/1e6:9.1f} oi {oi[e]/1e6:8.1f} om {100*oi[e]/rev[e]:5.1f}%' + (f' gm {100*g/rev[e]:5.1f}%' if g else ''))

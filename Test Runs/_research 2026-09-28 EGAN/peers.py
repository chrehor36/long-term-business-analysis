import sys, json, os, time
sys.path.insert(0,'../../tools')
import sources as S
from fetch import get
from datetime import date
T = ['NICE','VRNT','UPLD','FIVN','LPSN','CRM','NOW','PEGA','EGAN']
out = {}
for t in T:
    try:
        c = {'VRNT':('0001166388','VERINT (manual CIK)'),'LPSN':('0001102993','LIVEPERSON (manual CIK)')}.get(t) or S.cik_for(t)
        if c is None or (isinstance(c,tuple) and c[0] is None): print(t,'no cik'); continue
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
                    if x.get('form') not in ('10-K','10-K/A','20-F','20-F/A') or 'start' not in x: continue
                    d = (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days
                    if 340 <= d <= 380: rows.setdefault(x['end'], x['val'])  # first vintage seen per tag order
        return rows
    rev = ann(['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet'])
    oi = ann(['OperatingIncomeLoss'])
    gp = ann(['GrossProfit'])
    print('=====', t, c)
    for e in sorted(set(rev) & set(oi)):
        if e[:4] >= '2014':
            g = gp.get(e)
            print(f'  {e} rev {rev[e]/1e6:9.1f} oi {oi[e]/1e6:8.1f} om {100*oi[e]/rev[e]:5.1f}%' + (f' gm {100*g/rev[e]:5.1f}%' if g else ''))

import sys, os, json, time
sys.path.insert(0,'..')
from fetch import get
P={'CTS':26058,'LFUS':889331,'SRI':1043337,'TEL':1385157,'ALGM':866291,'MEAS':778734,'APH':820313}
for t,c in P.items():
    fn=f'{t}_companyfacts.json'
    if not os.path.exists(fn):
        open(fn,'wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json')); time.sleep(0.3)
    d=json.load(open(fn)); g=d['facts'].get('us-gaap',{})
    def ser(tags):
        out={}
        for tg in tags:
            if tg not in g: continue
            for u in g[tg]['units'].values():
                for f in u:
                    if f.get('form') not in ('10-K',) or 'start' not in f: continue
                    from datetime import date
                    dd=(date.fromisoformat(f['end'])-date.fromisoformat(f['start'])).days
                    if dd<350 or dd>380: continue
                    out.setdefault(f['end'][:7],f['val'])
        return out
    rv=ser(['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet'])
    oi=ser(['OperatingIncomeLoss'])
    gp=ser(['GrossProfit'])
    print('==',t,d.get('entityName'))
    print(' ', ' '.join(f"{k}:{oi[k]/rv[k]*100:.1f}%" for k in sorted(oi) if k in rv))
    print('  GM', ' '.join(f"{k}:{gp[k]/rv[k]*100:.1f}%" for k in sorted(gp) if k in rv))

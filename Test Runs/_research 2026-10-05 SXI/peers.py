import json, urllib.request, time
from datetime import date
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
tick=json.loads(urllib.request.urlopen(urllib.request.Request('https://www.sec.gov/files/company_tickers.json',headers=UA)).read())
m={v['ticker']:v['cik_str'] for v in tick.values()}
def series(d,tags,dur=True):
    out={}
    for t in tags:
        if t not in d: continue
        for x in list(d[t]['units'].values())[0]:
            if x['form'] not in ('10-K','20-F','10-K/A') or x.get('fp')!='FY': continue
            if dur:
                if 'start' not in x: continue
                if (date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<350: continue
            k=x['end'][:4]
            out.setdefault(k,x['val'])
    return out
for T in ['LFUS','CTS','ST']:
    cik=m[T]
    j=json.loads(urllib.request.urlopen(urllib.request.Request(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json',headers=UA)).read())
    json.dump(j,open(f'peers/{T}_facts.json','w'))
    d=j['facts']['us-gaap']
    rev=series(d,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet'])
    oi=series(d,['OperatingIncomeLoss'])
    ocf=series(d,['NetCashProvidedByUsedInOperatingActivities'])
    cap=series(d,['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'])
    sbc=series(d,['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'])
    eq=series(d,['StockholdersEquity'],dur=False)
    gw=series(d,['Goodwill'],dur=False)
    print(T,cik)
    for y in sorted(rev):
        if y<'2009': continue
        r=rev.get(y);o=oi.get(y)
        print(' ',y,'rev',round(r/1e6) if r else None,'OI',round(o/1e6) if o else None,'m%',round(100*o/r,1) if r and o else None,'OCF',round(ocf.get(y,0)/1e6),'capex',round(cap.get(y,0)/1e6),'sbc',round(sbc.get(y,0)/1e6),'eq',round(eq.get(y,0)/1e6),'gw',round(gw.get(y,0)/1e6))
    time.sleep(0.5)

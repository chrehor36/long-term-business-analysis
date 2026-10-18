import json, urllib.request, sys, time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
peers={'Masonglory (MSGY)':'0002020228','Ming Shing (MSW)':'0001956166','SU Group (SUGP)':'0001969863','Wang & Lee (WLGS)':'0001899658'}
tags=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','GrossProfit','OperatingIncomeLoss','NetIncomeLoss','ProfitLoss','StockholdersEquity','Assets','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest']
for name,cik in peers.items():
    d=json.load(urllib.request.urlopen(urllib.request.Request(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json',headers=UA),timeout=60))
    json.dump(d,open(f'cache/facts_{cik}.json','w'))
    print('=====',name)
    g=d['facts'].get('us-gaap',{})
    for t in tags:
        if t not in g: continue
        for unit,vals in g[t]['units'].items():
            rows={}
            for v in vals:
                if v.get('form') not in ('20-F','F-1','F-1/A','10-K','20-F/A'): continue
                if 'start' in v:
                    import datetime as D
                    dd=(D.date.fromisoformat(v['end'])-D.date.fromisoformat(v['start'])).days
                    if dd<340: continue
                k=v['end']
                rows.setdefault(k,(v['val'],v['accn'],v['form']))
            print(' ',t,unit,{k:(round(r[0]/1e6,3),r[1]) for k,r in sorted(rows.items())})
    time.sleep(0.3)

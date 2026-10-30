import json,urllib.request,time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
COS={'CVX':'0000093410','COP':'0001163165','EOG':'0000821189','FANG':'0001539838','DVN':'0001090012'}
TAGS=['NetCashProvidedByUsedInOperatingActivities',
      'DepreciationDepletionAndAmortization',
      'CashAndCashEquivalentsAtCarryingValue']
for t,cik in COS.items():
    for tag in TAGS:
        url=f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/us-gaap/{tag}.json"
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request(url,headers=UA)))
        except Exception as e:
            print(t,tag,'ERR',e); continue
        for u in d['units']['USD']:
            if u.get('fy')==2025 and u.get('fp')=='FY' and u.get('form')=='10-K' \
               and u.get('end')=='2025-12-31' and u.get('start','2025-01-01')=='2025-01-01':
                print(f"{t:5} {tag[:42]:44} {u['val']/1e6:>12,.0f}  acc={u['accn']}")
                break
        time.sleep(0.15)

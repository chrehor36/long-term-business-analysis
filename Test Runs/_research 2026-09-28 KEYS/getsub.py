import json, sys
from fetch import get
cik='0001601046'
b=get(f'https://data.sec.gov/submissions/CIK{cik}.json'); open(f'cache/sub_{cik}.json','wb').write(b)
d=json.loads(b)
print('=====', cik, d['name'], d.get('fiscalYearEnd'), d.get('stateOfIncorporation'), d.get('sicDescription'), d.get('category'), d.get('exchanges'), d.get('tickers'))
print('former', d.get('formerNames'))
r=d['filings']['recent']
for i in range(len(r['form'])):
    f=r['form'][i]
    if f in ('144','4','3','5','SC 13G','SC 13G/A','4/A','S-8 POS','SC 13D/A','11-K','S-8','FWP','424B2','424B5','424B3','SD','CERT','8-A12B') : continue
    if r['filingDate'][i] < '2024-06-01' and f not in ('10-K','10-K/A','10-12B','10-12B/A','8-K'): continue
    if r['filingDate'][i] < '2024-06-01' and f=='8-K' and not any(x in r['items'][i] for x in ('1.01','2.01','8.01')): continue
    print(r['filingDate'][i], f, r['accessionNumber'][i], r['primaryDocument'][i], r['items'][i], r['reportDate'][i])
print(d['filings'].get('files'))

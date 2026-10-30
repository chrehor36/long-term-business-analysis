import json, sys
from fetch import get
cik='0000026324'
b=get(f'https://data.sec.gov/submissions/CIK{cik}.json'); open(f'cache/sub_{cik}.json','wb').write(b)
d=json.loads(b)
print('=====', cik, d['name'], d.get('fiscalYearEnd'), d.get('stateOfIncorporation'), d.get('sicDescription'), d.get('category'), d.get('exchanges'), d.get('tickers'))
print('former', d.get('formerNames'))
def show(r):
    for i in range(len(r['form'])):
        f=r['form'][i]
        if f in ('144','4','3','5','SC 13G','SC 13G/A','4/A','S-8 POS','SC 13D/A','11-K','S-8','FWP','424B2','424B5','424B3','SD','CERT','8-A12B','SCHEDULE 13G','SCHEDULE 13G/A') : continue
        if r['filingDate'][i] < '2025-06-01' and f not in ('10-K','10-K/A','10-12B','10-12B/A','8-K','8-K/A','S-4','S-4/A','DEFM14A','DEF 14A','424B3','S-1','S-1/A','10-Q'): continue
        if r['filingDate'][i] < '2025-06-01' and f in ('8-K','8-K/A') and not any(x in r['items'][i] for x in ('1.01','2.01','8.01','4.02','2.05','2.06')): continue
        print(r['filingDate'][i], f, r['accessionNumber'][i], r['primaryDocument'][i], r['items'][i], r['reportDate'][i])
show(d['filings']['recent'])
print(d['filings'].get('files'))
for fx in d['filings'].get('files',[]):
    b2=get('https://data.sec.gov/submissions/'+fx['name']); open('cache/'+fx['name'],'wb').write(b2)
    show(json.loads(b2))

import json
from fetch import get
cik='0001618673'
b=get(f'https://data.sec.gov/submissions/CIK{cik}.json'); open(f'cache/sub_{cik}.json','wb').write(b)
d=json.loads(b)
print('=====', cik, d['name'], d.get('fiscalYearEnd'), d.get('stateOfIncorporation'), d.get('sicDescription'), d.get('category'), d.get('exchanges'), d.get('tickers'))
print('former', d.get('formerNames'))
skip={'144','4','3','5','4/A','3/A','S-8 POS','11-K','S-8','FWP','424B2','424B5','SD','CERT','8-A12B','SCHEDULE 13G','SCHEDULE 13G/A','SC 13G','SC 13G/A'}
def show(r):
    for i in range(len(r['form'])):
        f=r['form'][i]
        if f in skip: continue
        print(r['filingDate'][i], f, r['accessionNumber'][i], r['primaryDocument'][i], r['items'][i], r['reportDate'][i])
show(d['filings']['recent'])
for fx in d['filings'].get('files',[]):
    b2=get('https://data.sec.gov/submissions/'+fx['name']); open('cache/'+fx['name'],'wb').write(b2)
    show(json.loads(b2))

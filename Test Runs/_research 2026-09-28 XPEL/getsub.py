import json
from fetch import get
b=get('https://data.sec.gov/submissions/CIK0001767258.json'); open('cache/sub.json','wb').write(b)
d=json.loads(b)
print(d['name'], d.get('fiscalYearEnd'), d.get('stateOfIncorporation'), d.get('sicDescription'), d.get('category'), d.get('exchanges'))
print('former', d.get('formerNames'))
r=d['filings']['recent']
for i in range(len(r['form'])):
    f=r['form'][i]
    if f in ('144','4','3','5','SC 13G','SC 13G/A') : continue
    print(r['filingDate'][i], f, r['accessionNumber'][i], r['primaryDocument'][i], r['items'][i], r['reportDate'][i])
print(d['filings'].get('files'))

import json
from fetch import get
b=get('https://data.sec.gov/submissions/CIK0001601046-submissions-001.json'); open('cache/sub_001.json','wb').write(b)
r=json.loads(b)
for i in range(len(r['form'])):
    f=r['form'][i]
    if f in ('10-K','10-K/A','10-12B','10-12B/A','10-Q') or (f=='8-K' and any(x in r['items'][i] for x in ('1.01','2.01','8.01'))):
        print(r['filingDate'][i], f, r['accessionNumber'][i], r['primaryDocument'][i], r['items'][i], r['reportDate'][i])

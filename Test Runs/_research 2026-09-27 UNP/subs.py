import json,sys,os
from fetch import get
b=get('https://data.sec.gov/submissions/CIK0000100885.json')
open('submissions.json','wb').write(b)
d=json.loads(b)
r=d['filings']['recent']
for i in range(len(r['form'])):
    if r['filingDate'][i]>='2025-01-01':
        print(r['filingDate'][i],r['form'][i],r['accessionNumber'][i],r['primaryDocument'][i],r.get('items',[''])[i] if 'items' in r else '')
print(d['filings'].get('files'))

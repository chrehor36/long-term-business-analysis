import json
from fetch import get
CIK='0001701758'
j=json.loads(get(f'https://data.sec.gov/submissions/CIK{CIK}.json'))
open('submissions.json','w').write(json.dumps(j))
print(j['name'], j.get('formerNames'), j.get('fiscalYearEnd'), j.get('stateOfIncorporation'))
rows=[]
def add(r):
    for d,f,it,acc,doc in zip(r['filingDate'],r['form'],r['items'],r['accessionNumber'],r['primaryDocument']):
        rows.append((d,f,it,acc,doc))
add(j['filings']['recent'])
for fx in j['filings'].get('files',[]):
    add(json.loads(get('https://data.sec.gov/submissions/'+fx['name'])))
rows.sort(reverse=True)
json.dump(rows,open('allfilings.json','w'))
print(len(rows), rows[-1][0], rows[0][0])
from collections import Counter
print(Counter(r[1] for r in rows).most_common())
for r in rows:
    if r[1] in ('10-K','10-K/A','10-Q/A','S-4','425','SC TO-T','SC TO-C','SC 14D9','DEFM14A','PREM14A','8-K','8-K/A','SC 13E3') and r[0]>='2023-01-01':
        print(r)

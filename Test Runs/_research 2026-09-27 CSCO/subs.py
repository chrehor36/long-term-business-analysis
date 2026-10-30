import json, sys
from fetch import get
CIK='0000858877'
j=json.loads(get(f'https://data.sec.gov/submissions/CIK{CIK}.json'))
open('submissions.json','w').write(json.dumps(j))
rows=[]
def add(r):
    for d,f,it,acc,doc in zip(r['filingDate'],r['form'],r['items'],r['accessionNumber'],r['primaryDocument']):
        rows.append((d,f,it,acc,doc))
add(j['filings']['recent'])
for fx in j['filings'].get('files',[]):
    k=json.loads(get('https://data.sec.gov/submissions/'+fx['name']))
    add(k)
rows.sort(reverse=True)
json.dump(rows,open('allfilings.json','w'))
print(len(rows), rows[-1][0], rows[0][0])
for r in rows:
    if r[1] in ('10-K','10-K/A','10-Q','10-Q/A','DEF 14A','S-4','425','SC TO-T','SC TO-C','SC 14D9','8-K') and r[0]>='2023-06-01':
        print(r)

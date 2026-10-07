import json
from fetch import get
d=json.load(open('cache/sub.json'))
rows=[]
def add(r):
    for i in range(len(r['form'])):
        if r['form'][i] in ('10-K','10-K405','10-K/A'):
            rows.append((r['filingDate'][i], r['form'][i], r['accessionNumber'][i], r['primaryDocument'][i], r['reportDate'][i]))
add(d['filings']['recent'])
for f in d['filings'].get('files',[]):
    b=get('https://data.sec.gov/submissions/'+f['name']); open('cache/'+f['name'],'wb').write(b)
    add(json.loads(b))
for r in sorted(rows): print(*r)

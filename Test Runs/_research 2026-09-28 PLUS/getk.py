import json, os, time, sys
sys.path.insert(0,'.')
from fetch import get, strip
out=[]
for fn in ('cache/submissions.json','cache/submissions001.json'):
    s=json.load(open(fn))
    r=s['filings']['recent'] if 'filings' in s else s
    for i,f in enumerate(r['form']):
        if f in ('10-K','10-K405'): out.append((r['reportDate'][i],r['filingDate'][i],r['accessionNumber'][i],r['primaryDocument'][i]))
out.sort()
for rd,fd,acc,doc in [o for o in out if o[0]>="2005"]:
    p=f'cache/k_{rd}.txt'
    print(rd,fd,acc,doc)
    if not os.path.exists(p) and doc:
        b=get(f'https://www.sec.gov/Archives/edgar/data/1022408/{acc.replace("-","")}/{doc}')
        open(p,'w',encoding='utf-8').write(strip(b)); time.sleep(0.3)

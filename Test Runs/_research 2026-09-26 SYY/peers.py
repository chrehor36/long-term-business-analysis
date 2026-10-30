import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
P={'USFD':'0001665918','PFGC':'0001618673','CHEF':'0001517175'}
for tk,cik in P.items():
    sj=json.loads(get(f'https://data.sec.gov/submissions/CIK{cik}.json'))
    open(f'peers/{tk}_sub.json','w').write(json.dumps(sj))
    b=get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json'); open(f'peers/{tk}_facts.json','wb').write(b)
    r=sj['filings']['recent']
    ks=[(r['filingDate'][i],r['accessionNumber'][i],r['primaryDocument'][i],r['reportDate'][i]) for i in range(len(r['form'])) if r['form'][i]=='10-K']
    print(tk, sj['name'], ks[:8])
    for fd,acc,doc,rd in ks[:1]:
        t=strip(get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}'))
        open(f'peers/{tk}_10K_{rd}.txt','w',encoding='utf-8').write(t); print(' saved',rd,len(t))
    time.sleep(0.5)

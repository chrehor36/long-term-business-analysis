import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
P={'USFD':'0001665918','PFGC':'0001618673'}
for tk,cik in P.items():
    sj=json.load(open(f'peers/{tk}_sub.json'))
    r=sj['filings']['recent']
    ks=[(r['filingDate'][i],r['accessionNumber'][i],r['primaryDocument'][i],r['reportDate'][i]) for i in range(len(r['form'])) if r['form'][i]=='10-K']
    for fd,acc,doc,rd in ks[1:8]:
        fn=f'peers/{tk}_10K_{rd}.txt'
        if os.path.exists(fn): continue
        t=strip(get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}'))
        open(fn,'w',encoding='utf-8').write(t); print(' saved',fn,len(t)); time.sleep(0.3)

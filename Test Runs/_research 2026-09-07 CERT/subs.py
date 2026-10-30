import json,sys
sys.path.insert(0,'.')
from fetch import get
for tic,cik in [('SLP','0001023459'),('SDGR','0001490978')]:
    b=get(f'https://data.sec.gov/submissions/CIK{cik}.json')
    open(f'submissions_{tic}.json','wb').write(b)
    d=json.loads(b)
    r=d['filings']['recent']
    print('====',tic,d['name'],'fye',d.get('fiscalYearEnd'))
    n=0
    for i in range(len(r['form'])):
        if r['form'][i] in ('10-K','10-Q','10-K/A'):
            print(r['form'][i], r['filingDate'][i], r['reportDate'][i], r['accessionNumber'][i], r['primaryDocument'][i])
            n+=1
            if n>=10: break

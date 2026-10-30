import json, sys, os
from fetch import get
from tables import flat
cik=sys.argv[1]; tag=sys.argv[2]; forms=sys.argv[3].split(','); n=int(sys.argv[4])
d=json.loads(get(f'https://data.sec.gov/submissions/CIK{cik}.json'))
r=d['filings']['recent']; got=0
for i in range(len(r['form'])):
    if r['form'][i] in forms and got<n:
        acc=r['accessionNumber'][i]; doc=r['primaryDocument'][i]; fd=r['filingDate'][i]
        out=f"peers/{tag}_{r['form'][i].replace(' ','')}_{fd}.txt"
        print(fd, r['form'][i], acc, doc)
        if not os.path.exists(out):
            b=get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}')
            open(out,'w',encoding='utf-8').write(flat(b))
        got+=1

import json, sys, os
from fetch import get
from tables import flat
# usage: python peerdoc.py CIK TAG [N]  -> latest N 10-Ks flattened to cache/peers/TAG_kYYYY.txt
cik, tag = sys.argv[1], sys.argv[2]; n = int(sys.argv[3]) if len(sys.argv)>3 else 1
d=json.loads(get(f'https://data.sec.gov/submissions/CIK{cik}.json')); r=d['filings']['recent']
k=[(r['reportDate'][i], r['accessionNumber'][i], r['primaryDocument'][i]) for i in range(len(r['form'])) if r['form'][i]=='10-K']
for rep, acc, doc in k[:n]:
    out=f'cache/peers/{tag}_k{rep[:4]}.txt'
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(flat(b)); print(out, acc, doc)

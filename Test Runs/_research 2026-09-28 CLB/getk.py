import os, json, sys
from fetch import get, strip
rows=[]
for cik in ('0001958086','0001000229'):
    d=json.load(open(f'cache/sub_{cik}.json')); r=d['filings']['recent']
    for i in range(len(r['form'])):
        if r['form'][i] in ('10-K','10-K/A'):
            rows.append((r['reportDate'][i], r['form'][i], r['filingDate'][i], r['accessionNumber'][i], r['primaryDocument'][i], cik))
rows.sort()
with open('annual_list.txt','w') as fo:
    for x in rows: fo.write(' '.join(x)+'\n')
for rep, form, fd, acc, doc, cik in rows:
    if form!='10-K': continue
    out=f'cache/k{rep[:4]}.txt'
    if os.path.exists(out): continue
    a=acc.replace('-','')
    b=get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, acc, os.path.getsize(out))

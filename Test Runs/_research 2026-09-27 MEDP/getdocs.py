import json, os, sys
from fetch import get, strip
r=json.load(open('allfilings.json'))
CIK='1668397'
want=[]
for x in r:
    d,f,it,acc,doc=x
    if f in ('10-K','10-Q','DEF 14A','424B4') or (f=='8-K' and d>='2025-01-01') or f in ('SC TO-T/A','SC 14D9'):
        want.append(x)
for d,f,it,acc,doc in want:
    out='filings/%s_%s_%s.txt'%(d,f.replace(' ','').replace('/',''),acc)
    if os.path.exists(out): continue
    url='https://www.sec.gov/Archives/edgar/data/%s/%s/%s'%(CIK,acc.replace('-',''),doc)
    try:
        b=get(url); open(out,'w',encoding='utf-8').write(strip(b)); print(out,len(b))
    except SystemExit as e: print('FAIL',out)

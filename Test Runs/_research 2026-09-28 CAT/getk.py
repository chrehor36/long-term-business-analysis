import os, time, sys
sys.path.insert(0,'.')
from fetch import get, strip
for line in open('k_list.txt'):
    p=line.split()
    if len(p)<5 or p[2] not in ('10-K','10-K405'): continue
    fy=int(p[1][:4])-1
    if fy<2000: continue
    acc,doc=p[3],p[4]
    fn=f'cache/k_{fy}.txt'
    if os.path.exists(fn): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/18230/{acc.replace("-","")}/{doc}')
    open(fn,'w',encoding='utf-8').write(strip(b)); print(fy, acc, os.path.getsize(fn)); time.sleep(0.3)

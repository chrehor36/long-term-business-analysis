import json,os,time
from fetch import get, strip
rows=json.load(open('tenk_list.json'))
for rd,fd,acc,doc in rows:
    y=rd[:4]
    if int(y)<2000 or int(y)>2024: continue
    out=f'tenk_{y}.txt'
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/100885/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.3)

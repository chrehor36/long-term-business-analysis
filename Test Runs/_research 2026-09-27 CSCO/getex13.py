import json, os, time
from fetch import get, strip
CIK='858877'
rows=json.load(open('allfilings.json'))
for d,f,it,acc,doc in rows:
    if not f.startswith('10-K') or not ('2003-01-01'<=d<'2011-01-01'): continue
    ix=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/index.json'))
    for itm in ix['directory']['item']:
        n=itm['name']
        if 'ex13' in n.lower().replace('-','').replace('_','') or 'dex13' in n.lower():
            o=f'filings/{d}_10-K_{acc}_{n}.txt'
            if os.path.exists(o): continue
            b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{n}')
            open(o,'w',encoding='utf-8').write(strip(b)); print(o, os.path.getsize(o)); time.sleep(0.15)

import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
L=[]
for fn in ['submissions.json','sub001.json']:
    d=json.load(open(fn)); r=d['filings']['recent'] if 'filings' in d else d
    for i in range(len(r['form'])):
        if r['form'][i]=='10-K':
            L.append((r['reportDate'][i],r['accessionNumber'][i],r['primaryDocument'][i]))
for rd,acc,doc in sorted(L):
    fy=int(rd[:4])
    fn=f'10-K_FY{fy}.txt'
    if os.path.exists(fn): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/1477294/{acc.replace("-","")}/{doc}')
    open(fn,'w',encoding='utf-8').write(strip(b)); print(fn,acc,os.path.getsize(fn)); time.sleep(0.3)
b=get('https://www.sec.gov/Archives/edgar/data/1477294/000119312510053804/d424b4.htm')
open('424B4_2010-03_prospectus-10-K.txt','w',encoding='utf-8').write(strip(b)); print('424b4')

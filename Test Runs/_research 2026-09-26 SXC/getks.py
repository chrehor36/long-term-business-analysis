import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
L=[]
for fn in ['submissions.json','sub001.json']:
    d=json.load(open(fn)); r=d['filings']['recent'] if 'filings' in d else d
    for i in range(len(r['form'])):
        if r['form'][i] in ('10-K','10-K/A') and r['primaryDocument'][i]:
            L.append((r['reportDate'][i],r['form'][i],r['accessionNumber'][i],r['primaryDocument'][i]))
for rd,form,acc,doc in sorted(L):
    fy=int(rd[:4])
    if fy>2024: continue
    fn=f'tenk_FY{fy}{"_A" if form=="10-K/A" else ""}.txt'
    if os.path.exists(fn): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/1514705/{acc.replace("-","")}/{doc}')
    open(fn,'w',encoding='utf-8').write(strip(b)); print(fn,acc,os.path.getsize(fn)); time.sleep(0.3)

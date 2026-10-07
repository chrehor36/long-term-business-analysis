import sys,os,time,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='1383312'
L=[]
for fn in ('submissions.json','submissions001.json'):
    s=json.load(open(fn)); r=s['filings']['recent'] if 'filings' in s else s
    for i,f in enumerate(r['form']):
        if f in ('10-K','10-K/A'):
            y=r['reportDate'][i][:4]; out=('tenk_' if f=='10-K' else 'tenka_')+y+'.txt'
            L.append((r['accessionNumber'][i],r['primaryDocument'][i],out))
for acc,doc,out in L:
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.3)

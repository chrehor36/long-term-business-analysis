import sys,os,time,json,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='779152'
s=json.load(open('submissions.json'))['filings']['recent']
want=[]
for i in range(len(s['form'])):
    f=s['form'][i]; d=s['filingDate'][i]
    if (f in ('8-K','8-K/A') and d>='2024-06-01') or (f in ('10-K','10-Q') and d>='2024-08-01') or (f=='DEF 14A' and d>='2025-01-01'):
        want.append((d,f,s['accessionNumber'][i],s['primaryDocument'][i]))
os.makedirs('filings',exist_ok=True)
for d,f,acc,doc in want:
    a=acc.replace('-','')
    try:
        idx=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json'))
    except SystemExit: continue
    for it in idx['directory']['item']:
        n=it['name']
        if not n.lower().endswith(('.htm','.html')) or n.startswith(acc) : continue
        if f.startswith('8-K') or n==doc:
            out=f'filings/{d}_{f.replace("/","")}_{n}.txt'
            if os.path.exists(out): continue
            b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{n}')
            open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.25)

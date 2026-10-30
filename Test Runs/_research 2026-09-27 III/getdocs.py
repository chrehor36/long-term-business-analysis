import sys,os,time,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='1371489'
s=json.load(open('submissions.json'))['filings']['recent']
os.makedirs('filings',exist_ok=True)
for i in range(len(s['form'])):
    f=s['form'][i]; d=s['filingDate'][i]; it=s['items'][i]
    ok = f in ('10-K','10-K/A','10-Q/A') or (f=='10-Q' and d>='2025-01-01') or (f=='DEF 14A' and d>='2024-01-01') \
         or (f in ('8-K','8-K/A') and (d>='2024-01-01' or any(x in it for x in ('1.01','2.01','8.01','3.02')) and d>='2016-01-01')) or f=='SC TO-I'
    if not ok: continue
    acc=s['accessionNumber'][i]; doc=s['primaryDocument'][i]
    tag=f.replace(' ','').replace('/','')
    out=f'filings/{d}_{tag}_{acc}.txt'
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.2)
    if f in ('8-K','8-K/A'):
        try:
            ix=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/index.json'))
            for itm in ix['directory']['item']:
                n=itm['name']
                if n.lower().endswith(('.htm','.html')) and n!=doc and 'ex' in n.lower():
                    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{n}')
                    o2=f'filings/{d}_{tag}_{acc}_{n}.txt'
                    open(o2,'w',encoding='utf-8').write(strip(b)); print(o2, os.path.getsize(o2)); time.sleep(0.2)
        except Exception as e: print('ix fail',acc,e)

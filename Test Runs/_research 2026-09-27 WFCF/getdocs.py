import sys,os,time,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='1360565'
s=json.load(open('submissions.json'))['filings']['recent']
os.makedirs('filings',exist_ok=True)
want=('10-K','10-K/A','10-Q/A','S-3','S-3/A','DEF 14A','8-K','8-K/A','10-Q')
for i in range(len(s['form'])):
    f=s['form'][i]; d=s['filingDate'][i]
    if f not in want: continue
    if f in ('8-K','8-K/A','10-Q','DEF 14A','S-3','S-3/A','10-Q/A') and d<'2024-01-01': continue
    acc=s['accessionNumber'][i]; doc=s['primaryDocument'][i]
    tag=f.replace(' ','').replace('/','')
    out=f'filings/{d}_{tag}_{acc}.txt'
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.25)
    if f in ('8-K','8-K/A'):
        # index for exhibits
        try:
            ix=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/index.json'))
            for it in ix['directory']['item']:
                n=it['name']
                if n.lower().endswith(('.htm','.html')) and n!=doc and 'ex' in n.lower():
                    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{n}')
                    o2=f'filings/{d}_{tag}_{acc}_{n}.txt'
                    open(o2,'w',encoding='utf-8').write(strip(b)); print(o2, os.path.getsize(o2)); time.sleep(0.25)
        except Exception as e: print('ix fail',acc,e)

import sys,os,time,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='779152'
L=[]
s=json.load(open('submissions.json'))['filings']['recent']
for i in range(len(s['form'])):
    if s['form'][i] in ('10-K',) and s['filingDate'][i]<'2026-01-01':
        L.append((s['reportDate'][i][:4], s['accessionNumber'][i], s['primaryDocument'][i]))
o=json.load(open('submissions001.json'))
for i in range(len(o['form'])):
    if o['form'][i] in ('10-K','10-K405') and o['filingDate'][i]>='2000-01-01':
        L.append((o['reportDate'][i][:4], o['accessionNumber'][i], o['primaryDocument'][i]))
os.makedirs('tenk',exist_ok=True)
for fy,acc,doc in sorted(L):
    out=f'tenk/tenk_{fy}.txt'
    if os.path.exists(out): continue
    if fy<'2004' or not doc:
        b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc}.txt')
    else:
        b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, acc, doc, os.path.getsize(out)); time.sleep(0.3)

import json,os,time,sys
sys.path.insert(0,'.')
from fetch import get
from fetch2 import strip2
CIK='1027838'
s=json.load(open('cache/submissions.json'))['filings']['recent']
for i,f in enumerate(s['form']):
    acc,doc,rd,fd=s['accessionNumber'][i],s['primaryDocument'][i],s['reportDate'][i],s['filingDate'][i]
    out=None
    if f=='10-K': out=f'cache/K2_{rd}.txt'
    elif f=='10-Q' and fd>='2025-01-01': out=f'cache/Q2_{rd}.txt'
    elif f=='DEF 14A' and fd>='2025-01-01': out=f'cache/P2_{fd}.txt'
    if out and not os.path.exists(out):
        b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
        open(out,'w',encoding='utf-8').write(strip2(b)); time.sleep(0.25); print(out)

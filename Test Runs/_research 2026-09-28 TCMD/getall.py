import json, os, time, sys, re
sys.path.insert(0,'.')
from fetch import get, strip
CIK='1027838'
s=json.load(open('cache/submissions.json'))['filings']['recent']
def fetchdoc(acc,doc,out):
    if os.path.exists(out): return
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); time.sleep(0.25)
def exhibits(acc,prefix,pat=r'ex99'):
    a=acc.replace('-','')
    idx=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json'))
    for it in idx['directory']['item']:
        n=it['name']
        if re.search(pat,n,re.I) and re.search(r'\.htm',n,re.I):
            fetchdoc(acc,n,f'cache/{prefix}_{n[:40]}.txt')
    time.sleep(0.2)
for i,f in enumerate(s['form']):
    acc,doc,rd,fd,items=s['accessionNumber'][i],s['primaryDocument'][i],s['reportDate'][i],s['filingDate'][i],s['items'][i]
    if f=='10-K': fetchdoc(acc,doc,f'cache/k_{rd}.txt'); print('K',rd,acc)
    elif f=='10-Q' and fd>='2025-01-01': fetchdoc(acc,doc,f'cache/q_{rd}.txt'); print('Q',rd,acc)
    elif f=='DEF 14A' and fd>='2023-01-01': fetchdoc(acc,doc,f'cache/proxy_{fd}.txt'); print('P',fd,acc)
    elif f=='8-K':
        if fd>='2016-01-01' and items.strip()!='5.07':
            fetchdoc(acc,doc,f'cache/e_{fd}_{acc[-6:]}.txt')
            if '9.01' in items and ('2.02' in items or '7.01' in items or '8.01' in items or '1.01' in items):
                try: exhibits(acc,f'x_{fd}_{acc[-6:]}')
                except SystemExit as e: print('exh fail',acc)
            print('8K',fd,items,acc)

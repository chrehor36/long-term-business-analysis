import json, os, re
from fetch import get, strip
r=json.load(open('allfilings.json'))
CIK='1701758'
def save(d,f,acc,doc,tag=''):
    out='filings/%s_%s_%s%s.txt'%(d,f.replace(' ','').replace('/',''),acc,tag)
    if os.path.exists(out): return
    url='https://www.sec.gov/Archives/edgar/data/%s/%s/%s'%(CIK,acc.replace('-',''),doc)
    try:
        b=get(url); open(out,'w',encoding='utf-8').write(strip(b)); print(out,len(b))
    except SystemExit as e: print('FAIL',out)
def exhibits(d,f,acc,doc):
    try:
        idx=json.loads(get('https://www.sec.gov/Archives/edgar/data/%s/%s/index.json'%(CIK,acc.replace('-',''))))
        for it2 in idx['directory']['item']:
            n=it2['name']
            if re.search(r'\.htm$',n,re.I) and n!=doc and 'index' not in n.lower():
                save(d,f,acc,n,'_'+n.replace('.htm',''))
    except SystemExit: print('idx fail',acc)
for d,f,it,acc,doc in r:
    if f in ('10-K','10-K/A','10-Q/A','NT 10-Q','NT 10-K','SC 13D','SC 13D/A','DEF 14A'): save(d,f,acc,doc)
    elif f=='10-Q' and d>='2025-01-01': save(d,f,acc,doc)
    elif f in ('S-1','424B4','424B1') and d<'2019-01-01' and f!='S-1': save(d,f,acc,doc)
    elif f in ('8-K','8-K/A'):
        if d>='2023-01-01' or re.search(r'1\.01|2\.01|4\.0|5\.02|8\.01',it):
            save(d,f,acc,doc); exhibits(d,f,acc,doc)
        elif '2.02' in it and d>='2019-01-01':
            save(d,f,acc,doc); exhibits(d,f,acc,doc)

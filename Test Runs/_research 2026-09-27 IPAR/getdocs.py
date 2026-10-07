import json, os, re
from fetch import get, strip
r=json.load(open('allfilings.json'))
CIK='822663'
def save(d,f,acc,doc,tag=''):
    out='filings/%s_%s_%s%s.txt'%(d,f.replace(' ','').replace('/',''),acc,tag)
    if os.path.exists(out): return
    url='https://www.sec.gov/Archives/edgar/data/%s/%s/%s'%(CIK,acc.replace('-',''),doc)
    try:
        b=get(url); open(out,'w',encoding='utf-8').write(strip(b)); print(out,len(b))
    except SystemExit as e: print('FAIL',out)
dp=[x for x in r if x[1]=='DEF 14A']
for d,f,it,acc,doc in r:
    if f in ('10-K','10-K/A') and d>='2005-01-01': save(d,f,acc,doc)
    elif f in ('10-Q','10-Q/A') and d>='2025-04-01': save(d,f,acc,doc)
    elif f=='DEF 14A' and d>='2024-01-01': save(d,f,acc,doc)
    elif f in ('8-K','8-K/A') and d>='2024-01-01':
        save(d,f,acc,doc)
        try:
            idx=json.loads(get('https://www.sec.gov/Archives/edgar/data/%s/%s/index.json'%(CIK,acc.replace('-',''))))
            for it2 in idx['directory']['item']:
                n=it2['name']
                if re.search(r'(ex|99|10)[^/]*\.htm$',n,re.I) and n!=doc:
                    save(d,f,acc,n,'_'+n.replace('.htm',''))
        except SystemExit: print('idx fail',acc)

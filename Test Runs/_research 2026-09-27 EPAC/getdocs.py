import json, os, re, sys
from fetch import get, strip
r=json.load(open('allfilings.json'))
CIK='6955'
def save(d,f,acc,doc,tag=''):
    out='filings/%s_%s_%s%s.txt'%(d,f.replace(' ','').replace('/',''),acc,tag)
    if os.path.exists(out) or not doc: return
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
mode=sys.argv[1] if len(sys.argv)>1 else 'core'
for d,f,it,acc,doc in r:
    if mode=='core':
        if f in ('10-K','10-K/A') and d>='2012-01-01': save(d,f,acc,doc)
        elif f=='10-Q' and d>='2025-09-01': save(d,f,acc,doc)
        elif f=='DEF 14A' and d>='2024-01-01': save(d,f,acc,doc)
        elif f in ('8-K','8-K/A') and d>='2019-01-01' and re.search(r'1\.01|2\.01|2\.05|2\.06|4\.0|8\.01',it):
            save(d,f,acc,doc); exhibits(d,f,acc,doc)
        elif f in ('8-K',) and d>='2025-06-01' and ('2.02' in it or '5.02' in it):
            save(d,f,acc,doc); exhibits(d,f,acc,doc)
    elif mode=='old10k':
        if f in ('10-K','10-K405','10-K/A') and d<'2012-01-01' and d>='2000-01-01': save(d,f,acc,doc)
    elif mode=='rel':
        if f=='8-K' and '2.02' in it and d>='2019-01-01': save(d,f,acc,doc); exhibits(d,f,acc,doc)

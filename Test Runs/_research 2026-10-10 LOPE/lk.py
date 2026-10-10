import csv,sys,re
R={r['﻿id'] if '﻿id' in r else r['id']:r for r in csv.DictReader(open('../../principle_ledger_v5.csv',encoding='utf-8'))}
a=sys.argv[1:]
if a and a[0]=='-s':
    pat=re.compile(a[1],re.I)
    for k,r in R.items():
        if pat.search(r['quote_verbatim']): print(k,'|',r['quote_verbatim'][:300].replace('\n',' '))
else:
    for k in a: print(k,'|',R.get(k,{}).get('quote_verbatim','MISSING'),'\n')

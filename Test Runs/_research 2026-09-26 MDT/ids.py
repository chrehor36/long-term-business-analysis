import csv,sys,re
sys.stdout.reconfigure(encoding='utf-8')
rows={r['﻿id']:r for r in csv.DictReader(open('principle_ledger.csv',encoding='utf-8'))}
if sys.argv[1]=='grep':
    pat=re.compile(sys.argv[2],re.I)
    for k,r in rows.items():
        if pat.search(r['quote_verbatim']): print(k,r['year'],'|',r['quote_verbatim'][:int(sys.argv[3]) if len(sys.argv)>3 else 300]);print()
elif sys.argv[1]=='file':
    txt=open(sys.argv[2],encoding='utf-8').read()
    ids=sorted(set(re.findall(r'E\d-\d+',txt)))
    print('ids cited',len(ids)); print('MISSING',[i for i in ids if i not in rows])
else:
    for i in sys.argv[1:]:
        r=rows.get(i); print(i, (r['year']+' | '+r['quote_verbatim'][:700]) if r else 'MISSING'); print()

import csv,re,sys
import sys as _s; _s.stdout.reconfigure(encoding="utf-8")
rows=list(csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig')))
if sys.argv[1]=='id':
    for i in sys.argv[2:]:
        for r in rows:
            if r['id']==i: print(i,'|',r['year'],'|',r['quote_verbatim'],'\n')
else:
    pat=re.compile(sys.argv[2],re.I)
    for r in rows:
        if pat.search(r['quote_verbatim']): print(r['id'],'|',r['quote_verbatim'][:int(sys.argv[3]) if len(sys.argv)>3 else 300].replace('\n',' '))

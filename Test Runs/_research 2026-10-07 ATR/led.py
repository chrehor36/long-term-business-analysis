import csv,sys,re
rows=list(csv.DictReader(open('C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv',encoding='utf-8-sig')))
mode=sys.argv[1]
if mode=='id':
    for i in sys.argv[2:]:
        for r in rows:
            if r['id']==i: print(i,'|',r['quote_verbatim'][:900]); print()
else:
    pat=re.compile(sys.argv[2],re.I)
    for r in rows:
        if pat.search(r['quote_verbatim']): print(r['id'],'|',r['quote_verbatim'][:300].replace('\n',' '))

import csv,sys,re
R={r['\ufeffid']:r for r in csv.DictReader(open(r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv',encoding='utf-8'))}
mode=sys.argv[1]
if mode=='id':
    for i in sys.argv[2:]: print(i,'|',R[i]['quote_verbatim'] if i in R else 'MISSING'); print()
else:
    pat=re.compile(sys.argv[2],re.I)
    for i,r in R.items():
        if pat.search(r['quote_verbatim']): print(i,'|',r['quote_verbatim'][:400].replace('\n',' ')); print()

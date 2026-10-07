import csv,sys,re
rows={r['\ufeffid']:r for r in csv.DictReader(open(r'C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv',encoding='utf-8'))}
args=sys.argv[1:]
if args and args[0]=='-s':
    pat=re.compile(args[1],re.I)
    for k,r in rows.items():
        if pat.search(r['quote_verbatim']): print(k,'|',r['quote_verbatim'][:400].replace('\n',' '),'\n')
else:
    for a in args:
        r=rows.get(a); print(a,'|',r['quote_verbatim'] if r else 'MISSING','\n')

import csv,sys
rows=list(csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig')))
for kw in sys.argv[1:]:
    hits=[r for r in rows if kw.lower() in r['quote_verbatim'].lower()]
    print('==',kw,len(hits))
    for r in hits[:60]:
        print(r['id'],'|',r['quote_verbatim'][:400].replace('\n',' '))

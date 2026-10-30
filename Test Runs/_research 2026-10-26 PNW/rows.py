import csv,sys
rows={r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    r=rows.get(i)
    if not r: print(i,'MISSING'); continue
    print(i,r['year'],'|',r['quote_verbatim'].replace('\n',' '));print()

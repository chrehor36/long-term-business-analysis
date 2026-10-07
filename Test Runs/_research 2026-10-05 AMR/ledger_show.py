import csv,sys
rows={r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    r=rows.get(i)
    print('###',i, r['year'] if r else 'MISSING', r['source_file'] if r else '')
    if r: print(r['quote_verbatim']); print()

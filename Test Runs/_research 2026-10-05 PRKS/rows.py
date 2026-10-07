import csv,sys
ids=sys.argv[1:]
rows={r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
for i in ids:
    r=rows.get(i); print('=====',i, 'MISSING' if not r else (r['year'],r['speaker']))
    if r: print(r['quote_verbatim'])

import csv,sys
r={x['id']:x for x in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    x=r.get(i); print(i, 'MISSING' if not x else x['quote_verbatim'][:int(300)].replace('\n',' '))

import csv,sys
r={a['id']:a for a in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    a=r.get(i)
    print(i, '|', a['year'] if a else 'MISSING', '|', (a['quote_verbatim'] if a else ''))
    print()

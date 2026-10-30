import csv, sys
rows = {r['id']: r for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    print(i, '|', rows[i]['year'], '|', rows[i]['quote_verbatim'][:700]); print()

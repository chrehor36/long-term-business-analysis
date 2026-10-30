# print v5 ledger rows by id (utf-8), for quoting verbatim
import csv, sys
r = {x['id']: x for x in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    x = r.get(i)
    print(i, '::', x['year'] if x else '', '::', x['quote_verbatim'] if x else 'MISSING'); print()

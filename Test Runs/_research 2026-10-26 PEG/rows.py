import sys
import csv, sys
sys.stdout.reconfigure(encoding="utf-8")
r = list(csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig')))
ids = {x['id']: x for x in r}
for i in sys.argv[1:]:
    x = ids.get(i)
    print(i, '|', x['year'] if x else '', '|', x['quote_verbatim'][:900] if x else 'MISSING')
    print()

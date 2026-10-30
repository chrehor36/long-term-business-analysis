"""Print full rows of principle_ledger_v5.csv by id. Usage: ledger_show.py ID [ID ...]"""
import csv, sys
ids = set(sys.argv[1:])
with open('principle_ledger_v5.csv', encoding='utf-8-sig') as f:
    for x in csv.DictReader(f):
        if x['id'] in ids:
            print(x['id'], x['year'], x['source_file'], '|', x['quote_verbatim'], '\n')
            ids.discard(x['id'])
for i in ids:
    print('MISSING', i)

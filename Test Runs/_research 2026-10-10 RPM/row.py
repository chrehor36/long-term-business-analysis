"""Print the verbatim quote of v5 ledger rows. Usage: python row.py ID [ID ...]"""
import csv, sys, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'principle_ledger_v5.csv')
rows = {r['id']: r for r in csv.DictReader(open(p, encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print(f'[{i}]', r['quote_verbatim'] if r else 'MISSING')

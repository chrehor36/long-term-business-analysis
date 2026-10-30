"""Print v5 ledger rows by id (full quote). Usage: python -I led.py ID [ID ...]"""
import csv, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
rows = {r['id']: r for r in csv.DictReader(open(os.path.join(ROOT, 'principle_ledger_v5.csv'), encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print(i, '|', 'MISSING' if r is None else r['quote_verbatim'][:900], '\n')

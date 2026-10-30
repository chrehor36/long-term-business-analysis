"""Print full rows of principle_ledger_v5.csv by id. Usage: python ledger_show.py ID [ID ...]"""
import csv, sys, pathlib
root = pathlib.Path(__file__).resolve().parents[2]
rows = {r['id']: r for r in csv.DictReader(open(root / 'principle_ledger_v5.csv', encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    r = rows.get(i)
    if r is None:
        print(i, '-> MISSING')
    else:
        print(i, '->', r['speaker'], r['year'], r['source_file'])
        print(r['quote_verbatim'])
        print()

# Print v5 ledger rows by id, or search quote text (case-insensitive). Usage: python _row.py ID [ID...]  |  python _row.py -s "phrase"
import csv, sys, os
p = os.path.join(os.path.dirname(__file__), '..', '..', 'principle_ledger_v5.csv')
rows = list(csv.DictReader(open(p, encoding='utf-8-sig')))
if sys.argv[1] == '-s':
    q = sys.argv[2].lower()
    for r in rows:
        if q in r['quote_verbatim'].lower():
            print(r['id'], '|', r['quote_verbatim'][:300].replace('\n', ' '))
else:
    d = {r['id']: r for r in rows}
    for i in sys.argv[1:]:
        r = d.get(i)
        print(i, '=>', r['quote_verbatim'] if r else 'MISSING', '\n')

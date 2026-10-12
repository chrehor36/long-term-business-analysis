import csv, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
rows = {}
for r in csv.DictReader(open('../../principle_ledger_v5.csv', encoding='utf-8-sig')):
    rows[r['id']] = r
for i in sys.argv[1:]:
    r = rows.get(i)
    print(i, '|', r['quote_verbatim'] if r else 'MISSING'); print()

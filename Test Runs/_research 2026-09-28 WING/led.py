import csv, sys
sys.stdout.reconfigure(encoding='utf-8')
ids = sys.argv[1:]
rows = {}
for r in csv.DictReader(open('principle_ledger.csv', encoding='utf-8-sig')):
    rows[r['id']] = r
for i in ids:
    r = rows.get(i)
    print('\n', i, '|', (r['year'] + ' ' + r['source_file'][:50] + ' | ' + r['quote_verbatim'][:900]) if r else 'MISSING')

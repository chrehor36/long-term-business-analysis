import csv, sys
ids = sys.argv[2:]
rows = {r['\ufeffid']: r for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8'))}
with open(sys.argv[1], 'w', encoding='utf-8') as f:
    for i in ids:
        r = rows.get(i)
        f.write(f"{i} | {r['year'] if r else ''} | {(r['quote_verbatim'] if r else 'MISSING')}\n\n")

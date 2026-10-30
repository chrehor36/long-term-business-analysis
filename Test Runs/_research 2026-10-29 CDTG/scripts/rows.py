import csv, sys
ids = sys.argv[2:]
rows = {r['id']: r for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
with open(sys.argv[1], 'w', encoding='utf-8') as f:
    for i in ids:
        r = rows.get(i)
        f.write(i + ' || ' + (r['quote_verbatim'].replace('\n', ' ') if r else 'MISSING') + '\n\n')

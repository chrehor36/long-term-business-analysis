import csv, sys
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        rows[r['id']] = r
for i in sys.argv[1:]:
    r = rows.get(i)
    if not r: print(i, 'MISSING\n'); continue
    print(f"{i} [{r['speaker']}]: {r['quote_verbatim'][:900]}\n")

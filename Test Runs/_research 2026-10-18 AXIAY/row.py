import sys; sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import csv, sys
rows = {r['id'] if 'id' in r else list(r.values())[0]: r for r in csv.DictReader(open(r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv', encoding='utf-8'))}
for i in sys.argv[1:]:
    r = rows.get(i)
    if not r: print(i, 'MISSING'); continue
    q = [v for k, v in r.items() if k and 'quote' in k.lower()]
    print(i, '::', (q[0] if q else r)[:900]); print()

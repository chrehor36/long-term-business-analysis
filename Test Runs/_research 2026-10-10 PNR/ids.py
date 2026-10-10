"""Print v5 ledger rows for the given ids (lookup only)."""
import csv, sys
rows = {r['id']: r for r in csv.DictReader(open('C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv', encoding='utf-8-sig'))}
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
for i in sys.argv[1:]:
    r = rows.get(i)
    print(i, '::', (r['quote_verbatim'] if r else 'MISSING'))
    print()

import csv, sys
import io; sys_ = __import__("sys"); sys_.stdout.reconfigure(encoding="utf-8")
rows = {}
for r in csv.DictReader(open(r'C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv', encoding='utf-8-sig')):
    rows[r['id']] = r
for i in sys.argv[1:]:
    r = rows.get(i)
    if not r: print(i, 'MISSING'); continue
    print(i, r['year'], r['speaker'], '|', r['quote_verbatim'][:1500]); print()

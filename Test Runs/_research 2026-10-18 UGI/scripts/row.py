import sys
import csv, sys
sys.stdout.reconfigure(encoding="utf-8")
LEDGER = r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv"
rows = {list(r.values())[0]: r for r in csv.DictReader(open(LEDGER, encoding="utf-8"))}
for i in sys.argv[1:]:
    r = rows.get(i); print(i, "::", r["quote_verbatim"] if r else "MISSING"); print()

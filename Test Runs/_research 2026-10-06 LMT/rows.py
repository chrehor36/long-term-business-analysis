"""Print v5 ledger rows by id (quote truncated), and flag any id not found.
Usage: python -I rows.py ID [ID ...]   (run from the repository root or anywhere; finds the ledger by path)"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(HERE, "..", "..", "principle_ledger_v5.csv")
rows = {r["id"]: r for r in csv.DictReader(open(LEDGER, encoding="utf-8-sig"))}
for i in sys.argv[1:]:
    r = rows.get(i)
    if not r:
        print(f"MISSING {i}")
    else:
        print(f"{i} | {r['year']} | {r['quote_verbatim'][:260]}")

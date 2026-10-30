"""Print ledger rows by id. Usage: python -I rows.py <ledger.csv> ID [ID ...]"""
import csv, sys

rows = {r["id"]: r for r in csv.DictReader(open(sys.argv[1], encoding="utf-8-sig"))}
for i in sys.argv[2:]:
    r = rows.get(i)
    print(i, "MISSING" if r is None else f"({r['year']}) {r['quote_verbatim']}")
    print()

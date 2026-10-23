"""Print ledger rows' verbatim quotes for the given ids. Usage: python -X utf8 dumprows.py ID..."""
import csv, sys
rows = {}
with open("principle_ledger_v5.csv", encoding="utf-8") as f:
    r = csv.reader(f); next(r)
    for row in r: rows[row[0]] = row
for i in sys.argv[1:]:
    print(i, "||", rows[i][2].replace("\n", " ") if i in rows else "MISSING")
    print()

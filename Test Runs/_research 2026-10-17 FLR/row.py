"""Print ledger rows by id. Usage: row.py ID [ID...]"""
import csv, sys, os
sys.stdout.reconfigure(encoding="utf-8")
root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
rows = {r["id"]: r for r in csv.DictReader(open(os.path.join(root, "principle_ledger_v5.csv"), encoding="utf-8-sig"))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print(i, "::", "MISSING" if r is None else r["quote_verbatim"] + "  [" + r["source_file"] + "]")

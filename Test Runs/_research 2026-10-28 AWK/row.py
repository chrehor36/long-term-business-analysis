"""Print v5 ledger rows by id.  Usage: python -I row.py ID [ID ...]"""
import csv, sys, os
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
rows = {r[0]: r for r in csv.reader(open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8-sig"))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print(f"== {i}: " + ("MISSING" if r is None else r[2]))

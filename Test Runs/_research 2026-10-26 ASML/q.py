"""Print the verbatim quote of each ledger id given (v5 ledger). Usage: python -I q.py ID [ID ...]"""
import csv, os, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
rows = {r["﻿id"] if "﻿id" in r else r["id"]: r for r in csv.DictReader(open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8"))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print("==", i, "" if r else "MISSING")
    if r:
        print(r["quote_verbatim"]); print()

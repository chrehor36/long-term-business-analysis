import csv, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
rows = {r["﻿id"]: r for r in csv.DictReader(open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8"))}
for i in sys.argv[1:]:
    r = rows.get(i); print(i, "=>", r["quote_verbatim"] if r else "MISSING"); print()

"""Print v5 ledger rows for the ids given. Usage: rows.py ID [ID ...]"""
import csv, sys, os
here = os.path.dirname(os.path.abspath(__file__))
led = os.path.join(here, "..", "..", "..", "principle_ledger_v5.csv")
rows = {r["﻿id"]: r for r in csv.DictReader(open(led, encoding="utf-8"))}
out = []
for i in sys.argv[1:]:
    r = rows.get(i)
    out.append(f"== {i}: " + (r["quote_verbatim"] if r else "MISSING"))
open(os.path.join(here, "..", "rows_out.txt"), "w", encoding="utf-8").write("\n".join(out))

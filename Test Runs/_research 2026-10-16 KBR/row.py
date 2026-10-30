import csv, sys, os
sys_ = __import__("sys"); sys_.stdout.reconfigure(encoding="utf-8")
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "principle_ledger_v5.csv")
rows = {r[0]: r for r in csv.reader(open(p, encoding="utf-8"))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print(i, "::", r[3] if r else "MISSING", "\n   ", (r[2] if r else "")[:900], "\n")

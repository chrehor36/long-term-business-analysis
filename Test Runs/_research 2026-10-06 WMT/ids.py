"""Look up v5 ledger ids: python ids.py ID [ID ...]  -> prints FOUND/MISSING and the quote (truncated).
With --check <runfile>: every bold [M/L/R....] id in the run file must exist in principle_ledger_v5.csv."""
import csv, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
rows = {}
with open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8") as f:
    r = csv.reader(f)
    head = next(r)
    for row in r:
        rows[row[0]] = row
qi = next((i for i, h in enumerate(head) if "quote" in h.lower()), 1)
args = sys.argv[1:]
if args and args[0] == "--check":
    text = open(args[1], encoding="utf-8").read()
    ids = sorted(set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)))
    missing = [i for i in ids if i not in rows]
    print(f"{len(ids)} ids cited; missing: {missing or 'none'}")
    sys.exit(1 if missing else 0)
for i in args:
    if i in rows:
        print(f"FOUND {i}: {rows[i][qi][:300]}")
    else:
        print(f"MISSING {i}")

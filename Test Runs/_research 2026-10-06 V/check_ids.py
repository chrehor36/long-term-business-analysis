"""Check that every bold ledger id in the run file exists in principle_ledger_v5.csv.
python check_ids.py [ID ...]  -- with ids, prints each row's quote (to read a row before citing it)."""
import csv, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
LEDGER = os.path.join(ROOT, "principle_ledger_v5.csv")
RUN = os.path.join(ROOT, "Test Runs", "2026-10-06 Run - V Visa.md")

rows = {}
with open(LEDGER, newline="") as f:
    r = csv.reader(f)
    head = next(r)
    for row in r:
        rows[row[0]] = row

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        row = rows.get(i)
        print(i, "MISSING" if row is None else "| ".join(row[1:4])[:900])
        print()
    sys.exit()

ids = re.findall(r"\[((?:M|L|R)\d{4}-\d{3})\]", open(RUN).read())
missing = sorted({i for i in ids if i not in rows})
print("ids cited:", len(set(ids)), "missing:", missing or "none")

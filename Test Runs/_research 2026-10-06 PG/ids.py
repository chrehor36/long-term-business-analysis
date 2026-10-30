"""Check v5 ledger ids. Usage: python ids.py [--file RUNFILE] [ID ...] [--show ID]
With --file, every **[X0000-000]** id in the file is checked against principle_ledger_v5.csv."""
import sys, csv, re, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
rows = {}
with open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8") as f:
    r = csv.reader(f)
    head = next(r)
    for row in r:
        rows[row[0]] = row

args = sys.argv[1:]
if args[:1] == ["--show"]:
    for i in args[1:]:
        row = rows.get(i)
        print(i, "MISSING" if row is None else dict(zip(head, row)))
        print()
    sys.exit()
ids = []
if args[:1] == ["--file"]:
    txt = open(args[1], encoding="utf-8").read()
    ids = sorted(set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", txt)))
    args = args[2:]
ids += args
missing = [i for i in ids if i not in rows]
print(len(ids), "ids checked;", "missing:", missing or "none")

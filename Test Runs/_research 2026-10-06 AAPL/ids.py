"""Print v5 ledger rows by id (or verify every bold id in the run file resolves).
Usage: python ids.py ID [ID ...]      -> prints each row's quote (truncated)
       python ids.py --check RUNFILE  -> lists bold [Xnnnn-nnn] ids in the file that are not in the ledger"""
import sys, csv, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
rows = {}
with open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8-sig") as f:
    r = csv.reader(f)
    head = next(r)
    for row in r:
        rows[row[0]] = row
if sys.argv[1] == "--check":
    txt = open(sys.argv[2], encoding="utf-8").read()
    ids = sorted(set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", txt)))
    missing = [i for i in ids if i not in rows]
    print(len(ids), "ids;", "missing:", missing)
else:
    qi = head.index("quote_verbatim")
    for i in sys.argv[1:]:
        row = rows.get(i)
        print(i, "MISSING" if row is None else row[qi][:400].replace("\n", " "))

"""Check every bold v5 id in the HON run file against principle_ledger_v5.csv. Prints missing ids.
Usage (from the repository root): python -I "Test Runs/_research 2026-10-06 HON/check_ids.py"
Optional: --show ID [ID ...] prints the quote of each id.
"""
import csv, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
LEDGER = os.path.join(ROOT, "principle_ledger_v5.csv")
RUN = os.path.join(ROOT, "Test Runs", "2026-10-06 Run - HON Honeywell.md")

rows = {}
with open(LEDGER, encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        rows[r["id"]] = r

if len(sys.argv) > 2 and sys.argv[1] == "--show":
    for i in sys.argv[2:]:
        r = rows.get(i)
        print(i, "MISSING" if r is None else r["quote_verbatim"][:700])
        print()
    sys.exit(0)

text = open(RUN, encoding="utf-8").read()
ids = sorted(set(re.findall(r"\[((?:M|L|R)\d{4}-\d{3})\]", text)))
bad = [i for i in ids if i not in rows]
other = sorted(set(re.findall(r"\[(E\d+-\d+)\]", text)))
print(f"{len(ids)} v5 ids cited; missing: {bad if bad else 'none'}; v4 E-ids: {other if other else 'none'}")

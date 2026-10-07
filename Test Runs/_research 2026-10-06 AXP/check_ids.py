"""Every [M|L|R....-...] id cited in the run file must exist in principle_ledger_v5.csv. Run from the repo root."""
import csv, re, sys
run = "Test Runs/2026-10-06 Run - AXP American Express.md"
ids = sorted(set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", open(run, encoding="utf-8").read())))
rows = {r["id"]: r for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
missing = [i for i in ids if i not in rows]
print(len(ids), "distinct ids cited;", "missing:", missing or "none")
if "-v" in sys.argv:
    for i in ids:
        if i in rows: print(i, rows[i]["year"], rows[i]["quote_verbatim"][:160].replace("\n", " "))

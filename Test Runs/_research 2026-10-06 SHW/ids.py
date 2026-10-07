"""Check every [M/L/R....-nnn] id in the run file exists in principle_ledger_v5.csv."""
import csv, re, sys, os
root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ids = set()
with open(os.path.join(root, "principle_ledger_v5.csv"), encoding="utf-8") as f:
    for r in csv.reader(f):
        if r:
            ids.add(r[0])
run = open(os.path.join(root, "Test Runs", "2026-10-06 Run - SHW Sherwin-Williams.md"), encoding="utf-8").read()
cited = sorted(set(re.findall(r"\b([MLR]\d{4}-\d{3})\b", run)))
missing = [c for c in cited if c not in ids]
print(f"cited {len(cited)}; missing {len(missing)}: {missing}")

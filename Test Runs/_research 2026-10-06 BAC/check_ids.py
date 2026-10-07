"""Check that every [id] cited in the BAC run file resolves to a row of principle_ledger_v5.csv.
Run from the repository root: python "Test Runs/_research 2026-10-06 BAC/check_ids.py"
"""
import csv
import re

RUN = "Test Runs/2026-10-06 Run - BAC Bank of America.md"
ids = set()
with open("principle_ledger_v5.csv", encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        ids.add(row["id"])
text = open(RUN, encoding="utf-8").read()
cited = sorted(set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)))
other = sorted(set(re.findall(r"\[(E\d+-\d+)\]", text)))
missing = [c for c in cited if c not in ids]
print("cited v5 ids:", len(cited))
print("missing:", missing or "none")
print("v4 (E-) ids cited:", other or "none")

# Every quoted fragment written immediately before an id must appear in that row's verbatim quote.
rows = {}
with open("principle_ledger_v5.csv", encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        rows[row["id"]] = row["quote_verbatim"]


def norm(s):
    return re.sub(r"\s+", " ", s.replace("[...]", " ")).strip()


bad = 0
checked = 0
for m in re.finditer(r'"([^"]{8,}?)"\s*\*\*\[([MLR]\d{4}-\d{3})\]', text):
    frag, rid = m.group(1), m.group(2)
    parts = [norm(p) for p in frag.split("[...]") if norm(p)]
    checked += 1
    if not all(p in norm(rows.get(rid, "")) for p in parts):
        bad += 1
        print("NOT IN ROW", rid, ":", frag[:120])
print("quoted fragments checked:", checked, "mismatches:", bad)

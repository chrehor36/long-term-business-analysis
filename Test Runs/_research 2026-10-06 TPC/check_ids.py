"""Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment immediately
before an id (in the same paragraph) appears verbatim in that row (split on [...])."""
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
run = open("Test Runs/2026-10-06 Run - TPC Tutor Perini.md", encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
bad = 0
e_ids = re.findall(r"\[E\d-\d+\]", run)
print("E-ids:", e_ids or "none")
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
print("ids cited:", len(ids), "distinct:", len(set(ids)))
for i in set(ids):
    if i not in rows: print("MISSING", i); bad += 1
# quoted fragments: for each id occurrence, take the text since the previous id (or line start) and find "..." quotes
for para in run.split("\n"):
    pos = 0
    for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", para):
        seg = para[pos:m.start()]; pos = m.end()
        quotes = re.findall(r"\"([^\"]{6,}?)\"", seg)
        if not quotes: continue
        q = quotes[-1]   # the quote nearest the id
        row = rows.get(m.group(1), "")
        parts = [p.strip(" .,;") for p in q.split("[...]") if p.strip(" .,;")]
        ok = all(p in row for p in parts)
        if not ok:
            bad += 1; print("NOT IN ROW", m.group(1), "|", q)
print("FAIL" if bad else "PASS", bad)

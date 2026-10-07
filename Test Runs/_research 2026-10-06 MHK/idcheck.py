# Checks the run file: no v4 E-ids; every M/L/R id exists in the v5 ledger; every quoted fragment in the same
# sentence-chunk as an id is found verbatim in that id's row (after [...] splits).
import csv, re, sys
run = open("Test Runs/2026-10-06 Run - MHK Mohawk Industries.md", encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
bad = 0
e = re.findall(r"\[E\d+-\d+\]", run)
if e: print("E-ids:", e); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING", i); bad += 1
# quote-to-id: a quote immediately followed (within 12 chars) by an id
norm = lambda s: re.sub(r"\s+", " ", s.replace("’","'").replace("‘","'").replace("“",'"').replace("”",'"')).strip()
for m in re.finditer(r"\"([^\"]{6,})\"\s*(?:\([^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run):
    q, i = m.group(1), m.group(2)
    row = norm(rows.get(i, ""))
    for part in q.split("[...]"):
        p = norm(part)
        if p and p not in row:
            print("NOT IN ROW", i, "|", p[:90]); bad += 1
print("ids:", len(set(ids)), "bad:", bad)

# Run-file check: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment next to an id is in that row.
import csv, re, sys, unicodedata
RUN = "Test Runs/2026-10-07 Run - ACNB ACNB Corporation.md"
rows = {r[0]: r[2] for r in csv.reader(open("principle_ledger_v5.csv", encoding="utf-8"))}
def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"').replace("\ufffd", "")
    s = re.sub(r"[^a-z0-9 ]", "", s.lower())
    return re.sub(r"\s+", " ", s).strip()
txt = open(RUN, encoding="utf-8").read()
bad = 0
if re.search(r"\[E\d-\d+\]", txt): print("E-id found"); bad += 1
ids = set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", txt))
for i in sorted(ids):
    if i not in rows: print("MISSING", i); bad += 1
# fragments: a quoted string followed within 12 chars by **[ID]**
for m in re.finditer(r'"([^"]{6,400})"[^"\[]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', txt):
    frag, i = m.group(1), m.group(2)
    if i in rows:
        parts = [p for p in frag.split("[...]") if p.strip()]
        for p in parts:
            if norm(p) not in norm(rows[i]):
                print("FRAGMENT NOT IN ROW", i, "::", p[:80]); bad += 1
print("ids:", len(ids), "problems:", bad)
sys.exit(1 if bad else 0)

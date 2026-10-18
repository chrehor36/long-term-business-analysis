# Checks the run file: no E-ids; every M/L/R id in the v5 ledger; every quoted fragment in the same bullet/paragraph
# as an id appears in at least one of the ids cited in that paragraph (fragments under 12 chars skipped).
import re, csv, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
run = open(ROOT + r"\Test Runs\2026-10-16 Run - SPNX Superior Energy Services.md", encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(ROOT + r"\principle_ledger_v5.csv", encoding="utf-8-sig"))}
bad = 0; CHECKED = []
if re.search(r"\[E\d-\d+\]", run): print("E-id found"); bad += 1
ids = set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", run))
for i in sorted(ids):
    if i not in rows: print("MISSING", i); bad += 1
norm = lambda s: re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip()
paras = re.split(r"\n(?=- |\n|\| )", run)
for p in paras:
    pid = re.findall(r"\[([MLR]\d{4}-\d{3})\]", p)
    if not pid: continue
    # quoted fragments immediately followed (within 12 chars) by an id
    for m in re.finditer(r"\"([^\"]{12,}?)\"[^\"\[]{0,12}\*\*\[([MLR]\d{4}-\d{3})\]", p):
        frag, idd = m.group(1), m.group(2); CHECKED.append(idd)
        parts = [x.strip() for x in frag.split("[...]") if x.strip()]
        if not all(norm(x) in norm(rows.get(idd, "")) for x in parts):
            print("NOT IN ROW", idd, "::", frag[:90]); bad += 1
print("fragments checked:", len(CHECKED)); print("ids:", len(ids), "->", "PASS" if not bad else f"FAIL ({bad})")

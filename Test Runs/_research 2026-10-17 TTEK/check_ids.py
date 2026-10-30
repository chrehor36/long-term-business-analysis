# Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately followed by a bold id is found in that row (elisions [...] split the fragment).
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
run = open(ROOT + r"\Test Runs\2026-10-17 Run - TTEK Tetra Tech.md", encoding="utf-8").read()
rows = {r["\ufeffid"]: r["quote_verbatim"] for r in csv.DictReader(open(ROOT + r"\principle_ledger_v5.csv", encoding="utf-8"))}
norm = lambda s: re.sub(r"\s+", " ", s).strip()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", run)
print("E-ids:", eids or "none"); bad += len(eids)
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", run)
missing = sorted({i for i in ids if i not in rows})
print("ids cited:", len(set(ids)), "missing:", missing or "none"); bad += len(missing)
# quoted fragment followed by **[ID]** (allow a closing paren/space between)
for m in re.finditer(r"\u201c?\"([^\"]{3,600})\"\s*\**\s*\[([MLR]\d{4}-\d{3})\]", run):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    row = norm(rows[i])
    for part in frag.split("[...]"):
        part = norm(part.strip(" ."))
        if part and part not in row:
            print("NOT IN ROW", i, "::", part[:120]); bad += 1
print("RESULT:", "PASS" if bad == 0 else f"FAIL ({bad})")

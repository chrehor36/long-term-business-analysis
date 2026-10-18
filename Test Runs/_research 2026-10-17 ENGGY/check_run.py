# Check script for the ENGGY run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately before an id (within the same sentence span) is in that row.
import csv, re, sys
RUN = "Test Runs/2026-10-17 Run - ENGGY Enagas.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()
flat = re.sub(r"\s*\n\s*", " ", text)
bad = 0
eids = re.findall(r"\[E\d-\d+\]", text)
if eids:
    print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING id", i); bad += 1
# quoted fragment directly followed (optionally with punctuation/words up to 3) by a bold id
pat = re.compile(r"[\"“]([^\"“”]{3,400}?)[\"”][^\"“”\[*]{0,60}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*")
n = 0
for frag, i in pat.findall(flat):
    n += 1
    row = re.sub(r"\s+", " ", rows.get(i, ""))
    parts = [p.strip(" .,;:") for p in frag.split("[...]")]
    for p in parts:
        if p and p not in row:
            print(f"FRAGMENT NOT IN {i}: {p!r}"); bad += 1
print(f"ids cited: {len(set(ids))}; quoted fragments checked: {n}; problems: {bad}")
sys.exit(1 if bad else 0)

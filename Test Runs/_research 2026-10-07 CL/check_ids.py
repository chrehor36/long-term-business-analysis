# CL run check: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment set just before an id
# (same sentence, no other quote between) is in that id's row, elisions [...] taken in order
import csv, re, sys
run = open("Test Runs/2026-10-07 Run - CL Colgate-Palmolive.md", encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}

def norm(s):
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("—", "-"), ("–", "-")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()

bad = 0
eids = re.findall(r"\[E\d+-\d+\]", run)
print("E-ids:", eids or "none"); bad += len(eids)
ids = sorted(set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", run)))
missing = [i for i in ids if i not in rows]
print(f"ids cited: {len(ids)}; missing from the v5 ledger: {missing or 'none'}"); bad += len(missing)

flat = re.sub(r"\n\s*", " ", run)
pat = re.compile(r'"([^"]{3,400})"((?:(?!\. )[^"\[]){0,160}?)\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
checked = 0
for m in pat.finditer(flat):
    frag, i = m.group(1), m.group(3)
    if i not in rows: continue
    q = norm(rows[i]); pos = 0; ok = True
    for piece in [p.strip(" .,;") for p in norm(frag).split("[...]") if p.strip(" .,;")]:
        k = q.find(piece, pos)
        if k < 0: ok = False; break
        pos = k + len(piece)
    checked += 1
    if not ok:
        bad += 1; print(f"NOT IN ROW {i}: \"{frag}\"")
print(f"quoted fragments checked against their rows: {checked}")
print("RESULT:", "PASS" if bad == 0 else f"FAIL ({bad})")
sys.exit(1 if bad else 0)

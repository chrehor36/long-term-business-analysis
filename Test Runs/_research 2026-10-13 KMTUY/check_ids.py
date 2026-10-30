"""Run-file check: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that sits
immediately before an id (or a run of ids) is found in at least one of those rows (elisions [...] split the fragment)."""
import csv, re, sys
RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-13 Run - KMTUY Komatsu.md"
LED = r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(LED, encoding="utf-8-sig", newline=""))}
text = open(RUN, encoding="utf-8").read()
bad = 0
for m in re.finditer(r"\bE\d-\d{2}\b", text):
    print("E-id found:", m.group(0)); bad += 1
ids = set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", text))
for i in sorted(ids):
    if i not in rows: print("MISSING id:", i); bad += 1
norm = lambda s: re.sub(r"\s+", " ", s).strip()
# a quote followed (within the same sentence-ish span) by one or more bold ids
for m in re.finditer(r'"([^"]{3,600})"[^"\n]{0,12}?((?:\s*,?\s*\*\*\[[MLR]\d{4}-\d{3}\]\*\*)+)', text):
    frag, idrun = m.group(1), m.group(2)
    cand = re.findall(r"[MLR]\d{4}-\d{3}", idrun)
    parts = [norm(p) for p in frag.split("[...]") if norm(p)]
    ok = any(all(p in norm(rows.get(c, "")) for p in parts) for c in cand)
    if not ok:
        print(f"NOT VERBATIM in {cand}: \"{frag[:120]}\""); bad += 1
print("checked", len(ids), "ids;", "FAIL" if bad else "PASS", bad)

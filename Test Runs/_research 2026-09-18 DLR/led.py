import csv, sys
sys.stdout.reconfigure(encoding="utf-8")
rows = list(csv.DictReader(open(r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger.csv", encoding="utf-8-sig")))
k = list(rows[0].keys())
for i in sys.argv[1:]:
    hit = [r for r in rows if r[k[0]] == i]
    if not hit: print(i, "MISSING"); continue
    r = hit[0]; print(i, "|", " | ".join((r[c] or "")[:260] for c in k[1:5])); print()

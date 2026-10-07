import csv, sys
sys.stdout.reconfigure(encoding="utf-8")
ids = sys.argv[1].split()
rows = {}
for r in csv.reader(open(r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger.csv", encoding="utf-8")):
    rows.setdefault(r[0], []).append(r)
for i in ids:
    L = rows.get(i)
    if not L: print("MISSING", i); continue
    print(f"{i} n={len(L)} {L[0][3]} | {L[0][2][:int(sys.argv[2]) if len(sys.argv)>2 else 200]}")

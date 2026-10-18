import csv, sys
sys.stdout.reconfigure(encoding="utf-8")
rows = {r[0]: r for r in csv.reader(open(r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv", encoding="utf-8"))}
hdr = next(csv.reader(open(r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv", encoding="utf-8")))
qi = 2
for i in sys.argv[1:]:
    r = rows.get(i)
    print(i, "|", r[qi] if r else "MISSING")
    print()

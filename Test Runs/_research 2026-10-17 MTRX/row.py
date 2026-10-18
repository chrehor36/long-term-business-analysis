import csv, sys
sys_ = __import__("sys"); sys_.stdout.reconfigure(encoding="utf-8")
rows = {r["id"]: r for r in csv.DictReader(open(r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv", encoding="utf-8-sig"))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print("==", i, "MISSING" if not r else r["year"] + " | " + r["source_file"])
    if r: print(r["quote_verbatim"]); print()

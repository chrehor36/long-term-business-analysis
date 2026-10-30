import csv,sys
ids=set(sys.argv[1:])
with open(r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv",encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        if r["id"] in ids: print(r["id"],"|",r["quote_verbatim"]); print()

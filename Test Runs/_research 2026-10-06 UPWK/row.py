import csv, sys
rows = {r[list(r.keys())[0]]: r for r in csv.DictReader(open(r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv", encoding="utf-8"))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print("==", i, "MISSING" if r is None else "")
    if r: print([v for k, v in r.items() if k.lower().startswith("quote") or k.lower()=="text" or "verbatim" in k.lower()] or r)

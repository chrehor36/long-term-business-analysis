"""Print ledger rows verbatim for ids given on the command line. Usage: python ledger.py E3-43 E2-44 ..."""
import csv, sys
P = r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger.csv"
rows = {r["\ufeffid"] if "\ufeffid" in r else r["id"]: r for r in csv.DictReader(open(P, encoding="utf-8"))}
for k in sys.argv[1:]:
    r = rows.get(k)
    if not r:
        print(k, "MISSING"); continue
    print(f"[{k}] {r['year']} | {r['source_file']} | {r['concept']}\n  {r['quote_verbatim']}\n")

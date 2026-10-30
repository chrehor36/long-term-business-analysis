import csv,sys
R={r['id']:r for r in csv.DictReader(open(r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv",encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    r=R.get(i); print(f"[{i}]", r['quote_verbatim'] if r else "MISSING"); print()

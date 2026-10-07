import csv, sys, re
L="C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv"
rows={r["id"]:r for r in csv.DictReader(open(L,encoding="utf-8-sig"))}
args=sys.argv[1:]
if args and args[0]=="-s":
    pat=re.compile(args[1],re.I)
    for k,r in rows.items():
        if pat.search(r["quote_verbatim"]): print(k,"|",r["quote_verbatim"][:300].replace("\n"," "))
else:
    for k in args:
        r=rows.get(k); print(k, (r["year"],r["source_file"]) if r else "MISSING"); print("   ",r["quote_verbatim"] if r else ""); print()

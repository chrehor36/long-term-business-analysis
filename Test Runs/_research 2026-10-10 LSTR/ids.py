import csv,sys,os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","..","principle_ledger_v5.csv")
rows={r["id"]:r for r in csv.DictReader(open(R,encoding="utf-8-sig"))}
for i in sys.argv[1:]:
    r=rows.get(i)
    print(i, "MISSING" if not r else r["quote_verbatim"][:700]); print()

import csv,sys
rows={r[0]:r for r in csv.reader(open("principle_ledger_v5.csv",encoding="utf-8"))}
for i in sys.argv[1:]:
    r=rows.get(i); print(i, "MISSING" if r is None else r[1:4]+[r[4][:700]]); print()

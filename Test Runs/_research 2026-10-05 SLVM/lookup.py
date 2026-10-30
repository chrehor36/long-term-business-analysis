import csv,sys
rows={r[0]:r for r in csv.reader(open(r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv",encoding="utf-8"))}
hdr=rows.get('id') or next(iter(rows.values()))
for i in sys.argv[1:]:
    r=rows.get(i)
    if not r: print(i,"MISSING"); continue
    # find longest field as quote
    q=r[2]
    print(f"{i} | {q[:700]}\n")

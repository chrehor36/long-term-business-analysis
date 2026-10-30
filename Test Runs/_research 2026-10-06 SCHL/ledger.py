import csv,sys,re,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
P="C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv"
rows=list(csv.reader(open(P,encoding="utf-8-sig")))
hdr=rows[0]; rows=rows[1:]
byid={r[0]:r for r in rows}
if sys.argv[1]=="id":
    for k in sys.argv[2:]:
        r=byid.get(k); print(k,"|",r[3] if r else "MISSING","|",r[2] if r else ""); print()
elif sys.argv[1]=="grep":
    pat=re.compile(sys.argv[2],re.I)
    for r in rows:
        if pat.search(r[2]): print(r[0],"|",r[2][:int(sys.argv[3]) if len(sys.argv)>3 else 400]); print()

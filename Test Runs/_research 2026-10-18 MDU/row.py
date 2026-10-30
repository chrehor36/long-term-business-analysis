import csv,sys
sys.stdout.reconfigure(encoding="utf-8")
rows={r[0].lstrip("\ufeff"):r for r in csv.reader(open(r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv",encoding="utf-8"))}
for i in sys.argv[1:]:
    r=rows.get(i); print("##",i, (r[3]+" "+r[4]) if r else "MISSING"); 
    if r: print(r[2]); print()

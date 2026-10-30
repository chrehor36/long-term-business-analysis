import csv,sys
R={r[0]:r for r in csv.reader(open('../../principle_ledger_v5.csv',encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    r=R.get(i)
    print(f"[{i}]", (r[2] if r else "MISSING"))
    print()

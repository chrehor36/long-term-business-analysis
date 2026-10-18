import csv,sys
rows={r[0]:r for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    r=rows.get(i); print(i,'MISSING' if not r else r[2]); print()

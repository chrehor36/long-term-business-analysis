import sys; sys.stdout.reconfigure(encoding="utf-8")
import csv,sys
rows={r[0]:r for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8'))}
for i in sys.argv[1:]:
    r=rows.get(i)
    print(i, '|', (r[2][:900] if r else 'MISSING'))

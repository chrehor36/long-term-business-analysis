import csv,sys
sys.stdout.reconfigure(encoding='utf-8')
ids=sys.argv[1:]
rows={}
with open('principle_ledger_v5.csv',encoding='utf-8') as f:
    r=csv.reader(f); h=next(r)
    for row in r: rows[row[0]]=row
for i in ids:
    if i not in rows: print("MISSING",i); continue
    print(i, '|', rows[i][2][:320].replace('\n',' '))

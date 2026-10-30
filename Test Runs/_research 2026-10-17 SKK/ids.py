import csv,sys
sys.stdout.reconfigure(encoding="utf-8")
rows={r[0]:r for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8'))}
for i in sys.argv[1:]:
    r=rows.get(i); print('==',i, 'MISSING' if not r else ''); 
    if r: print('   ', r[1:4], '\n   ', r[4][:900] if len(r)>4 else '')

import csv,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
R={r[0]:r for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
for i in sys.argv[1:]:
  r=R.get(i); print(i,'||',(r[2] if r else 'MISSING')); print()

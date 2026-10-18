import csv,sys
sys.stdout.reconfigure(encoding='utf-8')
R={r[0]:r for r in csv.reader(open(r'C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv',encoding='utf-8'))}
hdr=R.get('id') or next(iter(R.values()))
for i in sys.argv[1:]:
    r=R.get(i)
    print('==',i, (r[1:4] if r else 'MISSING'))
    if r: print(r[4] if len(r)>4 else r)

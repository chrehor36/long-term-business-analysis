import csv,sys
rows={r[0]:r for r in csv.reader(open(r'c:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv',encoding='utf-8'))}
hdr=rows.get('id')
for i in sys.argv[1:]:
    r=rows.get(i)
    print('##',i, 'MISSING' if not r else '')
    if r: print('  ', r[1:3], '|', r[3][:900])

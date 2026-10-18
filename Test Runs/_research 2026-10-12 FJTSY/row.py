import csv,sys
rows={r[0]:r for r in csv.reader(open(sys.argv[1],encoding='utf-8'))}
for i in sys.argv[2:]:
    r=rows.get(i)
    print('==',i, 'MISSING' if r is None else '')
    if r: print(r[1][:900]); print('   ', r[2:4])

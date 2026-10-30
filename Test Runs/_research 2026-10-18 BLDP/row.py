import csv,sys
rows={r[0]:r for r in csv.reader(open(sys.argv[1],encoding='utf-8'))}
hdr=None
for i in sys.argv[2:]:
    r=rows.get(i)
    print('==',i, 'MISSING' if r is None else '')
    if r: print(r[1] if len(r)>1 else '', '|', r[2][:1200] if len(r)>2 else '')

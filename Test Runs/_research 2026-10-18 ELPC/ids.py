import csv,sys
sys.stdout.reconfigure(encoding='utf-8')
rows={r['id']:r for r in csv.DictReader(open(sys.argv[1],encoding='utf-8-sig'))}
for i in sys.argv[2:]:
    r=rows.get(i)
    if not r: print(i,'MISSING'); continue
    q=['quote_verbatim']
    print(i, '|', r.get(q[0]) if q else r)
    print()

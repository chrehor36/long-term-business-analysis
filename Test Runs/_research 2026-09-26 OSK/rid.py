import csv,sys,re
rows={r[list(r.keys())[0]]:r for r in csv.DictReader(open('../../principle_ledger.csv',encoding='utf-8'))}
ids=sys.argv[1:] if len(sys.argv)>1 else sorted(set(re.findall(r'E\d-\d+',open('../2026-09-26 Run - OSK Oshkosh.md',encoding='utf-8').read())))
miss=[i for i in ids if i not in rows]
print(len(ids),'ids; missing:',miss)

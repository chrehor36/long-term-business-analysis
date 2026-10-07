import re,csv,sys
t=open('../2026-09-28 Run - NWPX NWPX Infrastructure.md',encoding='utf-8').read()
ids=sorted(set(re.findall(r'E\d-\d{2}',t)))
L={r[0]:r for r in csv.reader(open('../../principle_ledger.csv',encoding='utf-8-sig'))}
miss=[i for i in ids if i not in L]
print(len(ids),'ids; missing:',miss)
for i in sys.argv[1:]:
    print(i, L[i][3], L[i][2][:400]); print()

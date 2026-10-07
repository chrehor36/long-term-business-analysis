import re,csv
t=open('../2026-09-28 Run - TECH Bio-Techne.md',encoding='utf-8').read()
ids=sorted(set(re.findall(r'E\d-\d{2}',t)))
L={r[0] for r in csv.reader(open('../../principle_ledger.csv',encoding='utf-8-sig'))}
miss=[i for i in ids if i not in L]
print(len(ids),'ids; missing:',miss)

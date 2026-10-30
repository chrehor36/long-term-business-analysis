import re,csv
s=open('../2026-09-26 Run - SXC SunCoke Energy.md',encoding='utf-8').read()
ids=set(re.findall(r'\bE\d-\d{2}\b',s))
R={r[0] for r in csv.reader(open('../../principle_ledger.csv',encoding='utf-8'))}
miss=sorted(i for i in ids if i not in R)
print(len(ids),'ids cited; missing:',miss)
print(sorted(ids))

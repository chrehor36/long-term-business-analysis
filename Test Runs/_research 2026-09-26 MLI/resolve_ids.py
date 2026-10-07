import re,csv
t=open(r'C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-09-26 Run - MLI Mueller Industries.md',encoding='utf-8').read()
ids=set()
for grp in re.findall(r'\[(E\d-\d+(?:\s*,\s*E\d-\d+)*)\]',t):
    for i in re.split(r'\s*,\s*',grp): ids.add(i)
led={r[0] for r in csv.reader(open(r'C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger.csv',encoding='utf-8-sig'))}
miss=sorted(i for i in ids if i not in led)
print(len(ids),'distinct ids; missing:',miss)

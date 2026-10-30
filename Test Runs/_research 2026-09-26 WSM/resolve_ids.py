import csv,re,sys
ids={r[0].strip() for r in csv.reader(open('../../principle_ledger.csv',encoding='utf-8-sig'))}
t=open(sys.argv[1],encoding='utf-8').read()
found=set()
for m in re.finditer(r'\[([^\]]+)\]',t):
    for x in re.findall(r'E\d-\d+',m.group(1)): found.add(x)
miss=sorted(x for x in found if x not in ids)
print(len(found),'distinct ids; missing:',miss)

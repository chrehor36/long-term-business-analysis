import re,csv,sys
t=open(sys.argv[1],encoding='utf-8').read()
ids=set()
for grp in re.findall(r'\[((?:E\d-\d+[, ]*)+)\]',t):
    ids.update(re.findall(r'E\d-\d+',grp))
rows={r[0] for r in csv.reader(open('principle_ledger.csv',encoding='utf-8-sig'))}
miss=sorted(i for i in ids if i not in rows)
print(len(ids),'ids cited; missing:',miss)

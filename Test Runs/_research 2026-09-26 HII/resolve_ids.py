import re,csv,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
t=open('../2026-09-26 Run - HII Huntington Ingalls Industries.md',encoding='utf-8').read()
ids=sorted(set(re.findall(r'E\d-\d+',t)),key=lambda x:(x[1],int(x[3:])))
rows={list(r.values())[0] for r in csv.DictReader(open('../../principle_ledger.csv',encoding='utf-8-sig'))}
miss=[i for i in ids if i not in rows]
print(len(ids),'ids cited; missing:',miss); print(' '.join(ids))

import re,csv,sys
ids=set(r['id'] for r in csv.DictReader(open('principle_ledger.csv',encoding='utf-8-sig')))
s=open('Test Runs/2026-09-27 Run - III Information Services Group.md',encoding='utf-8').read()
cited=set(re.findall(r'E[1-5]-\d{2}',s))
print(len(cited),'cited;','missing:',sorted(c for c in cited if c not in ids))
print(' '.join(sorted(cited,key=lambda x:(x[1],int(x[3:])))))

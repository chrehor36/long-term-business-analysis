import re, csv
ids={r['id'] for r in csv.DictReader(open('../../principle_ledger.csv',encoding='utf-8-sig'))}
t=open('../2026-09-28 Run - MA Mastercard.md',encoding='utf-8').read()
cited=set(re.findall(r'E\d-\d+',t))
print('cited',len(cited),'missing',sorted(cited-ids))
print('em dash count outside quotes (rough):', t.count('—'))

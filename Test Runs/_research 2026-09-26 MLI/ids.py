import csv,sys
ids=sys.argv[1].split(',')
rows={}
with open(r'C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger.csv',encoding='utf-8') as f:
    r=csv.reader(f); h=next(r)
    for row in r: rows.setdefault(row[0],row)
for i in ids:
    row=rows.get(i)
    print(i, '|', (' | '.join(row[1:]))[:260] if row else 'MISSING')

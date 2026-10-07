import csv,sys,re
rows={r[0]:r for r in csv.reader(open(r'C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger.csv',encoding='utf-8'))}
for i in sys.argv[1:]:
    r=rows.get(i)
    print(i, '|', (' | '.join(r[1:])[:260] if r else 'MISSING'))

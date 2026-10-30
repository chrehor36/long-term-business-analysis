import csv,sys
r=list(csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig')))
d={x['id']:x for x in r}
for i in sys.argv[1:]:
    print(i, i in d, '::', (d[i]['quote_verbatim'][:400] if i in d else ''))

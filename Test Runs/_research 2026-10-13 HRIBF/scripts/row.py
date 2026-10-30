import csv, sys
L = "C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv"
R = {x['\ufeffid'] if '\ufeffid' in x else x['id']: x for x in csv.DictReader(open(L, encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    x = R.get(i)
    print(i, '->', 'MISSING' if not x else x['quote_verbatim'])
    print()

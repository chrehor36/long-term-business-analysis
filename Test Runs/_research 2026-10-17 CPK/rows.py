import csv, sys
rows = {r['id']: r for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
out = open(sys.argv[2], 'a', encoding='utf-8')
for i in sys.argv[1].split(','):
    r = rows.get(i)
    out.write(i + ' | ' + (r['quote_verbatim'] if r else 'MISSING') + '\n\n')

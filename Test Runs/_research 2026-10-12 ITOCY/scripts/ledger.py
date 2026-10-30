# usage: python ledger.py id1 id2 ...   or   python ledger.py -s "regex"
import csv, sys, re
rows = list(csv.DictReader(open(r'C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv', encoding='utf-8-sig')))
by = {r['id']: r for r in rows}
if sys.argv[1] == '-s':
    pat = re.compile(sys.argv[2], re.I)
    for r in rows:
        if pat.search(r['quote_verbatim']):
            print(r['id'], '|', r['quote_verbatim'][:600].encode('ascii', 'replace').decode()); print()
else:
    for i in sys.argv[1:]:
        r = by.get(i)
        print(i, '|', (r['quote_verbatim'].encode('ascii', 'replace').decode() if r else 'MISSING')); print()

import csv, re, sys
rows = list(csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig')))
pat = re.compile(sys.argv[1], re.I)
n = int(sys.argv[2]) if len(sys.argv) > 2 else 500
for r in rows:
    if pat.search(r['quote_verbatim']):
        print(r['id'], '|', r['quote_verbatim'][:n].replace('\n', ' '))
        print()

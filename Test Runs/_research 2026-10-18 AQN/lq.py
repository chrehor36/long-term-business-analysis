# ledger query: python lq.py PATTERN [maxchars]  -> id | year | quote (regex, case-insensitive)
import csv, re, sys
pat = re.compile(sys.argv[1], re.I)
n = int(sys.argv[2]) if len(sys.argv) > 2 else 400
with open('principle_ledger_v5.csv', encoding='utf-8-sig', newline='') as f:
    for r in csv.DictReader(f):
        if pat.search(r['quote_verbatim']):
            print(r['id'], '|', r['quote_verbatim'][:n].replace('\n', ' '))
            print()

"""Print v5 ledger rows by id, or search quotes by regex. Usage: row.py ID [ID...] | row.py -s REGEX"""
import csv, re, sys
ROOT = __file__.rsplit('Test Runs', 1)[0]
rows = list(csv.reader(open(ROOT + 'principle_ledger_v5.csv', encoding='utf-8')))
h = rows[0]
args = sys.argv[1:]
if args and args[0] == '-s':
    rx = re.compile(args[1], re.I)
    for r in rows[1:]:
        if rx.search(r[3] if len(r) > 3 else ''):
            print(r[0], '|', r[3][:300].replace('\n', ' '))
else:
    if not args:
        print(h)
    for r in rows[1:]:
        if r[0] in args:
            print(r[0], '|', ' | '.join(x[:1200] for x in r[1:]))
            print()

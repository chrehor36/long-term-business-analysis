import sys; sys.stdout.reconfigure(encoding="utf-8")
import csv, sys
rows = {r['id']: r for r in csv.DictReader(open(sys.argv[1], encoding='utf-8-sig'))}
for i in sys.argv[2:]:
    r = rows.get(i)
    print(i, '::', (r['quote_verbatim'] if r else 'MISSING'))
    print()

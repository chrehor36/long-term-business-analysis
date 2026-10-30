import sys
import csv,sys
sys.stdout.reconfigure(encoding="utf-8")
rows={r['id']:r for r in csv.DictReader(open('../../principle_ledger_v5.csv',encoding='utf-8-sig'))}
for i in sys.argv[1:]:
  r=rows.get(i); print(i, 'MISSING' if not r else r['quote_verbatim'].replace('\n',' ')); print()

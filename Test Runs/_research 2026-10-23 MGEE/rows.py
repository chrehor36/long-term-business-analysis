import sys; sys.stdout.reconfigure(encoding="utf-8")
import csv,sys
rows={r['id']:r for r in csv.DictReader(open(sys.argv[1],encoding='utf-8-sig'))}
for i in sys.argv[2:]:
  r=rows.get(i)
  print('##',i, 'MISSING' if not r else r['year']+' | '+r['quote_verbatim'][:600].replace('\n',' '))

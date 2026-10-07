import csv,sys
rows={r['﻿id'] if '﻿id' in r else r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8'))}
out=open(sys.argv[1],'w',encoding='utf-8')
for i in sys.argv[2:]:
    r=rows.get(i)
    out.write(f"{i} | {r['year'] if r else 'MISSING'} | {r['quote_verbatim'] if r else ''}\n\n")

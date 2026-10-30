import csv,sys
rows={r['﻿id'] if '﻿id' in r else r['id']:r for r in csv.DictReader(open(sys.argv[1],encoding='utf-8'))}
for i in sys.argv[2:]:
    r=rows.get(i)
    print(i,'|',(r['quote_verbatim'][:700].replace('\n',' ') if r else 'MISSING')); print()

import csv,sys
r={x['﻿id']:x for x in csv.DictReader(open(sys.argv[1],encoding='utf-8'))}
for i in sys.argv[2:]:
    x=r.get(i); print('==',i, x['year'] if x else 'MISSING'); 
    if x: print(x['quote_verbatim'])

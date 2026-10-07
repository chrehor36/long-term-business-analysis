import csv,sys
r={row['﻿id']:row for row in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8'))}
for i in sys.argv[1:]:
    if i in r: print(f"[{i}] ({r[i]['year']}) {r[i]['quote_verbatim'][:900]}\n")
    else: print(f"[{i}] MISSING\n")

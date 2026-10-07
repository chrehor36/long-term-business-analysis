import csv,sys
rows={r['﻿id'] if '﻿id' in r else r['id']:r for r in csv.DictReader(open("principle_ledger_v5.csv",encoding="utf-8-sig"))}
for i in sys.argv[1:]:
    r=rows.get(i)
    print(f"[{i}]", "MISSING" if r is None else r["quote_verbatim"][:700].replace("\n"," "))
    print()

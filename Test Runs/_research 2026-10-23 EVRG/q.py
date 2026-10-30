import sys; sys.stdout.reconfigure(encoding="utf-8")
import csv,sys
r=list(csv.DictReader(open("principle_ledger_v5.csv",encoding="utf-8-sig")))
d={x["id"]:x for x in r}
for i in sys.argv[1:]:
    x=d.get(i)
    print(i, "|", x["quote_verbatim"] if x else "MISSING"); print()

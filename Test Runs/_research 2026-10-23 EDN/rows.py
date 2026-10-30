import csv,sys
ids=set(sys.argv[1:])
for r in csv.DictReader(open("principle_ledger_v5.csv",encoding="utf-8-sig")):
    if r["id"] in ids: print(r["id"],"|",r["quote_verbatim"][:700],"\n")

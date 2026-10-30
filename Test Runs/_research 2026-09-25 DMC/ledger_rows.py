import csv,sys
rows=list(csv.DictReader(open('principle_ledger.csv',encoding='utf-8-sig')))
ids=sys.argv[1].split(',')
for r in rows:
    if r['id'] in ids:
        print(f"[{r['id']}] ({r['year']}, {r['source_file']}): {r['quote_verbatim']}\n")

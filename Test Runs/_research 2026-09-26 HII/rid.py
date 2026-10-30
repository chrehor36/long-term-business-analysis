import csv,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
rows={list(r.values())[0]:r for r in csv.DictReader(open('../../principle_ledger.csv',encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    r=rows.get(i)
    if not r: print('MISSING',i); continue
    print(f"## {i} ({r['year']}, {r['source_file'][:60]}) :: {r['concept'][:160]}\n   Q: {r['quote_verbatim'][:900]}\n")

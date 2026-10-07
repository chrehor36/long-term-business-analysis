import csv, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
rows = list(csv.DictReader(open('../../principle_ledger.csv', encoding='utf-8-sig')))
for want in sys.argv[1:]:
    hit = [r for r in rows if r['id'] == want]
    if not hit: print(want, 'MISSING'); continue
    for r in hit:
        print('==', want, r['year'], r['source_file'], '|', r['quote_verbatim'][:700])

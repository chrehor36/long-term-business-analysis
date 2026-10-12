import csv, sys
rows = {r[list(r.keys())[0]]: r for r in csv.DictReader(open(r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv', encoding='utf-8'))}
for i in sys.argv[1:]:
    r = rows.get(i)
    if not r: print(i, 'MISSING'); continue
    q = [v for k, v in r.items() if k.lower().startswith('quote') or k.lower()=='verbatim']
    print(f"== {i}: {q[0] if q else r}\n")

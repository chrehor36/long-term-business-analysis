import csv, sys, re
pat = re.compile(sys.argv[1], re.I)
n = 0
for r in csv.DictReader(open(r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv', encoding='utf-8-sig')):
    if pat.search(r['quote_verbatim']):
        n += 1
        if n <= int(sys.argv[2] if len(sys.argv) > 2 else 15):
            print(f"== {r['id']}: {r['quote_verbatim'][:700]}\n")
print('matches', n)

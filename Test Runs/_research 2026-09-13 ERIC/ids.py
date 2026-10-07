# usage: python ids.py FILE  -> list ledger ids cited in FILE that are missing from principle_ledger.csv
import csv, re, sys
L = {r[0].lstrip('\ufeff'): r for r in csv.reader(open(r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger.csv', encoding='utf-8'))}
t = open(sys.argv[1], encoding='utf-8').read()
cited = sorted(set(re.findall(r'E\d-\d\d', t)))
print('cited', len(cited), 'missing', [c for c in cited if c not in L])
if len(sys.argv) > 2:
    for c in sys.argv[2:]:
        r = L.get(c); print(c, (r[5] + ' | ' + r[2][:160]) if r else 'MISSING')

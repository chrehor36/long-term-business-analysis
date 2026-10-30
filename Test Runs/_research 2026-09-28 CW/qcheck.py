import re, csv
ids = {list(r.values())[0] for r in csv.DictReader(open('../../principle_ledger.csv', encoding='utf-8'))}
t = open('../2026-09-28 Run - CW Curtiss-Wright.md', encoding='utf-8').read()
cited = set()
for grp in re.findall(r'\[((?:E\d-\d+)(?:,\s*E\d-\d+)*)\]', t):
    cited.update(x.strip() for x in grp.split(','))
cited |= set(re.findall(r'\bE\d-\d+\b', t))
missing = sorted(c for c in cited if c not in ids)
print('cited', len(cited), 'missing', missing)
print(sorted(cited))

import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
run = open(r'../2026-10-16 Run - SEI Solaris Energy Infrastructure.md', encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(r'../../principle_ledger_v5.csv', encoding='utf-8-sig'))}
def norm(s):
    s = s.replace('“', '"').replace('”', '"').replace('’', "'").replace('‘', "'")
    return re.sub(r'\s+', ' ', s).strip()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', run)
print('E-ids:', eids or 'none'); bad += len(eids)
ids = set(re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run))
missing = [i for i in ids if i not in rows]
print(len(ids), 'distinct ids; missing:', missing or 'none'); bad += len(missing)
# quote immediately followed by one or more bold ids
pat = re.compile(r'[“"]([^“”"]{6,}?)[”"][^“”"\n*]{0,40}?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,; ]*)+)')
n = 0
for m in pat.finditer(run):
    q = m.group(1); first = re.search(r'([MLR]\d{4}-\d{3})', m.group(2)).group(1)
    row = norm(rows.get(first, ''))
    parts = [norm(p).strip(' .,;:') for p in re.split(r'\[\.\.\.\]', q)]
    ok = all(p in row or p.replace('"', "'") in row.replace('"', "'") for p in parts if p)
    n += 1
    if not ok:
        bad += 1; print('NOT IN ROW', first, '|', q[:140])
print(n, 'quoted fragments checked;', 'FAIL' if bad else 'PASS')

# Dispatcher check: every quoted fragment written directly before a v5 id (the id within 25 characters after the
# closing quote, ids chained by commas allowed) is in one of those ids' rows.
import csv, re, sys
run = sys.argv[1]
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8') as f:
    rd = csv.reader(f); next(rd)
    for r in rd: rows[r[0]] = ' '.join(r)
def norm(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('\u2014', '-').replace('\u2013', '-')
    return re.sub(r'\s+', ' ', s).lower()
text = open(run, encoding='utf-8').read()
idre = r'[MLR]\d{4}-\d{3,4}'
pat = re.compile(r'["\u201c]([^"\u201c\u201d]{4,}?)["\u201d][^"\u201c\u201d\n]{0,25}?\*\*\[(' + idre + r')\]\*\*((?:\s*,\s*\*\*\[' + idre + r'\]\*\*)*)', re.S)
n = bad = 0
for m in pat.finditer(text):
    ids = [m.group(2)] + re.findall(idre, m.group(3))
    for fr in re.split(r'\[\.\.\.\]|\.\.\.|\u2026', m.group(1)):
        fr = fr.strip(' .,;:')
        if len(fr) < 4: continue
        n += 1
        if not any(norm(fr) in norm(rows.get(i, '')) for i in ids):
            bad += 1; print('NOT IN ROW', ids, '|', re.sub(r'\s+', ' ', fr)[:160])
missing = sorted({i for i in re.findall(r'\b(' + idre + r')\b', text) if i not in rows})
print('fragments', n, 'unmatched', bad, 'missing ids', missing, 'E-ids', re.findall(r'\[E\d-\d+\]', text))

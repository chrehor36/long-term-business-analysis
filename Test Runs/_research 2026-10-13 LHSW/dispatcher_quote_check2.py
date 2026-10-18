# Dispatcher check, tight form: a quotation that ends within a few characters before **[id]** must be in that row.
import csv, re, sys, unicodedata
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        rows[r[list(r.keys())[0]]] = ' '.join(r.values())
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in (('\u2019', "'"), ('\u2018', "'"), ('\u201c', '"'), ('\u201d', '"')): s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()
txt = re.sub(r'\s+', ' ', open(sys.argv[1], encoding='utf-8').read())
n = bad = 0
for m in re.finditer(r'["\u201c]([^"\u201c\u201d]{8,400})["\u201d][^"\u201c\u201d\[]{0,25}\*\*\[([MLR]\d{4}-\d{3}[a-z]?(?:\]\s*\[|, ?[MLR]\d{4}-\d{3}[a-z]?)*)', txt):
    q = m.group(1); ids = re.findall(r'[MLR]\d{4}-\d{3}[a-z]?', m.group(2)); n += 1
    for p in [p for p in re.split(r'\[\.\.\.\]|\.\.\.|\u2026', q) if len(p.strip()) > 5]:
        if not any(norm(p) in norm(rows.get(i, '')) for i in ids):
            print('NOT IN ROW', ids, '|', p.strip()[:140]); bad += 1
print('quotes beside ids', n, 'problems', bad)

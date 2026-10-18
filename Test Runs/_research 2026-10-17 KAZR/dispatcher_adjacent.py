# Dispatcher's tighter check: a quoted fragment followed within 40 characters by **[id]** (one or more ids) must be in one of those rows.
import csv, re, sys, unicodedata
rows = {r['id']: r for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
qcol = [k for k in next(iter(rows.values())).keys() if 'quote' in k.lower()][0]
def norm(s):
    s = unicodedata.normalize('NFKC', s).replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    return re.sub(r'\s+', ' ', s).lower().strip()
text = open(sys.argv[1], encoding='utf-8').read()
n = bad = 0
for m in re.finditer(r'"([^"]{8,})"([^"]{0,40}?)((?:\s*,?\s*\*\*\[[MLR]\d{4}-\d{3}\]\*\*)+)', text):
    ids = re.findall(r'[MLR]\d{4}-\d{3}', m.group(3))
    parts = [norm(x).strip(' .,;') for x in m.group(1).split('[...]') if len(norm(x)) > 5]
    n += 1
    if not all(any(p in norm(rows[i][qcol]) for i in ids if i in rows) for p in parts):
        bad += 1; print('SLIP?', ids, '|', m.group(1)[:140].replace('\n', ' '))
print('adjacent fragments', n, 'problems', bad)

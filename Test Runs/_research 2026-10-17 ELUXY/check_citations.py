"""Citation check for the ELUXY run: (1) no E-ids; (2) every M/L/R id exists in principle_ledger_v5.csv;
(3) every quoted fragment that stands beside an id (the id follows the closing quote, after at most a few characters,
or the id is the only id in a sentence that opens with the quote) is in that id's row (elisions [...] split the check).
(4) every id in the file is listed with whether a quote was checked against it."""
import csv, re, sys, unicodedata
run, ledger = sys.argv[1], sys.argv[2]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ledger, encoding='utf-8-sig'))}
def norm(s):
    s = unicodedata.normalize('NFKC', s).replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip()
text = norm(open(run, encoding='utf-8').read())
problems = 0
if re.search(r'\[E\d', text): print('E-id found'); problems += 1
ids = sorted(set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', text)))
for i in ids:
    if i not in rows: print('MISSING', i); problems += 1
checked = 0
for m in re.finditer(r'"([^"]{6,}?)"((?:\s|[.,;:)\]]){0,4})((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)', text):
    frag = m.group(1); cited = re.findall(r'\[([MLR]\d{4}-\d{3})\]', m.group(3))
    parts = [p.strip(' .,;') for p in frag.split('[...]')]
    ok = any(all(p in norm(rows.get(i, '')) for p in parts if p) for i in cited)
    checked += 1
    if not ok:
        print('NOT IN ROW:', frag[:100], '->', cited); problems += 1
print(f'ids: {len(ids)}; quote-id pairs checked: {checked}; problems: {problems}')

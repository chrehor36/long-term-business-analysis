# dispatcher's fold check (overnight cycle 2026-10-10): every quoted fragment (straight or curly quotes) followed by
# one or more bold v5 ids must appear, piece by piece split on [...], in at least one cited row; no E-ids; ids exist.
import csv, re, sys
RUN = sys.argv[1]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv', encoding='utf-8-sig'))}
txt = open(RUN, encoding='utf-8').read()
def n(s): return re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u2018', "'")).strip()
bad = []
if re.search(r'\[E\d+-\d+\]', txt): bad.append('E-id present')
ids = set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', txt))
bad += [f'missing {i}' for i in ids if i not in rows]
pat = re.compile(r'(?:"([^"\n]{3,600}?)"|\u201c([^\u201d]{3,600}?)\u201d)\s*(?:\([^)]{0,200}\)\s*)?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,;\s]*)+)')
k = 0
for m in pat.finditer(txt):
    frag = m.group(1) or m.group(2); cited = re.findall(r'[MLR]\d{4}-\d{3}', m.group(3)); k += 1
    pieces = [n(p) for p in re.split(r'\[\.\.\.\]|\[…\]|\.\.\.|…', frag) if n(p)]
    if not any(all(p in n(rows.get(c, '')) for p in pieces) for c in cited):
        bad.append(f'NOT IN ROW {cited}: {frag[:140]}')
print(f'ids {len(ids)}, fragments {k}, problems {len(bad)}'); [print(' ', b) for b in bad]

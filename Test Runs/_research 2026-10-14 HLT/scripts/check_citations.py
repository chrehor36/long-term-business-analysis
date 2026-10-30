# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# that sits immediately before an id (in the same sentence span) is found in that id's row.
import csv, re, sys, unicodedata
run, ledger = sys.argv[1], sys.argv[2]
rows = {}
for r in csv.DictReader(open(ledger, encoding='utf-8')):
    k = r.get('\ufeffid') or r.get('id'); rows[k] = r['quote_verbatim']
text = open(run, encoding='utf-8').read()
def norm(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"').replace('\u2014', '-').replace('\u2013', '-')
    s = s.replace('**', '')
    return re.sub(r'\s+', ' ', s).strip().lower()
eids = re.findall(r'\[E\d+-\d+\]', text)
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', text)
missing = sorted({i for i in ids if i not in rows})
print('E-ids:', eids); print('distinct M/L/R ids:', len(set(ids)), 'missing:', missing)
# fragments: a "..." quote followed (within 12 chars, allowing markup) by one or more ids
bad, n = [], 0
for m in re.finditer(r'"([^"]{3,600}?)"[^"\[]{0,40}?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[ ,]*)+)', text):
    frag = m.group(1); idl = re.findall(r'[MLR]\d{4}-\d{3}', m.group(2))
    parts = [p for p in re.split(r'\[\.\.\.\]', frag) if p.strip()]
    for i in idl[:1]:
        n += 1
        row = norm(rows.get(i, ''))
        if not all(norm(p).strip(' .,;:') in row for p in parts):
            bad.append((i, frag[:120]))
print('fragments checked:', n, 'not found in row:', len(bad))
for b in bad: print('  ', b)

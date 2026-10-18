# Check a run file against principle_ledger_v5.csv:
#  1. no E-ids; 2. every M/L/R id exists; 3. every quoted fragment in the same sentence-chunk as an id is in that row.
# usage: python -I -X utf8 check_ids.py LEDGER RUNFILE
import csv, re, sys, unicodedata

def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('—', '-').replace('–', '-').replace('�', '')
    s = re.sub(r'\*+', '', s)
    return re.sub(r'\s+', ' ', s).strip().lower()

rows = {r['id']: norm(r['quote_verbatim']) for r in csv.DictReader(open(sys.argv[1], encoding='utf-8-sig'))}
text = open(sys.argv[2], encoding='utf-8').read()
bad = 0
for m in re.finditer(r'\[E\d+-\d+\]', text):
    print('E-ID:', m.group()); bad += 1
ids = re.findall(r'\[((?:M|L|R)\d{4}-\d{3})\]', text)
for i in sorted(set(ids)):
    if i not in rows:
        print('MISSING ID:', i); bad += 1
# fragment check: split into chunks at ids; the quotes immediately before an id belong to it
flat = re.sub(r'\s+', ' ', text)
for m in re.finditer(r'((?:"[^"]{3,}?"[^"\[]{0,80}?)+)\*\*((?:\[(?:M|L|R)\d{4}-\d{3}\],? ?)+)\*\*', flat):
    quotes = re.findall(r'"([^"]{3,}?)"', m.group(1))
    cids = re.findall(r'(?:M|L|R)\d{4}-\d{3}', m.group(2))
    for q in quotes:
        parts = [p for p in re.split(r'\[\.\.\.\]', q) if p.strip()]
        ok = any(all(norm(p).strip(' .,;:') in rows.get(c, '') for p in parts) for c in cids)
        if not ok:
            print('NOT IN ROW', cids, ':', q[:140]); bad += 1
print('ids checked:', len(set(ids)), 'problems:', bad)

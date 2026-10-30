# Check for the LNT run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment that sits immediately before an id (within the same sentence run) is in that row.
import csv, re, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RUN = os.path.join(ROOT, 'Test Runs', '2026-10-18 Run - LNT Alliant Energy.md')
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(os.path.join(ROOT, 'principle_ledger_v5.csv'), encoding='utf-8-sig'))}
text = open(RUN, encoding='utf-8').read()

def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('�', '').replace('—', '-').replace('–', '-')
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()

bad = 0
eids = re.findall(r'\[E\d-\d+\]', text)
if eids:
    print('E-ids found:', eids); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', text)
for i in sorted(set(ids)):
    if i not in rows:
        print('MISSING id', i); bad += 1
print('ids cited:', len(set(ids)), 'occurrences:', len(ids))

# quoted fragment followed by one or more ids: "..." **[ID]** (allow intervening punctuation/space, up to 12 chars)
pat = re.compile(r'"([^"]{6,}?)"[^"\[]{0,12}((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[ ,;and]*)+)')
checked = 0
for m in pat.finditer(text):
    frag = m.group(1)
    cids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', m.group(2))
    parts = [p for p in re.split(r'\s*\[\.\.\.\]\s*', frag) if p.strip()]
    ok = any(all(norm(p) in norm(rows.get(c, '')) for p in parts) for c in cids)
    checked += 1
    if not ok:
        bad += 1
        print('NOT IN ROW', cids, '::', frag[:140])
print('quoted fragments checked:', checked)
print('RESULT:', 'PASS' if bad == 0 else 'FAIL (%d)' % bad)

"""Run check for the CSL run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment
standing immediately before an id (or a run of ids) is found in at least one of those rows (normalized for curly
quotes, apostrophes, dashes and whitespace; [...] splits a quote into parts, each checked)."""
import csv, re, sys
ROOT = r'C:\Users\chreh\OneDrive\Documents\BRK'
RUN = ROOT + r'\Test Runs\2026-10-07 Run - CSL Carlisle.md'
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ROOT + r'\principle_ledger_v5.csv', encoding='utf-8-sig'))}
text = open(RUN, encoding='utf-8').read()


def norm(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('\u2014', '-').replace('\u2013', '-').replace('\ufffd', '')
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()


bad = 0
eids = re.findall(r'\[E\d+-\d+\]', text)
if eids:
    print('E-IDS FOUND:', eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
missing = sorted(set(i for i in ids if i not in rows))
if missing:
    print('MISSING IDS:', missing); bad += 1
print('ids cited:', len(ids), 'distinct:', len(set(ids)))
# quote then ids: "..." optionally followed by up to 12 chars of punctuation/space, then one or more **[ID]**
pat = re.compile(r'["\u201c]([^"\u201c\u201d]{3,600})["\u201d][\s,.;:()\-\u2014]{0,12}((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[\s,]*)+)')
n = 0
for m in pat.finditer(text):
    frag = m.group(1)
    qids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', m.group(2))
    parts = [p for p in re.split(r'\[\.\.\.\]', frag) if p.strip()]
    ok = False
    for i in qids:
        src = norm(rows.get(i, ''))
        if all(norm(p).strip(' .,;:') in src for p in parts):
            ok = True
            break
    n += 1
    if not ok:
        bad += 1
        print('NOT IN ROW', qids, '::', frag[:160])
print('quoted fragments checked:', n)
print('RESULT:', 'PASS' if bad == 0 else 'FAIL')
sys.exit(1 if bad else 0)

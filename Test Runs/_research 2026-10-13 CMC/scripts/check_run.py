"""Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
within the same sentence/bullet as an id appears in at least one of the ids cited there (apostrophes and the
ledger's replacement characters normalized). Prints failures."""
import csv, re, sys
RUN = "Test Runs/2026-10-13 Run - CMC Commercial Metals.md"
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
def norm(s):
    s = s.replace('�', "'").replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = re.sub(r'\s+', ' ', s)
    return s.lower()
text = open(RUN, encoding='utf-8').read()
bad = 0
for m in re.finditer(r'\[E\d', text):
    print('E-id found at', m.start()); bad += 1
ids = set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', text))
for i in sorted(ids):
    if i not in rows: print('MISSING id', i); bad += 1
# fragment check: split into segments by blank line / bullet; within each, quoted strings near ids
for seg in re.split(r'\n\s*\n|\n- |\n\d+\. |\n\(\d+\)', text):
    segids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', seg)
    if not segids: continue
    # pair each quote with the first id that follows it in the segment
    for qm in re.finditer(r'"([^"]{6,})"', seg):
        q = qm.group(1)
        after = re.findall(r'\[([MLR]\d{4}-\d{3})\]', seg[qm.end():])
        cand = after[:3] if after else segids
        nq = norm(q).replace('[...]', '\x00')
        parts = [p.strip(' .,;:') for p in nq.split('\x00') if p.strip(' .,;:')]
        ok = any(all(p in norm(rows.get(c, '')) for p in parts) for c in cand)
        if not ok:
            # quote may be a filing quote, report for review
            print('UNMATCHED (review: filing quote or wrong id):', q[:90], '->', cand)
print('ids:', len(ids), 'failures:', bad)

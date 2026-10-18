# Citation check for the VSEC run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment in the same sentence-clause as an id is found in that id's row (quotes normalized).
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RUN = "Test Runs/2026-10-16 Run - VSEC VSE Corporation.md"
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('�', '').replace('—', '-').replace('–', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()
text = open(RUN, encoding='utf-8').read()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', text)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
print('distinct ids cited:', len(set(ids)))
# fragment check: for each id occurrence, look back over the text since the previous id (or line start) for quoted fragments
for line in text.splitlines():
    pos = 0
    for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', line):
        seg = line[pos:m.start()]
        pos = m.end()
        frags = re.findall(r'"([^"]{4,}?)"', seg)
        rid = m.group(1)
        if rid not in rows: continue
        rowt = norm(rows[rid])
        for f in frags:
            parts = [p.strip() for p in re.split(r'\[\.\.\.\]', f) if p.strip()]
            ok = all(norm(p).strip(' .,;:') in rowt for p in parts)
            if not ok:
                print(f'FRAGMENT NOT IN ROW {rid}: "{f}"'); bad += 1
print('RESULT:', 'PASS' if bad == 0 else f'FAIL ({bad})')

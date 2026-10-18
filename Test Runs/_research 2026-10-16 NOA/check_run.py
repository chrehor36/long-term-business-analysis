# Citation check for the NOA run of 2026-10-16.
# 1) no E-ids; 2) every M/L/R id cited exists in principle_ledger_v5.csv;
# 3) every quoted fragment in the same sentence as, and before, an id citation is found in that id's row
#    (elisions [...] split the fragment; whitespace normalized). Run from the repository root.
import csv, re, sys

run = open(sys.argv[1], encoding='utf-8').read()
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8') as f:
    r = csv.reader(f)
    next(r)
    for row in r:
        rows[row[0]] = row[2]

norm = lambda s: re.sub(r'\s+', ' ', s).strip()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', run)
print('E-ids:', eids or 'none')
bad += len(eids)
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)
missing = sorted(set(i for i in ids if i not in rows))
print('ids cited:', len(set(ids)), 'missing:', missing or 'none')
bad += len(missing)

def current_sentence(seg):
    seg = seg.split('\n\n')[-1]
    inq = False
    cut = 0
    for k, ch in enumerate(seg):
        if ch == '"':
            inq = not inq
        elif not inq and (seg[k:k + 2] in ('. ', '; ', '.\n', ';\n') or seg[k:k + 3] == '\n- '):
            cut = k + 1
    return seg[cut:]

pat = re.compile(r'((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)')
pos = 0
checked = 0
for m in pat.finditer(run):
    seg = current_sentence(run[pos:m.start()])
    pos = m.end()
    group = re.findall(r'[MLR]\d{4}-\d{3}', m.group(1))
    for q in re.findall(r'"([^"]*)"', seg):
        for p in [norm(x) for x in norm(q).split('[...]')]:
            p = p.rstrip('.,;: ').strip()
            if not p or p == '...':
                continue
            checked += 1
            if not any(p in norm(rows.get(g, '')) for g in group):
                bad += 1
                print('NOT IN ROW', group, '|', p[:120])
print('fragments checked:', checked)
print('RESULT', 'PASS' if bad == 0 else f'{bad} problems')

# Citation check for the NGS run: no E-ids; every M/L/R id in the v5 ledger; every quoted fragment beside an id is in that row.
import csv, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
RUN = "Test Runs/2026-10-16 Run - NGS Natural Gas Services Group.md"
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
text = open(RUN, encoding='utf-8').read()
bad = 0
for e in re.findall(r'\[(E\d-\d+)\]', text): print('E-id found:', e); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', text)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
# a quoted fragment immediately before an id (within the same paragraph): "...." **[ID]** or "...." [ID]
for para in re.split(r'\n\s*\n', text):
    flat = norm(para)
    for m in re.finditer(r'"([^"]{8,}?)"[^"\[]{0,40}?\*{0,2}\[([MLR]\d{4}-\d{3})\]', flat):
        frag, i = m.group(1), m.group(2)
        if i not in rows: continue
        q = norm(rows[i])
        parts = [norm(p) for p in frag.split('[...]')]
        ok = all(p.strip(' .,;:') in q for p in parts if p.strip(' .,;:'))
        if not ok: print(f'FRAGMENT NOT IN ROW {i}: "{frag[:90]}"'); bad += 1
print(f'ids cited: {len(set(ids))} distinct, {len(ids)} total; problems: {bad}')

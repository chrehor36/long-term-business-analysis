"""Run-file citation check: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
between the previous id (or paragraph start) and an id is found in that id's row (whitespace normalized; [...] splits)."""
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
run, ledger = sys.argv[1], sys.argv[2]
rows = {r['﻿id']: r['quote_verbatim'] for r in csv.DictReader(open(ledger, encoding='utf-8'))}
text = open(run, encoding='utf-8').read()
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
bad = 0
eids = re.findall(r'\[(E\d+-\d+)\]', text)
if eids: print('E-IDS FOUND', eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING ID', i); bad += 1
print(f'{len(ids)} id citations, {len(set(ids))} distinct')
paras = re.split(r'\n\s*\n', text)
for p in paras:
    pos = 0
    for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', p):
        seg = p[pos:m.start()]; pos = m.end()
        # only the stretch after the last sentence break that holds no other quote-free clause: take the whole segment
        quotes = [q for q in re.findall(r'"([^"]*)"', seg) if len(q) >= 6]
        row = norm(rows.get(m.group(1), ''))
        for q in quotes:
            for piece in re.split(r'\s*\[\.\.\.\]\s*', norm(q)):
                piece = piece.strip(' ,;:')
                if len(piece) < 4: continue
                if piece not in row:
                    print(f'NOT IN {m.group(1)}: "{piece[:110]}"'); bad += 1
print('RESULT', 'PASS' if bad == 0 else f'{bad} flags (filing quotes in the same span are expected flags; read each)')

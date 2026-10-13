"""Check the run file's citations: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment that
stands immediately before a bolded id (within the same sentence) is found verbatim in that row (elisions [...] split)."""
import csv, re, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
run = open(os.path.join(ROOT, 'Test Runs', '2026-10-12 Run - MTSUY Mitsui and Co.md'), encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(os.path.join(ROOT, 'principle_ledger_v5.csv'), encoding='utf-8-sig'))}
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', run)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
flat = norm(run)
# a quoted fragment followed (after optional punctuation/space) by one or more bold ids
for m in re.finditer(r'"([^"]{6,400}?)"[^"\n]{0,3}\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,\s]*)+)', flat):
    frag, idblock = m.group(1), m.group(2)
    rid = re.findall(r'[MLR]\d{4}-\d{3}', idblock)
    parts = [p.strip(' .,') for p in frag.split('[...]') if p.strip(' .,')]
    ok = any(all(norm(p) in norm(rows.get(r, '')) for p in parts) for r in rid)
    if not ok:
        print('NOT IN ROW', rid, '::', frag[:120]); bad += 1
print(f'{len(set(ids))} distinct ids; checks', 'FAILED' if bad else 'PASSED', bad)
sys.exit(1 if bad else 0)

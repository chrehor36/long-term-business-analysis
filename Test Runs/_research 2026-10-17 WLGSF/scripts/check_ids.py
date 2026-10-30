"""Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
immediately before an id (in the same sentence) is a substring of that row's quote."""
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
run = open(ROOT + r"\Test Runs\2026-10-17 Run - WLGSF Wang and Lee Group.md", encoding='utf-8').read()
R = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ROOT + r"\principle_ledger_v5.csv", encoding='utf-8-sig'))}
norm = lambda x: re.sub(r'\s+', ' ', x.replace('’', "'").replace('“', '"').replace('”', '"')).strip()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', run)
print('E-ids:', eids or 'none'); bad += len(eids)
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)
print('ids cited:', len(ids), 'distinct:', len(set(ids)))
for i in sorted(set(ids)):
    if i not in R: print('MISSING', i); bad += 1
# quoted fragment followed (within 6 chars, allowing ** and space) by an id
for m in re.finditer(r'"([^"]{6,400})"\s*\**\s*\[([MLR]\d{4}-\d{3})\]', run.replace('“', '"').replace('”', '"')):
    q, i = m.group(1), m.group(2)
    ok = i in R and all(norm(part) in norm(R[i]) for part in q.split('[...]') if part.strip())
    print('OK ' if ok else 'BAD', i, q[:80]); bad += (not ok)
print('PROBLEMS:', bad)

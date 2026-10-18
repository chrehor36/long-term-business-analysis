"""Citation check for the USAC run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted
fragment placed immediately before an id (or a run of ids) is found in one of those rows, elisions [...] split."""
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = "Test Runs/2026-10-16 Run - USAC USA Compression Partners.md"
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}

def norm(t):
    t = t.replace('“', '"').replace('”', '"').replace('’', "'").replace('‘', "'")
    t = re.sub(r'\s+', ' ', t)
    return t.strip().lower()

text = open(RUN, encoding='utf-8').read()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', text)
if eids:
    print('E-ids found:', eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
missing = sorted(set(i for i in ids if i not in rows))
if missing:
    print('missing ids:', missing); bad += 1
print(f'{len(ids)} id citations, {len(set(ids))} distinct, missing {len(missing)}')

# quoted fragment directly followed by a run of ids
pat = re.compile(r'"([^"]{3,})"\s*[.,;:]?\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)')
checked = 0
for m in pat.finditer(text):
    frag = m.group(1)
    cited = re.findall(r'[MLR]\d{4}-\d{3}', m.group(2))
    parts = [p for p in re.split(r'\[\.\.\.\]', frag) if p.strip()]
    ok = any(all(norm(p) in norm(rows.get(c, '')) for p in parts) for c in cited)
    checked += 1
    if not ok:
        bad += 1
        print('NOT IN ROW:', cited, '::', frag[:120])
print(f'{checked} quoted fragments checked against their rows')
print('PASS' if bad == 0 else f'FAIL ({bad})')

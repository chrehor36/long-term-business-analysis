"""Citation check for the FTS run file: no E-ids; every M/L/R id resolves in principle_ledger_v5.csv; every quoted
fragment that stands immediately before an id (or a run of ids) is in one of those rows. Usage: python check_ids.py"""
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
LEDGER = r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv"
RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-23 Run - FTS Fortis.md"
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(LEDGER, encoding='utf-8-sig'))}
text = open(RUN, encoding='utf-8').read()

def norm(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('\ufffd', '').replace('**', '')
    return re.sub(r'\s+', ' ', s).strip().lower()

bad = 0
eids = re.findall(r'\[E\d+-\d+\]', text)
if eids:
    print('E-ids found:', sorted(set(eids))); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', text)
missing = sorted({i for i in ids if i not in rows})
if missing:
    print('ids not in the ledger:', missing); bad += 1
print(f'{len(ids)} id citations, {len(set(ids))} distinct; missing {len(missing)}')

# a quoted fragment followed (within the same clause) by a run of bold ids
pat = re.compile(r'"([^"\n]{3,600}?)"[^"\n]{0,40}?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)')
checked = 0
for m in pat.finditer(text):
    frag = m.group(1); cited = re.findall(r'\[([MLR]\d{4}-\d{3})\]', m.group(2))
    pieces = [norm(p) for p in re.split(r'\[\.\.\.\]', frag) if norm(p)]
    ok = any(all(p in norm(rows.get(c, '')) for p in pieces) for c in cited)
    checked += 1
    if not ok:
        bad += 1
        print('NOT IN ROW:', cited, '|', frag[:160])
print(f'{checked} quoted fragments checked')
print('PASS' if not bad else f'FAIL ({bad})')

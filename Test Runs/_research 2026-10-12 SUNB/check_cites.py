"""Citation check for the SUNB run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
every quoted fragment placed immediately before an id (or a run of ids) is found in at least one of those rows."""
import csv, re, sys, unicodedata
RUN = sys.argv[1]; LED = sys.argv[2]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(LED, encoding='utf-8-sig'))}
def norm(t):
    t = unicodedata.normalize('NFKC', t)
    for a, b in [('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('—', '-'), ('–', '-'), ('�', '')]:
        t = t.replace(a, b)
    t = t.replace('**', '')
    return re.sub(r'\s+', ' ', t).strip().lower()
txt = open(RUN, encoding='utf-8').read()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', txt)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', txt)
missing = sorted(set(i for i in ids if i not in rows))
if missing: print('MISSING ids:', missing); bad += 1
# fragments: a double-quoted span followed (within 60 chars, no other quote) by one or more bold ids
pat = re.compile(r'"([^"]{3,600})"([^"]{0,60}?)((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[ ,;]*(?:and )?)+)')
nfrag = 0
for m in pat.finditer(txt):
    frag = m.group(1); between = m.group(2)
    if '\n' in between: continue
    cited = re.findall(r'\[([MLR]\d{4}-\d{3})\]', m.group(3))
    pieces = [p for p in re.split(r'\[\.\.\.\]', frag) if len(p.strip(' .,;:')) > 2]
    nfrag += 1
    for p in pieces:
        pn = norm(p).strip(' .,;:')
        if not any(pn in norm(rows.get(c, '')) for c in cited):
            print('NOT IN ROW', cited, '::', p[:120]); bad += 1
print(f'ids cited: {len(set(ids))} distinct; fragments checked: {nfrag}; problems: {bad}')
sys.exit(1 if bad else 0)

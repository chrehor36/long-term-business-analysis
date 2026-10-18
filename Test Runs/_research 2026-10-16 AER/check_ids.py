# Check the AER run file: no E-ids; every M/L/R id resolves in principle_ledger_v5.csv; every quoted fragment that
# sits in the same clause just before an id is found in that row (elisions [...] split the fragment).
import csv, re, sys, unicodedata
ROOT = r'C:\Users\chreh\OneDrive\Documents\BRK'
RUN = ROOT + r'\Test Runs\2026-10-16 Run - AER AerCap Holdings.md'
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ROOT + r'\principle_ledger_v5.csv', encoding='utf-8-sig'))}
text = open(RUN, encoding='utf-8').read()

def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in [('\u2019', "'"), ('\u2018', "'"), ('\u201c', '"'), ('\u201d', '"'), ('\u2014', '-'), ('\u2013', '-'), ('\ufffd', '-')]:
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()

fail = 0
eids = re.findall(r'\[E\d+-\d+\]', text)
if eids: print('E-ids found:', eids); fail += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
missing = sorted(set(i for i in ids if i not in rows))
if missing: print('MISSING ids:', missing); fail += 1
print(f'{len(ids)} id citations, {len(set(ids))} distinct, missing {len(missing)}')

# quoted fragments in the clause before each id
checked = 0; flagged = []
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text):
    i = m.group(1)
    start = max(text.rfind('**[', 0, m.start() - 1), text.rfind('\n\n', 0, m.start()), 0)
    seg = text[start:m.start()]
    # only the last clause: cut at sentence ends or parenthetical filing references
    seg = re.split(r'(?<=[.;:])\s+(?=[A-Z(*])', seg)[-1]
    for q in re.findall('["“]([^"“”]{6,})["”]', seg):
        if re.search(r'\(Item|\b20-F\b|10-K|8-K|accession|release\)', seg[seg.find(q) + len(q): seg.find(q) + len(q) + 25]):
            continue  # a filing quote, cited to the filing
        for frag in q.split('[...]'):
            frag = frag.strip(' ,.')
            if len(frag) < 6: continue
            checked += 1; print("   ok?", i, "|", frag[:90]) if "-v" in sys.argv else None
            if norm(frag) not in norm(rows.get(i, '')):
                flagged.append((i, frag))
print(f'{checked} fragments checked; {len(flagged)} not found in the cited row:')
for i, f in flagged: print('  ', i, '|', f[:120])
sys.exit(1 if (fail or flagged) else 0)

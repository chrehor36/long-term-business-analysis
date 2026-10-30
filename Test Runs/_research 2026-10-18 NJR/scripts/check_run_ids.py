"""Check the NJR run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that sits
immediately before an id (same paragraph, the last "..." before the id) is a substring of that row, after normalising quotes,
dashes and whitespace; [...] elisions split the fragment into pieces checked in order."""
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = r'C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-10-18 Run - NJR New Jersey Resources.md'
LED = r'C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv'
rows = {r[0]: r[2] for r in csv.reader(open(LED, encoding='utf-8'))}
def norm(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('\u2014', '-').replace('\u2013', '-').replace('\ufffd', '')
    return re.sub(r'\s+', ' ', s).strip()
text = open(RUN, encoding='utf-8').read()
bad = 0
if re.search(r'\[E\d', text): print('E-id found'); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
missing = sorted(set(i for i in ids if i not in rows))
print('ids cited:', len(set(ids)), 'missing:', missing); bad += len(missing)
paras = re.split(r'\n\s*\n|\n- |\n\| ', text)
checked = 0
for p in paras:
    for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', p):
        before = p[:m.start()]
        # the quote must end within 12 characters of the id (allowing punctuation, bold markers, spaces)
        q = re.search(r'"([^"]{6,}?)"[\s\.,;:\)\*]{0,12}$', norm(before))
        if not q: continue
        frag = q.group(1)
        row = norm(rows.get(m.group(1), ''))
        pieces = [x.strip(' .,;:') for x in re.split(r'\[\.\.\.\]', frag) if x.strip(' .,;:')]
        pos = 0; ok = True
        for pc in pieces:
            k = row.find(pc, pos)
            if k < 0: ok = False; break
            pos = k + len(pc)
        checked += 1
        if not ok:
            bad += 1; print('NOT IN ROW', m.group(1), '|', frag[:160])
print('quoted fragments checked:', checked, '| problems:', bad)

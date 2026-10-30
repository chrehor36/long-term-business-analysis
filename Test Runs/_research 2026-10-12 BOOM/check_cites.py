"""Citation check for the BOOM run: no E-ids; every M/L/R id in the v5 ledger;
every quoted fragment that sits before an id (in the same paragraph, after the previous id)
is found in that id's row (elisions [...] split the fragment)."""
import csv, re, sys
RUN = r"../2026-10-12 Run - BOOM DMC Global.md"
LED = r"../../principle_ledger_v5.csv"
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(LED, encoding='utf-8-sig'))}
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('—', '-').replace('–', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()
txt = open(RUN, encoding='utf-8').read()
problems = 0
eids = re.findall(r'\[E\d+-\d+\]', txt)
if eids: print('E-ids found:', eids); problems += len(eids)
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', txt)
allids = set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', txt))
for i in sorted(allids):
    if i not in rows: print('MISSING id', i); problems += 1
frag_count = 0
paras = re.split(r'\n(?=\s*\n|\s*[-|]\s|\s*\d+\.\s|#)', txt)
for para in [x.replace('\n', ' ') for x in paras]:
    # walk ids in order; the quoted fragments between the previous id and this id belong to it
    pos = 0
    for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', para):
        seg = para[pos:m.start()]
        pos = m.end()
        rid = m.group(1)
        if rid not in rows: continue
        q = norm(rows[rid])
        for f in re.findall(r'"([^"]{6,}?)"', seg.replace('“', '"').replace('”', '"')):
            for piece in re.split(r'\[\.\.\.\]', f):
                p = norm(piece).strip(' .,;:')
                if len(p) < 4: continue
                frag_count += 1
                if p not in q:
                    print(f'NOT IN ROW {rid}: "{piece.strip()}"'); problems += 1
print(f'{len(allids)} distinct ids, {frag_count} fragments checked, {problems} problems')
if '-v' in sys.argv: pass

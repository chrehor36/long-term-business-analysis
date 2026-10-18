import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('../../principle_ledger_v5.csv', encoding='utf-8-sig'))}
txt = open("../2026-10-17 Run - ATO Atmos Energy.md", encoding='utf-8').read()
def norm(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    return re.sub(r'\s+', ' ', s).strip()
for m in re.finditer(r'["\u201c]([^"\u201c\u201d\n]{4,400}?)["\u201d]', txt):
    after = txt[m.end():m.end()+90]
    mm = re.search(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', after)
    if not mm or re.search(r'["\u201c]', after[:mm.start()]): continue
    p = norm(m.group(1)).strip(' .,;:')
    rid = mm.group(1)
    ok = all(norm(x).strip(' .,;:') in norm(rows.get(rid,'')) for x in re.split(r'\[\.\.\.\]', p) if len(norm(x).strip(' .,;:'))>3)
    if not ok: print(rid, '|', p[:150], '| gap:', repr(after[:mm.start()][:60]))

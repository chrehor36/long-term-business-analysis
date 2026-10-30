# Dispatcher check, per id: the quoted string ending within 15 characters before the id (quote pairs counted backwards from the id).
import csv, re, sys
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip().lower()
text = open(sys.argv[1], encoding='utf-8').read().replace('“','"').replace('”','"')
checked = miss = 0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text):
    pre = text[max(0, m.start()-15):m.start()]
    k = pre.rfind('"')
    if k < 0: continue
    end = m.start()-15+k if m.start() >= 15 else k
    start = text.rfind('"', 0, end)
    if start < 0 or end - start > 1500: continue
    q = text[start+1:end]
    frags = [norm(x).strip(' .,;:') for x in re.split(r'\[\.\.\.\]|\.\.\.|\[…\]|…', q)]
    ok = all(fr in norm(rows.get(m.group(1), '')) for fr in frags if len(fr) > 3)
    checked += 1
    if not ok:
        miss += 1; print('MISS', m.group(1), '|', re.sub(r'\s+', ' ', q)[:200])
print('pairs', checked, 'unmatched', miss)

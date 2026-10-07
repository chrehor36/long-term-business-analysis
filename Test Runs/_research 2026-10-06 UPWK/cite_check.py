import csv, re
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
t = open('Test Runs/2026-10-06 Run - UPWK Upwork.md', encoding='utf-8').read()
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip()
print("E-ids:", re.findall(r'\[E\d+-\d+\]', t))
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', t)
print("ids", len(ids), "distinct", len(set(ids)), "missing", [i for i in set(ids) if i not in rows])
# for each id, the window since previous id marker or blank line
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t):
    start = max(t.rfind('**[', 0, m.start()-1), t.rfind('\n\n', 0, m.start()), t.rfind('\n- ', 0, m.start()))
    win = t[start:m.start()]
    # take only the last sentence-ish segment: after the last ';' or '. ' preceding non-quote
    frags = re.findall(r'"([^"]+)"|“([^”]+)”', win)
    for a, b in frags:
        q = a or b
        for piece in q.split('[...]'):
            p = norm(piece).strip(' .,')
            if len(p) < 4: continue
            if p not in norm(rows[m.group(1)]):
                print("NOT IN", m.group(1), "::", p[:120])

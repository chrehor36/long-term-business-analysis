import csv, re
norm=lambda s: re.sub(r'\s+',' ',s)
rows={r['id']:norm(r['quote_verbatim']) for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open('Test Runs/2026-10-05 Run - OGN Organon.md',encoding='utf-8').read()
ids=re.findall(r'\[([A-Z]\d{4}-\d{3})\]', t)
print('ids', len(ids), 'distinct', len(set(ids)), 'non-MLR', [i for i in ids if not re.match(r'[MLR]\d{4}-\d{3}$',i)])
print('E-ids:', re.findall(r'\[E\d+-\d+\]', t))
print('missing:', [i for i in set(ids) if i not in rows])
fails=0; checked=0
for m in re.finditer(r'"([^"]{6,}?)"[^"\n]{0,12}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t):
    q, i = norm(m.group(1)), m.group(2)
    for frag in [p.strip(' .,;') for p in q.split('[...]')]:
        if not frag: continue
        checked+=1
        if frag not in rows[i]:
            fails+=1; print('NOT IN ROW', i, '|', frag[:100])
print('fragments checked', checked, 'failures', fails)
print('em dashes outside mandated label:', t.replace('COMPUTATION — NOT A CLEARANCE','').count('—'))

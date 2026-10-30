import csv,re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open('Test Runs/2026-10-05 Run - MBUU Malibu Boats.md',encoding='utf-8').read()
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('�','?')
    return re.sub(r'\s+',' ',s).strip()
ids=re.findall(r'\[([A-Z]+\d{4}-\d{3})\]',t)
print('ids cited',len(ids),'distinct',len(set(ids)))
bad=[i for i in set(ids) if i not in rows]; print('missing ids',bad)
eids=re.findall(r'\[(E\d+-\d+)\]',t); print('E-ids',eids)
# segments: text up to each run of id markers
pat=re.compile(r'((?:\*\*\[[A-Z]+\d{4}-\d{3}\]\*\*[ ,;]*(?:and )?)+)')
pos=0; fails=0; checked=0
for m in pat.finditer(t):
    seg=t[pos:m.start()]; group=re.findall(r'\[([A-Z]+\d{4}-\d{3})\]',m.group(1)); pos=m.end()
    # only the current sentence-ish: after last blank line or bullet start
    seg=re.split(r'\n\s*\n|\n- |\n\d+\. ',seg)[-1]
    quotes=re.findall(r'"([^"]{6,})"|“([^”]{6,})”',seg)
    for a,b in quotes:
        q=norm(a or b); checked+=1
        parts=[p.strip(' .') for p in q.split('...') if len(p.strip(' .'))>3]
        ok=any(all(norm(p) in norm(rows.get(g,'')) for p in parts) for g in group)
        if not ok:
            fails+=1; print('NOT IN ROW',group,'|',q[:140])
print('quoted fragments checked',checked,'not matched',fails)

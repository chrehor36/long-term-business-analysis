import csv,re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
P='C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv'
R='C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-10-17 Run - CLNE Clean Energy Fuels.md'
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open(P,encoding='utf-8-sig'))}
def norm(s):
    s=s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"').replace('\ufffd',"'")
    s=s.replace('\u2014','-').replace('\u2013','-')
    return re.sub(r'\s+',' ',s).strip().lower()
txt=open(R,encoding='utf-8').read()
bad=0
if re.search(r'\[E\d',txt): print('E-id found'); bad+=1
ids=list(re.finditer(r'\*\*\[([A-Z]\d{4}-\d{3})\]\*\*',txt))
print('id occurrences',len(ids),'distinct',len(set(m.group(1) for m in ids)))
for m in ids:
    if m.group(1) not in rows: print('MISSING',m.group(1)); bad+=1
# fragments: quoted text in the 300 chars before each id, back to the previous id or paragraph break
prev=0
for m in ids:
    start=max(prev, txt.rfind('\n\n',0,m.start()), m.start()-400)
    seg=txt[start:m.start()]
    prev=m.end()
    for q in re.findall(r'"([^"]{6,})"|\u201c([^\u201d]{6,})\u201d',seg):
        q=q[0] or q[1]
        parts=[p.strip(' .,;:') for p in re.split(r'\[\.\.\.\]',q) if p.strip(' .,;:')]
        row=norm(rows.get(m.group(1),''))
        ok=all(norm(p) in row for p in parts)
        if not ok: print('CHECK',m.group(1),'|',q[:120])
print('problems (ids):',bad)

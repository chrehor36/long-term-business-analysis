import csv,re,sys
R={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
s=open('Test Runs/2026-10-05 Run - ABG Asbury Automotive.md',encoding='utf-8').read()
print('E-ids:', re.findall(r'\[E\d+-\d+\]',s))
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',s)
print('ids cited', len(ids), 'distinct', len(set(ids)), 'missing', [i for i in set(ids) if i not in R])
def norm(x): return re.sub(r'\s+',' ',x).strip()
bad=0
pos=0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',s):
    seg=s[pos:m.start()]; pos=m.end()
    # only quotes after the last sentence-ish boundary that is within the same paragraph
    seg=seg.split('\n\n')[-1]
    q=re.findall(r'"([^"]{6,}?)"(?=[^"]*$)',seg) if False else re.findall(r'"((?:[^"]|"(?=[A-Za-z\'][^"]{0,40}"))+?)"',seg)
    row=norm(R[m.group(1)])
    for frag in q:
        parts=[norm(p) for p in frag.split('[...]') if norm(p)]
        ok=all(p in row for p in parts)
        if not ok:
            bad+=1; print('CHECK', m.group(1), '|', frag[:120])
print('fragments flagged', bad)

import csv,re,sys
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open(sys.argv[1],encoding='utf-8').read()
def norm(x): return re.sub(r'\s+',' ',x).strip()
bad=0; n=0; frag=0
eids=re.findall(r'\[E\d-\d+\]',t)
if eids: print('E-ids found:',eids); bad+=1
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t):
    n+=1; i=m.group(1)
    if i not in rows: print('MISSING',i); bad+=1; continue
    # the quoted fragment immediately before this id (within 400 chars, no other id between)
    pre=t[max(0,m.start()-500):m.start()]
    pre=pre.split('**[')[-1] if '**[' in pre else pre
    qs=re.findall(r'"([^"]{6,})"',pre)
    if not qs: continue
    q=qs[-1]
    # only check if the quote ends close to the id (attached)
    tail=pre[pre.rfind('"')+1:]
    if len(tail)>14: continue
    frag+=1
    parts=[norm(p) for p in q.split('[...]') if norm(p)]
    row=norm(rows[i])
    for p in parts:
        if p not in row:
            print(f'FRAGMENT NOT IN ROW {i}: "{p}"'); bad+=1
print(f'{n} id citations, {frag} attached fragments checked, {bad} problems')

import csv,re,sys
RUN='../2026-10-06 Run - PATK Patrick Industries.md'
s=open(RUN,encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('../../principle_ledger_v5.csv',encoding='utf-8-sig'))}
def norm(t):
    t=t.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('�',"'")
    return re.sub(r'\s+',' ',t).strip().lower()
bad=0
print('em dashes:',s.count('—'),' en dashes:',s.count('–'))
ids=re.findall(r'\*\*\[([A-Z][0-9A-Z-]+)\]\*\*',s)
for e in [i for i in ids if i.startswith('E')]: print('E-ID',e); bad+=1
for i in sorted(set(ids)):
    if not re.match(r'^[MLR]\d{4}-\d{3}$',i) or i not in rows: print('MISSING',i); bad+=1
# fragment check: for each id occurrence, quoted strings in the 300 chars before it (same paragraph)
flat=re.sub(r'\s+',' ',s)
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',flat):
    i=m.group(1); pre=flat[max(0,m.start()-320):m.start()]
    pre=pre.split('**[')[-1] if '**[' in pre else pre   # stop at previous id
    q=[k for k,c in enumerate(pre) if c=='"']
    if len(q)<2:
        print('NO FRAGMENT before',i,'|',pre[-90:]); continue
    f=pre[q[-2]+1:q[-1]]
    if len(pre)-q[-1]>60: print('FRAGMENT FAR from',i,'| tail:',pre[q[-1]:][:80])
    ok=all(norm(p) in norm(rows[i]) for p in f.split('[...]') if p.strip())
    if not ok: print('FRAGMENT NOT IN ROW',i,'|',f); bad+=1
print('ids:',len(ids),'distinct:',len(set(ids)),'problems:',bad)

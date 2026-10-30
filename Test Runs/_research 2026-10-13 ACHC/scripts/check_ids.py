import csv,re,sys
run=open(sys.argv[1],encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2],encoding='utf-8-sig'))}
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('�','')
    return re.sub(r'\s+',' ',s).strip().lower()
bad=0
if re.search(r'\bE\d-\d+\b|\[E\d',run): print('E-id found'); bad+=1
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id',i); bad+=1
# quoted fragments immediately before an id (within the same paragraph, the last "..." before the id)
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run):
    i=m.group(1); pre=run[max(0,m.start()-600):m.start()]
    # take text after the previous id marker
    pre=re.split(r'\*\*\[[MLR]\d{4}-\d{3}\]\*\*',pre)[-1]
    if pre.count('"')<2: continue
    e=pre.rfind('"'); s=pre.rfind('"',0,e); f=pre[s+1:e]
    if len(f)<6: continue
    # only check fragments directly attached (within 12 chars of the id)
    tail=pre[pre.rfind('"')+1:]
    if len(tail.strip())>12: continue
    q=norm(rows.get(i,''))
    for piece in f.split('[...]'):
        piece=norm(piece).strip(' .,;')
        if piece and piece not in q: print('FRAGMENT NOT IN ROW',i,'|',piece[:120]); bad+=1
print('ids cited:',len(set(ids)),'problems:',bad)

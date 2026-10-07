import sys,re
f,marker,count=sys.argv[1],sys.argv[2],int(sys.argv[3])
occ=int(sys.argv[4]) if len(sys.argv)>4 else -1
L=open(f,encoding='utf-8').read().split('\n')
idx=[i for i,l in enumerate(L) if marker in l][occ]
rows=[];cur=None
for l in L[idx:idx+count*25]:
    toks=[t.strip() for t in l.split('|') if t.strip() and t.strip()!='$']
    for t in toks:
        if re.search(r'[A-Za-z]',t) and not re.fullmatch(r'\(?\s*[\d,\.]+\s*\)?',t):
            if cur: rows.append(cur)
            cur=[t]
        else:
            if cur is None: cur=['']
            cur.append(t)
    if len(rows)>count: break
if cur: rows.append(cur)
for r in rows[:count]: print(' | '.join(r))

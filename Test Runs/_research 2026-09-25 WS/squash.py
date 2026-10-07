import sys,re
t=open(sys.argv[1],encoding='utf-8').read()
lines=[l.strip() for l in t.split('\n')]
out=[];buf=[]
for l in lines:
    if l in ('','|','​','​ |','$ |','$','% |','%'): 
        if l.startswith('$') or l.startswith('%'): buf.append(l.rstrip('|').strip())
        continue
    if len(l)<60:
        buf.append(l.rstrip('|').strip())
    else:
        if buf: out.append(' '.join(buf)); buf=[]
        out.append(l)
if buf: out.append(' '.join(buf))
open(sys.argv[2],'w',encoding='utf-8').write('\n'.join(out))

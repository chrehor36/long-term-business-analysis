import sys,re
t=open(sys.argv[1],encoding='utf-8').read().split('\n')
a,b=int(sys.argv[2]),int(sys.argv[3])
out=[];buf=[]
for l in t[a-1:b]:
    s=l.strip()
    if s in ('|',''): continue
    if s.startswith('|') or len(s)<25 and not s.endswith('.'):
        buf.append(s.strip('| ').strip()); continue
    if buf: out.append(' | '.join(x for x in buf if x)); buf=[]
    out.append(s)
if buf: out.append(' | '.join(x for x in buf if x))
print('\n'.join(out))

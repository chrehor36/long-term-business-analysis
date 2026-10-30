import sys,re
f,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
L=open(f,encoding='utf-8').read().split('\n')[a-1:b]
out=[];cur=''
for l in L:
    s=l.strip()
    if s in ('|',''): continue
    if s.endswith('|'):
        cur+=' '+s.rstrip('|').strip()
    else:
        if cur: out.append(cur.strip()); cur=''
        out.append(s)
if cur: out.append(cur.strip())
txt='\n'.join(out)
txt=re.sub(r'\$\s+','$',txt); txt=re.sub(r'\(\s+','(',txt)
print(txt)

import sys,re
f,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
L=open(f,encoding='utf-8').read().split('\n')[a-1:b]
t=' '.join(L)
t=re.sub(r'\$\s*\|','',t); t=re.sub(r'\|\s*\)',')',t)
cells=[c.strip() for c in t.split('|')]
cells=[c for c in cells if c]
out=[];cur=[]
for c in cells:
    if re.fullmatch(r'[\(\-—]?[\d,\.]+\)?|—|\([\d,\.]+\)',c): cur.append(c)
    else:
        if cur or out: out.append(cur)
        out.append(c); cur=[]
s=''
for x in out:
    if isinstance(x,list): s+='  '+'  '.join(x)+'\n'
    else: s+=x
print(s)

import sys,re
src=sys.argv[1]; out=sys.argv[2]
L=open(src,encoding='utf-8').read().split('\n')
res=[];buf=[]
for l in L:
    s=l.replace('​','').strip()
    s=re.sub(r'^\|\s*','',s).strip()
    if s in ('','|','$','%',')'): 
        continue
    if len(s)<40 and not s.endswith('.'):
        buf.append(s)
    else:
        if buf: res.append(' '.join(buf)); buf=[]
        res.append(s)
if buf: res.append(' '.join(buf))
txt='\n'.join(res)
txt=re.sub(r'\( ([\d.,]+) \)',r'(\1)',txt)
open(out,'w',encoding='utf-8').write(txt)
print(out,len(res))

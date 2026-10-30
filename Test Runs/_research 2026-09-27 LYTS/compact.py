import sys,re
sys.stdout.reconfigure(encoding='utf-8')
fn,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
L=open(fn,encoding='utf-8').read().split('\n')[a-1:b]
out=[];cur=''
for x in L:
    s=x.strip()
    if s in ('|','$ |','$','','(',')','%'): 
        if s in ('(',')'): cur+=s
        continue
    s=s.rstrip('|').strip()
    s=re.sub(r'^\$\s*\|?\s*','',s)
    if re.match(r'^[\(\-–—]?[\d,\.]+\)?$',s) or s in ('-','—','–'):
        cur+=' '+s
    else:
        if cur: out.append(cur)
        cur=s
out.append(cur)
print('\n'.join(out))

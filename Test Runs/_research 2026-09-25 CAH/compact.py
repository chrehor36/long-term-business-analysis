import sys,re,io
f=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3])
L=io.open(f,encoding='utf-8').read().split('\n')[a-1:b]
out=[];cur=''
for l in L:
    s=l.strip().strip('|').strip()
    s=re.sub(r'\(\s+','(',s)
    if not s or s in ('$','%',')','(','|'):
        if s==')': cur+=')'
        continue
    if re.fullmatch(r'[\(\)\d,\.\-—–%\s�]+',s):
        cur+=' '+s
    else:
        if cur: out.append(cur)
        cur=s
out.append(cur)
print('\n'.join(x[:1800] for x in out))

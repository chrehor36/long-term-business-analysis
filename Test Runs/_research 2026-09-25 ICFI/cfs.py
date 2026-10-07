import sys,re,io
f=sys.argv[1]; key=sys.argv[2] if len(sys.argv)>2 else 'STATEMENTS OF CASH FLOWS'; n=int(sys.argv[3]) if len(sys.argv)>3 else 0
L=io.open(f,encoding='utf-8').read().split('\n')
idx=[i for i,l in enumerate(L) if key.lower() in l.lower()]
print('hits',idx)
i=idx[n]
out=[];cur=''
for l in L[i:i+900]:
    s=l.strip().strip('|').strip()
    if not s or s in ('$','%',')','(',''): 
        if s==')': cur+=')'
        continue
    if re.fullmatch(r'[\(\)\d,\.\-—–]+\)?',s):
        cur+=' '+s
    else:
        if cur: out.append(cur)
        cur=s
out.append(cur)
print('\n'.join(out))

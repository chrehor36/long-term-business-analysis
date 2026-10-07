import re,glob
def nums(line):
    s=line.replace('$','').replace('|',' ').replace(',','')
    s=re.sub(r'\(\s*([\d.]+)\s*\)?',r'-\1',s)
    return [float(x) for x in re.findall(r'-?\d+\.\d+|-?\d+',s)]
for f in sorted(glob.glob('10K_FY20*.txt')):
    L=open(f,encoding='utf-8').read().split('\n')
    idx=[i for i,l in enumerate(L) if re.search(r'CONSOLIDATED STATEMENTS OF (INCOME|OPERATIONS)',l)]
    # choose the one followed by 'REVENUE' within 6 lines
    st=None
    for i in idx:
        if any(re.match(r'\s*REVENUES?:',L[j]) for j in range(i,i+8)): st=i;break
    if st is None: print(f,'no IS');continue
    yrs=nums(' '.join(L[st+2:st+5]))
    yrs=[int(y) for y in yrs if 2000<y<2030][:3]
    out={}
    sec=None
    for l in L[st:st+40]:
        if re.match(r'\s*REVENUES?:',l): sec='R'
        elif re.match(r'\s*COST OF SALES',l): sec='C'
        k=None
        for key in ['New vehicle','Used vehicle','Parts and service','Finance and insurance']:
            if l.strip().startswith(key): k=key
        if k and sec:
            v=nums(l)[-3:]
            out[(sec,k)]=v
    print(f,yrs)
    for k,v in out.items(): print('  ',k,v)

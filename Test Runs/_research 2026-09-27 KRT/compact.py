import sys,re
for fn in sys.argv[1:]:
    s=open(fn,encoding='utf-8').read()
    s=s.replace('​','')
    lines=[l.strip() for l in s.split('\n')]
    out=[];buf=[]
    for l in lines:
        if l in ('','|','$','%',')','$ |','% |',') |'):
            if l.startswith('$') or l.startswith('%') or l.startswith(')'): buf.append(l.strip(' |'))
            continue
        # join short numeric/pipe fragments to previous line
        if re.fullmatch(r'[\(\)\d,.\-—–%$| ]+',l) and out:
            out[-1]+=' '+l.strip(' |'); continue
        out.append(l)
    open(fn.replace('.txt','_c.txt'),'w',encoding='utf-8').write('\n'.join(out))
    print(fn,len(out))

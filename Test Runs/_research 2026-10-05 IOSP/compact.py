import sys,re
for f in sys.argv[1:]:
    lines=[l.strip() for l in open(f,encoding='utf-8')]
    out=[];buf=''
    for l in lines:
        if not l or l=='|': continue
        if len(l)<40:
            buf+=' '+l
        else:
            if buf: out.append(buf.strip()); buf=''
            out.append(l)
    if buf: out.append(buf.strip())
    open(f.replace('.txt','_c.txt'),'w',encoding='utf-8').write('\n'.join(out))
    print(f,len(out))

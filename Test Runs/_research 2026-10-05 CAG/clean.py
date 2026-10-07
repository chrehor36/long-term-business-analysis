import sys,re
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8').read().replace('​','')
    lines=[l.strip() for l in t.split('\n')]
    out=[];buf=''
    for l in lines:
        if l in ('','|'): continue
        if l.startswith('|') or buf.endswith('|') or l.endswith('|') and len(l)<40:
            buf+=' '+l
        else:
            if buf: out.append(buf.strip())
            buf=l
    out.append(buf)
    s='\n'.join(out)
    s=re.sub(r'(\|\s*)+\|','|',s)
    open(f.replace('.txt','.c.txt'),'w',encoding='utf-8').write(s)
    print(f,len(s.split('\n')))

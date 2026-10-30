import sys,re,html
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8',errors='ignore').read()
    t=re.sub(r'(?is)<(script|style).*?</\1>','',t)
    def row(m):
        cells=re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>',m.group(0))
        cs=[]
        for c in cells:
            c=re.sub(r'<[^>]+>',' ',c); c=html.unescape(c).replace('\xa0',' ')
            c=re.sub(r'\s+',' ',c).strip()
            if c and c not in ('$',')','%'): cs.append(c)
            elif c in (')','%') and cs: cs[-1]+=c
        return '\n'+' | '.join(cs)+'\n'
    t=re.sub(r'(?is)<tr[^>]*>.*?</tr>',row,t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</h\d>','\n',t)
    t=re.sub(r'<[^>]+>',' ',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(f.rsplit('.',1)[0]+'.r.txt','w',encoding='utf-8').write(t)

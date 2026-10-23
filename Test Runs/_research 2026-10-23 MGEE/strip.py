import sys,re,html
s=open(sys.argv[1],encoding='utf-8',errors='replace').read()
s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
def row(m):
    t=m.group(0)
    cells=re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>',t)
    out=[]
    for c in cells:
        c=re.sub(r'<[^>]+>',' ',c); c=html.unescape(c).replace('\xa0',' '); c=re.sub(r'\s+',' ',c).strip()
        if c and c not in ('$',')','%'): out.append(c)
        elif c in (')','%') and out: out[-1]+=c
    return '\n'+' | '.join(out)+'\n'
s=re.sub(r'(?is)<tr[^>]*>.*?</tr>',row,s)
s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</h\d>','\n',s)
s=re.sub(r'<[^>]+>','',s)
s=html.unescape(s).replace('\xa0',' ')
s=re.sub(r'[ \t]+',' ',s)
s=re.sub(r'\n\s*\n+','\n',s)
open(sys.argv[2],'w',encoding='utf-8').write(s)

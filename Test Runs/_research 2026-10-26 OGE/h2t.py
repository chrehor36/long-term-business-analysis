import sys,re,html
s=open(sys.argv[1],encoding='utf-8',errors='ignore').read()
s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
s=re.sub(r'(?is)<ix:header>.*?</ix:header>','',s)
def row(m):
    cells=re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>',m.group(0))
    out=[]
    for c in cells:
        t=re.sub(r'<[^>]+>',' ',c); t=html.unescape(t).replace('\xa0',' '); t=re.sub(r'\s+',' ',t).strip()
        if t in ('','$','%',')'):
            if t==')' and out: out[-1]+=')'
            elif t=='%' and out: out[-1]+='%'
            continue
        out.append(t)
    return '\n'+' | '.join(out)+'\n' if out else '\n'
s=re.sub(r'(?is)<tr[^>]*>.*?</tr>',row,s)
s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</h\d>','\n',s)
s=re.sub(r'<[^>]+>','',s)
s=html.unescape(s).replace('\xa0',' ')
s=re.sub(r'[ \t]+',' ',s)
s=re.sub(r'\n\s*\n+','\n',s)
open(sys.argv[2],'w',encoding='utf-8').write(s)

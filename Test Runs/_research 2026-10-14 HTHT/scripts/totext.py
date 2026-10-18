import sys, re, html
def conv(s):
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?is)<ix:header>.*?</ix:header>','',s)
    # table rows: collapse
    def row(m):
        cells=re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>',m.group(0))
        out=[]
        for c in cells:
            c=re.sub(r'<[^>]+>','',c); c=html.unescape(c)
            c=re.sub(r'[\s​\xa0]+',' ',c).strip()
            if c and c not in ('$','%','(',')','US$','RMB'): out.append(c)
            elif c in (')','%') and out: out[-1]+=c
        return '\n'+' | '.join(out)+'\n' if out else '\n'
    s=re.sub(r'(?is)<tr[^>]*>.*?</tr>',row,s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</h\d>|</li>','\n',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s)
    s=re.sub(r'[ \t\xa0​]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
src,dst=sys.argv[1],sys.argv[2]
open(dst,'w',encoding='utf-8').write(conv(open(src,encoding='utf-8',errors='replace').read()))

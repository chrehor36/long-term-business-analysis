import re, html, sys
def clean(s):
    s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s); s=re.sub(r'[\s\xa0]+',' ',s).strip(); return s
def table(m):
    t=m.group(0); rows=[]
    for tr in re.findall(r'(?is)<tr.*?</tr>',t):
        cells=[clean(c) for c in re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>',tr)]
        cells=[c for c in cells if c not in ('','$',')','%')]
        if cells: rows.append(' | '.join(cells))
    return '\n[TABLE]\n'+'\n'.join(rows)+'\n[/TABLE]\n'
def conv(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?is)<ix:header>.*?</ix:header>',' ',s)
    s=re.sub(r'(?is)<table.*?</table>',table,s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</h\d>','\n',s)
    s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s)
    s=re.sub(r'[ \t\xa0]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
    return s
for f in sys.argv[1:]:
    open(f.replace('.txt.raw','.t2.txt'),'w',encoding='utf-8').write(conv(open(f,'rb').read()))

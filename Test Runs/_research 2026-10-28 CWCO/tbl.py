import sys,re,html
def clean(s):
    s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s).replace('\xa0',' ').replace('​','')
    return re.sub(r'\s+',' ',s).strip()
def flat(path,out):
    b=open(path,'rb').read().decode('utf-8','replace')
    b=re.sub(r'(?is)<(script|style).*?</\1>',' ',b)
    def tr(m):
        cells=[clean(c) for c in re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>',m.group(0))]
        cells=[c for c in cells if c not in ('','$','%',')')]
        return '\n'+' | '.join(cells)+'\n'
    b=re.sub(r'(?is)<tr[^>]*>.*?</tr>',tr,b)
    b=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</h\d>','\n',b)
    b=re.sub(r'<[^>]+>',' ',b); b=html.unescape(b).replace('\xa0',' ').replace('​','')
    b=re.sub(r'[ \t]+',' ',b); b=re.sub(r'\n\s*\n+','\n',b)
    open(out,'w',encoding='utf-8').write(b)
flat(sys.argv[1],sys.argv[2])

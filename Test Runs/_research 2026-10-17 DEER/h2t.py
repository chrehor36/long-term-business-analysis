import sys,re,html,os
src=sys.argv[1]
for f in os.listdir(src):
    if not f.endswith('.htm'): continue
    t=open(os.path.join(src,f),encoding='latin-1').read()
    t=re.sub(r'(?is)<(script|style).*?</\1>','',t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>|</th>',' | ',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n',t)
    open(os.path.join(src,f[:-4]+'.txt'),'w',encoding='utf-8').write(t)

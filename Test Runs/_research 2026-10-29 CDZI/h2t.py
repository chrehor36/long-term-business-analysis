import sys,re,html
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8',errors='ignore').read()
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',s)
    s=re.sub(r'(?i)</td>',' | ',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
    open(f.replace('.htm','.txt'),'w',encoding='utf-8').write(s)

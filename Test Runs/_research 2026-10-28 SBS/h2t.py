import sys,re,html
for p in sys.argv[1:]:
    t=open(p,encoding='utf-8',errors='replace').read()
    t=re.sub(r'(?is)<(script|style).*?</\1>','',t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>','\t',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n',t)
    open(p.rsplit('.',1)[0]+'.txt','w',encoding='utf-8').write(t)
    print(p,len(t.splitlines()))

import sys,re,html,glob,os
for f in glob.glob(os.path.join(sys.argv[1],'*.htm')):
    t=open(f,encoding='utf-8',errors='replace').read()
    t=re.sub(r'(?is)<(script|style).*?</\1>','',t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>','\n',t)
    t=re.sub(r'(?i)</td>',' | ',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(f[:-4]+'.txt','w',encoding='utf-8').write(t)

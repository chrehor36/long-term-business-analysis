import sys,re,html
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8',errors='ignore').read()
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?i)</(tr|p|div|br|li|h\d)>','\n',s)
    s=re.sub(r'(?i)</t[dh]>',' | ',s)
    s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s)
    s=re.sub(r'[ \t\xa0]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
    open(f[:-4]+'.txt','w',encoding='utf-8').write(s)

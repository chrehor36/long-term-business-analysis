import sys,re,html
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8',errors='replace').read()
    s=re.sub(r'(?is)<(script|style|ix:header).*?</\1>','',s)
    s=re.sub(r'\s+',' ',s)
    s=re.sub(r'(?i)</(p|div|tr|h\d|li|table)>|<br\s*/?>','\n',s)
    s=re.sub(r'(?i)</t[dh]>','|',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'(\s*\|\s*)+','|',s)
    s=re.sub(r'\n\s*\|?\s*\n+','\n',s); s=re.sub(r'\n\s*\n+','\n',s)
    open(f.rsplit('.',1)[0]+'.txt','w',encoding='utf-8').write(s)

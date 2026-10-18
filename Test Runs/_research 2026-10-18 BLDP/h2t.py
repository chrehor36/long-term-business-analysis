import sys,re,html
def conv(src,dst):
    s=open(src,encoding='utf-8',errors='replace').read()
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?i)<br\s*/?>','\n',s)
    s=re.sub(r'(?i)</(p|div|tr|h\d|li|table)>','\n',s)
    s=re.sub(r'(?i)</t[dh]>',' | ',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    open(dst,'w',encoding='utf-8').write(s)
for a in sys.argv[1:]:
    conv(a,a.rsplit('.',1)[0]+'.txt')

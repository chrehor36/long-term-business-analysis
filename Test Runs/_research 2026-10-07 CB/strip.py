import sys, re, html
def strip(h):
    h=re.sub(r'(?is)<(script|style).*?</\1>',' ',h)
    h=re.sub(r'(?is)<ix:header>.*?</ix:header>',' ',h)
    h=re.sub(r'(?i)<br\s*/?>','\n',h)
    h=re.sub(r'(?i)</(p|div|tr|li|h\d|table)>','\n',h)
    h=re.sub(r'(?i)</t[dh]>',' | ',h)
    h=re.sub(r'<[^>]+>','',h)
    h=html.unescape(h).replace('\xa0',' ')
    h=re.sub(r'[ \t]+',' ',h)
    h=re.sub(r'\n\s*\n+','\n',h)
    return h
src,dst=sys.argv[1],sys.argv[2]
open(dst,'w',encoding='utf-8').write(strip(open(src,encoding='utf-8',errors='replace').read()))

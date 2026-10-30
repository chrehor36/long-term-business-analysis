import re,sys,html
src,dst=sys.argv[1],sys.argv[2]
s=open(src,encoding='utf-8',errors='replace').read()
s=re.sub(r'(?is)<(script|style|head)[^>]*>.*?</\1>',' ',s)
s=re.sub(r'(?is)</(tr|p|div|table|h[1-6]|li)>','\n',s)
s=re.sub(r'(?is)</t[dh]>',' | ',s)
s=re.sub(r'(?s)<[^>]+>',' ',s)
s=html.unescape(s)
s=s.replace('\xa0',' ')
s=re.sub(r'[ \t]+',' ',s)
s=re.sub(r' *\n *','\n',s)
s=re.sub(r'\n{3,}','\n\n',s)
open(dst,'w',encoding='utf-8').write(s)
print(dst,len(s))

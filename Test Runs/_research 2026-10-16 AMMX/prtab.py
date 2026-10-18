import re,html,sys
s=open(sys.argv[1],encoding='utf-8',errors='replace').read()
s=re.sub(r'(?is)<(script|style).*?</\1>','',s); s=re.sub(r'\s+',' ',s)
s=re.sub(r'(?i)</t[dh]>','|',s); s=re.sub(r'(?i)</tr>|</p>','\n',s); s=re.sub(r'<[^>]+>','',s); s=html.unescape(s)
s=re.sub(r'\|\s*(\|\s*)+','|',s)
a=s.find(sys.argv[2]) if len(sys.argv)>2 else 0
b=s.find('Get News by Email')
print(s[max(a,0):b if b>0 else None])

import sys,re
t=open(sys.argv[1],encoding='utf-8').read()
idx=[m.start() for m in re.finditer(r'(?i)consolidated balance sheets', t)]
# pick occurrence followed by 'ASSETS' within 600 chars
for i in idx:
    seg=t[i:i+9000]
    if re.search(r'(?i)total assets',seg[:6000]) and re.search(r'(?i)real estate',seg[:3000]):
        s=re.sub(r'\s*\|\s*',' ',seg); s=re.sub(r'\n+','\n',s); s=re.sub(r' +',' ',s)
        print(s[:5000]); break

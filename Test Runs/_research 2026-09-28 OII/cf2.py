import re,sys
y=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 5000
s=open(f'cache/k{y}.txt',encoding='utf-8').read()
ms=[m.start() for m in re.finditer(r'(?i)CONSOLIDATED STATEMENTS OF CASH FLOWS',s)]
for i in ms:
    t=s[i:i+n]
    if re.search(r'(?i)depreciation',t[:3000]):
        t=re.sub(r'[ \t|$]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t); print(t); break

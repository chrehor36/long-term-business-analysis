import sys,re
f,pat=sys.argv[1],sys.argv[2]; n=int(sys.argv[3]) if len(sys.argv)>3 else 3000; k=int(sys.argv[4]) if len(sys.argv)>4 else 3
s=open(f,encoding='utf-8',errors='ignore').read(); s=re.sub(r'[\s|]+',' ',s)
for i,m in enumerate(re.finditer(pat,s,re.I)):
    if i>=k: break
    print('=== @',m.start()); print(s[m.start():m.start()+n])

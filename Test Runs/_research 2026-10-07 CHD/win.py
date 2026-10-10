import sys,re
pat=sys.argv[1]; w=int(sys.argv[2]); mx=int(sys.argv[3])
for f in sys.argv[4:]:
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\s*\|\s*',' ',t); t=re.sub(r'\s+',' ',t)
    print('==',f)
    for i,m in enumerate(re.finditer(pat,t,flags=re.I)):
        if i>=mx: break
        print('  >',t[m.start():m.start()+w])

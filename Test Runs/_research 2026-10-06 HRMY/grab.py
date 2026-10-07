import re,sys
f,pat,n,w=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
s=open(f,encoding='utf-8').read()
for m in list(re.finditer(pat,s))[:n]:
    sys.stdout.buffer.write((s[max(0,m.start()-150):m.start()+w]+'\n..\n').encode('utf-8'))

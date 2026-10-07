import sys,re
fn=sys.argv[1]; pat=sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 300; mx=int(sys.argv[4]) if len(sys.argv)>4 else 20
s=open(fn,encoding='utf-8').read()
s=re.sub(r'\s+',' ',s)
n=0
for m in re.finditer(pat,s,re.I):
    print('...',s[max(0,m.start()-w):m.end()+w],'...\n')
    n+=1
    if n>=mx: break

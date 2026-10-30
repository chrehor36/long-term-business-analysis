import io,sys; sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8",errors="replace")
import re,sys
f=sys.argv[1]; pat=sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 300; mx=int(sys.argv[4]) if len(sys.argv)>4 else 20
s=open(f,encoding='utf-8').read()
n=0
for m in re.finditer(pat,s,re.I):
    a=max(0,m.start()-w); b=min(len(s),m.end()+w)
    print('@%d: %s'%(m.start(), s[a:b].replace('\n',' / ')));print('---')
    n+=1
    if n>=mx: break

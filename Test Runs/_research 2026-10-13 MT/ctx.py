import re,sys
import io; sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8",errors="replace")
fn=sys.argv[1]; pat=sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 600; mx=int(sys.argv[4]) if len(sys.argv)>4 else 20
t=open(fn,encoding='utf-8').read().replace('\n',' ')
t=re.sub(r' +',' ',t)
n=0
for m in re.finditer(pat,t,flags=re.I):
    print(f'@{m.start()}: ...'+t[max(0,m.start()-w//3):m.start()+w]+'...\n')
    n+=1
    if n>=mx: break

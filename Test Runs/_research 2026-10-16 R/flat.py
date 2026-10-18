import sys,re
import io; sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
lines=open(sys.argv[1],encoding='utf-8').read().split('\n')[int(sys.argv[2]):int(sys.argv[3])]
out=[];cur=''
for l in lines:
    s=l.strip().strip('|').strip()
    if not s: continue
    if re.fullmatch(r"[\$\(\)\d,.\-—%\s|]+",s):
        cur+=' '+s.replace('|',' ')
    else:
        if cur: out.append(cur)
        cur=s
out.append(cur)
for o in out: print(re.sub(r'\s+',' ',o).replace('( ','(').replace(' )',')'))

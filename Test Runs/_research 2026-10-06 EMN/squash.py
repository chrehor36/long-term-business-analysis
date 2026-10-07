import sys,re
lines=[l.strip() for l in open(sys.argv[1],encoding='utf-8')]
a,b=int(sys.argv[2]),int(sys.argv[3])
out=[];buf=''
for l in lines[a-1:b]:
    if not l: continue
    if re.fullmatch(r'[-0-9(),.$%— ]+',l) or len(l)<4:
        buf+=' '+l
    else:
        if buf: out.append(buf.strip())
        buf=l
out.append(buf)
w=int(sys.argv[4]) if len(sys.argv)>4 else 1500
for o in out: print(o[:w])

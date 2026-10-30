import sys,re
f,start,n=sys.argv[1],sys.argv[2],int(sys.argv[3])
s=open(f,encoding='utf-8').read()
s=re.sub(r'[ \t|]*\n[ \t|\n]*',' ',s); s=re.sub(r'\s+',' ',s)
occ=int(sys.argv[4]) if len(sys.argv)>4 else 0
i=-1
for _ in range(occ+1): i=s.find(start,i+1)
print(s[i:i+n])

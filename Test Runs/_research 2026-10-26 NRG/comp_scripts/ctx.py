import sys,re
f=sys.argv[1]; pat=re.compile(sys.argv[2],re.I); after=int(sys.argv[3]) if len(sys.argv)>3 else 6; mx=int(sys.argv[4]) if len(sys.argv)>4 else 3
L=open(f,encoding='utf-8').read().split('\n'); n=0
for i,l in enumerate(L):
  if pat.search(l):
    print(f'--- {i+1}'); 
    for x in L[i:i+after+1]: print('   ',x[:260])
    n+=1
    if n>=mx: break

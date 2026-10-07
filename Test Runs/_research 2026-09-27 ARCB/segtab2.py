import re,sys
sys.stdout.reconfigure(encoding='utf-8')
y,anchor,n=sys.argv[1],sys.argv[2],int(sys.argv[3])
L=open('cache/tenk_%s.txt'%y,encoding='utf-8').read().split('\n')
for i,l in enumerate(L):
    if l.strip()==anchor:
        blk=' '.join(L[i-8:i+n]); blk=re.sub(r'\s*\|\s*',' ',blk).replace('​',' '); blk=re.sub(r'\s+',' ',blk)
        print('=====',y,i); print(blk[:3000]); break

import re,sys
sys.stdout.reconfigure(encoding='utf-8')
for y in sys.argv[1:]:
    L=open('cache/tenk_%s.txt'%y,encoding='utf-8').read().split('\n')
    for i,l in enumerate(L):
        if l.strip()=='REVENUES' or l.strip().startswith('REVENUES'):
            blk=' '.join(L[i-8:i+260])
            blk=re.sub(r'\s*\|\s*',' ',blk).replace('​',' ')
            blk=re.sub(r'\s+',' ',blk)
            print('=====',y,i); print(blk[:3800]); break

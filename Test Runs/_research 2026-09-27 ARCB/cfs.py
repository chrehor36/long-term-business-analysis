import re,sys
sys.stdout.reconfigure(encoding='utf-8')
for y in sys.argv[1:]:
    L=open('cache/tenk_%s.txt'%y,encoding='utf-8').read().split('\n')
    idx=[i for i,l in enumerate(L) if l.strip().upper().startswith('OPERATING ACTIVITIES')]
    i=idx[0]
    blk=' '.join(L[i-30:i+700]); blk=re.sub(r'\s*\|\s*',' ',blk).replace('​',' '); blk=re.sub(r'\s+',' ',blk)
    e=blk.find('See notes')
    print('=====',y); print(blk[:e if e>0 else 8000][:9000])

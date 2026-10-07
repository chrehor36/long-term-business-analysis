import re
R='C:/Users/chreh/OneDrive/Documents/BRK/'; M=R+'Test Runs/_research 2026-09-26 SXC/'
# 1. register entry, by line
p=R+'Screens/WATCHLIST RUN QUEUE.md'
raw=open(p,'rb').read(); crlf=b'\r\n' in raw; nl='\r\n' if crlf else '\n'
L=raw.decode('utf-8').split(nl)
def count(L):
    h=[i for i,l in enumerate(L) if l=='## COMPLETED FROM THE QUEUE']; e=[i for i,l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
    assert len(h)==1 and len(e)==1,(h,e)
    return h[0],[l for l in L[h[0]+1:e[0]] if l.startswith('- **')]
h,before=count(L)
assert not any(l.startswith('- **SXC ') for l in before)
new=open(M+'_reg_entry.md',encoding='utf-8').read().rstrip('\n').split('\n')
L=L[:h+1]+new+L[h+1:]
h2,after=count(L)
print('queue crlf',crlf,'heading line',h+1,'before',len(before),'after',len(after),'first',after[0][:30])
assert len(after)==len(before)+1 and after[0].startswith('- **SXC ') and after[1].startswith('- **WSM ')
open(p,'wb').write(nl.join(L).encode('utf-8'))
def append(path,addition):
    raw=open(path,'rb').read(); crlf=b'\r\n' in raw; nl='\r\n' if crlf else '\n'; t=raw.decode('utf-8')
    if not t.endswith(nl): t+=nl
    open(path,'wb').write((t+addition.replace('\r\n','\n').rstrip('\n').replace('\n',nl)+nl).encode('utf-8'))
    print(path.split('/')[-1],'crlf',crlf)
# 2. done file
dp=R+'Screens/_daily/_wave7_done.txt'
d=[x.strip() for x in open(dp) if x.strip()]; assert len(d)==50 and d[-1]=='WSM' and 'SXC' not in d
append(dp,'SXC'); d2=[x.strip() for x in open(dp) if x.strip()]; print('done lines',len(d2),d2[-2:])
# 3. shape note
sp=R+'Screens/SURVIVAL SHAPES - index.md'; st=open(sp,encoding='utf-8').read()
rows=re.findall(r'^\| (\d+) \|',st,re.M); print('shape rows',len(rows),'max',max(int(x) for x in rows))
assert len(rows)==30 and max(int(x) for x in rows)==30 and 'the SXC fold' not in st
append(sp,'\n'+open(M+'_shape_note.md',encoding='utf-8').read())
# 4. narrative fold
fp=R+'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'; ft=open(fp,encoding='utf-8').read()
assert 'UPDATE 2026-09-26 - SXC' not in ft
append(fp,open(M+'_fold.md',encoding='utf-8').read())

import re
p='../../Screens/WATCHLIST RUN QUEUE.md'
b=open(p,'rb').read(); assert b.count(b'\r\n')==b.count(b'\n')
L=b.decode('utf-8').split('\r\n')
def count(L):
    h=[i for i,l in enumerate(L) if l=='## COMPLETED FROM THE QUEUE']
    w=[i for i,l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
    assert len(h)==1 and len(w)==1,(h,w)
    ent=[l for l in L[h[0]+1:w[0]] if re.match(r'^- \*\*[A-Z0-9]',l)]
    return h[0],w[0],ent
h,w,ent=count(L)
print('before: heading line',h+1,'write-early line',w+1,'entries',len(ent),'first',ent[0][:12],'JJSF',sum(1 for l in ent if l.startswith('- **JJSF')))
assert L[h+1].startswith('- **IPAR')
entry=open('register_entry.md',encoding='utf-8').read().rstrip('\n').split('\n')
L=L[:h+1]+entry+L[h+1:]
open(p,'wb').write('\r\n'.join(L).encode('utf-8'))
L=open(p,'rb').read().decode('utf-8').split('\r\n')
h,w,ent=count(L)
print('after: heading line',h+1,'write-early line',w+1,'entries',len(ent),'first',ent[0][:12],'second',ent[1][:12],'JJSF',sum(1 for l in ent if l.startswith('- **JJSF')))
# reading list
p2='../../Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
b=open(p2,'rb').read(); assert b.endswith(b'\r\n')
note=open('fold_note.md',encoding='utf-8').read().replace('\n','\r\n').encode('utf-8')
open(p2,'wb').write(b+note)
# done file
d='../../Screens/_daily/_wave7_done.txt'
t=open(d,'rb').read(); nl=b'\r\n' if b'\r\n' in t else b'\n'
if not t.endswith(nl): t+=nl
open(d,'wb').write(t+b'JJSF'+nl)
lines=open(d,encoding='utf-8').read().splitlines()
print('done lines',len(lines),'last',lines[-1],'JJSF count',lines.count('JJSF'),'NDSN done?',lines.count('NDSN'))
o=open('../../Screens/_daily/_wave7_order.txt',encoding='utf-8').read().split()
nxt=[x for x in o if x not in set(lines)][0]; print('next not done:',nxt, 'remaining', len([x for x in o if x not in set(lines)]))

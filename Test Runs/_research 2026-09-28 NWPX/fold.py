import re
Q='../../Screens/WATCHLIST RUN QUEUE.md'
raw=open(Q,encoding='utf-8',newline='').read()
nl='\r\n' if '\r\n' in raw else '\n'
L=raw.split(nl)
def count(L):
    h=[i for i,l in enumerate(L) if l=='## COMPLETED FROM THE QUEUE']
    w=[i for i,l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
    assert len(h)==1 and len(w)==1
    ent=[l for l in L[h[0]+1:w[0]] if l.startswith('- **')]
    return h[0], ent
h, ent=count(L); before=len(ent)
assert not any(e.startswith('- **NWPX') for e in ent)
entry=open('register_entry.md',encoding='utf-8').read().rstrip('\n').split('\n')
assert L[h+1].startswith('- **POWL'), L[h+1][:40]
L=L[:h+1]+entry+L[h+1:]
h2, ent2=count(L)
assert len(ent2)==before+1 and ent2[0].startswith('- **NWPX') and ent2[1].startswith('- **POWL'), (len(ent2), ent2[0][:30])
assert sum(1 for e in ent2 if e.startswith('- **NWPX'))==1
open(Q,'w',encoding='utf-8',newline='').write(nl.join(L))
print('register', before, '->', len(ent2), 'heading line', h2+1)
# reading list
R='../../Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
r=open(R,encoding='utf-8',newline='').read(); rn='\r\n' if '\r\n' in r else '\n'
assert 'UPDATE 2026-09-28 - NWPX' not in r
note=open('fold_note.md',encoding='utf-8').read().replace('\n',rn)
open(R,'w',encoding='utf-8',newline='').write(r.rstrip('\r\n')+rn+note)
print('reading list ends:', repr(open(R,encoding='utf-8',newline='').read()[-40:]))
# survival shapes
S='../../Screens/SURVIVAL SHAPES - index.md'
s=open(S,encoding='utf-8',newline='').read(); sn='\r\n' if '\r\n' in s else '\n'
assert 'the NWPX fold' not in s
open(S,'w',encoding='utf-8',newline='').write(s.rstrip('\r\n')+sn+open('shape_note.md',encoding='utf-8').read().replace('\n',sn))
# done file
D='../../Screens/_daily/_wave7_done.txt'
d=open(D,encoding='utf-8',newline='').read(); dn='\r\n' if '\r\n' in d else '\n'
assert d.endswith(dn) and 'NWPX' not in d.split()
open(D,'w',encoding='utf-8',newline='').write(d+'NWPX'+dn)
dd=open(D).read().split(); o=open('../../Screens/_daily/_wave7_order.txt').read().split()
print('done', len(dd), dd[-1], 'equals order prefix', dd==o[:len(dd)], 'next', o[len(dd)])

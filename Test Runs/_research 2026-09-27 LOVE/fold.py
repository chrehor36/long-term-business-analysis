import io
Q='Screens/WATCHLIST RUN QUEUE.md'; D='Screens/_daily/_wave7_done.txt'; RL='Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
R='Test Runs/_research 2026-09-27 LOVE/'
def rd(p):
    b=io.open(p,'rb').read(); nl='\r\n' if b'\r\n' in b else '\n'; return b.decode('utf-8'),nl
def count(L):
    h=[i for i,l in enumerate(L) if l=='## COMPLETED FROM THE QUEUE']; w=[i for i,l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
    assert len(h)==1 and len(w)==1
    e=[l for l in L[h[0]+1:w[0]] if l.startswith('- **')]; return h[0],e
# 1. register
t,nl=rd(Q); L=t.split(nl)
hi,e=count(L); before=len(e); assert not any(x.startswith('- **LOVE') for x in e)
entry=io.open(R+'register_entry.md',encoding='utf-8').read().rstrip('\n').split('\n')
L=L[:hi+1]+entry+L[hi+1:]
hi2,e2=count(L); assert len(e2)==before+1 and e2[0].startswith('- **LOVE') and e2[1].startswith('- **NDSN'), (len(e2),e2[0][:20])
assert sum(1 for x in e2 if x.startswith('- **LOVE'))==1
io.open(Q,'wb').write(nl.join(L).encode('utf-8'))
print('register: heading line',hi+1,'before',before,'after',len(e2),'first',e2[0][:12])
# 2. done file
t,nl=rd(D); lines=[x for x in t.split(nl) if x!='']
assert lines[-1]=='NDSN' and 'LOVE' not in lines
io.open(D,'wb').write((t if t.endswith(nl) else t+nl).encode('utf-8')+('LOVE'+nl).encode('utf-8'))
t2,_=rd(D); l2=[x for x in t2.split(nl) if x!='']; print('done file lines',len(l2),'last',l2[-1])
# 3. reading list
t,nl=rd(RL); assert '## UPDATE 2026-09-27 - LOVE' not in t
note=io.open(R+'fold_note.md',encoding='utf-8').read().rstrip('\n')
add=nl.join(note.split('\n'))+nl
io.open(RL,'wb').write((t if t.endswith(nl) else t+nl).encode('utf-8')+add.encode('utf-8'))
t3,_=rd(RL); print('reading list ends:',repr(t3[-40:]))

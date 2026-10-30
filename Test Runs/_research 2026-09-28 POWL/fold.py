# The six-step fold for POWL. Writes by line, asserts before and after.
import re, io
ROOT='../../'
Q=ROOT+'Screens/WATCHLIST RUN QUEUE.md'
RL=ROOT+'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
DONE=ROOT+'Screens/_daily/_wave7_done.txt'
ORDER=ROOT+'Screens/_daily/_wave7_order.txt'
SH=ROOT+'Screens/SURVIVAL SHAPES - index.md'

def rd(p): return io.open(p,encoding='utf-8',newline='').read()
def wr(p,s): io.open(p,'w',encoding='utf-8',newline='').write(s)

# ---- step 1: register entry, inserted by line after the line-exact unique heading
s=rd(Q); nl='\r\n' if '\r\n' in s else '\n'
L=s.split(nl)
h=[i for i,l in enumerate(L) if l=='## COMPLETED FROM THE QUEUE']
assert len(h)==1, h
e=[i for i,l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]; assert len(e)==1
before=[l for l in L[h[0]+1:e[0]] if l.startswith('- **')]
assert len(before)==250 and before[0].startswith('- **PFGC'), (len(before), before[0][:20])
assert not any(l.startswith('- **POWL') for l in before)
entry=io.open('register_entry.md',encoding='utf-8').read().strip('\n').split('\n')
L=L[:h[0]+1]+entry+L[h[0]+1:]
s2=nl.join(L)
L2=s2.split(nl)
h2=[i for i,l in enumerate(L2) if l=='## COMPLETED FROM THE QUEUE']; assert len(h2)==1 and h2[0]==h[0]
e2=[i for i,l in enumerate(L2) if l.startswith('## THE WRITE-EARLY PROTOCOL')][0]
after=[l for l in L2[h2[0]+1:e2] if l.startswith('- **')]
assert len(after)==251 and after[0].startswith('- **POWL') and after[1].startswith('- **PFGC'), (len(after), after[0][:20])
assert sum(1 for l in after if l.startswith('- **POWL'))==1
wr(Q,s2); print('register: heading line', h[0]+1, 'before', len(before), 'after', len(after))

# ---- step 3a: done file
d=rd(DONE); dl=[x for x in d.split() if x]
o=[x for x in rd(ORDER).split() if x]
assert len(dl)==108 and dl==o[:108] and o[108]=='POWL', (len(dl), o[108])
sep='' if d.endswith('\n') else ('\r\n' if '\r\n' in d else '\n')
nl2='\r\n' if '\r\n' in d else '\n'
wr(DONE, d+sep+'POWL'+nl2)
dl2=[x for x in rd(DONE).split() if x]
assert len(dl2)==109 and dl2==o[:109]
print('done file', len(dl2), 'lines; next', o[109])

# ---- step 3b: reading-list fold (append)
r=rd(RL); nl3='\r\n' if '\r\n' in r else '\n'
assert r.rstrip().endswith('Next in the order file: POWL.')
assert '## UPDATE 2026-09-28 - POWL' not in r
frag=io.open('fold_note.md',encoding='utf-8').read().strip('\n').replace('\n',nl3)
wr(RL, r.rstrip('\r\n')+nl3+nl3+frag+nl3)
print('reading list appended')

# ---- step 5: survival-shapes dated note (count rows first)
t=rd(SH); nl4='\r\n' if '\r\n' in t else '\n'
rows=[int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \|', t)]
assert len(rows)==30 and max(rows)==30, (len(rows), max(rows))
assert 'the POWL fold' not in t
note=io.open('shape_note.md',encoding='utf-8').read().strip('\n')
wr(SH, t.rstrip('\r\n')+nl4+nl4+note+nl4)
print('shapes: rows', len(rows), 'max', max(rows), '- note appended')

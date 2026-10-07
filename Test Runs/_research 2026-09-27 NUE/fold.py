"""NUE fold: register entry by line under the line-exact heading (count before/after), done-file append, reading-list append.
Wave position counted from the done file and checked against the order file."""
import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
R='Test Runs/_research 2026-09-27 NUE/'
order=[x.strip() for x in open('Screens/_daily/_wave7_order.txt',encoding='utf-8') if x.strip()]
done=[x.strip() for x in open('Screens/_daily/_wave7_done.txt',encoding='utf-8') if x.strip()]
assert 'NUE' not in done
W=len(done)+1
assert order[W-1]=='NUE', (W, order[W-1])
nxt=order[W]; print('wave position',W,'next',nxt,'order len',len(order))
P='Screens/WATCHLIST RUN QUEUE.md'
raw=open(P,encoding='utf-8',newline='').read(); nl='\r\n' if '\r\n' in raw else '\n'
L=raw.split(nl)
H=[i for i,x in enumerate(L) if x=='## COMPLETED FROM THE QUEUE']; Wp=[i for i,x in enumerate(L) if x.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(H)==1 and len(Wp)==1 and H[0]<Wp[0]
def count(lines,h,w):
    ent=[x for x in lines[h+1:w] if re.match(r'^- \*\*',x)]
    return len(ent), sum(1 for x in ent if x.startswith('- **NUE (')), ent[0][:30] if ent else None
before=count(L,H[0],Wp[0]); print('before',before); assert before[1]==0
N=before[0]+1
entry=open(R+'register_entry.md',encoding='utf-8').read().rstrip('\n').split('\n')
entry=[e.replace('@@N@@',str(N)).replace('@@B@@',str(before[0])).replace('@@W@@',str(W)) for e in entry]
L2=L[:H[0]+1]+entry+L[H[0]+1:]
H2=[i for i,x in enumerate(L2) if x=='## COMPLETED FROM THE QUEUE']; W2=[i for i,x in enumerate(L2) if x.startswith('## THE WRITE-EARLY PROTOCOL')]
after=count(L2,H2[0],W2[0]); print('after',after)
assert after[0]==N and after[1]==1 and after[2].startswith('- **NUE (')
open(P,'w',encoding='utf-8',newline='').write(nl.join(L2))
# done file
d=open('Screens/_daily/_wave7_done.txt',encoding='utf-8',newline='').read()
assert d.endswith('\n'); open('Screens/_daily/_wave7_done.txt','a',encoding='utf-8',newline='').write('NUE\n')
# reading list
RL='Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
r=open(RL,encoding='utf-8',newline='').read(); rnl='\r\n' if '\r\n' in r else '\n'
assert r.rstrip().endswith('**Next in the order file: NUE.**')
note=open(R+'fold_note.md',encoding='utf-8').read().replace('@@N@@',str(N)).replace('@@W@@',str(W)).replace('@@NEXT@@',nxt)
if not r.endswith(rnl): r+=rnl
r+=note.replace('\n',rnl)
open(RL,'w',encoding='utf-8',newline='').write(r)
print('register entry',N,'wave',W,'done lines',len([x for x in open('Screens/_daily/_wave7_done.txt',encoding='utf-8') if x.strip()]))

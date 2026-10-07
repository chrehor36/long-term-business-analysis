import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
R='Test Runs/_research 2026-09-27 LYTS/'
def load(p):
    raw=open(p,encoding='utf-8',newline='').read(); return raw,('\r\n' if '\r\n' in raw else '\n')
# 1. register
P='Screens/WATCHLIST RUN QUEUE.md'
raw,nl=load(P); L=raw.split(nl)
H=[i for i,x in enumerate(L) if x=='## COMPLETED FROM THE QUEUE']
W=[i for i,x in enumerate(L) if x.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(H)==1 and len(W)==1 and H[0]<W[0],(H,W)
def count(lines,h,w):
    ent=[x for x in lines[h+1:w] if re.match(r'^- \*\*',x)]
    return len(ent),len([x for x in ent if x.startswith('- **LYTS ')]),ent[0][:30]
b=count(L,H[0],W[0]); print('before',b); assert b[1]==0
N=b[0]+1
e=open(R+'register_entry.md',encoding='utf-8').read().rstrip('\n').split('\n')
e=[x.replace('@@N@@',str(N)).replace('@@B@@',str(b[0])).replace('@@H@@',str(H[0]+1)) for x in e]
L2=L[:H[0]+1]+e+L[H[0]+1:]
H2=[i for i,x in enumerate(L2) if x=='## COMPLETED FROM THE QUEUE']; W2=[i for i,x in enumerate(L2) if x.startswith('## THE WRITE-EARLY PROTOCOL')]
a=count(L2,H2[0],W2[0]); print('after',a)
assert a[0]==N and a[1]==1 and a[2].startswith('- **LYTS ')
open(P,'w',encoding='utf-8',newline='').write(nl.join(L2))
# 3. reading list
P='Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
raw,nl=load(P)
assert raw.rstrip().endswith('Next in the order file: LYTS.'),raw[-60:]
assert '## UPDATE 2026-09-27 - LYTS' not in raw
note=open(R+'fold_note.md',encoding='utf-8').read().rstrip('\n').replace('@@N@@',str(N)).replace('\n',nl)
open(P,'w',encoding='utf-8',newline='').write(raw.rstrip('\r\n')+nl+nl+note+nl)
print('reading list appended')
# done file
P='Screens/_daily/_wave7_done.txt'
raw,nl=load(P); lines=[x for x in raw.split(nl) if x!='']
assert 'LYTS' not in lines and lines[-1]=='ABBV',lines[-3:]
open(P,'w',encoding='utf-8',newline='').write(raw.rstrip('\r\n')+nl+'LYTS'+nl)
raw2,_=load(P); print('done file',len(lines),'->',len([x for x in raw2.split(nl) if x!='']))
# shapes note
P='Screens/SURVIVAL SHAPES - index.md'
raw,nl=load(P); L=raw.split(nl)
rows=[x for x in L if re.match(r'^\| \d+ \|',x)]; nums=[int(re.match(r'^\| (\d+) \|',x).group(1)) for x in rows]
print('shape rows',len(rows),'max',max(nums)); assert 'the LYTS fold' not in raw
txt=('*Dated note, 2026-09-27 (the LYTS fold, wave 7 name 80): **no row was added, no number moved, and the count of distinct shapes is unchanged at 25.** '
 'The table was counted with a line-start regex immediately before writing: **%d rows, maximum number %d**. LSI Industries closed at **Q2 OUT**, so Q4 was never opened and the business has no named death. '
 'The run file names, as a signature WITHOUT a verdict, **#11 THE PASS-THROUGH** (a quoted-price maker of lighting fixtures and store fittings whose cost increases are passed on only when competitors allow: *"the lighting market remains very price competitive"*, FY2012; *"did not fully offset the increases in cost"*, FY2019; Display programmes priced at their start from then-current material cost), '
 'with **#6 THE BORROWED BALANCE SHEET** as a feature (net debt $241.7M after the Royston purchase, 7.3-19.5 times the owner-earnings range, under a leverage covenant measured on adjusted EBITDA stepping from 4.00x to 3.50x by September 2027). '
 'Not entered in the instances column, for the reason the PAGP, CALM, MRK and ABBV folds gave: entering a Q2 observation as a Q4 instance would make this index say something the run file does not.*')%(len(rows),max(nums))
open(P,'w',encoding='utf-8',newline='').write(raw.rstrip('\r\n')+nl+nl+txt+nl)
print('shapes note appended; register entry',N)

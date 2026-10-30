import re,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
ROOT='../../'
qf=ROOT+'Screens/WATCHLIST RUN QUEUE.md'
L=open(qf,encoding='utf-8').read().split('\n')
h=[i for i,x in enumerate(L) if x=='## COMPLETED FROM THE QUEUE']; assert len(h)==1,h
w=[i for i,x in enumerate(L) if x.startswith('## THE WRITE-EARLY PROTOCOL')]; assert len(w)==1,w
def count(L):
    h=[i for i,x in enumerate(L) if x=='## COMPLETED FROM THE QUEUE'][0]; w=[i for i,x in enumerate(L) if x.startswith('## THE WRITE-EARLY PROTOCOL')][0]
    return [x for x in L[h+1:w] if x.startswith('- **')]
before=count(L); assert not any(x.startswith('- **KVUE ') for x in before); assert before[0].startswith('- **CHD ')
entry=open('_reg_entry.md',encoding='utf-8').read().rstrip('\n').split('\n')
L=L[:h[0]+1]+entry+L[h[0]+1:]
after=count(L); assert after[0].startswith('- **KVUE ') and after[1].startswith('- **CHD ')
assert sum(1 for x in after if x.startswith('- **KVUE '))==1
print('register before',len(before),'after',len(after))
open(qf,'w',encoding='utf-8',newline='\n').write('\n'.join(L))
df=ROOT+'Screens/_daily/_wave7_done.txt'
d=open(df,encoding='utf-8').read()
if not d.endswith('\n'): d+='\n'
assert 'KVUE' not in d.split()
d+='KVUE\n'; open(df,'w',encoding='utf-8',newline='\n').write(d)
print('done lines',len([x for x in d.split('\n') if x.strip()]))
rf=ROOT+'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
r=open(rf,encoding='utf-8').read()
if not r.endswith('\n'): r+='\n'
r+=open('_reading_fold.md',encoding='utf-8').read()
open(rf,'w',encoding='utf-8',newline='\n').write(r)
sf=ROOT+'Screens/SURVIVAL SHAPES - index.md'
s=open(sf,encoding='utf-8').read()
rows=re.findall(r'(?m)^\| (\d+) \| ',s); nums=[int(x) for x in rows]
print('shape rows',len(nums),'max',max(nums))
note=(f"\n*Dated note, 2026-09-26 (the KVUE fold, wave 7 name 60): **no row was added, no number moved, and the count of distinct shapes is unchanged at 25.** "
 f"The table was counted with a line-start regex immediately before writing: **{len(nums)} rows, maximum number {max(nums)}**. Kenvue closed at **Q2 OUT**, so Q4 was never opened and the business has no named death. "
 "The run file names, as a signature WITHOUT a verdict, **#19 THE SHELF** (the brands are owned and the route to the buyer is rented from retailers whose top ten take 41% of sales and who stock their own label beside Tylenol and Zyrtec at a lower price; "
 "store brands held about 19% of global pain care and 27% of allergy care in 2022, and the company's units fell in every year 2023-2025 while it raised price 10.7%). "
 "**Not entered in #19's instances column**, for the reason the earlier wave 7 folds gave: entering a Q2 observation as a Q4 instance would make this index say something the run file does not. "
 "The quote is a merger spread (Kimberly-Clark, expected to close in the fourth quarter of 2026).*\n")
if not s.endswith('\n'): s+='\n'
s+=note; open(sf,'w',encoding='utf-8',newline='\n').write(s)
print('shape note appended')

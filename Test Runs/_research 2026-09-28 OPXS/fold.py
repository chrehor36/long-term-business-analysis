import re
def append(path, text):
    raw=open(path,'rb').read(); crlf=b'\r\n' in raw
    t=text.replace('\r\n','\n')
    if crlf: t=t.replace('\n','\r\n')
    nl=b'\r\n' if crlf else b'\n'
    if not raw.endswith(nl): raw+=nl
    open(path,'wb').write(raw+t.encode('utf-8'))
    return crlf
# 3. narrative fold
rl='Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
print('reading list crlf', append(rl, open('Test Runs/_research 2026-09-28 OPXS/fold_note.md',encoding='utf-8').read()))
# survival shapes: count the table first
sp='Screens/SURVIVAL SHAPES - index.md'
s=open(sp,encoding='utf-8').read()
rows=re.findall(r'(?m)^\| (\d+) \|',s); n=len(rows); mx=max(map(int,rows))
note=f"""
*Dated note, 2026-09-28 (the OPXS fold, wave 7 name 92): **no row was added, no number moved, and the count of distinct shapes is unchanged at 25.** The table was counted with a line-start regex immediately before writing: **{n} rows, maximum number {mx}**. Optex Systems Holdings closed at **Q2 OUT**, so Q4 was never opened and this business has no named death. The run file names **#20 THE WAVE** (the FY2023-FY2025 record made in the ground-vehicle replenishment and its supply-tight years, the 10-Q recording orders slowing and a new entrant) as a signature WITHOUT a verdict, with **#14 THE PATRON** (the buyer that funds the programme sets the terms: appropriations, termination for convenience, TINA certified cost) and **#11 THE PASS-THROUGH** (fixed prices absorbing cost inflation; the buyer's second source passing productivity back at the next bid) as features. **None is entered in an instances column**, for the reason the PAGP and CALM folds gave: a Q2 observation is not a Q4 instance.*
"""
print('shapes crlf', append(sp, note), n, mx)
# 5. done file
df='Screens/_daily/_wave7_done.txt'
raw=open(df,'rb').read(); crlf=b'\r\n' in raw; nl=b'\r\n' if crlf else b'\n'
if not raw.endswith(nl): raw+=nl
open(df,'wb').write(raw+b'OPXS'+nl)
L=[l for l in open(df,encoding='utf-8').read().splitlines() if l.strip()]
print('done lines',len(L),'last',L[-1],'dupes',len(L)-len(set(L)),'crlf',crlf)

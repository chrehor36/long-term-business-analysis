import re
# 1. shape index: count rows first
p='Screens/SURVIVAL SHAPES - index.md'
s=open(p,encoding='utf-8').read()
rows=[int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \|',s)]
print('shape rows',len(rows),'max',max(rows))
assert len(rows)==30 and max(rows)==30
note=("*Dated note, 2026-09-26 (the SYY fold, wave 7 name 47): **no row was added, no number moved, and the count of distinct shapes is unchanged at 25.** "
"The table was counted with a line-start regex immediately before writing: **30 rows, maximum number 30**. Sysco closed at **Q2 OUT**, so Q4 was never opened and the business has no named death. "
"The run file names, as a signature WITHOUT a verdict, **#11 THE PASS-THROUGH** (prices set at cost plus a mark-up with, in the registrant's words, *\"our limited ability to increase prices\"*; the procurement synergies of the pending Jetro Restaurant Depot purchase partly promised to customers; operating margin 5.1-5.3% in FY2009-FY2010 to 3.7% in FY2026 while sales doubled) "
"**with #24 THE BOUGHT AVERAGE as a feature** (a business whose own margin has drifted down agrees to buy a 12.3%-margin one for 91.5M new shares and about $21bn of new debt, lifting the blended margin and EBITDA growth its release headlines while the share count, the goodwill (pro forma $5.2bn to $24.0bn) and the debt (pro forma $13.5bn to $34.4bn) rise). "
"**None of these is entered in an instances column**, for the reason the PAGP, CALM, USPH, BDC, PPG, MATX and LNN folds gave: a Q2 observation entered as a Q4 instance would make this index say something the run file does not.*")
b=open(p,'rb').read(); nl=b'\r\n' if b.endswith(b'\r\n') else b'\n'; assert b.endswith(nl)
open(p,'wb').write(b+note.encode('utf-8')+nl); print('shape note ok',nl)
# 2. reading list
p='Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
b=open(p,'rb').read(); crlf=b'\r\n' in b[:20000]; nl='\r\n' if crlf else '\n'
add=open('Test Runs/_research 2026-09-26 SYY/reading_fold.md',encoding='utf-8').read()
add=add.replace('\r\n','\n')
if not b.endswith(nl.encode()): add='\n'+add
open(p,'wb').write(b+add.replace('\n',nl).encode('utf-8')); print('reading fold ok crlf',crlf)

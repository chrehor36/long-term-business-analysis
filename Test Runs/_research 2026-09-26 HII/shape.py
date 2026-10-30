import re
F='../../Screens/SURVIVAL SHAPES - index.md'
raw=open(F,'rb').read(); t=raw.decode('utf-8')
rows=[l for l in t.replace('\r\n','\n').split('\n') if re.match(r'^\| \d+ \|',l)]
n=len(rows); mx=max(int(re.match(r'^\| (\d+) \|',l).group(1)) for l in rows)
assert (n,mx)==(30,30),(n,mx)
note=("*Dated note, 2026-09-26 (the HII fold, wave 7 name 52): **no row was added, no number moved, and the count of distinct shapes is unchanged at 25.** "
"The table was counted with a line-start regex immediately before writing: **%d rows, maximum number %d**. Huntington Ingalls Industries closed at **Q2 OUT**, "
"so Q4 was never opened and the business has no named death. The run file names, as a signature WITHOUT a verdict, **#14 THE PATRON** in its rows' own "
"government form (the one buyer, the U.S. Navy, part-funds the plant through capital grants, a state-leased yard, progress payments and CAS pension recovery, "
"writes the rules that set the price - allowable cost under the FAR and CAS, audit, refund, a negotiated fee - and can change them: Item 1A names "
"*\"Changes in procurement practices favoring incentive-based fee arrangements, different award criteria, non-traditional contract provisions, and cost mandates from the government\"*, "
"and a public yard could take carrier refuelling; the segment margin fell from 10.1%% in 2016 to 5.0%% in 2024, the only rival yard's in step) "
"**with #11 THE PASS-THROUGH and #1 CONTRACTED NOT TO STOP as features** (under cost-type pricing, 50%% of 2025 revenue, a cost saving lowers the price; "
"incentive contracts past the share line *\"effectively become firm fixed-price contracts\"* on ships the yard must finish). **#4 THE CASH IS SPENT UNDOING PAST WORK was tested "
"and does not fit**: HII's customer advances ($1,220M at FY2025, $690M at 2026-06-30) are discharged at the contract margin, not a negative one, and reverse; they are not float. "
"**Not entered in an instances column**, for the reason the PAGP, CALM, USPH, BDC, PPG, MATX, LNN, SYY, MLI, CMT, WSM and SXC folds gave: entering a Q2 observation as a Q4 "
"instance would make this index say something the run file does not.*") % (n,mx)
open(F,'wb').write(raw+('\r\n'+note+'\r\n').encode('utf-8'))
print('ok',n,mx)

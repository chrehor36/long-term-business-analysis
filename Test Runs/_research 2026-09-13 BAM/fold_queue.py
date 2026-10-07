import io
Q=r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\WATCHLIST RUN QUEUE.md"
t=open(Q,encoding='utf-8').read()
entry=open('fold_entry.md',encoding='utf-8').read()

# 1. register entry at the top of COMPLETED FROM THE QUEUE
h='## COMPLETED FROM THE QUEUE\n'
assert t.count(h)==1
t=t.replace(h,h+entry,1)

# 2. strike the ticker in the MINI BERK roster (whole file searched)
old='0.08% parity; struck 2026-09-13)*, ~~HHH~~, ~~GHC~~, BAM, BN'
assert t.count(old)==1, t.count(old)
t=t.replace(old,'0.08% parity; struck 2026-09-13)*, ~~HHH~~, ~~GHC~~, ~~BAM~~ *(run 2026-09-13 - FAIL at Q2, OUT on the\nbusiness; see COMPLETED)*, BN',1)

# 3. dated note beside the 2026-09-02 block paragraph
old2='**BAM and BN remain BLOCKED and are out of scope**, stated rather than stretched over: they\nare asset managers with fee streams and consolidated funds, which is a **different perimeter\nproblem**, closer to the DKS/HON class than to the insurer class.'
assert t.count(old2)==1
t=t.replace(old2, old2+'\n\n*Dated note, 2026-09-13, left beside the paragraph above rather than replacing it (operator rule 6):*\n***BAM WAS RUN ON 2026-09-13** and the block was tested against the filings rather than inherited.\nThe perimeter is measurable - the 2025 reorganisation is fully restated with the ULC as Predecessor,\nconsolidated funds are separately captioned, and BN\u2019s carry has its own NCI lines - so the block was\na scheduling judgment, not a measurement finding. **The paragraph above was right about two things**:\nno five-year window on one perimeter exists, and the perimeter moved again on 2026-07-31 when BAM took\ncontrol of Oaktree. Verdict **Q2 OUT**; the entry is in `## COMPLETED FROM THE QUEUE`. **BN is still\nunrun and the paragraph still governs it.***',1)

# 4. dated note beside the 2026-09-13 backfill line
old3='**BAM and BN are NOT struck: they were never run.** They sit in the\nroster as BLOCKED, out of scope, as a different perimeter problem from the insurers. That is the\nonly part of the operator\u2019s lists still without a price and a pass/fail line.'
if t.count(old3)!=1:
    old3=old3.replace('\u2019',"'")
assert t.count(old3)==1, 'backfill anchor'
t=t.replace(old3, old3+'\n\n*Dated note, 2026-09-13, added beside the line above rather than rewriting it (operator rule 6):*\n***BAM was run later the same day** and is now struck in the roster, with price, share count, cover\naccession, cap, sovereign and a PASS/FAIL line in `## COMPLETED FROM THE QUEUE` (Q1 IN / Q2 OUT).\n**BN remains unrun and the sentence above still holds for it.***',1)

open(Q,'w',encoding='utf-8').write(t)
print('ok; lines',t.count(chr(10))+1)

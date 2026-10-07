run='../2026-09-28 Run - DTM DT Midstream.md'
s=open(run,encoding='utf-8').read()
anchor="(the template copied and committed before any fetch).**\n"
assert s.count(anchor)==1
banner=anchor+"""
**VERDICT: Q2 OUT.** Q1 IN. The file closes at Question 2, permanently, on the business: [E3-03] criterion (3) fails for
the FERC-tariffed third of the profit and criterion (2) is not shown for the unregulated gathering two-thirds. Q3 to Q6
are NOT scored; what was read beneath the close is recorded unscored.
"""
s=s.replace(anchor,banner)
a2="---\n## Q6 — THE REVERSAL CONDITION, IN WORDS"
assert s.count(a2)==1
tool="""---
## TOOLING, REPORTED NOT PATCHED (operator rule 8; a tool may never add a number)

- `tools/run.py DTM` (output `runpy_out.txt`) subtracts **total D&A including the acquired-intangible amortization** as its
  "OE hi" end (so its 570 is the screen's 570, not the filed construction's 628), defaults to a **three-year** window and prints
  the corpus's five-year window as "THE OTHER WINDOW"; its five-year figure ($315-534M) differs from this file's filed
  construction ($320M at the capex end; $528M with total D&A) by about $5M a year in opposite directions, source not traced.
- Its *"3. POINTS OVER THE SOVEREIGN -0.72 .. +1.80"* comes from an unprinted growth assumption (`points_over()`), while its own
  printed yield (2.17-4.57%) sits wholly below the 5.49% bond; reported, not used. Its *"2. GROWTH THE PRICE ASSUMES 9.2% (at a
  5.49% rate)"* is struck against the bond, not the ~10% floor [E4-28].
- It carries no perimeter warning: nothing in its output says that 2023-2024 exclude the pipes the cap now buys, or that 2019-2021
  are carve-out years.

"""
s=s.replace(a2,tool+a2)
open(run,'w',encoding='utf-8').write(s)
print('ok')

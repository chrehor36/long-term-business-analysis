import sys
p = "Test Runs/2026-10-18 Run - DTE DTE Energy.md"
t = open(p, encoding="utf-8").read()
R = [
("**Contrary evidence, written down as found** **[M1997-127]**:", "**Contrary evidence, written down as found** (\"write it down in the first 30 minutes\" **[M1997-127]**):"),
("- **The attacker with money** **[M2011-015]**:", "- **The attacker with money** (\"if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I\n  do it?\" **[M2011-015]**):"),
("- **Pricing power and the agony before a rise** **[M2005-020]**:", "- **Pricing power and the agony before a rise** (\"you can almost measure the strength of a business over time by the\n  agony they go through in determining whether a price increase can be sustained\" **[M2005-020]**):"),
("- **Unit volume** **[M1999-054]**, read as deliveries:", "- **Unit volume** (\"We measure it by unit cases sold\" **[M1999-054]**), read as deliveries:"),
("- **The low-cost position, and the customer who would take the low bid** **[M2017-009]**:", "- **The low-cost position, and the low bid** (\"it wouldn’t be a question of people buying candy for the low bid\"\n  **[M2017-009]**):"),
("- **Ask the competitors** **[M1999-130]**:", "- **Ask the competitors** (\"which one would it be and why?\" **[M1999-130]**):"),
("- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**:", "- **Widening or narrowing** (\"whether it’s likely to widen further or shrink on you\" **[M1999-108]**; \"grows either\n  weaker or stronger\" **[L2005-010]**):"),
("- **What could destroy, modify or reduce it** **[M2000-014]**: (i) the compact itself, as the 2023 letter narrates of\n  other states **[L2023-011]**:", "- **What could destroy, modify or reduce it** (\"destroy, or modify, or reduce the economic strengths\" **[M2000-014]**):\n  (i) the compact itself, as the 2023 letter narrates of other states, \"the regulatory climate in a few states has raised\n  the specter of zero profitability or even bankruptcy\" **[L2023-011]**;"),
("the newspaper question asked of a grid **[L2006-008]**;", "the question the 2006 letter asks of newspapers, \"if cable and satellite broadcasting, as well as the internet, had\n  come along first, newspapers as we know them probably would never have existed\" **[L2006-008]**, asked of a grid;"),
("""- **VERDICT: IN.** The deciding part's castle stands on the filings: a statutory franchise with competition capped at 10%
  of retail sales, an authorized return re-affirmed in the latest order, and no rival able to duplicate the grid
  **[M1995-038]**, **[M2013-054]**. It protects a regulated, fair return, not an excellent one **[L2007-004]**, which the
  framework sends to Q3 as a second best **[M2009-104]**, **[L2009-012]**. What could break it, the compact and the
  technology, is carried to Q9 **[L2023-011]**, **[M2000-014]**.""",
"""- **VERDICT: IN.** The deciding part's castle stands on the filings: a statutory franchise with competition capped at 10%
  of retail sales, an authorized return re-affirmed in the latest order, and no rival able to duplicate the grid, "You
  really couldn’t create another railroad" **[M2013-054]**. It protects a fair return, not "excellent returns on invested
  capital" **[L2007-004]**, which the framework sends to Q3 as a second best, "there’s no way we get rich on our utility
  investments" **[M2009-104]**. What could break it, the compact and the technology, is carried to Q9."""),
("""- **VERDICT: IN.** The deciding part is a rate-regulated electric utility whose earning power over ten years is set by
  rate base and an authorized return that are filed and slow to move **[M2012-065]**, **[M2010-037]**; the parts that cannot
  be foreseen are small and do not decide.""",
"""- **VERDICT: IN.** The deciding part is a rate-regulated electric utility whose earning power over ten years is set by
  rate base and an authorized return that are filed and slow to move, so "a reasonable fix on about what the earning power
  and competitive position will look like in five or 10 years" **[M2012-065]** is available for it, and "when you get an
  allowed return in the electric utility you’re almost certain of earning it" **[M2010-037]**; the parts that cannot be
  foreseen are small and do not decide."""),
]
for a, b in R:
    if a not in t: print("NOT FOUND:", a[:70]); continue
    t = t.replace(a, b)
open(p, "w", encoding="utf-8").write(t)
print("ok")

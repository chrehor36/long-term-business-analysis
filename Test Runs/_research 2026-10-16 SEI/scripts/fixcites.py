import re
p = '2026-10-16 Run - SEI Solaris Energy Infrastructure.md'
t = open(p, encoding='utf-8').read()
def rep(old, new):
    global t
    old_re = re.escape(old).replace(r'\ ', r'\s+')
    m = re.search(old_re, t)
    if not m: print('NOT FOUND:', old[:70]); return
    t = t[:m.start()] + new + t[m.end():]
rep("the rule binds the buyer's own financing and sizing, not the target **[M2012-081]**, **[L2023-005]**.",
    "the rule binds the buyer's own financing and sizing, not the target: \"never going to risk what we have and need for what we don’t have and don’t need\" **[M2012-081]**; \"Never risk permanent loss of capital.\" **[L2023-005]**.")
rep("The filer reports two parts with different economics **[L2008-005]**:",
    "The filer reports two parts with different economics, and \"lumping them together [...] impedes analysis\" **[L2008-005]**:")
rep("- Where will it be in ten years **[M1999-132]**? A fleet",
    "- \"What’s that chart going to look the next 10 years?\" **[M1999-132]** A fleet")
rep("Its key variables **[M1998-044]** are US completion",
    "Its key variables (\"trying to identify the key variables in that particular business\" **[M1998-044]**) are US completion")
rep("and the business is read off its figures **[M2008-069]**.",
    "and \"if you can’t make a decision on something like PetroChina off the figures, forget about going further\" **[M2008-069]**.")
rep("- Do the past statements tell the future ones **[M2008-033]**? Yes, for this part:",
    "- \"do I understand enough about this business so that the financial statements will tell me the information that’s useful to me\" **[M2008-033]**? Yes, for this part:")
rep("- Is it important and knowable **[M2006-076]**, and would its insiders write it down **[M2000-105]**? The economics",
    "- Is it among \"things that are important and knowable\" **[M2006-076]**, and would its insiders \"put down on paper their predictions\" **[M2000-105]**? The economics")
rep("with no figure for the fleet after them **[M2000-105]**.",
    "with no figure for the fleet after them; of such a forecast the insiders \"would not want to put down on paper their predictions\" **[M2000-105]**.")
rep("since no further reading of a filing could say what a turbine rents for in 2036 **[L1993-023]**, **[M2000-038]**.",
    "since no further reading of a filing could say what a turbine rents for in 2036: \"the nature of the industry would be the roadblock\" **[L1993-023]**; \"It just means that we don’t know how to evaluate it.\" **[M2000-038]**")
rep("by the business-of-parts CONVENTION on the fiscal window **[M2012-065]**,\n  **[M2008-033]**.",
    "by the business-of-parts CONVENTION on the fiscal window: \"a reasonable fix on about what the earning power and competitive position will look like\" **[M2012-065]** is had for that part.")
rep("- **The attacker with money** **[M2011-015]**. The attackers",
    "- **The attacker with money:** \"if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?\" **[M2011-015]** The attackers")
rep("- **Pricing power, and the price through the last inflation** **[M2005-020]**.",
    "- **Pricing power, and the price through the last inflation:** \"the agony they go through in determining whether a price increase can be sustained\" **[M2005-020]**.")
rep("- **Would the customer still choose it over the low bid** **[M2017-009]**?",
    "- **The low bid:** \"it wouldn’t be a question of people buying candy for the low bid\" **[M2017-009]**; here it is.")
rep("- **Unit volume** and **widening or narrowing** **[M1999-108]**.",
    "- **Unit volume, and the moat** \"likely to widen further or shrink on you\" **[M1999-108]**.")
rep("- **The low-cost position** **[M1997-010]**, **[M2006-004]**: the filer",
    "- **The low-cost position:** \"commodity businesses have risk unless you’re the low-cost producer\" **[M1997-010]**, measured \"more by cost of production\" **[M2006-004]**: the filer")
rep("- **What could destroy, modify or reduce it** **[M2000-014]**: customer",
    "- **What could** \"destroy, or modify, or reduce the economic strengths\" **[M2000-014]**: customer")
rep("This is not a castle \"whose future cannot be judged\"\n**[M2000-019]**: the returns are known,",
    "This is not the tenuous moat of which the rows say \"We don’t know how to valuate that\" **[M2000-019]**: the returns are known,")
rep("over the full cycle **[L2007-004]**, **[M2013-052]**, **[M2012-106]**, **[M2011-015]**, **[M1999-108]**. The file closes",
    "over the full cycle; the rows ask for a moat \"that protects excellent returns on invested capital\" **[L2007-004]**, and \"If the answer had been yes, we wouldn’t have done it.\" **[M2011-015]** The file closes")
rep("The eight to ten years of balance sheets were read in Step 0 **[M2025-032]**;",
    "The \"balance sheets over an 8 or 10 year period\" **[M2025-032]** were read in Step 0;")
rep("a later run that reaches Q5 must answer\nthem **[M2013-088]**.",
    "a later run that reaches Q5 must answer\nthem: \"If you’ve got doubts, forget it.\" **[M2013-088]**")
rep("Written down as found **[M1997-127]**; no verdict;",
    "Written down as found (\"write it down in the first 30 minutes\" **[M1997-127]**); no verdict;")
open(p, 'w', encoding='utf-8').write(t); print('done')

# Rewords every place where an id sat beside the analyst's or the framework's words, so that each id
# sits beside the row's own words (the brief's citation rule). Exact replacements; each must match once.
P = "Test Runs/2026-10-17 Run - AMTM Amentum.md"
s = open(P, encoding="utf-8").read()
R = [
("the balance sheet itself holds no warning sign of a kind the speakers name **[M2025-032]**, **[M1995-064]**.",
 "the balance sheet itself shows none of the signs the row names, no \"prepaid expense, deferred asset accounts start building up suspiciously high\" **[M1995-064]**, and it is the place where \"there are certain things it’s harder to hide or play games with\" **[M2025-032]**."),
("No macro forecast enters **[M2000-094]**: the federal budget,",
 "Macro conclusions \"just never enter into the discussion\" **[M2000-094]**: the federal budget,"),
("never as a forecast. Who is paid to tell you **[M2020-037]**: the 10-K calls",
 "never as a forecast. The filer's self-description is not weighed either: the 10-K calls"),
("none of that is weighed. Margin of safety **[M1996-084]** belongs to Q7.",
 "none of that is weighed. Whether the price \"ought to just kind of scream at you\" **[M1996-084]** belongs to Q7."),
("**Contrary evidence, written down as found** **[M1997-127]**:",
 "**Contrary evidence, written down as found** (the habit of Darwin, who had to \"write it down in the first 30 minutes\" **[M1997-127]**):"),
("is weighed at Q9, not here **[M2012-081]**.",
 "is weighed at Q9, not here; the standing rule is the buyer's, \"never going to risk what we have and need for what we don’t have and don’t need\" **[M2012-081]**."),
("This is a macro variable, which the foundations keep out as a forecast **[M2000-094]**;",
 "This is a macro variable, and macro conclusions \"just never enter into the discussion\" **[M2000-094]**;"),
("**Do the past statements tell me the future ones?** **[M2008-033]** Mostly yes,",
 "**Do the past statements tell me the future ones?** The row asks whether \"the financial statements will tell me the information that’s useful to me in making a judgment about what the future financial statements are going to look like\" **[M2008-033]**. Mostly yes,"),
("**Is it important and knowable?** **[M2006-076]** The deciding variables",
 "**Is it important and knowable?** \"If something’s important but unknowable, forget it.\" **[M2006-076]** The deciding variables"),
("The budget level is important and not knowable; the rows keep it out of the decision as a forecast **[M2000-094]**, and it is carried as width at Q7.",
 "The budget level is important and not knowable; it is kept out of the decision as a forecast (the foundations), and it is carried as width at Q7."),
("**Would the insiders write it down?** **[M2000-105]** The field's insiders do:",
 "**Would the insiders write it down?** The test is whether they \"would not want to put down on paper their predictions\" **[M2000-105]**. The field's insiders do:"),
("**The industry or the company?** **[M2012-067]** Seeing the industry is not seeing the company.",
 "**The industry or the company?** There are industries that \"may have a wonderful future, but we don’t have the faintest idea who the winners will be\" **[M2012-067]**."),
("can be pictured ten years out within a range **[M2012-065]**, **[M2011-084]**: the margin band",
 "gives \"a reasonable fix on about what the earning power [...] will look like in five or 10 years\" **[M2012-065]**, with \"some model in our mind of how far off we can be\" **[M2011-084]**: the margin band"),
("the budget level is width, not understanding **[M2000-094]**. Where the company will stand within the industry is passed to Q2 **[M2012-067]**.",
 "the budget level is width, not understanding. Where the company will stand within the industry is passed to Q2."),
("10. *Widening or narrowing?* **[M1999-108]** Narrowing signs:",
 "10. *Widening or narrowing?* The question is the moat's width \"and whether it’s likely to widen further or shrink on you\" **[M1999-108]**. Narrowing signs:"),
("No row-quality test separates them: the speakers say the moat is judged, not measured **[M1999-108]**.",
 "No measured test separates them: \"there’s no formula that gives you that precisely\" **[M1999-108]**."),
("11. *What could destroy, modify or reduce it, five to fifteen years out?* **[M2000-014]** The filer names them:",
 "11. *What could destroy, modify or reduce it, five to fifteen years out?* The row asks what could \"destroy, or modify, or reduce the economic strengths\" **[M2000-014]**. The filer names them:"),
("On the capital the work needs **[M2010-090]**, the field earns",
 "On \"the capital actually needed in the business\" **[M2010-090]**, the field earns"),
("is important and knowable **[M2006-076]**: the federal award record",
 "is among the \"things that are important and knowable\" **[M2006-076]**: the federal award record"),
("The castle's future cannot be judged from the filings read **[M2000-019]**, **[M2006-013]**: the pricing-power test fails **[M2005-020]**, the money test leans against **[M2011-015]**, the moat is one that must be continuously rebuilt **[L2007-005]**, and the evidence",
 "The castle's future cannot be judged from the filings read, \"We don’t know how to valuate that\" **[M2000-019]**, so it goes to the third of the \"three boxes at the company: in, out, and too hard\" **[M2006-013]**. There is no price of its own whose rise could be measured by \"the agony they go through\" **[M2005-020]**; to the question \"could I do it?\" **[M2011-015]** the filer's own takeaway wins answer yes for a rival; \"A moat that must be continuously rebuilt will eventually be no moat at all\" **[L2007-005]**; and the evidence"),
("a deal paid in shares **[L2009-019]**:", "a deal paid in shares, \"by issuing our stock in a merger\" **[L2009-019]**:"),
("(operator rule 2; Part VII, CONVENTION)* **[M1997-127]**.", "(operator rule 2; Part VII, CONVENTION).*"),
("**Knowable** **[M2006-076]**.", "**Knowable.**"),
("and the one fact that would close the file OUT** **[M1998-144]**.",
 "and the one fact that would close the file OUT**, so that the reading can \"possibly reject your original hypothesis\" **[M1998-144]**."),
("or the pass ends unsure **[M2002-092]**.",
 "or the pass ends unsure: \"if you have doubts about something being into your circle of competence, it isn’t\" **[M2002-092]**."),
]
for a, b in R:
    n = s.count(a)
    assert n == 1, (n, a[:70])
    s = s.replace(a, b)
open(P, "w", encoding="utf-8").write(s)
print("replaced", len(R))

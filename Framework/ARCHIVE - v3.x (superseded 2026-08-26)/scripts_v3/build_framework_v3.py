# -*- coding: utf-8 -*-
"""Generate: A Framework for Long-Term Business Analysis — v3.0 (July 2026).
Rebuilt from primary sources per CLAUDE.md. Citations reference
principle_ledger.csv row IDs (E1-xx .. E5-xx), claims_audit.csv (Cxx),
An Owner's Manual (OM-x), and the July 2026 field amendments (FA)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reportlab.platypus import PageBreak, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

from v3_style import (CHECK, GOLD, GRAY, MOTTO, NAVY, NumberedDoc, PALE, S,
                      callout, q, rule_card, source_class_box)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "A Framework for Long-Term Business Analysis v3.0.pdf")

el = []
P, SP = Paragraph, Spacer

# ================= COVER =================
el += [SP(1, 60),
 P("A FRAMEWORK FOR LONG-TERM<br/>BUSINESS ANALYSIS", S["title"]), SP(1, 10),
 P("Built exclusively on the primary sources of Warren E. Buffett and Charles T. Munger —<br/>"
   "who learned from Benjamin Graham and expanded on it", S["subtitle"]), SP(1, 6),
 P("VERSION 3.0 — JULY 2026", S["edition"]), SP(1, 26),
 P("“It’s not given to human beings to have such talent that they can just know everything about "
   "everything all the time. But it is given to human beings who work hard at it — who look and sift "
   "the world for a mispriced bet — that they can occasionally find one.”", S["epigraph"]),
 P("— Charles T. Munger, USC Business School, 1994 (PCA Talk 2) [E3-21]", S["epigraphsrc"]),
 SP(1, 18), P(f"“{MOTTO}”", S["epigraph"]),
 P("— framework motto (our words, not theirs)", S["epigraphsrc"]), SP(1, 30),
 P("Sources on the citation shelf: Buffett Partnership letters 1957–1970 · Berkshire Hathaway "
   "shareholder letters 1965–2025 (official text 1977–2025) · Berkshire annual meeting transcripts "
   "1994–2025 · Poor Charlie’s Almanack, 11 talks (Stripe Press free web edition) · An Owner’s "
   "Manual · Buffett’s Fortune essays 1977/1999/2001 · Wesco letters 1997–2009 (read; yielded "
   "operations, not philosophy [E5-07])", S["small"]),
 P("Every quotation in this document reproduces the corpus text verbatim and carries a ledger "
   "citation [Ex-xx] traceable in principle_ledger.csv. Anything not so cited is labeled either "
   "FRAMEWORK CONVENTION or FIELD AMENDMENT — JULY 2026. Nothing is silently invented.", S["small"]),
 PageBreak()]

# ================= TABLE OF CONTENTS =================
el += [P("TABLE OF CONTENTS", S["h1"])]
toc = [
 ("Abstract", "Thesis, method, scope, and the three-class sourcing rule"),
 ("The Spine", "An Owner’s Manual — 15 principles mapped to the gates"),
 ("The Structural Authority", "Buffett’s five risk factors (1993)"),
 ("Introduction", "What this framework is, is not, and why the sequence"),
 ("Gate 1", "Circle of Competence"),
 ("Gate 2", "Moat Identification — led by the 1991 franchise test"),
 ("Gate 3", "Management Integrity"),
 ("Gate 4", "Financial Quality — owner earnings, complete formula"),
 ("Gate 5", "Inversion"),
 ("Gate 6", "Valuation — Book One (the Buffett Statute) and Book Two (build-up DCF)"),
 ("Gate 7", "Position Sizing and Monitoring"),
 ("Gate 8", "Reverse DCF — the pari-mutuel gate"),
 ("Quick Reference", "One page"),
 ("Glossary", "Key terms, corpus-grounded"),
 ("Appendix A", "Primary-source reading order (ranges corrected)"),
 ("Appendix B", "Portfolio tracking tools"),
]
rowsT = [[P(f"<b>{a}</b>", S["body"]), P(b, S["body"])] for a, b in toc]
t = Table(rowsT, colWidths=[1.5 * inch, 5.2 * inch])
t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                       ("LINEBELOW", (0, 0), (-1, -2), 0.25, PALE),
                       ("TOPPADDING", (0, 0), (-1, -1), 3),
                       ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
el += [t, SP(1, 10),
 callout([P("A business must pass every gate in sequence. A failure at any gate stops the "
            "analysis entirely. The DCF is the last step — never the first.", S["cardbody"])]),
 PageBreak()]

# ================= ABSTRACT =================
el += [P("ABSTRACT", S["h1"]),
 P("Thesis", S["h2"]),
 P("This document proposes a sequential, gate-based methodology for evaluating businesses as "
   "long-term investment candidates, derived from the published primary sources of Warren E. "
   "Buffett and Charles T. Munger: the partnership letters, the Berkshire shareholder letters, "
   "the annual-meeting transcripts, the eleven talks of Poor Charlie’s Almanack, and An Owner’s "
   "Manual. Graham is present the way he is present in Berkshire itself — absorbed and extended: "
   "he is named only inside Buffett’s and Munger’s own sentences, never cited as an independent "
   "source.", S["body"]),
 P("The three-class sourcing rule", S["h2"]),
 P("The May 2026 edition claimed “No analytical principle in this framework is invented.” The "
   "audit (claims_audit.csv, 40 claims) proved that false: of the flagship attributions, nine were "
   "misattributed and nine could not be found in the corpus at all. Version 3.0 replaces that "
   "claim with an honest rule. Every load-bearing statement belongs to exactly one class:", S["body"]),
 P("• <b>LEDGER</b> — a verbatim corpus quotation, cited as [Ex-xx] to principle_ledger.csv, "
   "verifiable in under two minutes.", S["bullet"]),
 P("• <b>FRAMEWORK CONVENTION</b> — useful operational machinery (thresholds, fade periods, "
   "checklists) that is ours, not theirs, and is boxed and labeled as such.", S["bullet"]),
 P("• <b>FIELD AMENDMENT — JULY 2026</b> — rules earned in live application, boxed and labeled.", S["bullet"]),
 P("Scope and limitations", S["h2"]),
 P("Designed for publicly traded businesses with sufficient primary-source filing history "
   "(the eight-consecutive-quarters requirement is a FRAMEWORK CONVENTION). Not designed for "
   "early-stage companies or situations where filings are unavailable or unreliable. The framework "
   "does not guarantee outcomes; each gate is a structured attempt to identify the ways an analysis "
   "could be wrong.", S["body"]),
 P("Central claim", S["h2"])]
el += q("Your goal as an investor should simply be to purchase, at a rational price, a part interest "
        "in an easily-understandable business whose earnings are virtually certain to be materially "
        "higher five, ten and twenty years from now.", "Buffett, 1996 letter [E3-14]")
el += q("Time is the friend of the wonderful business, the enemy of the mediocre.",
        "Buffett, 1989 letter [E2-19]")
el += [P("A business that passes all eight gates at a price providing an adequate margin of safety "
   "is a probable mispriced bet. The framework does not predict when price converges to value; it "
   "holds that time, applied to a durable business, is itself the compounding force.", S["body"]),
 PageBreak()]

# ================= SPINE: OWNER'S MANUAL =================
el += [P("THE SPINE — AN OWNER’S MANUAL", S["h1"]),
 P("In 1983, Buffett set down 13 owner-related business principles; Berkshire republishes them, "
   "updated, as An Owner’s Manual — the closest thing to a framework document its authors ever "
   "wrote. Version 3.0 opens from it. The full mapping (with verbatim passages) is "
   "owners_manual_map.md; the table below is the summary. “All 13 remain alive and well today.”", S["body"])]
om = [
 ("OM-1", "Partnership attitude; part-owner of a business, indifferent to quotes", "Introduction; Gate 7"),
 ("OM-2", "“We eat our own cooking”", "Gate 3 — Alignment"),
 ("OM-3", "Maximize per-share intrinsic value gain, not size", "Gate 3 — Competence; Gate 6"),
 ("OM-4", "Own businesses earning above-average returns on capital; falling markets are good news", "Gate 4; Gate 7"),
 ("OM-5", "Consolidated numbers reveal little; segment economics matter", "Gate 2 rule; Gate 4"),
 ("OM-6", "Accounting doesn’t drive decisions; look-through earnings", "Gate 4 [E3-04]"),
 ("OM-7", "Debt used sparingly; float and deferred taxes as benign leverage", "Gate 4 — fortress test"),
 ("OM-8", "No wish-list acquisitions at shareholder expense", "Gate 3 — Competence"),
 ("OM-9", "$1 retained must create $1 of market value (test as corrected in 2009)", "Gate 3 — Competence"),
 ("OM-10", "Issue shares only for equal value received", "Gate 4 — dilution discipline"),
 ("OM-11", "No gin-rummy divestitures — CONTROLLED businesses only, per the OM’s own 2016 note", "Gate 7 caution"),
 ("OM-12", "Candor: report as we’d want reported to us; no big-bath, no smoothing", "Gate 3 — Integrity"),
 ("OM-13", "Silence on marketable securities; good ideas are rare and appropriable", "Gate 1 — edge"),
 ("OM-14", "Fair price preferred over high price; overvaluation is as bad as undervaluation", "Gate 7 — reduce trigger"),
 ("OM-15", "Book-value gain vs the S&P 500 — an honest self-benchmark", "Appendix B"),
]
rowsOM = [[P(f"<b>{a}</b>", S["body"]), P(b, S["body"]), P(c, S["body"])] for a, b, c in om]
t = Table([[P("<b>Principle</b>", S["body"]), P("<b>Substance</b>", S["body"]),
            P("<b>Maps to</b>", S["body"])]] + rowsOM,
          colWidths=[0.7 * inch, 3.9 * inch, 2.1 * inch])
t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                       ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                       ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                       ("LINEBELOW", (0, 0), (-1, -1), 0.25, PALE),
                       ("TOPPADDING", (0, 0), (-1, -1), 2.5),
                       ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5)]))
el += [t, SP(1, 8)]
el += q("Intrinsic value can be defined simply: It is the discounted value of the cash that can be "
        "taken out of a business during its remaining life. [...] intrinsic value is an estimate rather "
        "than a precise figure, and it is additionally an estimate that must be changed if interest "
        "rates move or forecasts of future cash flows are revised.",
        "An Owner’s Manual, Intrinsic Value section — the definition Gate 6 is built on; also the "
        "primary basis for Step 0’s rate refresh (FA)")
el += [PageBreak()]

# ================= STRUCTURAL AUTHORITY =================
el += [P("THE STRUCTURAL AUTHORITY — BUFFETT’S FIVE RISK FACTORS (1993)", S["h1"]),
 P("The May edition asserted its gate sequence without primary support. It never needed to. "
   "Buffett published the sequence himself:", S["body"])]
el += q("The primary factors bearing upon this evaluation are: 1) The certainty with which the "
        "long-term economic characteristics of the business can be evaluated; 2) The certainty with "
        "which management can be evaluated, both as to its ability to realize the full potential of "
        "the business and to wisely employ its cash flows; 3) The certainty with which management "
        "can be counted on to channel the rewards from the business to the shareholders rather than "
        "to itself; 4) The purchase price of the business; 5) The levels of taxation and inflation "
        "that will be experienced [...]", "Buffett, 1993 letter [E3-10]")
fr = [
 ("Factor 1 — certainty about business economics", "Gates 1–2 (competence to judge; the moat itself)"),
 ("Factor 2 — certainty about management ability", "Gate 3, Dimension 2 (competence)"),
 ("Factor 3 — certainty about management fidelity", "Gate 3, Dimensions 1 & 3 (integrity, alignment)"),
 ("Factor 4 — the purchase price", "Gates 6 & 8 (valuation, last)"),
 ("Factor 5 — taxation and inflation", "Context throughout; Gate 6 rate anchor"),
]
rowsF = [[P(f"<b>{a}</b>", S["body"]), P(b, S["body"])] for a, b in fr]
t = Table(rowsF, colWidths=[3.4 * inch, 3.3 * inch])
t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                       ("LINEBELOW", (0, 0), (-1, -2), 0.25, PALE),
                       ("TOPPADDING", (0, 0), (-1, -1), 3),
                       ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
el += [t, SP(1, 6),
 P("Certainty about the business and its people comes before price — Gates 4 (verify the "
   "economics in the filings) and 5 (attack the thesis) are how an outside analyst manufactures "
   "the certainty Buffett takes as given. Gate 8 re-tests price from the market’s side. The "
   "sequence is his; the gate machinery is ours.", S["body"]), PageBreak()]

# ================= INTRODUCTION =================
el += [P("INTRODUCTION", S["h1"]),
 P("What this framework is", S["h2"]),
 P("A sequential, gate-based process for evaluating businesses as long-term investment candidates. "
   "Every load-bearing principle traces to the ledger; all machinery is labeled.", S["body"]),
 P("What this framework is not", S["h2"]),
 P("A screening tool, a momentum system, or a macro process.", S["body"])]
el += q("I am not in the business of predicting general stock market or business fluctuations. If "
        "you think I can do this, or think it is essential to an investment program, you should not "
        "be in the partnership.", "Buffett, Ground Rules, 1962 [E1-11]")
el += q("Games are won by players who focus on the playing field — not by those whose eyes are "
        "glued to the scoreboard.", "Buffett, 2013 letter [E5-03]")
el += [P("The sequence principle", S["h2"]),
 P("The eight gates are a sequence, not a checklist. The most common failure is starting at Gate 6: "
   "a DCF on a business you do not understand, run by management you have not evaluated, with a "
   "moat you have not verified, is arithmetic dressed up as conviction. The sequence follows "
   "Buffett’s five factors (previous page) and his summary of the whole method:", S["body"])]
el += q("In our view, though, investment students need only two well-taught courses — How to Value "
        "a Business, and How to Think About Market Prices.",
        "Buffett, 1996 letter [E3-14 context]")
el += [P("The behavioral principle", S["h2"])]
el += q("You will be right, over the course of many transactions, if your hypotheses are correct, "
        "your facts are correct, and your reasoning is correct. True conservatism is only possible "
        "through knowledge and reason.", "Buffett, 1961 partnership letter [E1-05]")
el += q("We derive no comfort because important people, vocal people, or great numbers of people "
        "agree with us. Nor do we derive comfort if they don’t. A public opinion poll is no "
        "substitute for thought.", "Buffett, 1964 partnership letter [E1-06]")
el += [PageBreak()]

# ================= GATE 1 =================
el += [P("GATE 1 — CIRCLE OF COMPETENCE", S["h1"])]
el += q("What an investor needs is the ability to correctly evaluate selected businesses. Note that "
        "word “selected”: You don’t have to be an expert on every company, or even many. You only "
        "have to be able to evaluate companies within your circle of competence. The size of that "
        "circle is not very important; knowing its boundaries, however, is vital.",
        "Buffett, 1996 letter [E3-16]. Concept present by 1964: “When we really sit back with a smile "
        "on our face is when we run into a situation we can understand...” [E1-07]")
el += q("Every person is going to have a circle of competence. And it’s going to be very hard to "
        "enlarge that circle. [...] You have to figure out where you’ve got an edge.",
        "Munger, USC 1994, PCA Talk 2 [E3-18]")
el += q("You’ve got to have models in your head. And you’ve got to array your experience — both "
        "vicarious and direct — on this latticework of models.",
        "Munger, USC 1994, PCA Talk 2 [E3-19] — how the circle is built")
el += [rule_card("GATE 1 RULE", [
   P("Can you independently verify the moat claim without relying on management’s description? "
     "If no — stop. “I don’t know” is a valid and complete answer.", S["cardbody"]),
   P("“Focus on the future productivity of the asset you are considering. If you don’t feel "
     "comfortable making a rough estimate of the asset’s future earnings, just forget it and move "
     "on. [...] omniscience isn’t necessary; you only need to understand the actions you undertake.” "
     "— Buffett, 2013 letter [E5-02]", S["quote"])]),
 SP(1, 8), P("Questions to answer", S["h2"]),
 P("• Do you understand how the business makes money at the unit-economics level?", S["bullet"]),
 P("• Can you identify the primary cost drivers without reading the annual report?", S["bullet"]),
 P("• Do you have an informational edge, or publicly available narrative? (Good ideas are rare and "
   "subject to competitive appropriation — OM-13.)", S["bullet"]),
 P("• For multi-segment businesses: can you evaluate each segment independently?", S["bullet"]),
 P("Common failure modes", S["h2"]),
 P("• Confusing familiarity with understanding — using a product is not understanding its economics.", S["bullet"]),
 P("• Assuming domain expertise transfers — industry employment gives context, not analytical edge.", S["bullet"]),
 P("• Mistaking narrative for analysis — a thesis built on management’s words is outside the circle.", S["bullet"]),
 P("Acceptance criteria", S["h2"]),
 P("You can describe the moat mechanism in your own words without quoting management.", S["body"]),
 PageBreak()]

# ================= GATE 2 =================
el += [P("GATE 2 — MOAT IDENTIFICATION", S["h1"]),
 P("The corpus test comes first; the taxonomy is a labeled convention.", S["small"])]
el += q("The key to investing is not assessing how much an industry is going to affect society, or "
        "how much it will grow, but rather determining the competitive advantage of any given "
        "company and, above all, the durability of that advantage.",
        "Buffett, Fortune, Nov 22 1999 [E4-08] — the quote the May edition misattributed to the "
        "1986 letter, now on the shelf and verified (essay added to corpus 2026-07-14)")
el += q("An economic franchise arises from a product or service that: (1) is needed or desired; "
        "(2) is thought by its customers to have no close substitute and; (3) is not subject to price "
        "regulation. The existence of all three conditions will be demonstrated by a company’s "
        "ability to regularly price its product or service aggressively and thereby to earn high "
        "rates of return on capital. Moreover, franchises can tolerate mis-management.",
        "Buffett, 1991 letter [E3-03] — the franchise test: pricing power proven in returns on capital")
el += q("A truly great business must have an enduring “moat” that protects excellent returns on "
        "invested capital. The dynamics of capitalism guarantee that competitors will repeatedly "
        "assault any business “castle” that is earning high returns.",
        "Buffett, 2007 letter [E4-03]. First moat: GEICO’s cost advantage, 1986 [E2-10]")
el += q("Our criterion of “enduring” causes us to rule out companies in industries prone to rapid "
        "and continuous change. [...] A moat that must be continuously rebuilt will eventually be no "
        "moat at all. Additionally, this criterion eliminates the business whose success depends on "
        "having a great manager.", "Buffett, 2007 letter [E4-04]")
el += q("When our long-term competitive position improves as a result of these almost unnoticeable "
        "actions, we describe the phenomenon as “widening the moat.” [...] when short-term and "
        "long-term conflict, widening the moat must take precedence.",
        "Buffett, 2005 letter [E4-02] — moat DIRECTION is what monitoring watches")
el += q("businesses logically are worth far more than net tangible assets when they can be expected "
        "to produce earnings on such assets considerably in excess of market rates of return. The "
        "capitalized value of this excess return is economic Goodwill.",
        "Buffett, 1983 letter appendix [E2-04]; “economic goodwill is much like land” — 1999 letter [E4-07]")
el += [rule_card("GATE 2 RULE", [
   P("Never assess a conglomerate as a single moat. Evaluate each business segment independently "
     "(OM-5: “consolidated reported earnings may reveal relatively little about our true economic "
     "performance”). Name the mechanism that stops a well-capitalized competitor — then prove the "
     "moat’s direction with a metric, not a claim.", S["cardbody"])]), SP(1, 8),
 source_class_box("convention", [
   P("The four-type taxonomy (switching cost / network effect / intangible asset / cost advantage) "
     "is Morningstar/Dorsey’s systematization, kept because it is operationally useful. Buffett "
     "himself named two types: low-cost producer and world-wide brand [E4-03]. The 8-quarter metric "
     "trend, the two-consecutive-quarters signal rule, and the metric menu (NRR, MAU, brand "
     "premium, relative gross margin) are conventions. The moat-class fade structure (wide "
     "10yr+15yr / narrow 10yr+10yr / none 5yr+5yr) is a convention inspired by, not derived from, "
     "[E2-19].", S["cardbody"])]), SP(1, 8),
 P("Acceptance criteria", S["h2"]),
 P("Franchise test answered per segment with the pricing-power evidence named; moat direction "
   "(widening / stable / narrowing) supported by a metric trend from primary filings.", S["body"]),
 PageBreak()]

# ================= GATE 3 =================
el += [P("GATE 3 — MANAGEMENT INTEGRITY", S["h1"])]
el += q("We will be candid in our reporting to you, emphasizing the pluses and minuses important in "
        "appraising business value. Our guideline is to tell you the business facts that we would "
        "want to know if our positions were reversed. We owe you no less. [...] The CEO who misleads "
        "others in public may eventually mislead himself in private.",
        "An Owner’s Manual, principle 12 (1983) — the candor standard. (The May edition cited the "
        "1989 letter; the word does not appear there — claims_audit C05.)")
el += q("At Berkshire you will find no “big bath” accounting maneuvers or restructurings nor any "
        "“smoothing” of quarterly or annual results.",
        "An Owner’s Manual, principle 12 — the red-flag list")
el += q("if you get an intelligent, energetic guy, or woman, who is pursuing a course of action "
        "which, if put on the front page, you know, would make you very unhappy, you can get in a "
        "lot of trouble.", "Buffett, 2016 annual meeting (recounting the integrity-energy-intelligence "
        "maxim he attributes to another) [claims_audit C18] — transcription source")
el += q("My most surprising discovery: the overwhelming importance in business of an unseen force "
        "that we might call “the institutional imperative.” [...] rationality frequently wilts when "
        "the institutional imperative comes into play.",
        "Buffett, 1989 letter [E2-18]; compact definition, 1990 letter: “the tendency of executives to "
        "mindlessly imitate the behavior of their peers” [E3-02]")
el += [rule_card("GATE 3 RULE", [
   P("Evaluate three dimensions in sequence; a failure on INTEGRITY disqualifies regardless of the "
     "other two. Evidence from primary sources only: 10-K, 10-Q, 20-F, 6-K, earnings-call "
     "transcripts.", S["cardbody"])]), SP(1, 8),
 P("Dimension 1 — Integrity (binary)", S["h2"]),
 P("• Unflattering information volunteered, or disclosed only when required? Metric used verbally "
   "when favorable and dropped when it deteriorates? Restatements, SEC letters, disclosure failures? "
   "ONE DELIBERATE DECEPTION = DISQUALIFICATION.", S["bullet"]),
 P("Dimension 2 — Competence", S["h2"]),
 P("• Capital-allocation record above cost of capital over a full cycle (OM-3: per-share progress, "
   "not size). The retention test — “whether retention, over time, delivers shareholders at least "
   "$1 of market value for each $1 retained” (OM-9, with Buffett’s own 2009 correction).", S["bullet"]),
 P("• Buybacks only under the two conditions: ample funds AND “a material discount to the "
   "company’s intrinsic business value, conservatively calculated” — 2011 letter [E5-01]; 1984 "
   "endorsement [E2-06].", S["bullet"]),
 P("Dimension 3 — Alignment", S["h2"]),
 P("• “We eat our own cooking” (OM-2): wealth in shares held, not options; compensation not built "
   "on adjusted metrics; shareholders addressed as partners (OM-1).", S["bullet"]),
 P("Sequence note", S["h2"])]
el += q("when a management with a reputation for brilliance tackles a business with a reputation "
        "for bad economics, it is the reputation of the business that remains intact.",
        "Buffett, 1989 letter [E2-17] — which is why Gate 2 precedes Gate 3")
el += [P("Acceptance criteria", S["h2"]),
 P("Clean integrity record; competence and alignment positive; any integrity flag documented in "
   "writing before proceeding.", S["body"]), PageBreak()]

# ================= GATE 4 =================
el += [P("GATE 4 — FINANCIAL QUALITY", S["h1"])]
el += q("we can gain some insights about what may be called “owner earnings.” These represent (a) "
        "reported earnings plus (b) depreciation, depletion, amortization, and certain other non-cash "
        "charges such as Company N’s items (1) and (4) less (c) the average annual amount of "
        "capitalized expenditures for plant and equipment, etc. that the business requires to fully "
        "maintain its long-term competitive position and its unit volume. (If the business requires "
        "additional working capital to maintain its competitive position and unit volume, the "
        "increment also should be included in (c).)",
        "Buffett, 1986 letter appendix [E2-08] — the COMPLETE definition. The May edition dropped the "
        "working-capital clause from its formula (claims_audit C01); the 1997 meeting confirms "
        "practitioners read (c) as “maintenance capital spending and working capital requirements.”")
el += [rule_card("THE OWNER EARNINGS FORMULA — AS BUFFETT DEFINED IT", [
   P("OWNER EARNINGS = Net income + D&amp;A and other non-cash charges − Maintenance capex − "
     "required working-capital increment", S["cardbody"]),
   P("Pull every figure from primary filings. No analyst estimates, no adjusted metrics, no "
     "consensus anchoring. Never adjusted EBITDA.", S["cardbody"])]), SP(1, 8)]
el += q("Our owner-earnings equation does not yield the deceptively precise figures provided by "
        "GAAP, since (c) must be a guess — and one sometimes very difficult to make. Despite this "
        "problem, we consider the owner earnings figure, not the GAAP figure, to be the relevant item "
        "for valuation purposes [...] We agree with Keynes’s observation: “I would rather be vaguely "
        "right than precisely wrong.”", "Buffett, 1986 letter appendix [E2-09]")
el += q("The primary test of managerial economic performance is the achievement of a high earnings "
        "rate on equity capital employed (without undue leverage, accounting gimmickry, etc.) and not "
        "the achievement of consistent gains in earnings per share.", "Buffett, 1979 letter [E2-01]")
el += q("Leaving the question of price aside, the best business to own is one that over an extended "
        "period can employ large amounts of incremental capital at very high rates of return.",
        "Buffett, 1992 letter [E3-05]; Munger’s quantitative rendering — 6% vs 18% on capital — "
        "PCA Talk 2 [E3-17]")
el += q("look-through earnings, which consist of: (1) the operating earnings reported in the "
        "previous section, plus; (2) the retained operating earnings of major investees that, under "
        "GAAP accounting, are not reflected in our profits, less; (3) an allowance for the tax that "
        "would be paid [...]", "Buffett, 1991 letter [E3-04] — the partial-ownership analog (OM-6); "
        "absent from the May edition entirely")
el += [P("SBC and dilution", S["h2"])]
el += q("If options aren’t a form of compensation, what are they?",
        "Buffett, 1992 letter; “To say ‘stock-based compensation’ is not an expense is even more "
        "cavalier.” — 2016 letter [E5-06]. Issuance-for-value: OM-10.")
el += [source_class_box("convention", [
   P("Operational thresholds are ours: maintenance-capex bands (65–70% capital-intensive / 20–30% "
     "asset-light / 50% mixed, overridden by any management-disclosed split); the SBC-materiality "
     "deduction trigger at 15% of OE; ROIC &gt; 15% as the quantitative moat check (the corpus gives "
     "the TEST [E2-01, E3-05, E3-17], not the number — the May edition’s “Munger’s primary moat "
     "confirmation test” attribution was false, claims_audit C25); the 8-quarter margin-stability "
     "check.", S["cardbody"])]), SP(1, 8),
 P("Fortress balance sheet", S["h2"])]
el += q("We use debt sparingly. We will reject interesting opportunities rather than over-leverage "
        "our balance sheet. (As one of the Indianapolis “500” winners said: “To finish first, you "
        "must first finish.”)", "An Owner’s Manual, principle 7")
el += q("When assets are twenty times equity — a common ratio in this industry — mistakes that "
        "involve only a small portion of assets can destroy a major portion of equity.",
        "Buffett, 1990 letter, on banking [E3-02 context] — the corpus basis for the leverage "
        "ceiling below")
el += [source_class_box("amendment", [
   P("<b>THE FORTRESS TEST, TWO TRACKS (ratified 2026-07-15, PENDING RULINGS.md Ruling 2).</b> "
     "Non-financial businesses pass on SURVIVAL, not net-cash: can the business service its debt "
     "and fund operations through a 50% OE decline sustained for 2 consecutive years without "
     "existential risk — judged via credit rating, undrawn liquidity vs. near-term maturities, and "
     "a termed-out (not cliff-concentrated) debt schedule. Ordinary investment-grade leverage "
     "serving routine capital needs is NOT a disqualifier on its own. Financial businesses (banks, "
     "insurers, anything balance-sheet or float-levered) must ALSO clear a hard mechanical ceiling: "
     "assets ÷ equity &gt; 10:1 is an AUTOMATIC FAIL, no exception, no judgment call. Retroactive "
     "validation: this ceiling mechanically rejects Citigroup mid-2007 (19:1 leverage; −95% "
     "followed) while the prior blanket net-cash rule had eliminated ordinary resilient industrials "
     "(Home Depot, Sherwin-Williams) for carrying normal corporate debt.", S["cardbody"])])]
el += [P("Acceptance criteria", S["h2"]),
 P("Owner earnings calculable from filings per the complete formula; growing (or a written, "
   "evidence-backed case that a decline is cyclical, not secular); SBC treated as cost; balance "
   "sheet passes the two-track fortress test above.", S["body"]), PageBreak()]

# ================= GATE 5 =================
el += [P("GATE 5 — INVERSION", S["h1"])]
el += q("It is in the nature of things, as Jacobi knew, that many hard problems are best solved only "
        "when they are addressed backward.",
        "Munger, Harvard School commencement, 1986 — PCA Talk 1 [E2-20]. (The May edition dated this "
        "to USC 1994 — claims_audit C26.)")
el += q("it is not enough to think problems through forward. You must also think in reverse, much "
        "like the rustic who wanted to know where he was going to die so that he’d never go there. "
        "[...] that is why the great algebraist Carl Jacobi so often said, “Invert, always invert”",
        "Munger, Stanford Law, 1996 — PCA Talk 3 [E3-22]")
el += q("Darwin’s result was due in large measure to his working method, which [...] always gave "
        "priority attention to evidence tending to disconfirm whatever cherished and hard-won theory "
        "he already had.",
        "Munger, PCA Talk 1 [E2-21]. (The May edition’s “hold two opposing ideas” line was F. Scott "
        "Fitzgerald’s, not Munger’s — claims_audit C27.)")
el += [rule_card("GATE 5 RULE", [
   P("Before building any DCF, attempt to destroy the thesis. This gate cannot be skipped.", S["cardbody"])]),
 SP(1, 8),
 P("The inversion process", S["h2"]),
 P("• STEP A — List every assumption the bull case requires. If you cannot list them, you have no "
   "thesis.", S["bullet"]),
 P("• STEP B — For each assumption, construct the complete-failure scenario (the Darwin discipline, "
   "[E2-21]).", S["bullet"]),
 P("• STEP C — Check whether management has addressed each scenario on the record — filings or "
   "earnings transcripts only.", S["bullet"]),
 P("• STEP D — Score each: [D] Direct / [DS] Structural / [P] Partial / [U] Unanswered.", S["bullet"]),
 P("Mandatory inversions", S["h2"]),
 P("• MOAT DESTRUCTION — what kills it? (“A moat that must be continuously rebuilt will eventually "
   "be no moat at all” [E4-04].)", S["bullet"]),
 P("• MANAGEMENT FAILURE — key person, succession, incentives; the institutional imperative "
   "[E2-18].", S["bullet"]),
 P("• BALANCE-SHEET STRESS — trough economics; the 50%-for-2-years drill (convention).", S["bullet"]),
 P("• THESIS-BREAKING METRIC — define it before entry, in writing [E1-02].", S["bullet"]),
 SP(1, 4),
 source_class_box("convention", [
   P("The D/DS/P/U scoring notation and the specific mandatory-inversion list are conventions "
     "implementing [E2-20/E2-21/E3-22]. The unpriced risk is the one management has never been "
     "asked about; an UNANSWERED score on a mandatory inversion requires written justification to "
     "proceed.", S["cardbody"])]),
 SP(1, 8), P("Acceptance criteria", S["h2"]),
 P("Every material inversion scored against primary-source responses; the thesis-breaking metric "
   "committed to in writing.", S["body"]), PageBreak()]

# ================= GATE 6 =================
el += [P("GATE 6 — VALUATION", S["h1"]),
 P("Two books, honestly labeled. Book One is corpus-grounded and field-tested; Book Two is a "
   "confessed convention. The yardstick is never a perpetuity input in either book.", S["small"])]
el += q("the formula for valuing all assets that are purchased for financial gain has been unchanged "
        "since it was first laid out by a very smart man in about 600 B.C. [...] The oracle was Aesop "
        "and his enduring, though somewhat incomplete, investment insight was “a bird in the hand is "
        "worth two in the bush.” To flesh out this principle, you must answer only three questions. "
        "How certain are you that there are indeed birds in the bush? When will they emerge and how "
        "many will there be? What is the risk-free interest rate (which we consider to be the yield "
        "on long-term U.S. bonds)?", "Buffett, 2000 letter [E4-01]")
el += q("The risk-free rate is used merely to equate one item to another. [...] obviously, we can "
        "always buy the government bonds. So that becomes the yardstick rate. [...] Now, it gets into "
        "degree of certainty, too. But it’s the yardstick rate.",
        "Buffett, 1997 annual meeting [E3-23] — comparison standard, NOT a build-up input")
el += q("in a world of 7 percent long-term bond rates [...] we would certainly want to think we were "
        "discounting future after-tax streams of cash at at least a 10 percent rate. But that will "
        "depend on the certainty we feel about the business.",
        "Buffett, 1994 annual meeting [E3-13]. (The May edition’s “I use the 30-year Treasury rate. "
        "That’s my yardstick” quote does not exist in the transcript — claims_audit C10.)")
el += q("the investment analyst must himself estimate the future “coupons.” [...] The investment "
        "shown by the discounted-flows-of-cash calculation to be the cheapest is the one that the "
        "investor should purchase", "Buffett, 1992 letter [E3-07]; the growing-coupon reading of "
        "equities: 1981 letter [E2-02, E2-03]")
el += [SP(1, 4), source_class_box("amendment", [
   P("<b>STEP 0 — RATE REFRESH.</b> Re-pull the sovereign 30-year yield on every analysis date; a "
     "move of more than 50bp since the last valuation triggers revaluation of the affected names. "
     "Primary basis: the Owner’s Manual — intrinsic value is “an estimate that must be changed if "
     "interest rates move.”", S["cardbody"]),
   P("<b>BOOK ONE — THE BUFFETT STATUTE (wonderful-at-fair; starter size).</b> The current-tier "
     "verified owner-earnings yield must meet or exceed the sovereign 30-year yield, plus +1% for "
     "small/mid caps, +2% for micro/illiquid names; hurdle floored at 4%. Generational moats may "
     "enter at 70% of hurdle (the Coca-Cola clause). Authorities for the comparison-hurdle form: "
     "[E4-01], [E3-23], [E3-13]; the growing-coupon reading: “it seems reasonable to think of it "
     "as an equity coupon” — Fortune 1977 [E2-22]. Certainty is handled by analysis and the moat "
     "class, never by an added risk premium.", S["cardbody"]),
   P("<b>THE SCREAM TEST.</b> A verdict must agree at the bare-yardstick rate and at the Book Two "
     "build-up rate; if the verdicts diverge, the opportunity is a whisper, not a scream — pass.", S["cardbody"]),
   P("<b>OE RANGE ANCHORING.</b> Buy prices are computed from the LOWEST verified owner-earnings "
     "tier; thresholds rise only on published filings.", S["cardbody"])]), SP(1, 8),
 source_class_box("convention", [
   P("<b>BOOK TWO — BUILD-UP DCF (wonderful-at-cheap; full size).</b> WACC = sovereign long yield + "
     "equity risk premium 5–6% + company-specific 0–2% (≈10.5% for a US large-cap of quality); "
     "three scenarios (Bear/Base/Bull); 10-year explicit period; moat-class fades (15/10/5 yr); "
     "terminal growth Bear 2% / Base &amp; Bull 3% (always &lt; WACC); minimum MOS 20% (30% "
     "no-moat): max buy = IV × 0.80 (0.70). All of it is OURS — the ERP build-up is not Buffett’s "
     "method and the corpus actively contradicts attributing it to him [E3-23]. Non-USD: discount "
     "in the earnings currency at the relevant sovereign anchor; convert at the end.", S["cardbody"])]),
 SP(1, 8), P("Margin of safety", S["h2"])]
el += q("we insist on a margin of safety in our purchase price. If we calculate the value of a "
        "common stock to be only slightly higher than its price, we’re not interested in buying. We "
        "believe this margin-of-safety principle, so strongly emphasized by Ben Graham, to be the "
        "cornerstone of investment success.",
        "Buffett, 1992 letter [E3-08]; earliest form 1961 [E1-04]; late form: “Never risk permanent "
        "loss of capital.” — 2023 letter [E5-05]")
el += q("It is better to be approximately right than precisely wrong.",
        "Buffett, 1993 letter [E3-12] — the sensitivity-grid principle: the thesis must hold across "
        "the majority of the WACC × terminal-growth table")
el += [P("Acceptance criteria", S["h2"]),
 P("Book One hurdle met on the lowest verified OE tier at today’s refreshed rate; Book Two IV and "
   "MOS computed; Scream Test concordant; sensitivity table majority-green.", S["body"]),
 PageBreak()]

# ================= GATE 7 =================
el += [P("GATE 7 — POSITION SIZING AND MONITORING", S["h1"])]
el += q("We believe that a policy of portfolio concentration may well decrease risk if it raises, as "
        "it should, both the intensity with which an investor thinks about a business and the "
        "comfort-level he must feel with its economic characteristics before buying into it.",
        "Buffett, 1993 letter [E3-11]; the 40% ground rule, 1965 [E1-08]; expected-value framing "
        "[E1-09]")
el += q("the wise ones bet heavily when the world offers them that opportunity. They bet big when "
        "they have the odds. And the rest of the time, they don’t. It’s just that simple.",
        "Munger, USC 1994, PCA Talk 2 [E3-21]. (This, not the Kelly Criterion, is the corpus basis "
        "for sizing — claims_audit C28.)")
el += q("when we own portions of outstanding businesses with outstanding managements, our favorite "
        "holding period is forever.",
        "Buffett, 1988 letter [E2-14] — note the CONDITION: outstanding business AND management")
el += q("Charlie and I let our marketable equities tell us by their operating results — not by their "
        "daily, or even yearly, price quotations — whether our investments are successful.",
        "Buffett, 1987 letter [E2-13]; “Lethargy bordering on sloth remains the cornerstone of our "
        "investment style.” — 1990 letter [E3-01]; “Inactivity strikes us as intelligent behavior.” "
        "— 1996 letter [E3-15]")
el += [rule_card("BEFORE ENTRY — DEFINE AND COMMIT IN WRITING", [
   P("“I believe in establishing yardsticks prior to the act; retrospectively, almost anything can "
     "be made to look good in relation to something or other.” — Buffett, 1961 [E1-02]", S["quote"]),
   P("The thesis-confirming metric; the thesis-breaking metric; the next catalyst date.", S["cardbody"])]),
 SP(1, 8), P("The only valid reasons to sell", S["h2"]),
 P("• Thesis-breaking metric confirmed deteriorating (convention: two consecutive quarters) — EXIT.", S["bullet"]),
 P("• Management integrity failure — EXIT.", S["bullet"]),
 P("• Price materially above conservatively calculated value — begin reducing (OM-14: overvaluation "
   "is as unwelcome as undervaluation; the 120% trigger is a convention).", S["bullet"]),
 P("• A materially superior opportunity — evaluate; remember “There’s a cost to activity” has NO "
   "corpus source [C20]; the corpus voice is Munger’s: sit-on-your-ass investing [E4-06].", S["bullet"]),
 P("• NEVER on price decline alone; falling prices are the buyer’s friend (OM-4; [E4-05]).", S["bullet"]),
 SP(1, 4),
 callout([P("Scope caution the May edition missed: OM-11’s never-sell language covers CONTROLLED "
            "businesses — the Owner’s Manual says so explicitly in its 2016 clarification. For "
            "marketable securities the authority is [E2-13]/[E2-14]: quality-conditional patience, "
            "verdicts from operating results.", S["cardbody"])]),
 SP(1, 4), source_class_box("amendment", [
   P("OE RANGE ANCHORING (monitoring side): sizing additions use the lowest VERIFIED owner-earnings "
     "tier; thresholds rise only on published filings. Rerun Gates 4–6 when reported OE moves the "
     "base more than 10% (the 10% is a convention).", S["cardbody"])]),
 SP(1, 8),
 P("THE FINAL RULE: once the framework is complete and the entry price is met — do nothing. "
   "“Inactivity strikes us as intelligent behavior.” [E3-15]", S["body"]), PageBreak()]

# ================= GATE 8 =================
el += [P("GATE 8 — REVERSE DCF", S["h1"]),
 P("The May edition confessed this gate was “not a Buffett or Munger original.” The frame, it "
   "turns out, is Munger’s own:", S["small"])]
el += q("The model I like — to sort of simplify the notion of what goes on in a market for common "
        "stocks — is the pari-mutuel system at the racetrack. [...] the bad horse pays 100 to 1, "
        "whereas the good horse pays 3 to 2. Then it’s not clear which is statistically the best bet.",
        "Munger, USC 1994, PCA Talk 2 [E3-20] — the price already encodes the crowd’s belief; the "
        "question is whether the odds are wrong")
el += [rule_card("GATE 8 RULE", [
   P("Run after the forward valuation. Ask what the market must believe for today’s price to be "
     "fair — then test that belief against the record.", S["cardbody"])]), SP(1, 8),
 P("The two core questions", S["h2"]),
 P("• Q1 — growth held fixed: what OE base does the price imply? Below trough = pessimism priced "
   "in; above peak = heroic, do not enter.", S["bullet"]),
 P("• Q2 — OE base held fixed: what year-1 growth does the price imply? Score across deceleration "
   "profiles: ACHIEVABLE / STRETCHED / HEROIC.", S["bullet"]),
 SP(1, 4), source_class_box("convention", [
   P("The mechanics — four deceleration profiles (1/1.5/2/2.5pp per year), the asymmetry ratio "
     "(Base-IV upside ÷ Bear-IV downside; &gt;3:1 high conviction, 2–3:1 acceptable, &lt;2:1 wait) — "
     "are conventions implementing [E3-20] and the expected-value discipline of [E1-09].", S["cardbody"])]),
 SP(1, 8), P("Acceptance criteria", S["h2"]),
 P("Implied OE at or below current; implied growth achievable on at least two profiles; asymmetry "
   "above 2:1; price below the Book Two entry threshold (and Book One hurdle already met).", S["body"]),
 PageBreak()]

# ================= QUICK REFERENCE =================
el += [P("QUICK REFERENCE", S["h1"])]
qr = [
 ("Gate 1", "Verify the moat without management’s words; future productivity or pass [E3-16, E5-02]"),
 ("Gate 2", "Franchise test + moat direction with a filing-sourced metric [E3-03, E4-02]"),
 ("Gate 3", "Candor (OM-12) → competence (OM-9, E5-01) → alignment (OM-2); one deception = out"),
 ("Gate 4", "OE = NI + D&A − maint. capex − req’d WC [E2-08]; look-through for partial stakes [E3-04]"),
 ("Gate 5", "Invert: list assumptions, build failure scenarios, score D/DS/P/U [E2-20, E3-22]"),
 ("Gate 6", "Step 0 rate refresh → Book One Statute hurdle (FA) → Book Two DCF + 20% MOS (convention) → Scream Test (FA)"),
 ("Gate 7", "Pre-committed metrics [E1-02]; bet heavily when odds favor [E3-21]; sell only on thesis/integrity/valuation"),
 ("Gate 8", "Pari-mutuel check [E3-20]: implied OE, implied growth, asymmetry ratio"),
]
rowsQ = [[P(f"<b>{a}</b>", S["body"]), P(b, S["body"])] for a, b in qr]
t = Table(rowsQ, colWidths=[0.9 * inch, 5.8 * inch])
t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                       ("LINEBELOW", (0, 0), (-1, -2), 0.25, PALE),
                       ("TOPPADDING", (0, 0), (-1, -1), 3),
                       ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
el += [t, SP(1, 10),
 callout([P("Source classes at a glance — LEDGER quotes: the spine, verifiable in two minutes. "
            "CONVENTIONS: every number you can argue with (fades, 20%/30%, 15% SBC, 10.5%, 8 "
            "quarters, 3:1). FIELD AMENDMENTS: the Statute, Step 0, Scream Test, range anchoring.",
            S["cardbody"])]), PageBreak()]

# ================= GLOSSARY =================
el += [P("GLOSSARY", S["h1"])]
gl = [
 ("CIRCLE OF COMPETENCE", "The domain where you can evaluate businesses independently. “Knowing its boundaries... is vital.” [E3-16]; Munger’s edge test [E3-18]."),
 ("ECONOMIC GOODWILL", "The capitalized value of returns above market rates on tangible assets [E2-04]; “much like land” [E4-07]."),
 ("ECONOMIC FRANCHISE", "Needed/desired; no close substitute; unregulated — proven by aggressive pricing and high returns on capital [E3-03]."),
 ("FLOAT", "“The investment income that an insurer earns from holding on to policyholders’ funds” [E2-11]; OM-7’s benign leverage."),
 ("INSTITUTIONAL IMPERATIVE", "“The tendency of executives to mindlessly imitate the behavior of their peers” [E3-02]."),
 ("INTRINSIC VALUE", "“The discounted value of the cash that can be taken out of a business during its remaining life” (Owner’s Manual). An estimate that must change when rates move."),
 ("LOOK-THROUGH EARNINGS", "Reported operating earnings + retained earnings of investees − tax allowance [E3-04]."),
 ("MARGIN OF SAFETY", "“The cornerstone of investment success” [E3-08]; “Never risk permanent loss of capital” [E5-05]. The 20%/30% floors are conventions."),
 ("MOAT", "A durable barrier protecting high returns on invested capital [E4-03]; first used of GEICO’s cost advantage [E2-10]."),
 ("OWNER EARNINGS", "See Gate 4 — the complete 1986 definition including the working-capital increment [E2-08]."),
 ("RISK", "“The possibility of loss or injury” — not volatility, not beta [E3-09]; permanent loss vs quotational variation [E1-10]."),
 ("YARDSTICK", "A pre-committed standard of comparison [E1-02]. As a rate: the sovereign long bond, used “merely to equate one item to another” [E3-23] — never a perpetuity input."),
]
for term, defn in gl:
    el += [P(f"<b>{term}</b> — {defn}", S["body"])]
el += [PageBreak()]

# ================= APPENDICES =================
el += [P("APPENDIX A — PRIMARY-SOURCE READING ORDER", S["h1"]),
 P("Tier 1 — foundational", S["h2"]),
 P("• Buffett Partnership letters, 1957–1970 (29 letters; the Ivey compilation). The method before "
   "the quality evolution; the ground rules; the 1967 qualitative pivot [E1-15].", S["bullet"]),
 P("• Berkshire letters 1977–1989 — the framework crystallizes: 1979 ROE test, 1983 goodwill "
   "appendix, 1986 owner-earnings appendix, 1987 Mr. Market, 1989 Mistakes of the First "
   "Twenty-Five Years.", S["bullet"]),
 P("• Poor Charlie’s Almanack, the 11 talks (Stripe Press free web edition) — Talks 1–3 "
   "especially.", S["bullet"]),
 P("Tier 2 — depth", S["h2"]),
 P("• Berkshire letters 1990–2025 — 1991 franchises; 1992 value/growth and DCF; 1993 five risk "
   "factors and concentration; 1996 two courses; 2000 Aesop; 2005 widening; 2007 great/good/"
   "gruesome; 2013 basics; 2014 (with the Special Letters) the 50-year retrospectives; 2023 "
   "Munger memorial.", S["bullet"]),
 P("• Annual meeting transcripts 1994–2025 (third-party transcriptions — flag when quoting): 1994 "
   "and 1997 for the discount-rate and yardstick passages; 2000 for value-investing and "
   "competitive-advantage exchanges.", S["bullet"]),
 P("• An Owner’s Manual — reread annually; it is the spine.", S["bullet"]),
 P("Context (read if present, never cite)", S["h2"]),
 P("• Wesco letters 1997–2009 (on the shelf but operational in content [E5-07]); biographies and "
   "commentary; secondary quote compilations — where most of the May edition’s errors came from.", S["bullet"]),
 SP(1, 8),
 P("APPENDIX B — PORTFOLIO TRACKING TOOLS", S["h1"]),
 P("The price ladder, watchlist, position log, and eliminated-companies register are memory and "
   "discipline tools (see the Workbook, Sheets 8–10). Two corpus anchors: pre-committed yardsticks "
   "[E1-02], and OM-15’s honest self-benchmark — compare your results to the index and ask, "
   "“Otherwise, why do our investors need us?”", S["body"]),
 SP(1, 20), P(f"“{MOTTO}”", S["epigraph"]),
 P("A Framework for Long-Term Business Analysis — v3.0 — July 2026", S["epigraphsrc"])]

doc = NumberedDoc(os.path.abspath(OUT), "A Framework for Long-Term Business Analysis")
doc.build(el)
print("built:", os.path.abspath(OUT))

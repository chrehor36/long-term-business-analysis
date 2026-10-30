# -*- coding: utf-8 -*-
"""Generate: Principles — Complete Source Tracing v3.0 (July 2026).
47 principles in three classes. Every Class-A principle cites ledger rows
(principle_ledger.csv); conventions and field amendments are labeled.
Old(May)->new numbering map lives in CHANGELOG.md."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reportlab.platypus import KeepTogether, PageBreak, Paragraph, Spacer
from v3_style import GRAY, MOTTO, NumberedDoc, S, callout, source_class_box

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "Principles - Complete Source Tracing v3.0.pdf")
P, SP = Paragraph, Spacer
el = []

el += [SP(1, 70),
 P("PRINCIPLES —<br/>COMPLETE SOURCE TRACING", S["title"]), SP(1, 10),
 P("Companion to: A Framework for Long-Term Business Analysis", S["subtitle"]),
 SP(1, 6), P("VERSION 3.0 — JULY 2026", S["edition"]), SP(1, 24),
 P("48 principles in three honest classes: 36 traced to verbatim ledger quotations "
   "(principle_ledger.csv, 76 entries, sourced from the Buffett/Munger corpus in /BRK), "
   "3 confessed framework conventions, and 4 field amendments from live application. "
   "The May 2026 edition’s claim that “nothing is invented” is retired; what is invented "
   "is now labeled. Verification standard: any principle checkable against its source in "
   "under two minutes via the ledger row ID.", S["small"]),
 SP(1, 14), P(f"“{MOTTO}”", S["epigraph"]),
 P("— framework motto (our words)", S["epigraphsrc"]), PageBreak()]

def princ(num, title, body, cite, note=None):
    """Class A principle: ledger-cited."""
    fl = [P(f"PRINCIPLE {num} — {title}", S["h2"]),
          P(f"“{body}”", S["quote"]),
          P(cite, S["source"])]
    if note:
        fl.append(P(note, S["small"]))
    return KeepTogether(fl)

# ---------------- PART I: BUFFETT — THE METHOD ----------------
el += [P("PART I — LEDGER PRINCIPLES: THE INVESTOR AND THE BUSINESS (1–15)", S["h1"])]
el += [
princ(1, "PARTNERSHIP ATTITUDE",
 "Although our form is corporate, our attitude is partnership. [...] visualize yourself as a part "
 "owner of a business that you expect to stay with indefinitely, much as you might if you owned a "
 "farm or apartment house in partnership with members of your family.",
 "An Owner’s Manual, principle 1 (1983).",
 "Applied: Introduction; the stance from which every gate is run."),
princ(2, "PRE-COMMITTED YARDSTICKS",
 "I believe in establishing yardsticks prior to the act; retrospectively, almost anything can be "
 "made to look good in relation to something or other.",
 "Buffett, 1961 partnership letter [E1-02].",
 "Applied: Gate 7 — thesis metrics defined before entry; Workbook Sheets 6 and 9."),
princ(3, "TRUE CONSERVATISM = KNOWLEDGE AND REASON",
 "You will be right, over the course of many transactions, if your hypotheses are correct, your "
 "facts are correct, and your reasoning is correct. True conservatism is only possible through "
 "knowledge and reason.",
 "Buffett, 1961 partnership letter [E1-05]; restated 1964 [E1-06].",
 "Applied: Gates 1 and 5 — independence from consensus in both directions."),
princ(4, "CIRCLE OF COMPETENCE",
 "You only have to be able to evaluate companies within your circle of competence. The size of "
 "that circle is not very important; knowing its boundaries, however, is vital.",
 "Buffett, 1996 letter [E3-16]; Munger’s edge test, USC 1994 [E3-18]; concept by 1964 [E1-07].",
 "Applied: Gate 1."),
princ(5, "FUTURE PRODUCTIVITY OR WALK AWAY",
 "If you don’t feel comfortable making a rough estimate of the asset’s future earnings, just "
 "forget it and move on. [...] omniscience isn’t necessary; you only need to understand the "
 "actions you undertake.",
 "Buffett, 2013 letter [E5-02].",
 "Applied: Gate 1 acceptance; Gate 6 Step 1."),
princ(6, "THE FIVE RISK FACTORS",
 "1) The certainty with which the long-term economic characteristics of the business can be "
 "evaluated; 2) The certainty with which management can be evaluated [...]; 3) The certainty with "
 "which management can be counted on to channel the rewards [...] to the shareholders; 4) The "
 "purchase price of the business; 5) The levels of taxation and inflation [...]",
 "Buffett, 1993 letter [E3-10].",
 "Applied: the gate SEQUENCE itself — the framework’s structural authority."),
princ(7, "THE FRANCHISE TEST",
 "An economic franchise arises from a product or service that: (1) is needed or desired; (2) is "
 "thought by its customers to have no close substitute and; (3) is not subject to price "
 "regulation. [...] demonstrated by a company’s ability to regularly price its product or service "
 "aggressively and thereby to earn high rates of return on capital.",
 "Buffett, 1991 letter [E3-03].",
 "Applied: Gate 2 — the corpus-native moat test, ahead of any taxonomy."),
princ(8, "THE ENDURING MOAT",
 "A truly great business must have an enduring “moat” that protects excellent returns on invested "
 "capital. [...] A moat that must be continuously rebuilt will eventually be no moat at all.",
 "Buffett, 2007 letter [E4-03, E4-04]; first use (GEICO cost moat), 1986 [E2-10]; “widening the "
 "moat must take precedence,” 2005 [E4-02]; “Time is the friend of the wonderful business, the "
 "enemy of the mediocre,” 1989 [E2-19]; “the durability of that advantage” — Fortune 1999 [E4-08].",
 "Applied: Gate 2; monitoring direction in Gate 7."),
princ(9, "ECONOMIC GOODWILL",
 "businesses logically are worth far more than net tangible assets when they can be expected to "
 "produce earnings on such assets considerably in excess of market rates of return. The "
 "capitalized value of this excess return is economic Goodwill.",
 "Buffett, 1983 letter appendix [E2-04]; growth-like-land restatement, 1999 [E4-07].",
 "Applied: Gate 2 — intangible-moat economics. (May edition cited 1987 — corrected.)"),
princ(10, "THE BUSINESS BEATS THE MANAGER",
 "when a management with a reputation for brilliance tackles a business with a reputation for bad "
 "economics, it is the reputation of the business that remains intact.",
 "Buffett, 1989 letter [E2-17].",
 "Applied: Gate 2 precedes Gate 3; Gate 5 key-person inversion."),
princ(11, "CANDOR",
 "Our guideline is to tell you the business facts that we would want to know if our positions "
 "were reversed. [...] The CEO who misleads others in public may eventually mislead himself in "
 "private.",
 "An Owner’s Manual, principle 12 (1983). Red flags in the same principle: big-bath maneuvers, "
 "smoothing.",
 "Applied: Gate 3, Dimension 1. (May edition cited the 1989 letter; candor is not in it — C05.)"),
princ(12, "THE INSTITUTIONAL IMPERATIVE",
 "rationality frequently wilts when the institutional imperative comes into play.",
 "Buffett, 1989 letter [E2-18]; definition, 1990 letter [E3-02]. PCA checklist: “Avoid dealing "
 "with people of questionable character.”",
 "Applied: Gate 3; mandatory management-failure inversion in Gate 5."),
princ(13, "EAT YOUR OWN COOKING",
 "We eat our own cooking. [...] We want to make money only when our partners do and in exactly "
 "the same proportion.",
 "An Owner’s Manual, principle 2.",
 "Applied: Gate 3, Dimension 3 — alignment through owned shares, not options."),
princ(14, "THE RETENTION TEST",
 "We test the wisdom of retaining earnings by assessing whether retention, over time, delivers "
 "shareholders at least $1 of market value for each $1 retained.",
 "An Owner’s Manual, principle 9 — including Buffett’s published 2009 correction of his own "
 "1983 formulation.",
 "Applied: Gate 3, Dimension 2. Bondholder logic behind it: 1981 letter [E2-03]."),
princ(15, "BUYBACKS — TWO CONDITIONS",
 "Charlie and I favor repurchases when two conditions are met: first, a company has ample funds "
 "[...]; second, its stock is selling at a material discount to the company’s intrinsic business "
 "value, conservatively calculated.",
 "Buffett, 2011 letter [E5-01]; 1984 endorsement and greenmail condemnation [E2-06].",
 "Applied: Gate 3, Dimension 2."),
]
el += [PageBreak(),
 P("PART II — LEDGER PRINCIPLES: EARNINGS AND VALUE (16–28)", S["h1"])]
el += [
princ(16, "OWNER EARNINGS — THE COMPLETE FORMULA",
 "These represent (a) reported earnings plus (b) depreciation, depletion, amortization, and "
 "certain other non-cash charges [...] less (c) the average annual amount of capitalized "
 "expenditures for plant and equipment, etc. [...] (If the business requires additional working "
 "capital to maintain its competitive position and unit volume, the increment also should be "
 "included in (c).)",
 "Buffett, 1986 letter appendix [E2-08]; practitioner reading confirmed, 1997 meeting Q14.",
 "Applied: Gate 4; Workbook Sheet 5. The May formula omitted the working-capital clause — fixed."),
princ(17, "APPROXIMATELY RIGHT",
 "It is better to be approximately right than precisely wrong.",
 "Buffett, 1993 letter [E3-12]; Keynes original quoted by Buffett, 1986 appendix [E2-09].",
 "Applied: Gate 4 (OE is an estimate); Gate 6 Step 6 (sensitivity grid)."),
princ(18, "RETURNS ON CAPITAL, NOT EPS",
 "The primary test of managerial economic performance is the achievement of a high earnings rate "
 "on equity capital employed [...] and not the achievement of consistent gains in earnings per "
 "share.",
 "Buffett, 1979 letter [E2-01]; incremental-capital form, 1992 [E3-05].",
 "Applied: Gate 4. (Replaces the unsourced Wesco-meeting ROIC quotes — C21/C22.)"),
princ(19, "RETURNS CONVERGE TO BUSINESS RETURNS",
 "If the business earns 6 percent on capital over 40 years and you hold it for that 40 years, "
 "you’re not going to make much different than a 6 percent return, even if you originally buy it "
 "at a huge discount. Conversely, if a business earns 18 percent on capital over 20 or 30 years, "
 "even if you pay an expensive-looking price, you’ll end up with one hell of a result.",
 "Munger, USC 1994, PCA Talk 2 [E3-17].",
 "Applied: Gates 2/4; the quantitative heart of wonderful-at-fair."),
princ(20, "LOOK-THROUGH EARNINGS",
 "look-through earnings, which consist of: (1) the operating earnings [...], plus; (2) the "
 "retained operating earnings of major investees [...], less; (3) an allowance for the tax [...]",
 "Buffett, 1991 letter [E3-04]; An Owner’s Manual, principle 6.",
 "Applied: Gate 4 — partial-ownership analog of owner earnings. New in v3.0."),
princ(21, "SBC IS AN EXPENSE",
 "If options aren’t a form of compensation, what are they?",
 "Buffett, 1992 letter; “To say ‘stock-based compensation’ is not an expense is even more "
 "cavalier.” — 2016 letter [E5-06]; issuance-for-value, OM-10.",
 "Applied: Gate 4. (The 15% materiality trigger is Convention 44.)"),
princ(22, "DEBT SPARINGLY; FLOAT",
 "We use debt sparingly. We will reject interesting opportunities rather than over-leverage our "
 "balance sheet.",
 "An Owner’s Manual, principle 7; float defined, 1986 letter [E2-11].",
 "Applied: Gate 4 fortress test."),
princ(23, "INTRINSIC VALUE",
 "It is the discounted value of the cash that can be taken out of a business during its remaining "
 "life. [...] an estimate that must be changed if interest rates move or forecasts of future cash "
 "flows are revised.",
 "An Owner’s Manual, Intrinsic Value section.",
 "Applied: Gate 6 foundation; Step 0 rate refresh (Field Amendment 45)."),
princ(24, "AESOP’S THREE QUESTIONS",
 "How certain are you that there are indeed birds in the bush? When will they emerge and how many "
 "will there be? What is the risk-free interest rate (which we consider to be the yield on "
 "long-term U.S. bonds)?",
 "Buffett, 2000 letter [E4-01].",
 "Applied: Gate 6 — the entire valuation problem in three questions."),
princ(25, "THE YARDSTICK RATE",
 "The risk-free rate is used merely to equate one item to another. [...] it’s the yardstick rate.",
 "Buffett, 1997 meeting [E3-23]; certainty-adjusted form, 1994 meeting [E3-13].",
 "Applied: Gate 6 Book One. Never a perpetuity input; never an ERP build-up. (Replaces the "
 "fabricated “That’s my yardstick” quote — C10.)"),
princ(26, "EQUITIES ARE COUPON-BEARING",
 "the investment analyst must himself estimate the future “coupons.” [...] The investment shown by "
 "the discounted-flows-of-cash calculation to be the cheapest is the one that the investor should "
 "purchase",
 "Buffett, 1992 letter [E3-07]; frozen-coupon inflation form, 1981 [E2-02, E2-03]; “equity "
 "coupon” origin — Fortune 1977 [E2-22].",
 "Applied: Gate 6 — the growing-coupon reading behind the Statute."),
princ(27, "MARGIN OF SAFETY",
 "we insist on a margin of safety in our purchase price. [...] the cornerstone of investment "
 "success.",
 "Buffett, 1992 letter [E3-08]; earliest form 1961 [E1-04]; “Never risk permanent loss of "
 "capital.” — 2023 letter [E5-05].",
 "Applied: Gate 6 Step 5. Graham is named inside Buffett’s sentence — per the 2026-07-13 shelf "
 "amendment, that is how he appears throughout v3.0."),
princ(28, "VALUE AND GROWTH ARE JOINED",
 "Growth is always a component in the calculation of value [...] the very term “value investing” "
 "is redundant.",
 "Buffett, 1992 letter [E3-06]; “all intelligent investing is value investing” — Munger, 2000 "
 "meeting [E4-06].",
 "Applied: Gate 6 scenarios; kills the value-vs-growth false dichotomy."),
]
el += [PageBreak(),
 P("PART III — LEDGER PRINCIPLES: PRICE, TEMPERAMENT, AND ACTION (29–36)", S["h1"])]
el += [
princ(29, "MR. MARKET",
 "you should imagine market quotations as coming from a remarkably accommodating fellow named Mr. "
 "Market who is your partner in a private business. [...] the poor fellow has incurable emotional "
 "problems.",
 "Buffett retelling “Ben Graham, my friend and teacher,” 1987 letter [E2-12].",
 "Applied: Gates 6–8; the market serves, never instructs."),
princ(30, "OPERATING RESULTS ARE THE VERDICT",
 "Charlie and I let our marketable equities tell us by their operating results — not by their "
 "daily, or even yearly, price quotations — whether our investments are successful.",
 "Buffett, 1987 letter [E2-13]; “playing field, not scoreboard,” 2013 [E5-03].",
 "Applied: Gate 7 monitoring."),
princ(31, "NO MACRO",
 "I am not in the business of predicting general stock market or business fluctuations.",
 "Buffett, Ground Rules, 1962 [E1-11]; “Forming macro opinions [...] is a waste of time,” 2013 "
 "[E5-03].",
 "Applied: Introduction; scope discipline everywhere."),
princ(32, "CONCENTRATION",
 "a policy of portfolio concentration may well decrease risk if it raises, as it should, both the "
 "intensity with which an investor thinks about a business and the comfort-level he must feel "
 "with its economic characteristics before buying into it.",
 "Buffett, 1993 letter [E3-11]; the 40% ground rule, 1965 [E1-08]; expected-value framing "
 "[E1-09].",
 "Applied: Gate 7."),
princ(33, "BET HEAVILY WHEN THE ODDS FAVOR",
 "the wise ones bet heavily when the world offers them that opportunity. They bet big when they "
 "have the odds. And the rest of the time, they don’t. It’s just that simple.",
 "Munger, USC 1994, PCA Talk 2 [E3-21].",
 "Applied: Gate 7 sizing. (Replaces the Kelly Criterion attribution — zero corpus hits, C28.)"),
princ(34, "QUALITY-CONDITIONAL FOREVER",
 "when we own portions of outstanding businesses with outstanding managements, our favorite "
 "holding period is forever.",
 "Buffett, 1988 letter [E2-14]; sit-on-your-ass investing — Munger, 2000 meeting [E4-06]; "
 "“Lethargy bordering on sloth...” 1990 [E3-01]; “Inactivity strikes us as intelligent "
 "behavior.” 1996 [E3-15].",
 "Applied: Gate 7. OM-11’s never-sell covers CONTROLLED businesses only (its own 2016 note)."),
princ(35, "BE GREEDY ONLY WHEN OTHERS ARE FEARFUL",
 "we simply attempt to be fearful when others are greedy and to be greedy only when others are "
 "fearful.",
 "Buffett, 1986 letter [E2-07]; falling prices are good news — OM-4; “Price is what you pay; "
 "value is what you get” (Graham, as taught to Buffett), 2008 letter [E4-05].",
 "Applied: Gate 7 temperament."),
princ(36, "RISK IS PERMANENT LOSS",
 "we define risk, using dictionary terms, as “the possibility of loss or injury.”",
 "Buffett, 1993 letter [E3-09]; quotational vs permanent, 1965 [E1-10]; “Never risk permanent "
 "loss of capital,” 2023 [E5-05].",
 "Applied: Glossary; Gates 6–7. (Retires the apocryphal “Rule No. 1” quote — C15.)"),
]
el += [PageBreak(),
 P("PART IV — LEDGER PRINCIPLES: THE MUNGER DISCIPLINES (37–41)", S["h1"])]
el += [
princ(37, "INVERT, ALWAYS INVERT",
 "It is in the nature of things, as Jacobi knew, that many hard problems are best solved only "
 "when they are addressed backward.",
 "Munger, Harvard School, 1986 — PCA Talk 1 [E2-20]; “Invert, always invert” verbatim — PCA "
 "Talk 3, 1996 [E3-22].",
 "Applied: Gates 5 and 8. (May edition dated it USC 1994 — corrected, C26.)"),
princ(38, "SEEK DISCONFIRMING EVIDENCE",
 "[Darwin] always gave priority attention to evidence tending to disconfirm whatever cherished "
 "and hard-won theory he already had.",
 "Munger, PCA Talk 1 [E2-21].",
 "Applied: Gate 5 Step B. (The “two opposing ideas” line was Fitzgerald’s — removed, C27.)"),
princ(39, "THE LATTICEWORK",
 "You’ve got to have models in your head. And you’ve got to array your experience — both "
 "vicarious and direct — on this latticework of models.",
 "Munger, USC 1994, PCA Talk 2 [E3-19].",
 "Applied: Gate 1 — how a circle of competence is actually built."),
princ(40, "THE MISPRICED BET",
 "It’s not given to human beings to have such talent that they can just know everything about "
 "everything all the time. But it is given to human beings who work hard at it — who look and "
 "sift the world for a mispriced bet — that they can occasionally find one.",
 "Munger, USC 1994, PCA Talk 2 [E3-21].",
 "Applied: Introduction — the purpose of the whole framework."),
princ(41, "THE PARI-MUTUEL MARKET",
 "the bad horse pays 100 to 1, whereas the good horse pays 3 to 2. Then it’s not clear which is "
 "statistically the best bet.",
 "Munger, USC 1994, PCA Talk 2 [E3-20].",
 "Applied: Gate 8 — price already encodes belief; the Reverse DCF asks whether the odds are "
 "wrong. (Upgrades Gate 8 from ‘not an original’ to corpus-framed.)"),
]

# ---------------- PART V: CONVENTIONS ----------------
el += [PageBreak(),
 P("PART V — FRAMEWORK CONVENTIONS (42–44) AND FIELD AMENDMENTS (45–47)", S["h1"]),
 P("Nothing below is attributable to Buffett or Munger. It stays because it is useful; it is "
   "labeled because the ledger cannot support it.", S["small"])]
el += [source_class_box("convention", [
 P("<b>PRINCIPLE 42 — MOAT MEASUREMENT MACHINERY.</b> The four-type taxonomy (Dorsey/Morningstar); "
   "the 8-quarter metric trend from primary filings; the two-consecutive-quarters signal rule; "
   "the metric menu (NRR, MAU, brand premium, relative gross margin). Rationale: the franchise "
   "test [E3-03] needs an operational measurement layer to be repeatable.", S["cardbody"])]),
 SP(1, 6),
 source_class_box("convention", [
 P("<b>PRINCIPLE 43 — DCF MECHANICS (BOOK TWO).</b> The ERP build-up (sovereign + 5–6% + 0–2%, "
   "≈10.5% US large-cap quality); 10-year explicit period; moat-class fades 15/10/5yr; terminal "
   "growth 2%/3% (&lt; WACC always); scenario trio; earnings-currency discounting. Rationale: a "
   "conservative pricing machine for full-size entries; corpus-contradicted as a Buffett method "
   "[E3-23], hence confessed.", S["cardbody"])]),
 SP(1, 6),
 source_class_box("convention", [
 P("<b>PRINCIPLE 44 — NUMERIC THRESHOLDS.</b> MOS floors 20%/30%; SBC materiality 15% of OE; "
   "maintenance-capex bands 65–70%/20–30%/50%; ROIC &gt; 15% check; 50%-OE-decline-for-2-years "
   "survival drill; IV-change &gt; 10% rerun trigger; reduce at 120% of IV; asymmetry 3:1 / 2:1 "
   "bands; 8-consecutive-quarters data floor. Rationale: pre-committed numbers [E1-02] beat "
   "ad-hoc judgment even when the numbers themselves are conventions.", S["cardbody"])]),
 SP(1, 10),
 source_class_box("amendment", [
 P("<b>PRINCIPLE 45 — THE BUFFETT STATUTE (GATE 6-B) AND STEP 0.</b> Sovereign 30-yr yield as a "
   "COMPARISON hurdle: OE yield ≥ sovereign; +1% small/mid, +2% micro/illiquid; hurdle floored at "
   "4%; Coca-Cola clause at 70% of hurdle for generational moats. Dual-book regime: Statute = "
   "wonderful-at-fair (starter size); Book Two DCF + 20% MOS = wonderful-at-cheap (full size). "
   "Step 0: re-pull the 30-yr yield each analysis date; &gt;50bp move triggers revaluation. "
   "Primary anchors: [E4-01], [E3-23], [E3-13], OM Intrinsic Value.", S["cardbody"])]),
 SP(1, 6),
 source_class_box("amendment", [
 P("<b>PRINCIPLE 46 — THE SCREAM TEST.</b> Verdicts must agree at the bare-yardstick rate and at "
   "the Book Two build-up rate; disagreement = whisper = pass. Extends the sensitivity-grid "
   "principle [E3-12].", S["cardbody"])]),
 SP(1, 6),
 source_class_box("amendment", [
 P("<b>PRINCIPLE 47 — OE RANGE ANCHORING.</b> Buy prices computed from the lowest VERIFIED "
   "owner-earnings tier; thresholds rise only on published filings. Extends the primary-sources "
   "data discipline (the May edition’s ‘Principle 15’, itself a convention).", S["cardbody"])]),
 SP(1, 6),
 source_class_box("amendment", [
 P("<b>PRINCIPLE 48 — THE FORTRESS TEST, TWO TRACKS</b> (ratified 2026-07-15, PENDING RULINGS.md "
   "Ruling 2). Non-financial businesses pass Gate 4's balance-sheet check on SURVIVAL, not "
   "net-cash: service debt and fund operations through a 50% owner-earnings decline sustained for "
   "2 consecutive years without existential risk — judged via credit rating, undrawn liquidity vs. "
   "near-term maturities, and a termed-out debt schedule. Ordinary investment-grade leverage is not "
   "itself a disqualifier. Financial businesses (banks, insurers, anything balance-sheet or "
   "float-levered) must ALSO clear a hard mechanical ceiling: assets ÷ equity &gt; 10:1 is an "
   "automatic FAIL, no exception. Corpus basis for the ceiling: “When assets are twenty times "
   "equity — a common ratio in this industry — mistakes that involve only a small portion of "
   "assets can destroy a major portion of equity.” — Buffett, 1990 letter, on banking [E3-02 "
   "context]. Retroactively validated: mechanically rejects Citigroup 2007 at 19:1 leverage "
   "(−95% followed) while the prior blanket net-cash rule had eliminated ordinary resilient "
   "industrials (Home Depot, Sherwin-Williams) for carrying normal corporate debt.", S["cardbody"])]),
 SP(1, 14),
 callout([P("Retired outright: “Rule No. 1: never lose money” (no corpus source — replaced by "
            "[E5-05]); “Take a simple idea and take it seriously” (unlocated in the 11 talks); "
            "the four Wesco-meeting quotes (cost of activity, 25% on equity, income statements "
            "are lies, agency costs — none on the shelf, C20–C23); the Kelly Criterion "
            "attribution (C28); “It’s not supposed to be easy” (unlocated). If a page-verified "
            "source surfaces, any of these may return with a real citation.", S["cardbody"])]),
 SP(1, 16),
 P("Summary — 48 principles: 36 ledger-cited (Buffett 28 · Munger 6 · Owner’s Manual/joint 2 by "
   "lead voice; many co-cited) · 3 conventions · 4 field-amendment sets (Statute+Step 0, Scream "
   "Test, Range Anchoring, the Fortress Test counted with their sub-rules as 45–48). Ledger: "
   "principle_ledger.csv, 76 rows, E1 1957–1970 through E5 2009–2025.", S["small"]),
 SP(1, 10), P(f"“{MOTTO}”", S["epigraph"]),
 P("Principles — Complete Source Tracing — v3.0 — July 2026", S["epigraphsrc"])]

doc = NumberedDoc(os.path.abspath(OUT), "Principles — Complete Source Tracing")
doc.build(el)
print("built:", os.path.abspath(OUT))

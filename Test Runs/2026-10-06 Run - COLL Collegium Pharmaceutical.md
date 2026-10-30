# Company Run: Collegium Pharmaceutical, Inc. (NASDAQ: COLL), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Form copied from
`Test Runs/_TEMPLATE - Company Run.md` before any fetch. Every judgment cites a v5 ledger id in bold; every filing fact
carries its accession; a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.
Working folder: `Test Runs/_research 2026-10-06 COLL/` (filing texts, `row.py` ledger lookup, `facts.py`, `runoff.py`
and its output, peer filings under `peers/`).

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is on this run's blind list, so whether the
operator holds COLL is unknown to the analyst.

**CONTAMINATION, declared:** no blind-listed file was opened. Seen without opening, in the session's own context: the
commit subjects of the REYN (OUT at Q7), PATK (OUT at Q2), BCC (OUT at Q2) and ASO (OUT at Q2) runs and of an addendum on
the OSIS and BCC runs quoting the framework beside M2000-019; the file names (only) of untracked 2026-10-06 runs on MHO,
TPC and WKC; and the auto-loaded memory index (queue paused; "57 gate-clearers, nothing buyable"). None concerns COLL or
pharmaceuticals. The pattern of recent OUT verdicts is a pull toward OUT, and is named here so it can be discounted.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $21.87, close 2026-10-05, from the aggregator quote `tools/run.py` uses (**aggregator, flagged**, operator rule
  5). For scale, the company's own 8-K of 2026-08-13 (accession 0001104659-26-095464) records a $25.70 close on 2026-08-12.
- **Shares:** one class, common stock, **32,555,613** as of 2026-07-31, from the cover of the 10-Q for the quarter ended
  2026-06-30 (filed 2026-08-06, accession 0001628280-26-053851; `python Screens/cover_shares.py COLL`). The balance sheet
  shows 32,498,310 outstanding and 41,527,032 issued at 2026-06-30. An accelerated buyback of $50 million (8-K above)
  delivered 1,556,420 shares initially on 2026-08-12; the cover count is used with the 2026-06-30 net debt, both before it.
- **Market cap:** $21.87 x 32.556M = **$712.0M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 2026-10-05 (issuing
  authority, via `tools/run.py`).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-26, accession 0001628280-26-011992 (Business,
  Risk Factors, MD&A, Notes 3, 4, 11, 13, 14); 10-Q for Q2 2026, filed 2026-08-06, accession 0001628280-26-053851;
  proxy DEF 14A filed 2026-04-07, accession 0001628280-26-024063 (pay metrics); 8-Ks of 2025-12-30 (0001104659-25-125026,
  new credit agreement), 2026-03-19 (0001104659-26-032166, Azstarys agreement and release), 2026-05-12
  (0001104659-26-059018, Azstarys closing), 2026-08-06 (0001628280-26-053849, Q2 release and guidance), 2026-08-13
  (ASR); 10-K for FY2020 (0001558370-21-001814, the Teva settlement on Xtampza ER, revenue 2018-2020) and FY2022
  (0001558370-23-001900, revenue 2020-2022).
- **One figure cross-checked against the filed statement:** net cash from operating activities FY2025, $329.3M in
  `tools/run.py`; the 10-K's MD&A cash-flow table prints "$ 329,323" thousand. Agrees.
- **`tools/run.py COLL`, arithmetic lines only** (Part VII; its v4 floor and v4 material ignored): OCF / SBC / D&A /
  capex FY2023 274.7 / 27.1 / 149.3 / 0.5; FY2024 205.0 / 32.4 / 169.2 / 1.7; FY2025 329.3 / 41.9 / 226.1 / 1.7 ($M).
  Owner cash on the capex basis, three-year mean 234.6; on the D&A basis 54.4 (five-year window also 54.4). SBC tagged
  every year, complete. The tool's own line: "no intangible [...] payment beside capex" is true of the three years it
  read and false for the decade: the product purchases sit in investing cash as business or intangible acquisitions,
  below.

**Owner cash after every real cost, the decade** (XBRL transcription from the 10-Ks, $M; the purchases are the capital
this business spends; the 2024 figure adds the $164.6M of Ironshore debt repaid at closing, which the FY2025 MD&A
reports in financing):

| Year | Revenue | OCF | SBC | Capex | Product / business purchases | OCF - SBC - capex | After purchases |
|---|---|---|---|---|---|---|---|
| 2016 | 1.7 | -75.1 | 5.8 | 0.5 | 2.5 | -81.4 | -83.9 |
| 2017 | 28.5 | -67.0 | 7.9 | 1.0 | 0 | -75.9 | -75.9 |
| 2018 | 280.4 | 169.4 | 13.8 | 5.5 | 18.9 | 150.1 | 131.2 |
| 2019 | 296.7 | 27.8 | 16.5 | 6.4 | 0 | 4.9 | 4.9 |
| 2020 | 310.0 | 93.9 | 21.9 | 5.5 | 368.2 (Nucynta) | 66.5 | -301.7 |
| 2021 | 276.9 | 103.6 | 24.3 | 1.9 | 0 | 77.4 | 77.4 |
| 2022 | 463.9 | 124.2 | 22.9 | 1.6 | 572.1 (BDSI) | 99.7 | -472.4 |
| 2023 | 566.8 | 274.7 | 27.1 | 0.5 | 0 | 247.1 | 247.1 |
| 2024 | 631.4 | 205.0 | 32.4 | 1.7 | 432.1 (Ironshore, incl. debt repaid) | 170.9 | -261.2 |
| 2025 | 780.6 | 329.3 | 41.9 | 1.7 | 0 | 285.7 | 285.7 |
| **2016-25** | | | | | **1,393.8** | **945.0** | **-448.8** |
| **2021-25** | | | | | **1,004.2** | **880.8** | **-123.4 (mean -24.7/yr)** |

And on 2026-05-12, $655.4M more (Azstarys, net of cash acquired, 10-Q cash-flow statement), plus up to $135M of
milestones (acquisition-date fair value $38.5M). OCF is after interest paid, so the column is cash to the shares. Over the
decade the business has not yet produced cash to its owners after paying for the products that produce it; revenue grew
from $310.0M (2020) to $780.6M (2025) on those purchases, so part of the spend bought growth, not only replacement.

**The balance sheets first, ten year-ends**, "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]** (the file closes at Q1, so they
are read here; `tools/run.py` ten-year table, first-filed XBRL, checked against the 2026-06-30 statement in the 10-Q):
- 2016-2019: equity fell from $135M to $87M while losses ran through retained earnings (-$223M to -$360M); cash held at
  $150-170M because shares were sold (equity issuance $137.3M in 2016, $34.3M in 2017). Xtampza ER was launched on
  owners' money, not earned money.
- 2020: the Nucynta purchase. Intangibles to $336M, debt on the face to $257M (term loan and the 2026 convertible), total
  assets to $644M; equity $186M.
- 2022: BDSI. Assets $1,174M, goodwill $134M, intangibles $567M, debt $701M; equity $195M, unchanged in substance.
- 2024: Ironshore. Assets $1,664M, intangibles $891M, debt $852M, cash down to $71M.
- 2025: intangibles amortized to $670M; cash $231M plus securities $155M; debt $809M; accumulated deficit $101M.
- 2026-06-30: Azstarys. Intangibles $1,186M and goodwill $190M against total equity of $312M, so tangible equity is about
  minus $1,064M; term notes $853M carried (principal about $866M after the $300M delayed draw), convertible notes $239M
  carried ($241.5M principal, due 2029), a deferred royalty obligation on Jornay PM of $121M, contingent consideration
  $38.5M, deal payables $29.7M; cash $129.5M (securities sold to fund the deal). Accrued rebates, returns and discounts are
  $406.9M against receivables of $285.1M and quarterly revenue of $199.9M: the payers' claim on gross revenue is the
  largest current liability.
- **What the figures say:** each wave of revenue was bought, carried as an intangible, financed with debt, and is being
  written off on management's own schedule (Belbuca to nil in 2026, Nucynta to nil by 2026-06-30, Jornay PM over the
  years to about 2032, Azstarys over 11.6 years). The retained earnings have never turned positive in ten years. **What
  they cannot say:** whether the next purchase will earn its price; that is decided by deals not yet made.
- **Net debt used below** (2026-06-30, before the ASR, to pair with the cover count): term principal ~865.5 + convertible
  241.5 + deferred royalty 121.4 + contingent consideration 38.5 + deal payables 29.7, less cash 129.5 and the restricted
  escrow 19.9 held against the payables = **$1,147.2M**. Enterprise value at the price: **$1,859.2M**.

---
## THE FOUNDATIONS (not a gate)
A share is a business: "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**. For COLL
the five years would include the generic entry already under way on Nucynta (2025 revenue $196.3M) and the scheduled
end of the '866 patent on Belbuca in 2027 (2025 revenue $221.7M). The market serves: "It just tells us prices."
**[M2006-077]**; the fall from $25.70 in August to $21.87 is not evidence either way. Who is paid to tell you: the
Azstarys release was headed "Accretive to Adjusted EBITDA" and named fee-earning advisers on both sides (Leerink,
Centerview), and the proxy pays the officers' annual cash on adjusted EBITDA (20% weighting, goal $446.8M, achieved
$460.5M), so the figure management promotes is the figure management is paid on. The analyst's habit, "I’m looking for
what’s wrong in things because that’s part of investing" **[M2025-013]**, was applied hardest to the case below.

**Contrary evidence**, "write it down in the first 30 minutes" **[M1997-127]** (evidence for the business, against the OUT this run reaches):
1. The purchases have so far paid back or nearly so. Nucynta, bought in 2020 for $368.2M of cash, produced $1,100M+ of
   revenue in 2020-2025; Belbuca and Symproic (BDSI, $572.1M net cash in 2022) produced about $800M of revenue through
   2025 at a company operating margin before amortization of 51-55% (2023-2025).
2. The ADHD half is growing: Jornay PM net revenue +41% year on year in Q2 2026 ($46.1M), prescribers at a record 30,000+;
   2026 guidance $190-200M; Azstarys with "six Orange Book-listed patents, most of which do not expire until December
   2037" (release of 2026-03-19).
3. The speakers' own record on pharma is a mistake of omission: "the pharmaceutical industry, as a whole, has done very
   well" **[M1999-043]**, and Buffett said the industry "has a far, far better record of returns on large amounts of
   equity over time" **[M2001-002]** than tech.
4. Xtampza ER's patents were held against Teva by consent judgment; Teva may launch only "on or after September 2, 2033
   (subject to FDA approval and acceleration under certain circumstances)" (FY2020 10-K).
5. Belbuca's '539 patent was upheld at trial and on appeal against Alvogen (final judgment 2022-01-21; Federal Circuit
   2022-12-21), which put Alvogen's approval date at 2032-12-21 before Alvogen's non-infringement notice of 2025-06-09.

## THE STANDING RULE
The buyer's own conduct: "We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. No purchase is made here; any
purchase of COLL would be in cash and sized so that its total loss, which the leverage below makes possible, could not
touch what the buyer needs. Not engaged by this run.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test as the framework states it, on the filings.** Understanding is "a reasonable fix on about what the earning
power and competitive position will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10
years" **[M2000-037]**.

**What the business is (FY2025 10-K, 0001628280-26-011992).** A US-only seller of six branded, scheduled medicines, none
invented in the last decade by the company except Xtampza ER (approved 2016): "As of April 1, 2022, we focused entirely
on commercial products rather than research and development and redirected resources from research and development
activities. As such, there were no expenses incurred in research and development after the three months ended March 31,
2022." Revenue 2025 by product ($M, Note 3): Belbuca 221.7, Xtampza ER 199.3, Jornay PM 148.9, Nucynta IR 115.3,
Nucynta ER 81.0, Symproic and other 14.5; total 780.6. Three wholesalers took 34%, 34% and 29% of revenue. Since May 2026
Azstarys as well (2026 guidance $65-75M for the part year).

**The key variables and whether they are foreseeable.** "If something is not very predictable, forget it." **[M1998-044]**

| Product | 2025 rev. | Exclusivity, from the filings | What the filings show |
|---|---|---|---|
| Nucynta IR / ER | 196.3 | pediatric exclusivity to 2025-12-27 (ER) and 2027-01-03 (IR); a third-party Nucynta IR generic approved January 2026; the authorized generic (Hikma) launched 2026-02-25, ER to follow; Grünenthal sued 2026-02-02 over the ER authorized generic | Q2 2026: IR $14.4M vs $26.5M a year earlier (-46%), ER $15.7M vs $19.9M; franchise -24% including $5.1M of AG sales; 2026 guidance cut $40M "largely driven by lower-than-expected revenue from the AG versions" |
| Belbuca | 221.7 | patents to 2027 ('866) and 2032 ('539); Alvogen non-infringement notice on the '539 received 2025-06-09, suit 2025-07-24, 30-month stay, trial set for 2027-04-12; Ascent Paragraph IV on the '539 received 2026-06-04, suit 2026-07-16; Chemo ANDA pending | the intangible is amortized to nil in 2026 (management's own life for the asset); "unable to evaluate the likelihood of an unfavorable outcome" |
| Xtampza ER | 199.3 | patents to 2030 and 2036; Teva licensed from 2033-09-02, subject to acceleration; Purdue's suit, now Knoa Pharma's (substituted 2026-07-16), seeks damages and an injunction | 2025 rise was "lower gross-to-net adjustments [...] higher gross price partially offset by lower sales volume"; Q2 2026 -14% |
| Jornay PM | 148.9 | sixteen patents to 2032; a 9.7% royalty to former Ironshore lenders through March 2032 | growing; the $25M revenue milestone for 2025 "was not achieved" |
| Azstarys | n/a | most patents to December 2037 (company release) | bought for $655.6M cash plus up to $135M; Q2 2026 prescriptions +1.9% |
| Symproic | 14.5 | licensed from Shionogi; intangible amortized to 2031 | small, declining |

The opioid market itself: "In 2025, there were approximately 133.2 million prescriptions for opioids written in the
United States [...] After marked increases in opioid prescriptions from 2000 to 2015, prescriptions decreased each year
since 2015" (10-K, Item 1). Every pain product's 2025 revenue increase was price or rebates "partially offset by lower
sales volume" (MD&A).

**Where it will be in ten years.** On the filer's own dates, every product that made 2025's revenue is off patent, or
under a licensed generic, inside the ten years: Nucynta now, Belbuca in 2027 or 2032 by the litigation, Xtampza ER from
2033 (2030 if accelerated), Jornay PM in 2032; only Azstarys (2037) runs past 2035. The company's own accounts write off
every product right on a finite life. So the earning power of 2036 will be what is bought between now and then, at
prices not yet set, out of cash the purchases themselves have so far used up (owner cash after purchases -$448.8M over
2016-2025). The past statements do not tell the future ones; the test is whether "the financial statements will tell me the information that’s useful to me in making a judgment about what the future financial statements are going to look like" **[M2008-033]**, and here they cannot: the 2016-2025 statements describe five
different portfolios (Xtampza alone; plus Nucynta; plus Belbuca; plus Jornay; plus Azstarys), "sometimes the past doesn’t
give you any insights into the future" **[M2007-025]**.

**The framework's pharmaceutical routing.** Q1's list of what it rules OUT carries, for businesses that live on
continued invention, the row: "Take pharmaceuticals, if they had never invented any more pharmaceuticals, it would be a
terrible business." **[M1999-075]**. COLL lives on more than continued invention; it lives on continued *purchase* of
other companies' inventions, because its own invention stopped in 2022 and each purchased product ends on a date its
10-K prints. Take away the next purchase and what remains is a portfolio running down to Azstarys alone by the mid-2030s:
the "terrible business" of the row, with $1.15 billion of net debt in front of the shares.

The second pharmaceutical routing in Q1 (test 6, "Can I name the winner, not just the industry?") rests on the same
speakers: "than it is for me to figure out which one in the pharmaceutical." **[M1997-119]**, and "we don’t know the
answer on the pipeline. It will be a different pipeline anyway five years from now." **[M2008-113]**, whose answer was
that "a group approach makes sense" **[M2008-113]**. That routing would send a single drug company to TOO HARD. It is
weighed and not taken, for two reasons. First, the deciding fact here is not ignorance of a pipeline (COLL has none) but
a finding from the filings: the product lives end on printed dates and the replacement is bought, which is the condition
M1999-075 names. Second, the group approach the speakers allowed rested on the industry's record of "returns on large
amounts of equity over time" **[M2001-002]**; COLL's own decade shows an accumulated deficit, negative tangible equity,
and no cash to owners after the purchases. The patent litigations (Belbuca '539, Knoa on Xtampza, Grünenthal on the
Nucynta ER AG) are important and, by the filer's own words, not something it can evaluate; "If something’s important but
unknowable, forget it." **[M2006-076]**. They move the dates inside the window; they do not move the end of it, so the
verdict does not rest on them.

What the run cannot see is the one thing that would rescue the economics: the price and quality of the purchases of
2027-2036. "the biggest judgment you have to make is how well capital will be deployed in the future" **[M2001-111]**; for
COLL that judgment is not one input among others, it is the whole of the ten-year economics. And "if you have doubts
about something being into your circle of competence, it isn’t." **[M2002-092]**.

- **VERDICT: OUT**, at Q1, on **[M1999-075]**: the business lives on replacing, by purchase, products whose exclusivity
  ends inside the ten years on dates its own 10-K prints, with no invention of its own since 2022; its ten-year economics
  are those of whatever it buys next, financed by debt. The TOO HARD pull of **[M1997-119]** and **[M2008-113]** is
  recorded and declined above. Three boxes: "in, out, and too hard" **[M2006-013]**; this is the second.

**The run closes here.** Q2 to Q12 are NOT REACHED. What follows them is COMPUTATION and reading, not clearance.

---
## Q2: WHY IS THE CASTLE STILL STANDING? STOP. **NOT REACHED.**
**Reading only, gathered for the owner, not a verdict.** The competitor row, from the competitors' own filings:

| Company | Metric | Figures | Source |
|---|---|---|---|
| Assertio (formerly Depomed, the seller of Nucynta to COLL) | total revenue | $455.9M (2016) to $118.7M (2025); net loss in six of the seven years 2019-2025 (2023: -$331.9M) | 10-K FY2018, 0001005201-19-000040; 10-K FY2025, 0001808665-26-000011 |
| Assertio, in its own words | generic erosion | "Competition from generics has adversely affected and could continue to have further adverse effects on our business." INDOCIN, with no patents, 21% then 16% of revenue | 10-K FY2025, 0001808665-26-000011 |
| Supernus (ADHD peer: Qelbree; epilepsy) | revenue of the two products that lost exclusivity | Trokendi XR $94.3M (2023), $63.2M (2024), $42.4M (2025) after January 2023 generics; Oxtellar XR $113.4M, $99.5M, $40.7M after September 2024 generics (-59% in the first full year) | 10-K FY2025, 0001356576-26-000011 |
| Supernus, in its own words | after entry | "as we have observed with Trokendi XR and Oxtellar XR, competition from generic equivalents adversely, materially, and permanently impact our revenues, profitability, and cash flows from those products" | same |
| Supernus | how it replaces | invents: R&D $106.2M in 2025; total revenue $215.0M (2016) to $719.0M (2025); 2025 net loss $38.5M | same; XBRL |
| Purdue (OxyContin) | private, flagged | no filings; from COLL's own 10-K: Chapter 11 from 2019-09-15, successor Knoa Pharma from about 2026-05-01; Purdue shares COLL's API suppliers | COLL 10-K FY2025; 10-Q Q2 2026 |
| Generic makers (Hikma, Teva, Alvogen, Chemo, Ascent) | entry | Hikma sells COLL's own authorized generics of Nucynta; Teva licensed on Xtampza ER from 2033; three ANDA filers against Belbuca; no comparable public figures in SEC filings for Hikma (London-listed), Alvogen, Chemo or Ascent (flagged) | COLL filings above |

COLL's own sentence on the same: "after the introduction of a generic competitor, a significant percentage of the sales
of any branded product are typically lost to the generic product" (10-K Risk Factors). Over the whole span, the two
peers that replaced expiring products did so either by invention (Supernus, revenue up, now loss-making) or not at all
(Assertio, revenue down three-quarters). Neither shows a castle that outlives its patents.

## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING. **NOT REACHED.**
(Reading only: the table in Step 0. Over 2016-2025 the purchases, $1,393.8M, exceeded the cash before purchases, $945.0M.
Owner cash is never set here against depreciation alone: capex is $1-6M a year; the capital is the product purchases.)

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion. **NOT REACHED.**
(Reading only, recorded as found: the balance sheets are read in Step 0. The company features "Adjusted EBITDA" and
"adjusted net income" ($75.4M for Q2 2026 against a GAAP net loss of $15.1M), and the proxy pays on adjusted EBITDA. The
rows on it: "The one figure we regard as utter nonsense is the so-called EBITDA." **[M1998-086]**; a management that
waves away real costs by highlighting adjusted earnings "makes us nervous" **[L2016-006]**. Its product-right
amortization is a real cost here: "Some truly deplete over time while others never lose value." **[L2012-003]**; these
deplete on the company's own schedules. These would have weighed against at Q4; they are not judged.)

## Q5: WHO RUNS IT? STOP on integrity. **NOT REACHED.**
(Reading only: the chief executive changed (the proxy's pay-versus-performance table names Ciaffoni and Heffernan for 2024 and Karnani for 2025); executive-transition costs were charged
in 2025 and again in Q2 2026; the general counsel left 2025-03-07. Not judged.)

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING. **NOT REACHED.**
(Reading only: buybacks of $47.9M, $14.1M, $75.0M, $60.0M and $25.1M in 2021-2025, the 2024-2025 programme at a
weighted $31.43 a share, and $50M by ASR in August 2026 at about $25.70, all with no stated price limit. Each sits above
the low end and below the top of the computation below; Q6's test against the bottom of the Q7 range would have weighed
against. Not judged.)

## Q7: WHAT IS IT WORTH? STOP. **NOT REACHED: COMPUTATION, NOT A CLEARANCE.**

**COMPUTATION, NOT A CLEARANCE** (operator rule 3's heading, written without its dash under the standing no-em-dash rule). The owner asked for a value range, a fair price and a cheap price. They are given
below, labelled, with no entry language; the file closed at Q1 and none of this reopens it.

**Construction (CONVENTION of this run, at the owner's request, departing from the Q7 convention):** the Q7 convention
carries a five-year average forward with a no-growth perpetuity after year ten. For a business whose products end on
printed dates that tail is false, so each product's stream is valued separately and declines after its exclusivity
ends. Inputs (`runoff.py`, output in `runoff_output.txt`):
- Revenue from 2027 by product, three cases, from the dates and trends in the table at Q1. Low: Belbuca generic from
  mid-2027, Xtampza ER -10% a year and generic from 2030, Jornay PM +3% a year, Azstarys flat and generic from 2034.
  Central: Belbuca generic from 2028 (the end of the Alvogen 30-month stay), Xtampza ER -5% a year and generic from 2034
  (after Teva's 2033 licence), Jornay PM +8% a year to 2031, Azstarys +8% a year to 2037. High: Belbuca's '539 upheld to
  2032, Xtampza ER flat to 2033, Jornay PM and Azstarys +12% a year. Nucynta is treated as already generic in all three.
- Erosion after entry (CONVENTION, from the filings' only observations): -50% in the year of entry, then -35% a year.
  Basis: Nucynta IR -46% in the first quarter after the AG; Oxtellar XR -59% in its first full year; Trokendi XR -33% a
  year in years two and three (Supernus 10-K).
- Pre-tax, unlevered cash = revenue x contribution margin, less $2M capex. Margin 50% central (company operating margin
  before amortization 55.2%, 53.1%, 51.4% in 2023-2025; 2026 adjusted-EBITDA guidance $445-470M on $825-855M less SBC),
  45% low, 55% high. Stock pay is a cost inside the margin. **No replacement purchases are assumed:** this values the
  portfolio the owner would buy, not the deals management will make with its cash. A deal that earns its price leaves
  the value unchanged; one that does not lowers it.
- Q4 2026 at a quarter of the low end of 2026 adjusted-EBITDA guidance less stock pay. Discounted mid-year.
- The uniform margin is generous in the run-off years, when the sales forces and head office do not shrink with
  revenue. A sensitivity (CONVENTION) sets costs at $120M fixed plus 35% of revenue, which gives the same 50% in 2027.

**Results** ($M; equity per share = (enterprise value - net debt $1,147.2M) / 32.556M shares):

| Case | Pre-tax cash, Q4 2026-2045 | EV at 5.66% | Per share | EV at 10% | Per share | Pre-tax return on today's EV $1,859M |
|---|---|---|---|---|---|---|
| Low | 1,708 | 1,434 | **$8.81** | 1,276 | $3.95 | -2.5% |
| Central, uniform margin | 3,134 | 2,413 | $38.87 | 2,038 | $27.37 | 12.7% |
| Central, fixed + variable costs | n/a | 1,997 | $26.10 | 1,744 | **$18.32** | 7.9% |
| High | 5,051 | 3,782 | **$80.93** | 3,130 | $60.90 | 25.9% |

For comparison, the Q7 convention as written, on the D&A-basis owner cash of $54.4M a year (no-growth end, ten years
then flat, at 5.66%): enterprise value about $961M, below net debt, so about **-$5.72** a share. On the capex basis
($234.6M) it would be several times the price; the convention has no rule for a business whose capital spending is
product purchases, which is why the run-off construction is used.

**(a) VALUE RANGE (COMPUTATION):** **$8.81 to $80.93** a share at the long Treasury rate "(which we consider to be the
yield on long-term U.S. bonds)" **[L2000-021]**, against **$21.87**. The equity range is 9.2 to 1 (the enterprise range
2.6 to 1; the $1.15 billion of net debt in front of the shares multiplies the width). Under Q7's three-to-one CONVENTION
the range would close TOO HARD: "Usually, the range must be so wide that no useful conclusion can be reached."
**[L2000-025]**. The width comes almost wholly from two things the run cannot judge: the Belbuca and Xtampza litigations,
and the growth of the two ADHD products.

**(b) FAIR PRICE (COMPUTATION):** the price at which the central case clears the about-ten-percent pre-tax floor
(CONVENTION, Q7; "we don’t want to buy equities where our real expectancy is below 10 percent" **[M2003-149]**). Tax:
pre-tax throughout, no tax deducted, as the floor is pre-tax. Basis: **enterprise value (equity plus net debt)**, i.e. the
floor is applied to the whole price including the debt the buyer steps behind, as the speakers "evaluate acquisitions on
an all-equity basis" **[L2017-004]**. Result: **about $18.32** with costs partly fixed (taken as the central figure,
because the 10-K says the SG&A is "primarily [...] salaries and employee-related costs" that do not fall with revenue),
**$27.37** with the uniform margin. At $21.87 the central pre-tax return is 7.9% (partly fixed costs) to 12.7% (uniform).

**(c) CHEAP PRICE (COMPUTATION):** rule of this run (CONVENTION): the price below which even the **low case** (Belbuca
generic in 2027, Xtampza ER generic in 2030 and falling 10% a year before, no growth in Azstarys, 45% margin, no new
purchases) clears the 10% pre-tax floor on enterprise value, so that no case needs a pencil ("It should scream at you."
**[M2009-005]**). Result: **about $3.95**. The price is 5.5 times it.

The price sits inside the range and near the central floor price: not a screamer on any reading.

## Q8: BETTER THAN THE ALTERNATIVES? STOP. **NOT REACHED.**
## Q9: COULD IT RUIN US? WEIGHING. **NOT REACHED.**
(Reading only: funded debt about $1,107M plus the $121M royalty obligation, against 2026 adjusted-EBITDA guidance of
$445-470M; covenants on first-lien net leverage and fixed-charge cover, tested quarterly; the credit facility matures
2030, or 2028-11-18 if more than $50M of the 2029 convertibles are outstanding and liquidity is below $350M; the
convertible holders can put on a fundamental change. Not weighed.)
## Q10: THE FAT PITCH? WEIGHING. **NOT REACHED.**
## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE? **NOT REACHED.**
(Reading only: four of the seven products are Schedule II opioids or Schedule III buprenorphine; the company settled 27
municipal opioid suits for $2.75M in 2022 and gave an Assurance of Discontinuance to Massachusetts in 2021; subpoenas from
three other states are open. Opioids are not among the businesses Q12 names. Not judged.)

---
## THE BOX
**OUT, at Q1** (**[M1999-075]**): a business that lives on buying replacements for products whose exclusivity ends
inside ten years on its own printed dates, with no invention of its own since 2022. Value range (COMPUTATION, not a
clearance) $8.81 to $80.93 against $21.87; fair about $18.32 (central, floor on enterprise value, pre-tax); cheap about
$3.95. No research pass: OUT is not TOO HARD (WORK). Q11 belongs to a holding review.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written top to bottom. Not committed, by instruction of this session
      (the operator's dispatch forbade commits); the write-early commits are therefore absent, declared here.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script); every filing fact has its accession; every
      number has a filing, a row or a CONVENTION label.
- [x] The order was kept; the first STOP that failed (Q1) closed the run; nothing after it is a clearance, and the
      computation is headed as such.
- [x] Owner cash after every real cost, never a net-income proxy: OCF less SBC, capex and the product purchases; the
      sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down at once, "write it down in the first 30 minutes" **[M1997-127]** (five items, Foundations).
- [x] No row dated after the anchor: the run is dated today; not a point-in-time test.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 floor and v4 ids ignored.
- [x] `python tools/check_framework.py` PASS on 2026-10-06 with this file in place (checks over run files included); a
      run-local script (`check_ids.py`) found no E-id, all 29 v5 ids present, and all 32 quoted fragments inside their rows.
- [ ] Not done: a second analyst's blind reading of the Q1 routing choice (OUT against TOO HARD); recommended, since the
      framework itself carries both routings for pharmaceuticals.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Q1 carries two routings for a pharmaceutical name that point to different boxes.** Its list of what it rules OUT
   carries the row on pharmaceuticals and continued invention, **[M1999-075]**; its test 6 and its TOO HARD paragraph
   send industries whose winners cannot be named to TOO HARD, and test 6's own row, **[M1997-119]**, is about picking
   among pharmaceutical companies. Nothing says which governs a single named drug company with dated patents and no pipeline.
   This run took OUT because the deciding fact was a finding from the filings, not ignorance; another analyst could take
   TOO HARD (NATURE) on the litigations the filer says it cannot evaluate. The box differs, the action does not.
2. **The Q7 range CONVENTION has no rule for finite-life assets.** Its no-growth perpetuity after year ten assumes the
   earning power outlives the decade; for a drug company it does not. And its owner-cash input ("deducts all capital
   spending") is silent on product purchases: on the capex basis the convention gives a value several times the price,
   on the D&A basis a negative equity. The run-off construction used here, at the owner's request, is ours.
3. **The three-to-one width test does not say whether it is measured on enterprise value or on equity per share.** With
   $1.15 billion of net debt the same cash streams give 2.6 to 1 on the enterprise and 9.2 to 1 on the shares; the box
   at Q7 would differ (OUT against TOO HARD) by the choice.
4. **The floor CONVENTION does not say whether the ten percent is on the equity price or on equity plus net debt.** This
   run applied it to the enterprise, on **[L2017-004]**; on the equity alone, with debt costing about 6.9%, the fair
   price would come out higher.
5. **The template's position note says "check `PORTFOLIO.md`", which this run's blind rule forbids.** The note was left
   unchecked and said so.
6. **`tools/run.py` reports "no intangible [...] payment beside capex"** for its three-year window, which for a company
   whose capital is product purchases invites the capex-basis owner cash of $234.6M as if it were the owner's cash. The
   arithmetic is right; the line misleads unless the decade is read.

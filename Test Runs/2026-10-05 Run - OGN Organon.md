# Company Run: Organon & Co. (NYSE: OGN), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Template:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch. Working folder:
`Test Runs/_research 2026-10-05 OGN/` (raw filings, text extracts, `fetch.py`, `facts.py`, `peers.py`, `calc.py`,
`row.py`, `run_py_output.txt`). Every judgment cites a v5 ledger id in bold; every filing fact carries its accession;
the first STOP that failed closed the run and later questions are marked NOT REACHED.

**POSITION NOTE, declared before any verdict:** not known to this analyst. `PORTFOLIO.md` was not opened (blind rule).
A directory listing of `Test Runs/` taken to check for earlier OGN files showed holding-review file names dated
2026-10-05 for other tickers and no file of any kind for OGN.

**CONTAMINATION DECLARED.** (1) The session context showed five recent commit subjects naming other companies' v5 runs
(PENN, YELP, ROCK, ENR) with their boxes and their fair and cheap figures. (2) The `Test Runs/` listing showed file names
of other 2026-10-05 runs, holding reviews and research passes (none opened). (3) The memory index in the session context
carried queue-state lines ("57 gate-clearers, nothing buyable"). (4) `tools/run.py` printed v4-era yield and growth lines;
only its arithmetic lines were used (Part VII). Nothing seen concerned OGN. No forbidden file was opened.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $13.72 (2026-10-05; `tools/run.py` live quote, AGGREGATOR, flagged per operator rule 5). The price is pinned
  by a cash merger agreement at $14.00 a share (below, and the WORKOUT note after the close).
- **Shares:** 262,609,433 common, one class, cover of the 10-Q for the quarter to 2026-06-30, filed 2026-07-31, accession
  `0001628280-26-051230` (`python Screens/cover_shares.py OGN`); the same count is the record-date count in the 8-K of the
  stockholder vote (accession `0001193125-26-314587`). Fully diluted count "approximately 284.9 million" as of 2026-04-24
  (proxy supplement, 8-K accession `0001193125-26-307767`).
- **Market cap:** about $3,603M (262.6M x $13.72).
- **Sovereign for the earnings currency (USD):** 5.66%, US Treasury daily par yield curve, 30-year, 10/05/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 filed 2026-02-24, accession `0001628280-26-011125` (business, risk
  factors, MD&A, statements, Notes 5 and 18); 10-Ks FY2021 to FY2024 (`0001821825-22-000002`, `0001821825-23-000003`,
  `0001628280-24-006733`, `0001821825-25-000006`) for the product tables and the cash-flow statements; 10-Q Q2 2026
  `0001628280-26-051230`; DEF 14A filed 2026-04-24 `0001193125-26-177411` (pay sections only); the Form 10 information
  statement, 10-12B/A filed 2021-04-29, `0001193125-21-140380`, Exhibit 99.1 (selected data); 8-Ks
  `0001104659-25-102324` (CEO resignation and audit-committee findings, with Exhibit 99.1), `0001193125-26-178718` (merger
  agreement with Sun Pharma), `0001193125-26-307767` (proxy supplement with management projections),
  `0001193125-26-314587` (merger vote), `0001104659-26-017870` (second audit-committee review), `0001104659-26-089008`.
- **One figure cross-checked against the filed statement:** net cash from operating activities FY2025 $700M, Consolidated
  Statements of Cash Flows, 10-K `0001628280-26-011125`; `tools/run.py` transcribed 700.0. Agrees.
- **`tools/run.py OGN`, arithmetic lines only** (USD M; OCF less stock pay less capital spending; first-filed XBRL,
  checked against the filed cash-flow statements):

| FY | OCF | stock pay | capex | owner cash (capex basis) | D&A | owner cash (D&A basis) | other capital payments (product rights, acquired IPR&D, Dermavant) | owner cash after all capital payments |
|---|---|---|---|---|---|---|---|---|
| 2021 | 2,160 | 59 | 192 | 1,909 | 195 | 1,906 | 296 | 1,613 |
| 2022 | 858 | 75 | 196 | 587 | 212 | 571 | 231 | 356 |
| 2023 | 799 | 101 | 251 | 447 | 236 | 462 | 10 | 437 |
| 2024 | 939 | 105 | 175 | 659 | 277 | 557 | 342 | 317 |
| 2025 | 700 | 77 | 162 | 461 | 361 | 262 | 229 | 232 |

  Five-year mean, capex basis: 812.6. **2021 is abnormal** and the mean is not used as the base without a variant: the
  spin year's operating cash carries a one-time working-capital inflow (trade payables +663, other current assets +353,
  accrued liabilities +329; 10-K FY2022 cash-flow statement, `0001821825-23-000003`) and only seven months of interest
  ($258M against $527M in 2023). Whole-cycle variant (2022 to 2025): 538.5 capex basis; 463.0 D&A basis; 335.5 after all
  capital payments. Shown change of the aggregate, 2022 to 2025: -7.7% a year (capex basis), -13.3% a year (after all
  capital payments). H1 2026 operating cash $332M (10-Q). Stock pay is 13% to 23% of owner cash, capex basis, 2022 to 2025.
  Pre-spin years (2019, 2020) are Merck carve-outs with no interest and allocated costs; they are not used for owner cash.

### The balance sheets, read in Step 0 because the file closes before Q4 **[M2025-032]**
Organon's own-basis balance sheets exist from 2020 (10-K FY2021); the Form 10's 2018 and 2019 combined statements
include products Merck retained (the 10-K FY2021 reports them as discontinued operations), so they are not comparable
and were not used. Seven year-ends plus June 2026 were read (USD M; 10-Ks named above; June 2026 from the 10-Q):

| | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Jun 2026 |
|---|---|---|---|---|---|---|---|
| sales (year) | 6,532 | 6,304 | 6,174 | 6,263 | 6,403 | 6,216 | 3,018 (H1) |
| cash | 12 | 737 | 706 | 693 | 675 | 574 | 1,132 |
| receivables | 1,038 | 1,382 | 1,475 | 1,744 | 1,358 | 1,331 | 1,492 |
| inventory, current | 913 | 915 | 1,003 | 1,315 | 1,321 | 1,406 | 1,351 |
| inventory in other assets | n/r | n/r | 148 | 110 | 215 | 236 | 273 |
| goodwill | 4,603 | 4,603 | 4,603 | 4,603 | 4,680 | 4,153 | 4,153 |
| intangibles | 503 | 651 | 649 | 533 | 1,414 | 1,130 | 1,112 |
| debt (balance sheet) | 0 | 9,134 | 8,913 | 8,760 | 8,880 | 8,644 | 8,553 |
| equity | 5,486 | -1,508 | -892 | -70 | 472 | 752 | 1,006 |
| retained earnings | n/a | -998 | -331 | 443 | 1,010 | 1,109 | 1,352 |

What the figures say. (1) **The spin loaded the debt.** $9.47B was borrowed in 2021 and $9.0B paid to Merck; equity went
from $5,486M to -$1,508M in one year. Four and a half years later principal is $8.55B; $1,114M of dividends were paid
2021 to 2025 while principal fell by less than $1B. (2) **Tangible equity is deeply negative**: goodwill and intangibles of
$5,265M against equity of $1,006M at June 2026. (3) **Inventory has run ahead of sales**: current inventory up 54% from
2020 to 2025 while sales fell 5%; with the inventory carried in other assets it was 26% of 2025 sales against 14% in 2020.
The filer attributes part of this to "inventory stock bridges" for its exits from Merck supply agreements (10-Q). This is
one of the named tells, "inventories look out of line, you know, with sales" **[M1995-064]**. (4) **Receivables are held
down by factoring**: $186M (2024) and $217M (2025) factored (10-K Note on financial instruments); added back, receivables
were about 25% of 2025 sales against 16% in 2020. (5) **Goodwill was written down $301M in 2025**, which the filer says
"resulted from the decline of the Company’s patent protected products in the U.S." (10-K FY2025, MD&A). What the figures
cannot say: what the products bought since 2021 will earn; the balance sheet shows only what was paid.

---
## THE FOUNDATIONS (not a gate)
Two foundations bear. **A share is a business:** "Would I be happy buying this stock if the market closed for five
years?" **[M1997-109]**. Today's price is not set by the business at all: it is set by an announced cash merger at $14.00,
the case the speakers call a workout, securities "whose value depends not on what the market price does, but whether a
given corporate event occurs" **[M2022-057]**, where "The profit is limited" and "if the deal blows up, you may have a
stock that’s at $40 or something" **[M2022-058]**. A buyer at $13.72 is buying the deal, and owns this business only if
the deal fails. **Who is paid to tell you:** the only multi-year forecast on file is management's own projection to 2030,
published in a sale proxy; "don’t ask the barber whether you need a haircut" **[M2011-083]**, and projections are not
consulted **[M1995-050]**.
**Contrary evidence, written down as found** **[M1997-127]**: (a) the case for the business: Nexplanon grew 17% from 2019
to 2025 and the FDA extended its label to five years in January 2026; Hadlima grew from $44M to $228M in two years;
Emgality grew 45% in H1 2026; China sales held between $829M and $933M a year over 2019 to 2025 despite VBP; owner cash
has been positive every year. (b) Against the deciding reading below: the merger proxy shows insiders did write a
five-year forecast (revenue $6,252M in 2026E rising to $6,822M in 2029E), which weakens any claim that the next five
years cannot be written down. Both are carried into Q1.

## THE STANDING RULE
Nothing in a cash purchase of this stock puts the buyer at risk of ruin if it is bought without borrowed money and sized
so that a loss of half the price (the unaffected price before the deal rumour is implied at about $6.90) does not matter:
"borrowed money has no place in the investor's tool kit" **[L2014-005]**; "We are never going to risk what we have and
need for what we don’t have and don’t need." **[M2012-081]**. The rule is met by the buyer's conduct, not by the target.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years" **[M2012-065]**, and "do I understand enough about this business so that the financial statements
will tell me the information that’s useful to me in making a judgment about what the future financial statements are
going to look like" **[M2008-033]**.

**The filing facts.**
- *What the business is.* Women's Health ($1,752M in 2025: Nexplanon $921M, Follistim $264M, others), biosimilars ($691M:
  Renflexis, Hadlima, Ontruzant, Brenzys) and established brands ($3,773M, of which $302M is Vtama and Emgality, bought or
  licensed since 2024) (10-K FY2025 Note 5, `0001628280-26-011125`).
- *The exclusivity is gone or going, by the filer's own words.* "Except for Emgality and Vtama , our established brands
  products are beyond market exclusivity." "Loss of patent protection typically leads to a significant and rapid loss of
  sales". Nexplanon, "the largest brand we commercialize that continues to have market exclusivity": US rod patents expire
  late 2027, applicator patents 2030; "market exclusivity for the majority of countries where Nexplanon is commercialized
  outside the United States will expire in the first half of 2026"; a Paragraph IV filer (Xiromed) was sued in April 2025,
  triggering a stay of up to 30 months (10-K FY2025, risk factors, MD&A, Note 18).
- *The filer says the business needs new products to stand still.* "Our results of operations may be adversely affected
  by the lost sales unless and until we have launched commercially successful products that replace the lost sales"; "We
  have limited in-house discovery and limited cash to pursue [...] external acquisitions, partnerships and collaborations,
  which may limit our ability [...] to replace the sales of products that lose patent protection" (10-K FY2025, risk
  factors).
- *The record of the book without replacement.* Revenue $7,777M (2019) to $6,216M (2025), -20%. Established brands
  excluding the bought Vtama and Emgality and manufacturing sales: $5,161M to $3,389M, -34%, about -6.8% a year, in steps:
  NuvaRing $879M to $91M, Singulair $698M to $252M, Zetia and Vytorin $875M to $442M, Cozaar/Hyzaar $442M to $219M, Atozet
  -31% in 2025 alone (10-K FY2021 Note 18 `0001821825-22-000002`; 10-K FY2025 Note 5). LOE cost $197M of 2025 sales. VBP
  in China: "Mature products that have entered into the first ten rounds of VBP have had, on average, a price reduction of
  over 50%", about 450 molecules, roughly semi-annual rounds (10-K FY2025). Reported gross margin 70.8% (2019, carve-out
  basis) to 53.3% (2025) to 54.0% (H1 2026).
- *What has been bought to replace it.* Dermavant (Vtama), 2024: $175M upfront, $75M on approval, up to $950M of
  commercial milestones, royalties (10-K FY2024 `0001821825-25-000006`); Vtama sold $128M in 2025 and $60M in H1 2026, and
  in Q2 2026 the contingent consideration was revalued "related to changes in the timing of expected commercial milestones
  based on updated sales forecasts" (10-Q). The 2025 goodwill impairment of $301M is attributed to "the decline of the
  Company’s patent protected products in the U.S." (10-K FY2025).
- *The insiders' forecast.* Management projections in the sale proxy (8-K `0001193125-26-307767`): revenue $6,252M
  (2026E), $6,475M, $6,693M, $6,822M (2029E), $6,470M (2030E); five years, not ten, written to support a sale, and
  depending on products not yet launched ("Organon’s pipeline products", same document).

**The key variables and whether they are foreseeable** **[M2012-065]**. (1) The pace at which the off-patent brands erode:
foreseeable in direction (down; the record above), not in pace, which moves in steps with each country's generic entry
and each VBP round. (2) The date generic Nexplanon reaches the United States: set by a patent case and the FDA, not by
anything an outside reader can know. (3) Government pricing in China, Japan, the EU and the United States (VBP, URPS,
MFN): "much of it is in the political realm. And my judgment about the [...] what politicians will do is probably not
better than yours." **[M2005-098]**. (4) Which products will be bought to replace the lost sales, at what price, earning
what: unknowable from outside, and the record so far (Dermavant) is a downward revision. Of the industry's single
companies the speakers say: "It would not have been within our circle of competence to try and pick a single company."
**[M1998-073]**; "when we invest in something like pharma, we don’t know the answer on the pipeline. It will be a
different pipeline anyway five years from now." **[M2008-113]**.

**The reading.** What can be foreseen about the ten-year economics is one thing, and it is the thing Q1 rules out: on the
filer's own words and on the 2019 to 2025 record, this is a business that is good only if new medicines keep arriving to
replace the ones losing protection, and that would be a shrinking, debt-laden run-off without them. The speakers name that
dependence in Q1's own list of what it rules out: "Take pharmaceuticals, if they had never invented any more
pharmaceuticals, it would be a terrible business." **[M1999-075]**. Organon does not invent (limited in-house discovery,
by its own account); it buys invention with borrowed money, which is the same dependence one step removed. The contrary
evidence from Step 0 does not reach this: the growing products (Nexplanon, Hadlima, Emgality) are themselves either losing
exclusivity on a schedule (Nexplanon) or sold in a bid market (biosimilars), and the insiders' five-year forecast rises
only on products not yet launched, then falls in 2030. Doubt on the remaining question, what replaces the book, keeps it
outside the circle in any case: "if you have doubts about something being into your circle of competence, it isn’t."
**[M2002-092]**.

**VERDICT: OUT** at Q1, under the rule against businesses that live on continued invention **[M1999-075]**, on the
filing facts above. A lower price does not reopen it: "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t
selling for a fraction of its worth." **[M2000-038]**. (The alternative readings, TOO HARD (NATURE) on variables 2 to 4,
and Q1 IN with Q2 OUT on the evidence of a castle being crossed, are set out in the last section; all three close the
file, and none reaches Q7.)

## Q2: WHY IS THE CASTLE STILL STANDING? NOT REACHED.
## Q3: HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED (the balance sheets were read in Step 0).
## Q5: WHO RUNS IT? NOT REACHED.
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7: WHAT IS IT WORTH? NOT REACHED (the computation below is not a clearance).
## Q8: IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9: COULD IT RUIN US? NOT REACHED.
## Q10: IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional): NOT ASKED.

---
## AFTER THE CLOSE: FACTS RECORDED FOR THE OPERATOR. NOT CLEARANCES, NOT VERDICTS.
Gathered in the same reading; written down because each bears on the box and because contrary evidence is written down as
found **[M1997-127]**. None of them is an answer to a question the run did not reach.

**The competitor row (Q2 material), same metric from each filer's own XBRL statements, whole span available.** Reported
gross margin (cost of sales includes amortization at all four) and revenue, USD M:

| filer | first year | gross margin | revenue | latest year | gross margin | revenue | accession (latest 10-K) |
|---|---|---|---|---|---|---|---|
| Organon | 2019 | 70.8% | 7,777 | 2025 | 53.3% | 6,216 | 0001628280-26-011125 |
| Viatris (Mylan to 2019) | 2014 | 45.7% | 7,720 | 2025 | 35.1% | 14,300 | 0001792044-26-000013 |
| Teva | 2015 | 57.8% | 19,652 | 2025 | 51.8% | 17,258 | 0001193125-26-034532 |
| Perrigo | 2014 | 35.7% | 4,061 | 2025 | 35.1% | 4,253 | 0001585364-26-000009 |

Viatris revenue fell from $17,886M (2021, first full year after the Upjohn merger) to $14,300M (2025), -20%; Teva from
$22,385M (2017) to $17,258M, -23%, with its margin trough at 44.0% in 2018; Perrigo from $5,281M (2016) to $4,253M, -19%.
Every filer in the off-patent field shrank over its span; Organon kept the highest margin and lost the most of it (17.5
points in six years). Peer figures are XBRL transcription from each filer's companyfacts and were not cross-checked
against the peers' filed statements. No listed women's-health peer was fetched.

**The Nexplanon wholesaler matter (Q4 and Q5 material).** The audit committee found the company "asked certain
wholesalers in the United States to purchase greater quantities of Nexplanon" than demand at the end of Q4 2022, Q3 and
Q4 2024, and Q1 to Q3 2025, in some cases waiving inventory-fee metrics, and that "without these sales practices, the
Company’s consolidated revenue for certain of those periods would have fallen short of the Company’s guidance and/or
certain external revenue expectations"; the board found "certain of the Company’s prior statements were inaccurate or
incomplete" (8-K `0001104659-25-102324`). The CEO resigned without severance on 2025-10-26; the head of US commercial was
dismissed. The 10-K and 10-Q report material weaknesses: "We failed to set an appropriate tone at the top. Specifically,
our former CEO and leader of our U.S. commercial organization applied inappropriate pressure to achieve sales targets"
(10-Q). The SEC opened an investigation after a voluntary self-disclosure; consolidated securities class actions and
derivative suits are pending (10-Q Note 15). No restatement. A second audit-committee review in February 2026 (timing of
biosimilar purchases) found no improper conduct (8-K `0001104659-26-017870`). The 2025 annual bonus weighted revenue at
40% (DEF 14A). The rows that bear: "Managers that always promise to "make the numbers" will at some point be tempted to
make up the numbers." **[L2002-041]**; "you get what you reward for" **[M2016-083]**; "There is seldom just one cockroach
in the kitchen." **[L2002-039]**. Under the framework's two-tell convention this is the habit plus a second tell
(statements found inaccurate), the suspicion the Q4 STOP names; it was not reached as a verdict.

**Capital allocation (Q6 material).** No buybacks; shares 253.5M at the spin to 262.6M (+3.6%). Dividends of $1,114M paid
2021 to 2025, then cut 90% in 2025 to $0.02 a quarter "with the goal of accelerating an improvement in our net leverage"
(10-K FY2025). The securities suits allege misleading statements about the dividend and debt-reduction strategy
(10-Q Note 15). Product purchases 2021 to 2025 about $1.1B (cash-flow statements), plus Dermavant milestones contingent.

**Debt (Q9 material).** Principal $8,553M at 2026-06-30: term loans due 2031 ($1,522M and EUR 707M), secured notes due
2028 ($2,100M at 4.125% and EUR 1.25B at 2.875%, together $3,525M), unsecured notes due 2031 ($1,582M), notes due 2034
($1,000M); weighted rate 4.9%, average maturity 4.1 years; revolver undrawn; cash $1,132M after the Jada sale (10-Q
`0001628280-26-051230`, Note 10). Coverage as pre-tax earnings plus interest over interest **[L2012-002]**: 3.7x (2022),
2.3x (2023), 2.6x (2024), 1.8x (2025, after the goodwill charge). No product-liability insurance for most product
liabilities (10-Q Note 15). "Companies with large debts often assume that these obligations can be refinanced as they
mature. That assumption is usually valid." **[L2010-020]**.

**The workout.** Merger agreement of 2026-04-26 with Sun Pharmaceutical: $14.00 cash a share, "a 103% premium to the
Company’s closing Share price on April 9, 2026" (implying about $6.90 unaffected); Sun has committed debt financing;
conditions are HSR, non-US antitrust and foreign-investment approvals and no material adverse effect; outside date
2027-01-26, extendable for regulatory conditions; a $120M fee payable by Organon in certain cases (8-K
`0001193125-26-178718`). Stockholders adopted it on 2026-07-23, 192,776,552 for and 2,573,118 against (8-K
`0001193125-26-314587`). The 10-Q says the transaction "is expected to close in early 2027". At $13.72 the gross spread is
$0.28 plus one or two $0.02 dividends: 2.2% over four months (6.7% a year) or 2.3% over six (4.7% a year), against a
downside to the unaffected level of about half the price. The speakers' rows: diversify such commitments **[L1993-024]**,
and "you don’t take on the United States government" **[M2023-096]**. The framework has no question for a workout; see
the last section.

---
## COMPUTATION — NOT A CLEARANCE
*(Label required by operator rule 3. Arithmetic only; the file closed at Q1 and nothing below is entry language.)*

**(a) VALUE RANGE, Q7 CONVENTION** (five-year average owner cash after every real cost, carried ten years at the growth
shown, then no nominal growth, at the 5.66% sovereign; ends = no-growth and shown-growth cases; per share on 262.6M):
- *As the convention reads mechanically (2021 to 2025, capex basis):* base $812.6M, shown change 2021 to 2025 -29.9% a
  year: **$6.90 to $54.67**, about eight to one. The width alone would close Q7 TOO HARD **[L2000-025]**, and the base and
  the growth are both artefacts of the abnormal 2021 **[L2005-003]**.
- *Whole-cycle variant, dropping 2021 (2022 to 2025), all capital spending deducted* (capex plus product rights, acquired
  IPR&D and Dermavant, the convention's "all capital spending"): base $335.5M, shown -13.3% a year: **$8.16 to $22.57**,
  2.8 to one. The price of $13.72 sits inside it.
- *Same window, capex only* (product purchases treated as optional growth outlays, not maintenance **[L1999-024]**): base
  $538.5M, shown -7.7% a year: $19.82 to $36.23, 1.8 to one.
- Fully diluted (284.9M shares) each figure is about 8% lower.

**(b) FAIR PRICE** (the price at or below which the central case clears about 10% pre-tax, the floor CONVENTION
**[M2003-149]**). Tax treatment, a CONVENTION of this run: owner cash is after the company's interest and taxes, and the
10% is read as the return to the holder before the holder's own tax. Central case, a CONVENTION of this run: the
whole-cycle base after all capital spending ($335.5M), carried at half its shown decline (-6.65% a year) for ten years,
then flat, discounted at 10%: **about $8.25** ($7.60 diluted). On the capex-only base the same construction gives about
$15.85.

**(c) CHEAP PRICE** (rule, a CONVENTION of this run: the price at which the low end of the whole-cycle range, the base
after all capital spending carried at its full shown decline, still returns 10%, so that no pencil is needed even in the
worst case shown **[M1996-084]**, **[M2009-005]**): **about $5.50** ($5.10 diluted).

Against the price: $13.72 is above the fair price on the convention's base and inside the whole-cycle range; it is about
twice the unaffected price, and is held there by the $14.00 cash offer, not by the business.

---
## THE BOX
**OUT at Q1**: a business whose ten-year economics depend on replacing products that lose exclusivity, with medicines it
does not invent and buys with borrowed money **[M1999-075]**; closed before any valuation. (Computation only: whole-cycle
range $8.16 to $22.57, fair about $8.25, cheap about $5.50, against $13.72, the price set by a pending $14.00 cash
merger.) Q11 belongs to the holding review.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. [ ] Written question by question and committed after each: **NOT
      DONE.** The file was written in one pass after the reading, and nothing was committed (the dispatch forbade commits).
      The write-early rule was broken.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, below); every filing fact has its accession;
      peer figures are flagged as XBRL transcription.
- [x] The order was kept; Q1 closed the run; Q2 to Q10 are NOT REACHED; the after-close facts are marked as no verdicts and
      the valuation carries the COMPUTATION label.
- [x] Owner cash after stock pay and all capital spending, never a net-income proxy; the sovereign from the US Treasury;
      the price flagged as an aggregator quote.
- [x] Contrary evidence written down (Foundations; Q1). [ ] Written within thirty minutes of finding it: not shown, since
      the file was written in one pass.
- [x] No point-in-time anchor applies (a live run); no row is dated after today.
- [x] Only the arithmetic lines of `tools/run.py` were used; its yield and growth lines were not.
- [x] `python tools/check_framework.py` PASS after writing (2026-10-05); `_research 2026-10-05 OGN/check_ids.py`: no E-ids, every id in the v5 ledger, every quoted fragment found in its row. Not committed (dispatch rule).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1's two lists disagree about pharmaceuticals.** **[M1999-075]** stands in Q1's "What it rules OUT" list, but the
row's own words make it a technology-dependence row ("dependent on the technology continuing to gallop"), and the
correction pass of 2026-10-05 moved "fast-moving technology and businesses that change" to TOO HARD on the ground that the
rows give ignorance as the reason. A name like Organon can therefore close Q1 OUT (the dependence shown, as here), Q1 TOO
HARD (NATURE) (the replacement products, the patent case and government pricing cannot be foreseen: **[M1998-073]**,
**[M2008-113]**, **[M2005-098]**), or pass Q1 as an understood run-off and close Q2 OUT on a castle shown being crossed
(**[M2012-062]**: "If you really think a business is declining, most of the time you should avoid it."). I chose OUT
because the filer states the dependence and the 2019 to 2025 record shows it; a second analyst could defensibly choose
either other reading. The box is closed in all three; a ruling on which list M1999-075 belongs to would make the deciding
question reproducible. (2) **No question handles a workout.** The price is set by a $14.00 cash merger approved by the
holders; the rows on workouts (**[M2022-057]**, **[M2022-058]**, **[L1993-024]**) sit in the ledger but no question of v5
asks whether the deal, not the business, is being bought. I recorded the spread arithmetic after the close; it does not
clear the 10% floor at any closing date the filer gives. (3) **The Q7 convention's "five-year average" has no rule for a
spin year.** The 2021 owner cash is 3.5 times any later year for reasons of separation accounting; the reporting request
allowed a whole-cycle variant, but the convention itself does not say which years replace the abnormal one; I dropped it
and used four years. (4) **"All capital spending" is undefined for a company that buys products.** Product-right purchases
and acquired IPR&D are investing outflows that replace eroding sales; I deducted them in the convention's base and showed
the capex-only variant; the two fair prices differ by a factor of about two. (5) **The protocol's mandated label
"COMPUTATION — NOT A CLEARANCE" contains the dash the standing style rule forbids**; I kept the protocol's exact label once
and used no other.

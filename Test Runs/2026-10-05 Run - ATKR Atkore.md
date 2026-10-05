# Company Run — Atkore Inc. (NYSE: ATKR) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The dispatch's blind rule forbids opening `PORTFOLIO.md`,
any holding review, the resume state, the run queue and the prepped reading list, and this run did not open them. Whether
the operator holds or wants this name is unknown to the analyst.

**CONTAMINATION DECLARED.** (1) The commit subjects visible at session start name other runs of 2026-10-05 (WCC, LMB, DY,
MTZ, PRIM) and their boxes, all OUT at Q2; the git status shows run files for HUBB and NVT dated today. None was opened.
The pattern (electrical and construction names closing at Q2) was seen and is named here so it can be discounted. (2) The
analyst knew from general knowledge, before any fetch, that Atkore was a PVC and steel conduit maker that earned a large
windfall in 2021 to 2023; the filings were read to test that, not to confirm it. (3) Discovered in the filings, not known
before: Atkore agreed on 2026-08-02 to be acquired by Prysmian for $95.00 cash a share (below, Step 0). This fact changes
what a purchase today is, and it is carried openly through the run.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $94.78 (2026-10-05, as printed by `tools/run.py`; an aggregator quote, flagged per operator rule 5, live
  quote only). The unaffected close before the deal was $72.96 on 2026-07-31 (the company's own figure, DEFA14A of
  2026-09-30, accession 0001666138-26-000035).
- **The pending deal.** Agreement and Plan of Merger dated 2026-08-02 with Prysmian S.p.A.: each share "will be converted
  into the right to receive $95.00 in cash, without interest"; no financing condition; regular dividends allowed at no more
  than $0.33 a quarter; HSR waiting period expired 2026-09-14; other approvals (Austria, Australia, Canada) and the
  stockholder vote outstanding; outside date 2027-08-03 with two three-month extensions; company termination fee
  $115.92 million (8-K, 2026-08-03, accession 0001666138-26-000016; 8-K, 2026-09-15, accession 0001666138-26-000027;
  DEFM14A, 2026-09-09, accession 0001140361-26-035981). The price sits $0.22 under the deal price.
- **Shares by class** from the latest filing's cover: one class, Common Stock $0.01 par, **33,772,550** (10-Q for the
  quarter ended 2026-06-26, filed 2026-08-04, accession 0001628280-26-052084; `python Screens/cover_shares.py ATKR`). The
  10-K cover gave 33,750,486 at 2025-11-24 (accession 0001628280-25-054049).
- **Market cap:** 33.77M x $94.78 = **$3,201M** (at the deal price, $3,208M).
- **Sovereign for the earnings currency (USD):** **5.63%**, US Treasury daily par yield curve, 30-year, 2026-10-02
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): Form 10-K for FY ended 2025-09-30, filed 2025-11-26, accession 0001628280-25-054049
  (Items 1, 1A, 3, 5, 7, 8 notes on debt, goodwill, legal matters); the nine 10-Ks FY2016 to FY2024 for the sales bridges
  and the record (accessions 0001666138-16-000021, -17-000105, -18-000129, -19-000094, -20-000123, -21-000163,
  -22-000128, -23-000111, -24-000164); 10-Q for the quarter ended 2026-06-26 (accession 0001628280-26-052084); the annual
  proxy DEF 14A filed 2025-12-12 (accession 0001666138-25-000204); the merger proxy DEFM14A filed 2026-09-09 (accession
  0001140361-26-035981) and its supplement of 2026-09-30; the 8-Ks of 2025-09-29 to 2026-09-15 listed where used.
- **One figure cross-checked against the filed statement:** FY2025 net cash from operating activities, $402,762 thousand
  in the 10-K's liquidity table ("Operating activities | $ | 402,762 | $ | 549,033"), equal to the XBRL figure $402.8M that
  `tools/run.py` used. Agrees.
- `python tools/run.py ATKR` arithmetic lines only (its v4 rule text, ids and floor are ignored, Part VII): OCF less SBC
  less capex, FY2021 to FY2025 (USD millions): 2021 573-17-65 = 491; 2022 787-17-136 = 634; 2023 808-21-219 = 568;
  2024 549-20-150 = 379; 2025 403-24-107 = 272. Five-year mean **469** (all capex deducted); run.py's 3-year mean 400 to
  450 and 5-year 462 to 505 (its "hi" end deducts only depreciation-level capex). SBC is resolved and complete in every
  year (12.8 to 23.6). D&A FY2025 124.5 (depreciation 82.6, intangible amortization 41.9). These are recast at Q4; the
  window FY2021 to FY2025 sits wholly inside or just after the PVC price spike and is treated at Q7, not here.

## THE FOUNDATIONS (not a gate)
Three foundations bear on this name, and the first changes what a purchase is. **A share is a business:** the test is
"Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**. At $94.78, with $95.00 cash
agreed, a buyer today is not buying the conduit business for five years; he is buying what the speakers call a workout,
a security "whose value depends not on what the market price does, but whether a given corporate event occurs"
**[M2022-057]**. The run below answers the framework's questions about the business, as the dispatch asks, and the
workout is set out separately after the box, as computation. **The market serves, it does not instruct:** the deal price,
the bids of $72 to $95 in the sale process (DEFM14A, background, accession 0001140361-26-035981) and the unaffected
$72.96 "just tells us prices" **[M2006-077]**; none of them is a value. **Who is paid to tell you:** the merger proxy
carries management's projections to fiscal 2030 and two fairness opinions from bankers paid on the deal; "you do not get
impartial advice from Wall Street" **[M2020-037]**, and the projections were not read for this run ("we’ve never looked
at a projection" **[M1995-050]**).

**Contrary evidence, written down as found** **[M1997-127]** (in the order found):
1. Item 1 of the 10-K claims "#1 or #2 positions in the United States by net sales in a significant number of our
   products", "must-stock lines" at many of the more than 12,000 US electrical-distributor branches, and a low-cost
   in-line galvanizing process (Flo-Coat) (accession 0001628280-25-054049). These are the company's own claims, unproven.
2. Before the boom the Electrical segment earned an Adjusted EBITDA margin of 18.7% (FY2018), 20.3% (FY2019) and 22.5%
   (FY2020) (10-Ks FY2019 and FY2020), and operating income of $224M on about $955M of capital employed in FY2019
   (equity $233M plus long-term debt $845M less cash $123M): a decent pre-tax return in a normal year.
3. Volume is rising now: Electrical volume +$62.8M in the June 2026 quarter and +$114.6M over nine months (10-Q,
   accession 0001628280-26-052084).
4. Against my favourite reading of the castle as open, the boom's margins were not unique to Atkore (see Q2): that cuts
   both ways, since it also means Atkore was not uniquely bad.
5. Found later and against the business: a DOJ Antitrust Division grand jury subpoena of 2025-02-13 on "the pricing of
   the Company’s PVC pipe and conduit products", still open; $186.5M of class settlements without admission (10-Q note
   16); securities class actions and derivative suits pending, one with an insider-trading claim.

## THE STANDING RULE
Nothing in buying this stock for cash, unlevered and sized so that a break of the deal could be borne, puts the buyer at
risk of ruin: "We are never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**;
no borrowed money, which "can prevent you from playing out your hand" **[M2004-065]**; no arrangement that could bring
"sudden demands for large sums" **[L2014-024]**. The rule binds the buyer's conduct, and the conduct proposed is a cash
purchase. PASS for the buyer; the target's own debt would be Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What it is, from the filing.** A converter of steel, PVC resin and copper into standard electrical raceway: metal and
  PVC conduit and fittings, armored (MC) cable, flexible conduit (Electrical, $2.0B of FY2025's $2.85B sales), and metal
  framing, mechanical tube for solar trackers and perimeter security (Safety & Infrastructure, $0.85B). 88% of sales in
  the US; about 83% through electrical and industrial distributors; top ten customers about 40%; Sonepar over 10%;
  38 plants. Demand follows US non-residential construction and repair; "We generally sell our products on a spot basis
  (and not under long-term contracts)" (10-K Item 1A, accession 0001628280-25-054049).
- **The key variables and how predictable they are** **[M1998-044]**: (1) unit volume, which follows non-residential
  construction and moved +5.0%, -3.2%, +3.2%, +3.5%, +0.7% in FY2021 to FY2025 (10-K sales bridges); predictable within a
  band. (2) The spread between the selling price and the cost of resin, steel and copper, which moved the selling price
  +55.4% (FY2021), +34.0% (FY2022), -16.5% (FY2023), -11.5% (FY2024), -11.9% (FY2025) (consolidated bridges, 10-Ks
  FY2021 to FY2025). The company said of it in 2021: "Pricing for PVC products, as well as other parts of the business,
  are expected to return to more normal historical levels over time, but that time is uncertain." (10-K FY2021,
  accession 0001666138-21-000163).
- **The test as stated.** Understanding is "a reasonable fix on about what the earning power and competitive position
  will look like in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand the economic dynamics
  of the industry" **[M2011-014]**. The dynamics here are plain and on the record: a spot-priced converter of three
  commodities, sold through distributors who also stock competitors, whose margin is set by the spread. What the spread
  will be is the castle question, and the industry's insiders do write it down: Otter Tail, a PVC pipe maker, "we expect
  these industry conditions to gradually normalize through 2027" (OTTR 10-K FY2025, accession 0001466593-26-000008), so
  test 5 of Q1 **[M2000-105]** does not send this name to NATURE. The question is "important and knowable"
  **[M2006-076]**. The technology does not change fast: the products are built to the National Electrical Code and UL
  standards, and the routing rule for fast change does not apply.
- **Doubt test** **[M2002-092]**: I do not doubt the dynamics; I doubt the level of the spread, which is a Q2 matter and
  is answered there from the evidence, not here by a refusal.
- **VERDICT: IN.** The economics of a commodity converter in a construction-cyclical market can be foreseen as to how they
  work **[M2011-014]**, **[M2012-065]**; whether the earning power holds is Q2's.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**. The tests, each with its filing fact:

- **Is it a commodity business?** The rows define one by the customer's indifference and by price competition
  **[L2004-003]**. Atkore's own words: "Competition is based primarily on product offering, product innovation, quality,
  service and price"; competitors "adding production capacity and the expansion of imported products, may encourage us to
  lower our prices"; "Substantially all of the products we sell (such as steel conduit, tubing and framing, copper wiring
  in our cables, and PVC and HDPE conduit) are subject to price fluctuations because they are composed primarily of steel,
  copper or resin"; its distributors "also offer the products of our competitors to our ultimate customers" (10-K Item 1A,
  accession 0001628280-25-054049). Encore Wire, a peer in copper building wire, called its own line a "commodity"
  product line and said it "sells its products in accordance with prevailing market prices" (Encore 10-K FY2023,
  accession 0000850460-24-000017). The products are made to code, interchangeable across makers, and sold on the spot.
  This is "a product with commodity-like economic characteristics" **[L2000-017]**.
- **Pricing power and the agony before a rise** **[M2005-020]**; "the businesses with strong competitive positions
  manage to pass through increases in raw material costs" **[M2005-017]**. The selling price fell three years running
  while volume held: FY2023 price -16.5% with volume +3.2%; FY2024 price -11.5% with volume +3.5%; FY2025 price -11.9%
  with volume +0.7% (10-K bridges). In fiscal 2026, with Electrical volume up, the company could not pass costs through:
  "The decrease in Adjusted EBITDA and Adjusted EBITDA margin was largely due to the increase in input costs outpacing
  increases in average selling prices" (10-Q, nine months, accession 0001628280-26-052084). And in FY2025: "We generally
  sell our products on a spot basis and as such, were exposed to sales prices on our products that decreased faster than
  the cost for the related raw materials" (10-K MD&A). The price is the market's: "whatever he charged for gas was my
  price" **[M2012-109]**.
- **Widening or narrowing** **[M1999-108]**. Electrical segment Adjusted EBITDA margin (the filer's own measure, used here
  only as a like-for-like trend, never as earnings): FY2018 18.7%, FY2019 20.3%, FY2020 22.5%; FY2021 39.1%, FY2022
  42.3%, FY2023 37.6%; FY2024 30.9%, FY2025 16.5%; nine months FY2026 13.8% against 17.9% a year before (10-Ks FY2019 to
  FY2025; 10-Q). The margin has fallen below where it stood before the boom. Consolidated operating margin: FY2016 to
  FY2020 8.3% to 13.6%; FY2022 31.5%; FY2025 8.3% before $214.4M of impairments (0.8% reported). This is narrowing, not
  a cyclical dip in a widening position of the kind the 1995 letter describes **[L1995-022]**: no filing fact shows a
  competitive superiority maintained.
- **The low-cost exception** **[L2004-007]**, **[L2000-017]**, **[M1997-010]**. The rows let a commodity business through
  if it is the low-cost producer, measured against the competitor **[M2001-013]**, **[M2009-059]**. The evidence:
  (a) the only claim is the company's own (Flo-Coat galvanizing; "low-cost high-quality galvanized tube products");
  (b) in the normal years FY2016 to FY2020 its operating margin (8.3% to 13.6%) sat below Hubbell's (12.4% to 13.7%) and
  nVent's (14.0% to 15.7% excluding nVent's 2020 impairment year) and near Otter Tail Plastics' (about 11% to 12% net in
  2018 to 2019); (c) one of its three named PVC resin suppliers, Westlake ("our primary suppliers of PVC resin are
  Westlake, Formosa and Oxy Vinyls", Atkore 10-K Item 1), calls itself "a vertically integrated global manufacturer" and
  makes PVC pipe for "electrical duct and conduit" (Westlake 10-K FY2025, accession 0001262823-26-000016): Atkore buys its
  main plastic input from an integrated competitor, and Otter Tail names the same handicap in its own filing, competitors
  with "integration with PVC resin producers" (OTTR 10-K FY2025, accession 0001466593-26-000008); (d) today it cannot pass
  costs through (above). No filing fact shows Atkore to be the low-cost producer; the exception is not shown, and
  "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**.
- **The attacker with money** **[M2011-015]**, and imports **[M2007-116]**. The 10-K names as competitors Zekelman,
  Mitsubishi, Nucor, Southwire, Dura-Line and Prysmian in Electrical, and Zekelman, Eaton, ABB, Hubbell, nVent and Haydon
  in Safety & Infrastructure; it names imports as able to "depress the selling prices of our products and those of our
  competitors". The product is one "that can be shipped in from abroad very easily" **[M2007-116]** and is made by many
  with capital. A sweep of all ten 10-Ks (FY2016 to FY2025) for "antidumping", "anti-dumping" and "countervailing" found
  no trade protection for conduit; the only instance is an order against Atkore's own imported fittings (FY2017 to
  FY2019). Rivals are already in every line, and "you can have only two competitors and they’re still terrible
  businesses" **[M2013-052]**.
- **Would the customer still choose it over the low bid?** **[M2017-009]**, **[M1997-102]**. The buyer is a distributor
  stocking several makers' code-compliant conduit for a contractor; no filing fact shows a price premium held against a
  cheaper rival in the three years prices fell. The company merged its brands in 2020 into "one master brand, Atkore" (10-K Item 1);
  no filing shows the contractor asking for it by name.
- **Ask the competitors** **[M1999-130]**, **[M2017-091]**. No interview was possible. What competitors did, on the
  public record: the same windfall came and went at the commodity converters at the same time (row below); one strategic
  bidder in the 2026 sale process wanted only Atkore's "conduit business" and excluded the antitrust liabilities (DEFM14A,
  background, Bidder D).
- **What could destroy, modify or reduce it** **[M2000-014]**. The pricing of the boom years is the subject of a DOJ
  grand jury investigation and of class suits alleging that manufacturers "improperly shared otherwise confidential
  information through their contribution of information to, and readership of, a weekly report" published by OPIS
  (10-Q note 16). Atkore admits nothing and settled the three classes for $186.5M. I draw no conclusion of guilt. The fact
  that bears on the castle is narrower: the earning power of 2021 to 2023 rested on an industry price level, which the
  industry is accused of having coordinated and which has since fallen, not on a cost or brand position of Atkore's.

**The competitor row** (operating income over sales unless stated; each company's own filings, XBRL as first filed, the
segment figures read from the 10-K text):

| Company (what it makes) | normal years | boom peak | latest | source |
|---|---|---|---|---|
| Atkore, consolidated | 8.3% to 13.6% (FY2016 to FY2020) | 31.5% (FY2022) | 8.3% before impairments (FY2025); 9M FY2026 operating income $94.4M on $2,182M (4.3%, after $11.6M of impairments) | 10-Ks listed at Step 0; 10-Q 0001628280-26-052084 |
| Atkore, Electrical segment, Adjusted EBITDA margin (filer's measure, trend only) | 18.7% to 22.5% (FY2018 to FY2020) | 42.3% (FY2022) | 16.5% (FY2025); 13.8% (9M FY2026) | same |
| Otter Tail Plastics (PVC water pipe) | net income $23.8M on $197.8M (2018) and $20.6M on $183.3M (2019); operating income $37.8M on $205.2M (2020, 18.4%) | 51.6% (2022: $264.6M on $512.5M) | revenue less cost of goods and SG&A $231.1M on $422.8M (2025, 54.7%) | OTTR 10-Ks 0001437749-20-003157, 0001466593-23-000053, 0001466593-26-000008 |
| Encore Wire (copper building wire) | 5.4% to 7.7% (2016 to 2020) | 30.3% (2022) | 17.6% (2023, its last 10-K in EDGAR) | XBRL; 10-K 0000850460-24-000017 |
| Hubbell (branded electrical products) | 12.4% to 13.7% (2016 to 2020) | no spike: 14.3% (2022) | 20.7% (2025) | XBRL; 10-K 0001628280-26-007500 |
| nVent (enclosures, fastening, thermal) | 14.0% to 15.7% (2016 to 2019) | no spike: 15.1% (2022) | 15.8% (2025) | XBRL; 10-K 0001628280-26-008608 |
| Westlake (resin maker, integrated into PVC pipe and conduit) | pipe margin not separable (its HIP segment mixes siding, windows and pipe) | | | 10-K 0001262823-26-000016 |
| Steel conduit peers (Zekelman private; Nucor's tubular products inside a larger segment) | not separable from public filings | | | |

What the row says: the boom appeared at the same time in the three commodity converters (Atkore, Encore, Otter Tail
Plastics) and not in the two branded electrical makers (Hubbell, nVent). It was an industry condition of the converters,
not a castle of Atkore's. In the reversal Atkore fell back faster than Otter Tail's water pipe and is now below its own
pre-boom margin, while Hubbell's rose. This is the field where "the improvement you get one day, your competitor gets the
next day" **[M2004-053]**, and the 2021 to 2023 returns are of the kind on which the speakers "would not want to buy
things on the basis that these returns would be sustained" **[M1998-016]**.

- **Why OUT and not TOO HARD.** The castle's future is not unknowable here; the evidence runs one way. The filer's own
  words describe price competition, spot selling, import pressure and costs it cannot pass through; the margin has
  narrowed past its pre-boom level; the low-cost exception is not shown and a main resin supplier is an integrated rival;
  the peers show the windfall belonged to the industry. "Business history is filled with "Roman Candles," companies whose
  moats proved illusory and were soon crossed." **[L2007-004]**. A castle shown open on the evidence is OUT
  **[M2011-015]**, and price does not reopen it: "What you can’t do is turn any investment into a good deal by paying
  little" **[M2019-015]**.
- **VERDICT: OUT.** A commodity-like converter whose price is set by the market **[M2012-109]**, **[L2004-003]**, that has
  not shown the low-cost position the rows require to prosper in such a field **[M1997-010]**, **[L2004-007]**, and whose
  margin is narrowing below its pre-boom level **[M1999-108]**. The file closes here.

---
## Q3 to Q10, Q12: NOT REACHED
The file closed at Q2. Q3 (capital), Q4 (the numbers), Q5 (the people), Q6 (the money and the owners), Q7 (value), Q8
(alternatives), Q9 (the target's debt), Q10 (the fat pitch) and Q12 (optional) are not answered, and nothing below is a
clearance of any of them. The facts the owner asked for (the balance sheets, owner cash, the range, the fair-price band
and the cheap price) follow under COMPUTATION — NOT A CLEARANCE. The antitrust, securities and derivative matters are
recorded as facts; no judgment of integrity is made, since Q5 was not reached.

---
## THE BOX
**OUT at Q2.** A commodity-like converter of steel, resin and copper whose price is the market's, without a shown
low-cost position, whose 2021 to 2023 margins were an industry windfall now reversed below the pre-boom level. Not a TOO
HARD, so no research pass is opened. For the record only (COMPUTATION, below): value range $55 to $133 a share on a base
that treats the boom as aberrational (the convention read literally gives $86 to $247), against $94.78, with $95.00 cash
agreed.

---
## COMPUTATION — NOT A CLEARANCE
*Everything in this section was produced after the file closed at Q2, at the owner's request (reporting, not a rule
change). It answers no question of the framework, carries no entry language, and binds nothing (operator rule 3).*

### C1. The balance sheets, ten years, read before the income account
"I like to look at balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**.
USD millions at each fiscal year-end (XBRL as first filed, the accessions at Step 0; June 2026 from the 10-Q):

| FY | equity | goodwill + intangibles | tangible equity | cash | long-term debt | net debt | receivables / sales | inventory / sales | PP&E | retained earnings |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 257 | 371 | -114 | 200 | 629 | 429 | 12.6% | 10.6% | 203 | -113 |
| 2017 | 361 | 492 | -131 | 46 | 572 | 526 | 14.9% | 13.3% | 209 | -42 |
| 2018 | 122 | 462 | -340 | 127 | 878 | 751 | 14.4% | 12.1% | 213 | -317 |
| 2019 | 233 | 472 | -239 | 123 | 845 | 722 | 16.5% | 11.8% | 261 | -200 |
| 2020 | 378 | 444 | -65 | 284 | 804 | 519 | 16.9% | 11.3% | 244 | -64 |
| 2021 | 865 | 440 | 425 | 576 | 758 | 182 | 17.9% | 9.8% | 276 | 389 |
| 2022 | 1,250 | 672 | 578 | 389 | 760 | 372 | 13.5% | 11.6% | 390 | 802 |
| 2023 | 1,468 | 706 | 763 | 388 | 763 | 375 | 15.9% | 14.0% | 559 | 995 |
| 2024 | 1,540 | 654 | 886 | 351 | 765 | 413 | 15.3% | 16.4% | 652 | 1,049 |
| 2025 | 1,398 | 455 | 943 | 507 | 757 | 250 | 15.7% | 17.0% | 594 | 889 |
| Jun 2026 | 1,276 | 409 | 867 | 346 | 756 | 410 | (quarter) | (quarter) | 521 | n/a |

What the figures say. (1) Before the boom this was a leveraged company with negative tangible equity every year from
FY2016 to FY2020; in FY2018 it borrowed $425M to buy back about 17.2 million shares from its private-equity sponsor
(CD&R) at $21.77, $375M in all (10-K FY2018, accession 0001666138-18-000129), which took equity to $122M. (2) The boom
built the balance sheet, not the business's structure: retained earnings went from -$64M to +$1,049M in four years and
tangible equity turned positive. (3) Long-term debt stayed at about $757M to $765M from FY2021 to June 2026; the boom's
cash went to buybacks of $1.61B (FY2021 to FY2025), acquisitions of $440M (FY2021 to FY2024) and capital spending, not to
repaying debt. (4) PP&E more than doubled, $276M (FY2021) to $652M (FY2024), with capital spending of $505M in FY2022 to
FY2024 against depreciation of $171M, built at the peak; the HDPE part of it was then written down ($194.5M in FY2025,
$6.5M of goodwill and a $25.7M loss on assets held for sale in FY2026) and sold. (5) Inventory rose against sales from
9.8% (FY2021) to 17.0% (FY2025) while prices fell: inventory "out of line, you know, with sales" is one of the tells
**[M1995-064]**; it was not tested at Q4, which was not reached. (6) Goodwill and intangibles fell from $706M to $409M
with the impairments and the amortization. What they cannot say: whether the boom's margins were earned or, as alleged,
coordinated; the balance sheet shows only that the cash came and where it went.

### C2. Owner cash after every real cost, and how the boom was treated
Owner cash = operating cash flow less stock pay less all capital spending (USD millions; XBRL, the FY2025 operating cash
flow cross-checked to the filed statement at Step 0). Stock pay is deducted because the cash flow statement adds it back;
the operating cash flow is after interest and tax, so the figures are cash to the equity and no net debt is subtracted
again. The depreciation variant (capital spending replaced by depreciation) is shown beside it as the convention asks.

| FY | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| owner cash (all capex) | 118.7 | 83.8 | 92.5 | 163.0 | 201.9 | 491.4 | 633.8 | 567.6 | 378.8 | 272.1 |
| depreciation variant | 102.7 | 76.6 | 96.2 | 158.4 | 193.5 | 511.0 | 721.4 | 728.8 | 463.2 | 296.6 |
| as % of sales | 7.8% | 5.6% | 5.0% | 8.5% | 11.4% | 16.8% | 16.2% | 16.1% | 11.8% | 9.5% |

Trailing twelve months to June 2026: operating cash flow $120.1M (after $136.5M of settlements paid and a $163.4M rise
in receivables), stock pay $27.0M, capital spending $62.6M: $30.5M. On the earnings side, trailing operating income
before impairments $135.9M, less interest $28.8M, taxed at 21%, plus the after-tax amortization of acquired intangibles
($26.2M pre-tax, added back as the rows allow for amortization that does not deplete **[L2015-004]**): about **$105M**,
before the $186.5M of settlements, which are left out of the run rate and counted separately (C5). FY2025 on the same
earnings basis: pretax $202.0M before the impairments and the Northwest Polymers loss, about $193M after tax with the
amortization added back. The figures are "after interest, taxes, depreciation, amortization and all forms of compensation"
**[L2021-003]**; the filer's Adjusted EBITDA is not used, the speakers call that figure "utter nonsense" **[M1998-086]**.

**The boom in the base.** The Q7 convention averages the last five years, FY2021 to FY2025, which are three boom years
and two years of reversal: mean owner cash $468.7M (depreciation variant $544.2M), shown growth -13.7% a year (from
$491M to $272M). The rows warn against exactly this base: "If either year was aberrational, any calculation of growth
will be distorted" **[L2005-003]**; a high return is read for "a cyclical peak in earnings" **[L1994-009]**; and Dexter
was bought by assuming "that the future would be as good as the past" **[M2003-077]**. So two ranges are shown. The
literal one obeys the convention. The treated one, which the run uses for every figure the owner asked for, replaces the
boom-contaminated five-year mean with two bases, each confessed:
- **Low base, the run rate, $105M:** the trailing-twelve-month earnings figure above (CONVENTION, ours: the latest
  twelve months as the low end; rationale: the business's own margin is now below its pre-boom level, so the trough is
  not behind it on the evidence of Q2).
- **High base, the pre-boom margin on today's sales, $219M:** owner cash averaged 7.67% of sales in FY2016 to FY2020;
  applied to FY2025 sales of $2,850M (CONVENTION, ours: a normal year is taken as the five years before the boom, at
  today's size; rationale: those are the only five consecutive years in the record without the windfall or its
  reversal). Shown growth for this end is the volume growth the filings show, about 1.8% a year (FY2021 to FY2025
  volume +5.0, -3.2, +3.2, +3.5, +0.7), for ten years, then zero, per the convention's specifics.

### C3. Value range, fair-price band and cheap price (all COMPUTATION)
Discount rate 5.63% (the US 30-year par yield, Treasury, 2026-10-02). Ten years at the stated growth, then zero nominal
growth. Shares 33.77M (the 10-Q cover; unvested awards, which the deal pays out, are not added).

| case | base ($M) | growth, years 1 to 10 | value a share |
|---|---|---|---|
| Literal convention, shown-growth end | 468.7 | -13.7% | $86 |
| Literal convention, no-growth end | 468.7 | 0% | $247 |
| Treated, low end (run rate, no growth) | 105 | 0% | **$55** |
| Treated, high end, no growth | 219 | 0% | $115 |
| Treated, high end, shown volume growth | 219 | 1.8% | **$133** |

- **Value range: $55 to $133 a share** (treated; 2.4 to 1), against $94.78. Read literally the convention gives $86 to
  $247 (2.9 to 1). Either way the price sits inside the range, which under the Q7 convention closes OUT, not a screamer
  **[M2009-005]**, **[M1996-084]**; the boom-treated range is the one the rows support **[L2005-003]**, **[M1998-016]**.
- **How pre-tax and after-tax were converted.** The floor is about 10% pre-tax (the Q7 CONVENTION, from **[M1994-004]**,
  **[L2002-020]**, **[M2003-149]**). Owner cash is after corporate tax, so the floor was converted to an after-tax yield by
  multiplying by one less the tax rate: 10% x (1 - 0.21) = 7.9% after tax, at the 21% US federal rate (Atkore's own
  effective rate was 19.5% in FY2024 and 18.4% in FY2025; at 25%, with state taxes, every price below rises about 5%).
  The 2002 letter made the same conversion at its own era's rate. Each price below is the present value, at 7.9%, of the
  base carried at the stated growth for ten years and then flat: the price at which the expected return is about 10%
  pre-tax.
- **Fair-price band: $55 to about $61**, widening to $69 if the shown volume growth is credited. These are the prices
  inside the range at which the expected return on the mid base ($162M, halfway between the run rate and the pre-boom
  normal) is at or above the floor. On the high base alone (the pre-boom margin fully back) the floor is met up to $82
  with no growth and $93 with growth; on the run-rate base, only up to $40 to $45. The price of $94.78 is above every one
  of these: it needs the pre-boom margin restored in full, volume growth for ten years, and nothing paid on the open DOJ
  investigation.
- **Cheap price: below about $40**, where the run-rate earnings alone, with no growth and no recovery of margin, give the
  floor; about 27% below the bottom of the range, the zone where "it ought to just kind of scream at you" **[M1996-084]**.
  Because the file closed at Q2, even this price would not reopen it: a castle shown open is not cured by a low price
  **[M2019-015]**.

### C4. Capital: what the added capital earned
FY2019 operating income $223.7M on about $955M of capital employed (equity $233M + long-term debt $845M - cash $123M).
FY2025: operating income before impairments $237.6M on about $1,648M ($1,398M + $757M - $507M); trailing twelve months
to June 2026, $135.9M on about $1,690M ($1,276M + $760M - $346M). About $700M of capital was added and the operating
income it supports is the same or lower: on the record, the incremental capital earned nothing. Acquisitions FY2017 to
FY2023 cost $720M (XBRL, payments to acquire businesses); impairments FY2025 to FY2026 $226M plus losses on sale.

### C5. Buybacks against the range, and the litigation tail
Shares bought (equity statements, 10-Ks FY2021 to FY2025): FY2021 2.33M for $135.1M (about $58); FY2022 5.08M for
$500.1M (about $98); FY2023 4.32M for $494.4M (about $114); FY2024 2.95M for $383.9M (about $130); FY2025 1.32M for
$100.6M (about $76); none in the nine months of FY2026. The programmes were stated in dollars ("up to $ 400 million",
"$ 800.0 million", "$ 500.0 million"), with no price named (10-K FY2025 equity note). About $1.38B of the $1.61B was
paid at average prices of $98 to $130: at the high base's no-growth value ($115) in FY2023, above it in FY2024, and
above the deal price throughout FY2022 to FY2024. Measured against the rule "Continuing shareholders are hurt unless
shares are purchased below intrinsic value" **[L2011-003]**, the purchases at the peak would weigh against at Q6; Q6 was
not reached and no verdict is given. Litigation: $186.5M of class settlements in FY2026 ($5.52 a share), the British
Columbia suit, the DOJ grand jury investigation, the securities class actions and the derivative suits remain open
(10-Q note 16); none is deducted in the range above, and each could only lower it.

### C6. What a purchase today actually is: the workout
The price is $94.78 against $95.00 cash, no financing condition, HSR expired, stockholder vote and Austrian, Australian
and Canadian approvals outstanding, an end date of 2027-08-03 (extendable twice by three months), a material-adverse-
effect condition, and dividends of up to $0.33 a quarter allowed while pending (8-K accession 0001666138-26-000016).
"The profit is limited." **[M2022-058]**: $0.22 a share, plus $0.33 for each quarterly dividend paid before closing.
The loss if the deal breaks, to the unaffected $72.96, is $21.82, and the business's own trend (C2) suggests the stock
would not stop there. At one dividend the completion probability needed to break even is 21.82 / (21.82 + 0.55), about
97.5%; with none, about 99.0%. The speakers weigh a workout by "whether a given corporate event occurs" **[M2022-057]**,
note that a buyer with the money "takes that one risk out of it" **[M2022-058]**, and do such commitments only as "one of
many mutually-independent commitments" **[L1993-024]**. Nothing in this framework's purchase questions values the
workout; it is recorded so that the owner sees that the business verdict (OUT at Q2) and the price on the screen
(bounded at $95.00 by contract) answer different questions.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written section by section as each closed (Step 0, then the
      foundations to Q1, then Q2 and the box, then the computation). **Not committed**: the dispatch forbade commits;
      write-early was kept, commit-after-each was not, by instruction.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, below); every filing fact carries its
      accession or names the filing whose accession is listed at Step 0; no number without a filing or a CONVENTION label.
- [x] The order was kept: the foundations, the standing rule, Q1 IN, Q2 OUT; nothing after Q2 is answered, and the
      computation is headed as operator rule 3 requires.
- [x] Owner cash after every real cost (stock pay and all capital spending deducted), never a net-income proxy; the
      sovereign from the Treasury curve; the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (five items under the foundations).
- [x] No point-in-time anchor applies (a run of today); no row is cited for a date after it.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 text, ids and floor were ignored.
- [x] `python tools/check_framework.py` PASS (2026-10-05, after the last edit); a separate script found no E-ids, every
      cited M/L/R id in the v5 ledger, and every quoted fragment set beside an id inside that row.
- [x] Blind rule kept: `PORTFOLIO.md`, the holding reviews, the resume state, the run queue, the prepped reading list and
      other runs of today were not opened; the contamination is declared at the top.
- Weak points, stated: the Q1 IN is a judgment that the spread is understood as a mechanism even though its level swung
  threefold; a stricter reader could close Q1 TOO HARD on test 2 **[M1998-044]**, but the insiders write the forecast
  down, so it would be WORK, and the Q2 evidence would then decide the research pass the same way. The competitor row
  lacks the steel-conduit peers (Zekelman is private; Nucor's conduit is not separable) and a separable Westlake pipe
  margin. No competitor, customer or distributor was interviewed.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **A boom inside the five-year window.** The Q7 convention fixes the base as the mean of the last five
years and the growth as the growth shown, but says nothing of a window that is mostly an aberration. Here the literal
base ($469M) is more than four times the run rate and more than twice the pre-boom normal, and the shown growth is
-13.7%, so the literal range ($86 to $247) is both too high and, at its low end, carried by a decline the convention then
treats as growth. The rows that govern (**[L2005-003]**, **[L1994-009]**, **[M1998-016]**, **[M2003-077]**) point one
way, but the convention names no procedure, so this run invented two (the run rate as the low base, the pre-boom margin
on today's sales as the high base) and confessed them; two analysts could pick different normal years. A specific is
needed: what replaces the five-year mean when the window holds a boom or a bust, and how the normal years are chosen.
(2) **The fair-price band and the cheap price are not framework terms.** The owner asked for them; the framework's Q7
gives a range, a floor and the screamer, but no defined band or cheap price, nor the pre-tax to after-tax conversion (the
2002 row converts at its era's tax rate and the convention is silent). The conversion used is stated in C3. (3) **A name
under a signed cash merger.** The framework has no instruction for a purchase run on a stock whose price is bounded by
contract; the business questions and the workout answer different questions, and the template has no place for the
second. It was carried in the foundations and in C6, as computation. (4) **Q1 test 2 against the routing rule.** Test 2
says "If something is not very predictable, forget it" **[M1998-044]**, while the routing sends only fast-changing
industries to TOO HARD at Q1. A slow-changing industry whose key variable (the spread) is volatile but understood falls
between them; this run read it as IN at Q1 and decided it at Q2, and says so, but another analyst could close it at Q1.


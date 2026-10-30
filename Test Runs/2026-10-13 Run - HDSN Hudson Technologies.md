# Company Run — Hudson Technologies, Inc. (NASDAQ: HDSN) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch** (commit
`aa6610f9`, before the first EDGAR request).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (HDSN, Hudson Technologies); not held.*

**Dispatch:** a dispatched blind run under the brief of 2026-10-13, whose one stated departure from
`Screens/_daily/_dispatch_brief.md` is that the lines of evidence are derived by the analyst from the latest 10-K's Item 1,
Item 1A and Item 7 (below, "The lines of evidence"). Working folder `Test Runs/_research 2026-10-13 HDSN/`.

**Contamination, declared:** nothing about this company from any other run file, holding review, `PORTFOLIO.md`, the
register or the reading list was opened, listed or searched. Seen by accident and not used: the session's opening git
status and recent commit subjects (another company's run, HRIBF, and untracked research files of AYI and ARCB); the
memory index lines loaded with the session (queue counts and dates, no ticker of this company); one command that counted
the entries of `Test Runs/` without printing a name. None of it bears on HDSN.

**The lines of evidence, derived from the FY2025 10-K (Items 1, 1A, 7; accession 0001104659-26-028445), and why:**
1. *Refrigerant prices and the HFC phasedown.* Item 1A's first risk is "changes in commodity prices" of refrigerant gases;
   Item 1 ties supply to the AIM Act's allowance step-downs (40% cut 2024-2029) and to EPA rules, one of them (the
   Technology Transition rule) "reconsider[ed]" in 2025. The economics turn on this line, so the ten-year record of price
   effects is read from every 10-K FY2018 to FY2025.
2. *Regulatory dependence.* Item 1A: "Our business and prospects are largely dependent upon continued regulation of the
   use and disposition of refrigerants." Read: the AIM Act and Refrigerant Management Rule text in Item 1; the FY2018 10-K
   on the 2018 price collapse.
3. *Inventory and working capital.* Item 7: inventory $135.9M at 2025 year-end against revenue $246.6M; Item 1A on
   lower-of-cost write-downs. Read: ten balance sheets, the cash-flow working-capital lines, the 2018 write-down.
4. *Competition on price.* Item 1, Competition: Hudson competes on equipment, breadth of service "and price, particularly
   with respect to refrigerant sales", against "numerous regional and national companies". Read for Q2.
5. *Customer concentration (DLA).* Item 1A: the DLA was 15%, 15% and 18% of revenue 2025, 2024, 2023; contract protested
   and rebid. Read: 8-Ks of 2025-10-22, 2026-01-30, 2026-05-28, 2026-08-06.
6. *Debt and liquidity.* Item 1A on the Wells Fargo asset-based facility (expires 2027-03-02); the FY2018-FY2020 10-Ks
   on the covenant waivers after the 2017 acquisition. Read for Q4 and Q9.
7. *Management change.* 8-Ks of 2025-11-03, 2025-11-13, 2025-12-09, 2026-03-18; the proxy. Read for Q5 and Q6.

**Competitors (the brief's rule):** the FY2025 10-K names no competitor. Item 1 speaks of "numerous regional and national
companies that market reclaimed and virgin refrigerants and provide refrigerant reclamation services" and Item 1A of
competitors "including certain of our suppliers"; no name appears in Items 1, 1A or 7 of the FY2021 to FY2025 10-Ks
(text search for competitor, Chemours, Honeywell, A-Gas, Airgas, Arkema, Koura, Combs). **No named rival, so no rival
filing could be taken; flagged.** The only rival the filings mention is the unnamed bidder who protested the DLA award.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $5.12 (close 2026-10-12; `tools/run.py`'s aggregator quote, flagged per operator rule 5, live quote only).
- **Shares by class:** one class, common, **42,088,547** as of 2026-07-27, from the cover of the 10-Q for the quarter
  ended 2026-06-30, filed 2026-08-07, accession `0001104659-26-092682` (`python Screens/cover_shares.py HDSN`). Checked
  against the balance sheet of the same 10-Q: "issued and outstanding: 42,088,547 and 41,647,221, respectively"
  (2026-06-30 and 2025-12-31); there is no treasury stock (repurchased shares are retired: paid-in capital fell from
  $91.7M to $86.3M over the half). No 8-K, prospectus or shelf takedown was filed after the 10-Q (EDGAR submissions list,
  read 2026-10-13: the 10-Q of 2026-08-07 is the latest filing). Beside it: 3,039,889 options outstanding at 2025-12-31
  at a weighted average exercise price of $4.28 (FY2025 10-K, Note on stock options), about 7% of the share count and in
  the money at $5.12; shares rose 441,326 in the first half of 2026 although 416,480 were repurchased.
- **Market cap:** 42.0885M x $5.12 = **$215.5M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, US Treasury daily par yield curve, 30-year, 2026-10-09
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-03-16, `0001104659-26-028445` (Items 1, 1A, 7, 7A,
  the statements and notes); 10-Q Q2 2026, filed 2026-08-07, `0001104659-26-092682` (MD&A, balance sheet); 10-Q Q1 2026,
  `0001104659-26-058632` (fetched); proxy DEF 14A filed 2026-04-24, `0001104659-26-048223`; 8-Ks
  `0001104659-25-101581`, `-25-105559` (with its Exhibit 99.1), `-25-111455`, `-25-117162`, `-25-119656`, `-25-122053`,
  `0001104659-26-008337`, `-26-009003`, `-26-023461` (Ex. 99.1), `-26-030906`, `-26-042384`, `-26-063042`, `-26-064492`,
  `-26-067511`, `-26-073424`, `-26-091092` (Ex. 99.1), `-26-091361`; for the span, the 10-Ks FY2024
  `0001410578-25-000323`, FY2023 `0001410578-24-000199`, FY2022 `0001410578-23-000263`, FY2021 `0001410578-22-000491`,
  FY2020 `0001104659-21-035666`, FY2019 `0001104659-20-033130`, FY2018 `0001144204-19-014301`.
  **One figure cross-checked against the filed statement:** FY2025 net cash from operations, tagged -$3.16M, is the cash
  flow statement's figure and the MD&A's "Net cash used in operating activities for the year ended December 31, 2025 was
  $3.2 million"; inventory $135,923 thousand tagged equals the MD&A's "$135.9 million".
- **`python tools/run.py HDSN`, arithmetic lines only** (its rule lines, ids and floor not used; Part VII): owner cash
  (operating cash less stock pay less capital spending) FY2023 $52.7M, FY2024 $85.7M, FY2025 -$9.3M; the five-year
  window FY2021-25 averages $36.7M on capex, $35.1M on depreciation. Checked line by line against the FY2025 cash flow
  statement: depreciation $2,695K and amortization of intangibles $3,296K (the tool's "D&A" for 2025 is the
  amortization line; depreciation of plant is $2.7M); stock pay $1,100K; capital spending $5.05M (investing cash of $7.3M less acquisitions of $2.24M, as the MD&A states); acquisitions $2.24M
  (2025) and $20.67M (2024) sit outside its owner-cash line and are deducted below. Owner cash by year, all ten years,
  is in `Test Runs/_research 2026-10-13 HDSN/owner_cash.py`:

| FY | operating cash | stock pay | capex | acquisitions | owner cash after acquisitions | operating cash / sales |
|---|---|---|---|---|---|---|
| 2016 | 9.35 | 0.71 | 1.73 | 0 | 6.91 | 6.6% |
| 2017 | 18.37 | 1.50 | 1.02 | 208.97 (Airgas-Refrigerants, "ARI") | -193.12 | 11.3% |
| 2018 | 36.33 | 1.40 | 1.09 | 0 | 33.84 | 20.3% |
| 2019 | 33.82 | 1.83 | 1.01 | 0 | 30.98 | 19.1% |
| 2020 | 11.69 | 0.66 | 1.47 | 0 | 9.56 | 6.5% |
| 2021 | -1.23 | 0.51 | 1.92 | 0 | -3.66 | -1.9% |
| 2022 | 62.81 | 0.92 | 3.66 | 0 | 58.23 | 17.9% |
| 2023 | 58.55 | 2.31 | 3.58 | 0 | 52.66 | 18.2% |
| 2024 | 91.81 | 0.84 | 5.30 | 20.67 (USA Refrigerants) | 65.00 | 36.1% |
| 2025 | -3.16 | 1.10 | 5.05 | 2.24 (Refrigerants Inc.) | -11.55 | -3.8% |

  USD millions, from the XBRL cash-flow lines of the 10-Ks named above (transcription), the last three years checked
  against the FY2025 statement. Five-year average FY2021-25: **$32.1M** after acquisitions (equity-only, after interest);
  $36.7M before acquisitions. Ten-year average FY2016-25 after acquisitions: **$4.9M**. The operating-cash swings are
  inventory: the cash flow statement shows inventories releasing $60.2M of cash in 2024 and absorbing $40.9M in 2025.

## THE FOUNDATIONS (not a gate)
Three bear on this name. **A share is a business:** "Would I be happy buying this stock if the market closed for five
years?" **[M1997-109]**; for a business whose ten-year record runs from a $55.7M loss (FY2018) to $103.8M of profit
(FY2022) on the price of a gas, the honest answer depends on knowing where that price and its regulator will be, which is
the question the run must face. **The market serves:** the quotation "just tells us prices" **[M2006-077]**; at $5.12 the
price has fallen with the HFC market and tells nothing about the business by itself. **No macro enters:** "macro
conclusions are — just never enter into the discussion" **[M2000-094]**; the HFC price and the EPA's course are not
forecast here; where the run needs them, it says it cannot have them. **The analyst's habits:** look for "what’s wrong in
things" **[M2025-013]**; and the anchor to avoid "is always your previous conclusion" **[M2016-054]**: a price that looks
cheap on five-year owner cash is exactly the anchor the run must not carry into Q1 and Q2.
**Contrary evidence, written down as found** **[M1997-127]**:
1. The ten-year record contains a near-failure: the October 2017 purchase of ARI for $208.97M, financed with $105M of term
   debt and $65M of revolver (FY2017 cash flow), was followed by a $35.9M inventory write-down in 2018 "due to a price
   correction" and "a challenging pricing environment affecting the industry" (FY2018 10-K, `0001144204-19-014301`),
   four waivers and amendments of the term loan's leverage covenant in 2018-2019 (FY2019 10-K, `0001104659-20-033130`),
   and Nasdaq notices that the stock had closed below the $1.00 minimum bid (8-Ks under Item 3.01 of 2019-08-02,
   2020-01-30, 2020-04-20; `0001144204-19-037455`, `0001104659-20-008674`, `0001104659-20-048702`). Equity fell from $123.5M (2017) to
   $40.6M (2020).
2. With that acquisition deducted, ten years of owner cash average $4.9M a year; the five-year average of $32.1M exists
   only because the window begins after it.
3. The filer competes on "price, particularly with respect to refrigerant sales" (FY2025 10-K, Item 1).
4. The chief executive and chairman (employment agreements with him filed back through the 10-K exhibit list) left "without Cause" on 2025-11-03 with severance (proxy, `0001104659-26-048223`); the
   senior vice president of sales, a director, resigned 2026-03-13 (8-K `0001104659-26-030906`).
5. In August 2026 the company cut its own full-year gross-margin "target" and described "a continued trough in HFC market
   prices" (Exhibit 99.1 of 8-K `0001104659-26-091092`).
6. For the business: reclaimed refrigerant "is not subject to the allowance system" while virgin HFC supply is cut by law,
   and the 2024 Refrigerant Management Rule mandates "the use of reclaimed HFCs for certain applications" (FY2025 10-K,
   Item 1); volume rose 12% in Q2 2026 and 17% in the half (the same Exhibit 99.1); no debt at 2026-06-30.

## THE STANDING RULE
Owning a part-interest of this size, bought without borrowed money, puts no buyer at risk of ruin; the rule binds the
buyer's financing and sizing, "Never risk permanent loss of capital." **[L2023-005]**, "borrowed money has no place in
the investor's tool kit" **[L2014-005]**. Nothing in a run decides those; the run notes that the target itself once came
near its lenders' switch (contrary evidence 1), which is weighed at Q9 if reached, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from the filings.** Hudson buys used refrigerant from contractors and owners, cleans it to the
  AHRI 700 purity standard in its plants (it holds "two of only four certified refrigerant testing laboratories in the
  United States" under AHRI's program), and resells it; it also buys virgin HFC and HFO refrigerants "from several
  suppliers, which are then resold"; it runs the DLA's refrigerant and gas supply contract; and it sells on-site
  RefrigerantSide services (FY2025 10-K, Item 1, `0001104659-26-028445`). One reportable segment. The MD&A explains each
  year's revenue as pounds sold times price per pound (FY2018 10-K: 2018 revenue fell "$33 million" on "selling price per
  pound" and "$9 million" on pounds; FY2025 10-K: higher volume "partially offset by lower average selling prices").
- **The key variables and whether they are foreseeable**, the first step being "trying to identify the key variables in
  that particular business, and evaluating how predictable they were" **[M1998-044]**: (1) *pounds sold*: tied to the installed base
  of HFC equipment that must be serviced through its life, while the AIM Act cuts virgin HFC supply by statute (40% below
  baseline 2024-2029, with further step-downs) and "Reclamation is not subject to the allowance system or restricted from
  use"; the 2024 Refrigerant Management Rule mandates "the use of reclaimed HFCs for certain applications" (Item 1). The
  direction of this variable can be seen. (2) *price per pound*: set by the refrigerant market, "affected by a wide range
  of factors beyond our control, including weather, seasonality, the availability and adequacy of supply, government
  regulation and policies" (Item 1A); its record is a fall in 2018 that cost $35.9M of inventory write-downs, a spike in
  2022 (gross margin 50%), and "a continued trough in HFC market prices" in 2026. Not foreseeable, and the filer says so.
  (3) *the regulator*: "Our business and prospects are largely dependent upon continued regulation" (Item 1A); the
  Technology Transition rule was proposed for reconsideration in 2025 with a final rule "expected in third quarter of
  2026" (Item 1). Not foreseeable.
- **The routing the framework fixes for this case.** "A dependence on a commodity price is never by itself a STOP at Q1
  or Q2": the speakers "don’t think we can predict commodity prices" **[M2016-025]** and still decide "off the figures"
  **[M2008-069]**; Q1 asks whether the business can be understood from its figures, and the price level enters at Q7
  (Q2, A commodity business). Read that way, the economic dynamics are plain: what matters "is that I understand the
  economic dynamics of the industry. Is there — are there competitive moats? Is there ease of entry?" **[M2011-014]**,
  and those are the questions Q2 must answer. The product changes slowly (HFC to HFO equipment, both reclaimable; patents
  and process, not fast-moving technology), so the fast-change routing to TOO HARD at Q1 does not apply; slow change is
  still change and is carried to Q2 **[M2014-038]**.
- **What I cannot do, recorded as contrary evidence** **[M1997-127]**: understanding is "a reasonable fix on about what
  the earning power and competitive position will look like in five or 10 years" **[M2012-065]**, and the earning power
  of this business has ranged from a $42.6M operating loss (FY2018) to $131.5M of operating profit (FY2022) on the price of
  a gas and the course of a regulator. I do not have a fix on the earning power. By the commodity routing, that doubt is
  about the price, which belongs to Q7, and about the castle and the regulator, which belong to Q2; it is not a doubt
  about what the business does or how its figures behave. "if you have doubts about something being into your circle of
  competence, it isn’t" **[M2002-092]** is weighed against that routing and does not overrule it here, because the doubt
  is about a forecast the framework places later, not about the circle; a later run that reads the routing the other way
  would close here TOO HARD (NATURE), and the question is named below.
- **VERDICT: IN**, by the commodity routing (Q2, A commodity business, **[M2016-025]**, **[M2008-069]**, **[M2011-014]**),
  with the earning-power doubt **[M2012-065]** carried to Q2 and Q7. Filing fact: one segment whose revenue is pounds
  times price, reported so in every MD&A FY2018 to FY2025.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**. A moat is what "protects excellent returns on invested capital"
**[L2007-004]**. Hudson sells a gas whose purity is fixed by a public standard: "reclaimed refrigerant must satisfy the
same purity standards as newly manufactured, virgin refrigerants" (FY2025 10-K, Item 1). The product is standard and
available from many suppliers, which is how the rows define the commodity: "Policy forms are standard, and the product
is available from many suppliers" and "most insureds don't care from whom they buy" **[L2004-003]**. So the governing
paragraph is Q2's "A commodity business": the castle, if there is one, is the low-cost position, read from the filer's
own and its operators' filings: "more by cost of production than we would by whether copper was selling for $2.00 a
pound or a dollar a pound" **[M2006-004]**; "The figures are available." **[M2009-059]**.

**The castle tests, each with its filing fact:**
1. *What keeps it standing, how permanent.* What the filings name: scale ("one of the largest refrigerant reclaimers in
   the United States", Item 1), two of the four AHRI-certified labs, proprietary high-speed equipment and process patents
   that "will expire between August 2026 and December 2036" (Item 1), the DLA prime contract since 2016, and supply
   relationships (Lennox, exclusive supplier of certified reclaimed refrigerant for its residential aftermarket, 2022;
   Item 1). None is shown to make a customer pay more; the patents are expiring; the DLA contract was won, protested by "a
   competitor", rescinded, rebid and re-awarded on 2026-08-04 (10-Q Q2 2026, `0001104659-26-092682`), which is a
   contract held by bidding, not a castle.
2. *Without the lord.* The business ran through the chief executive's departure in November 2025; nothing in the
   filings ties the economics to one person. Not the deciding test here.
3. *The money test* **[M2011-015]**. Could an attacker with money take it on? The filer says it competes with "numerous
   regional and national companies", some with "greater financial, marketing, distribution and other resources", and
   with "certain of our suppliers" (Items 1, 1A). Hudson itself bought more reclamation and distribution for small sums:
   USA Refrigerants for $20.67M (2024), Refrigerants Inc. for $2.24M plus up to $2.0M contingent (2025). That reclaimers
   can be bought this cheaply is evidence that the capacity can be assembled; it is not evidence that Hudson's position
   can be taken, since no rival's cost or share is on any filing read.
4. *Pricing power and the agony before a rise* **[M2005-020]**. No pricing power is shown. The price is the market's:
   2018 revenue fell $33M on "selling price per pound" (FY2018 10-K); 2025 "lower average selling prices for certain
   refrigerants" (FY2025 10-K); Q2 2026 "Pricing -6%" against "Sales Volume +12%" (Ex. 99.1, `0001104659-26-091092`).
   The filer competes on "price, particularly with respect to refrigerant sales" (Item 1). When the market falls, Hudson's
   price falls with it, as at the gas station where "whatever he charged for gas was my price" **[M2012-109]**.
5. *Unit volume.* For: pounds rose 12% in Q2 2026 and 17% in the half, trailing-twelve-month volume "up double-digits"
   (same exhibit), in a falling price market.
6. *The low-cost position* **[M1997-010]**, **[L2000-017]**. Not readable. The filer states no cost per pound and no
   comparison; no rival is named; the rivals the filer describes (regional and national reclaimers and distributors, and
   its own suppliers) are not identified in any filing read, so no rival's cost can be read. Gross margin, the only proxy
   on the filer's side, follows the market price (test 10), not a cost edge.
7. *The brand.* "EMERALD Refrigerants" is a trade name on a product sold to a public purity standard; no filing shows a
   customer asking for it by name or paying more for it.
8. *Would the customer still choose it over the low bid?* **[M2017-009]**. The customers are "commercial, industrial and
   governmental customers, as well as [...] refrigerant wholesalers, distributors, contractors", with "standardized
   pricing" for larger customers and no backlog (Item 1); the DLA buys by competitive bid. The filings show buying on
   price.
9. *Ask the competitors.* Not possible from the record; the one rival on the record is the unnamed DLA protester.
10. *Widening or narrowing.* The margin follows the gas price, not a moat. Gross margin FY2016 to FY2025, from the
    10-Ks: 29.5%, 27.1%, -4.4%, 10.6%, 24.0%, 37.2%, 50.1%, 38.6%, 27.7%, 25.2%; 23% in the first half of 2026. SG&A rose
    from $26.6M (2021) to $40.2M (2025), with $4.0M of severance in 2025.
11. *What could destroy, modify or reduce it* **[M2000-014]**. The filer names it: "significant relaxation of regulatory
    requirements could also adversely affect demand for and supply of our services and products" (Item 1A); the
    Technology Transition rule is being reconsidered (Item 1). The 2018 collapse shows what a fall in the price does to
    this business with inventory on hand: a $35.9M write-down "due to a price correction" (FY2018 10-K). The rows record
    the same shape of loss where a regulator turned: "it is difficult to project both earnings and asset values"
    **[L2023-011]**; and "railroads, utilities, insurance companies, are all very much affected by the political process"
    **[M2012-074]**.

**The competitor row:** none. The 10-K names no rival (Step 0); no comparison of the same metric could be made from a
rival's own filing. Flagged as the brief requires.

**The parts table:** not applicable. One reportable segment; the DLA business (revenue $38.2M in 2025, 15%) is not
reported as a part with its own profit.

**The field's returns over the last full cycle** (the filer's own filings only; no rival filing to read). Pre-tax
operating income on capital employed (equity plus borrowings less cash, at year-end), USD millions, from the 10-Ks named
in Step 0 (borrowings: the tagged long-term debt, current and noncurrent, and short-term revolver borrowings):

| FY | operating income | capital employed | return |
|---|---|---|---|
| 2016 | 18.95 | 78.5 | 24% |
| 2017 | 15.13 | 285.9 (after ARI) | 5% |
| 2018 | -42.61 | 196.8 | -22% |
| 2019 | -15.78 | 141.5 | -11% |
| 2020 | 5.90 | 129.1 | 5% |
| 2021 | 42.30 | 160.8 | 26% |
| 2022 | 131.51 | 212.8 | 62% |
| 2023 | 78.17 | 216.3 | 36% |
| 2024 | 29.30 | 175.7 | 17% |
| 2025 | 18.56 | 203.9 | 9% |

Ten-year average: about 15% pre-tax on about $192M of capital; owner cash after acquisitions averaged $4.9M a year over
the same ten years (Step 0). In words: the returns are set year by year by the price of the gas: losses in the two years
after the 2017 purchase, a peak in the first years of the AIM Act allowances (2022-2023), and a return toward single
digits by 2025 as "HFC market prices" troughed. The word ordinary carries no figure and is judged in words, as the moat is: "there’s no formula that gives you that
precisely" **[M1999-108]**. On these figures the field can be called neither ordinary nor excellent, because the swing is the finding, so the "standing
castle that protects only ordinary returns" OUT is not shown either.

**The change for the better.** The AIM Act (enacted December 2020; allowance cuts from 2022) changed the field, and the
2021-2023 figures show the change as better. The framework credits such a change only on a full cycle in which the price
held (Q2, Change, and what it does to a castle), from the row that "you learn a lot about the durability of the economics
of a business by observing the behavior of — the price behavior" **[M2005-020]**. The first downturn since the change is under way
(FY2024 to H1 2026): volume held and rose; price did not hold ("Pricing -6%", "a continued trough in HFC market
prices"). The change is not credited, and the question waits on a cycle; "the railroads were a terrible business for
decades and decades and decades and then they got good" **[M2017-026]**, but only the years showed it.

**Contrary evidence for the castle, written down** **[M1997-127]**: reclaimed supply sits outside the allowance system
while virgin supply is cut by law; the 2024 rule mandates reclaimed HFC for some uses; Hudson is among the largest
reclaimers and gained volume through the downturn; it earned money in every year since 2021, the trough included; and
the rows allow that "If a thing is cheap enough, obviously you can afford a little more country risk, or regulatory risk,
or whatever." **[M2004-083]**. Against the last: a castle whose future cannot be judged goes to the "too hard" box, which
a lower price does not reopen, "It doesn’t mean it isn’t selling for a fraction of its worth. It just means that we don’t
know how to evaluate it." **[M2000-038]**; the price enters only at Q7.

**What decides.** The commodity paragraph: a high-cost producer in a commodity field is OUT; where the cost position
cannot be read because the operators' reports were not read, TOO HARD (WORK); where no filing states it, TOO HARD
(NATURE). No filing states Hudson's cost position against its rivals: the filer gives none and names no rival, and the
reclaimers it describes are not identified in any filing read, so there is no operators' report left unread whose reading
would answer it. Beside it, the second deciding question, whether the regulated scarcity that lifted the field's returns
after 2021 will hold for ten years, is a forecast of a regulator's course that the filer itself declines to make ("future
trends are difficult to predict", Item 1A) and that the field's insiders "would not want to put down on paper"
**[M2000-105]**: "We couldn't solve this problem, moreover, even if we were to spend years intensely studying those
industries." **[L1993-023]**. The castle is not shown open on the evidence (the low-cost test cannot be read, and volume
held), so OUT is not the box; its future cannot be judged: "We don’t know how to valuate that, and therefore we leave it
alone." **[M2000-019]**.

- **VERDICT: TOO HARD (NATURE)**, the "too hard" box of "in, out, and too hard" **[M2006-013]**, by **[M2000-019]** and
  **[L1993-023]**: a commodity seller whose cost position no filing states, in a field whose returns are set by a
  regulated scarcity whose ten-year course nobody inside it will write down; the change for the better is not credited
  until a full cycle in which the price holds. **Re-look condition** (Q2, Change, and what it does to a castle): the first
  fiscal year in which Hudson's reported refrigerant volume, or the field's volume, falls, read from the 10-K; then Q2 is
  put again.

## Q3 to Q12: NOT REACHED
The STOP at Q2 closed the file (operator rule 2). Facts already found are under AFTER THE STOP, below, written down and
not weighed; every figure there is a COMPUTATION, NOT A CLEARANCE.

---
## THE BOX
**TOO HARD (NATURE) at Q2**: a seller of a commodity gas whose cost position no filing states (no rival named in the
10-K), in a field whose returns are set by HFC prices and a regulated scarcity whose ten-year course nobody inside it
will write down; the change for the better is not credited until a full cycle in which the price holds. **Re-look
condition:** the first fiscal year in which Hudson's reported refrigerant volume, or the field's volume, falls (10-K);
then Q2 is put again. A lower price does not reopen the box **[M2000-038]**. **Integrity facts recorded, not judged**
(the gross-margin target and its revision; the chief executive's termination without cause; see AFTER THE STOP, Q5).
For the operator's figures, COMPUTATION, NOT A CLEARANCE: value range **$8.67 to $19.14** a share (all-equity, cycle
base) against **$5.12**; fair price **$8.40** all-equity, **$9.54** equity-only.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(The file closed at Q2. Facts already found that bear on later questions, each with its source **[M1997-127]**;
written down, not weighed; no verdict; the box unchanged, operator rule 2.)*

### Bearing on Q3 (capital in, earnings out)
- Capital employed (equity plus borrowings less cash) ran $78.5M (2016) to $285.9M (2017, after ARI) and back to $203.9M
  (2025); the business's capital is mostly inventory: $135.9M of $318.6M of assets at 2025-12-31 (FY2025 10-K).
  Property, plant and equipment net $23.6M. Capital spending $3.6-5.3M a year since 2022 against depreciation of $2.7-3.0M;
  the 2025-26 excess includes a capitalized ERP system and plant capacity (10-Q Q2 2026 MD&A; Ex. 99.1 of
  `0001104659-26-091092`). Return table: Q2 above.

### Bearing on Q4 (the accounts). The balance sheets first, ten year-ends **[M2025-032]**
USD thousands, from `tools/run.py`'s ten-year table (first-filed XBRL, transcription) and the filed statements named in
Step 0; borrowings add the tagged short-term revolver borrowings to the long-term lines.

| year-end | assets | equity | cash | receivables | inventory | goodwill | intangibles | borrowings | retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2017 | 321,444 | 123,453 | 5,002 | 14,831 | 172,485 | 49,464 | 32,419 | about 167,400 | 8,727 |
| 2018 | 228,341 | 69,213 | 2,272 | 14,065 | 101,962 | 47,803 | 29,451 | about 129,900 | -46,932 |
| 2019 | 180,153 | 45,111 | 2,600 | 8,061 | 59,238 | 47,803 | 26,012 | about 99,000 | -72,872 |
| 2020 | 161,649 | 40,622 | 1,348 | 9,806 | 44,460 | 47,803 | 23,150 | about 89,800 | -78,080 |
| 2021 | 215,715 | 70,939 | 3,492 | 14,223 | 94,144 | 47,803 | 20,357 | about 93,400 | -45,821 |
| 2022 | 272,493 | 174,875 | 5,295 | 20,872 | 145,377 | 47,803 | 17,564 | 43,235 | 57,980 |
| 2023 | 296,672 | 228,773 | 12,446 | 25,169 | 154,450 | 47,803 | 14,771 | 0 | 110,227 |
| 2024 | 302,652 | 245,850 | 70,134 | 13,629 | 96,247 | 62,280 | 14,100 | 0 | 134,615 |
| 2025 | 318,648 | 243,390 | 39,456 | 17,098 | 135,923 | 65,282 | 11,294 | 0 | 151,282 |

The FY2016 year-end (FY2017 10-K comparatives): equity $112.0M after a $51.1M share sale in 2016, cash $33.9M, inventory
$68.6M, almost no debt.
What the figures say: **(1)** inventory is the business. It ran 65% of sales (2016), 123% (2017, after ARI's $103.9M of
inventory was bought at a stepped-up value), 30% (2020), 53% (2023), 41% (2024), 55% (2025). Its value is the gas price:
the 2018 write-down of $35.9M "included a $17.6 million write-down of a previously recorded step-up in inventory basis
associated with the acquisition of ARI and an $18.3 million write-down for a lower of cost or net realizable value
adjustment" (FY2018 10-K). Smaller write-downs recur: $3.0M (2024), $1.7M (2025), a $2.3M reversal (2023) (FY2025 cash
flow statement). **(2)** Equity was nearly erased and rebuilt: $123.5M (2017) to $40.6M (2020), retained earnings from
+$8.7M to -$78.1M, then +$151.3M (2025). **(3)** The debt came with the acquisition and left with the boom: about
$167M at 2017 year-end, covenant waivers in 2018-2019, refinanced in December 2019 and March 2022, nil since 2023 (FY2019,
FY2022 and FY2025 10-Ks). **(4)** Goodwill and intangibles, $76.6M at 2025 (31% of equity), rose with the 2024 and 2025
purchases. **(5)** Receivables track sales and season (5-11% of sales at year-end over FY2017-25; $43.3M at 2026-06-30 "mainly due to
seasonal timing", 10-Q). **(6)** Prepaid and other assets absorbed $3.4M, $1.1M and $3.2M of cash in 2025, 2024, 2023
(cash flow statement); no build out of line with sales was found in the lines read. What the figures cannot say: what the
inventory will fetch, which is the gas price.
- *The real costs:* stock pay is small ($0.5-2.3M a year); depreciation $2.7-3.0M against capital spending above it since
  2022; amortization of purchased intangibles $3.3M (2025), from acquired customer relationships; inventory write-downs
  recur and are in cost of sales; 2025 SG&A carried $4.0M of severance; 2025 other income includes a $1.6M gain from
  reversing an earn-out liability (FY2025 10-K, Item 7). Taxes: a valuation allowance of about $11.3M was set up in 2018
  (FY2018 10-K); cash taxes paid were $15.5M, $18.5M, $9.0M, $5.8M in 2022-2025.
- *EBITDA in the filer's mouth:* only in the credit agreement's fixed-charge ratio (Item 7). The three earnings releases
  read (Ex. 99.1 of `0001104659-25-105559`, `0001104659-26-023461`, `0001104659-26-091092`) feature no adjusted earnings
  or EBITDA figure (text search). *Guidance:* the August 2026 release revises "its previously announced full year 2026
  gross margin target from mid-twenty percent to low-to-mid-twenty percent"; the FY2025 release forecast first-quarter ERP
  inefficiencies. Carried to Q5 as the gaps case directs; not weighed here.

### Bearing on Q5 (who runs it). Integrity facts recorded, not judged
- Brian F. Coleman stepped down as chairman, president and chief executive "effective immediately" on 2025-11-03 (8-K
  `0001104659-25-105559`); the proxy records termination "without Cause", severance of base salary ($695,000 a year) for
  24 months plus other amounts, $494,778 paid in 2025 (DEF 14A `0001104659-26-048223`); he left the board on 2025-12-09
  "not the result of any disagreement" (8-K `0001104659-25-119656`). Kenneth Gaglione, a former Hudson vice president of
  operations (2020-2023) and earlier a Honeywell refrigerants marketing director, became chairman, president and chief
  executive on 2025-11-24 at $695,000 salary and a 75% target bonus (8-K `0001104659-25-111455`). The senior vice
  president of sales, a director, resigned 2026-03-13 (8-K `0001104659-26-030906`); two directors were added 2026-04-10,
  one a former SPAC sponsor (8-K `0001104659-26-042384`). Officers and directors own about 3.1% (FY2025 10-K, Item 1A).
  Insiders bought shares in May 2026 (8-K `0001104659-26-063042`, press release not read).
- The gross-margin target and its revision (above). The 2025 options to executives vest in part on earnings-per-share growth
  of 8% (proxy).

### Bearing on Q6 (the money and the owners)
- **Buybacks:** 1,244,076 shares for $8.1M in 2024 (about $6.55 a share), 2,890,240 for $20.0M in 2025 (about $6.92),
  416,480 for $2.5M in the first half of 2026 (about $6.00) (FY2025 10-K, Item 7; 10-Q Q2 2026). The programme names no
  price: the timing "will depend on a variety of factors, including stock price, trading volume, market conditions" (8-K
  `0001104659-25-117162`). The framework's test reads the prices paid against the bottom of the Q7 range; that range is a
  COMPUTATION here (bottom $8.67 all-equity, $7.22 on the literal window), and the prices paid sit below it; not weighed,
  since Q7 was not reached. Option exercises added back more shares than the 2026 buyback removed.
- **Deals:** all paid in cash: ARI $208.97M (2017, with $105M term loan and revolver borrowing), USA Refrigerants $20.67M
  (2024), Refrigerants Inc. $2.24M plus up to $2.0M contingent (2025). No deal paid in shares. Net purchases over FY2021-25
  ($22.9M) are under half of owner cash before purchases, so the serial-acquirer convention does not apply.
- **Dividends:** none; the credit agreement limits them (Item 7).

### Bearing on Q7: COMPUTATION, NOT A CLEARANCE
*(No figure here is a clearance or entry language, operator rule 3. Script and output:
`Test Runs/_research 2026-10-13 HDSN/q7_computation.py`, `q7_computation_output.txt`.)*
- **Cash input:** all-equity owner cash (operating cash less stock pay less all capital spending less acquisitions, plus
  interest paid after tax, less net interest income after tax), USD millions: 2021 4.37, 2022 67.47, 2023 56.19, 2024
  64.62, 2025 -13.55. Working capital counted (in operating cash). Tax: the company's own; 2021-2025 interest at 21%.
- **(a) Cycle base.** The last year, FY2025, is a trough on the filer's own description ("lower average selling prices";
  in 2026 "a continued trough in HFC market prices"), and the owner-cash series has troughs at FY2021 and FY2025. Cycle
  base: FY2022-FY2025, the full owner-cash cycle ending at the latest trough, **$43.7M**. Literal window FY2021-25 beside:
  **$35.8M**. The FY2016-FY2020 cycle, which contains the ARI purchase, averaged negative after acquisitions, so growth
  between cycles is meaningless.
- **(b) Decline.** Growth between the window's halves (FY2021-22 average $35.9M to FY2024-25 average $25.5M, three years
  apart): **-10.8% a year**, negative, so it is the bottom of the range and the no-growth case is the top.
- **(c) Acquisitions** deducted and the total growth credited (the default pair); the filer reports no organic growth
  figure, so no organic pair is shown. No merger; no signed unclosed deal; no serial acquirer.
- **(d) Working capital** counted. The FY2024 inventory release ($60.2M) and FY2025 build ($40.9M) offset inside the base.
- **(e) Growth spending.** The filing gives no maintenance figure; the central case charges all capital spending.
  Maintenance at depreciation would add about $1.6M a year (FY2022-25 capex $4.4M against depreciation $2.8M on average).
- **(f) The cap.** Not engaged: the growth carried is negative.
- **Rate:** 5.60% (UST 30-year, 2026-10-09); ten years, then zero nominal growth.
- **Net debt** at 2026-06-30: no borrowings, cash $25.6M, net debt **-$25.6M** (10-Q); operating leases left out ($2.7M
  long-term). The June 2026 storm costs are stated as "expected to be covered through insurance" (Ex. 99.1 of
  `0001104659-26-091092`); nothing added.
- **Value range (all-equity, central):** whole business $339.1M (decline) to $780.0M (no growth), plus $25.6M net cash,
  over 42,088,547 shares: **$8.67 to $19.14 a share**, width 2.3 to 1. Literal window beside: $7.22 to $15.81.
- **The floor, tested first:** at $5.12 (enterprise cost $189.9M) the no-growth case returns about 23.0% and the decline
  case about 12.1% a year (literal window: 18.9% and 9.3%). Some case earns the floor.
- **Width:** 2.3 to 1, under the three-to-one line.
- **The price against the range:** $5.12 is below the bottom of the central range ($8.67) by about 41%.
- **Fair price (Part VII; each end valued at ten percent, averaged; company's own tax; no conversion):** **$8.40 a share
  on the all-equity basis** (central; ends $5.80 and $10.99); **$9.54 on the equity-only basis** (beside; owner cash after
  interest $41.1M cycle base, growth -0.7% between halves; ends $9.32 and $9.76). Literal window: $6.99 all-equity, $7.46
  equity-only.
- **Beside, not part of the convention:** the ten-year record FY2016-25 with the ARI purchase deducted averages $10.9M of
  all-equity owner cash a year; at no growth that is $5.25 a share at the government rate and $3.21 at ten percent, and
  at $5.12 it returns about 5.8%. The range's comfort rests on a window that begins after the 2017 purchase.

### Bearing on Q9 (debt and exposures)
- No borrowings at 2026-06-30; $40M asset-based facility (cut from $75M in June 2025), secured "by substantially all of our
  assets", maturing **2027-03-02**; minimum liquidity covenant $5M; a springing fixed-charge covenant (10-Q Q2 2026).
  Environmental impairment insurance $10M per occurrence and aggregate (Item 1). DLA 15% of revenue; one other customer
  20% of receivables at 2026-06-30 (10-Q). The 2018-2019 record of covenant waivers after a debt-financed purchase (Step 0).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `aa6610f9`); written question by question; committed after Step 0,
      Q1, Q2 and the close (write-early).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's to hold; the
      fold into the register is the dispatcher's (operator rule ten). This run binds nothing until folded.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under Contamination and not used.
- [x] Every v5 id resolves (`check_ids.py` in the research folder: every id in the CSV, every quoted fragment beside an
      id found in that row, no E-id); every filing fact carries its document and accession.
- [x] The order was kept; the first failing STOP (Q2) closed the run; everything after it is under AFTER THE STOP and
      every figure there is headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (operating cash less stock pay less all capital spending less acquisitions), never
      a net-income proxy; the sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found: in the foundations (six items) and in Q1 and Q2.
- [x] Not a point-in-time run; no anchor bar applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; its ids, rules and floor were not read as rules. Its "D&A"
      column for FY2025 is the intangible-amortization line, checked and corrected in Step 0.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the commit message of the close).

**Honest limits.** The ten-year operating-cash, debt and capital figures before FY2023 are XBRL transcriptions checked
against the filed text only where quoted (FY2018 write-down and revenue bridge; FY2025 cash flow statement); the
borrowings column for FY2017-FY2021 adds two tagged lines and is marked "about". The rival comparison could not be made at
all. The Q1 verdict rests on the routing paragraph and a reader could route the same doubt to Q1 (below).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
**(1) Where a regulated commodity belongs.** The commodity paragraph says a dependence on a commodity price "is never by
itself a STOP at Q1 or Q2", but this business depends on a price that a regulator makes (the AIM Act's allowances, the
EPA's rules, one of them under reconsideration). Q1's definition of understanding, a "fix" on earning power in ten years
**[M2012-065]**, and its doubt rule **[M2002-092]** would close the file at Q1 TOO HARD (NATURE); the commodity routing
sends the same doubt to Q2 and Q7. I followed the routing and closed at Q2 on the same cause, so the box does not change,
but the text does not say whether a regulator-set price is a "commodity price" for the routing. **(2) The low-cost test
when no rival is named.** The commodity paragraph distinguishes "operators' reports not read" (WORK) from "no filing
states it" (NATURE); the brief limits rivals to those the 10-K names, and this 10-K names none. I read the absence of any
named rival, together with the filer stating no cost position, as "no filing states it". A run that searched for rivals
outside the 10-K (the brief forbids it) might find private and foreign firms whose filings do not break out reclamation,
reaching the same box; the text should say whether the brief's limit or the paragraph governs. **(3) The cycle base when
both ends of the window are troughs.** Specific (a) says "peak to peak or trough to trough" but not whether both troughs
are counted; FY2021-24 gives $48.2M, FY2022-25 $43.7M, FY2021-25 $35.8M. I took FY2022-25 (the cycle ending at the latest
trough) and showed the literal window beside; the text should fix the count. **(4) A window that begins after a
ruinous purchase.** The five-year window starts four years after the 2017 acquisition that nearly broke the company, and
the ten-year average with that purchase deducted ($10.9M) puts the price near the government-rate value. The convention
has no place for the previous cycle's acquisition once the cycle growth is meaningless; I showed it beside, unlabelled
as a range end. **(5) The change-for-the-better re-look** names a volume fall as the trigger, but here volume rose while
price fell; the question the downturn must answer is whether the price holds, and a falling-volume trigger may never fire
for a business whose volume grows as its price falls.

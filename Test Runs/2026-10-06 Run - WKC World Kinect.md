# Company Run: World Kinect Corporation (NYSE: WKC), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from `Test Runs/_TEMPLATE - Company Run.md`
to this dated name before any fetch. Working folder: `Test Runs/_research 2026-10-06 WKC/` (fetch script, filing texts,
competitor filings, `value_calc.py` and its output).

*(Formatting note: the template's em dashes in headings are written here as colons or hyphens under the operator's
standing no-em-dash rule; the protocol's required heading is written "COMPUTATION - NOT A CLEARANCE".)*

**POSITION NOTE, declared before any verdict:** not checked. The blind rule of this run forbids opening `PORTFOLIO.md`
or any holding review. The names of the holding reviews dated 2026-10-05 were visible in a directory listing (BN, BRK.B,
CCB, HRB, MITSY, NCLTY, SONY, TBTC, V, and a QQQM note); WKC is not among them. That is a file-name observation, not a
check of the portfolio.

**CONTAMINATION, declared.** Seen before or during the run without opening the files: the git status and recent commit
subjects in the session context (purchase runs of record for BCC, ASO and BTU closing OUT at Q2, a session-state commit
"S&P 600 ranks 31-40", a `cover_shares.py` fix; untracked 2026-10-06 run files for PATK, REYN and TPC); a directory
listing of `Test Runs/` showing the names of the 2026-10-05 runs, research passes and holding reviews; the memory index
line "57 gate-clearers, nothing buyable". No file about WKC was found in `Test Runs/` by a name search for WKC, INT and
World; none was opened. The commit subjects carry a prior: three recent names closed OUT at Q2 on commodity grounds. I
name it so that it can be discounted; the Q2 below rests on WKC's own filings and the competitors' filings.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $36.43 (close 2026-10-05; Yahoo chart via `tools/sources.py`; **aggregator, live quote only**, operator
  rule 5). The same aggregator gives roughly $23 to $27 for most of 2025 and early 2026 and a rise to $39.79 on
  2026-07-27; the 2010-11-01 monthly close was $37.54 (aggregator, flagged).
- **Shares by class** from the latest filing's cover: one class, common stock $0.01 par, **51,151,620** (10-Q for the
  quarter ended 2026-06-30, filed 2026-07-24, accession `0000789460-26-000040`; `python Screens/cover_shares.py WKC`).
  Balance-sheet count 51.2M at 2026-06-30 against 54.1M at 2025-12-31 (same 10-Q).
- **Market cap:** 51.15M x $36.43 = **$1,863.5M**.
- **Convertible:** $350.0M 3.250% notes due 2028-07-01, conversion price about $28.08; principal settled in cash; note
  hedges at the conversion price and sold warrants at $39.64 (10-K FY2025, accession `0000789460-26-000015`, MD&A). At
  $36.43 the hedge offsets the conversion premium, so no share dilution below about $39.64; the $350M is in debt.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 10/05/2026
  (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-24, `0000789460-26-000015`): Business, Risk Factors,
  MD&A in full, balance sheet, cash-flow statement, Notes 3, 8, 9 and the tax note; 10-Q Q2 2026 (filed 2026-07-24,
  `0000789460-26-000040`): MD&A, cash flow, repurchase table; proxy DEF 14A (filed 2026-04-28,
  `0001193125-26-187092`): summary compensation, incentive design, severance, ownership; 8-Ks
  `0001193125-25-253809` (2025-10-22 succession), `0001193125-25-312919` (CAO pay), `0001193125-25-280505` (credit
  agreement), `0000789460-26-000046` (2026-09-17, founder steps down as Executive Chairman),
  `0000789460-26-000035` (Q2 2026 release). For the fifteen-year record: 10-Ks FY2009 (`0001193125-10-040758`), FY2012
  (`0001047469-13-001398`), FY2015 (`0001558370-16-003246`), FY2018 (`0001628280-19-002382`), FY2020
  (`0001628280-21-003481`), FY2022 (`0001628280-23-005058`), FY2023 (`0001628280-24-006634`), FY2024
  (`0001628280-25-007620`); Q4 earnings releases for FY2015 (`0001157523-16-004555`) and FY2016
  (`0001628280-17-001322`) for volumes, which the older 10-Ks do not state.
- **One figure cross-checked against the filed statement:** total assets at 2025-12-31, $5,863.9M on the filed balance
  sheet (10-K FY2025) against $5,864M in `tools/run.py`'s XBRL table; goodwill $737.5M filed against $738M. They agree.
- **`python tools/run.py WKC`, arithmetic lines only** (Part VII; its v4 material ignored): OCF 271.3 / 259.9 / 292.9
  for 2023-2025; SBC 24.2 / 28.1 / 25.5; capex 87.6 / 68.2 / 65.6; D&A 104.5 / 106.4 / 98.2; five-year means 136.3
  (capex basis) and 104.6 (D&A basis). Its three-year window (175.0 / 145.7) is not used: the three most recent years
  are years of falling fuel prices, which release working capital (the 10-K says so of 2025: cash "driven by the
  declining price environment"). **Checked against the filings:** the tool's OCF for 2016-2018 is the restated figure.
  The FY2018 10-K moved "Cash receipts of retained beneficial interests in receivable sales" ($154.5M, $338.8M,
  $369.8M for 2016-2018) from operating to investing; with them added back, OCF is $205.2M, $205.2M and $187.3M, which
  is what the earlier 10-Ks reported. The series below uses the added-back figures.

### Owner cash, the whole cycle (USD millions; filed cash-flow statements; `value_calc.py`)
Owner cash = operating cash flow (with the receivables-sale receipts added back for 2016-2018) less stock pay less all
capital spending; the D&A variant beside it. Never a net-income proxy (operator rule 5).

| year | OCF | SBC | capex | D&A | owner cash (capex) | owner cash (D&A) | tax paid | acquisitions less divestitures |
|---|---|---|---|---|---|---|---|---|
| 2010 | -35.7 | 8.8 | 12.5 | 19.1 | -57.0 | -63.6 | 24.8 | 177.8 |
| 2011 | -142.5 | 11.0 | 19.5 | 40.5 | -173.0 | -194.0 | 51.1 | 122.7 |
| 2012 | 145.8 | 14.1 | 28.5 | 36.7 | 103.2 | 95.0 | 26.5 | 217.8 |
| 2013 | 264.3 | 16.7 | 82.7 | 44.7 | 164.9 | 202.9 | 34.6 | 76.9 |
| 2014 | 141.2 | 15.8 | 50.2 | 59.4 | 75.2 | 66.0 | 40.8 | 230.6 |
| 2015 | 447.5 | 17.0 | 51.0 | 63.4 | 379.5 | 367.1 | 44.0 | 96.9 |
| 2016 | 205.2 | 19.2 | 36.1 | 82.3 | 149.9 | 103.7 | 37.5 | 430.8 |
| 2017 | 205.2 | 21.2 | 54.0 | 86.0 | 130.0 | 98.0 | 50.8 | 120.7 |
| 2018 | 187.3 | 8.3 | 72.3 | 81.5 | 106.7 | 97.5 | 85.3 | 21.3 |
| 2019 | 228.8 | 23.6 | 80.9 | 87.4 | 124.3 | 117.8 | 82.9 | -30.8 |
| 2020 | 604.1 | 0.0* | 51.3 | 85.8 | 552.8 | 518.3 | 68.5 | -131.0 |
| 2021 | 173.2 | 19.6 | 39.2 | 81.0 | 114.4 | 72.6 | 39.0 | 12.1 |
| 2022 | 138.5 | 17.6 | 78.6 | 107.8 | 42.3 | 13.1 | 66.6 | 643.9 |
| 2023 | 271.3 | 24.2 | 87.6 | 104.5 | 159.5 | 142.6 | 61.3 | 67.3 |
| 2024 | 259.9 | 28.1 | 68.2 | 106.4 | 163.6 | 125.4 | 60.6 | -117.2 |
| 2025 | 292.9 | 25.5 | 65.6 | 98.2 | 201.8 | 169.2 | 97.0 | 137.4 |

\*2020 stock pay was filed as -0.9 (reversals); taken as zero, not as an add. Acquisitions include deferred
consideration paid in financing (2023-2025: 62.9, 51.8, 7.2). H1 2026: OCF **-$67.7M** (10-Q), the working capital
absorbing the 2026 fuel-price rise.

- **Five-year average (2021-2025):** $136.3M (capex basis); $104.6M (D&A basis); cash taxes $64.9M.
- **Whole cycle (2010-2025, sixteen years, which holds two fuel-price collapses, a pandemic and two price spikes):**
  $139.9M (capex basis); $120.7M (D&A basis). The whole-cycle figure and the five-year figure agree within 3%.
- **Where the cash went over the sixteen years:** owner cash summed to **$2,238M**; acquisitions less divestiture
  proceeds summed to **$2,077M**, 93% of it. Buybacks 2013-2025 were about $717M and dividends 2010-2025 about $336M, far more than the
  $161M left after acquisitions; total long-term liabilities were $81.4M at 2010 year-end (10-K FY2012, selected data)
  and debt was $697.1M at 2025 year-end.
- **Maintenance:** the 10-K says 2026 capex will be "generally consistent" with 2025's $65.6M; capex ran below D&A in
  every year from 2016 to 2025 (capex 36-88, D&A 81-108), part of D&A being amortization of acquired
  intangibles. Where maintenance sits inside the capex band the filing does not say. The larger question is whether
  acquisitions are a cost of standing still; that is Q3's and is not reached (see the computation section).

### Balance sheets, ten year-ends, read before the income account **[M2025-032]**
"balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**. From the
`tools/run.py` table (first-filed XBRL), checked against the FY2025 filed balance sheet:

| year-end | assets | equity | goodwill | intangibles | receivables | payables | inventory | debt | cash |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 5,413 | 1,925 | 836 | 282 | 2,344 | 1,770 | 458 | 1,186 | 699 |
| 2018 | 5,677 | 1,815 | 853 | 245 | 2,740 | 2,400 | 523 | 701 | 212 |
| 2020 | 4,500 | 1,909 | 859 | 203 | 1,238 | 1,215 | 344 | 525 | 659 |
| 2022 | 8,165 | 1,985 | 1,233 | 336 | 3,294 | 3,530 | 780 | 846 | 298 |
| 2024 | 6,732 | 1,949 | 1,182 | 261 | 2,433 | 2,727 | 514 | 881 | 383 |
| 2025 | 5,864 | 1,299 | 738 | 312 | 2,208 | 2,587 | 454 | 697 | 194 |

What the figures say:
- **Equity did not grow in ten years.** $1,925M (2016) to $1,949M (2024), then $1,299M after the 2025 write-downs.
  Book value per share rose only because shares fell (about 70M to 51M). Retained earnings $1,679M (2016) to $2,009M
  (2024) to $1,316M (2025).
- **Most of the equity was purchased goodwill.** Goodwill plus intangibles were $1,118M of $1,925M equity in 2016 and
  $1,443M of $1,949M in 2024. Tangible equity at 2025-12-31 is about $250M ($1,299M less $738M less $312M), under
  $5 a share, against $2.2B of customer receivables. The land goodwill bought with Flyers in 2022 ($795M purchase
  price, 10-K FY2023) was largely written off in 2025 ($528.3M goodwill impairment, plus $161.3M other asset
  impairments, 10-K FY2025).
- **The business is financed by its suppliers and by selling its receivables.** Payables ($2.6B) exceed receivables
  ($2.2B) at 2025 year-end; in addition the company sold receivables with a face value of $11.5B in 2025 under
  receivables purchase agreements, off the balance sheet, paying $31.8M in fees (Note 3), and had $210.1M of supplier
  finance obligations (Note 8) and $490.3M of letters of credit and bank guarantees (MD&A). Receivables and payables
  move with the fuel price: in H1 2026 receivables rose to $2.94B and the credit-loss allowance from $15.6M to $48.6M
  (10-Q), after a marine customer "filed for creditor protection during the second quarter of 2026".
- **Debt** fell from $1,186M (2016) to $697M (2025) and was $745.4M at 2026-06-30; cash $135.3M (10-Q).
- **What they cannot say:** the credit quality of the receivables sold off balance sheet; the outcome of the Danish tax
  case, final assessments of $123.6M for 2013-2019 and proposed $27.0M for 2020-2021, against total unrecognized tax
  liabilities of $95.9M (10-K FY2025, tax note); "Other non-current assets" of $965.9M are not itemized on the face.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what the business will do, not what the quote does. The quote rose from about
$23 in March 2026 to $36.43 as a Middle East conflict drove jet fuel to $4.24 a gallon in Q2 2026 (10-Q); the market
"just tells us prices" **[M2006-077]**, and a price spike in fuel is not a forecast of WKC's economics. No macro
forecast enters the verdict: "just never enter into the discussion" **[M2000-094]**. The analyst's habits: hunt
"what you’re missing" **[M2025-013]**, and read the competitors "to possibly reject your original hypothesis"
**[M1998-144]**.

**Contrary evidence, written down as found** **[M1997-127]** ("write it down in the first 30 minutes"):
1. *For the business, found while reading:* aviation gross profit per gallon rose from about 5.6 cents (2014-2017) to
   7.4 cents (2025), and aviation operating income from about $130-150M (2011-2015) to $240-259M (2024-2025), on flat
   volume. The aviation segment is better than it was. Written down at once; weighed at Q2.
2. *For the business:* the marine segment "traditionally benefited from elevated fuel prices and volatility as well as
   a constrained credit environment" (10-K FY2025); H1 2026 gross profit rose 37% (10-Q). The business is paid when
   others are short of credit. Weighed at Q2 (it is the opposite of a moat that holds in calm years).
3. *Against my first read of the price:* at the sovereign rate and no growth, five-year owner cash is worth about $47 a
   share, above the $36.43 price. Written down; it bears on nothing until Q2 is passed (computation section).

## THE STANDING RULE
Owning this, bought for cash and sized so that a total loss cannot touch what the buyer has and needs, puts the buyer
at no risk of ruin: "We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]**; no borrowed money **[L2014-005]**. The target's own leverage (receivables financed by suppliers and
banks) is Q9's and is not reached.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**.
- **What the business is, from the filing.** It buys aviation, marine and land fuel from refiners and other suppliers
  and resells it with credit, logistics and services; "Profit from our segments is generally determined by the volume
  and the unit margin achieved on fuel resales" and depends on operating expenses "which may be materially affected to
  the extent that we are exposed to credit losses" (10-K FY2025, Item 1). In the land segment "We typically serve as a
  reseller, where we purchase fuel from a supplier and contemporaneously resell it"; in marine "we serve primarily as a
  reseller" and "The majority of our marine segment activity consists of spot sales" (same).
- **Key variables and whether they are foreseeable** ("trying to identify the key variables in that particular
  business, and evaluating how predictable they were first" **[M1998-044]**): volume (aviation 6.3B gallons in 2015,
  8.5B in 2019, 7.1B in 2025; marine 32.6M metric tons in 2015, 15.8M in 2025); unit margin (total gross profit of 4 to
  6 cents a gallon-equivalent in every year from 2014 to 2025); operating cost (compensation plus G&A $720M against
  gross profit $948M in 2025); credit losses (provisions $3.8M to $63.7M a year, 2008-2025, the worst in 2020). The
  year-to-year margin moves with fuel-price volatility and credit conditions, which nobody can forecast; the decade
  range of each variable is on the public record and has held through 2008, 2014-2016, 2020 and 2022. The ten-year
  picture is foreseeable in outline: a thin-margin reseller of a product whose demand changes slowly. Fifteen years of
  statements do tell me what the future statements will look like **[M2008-033]**: "the financial statements will tell
  me the information that’s useful to me".
- **Routing.** Not a fast-changing technology; the energy transition (sustainable aviation fuel, marine fuels) is slow
  change, owned by Q2. Not a bank, though it extends unsecured trade credit; its receivables are 94% under 60 days
  (Note 3) and its loss history is readable. The derivatives book is for hedging and customer pricing (net commodity
  derivative fair value $65.0M at 2025 year-end, Item 7A), small against the business.
- **The doubt rule.** "if you have doubts about something being into your circle of competence, it isn’t."
  **[M2002-092]**. My doubt is not whether I can picture this business in ten years; it is whether the picture is a good
  one. That is the castle question.
- **VERDICT: IN.** The economics can be pictured from the filings **[M2012-065]**, **[M1998-044]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing?" **[M1995-038]**. The filer has answered for itself, the same way in 2015 and 2025.

**The castle tests, each with its filing fact**
- **The attacker with money.** "if I had a hundred million dollars and I wanted to go in and take on See’s Candy,
  could I do it?" **[M2011-015]**. WKC's competitors "range from large multinational corporations, which have
  significantly greater capital resources than us, to relatively small and specialized firms"; "In our fuel
  distribution activities, we compete with major oil companies that market fuel and other energy products directly"
  (10-K FY2025, Item 1). And the barrier it does have is money, which the fuel price lends and withdraws: "Low fuel
  prices also facilitate increased competition by reducing financial barriers to entry and enabling existing,
  lower-capitalized competitors to conduct more business as a result of lower working capital requirements" (10-K FY2025,
  MD&A; the same sentence is in the 10-K FY2015, `0001558370-16-003246`). A barrier made of working capital is the
  attacker's to cross whenever fuel is cheap. "there are some industries that are just never going to have barriers to
  entry" **[M2012-106]**. Against the majors the edge in money runs the other way, as in leasing: "The banks have an
  advantage over us because their cost of funds is so low now." **[M2016-029]**.
- **Would the customer still choose it over the low bid?** "it wouldn’t be a question of people buying candy for the
  low bid" **[M2017-009]**. WKC: "We compete, among other things, on the basis of service, convenience, reliability,
  availability of trade credit and price"; marine is mostly "spot sales"; "many of our sales contracts being 12 months
  or less in duration" (10-K FY2025). The product is jet fuel, bunker fuel and diesel to specification, sold by many:
  "most insureds don't care from whom they buy" **[L2004-003]**, read for fuel.
- **The service escape, tested.** The rows name service as a way out of the commodity class: "fractional ownership is
  not a commodity business" because "the people care enormously about service" **[M2001-014]**. WKC claims "the breadth
  of our service offerings combined with our global supplier network is a strategic differentiator" (Item 1). The
  filing's own risk factor answers: "Industry developments, such as fuel price transparency, procurement technology
  tools, increased regulation and increasing customer sophistication may, over time, reduce demand for our services"
  (10-K FY2025, Item 1A). And the GEICO row puts service in its place: good service "does not distinguish us from a great
  many competitors. Having the low cost is crucial." **[M2000-146]**.
- **The low-cost position, the one exception for a commodity field.** "Another way to prosper in a commodity-type
  business is to be the low-cost operator." **[L2004-007]**; "being the low-cost producer is all-important"
  **[L2000-017]**. No evidence in the filings that WKC is the low-cost operator, and evidence against: WKC buys from
  refiners who "may have significant negotiating leverage over us" (Item 1A: "we rely on a single or limited number of
  suppliers ... These parties may have significant negotiating leverage over us"); its operating costs absorbed 76% of
  gross profit in 2025 ($720M of $948M), against 67% in 2014 ($545M of $814M; operating income $269M); operating income
  including every real cost fell from an average of $263.5M (2012-2014) to $227.3M (2022-2024), about 1.5% a year,
  while about $1.6B net went into acquisitions (2012-2024). A low-cost operator would show costs falling against its rivals and share
  rising **[L1996-015]**; WKC shows neither. "commodity businesses have risk unless you’re the low-cost producer"
  **[M1997-010]**.
- **Pricing power and the agony before a rise** **[M2005-020]**. No price is set by WKC; its revenue moves with the
  index price and its margin with volatility. The filer: "Due to the generally spot nature of sales in our marine
  business, we have traditionally benefited from elevated fuel prices and volatility as well as a constrained credit
  environment" (10-K FY2025). Profit set by the market's condition, not by the seller: "whatever he charged for gas was
  my price" **[M2012-109]**; "he determined our profit, because we looked at his price every day" **[M2023-079]**.
- **Unit volume and share.** Marine volume fell by half, 32.6M metric tons (2015) to 15.8M (2025); marine gross profit
  $189.6M to $123.1M; marine operating income $73.0M (2015) to $0.9M (2025). Aviation volume 6.3B gallons (2015), 8.5B
  (2019), 7.1B (2025), and the 2026 10-Q reports volume falling again, "driven primarily by a reduction in lower margin
  activity". Land volume rose only by purchase (4.2B gallons 2014, 6.2B 2022 after Flyers) and is being cut back by
  sale (Watson Fuels 2025, Brazil 2024, transport and lubricants 2026).
- **Widening or narrowing** ("whether it’s likely to widen further or shrink on you" **[M1999-108]**). Narrowing in
  marine and land on the numbers above; the land write-off is the company's own estimate that the land reporting unit
  is worth $528M less than it paid. Aviation is the exception (contrary evidence 1): gross profit per gallon 5.7 cents
  (2015), 6.5 (2019), 6.6 (2023), 7.4 (2025). Read in full, the 2025 rise is partly bought (Universal TSS, acquired
  November 2025 for about $207M) and the 2026 rise is volatility ("stronger physical inventory-related profitability
  ... driven by elevated jet fuel price volatility", 10-Q). Over 2014-2025 aviation's margin rose about 1.7 cents a
  gallon while its volume did not grow; that is the record of a reseller dropping low-margin accounts, which the 10-Q
  names, not of a castle widening.
- **What could destroy, modify or reduce it** **[M2000-014]**. The filer names it: price transparency, procurement
  tools and customer sophistication (Item 1A, above); and the energy transition, which "could adversely affect demand for
  our energy products" (Item 1).
- **Ask the competitors.** Not possible from the record; their filings stand in below.

**The competitor row, same metric from the competitors' own filings** (gross profit or product margin per gallon; the
whole span available, not one year)

| business | metric | 2014 | 2015 | 2016 | 2018 | 2019 | 2021 | 2022 | 2024 | 2025 | source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| WKC, all segments | gross profit per gallon-equivalent (marine at 264 gal/t) | 4.9c | 4.3c | 4.3c | 5.1c | 5.7c | 4.9c | 5.9c | 5.8c | 5.6c | WKC 10-Ks and releases above |
| WKC aviation | gross profit per gallon | 5.6c | 5.7c | 5.6c | 6.2c | 6.5c | 6.6c | 5.0c | 6.7c | 7.4c | same |
| WKC land | gross profit per gallon-equivalent | 6.7c | 6.3c | 6.5c | 6.5c | 6.9c | 5.7c | 7.7c | 6.3c | 5.3c | same |
| WKC marine | gross profit per metric ton | $8.00 | $5.82 | $4.76 | $6.15 | $8.68 | $5.45 | $13.40 | $9.42 | $7.79 | same |
| Global Partners (GLP), Wholesale | product margin per gallon | 5.9c | 5.6c | 4.8c | 3.8c | 2.9c | 3.8c | 8.4c | 6.4c | 5.5c | GLP 10-Ks FY2016 `0001558370-17-001611`, FY2019 `0001558370-20-002120`, FY2022 `0001558370-23-002156`, FY2025 `0001104659-26-021381` |
| GLP, Commercial | product margin per gallon | 7.5c | 6.5c | 4.6c | 3.7c | 3.8c | 4.2c | 9.9c | 6.7c | 4.7c | same |
| GLP, Gasoline Distribution and Station Operations (owned and leased stations) | gasoline product margin per gallon | 18.4c | 18.3c | 18.2c | 23.4c | 23.1c | 26.8c | 35.7c | 36.5c | 38.3c | same |
| Sunoco LP (SUN), wholesale motor fuel | gross profit / profit per gallon | 10.6c | 9.4c | 9.8c | 11.4c | 10.1c | 11.2c | 12.8c | 11.6c | 13.2c | SUN 10-Ks FY2016 `0001552275-17-000012`, FY2019 `0001552275-20-000007`, FY2022 `0001552275-23-000010`, FY2025 `0001552275-26-000021` |

*Arithmetic: WKC segment gross profit divided by the segment volumes the filings and releases state (2021 land 5,254
million gallons and marine 18.4M t from the FY2022 10-K; 2019 from the FY2020 10-K's year-on-year changes). GLP's
per-gallon figures are segment product margin divided by segment volume from its tables; its 2018 and 2021 columns are
from the comparative years of the FY2019 and FY2022 10-Ks. Sunoco's figures are as it reports them (wholesale only for
2014-2016, all motor fuel after its 2018 retail sale; 2024-2025 include its NuStar-era volume growth). WKC 2016 aviation and
land gross profit are derived from the FY2018 10-K's stated changes against 2017; WKC 2018 volumes are the rounded
figures the FY2018 10-K states (8.2B, 5.6B gallons, 23.7M t). Signature Aviation (London-listed) files nothing with the SEC; Atlantic Aviation's owner Macquarie
Infrastructure (MIC 10-Ks FY2015 `0001144204-16-083730`, FY2019 `0001628280-20-002149`) describes its FBO fuel as sold
on "the dollar-based margin/fee per gallon" with "fluctuations in the cost of fuel ... passed through to the customer",
but its filings give no per-gallon figure I could extract; the oil majors do not report marketing margins per gallon.*

**What the row shows.** Over twelve years WKC's resale margins sit in the band of a pure wholesaler with no stations
(GLP Wholesale 2.9 to 8.4 cents, GLP Commercial 3.7 to 9.9 cents) and below a wholesaler with long fixed-margin supply
contracts and branded sites (Sunoco 9.4 to 13.2 cents). The money in fuel distribution is earned where a location is
owned: GLP's stations earn 18 to 38 cents a gallon and that margin has doubled since 2016; WKC's land margin fell from
6.7 to 5.3 cents over the same span. Every distributor's margin jumps in the volatile years (2022 for all three
resellers), which is the market paying for liquidity, not a castle. "Those are two different kinds of businesses."
**[M2009-059]**: WKC is the kind that is paid like the wholesaler, not the kind that owns the corner.

**The other side's case, stated as well as I can** (as the rows ask of a disagreement **[M2016-055]**): a forty-year
global network, credit and dispatch in 200 countries, a reputation for "surety of supply", an aviation business whose
unit margin has risen for a decade, and a marine business that earns most when credit is scarce; no competitor has
copied the network in four decades. That case is real for aviation. It does not answer three facts in WKC's own filings:
the barrier falls when fuel is cheap; the suppliers have the leverage and the customers have the price screens; and the
two non-aviation segments, half the gross profit, have shrunk or been written down while the money spent to grow them was
lost. A castle that one segment holds and two lose is not a castle the buyer of the whole company owns.

**Reading the evidence against the box.** The commodity marks are present in the filer's own words: rivals with more
capital, competition on price and credit, profit set by volatility, improvements copied ("the improvement you get one
day, your competitor gets the next day" **[M2004-053]**), and average that "is not going to go away, either"
**[M2000-072]**. The one way out the rows give, the low-cost operator **[L2004-007]**, **[L2000-017]**, is not shown;
the costs absorb more of the gross profit than a decade ago, and the high-cost producer's end is stated:
"In an unregulated commodity business, a company must lower its costs to competitive levels or face extinction."
**[L1994-035]**; "the guy with the lower cost comes in and kills you" **[M2001-013]**. The castle is not a castle whose
future cannot be judged; it is one the evidence shows open, at least in marine and land, by the filer's own account and
its own write-downs. Price does not reopen it: "What you can’t do is turn any investment into a good deal by paying
little" **[M2019-015]**.

- **VERDICT: OUT.** A commodity reseller that is not the low-cost operator, whose only barrier is working capital that
  the filer says falls with the fuel price, and whose marine share halved and land investment was written down: the
  castle is shown open on the evidence **[M2011-015]**, **[L1994-035]**, **[M1997-010]**, **[M2012-106]**. Box: OUT, of
  the three boxes "in, out, and too hard" **[M2006-013]**. Not TOO HARD: the deciding facts are in the filings and
  were read; nothing in the castle question waits on work not done.

## Q3: HOW MUCH CAPITAL MUST GO IN. WEIGHING.
NOT REACHED (Q2 closed OUT). Facts recorded for the record, no weighing: $2,077M of net acquisitions against $2,238M of
owner cash over 2010-2025; land operating income $75-90M (2012-2014) against $40-41M (2023-2024) after the $795M Flyers
purchase.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. STOP on confusion; otherwise WEIGHING.
NOT REACHED as a verdict. The balance sheets were read in Step 0, as the template asks when the file closes before Q4.
Facts recorded: the operating-cash reclassification of 2016-2018 (handled above); "restructuring and exit costs" in 2023,
2024, 2025 and 2026 (recurring); the annual bonus is 75% on "Adjusted EBITDA" (proxy 2026).

## Q5: WHO RUNS IT. STOP on integrity.
NOT REACHED. Facts recorded: founder Michael Kasbar, CEO to 2025-12-31, paid $6.4M to $6.8M a year 2023-2025 (proxy
2026) in a period when net income was $52.9M, $67.4M and -$614.4M; the 2023-2025 performance units were forfeited in
full when adjusted EPS missed the threshold; he steps down as Executive Chairman on 2026-12-31 and receives the severance
of an employment agreement that "expired on December 31, 2025" (8-K `0000789460-26-000046`; proxy). CFO since 2007, Ira
Birns, became CEO on 2026-01-01. Officers and directors own 3.8% as a group.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. WEIGHING.
NOT REACHED. Facts recorded: buybacks with no stated price (authorizations of $200M in 2024 and $150M in 2025 "do not
require a minimum number of shares" and "have no expiration date", 10-Q); about $75M bought in Q1 2026 and 500,000
shares at $28.56 in May 2026; the 2022 Flyers deal paid $642.7M cash and 1,768,034 shares at $28.28 (10-K FY2022).

## Q7: WHAT IS IT WORTH. STOP.
NOT REACHED as a verdict. The owner's arithmetic is in the section below, headed as a computation.

## Q8: IS IT BETTER THAN THE ALTERNATIVES. STOP.
NOT REACHED.

## Q9: COULD IT RUIN US. WEIGHING.
NOT REACHED. Facts recorded: debt $745.4M (2026-06-30); letters of credit and guarantees $490.3M; off-balance-sheet
receivable sales; Danish tax assessments of $150.6M final and proposed; the credit agreement's leverage covenant of 4.75
times an EBITDA-based measure.

## Q10: IS IT THE FAT PITCH. WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (No named business: fuel distribution is not among the businesses the rows name.)

---
## COMPUTATION - NOT A CLEARANCE
*Written at the owner's request (reporting, not a rule change). The file closed OUT at Q2; nothing here reopens it
**[M2019-015]**, and nothing here is entry language. Operator rule 3.*

**Construction (the Q7 CONVENTION of Part VI, applied as written).** Cash input: owner cash after every real cost,
five-year average, capex basis (D&A variant beside it). Growth shown, measured on aggregate owner cash: the four-year
block 2012-2015 averaged $180.7M and 2022-2025 averaged $141.8M, **-2.4% a year** over ten years; operating income
including every real cost agrees in sign (-1.5% a year, 2012-2014 to 2022-2024). Any growth figure here depends on the
base years ("a base year in which earnings were poor can produce a breathtaking, but meaningless, growth rate"
**[L2005-003]**), so both blocks are four-year averages across price cycles. Ten years at the growth shown, then zero
nominal growth, discounted at the 30-year Treasury, 5.66%. The two ends: no growth and growth shown (-2.4%).

**(a) VALUE RANGE** (per share, 51.15M shares; owner cash is after interest and tax, so these are equity values):

| case | cash input | growth shown (-2.4%) | no growth |
|---|---|---|---|
| five-year, capex basis (the convention's case) | $136.3M | **$38.97** | **$47.09** |
| five-year, D&A basis | $104.6M | $29.90 | $36.12 |
| **whole-cycle variant**, sixteen years 2010-2025, capex basis | $139.9M | **$39.99** | **$48.32** |
| whole-cycle, D&A basis | $120.7M | $34.51 | $41.70 |
| acquisitions treated as a cost of standing still (sixteen years; owner cash less net acquisitions) | $10.1M | $2.87 | $3.47 |

- **The convention's range: $38.97 to $47.09** against a price of **$36.43**. Width 1.2 to 1. The price sits 7% below
  the bottom of the range: under the convention that is OUT, "not a screamer" ("It should scream at you."
  **[M2009-005]**; "it’s too close to think about" **[M1996-084]**).
- **The whole-cycle variant: $39.99 to $48.32**, because fuel prices swing working capital; it agrees with the five-year
  case within $1.25 a share, since the sixteen-year average ($139.9M) and the five-year average ($136.3M) are close.
- **The width question the range hides.** If the acquisitions were the cost of keeping the gallons (land volume rose
  only by purchase and op income fell anyway), the cash that was free to owners over sixteen years averaged $10.1M a
  year and the bottom of the range falls to about $3. With that row in, the range is wider than three to one and the
  convention would close TOO HARD ("the range must be so wide that no useful conclusion can be reached" **[L2000-025]**).
  Which reading is right is Q3's question; Q2 closed first.

**(b) FAIR PRICE: the price at or below which the central case clears the ~10% pre-tax floor** (CONVENTION, Q7:
**[M2003-149]**, **[L2002-020]**: "a very high probability of at least 10% pre-tax returns").
- **Tax treatment:** owner cash is after tax; pre-tax owner cash adds back cash taxes paid (five-year average $64.9M),
  giving $201.2M (capex basis) and $169.5M (D&A basis). **The floor is applied on equity** (market cap), because owner
  cash is already after interest; the enterprise variant is shown beside it.
- **Central case** (five-year capex basis at the growth shown, -2.4% for ten years then flat): fair price **$33.50**
  (the price whose pre-tax cash stream, discounted at 10%, equals it). At no growth: $39.34. Whole-cycle central case:
  $32.35 (no growth $37.99). D&A basis central: $28.21.
- **At $36.43 the expected pre-tax return is about 9.2%** in the central case (10.8% only if the decline stops at once;
  7.6% on the D&A basis), below the floor: "there’s just a point at which we drop out of the game" **[M2003-149]**.
- **Enterprise variant:** pre-tax, pre-interest cash $306.8M (adding the five-year average of "interest expense and other
  financing costs, net", which includes the receivables-sale fees) against an enterprise value of $2,474M ($1,863.5M plus
  net debt $610.1M at 2026-06-30): 12.4%; fair equity price at 10% with no growth, $48.06. I do not use it as the central
  case: the receivables sold off balance sheet are not in the net debt, while their fees are in the interest added back,
  so the enterprise figure flatters.

**(c) CHEAP PRICE: below which no pencil is needed. My rule (CONVENTION of this run):** half of the lowest standard case
of the range, the five-year D&A basis at the growth shown ($29.90), so **$14.95**. Rationale: the rows ask for "a big
discount from that present value calculated using the risk-free interest rate" **[M1997-126]** and a price that
screams, as when "I didn’t need to know whether it was worth 97 billion or 103 billion if I was buying it at 35
billion" **[M2008-068]**, and give no number; a 50% discount to the lowest standard case is my figure, chosen because
at it the most conservative cash basis yields 22% pre-tax, more than twice the floor. It does not cover the
acquisitions-as-maintenance case (about $3), and it does not reopen Q2.

**Against the price:** $36.43 is above the fair price ($33.50 central, $32.35 whole cycle), inside the D&A-basis range,
just below the convention's capex-basis range, and more than twice the cheap price. Earnings at the date are near a peak:
H1 2026 gross profit is up 37% on fuel volatility (10-Q), and the reported quarter is not the base year ("a cyclical peak
in earnings" **[L1994-009]** is the first thing a high return is read for).

---
## THE BOX
**OUT at Q2.** A fuel reseller in a commodity field that is not the low-cost operator: its barrier is working capital
that falls with the fuel price (the filer's own words, 2015 and 2025), its suppliers hold the leverage and its customers
buy on price and credit, marine volume halved in ten years and the land investment was written down by $528M of
goodwill. Q3 to Q12 NOT REACHED. For the owner (computation only): value range $38.97 to $47.09 (whole cycle $39.99 to
$48.32) against $36.43; fair price about $33.50; cheap price about $14.95.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written top to bottom. [ ] Committed after each question: **not
      done**, by instruction of this run (no commits); the write-early discipline was kept in the file only.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script; see below); every filing fact has its
      accession; numbers carry a filing, a row, or a CONVENTION label.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance; the arithmetic is headed as a computation.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the US Treasury;
      the price flagged as an aggregator quote.
- [x] Contrary evidence written down as it was found **[M1997-127]** (three items, Foundations).
- [x] No row dated after the anchor: not a point-in-time run; the anchor is today.
- [x] Only the arithmetic lines of `tools/run.py` used; its OCF for 2016-2018 corrected from the filings, and its
      three-year window set aside for the reason given.
- [x] `python tools/check_framework.py` run after writing (result recorded below).
- **Honest gaps:** the oil majors' marketing margins and Signature/Atlantic per-gallon figures were not obtained; WKC's
  2021 aviation-plus-marine all-segment per-gallon cell and 2022's were not computed; volumes before 2014 are not in the
  filings read; the off-balance-sheet receivables outstanding at any date is not disclosed in what I read (only the
  annual face value sold); no scuttlebutt.

**Acceptance test, 2026-10-06:** `python tools/check_framework.py` **PASS** (test runs: phantom ids in 0 files; v5
ledger verbatim 4279/4279; v5 scope OK). The id check script (`Test Runs/_research 2026-10-06 WKC/check_ids.py`):
60 citations, 47 distinct ids, no E-ids, none missing; 42 quote-id pairs checked, 0 failures; 0 em dashes.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **Q2's "one exception" and the service escape do not say how to grade a company whose segments split.**
Aviation shows a rising unit margin while marine and land shrink; the framework tests "the castle" of a business, and
gives no rule for a company whose castle holds in one segment and is open in two. I closed on the whole company, the
thing a buyer of the shares owns, because the rows' holding-company rule (Q1, read by its parts, a part that matters and
fails keeps the whole out) points that way; that is my reading, and a rule is owed. (2) **The Q7 convention's "growth
shown" is unstable for a working-capital business.** Owner cash swings from -$173M to +$553M with fuel prices; any
endpoint growth rate is a base-year artifact **[L2005-003]**. I used four-year block averages and checked the sign
against operating income; the convention should say how growth is measured when the cash series is dominated by
working capital. (3) **The convention deducts capex but is silent on serial acquisitions.** Here acquisitions took 93%
of sixteen years of owner cash; whether they are maintenance changes the bottom of the range from about $39 to about $3
and flips the convention's verdict from OUT to TOO HARD. The construction should say where acquisition spending goes
(Q3 is the place, but Q7's arithmetic runs before Q3's judgment is read back). (4) **The protocol's required heading
contains an em dash**, which the operator's standing rule forbids; I wrote it with a hyphen and say so here.

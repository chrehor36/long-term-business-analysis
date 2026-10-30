# Company Run: Global Water Resources, Inc. (Nasdaq: GWRS), 2026-10-28
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind
purchase run under `Screens/_daily/_dispatch_brief.md` (the brief states its own departures: the new repository path, and the
lines of evidence derived by the analyst from Items 1, 1A and 7). Every judgment cites a v5 ledger id in bold; every filing
fact carries its accession; a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.
Copied from the template before any fetch (commit `c1c35afa`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-28, after the run was committed (5e67618b): not held (`PORTFOLIO.md` read for this ticker only).*

**Contamination declared.** Seen without opening, before the run began: the session context's recent commit subjects (all
about another company's run, none about this name); the memory index lines loaded with the session (queue counts, no
name of this company); a count of the files in `Test Runs/` printed by a shell command (a number, no names). No run
file, research pass, holding review, `PORTFOLIO.md`, queue or reading-list file was opened, listed or searched. Nothing
from them is used.

**Lines of evidence chosen** (brief's departure; derived from FY2025 10-K Items 1, 1A and 7, accession
0001628280-26-014659): (1) the ACC's rate regulation, the allowed return and the lag, and the open GW-Santa Cruz /
GW-Palo Verde rate case with its Southwest Plant matter; (2) connection growth and its dependence on housing in the City
of Maricopa (81.9% of connections in one municipality); (3) water supply under the assured-water-supply rules (DAWS); (4)
capital spending against operating cash, and how it is funded (debt, developer advances, repeated share sales);
(5) condemnation (two former utilities taken by municipalities); (6) the non-utility Buckeye growth premiums, which end
in 2034; (7) control by one family (42.3%) and the related-party placements.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $7.74 (2026-10-28, printed by `tools/run.py` as an aggregator quote, flagged per operator rule 5: live quote only).
- **Shares:** one class. Cover of the 10-Q for the period ended 2026-06-30 (filed 2026-08-13, accession
  0001628280-26-056446): **28,795,352** common shares as of 2026-08-07 (`python Screens/cover_shares.py GWRS`). Check
  against issued less treasury on the same 10-Q's balance sheet at 2026-06-30: 29,170,113 issued less 374,761 treasury =
  28,795,352, agrees. **After the 10-Q:** private placement of **1,129,944** shares at $8.85 agreed 2026-08-20 (8-K filed
  2026-08-21, accession 0001628280-26-058486; "Each of the Purchasers is an "accredited investor"", proceeds about $10
  million). Count used: **29,925,296** shares.
- **Market cap:** 29.925M x $7.74 = **$231.6M**.
- **Sovereign for the earnings currency (USD):** **5.30%**, US Treasury daily par yield curve, 30-year, 2026-10-27
  (issuing authority; printed by `tools/run.py`).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-03-04, accession 0001628280-26-014659), Items 1, 1A, 2,
  3, 5, 7 and 8 with the notes; 10-K FY2024 (0001434728-25-000079), FY2023 (0001434728-24-000087), FY2022
  (0001434728-23-000086), FY2021 (0001434728-22-000077) for the cash-flow statements and balance sheets of the window;
  10-Q Q2 2026 (0001628280-26-056446); DEF 14A 2026 (filed 2026-03-31, 0001628280-26-022461); 8-Ks of 2025-09-30
  (0001628280-25-044355), 2026-04-14 (0001628280-26-025290), 2026-04-28 (0001628280-26-028741), 2026-04-30
  (0001628280-26-029760), 2026-08-12 earnings release Ex. 99.1 (0001628280-26-056434), 2026-08-20
  (0001628280-26-058486), 2026-08-28 (0001628280-26-059647). Competitors: NW Natural Holding 10-K FY2025
  (0001733998-26-000012); Algonquin Power & Utilities 40-F FY2025, Ex. 99.3 MD&A (0001174169-26-000015).
- **One figure cross-checked against the filed statement:** net cash from operating activities 2025 **$20,168K** on the
  filed cash-flow statement (10-K FY2025, p. 59) against 20.2 printed by `tools/run.py`; capital expenditures 2025
  $67,321K filed against 67.3 printed. Agree.
- `tools/run.py GWRS`, arithmetic lines only (Part VII): OCF 25.4 / 21.8 / 20.2 (2023-2025, $M), SBC 1.3 / 1.0 / 0.9,
  D&A 12.3 / 12.7 / 15.0, capex 22.3 / 32.3 / 67.3; owner cash on the all-capex basis 1.8 / -11.6 / -48.0 before
  acquisitions; finance-lease principal 0.5 / 0.3 / 0.4 printed as an alternate (taken: it is a real capital payment).
  The tool's "d2" debt column (`CapitalizationLongtermDebtAndEquity`) is debt plus equity, not debt, and is not used.
  Nothing it prints as a rule, an id or a verdict is used.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would own this if the market closed for years **[M1997-109]**; a regulated
water utility is the kind of business one could own that way, so the foundation does not bar it. The market serves:
"it doesn’t tell us anything. It just tells us prices." **[M2006-077]**, so the recent share prices of the company's own
placements ($10.00, $10.30, $8.85) say nothing about value. No macro enters **[M2000-094]**: the housing permits and the
TSMC investment featured in the release are not used as forecasts. Who is paid to tell you **[M2020-037]**: the
management's release features growth language and an adjusted EBITDA; read as the seller's projection. The analyst's
habits: "What do I not know that I need to know?" **[M1999-129]**, and look for "what’s wrong" **[M2025-013]**.
**Contrary evidence, written down as found** **[M1997-127]**: (i) the ACC Staff's testimony of 2025-10-01 recommended a
net annual revenue *decrease* of about $7.1 million for the two largest utilities, against the company's request for an
increase (10-K FY2025, Item 7, Rate Regulation Updates); (ii) about $7.8 million of Southwest Plant cost was "prematurely
included as "plant in service"" for ratemaking from 2007 to 2024 (Note 3); (iii) dividends exceed net income every year
read and are charged in part to paid-in capital while shares are sold almost every year (statements of equity);
(iv) capital spending ran at 1.0 to 3.3 times operating cash in 2021-2025 (cash-flow statements); (v) 81.9% of active
connections are in one municipality (Item 1A); (vi) two former utilities were taken by condemnation (Item 1A).

## THE STANDING RULE
Owning a part-interest bought for cash puts the buyer at no risk of ruin from the buyer's own conduct; the rule binds the
buyer's financing and size, "never going to risk what we have and need for what we don’t have and don’t need"
**[M2012-081]**. Nothing in the target changes that; its own debt is weighed at Q9.

---
## Q1: CAN I UNDERSTAND IT? STOP.
- **The test applied.** Understanding means "a reasonable fix on about what the earning power and competitive position
  will look like in five or 10 years" **[M2012-065]**. The business: thirty-nine water, wastewater and recycled-water
  utility systems, all revenue regulated by the ACC (2025: $55.8M), one reportable segment (Note 18), 68,577 active
  connections, 87.3% in GW-Santa Cruz (water) and GW-Palo Verde (wastewater) in one service area (10-K FY2025, Item 1).
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) rate base, which grows with capital spent
  and is set by the ACC on a historical test year; (2) the allowed return (9.2% to 9.6% ROE on a 55% equity structure in
  the decisions and the 2026 settlement, Item 1 table; 8-K 2026-04-28); (3) the lag between spending and rates; (4)
  connections, which follow homebuilding in Maricopa; (5) water supply under the DAWS (22,900 acre-feet permitted, 9,501
  used in 2025, Item 1). Each is knowable from public filings and dockets; none turns on fast-moving technology. The
  financial statements do tell what the future ones will look like in their structure **[M2008-033]**: revenue is a
  regulated return on rate base plus costs.
- **What could keep it outside.** The size of the return the ACC will allow is a judgment of a five-member elected body;
  the rows on utilities say returns differ "by state" **[M2024-011]**. That is a question about the level of the return
  (Q2, Q3, Q7), not about whether the economics can be pictured. No doubt is found that the business sits inside the
  circle **[M2002-092]**.
- **VERDICT: IN** **[M2012-065]**, **[M1998-044]**: a regulated water and wastewater monopoly whose ten-year economics are
  rate base times an allowed return, less the lag, with the variables named above.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
- **The attacker with money** **[M2011-015]**. Inside its service areas no attacker can enter: "Arizona law provides the
  holder of a CC&N for water and wastewater service with an exclusive right to provide that service within the
  ACC-designated service area", and "the high cost of constructing water and wastewater systems in an existing market
  creates a barrier to entry" (10-K FY2025, Item 1, Competition). The competition named is for *new* service areas and
  acquisitions only. The one attacker the filings show succeeding is a government: "the assets of our former utility
  subsidiaries, Cave Creek Water Co. and Valencia Water Company, Inc., were acquired from us by municipalities pursuant to
  condemnation proceedings" (Item 1A). Condemnation pays a price (Valencia's still pays the Buckeye growth premiums, Note
  19), so it ends the franchise without ending the owner's capital at zero.
- **Pricing power and the agony before a rise** **[M2005-020]**. No price rises without a rate case; "Rate cases and other
  rate-related proceedings can take a year or more to complete" (Item 7). The present case is the agony in plain sight:
  the company asked for about $6.5M, the ACC Staff recommended a *decrease* of about $7.1M and RUCO an increase of about
  $3.0M (Item 7, Rate Regulation Updates); the settlement of 2026-04-28 gives GW-Santa Cruz about $2.3M at 55/45 and a
  9.6% ROE, withdraws GW-Palo Verde's case to be refiled in 2027, and *raises* GW-Palo Verde's bill credit by about $0.4M
  a year (8-K 0001628280-26-028741); the CEO calls it "a net $1.9 million rate increase" (Ex. 99.1, 2026-08-12). For a
  regulated monopoly this test reads the regulator, not the customer.
- **Unit volume** **[M1999-054]**. Active connections 68,577 at 2025 year-end, organic growth 3.2% (Item 7); 69,429 at
  2026-06-30, organic 2.6% annualized (Ex. 99.1). Contrary: single-family permits in the City of Maricopa fell 39% in
  2025, multi-family 46% (Item 7 table).
- **The low-cost position; the brand; the low bid** **[M2004-091]**, **[M2017-009]**: not applicable as tests of choice;
  the customer cannot choose. Water is "something that’s essential to people" **[M2004-091]**, and the franchise is
  exclusive.
- **Ask the competitors** **[M1999-130]**: no instance found in the filings read of a rival's view of this company.
- **Widening or narrowing** **[M1999-108]**. The franchise area is unchanged in its core (418 square miles) and grew by the
  Tucson systems (2025). The regulatory standing narrowed: the Southwest Plant cost was "prematurely included as "plant
  in service"" in three rate decisions (2010, 2014, 2022); the company itself "disclosed this circumstance to the ACC on
  March 1, 2024" (Note 3), and the bill credit is now being raised. The same regulator's Staff recommended increases for
  the rivals' Arizona water utilities in the same period (below), so the narrowing reads as this company's, not the field's.
- **What could destroy, modify or reduce it** **[M2000-014]**: (1) the regulatory climate: "the regulatory climate in a
  few states has raised the specter of zero profitability or even bankruptcy" **[L2023-011]** (carried OPEN in section
  VI); (2) condemnation, which has happened twice; (3) water: "our ability to serve new customers will remain dependent on
  our ability to access groundwater" (Item 1), with the smaller DAWS area "more constrained by state law"; (4) one
  municipality holds 81.9% of connections (Item 1A).

**The competitor row** (the 10-K names EPCOR Water Arizona Inc., Arizona Water Company, Central States Water Resources,
NW Natural Water Company, LLC, Ullico Inc., Liberty Utilities, Community Water of Arizona and Voyager Water Company; the
brief listed the first five. SEC filers among them or their parents: NW Natural Water through Northwest Natural Holding
(10-K) and Liberty Utilities through Algonquin Power & Utilities (40-F). Not filing with the SEC, flagged: EPCOR Water
Arizona (parent EPCOR Utilities, owned by the City of Edmonton), Arizona Water Company, Central States Water Resources,
Ullico Inc., Community Water of Arizona, Voyager Water Company.)

| Metric | GWRS | NWN Water (NWN 10-K FY2025, 0001733998-26-000012) | Liberty water, Algonquin (40-F FY2025, Ex. 99.3, 0001174169-26-000015) |
|---|---|---|---|
| Operating income / revenue 2023 | 23.2% (12,286 / 53,028) | 16.9% (6,569 / 38,852) | not separated in the filing (Regulated Services Group) |
| Operating income / revenue 2024 | 17.8% (9,364 / 52,692) | 19.1% (9,935 / 52,036) | not separated |
| Operating income / revenue 2025 | 12.8% (7,156 / 55,758) | 28.8% (18,906 / 65,646) | not separated |
| Capital spending / revenue 2023-2025 | 42% / 61% / 121% | 94% / 77% / 67% | not read |
| Revenue / segment assets 2025 | 11.5% (55,758 / 482,913 total assets) | segment assets "omitted" by the filer | 21.1% (net utility sales $400.0M / assets $1,895.4M) |
| ACC terms in Arizona | 9.6% ROE, 55/45 (2026 settlement); Staff first recommended a decrease | Foothills: 9.55% ROE, 55/45 (rates effective 2024-11-01) | Litchfield Park: Staff recommended +$14.5M at 9.45% ROE / 54% equity; settlement 9.75% / 54% |

The span is 2023 to 2025 only: NWN first reports its water business as a segment in the FY2025 10-K with two prior
years; earlier years sit inside "Other" and are not separable (NWN 10-K FY2023 read, 0001733998-24-000011). Algonquin
does not report a water operating profit. Over the span the GWRS margin fell each year while NWN Water's rose; on the
same regulator's terms the rivals obtained the ACC Staff's support for increases.

**The parts table:** one reportable segment (Note 18); every utility is ACC-regulated water or wastewater. No parts
reading is needed; the regulated whole decides.

**The field's returns over the last full cycle.** The field is regulated: its returns are set by the ACC at about 9.2%
to 9.75% on equity in the decisions above. The framework sends this case on: "A return set by a regulator is the
exception, carried to Q3 as a second best" (Q2, What it rules OUT), on "there’s no way we get rich on our
utility investments. But there’s no way we get poor, either." **[M2009-104]**, and on **[L2009-012]**. What GWRS itself earns on its capital
is weighed at Q3.

- **VERDICT: IN** **[M2011-015]**, **[M2009-104]**. The castle stands for the reason the filings give, an exclusive
  certificate and a cost of duplication no rival would pay; it is not shown open on the evidence, and its future is a
  regulated return whose level is judged at Q3 and Q7. Contrary, written down **[M1997-127]**: the regulatory standing of
  this company has narrowed (the Staff's recommended decrease, the Southwest Plant credit), the climate row **[L2023-011]**
  stays OPEN, and condemnation has twice ended a franchise.

## Q3: HOW MUCH CAPITAL MUST GO IN, and what does the added capital earn? WEIGHING.
- **What it has earned on the capital it needs** **[M1995-051]**, **[M2010-090]**. Operating income after tax (25.8%, the
  2025 effective rate) against average capital employed (shareholders' equity plus long-term debt, its current portion and
  the line of credit, less cash; developer advances and contributions left out because the owners did not supply them),
  from the filed statements (`_research 2026-10-28 GWRS/q3_returns.py`): **2021 4.0%, 2022 4.2%, 2023 6.1%, 2024 4.4%,
  2025 2.8%; mean 4.3%**. Earnings after depreciation against capital employed, the pairing the rows give for a utility:
  "It’s measured by the operating earnings after depreciation." **[M2014-086]**.
- **What the added capital earned** **[M2001-019]**. From 2020 year-end to 2025 year-end capital employed rose by $87.1M
  (from $129.2M to $216.2M); after-tax operating income was $5.4M in 2020 and $5.3M in 2025. The added capital earned
  nothing yet in operating earnings. "we’re not earning a higher rate of return on capital than we were when we started.
  We just put way more capital into the business" **[M2023-081]**. Part of the cause is the lag: the ACC sets rates on a
  historical test year (Item 7), and the GW-Palo Verde case, the larger utility by revenue, is withdrawn to 2027.
- **Reinvestment to stand still and to grow** **[L2000-035]**. Capital spending 2021-2025: $18.3M, $34.0M, $22.3M,
  $32.3M, $67.3M against depreciation and amortization of $9.5M to $15.0M; operating cash $20.2M to $25.4M. The business
  does not fund its own spending: the 2025 gap was met by $44.1M of share sales, $15.2M of new debt and developer cash
  (cash-flow statement). The proxy's incentive plan counts 2025 "Cap Ex" of $58.6M as excluding "new growth or acquisition
  Cap Ex" (DEF 14A 2026, Company Goals, Component 3), which, if read as the company's own split, puts most of the spending
  outside growth; the 10-K gives no split.
- **The regulated return, as a second best** **[M2018-055]**, **[L2009-012]**. The rows accept a capital-heavy regulated
  business only on "decent returns on the incremental sums they invest" **[L2009-012]**; "cash-consuming businesses, by
  their nature, are unattractive unless the cash they consume gets to earn a reasonable return" **[M2012-057]**. The
  allowed return is reasonable (9.6% on equity at 55% equity); what the owners' capital has actually earned is about 4%,
  and the regulated utility is the case where "To earn more, their owners must invest more." **[L2011-019]**.
- **The growth arithmetic and its caps.** Connections grew 3.2% organically in 2025; capital employed grew 34% in that
  year alone. No absurdity arises because no growth in earnings is shown to carry.
- **WEIGHS AGAINST** **[M2012-057]**, **[M2014-086]**, **[M2023-081]**: a second-best business by the rows' own ranking,
  earning about 4% after tax on the owners' and lenders' capital over five years, with the capital added since 2020 not
  yet earning anything in operating earnings. The "little or no debt" criterion is applied at Q9.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten year-ends, before the income account** **[M2025-032]** (USD millions; 2017-2025 from the
first-filed XBRL printed by `tools/run.py` and checked against the filed balance sheets of the FY2021 to FY2025 10-Ks; 2016
from the XBRL facts; AIAC and CIAC from the filed balance sheets and the XBRL facts):

| Year-end | Total assets | Equity | Long-term debt (incl. current) | Cash | Receivables | Advances in aid of construction | Contributions in aid, net | Retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2016 | n/r | 15.2 | 115.0 | 20.5 | n/r | 62.0 | 4.6 | n/r |
| 2017 | 238.6 | 14.9 | 115.1 | 5.2 | 1.5 | 62.7 | 4.4 | 0.4 |
| 2018 | 262.5 | 27.9 | 115.1 | 12.8 | 1.5 | 67.7 | 10.7 | 0 |
| 2019 | 266.1 | 24.7 | 115.0 | 7.5 | 1.6 | 67.6 | 14.5 | 0 |
| 2020 | 283.4 | 32.2 | 115.0 | 18.0 | 2.1 | 76.4 | 14.6 | 0 |
| 2021 | 294.1 | 30.0 | 113.1 | 12.6 | 2.0 | 84.6 | 21.3 | 0 |
| 2022 | 323.1 | 44.4 | 108.8 | 6.6 | 2.1 | 93.7 | 26.4 | 0 |
| 2023 | 361.1 | 48.6 | 105.6 (+2.3 line) | 3.1 | 2.8 | 111.5 | 36.4 | 0.8 |
| 2024 | 405.1 | 47.6 | 122.4 | 9.0 | 3.2 | 126.5 | 36.8 | 0 |
| 2025 | 482.9 | 86.6 | 133.7 | 4.1 | 3.7 | 155.4 | 37.9 | (1.0) |
| 2026-06-30 (10-Q) | 484.2 | 84.8 | 131.8 (+5.8 revolver) | 1.5 | 3.7 | 155.7 | 39.9 | (0.8) |

What the figures say, and what they cannot say **[M2025-032]**:
- **Equity was built by selling shares, not by keeping earnings.** Retained earnings sit at or near zero in every year:
  dividends exceed net income and the excess is charged to paid-in capital ("Dividend declared $0.30 per share" charged
  $4,398K to paid-in capital and $3,918K to retained earnings in 2025; statement of shareholders' equity, 10-K FY2025).
  Equity rose from $14.9M (2017) to $86.6M (2025) on share sales of $11.7M (2020), $14.8M (2022), $2.7M (2023) and $44.1M
  (2025) (cash-flow statements), with $10.0M more in August 2026.
- **The plant is funded largely by developers and lenders.** Net utility plant $441.9M (2025) against advances in aid of
  construction $155.4M (refundable from revenue over "the next two decades", Note 17), contributions $37.9M, ICFA deferred
  revenue $22.8M, debt $133.7M and equity $86.6M. Advances doubled from $76.4M (2020) to $155.4M, mostly plant "constructed
  by developers and conveyed" ($26.0M in 2025, Note 20). They are not counted as debt by the framework's definition of net
  debt (borrowings and finance leases), and the refunds ($1.4M in 2025, rising to an estimated $1.5M a year, Note 17)
  are inside the cash statements; written down here, weighed at Q9.
- **Cash fell to $1.5M at 2026-06-30** with $5.8M drawn on the revolver; debt was flat at $115M for seven years, then rose
  with the 6.91% notes (2024) and the 5.49% CoBank term loan (2025).
- **Receivables** rose from $1.5M to $3.7M while revenue rose from $31.2M to $55.8M: from 4.9% to 6.7% of revenue, with
  "Higher credit loss expense as a result of aging receivables" named in 2025 (Item 7). Small.
- **Goodwill and intangibles** are small ($6.5M and $6.1M); $3.0M of goodwill was reclassified to a regulatory asset in
  2025 on the ACC's deferral (Note 8).

**The real costs** **[L2015-004]**, **[L2021-003]**:
- Depreciation is a real cost and is charged; it rose 18% in 2025 with the plant placed in service (Item 7). The CEO
  calls it among "non-cash expenses" that "can affect near-term net income" (Ex. 99.1, 2026-08-12), which is the
  language the rows warn against for depreciation, "almost always true costs" **[L2015-004]**; for a utility the charge
  is recovered in rates only after a rate case.
- Stock pay is small ($0.9M to $2.9M a year, "Deferred compensation" / "Share-based compensation" add-backs, 2021-2025)
  and is charged in full in the owner cash below.
- No recurring restructuring. A $1.25M loss on disposals in 2025 on the Southwest Plant recommissioning (Note 19).
- **Non-utility income inside the earnings and the operating cash:** Buckeye growth premiums from the 2015 condemnation of
  Valencia, $1.4M / $2.5M / $2.4M / $2.9M / $2.4M (2021-2025, 10-Ks FY2021 and FY2023 Note 1, FY2025 Note 19), for "a
  20-year period ending December 31, 2034, subject to a maximum payout of $45.0 million", $16.1M received to date. They
  end inside ten years and are valued apart at Q7.
- **ICFA revenue** is recognized from deferred revenue when a facility is commissioned: $2.1M of "unregulated revenue" in
  Q2 2026, non-cash in that quarter (10-Q Q2 2026, cash-flow statement). Lumpy; outside the window's figures.

**EBITDA in the filer's own mouth.** The earnings release features "Adjusted EBITDA, a non-GAAP measure" as a highlight,
defined to exclude restricted stock expense and ICFA revenue (Ex. 99.1, 2026-08-12); the CODM reviews "EBITDA and
Adjusted EBITDA" (Note 18); the officers' bonus pays on "Further Adjusted EBITDA", which excludes share-based pay, the
Buckeye earnout and AFUDC (DEF 14A 2026, Component 2). "The one figure we regard as utter nonsense is the so-called
EBITDA" **[M1998-086]**; an adjusted figure featured is weighed here and carried to Q5 **[L2016-006]**, **[M1994-018]**.

**An inconsistency recorded.** Cash paid for interest for 2022 is stated as $11,355K in the FY2022 10-K (Note,
supplemental cash flow) and as $1,450K "net of amounts capitalized" in the FY2023 10-K for the same year, against interest
expense of $4,036K (as first filed) or $4,759K (as restated in the FY2023 10-K) and coupons of about $5.2M on the notes. A
supplemental line, not the statements; knowable from the filings; not used in any figure below (interest expense is used).

**The recast owner cash for Q7** (equity-only, after interest and the company's tax; USD thousands; `q7_calc.py`):
OCF less stock pay, less finance-lease principal, less the Buckeye premiums, less (a) depreciation and amortization as the
maintenance guess **[M1998-127]**, or (b) all capital spending and acquisitions:

| | 2021 | 2022 | 2023 | 2024 | 2025 | Mean |
|---|---|---|---|---|---|---|
| (a) after maintenance guess | 6,465 | 9,418 | 9,706 | 4,847 | 1,496 | **6,386** |
| (b) after all spending | (4,363) | (14,857) | (7,415) | (14,907) | (58,925) | **(20,093)** |

- **VERDICT on the accounts: WEIGHS AGAINST** **[M1994-018]**, **[L2016-006]**. The statements are audited (Deloitte;
  critical audit matter on rate regulation), readable and not confusing; no tell in the accounts rises to suspicion
  **[M1995-065]** (no prepaid or deferred accounts building, reserves not moving with share sales). Against: the adjusted
  EBITDA featured and paid on, depreciation called non-cash in the release, and the 2022 interest-paid inconsistency.
  The habit of the featured adjusted figure is carried to Q5.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The people.** Ron L. Fleming, CEO since May 2015 and chairman, with the company since 2004 (COO, VP and GM 2007-2014);
  Michael J. Liebman, CFO (DEF 14A 2026). Control: the Levine family through Levine Investments LP holds 42.3% and director
  Andrew Cohn 9.1%; officers and directors as a group 53.7% (DEF 14A 2026, beneficial ownership). A standstill agreement
  of 2021 keeps the family below "control" under the ACC rules.
- **The two yardsticks** **[M1994-008]**. *How well they run it, against the hand dealt:* the hand is a regulated monopoly
  in a fast-growing metro area at an allowed 9.2% to 9.6% ROE; what the owners' capital earned was about 4% after tax over
  five years (Q3), and the margin fell each year from 2023 to 2025 while NWN Water's rose under the same regulator (Q2
  row). *How they treat the owners:* modest pay (CEO total $819,403 in 2025, DEF 14A Summary Compensation Table);
  directors buy shares with their own money (below); dividends paid beyond earnings with share sales (Q6).
- **The tells, read** **[M1995-111]**, **[M2007-082]**.
  - *The Southwest Plant.* About $7.8M of construction cost was carried as plant in service for ratemaking from 2007,
    reflected in rates in decisions of 2010, 2014 and 2022, during which the present CEO was COO, then CEO. The company
    "discovered" it in January 2024, "disclosed this circumstance to the ACC on March 1, 2024", and itself applied for a
    customer bill credit, approved 2024-07-18 (10-K FY2025, Note 3); the 2026 settlement raises the credit by about $0.4M a
    year (8-K 0001628280-26-028741). Read as the rows read conduct after bad news: "tell us the bad news immediately"
    **[M1998-039]**; the failing case is a management that "didn’t act when they learned about it" **[M2017-005]**. Here
    they acted within two months and against their own revenue. The facts read do not show that the inclusion was intended.
  - *Candour on adverse facts.* The 10-K states the Staff's recommended revenue decrease and that the positions "could have
    a material adverse impact" (Item 7). For.
  - *The habits carried from Q4.* Adjusted EBITDA featured as a highlight in the releases and used for the bonus;
    depreciation described as "non-cash expenses" affecting "near-term" income (Ex. 99.1). No earnings guidance found in the
    release or the 10-K read; no habit of beating declared targets found. Read with the record: a weighing against, not a
    doubt about honesty **[M1994-018]**.
  - *Filings by insiders.* Thirteen officers and directors filed Section 16 reports late, Mr. Cohn nine forms (DEF 14A
    2026, Delinquent Section 16(a) Reports). Carelessness, recorded.
  - *Related-party dealings.* The family and Mr. Cohn bought in the March 2025 offering at the public price ($10.00) and in
    the placements of September 2025 ($10.30) and August 2026 ($8.85), each "equal to the consolidated closing bid price"
    (8-Ks 0001628280-25-044355 and 0001628280-26-058486). The medical plan is pooled with Camelback Systems, of which Mr. J.
    Levine is President ($2.6M of claims in 2025, Note 16). Neither shows a transfer from the other owners at an off-market
    price.
- **Love of the business; the same after being paid.** A long-tenured operator who came up through the construction of
  the plant; the employment agreements give fixed RSA grants (DEF 14A). No evidence either way beyond tenure.
- **VERDICT on integrity: IN**, **[M2013-088]** applied: the doubts recorded above go to competence and control (a rate-base
  error carried fourteen years, late filings), not to honesty; the decisive fact is that the company found and disclosed
  the error against its own revenue. A reader who takes the fourteen years as doubt about honesty would close the file
  here; the facts are written down for that reader. **Ability WEIGHS AGAINST** **[M1994-008]**: about 4% earned on capital
  against an allowed return more than twice that; the largest rate case withdrawn after the Staff recommended a decrease;
  a margin falling while a rival's rose under the same regulator.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- **Retention test** **[M1998-033]**, **[R1995-009]**. Nothing is retained: dividends paid 2021-2025 total $36.2M ($6.6M,
  $6.9M, $7.2M, $7.3M, $8.2M) against net income of $25.8M ($3.6M, $5.5M, $8.0M, $5.8M, $3.0M), the excess charged to
  paid-in capital (statements of equity). The fixed monthly dividend ($0.30396 a year) is paid while the business needs
  more cash than it makes and sells shares to get it. "a company that expects to regularly earn more than it can
  profitably employ in its business, should be paying out dividends" **[M2004-089]**; this company earns less than it
  employs, and the rows put "the internal need for funds" first **[L2016-003]**. The dividend comes back in as equity
  sold at a cost (2025 offering: $32.2M gross, $30.8M net, Note 9).
- **Issuance** **[R1995-010]**, **[L2014-015]**. Shares sold at $12.50 (January 2020), $13.50 (August 2022), $12.07 (June
  2023), $10.00 (March 2025), $10.30 (September 2025), $8.85 (August 2026); an S-3 shelf filed 2026-08-07 (accession
  0001628280-26-054889); the revolver's limit falls from $30M to $25M if the company "completes any capital market
  activity" (8-K 0001628280-26-059647), so more issuance is contemplated in the lender's terms. Six sales in seven years
  is the pattern the rows name: "we have never invested in companies that are hell-bent on issuing shares" **[L2014-015]**,
  carried in the framework as a candidate second STOP whose status is unresolved (section VI); applied here as a weighing,
  heavily against. Measured as value given against value got **[R1995-010]**: every sale price sits above the top of the
  Q7 range below, so the sales did not transfer value from the continuing owners; the objection is the habit and what it
  funds, not the price.
- **Buybacks.** None; the only purchases are shares withheld for employees' taxes (Item 5). The Q6 buyback test against
  the bottom of the Q7 range has nothing to test (written back at Q7).
- **Deals** **[M1995-001]**. Small cash acquisitions: Farmers (2023, $6.2M cash plus a growth premium up to $3.5M) and the
  Tucson systems (2025, $8.1M for a $7.7M rate base, Note 2). No deal paid in shares; Q6's STOP **[L2009-019]** does not
  arise.
- **Part A WEIGHS AGAINST** **[L2014-015]**, **[L2016-003]**: a dividend beyond earnings funded by serial share sales.

**Part B, the pay, the board and the owners.**
- **Pay tied to what the person controls** **[M2003-019]**. The 2025 incentive pool: 25% compliance and safety, 25%
  "Further Adjusted EBITDA" against a $24.3M budget (excludes share-based pay, AFUDC and the Buckeye earnout), 25% capital
  projects "completed on schedule and within budget" ($58.6M spent against $65.9M), 25% board discretion (DEF 14A 2026).
  Nothing pays on the return earned on the capital; a quarter pays on getting the capital spent. "you get what you reward
  for" **[M2016-083]**. The sums are small.
- **The board** **[M2007-120]**, **[L2014-026]**. The CEO is chairman; there is a lead independent director. Four of seven
  are called independent; one of the four, Mr. Huckelbridge, manages money for which the controlling family's partnership
  "provides a significant portion of the assets under management" (DEF 14A 2026); the rows look past the label: "A
  director getting $150,000 a year from a company, who needs it, is not an independent director." **[M2005-090]**, here
  by analogy, the payer being the controlling holder.
- **The owners as partners.** Directors Levine and Cohn bought shares with their own money at market prices, "with their
  savings" **[L2019-008]**: for. Adjusted EBITDA talked to the owners in the releases: against.
- **Part B WEIGHS AGAINST** **[M2016-083]**, **[M2005-090]**, with the directors' own purchases for.

## Q7: WHAT IS IT WORTH? STOP.
**Which basis.** Q7's regulated-utility section applies "Where the deciding part of a business (Q2, a business of parts)
earns a return a regulator allows on its invested capital": all of GWRS's revenue in 2025 was ACC-regulated (Item 1, "Revenue
from our regulated utilities accounted for all of our total revenue in 2025"), one segment, and the ACC sets "a fair and
reasonable cost of equity" on rate base (Item 7). "when you get an allowed return in the electric utility you’re almost
certain of earning it" **[M2010-037]** speaks of electric utilities; this company has not earned its allowed return (Q3),
which is weighed below, but the return is a regulator's. So the **equity-only basis is central** **[L2017-012]**, with the
all-equity basis beside. The 2026 Q2 "unregulated revenue" ($2.1M of ICFA revenue) falls after the window and is not used.

**The inputs** (`_research 2026-10-28 GWRS/q7_calc.py`, output `q7_out.txt`; USD thousands unless stated):
- Owner cash, equity-only, five-year window 2021-2025, from Q4's table: after the maintenance guess, mean **6,386**; after
  all spending, mean **(20,093)**. Both after interest and the company's own tax as paid (no carryforwards: "the Company
  has no net operating loss carry forwards", Note 14), after stock pay and finance-lease principal.
- **The maintenance guess** **[M2000-144]**, **[L1999-024]**: depreciation and amortization, "not inappropriate in most
  companies to use as a proxy for required capital expenditures" **[M1998-127]**, the plant of the two main utilities
  being "less than twenty years old" (Item 1). Against it, written down: the proxy counts $58.6M of 2025 spending as
  excluding "new growth or acquisition Cap Ex" (DEF 14A 2026), which, read literally, puts that year's non-growth spending
  near four times depreciation. The 10-K makes no split. The central case uses depreciation, the all-spending case is shown
  beside, and the proxy's reading would put the central case below the all-spending side, not above it.
- **The Buckeye premiums, valued apart.** CONVENTION of this run: the City of Buckeye's growth premiums ($3,000 a meter,
  "for a 20-year period ending December 31, 2034, subject to a maximum payout of $45.0 million", $16.1M received, Note 19)
  are taken out of owner cash and valued as their own stream of nine years (2026-2034) at the window's mean of $2,326K a
  year (total $20.9M, inside the $28.9M remaining cap); rationale: Q7's own rule prices separately a shelter "that runs out
  inside ten years", and this non-utility income runs out the same way, so it is not carried into the perpetuity. PV at
  5.30%: $16.3M; at 10%: $13.4M.
- **Growth shown** (aggregate, specific (b)): owner cash after maintenance fell from 6,465 (2021) to 1,496 (2025),
  **-30.6% a year** compound; by halves, 7,942 (2021-2022) to 3,172 (2024-2025), also a decline. The filer does not
  describe 2025 as aberrational; it names the rise in depreciation from "our 2025 capital expenditure program" and the
  regulatory lag (Item 7). Specific (b): the decline is the bottom of the range, the no-growth case the top. The inversion
  is the finding: the growth spending has not bought growth in owner cash in the window, "growth can destroy value"
  **[L2000-023]** where the return on the added capital stays below its cost.
- **Growth spending** (specific (e), 2026-10-23): capital spending and acquisitions above the maintenance guess, window
  mean **26,480** a year; in the growth case it moves at the growth rate carried and stops after year ten: **$18,366K in
  year one, $682K in year ten**, none after. (The rule grows it "at the growth rate carried"; carried at a negative rate
  it shrinks. Recorded under What was unclear.)
- **The utility debt credit** (2026-10-23): long-term debt with its current portion and finance leases rose from $115,003K
  (2020 year-end) to $134,877K ($133,698K carrying plus $1,179K finance leases, 2025 year-end): **$3,975K a year**,
  credited against the growth spending only, moving with it ($2,757K in year one). Cap: the allowed debt share of the
  deciding part, **45%**: the 2026 GW-Santa Cruz settlement states "a capital structure of 55% common equity/45% debt" (8-K
  0001628280-26-028741) and the 2024 decision for seven utilities a capital structure "matching the Company’s previous
  rate of 55% equity" (10-K FY2023); 45% of the growth spending is $11,916K, so the cap does not bind. The revolver
  ($5.8M at 2026-06-30) is short-term borrowing and is left out.
- **Rate** 5.30% (Step 0). **Shares** 29,925,296. **Price** $7.74; market value **$231.6M**.

**The floor, tested first** (Q7, 2026-10-10) **[M2003-149]**. The best case at the price is the no-growth maintenance case:
owner cash 6,386 plus the Buckeye mean 2,326 = $8.7M a year on $231.6M, **3.8%**. Every other case is lower: the growth case
and the all-spending case are negative; the all-equity top case earns **3.5%** on market value plus net debt. Two checks
that are not cases, written down because they are the most favourable readings the filings allow: adding the developers'
net cash (advances and contributions received less refunds, mean $4,740K) to the top case gives **5.8%**; and the full
allowed return on an approximate rate base (net plant $441.9M less advances, contributions, deferred income taxes and ICFA
deferred revenue = $216.1M, times 55% equity times 9.6%) is $11.4M, **4.9%** of the market value, before any spending. **No
case earns the floor of about ten percent at the price. The file closes OUT on the floor, whatever the width.**

**The value range** (reported at the owner's request; Q7's construction):

| Basis | Bottom (decline case, growth spending and credit charged to year ten) | Top (no growth, maintenance only) | Literal window, all spending (beside) |
|---|---|---|---|
| **Equity-only (central, regulated utility)** | **-$0.42** a share (-$12.5M) | **$4.57** a share ($136.8M) | -$9.62 a share |
| All-equity (beside): owner cash before interest (after-tax interest $3,993K added), less net debt $127.3M | -$4.63 | $2.84 | not computed |

Net debt for the all-equity basis: long-term debt $127,828K plus current $3,947K plus revolver $5,800K plus finance leases
$1,179K (2025 year-end split, the latest stated), less cash $1,458K (10-Q 2026-06-30), less the $10.0M placement proceeds of
2026-08-20 (the shares are in the count): **$127,296K**. Operating leases left out, said so; advances in aid of
construction ($155.7M, refundable from revenue) left out by the framework's definition and weighed at Q9.

- The price ($7.74) sits above the top of the central range ($4.57): OUT by the floor convention as well
  **[M2003-149]**, and "if you have to actually do it on — with pencil and paper, it’s too close to think about"
  **[M1996-084]** does not arise, since no pencil finds the price below value.
- Width: not tested (the floor closes first).
- **Q6 written back:** no buybacks; the buyback test against the bottom of the range ($-0.42) has nothing to test.

**Fair price (a reporting figure, never a verdict; Part VII):** each end valued at ten percent and the two averaged, after
the company's own tax. **Equity-only (central, regulated utility): $1.07 a share** (top $2.58, bottom -$0.44). All-equity
(beside): **-$2.51 a share** (top -$0.34, bottom -$4.68): not positive. Growth spending $18,366K in year one, $682K in
year ten, none after (specific (e)). Utility debt credit: long-term debt increase $3,975K a year, against growth spending
only, cap 45% (the deciding part's allowed share, from the filings named above).

- **VERDICT: OUT** **[M2003-149]**, **[M2009-005]**: no case of the range earns the floor of about ten percent at $7.74; the
  price is above the top of the central range.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9: COULD IT RUIN US? WEIGHING.
NOT REACHED.

## Q10: IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7** (the floor, tested first): no case earns about ten percent at $7.74. Value range, equity-only (central,
regulated utility) **-$0.42 to $4.57** a share against **$7.74**; all-equity beside -$4.63 to $2.84. Re-look condition
(Part VII, like any OUT): the top of the computed range, $4.57.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged; operator rule 2; **[M1997-127]**.)*
- **Q8, the bond.** The 30-year Treasury yields 5.30% (Step 0); the best case of the range earns 3.8% on the market value
  (Q7).
- **Q9, the target's debt and exposures.**
  - Long-term debt $131.8M at 2026-06-30 plus $5.8M on the revolver; equity $84.8M (10-Q). Pre-tax earnings over interest
  **[L2012-002]**: 2025 (3,983 + 5,964) / 5,964 = 1.7 times; 2024 (7,862 + 6,098) / 6,098 = 2.3 times (10-K FY2025).
  - Maturities: $3.9M a year of Series B principal; the $28.75M Series A notes due June 2028; the revolver now due
    2028-08-30 (8-K 0001628280-26-059647); the 6.91% notes balloon in January 2034 (Note 10).
  - Covenants: debt service coverage on "consolidated EBITDA" of at least 1.10, dividends limited below 1.25; the notes
    are "collateralized by a security interest in the Company’s equity interest in its subsidiaries" (Note 10).
  - Advances in aid of construction $155.7M, refundable from revenue on developer-built plant, "Portions of these refund
    amounts are payable annually over the next two decades", estimated $1.5M to $1.7M a year to 2030 (Note 17).
  - One municipality holds 81.9% of connections; one aquifer system and the DAWS permits govern growth (Item 1A).
  - The "little or no debt" criterion **[R1997-001]** is stated for whole businesses offered; the part-interest case is
    the one Q9 weighs.
- **Q10.** Nothing.
- **Q12.** Water and wastewater service; nothing named by the rows.
No integrity facts left unjudged: Q5 was reached and answered.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `c1c35afa`); written question by question; committed after each
      question (Q1 `976b9645`, Q2 `44972819`, Q3 `5d8c7172`, Q4 `a6e2feec`, Q5 and Q6 together `c184a6df`, Q7 `8062f029`,
      the close in the final commit). **Departure:** Q5 and Q6 were committed in one commit, not one each (a failed shell
      append; the two were drafted together). **Departure:** the Q7 and Q3 arithmetic scripts were written and run, and
      `q7_calc.py` with its first output was committed with Q1, before Q2 to Q6 were written; the Q2 to Q6 verdicts were
      written after seeing that output. Declared, not repaired. The Q7 section was itself written only after Q6 closed.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's (not checked by
      this analyst); the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under contamination at the top and not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `_research 2026-10-28 GWRS/check_ids.py` (ids exist, no
      E-ids, every quoted fragment beside an id found in that row); every filing fact carries its accession or names its
      filing and note.
- [x] The order was kept; Q1 to Q6 answered before Q7 was written; Q7 (a STOP) closed the file; Q8 to Q12 NOT REACHED.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): operating cash less stock pay, finance-
      lease principal and capital spending (maintenance guess or all); the sovereign from the US Treasury; the price an
      aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations, Q2, Q3, Q5); the facts for later questions are under AFTER
      THE STOP.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` used (its debt-plus-equity column rejected, said so).
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the reply).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Specific (e) at a negative rate.** The growth spending "grows at the growth rate carried for the ten years"; where
the shown growth is a decline (specific (b)), carrying it literally shrinks the growth spending by 30.6% a year, so the
decline case charges less spending each year as owner cash falls. The text was written for a positive rate; I applied
it literally, and it does not decide the box (the floor fails on every case). A rule for the negative case is wanted:
hold the spending flat, or charge none and treat the decline as the price of the spending already made. (2) **The
regulated-utility section for a utility that does not earn its allowed return.** The section moves the central figure to
the equity-only basis on the reasoning that the allowed return is "almost certain" **[M2010-037]**; this company earned
about 4% on capital against an allowed 9.6% on equity, and the equity-only basis with a debt credit then values the
business at more than the all-equity basis. The text does not say whether the swap still applies when the allowed
return is shown not to be earned; I applied it because the return is still the regulator's. (3) **Maintenance guess
against the company's own split.** The proxy calls most of the 2025 spending non-growth, which would make depreciation
a poor proxy; Q7 does not say whether a proxy-statement label may serve as "the filing" that allows or forbids the
guess. (4) **Non-utility income that ends inside ten years** (the Buckeye premiums) has no rule; I confessed a
CONVENTION of this run by analogy to the carryforward rule. (5) **Developer-funded plant** (advances and contributions in
aid of construction, $193M) has no place in the framework's net debt or owner cash; I left it out of both and showed
the developer cash beside the floor test. (6) **Serial issuance** **[L2014-015]** remains a candidate STOP with no
ruling; six share sales in seven years were weighed, not closed on.

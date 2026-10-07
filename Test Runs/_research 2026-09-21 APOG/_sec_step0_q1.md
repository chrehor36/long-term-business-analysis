
---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34%** · date **2026-09-18** · source **US Treasury daily par yield curve, 30-year,
  from the issuing authority** (`python tools/sources.py`, struck fresh in this run; FRED DGS30
  not used — it is the fallback, not the source).
- **Currency argued from the filing, not assumed.** The FY2026 10-K reports in USD and the
  business is overwhelmingly North American: *"We primarily supply architectural glass products
  and aluminum framing systems, including window, curtainwall, storefront and entrance systems,
  to customers in North America"* (FY2026 10-K, Item 1). The one foreign-currency operation of
  size is the Canadian Alumicor business plus European/Asian distribution of coatings; the
  filing's own market-risk item names **aluminum and lumber** as the exposures it quantifies and
  does not present FX as a material driver. **USD is the earnings currency. FX ENTERS THIS FILE
  ON A DATE CERTAIN AND IT IS IN THE FUTURE, NOT THE PAST:** the GroGlass purchase agreement of
  2026-09-02 is denominated in **euro** (€62.5 million including up to €10 million of earn-out)
  for a Latvian operating company. That is a post-balance-sheet perimeter change, recorded at Q1
  and Q4, not a re-denomination of the historic series.
- FX if the quote and the earnings differ in currency: **n/a — both USD.** ADR ratio: **n/a.**

**THE PRICE, THE SHARES AND THE CAP — STRUCK BY HAND [operator rule 5]**
- **Price US$36.80**, close of **2026-09-18**, the last trading day before this run (2026-09-21
  is a Monday and the run was dispatched before the open). **Aggregator quote, flagged as such**
  — Yahoo Finance chart endpoint — raw responses on disk at
  `Test Runs/_research 2026-09-21 APOG/yahoo_APOG_chart.json` and `yahoo_APOG_6mo.json`.
- **Shares 20,868,294**, from the cover of the **10-Q for the quarter ended 2026-05-30
  (Q1 FY2027), accession `0000006845-26-000063`, filed 2026-06-30**, verbatim:
  > *"As of June 25, 2026, 20,868,294 shares of the registrant's common stock, par value
  > $0.33 1/3 per share, were outstanding."*

  The `dei:EntityCommonStockSharesOutstanding` fact on that accession carries the same number
  (20,868,294, measured 2026-06-25). **One class of common only**; the Junior Preferred plan has
  *"zero shares issued and outstanding as of May 30, 2026."*
- **No splits** in the Yahoo split-event series or anywhere in the seventeen fiscal years of
  filings read, so `cap = close × shares from the newest cover × splits after that measurement`
  reduces to close × shares.
- **CAP, HAND-STRUCK: 20,868,294 × $36.80 = US$767,952,219 ≈ US$768.0M.** Every yield in this
  file uses **$768M**. The screen's $787M is **2.5% high and is NOT a share-count error** — see
  flag (i).

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **Form 10-K for fiscal 2026 (year ended 2026-02-28), filed
  2026-04-24, accession `0000006845-26-000023`**; the **10-Q for Q1 FY2027 (quarter ended
  2026-05-30), accession `0000006845-26-000063`**; and six 8-Ks listed below.
- **figures cross-checked against the filed statement:** the CONSOLIDATED STATEMENTS OF CASH
  FLOWS in the FY2026 10-K reads **"Net cash provided by operating activities | 122,465 |
  125,162 | 204,154"**, **"Capital expenditures | ( 27,308 ) | ( 35,593 ) | ( 43,180 )"**,
  **"Depreciation and amortization | 49,998 | 44,608 | 41,588"** and **"Acquisition of business,
  net of cash acquired | — | ( 232,169 ) | —"** ($000). All four agree to the dollar with the
  XBRL facts used to build the owner-earnings series at Q4. The $232.2M acquisition line is the
  one the screen's `acq_note` points at, and it is real.

### THE DEAL ON FILE — resolved from the documents. The screen's note is NINETEEN DAYS STALE AND ONE DEAL SHORT.

The screen's `deal_note` reads: *"M&A AGREEMENT ON FILE: EX-2.1 (plan of merger or acquisition)
with the 8-K Item 1.01 of 2026-05-28 (0000006845-26-000044). It is filed by the TARGET and the
ACQUIRER alike - READ IT: if this company is being bought the quote is a SPREAD, if it is buying
the perimeter changes [ACVA, 2026-09-13]."* I read the Item 1.01 text itself rather than
inferring from the exhibit type, and checked EDGAR for everything filed since instead of
trusting `newest_filing`.

**APOGEE IS THE ACQUIRER, NOT THE TARGET. The quote is a price for a business, not a spread.**
From the 8-K of 2026-05-28 (accession `0000006845-26-000044`, period 2026-05-27), Item 1.01,
verbatim:
> *"On May 27, 2026, Apogee Enterprises, Inc. (the "Company") entered into a Merger Agreement
> (the "Merger Agreement") with Keller Companies, Inc. ("KCI") and KCI's shareholders (the
> "Sellers"). KCI is the controlling shareholder of Kalwall Corporation ("Kalwall") and
> Structures Unlimited Inc. ("SUI"). … the Company has agreed to acquire all of the outstanding
> equity interests of KCI from the Sellers pursuant to a merger in which KCI will survive as a
> wholly owned subsidiary of the Company"*

— consideration *"an amount in cash equal to approximately $105 million"* plus *"up to an
additional $10 million in post-closing earn-out consideration"*, financed *"with cash on hand
and funds available under its existing credit facility."*

**THE SCREEN'S NOTE IS STALE IN BOTH DIRECTIONS.** Checking EDGAR rather than the CSV's
`newest_filing 2026-02-28` found two later events the screen cannot have seen:

1. **THE KALWALL DEAL CLOSED.** 8-K filed 2026-07-01, accession `0000006845-26-000068`, **Item
   2.01 Completion of Acquisition or Disposition of Assets**: *"On July 1, 2026, Apogee
   Enterprises, Inc. … completed the transaction contemplated by the Merger Agreement, dated
   May 27, 2026 … in exchange for cash consideration consisting of $105 million paid at closing
   … and up to an additional $10 million of contingent consideration based on the future
   financial performance of the Acquired Companies."* Funded *"using available cash and
   borrowings under its existing revolving credit facility."* The EX-99.1 values it *"at up to
   $115 million."*
2. **A SECOND, LARGER DEAL WAS SIGNED AND IS STILL PENDING.** 8-K filed 2026-09-03, accession
   `0000006845-26-000087`, Item 1.01, with its own EX-2.1: *"On September 2, 2026, Apogee
   Enterprises, Inc. … entered into a Share Purchase Agreement … to acquire 100% of the issued
   and outstanding equity interests of SIA "Alzette", a Latvian limited liability company …
   Alzette owns 100% of the equity interests of SIA "GroGlass" … the Transaction values Groglass
   at approximately €62.5 million on a cash-free, debt-free basis … The maximum contingent
   consideration payable pursuant to the earnout provisions is €10 million."* Expected to close
   *"during the Company's third quarter of fiscal 2027"*, financed *"with cash on hand and
   borrowings under its existing credit facility."* The press release puts it at *"approximately
   $72.5 million at current exchange rates."*

**WHAT THAT DOES TO THE ARITHMETIC, SAID PLAINLY.** The perimeter has changed twice since the
last audited year-end and will change a third time before the next one.
- **The DENOMINATOR — the $768M cap — is today's equity claim on a company that has already
  paid out $105M of cash and revolver for Kalwall and is committed to roughly $72.5M more for
  GroGlass.** That is **$177.5M of purchase price, 23% of the hand-struck cap, spent or
  committed in four months, and none of it is in the FY2026 balance sheet** the owner-earnings
  series is built on. The cap does not shrink when the cash leaves; the debt behind it grows.
- **The NUMERATOR — the FY2022-FY2026 owner-earnings mean — contains no day of Kalwall and no
  day of GroGlass**, and the window is contaminated the other way as well: **$232.2M was paid
  for UW Solutions in FY2025** (filed cash-flow line, above), so FY2025 and FY2026 owner
  earnings already include a business FY2022-FY2024 do not.
- The screen's own `acq_note` — *"acquisitions are $232M, 30% of cap, inside the window - the
  numerator and denominator may be different compani[es]"* — is **RIGHT, AND IT UNDERSTATES
  ITSELF.** Counting the two 2026 deals the figure is **$409.7M, 53% of the hand-struck cap**,
  inside or immediately after the five-year window; and across the full seventeen-year series
  filed acquisition spend is **$626.9M** (FY2011 $20.6M, FY2014 $53.3M, FY2017 $137.9M, FY2018
  $182.8M, FY2025 $232.2M).
- **The [E4-38] remedy is therefore mandatory here, not optional:** no single window describes
  one company. Every window is published at Q4 and the spread is carried as part of the range
  **[E4-25]**.
- **ACVA precedent, applied and distinguished.** ACVA of 2026-09-13 was the *target* branch —
  *"ACV is a pending Copart acquisition at $10.50"* — and that file still closed on the business
  at Q2. APOG is the **other** branch of the same note: the acquirer. There is no deal price to
  price against; the quote is the business, and the business is a different business each year.

**EVERYTHING FILED SINCE THE SCREEN DATE**, checked on EDGAR (`submissions.json` saved to the
research folder) rather than taken from `newest_filing 2026-02-28`: 8-K 2026-09-14
(`0000006845-26-000091`, Items 5.02/7.01), 8-K 2026-09-03 (GroGlass, above), S-8 2026-08-20,
8-K 2026-08-05 (`0000006845-26-000070`, Item 5.02), 8-K 2026-07-01 (Kalwall close), 10-Q
2026-06-30 (`0000006845-26-000063`), 8-K 2026-06-29 (Item 5.07), **8-K 2026-06-26
(`0000006845-26-000058`, Item 2.02 — the Q1 FY2027 earnings release, read at Q3)**, DEF 14A
2026-05-12 (`0000006845-26-000036`), 10-K 2026-04-24 (`0000006845-26-000023`), **8-K 2026-04-24
(`0000006845-26-000020`, Item 2.02 — the Q4/FY2026 earnings release, read at Q3)**. **The CSV's
`newest_filing 2026-02-28` is a REPORT date, not a filing date; the newest actual filing on
2026-09-21 is 2026-09-15.**

### THE SCREEN'S OTHER FLAGS, EACH RESOLVED BY HAND AND SCORED

**(i) `cap_flag` — "cap $787M against a filed float of $915M (1.16x) as of 2025-08-29. A cap
cannot be smaller than a subset of itself. One of the two is wrong." → WRONG ABOUT "ONE OF THE
TWO IS WRONG"; RIGHT TO SEND ME TO RE-STRIKE. This is the CALM / EMBC / BRBR / FC branch: THE
TWO DATES DIFFER.** The FY2026 10-K cover reads, verbatim:
> *"As of August 29, 2025, the last business day of the registrant's most recently completed
> second fiscal quarter, the approximate aggregate market value of voting and non-voting common
> equity held by non-affiliates of the registrant was $ 915,200,000 (based on the closing price
> of $43.98 per share as reported on The Nasdaq Stock Market as of that date)."*

$915,200,000 ÷ $43.98 = **20,809,459 implied non-affiliate shares** against **21,220,737**
outstanding on the same cover as of 2026-04-17, so **affiliates hold on the order of 2% and
essentially the whole company is float.** The entire 1.16x is **twelve and a half months of
price and buyback**: $43.98 → $36.80 is **−16.3%**, and the count fell 21,220,737 → 20,868,294
(−1.7%) in the single quarter to 2026-06-25 on 269,500 shares repurchased for **$9.7 million**
(10-Q, repurchase-authorization note). Those two together reproduce the 1.16x to within
rounding. **I second the MGPI and FC runs: this diagnostic should say "or the two dates differ."
This is the fifth consecutive run in which it has meant exactly that and not a data error.**

**NEW, AND IT REFUTES A PRIOR: THE FC DEFECT (i-a) DOES NOT REPRODUCE HERE.** FC's run of
2026-09-21 found the screen pricing off the **stale annual cover** when a newer 10-Q cover
existed, overstating the cap by 18%, and warned it would recur on every buyback filer. Tested on
APOG: the screen's $787M against the **10-Q** count of 20,868,294 implies **$37.71**, and
against the **annual** count of 21,220,737 implies **$37.09**. The closes on the screen's own
dates were **$37.59 (2026-09-01)** and **$38.06 (2026-09-02)**, which bracket $37.71 and do not
bracket $37.09. **The screen used the newer 10-Q cover count on this row.** The whole of the
$787M → $768M gap (−2.4%) is nineteen days of price, and it points the safe way — the screen
made the name look **dearer** than it is. **The FC defect is real but it is not universal; it is
a per-row question, and this row is clean.**

**(ii) `level_shift` 1.34 "no step" against `level_shift_oe` 1.69 "STEP UP - normalize down
[E4-41]" → BOTH RIGHT, AND THE OE ONE IS THE ONE THAT MATTERS.** On the seventeen-year filed
series (Q4 table) the OCF level drifts up modestly; the **owner-earnings** level steps hard, and
the step has a name: **FY2024**, where OCF was $204.2M against a seventeen-year mean of $97.7M.
Owner earnings that year were **$152.9M** on the D&A end against a five-year mean of $76.6M —
**twice the mean, in one year.** [E4-41] is the corpus's instruction for exactly this and it is
obeyed at Q4: the mean is normalized down and every window is published.

**(iii) `best_year_dep` 0.079 "no single-year dependence (9-yr OCF series)" against
`best_year_dep_oe` 0.121 → THE PAIR CONTRADICTS ITSELF AND THE OE ONE IS CORRECT; AND
`flags_disagree` IS EMPTY WHEN IT SHOULD HAVE FIRED.** On the series rebuilt by hand, dropping
FY2024 moves the FY2018-FY2026 owner-earnings mean from **$69.5M to $59.1M (−15.0%)** and the
FY2022-FY2026 mean from **$76.6M to $57.5M (−24.9%)**. A quarter of the five-year
owner-earnings mean is one year. **The OCF-based flag reads 0.079 and pronounces "no
single-year dependence" because OCF IS THE WRONG SERIES TO MEASURE IT ON** — subtracting capex
and SBC amplifies the outlier rather than damping it. The two figures differ by 53% and
`flags_disagree` is blank. **TOOLING DEFECT, recorded at the fold.**

**(iv) `window_disagree` — "9yr and the full 17yr series give different KINDS of answer; the 9yr
base may already contain the wave [E4-41]" → RIGHT, AND IT IS THE SHARPEST THING THE SCREEN SAYS
ABOUT THIS NAME.** FY2018-FY2026 owner earnings mean **$69.5M-$76.9M**; FY2010-FY2026 mean
**$51.9M-$55.4M**. On the $768M cap that is **9.05%-10.02%** against **6.76%-7.21%** — the
difference between a name that touches the [E4-28] floor and one that is nowhere near it,
decided entirely by whether the window starts before or after the FY2011-FY2014 trough. Carried
at Q4 as range per **[E4-25]**, not resolved by preference.

**(v) `spread_caveat` — "4-construction width only (3y/5y x two capex ends): CANNOT see
variation older than the 5-year window; rebuild it [E4-25]" → RIGHT, AND REBUILT.** The Q4 table
runs **seventeen fiscal years, FY2010 through FY2026**, from the filed cash-flow statements,
with **eight** windows rather than four constructions. What the rebuild shows and the
4-construction width could not: **owner earnings were NEGATIVE in FY2011 (−$41.4M to −$22.3M)
and near zero in FY2012 and FY2013.** The five-year window cannot see the last time this
business stopped generating cash, and the filing says the mechanism is still there — Q4.

**(vi) `years_filed 17` → RIGHT.** FY2010 (ended 2010-02-27) through FY2026 (ended 2026-02-28),
seventeen annual periods, all present and traced to 10-K cash-flow statements.

**(vii) `flags_disagree` (empty), `level_shift_full` n/a, `da_note`, `name_change_note`,
`wc_note` (all empty) → `flags_disagree` IS WRONG TO BE EMPTY** (see (iii)); the other four are
correctly empty. Incorporated in Minnesota in 1949 and named Apogee throughout; no D&A anomaly
beyond the acquisition amortization the filing discloses by segment; and no single
working-capital line carries the cash flow.

**SCORE — nine flags and sub-flags resolved by hand before Q1 opened. THREE RIGHT AND USEFUL**
(`window_disagree`, `spread_caveat`, `acq_note` — the last understating itself), **TWO RIGHT**
(the `level_shift` pair, `years_filed`), **TWO WRONG ON SEMANTICS** (`cap_flag`'s "one of the
two is wrong"; `best_year_dep` against `best_year_dep_oe` with `flags_disagree` blank), **ONE
STALE** (`deal_note` — nineteen days behind a closed deal and blind to a second, larger one),
**ONE PRIOR REFUTED** (FC's (i-a) stale-cover defect does not reproduce on this row).

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Apogee sells the outside skin of
commercial buildings, four ways. Three of the four are the same trade: a general contractor or a
glazing subcontractor puts a job out to bid; Apogee bids a price to engineer, fabricate and — in
one segment — physically hang the aluminium frames and coated glass that make up the façade; if
it wins, it buys aluminium billet and float glass, adds fabrication and coating, and delivers to
a schedule set by somebody else's construction programme. Revenue arrives project by project
over months to years. The money is the gap between the bid price and the delivered cost, and the
two large risks inside that gap are **the metal price between bid and delivery** and **the
schedule slipping on a site Apogee does not control**. The fourth segment, **Performance
Surfaces, is a different business inside the same company**: coated glass and acrylic sheet —
museum glazing, picture framing, printable panels, warehouse decking — sold through distributors
as catalogue product, not as a bid. It is 14% of net sales, it is the one with recurring
non-project economics, and it is the one both 2026 acquisitions were bought for.

Segment weights, from the FY2026 10-K Item 1, verbatim: Architectural Metals *"approximately 36%
of our net sales"*; Architectural Services *"approximately 31%"*; Architectural Glass
*"approximately 19%"*; Performance Surfaces *"approximately 14%"*. **Eighty-six per cent of this
company is bid-priced non-residential construction.**

**The scarce input this business controls.** *In the three architectural segments: very little
that is scarce.* The filing's own account of its inputs is the tell — *"Most of our raw
materials are readily available from a variety of domestic and international sources"* — and of
its intellectual property — *"we do not regard our business as being materially dependent on any
single item or category of intellectual property."* What it does have is a **national
installation footprint**, and the filing states it as a fact about the industry rather than a
boast: *"We are one of only a few architectural glass installation service companies in the U.S.
to have a national presence and we have the ability to provide installation project management
throughout the country."* That is real, and it is narrow — a scarce *capability* in one of four
segments, not a scarce *input*. *In Performance Surfaces:* proprietary coating formulations and
the brands carrying them (Tru Vue, ChromaLuxe, ResinDEK, Unisub), which is the nearest thing in
the company to a controlled scarce input, and which the run tests properly at Q2.

**Will the fundamentals look broadly the same in ten years?** Yes — and that is the honest
answer, not the flattering one. Buildings will still need façades; façades will still be bid;
aluminium and float glass will still be commodities; and the North American non-residential
construction cycle will still be a cycle, which the filing says in its own voice: *"the North
American non-residential construction industry, which is cyclical in nature."* Nothing here is
subject to the *"constant change"* [E3-31] excludes. The business is **relatively simple**;
whether it is **stable in character** is the harder half, and the answer is that the *unit
economics* are stable while the *perimeter* is not — five acquisitions in seventeen years,
$626.9M of purchase price, two of them in the last four months. That is a finding for Q3 and Q4,
not a Q1 failure: I can describe how each acquired piece makes money in the same sentences as
the rest of it.

**[E4-46] applied:** nothing here would take five months to learn. Four segments, one sentence
each; commodity inputs; bid pricing; a construction cycle. This is inside the circle, and the
verdict is not close.

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE

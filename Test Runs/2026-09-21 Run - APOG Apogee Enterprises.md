# Company Run — APOGEE ENTERPRISES, INC. (APOG) — 2026-09-21
**CIK 0000006845** · NASDAQ · fiscal year ends late February / early March
**Wave 7, name 13 of 218** (`Screens/_daily/_wave7_order.txt`) · run started 2026-09-21, unattended
**Written question by question under the write-early protocol. Step 0, Q1 and Q2 written 2026-09-21. **The file closes at Q2.****
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

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

## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that *"(1) is needed or desired; (2) is thought by its
> customers to have **no close substitute** and; (3) is not subject to price regulation."*
> — **[E3-03]**, 1991 letter

- **Needed or desired [x]** — commercial buildings need façades; the demand is real and
  physical.
- **No close substitute [ ] — FAILS, AND IT FAILS ON THE FILER'S OWN SENTENCE.** The FY2026
  10-K, Item 1, Competitive Conditions, verbatim:
  > *"The North American non-residential construction market is **highly fragmented**.
  > Competitive factors include **price**, product quality, product attributes and performance,
  > reliable service, on-time delivery, lead-time, warranties, and the ability to provide
  > project management, technical engineering and design services."*

  **Price is the first word on the list**, as it was for Franklin Covey. And the Architectural
  Glass paragraph goes further and concedes the substitute explicitly:
  > *"In our Architectural Glass Segment, we compete with regional glass fabricators and
  > international competitors **who can provide certain products with attributes similar to
  > ours**."*

  The Architectural Services paragraph concedes cost as the axis: *"We compete by offering a
  robust set of capabilities **at a competitive cost**."* The Architectural Metals paragraph
  names the field: *"competes against **several** national, regional, and local aluminum window
  and storefront manufacturers, as well as regional finishing companies."* **That is the filer,
  in its own annual report, describing the market as fragmented, the axis as price, and the
  substitutes as available.**
- **Not price-regulated [x]** — passes, and it is the only one of the three that does.

**Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04]**
**[E4-04] IS NOT THE OPERATIVE RULE HERE AND IS NOT BEING USED AS ONE.** Under the ruling of
2026-09-20, [E4-04] is applied as a **competence limit**, never as a fourth franchise criterion,
and the perimeter close (UNKNOWABLE at Q2) is reserved for names that **pass [E3-03]** and whose
durability cannot be judged from filings. **APOG does not reach that branch: it fails [E3-03]
criterion 2 on filed evidence.** This is the FC and MGPI shape — **OUT on the business** — not
the TSM shape. Recorded so no reader mistakes which door this file went through.

**Primary moat metric, filing-sourced, and its trend — [E3-46], "the second question about the
business is a number."** *"the best businesses, by definition, are going to be businesses that
earn very high returns on capital employed over time."* Operating income ÷ (total assets less
current liabilities), ten years, from 10-K facts:

**APOG, EBIT ÷ capital employed, by fiscal year (label = year of the late-February end date):**
FY2017 20.4% · FY2018 14.0% · FY2019 8.0% · FY2020 10.3% · FY2021 3.2% · FY2022 3.4% ·
FY2023 18.7% · FY2024 20.9% · FY2025 13.3% · FY2026 9.9% — **ten-year mean 12.2%, minimum
3.2%.** Operating margin on the same ten years: **mean 6.7%**, range 1.7% to 11.0%.
**Direction: DOWN.** FY2024 20.9% → FY2025 13.3% → FY2026 9.9%, and consolidated adjusted
EBITDA margin 12.6% → 14.2% → **11.9%**.

### THE COMPETITOR ROW — required [E3-28]. Same metric, same window, filing-sourced.

**The window is aligned, and the alignment is stated.** Apogee's fiscal year ends in late
February, so fiscal year Y runs March(Y−1) to February(Y) and maps to **calendar year Y−1**.
Every peer is a December or October year-end mapped to its own end year. The row below is
therefore the same ten calendar years, 2016 through 2025, for all seven names.

**EBIT ÷ capital employed (operating income ÷ (total assets − current liabilities)), %, by
calendar year, from each company's own 10-K XBRL facts:**

| calendar year | **APOG** | TGLS | ROCK | AWI | BLDR | GFF | JELD | NX |
|---|---|---|---|---|---|---|---|---|
| 2016 | **20.4** | 15.1 | 9.6 | 12.8 | 11.0 | 5.6 | 10.3 | n/a |
| 2017 | **14.0** | 9.9 | 11.3 | 15.2 | 12.9 | 4.5 | 11.5 | n/a |
| 2018 | **8.0** | 12.9 | 12.1 | 19.4 | 16.8 | 5.5 | 7.0 | n/a |
| 2019 | **10.3** | 13.3 | 10.7 | 23.7 | 16.2 | 6.4 | 7.3 | n/a |
| 2020 | **3.2** | 15.1 | 11.8 | 16.5 | 17.6 | 7.0 | 6.1 | n/a |
| 2021 | **3.4** | 26.8 | 10.5 | 17.3 | 27.8 | 8.2 | 9.4 | n/a |
| 2022 | **18.7** | 43.2 | 13.1 | 18.5 | 43.1 | −7.9 | 2.2 | n/a |
| 2023 | **20.9** | 35.7 | 11.7 | 21.9 | 25.2 | 9.6 | 6.2 | 15.9 |
| 2024 | **13.3** | 30.2 | 12.0 | 23.5 | 18.1 | 19.7 | −6.3 | 2.7 |
| 2025 | **9.9** | 25.4 | 11.9 | 26.0 | 8.1 | 11.9 | −27.3 | n/a |
| **10-yr mean** | **12.2** | **22.8** | **11.5** | **19.5** | **19.7** | **7.1** | **2.6** | 9.3 (2y) |
| **10-yr mean operating margin** | **6.7** | **20.6** | **9.8** | **25.8** | **8.1** | **5.9** | **1.9** | 7.0 (2y) |

- **TGLS — Tecnoglass Inc.**, CIK 0001534675. *The closest listed competitor Apogee has*:
  architectural glass and aluminium window/curtainwall systems for North American commercial
  and residential construction, the same product in the same market. **22.8% on capital
  employed and a 20.6% operating margin against Apogee's 12.2% and 6.7%** — three times the
  margin, on the same product, over the same ten years, and **its worst year (9.9%) is better
  than Apogee's mean.**
- **AWI — Armstrong World Industries**, CIK 0000007431: interior building products (ceilings)
  sold into the same non-residential construction cycle. 19.5% / 25.8%, and **it did not have a
  single year below 12.8%** across the decade.
- **ROCK — Gibraltar Industries**, CIK 0000912562: building products, the nearest thing to
  Apogee's own economics. 11.5% / 9.8% — **the one peer Apogee genuinely matches**, and Apogee
  beats it only on the metric flattered by its thinner balance sheet, losing on margin.
- **BLDR — Builders FirstSource**, CIK 0001316835: building-products distribution and
  manufacturing, carried because it shows what the 2021-2023 construction wave did to every
  balance sheet in this industry (27.8 → 43.1 → 25.2 → 8.1). **Included precisely to make the
  wave visible.**
- **GFF — Griffon Corporation**, CIK 0000050725: building products (doors, outdoor). 7.1% / 5.9%.
- **JELD — JELD-WEN Holding**, CIK 0001674335: windows and doors. 2.6% / 1.9%, and **negative in
  each of the last two years** — the downside of this industry, filed.
- **NX — Quanex Building Products**, CIK 0001423221: window and door components. **Only two
  years resolve undimensioned in companyfacts** (2023, 2024); carried with that limit stated
  rather than dropped, and it does not move the reading.

- **Peers named: SEVEN of the industry's real competitors.** Buffett says eight. I took seven
  and here is why the eighth is not on the row, stated rather than hidden: **the filer says the
  competitors are not listed.** FY2026 10-K, performance-graph note, verbatim:
  > *"most of our direct competitors in our various business units are **either privately owned
  > or are divisions of larger, publicly owned companies**."*

  **Two natural peers stopped filing inside the window, and I checked that on EDGAR rather than
  asserting it: PGT Innovations, Inc.** (CIK 0001354327) filed **Form 15-12G on 2024-04-08**,
  its last 10-K being 2024-02-23 for the year ended 2023-12-30; **Masonite International Corp**
  (CIK 0000893691) filed **Form 15-12G on 2024-05-28**, last 10-K 2024-02-29 for the year ended
  2023-12-31. Both deregistered. Kalwall — which Apogee has now bought — was family-owned, as
  the merger agreement's counterparties (the Keller family trusts) show on the face of the
  8-K exhibit list. The remaining direct competitors the filing alludes to are divisions, and
  divisions do not file segment-level capital employed. **This is the [E3-28] limit being met, not
  evaded:** the seven listed names are all that file, and they span the industry from its best
  (TGLS, AWI) to its worst (JELD).
- **Any peer unavailable? Yes — the named private and divisional competitors above.** The row is
  nonetheless **not PROVISIONAL**, because the verdict does not rest on the row: it rests on the
  filer's own description of its market and on its own price/volume decomposition below. The row
  corroborates; it does not carry.
- **The row's limit, stated [E3-61]:** *"In some businesses, the participants behave like a
  demented Kellogg. In other businesses, they don't … I think you'd have to know the people
  involved."* The row shows position, not conduct. What follows is conduct, and it is Apogee's
  own filed account of it.

### THE DECIDING EVIDENCE — THE FILER'S OWN PRICE/VOLUME DECOMPOSITION, AND IT IS SEGMENT BY SEGMENT

This is **[E2-44]**'s first characteristic — can it *"raise prices … even when product demand is
flat and capacity is not fully utilized"* — put to the company in the company's own words, in
the year its demand was not flat but falling. FY2026 MD&A, verbatim, all four segments:

- **Architectural Metals (36% of net sales):** *"Net sales were $504.0 million, compared to
  $524.7 million, due to lower volume, **partially offset by favorable price**."* Price held.
  **And it did not matter:** *"Adjusted EBITDA was $54.1 million, or **10.7%** of net sales,
  compared to $70.6 million, or **13.5%** … primarily driven by inflation, including higher
  aluminum costs, and the impact of lower volume, partially offset by pricing."* **The price
  increase was real and it did not cover the cost increase.** That is exactly **[E4-37]**'s
  inverse metric — *"you can almost measure the strength of a business over time by the agony
  they go through in determining whether a price increase can be sustained"* — and the risk
  factors describe the agony in the filer's own voice: *"We may be unable to pass through
  additional tariff costs to our customers through price increases"*, and *"Our ability to
  mitigate these costs, or recover the cost increases through price increases, **may lag** the
  cost increases, which could negatively impact our margins."*
- **Architectural Services (31%):** *"The increase in net sales was driven by increased volume,
  partially offset by unfavorable project mix **and lower pricing**."* **Price conceded while
  VOLUME ROSE.** Adjusted EBITDA margin 8.0% → **7.0%**.
- **Architectural Glass (19%):** *"The decrease in net sales was primarily driven by **lower
  volume and price** due to lower end-market demand."* **Price conceded on top of the volume
  loss** — the MGPI sentence, in a different industry. Adjusted EBITDA margin 22.2% → **16.1%**,
  a 6.1-point collapse in one year.
- **Performance Surfaces (14%):** *"The increase was driven by $65.3 million of inorganic sales
  contribution from the acquisition of UW Solutions, and higher volume and price."* Price and
  volume both up — **and the margin fell anyway**, 25.3% → **21.0%**, *"primarily driven by
  higher manufacturing costs and the dilutive effect of lower adjusted EBITDA margin from the UW
  Solutions acquisition."*

**In a single fiscal year: two segments carrying half of net sales conceded price outright, one
raised price and still lost 2.8 points of margin to input costs, and the fourth grew price and
volume and still lost 4.3 points because the business it bought earns less than the business it
already had.** Consolidated adjusted EBITDA margin: 12.6% → 14.2% → **11.9%**. **A franchise is
the thing that does not do this.**

### THE VOLUME SERIES — [E4-55], "where units exist, monitor units"

> *"Precision Steel's pounds fell 69M → 46M while price rises held dollar revenue level — 'a
> serious reverse, not likely to disappear in some bounce back effect.'"* — **[E4-55]**

Apogee does not publish pounds or square feet, so the honest proxy is **revenue net of what was
bought**, and the filings give it:

| | FY2019 | FY2026 |
|---|---|---|
| Consolidated net sales (filed) | **$1,402.6M** | **$1,404.7M** |
| less UW Solutions, acquired FY2025 | — | ~**$100M** *(10-K: the business "delivered upon the first-year financial targets of **$100 million in revenue** and adjusted EBITDA margin of at least 20%")* |
| **organic, approximate** | **$1,402.6M** | **~$1,305M** |

**Seven fiscal years, $232.2M of cash paid for a business, and the consolidated top line is
$2.1M higher — which means the pre-existing business is about 7% SMALLER in nominal dollars, and
very much smaller in units, over a period in which construction costs rose substantially.** The
three architectural segments make it plainer still, from the segment tables: **$1,317.6M
(FY2024) → $1,238.9M (FY2025) → $1,206.8M (FY2026), down 8.4% in two years.** Backlog in the one
segment that reports it went **$720.3M → $693.8M**. *"Dollar revenue flattered by pricing is how
a shrinking franchise hides; the physical series is the honest one"* **[E4-55]** — here dollar
revenue is flattered by **acquisition**, which is the same concealment by a different route.

### **Untapped pricing power [E3-33]?** NO — and claiming it would be claiming near-monopoly.

> *"If you name some business that has incredible pricing power, you're talking about a business
> that's **a monopoly or a near monopoly**"* — **[E5-28]**

The filer's own first sentence on competition is *"highly fragmented."* The row above shows
seven listed competitors and the filing names private and divisional ones besides. **No claim
to this class is available, and none is made.**

### THE DISCONFIRMING CASE, PUT AS STRONGLY AS I CAN PUT IT — [E4-26], [E4-51]

> *"I'm not entitled to have an opinion unless I can state the arguments against my position
> better than the people who are in opposition."* — **[E4-51]**

**Four real arguments that APOG has a franchise, and what each is worth:**

1. **"Metals raised price in a falling market — that IS [E2-44] criterion 1, on 36% of sales."**
   *True, and it is the best fact in the file.* But [E2-44]'s test is whether price can be
   raised *"even when product demand is flat and capacity is not fully utilized"* **and the
   return survive it**; here the return did not survive it — 13.5% to 10.7%. A price rise that
   is smaller than the cost rise it answers is cost pass-through attempted and failed, which is
   **[E3-62]**'s second step run in reverse: the gains did not stay home.
2. **"Performance Surfaces earns 21% adjusted EBITDA margins on proprietary brands — a real
   franchise inside the company."** *This is the strongest structural argument and I take it
   seriously.* Three answers. (a) **It is 14% of net sales**, and the unit of the test is the
   company **[E4-08]**; $41.6M of the $172.3M of segment adjusted EBITDA, 24%, cannot make the other 86% of sales a franchise.
   (b) **Its margin is falling** — 27.5% → 25.3% → 21.0% — and the filer says why: the business
   it bought to grow the segment earns less than the segment did. (c) **On the capital actually
   employed it is the WORST of the four segments**: FY2026 segment EBIT of $26.5M (adjusted
   EBITDA $41.6M less segment D&A $15.2M) against **identifiable assets of $337.1M = 7.9%**,
   against Architectural Glass's 16.0%, Services' 15.2% and Metals' 12.1%. **The segment that
   looks like a franchise on margin is the one whose returns were bought rather than earned**,
   and [E2-43] is explicit that for an acquisitive filer the honest denominator is unleveraged
   **net tangible** assets with the goodwill wedge reported separately, not hidden.
3. **"'One of only a few architectural glass installation service companies in the U.S. to have
   a national presence' — that is a scarce capability, filed."** *True, and it is the one
   genuine structural asset in the architectural half.* And **it earns the lowest margin of the
   four segments** — 7.0% adjusted EBITDA, 6.2% EBIT — which is [E2-53] running backwards: in a
   dominance business *"Good or bad, it will prosper"*, and here the near-unique national
   position prospers at seven per cent. A scarce position that cannot be priced is not a moat;
   it is a job.
4. **"APOG earned 18.7% and 20.9% on capital employed in calendar 2022 and 2023 — better than
   Gibraltar, near Armstrong."** *True, and it is the reason this file deserved the work.* It
   is also **the wave [E3-51]**: *"when a surfer gets up and catches the wave and just stays
   there, he can go a long, long time. But if he gets off the wave, he becomes mired in
   shallows."* Look along the row for those two years — **TGLS 43.2% and 35.7%, BLDR 43.1% and
   25.2%, AWI 18.5% and 21.9%** — the entire industry printed its best numbers in the same two
   years, which is what a wave looks like and not what a moat looks like. **The screen's own
   `window_disagree` flag said this before I did** (*"the 9yr base may already contain the wave
   [E4-41]"*), and calendar 2025 has the answer: APOG back to 9.9%, BLDR to 8.1%, JELD to
   −27.3%, while **TGLS is still at 25.4% and AWI at 26.0%.** **The tide went out and two names
   were still dressed.** Apogee was not one of them.

**[E4-36] applied — which of the four causes of extreme success is this?** Munger's list, in
his own words: *"Extreme maximization or minimization of one or two variables … Adding success
factors so that a bigger combination drives success, often in nonlinear fashion … An extreme of
good performance over many factors … **Catching and riding some sort of big wave**."* Not the
first three: APOG maximizes no variable (it is mid-pack on every metric in the row), combines
nothing nonlinearly, and is not extreme on many factors. **It is the fourth**, and [E3-51] says
where that advantage lives — in the wave, not in the surfer.

### THE COMMODITY DOCTRINE, AND ITS ONE EXIT — [E2-58]

> *"persistent over-capacity without administered prices (or costs) equals poor profitability"*
> … the one exception is *"a cost advantage that is both **wide and sustainable** … By
> definition such exceptions are few."* — **[E2-58]**

A *"highly fragmented"* market (the filer's word) in which demand is falling (*"lower volume,
primarily as a result of lower demand"*) and price is being conceded in two segments is
over-capacity without administered prices. **The one exit [E2-58] permits is a wide and
sustainable cost advantage, and the competitor row is the test of it: a ten-year mean operating
margin of 6.7% against Tecnoglass's 20.6% and Armstrong's 25.8% is the opposite of a cost
advantage.** The exit is not available.

- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: NARROWING**
  (EBIT/capital employed 20.9% → 13.3% → 9.9%; adjusted EBITDA margin 14.2% → 11.9%; backlog
  $720.3M → $693.8M; three of four segments with falling margins.) **[E4-32]**'s *"primary
  criterion of a great business"* is a moat that widens every year. This one narrowed in each
  of the last two.
- **VERDICT: [ ] IN  [x] OUT — ON THE BUSINESS  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**One line:** *Apogee's own 10-K calls its market "highly fragmented", lists **price** first
among the factors that decide a sale, concedes that competitors "can provide certain products
with attributes similar to ours", and then shows two of four segments conceding price in a
single year while a third raised price and lost margin anyway — against a competitor row in
which the closest listed rival earns three times the operating margin on the same product over
the same ten years.* **Criterion 2 of [E3-03] fails on the filer's own words. OUT.**

---
⛔ **THE FILE CLOSES HERE.** Q3, Q4, Q5 and Q6 are **NOT OPENED** and no verdict is recorded for
them. Operator protocol rule 2, hard sequence: *"No Q5 output may be reported unless Q1-Q4 each
show IN."* **[E3-03]** is answered OUT on the business, which is permanent and which no price
repairs — *"You can turn any investment into a bad deal by paying too much. **What you can't do
is turn any investment into a good deal by paying little**"* **[E5-35]**.

### AND THE UNCOMFORTABLE PART, RECORDED BECAUSE IT IS TRUE — **COMPUTATION — NOT A CLEARANCE**

*The arithmetic below was produced at Step 0 in the course of resolving the screen's
`window_disagree`, `spread_caveat` and `best_year_dep` flags, before Q2 closed. It carries no
entry language and it is not a clearance; operator rule 3. It is written down because the
framework's honesty rule requires the run to say when the price was not the problem, and
because a reader who sees only "OUT" should see what was given up.*

Owner earnings rebuilt by hand over **seventeen fiscal years** from the filed consolidated
statements of cash flows (OCF less SBC less (c), with (c) shown at both the **[E3-44]** D&A
default and the total-capex end), against the hand-struck cap of **$768.0M** and the sovereign
of **5.34%**:

| window | OE, (c) = D&A | OE, (c) = total capex | yield on $768M |
|---|---|---|---|
| FY2022-FY2026 (5y, the corpus default **[E2-42]**) | $76.6M | $87.7M | **9.97% – 11.42%** |
| FY2018-FY2026 (9y) | $69.5M | $76.9M | **9.05% – 10.02%** |
| FY2010-FY2026 (17y, everything filed) | $51.9M | $55.4M | **6.76% – 7.21%** |

**So the five-year window puts APOG at or just over the [E4-28] ~10% floor, and the
seventeen-year window puts it nowhere near.** That is the third consecutive wave-7 run — MGPI,
FC, now APOG — in which **the price was never the problem**, and it is the reason the gate order
is the gate order: **Q5 was not reached, so none of this counts, and the fact that the yield
looks interesting is exactly the pressure operator rule 9 exists to resist.** The seventeen-year
series also contains the answer to why the five-year figure should not be trusted on its own:
**owner earnings were NEGATIVE in FY2011 (−$41.4M to −$22.3M) and near zero in FY2012 and
FY2013**, and **FY2024 alone carries 24.9% of the five-year mean** — [E4-41]'s normalize-down
case, unresolved because the file closed before it needed resolving.

---
## Q3, Q4, Q5, Q6 — NOT OPENED

**No verdict is recorded for any of them, and the template's blank fields for them have been
removed rather than left standing, so that no reader mistakes an unfilled box for an unfinished
gate.** Operator protocol rule 2, hard sequence: the run stops at the first verdict that is not
IN, and **Q2 is OUT on the business**. OUT is permanent and no price repairs it **[E5-35]**.

*The one piece of arithmetic that exists below the closed gate is the seventeen-year
owner-earnings rebuild, which was produced at Step 0 in the course of resolving the screen's
`window_disagree`, `spread_caveat` and `best_year_dep` flags — that is, BEFORE Q2 closed and in
service of Step 0, not of Q5. It is headed **COMPUTATION — NOT A CLEARANCE** where it appears at
the end of Q2 and carries no entry language (operator rule 3).*

**The 8-K EX-99.1 earnings releases were fetched but NOT scored.** The standing instruction from
the CGNX run is to pull the latest Item 2.02 release before scoring **[E4-29]** and **[E4-22]**'s
third flag. Both were identified on EDGAR and are named in Step 0 — **8-K of 2026-04-24
(`0000006845-26-000020`) and 8-K of 2026-06-26 (`0000006845-26-000058`)** — and one observation
that would have belonged to Q3 is recorded here as a **pointer, not a finding**, because the gate
was never opened: **Apogee's segment-profit measure in the audited segment footnote of the FY2026
10-K is "Adjusted EBITDA"**, the GroGlass press release headlines *"approximately 25% adjusted
EBITDA margin"* for an unclosed acquisition, and the company *"is unable to provide a
reconciliation of the forward-looking projected adjusted EBITDA margin non-GAAP measure to the
most directly comparable GAAP measure."* **[E4-29]** — *"Trumpeting EBITDA … is a particularly
pernicious practice"* — would plainly have had work to do here. **It was not done, it is not
scored, and it must not be read as a Q3 finding.** Written down so that a future run reopening
this name on new facts knows where to start.

---
## SELF-AUDIT

- [x] **Questions answered in order; no verdict skipped.** Step 0 → Q1 (IN) → Q2 (OUT). Stopped
      there. Q3-Q6 not opened and explicitly marked so.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests on
      the filed Item 1 of the FY2026 10-K, quoted. The Q2 competitor row is **not** marked
      PROVISIONAL, and the reason is stated in the row: the verdict rests on the filer's own
      words and its own price/volume decomposition, which the row corroborates rather than
      carries. Two claims that could have rested on memory — PGT Innovations' and Masonite's
      deregistration — were **checked on EDGAR** and carry their Form 15-12G dates and CIKs.
- [x] **Every UNRESEARCHED verdict names the artifact and where it lives.** None issued.
- [x] **Every UNKNOWABLE verdict states what specifically cannot be known.** None issued.
      [E4-04]'s perimeter close was considered and explicitly **declined**: APOG does not reach
      that branch, because it fails [E3-03] on filed evidence rather than passing it with
      unjudgeable durability.
- [x] **Step 0: the filing was read, with accession number; figures were cross-checked.** FY2026
      10-K, accession `0000006845-26-000023`, filed 2026-04-24; Q1 FY2027 10-Q, accession
      `0000006845-26-000063`; six 8-Ks by accession. **Four cash-flow lines cross-checked against
      the filed CONSOLIDATED STATEMENTS OF CASH FLOWS** (OCF 122,465 / capex (27,308) / D&A
      49,998 / acquisition of business (232,169), $000), all agreeing to the dollar with the XBRL
      used to build the series.
- [x] **Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.**
      Seventeen fiscal years, eight windows, (c) shown at both the [E3-44] D&A default and the
      total-capex end. **Headed COMPUTATION — NOT A CLEARANCE**, because the gate it would serve
      was never opened.
- [x] **Competitor row filled.** Seven listed peers, ten calendar years, EBIT ÷ capital employed
      and operating margin, each from its own 10-K XBRL facts, **with the fiscal-calendar
      alignment stated** (Apogee's fiscal Y = calendar Y−1). Quanex carried with its two-year
      data limit named rather than dropped. The eighth peer is absent and the filing's own
      sentence on why is quoted.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.** USD 5.34%,
      09/18/2026, US Treasury daily par yield curve, 30-year. **Currency argued from the filing,
      not assumed** — and the euro exposure that arrives with GroGlass is dated and placed in the
      future.
- [x] **Value stated as a round-number range, not a point estimate.** n/a — Q5 not opened. The
      Step-0 computation is reported as ranges across windows and capex ends, never as a point.
- [x] **One bar chosen, not both; windage count stated.** n/a — no bar chosen, no margin applied,
      **windage count 0**.
- [x] **Prices dated; aggregator used for live quotes only and flagged.** $36.80, close
      2026-09-18, Yahoo Finance chart endpoint, flagged, raw JSON on disk.
- [x] **Run committed to git.** Skeleton before any fetch (write-early protocol), then after
      Step 0 + Q1, then after Q2, then at the fold.
- [x] **Operator rule 9 obeyed in writing.** The four strongest arguments *for* a franchise are
      stated at Q2 under [E4-51]'s iron prescription and answered one by one, and the run records
      plainly that **the price was never the problem** rather than letting the OUT verdict hide
      it.

---
## REGISTER

- **Verdict: [ ] IN  [x] OUT (about the business)  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
- **One line:** *Apogee's own 10-K calls its market "highly fragmented", lists **price** first
  among the factors that decide a sale, and concedes that competitors "can provide certain
  products with attributes similar to ours" — and then its own MD&A shows two segments carrying
  half of net sales conceding price in a single year while a third raised price and lost margin
  anyway, against a competitor row in which the closest listed rival earns three times the
  operating margin on the same product over the same ten years.*
- **If UNRESEARCHED — THE WORK ORDER:** n/a.
- **If UNKNOWABLE:** n/a.
- **THE REVERSAL CONDITION, in words rather than as a price band (the QLYS ruling, 2026-09-07 — a
  name that failed on the BUSINESS does not get an alert):** *reopen this file only if the
  Performance Surfaces Segment — post-Kalwall and post-GroGlass — reaches a **majority of
  consolidated net sales** AND holds an **adjusted-EBITDA margin above 20% for three consecutive
  fiscal years** while the architectural segments shrink. That is: only if Apogee stops being a
  bid-priced construction business and becomes a branded-coatings business.* Management is moving
  in exactly that direction and the filed arithmetic says how far it has to go: **$177.5M has
  bought roughly $130M of revenue against $1.2bn of architectural sales, so the reversal is three
  or four more deals away, and no price move triggers it.** Carried openly against **[E3-47]** —
  *"their invisibility does not reduce their cost"* — because APOG is squarely inside the circle
  of competence and a wrongly-closed file there is the error class the corpus rates most
  expensive.

# Company Run — MGP Ingredients, Inc. (MGPI) — 2026-09-20
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
## STEP 0 — THE RATE, THE FILING, AND THE SIX FLAGS THE BRIEF SENT ME TO RESOLVE

**Sovereign, for the currency the business EARNS in** -- the currently observed rate, never a
forecast **[E4-15, E3-32]**:
- rate **5.34 %** · date **09/18/2026** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year**, struck fresh in this run with `python tools/sources.py` on
  2026-09-20. FRED DGS30 is the documented fallback and was not used. (The same call returned
  JPY 4.05% and EUR 3.75%, both 2026-09-17; neither is used.)
- **The currency is argued, not assumed.** FY2025 10-K Note 14, footnote (a), verbatim:
  *"Sales from foreign sources totaled $ 36,497 , $ 36,240 , and $ 49,822 for the years ended
  December 31, 2025, 2024, and 2023, respectively, and are largely derived from the United
  Kingdom, Japan, Canada, Mexico, and Australia. The balance of total sales is from domestic
  sources."* Against FY2025 sales of $536,375k that is **6.8% foreign, 93.2% domestic**. The
  same note reports long-lived assets in Northern Ireland of **$5,120k** out of $327,987k of
  net PP&E (1.6%). The registrant reports in USD, the quote is USD on Nasdaq, the excise-tax
  and three-tier distribution regime it sells into is domestic, and the grain it buys is priced
  in USD. **USD is the earnings currency on the filed evidence, not by default.** Disclosed
  limit: USD at 5.34% is also the HIGHEST of the three sovereigns, so the choice cannot flatter
  this name; and the ~10% floor **[E4-28]** does not move with the sovereign in any case.

**The filing was read** -- not tagged data **[E3-27]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **Form 10-K for the fiscal year ended 2025-12-31, filed
  2026-02-25, accession 0000835011-26-000031.** Superseded in part by the **Form 10-Q for the
  quarter ended 2026-06-30, filed 2026-07-29, accession 0000835011-26-000103** -- which the
  screen could not see and which is the source of the current share count, the H1 2026 cash
  flows, and the receivable matter at flag (ii). Also read: the **FY2024 10-K** (accession
  0001628280-25-007962), the **FY2023 10-K** (0001628280-24-006149), the **FY2021 10-K**
  (0001628280-22-003647, the Luxco perimeter); the **Q2 2025 10-Q** (0001628280-25-036842);
  **DEF 14A** filings of 2026-04-09 (0000835011-26-000058), 2025-04-21 (0001628280-25-018635),
  2024-04-09 (0001628280-24-015469) and 2023-04-12 (0001628280-23-011403); the 8-K EX-99.1
  earnings releases of 2026-07-29 (0000835011-26-000101), 2026-04-29 (0000835011-26-000066)
  and 2026-02-25 (0000835011-26-000029); the 8-K of **2026-08-07 Item 1.01**
  (0000835011-26-000108) **and both of its exhibits in full**; the 8-K of 2026-04-07 Item 7.01
  (0000835011-26-000052); and the Item 5.02 8-Ks of 2024-12-20 (0001628280-24-052151),
  2025-07-21 (0001628280-25-035386), 2025-12-16 (0000835011-25-000105) and 2026-02-17
  (0000835011-26-000006).
- **figure cross-checked against the filed statement:** XBRL
  `NetCashProvidedByUsedInOperatingActivities` for FY2025 returns **121,528,000**. The filed
  Consolidated Statements of Cash Flows in the FY2025 10-K reads, verbatim, *"Net cash provided
  by operating activities | 121,528 | 102,278 | 83,783"* in $ thousands. They agree. Second
  cross-check: XBRL `InventoryNet` at 2025-12-31 returns **382,741,000**; the filed
  Consolidated Balance Sheet reads *"Inventory | 382,741 | 364,944"*. They agree. **Both
  figures are load-bearing below and neither is taken from the tags alone.**

### FLAG (i) — `cap_flag`. RESOLVED, and it is a THIRD branch: neither number is wrong.

The screen said: *"CAP BELOW FILED PUBLIC FLOAT - cap $362M against a filed float of $423M
(1.17x) as of 2025-06-30. A cap cannot be smaller than a subset of itself. One of the two is
wrong - RE-STRIKE THE CAP BY HAND before using any yield on this row [operator rule 4]."*
**The screen's data are right and the screen's imperative is wrong on this name.** Both figures
are correct and they are not comparable, because they are struck fourteen months apart across a
collapse in the share price.

- **The float figure, verbatim off the FY2025 10-K cover** (accession 0000835011-26-000031):
  *"The aggregate market value of the voting and non-voting common equity held by non-affiliates
  of the registrant computed by reference to the closing price at which the common equity was
  sold, as reported by Nasdaq, on June 30, 2025, was approximately $ 423 million."*
- **The branch test the brief set.** MGPI's close on **2025-06-30 was $29.97** (aggregator,
  flagged; raw response `quote_MGPI_10y_raw.json`). $423,000,000 / $29.97 = **14,114,782
  implied non-affiliate shares.** Shares outstanding at the nearest cover date, the Q2 2025
  10-Q (accession 0001628280-25-036842): *"21,292,736 shares of Common Stock, no par value, as
  of July 25, 2025"*. **Float is therefore 66.3% of the shares, and an affiliate block of about
  7.18 million shares (33.7%) is real.** This is the **MCFT branch, not the CE branch** -- the
  float is a genuine subset and the ratio is informative. It is corroborated inside the 10-K's
  own risk factors: *"a group of stockholders beneficially owning appro ximately 20 percent of
  our Common Stock as of December 31, 2025 (excluding shares controlled by certain other
  stockholders) have a right to nominate up to two of the four directors to be elected by our
  Common Stockholders pursuant to a shareholders' agreement … and two other individuals who
  beneficially own approximately 9 percent of our Common Stock as of December 31, 2025 have
  agreed to vote in favor of those nominees"* (the spacing artifact *"appro ximately"* is the
  filed text and is left unsmoothed, PRIME RULE 1).
- **Why the 1.17x is not an error in the data.** The float is measured at 2025-06-30 ($29.97);
  the screen struck its cap on 2026-09-02. $362M / 21,363,225 shares implies a strike price of
  about **$16.95**. The same 14,114,782 float shares at $16.95 are worth **$239M against a cap
  of $362M** -- the subset is a subset. **The whole of the 1.17x is the price: $29.97 to about
  $16.95 is a 43% fall, and $29.97 to Friday's $14.13 is a 53% fall.**
- **TWO CLASSES — verified from the filing, and the answer is not quite the one the brief
  expected.** Section 12(b) of the FY2025 10-K cover lists exactly one security: *"Common Stock,
  no par value | MGPI | Nasdaq Global Select Market"*, with *"Securities registered pursuant to
  Section 12(g) of the Act: None"*. But the **balance sheet carries a second class outstanding**:
  *"Preferred, 5 % non-cumulative; $ 10 par value; authorized 1,000 shares; issued and
  outstanding 437 shares"*, carried at **$4 thousand**. The brief's recollection of a small
  preferred issue is **CONFIRMED, and it is smaller than small: 437 shares, $4,370 of par, about
  $219 a year of dividend.** It is unlisted and has no quote; adding it to the cap at par changes
  the cap by 0.0014%. **The cap is the common alone. The preferred's significance is entirely at
  Q3, where it is enormous** -- see the control finding there.
- **THE CAP, RE-STRUCK BY HAND.** `cap = close(anchor) x shares(measurement) x splits AFTER
  measurement`; `close`, never `adjclose`.
  - shares(measurement): **21,414,076**, from the cover of the newest periodic filing, the 10-Q
    for the quarter ended 2026-06-30, accession **0000835011-26-000103**: *"21,414,076 shares of
    Common Stock, no par value, as of July 24, 2026"*.
  - splits effective after 2026-07-24: **none.** The chart endpoint returns an empty splits map
    over the full available history; raw response saved to `quote_MGPI_10y_raw.json`.
  - close(anchor): **$14.13 on 2026-09-18** -- the last close before this run; today is Sunday
    2026-09-20. **AGGREGATOR (Yahoo Finance chart endpoint), flagged as such per operator rule
    5, permitted for live quotes only**; raw JSON written to the research folder.
  - **cap = 21,414,076 x $14.13 = $302,580,894 ≈ $303 million.**
  - **The screen's $362M is 20% too high because it is sixteen trading days stale.** Every yield
    below uses **$303M**.

### FLAG (ii) — `deal_note`. The "probably a credit facility" 8-K is the sharpest document in this file. THIRD TIME.

The screen said: *"1 8-K Item 1.01 filing(s) since 2026-02-25, none carrying a merger agreement
(EX-2.1) - most likely a credit facility or offering; **open them only if something else is
odd**."* The brief ordered it opened anyway. It was opened, and so were both exhibits.

**8-K filed 2026-08-07 for an event of 2026-08-06, accession 0000835011-26-000108, Item 1.01.**
Two exhibits, not one: EX-10.1 *Amendment No. 2 to Amended and Restated Credit Agreement* (Wells
Fargo as administrative agent) and EX-10.2 *Eighth Amendment to Note Purchase and Private Shelf
Agreement* (PGIM). Verbatim from the filed Item 1.01:

> *"Pursuant to Amendment No. 2, the definition of Consolidated EBITDA was modified to permit
> the Company to add back, for any period on or prior to December 31, 2027, **aggregate losses up
> to $20,000,000 related to accounts receivable from specific customers**, subject to disclosure
> of such customers in writing to the Administrative Agent. … As a result of Amendment No. 2,
> such uncollected receivables will not negatively impact the calculation of the financial
> covenants which the Company must comply with under the A&R Credit Agreement, including (i) a
> consolidated fixed charge coverage ratio covenant of not less than 1.25 to 1.00 and (ii) a
> consolidated net leverage ratio covenant of no greater than 4.00 to 1.00, as may be increased
> to 4.50 to 1.00 in any fiscal quarter in which a permitted acquisition is consummated and for
> the three consecutive fiscal quarters thereafter … **The Company has exercised its option for
> an Elevated Ratio Period, commencing with the fiscal quarter ended June 30, 2026 and for the
> three fiscal quarters thereafter, in connection with the earnout obligations for the
> acquisition of Penelope Bourbon LLC.**"*

and, on the reason, in the filer's own words:

> *"The Company undertook the Amendments described above as **precautionary measures**. The
> Company continues to believe that **the third fiscal quarter of 2026 will represent its peak
> leverage**, after which it expects leverage to decline. The Amendments were supported by the
> full participation of the banking group."*

**Three facts the screen could not have produced:**
1. **Up to $20 million of customer receivables is being pre-emptively excluded from covenant
   EBITDA** -- a named, bounded, disclosed-to-the-agent credit loss, with the exclusion running
   to 2027-12-31. This is the exact subject matter of [E2-54]'s coverage test.
2. **The net leverage covenant has been stepped up from 4.00x to 4.50x** for four quarters, and
   the mechanism invoked to do it is a clause written for *"any fiscal quarter in which a
   permitted acquisition is consummated"* -- used here for an **earnout payment on a 2023
   acquisition**, not for a new one.
3. **The filer itself says Q3 2026 is peak leverage.** That is a forward statement about its own
   balance sheet made six weeks ago, and it frames Q4.

**The screen's advice would have missed all three**, exactly as at CGNX and at CE. Recorded as a
standing tooling finding: **`deal_note`'s closing clause should be deleted, not merely ignored.**

### FLAGS (iii) and (iv) — `level_shift`, `flags_disagree`, `window_disagree`. RESOLVED TOGETHER, because they are one fact.

**What the two series actually are.** `tools/sources.py annual()` on the filer's own companyfacts
returns **17 annual periods**, matching the screen's `years_filed 17`. They are not 17 years of
one calendar, and that is the first thing the screen could not see:

| period end | OCF $M | | period end | OCF $M |
|---|---|---|---|---|
| 2009-06-30 | 3.2 | | 2018-12-31 | 33.5 |
| 2010-06-30 | 32.7 | | 2019-12-31 | 19.7 |
| 2011-06-30 | 3.1 | | 2020-12-31 | 53.3 |
| *2011-07-01 to 2011-12-31* | **MISSING** | | 2021-12-31 | 88.3 |
| 2012-12-31 | −5.0 | | 2022-12-31 | 88.9 |
| 2013-12-31 | 17.3 | | 2023-12-31 | 83.8 |
| 2014-12-31 | 15.8 | | 2024-12-31 | 102.3 |
| 2015-12-31 | 18.7 | | 2025-12-31 | 121.5 |
| 2016-12-31 | 19.7 | | | |
| 2017-12-31 | 33.5 | | | |

**The fiscal year changed.** The 10-K filed 2011-09-02 covers the year ended **2011-06-30**; the
next 10-K, filed 2012-03-13, covers the period ended **2011-12-31**. The six months from
2011-07-01 to 2011-12-31 fall outside the 340-380-day duration filter and are **absent from the
series entirely.** A "17-year series" with a hole in it is not a 17-year series.

**The second series, and why it refuses the ratio.** The screen's `level_shift_oe n/a` with
`level_note_oe` *"EARLY HALF STRADDLES ZERO - the pre-window years run from $-0.7M to $3…"* is
the **owner-earnings series at the total-capex end of (c)**, and it is reproduced exactly:

| year | OCF | − SBC | (c) = D&A | **OE at D&A end** | (c) = total capex | **OE at capex end** |
|---|---|---|---|---|---|---|
| 2017 | 33.5 | 2.6 | 11.3 | **19.6** | 21.1 | **9.8** |
| 2018 | 33.5 | 3.1 | 11.4 | **19.0** | 31.0 | **−0.7** |
| 2019 | 19.7 | 3.3 | 11.6 | **4.8** | 16.7 | **−0.3** |
| 2020 | 53.3 | 3.0 | 13.0 | **37.3** | 19.7 | **30.6** |
| 2021 | 88.3 | 5.6 | 19.1 | **63.6** | 47.4 | **35.3** |
| 2022 | 88.9 | 5.5 | 21.5 | **62.0** | 45.3 | **38.1** |
| 2023 | 83.8 | 10.6 | 22.1 | **51.0** | 55.3 | **17.9** |
| 2024 | 102.3 | 4.0 | 22.0 | **76.3** | 71.2 | **27.1** |
| 2025 | 121.5 | 4.7 | 24.1 | **92.7** | 45.5 | **71.3** |

- **The screen's band is reproduced from the filings:** the 5-year (2021-2025) mean at the
  capex end is **$37.9M** (screen `oe_bottom_m 38`) and the 3-year (2023-2025) mean at the D&A
  end is **$73.3M** (screen `oe_top_m 73`). The screen's arithmetic is right.
- **`flags_disagree` is explained and it is not a defect.** The OCF series is positive in every
  period and takes a ratio; the owner-earnings series at the capex end is **−$0.7M in 2018 and
  −$0.3M in 2019**, so a ratio of halves is undefined. Two different series, two different
  answers, and **[E4-25]** governs the reading: *"Usually, the range must be so wide that no
  useful conclusion can be reached."*
- **WHICH YEARS CARRY THE SHIFT, which is what the screen's own instruction `read the filing`
  asked for.** The OCF step is **2020 → 2021**: a 2017-2020 mean of **$35.0M** against a
  2022-2025 mean of **$99.1M**, a 2.8x step. **2021 is the year the Luxco merger closed
  (2021-04-01).** The step is an **acquisition**, not a cycle. The cycle is what is taking it
  away now.
- **SBC resolves for every year used, and is never zero** (FY2017 $2.6M through FY2025 $4.7M;
  FY2023 $10.6M). Verified as the brief required; it is subtracted in full **[E5-06]**.
- **Restatement vintage:** `vintage="newest"` throughout, so where a figure was restated the
  latest filed value is used. No figure used above differs between vintages by more than
  rounding.

### FLAG (iv), continued — THE PERIMETER, and this is the most important paragraph in the file.

**Established from the filings, not from the brief.** There are at least **three different
companies** inside these 17 periods, and the boundaries are documented:

1. **Through FY2011 (June fiscal years)** — the Midwest Grain inheritance: industrial alcohol
   and wheat proteins and starches. FY2009 (June) carries a **net loss of $69.1M** on sales of
   $291.8M.
2. **A fiscal-year change**, leaving the six-month stub above out of every annual series.
3. **FY2012-FY2020** — two segments, distillery products and ingredient solutions. Sales run
   $318.3M (2016) to $395.5M (2020). **Branded spirits does not exist.**
4. **2021-04-01 — the Luxco merger.** FY2021 10-K Note 4, verbatim: *"The aggregate consideration
   paid by the Company in connection with the Merger was $ 237,500 in cash (less assumed
   indebtedness) and 5,007,833 shares of common stock of the Company … The Company Shares were
   valued at $ 296,213 and represented approximately 22.8 percent of the Company's outstanding
   common stock immediately following the closing of the Merger."* The purchase-price allocation
   table gives *"Cash, net of assumed debt | $ 149,484"*, *"Value of MGP Common Stock issued at
   close (a) | 296,279"*, *"Fair value of total consideration transferred | $ 445,763"*. **This
   created the Branded Spirits segment.** Share count went 16.9M → 22.0M.
5. **2023-06-01 — Penelope Bourbon.** FY2025 10-K Note 4: *"$ 105,000 in cash paid at closing"*
   (finalised at $104,638) *"with further additional potential earn-out consideration of up to a
   maximum cash payout of $ 110,800"*, and *"The Company achieved the maximum net sales target …
   during the third quarter 2025, and in accordance with the terms of the agreement, the Company
   will pay out the full contingent consideration of $ 110,800 during the first half of 2026."*
6. **December 2023 — the Atchison distillery closed.** FY2025 10-K Note 6: *"The decision to
   close the Atchison Distillery is consistent with the Company's plan to address profitability
   headwinds associated with its GNS and industrial alcohol products within the Distilling
   Solutions segment."* A $17,112 asset impairment in 2023. **White goods and other co-products
   revenue: $133,031 (2023) → $32,901 (2024) → $20,562 (2025).** A whole product line left.
7. **2026-05-01 — distilling idled at two of the three distilleries** (8-K 2026-04-07,
   accession 0000835011-26-000052, EX-99.1): *"plans to temporarily idle distilling operations at
   its Limestone Branch Distillery in Lebanon, Kentucky and Lux Row Distillers in Bardstown,
   Kentucky"*, effective 2026-05-01, resumption *"could be as early as 12 months after that
   date."*

**SO: WHAT IS THE LONGEST WINDOW ON ONE PERIMETER?**
- Luxco in, Penelope in, Atchison out: **FY2024 and FY2025. Two years, plus H1 2026.**
- Luxco in for a full year: FY2022-FY2025, **four years** — but FY2022 and FY2023 still contain
  the Atchison white-goods leg ($133M of FY2023 sales) and FY2023 contains only seven months of
  Penelope.
- **There is no five-year window on one perimeter.** The corpus's default window is five years
  **[E2-42]** — *"we recommend not less than a five-year test as a rough yardstick of economic
  performance"* — and **[E1-03]**, *"I much prefer a five-year test."* It cannot be satisfied
  here. **This is the BN shape of this morning: the perimeter is measurable, and no five-year
  window on one perimeter exists.**
- **The screen's `window_disagree` hypothesis was half right.** *"the 9yr base may already
  contain the wave"* — it does, but the thing it contains is an **acquisition financed 66% in
  stock**, and the wave arrives later and in the other direction.

### FLAG (v) — `acq_note`. The brief's prediction is CONFIRMED to the dollar, and the understatement is the largest yet recorded.

The screen said: *"acquisitions are $253M, 70% of cap, inside the window."* That is
**$149.0M (2021) + $103.7M (2023) = $252.7M**, and it is **the investing-cash line and nothing
else.** The filings give the real perimeter:

| | screen sees | the filing says | invisible to the tool |
|---|---|---|---|
| Luxco, 2021-04-01 | $149.0M | **$445,763k** total consideration transferred | **$296,279k paid in MGP stock** (5,009,206 shares, 22.8% of the company) |
| Penelope, 2023-06-01 | $103.7M | **$215,438k** ($104,638k cash + $110,800k earnout, maximum achieved) | **$110,800k of earnout**, paid H1 2026 |
| **total** | **$252.7M** | **$661,201k** | **$407.1M** |

- **$661.2M of acquisition consideration against a hand-struck cap of $303M — 218% of the
  market capitalisation, not 70%.** The screen understates the perimeter by **$408.5M**.
- **The known source limit held exactly as the brief said it would** and was not re-tested:
  `BusinessCombinationConsiderationTransferred1` and its equity sibling do not resolve
  undimensioned in companyfacts. The stock leg and the earnout leg were both read by hand out of
  the business-combination notes. **This is the seventh consecutive perimeter understatement in
  this project and the largest in relative terms.**
- **And the earnout is now paid.** Q2 2026 10-Q cash-flow statement: *"Payment of contingent
  consideration | ( 48,700 )"* inside operating activities and *"Payment of contingent
  consideration | ( 62,100 )"* inside financing activities — **$110,800k, in cash, in six
  months**, funded by *"Proceeds from long-term debt | 145,000"*.

### FLAG (vi) — `wc_note` EMPTY. The tool's blind spot, and on this name it is the whole story.

The brief was right that an empty flag here is not a clean bill. `working_capital_flag()` reads
annual facts only. Tested by hand, year by year, over the whole window.

**The inventory line from the filed cash-flow statements (a build is a cash OUTFLOW):**
2015 −$24.3M · 2016 −$20.1M · 2017 −$14.3M · 2018 −$15.6M · 2019 −$28.2M · 2020 −$3.9M ·
2021 −$14.2M · 2022 −$44.4M · 2023 −$46.9M · 2024 −$18.2M · 2025 −$18.1M · **H1 2026 −$25.6M**.
**Cumulative 2015 to H1 2026: $273.8M of cash absorbed by inventory.**

**Aged inventory is separately disclosed and it is the business.** FY2025 10-K Note 2:
*"Barreled distillate (bourbons and other whiskeys) | 301,665 | 283,119"* out of total inventory
of *"382,741"* — **78.8% of inventory, 24.4% of total assets, and all of it classified current**:
*"Bourbons, ryes, and other whiskeys, included in inventory, are normally aged in barrels for
several years, following industry practice; all barreled bourbon, rye, and other whiskeys are
classified as a current asset."*

**THE ARITHMETIC THAT MATTERS, AND IT POINTS THE OPPOSITE WAY FROM THE SCREEN.** Strip the
working-capital movements out of the filed operating cash flow:

| | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---|---|---|---|
| Net cash provided by (used in) operating activities, as filed | **$83.8M** | **$102.3M** | **$121.5M** | **−$40.7M** |
| less: total working-capital movements | −$79.6M | −$47.2M | **+$26.2M** | −$20.5M |
| **operating cash flow BEFORE working capital** | **$163.4M** | **$149.5M** | **$95.3M** | (see note) |

- **Reported operating cash flow rose 45% from FY2023 to FY2025. Operating cash flow before
  working capital FELL 42% over the same two years.** The reported series and the business are
  moving in opposite directions, and the reported series is the one the screen read.
- **What did it:** FY2025 released **$32.2M** of receivables as sales fell 24%, and turned
  $47.2M of working-capital absorption in FY2024 into $26.2M of working-capital *release* in
  FY2025. A shrinking business releases working capital. That is not earnings.
- H1 2026 is not comparable on the same line because it also carries the $48.7M earnout payment
  inside operating activities; stripping both the earnout and the working-capital movements,
  H1 2026 operating cash was **+$28.4M against H1 2025's +$46.8M**, down 39%.
- **This is [E2-23] constraint 3 read in the direction that hurts.** The working-capital
  increment belongs in (c) *"If the business requires additional working capital to maintain its
  competitive position and unit volume."* MGPI requires barrels laid down years before they are
  sold. **It has just announced it will stop laying them down at two of three distilleries.**
  The 2026 and 2027 cash-flow statements will therefore look BETTER while the business is being
  made SMALLER, and **[E2-60]** names that transaction: restricted earnings are those whose
  distribution costs the business *"its ability to maintain its unit volume of sales, its
  long-term competitive position, its financial strength"*, and *"a company that consistently
  distributes restricted earnings is destined for oblivion."*
- **The filer's own capex plan confirms it.** FY2026 guidance, 8-K EX-99.1 of 2026-07-29:
  *"Full-year capital expenditures expected to be approximately $20 million."* Against D&A of
  $24.1M in FY2025 and capex of $71.2M in FY2024. **Planned capex is now BELOW depreciation.**

### THE BRIEF'S THREE UNVERIFIED RECOLLECTIONS — each checked against a filed document

Operator rule 9 and **[E4-26]** require the disconfirming evidence to be hunted hardest for the
favourite hypothesis, and **[E3-41]**: *"you must not fool yourself, and you're the easiest person
to fool."* The brief named three recollections and said to discard any not in the filings.

| the brief's recollection | verdict | the document |
|---|---|---|
| (a) "a large impairment against its branded-spirits reporting unit in the FY2024 or FY2025 cycle" | **CONFIRMED, and understated — there are THREE consecutive impairment events, not one** | FY2025 10-K Note 5: goodwill impairment **$73,755** (FY2024) and **$132,122** (FY2025) plus trade-name impairment **$20,500** (FY2025); Q2 2026 10-Q: a further **$115,667** goodwill and **$36,990** trade-name impairment in Q1 2026, inside *"Impairment and other | 180,277"* year-to-date |
| (b) "a CEO change effective around January 2025" | **CONFIRMED with a correction: the January 2025 change was an INTERIM appointment; the permanent CEO started 2025-07-21** | 8-K filed 2024-12-20, accession 0001628280-24-052151: Brandon M. Gall, the CFO, appointed *"Interim President and Chief Executive Officer, effective January 1, 2025"*, succeeding David S. Bratcher, *"whose service … will end at the close of business on December 31, 2024, under circumstances entitling him to severance benefits."* Then 8-K of 2025-07-21, accession 0001628280-25-035386: *"MGP INGREDIENTS APPOINTS JULIE FRANCIS AS CHIEF EXECUTIVE OFFICER"* |
| (c) "a reduction in distillate production in response to oversupply" | **CONFIRMED, and it is larger than "a reduction"** | 8-K of 2026-04-07, accession 0000835011-26-000052, EX-99.1: *"MGP INGREDIENTS ANNOUNCES TEMPORARY IDLING OF OPERATIONS AT TWO KENTUCKY DISTILLING FACILITIES"*, effective 2026-05-01, *"The decision will affect 33 employees"* |

**None of the three was refuted. The brief was right three times, and (a) and (c) were both
larger than briefed.** The one correction is on (b)'s character, not its date.

**One thing the brief did NOT brief, and it is the single sharpest sentence in the file.** The
2026-04-07 release quotes the CEO by name:

> *"The American whiskey market continues to be **structurally oversupplied, with excess capacity
> and elevated inventory**. Like many companies across the industry, we are navigating a
> challenging environment and taking steps to better align our operations with current inventory
> levels"* — Julie Francis, president and CEO, 8-K EX-99.1, 2026-04-07

That is **[E2-58]**'s equation stated by the subject company about its own market, in its own
words, over the CEO's name, in a furnished exhibit. It is quoted again at Q2.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Three different cash cycles under one
roof, and they do not resemble each other.

1. **Rent time to other people's brands.** Buy corn and rye at market, cook and ferment and
   distill at Lawrenceburg, Indiana and two Kentucky distilleries, fill new charred-oak barrels,
   and then either (a) sell the liquid — new-fill or aged — in bulk by the proof gallon to
   somebody else's brand, or (b) keep the customer's barrels in your rickhouses and charge them
   rent and handling for years. Cash leaves at fill; it comes back two to eight years later. The
   buyer is another company's purchasing department and the invoice is priced per proof gallon.
   FY2025: brown goods $128.5M, warehouse services $32.4M.
2. **Own the brand instead.** Take liquid — your own or bought in — bottle it under trademarks
   you own (Penelope, Rebel, Remus, Yellowstone, El Mayor), ship to distributors inside the
   US three-tier system, and keep the gap between liquid plus glass plus federal excise and
   whatever shelf price the brand can hold, less the advertising it takes to hold it. FY2025:
   $232.9M of sales, $29.2M of advertising and promotion, 49.5% segment gross margin.
3. **Mill wheat and sell the fractions.** Separate wheat flour into starch and vital gluten;
   sell the specialty grades (Fibersym, Arise, Proterra) to food processors at a premium to the
   commodity grades; the commodity starch, commodity gluten and biofuel clear at market prices
   you do not set. FY2025: $122.0M of sales at a **12.7% gross margin**, down from 35.6% in 2023.

**The scarce input this business controls: time already spent.** $301,665k of *"Barreled
distillate (bourbons and other whiskeys)"* — 78.8% of inventory, 24.4% of total assets — plus the
licensed distilling and warehousing capacity to make more. Nothing else on the input list is
scarce: corn, rye and wheat are exchange-traded, glass and labels are bought, and *"two suppliers
… approximated 19 percent of consolidated purchases"* (Note 13) means the grain is bought, not
controlled. **Aged whiskey cannot be hurried, and that is the whole of what MGPI owns that a
competitor with capital cannot buy this year.** Whether that is a *moat* is Q2's question and the
answer there is not the same as the answer here.

**Will the fundamentals look broadly the same in ten years?** Yes. Grain in; ferment; distill;
barrel; wait; bottle or sell in bulk; wheat milled into starch and protein. No technology
transition is in prospect, no regulatory re-architecture is disclosed as pending, and the products
are the same products the Atchison plant was making in 1941. **[E3-31]**'s actual test — *"they
must be relatively simple and stable in character"* — is met, and this is not a business where
*"we're not smart enough to predict future cash flows"* for want of comprehension.

**The honest qualifier, recorded so it is not mistaken for a defect at this gate.** The company in
its present shape is **twenty-six months old** (Penelope closed 2023-06-01; Atchison closed
December 2023). **That is a problem with the RECORD, not with the comprehension**, and it is
carried forward to Q4's window, where **[E2-42]**'s five-year default cannot be met. Marking Q1
IN says I understand the three businesses; it does not say I can price the combination. Those are
different claims and the framework separates them — **[E5-42]**: *"whether it's a good investment
for us depends on how much we pay for that in the end."*

**No degree-of-difficulty credit was taken and none was needed [E4-18].** Nothing above required
narrowing an assumption; the three cycles are described in the filer's own revenue-disaggregation
table.

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The three criteria, applied per leg, because the brief was right that these are three different
questions and cannot share one answer.** FY2025 gross profit: Branded Spirits **$115.3M (57.8%)**,
Distilling Solutions **$68.6M (34.4%)**, Ingredient Solutions **$15.5M (7.8%)**.

| **[E3-03]** criterion | Branded Spirits | Distilling Solutions | Ingredient Solutions |
|---|---|---|---|
| (1) needed or desired | **yes** | yes | yes |
| (2) **no close substitute in the customer's own judgement** | **split** — premium plus yes, mid and value no | **NO** | **NO** |
| (3) not subject to price regulation | yes (control-state listings gate access, they do not set the price) | yes | yes |

### (2) is the whole question, and the filer answers it in its own volume series.

**[E4-55]** is explicit that where units exist, the units are the honest series — *"Dollar revenue
flattered by pricing is how a shrinking franchise hides; the physical series is the honest one."*
MGPI publishes the decomposition itself. FY2025 10-K, Distilling Solutions, verbatim:

> *"Brown goods | $ 128,450 | $ 265,873 | $ (137,423) | (52) | %"* and, in the
> attribution table immediately beneath, *"Brown goods | (52)% | **(46)%** | (6)%"* against column
> headings *"Total"*, *"Volume"*, *"Net Price/Mix"*.

**Volume fell 46 percent in one year and the price fell 6 percent on top of it.** A product with no
close substitute does not lose 46% of its units while also conceding price. And the filer names the
mechanism: *"Brown goods sales volume and net price/mix decreased primarily due to reduced customer
demand resulting from **elevated industry-wide barrel inventory levels**."* The FY2024 MD&A adds
*"instances of **customer contract non-performance**"* — customers with a contract chose to break
it rather than take the liquid, which is a statement about substitutability that no ratio could
make.

**Ingredient Solutions fails (2) on its own margin series.** Segment gross margin **35.6% (2023) →
20.1% (2024) → 12.7% (2025) → 10.1% (Q2 2026)**, and the Q2 2026 release attributes it to *"higher
waste starch stream costs"* — an input the segment cannot pass on. A specialty ingredient with no
close substitute passes a cost through.

**Branded Spirits is where (2) can be argued, and the argument splits the portfolio in two.**
FY2025 10-K revenue disaggregation:

| price tier | 2023 | 2024 | 2025 | two-year change |
|---|---|---|---|---|
| Premium plus | $105,465 | $110,991 | $116,730 | **+10.7%** |
| Mid | $75,676 | $63,454 | $59,486 | **−21.4%** |
| Value | $47,907 | $42,100 | $32,606 | **−31.9%** |
| Other (mainly private label) | $24,885 | $24,271 | $24,119 | −3.1% |

Premium plus is growing — Q2 2026: *"Penelope Bourbon maintained its strong growth trajectory and
was up 13%."* **That is $116.7M of FY2025 sales, 21.8% of the company.** The mid and value tiers,
$92.1M, are in decline, and the company's own valuation specialist says so in the impairment note:
*"The impairment charge to the trade name indefinite-lived intangible assets were most impacted by
declines in the mid and value price tiers within the Branded Spirits segment."*

### THE COMMODITY DOCTRINE **[E2-58]** — and the company states its premise for me.

The equation: *"persistent over-capacity without administered prices (or costs) equals poor
profitability"*, long-run profitability set by *"the ratio of supply-tight to supply-ample years"*,
prosperity breeding the next glut — *"nothing fails like success."* Every element is in the
filings, and the first one is over the CEO's signature in a furnished exhibit:

> *"The American whiskey market continues to be **structurally oversupplied, with excess capacity
> and elevated inventory.** Like many companies across the industry, we are navigating a
> challenging environment and taking steps to better align our operations with current inventory
> levels"* — Julie Francis, president and CEO, 8-K EX-99.1, 2026-04-07, accession
> 0000835011-26-000052

- **Persistent over-capacity: stated by the filer.** *"structurally oversupplied, with excess
  capacity."*
- **No administered prices: demonstrated by the filer.** Net price/mix −6% on brown goods while
  volume fell 46%, and *"we sold younger barrels on average in 2024 compared to 2023."*
- **Prosperity breeding the glut: the filer's own capital account is the evidence.** Capex ran
  $47.4M, $45.3M, $55.3M, $71.2M across 2021-2024 — $219.2M of it — into warehouse and distilling
  capacity during the boom, and the 2026 plan is *"approximately $20 million"* with two of three
  distilleries idled. *"Nothing fails like success."*
- **The second step [E3-62] was never taken.** In a commodity business the gains from capacity
  investment *"flow through to the customer"* — *"Nothing was going to stick to our ribs as
  owners."* MGPI's own gross profit on brown goods proves the direction: the industry built
  rickhouses together, and the benefit went to the brand owners who buy the liquid.

**The equation's only exception is *"a cost advantage that is both wide and sustainable … By
definition such exceptions are few."* The exception is not established here, and the burden is on
the claim.** MGPI's own filings make **no** cost, scale or capacity leadership claim: the single
self-description is *"a leading producer of branded and distilled spirits, as well as food
ingredient solutions"* (three occurrences, Items 1 and 7 and Note 1) — a scale phrase, not a cost
claim — and **[E3-28]** forbids evidencing a relative claim from one company's numbers in any case.

### THE COMPETITOR ROW — required **[E3-28]**. *"I can't be an intelligent owner of a business unless I know what all the other businesses in that industry are doing."*

**THE CENSUS IS SOURCED FROM A PEER'S OWN FILING, not from my knowledge.** Brown-Forman's 10-K for
the fiscal year ended 2026-04-30, accession 0000014693-26-000024, Item 1, verbatim:

> *"Our competitors include major global spirits companies, such as **Bacardi Limited, Becle
> S.A.B. de C.V., Davide Campari-Milano N.V., Diageo PLC, LVMH Moët Hennessy Louis Vuitton SE,
> Pernod Ricard SA, Rémy Cointreau, and Suntory Global Spirits.** In addition, particularly in the
> United States, we compete with national companies and craft spirit brands."*

**Two findings come straight out of that sentence, before any number is computed.**
1. **Eight companies are named as the spirits industry, and exactly ONE of the eight files with the
   SEC: Diageo PLC, on Form 20-F.** Bacardi is private; Becle lists in Mexico City; Campari on
   Euronext; LVMH, Pernod Ricard and Rémy Cointreau in Paris; Suntory Global Spirits is a
   subsidiary of a privately held Japanese parent. **The industry is structurally unmeasurable from
   SEC filings, and that is a limit of the evidence, stated rather than papered over.**
2. **The branded leader's own competitor list does not contain MGP Ingredients.** Nor does any
   other filer's: an EDGAR full-text search for `"MGP Ingredients"` in Form 10-K over 2024-01-01 to
   2026-09-20 returns **38 hits**, of which **21 are MGPI's own filings** and the remainder are
   board-overlap and unrelated mentions (Calavo Growers, Canopy Growth, Clearway Energy, Duckhorn,
   Farmer Brothers, FHLB Topeka, Laird Superfood, Whole Earth Brands). **No SEC filer names MGPI as
   a competitor.** `fts_count()` was used, with the bare zero-padded CIK, so a malformed-call
   zero-hit is excluded.

**THE ROW. Same metric, same window, filing-sourced from each peer's own XBRL.** Primary metric:
**operating income ÷ revenue, as reported.** Chosen because **[E3-46]** asks the second question
about the business as a number and **[E2-58]**'s exception is a *cost* claim, which a margin series
tests directly. Fiscal calendars differ and are labelled; that mismatch is disclosed, not hidden.

| Company | FY calendar | operating margin, by fiscal year (%) | **9-year mean** | **recent 3-yr mean** | source |
|---|---|---|---|---|---|
| **MGPI** | Dec | 12.3 · 13.3 · 13.0 · 13.7 · 20.2 · 19.0 · 17.8 · 10.6 · **−17.6** | **11.4** | **3.6** | own 10-K XBRL, FY2017-FY2025 |
| Brown-Forman (BF-B) | Apr | 33.7 · 32.3 · 34.4 · 32.4 · 33.7 · 30.6 · 26.7 · 33.8 · 27.8 *(FY26: 25.5)* | **31.7** | **29.0** | 10-K XBRL, FY2017-FY2026 |
| Constellation Brands (STZ) | Feb | 32.6 · 30.1 · 29.7 · 25.8 · 32.4 · 26.4 · 30.1 · 31.8 · 3.5 *(FY26: 29.8)* | **26.9** | **21.7** | 10-K XBRL, FY2017-FY2026 |
| Diageo (DEO) | Jun | *(USD only from FY2022)* 19.8 · 19.6 · 21.5 · 15.5 | **19.1** *(4 yrs)* | **18.9** | 20-F XBRL, FY2022-FY2025 |
| Ingredion (INGR) | Dec | 13.4 · 11.2 · 10.7 · 9.7 · 4.5 · 9.6 · 11.7 · 11.9 · 14.1 | **10.8** | **12.6** | 10-K XBRL, FY2017-FY2025 |
| Archer-Daniels-Midland (ADM) | Dec | **UNAVAILABLE** | — | — | does not tag `OperatingIncomeLoss` |

**Corroborating metric, same sources — gross margin (%), most recent five fiscal years:**

| MGPI | BF-B | STZ | DEO | INGR |
|---|---|---|---|---|
| 31.7 · 32.4 · 36.4 · 40.7 · **37.2** | 60.5 · 60.8 · 59.0 · 60.5 · 58.9 *(FY26 60.5)* | 51.8 · 53.4 · 50.5 · 50.4 · 52.1 *(FY26 51.6)* | 42.3 · 43.4 · 43.7 · **43.5** | 19.3 · 18.8 · 21.4 · 24.1 · **25.3** |

- **Peers named: 5, of the 8 the industry leader itself names plus 2 ingredient processors** — so
  **5 attempted, 4 producing the metric, against Buffett's eight [E3-28]**. Six of the eight names
  in Brown-Forman's own sentence cannot be reached from SEC filings at all.
- **WHERE MGPI RANKS.** **Third of four on the 9-year operating-margin mean (11.4%), barely above a
  corn wet-miller; LAST of five on the recent three-year mean (3.6% against 12.6% for Ingredion and
  29.0% for Brown-Forman); and last on gross margin among the spirits filers, never within
  eighteen points of Brown-Forman in any year.** Its gross margin sits between Ingredion's and
  Diageo's — that is, **between a starch processor and a spirits company**, which is a fair
  description of what MGPI is.
- **Even the ex-impairment variant does not move the rank.** Adding back the goodwill, intangible
  and long-lived impairments (but not the contingent-consideration marks, which are real purchase
  cost — **[E5-33]**, *"to tell owners year after year, 'Don't count this' … is misleading"*):
  FY2023 **20.1%**, FY2024 **21.1%**, FY2025 **10.8%**. Still below every spirits peer in every
  year, and below Brown-Forman's **worst** year of the decade.
- **The row's limit, stated [E3-61].** *"In some businesses, the participants behave like a demented
  Kellogg. In other businesses, they don't … I think you'd have to know the people involved."* This
  row shows **position** and cannot show **conduct**. And it has a second limit specific to this
  name: **it cannot measure the leg that carries 34% of gross profit at all.** MGPI's contract- and
  bulk-distilling rivals are Kentucky and Indiana distillers that are privately or foreign held and
  file nothing; no SEC filing gives their cost per proof gallon. **The row therefore cannot
  establish or refute a cost advantage on the distilling leg, and I do not claim it does.** What
  the row does establish is the consolidated outcome, and **[E2-58]** does not need the peer row to
  reach its conclusion — the row would be needed to establish the *exception*, and the exception is
  what is missing.

### The remaining Q2 tests, each answered.

- **The two-characteristic test [E2-44].** Can it raise prices *"even when product demand is flat
  and capacity is not fully utilized"*? **No** — brown-goods net price/mix **−6%** with two of three
  distilleries idled from 2026-05-01. Can it grow dollar volume *"with only minor additional
  investment of capital"*? **No** — $661.2M of acquisition consideration plus $273.8M of cumulative
  inventory build plus $219.2M of 2021-2024 capex produced FY2025 sales of **$536.4M against
  FY2020's $395.5M**.
- **The attacker's test [E2-45]** — *"how I would like, assuming I had ample capital and skilled
  personnel, to compete with it."* Easily, and cheaply, right now: buy new-fill and aged whiskey at
  glut prices from the people who cannot sell it, rent rickhouse space from the same people, and
  put the brand spend behind a label. **That is not a hypothetical; it is what the industry did, and
  the 46% volume loss is the bill.**
- **Untapped pricing power [E3-33], scoped by [E5-28].** None. The claim would be a claim of
  *"a monopoly or a near monopoly"* and the row refuses it. **[E4-37]**'s inverse metric fires the
  wrong way: the tell of a weak business is *"the agony they go through in determining whether a
  price increase can be sustained"*, and this filer is not agonising over a price increase — it is
  conceding price and idling plant.
- **Direction outranks existence [E4-32].** The moat is **narrowing on every filed measure**:
  brown-goods volume −46%, mid tier −21% and value tier −32% over two years, goodwill $321.5M →
  **zero** by Q1 2026, indefinite-lived trade names to *"equal to the respective carrying values"* —
  **zero headroom** — and advertising and promotion cut 18% in Q2 2026. A widening moat *"is the
  primary criterion of a great business"*; this is its opposite.
- **The dominance class [E2-53]** — *"Once dominant, the newspaper itself, not the marketplace,
  determines just how good or how bad the paper will be."* **Refuted by the filings**: here the
  marketplace determined it. And customer concentration runs the other way — Note 13: *"one customer
  of the Branded Spirits segment accounted for approximately 16 percent of consolidated sales and
  one customer of the Ingredient Solutions segment accounted for approximately 14 percent"*, ten
  largest **54%**, up from 44% in 2023.
- **Key-person dependence [E4-23]: NOT a defect here, recorded so the absence is on the file.**
  Nothing in these filings makes the economics depend on a named individual. The three CEOs in
  nineteen months are a Q3 matter, not a Q2 moat defect.
- **[E4-04] is NOT the ground of this verdict.** Amended 2026-09-20, it is a **competence limit,
  never a fourth franchise criterion**, and on the branded leg alone it would give UNKNOWABLE
  without prejudice: a lapse in advertising spend on Penelope would *narrow* the brand, not destroy
  a structure that must be rebuilt from zero, which is the **[E3-49]/[E5-23]** maintenance case, not
  the competitive-destruction case. **The OUT below does not rest on [E4-04] and must not be read as
  if it did.**

### THE SOURCE OF THE RECORD — **[E4-36]**'s four causes, and **[E3-51]**.

*"When a surfer gets up and catches the wave and just stays there, he can go a long, long time. But
if he gets off the wave, he becomes mired in shallows"* **[E3-51]** — and *"A surfing run is not a
moat; the advantage lives in the wave, not the surfer."* Asked of **[E4-36]**'s four causes — extreme
max/min of one or two variables; a nonlinear combination; extreme performance over many factors;
wave-riding — the 2021-2023 record is **the fourth, plus an acquisition**, and both halves are
filed:

- The **level step in operating cash flow is 2020 → 2021** (a 2017-2020 mean of $35.0M against a
  2022-2025 mean of $99.1M) and **2021 is the Luxco merger year**. That half of the record was
  *bought*, two thirds of it with 22.8% of the company's own stock.
- The other half was the wave, and the filer says the wave has turned: *"structurally
  oversupplied."* **The surfer is off the wave**, and *"mired in shallows"* is a fair description of
  a 46% volume decline with two of three distilleries idle.

**Neither cause is ownable. That is the [E4-36] answer and it is the same answer the arithmetic
gave at flag (iv).**

### THE DISCONFIRMING CASE, put as strongly as I can make it **[E4-26]**, and why it does not carry.

*"you must not fool yourself, and you're the easiest person to fool"* **[E3-41]**, and the antidote
is to hunt hardest against the favourite hypothesis — which, for a run that has already found this
much, is OUT. So:

1. **Aged inventory is a genuinely scarce asset and time cannot be bought.** $301.7M of barreled
   distillate is four to eight years of somebody's patience. **Answer:** it is scarce only when the
   industry is short. In a glut everyone holds it, which is the definition of *"elevated
   industry-wide barrel inventory levels"*, and the filer is holding more of it every half-year
   (+$25.6M in H1 2026) while the price of selling it falls.
2. **Warehouse services is a toll road: $32.4M of stable, high-margin, switching-cost revenue.**
   **Answer:** it is real, it *"increased by high-single digits"* in Q2 2026, and it is **6.0% of
   FY2025 sales.** A toll booth on 6% of the company does not make the company a franchise, and its
   own driver is the customer barrels the glut put there.
3. **Penelope grew 13% in the latest quarter and premium plus has grown for three straight years.**
   **Answer:** accepted, and it is the strongest thing in the file. It is also $116.7M of sales, 22%
   of the company, sitting inside a reporting unit whose goodwill the company's own valuation
   specialist has written to zero. **A growing brand inside a written-off reporting unit is a
   reason to watch, not a franchise finding for the consolidated filer** — and **[E4-08]** sets the
   unit of the test as the company.
4. **"MGP rye" had genuine name recognition among craft brands.** **Answer:** I can find no filing
   that says so, by MGPI or by anyone else. Under PRIME RULE 1 and 3 it stays out of the file as an
   unsourced recollection, and the filed series — 46% of volume gone, price conceded, contracts not
   performed — is evidence against it rather than for it.

### VERDICT

**Criterion (2) of [E3-03] fails on the filer's own volume and margin series for the two legs that
carry 42.2% of gross profit, and it splits inside the third.** The commodity doctrine **[E2-58]**
applies to the distilling leg on the CEO's own statement of *"structurally oversupplied, with
excess capacity"*, and its single exception — *a cost advantage both wide and sustainable, "By
definition such exceptions are few"* — is not established, while the competitor row puts the filer
**last of five on the recent operating-margin mean and never within eighteen points of the branded
leader's gross margin.** The record's source is **[E4-36]**'s wave plus an acquisition, and *"a
surfing run is not a moat"* **[E3-51]**.

**This is a finding about the business, on filed evidence, and the document that would resolve it is
already read.** It is not a perimeter close: I am not saying durability cannot be judged; I am
saying the filings judge it and the answer is no. **[E4-04] is not invoked.**

- Class: [ ] WIDE [ ] NARROW [x] **NONE** [ ] PROVISIONAL · Direction: **narrowing on every filed
  measure**
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

---
# ⛔ THE FILE CLOSES HERE. Q2 IS OUT.

**Operator protocol rule 2: the hard sequence is a block, not a preference.** No Q5 output may be
reported unless Q1-Q4 each show IN. Q2 is OUT, so **Q3 through Q6 below carry NO VERDICTS** — they
are recorded because the reading is worth keeping, and because a later session should not have to
re-read nine filings to learn what is in them. **Every number below Q2 is descriptive. None of it
votes, and the valuation arithmetic in the Q5 block is headed COMPUTATION — NOT A CLEARANCE per
operator rule 3 and carries no entry language.**

**OUT is permanent about the business as the filings now stand [E4-19].** The reversal condition is
stated in words at Q6 and deliberately **not** as a price — the QLYS ruling: a name that failed on
the business gets no price alert, because that would be a category error.

---
# RECORDED BENEATH THE CLOSE — Q3 THROUGH Q6, NO VERDICTS

*The file closed at Q2. Nothing below is a verdict and nothing below votes. It is recorded because
the reading is worth keeping (operator rule 6's spirit: corrections and findings go on the record),
and because three of these findings would have changed the run's shape had the file survived to
them.*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? *(recorded, not scored)*

### STEP 1 — THE WEIGHT CASE, declared before anything else is written.

- [x] **Daily execution** — **[E3-38]**, its 1991 original **[E3-43]** and the 1977 root **[E2-70]**:
  an undifferentiated product magnifies the manager. Brown goods is bulk liquid sold per proof
  gallon and Q2 established it has close substitutes; the mid- and value-tier brands compete on
  shelf price. **Ticked.**
- [ ] **Control [E1-16]** — not applicable; this would be a minority public holding.
- [x] **Leverage [E3-29]** — total indebtedness **$376,850k** at 2026-06-30 against total equity of
  **$590,813k** and cash of **$17,794k**; a net-debt leverage ratio the filer reports as **3.5x
  against 1.8x a year earlier**; a covenant at 4.00x stepped to 4.50x; and inventory of
  **$408,416k**, which is **69% of equity and 108% of total debt**. **Ticked.**

**Two ticked, so had this file reached Q3, Q3 would have been a BINARY GATE and no price would
compensate [E1-16, E3-29, E5-35]:** *"You can turn any investment into a bad deal by paying too
much. What you can't do is turn any investment into a good deal by paying little."*

**And a structural fact that does not fit the three determinants, flagged as reasoning by analogy
and NOT as a corpus rule.** FY2025 10-K, Item 1A, verbatim: *"Under our Articles of Incorporation,
(i) holders of our preferred stock, par value $10.00 per share ("Preferred Stock"), are entitled to
elect five of our nine directors and (ii) only holders of our Preferred Stock are entitled to vote
with respect to a merger, dissolution, lease, exchange, or sale of substantially all of our
assets"*, and *"As of December 31, 2025, the majority of the outstanding shares of our Preferred
Stock is beneficially owned by one individual, who is effectively in control of the election of five
of our nine directors."* There are **437 preferred shares outstanding, $10 par, $4,370 of par value
in total.** **A block of stock worth four thousand three hundred and seventy dollars at par elects
the board majority and holds the only vote on selling the company.** The common holder of a $303M
company has four of nine directors and no vote on a sale. *(The corpus's [E1-16] weight determinant
is about the damage an owner cannot escape; this is its mirror and I am not claiming the row covers
it. Recorded as a finding with its source, not dressed as a rule.)*
**And the 8-K of 2024-09-30 (accession 0001628280-24-041543) moved in the same direction:** the
amended bylaws *"permit holders of the Company's preferred stock to act by majority written consent
in lieu of requiring unanimous written consent"* and *"remove a provision that had required that
all proxies, ballots, and vote tabulations identifying the particular vote of a stockholder be kept
confidential from the Board and the Company's officers and employees."*

### Honesty — binary, permanent, filings-based [E5-16], each matter dated to when it became PUBLIC.

**No integrity disqualifier was found in these filings.** Written as **[E5-17]** requires — *"A Q3
pass is the absence of found disqualifiers, not a finding that the managers are honest"*, because
*"Sincerity and empathy can easily be faked"*. Auditor's report clean; disclosure controls declared
effective; the 404(b) attestation box ticked; no restatement box ticked; no Item 4.01 or Item 4.02
in the filing index.

### STEP 2 — THE FLAGS. Each a prompt to read, never a verdict [E5-36, E5-38].

- **[x] EBITDA / adjusted-earnings promotion — [E4-29], the fifth flag, and this is the largest gap
  this project has recorded.** *"Trumpeting EBITDA … is a particularly pernicious practice … That's
  nonsense."* In the DEF 14A filed 2026-04-09 (accession 0000835011-26-000058) the committee
  reports, for the same fiscal year 2025 in which the filed Consolidated Statements of Income (Loss)
  show **operating income (loss) of $(94,615)k**:

  > *"Adjusted Operating Income | 70 | 89.2 million | 95"* and *"Adjusted EBITDA | 20 | 117.6
  > million | 94"* and *"Adjusted Basic EPS | 10 | 2.91 | 98"*

  **A $183.8 million gap between the pay metric and the filed GAAP operating line, in one year, and
  the executives were paid at 94-98% of target on the upper number.** GAAP basic EPS for FY2025 was
  **$(4.99)**; the incentive plan recorded **$2.91**. This is [E5-41]'s *"reverse float"* in its
  purest form: the expense already paid is exactly the one the measure deletes.
  **And the earnings release does the same in the headline.** 8-K EX-99.1 of 2026-02-25: the banner
  reads *"Full-year results above the top end of guidance"*, the quarter's $152.6M impairment is
  called *"a discrete, non-cash **adjustment** of $152.6 million to lower the carrying amount of
  goodwill and indefinite-lived intangible assets"*, and the $(6.22) quarterly EPS is followed in
  the next clause by *"Adjusted basic EPS decreased 60% to $0.63 per share."* The Q2 2026 release's
  *"Key Second Quarter Metrics"* table carries Adjusted net income, Adjusted EPS, Adjusted EBITDA and
  a Net debt leverage ratio, and the CEO's lead sentence is *"adjusted EBITDA and adjusted basic EPS
  came in ahead of our expectations."*
- **[x] Trumpeted earnings projections / growth targets — [E4-22]'s third flag, with [E5-30]'s
  ratchet.** Guidance is issued for sales, adjusted EBITDA, adjusted basic EPS, tax rate, share count
  and capex, and reaffirmed at every opportunity — 2026-02-25, again inside the 2026-04-07 idling
  release (*"Reaffirms full year 2026 financial outlook"*), again on 2026-07-29. **[E5-30]**: *"once
  you start it, it's all over. You can't quit … And forecasting earnings, I can't imagine anything
  more destructive."*
- **[E3-48] — the action on the projections flag: pull the past guidance and set it against the
  outturn.** The record is filed and it is a two-year descent.

  | adjusted EBITDA guidance | when | source |
  |---|---|---|
  | **$218 to $222 million** | confirmed 2024-08-01 | quoted in the 8-K EX-99.1 of 2024-10-17 |
  | **$196 to $200 million** | cut 2024-10-17 | 8-K EX-99.1, accession 0001628280-24-043025 |
  | **$120.0 million** (the 2025 STI target) | set early 2025 | DEF 14A 2026-04-09 |
  | **$90 to $98 million** | 2026-02-25, reaffirmed 2026-07-29 | 8-K EX-99.1 |

  **Guided adjusted EBITDA has fallen 56% in two years.** And the 2024-10-17 cut carries the
  then-CEO's own characterisation of the cause: *"The American whiskey category has successfully
  navigated periods of **temporary** supply-demand imbalance over the years"*. **Eighteen months
  later his successor's word for the same market is *"structurally oversupplied"*.** The base rate
  **[E3-48]** states — *"about nine cases out of ten"* of projections exist to justify a decided
  course — and the remedy, *"the record of the people who made the projections"*, is the table above.
- **[x] The "except for" flag — [E2-57].** *"you must count the runs scored against you in all nine
  innings … the real mistake is not the act, but the actor."* FY2025's Ingredient Solutions collapse
  is attributed in the 2026-02-25 release to *"a significant weather impact in the first quarter, and
  a number of **transitory headwinds**, including the impact of the failure of a key equipment outage
  in the second half of the year and high waste starch stream disposal costs."* That segment's gross
  margin has now fallen in **three consecutive years and again in Q2 2026** (35.6% → 20.1% → 12.7% →
  10.1%). The third consecutive year of a decline is not transitory.
- **[x] The restructuring/impairment charge — [E3-53], [E5-33].** *"a large chunk of costs that
  should properly be attributed to a number of years is dumped into a single quarter."* Three
  successive impairment events, all in Q4 or Q1, all excluded from the pay metric: **$73,755k
  (Q4 2024) + $152,622k (Q4 2025) + $180,277k (Q1 2026) = $406,654k in five quarters.** **[E5-33]**
  is explicit that these are real costs and belong in the owner-earnings mean: *"to tell owners year
  after year, 'Don't count this' … is misleading."* Against **$661.2M** of acquisition consideration,
  **$406.7M has now been written off — 61% of everything paid, inside five years of paying it.**
- **[ ] Serial share issuance — [E5-15]. DOES NOT FIRE as a promotion tell.** The one large issuance
  was acquisition consideration (5,009,206 shares, 22.8% of the company, April 2021) and the count has
  since *fallen* from 22.0M to 21.4M. **[E5-44]** is the live rule instead: *"The intrinsic value of
  the shares you give in an acquisition must not be greater than the intrinsic value of the business
  you receive."* MGP paid 22.8% of itself, valued at **$296,279k**, for a business whose entire
  goodwill is now zero.
- **[ ] Weak accounting: no instance found** on the machine-checkable items — SBC is expensed in
  every year, the pension disclosure is ordinary, the impairment assumptions are quantified (an *"11
  percent discount rate"* in 2025, *"a 10 percent discount rate"* in 2024) and the residual headroom
  is disclosed as a number both years: *"by a range of 0 percent to 30 percent"* (2025) and *"by a
  range of 10 percent to 20 percent"* (2024). **That headroom disclosure is a candor positive and is
  scored as one.**
- **[ ] Unintelligible footnotes: no instance found.** The notes are short, plainly written and the
  segment, inventory, business-combination and debt notes each answer the question they raise.
- **[ ] Filed-figure tells [E4-30]. DOES NOT FIRE.** Reported growth is not unnaturally smooth — it
  is violently unsmooth. Cash taxes as a share of reported pretax income: **24.8% (2023), 52.7%
  (2024)**, and not computable for 2025 against a pretax loss. The direction is up, not down, which
  is the opposite of the tell.
- **[ ] Metric-switching — [E2-49]. DOES NOT FIRE. This is its SIXTH failure** (after QLYS, CRM,
  CORT, PLTR, INOD), and the test was run properly across four proxies rather than assumed either
  way. The STI metrics and weightings are **identical** in the 2023, 2024, 2025 and 2026 proxies:
  Adjusted Operating Income 70%, Adjusted EBITDA 20%, Adjusted Basic EPS 10%, with Adjusted
  Operating Income named *"the core measure of performance"* in both the earliest and the latest.
  **No yardstick was disposed of.** What did change, recorded because it is real even though the
  flag misses it:
  - **The targets were reset down by a third.** Adjusted Operating Income target **$133,643k (2022)
    → $90.8 million (2025)**; Adjusted EBITDA target $155,991k → $120.0 million; Adjusted Basic EPS
    target $4.31 → $2.94. Resetting a target to a collapsed budget is the honest alternative to
    switching the metric, and **[E2-49]**'s demand is for *"pre-set, long-lived and small
    bullseyes"* — these are pre-set and small; they are not long-lived.
  - **A discretionary adjustment in the participants' favour**, disclosed: *"the Committee approved
    further adjustments to Adjusted Operating Income and Adjusted EBITDA of $1.6 million and Adjusted
    Basic EPS of $0.05 related to tariff impacts that were not reasonably predicable at the time the
    targeted achievement levels were originally approved"* (spelling *"predicable"* is the filed
    text, left unsmoothed — PRIME RULE 1). $1.6M on an $89.2M outcome against a $90.8M target is
    material to the payout.
  - **The long-term incentive horizon was SHORTENED to one year:** *"PSUs granted in 2025 have a
    one-year performance period, reflective of the current uncertainty affecting our industry."*
  - **And one change ran the other way, recorded under [E2-69]'s direction test:** the STI
    change-in-control provision moved from single trigger to **double trigger** effective 2025-01-01.
    A deviation toward shareholders is not the weak-accounting flag.
- **[x] Flags that converge — [E4-52], the lollapalooza.** *"extreme consequences from confluences of
  psychological tendencies acting in favor of a particular outcome."* Four of the flags above point
  the same way — an adjusted operating figure $183.8M above the GAAP line, reaffirmed guidance
  through a 56% two-year guidance descent, "transitory" applied to a three-year decline, and
  $406.7M of charges routed outside the pay metric — and **[E4-52]** says to read them as one
  reinforcing system rather than four prompts. *(Recorded with the id checked: **[E4-52]** is the
  lollapalooza row. **[E4-27]** is the incentives row and is used below for pay; the two are not
  interchangeable and every brief written for this queue before 2026-09-13 confused them.)*

### STEP 3 — THE PRIMARY TEST [E2-01]. *"a high earnings rate on equity capital employed (without undue leverage, accounting gimmickry, etc.) and not … consistent gains in earnings per share."*

Balance sheet before income statement, multi-year, from the filed statements:

| | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| total equity, $M | 201.4 | 231.0 | 262.5 | 644.8 | 746.7 | 850.5 | 834.2 | 718.4 |
| net income, $M | 37.3 | 38.8 | 40.3 | 91.3 | 109.5 | 107.5 | 34.7 | **−107.8** |
| **return on equity** | 18.5% | 16.8% | 15.4% | **14.2%** | 14.7% | 12.6% | **4.2%** | **−15.0%** |

**The pre-acquisition company earned a better return on equity than the post-acquisition company did
in any year.** 2018-2020 averaged 16.9%; 2021-2025 averaged 6.1%. The equity trebled in 2021 and the
return on it has fallen every year since.

**Scoped as [E2-43] scopes it for an acquisitive filer** — *"unleveraged net tangible assets … the
best guide to the economic attractiveness of the operation"*, with the goodwill wedge reported
separately rather than hidden in book equity. Net tangible assets (equity less goodwill less
intangibles): **$317.9M (2024), $358.0M (2025)**. Operating income excluding the impairments against
that base: **$148.3M / $317.9M = 46.6% (2024)** and **$58.0M / $358.0M = 16.2% (2025)**.
**That is the finding [E2-43] exists to produce, and it is the kindest number in this file: the
OPERATION is not the problem. The PRICE PAID for it was.** **[E2-73]** makes the same distinction —
*"what we pay for a business does not affect the amount of capital its manager has to work with"* —
and it is why the two yardsticks of **[E3-59]** separate here: on *"how well they run the business"*
the operators look competent against the hand they were dealt; on *"how well they treat their
owners"* the record below is what it is.

### Capital allocation — the rationality half [E2-29], and this is where the file's weight sits.

- **THE RETENTION TEST [E3-54] — at least $1 of market value per $1 retained, five-year rolling.**
  Retained earnings **$262.9M (2020-12-31) → $445.7M (2025-12-31) = $182.8M retained.**
  Market value: **16.9M shares x $47.06 = $795.3M** at 2020-12-31 against **21,294,315 x $24.30 =
  $517.5M** at 2025-12-31. **A change of MINUS $277.9M on $182.8M retained — and that is BEFORE
  crediting the $296.3M of stock the company issued into itself in April 2021.** At Friday's
  $14.13 the market value is **$302.6M**. **The test fails at roughly minus $1.52 of market value per
  dollar retained on the raw comparison, and worse once the issuance is netted.** From the 10-year
  high of **$125.50 on 2022-11-25** the fall is **88.7%**.
- **THE BUYBACK CONDITIONS [E5-08], and the third condition [E4-31].** *"first, a company has ample
  funds … second, its stock is selling at a material discount to … intrinsic business value,
  conservatively calculated"*, plus *"Shareholders should have been supplied all the information they
  need for estimating that value."* A $100,000k programme was announced 2024-02-29; **886,936 shares
  were repurchased in 2024 for $46,588k — an average of $52.53 a share.** The stock is **$14.13**, a
  **73% loss on the repurchase**, and $53,412k of the authorisation remains unused (none was used in
  2025). **The dating is the finding.** The same FY2024 10-K that reports those purchases reports the
  impairment test that triggered them into question: *"During the fourth quarter 2024, the Company
  experienced **a decrease in stock price and market capitalization** as well as experienced the
  effects of the softening alcohol industry which contributed to declines in current year
  consolidated results and forecasted outlook. Based on these factors, the Company performed a
  quantitative assessment of goodwill"* — and wrote off $73,755k. **In the same fiscal year the
  company told its auditors the share-price decline was evidence its assets were worth less, and told
  its owners the shares were worth buying.** Both statements may be sincere; **[E5-24]**'s first law
  governs either way — *"what is smart at one price is dumb at another"*. Stated with the humility
  clause **[E4-13]**: *"it is natural for CEOs to be optimistic about their own businesses. They also
  know a whole lot more about them than I do"*, and **[E5-08]**'s own *"many CEOs never stop believing
  their stock is cheap"*. **This is a capital-allocation flag, and it binds position size, never a
  discount rate** — and there is no position to size, because Q2 closed the file.
- **[E5-44] — the stock leg, measured at intrinsic value rather than at quote.** $296,279k of MGP
  stock was handed over on 2021-04-01, when the shares closed at **$59.39**. The entire goodwill it
  created is now zero and the trade names stand at fair value with no headroom. Whatever the shares
  were worth that day, **the business received in exchange no longer carries any of it on the balance
  sheet.**
- **[E2-52] and [E2-60] — the payout.** Dividends of **$10,675k (2023), $10,630k (2024), $10,325k
  (2025)** and **$5,196k in H1 2026**, declared without interruption through a $107.8M net loss, a
  $122.8M half-year loss, an operating cash outflow of $40.7M, and **$145,000k of new revolver
  borrowing in the same six months.** [E2-52]'s literal test is dividends funded by *issuance*, which
  does not fire; **[E2-60] is the row that does**: restricted earnings are those whose payout costs
  the business *"its ability to maintain its unit volume of sales, its long-term competitive
  position, **its financial strength**"* — *"where leverage rises to fund the payout, (c) was
  understated"* — and *"a company that consistently distributes restricted earnings is destined for
  oblivion."*
- **[E2-56] — the Pro-Am effect, judged segment by segment rather than on the blend.** *"Their
  marvelous core businesses … camouflage repeated failures in capital allocation elsewhere."* Here it
  runs the other way and is worth saying plainly: **Distilling Solutions and Ingredient Solutions
  earned $75.6M of FY2025 operating income between them on identifiable assets of $476.3M, while
  Branded Spirits — which holds $734.5M of the $1,235.9M of identifiable assets, 59% — lost
  $127.7M.** The capital went to the segment that has consumed it.
- **[E2-30] — the institutional imperative, all four scored. Not a fraud test:** *"Institutional
  dynamics, not venality or stupidity, set businesses on these courses."*
  - [x] **resists any change in current direction** — guidance reaffirmed at every opportunity
    including inside the release announcing two distilleries idled; the *"strategic roadmap"* language
    unchanged across four releases.
  - [x] **projects or acquisitions materialise to soak up available funds** — $219.2M of capex
    2021-2024 and $661.2M of acquisitions, immediately before a 46% volume decline.
  - [ ] **staff studies produced to justify the leader's craving** — no instance found in the
    filings; third-party valuation specialists were engaged for impairment testing, which is the
    ordinary use.
  - [x] **peer behaviour mindlessly imitated** — the filer's own words for the industry-wide
    capacity build it joined: *"Like many companies across the industry, we are navigating a
    challenging environment"*, and *"elevated industry-wide barrel inventory levels."*
- **[E3-58] — delegation and tenure.** Not a flag: there is no sign of consultant-led or
  banker-driven allocation in these filings. But the tenure point bites in reverse — **three chief
  executives in nineteen months** (Bratcher to 2024-12-31; Gall interim 2025-01-01 to 2025-07-20;
  Francis from 2025-07-21) **and three chairmen** (Seaberg to 2024-12-31; Donn Lux from 2025-01-01;
  Martin Roper by 2025-07-21), with the Chief Human Resources Officer and Chief Commercial Officer
  both terminated on 2026-02-20 (8-K accession 0000835011-26-000006). **The allocation decisions that
  produced the $406.7M of write-offs were made by people no longer at the company**, which is
  **[E2-57]**'s *"the real mistake is not the act, but the actor"* read at the institution rather than
  the individual.
- **[E4-39] — the rare-positive tell: a candid acquisition post-mortem, *"almost never witnessed"*.**
  **Not found.** No filing sets the Luxco or Penelope case as announced against the outturn. The
  impairment notes describe the write-down mechanically and never revisit the acquisition thesis.
  Its absence is the normal case and is scored as neutral, not as a flag.
- **[E4-27] — the incentives row, and it is the right id for pay.** *"Never, ever, think about
  something else when you should be thinking about the power of incentives."* In FY2025 the plan paid
  at 94-98% of target on a metric $183.8M above the filed operating line, in the year the company lost
  $107.8M, cut the value of its brands by $152.6M and held the dividend by borrowing. **That is what
  the incentive was pointed at, and the outcome is what it produced.**

### Candor [E2-26] — *"the business facts that we would want to know if our positions were reversed."*

**Two findings, one each way.**
- **Against.** The Chapter 11 of a significant customer is disclosed in the Q2 2026 10-Q with an
  allowance of **$2,148k** and the words *"the ultimate amount recoverable may differ from current
  estimates."* Eleven days later the company signed an amendment permitting **up to $20,000,000** of
  *"aggregate losses … related to accounts receivable from specific customers"* — plural — to be
  added back to covenant EBITDA through 2027-12-31. **The company negotiated relief sized at roughly
  nine times the loss it had booked, and the 10-Q reader is not told that number.** It is in the
  8-K, and only a reader who opened the "probably a credit facility" 8-K would ever put the two
  together. *(Note 13 records that one Branded Spirits customer was 16% of consolidated sales in
  2025, up from 13%, and that the credit-loss allowance sits in Branded Spirits. Whether that is the
  same customer is not stated in any filing and is **not asserted here.**)*
- **For.** The impairment notes disclose the residual headroom as a number in both years, including
  the uncomfortable one — *"the fair values of the Company's indefinite-lived intangible assets were
  equal to or exceeded the respective carrying values by a range of 0 percent to 30 percent"* (FY2025)
  and *"equal to the respective carrying values"* (Q1 2026). **Publishing a zero is the candor
  standard [E2-67] demonstrated**, and it is the single most useful sentence a reader of these
  filings is given.
- **[E2-68] — conduct across an information asymmetry.** The related-party disclosure passes on its
  face: *"The Company leased bottling and warehousing facilities in St. Louis, Missouri from
  Kemper-Themis, L.L.C. ("Kemper"), which was owned by Donn Lux, a member of the Company's Board of
  Directors. On October 31, 2023, the Company's Audit Committee and Board of Directors approved the
  purchase of the Kemper bottling and warehousing facilities from Kemper for $ 9,000 … The
  transaction was entered into at fair value based on **two independent appraisers' valuation**."*
  Disclosed, board-approved, twice appraised — and the counterparty became Chairman of the Board
  fourteen months later. **Recorded as read, not as a flag.**

### THE GUARDRAIL — checked, as the template requires.

- [x] Confirmed: **nothing in this Q3 is used to promote the name.** It could not be: Q2 closed the
  file, and **[E2-37]** governs — *"a good managerial record … is far more a function of what business
  boat you get into than it is of how effectively you row."* **[E2-38]**: *"Good jockeys will do well
  on good horses, but not on broken-down nags."*
- [x] **This business does not require a great manager**, so no [E4-23] moat defect is recorded at Q2
  on that ground.
- [x] Is a great manager the reason to act? **No, and the [E2-36] test is the right frame and it
  fails:** the damage here is not *"a localized excisable cancer"* in an intact franchise — Q2 found
  the franchise is the thing that is missing. **[E5-18]**'s capacity-to-stand-mismanagement test is
  also informative in the negative: this business has just demonstrated it cannot stand a
  $661.2M acquisition programme.

*(No verdict. The file closed at Q2.)*

## Q4 — WILL IT SURVIVE? *(recorded, not scored)*

### Owner earnings, with every window, because [E4-38] says publish them all.

**[E4-38]**: *"growth-rate presentations can be significantly distorted by a calculated selection of
either initial or terminal dates"*, and the remedy is to publish **every** window.

| window | perimeter | (c) = D&A | (c) = total capex |
|---|---|---|---|
| 9 years, 2017-2025 | **three companies** | $47.1M | $25.4M |
| 5 years, 2021-2025 *(the [E2-42] default)* | **two companies** | $69.1M | $37.9M |
| 3 years, 2023-2025 | **Atchison in for one of them** | $73.3M | $38.8M |
| **2 years, 2024-2025** | **ONE perimeter — the only clean window** | **$84.5M** | **$49.2M** |
| TTM to 2026-06-30, as filed | one perimeter | **−$5.6M** | **−$4.1M** |
| TTM to 2026-06-30, adding back the $48.7M earnout paid through operating | one perimeter | $43.0M | $44.5M |

- **The combined range across windows and capex ends runs from MINUS $5.7M to PLUS $84.5M.**
  **[E4-25]** is unambiguous about what that means: *"Usually, the range must be so wide that no
  useful conclusion can be reached"* — **and here the width is not only a capex judgment, it spans
  three different companies. That IS the conclusion**, and it is the honest close rather than a
  preference exercised.
- **The (c) judgment, disclosed as a guess because [E2-09] says it must be one.** *"(c) must be a
  guess — and one sometimes very difficult to make"*; *"I would rather be vaguely right than
  precisely wrong."* The corpus default is D&A **[E3-44, E2-41]**. **On this name the two ends have
  CROSSED**, which is worth naming: 2021-2025 capex averaged **$53.0M against D&A of $21.7M — 2.4x** —
  and the FY2026 plan is *"approximately $20 million"* against D&A of **$24.1M — 0.8x**. A business
  that spent 2.4x depreciation for five years and now plans 0.8x has not found efficiency; it has
  **stopped maintaining**, and the 8-K of 2026-04-07 says so in plant terms. **My disclosed guess for
  (c) is $45M to $55M**, at or modestly below the five-year capex mean of $53.0M and far above the $20M
  plan, because the plan is a shrinkage plan and not a maintenance level.
  **AND A DOUBLE-COUNT IS AVOIDED HERE ON PURPOSE.** [E2-23]'s working-capital clause says the
  increment *"also should be included in (c)"*, but this framework's own CONVENTION computes owner
  earnings from **operating cash flow**, which *"nets the working-capital change from one audited
  line"* — so the $273.8M of barrel build is **already inside the numerator**, and adding it to (c)
  as well would subtract it twice. **(c) above is maintenance capex alone.** The inventory finding does
  its work in the other direction, at flag (vi): the numerator will RISE in 2026-27 as the build stops,
  for a reason that is the opposite of maintenance.
  **And the honest consequence of that (c), stated because it does not help the OUT:** at (c) = $50M
  the FY2024-FY2025 mean owner earnings is **$57.5M** and the FY2021-FY2025 mean is **$40.9M** —
  yields of **19.0%** and **13.5%** on the $303M cap. **Even at the harshest defensible (c) the price
  clears the floor. The price is not what closed this file.**
- **Normalise DOWN for luck [E4-41]**, not up: *"Favourable exogenous breaks in the window are named
  and removed before the mean is trusted."* The favourable break is named by the filer — the American
  whiskey put-away boom — and the 2021-2023 numbers should be read net of it. The screen's
  `level_note` said *"STEP UP - normalize down [E4-41]"* and that instruction was correct.
- **[E3-55] — is the spread noise or level uncertainty?** *"If we have a business about which we're
  extremely confident as to the business result, we would prefer that it have high volatility."*
  **Not this case.** See's losing money eight months a year is a certain mechanism with a bouncing
  figure; here the *level* is in doubt, the perimeter changed three times, and the sign of the
  trailing-twelve-month figure depends on how one treats an earnout. **That is width, not noise.**
- **SBC subtracted in full [E5-06]** in every window; **[E3-70]**'s market-value measure was not
  reachable (no option-grant fair-value disclosure of the kind it asks for; RSUs and PSUs are the
  instruments), so the reported charge is used and flagged as **the floor of the subtraction, not the
  measure.**

### Great, good, or gruesome? [E4-20]

- [ ] great · [ ] good · [x] **gruesome, on the corpus's own definition** — *"The worst sort of
  business is one that grows rapidly, requires significant capital to engender the growth, and then
  earns little or no money"*, and the qualifier **[E4-43]** that only the gruesome fails: what makes
  cash consumption gruesome is *"unless the cash they consume gets to earn a reasonable return."*
  **$661.2M of acquisition consideration + $219.2M of 2021-2024 capex + $273.8M of cumulative
  inventory build = roughly $1.15 billion deployed since 2015, to arrive at FY2025 sales of $536.4M
  against FY2020's $395.5M, a FY2025 operating loss, and a market capitalisation of $303M.**
  **[E4-20]**'s own warning applies exactly: investors *"poured money into a bottomless pit,
  attracted by growth when they should have been repelled by it."*

### Staying power — score all three [E5-11]

1. **A large and reliable stream of earnings — FAILS on "reliable."** Sales $836.5M → $703.6M →
   $536.4M → guided $480-500M. Operating income $148.6M → $74.4M → $(94.6)M. Half-year net income
   $11.4M → $(122.8)M.
2. **Massive liquid assets — FAILS on "massive."** Cash **$17,794k** at 2026-06-30 against total
   indebtedness of **$376,850k**. What exists instead is **$338,000k of undrawn revolver**, and
   **[E5-39]** is explicit that this does not count: *"We will never be dependent on the kindness of
   strangers … cash is a lot like oxygen: you don't notice it 99.9 percent of the time. But if it's
   absent, it's the only thing you notice."* **No bank lines counted, no commercial paper, nothing
   depended on.** The one genuinely liquid asset is the **$408,416k of inventory**, of which **$301.7M
   is barrelled whiskey — liquid only into the market that is refusing it.**
3. **NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — FAILS, and this is *"the one that usually kills"*.**
   Three, all dated, all in the filings:
   - **$201,250k of Convertible Senior Notes are PUTABLE AT PAR ON 2026-11-15 — fifty-five days from
     this run.** Q2 2026 10-Q, Note 4: *"Holders of the 2041 Notes have the option to require the
     Company to purchase their notes on each of November 15, 2026, November 15, 2031 and November 15,
     2036 at a repurchase price equal to 100 % of the principal amount."* The conversion price is
     **$96.24** against a **$14.13** share price, so the option is worthless and a rational holder of
     a 1.88% fifteen-year note puts it at par. **The FY2025 10-K states the company's own expectation:**
     *"We expect some holders of the Convertible Senior Notes to require the Company to repurchase the
     Convertible Senior Notes during the fourth quarter of 2026."*
   - **$110,800k of Penelope earnout — already paid**, in H1 2026, funded by $145,000k of revolver
     draw. Done, and it is why debt rose $116.8M in six months.
   - **Up to $20,000,000 of receivable losses the company has already asked its lenders to
     disregard**, against a booked allowance of $2,148k.
- **[E2-54] — the coverage test, zip up your wallet.** *"whenever someone creates a capital structure
  that does not allow all interest, both payable and accrued, to be comfortably met out of current
  cash flow net of ample capital expenditures — zip up your wallet."* Interest paid FY2025:
  **$9,417k**, on debt that averaged well under $300M and included $201.25M at **1.88%**. **If the
  2041 Notes are put in November and refinanced on the revolver at its current 4.99%, the same debt
  costs about $6.3M a year more** — $201,250k x (4.99% − 1.88%) — taking pro-forma cash interest to
  roughly **$18-19M**, against FY2025's $9.4M. Set against the cleanest available current cash
  figure (H1 2026 operating cash before working capital and before the earnout, **$28.4M**,
  annualised to roughly $57M, less the company's own $20M capex plan) coverage is about **2.0x**.
  **That is met. It is not "comfortably" met**, and the covenant arithmetic is tighter than the
  interest arithmetic: net debt of $359.1M at a reported 3.5x implies covenant EBITDA near $102.6M,
  guidance is $90-98M, the covenant is 4.50x only until Q2 2027 and then **reverts to 4.00x** — at
  4.00x on $95M of EBITDA the ceiling is $380M of net debt against $359.1M today.
- **[E3-52] — read the terms, not just the quantity.** The good news and the bad news are both in the
  terms. The revolver runs to **2030** and $338M is undrawn; the secured notes are small ($13.6M) and
  run to 2027 and 2029; $55,000k of the floating exposure is swapped to fixed from 2026-06-30. **But
  the $201.25M convertible is the opposite of [E3-52]'s covenant-free, long-dated, customer-prepaid
  liability**: its 2041 maturity is cosmetic, because the holder's put makes it a fifty-five-day
  liability at the holder's option.
- **[E2-55] — score the worst case, not the expected one:** *"we do not wish it to be only likely
  that we can meet our obligations; we wish that to be certain … acceptable long-term results under
  extraordinarily adverse conditions."* **Not certain. Contingent on a revolver.**
- **[E5-29] — risk here means impairment, never price movement.** The 88.7% fall from the 2022 high
  is not the risk finding; the three near-term cash requirements are.

### Name the specific way THIS business dies [E2-27, E3-24] — quantified, with a stated likelihood.

**[E2-27]** is the mechanism, and it is the industry's own: *"Viewed individually, each company's
capital investment decision appeared cost-effective and rational; viewed collectively, the decisions
neutralized each other and were irrational … After each round of investment, all the players had more
money in the game and returns remained anemic."* **Every American whiskey producer built rickhouses
into the same boom. MGPI's share of that collective decision is $219.2M of 2021-2024 capex and
$273.8M of inventory, and the collective outcome is the 46% volume decline.**

**Consider some mathematics, in [E3-24]'s form.** The barrelled distillate is carried at
**$301,665k**. Suppose the glut resolves not through recovery but through the industry clearing
inventory at a discount, and MGPI's own barrels realise **75 cents on carrying value**: a **$75.4M**
pre-tax inventory charge, against total equity of $590.8M and covenant EBITDA near $100M. At 4.50x
that alone consumes headroom; if it lands after the covenant reverts to 4.00x in Q2 2027, the
arithmetic is tighter. Layer on the November 2026 put refinanced at revolver rates (+$6.3M of annual
interest), the $20M of receivable losses already carved out, and a dividend the company has not cut
($10.3M a year), and the sequence to a covenant breach is short, arithmetical and **does not require
the business to stop working.** **It requires only that the whiskey be worth less than it is
carried at.**

**Likelihood: [ ] likely · [x] A REAL POSSIBILITY · [ ] a low-level possibility.** Stated in
**[E3-24]**'s own vocabulary. It sits above a low-level possibility because the trigger is already
visible in three filed facts — the 0% headroom on the trade names, the $20M covenant carve-out, and
the filer's own *"structurally oversupplied"* — and below likely because the revolver is large, the
maturity is 2030, the banks gave the amendment *"the full participation of the banking group"*, and
the company retains a genuinely growing premium-plus brand.

**[E4-40] — model exposure, not experience.** *"all of us in the industry made a fundamental
underwriting mistake by focusing on experience, rather than exposure."* The relevant fact is not that
MGPI has never breached a covenant; it is that **24.4% of its assets is one commodity whose market
its own CEO calls structurally oversupplied**, and a benign loss history late in a good cycle is *"not
only useless, but actually dangerous"* as a guide.

### The survival shape — **[E3-51]** and `Screens/SURVIVAL SHAPES - index.md`

**Shape #20, THE WAVE** (first named at AEHR, 2026-09-18) is the fit, and the mapping is close enough
to be worth writing down: *one customer's capacity build in one new market makes the record; when that
market slows the systems and the per-device consumables stop together, the inventory built for the ramp
stays, and the next market must be found and funded again, with new stock.* Substitute *the American
whiskey put-away boom* for the one customer, *brown goods* for the systems, *warehouse services* for the
consumables, and *$301.7M of barrels* for the inventory built for the ramp. **Two features attach:
#11 THE PASS-THROUGH** (the boom's capacity gains went to the brand owners who buy the liquid —
**[E3-62]**'s second step, never asked) **and #5 THE SELF-LIQUIDATING DISTRIBUTION** (a $10.3M dividend
held through a $122.8M half-year loss by drawing $145M on the revolver — **[E2-60]**).

**RECORDED AS THE SIGNATURE WITHOUT THE VERDICT, on the PAGP precedent of 2026-09-20, and deliberately
NOT counted as an instance of #20.** The file closed at Q2 OUT; Q4 was never reached as a gate, so **no
shape is this business's named death.** The mapping is recorded so the next run in American whiskey
starts from the mechanism rather than rediscovering it, and so that no reader counts MGPI among the Q4
deaths.

*(No verdict. The file closed at Q2.)*

## Q5 — COMPUTATION — NOT A CLEARANCE

**Operator rule 3. Q1-Q4 do not all show IN, so no entry language may appear here and none does. The
business is judged before the price [E5-42].** This block exists for one reason: **the price is not
what closed this file, and a reader is entitled to know that.**

- market capitalisation, hand-struck: **$303M** (21,414,076 x $14.13, 2026-09-18)
- sovereign: **5.34%**, US Treasury 30-year par yield, 09/18/2026
- owner earnings, the screen's own band on the corrected cap: **$38M → 12.5%** · **$73M → 24.1%**
- the only one-perimeter window (FY2024-FY2025): **$49.2M → 16.2%** at the capex end, **$84.5M →
  27.9%** at the D&A end
- trailing twelve months to 2026-06-30, as filed: **negative at both ends**; adding back the earnout,
  **$43.1-44.6M → 14.2-14.7%**

**THE UNCOMFORTABLE PART, SAID OUT LOUD.** On every window except the trailing twelve months as
filed, the owner-earnings yield **clears the ~10% floor [E4-28] by a wide margin** — the screen's own
`growth_required` of **−0.48%** says the quote needs no growth at all — and at the corrected cap it
clears by more than the screen thought. **A run that skipped the business questions and went to the
arithmetic would have passed this name at a 12.5% to 24% owner-earnings yield.** The reason it does
not pass is **[E5-42]**: *"whether it's a good investment for us depends on how much we pay for that
in the end"* — the price question comes last, and the three before it are about the business.

**And the yield is high for a reason the arithmetic cannot see.** The numerator's best year, FY2025's
$121.5M of operating cash flow, contains **$26.2M of working-capital release from a shrinking
business** — operating cash before working capital fell from $163.4M to $95.3M over the same two
years — and the denominator is a price **88.7% below its 2022 high**. **A high yield on a melting
numerator against a collapsing denominator is not a discount; it is a description.** **[E4-25]** and
**[E3-17]** together are the guard: *"If the business earns 6 percent on capital over 40 years … you're
not going to make much different than a 6 percent return, even if you originally buy it at a huge
discount."*

**No bar is chosen and no margin of safety is applied, because neither is permitted here.**
**Windage count: zero — conservatism was not spent, because there is no valuation to protect.** The
sovereign is used bare: **[E3-42]**, *"use the government bond rate"*, and no per-name premium was
added to any rate anywhere in this file.

*(No verdict. Q5 does not open. Recorded as computation only.)*

## Q6 — WHAT WOULD PROVE ME WRONG? *(recorded, not scored)*

**[E1-02]**: *"I believe in establishing yardsticks prior to the act."* There is no act, so what
follows is a **reversal condition, stated in words and deliberately NOT as a price** — the QLYS ruling
of 2026-09-07: a name that failed on the business gets no price alert, because a price alert on a
business finding is a category error. **No band is armed in `tools/alerts.json` and no `PORTFOLIO.md`
row is added.**

**WHAT WOULD MAKE ME RE-OPEN THIS FILE — all of the first three, in filings, not in a release:**
1. **Brown-goods VOLUME growth for four consecutive quarters** in the filer's own volume/price
   attribution table — the series that fell 46%. Dollars will not do; **[E4-55]** requires the
   physical series, and dollar revenue flattered by pricing is precisely how this would hide.
2. **Warehouse services and brown goods both growing while barrel inventory FALLS** — that is the
   signature of the glut clearing rather than of the company laying down less.
3. **The 2041 Notes retired or refinanced on terms that do not raise cash interest above roughly
   $15M a year**, disclosed in a 10-Q or 8-K.
4. **A further trade-name impairment would confirm rather than reverse the finding**, and it is the
   most likely next filed event: the FY2025 10-K puts the residual headroom at *"0 percent to 30
   percent"* and the Q1 2026 test leaves the indefinite-lived intangibles *"equal to the respective
   carrying values."*

**What would NOT re-open it:** a lower price; an adjusted-EBITDA beat; a reaffirmed guidance range;
a premium-plus growth rate. **[E2-28]** rejects price appreciation and holding period as reasons to
act, and the mirror holds: a falling quote is not a reason either. **[E4-17]**'s *"beliefs change
quite gradually"* governs how this belief would be revised, and **[E2-40]**'s counter-trigger governs
what to do once revised.

**Position size: none. [E3-45]**'s direction — capital goes to rank #1 — and this name is not ranked.

*(No verdict. The file closed at Q2.)*

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 OUT, file closed; Q3-Q6 recorded
      beneath the close with **no verdicts attached**, per the standing practice of every recent run.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the only IN and
      it rests on the filer's own revenue-disaggregation and inventory notes.
- [x] Every UNRESEARCHED verdict names the artifact — **there are none in this file.**
- [x] Every UNKNOWABLE verdict states what specifically cannot be known — **there are none.** Q2 is
      OUT on filed evidence, not a perimeter close, and the file says so explicitly so that no reader
      mistakes it for an [E4-04] close.
- [x] Step 0: the filing was read, with accession numbers; **two** figures were cross-checked against
      the filed statements (FY2025 operating cash flow; 2025-12-31 inventory).
- [x] Owner earnings on a multi-year mean; **six windows** stated, not one; capex band disclosed as a
      judgment with the (c) guess named and reasoned; SBC subtracted in full in every window and
      confirmed to resolve in every year used.
- [x] Competitor row filled — **5 peers attempted, 4 producing the metric, census sourced from
      Brown-Forman's own 10-K**, with the unavailability of six of the eight industry names and of the
      entire contract-distilling peer set **stated as a limit** rather than silently omitted.
- [x] Sovereign is for the earnings currency (USD, argued from the 6.8%-foreign geographic footnote),
      from the issuing authority, dated.
- [x] Value stated as a range, not a point estimate — and headed **COMPUTATION — NOT A CLEARANCE**.
- [x] One bar chosen, not both — **neither**, because Q5 did not open. **Windage count: zero.**
- [x] Prices dated; the aggregator is used for live quotes only and is flagged, with the raw response
      written to the research folder.
- [x] Run committed to git, with a pathspec, in three commits (Step 0 + Q1; Q2; the close and the
      fold).
- [x] **Every distinct ledger id cited in this file was checked against `principle_ledger.csv` before
      it was written**, and **[E4-52]** versus **[E4-27]** was checked specifically, because that is
      the confusion every brief before 2026-09-13 carried.

## REGISTER
- Verdict: [ ] IN · [x] **OUT (about the business)** · [ ] UNRESEARCHED · [ ] UNKNOWABLE
- **One line:** *The CEO calls her own market "structurally oversupplied, with excess capacity and
  elevated inventory"; the filer's own attribution table puts brown-goods VOLUME down 46% in a year
  with price conceded 6% on top; the competitor row built from five peers' own filings puts MGPI last
  of five on the recent operating-margin mean and never within eighteen points of the branded leader's
  gross margin — so [E3-03] criterion 2 fails for the legs carrying 42% of gross profit and [E2-58]'s
  only exception, a cost advantage both wide and sustainable, is not established. The price was never
  the problem: at the hand-struck $303M cap the owner-earnings yield is 12.5% to 24%.*
- **Reversal condition (words, not a price):** four consecutive quarters of brown-goods VOLUME growth
  in the filer's own attribution table, with barrel inventory falling rather than rising, and the 2041
  Notes refinanced without materially raising cash interest.


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

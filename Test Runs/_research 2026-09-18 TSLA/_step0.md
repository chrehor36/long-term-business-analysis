## STEP 0: THE SKIP REASON, THE RATE, THE PRICE, THE COUNT, THE PERIMETER, AND THE FILING

### The skip reason, tested on the filing rather than inherited
The wave 5 row is *"perimeter or restatement above threshold: read the filing first"*; the skipped-reason list
says *"revenue step or cross-accession restatement above threshold."* **A prompt to read, never a verdict.**

**Which code produced the label.** Per the SNOW run's reading (Step 0 of `2026-09-18 Run - SNOW Snowflake.md`),
the triage guard order at `ce98258`/`a8bc84f` is: (1) `share_count_shift` outside **0.75-1.50x** returns
"perimeter"; (2) `scale_shift` **> 2.0** returns "perimeter by revenue step"; (3) `filed_years < 5`;
(4) `owner_earnings() == "CAPEX_UNRESOLVED"`; and `restatement_shift` is never called. Reproduced here with
`floor_screen.py` as it stood at `a8bc84f` (copied as `floor_screen_a8bc84f.py`) over companyfacts pulled
2026-09-18 and **cut to facts filed by 2026-09-01** (`triage_repro.py`, output `triage_repro_out.txt`):

| guard, in order | value | fires? | what it was reacting to, on the filings |
|---|---|---|---|
| 1. `share_count_shift` | **1.230x** | no (inside 0.75-1.50) | dei count 3,949,547,394 (2026-07-16) over 3,216,517,037 (2025-01-22). **Not a split** (the 5-for-1 of 2020 and 3-for-1 of 2022 both sit before the older observation; `split_factor_after("TSLA", "2026-07-16")` = 1.0). **It is real, and it is the CEO's pay**: 423,743,904 restricted shares of the 2025 CEO Performance Award issued at grant, and about 286.4M restricted shares from the June 2026 exercise of the 2018 award (below). Under the 1.50 line, so it did not fire. |
| **2. `scale_shift`** | **2.5079x** | **YES: THIS IS THE GUARD THAT RETURNED TSLA UNPRICED** | **A HOLE IN THE TAGGED SERIES, NOT A REVENUE STEP.** The `a8bc84f` `annual()` keeps the FIRST revenue element that yields any data (*"first tag that yields data wins"*), and Tesla's first `REV_TAGS` element, `RevenueFromContractWithCustomerExcludingAssessedTax`, carries total revenue only for **FY2018** (FY2018 10-K) and **FY2021-FY2025** (FY2023 10-K onward). **FY2019 and FY2020 are missing from that element**, so the function set FY2018 ($21,461.3M) beside FY2021 ($53,823.0M) as if they were consecutive years: a three-year ratio, 2.51x, read as a one-year step. The same totals sit unbroken under `Revenues` for every year FY2009-FY2025. **The largest real consecutive step in the window is FY2020 $31,536M to FY2021 $53,823M = 1.707x**, under the line, and it is what the current screen's `scale_shift` returns (1.7067, `probe_current_out.txt`). |
| 3. `filed_years` | 15 | no | |
| 4. `owner_earnings` | 5y D&A **$8,404M**, 5y capex **$3,146M** | no (priced, positive) | the triage stopped at guard 2 and never reached this |
| (`restatement_shift`, not a guard) | (1.0, FY2022) | n/a | a null, as at SMCI and SNOW |

**So the label was, for TSLA: a tag-coverage artefact in the revenue series (a two-year hole in the first element
read), not a perimeter event and not a restatement.** Checked on the documents as well as in the tags: the FY2025
10-K cover leaves the error-correction box unticked (*"reflect the correction of an error to previously issued
financial statements. o"*); the five 10-K/As in the filing index (FY2019, FY2020, FY2021, FY2024, FY2025) are
Part III amendments (the FY2025 one: *"The Original Form 10-K omitted Part III, Items 10 ... 11 ... 12 ... 13 ...
and 14"*); no 10-Q/A exists; and the FY2021-FY2025 revenue, operating-cash and SBC figures on the FY2023 and FY2025
10-K faces agree with companyfacts to the million. **The perimeter events that DO matter are newer than the
triage's data and run through the share count, not revenue** (below): the guard that would have seen them sat at
1.23x, under its line.

**What the current screen says behind the label (tagged data, a prompt only):** `owner_earnings()` prices TSLA at
5y D&A end **$8,394M**, 5y capex end **$3,146M**, 3y D&A end $7,937M, 3y capex end $2,457M;
`working_capital_flag` fires on 2022 (*"AccountsPayableAndAccruedLiabilities moved 41% of 2022 OCF"*), taken up at
Q4; `acquisition_flag` $64M over five years; `stale_filer` newest annual 2025-12-31. **The two capex ends are
$5.2bn a year apart**, which is the (c) question of Q4 in one line.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly
  by this run with the cache bypassed (`treasury_out.txt`: *"09/18/2026,...,5.38,5.34"*). `tools/sources.sovereign("USD")`
  returned the cached **09/17/2026 5.29%** row at 18:41 EDT (`step0_out.txt`), the stale-cache defect the SNOW run
  recorded; the newer issuing-authority figure is used. FRED was not used.
- **Earnings currency: USD for the reporting and the quote.** Revenue by sales location FY2025 (10-K segment note):
  United States $47,627M of $94,827M (50.2%), China $20,962M (22.1%), other international $26,238M (27.7%).
  Half the revenue is earned outside the US and reported in dollars; the cap is in dollars, so the dollar long bond
  pairs with it. No FX or ADR conversion applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$364.27, the close of 2026-09-18** (Friday). Source: Yahoo Finance daily chart via `sources._chart("TSLA",
  rng="1mo")` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`). Bar: open 369.28, high
  370.90, low 360.75, close 364.27, volume 51.8M; `regularMarketTime` 1789761600 = 16:00 EDT, so the figure is the
  closing print, not an intraday quote (the run was struck at 18:41 EDT).
- Recent closes: 09-10 $363.56 · 09-11 $365.44 · 09-14 $358.97 · 09-15 $356.58 · 09-16 $358.08 · 09-17 $366.20 ·
  09-18 $364.27. One-month range of closes $345.13-$376.37.
- **Primary-filing cross-check of the aggregator:** Form 4 accession `0001104659-26-106432` (Vaibhav Taneja, CFO)
  reports shares sold by the issuer for tax withholding on **2026-09-08 at a weighted $360.134**, inside Yahoo's 09-08
  bar (low $355.75, high $370.00). **The aggregator series is corroborated by a primary document.**
- **Split factor after the count's date: 1.0** (`sources.split_factor_after("TSLA", "2026-07-16")`). `close` used,
  never `adjclose`.

### The share count: from the cover, with the accession
- **3,949,547,394 shares**, from the cover of the **Q2 2026 Form 10-Q** (quarter ended 2026-06-30, filed
  **2026-07-23**, accession **`0001628280-26-049270`**): *"As of July 16, 2026, there were 3,949,547,394 shares of
  the registrant's common stock outstanding."* One class of common stock; *"Preferred stock; $ 0.001 par value; 100
  shares authorized; no shares issued and outstanding."*
- **THE COVER COUNT IS NOT THE ECONOMIC COUNT, and the gap is 10.7% of it.** The same 10-Q's income statement
  divides by **3,237M basic** weighted shares for the quarter (3,540M diluted) while the balance sheet reads *"3,949
  and 3,751 shares issued and outstanding as of June 30, 2026 and December 31, 2025"*. Note 9 explains the two blocks
  that are legally issued and outstanding but not in basic EPS:
  1. **423,743,904 restricted shares of the 2025 CEO Performance Award**, issued at grant and **unearned**: they are
     earned tranche by tranche only at market-capitalisation milestones of **$2.0 trillion to $8.5 trillion** plus
     operational milestones, and *"Unearned Shares will be forfeited and returned upon the 10-year anniversary"*.
     They *"vote proportionately"* until earned. Form 4 `0001104659-26-075213` (Elon Musk, 2026-06-16) footnotes
     the same *"423,743,904 shares of restricted stock"*.
  2. **About 286.4M restricted shares from the 2018 CEO Performance Award**, exercised in Q2 2026 after the
     Delaware Supreme Court reinstated it (*"our CEO exercised approximately 304.0 million of the stock options ...
     and elected to net settle the exercise price of his options, which amounted to approximately 17.5 million
     shares"*; Form 4: 303,960,630 exercised at $23.34, 17,531,857 withheld at $404.66). These carry a service
     condition to 2028-01-19 but were fully vested options before; **they are an economic claim now**, and the
     diluted count already carried them.
  The 96M-share 2025 CEO Interim Award was **forfeited** on 2026-04-21 (*"no double dip"*), so it is not in the
  July count.
- **Treatment, displayed side by side and not blended:** the cover count is the legal count; **the economic count
  is the cover less the 423,743,904 unearned 2025-award shares = 3,525,803,490.** The unearned shares enter the
  equity only if the company is worth $2 trillion or more, at which point any cap computed here is moot; they are a
  Q3 matter (what pay vests on) before they are a Q5 one.

### The perimeter between the business and the common holder: stated, not blended
1. **Cash and investments at 2026-06-30: $43,524M** (cash $15,219M, short-term investments $28,305M), against
   **debt and finance leases of $9,342M** ($1,418M current, $7,924M non-current); digital assets $674M.
2. **A $2.00bn equity stake in SpaceX, bought from the CEO's other company.** Note 13: *"the Company invested $ 2.00
   billion in SpaceX common stock (formerly a preferred share investment in xAI) representing an ownership interest
   of less than 1 % in March 2026"*, carried at fair value, with a **$1,005M unrealized gain** in H1 2026 (cash-flow
   face). It is in other non-current assets. Taken up at Q3 (related party).
3. **No convertible notes, no preferred, no live deal.** `sources.deal_filings("0001318605")` returned `([], [],
   '2026-01-29')` and `deal_note` an empty string; every 8-K in 2026 carries Items 2.02 and 9.01 only
   (`filings_list.txt`). The quote is an owner-earnings price, not a spread.

### The market cap
- **Legal: $364.27 x 3,949,547,394 = US$1,438,702M ($1.44 trillion).**
- **Economic (unearned 2025-award shares excluded): $364.27 x 3,525,803,490 = US$1,284,344M ($1.28 trillion).**
- Net cash and investments of about $34.2bn ($43.5bn less $9.3bn of debt and finance leases) is 2.4-2.7% of either;
  shown, not netted. Split factor after 2026-07-16 = 1.0.

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2025 Form 10-K**, fiscal year ended 2025-12-31, filed **2026-01-29**, accession **`0001628280-26-003952`**
  (`10K_FY2025.txt`); auditor **PricewaterhouseCoopers LLP**, San Jose, report dated January 28, 2026, *"We have
  served as the Company's auditor since 2005."* Part III in the **10-K/A** filed 2026-04-30, accession
  **`0001104659-26-053166`**.
- **Q2 2026 Form 10-Q**, quarter ended 2026-06-30, filed **2026-07-23**, accession **`0001628280-26-049270`**; the Q1
  2026 10-Q (`0001628280-26-026673`).
- Also read: 10-Ks FY2024 (`0001628280-25-003063`), FY2023 (`0001628280-24-002390`), FY2022 (`0000950170-23-001409`),
  FY2021 (`0000950170-22-000796`); the DEF 14A of 2025-09-17 (`0001104659-25-090866`); the 8-K EX-99.1 releases
  named at Q3; and the Form 4s above.
- **Figures cross-checked against the filed statement** (FY2025 consolidated statement of cash flows): *"Net cash
  provided by operating activities | 14,747 | 14,923 | 13,256"*, *"Stock-based compensation | 2,825 | 1,999 |
  1,812"* and *"Purchases of property and equipment excluding finance leases, net of sales | ( 8,527 ) | ( 11,342 ) |
  ( 8,899 )"* match companyfacts (capex FY2024 tagged $11,339M against the face's $11,342M, and FY2023 $8,898M
  against $8,899M: the FY2023 10-K face reads *"( 8,898 )"*, so the later face re-presented it; both differences are
  $1-3M and immaterial). **One tagged series does not match the face**: `da_annual()` returns FY2025 D&A $5,030M
  while the face line is *"Depreciation, amortization and impairment | 6,148"*; the difference is impairment and is
  taken up at Q4.


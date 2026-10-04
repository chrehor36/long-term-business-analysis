# Company Run — Tesla, Inc. (TSLA) — 2026-09-18
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs. **This is a NEW NAME, not a
holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.**

Filled top to bottom. **Stop at the first verdict that is not IN.** Run unattended from scratch on 2026-09-18
(evening, EDT). No prior run file for TSLA exists; the TM run of 2026-09-13 carried Tesla as a line in its
automaker competitor row, and every TSLA figure below is recomputed from Tesla's own filings. WAVE 5, the third
of the seven "perimeter or restatement above threshold" names. Research, scripts and downloaded filings are in
`Test Runs/_research 2026-09-18 TSLA/`.

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

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### The unit economics, in my own words, without management's language
Tesla builds battery cars in plants it mostly owns (Item 2: Texas, Fremont, Nevada and Berlin owned; Shanghai
buildings owned on 50-year land-use rights; New York and the Lathrop battery plant leased) and sells them through its website and *"a global network of company-owned
stores"* (Item 1), with no independent dealer, mostly for cash or a third-party loan and some on its own leases. It keeps the difference between the price of the car and what the parts,
labour and plant wear cost to build it, and then pays for engineering, selling and head office out of that
difference. Beside the cars it sells three smaller things: large battery installations to power companies
(Megapack) and home batteries; used cars, repairs, charging sessions, insurance and parts; and **"regulatory
credits"**, which are permissions other carmakers buy from Tesla because governments fine carmakers whose
fleets pollute more than a set limit. The credits cost Tesla nothing to make.

FY2025 10-K (accession `0001628280-26-003952`) and FY2023 10-K (`0001628280-24-002390`), statements of
operations and segment note, $M:

| line | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---:|---:|---:|---:|---:|---:|
| Automotive sales | 44,125 | 67,210 | 78,509 | 72,480 | 65,821 | 35,479 |
| cost of automotive sales | 32,415 | 49,599 | 65,121 | 61,870 | 56,267 | 29,482 |
| **gross margin on cars sold** | **26.5%** | **26.2%** | **17.1%** | **14.6%** | **14.5%** | **16.9%** |
| Automotive regulatory credits (no cost) | 1,465 | 1,776 | 1,790 | 2,763 | 1,993 | 526 |
| Energy generation and storage revenue | 2,789 | 3,909 | 6,035 | 10,086 | 12,771 | 5,547 |
| energy gross margin | -4.6% | 7.4% | 18.9% | 26.2% | **29.8%** | 28.7% |
| Total revenues | 53,823 | 81,462 | 96,773 | 97,690 | 94,827 | 50,623 |
| **Income from operations** | 6,523 | 13,656 | 8,891 | 7,076 | **4,355** | 1,339 |
| operating margin | 12.1% | 16.8% | 9.2% | 7.2% | **4.6%** | 2.6% |
| **operating income less regulatory credits** | 5,058 | 11,880 | 7,101 | 4,313 | **2,362** | 813 |
| consumer vehicles delivered (MD&A) | 936,222 | 1,313,851 | 1,808,581 | ~1,789,000 | ~1.64 million | ~838 thousand |
| automotive sales per car delivered ($000) | 47.1 | 51.2 | 43.4 | 40.5 | ~40.1 | ~42.3 |

Read as a car manufacturer that also sells batteries:
1. **The car business earns what any car business earns when its price falls.** Revenue per car delivered fell
   from about $51k (FY2022) to about $40k (FY2025) while the gross margin on cars fell from 26.2% to 14.5%. The
   10-K's own account of how it sells: *"Our cost reduction efforts, cost innovation strategies, and additional
   localized procurement and manufacturing are key to our vehicles' affordability and have allowed us to
   competitively price our vehicles"* (MD&A, 2026 Outlook).
2. **Units have fallen for two years.** 1.81 million (FY2023), about 1.79 million (FY2024), about 1.64 million
   (FY2025); H1 2026 about 838 thousand, up about 18% on a prior-year half depressed by the Model Y changeover
   (10-Q MD&A: *"in part from bringing down all of our vehicle factories simultaneously for the changeover to the
   New Model Y in the prior period"*).
3. **The free credits are a large share of the profit.** Regulatory credits were **46% of FY2025 operating
   income** ($1,993M of $4,355M) and 39% of FY2024's. They are falling: H1 2026 $526M against $1,034M (*"decreased
   $508 million, or 49%"*, 10-Q MD&A). Their price is set by governments' fleet rules, not by Tesla.
4. **The battery business is the part that grew and earns more per dollar.** Energy revenue rose 4.6x in four
   years to $12.8bn and its gross margin from negative to 29.8%; it produced **$3.8bn of the $17.1bn** FY2025
   segment gross profit (22%). FY2025 deployments 46.7 GWh (MD&A).
5. **Everything else the company describes as its future has no separate revenue line.** FSD (Supervised)
   revenue is recognised inside automotive sales and deferred revenue (FSD and related deferred revenue $3,867M at
   2025-12-31, $956M recognised in FY2025); Robotaxi, launched June 2025, and Optimus are not segments and carry no
   disclosed revenue.

### The scarce input this business controls
**Not the factories and not the product category**: every competitor in the TM run's row builds battery cars
in owned plants. The 10-K itself names what Tesla believes it controls: cost (*"our ongoing cost reduction
efforts ... vertical integration and supply chain localization will continue to benefit us in relation to our
competitors"*), software, a fleet collecting driving data for FSD, the Supercharger network (now opened to other
makers under NACS: *"as other automotive manufacturers have announced their adoption of NACS and agreements
with us to utilize our Superchargers"*), and a brand sold without dealers (*"Historically, we have been able to achieve sales without relying on
traditional advertising and at relatively low marketing costs"*, Item 1).
Whether any of these is a position or a lead is a relative claim and is Q2's question. **One scarce input is
plainly not the company's**: the regulatory credits, whose value is set by rules in the US, Europe and China.

### Will the fundamentals look broadly the same in ten years?
**The company says no, deliberately.** The first sentence of the FY2025 MD&A and of the Q2 2026 10-Q MD&A: *"We
are focused on bringing artificial intelligence into the real world, through products and services like FSD
(Supervised) and Robotaxi, as well as working to develop and commercialize AI robots (including Optimus). We intend
to leverage our current operations ... to achieve that objective."* Research and development rose from $3,969M
(FY2023) to $6,411M (FY2025) and $4,317M in H1 2026 alone; the CEO's 2025 award is earned on 20 million
vehicles, 10 million FSD subscriptions, **1 million bots** and **1 million Robotaxis** (10-Q Note 9).

**The car and battery businesses, as mechanisms, probably yes**: build a car or a battery in an owned plant, sell
it for cash above its cost. That mechanism has been the same in every 10-K on disk (FY2021-FY2025): automotive and
energy revenue together were $82.3bn of $94.8bn in FY2025 (86.8%), and the remaining "services and other"
($12.5bn) is used cars, repairs, charging, insurance and parts sold to the same fleet (Item 1).

**The honest limit, stated rather than smoothed.** [E3-31] asks for businesses *"relatively simple and stable in
character"* and adds *"If a business is complex or subject to constant change, we're not smart enough to predict
future cash flows."* I can say how Tesla makes its money today: a markup on cars and batteries, plus credits a
regulator creates. **I cannot say how it will make money if its stated objective succeeds**, because no filing
shows the unit economics of a Robotaxi fleet or a humanoid robot, and [E4-46] says that studying for months does
not repair that: *"if we can't make a decision in five minutes, we can't make it in five months."* That part is
outside the circle and is not what this verdict covers. **The verdict covers the business the filings show**, and
whether the car and battery business has a position that survives the change the company is choosing is a moat
question: carried to Q2, where the AI businesses would have to show up as a franchise in the filed record or not
count.

- **VERDICT: [x] IN** on the business the filings show (cars, batteries, credits and fleet services, the whole of
  disclosed revenue): the unit economics are stated above from the filed statements in my own words, and the
  figures reconcile to the faces of the FY2023 and FY2025 10-Ks and the Q2 2026 10-Q. **Not IN** for the AI and
  robot businesses, which have no revenue line to understand; they are recorded as outside the circle [E3-31,
  E4-46] and **cannot be counted at any later gate**, including Q5.

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

### WHAT IS BEING TESTED
The business Q1 found understandable: cars (automotive segment 78% of FY2025 segment gross profit, $13,292M of
$17,094M, with regulatory credits and fleet services inside it), and batteries (energy segment 22%, $3,802M).
The AI and robot businesses are outside the circle (Q1) and cannot supply the moat here. **The hypothesis to be
refuted, at full strength**: Tesla is the one carmaker whose record differs from the industry's, because it
earned the highest margin in the automaker row without a finance arm, sells without dealers, makes its own
software, cells and chargers, and built a charging network its rivals adopted.

### THE CASE FOR, AT FULL STRENGTH **[E4-26, E4-51]**
1. **The best five-year margin in the row.** Consolidated GAAP operating margin pooled FY2021-25 **9.54%**
   (TM run's row, recomputed here from Tesla's faces: 12.1 / 16.8 / 9.2 / 7.2 / 4.6), above Toyota's automotive
   8.22% all-in and GM's 5.39% consolidated with GM Financial inside it; and pre-tax return on capital employed of
   **57.5% in FY2022** (`roc_out.txt`), a figure no volume maker in the TM row approaches.
2. **A charging network the industry adopted.** 8,704 Supercharger stations and 82,357 connectors at Q2 2026,
   +17-18% a year (Q2 2026 Update, 8-K `0001628280-26-049213`); *"as other automotive manufacturers have
   announced their adoption of NACS and agreements with us to utilize our Superchargers"* (10-K MD&A).
3. **Software sold after the car.** Active FSD subscriptions 0.95M to **1.48M** in a year (+56%), *"over 55% of new
   deliveries including FSD subscriptions"* in North America (Q2 2026 Update); services and other gross profit a
   record $648M in Q2 2026.
4. **The battery business beats its filed rival.** Energy gross margin 18.9% / 26.2% / **29.8%** (FY2023-25)
   against Fluence's 13.1% (FY Sep-2025) and 6.5% (9M FY2026), per the FLNC run's accessioned row; per kWh, the
   FLNC run computed Tesla's CY2025 gross profit at about $81/kWh against Fluence's $60 **while charging about 40%
   less per kWh**.
5. **Volume is recovering.** Q2 2026 deliveries 480,126, **+25% year on year**, a record second quarter (Q2 2026
   Update); H1 2026 about 838 thousand.

### THE THREE CONDITIONS **[E3-03]**
- **(1) Needed or desired: YES.** 1.64 million cars and 46.7 GWh of storage sold in FY2025.
- **(3) Not subject to price regulation: YES for the car; but 46% of FY2025 operating income was set by a
  regulator.** Regulatory credits ($1,993M of $4,355M) exist only because governments fine fleets above an
  emissions limit, and the regime is being withdrawn: *"In 2025, governmental and regulatory actions, such as
  OBBBA, have restricted certain regulatory credit programs tied to our products. Furthermore, we are impacted by
  the demand for credits by other automobile manufacturers"* (FY2025 10-K MD&A); H1 2026 credits **-49%**. That is
  **[E2-59]**'s class: the profit *"may be escaped, true, if prices or costs are administered"*, and the moat
  belongs to the **regime**, not the business. **Operating income less credits: $11,880M (FY2022), $7,101M,
  $4,313M, $2,362M (FY2025), $813M in H1 2026.**
- **(2) No close substitute: NOT SHOWN, AND CONTRADICTED IN TESLA'S OWN FILINGS.**
  - **The company says its customer has substitutes.** *"Competing products typically include internal
    combustion vehicles from more established automobile manufacturers; however, many established and new
    automobile manufacturers have entered or have announced plans to enter the market for electric and other
    alternative fuel vehicles ... Model 3 and Model Y compete with small to medium-sized sedans and compact SUVs,
    all of which are extremely competitive markets"* (FY2025 10-K Item 1, Competition). And in Item 1A: *"Many of
    our competitors have significantly more or better-established resources than we do ... and may achieve
    additional cost efficiencies owing to location and economic environments. Increased competition could result
    in our lower vehicle unit sales, price reductions, revenue shortfalls, loss of customers and loss of market
    share."*
  - **The price record shows the customer treats them as substitutes.** Three consecutive 10-Ks explain falling
    revenue per car with price cuts and incentives: FY2023 *"a lower average selling price on our vehicles driven by
    overall price reductions year over year"*; FY2024 *"lower average selling price on our vehicles driven by overall
    price reductions and attractive financing options"*; FY2025 *"a lower average selling price per unit driven by
    sales mix and higher customer incentives such as attractive financing options."* Revenue per car delivered fell
    from about $51.2k (FY2022) to about $40.1k (FY2025), -22%, and the gross margin on cars from 26.2% to 14.5%.
  - **And the cuts were made with idle capacity.** The Q4 2023 Update (8-K EX-99.1, accession
    `0000950170-24-007073`) lists *"Current Installed Annual Vehicle Capacity"* of about **2.35 million** (California
    100,000 S/X and 550,000 3/Y, Shanghai >950,000, Berlin 375,000, Texas >250,000 Model Y and >125,000 Cybertruck),
    against deliveries of about 1.79 million in FY2024 (76%) and about 1.64 million in FY2025 (70%); the Q2 2026
    Update lists >2.375 million with Cybercab, against a Q2 2026 production rate of about 1.81 million annualised. [E2-58]: *"persistent over-capacity without administered prices (or costs) equals poor
    profitability"*, with profitability set by *"the ratio of supply-tight to supply-ample years."* **Tesla's margin
    peak sits exactly in the supply-tight years** (FY2021-22, when the whole row printed its best numbers) and its
    fall exactly in the supply-ample ones.

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4)*
**Built from the TM run's accessioned row** (`Test Runs/_research 2026-09-13 TM/peers/COMPETITOR ROW - five-year
industrial margins.md`: GM 10-Ks `0001467858-26-000013`, `-25-000032`, `-24-000031`; Ford `0000037996-26-000015`,
`-25-000013`, `-24-000009`; Honda 20-Fs `0001193125-26-274991` and earlier; Stellantis 20-Fs `0001605484-26-000021`
and earlier; VW Annual Report 2025 on its IR site; Hyundai 2025 audited statements), with **every Tesla figure
recomputed here from Tesla's own faces** (FY2021-FY2025 10-Ks listed at Step 0), and matching the TM row to the
hundredth. **Same window (five latest fiscal years, March year-ends aligned to the calendar year inside them).**

| Operating margin, % | CY21 | CY22 | CY23 | CY24 | CY25 | 5-yr pooled | measure · source |
|---|---:|---:|---:|---:|---:|---:|---|
| **TESLA consolidated** | **12.12** | **16.76** | **9.19** | **7.24** | **4.59** | **9.54** | GAAP income from operations · Tesla 10-Ks |
| **TESLA less regulatory credits** | **9.66** | **14.91** | **7.48** | **4.54** | **2.54** | **7.40** | same, credits removed from income · computed here |
| Toyota automotive | 7.99 | 6.45 | 11.20 | 9.12 | 6.11 | 8.22 | IFRS segment operating income, all charges in · 20-F |
| GM consolidated | 7.34 | 6.58 | 5.41 | 6.82 | 1.57 | 5.39 | GAAP operating income, incl. GM Financial · 10-K |
| GM (GMNA+GMI) | 9.82 | 9.83 | 8.59 | 8.65 | 6.67 | 8.60 | EBIT-adjusted (non-GAAP) · 10-K Note 23 |
| Ford consolidated | 3.32 | 3.97 | 3.10 | 2.82 | (4.90) | 1.46 | GAAP operating income · 10-K |
| Honda automobile | 2.52 | (0.15) | 4.07 | 1.69 | (9.96) | (0.62) | IFRS segment profit · 20-F |
| Stellantis (vehicle segments) | 12.54 | 13.67 | 13.65 | 5.90 | 0.49 | 9.61 | AOI (non-GAAP) · 20-F |
| Volkswagen Automotive Division | 6.4 | 7.1 | 7.0 | 5.6 | 1.8 | ≈5.6 | IFRS operating return on sales · AR 2025 |
| Hyundai vehicle segment | n/o | n/o | n/o | 8.10 | 5.05 | | K-IFRS · 2025 audited statements |
| BYD | blocked | | | | | | TM run: IR site HTTP 504; HKEX annual report not obtained |

*Tesla less credits*: (operating income less credits) / (revenue less credits): FY2021 5,058/52,358; FY2022
11,880/79,686; FY2023 7,101/94,983; FY2024 4,313/94,927; FY2025 2,362/92,834; pooled 30,714/414,788. **H1 2026:
Tesla 2.6% consolidated and 1.6% less credits** (10-Q).

| Other same-window facts | Tesla | Toyota | GM | Ford | Stellantis |
|---|---|---|---|---|---|
| Units, latest vs peak inside the window | 1.64m (CY25) vs 1.81m (CY23): **-9%** | 9,595k, at its high | 3,799k vs 4,010k | 4,394k | 5,484k vs 5,836k |
| Pre-tax return on capital employed (Tesla, `roc_out.txt`) | **57.5% (CY22) → 26.7% → 16.6% → 9.4% (CY25); 5.1% less credits** | | | | |
| Own words on price | *"price reductions"*, *"attractive financing options"*, *"higher customer incentives"* | *"further downward price pressure"* | *"excess capacity and high fixed costs"* | *"pricing pressure resulting from industry excess capacity"* | *"intense price competition"* |

- **Peers taken: 9** (Toyota, GM, Ford, Honda, Stellantis, Volkswagen, Hyundai, BYD, plus Fluence for the energy
  segment) of an industry whose at-scale competitors in the 10-K's own words are *"a significant and growing
  number of established and new automobile manufacturers"*; five complete from SEC filings, VW on company-stated
  ratios, Hyundai on two years, **BYD blocked** (TM run's recorded obstacle; not re-attempted). **Can I name the
  document? Yes: BYD's 2025 annual report on HKEXnews.** It is a work order for any future upgrade and not for this
  verdict, for the FLNC run's directional reason: an absent low-cost rival can only make the attack stronger; it
  cannot rescue a moat that the present row and Tesla's own words already refute. For the energy segment,
  CATL, Sungrow and Wärtsilä are not SEC registrants and were not pulled (the FLNC run's stated limit).
- **The row's limit [E3-61]:** it shows position, not conduct; *"I think you'd have to know the people
  involved."*

**WHAT THE ROW ESTABLISHES, in both directions.**
1. **Tesla's five-year record DOES lead the row, and that is said first [E4-26].** Its pooled 9.54% is the highest
   consolidated GAAP figure, and even less credits (7.40%) it is above GM's GAAP 5.39%, VW's ≈5.6% and Ford's 1.46%.
2. **But the lead was made in two years and is gone.** FY2022 (16.76%) and FY2021 (12.12%) carry the pool; by
   FY2025 Tesla's 4.59% is **below Toyota's all-in 6.11% and Hyundai's 5.05%**, and less credits (2.54%) it is
   below Toyota, Hyundai and GM's adjusted measure (6.67%), above only the makers in charge years (GM GAAP 1.57%,
   VW 1.8%, Stellantis 0.49%, Ford, Honda). H1 2026 (2.6%;
   1.6% less credits) is lower again, while deliveries rose 18% in the half. **A lead that exists only in the
   supply-tight years is [E2-58]'s ratio, not a cost advantage "both wide and sustainable"**, and the corpus says
   *"By definition such exceptions are few."*
3. **Return on capital tells the same story from the balance sheet [E3-46]**: 57.5% to 9.4% pre-tax in three
   years, 5.1% less credits, while capital employed rose from $26.8bn to $47.2bn. The best businesses *"earn very
   high returns on capital employed over time"*; this one earned them for a period.

### THE OTHER Q2 TESTS
- **The two-characteristic test [E2-44], both legs fail.** (1) Price rises *"even when product demand is flat and
  capacity is not fully utilized"*: the record is the reverse, price **cuts** with a quarter to a third of installed
  capacity idle. (2) Dollar volume *"with only minor additional investment of capital"*: capital expenditure $6,482M /
  $7,158M / $8,898M / $11,342M / $8,527M (FY2021-25) against D&A of $2.9-6.1bn, and **$8,282M in H1 2026 alone**
  (Q2 alone $5,789M per the Update) for flat-to-lower revenue from FY2023 to FY2025.
- **Untapped pricing power [E3-33]: none**, and **[E5-28]** scopes the claim to near-monopoly, which the row
  refutes. **The inverse metric [E4-37]**, *"a prayer session before you raise your prices a penny"*: three years of
  cuts and *"attractive financing options"* are the agony end of the scale.
- **The attacker's test [E2-45]:** with ample capital and skilled people, how would one compete with Tesla's car
  business? The filings say it is being done: *"Many major automobile manufacturers have electric vehicles
  available today in major markets including the U.S., China and Europe"*, and China revenue has been flat for
  three years ($21,745M, $20,944M, $20,962M FY2023-25) in the largest EV market.
- **Direction [E4-32] and units [E4-55]:** **narrowing.** Units fell two years running (1.81m, ~1.79m, ~1.64m)
  while revenue per car fell 22%; the H1 2026 unit recovery came with a lower margin, not a higher one.
- **[E4-04], and the [E5-23] test (does the spending defend the same advantage or buy its replacement?)**: the
  company is buying its replacement, in its own words. *"The next phase of production growth will be initiated
  by advances in autonomy and the introduction of new products, including those built on our next generation
  vehicle platform"* (FY2025 10-K MD&A); the Q2 2026 Update records the Model S and X lines decommissioned for
  Optimus, Cybercab in production, and capex 142% up on the year. The moat claim for the car rests on the next
  platform, which is [E4-04]'s *"industries prone to rapid and continuous change"* named by the company itself.
- **The four causes of extreme success [E4-36] and the surfing run [E3-51]:** FY2020-22 was **wave-riding**: first
  at scale into battery cars during a supply-tight market with a regulator paying for credits. When the wave
  flattened (rivals' EVs, capacity loose, credits withdrawn), the margin went with it. *"If he gets off the wave,
  he becomes mired in shallows."*
- **Key-person dependence, recorded here as a MOAT DEFECT [E4-23]:** the 10-K: *"we are highly dependent on the
  services of Elon Musk, Technoking of Tesla and our Chief Executive Officer. None of our key employees is bound
  by an employment agreement for any specific term"*; the 2025 proxy (DEF 14A `0001104659-25-090866`): the
  compensation proposals are an *"endorsement of his singular role in leading Tesla into the future"* and *"the
  Board believes that Mr. Musk's vision and leadership are critical to nailing that execution."* **The board and
  the company both say the plan requires this manager.** [E4-23]: *"if a business requires a superstar to produce
  great results, the business itself cannot be deemed great."* (Recorded at Q2, as the framework requires, not as a
  compliment at Q3.)
- **The energy segment, separately:** the best filed position in its row (FLNC run), and widening on its own
  margin; but the FLNC run also found price per kWh following cell cost down (*"a decrease in average selling price
  of Megapack"*), the low-cost Chinese integrators unpulled, and the US edge partly statutory. **At most a narrow,
  PROVISIONAL position in 22% of gross profit.** It cannot make the whole a franchise: the business is 78% the car
  segment, and the verdict is on the business.

### CLASS AND VERDICT
- **Class: [ ] WIDE [ ] NARROW [x] NONE for the business as constituted [ ] PROVISIONAL · Direction: narrowing**
  (car segment: none, narrowing; energy segment: a narrow position at most, provisional, 22% of gross profit).

**VERDICT: [ ] IN  [x] OUT**  [ ] UNRESEARCHED  [ ] UNKNOWABLE

**OUT on [E3-03] criterion (2), named precisely: the customer has close substitutes, which Tesla's own 10-K names
(*"extremely competitive markets"*, competitors with *"significantly more or better-established resources"*), and
the proof that the customer treats them as substitutes is in three consecutive 10-Ks explaining lower revenue per
car by *"price reductions"* and *"attractive financing options"*, made with a quarter to a third of installed capacity
idle [E2-58, E2-44].** Compounded by: the row-leading margin was a supply-tight-years lead that has gone (4.59% in
FY2025, below Toyota and Hyundai; 2.6% in H1 2026) [E3-46, E4-32]; 46% of FY2025 operating income came from
credits a regulator creates and is withdrawing [E2-59]; the company is buying its replacement advantage rather than
defending a standing one [E4-04, E5-23]; and the board says the plan requires one manager [E4-23]. *Evidence is in
and the business fails the test; this is a finding about the business as constituted, not about the price and not
about the AI businesses, which Q1 placed outside the circle and which therefore cannot be scored as a moat here.*
**Can I name a document that would reverse it? No filing now on file could**: a reversal would need a record not
yet made (Q6 states it in words).

*The file closes here. Q3, Q4, Q5 and Q6 below are RECORDED, NOT GOVERNING, as at SMCI, SNOW, TM and the other Q2
closes in wave 5.*

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT, on the business). This section is written because the
> brief asked for Q3 with the 8-K EX-99.1 releases and the proxy, and because what it finds belongs in the Q6
> reopening conditions. Nothing here can promote the name or repair Q2 **[E2-37, E2-38, E3-39]**.

### STEP 1 - THE WEIGHT CASE
- [x] **Daily execution** **[E3-38]**: a car maker is have-to-be-smart-every-day: prices, recalls, launches and
  plant changeovers are decided continuously (the Model Y changeover took every factory down at once in H1 2025,
  10-Q MD&A), and Q2 found no franchise to stand a mistake **[E3-43]**: *"a business, unlike a franchise, can be
  killed by poor management."*
- [ ] **Control** **[E1-16]**: a minority purchase of a listed share.
- [ ] **Leverage** **[E3-29]**: net cash of about $34bn at 2026-06-30.

**Case declared: a BINARY GATE**, on daily execution. No price compensates.

### THE BINARY - honesty **[E5-16]**, each matter dated to when it became PUBLIC
1. **2018-09-29 (settlement filed; judgment 2018-10-16): the SEC action over the CEO's going-private statement.**
   FY2021 10-K: *"in connection with the actions taken by the SEC relating to Mr. Musk's statement on August 7, 2018
   that he was considering taking Tesla private. Pursuant to the settlement, we, among other things, paid a civil
   penalty of $20 million, appointed an independent director as the chair of our board of directors, appointed two
   additional independent directors ... and made further enhancements to our disclosure controls."* The filing
   records a settlement, not an admission.
2. **2023-02-03: the civil jury on the same statement found for the defendants.** FY2023 10-K: *"on February 3,
   2023, a jury rendered a verdict in favor of the defendants on all counts"*; judgment entered 2023-07-11,
   plaintiffs appealed.
3. **2024-01-30 to 2025-12-19: the 2018 pay award.** The Court of Chancery found it *"should be rescinded"*; the
   Delaware Supreme Court *"reversed the Court of Chancery's rescission order, reinstating Mr. Musk's 2018
   compensation package, and awarded $ 1 in nominal damages"* (FY2025 10-K). No adjudicated finding survives.
4. **2023-07-14 to 2025-01-13: directors' pay.** A derivative suit over directors' own awards 2017-2020 settled
   *"which does not involve an admission of any wrongdoing"*, with *"Proceeds received from directors in
   shareholder settlement | 277"* on the FY2025 cash-flow face.
5. **Open, none adjudicated:** a securities class action (filed 2025-08-04) alleging *"material misrepresentations
   in public filings regarding the effectiveness of Autopilot, Full-Self Driving (Supervised), and Robotaxi"*; the
   FSD consumer class (certified in part 2025-08-18, on appeal); a new consumer class filed 2026-06-04 on driver-
   assistance statements; the Benavides Autopilot verdict ($129M compensatory at 33% fault, $200M punitive, on
   appeal); the CRD and EEOC discrimination suits (CRD trial set 2026-09-21); and regulators' requests *"including
   subpoenas"* from NHTSA, NTSB, the SEC and the DOJ, on which *"To our knowledge no government agency in any
   ongoing investigation has concluded that any wrongdoing occurred"* (Q2 2026 10-Q).
6. **Auditor and controls:** PwC since 2005, clean opinion and effective internal control at 2025-12-31; no
   restatement (Step 0).

**Read on the binary:** no adjudicated integrity finding against the company or the CEO is on file; the one
enforcement matter (2018) settled without admission, and the civil jury on the same facts found for the
defendants. **Whether a settled SEC action over a CEO's market statement meets [E5-16]'s zero-tolerance test is a
reading of the framework**, the same class of question the UMC run raised on a corporate plea; it is carried to the
operator, not settled here, and it does not govern (Q2 closed the file). *A Q3 pass is the absence of found
disqualifiers, not a finding that the managers are honest* **[E5-17]**.

### THE INCENTIVE READ **[E4-27]**
**What the CEO's pay vests on is written in the 10-Q.** The 2025 CEO Performance Award (423,743,904 restricted
shares, 10.7% of the cover count) is earned in twelve tranches, each requiring **a market capitalisation from $2.0
trillion to $8.5 trillion** (*"measured on a trailing average basis over both a six-month period and a 30-day
period"*) plus operational milestones of which five are deliveries, subscriptions, bots and Robotaxis and **seven
are Adjusted EBITDA thresholds from $50 billion to $400 billion**, with Adjusted EBITDA defined as net income
*"before interest expense, provision (benefit) for income taxes, depreciation, amortization and impairment,
stock-based compensation and digital assets gains and losses"* (10-Q Note 9). The 2018 award, now exercised, was
built the same way. **Two corpus flags fire from the pay document itself:**
- **[E3-50], stock-price targeting**, at full strength: the award is a schedule of share prices. The corpus's
  objection is to managers whose premise is *"that their job at all times is to encourage the highest stock price
  possible (a premise with which we adamantly disagree)"*; here the premise is the contract.
- **[E4-29], EBITDA**, at full strength: the yardstick for most of the operational milestones excludes the two
  costs this business is made of: depreciation (capex ran 2.5x depreciation over five years, Q4) and stock pay.
  *"Doing so implies that depreciation is not truly an expense ... That's nonsense."*

### STEP 2 - THE FLAGS. *Each is a prompt to READ, never a verdict.*
- [ ] **weak accounting** - SBC expensed; no restatement; the 2023 valuation-allowance release ($5.93bn, *"a
  one-time non-cash tax benefit"*) was called out in the MD&A. Not fired.
- [ ] **unintelligible footnotes** - the award and implementation-agreement notes are long but legible. Not fired.
- [x] **trumpeted projections / growth targets [E4-22]** - the quarterly Update's outlook is qualitative
  (*"Amazing Abundance"*; *"Scaling will be non-linear"*; *"We've never been more optimistic about the future"*, Q2
  2026 Update), and the pay plan sets targets of $400bn of Adjusted EBITDA against $15.3bn over the last four reported quarters (Q3 2025-Q2 2026 Updates: 4,227 + 4,154 + 3,668 + 3,273). **[E3-48]'s remedy,
  run on the filed outlooks:** the Q4 2023 Update (`0000950170-24-007073`) said volume growth *"may be notably lower
  than the growth rate achieved in 2023"*: outturn -1% (FY2024) and about -8% (FY2025), lower than guided in
  direction, not only in rate; it said energy growth *"should outpace the Automotive business"*: **held** (energy
  revenue +67% in FY2024). The sentence *"over time, we expect our hardware-related profits to be accompanied by an
  acceleration of AI, software and fleet-based profits"* appears unchanged in each Update read (Q4 2023, Q1 2024,
  Q2 2026), ten quarters apart, without a number to score it against.
- [x] **serial share issuance [E5-15]** - share count 3,100M (2021) to 3,949.5M (July 2026), +27%, of which about
  710M (23% of the 2021 base) went to one holder through the 2018 and 2025 awards; employee dilution alone is
  about 0.8% a year (basic weighted 3,174M FY2023 to 3,237M Q2 2026). No buyback has offset it.
- [x] **EBITDA promotion [E4-29]** - the Q2 2026 Update's Financial Summary carries *"Adjusted EBITDA 3,401 4,227
  4,154 3,668 3,273"* and *"Adjusted EBITDA margin 15.1% 15.0% 16.7% 16.4% 11.6%"* beside GAAP operating margin
  4.1% to 1.4%; the 10-K uses the term only in the pay-award note (all 11 occurrences), where it is the yardstick
  (above).
- [ ] **filed-figure tells [E4-30]** - reported growth is not smooth (operating income fell 68% FY2022-25), and cash
  taxes rose as a share of pretax income: $561M / $1,203M / $1,119M / $1,331M / $1,232M against pretax $6,343M /
  $13,719M / $9,973M / $8,990M / $5,278M = **8.8%, 8.8%, 11.2%, 14.8%, 23.3%**. Not fired; the direction is the
  reverse of the tell.
- **[E2-49] metric-switching:** the outlook's growth driver changed from *"the next-generation vehicle platform"*
  (Q4 2023 Update) to *"advances in autonomy and introduction of new products"* (Q1 2024 Update) the quarter after
  the volume guide softened. A change of plan announced with the reason is closer to the candor case; recorded, not
  fired.
- **Flags that converge [E4-52]:** pay set on share price and EBITDA, a quarterly narrative without numbers, and an
  award that transfers 10.7% of the company to one holder point the same way; read as one system, not a sum.

### STEP 3 - THE PRIMARY TEST **[E2-01]**, scoped by **[E2-43]**
Return on equity, net income attributable over average stockholders' equity: FY2022 **33.5%** ($12.56bn); FY2023
**27.9%** as reported, **16.9%** without the $5.93bn tax release; FY2024 **10.5%**; FY2025 **4.9%** ($3.79bn on
$77.5bn). Pre-tax return on capital employed net of cash (the unleveraged denominator [E2-43]; `roc_out.txt`):
57.5%, 26.7%, 16.6%, 9.4%, and 5.1% in FY2025 less regulatory credits. **The primary test is failing in its own
terms, on a falling five-year line** [E2-42].

### CANDOR - THE HALF-OWNER TEST **[E2-26]**
The 10-K and 10-Qs pass on the items tested: restructuring charges quantified (*"$583 million of employee
termination expenses"*, 2024; *"$390 million ... related to charges for supercomputer assets, contract terminations
and employee terminations"*, 2025), the tax release named, related-party revenue quantified ($430M from xAI in
FY2025; $405M from SpaceX in H1 2026). **The quarterly Update fails it in one respect**: its headline profit line
beside GAAP is Adjusted EBITDA, and its outlook carries no figure a holder could score.

### RATIONALITY IS CAPITAL ALLOCATION
- **Capital into the CEO's other company, against the shareholder count.** Shareholder Proposal 7 at the 2025
  meeting (*"Board authorization of an investment in x.AI Corp."*) drew 1,059.0M for, 916.3M against and 473.1M
  abstaining, and *"was not approved under the bylaw standard"* (8-K `0001104659-25-108507`). In January 2026 the
  company agreed *"to invest approximately $ 2 billion to acquire shares of Series E Preferred Stock of xAI"*
  (FY2025 10-K Note 15), which became *"$ 2.00 billion in SpaceX common stock ... representing an ownership interest
  of less than 1 %"* (Q2 2026 10-Q Note 13). The board may do so on an advisory vote; the [E3-40] prompt is that
  capital is moving toward the ventures the 10-K lists as competing for the CEO's time: *"he does not devote his full
  time and attention to Tesla. For example: Mr. Musk also currently holds management positions at Space Exploration
  Technologies Corp., X.AI Holdings Corp. ("xAI"), Neuralink Corp. and The Boring Company."*
- **The institutional imperative [E2-30]:** (1) resists change: not scored; (2) **projects soak up funds: fired as a
  prompt**: capex $8.3bn in H1 2026 (Q2 alone $5.8bn, *"142%"* up) for chip fabs, lithium refining, cathode,
  solar, AI compute, Optimus, Semi and Cybercab, while the core business earned 1.4% operating margin in the quarter;
  (3) staff studies for the leader's craving: not observable from filings; (4) imitation: not scored.
- **Buybacks [E5-08]:** none. The business pays no dividend and buys no stock; the discount condition is moot at a
  yield under 1% (Q5).
- **Stock deals in shares [E5-44]:** the 2025 award is paid in shares at a quote Q5 finds far above any owner-earnings
  value, so its cost to other holders is larger than the accounting charge, as [E3-70] says of options.

### THE GUARDRAIL
- [x] Nothing in this Q3 is used to promote the name. [x] "Requires a great manager" is recorded at Q2 as a moat
  defect **[E4-23]**. [x] The manager is the plan in the company's own proxy (*"his singular role in leading Tesla
  into the future"*), which is the **[E2-36]** corporate-Pygmalion case, not the excisable-cancer one.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary as the filings stand** (no adjudicated disqualifier;
  the 2018 SEC settlement carried to the operator as a reading question) [ ] OUT [ ] UNRESEARCHED [ ] UNKNOWABLE.
  **Four flags converge [E4-52]**: [E3-50] and [E4-29] written into the pay contract, [E5-15] issuance concentrated
  in one holder, [E4-22]'s projections flag with an outlook that cannot be scored; plus an [E3-40] capital-allocation
  prompt on the xAI/SpaceX investment. *IN = no disqualifier found, never a promotion.*

---
## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). Written for the reopening conditions at Q6 and because
> the owner-earnings number is what Q5 would need.

### Owner earnings — the one number **[E2-23]**
From the filed cash-flow faces (FY2023 and FY2025 10-Ks; Q2 2026 10-Q), `oe.py`, output `oe_out.txt`, $M. **SBC
made complete** by adding the capitalised part each 10-K states (*"stock-based compensation expense capitalized to
our consolidated balance sheets was $ 238 million"* FY2025; $198M, $199M, $245M, $182M before) **[E5-06]**.

| year | OCF | SBC complete | capex (face) | PP&E depreciation | **OE, capex end** | **OE, depreciation end** | capex / dep |
|---|---:|---:|---:|---:|---:|---:|---:|
| FY2021 | 11,497 | 2,303 | 6,514 | 1,910 | 2,680 | 7,284 | 3.41 |
| FY2022 | 14,724 | 1,805 | 7,163 | 2,420 | 5,756 | 10,499 | 2.96 |
| FY2023 | 13,256 | 2,011 | 8,899 | 3,330 | 2,346 | 7,915 | 2.67 |
| FY2024 | 14,923 | 2,197 | 11,342 | 4,120 | 1,384 | 8,606 | 2.75 |
| FY2025 | 14,747 | 3,063 | 8,527 | 5,030 | 3,157 | 6,654 | 1.70 |
| TTM Jun-26 | 18,685 | 3,798 (expensed only) | 12,923 | 5,440 | 1,964 | 9,447 | 2.38 |

- **Five-year default window FY2021-25 [E2-42]: capex end $3,065M; depreciation end $8,192M.** Three-year FY2023-25:
  $2,296M to $7,725M. **Combined range: about $1.4bn (FY2024 capex end) to $10.5bn (FY2022 depreciation end) by year;
  $2.3-8.2bn across the means.** The spread is wide, and it is a Q4 finding **[E4-25, E5-11]**: FY2022 is the
  supply-tight peak, and the capex band is itself $5.1bn a year wide.
- **Maintenance capex, a DISCLOSED JUDGMENT [E2-23].** Depreciation is the corpus default **[E3-44, E2-41]**, and
  capex has run 1.7-3.4x it. Most of the excess is growth by the company's own account (new plants, Cybercab, Semi,
  Optimus, AI compute, a chip fab). **But car making is in the [E5-20] exception class on this filer's own
  evidence**: each platform generation retools the lines (*"We have decommissioned the manufacturing lines for Models
  S & X at our Fremont Factory"*, Q2 2026 Update), AI compute was written off within two years (the FY2025 $390M
  *"charges for supercomputer assets"*), and the Q4 2023 Update tied the next growth wave to *"the next-generation
  vehicle platform"*. **(c) is judged above depreciation and below total capex; the run carries the band and does
  not pick a point.** Under [E3-44]'s exception wording the depreciation end is optimistic, not merely one end.
- **Working capital [E2-23]:** the face's operating asset and liability lines netted -$914M a year over FY2021-25
  (inventory and lease vehicles absorbing more than payables supplied), already inside OCF. `working_capital_flag`
  (FY2022 payables 41% of OCF) is real but offset in the same year by inventory (-$6,465M).
- **Stock compensation [E5-06, E3-70]:** subtracted in full at the charge. The [E3-70] market measure would be
  larger: the 2025 award's unrecognised expense is *"$ 105.82 billion to $ 120.37 billion"* for the milestones not
  yet probable, against $9.82bn recognised over 9.2 years for the one that is (10-Q Note 9). None of that is in the
  five-year mean.
- **Regulatory credits** ($1,957M a year, five-year mean) are inside OCF; less them, the depreciation end is
  **$6,235M** and the capex end **$1,108M** (display; the regime is being withdrawn, Q2).

### Great, good, or gruesome? **[E4-20, E4-43]**
- [ ] great [ ] good [x] **gruesome on the FY2022-25 record**: capital employed rose **$20.4bn** (from $26.8bn to
  $47.2bn) while operating income fell **$9.3bn** (from $13.66bn to $4.36bn) and revenue was flat from FY2023; the
  savings account paid 57% and now pays 9% pre-tax (5% without credits), and the company is adding money at a
  faster rate than ever (H1 2026 capex $8.3bn). FY2020-22 was great; the class moved.

### Staying power — score all three **[E5-11]**
- (1) Earnings: net income positive in every year read, FY2021-25; operating margin 1.4% in Q2 2026. Reliable in sign, not in
  size.
- (2) Liquid assets: **$43.5bn** of cash and short-term investments at 2026-06-30.
- (3) Near-term cash requirements: debt and finance leases $9.3bn ($1.4bn current); capex running at an annualised
  $16bn+ in H1 2026, which the company says it can slow (*"we may choose to correspondingly slow the pace of our
  capital expenditures"*, FY2025 10-K).
- Leverage **[E4-16, E2-54]**: interest expense $338M (FY2025) against OCF of $14.7bn net of all capex: covered
  many times. **Survival is not in doubt.**

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**
- **The mechanism: shape #11, the pass-through, with #14's feature (the patron)** (`Screens/SURVIVAL SHAPES -
  index.md`). The company lives; the owner's return is competed away: price cuts pass cost gains to buyers
  **[E3-62]**, the credits a regulator paid for are withdrawn, and the cash is re-spent on replacement platforms
  whose economics are not filed.
- **Quantified:** at FY2025's structure, removing the remaining credits ($1,993M) takes operating income to $2,362M
  (2.5% of revenue); H1 2026 was $813M less credits on $50.1bn of revenue (1.6%). A further 5% cut in revenue per car
  at FY2025 volume ($3.3bn) exceeds that. The exposure is filed: *"Increased competition could result in our lower
  vehicle unit sales, price reductions"*.
- **Likelihood: [x] a real possibility** that the car business earns about nothing for owners for years, as Ford and
  Honda automobile did in the row; **a low-level possibility** of anything worse, given $43.5bn of liquidity.
- **VERDICT (RECORDED, NOT GOVERNING): [ ] IN [x] OUT on [E4-20]'s gruesome leg for the FY2022-25 record; IN on
  survival** [ ] UNRESEARCHED [ ] UNKNOWABLE.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 is OUT. Nothing below is a clearance.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
`q5.py`, output `q5_out.txt`. Legal cap $1,438,702M; economic cap (unearned 2025-award shares excluded)
$1,284,344M; sovereign **5.34%** (US Treasury 30 Yr, 09/18/2026).

| owner earnings case | $M | yield, legal cap | yield, economic cap | vs 5.34% | perpetual growth needed for 10% |
|---|---:|---:|---:|---:|---:|
| 5y FY2021-25, capex end | 3,065 | 0.21% | 0.24% | -5.10 | 9.74% |
| 5y FY2021-25, depreciation end | 8,192 | 0.57% | 0.64% | -4.70 | 9.30% |
| 3y FY2023-25, capex end | 2,296 | 0.16% | 0.18% | -5.16 | 9.80% |
| TTM to 2026-06-30, depreciation end | 9,447 | 0.66% | 0.74% | -4.60 | 9.20% |

- **The floor first [E4-28]:** a 10% pre-tax expectancy at the economic cap needs **$128.4bn** of owner earnings a
  year, **15.7x** the most generous five-year figure; at 15% a year compounded the depreciation end reaches it in about
  20 years, at 20% in about 15. **[E4-35]**: *"fewer than 10 of the 200 most profitable companies"* sustain 15% for 20
  years, and this base is the depreciation end of a business whose operating income fell 68% in three years.
- **What the price already assumes:** perpetual growth of 9.2-9.8% a year from today's owner earnings, forever, to
  earn the floor; about 4.6-5.2 points **below** the bond at today's yield. **[E4-44]**: *"the value of an asset ...
  cannot over the long term grow faster than its earnings do."* The only filed document that states earnings of
  that order is the pay contract's $400bn Adjusted EBITDA milestones, which are targets, not a record.

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-01]**
At the floor, owner earnings capitalised with 0-7% perpetual growth: **roughly $10-30 a share on the capex end and
$25-75 on the depreciation end** (economic count), against **$364.27**. **Bar 2, the screamer test [E4-01]**: the
price is above the whole range; the answer would be *no*, not "no useful conclusion". **Windage count: one** (the
floor); no margin applied, because the price is above the range before any margin.

- **VERDICT: none. Q5 did not open (Q2 OUT).** Had every gate been IN, the computation shows a yield under 1%
  against a 5.34% bond and a 10% floor.

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

> **RECORDED, NOT GOVERNING.** Nothing is owned and nothing is armed (the QLYS ruling: a Q2 failure is a failure
> of the business, and a price alert on it would be a category error). These are the conditions on which the file
> would be reopened, written before any reopening **[E1-02]**.

**What would reopen Q2 (the governing gate):**
1. **A franchise shown in a supply-ample period:** Tesla's GAAP operating margin **less regulatory credits** above
   the volume makers' comparable figures (Toyota all-in, GM consolidated) for at least three consecutive years in
   which the industry's own filings still describe excess capacity, **with revenue per car delivered flat or rising
   and no filed "price reductions" or financing incentives cited as a cause** [E2-44, E4-37, E3-43].
2. **Return on capital recovering while capital grows:** pre-tax return on capital employed, less credits, back above
   20% for three years with capital employed higher than FY2025's $47.2bn [E3-46, E4-32].
3. **The AI businesses entering the circle:** Robotaxi, FSD or Optimus reported as a segment, with at least three
   years of filed revenue, cost and capital employed, so that Q1 can be asked of them at all [E3-31]; until then no
   price can be paid for them in this framework.
4. **Key-person dependence reduced in the filing itself** [E4-23]: a board and 10-K that no longer describe the plan
   as resting on one manager.

**And what would close it harder:** units down a third year; credits gone and the margin less credits at or under
zero; further capital to the CEO's other companies.

**The sell rule [E2-28]** does not apply (nothing held). **Position size:** none.
**VERDICT (RECORDED, NOT GOVERNING): not applicable; the file closed at Q2 and Q6 arms nothing.**

---
## SELF-AUDIT
- [x] Questions answered in order; the gate stopped at Q2 (OUT); Q3-Q6 recorded beneath explicit RECORDED, NOT
  GOVERNING banners, with Q5 headed COMPUTATION — NOT A CLEARANCE and carrying no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed statements
  and is scoped in writing to the business the filings show; the AI and robot businesses are recorded as outside
  the circle, not as a provisional IN. The energy segment's position is PROVISIONAL at Q2, and Q2 is OUT on the car
  business, which the provisional part cannot rescue.
- [x] No UNRESEARCHED or UNKNOWABLE verdict was returned. One document is named as a work order for any future
  upgrade only: BYD's 2025 annual report on HKEXnews (not re-attempted; the TM run recorded the obstacle).
- [x] Step 0: the filing was read with accession numbers; OCF, SBC and capex cross-checked to the FY2025 10-K face;
  the one tagged series that does not match the face (D&A) named and handled at Q4.
- [x] Owner earnings on the five-year default window and a three-year window, both (c) ends, TTM shown; SBC made
  complete with the capitalised part; working capital read from the face; (c) disclosed as a judgment inside the band.
- [x] Competitor row filled: nine peers named, five complete from SEC filings via the TM run's accessioned row with
  every Tesla figure recomputed here; gaps stated (BYD blocked; CATL, Sungrow, Wärtsilä unpulled for energy).
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated 09/18/2026, fetched uncached.
- [x] Value stated as a round-number range under a COMPUTATION — NOT A CLEARANCE heading.
- [x] One bar (the screamer test); windage count one.
- [x] Price dated as the 2026-09-18 close, aggregator flagged, corroborated by a Form 4.
- [x] Run committed after Step 0, Q1, Q2 and Q3-Q6, each with a pathspec.
- [x] Every ledger id cited was looked up in `principle_ledger.csv` (`led.py`) before it was written.
- [x] No em dashes in anything this session wrote (the template's own headings and the required
  `COMPUTATION — NOT A CLEARANCE` heading carry them).
- [x] Never presented as proven to beat the market; nothing here claims it.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **Q2, corrected before commit:** the first draft of the "Tesla less regulatory credits" row carried wrong margins
   (9.40 / 14.58 / 7.34 / 4.42 / 2.49, pooled 7.30); recomputed from the stated numerators and denominators they are
   9.66 / 14.91 / 7.48 / 4.54 / 2.54, pooled 7.40, and the text now uses those.
2. **Q2, corrected before commit:** a draft said Tesla less credits was below every volume maker in FY2025 except
   those in charge years; GM's GAAP 1.57% and VW's 1.8% are below its 2.54%, and the sentence now names who is above
   and who is below.
3. **Q2, corrected before commit:** a draft put idle capacity at "about 30%" from the Q2 2026 capacity table against
   FY2025 deliveries; the price cuts were made in FY2023-25, so the capacity figure now comes from the Q4 2023 Update
   (about 2.35 million) and the idle share is stated as a quarter to a third (76% and 70% utilisation).
4. **Q1, corrected before commit:** a draft said 97% or more of revenue came from the car and battery mechanism; the
   filed figure is 86.8% for automotive plus energy, with services and other (13.2%) sold to the same fleet.
5. **Q3, corrected before commit:** a draft set the pay plan's $400bn Adjusted EBITDA against "$16.3bn TTM"; the four
   latest quarters in the Update sum to $15.3bn. A draft said the 10-K does not use EBITDA; it uses it 11 times, all in
   the pay-award note. A draft put the CEO's share of issuance at 18% of the 2021 base; it is 23%.
6. **Committed 33 JPEG slide images** of the Q2 2026 Update (`8k/q2_2026_deck/*.jpg`, about 3.9 MB) in the Q2 commit
   `251f6f1`. The deck's text layer (`exhibit991.htm.txt`) was what the run used; the images are re-fetchable from
   EDGAR and should not have been committed. `.gitignore` covers `.htm`, `.html`, `.pdf` and `.xlsx` in research
   folders but not `.jpg`. **History is not rewritten**; a tooling note below.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **"Pull ... the proxy"**: there is no 2026 proxy statement. The FY2025 Part III was filed as a **10-K/A**
   (`0001104659-26-053166`, 2026-04-30), whose explanatory note says the original 10-K omitted Items 10-14; the latest
   DEF 14A is 2025-09-17 (`0001104659-25-090866`, for the 2025-11-06 meeting). Both were used.
2. **"Check any large `share_count_shift` against the split feed first"**: held and worth doing, but the answer at
   TSLA is that the shift (1.23x) was **not** a split (both splits sit before the older observation) and **not** the
   guard that fired; it is the CEO's awards, 10.7% of the cover count unearned.
3. **The SNOW register discrepancy (104 counted vs 103 stated)**: **not reproduced.** Counting line-start
   `- **TICKER (` entries from the heading line `## COMPLETED FROM THE QUEUE` to `## THE WRITE-EARLY PROTOCOL` gives
   **103, no duplicate ticker**, so SNOW's "103" was right and TSLA is **104**. Two looser counts give 105, not 104:
   slicing from the phrase's first occurrence (the trap the 2026-09-13 resume note records), and matching `- **X (`
   anywhere in a line, which picks up two unit series in prose (*"- **806 (2018)**"* and *"- **600 (2025)**"*). No
   count tried gives 104.
4. **"`restatement_shift` cannot have fired"** (from the SNOW note): held; the TSLA guard was `scale_shift`, as at
   SNOW, but for a different reason (a tag hole, not an organic step).

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`scale_shift` at `a8bc84f` compares non-consecutive years when the first element read has a hole.** Tesla's
  `RevenueFromContractWithCustomerExcludingAssessedTax` skips FY2019-20, so FY2018 sat beside FY2021 as a "one-year"
  step of 2.51x. The current screen reads the union of elements and returns 1.71x; any other name re-triaged from the
  old code could carry the same false step. A guard that also required the two period ends to be about a year apart
  would have refused the pair.
- **`share_count_shift` reads the legal cover count, which includes unearned restricted stock**: Tesla's cover
  carries 423.7M shares that basic EPS excludes. Any cap built on the dei element for a filer with issued-but-unearned
  performance shares is overstated by that block.
- **`tools/sources.sovereign()` served the cached 09/17 row at 18:41 EDT** while the Treasury had published 09/18
  (5.34%): the SNOW run's note, reproduced.
- **`.gitignore` does not cover `.jpg`** in research folders; image-only 8-K exhibits (Tesla's Updates) will slip
  through the same way.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**A five-year pooled margin can be two years of wave and three of sand.** Tesla's 9.54% leads the automaker row and
looks like a moat; year by year it is 16.8% in the supply-tight year and 4.6% three years later, below Toyota, with
46% of the last year's operating income paid by a regulator. Read the pool one year at a time, and take the credits
out, before a row-leading average is allowed to argue for a franchise.

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** TSLA FAILS AT Q2 (OUT, on [E3-03] criterion (2) not shown and contradicted in its own 10-Ks:
  *"extremely competitive markets"*, competitors with *"significantly more or better-established resources"*, and
  three years of lower revenue per car explained by *"price reductions"* and *"attractive financing options"* with a
  quarter to a third of installed capacity idle [E2-58, E2-44]; the row-leading five-year margin (9.54%) was a
  supply-tight lead, 16.8% in FY2022 to 4.6% in FY2025 and 2.6% in H1 2026, below Toyota and Hyundai [E3-46, E4-32];
  46% of FY2025 operating income from regulatory credits being withdrawn [E2-59]; buying its replacement platform
  [E4-04, E5-23]; the plan requires one manager per the board [E4-23]). Q1 IN on the business the filings show, the
  AI and robot businesses outside the circle; Q3 IN on the binary (recorded; gate case; [E3-50] and [E4-29] in the pay
  contract, [E5-15], [E4-22], an [E3-40] prompt on the xAI/SpaceX investment; the 2018 SEC settlement carried to the
  operator); Q4 IN on survival, gruesome on the FY2022-25 record, five-year owner earnings $3.1bn to $8.2bn (recorded;
  shape #11 with #14's feature); price $364.27 x 3,949,547,394 = $1.44tn legal, $1.28tn economic, headed COMPUTATION —
  NOT A CLEARANCE: yield 0.2-0.6% against 5.34%, $128bn of owner earnings needed for the floor; Q6 arms nothing.
- Work order: none for this verdict. UNKNOWABLE: none.

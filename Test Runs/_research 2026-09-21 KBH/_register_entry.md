- **KBH (KB Home), 2026-09-21 - FAIL at Q2 (OUT, ON THE BUSINESS).**
  Q1 IN. **WAVE 7, name 14. Register entry 146** (re-derived by the method the entry below
  describes: a line-start regex `^- \*\*` inside the slice from this file's
  `## COMPLETED FROM THE QUEUE` **heading line** to `## THE WRITE-EARLY PROTOCOL`, taken by
  index rather than by a last-occurrence search, because the heading string occurs **21 times**
  in this file and a bare search inserts outside the slice the count measures -- the USAR fold
  trap. **145 entries stood above this one, 145 distinct tickers, no duplicate**, which agrees
  with the APOG entry directly below claiming 145 for itself. After insertion: 146.)
  **Price US$47.12**, close of 2026-09-18, aggregator (Yahoo Finance chart endpoint), **flagged
  as an aggregator, live quote only**, raw response on disk at
  `Test Runs/_research 2026-09-21 KBH/price_KBH_yahoo_raw.json`. **Shares 61,309,728**, from the
  **cover of the 10-Q for the quarter ended 2026-05-31, accession `0000795266-26-000063`, filed
  2026-07-09** -- *"There were 61,309,728 shares of the registrant's common stock, par value
  $1.00 per share, outstanding on May 31, 2026."* One class of common only. **No splits after
  the measurement date.** **Cap re-struck by hand: US$2,888.9M** (61,309,728 x $47.12 =
  $2,889,914,383), against the screen row's **$3,217M**. **Sovereign 5.34%, 09/18/2026, US
  Treasury daily par yield curve, 30-year, from the issuing authority**, downloaded in this run
  and saved to the research folder; FRED was not used. Currency argued, not assumed: KB Home
  builds and sells in nine US states with no foreign operations -- USD is the earnings currency.
  **Newest annual is FY2025 (year ended 2025-11-30, accession `0000795266-26-000017`, filed
  2026-01-23); newest periodic is the 10-Q of 2026-07-09; the newest filing of any kind on
  2026-09-21 is a Form 4 of 2026-08-07, and NO Q3 filing (quarter ended 2026-08-31) exists yet
  -- EDGAR was checked rather than assumed.** The CSV's `newest_filing 2025-11-30` is a REPORT
  date, not a filing date: the APOG tooling defect, confirmed on a second name.

  **THE cap_flag FIRED FOR THE SIXTH CONSECUTIVE RUN AND WAS FALSE FOR THE SIXTH CONSECUTIVE
  TIME, and this run closed it with arithmetic rather than argument.** The flag said *"cap
  $3,217M against a filed float of $3,510M (1.09x) as of 2025-05-31. A cap cannot be smaller
  than a subset of itself. One of the two is wrong."* Neither is wrong. The filed float of
  **$3,510,028,491** is dated **2025-05-31**; shares outstanding on that date were
  **68,050,184** (cover of accession `0000795266-25-000081`); KBH's close on 2025-05-30, the
  last trading day before it, was **$51.58**; and **68,050,184 x $51.58 = $3,510,028,491, to
  the dollar.** The "float" KB Home files is therefore **every outstanding share at the May-2025
  close** -- the whole market capitalisation on a date fifteen months before the screen's cap,
  not a subset of any later one. What the flag actually detects is a **17.7% fall in market
  value**, 9.9 points of it price and the rest **6.74 million shares retired**. **Fix recorded:
  compare the filed float against a cap struck on the float's OWN as-of date; three of the four
  inputs are already on the cover page the tool parses.**

  **THE GATE THAT CLOSED THE FILE: Q2, on [E3-03] criterion 2, in the filer's own words.**
  FY2025 10-K, Item 1, Competition: *"We **also compete for homebuyers against housing
  alternatives to new homes, including resale homes, apartments, single-family rentals and
  other rental housing**."* Four substitute categories, named by the company. And the pricing
  strategy is built on one of them: *"a simplified sales strategy focused on providing a
  straightforward, transparent base price, with limited, if any, concessions or incentives,
  that is intended to offer to our customers **a compelling value competitive with area resale
  home prices**."* The same paragraph puts **selling price first** among the factors that
  decide a sale: *"we **primarily compete with other homebuilders on the basis of selling
  price**, community location and amenities ..."*

  **THE COMPETITOR ROW DECIDED IT -- eight peers, ten fiscal years, calendars aligned, every
  figure filing-sourced.** D.R. Horton, Lennar, PulteGroup, NVR, Toll Brothers, Meritage,
  M/I Homes, Century Communities. **Ten-year mean return on equity: KBH 13.6%, LAST of nine**
  (NVR 39.9, PHM 22.1, DHI 20.7, MHO 17.6, MTH 16.5, TOL 15.8, CCS 15.1, LEN 14.9). **The
  leverage defence was run BEFORE the verdict was written [E4-26] and it fails twice.** On the
  leverage-neutral measure, ten-year mean return on **assets**: **KBH 6.8%, LAST of nine, and
  last or joint-last in EVERY ONE of the ten individual years** (NVR 23.1, DHI 13.2, PHM 12.5,
  MTH 10.2, MHO 9.1, LEN 8.5, TOL 7.8, CCS 7.4). And the direction of the objection is
  backwards: KB Home's *"ratio of debt to capital, was **30.3%** at November 30, 2025"* (rising
  to 34.1% at 2026-05-31), **more** than DHI 19.8%, LEN 21.1% or TOL 17.4%. **It earns the
  lowest return in the group on one of the more leveraged balance sheets in it.**

  **[E2-58]'s one exception -- *"a cost advantage that is both wide and sustainable"* -- was
  looked for and found in a COMPETITOR, not in the subject.** NVR's 10-K (FY2025, accession
  `0000906163-26-000018`): *"We expect, however, to continue to acquire **substantially all of
  our finished lot inventory using LPAs with forfeitable deposits**."* NVR turns its
  homebuilding inventory roughly **6.0x** (components added by hand from the filing:
  $1,422.2M sold + $253.5M unsold + $39.3M land under development against $10,324M of revenue);
  **KB Home turns it 1.11x**, holds **59,106 lots, about 62% of them owned**, and put
  **$2.61 billion** into land and land development in FY2025 against $6.21bn of revenue.
  **Units, price and margin are all falling together [E4-55]:** deliveries 14,169 (FY2024) ->
  12,902 (FY2025) -> **10,500-11,000 guided** (FY2026); ASP $486,900 -> $481,400 -> $457,000
  actual for the six months to 2026-05-31; housing gross margin 21.0% -> 18.6% -> **16.1-16.5%
  guided**. **[E4-37]**'s inverse metric reads at the far end: KB Home did not agonise over a
  price increase, it *"**reduced selling prices** relative to applicable market conditions"* as
  stated strategy. **Class NONE, direction NARROWING.** The **[E4-04]** perimeter close was
  available and deliberately **NOT** taken: under the ruling of 2026-09-20 it is reserved for
  names that PASS [E3-03], and this one does not, so the verdict is OUT on the business.

  **THE v3.0 PRIOR'S QUOTE SURVIVED.** `Test Runs/2026-07-16 Run - Homebuilders 6-pack (KBH MHO
  TMHC MTH DFH CCS).md` rendered KBH's filing as *"compete... against numerous homebuilders...
  some of which are larger and have greater financial resources than us."* Opened against the
  FY2025 10-K: *"We compete for homebuyers, construction resources and desirable land against
  numerous homebuilders, ranging from regional and national firms, some of which are larger and
  have greater financial resources than us, to small local enterprises."* **Every quoted word is
  present, in order, and the two ellipses cover exactly what they should** -- an accurate prior,
  recorded as plainly as an error would be. **Its METHOD is not inherited**: its stated v3.0
  rule, *"generic competition text eliminates"*, is a verdict on prose and is nowhere in v4 or
  the corpus. Same answer, far stronger evidence. *(That file also carries two things v4 later
  banned: a Gate 3 *"PASS (provisional)"* on *"general knowledge, unverified"*, and DFH's owner
  earnings computed as *"OE = NI"*, the net-income proxy operator rule 5 forbids.)*

  **THREE READING ASSIGNMENTS, ANSWERED IN A `COMPUTATION - NOT A CLEARANCE` BLOCK** (operator
  rule 3; nothing in it can promote the name and Q5 never opened).
  **(i) The eighteen-year rebuild [E4-25].** Operating cash flow was **NEGATIVE in five of the
  eighteen filed years** (2010, 2011, 2013, 2014, 2021). Owner earnings, OCF less SBC less the
  (c) guess: **three-year $518.3M; five-year $309.1M; EIGHTEEN-YEAR $120.7M; the decade
  2011-2020 $6.9M.** The screen's band is now **reproducible to the dollar** -- `oe_top_m 518`
  is the 3-year OCF mean less SBC less D&A, `oe_bottom_m 309` is the 5-year OCF mean less SBC
  less TOTAL capex -- and it sits **4.3x above the eighteen-year figure**. The `spread_caveat`
  was right that the band cannot see past five years; this run measures how much that costs.
  **(ii) The `wc_note` is wrong in both of its claims.** *"ONE LINE MADE THE CASH"* -- FY2021
  operating activities **CONSUMED $37.3M**; there was no cash to make, and the 487% is
  |+181.6| / |-37.3|, a ratio to a near-zero **negative** denominator. And it names the wrong
  line: the **inventories** line moved **-$897.8M** in that same year, **4.9x** the
  accounts-payable move, and over all eighteen years OCF correlates **-0.58** with it. For a
  builder, land and homes under construction **are** the working capital of **[E2-23]**'s
  parenthetical, so operating cash goes negative when it buys land (FY2014: inventory +$919.8M,
  OCF -$630.7M) and positive when it liquidates (FY2023: inventory **-$409.5M**, OCF
  **+$1,082.7M** -- the largest operating-cash year in the filed record is the year it shrank
  its land position). **Is the mean measuring the cycle or the business? Both, and the window
  decides**: a 3- or 5-year mean anchored on FY2023 measures the liquidation phase; only the
  eighteen-year window contains both ends of **[E2-58]**'s *"ratio of supply-tight to
  supply-ample years."* And the increment is not buying unit volume: inventory +2.6% over two
  years while deliveries fall ~24% to the FY2026 guidance midpoint.
  **(iii) The `da_note`'s 10.7x step is ASC 606, and the brief's ASC 842 candidate is REFUTED
  from the filing.** FY2019 10-K Note 1: *"**We will adopt** ASU 2016-02 and its related
  amendments (collectively, "ASC 842") **beginning December 1, 2019**"* -- the year AFTER the
  step -- at *"approximately **$31.0 million**"* of right-of-use assets, with *"**no material
  impact** on our consolidated statements of operations or cash flows."* Note 10 gives the real
  cause: *"a change in the classification of certain community sales office and other
  marketing- and model home-related costs ... **from inventories to property and equipment,
  net** due to **our adoption of ASC 606** effective December 1, 2018"* -- the "Model
  furnishings and sales office improvements" line going from **$0** to **$82,117 thousand** in
  one year, with depreciation *"$27.2 million in 2019, $2.5 million in 2018."* **Consequence
  that outlives this name: the pre-2019 and post-2019 operating-cash-flow series of ANY
  homebuilder that adopted ASC 606 this way are not like-for-like**, because ~$30-45M a year of
  model-home spend moved out of OCF and into investing.

  **NO PRICE ALERT AND NO PORTFOLIO ROW** -- the QLYS ruling, 2026-09-07: a name that failed on
  the BUSINESS gets a reversal condition in words, not a band. **Reversal condition:** KB Home
  would have to move to a **land-light structure** of the kind its competitor NVR discloses --
  owned lots falling materially below the current ~62% of 59,106, inventory turns rising toward
  the peer top quartile -- **and** the return-on-assets ranking changing for reasons other than
  the cycle. **[E4-17]**: *"those beliefs change quite gradually."*

  **Acceptance test: PASS** before the commit -- 0 phantom citations across 1,099 run files and
  25,081 id citations, 0 unlabelled numbers in all five governed documents, 310 of 311 ledger
  rows verbatim against their cited sources (E5-07 is the declared negative finding).
  **Ledger-count finding, recorded for the operator and NOT acted on:** the file and
  `tools/check_framework.py` both report **311 rows, 311 unique ids**; `CLAUDE.md`'s KEY FILES
  pointer says **267**. That pointer was itself corrected from 117 on 2026-09-19. This run did
  not edit `CLAUDE.md`. *"Count the file, never the pointer"* is that file's own instruction.
  Run file: `Test Runs/2026-09-21 Run - KBH KB Home.md`.

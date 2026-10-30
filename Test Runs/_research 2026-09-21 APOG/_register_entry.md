- **APOG (Apogee Enterprises, Inc.), 2026-09-21 - FAIL at Q2 (OUT, ON THE BUSINESS).**
  Q1 IN. **WAVE 7, name 13. Register entry 145** (re-derived by counting the register itself with
  a line-start regex `^- \*\*` inside the slice from this file's `## COMPLETED FROM THE QUEUE`
  **heading line** (line 502, not its earlier textual occurrences) to `## THE WRITE-EARLY
  PROTOCOL` (line 11270): **144 entries stood above this one, 144 distinct tickers, no
  duplicate**, which agrees with the FC entry directly below claiming 144 for itself).
  **Price US$36.80**, close of 2026-09-18, aggregator (Yahoo Finance chart endpoint), flagged,
  raw responses on disk at `_research 2026-09-21 APOG/yahoo_APOG_chart.json` and
  `yahoo_APOG_6mo.json`. **Shares 20,868,294**, from the **cover of the 10-Q for the quarter
  ended 2026-05-30 (Q1 FY2027), accession `0000006845-26-000063`, filed 2026-06-30**, as of
  2026-06-25 -- *"As of June 25, 2026, 20,868,294 shares of the registrant's common stock, par
  value $0.33 1/3 per share, were outstanding"* (the `dei:EntityCommonStockSharesOutstanding`
  fact on that accession carries the same number). One class of common only; the Junior Preferred
  plan has *"zero shares issued and outstanding as of May 30, 2026."* **No splits anywhere in
  the available history. Cap re-struck by hand: US$768.0M** (20,868,294 x $36.80 = $767,952,219),
  against the screen row's **$787M** -- **the screen is 2.4% high and it is NOT a share-count
  error**, see flag (i-a) below. **Sovereign 5.34%, 09/18/2026, US Treasury daily par yield
  curve, 30-year, from the issuing authority**, struck fresh in this run. Currency argued, not
  assumed: *"We primarily supply architectural glass products and aluminum framing systems ... to
  customers in North America"* and the filing's own market-risk item quantifies **aluminum and
  lumber**, not FX -- USD is the earnings currency. **Newest annual FY2026 (year ended
  2026-02-28, accession `0000006845-26-000023`, filed 2026-04-24); EDGAR was checked rather than
  trusting the CSV's `newest_filing 2026-02-28`, which is a REPORT date, not a filing date --
  the newest actual filing on 2026-09-21 is 2026-09-15.**

  **THE DEAL NOTE GOVERNED THE ARITHMETIC AND IT WAS STALE AND ONE DEAL SHORT. APOGEE IS THE
  ACQUIRER, TWICE.** The screen's `deal_note` pointed at EX-2.1 to the 8-K of 2026-05-28
  (`0000006845-26-000044`) and asked which side Apogee was on. Item 1.01, verbatim: *"On May 27,
  2026, Apogee Enterprises, Inc. ... entered into a Merger Agreement ... with Keller Companies,
  Inc. ("KCI") and KCI's shareholders ... the Company has agreed to acquire all of the
  outstanding equity interests of KCI"* -- **$105 million cash plus up to $10 million of
  earn-out**, financed *"with cash on hand and funds available under its existing credit
  facility."* **So the quote is a price for a business, not a spread** -- the OTHER branch of the
  ACVA note of 2026-09-13. **Two later events the screen could not see, found by checking EDGAR:**
  (1) **the deal CLOSED** -- 8-K of 2026-07-01, accession `0000006845-26-000068`, **Item 2.01**:
  *"On July 1, 2026, Apogee Enterprises, Inc. ... completed the transaction contemplated by the
  Merger Agreement"*; (2) **a SECOND, larger deal was signed and is still pending** -- 8-K of
  2026-09-03, accession `0000006845-26-000087`, Item 1.01, its own EX-2.1: *"On September 2,
  2026, Apogee Enterprises, Inc. ... entered into a Share Purchase Agreement ... to acquire 100%
  of the issued and outstanding equity interests of SIA "Alzette" ... Alzette owns 100% of the
  equity interests of SIA "GroGlass""*, at *"approximately EUR 62.5 million on a cash-free,
  debt-free basis"* (~$72.5M), expected to close in fiscal 2027 Q3. **What it does to the
  arithmetic: $177.5M of purchase price spent or committed in four months, 23% of the hand-struck
  cap, and none of it is in the FY2026 balance sheet the owner-earnings series is built on; the
  cap does not shrink when the cash leaves, the debt behind it grows; and the FY2022-FY2026
  numerator contains no day of either business while already containing the $232.2M UW Solutions
  acquisition of FY2025.** Counting all three, **$409.7M -- 53% of the cap -- in deals inside or
  immediately after the five-year window**, and **$626.9M across the seventeen filed years**
  (FY2011 $20.6M, FY2014 $53.3M, FY2017 $137.9M, FY2018 $182.8M, FY2025 $232.2M). **The screen's
  own `acq_note` is RIGHT and understates itself.** [E4-38]'s publish-every-window remedy is
  therefore mandatory on this name, not optional.

  **NINE FLAGS AND SUB-FLAGS RESOLVED BY HAND BEFORE Q1 OPENED. SCORE: three right and useful,
  two right, two wrong on semantics, one stale, one prior refuted.**
  (i) `cap_flag` *"cap $787M against a filed float of $915M (1.16x) as of 2025-08-29 ... **One of
  the two is wrong**"*: **WRONG ABOUT "ONE OF THE TWO IS WRONG". This is the CALM / EMBC / BRBR /
  FC branch -- the two dates differ, and it is now FIVE consecutive runs.** The FY2026 10-K cover
  reads *"As of August 29, 2025 ... the approximate aggregate market value of voting and
  non-voting common equity held by non-affiliates ... was $ 915,200,000 (based on the closing
  price of $43.98 per share)"*; $915.2M / $43.98 = **20,809,459 implied non-affiliate shares**
  against **21,220,737** outstanding on the same cover as of 2026-04-17, so **affiliates hold on
  the order of 2% and essentially the whole company is float**. The entire 1.16x is twelve and a
  half months of price and buyback: **$43.98 -> $36.80 is -16.3%**, plus a count that fell
  21,220,737 -> 20,868,294 on **269,500 shares repurchased for $9.7 million in one quarter**.
  **I second FC and MGPI: the diagnostic should say "or the two dates differ."**
  **(i-a) A PRIOR IS REFUTED: FC's stale-annual-cover defect does NOT reproduce on this row.**
  FC found the screen pricing off the annual cover when a newer 10-Q cover existed, overstating
  its cap by 18%, and warned it would recur on every buyback filer. Tested here: $787M implies
  **$37.71** on the 10-Q count and **$37.09** on the annual count; the closes on the screen's own
  dates were **$37.59 (2026-09-01)** and **$38.06 (2026-09-02)**, which bracket $37.71 and not
  $37.09. **The screen used the newer 10-Q count**, the whole 2.4% gap is nineteen days of price,
  and it points the safe way -- the screen made the name look DEARER. **The FC defect is real but
  per-row, not universal.**
  **(ii) NEW TOOLING DEFECT: `best_year_dep` (0.079, *"no single-year dependence (9-yr OCF
  series)"*) CONTRADICTS `best_year_dep_oe` (0.121) BY 53%, AND `flags_disagree` IS EMPTY.**
  Rebuilt by hand, dropping FY2024 moves the FY2018-FY2026 owner-earnings mean from **$69.5M to
  $59.1M (-15.0%)** and the FY2022-FY2026 mean from **$76.6M to $57.5M (-24.9%)**. A quarter of
  the five-year owner-earnings mean is one year, and the screen's verdict string says there is no
  single-year dependence. **OCF is the wrong series to measure single-year dependence on:
  subtracting capex and SBC AMPLIFIES the outlier rather than damping it**, so the OCF-based flag
  will systematically under-report it on every low-capex filer. `flags_disagree` should have
  fired and did not.
  (iii) `window_disagree` *"9yr and the full 17yr series give different KINDS of answer; the 9yr
  base may already contain the wave [E4-41]"*: **RIGHT, AND THE SHARPEST THING THE SCREEN SAYS
  ABOUT THIS NAME** -- and Q2 found the wave in the competitor row independently.
  (iv) `spread_caveat` *"4-construction width only ... rebuild it [E4-25]"*: **RIGHT, AND
  REBUILT OVER SEVENTEEN FISCAL YEARS (FY2010-FY2026)** from the filed consolidated statements of
  cash flows, eight windows instead of four constructions. **What the 5-year width cannot see:
  owner earnings were NEGATIVE in FY2011 (-$41.4M to -$22.3M) and near zero in FY2012 and FY2013.**
  (v) `level_shift` 1.34 *"no step"* vs `level_shift_oe` 1.69 *"STEP UP - normalize down
  [E4-41]"*: **BOTH RIGHT; the OE one is the one that matters**, and the step has a name --
  FY2024, OCF $204.2M against a seventeen-year mean of $97.7M.
  (vi) `years_filed 17`: **RIGHT**, FY2010 through FY2026, all traced to 10-K cash-flow
  statements. (vii) `name_change_note`, `wc_note`, `da_note`, `level_shift_full`: correctly
  empty.

  **Q1 IN.** Four segments, one sentence each, commodity inputs, bid pricing, a construction
  cycle -- inside the circle and not close. Segment weights from Item 1, verbatim: Architectural
  Metals *"approximately 36% of our net sales"*, Architectural Services *"approximately 31%"*,
  Architectural Glass *"approximately 19%"*, Performance Surfaces *"approximately 14%"*.
  **Eighty-six per cent of this company is bid-priced non-residential construction.** The scarce
  input in the architectural half is close to nothing the filing will claim: *"Most of our raw
  materials are readily available from a variety of domestic and international sources"* and *"we
  do not regard our business as being materially dependent on any single item or category of
  intellectual property."*

  **Q2 OUT, ON THE BUSINESS -- [E3-03] criterion 2 fails on the filer's own sentences, and the
  price/volume decomposition proves it segment by segment inside one fiscal year.** The FY2026
  10-K, Item 1: *"The North American non-residential construction market is **highly
  fragmented**. Competitive factors include **price**, product quality, product attributes and
  performance, reliable service, on-time delivery, lead-time, warranties ..."* -- **price first,
  as it was for FC** -- and, on substitutes, *"we compete with regional glass fabricators and
  international competitors **who can provide certain products with attributes similar to
  ours**."* Then the MD&A, all four segments, FY2026: **Architectural Glass (19%)** *"lower
  volume **and price** due to lower end-market demand"*, adjusted EBITDA margin 22.2% -> 16.1%;
  **Architectural Services (31%)** *"increased volume, partially offset by unfavorable project
  mix **and lower pricing**"*, 8.0% -> 7.0%; **Architectural Metals (36%)** *"lower volume,
  partially offset by **favorable price**"* -- price held **and it did not matter**, 13.5% ->
  10.7%, on the filer's own reason, *"inflation, including higher aluminum costs"*; **Performance
  Surfaces (14%)** price and volume both up and margin down anyway, 25.3% -> 21.0%, on *"the
  dilutive effect of lower adjusted EBITDA margin from the UW Solutions acquisition."*
  Consolidated adjusted EBITDA margin 12.6% -> 14.2% -> **11.9%**. **In one year, two segments
  carrying half of net sales conceded price outright, one raised price and still lost 2.8 points,
  and the fourth grew price and volume and still lost 4.3 points because the business it bought
  earns less than the business it had.** The risk factors carry [E4-37]'s agony in the filer's
  voice: *"We may be unable to pass through additional tariff costs to our customers through
  price increases"*, and recovery *"may lag the cost increases."*

  **THE COMPETITOR ROW -- SEVEN LISTED PEERS, TEN CALENDAR YEARS, EBIT / CAPITAL EMPLOYED, EACH
  FROM ITS OWN 10-K FACTS, WITH THE FISCAL CALENDAR ALIGNED AND THE ALIGNMENT STATED** (Apogee's
  fiscal year Y ends in late February and runs Mar(Y-1)-Feb(Y), so it maps to calendar Y-1):
  **APOG 12.2% mean / 6.7% mean operating margin**, minimum 3.2%; **TGLS (Tecnoglass, CIK
  0001534675 -- the closest listed rival, the same product in the same market) 22.8% / 20.6%,
  whose WORST year (9.9%) beats Apogee's mean**; AWI (Armstrong World) 19.5% / 25.8%, never below
  12.8% in the decade; BLDR 19.7% / 8.1%; ROCK (Gibraltar) 11.5% / 9.8% -- the one peer Apogee
  genuinely matches; GFF (Griffon) 7.1% / 5.9%; JELD (JELD-WEN) 2.6% / 1.9% and negative in each
  of the last two years; NX (Quanex) carried with only two years resolving undimensioned, stated
  rather than dropped. **Seven, not eight, and the filing says why: *"most of our direct
  competitors in our various business units are either privately owned or are divisions of
  larger, publicly owned companies."*** Two natural peers deregistered inside the window and that
  was checked on EDGAR rather than asserted: **PGT Innovations (CIK 0001354327) filed Form 15-12G
  on 2024-04-08** and **Masonite International (CIK 0000893691) filed Form 15-12G on 2024-05-28**.

  **THE WAVE, AND THE DISCONFIRMING CASE ANSWERED [E4-26, E4-51].** The four honest arguments FOR
  a franchise are in the run file with their answers. The strongest is that **APOG earned 18.7%
  and 20.9% on capital employed in calendar 2022-2023** -- and the row shows **TGLS printed 43.2%
  and 35.7% and BLDR 43.1% and 25.2% in exactly those years**. The whole industry printed its
  best numbers at once, which is **[E3-51]'s surfing run, not a moat**, and [E4-36] names it as
  the wave-riding cause of extreme success. **Calendar 2025 is the answer: APOG back to 9.9%,
  BLDR to 8.1%, JELD to -27.3%, while TGLS is still at 25.4% and AWI at 26.0%.** The tide went
  out and two names were still dressed; Apogee was not one of them. The second-strongest
  argument, Performance Surfaces at a 21.0% adjusted EBITDA margin on proprietary brands, is
  answered three ways: it is 14% of sales and $41.6M of $172.3M of segment EBITDA; its margin is
  **falling** (27.5% -> 25.3% -> 21.0%); and **on the capital actually employed it is the WORST
  of the four segments** -- FY2026 segment EBIT $26.5M against identifiable assets of $337.1M =
  **7.9%**, against Glass 16.0%, Services 15.2% and Metals 12.1%. **The segment that looks like a
  franchise on margin is the one whose returns were bought rather than earned** [E2-43]. The
  third, *"one of only a few architectural glass installation service companies in the U.S. to
  have a national presence"*, is real **and earns the lowest margin of the four segments** --
  [E2-53] running backwards.

  **[E4-55], WHERE UNITS EXIST, MONITOR UNITS -- and here the concealment is by acquisition
  rather than by pricing.** Consolidated net sales **FY2019 $1,402.6M -> FY2026 $1,404.7M**, and
  in between **$232.2M of cash was paid for UW Solutions**, which the 10-K says *"delivered upon
  the first-year financial targets of **$100 million in revenue**"*. **Seven fiscal years, a
  quarter of a billion dollars spent, and the top line is $2.1M higher -- so the pre-existing
  business is about 7% SMALLER in nominal dollars, and much smaller in units, through a period of
  heavy construction-cost inflation.** The three architectural segments: **$1,317.6M (FY2024) ->
  $1,238.9M (FY2025) -> $1,206.8M (FY2026), -8.4% in two years.** Backlog $720.3M -> $693.8M.
  **Class NONE. Direction NARROWING.** [E4-32]'s *"primary criterion of a great business"* is a
  moat that widens every year; this one narrowed in each of the last two.

  **AND AS WITH MGPI AND FC, THE PRICE WAS NEVER THE PROBLEM -- headed COMPUTATION, NOT A
  CLEARANCE, carrying no entry language, because Q5 was never opened (operator rule 3).** Owner
  earnings rebuilt by hand over seventeen fiscal years, OCF less SBC less (c), with (c) at both
  the [E3-44] D&A default and the total-capex end, against the hand-struck $768.0M cap:
  **FY2022-FY2026 (the [E2-42] default window) $76.6M-$87.7M = a 9.97%-11.42% yield**;
  FY2018-FY2026 $69.5M-$76.9M = 9.05%-10.02%; **FY2010-FY2026 (everything filed) $51.9M-$55.4M =
  6.76%-7.21%**. **The five-year window clears the [E4-28] ~10% floor and the seventeen-year
  window is nowhere near it**, which is the `window_disagree` flag being right in dollars. **THIS
  IS THE THIRD CONSECUTIVE WAVE-7 NAME WHOSE PRICE WAS NOT THE PROBLEM** (MGPI, FC, APOG), and
  the gate order is why none of it counts.

  **NO BANDS, NO PORTFOLIO ROW -- the QLYS ruling.** A name that failed on the BUSINESS gets a
  reversal condition in words, not a price alert. **THE REVERSAL CONDITION FOR APOG:** *reopen
  this file only if the Performance Surfaces Segment -- post-Kalwall and post-GroGlass -- reaches
  a majority of consolidated net sales AND holds an adjusted-EBITDA margin above 20% for three
  consecutive fiscal years while the architectural segments shrink, i.e. only if Apogee stops
  being a bid-priced construction business and becomes a branded-coatings business. The two 2026
  acquisitions are management moving in exactly that direction; $177.5M buys roughly $130M of
  revenue against $1.2bn of architectural sales, so on the filed arithmetic that reversal is
  three or four more deals away and no price move triggers it.*

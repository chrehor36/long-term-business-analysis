- **MNRO (Monro, Inc.), 2026-09-21 - FAIL at Q2 (OUT, ON THE BUSINESS).**
  Q1 IN. **WAVE 7, name 15. Register entry 147** (re-derived, not inherited: a line-start
  regex `^- \*\*` inside the slice taken **by index** from this file's
  `## COMPLETED FROM THE QUEUE` **heading line** (502) to `## THE WRITE-EARLY PROTOCOL`
  (11606). The bare phrase "COMPLETED FROM THE QUEUE" occurs **22 times** in this file and
  only **one** line is the exact heading, which is the USAR fold trap and the reason the
  slice is taken by index. **146 entries stood above this one**, agreeing with the KBH entry
  directly below claiming 146 for itself. After insertion: 147.)
  **Price US$12.10**, close of 2026-09-18, aggregator (Yahoo Finance chart endpoint via
  `tools/sources.py`), **flagged as an aggregator, live quote only**. **Shares 31,264,060**,
  from the **cover of the 10-Q for the quarter ended 2026-06-27, accession
  `0000876427-26-000010`, filed 2026-07-29** - *"As of July 18, 2026, 31,264,060 shares of the
  registrant's common stock, $0.01 par value per share, were outstanding."* One class of
  common outstanding; the Class C Convertible Preferred **converted on 2026-06-18** into
  1,204,908 common shares and no longer exists. **No splits after the measurement date.**
  **Cap re-struck by hand: US$378.3M** (31,264,060 x $12.10 = $378,295,126), against the
  screen row's **$397M**. **Sovereign 5.34%, 09/18/2026, US Treasury daily par yield curve,
  30-year, from the issuing authority**, downloaded in this run and saved to the research
  folder; FRED was not used. The screen row's `vs_sovereign 0.04` is stale by 134bp and was
  used nowhere. Currency argued, not assumed: 1,115 stores in 32 US states, one operating
  segment, no foreign operations - USD is the earnings currency.
  **THE `cap_flag` IS REFUTED BY EXACT ARITHMETIC, AND THE DEFECT IS A DATE MISMATCH, NOT
  ARITHMETIC.** The flag said *"A cap cannot be smaller than a subset of itself. One of the
  two is wrong."* **Neither is wrong.** The float of **$541.4M is dated 2025-09-27** (FY2026
  10-K cover, accession `0000876427-26-000007`), when MNRO last closed at **$18.68** (Friday
  2025-09-26). Implied non-affiliate count $541,400,000 / $18.68 = **28,983,940**, against
  **30,019,660** outstanding at that date (10-Q cover, accession `0000876427-25-000005`) =
  **96.55%** - a proper subset. Implied cap on the float date: 30,019,660 x $18.68 =
  **$560.8M, LARGER than the float.** The stock then fell **35.2%**. **Fix owed to the
  tooling: compare the filed float against a cap struck AT THE FLOAT DATE, never against the
  live cap** - the present test is a price-decline detector wearing a sanity check's label,
  and will false-positive on any name down more than `1 - float/shares` since its float date.
  **A second cap defect the flag did not catch:** the screen used a pre-conversion share
  count, understating shares by **4.0%**.
  **MNRO IS A FISCAL-MARCH FILER** (dei `fiscalYearEnd` 0327; FY2026 ended Saturday
  2026-03-28). **`newest_filing` and `newest_periodic` are BOTH artifacts**: 2026-03-28 is a
  **period-end date, not a filing date** (the 10-K was filed 2026-05-27), and both fields are
  **a quarter stale** against the CSV's own date of 2026-09-02, missing the 10-Q of 2026-07-29
  - which is the filing that carried the share count the cap needed. Seventh confirmation of
  the APOG report-date defect.
  **Filing read: Form 10-K for the fiscal year ended March 28, 2026, filed 2026-05-27,
  accession `0000876427-26-000007`** (MD&A, Consolidated Statements of Cash Flows including
  detail lines, and footnotes), plus the 10-Q of 2026-07-29 and both furnished 8-K EX-99.1
  earnings releases. **Figures cross-checked by hand against the filed statements:** D&A
  $61,674 thousand (agrees across MD&A narrative, the filed cash-flow statement and XBRL);
  operating income $20,029 thousand = gross profit $405,261 less OSG&A $385,232; acquisition
  outflows FY2020 $104,436 thousand and FY2023 $6,685 thousand; operating cash flow FY2011-13
  $65,520 / $82,626 / $84,436; and the peer figure that carries the competitor row, Valvoline's
  $389.9M operating income on $1,710.3M of revenue (10-K `0001674910-25-000135`).
  **PASS/FAIL: FAIL AT Q2 - OUT, ON THE BUSINESS.** Monro fails **[E3-03]** criterion (2) on
  its own Competition section, which calls its segment *"fragmented and highly competitive"*,
  names *"independent garages, and gas stations"* among the substitutes, and says competition
  is *"based primarily on price."* And **[E3-03]'s own demonstration test - aggressive pricing
  producing high returns on capital - runs backwards in the filings.** Monro publishes a
  physical series in Item 1 of every 10-K, which is what **[E4-55]** asks for: **vehicles
  serviced fell 6.2 million (FY2019) to 3.8 million (FY2026), -38.7%**, while **sales per
  vehicle rose $194 to $305, +57.3%**. Dollar sales fell only 3.6% because the price carried
  them. **Operating margin went 10.56% to 1.73% anyway**, and **return on unleveraged net
  tangible assets [E2-43] went 21.5% to 2.4%** (3.1% removing the post-ASC-842 ROU asset so
  both years sit on one basis). Tangible book equity is **negative $152.6M**.
  **THE COMPETITOR ROW REFUTED THE HYPOTHESIS THAT WOULD HAVE KEPT THE FILE OPEN.** Five filed
  peers, operating margin, each over its own fiscal window ending 2019 to latest: **Valvoline
  22.04% to 22.80% (+0.76)**, Driven Brands 11.66% to 12.41% (+0.75), O'Reilly 18.92% to
  19.46% (+0.54), AutoZone 18.68% to 19.06% (+0.38), Advance Auto Parts 6.97% to -0.50%
  (-7.47), **Monro 10.56% to 1.73% (-8.83)**. The closest peer by business model - Valvoline,
  which also sells labour hours out of service bays to walk-in retail customers - **expanded**
  its margin to thirteen times Monro's. **The category did not break. This company did.** The
  four largest direct competitors (Mavis, Discount Tire, Les Schwab, Bridgestone Retail) are
  private or unsegmented and are named as unavailable; that would hold a WIDE claim
  PROVISIONAL, and does not bind, because the row is used only to test the category
  hypothesis.
  **[E4-04] was checked against the 2026-09-20 ruling and does NOT fire.** This is not the
  perimeter close: the finding is about the business, from the filings, and there is no
  document I cannot get. **Not OUT on a competence limit - OUT on [E3-03] evidence.**
  **PRIORS REFUTED.** (a) The ORLY **distribution-density** moat case does **not** transfer:
  Monro **sold** its wholesale and distribution operations to American Tire Distributors in
  June 2022 and now rents category management, ordering and inventory services back from a
  counterparty that also serves the field. (b) The `acq_note` understates the roll-up by a
  factor of nine: **$859.7M of acquisitions across FY2010-FY2026, 227% of the hand-struck
  cap**, not the 24% the five-year window could see - and the line has been **zero for three
  consecutive years** while the store count went 1,304 to 1,115 and 145 stores closed in one
  quarter. That is **[E3-51]**'s surfer off the wave, and **[E4-36]**'s fourth cause of
  extreme success rather than an ownable one. (c) The **ASC 842 discontinuity** the KBH run
  found is **absent** here: operating leases sat in operating cash both before and after
  adoption and capital/finance leases sat in financing both before and after, so the OCF
  series is like-for-like; the **balance sheet** is not (assets $1,312M to $2,049M on
  adoption), which is why the return table shows FY2026 twice.
  **NO PRICE BAND ARMED - the QLYS ruling (2026-09-07).** A name that failed on the business
  gets no alert. **Reversal condition, in words: three consecutive fiscal years of RISING
  vehicles serviced, as disclosed in Item 1, together with operating margin above 6%.** A
  recovery in dollar sales alone does not qualify, and the last seven years are the proof.
  **Owner earnings, rebuilt across all seventeen filed years** (COMPUTATION - NOT A CLEARANCE;
  Q5 did not open): with (c) disclosed as **cash capex plus finance-lease principal** - because
  783 of 1,115 stores are leased and finance-lease principal never touches operating cash -
  the mean is **$37.9M over 3 years, $69.3M over 5, $68.4M over 7, $75.5M over 10 and $70.4M
  over 17**, and **FY2026 alone is NEGATIVE $3.8M**. That construction agrees with the corpus's
  own D&A default **[E3-44, E2-41]** within a few million at every window ($37.1M / $66.4M /
  $70.0M / $73.5M / $69.3M), which is why **the cash-capex-only end, the source of the screen's
  $107M top, is named INVALID** - the mirror of **[E5-20]**: here depreciation runs *above*
  cash capex precisely because the lease-financed half of the estate never reaches the capex
  line. Against the hand-struck cap the range runs from **negative to 18.6%** depending
  entirely on which years are averaged, which is **[E4-25]**'s too-wide-to-conclude in dollars,
  and is itself a statement that the seventeen-year mean averages two different companies.
  **TOOLING DEFECTS FOUND, four new ones.** (1) The `cap_flag` date mismatch, above. (2)
  **`floor_screen.capital_acquired()` adds a NON-CASH lease-inception entry**
  (`RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability`) to cash capex as if it were
  annual maintenance capex. For MNRO it resolves in **five of seventeen years**
  ($19.2M/$14.6M/$64.4M/$104.2M/$8.8M, then nothing), driving FY2020 owner earnings to
  **-$2.8M** - the single negative value that trips the straddle-zero refusal, which produces
  `level_shift_oe n/a`, which produces `flags_disagree`. **One non-cash entry cascades into
  three CSV flags.** Proposed one-tag fix: use **`FinanceLeasePrincipalPayments`**, which is
  smooth, cash, available every year from FY2020, and lands on the corpus default. This can
  fire on every lease-heavy filer in the queue - every retailer, restaurant chain and
  service-bay operator. (3) **Three CSV note columns are sliced mid-sentence** in
  `Screens/regen_queue.py`: `level_note[:60]`, `level_note_oe[:70]`, `acq_note[:110]`, while
  `wc_note` gets 260 and `cap_flag` is written in full at 252. **The truncation inverted the
  meaning here**: `level_note_oe` reads *"the pre-window years run from $-2.8M to $1"*, which
  looks like a near-zero range, when the recovered full string ends at **$170.3M**; and
  `level_note` is cut at *"a tight spread her"*, losing the words *"e is not safety."* (4)
  **`best_year_dep_oe` has no note column at all** - the CSV carries the number 0.265 and
  discards the string the function returned, *"TWO YEARS JOINTLY CARRY THE WINDOW - the exact
  two-year-boom shape leave-one-out cannot see; re-price on a window that excludes both."*
  There is a `best_year_note` for the operating-cash series and none for the series that is
  actually valued. Both (3) and (4) are the defect class this file's own FOLD section names:
  **a diagnostic that exists but never reaches the reader.**
  **LEDGER COUNT, recorded again and NOT fixed:** `principle_ledger.csv` holds **311 rows**
  and `tools/check_framework.py` reports 311 (310 verbatim, E5-07 declared not a quote);
  `CLAUDE.md`'s KEY FILES table still says 267. **Thirteenth consecutive fold to record it.
  `CLAUDE.md` is not edited - PRIME RULE 5 puts a structural correction to the operator's own
  file in front of the operator first.**
  **[E4-29] DOES NOT FIRE, and the negative finding is recorded rather than assumed.** The
  CGNX standing instruction was carried out early: both furnished 8-K EX-99.1 releases were
  pulled (`0001193125-26-322170`, 2026-07-29; `0001193125-26-240509`, 2026-05-27) and **the
  word EBITDA appears zero times in either.** "EBITDAR" appears in the 10-K only inside the
  lenders' covenant definitions. What the release did carry was a **moat** claim - *"we were
  able to hold our tire unit volumes flat, and we believe this allowed us to take market
  share"* - which was therefore tested at Q2 and **not sustained**: the same release reports
  comparable store sales **-1.7%**, credits the flat units to customers *"traded-down to
  lower-cost alternatives"* and the expansion of *"tier four"* tires, and reports **adjusted
  operating income BELOW the GAAP figure at 0.8% of sales** with a net loss of $2.1 million.
  Acceptance test PASS before the commit. Run file:
  `Test Runs/2026-09-21 Run - MNRO Monro.md`.

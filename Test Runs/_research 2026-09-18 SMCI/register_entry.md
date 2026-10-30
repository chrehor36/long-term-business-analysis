- **SMCI (Super Micro Computer, Inc.), 2026-09-18 - FAIL at Q2 (OUT, ON THE BUSINESS, ON [E3-03] CRITERION (2) IN THE COMPANY'S OWN WORDS: gross margin given up
  *"to gain market share"* in FY2025 and FY2026, and *"a continued decline of average selling prices across our business and we expect that these historical trends
  will continue"*; the product is the supplier's platform (63.1% of all purchases from one supplier; every FY2026 system line an NVIDIA platform) sold by every rival;
  gross margin 18.01% (FY2023) to 10.82% (FY2026), below Celestica's 12.1% and under half Dell ISG's (25.98%) and HPE Server's (20.89%); 9.2 cents of gross profit per
  incremental dollar of sales FY2023-26 while NVIDIA keeps 71%; [E2-44] fails on both halves, operating cash -$6,809.9M in FY2026 on a $9,648.3M working-capital build;
  [E4-04] engaged, the advantage re-won each platform generation with the old one written down; key-person dependence recorded at Q2 [E4-23]). Q1 IN; Q3, Q4, Q5 and Q6
  RECORDED, NOT GOVERNING under explicit banners (Q3 a GATE case on daily execution, UNKNOWABLE on the binary: an SEC antifraud cease-and-desist order of 2020-08-25
  (Securities Act Rel. 10822) against the company, with the former CFO sanctioned separately and the CEO repaying $2,122,000 under SOX 304; Ernst & Young's 2024
  resignation letter, *"no longer be able to rely on management's and the Audit Committee's representations"*; nine people who left after the 2017 investigation
  rehired, among them (by the filed dates) the co-founder Senior VP who resigned in January 2018 and returned as consultant, officer and director, and who was
  indicted by SDNY on 2026-03-19 for an export-control conspiracy; SEC, SDNY and BIS investigations open; material weakness unremediated at FY2026; flags converge:
  weak accounting, a guidance record missed in both directions, serial issuance, "Adjusted EBITDA" first added in the release that cut FY2025 guidance, CEO paid on
  revenue and stock-price milestones; Q4 UNKNOWABLE: five-year owner earnings -$1.8bn (all of the working-capital increment in (c)) to +$1.0bn (none of it), spanning
  zero; $34.2bn of non-cancelable purchase commitments plus $12.9bn of inventory against $14.5bn of equity; staying power 0-1 of 3; price headed COMPUTATION - NOT A
  CLEARANCE; Q6 records reopening conditions in words and arms nothing). WAVE 5, the first of the seven "perimeter or restatement above threshold" names; run
  unattended from scratch, SMCI's figures rebuilt from its own filings rather than imported from the DELL run. Register entry 102, counted from this file.**
  `Test Runs/2026-09-18 Run - SMCI Super Micro Computer.md` (template `cd6f9aa`, Step 0 and Q1 `530ef45`, Q2 `a141e1c` and `d6b0305`, Q3 `a68666e`, Q4 and the Q3
  correction `26fbaa8`, Q5-Q6, audit and register `70c524e`), `check_framework.py` PASS.
  **THE PAIR.** Price **US$40.35** (2026-09-17 close, Yahoo daily chart, aggregator flagged; **not** `tools/sources.price()`, which returned an intraday
  `regularMarketPrice` of $38.72 stamped 2026-09-18, the TOST defect on a fourth name; corroborated by Form 4s `0001392942-26-000013` and `0001392941-26-000014`, the
  founders' joint sales at $36.60-$40.00 on 2026-09-03/04, inside those days' ranges) x **656,965,384 shares** x 1.0 = cap **US$26,508.6M**. **Count:** the FY2026 10-K
  cover, accession **`0001375365-26-000022`** (filed 2026-08-31), *"As of July 31, 2026, there were 656,965,384 shares of the registrant's common stock ... which is the
  only class of common stock of the registrant issued"*; `cover_shares.py` agrees. ERIC trap checked (issued equals outstanding, 656,882 thousand at 2026-06-30, no
  treasury); SPGI trap checked (no exclusion clause). **Perimeter:** the 7.00% Series A Mandatory Convertible Preferred issued June 2026 ($4.31bn) converts in 2029
  into *"between 30.3040 and 36.3640 shares of Common Stock"* each, **130.7M to 156.8M shares (+20% to +24%)**; the yields use the harder cap with the minimum
  conversion, **US$31,781.7M**, and do not also deduct its dividend. Convertible notes ($4.725bn; conversion prices about $55-61 and above) out of the money, treated as
  debt. **Sovereign USD 30-year 5.29%** (US Treasury daily par yield curve, **09/17/2026**, cache deleted and re-fetched by this run). **No live deal**: `deal_filings`
  empty since the 10-K; every 8-K since 2024-01-01 downloaded and the Item 1.01 ones read (credit facilities, a receivables purchase agreement, convertible indentures,
  the June 2026 offerings); none an offer for Super Micro's shares.
  **The skip reason, tested - A SPLIT ARTEFACT, AN ORGANIC REVENUE STEP, AND A RESTATEMENT GUARD THAT CANNOT SEE THE RESTATEMENT.** The guard that stopped SMCI at the
  2026-09-01 triage was `share_count_shift` at **11.22x**: the 10-for-1 split of 2024-10-01, which the `a8bc84f` code did not divide out (fixed 2026-09-02; the row was
  never re-triaged; the current guard with the ticker returns **1.12x**). `scale_shift` **2.10x** is the organic AI step from $7.1bn (FY2023) to $15.0bn (FY2024) (no
  acquisition beyond $0.3M). `restatement_shift` returned **1.0, a null**: it stops at the first revenue element with data and is blind to the real restatement of
  FY2015-16 (filed 2019-05-17), recorded across an element change (`SalesRevenueNet` original $1,991.2M, `Revenues` restated $1,954.4M for FY2015). **The current screen
  prices SMCI with negative owner earnings at every end** (5y capex -$1,794M); SBC resolves and is complete on the face every year; `working_capital_flag` returned
  `None` because it reads only liability-side lines, while the cash went into inventories (-$8,876.7M) and receivables (-$3,921.9M).
  **Q2 - THE COMPETITOR ROW, from filings: Dell ISG, HPE Server, Celestica (the one ODM-type filer on EDGAR) and NVIDIA** (two of the seven rivals the 10-K names; Cisco
  unsegmented, Lenovo IFRS-only, Foxconn, Quanta and Wiwynn not on EDGAR: the row's gap, stated; the gate does not close on it). Operating margin before stock
  compensation 9.62%, 7.13%, 8.15% (FY2024-26) against Dell ISG 11.7-12.8%, HPE Server 7.6-12.7%, Celestica CCS 6.2-8.2%. Pre-tax return on invested capital 21-43%
  FY2022-26 (10.7-17.5% FY2016-21), recorded at full strength and read as turnover times a thin margin that moves with the wave [E4-36, E3-51]. Q4 FY2026 gross margin
  **17.5%** against the company's own 8.2-8.4% guidance, recorded as the strongest fact for and as a one-quarter mix outlier.
  **Q5 COMPUTATION - NOT A CLEARANCE:** business yield on the five-year default **-5.6% (convention: all working capital in (c)) to +2.9% (display: none of it)**
  against **5.29%**; FY2026 alone on the display 6.5%; even the company's own Q1 FY2027 guidance annualised (net income, displayed only) gives 8.4-9.2%, below the ~10%
  floor; value nothing on the convention and **roughly $15-35 a share** on the display at 3-5% growth; price inside the whole range (nothing to about $90): no useful
  conclusion.
  **REVERSAL CONDITION, in words (step 4 of the fold; nothing armed, no PORTFOLIO row):** reopen Q2 only on annual gross margin back above 15% for two consecutive
  10-Ks including a supplier-generation transition, without the *"competitive pricing to gain market share"* sentence; operating cash above stock compensation plus
  capex in a year of 30%+ sales growth; gross margin at or above Dell ISG's and HPE Server's for three years, or the declining-selling-price sentence withdrawn with
  reasons; and a named CEO succession plan with the Special Committee's CFO replacement completed. Q3 would reopen on the SEC, SDNY and BIS conclusions, either way.
  **Defects found in the brief (five):** the probe called `share_count_shift` without the ticker and reprinted the pre-fix 11.2x; it read the 1.0 `restatement_shift`
  as a flag when it is a null; the six memory items all held on the filings (the 2026 matter sharper than suggested: the indicted man was a co-founder director who had
  been brought back); the June 2026 perimeter change (mandatory preferred, 52.3M-share offering, ATM) and the $34.2bn of non-cancelable purchase commitments were not
  anticipated. **Two errors of this run corrected in later commits** (Q2 rival count; Q3 identifications of the rehired and the former CFO labelled as inferences).
  **Survival shapes:** #1 CONTRACTED NOT TO STOP ($34.2bn of non-cancelable purchases against cancellable orders) with #11 THE PASS-THROUGH as the reason margin cannot
  absorb a write-down, #6 THE BORROWED BALANCE SHEET as a feature, and #17 THE PERMIT as a second exposure (export privileges); no new shape.

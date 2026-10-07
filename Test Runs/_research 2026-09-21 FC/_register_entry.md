- **FC (Franklin Covey Co.), 2026-09-21 - FAIL at Q2 (OUT, ON THE BUSINESS).**
  Q1 IN. **WAVE 7, name 12. Register entry 144** (re-derived by counting the register itself with
  a line-start regex `^- \*\*` inside the slice from this file's `## COMPLETED FROM THE QUEUE`
  **heading line** (line 502, not its earlier textual occurrences) to `## THE WRITE-EARLY
  PROTOCOL`: **143 entries stood above this one, 143 distinct tickers, no duplicate**, which
  agrees with the MGPI entry directly below claiming 143). **Price US$17.27**, close of
  2026-09-18, aggregator (Yahoo Finance chart endpoint), flagged, raw response on disk at
  `_research 2026-09-21 FC/yahoo_FC_chart.json`. **Shares 11,293,873**, from the **cover of the
  10-Q for the quarter ended 2026-05-31, accession `0001193125-26-297572`, filed 2026-07-07**, as
  of 2026-06-30 -- *"11,293,873 sha res of common stock, $0.05 par value per share, as of June 30,
  2026"* (the space inside "shares" is a filer inline-XBRL span artifact, flagged not smoothed;
  the `dei:EntityCommonStockSharesOutstanding` fact carries the same number). One class only. **No
  splits anywhere in the available history. Cap re-struck by hand: US$195.0M** (11,293,873 x
  $17.27 = $195,045,187), against the screen row's **$231M** -- **the screen's cap is 18% too
  high** and every yield in the file uses $195M. **Sovereign 5.34%, 09/18/2026, US Treasury daily
  par yield curve, 30-year, from the issuing authority**, struck fresh in this run. Currency
  argued, not assumed: FX moved FY2025 consolidated revenue by **$0.2M on $267.1M (0.07%)** --
  *"In constant currency, our consolidated revenue was $267.3 million for fiscal 2025"* -- so USD
  is the earnings currency on the filed evidence. **Newest annual FY2025 (2025-08-31, accession
  `0000886206-25-000085`); FY2026 ended 2026-08-31 and EDGAR was checked rather than assumed --
  NO FY2026 10-K AND NO Q4 EARNINGS 8-K EXISTS YET**, the newest filings being an Item 5.02 8-K of
  2026-09-01 and Forms 3/4.
  **FOUR STEP-0 FLAGS RESOLVED BEFORE Q1 OPENED, AND THE SCORE IS ONE RIGHT, THREE WRONG OR
  INCOMPLETE.**
  (i) `cap_flag` "cap $231M against a filed float of $350M (1.51x) as of 2025-02-28 ... **One of
  the two is wrong**": **NEITHER IS WRONG, and this is the CALM / EMBC / BRBR branch, not a fifth.**
  The FY2025 10-K cover reads *"As of February 28, 2025, the aggregate market value of the
  Registrant's Common Stock held by non-affiliates ... was approximately $ 349.5 million, which
  was based upon the closing price of $31.98 per share"* -- $349.5M / $31.98 = **10,928,706
  implied non-affiliate shares** against *"As of October 31, 2025, the Registrant had 12,155,832
  shares of Common Stock outstanding"*, so the affiliate block is only **~1.0-1.2M shares, 8-10%,
  and there is no control block** (DEF 14A `0001193125-25-324927` shows no holder near a blocking
  stake). **The whole of the 1.51x is nineteen months of price: $31.98 to $17.27 is -46%**, and
  the aggregator reproduces the $31.98 cover close to the cent, which is an independent check ON
  THE FILING. **I second the MGPI run's proposed rewording of this diagnostic -- it should say
  "or the two dates differ."**
  **NEW TOOLING DEFECT (i-a): the screen priced FC off the ANNUAL cover share count when a newer
  10-Q cover count existed and was 7.1% lower.** The `newest_periodic` column already knew the
  later periodic existed (`2026-05-31`); the share count did not follow it. On a filer retiring
  ~5% of its shares a year this overstates the cap on every row, and the error points the wrong
  way -- it makes names look DEARER than they are, so it will have suppressed candidates rather
  than promoted them.
  (ii) `wc_note` "ONE LINE MADE THE CASH: ContractWithCustomerLiability moved 43% of 2021 OCF":
  **RIGHT, AND IT IS THE FIRST TIME IN FOUR RUNS.** I ranked every FY2021 working-capital line
  with its sign against OCF of $46,177k: deferred revenue **+19,788 (+42.9%, PRODUCED)**, accounts
  payable and accrued +14,372 (+31.1%), accounts receivable -14,266 (-30.9%), other liabilities
  -1,860, prepaid -880, inventories +463, income taxes +273, related party 0 -- net **+17,890
  (+38.7%)**. **The flag names the actual largest mover and gets the sign right.** The
  EMBC/MCFT/BRBR inversion pattern does NOT reproduce; the honest standing instruction is to rank
  every line every time, not to expect inversion. **And the answer to the question the flag is
  for:** FY2021 operating cash is real (customers prepay; FY2025 carries **$106,534k of deferred
  subscription revenue plus $16,327k of customer deposits against $242,912k of total assets** --
  [E3-52]'s covenant-free, undated class), **but the increment is a growth stream, not an earnings
  stream, and the filings prove it inside the window**: +19,788 (FY21), +14,245, +8,806, +13,458,
  **+3,151 (FY25)**, and **-12,022 over the three quarters to 2026-05-31**. Operating cash tracked
  it: $60.3M -> $29.0M -> $17.5M for nine months.
  (iii) `spread_caveat` "4-construction width only ... rebuild it [E4-25]": **REBUILT OVER
  EIGHTEEN FISCAL YEARS (FY2008-FY2025) BY HAND from the CONSOLIDATED STATEMENTS OF CASH FLOWS of
  eight 10-Ks** -- FY2010 `0000886206-10-000031`, FY2013 `...-13-000032`, FY2016 `...-16-000075`,
  FY2019 `...-19-000036`, FY2021 `...-21-000040`, FY2022 `...-22-000028`, FY2024 `...-24-000060`,
  FY2025 `...-25-000085`, overlaps agreeing year by year. **The screen's $24-31M band is the
  FY2021-FY2025 window and nothing else** (my rebuild reproduces its bottom at $25.4M, so the
  construction is not in dispute -- the WINDOW is). **The eighteen-year mean is $9.5M at the D&A
  end of (c) and $13.3M at the total-capex end; the ten-year is $15.6M/$19.2M.** Combined range
  carried as **$9.5M to $25.4M, a factor of 2.7**, straddling the [E4-28] floor. **`level_shift
  1.31 (no step)` and `best_year_dep 0.09 ("no single-year dependence")` are both FALSE on the
  rebuilt series**: the step is FY2020->FY2021 (FY16-20 OCF mean $25.0M against FY21-25 $44.7M,
  **1.79x**, and it did not hold), and **FY2024 alone is 30.6% of the five-year owner-earnings sum**.
  **NEW TOOLING DEFECT (iii-a), AND IT IS THE ONE THAT MATTERS MOST: FC's capex is split across a
  us-gaap tag and a COMPANY EXTENSION, and `companyfacts` carries only the first.** The investing
  section has three capitalised lines; only *Purchases of property and equipment* is
  `PaymentsToAcquirePropertyPlantAndEquipment`. *Capitalized curriculum development costs* is
  **`fc:PaymentsForCurriculumDevelopmentCosts`**, and **SEC companyfacts carries no custom
  taxonomy namespace at all** (FC's file has none). **Measured: FY2025 capex is $8,253 + $7,561 +
  $1,074 = $16,888k filed against $8,253k visible -- the screen sees 49%. FY2023: $13,550 against
  $4,515, 33%. Over FY2008-FY2025 the screen sees $67.4M of $149.1M, 45%.** Same class as the
  Marvell capitalised-IP-licence limit; a SOURCE LIMIT, not a bug. **The company itself agrees:
  its own Free Cash Flow definition subtracts "purchases of property and equipment, curriculum
  development, and content or license rights."**
  **NEW TOOLING DEFECT (iii-b): the D&A tags resolve to $4.1M for FY2025 against a filed $8,458 +
  $4,440 = $12,898k**, because FC splits *Depreciation* and *Amortization* on the face of the
  income statement and tags the cash-flow add-backs separately. A run using the undimensioned D&A
  fetch would have set (c) at a third of its true default and overstated owner earnings by ~$8M a
  year -- the [E5-06]-shaped error in the (c) input rather than the SBC input.
  (iv) THE EMPTY COLUMNS. **`acq_note` empty is FALSE and the diagnostic is now 0 for 4** (CGNX,
  CE, MGPI, FC): **nine acquisitions in the filed window**, $ thousand -- FY2009 1,157, FY2010
  3,256, FY2011 5,411, FY2013 4,185, FY2014 6,167, FY2015 262, FY2017 7,272, FY2018 1,108, FY2019
  32, FY2021 10,209 -- plus licence/content rights of 750, 750 and 1,074. **~$41.6M against a
  $195M cap.** **`deal_note` empty is TRUE for a live deal but INCOMPLETE for the perimeter**: no
  DEFM14A/S-4/425 anywhere, and the five Item 8.01 8-Ks of the last year are **conference-call
  scheduling notices** -- I OPENED the 2026-06-17 one rather than assume -- but two real perimeter
  events sit inside the window that no flag saw, the **FY2008 sale of the Consumer Solutions
  business unit** ($28,241k of proceeds, $9,131k gain, which is why FY2008 owner earnings are near
  zero) and the **FY2025 conversion of the France licensee to a directly owned office**.
  **`name_change_note` empty is GENUINELY CORRECT** and was checked in the filing history, not the
  field: `formerNames` is NOT empty (*FRANKLIN QUEST COMPANY*, *FRANKLIN QUEST CO* to 1997-02-11)
  but falls outside the detector's 2017 window, and **CIK 0000886206 with file number 001-11107
  carries unbroken through the 1997 Covey Leadership Center merger -- a rebrand, not a Rule
  12g-3(a) successor substitution, and eleven years before the earliest year in the series. The
  BRBR defect class does not reproduce here.**
  **Q1 IN.** Two customers, one product. An employer buys an annual site licence to copyrighted
  leadership content (the All Access Pass) plus consultant days; a school buys the same thing as
  Leader in Me. Both invoiced in advance. **Gross margin 76.2% ($267,067 revenue against $63,498
  cost of revenue) and SG&A 68.4% of revenue ($182,684), leaving income from operations of $5,704k
  -- 2.1%.** The scarce input is the IP (*"We claim rights for 706 trademarks"*, *"We claim 265
  registered copyrights"*); what it does NOT control is the salesperson and the consultant, which
  the 10-K says itself.
  **Q2 OUT ON THE BUSINESS -- IT IS A BUSINESS, NOT A FRANCHISE [E3-43], AND THE FILER'S OWN
  10-K IS THE EVIDENCE.** [E3-03] criterion 2 fails. FC names **twenty-four competitors across
  nine categories** unprompted (*"McKinsey & Company, Deloitte, and Accenture ... Korn Ferry and
  Heidrick & Struggles ... DDI, LHH, and Blanchard ... BetterUp, CoachHub, and Ezra ... RAIN
  Group, Sandler, and Challenger ... Workboard, Amplify, and Cornerstone ... Udemy Business and
  LinkedIn Learning"* plus five Education names) -- **and a list is not by itself a finding, so
  what makes it one is that FC's own ten "principal competitive factors" include "Competitive
  pricing."** Then the customers behaved like customers with substitutes: *"many of our clients
  ... have sought to reduce their spending ... which led to delayed decision making, decreased
  contract expansion, and **lower client retention**."* **[E2-44] fails on the filed conduct** --
  in a flat-demand, under-utilised year FC did not raise price, it took **$6,723k of restructuring**
  (against $3,008k) while operating income fell from $33,042k to $5,704k -- and **[E4-37]'s agony
  metric is filed as a risk factor**: *"we may shift the type and pricing of our offerings, which
  may adversely impact client renewal rates."*
  **THE COMPETITOR ROW, SEVEN NAMES, TWELVE YEARS, EACH FROM THE PEER'S OWN 10-K** (EBIT / (total
  assets - current liabilities), us-gaap `OperatingIncomeLoss`/`Assets`/`LiabilitiesCurrent`,
  newest vintage; **FC's FY2025 cross-checked to the filed statements: income from operations
  $5,704k, total assets $242,912k, total current liabilities $157,292k, CE $85,620k**). Peer set
  derived from FC's OWN competition disclosure -- of the twenty-four names, **only four file**;
  Skillsoft and Coursera added as the listed form of the learning-library class FC does name, and
  said so; the rest are private partnerships, venture-held, inside Adecco, inside Microsoft, or
  private since 2021, each named:
  **FC 15.3 / 12.1 / 10.1 / -6.8 / -2.8 / 2.2 / 3.0 / 7.2 / 22.5 / 28.0 / 33.3 / 6.7 (FY14-25),
  12-year mean 10.9%** * **Accenture 33.9% mean, never negative** * **Korn Ferry 10.1%** *
  **Heidrick & Struggles 7.8%** * **Udemy, Coursera and Skillsoft NEGATIVE IN EVERY FILED YEAR.**
  **FC's twelve-year return on capital employed IS Korn Ferry's, a third of Accenture's, and the
  pure content-library class loses money at the operating line every year -- which says the
  library alone is worthless and the consultants are what is being sold.** And the FY2022-24 run
  is partly denominator: **capital employed fell from $162.3M (FY2014) to $85.6M (FY2025), -47%,
  on $289,933k of treasury stock against $66,911k of equity** -- [E2-47]'s carve-out.
  **DIRECTION NARROWING [E4-32], on four independent filed series:** (1) revenue $287,233 ->
  $267,067 (**-7.0%**) with FY2026 guidance CUT on 2026-07-01 to *"$260 million to $267 million"*
  from $265-275M -- **and growth from FY2019's $225.4M to the FY2026 midpoint is 16.9% nominal
  over seven years, below CPI, so in real terms this business has not grown since 2019**;
  (2) **units, where units exist [E4-55]** -- new Leader in Me schools **739 (FY2022, "a record")
  -> 728 (FY2024) -> 624 (FY2025), -14%** -- while Enterprise publishes **no unit metric at all**,
  only the dollar word *"invoiced"*; (3) operating margin **11.5% -> 2.1% on a 7% revenue fall**,
  which is [E2-58]'s shape; (4) **THE RETENTION METRIC WAS WITHDRAWN** -- FY2021 *"annual AAP
  revenue retention remained above 90 percent"*, FY2022 *"remained well above 90 percent"*, FY2024
  *"greater than 90%"*, **FY2025 NO NUMBER**, replaced by *"the majority of our clients are
  renewing"* in the same document that concedes *"lower client retention."* **[E4-36]/[E3-51]: the
  FY2022-24 run reads as WAVE-RIDING**, and FY2025 plus three quarters of FY2026 are the shallows.
  **[E3-33]/[E5-28] untapped pricing power: NO** -- FC's $267.1M is **0.14% of the
  *"approximately $188 billion"* US market its own 10-K defines**, with no client over 10% of
  revenue. Class NONE, direction NARROWING. **Asked aloud and answered: there is no unread
  document, so this is not UNRESEARCHED; and the 2026-09-20 [E4-04] ruling that closes a name
  UNKNOWABLE applies to names that PASS [E3-03], which FC does not reach.** OUT.
  **Q3-Q6 RECORDED BENEATH THE CLOSE, NO VERDICTS, arithmetic headed COMPUTATION - NOT A
  CLEARANCE (operator rule 3).** The material the next reader needs:
  **[E4-29] FIRES HARD, and only the EX-99.1 shows it** -- the Q3 FY2026 release headline block is
  five bullets in ascending order of goodness ending *"**Adjusted EBITDA Increases 14% to $8.3
  Million**"*, the CFO's quote leads with it, **guidance is given in it**, the segment note reports
  in it, and **management is paid on it** (proxy: *"split between adjusted EBITDA (50% weighting)
  and ... net revenue (20% weighting)"*; **"Qualified Adjusted EBITDA" is the Company-Selected
  Measure** and *"comprises the largest portion of the performance metrics for determining our
  LTIP and STIP awards"*). **FC's definition deletes D&A, SBC AND restructuring -- three things
  the corpus names as real expenses in three separate places [E4-29, E5-06, E3-53/E5-33] -- a
  ~$25.4M wedge between FY2025 Adjusted EBITDA of $28.8M and income from operations of $5,704k.**
  **And the mechanism the flag exists to catch is in the same release: while Adjusted EBITDA rose
  14%, operating cash fell to $1.1M from $6.3M, free cash flow was $(1.0)M against $2.8M, and cash
  fell to $12.0M from $33.7M.** A run reading only the 10-K would have missed the headline block.
  **[E2-49] FIRES on the withdrawn retention metric (above); my prior now reads SEVEN FIRES AND
  FIVE FAILURES** (SHOP, MRVL, PAY, ARM, CALX, BE, FC v. QLYS, CRM, CORT, PLTR, INOD). **The
  candor case of the same family is stated beside it [E4-26]:** PSUs vested through FY2024 on *"the
  highest rolling four-quarter Adjusted EBITDA performance within the three-year cycle"* -- a
  HIGH-WATER MARK, so the FY2023-25 cycle paid against **$56.0M while FY2025 actual was $28.8M** --
  and FC **redesigned it ahead of the deterioration** to cumulative revenue/EBITDA over FY2025-27.
  **More disconfirming evidence, hunted deliberately:** the bad year was NOT paid (*"resulting in
  no payout for the financial component of the STIP for the NEOs"*), upside was cut in advance
  from 200% to 150% with reasons, and **FC's own Free Cash Flow definition is stricter than the
  screen's capex.** **[E4-30] does not fire in either direction** -- growth is conspicuously
  UNsmooth and **cash taxes are RISING** ($3,308 -> $4,205 -> $7,693) against falling pretax income.
  **[E2-01] fifteen-year ROE 6.1 / 9.2 / 14.5 / 15.5 / 8.8 / 6.4 / -8.0 / -7.1 / -1.3 / -13.3 /
  19.6 / 22.7 / 22.0 / 28.9 / 4.1 -- mean 8.5%, five negative years**, on equity cut 47% by
  buybacks; **against paid-in capital plus retained earnings of $356.5M, FY2025's $3,068k is 0.9%.**
  **THE BUYBACK IS THE LARGEST DECISION THIS MANAGEMENT MAKES AND IT IS A LIVE [E5-08] QUESTION
  ON BOTH CONDITIONS.** FY2023 through three quarters of FY2026: **$120,796k gross, less $5,422k
  of reissue proceeds = $115,374k net, for a share count from 13,853k to 11,293,873 -- 2,559k net
  shares, $45.09 of net cash per net share retired, against $17.27 on 2026-09-18** [E5-24]. On
  condition (1): in nine months FC generated $17,476k of operating cash and $8,477k of free cash
  flow and spent **$28,118k** on buybacks; **cash fell $31,698k -> $11,972k**; [E5-39] refuses to
  count the $62.5M revolver and **FC has published no liquidity floor** [E5-25]. On 2025-08-11 the
  Board replenished the authorisation to $50.0M and **on 2025-08-14, three days later**, FC
  *"initiated a 10b5-1 plan to purchase up to $10.0 million ... through daily purchases."* Humility
  clause attached and not decorative [E4-13].
  **Q4 STAYING POWER [E5-11]: (1) LARGE, NOT RELIABLE** -- five negative net-income years in
  fifteen, owner earnings -$5.5M to +$38.8M; **(2) NOT massive liquid assets** -- $11,972k at
  2026-05-31, about **eighteen days of operating cost**, with the mitigant stated ($122.9M of
  customer prepayments, covenant-free and undated [E3-52]); **(3) near-term cash requirements
  mostly clean** -- **$823k of notes payable, nothing long-term, revolver undrawn, cash interest
  paid $496k**, but the 2023 Credit Agreement restricts distributions unless Leverage <3.00x and
  FCCR >1.15x **before and after**, so a further Adjusted-EBITDA decline closes the buyback.
  **THE NAMED DEATH, QUANTIFIED [E2-27, E3-24, E4-40]:** 100% of revenue is a discretionary line
  in someone else's budget, sold by a fixed salesforce against twenty-four named alternatives and
  a zero-marginal-cost substitute. **SG&A is 89.7% of gross profit. A second -7.0% year removes
  $14.3M of gross profit against $5.7M of operating income -- an $8.6M operating loss unless costs
  come out first, and a -2.8% year takes operating income to zero.** Not hypothetical: **FY2017-20
  were four consecutive net-loss years in this filing history.** **Likelihood: A REAL
  POSSIBILITY.** It does not kill the company -- no debt, no maturity, customers prepay -- **it
  returns FC to what it was between 2017 and 2020, a going concern earning nothing for its owners
  for several years at a stretch.** [E4-51]'s bear-case test answered with the holders' strongest
  fact recorded rather than buried: three consecutive quarters of Enterprise North America
  invoiced growth and Enterprise deferred revenue up 15% year on year.
  **Q5 COMPUTATION - NOT A CLEARANCE, AND THE UNCOMFORTABLE PART: THE PRICE WAS NEVER THE
  PROBLEM.** $9.5M-$25.4M of owner earnings on the re-struck $195.0M cap is a **4.9% to 13.0%**
  yield against a **5.34%** sovereign. **The five-year window CLEARS the ~10% floor at 13.0%; the
  ten-year (8.0-9.8%) and eighteen-year (4.9%) do not.** The file closed anyway, and it closed on
  the business -- which is the framework working in the order it is written [E5-42, E2-31]. **Had
  the gates cleared, a range straddling the floor by a factor of 2.7 is [E4-25]'s "no useful
  conclusion" and that would itself have been the verdict.** No bar chosen, no margin applied,
  **windage count 0**.
  **Q6: NO ALERT BAND AND NO PORTFOLIO ROW (the QLYS ruling) -- a name that failed on the business
  does not get a price trigger.** The reversal condition is in words: **(1)** a filed price
  increase taken and held with retention intact ([E4-37]'s yawn); **(2)** AAP revenue retention
  **published as a number again above 90%**; **(3)** two consecutive years of revenue growth above
  CPI; **(4)** EBIT/capital employed durably above Korn Ferry's and Heidrick's across a full cycle
  rather than for the three years of a wave. **The way back in is a franchise finding, not a
  cheaper price** -- and [E3-47] is carried openly, because FC is inside the circle and a
  wrongly-closed file there is the expensive error class.
  `tools/check_framework.py` **PASS** (0 phantom citations, 0 unlabelled numbers, every ledger row
  verbatim) before the commit. **93 ledger ids cited in the run file, 0 phantom**, verified
  against `principle_ledger.csv` directly.
  Run file: `Test Runs/2026-09-21 Run - FC Franklin Covey.md`. Research:
  `Test Runs/_research 2026-09-21 FC/`.

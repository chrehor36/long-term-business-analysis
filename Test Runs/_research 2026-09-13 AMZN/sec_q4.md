
---
## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the queue asks every run for a price and because the evidence was gathered; it decides nothing and cannot reopen Q2 [E2-37, E3-39].

### First: THE SKIP REASON, TESTED. It was not [E5-20]. It was a tag-union defect fixed the next day.
The wave 5 table carries AMZN under *"capex unresolved [E5-20]: build (c) by hand from the filing"*, and the ABNB run asked this
name to test which case it is before assuming the exception. **Tested by running the screen as it stood when the label was written.**
- The watchlist queue with the "capex unresolved" row was created at commit `a8bc84f` (2026-09-01 22:15). `Screens/floor_screen.py`
  at that commit, run on Amazon's companyfacts today, returns **`CAPEX_UNRESOLVED`**, and its `annual()` returns capex only for
  FY2007-FY2016.
- **The reason is in the tags, not the business.** Amazon's capex sits under `PaymentsToAcquirePropertyPlantAndEquipment` for FY2007-2016
  (the net-of-incentives line, $6,737M for 2016) and under `PaymentsToAcquireProductiveAssets` from FY2016 on (gross, $7,804M for 2016,
  $131,819M for 2025). The old `annual()` stopped at the first tag that yielded any data (the docstring's own words: *"The previous
  version wrote `if by_end: break` - the first tag yielding ANY data won and the rest were never read"*), so every window after 2016
  had no capex and the screen refused.
- **The fix landed at `dff6ab6` (2026-09-02 12:23), fourteen hours after the label was written**, and the current `floor_screen.py`
  prices Amazon: `{'5y_da': 18,421, '5y_capex': -13,770, '3y_da': 35,874, '3y_capex': 961}` ($M). The capex end reproduces to the
  dollar from the hand table below as **gross capex plus finance-lease additions** (-13,770 and 961); `run.py`'s -11,342 and 2,430
  are the same windows on gross capex alone (Step 0). The screen's `_da` end uses the broad cash-flow D&A line ($65,756M in 2025,
  which includes capitalized content and operating-lease amortization), not property-and-equipment depreciation.
- **So the label was wrong for this name for a second, different reason than at ABNB.** At ABNB the tag gap was real (a presentation
  change) and the exception did not fit. At AMZN there was no gap in the filing at all; the gap was in the screen. **Whether the
  [E5-20] exception applies is then a separate question, and it is answered below on the filed record, not on the label.**

### The construction, audited
`oe.py` (the killed session's scratch) was read line by line and **every input re-read against the filed statements**: OCF, SBC,
purchases of property and equipment, proceeds from sales and incentives, principal repayments of finance leases and of financing
obligations (cash-flow statements, FY2017 10-K `0001018724-18-000005` through FY2025 10-K `0001018724-26-000004`, newest vintage
where restated: 2016 OCF $17,272M as first filed, $17,203M from the FY2018 10-K on); property acquired under finance (capital) leases
and build-to-suit arrangements (supplemental cash-flow tables); total net additions to property and equipment and P&E depreciation
(segment note and Note 3). TTM = FY2025 − H1 2025 + H1 2026 from the 10-Q `0001018724-26-000026`, whose cash-flow statement also prints
the twelve-month column directly (OCF 161,403; SBC 19,314; capex 173,028; proceeds 4,021; lease principal 1,599; financing-obligation
principal 308; finance-lease additions 4,048 — every one matched). **One input was wrong and none of its outputs used it**: build-to-suit
additions for 2021 were carried as 5,846; the FY2021 10-K supplemental table reads *"Property and equipment acquired under build-to-suit
lease arrangements | $ | 1,362 | | | $ | 2,267 | | | $ | 5,616"*. Corrected in `oe2.py`, which also defines what `oe.py` never wrote
down:
- **"cash plant"** (oe.py's "cash basis") = purchases of P&E − proceeds from sales and incentives + principal repayments of finance leases
  + principal repayments of financing obligations. Leased plant enters when its principal is paid.
- **"formation (TNA)"** = the segment note's *"Total net additions to property and equipment"*, which *"include technology infrastructure
  assets and the effect of non-cash activity such as property and equipment acquired but not yet paid"* and include finance-lease and
  build-to-suit additions. Leased and unpaid plant enters when it is placed.
- Added: **gross capex + finance-lease additions** (the current screen), and **net capex + finance-lease and build-to-suit additions**
  (the MSFT run's convention, `_research 2026-09-06 MSFT/CORRECTION - finance leases and the screen row.md`). Operating-lease assets are
  excluded throughout: their cost is already inside OCF.

**Finance leases, decided: they are capital spending by another route and they enter (c).** 2016-2021 Amazon acquired **$58.3bn** of
property under capital/finance leases (5,704 / 9,637 / 10,615 / 13,723 / 11,588 / 7,061), much of it servers (FY2019 10-K: equipment
*"included in "Property and equipment acquired under finance leases" of $13,723 million"*), and the principal was repaid in
**financing**, never in OCF. Gross capex alone understates 2016-2020 plant by about half. The two lease routes (additions at placement;
principal at payment) are both shown because they time the same spending differently.

### Stock compensation — subtracted in full **[E5-06]**; RESOLVES and is COMPLETE
- The cash-flow add-back *"Stock-based compensation"* resolves in **every year 2016-TTM** from the filed statement (2,975 / 4,215 / 5,418 /
  6,864 / 9,208 / 12,757 / 19,621 / 24,023 / 22,011 / 19,467 / TTM 19,314). XBRL carries it under `ShareBasedCompensation` (and
  `AllocatedShareBasedCompensationExpense` for interims); no year is missing, dimensioned or zero.
- **Completeness, read line by line** (the Boeing check): the operating block carries no other equity-settled line (the lines are D&A,
  SBC, non-operating expense (income), deferred income taxes, and working capital). The equity statement's *"Stock-based compensation and
  issuance of employee benefit plan stock"* is **$23,960M / $21,841M / $19,161M** (2023-25), within 0.3-1.6% of the add-back and *below*
  it. The proxy describes the 401(k) as *"401(k) with company match"*; no stock-settled match or pension contribution appears in the
  cash-flow statement or the equity statement.
- **SBC/OCF: 20.9% cumulative 2016-25; 22.6% 2021-25; 12.0% TTM** (42.0% in 2022). Far below the calibrated row (CRWD 68.0%, ABNB 49.6%).
  The [E3-70] grant-date measure was not rebuilt: under 50% of OCF, the resume state's hand-read threshold is not met; the charge is the
  floor of the subtraction and is stated as such.

### Owner earnings by year, $M (`_research .../oe2.py`, output `oe2_out.md`)
| year | OCF | SBC | OCF−SBC | gross capex (run.py) | gross capex + FL adds (screen) | net capex + FL + BTS adds | cash plant | formation (TNA) | (c)=1.3× P&E D&A | (c)=P&E D&A | TNA ÷ D&A |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 17,203 | 2,975 | 14,228 | 6,424 | 720 | 578 | 3,484 | 643 | 5,908 | 7,828 | 2.12× |
| 2017 | 18,365 | 4,215 | 14,150 | 2,195 | -7,442 | -9,086 | -907 | -15,633 | 2,670 | 5,319 | 3.37× |
| 2018 | 30,723 | 5,418 | 25,305 | 11,878 | 1,263 | -274 | 6,196 | 237 | 9,526 | 13,167 | 2.07× |
| 2019 | 38,514 | 6,864 | 31,650 | 14,789 | 1,066 | 3,876 | 9,306 | 1,632 | 11,955 | 16,500 | 1.98× |
| 2020 | 66,064 | 9,208 | 56,856 | 16,716 | 5,128 | 7,957 | 11,117 | -1,120 | 35,745 | 40,617 | 3.57× |
| 2021 | 46,327 | 12,757 | 33,570 | -27,483 | -34,544 | -34,503 | -33,151 | -38,755 | 3,788 | 10,661 | 3.16× |
| 2022 | 46,752 | 19,621 | 27,131 | -36,514 | -37,189 | -35,085 | -39,379 | -33,705 | -5,270 | 2,207 | 2.44× |
| 2023 | 84,946 | 24,023 | 60,923 | 8,194 | 7,552 | 11,791 | 8,135 | 12,579 | 21,630 | 30,698 | 1.60× |
| 2024 | 115,877 | 22,011 | 93,866 | 10,867 | 10,013 | 15,257 | 13,496 | 8,114 | 52,179 | 61,799 | 2.67× |
| 2025 | 139,514 | 19,467 | 120,047 | -11,772 | -14,683 | -11,625 | -10,158 | -22,305 | 65,629 | 78,187 | 3.40× |
| **TTM 2Q26** | 161,403 | 19,314 | 142,089 | **-30,939** | -34,987 | -30,966 | -28,825 | **-60,701** | 77,426 | 92,348 | **4.08×** |

**Plant formation has run at 1.6-4.1× P&E depreciation in every year for a decade, and at 4.08× in the latest twelve months.**

### MORE THAN ONE WINDOW, BOTH (c) ENDS — THE SPREAD IS PART OF THE RANGE **[E4-25, E4-38]**
| window | gross capex | + FL adds (screen) | net + FL + BTS | cash plant | **formation (TNA)** | (c)=1.3× D&A | **(c)=D&A (INVALID, below)** |
|---|---|---|---|---|---|---|---|
| **5-yr 2021-25 (the corpus default [E2-42])** | -11,342 | -13,770 | -10,833 | -12,211 | **-14,814** | 27,591 | 36,710 |
| 3-yr 2023-25 | 2,430 | 961 | 5,141 | 3,824 | -537 | 46,479 | 56,895 |
| 10-yr 2016-25 | -471 | -6,812 | -5,111 | -3,186 | -8,831 | 20,376 | 26,698 |
| 5-yr 2016-20 | 10,400 | 147 | 610 | 5,839 | -2,848 | 13,161 | 16,686 |
| 5-yr to TTM (FY2022-25 + TTM; TTM overlaps H2 2025, stated) | -12,033 | -13,859 | -10,126 | -11,346 | -19,204 | 42,319 | 53,048 |
| **TTM to 2026-06-30** | **-30,939** | -34,987 | -30,966 | -28,825 | **-60,701** | 77,426 | **92,348** |
| 8 years 2016-25 excluding 2021-22 | 7,411 | 452 | 2,309 | 5,084 | -1,982 | 25,655 | 31,764 |

**In dollars and in words, where the bottom sits:**
- **Every capex-based construction is below zero on the five-year default window (−$10.8bn to −$14.8bn a year), on the five years to TTM
  (−$10.1bn to −$19.2bn), on the ten years (−$0.5bn to −$8.8bn) and on the TTM (−$28.8bn to −$60.7bn). That is NEGATIVE: over five years
  Amazon's owners have received no owner earnings on any construction that counts the plant it actually bought.**
- Near zero, not clearly positive: the three years 2023-25 (−$0.5bn to +$5.1bn) and the eight years excluding 2021-22 (−$2.0bn to +$7.4bn).
- **Positive only where (c) is a depreciation multiple:** +$20.4bn to +$92.3bn.
- **Excluding 2021-22 does not rescue the capex ends** (they reach at most +$7.4bn a year on the eight remaining years): the negative
  five-year mean is not a pandemic artefact. It is the plant.

### Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT **[E3-44, E2-41, E5-20, E4-47]**
**Which case is this? The exception class, on the filer's own words, for the plant that is most of the spending.**
- [E5-20]'s class is *"anything whose own filing says depreciation understates renewal"* (THE FRAMEWORK v4, Q4). **Amazon's filing says it
  of its servers:** *"Effective January 1, 2025 we changed our estimate of the useful lives of a subset of our servers and networking
  equipment from six years to five years. The shorter useful lives are due to the increased pace of technology development, particularly in
  the area of artificial intelligence and machine learning. The effect of this change in estimate for the year ended December 31, 2025 ...
  was an increase in depreciation and amortization expense of $1.4 billion ... which primarily impacted our AWS segment"* (FY2025 10-K, Note
  1). The six-year life it reversed had been set a year earlier (*"Effective January 1, 2024, we changed our estimate of the useful lives for
  our servers from five to six years"*). **The depreciation charged in 2024 on that subset was, by the filer's later judgment, too low.**
- The same note **lengthened** heavy equipment (*"Ten to thirteen years"*, *"Ten years prior to January 1, 2025"*), which lowers D&A on
  fulfilment and data-centre infrastructure. The two changes run in opposite directions; the filing states no effect for the second.
- **Where the plant is:** gross P&E at 2025-12-31 **$534.1bn**: servers and networking $172.5bn, heavy equipment $65.5bn, other equipment
  $63.4bn, land and buildings $155.1bn, construction in progress $71.7bn. AWS took **67.8%** of 2025 net additions (96,496 of 142,352) and
  **76.0%** of H1 2026's (90,120 of 118,648). The five-year-lived fleet is the growing majority of the spending.
- **Renewal at current scale (CONVENTION, confessed; `oe2.py`):** gross P&E by class ÷ the midpoint of its filed useful life (buildings 40
  years with land included, servers 5.5, heavy equipment 11.5, other equipment 6.5) = **~$50.7bn for 2025, 1.21× the $41.9bn of P&E
  depreciation.** It overstates slightly (gross includes fully-depreciated assets and land) and understates for a fleet whose next
  generation costs more per unit [E4-47]. The **1.3× D&A column** sits just above it and is the most generous (c) this run will call a
  judgment. **The D&A end (1.0×) is INVALID for this business as constituted** and is shown only as the most generous number constructible.
- **Where in the band (c) sits, and why the band does not resolve.** Unit volume can be kept at ~1.2-1.3× D&A. **Competitive position cannot
  be read off any filed figure**: AWS's rivals spent 3.4-9.0× depreciation in their latest periods (Table A), AWS's backlog doubled on
  commitments from two companies Amazon funds, and the filing does not separate maintenance from growth capex (no instance found of a
  maintenance or growth split in the FY2025 10-K, the Q2 2026 10-Q or the four releases). The corpus says (c) *"must be a guess"*; the guess
  here is that **the true (c) lies somewhere between ~1.3× D&A and total plant formation, and the filing cannot place it**.
- **The prior this tests (the brief's first).** *"The negative capex-only means say something about Amazon's earning power."* **Half right.**
  They are **not** evidence that the business has no earning power: at a renewal-at-scale (c), five-year owner earnings are ~$27.6bn and TTM
  ~$77.4bn. **They are** the honest answer to what owners have been paid: nothing, for five years, on any construction that counts the plant
  bought. The split between the two readings is exactly the (c) judgment, and **the band changes the sign, so by the template's own rule the
  verdict below is UNKNOWABLE on the level** [E4-25].

### The working-capital flag, run by eye (a single line moving by more than 30% of a year's OCF)
- **Fires three times:** 2017 accounts payable **+$7,100M (38.7% of OCF)**; 2021 accounts receivable and other **−$18,163M (39.2%)**; 2022
  accounts receivable and other **−$21,897M (46.8%)**. 2020 accounts payable +$17,480M (26.5%) sits just under.
- **Read:** Amazon's supplier float is real and large (accounts payable $121,909M at 2025-12-31 and $147,440M at 2026-06-30, and *"amounts due to
  third-party sellers"* among the restricted cash pledges), and it **releases cash as sales grow**; 2020's +$17.5bn is the pandemic surge. 2021-22's receivables
  and other-assets drain is the reverse. **From 2023 the filing splits out "Other assets"** (−$12.3bn / −$14.5bn / −$15.6bn / TTM −$17.8bn),
  whose balance sheet caption includes *"video and music content, net of accumulated amortization"* and *"satellite network launch services
  deposits"*: **content and satellite prepayments are already inside OCF**, which is why no "ex-working-capital" owner-earnings figure is
  computed here (it would strip real spending along with the float).
- The increment [E2-23] is therefore included, through OCF, and the float's sign is stated: in a shrinking year the payables release reverses.

### Taxes and the marks — separated
- **The Anthropic and OpenAI marks do not reach owner earnings.** TTM *"Non-operating expense (income), net"* **−$79,818M** is removed inside
  OCF, and *"Deferred income taxes"* **+$41,441M** TTM adds back the tax booked on them, so **OCF carries neither the gain nor its deferred tax.**
  Cash taxes paid were **$6,635M TTM** against pre-tax income of $175,466M (3.8%; 7.0% of pre-tax income excluding the $80,425M of other
  income). By year: 29.8% (2023, $11.2bn of $37,557M), 17.9% (2024), 8.5% (2025, $8.3bn of $97,311M). Explained in the filing: *"reinstating
  the option to claim 100% accelerated depreciation deductions on qualified property"* (the 2025 Tax Act) and R&D expensing. **Cash taxes
  are low because the plant is being deducted as it is bought; when the spending slows, cash taxes rise. That is a Q5 sensitivity, stated,
  not stacked.**
- **Look-through [E3-04]: none added** (Q1): no undistributed investee earnings are evidenced.

### Great, good, or gruesome? **[E4-20, E4-43]**
- [ ] great · **[x] good, and on the incremental AWS capital travelling toward the boundary** · [ ] gruesome
- **Evidence:** operating income $24.9bn (2021) → $93.7bn (TTM) on total P&E, net $160.3bn → $446.0bn: **~24% pre-tax on the added plant,
  consolidated.** But the leg taking the capital earns less on it each year: **AWS operating income +$30.1bn (2023 → TTM) on segment assets
  +$241.6bn (108,533 → 350,170) = ~12.5% pre-tax on the increment**, against 25.0% on the 2023 base; net sales per dollar of average AWS
  P&E 1.17× → 0.65×. **[E4-43]'s good class passes** (*"nothing shabby"* about a reasonable return on added capital), and the gruesome test
  *"unless the cash they consume gets to earn a reasonable return"* is not met today. **But the direction is toward it**, and the two largest
  new AWS commitments are from customers Amazon funds (below).

### Staying power — score all three **[E5-11]**
- **(1) a large and reliable stream of earnings — LARGE, NOT RELIABLE AS OWNER EARNINGS.** OCF $161.4bn TTM and rising every year since 2022.
  Owner earnings: see the band; negative on every capex construction over five years.
- **(2) massive liquid assets — YES, AND ALREADY SPOKEN FOR.** *"cash, cash equivalents, and marketable securities ... were $123.0 billion as of
  December 31, 2025 and June 30, 2026"* (10-Q MD&A). **After the quarter, $21.3bn went to OpenAI.** Revolvers ($20.0bn), commercial paper
  ($30.0bn programs) and the $17.5bn delayed-draw term loan are undrawn and **not counted** [E5-39].
- **(3) no significant near-term cash requirements — NO.** 10-Q Note 4: **total commitments $650,034M at 2026-06-30, up from $439,661M at
  2025-12-31 (+$210bn in six months)**; $42,752M due in H2 2026 and $78,084M in 2027; **leases not yet commenced $137,214M** (from $96,373M);
  **unconditional purchase obligations $130,065M** (from $84,772M), of which $33,026M in 2027. Beyond the table: the Anthropic facility of up
  to **$15.0bn** available *"as we reach certain delivery milestones of compute capacity"*; the Globalstar consideration (up to ~$4.6bn cash at
  today's price, plus the Apple redemption, amount not stated); capex running at $173.0bn TTM that the filing calls investment in AI.
- **Score: 1.5 of 3.**
- **Leverage, named and quantified [E4-16, E3-29]:** face value of long-term debt **$68,836M → $132,995M in six months** (10-Q Note 5,
  including March, May and June 2026 issues in dollars, euros, Swiss francs and Canadian dollars), plus a £ offering on 2026-09-11
  (424B5 `0001104659-26-107122`: *"The net proceeds from the sale of the notes are estimated to be approximately £4.231 billion"*); finance
  lease liabilities $13,451M; financing obligations $11,070M gross; operating lease liabilities $96,320M. Equity $551,620M, of which
  **~$219bn is the carrying value of two private AI laboratories** (Q1 table) and $66,287M is AOCI.
- **Coverage [E2-54]:** interest expense TTM $3,331M (FY2025 2,274 − H1 2025 1,057 + H1 2026 2,114), cash interest on debt $1,709M TTM.
  **Against OCF: ~48×. Against OCF net of capital expenditures: not covered** — TTM free cash flow as Amazon defines it is **−$7,604M**
  (release: *"Free cash flow decreased to an outflow of $7.6 billion for the trailing twelve months"*). [E2-54]'s test (*"comfortably met out
  of current cash flow net of ample capital expenditures"*) **is failed on the TTM**, with the caveat that most of that capex is growth. The
  gap is being filled with debt: $64bn of notes in six months.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40, E4-51]**
**The mechanism — THE ROUND TRIP** *(a proposed eighteenth shape; argued against the index below).* **Amazon finances its largest cloud
customers, books their multi-year commitments as backlog, marks its stakes in them up at the funding rounds its own cash joins, and borrows to
build the capacity they have committed to buy.** The revenue, the backlog, the capex and a large part of the equity rest on the same few
counterparties' continuing ability to raise money. The business does not die; **the owner's return on the AI plant dies** if the
counterparties stop being funded, and the retail cash that would otherwise reach owners is spent carrying the plant.

**Exposure, from the filing, not experience [E4-40]:**
- **Backlog:** *"For contracts with original terms that exceed one year, those commitments not yet recognized were approximately $496 billion
  as of June 30, 2026. The weighted-average remaining life of our long-term contracts is 6.4 years"*, against **~$244bn and 4.1 years at
  2025-12-31**. In the same six months: *"AWS and OpenAI Group PBC ("OpenAI") announced an expansion of the existing $38.0 billion multi-year
  commitment ... by $100.0 billion over 8.0 years"* and *"AWS and Anthropic announced an expansion ... by more than $100.0 billion over 10.0
  years"*. **At least $200bn of the ~$252bn increase is commitments from the two companies whose equity Amazon holds.**
- **Funding of the same counterparties:** $50.0bn of OpenAI Series C in 2026 (8-K 2026-02-27; *"Subsequent to June 30, 2026, we invested the
  remaining $21.3 billion"*); Anthropic $8.0bn of notes (2023-25), $5.0bn Series G and $5.0bn Series H in Q2 2026, and a facility of up to
  $15.0bn more tied to *"delivery milestones of compute capacity"* — **Amazon's money is paid in as the lab takes delivery of Amazon's
  capacity.**
- **The marks:** Anthropic preferred and notes $190.4bn and OpenAI $28.7bn at 2026-06-30 (+$21.3bn funded after), **~$240bn against equity of
  $551.6bn**; upward adjustments *"to reflect observable changes in price related to Anthropic's fundings"* of $62.8bn in H1 2026, in a
  quarter in which Amazon itself bought Series H.
- **The plant:** AWS P&E, net $263.8bn (from $72.7bn at 2023-12-31); AWS net additions $90.1bn in H1 2026; servers on five-year lives.

**Quantified, from filed figures (my arithmetic):**
- **If the two laboratories stop being funded:** (a) the ~$240bn of carrying value (including the $21.3bn funded after June 30) is at risk of write-down (non-cash, but ~43% of the
  June 30 book equity);
  (b) commitments of ~$238bn+ (OpenAI $138bn; Anthropic "more than $100.0 billion" plus the unstated base) stand against counterparties
  without the means to pay; (c) the capacity built for them (a share of the $90bn of H1 2026 AWS additions not stated in the filing) earns
  nothing until re-let, **in a market where Microsoft, Alphabet and Oracle have added the same capacity** (Table A: 3.4-9.0× depreciation).
  AWS TTM operating income $54.7bn is 58% of the total; **every $10bn of AWS revenue lost at the 36.8% segment margin is ~$3.7bn of operating
  income**, and depreciation on the idle plant keeps running (AWS D&A $15.4bn in H1 2026, annualising ~$31bn).
- **What survives it:** North America and International TTM operating income $39.0bn; OCF before AWS capex remains large; $123.0bn of liquidity
  (less $21.3bn); debt maturities of $14.1bn (2027) and $17.1bn (2028) including interest. **The company survives. The five-year owner
  earnings, already negative on every capex construction, stay negative for as long as the plant is carried.**
- **Likelihood:** the erosion (backlog concentrated on funded counterparties, marks rising with rounds Amazon joins, capex outrunning OCF and
  filled with debt) is **not a possibility but the filed present**. The death (the two laboratories unable to raise money, commitments
  unpaid, marks written down, plant idle into a four-way glut) is **a real possibility**: no document states the laboratories' own finances,
  and **[E4-40]** forbids reading the last three years of their fundraising as the guide.

**Against the index (17 shapes, five proposed, as read at 2026-09-13 after the ABNB fold):**
- **#1 CONTRACTED NOT TO STOP (ORCL)** is the nearest and is carried beside it: Amazon's $650bn of commitments and $137bn of leases not yet commenced
  are that shape. **The difference is the other side of the ledger**: Oracle contracted to supply OpenAI; Amazon also **owns and funds** its
  largest customers and books gains on them, so the customer's solvency, the vendor's backlog and the vendor's equity are one variable.
- **#8 THE EQUITY IS THE REVENUE (RGTI)**: customers pay a small part and new shareholders pay the rest. Close in kind; at Rigetti the subject's
  own shareholders fund the subject. **Here the customer's shareholders fund the customer, and the vendor is one of them.**
- **#11 THE PASS-THROUGH (TM)**: AWS's thirteen filed years of *"partially offset by pricing changes"* are that shape's mechanism, and it is
  recorded as a later instance.
- **#10 THE CAMOUFLAGE (SONY)**: retail cash recycled into the AWS race; true of the flow, but the retail leg is not re-winning a race each
  cycle in the filing's own words, and the camouflage is not the death.
- **Proposed as the eighteenth shape, THE ROUND TRIP**, pending the operator like #13-#17. Later instances likely on the same evidence at ORCL
  (as supplier) and MSFT (as investor and supplier); not asserted for either here.

- **VERDICT (RECORDED, NOT GOVERNING): [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [x] UNKNOWABLE**
  *Can I name the document that would resolve it? **No.** The (c) judgment turns on how much of $173bn a year of plant is needed to hold AWS's
  position in a four-way race, and no filing separates maintenance from growth; the counterparties' ability to pay turns on two private
  companies' future fundraising, which no document states. **The band changes the sign of owner earnings** (−$14.8bn to +$27.6bn on the
  five-year default; −$60.7bn to +$77.4bn TTM, the INVALID D&A end excluded) and [E4-25] says a range that wide is the conclusion. The company
  survives on any reading ([E5-11] 1.5 of 3); **what cannot be known is whether owners are earning anything on it.** Not a finding against the
  business, and not what closed this file.*

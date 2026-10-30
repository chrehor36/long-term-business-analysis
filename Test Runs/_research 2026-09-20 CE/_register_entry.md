- **CE (Celanese Corporation), 2026-09-20 - FAIL at Q2 (OUT, ON THE BUSINESS).**
  Q1 IN. **WAVE 7, name 10. Register entry 142** (re-derived by counting the register itself
  with a line-start regex `^- \*\*` inside the slice from this file's `## COMPLETED FROM THE
  QUEUE` **heading line** to `## THE WRITE-EARLY PROTOCOL`: **141 entries stood above this
  one**, which agrees with the BRBR entry directly below claiming 141). **Price US$45.41**,
  close of 2026-09-18, aggregator (Yahoo Finance chart endpoint), flagged, raw response on
  disk at `_research 2026-09-20 CE/quote_CE_raw.json`. **Shares 109,748,926**, from the
  **cover of the 10-Q for the quarter ended 2026-06-30, accession `0001306830-26-000117`,
  filed 2026-08-05**, as of 2026-08-03. **One class of stock only** (Section 12(b) registers
  Common Stock, $0.0001 par, plus **four series of senior notes**, CE/27, CE/28, CE/29A and
  CE/31, which are debt and not a second equity class). No splits since the 2005 IPO.
  **Cap re-struck by hand: US$4,984M**, against the screen row's $4,861M, which is the same
  number at a slightly staler quote ($44.29). **Sovereign 5.34%, 09/18/2026, US Treasury
  daily par yield curve, 30-year, from the issuing authority, struck fresh in this run with
  `tools/sources.py`** -- and the currency choice is argued, not assumed: only **30.4%** of
  FY2025 net sales go to North America (Europe and Africa 32.1%, Asia-Pacific 35.2%), so USD
  is chosen because the filer reports and is quoted in USD, because acetyls price globally,
  and because USD at 5.34% is the **highest** of the three sovereigns and therefore the
  conservative choice.
  **FIVE STEP-0 FLAGS RESOLVED BEFORE Q1 OPENED, THREE OF THEM AGAINST THE SCREEN.**
  (i) `cap_flag` "cap $4,861M against a filed float of $6,048M (1.24x) as of 2025-06-30":
  **NEITHER NUMBER IS WRONG.** The FY2025 10-K cover (accession `0001306830-26-000031`) says
  the float *"as of June 30, 2025 ... was $ 6,048,316,998 "*; CE closed at **$55.33** that
  day and $6,048,316,998 / $55.33 = **109,313,701 shares**, against roughly 109.4M then
  outstanding -- so non-affiliates hold essentially all of the stock, the float IS the cap,
  and the 1.24x is the price change (55.33/45.41 = 1.218). The CALM/EMBC branch, not MCFT.
  What the flag really reports is an **18% fall in fourteen months inside a 74% fall in
  thirty** ($171.86 in 2024-03 to $45.41).
  (ii) `acq_note` "**NET CASH INFLOW** on the acquisition line ($11,783M, 242% of cap) - cash
  acquired exceeded cash paid": **WRONG IN SIGN, IN YEAR AND IN MECHANISM, and the arithmetic
  that made it is recoverable.** 10,589 + 1,142 + 52 = **11,783 exactly**: the screen summed
  three consecutive years of `PaymentsToAcquireBusinessesNetOfCashAcquired` on **absolute**
  values and took the sign of the smallest of the three. The filed FY2022 Consolidated
  Statements of Cash Flows (10-K accession `0001306830-23-000023`) reads *"Acquisitions, net
  of cash acquired | ( 10,589 )"* -- an **OUTFLOW**, the DuPont Mobility & Materials purchase
  closed 2022-11-01 -- preceded by **$1,142M outflow** for Santoprene in 2021 and followed by
  a **+$52M** post-closing settlement in 2023. **Celanese paid $11.7bn; it did not receive
  it.**
  (iii) `deal_note` "1 8-K Item 1.01 ... most likely a credit facility or offering; **open
  them only if something else is odd**": it is a credit facility **and it is the loudest
  document in the file**. 8-K of 2026-08-04 for an event of 2026-07-31, accession
  `0001104659-26-090359`: *"The Amendment (i) **increases the consolidated net leverage ratio
  financial covenant level** ... from the fiscal quarter ending March 31, 2027 through the
  maturity date to initially **5.50:1.00**"*. **The brief's instruction not to open it is
  recorded as a brief defect** -- the CGNX error in a new place. Liveness confirmed on four
  marks; the **Form 25-NSE of 2026-06-25** is **not** an equity delisting but the removal of
  the redeemed 4.777% notes (8-K of 2026-06-10, accession `0001104659-26-072110`).
  (iv) `spread_caveat` / `years_filed = 19`: the window was **rebuilt to nineteen years,
  FY2007-FY2025**, from the ten 10-Ks that carry them at the newest vintage. SBC is untagged
  before FY2012 (a source limit, not a zero), and **the perimeter moved twice** -- Santoprene
  2021, M&M 2022 -- plus a FY2023 disposal ($480M proceeds, $505M gain) sitting inside the
  highest operating-cash year in the table. Both `name_change_note` and `wc_note` were empty,
  and empty was an absence of a finding, not a finding of absence.
  (v) **A flag the screen does not carry:** net debt **$10,643M** at 2026-06-30 against a
  $4,984M cap, interest expense **$701M** in FY2025 and **$369M in H1 2026 alone**.
  **THE CLOSE, AT Q2.** **[E3-03] criterion 2 fails in both segments on the filer's own
  published decomposition of net sales into volume, price and currency.** Engineered
  Materials -- the half that is supposed to be differentiated -- **cut price in three
  consecutive years (-1%, -3%, -1%) while volume fell in three consecutive years (-5%, -4%,
  -3%)**, the 10-K naming the cause as *"competitive market dynamics"*; **[E4-55]**'s
  physical series and **[E4-37]**'s inverse pricing metric both read the same way, and
  **[E3-33]**'s untapped pricing power answers itself. The Acetyl Chain is **[E2-58]**'s
  commodity case in the filer's own words -- *"an environment with greater supply than
  demand"*, printed in two successive 10-Ks -- with price **-17%, -6%, -6% and then +18% in a
  single quarter**.
  **THE COMPETITOR ROW, and it is where the verdict actually rests.** Seven SEC registrants
  (EMN, DOW, LYB, WLK, HUN, AVNT, DD), one metric (**EBIT = pretax income + interest expense,
  over capital employed = total assets less current liabilities**), one window (FY2018-FY2025),
  each figure from the named filer's own 10-K XBRL at the newest vintage. The industry census
  is taken from **Eastman's own FY2025 10-K (accession `0000915389-26-000013`)**, which names
  Celanese three times and prints the producer list for acetic acid and derivatives
  (*"Lyondell Bassell, BASF SE, Dow Inc., OXEA, Celanese Corporation, Lonza, Ineos Group
  Holdings S.A"*) and for acetate tow (*"Celanese Corporation, Cerdia International, Daicel
  Corporation, Jinan Acetate Chemical"*). **Celanese's eight-year mean ROCE is 12.4%, second
  of eight. Its FY2023-FY2025 mean is 1.2%, SIXTH of eight**, behind Eastman (5.7%),
  LyondellBasell (4.2%), Avient (2.0%), Dow (1.6%) and DuPont (1.5%). Adding back the filed
  impairments ($1,639M in 2024, $1,513M in 2025) and stripping the 2023 disposal gain leaves
  **6.1%, 6.8%, 5.5% -- a three-year mean of 6.1%, still only the peer median.** So the one
  escape **[E2-58]** allows, *"a cost advantage that is both wide and sustainable"*, is **wide
  but not sustained**, and that is a RELATIVE finding and therefore not the category downturn
  (the SMPL distinction, applied). On **[E2-43]**'s denominator the plants earn **9.3%** and
  the capital actually committed earns **5.5%**, the gap being the $7,355M goodwill-and-
  intangibles wedge from a purchase already written down by **$2.7bn of goodwill and $463M of
  trade names, primarily Zytel**.
  **RECORDED BELOW THE CLOSE, WITHOUT VERDICTS.** **[E2-49] metric-switching fires with a
  dated quotation**: the DEF 14A of 2023-03-09 (accession `0001306830-23-000047`) says *"Use
  of Adjusted EBITDA as the primary financial metric (in lieu of Adjusted EBIT)"* and *"For
  the 2023 Annual Incentive Plan, these metrics were replaced with Adjusted EBITDA and Free
  Cash Flow"* -- **the first plan year after the acquisition that took D&A from $462M to
  $801M** (seventh fire of this prior, against five failures). **[E4-29] fires at full
  strength** in the 8-K EX-99.1s, where a **(8)% GAAP operating margin sits beside a 20%
  "operating EBITDA" margin in one sentence** and *"Certain Items totaling $1.6 billion"* is
  the bridge; operating EBITDA is also **the primary annual-incentive metric**. Against them:
  **no serial issuance** (108.5M to 109.7M shares, stock-plan vesting only; no equity issued
  to service the debt), a **voluntary immaterial revision** quantified line by line, and a
  goodwill note that concedes *"the projected cash flows ... had not declined"*.
  **A corporate conduct record:** a **July 2020 European Commission competition-law
  settlement** over ethylene purchasing, with *"11 new claims ... filed against Celanese and
  other ethylene purchasers in 2025 and early 2026"* -- **the second Q3 in this project to
  rest on the company's own record rather than named people's conduct, after UMC (2026-09-13),
  whose question to the operator is still open.**
  **Q4, recorded:** owner earnings **$330M to $1,000M** across two windows and three
  treatments of (c) -- a **threefold** range, which under **[E4-25]** is itself the
  conclusion. (c) is a disclosed guess at **depreciation excluding intangible amortisation
  ($620M)**, because the corpus default is wrong in both directions here: intangible
  amortisation is not a renewal cost **[E3-44]**, and **capex has run at 55% of depreciation
  and falling** ($568M → $435M → $343M → $256M annualised). Staying power fails on **[E5-11]**
  strength 3: **$7,281M of principal due inside five years** (2026 $1,204M, 2027 $1,357M,
  2028 $1,564M, 2029 $1,356M, 2030 $1,800M), a **$1.5bn-a-year receivables sale facility**
  renewed annually, **four rating downgrades in thirteen months worth 100bp of contractual
  step-ups**, and **three covenant amendments (2024, 2025, July 2026)**. **[E2-54]**'s
  coverage test, charging maintenance at depreciation rather than at the reduced spend, gives
  **1.7x on FY2025 and 0.93x on H1 2026 annualised.**
  **Q5 is headed COMPUTATION - NOT A CLEARANCE and no box is ticked.** The screen's
  `yield_bottom` of 10.71% **reproduces** ($522M at full D&A over the re-struck $4,984M gives
  10.5%), and `growth_required = -0.0071` reproduces too -- it is what a **blend of a peak
  year and a trough year** looks like divided by a price that has already fallen 74%.
  **The brief's prior that the debt destroys that yield is recorded as WRONG**: operating cash
  flow is already net of the $700M of interest, so the levered numerator belongs against the
  levered denominator and an enterprise-value yield would count the debt twice. **The debt is
  fatal at Q4, not at Q5.**
  **No band armed and no `PORTFOLIO.md` row** -- the failure is on the business (the QLYS
  ruling). The reversal condition is recorded in words in the run file: EM **volume** positive
  for four consecutive quarters, **and** Celanese back in the top two of that competitor row
  on ROCE for three consecutive years. Re-examination date: the FY2026 10-K, February 2027,
  which carries the covenant's first test at 5.50:1.00 for the quarter ending 2027-03-31.
  `Test Runs/2026-09-20 Run - CE Celanese.md`.


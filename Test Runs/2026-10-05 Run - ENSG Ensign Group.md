# Company Run — The Ensign Group, Inc. (NASDAQ: ENSG) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The blind rule of this run forbids opening `PORTFOLIO.md`,
any holding review, the session-state file, the register and the reading list, and none was opened. Whether the operator
holds ENSG is unknown to this analyst.

**Contamination declared.** Before the run, the session context showed `CLAUDE.md`, the operator protocol, the memory
index (which says, of the whole queue, "57 gate-clearers, nothing buyable") and five recent commit subjects (MBUU research
pass, a small-cap top ten). None names ENSG. No other `Test Runs/` file about ENSG was opened; whether one exists was not
searched beyond one `ls | grep -i ensg` of `Test Runs/` before the copy, which returned nothing. `tools/run.py` printed v4
material; only its arithmetic lines were read (Part VII).

**Working folder:** `Test Runs/_research 2026-10-05 ENSG/` (filings as text, the XBRL pulls, the guidance history, the
valuation script `value.py`, the ledger rows read `rows.txt`).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $173.25 (2026-10-05, aggregator quote printed by `tools/run.py`; flagged under operator rule 5, live quote
  only).
- **Shares by class** from the latest filing's cover: one class, common stock, **58,282,434** shares (10-Q for the
  quarter to 2026-06-30, filed 2026-07-27, accession `0001125376-26-000034`; `python Screens/cover_shares.py ENSG`). No
  split since the count, so the tool's share basis (58.3M) agrees.
- **Market cap:** 58.282M x $173.25 = **$10,097M**.
- **Sovereign for the earnings currency:** USD, **5.63%**, 30-year par yield, US Treasury daily par yield curve, dated
  2026-10-02 (`python tools/sources.py`).
- **Filings read** (operator rule 4):
  - 10-K for FY2025, filed 2026-02-04, accession `0001125376-26-000007` (business, risk factors, MD&A, statements, Note 18
    litigation, leases).
  - 10-Q for Q2 2026, filed 2026-07-27, accession `0001125376-26-000034` (statements, litigation note).
  - Proxy (DEF 14A) filed 2026-04-02, accession `0001125376-26-000014` (CD&A, summary compensation table, ownership,
    related persons).
  - 8-Ks: credit agreement 2026-08-19 (`0001125376-26-000038`); bylaws 2026-08-20 (`0001125376-26-000040`); buyback
    authorisations 2026-05-13 and 2026-06-12 (`0001125376-26-000029`, `0001125376-26-000031`); Q2 2026 results and press
    release (`0001125376-26-000036`, exhibit `q22026pressrelease.htm`).
  - For the ten-year record: 10-Ks for FY2016 (`0001125376-17-000013`), FY2017 (`0001125376-18-000028`), FY2019
    (`0001125376-20-000018`), FY2020 (`0001125376-21-000020`), FY2022 (`0001125376-23-000018`), FY2023
    (`0001125376-24-000018`); every earnings press release from February 2019 to July 2026 (the guidance history, Q4 below).
  - Competitors: NHC 10-K FY2025 XBRL (`0001437749-26-005910`); Pennant XBRL (`0001766400-26-000014`); Genesis Healthcare
    XBRL to FY2020 (`0001558370-21-003091`); Omega Healthcare Investors 10-K FY2025 (`0000888491-26-000008`); Sabra 10-K
    FY2025 (`0001492298-26-000008`, read for tenant coverage, none found in a usable form).
- **One figure cross-checked against the filed statement:** the tool's 2025 equity of 2,232 against the filed balance
  sheet's "Total Ensign Group, Inc. stockholders' equity | 2,231,725" (thousands): agrees. Cash 504 against 503,881: agrees.
- `python tools/run.py ENSG` arithmetic lines: **defective for this name.** Its owner-earnings table stops at 2019 because
  the filer's capital-spending tag changed after 2019; its five-year window is therefore 2015-2019 and useless. Its debt
  column is non-current debt only. The ten-year balance-sheet table was used and checked against the filed statements.
  Owner cash below is built from the filed cash-flow statements:

  | $M | 2021 | 2022 | 2023 | 2024 | 2025 | five-year average |
  |---|---|---|---|---|---|---|
  | Operating cash flow (filed) | 275.7 | 272.5 | 376.7 | 347.2 | 564.3 | |
  | less stock pay (filed, added back in OCF) | 18.7 | 22.7 | 30.8 | 36.2 | 48.3 | |
  | less purchase of property and equipment | 69.6 | 87.5 | 106.2 | 158.2 | 193.6 | |
  | **A. owner cash after all capex** | **187.5** | **162.2** | **239.7** | **152.7** | **322.4** | **212.9** |
  | less cash paid for acquisitions (business and asset) | 104.2 | 101.1 | 69.0 | 156.5 | 323.3 | |
  | **B. owner cash after all capital spending incl. acquisitions** | 83.2 | 61.1 | 170.7 | -3.8 | -0.8 | **62.1** |
  | Depreciation variant: OCF less stock pay less D&A | 201.0 | 187.4 | 273.5 | 226.8 | 411.6 | 260.1 |

  Sources: cash-flow statements in the FY2025 10-K (2023-2025) and FY2022 10-K (2021-2022). The first half of 2026 (10-Q):
  OCF 272.1, stock pay 30.1, capex 88.3, acquisitions **376.0**; cash fell from 503.9 to 262.3. 2025 OCF was helped by
  working capital (accrued wages +82.8, other accrued +41.7, self-insurance +35.3), which the five-year average dampens.
  The acquisitions are the capital outlay the tool's owner-earnings arithmetic misses; they are the growth capital of
  this business, 2021-2025 total 754.1 against 1,064.5 of owner cash A.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own this if the market closed for five years
**[M1997-109]**, and the answer turns on government reimbursement, labour and acquisitions, not on the quotation. The
market serves: the price tells nothing about value **[M2006-077]**. Margin of safety: "if you have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**. No macro enters: the One Big Beautiful Bill, the
staffing rule and state budgets are read here only as facts about this business's payers, not as forecasts
**[M2000-094]**. Who is paid to tell you: the press releases are the company's, and their headline figure is the company's
adjusted one (Q4). The analyst's habits: look for "what’s wrong in things" **[M2025-013]**; scuttlebutt is to "possibly reject your original hypothesis" **[M1998-144]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. Payers. Medicare and Medicaid were 69.5% of 2025 service revenue (FY2025 10-K, revenue by payor); Medicaid is 59.0% of
   skilled nursing days. The price is set by governments, not by Ensign.
2. Labour. "approximately 60.0% of our total expenses were payroll related" (FY2025 10-K, Human Capital); state minimum
   staffing ratios limit cutting staff.
3. Government claims. A $48.0M settlement with the DOJ in October 2013 over Medicare rehabilitation claims, with a
   five-year Corporate Integrity Agreement (FY2016 10-K, `0001125376-17-000013`); a qui tam over medical-director
   relationships (CID of 2018, DOJ declined to intervene in 2020) settled in 2024 for **$48.0M** (FY2025 10-K, Note 18); a
   **new DOJ CID received January 2024**, open, covering 2016 to the present, investigating whether "claims have been submitted to Medicare and Texas Medicaid for services which were unnecessary or otherwise not consistent with existing reimbursement requirements" (FY2025 10-K; repeated in the Q2 2026 10-Q). 18 subsidiaries had multi-claim Medicare or
   Medicaid reviews scheduled or in process (10-Q).
4. Earnings presentation. Every earnings release leads with GAAP and adjusted EPS side by side; adjusted net income and
   the guidance exclude stock-based compensation; guidance was raised in every year 2019-2026 and met or beaten in every
   year 2020-2025 (Q4).
5. Capital. Acquisitions consumed 71% of owner cash A over 2021-2025; in 2024 and 2025 owner cash after acquisitions was
   negative; in the first half of 2026 acquisitions (376.0) exceeded owner cash A for the full year 2025.
6. Leases. 253 of 373 facilities are leased; lease liabilities $2,064M at 2025 year-end; 104 operations sit under eight
   CareTrust master leases and another 104 under 19 other master leases, where "a default at a single facility could subject one or more of the other independent subsidiaries covered by the same master lease to the same default risk. Failure to comply with Medicare and Medicaid provider requirements is a default under several of our leases" (FY2025
   10-K, risk factors).
7. Pay. The executive bonus pool is 15% of adjusted pre-tax earnings above $199M with no charge for capital; the 2025 pool
   was $49.9M (proxy).

## THE STANDING RULE
Owning ENSG for cash, unlevered, at a size the buyer can hold through a fall of half, puts no risk of ruin on the buyer:
"borrowed money has no place in the investor's tool kit" **[L2014-005]**; the rule binds the buyer's conduct, not the
target's **[M2012-081]**. The target's own debt and leases are Q9's (NOT REACHED).

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**; the first step is "trying to identify the key variables in that particular business, and evaluating how predictable they were" **[M1998-044]**.
- **The business, from the 10-K.** 373 skilled nursing and senior living facilities in 17 states (37,911 operational
  skilled beds, 3,402 senior living units), 253 leased and 120 owned and operated, plus 38 owned properties leased to
  other operators through the captive REIT Standard Bearer (formed January 2022). The model: buy underperforming
  facilities ("some facilities having had occupancy rates as low as 30% at the time of acquisition"), put a locally
  trained administrator in charge, raise occupancy and skilled mix. Home health, hospice and most senior living were spun
  off as Pennant on 2019-10-01 (FY2019 10-K); the owned real estate was spun off as CareTrust REIT in 2014, from which
  Ensign now leases 104 operations and is buying some back.
- **The key variables and how predictable they are.**
  1. Occupancy (total, operational beds; ten 10-Ks): 2015 77.6%, 2016 75.4%, 2017 75.4%, 2018 77.4%, 2019 79.2%, 2020
     73.5%, 2021 72.8%, 2022 75.3%, 2023 78.5%, 2024 80.5%, 2025 82.2%. Same Facility 82.9% in 2025, 84.1% in Q2 2026.
     Demand is driven by an ageing population and hospital discharges: slow, foreseeable in direction.
  2. Skilled mix by days: 2015 30.4%, 2016 30.9%, 2017 30.3%, 2018 29.5%, 2019 29.0%, 2020 31.7%, 2021 31.7%, 2022 31.8%,
     2023 30.4%, 2024 29.9%, 2025 30.7%. Flat for a decade: the acuity story has not moved the mix.
  3. Government rates against wages. Medicare 23.7% and Medicaid (with Medicaid-skilled) 45.8% of 2025 service revenue;
     payroll 60% of expenses. The level of rates over ten years is political (the OBBB's provider-tax and
     state-directed-payment changes from 2028; the CMS staffing rule issued April 2024 and repealed 2025-12-02; Medicare
     sequestration). Its direction over 25 years has let the better operators earn a thin margin and the worse ones fail
     (Q2).
  4. Acquisition supply and price: the release of 2026-07-27 names "larger portfolios, landlords looking to replace current tenants, non-profits looking to divest". Foreseeable while weak operators keep failing.
- **Routing.** Not a fast-changing technology; no financial book; one business plus a captive landlord, read by its
  parts (the REIT segment earned $37.6M of $456.7M segment income in 2025).
- **The doubt, stated.** Variable 3 is important, and its level is not knowable ten years out **[M2006-076]**. The rows do
  not put a government-priced business outside the circle for that reason: they bet that regulators "will treat us fairly in the future" **[M2014-087]** and price the rest, "If a thing is cheap enough, obviously you can afford a little more country risk, or regulatory risk, or whatever." **[M2004-083]**; against that, "it is difficult to project both earnings and asset values in what was once regarded as among the most stable industries in America" **[L2023-011]**. My reading:
  I know the economics and how "far off we can be" **[M2011-084]** on the rate variable (a range, carried into Q2's threat
  test and Q7's width), not whether the business can be foreseen at all. The insiders would write the ten-year forecast
  down in direction (more patients, Ensign gaining share from weak operators), not in margin **[M2000-105]**.
- **VERDICT: IN.** The economics and Ensign's place in them can be foreseen in direction **[M2012-065]**, **[M2000-037]**;
  the rate variable is carried forward as a range, not a reason to stop. Contrary note kept: "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**; my doubt is about the level of one variable,
  not about the circle, and a reader who weighs it as a doubt about the circle would close this file here TOO HARD
  (NATURE).

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years from now." **[M1995-038]**

- **The field is commodity-priced.** Medicaid and Medicare pay every facility in a state the same schedule, adjusted for
  acuity; Ensign cannot raise prices, so the pricing-power test **[M2005-020]** has no positive answer and the only castle
  the rows allow in such a field is the low-cost operator: "Another way to prosper in a commodity-type business is to be the low-cost operator." **[L2004-007]**; "being the low-cost producer is all-important" **[L2000-017]**.
- **The competitor row** (operating income over revenue, from each filer's own XBRL; "before rent" adds back lease cost,
  used only to compare an operator that leases most of its buildings with one that owns them, never as earnings):

  | | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | ten-year mean |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | ENSG operating margin | 5.6 | 2.7 | 4.8 | 6.3 | 9.3 | 9.9 | 9.8 | 6.8 | 8.4 | 8.4 | **7.2** |
  | NHC operating margin | 6.6 | 5.6 | 5.7 | 4.9 | 4.7 | 4.7 | 2.9 | 5.0 | 6.9 | 8.5 | **5.6** |
  | ENSG before lease cost | | | | 13.2 | 15.3 | 15.8 | 15.5 | 12.7 | 14.1 | 13.7 | |
  | NHC before lease cost | | | | 8.5 | 8.2 | 8.1 | 6.3 | 8.1 | 9.6 | 10.9 | |

  ENSG figures before 2019 mix pre-spin and restated years (2016 includes what became Pennant; 2017-2018 are restated to
  continuing operations), so the first three columns are not like for like. ENSG trailed NHC in 2016-2018 and matched it in
  2025 on the plain margin; before lease cost it led in every year read, by 3 to 9 points. Return on average equity,
  ENSG against NHC: 2021 21.2% / 16.3%, 2022 19.8% / 2.5%, 2023 15.3% / 7.5%, 2024 17.9% / 10.8%, 2025 16.9% / 11.7% (ENSG's
  is flattered by lease leverage; NHC carries large investment securities).
  **Genesis Healthcare**, once the largest operator (revenue $5.6B in 2015): pre-tax loss in every year 2013-2018 and 2020,
  stockholders' equity negative from 2014 (-$1,339M in 2018), and Chapter 11 in July 2025 (Omega 10-K FY2025, which also
  records LaVie's Chapter 11 in June 2024 and three operators placed on a cash basis in 2025). **Pennant** (home health and
  hospice, Ensign's 2019 spin): operating margin 2017 6.1% to 2025 5.5%, a different business, shown for the family
  resemblance only.
- **The castle tests.**
  1. *Key factors, and how permanent* **[M1995-038]**: local leadership (CEO-in-Training, 70 to 80 administrators in
     training), clinical reputation with hospital referrers, a cluster structure that shares data, a captive insurer, and
     a 20-year record of turning facilities. Same Facility occupancy rose 2.0 points in 2025 and 2.7 points in Q2 2026 at
     mature buildings: share taken from local rivals.
  2. *Without the lord* **[L2007-006]**, **[M1996-037]**: the castle is a culture, and a culture is the one moat the rows
     admit that is made of people: "we have a culture and a business model, which people are going to find very, very difficult to copy, even semi-copy" **[M2009-038]**. Test: the founder CEO handed over in May 2019 and the founder
     chairman retired 2025-09-01; occupancy, margin and returns rose after both. Evidence for.
  3. *Money test* **[M2011-015]**: money has bought scale in this field many times (Genesis, LaVie, the private-equity
     tenants of the REITs) and has not bought Ensign's results. Evidence for.
  4. *Low bid* **[M2017-009]**: the payer's price is fixed, so referrers and families choose on reputation and star
     ratings, not on price; the company reports Same Facilities' CMS quality measures 23% better than state peers and no
     Special Focus Facility among 398 (release of 2026-07-27, company's claim from CMS data, not verified here).
  5. *Low cost* **[L1997-021]**: "a tough market helps the low-cost operator". The REIT tenants failing while Ensign buys
     their buildings is the tough market doing that.
  6. *Widening or narrowing* **[L2005-010]**: occupancy widening since 2021; skilled mix flat for ten years; margin back
     to 2020-2022 levels after the 2023 settlement year.
  7. *What could destroy it, five to fifteen years out* **[M2000-014]**: a cut in government rates below the cost of care
     for everyone (shared by all, survived best by the low-cost operator); wage inflation ahead of rates (payroll 60%;
     "we like a business with low labor costs" **[M1997-111]**; the shipped-from-abroad half of **[M2007-116]** cannot
     apply to local care); home and community-based care drawing off the Medicaid long-stay patient (OBBB permits HCBS
     waivers; "slow change can be much harder to perceive" **[M2014-038]**); and, specific to Ensign, a DOJ finding that
     part of its billing was for unnecessary services, which would mean part of the margin advantage is not a cost
     advantage at all.
- **Weighing.** The evidence over the span shows the castle standing and widening on occupancy, with the advantage held
  through a change of lord. It is not shown open. The DOJ question is the one fact that could show part of it illusory; it
  is open, and on the record two settlements of $48.0M each, eleven years apart, were paid without admission. Read as a
  castle question it is a threat graded "major" but not proven; it is an integrity question first, which is Q5's.
- **VERDICT: IN.** The low-cost operator in a commodity-priced field **[L2004-007]**, **[L2000-017]**, shown on the whole
  span against NHC and Genesis, with a culture-moat that survived its founders **[M2009-038]**.
  Not "tenuous in any way" **[M2000-019]** on the evidence; the DOJ threat is carried to Q5 and Q9.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, earnings after depreciation against capital employed. 2025:
  pre-tax income 455.6 plus interest expense 8.0 less interest income 24.5 = **439.1** operating pre-tax, against capital
  employed of equity 2,234.8 plus debt 141.8 less cash 503.9 = **1,872.7**: about **23% pre-tax**. Goodwill is 98.0 and
  intangibles 6.4, so tangible capital is nearly all of it. Leases are outside the denominator because rent (lease cost
  267.9) is inside the earnings.
- **Incremental.** 2021 to 2025: operating income +164.8 (260.5 to 425.3) on capital employed up about 957 (from roughly
  916 to 1,873, filed balance sheets), about 17% pre-tax on the added balance-sheet capital, flattered by occupancy
  recovering from the 2021 trough (72.8% to 82.2%), which cannot repeat at the same pace.
- **Cash test**, cash earnings against capital spending: 2021-2025 OCF less stock pay 1,679.7 against capex plus
  acquisitions 1,369.2: **82% of cash earnings went back in**. In the first half of 2026 capital spending (464.3) exceeded
  cash earnings (242.0).
- **The grade.** "The second-best business is a business that also gives you more and more money. It takes more money, but the rate at which you invest — reinvest — the money to get that growth is a very satisfactory rate." **[M1998-081]**
  That is Ensign: growth that consumes most of the cash, at returns that look satisfactory on the record **[L2009-012]**.
  Its growth is optional (acquisitions), not compulsory, which keeps it out of the "worst business" clause of the same row.
  Against: "whether that’s good or bad depends on what we earn on that incremental $130 million over time" **[M2001-019]**,
  and the incremental return includes a recovery.
- **WEIGHS FOR**, modestly: about 23% pre-tax on capital employed and satisfactory incremental returns on optional growth
  capital **[M1998-081]**, **[L2009-012]**, with most of the cash reinvested.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, 2017 to 2025** **[M2025-032]** (the tool's table checked against the filed statements;
$M):

| year-end | assets | equity (Ensign) | cash | receivables | goodwill | LT debt | lease liabilities | retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2017 | 1,102 | 492 | 42 | 265 | 81 | 303 | off balance sheet | 265 |
| 2018 | 1,182 | 591 | 31 | 276 | 80 | 233 | off | 345 |
| 2019 | 2,362 | 654 | 59 | 309 | 54 | 325 | 1,019 | 392 |
| 2020 | 2,546 | 818 | 237 | 305 | 54 | 113 | 999 | 551 |
| 2021 | 2,851 | 1,021 | 262 | 329 | 60 | 153 | 1,109 | 734 |
| 2022 | 3,452 | 1,247 | 316 | 408 | 77 | 149 | 1,421 | 946 |
| 2023 | 4,178 | 1,492 | 510 | 485 | 77 | 146 | 1,722 | 1,143 |
| 2024 | 4,669 | 1,837 | 465 | 570 | 98 | 142 | 1,829 | 1,427 |
| 2025 | 5,463 | 2,232 | 504 | 637 | 98 | 138 | 2,064 | 1,756 |

What the figures say. Equity grew from 492 to 2,232 almost entirely by retained earnings (265 to 1,756), not by issuance
(paid-in capital 615 at 2025, built by option exercises and stock pay); goodwill stayed under 100 while revenue tripled,
because acquisitions are booked mostly as property and leases, not goodwill. Receivables fell from 16.6% of revenue (2017)
to 12.6% (2025): cash is collected, not booked ahead of it. Debt was cut after the 2019 spin (325 to 113) and is now HUD
mortgages of 138 plus an undrawn revolver raised to $800M on 2026-08-19. The step in 2019 is ASC 842 putting about $1.0B
of leases on the balance sheet; lease liabilities have since doubled to 2,064, the true leverage of the business. What
the figures do not say: accrued self-insurance liabilities (professional liability and workers' compensation) rose from
120.5 at 2020 (current 58.1 plus non-current 62.4, FY2020 10-K) to **246.4** at 2025 (81.6 plus 164.8), faster than
revenue; the self-insurance reserve is a figure management estimates. What they cannot say: what the open DOJ CID costs.

**The income account and the real costs.** Stock pay is expensed in GAAP (48.3 in 2025) and is deducted above. Depreciation
104.3 against capex 193.6 in 2025: capex runs well above depreciation because acquired buildings are renovated; the
maintenance share is not disclosed **[M2000-144]**, so both variants are shown in Step 0. GAAP net income has been below
OCF in every year 2021-2025: the cash confirms the earnings.

**The tells** **[M1995-064]** as the convention lists them:
1. **The make-the-numbers habit** **[L2002-041]**: "we become downright incredulous if they consistently reach their declared targets". The record, from every earnings release 2019-2026 (working folder):

   | year | first guidance (Feb) | last guidance | actual adjusted EPS | GAAP diluted EPS |
   |---|---|---|---|---|
   | 2020 | $2.50-2.58 | $3.04-3.12 | $3.13 | n/r |
   | 2021 | $3.44-3.56 | $3.60-3.68 | $3.64 | n/r |
   | 2022 | $4.01-4.13 | $4.10-4.18 | $4.14 | n/r |
   | 2023 | $4.60-4.74 | $4.73-4.79 | $4.77 | $3.65 |
   | 2024 | $5.29-5.47 | $5.46-5.52 | $5.50 | $5.12 |
   | 2025 | $6.16-6.34 | $6.48-6.54 | $6.57 | $5.84 |
   | 2026 | $7.41-7.61 | $7.75-7.85 (July) | | |

   Guidance raised at least once in every year 2019-2026, never cut; the actual above the top of the first range in all six
   completed years and inside or above the last range in all six. That is a habit of making declared targets.
2. **Adjusted earnings featured**, the tell of a management that "regularly attempts to wave away very real costs"
   **[L2016-006]**.
   The record: every release opens with GAAP and adjusted EPS side by side ("GAAP diluted earnings per share of $1.68 and adjusted earnings per share of $1.92", release of 2026-07-27), and the CFO's guidance statement in the same release
   says the guidance "excludes certain charges that arise outside the normal course of business, amortization of system implementation costs, acquisition related costs and share-based compensation".
   Stock pay is the cost the rows name first, "the most egregious example" **[L2015-003]**.
   In 2023 the adjusted figure ($4.77) was 31% above GAAP ($3.65), the gap including the $48M settlement of an
   alleged-kickback qui tam; telling owners to leave out a settlement when settlements recur (2013, 2024) is the
   "Don't count this" of **[L2016-007]**.

**Contrary evidence on this question, written down** **[M1997-127]**:
GAAP comes first in each headline; every adjustment is reconciled; OCF exceeds net income; and in setting its own bonus
pool management recommended that stock-based compensation ($48.3M) and the $12.0M California class settlement be charged
back, cutting adjusted EBT from 515.9 to 455.6 (proxy, CD&A), so the adjusted figure is not the one that pays them.
A management "preoccupied with accounting considerations" is "a negative" that the speakers "can’t afford to use it as a total exclusionary factor" **[M1994-018]**.
The accounts are not confusing; nothing here is hidden.

**The rule applied.** The framework's Q4 paragraph "The make-the-numbers habit, tested" (a CONVENTION) reads: "A habit of making or beating stated targets, found alone, is a weighing against and never a STOP [...] It becomes suspicion, and so the STOP above, only with a second tell from the list under The tells (reserves that move, adjusted earnings featured, prepaid or deferred accounts building, profits on both sides of a contract)". Both are present, each on the filed record
for six or more years: the habit, and adjusted earnings featured with stock pay waved away. The convention's own reason
for counting a second tell is the cockroach row: "There is seldom just one cockroach in the kitchen" **[L2002-039]**.
The speakers' instruction on suspicion is plain: "If you ever get suspicious about accounting, just go onto the next company." **[M1995-065]**
And: "we have never had any great investment results from companies whose accounting we regarded as suspect" **[M1995-063]**.

- **VERDICT on confusion: none. VERDICT on suspicion: OUT** under the two-tell convention: the make-the-numbers habit
  **[L2002-041]** plus adjusted earnings featured with stock pay excluded **[L2016-006]**, **[L2015-003]**, closing at
  **[M1995-065]**. The box is named OUT because the question was answered against the name on the evidence, not left
  unanswerable; the framework does not name the box for this STOP (see the last section). The file closes here. Nothing
  below is a clearance.

---
**Everything below this line is NOT REACHED as a judgment.** Facts already gathered are recorded so that a later reader
does not have to fetch them again; the valuation is reported at the owner's request and is headed as the protocol
requires.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.** Facts recorded, not judged: CEO Barry Port since May 2019, also Chairman since the founder's retirement
2025-09-01 (proxy); executive officers and directors own 4.0% (2,335,861 shares including 273,777 option shares; the
founder Christopher Christensen 2.0%); four relatives of officers or directors are employed (the founder's brother as Chief
Human Capital Officer, $1.46M cash in 2025; the COO's and CIO's brothers-in-law; a director's sister), each approved by the
audit committee. The DOJ record is in the contrary-evidence list above. The integrity question a reached Q5 would have to
answer is whether two $48.0M settlements and an open medical-necessity CID are the industry's weather or this company's
conduct; "If you’ve got doubts, forget it." **[M2013-088]** would govern it.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** Facts recorded: dividends $14.4M in 2025 (about 4% of net income); buybacks $20.0M in 2025 (157,000
shares, about $127 a share) and $40.0M in Q2 2026 (257,000 shares, about $156 a share), under authorisations of $40M
(2026-05-13) raised to $100M (2026-06-12) that name no price **[L2016-002]**; all acquisitions paid in cash, none in stock.
Pay: the bonus pool formula is 15% of adjusted EBT above $199M (2025 brackets start at $99M), with no charge for the
capital the acquisitions consume, against "we also both charge managers a high rate for incremental capital they employ"
**[L1994-019]**; 2025 pool $49.9M, CEO total $13.8M (bonus $10.3M cash plus $2.9M in vested stock).

## Q7 — WHAT IS IT WORTH? STOP.
**COMPUTATION — NOT A CLEARANCE.** The file closed at Q4. The figures below are arithmetic reported at the owner's
request; they carry no entry language and do not reopen the file.

- **Construction** (the Q7 CONVENTION, five-year average, growth as shown and capped, ten years then no growth, at the
  sovereign 5.63% **[L2000-021]**, **[M1996-025]**), with this run's reading confessed: *CONVENTION of this run: the base
  is owner cash A (after all capex, before acquisitions), five-year average **212.9**; the acquisitions are the growth
  capital, so the growth case deducts them at their historical share of owner cash (70.8%, 2021-2025) for the ten
  growth years.* Rationale: the framework's "all capital spending" read literally (cash B, average 62.1, growth on that
  aggregate negative) charges every growth dollar and credits none, and the depreciation variant with its own 19.6% growth
  credits growth whose capital it never charged; both are shown, neither is the base. Growth shown: owner cash A
  2021-2025 compounded **14.5%** a year (aggregate, not per share).
- **Value range:** no-growth end $3,782M = **$64.89 a share**; shown-growth end (14.5% for ten years, 70.8% of it
  reinvested, then flat) $9,463M = **$162.37 a share**. Width 2.5 to one, inside the convention's three to one, so the
  range is usable. Beside it: the depreciation variant's no-growth end, 260.1 / 5.63% = **$79.27**; cash B at no growth,
  $18.93. If the single year 2025 (322.4, with its working-capital help) replaced the average, every figure would rise by
  about half (top of range about $245).
- **Against the price $173.25:** above the top of the range. By the convention a price above the top closes OUT through
  the floor. Expected return at $173.25, from the same model: no growth **2.1%**, central case **4.2%**, shown growth
  **5.4%**, every case below the 5.63% bond and below the floor.
- **FAIR PRICE** (owner's request): the price at which the central case returns the floor of about ten percent before the
  holder's tax **[M2003-149]**, **[L2002-020]**. *CONVENTION of this run, the central case: growth 10% a year for ten
  years, half of owner cash reinvested to get it, then flat;* rationale: below the 14.5% shown because the 2021-2025
  growth includes an occupancy recovery that cannot recur, above zero because the acquisition record is real. **Fair
  price: $54.80 a share.** The floor is read as the holder's pre-tax return on owner cash that is already after corporate
  tax; the after-tax equivalent at a 21% tax rate on the holder's return is about 7.9% (the 2002 letter converts its own
  ten percent at the corporate tax of that time **[L2002-020]**). On the 2025 single-year base the fair price would be
  about $83.
- **CHEAP PRICE** (owner's request). *Rule (CONVENTION of this run): the price at which the no-growth case alone returns
  the floor, so that all growth is free and no pencil is needed* **[M2009-005]**. **Cheap price: $36.53 a share**, 44%
  below the bottom of the range.
- **VERDICT:** NOT REACHED. Reported only: the price sits above the top of the range, at 3.2 times the fair price and 4.7
  times the cheap price.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.** Reported only: every expected return computed above (2.1% to 5.4%) is below the 5.63% government bond,
the first filter **[M1997-089]**.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts recorded: debt 141.8 (HUD mortgages), revolver $800M undrawn but for letters of credit, maturity
2031-08-19, secured, priced on net debt to EBITDA; lease liabilities 2,064 under master leases that cross-default on a
single facility and default on loss of Medicare or Medicaid provider status; pre-tax earnings over interest about 57 times
in 2025 (455.6 + 8.0 over 8.0, "pre-tax earnings/interest, not EBITDA/interest" **[L2012-002]**); self-insurance reserves
246.4.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** Recorded for a later reader: care of the frail elderly paid by taxpayers is not a named business
**[M2016-064]**; the newspaper test **[M2008-011]** would be put to the 2013 and 2024 settlements and the open CID, and to
the company's claim of quality ratings above state peers.

---
## THE BOX
**OUT at Q4** (suspicion under the framework's two-tell convention: guidance made or beaten in every year 2020-2025 and
raised in every year 2019-2026, plus adjusted earnings featured that exclude stock pay), after Q1 IN and Q2 IN. Not TOO
HARD; no research pass. For the record (COMPUTATION, not reached): value range $64.89 to $162.37 a share against $173.25;
fair price $54.80; cheap price $36.53.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the copy preceded `tools/run.py` and every EDGAR request).
- [ ] Written question by question and committed after each: **not done.** The file was written after the reading, in one
      pass, and nothing was committed, on the instruction of this session ("Do not commit"). Write-early was not kept.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in that row (checked by
      script, result in the closing note); every filing fact carries its accession; no number without a filing or a
      CONVENTION label.
- [x] The order was kept; the first STOP that failed (Q4) closed the run; nothing after it is a clearance, and Q7 is
      headed COMPUTATION — NOT A CLEARANCE.
- [x] Owner cash built from the filed cash-flow statements after stock pay, capex and (in variant B) acquisitions, never
      a net-income proxy; the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as found **[M1997-127]** (seven items under the foundations, one paragraph at Q4).
- [x] No point-in-time anchor; not applicable.
- [x] Only the arithmetic lines of `tools/run.py` were used, and its owner-earnings table was found stale and replaced.
- [x] `python tools/check_framework.py` run after writing: **PASS**. A separate script
      (`_research 2026-10-05 ENSG/check_ids.py`) found no E-id, 62 v5 ids all present in the ledger, every quoted fragment
      on a line with an id present in one of that line's rows, and no em dash in this file's own prose.
- Declared: Pennant, NHC and Genesis comparisons are from XBRL, not from reading their filed statements; the Sabra and
  Omega 10-Ks were searched for tenant coverage ratios and none usable was found; the quality-rating claims are the
  company's.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **The two-tell line at Q4 decided this run, and it is too wide.** Guidance beaten plus an adjusted EPS headline
   describes a large share of US companies; the convention cannot tell a company whose cash confirms its earnings (OCF
   above net income in every year read, receivables falling against revenue, management charging stock pay back into its
   own bonus base) from one massaging numbers. The corpus rows do support suspicion here (**[L2002-041]**, **[L2016-006]**),
   and I applied the text; but the result is that a business I found IN at Q1 and Q2 closes on its press-release habits
   before its management (Q5) or its price (Q7) is judged. A case for the operator: should the second tell have to be an
   *accounting* tell visible in the statements (reserves, deferred accounts), with "adjusted earnings featured" counted
   only when the adjusted figure is what pays management?
2. **The Q4 STOP names no box.** Section I says Q4's STOP is "stated without naming the box". I wrote OUT, because the
   question was answered against the name on evidence; a reader could argue TOO HARD. The template should say.
3. **"All capital spending" is undefined for an acquirer.** For a business whose growth is bought, reading acquisitions as
   capital spending and measuring growth on the after-acquisition aggregate gives a negative growth rate and a value of $19
   a share; leaving them out credits growth whose capital is never charged. The convention needs a sentence on
   acquisitions; I confessed one.
4. **"About ten percent pre-tax" does not say whose tax.** The 2002 row converts at corporate tax; a private holder's floor
   on owner cash already after corporate tax is a different number. I stated my reading.
5. **No row on a payer that sets the price.** Q2's commodity rows were carried by analogy to a field where the government,
   not a rival, fixes the price; Q1's regulated-business rows are all about utilities, where the regulator grants a return
   on capital, which Medicaid does not. A business paid by governments for labour has no direct row in the v5 ledger
   (searches for "Medicare", "Medicaid", "nursing", "hospital" return nothing relevant; "health care|healthcare" one row).
6. **The hard sequence leaves the most important question unjudged.** For this name the open DOJ medical-necessity CID
   is the strongest evidence against, and it belongs to Q5 (integrity) and Q2 (whether the margin is real). A Q4 close means
   it is recorded but never weighed. That is the protocol working as written; it is worth the operator knowing that an OUT
   at Q4 here says nothing about whether Ensign is honest or its castle real.

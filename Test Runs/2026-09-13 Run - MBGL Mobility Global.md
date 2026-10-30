# Company Run — Mobility Global Inc. (MBGL) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

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
## STEP 0 — THE RATE, AND THE FILING

### STEP 0(a) — WHICH COMPANY. The triage label is wrong, and the run starts from zero.
- **The operator's watchlist was never saved to disk** (`Screens/WATCHLIST RUN QUEUE.md`,
  "WHAT CANNOT BE RECONCILED FROM DISK"), so **the ticker is the only evidence of what the
  operator meant.** The ticker resolves on EDGAR to exactly one registrant: **Mobility Global
  Inc., CIK 0002090312**, NYSE: MBGL, Delaware, SIC 7389, fiscal year-end 12-31, former name
  **"S&P Global Mobility Holding Co" (2025-10-23 to 2026-01-21)** (EDGAR submissions JSON, read
  2026-09-13). **This run prices the SEC registrant trading as MBGL.**
- **TRIAGE DEFECT, recorded:** the 2026-09-01 triage narrative listed MBGL among the companies
  that "file 20-F", as **Mercedes** (`Screens/2026-08-31 PREPPED READING LIST (operator lists).md`
  line 1436, *"... Stellantis, GlobalFoundries and Mercedes file **20-F, not 10-K**"*, and the same
  list in the comment at `Screens/floor_screen.py` line 154). Mercedes-Benz Group AG does not file with the SEC under
  this ticker; MBGL files **10-Q and 8-K**, and the WAVE 5 table carries it under "foreign 20-F
  filers, short XBRL history", which is also wrong. **The real skip reason is simpler: the
  registrant is ten weeks old as a public company and has filed one 10-Q; its combined
  (carve-out) history is in a Form 10 information statement, not in companyfacts annual
  facts.** Nothing about the Mercedes label carries over. The row is read as UNLABELLED.
- **BRIEF DEFECT, recorded:** the pre-check said the filed record under this CIK is "very
  short" and listed the 10-Q, two 8-Ks, Forms 3/4 and a 13G. **It omitted the Form 10-12B
  (2026-05-07, `0001104659-26-057155`), the Form 10-12B/A (2026-05-27, `0001104659-26-066592`)
  whose EX-99.1 is the 850-page Information Statement with three years of AUDITED combined
  financial statements including cash-flow statements, the S-8 (2026-07-01), the 8-K of
  2026-06-26 (Item 5.02), and three DRS filings (2025-10-23, 2026-01-21, 2026-03-25).** The
  brief then directed the run to look for the predecessor history at S&P Global and "any Form
  10"; the Form 10 is under MBGL's own CIK. The `deal_note` flag also misread the EX-2.1: it
  is a **Separation and Distribution Agreement**, not a merger agreement (Reg S-K Item
  601(b)(2) covers plans of "acquisition, reorganization, arrangement, liquidation or
  succession", which includes a spin-off). See Q1 for what closed.

### STEP 0(b) — THE RATE
**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.35 %** · date **2026-09-11** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year**, struck fresh via `tools/sources.py:sovereign('USD')` on 2026-09-13
- **USD earnings**: 2025 revenue **U.S. $1,454M of $1,750M (83.1%)**, international $296M
  (Information Statement, combined Note 8, geographic table); H1 2026 **U.S. $765M of $923M
  (82.9%)** (10-Q Note 7). Quote in USD on the NYSE. No FX, no ADR.

### STEP 0(c) — THE FILING
**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Documents read, with dates and accessions** (all saved to `Test Runs/_research 2026-09-13 MBGL/`):
  1. **Form 10-12B/A, 2026-05-27, `0001104659-26-066592`, EX-99.1 Information Statement dated
     May 27, 2026** — audited combined statements of income, balance sheets, **cash flows** and
     equity for **2025, 2024, 2023** (F-20 to F-24), notes 1-11 (basis of presentation, goodwill
     and intangibles, taxes, SBC, restructuring, segments, related parties), unaudited condensed
     combined Q1 2026/Q1 2025, pro forma statements, capitalization, MD&A, Business, Risk
     Factors, Management and CD&A. (`form10a_infostmt.txt`)
  2. **Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-07, `0002090312-26-000014`** —
     condensed combined statements, Notes 1-10 incl. Debt (Note 4), Taxes (5), Segments (7),
     Related Party (9), Subsequent Events (10); MD&A. (`10q.txt`)
  3. **8-K of 2026-07-02 (event date 2026-06-30), `0001104659-26-080006`**, Items 1.01, 2.01,
     5.01, 5.02, 5.03, 8.01, with EX-2.1 Separation and Distribution Agreement and EX-99.1 press
     release. (`8k_0702.txt`, `8k_0702_ex21.txt`, `8k_0702_ex991.txt`)
  4. **8-K of 2026-08-07, `0002090312-26-000013`**, Items 2.02/7.01, EX-99.1 earnings release and
     EX-99.2. (`8k_0807_ex991.txt`, `8k_0807_ex992.txt`)
  5. **8-K of 2026-06-26, `0001104659-26-077915`** (Item 5.02). (`8k_0626.txt`)
  6. **Schedule 13G, 2026-08-06, `0002012383-26-003227`**. (`13g.xml`)
  7. **DRS, 2025-10-23, `0001104659-25-101868`** (draft information statement, combined
     statements for 2024 and 2023 only — **no 2022 cash-flow statement was ever filed for this
     perimeter**). (`drs_2025.txt`)
  8. **Predecessor segment record at the former parent: S&P Global 10-K FY2025 (2026-02-11,
     `0000064040-26-000013`) and FY2022 (2023-02-10, `0000064040-23-000058`), and S&P Global
     10-Q Q2 2026 (2026-07-28, `0000064040-26-000045`)** — Mobility segment revenue, operating
     profit, D&A and capex; **segment lines, not cash-flow statements.**
- **Figures cross-checked against the filed statements:**
  - **2025 revenue**: Information Statement combined statement of income **$1,750M** against
    S&P Global 10-K FY2025 segment note, Mobility revenue from external customers **$1,747M**;
    2024 $1,613M vs $1,609M; 2023 $1,485M vs $1,484M. **Agree within $4M each year** (the
    perimeters differ slightly; the carve-out is not the segment).
  - **H1 2026 operating cash flow $189M** (10-Q cash-flow statement) against companyfacts
    `NetCashProvidedByUsedInOperatingActivities` 2026-01-01..06-30 **189,000,000**
    (`0002090312-26-000014`). **Agrees.**
  - **Share count 294,821,320**: 10-Q cover (*"As of July 1, 2026, there were 294,821,320 shares
    of common stock of the registrant outstanding"*) against dei
    `EntityCommonStockSharesOutstanding` 2026-07-01 **294,821,320**. **Agrees.**
- **What companyfacts holds for this CIK:** only the 10-Q (two six-month OCF and SBC facts and
  the cover count). **No annual fact exists, which is the whole reason the triage could not
  price it.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### Q1(a) — WHAT CLOSED ON 2026-07-01, WHO CONTROLS THE COMPANY, AND WHETHER ANYTHING IS PENDING
**A spin-off. Not a merger, not a sponsor sale, not a combination.** 8-K of 2026-07-02
(`0001104659-26-080006`), Item 2.01, verbatim: *"Effective as of 12:01 a.m. New York City time on
the Distribution Date, the common stock of Mobility Global was distributed, on a pro rata basis, to
S&P Global's stockholders of record as of the close of business on the Record Date. On the
Distribution Date, each of the stockholders of S&P Global received one share of Mobility Global
common stock for every share of S&P Global's common stock held by such stockholder on the Record
Date."* Item 5.01: *"Following completion of the Distribution, Mobility Global became an
independent, publicly-traded company, and S&P Global retains no ownership interest in Mobility
Global."*

- **The perimeter distributed** (Item 1.01): *"the business of S&P Global and its subsidiaries with
  respect to providing analytics, marketing, planning solutions, reports, forecasts and vehicle
  history data for the automotive sector, which operated under the S&P Global Mobility division."*
  It is S&P Global's former **Mobility segment**, which S&P Global acquired inside the **IHS Markit
  merger of 2022-02-28** (combined Note 1: *"Mobility was acquired as part of the IHS Markit Ltd
  ("IHS Markit") merger with S&P Global in February 2022"*).
- **Control now:** a widely held public company. **No holder retains a block from the separation**:
  S&P Global keeps nothing, and the distribution went pro rata to S&P Global's own dispersed
  register. The one ownership filing since is a **Schedule 13G** of 2026-08-06
  (`0002012383-26-003227`) by **BlackRock, Inc.** (reporting-person type HC, event date 07/31/2026),
  a passive-holder form (13G, not 13D); no 13D has been filed against this
  CIK (submissions index, read 2026-09-13). **The only control arrangement of substance is the Tax
  Matters Agreement** (below), which binds the company's own freedom, not a holder's.
- **The cash that went to the former parent:** 10-Q Note 4, verbatim: *"the Company used the net
  proceeds from the Senior Notes, after deducting discounts and commissions to the initial
  purchasers, to pay a $2.0 billion dividend to S&P Global as consideration for the transfer of
  certain assets, liabilities and entities to Mobility Global in connection with the Separation."*
  Net transfers to Parent in H1 2026: **$(2,011)M** (10-Q cash-flow statement).
- **The debt raised to pay it:** **$2.0bn of senior notes issued 2026-05-29** — $650M 5.050% due
  2029, $650M 5.450% due 2031, $700M 6.050% due 2036 — plus an **undrawn $500M revolver** maturing
  2031-07-01 with a **3.50x total net leverage covenant** (10-Q Note 4). Carried at Q4.
- **IS ANYTHING PENDING? No transaction to buy or sell the company is on file.** The 8-K of
  2026-07-02 carries **no Rule 425, 14a-12, 14d-2 or 13e-4 box ticked** (cover, read); the
  submissions index since 2026-07-01 holds Forms 3/4, one 13G, the 10-Q and the results 8-K — **no
  DEFM14A, PREM14A, S-4, SC TO-T, SC 14D9 or 425.** `tools/sources.py:deal_note()` fired only on the
  EX-2.1, which is the **Separation and Distribution Agreement** (exhibit index: *"Separation and
  Distribution Agreement between S&P Global Inc. and Mobility Global Inc., dated June 30, 2026"*).
  **The quote is therefore an owner-earnings price, not a deal spread** — the opposite of the
  ACVA/ROKU treatment.
- **But a would-be acquirer is legally fenced for two years.** Tax Matters Agreement (8-K Item 1.01,
  verbatim): the company may not *"cause or permit certain business combinations or transactions to
  occur during the two-year period following the Distribution Date"*, may not *"sell or otherwise
  issue Mobility Global's common stock during the two-year period ... other than pursuant to
  issuances that satisfy certain regulatory safe harbors"*, may not *"redeem or otherwise acquire
  any of Mobility Global's common stock, other than pursuant to open-market repurchases of less than
  20% ... during the two-year period"*, and *"is generally required to indemnify S&P Global against
  any and all tax-related liabilities ... to the extent caused by any action undertaken by Mobility
  Global or in respect of Mobility Global's shares."* **Window: to 2028-07-01.** This matters twice:
  it forbids serial issuance **[E5-15]** and caps buybacks for two years (Q3), and it makes a sale of
  the company before mid-2028 carry a Section 355(e) indemnity (Q6).

**THE ONGOING RELATIONSHIP WITH S&P GLOBAL, as MBGL's own documents state it** (SPGI itself is not
run here; wave 5 carries it separately):
- **Transition Services Agreement**: S&P Global provides *"information technology, finance and human
  resources, generally for a period of up to 18 months following the Distribution"*, charged at
  *"S&P Global's reasonably apportioned fully-loaded overhead"*; each side's liability capped at the
  fees paid. **Ends by about 2027-12-31.**
- **Tax Matters Agreement**: S&P Global bears pre-closing taxes on combined returns; MBGL bears
  pre-closing taxes on its separate returns, the two-year covenants above, and the 355 indemnity.
- **Employee Matters Agreement**: benefit plans split; the 401(k) moved to an MBGL plan in July 2026
  (10-Q Note 6).
- **Separation and Distribution Agreement**: *"uncapped cross-indemnities"*; **cross-licences of IP,
  non-exclusive** (*"Mobility Global also grants and receives non-exclusive licenses under certain
  intellectual property"*).
- **The related-party Canada Carfax Loan** (CAD$403M, 6.0%, $230M at 2025-12-31) was eliminated at
  separation (10-Q supplemental: *"Consolidation of Canada Carfax Loan $230"*).
- **Commercial data agreements** (Information Statement, "Commercial Arrangements"; the 8-K does not
  list them; the 10-Q names *"other commercial arrangements"*): *"(i) we will provide S&P Global with a
  non-exclusive right to use certain Mobility data products for internal business purposes and derived
  data creation across certain S&P Global business divisions and (ii) S&P Global ... will provide us
  with a non-exclusive right to use certain S&P Global data products"*, on *"multiyear terms"* and
  *"arms-length terms"*; the company's own words: *"These agreements are not material to us."*
  *(Corrected before commit: a first draft of this line said no commercial agreement was described; the
  8-K is silent, the Information Statement is not.)*

### Q1(b) — THE BUSINESS, from the Information Statement and the 10-Q
**Two segments. Revenue and pre-amortization segment profit, 2023-2025, from the audited combined
segment note and MD&A** (segment operating profit is after $189-190M/yr CARFAX and $106-107M/yr B2B
of amortization of intangibles **acquired in the IHS Markit purchase accounting**; the corpus says
*"amortization charges should be ignored"* when judging the operation **[E2-43]**, so both are shown):

| $M | 2023 | 2024 | 2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|
| **CARFAX revenue** | 928 | 1,039 | 1,142 | 564 | 610 |
| — subscription / non-subscription | 748 / 180 | 843 / 196 | 927 / 215 | 459 / 105 | 494 / 116 |
| CARFAX segment op. profit (GAAP) | 210 | 259 | 322 | 166 | 190 |
| CARFAX op. profit **before acquired amortization** | 400 (43.1%) | 449 (43.2%) | 511 (44.7%) | 261 | 285 |
| **B2B revenue** | 557 | 574 | 608 | 295 | 313 |
| — subscription / non-subscription | 422 / 135 | 460 / 114 | 499 / 109 | 242 / 53 | 261 / 52 |
| B2B segment op. profit (GAAP) | 61 | 69 | 62 | 30 | 8 |
| B2B op. profit **before acquired amortization** | 167 (30.0%) | 176 (30.7%) | 169 (27.8%) | 83 | 61 |
| Corporate unallocated | (32) | (30) | (45) | (16) | (35) |
| **Total revenue** | **1,485** | **1,613** | **1,750** | 859 | 923 |
| Total operating profit (GAAP) | 239 | 298 | 339 | 180 | 163 |

*Sources: Information Statement MD&A "Segment Results of Operations" (CARFAX and B2B tables) and
combined statements of income; H1 from 10-Q Note 7 and the 8-K EX-99.1 Exhibit 4 (segment operating
profit table). B2B H1 2026 carries $33M of separation transaction costs (EX-99.1 Exhibit 5).*

**Unit economics, in my own words:**
- **CARFAX (65% of 2025 revenue, ~75% of pre-amortization segment profit).** CARFAX collects the
  events in a car's life — accidents from police reports, services from repair shops, title and
  ownership events, dealer sales — from **"more than 177,000 sources ... including more than 92,000
  dealers and service shops, 6,300 police agencies and 36 OEMs"**, largely on a **"give-get"**
  basis (the shop gives its service records and gets CARFAX's customer-retention tools back). It
  then sells the same compiled history over and over: **to used-car dealers by monthly subscription
  per rooftop** (Advantage: unlimited reports; Car Listings: the right to list on CARFAX's consumer
  site; CARFAX For Life: service-retention marketing to the dealer's own customers), **to lenders
  and insurers** ("BIG", usage-tiered minimums), and **to consumers per report.** The consumer brand
  is the lever on the dealer: a shopper who expects to see the CARFAX report makes the dealer pay to
  show it. Revenue driver stated by the company: *"the number of dealer locations enrolled in dealer
  subscription products ..., the average monthly price per location on each product, and the number
  of BIG customers and their average monthly price per customer."* **The cost of the next report is
  near zero; the cost of the database is paid continuously in operating expense (data acquisition,
  technology, advertising), not in capex** — 2025 capex was **$24M on $1,750M revenue (1.4%)**.
- **B2B (35% of revenue, ~25% of profit).** Three things sold to different buyers: (1) **Polk
  registration and ownership data** (sourced under the DPPA from state DMVs and industry bodies) sold
  to OEMs and dealers as market-share and loyalty reporting and as marketing audiences, plus **Recall**
  outreach billed by campaign volume; (2) **dealer software** — automotiveMastermind (predictive
  prospecting for dealers) and Market Scan (a payment and incentive calculation engine, *"priced by
  dealer rooftops"*); (3) **Strategy & Planning** — light-vehicle production, powertrain and
  supply-chain forecasts sold by subscription to OEMs, suppliers and banks. Mostly subscription
  (82% in 2025), the transactional remainder tied to OEM marketing spend and recall volume.
- **Subscription share, whole company: 79% (2023), 81% (2024), 81% (2025), 82% (H1 2026).**
  Remaining performance obligations only **$78M** at 2025-12-31 (combined Note 1) — the book is
  mostly **monthly or annual**, so "recurring" here means renewals, not a long contracted backlog.
- **Customer concentration: none material.** Combined Note 1: *"for the years ended December 31,
  2025, 2024 and 2023, no single customer accounted for more than 10% of our revenue."* Concentration
  is by **group** (dealers, OEMs), which the risk factors name.
- **Geography: U.S. 83%** (2025).

**The scarce input this business controls:** the **accumulated, contributory vehicle-event database**
(38 billion history records, 30+ years of ownership data) and the **consumer brand that makes dealers
pay to display it** (company survey: *"an average of 96% in-market awareness"* — a company-commissioned
survey, recorded as the company's claim, not as evidence). **Neither is an exclusive legal right**:
the DMV data is available to anyone who pays for it (*"Even data obtained from public sources, such
as state DMVs, presents a high barrier to entry for new competitors due to the significant cost
relative to potential monetization"* — a cost barrier, not a legal one), and some third-party data
agreements *"allow them to cancel on short notice"* (Risk Factors). Whether the scarcity is real
**relative to AutoCheck and the listing sites** is Q2's question, not Q1's.

**The perimeter is stable across the window that has cash-flow statements.** Market Scan acquired
2023-02-16 for $223M ($214M cash); Catalyst for Aftersales sold August 2023; *"In 2025 and 2024, we
did not make any material acquisitions"* (combined Note 2); none in H1 2026. A ~35% stake in New
General Company is held by CARFAX. **The business distributed on 2026-07-01 is the business the
three audited years record** — what changed is the capital structure (Q4) and the corporate cost
base (Q4).

**Will the fundamentals look broadly the same in ten years?**
- **CARFAX: broadly yes, with one named threat.** A used-car buyer's need to know a car's past does
  not go away while used cars trade hands; CARFAX revenue has risen every year of the filed record
  (+12%, +10%, +8% in H1 2026). **The named threat is the source of the history itself**: modern
  cars report their own service and crash events to the OEM, so the OEM could become the history
  vendor and the police-report/service-shop network could lose its exclusivity. The company names
  the direction without quantifying it (36 OEM CPO programs are already contributors). Recorded at
  Q2 and Q4 as exposure, not dismissed.
- **B2B: less stable.** Forecasting and dealer-marketing software sit in a fragmented market the
  company itself calls *"highly fragmented and global"* with competitors named (J.D. Power, Cox
  Automotive, Experian, GlobalData); B2B non-subscription revenue fell **$135M → $114M → $109M**
  (2023-25) on recall volume and OEM discretionary budgets.

**[E3-31] applied to this record: can future cash flows be understood from the filed record of the
business as it now stands?** Yes for the operating business: three audited years of cash-flow
statements on an unchanged perimeter, a simple repeat-sale data model, no customer above 10%, 81%
subscription. **What the filed record does NOT contain is a single day of standalone operation**:
every statement through 2026-06-30 is a carve-out with allocated corporate costs, and the company
says the stand-alone cost *"is not practicable"* to quantify. **That is a measurement question about
the owner-earnings level (Q4), not an understanding question about how the money is made** — the
distinction the HHH and RGTI closures turned on was that *the forward entity, by its own declared
program, was not the filed entity*. Here the forward entity **is** the filed entity with a new
balance sheet and its own head office. **[E4-46]:** this is not a business that needs months of
study; a vehicle-history subscription is understood in five minutes.

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *(Separating test not required on an IN. The HHH/RGTI shape was considered and rejected on the
  ground above.)*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**Judged by line, because the lines are different businesses [E5-37].** Revenue by business line, 2025
(Investor Day presentation of 2026-05-12, p.93 — furnished on EDGAR as S&P Global 8-K EX-99.1,
`0001104659-26-058908`, as page images; text read from the company's IR PDF of the same deck dated
2026-06-01, **IR rung, flagged**): **CARFAX Advantage (dealer vehicle-history subscriptions) 25% ·
CARFAX Listings 14% · CARFAX Financial/Consumer/Other 17% · CARFAX International 9% · B2B Marketing &
Sales 26% · B2B Planning 9%.** The vehicle-history report itself — Advantage plus the lender/insurer and
consumer lines — is roughly **40% of revenue**; the rest of CARFAX rides on its brand.

### (a) The vehicle-history report — the only candidate franchise in the file
- **Needed or desired [x].** 81% subscription; revenue up every filed year; the company's survey
  figure of *"~2M Number of times per month consumers walk into dealerships and say 'Show me the
  CARFAX'"* (Investor Day p.67, company data via a third-party survey, YE2024 — recorded as the
  company's claim).
- **No close substitute [ ] — CONTESTED on filed third-party evidence, and not resolvable from any
  filing:**
  - **Against: two registrants name a co-equal substitute.** ACV Auctions 10-K FY2025: *"The True360
    Reports can be used with leading vehicle history report providers, such as CarFax and AutoCheck"*.
    OPENLANE 10-K FY2025 (`0001395942-26-000006`): *"We offer access to vehicle history resources such
    as CARFAX and AutoCheck"*. `fts_count` over 10-Ks: OPENLANE names CARFAX 11 times and AutoCheck 11
    times, ACV 5 and 5 — **at wholesale the two are offered side by side.** AutoCheck belongs to
    Experian, which MBGL's own Information Statement names as a competitor.
  - **For: at retail, the registrants name CARFAX alone.** Carvana 10-K FY2025
    (`0001690820-26-000009`) lists *"Carfax"* among competing sites; Cars.com 10-K FY2025
    (`0001193125-26-076546`): *"We also compete with other automotive websites, such as CARFAX, Edmunds
    and Kelley Blue Book"*; CarGurus 10-K FY2025 names *"CARFAX.com"*. **None of those three names
    AutoCheck** (`fts_count` "AutoCheck" in 10-Ks: Carvana 0, Cars.com 0, CarGurus 0; CarMax,
    AutoNation, Lithia, Sonic, Group 1, Asbury, Penske, America's Car-Mart, Vroom, Copart, RB Global
    also 0 — a screen, not evidence, per operator rule 8; `fts_dealers.json`).
  - **For: customers once sued over the position.** IHS Markit 10-K FY2016 (`0001598014-17-000024`)
    and FY2017 (`0001598014-18-000020`): a 2013 complaint *"purportedly on behalf of certain auto and
    light truck dealers"* alleged that *"in violation of antitrust laws, CARFAX entered into exclusive
    arrangements regarding the sale of CARFAX vehicle history reports with certain auto manufacturers
    and owners of two websites providing classified listings"*, later naming *"approximately 469 auto
    dealers"*; *"On September 30, 2016, the District Court granted CARFAX's motion for summary
    judgment, dismissing all claims"*; another group of dealers filed on 2017-01-13. No instance found
    in the CARFAX passages of the FY2018-FY2021 IHS Markit 10-Ks (sweep: every "CARFAX" occurrence in
    those four vintages). As at EFX, **litigation by customers is the shadow a position casts — it shows
    the customers once thought the substitute was not close; it does not show the position is still
    there.**
  - **What would settle it — AutoCheck's scale or share — is in no filing.** Experian plc is not an SEC
    registrant; its Annual Report reports by region and business line (the EFX run's transcription of
    AR 2026: North America Business-to-Business / Financial Services / Verticals / Consumer Services),
    and **this run could not reopen that document**: experianplc.com returned an Incapsula bot-block
    page on 2026-09-13 (rung: company IR; obstacle: bot protection). I therefore do not assert that the
    AR lacks an automotive line; I record that no AutoCheck or automotive P&L was transcribed by the run
    that did read it, and that an automotive revenue share would show attacker scale, not whether
    dealers regard the two reports as substitutes.
- **Not price-regulated [x].** The DPPA governs the use of DMV data, not the price of a report.

**[E2-44] — the two-characteristic test.**
- **(1) Price rises "rather easily ... without fear of significant loss of either market share or unit
  volume": the first half is shown, the second half is not.**
  - Price is being taken. 10-Q Q2 2026 MD&A, whole company: revenue *"increased $64 million in the six
    months ended June 30, 2026 ... driven primarily by price increases of approximately $16 million and
    $36 million, respectively, and continued new business growth of approximately $8 million and $20
    million"*; CARFAX: *"primarily driven by price increases."* Information Statement, CARFAX 2025:
    +$103M, of which *"new business growth and solid underwriting volumes of $46 million and $13 million
    ... and the remaining increase driven by improved contract terms"* — about **$44M, ~4% of 2024
    CARFAX revenue**.
  - **Units are not filed as a series, and the one consumer unit given at two dates fell.** Dealer
    customers: *"more than 40,000"* in the DRS of 2025-10-23 and *"over 40,000 ... as of December 31,
    2025"* in the Form 10 — **a frozen floor**, the CTAS "more than one million businesses" absence
    pattern. **Vehicle-history report views:** DRS of 2025-10-23 (`0001104659-25-101868`): *"more than
    31 million monthly average CARFAX vehicle history report views for the twelve month period ended
    September 30, 2025"*; DRS/A of 2026-01-21 (`0001104659-26-005378`), DRS/A of 2026-03-25
    (`0001104659-26-034599`), Form 10 of 2026-05-07 (`0001104659-26-057155`) and Form 10/A of 2026-05-27:
    *"more than 28 million monthly average CARFAX vehicle history report views for the twelve-month
    period ended December 31, 2025"*; Investor Day p.67: *"28M+ ... BASED ON MONTHLY AVERAGE DEALER USAGE
    IN 2025."* Unique visitors moved from *"over 23 million"* to *"approximately 23 million"*. **Floor to
    floor, a trailing-twelve-month average cannot fall from 31M+ to 28M+ by moving the window one quarter
    unless Q4 2025 views were roughly 24-36M below Q4 2024 — or the definition changed.** No document
    says which. **[E4-55]: the physical series is the honest one, and the only one on file points down
    while dollars rise on price.** It is too thin (two floors, one quarter apart, possibly redefined) to
    convict; it is exactly the kind of fact that forbids an IN.
  - **The longer revenue record, at its honest rung.** Investor Day p.91 (S&P Global 8-K EX-99.1,
    `0001104659-26-058908`, furnished; company-compiled): revenue **$529M (2014) → $585M → $719M →
    $836M → $979M → $1,074M → $1,052M (2020) → $1,247M → $1,351M → $1,485M → $1,613M → $1,750M
    (2025)**, organic growth *"10% 11% 14% 11% 10% (2%) 18% 10% 9% 9% 9%"* against an industry series
    (FRED vehicle sales) of *"6% 0% (2%) 1% (1%) (15%) 4% (8%) 13% 2% 2%"*. The deck's own footnote:
    *"THESE NUMBERS ARE NOT PREPARED ON A CONSISTENT BASIS AND MAY NOT BE COMPARABLE PERIOD OVER
    PERIOD"* (2014-21 from IHS Markit's Transportation segment *"adjusted to exclude revenue associated
    with other businesses"*, 2022 from S&P Global's segment, 2023-25 audited carve-out). **Read for what
    it can carry: a decade of dollar growth near 10% through flat and falling vehicle volumes, and only
    −2% in 2020 against −15% for the industry — the first half of [E2-44](1) across a cycle.** It is
    revenue for the whole perimeter, not CARFAX; it carries no unit series and no comparison with
    AutoCheck, so it does not touch the two gaps that decide this gate.
- **(2) Growth "with only minor additional investment of capital": passes.** Capex $18M / $15M / $24M
  on revenue $1,485M / $1,613M / $1,750M (1.2% / 0.9% / 1.4%, combined cash-flow statements).

**[E3-46] and [E2-43] — returns on the tangible capital employed.** At 2025-12-31: total assets
$12,995M less goodwill $8,845M, other intangibles $3,789M and cash $38M leaves **$323M** of tangible
non-cash assets, against $255M of non-interest-bearing operating liabilities (payables $56M, accrued
compensation $64M, unearned revenue $78M, other current $45M, lease $11M, other $1M). **Unleveraged net
tangible assets ~$68M against 2025 operating profit before acquired amortization of $635M.** The ratio is
not meaningful because the denominator is near zero: this business runs on customers' money and the
database is expensed, not capitalised. **The second question about the business, answered as a number,
is as good as the corpus's best** — which is why this Q2 is hard rather than easy.

**[E4-04] — must the moat be continuously rebuilt?** The data estate is **defended, not replaced**
[E5-23, E3-49]: the same records accumulate. IHS Markit 10-K series, CARFAX records and sources:
*"more than 17 billion records collected from more than 100,000 data sources"* (FY2016) → 19bn /
110,000 (FY2017) → 20bn / 112,000 (FY2018) → 23bn / 112,000 (FY2019) → 25bn / 112,000 (FY2020) →
27bn / 130,000 (FY2021, `0001598014-22-000011`) → 37bn / 175,000 (DRS, 2025-09-30) → **38bn / 177,000
(Form 10, 2025-12-31)**. Brand defence is continuous too: advertising *"primarily comprised of advertising
for CARFAX"* $35.2M (FY2014) → $76.4M (FY2021) (IHS Markit 10-Ks); +$23M of *"strategic investments
including advertising and promotion costs"* in 2025 (Information Statement). **A lapse would narrow the
structure, not destroy it.** The basis-replacement risk is named at Q1: the car itself reporting its
history to its maker. **Great manager required? No** [E4-23]: CARFAX has earned these economics under
three owners (Polk, IHS/IHS Markit, S&P Global).

**[E2-45] — the attacker's test.** Experian (AutoCheck) and Cox (Autotrader, Kelley Blue Book) have
had ample capital for two decades; CARFAX's pre-amortization margin was **43.1% → 43.2% → 44.7%**
(2023-25). That is the strongest single argument for the franchise, and it is an argument from
persistence, not a measurement of the attacker.

**[E4-32] — direction. Not shown to widen.** CARFAX revenue growth **+12% (2024), +10% (2025), +8%
(H1 2026)**; the growth attribution moved toward price (above); the one unit metric fell; the margin
rose slightly. *"That does not necessarily mean that the profit is more this year than last year."*

### (b) CARFAX Listings (14%) — a follower in a crowded market
CarGurus 10-K FY2025 (`0001193125-26-059435`) lists *"major U.S. online automotive marketplaces, such as
AutoTrader.com, CARFAX.com, Cars.com, and TrueCar.com"* and claims the most-visited position against
*"CARFAX.com Listings (defined as CARFAX.com Total Visits minus Vehicle History Reports)"* (Similarweb,
Q4 2025). Cars.com names CARFAX among *"other automotive websites"*. **Criterion (2) fails for this
line on three registrants' lists.** It sells because the report is attached to every listing — the
brand's rent, not a second moat.

### (c) B2B (35%) — no franchise on its own filing
- **Criterion (2) fails on MBGL's own list:** *"Our competitors include: (i) automotive data and
  analytics providers, such as J.D. Power and Cox Automotive; (ii) data and information providers,
  such as Experian and Global Data; (iii) business intelligence and consulting firms ...; and (iv)
  smaller niche players"*, in a market it calls *"highly fragmented and global."*
- **The numbers do not show a position:** pre-amortization margin **30.0% → 30.7% → 27.8%**; revenue
  CAGR 4.5%; non-subscription **$135M → $114M → $109M**; H1 2026 growth *"primarily due to continued
  new business growth"* — no price claimed. The registration data is DMV-sourced and open to Experian
  and others (*"a high barrier to entry for new competitors due to the significant cost relative to
  potential monetization"* — a cost barrier the company states, not an exclusive right).
- **Class: NONE.**

**THE COMPETITOR ROW — required [E3-28].** Same metrics, same window (2023-2025), filing-sourced.
Operating margin is shown **before amortization of acquired intangibles** because MBGL carries $296M a
year of IHS Markit purchase-accounting amortization the operators did not choose [E2-43, E2-73]; the
peers' amortization is added back the same way. **MBGL's segment margins exclude corporate unallocated
($30-45M a year); the peers' are whole-company.**

| Company | Revenue 2025 $M | Revenue CAGR 2023-25 | Op. margin before acquired amortization 2023 / 2024 / 2025 | Capex + capitalised software, % rev 2025 | Source |
|---|---|---|---|---|---|
| **MBGL — CARFAX segment** | 1,142 | 10.9% | **43.1% / 43.2% / 44.7%** | n/a by segment | Form 10/A `0001104659-26-066592`, MD&A segment tables |
| **MBGL — B2B segment** | 608 | 4.5% | **30.0% / 30.7% / 27.8%** | n/a by segment | same |
| **MBGL — combined** | 1,750 | 8.6% | **36.0% / 36.8% / 36.3%** | 1.4% | same, combined statements |
| CarGurus (continuing ops; CarOffer discontinued) | 907.0 | 14.0% | 17.2% / 19.7% / 26.9% (acquired amortization ~$1M a year) | 3.2% ($6.4M + $22.9M) | 10-K FY2025 `0001193125-26-059435`; companyfacts cross-checked to the filed income statement |
| Cars.com | 723.2 | 2.4% | 19.3% / 18.6% / 17.0% | 3.6% ($4.3M + $21.6M) | 10-K FY2025 `0001193125-26-076546`; companyfacts, 2025 cross-checked to the filed statement |
| Experian plc (AutoCheck inside, unsegmented) | group 8,445 (FY to 2026-03-31) | — | North America Benchmark EBIT 34.2% (all NA products) — **not the same metric** | group capex 8.6% | AR 2026, IR rung, from `_research 2026-09-05 EFX/row Experian.md`; not re-read (blocked) |
| Cox Automotive (Autotrader, KBB, vAuto, Dealertrack, Manheim) | — | — | — | — | private (Cox Enterprises); no filing |
| J.D. Power · CDK Global | — | — | — | — | private; no filing |
| GlobalData plc | — | — | — | — | LSE; not an SEC registrant; not fetched |

- **Peers taken: 2 SEC filers plus 1 at the IR rung, of the ~8 real competitors the filings name**
  (AutoCheck/Experian, Cox Automotive, J.D. Power, GlobalData, CarGurus, Cars.com, TrueCar, CDK).
- **What the row shows:** CARFAX's economics sit well above both filed listing rivals and above
  Experian's regional margin; B2B sits between. **What it cannot show:** CARFAX against AutoCheck, the
  one direct substitute in the product that carries the franchise claim. **This is not the CTAS, TSCO
  or EFX case, where a private or unsegmented peer was one of several and a filed unit series carried
  the verdict.** Here the missing peer is the only direct competitor in the report, and the unit
  disclosure is a frozen dealer floor plus one consumer metric that fell. The narrow-only rule (an
  unmeasured competitor can only narrow a moat) is exactly why the gap matters: the verdict it could
  move is an IN.
- **[E3-61] limit:** the row shows position, not conduct.
- **Untapped pricing power [E3-33, E5-28]? Not claimed.** Price is being taken, not held back, and the
  claim would assert near-monopoly against two registrants' lists.
- **Class: [ ] WIDE [ ] NARROW [ ] NONE [x] PROVISIONAL** — the report NARROW-or-better on margin,
  capital intensity, persistence and the customers' own antitrust complaint, **but unmeasured against
  its one substitute and unsupported by any unit series**; Listings NONE; B2B NONE. Blended by segment
  profit (CARFAX ~75%): **PROVISIONAL.** **Direction:** not shown widening; growth decelerating and
  increasingly attributed to price.

**THE VERDICT, AND THE SEPARATING TEST ASKED ALOUD.**
*Can I name the document that would resolve this?*
- **Not one that exists and I have not read.** Every rung that could carry it has been read or tried:
  the Form 10 and its four earlier versions, the 10-Q, the 8-Ks, the Investor Day deck and the Q2
  earnings deck, S&P Global's segment note, six IHS Markit 10-Ks, and the 10-Ks of CarGurus, Cars.com,
  OPENLANE, ACV and Carvana. **The Experian AR is blocked at its IR rung and, even if opened, would give
  attacker scale in revenue at best — not whether dealers treat the reports as substitutes, and not the
  unit trend.** Recorded below as a non-verdict-moving work order.
- **The record that would resolve it does not yet exist, and it can be named precisely:** (1) a filed
  CARFAX unit series on a stated, consistent definition — **dealer rooftops, revenue per rooftop, and
  vehicle-history report volume** — across **two or three standalone fiscal years** (MBGL's first 10-K,
  for FY2026, is due in early 2027); (2) a stable, defined split of growth into price and volume (the
  Form 10 and the 10-Q attribute the same quarter differently — see Q3); (3) any filed measure of
  AutoCheck's scale. **An IN today would hold only after narrowing three assumptions** — that AutoCheck
  is materially behind, that the fall in report views is a redefinition, and that price is not costing
  dealers — **and a verdict that needs narrowing assumptions is UNKNOWABLE [E4-18].** An OUT would need
  the opposite assumptions against 45% margins held for years under a well-funded attacker. Neither is a
  one-foot bar.
- **Why not OUT, given the queue's ACVA rule that registrant-named substitutes fail criterion (2)?**
  Because ACV had no return on capital in seven filed years and was last in its row on every measure;
  the substitute list there was corroborated by the numbers. Here the numbers point the other way, the
  unit disclosure points down, and no filing adjudicates between them.
- **[E3-47], the hesitation required on an understood name, taken:** this is a business I understand
  (Q1 IN), at a price that may not be demanding (Q5, recorded). That is precisely where a wrongly closed
  file costs most — and it is also where operator rule 9 bites hardest, because a cheap-looking
  45%-margin data business is the hypothesis an analyst most wants to clear. The closure is **without
  prejudice** and names what reopens it.

- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [x] UNKNOWABLE → CARFAX's position against its one
  direct substitute (Experian's AutoCheck) is measured in no filing; the unit disclosures that would
  stand in for it are a frozen dealer floor and one consumer metric that fell; B2B and Listings carry
  no franchise of their own; and the record that would decide it — a defined CARFAX unit and
  price/volume series over two to three standalone years — does not yet exist.**
- **Non-verdict-moving work order (UNRESEARCHED, recorded so it is not lost):** Experian plc Annual
  Report 2026 (year to 2026-03-31), revenue by customer segment — does it disclose an automotive share?
  Lives at experianplc.com (company IR rung); blocked on 2026-09-13 by Incapsula bot protection.
- **What reopens the file [E3-47]:** MBGL's FY2026 and FY2027 10-Ks (or 10-Q KPIs) showing CARFAX dealer
  rooftops and report volume flat-to-up on a stated definition while price is taken; a reconciled
  price/new-business attribution; margins held through the stand-up.
- *The hard sequence closes the file here. **Q3-Q6 below are RECORDED, NOT GATES** (the HHH/RGTI
  precedent), because the brief asks for them and the output contract requires a price under
  `COMPUTATION — NOT A CLEARANCE`. Nothing recorded below can reopen Q2.*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — **RECORDED, NOT A GATE (file closed at Q2)**
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`. Run in full because the brief asks for it;
nothing here reopens Q2, and [E2-37, E2-38, E3-39] forbid it from promoting the name in any case.*

**STEP 1 — THE WEIGHT CASE.**
- [ ] **Daily execution [E3-38]** — no. A subscription data business sold on a database accumulated
  over decades; the damage a manager can do in a quarter is small.
- [ ] **Control [E1-16]** — no. A minority, exit-able holding.
- [ ] **Leverage [E3-29]** — no, in the sense the source means (20:1 asset leverage). $2.0bn of notes
  against 2025 operating cash of $485M (Q4 quantifies it); a manager's error does not wipe the equity
  in one bad year.

**Case declared: OVERLAY.** Findings are recorded; manager quality alone would not stop the run.

**Honesty — binary, filings-based [E5-16].** No integrity disqualifier found. Matters, dated to when
public: the **2013 dealer antitrust complaint against CARFAX** (public in IHS Markit's 10-Ks; *"On
September 30, 2016, the District Court granted CARFAX's motion for summary judgment, dismissing all
claims"*) — a competition claim, dismissed, not personal misconduct; the 10-Q's legal note says none of
the pending proceedings *"is expected to have a material adverse effect"*. Board and officers took
office 2026-06-25 and 2026-07-01 (8-Ks of 2026-06-26 and 2026-07-02): Joseph R. Hinrichs, chair
(*"President and Chief Executive Officer of CSX Corporation from September 2022 to September 2025"*,
earlier President of Ford's global automotive business); William W. Eager, CEO (CEO of CARFAX since
December 2021 and *"Vice President of CARFAX's Dealer Business for 17 years"*, S&P Global 10-K FY2025);
Matthew A. Calderone, CFO (joined 2026). **A pass here is the absence of a found disqualifier, not a
finding that they are honest [E5-17]; the public record of this team as a public company is ten weeks
long.**

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E2-49].** Each a prompt to read.
- [ ] **Weak accounting.** Not ticked. SBC is expensed; carve-out allocations and the separate-return tax
  method are disclosed and explained; transaction costs are quantified at every line. *The carve-out's
  cash-tax line ($15M / $29M / $26M paid against current tax of $156M / $178M / $196M) is not a tell:
  combined-return taxes were "deemed settled with S&P Global as a component of Net parent investment"
  (10-Q Note 5), so the cash-tax share of pretax cannot be read on this record [E4-30].*
- [ ] **Unintelligible footnotes.** Not ticked — but see the attribution defect under the sixth flag.
- [x] **Trumpeted projections [E4-22 third flag, E3-48, E5-30].** **FIRES, and the first outturn is in.**
  Investor Day of 2026-05-12 (S&P Global 8-K `0001104659-26-058908`, EX-99.1): *"7.5-10% annually"*
  organic revenue growth, *"8-11% Adj. EBITDA growth"*, *"+50bps annually after standalone reset"*,
  *"75%+ of FCF returned annually"*, and for 2026 itself **organic constant-currency growth of
  *"7.5-9%"*** (p.90). **87 days later** the 8-K of 2026-08-07 guided FY2026 revenue growth to
  **"6.9% - 7.7%"** on a **reported** basis, with foreign exchange having *"benefited ... first half
  revenue by ~$5 million"* (Q2 earnings deck p.5) — so the organic figure sits below the reported one,
  and **the first guidance was cut below its own floor within one quarter** while the release says it
  *"reiterated medium-term financial targets"*. **[E3-48]: the record of the people who made the
  projections is one projection long, and it missed.** [E5-30]: a guidance culture adopted on day one
  is a ratchet, not a season.
- [ ] **Serial share issuance [E5-15].** Not ticked. 294,821,320 shares, fixed by the distribution; the
  Tax Matters Agreement forbids issuance outside employee safe harbours to 2028-07-01. SPGI awards held
  by MBGL staff were converted into MBGL awards under the 2026 Long Term Incentive Plan (10-Q, Subsequent Events) — a dilution source, measured at Q4.
- [x] **EBITDA promotion [E4-29].** **FIRES at full strength.** The results release leads with
  *"Delivered net income of $53 million and adjusted EBITDA¹ of $202 million, which represents a 43%
  margin and a 7% increase year-over-year"* in a quarter when **GAAP operating profit fell 15%** ($96M
  → $82M). Adjusted EBITDA excludes **stock-based compensation** [E5-06] and *"employee severance
  charges and other costs that are not representative"*; the leverage target (*"<2.5X Target Gross
  Leverage Ratio"*) and the growth targets are denominated in it.
- [ ] **Filed-figure fraud tells [E4-30].** Not ticked: quarterly revenue $420M / $439M / $445M / $446M
  (2025) is not engineered-smooth (Q4 flat on Q3), and the cash-tax test cannot be run on a carve-out.

**Sixth — metric-switching [E2-49]. FIRES, twice.**
1. **The segment yardstick.** Information Statement (May 2026): *"We internally manage our operations by
   reference to operating profit with economic resources allocated primarily based on each segment's
   contribution to operating profit."* 10-Q Note 7 (August 2026): *"Beginning in the second quarter of
   2026, the Company changed its segment profitability measure from segment operating profit to
   Adjusted EBITDA and recast prior period amounts accordingly."* **The switch landed in the quarter
   segment operating profit fell** (B2B $16M → $3M; total $96M → $82M, EX-99.1 Exhibit 4), with no
   advance notice or reasons in the Form 10. The corpus's test: *"Yardsticks seldom are discarded while
   yielding favorable readings."* (Transaction costs caused most of the fall, which is the humility
   clause; the switch still followed the deterioration rather than preceding it.)
2. **The growth attribution.** Form 10/A (2026-05-27), Q1 2026, whole company +$35M: *"continued new
   business growth and solid underwriting volumes of $26 million and $2 million, respectively, and the
   remaining increase driven by improved contract terms"* (≈$7M). 10-Q (2026-08-07), H1 2026 +$64M:
   *"driven primarily by price increases of approximately $16 million and $36 million, respectively,
   and continued new business growth of approximately $8 million and $20 million"*. **Implied Q1 from
   the 10-Q: price ≈$20M, new business ≈$12M — against $7M and $26M for the same quarter three months
   earlier.** Neither filing defines the terms. Either the vocabulary changed (new business once
   included price on renewals) or the measurement did; **the half-owner test [E2-26] fails on this line
   until it is reconciled**, and it is the one line Q2 needs.

**Ninth and tenth — "except for" [E2-57] and the restructuring charge [E3-53, E5-33]. PROMPT.** The
Investor Day reconciliation removes *"One-Time Adjustments"* of **$30M (2023), $23M (2024), $40M
(2025)** — severance every year (2025: $20M, 8-K EX-99.2), acquisition integration, transaction costs —
and guides a further *"one-time stand-up / transition cost of ~$75-100M over 12-18 months"*, of which the
Q2 deck says *"~50% ... to be capitalized"*. **Recurring every year is not one-time; these stay in the
owner-earnings mean at Q4.**

**Converging flags [E4-52].** Projections cut within a quarter, an EBITDA headline over a falling GAAP
line, the segment yardstick switched the quarter it turned, a growth attribution rewritten between two
filings, and "one-time" costs every year — **five prompts pointing one way: the spin-off's growth-and-margin
story.** Read as one system, not a sum. The corpus says a flag reads the accounting, not the person
[E5-38]; this record is about how the company presents itself at its first public moment, and it is the
reason the unit series Q2 needs cannot be taken on trust when it arrives.

**STEP 3 — THE PRIMARY TEST [E2-01], scoped [E2-43, E2-73].** Book equity is S&P Global's
purchase-accounting investment ($11,485M at 2025-12-31, $9,835M at 2026-06-30), so the earnings rate on
book equity (~2%) measures IHS Markit's 2022 price, not the operators. On unleveraged net tangible
assets (~$68M, Q2) the rate is unmeasurably high. **The operators' record on the capital they actually
work with is excellent; no GAAP series under their own stewardship as a public company exists.**

**The half-owner test [E2-26].** Mixed. Passes on transaction costs (quantified at every line, allocated
share disclosed: *"approximately $15 million and $22 million, respectively, was allocated to the Company
from S&P Global"*). **Fails on units**: the dealer count is a frozen floor, report views are given as
floors on shifting windows, and the price/volume attribution is inconsistent — the business facts an
owner in the reversed position would most want.

**The institutional imperative [E2-30].**
- [ ] resists change — not observed.
- [x] **projects/acquisitions to soak up funds — PROMPT.** Investor Day *"M&A as an Accelerant ...
  Additional capacity while maintaining IG rating"*; Information Statement: *"well-positioned to
  capitalize on inorganic growth opportunities across what is a highly fragmented industry ...
  including but not limited to automotive software, service lane solutions and the parts and
  aftermarket"*. Stated intent, not yet an act; the Tax Matters Agreement constrains large deals to
  mid-2028.
- [ ] staff studies for the leader's craving — not observable.
- [ ] peer imitation — not scored.

**Capital allocation — [E5-08], [E5-24], [E2-52], [E2-60].**
- **The $2.0bn to S&P Global is the former parent's allocation, not this management's.** Information
  Statement: *"The financial terms of the Separation, including the new indebtedness expected to be
  incurred by Mobility, have been determined by the S&P Global Board of Directors based on ... the
  level of indebtedness relative to earnings of various comparable companies."* **[E4-27]:** the party
  that set the debt was the party receiving the cash. [E2-60]'s third dimension — financial strength —
  is carried to Q4.
- **Buybacks: none yet** (*"Share Repurchases Disciplined approach; beginning in 2027"*). Condition (1),
  ample funds: gross leverage 2.8x (Investor Day p.115, LTM 2026-03-31) above the company's own *"<2.5X"*
  target, first coupon $60M in Q4 2026 — **not yet met on the company's own yardstick.** Condition (2),
  material discount: cannot be scored before an act. **But the pre-committed *"Target of 75%+ of FCF
  returned annually"* is a price-insensitive promise, and [E5-24] says "what is smart at one price is dumb
  at another."** Prompt, bound to position size, with the humility clause [E4-13].
- **Dividend:** $0.06 a quarter (declared August 2026) ≈ **$70.8M a year** on 294.8M shares, funded from
  operating cash, not issuance — **[E2-52] does not fire.**

**What pay vests on [E4-27].** Legacy awards, carried into MBGL shares: CARFAX PSUs *"based on the level
of attainment of a three-year cumulative non-GAAP ICP Adjusted EBITA ... goal for CARFAX U.S."* (2025
grant: threshold $1,490M, target $1,557M, maximum $1,648M), *"as may be adjusted in a manner deemed
appropriate by the S&P Compensation Committee"*; the CARFAX bonus pool *"funded 100% based on CARFAX U.S.
EBITA"* (2025 target $467.1M, actual $479.3M); S&P Global PSUs on adjusted EPS. **EBITA is after
depreciation, which is the better half of the choice [E4-29]; it is before amortization, which [E2-43]
allows for operators; and it is adjustable after grant, which is where incentives leak.** The post-spin
program is undesigned (*"we have generally not yet made any final determinations"*); the CEO's first MBGL
grant is **$2.5M of time-vesting RSUs** (8-K 2026-06-26), and Investor Day says *"Equity compensation to be
aligned with public company peers"* — **SBC is guided up** (Q4).

**THE GUARDRAIL — checked.**
- [x] Nothing here promotes the name; a strong Q3 could not repair Q2 [E2-37, E2-38, E3-39].
- [x] Key-person dependence: none recorded at Q2 [E4-23].
- [x] No great manager is the reason to act [E2-35, E2-36].

- **VERDICT (recorded, not governing): no integrity disqualifier found [E5-16, E5-17]; weight case
  OVERLAY; five converging disclosure flags [E4-52] — projections cut within a quarter [E3-48], EBITDA
  headline [E4-29], two metric switches [E2-49], recurring "one-time" charges [E2-57, E3-53]; a
  price-insensitive capital-return pledge [E5-24] as a prompt. As a gate this would read IN (no
  disqualifier) with the flags binding position size — but the file is closed at Q2.**

## Q4 — WILL IT SURVIVE? — **RECORDED, NOT A GATE (file closed at Q2)**

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**THE PERIMETER, AND WHY THE FIVE-YEAR DEFAULT CANNOT BE BUILT [E2-42].** One perimeter: the Mobility
business as distributed, recorded in **audited combined cash-flow statements for 2023, 2024 and 2025**
(Form 10/A `0001104659-26-066592`, F-23) and the **condensed combined statement for H1 2026 and H1 2025**
(10-Q `0002090312-26-000014`). **No cash-flow statement exists for this perimeter before 2023:** the first
DRS (`0001104659-25-101868`) carries 2024 and 2023 only; S&P Global's 10-K carries a Mobility *segment*
(revenue, operating profit, D&A, capex) from 2022-02-28, not a cash-flow statement; IHS Markit's 10-Ks
carry a *Transportation* segment on a November year-end that included other businesses. **Windows before
2023 are refused, not rebuilt** — a segment operating-profit line is not a cash-flow statement, and the
STLA rule rebuilt pro forma only from filed cash-flow statements. **So the windows are three years, two
years, the latest year and the trailing twelve months to 2026-06-30; the five-year default is short by two
years and says so.** Perimeter changes inside the window: Market Scan acquired 2023-02-16 ($214M cash);
Catalyst for Aftersales sold August 2023; nothing material since.

**Construction (CONVENTION, the framework's): operating cash flow less stock compensation less (c).**
OCF is already net of current income taxes: the carve-out's combined-return taxes were *"deemed settled
with S&P Global as a component of Net parent investment"* (10-Q Note 5) with no add-back line in the
cash-flow statement, so the current provision ($156M / $178M / $196M) sits inside OCF as if paid. The Q2
earnings deck's *"Cash taxes will be $80-90M higher due to the Deferred Tax Liability"* describes the same
gap between book tax and current tax that the deferred-tax line ($(95)M / $(102)M / $(90)M) already
removes from OCF. **No further tax adjustment.**

**Owner earnings by year, filed perimeter, $M** (arithmetic in `_research 2026-09-13 MBGL/oe.py`):

| | OCF | SBC | Depreciation | Capex | Related-party WC lines | **OE at D&A (c)** | **OE at capex (c)** | OE at capex, related-party lines removed |
|---|---|---|---|---|---|---|---|---|
| 2023 | 393 | 20 | 12 | 18 | +17 | **361** | **355** | 338 |
| 2024 | 427 | 28 | 13 | 15 | −5 | **386** | **384** | 389 |
| 2025 | 485 | 22 | 14 | 24 | +14 | **449** | **439** | 425 |
| TTM to 2026-06-30 | 441 | 22 | 14 | 28 | −27 | **405** | **391** | 418 |

*TTM = FY2025 − H1 2025 + H1 2026. Related-party lines are "Due from related parties" plus "Due to related
parties" in the working-capital section — intercompany settlements that end with the separation, shown as
a sensitivity, not as a correction.*

- **Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT.** **The D&A default [E3-44, E2-41]
  is valid here**: capex is 0.9-1.4% of revenue and the filing gives no sign that depreciation understates
  renewal; this is not the [E5-20] class. The D&A end uses the **"Depreciation" line only** ($12-14M) —
  the $295-296M of amortization is IHS Markit purchase accounting, not a renewal cost. **Capex runs above
  depreciation every year** (18 vs 12, 15 vs 13, 24 vs 14), so the band is carried as depreciation →
  total capex. **Judgment on capitalised technology:** gross capitalised technology rose $24M → $40M in
  2025 (combined Note 1) while property and equipment fell and no other investing line absorbs it, so the
  $24M capex line is read as including it. **Where the real maintenance lives:** in operating expense —
  data acquisition, the give-get network, and advertising (*"primarily comprised of advertising for
  CARFAX"*, $76.4M in FY2021 at IHS Markit; +$23M of strategic and advertising spend in 2025). Those are
  already inside OCF, which is why (c) is small and why the band is narrow.
- **Stock compensation subtracted in full [E5-06]: RESOLVED and COMPLETE on the filed perimeter.** The
  cash-flow line resolves in every year ($20M / $28M / $22M; $9M in each half). Allocated S&P Global
  corporate costs, including any equity pay inside them, were *"effectively settled"* through parent
  investment and so reduce OCF with no add-back — nothing is omitted. **SBC is 4.5-6.6% of OCF**, far
  below the level at which [E3-70]'s grant-date measure must be built by hand. **But the standalone level
  is guided UP and unquantified** (*"Equity compensation to be aligned with public company peers"*,
  Investor Day p.96; the CEO's $2.5M RSU grant, 8-K 2026-06-26). Carried as a named downward pressure; no
  number invented for it.
- **Working-capital increment:** inside OCF. Unearned revenue +$5M / +$7M / +$4M; receivables
  −$34M / −$12M / −$11M. **H1 2026 OCF fell 19% ($233M → $189M)** on payables, prepaid assets,
  receivables and a −$19M related-party swing, in the half the separation costs landed — named at the
  window, not smoothed.

**THE STANDALONE BRIDGE — the balance sheet and head office changed; the business did not.** Every input
is a named judgment:
1. **New interest.** Coupons $650M × 5.050% + $650M × 5.450% + $700M × 6.050% = **$110.6M a year**
   (10-Q Note 4; the Q2 deck guides *"Second half 2026 interest expense is expected to be ~$55M"*, which
   agrees). After tax at **26%** — the midpoint of the company's *"Medium-term effective tax rate of
   25-27%"* (Investor Day p.97, IR rung, flagged) — **−$81.8M.**
2. **Old interest removed.** The Canada Carfax Loan interest ($18M / $17M / $14M paid) ends with the
   separation; added back after tax, **+$10-12M**.
3. **Standalone running costs.** *"Expected incremental ~$20-25M in run-rate costs to operate as a
   standalone company compared to historic SPGI allocations"* (Investor Day p.96) and *"~150bps on
   full-year margins (relative to FY'25 base) on a run rate basis"* (Q2 deck) = ~$26M. After tax **−$14.8M
   (optimistic) to −$19.2M (conservative)**. *A company estimate, used because no filed figure exists;
   the Information Statement calls the historical stand-alone cost "not practicable" to quantify.*
4. **Stand-up costs, carried not annualised away [E5-33].** *"one-time stand-up / transition cost of
   ~$75-100M over 12-18 months"*, *"~50% of these one-time costs to be capitalized"*. Spread over the
   five-year default window: **−$13.1M to −$17.4M a year.**

**Standalone owner earnings, $M:**

| Window | Optimistic end (D&A c, related-party lines in, low costs) | Conservative end (capex c, related-party lines out, high costs) |
|---|---|---|
| 3-year mean 2023-25 | 301 | **278** |
| 2-year mean 2024-25 | 319 | 300 |
| FY2025 | **350** | 317 |
| TTM to 2026-06-30 | 306 | 310 |

- **Short window (FY2025 / TTM): $306-350M. Long window available (3-year mean): $278-301M.**
- **Combined range: ~$280M to ~$350M.** Spread from the top: **~21%**.
- **Too wide to conclude? No [E4-25].** The capex band is worth only $6-14M a year; the width is almost
  entirely **growth across the window** (OE at capex rose $355M → $439M, +11% a year) plus the two
  standalone-cost judgments.
- **Distorted years named [E5-11]:** H1 2026 (separation costs, related-party unwinding); 2025 carries
  $40M of "one-time" adjustments, 2023 $30M, 2024 $23M — **kept in, because they recur.**
- **Normalise down for luck [E4-41]:** the Investor Day's own slide p.70 shows new and used vehicle prices
  *"at or near all-time highs"*, and the company says report value *"Grows with vehicle values"* (p.72).
  A price level at a record is a favourable exogenous break; it cannot be removed numerically from this
  record, so it is **named and pushes the reading toward the conservative end**.

### Great, good, or gruesome? **[E4-20]**
- [x] **great, on the operating perimeter** — owner earnings of $355-439M on unleveraged net tangible
  assets of ~$68M (Q2); growth took capex of 1-1.4% of revenue.
- [ ] good
- [ ] gruesome
- **Evidence and its limit:** the business consumes almost no capital. **The equity holder, however, owns
  it with $2.0bn of debt it never used**, taken to pay the former parent — the owner's savings account
  pays its rate after a $110.6M coupon that bought nothing for the business.

### Staying power — score all three **[E5-11]**
- **(1) Large and reliable stream of earnings — PASS.** OCF $393M / $427M / $485M; 81-82% subscription;
  no customer above 10%; company-compiled revenue fell only 2% in 2020 against a 15% industry decline
  (Investor Day p.91, flagged).
- **(2) Massive liquid assets — FAIL.** Cash **$186M** at 2026-06-30 against a stated target of about $200M;
  the **undrawn $500M revolver is a bank line and is not counted** [E5-39].
- **(3) No significant near-term cash requirements — MARGINAL.** No maturity before **2029 ($650M)**;
  near-term calls are the coupon ($110.6M a year, the first $60M in Q4 2026), the stand-up cost ($75-100M
  over 12-18 months), the dividend (~$70.8M a year) and the pledge to return *"75%+ of FCF annually"* with
  buybacks from 2027. None is large against operating cash; together with a 75% payout pledge they leave
  little to reduce the notes before 2029.
- **Leverage, named and quantified [E4-16, E3-29]:** gross debt **$2,000M**, net **$1,814M**; **4.1x 2025
  OCF**; the company's own gross leverage **2.8x** LTM Adjusted EBITDA against its *"<2.5X"* target. Revolver
  covenant: *"total net leverage ratio of not greater than 3.50 to 1.00"*. Notes: no leverage covenant; a
  101% put on a change of control *with* a downgrade below investment grade. **Coverage [E2-54]: owner
  earnings before interest at the conservative end (~$360M after tax) cover the after-tax coupon ~4.4x;
  interest is "comfortably met out of current cash flow net of ample capital expenditures." PASS.**
  **Terms [E3-52]:** fixed-rate, staggered 2029/2031/2036, unsecured — the better kind of debt.
- **[E5-11]: 1.5 of 3.**

### Name the specific way THIS business dies **[E2-27, E3-24]**
- **The mechanism:** the vehicle-history report stops being the thing the car buyer asks for. Two routes,
  both already visible in the filings: **(i) the source moves** — the car reports its own service and crash
  history to its maker (36 OEM programmes already contribute; the Information Statement names connected-car
  forecasting as a product, not as a threat), and **(ii) the substitute is bundled** — the two largest
  wholesale platforms already offer AutoCheck beside CARFAX. The first sign would be **units falling while
  price rises** — the Q2 report-view figure is already that sign on thin evidence. With **$2.0bn of debt set
  by the departing parent** and a **75%+ free-cash-flow return pledge**, there is no cushion when the
  $650M 2029 maturity must be refinanced.
- **Quantified from filed figures:** a **10% revenue loss** ($175M) at a **70% decremental margin** (a
  data business's costs are mostly fixed; judgment) removes ~$122M of pre-tax profit, ~$90M after tax:
  owner earnings fall from ~$280-350M to **~$190-260M**, coverage stays above 3x, Adjusted EBITDA falls to
  ~$590M and net leverage rises to ~3.1x — **under the 3.50x revolver covenant.** A **25% loss** ($438M,
  ~$306M pre-tax) takes Adjusted EBITDA to ~$405M and net leverage to **~4.5x — through the covenant**, with
  the 2029 notes to refinance on a falling business. **The company survives the first; the second is the
  death, and it would arrive slowly, visible in units first.**
- **Likelihood:** [ ] likely [x] **a real possibility over ten years** (for the 10% case) · [x] **a
  low-level possibility before the 2029 maturity** (for the 25% case).
- **Against the registered survival shapes** (`Screens/WATCHLIST RUN QUEUE.md`): not ORCL's contract to
  keep spending, not ARM's stock pay, not THE CASH IS SPENT UNDOING PAST WORK, not the FIFTH's recurring
  distribution above owner earnings (the dividend and pledge sit below owner earnings), not the SIXTH's
  borrowed balance sheet (the operations use none), not THE TENANT or THE PASS-THROUGH. **It shares HHH's
  and BE's too-little-history feature for the standalone company only, not for the business.** **Proposed
  shape, for the operator to register or reject: THE DOWRY** (it would be the FIFTEENTH: twelve are
  registered, SPOT's THE TENANT and GFS's THE PATRON are proposed and unregistered, both read in the
  reading list before this was written) — a spun-off business carrying debt
  sized by the departing parent to *"the level of indebtedness relative to earnings of various comparable
  companies"* and paid to that parent, so the leverage was chosen by the party that left with the cash and
  survival rests on a franchise the new owners must still prove. **Distinguishing test:** the debt financed
  a distribution to a former controller at separation, not the operations and not a recurring payout.
- **VERDICT (recorded, not governing): would be IN on survival** — owner earnings ~$280-350M on a range
  narrow enough to conclude, coverage ~4.4x, no maturity before 2029, gross leverage 2.8x; [E5-11] 1.5 of 3
  with liquid assets failing — **with the franchise that carries all of it unmeasured at Q2.**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 is UNKNOWABLE. **The file is closed.** What follows is
the price, stated because the operator's instruction requires every run to end with one.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND? — **COMPUTATION — NOT A CLEARANCE**

*Headed as operator protocol rule 3 requires. No entry language; no ranking; no band.*

- **Price:** **US$20.16**, NYSE close **2026-09-11** (Yahoo Finance chart API via `tools/sources.py:price`,
  **aggregator, live quote only, flagged**). Daily closes in the same series from 2026-06-26 (when-issued) to
  2026-09-11: $19.00-$23.00.
- **Shares:** **294,821,320** — 10-Q cover (*"As of July 1, 2026, there were 294,821,320 shares of common
  stock of the registrant outstanding"*), equal to S&P Global's count at the 2026-06-15 record date on the
  1-for-1 ratio (10-Q Note 3). **One economic class; no treasury shares; no shares retained by S&P Global
  (*"S&P Global retains no ownership interest"*); none issued to a counterparty.** Converted equity awards
  and new RSUs are unvested and uncounted (the company guides an FY2026 average of *"295M – 297M shares"*).
  **Split-invariant check:** listed 2026-07-01, no split since; close × measurement count.
- **Market cap:** $20.16 × 294,821,320 = **US$5,943.6M**. Net debt $1,814M → enterprise value ~$7.76bn.
- **Sovereign:** **5.35%**, US Treasury 30-year, 2026-09-11, struck via `tools/sources.py`.

**1. THE YIELD.** Standalone owner earnings **~$280M to ~$350M** ÷ $5,943.6M = **4.7% to 5.9%**, beside the
sovereign at **5.35%**.

**2. WHAT THE PRICE ALREADY ASSUMES.** At the **~10% floor [E4-28]**, a buyer needs perpetual owner-earnings
growth of **~4.1% (optimistic end) to ~5.3% (conservative end)** — *growth needed = 10% − yield*. At the
bond rate, the price needs **about none** (−0.5% to +0.7%). **What the business has done:** owner earnings
at capex +11% a year 2023-25 on the filed perimeter; revenue +8.6% a year; company-compiled organic revenue
growth ~9-10% a year over a decade (flagged). **What the company now guides:** FY2026 revenue +6.9-7.7%
reported, below its own 7.5-9% organic guidance of May. **[E4-35]:** 4-5% forever is not the heroic
15%-for-20-years case the corpus bets against, but it is **the growth of a franchise whose units Q2 could
not see** — and [E4-44] bounds value by earnings, not by price increases on a shrinking base.

**3. WHAT YOU ARE PAID.** At today's price, **−0.7 to +0.5 points over the sovereign** before growth.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** (owner earnings × (1+g) ÷ (r − g), per share, arithmetic in
`oe.py`):

| discount rate | g = 0% | g = 3% | g = 5% | g = 6% |
|---|---|---|---|---|
| **10% floor** | **$9-12** | $14-17 | **$20-25** | $25-31 |
| 5.35% sovereign | $18-22 | $41-52 | not meaningful (r ≈ g) | — |

- **conservative ~$9-12 (no growth, at the floor) · optimistic ~$25-31 (6% growth, at the floor) · current
  price $20.16.**
- **In words, what the buyer is paying for:** the no-growth value of the standalone business at the bond
  rate, which is also its value at the 10% floor **only if owner earnings grow about 5% a year forever**.
  The buyer is paying for CARFAX to keep taking price without losing dealers or report volume, for B2B to
  hold, and for the $2.0bn of separation debt to be carried without incident — **the first of which is the
  exact question Q2 could not settle.**
- **Screamer test [E4-01], recorded:** the price sits **inside the range** (above the no-growth value at the
  floor, below the growth cases). **No useful conclusion — move on.** Not below the conservative case.
- **Windage count:** conservatism was spent **once**, at the conservative end of the owner-earnings range
  (capex (c), related-party lines out, high standalone costs, full stand-up cost). No margin of safety
  applied; no premium in the rate [E3-42].
- **VERDICT: not opened as a verdict — COMPUTATION ONLY. PASS/FAIL: FAIL (closed at Q2, UNKNOWABLE).**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL? — **RECORDED; NOTHING ARMED**

No position, no band, no PORTFOLIO row (FOLD step 4: a name that did not clear the business gates gets
reopening conditions in words, not a price alert).

**What would reopen the file [E3-47], pre-registered [E1-02]:**
- **Thesis-confirming (for reopening Q2):** MBGL's FY2026 10-K (early 2027) or later filings disclose a
  **CARFAX unit series on a stated definition** — dealer rooftops, revenue per rooftop, vehicle-history
  report volume — and it is **flat-to-up across two standalone years while price is taken**; the growth
  attribution is reconciled between "price" and "new business".
- **Thesis-breaking (would convert UNKNOWABLE to OUT):** report volume or dealer rooftops **declining for
  two consecutive annual disclosures while revenue per rooftop rises** [E4-55]; a registrant or MBGL
  filing that records a large dealer group or wholesale platform moving from CARFAX to AutoCheck; B2B
  subscription growth turning negative.
- **Survival watch:** net leverage above 3.0x on the company's own measure; buybacks begun while gross
  leverage is above the *"<2.5X"* target [E5-08 condition 1]; a tuck-in programme financed by debt before
  the 2029 maturity.
- **Next catalyst dates:** Q3 2026 10-Q (the first standalone quarter, ~November 2026); FY2026 10-K
  (~February-March 2027); Tax Matters Agreement restrictions lapse **2028-07-01**; first note maturity
  **2029**.

**The sell rule [E2-28]** does not apply — nothing is held. **Position size:** none.

- **VERDICT: not opened — file closed at Q2.**

## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Step 0 → Q1 IN → **Q2 UNKNOWABLE → file closed.**
      Q3-Q6 recorded under explicit NOT-A-GATE banners; the price is headed COMPUTATION — NOT A CLEARANCE.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the
      audited combined statements and the separation documents. The PROVISIONAL moat class sits at Q2, which
      is not IN.
- [x] **Every UNRESEARCHED item names the artifact and where it lives.** One, non-verdict-moving: Experian
      plc Annual Report 2026, customer-segment revenue (experianplc.com, IR rung, blocked by Incapsula on
      2026-09-13).
- [x] **The UNKNOWABLE verdict states what specifically cannot be known:** CARFAX's position against
      AutoCheck and the unit trend behind its price-led growth; and names the record that would decide it (a
      defined CARFAX unit and price/volume series over two to three standalone years).
- [x] **Step 0: the filing was read, with accession numbers; three figures cross-checked** (2025 revenue
      against S&P Global's segment note; H1 2026 OCF and the cover count against companyfacts).
- [x] **Owner earnings on multi-year means; windows stated; capex band disclosed as a judgment.** The
      five-year default could not be built (no pre-2023 cash-flow statement for the perimeter) and the
      shortfall is stated, not filled from segment lines.
- [x] **Competitor row filled** with two SEC filers and one IR-rung peer; the missing direct competitor is
      the ground of the Q2 verdict, not a footnote.
- [x] **Sovereign for the earnings currency (USD), from the issuing authority (US Treasury), dated
      2026-09-11, struck fresh.**
- [x] **Value stated as a round-number range** ($9-12 conservative to $25-31 optimistic at the floor).
- [x] **One bar recorded (screamer test), windage count one.**
- [x] **Price dated (2026-09-11 close), aggregator flagged.**
- [x] **Ledger ids checked against `principle_ledger.csv` before citing** (every id in this file resolves;
      [E4-27] used for incentives, [E4-52] for converging flags — the brief's warning heeded).
- [x] **Run committed to git** with a pathspec after each section (Step 0 `de1a7d4`, Q1 `c944d57`, Q2
      `1bdc987`, Q3 `20c3866`, Q4-Q6 and audit in the commit that carries this line).

**Errors of my own, corrected before commit:** (1) Q1's first draft said no commercial agreement with S&P
Global was described; the Information Statement describes non-material reciprocal data licences. (2) My
first scan of the growth attribution read only the Form 10's vocabulary; the 10-Q's "price increases"
wording was found on a second pass and became a Q3 flag. (3) The first owner-earnings script derived a TTM
interest figure from half-year interest *expense*, which includes accrued note interest never paid by the
carve-out; replaced with FY2025 cash interest paid, stated as an approximation.

**Brief and tooling defects found (reported, not fixed):**
1. **The brief's pre-check omitted the Form 10-12B, the Form 10-12B/A and three DRS filings** under
   MBGL's own CIK — the documents that hold the only cash-flow statements for the perimeter. It sent the
   run to S&P Global for predecessor history that is filed under MBGL itself.
2. **`tools/sources.py:deal_note()` labels every EX-2.1 "plan of merger or acquisition"**; here it is a
   Separation and Distribution Agreement. The note's instruction to read the exhibit is right; the label
   invites the ACVA/ROKU spread treatment on a spin-off.
3. **The triage label "Mercedes, 20-F filer"** in `Screens/2026-08-31 PREPPED READING LIST (operator
   lists).md` line 1436 and the comment at `Screens/floor_screen.py` line 154, and the WAVE 5 grouping
   "foreign 20-F filers, short XBRL history", are wrong for this ticker.
4. **A date disagreement between two filers:** S&P Global's 10-Q Q2 2026 says the notes were issued *"On
   May 19, 2026"*; MBGL's 10-Q Note 4 says *"On May 29, 2026"*. Immaterial; recorded.
5. **The company's own disclosure record, not a tool:** the report-view metric moved from 31M+ (TTM
   Sep-2025) to 28M+ (TTM Dec-2025) across DRS versions without a stated redefinition.

## REGISTER
- Verdict: [ ] IN [ ] OUT (about the business) [ ] UNRESEARCHED (about my diligence)
  **[x] UNKNOWABLE (about my evidence)** — at **Q2**.
- **One line:** Mobility Global (the CARFAX, Polk, automotiveMastermind and Market Scan business spun off by
  S&P Global on 2026-07-01, widely held, $2.0bn of notes paid to the former parent, nothing pending) —
  **Q1 IN; Q2 UNKNOWABLE**: a 43-45%-margin, capital-light vehicle-history franchise candidate whose position
  against its one direct substitute (Experian's AutoCheck) is measured in no filing and whose only unit
  disclosures are a frozen dealer floor and a report-view figure that fell, with B2B and Listings carrying
  no franchise; **price US$20.16 × 294,821,320 = US$5,943.6M; standalone owner earnings ~$280-350M, a
  4.7-5.9% yield against a 5.35% Treasury, needing ~4-5% perpetual growth to reach the 10% floor —
  COMPUTATION ONLY. PASS/FAIL: FAIL, closed at Q2.**
- **If UNKNOWABLE — what specifically cannot be known:** whether CARFAX's price-led growth is taken from a
  position AutoCheck cannot erode or from a unit base that is quietly shrinking. **Reopened by:** a defined
  CARFAX unit and price/volume series in MBGL's FY2026 and FY2027 filings.
- **Non-verdict-moving work order:** artifact Experian plc Annual Report 2026 (customer-segment revenue) ·
  lives at experianplc.com · rung company IR · blocked by Incapsula bot protection.

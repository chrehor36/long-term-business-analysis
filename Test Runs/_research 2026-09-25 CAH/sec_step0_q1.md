## STEP 0 - THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** - the currently observed rate, never a forecast
**[E4-15, E3-32]**:
- rate **5.47** % · date **09/24/2026** (the newest row on the curve when this run struck it, 2026-09-25) · source
  (issuing authority) **US Treasury daily par yield curve, 30 Yr, `home.treasury.gov` daily-treasury-rates.csv for
  2026**, struck fresh by this run and saved raw as `Test Runs/_research 2026-09-25 CAH/treasury_2026.csv`;
  `python tools/run.py CAH` printed the same figure and date from the same source. Neighbouring rows 5.40 (09/23),
  5.29 (09/22). **FRED DGS30 was not used.**
- FX: **not required.** Segment note: United States revenue $252,639M of $254,344M segment revenue in FY2026
  (99.3%); the functional and reporting currency is the US dollar (*"our functional currency"*, market-risk section).
  USD sovereign.

**The filing was read** - not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K for the year ended 2026-06-30, filed 2026-08-11, accession `0000721371-26-000038`** (`cah-20260630.htm`).
    Read: cover; MD&A whole (this filer puts MD&A first: overview, significant developments, the IEEPA tariff refund,
    results by segment, other components of operating earnings, liquidity and capital resources, contractual
    obligations, critical accounting estimates); the non-GAAP reconciliation section; market risk; Business whole
    (segments, Red Oak, acquisitions table, customers, suppliers, competition, regulation); Risk Factors whole;
    Properties and Legal Proceedings; the issuer-purchase table; the four primary statements with every cash-flow
    reconciliation line; Notes 1 (VIEs, SBC policy), 2 (acquisitions and purchase-price tables), 3 (restructuring),
    4 (goodwill by segment, accumulated impairments, intangibles), 5 (leases), 6 (debt), 7 (commitments, opioid and
    tax contingencies), 11 (buybacks), 12 (EPS), 13 (segments), 14 (share-based compensation, including The Specialty
    Alliance's own plan) and Schedule II.
  - **Earlier 10-Ks, each carrying three years of cash-flow statements, so FY2012-FY2026 (fifteen years) is covered
    without a gap from filed statements:** FY2025 `0000721371-25-000079`, FY2024 `0000721371-24-000056` (which
    **revised** FY2022 and FY2023 for *"an accounting error related to revenue recognition from third party payors
    within the at-Home Solutions operating segment"* and other immaterial errors; the revised figures are used),
    FY2023 `0000721371-23-000060`, FY2020 `0000721371-20-000089`, FY2019 `0000721371-19-000090`, FY2017
    `0000721371-17-000083`, FY2014 `0000721371-14-000181`. Opened for dated language as well as numbers (the
    Walgreens and Express Scripts expirations in the FY2014 10-K, the OptumRx expiration in the FY2024 10-K, the
    Cordis and Patient Recovery purchases, the $5.63bn opioid charge in the FY2020 10-K).
  - **8-K of 2026-08-11 (`0000721371-26-000037`) with its EX-99.1 FY2026 results release**, read for guidance and
    non-GAAP language; every 8-K main document from 2025-08-14 to 2026-08-11 (the August 2025 notes offering, the
    364-day facility and receivables-facility amendment of October 2025, the January 2026 outlook update, the
    Chief Accounting Officer succession of March and August 2026, the chair's retirement of March 2026, the $4.0bn
    revolver of 2026-08-07, `0000721371-26-000036`).
  - **DEF 14A filed 2026-09-21, `0001308179-26-000402`**, downloaded; pay metrics read (Q3 prompts).
- **deal_note, opened:** the screen column is empty. The submissions index lists **no S-4, 425, DEFM14A, SC TO or SC
  13E3** in the recent filings; every Item 1.01 8-K since August 2025 is a financing (the notes of August 2025, the
  364-day facility, the receivables-facility extension, the $4.0bn revolver). **Nothing deal-shaped is live against
  Cardinal; the quote is an owner-earnings price, not a spread.** Cardinal is itself an acquirer: the FY2026 release
  names *"the Company's recently completed tuck-in acquisition of Strive Medical and the announced tuck-in
  acquisition of the Diabetes Health business of AdaptHealth"*, with no price in the documents read.
- **figure cross-checked against the filed statement: FY2026 net cash provided by operating activities, $5,174M**,
  rebuilt from its own reconciliation lines: net earnings 1,705 + D&A 956 + investment impairments 21 + Outcomes
  impairment 122 + asset impairments 177 + share-based compensation 367 + deferred taxes 91 + bad debts 74 = 3,513;
  working-capital lines: receivables -408, inventories -488, payables +3,463, repurchases of liability-classified
  Specialty Alliance Units -45, other accrued liabilities -861 = +1,661; total **5,174. Ties.** The XBRL pull
  (`peers_xbrl.txt`, `vintage="newest"`) reproduces FY2026 revenue $254,248M and operating cash $5,174M against the
  filed statement; it also carries FY2022 operating cash as **$3,175M, the FY2024 10-K's revised figure, against
  $3,122M in the FY2023 10-K as first filed** (the at-Home revision above).
- *If the filing could not be obtained -> **UNRESEARCHED**.* **Not invoked; every document came from SEC EDGAR primary
  documents.**

**THE PRICE AND THE CAP** *(struck by this run, not carried from the screen)*
- **Share count, quoted from the cover of the 10-K for the year ended 2026-06-30, accession `0000721371-26-000038`,
  the latest periodic filing:** *"The number of the registrant's common shares, without par value, outstanding as of
  July 31, 2026, was the following: 232,575,728 ."* Note 11: 750 million Class A and 5 million Class B common shares
  authorised, *"Only Class A common shares were outstanding at June 30, 2026 and 2025"*; no preferred issued. **One
  class; no classes summed.** `python Screens/cover_shares.py CAH` returned the same document, accession and count.
- **Price $222.62** (close 2026-09-24, **aggregator quote, flagged**: Yahoo Finance chart endpoint, raw response saved
  as `price_raw.json`; `regularMarketTime` 16:00 EDT on 09-24). A null close for 2026-09-22 in the aggregator's series,
  recorded not filled. Two-year closing range in the same pull **$107.89 to $248.61**. No split in the pull.
- **cap = close x shares**, split-invariant, `close` never `adjclose`: $222.62 x 232,575,728 = **$51.78 billion.** The
  screen's $54,483M is an earlier price on a similar count.
- **The balance sheet beside the cap (2026-06-30):** cash $4,856M; total long-term obligations including the current
  portion **$8,886M** (MD&A: *"$8.9 billion"*); **opioid settlements accrued $4.3bn** (*"we expect the majority of the
  remaining payment amounts to occur through 2038"*); total shareholders' **deficit** $(2,724)M; goodwill and other
  intangibles $13,631M.

**THE PERIMETER, read before any question.** Acquisition cash from the filed cash-flow statements, FY2012-FY2026:
**$21.9bn** (FY2013 $2,239M; FY2016 $3,614M, chiefly Cordis from Johnson & Johnson, *"$1.9 billion in October
2015"*, and 71% of naviHealth; FY2018 $6,142M, the Patient Recovery Business from Medtronic, *"$6.1 billion in
cash"*; FY2024 $1,190M; FY2025 $5,250M, ION $1.1bn, 73% of GI Alliance $2.8bn, ADS $1.0bn, Urology America $0.4bn;
FY2026 $1,991M, Solaris Health $1.9bn). **The screen's `acq_note` ($8,463M inside the five-year window, 16% of cap)
reproduces exactly** from FY2022-FY2026 (22 + 10 + 1,190 + 5,250 + 1,991).
- **What the older purchases became:** the GMPD segment's *"accumulated goodwill impairment loss was $ 5.4 billion"*
  (Note 4; $675M of it in FY2024, *"GMPD had no goodwill balance remaining as of March 31, 2024"*); Nuclear and
  Precision Health Solutions' accumulated impairment $829M; **Cordis was sold in FY2022** (proceeds from
  divestitures $923M) after being held for sale from FY2021. naviHealth was the exception: majority sold in August
  2018 for $737M plus a retained stake, the stake sold in FY2020 for a $579M pre-tax gain.
- **What the recent purchases are:** The Specialty Alliance (gastroenterology and urology management services
  organisations, *"we own approximately 76%"*) and Navista (oncology). Physicians and managers hold Specialty Alliance
  Units, liability-classified, with **$407M of unrecognised compensation cost** still to come; Navista & ION took a
  **$184M goodwill impairment in FY2026**, the year after purchase.
- **The customers who left, from the filings:** Express Scripts (contract expired 2012-09-30, $2.0bn of revenue),
  **Walgreens** (*"our second largest customer in fiscal 2013"*, expired August 2013, $16.9bn of revenue) and
  **OptumRx** (*"17 percent of our fiscal 2024 revenue"*, expired June 2024). Carried to Q2.

**Cash items that are not recurring owner earnings, found in the notes and carried to Q4:**
1. **FY2022 net cash tax refunds of $766M** (supplemental cash-flow line, *"Net cash payments/(refunds) for income
   taxes ... (766)"*), which the IRS now contests: a June 2026 Notice of Proposed Adjustment challenges *"the tax
   deductibility of self-insurance pre-tax losses and related carryback claims to fiscal 2015-2018, which could result
   in approximately $ 400 million in additional tax expense (plus interest) and approximately $ 1.4 billion in
   additional tax liability (plus interest)"*.
2. **Litigation recoveries** inside operating cash: antitrust class-action recoveries of $117M (FY2024), $171M (FY2025),
   $24M (FY2026) [E4-41].
3. **Opioid settlement payments inside operating cash from FY2022**: $798M (FY2025), $417M (FY2026); approximately
   $1.2bn paid to governmental entities through July 2023, $1.9bn through July 2024, $2.6bn through July 2026. These
   are real costs and stay in [E5-33]; the FY2020 charge itself ($5.63bn) never touched operating cash.
4. **The screen's `wc_note`, tested and refuted as a description of 2025.** It read *"ONE LINE MADE THE CASH:
   AccountsPayable moved 114% of 2025 OCF"*. The arithmetic is right (payables +$2,732M against operating cash of
   $2,397M), **but total working capital in FY2025 was a USE of $523M** (receivables -833, inventories -1,816,
   payables +2,732, unit repurchases -19, other accrued -587): payables offset most of an inventory build, and the MD&A
   names the drag, *"the impact of unwinding the negative net working capital associated with the OptumRx
   contracts"*. **The year in which working capital made the cash is FY2026** (+$1,661M in total, +$2,567M from the
   three trade lines, *"which reflects the impact of normal timing of payments to vendors"*), and FY2024 (+$1,510M).
   The line the flag names is real; its sentence says the opposite of what happened in the year it names, the MHH
   defect again.

---
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words.** Cardinal buys about $245bn a year of drugs and medical supplies and resells them
  to pharmacies, hospitals, clinics and patients, keeping **3.8%** of revenue as gross margin (FY2026) and about **1%**
  as operating earnings. In drug distribution it is paid three ways: by manufacturers, in fees *"typically ... a
  percentage of the wholesale acquisition cost that is set by manufacturers"*; by the spread on generics, bought
  through Red Oak, its sourcing venture with CVS Health, and sold at prices that fall after launch; and by its
  suppliers' credit. That last is the engine: at 2026-06-30 payables were **$38.3bn** against receivables of
  $13.8bn and inventories of $17.3bn, about **57 days** of purchases owed against about 26 days of stock and 20 days
  of receivables, so the manufacturers finance the inventory and part of the customers' credit, and revenue growth
  releases cash rather than consuming it. Around the distribution core sit a medical-products maker and distributor
  (GMPD: gloves, gowns, syringes, compression, $12.7bn of revenue, 2.0% segment margin in FY2026 including a one-time
  tariff refund), nuclear pharmacies, a home-supply business, a freight-management service, and, since FY2025,
  physician-practice management (The Specialty Alliance, Navista), bought for about $6.2bn in twelve months (ION, GI
  Alliance, Urology America, Solaris Health, December 2024 to November 2025), which
  earns management fees and ancillary revenue from gastroenterology, urology and oncology practices.
- **The scarce input this business controls:** a national network licensed to hold and ship controlled substances
  (DEA registrations, state pharmacy licences, the DSCSA traceability system, a monitored anti-diversion programme
  under the opioid settlement), a buying volume that commands manufacturer terms, and the supplier credit that volume
  earns. Whether any of it is scarce **relative to McKesson and Cencora**, which own the same things at larger scale,
  is the Q2 question.
- **Will the fundamentals look broadly the same in ten years?** The mechanism will: someone must move $250bn a year of
  manufacturers' drugs to the pharmacies, hospitals and clinics that dispense them, and the filing names two national
  competitors doing the same (*"wholesale distributors with national reach, including McKesson Corporation and
  Cencora, Inc."*). What the filing says may change is the price the compensation rides on, not the
  mechanism: *"The Inflation Reduction Act has and will continue to adversely impact our revenue by capping prices for
  certain drugs"*, the most-favoured-nation order *"may impact the sales or profitability"*, and *"If manufacturers
  change their historical approach to setting and increasing wholesale acquisition cost ... our margins could be
  adversely affected."* That is a question about bargaining power and regulation, placed at Q2 by the 2026-09-20
  ruling; it does not close Q1.
- **The physician-practice leg**, stated so Q1 is not passed on the core alone: an MSO is paid out of practices'
  revenue, most of it reimbursed by Medicare and commercial payors, and the filing names the risks as *"fraud, waste,
  and abuse laws"*, *"direct or indirect ownership of provider practices"* (Oregon has legislated against it) and the
  retention of physicians paid partly in Specialty Alliance Units. It is understandable in a paragraph; its economics
  inside Cardinal date from a 2022 minority purchase (the subject of the Department of Justice demand of November
  2023) and the purchases of FY2025-FY2026, which is a durability and capital-allocation matter, not a comprehension
  one.
- **The five-minute test [E4-46]:** the core can be stated in a paragraph and the filing confirms each clause. Nothing
  here needs months of study.
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

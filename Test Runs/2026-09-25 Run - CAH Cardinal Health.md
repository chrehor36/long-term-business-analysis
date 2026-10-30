# Company Run - Cardinal Health, Inc. (CAH) - 2026-09-25
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

*CLAIMED 2026-09-25 (write-early; no `*Run - CAH *.md` existed in `Test Runs/`). Research folder `Test Runs/_research 2026-09-25 CAH/`. WAVE 7 name 35 of 218 (line 35 of `_wave7_order.txt`; 34 lines in `_wave7_done.txt` at claim, the last being MHH). Unattended session. Sections below are filled as they close.*

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
    non-GAAP language; every Item 1.01, 5.02 and 7.01 8-K main document from 2025-08-14 to 2026-08-11 (the August 2025 notes offering, the
    364-day facility and receivables-facility amendment of October 2025, the January 2026 outlook update, the
    Chief Accounting Officer succession of March and August 2026, the chair's retirement of March 2026, the $4.0bn
    revolver of 2026-08-07, `0000721371-26-000036`). The quarterly results 8-Ks of October 2025, February 2026 and April 2026 and the
    November 2025 voting-results 8-K were not opened.
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
**$21.9bn** (FY2013 $2,239M, chiefly AssuraMed, home medical supplies; FY2016 $3,614M: The Harvard Drug Group (July
2015, generics repackaging), Cordis from Johnson & Johnson, *"$1.9 billion in October 2015"*, and 71% of naviHealth; FY2018 $6,142M, the Patient Recovery Business from Medtronic, *"$6.1 billion in
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

## Q2 - IS IT A FRANCHISE? **[E3-03]**

> *"An economic franchise arises from a product or service that: (1) is needed or desired; (2) is thought by its
> customers to have no close substitute and; (3) is not subject to price regulation. The existence of all three
> conditions will be demonstrated by a company's ability to regularly price its product or service aggressively and
> thereby to earn high rates of return on capital."* **[E3-03]**, 1991 letter

**The hypothesis I formed while reading, stated so it can be attacked [E4-26]:** *Cardinal is one of three national
drug wholesalers whose largest customers treat the three as interchangeable and move their volume among them at
contract renewal; the industry's position is strong, but the customer, not Cardinal, holds the terms, and Cardinal's
own margin has been ground down for a decade.* The evidence against it was hunted first and is set out before the
verdict; it is the strongest counter-case any Q2 in this wave has had to answer.

### The three criteria, on the registrant's own words and its competitors'

- **(1) Needed or desired: PASSES.** Revenue $254.2bn in FY2026; the drug distribution function is required for
  manufacturers to reach dispensing sites, and the filing's customers include *"retailers (including chain and
  independent drug stores ...), hospitals, and other healthcare providers"*.
- **(2) Thought by its customers to have no close substitute: FAILS, on the customers' own conduct, recorded in three
  companies' filings.**
  - **The largest customers have left for a rival, three times in twelve years.** Express Scripts' contract *"expired
    ... on September 30, 2012 ($2.0 billion)"*; Walgreens, *"which was our second largest customer in fiscal 2013"*,
    expired in August 2013 and took **$16.9bn** of revenue (10-K FY2014); OptumRx, *"17 percent of our fiscal 2024
    revenue"*, *"expired at the end of June 2024"* (10-K FY2024). **Cencora's FY2025 10-K (`0001140859-25-000131`)
    shows where two of them went:** *"In fiscal 2025, Walgreens and Boots together accounted for approximately 25% of
    revenue and Evernorth Health Services accounted for approximately 13% of revenue"* (Evernorth is the parent of
    Express Scripts).
  - **Cardinal's largest customer buys the same service from a rival at the same time.** Cardinal: *"CVS Health
    accounted for 28 percent of our fiscal 2026 revenue."* **McKesson's FY2026 10-K (`0000927653-26-000069`)**:
    *"Sales to our largest customer, CVS Health Corporation ("CVS"), accounted for approximately 24% of our total
    consolidated revenues in fiscal 2026."* One customer is the largest account of two of the three national
    wholesalers. A customer who splits its volume between two suppliers has told both that each is the other's close
    substitute.
  - **The registrant names the mechanism.** *"Consolidations create larger enterprises with greater negotiating power
    and could result in the possible loss of a customer in the situation where the combined enterprise selects one
    distributor from two incumbents"*; *"Our businesses face continued pricing pressure from these and other factors,
    which adversely affects our margins."* And in Business: *"We compete on many levels, including price ..."*, against
    *"wholesale distributors with national reach, including McKesson Corporation and Cencora, Inc., regional wholesale
    distributors, self-warehousing chains, specialty distributors, third-party logistics companies"*, and *"manufacturers
    that distribute their products directly to customers"*.
  - **The buyers are organised to buy on price.** *"our five largest customers, including CVS Health, accounted for 43
    percent"*; group purchasing organisations Vizient and Premier *"act as agents to negotiate vendor contracts on
    behalf of their members"*, **29%** of revenue. The OptumRx business *"generated a meaningfully lower operating margin
    than the overall Pharmaceutical and Specialty Solutions segment"* (10-K FY2024): the largest buyers get the thinnest
    price, which is what a buyer with a close substitute gets.
  - **Cardinal pays its largest customer.** Red Oak Sourcing, the generic-buying venture with CVS Health, began with
    *"39 quarterly payments of $25.6 million to CVS"* (10-K FY2014), was extended to June 2029 in August 2021, and *"We
    are required to make quarterly payments to CVS Health for the term of the arrangement"* (10-K FY2026, Note 7). Buffett's
    second criterion asks whether the customer thinks it has no alternative; here the supplier pays the customer to stay.
- **(3) Not subject to price regulation: PASSES narrowly on Cardinal's own fee, and the exposure is recorded.** No
  filing read regulates the wholesaler's fee directly. But the fee rides on a price that is now administered in part:
  compensation is *"typically ... a percentage of the wholesale acquisition cost that is set by manufacturers"*; *"The
  Inflation Reduction Act has and will continue to adversely impact our revenue by capping prices for certain drugs"*;
  the most-favoured-nation order *"may impact the sales or profitability"*; *"We have not experienced a negative impact to
  our profit as a result of these initiatives; however, we expect changes in manufacturer prices to continue to
  adversely impact our revenue and may, in the future, result in adverse impacts to our profitability."* The MSO leg is
  paid out of Medicare and payor reimbursement, an administered price by construction. That is [E2-59]'s regime in its
  withdrawing form, recorded as a Q4 exposure, not a criterion-3 failure.

**Checklist:** Needed or desired [x] · no close substitute [ ] **fails** · not price-regulated [x] (with the exposure above)

### [E3-03]'s demonstration clause, tested: fifteen years of margin, and the dollars that hid it

| FY | 2015 | 2016 | 2017 | 2019 | 2020 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| consolidated gross margin % | 5.57 | 5.38 | 5.03 | 4.70 | 4.49 | 3.58 | 3.35 | 3.27 | 3.67 | 3.84 |
| Pharma segment profit $M | 2,094 | 2,488 | 2,187 | 1,834 | 1,753 | 1,770 | 1,999 | 2,015 | 2,258 | 2,783 |
| Pharma segment revenue $bn | 91.1 | 109.1 | 116.5 | | | | | 210.0 | 204.6 | 234.8 |
| Pharma segment margin % | 2.30 | 2.28 | 1.88 | | | | | 0.96 | 1.10 | 1.19 |

*(Gross margin from XBRL `vintage="newest"`, checked against the filed FY2026, FY2024 and FY2017 statements;
segment profit from the MD&A tables of the 10-Ks FY2017, FY2020, FY2023 and FY2026; segment definitions moved in
FY2024, when the segment became "Pharmaceutical and Specialty Solutions", so the 2015-2017 and 2024-2026 margins are
comparable only roughly.)* **Pharmaceutical segment profit in dollars was about the same in FY2023 ($1,999M) as in
FY2015 ($2,094M), while segment revenue more than doubled; the margin on each dollar of drugs moved roughly halved.**
The FY2024-FY2026 rise to $2,783M carries the physician-practice purchases (ION, GI Alliance, Urology America,
Solaris: about $6.2bn of cash in twelve months) and GLP-1 volume, of which the MD&A says *"increased GLP-1 sales did
not meaningfully contribute to segment profit."* A business that could *"regularly price its product or service
aggressively"* would not have held its dollar profit flat for eight years while its volume doubled. **No unit series
is filed [E4-55]**; the dollar revenue is carried by manufacturers' prices, which is the flattering direction.

**The medical-products leg fails the clause outright.** GMPD segment profit **$92M (FY2024), $135M (FY2025), $258M
(FY2026, *"primarily driven by IEEPA tariff refunds"* in the fourth quarter)** on $12.4-12.7bn of revenue: 0.7%, 1.1%,
2.0%. The risk factor: *"Due to competitive dynamics and contractual limitations, passing along cost increases is
challenging"*, and it did not offset the cost increases *"in fiscal years 2024, 2025, and 2026"*. **$5.4bn of goodwill
bought into this segment (Cordis, the Patient Recovery Business) has been written off.**

### THE COMPETITOR ROW - required **[E3-28]**

**Same metric (operating margin on consolidated GAAP figures, and the distribution segment's own margin where filed),
same window (latest fiscal year and ten years earlier). The CAH row is from its filed statements; the peer rows are SEC
XBRL companyfacts, `vintage="newest"` (`peers_xbrl.txt`), flagged as transcription, except the segment margins, which
are read from the peers' 10-K text (`peers/`).**

| Company | op. margin, latest FY | op. margin, ten years earlier | gross margin latest / ten years earlier | distribution segment margin, latest FY | revenue latest FY $bn | how it enters the row |
|---|---|---|---|---|---|---|
| **Cardinal Health (CAH)** | **1.03%** (FY to 2026-06) | 2.02% (FY2016) | 3.84% / 5.38% | **Pharma 1.19%**; GMPD 2.03% | 254.2 | subject |
| McKesson (MCK) | 1.54% (FY to 2026-03) | 1.86% (FY2016) | 3.61% / 5.98% | North American Pharmaceutical **1.09%**; Medical-Surgical **8.15%** | 403.4 | named by CAH |
| Cencora (COR) | 0.82% (FY to 2025-09) | 1.04% (FY2016) | 3.57% / 2.91% | U.S. Healthcare Solutions **about 1.2%** (operating income $3,574.7M on about $291bn, from the segment cost and expense tables) | 321.3 | named by CAH |
| Medline (MDLN) | 7.78% (FY2025) | 5.38% (FY2023, first filed year) | 26.4% / 25.3% | not segmented in the row | 28.4 | named by CAH (GMPD) |
| Owens & Minor | **not obtained** | | | | | named by CAH (GMPD); the tool's ticker map returned 404 |
| regional wholesalers, self-warehousing chains, 3PLs, manufacturers shipping direct | **not obtained** | | | | | named by CAH as classes; no single filer |

- **Peers: Cardinal names 4 companies (McKesson, Cencora, Medline, Owens & Minor) plus classes; same-metric figures
  obtained for 3 of the 4.** Both McKesson and Cencora name Cardinal in turn (Cencora: *"Our largest competitors are
  McKesson Corporation ("McKesson"), Cardinal Health, Inc."*). For a moat CLAIM the missing Owens & Minor row would hold
  the class PROVISIONAL; **it does not here, because the verdict rests on the customers' conduct in three registrants'
  filings**, and Owens & Minor competes in the leg (GMPD) that fails the demonstration clause on its own figures.
- **What the row shows, including the part that cuts for Cardinal.** (i) **The three wholesalers earn the same thin
  margin on distribution**: 1.09%, about 1.2% and 1.19%; Cardinal is not the low-cost operator [E3-43], and nothing in
  the row shows a cost advantage *"both wide and sustainable"* [E2-58]. (ii) **Stated because [E4-26] requires it: every
  operating loss in the three firms' XBRL series since FY2015 is a charge, not a price war** (the opioid accruals at all
  three in FY2020-FY2021, and at Cardinal the medical-products goodwill write-downs of FY2018 and FY2022), and none has
  collapsed into the over-capacity loss years of [E2-58]'s equation; the structure has been rational. (iii) **In medical
  products Cardinal is the weak member**: GMPD at 2.0% against McKesson's Medical-Surgical at 8.15% and Medline at 7.8%.
  (iv) **The row's limit [E3-61]**: *"In some businesses, the participants behave like a demented Kellogg. In other
  businesses, they don't ... I think you'd have to know the people involved to fully understand what was happening."*
  The row shows three firms at the same margin; it cannot show whether the next CVS or GPO renewal is priced by a
  demented Kellogg.

### The remaining Q2 tests
- **[E3-46], the second question about the business, and the one that cuts hardest for Cardinal.** *"the best
  businesses, by definition, are going to be businesses that earn very high returns on capital employed over time."*
  Cardinal's operating capital is **negative**: at 2026-06-30 trade receivables $13,815M + inventories $17,297M +
  prepaid $2,764M − payables $38,283M − other accrued $3,739M = **−$8,146M** of working capital, against property of
  $3,031M. The return on tangible operating capital is not a ratio; the suppliers finance the business. **Why this does
  not carry Q2:** the negative working capital belongs to the trade position (McKesson and Cencora run the same
  structure; the payables are the manufacturers' terms for volume), and it travels with the customer: losing Walgreens
  *"favorably affected net cash provided by operating activities due to a significant reduction in net working capital"*
  in FY2014, and losing OptumRx cost cash through *"the unwinding of the negative net working capital"* in FY2025. A
  return that leaves with the account is a return on the account, not on a franchise. [E2-43]'s *"unleveraged net
  tangible assets"* is negative here, so the corpus's own denominator cannot be applied.
- **[E2-44], the two-characteristic test.** (1) *"an ability to increase prices rather easily (even when product
  demand is flat and capacity is not fully utilized) without fear of significant loss of either market share or unit
  volume"*: **fails** (three customer departures; margin halved; *"continued pricing pressure"*). (2) *"an ability to
  accommodate large dollar volume increases in business ... with only minor additional investment of capital"*:
  **passes, strongly**, on the vendor financing above. One of two.
- **[E3-33] / [E5-28], untapped pricing power: No.** Claiming it is claiming *"a monopoly or a near monopoly"*; the
  registrant's largest customer buys from a rival too.
- **[E4-37], the agony metric:** *"it's not a great business when you have to have a prayer session before you raise
  your prices a penny."* The filing on tariffs: *"if our competitors do not increase prices, or increase prices to a
  lesser extent than we do ... our competitive and financial position may be adversely affected."* On branded drugs,
  the price is the manufacturer's to set and, increasingly, the government's.
- **[E2-45], the attacker's test:** *"how I would like, assuming I had ample capital and skilled personnel, to compete
  with it."* The attackers are already inside and well funded: McKesson and Cencora took Express Scripts, Walgreens and
  a share of CVS. **Cutting for Cardinal:** no new national wholesaler appears in any document read, and the licences,
  the DSCSA traceability system and the opioid settlement's monitored anti-diversion obligations raise the cost of a
  fourth. The barrier protects the three from a fourth, not Cardinal from the other two.
- **[E2-53], the dominance class:** *"Once dominant, the newspaper itself, not the marketplace, determines just how
  good or how bad the paper will be."* No one of the three is dominant; the customer's renewal determines how good
  Cardinal's year will be.
- **[E3-62], the second step:** the gains from Cardinal's buying scale go where the customer contract puts them: the
  largest customer was paid quarterly to pool its generic buying with Cardinal, and the largest customers *"generated a
  meaningfully lower operating margin"*.
- **[E4-32], direction:** gross margin 5.57% (FY2015) to 3.84% (FY2026); pharma segment margin roughly halved; three
  large customers lost; medical products written down to no goodwill. **Direction: narrowing**, with the FY2024-FY2026
  dollar recovery bought (physician practices) rather than priced.
- **[E4-36] / [E3-51], which cause of success:** the scale of a national network is *"Extreme maximization ... of one or
  two variables"* shared by three firms; the recent growth rides the specialty-drug and GLP-1 wave, which the filing
  says adds revenue, not profit.
- **[E4-04]: not the ground.** Under the 2026-09-20 ruling it is a competence limit applied only to a name that passes
  [E3-03]; Cardinal does not. **No key-person defect is recorded [E4-23]**: the chair retired in March 2026 and the
  Chief Accounting Officer is being replaced without any change the filings attribute to one person.

### THE VERDICT, AND THE REASONING STATED SO IT CAN BE ATTACKED

**Cardinal is a large, durable, rationally competed trade position, and not a franchise.** [E3-03] asks whether the
customers think the service has no close substitute. Cardinal's customers answer by what they do: Express Scripts,
Walgreens and OptumRx each left for a rival, two of them now among Cencora's largest accounts; CVS Health, Cardinal's
largest customer at 28% of revenue, is also McKesson's largest at 24%; the group purchasing organisations negotiate on
their members' behalf; and Cardinal pays CVS quarterly under the sourcing venture. The registrant says it competes on
price and faces *"continued pricing pressure ... which adversely affects our margins"*. The demonstration clause
answers the same way: the pharmaceutical margin roughly halved over the decade and the segment's dollar profit was flat
for eight years while revenue doubled; the medical-products leg earns 0.7-2.0% and its goodwill is gone. **[E2-53]
names what is left: the customer's renewal, not the business, determines how good Cardinal's year will be.**

**The strongest evidence against the verdict, stated so the verdict can be judged against it [E4-51]:** every
operating loss the three national wholesalers filed since FY2015 was a charge (opioids, write-downs), not a price war,
and no fourth has appeared; Cardinal's operating capital is negative, so growth releases cash rather than consuming it ([E2-44]'s second
characteristic, passed strongly); segment profit rose from $1,999M to $2,783M between FY2023 and FY2026 and non-GAAP
operating earnings 30% in FY2026; the customers that left were the lowest-margin class of trade, and Cardinal's profit
rose after OptumRx went, which is what a seller who declines to buy volume at any price looks like; the manufacturers
pay Cardinal fees because they need its reach; and the IRA has not yet cut its profit. **[E3-47] warns that closing a
file wrongly is the costliest error class, and this is the name in the wave where that warning bites hardest.** I
weighed it. Every item on that list describes the position of the three wholesalers together, or Cardinal's discipline
in walking away from a price; none of it shows a customer who could not have bought the same service from McKesson or
Cencora, and the filings show many who did. [E3-43] gives the only route left, *"a business earns exceptional profits
only if it is the low-cost operator or if supply of its product or service is tight"*, and adds *"a business, unlike a
franchise, can be killed by poor management"*; the competitor row shows Cardinal is not the low-cost operator, and the
tightness is shared by three. **[E5-42] keeps the two judgments apart**: this is a question about whether the advantage
belongs to the business, and on the filings it belongs to the structure and is priced by the customer.

**Why OUT and not the perimeter close (UNKNOWABLE at Q2).** The 2026-09-20 ruling reserves UNKNOWABLE for *"A name that
passes [E3-03] and whose durability cannot be judged from filings"*. Cardinal does not pass [E3-03]: criterion (2) fails
on the customers' filed conduct, and the demonstration clause fails on fifteen years of margins. What I cannot judge is
whether the physician-practice purchases will earn their price, and I do not need to.

- **Untapped pricing power [E3-33]**: none.
- Class: [ ] WIDE [ ] NARROW **[x] NONE** [ ] PROVISIONAL · **Direction: narrowing (gross margin 5.57% to 3.84%,
  FY2015-FY2026; pharmaceutical segment margin about 2.3% to about 1.2%; three large customers lost to rivals, 2012,
  2013 and 2024; GMPD goodwill of $5.4bn written off).**
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

> **Q2 closes the file. Under the hard sequence (operator rule 2), no verdict below this point is reached and no Q5
> clearance exists.** What follows is recorded beneath the close, as the MHH, ICFI, CRUS and CVS runs did, because the
> brief asked for the owner-earnings rebuild and because a later reader deciding whether to reopen Q2 needs it. None of
> it is a verdict and none of it promotes the name.

## Q3 - ARE THEY HONEST, AND ARE THEY RATIONAL?
**VERDICT: NOT REACHED** (Q2 closed the file). *Recorded beneath the close as prompts, without a verdict. IN would
never have promoted the name; nothing here repairs Q2 [E2-37, E2-38, E3-39].*

- **Weight case, had it been declared:** **daily execution** would be ticked. A wholesaler that re-wins its largest
  accounts at each renewal, on price, is [E3-38]'s have-to-be-smart-every-day class, and [E3-43]'s *"a business,
  unlike a franchise, can be killed by poor management"* applies to a name that failed [E3-03]. **Leverage** would be
  argued: total shareholders' deficit $(2,724)M, $8.9bn of debt, $4.3bn of accrued opioid settlements, and $38.3bn of
  payables carried against $31.1bn of receivables and inventory, so a small error in terms or in a large account moves
  billions of cash [E3-29]. **Control**: none (widely held: the DEF 14A's largest holders are index and institutional managers at 6.0-7.6% each; the
  chief executive owns 61,956 shares beside 128,647 unvested units). **So Q3 would
  have been a binary gate.**
- **Conduct matters found, dated to publication, as prompts and not findings [E5-16, E5-22]:**
  - **Opioids.** The FY2020 10-K recorded a **$5.63bn** pre-tax charge; the national settlement resolved the claims of
    all 50 states *"without admitting liability"*; **$4.3bn** remains accrued with payments *"through 2038"*; the
    settlement's injunctive terms put Cardinal's anti-diversion programme under *"A monitor ... for five years from
    entry into the NOSA, until January 2028"*; about 73 private suits remain; the Fourth Circuit vacated the Cabell
    County judgment in October 2025 and a ruling on remand is pending. A settled corporate matter without an admission;
    the UMC question of 2026-09-13 (does a corporate record without identified individual accountability meet the
    honesty test?) is the same reading and is not resolved here.
  - **A Corporate Integrity Agreement** since fiscal 2022 in the Specialty business, *"in connection with an
    investigation into discounts and rebates offered or provided to certain Specialty customers"*.
  - **A Department of Justice Civil Investigative Demand of November 2023** under the Anti-Kickback Statute and False
    Claims Act, about the 2022 purchase of a rheumatology MSO stake and a GPO; *"We are cooperating"*.
  - **An FDA warning letter of April 2024** on syringes from a Chinese contract maker without *"appropriate 510(k)
    clearance"*.
  - **Cordis IVC filter settlements of $448M** for about 6,845 implantees.
  - **Absence of a found matter against a named officer in the documents read; not a finding of honesty [E5-17].**
- **[E4-22]'s first flag, weak accounting, as a prompt:** the FY2024 10-K **revised** FY2022 and FY2023 for *"an
  accounting error related to revenue recognition from third party payors within the at-Home Solutions operating
  segment"* and *"other unrelated immaterial errors, including an adjustment to an uncertain tax position"* that had
  been *"previously corrected in the periods they were identified"* and were moved back to their periods of origin.
  Disclosed, judged immaterial, not a restatement; *"There is seldom just one cockroach in the kitchen."* A Chief
  Accounting Officer succession runs from March to November 2026 (the incumbent retiring; the successor from
  Baxter), without a reported disagreement.
- **[E4-22]'s third flag and [E5-30], projections: FIRES, and the record is kept [E3-48].** The FY2027 release
  headlines *"fiscal year 2027 non-GAAP EPS guidance of 13% to 15% growth ($12.40 to $12.60), above the Company's
  long-term EPS guidance"*; the June 2025 Investor Day *"detailed ... updated long-term value creation plans"*. **The
  record of the people who made the projections**, FY2026: preliminary $9.10-$9.30 (Investor Day, June 2025), raised to
  $9.30-$9.50 (August 2025), to $9.65-$9.85, to *"at least $10.00"* (January 2026), **outturn $11.26 ($10.95 excluding
  the tariff refund)**. Beaten each time. [E3-48]'s remedy was run, and the record is good; the flag stays, because
  *"once you start it, it's all over. You can't quit"* is about the practice, not the hit rate.
- **[E4-29] EBITDA promotion: reads clean.** The word does not appear in the FY2026 10-K or the FY2026 release. **What
  the releases headline instead** is non-GAAP EPS and *"adjusted free cash flow $5.0 billion"*; the proxy defines the
  pay version of adjusted free cash flow as operating cash *"excluding settlement payments and receipts related to
  matters included in litigation (recoveries)/charges"*, which removes the opioid payments ($417M in FY2026; about
  $0.4bn a year to 2038), and non-GAAP earnings exclude the $287M of *"Acquisition-related cash and share-based
  compensation costs"*, the $361M of acquired-intangible amortization and the recurring restructuring ($175M, $88M,
  $106M in FY2024-FY2026). **[E5-33]**: *"to tell owners year after year, 'Don't count this,' when management is
  simply making business adjustments that are necessary, is misleading."* GAAP is presented first and each item is
  reconciled and tax-effected, so the half-owner test [E2-26] passes on form.
- **What pay vests on [E4-27], DEF 14A of 2026-09-21 (`0001308179-26-000402`):** the FY2026 annual cash incentive on
  *"adjusted non-GAAP operating earnings"* (target **$3,215M**, *"approximately 15% growth"*) for 60%, *"non-GAAP
  adjusted free cash flow"* for 15%, strategic objectives 15%, "Our Path Forward" 10%; the FY26-28 performance shares
  on *"the sum of adjusted non-GAAP diluted EPS CAGR and average annual dividend yield"* for 70%, adjusted free cash
  flow 20%, with a relative TSR modifier. **Prompt: every earnings measure the managers are paid on excludes the
  acquisition-related stock pay of the physician platforms their own acquisitions created, and the cash measure
  excludes the opioid payments.** The FY25-27 and FY26-28 performance shares *"assume payout at the maximum payout
  level"*.
- **[E2-56]'s camouflage test, and [E3-40] loss of focus, the sharpest prompt in the file.** $21.9bn of acquisition
  cash FY2012-FY2026 against **$6.4bn of goodwill written off** (GMPD $5.4bn, Nuclear $829M, Navista & ION $184M):
  Cordis bought for $1.9bn in October 2015 and sold in FY2022 for proceeds of $923M after being held for sale; the
  Patient Recovery Business bought for $6.1bn in July 2017 inside a segment whose goodwill is now nil; the one clean
  success, naviHealth, sold for $737M plus a stake later sold at a $579M gain. **The base business's cash carried
  repeated capital-allocation failures in medical products**, [E2-56]'s *"high-priced acquisitions of businesses that
  have inherently mediocre economics"*; the current programme (about $6.2bn of physician platforms in twelve months,
  $1.1bn of Navista written down by $184M within about fifteen months) is the next test, too young to score. **Candour
  on it is present in form** (the impairment, its discount-rate cause and its sensitivity are disclosed) **and a
  post-mortem against the announcement case [E4-39] was not found.** The [E2-30] imperative's second behaviour,
  *"acquisitions will materialize to soak up available funds"*, is a live prompt; the Elliott cooperation
  agreement (expired in the second quarter of fiscal 2025) and its board *"Business Review Committee"*, *"tasked with
  undertaking a comprehensive review of our strategy, portfolio, capital allocation framework, and operations"*, are the
  record of an outside owner pressing the same point.
- **Buybacks [E5-08]:** $2.9bn in FY2024-FY2026 by accelerated repurchase at average prices of **$88-$104 (FY2024),
  $110-$126 (FY2025) and $152-$210 (FY2026)**, and a new **$5.0bn** authorisation in August 2026. Condition one is met
  on its face (cash $4.9bn, no commercial paper outstanding at year-end). Condition two needs an IV this run did not
  reach at Q5; for the record, at the FY2024 prices the five-year owner earnings of construction A were about a 10%
  yield on the cap, and at the FY2026 prices about 5-6%. **With the humility clause [E4-13]**: *"They also know a whole
  lot more about them than I do."*
- **[E5-15] serial issuance: does not fire at the parent** (weighted basic shares 245M to 236M, FY2024-FY2026). **At
  the subsidiary it does, in a different form**: physicians and managers hold about 24% of The Specialty Alliance
  through Units, **$407M of unrecognised compensation cost** still to come; [E5-44]'s *"The intrinsic value of the
  shares you give in an acquisition must not be greater than the intrinsic value of the business you receive"* applies
  to Units given as well as cash.
- **[E4-30] cash-tax tell, as a prompt:** cash taxes against the provision, **55% (FY2024), 83% (FY2025), 72%
  (FY2026)**; FY2022 was a **net refund of $766M** from carrying opioid-related losses back to FY2015-FY2018 through the
  captive insurer, which the IRS now proposes to disallow (*"approximately $ 1.4 billion in additional tax liability
  (plus interest)"*). Not falling as a trend; the dispute is the prompt.
- **The primary test [E2-01]** cannot be run as written: shareholders' equity has been negative since at least
  FY2023 (a deficit of $(2,957)M at 2023-06-30) after buybacks, the opioid charge and the write-downs; [E2-47]'s
  carve-out for *"unusual debt-equity ratios"* applies, and [E2-43]'s net tangible assets are negative too. The
  segment-profit record above is the usable series.

## Q4 - WILL IT SURVIVE?
**VERDICT: NOT REACHED.** *The owner-earnings rebuild the brief asked for, recorded beneath the close. It is not a
verdict.*

### Owner earnings **[E2-23]**, FY2012-FY2026, from the filed cash-flow statements (seven 10-Ks, fifteen years)
*CONVENTION (framework section VI): operating cash flow less SBC, less the (c) guess.* **No net-income proxy.**

- **SBC resolves and is complete on the documents read.** Subtracted: the cash-flow line *"Share-based compensation"*,
  **$367M in FY2026 = $122M under Cardinal's own plans (restricted and performance share units; *"There were no stock
  options granted"*) + $245M under The Specialty Alliance's standalone plan** (Note 14; $238M of it inside
  *"Acquisition-related cash and share-based compensation costs"*); FY2025 $244M = $121M + $123M. The cash side of the
  physician arrangements is already inside operating cash: *"Repurchases of liability-classified Specialty Alliance
  Units"* ($45M, $19M) and the cash acquisition-related compensation. The 401(k) match ($152M in FY2026) is cash.
  **[E3-70] at grant value, recorded:** FY2026 grants of 0.6M restricted units at $158.85 and 0.5M performance units at
  $153.66 (about $172M) and 228M Specialty Alliance Units at $1.53 (about $349M) total about **$521M against the $367M
  charge**; SBC is about 7% of FY2026 operating cash, so the charge is used and the $154M gap is carried as a
  sensitivity. The screen's SBC for FY2024-FY2026 (121, 244, 367) reproduces the filed line.
- **(c) is carried as a band** [E2-09]: the **capex end** is additions to property and equipment plus *"New finance
  leases"* (Note 5: $40M FY2020 to $107M FY2025; before FY2020 the finance-lease column is not disclosed and is taken
  as nil, recorded); the **D&A end** is total D&A, which includes acquired-intangible amortization ($361M of $956M in
  FY2026). **Which end is the guess, stated from the filing:** depreciation alone (D&A less intangible amortization)
  was $595M in FY2026 against capex plus finance leases of $681M, and $246-487M against $195-654M over the fifteen
  years, so the capex end sits at or above [E3-44]'s default (*"reported earnings plus amortization of intangibles
  usually gives a pretty good indication of earning power"*). This is not the [E5-20] exception class: distribution
  centres and technology, capex guided at about $700M for FY2027. The D&A end is carried as the conservative display,
  counting some bought position as upkeep, the ICFI and MHH reasoning.
- **The working-capital construction, and why it decides the number here.** A distributor on negative working
  capital releases cash as revenue grows and as year-end payment timing falls, and gives it back when a large customer
  leaves or terms shorten. Two constructions are shown: **(A) the convention, operating cash as filed**; and **(B)
  operating cash with the three trade lines (receivables, inventories, payables) removed**, keeping *"Other accrued
  liabilities and operating items"*, which carries the opioid payments, tax timing and the Unit repurchases. (B) is the
  earning power of the trade; (A) adds the growth of the suppliers' credit. [E2-23] puts a *required* working-capital
  increment into (c); here the increment has been a SOURCE in eleven of fifteen years, the suppliers' money, which
  [E3-52]'s distinction reads correctly only if the terms are read: these liabilities are due in about 57 days and
  are set by the manufacturers, not *"liabilities without covenants or due dates"*.

| FY | OCF | SBC | D&A | capex + fin. leases | trade WC (AR+inv+AP) | other accrued | (A) capex end | (A) D&A end | (B) capex end | (B) D&A end |
|---|---|---|---|---|---|---|---|---|---|---|
| 2012 | 1,176 | 85 | 325 | 260 | -305 | -129 | 831 | 766 | 1,136 | 1,071 |
| 2013 | 1,727 | 93 | 397 | 195 | +272 | -281 | 1,439 | 1,237 | 1,167 | 965 |
| 2014 | 2,524 | 96 | 459 | 249 | +871 | -116 | 2,179 | 1,969 | 1,308 | 1,098 |
| 2015 | 2,540 | 110 | 451 | 300 | +299 | +153 | 2,130 | 1,979 | 1,831 | 1,680 |
| 2016 | 2,971 | 111 | 641 | 465 | +770 | -147 | 2,395 | 2,219 | 1,625 | 1,449 |
| 2017 | 1,184 | 96 | 717 | 387 | -774 | -493 | 701 | 371 | 1,475 | 1,145 |
| 2018 | 2,768 | 85 | 1,032 | 384 | +492 | +415 | 2,299 | 1,651 | 1,807 | 1,159 |
| 2019 | 2,722 | 82 | 1,000 | 328 | +562 | +193 | 2,312 | 1,640 | 1,750 | 1,078 |
| 2020 | 1,960 | 90 | 913 | 415 | -489 | +6,550 | 1,455 | 957 | 1,944 | 1,446 |
| 2021 | 2,429 | 89 | 783 | 445 | -163 | +452 | 1,895 | 1,557 | 2,058 | 1,720 |
| 2022 | 3,175 | 81 | 692 | 415 | +946 | +264 | 2,679 | 2,402 | 1,733 | 1,456 |
| 2023 | 2,844 | 96 | 692 | 523 | +1,454 | -997 | 2,225 | 2,056 | 771 | 602 |
| 2024 | 3,762 | 121 | 710 | 566 | +1,943 | -433 | 3,075 | 2,931 | 1,132 | 988 |
| 2025 | 2,397 | 244 | 790 | 654 | +83 | -606 | 1,499 | 1,363 | 1,416 | 1,280 |
| 2026 | 5,174 | 367 | 956 | 681 | +2,567 | -906 | 4,126 | 3,851 | 1,559 | 1,284 |

$ millions. Vintages: FY2012-14 from the 10-K FY2014, FY2015-17 from the 10-K FY2017 (FY2017 checked against the
10-K FY2019), FY2018-20 from the 10-K FY2020, FY2021 from the 10-K FY2023, FY2022-23 from the 10-K FY2024 as
**revised**, FY2024-26 from the 10-K FY2026. FY2020's +$6,550M of other accrued liabilities is the add-back of the
$5.63bn opioid accrual charged in net earnings; it nets to nothing in operating cash. Arithmetic in `oe.py` and
`oe_out.txt`.

- **MORE THAN ONE WINDOW [E4-25]:**

  | window | (A) OCF as filed | (B) trade working capital stripped |
  |---|---|---|
  | 3 years, FY2024-26 | $2.72bn to $2.90bn | $1.18bn to $1.37bn |
  | **5 years, FY2022-26 (the default [E2-42])** | **$2.52bn to $2.72bn** | **$1.12bn to $1.32bn** |
  | 5 years, FY2022-26, less the FY2022 tax refund of $766M [E4-41] | $2.37bn to $2.57bn | $0.97bn to $1.17bn |
  | 7 years, FY2020-26 | $2.16bn to $2.42bn | $1.25bn to $1.52bn |
  | 10 years, FY2017-26 | $1.88bn to $2.23bn | $1.22bn to $1.56bn |
  | 15 years, FY2012-26 | $1.80bn to $2.08bn | $1.23bn to $1.51bn |
  | 5 years, FY2017-21 (the earlier five) | $1.24bn to $1.73bn | $1.31bn to $1.81bn |
  | FY2026 alone | $3.85bn to $4.13bn | $1.28bn to $1.56bn |

  **Combined range of the multi-year means, across windows, constructions and both (c) ends: about $1.0bn to $2.9bn a
  year.** In words: **the trade itself has earned about $1.0-1.8bn a year for owners on every window since FY2012**
  (construction B), **and the growth of the suppliers' credit has added about $0.6-1.5bn a year on top in the windows ending FY2026, and
  nothing in FY2017-FY2021** (the gap to construction A), largest in the most recent windows because FY2022-FY2026 revenue rose from $181bn to $254bn and
  year-end payment timing ran in Cardinal's favour in FY2026. The screen's band ($2,503M to $2,900M) is construction A
  and **its two ends come from different windows**: the bottom is the five-year D&A end (on run.py's D&A of $734M and
  $791M for FY2024-25, against filed $710M and $790M), the top is the three-year capex-plus-leases end. **A wide
  spread is itself the finding [E4-25, E5-11]**: half the recent cash is the working-capital line, and the same line
  gave back about $2.0bn in the year a 17% customer left (total working capital +$1,510M in FY2024, -$523M in FY2025).
- **Normalise down for luck [E4-41]:** the FY2022 net tax refund ($766M, contested); antitrust recoveries ($117M,
  $171M, $24M in FY2024-26); the FY2026 IEEPA tariff refund (a $200M receivable, about $100M net in the fourth quarter,
  most of it not yet cash). **Normalise nothing up**: the opioid payments ($798M FY2025, $417M FY2026) are real costs
  and stay [E5-33]; the FY2012-FY2021 years carried none of them although the conduct they settle belongs to those years
  [E4-40], so the long windows flatter the past.
- **Great, good or gruesome [E4-20], a prompt only:** on its own capital the trade is close to [E4-20]'s great account
  in form (growth financed by suppliers) and poor in rate (about 1% of revenue, halving over the decade); **the capital
  it retained went to the gruesome account**: $21.9bn of acquisitions, $6.4bn of goodwill written off, the
  medical-products segment earning 0.7-2.0% after two purchases totalling $8.0bn. [E4-43]'s satisfactory case needs
  *"the cash they consume"* to earn a reasonable return; the filings show the older purchases did not, and the newer
  ones are unproven.
- **Staying power [E5-11], a prompt only:** (1) **earnings stream large and fairly reliable in the trade** (construction
  B positive in all fifteen years, $0.6-2.1bn), volatile in the cash timing; (2) **liquid assets**: cash $4.9bn at
  2026-06-30; the $4.0bn revolver and the commercial-paper programme are *"the kindness of strangers"* and not counted
  [E5-39]; (3) **near-term cash requirements are the killer and they are significant**: the contractual table's FY2027
  column is **$3,698M** (debt maturities $1,835M, interest $429M, opioid $403M, leases $286M, purchase obligations
  $745M), the July 2026 opioid payment of $374M, the IRS proposals (about $1.4bn plus interest, and $160M plus
  interest), the call right on the rest of GI Alliance from January 2028, and above all **$38.3bn of payables due in
  about 57 days**, rolled only as long as revenue and terms hold. **Leverage, named [E4-16]:** debt $8.9bn, opioid
  accrual $4.3bn, a shareholders' deficit of $2.7bn; covenant *"Consolidated Net Leverage Ratio ... of no greater than
  4.00 to 1.00"*. **Coverage [E2-54]:** cash interest $406M in FY2026 against construction B plus interest of about
  $1.7-2.0bn, 4-5 times; against construction A (FY2026) about 10-11 times.
- **The named way it dies [E2-27, E3-24], as a signature only:** the nearest shape in `Screens/SURVIVAL SHAPES -
  index.md` is **#6 THE BORROWED BALANCE SHEET** (*"the business runs on other people's money it must keep rolling"*,
  NEGG's supplier-credit "pendulum" at the scale of a $254bn distributor), with **#11 THE PASS-THROUGH** (the margin halved to
  the customers) and **#10 THE CAMOUFLAGE** (the trade's cash recycled into medical products, now physician practices)
  as features. **The mechanism in the filing**: a large customer leaves or re-prices at renewal, the negative working
  capital it carried unwinds, and the cash call lands in the same years as the debt, opioid and tax requirements.
  **Quantified from filed figures**: OptumRx at 17% of revenue swung total working capital by about $2.0bn in one
  year; CVS at 28% would, on the same proportion (an assumption, not a filed figure), swing about $3.3bn, against
  $4.9bn of cash and a $3.7bn FY2027 requirement column. Likelihood: **a real possibility over a decade, on exposure
  and not experience [E4-40]**: three of the largest customers left in twelve years, and the one that now matters most
  also buys from McKesson. **Not entered in the index's instances column**, for the reason the PAGP, CALM, ICFI and MHH
  folds gave: the file closed at Q2, so no Q4 death was reached. No new shape is proposed.

---
⛔ **Q5 does not open. Q2 is OUT.**

---
## Q5 - WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?
**VERDICT: NOT REACHED.** No ranking position exists; a name that failed Q2 is not ranked.

### COMPUTATION — NOT A CLEARANCE
*Arithmetic only, no box ticked, no entry language. Produced because the queue records it for every run.*
- **Yield on the $51.78bn cap:** five-year (A) $2.52-2.72bn = **4.9% to 5.3%**; five-year (B) $1.12-1.32bn = **2.2% to
  2.5%**; three-year (A) 5.2% to 5.6%; FY2026 alone (A) 7.4% to 8.0%. Sovereign **5.47%**. On enterprise value
  (cap plus debt of $8.9bn less cash of $4.9bn, about $55.8bn; the opioid accrual is not added because its payments
  are already inside operating cash), five-year (A) is 4.5% to 4.9%.
- **What the price already assumes [E4-44]:** at the ~10% floor [E4-28], a perpetual growth rate of roughly **5% a year**
  on five-year (A) (10% less a 4.9-5.3% yield) or **7.5-8% a year** on five-year (B), before net debt. The company's
  own guidance is 13-15% non-GAAP EPS growth for FY2027 alone; [E4-35]'s base rate says fewer than one in twenty of the
  most profitable companies sustain 15%.
- **At the ~10% floor with no growth:** five-year (A) capitalised at 10% is **$25-27bn**, (B) **$11-13bn**, less net
  debt of about $4.0bn: **$21-23bn and $7-9bn against a $51.8bn quote.** The quote sits above every construction on
  every window; clearing it needs construction A's recent level to grow for years, and A's recent level is half
  suppliers' credit.
- **Windage count: ONE** (construction B's removal of the trade working-capital lines); construction A, the (c) band,
  the window spread and the tax-refund sensitivity are displayed, not spent. The [E3-70] grant-value gap ($154M in
  FY2026) is a completeness sensitivity, not windage.

## Q6 - WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
**VERDICT: NOT REACHED** (nothing to sell; no position). **The reversal conditions, in words, for whoever reopens Q2**
(the QLYS ruling: a Q2 failure gets no price alert):
1. **Evidence that customers do not treat the three wholesalers as substitutes**: a run of large-account renewals
   (CVS above all, and the GPO contracts) at stable or rising margin with no share moved to McKesson or Cencora, and the
   largest customer no longer also the largest account of a rival.
2. **[E3-03]'s demonstration clause turning**: the pharmaceutical distribution margin rising for five years, organically
   (excluding acquired physician platforms), and above McKesson's North American Pharmaceutical and Cencora's U.S.
   Healthcare Solutions margins over the same years.
3. **The capital record turning**: the physician platforms earning more than their cost with no further impairment by
   FY2030, and GMPD at a medical-products margin near its named competitors' (Medline 7.8%, McKesson Medical-Surgical
   8.2%) for several years without tariff refunds.
- **The moat-downgrade question, for the record [E3-30]:** the margin compression of FY2015-FY2023 is not an
  aberrational cycle (it ran for eight years through good and bad markets); the FY2024-FY2026 recovery is partly bought
  and partly the specialty and generics mix. The first is the Q2 finding; the second is what a reopening would test.
- **Next catalyst dates:** the Q1 FY2027 release (the Q1 FY2026 release came on 2025-10-30); the Cabell County remand
  ruling; the IRS Notices of Proposed Adjustment; the end of the opioid monitor in January 2028; the GI Alliance call
  right from January 2028; the Red Oak term end in June 2029.

## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Step 0, Q1 IN, Q2 OUT; Q3-Q6 marked NOT REACHED and their
      material recorded beneath the close without verdicts.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the 10-K's own
      description of how each segment is paid, clause by clause.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives: none issued. The unobtained peer (Owens & Minor)
      is named at Q2 with the reason, and why the verdict does not rest on it.
- [x] Every UNKNOWABLE verdict states what specifically cannot be known: none issued; the perimeter close was
      considered at Q2 and refused in writing.
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked (FY2026 operating cash $5,174M
      rebuilt from its lines; ties). The screen's `wc_note` was tested against the FY2025 statement and refuted as a
      description; its `acq_note` reproduces exactly.
- [x] Owner earnings on a multi-year mean; eight windows and two constructions stated over fifteen filed years; capex
      band disclosed as a judgment, finance-lease additions included (beneath the close).
- [x] Competitor row filled: McKesson, Cencora and Medline (3 of 4 named), XBRL transcription flagged, segment margins
      from the peers' 10-K text; the verdict rests on the customers' conduct in three registrants' filings, and why is
      stated.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury par curve), dated
      09/24/2026.
- [x] Value stated as a round-number range, not a point estimate (inside a COMPUTATION block only).
- [x] One bar chosen, not both: none; Q5 not reached. Windage count stated (one).
- [x] Prices dated; aggregator used for the live quote only and flagged.
- [x] Run committed to git, with pathspecs, after the claim, after Step 0 and Q1, after Q2 and after this section.
- [x] Ledger ids: every id cited in this file was resolved against `principle_ledger.csv` (311 rows by
      `csv.DictReader`) before citing, quotes taken from `quote_verbatim` (pull saved as `ledger_rows.txt`); the count
      and the zero-phantom check are recorded in the fold commit's message and `check_out.txt`. [E4-52] is not used for
      incentives; the incentives row is [E4-27].

**The brief's priors, scored:**
- *CAH's fiscal year ends June 30; the FY2026 10-K should be the newest periodic*: **confirmed** (filed 2026-08-11,
  `0000721371-26-000038`; the cover count is as of July 31, 2026).
- *The `wc_note` "one line made the cash" may be wrong about total working capital (the MHH defect)*: **confirmed**:
  FY2025 total working capital was a $523M use; payables offset an inventory build and the OptumRx unwind.
- *acq_note: acquisitions inside the window large relative to cap; establish the perimeter*: **confirmed and
  reproduced** ($8,463M FY2022-26), extended to $21.9bn over fifteen years with $6.4bn of goodwill written off.
- *Verify SBC resolves and is complete*: **resolves and complete** ($367M = $122M + $245M from The Specialty Alliance's
  own plan; the cash side of the physician units is in operating cash); grant value about $154M higher, recorded.
- *deal_note: check for a live deal*: **none live against Cardinal**; Cardinal is an acquirer (Strive Medical completed,
  the AdaptHealth diabetes business announced, prices not in the documents read).
- *The spread caveat: the 4-construction width cannot see variation older than five years; rebuild it*: **rebuilt over
  fifteen years**; the width is dominated not by (c) but by the trade working-capital line, which the screen's
  constructions all include.

**My own errors, caught before commit:**
1. Q1's first draft said the physician platforms were bought for "about $7.4bn in eighteen months"; the filed purchases
   (ION, GI Alliance, Urology America, Solaris) are about $6.2bn in twelve months; ADS ($1.0bn) is a home-supply
   business, not a physician platform. Corrected before the Step 0/Q1 commit.
2. The perimeter's first draft described FY2016's $3,614M as "chiefly Cordis and naviHealth" and FY2013's $2,239M
   without a name; the 10-Ks name The Harvard Drug Group (July 2015) and AssuraMed (March 2013). Corrected in the Q2
   commit.
3. Q2's first draft said the three wholesalers "stayed profitable for the whole window except the opioid charges";
   Cardinal's FY2018 and FY2022 operating losses were medical-products write-downs. Corrected before the Q2 commit.
4. My first `peers.py` divided figures that `sources.annual()` already returns in millions by a further million and
   printed zeros; caught on the first read and rerun.
5. My first exhibit fetch wrote EX-99.1 and EX-99.2 of the August 2025 8-K to one filename, so the second overwrote the
   first; caught when the guidance grep returned the wrong document, refetched under distinct names.
6. A ledger dump first failed on the console's cp1252 encoding (the MHH error again); rerun with UTF-8.
7. Beneath the close, four figures in the first draft were corrected before commit: working capital a source in
   "twelve" of fifteen years (eleven); the suppliers'-credit gap "$0.5-1.6bn" ($0.6-1.5bn, and nil in FY2017-21);
   coverage on construction A "9-11 times" (10-11 on FY2026); and an unsourced "2022" date for the Elliott agreement,
   removed.

**Errors in the brief:** none found that bear on a verdict. Its counts were checked rather than inherited: the ledger is
311 rows by `csv.DictReader`, `_wave7_done.txt` held 34 lines ending MHH, line 35 of `_wave7_order.txt` is CAH and line
36 is NATH. One conflict recorded: the brief's commit trailer (*"Claude Opus 5 (1M context)"*) differs from the
session's attribution instruction (*"Claude Opus 5.5"*); the claim, Step 0/Q1 and Q2 commits carry the brief's form,
later commits the session's.

**Tooling observations (reported, not patched):**
- **`working_capital_flag()` fired "ONE LINE MADE THE CASH" on a year whose total working capital was a use** (FY2025,
  -$523M), the second run in a row to find it (MHH 2021). A check of the sign of total working capital before the
  sentence is written would stop it.
- **The screen band's two ends come from different windows again**: `oe_bottom` $2,503M is the five-year D&A end,
  `oe_top` $2,900M the three-year capex-plus-finance-lease end (reproduced in `oe.py`). The BA, ACMR, ALKT and ACVA
  defect, now on a positive band.
- **`run.py`'s D&A rule replaced a filed total with a larger component sum**: FY2024 `Depreciation` $470M +
  `AmortizationOfIntangibleAssets` $264M = $734M against the filed `DepreciationDepletionAndAmortization` of $710M
  (FY2025 $791M against $790M). The code comment says *"PREFER A FILED TOTAL; WHERE NONE EXISTS, SUM THE COMPONENTS"*;
  the code overrides the total whenever the parts are larger. Conservative direction, $24M here.
- **No construction the screen or `run.py` prints separates the trade working-capital lines**, so for a negative
  working-capital distributor every published figure is construction A, about double construction B on the recent
  windows.
- `sources.cik_for()` returned HTTP 404 for OMI (Owens & Minor); not investigated.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- One line: **CAH FAIL at Q2 (OUT, ON THE BUSINESS). Q1 IN. [E3-03] criterion (2) fails on the customers' filed
  conduct: Express Scripts (2012), Walgreens (2013, $16.9bn) and OptumRx (2024, 17% of revenue) left for rivals, two of
  them now among Cencora's largest accounts; CVS Health is the largest customer of both Cardinal (28%) and McKesson
  (24%); Cardinal pays CVS quarterly under Red Oak. The demonstration clause fails: gross margin 5.57% to 3.84%
  (FY2015-FY2026), pharmaceutical segment profit flat in dollars FY2015-FY2023 while revenue doubled, medical products
  at 0.7-2.0% with $5.4bn of goodwill written off. [E2-53]: the customer's renewal, not the business, sets how good the
  year will be.** Price $222.62 (2026-09-24, aggregator, flagged) x 232,575,728 shares (10-K cover,
  `0000721371-26-000038`) = $51.78bn; sovereign 5.47% (US Treasury, 09/24/2026).
- **If UNRESEARCHED:** not applicable.
- **If UNKNOWABLE:** not applicable.

## STEP 0 - THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** - the currently observed rate, never a forecast
**[E4-15, E3-32]**:
- rate **5.47** % · date **09/24/2026** (the newest row the curve carried when this run struck it, early on
  2026-09-25) · source (issuing authority) **US Treasury daily par yield curve, 30 Yr, `home.treasury.gov`
  daily-treasury-rates.csv for 2026**, struck fresh by this run and saved raw as
  `Test Runs/_research 2026-09-25 CVS/treasury_2026.csv`. Neighbouring rows 5.40 (09/23), 5.29 (09/22).
  **FRED DGS30 was not used.**
- FX: **not required.** CVS earns in US dollars; Item 1 describes a US business (about 9,000 US retail locations,
  CMS as the largest single customer); the Health Care Benefits segment *"also serves medical members in certain
  countries outside the U.S."*, immaterial to the currency choice. USD sovereign.

**The filing was read** - not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K for the year ended 2025-12-31, filed 2026-02-10, accession `0000064803-26-000010`**
    (`cvs-20251231.htm`). Read: the cover; Item 1 (the three operating segments, pricing, competition, the
    government-regulation summary); Item 1A in the parts cited below; Item 7 MD&A whole through Liquidity (the
    segment reconciliations, each segment's table and commentary, Trends and Uncertainties, cash flows, store
    development); the balance sheet, the cash-flow statement with its reconciliation lines, and the notes cited
    (Note 1 Subsidiary Bankruptcy, Note 6 goodwill, Note 18 legal matters, Note 19 segments).
  - **10-K FY2024 `0000064803-25-000007`, 10-K FY2022 `0000064803-23-000009`, 10-K FY2019 `0000064803-20-000007`,
    and the FY2017 10-K's Exhibit 13 annual report `0001558370-18-000707`** for the long series (each carries three
    years, so 2015-2025 is covered without a gap).
  - **10-Q for the quarter ended 2026-06-30, filed 2026-08-05, accession `0000064803-26-000098`** (cover, legal
    matters, trends).
  - **8-K EX-99.1 earnings releases**: Q1 2024 (`0000064803-24-000015`), Q2 2024 (`0000064803-24-000028`), Q4 2024
    (`0000064803-25-000006`), Q4 2025 (`0000064803-26-000009`), Q1 2026 (`0000064803-26-000051`), **Q2 2026
    (`0000064803-26-000097`, 2026-08-05, the latest)**; and the 8-Ks of 2024-10-18 (`0001193125-24-239193`, CEO
    change and guidance withdrawal), 2024-11-18 (`0001193125-24-260405`, the Glenview agreement), 2026-03-18
    (`0000064803-26-000017`), 2026-08-17 (`0001193125-26-354096`).
- figure cross-checked against the filed statement (say which): **2025 net cash provided by operating activities,
  $10,639M** (Consolidated Statements of Cash Flows, 10-K p. 96-97), rebuilt from its own reconciliation lines: net
  income 1,728 + D&A 4,606 + goodwill impairment 5,725 + stock-based compensation 535 + loss on sale of subsidiary
  236 - gain on deconsolidation 483 + deferred taxes 102 - other items 336 - receivables 3,498 - inventories 1,267 -
  other assets 2,593 + accounts payable and pharmacy claims 3,855 + health care costs payable 16 + other liabilities
  2,013 = **10,639. Ties**, and ties to the direct-method total above it on the same page.
- *If the filing could not be obtained -> **UNRESEARCHED**.* **Not invoked; every document came from SEC EDGAR
  primary documents (submissions pull saved as `subs.json`).**

**THE PRICE AND THE CAP** *(struck by this run, not carried from the screen)*
- **Share count, quoted from the cover of the 10-Q for 2026-06-30, accession `0000064803-26-000098`:** *"As of July
  29, 2026, the registrant had 1,278,970,369 shares of common stock issued and outstanding."* One class registered
  (*"Common Stock, par value $0.01 per share | CVS | New York Stock Exchange"*); the balance sheet reads *"Preferred
  stock, par value $ 0.01 : 0.1 shares authorized; none issued or outstanding"*. No classes summed. The FY2025 10-K
  cover gave 1,272,211,063 at 2026-02-04, so the count has risen 0.5% in six months (no buyback in 2025; option
  exercises and awards).
- **Price $85.05** (close 2026-09-24, **aggregator quote, flagged**: Yahoo Finance chart endpoint,
  `regularMarketTime` 2026-09-24 20:00 UTC; raw response saved as `price_raw.json`). Two-year closing range in the
  same pull $43.78 to $110.60; the price has fallen every session since 2026-09-15 ($94.49).
- **cap = close x shares**, split-invariant, `close` never `adjclose`: $85.05 x 1,278,970,369 = **$108,776 million.**
- The screen's $119,238M implies about $93.2 a share on the same count, a price of mid-September; no flag to
  resolve. The FY2025 10-K cover's non-affiliate float, *"approximately $ 86,382,523,283 as of June 30, 2025"*, was
  struck at a lower price a year earlier and is consistent.

**THE PERIMETER, read before anything else. It has moved more than the screen's five-year note can see
[E4-25].**
1. **Aetna, 2018**: *"On November 28, 2018 [...] the Company acquired Aetna Inc. ("Aetna") for a combination of cash
   and CVS Health stock"* (FY2019 10-K); *"Acquisitions (net of cash acquired)"* **$(42,226)M** in 2018 (FY2019 10-K cash-flow
   statement), funded by **$44,343M of new long-term debt** the same year. Everything before 2019 is a different
   company: 2017 insurance benefits paid were $2,810M against $121,238M in 2025.
2. **Signify Health and Oak Street Health, 2023**: acquisitions net of cash **$(16,612)M** in 2023. Both sit in the
   Health Services segment's Health Care Delivery reporting unit, **which took a $5.7bn goodwill impairment in
   Q3 2025**; *"the remaining goodwill balance in the Health Care Delivery reporting unit was approximately $4.2
   billion"* and *"it is reasonably possible in the near term that the goodwill of the Health Care Delivery
   reporting unit could be deemed to be impaired again by a material amount."* Earlier impairments: $6,149M in 2018
   and $181M in 2017 (LTC), $431M in 2021.
3. **Omnicare (long-term-care pharmacy, bought 2015) deconsolidated 2025-09-22**: *"Omnicare, LLC [...] and certain
   of Omnicare's subsidiary entities [...] voluntarily initiated Chapter 11 proceedings"*, after a False Claims Act
   judgment against Omnicare ($387M + $542M charges in 2025). Gain on deconsolidation $483M.
4. **Exits and closures**: Public Exchange business exited effective January 2026; Medicare Shared Savings
   Program operations sold March 2025; stores 9,674 at the start of 2023 to 9,135 at the start of 2025, **243
   closed and 87 opened or acquired in 2025**; Rite Aid prescription files bought in 2025.
5. **The screen's working-capital flag, recorded now and resolved at Q4**: the accounts-payable-and-pharmacy-claims
   line did add **$3,855M, 36.2% of 2025 operating cash**. The flag is arithmetically right. But receivables took
   out $3,498M and other assets $2,593M in the same year; **the working-capital lines together were a net USE of
   $1,474M in 2025**, so operating cash was not made by the payables line.

**STAGE 0(b) OF THE SECTOR METHOD - is CVS an insurer, a float-bearing holding company, or neither? Decided from
the filing, before Q1.** *(The brief asked for this reasoning to be written down; the sector method requires it,
`Framework/SECTOR METHOD - owner earnings for insurers ...`, Stage 0(b).)*
- **The facts, FY2025 10-K.** Premiums were **$134,751M of $402,067M revenue (33.5%)**; the Health Care Benefits
  segment earned **$2,939M of $14,443M adjusted operating income (20.3%)**, and in 2024 **$307M of $11,976M
  (2.6%)**. Investments: **$2,145M current + $32,669M long-term = $34,814M**. Insurance liabilities: health care
  costs payable **$15,399M** + other insurance liabilities **$1,116M** + other long-term insurance liabilities
  **$4,716M** = **$21,231M**. Shareholders' equity **$75,382M**.
- **The two ratios the method asks for, computed and stated, neither a threshold.** Insurance liabilities to
  investments **61%** (Berkshire at [E5-46]'s test 41.8%); investments to equity **0.46x** (Berkshire 0.45x in the
  method's CONVENTION 5). **On those two ratios alone CVS would look like the method's subject.** It is not, for
  three reasons from the filing:
  1. **The float is short.** Q2 2026 release: *"Days claims payable were 41.7 days as of June 30, 2026"*. Health
     claims are paid in weeks; the money is not held for years as [E5-46]'s float is, and the method's cost-of-float
     test **[E3-69]** needs *"a period of years"* of float that is actually carried.
  2. **The portfolio is not the principal asset, and it is not free to the owner.** Net investment income was
     **$2,233M, 0.6% of revenue**; the rest of the value is three operating businesses. And *"approximately $8.5
     billion in cash and cash equivalents, approximately $2.8 billion of which was held by the parent company or
     nonrestricted subsidiaries"*: most of the liquid assets sit behind insurance regulation.
  3. **Product (drug) sales are $249,908M, 62% of revenue, and the PBM and the stores earn $13,191M of the $16,130M
     of segment adjusted operating income before corporate costs (82%)**, where the ordinary owner-earnings method
     applies.
- **RULING: CVS is an operating company that owns a health insurer; for the method it is "neither", and the
  ordinary owner-earnings method governs** *(Stage 0(b): "Say which, and take the ordinary method if so")*. **Three
  corrections from the sector method still bind, and are carried to Q4:** (i) **[E5-48]'s anti-double-counting
  rule**: net investment income is already inside operating cash, so the $34.8bn portfolio is **never** added to an
  owner-earnings value; (ii) **[E2-61]**, broke-but-flush: for the insurer part, liquidity is read as reserve
  adequacy and statutory capital, never cash on hand, and growth in health-care-costs-payable is borrowed money
  that reverses (the UNH run's treatment, 2026-08-31, which stripped float growth from operating cash); (iii) the
  reserve-development read as the candor test **[E2-67]** belongs at Q3/Q4. **[E2-70]**'s warning, that an insurer's
  *"only products are promises"*, applies to the Health Care Benefits segment at Q2. *(CONVENTION 3 of the sector
  method, "value separately", is not invoked: its rationale is a finance book whose cash flows run the opposite
  way to the operating business's, and CVS's insurer and PBM are not separable that way; the segments trade with
  each other, $71,563M of intersegment revenue eliminated in 2025. Recorded, not applied.)* **[E5-37]**: *"different
  numbers are of different importance [...] depending on the kind of business"* is the general rule this applies.

---
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words, no management language.** CVS is three businesses that sell to each other.
  **First, a pharmacy benefit manager (Caremark, in the Health Services segment).** Employers, health plans and
  government programs hire it to run their prescription-drug benefit. It sets the list of drugs the plan will pay
  for, negotiates what drug makers pay back to be on that list, contracts with retail pharmacies on what they are
  paid per prescription, and runs its own mail and specialty pharmacies. It books the whole drug cost as revenue
  and keeps a thin slice: **1,900.7 million 30-day-equivalent claims in 2025, $190,425M of segment revenue, $7,151M
  of adjusted operating income, 3.8 cents on the revenue dollar and about $3.76 a claim.** Its money comes from
  the difference between what the client pays and what the pharmacy and the drug maker net out, from the share of
  manufacturer rebates it keeps, from administrative fees, and from dispensing margin on mail and specialty drugs.
  **Second, a health insurer (Aetna, the Health Care Benefits segment).** It takes a fixed premium per member per
  month, from CMS for **4.27 million Medicare Advantage members** and 4.04 million stand-alone Part D members, from
  states for 2.3 million Medicaid members, and from employers, and pays whatever care those members consume; for
  **15.7 million more** it only administers, for a fee. In 2025: **premiums $134,749M, health care costs $122,949M,
  MBR 91.2%**, operating expenses 13.0% of revenue, **adjusted operating income $2,939M, 2.1% of revenue** (0.2% in
  2024). **Third, a drugstore chain (CVS Pharmacy, the Pharmacy & Consumer Wellness segment).** About 9,000 stores
  fill prescriptions (**1,808.8 million in 2025**) at a reimbursement set by whichever PBM or plan the customer
  belongs to, and sell front-store goods (**$21,459M**, flat for three years). Pharmacy revenue **$115,510M**; the
  segment earned **$6,040M adjusted, 4.3%**, about **$3.34 a prescription**. **The three trade with each other:**
  Caremark's network includes CVS stores; Aetna's pharmacy benefit runs through Caremark; the stores fill Caremark's
  mail and specialty orders. **$71,563M of 2025 revenue (17.8% of the consolidated total) is intersegment and
  eliminated**, so every segment margin depends partly on internal transfer prices. What the whole employs:
  **$2.8bn a year of capex (77% of it technology), $13.1bn of property, $15.0bn of leased stores, and $111.0bn of
  goodwill and intangibles** against **$75.4bn of equity**, so tangible equity is about **minus $35.6bn**; plus
  **$64.6bn of debt**. Consolidated 2025: revenue $402,067M; adjusted operating income $14,443M; GAAP operating
  income $4,660M after a $5,725M goodwill impairment and $1,220M of *"legacy litigation charges"*.
- **The scarce input this business controls: volume.** Caremark directs the drug spend of about 87 million plan
  members, which is what makes drug makers pay rebates and pharmacies accept its rates; Aetna directs the care of
  26.6 million medical members, which is what makes hospitals and physicians accept its rates; and the stores
  hold a location within reach of most Americans, which is what makes a PBM want them in its network. **None of
  the three is a scarce asset in the sense of a trademark or a licence**: the input is scale, and Q2 must test
  whether scale holds against the customer.
- **Will the fundamentals look broadly the same in ten years?** **The mechanisms yes; the terms no, and the filing
  says the terms are moving.** Someone will still pool medical risk, someone will still run drug benefits, and
  people will still collect prescriptions. What the 10-K lists as live change is the price-setting itself:
  *"The Company continues to share with clients a larger portion of rebates, fees and/or discounts received from
  pharmaceutical manufacturers [...] marketplace dynamics and regulatory changes have limited the Company's ability
  to offer plan sponsors pricing that includes retail network 'differential' or 'spread.' The Company expects these
  trends to continue"*; *"Legislation and/or regulations seeking to regulate PBM activities in a comprehensive
  manner have been proposed or enacted in a majority of states and on the federal level"*, and in the June 2026
  10-Q, *"some states have recently enacted or are considering legislation related to prohibiting pharmacy
  licensure for pharmacies affiliated with a PBM"*; the 2027 Medicare Advantage advance notice at *"0.09%"*; and
  the stores' own move: *"CVS Pharmacy successfully completed the transition to cost-based reimbursement"* (Q4 2025
  release). **That is the substance of Q2, recorded here.**
- **[E4-46] check, and it is the closest call in this Q1.** *"if we can't make a decision in five minutes, we can't
  make it in five months."* **The case for Q1 OUT, stated as strongly as I can:** [E3-31] asks for businesses
  *"relatively simple and stable in character"*, and *"If a business is complex or subject to constant change, we're
  not smart enough to predict future cash flows."* CVS is three businesses whose reported margins rest on transfer
  prices across $71.6bn of eliminated revenue; whose PBM economics turn on rebate and spread terms the filing does
  not quantify; whose insurer's earnings are an actuarial estimate that moved adjusted operating income from
  $5,577M to $307M in one year; whose perimeter has taken in about $61bn of cash acquisitions since 2018 (2018-2025 cash-flow lines) and
  written off about $12.3bn of goodwill (2018, 2021, 2025); and whose own management withdrew its guidance in October 2024 after cutting it in May
  and again in August. **The ruling, and the reason.** [E4-46]'s test is whether the decision needs months of study,
  not whether the company is large. The mechanism above was written from one 10-K, its predecessors' segment
  tables and one quarter's release; each segment's economics are disclosed with volume and margin; the question
  the business turns on, whether its volume commands price, is answerable from the segment series and the
  competitors' filings at Q2. **What the complexity destroys is my ability to estimate what CVS will earn, which is
  [E5-34]'s separate test and lives at Q4/Q5; it does not destroy my ability to say how it makes money.** This is
  the ruling the UNH run of 2026-08-31 made on the same shape of business, and I have tested it here rather than
  inherited it: the two differ (CVS adds a drugstore chain and a larger PBM share), and neither difference is one I
  cannot describe. **Ruling Q1 IN is not a claim that the earnings are forecastable, and no later gate may borrow
  that claim.**
- **VERDICT: [x] IN**


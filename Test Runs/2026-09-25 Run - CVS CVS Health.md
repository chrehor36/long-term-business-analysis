# Company Run - CVS Health Corporation (CVS) - 2026-09-25
**CIK 0000064803. NYSE. Fiscal year ends 31 December. WAVE 7, name 31 of 218 by the order file
(`Screens/_daily/_wave7_order.txt` line 31; `_wave7_done.txt` held 30 lines, the last CLX, when this run started;
both counted by this run, not carried from the brief). Not on the 45-name financial held-out list. Name claimed at
dispatch (commit `d9e33c8`; no `*Run - CVS *.md` existed in `Test Runs/`). Run unattended overnight, 2026-09-25.
Research folder: `Test Runs/_research 2026-09-25 CVS/`. Peer filings reused from the UNH run's folder
(`Test Runs/_research 2026-08-26/`: the FY2025 10-Ks of UNH, CI, ELV, HUM, CNC), with the figures used re-read from
those filings by this run.**

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

## Q2 - IS IT A FRANCHISE? **[E3-03]**

**The question, posed plainly: does CVS's volume let it set its price against the customer, in any of its three
businesses, or does the customer (CMS, the PBM client, the payer) set the price and CVS earn a spread inside it?**
The answer this run reaches is the second, in all three, and the evidence is the registrant's own words about who
takes the price, the unit series, and three competitor rows. Worked below.

**[E3-03], the three criteria, business by business:**

- **Needed or desired: [x] YES** in all three. Health cover, drug benefits and prescriptions are not
  discretionary; the federal government alone is *"approximately 20% of the Company's consolidated total
  revenues"*.
- **No close substitute: [ ] FAILS in all three, in the registrant's own words and in its own unit series.**
  - **PBM**: *"PBM clients are generally well informed, can move between us and our competitors and often seek
    competing bids prior to expiration of their contracts. We are therefore under pressure to contain price
    increases despite being faced with increasing drug costs and increasing operating costs"* (10-K FY2025, Item
    1A). **And a client proved it: claims processed fell 18.2% in 2024, 2,344.3M to 1,917.6M, *"primarily driven
    by the previously announced loss of a large client"***, while Cigna's Pharmacy Benefit Services claims rose
    1,585M to 2,120M, Cigna's 10-K recording that *"Express Scripts and Centene Corporation ("Centene") have a
    multiyear agreement, which began January 1, 2024"*. **CVS does not name the client; the timing and the two claim
    series fit one contract moving most of a fifth of Caremark's volume to a named competitor in one renewal.** Item 1 names the substitutes: *"large, national PBM companies (e.g., Prime
    Therapeutics and MedImpact), PBMs owned by large national health plans (e.g., the Express Scripts business of
    Cigna Corporation and the Optum Rx business of UnitedHealth Group) and smaller standalone PBMs."*
  - **Insurer**: *"we must often bid against our competitors in a highly competitive environment to acquire and
    retain our government customers' business"*; the Medicare member re-chooses every autumn. **The insured book
    fell from 12,514k members (2024) to 9,829k (June 2026), minus 21%, and stand-alone PDP from 6,081k (2023) to
    3,870k, minus 36%**, as CVS repriced and exited the exchanges.
  - **Stores**: *"The retail pharmacy business is highly competitive [...] the Company competes with other drugstore
    chains (e.g., Walgreens), supermarkets, discount retailers (e.g., Walmart), independent pharmacies, restrictive
    pharmacy networks, online retailers (e.g., Amazon), membership clubs, infusion pharmacies, as well as mail
    order dispensing pharmacies"*; and the customer's plan, not the customer, chooses the network.
- **Not subject to price regulation: [ ] FAILS for the insurer outright; for the PBM and the stores the price is
  set by the counterparty, and increasingly by statute.**
  - Insurer: CMS pays *"a fixed per member (or "capitation") payment"*, *"subject to annual revision by CMS"*; *"the
    ACA requires minimum MLRs for Medicare Advantage and Medicare Part D plans of 85%. If a Medicare Advantage or
    Medicare Part D contract pays minimum MLR rebates for three consecutive years, it will become ineligible to
    enroll new members"*; commercial premium rates are, *"Where required by state laws, [...] filed and approved by
    state regulators"*; the 2027 advance notice was *"0.09%"* before risk-score trend.
  - PBM: *"Legislation and/or regulations seeking to regulate PBM activities in a comprehensive manner have been
    proposed or enacted in a majority of states and on the federal level"*, and some states are *"prohibiting
    pharmacy licensure for pharmacies affiliated with a PBM"* (10-Q Q2 2026). In July 2026 *"the Company and the
    FTC announced a proposed settlement agreement that would resolve all of the FTC's outstanding investigations
    related to the Company's PBM and affiliated pharmacy businesses, including rebate, pharmacy network, contract,
    and vertical integration issues"* (terms not in the filings read; recorded as a live regulatory change to the
    terms of trade, not scored).
  - Stores: *"Substantially all of the Pharmacy & Consumer Wellness segment's pharmacy revenues are derived from
    pharmacy benefit managers, managed care organizations ("MCOs"), government funded health care programs,
    commercial employers and other third-party payors"*: the price of the product is the payer's reimbursement.

**Score: one of three, in every one of the three businesses. [E3-03] is not met.**

### The separating tests

- **[E2-44], the two-characteristic test: the pricing half fails in the registrant's own words, every year the
  series was read.** Characteristic (1) is *"an ability to increase prices rather easily [...] without fear of
  significant loss of either market share or unit volume"*. CVS's filings say the opposite, and say it as a
  standing condition: *"If we are unable to limit our price increases, we may lose customers to competitors with
  more favorable pricing"* (Item 1A, stated identically for the PBM and for the stores). The PBM's price moves
  **toward the client every year**: *"continued price compression"* (10-K FY2017, FY2019); *"continued pharmacy
  client price improvements"* (FY2022, FY2024, FY2025, and the Q2 2026 release); *"The Company continues to share
  with clients a larger portion of rebates, fees and/or discounts received from pharmaceutical manufacturers, and
  typically offers clients minimum pricing guarantees that cannot always be achieved"* (FY2025, Trends). The
  stores: *"reimbursement pressure"* is named in every 10-K read (FY2017, FY2019, FY2022, FY2024, FY2025), in
  FY2025 as *"continued pharmacy reimbursement pressure"*.
  The insurer: priced up for 2025-26 and **lost 21% of its insured members** (above). Characteristic (2),
  capital-light growth: **half yes**. Capex is 0.7% of revenue; but the growth was bought: **about $61bn of cash
  acquisitions 2018-2025**, leaving **$111.0bn of goodwill and intangibles against $75.4bn of equity**.
- **[E3-62], the second step, is the clearest read of the PBM.** *"All of the advantages from great improvements
  are going to flow through to the customers."* The PBM's own explanation of its segment result, year after year,
  is a give and a take: 2024, adjusted operating income down *"primarily driven by continued pharmacy client price
  improvements and the previously announced loss of a large client. These decreases were largely offset by
  improved purchasing economics"*; 2025, *"continued pharmacy client price improvements [...] partially offset by
  improved purchasing economics and pharmacy drug mix."* What it wins from drug makers and pharmacies (purchasing
  economics) it hands to clients (price improvements). **The margin is the residue of a two-sided negotiation it
  does not control, not a price it sets.** Segment adjusted operating income has been **$7,356M, $7,312M, $7,243M,
  $7,151M** (2022-2025) in nominal dollars, and since 2023 that figure includes the Health Care Delivery assets
  bought for $16.6bn.
- **[E4-55], units, the honest series.** **PBM claims**: 2,344.3M (2023) to 1,900.7M (2025), minus 19%; H1 2026
  flat (937.7M against 933.2M). **Insured medical members** minus 21% since 2024; **Medicare Advantage** 4,447k to
  4,202k. **Stores**: prescriptions rose (1,230.5M in 2017 to 1,808.8M in 2025, partly bought: *"incremental volume
  resulting from the Company's Rite Aid prescription file acquisitions"*), **but adjusted operating income per
  prescription fell from $6.07 (2017) to $3.34 (2025), minus 45%**, and front-store sales are flat at about $21.5bn
  while the store count fell from 9,674 (start of 2023) toward 9,000. **More units at a falling unit price is
  [E4-55]'s shape run in reverse: the volume held and the price went.**
- **[E4-47], nominal earning power.** Consolidated adjusted operating income **$15,339M (2019), $16,008M, $17,312M,
  $17,532M, $17,534M (2023), $11,976M (2024), $14,443M (2025)**. 2025 is below 2019 in nominal dollars, after
  $18.3bn more of cash acquisitions (2020-2025 cash-flow lines). H1 2026 ($10,307M against $8,387M) is a recovery, recorded
  in the bull case below.
- **[E3-46], the second question about the business, is a number, and it is ordinary.** 2025 adjusted operating
  income of $14,443M, pre-tax, on shareholders' equity plus debt of about $139.9bn ($75,382M + $64,570M) is about
  **10.3%**; at the 2019-2023 peak of about $17.5bn it would be about 12.5%. The capital employed is mostly goodwill
  the owners paid for; *"the best businesses, by definition, are going to be businesses that earn very high
  returns on capital employed over time"*. Recorded as evidence, not as a verdict on its own.
- **[E2-53], the dominance class. FAILS.** CVS has about 9,000 stores (Walgreens 8,572 at its last 10-K), is one of *"the three largest PBMs (the "PBM
  Group")"* the FTC sued (10-Q Q2 2026), and insures more than 37 million people. In 2024 its insurer's adjusted
  operating income fell **from $5,577M to $307M**, the retail segment's per-script earnings fell for the seventh
  year of eight (2017-2025), and the PBM lost a fifth of its claims. **Size did not determine how good or bad the year would
  be; CMS, a client's re-bid and the payers did.**
- **[E2-45], the attacker's test, and its answer is on file.** With ample capital and skilled people, how would I
  compete with Caremark? **Cigna's Express Scripts already did: its Centene agreement began in January 2024, the year Caremark's claims fell
  426.7 million "primarily driven by the previously announced loss of a large client".** Against Aetna: bid
  a lower Medicare Advantage premium one autumn; the member moves at zero cost. Against the stores: be the PBM, and
  set their reimbursement. The 10-K adds a new attacker class: *"Direct-to-consumer ("DTC") sales of prescription
  drugs by pharmaceutical companies [...] bypassing traditional distribution channels and intermediaries,
  including pharmacies and PBMs."*
- **[E4-32], direction, which outranks existence: NARROWING on every series with units.** PBM claims minus 19%;
  insured members minus 21%; PDP minus 36%; retail earnings per script minus 45% since 2017; stores down; the
  insurer's MBR the worst of six filers in 2024 and second-worst in 2025 (row below). The one widening series is
  the PBM's earnings per claim (about $2.60 in 2017 to about $3.76 in 2025, with a definitional break in 2023),
  which the second-step read above explains as specialty mix and purchasing, handed back to clients the next
  year.
- **[E4-36] / [E3-51], which cause of success?** Not an extreme of one variable, not a nonlinear combination. The
  record's best years (2020-2023) came from **riding waves CVS did not make**: pandemic testing and vaccination
  (*"lower contributions from COVID-19 over-the-counter ("OTC") test kits since the expiration of the public health
  emergency"*, FY2024), and the Medicare Advantage and generic-drug waves. *"if he gets off the wave, he becomes
  mired in shallows."* A surfing run is not a moat.
- **[E3-33] / [E5-28], untapped pricing power: NOT CLAIMED, and the scope rule forbids it.** Claiming it is
  claiming *"a monopoly or a near monopoly"*; the filing names four PBM competitors plus *"smaller standalone PBMs"*,
  nine kinds of pharmacy competitor, and a competitive bid for every government contract.
- **[E2-58] / [E2-59].** The insurer is the [E2-59] case, *"legally through government intervention"*: the regime
  sets the price and caps the retained margin by the 85% MLR; the UNH run of 2026-08-31 worked the same regime to
  the same result. The PBM and the stores are closer to [E2-58]'s commodity equation with a cost-advantage
  exception to test: **is CVS's cost position "both wide and sustainable"?** The row says it is wider than
  Walgreens' and not sustainable: its own per-script earnings fell 45% in eight years.
- **[E2-70], the insurer's own warning.** *"Their only products are promises. It is not difficult to be licensed,
  and rates are an open book."* Aetna's product is the ordinary one, which is why its MBR moved with the whole row.

### THE COMPETITOR ROWS - required **[E3-28]**. Full transcription with sources and limits:
`Test Runs/_research 2026-09-25 CVS/PEER_ROWS.md`. Every figure read by this run from the filing named; no sub-agent.

**A. The insurer, medical/benefit cost ratio, same metric, calendar years, each issuer's own 10-K:**

| | FY2023 | FY2024 | FY2025 | change 23-25 |
|---|---|---|---|---|
| **CVS Health Care Benefits (MBR)** | **86.2%** | **92.5%** | **91.2%** | **+500bp** |
| UnitedHealth (MCR) | 83.2% | 85.5% | 89.1% | +590bp |
| Elevance (benefit expense ratio) | 87.0% | 88.5% | 90.0% | +300bp |
| Humana (benefit ratio) | 87.3% | 89.8% | 90.2% | +290bp |
| Cigna Healthcare (MCR) | 81.3% | 83.2% | 84.4% | +310bp (Medicare sold 2025-03-19) |
| Centene (HBR) | 87.7% | 88.3% | 91.9% | +420bp |

Six filers, five business models, one direction. **CVS was the worst of the six in 2024 and second-worst in 2025**;
its adjusted segment margin went 5.3% to 0.2% to 2.1%. H1 2026 MBR 86.0% against 88.6%, the recovery, with *"Prior
years' health care costs payable estimates developed favorably by $1.2 billion during the six months"*.

**B. The PBM, claims and segment income (three filers, three counting bases; direction and order, not a per-claim
ranking):**

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| **CVS Health Services: claims (M) / adj. op. income ($M, margin)** | **2,344.3 / 7,312 (3.9%)** | **1,917.6 / 7,243 (4.2%)** | **1,900.7 / 7,151 (3.8%)** |
| Cigna Evernorth Pharmacy Benefit Services: claims (M) / pre-tax adj. income ($M, margin on adj. revenue) | 1,585 / 3,469 (4.5%) | 2,120 / 3,577 (3.2%) | 2,222 / 3,506 (2.7%) |
| UnitedHealth Optum Rx: adjusted scripts (M) / earnings from operations ($M, margin) | not in the file read / 5,115 (4.4%) | 1,623 / 5,836 (4.4%) | 1,659 / 7,193 (4.6%) |

**C. The drugstore, adjusted operating income per 30-day prescription, each company's own segment disclosure:**

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| **CVS retail (Retail/LTC, then PCW)** | **$4.73** | **$4.19** | **$4.80** | **$4.13** | **$3.62** | **$3.37** | **$3.34** |
| Walgreens U.S. Retail Pharmacy (fiscal Aug.) | $5.11 | $4.09 | $4.15 | $4.13 | $3.04 | $1.77 | delisted 2025-08-28 |

- **Peers named: 5 insurers (all the listed national full-line competitors; Blues plans and Kaiser file no 10-K),
  2 PBMs (the other two of the three the FTC named; Prime and MedImpact are private, which is the row's boundary),
  1 drugstore chain (Walgreens, the only other listed national chain until its 2025 take-private; Rite Aid was not
  pulled; Walmart, Kroger and Amazon do not segment pharmacy).** No peer the verdict depends on is missing, so
  the class is not PROVISIONAL.
- **The row's limit [E3-61]:** it shows position, not conduct. It cannot say whether the three PBMs will price
  rationally under the new state laws and the FTC settlement, and the corpus says even Munger had no model for
  that.
- **What the rows say.** (A) the insurer's economics moved with the regime, and CVS's moved the most; (B) the PBM
  business is an oligopoly of three in which the largest client can move a fifth of a leader's volume in one
  renewal, and whose margins run 2.7% to 4.6% of the drug dollar at all three; (C) the drugstore's price is set
  by its payers, and **CVS's lead over Walgreens is real (it lost less) and it is not a lead in direction: CVS's
  earnings per script fell in five of six years 2019-2025, Walgreens' in four of five FY2019-FY2024.**

### The integration claim, tested rather than accepted
The strongest bull argument is that CVS is the only company that owns all three (insurer, PBM, stores), so each
steers volume to the others and the whole is harder to displace than any part. Two filed facts limit what an
outsider can conclude. **$71,563M of 2025 revenue is intersegment and eliminated**, so each segment's margin rests
partly on transfer prices CVS sets. And **the integration did not protect any part when it mattered**: Aetna's MBR
moved with an unintegrated field; Caremark lost its largest client to a competitor that owns no drugstore; the
stores' earnings per script fell with Walgreens', which owns no PBM. Integration is a real feature of the
business; the rows do not show it to be a moat.

### THE IRON PRESCRIPTION **[E4-51]**: the bull case, stated in the form its holders would accept

> **The case for CVS, fairly stated.** CVS owns the most complete set of positions in American pharmacy and health
> benefits: about 9,000 stores (Walgreens had 8,572 at its last 10-K), one of the three largest PBMs,
> and an insurer serving more than 37 million people. Its PBM earned $7.1-7.4bn a year through a lost mega-contract and relentless
> client price pressure, which shows how durable the scale economics are; Caremark *"closes out 2025 with
> significant customer wins and strong retention"*. The 2024 insurer collapse was a pricing error the company has
> already corrected: MBR 86.0% in H1 2026 against 88.6%, adjusted operating income up 23% in the half, guidance
> raised twice in 2026 (adjusted EPS $7.00-7.20 to $7.90-8.10; operating cash to at least $11.5bn). The stores
> moved to cost-based reimbursement (*"CVS Pharmacy successfully completed the transition to cost-based
> reimbursement across its Commercial, Third-Party Discount, Medicare and Medicaid businesses"*), which ends the
> generic-deflation squeeze, and competitors are shrinking (Walgreens delisted in 2025 with 8,572 stores
> against 9,285 in FY2019; Rite Aid's prescription files bought by CVS in 2025), so CVS inherits their scripts: prescriptions up 5.4% in 2025. A new CEO from the PBM side, four directors
> appointed under an agreement with Glenview Capital, and $14-18bn of adjusted operating income on a $109bn market value. Buy the
> survivor of a consolidating industry at a trough.

**Every fact in that paragraph is on file and the run endorses the parts about scale and the 2026 recovery. The
answer, mechanism by mechanism.**
- **The PBM's durability is durability of volume, not of price.** The same filings that show $7.1-7.4bn show the
  price going to the client every year (*"continued pharmacy client price improvements"*) and a fifth of volume
  leaving in one renewal. A business that holds its earnings only by winning back in purchasing what it concedes in
  price is inside [E3-62]'s second step, and the new state laws and the FTC settlement act on exactly the
  purchasing side.
- **The insurer's recovery is real and it is the wrong kind of evidence.** It came from repricing and shedding: 21%
  of insured members and 36% of stand-alone PDP members gone, the exchange business exited, and $1.2bn of
  favourable prior-year development in H1 2026. A franchise raises price and keeps the customer (the [E2-44] test);
  Aetna raised price and the customer left. And its next price is CMS's to set (the 0.09% advance notice).
- **Cost-based reimbursement is a change of the payer's formula, not a grant of pricing power.** It resets how the
  payer pays; it does not give the store the right to name its price, and a store's customer still goes where his
  plan's network sends him.
- **Inheriting a dying competitor's scripts is [E2-58]'s over-capacity self-correcting**, *"as capacity shrinks"*;
  the equation's own words are that such corrections leave the survivors in the same commodity business.
- **And the fact the bull case cannot absorb is the direction of the units**: every series with units in it
  narrowed, and nominal earning power in 2025 was below 2019.

### [E4-04]'s perimeter close, considered and refused in writing
Is this a name whose durability cannot be judged from filings (UNKNOWABLE at Q2, without prejudice)? No. The
filings do judge it: the registrant says in its own words that clients move and bid, that price compression is
continuous, that reimbursement is set by payers, and that CMS sets the insurer's rate; the unit series and three
competitor rows confirm each. **The evidence is in and it fails [E3-03] on the business, which is OUT, not
UNKNOWABLE.** Nor is this the rebuilt-from-zero technology case [E4-04] names; the failure is criterion (2) and (3)
of [E3-03], not durability.

### [E3-47], the cost of a wrong close, weighed
*"our most egregious mistakes fall in the omission, rather than the commission, category."* The strongest evidence
against this verdict is the PBM's earnings record: $4.6bn (2017) to $7.1-7.4bn (2022-2025) through price
compression and a lost mega-client, which a commodity middleman should not manage; and the per-claim figure has
risen. **Weighed, and it does not carry the verdict**: the rise came with specialty-drug mix and purchasing
economics the filings say are being handed back and legislated against, the segment's nominal income has been flat
for four years, and the two other PBMs earn the same order of margin on the same model. **Recorded as the strongest
evidence against the verdict.**

- Class: **[x] NONE** in [E3-03]'s sense (one of three criteria met in each business); as a scale position,
  **NARROW** · Direction: **NARROWING on every series with units in it**
- **VERDICT: [ ] IN  [x] OUT (on the business)  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  **[E3-03] criterion (2) fails in all three businesses on the registrant's own words and its unit series**: *"PBM
  clients are generally well informed, can move between us and our competitors and often seek competing bids"*, and
  claims fell 18.2% in 2024 on *"the previously announced loss of a large client"*, the year Express Scripts'
  Centene agreement began; the insured book lost 21% of its
  members when repriced; the stores compete with nine named classes of seller for a customer whose plan chooses
  the network. **Criterion (3) fails for the insurer outright** (capitated rates *"subject to annual revision by
  CMS"*, an 85% MLR floor with rebates and enrolment penalties) and **the price is set by the counterparty for the
  PBM and the stores**, with PBM regulation *"proposed or enacted in a majority of states and on the federal
  level"*. **[E2-44]**: the pricing characteristic is failed in the filings' standing words, *"If we are unable to
  limit our price increases, we may lose customers to competitors with more favorable pricing"*. **[E4-55]**: units
  narrowing (claims minus 19%, insured members minus 21%, retail earnings per script minus 45% since 2017).
  **[E4-47]**: 2025 adjusted operating income below 2019 in nominal dollars. **[E2-53]**: the largest in each field
  and none of the three set its own year. **[E2-45]**: a funded attacker already won the renewal that cost Caremark most of a fifth of its claims.
  **What is here is a very large operator of three spread businesses whose prices are set by CMS, by PBM clients
  and by payers, where [E2-59] says the moat belongs to the regime and [E3-62] says the gains flow to the
  customer.** The entry run stops at this gate. [E5-13]: most names should end here, and that is the system
  working.
  **What this verdict is NOT.** It is not a forecast that CVS will do badly; the 2026 recovery is real and may
  continue. It is not a Q3 finding (the conduct record is written out below, without a verdict). And it is not a
  claim about the price, which is computed below without entry language.

---
**STOP: THE HARD SEQUENCE CLOSES THE FILE HERE.** Q1 is IN, **Q2 is OUT**. Q3, Q4, Q5 and Q6 are not answered as gates
and return no verdict. What follows is **recorded evidence and computation**, carried because a closed file with its
evidence written down is worth more later than one without, and because the brief asked for the working-capital
flag and the owner-earnings rebuild. **No entry language appears anywhere below.**

## Q3 - ARE THEY HONEST, AND ARE THEY RATIONAL? MATERIAL ONLY, NO VERDICT
*The file closed at Q2. Nothing below is a gate; each item is a prompt recorded for the next reader, dated to when it
became public. The DEF 14A of 2026-04-03 (`0001308179-26-000201`) was listed but NOT read by this run; the pay and
incentive design is therefore not scored here.*

**Weight case, declared as it would have been:** **daily execution** (an insurer re-prices every year and *"the nature
of the insurance business magnifies the effect which individual managers have on company performance"* **[E2-70]**; a PBM
re-bids its clients on about three-year contracts; **[E3-38]**) and **leverage** ($64.6bn of debt and a float-funded
insurer, **[E3-29]**). **Two of three ticked: Q3 would have been a binary gate.**

**Conduct matters on file** (a prompt to read, never a venality finding **[E5-22]**; penalty size is not seriousness in
either direction):
- **Omnicare False Claims Act case** (public at the April 2025 verdict; 10-K FY2025 and 10-Q Q2 2026): *"In April 2025,
  the jury found both Omnicare and CVS Health Corporation liable"* for dispensing *"where a valid prescription did not
  exist"* (2010-2018, spanning the 2015 acquisition); trebled damages of about $407M and penalties of $542M, **CVS Health
  Corporation jointly and severally liable for $165M** of the penalties. **On 2025-09-22 Omnicare filed for Chapter 11 and
  was deconsolidated**; the 2025 tax rate fell *"due to a worthless stock deduction associated with a subsidiary that filed
  for bankruptcy in 2025"*; and in July 2026 CVS agreed that *"the DOJ will receive a minimum of $ 440 million from Omnicare
  and CVS Health Corporation"*, CVS paying $130M directly and guaranteeing collection of up to $310M from the estate. **The
  prompt, stated without a finding:** a judgment of about $949M against a subsidiary is being settled at a stated minimum of
  $440M through that subsidiary's bankruptcy, with a tax deduction for the parent. Every step is disclosed in the filings,
  which is the candor side of **[E2-26]**; whether it is also the conduct **[E2-68]** describes (behaviour where the company
  holds the advantage) is the question a Q3 read would have had to answer.
- **Behnke (PBM)**: a court found *"certain subsidiaries of CVS Health Corporation liable for damages"* on Medicare Part D
  *"direct and indirect remuneration reporting practices for two clients from 2010 through 2016, which the Company has since
  modified"*; charge $291M (June 2025).
- **Opioids**: *"remaining accrual related to these opioid litigation matters was approximately $ 4.0 billion"* at
  2025-12-31, payable $648M current and $3,327M later; further charges $100M (2024) and $320M (2025).
- **FTC**: the September 2024 insulin complaint against *"the three largest PBMs"*, with a proposed settlement announced July
  2026 covering *"rebate, pharmacy network, contract, and vertical integration issues"* (terms not read).

**The flags [E4-22, E4-29, E5-15]:**
- **[E4-29], EBITDA: does not fire.** The word appears **zero times** in the FY2025 10-K, the Q2 2026 10-Q and the Q2 2026
  release (the brief's standing rule, checked).
- **[E4-22] third flag, projections: fires.** Every release carries full-year GAAP and adjusted EPS guidance. **[E3-48]'s
  action, guidance against outturn:** 2024 adjusted EPS guided *"at least $8.30"* (as restated in the Q1 2024 release), cut
  to *"at least $7.00"* (2024-05-01), to $6.40-6.65 (2024-08-07), then *"investors should no longer rely on the Company's
  previous guidance"* (2024-10-18, the day the CEO was replaced); **outturn $5.42, 35% below the first figure**. 2025: guided
  $5.75-6.00 (2025-02-12), outturn **$6.75**, above. 2026: $7.00-7.20, raised to $7.30-7.50 and to $7.90-8.10. One large miss
  and two beats; the miss was the insurer's cost trend.
- **[E2-57] / [E5-33] / [E3-53], "except for": fires, and it is the sharpest disclosure prompt in the file.** Adjusted
  operating income excludes, besides about $1.9-2.0bn a year of intangible amortization, a charge in every year read:
  restructuring $507M (2023) and $1,179M (2024); loss on assets held for sale $349M (2023) and $2,533M (2022); opioid charges
  (2024, 2025); *"legacy litigation charges"* $1,220M (2025); goodwill impairments $431M (2021) and $5,725M (2025); store
  impairments $1,358M (2021); losses on Accountable Care assets $288M and a clinic-closure charge $83M (2025). **2025 GAAP
  diluted EPS $1.39 against adjusted $6.75.** Each item is separately quantified at every line, which is the passing side of
  [E2-26]; that there is one every year is [E2-57]'s *"count the runs scored against you in all nine innings"* and [E5-33]'s
  *"to tell owners year after year, 'Don't count this' ... is misleading"*.
- **[E5-15], serial issuance: does not fire on the recent record** (1,272.2M shares at 2026-02-04, 1,279.0M at 2026-07-29;
  buybacks $2.0bn in 2023, $3.0bn in 2024, none in 2025). The 2018 Aetna purchase was paid partly in stock (*"a combination of
  cash and CVS Health stock"*), the test **[E5-44]** would apply to; not computed.

**The primary test [E2-01], scoped [E2-47, E2-43]:** GAAP return on book equity 2025 about 2.4% ($1,768M on year-end $75,214M), 2023
about 11.7% ($8,344M on the 2022 year-end $71,469M); **tangible equity is about minus $35.6bn**, so [E2-47]'s *"unusual debt-equity ratios"* and *"assets carried at
unrealistic balance sheet values"* carve-out applies, and [E2-43]'s unleveraged-net-tangible-assets denominator is swamped
by float and payables. Not computed further.

**Institutional imperative [E2-30], prompts:** (2) *"acquisitions will materialize to soak up available funds"*: about $61bn
of cash acquisitions 2018-2025, and the 2023 purchases (about $16.6bn) were written down by $5.7bn within two years; the
Health Care Delivery unit may be *"impaired again by a material amount"*. (4) peer imitation: all three large PBMs sit
inside an insurer (CVS, Cigna, UnitedHealth) and each group has bought into primary care (Oak Street; Optum Health; Cigna's
VillageMD investment, whose accrued dividend receivable Cigna impaired in 2024, CI 10-K FY2025). Recorded, not scored.

**Buybacks [E5-08, E4-31]:** $2.0bn at about $87.7 a share (January 2023, 22.8M shares) and $3.0bn at about $75.6 (January
2024, 39.7M shares), the second paid in the first week of the year the insurer's earnings collapsed; the 10-K's own performance graph has $100 at
2020 worth **$74 at 2024 year-end**. Whether either was at a *"material discount"* to value is not judged here.

**Management change:** CEO replaced 2024-10-17 (*"The Board believes this is the right time to make a change"*); four
directors appointed 2024-11-17 under a confidentiality agreement with Glenview Capital, one of whom (Mr Robbins) resigned
2026-08-13 *"not the result of any disagreement"*. **Recorded; the guardrail binds: nothing here could repair Q2.**

## Q4 - WILL IT SURVIVE? MATERIAL ONLY, NO VERDICT

### Owner earnings **[E2-23]**, rebuilt year by year from the filed cash-flow statements; no net-income proxy
Working file `oe.py` / `oe_out.md`. Construction (CONVENTION, framework section VI): operating cash flow, less stock-based
compensation in full **[E5-06]** (the cash-flow line, every year resolved), less the year's growth in *"Health care costs
payable and other insurance liabilities"* (the insurer's float, stripped per Stage 0(b) and the UNH precedent: borrowed
money that reverses **[E2-61]**), less (c). **(c) is a disclosed judgment with two ends:** the low end is **depreciation**,
D&A less the amortization of acquired intangibles, because the corpus default is *"the depreciation charge"* **[E3-44, E2-41]**
and the same row says *"reported earnings plus amortization of intangibles usually gives a pretty good indication of earning power"*; the high end is
**total capex**, 77% of which is *"technology, digital and other strategic initiatives"*. **Judged (c): close to the capex
end**, because the stores and systems are being replaced, not grown (stores down), so capex is mostly maintenance; the two
ends are only $0.2-0.6bn apart after 2019 and the choice moves nothing. This is not the [E5-20] railroad class.

| year | OCF | SBC | float growth stripped | depreciation | capex | OE, (c)=depreciation | OE, (c)=capex |
|---|---|---|---|---|---|---|---|
| 2015 | 8,539 | 230 | 0 | 1,481 | 2,367 | 6,828 | 5,942 |
| 2016 | 10,141 | 222 | 0 | 1,680 | 2,224 | 8,239 | 7,695 |
| 2017 | 8,007 | 234 | 0 | 1,662 | 1,918 | 6,111 | 5,855 |
| 2018 | 8,865 | 280 | -311 | 1,712 | 2,037 | 7,184 | 6,859 |
| 2019 | 12,848 | 453 | 320 | 1,935 | 2,457 | 10,140 | 9,618 |
| 2020 | 15,865 | 400 | -231 | 2,100 | 2,437 | 13,596 | 13,259 |
| 2021 | 18,265 | 484 | 169 | 2,253 | 2,520 | 15,359 | 15,092 |
| 2022 | 16,177 | 447 | 1,247 | 2,439 | 2,727 | 12,044 | 11,756 |
| 2023 | 13,426 | 588 | 394 | 2,461 | 3,031 | 9,983 | 9,413 |
| 2024 | 9,107 | 540 | 2,757 | 2,572 | 2,781 | 3,238 | 3,029 |
| 2025 | 10,639 | 535 | 16 | 2,630 | 2,832 | 7,458 | 7,256 |

($M. Sources: 10-K FY2017 Exhibit 13 for 2015-2017, FY2019 for 2017-2019, FY2022 for 2020-2022, FY2025 for 2023-2025; the
2017 row read in two filings and it agrees. Intangible amortization from the segment reconciliations and the FY2017
intangibles note.)

**Windows, both (c) ends [E4-25, E4-38]:** 3y 2023-25 **$6,566M-$6,893M**; 5y 2021-25 **$9,309M-$9,616M**; 7y 2019-25 (the
post-Aetna perimeter) **$9,918M-$10,260M**; 10y 2016-25 $8,983M-$9,335M, crossing the Aetna perimeter and shown for display
only. **The spread is wide (3y to 7y about 50%) and it is a finding [E5-11]:** **[E4-41] names the luck in the window**:
2020-2022 carry the pandemic years (HCB MBR **80.9%** in 2020 against 86-92% since; *"lower contributions from COVID-19 ... test
kits since the expiration of the public health emergency"*), which a normalised mean removes; the 5y and 7y means are
flattered by them. **The honest range is roughly $6.5bn to $9.5bn**, and 2026 guidance of *"at least $11.5 billion"* of
operating cash (H1 2026 $10.6bn, with timing in it) sits inside the upper half if it holds.

**The screen's working-capital flag, resolved:** the payables line's +$3,855M in 2025 was offset by receivables (-$3,498M)
and other assets (-$2,593M); **working capital was a net use of $1,474M in 2025**, so 2025 operating cash understates rather
than overstates the year. The screen's `wc_note` is arithmetically right and does not move the owner-earnings figure. The
float line is the one that did move a year: **+$2,757M in 2024**, stripped above.

### Great, good, or gruesome? **[E4-20]**: stated, unticked
On the acquired capital, the gruesome prompt: about $61bn of cash acquisitions 2018-2025 (plus the stock paid for Aetna)
took consolidated adjusted operating income from $10,825M (2017) to $14,443M (2025), about $3.6bn more pre-tax on $61bn,
roughly 6%, before the stock. The base drugstore and PBM businesses need little capital; the growth was bought.

### Staying power, all three scored **[E5-11]**: findings, not a verdict
- **(1) Large and reliable earnings:** large, not reliable: owner earnings $3.0-3.2bn in 2024 against $15.1-15.4bn in 2021.
- **(2) Massive liquid assets, read per [E2-61]:** $8.5bn of cash, *"approximately $2.8 billion of which was held by the
  parent company or nonrestricted subsidiaries"*; the rest and most of the $34.8bn portfolio stand behind insurance
  regulation. Three $2.5bn back-up revolvers undrawn; no commercial paper at 2026-06-30. **The parent depends on bank lines
  and dividends up from regulated subsidiaries**, which [E5-39]'s *"kindness of strangers"* describes.
- **(3) Near-term cash requirements:** 2026 contractual cash due **$11,530M** (debt $4,007M, interest $2,933M, leases
  $2,626M, opioid $648M, insurance items $1,177M), plus a dividend of about $3.4bn a year (*"expects to maintain its quarterly
  dividend of $0.665 per share throughout 2026"*). **In 2024 owner earnings ($3.0-3.2bn) did not cover the dividend.**
- **Coverage [E2-54]:** interest paid $2,991M (2025) against owner earnings before interest of about $10.2bn at the capex end:
  about 3.4 times, in the 2024 trough about 2.0 times. Debt $64.6bn; no ratio ceiling applied.

### The way it dies, named from exposure **[E2-27, E3-24, E4-40]**: named, not scored
**The three spreads compress in the same year.** 2024 is the filed rehearsal: insurer adjusted operating income $5,577M to
$307M, owner earnings to $3.0bn, below the dividend. The exposure beyond that experience: PBM legislation *"in a majority of
states and on the federal level"* aimed at the purchasing economics that fund the client concessions, states barring
PBM-affiliated pharmacies, a 2027 Medicare Advantage advance notice of 0.09%, and $4.0bn of opioid payments due. Quantified:
a repeat of 2024 with the PBM's $7.2bn cut by a third (about $2.4bn pre-tax, about $1.8bn after tax at 2024's 25.4%)
would leave owner earnings of about $1.2bn against $11.5bn of contractual cash and a $3.4bn dividend, refinanced through the bond market. Likelihood, stated in the corpus's vocabulary: **a real
possibility** for a repeat of the 2024 earnings shape; **a low-level possibility** for a solvency event, given undrawn
revolvers and the parent's access to debt markets.

## COMPUTATION - NOT A CLEARANCE
*Arithmetic only, no box, no entry language (operator rule 3).*
- Cap **$108,776M** ($85.05 x 1,278,970,369). Owner-earnings yield: 3y **6.0%-6.3%**; 5y 8.6%-8.8%; 7y 9.1%-9.4%; against
  **5.47%** (US Treasury 30 Yr, 09/24/2026). On the honest range of $6.5bn to $9.5bn, about **6% to 9%**.
- **At the ~10% floor [E4-28] with no growth**, owner earnings of $6.5bn to $9.5bn are worth roughly **$65bn to $95bn**,
  against $109bn. The price assumes the 2026 recovery holds and grows from there; [E4-35]'s base rate is recorded against any
  growth case, and none is made here.
- Not added: the $34.8bn investment portfolio (**[E5-48]**: its income is already inside operating cash). Not deducted
  separately: the $4.0bn opioid obligation (its payments fall inside future operating cash).
- **Windage count: ONE** (the pandemic years named as luck in the window; no other conservative adjustment).

## Q6 - WHAT WOULD PROVE ME WRONG? REVERSAL CONDITIONS, NO POSITION
*A failure on the business gets reversal conditions in words, not a price alert (the QLYS ruling). Pre-committed here
[E1-02]; each is a filed series, read slowly [E4-17], the [E3-30] question asked of it.*
1. **The PBM keeps its price:** three consecutive 10-Ks in which Health Services' result is not explained by *"client price
   improvements"* or *"price compression"*, with claims growing and no large-client loss.
2. **The stores gain price, not only volume:** retail adjusted operating income per 30-day prescription rising for three
   consecutive years on the filed segment table (from $3.34 in 2025), after the move to cost-based reimbursement.
3. **The insurer holds its members at a lower cost ratio than the row:** insured medical membership growing while the MBR sits
   at or below the peer median of the competitor row for three years, through at least one CMS rate year below trend.
4. **Nominal earning power returns without purchase:** consolidated adjusted operating income above the 2022-2023 level of
   about $17.5bn for two consecutive years with cash acquisitions under $1bn a year.
Any one of these re-opens Q2; none re-opens it alone if the other three series keep narrowing.

---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN, Q2 OUT. Q3, Q4 and Q6 carry material only; Q5's block is
  replaced by COMPUTATION - NOT A CLEARANCE with no box and no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 rests on the FY2025 10-K's Item 1 and
  segment tables and the predecessor 10-Ks; every prior in the brief was checked against a filing before use (below).
- [x] Every UNRESEARCHED verdict names the artifact: **none issued.** The unmeasured competitors (Prime, MedImpact, the Blues
  plans, Kaiser, Walmart and Kroger pharmacy) are private, non-filing or unsegmented, named at Q2; no document exists to
  fetch for them.
- [x] Every UNKNOWABLE verdict states what cannot be known: **none issued.** [E4-04]'s perimeter close was considered and
  refused in writing at Q2.
- [x] **Step 0: the filing was read, accession numbers recorded; 2025 net cash provided by operating activities of $10,639M
  rebuilt from its own reconciliation lines and tied to the direct-method total.** A second cross-check: the 2017 operating
  cash, capex and SBC read in two filings (FY2017 Exhibit 13 and FY2019 10-K) agree; ELV's and HUM's benefit ratios in the
  reused UNH row re-read from their FY2025 10-Ks and agree.
- [x] **Owner earnings on multi-year means, four windows up to ten years, both (c) ends, the judged end disclosed; SBC from
  the cash-flow line in every year; the insurer's float growth stripped; no net-income proxy.** The sector-method question
  the brief raised is decided in writing at Stage 0(b): an operating company that owns a health insurer, ordinary method,
  three sector-method corrections bound.
- [x] **Competitor rows filled**, three of them (insurer, PBM, drugstore), every cell read by this run from the named filing;
  the insurer row's UNH/CI/CNC cells reused from the UNH run's filing-sourced row, the ELV and HUM cells re-read; no
  sub-agent used. Limits stated at each row.
- [x] **Sovereign for the earnings currency (USD), from the issuing authority, dated**: 5.47%, US Treasury daily par yield
  curve, 30 Yr, 09/24/2026, raw file saved; FRED not used.
- [x] Value stated as a round-number range, inside the COMPUTATION only.
- [x] One bar: none chosen, because Q5 did not open; windage count stated (ONE).
- [x] **Prices dated; aggregator used for the live quote only and flagged** ($85.05, close 2026-09-24, Yahoo chart endpoint,
  raw response saved).
- [x] **Every ledger id cited checked against `principle_ledger.csv`: 76 distinct ids in this file, none missing**; every row
  cited in the run's own sections was opened and read before citing. `tools/check_framework.py` run before the fold commit.
- [x] Run committed to git with pathspecs: `d9e33c8` (claim), `0f6200b` (Step 0, Q1), `73c3586` (Q2), `b6e471b`
  (beneath the close, self-audit, register), then the fold commit (the queue file staged from the HEAD blob plus the register
  entry only).

**THE BRIEF'S PRIORS, each checked against a filing:**
1. *Three segments* - **half right.** The 10-K reports **four** reportable segments (*"Health Care Benefits, Health Services,
   Pharmacy & Consumer Wellness and Corporate/Other"*), and Health Services is not only the PBM: it also holds the Health
   Care Delivery assets (Oak Street, Signify), whose losses sit inside the PBM's segment result from 2023. The three-business
   reading holds for the operating businesses.
2. *The perimeter* - **confirmed and extended**: Aetna (2018, cash and stock), Signify and Oak Street (2023, $16.6bn cash), the
   2025 Health Care Delivery impairment ($5.7bn); **not in the brief**: Omnicare's Chapter 11 and deconsolidation (2025),
   the exchange exit (2026), the MSSP sale (2025), and the LTC impairment of 2018 ($6,149M).
3. *CEO replaced 2024; guidance withdrawn; PBM under regulatory and litigation pressure* - **all confirmed** from the 8-K of
   2024-10-18, the 2024 releases, the 10-K and the 10-Q (the July 2026 FTC settlement proposal was not in the brief).
4. *One payables line moved about a third of 2025 operating cash* - **arithmetically confirmed (36.2%) and resolved: net
   working capital was a use of $1,474M in 2025.** The line that moved a year was the insurer's float in 2024 (+$2,757M).
5. *Pull the latest EX-99.1* - done; [E4-29] does not fire, [E4-22]'s third flag does.

**ERRORS, ARTIFACTS AND REPORTED-NOT-PATCHED, recorded rather than smoothed.**
1. **My own errors, caught before commit.** The Q1 draft said *"about $59bn of acquisitions"* and *"about $12.5bn of
   goodwill"* written off, and that guidance was cut *"twice in three months"*; the cash-flow lines sum to about $61bn, the
   impairments to about $12.3bn, and the cuts were May and August 2024. The Q2 draft attributed 427 million claims to
   Cigna as a fact (CVS does not name the client; restated as consistent with the timing), called CVS *"the largest drugstore
   chain"* and *"a top-five insurer"* (neither in a filing read; replaced by store counts and the 37 million figure), said
   Rite Aid was *"in liquidation"* and *"in bankruptcy"* (not read by this run; removed), miscounted the pharmacy-competitor
   classes (nine, not seven) and the retail per-script declines (seven of eight years, not eight of nine), and wrote the
   Walgreens comparison as five of six (four of five). The Q3 draft paraphrased [E3-44] past its words (*"better picture"*;
   the row says *"a pretty good indication of earning power"*) and placed both buybacks inside the collapse year (only the
   second was). All corrected before commit.
2. **Not read: the DEF 14A of 2026-04-03.** Pay design and incentive metrics are not scored; the file closed at Q2, so no
   verdict depends on it.
3. **Segment definitions changed in 2023** (Pharmacy Services to Health Services with the delivery assets; Retail/LTC to
   Pharmacy & Consumer Wellness), so the long PBM and retail series cross a definitional break; the direction statements are
   made within each run of years as well as across the break.
4. **The template's STOP sign.** The template marks the Q5 gate with a warning symbol; this file's stop line uses the words
   only.
5. **REPORTED, NOT PATCHED: the screen's `wc_note` names the one line that moved and not the net.** On CVS it read *"ONE
   LINE MADE THE CASH: AccountsPayable moved 36% of 2025 OCF"*; the net working-capital change that year was a use of
   $1,474M, so the line did not make the cash. Printing the net change beside the line would separate the two cases.
6. **The price** has fallen every session since 2026-09-15 ($94.49 to $85.05) with no 8-K filed since 2026-08-17; nothing in
   this file depends on the reason, and none is offered.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- **One line: Q1 IN / Q2 OUT, on the business.** Three spread businesses (a PBM, a Medicare-heavy insurer, a drugstore
  chain) whose prices are set by the other side: PBM clients *"can move between us and our competitors"* and one did (claims
  -18.2% in 2024), the price goes to the client every year (*"continued pharmacy client price improvements"*); the insurer's
  rate is CMS's and its insured book fell 21% when repriced; the stores' earnings per prescription fell 45% since 2017 on
  payer reimbursement, as Walgreens' did. 2025 adjusted operating income below 2019 in nominal dollars after about $61bn of
  acquisitions since 2018. At $85.05 (cap $108,776M) against a 5.47% sovereign the owner-earnings yield is about 6% to 9%,
  recorded as arithmetic only.
- **If UNRESEARCHED - THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.

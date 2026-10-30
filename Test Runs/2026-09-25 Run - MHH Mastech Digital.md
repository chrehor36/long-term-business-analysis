# Company Run - Mastech Digital, Inc. (MHH) - 2026-09-25
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

*CLAIMED 2026-09-25 about 06:45 EDT (write-early; no `*Run - MHH *.md` existed in `Test Runs/`; commit `fbd26d0`). Research folder `Test Runs/_research 2026-09-25 MHH/`. WAVE 7 name 34 of 218 (counted: line 34 of `_wave7_order.txt`; 33 lines in `_wave7_done.txt` at claim, the last being ICFI). Unattended session. Sections below are filled as they close.*

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
- rate **5.47** % · date **09/24/2026** (the newest row on the curve when this run struck it, about 06:45 EDT on
  2026-09-25) · source (issuing authority) **US Treasury daily par yield curve, 30 Yr, `home.treasury.gov`
  daily-treasury-rates.csv for 2026**, struck fresh by this run and saved raw as
  `Test Runs/_research 2026-09-25 MHH/treasury_2026.csv`; `python tools/sources.py` returned the same figure and date.
  Neighbouring rows 5.40 (09/23), 5.29 (09/22). **FRED DGS30 was not used.**
- FX: **not required.** The 10-K: *"Approximately 99% of our revenues are generated from clients located in North
  America"* and *"we receive the vast majority of our revenues in U.S. dollars"*; the cost exposure is the rupee
  (recruiting and delivery staff in India are *"paid in rupees"*). USD sovereign.

**The filing was read** - not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K for the year ended 2025-12-31, filed 2026-03-18, accession `0001193125-26-112845`** (`mhh-20251231.htm`).
    Read: cover; Item 1 whole (overview, history, the two segments, sales and marketing, recruiting, employees,
    competitive position, strengths, government regulation); Item 1A whole; Item 7 MD&A whole (segment revenue and
    margin table, SG&A detail, 2025 v 2024 and 2024 v 2023, liquidity, the Primentor agreement, the 2023 employment
    claim, the finance-function transfer to India); the balance sheet, income statement, equity statement and cash-flow
    statement with every reconciliation line; notes on goodwill impairment, contingencies and credit facility.
  - **10-Ks FY2022 `0001193125-23-079936`, FY2019 `0001193125-20-090186` and FY2016 `0001193125-17-094899`**, each
    carrying three years of cash-flow statements, so **FY2014-FY2025 (twelve years) is covered without a gap** from
    filed statements. FY2017, FY2020, FY2021, FY2023 and FY2024 10-Ks opened for dated language (acquisitions,
    contingent consideration, the 2018 ERP disruption, the CARES Act payroll-tax deferral, consultant counts, bill
    rates, the Primentor cost).
  - **10-Q for the quarter ended 2026-06-30, filed 2026-08-06, accession `0001193125-26-337054`** (cover, notes on the
    credit facility, the buyback authorisation, Primentor).
  - **8-K EX-99.1 earnings releases** for Q4 2023 (2024-02-07) through **Q2 2026 (2026-08-06, `0001193125-26-337015`)**,
    ten in all; every 8-K main document since 2024-01-01 (officer changes, the Primentor consulting agreement of
    2024-01-19, the auditor change of 2025-12-10, the Dallas lease of 2026-03-11, the bylaw amendment and CEO RSU grant
    of 2026-08-06, the CFO RSU grant of 2026-08-14); the 2017 InfoTrellis 8-Ks and the 2020 AmberLeaf and Schedule 13D
    filings.
  - **DEF 14A filed 2026-04-09, `0001193125-26-149074`**, downloaded; beneficial ownership and the 2025 bonus table read.
- **deal_note, opened:** the screen column is empty and the submissions index for 2020-2026 lists **no S-4, 425,
  DEFM14A, SC TO or SC 13E3**. The one Item 1.01 8-K of 2026 (`0001193125-26-102393`, filed 2026-03-11) is **a
  five-year office lease in Dallas** (5,895 sq ft, $18,176 a month rising to $20,259). The Schedule 13D filings of
  2020-2023 are the founders' transfers to family trusts *"for estate planning purposes"*. **Nothing deal-shaped is
  live; the quote is an owner-earnings price, not a spread.** Recorded for Q3 rather than here: a 2024 consulting
  agreement (below) pays its consultant in founder shares on a "Sale Event".
- figure cross-checked against the filed statement: **FY2025 net cash provided by operating activities, $11,135K**,
  rebuilt from its own reconciliation lines: net income 609 + D&A 3,324 + bad debt 36 + financing-cost amortization 94
  + stock compensation 3,118 - deferred taxes 1,290 + lease 45 + fixed-asset loss 4 + deferred-compensation
  amortization 500 - long-term severance 657 - deferred-compensation payment 2,000 = 3,783; working-capital lines
  +5,013 + 1,729 - 1,215 + 1,756 + 357 - 288 = **+7,352**; total **11,135. Ties.** The XBRL pull (`xbrl_out.txt`)
  reproduces FY2025 revenue $191.37M against the filed $191,371K.
- *If the filing could not be obtained -> **UNRESEARCHED**.* **Not invoked; every document came from SEC EDGAR primary
  documents.**

**THE PRICE AND THE CAP** *(struck by this run, not carried from the screen)*
- **Share count, quoted from the cover of the 10-Q for 2026-06-30, accession `0001193125-26-337054`:** *"The number of
  shares of the registrant's Common Stock, par value $.01 per share, outstanding as of July 31, 2026 was 12,012,581."*
  One class of common; the balance sheet: *"Preferred Stock, no par value; 20,000,000 shares authorized; none
  outstanding"*. No classes summed. `python Screens/cover_shares.py MHH` returned the same document, accession and
  count.
- **Price $7.22** (close 2026-09-24, **aggregator quote, flagged**: Yahoo Finance chart endpoint, raw response saved
  as `price_raw.json`). **Thinly traded**: 1,200 shares changed hands on 2026-09-24 and 3,900 on 09-23; the meta
  block's `regularMarketTime` is 11:17 EDT on 09-24, the last trade of the day. Two-year closing range in the same
  pull **$5.50 to $15.98**. A null close for 2026-09-22 in the aggregator's series, recorded not filled. No split in
  the pull (the last split was the 2018 two-for-one, 10-K FY2018).
- **cap = close x shares**, split-invariant, `close` never `adjclose`: $7.22 x 12,012,581 = **$86.7 million.**
- **THE SCREEN'S CAP FLAG, SETTLED: the cap is right and the tagged float is wrong by a factor of 1,000.** The flag
  read a public float of $24,874M against a cap of $89M. The FY2024 10-K cover (`0001193125-25-054447`) says in words
  *"The aggregate market value of the voting stock held by non-affiliates of the registrant as of June 30, 2024 ... was
  $ 24,874,000"*, and companyfacts carries that fact as **24,874,000,000**. The same thousand-fold tagging error sits
  in the FY2021, FY2022 and FY2023 covers (tagged 47,201,000,000, 49,226,000,000 and 32,173,000,000); FY2011-FY2020 and
  the FY2025 cover are tagged at face. **A filer scale error in dei:EntityPublicFloat, not a cap error.** A second
  cover defect, recorded for Q3: **the FY2025 10-K (filed 2026-03-18) repeats the prior year's float figure and date,
  "as of June 30, 2024 ... $ 24,874,000"**, where the rule asks for the float at the end of the second quarter of
  FY2025. The screen's $89M is an early-September price on about the same count.

**THE PERIMETER, read before any question.** From the filed cash-flow statements and the 8-Ks:

| year | $M, cash at closing | what was bought |
|---|---|---|
| 2015 | 17.0 | Hudson IT (the US IT staffing business of Hudson Global), June 2015 |
| 2017 | 34.8 | the services business of InfoTrellis (data management), July 2017; plus up to $19.25M of EBIT-contingent deferred payments, **never paid**: revalued to credits of $11.1M (2018) and $6.1M (2019) |
| 2020 | 9.3 | AmberLeaf Partners (customer-experience consulting), October 2020; contingent consideration revalued to a $2.9M credit in 2021 |

**$61.1M of acquisition cash FY2014-FY2025, against a $86.7M cap.** Goodwill impairments on the Data and Analytics
segment: **$9.7M (2018) and $5.3M (2023)**. Goodwill $27.2M and intangibles $6.5M at 2026-06-30 against equity of
$91.8M: **tangible equity about $58M, of which $35.6M is cash**. The 2017 purchase was part-funded by a **$6.0M private
placement to the two founders at $7.00 a share, above the $6.35 market close**, negotiated by a special committee of
independent directors (10-K FY2017), with a founders' equity-support commitment for the deferred payments. No
acquisition since 2020.

**Cash items that are not recurring owner earnings, found in the notes and carried to Q4:**
1. **The CARES Act payroll-tax deferral**: *"Reductions in operating working capital levels provided $7.3 million of
   cash, of which $4.6 million was related to the COVID-19 payroll tax deferment program"* (10-K FY2020), repaid
   $2.3M in 2021 and $2.3M in 2022.
2. **The 2018 ERP disruption and its 2019 reversal**: receivables built $7.4M in 2018 and released $5.6M in 2019,
   *"the resolution of cash conversion disruptions related to our 2018 Cloud-based ERP platform implementation"*
   (10-K FY2021).
3. **Receivables released by a shrinking book**: +$12.5M in 2023 and +$5.0M in 2025, *"reflecting significant revenue
   declines during the year"* (2023) and *"lower accounts receivable, reflecting decreased revenue levels"* (2025).
4. **The screen's `wc_note`, tested and refuted as a description of 2021.** It read *"AccountsPayable moved 45% of 2021
   OCF"* and *"one line made the cash"*. The arithmetic is right (payables +$2,365K against operating cash of $5,216K),
   but payables did not make 2021's cash: total working capital that year was a **use of $11.7M**, driven by
   receivables (-$11,389K) on 14% revenue growth and the $2.3M CARES repayment; payables offset a fifth of it. The
   10-K FY2021: *"investments in operating working capital of $12 million"*. **2021 is the year working capital
   depressed the cash, not the year one line manufactured it.** The years in which working capital manufactured cash
   are 2019, 2020, 2023 and 2025 (items 1-3).

---
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

*Priors from the brief, stated as hypotheses and tested against the filing:*
- *"IT staffing plus a data-and-analytics services segment; spun off from iGATE around 2008"*: **confirmed.**
  *"incorporated in Pennsylvania on June 6, 2008 as a wholly-owned subsidiary of iGATE Corporation ... On September 30,
  2008, the Company was separated from iGATE"*. FY2025 revenue $191.4M: IT Staffing Services $158.1M (83%), Data and
  Analytics Services $33.3M (17%). From FY2026 the segments are recast as **Talent** and **Data & AI** (announced in
  the FY2025 10-K with reasons, *"account-centric management, industry-focused leadership"*).
- *"The analytics segment was built by acquisition (InfoTrellis around 2017, AmberLeaf around 2020)"*: **confirmed**,
  July 2017 and October 2020; *"Our Data and Analytics Services segment was established through the July 2017
  acquisition ... and expanded through the October 2020 acquisition of AmberLeaf Partners"*.
- *"Goodwill and intangibles may be a meaningful share of equity"*: **confirmed in size, softened in effect**: $33.8M
  of $91.8M (37%) at 2026-06-30, after $15.0M of impairments; tangible equity is positive and mostly cash.
- *"Founders' families (Wadhwani, Trivedi) hold a large, possibly controlling, stake"*: **confirmed, controlling.**
  Risk factor: *"Sunil Wadhwani and Ashok Trivedi, co-founders of the Company, beneficially own approximately 58% ...
  together have sufficient voting power to elect all the members of the Board of Directors"*. DEF 14A (2026-03-31):
  Trivedi 27.7%, Wadhwani 13.1%, the Wadhwani 2020 family trust 15.6%; an outside holder, Steven A. Shaw, 11.0%.
- *"Revenue declined after 2022"*: **confirmed**: $242.2M (2022) to $201.1M, $198.9M, $191.4M, and H1 2026 $82.5M
  against $97.4M (-15.3%). **CEO change**: Vivek Gupta resigned December 2024, Nirav Patel appointed (employment
  agreement 2024-11-01). **Restructuring**: severance $2.4M, $2.1M and $2.8M in 2023-2025 (*"largely related to
  executive leadership departures"*) and a $1.9M transfer of the finance function to India in 2025. **Buybacks**:
  $2.2M in 2025; a new $5.0M authorisation in February 2026, unused at June 2026. **No deal-shaped 8-K** (Step 0).

- **Unit economics in my own words.** Mastech places about 840 IT contractors (year-end 2025, down from 1,261 at the
  end of 2021) at client sites, mostly large banks and system integrators, and bills them by the hour (average
  **$86.10** an hour in 2025); it pays the contractor, and keeps about **24%** of the bill as gross margin in staffing.
  About half of its employees work on Mastech-sponsored H-1B visas (*"approximately 48% of our employee workforce"*),
  and roughly 89 recruiters, mostly in Noida, India, find candidates from *"the same candidate pool"* other staffing
  firms use. The smaller data-and-analytics arm sells project consulting (master data management, data engineering,
  customer-experience work, now "agentic AI") in engagements of *"approximately $0.3 million to $2.5 million"*, at a
  **46%** gross margin in 2025, delivered partly offshore. Selling and administration take the rest: FY2025 gross
  profit $53.1M against SG&A $53.1M, **operating income $1K**. Capital needs are working capital (receivables at
  54 days) and almost no plant (capex $0.4M).
- **The scarce input this business controls:** a recruiting engine and a visa-sponsorship practice that let it supply
  contractors quickly, plus preferred-vendor status on client lists and a minority-owned certification (*"attractive to
  certain existing and potential clients in the U.S. government and public-sector segments"*). Whether any of that is
  scarce **relative to the client's alternatives** is the Q2 question.
- **Will the fundamentals look broadly the same in ten years?** The mechanism will: large companies will rent IT labour
  by the hour. The terms are moving against the supplier on the filing's own account (managed service providers and
  clients' own offshore Global Capability Centres now sit between Mastech and the end client; a top-ten client is
  insourcing), and the filing names AI as both an offering and a risk. That is a question about bargaining power and
  durability, which the 2026-09-20 ruling places at Q2; it is carried there, not used to close Q1.
- **The five-minute test [E4-46]:** the business can be stated in a paragraph and the filing confirms each clause.
  Nothing here needs months of study.
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

## Q2 - IS IT A FRANCHISE? **[E3-03]**

> *"An economic franchise arises from a product or service that: (1) is needed or desired; (2) is thought by its
> customers to have no close substitute and; (3) is not subject to price regulation. The existence of all three
> conditions will be demonstrated by a company's ability to regularly price its product or service aggressively and
> thereby to earn high rates of return on capital."* **[E3-03]**, 1991 letter

**The hypothesis I formed while reading, stated so it can be attacked [E4-26]:** *Mastech rents out IT contractors
that its clients can and do get from many other suppliers, through intermediaries that run the vendor list on the
client's behalf, so the client, not Mastech, holds the terms.* The evidence against it was hunted first and is set out
before the verdict.

### The three criteria, on the registrant's own words

- **(1) Needed or desired: PASSES.** Revenue $191.4M in FY2025; the filing names large, recurring IT-labour budgets
  at *"businesses and institutions with significant IT-spend and recurring staffing needs"*, and three clients above
  10% of revenue (Fidelity 16.7%, Populus 12.1%, CGI 10.8%).
- **(2) Thought by its customers to have no close substitute: FAILS, on the registrant's own description of how it is
  bought, and on what its clients are doing.**
  - **The client buys from several suppliers at once, on price among other things.** Item 1, IT Staffing Services:
    *"Clients typically engage multiple staffing providers, and assignments are awarded based on qualifications,
    availability, and pricing."* And the candidates are shared: *"most staffing firms access the same candidate pool
    via job boards, websites and other recruitment tools"*, so the edge the filing claims is speed (*"respond to client
    requests faster than the competition"*), not a supply no one else has.
  - **The client has put an intermediary in charge of choosing.** *"the third-party managed service provider ("MSP")
    retains control of the vendor selection and vendor evaluation process, which somewhat weakens the relationship
    built with the client"*; MSP clients with their own offshore Global Capability Centres *"represented approximately
    30% of our IT Staffing Services Segment's 2025 revenues"*, and *"The general impact of this shift towards the MSP
    and GCC model has been to lower our gross margins and create delivery inefficiencies ... resulted in a loss of
    business opportunities"*. The MD&A adds: *"These intermediated delivery models may reduce pricing flexibility"*.
  - **Where the client grants volume, it takes price.** *"Clients enter into these contracts to reduce their number of
    vendors and obtain better pricing in return for a potential increase in the volume of business to the preferred
    vendor. While these contracts are expected to generate higher volumes, they generally carry lower margins."* Losing
    that status *"may preclude us from providing services to existing or potential clients, except as a
    subcontractor"*.
  - **The client can leave at will, and is leaving.** *"These contracts are terminable without penalty, as are most of
    our contracts."* The analytics segment's multi-year Center of Excellence offering *"generally can be early
    terminated by the client with a short-term notice"*. In 2026 a top-ten client took the work in-house: *"a 22.3%
    decrease in billable consultants since the second quarter of 2025, as a top ten client continued insourcing services
    we provide in this segment"* (Q2 2026 release, EX-99.1 to `0001193125-26-337015`), and the risk factor already
    names the option: *"clients may elect to increase their internal resources to satisfy their staffing and data and
    analytics needs"*. The client's closest substitute is its own payroll.
  - **The registrant says the barriers are low, twice.** Item 1: *"We operate in highly competitive and fragmented
    industries, with largely low barriers to entry in our IT Staffing Services segment."* Item 1A, under the heading
    *"Our industries are highly competitive and fragmented, which may limit our ability to increase our prices for
    services"*: *"There are relatively few barriers to entry into many of our markets, and as such we may face
    additional competition from new entrants into our markets."*
  - **The analytics arm faces the largest firms in the trade.** *"In our Data and Analytics Services segment, we
    primarily compete with Cognizant, Tata Consultancy Services, Capgemini, as well as with smaller boutique data and
    analytics firms. Many competitors are significantly larger and have greater financial resources in comparison to
    us."* The segment's goodwill was impaired twice ($9.7M in 2018; $5.3M in 2023, on *"declining revenue trends and
    lower future revenue projections"*), and its revenue fell from $40.6M (2022) to $33.3M (2025).
  - **One of its three largest clients is a competitor.** CGI (10.8% of FY2025 revenue, 22.5% of FY2023) is a systems
    integrator, and the 10-K names system integrators as a sales channel for staffing *"with a need to supplement their
    own abilities to attract highly qualified temporary IT personnel"*: Mastech is in part a subcontractor to firms that
    sell the same end service.
- **(3) Not subject to price regulation: PASSES on price, with a cost-side exposure recorded.** No filing read
  describes regulated bill rates. The regime touches the cost and supply of labour instead: *"approximately 48% of our
  employee workforce was working under Mastech Digital sponsored H1-B temporary work visas"*, and legislation *"could
  be enacted limiting H1-B visa holders' employment with staffing companies"*. That is [E2-59]'s administered regime
  in the form that can withdraw an input, recorded as a Q4 exposure, not a criterion-3 failure.

**Checklist:** Needed or desired [x] · no close substitute [ ] **fails** · not price-regulated [x]

### [E3-03]'s demonstration clause, and [E3-43]'s alternative, both tested
**The clause runs the wrong way.** Operating margin, from the filed income statements (FY2016, FY2019, FY2022 and
FY2025 10-Ks; the XBRL pull in `xbrl_out.txt` reproduces each):

| FY | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| revenue $M | 113.5 | 123.5 | 132.0 | 147.9 | 177.2 | 193.6 | 194.1 | 222.0 | 242.2 | 201.1 | 198.9 | 191.4 |
| operating margin %, reported | 4.9 | 3.8 | 3.4 | 2.8 | 6.6 | 8.8 | 6.9 | 7.9 | 5.0 | -4.6 | 1.9 | 0.0 |
| operating margin %, without the contingent-consideration credits and impairments | 4.9 | 3.8 | 3.4 | 2.8 | 5.8 | 5.6 | 6.9 | 6.6 | 5.0 | -0.4 | 1.9 | 0.0 |

*(Adjustments from the filed SG&A lines: 2018 less the $11.1M contingent-consideration credit plus the $9.7M goodwill
impairment; 2019 less the $6.1M credit; 2021 less the $2.9M AmberLeaf credit; 2023 plus the $5.3M impairment and the
$3.1M employment claim.)* **Twelve years between -0.4% and 6.9% on the adjusted line, and the last three at 1.9% or
below.** A business that could *"regularly price its product or service aggressively"* would not have earned $1K of
operating income on $191.4M of revenue in 2025.

**[E3-43] gives the other route to exceptional profits**: *"'a business' earns exceptional profits only if it is the
low-cost operator or if supply of its product or service is tight."* The 10-K claims the first (*"We have historically
enjoyed a lower operating cost structure than our industry peers"*). The filed result tests it: in FY2025 Mastech's
operating margin (0.0%) sat below Kforce's (3.8%) and Information Services Group's (7.3%) and above Robert Half's (1.4%)
only by rounding; whatever the cost advantage is, it is neither wide nor sustainable in [E2-58]'s sense (*"a cost
advantage that is both wide and sustainable ... By definition such exceptions are few"*). The second route, tight
supply, is the 2021-2022 labour market: operating margin peaked at 7.9% reported in 2021 and fell back as supply
loosened.

**Units, not dollars [E4-55].** The physical series is consultants on billing: **1,167 (end 2019), 1,063 (2020), 1,261
(2021), 1,208 (2022), 946 (2023), 1,008 (2024), 840 (2025)**, and a further 22.3% fall year on year to Q2 2026. The
average bill rate rose **$75.66 (2021), $80.64, $78.84, $82.77, $86.10 (2025), $92.17 (Q2 2026)**; the MD&A attributes
the rise to *"higher rates on new assignments and was reflective of the type of skill sets that we deployed"*, and in
2026 to exiting *"lower-margin and non-strategic positions"*. Rates up on a shrinking, re-mixed book is mix, not
pricing power: the 2025 rate rose 4.0% while staffing revenue fell 2.6% and heads fell 16.7%.

### Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]**
**The verdict does not rest on [E4-04].** Under the 2026-09-20 ruling it is a competence limit, applied only to a name
that passes [E3-03]; Mastech does not. Recorded for completeness: the placements are re-won assignment by assignment
(*"assignment completions tend to be higher near the end of the calendar year"*), and the analytics offering has been
re-labelled with each technology wave (*"social, mobile, data, analytics, cloud"*, now *"AI-first"*). No single great
manager is named by the filing as the source of results; the chief executive changed in December 2024 and the CFO in
April 2025 without a change in the business model. **No key-person defect is recorded [E4-23].**

### THE COMPETITOR ROW - required **[E3-28]**

**Same metric (operating margin on consolidated GAAP figures), same window (latest fiscal year and the year six years
earlier), SEC XBRL companyfacts, `vintage="newest"` (`peers_xbrl.txt`). XBRL transcription, flagged as such: the MHH
row was checked against its filed statements and ties; the peer rows were not opened in their filings, and the verdict
does not rest on them.**

| Company | op. margin, latest FY | op. margin, six years earlier | revenue latest FY $M | revenue change, latest FY | latest FY | how it enters the row |
|---|---|---|---|---|---|---|
| **Mastech Digital (MHH)** | **0.0%** | 8.8% reported, 5.6% adjusted (FY2019) | 191.4 | **-3.8%** | FY2025 | subject |
| Cognizant (CTSH) | 16.1% | 14.6% | 21,108 | +7.0% | FY2025 | named by MHH (analytics) |
| Kforce (KFRC) | 3.8% | 5.6% | 1,329 | -5.4% | FY2025 | CTG's pay peer group, with MHH |
| Robert Half (RHI) | 1.4% | 10.2% | 5,379 | -7.2% | FY2025 | US staffing, added |
| Kelly Services (KELYA) | -1.6% | 1.5% | 4,251 | -1.9% | FY2025 | US staffing, added |
| BGSF | -9.5% | 6.8% | 93 | -10.6% | FY2025 | names MHH in its performance-graph peer group |
| GEE Group (JOB) | -26.2% | -3.3% | 97 | -9.7% | FY to 2025-09-30 | in BGSF's peer group with MHH |
| Resources Connection (RGP) | -8.5% | 6.9% | 452 | -18.0% | FY to 2026-05-30 | in BGSF's peer group with MHH |
| Information Services Group (III) | 7.3% | 5.0% | 245 | -1.2% | FY2025 | CTG's pay peer group, with MHH |
| EPAM Systems (EPAM) | 9.5% | 13.2% | 5,457 | +15.4% | FY2025 | CTG's pay peer group, with MHH |
| Tata Consultancy Services · Capgemini | **not obtained** | | | | | named by MHH; no SEC registrant (Indian and French listings) |
| ASGN · Cross Country Healthcare | **not obtained** | | | | | CTG's peer group; the tool's ticker map returned 404 for both |
| Computer Task Group · Perficient | **not obtained** | | | | | CTG's peer group; no longer filing (taken private) |

- **Peers: MHH names 3 competitors (Cognizant, TCS, Capgemini) plus "smaller boutique" firms and, in staffing, whole
  classes (*"outsourcing services, systems integrators, computer systems consultants, other staffing services
  firms"*); same-metric figures obtained for 1 of the 3 named, plus 8 filers that list MHH in their own peer groups or
  are US IT staffing registrants.** EDGAR full-text search of 10-Ks filed 2023-2026 for "Mastech" returned two other
  registrants naming it: BGSF's FY2025 10-K (*"Our peer group includes: GEE Group, Mastech Digital, and Resources
  Connection, Inc."*) and Computer Task Group's FY2022 10-K (pay peer group). Neither calls MHH a competitor in terms;
  both place it in the same class. **For a moat CLAIM this would hold the class PROVISIONAL. It does not here, because
  the verdict below rests on the registrant's own description of how it is bought**, and no peer's margin can reverse a
  filed statement that clients use several suppliers, choose partly on price, and can end the contract without
  penalty (the ICFI, CRUS and QCOM precedent).
- **What the row shows, including the part that cuts for MHH.** (i) **The 2025 downturn hit the whole staffing class**:
  Robert Half fell from 10.2% to 1.4%, Kelly, BGSF, GEE and RGP are loss-making; Mastech's 0.0% is in the middle of the
  staffing names, not the bottom. Stated plainly because [E4-26] requires it: part of Mastech's collapse is the cycle
  every supplier shares. (ii) **The two names in the row that grew are the large offshore-delivery IT services firms**
  (Cognizant +7.0%, EPAM +15.4%), with margins of 9.5-16.1%; Cognizant is the competitor MHH names in analytics.
  (iii) Nobody in the staffing half of the row earns what [E3-03]'s demonstration clause describes in any year shown.
  (iv) The row's limit [E3-61]: *"In some businesses, the participants behave like a demented Kellogg. In other
  businesses, they don't. ... I think you'd have to know the people involved"*. The row shows where each firm stands;
  it cannot show how an MSP will score the next requisition.

### The remaining Q2 tests
- **[E3-33] / [E5-28], untapped pricing power: No.** Claiming it is claiming *"a monopoly or a near monopoly"*; the
  filing describes a fragmented industry with *"relatively few barriers to entry"*.
- **[E4-37], the agony metric:** *"it's not a great business when you have to have a prayer session before you raise
  your prices a penny"*. Mastech's own words on inflation: *"whenever possible, seek to ensure that billing rates
  reflect increases in costs due to inflation"*, and on the downturn: *"In a softer demand environment, competitive
  pricing conditions also affected our gross margins."* Passing costs through when possible is the prayer session.
- **[E2-44], the two-characteristic test.** (1) *"an ability to increase prices rather easily ... without fear of
  significant loss of either market share or unit volume"*: **fails** (units fell 33% from 2021 to 2025 while the rate
  rose on mix). (2) *"large dollar volume increases ... with only minor additional investment of capital"*: **passes on
  plant** (capex $0.4M) and **fails on working capital and acquisitions**: revenue growth of $28M in 2021 took $11.4M
  of receivables, and the analytics segment was bought for $44.1M of acquisition cash plus the deferred payments.
- **[E3-46], the second question about the business:** on tangible capital the return has been moderate in good years
  (operating income of $12.2-17.6M in 2019-2022 against tangible operating capital of roughly $19-32M at the year-ends 2019-2022:
  receivables, unbilled and prepaid less payables and accruals, plus equipment; 10-Ks FY2020 and FY2022), and nil in 2023-2025 (operating income -$9.3M, $3.8M, $0.0M). A people business earns a
  high return on tangible assets by construction; the corpus asks for that return to be *"demonstrated by"* aggressive
  pricing, and here it has not held through one cycle.
- **[E2-45], the attacker's test:** *"how I would like, assuming I had ample capital and skilled personnel, to compete
  with it"*. With a recruiting team and an H-1B practice, the attack is ordinary: get on the MSP's vendor list and
  submit candidates faster. The registrant says the barriers are *"relatively few"*.
- **[E2-53], the dominance class:** *"Once dominant, the newspaper itself, not the marketplace, determines just how
  good or how bad the paper will be."* Mastech is not in this class; in 2025-2026 its clients and their MSPs determined
  how good its year would be, and one of them decided to do the work itself.
- **[E2-58], the commodity equation:** *"persistent over-capacity without administered prices (or costs) equals poor
  profitability"*. A fragmented industry with *"relatively few barriers to entry"*, a shared candidate pool and
  intermediaries whose job is to *"drive down overall costs"* is that equation, and the margin table is its result.
- **[E4-32], direction:** the filing shows the moat, if any, narrowing: MSP and GCC share rising, a top-ten client
  insourcing, analytics revenue down 18% from 2022 to 2025. **Direction: narrowing.**
- **[E4-36] / [E3-51], which cause of success:** the best years (2019, 2021-2022) coincide with tight technology labour
  markets and a pandemic-era hiring wave, and the analytics segment was bought to ride the data wave. Wave-riding in the
  corpus's sense; the wave belongs to the labour market.
- **[E3-62], the second step:** the gains from Mastech's own efficiency (the offshore recruiting centre, AI sourcing
  tools, the finance function moved to India for *"annualized cost savings of approximately $1.2 million"*) go where the
  MSP's next rate card puts them; the filing itself says the MSP exists *"to manage their contractor expenses in an
  effort to drive down overall costs"*.

### THE VERDICT, AND THE REASONING STATED SO IT CAN BE ATTACKED

**Mastech is a small, competently financed IT staffing and consulting firm, and not a franchise.** [E3-03] asks whether
customers think the service has no close substitute. Mastech's customers answer by how they buy: they *"engage multiple
staffing providers"*, award assignments on *"qualifications, availability, and pricing"*, hand vendor selection to an
MSP whose purpose is to cut their contractor costs, trade volume for *"better pricing"* on preferred-vendor lists, and
can terminate *"without penalty"*; in 2026 one of the ten largest took the work in-house. The registrant itself says the
barriers to entry are *"relatively few"* and that competition *"may limit our ability to increase our prices"*. Twelve
years of operating margin between -0.4% and 6.9% on an adjusted basis, ending at 0.0%, is the demonstration clause answered
in the negative. **[E2-53] names what is left: the client and its intermediary, not the business, determine how good
Mastech will be.**

**The strongest evidence against the verdict, stated so the verdict can be judged against it:** the analytics segment
earned gross margins of 43.5-49.1% in 2023-2025, well above staffing, and booked $13.5M in Q2 2026 against $9.0M a year
earlier; the average bill rate rose every year but one since 2021 and reached $92.17; the 10-K cites *"consistently low
customer attrition"* and *"long-standing engagements with marquee brands"*; the minority-owned certification opens
set-aside budgets; the balance sheet carries $35.6M of cash and no debt; and much of the 2023-2025 margin collapse is
the staffing cycle that took Robert Half from 10.2% to 1.4%. **[E3-47] warns that closing a file wrongly is the costliest
error class.** I weighed it. The analytics gross margin is a margin before selling costs in a segment the registrant
says competes with Cognizant, TCS and Capgemini, and whose goodwill was impaired twice; the bill rate is mix on a
shrinking book (heads -33% from 2021); "low customer attrition" is unquantified and sits beside a top-ten client
insourcing; and the cycle explains why margins fell, not why they never rose above 7%. None of it is evidence that
Mastech's clients cannot choose someone else. **[E5-42] keeps the two judgments apart**: this is a question about whether
the advantage belongs to the business, and on the filing it belongs to the buyer.

**Why OUT and not the perimeter close (UNKNOWABLE at Q2).** The 2026-09-20 ruling reserves UNKNOWABLE for *"A name that
passes [E3-03] and whose durability cannot be judged from filings"*. Mastech does not pass [E3-03]: criterion (2) fails
on the registrant's own description of multi-supplier, price-inclusive buying through intermediaries, terminable
without penalty, and on a top-ten client's insourcing; the demonstration clause fails on twelve years of margins. What
I cannot judge is how the "AI-first" repositioning will fare, and I do not need to.

- **Untapped pricing power** **[E3-33]**: none.
- Class: [ ] WIDE [ ] NARROW **[x] NONE** [ ] PROVISIONAL · **Direction: narrowing (MSP and GCC share of staffing
  revenue about 30% and rising; consultants on billing 1,261 to 840, 2021 to 2025, and -22.3% more by Q2 2026; a
  top-ten client insourcing; analytics revenue $40.6M to $33.3M, 2022 to 2025).**
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

> **Q2 closes the file. Under the hard sequence (operator rule 2), no verdict below this point is reached and no Q5
> clearance exists.** What follows is recorded beneath the close, as the ICFI, CRUS and CVS runs did, because the brief
> asked for the owner-earnings rebuild and because a later reader deciding whether to reopen Q2 needs it. None of it is
> a verdict and none of it promotes the name.

## Q3 - ARE THEY HONEST, AND ARE THEY RATIONAL?
**VERDICT: NOT REACHED** (Q2 closed the file). *Recorded beneath the close as prompts, without a verdict. IN would
never have promoted the name; nothing here repairs Q2 [E2-37, E2-38, E3-39].*

- **Weight case, had it been declared:** **daily execution** would be ticked. Every requisition is a new contest
  against the other suppliers on the MSP's list, and [E3-43]'s *"a business, unlike a franchise, can be killed by poor
  management"* applies to a name that failed [E3-03]: the have-to-be-smart-every-day class [E3-38]. **Control** is not
  the investor's here, which is the point worth recording: the founders hold about 56-58% and *"have sufficient voting
  power to elect all the members of the Board of Directors"*, so an outside owner cannot change a manager he judges
  wrong. **Leverage**: none (no bank debt since January 2023). **So Q3 would have been a binary gate.**
- **Honesty matters found, dated to publication:** no conduct finding against a named person in the documents read.
  Item 3 of the FY2025 10-K: routine proceedings, *"should not have a material adverse effect"*. The 2023 settlement of
  a former employee's *"various employment-related claims"* for $3.1M net of recoveries, plus $0.9M of fees, is under
  a confidential agreement and the filing does not say what was claimed. **Absence of a found matter, not a finding of
  honesty [E5-17].**
- **THE PRIMENTOR AGREEMENT, the sharpest prompt, dated 2024-01-19 (8-K `0001193125-24-011240`).** The company
  engaged Primentor Inc., owned by Phaneesh Murthy, as a strategy consultant, in an agreement **to which the two
  founders are also parties**. The company pays: $100,000 a month for nine months, stepping down to $20,000, plus a
  $120,000 lump sum, and options on **385,000 shares** (about 3.2% of the count) at $8.34. The founders pay, personally,
  on a "Sale Event": *"an aggregate number of shares of Common Stock held by the Founders ... equal to 1.1% of the total
  number of shares of Common Stock outstanding"* to each of Murthy and Sengupta, where a Sale Event counts only if
  *"more than 80% of the shares of capital stock of the Company held by the Founders ... are sold"*. **So a consultant
  paid by all shareholders is paid a further bonus by the controlling shareholders for delivering the sale of their
  stake.** It is disclosed, and a sale of the whole company would pay the public holders too; recorded as an
  [E4-27] incentive prompt, not a finding. **Its cost is reported three different ways**: the FY2024 10-K says 2024
  consulting expense was *"approximately $1.1 million"*; the FY2025 10-K says *"During 2025 and 2024, the Company
  incurred consulting expenses of approximately $0.5 million and $0.4 million"*; the Q2 2026 10-Q says *"During 2024
  and 2025 ... approximately $1.1 million and $0.3 million, respectively"*. The contract's own schedule gives about
  $0.99M of monthly fees for 2024. Two of three filings agree on 2024; no two agree on 2025. **[E4-22]'s first flag as a
  prompt: *"There is seldom just one cockroach in the kitchen."***
- **The other cockroaches, as prompts:** (i) the **public float tagged 1,000 times too large on four consecutive 10-K
  covers** (FY2021-FY2024) and the **FY2025 cover repeating the June 2024 float and date** (Step 0); (ii) the FY2024
  10-K's exhibit index dates the Primentor 8-K to *"January 19, 2025"*, a year late; (iii) **two material weaknesses at
  2020 year-end** (*"management review controls ... related to goodwill impairment, business combinations, revenue
  recognition, share-based compensation, and income taxes"* and IT general controls), remediated in 2021; (iv) in 2025
  the finance function was moved to India and in **December 2025 the auditor, UHY LLP, was dismissed and BDO India
  Services engaged for FY2026** (8-K `0001193125-25-314253`; the 8-K reports no disagreements and UHY's letter agrees).
  Each is small; [E4-22] says to count them together, and [E4-52] says flags that converge are a different event.
  They converge on care, not on concealment; recorded without a finding.
- **What pay vests on [E4-27], from the DEF 14A of 2026-04-09 (`0001193125-26-149074`):** the CEO's 2025 bonus paid
  **123% of goal ($616,932)** on four equal parts: consolidated revenue (target $194.6M, actual $191.4M, paid
  $114,750), gross margin (27.9% against 27.9%, paid $166,667), **"Consolidated non-GAAP diluted EPS" (target $0.63,
  actual $0.72, paid $198,250)**, and a discretionary part ($137,265). **GAAP diluted EPS was $0.05 and operating
  income was $1K.** The non-GAAP figure excludes stock pay, acquired-intangible amortization, severance and the
  finance-transition cost. The revenue target ($194.6M) was set below the prior year's actual ($198.9M). The bonus was
  then paid in 100,314 immediately-vested shares at a $6.15 VWAP, *"issued in settlement of previously accrued cash
  compensation"* (10-Q, note 7), so it never appears in the stock-compensation line. **Prompt: the pay design rewards a
  per-share figure that removes the stock pay itself.**
- **The flags, as prompts:**
  - **[E4-29] EBITDA promotion: reads clean.** EBITDA does not appear in the FY2025 10-K, the Q2 2026 10-Q or any of the
    ten furnished releases read (2024-02-07 to 2026-08-06); it appears only in the DEF 14A's list of permissible plan
    goals. The releases headline **non-GAAP net income and non-GAAP EPS**, excluding stock pay and amortization;
    GAAP is presented first and reconciled line by line. The half-owner test [E2-26] passes on form.
  - **[E4-22] projections / [E3-48] the record:** no numeric revenue or earnings guidance found in the releases read.
    The only forward figure checked: the finance transfer's *"annualized cost savings of approximately $1.2 million
    beginning in 2026"*; H1 2026 SG&A fell $5.2M, of which $2.3M was the absence of H1 2025's severance and transition costs.
  - **Serial issuance [E5-15]: mild, not serial.** Weighted basic shares 11.03M (2019) to 11.75M (2025), cover
    12,012,581 (July 2026), about 1.3% a year, from options, the ESPP (at a 15% discount, terminated from July 2026) and
    the CEO's bonus shares; partly offset by $2.2M of buybacks in 2025 at about $7.50 a share.
  - **[E2-49] metric-switching:** the FY2026 segment change (Talent, Data & AI) was announced in the FY2025 10-K with
    reasons and prior periods recast; **the candor case, not the flag.** But the recast moves staffing revenue into
    "Data & AI" (H1 2025 Data & AI $31.7M against FY2025 Data and Analytics $33.3M for the whole year), so the analytics
    series above does not continue under the new name.
  - **[E4-30] filed-figure tells:** reported growth is not smooth; cash taxes $0.9M against pretax income $1.1M (2025),
    $2.2M against $4.4M (2024). Not tested further.
- **The primary test [E2-01], as a series:** net income against equity: 2020 $9.9M on about $53M average (19%), 2021
  $12.2M on $67M (18%), 2022 $8.7M on $80M (11%), 2023 -$7.1M, 2024 $3.4M on $84M (4%), 2025 $0.6M on $88M (0.7%).
  Equity is about 37% goodwill and intangibles and 39% cash (2026-06-30).
- **Capital allocation, the record.** **[E2-56]'s camouflage test, segment by segment (MD&A table, FY2025 10-K):**
  staffing contributed gross profit less its own SG&A of **$6.0M, $5.4M and $7.7M** in 2023-2025; the analytics segment,
  bought for **$44.1M of acquisition cash** (InfoTrellis and AmberLeaf) and carrying all of the goodwill, contributed
  **-$1.7M, +$3.3M and -$0.2M**, before $2.6-2.8M a year of acquired-intangible amortization, and its goodwill was
  impaired twice. **The base business carries a bought one that has not earned its price.** The buyback prompt [E5-08]
  needs an IV range this run did not reach; recorded only that 2025 repurchases averaged about $7.50 against $7.22 now,
  from $36.5M of cash with no debt, which meets the first condition on its face.
  **In the founders' favour, recorded because [E4-26] requires it:** in 2017 they bought $6.0M of new shares at $7.00
  when the market was $6.35, on terms negotiated by a special committee, and stood behind the InfoTrellis deferred
  payments with an equity-support commitment.

## Q4 - WILL IT SURVIVE?
**VERDICT: NOT REACHED.** *The owner-earnings rebuild the brief asked for, recorded beneath the close. It is not a
verdict.*

### Owner earnings **[E2-23]**, FY2014-FY2025, from the filed cash-flow statements (four 10-Ks, twelve years)
*CONVENTION (framework section VI): operating cash flow less SBC, less the (c) guess.* **No net-income proxy.**

- **SBC resolves and is complete, with one addition.** Subtracted: the cash-flow line *"Stock-based compensation
  expense"* ($3,118K in FY2025), which covers options, restricted stock and the ESPP (*"The fair value of our stock
  options and shares issued under the Company's Stock Purchase Plan is determined at the date of grant using the
  Black-Scholes option pricing model"*; the ESPP discount is 15%). **Added for FY2025: $617K**, the CEO's 2025 bonus
  accrued as cash and settled in stock (*"they did not result in additional stock-based compensation expense, but
  rather, they were issued in settlement of previously accrued cash compensation"*), whose cash therefore never leaves
  through operating cash. SBC was **25.8% of operating cash FY2021-FY2025**. The 385,000 Primentor options are inside
  the line. [E5-06]'s subtraction is complete on the documents read.
- **(c) is carried as a band** [E2-09]: the **capex end** is purchases of equipment and software ($0.1-1.9M a year);
  the **D&A end** is total D&A, which since 2017 is mostly amortization of acquired intangibles ($2.6M of $3.3M in
  FY2025). [E3-44]'s default treats D&A as the proxy and adds back intangible amortization; I keep the D&A end as the
  conservative bound for the ICFI reason, stated: part of this company's position was bought (the whole analytics
  segment), so some of what it paid is arguably the upkeep of position. Band carried whole.
- **The working-capital construction, and why it matters here more than anywhere in the series.** A staffing firm's
  receivables grow with revenue and are released when revenue falls. The releases are the return of capital from a
  shrinking book, not earnings, and the brief asked for single-line artifacts to be stripped. Two constructions are
  shown: **(A) the convention, operating cash as filed**; and **(B) [E2-23] in its own form, (a) reported earnings plus
  (b) the non-cash charges, less SBC and (c)**, which is operating cash with every working-capital line removed. (B) also
  removes the CARES Act deferral (+$4.6M 2020, -$2.3M 2021 and 2022) and the 2018-2019 ERP swing [E4-41].

| FY | OCF | SBC | D&A | capex | working-capital lines | (A) OE, capex end | (A) OE, D&A end | (B) OE, capex end | (B) OE, D&A end |
|---|---|---|---|---|---|---|---|---|---|
| 2014 | 3.3 | 0.3 | 0.1 | 0.7 | -0.7 | 2.2 | 2.2 | 2.9 | 2.9 |
| 2015 | 3.0 | 0.3 | 0.7 | 0.2 | -0.7 | 2.6 | 2.1 | 3.3 | 2.8 |
| 2016 | 2.3 | 0.4 | 1.0 | 0.1 | -1.8 | 1.8 | 0.9 | 3.6 | 2.7 |
| 2017 | 3.3 | 0.4 | 1.9 | 1.1 | -0.5 | 1.8 | 1.0 | 2.4 | 1.6 |
| 2018 | -0.5 | 0.5 | 3.2 | 0.8 | -9.9 | -1.7 | -4.1 | 8.2 | 5.8 |
| 2019 | 16.1 | 0.9 | 3.4 | 1.0 | +5.1 | 14.1 | 11.7 | 9.1 | 6.7 |
| 2020 | 21.2 | 2.0 | 3.6 | 0.3 | +7.3 | 18.9 | 15.6 | 11.6 | 8.3 |
| 2021 | 5.2 | 2.2 | 4.0 | 1.9 | -11.7 | 1.1 | -1.0 | 12.8 | 10.8 |
| 2022 | 12.6 | 2.2 | 4.2 | 0.8 | -2.9 | 9.6 | 6.2 | 12.5 | 9.1 |
| 2023 | 16.0 | 3.1 | 3.9 | 0.3 | +12.5 | 12.6 | 9.0 | 0.1 | -3.5 |
| 2024 | 7.2 | 2.2 | 3.5 | 0.9 | -2.3 | 4.1 | 1.5 | 6.3 | 3.8 |
| 2025 | 11.1 | 3.7 | 3.3 | 0.4 | +7.4 | 7.0 | 4.1 | **-0.3** | **-3.3** |

$ millions. Arithmetic in `Test Runs/_research 2026-09-25 MHH/oe.py` and `oe_out.txt`. (FY2018's (B) excludes the
non-cash $11.1M contingent-consideration credit and $9.7M impairment, as the cash-flow statement does.) **H1 2026
operating cash was -$0.9M** (10-Q), with accrued payroll paid down $3.3M.

- **MORE THAN ONE WINDOW [E4-25]:**

  | window | (A) OCF as filed | (B) working capital stripped |
  |---|---|---|
  | 3 years, FY2023-25 | $4.9M to $7.9M | **-$1.0M to $2.0M** |
  | **5 years, FY2021-25 (the default [E2-42])** | **$4.0M to $6.9M** | **$3.4M to $6.3M** |
  | 7 years, FY2019-25 | $6.7M to $9.6M | $4.5M to $7.4M |
  | 10 years, FY2016-25 | $4.5M to $6.9M | $4.2M to $6.6M |
  | 12 years, FY2014-25 | $4.1M to $6.2M | $4.0M to $6.0M |
  | FY2025 alone | $4.1M to $7.0M | **-$3.3M to -$0.3M** |

  **Combined range across windows, constructions and both (c) ends: -$3.3M to +$9.6M.** In words: over five years or
  more, owner earnings of **roughly $3-10M a year**; **in the latest three years, about nil (-$1.0M to +$2.0M) once the
  cash released by a shrinking receivables book is taken out, and below zero in FY2025.** The (A) figures for 2023 and
  2025 are working capital coming home, not earnings; the screen's $4-8M band is (A) over three years. The range is
  too wide at its current end to price, and that is itself the finding [E4-25, E5-11]: the earning power fell from
  about $9-13M (2021-2022, construction B) to about nil (2023-2025).
- **Great, good or gruesome [E4-20], a prompt only:** on plant, it needs almost nothing; on the capital spent to grow
  (working capital in up-years, $61.1M of acquisitions), the added capital earned little: the bought segment
  contributes about nil after its own costs. **Closer to gruesome on the acquired growth; the staffing base is a
  cyclical earner of $5-8M of segment contribution.** [E4-43]'s satisfactory case needs *"the cash they consume"* to
  earn a reasonable return, and the filings show it did not.
- **Staying power [E5-11], a prompt only:** (1) earnings stream: **small and not reliable** (operating income $17.6M
  in 2021, $0.0M in 2025); (2) **liquid assets strong for the size**: cash $35.6M at 2026-06-30, 41% of the cap, no bank
  debt, $20.4M of unused revolver; (3) **near-term cash requirements small**: operating leases ($2.1M liability, plus
  the new Dallas lease at about $0.22M a year), no debt maturities. **Leverage, named** [E4-16]: none. Coverage [E2-54]:
  no interest to cover.
- **The named way it dies [E2-27, E3-24], as a signature only:** the nearest shape in `Screens/SURVIVAL SHAPES -
  index.md` is **#11 THE PASS-THROUGH** (*"the company survives but gains are passed to customers and suppliers,
  compressing the owner's return"*), with **#19 THE SHELF** as a feature (the route to the buyer is held by an MSP that
  runs the vendor list and, in the filing's words, exists *"to manage their contractor expenses in an effort to drive
  down overall costs"*). The mechanism in the filing: MSPs and clients' offshore centres take the rate, clients take
  the work in-house, and every efficiency Mastech finds is competed away at the next requisition [E3-62].
  **Quantified**: Talent revenue fell 16.2% year on year in Q2 2026; another year at that rate on H1 2026's annualised
  $113M takes about $18M of revenue and, at the 22.8% H1 gross margin, about $4M of gross profit, against FY2025
  operating income of $1K and staffing's $7.7M segment contribution. **The company lives on its cash; the owner's return
  goes to nil or below until SG&A is cut to match.** Likelihood: **a real possibility**, on exposure, not experience
  [E4-40]: the insourcing is under way. **Not entered in the index's instances column**, for the reason the PAGP, CALM
  and ICFI folds gave: the file closed at Q2, so no Q4 death was reached. No new shape is proposed.

---
⛔ **Q5 does not open. Q2 is OUT.**

---
## Q5 - WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?
**VERDICT: NOT REACHED.** No ranking position exists; a name that failed Q2 is not ranked.

### COMPUTATION — NOT A CLEARANCE
*Arithmetic only, no box ticked, no entry language. Produced because the queue records it for every run.*
- **Yield on the $86.7M cap:** five-year owner earnings (A) $4.0-6.9M = **4.6% to 8.0%**; (B) $3.4-6.3M = 3.9% to 7.3%;
  three-year (B) -$1.0M to $2.0M = **-1.2% to 2.3%**; FY2025 (B) below zero. Sovereign **5.47%**.
- **The cash:** $35.6M of the $86.7M quote is cash (2026-06-30), and about $0.8M a year of interest on it is inside
  operating cash. Ex cash, the operating business is priced at about $51M; five-year (B) less FY2025's $0.8M of interest, about
  $2.6-5.5M, is 5.1% to 10.8% of it; three-year (B), below 2%.
- **At the ~10% floor [E4-28] with no growth:** five-year (B) capitalised at 10% plus cash is **$70-99M against an
  $86.7M quote**; three-year (B) on the same construction, **$26-56M**. The quote sits inside the five-year range and
  above every construction on the recent level; clearing it needs the earning power of 2019-2022 back, which the
  filings of 2023-2026 do not show.
- **Windage count: ONE** (construction B's removal of working-capital releases and the CARES deferral, [E4-41]); the
  (c) band, the window spread and construction A are displayed, not spent. The $617K bonus adjustment is a completeness
  correction under [E5-06], not windage.

## Q6 - WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
**VERDICT: NOT REACHED** (nothing to sell; no position). **The reversal conditions, in words, for whoever reopens Q2**
(the QLYS ruling: a Q2 failure gets no price alert):
1. **Evidence that clients do not re-source Mastech's work**: a 10-K in which a material share of revenue is under
   multi-year contracts not terminable without penalty, or from licensed IP or platforms (the "AI-first" Data & AI
   segment sold on terms rather than hours), and the multi-supplier and low-barrier language in Items 1 and 1A narrows
   accordingly.
2. **[E3-03]'s demonstration clause turning**: operating margin above about 10% for five consecutive years on organic
   revenue growth, above Kforce and Robert Half across a staffing downturn.
3. **Units and rate rising together**: consultants on billing growing while the average bill rate rises, and the MSP
   and GCC share of staffing revenue falling.
- **The moat-downgrade question, for the record [E3-30]:** the 2023-2025 fall is partly the staffing cycle every peer
  shares (aberrational) and partly the structure the cycle exposed (clients buy through intermediaries and can take the
  work in-house). The first may be made up; the second is the Q2 finding and does not bounce back.
- **Next catalyst dates:** the Q3 2026 release (no date announced in the 8-Ks read; the Q3 2025 release came on
  2025-11-12); the FY2026 10-K (about March 2027), the first audited by BDO India and the first under the Talent and
  Data & AI segments, where conditions 1 and 3 would first appear.

## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Step 0, Q1 IN, Q2 OUT; Q3-Q6 marked NOT REACHED and their
      material recorded beneath the close without verdicts.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the 10-K's own
      description, confirmed clause by clause.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives: none issued. The unobtained peers are named at
      Q2 with the reason (no SEC registrant, or the ticker map failed, or no longer filing).
- [x] Every UNKNOWABLE verdict states what specifically cannot be known: none issued; the perimeter close was
      considered at Q2 and refused in writing.
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked (FY2025 operating cash $11,135K
      rebuilt from its lines; ties). The screen's cap flag was settled from the 10-K cover text.
- [x] Owner earnings on a multi-year mean; six windows and two constructions stated; capex band disclosed as a judgment
      (beneath the close).
- [x] Competitor row filled: Cognizant (1 of 3 named) plus eight peer-group or US staffing filers, XBRL transcription
      flagged; the verdict does not rest on the row, and why is stated.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury par curve), dated
      09/24/2026.
- [x] Value stated as a round-number range, not a point estimate (inside a COMPUTATION block only).
- [x] One bar chosen, not both: none; Q5 not reached. Windage count stated (one).
- [x] Prices dated; aggregator used for the live quote only and flagged, with its thin volume recorded.
- [x] Run committed to git, with pathspecs, after the claim, after Step 0 and Q1, after Q2 and after this section.
- [x] Ledger ids: the run file cites **65 distinct ids**; every one resolved against `principle_ledger.csv` (311 rows
      by `csv.DictReader`) before citing, quotes taken from `quote_verbatim` (pull saved as `ledger_rows.txt`).
      `python tools/check_framework.py`: **PASS** (phantom citations 0 across 1,219 run files; output in
      `check_out.txt`).

**The brief's priors, scored:**
- *IT staffing plus a data-and-analytics segment; spun off from iGATE around 2008*: **confirmed** (separated
  2008-09-30).
- *Analytics built by acquisition, InfoTrellis around 2017, AmberLeaf around 2020*: **confirmed** (July 2017, October
  2020); the brief omitted Hudson IT (2015, $17.0M), which built part of the staffing side.
- *Goodwill and intangibles a meaningful share of equity*: **confirmed** ($33.8M of $91.8M), after $15.0M of
  impairments the brief did not mention.
- *Founders' families hold a large, possibly controlling, stake*: **confirmed, controlling** (about 58% per the 10-K;
  56.4% across the three DEF 14A lines). Related-party dealing found: the Primentor agreement, to which the founders
  are parties (Q3).
- *Revenue declined after 2022; restructurings, CEO changes, buybacks, deal-shaped 8-Ks*: **confirmed** on decline,
  CEO change (December 2024), CFO change (April 2025), severance each year 2023-2025, a 2025 buyback and a 2026
  authorisation; **no deal-shaped 8-K**, but a consultant incentivised on a sale of the founders' stake.
- *The cap flag is a scale error in the tagged float*: **confirmed** from the cover text (FY2021-FY2024 covers tagged
  1,000x).
- *The 2021 payables swing*: **confirmed in arithmetic, refuted as a description**: 2021 working capital was a use of
  $11.7M; payables offset part of it.

**My own errors, caught before commit:**
1. First wrote tangible operating capital for 2019-2022 as "roughly $20-35M" before computing it; the balance sheets
   give about $19-32M. Corrected before the Q2 commit.
2. First computed FY2025 owner earnings with SBC from the line alone; the 10-Q note shows the CEO's $617K bonus was
   settled in stock outside the line. Added.
3. My first `compact.py` table parser dropped negative figures printed as "( 7,138)" with a space inside the
   parenthesis, so the first cash-flow extraction read partial lines; caught on the first read and fixed before any
   figure was used.
4. A ledger-row dump first failed on the console's cp1252 encoding and left a truncated file; rerun with UTF-8.

**Errors in the brief:** (1) *"267 rows"* for `principle_ledger.csv`: `csv.DictReader` returns **311** (the count in
CLAUDE.md's key-files table is stale; the resume state records 311 since 2026-09-20). (2) The priors omit Hudson IT
and the two goodwill impairments. Neither affected a verdict. The brief's "WAVE 7 name 34 of 218" was counted and is
right.

**Tooling observations (reported, not patched):**
- **`tools/run.py MHH` and the screen band count working-capital releases as owner earnings.** Its three-year band
  ($5-8M) includes $12.5M (2023) and $7.4M (2025) of receivables released by a shrinking book; with working capital
  stripped the same three years are -$1.0M to +$2.0M. Generous direction. Any shrinking staffing or services filer
  will carry it.
- **`working_capital_flag()` (the screen's `wc_note`) names a line that moved more than 30% of operating cash without
  checking the sign of total working capital.** For MHH 2021 it printed *"ONE LINE MADE THE CASH: AccountsPayable moved
  45% of 2021 OCF"*, when that year's working capital was an $11.7M use and payables offset part of it. The flag is a
  prompt and it did its job of sending me to 2021; its sentence says the opposite of what happened.
- **`regen_queue.py`'s cap flag fired correctly and could not say which side was wrong.** The float was tagged 1,000x
  too large by the filer on four covers. A check of dei:EntityPublicFloat against the previous year's float (it jumped
  from $81.7M to $47,201M between the FY2020 and FY2021 covers) would have named the float as the broken input.
- **`run.py` cannot see stock-settled bonuses** accrued as cash (MHH FY2025, $617K); no tag separates them.
- `sources.cik_for()` returned HTTP 404 for ASGN and CCRN in `peers.py`; not investigated.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- One line: **MHH FAIL at Q2 (OUT, ON THE BUSINESS). Q1 IN. [E3-03] criterion (2) fails on the registrant's own words:
  clients *"engage multiple staffing providers"* and award assignments on *"qualifications, availability, and
  pricing"*, MSPs control vendor selection, preferred-vendor status trades volume for price, contracts are *"terminable
  without penalty"*, the barriers to entry are *"relatively few"*, and a top-ten client is insourcing; operating margin
  -0.4% to 6.9% (adjusted) for twelve years and 0.0% in FY2025; consultants on billing 1,261 to 840 (2021-2025); [E2-53]: the
  client and its intermediary, not the business, set how good it will be.** Price $7.22 (2026-09-24, aggregator,
  flagged, thin volume) x 12,012,581 shares (10-Q cover, `0001193125-26-337054`) = $86.7M; sovereign 5.47% (US Treasury,
  09/24/2026).
- **If UNRESEARCHED:** not applicable.
- **If UNKNOWABLE:** not applicable.

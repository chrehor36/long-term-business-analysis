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


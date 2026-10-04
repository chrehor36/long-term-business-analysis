# Company Run - ICF International, Inc. (ICFI) - 2026-09-25
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

*CLAIMED 2026-09-25 05:50 EDT (write-early; no `*Run - ICFI *.md` existed in `Test Runs/`). Research folder `Test Runs/_research 2026-09-25 ICFI/`. WAVE 7 name 33 of 218 (counted: line 33 of `_wave7_order.txt`; 32 lines in `_wave7_done.txt` at claim). Unattended session. Sections below are filled as they close.*

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
- rate **5.47** % · date **09/24/2026** (the newest row on the curve when this run struck it, about 05:50 EDT on
  2026-09-25) · source (issuing authority) **US Treasury daily par yield curve, 30 Yr, `home.treasury.gov`
  daily-treasury-rates.csv for 2026**, struck fresh by this run and saved raw as
  `Test Runs/_research 2026-09-25 ICFI/treasury_2026.csv`; `python tools/sources.py` returned the same figure and
  date. Neighbouring rows 5.40 (09/23), 5.29 (09/22). **FRED DGS30 was not used.**
- FX: **not required.** The registrant reports in US dollars; international government clients were 7% of FY2025
  revenue, and the MD&A names the euro and the pound as *"the principal currencies in which we transact"* outside
  the US (foreign-currency loss $2.5M in FY2025). USD sovereign.

**The filing was read** - not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K for the year ended 2025-12-31, filed 2026-02-27, accession `0001193125-26-082536`**
    (`icfi-20251231.htm`). Read: Item 1 whole (overview, markets, strengths, strategy, client and contract mix,
    backlog, business development, competition, IP, regulation); Item 1A in the parts cited below (appropriations,
    the Administration and DOGE terminations, competitive bidding, termination for convenience, fixed-price
    estimates, protests, audits); Item 7 MD&A whole; the income statement, balance sheet and cash-flow statement with
    every reconciliation line; notes on restricted cash, receivables sold to MUFG, goodwill and intangibles,
    stock-based compensation (including cash-settled RSUs and the ESPP), the 401(k), acquisitions.
  - **10-Ks FY2022 `0000950170-23-005304`, FY2019 `0001564590-20-007616` and FY2016 `0001437749-17-003385`**, each
    carrying three years of cash-flow and income statements, so **FY2014-FY2025 (twelve years) is covered without a
    gap** from filed statements. FY2024 `0000950170-25-029917`, FY2023 `0000950170-24-021617` and FY2020
    `0001564590-21-009169` 10-Ks opened for dated language (competitive factors, client mix, acquisitions).
  - **10-Q for the quarter ended 2026-06-30, filed 2026-08-06, accession `0001193125-26-338422`** (cover, balance
    sheet, cash-flow statement, notes on restricted cash, receivables sold, leases, the new credit agreement).
  - **8-K EX-99.1 earnings releases** for Q4 2024 (2025-02-27), Q1-Q3 2025, Q4 2025 (2026-02-26, `0001193125-26-076573`),
    Q1 2026 (2026-05-07) and **Q2 2026 (2026-08-06, `0001193125-26-337985`)**; the 2026-06-25 buyback release; the
    2026-09-24 8-K (Item 2.02, **only the date of the Q3 release, 2026-11-05**; no figures).
  - **DEF 14A filed 2026-04-22, `0001140361-26-016102`**, downloaded; read only if the file reaches Q3.
- **deal_note, opened:** the one 8-K with Item 1.01 since 2026-02-27 is **`0001437749-26-012565` (filed 2026-04-16,
  event 2026-04-10)**: an *"Amended and Restated Credit Agreement"* with PNC as agent that maintains a $600M
  revolver, raises the term loan from $300M to $450M, keeps a $400M delayed-draw term loan, replaces the leverage
  covenant with *"a maximum Consolidated Net Leverage Ratio covenant, which is maintained at a maximum of 4.50 to
  1.00"*, extends maturity to 2031-04-10, and is *"secured by a first-priority security interest in substantially
  all of the assets"*. **A credit facility, not a merger.** The submissions index for 2025-2026 lists no S-4, 425,
  DEFM14A or tender filing. **Nothing deal-shaped is live; the quote is an owner-earnings price, not a spread.**
- figure cross-checked against the filed statement: **FY2025 net cash provided by operating activities, $141,870K**,
  rebuilt from its own reconciliation lines: net income 91,588 - credit-loss provision 429 + deferred taxes 5,078 +
  non-cash equity compensation 17,686 + D&A 58,147 + other 2,325 = 174,395; working-capital lines +25,369 + 22,031 +
  2,944 - 8,366 - 36,827 - 10,843 - 1,952 - 13,019 - 11,694 - 168 = **-32,525**; total **141,870. Ties.** The XBRL
  pull (`peers_xbrl.txt`) reproduces FY2025 revenue $1,872.9M and operating income $145.5M against the filed income
  statement ($1,872,851K and $145,465K).
- *If the filing could not be obtained -> **UNRESEARCHED**.* **Not invoked; every document came from SEC EDGAR primary
  documents.**

**THE PRICE AND THE CAP** *(struck by this run, not carried from the screen)*
- **Share count, quoted from the cover of the 10-Q for 2026-06-30, accession `0001193125-26-338422`:** *"As of July
  31, 2026, there were 17,933,884 shares outstanding of the registrant's common stock."* One class of common
  ($.001 par, 70,000,000 authorized); *"Preferred stock, par value $ .001 ; 5,000,000 shares authorized; none
  issued"* (balance sheet). No classes summed. `python Screens/cover_shares.py ICFI` returned the same document,
  accession and count.
- **Price $83.00** (close 2026-09-24, **aggregator quote, flagged**: Yahoo Finance chart endpoint,
  `regularMarketTime` 2026-09-24 20:00 UTC; raw response saved as `price_raw.json`). Two-year closing range in the
  same pull **$59.90 to $176.06**. No split event in the pull. A null close for 2026-09-22 in the aggregator's
  series, recorded not filled.
- **cap = close x shares**, split-invariant, `close` never `adjclose`: $83.00 x 17,933,884 = **$1,488.5 million.**
- The screen's $1,619M implies about $90 a share on this count; a price from early September, no cap flag to resolve.

**THE PERIMETER, read before any question. The screen's `acq_note` sees only the five-year window [E4-25].**
From the filed cash-flow statements, *"Payments for business acquisitions, net of cash acquired"*:

| year | $M | what the 10-Ks name |
|---|---|---|
| 2014 | 347.9 | Olson (*"aggregate purchase price of approximately $298.2 million in cash"*, FY2016 10-K) |
| 2015-2017 | 2.0 | small |
| 2018 | 34.6 | The Future Customer, DMS Disaster Consultants, We Are Vista |
| 2019 | 3.6 | small |
| 2020 | 253.3 | ITG (Incentive Technology Group), January 2020 |
| 2021 | 174.5 | ESAC (*"approximately $ 17.3 million"*) and Creative Systems (*"$ 156.6 million"*, final) |
| 2022 | 237.3 | SemanticBits (the balance) and Blanton & Associates (*"$ 22.9 million"*) |
| 2023 | 32.7 | CMY Solutions (*"$ 32.6 million in cash"*); **less $51.3M received** for the divested US commercial marketing business |
| 2024 | 55.0 | Applied Energy Group |
| 2025 | 0 | none |

**$1,141M spent on acquisitions FY2014-FY2025, $500M of it FY2021-FY2025 (the screen's figure, confirmed to within
$1M), against a $1,488.5M cap.** Goodwill is **$1,251.5M** at 2026-06-30 and intangibles $68.4M, against total equity
of $1,049.9M: **tangible equity is about -$270M.** The acquired businesses are inside the owner-earnings series from
their purchase year onward, so the numerator and the cap describe the same perimeter only from FY2025 (Applied Energy
Group closed in December 2024); every earlier year is a smaller company. This is carried to Q4 as a window issue, and at Q3 as a capital-allocation prompt.

**Two cash items that are not the owner's, found in the notes and carried to Q4:**
1. **Restricted cash from the utility energy-efficiency programmes flows through operating cash.** *"Restricted cash
   is primarily related to the Company's energy incentive business with public utility clients and restricted cash
   advances on certain programs"* (FY2025 10-K, Note 3). Restricted cash rose $3.1M (2023) to $13.9M (2024) to
   $51.0M (2025) to $99.3M (2026-06-30), and the Q2 2026 release says *"Cash flows from operations were $99.7 million
   in this year's second quarter, including $43.0 million in restricted cash tied to energy efficiency programs"*;
   the company's own 2026 guidance is stated *"excluding the impact of restricted cash"*. In 2020-2022 a different
   restricted balance (advances under a contract commenced Q4 2020) was classified in **financing**, not operating
   cash, and does not touch the series.
2. **Receivables sold to MUFG without recourse**: net operating-cash effect -$7.3M (2025), +$6.2M (2024), -$4.4M
   (H1 2026). Small; recorded, not adjusted.

---
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

*Priors from the brief, stated as hypotheses and tested against the filing:*
- *"Consulting / technology-services contractor, roughly half or more of revenue from US federal agencies"*:
  **confirmed in kind, refuted in size for the latest year.** Federal was **54-55%** in FY2022-FY2024 and fell to
  **43%** in FY2025 (39.0% in Q2 2026); it was 38-51% across FY2014-FY2021. State and local 17%, international
  government 7%, **commercial 33%** in FY2025 (24% in FY2023). Contract mix FY2025: time-and-materials 43%,
  fixed-price 50%, cost-based 7% (cost-based was 14% in FY2023). Prime on about 86% of revenue.
- *"2025 federal terminations, particularly USAID and HHS-type programmes"*: **confirmed for HHS, not found for
  USAID by name.** The MD&A: federal revenue fell **$279.5M** in FY2025, *"primarily as a result of terminated
  contracts in 2025 due to the Administration's changing priorities and the actions recommended by DOGE, as well as
  the disruption in the typical U.S. federal government procurement cycle"*; Health and Social Programs fell
  $144.4M (18.9%), with $156.6M of that from federal clients. HHS was **26%, 25% and 22%** of revenue in FY2023-FY2025.
  USAID appears in the FY2025 10-K only as a cost-audit agency (*"through 2015 for our USAID-cognizant indirect
  rates"*); no USAID revenue figure was found in the documents read.
- *"Acquisitions SemanticBits and ESAC in 2022, ITG earlier"*: **partly refuted on dates.** ESAC closed November 2021
  (about $17.3M), Creative Systems December 2021 ($156.6M), SemanticBits July 2022, ITG January 2020. Table above.

- **Unit economics in my own words.** ICF rents out the time of about 8,400 people (42% of the benefits-eligible
  staff hold post-graduate degrees) to governments, utilities and companies, and passes through subcontractor and
  other direct costs ($454.0M, 24% of FY2025 revenue). The customer pays by the hour at an agreed rate
  (time-and-materials), a fixed sum for a defined job (fixed-price, where ICF keeps the saving or eats the overrun),
  or its costs plus a fee (cost-based). Work is won by bidding: on federal task orders under GSA Schedules and IDIQ
  vehicles *"we compete for each delivery order and task order"*; contracts run *"from one month to five years,
  including option periods"*, and *"our existing contracts regularly become subject to re-competition and
  expiration"*. **FY2025 in one line: revenue $1,872.9M, direct costs $1,176.8M (62.8%), indirect and selling
  $492.4M (26.3%), D&A $58.1M (of which $37.0M is amortization of acquired intangibles), operating income $145.5M
  (7.8%).** Capital needs are small (capex $21.7M); the capital that matters is the purchase price of acquired firms.
  **The commercial third** is mostly running utilities' energy-efficiency and load-management programmes
  (*"approximately 82%"* of Q2 2026 commercial energy revenue), won and re-won by competitive contract.
- **The scarce input this business controls:** trained professional staff with subject-matter knowledge, the
  past-performance record and the contract vehicles (GSA Schedules, IDIQs, MSAs) that let it bid, and relationships
  that span decades (management's 279 vice-presidents average about 18 years' tenure). Whether any of that is
  scarce **relative to the customer's alternatives** is the Q2 question.
- **Will the fundamentals look broadly the same in ten years?** The mechanism will: governments and utilities will
  buy professional hours by competitive procurement. The mix will not stay still: FY2025 shows 11 points of federal
  share lost in one year to a customer decision, and the filing names AI (its *"ICF Fathom AI platform"*) as both an
  offering and a risk. That is a question about durability and bargaining power, which [E4-04] and the 2026-09-20
  ruling place at Q2; it is carried there, not used to close Q1.
- **The five-minute test [E4-46]:** the business can be stated in a paragraph and the filing confirms each clause.
  Nothing here needs months of study.
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

## Q2 - IS IT A FRANCHISE? **[E3-03]**

> *"An economic franchise arises from a product or service that: (1) is needed or desired; (2) is thought by its
> customers to have no close substitute and; (3) is not subject to price regulation. The existence of all three
> conditions will be demonstrated by a company's ability to regularly price its product or service aggressively and
> thereby to earn high rates of return on capital."* **[E3-03]**, 1991 letter

**The hypothesis I formed while reading, stated so it can be attacked [E4-26]:** *ICF sells professional hours into
competitive procurements run by customers who can and do switch, so the customer, not ICF, holds the terms.* The
evidence against that hypothesis was hunted first and is set out before the verdict.

### The three criteria, on the registrant's own words

- **(1) Needed or desired: PASSES.** Revenue $1,872.9M in FY2025, backlog $3,405.0M at year end ($3.3bn at
  2026-06-30), a trailing twelve-month book-to-bill of 1.09 at Q2 2026, and customer relationships the filing says
  *"span decades"*.
- **(2) Thought by its customers to have no close substitute: FAILS, on the registrant's own description of how it
  is bought and on what its largest customer did in 2025.**
  - **The customer buys by competition, task order by task order.** *"We derive significant revenue and profit from
    contracts that are awarded through competitive bidding processes"*; under GSA Schedules and IDIQ vehicles *"we
    compete for each delivery order and task order, rather than having a more predictable stream of activity during
    the term of a multi-year contract"*; and *"Even if we win a particular contract through competitive bidding, our
    profit margins may be depressed, or we may even suffer losses as a result of the costs incurred through the
    bidding process and the need to lower our prices to overcome competition"* (FY2025 10-K, Item 1A; the same
    sentence stands in the FY2016 and FY2019 10-Ks).
  - **The customer re-buys, and may shut ICF out.** *"our existing contracts regularly become subject to
    re-competition and expiration"*; *"the client may not re-procure those requirements, re-procurement may be
    restricted in a way that would eliminate us from the competition (e.g., set asides for small businesses), or we
    may not be successful in any such re-procurements"*. Contract terms run *"from one month to five years,
    including option periods"*.
  - **The customer can stop at will, and did.** *"Certain contracts contain provisions that allow our clients to
    terminate or modify these contracts at their convenience on short notice"*, and when that happens ICF *"would have
    no right to seek lost fees or other damages"*. In 2025: *"Pursuant to the executive orders issued by the
    Administration and actions by the Department of Government Efficiency ("DOGE"), we received contract terminations
    and temporary stop-work orders primarily in the first and second quarters of 2025"*. **Federal revenue fell
    $279.5M in one year** (MD&A), federal share 54% to 43%, HHS 25% to 22%, total revenue -7.3% ($2,019.8M to
    $1,872.9M), and Q2 2026 federal revenue was still 9.5% below Q2 2025. Severance on those terminations was, in the
    company's words, *"for which the Company was not reimbursed, or will not be reimbursed, by our federal government
    customers"*. The customer that was 54% of revenue cut, inside two quarters, work that (with the slower procurement
    that followed) took about a quarter of its annual spend with ICF (federal revenue about $1,091M in FY2024), and
    paid no lost fees. A customer that thought the service had no close substitute would not do that; this one did,
    and the registrant's contracts gave it the right.
  - **The customer has many substitutes, named by the registrant.** *"We operate in a highly competitive and
    fragmented marketplace"*, fifteen principal competitors named (Abt Global, Accenture, AECOM, Booz Allen, CACI,
    CLEAResult, Deloitte, General Dynamics, Guidehouse, Leidos, PA Consulting, SAIC, RTI International, Tetra Tech,
    Westat), *"In addition, we have numerous smaller competitors"*, and *"Some of our competitors are significantly
    larger than we are"*. **The substitution runs both ways on filed record**: Tetra Tech's FY2025 10-K
    (`0000831641-25-000032`) names *"ICF International, Inc."* among its principal competitors and says *"Historically,
    clients have chosen among competing firms by weighing the quality, innovation and timeliness of the firm's service
    versus its cost to determine which firm offers the best value"*.
  - **Price was a named competitive factor, and the word was later dropped.** The FY2016, FY2019, FY2022 and FY2023
    10-Ks list ICF's principal competitive factors or advantages ending *"... scope of service offerings, and
    pricing"*; the FY2024 and FY2025 10-Ks end at *"the scope and scale of our service offerings"*, without
    *"pricing"*. The risk-factor sentence about lowering prices to overcome competition was not dropped. Recorded as a
    wording change, dated to the FY2024 10-K (filed 2025-02-28), without a finding about why.
  - **The commercial third is bought the same way.** The Q2 2026 release lists its notable commercial wins: of eight,
    **six are "recompete" contracts or subcontracts** with utilities for energy-efficiency and electrification
    programmes, and two are new. A utility programme implementer is re-chosen at each recompete.
- **(3) Not subject to price regulation: FAILS IN PART, on the federal half.** The federal customer audits the
  price: *"Government departments and agencies we work for ... review, audit, and investigate our contract
  performance, pricing practices, cost structure"*; *"Payments we received on cost-based contracts with the federal
  government are provisional payments subject to adjustment upon audit"*; and the filing lists the *"U.S. Truthful
  Cost or Pricing Data Act"* among the laws that govern how its contracts are formed. Cost-based work (7% of FY2025
  revenue, 14% in FY2023) is priced as cost plus a fee under that regime. On the commercial side, the utility
  programmes ICF runs exist because state regulators require utilities to fund them (Item 1: demand driven by
  *"changing state and federal regulation"*); the price is set by the utility's procurement, and the programme budget
  by its regulator. That is [E2-59]'s administered price in a form that caps rather than floors.
- **[E3-03]'s demonstration clause runs the wrong way.** The criteria *"will be demonstrated by a company's ability
  to regularly price its product or service aggressively and thereby to earn high rates of return on capital."*
  ICF's operating margin has sat between **5.9% and 8.2% in every one of twelve filed years** (FY2014-FY2025, table
  below), which is what a bidder's margin looks like, and the filing speaks of lowering prices to win, not raising
  them.

**Checklist:** Needed or desired [x] · no close substitute [ ] **fails** · not price-regulated [ ] **fails in part**
*(federal cost and pricing audit; regulator-funded utility programmes)*

### Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]**
**The verdict does not rest on [E4-04].** Under the 2026-09-20 ruling it is a competence limit, applied only to a
name that passes [E3-03]; ICF does not. Recorded for completeness: the contract base is re-won continuously
(*"We continually bid for and execute new contracts"*), which is the defended-not-replaced case the scope paragraph
permits, and no single great manager is named by the filing as the source of results (the CEO, John Wasson, also
chairs the board; 279 vice-presidents average about 18 years' tenure). **No key-person defect is recorded [E4-23].**

### Primary moat metric, filing-sourced, and its trend
Operating margin (the share of each dollar of billings ICF keeps after paying its people, subcontractors and
overhead), FY2014-FY2025, from the filed income statements (FY2016, FY2019, FY2022, FY2025 10-Ks; the XBRL pull in
`peers_xbrl.txt` reproduces each):

| FY | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| revenue $M | 1,050 | 1,132 | 1,185 | 1,229 | 1,338 | 1,479 | 1,507 | 1,553 | 1,780 | 1,963 | 2,020 | 1,873 |
| operating margin % | 6.6 | 6.6 | 7.0 | 6.7 | 6.9 | 6.9 | 5.9 | 7.1 | 6.1 | 6.7 | 8.2 | 7.8 |

**Trend: flat within a two-point band for twelve years, with the two highest years the last two.** Revenue grew
78% over the period, alongside **$1,141M of acquisitions**; how much of the growth was organic the filings read do
not state in one series, and none is claimed here.

### THE COMPETITOR ROW - required **[E3-28]**

**Same metric (operating margin on consolidated GAAP figures), same window (latest fiscal year and the year six
years earlier), SEC XBRL companyfacts, `vintage="newest"`. XBRL transcription, flagged as such: the ICF row was
checked against its filed statement and ties; the peer rows were not opened in their filings, and the verdict does
not rest on them.**

| Company | operating margin, latest FY | operating margin, six years earlier | revenue latest FY $M | revenue change, latest FY | latest FY | named by ICF? |
|---|---|---|---|---|---|---|
| **ICF International (ICFI)** | **7.8%** | 6.9% (FY2019) | 1,872.9 | **-7.3%** | FY2025 | subject |
| Booz Allen (BAH) | 9.2% | 9.0% | 11,217 | -6.4% | FY to 2026-03-31 | yes |
| CACI | 9.6% | 8.0% | 9,568 | +10.9% | FY to 2026-06-30 | yes |
| SAIC | 7.2% | 5.8% | 7,262 | -2.9% | FY to 2026-01-30 | yes |
| Leidos (LDOS) | 12.3% | 8.2% | 17,174 | +3.1% | FY to 2026-01-02 | yes |
| Tetra Tech (TTEK) | 7.5% | 6.1% | 5,443 | +4.7% | FY to 2025-09-28 | yes (and names ICF) |
| AECOM (ACM) | 6.4% | 2.9% | 16,140 | +0.2% | FY to 2025-09-30 | yes |
| Accenture (ACN), consolidated, federal arm not segmented | 14.7% | 14.6% | 69,673 | +7.4% | FY to 2025-08-31 | yes |
| General Dynamics (GD), consolidated | 10.2% | 11.6% | 52,550 | +10.1% | FY2025 | yes |
| Maximus (MMS) | 9.7% | 11.0% | 5,431 | +2.4% | FY to 2025-09-30 | no; added at the brief's request (lists ICF in its proxy peer group) |
| Abt Global · CLEAResult · Deloitte · Guidehouse · PA Consulting · RTI International · Westat | **not obtained** | | | | | yes |

- **Peers: 15 named by the subject; same-metric figures obtained for 8 of them (BAH, CACI, SAIC, LDOS, TTEK, ACM, ACN,
  GD), plus Maximus.** The seven not obtained have no SEC ticker in the tool's map (`sources.ticker_map()` searched by
  name for Guidehouse, Deloitte, Abt, Westat, Research Triangle, PA Consulting and CLEAResult: no hit), so they are
  private or non-SEC; rung 3 (company websites) was not attempted. Accenture and General Dynamics are consolidated
  figures in which the federal consulting arm is not separated, so their rows describe different businesses and
  are shown for completeness only. **For a moat CLAIM this would hold the class PROVISIONAL. It does not here,
  because the verdict below rests on the registrant's own description of how it is bought and on its largest
  customer's filed conduct in 2025; no peer's margin can reverse a filed statement that the work is won by bidding
  and cancellable at will** (the CRUS and QCOM precedent).
- **What the row shows, including the part that cuts for ICF.** (i) ICF sits **in the pack**: 7.8% against 6.4% to
  12.3% for the pure government-services peers, below Booz Allen, CACI, Leidos and Maximus, level with SAIC and Tetra
  Tech. Nobody in the row earns what [E3-03]'s demonstration clause describes. (ii) **The 2025 federal shock hit the
  civilian-agency consultants, not the defence integrators**: ICF -7.3% and Booz Allen -6.4% in revenue, against CACI
  +10.9%, Leidos +3.1%, GD +10.1% (fiscal years differ by up to nine months). **An inference, stated as one:** the
  pattern is consistent with the customer re-allocating spend among its suppliers, which is substitution at the level
  of the whole category; no filing read says so in terms. (iii) **Stated plainly because [E4-26] requires it: ICF held its margin through a 7.3% revenue
  fall** (8.2% to 7.8%), and cut indirect and selling costs by $26.0M to do it. That is good management of a bidder's
  cost base; it is not pricing power. (iv) The row's limit [E3-61]: *"In some businesses, the participants behave
  like a demented Kellogg. In other businesses, they don't. ... I think you'd have to know the people involved"*.
  The row shows where each company stands; it cannot show how a contracting officer will score the next recompete.

### The remaining Q2 tests
- **[E3-33] / [E5-28], untapped pricing power: No.** Claiming it is claiming *"a monopoly or a near monopoly"*; the
  filing describes fifteen named competitors, numerous smaller ones and price reductions to win.
- **[E4-37], the agony metric:** *"it's not a great business when you have to have a prayer session before you raise
  your prices a penny"*. ICF does not raise prices in the ordinary sense: rates are bid into each task order and
  re-bid at recompete. The one positive line: *"We generally have been able to price our contracts in a manner that
  accommodates the rates of inflation experienced in recent years, although we cannot ensure that we will be able to
  do so in the future"* (MD&A). That is keeping pace with costs, not pricing power, and the filing hedges it.
- **[E2-44], the two-characteristic test.** (1) *"an ability to increase prices rather easily ... without fear of
  significant loss of either market share or unit volume"*: **fails**. (2) *"large dollar volume increases ... with
  only minor additional investment of capital"*: **passes on physical capital** (capex $21.7M in FY2025, 1.2% of
  revenue) and **fails on the capital actually spent**: the growth came with $1,141M of acquisitions, and goodwill
  ($1,251.5M) is larger than total equity ($1,049.9M).
- **[E3-46], the second question about the business:** on tangible capital the return is very high (operating income
  before acquired-intangible amortization $182.5M in FY2025, against net tangible operating capital at 2025-12-31 of
  about $45M if the $170.0M of lease liabilities are treated as operating and about $215M if they are treated as
  debt, because the business is people and receivables funded largely by payables and accruals); on the capital
  owners and lenders actually put in, including what was paid for acquisitions, it is about 13% pre-tax before
  acquired-intangible amortization and about 10% after it ($182.5M and $145.5M against equity $1,028.5M plus debt
  $401.4M at 2025-12-31). A people business earns a high return on tangible assets by construction; [E3-03] asks for
  that return to be *"demonstrated by"* aggressive pricing, and here it is demonstrated by having few tangible assets.
- **[E2-45], the attacker's test:** *"how I would like, assuming I had ample capital and skilled personnel, to compete
  with it"*. With skilled personnel, the attack is ordinary: bid the next recompete. The barriers the filing names are
  past performance, relationships and contract-vehicle access, and fifteen named firms already hold them; the customer
  also sets aside work for small businesses, which lets new entrants in by rule.
- **[E2-53], the dominance class:** *"Once dominant, the newspaper itself, not the marketplace, determines just how
  good or how bad the paper will be."* ICF is not in this class; in 2025 the customer, through executive orders,
  determined how good ICF's year would be.
- **[E4-32], direction:** within its markets ICF moved toward commercial energy and technology modernization and away
  from federal health and social programmes; the moat, if any, did not widen in a way the filings show. **Direction:
  a shift of mix, not a widening.**
- **[E4-36] / [E3-51], which cause of success:** the twelve-year record is steady execution plus acquisition, riding
  the funding waves of whoever is buying (disaster recovery after the 2017 hurricanes, with Puerto Rico a top-three
  client in 2019; federal health IT after 2020; utility programmes now). Wave-riding in the corpus's sense, and a
  bidder's wave.
- **[E3-62], the second step:** the gains from ICF's own efficiency (the AI platform it names, the 2025 cost cuts) go
  where the next bid puts them; under competitive re-procurement, the customer captures them at recompete.

### THE VERDICT, AND THE REASONING STATED SO IT CAN BE ATTACKED

**ICF is a well-run professional-services bidder and not a franchise.** [E3-03] asks whether customers think the
service has no close substitute. ICF's customers answer by how they buy and by what they did: they compete each task
order, re-compete each contract at expiry, can set work aside for small firms, audit the price, and can terminate at
convenience without paying lost fees; in 2025 the largest of them cancelled enough work to take $279.5M out of ICF's
revenue in a year, and paid nothing for the lost fees. Fifteen named competitors, and a rival that names ICF back,
stand ready to take the next recompete. The operating margin, flat between 5.9% and 8.2% for twelve years, is the
margin of a firm that wins by bidding. **[E2-53] names what is left: the customer, through its procurement rules and
its budget, not the business, determines how good ICF will be.**

**The strongest evidence against the verdict, stated so the verdict can be judged against it:** relationships that span
decades and 86% prime work; a margin that held (8.2% to 7.8%) while revenue fell 7.3%; a trailing book-to-bill of 1.09
and a $9.3bn pipeline at Q2 2026; a commercial energy business that grew into a third of revenue and keeps winning its
recompetes; very high returns on tangible capital; the MD&A's statement that ICF has priced to cover inflation.
**[E3-47] warns that closing a file wrongly is the costliest error class.** I weighed it. Every item on that list is
compatible with ICF continuing to win bids, and none is evidence that its customers cannot choose someone else; the
recompete wins in the Q2 2026 release are evidence that the customer re-chooses, which is the opposite of no close
substitute. **[E5-42] keeps the two judgments apart**: this is a question about whether the advantage belongs to the
business, and on the filing it belongs to the procurement process, whose rules the customer writes.

**Why OUT and not the perimeter close (UNKNOWABLE at Q2).** The 2026-09-20 ruling reserves UNKNOWABLE for *"A name that
passes [E3-03] and whose durability cannot be judged from filings"*. ICF does not pass [E3-03]: criterion (2) fails on
the registrant's own description of competitive bidding and on the customer's filed conduct in 2025, criterion (3)
fails in part on the federal cost and pricing regime, and the demonstration clause fails on twelve years of margins.
The durability of ICF's relationships is the part I cannot judge, and I do not need to.

- **Untapped pricing power** **[E3-33]**: none.
- Class: [ ] WIDE [ ] NARROW **[x] NONE** [ ] PROVISIONAL · **Direction: mix shifting from federal (55% to 43%) to
  commercial (24% to 33%) and international (5% to 7%), FY2023 to FY2025; margins flat; the customer that cut hardest
  was the largest.**
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

> **Q2 closes the file. Under the hard sequence (operator rule 2), no verdict below this point is reached and no Q5
> clearance exists.** What follows is recorded beneath the close, as the CRUS and CVS runs did, because the brief asked
> for the owner-earnings rebuild and because a later reader deciding whether to reopen Q2 needs it. None of it is a
> verdict and none of it promotes the name.

## Q3 - ARE THEY HONEST, AND ARE THEY RATIONAL?
**VERDICT: NOT REACHED** (Q2 closed the file). *Recorded beneath the close as prompts, without a verdict. IN would
never have promoted the name; nothing here repairs Q2 [E2-37, E2-38, E3-39].*

- **Weight case, had it been declared:** **daily execution** would be ticked. Every task order and recompete is a new
  contest, fixed-price work is half of revenue and *"we realize a profit on fixed-price contracts only if we can
  control our costs"*, and [E3-43]'s *"a business, unlike a franchise, can be killed by poor management"* applies to
  a name that failed [E3-03]: the have-to-be-smart-every-day class [E3-38]. **Leverage** would be a second prompt, not
  a tick: net debt about $400M against equity that is entirely goodwill (tangible equity about -$270M), under a secured
  facility. **So Q3 would have been a binary gate.**
- **Honesty matters found, dated to publication:** none in the documents read. Item 3 (Legal Proceedings) of the FY2025
  10-K and the 8-Ks listed in Step 0 carry no conduct matter; the auditor's FY2025 opinion is unqualified, with one
  critical audit matter (estimates-at-completion on cost-input contracts, $453.8M of FY2025 revenue). **Absence of a
  found matter, not a finding of honesty [E5-17].**
- **What pay vests on [E4-27], from the DEF 14A of 2026-04-22 (`0001140361-26-016102`):** the annual bonus is 80%
  financial, split **Adjusted EPS 50% and "Company Gross Revenue" 30%**, 20% individual; the long-term award is 50%
  performance shares on **"PSA Adjusted EPS"** over two years with a relative-TSR modifier of 75-125%. The 2025
  targets were set lower after the terminations (*"The 2025 financial targets were lower than in 2024 as a result of
  the Administration's changing priorities"*): Adjusted EPS target $6.21, actual $6.03; revenue target $1,920.0M,
  actual $1,872.9M, **threshold $1,536.0M**; the financial portion paid 72.96% against an 80% target. Two prompts:
  **gross revenue is paid for whether it is organic, acquired or pass-through** (subcontractor and other direct costs
  were $454.0M of FY2025 revenue), and the bonus's Adjusted EPS adds back the 2025 severance on the terminated
  contracts ($5.9M) along with the bonus accrual. No element of the pay design read measures return on the capital paid for
  acquisitions.
- **The flags, as prompts:**
  - **[E4-29] EBITDA promotion: FIRES, in the furnished releases and in the lending terms.** The Q2 2026 release's
    headline bullets are *"EBITDA 1 Was $53.0 Million; Adjusted EBITDA 1 Was $53.4 Million, or 11.2% of Total
    Revenues"*, and the CEO states *"our long-standing commitment to increase adjusted EBITDA margins by 10 to 20
    basis points annually"* (EX-99.1 to `0001193125-26-337985`). The April 2026 credit agreement sizes the incremental
    facility at *"100% of Consolidated EBIDTA"* (the filing's own spelling), and the covenant is a net leverage ratio. The 10-K presents EBITDA and
    Adjusted EBITDA reconciliations in the MD&A with the caveat that they *"do not include certain cash requirements
    such as interest payments, tax payments, capital expenditures, and debt service"*. Stated fairly: D&A here is
    mostly amortization of acquired intangibles ($37.0M of $58.1M in FY2025), not a physical renewal cost, so EBITDA
    overstates this business less than it would a capital-heavy one; the flag fires on the practice, as a prompt.
  - **Non-GAAP EPS** excludes amortization of acquired intangibles ($37.0M) and special charges; GAAP is presented
    first and reconciled line by line. The half-owner test [E2-26] passes on form.
  - **[E4-22] projections / [E3-48] the record:** the 2025 guidance was a framework (revenue and EPS *"flat to down 10%"*),
    and revenue came in at -7.3%, inside it. Operating cash was guided *"approximately $150 million"*, revised to
    *"$125 million to $150 million"* in October, and reported at **$141.9M, which includes the $37.2M build of
    restricted utility-programme cash**; excluding it, about $105M. The 2026 guidance (*"$135 million to $150 million,
    excluding the impact of restricted cash"*) moves to the stricter definition. **Recorded without a finding: the
    2025 figure met its guidance on a definition the company itself abandoned for the next year**, and the direction of
    the change is toward the reader. The multi-year promise *"a return to mid- to high-single digit growth in 2027"*
    (Q2 2026 release) is a growth projection of the kind [E4-22] names.
  - **Serial issuance [E5-15]: the reverse.** Basic weighted shares 18,802K (2023) to 18,414K (2025); cover 17,933,884.
    Net stock repurchases $163.4M FY2021-FY2025, $32.7M in H1 2026.
  - **[E4-30] filed-figure tells:** reported growth is not smooth (FY2025 revenue -7.3%; operating margin 5.9-8.2%).
    Cash taxes against pretax income not tested beyond the FY2025 effective rate (18.2%, on a named cause: Section 987
    regulations).
- **Capital allocation, the record:** **$1,141M of acquisitions FY2014-FY2025** against **cumulative owner earnings of
  roughly $0.76-0.97bn over the same twelve years (stripped series below)**, with debt carrying the difference (the
  facility balance was $556.3M at 2022 year end, $401.4M at 2025 year end). Goodwill now exceeds equity. **[E2-56]'s
  camouflage test would be the first read**: the acquired businesses are integrated and not reported separately
  (*"Computation of an earnings measure other than gross profit is impracticable"* for SemanticBits in its first year),
  so their returns cannot be judged from the filing. **The 2020-2022 federal IT purchases (ITG, ESAC, Creative Systems, SemanticBits, about $0.64bn) included two bought
  as providers to U.S. federal health agencies (ESAC, SemanticBits), the client group the 2025 terminations hit
  hardest** (Health and Social Programs -18.9%); what that did to those units' returns is not disclosed. The buyback
  prompt [E5-08] needs an IV range this run did not reach; recorded only that the company bought at an average
  **$80.93** in Q4 2025 and about **$64.8** in Q2 2026, against **$83.00** now, funded *"from our existing cash
  balances and/or borrowings"*.

## Q4 - WILL IT SURVIVE?
**VERDICT: NOT REACHED.** *The owner-earnings rebuild the brief asked for, recorded beneath the close. It is not a
verdict.*

### Owner earnings **[E2-23]**, FY2014-FY2025, from the filed cash-flow statements (four 10-Ks, twelve years)
*CONVENTION (framework section VI): operating cash flow less SBC, less the (c) guess.* **No net-income proxy.**

- **SBC resolves and is complete.** Subtracted: the cash-flow line *"Non-cash equity compensation"* ($17,686K in FY2025),
  which equals the equity-settled awards in the stock-compensation note (RSUs $11,256K + director awards $1,019K +
  performance shares $5,410K = $17,685K). **Cash-settled RSUs** ($4,291K expense in FY2025; *"settled only in cash
  payments"*, $6.4M paid) are liability awards whose cash already leaves through operating cash, so subtracting them
  again would double-count. The **ESPP** is at a discount *"not to exceed 5 %"* and carries no compensation expense. The
  **401(k) match** is a contribution expense ($26.1M in FY2025) that no document read describes as paid in stock, so it
  sits inside operating cash. **No stock-settled plan sits outside the
  subtracted line.** [E5-06]'s subtraction is complete.
- **(c) is carried as a band** [E2-09]: the **capex end** is purchases of property, equipment and capitalized software
  plus *"Payments on capital expenditure obligations"* (a financing line, 2014-2020); the **D&A end** is total D&A,
  which from 2022 is mostly amortization of acquired intangibles ($28.4M of $49.9M in FY2022, $37.0M of $58.1M in
  FY2025). [E3-44]'s default
  treats D&A as the proxy and adds back intangible amortization; I keep the D&A end as the conservative bound for a
  stated reason: this company has maintained its competitive position partly by **buying** capabilities (*"Since 2020,
  we have executed a series of strategic acquisitions to strengthen our leadership in IT modernization"*), so some of
  what it pays for acquisitions is arguably the upkeep of position. Band carried whole, not resolved by preference.
- **The restricted-cash strip [E4-41].** The build of restricted utility-programme cash inside operating cash is client
  money, not owner earnings, and the company's own 2026 guidance excludes it. Estimated as the change in restricted
  cash less the net restricted-contract flows the statements put in financing: **FY2023 $1.8M, FY2024 $12.8M, FY2025
  $37.2M** (FY2025 has no financing or investing line that could carry it, so the whole build came through operating
  cash; an inference from the statements, stated as one). **Stripped from every window below.** H1 2026 carries
  another build of about $53M, not in any annual window.

| FY | OCF | SBC | D&A | capex + obligations | restricted build | OE, capex end | OE, D&A end |
|---|---|---|---|---|---|---|---|
| 2014 | 79.2 | 11.0 | 23.8 | 13.0 | - | 55.2 | 44.3 |
| 2015 | 76.3 | 10.8 | 33.4 | 16.0 | - | 49.5 | 32.1 |
| 2016 | 79.6 | 9.1 | 29.1 | 17.8 | - | 52.6 | 41.4 |
| 2017 | 117.2 | 10.3 | 28.6 | 19.3 | - | 87.6 | 78.3 |
| 2018 | 74.7 | 11.5 | 27.2 | 25.5 | - | 37.6 | 36.0 |
| 2019 | 91.4 | 15.8 | 28.2 | 28.5 | - | 47.1 | 47.4 |
| 2020 | 173.1 | 17.6 | 33.7 | 19.4 | - | 136.2 | 121.8 |
| 2021 | 110.2 | 13.2 | 32.0 | 19.9 | - | 77.0 | 65.0 |
| 2022 | 162.2 | 13.2 | 49.9 | 24.5 | - | 124.6 | 99.1 |
| 2023 | 152.4 | 14.9 | 60.7 | 22.3 | 1.8 | 113.4 | 75.0 |
| 2024 | 171.5 | 16.7 | 53.5 | 21.4 | 12.8 | 120.6 | 88.6 |
| 2025 | 141.9 | 17.7 | 58.1 | 21.7 | 37.2 | **65.4** | **28.9** |

$ millions. Arithmetic in `Test Runs/_research 2026-09-25 ICFI/oe.py` and `oe_out.txt`. (FY2019's capex end sits a
hair below its D&A end because capex plus obligations exceeded D&A that year.)

- **MORE THAN ONE WINDOW [E4-25], restricted build stripped:**

  | window | OE mean, D&A end | OE mean, capex end |
  |---|---|---|
  | 3 years, FY2023-25 | $64M | $100M |
  | **5 years, FY2021-25 (the default [E2-42])** | **$71M** | **$100M** |
  | 7 years, FY2019-25 | $75M | $98M |
  | 10 years, FY2016-25 | $68M | $86M |
  | 12 years, FY2014-25 | $63M | $81M |
  | FY2025 alone | $29M | $65M |

  **Combined range across windows and both (c) ends: $63M to $100M**; FY2025 alone sits below every multi-year mean.
  The screen's band ($74-110M, three years) is the **unstripped** figure with SBC over-subtracted (see tooling);
  unstripped, this run gets $81-117M. **What the range says [E5-11]:** the level is not rising with revenue; FY2020 and FY2024
  are the high years, and FY2025 is the lowest of all twelve on the D&A end.
- **The perimeter caveat:** every window before FY2025 is a smaller company than the one the cap prices, and the
  acquisitions that made it larger cost $1,141M. Owner earnings per dollar of capital put in have not risen: the
  12-year mean is $63-81M on a business that absorbed about $1.1bn of acquisitions to reach a five-year mean of
  $71-100M.
- **Great, good or gruesome [E4-20], a prompt only:** on physical capital, the business needs almost none; on the capital
  actually spent to grow it (acquisitions), the increment is thin: roughly $25-45M of added annual owner earnings
  (FY2014-19 mean $47-55M to FY2021-25 mean $71-100M, by end) for about $0.75bn of acquisitions in FY2020-FY2024
  ($0.70bn net of the 2023 divestiture), about 3-6% a year, before crediting any of the increase to organic growth. **Closer to gruesome on the
  acquired growth, closer to good on the organic base**; [E4-43]'s satisfactory case needs *"the cash they consume"* to
  earn a reasonable return, and the filing does not let me confirm that it did.
- **Staying power [E5-11], a prompt only:** (1) earnings stream moderate and not reliable: FY2025 showed one customer
  decision taking $279.5M of revenue; (2) **liquid assets thin**: unrestricted cash $4.6M at 2026-06-30 (restricted
  $99.3M is client money), dependence on the revolver; (3) **near-term cash requirements**: none large; the facility
  was refinanced in April 2026 to 2031, term-loan amortization and interest (about $29M paid in FY2025) and operating leases
  ($178.8M of minimum payments, $20.4M in the next twelve months). **Leverage, named** [E4-16]: debt $406.2M at
  2026-06-30, secured on substantially all assets, covenant *"maximum Consolidated Net Leverage Ratio ... 4.50 to 1.00"*;
  coverage [E2-54]: FY2025 owner earnings are after interest, and positive at both ends.
- **The named way it dies [E2-27, E3-24], as a signature only:** **#14 THE PATRON** in `Screens/SURVIVAL SHAPES -
  index.md` (*"the government that funds the plant sets the terms and can change them"*) fits the filed mechanism: the
  government that funds 67% of revenue (federal 43%, state and local 17%, international 7%) writes the procurement
  rules, audits the price, terminates at convenience, and in 2025 changed its priorities by executive order. The
  commercial third is regulator-funded utility programmes, the same shape one step removed. **Quantified**: a second
  federal cut the size of 2025's ($279.5M of revenue) at FY2025's observed decremental margin (operating income fell
  $20.4M on $146.9M less revenue, 13.9%, with overhead cut) would take about $39M of operating income; at the 37.2%
  gross margin with no overhead relief, about $104M, against FY2025 operating income of $145.5M. **The company lives;
  the owner's return compresses.** Likelihood: **a real possibility** on exposure, not experience [E4-40]; 2025 was the
  first such year in the twelve read. **Not entered in the index's instances column**, for the reason the PAGP and CALM
  folds gave: the file closed at Q2, so no Q4 death was reached.

---
⛔ **Q5 does not open. Q2 is OUT.**

---
## Q5 - WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?
**VERDICT: NOT REACHED.** No ranking position exists; a name that failed Q2 is not ranked.

### COMPUTATION — NOT A CLEARANCE
*Arithmetic only, no box ticked, no entry language. Produced because the queue records it for every run.*
- **Yield on the $1,488.5M cap:** five-year stripped owner earnings $71-100M = **4.8% to 6.7%**; twelve-year $63-81M
  = 4.2% to 5.4%; FY2025 alone $29-65M = 1.9% to 4.4%. Sovereign **5.47%**. The owner earnings are after interest on
  $406M of debt, so the equity yield already carries the leverage.
- **The company's own 2026 guide, as a cross-check, not a window:** operating cash of $135-150M excluding restricted
  cash, less SBC (about $18M) and capex (about $22M), is about **$95-110M, 6.4% to 7.4%**.
- **At the ~10% floor [E4-28] with no growth:** the five-year range capitalised at 10% is **$0.7-1.0bn against a
  $1.49bn quote**; the 2026 guide on the same construction, $0.95-1.1bn. The quote is above every no-growth
  construction here; closing the gap needs the growth the company projects for 2027, which no filed window shows.
- **Windage count: ONE** (the restricted-cash strip, [E4-41]); the (c) band and the window spread are displayed, not
  spent.

## Q6 - WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
**VERDICT: NOT REACHED** (nothing to sell; no position). **The reversal conditions, in words, for whoever reopens Q2**
(the QLYS ruling: a Q2 failure gets no price alert):
1. **Evidence that customers do not re-compete ICF's work**: a 10-K in which a material share of revenue is under
   sole-source, long-dated contracts or proprietary platforms the customer cannot re-bid (the *"ICF Fathom AI
   platform"* licensed on terms rather than hours would be the place to look), and the competitive-bidding risk factor
   narrows accordingly.
2. **[E3-03]'s demonstration clause turning**: operating margin held above the peer range (above about 12%) for five
   consecutive years on organic revenue growth, without acquisitions carrying it.
3. **The commercial energy business shown to be re-awarded without competition**: utility programme renewals disclosed
   as extensions rather than recompetes, at stable or rising margins, across more than one regulatory cycle.
- **The moat-downgrade question, for the record [E3-30]:** the 2025 federal fall is partly an aberrational shock (a
  one-time policy change) and partly a permanent fact the shock revealed (the customer can do it at will). The first
  may be made up; the second is the Q2 finding and does not bounce back.
- **Next catalyst dates:** the Q3 2026 release on **2026-11-05** (8-K of 2026-09-24), where the company expects
  *"positive quarterly comparisons beginning in this year's third quarter"*; the FY2026 10-K (late February 2027),
  whose Item 1 client mix and Item 1A competitive-bidding language are where conditions 1 and 3 would first appear.

## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Step 0, Q1 IN, Q2 OUT; Q3-Q6 marked NOT REACHED and their
      material recorded beneath the close without verdicts.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the 10-K's own
      description, confirmed clause by clause.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives: none issued. The seven unobtained peers are
      named at Q2 with the reason (no SEC registrant) and the rung not attempted.
- [x] Every UNKNOWABLE verdict states what specifically cannot be known: none issued; the perimeter close was
      considered at Q2 and refused in writing.
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked (FY2025 operating cash $141,870K
      rebuilt from its lines; ties).
- [x] Owner earnings on a multi-year mean; five windows stated; capex band disclosed as a judgment (beneath the close).
- [x] Competitor row filled: 8 of 15 named peers plus Maximus, XBRL transcription flagged; the verdict does not rest
      on the row, and why is stated.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury par curve), dated
      09/24/2026.
- [x] Value stated as a round-number range, not a point estimate (inside a COMPUTATION block only).
- [x] One bar chosen, not both: none; Q5 not reached. Windage count stated (one).
- [x] Prices dated; aggregator used for the live quote only and flagged.
- [x] Run committed to git, with pathspecs, after the claim, after Q1, after Q2 and after this section.
- [x] Ledger ids: the run file cites **60 distinct ids**; every one was read in `principle_ledger.csv` (311 rows by
      `csv.DictReader`) before citing, quotes taken from `quote_verbatim` (pull saved as `ledger_rows.txt`).
      `python tools/check_framework.py`: **PASS** (phantom citations 0 across 1,209 run files).

**The brief's priors, scored:**
- *Consulting / technology-services contractor, roughly half or more from US federal agencies*: **confirmed in kind;
  "half or more" was true FY2022-FY2024 (54-55%) and is no longer: 43% in FY2025, 39.0% in Q2 2026.** Contract types,
  recompete cadence and backlog confirmed from the 10-K.
- *2025 terminations hit USAID and HHS-type programmes*: **HHS confirmed** (HHS 25% to 22% of revenue; Health and
  Social Programs -$144.4M); **USAID not found** as a revenue line in the documents read. Size: federal revenue -$279.5M.
  It does not change the Q2 reading so much as demonstrate it.
- *Acquisitions of about $500M inside the window; SemanticBits and ESAC in 2022, ITG earlier*: **$500M confirmed**
  ($499.5M, FY2021-FY2025); **dates partly refuted** (ESAC and Creative Systems closed in late 2021, SemanticBits July
  2022, ITG January 2020); **the window misses $601M more** (Olson $298.2M in 2014, ITG about $253M in 2020, others).
- *Shape #14 THE PATRON*: **fits the filed mechanism**, recorded as a signature beneath the close, not adopted as a
  verdict because Q4 was not reached.
- *Competitor row from filed documents*: Booz Allen, CACI, SAIC, Leidos, Tetra Tech, Accenture (consolidated),
  Maximus obtained; **Guidehouse not obtainable** (no SEC registrant), with Abt, CLEAResult, Deloitte, PA Consulting,
  RTI and Westat.

**My own errors, caught before commit:**
1. First totalled FY2014-FY2025 acquisitions as $1,138M; the filed lines sum to $1,140.8M. Corrected to $1,141M.
2. First wrote that the owner-earnings numerator and the cap describe the same company "from 2023"; Applied Energy
   Group closed in December 2024, so the same perimeter holds only from FY2025. Corrected.
3. First computed the return on capital put in (EBITA over equity plus debt) as "about 10%"; it is about 13% before
   acquired-intangible amortization and about 10% after. Both now stated.
4. First wrote that the 2025 revenue pattern across peers showed the customer re-allocating spend; no filing says so.
   Now stated as an inference, with the fiscal-year mismatch noted.
5. First wrote that the customer cancelled "a quarter" of its work "in two quarters"; the $279.5M federal fall
   includes the procurement slowdown that followed the terminations. Reworded to say so.
6. My first peer script divided the XBRL values by a million a second time (the helper already returns millions) and
   printed zeros; caught on the first read and rerun.

**Errors in the brief:** (1) *"SemanticBits and Enterprise Science and Computing (ESAC) in 2022"*: ESAC closed
2021-11-01; only SemanticBits (and Blanton) closed in 2022. (2) *"roughly half or more of revenue from US federal
agencies"* is stale by one filing (43% in FY2025). Neither affected a verdict. The brief's "WAVE 7 name 33 of 218" was
counted and is right (line 33 of `_wave7_order.txt`; 32 lines in `_wave7_done.txt` at claim). The ledger was counted:
`csv.DictReader` returns **311** rows.

**Tooling observations (reported, not patched):**
- **`tools/run.py ICFI` over-subtracts SBC**: it subtracts the note's *total* stock-based compensation ($22.0M,
  $25.1M, $22.9M for FY2025-FY2023), which includes cash-settled RSUs ($4.3-8.3M a year) whose cash already left
  through operating cash. A double count, in the conservative direction; about $7M a year here (FY2023-FY2025). Any filer with
  liability-classified awards will carry it.
- **`run.py` cannot see restricted client cash inside operating cash.** Its three-year window (and the screen's
  $74-110M) includes $51.8M of restricted utility-programme cash built up in FY2023-FY2025, about $17M a year, in the
  generous direction. The tool cannot know it; the Q2 2026 release says it in one sentence.
- `peers.py` (mine): `sources.annual()` returns values already in millions for these tags; my first version divided
  again. Not a tool defect; a trap for new scripts, like CRUS's `cik_for()` tuple note.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- One line: **ICFI FAIL at Q2 (OUT, ON THE BUSINESS). Q1 IN. [E3-03] criterion (2) fails on the registrant's own
  words and its largest customer's conduct: work is won by competitive bidding task order by task order, re-competed at
  expiry, subject to small-business set-asides and terminable at convenience without lost fees; in 2025 executive orders
  and DOGE terminations took $279.5M of federal revenue (federal 54% to 43%, HHS 25% to 22%); criterion (3) fails in
  part on federal cost and pricing audit; operating margin 5.9-8.2% for twelve years; [E2-53]: the customer's
  procurement, not the business, sets how good it will be.** Price $83.00 (2026-09-24, aggregator, flagged) x
  17,933,884 shares (10-Q cover, `0001193125-26-338422`) = $1,488.5M; sovereign 5.47% (US Treasury, 09/24/2026).
- **If UNRESEARCHED:** not applicable.
- **If UNKNOWABLE:** not applicable.

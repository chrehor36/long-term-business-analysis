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
their purchase year onward, so the numerator and the cap describe the same company only from 2023; the earlier
years are a smaller company. This is carried to Q4 as a window issue, and at Q3 as a capital-allocation prompt.

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

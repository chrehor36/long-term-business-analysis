## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34 %** · date **2026-09-18** (the newest published print; today 2026-09-21 is a Monday
  and the curve for it had not posted at the time of the strike) · source (issuing authority)
  **US Treasury daily par yield curve, 30-year par yield**, struck fresh this run through
  `tools/sources.py`, which returned `(5.34, '09/18/2026', 'US Treasury daily par yield curve')`.
  **FRED DGS30 was not used; it is the fallback, not the source.** No rate was inherited from
  the dispatch brief, which deliberately supplied none.
- FX: **none needed.** Superior earns in USD. Revenue is sold to US customers in all three
  segments (10-K Item 1: Healthcare Apparel *"sells its products to healthcare laundries,
  dealers, distributors, retailers and consumers primarily in the United States"*; Contact
  Centers *"provides outsourced, nearshore and onshore business process outsourcing, contact and
  call-center support services to North American customers"*). **Note the asymmetry and carry it
  to Q4:** revenue is USD, but **5,800 of 6,520 employees are outside the US** and the cost base
  sits in El Salvador, Belize, the Dominican Republic, Haiti, China, Bangladesh, Vietnam and
  Madagascar. This is a USD-revenue business with a foreign cost base, not a USD business.

**THE PRICE — AGGREGATOR, FLAGGED, LIVE QUOTE ONLY (operator rule 5).**
- **$12.36**, the live quote at **2026-09-21 09:44 ET**, Yahoo Finance chart API via
  `tools/sources.py`. Raw metadata saved to
  `Test Runs/_research 2026-09-21 SGC/price_raw_aggregator.json` (`regularMarketPrice 12.36`,
  `currency USD`, `fullExchangeName NasdaqGM`). The five prior closes read 12.47 / 12.57 / 12.40 /
  12.45 / 12.40, so the quote is not an outlier print. **This is the only number in this file
  that comes from an aggregator.**

**THE SHARE COUNT AND THE CAP — STRUCK BY HAND OFF THE COVER OF THE NEWEST PERIODIC FILING.**
- Cover of the **Form 10-Q for the quarterly period ended June 30, 2026**, filed 2026-08-04,
  **accession 0001437749-26-025511**, verbatim: *"The number of shares of common stock of the
  registrant outstanding as of July 30, 2026 was **15,945,201** shares."*
- **ONE CLASS ONLY**, checked rather than assumed. The FY2025 balance sheet reads *"Preferred
  stock, $.001 par value - authorized 300,000 shares (none issued)"* and *"Common stock, $.001
  par value - authorized 50,000,000 shares, issued and outstanding - 15,730,615 and 16,484,921
  shares, respectively"*. The 10-Q balance sheet reads 15,945,623 issued and outstanding at
  2026-06-30. **The BELFB dual-class cover defect cannot arise here.**
- **Splits after the measurement date: none.** `split_factor_after('SGC','2026-07-30')` returns
  **1.0**. `cap = close(anchor) × shares(measurement) × splits AFTER measurement`
  = 12.36 × 15,945,201 × 1.0 = **$197.1M**, on `close`, never `adjclose`.
- **THE SCREEN'S CAP OF 196 IS RIGHT, and that is the finding.** 196 ÷ 15,945,201 implies
  $12.29 against today's $12.36 — a 0.6% difference, entirely the three-week-stale price. The
  number was reproduced, not adopted. **The cap used everywhere below is the hand-struck $197.1M.**
- **The count is falling, not rising.** 16,484,921 (2023-12-31) → 15,730,615 (2024-12-31) →
  15,945,201 (2026-07-30). Retirement by buyback, partly offset by equity grants. Carried to Q3,
  where **[E5-15]**'s serial-issuance flag is scored.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **Form 10-K for the fiscal year ended December 31, 2025**, filed 2026-03-03,
    **accession 0001437749-26-006653** (`sgc20251231_10k.htm`) — the newest ANNUAL filing, and
    exactly the `newest_filing 2025-12-31` the screen row carries.
  - **Form 10-Q for the quarter ended June 30, 2026**, filed 2026-08-04,
    **accession 0001437749-26-025511** — the newest PERIODIC filing, exactly the screen row's
    `newest_periodic 2026-06-30`. **The screen told me to read it and I read it.**
  - **DEF 14A filed 2026-03-23, accession 0001437749-26-009335** (read at Q3).
  - **8-K of 2026-08-11, accession 0001437749-26-026859**, Items 1.01/1.02/2.03/7.01/9.01 — the
    single Item 1.01 the screen's `deal_note` pointed at. **Opened; see the table below.**
  - **8-K EX-99.1 earnings releases**: Q2 2026, furnished 2026-08-04, accession
    0001437749-26-025507 (`ex_968533.htm`); FY2025/Q4, furnished 2026-03-03, accession
    0001437749-26-006593 (`ex_880700.htm`, `ex_880701.htm`).
- **figures cross-checked against the filed statements — three, by hand, not against XBRL:**
  1. **Shareholders' equity recomputed from A − L** *(the [E5-32] cross-check: Salomon's books
     carried an invented number for twelve audited years, so audited does not mean true)*: total
     assets **$421,844** less total liabilities **$229,026** = **$192,818**, which is the filed
     *"Total shareholders' equity 192,818"* to the dollar.
  2. **FY2025 operating cash flow $19,709 thousand** read off the filed Consolidated Statements
     of Cash Flows, equal to the companyfacts figure used in the series at Q4.
  3. **The segment table reconciles to pretax income**: consolidated gross margin $212,864 less
     consolidated selling and administrative $199,475 = $13,389 of operating profit, less
     interest expense $5,143 = **$8,246**, which is the filed *"Income before income tax
     expense 8,246"*. The same arithmetic on FY2024 gives $20,652 − $6,358 = $14,294, also filed.

**THE SCREEN ROW'S IMPERATIVES — EACH ONE TESTED.** *(The tail-triage correction of 2026-09-12:
every field is a prompt to read, never a score and never a verdict.)*

| screen field | what it said | what the filings say |
|---|---|---|
| `deal_note` | one Item 1.01 since 2026-03-03, *"most likely a credit facility or offering"* | **TESTED; the guess was right and is now a fact with terms.** The 8-K of 2026-08-11 (acc. 0001437749-26-026859) reports an **Amended and Restated Credit Agreement dated 2026-08-07** with PNC: *"a revolving credit facility in the aggregate maximum principal amount of $125 million and a term loan in the aggregate principal amount of $75 million"*, five-year term, SOFR + 1.125%–2.125%, *"secured by substantially all of the operating assets of the Company"*. Item 1.02 terminated the 2022 agreement, under which *"a revolving line of credit … (approximately $29.0 million outstanding balance) plus term loans with an aggregate outstanding balance of approximately $56.25 million"* was repaid. **This is a post-balance-sheet event in no filed statement, and it matters at Q4: the covenants are now named — fixed charge coverage ≥ 1.25:1, net leverage ≤ 4.0:1.** The screen's guess was honestly labelled as one; the *terms* are the news, not the existence. |
| `cap_m 196` | screening cap | **Reproduced at $197.1M** from a hand-struck cover count. Right, for once. |
| `newest_periodic 2026-06-30` | a periodic filing exists beyond the annual date | **Read.** H1 2026 operating cash $17,735k, net income $2,055k, a **$2.6M tradename impairment in Healthcare Apparel**, and the new credit agreement in the subsequent-events note. |
| `acq_note` $32M, 16% of cap | perimeter warning | **Established at Q4.** Acquisition cash inside the 5-year window is $16.4M (2021) + $11.2M (2022) + $4.0M (2024) = **$31.6M**, the screen's $32M, and **16.0% of the $197.1M cap**. Over the full 16-year filed series it is **$172.9M**, which is **88% of today's market capitalisation**. The perimeter problem is far larger than the 5-year window can show — which is the screen flag's own point, made bigger by the rebuild it also ordered. |
| `spread_caveat` — an [E4-25] rebuild ordered | the 4-construction width cannot see past 5 years | **Rebuilt to 16 years at Q4, from the filings.** The rebuild moves the answer materially and is the single most consequential piece of arithmetic in this file. |
| `best_year_note` ONE YEAR CARRIES THE WINDOW | on a 9-year OCF series | **Confirmed and named**: FY2023 operating cash of **$78.9M** against a 16-year median near $17M, and the cause is in the filed cash-flow detail — a **$24.7M inventory release** unwinding the $24.5M (2021) and $15.9M (2022) builds. It is a balance-sheet unwind, not earnings. |
| `level_note` / `level_note_oe` EARLY HALF STRADDLES ZERO | the guard refused to print a ratio | **A refusal, not a finding, and now resolved by reading.** **FY2011 operating cash was −$0.9M** and **FY2022 operating cash was −$2.6M** (owner earnings −$17.9M, the figure the truncated screen string was reaching for). Two negative operating-cash years in sixteen, one of them inside the current window. |
| `wc_note` **empty** | the flag reads ANNUAL facts only (its docstring) | **Checked by hand in the 10-Q, as the docstring requires.** H1 2026 working-capital lines: accounts receivable +$9,115k, contract assets −$8,185k, inventories +$2,386k, prepaid −$568k, other assets −$2,453k, accounts payable and other current liabilities −$4,503k, other long-term +$1,108k — **a net drag of about $3.1M on $17.7M of operating cash.** No half-year prepayment of the INOD kind. The empty flag is correct for this filer this half; it was verified, not inherited. |

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language.** Superior is a **holding company over
  three unrelated sourcing-and-labour spreads**, with almost no owned production:

  1. **Branded Products (64% of FY2025 sales, $361.1M).** A promotional-merchandise and branded-
     uniform **broker**. A corporate customer wants 40,000 branded jackets or a gift-with-purchase
     item; Superior designs it, places the order with a third-party factory in Asia, imports it,
     warehouses it and ships it. The line is `units × (price to customer − landed cost of goods)`
     less the cost of the salespeople who won the programme. Landed cost includes tariff. Gross
     margin **34.3%** in FY2025; selling and administrative **26.6%** of sales; **segment
     operating margin 7.66%** ($27.6M on $361.1M, computed here from the filed segment table).
  2. **Healthcare Apparel (20%, $115.9M).** The same spread against a different buyer: scrubs, lab
     coats and patient gowns under Wink, Fashion Seal Healthcare, CID Resources and a licensed
     Carhartt Medical name, made by third parties or in Superior's own Haitian plants and sold to
     hospital laundries, distributors, retailers and consumers. Gross margin **36.2%**; S&A
     **34.1%** of sales; **segment operating margin 2.08%** ($2.4M on $115.9M).
  3. **Contact Centers (16%, $92.5M).** Not apparel at all. Superior hires bilingual agents in El
     Salvador, Belize and the Dominican Republic and rents their hours to North American
     companies. The line is `seats × utilisation × (bill rate − fully loaded wage)`; cost of goods
     sold here *is* agent payroll (10-K: *"Cost of goods sold for our Contact Centers segment
     includes salaries and payroll related benefits for agents"*). Gross margin **52.9%**; S&A
     **45.8%** of sales; **segment operating margin 7.13%** ($6.6M on $92.5M).

  Above the three sits a corporate centre that consumed **$23.3M** of selling and administrative
  expense in FY2025 (the "Other" column of the filed segment table). **That is the single most
  important fact about how this makes money: the three segments earn $36.6M of operating profit
  between them and the holding company keeps $13.4M of it**, before $5.1M of interest — a
  consolidated operating margin of **2.36%** on $566.2M of sales.

- **The scarce input this business controls.** Asked honestly, **the filings evidence none.** The
  candidates, and what the filing itself does to each:
  - *The factories*: not owned except in Haiti, and the 10-K names the redundancy as the point —
    *"The Company believes that its vast redundant network of suppliers, including its own
    manufacturing facilities in Haiti, provide sufficient capacity to mitigate most dependency
    risks on a single supplier."* A redundant network is by construction not scarce.
  - *The raw materials*: *"The majority of such fabrics are sourced in China"*, and for Branded
    Products, *"The Branded Products segment has flexibility in its suppliers, as other suppliers
    of the same or similar products are widely available."* Superior states its own input is
    commoditised.
  - *The agents*: Central American labour, hired against every other nearshore operator.
  - *The brands*: Wink and Fashion Seal Healthcare are real registered marks and the 10-K calls
    them *"critically important to the marketing and operation of Superior's Healthcare Apparel
    segment"* — but a **$2.6M tradename impairment was taken in that very segment in Q2 2026**,
    which is the filing marking its own brand value down.

  The honest answer is **customer relationships and programme incumbency** — the switching
  friction of a uniform or merchandise programme already running across a customer's estate. That
  is real and it is not nothing. Whether it is *scarce* is Q2's question, not Q1's, and Q1 does not
  borrow it.

- **Will the fundamentals look broadly the same in ten years?** **Yes, and that is not a
  compliment.** Nothing here is a technology. People will still wear scrubs and branded polos in
  2036, corporates will still buy promotional merchandise, and somebody will still answer the
  phone. The business's shape in 2036 will be what it was in 2010 and is now: buy from Asia and
  Central America, sell to America, keep the spread. The two things that can change the arithmetic
  — tariff regimes and where cheap labour is — are exogenous and are already moving (the 10-K
  records the IEEPA tariffs invalidated by the Supreme Court on 2026-02-20, a replacement 10%
  Section 122 tariff from 2026-02-24, and AGOA/HOPE/HELP preferences extended only to **December
  2026**). Those change the *level*, not the *mechanism*, and Q1 asks about the mechanism.

- **Is Q1 answerable consolidated, or only segment by segment?** *(The brief asked; the filings
  answer.)* **Consolidated, and the consolidated answer is the framework's answer.** All three
  segments are the same species of business — buy an input at a price you do not set, sell it at a
  price you do not set, live on the difference, with no owned scarce asset in between. Each one's
  arithmetic fits on one line and the lines add. This is not the ORCL/ARM class where a leg is
  opaque, and it is not the HHH/RGTI class where the filed history is too short: **sixteen years of
  annual data are on file and were rebuilt this session.** The difficulty here is not understanding
  the business; it is that understanding it tells you the advantage may not be there — and that is
  Q2's verdict to reach, not Q1's.

- **VERDICT: [x] IN**
  *Simple and stable in character **[E3-31]**; the unit economics of all three legs are written
  above without management's language; no degree-of-difficulty credit was needed **[E4-18]**; and
  no part of this verdict rests on a document I have not opened.*


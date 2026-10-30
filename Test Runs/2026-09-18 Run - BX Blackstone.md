# Company Run — Blackstone Inc. (BX) — 2026-09-18
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs. **This is a NEW NAME, not a
holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.**

Fill top to bottom. **Stop at the first verdict that is not IN.**

Run unattended from scratch on 2026-09-18 (evening, EDT); the template was copied and committed before any fetch
(`05f082b`). No prior run file for BX exists. WAVE 5, the sixth of the seven "perimeter or restatement above
threshold" names. Research, scripts and downloaded filings are in `Test Runs/_research 2026-09-18 BX/`; the brief is
`_BRIEF.md` there. Sections were written as they closed and committed after each gate. **The BAM run of 2026-09-13
read BX's filings for its competitor row; nothing in that run is evidence about BX, and every BX figure below was read
on BX's own filing.**

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
## STEP 0: THE SKIP REASON, THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

### The entity, in every year used
CIK 0001393818, `submissions.json`: *"Blackstone Inc."*, SIC *"Investment Advice"*, fiscal year end 1231; former names
*"Blackstone Group L.P."* (2007-03-22 to 2019-06-28), *"Blackstone Group Inc"* (2019-07-01 to 2021-08-05), *"Blackstone
Inc"* (from 2021-08-06). The FY2021 10-K: *"Effective August 6, 2021, The Blackstone Group Inc. changed its name to
Blackstone Inc. Blackstone Inc. was initially formed as The Blackstone Group L.P. (the "Partnership") and converted from a
Delaware limited partnership to a Delaware corporation, The Blackstone Group Inc. (the "Conversion"), effective July 1,
2019."* **One reporting entity throughout; no reverse recapitalization and no shell (the DJT check was run).** The
conversion matters for one thing only: FY2019 is part partnership and part corporation for tax, so the provision for
taxes before FY2020 is not comparable. **Every owner-earnings year used below (FY2020-25, H1 2026) is after the
conversion.**

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"perimeter or restatement above threshold: read the filing first"*; the skipped-reason list: *"revenue step
or cross-accession restatement above threshold."* **A prompt to read, never a verdict.** Reproduced by the
brief-writer against `Screens/floor_screen.py` at `a8bc84f` (`floor_screen_a8bc84f.py`) over companyfacts cut to facts
filed by 2026-09-01 (`triage_repro.py`, `triage_repro_out.txt`, re-read by this run):

| guard, in order | value | fires? | what it was reacting to, on the filings |
|---|---|---|---|
| 1. `share_count_shift` | 1.040 | no | ordinary vesting and unit exchanges net of buybacks; no split (`split_factor_after` 1.0); a dei element exists (the RIVN None check) but it is **common stock only** (below) |
| **2. `scale_shift`** | **3.700** | **YES: THE GUARD THAT RETURNED BX UNPRICED** | **NOT A PERIMETER AND NOT A RESTATEMENT: A MARK.** FY2020 $6,101.9M to FY2021 $22,577.1M under `Revenues`, consecutive years (the TSLA check was run: the same element carries every year FY2008-25). The FY2022 10-K statement of operations (`0001193125-23-048733`), $K FY2022 / FY2021 / FY2020: *"Performance Allocations Realized 5,381,640 5,653,452 2,106,000 Unrealized ( 3,435,056 ) 8,675,246 ( 384,393 )"* and *"Principal Investments Realized 850,327 1,003,822 391,628 Unrealized ( 1,563,849 ) 1,456,201 ( 114,607 )"*. **Unrealized marks were $10,131M of FY2021 revenue and minus $4,999M of FY2022**; the swing in those two lines ($15,130M) is larger than the whole FY2021-22 revenue fall ($14,059M). Fees did not step: *"Management and Advisory Fees, Net $ 6,303,315 $ 5,170,707 $ 4,092,549"*. The next step (0.377) is the same marks reversing. |
| 3. `filed_years` | 16 | no | |
| 4. `owner_earnings` | 5y $3,405M D&A end / $3,348M capex end | no (priced) | the triage stopped at guard 2; the figures are OCF less SBC less (c) with the firm's and the consolidated funds' investment purchases and sales inside OCF (below, and Q4) |
| (`restatement_shift`, not a guard in that pipeline) | (1.004, FY2016) | n/a | a null, as at SMCI, SNOW, TSLA, RIVN and DJT |

**So the label was, for BX: GAAP revenue that includes unrealized fair-value marks on carried interest and on the
firm's own investments, which moved +$10.1bn in FY2021 and -$5.0bn in FY2022.** Not a perimeter event, not an organic
step, not a tag hole, and not a restatement: **no 10-K/A or 10-Q/A exists in the 1,726-filing index
(`filings_list.txt`)**, and the FY2025 10-K cover leaves the error-correction box unticked (*"reflect the correction of
an error to previously issued financial statements. ☐"*). **This is the first name in the row whose label measured
neither a business event nor a tooling artefact but an accounting convention: revenue recognised on marks.** The
`scale_shift` guard will fire on any carry-earning manager in a strong mark year.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by
  this run at 20:11 EDT (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned the cached **09/17/2026 5.29%** row one second earlier (`step0_out.txt`), the
  stale-cache defect recorded a fifth time; the issuing-authority figure is used. FRED not used. Not inherited from DJT
  (the figure agrees because it is the same day's print).
- **Earnings currency: USD.** A Delaware corporation in New York reporting in dollars. No FX or ADR conversion applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$124.96, the close of 2026-09-18** (Friday). Source: Yahoo Finance chart via `sources._chart("BX", rng="1mo",
  max_age_h=0)` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`): `regularMarketPrice` 124.96,
  `regularMarketTime` 1789761603 = 16:00:03 EDT, so the figure is the closing print. The day's bar had not finalised
  (open 124.28, high 125.17, low 122.85, close None). `tools/sources.price()` returned the same 124.96 stamped 2026-09-18.
- Recent closes: 09-11 $128.51 · 09-14 $128.29 · 09-15 $126.70 · 09-16 $123.45 · 09-17 $125.41 · 09-18 $124.96. One
  month earlier (08-19) $145.09: **down 14% in a month.**
- **Primary-filing cross-check:** Form 4 `0001193125-26-395751` (Joseph Baratta, filed 2026-09-18) reports sales on
  **2026-09-18** at weighted **$123.35** (*"prices ranging from $122.85 to $123.84, inclusive"*) and **$124.13**
  (*"$123.85 to $124.72"*), inside the Yahoo bar's range. **Corroborated.**
- **Split factor after the count's date (2026-07-31): 1.0.** `close` used, never `adjclose`.

### The share count: from the cover, with the accession, and the units question
- **750,625,114 shares of common stock**, from the cover of the **Q2 2026 Form 10-Q** (quarter ended 2026-06-30, filed
  **2026-08-07**, accession **`0001193125-26-340208`**): *"As of July 31, 2026, there were 750,625,114 shares of common
  stock of the registrant outstanding."* `Screens/cover_shares.py BX` returns the same figure and accession.
- **The cover count is not the economic count.** 10-Q Note 13: *"As of June 30, 2026, the total shares of common stock
  and Blackstone Holdings Partnership Units entitled to participate in dividends and distributions were as follows"*:
  Common Stock Outstanding 752,601,287; Unvested Participating Common Stock 47,333,292; Total Participating Common Stock
  799,934,579; **Participating Blackstone Holdings Partnership Units 443,878,452; total 1,243,813,031.** Holders *"may
  exchange their Blackstone Holdings Partnership Units for shares of Blackstone common stock on a one-for-one"* basis
  (Note 17); Net Income Before Taxes allocated to the unitholders was *"37.2%"* for H1 2026 (MD&A). The Series I and
  Series II preferred are **one share each** (*"the holder of the sole outstanding share of our Series I preferred
  stock"*; the same for Series II), carrying votes and no economics.
- **Which count the yield uses, and why:** owner earnings below are computed for the whole operating firm, before the
  income attributed to *"Non-Controlling Interests in Blackstone Holdings"*, so they belong to common and units
  together. **The yield uses the economic count, 1,243,813,031** (one note, one date, 2026-06-30). Pairing firm-level
  owner earnings with the common count alone would overstate the yield by 66%. The unvested participating common is
  included because it receives dividends; its vesting cost is also inside the SBC subtracted at Q4, so this choice errs
  conservative by at most 3.8%.

### The market cap, on both counts
- **Common alone: $124.96 x 750,625,114 = US$93,798M ($93.8bn)** (public float $108.9bn at 2025-06-30, 10-K cover).
- **Common plus participating units (economic): $124.96 x 1,243,813,031 = US$155,427M ($155.4bn)**, the cap the yield
  uses. (Cover common at 07-31 plus the 06-30 unvested common and units gives 1,241,836,858 and $155.2bn; the same-date
  figure is used.) Split factor 1.0.

### THE DEAL CHECK: none live
`sources.deal_filings("0001393818")` returned no deal forms since the annual report of 2026-02-27 and `deal_note` returned
empty. Read on the index: **no 425, S-4, SC TO, SC 13E-3, DEFM14A or PREM14A has ever been filed by this registrant.**
The two 8-Ks with Item 1.01 in the last year are financing: 2025-10-17 (`0001193125-25-242655`, *"an amended and restated
$4.325 billion revolving credit facility"*) and 2025-11-03 (`0001193125-25-262626`, a supplemental indenture for senior
notes). The SC 13D filings in the index are Blackstone's own filings on other issuers. **The quote is not a spread and
buys this company.**

### The perimeter: consolidated funds, the firm's own balance sheet, and the fee business, stated and not blended
The 10-Q, Item 1A, *"Unaudited Consolidating Statements of Financial Condition"* at 2026-06-30, $M:

| | Consolidated Operating Partnerships | Consolidated Blackstone Funds | eliminations | consolidated |
|---|---:|---:|---:|---:|
| Cash | 2,507.1 | 266.2 (*"Cash Held by Blackstone Funds and Other"*) | | 2,773.3 |
| Investments | 30,308.8 | 5,233.8 | (954.9) | 34,587.7 |
| Total assets | 45,071.1 | 5,843.1 | (1,022.0) | 49,892.2 |
| Loans payable | 13,070.8 | 123.9 | | 13,194.7 |
| Total liabilities | 27,123.8 | 404.8 | (69.5) | 27,459.0 |
| NCI in consolidated entities (incl. redeemable) | 4,022.4 | 4,452.9 | | 8,475.4 |

- **The consolidated funds are small** (12% of assets). The FY2025 MD&A: *"The consolidation of these Blackstone Funds
  has no net effect on Blackstone's Net Income or Equity"*; *"Blackstone's share of Investments of Consolidated
  Blackstone Funds totaled 457.1 million"* of their $5,233.8M (10-Q Note 4).
- **The firm's own balance sheet is not small.** 10-Q Note 4, investments at 2026-06-30, $M: **Accrued Performance
  Allocations 13,906.8** (carried interest accrued on marks and not yet paid; a large part is owed on to employees,
  inside accrued compensation of $6,844.2M); **Partnership Investments 6,535.5** (GP and co-investment stakes, equity
  method); **Other Investments 8,510.2** (proprietary; at 2025-12-31 the MD&A counted *"$7.1 billion in Other
  Investments (which included $6.5 billion of liquid investments)"*); Corporate Treasury Investments 401.5. Against it:
  **loans payable $13,070.8M** at the operating partnerships (*"$12.4 billion in borrowings from our bond issuances"* at
  2025-12-31, and *"In February 2026, we drew $900.0 million under the Revolving Credit Facility"*, FY2025 MD&A).
  **The price therefore buys a fee business, a claim on carried interest, and a leveraged book of investments; Q1 and
  Q4 keep them apart.**

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2025 Form 10-K**, fiscal year ended 2025-12-31, filed **2026-02-27**, accession **`0001193125-26-082531`**
  (`10K_FY2025.txt`; Part III is inside the 10-K: the company files no proxy statement, Q3).
- **Q2 2026 Form 10-Q**, quarter ended 2026-06-30, filed **2026-08-07**, `0001193125-26-340208`; Q1 2026 10-Q
  `0001193125-26-214609`.
- Also read: FY2020-24 10-Ks (`0001193125-21-060361`, `-22-054433`, `-23-048733`, `-24-044485`, `-25-042469`) for the
  FY2018-25 statements; the 8-Ks and Form 4s named in this file.
- **Figures cross-checked against the filed statement** (FY2025 10-K consolidated statements of cash flows and of
  operations, $K, FY2025 / 2024 / 2023): *"Net Cash Provided by Operating Activities 4,663,161 3,481,662 4,056,906"*,
  *"Equity-Based Compensation Expense 1,445,352 1,168,435 987,549"*, *"Purchase of Furniture, Equipment and Leasehold
  Improvements ( 115,703 ) ( 61,409 ) ( 224,231 )"* and *"Total Revenues 14,450,265 13,229,968 8,022,841"* match
  companyfacts to the thousand. **Two lines inside operating cash are not operating in the ordinary sense**:
  *"Investments Purchased ( 3,807,149 ) ( 2,429,824 ) ( 5,010,341 )"* and *"Cash Proceeds from Sale of Investments
  6,679,186 4,342,636 7,189,240"*; they carry the firm's own and the consolidated funds' investment activity, and
  realized carried interest, which the reconciliation first removes (*"Net Realized Gains on Investments ( 4,820,209 )"*),
  can only come back through the second. Q4 takes them apart.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

> *"we try to stick to businesses we believe we understand. That means they must be relatively simple and stable in
> character. If a business is complex or subject to constant change, we're not smart enough to predict future cash
> flows."* **[E3-31]**

### What the filings show, in my own words, without management's language
Pension funds, insurers, sovereign funds and, increasingly, wealthy individuals give Blackstone money to buy buildings,
companies, loans and stakes in other managers on their behalf. **Blackstone charges a yearly fee on that money whatever
the investments do (about 0.83-0.88% of fee-paying capital), takes a share of the profit when an investment is sold at a
gain (carried interest, *"up to 20% of the net realized income and gains"* in the carry funds, FY2025 10-K Item 1), and invests some of its own money beside the clients.** It pays its people out of all
three, and a large part of their pay is a share of the carried interest. Nothing is manufactured; the one physical
outlay is offices and equipment.

Three streams, from the company's segment note and its reconciliation of GAAP income to its own measures (FY2020-22
from the FY2022 10-K `0001193125-23-048733`; FY2023-25 from the FY2025 10-K `0001193125-26-082531`), $M:

| | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|---:|
| GAAP Management and Advisory Fees, Net | 4,092.5 | 5,170.7 | 6,303.3 | 6,671.3 | 7,188.9 | 8,075.6 |
| **1. Fee Related Earnings** (company's measure: fees plus fee-related performance revenues, less fee-related pay and operating costs) | 2,370.1 | 4,050.8 | 4,412.6 | 4,349.3 | 5,282.1 | **5,737.5** |
| 2. Realized Performance Revenues | 1,866.0 | 3,883.1 | 4,461.3 | 2,061.1 | 2,287.0 | 2,815.5 |
| less Realized Performance Compensation | (714.3) | (1,557.6) | (1,814.1) | (896.0) | (951.2) | (1,090.6) |
| 3. Realized Principal Investment Income | 158.9 | 587.8 | 396.3 | 110.9 | 92.5 | 419.7 |
| **Net realizations (2 + 3), share of Total Segment DE** | 36% | 42% | 41% | 23% | 21% | **27%** |
| GAAP Unrealized Performance Allocations | (384.4) | 8,675.2 | (3,435.1) | (1,691.7) | 371.4 | 643.1 |
| GAAP Unrealized Principal Investment income | (114.6) | 1,456.2 | (1,563.8) | (603.2) | 380.6 | 248.3 |

1. **The fee stream.** FY2025 segment Base Management Fees $7,548.9M on Fee-Earning Assets Under Management of $830.7bn
   rising to $921.7bn; the company's own *"Annualized Base Management Fee Rate"* was **0.88% (FY2023), 0.85% (FY2024),
   0.86% (FY2025) and 0.83% (H1 2026)** (10-K and Q2 2026 10-Q AUM tables), by segment in FY2025 Real Estate 0.94%, Private
   Equity 1.07%, Credit & Insurance 0.66%, Multi-Asset Investing 0.66%. **Part of what the company calls fee-related is
   itself a performance fee**: *"Fee Related Performance Revenues"* of $1,825.4M in FY2025, *"the realized portion of
   Performance Revenues from Perpetual Capital that are (a) measured and received on a recurring basis"*, which is 32% of
   FY2025 FRE and moves with the marks of BREIT, BCRED and the other perpetual vehicles.
2. **Carried interest.** Accrued on marks as *"Performance Allocations"* (*"as if the fair value of the underlying
   investments were realized as of such date"*, 10-Q Note 2), realized when the fund sells; about 39% of realized
   performance revenue is paid on to employees (FY2025 $1,090.6M of $2,815.5M). The accrual stood at **$13,906.8M at
   2026-06-30**. This is the stream that made the FY2021 revenue step and the FY2022 reversal (Step 0).
3. **The firm's own investments.** GP and co-investment stakes ($6,535.5M), proprietary *"Other Investments"* ($8,510.2M)
   and consolidated-fund stakes ($457.1M Blackstone share), financed partly by $13.1bn of senior notes (Step 0).

**The scarce input the business controls:** long-dated client commitments and the record that raises the next one.
*"Perpetual Capital Total Assets Under Management were $523.6 billion as of December 31, 2025"*, 41.1% of $1,274.9bn
total AUM (FY2025 10-K MD&A); *"Perpetual Capital"* is AUM *"with an indefinite term, that is not in liquidation, and for
which there is no requirement to return capital to investors through redemption requests in the ordinary course of
business, except where funded by new capital inflows"*. The qualification sits in the same definition and the same 10-K:
in the individual-investor vehicles *"investors may request redemptions or repurchases"*, and when BREIT's requests rose
*"BREIT began to prorate such requests beginning in November 2022"* (FY2022 10-K, filed 2023-02-24), with *"$13.3 billion
from BREIT, reflecting repurchases"* as FY2023 outflows (FY2023 10-K). The lock is real and it is conditional. Whether
that makes it a franchise is Q2.

**Will the fundamentals look broadly the same in ten years?** The mechanism will: a fee on committed capital, a share of
profits on realization, a balance sheet beside the funds. The FY2020 and FY2025 10-Ks carry the same revenue lines and
the same segment measures (FRE, DE) under the same definitions, and there are four segments in both (the FY2020 10-K's *"Hedge Fund Solutions"* stands where the FY2025 10-K's
*"Multi-Asset Investing"* stands; whether that segment's perimeter also changed was not traced). **The mix moves**: Credit & Insurance (0.66%) and individual-investor
perpetual vehicles have grown fastest, and the blended fee rate drifted from 0.88% to 0.83% in two and a half years;
that is a Q2 question about price, not a Q1 question about what the product is.

### THE CASE FOR UNKNOWABLE, AT FULL STRENGTH **[E4-26, E4-51]**
(1) GAAP revenue swung from $6.1bn to $22.6bn to $8.5bn in three years on marks the company sets; a business whose reported revenue can quadruple and fall by two-thirds is not *"relatively
simple and stable in character"* on its face. (2) About a quarter to two-fifths of the company's own distributable
measure comes from realizations whose timing depends on exit markets (42% in FY2021, 21% in FY2024), and a third of FRE
is a performance fee on the perpetual vehicles' marks. (3) The structure is layered: consolidated funds and CLOs, five
Holdings partnerships, a Tax Receivable Agreement paying *"85 % of the amount of cash savings"* to unitholders, two
single-share preferred classes that elect the board. (4) The fastest-growing capital is individual-investor money that
can ask to leave, and did (BREIT, 2022-23).

**Why it does not carry.** HHH and RGTI closed UNKNOWABLE because the declared business was not the filed one; DJT
because the company the share buys was undecided. **Here the declared business and the filed business are the same
business, and every complication above is disclosed and reversed by a line the company itself prints**: the
reconciliation from GAAP net income to Distributable Earnings removes the consolidation (*"Impact of Consolidation (c)
(706,068 )"*, FY2025), the unrealized marks (lines (d), (e), (f)) and the TRA, each as a separate line in every year; the
consolidating balance sheet separates the funds from the firm; the carry accrual has its own roll-forward by segment.
The swings in (1) are the accounting of a mechanism, not a change in the mechanism: fees rose in every year FY2020-25.
**[E4-46]'s five-minute test is passed**: the paragraph at the head of this section states the engine. What cannot be
predicted is the timing of realizations and the level of marks, which is a range to carry at Q4 [E4-25] rather than a
failure to understand the business. Complexity of presentation is carried to Q3 as a candor question **[E2-26, E4-22]**.

- **VERDICT: [x] IN.** The business sells the management of other people's long-dated capital for about 0.83-0.88% a
  year, keeps a share of realized gains of which it passes about two-fifths to its people, and invests beside its
  clients; the filings show each stream separately in every year FY2020-25, with the company's own bridge from the GAAP
  figures that swing on marks to the realized figures that do not. Whether clients could take that money elsewhere at
  the same price is Q2.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that *"(1) is needed or desired; (2) is thought by its customers to have **no
> close substitute** and; (3) is not subject to price regulation."* **[E3-03]**, 1991 letter

### THE HYPOTHESIS TO BE REFUTED, AT FULL STRENGTH **[E4-26, E4-51]**
Blackstone is the one alternative manager with a moat. It calls itself *"the world's largest alternative asset
manager"* (FY2025 10-K MD&A) and the filings support the size: $921.7bn of fee-earning capital against $709.1bn at
Apollo, $604.1bn at KKR and $602.7bn at Brookfield. Size buys three things an entrant cannot: a private-wealth
distribution machine that raised BREIT, BCRED and BXPE from individual investors, a record long enough that the largest
pension funds re-up by default, and a cost base spread over more fees (FY2025 FRE $5,737.5M on $9,841.5M of fee-related
revenue, **58.3%**, computed). $523.6bn of the capital is *"Perpetual Capital"*. Return on the owners' equity is about
41% (below). If any firm in the row can hold its price while others cut, it is this one.

### THE THREE CONDITIONS **[E3-03]**
- **(1) Needed or desired: YES.** FY2025 fee-earning *"Net Inflows"* of $127.1bn (gross inflows $167.0bn before $39.9bn
  of outflows), Fee-Earning AUM $830.7bn to $921.7bn, and $961.6bn at 2026-06-30 (10-K and Q2 2026 10-Q roll-forwards).
- **(3) Not subject to price regulation: YES.** Fees are contracted fund by fund. The 10-K names a regulatory
  *disclosure* pressure, not a price regime: *"we may experience pressure to do so, including in response to regulatory
  focus by the SEC on the quantum and types of fees and expenses charged by private funds"* (Item 1A).
- **(2) No close substitute: NO, AND THE COMPANY SAYS SO.** FY2025 10-K, Item 1, Competition: competition for fundraising
  *"is also driven by the willingness of certain of our competitors to charge lower fees or pay higher or different
  types of distributors fees."* Item 1A: *"We have confronted and expect to continue to confront requests from a variety
  of investors and groups representing investors to decrease fees, which could result in a reduction in the fees and
  Performance Revenues we earn."* **And the customers acted on the substitute:** when BREIT's individual investors wanted
  out, *"BREIT began to prorate such requests beginning in November 2022"* (FY2022 10-K), with *"$13.3 billion from
  BREIT, reflecting repurchases"* in FY2023 outflows; to hold one institutional subscriber in that period, Blackstone
  gave UC Investments an *"11.25 % target annualized net return on its $ 4.5 billion investment in BREIT shares"*,
  *"supported by a pledge by Blackstone of $ 1.1 billion of its holdings in BREIT"* (FY2025 10-K, Note 18, Commitments and Contingencies). **A seller who
  must pledge its own capital to support a customer's return is not selling something with no close substitute.**

**Criterion (2) fails, so the conjunction fails.**

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4; the corpus's own test is pricing conduct plus returns on capital [E3-43])*
**One specification: FY2025 management-fee line as filed ÷ the average of the fee-earning capital measure at 2024-12-31
and 2025-12-31, each from that company's own FY2025 10-K.** The BAM run's nine-peer map (2026-09-13) was the starting
point; **every figure below was re-read by this run on a fresh EDGAR fetch of the filer's own 10-K**
(`peers/getpeers.py`, `peers/verify.py`, whose output prints the caption and the numbers from each filing; arithmetic in
`peers/calc.py`, output `peers/calc_out.txt`). Brookfield is added as the ninth alternative manager (its 10-K, fetched
the same way).

| company | FY2025 fee line (as filed, $M) | fee-earning capital YE2024 → YE2025 ($M, as filed) | **fee rate, bp** | fee-earning capital growth YE24→25 (CAGR 23-25) | FRE growth FY24→25 | 10-K accession |
|---|---:|---|---:|---:|---:|---|
| **BX (subject)** | **8,075.6** "Management and Advisory Fees, Net" *(segment Base Management Fees 7,548.9)* | **830,708.6 → 921,674.5** FEAUM | **92.2** *(86.2 on base fees; the firm's own rate 0.86%)* | **11.0% (9.9%)** | **8.6%** | `0001193125-26-082531` |
| OWL | 2,521.9 "Management fees, net" | 159,794 → 187,735 FPAUM | 145.1 | 17.5% (35.2%, with $47.0bn acquired) | 19.4% | `0001823945-26-000009` |
| TPG | 1,826.4 "Management fees" | 141,286 → 170,102 FAUM | 117.3 | 20.4% (11.5%, $4.5bn acquired in 2025) | 24.6% | `0001880661-26-000011` |
| ARES | 3,680.5 "Management fees" | 292,553 → 384,949 FPAUM | 108.6 | 31.6% (21.1%) | 30.4% | `0001628280-26-011413` |
| BAM | 4,896 "Base management fees" (100% basis incl. Oaktree) | 538,541 → 602,714 Fee-Bearing Capital | 85.8 | 11.9% (14.8%) | n/a (not re-read) | `0001628280-26-013098` |
| CG | 2,396.6 "Fund management fees" | 304,358 → 336,778 Fee-earning AUM | 74.8 | 10.7% (4.7%) | 11.9% | `0001527166-26-000009` |
| KKR | 2,496.8 GAAP "Management Fees" *(segment 4,100.8)* | 511,963 → 604,144 FPAUM | 44.7 *(73.5 on segment)* | 18.0% | 13.7% | `0001404912-26-000007` |
| APO | 2,378 GAAP "Management fees" *(segment 3,391)* | 568,666 → 709,139 Fee-Generating AUM | 37.2 *(53.1 on segment)* | 24.7% (19.9%) | 22.5% | `0001858681-26-000013` |
| TROW | 6,602.3 "Investment advisory fees" | 1,606,600 → 1,775,600 ending AUM *(no FEAUM measure)* | 39.0 | 10.5% | n/a | `0001628280-26-008002` |
| BLK | 19,179 "Total investment advisory, administration fees and securities lending revenue" | 11,551,251 → 14,041,518 total AUM *(no FEAUM measure)* | 15.0 | 21.6% | n/a | `0001193125-26-071966` |

**Comparability, carried rather than smoothed:** KKR's and APO's GAAP fee lines are net of eliminations for their
insurers and consolidated funds, so both bases are shown; BLK and TROW publish no fee-earning measure and are in the
row as the substitute at the traditional end, not as like-for-like rates; OWL, TPG and ARES grew partly by acquisition,
which the roll-forwards show and the growth column notes. FRE margins are defined differently at each firm and were not
re-read on their denominators here, so they are not a row column; BX's own 58.3% is stated above.

**WHERE THE SUBJECT SITS: fourth of eight alternative managers on price** on either BX line (behind OWL, TPG and ARES;
its base-fee rate of 86.2bp sits level with BAM's 85.8bp); **second slowest of the eight on fee-earning capital growth**,
in FY2025 (11.0%, above only Carlyle's 10.7%) and over FY2023-25 where the filings give the base (9.9%, above only
Carlyle's 4.7%); and **the slowest of the seven that report FRE on FY2025 FRE growth (8.6%)**. **The largest by capital, and
not the price leader, not the growth leader, and not the direction leader.** That is what close substitutes look like in
filed data, and establishing it is the row's whole job.

- **Peers named: nine**, every SEC-filing alternative manager of scale plus the two traditional managers that sell the
  substitute at the low end. Buffett says eight **[E3-28]**. **Not taken, named:** EQT AB, Partners Group, CVC and
  Antin file no SEC annual report (their own annual reports would resolve them); Bain Capital, Stonepeak and others are
  private. **This does not make the class PROVISIONAL, and the reason is directional:** every missing name is an
  additional substitute, so a longer row can only strengthen a finding that close substitutes exist. Were this Q2 heading
  for IN, those annual reports would have to be read first and the class held PROVISIONAL until they were.
- **The row's limit, stated [E3-61]:** it shows position, not conduct. The conduct is in BX's own words above: *"the
  willingness of certain of our competitors to charge lower fees"*.

### THE OTHER Q2 TESTS
- **The primary metric, and its direction [E4-32]:** the company's own *"Annualized Base Management Fee Rate"* was
  **0.88% (FY2023), 0.85% (FY2024), 0.86% (FY2025), 0.83% (H1 2026)**; in Real Estate, the segment the firm is best known
  for, **0.97%, 0.93%, 0.94%, 0.91%** (10-K and 10-Q AUM tables). Mix explains part of it (Credit & Insurance at
  0.64-0.66% has grown fastest); mix is also what a price-taker's growth looks like. **Not widening.**
- **Must the moat be continuously rebuilt? [E4-04, E5-23]:** for the drawdown funds, yes by construction. In FY2025
  *"Realizations"* removed **$76.6bn** of Fee-Earning AUM and outflows **$39.9bn**: **$116.5bn, 14.0% of the opening
  $830.7bn, had to be replaced before any growth** (FY2024: $59.2bn and $46.4bn). The spending buys the replacement
  vintage (the Rhodes Ridge case the framework names), not the defence of one advantage. The perpetual 41.1% of AUM is
  the genuine exception, and its individual-investor part showed in 2022-23 that its lock is conditional on proration.
- **Which of the four causes of extreme success [E4-36]:** closest to wave-riding: the institutional and now
  individual-investor reallocation into private markets lifted every name in the row at 10-35% a year of fee-earning
  capital. **[E3-51]**: a surfing run is not a moat; the advantage lives in the wave. The row shows eight surfers on it,
  six of them moving faster than the largest in FY2025.
- **The two-characteristic test [E2-44]:** (a) price rises under flat demand: **NO**; no fee increase is on file, and the
  rate fell through record fundraising. (b) Growth with minor added capital: **PARTLY**; capex of $61-224M a year
  FY2023-25 against $159bn of added fee-earning capital, but growth also consumes the firm's own GP commitments and
  warehousing (Q4).
- **Return on capital [E3-46]:** net income to Blackstone Inc. plus the Holdings unitholders, FY2025 $5,340.6M, on
  average equity of the two ($8,665.5M + $4,610.9M at 2025-12-31; $8,212.3M + $4,326.4M at 2024-12-31) = **41.4%**.
  High, and **not a relative advantage**: a fee manager employs little capital by construction and every name in the
  row prints a high return on it. Recorded, not counted.
- **The dominance class [E2-53]:** NO. The largest by capital does not set the price; OWL charges 145bp and grows
  faster.
- **The attacker's test [E2-45]:** answered by the row. Blue Owl went public in 2021 and took fee-paying capital from
  $102.7bn to $187.7bn in two years at 145bp (with $47.0bn of it acquired); Ares grew 21% a year at 109bp. Capital and
  people have taken share from the largest firm inside two years.
- **[E4-37], the price-rise test:** the 10-K's fee language is defensive throughout (*"pressure"*, *"requests ... to
  decrease fees"*, *"no obligation to modify any of our fees with respect to our existing funds"*). No increase is
  contemplated.
- **Untapped pricing power [E3-33, E5-28]:** would require near-monopoly; nine filers sell the product and three charge
  more. None.
- **Key-person dependence [E4-23], recorded here as the moat check it is:** *"We depend on the efforts, skill,
  reputations and business contacts of our co-founder, Stephen A. Schwarzman, our President, Jonathan D. Gray, and
  other key senior managing directors"*, and *"the governing agreements of many of our funds generally provide investors
  with the ability to terminate the investment period in the event that certain "key persons" in the fund do not meet
  the specified time commitment"* (Item 1A). Fund-level key-person clauses make the fee base contractually dependent on
  named people. **Recorded as a defect of the business, not a compliment to the people.**

### CLASS AND VERDICT
- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL.** A very good business with a high return on its small capital
  and a conditional lock on 41% of its money; not a franchise. *(Not PROVISIONAL: nine filers on one specification from
  their own 10-Ks, and the unpulled foreign managers shown to be directionally unable to reverse the finding.)*
- **Direction: flat to narrowing** (0.88% → 0.83% blended; Real Estate 0.97% → 0.91%; FRE growth the slowest in the row).
- **VERDICT: [x] OUT, ON THE BUSINESS. Permanent.** Criterion (2) of **[E3-03]** fails on the company's own statement that
  competitors charge lower fees and investors ask for cuts, on the customers' own conduct (BREIT's prorated repurchases
  and a $1.1bn pledge to hold one subscriber), and on a nine-filer row in which the largest firm is fourth on price and
  second slowest on growth; the drawdown fee base is replaced by design, 14% of it in FY2025 alone **[E4-04]**; the record
  is a surfing run **[E3-51, E4-36]**; no pricing power is on file **[E2-44, E4-37, E3-33]**; the metric that prices the
  moat is not widening **[E4-32]**; fund key-person terms tie the fee base to named people **[E4-23]**.
  *Not UNRESEARCHED: the row is complete on one specification from primary filings, and the missing foreign managers
  can only add substitutes. Not UNKNOWABLE: the evidence is in and it decides.*
- **A conclusion that required fighting for it is worth less [E4-18].** This one did not: the subject's own Item 1 names
  the cheaper competitor.

**⛔ THE FILE CLOSES HERE. Q3, Q4, Q5 and Q6 below are RECORDED, NOT GOVERNING** (the BAM, DJT and RIVN precedent),
written because the brief asks for the owner-earnings rebuild and the Q3 read, and because they set the reopening
conditions at Q6. **Q5 carries the heading `COMPUTATION — NOT A CLEARANCE` and no entry language appears anywhere
below.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT, on the business). Written because the brief asked for the
> earnings releases and Part III to be read, and because the findings belong in the reopening conditions. Nothing here
> can promote the name or repair Q2 **[E2-37, E2-38, E3-39]**.

### STEP 1 - THE WEIGHT CASE
- [x] **Daily execution [E3-38, E3-43]:** Q2 found a business, not a franchise, and the fee base is re-won vintage by
  vintage on performance (14% of fee-earning capital replaced in FY2025; fund key-person terms). *"a business, unlike a
  franchise, can be killed by poor management."*
- [ ] **Control [E1-16]:** a minority purchase of a listed share; but see governance below: the common holder cannot
  elect a director.
- [x] **Leverage [E3-29], partly:** $13.1bn of operating-partnership borrowings against about $15bn of GP, co-investment
  and proprietary investments plus a $13.9bn carry accrual whose value moves with fund marks. Not bank leverage; enough
  that a mark cycle and a refinancing cycle can meet.

**Case declared: a BINARY GATE** on daily execution, with leverage as a contributing factor. No price compensates.

### THE BINARY - honesty **[E5-16]**, each matter dated to when it became PUBLIC
1. **SEC order, 2015-10-07 (public that day).** Release IA-4219, administrative proceeding 3-16887, against Blackstone
   Management Partners L.L.C., III and IV (`sec_ia-4219.pdf`, not committed; SEC press release 2015-235): the advisers
   *"failed to fully inform investors about benefits that the advisers obtained from accelerated monitoring fees and
   discounts on legal fees"*; *"Blackstone violated its fiduciary duty by failing to properly disclose the fees"* (the
   Enforcement Division's co-chief, in the release). Disgorgement and interest *"$28,911,756"* to the funds and a penalty,
   *"nearly $39 million"* in all, settled *"without admitting or denying the findings"*. **Read against [E5-22] (penalty
   size is not seriousness; the failure that counts is not acting when they learned):** the order itself records that
   *"the Commission considered remedial acts taken by Blackstone prior to contact from Commission staff"*: *"In early
   2011, Blackstone voluntarily ended its disparate legal fee arrangement with the Law Firm. In 2012, Blackstone disclosed
   to all limited partners ... that histor[ical]"* accelerations had occurred. The conduct was a conflict resolved in the
   adviser's favour and then disclosed and ended before the regulator arrived. **On the corpus's test this is a serious
   institutional failure that was acted on, not a finding of personal misconduct**; it is recorded and would bear weight
   at any reopening.
2. **The Kentucky Retirement System litigation, from December 2017 (public in the 10-Ks since).** Derivative, Attorney
   General and class actions over a Blackstone fund of hedge funds; the Attorney General's action survived dismissal in
   May 2024; pending (FY2025 10-K, Note 18). No finding against the company. **The company's own note quotes a report
   commissioned by the plaintiff system that *"did not find any violations of fiduciary duty or illegal activity by
   [BLP]"* and that BLP *"[h]as killed it"***: advocacy inside an audited footnote, carried to candor below.
3. **BREIT's prorated repurchases, from November 2022 (public in BX's FY2022 10-K of 2023-02-24 at the latest;
   BREIT's own notices were not read):** a contractual limit exercised under the vehicle's terms, disclosed; not a conduct matter on the filings.
4. **Legal proceedings, Q2 2026 10-Q:** *"We are not currently subject to any pending legal (including judicial,
   regulatory, administrative or arbitration) proceedings that we expect to have a material impact"*.
- **Recorded (not governing): IN on the binary as filed**, written as the absence of a found disqualifier, not a finding
  that anyone is honest **[E5-17]**. SEC orders after 2015 against Blackstone advisers were not searched on the SEC's
  enforcement pages beyond this one release (a named gap: the SEC administrative-proceedings index would resolve it).

### THE INCENTIVE READ **[E4-27]**
- **What the CEO is paid on:** FY2025 Summary Compensation Table, Mr. Schwarzman: salary $350,000, no bonus, no stock
  award, *"All Other Compensation"* $125,291,824, which is realized carried interest and incentive fees (*"Mr. Schwarzman
  has not received any cash compensation other than the $350,000 annual salary described above and the actual realized
  carried interest distributions or incentive fees"*). Mr. Gray: $96.1M, of which $58.9M carry and $36.8M stock. **Pay
  vests on realized fund profits, not on GAAP marks and not on a stock-price target**: the table reports carry *"paid"*,
  not accrued (the accrued figure for Mr. Schwarzman would have been $74.7M). The incentive is to realize gains for the
  funds, which is the clients' incentive.
- **Where the incentive diverges from the common holder:** Mr. Schwarzman owns **no common stock and 231,924,793
  Blackstone Holdings Partnership Units (52.2% of the units, about 18.6% of the economic count)** (Item 12). The units
  receive distributions before the common holder's corporate tax, and the **Tax Receivable Agreement pays the exchanging
  unitholders *"85 % of the amount of cash savings"*** the corporation realizes from their exchanges ($2,076.2M of future
  TRA payments at 2025-12-31, contractual-obligations table). The 10-K states the timing conflict itself: *"Decisions we
  make in the course of running our business, such as with respect to mergers, asset sales ... may influence the timing
  and amount of payments that are received by an exchanging or selling holder of Blackstone Holdings Partnership Units
  under the tax receivable agreement."* Disclosed, and a standing divergence.
- **Governance:** *"Because the Series II Preferred Stockholder holds more than 50% of the voting power for the election
  of directors, we are a "controlled company""*; the Series II holder is controlled by Mr. Schwarzman (*"will have the
  power to vote upon ... any matters to be voted upon"*); common holders *"are not able to bring matters before our annual
  meeting of stockholders or nominate directors"*; the company files no proxy statement (no DEF 14A in the 1,726-filing
  index; Part III is in the 10-K). **The common holder has no vote on the board. Recorded; it is the [E1-16] shape without
  the ownership.**
- **Succession [E4-23]:** the 10-K names Mr. Gray as President and COO beside the co-founder; the succession is
  disclosed by title, not by date. Recorded at Q2 as key-person dependence.

### STEP 2 - THE FLAGS. *Each is a prompt to READ, never a verdict.*
- [ ] **Weak accounting:** carry accrued on marks is GAAP (HLBV) and fully reconciled; SBC expensed. Not ticked.
- [ ] **Unintelligible footnotes:** long, but each complication has its own reconciling line (Q1). Not ticked.
- [x] **Trumpeted projections / narrative:** the Q2 2026 release (8-K EX-99.1, `0001193125-26-313250`, 2026-07-23)
  opens with the CEO: *"Our decision to lean into the artificial intelligence megatrend is leading to standout investment
  performance across numerous strategies and creating extraordinary opportunities for growth."* No numeric earnings
  target was found in the release or the 10-K. Ticked as a narrative prompt, not a guidance culture.
- [ ] **Serial share issuance [E5-15]:** dei common count up 4.0% over the screen window (`share_count_shift` 1.040), from
  vesting and unit exchanges, with $312-661M a year spent on net settlement and repurchase (FY2023-25). Not ticked.
- [x] **Adjusted-earnings promotion [E4-29]:** the release's first financial measures are *"Fee Related Earnings ("FRE")
  of $1.8 billion ($1.43/share)"* and *"Distributable Earnings ("DE") of $2.0 billion ($1.52/share)"*, **both before
  stock compensation** (the reconciliation adds back *"Equity-Based Compensation (h) 1,443,246"* for FY2025, 20% of DE),
  and *"Net Accrued Performance Revenues of $7.5 billion ($6.00/share)"*, an unrealized mark per share. *"Adjusted
  EBITDA"* appears only inside the reconciliation (five mentions), not as a headline. GAAP net income follows in the
  release's body. **The headline measure deletes the one expense [E5-06] says is simply an expense.** Ticked.
- [ ] **Filed-figure tells [E4-30]:** cash taxes paid $569.4M, $646.9M, $562.6M (FY2023-25) against provisions of
  $513.5M, $1,021.7M, $1,125.0M; the falling ratio is the mark-driven deferred component of pretax income (unrealized
  gains taxed later), not a tell on its face. Not ticked; carried as read.
- **Dividends against issuance [E2-52]:** the policy is to pay *"approximately 85% of Blackstone Inc.'s share of
  Distributable Earnings"* (release), and DE excludes $1.4bn a year of stock pay; owners receive cash at 85% of a measure
  that the employees' new shares partly replace. Not the Peter-and-Paul case (no shares are sold for cash to fund the
  dividend), but the payout is set on a pre-SBC figure. A prompt, recorded.
- **The auditor's-eye test [E4-34]:** the fourth question (period-shifting) is where a carry accrual lives; the
  company's roll-forward of Accrued Performance Allocations by segment (10-Q Note 4) is the disclosure that answers it.

### STEP 3 - THE PRIMARY TEST **[E2-01]**
Net income to Blackstone Inc. plus the Holdings unitholders on their average equity: **FY2025 41.4%** (Q2). FY2021-25
GAAP net income to both: $10,743.9M, $3,024.0M, $2,465.6M, $5,025.3M, $5,340.6M, swinging with marks; the realized
measure (DE) ran $6,170.8M, $6,632.8M, $5,061.0M, $5,966.7M, $7,110.9M. High on either, earned with little capital and
with $13.1bn of debt beside the investment book **[E2-47 carve-out noted: the denominator excludes the accrued carry's
future compensation, which sits in liabilities]**.

### CANDOR - THE HALF-OWNER TEST **[E2-26]**
Passes on disclosure (every mark, every consolidation effect, every TRA payment on its own line; the accrued figure of
executive carry stated beside the paid figure). Two deductions: the release leads with pre-SBC per-share measures, and
the litigation note carries the company's advocacy (*"[h]as killed it"*). Recorded.

### RATIONALITY IS CAPITAL ALLOCATION
- **Buybacks [E5-08]:** *"During the three and six months ended June 30, 2026, Blackstone repurchased 0.2 million and 0.4
  million shares of common stock ... at a total cost of $ 24.0 million and $ 48.4 million"*; $1.6bn authorised and unused.
  Condition (2) cannot be scored without a value range that clears the gates; at the Q5 computation's range the price is
  above it and small buybacks are consistent with that. No flag.
- **The institutional imperative [E2-30]:** (2) *"projects ... materialize to soak up available funds"*: the firm
  launches vehicles continuously (BXPE, BXINFRA and BXCI are named in the FY2025 10-K; the CEO's release names the
  *"artificial intelligence megatrend"*); that is the product line of an asset manager, not surplus-soaking, and is not ticked. (4) *"peer behaviour
  mindlessly imitated"*: the private-wealth and insurance channels are pursued by every name in the Q2 row at once; the
  10-K itself says competition there *"is also driven by the willingness of certain of our competitors to charge lower
  fees"*. Ticked as a prompt.
- **VERDICT (RECORDED, NOT GOVERNING): IN on the binary as filed**, with [E4-29] ticked on the headline measures and the
  governance structure recorded (a controlled company whose common holders elect no director, and a TRA paying the
  founder's class). Not an OUT on the filings read.

### THE GUARDRAIL
- [x] Nothing in this Q3 promotes the name; Q2 is closed on the business **[E2-37, E2-38, E3-39]**.
- [x] Key-person dependence recorded at Q2 as a defect **[E4-23]**.
- [x] No great-manager exception is claimed.

## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The brief asked for the owner-earnings rebuild over every window the statements support,
> with the consolidated funds stripped and the three sources of cash separated; it is done here and it governs nothing.

### Owner earnings — the one number **[E2-23]**
**Which windows exist, and why no longer one is used:** the FY2020-25 statements are all after the 2019 conversion to a
corporation; the FY2016-19 statements exist (FY2020 and earlier 10-Ks) but FY2019 is part-partnership and the provision
for taxes before it is not comparable, so a window reaching back past FY2020 would overstate after-tax owner earnings.
**Windows used: five years FY2021-25 (the default, [E2-42]), three years FY2023-25, six years FY2020-25, and the TTM to
2026-06-30.**

**Two constructions, because operating cash here is not operating cash in the ordinary sense (Step 0).** `oe.py`,
`oe_out.txt`, $M, every input from the filed faces (FY2022 10-K for FY2020-22; FY2025 10-K for FY2023-25; Q2 2026 10-Q
and EX-99.1 for the TTM):

| year | **A: OCF − SBC − capex** (the convention, all cash flows) | A at the D&A end | investment turnover inside OCF (*"Cash Proceeds from Sale of Investments"* less *"Investments Purchased"*) | **B: DE + D&A − SBC − capex** (the company's own bridge) | B at the D&A end (DE − SBC) | of B: fee-only, pre-tax (FRE − SBC + D&A − capex) | of B: net realizations (realized carry less carry pay, plus realized principal income) |
|---|---:|---:|---:|---:|---:|---:|---:|
| FY2020 | 1,386.0 | 1,391.5 | 2,062.5 | 2,826.7 | 2,903.3 | 1,855.2 | 1,310.6 |
| FY2021 | 3,284.2 | 3,221.5 | 4,531.4 | 5,521.3 | 5,533.4 | 3,401.2 | 2,913.3 |
| FY2022 | 5,254.4 | 5,353.6 | 5,139.4 | 5,620.2 | 5,786.4 | 3,400.0 | 3,043.5 |
| FY2023 | 2,845.1 | 2,935.2 | 2,178.9 | 3,943.3 | 4,073.4 | 3,231.7 | 1,276.0 |
| FY2024 | 2,251.8 | 2,178.5 | 1,912.8 | 4,835.7 | 4,798.3 | 4,151.0 | 1,428.3 |
| FY2025 | 3,102.1 | 3,083.8 | 2,872.0 | 5,648.8 | 5,665.5 | 4,275.5 | 2,144.7 |
| **5y FY2021-25 mean** | **3,347.5** | **3,354.5** | | **5,113.8** | **5,171.4** | 3,691.9 | 2,161.2 |
| 3y FY2023-25 mean | 2,733.0 | 2,732.5 | | 4,809.2 | 4,845.7 | 3,886.0 | 1,616.3 |
| 6y FY2020-25 mean | 3,020.6 | 3,027.3 | | 4,732.7 | 4,793.4 | 3,385.8 | 2,019.4 |
| TTM to 2026-06-30 | 3,908.9 | | | | 6,299.0 | | |

- **Construction A reproduces the screen** (5y $3,347.5M capex end / $3,354.5M D&A end against `a8bc84f`'s $3,347.5M /
  $3,405.3M; the D&A-end difference is the screen's earlier D&A vintage). Its OCF carries **investment turnover of $1.9-5.1bn
  a year**: the firm's own GP, co-investment and proprietary purchases and sales, the consolidated funds' trading, and
  realized carry arriving as sale proceeds (the reconciliation first removes it, *"Net Realized Gains on Investments ( 4,820,209
  )"*, FY2025). Without the turnover line, OCF less SBC less capex is about zero over five years ($20.6M a year), because
  carry and principal realizations are the cash.
- **Construction B is [E2-23]'s own form: (a) reported earnings plus (b) non-cash charges, less (c)**, built on the company's
  line-by-line bridge from GAAP pretax income, which removes the consolidated funds (*"Impact of Consolidation (c)"*, FY2025
  $(706.1)M, *"This adjustment reverses the effect of consolidating Blackstone Funds"*), removes every unrealized mark
  (lines (d), (e), (f)), and deducts *"Taxes and Related Payables"* (current tax plus the TRA). **It is not the company's
  measure: SBC is subtracted in full from the cash-flow face ($1,445.4M FY2025, against the bridge's add-back of $1,443.2M
  on a segment basis) [E5-06], and capex is subtracted.** It is not a net-income proxy: no GAAP net income enters it, and
  every line that differs from cash is named.
- **The consolidated funds, stripped and bridged:** at the income level by the company's *"Impact of Consolidation"* line
  (above). At the cash level the funds are financed by their outside holders: *"Contributions from Non-Controlling Interest
  Holders in Consolidated Entities"* less *"Distributions"* were $(72.4)M, $(3.6)M, $(295.3)M, $33.2M and **$1,490.3M** in
  FY2021-25; FY2025's figure matches the MD&A's *"increase in Investments was primarily attributable to purchases made by
  consolidated fund entities"* ($1.3bn). Those lines also carry the non-controlling holders of the operating partnerships
  (NCI of $4,022.4M at the operating partnerships, 10-Q Item 1A), so they bracket rather than measure the funds' effect on
  construction A; **construction B does not need them.**
- **The three sources of cash, and which one owner earnings measures:** (1) **fees**: FRE less SBC, D&A-for-capex,
  pre-tax, **$3.7bn a year over five years**, the recurring core; (2) **realized carried interest less the employees'
  share**: $1.3-3.0bn a year; (3) **income on the firm's own balance sheet**: realized principal income $92-588M a year.
  **Owner earnings measures all three, after tax**, because [E2-23] asks for *"the average annual amount"* the business
  produces and the carry is part of the product sold (the carry funds' *"up to 20% of the net realized income and gains"*),
  not a windfall; realized principal income is included because the cap buys the balance sheet that earns it. **Two
  corpus rules then bind the level: [E4-41] normalizes down for lucky years** (FY2021-22 net realizations of $2.9-3.0bn
  were an exit boom, twice FY2023-24), **and [E4-25] carries the spread rather than resolving it.** The unrealized marks
  are excluded throughout; they are neither cash nor realized.
- **Carried-interest pay, and how owner earnings treats it:** *"Realized Performance Compensation"* ($1,090.6M FY2025)
  is paid in cash when carry is realized and is subtracted in both constructions (in B through DE; in A through
  *"Accrued Compensation and Benefits ( 1,493,875 )"*, the payment of prior accruals). The unrealized accrual
  ($376.9M FY2025) is excluded like the revenue it matches. **Pay is an expense whatever form it takes [E5-06].**
- **SBC, resolved and complete on the face in every year used:** *"Equity-Based Compensation Expense"* 438.3, 637.4, 846.3,
  987.5, 1,168.4, 1,445.4 and H1 2026 915.5 ($M), matching companyfacts; no capitalised SBC is disclosed. SBC was 13-34%
  of OCF and 10-20% of DE, and **rose in dollars every year** FY2020-25 ($438M to $1,445M). Below the 50% line at which **[E3-70]**'s grant table must be
  read by hand; the charge is taken as the floor of the subtraction, as [E3-70] requires, and the grant-date market
  measure was not built (a named gap).
- **Maintenance capex, a DISCLOSED JUDGMENT:** plant is offices and equipment; capex $61-235M against D&A $94-99M
  (segment) or $134M (with intangibles). **The D&A default [E3-44, E2-41] is valid for the plant; the [E5-20] exception
  class does not apply.** The two plant ends differ by under 2%. **The (c) question at this company is not plant**: the
  business *"require[s]"* the firm to commit its own capital to each new fund (*"our minimum general partner commitments
  are generally less than 5% of the limited partner commitments of a fund"*, and liquidity is used for *"funding our
  general partner and co-investment commitments to our funds and warehousing investments for our funds"*, FY2025 MD&A).
  Unfunded commitments were **$6,481.4M** at 2025-12-31 (contractual-obligations table). Construction A charges the net
  of those investments in the year it happens; construction B charges none of them and counts only their realized
  income. **The honest (c) sits between the two constructions**: the part of GP commitment that merely replaces realized
  commitments is maintenance, the rest is growth. The filings do not split it. **That is the width of the range.**
- **Short-window mean (3y FY2023-25): $2,733M (A, capex end) to $4,846M (B, D&A end).** **Long-window mean (5y
  FY2021-25): $3,348M to $5,171M.** Six-year: $3,021M to $4,793M. TTM: $3,909M (A) to $6,299M (B).
- **Combined range, five-year default: about $3.3bn to $5.2bn a year**, a spread of 54% of the low end; **after the
  [E4-41] luck normalization** (FY2021-22 net realizations set to the FY2023-25 average, pre-tax, so the cut is slightly
  overstated), the five-year B end falls to about $4.6bn. **Is the range too wide to conclude?** At Q2's close the question does not govern; at Q5 both ends sit far
  below the bond and the floor, so the width would not change that computation's answer (below).
- **A wide spread is also a Q4 finding [E5-11]:** the distorted years are FY2021-22 (the realization boom and the mark
  swing), and the construction gap is the unsplit GP commitment.

### Great, good, or gruesome? **[E4-20, E4-43]**
- [ ] great · [x] **good** · [ ] gruesome. A high return on little capital (41% on the owners' equity, Q2), but growth
  requires the firm's own capital beside every new fund ($6.5bn unfunded) and the price per unit of capital is drifting
  down; the added capital earns an attractive rate, so *good* rather than *great* [E4-43].

### Staying power — score all three **[E5-11]**
- **(1) Large and reliable stream:** FRE $4.35-5.74bn a year FY2022-25, down only in FY2023 (-1.4%); fee revenue rose in
  every year FY2020-25. **Yes for the fee stream; no for carry** (net realizations fell 58% FY2022 to FY2023).
- **(2) Massive liquid assets:** at 2025-12-31, *"$2.6 billion in Cash and Cash Equivalents, $359.7 million invested in
  Corporate Treasury Investments and $7.1 billion in Other Investments (which included $6.5 billion of liquid
  investments), against $12.4 billion in borrowings"*, and a $4.325bn revolver undrawn at year end (drawn $900M in
  February 2026). **Adequate, not massive**: liquid resources of about $9.5bn against $12.4bn of bonds.
- **(3) No significant near-term cash requirements:** 2026 obligations of $704.8M of borrowings, $498.6M of interest and
  **$6,481.4M of capital commitments to Blackstone funds callable at any time**, $59.4M of TRA. **The commitments are the
  requirement that matters**; they are called as funds invest, which in a downturn is also when realizations stop.
- **Leverage, named and quantified [E4-16, E3-29, E2-54]:** $12.4bn of senior notes (the Q2 2026 balance sheet $13.1bn);
  FY2025 interest paid $463.5M against FRE of $5,737.5M: **12x coverage out of the fee stream alone, after capex**. The
  notes carry *"customary covenants and financial restrictions"* on secured debt and mergers (10-Q), no maintenance test
  was found. Comfortably met [E2-54].

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**
- **The mechanism, stated as its holders would accept it:** Blackstone does not die; its owners' return compresses.
  Eight managers of scale sell the same product into the same reallocation (Q2); growth comes from the cheapest capital
  (Credit & Insurance at 0.64-0.66%, private wealth sold through distributors whom competitors *"pay higher or different
  types of distributors fees"*); the blended rate drifts down (0.88% to 0.83%) while stock pay rises every year in dollars (from 13% to
  20% of DE over FY2020-25), so fee growth reaches the owner at a falling rate. **Shape #11, THE PASS-THROUGH** (the gains passed to the
  customers through price), **with #9, THE WAREHOUSE, as a feature** (*"warehousing investments for our funds"* and $6.5bn
  of commitments on a $12.4bn-bond balance sheet). No new shape is named.
- **The exposure, quantified [E4-40]:** a 2022-23 repeat, from the filed years: net realizations fell from $3,043.5M to
  $1,276.0M and DE by 24% ($6,632.8M to $5,061.0M) while FRE held; a wider run on the individual-investor perpetual
  vehicles would reach FRE itself, because *"Fee Related Performance Revenues"* ($1,825.4M, 32% of FY2025 FRE) are paid on
  those vehicles' returns. A year with realized carry at zero, fee-related performance revenue at zero and base fees
  flat would leave pre-tax fee earnings of roughly $3.9bn ($5,737.5M − $1,825.4M), about 8x interest.
- **Likelihood:** the return compression, **a real possibility** (the filed direction already); insolvency, **a
  low-level possibility**.
- **VERDICT (RECORDED, NOT GOVERNING): would be IN.** A mechanism named and quantified; survival is not in doubt; the
  owner-earnings range is wide for a stated reason (the unsplit GP commitment) and carried, not resolved.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 is OUT. The block below is arithmetic only.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
Cap **$155,427M** (economic count, $124.96 x 1,243,813,031); sovereign **5.34%** (US Treasury 30 Yr, 09/18/2026).

| owner earnings case | $M | yield on the economic cap | vs 5.34% |
|---|---:|---:|---:|
| 5y FY2021-25, A, capex end (all cash flows) | 3,347.5 | 2.15% | -3.19 |
| 5y FY2021-25, B, D&A end (the company's bridge, SBC in full) | 5,171.4 | 3.33% | -2.01 |
| 5y, B, after the [E4-41] normalization | about 4,600 | about 2.96% | about -2.4 |
| 3y FY2023-25, A to B | 2,733.0 to 4,845.7 | 1.76% to 3.12% | -3.58 to -2.22 |
| TTM to 2026-06-30, A to B (the most generous) | 3,908.9 to 6,299.0 | 2.51% to 4.05% | -2.83 to -1.29 |

- **The count matters, and the wrong pairing is shown so no one repeats it:** the five-year B figure on the common-only cap
  ($93,798M) would read **5.51%**, above the bond, because it credits the common holder with the 37.2% of firm earnings that
  belongs to the Holdings unitholders. The yield uses the economic count (Step 0).
- **The floor first [E4-28]:** every case sits below 10% and below the bond. On the bottom boundary a 10% pre-tax return
  needs **about 6.7-7.9 points a year of perpetual growth** from here (engine only, [E3-34]); FRE grew 19.3% a year
  FY2020-25 off a pandemic base and **9.1% a year FY2022-25**; **[E4-35]** (fewer than one in twenty of the best
  businesses sustains 15% for twenty years) and **[E4-44]** bind, and a Q2 OUT on a narrowing price does not carry that
  burden.

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-01]**
At the floor, with no growth, the five-year range capitalizes to **$33-52bn ($27-42 a share on the economic count)**; with
5% perpetual growth granted, **$70-109bn ($56-87 a share)**. **Price $124.96 is above the whole range.** Bar 2, the
screamer test **[E4-01]**: the answer would be *no*. **Windage count: one** (the [E4-41] normalization; the growth case
is shown as a sensitivity, not as a margin).

- **VERDICT: none. Q5 did not open (Q2 OUT).** Had every gate been IN, the computation shows a yield of about 2-4% against a
  5.34% bond and a ~10% floor, at a price roughly 1.4-4.6 times the range.

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

> **RECORDED, NOT GOVERNING.** Nothing is owned and nothing is armed (a Q2 OUT is a finding about the business, and a
> price alert on it would be a category error, the QLYS ruling). These are the conditions on which the file would be
> reopened, written before any reopening **[E1-02]**.

**What would reverse Q2 (the governing gate), in words:**
1. **The price series turns**: the company's own *"Annualized Base Management Fee Rate"* rising for three consecutive
   years, in Real Estate and Private Equity as well as blended, **while the same-specification row shows peers' rates flat
   or falling** [E4-32, E2-44, E4-37].
2. **The customers show there is no substitute**: fee-earning capital growth above the row's median for three years
   without acquisitions, with no proration of any perpetual vehicle and no return support pledged to hold a subscriber.
3. **The foreign managers read**: EQT, Partners Group, CVC and Antin's annual reports pulled and showing that BX's position
   is unique on price, which the directional argument at Q2 says cannot happen.

**What would close it harder:** a fee cut on a flagship fund; a second proration at BREIT or BCRED; the TRA or
controlled-company structure used against the common holder in a transaction; SBC continuing to rise faster than FRE.

**The sell rule [E2-28]** does not apply (nothing held). **Position size:** none.
**VERDICT (RECORDED, NOT GOVERNING): not applicable; the file closed at Q2 and Q6 arms nothing.**

---
## SELF-AUDIT
- [x] Questions answered in order; the gate stopped at Q2 (OUT, on the business); Q3-Q6 recorded beneath explicit
  RECORDED, NOT GOVERNING banners, with Q5 headed COMPUTATION — NOT A CLEARANCE and carrying no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed segment note
  and the company's own GAAP-to-DE bridge, FY2020-25. Q3's and Q4's INs are recorded and not governing.
- [x] No UNRESEARCHED or UNKNOWABLE verdict was returned; the case for UNKNOWABLE at Q1 is recorded at full strength and
  not taken, with the reason.
- [x] Step 0: the skip reason reproduced and explained on the face of the FY2022 10-K statement of operations (unrealized
  performance allocations and principal investment income); the entity checked across the 2019 conversion and the 2021
  rename; the filing read with accession numbers; OCF, SBC, capex and revenue cross-checked to the FY2025 10-K face; the
  FY2020-22 faces read from the FY2022 10-K and matched to companyfacts.
- [x] Owner earnings on the five-year default window and on three-year, six-year and TTM windows, both (c) ends and two
  constructions; the consolidated funds stripped by the company's own line and bracketed at the cash level; the three
  sources of cash separated with the ledger ids that govern their treatment [E2-23, E4-41, E4-25, E5-06]; the windows
  that do not exist (before FY2020) named with the reason.
- [x] Competitor row filled from nine peers' own FY2025 10-Ks, each re-fetched from EDGAR by this run and each figure
  found in the filer's own text (`peers/verify.py`); the foreign managers named and shown to be directionally unable to
  reverse the finding.
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated 09/18/2026, fetched directly; the
  cached 09/17 row from `sources.sovereign()` recorded and not used.
- [x] Value stated as a range under COMPUTATION — NOT A CLEARANCE ($27-42 a share at the floor with no growth, $56-87
  with 5% perpetual growth).
- [x] One bar (the screamer test); windage count one, stated.
- [x] Price dated as the 2026-09-18 close, aggregator flagged, corroborated by a same-day Form 4.
- [x] Share count from the Q2 2026 10-Q cover with its accession, and the economic count (with Holdings units) from the
  same 10-Q's Note 13, the cap shown on both and the yield's choice stated; the wrong pairing shown so it is not repeated.
- [x] Deal check run on EDGAR: none live; the Item 1.01 8-Ks are financing.
- [x] Run committed after Step 0, Q1, Q2 and Q3-Q6, each with a pathspec.
- [x] Every ledger id cited was looked up in `principle_ledger.csv` (`led.py`) before it was written.
- [x] No em dashes in anything this session wrote (the template's headings and the required `COMPUTATION — NOT A
  CLEARANCE` heading carry them).
- [x] Never presented as proven to beat the market; nothing here claims it.
- [x] No image files committed; the downloaded 10-K/10-Q texts, the peers' 10-Ks, the SEC order PDF and press release,
  and `companyfacts.json` were left out of every commit.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **A commit ran after a failed edit.** The Q2 commit `5b58f32` was chained after a Python edit whose assertion failed;
   the commit still ran, carrying the uncorrected research copy `_q2.md` and a run file without Q2. Corrected in
   `9e6d3f2`, which put Q2 into the run file with the row positions restated; history kept. The lesson: chain a commit
   only on the edit's success.
2. **Q1, corrected before the run-file commit:** a draft gave FY2020's net-realizations share of Total Segment DE as 43%;
   the filed figures give 36% ($1,310.6M of $3,680.6M), and the text says 36%.
3. **Q1, removed:** a draft said the marks had *"a Level 3 input set behind most of them"*; this run did not read the
   fair-value hierarchy table, so the clause was deleted.
4. **Q2, corrected in `9e6d3f2`:** a draft said BX was the slowest-growing alternative manager *"except Carlyle"* over
   FY2023-25 while KKR's FY2023 base had not been read, and that five peers grew faster; the text now gives both windows
   separately and six faster in FY2025. A draft note that Ares grew partly by acquisition was not checked on Ares's
   roll-forward and was removed from the table.
5. **Q3-Q4, corrected before commit:** the price-to-range multiple (1.4-4.6x, not 1.2-4.5x), the floor-growth span
   (6.7-7.9 points), *"rising every year"* for SBC (true in dollars, not as a share of OCF or DE), and a vehicle name
   (*"a BREIT-adjacent credit sleeve"*) that no filing read by this run carries.
6. **Tooling friction, not an error:** the first attempt to write Step 0 by bash heredoc failed on an apostrophe, as the
   brief warned; the section was written with the file tool instead.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **"FY2014-15 absent from the tag series" (section 2) is not what the probe output shows.** The current screen's `ocf()`
   in `_probe_screen_output.txt` carries FY2014 $1,655.0M and FY2015 $2,397.0M (listed at the end of the dictionary,
   out of date order, which is probably what was misread), and FY2014-15 SBC and capex are present too. Nothing is
   absent. No window this run used reaches those years (the conversion rule at Q4).
2. **"Read the proxy" (section 4) and "settle on the DEF 14A" (section 3): Blackstone files no proxy statement.** No DEF
   14A exists in the 1,726-filing index; as a controlled company whose common holders cannot nominate directors, it puts
   Part III (compensation, ownership, related parties) inside the 10-K. Read there.
3. **"Strip the consolidated funds out of operating cash using ... the consolidating schedules" (section 4):** the
   company publishes consolidating schedules for the **statement of financial condition only**, not for cash flows. The
   funds can be removed exactly at the income level (the company's *"Impact of Consolidation"* line) and only bracketed
   at the cash level (the NCI contribution and distribution lines also carry the operating partnerships' non-controlling
   holders). The run did both and said which is exact.
4. **The memory-sourced beliefs (section 3), settled:** GAAP revenue includes performance allocations and principal
   investment income, and 2021/2022 made the step and reversal: **held**, and it is the whole skip reason. Consolidated
   Blackstone Funds run through operating cash: **held**, but small (12% of assets; $457.1M Blackstone share), and the
   bigger distortion in OCF is the firm's own investment turnover. Conversion 2019-07-01 and rename 2021: **held**
   (2021-08-06). Economic count larger than common: **held** (1,243,813,031 against 750,625,114; Series I and II one
   share each). FRE margin 58.3% and fee rate 92.2bp (0.86%): **held**, re-read on BX's 10-K. Schwarzman chairman, CEO,
   co-founder with a large holding: **held** (231.9M units, no common stock); Gray president and COO: **held**; *"named
   successor"*: **not settled** on the filings read (the 10-K names him beside the co-founder, not as successor). BREIT
   limited redemptions late 2022 into 2023: **held** (proration from November 2022; $13.3bn of FY2023 outflows). High
   payout of DE: **held** (*"approximately 85%"*).
5. **The brief did not know about the UC Investments return support** (an 11.25% target return on $4.5bn backed by a
   $1.1bn pledge of Blackstone's own BREIT holdings, 2023), which is the sharpest single Q2 fact in the file, or the 2015
   SEC order (IA-4219), which is the one conduct matter on record.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`scale_shift` fires on mark-driven revenue.** A carry-earning manager's `Revenues` element includes unrealized
  performance allocations and principal marks, so the guard will return every such name unpriced in a strong or weak mark
  year. A screen could flag filers whose revenue carries an unrealized component (BX tags no
  `RevenueFromContractWithCustomer...` annual fact at all, `triage_repro_out.txt`); not built.
- **`owner_earnings()` for a fee manager includes investment turnover in OCF**: $1.9-5.1bn a year at BX. The screen's
  figure is construction A; the company's bridge gives B, 54% higher on five years. Only a reader sees which a filer is.
- **`tools/sources.sovereign()` served the cached 09/17 row** at 20:11 EDT while the Treasury had published 09/18: the
  SNOW, TSLA, RIVN and DJT note, reproduced a fifth time.
- **`sources._chart()` returned `close None` for the day's bar** after the close; `regularMarketPrice` with its
  `regularMarketTime` carried the closing print. Recorded so a later run does not read None as no trade.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**For an asset manager, "revenue" includes the marks and "operating cash" includes the balance sheet.** The skip label
here measured an accounting convention, not a business event; and owner earnings for a fee manager sit between two
constructions whose gap is the manager's own capital committed to its funds, which no filing splits into maintenance and
growth. State both, say which is exact, and carry the gap as the range.

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)**, at Q2. [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** BX CLOSES AT Q2 (OUT, ON THE BUSINESS, [E3-03] criterion 2, with [E4-04], [E4-32], [E3-51], [E4-23]):
  the 10-K itself says competitors *"charge lower fees"* and investors ask it *"to decrease fees"*; BREIT prorated
  repurchases from November 2022 and Blackstone pledged $1.1bn of its own BREIT holdings behind an 11.25% target return
  to hold one subscriber; on a nine-filer row re-read from each 10-K, the largest firm is fourth of eight alternative
  managers on price (92.2bp) and second slowest on fee-earning growth (11.0% FY2025; 9.9% a year FY2023-25), its own fee
  rate drifting 0.88% to 0.83%; 14% of fee-earning capital had to be replaced in FY2025 alone. Q1 IN (fees on long-dated
  capital, realized carry less the employees' share, and a balance sheet beside the funds, separable on the company's own
  bridge). Q3 recorded IN on the binary (the 2015 SEC fee-disclosure order, remedied before contact) with [E4-29] ticked
  on pre-SBC headline measures and a controlled-company structure in which common holders elect no director; Q4 recorded
  IN (owner earnings five-year $3.3bn to $5.2bn a year, the gap being the firm's own fund commitments; #11 with #9's
  feature); price $124.96 x 1,243,813,031 economic shares = $155.4bn (common alone $93.8bn), headed COMPUTATION — NOT A
  CLEARANCE: yield 2.2-3.3% against 5.34% and a ~10% floor; Q6 records the reversal condition in words and arms nothing.
- **The skip reason, as it turned out:** unrealized marks in GAAP revenue (+$10.1bn FY2021, -$5.0bn FY2022), not a
  perimeter change and not a restatement.

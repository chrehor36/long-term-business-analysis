
## UPDATE 2026-09-13 - GFS: Q2 OUT, a specialty foundry whose price re-set to the second source when the contracts ran off
`Test Runs/2026-09-13 Run - GFS GlobalFoundries.md`. **Q1 IN, Q2 OUT, file closed; Q3 recorded (IN on the binary, with the weak-accounting,
EBITDA and metric-switching flags, US$500M of buybacks paid to the controlling shareholder, and seven converging prompts); Q4 recorded (OUT on
[E4-20], gruesome; THE PASS-THROUGH likely; THE PATRON proposed); Q5 headed COMPUTATION - NOT A CLEARANCE; Q6 recorded with nothing armed.**
Price **US$46.95** x **558,658,481 shares** (548,751,082 at 2026-06-30 plus 9,907,399 agreed for the Department of Commerce) = cap **US$26.2bn**;
sovereign **USD 30-year 5.35%** (US Treasury, 09/11/2026). **The ninth WAVE 5 name.** @@COUNT@@

### THE SKIP REASON, TESTED - ONE CAUSE ISOLATED: THE TAG NAMES
GFS reports **IFRS in US dollars**. companyfacts carries `ifrs-full` only, **unit USD**, seven annual periods 2019-2025, **FY2025 ingested**. So the
USD-unit filter cannot be the cause and neither can lag: **`tools/run.py GFS` fails on the US-GAAP tag names alone.** This is the cleanest
isolation yet of the second cause in RESUME STATE section 9 (SONY/TM/HMC/TSM: lag; ERIC/SPOT: unit filter plus names; GFS: names only). The
"short history" is real in a different sense: **only five comparable annual periods exist** (2019-2020 sit before the IPO, before the 2021
useful-life change and before the EFK exit), so the five-year default consumes all of them and no independent second window can be built.

### THE BRIEF'S QUESTIONS, ANSWERED FROM THE FILED RECORD
- **Issued vs outstanding (ERIC):** does not fire - issued equals outstanding; repurchases are cancelled.
- **The latest 6-K moved the count:** 9,907,399 shares to the DOC at US$37.85 (agreed 2026-09-03), exactly US$375.0M, the amount of an announced
  DOC quantum grant; the filing does not state the link. Included in the count.
- **Controlling shareholder:** Mubadala 81.0% -> 72.82% in six months (13G/A No. 3); sold to the company at US$40.845 in March and noticed 22M shares
  at US$89.96 in May (Form 144). Consent rights over issuance, M&A above US$300M, debt above US$200M, and the CEO, CFO and CLO; auditor aligned to
  Mubadala's; Nasdaq 5605(e) and 5635 home-country exemptions; Mubadala's CFO, CLO and Deputy Chief Strategy Officer each labelled *"independent ...
  pursuant to applicable Nasdaq rules"*.
- **Perimeter:** EFK to onsemi closed 2022-12-31 (not separately disclosed; inside the five-year window; the three-year window is post-EFK); SMP,
  MIPS, InfiniLink, AMF (2025) and Synopsys ARC (2026-06-01), ~US$1.3bn, individually immaterial; no foundry combination in any filing.
- **Government funding:** asset grants reduce the asset's basis and sit in investing (financing until 2022); US$1,124M received 2019-2025; CHIPS
  Direct Funding Agreement up to US$1.5bn plus US$75M, New York US$570M; the agreement restricts *"dividends and share repurchases"* and change of
  control (terms not quantified in any filing read); AMITC repayment reserve US$50M. **Treated in (c) as a reduction of capex; the 2026 DOC money is
  counted in the share count, not as a grant.**
- **Customer prepayments:** contract liabilities run through **operating** cash (US$1,901M built in 2021, US$1,230M at 2025, US$954M at June 2026), so
  **TSM's strip was followed** (UMC's deposits sit in financing, which is why UMC did not strip). Shown both ways: the five-year owner earnings are
  US$234-248M with the strip and US$453-467M without.
- **Price per wafer through the trough:** flat in 2023 only because customers' shortfall payments were booked inside wafer revenue; -3% in 2024 at
  77% utilisation; **-10.4% in 2025 while utilisation rose to 86%**, explicitly *"where customers are dual sourced"*.

### REFUTED OR NARROWED PRIORS
- **"63% single-sourced is a franchise"**: narrowed to a design-level switching cost. It is the company's own belief, measured in volume, defined
  per product, and re-competed at every design win; the price fell where the other 37% could move, and the five-year ROE averaged 5.6%.
- **"The US location is a moat"**: narrowed to a regime [E2-59]. Customers' filings pay for it (Cirrus Logic's largest customer's American
  Manufacturing Program; Navitas), and the state that funds it changed its terms once already in 2026.
- **"GFS is UMC with a lower margin"** (the brief's anchoring risk, pre-registered): partly refuted. GF's specialty claim is stronger than UMC's and
  its customers' words are more mixed; its return is weaker (5.6% against UMC's 18.8% five-year ROE); it has no trade-secret conviction; and it adds
  a controlling shareholder and a government counterparty UMC does not have.

### NEW FOR THE OPERATOR
- **A proposed fourteenth survival shape, THE PATRON** (after SPOT's pending THE TENANT): the plant that makes the business distinctive is funded by
  a sovereign that sets, changes and can reclaim the terms. Register it, fold it into [E2-59]'s regime reading, or reject it - a naming call.
- **Buybacks from a controlling shareholder inside its own secondary offerings** (US$200M at US$50.75 in 2024, US$300M at US$40.845 in 2026) priced
  to the underwriters' price, not to a published value. Any controlled-company run should read the underwriting agreement's repurchase clause.
- **Performance-share yardsticks dropped mid-cycle** (absolute ROIC and TSR relative to SOX, 2022-2023) for revenue, an adjusted FCF that ignores SBC
  and rises when capex is cut, and absolute TSR set annually. [E2-49] fires here; the prior's running tally is not re-counted in this run.

### TOOLING AND SOURCE DEFECTS FOUND
- **`companyfacts` `DepreciationAndAmortisationExpense` for GFS is not the cash-flow add-back** (US$1,168M against US$1,314M for 2025); every (c) uses
  the filed line. Same class as UMC's depreciation tag.
- **The TSM run's GFS capex % of revenue for 2019 (10.1%) is PP&E only**; with intangibles it is 13.3%. Not a defect in its verdict; recorded so the
  row is not copied.
- **`qtr.py` could not parse the Q1 2022 release table**; its quarter's figures were taken from the Q2 2022 release's comparative columns.
- **EDGAR full-text search through `fts_count()`: 35 calls, no HTTP error**; every hit document opened.

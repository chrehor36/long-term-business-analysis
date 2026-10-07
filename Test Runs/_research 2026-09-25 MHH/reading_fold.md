
## UPDATE 2026-09-25 - MHH: Q2 OUT. A labour broker its clients buy from alongside others, through intermediaries whose job is to cut the rate, and one of its ten largest clients is taking the work home.

**Mastech Digital, Inc. (MHH), wave 7 name 34, register entry 166.** Run file `Test Runs/2026-09-25 Run - MHH Mastech
Digital.md`. Price $7.22 (close 2026-09-24, aggregator, flagged; 1,200 shares traded that day) x 12,012,581 shares (10-Q
cover for 2026-06-30, `0001193125-26-337054`) = cap $86.7M; sovereign 5.47% (US Treasury, 30 Yr, 09/24/2026). **Q1 IN,
Q2 OUT on the business.**

### The finding
- **[E3-03] criterion (2) fails on how the service is bought.** The FY2025 10-K (`0001193125-26-112845`): *"Clients
  typically engage multiple staffing providers, and assignments are awarded based on qualifications, availability, and
  pricing"*; the managed service provider *"retains control of the vendor selection and vendor evaluation process"*,
  and MSP clients with their own offshore centres were about 30% of 2025 staffing revenue, which has *"lower[ed] our
  gross margins"*; preferred-vendor contracts exist so clients can *"obtain better pricing"*; *"These contracts are
  terminable without penalty, as are most of our contracts"*; and *"There are relatively few barriers to entry into
  many of our markets"*. **And on what a client did**: the Q2 2026 release reports consultants on billing down 22.3% *"as
  a top ten client continued insourcing services we provide"*.
- **The demonstration clause fails on twelve years of margins**: operating margin 2.8-8.8% reported FY2014-FY2022 (2.8-6.9%
  once the contingent-consideration credits and impairments are taken out), -4.6%, 1.9% and **0.0%** in 2023-2025.
- **Units, not dollars [E4-55]**: consultants on billing 1,261 (2021) to 840 (2025); the bill rate rose on mix, $75.66 to
  $86.10, and the filing attributes it to *"the type of skill sets that we deployed"* and exiting low-margin positions.
- **Strongest evidence against, weighed at [E3-47] and recorded**: the analytics segment's 43.5-49.1% gross margin and
  rising Q2 2026 bookings; *"consistently low customer attrition"*; $35.6M of cash and no debt; and the fact that the
  2023-2025 collapse is partly the staffing cycle that took Robert Half from 10.2% to 1.4%. None of it shows the client
  cannot choose someone else.

### For the next staffing or IT-services name
**Read Item 1's sentence on how clients award work, and the risk factor on MSPs.** Mastech says both plainly, and the
answer to Q2 sits in them. Then **strip the working capital** before trusting the cash: a staffing firm releases
receivables as it shrinks, and Mastech's 2023 and 2025 operating cash ($16.0M and $11.1M) was mostly that; with the
working-capital lines removed, the last three years earned -$1.0M to +$2.0M a year after SBC and (c). And **read the
bonus table**: the CEO's 2025 bonus paid 123% of goal on non-GAAP EPS of $0.72 when GAAP EPS was $0.05, and was then
settled in shares outside the stock-compensation line.

### Priors, refuted or confirmed
- *IT staffing plus analytics, spun off from iGATE in 2008; analytics bought (InfoTrellis 2017, AmberLeaf 2020)*:
  **confirmed**; the brief omitted Hudson IT (2015, $17.0M) and the $9.7M (2018) and $5.3M (2023) goodwill impairments.
- *Founders hold a large, possibly controlling, stake*: **controlling**, about 58% per the 10-K (Trivedi 27.7%, Wadhwani
  13.1%, the Wadhwani family trust 15.6% in the DEF 14A).
- *Revenue declined after 2022; restructurings, CEO changes, buybacks, deal-shaped 8-Ks*: **confirmed** on the decline,
  a CEO change (December 2024), a CFO change (April 2025), severance in each of 2023-2025, a 2025 buyback and a $5.0M
  authorisation in 2026; **no deal-shaped 8-K**.
- *The screen's cap flag is a tagged-float scale error*: **confirmed** from the cover text: the float was tagged 1,000x
  too large on the FY2021-FY2024 covers (the FY2024 cover says $24,874,000; companyfacts carries 24,874,000,000).
- *The 2021 payables swing*: **arithmetic confirmed (45% of OCF), description refuted**: 2021 working capital was an
  $11.7M use, driven by receivables on 14% growth and the CARES repayment; payables offset part of it.

### Beneath the close, for the next reader
- Q3 prompts: **the Primentor agreement** (8-K 2024-01-19): a consultant paid by the company (fees and 385,000 options)
  and, separately, by the controlling founders in their own shares if they sell more than 80% of their stake; its cost
  is reported three different ways across the FY2024 10-K, the FY2025 10-K and the Q2 2026 10-Q. Other care prompts:
  the float mistagged for four years and the FY2025 cover repeating the 2024 float; two material weaknesses at 2020
  year-end; the auditor changed from UHY to BDO India for FY2026 after the finance function moved to India. **[E4-29]
  reads clean** (no EBITDA in the 10-K or ten releases). The analytics segment, bought for $44.1M of cash, contributed
  -$1.7M, +$3.3M and -$0.2M in 2023-2025 before amortization; staffing contributed $5.4-7.7M.
- Owner earnings FY2014-FY2025 from four 10-Ks, SBC complete plus the $617K stock-settled bonus, (c) from capex to D&A:
  five-year $4.0-6.9M as filed, $3.4-6.3M with working capital stripped; three-year stripped -$1.0M to +$2.0M; FY2025
  stripped below zero. $70-99M at the ~10% floor with no growth on the five-year level including $35.6M of cash, $26-56M
  on the three-year level, against $86.7M. Arithmetic only.

### Tooling, REPORTED NOT PATCHED
- **`tools/run.py` and the screen band count receivables released by a shrinking book as owner earnings**: MHH's
  three-year band ($5-8M) is -$1.0M to +$2.0M once the working-capital lines are removed. Generous direction; any
  shrinking staffing or services filer carries it.
- **`working_capital_flag()` prints "ONE LINE MADE THE CASH" without checking the sign of total working capital**: for
  MHH 2021 the named line (payables) offset part of an $11.7M working-capital use. The flag sent the reader to the right
  year with the wrong sentence.
- **The cap flag in `regen_queue.py` fired correctly and could not say which side was wrong**: a year-on-year check of
  dei:EntityPublicFloat ($81.7M to $47,201M between the FY2020 and FY2021 covers) would have named the float.
- **`run.py` cannot see a bonus accrued as cash and settled in stock** ($617K at MHH, FY2025).
- `sources.cik_for()` returned HTTP 404 for ASGN and CCRN; not investigated.
- No change to `SURVIVAL SHAPES - index.md`: #11 THE PASS-THROUGH fits as a signature with #19 as a feature, but only a
  Q4 verdict enters the instances column.

**No alert, no PORTFOLIO.md row** (failed on the business). Reversal conditions in words at Q6: a 10-K showing a
material share of revenue under multi-year contracts not terminable without penalty, or from licensed IP; five years of
operating margin above about 10% on organic growth, above Kforce and Robert Half through a downturn; consultants on
billing growing while the rate rises and the MSP share falls.

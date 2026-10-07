
## UPDATE 2026-09-25 - TTSH: Q2 OUT. Tile Shop sells tile from 140 leased showrooms at a 64% gross margin and a -1.7% operating margin, and in December 2025 it stopped reporting to its owners.

**Tile Shop Holdings, Inc. (TTSH), wave 7 name 39, register entry 171.** Run file
`Test Runs/2026-09-25 Run - TTSH Tile Shop.md`. CIK 0001552800. Price $2.01 (close 2026-09-24, OTC Markets OTCPK,
aggregator, flagged) x 39,821,741 shares (10-K cover for FY2025, `0001552800-26-000006`) = cap $80.0M; sovereign 5.47% (US
Treasury, 30 Yr, 09/24/2026). **Q1 IN, Q2 OUT on the business.** No earlier note on this name was found in this file.

### The first thing the run found: the company went dark, and the screen could not see it
- A 1-for-3,000 reverse split followed at once by a 3,000-for-1 forward split (2025-12-15) cashed out every holder of
  fewer than 3,000 shares at **$6.60**; the company estimated the cost at $4.8M in October and paid **$32.2M**. Form 25
  followed on 2025-12-17, Form 15 on 2026-01-02 (39 holders of record), and the FY2025 10-K of 2026-02-26 says it is the
  last: *"The Company does not intend, and does not expect that it will be required, to file current or periodic reports
  with the SEC following the filing of this Annual Report on Form 10-K."*
- The stock now trades on OTC Pink Limited: $6.56 on the day of the split, $3.68 on 2025-12-26, $2.01 now, on a few
  thousand shares a day. Directors, officers and affiliates hold about 73% (Fund 1 Investments, about 29%, was promised two
  board nominees under a cooperation agreement).
- **It is the second time.** The board delisted in November 2019; shareholders sued in Delaware, a TRO stopped the Form 15,
  the directors gave standstill commitments, the case settled in 2020, and the stock returned to Nasdaq in June 2021. The
  2025 going-dark proxy does not mention any of it.
- **The screen's `cap_flag` was not an error in either figure**: the $181M float was struck at $6.36 on Nasdaq in June
  2025; the $102M cap at about $2.52 on OTC Pink in September 2026.

### The finding
- **The registrant describes a market with no moat in it**: *"The barriers of entry into the retail tile industry are
  relatively low"*, and *"Many of our competitors enjoy competitive advantages over us"*. Retailing is the corpus's named
  have-to-stay-smart class [E3-74].
- **The returns agree**: operating margin 18.8% in 2012, 10.1% in 2016, 5.7% in 2022, -1.7% in 2025 (2015-2025 mean
  4.5%); return on equity mean 7.0% with a best of 15.0%; the company's own pretax return on capital employed (4.8)% in
  2025. Comparable sales fell three years running on falling traffic.
- **The competitor row**: Floor & Decor, selling the same category into the same housing market, averaged 7.6% and kept
  5.7-5.8% in 2024-2025; Tile Shop was below it every year since 2017. Home Depot 14.1%, Lowe's 10.3%.
- **The strongest counter-evidence**, the 64% gross margin from direct import and own label, is a markup the showroom
  model spends: SG&A was 65.6% of 2025 sales.
- **Beneath the close**: owner earnings over 3, 5, 10 and 14 years at both (c) ends run $4.4M to $17.2M, and 2025 alone was
  negative at both ends; covenants were breached at 2025 year-end and waived; at the ~10% floor the filed record is worth
  roughly $1 to $4 a share against $2.01 (computation only, inside the range). The cash-out spent $32.2M, partly borrowed,
  to save about $2.4M a year and to stop publishing.

### What the reading list should carry forward
**Even a business that passed Q2 could not be monitored here.** The ladder for 2026 financials found nothing (EDGAR ends
at the 10-K; the IR site did not connect; the OTC Markets API refused). Any future look at this name starts with a
document question [E4-19]: has the company published audited statements, re-registered, or relisted?

### Priors refuted or confirmed
- `cap_flag`: refuted as an error; explained as a delisting between two correct figures.
- `wc_note` (payables 297% of 2022 OCF): arithmetic right, inference wrong. Payables were a $8.1M use; the four current
  working-capital lines used $34.7M. Third instance after CAH and DMC.
- `best_year_note`: confirmed; 2020 and 2023 were inventory liquidations carrying 41.8% of nine years of operating cash.
- `level_note_oe` and `flags_disagree`: confirmed and explained (owner earnings negative in 2013 and 2018; OCF never).
- Empty `deal_note`: a blind spot, not an absence.

### Tooling defects (reported, not patched)
- `cap_flag` cannot see a delisting between the float date and the cap date.
- `deal_note()` missed a completed Rule 13e-3 going-private (SC 13E-3, Form 25, Form 15): the third `deal_filings()` blind
  spot after WS and DMC. A row for a company that has filed Form 15 should say so before it prints a yield.
- `working_capital_flag()` fired against a total working-capital use, third time.
- `run.py` priced the intraday print and printed a 15-21% three-year yield with no note that the issuer no longer reports.

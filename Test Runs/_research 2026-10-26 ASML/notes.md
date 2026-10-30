ASML purchase run of record, 2026-10-26. Working notes.

## Contamination log (seen by accident, not used)
- `git status` at start showed a modified path under another company's research folder (`_research 2026-09-27 ARCB`) and untracked `Screens/_daily/` files; nothing about ASML.
- `git log -5` commit subjects named other companies' v5 runs and price alerts (AAPL, CRM, GOOGL, JPM, MSFT, NWE). Nothing about ASML. Not used.

## Framework notes (one read, top to bottom, 2026-10-26; slices of 400/200 lines)
- I. Boxes IN/OUT/TOO HARD (M2006-013). TOO HARD records cause: WORK (knowable, work not done; research pass steps 1-2 written, not run) or NATURE (insiders would not write the forecast down, M2000-105; L1993-023; L1999-018; closed, price does not reopen, M2000-038). A pass that ends unsure ends NATURE (M2002-092).
- Q1 STOP: understanding = reasonable fix on earning power and competitive position in 5-10 yrs (M2012-065, M2000-037). Fixed routing: a business whose ten-year economics cannot be foreseen because its industry changes fast closes at Q1 TOO HARD (M1998-008, L1993-023, M1999-063). Seeing industry != seeing company (M2012-067, L2009-005). Tests 1-12: key variables & predictability (M1998-044); insiders write it down? (M2000-105); customers or technology (M2017-019, M2023-030); how far off (M2011-084); doubt = outside (M2002-092); abroad governance/tax (M2000-141). Technology label on consumer business not ruled out.
- Q2 STOP: castle tests 1-11; commodity & low-cost exception; change paragraph; businesses living on continued invention -> TOO HARD (M1999-075, M2001-069); rapid change L2007-005; moat rebuilt continuously L2007-005; standing castle with ordinary returns -> OUT (CONVENTION 2026-10-06); parts table: part decides at >50% of 5-yr op profit else largest; change for better credited only on full cycle (TOO HARD NATURE with re-look). Row about one company never decides alone.
- Q3 WEIGHING: return on tangible capital needed (M2010-090, M2011-060); maintenance vs growth (L1999-024, M2000-144); growth arithmetic; cap (M1997-095, M1999-067). Debt STOP owned by Q9 (R1997-001).
- Q4: balance sheets 8-10 yrs first (M2025-032). Real costs: depreciation, SBC (L2015-003), restructuring, EBITDA. Tells. STOP: suspicion -> OUT; confusion -> TOO HARD WORK/NATURE. Guidance/targets/adjusted figure: weigh against at Q4 and carry to Q5 (L2002-041, L2019-006, L2016-006, M1994-018, M2004-067). Equity-method income = dividends received.
- Q5: integrity STOP on doubt (M2013-088); ability weighed.
- Q6 WEIGHING: retention test (R1995-009, M1998-110); buybacks only below value (L1999-023, L2011-003); no stated price weighs against unless prices paid <= bottom of Q7 range (CONVENTION). STOP: all-stock deal in undervalued stock (L2009-019). Part B pay, board.
- Q7 STOP. Range CONVENTION: 5-yr avg owner cash after every real cost; growth shown (aggregate, not per share), capped; 10 yrs then zero nominal growth; discount at long govt rate (sovereign of earnings currency); ends = no-growth and shown-growth. All capex deducted (depreciation variant beside). Specifics (a) cycle base if end year aberrational on filer's own description, growth between successive cycle averages, literal window beside; (b) decline as bottom; halves if sign change; (c) acquisitions deducted w/ total growth (default), organic pair beside; serial acquirer >50% -> organic central; merger = paid in shares; (d) working capital increase is capital spending; (e) maintenance case central where filing allows guess; growth spending (capex above maintenance) grows with growth rate for 10 yrs, stops after; maintenance charged every year; (f) cap: if shown growth carried 10 yrs would need owner cash above the highest share of sales earned in filings read, carry business's own sales growth over same window, never above discount rate.
- Floor ~10% (CONVENTION) on owner cash after company tax. Floor tested FIRST: if no case earns floor at price -> OUT whatever width. Else TOO HARD if top/bottom > ~3; OUT if price inside/just below narrower range; IN only if screamer.
- Basis: all-equity central (owner cash before interest, vs mkt cap + net debt; net debt = borrowings + finance leases - cash & securities, operating leases out, said so; latest balance sheet + stated subsequent events). Equity-only beside.
- Fair price: each end case valued at 10% (instead of sovereign), averaged, per share, all-equity less net debt; equity-only beside. No cheap price.
- After a STOP: COMPUTATION, NOT A CLEARANCE heading; AFTER THE STOP facts not weighed; integrity flag in box line if any.
- Research pass only if TOO HARD (WORK); and only run if some case earns floor at price (VII). Brief: write steps 1-2, do not run.
- run.py: arithmetic lines only (v4 material ignored).
- Q8 STOP bond/alternatives; Q9 WEIGHING (little or no debt STOP for whole businesses only); Q10 weighing; Q12 optional.

## Run log
- Tools: run.py ASML refused the USD quote (currency guard); rerun with --quote ASML.AS. cover_shares 385,417,665 (FY2025 20-F cover).
- Filings fetched to cache/ (ignored): 20-F FY2025, FY2022, FY2019, FY2016; 6-Ks 2026-01-28, 2026-07-15 (incl. H1 statutory report), 2026-10-14; peers' 10-K R pages.
- Decision: Q1 TOO HARD (NATURE). Deciding facts: filer's own risk factor on architectures less reliant on lithography; High NA still qualifying for HVM; China 29-36% of sales under licences; company's 2018 range for 2025 (15-24bn) outrun at 32.7bn; 2026 guidance 34-39bn -> 44-45bn within a year.
- COMPUTATION: range EUR 661-808/share (maintenance case, all-equity), fair EUR 272 (equity-only 246); expected return at price 1.6-2.1%.
- check_cites.py FLAGS 0; tools/check_framework.py PASS.

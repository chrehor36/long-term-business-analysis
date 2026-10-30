# AQN run notes (2026-10-27)
Working notes for the purchase run of Algonquin Power & Utilities Corp. under THE FRAMEWORK v5.

## Framework v5 read (full, 2026-10-27, in slices of <=200 lines)
- Boxes: IN/OUT/TOO HARD; TOO HARD cause WORK (knowable, work not done) or NATURE (insiders would not write it down).
- Q1 STOP: ten-year economics foreseeable [M2012-065],[M2000-037]; key variables [M1998-044]; abroad: governance and tax [M2000-141].
- Q2 STOP: castle tests 1-11; parts table (deciding part > half 5y op profit, else largest); field's returns over last full cycle;
  "standing castle that protects only ordinary returns" = OUT, BUT "A return set by a regulator is the exception, carried to Q3 as a
  second best [M2009-104],[L2009-012]". Regulated moat that broke: [L2023-011]; open tension L2023-011/M2024-011 vs earlier rows.
- Q3 WEIGHING: return on capital needed; capital-heavy second best [M2018-055],[L2009-012],[M2009-104],[L2011-019],[M2012-057].
- Q4: balance sheets 8-10y first [M2025-032]; real costs; EBITDA tells [M1998-086]; adjusted figure featured [L2016-006] weighs and goes to Q5.
- Q5 STOP on integrity [M2013-088].
- Q6 WEIGHING; retention test [R1995-009],[M1998-110]; buyback vs bottom of Q7; issuance [R1995-010],[L2014-015]; all-stock STOP [L2009-019].
- Q7 STOP: range = 5y avg owner cash, shown growth capped, 10y then zero nominal growth, at sovereign; ends no-growth and shown-growth;
  floor ~10% tested first (OUT if no case earns it at price); TOO HARD if top > ~3x bottom (only where some case clears floor);
  OUT if price inside/just below; IN only if screamer. Specifics (a)-(f). Regulated utility: equity-only central; LTD increase per year
  credited against growth spending only, capped at allowed debt share of deciding part (rate-base weighted; if allowed share stated for
  < half rate base, own LTD share of LT capital); securitization bonds out; all-equity beside. Floor earned on equity.
  Fair price: each end case discounted at 10%, averaged, per share.
- Q8 STOP: bond, more of what owned. Q9 weighing: debt cover in bad years [L2010-012],[L2005-019]. Q10 weighing. Q12 optional.
- Part VII: research pass only where some case earns floor at price; AFTER THE STOP facts section; tools/run.py arithmetic only.

## Resume 2026-10-28
- Framework v5 re-read in full (slices <= 320 lines): I, II, III, Q1-Q10, Q7 (floor, whose tax, all-equity basis, regulated utility,
  range convention, floor first, six specifics, (e) growth spending), Part VI conventions, Part VII.
- tools/run.py fails on AQN (40-F cash-flow tags stop in 2017): all figures from the filed statements.
- Helper scripts: fetch.py (EDGAR fetch with UA), strip.py (html to text), xbrl_table.py, idq.py (ledger lookup),
  comp.py (competitor 10-K facts), q7.py (Q7 cases; output q7_out.txt), check_run.py (citation check).
- Key facts: Reg Services decides (2025 op income 508.6 of 504.7 total); filer splits capex Sustaining/Growth (MD&A);
  NH DOE motions to dismiss rate cases over data reliability; MO OPC/Staff motions to dismiss Empire case (billing);
  Lexington gas explosion 2025-04-09; shares 274.1M (2016) -> 769.7M (2026-06).

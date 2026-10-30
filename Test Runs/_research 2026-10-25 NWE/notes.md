# NWE run notes, 2026-10-25

Working notes for the NorthWestern Energy Group (NWE) purchase run. Started 2026-10-25.

## Contamination log
- Directory listing of the repository root showed the file name PORTFOLIO.md; of Screens/ showed the file names "RESUME STATE 2026-09-02 ..." , "RESUME STATE 2026-09-12 ..." and "2026-08-31 PREPPED READING LIST (operator lists).md". File names only; none opened; nothing used.
- git status output showed a modified file under MBA - UNG/ (not touched).

## Framework notes (read once)
Read in four large reads (lines 1-500, 500-920, 920-1320, 1320-1620, 1620-1916); not to be re-read.
- Boxes: IN / OUT / TOO HARD (WORK or NATURE, cause always stated). Q1, Q2, Q7, Q8 STOP; Q4 STOP on confusion (TOO HARD) or suspicion (OUT); Q5 STOP on integrity; Q3, Q6, Q9 weighings each with one narrow STOP (Q3's debt criterion applied at Q9; Q6 all-stock deal in undervalued stock; Q9 "little or no debt" for whole businesses only).
- Q1 tests 1-12; routing: fast change closes Q1 TOO HARD; holding company by parts (a part matters at >half of five-year operating profit, else the largest).
- Q2: 11 castle tests; commodity business and the low-cost exception; a return set by a regulator is the exception to the "ordinary returns" OUT, carried to Q3 as second best [M2009-104], [L2009-012]; regulated moat that broke [L2023-011]; business of parts convention; the competitor row from rivals' own filings over the whole span.
- Q3: capital-heavy as second best [M2018-055], [L2009-012], [M2009-104]; utilities "To earn more, their owners must invest more" [L2011-019]; return on added capital "measured by the operating earnings after depreciation" [M2014-086].
- Q4: balance sheets 8-10 years first [M2025-032]; real costs; tells; deferred taxes in a utility not hidden equity [M2015-030]; pensions [M2003-110].
- Q5: integrity on doubt [M2013-088]; proxy [M1994-009]; make-the-numbers habit carried from Q4.
- Q6: retention test; buybacks; issuance [L2014-015] serial issuer candidate STOP (OPEN); dividends when the dollar cannot be used [M2004-089]; order of uses.
- Q7: definition [R1996-018]; rate = long government bond, no risk premium; floor CONVENTION about ten percent pre-tax = after company tax, before holder's tax (Whose tax); range CONVENTION: five-year average owner cash after every real cost, shown aggregate growth, ten years then zero nominal growth; TOO HARD if top > ~3x bottom (only where some case clears the floor), OUT if price inside/just below a narrower range or above the top; floor tested first. Four specifics; six specifics (a) cycles, (b) decline, (c) acquisitions, (d) working capital, (e) growth spending grows with growth and stops at year ten, maintenance charged always, (f) cap at own sales growth. The regulated utility paragraph (2026-10-18, 2026-10-23): equity-only basis central where the deciding part earns an allowed return [L2017-012], [M2010-037]; debt credit = increase over window in long-term debt (borrowings due after a year, current maturities, finance leases; CP, short-term borrowing, cash left out; securitization bonds left out with their charge), averaged per year, against growth spending only, capped at allowed debt share of the deciding part weighted by rate base; grows and stops with growth spending. All-equity beside. Fair price = each end case valued at ten percent, averaged (Part VII).
- Q8: bond first, then more of what one owns. Q9: debt against cover in bad years [L2010-012], [L2005-019] single utility insolvency; Q10 sizing; Q12 optional.
- Part VII: COMPUTATION, NOT A CLEARANCE heading after an early STOP; AFTER THE STOP: FACTS FOUND, NOT WEIGHED; research pass only where some case earns the floor; run.py arithmetic lines only.

## Close, 2026-10-25
- Box: OUT at Q7 (the floor). Central range the no-growth maintenance case alone, $9.87/share at 5.33%; depreciation variant $43.90 beside; price $77.59. Fair price $5.26 central (equity-only), $23.40 beside; all-equity basis not positive.
- Merger: all-stock, 0.98 BKH per NWE share, Montana order awaited; valued beside, changes nothing.
- Could not get: the Q3 2026 10-Q (not yet filed); Black Hills' maintenance-versus-growth capex split (not disclosed, so the combined figure uses the depreciation basis); NWE's end-2020 share price from a primary source (the proxy's $100-investment table used instead); the merger agreement's omitted schedules.
- Checks: check_ids.py PASS (131 citations, 88 distinct ids, no E-ids); tools/check_framework.py PASS.

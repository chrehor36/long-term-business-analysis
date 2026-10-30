# OGE run 2026-10-26 - working notes

Run file: `Test Runs/2026-10-26 Run - OGE OGE Energy.md`. Raw filings go to `cache/` (gitignored).

## Framework notes (one read, top to bottom, slices of at most 400 lines; read 2026-10-26 in nine slices, lines 1 to 1916)
- I: boxes IN / OUT / TOO HARD; TOO HARD records cause WORK (knowable, not done; research pass steps 1-2 written, not run) or NATURE (insiders would not write it down). Research pass run only where some case of the range earns the floor at the price (VII).
- Foundations: not a gate. Contrary evidence written down as found [M1997-127].
- Standing rule: the buyer's conduct (no borrowed money, no sudden demands); not the target.
- Q1 STOP: ten-year economics foreseeable? key variables predictable? [M2012-065], [M1998-044], [M2006-076].
- Q2 STOP: castle tests 1-11; parts table (part decides at >50% of 5-yr op profit else largest); field's returns over a full cycle judged in words; ordinary returns -> OUT EXCEPT "A return set by a regulator is the exception, carried to Q3 as a second best [M2009-104], [L2009-012]". Utilities mistake row [L2023-011] (regulatory compact can break; OPEN tension L2023-011/M2024-011). Castle open on evidence -> OUT; future cannot be judged -> TOO HARD.
- Q3 WEIGHING: returns on tangible capital, maintenance vs growth spend [L1999-024], [M2000-144]; capital-heavy second best [M2018-055], [L2009-012], [M2009-104], [M2007-112]; BNSF [L2023-009]; utility "to earn more ... must invest more" [L2011-019]. Debt STOP owned by Q9.
- Q4: balance sheets 8-10 yrs first [M2025-032]; depreciation real [R1996-023]; deferred taxes in a utility not hidden equity [M2015-030]; pensions [M2003-110], [M2013-075]; Q4 STOP on suspicion -> OUT; confusion -> TOO HARD WORK/NATURE; guidance / adjusted EPS featured = weighs against at Q4, judged at Q5 [L2019-006], [L2016-006], [M2013-088].
- Q5 STOP on integrity (doubt closes [M2013-088]); ability weighed.
- Q6 weighing: retention test; buybacks below Q7 bottom; issuance (value given vs got); STOP only on all-stock deal in undervalued stock [L2009-019]; serial issuance candidate second STOP (OPEN) [L2014-015]; dividends not by ratio [M2000-051]. Part B pay/board.
- Q7 STOP. Range convention: 5-yr avg owner cash after every real cost; growth shown on AGGREGATE owner cash, capped by Q3 and (f); 10 years then zero nominal growth; discount at long gov rate (USD = Treasury 30-yr par). Ends: no-growth and shown-growth. Specifics: all capex deducted, depreciation variant beside; (a) aberrational end year -> cycle base, literal window beside; (b) negative growth = bottom; sign change -> halves; meaningless -> no-growth alone; (c) acquisitions; (d) working capital increase is capex; (e) maintenance case central where filing allows guess; growth spend = capex above maintenance, grows with growth rate, stops after yr 10; state yr1 and yr10 growth spend; (f) cap: owner cash above highest share of sales -> cut to own sales growth.
- Floor ~10% after company's tax, no conversion. Floor tested FIRST: no case earns floor at price -> OUT whatever width. Then width >~3:1 -> TOO HARD. Price inside or just below a narrower range -> OUT. IN only screamer.
- Basis: all-equity central generally; REGULATED UTILITY: equity-only central (owner cash after interest, after tax, vs market cap); credit = increase over window in long-term debt (incl. current maturities, finance leases; excl. CP, short-term, cash; securitization bonds excluded with their charge, said so), averaged per year, credited against GROWTH spending only, capped at the deciding part's allowed debt share as filed (rate-base weighted; if allowed share stated for <half of rate base, own LTD share of LT capital at latest date). In growth case credit grows and stops with growth spend. All-equity beside. Floor earned on equity; "a utility at a full price closes OUT as before". Debt weighed at Q9 on cover in bad years [L2010-012].
- Fair price (VII): each end case valued at 10% instead of gov rate; average; per share; for utility equity-only central.
- Q8 STOP: bond first filter; more of best owned (blind run: cannot see holdings).
- Q9 weighing: debt vs ability to pay under bad conditions [M1995-104], [L2010-012]; single utility catastrophe [L2005-019]; "little or no debt" STOP stated for whole businesses only [R1997-001].
- Q10 weighing; Q12 optional.
- VII: AFTER THE STOP facts section; tools/run.py arithmetic lines only (v4 material ignored).

## Contamination log
- `git log --oneline -3` at start showed three commit subjects about other companies (NI fold, ASML fold and a follow-up). Not OGE. Not used.
- `git status --short | head -5` showed a modified file in another run's research folder (ARCB, 2026-09-27) and MBA coursework paths. Not opened, not used.
- `CLAUDE.md` (the project map, auto-loaded) names PORTFOLIO.md, RESUME STATE, WATCHLIST RUN QUEUE as files; none opened.

## Filing facts gathered (2026-10-26)
- 10-K FY2025: acc 0001193125-26-055414, filed 2026-02-18. 10-Q Q2 2026: acc 0001021635-26-000025, filed 2026-07-29. Proxy: DEF 14A acc 0001193125-26-138065, filed 2026-04-01.
- FY2023 10-K acc 0000950170-24-017400 restates 2021-2022 cash flows (cost of removal moved to investing): OCF 2022 952.4, 2021 (229.9); COR 112.7, 89.0.
- Consolidated cash flow 2023-2025 (FY2025 10-K): OCF 1,232.3 / 812.8 / 1,137.1; capex 1,178.2 / 1,090.9 / 1,054.4; COR+other 93.9 / 70.3 / 72.2; SBC 13.1/11.7/14.0; D&A 506.6/539.5/559.8.
- 2021: Enable distributions 73.4 in OCF; 2022: ET distributions 34.0 (FY2022 10-K acc 0000950170-23-003858), ET units 95.4M sold for pre-tax net proceeds 1,067.2 (investing); cash taxes 2022 276.0 "primarily relating to the sale of Energy Transfer's limited partner units"; 2023 cash taxes 41.5.
- Uri: 2021 reg assets (874.9) in OCF; 2022 +702.2 incl. ODFA securitization receipt; Oklahoma bonds issued by ODFA, repaid by customer charge over 28 years; Arkansas recovered over 10 years via reg asset.
- Rate cases: OK 2015 asked $92.5M @10.25%/53% eq -> $8.8M @9.50% (Mar 2017); AR 2016 asked $16.5M @10.25% -> $7.1M @9.5% on 50% eq + FRP; OK 2018 asked $1.9M @9.9% -> no base change, 9.5%; FERC 2019 settlement 10.0% base + 50bp (complaint sought 7.85% from 10.60%); OK 2021 asked $163.5M @10.2%/53.37% -> $30.0M @9.5%/53.37%; OK 2023 asked $332.5M @10.5%/53.5% -> $126.7M @9.5%/53.5%; AR FRP annual +6.7 (2021), +4.2 (2022), +9.6 (2023), +3.5 (2024, asked 4.7); AR FRP extension denied Sept 2022 (May 2022 order had moved to 55/45 debt/equity, reversed). 2025 OCC preapproval: settlement rejected, projects approved with no CWIP; APSC Jan 2026 denied HL 13-14 preapproval.
- Revenue by jurisdiction 2025: OCC 88%, APSC 7%, FERC 5%. Rate base by jurisdiction: not found in filings read (search "rate base" in FY2025 10-K, Q2 2026 10-Q, FY2022 10-K: no hit).
- Capex plan 2026-2030: 1,385 / 1,525 / 1,530 / 1,445 / 1,400 = 7,285.
- Ratings: Moody's negative outlook Apr 2025 (capex plan, holdco debt); S&P OG&E negative Nov 2025 (wildfire exposure).
- Equity: Nov 2025 offering 9,226,744 sh (~$397M): 4,613,372 issued, 4,613,372 under forward sale agreements (FSAs), settle within 18 months; DRIP $15-25M 2026.
- Guidance: EPS growth 5-7% through 2030; 2026 EPS $2.38-2.48; dividend payout target 60-70%.

## Close (2026-10-26)
- Box: OUT at Q7 (floor). Range $27.08 equity-only (no-growth alone, spec (b)); fair $14.43 equity-only, all-equity -$6.03; price $48.41.
- python tools/check_framework.py: PASS (run before the final commit).
- python -I check_run.py: PASS (56 distinct ids, 32 fragments checked, 0 problems).

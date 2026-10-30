# The dispatcher's batch for tools/v5_rerun_fold.py; every figure is copied from the run file and the analyst's reply.
import json
name = ("Ameren Corporation; NYSE AEE, SEC CIK 0001002910, Missouri, 10-K filer; a public utility holding company in St. Louis whose subsidiaries are "
"Ameren Missouri (rate-regulated electric generation, transmission and distribution and gas distribution), Ameren Illinois (rate-regulated electric transmission and distribution and gas distribution) "
"and ATXI (FERC-regulated transmission in the MISO), four segments; no rename, merger, spin-off or split in the 8-Ks since December 2025; "
"the 10-K names no SEC-filing rival, Evergy, WEC Energy and Xcel Energy chosen as a CONVENTION of the run")
entry = ("Price **$106.08** (close 2026-10-16, Yahoo chart feed through `tools/sources.py`, aggregator, flagged). Shares 276,843,251 at 2026-07-30 from the 10-Q cover (0001002910-26-000023), "
"read by hand because `Screens/cover_shares.py` parsed no count; no treasury stock; 16.0M shares sold forward at June 30 plus 1.4M in July, not counted, effect shown at Q7. "
"Sovereign **5.43%**, the US Treasury 30-year par yield (issuing authority), the earnings currency being the US dollar. "
"Read from the 10-K for 2025 (0001002910-26-000009), the Q2 2026 10-Q, the 2026 proxy (0001104659-26-037756), the 10-Ks for 2022 and 2020 for the earlier cycle, and ten 8-Ks; "
"2025 operating cash $3,353M checked to the filed statement. Lines of evidence derived by the analyst from Items 1, 1A and 7, stated in the run file. "
"**Q1 IN**: a regulated return on a rate base the company publishes five years ahead, $30.5B to $33.1B of capital spending for 2026 to 2030; allowed returns 8.72% (Illinois electric), 9.60% (Illinois gas), 10.48% (transmission). "
"**Q2 IN**: a legal franchise, its regulated return carried to Q3 as the regulated exception; Ameren Missouri deciding at 46.7% of four-segment net income 2021 to 2025; electric volumes 80.5B kWh (2018) to 69.4B (2025); "
"comparators Evergy, WEC and Xcel, mean return on equity 2016 to 2025 10.3% for Ameren against 8.1%, 12.0% and 10.4%. "
"**Q3 weighs against**: about 6.0% after tax before interest on all capital, 6.7% on capital added, against the 5.43% Treasury; the 10.1% to 11.4% return on equity from leverage, debt 52% to 60% of capital. "
"**Q4 no STOP, weighs against**: accounts readable; non-cash construction and deferral income in earnings; depreciation understates what keeps the system running; an adjusted EPS featured in the proxy. "
"**Q5 integrity IN, ability weighs for, modestly**: the Rush Island Clean Air Act liability ruling (2017, affirmed 2021) recorded and weighed. "
"**Q6 weighs against**: a 57% payout ratio while stock is issued every year since 2018 and planned through at least 2030; no buyback since 2017; pay on EPS, relative TSR and megawatts built, no capital charge. "
"**Q7 OUT**: owner cash 2021 to 2025 with depreciation as maintenance, central by (e), **$1,467M a year all-equity**, $1,050M equity only, flagged generous; after all spending negative every year (-$1,175M equity-only mean); "
"net debt $21,796M; growth credited at the 6.68% incremental return in place of (f)'s cut, the mechanical (e) with (f) figure $11.04 shown beside; "
"value range **$18.84 to $36.89 a share all-equity** (equity-only $69.86 to $87.91); expected return 2.87% to 3.93% at the price all-equity, 3.58% to 4.85% equity-only; "
"fair price **not positive all-equity** (both ends at ten percent below net debt), **$31.39 equity-only**. "
"Contamination declared by the analyst: LNT commit subjects in the opening git log and memory-index lines on the queue; Alliant set aside as a comparator for that reason; none used. "
"Write-early departures declared: the first full write replaced the template body after Q2, later sections rebuilt one commit per question; the Q7 arithmetic run before Q3 to Q6 were written, "
"one Q6 sentence ('fails on Q7's arithmetic') committed before Q7. "
"Commits c73196db (template), 205f203c (Step 0, Q1, Q2), c2ee0e2d (Q3 with Q4), 109304f2 (Q5 with Q6), f4f48c21 (Q7), 25d91f28 (after the stop, self-audit, notes). "
"Position note filled at the fold: not held. Citations: the analyst's `check_run.py` no problem; the dispatcher's `dispatcher_check.py` no E-id, no missing id, 54 quoted fragments within reach of an id, 1 flagged by the parser "
"('little or no debt', a parenthesis without an id in Q3, read by hand; its cited use at Q9 is in R1997-001), **no citation slip**. No tracked research file over 200 KB. check_framework PASS. "
"**For the operator** (the analyst's framework notes): (1) specific (e) against (f) when growth is bought by heavy spending; (2) the maintenance guess when the rows call a utility's depreciation too low; "
"(3) Whose tax for a regulated company and the rate on the all-equity interest add-back; (4) the equity-only growth case mixes bases; (5) serial issuance as a funding plan against the candidate STOP; "
"(6) a default comparator set when a regulated monopoly's 10-K names no rival. "
"Not armed: all-equity fair not positive and no organic-pair figure. Could not get: a maintenance-capex figure, the EEI rate chart's figures, a guidance-beat test, the FY2021 10-K's own account of 2021 operating cash.")
narr = ("OUT at Q7, on the floor and above the top of the range (Ameren Corporation, NYSE AEE; regulated electric and gas utilities in Missouri and Illinois and FERC transmission; "
"Q1 IN; Q2 IN as the regulated exception, return on equity 10.3% mean beside Evergy, WEC and Xcel; Q3 against, about 6.7% on added capital; Q4 no STOP, against; "
"Q5 integrity IN, ability for, modestly; Q6 against, ratio dividend with yearly issuance; owner cash $1,467M a year all-equity after maintenance, negative after all spending every year; "
"value range $18.84 to $36.89 all-equity at $106.08, fair not positive all-equity, $31.39 equity-only; no citation slip; not held; not armed; "
"framework gaps for the operator: (e) against (f), the utility maintenance guess, Whose tax at a regulated company, serial issuance as a funding plan)")
b = {"batch": "overnight 2026-10-18", "date": "2026-10-18", "runs": [{"t": "AEE", "name": name, "file": "2026-10-18 Run - AEE Ameren.md",
     "box": "OUT AT Q7, ON THE FLOOR AND ABOVE THE TOP OF THE RANGE", "entry": entry, "narr": narr, "fair": None, "fair_label": ""}]}
json.dump(b, open(r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-10-18 AEE\batch.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)

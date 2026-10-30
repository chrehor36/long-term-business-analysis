import json
entry = ("Price **$2.41** a share (close 2026-10-16, `tools/run.py` quote source, aggregator, flagged). Shares **41,335,823**, one class "
"(10-Q for the quarter to 2026-07-03, `0001193125-26-342455`, cover as of 2026-08-07; `Screens/cover_shares.py` the same; the balance sheet's "
"41,335,823 issued and outstanding, no treasury shares; includes the 4,289,500 shares sold at $3.50 in May 2026; no ATM sales stated); cap **$99.6M**. "
"Sovereign **5.43%** (US Treasury 30-year par yield, 2026-10-16). Documents read: 10-K FY2025 (`0001193125-26-105064`), the 10-Q for Q2 2026 "
"(`0001193125-26-342455`), the 10-Ks FY2024 (`0000950170-25-042721`) and FY2023 (`0000950170-24-038024`), the IPO prospectus of 2023-11-15 "
"(`0001193125-23-277906`) for FY2021 and FY2022, DEF 14A of 2026-04-22 (`0001193125-26-170397`), the 8-Ks of 2024-05-20, 2025-09-08, 2026-03-31, "
"2026-04-28, 2026-05-26 and 2026-10-08. Cross-check: FY2025 operating cash $(65,114) thousand on the filed statement against -65.1 in `tools/run.py`. "
"The brief's stated departures: lines of evidence derived by the analyst from Items 1, 1A and 7 (eleven lines, listed in the run file); rivals from the "
"nine the 10-K names, Granite (GVA) and Fluor (FLR) the two SEC filers, Barnard, Ames, Flatiron Dragados, Kiewit, Skanska USA, Traylor and Walsh flagged "
"as not SEC filers. **Q1 IN** narrowly: a bid-won public contractor, prime on about 96% of backlog, fixed-price revenue $434.9M of $492.8M in FY2025, "
"its key variables readable from its own and its rivals' filings. **Q2 OUT** **[L2004-003]**, **[M2017-009]**, **[M2012-106]**, **[L2007-004]**, "
"**[M2011-015]**: awards \"generally being made to the lowest bidder\" and larger rivals that \"could establish a presence in our markets\" on the filer's "
"own Item 1A; inflation absorbed on fixed-price work, gross margin negative in FY2021 and FY2024; operating margin (11.9)% FY2021 to FY2025 ((5.5)% "
"without the purchase year) against Granite 2.1% FY2014 to FY2025 (about 4.0% a year on equity) and Fluor (0.1)% FY2017 to FY2025 (about 1.6%); the "
"claimed turn to smaller and collaborative contracts two years old with no downturn, and read as reaching at best the field's ordinary returns, so OUT "
"and not TOO HARD (NATURE), the analyst declaring another analyst could close TOO HARD (NATURE). After the stop, integrity facts recorded, not judged: "
"a controlled company (GOHO, the executive chairman's vehicle, 57.8%; AECOM 18.5%); AECOM's Delaware Chancery suit released in May 2024 with 7,745,000 "
"shares issued to AECOM; MidCap defaults waived 2024 and a covenant breach waived March 2026; a special committee over the budget and use of funds under "
"an AECOM side letter; Adjusted EBITDA featured; the CEO's bonus with a guaranteed minimum of 80% of salary and a $720,000 incentive in a $25.6M loss "
"year; shares up 62% in under three years ($7.00 IPO, AECOM shares, $3.50 in May 2026), an ATM of $7.8M open; PIK interest permitted, liquidity $33M; "
"unapproved change orders and claims in revenue, no amount disclosed. Balance sheet: six year-ends only (a 2021 carve-out); 2021 equity from a $233.1M "
"bargain-purchase gain and $160.4M of cash acquired, since spent: cash $77.8M to $16.9M, retained earnings $49.1M to $(113.2)M, equity a deficit of "
"$(50.3)M, debt nil to $72.4M, contract assets $122.5M, PP&E $19.1M to $6.7M. COMPUTATION, NOT A CLEARANCE: owner cash FY2021 to FY2025 (operating "
"cash less stock pay and all capital spending) (58.1), (15.8), (97.2), (37.9), (76.7), mean **$(57.1)M**, negative every year, H1 2026 operating cash "
"$(24.6)M; (b) the no-growth case alone, a growth rate on an all-negative series meaningless; (e) capex basis central, depreciation beside; no tax paid, "
"no shelter priced; net debt $58.1M; value **$(26.25)** a share all-equity, a single case wholly below zero against $2.41 ($(29.73) depreciation "
"variant, $(25.46) equity-only); no case earns the floor at any positive price; fair **$(14.90)** all-equity, **$(13.83)** equity-only; not armed "
"(box OUT at Q2). Contamination declared by the analyst: one directory listing of `Test Runs/` filtered for SHIM or SCCI at the start, no match, "
"declared; the TSSI commit subjects and memory index lines; the 10-K's own statement that Berkshire Hathaway provides surety bonding and lends under the "
"credit agreement, used only as a filing fact; none used. Commits be18bf5e (template), b3a2d295 (Step 0), c27f1308 (Q1), 05e5535f (Q2), 6e5c3078 "
"(close). Position note filled at the fold: not held. Citations: the analyst's `check_ids.py` PASS (31 ids, 32 fragments); the dispatcher's "
"`fold_cite_check.py`, 30 fragments immediately beside an id, **no slip**, 31 ids all in the ledger, no E-ids. No tracked research file over 200 KB. "
"check_framework PASS. **For the operator** (the analyst's framework notes): (1) Q2's change-for-the-better rule and its ordinary-returns rule meet "
"with no rule for which governs, so the same file could close OUT or TOO HARD (NATURE); (2) the parts paragraph assumes five years of operating profit "
"by part, here two years of gross margin only; (3) Q4's eight to ten years of balance sheets cannot be had for a recent carve-out, and nothing says "
"whether to seek the predecessor's years; (4) Q7 states no case for an owner-cash series negative in every year. Could not get: the rivals' figures read "
"in their filed statements (tagged data used), FY2023 cash interest (bounded), the amount of claims and unapproved change orders, the Forms 4 and 144, "
"the AECOM complaint, part-level operating profit beyond two years.")
narr = ("OUT at Q2 (Shimmick Corporation, Nasdaq SHIM; public water, dam, lock and transit contractor, mostly California, carved out of AECOM in 2021). "
"Contracts won \"generally\" by \"the lowest bidder\" and larger rivals free to enter on the filer's own words; operating margin (11.9)% FY2021 to FY2025 "
"against Granite 2.1% and Fluor (0.1)% over their cycles, the field ordinary and the claimed turn two years old. Integrity facts recorded, not judged: "
"a controlled company, the AECOM suit released for shares, lender defaults and a covenant breach waived, a guaranteed bonus floor, shares up 62% in under "
"three years. Computation beneath the stop: owner cash negative every year, mean $(57.1)M; value $(26.25) a share all-equity, wholly below zero against "
"$2.41; fair $(14.90) all-equity ($(13.83) equity-only); not armed. Framework gaps for the operator: Q2's change rule against its ordinary-returns rule, "
"the parts rule with two years of gross margin, Q4's balance sheets for a carve-out, Q7 on an all-negative owner-cash series.")
b = {"batch": "overnight 2026-10-17", "date": "2026-10-17", "runs": [{
  "t": "SHIM",
  "name": "Shimmick Corporation; Nasdaq SHIM, SEC CIK 0001887944, formerly SCCI National Holdings, Inc. until August 2023; water and critical infrastructure construction (water and wastewater treatment, desalination, dams, locks, transit), mostly in California, backlog about $793M at 2026-01-02; sold by AECOM in 2021, IPO November 2023; an ATM agreement of 2025-09-08, 4,289,500 shares sold at $3.50 in May 2026, a $14.3M Sixty-First Commercial Finance loan and Amendment No. 11 to the credit agreement 2026-10-02, a new chief operating officer from 2026-04-28",
  "file": "2026-10-17 Run - SHIM Shimmick.md",
  "box": "OUT AT Q2; integrity facts recorded, not judged",
  "entry": entry, "narr": narr, "fair": None, "fair_label": ""}]}
json.dump(b, open("Test Runs/_research 2026-10-17 SHIM/batch.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)

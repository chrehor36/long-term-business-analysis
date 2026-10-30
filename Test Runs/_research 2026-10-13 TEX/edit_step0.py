p = "Test Runs/2026-10-13 Run - TEX Terex.md"
s = open(p, encoding="utf-8").read()
head_new = """# Company Run — Terex Corporation (NYSE: TEX) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**
*(Copied from `Test Runs/_TEMPLATE - Company Run.md` before any fetch; research folder `Test Runs/_research 2026-10-13 TEX/`.
A dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the brief's one stated departure: the lines of
evidence are derived by the analyst from the FY2025 10-K's Items 1, 1A and 7.)*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**CONTAMINATION, declared:** (1) the session context shown at start carried the subjects of the five most recent commits
of the repository, which name another company's v5 run (a Hong Kong machinery maker, its box and its computed range); (2) a
directory listing of `Test Runs/` made to copy the template showed the file names of other runs dated 2026-10-12 (names
only), and a name filter for "TEX" showed the file names of runs on other companies whose tickers contain those letters
(names only, none about Terex; no prior Terex run file was listed); (3) the memory index loaded at start carried one-line
notes on the queue and on how many names had cleared. None of them was opened, and nothing of them is used.

---
"""
s = head_new + s[s.index("## STEP 0"):]
step0_old = s[s.index("## STEP 0"):s.index("## THE FOUNDATIONS")]
step0_new = """## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $51.49 (51.485, quote of 2026-10-13 through `tools/sources.py`; **aggregator, live quote only, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock $0.01 par, **114.3 million** outstanding as of
  2026-07-28 (10-Q for the quarter to 2026-06-30, filed 2026-07-30, accession `0000097216-26-000116`;
  `python Screens/cover_shares.py TEX`). Checked against the same 10-Q's balance sheet: issued 134.4 million less 20.8 million
  in treasury = 113.6 million at 2026-06-30, the 0.7 million gap falling in the four weeks to the cover date. The REV merger
  issued 47.9 million shares on 2026-02-02 (8-K of 2026-07-31, Exhibit 99.2, accession `0000097216-26-000124`, Note 2:
  "In connection with the Merger, there were an additional 47.9 million shares of Terex issued upon conversion"); they are
  inside the cover count, since 85.5 million issued at 2025-12-31 became 134.4 million at 2026-06-30. No 8-K after the 10-Q
  issues shares (filing list read through the 8-K of 2026-08-03, accession `0000097216-26-000130`).
- **Market cap:** 114.3 million x $51.485 = **$5,885M**.
- **Net debt at the latest filed date (2026-06-30, 10-Q `0000097216-26-000116`, Note I):** total debt $2,687M (5% notes 2029
  $597M, 6.25% notes 2032 $737M, term loan 2031 $1,214M, revolver $110M, secured borrowings $20M, finance leases $9M) less cash
  $407M = **$2,280M**. Operating leases left out, said so. The REV cash consideration ($548M including REV's bank debt repaid,
  against $81M of REV cash acquired) is inside these balances, the merger having closed on 2026-02-02.
- **Sovereign for the earnings currency (USD):** **5.60%**, US Treasury daily par yield curve, 30-year, 10/09/2026
  (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-13, accession `0000097216-26-000035` (Items 1, 1A, 7, 8);
  10-Q for the quarter to 2026-06-30, filed 2026-07-30, `0000097216-26-000116`; proxy (DEF 14A) filed 2026-04-29,
  `0000097216-26-000071`; 8-K of 2026-07-31 with REV's last quarter and the pro forma combination, `0000097216-26-000124`;
  the 10-Ks for FY2018 to FY2024 (`0000097216-19-000024`, `-20-000027`, `-21-000030`, `-22-000013`, `-23-000012`,
  `-24-000013`, `-25-000011`); REV Group's 10-Ks for FY2021 to FY2025 (`0001564590-21-060365`, `0000950170-22-026493`,
  `0000950170-23-069876`, `0000950170-24-135208`, `0001193125-25-313470`). **One figure cross-checked against the filed
  statement:** net cash provided by operating activities FY2025 **$440M**, read on the filed Consolidated Statement of Cash
  Flows (10-K `0000097216-26-000035`, page F-8), equal to the XBRL figure `tools/run.py` printed.
- `python tools/run.py TEX` arithmetic lines only (output kept at `Test Runs/_research 2026-10-13 TEX/run_py_output.txt`):
  operating cash $459M, $326M, $440M (FY2023 to FY2025); stock pay $44M, $30M, $32M; capex $127M, $137M, $118M; D&A $56M,
  $82M, $157M (FY2025 includes the amortization of ESG intangibles). Its "capex alt" column doubles capex by adding a
  company-tagged line (`tex:PaymentstoAcquireProductiveAssetsincludingdiscontinuedoperations`) that is the same payment
  under another tag; the filed cash-flow statement shows one capex line ($118M for FY2025), so the alternate is a double
  count and is not used. Five-year owner cash and the recast are built at Q4 from the filed statements.

"""
s = s.replace(step0_old, step0_new)
found_old = s[s.index("## THE FOUNDATIONS"):s.index("---\n## Q1")]
found_new = """## THE FOUNDATIONS (not a gate)
A share is a business, and the test is the closed market: "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**. For Terex the answer turns on what its businesses earn through a fall in their customers' spending, since the
company sells equipment to rental fleets, quarries, haulers, utilities, municipalities and RV buyers. The market serves and
does not instruct, "It just tells us prices." **[M2006-077]**: the $58.99 at which the company issued 47.9 million shares to
REV's holders on 2026-02-02 and the $51.49 quoted today are prices, not findings. Who is paid to tell you bears on the two
deals of 2024 and 2026 and on the company's yearly EBITDA and EPS outlook: "you do not get impartial advice from Wall
Street" **[M2020-037]**. The margin of safety is an attitude here **[M1996-084]**. **Contrary evidence, written down as found**
**[M1997-127]**: (1) debt rose from $623M at 2023-12-31 to $2,687M at 2026-06-30, through the ESG purchase (cash, borrowed) and
the REV merger (its cash leg from the revolver and cash); (2) the 10-K says the company competes "particularly" on price and
that "Low-cost competition from China and other developing markets could also result in decreased demand for our products"
(Item 1A), and the Aerials segment margin fell to 5.0% in 2025; (3) the segment measure changed in 2026 to "Adjusted segment
operating profit" (10-Q, Note B); (4) the portfolio has been remade repeatedly, "much of this change has been historically
accomplished through acquisitions and managing our portfolio of companies by divestiture of non-core businesses and
products" (Item 1), so the past statements are statements of a different set of businesses; (5) the first-filed FY2016
figures show an operating loss of $147.8M (XBRL OperatingIncomeLoss, FY2016 vintage).

## THE STANDING RULE
The buyer's own conduct: a purchase of these shares for cash, unborrowed, sized so that a fall of half or more could be sat
through, puts the buyer at no risk of ruin. "We are never going to risk what we have and need for what we don’t have and
don’t need." **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target's own debt
is Q9's question, not this one.

"""
s = s.replace(found_old, found_new)
open(p, "w", encoding="utf-8").write(s)
print("ok")

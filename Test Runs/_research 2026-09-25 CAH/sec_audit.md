## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Step 0, Q1 IN, Q2 OUT; Q3-Q6 marked NOT REACHED and their
      material recorded beneath the close without verdicts.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the 10-K's own
      description of how each segment is paid, clause by clause.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives: none issued. The unobtained peer (Owens & Minor)
      is named at Q2 with the reason, and why the verdict does not rest on it.
- [x] Every UNKNOWABLE verdict states what specifically cannot be known: none issued; the perimeter close was
      considered at Q2 and refused in writing.
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked (FY2026 operating cash $5,174M
      rebuilt from its lines; ties). The screen's `wc_note` was tested against the FY2025 statement and refuted as a
      description; its `acq_note` reproduces exactly.
- [x] Owner earnings on a multi-year mean; eight windows and two constructions stated over fifteen filed years; capex
      band disclosed as a judgment, finance-lease additions included (beneath the close).
- [x] Competitor row filled: McKesson, Cencora and Medline (3 of 4 named), XBRL transcription flagged, segment margins
      from the peers' 10-K text; the verdict rests on the customers' conduct in three registrants' filings, and why is
      stated.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury par curve), dated
      09/24/2026.
- [x] Value stated as a round-number range, not a point estimate (inside a COMPUTATION block only).
- [x] One bar chosen, not both: none; Q5 not reached. Windage count stated (one).
- [x] Prices dated; aggregator used for the live quote only and flagged.
- [x] Run committed to git, with pathspecs, after the claim, after Step 0 and Q1, after Q2 and after this section.
- [x] Ledger ids: every id cited in this file was resolved against `principle_ledger.csv` (311 rows by
      `csv.DictReader`) before citing, quotes taken from `quote_verbatim` (pull saved as `ledger_rows.txt`); the count
      and the zero-phantom check are recorded in the fold commit's message and `check_out.txt`. [E4-52] is not used for
      incentives; the incentives row is [E4-27].

**The brief's priors, scored:**
- *CAH's fiscal year ends June 30; the FY2026 10-K should be the newest periodic*: **confirmed** (filed 2026-08-11,
  `0000721371-26-000038`; the cover count is as of July 31, 2026).
- *The `wc_note` "one line made the cash" may be wrong about total working capital (the MHH defect)*: **confirmed**:
  FY2025 total working capital was a $523M use; payables offset an inventory build and the OptumRx unwind.
- *acq_note: acquisitions inside the window large relative to cap; establish the perimeter*: **confirmed and
  reproduced** ($8,463M FY2022-26), extended to $21.9bn over fifteen years with $6.4bn of goodwill written off.
- *Verify SBC resolves and is complete*: **resolves and complete** ($367M = $122M + $245M from The Specialty Alliance's
  own plan; the cash side of the physician units is in operating cash); grant value about $154M higher, recorded.
- *deal_note: check for a live deal*: **none live against Cardinal**; Cardinal is an acquirer (Strive Medical completed,
  the AdaptHealth diabetes business announced, prices not in the documents read).
- *The spread caveat: the 4-construction width cannot see variation older than five years; rebuild it*: **rebuilt over
  fifteen years**; the width is dominated not by (c) but by the trade working-capital line, which the screen's
  constructions all include.

**My own errors, caught before commit:**
1. Q1's first draft said the physician platforms were bought for "about $7.4bn in eighteen months"; the filed purchases
   (ION, GI Alliance, Urology America, Solaris) are about $6.2bn in twelve months; ADS ($1.0bn) is a home-supply
   business, not a physician platform. Corrected before the Step 0/Q1 commit.
2. The perimeter's first draft described FY2016's $3,614M as "chiefly Cordis and naviHealth" and FY2013's $2,239M
   without a name; the 10-Ks name The Harvard Drug Group (July 2015) and AssuraMed (March 2013). Corrected in the Q2
   commit.
3. Q2's first draft said the three wholesalers "stayed profitable for the whole window except the opioid charges";
   Cardinal's FY2018 and FY2022 operating losses were medical-products write-downs. Corrected before the Q2 commit.
4. My first `peers.py` divided figures that `sources.annual()` already returns in millions by a further million and
   printed zeros; caught on the first read and rerun.
5. My first exhibit fetch wrote EX-99.1 and EX-99.2 of the August 2025 8-K to one filename, so the second overwrote the
   first; caught when the guidance grep returned the wrong document, refetched under distinct names.
6. A ledger dump first failed on the console's cp1252 encoding (the MHH error again); rerun with UTF-8.
7. Beneath the close, four figures in the first draft were corrected before commit: working capital a source in
   "twelve" of fifteen years (eleven); the suppliers'-credit gap "$0.5-1.6bn" ($0.6-1.5bn, and nil in FY2017-21);
   coverage on construction A "9-11 times" (10-11 on FY2026); and an unsourced "2022" date for the Elliott agreement,
   removed.

**Errors in the brief:** none found that bear on a verdict. Its counts were checked rather than inherited: the ledger is
311 rows by `csv.DictReader`, `_wave7_done.txt` held 34 lines ending MHH, line 35 of `_wave7_order.txt` is CAH and line
36 is NATH. One conflict recorded: the brief's commit trailer (*"Claude Opus 5 (1M context)"*) differs from the
session's attribution instruction (*"Claude Opus 5.5"*); the claim, Step 0/Q1 and Q2 commits carry the brief's form,
later commits the session's.

**Tooling observations (reported, not patched):**
- **`working_capital_flag()` fired "ONE LINE MADE THE CASH" on a year whose total working capital was a use** (FY2025,
  -$523M), the second run in a row to find it (MHH 2021). A check of the sign of total working capital before the
  sentence is written would stop it.
- **The screen band's two ends come from different windows again**: `oe_bottom` $2,503M is the five-year D&A end,
  `oe_top` $2,900M the three-year capex-plus-finance-lease end (reproduced in `oe.py`). The BA, ACMR, ALKT and ACVA
  defect, now on a positive band.
- **`run.py`'s D&A rule replaced a filed total with a larger component sum**: FY2024 `Depreciation` $470M +
  `AmortizationOfIntangibleAssets` $264M = $734M against the filed `DepreciationDepletionAndAmortization` of $710M
  (FY2025 $791M against $790M). The code comment says *"PREFER A FILED TOTAL; WHERE NONE EXISTS, SUM THE COMPONENTS"*;
  the code overrides the total whenever the parts are larger. Conservative direction, $24M here.
- **No construction the screen or `run.py` prints separates the trade working-capital lines**, so for a negative
  working-capital distributor every published figure is construction A, about double construction B on the recent
  windows.
- `sources.cik_for()` returned HTTP 404 for OMI (Owens & Minor); not investigated.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- One line: **CAH FAIL at Q2 (OUT, ON THE BUSINESS). Q1 IN. [E3-03] criterion (2) fails on the customers' filed
  conduct: Express Scripts (2012), Walgreens (2013, $16.9bn) and OptumRx (2024, 17% of revenue) left for rivals, two of
  them now among Cencora's largest accounts; CVS Health is the largest customer of both Cardinal (28%) and McKesson
  (24%); Cardinal pays CVS quarterly under Red Oak. The demonstration clause fails: gross margin 5.57% to 3.84%
  (FY2015-FY2026), pharmaceutical segment profit flat in dollars FY2015-FY2023 while revenue doubled, medical products
  at 0.7-2.0% with $5.4bn of goodwill written off. [E2-53]: the customer's renewal, not the business, sets how good the
  year will be.** Price $222.62 (2026-09-24, aggregator, flagged) x 232,575,728 shares (10-K cover,
  `0000721371-26-000038`) = $51.78bn; sovereign 5.47% (US Treasury, 09/24/2026).
- **If UNRESEARCHED:** not applicable.
- **If UNKNOWABLE:** not applicable.

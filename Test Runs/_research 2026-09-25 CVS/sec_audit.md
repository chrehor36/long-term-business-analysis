## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN, Q2 OUT. Q3, Q4 and Q6 carry material only; Q5's block is
  replaced by COMPUTATION - NOT A CLEARANCE with no box and no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 rests on the FY2025 10-K's Item 1 and
  segment tables and the predecessor 10-Ks; every prior in the brief was checked against a filing before use (below).
- [x] Every UNRESEARCHED verdict names the artifact: **none issued.** The unmeasured competitors (Prime, MedImpact, the Blues
  plans, Kaiser, Walmart and Kroger pharmacy) are private, non-filing or unsegmented, named at Q2; no document exists to
  fetch for them.
- [x] Every UNKNOWABLE verdict states what cannot be known: **none issued.** [E4-04]'s perimeter close was considered and
  refused in writing at Q2.
- [x] **Step 0: the filing was read, accession numbers recorded; 2025 net cash provided by operating activities of $10,639M
  rebuilt from its own reconciliation lines and tied to the direct-method total.** A second cross-check: the 2017 operating
  cash, capex and SBC read in two filings (FY2017 Exhibit 13 and FY2019 10-K) agree; ELV's and HUM's benefit ratios in the
  reused UNH row re-read from their FY2025 10-Ks and agree.
- [x] **Owner earnings on multi-year means, four windows up to ten years, both (c) ends, the judged end disclosed; SBC from
  the cash-flow line in every year; the insurer's float growth stripped; no net-income proxy.** The sector-method question
  the brief raised is decided in writing at Stage 0(b): an operating company that owns a health insurer, ordinary method,
  three sector-method corrections bound.
- [x] **Competitor rows filled**, three of them (insurer, PBM, drugstore), every cell read by this run from the named filing;
  the insurer row's UNH/CI/CNC cells reused from the UNH run's filing-sourced row, the ELV and HUM cells re-read; no
  sub-agent used. Limits stated at each row.
- [x] **Sovereign for the earnings currency (USD), from the issuing authority, dated**: 5.47%, US Treasury daily par yield
  curve, 30 Yr, 09/24/2026, raw file saved; FRED not used.
- [x] Value stated as a round-number range, inside the COMPUTATION only.
- [x] One bar: none chosen, because Q5 did not open; windage count stated (ONE).
- [x] **Prices dated; aggregator used for the live quote only and flagged** ($85.05, close 2026-09-24, Yahoo chart endpoint,
  raw response saved).
- [x] **Every ledger id cited checked against `principle_ledger.csv`: 76 distinct ids in this file, none missing**; every row
  cited in the run's own sections was opened and read before citing. `tools/check_framework.py` run before the fold commit.
- [x] Run committed to git with pathspecs: `d9e33c8` (claim), `0f6200b` (Step 0, Q1), `73c3586` (Q2), then the commit
  carrying the material beneath the close and this audit, then the fold commit.

**THE BRIEF'S PRIORS, each checked against a filing:**
1. *Three segments* - **half right.** The 10-K reports **four** reportable segments (*"Health Care Benefits, Health Services,
   Pharmacy & Consumer Wellness and Corporate/Other"*), and Health Services is not only the PBM: it also holds the Health
   Care Delivery assets (Oak Street, Signify), whose losses sit inside the PBM's segment result from 2023. The three-business
   reading holds for the operating businesses.
2. *The perimeter* - **confirmed and extended**: Aetna (2018, cash and stock), Signify and Oak Street (2023, $16.6bn cash), the
   2025 Health Care Delivery impairment ($5.7bn); **not in the brief**: Omnicare's Chapter 11 and deconsolidation (2025),
   the exchange exit (2026), the MSSP sale (2025), and the LTC impairment of 2018 ($6,149M).
3. *CEO replaced 2024; guidance withdrawn; PBM under regulatory and litigation pressure* - **all confirmed** from the 8-K of
   2024-10-18, the 2024 releases, the 10-K and the 10-Q (the July 2026 FTC settlement proposal was not in the brief).
4. *One payables line moved about a third of 2025 operating cash* - **arithmetically confirmed (36.2%) and resolved: net
   working capital was a use of $1,474M in 2025.** The line that moved a year was the insurer's float in 2024 (+$2,757M).
5. *Pull the latest EX-99.1* - done; [E4-29] does not fire, [E4-22]'s third flag does.

**ERRORS, ARTIFACTS AND REPORTED-NOT-PATCHED, recorded rather than smoothed.**
1. **My own errors, caught before commit.** The Q1 draft said *"about $59bn of acquisitions"* and *"about $12.5bn of
   goodwill"* written off, and that guidance was cut *"twice in three months"*; the cash-flow lines sum to about $61bn, the
   impairments to about $12.3bn, and the cuts were May and August 2024. The Q2 draft attributed 427 million claims to
   Cigna as a fact (CVS does not name the client; restated as consistent with the timing), called CVS *"the largest drugstore
   chain"* and *"a top-five insurer"* (neither in a filing read; replaced by store counts and the 37 million figure), said
   Rite Aid was *"in liquidation"* and *"in bankruptcy"* (not read by this run; removed), miscounted the pharmacy-competitor
   classes (nine, not seven) and the retail per-script declines (seven of eight years, not eight of nine), and wrote the
   Walgreens comparison as five of six (four of five). The Q3 draft paraphrased [E3-44] past its words (*"better picture"*;
   the row says *"a pretty good indication of earning power"*) and placed both buybacks inside the collapse year (only the
   second was). All corrected before commit.
2. **Not read: the DEF 14A of 2026-04-03.** Pay design and incentive metrics are not scored; the file closed at Q2, so no
   verdict depends on it.
3. **Segment definitions changed in 2023** (Pharmacy Services to Health Services with the delivery assets; Retail/LTC to
   Pharmacy & Consumer Wellness), so the long PBM and retail series cross a definitional break; the direction statements are
   made within each run of years as well as across the break.
4. **The template's STOP sign.** The template marks the Q5 gate with a warning symbol; this file's stop line uses the words
   only.
5. **The price** has fallen every session since 2026-09-15 ($94.49 to $85.05) with no 8-K filed since 2026-08-17; nothing in
   this file depends on the reason, and none is offered.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- **One line: Q1 IN / Q2 OUT, on the business.** Three spread businesses (a PBM, a Medicare-heavy insurer, a drugstore
  chain) whose prices are set by the other side: PBM clients *"can move between us and our competitors"* and one did (claims
  -18.2% in 2024), the price goes to the client every year (*"continued pharmacy client price improvements"*); the insurer's
  rate is CMS's and its insured book fell 21% when repriced; the stores' earnings per prescription fell 45% since 2017 on
  payer reimbursement, as Walgreens' did. 2025 adjusted operating income below 2019 in nominal dollars after about $61bn of
  acquisitions since 2018. At $85.05 (cap $108,776M) against a 5.47% sovereign the owner-earnings yield is about 6% to 9%,
  recorded as arithmetic only.
- **If UNRESEARCHED - THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.

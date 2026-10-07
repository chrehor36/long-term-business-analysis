---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN, Q2 OUT. Q3, Q4 and Q6 carry material only; Q5's block is
  replaced by COMPUTATION - NOT A CLEARANCE with no box and no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 rests on the filed FY2026 statements,
  Item 1 and the FY2010 10-K; the brief's two general-knowledge beliefs were verified against the filings before use.
- [x] Every UNRESEARCHED verdict names the artifact: **none issued.** The unmeasured competitors are private or
  non-segmented, named at Q2; no document exists to fetch for them.
- [x] Every UNKNOWABLE verdict states what cannot be known: **none issued.** [E4-04]'s perimeter close was considered and
  refused in writing at Q2.
- [x] **Step 0: the filing was read, accession numbers recorded; FY2026 net cash provided by operations of $612M rebuilt
  from its own lines.** A second cross-check: FY2025 net tangible operating assets recomputed from the filed balance sheet
  ties to the companyfacts figure (1,438 both ways).
- [x] **Owner earnings on multi-year means, five windows up to sixteen years, both (c) ends, the judged end disclosed, the
  Glad buyout shown both ways; SBC from the cash-flow line in every year; no net-income proxy.**
- [x] **Competitor row filled**: five company-level peers reused from the CL run's row (cited as that run's evidence, the
  Clorox cells re-derived here), plus Reynolds (Hefty) from its 10-Ks and Reckitt (Lysol) from its annual reports and H1
  2026 announcement, both transcribed by sub-agents of this run with every cell sourced; figures read against the sub-agents'
  files, and two quotes (Reckitt's 700bps and H1 2026 share sentences) spot-checked in the extracted text before use.
- [x] **Sovereign for the earnings currency (USD), from the issuing authority, dated**: 5.47%, US Treasury daily par yield
  curve, 30 Yr, 09/24/2026, raw file saved; FRED not used.
- [x] Value stated as a round-number range, inside the COMPUTATION only.
- [x] One bar: none chosen, because Q5 did not open; windage count stated (ONE).
- [x] **Prices dated; aggregator used for the live quote only and flagged** ($81.80, close 2026-09-24, Yahoo chart endpoint,
  raw responses saved).
- [x] Every ledger id cited checked against `principle_ledger.csv` (all present; the quotations used were read against
  the rows); `tools/check_framework.py` run before the fold commit.
- [x] Run committed to git with pathspecs: `063170b` (claim), `d8f8489` (Step 0, Q1), `ad3e896` (Q2), `7dbba04`
  (beneath the close), then the fold commit (the queue file staged from the HEAD blob plus the register entry only).

**ERRORS, ARTIFACTS AND REPORTED-NOT-PATCHED, recorded rather than smoothed.**
1. **The brief's error.** The brief said the screen's `newest_filing` of 2025-06-30 meant the screen was built before the
   FY2026 10-K. The 10-K was filed 2026-08-07, before the screen's date; the cause is that **SEC companyfacts had still not
   ingested the FY2026 10-K on 2026-09-25**, seven weeks after filing (Step 0). The brief also said the CL run recorded Clorox's
   volume as *"-10 then -7"*; those are FY2023 and FY2026, not consecutive years, with -5 and +7 between them (the CL run's own
   row reads +6 / -5 / -10 / -5 / +7 / -7, which this run re-read from the bridge tables and confirms). And the brief's
   perimeter prior named only disposals; **the largest perimeter event is an acquisition, GOJO ($2,147M, April 2026), plus a
   $476M buyout run through operating cash**, neither of which the brief mentioned. The brief's other priors (the disposals,
   the cyberattack, the ERP disruption, the stale cap) were each right on the filings.
2. **REPORTED, NOT PATCHED: `tools/run.py` cannot see a 10-K that companyfacts has not ingested, and does not say so.** On
   CLX it priced FY2023-FY2025 as "the mean of 3 years" with no warning that a newer 10-K sat in EDGAR submissions. A check
   that compares the newest 10-K in `submissions` with the newest 10-K accession in companyfacts would name the gap. Not
   patched by this run, as the brief instructed for the sibling run.py defect of the same night.
3. **REPORTED, NOT PATCHED: the cap guard in `Screens/regen_queue.py` compares a cap and a float struck at different dates.**
   *"A cap cannot be smaller than a subset of itself"* is true only on one date; for a stock that fell 37% between the float
   date (2024-12-31, $162.41) and the cap's price, it fires on two correct numbers. Dating both, or restating the float at the
   cap's price date, would separate a stale input from a wrong one.
4. **My own error, caught before the Q2 commit:** the first Step 0 draft said the two disposed businesses were *"loss-making
   or low-margin"*; no filed figure read supported that for Argentina. Replaced by the filed VMS impairments. A second, in the
   Q2 draft: the row sentence said Clorox's operating margin was lowest in the row in four of five years; it is three
   (FY2022-FY2024). And the Q4 draft's capex and D&A sums and the FY2011-15 owner-earnings mean were first typed from memory of
   the table and were wrong ($3,362M, $3,205M, $522M); recomputed as $3,382M, $3,105M, $538M before commit.
5. **Text artifacts.** The stripped text of the FY2014-FY2016 10-K exhibits renders the registered-trademark sign as the
   replacement character (U+FFFD); the quotations restore the filed *"®"*, which is the filing's character and this run's
   extraction artifact. The Reckitt sub-agent flagged out-of-column numbers in two annual-report summary boxes and re-extracted
   the H1 2026 tables with a second library; see `peers_reckitt/RECKITT_ROW.md`. The REYN sub-agent flagged a garbled dash
   (nil) in three 10-Ks and a $4M unreconciled capex gap in FY2019.
6. **Repository weight, disclosed:** the Reckitt annual reports' extracted text (about 13 MB of `.txt`) was committed with the
   Q2 commit, because the verbatim Reckitt quotes rest on it; the PDFs themselves are ignored by `.gitignore`. Recorded, not
   rebased.
7. **The price is the lowest close in the two-year series** and has fallen every week since 2026-08-28 with no 8-K filed;
   nothing in this file depends on the reason, and none is offered.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- **One line: Q1 IN / Q2 OUT, on the business.** A maker of branded household staples that earns a high return on its small
  tangible capital, as every branded staple does, but whose price rises cost it units in its own words (bleach FY2015, Glad
  FY2014 and FY2019, the company FY2023 *"primarily due to pricing actions"*), whose units are below FY2019 after about 28
  points of price, whose EBIT is lower in nominal dollars than in FY2019, and whose direct disinfecting competitor reports
  share gains since 2019. At $81.80 (cap $9,892M) against a 5.47% sovereign the owner-earnings yield is about 6.3% to 7.8%,
  recorded as arithmetic only.
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.

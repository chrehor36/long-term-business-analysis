
---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN, Q2 OUT; the file closed at Q2; Q3-Q6 recorded beneath
      the close without boxes)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** (Q1 IN rests on the 10-K business
      descriptions FY2007-FY2025 and the FY2025 unit economics, all read)
- [x] Every UNRESEARCHED verdict names the artifact and where it lives (none issued)
- [x] Every UNKNOWABLE verdict states what specifically cannot be known (none issued; the [E4-04] perimeter close was
      not needed because [E3-03] fails first, on criteria (2) and (3))
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked (FY2025 OCF $75,058K in the filed
      statement = MD&A = tag; Q2 adds FY2010 revenue $211,233K and operating income $33,190K, and FY2025 operating income
      $86,677K, each read in the filed statement)
- [x] Owner earnings on a multi-year mean; every window FY2008-FY2025 published with both (c) ends, after the partners'
      share, with the partner-buyout choice shown apart; the negative and near-zero years named (2011 negative after
      buyouts; 2021 and 2022 near zero at the low end after buyouts); SBC resolves and is complete (beneath the close)
- [x] Competitor row filled (Select Medical's outpatient segment and ATI Physical Therapy, the two SEC filers, same
      per-visit metric over 2015-2025; both now deregistered; every other competitor files nothing; the verdict does
      not rest on the row)
- [x] Sovereign is for the earnings currency, from the issuing authority, dated (5.49%, US Treasury 30-year par,
      09/25/2026, struck fresh; FRED not used)
- [x] Value stated as a round-number range, not a point estimate (computation only)
- [x] One bar chosen, not both; windage count stated (ONE; no bar applied, Q5 not opened)
- [x] Prices dated; aggregator used for the live quote only and flagged ($84.84, 2026-09-25 close, Yahoo chart
      endpoint, raw response saved)
- [x] Run committed to git (claim `ce883969`, Step 0 and Q1 `553bf209`, Q2 `b3372d0f`, beneath the close
      `e92f0020`, this section and the fold after)

**Brief priors, each tested:**
1. *deal_note: two Item 1.01 8-Ks, most likely credit or an offering* — **half confirmed**: one is the $450M credit
   agreement (2026-04-15); the other is the new CFO's employment agreement (2026-08-14). No deal; the quote is not a
   spread.
2. *acq_note: acquisitions $322M, 27% of cap, inside the window* — **confirmed in kind and read**: $15.7M (2025),
   $133.1M (2024), $26.6M (2023), $59.8M (2022), $86.8M (2021) from the filed statements, $322.0M over 2021-2025. What it
   does: growth bought while the owned base is flat, goodwill and intangibles to $865.3M, the return on what was paid
   down to 9.6% pretax.
3. *spread_caveat: rebuild the width over older windows* — **done**: 3, 5, 10 and 18-year windows, both (c) ends, with
   and without partner buyouts.
4. *The roll-up's partnership structure and what the parent owns* — **read and applied**: the screen's owner earnings
   omit the partners' share entirely (below).
5. *level_shift 1.09 / 1.47, no step* — consistent with the rebuilt table: no single distorted year drives any window;
   2020-2021 carried Relief Funds, removed.

**Errors of mine caught before commit:** (1) a first grep of the 2026 10-Q and release for "per visit" returned
nothing, and I nearly recorded that the company had **dropped** the rate metric in 2026; the phrase was split across
extracted lines, and a whitespace-normalised search found it renamed and widened (*"Physical therapy revenue per patient
visit"*). The run records the widening, not a withdrawal. (2) I first gave Select Medical 1,933 clinics at end 2025;
its table runs 2023 to 2025 left to right, so 1,933 is 2023 and 1,917 is 2025; corrected. (3) I first wrote that
Select Medical "completed a take-private"; I read only the EDGAR index, so the text now says what the index shows.
(4) I first wrote the partners' distributions as $14.7-18.3M a year 2018-2025; 2025 was $19.3M; corrected.

**Tooling defects, reported, not patched:**
1. **The screen and `tools/run.py` compute owner earnings on consolidated operating cash and never subtract the
   non-controlling partners' share.** For USPH the partners took $14.7-19.3M a year in distributions 2018-2025 (31.8% of
   2025 net income), so the screen's $49-59M and `run.py`'s $51-59M overstate the owner's figure by roughly a quarter to
   two-fifths, and every yield and growth-required field built on them. Any filer with material non-controlling
   interests (clinic partnerships, MLP general partners, joint-venture-heavy filers) carries the same error. The fix
   would subtract `PaymentsToMinorityShareholders` or the distributions line where it resolves, and flag where it does
   not.
2. **The screen's `acq_note` counts acquisitions but not purchases of partner interests** ($8.4-29.5M a year
   2019-2025), a second recurring use of owner cash in this structure.
3. **A plain grep of the stripped filing text misses phrases broken across lines** (error 1 above); any tool or run
   that searches `fetch.py` output for a multi-word phrase should normalise whitespace first.

## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- One line: **U.S. Physical Therapy owns the majority of about 780 outpatient clinic partnerships whose therapist-partners
  hold the physician referrals; every visit is paid at a rate the payor sets (36% of patient revenue on the Medicare fee
  schedule, cut in each year 2021-2025; the rest *"stipulated in the payor contracts"*), in a field the registrant calls
  *"highly competitive"* and *"highly fragmented"*. Net patient revenue per visit was $105.92 in 2010 and $105.76 in 2025
  while salaries per visit rose; operating margin fell from 15.7% to 11.1% and the pretax return on capital including
  goodwill from 21.1% (2013) to 9.6% (2025). [E3-03] criteria (2) and (3) fail on the filing, the demonstration clause
  fails on the price series, and [E4-23]'s surgeon is the business model. The best operator of the three SEC filers in
  its field, which is [E2-37]'s remarkable textile company.**
- **PASS/FAIL: FAIL at Q2 (OUT, ON THE BUSINESS).** Price **$84.84** (NYSE close 2026-09-25, aggregator, flagged) ×
  **14,922,698 shares** (10-Q cover for 2026-06-30, accession `0001140361-26-031825`) = cap **$1,266.0M**; sovereign
  **5.49%** (US Treasury 30-year par, 09/25/2026). USPH owner earnings after the partners' share: five-year FY2021-2025
  **$31.7-38.5M (2.50-3.04%)**, ten-year $34.7-38.9M (2.74-3.08%), eighteen-year $27.8-30.9M; after net partner buyouts
  $17.3-24.1M (five-year).
- **If UNRESEARCHED — THE WORK ORDER:** n/a.
- **If UNKNOWABLE:** n/a.

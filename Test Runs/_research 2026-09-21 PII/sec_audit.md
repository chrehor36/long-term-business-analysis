---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN, Q2 OUT. Q3, Q4 and Q6 carry
  material and the words "not written"; Q5's template block is replaced by the COMPUTATION —
  NOT A CLEARANCE heading, with no box, no ranking and no entry language (operator rule 3).
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's figures are
  off the filed FY2025 statements, Item 1 and Note 11.
- [x] Every UNRESEARCHED verdict names the artifact: **none issued.** The two limits met were
  named with their rung instead: Arctic Cat, Gator and Honda's ORVs sit inside conglomerate
  segments (not separable), and Kawasaki, Yamaha, Kubota, CFMOTO and Hisun do not file with the
  SEC (**exchange filings / EDINET, EDINET blocked by a paid key**); Indian's own cash result is not
  separately filed (**the filer's own segment disclosure**).
- [x] Every UNKNOWABLE verdict states what cannot be known: **none issued.** [E4-04]'s perimeter
  close was considered and refused in writing at Q2.
- [x] **Step 0: the filing was read, with accession numbers; two figures cross-checked by
  re-derivation** (FY2025 operating cash $741.0M from its own lines; total equity $832.9M from
  the equity statement's closing row). The Q2 2026 10-Q, both 2026 10-Qs' cash-flow statements,
  eleven earnings releases, five 8-Ks, the DEF 14A and three older 10-Ks were read for the
  material they are cited for.
- [x] **Owner earnings on a multi-year mean, every window published, both (c) ends and a judged
  (c) disclosed**; SBC off the filer's own line, checked against the note sums and the larger
  taken; no net-income proxy anywhere (PRIME RULE 3 as amended 2026-09-20).
- [x] **Competitor row filled** with the one comparable filer (BRP, two 40-Fs and a 6-K, accessions
  recorded), and every excluded competitor named with the reason. Not PROVISIONAL, and the reason is
  written at Q2.
- [x] **Sovereign for the earnings currency, from the issuing authority, dated**: 5.47%, US
  Treasury daily par yield curve, 30 Yr, 09/24/2026, raw file saved; FRED not used.
- [x] Value stated as a round-number range ($1bn to $7.5bn), inside the COMPUTATION only.
- [x] One bar only: none chosen, because Q5 did not open; windage count stated (ONE).
- [x] **Prices dated; the aggregator used for the live quote only and flagged** ($52.38, close
  2026-09-24, Yahoo chart endpoint, raw response saved).
- [x] **Every ledger id cited in this file resolves against `principle_ledger.csv`** (checked by
  script at the fold, zero phantoms), and `python tools/check_framework.py` PASS before the fold
  commit.
- [x] Run committed to git with pathspecs: `c9c1aa6` (Step 0, Q1, Q2) and the fold commit.

**ERRORS AND ARTIFACTS, recorded rather than smoothed.**
1. **My own error, caught before commit:** the working-capital sum for 2018 was first keyed as
   **$(141.2)M**; re-adding the six filed lines gives **$(142.2)M**. Fixed in `oe.py` with the
   correction noted; no owner-earnings figure depended on it (the line is displayed, not
   subtracted). The 2015 sum was likewise first written (155.5) in the table against the script's
   (155.6) and corrected to the script.
2. **My own error, caught before commit:** a first draft of the Q2 [E3-46] bullet described the
   2014-15 return only as *"16.0% operating margins ... on a consolidated asset base far smaller"*,
   which conceded nothing measurable. It was replaced, before this file was finished, by the
   unleveraged-net-tangible-asset series (68% / 42% / 42% / 13.6% / 6.1%), which is **the strongest
   evidence against the Q2 verdict** and belongs beside it in numbers.
3. **A first draft of Q3 said SBC was "6-12% of operating cash in normal years", then "9.2%"; the
   script gives 10.5% of cumulative operating cash.** Corrected before commit.
4. **A first draft attributed the words "particularly dependent upon future industry strength" to
   EY's critical audit matter; they are the MD&A's.** Corrected before commit.
5. **Tag-layer sign artifact:** the FY2023 10-K tags the 2022 TAP disposal proceeds ($42.2M) as a
   negative `PaymentsToAcquireBusinessesNetOfCashAcquired`, which the screen read as an acquisition
   inflow. Recorded at Step 0; not a tooling fix.
6. **The price response carries a null close for 2026-09-22**; that day is simply not quoted in
   the run.
7. **The prior session's claim file `_msg_claim.txt`** was left untouched and uncommitted in the
   research folder, as found.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- **One line: Q1 IN / Q2 OUT, on the business.** The North American off-road share leader
  competes on price and incentives in its own words, has lost twelve points of core-segment gross
  margin in eleven years (32.3% to 20.2%), and earned less than BRP on gross and operating margin
  in every year of five; at $52.38 (cap $2,981M) against a 5.47% sovereign the owner-earnings range
  runs from about $50M to $420M, too wide for a conclusion, recorded as arithmetic only.
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.

**STATUS: COMPLETE 2026-09-25 (resumed 2026-09-24).** Fold: register entry, strike, `_wave7_done.txt`,
narrative fold; no alert and no PORTFOLIO.md row (failed on the business, the QLYS ruling).

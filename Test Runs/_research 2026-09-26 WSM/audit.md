## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Step 0, Q1 IN, Q2 OUT; the file closed at Q2, and Q3-Q6 carry prompts beneath the close, no verdicts)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** (Q1 IN rests on the filed 10-Ks fiscal 2001-2025)
- [x] Every UNRESEARCHED verdict names the artifact and where it lives (none issued)
- [x] Every UNKNOWABLE verdict states what specifically cannot be known (none issued; why the perimeter close does not apply is argued at Q2)
- [x] Step 0: the filing was read, with accession number (10-K `0000719955-26-000059`, 10-Q `0000719955-26-000208`); a figure was cross-checked (fiscal 2025 operating cash 1,314,889, SBC 106,522, capex 259,438 and operating income 1,415,722 in the filed statements equal the tags)
- [x] Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment (every window 3-20 years, both ends, beneath the close)
- [x] Competitor row filled, or the moat marked PROVISIONAL and UNRESEARCHED (nine SEC filers; the private rivals named with the obstacle; the verdict stated not to rest on any one peer)
- [x] Sovereign is for the earnings currency, from the issuing authority, dated (USD 5.49%, US Treasury par curve, 09/25/2026)
- [x] Value stated as a round-number range, not a point estimate (beneath the close, headed COMPUTATION — NOT A CLEARANCE: about $40-95 at the floor, $70-175 at the sovereign)
- [x] One bar chosen, not both; windage count stated (no bar chosen, Q5 not opened; windage ONE in the computation)
- [x] Prices dated; aggregator used for live quotes only and flagged ($231.90, 2026-09-25, Yahoo chart endpoint)
- [x] Run committed to git (commits `7c62bf12` claim, `62a69065` Step 0 and Q1, `7f64b47b` Q2, `25d9e808` beneath the close, then this audit and the fold)
- **Ledger ids resolved by script** (`resolve_ids.py`): every id cited in this file is found in `principle_ledger.csv`. [E4-27] is cited for pay (not [E4-52], the lollapalooza row).
- **No net-income proxy anywhere** (operator rule 5; the PRIME RULE 3 clause): owner earnings are operating cash less SBC less (c) in every year and window.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- One line: **FAIL at Q2 (OUT, on the business).** A well-run designer-retailer of its own home furnishings whose own 10-K says it competes with retailers that *"market lines of merchandise similar to ours"* and *"discount retailers selling similar products at reduced prices"*, against *"increasingly competitive promotional activity"*, with a product re-won each season as *"style and color trends are constantly evolving"*; the same brands earned 8.4% of revenue over fiscal 1997-2019, in line with a row that includes two bankrupt home retailers, and 1.2% before tax in fiscal 2008; the post-2020 doubling was the row's wave, and the margin held since fiscal 2023 was held by giving up volume and share. A merchant, not a franchise.
- **Brief errors found (every brief has had one):**
  1. **"the screen says 18 years filed but its series is 9"**: the screen row's own `best_year_note` says *"9-yr OCF series"*, and the XBRL operating-cash tag does run in the tagged set with gaps (no annual value for fiscal 2014 and fiscal 2015 under the tag read); the filed cash-flow statements resolve every year fiscal 2006-2025 (twenty), and `years_filed` 18 is the XBRL span (FY2008-FY2025). Not an error so much as a count that needed its source named.
  2. **The screen's cap ($25,998M) is 4.8% below today's** ($27,313M); the brief said it was stale, and it is.
  3. **`deal_note` empty: confirmed**, not an error; the one Item 1.01 in the window is the June 2025 credit agreement.
  4. The brief's list of known run.py defects includes *"cover_shares may return the issued count including unvested restricted stock"*: **not so for WSM**; its cover states shares *"outstanding"*, equal to the balance-sheet count, and unvested awards are RSUs.
- **Tooling, reported, not patched:** `tools/run.py WSM` printed *"GROWTH THE PRICE ASSUMES -4.8% (at a 5.49% rate)"* (on its own three-year top of $1,141M against the $27,313M cap, the growth needed to reach 5.49% is about +1.3%; the sign or construction is wrong, a seventh run running after MATX, PPG, LNN, SYY, MLI and CMT) and *"POINTS OVER THE SOVEREIGN +1.28 .. +1.39"* on yields of 4.08-4.18% against 5.49% (the difference is −1.31 to −1.41; fourth run with this line wrong, after SYY, MLI and CMT); its three-year *"OE lo/hi"* takes the per-year minimum and maximum of the two (c) ends, mixing ends inside one window (fiscal 2023: lo $1,363M is the D&A end, hi $1,407M the capex end); it stops at five years on a twenty-year series. The screen's `level_note` and `level_note_oe` are cut short in the CSV (known). `cover_shares.py` returned the right count for this filer.
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.

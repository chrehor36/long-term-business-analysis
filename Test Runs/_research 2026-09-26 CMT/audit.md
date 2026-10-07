
---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Step 0, Q1 IN, Q2 OUT; the file closed at Q2, and Q3-Q6 carry prompts beneath the close, no verdicts)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** (Q1 IN rests on the filed 10-Ks; the PROVISIONAL mark sits on the Q2 competitor row, which is not an IN and on which the OUT is stated not to rest)
- [x] Every UNRESEARCHED verdict names the artifact and where it lives (none issued)
- [x] Every UNKNOWABLE verdict states what specifically cannot be known (none issued)
- [x] Step 0: the filing was read, with accession number (10-K `0001026655-26-000009`, 10-Q `0001026655-26-000053`); a figure was cross-checked (FY2025 operating cash 19,185, SBC 1,788, capex 17,268 and operating income 14,218 in the filed statements equal the tags)
- [x] Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment (every window 3-20 years, both ends, beneath the close)
- [x] Competitor row filled, or the moat marked PROVISIONAL and UNRESEARCHED (two SEC filers, the six named rivals not obtainable and named with the obstacle; the row marked PROVISIONAL and the verdict stated not to rest on it)
- [x] Sovereign is for the earnings currency, from the issuing authority, dated (USD 5.49%, US Treasury par curve, 09/25/2026; peso and Canadian-dollar costs stated)
- [x] Value stated as a round-number range, not a point estimate (beneath the close, headed COMPUTATION — NOT A CLEARANCE: about $6-18 at the floor, $11-33 at the sovereign)
- [x] One bar chosen, not both; windage count stated (no bar chosen, Q5 not opened; windage ONE in the computation)
- [x] Prices dated; aggregator used for live quotes only and flagged ($23.21, 2026-09-25, Yahoo chart endpoint)
- [x] Run committed to git (commits `25f29ef7` claim, `37f2438e` Step 0 and Q1, `7ad03eb0` Q2, `1ccb082b` beneath the close, then this audit and the fold)
- **Ledger ids resolved by script** (`resolve_ids.py`): the file cites 61 distinct ids before this section, every one found in `principle_ledger.csv`. [E4-27] is cited for pay (not [E4-52], the lollapalooza row).

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- One line: **FAIL at Q2 (OUT, on the business).** A contract moulder of truck, powersports and industrial parts whose own 10-K has said in the same words for twenty years that its OEM customers *"demand and receive price reductions ... through their use of competitive selection processes"* and that its *"end products are similar and are not unique"*; its founding customer's supply held only *"as long as the Company remains competitive in cost, quality, and delivery"*, Volvo's existing programmes moved to programmes it *"does not support"*, and its operating margin summed to 5.3% of sales over FY2004-FY2025. A supplier, not a franchise.
- **Brief errors found (every brief has had one):**
  1. **The `wc_note` inference is refuted.** *"ONE LINE MADE THE CASH: AccountsPayable moved 43% of 2021 OCF"*: the ratio is right ($5.3M of $12.5M) but the filed 2021 statement shows receivables (−$9.0M) and inventories (−$6.8M) outweighing payables, the working-capital lines together USING $5.9M, and operating cash below net income plus D&A plus SBC. The DELL/INOD shape does not apply to 2021.
  2. **`years_filed` 16 is the XBRL span**, not the filed history: the 10-Ks run to FY1996 on EDGAR and the owner-earnings series resolves from FY2006 (twenty years).
  3. **The screen's cap ($222M) is 8.1% above today's** ($205.4M); the brief said it was stale, and it is.
  4. The `deal_note` count is right for its window (one Item 1.01 since 2026-03-10, the July credit amendment); the brief's reading, *"most likely a credit facility"*, is confirmed. Not an error; recorded because the brief asked.
- **Tooling, reported, not patched:** `tools/run.py CMT` printed *"GROWTH THE PRICE ASSUMES -13.6% (at a 5.49% rate)"* (no simple reading of its own yields gives that figure; the sign or the construction is wrong, a sixth run running after MATX, PPG, LNN, SYY and MLI) and *"POINTS OVER THE SOVEREIGN +3.53 .. +5.33"* on yields of 6.23-7.95% against 5.49% (the difference is +0.74 to +2.46; third run with this line wrong, after SYY and MLI); its three-year *"OE lo/hi"* takes the per-year minimum and maximum of the two (c) ends, mixing ends inside one window; the D&A end carries acquired-intangible amortisation; it stops at five years on a twenty-year filer. The screen's `level_note` and `level_note_oe` are cut off mid-figure in the CSV (known). `cover_shares.py` returns the cover's "issued" count including unvested restricted stock without saying so; correct as the cover reads, but a reader must see the 285,735 to know the balance-sheet count differs.
- **Dated note on an earlier section, 2026-09-26, not edited (operator rule 6):** the Q2 table gives H1 2026 sales as $121.4M, the sum of the release's rounded production ($118.4M) and tooling ($3.0M) revenue; the 10-Q states $121,312,000. Immaterial to any verdict.
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.

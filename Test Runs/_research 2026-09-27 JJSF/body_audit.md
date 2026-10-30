---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN, Q2 OUT; Q3-Q6 not opened because the file closed at Q2, the hard sequence)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** (Q1 IN rests on the filed descriptions of FY2004 and FY2025)
- [x] Every UNRESEARCHED verdict names the artifact and where it lives (none used)
- [x] Every UNKNOWABLE verdict states what specifically cannot be known (none used)
- [x] Step 0: the filing was read, with accession number (10-K FY2025 `0001437749-25-036456`; 10-Q to 2026-06-27 `0001437749-26-026302`); operating cash, SBC and capex for FY2023-FY2025 cross-checked between the filed statement and companyfacts
- [x] Owner earnings on a multi-year mean; every window 1-23 years shown; capex band disclosed as a judgment (beneath the close, not governing); no net-income proxy
- [x] Competitor row filled (nine SEC filers; the like-for-like rivals are private and named); the class does not rest on the row, so not held PROVISIONAL (the IPAR and MEDP precedent)
- [x] Sovereign is for the earnings currency (USD; foreign sales 4.4%), from the issuing authority (US Treasury par curve, 30 Yr, 5.49%, 09/25/2026), dated
- [x] Value stated as a round-number range, not a point estimate (the computation beneath the close only: about $21-51 a share at the ~10% figure, no growth)
- [x] One bar chosen, not both; windage count stated: **not applicable, Q5 not opened**
- [x] Prices dated; aggregator used for live quotes only and flagged (Yahoo chart endpoint, close 2026-09-25)
- [x] Run committed to git (pathspec commits `b312f7d2`, `0b915814`, `e5c6d8ec`, and the commit carrying this audit)

**Ledger ids.** Every id cited in this file was opened in `principle_ledger.csv` and read before use (`ledger_ids.txt` lists them); the brief's labels were checked against the rows: [E4-52] lollapalooza, [E4-27] incentives, [E2-09] "(c) must be a guess", [E2-23] the equation, [E4-25] the range rule, [E4-01] Aesop, [E4-28] the quit point, [E3-03]/[E3-43]/[E2-44] the franchise tests, [E4-23] key person, [E4-26] disconfirming evidence, [E3-41] the easiest person to fool, [E4-44] the growth ceiling (the row's own words: *"my postulation of 5% growth in GDP"*): **all match.**

**Brief and screen errors found (each a prompt to read; none changed the verdict):**
1. **`cap_m` 1,668 is stale**: today's cap is $1,448.0M, 13.2% below the row (price $77.51 against about $86-89 implied; 812,000 fewer shares since FY2025 year-end after buybacks).
2. **`cap_flag` is a date mismatch, not a contradiction**: the filed float ($1,968.0M) was struck at $130.14 on 2025-03-28 and the screen's cap at a price about a third lower eighteen months later; both figures are right for their dates.
3. **`vs_sovereign` −0.0284 implies a 5.35% sovereign**; today's is 5.49% (the BR, NGVC, JKHY, CSCO, MEDP and IPAR finding again).
4. **`deal_note` is right** (the one Item 1.01 since the 10-K is Amendment No. 2 to the credit agreement), and blind to the 2022 Dippin' Dots deal, in which J & J was the buyer; no harm here.
5. **`wc_note` reproduces the share (34.9%) and reads the wrong way**: FY2021 working capital in total consumed $4.9M (receivables −$35.8M, inventories −$14.2M, prepaid +$9.6M, payables +$35.4M); one line did not make the cash.
6. `oe_bottom_m` 42 and `oe_top_m` 95 **reproduce** (five-year capex end $41.9M; three-year D&A end $95.2M); `acq_note` $228M **reproduces** ($221.3M plus $7.0M).
7. **`level_note_oe` is truncated** in the CSV and **mislabels FY2022's −$65.5M as "pre-window"**; FY2022 is inside the five-year window.
8. **`level_shift` "STEP UP - normalize down [E4-41]"**: the step is the post-pandemic and post-inflation recovery of margin plus a working-capital release in FY2023, not an exogenous windfall; the [E4-41] adjustment, where it applies, is the FY2023 release ($20.9M of receivables and inventories).
9. **`years_filed` 17 is XBRL depth** (FY2009-FY2025); this run read cash-flow statements for FY2003-FY2025 (23 years) and 10-Ks back to FY2003.
10. The brief's commit trailer (*"Claude Opus 5 (1M context)"*) differs from the environment's attribution line; the brief's was used, as the IPAR and MEDP runs did, and is recorded here.

**Tooling defects, reported not patched:** `working_capital_flag()` reports one line's share without the signs of the other working-capital lines (third run in a row); the screen's `level_note_oe` string is truncated in the CSV and calls an in-window year "pre-window"; `cap_flag` compares a cap and a float struck at different dates without stating either price; `tools/run.py` not run.

---
## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- One line: **J & J Snack Foods is a competent maker of frozen snacks and bakery goods with a good frozen-beverage route, selling mostly to professional buyers who choose on price: its largest line is priced by a contractual cost true-up and won by bid, a price rise under flat demand lost placements (FY2019), after-tax return on equity has not exceeded 14.4% in twenty-five years, and even the ICEE segment earns 11-15% pre-tax on its own assets; [E3-43]'s "a business", not a franchise. FAIL at Q2 (OUT, on the business) at $77.51 (2026-09-25) x 18,681,608 shares = $1,448.0M, against a 5.49% bond (09/25/2026). Owner earnings, every window 1-23 years at both (c) ends, $39.9-95.2M (2.76-6.57%); five-year $41.9-60.4M.**
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.

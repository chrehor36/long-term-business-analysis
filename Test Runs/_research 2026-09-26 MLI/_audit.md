## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. **Q1 IN, Q2 OUT**; the file closed at Q2; Q3 to Q6 recorded beneath the close without verdicts.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests on the filings named at Step 0.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives: none issued.
- [x] Every UNKNOWABLE verdict states what specifically cannot be known: none issued (the perimeter close was considered at Q2 and refused, with the reason stated).
- [x] Step 0: the filing was read, with accession number (10-K FY2025 `0000089439-26-000008`; 10-Q to 2026-06-27 `0000089439-26-000032`; the 8-Ks named); a figure was cross-checked (FY2025 OCF 755,444 = tag; SBC and operating income likewise).
- [x] Owner earnings on a multi-year mean (beneath the close); every window 3 to 20 years with both ends; the D&A end net of acquired-intangible amortisation; NCI share subtracted; SBC complete, the 401(k) match paid in cash; non-capital insurance and working capital shown as separate columns; the capex band disclosed as a judgment (not [E5-20]'s class; the two ends differ by under 3%); **no net-income proxy**.
- [x] Competitor row filled from three SEC filers (Wolverine Tube, Encore Wire, Global Brass & Copper), flagged as transcription, Mueller's checked to its filed statements; Cerro, Cambridge-Lee, Wieland Chase, NIBCO and Southwire named as unobtainable; the verdict stated not to rest on the row.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated (US Treasury, 30 Yr, 09/25/2026, 5.49%), struck fresh; the currency mix stated.
- [x] Value stated as a round-number range, not a point estimate: n/a at Q5 (not opened); the computation gives per-share ranges only.
- [x] One bar chosen, not both; windage count stated: n/a at Q5 (not opened); the computation's windage count is one.
- [x] Prices dated; aggregator used for live quotes only and flagged (Yahoo chart endpoint, close 2026-09-25).
- [x] Run committed to git with pathspecs (claim `7fd48dab`; Step 0 and Q1 `9b2f762a`; Q2 `915e6914`; beneath the close `482954e8`; this audit and the register in the next commit; the fold after).
- [x] **Every ledger id cited in this file resolved against `principle_ledger.csv`** by script (`resolve_ids.py` in the research folder) before the commit: 67 distinct ids, none missing.
- [x] **The strongest evidence against the verdict is recorded and answered** [E4-26] (at Q2): five years of 17-29% margins, the step held longer than Encore's, a three-mill market Mueller is consolidating, the price-over-volume policy, and [E3-47]'s warning.

**Priors from the brief, tested.** *"the screen row flags a pre-window straddle of zero and a step-up"*: both confirmed (FY2017 -$11.0M on the capex end after the NCI share; the step is 4.8 times on owner earnings, larger than the screen's 2.45 on operating income). *"Recent runs used #11 THE PASS-THROUGH"*: chosen on the evidence, with the reasons stated, and #14 and #3 considered. *"the screen cap predates the 2-for-1 split"*: immaterial either way, because a market cap does not change with a split; the 4.3% gap to Step 0 is the older price. **One brief figure did not hold**: *"the last entry was SYY at 179, so MLI should be 180"*. Counted from the file at fold, the register holds **189** entries before this one, because the backfill of 2026-09-26 (ten gate-clearers of 2026-08-31 and 2026-09-01, commit `d9dac534`) added ten after SYY was entered; **MLI is entry 190**.

**Tooling defects, reported, not patched.**
1. **`tools/run.py` printed *"GROWTH THE PRICE ASSUMES -6.7%"*** on a 4.47-4.57% yield against a 5.49% sovereign, where a price above the no-growth value must assume positive growth (about +0.9 to +1.0 points to match the bond): **the fifth run running** (MATX, PPG, LNN, SYY, MLI).
2. **`tools/run.py` printed *"POINTS OVER THE SOVEREIGN +1.69 .. +1.80"*** when its own yield two lines above is **below** the sovereign; the points are about **-0.9 to -1.0**. The second run running (SYY, MLI).
3. **Neither `tools/run.py` nor the screen subtracts non-controlling interests**: the screen's *oe_bottom* $547M is this file's five-year capex end plus the NCI share ($7.8M a year); `run.py`'s means likewise.
4. **The D&A end in `run.py` and the screen includes acquired-intangible amortisation** ($20.8M in FY2025, $13.2M a year on the three-year window; the screen's *oe_top* $612M is the three-year D&A end with it left in and NCI not subtracted). The open ruling of 2026-09-18.
5. **Neither tool sees non-capital insurance proceeds inside operating cash** ($15.5-18.9M a year in FY2024-FY2025, $32.4M in FY2013), so [E4-41]'s normalisation is never prompted.
6. **`run.py` stops at five years** on a filer with twenty years of expensed SBC, and the screen's *spread_caveat* says the same; the long windows here are about two-fifths of the five-year figure.
7. **The screen's `level_note_oe` field is cut off mid-figure in the CSV** (*"the pre-window years run from $-9.6M to $6"*); `Screens/floor_screen.py` (line 1421) builds a sentence that goes on to give the maximum, the mean and the ratio, and that text never reaches the reader. The cause was not traced.
8. `cover_shares.py` agreed with the cover read by hand (Step 0).

**Errors found in the earlier sections, recorded here and not edited (operator rule 6).** *Dated note, 2026-09-26, by the session that wrote the material beneath the close.*
- **Step 0** (the `level_shift` line) says operating income ran *"$126-270M a year in FY2008-FY2020"*, and **Q1** says *"$126-245M a year in FY2008-FY2020"*. **Both omit FY2009, $32.2M** (2.1% of sales), which Q2's own table carries. The low of the pre-step range is $32.2M, not $126M. The error understates how far the pre-step record fell in a bad year; it does not touch the Q2 verdict, which rests on criterion (2).
- **Q2** gives the 2012 Leucadia repurchase as *"$427.4M"*; the FY2014 10-K says *"at a total cost of $427.3 million"*. Immaterial; the source of the $427.4M figure was not traced.

## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- One line: **MLI FAIL at Q2 (OUT, on the business): a North American copper-tube, fittings and brass-rod maker that passes the metal through and keeps a spread its own 10-K says is set by "overall supply and demand in the market for our products and for our competitors' products" ([E3-03] criterion 2; a former rival called the same line "commodity-type"); its Piping Systems margin stepped from 6-10% (FY2008-FY2020) to 18.7-28.5% (FY2021-FY2025) after the named domestic tube rivals fell from five to two behind antidumping orders, while its Piping pounds fell about a fifth, which is [E3-43]'s tight supply, not a franchise. Price $60.52 (2026-09-25) x 221,181,388 (10-Q cover, post-split) = $13,385.9M; owner earnings $205-628M over every window 3-20 years and both ends (1.5-4.7%), below the 5.49% sovereign on every window; $94M a year before the step.**
- **If UNRESEARCHED — THE WORK ORDER:** n/a
- **If UNKNOWABLE:** n/a

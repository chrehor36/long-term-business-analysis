# AUDIT — Test Run of 2026-07-14 (SONY / TBTC / NTDOY)
Audited against: Workbook v3.0 sheet flow, Framework v3.0 gate rules, field amendments
P45–P47, and the Quick Reference. Every step checked one by one. Verdicts: ✓ FOLLOWED ·
◐ PARTIAL · ✗ VIOLATED (with correction applied below).

## A. Sequence and verdict discipline

| # | Rule (source) | Finding |
|---|---|---|
| A1 | "Complete each sheet in sequence. A FAIL at any gate — stop." (Workbook rules; Framework cover) | ✗ **VIOLATED for all three.** Gate 6 was run with Gates 1–5 incomplete: Sony Gate 1 was CONDITIONAL (not PASS) yet valuation proceeded; Nintendo Gate 3 was never evaluated at all; TBTC carried a **[U] on a mandatory inversion** into Gate 6 without the required written justification. |
| A2 | Verdict integrity: entry permissions only exist after gates pass | ✗ **TBTC "STARTER SIZE PERMITTED" is hereby RETRACTED.** The Statute *price test* passes, but no entry class of any size exists while Gates 1–5 are open. Correct status: price test passed, entry contingent. |
| A3 | "A company enters the watchlist only after completing all gates through Gate 8" (Appendix B) | ✗ Sony/NTDOY were labeled WATCHLIST. Mislabeled — correct label: **PIPELINE, GATES PENDING.** |
| A4 | Sheet 1 gate tracker / Sheet 10 registers maintained | ◐ Test-run doc serves as the record; no tracker sheets filled. Acceptable for a test, not for a real run. |

## B. Data discipline (primary sources only)

| # | Rule | Finding |
|---|---|---|
| B1 | All figures from primary filings; no aggregators | ✗/◐ Prices and market caps came from aggregators (Nintendo showed a $50.8B vs $56.3B discrepancy — ¥8.4T was chosen without resolving it); TBTC quote was June-dated; Sony capex was inferred from the ¥1.8T 3-yr budget, not the filing; Nintendo net cash ¥2.0T is an unverified estimate. Fundamentals (NI, D&A, OCF, capex) did come from filing-derived sources. ✓ after Addendum 2 for the OE inputs. |
| B2 | Gate 4: full OE formula [E2-08], never a proxy | ✗ in pass one (NI proxy) → **corrected in Addendum 2**. Residual gap: Sony prior-year FULL OE never computed (affects B4 and C3). |
| B3 | OCR/data anomalies flagged, not smoothed (Prime Rule 1 spirit) | ✓ Nintendo's suspect ¥289.8B FY3/26 D&A aggregator figure was distrusted; anchor year used the verified ¥12.07B. |
| B4 | **Range anchoring (P47): lowest VERIFIED OE tier** | NTDOY ✓ (anchored to FY3/25). Sony ◐ (FY3/26 continuing NI ¥1,031B < prior ¥1,067B, so lowest was used — but full-OE tiers for prior year unverified). **TBTC ✗ — 2024's $1.58M NI is the lowest verified tier, not 2025's $1.63M.** Corrected: Statute yield at strict anchor = 7.61% vs 7.10% — still PASSES; Statute price tightens $5.17 → **$4.80**. |

## C. Gate 6 mechanics (Sheet 7 / 7-B)

| # | Rule | Finding |
|---|---|---|
| C1 | Step 0 rate refresh; >50bp trigger | ✓ US 5.10%, JGB 3.93%; the +89bp JGB move was flagged and acted on. |
| C2 | Statute arithmetic: hurdles, premiums, 4% floor, Coca-Cola clause | ✓ +0 large caps, +2% micro (TBTC), floor not binding, clause not invoked. |
| C3 | **Base-scenario year-1 growth = LOWER of recent OE growth or guidance** | ✗ **VIOLATED for Sony** (recent NI growth −3.4%, base used +4%) and **strictly for TBTC** (OCF trend negative). NTDOY ✓ (4% < the 11.2% anchor-to-guidance path). **Corrected below.** |
| C4 | Three scenarios; 10yr explicit + moat fade + TV; TGR < WACC | ✓ all three, both passes. |
| C5 | Earnings-currency discounting, convert last | ✓ JPY DCFs at JGB anchor; USD conversion only at per-ADR step. |
| C6 | Step 6 sensitivity grid (WACC × TGR, majority must hold) | ✗ **SKIPPED for all three.** Partially mitigated by the two-rate Scream Test, but the grid is its own requirement. Open item. |
| C7 | Scream Test (P46) | ✓ run where Gate 6 was reached; whispers correctly identified. |
| C8 | MOS floors (20%/30%) | ✓ 20% applied (all classified narrow-or-better). |

## D. Gate 8

| # | Rule | Finding |
|---|---|---|
| D1 | Reverse DCF runs only after Gate 6 passes | ✓-by-consequence: no name passed Gate 6 for full size, so Gate 8 was legitimately not reached. (TBTC would have required it under the now-retracted starter verdict.) |

## E. Corrected numbers (strict rules applied)

Rule-compliant Base scenario (year-1 growth anchored at 0% where recent growth was
negative/ambiguous), full OE, mid-band:

| | Base IV/sh (band) | Current | Max buy (×0.80) | Statute price (strict anchor) | Status |
|---|---|---|---|---|---|
| **SONY** | **$17.77** (16.25–19.30) | $20.85 | **$14.22** | $34.30 | **GATES PENDING** — G1 conditional; G2 metrics, G3 proxy read, G5 not run. Price > IV regardless. |
| **TBTC** | **$5.21** | $4.48 | **$4.17** | **$4.80** | **GATES PENDING** — G5 [U] key-person unresolved; G3 proxy read; stale quote. Statute price test passes; NO entry permission yet. |
| **NTDOY** | **$7.43** (7.06–7.81) | $10.97 | **$5.94** | $7.88 | **GATES PENDING + Statute FAIL on anchor.** G3/G5 never run. Both triggers below market. |

## F. Audit summary

5 violations (A1 sequence, A2 verdict, A3 watchlist label, B4 TBTC anchor, C3 growth
anchor ×2 names), 4 partials, 11 rules followed. The two numeric violations moved
prices: Sony max-buy $16.78 → **$14.22**; TBTC max-buy $4.39 → **$4.17** and Statute
$5.17 → **$4.80**. No violation moved a verdict in the permissive direction once
corrected — every correction tightened.

**The meta-lesson is [E1-02] itself:** "I believe in establishing yardsticks prior to
the act; retrospectively, almost anything can be made to look good..." The framework's
pre-committed rules caught the analyst (me) relaxing them under momentum — sequence
first, then data, then growth anchors. This audit is the Scream Test applied to the
process instead of the price.

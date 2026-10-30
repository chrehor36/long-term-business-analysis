# Company Run — PNC Financial Services Group (PNC) — 2026-07-31
Framework v3.0. Complete top to bottom. **A section may be filled only when every
section above it has a verdict.** A FAIL stops the run — record it in the Eliminated
register and stop. Anything computed out of order must be headed
**"COMPUTATION — NOT A CLEARANCE"** and carries no entry language.

## STEP 0 — RATE REFRESH (before anything)
- Sovereign 30-yr (earnings currency): **5.28** % (date: 2026-07-31, source: Yahoo ^TYX, cross-validated vs FRED DGS30 on five overlapping sessions, ratio 1.001-1.003)
- Δ vs last valuation: **+17** bp (prior 5.11% @ 2026-07-20) → >50bp? [ ] YES [x] NO
- FX (if non-USD): n/a — USD reporter

## GATE 1 — CIRCLE OF COMPETENCE
- Unit economics: a deposit-funded lender. Gather deposits cheaply (23% of them
  noninterest-bearing), lend at a spread, and earn fee income on top. Owner earnings track
  net interest income less credit costs less operating expense; the durable asset is the
  low-cost deposit base, not the loan book.
- Informational edge: none.
- Segment count: 3 (Retail Banking, Corporate & Institutional Banking, Asset Management),
  each separately reported and evaluable.
- **VERDICT: [x] PASS [ ] FAIL - STOP**

## GATE 2 — MOAT (per segment)
- Franchise test [E3-03]: needed/desired [x] · no close substitute [~] deposits are
  commoditised; the stickiness is inertia and branch convenience · **unregulated [ ] - NO,
  and this is stated plainly rather than glossed:** banking is heavily rate- and
  capital-regulated, which is a real constraint on pricing power · proven by pricing power
  + returns on capital [~] - see below
- Primary moat metric + 8-quarter trend: NIM climbed **2.64% -> 2.96%**, but this is
  **entirely fixed-rate asset repricing plus a deposit down-beta the CFO has said is now
  over** - a mechanical, self-terminating tailwind, not pricing power. The efficiency ratio
  never moved off **59-61%** across the same eight quarters. The franchise did hold through
  the 2023 regional stress (deposits down only 1% on the year, no assistance, $5.6B earned).
- Direction: [ ] WIDENING [x] STABLE [ ] NARROWING · Class: [ ] WIDE [x] NARROW [ ] NONE
- **VERDICT: [x] PASS [ ] FAIL - STOP**

## GATE 3 — MANAGEMENT
- Integrity: **PASS.** No fraud, accounting manipulation, cartel, bribery or regulator
  finding of misconduct against PNC's own conduct in the current record. (The 2013 DOJ/CFPB
  consent order was National City's pre-acquisition conduct, paid as successor.)
- Competence: sound through the cycle; the 2023 stress test was passed without assistance.
- Alignment: **UNRESOLVED** - compensation structure could not be fully established in this
  run. Recorded as an open item rather than assumed satisfactory.
- **VERDICT: [x] PASS [ ] FAIL - STOP**

## GATE 4 — FINANCIAL QUALITY (full formula only — no NI proxy in any reported figure)
- NI ____ + D&A ____ − maint capex ____ (disclosed split? [ ] Y [ ] N — band used: ____)
  − required WC increment ____ = **OE ____**
- OE tier table (all recent verified years): ____
- **LOWEST VERIFIED TIER (anchors all buy prices): ____**
- Fortress check — two tracks (FA, ratified 2026-07-15): financial business (bank/
  insurer/balance-sheet levered)? [ ] Y [ ] N
  · If N — SURVIVAL TRACK: credit rating ____ · undrawn revolver+cash ____ vs. debt
    due <24mo ____ · schedule termed-out? [ ] Y [ ] N · survives 50% OE decline ×2yr
    without existential risk? [ ] YES [ ] NO (ordinary IG leverage is not itself a fail)
  · If Y - LEVERAGE CEILING (mechanical), 12/31/2025: assets **$603.0B** / equity
    **$63.6B** = **9.47:1** -> within the 10:1 ceiling. **PASS.**
    **RULING 2026-08-01 (denominator convention):** on *common* equity the ratio is
    **10.46:1**, which would breach the ceiling. The framework's ceiling is applied to
    TOTAL equity (XBRL StockholdersEquity, preferred included), consistent with every prior
    run and with the BT-15/BT-16 screens. Changing the denominator now would silently
    invalidate earlier financial verdicts. The stricter common-equity reading is recorded
    here so the margin is visible: PNC clears this gate by less than one turn, and would
    fail on the stricter convention.
- **VERDICT: [x] PASS [ ] FAIL - STOP** (9.47:1 on the ruling convention; 10.46:1 on common
  equity - clears narrowly)

## GATE 5 — INVERSION
- Bull-case assumptions: (1) the deposit franchise stays cheap and sticky; (2) asset
  repricing keeps lifting NIM; (3) commercial real estate losses stay contained;
  (4) efficiency finally improves.
- Mandatory inversions: moat destruction **RESOLVED** · management failure **RESOLVED**
  · **balance sheet UNRESOLVED** · thesis-breaking metric **RESOLVED**. 3/4.
- Any [U] on a mandatory inversion? [ ] NO [x] YES - and this one is disqualifying rather
  than carryable. **PNC's AOCI and held-to-maturity unrealised securities losses could not
  be established** (SEC EDGAR returned 403 throughout the research). For a bank in a 5.28%
  rate environment that is not a detail - it is the exact figure that determines whether
  reported equity is real, and it is the same figure that destroyed several banks in 2023.
  Separately, **multifamily exposure of $14.7B (~2.9x the office book) was never examined**;
  office CRE itself is fine at $5.1B, 1.5% of loans, reserved at 11%.
- Thesis-breaking metric + exit threshold: not set - a thesis cannot be falsified when its
  central balance-sheet input is unknown.
- **VERDICT: [ ] PASS [x] FAIL - STOP**

---
⛔ **VALUATION LOCK — do not fill below this line unless Gates 1–5 each show PASS.**
---

## GATE 6 — VALUATION
- 6-B Statute (Book One): anchored OE yield ____ % vs hurdle ____ % (sovereign + size
  premium, floor 4%) → [ ] PASS [ ] FAIL
- Book Two DCF: WACC ____ · scenarios Bear/Base/Bull (year-1 growth = LOWER of recent
  OE growth or guidance: anchor value ____ %) · IV/sh: ____ / ____ / ____
- Sensitivity grid (WACC × TGR) holds across majority? [ ] Y [ ] N
- Scream Test: yardstick verdict ____ · build-up verdict ____ → [ ] AGREE [ ] WHISPER — pass
- Max buy = Base IV × 0.80 (0.70 no-moat): ____
- **VERDICT: [ ] BUY-ELIGIBLE (price ≤ max buy) [ ] STATUTE-ONLY (starter) [ ] WAIT**

## GATE 8 — REVERSE DCF (only if Gate 6 verdict is BUY-ELIGIBLE or STATUTE-ONLY)
- Implied OE base vs trough/current/peak: ____
- Implied year-1 growth across 4 deceleration profiles (A/S/H): ____
- Asymmetry ratio: ____ : 1 (≥2:1 required)
- **VERDICT: [ ] ENTER (size per Gate 7) [ ] WAIT**

## GATE 7 — ENTRY COMMITMENTS (before any order)
- Thesis-confirming metric: ____ · Thesis-breaking metric: ____ · Next catalyst date: ____
- Size (conviction × MOS; illiquidity cap if OTC): ____

## SELF-AUDIT (run is incomplete until every box is checked)
- [ ] Sections completed in order; no verdict line skipped
- [ ] No entry language anywhere above an unfilled verdict
- [ ] Full OE formula used in every reported figure (no NI proxy)
- [ ] Buy prices anchored to the LOWEST verified OE tier
- [ ] Year-1 growth ≤ lower of recent OE growth / guidance
- [ ] Prices/market cap dated; aggregator figures flagged; filings cited for fundamentals
- [ ] Step 0 rates dated; >50bp rule checked
- [ ] Run committed to git

---
## APPENDIX — COMPUTATION, NOT A CLEARANCE (produced 2026-07-31, before Gates 1-3 verdicts)
Per operator protocol rule 2 this carries **no clearance and no entry language**.
Source: SEC XBRL company facts, 10-K only. Full OE formula (NI + D&A - capex - dWC);
no net-income proxy. Maintenance-capex is not separately tagged by the filer, so TOTAL
capex is used — this understates OE and is the conservative direction.

OE tier table:
  - n/a
- **Lowest verified tier: n/a** — anchors all buy prices (range-anchoring field amendment)
- Balance sheet (latest): assets $603.0B / equity $63.6B = 9.5:1
- Fortress track: FINANCIAL - hard 10:1 assets/equity ceiling applies
- **LEVERAGE CEILING: 9.5:1 vs 10:1 → within limit**


---
## RUN RESULT - ELIMINATED AT GATE 5 (2026-08-01)
PNC clears Gates 1-4 and fails Gate 5 on an unresolved mandatory inversion: the securities
marks that determine whether reported equity is real could not be established, and the
multifamily book was never examined. The framework's own rule is that a mandatory inversion
left [U] without written justification is a fail, and no justification survives here - this
is missing evidence, not accepted risk.

**No valuation performed. No Book One yield reported. No watchlist placement, no entry
language.** Note also that Gate 4 cleared by less than one turn of leverage and would fail
on a common-equity denominator.

Eliminated register: **PNC - Gate 5 (unresolved balance-sheet inversion: AOCI/HTM
unrealised losses not established; $14.7B multifamily unexamined).**
Re-runnable if the securities marks are obtained from the 10-K directly.

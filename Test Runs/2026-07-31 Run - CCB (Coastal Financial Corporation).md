# Company Run — Coastal Financial Corporation (CCB) — 2026-07-31
Framework v3.0. Complete top to bottom. **A section may be filled only when every
section above it has a verdict.** A FAIL stops the run — record it in the Eliminated
register and stop. Anything computed out of order must be headed
**"COMPUTATION — NOT A CLEARANCE"** and carries no entry language.

## STEP 0 — RATE REFRESH (before anything)
- Sovereign 30-yr (earnings currency): **5.28** % (date: 2026-07-31, source: Yahoo ^TYX, cross-validated vs FRED DGS30 on five overlapping sessions, ratio 1.001-1.003)
- Δ vs last valuation: **+17** bp (prior 5.11% @ 2026-07-20) → >50bp? [ ] YES [x] NO
- FX (if non-USD): n/a — USD reporter

## GATE 1 — CIRCLE OF COMPETENCE
- Unit economics in my own words (no management language): Two businesses. (1) An
  ordinary Everett, WA community bank. (2) CCBX — Coastal rents its bank charter to
  fintech partners. Coastal originates subprime consumer paper on its own balance sheet
  (~14.56% yields, 8.73% annualised charge-offs excluding the troubled partner) and books
  an offsetting **credit enhancement asset** representing the fintech's contractual
  indemnity, leaving ~98.8% of credit "covered" on paper. So the real exposure is NOT
  borrower credit — it is **unsecured counterparty risk to thinly capitalised private
  fintechs**. Coastal writes the credit insurance and buys its reinsurance from a startup.
  Headline NIM of 7.27% is ~**3.98%** net of BaaS loan expense.
- Informational edge: **None available.** Partners are not named, their balance sheets are
  not disclosed, and partner-level concentration is only partially given.
- Segment count: 2 (community bank + CCBX). CCBX is **not** independently evaluable.
- **VERDICT: [ ] PASS [x] FAIL — STOP** (CONDITIONAL = not a pass; stop or resolve)

**Reason for failure — knowability, not complexity.** The model is explainable in a
paragraph; what cannot be done is *verifying* it from outside. Q2 2026 (reported
2026-07-30, two days before this run) turned a +$12.0M quarter into a **−$42.1M net loss,
$(2.76)/sh**, on **$68.8M of credit expense from a single CCBX partner**, including a
**$46.0M write-down of the credit enhancement asset** because the amounts are "not
expected to be fully recovered under the partner's indemnification." That single partner
held **$530.3M — 24% of the CCBX book**. A ~$54M swing, roughly 15% of equity, in one
quarter, with no external warning available to an outside owner. Management calls it
isolated; confirming that requires precisely the partner financials that are not
disclosed. An investment whose central risk cannot be monitored from public filings is
outside the circle of competence by definition.

## GATE 2 — MOAT — NOT REACHED (run stopped at Gate 1)
- Franchise test [E3-03]: needed/desired [ ] · no close substitute [ ] · unregulated [ ]
  · proven by pricing power + returns on capital [ ]
- Primary moat metric + 8-quarter trend (filing-sourced): ____
- Direction: [ ] WIDENING [ ] STABLE [ ] NARROWING · Class: [ ] WIDE [ ] NARROW [ ] NONE
- **VERDICT: [ ] PASS [ ] FAIL — STOP**

## GATE 3 — NOT REACHED (recorded for the register only)
- Integrity (recorded, not a verdict): **clean** — no consent order and no BSA/AML action,
  which is genuinely rare among sponsor/BaaS banks. CEO pay restrained at $1.69M.
- Competence (recorded): fails on concentration control — 24% of the CCBX book in one
  undisclosed counterparty.
- Competence (returns on capital; OM-9 retention test; buybacks per [E5-01]): ____
- Alignment (proxy statement read — comp structure, ownership): ____
- **VERDICT: [ ] PASS [ ] FAIL — STOP** (integrity fail is permanent)

## GATE 4 — NOT REACHED — but note it would ALSO have failed mechanically
Assets/equity at Q2 2026 = $5.46B / $463.4M = **11.78:1** against the ratified hard
**10:1** ceiling for financial businesses (Ruling 2) — an automatic FAIL, no exception.
It was 9.65:1 at Q4 2025, so the ceiling was breached in two quarters while Tier 1
leverage fell 151bp to 9.11%. (This run's own XBRL pull, one quarter staler, gave
11.2:1 — same conclusion.) Two independent gates therefore reject CCB.

## (template Gate 4 fields, unused)
- NI ____ + D&A ____ − maint capex ____ (disclosed split? [ ] Y [ ] N — band used: ____)
  − required WC increment ____ = **OE ____**
- OE tier table (all recent verified years): ____
- **LOWEST VERIFIED TIER (anchors all buy prices): ____**
- Fortress check — two tracks (FA, ratified 2026-07-15): financial business (bank/
  insurer/balance-sheet levered)? [ ] Y [ ] N
  · If N — SURVIVAL TRACK: credit rating ____ · undrawn revolver+cash ____ vs. debt
    due <24mo ____ · schedule termed-out? [ ] Y [ ] N · survives 50% OE decline ×2yr
    without existential risk? [ ] YES [ ] NO (ordinary IG leverage is not itself a fail)
  · If Y — LEVERAGE CEILING (mechanical): assets ____ ÷ equity ____ = ____:1 →
    >10:1 = AUTOMATIC FAIL, no exception
- **VERDICT: [ ] PASS [ ] FAIL — STOP**

## GATE 5 — INVERSION
- Bull-case assumptions listed: ____
- Mandatory inversions scored (moat destruction / management failure / balance sheet /
  thesis-breaking metric): [D/DS/P/U] ____ ____ ____ ____
- Any [U] on a mandatory inversion? [ ] NO [ ] YES — written justification: ____
- Thesis-breaking metric + exit threshold (pre-committed [E1-02]): ____
- **VERDICT: [ ] PASS [ ] FAIL — STOP**

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
  - FY 2020-12-31: $11M
  - FY 2021-12-31: $26M
  - FY 2022-12-31: $40M
  - FY 2023-12-31: $41M
  - FY 2024-12-31: $40M
  - FY 2025-12-31: $45M
- **Lowest verified tier: $11M** — anchors all buy prices (range-anchoring field amendment)
- Balance sheet (latest): assets $5.7B / equity $0.5B = 11.2:1
- Fortress track: FINANCIAL - hard 10:1 assets/equity ceiling applies
- **LEVERAGE CEILING: 11.2:1 vs 10:1 → AUTOMATIC FAIL, no exception**


---
## RUN RESULT — ELIMINATED AT GATE 1 (2026-08-01)
**No valuation performed. No Book One yield, no watchlist placement, no entry language.**
Gates 2, 4 and 5 were not worked as verdicts; the Gate 4 leverage figure is recorded above
only because it is mechanical and independently disqualifying.

Eliminated register: **CCB — Coastal Financial Corporation — Gate 1 (circle of
competence: BaaS counterparty risk not verifiable from public disclosure). Gate 4 would
also fail on the 10:1 leverage ceiling (11.78:1).**

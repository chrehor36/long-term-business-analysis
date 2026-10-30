# OTCQX Mechanical Screen — 2026-07-15
**This is a screen, explicitly not framework output.** Per the Framework's own
identity ("This framework is not... a stock screening tool"), nothing here is a
gate verdict. It exists only to shrink 157 companies down to a list worth spending
real gate-by-gate effort on.

## Source
User-exported list from the OTC Markets screener: `Stock_Screener.csv` — 157
companies, pre-filtered to Tier=OTCQX, Country=USA, Sec Type=Common Stock. This
solved a real access problem: OTC Markets' live site returns a bot-detection decoy
page to any scripted request, and third-party aggregators mix in thousands of
foreign ADRs with no tier/country field — the user's own export was the only clean
path to this list.

## Method
For each ticker: fetched market cap and 5-year Net Income history from
stockanalysis.com (server-rendered pages, no JS execution needed). Computed a
**bare Statute yield check only** — NI (lowest of the last 5 fiscal years, as a
rough OE proxy, NOT the full owner-earnings formula) ÷ market cap, vs. the US
30-yr hurdle (5.10%, +2% for market caps under $300M as a micro-cap proxy for
"illiquid"). This is Gate 6 arithmetic run in isolation, with none of Gates 1–5
attempted — a deliberate simplification appropriate only for triage.

144/157 tickers resolved cleanly; 13 had no coverage on the data source used
(MNAT, ETCG, WRIV, ZCSH, BCHG, LTCN, GXLM, HZEN, BKFL, MDNC, CMSG, OBNK, GTAO) —
not evaluated, not failed; genuinely unknown from this pass.

## Result: 34 of 157 clear the bare yield check
Full ranked list: `2026-07-15 OTCQX Mechanical Screen - full results.csv`.

**Composition is the important finding, not the count.** Manual review of the 34
survivors (the automated bank-keyword filter under-matched):

- **31 are bank or thrift holding companies** (e.g., Alpine Banks of Colorado,
  Somerset Trust, Uwharrie Capital, First National Bank Alaska, CBB Bancorp,
  Dacotah Banks). This is not a coincidence: small community/thrift banks are
  exactly the kind of business that lists on OTCQX rather than Nasdaq (no need
  for the visibility, family/community ownership, cost-conscious), and bank
  stocks in this segment chronically trade at single-digit P/E — which is what a
  NI-based yield screen is mechanically going to surface.
- **3 are non-financial: Unit Corp** (oil & gas E&P), **Table Trac** (gaming
  technology — already has a full Framework v3.0 run on file, 2026-07-14 test
  run + 2026-07-14 full-OE addendum, verdict WAIT), and **Gamco Investors**
  (asset manager — judgment call on financial classification, see below).

## Why this blocks a naive "run the template on all 34"
Ruling 2 (the Fortress Test) requires financial businesses to clear a **hard
10:1 assets/equity leverage ceiling** before Gate 4 can pass — this screen did not
check that (it has no balance-sheet data, only NI and market cap). Separately,
the **owner-earnings formula itself doesn't fit a depository institution**: banks
don't have "maintenance capex" in the industrial sense; net income net of loan-loss
provisioning is closer to the real economic earnings already, but the moat test
(Gate 2's franchise test), the fortress test, and even what counts as the
"business" being evaluated all need bank-specific handling that the standard
template (built and tested on Visa/Chubb/Sherwin-Williams/S&P Global) does not
yet encode explicitly.

Gamco Investors is the edge case worth naming: an asset manager is
balance-sheet-light and fee-based, arguably closer to Visa's toll-model than to a
bank's — whether it needs the leverage-ceiling track or the ordinary survival
track is itself a judgment call, not a mechanical one.

**Recommendation, pending user direction:** build a bank-specific Gate 4/6
adaptation (leverage ceiling first, then P/B + ROE + NIM + credit-quality in place
of the OE formula) before running the 31 bank names — rather than force-fit the
industrial template and produce a technically-complete but methodologically wrong
result. Unit Corp and Gamco can proceed under the existing template as-is.

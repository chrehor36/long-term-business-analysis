# BACKTEST PLAN — The Statute, Point-in-Time, 2010–2024 — v0.1 (design)
2026-07-17. The next study project (user-chosen): test the framework's
mechanical layer against history with real, free, honest data. This
extends the 24-episode qualitative backtests (2026-07-14/15) with a
systematic, quantitative one.

## Questions, in test order
1. **B1**: Does buying Book One passes (worst-5yr E/P ≥ 30yr Treasury
   + size premium) beat SPY on 1-year holds, 2010–2024?
2. **B2**: Does the 2×AAA Graham bar (stricter) beat the Statute bar?
3. **B3**: Does the whisper filter add value — i.e., do Book One passes
   that ALSO clear a conventionalized Book Two (g1=2%, moat-blind NARROW
   spread) beat Book One passes that don't?
4. **B4**: Sell rules — +50%-or-2-years vs simple 1-year rebalance vs
   buy-and-hold of passes.

## Data layer (all free, no keys)
- **Fundamentals, point-in-time**: SEC XBRL companyfacts — every fact
  carries its `filed` date, so a screen "as of June 30 of year t" uses
  only facts filed before that date. **This kills look-ahead bias
  properly** — most home backtests fail here; ours won't. Coverage:
  reliable from ~2010 (XBRL mandate phase-in) — hence the window.
- **Prices**: stooq.com free daily CSVs (long history, no auth);
  dividends handling = use adjusted closes where available, flag where
  not (total-return approximation is a known limitation, documented).
- **Yields**: FRED CSV endpoints — DGS30 (30yr Treasury), AAA (Moody's
  Aaa). Historical hurdles computed per rebalance date, floored at 4%
  per the Statute.
- **Universe & the survivorship problem (the honest flaw)**: free
  point-in-time index membership doesn't exist. Mitigations, in order:
  (a) universe = all CIKs with XBRL data at each date (not just today's
  survivors) — XBRL includes delisted/acquired companies' historical
  filings, which substantially de-biases the screen side; (b) price
  data for dead tickers is the remaining gap (stooq keeps some, not
  all) — every name that passes a screen but lacks price history gets
  LOGGED as a coverage failure, not silently dropped, and the results
  carry a stated survivorship-residual caveat. No pretending.

## Build phases (multi-session; each commits separately)
- **BT-0**: data-layer fetchers (FRED, stooq, XBRL point-in-time
  extractor with `filed`-date cutoffs) + cache directory (gitignored).
  **✅ DONE 2026-07-22** — stooq turned out to be JS-walled/unusable;
  substituted Yahoo Finance chart API (adjusted close, better than stooq's
  plain close for this purpose). Scripts in `scripts/`.
- **BT-1**: single-year proof (screen as of 2015-06-30, hold 1yr,
  measure) — validates the pipeline end to end before scaling.
  **✅ DONE 2026-07-22**, folded into the BT-2 run below.
- **BT-2**: full annual loop, B1 (36-name universe, 2013-2025, not the
  original 2010-2024 window — XBRL coverage for several names starts
  later). **✅ DONE 2026-07-22** — see
  `2026-07-22 BT-0-1-2 Results - The Statute, Point-in-Time, 2013-2025.md`.
  Headline: Book One alone does NOT show a robust edge (49.3% win rate vs
  SPY, negative median excess return) and the pass-list is concentrated in
  14 of 36 names, dominated by CMCSA/TSCO/VZ/ELV — a value-trap-leaning
  pattern, not a diversified "wonderful business" signal. **This is the
  first hard evidence that Gates 2-5 are load-bearing, not just caution.**
  B2 (Graham's 2×AAA bar) not yet run this pass.
- **BT-3**: B3 (dual-book/whisper filter) and B4 (sell rules). **OPEN.**
- **BT-4**: write-up with every limitation stated; feed anything that
  contradicts the framework back into PENDING RULINGS for user decision
  (the text wins — including when the text is a backtest). **Partially
  open** — the BT-2 finding (bare Statute ≈ coin-flip, concentrated in
  value-trap sectors) is exactly the kind of contradiction this rule
  exists for; recorded here and in the results doc, not yet escalated to
  PENDING RULINGS since B3 (does the whisper filter fix it?) hasn't been
  tested yet — escalate only if B3 fails to resolve it.

## Standing rules
Same discipline as everything else: no smoothing, coverage failures
logged, look-ahead handled via filed-dates, results are STUDY output —
they change rulings only through the user, never silently.

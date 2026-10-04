# BACKTEST BT-5 — The Largest Test: Systematic Berkshire 13F History + Multiple Screen Portfolios — 2026-07-22
Direct follow-up to the "7 famous picks" test, which was explicitly flagged as
cherry-picked. This pass does two things the user asked for: (1) tests
Berkshire's **entire disclosed equity portfolio, every year, 1998-2025** —
not the 7 names everyone already knows worked — and (2) builds **several
different small portfolios from our own framework's mechanical screen data**
to see how real buy-and-hold compounding actually behaves, not just 1-year
rolling returns.

## PART 1 — SYSTEMATIC BERKSHIRE 13F TEST (1998-2025, 28 years)

### Method
- Pulled **every year-end 13F-HR filing** Berkshire Hathaway has ever filed
  with the SEC (CIK 0001067983), 1998 through 2025 — 28 consecutive annual
  snapshots, not a selected subset.
- **Pre-2013 filings** (15 years) are legacy fixed-width text tables with no
  two years formatted quite the same way (different filing agents, different
  column wording). Built a parser for this era and **validated every single
  year's parsed total against that filing's own stated total — all 15 years
  match exactly, dollar for dollar.** That's a genuine correctness proof, not
  an assumption.
- **2013-2025 filings** (13 years) use the SEC's mandatory structured XML
  info-table format — parsed directly and trusted.
- **Unit change caught and corrected**: the SEC's 2023 rule change requires
  13F values in whole dollars starting with the 2022 year-end filing;
  everything before that is in thousands. Confirmed by cross-checking
  against known real Berkshire portfolio sizes at each point (e.g., 2021
  ≈$331B, 2022 ≈$299B — both directionally sensible only under this
  correction).
- **Ticker resolution**: issuer names in 13F filings are free text, not
  tickers. Built a name-matching table for every name that ever appeared in
  a top-10 holding across all 28 years (~55 distinct issuers). Four
  positions were deliberately excluded rather than force-mapped: **Wesco
  Financial** (Berkshire's own majority-owned subsidiary, not a third-party
  pick), **American Standard** (2007-08 three-way breakup, too complex for
  this pass), **Anheuser-Busch** (acquired by InBev 2008, delisted), and
  **PS Group Holdings** (too small/obscure to reliably resolve). These are
  logged, not silently dropped.
- **Portfolio construction**: each year-end, take the top 5 or top 10
  holdings by disclosed value, hold for exactly one year (to the next
  year-end snapshot), reconstitute — both equal-weighted and value-weighted
  versions. This directly mirrors what a systematic "buy what Berkshire
  actually discloses owning" strategy would have done.

### Result — a genuinely humbling comparison

| Portfolio | CAGR (1999-2025) | Total multiple |
|---|---|---|
| Top 10, equal-weighted | 9.04% | 10.4x |
| Top 10, value-weighted | 7.75% | 7.5x |
| Top 5, equal-weighted | 8.14% | 8.3x |
| Top 5, value-weighted | 7.58% | 7.2x |
| **SPY, same window** | **8.34%** | **8.7x** |
| **Berkshire's own stock (BRK.A), same window** | **9.33%** | **11.1x** |

**None of the four systematic constructions clearly beats Berkshire's own
stock.** The best of them (top-10 equal-weight, 9.04%) sits just under
BRK.A's actual 9.33%, and the value-weighted versions (which overweight
whatever was the single largest position that year — Coca-Cola for over a
decade, then Apple from 2018 on) trail even SPY. **Equal-weighting clearly
beats value-weighting here** — concentrating in the single biggest disclosed
position, year after year, added risk without added return.

This is a completely different picture from the 7-name cherry-picked test
(14.66%, which beat both benchmarks). That's the point of running it: **the
famous picks that get talked about are, definitionally, survivors — the
full disclosed portfolio, taken systematically, looks much more like "roughly
matches the market, doesn't clearly beat Berkshire's own operating engine."**
Berkshire's real edge shows up in capital allocation, insurance float,
wholly-owned businesses, and timing that a passive annual-reconstitution
simulation of the 13F alone cannot capture.

## PART 2 — MULTIPLE SMALL PORTFOLIOS FROM THE FRAMEWORK'S OWN SCREEN
Built 6 different portfolio constructions from the 142-name combined
mechanical-screen universe (BT-2/wider-universe backtests), this time as
**real buy-and-hold-to-today** positions (bought at each name's first
Statute pass, held continuously through 2026-07-22) rather than 1-year
rolling returns — a much more direct test of "does this actually compound
over the long run."

| Portfolio | n | Mean CAGR | Matched-SPY CAGR (same entry dates) |
|---|---|---|---|
| **A. HIGH persistence** (passed Statute ≥8 of 13 yrs — CMCSA, TSCO, BKNG, GIS, INTC, CSX, EXC) | 7 | **9.12%** | 14.21% |
| **A. MED persistence** (passed 3-7 of 13 yrs, 34 names) | 34 | 10.88% | 14.99% |
| **A. LOW persistence** (passed only 1-2 of 13 yrs, 29 names) | 29 | **15.24%** | 15.72% |
| B. Top 10 cheapest at first pass (highest yield) | 10 | 14.41% | 15.39% |
| B. Top 20 cheapest at first pass | 20 | 12.80% | 15.05% |
| C. Earliest-discovered 10 (2013-14 vintage) | 10 | 8.28% | 13.66% |
| **All 70 names that ever passed, equal weight** | 70 | 12.51% | 15.21% |

### The honest, unflattering headline
**Every single construction underperformed a simple "buy SPY on that same
entry date" comparison.** This is a real, structural finding, not a rounding
error: 2013-2025 was an extraordinary bull market driven overwhelmingly by
mega-cap growth/tech names (Apple, Microsoft, Alphabet, Amazon, Nvidia) —
**stocks a bare earnings-yield value screen can never flag as "cheap,"
almost by construction.** A value screen searching for statistically cheap
businesses will systematically miss the very names that drove the index's
return in this specific window. That's a limitation of the testing window,
not necessarily of the framework's full 8-gate logic (which was never
re-applied here — this tests Book One alone, same scope as BT-2).

### The one genuinely actionable finding
**LOW-persistence names (occasional passes — a temporary dip, not a chronic
discount) clearly outperformed HIGH-persistence names (perpetually
statistically cheap): 15.24%/yr vs 9.12%/yr.** This is the same BKNG-vs-INTC
insight from the wider-universe backtest, now confirmed at the
whole-portfolio level: **a stock that trips the value screen only once or
twice tends to be a real business having a temporary bad stretch (which
recovers); a stock that trips it 8+ years running tends to be a business the
market has permanently discounted for a structural reason.** If this
framework is going to be used to build a "few wonderful businesses" starter
list, **the occasional-pass names are the better hunting ground than the
chronic-pass names** — the opposite of the naive instinct to trust whatever
looks "reliably cheap."

## LIMITATIONS, STATED PLAINLY
- **13F test**: name-resolution excluded 4 positions (see above); top-10/
  top-5 by value is a simplification of Berkshire's full portfolio (which
  runs 40-50+ names in most years) — captures the large majority of value
  but not all of it. Annual (not more frequent) reconstitution.
- **Screen portfolios**: this is Book One alone, not the full 8-gate
  framework re-applied at each entry date — a stated, deliberate scope
  limit carried over from BT-2. The 2013-2025 window is a single, unusually
  strong bull market for SPY; these results would likely look different in
  a sideways or bear-market decade, and that's not tested here.
- Both parts share the universe limitations already logged in BT-2/the wide
  backtest (coverage gaps for recent IPOs/spinoffs, survivorship bias in the
  screen universe itself).

## WHAT'S NEXT
- Re-test the screen portfolios starting from an EARLIER window (e.g.
  2003-2013) to see whether the "SPY wins because of mega-cap growth"
  explanation is specific to this decade or a durable structural feature of
  value screens.
- Apply a real Book Two / qualitative moat filter to the HIGH-persistence
  bucket specifically — does separating BKNG-type names from INTC-type names
  within that bucket (rather than avoiding chronic-pass names altogether)
  recover the underperformance?
- Full (not top-10) reconstruction of Berkshire's 13F for a more complete
  systematic replication.

## SELF-AUDIT
- [x] 13F parser validated against each filing's own stated total (15/15
  pre-2013 years match exactly; XML era trusted)
- [x] Unit-change (thousands → dollars, 2022 SEC rule) caught and corrected,
  not silently wrong
- [x] Excluded/unresolved positions named explicitly, not force-mapped
- [x] The unflattering result (screen portfolios underperforming SPY)
  reported as prominently as the favorable ones, with the honest
  explanation (mega-cap growth exclusion) stated rather than hidden
- [x] Raw 13F dataset (28 years, verified), resolved top-10 table, and
  per-ticker screen-portfolio results all committed alongside scripts

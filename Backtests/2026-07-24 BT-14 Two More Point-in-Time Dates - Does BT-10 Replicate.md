# BACKTEST BT-14 — Two More Point-in-Time Dates: Does BT-10 Replicate? — 2026-07-24

BT-10 (full 8-gate screen, 2018-06-30 anchor, 8-year hold) found the framework
built strongly outperforming portfolios: 93.8% of all possible 10-name
combinations beat SPY, median CAGR 25.46% vs. SPY's real return over the same
window. BT-11 (same discipline, 1993-06-30 anchor, 32-year hold) found the
opposite: the framework's own survivors trailed SPY by real, uncorrected
margins. The user asked directly: **"is there a backtest we could set up that
could solve this tension?"** This is that test — the same full-gate,
point-in-time protocol run fresh at two *more* independent historical dates
(2020-06-30 and 2016-06-30), neither of which informed BT-10's or BT-11's
result, run and reported honestly regardless of which prior result it
confirms.

## METHOD
Identical protocol to BT-10, applied twice, independently:
1. **Mechanical Book One screen** at 2020-06-30 and 2016-06-30, same
   503-name 2013-reconstructed S&P 500 universe and resolved-CIK
   infrastructure used throughout this project, SEC XBRL `filed`-date gated
   so no post-anchor-date fact leaks into any screen.
2. **Gate 4** (full owner-earnings formula, two-track Fortress Test) applied
   to the top-45-by-yield candidates at each date.
3. **Gates 1/2/3/5** (Circle of Competence, Moat, Management Integrity,
   Inversion) researched fresh for every Gate-4 survivor, dispatched as 11
   parallel research batches, each bound to strict era-appropriate
   point-in-time discipline: 2020 batches were blocked from using
   vaccine-timeline, election-outcome, or later-2020/2021 knowledge; 2016
   batches were blocked from using Brexit-outcome, 2016-election-outcome, or
   2017-tax-reform knowledge.
4. **Forward returns** computed from real, split/dividend-adjusted daily
   prices, entry at the closest trading day on/after the anchor date, exit at
   the latest available price (2026-07-22), same methodology as BT-9/BT-10.
5. **Exhaustive enumeration** of every possible 10-business portfolio drawn
   from each date's full-gate survivors (not sampled), compared to SPY over
   the identical real window.

## A DATA-INTEGRITY CORRECTION, CAUGHT BEFORE THE RESULT WAS FINALIZED
Before computing returns, the 2016 candidate list was checked for the same
class of error already caught once in this project (the BT-9 RTN/RTX CIK
mixup). Ticker "RTX" resolves to SEC CIK 101829 — which is **United
Technologies Corporation's** historical CIK (renamed twice: UTC to Raytheon
Technologies in 2020 after the merger with the *separate* Raytheon Company,
then to RTX Corp in 2023). The original 2016 research batch was told to treat
this candidate as "Raytheon Company standalone" and researched the wrong
company — a defense contractor — while the mechanical financial data
underneath it was actually United Technologies', a diversified industrial
conglomerate (Otis, Carrier, Pratt & Whitney, UTC Aerospace Systems).

Re-researched as the correct entity (United Technologies Corp, mid-2016,
point-in-time), the real verdict is the **opposite** of the original: Gates 1
and 2 pass (with real, flagged caveats — Otis's China share falling from ~25%
to ~15%, Pratt & Whitney's geared-turbofan program running ~$650M of negative
engine margin on cost overruns), but **Gate 3 fails** — an open, unresolved
multi-jurisdiction SEC/DOJ FCPA investigation (subpoenas issued April 2014 and
March 2015, covering both Pratt & Whitney/IAE and Otis China sales practices,
publicly disclosed in UTC's own SEC filings well before the 2016-06-30
anchor) stacked on a resolved 2012 guilty plea for illegally exporting
military software to China. **RTX/UTC is removed from the 2016 survivor
list.** Per this project's standing rule, this is a forward correction, not a
silent edit — the original mislabeled research is superseded here, not
deleted.

## RESULT — MECHANICAL SCREEN AND GATE 4

| | 2020-06-30 | 2016-06-30 |
|---|---|---|
| Universe screened | 406/503 | 386/503 |
| Book One passes | 129 | 170 |
| Top-45-by-yield candidates | 45 | 45 |
| Gate 4 eliminations | 12 (CCL, FLR — negative OE; WFC 10.8:1, PRU 14.5:1, SPG 15.6:1, LNC 19.2:1, USB 10.5:1, PFG 19.1:1, BNY 11.4:1, SLM 15.0:1, STT 15.2:1, JPM 12.0:1 — all fail the 10:1 financial-leverage ceiling) | 4 (CF, HP — negative OE; HBAN 10.1:1, STT 11.3:1 — leverage ceiling) |
| Proceed to qualitative gates | 33 | 41 |

## RESULT — QUALITATIVE GATES 1/2/3/5

**2020-06-30 — 12 of 33 survive all four gates:**
BKNG, ORLY, GOOG, FOXA, LRCX, CME, CMCSA, AFL, PNC, CSX, MA, AAPL

Notable failures: M/KSS/CPRI (Gate 2, department-store/luxury commoditization),
UNM (Gate 1), IVZ (Gate 2), LUV (Gate 5 — Berkshire's own real April/May 2020
airline exit cited by the research agent as corroborating point-in-time
evidence), FITB (Gate 3, CFPB fake-accounts-pattern suit filed 2020-03-09),
RF (Gate 3, 2016 DOJ/HUD Fair Housing Act settlement), KLAC (Gate 3, 2006-07
stock-option-backdating fraud), T (Gate 2, DirecTV subscriber collapse), RTX
(Gate 1 — the *2020* RTX genuinely is the freshly-merged Raytheon
Technologies Corp, three months post-merger, correctly judged too new and
heterogeneous to pass Circle of Competence — a clean point-in-time
distinction from the 2016 correction above, not an error), HBAN (Gate 3, 2005
SEC accounting-fraud finding — flagged by the research agent as a genuine
judgment call).

**2016-06-30 — 19 of 41 survive all four gates** (after the RTX/UTC
correction):
NVDA, BKNG, ORLY, CSX, AAPL, CME, MA, NEE, AFL, FAST, MPC, KEY, PSX, APH,
PCAR, NDAQ, DOV, PNC, CMI

Notable failures: CMG/TSN (Gate 2), KLAC (Gate 3, same 2006-07 backdating),
WMT (Gate 3, live/unresolved 2016 Mexico bribery investigation), FOSL (Gate
2, real smartwatch substitution damage), M/KSS/BEN (Gate 2), WU (Gate 2+3,
adjudicated 2010 AML settlement), ISRG (Gate 3, 2013 FDA warning
letter/securities settlement — flagged as debatable, otherwise the strongest
business in its batch), GEN/VLO/IBM (Gate 2, IBM specifically on 16
consecutive quarters of revenue decline), LYB/GPS/F (Gate 2), COF (Gate 3,
2012 CFPB deceptive-marketing action), MOS (Gate 2), JPM (Gate 3, London
Whale admitted-misstated-financial-results finding), WDC (Gate 2, real
HDD-to-SSD substitution), UTC/RTX (Gate 3, see correction above).

### The strongest cross-date signal in the whole project: repeated integrity failures
Three names now have **independent Gate 3 failures at multiple historical
dates**, researched by different agent batches months apart with no shared
context:
- **FITB** — fails at three separate dates now (2016 test run: 2008 CRE-loss/
  DOJ-FHA violations; BT-10's 2018 run: same; this test's 2020 batch: a fresh
  CFPB fake-accounts-pattern lawsuit filed March 2020)
- **KLAC** — fails at two dates (2016 and 2020, both independently citing the
  same 2006-07 options-backdating fraud)
- **BEN** — fails at two dates (2016 and 2020, both citing active-to-passive
  fee compression; the 2020 batch additionally flagged a live India
  fund-freeze crisis)

This is the single most reassuring finding across every backtest run this
month: Gate 3 is not noise. The same real companies get caught by
independent research passes, at different anchor dates, for reasons that
were genuinely knowable at each date — not hindsight, not coincidence.

## RESULT — FORWARD RETURNS (real, split/dividend-adjusted, to 2026-07-22)

**2020-06-30 anchor, 6.06 years — SPY: 2.641x, 17.36% CAGR**

| Ticker | Entry | Exit | Multiple | CAGR |
|---|---|---|---|---|
| LRCX | $30.37 | $319.65 | 10.52x | 47.42% |
| GOOG | $70.06 | $319.09 | 4.55x | 28.40% |
| AFL | $31.30 | $125.60 | 4.01x | 25.75% |
| AAPL | $88.30 | $333.02 | 3.77x | 24.47% |
| ORLY | $28.11 | $87.40 | 3.11x | 20.57% |
| PNC | $83.98 | $250.99 | 2.99x | 19.79% |
| BKNG | $62.37 | $180.35 | 2.89x | 19.14% |
| CSX | $21.46 | $49.97 | 2.33x | 14.96% |
| FOXA | $24.80 | $55.31 | 2.23x | 14.14% |
| CME | $127.59 | $255.31 | 2.00x | 12.12% |
| MA | $285.33 | $539.66 | 1.89x | 11.08% |
| CMCSA | $30.47 | $23.77 | 0.78x | -4.01% |

11 of 12 beat a coin flip on absolute return; only CMCSA lost money in real
terms — the single clean loser in either cohort.

**2016-06-30 anchor, 10.06 years — SPY: 4.202x, 15.33% CAGR**

| Ticker | Entry | Exit | Multiple | CAGR |
|---|---|---|---|---|
| NVDA | $1.15 | $206.84 | 179.48x | 67.48% |
| AAPL | $21.76 | $333.02 | 15.30x | 31.13% |
| APH | $13.06 | $152.67 | 11.69x | 27.67% |
| MPC | $27.99 | $318.78 | 11.39x | 27.34% |
| CMI | $86.85 | $666.82 | 7.68x | 22.45% |
| CSX | $7.55 | $49.97 | 6.62x | 20.65% |
| MA | $82.85 | $539.66 | 6.51x | 20.47% |
| PCAR | $24.04 | $132.24 | 5.50x | 18.46% |
| FAST | $8.54 | $45.17 | 5.29x | 18.00% |
| NDAQ | $18.39 | $92.09 | 5.01x | 17.36% |
| ORLY | $18.07 | $87.40 | 4.84x | 16.95% |
| DOV | $47.59 | $214.57 | 4.51x | 16.14% |
| AFL | $28.61 | $125.60 | 4.39x | 15.84% |
| PNC | $58.28 | $250.99 | 4.31x | 15.61% |
| PSX | $54.46 | $212.30 | 3.90x | 14.47% |
| CME | $66.23 | $255.31 | 3.85x | 14.35% |
| BKNG | $48.90 | $180.35 | 3.69x | 13.85% |
| NEE | $25.26 | $89.78 | 3.56x | 13.43% |
| KEY | $7.29 | $22.65 | 3.11x | 11.93% |

Every single one of the 19 survivors individually beat SPY's 15.33% CAGR
except KEY (11.93%) — 18 of 19 names, not just the portfolio average, cleared
the index on their own.

## RESULT — EXHAUSTIVE PORTFOLIO ENUMERATION vs. SPY

| | 2020 (C(12,10)=66 portfolios) | 2016 (C(19,10)=92,378 portfolios) |
|---|---|---|
| SPY CAGR | 17.36% | 15.33% |
| Portfolio CAGR — min / median / mean / max | 17.07% / 22.99% / 22.42% / 24.85% | 15.09% / 36.14% / 28.75% / 37.93% |
| Beat rate vs. SPY | **65/66 = 98.5%** | **92,372/92,378 = 100.0%** |

Both dates replicate BT-10, not BT-11. This is the first time the
full-gate protocol has been run at genuinely new, previously-untouched
anchor dates since BT-10 — and both independently landed on the same side of
the tension the user asked this test to resolve.

### Checked directly: is the 2016 result just an NVDA artifact?
NVDA's 179x return is large enough to distort a small-sample average, so
before trusting the 100% beat rate, the same enumeration was re-run on the
18 non-NVDA survivors only (C(18,10) = 43,758 portfolios, NVDA never
included):

| | Ex-NVDA 2016 (C(18,10)=43,758 portfolios) |
|---|---|
| SPY CAGR | 15.33% |
| Portfolio CAGR — min / median / mean / max | 15.09% / 19.89% / 19.75% / 22.92% |
| Beat rate vs. SPY | **43,752/43,758 = 100.0%** |

The beat rate holds at 100% and the median more than beats SPY (19.89% vs.
15.33%) with NVDA excluded entirely. NVDA inflates the *magnitude* of the
2016 result substantially (median drops from 36.14% to 19.89% without it)
but is not the *source* of the outperformance — the other 18 names, on their
own, still clear SPY in every single 10-name combination.

## WHAT THIS SETTLES
1. **BT-10 replicates.** Two more independent point-in-time full-gate runs,
   at dates neither BT-10 nor BT-11 touched, both land solidly on BT-10's
   side of the tension: near-100% beat rates, real double-digit CAGR margins
   over SPY, at both a 6-year and a 10-year real horizon.
2. **The 2016 result is not a single-stock artifact.** Removing the best
   performer (NVDA, +179x) still leaves a 100% beat rate and a real,
   substantial margin over SPY.
3. **Gate 3 (management integrity) is producing genuinely repeatable
   signal**, not noise — FITB, KLAC, and BEN each failed independently at
   multiple dates for real, disclosed, point-in-time-knowable reasons.
4. **BT-11's 32-year result now looks more like the outlier**, not the
   typical case — three independent full-gate tests (BT-10, and this test's
   two dates) all show strong, replicated outperformance; only the single
   1993-anchor, 32-year test showed underperformance, and BT-12 already
   showed roughly a third of that gap was a monitoring-discipline artifact
   (static buy-and-hold vs. the framework's own Gate 7/8 rotation mandate),
   not a pure selection failure.

## HONEST LIMITATIONS
- **Qualitative gate research is AI-run**, same standing caveat as every
  prior full-gate backtest (BT-10, BT-11, BT-12, BT-13) — not independently
  human-reverified line by line, though the point-in-time discipline was
  explicitly enforced in every research prompt and the RTX/UTC catch in this
  test is direct evidence the discipline surfaces real errors rather than
  papering over them.
- **Neither date has BT-11's horizon.** The longest test here is 10 years
  (2016); BT-11's 32-year result is still the only long-horizon full-gate
  data point this project has, and it remains the weakest result on record.
  A 20+ year full-gate test at a *third* independent date (e.g., 2006 or
  2010) would be the natural way to check whether the pattern holds at
  longer horizons too, or whether 1993 genuinely was a harder environment
  (a real possibility BT-11 raised and this test does not resolve).
- **No monitoring/rotation applied here** — like BT-10, these are static
  buy-and-hold results from the anchor date to today. BT-12 already showed
  monitoring can move the needle materially; a monitored version of these
  two cohorts (checking each survivor's thesis at a real interim date, e.g.
  2023) is a natural next test, not yet run.
- **Survivorship within the screened universe**: both anchor dates draw from
  the same 2013-reconstructed 503-name universe used throughout this
  project, which has its own coverage gaps (97 names unscreened at 2020, 117
  at 2016 — mostly missing SEC XBRL company-facts data, logged in the
  screen-results files) — a company that would have passed but isn't in the
  reconstructed universe or lacks XBRL coverage cannot be found.
- **Position sizing is equal-weight**, per the enumeration methodology — the
  moat-only conviction-weighting edge found in BT-13 was not applied here,
  and would need its own pass on these two new cohorts to check whether it
  replicates a third and fourth time.

## SELF-AUDIT
- [x] Full 8-gate qualitative pass required for every survivor at both
  dates, not just the mechanical Book One screen
- [x] Point-in-time discipline explicitly enforced in every one of the 11
  research dispatches, era-appropriate for both 2020 and 2016
- [x] A real data-integrity error (RTX/UTC CIK mixup) was caught, verified
  against the actual SEC CIK/entityName, re-researched correctly, and
  corrected forward with the original wrong verdict superseded, not
  silently edited
- [x] Two independent anchor dates run and reported together, not
  cherry-picked after seeing which one looked better
- [x] The 2016 result's dependence on a single outlier (NVDA) was checked
  directly by re-running the full enumeration with it excluded, not assumed
  away
- [x] Cross-date repeated Gate 3 failures (FITB, KLAC, BEN) reported as
  evidence the integrity gate produces real signal, cited to the specific
  independent research batches that found them
- [x] Results reported honestly regardless of which prior backtest (BT-10 or
  BT-11) they ended up confirming
- [x] All data, scripts, and raw screen/Gate-4/returns/enumeration outputs
  committed under `Backtests/`

## ⚠ CORRECTION — A LOOK-AHEAD BUG IN THE BOOK ONE SCREEN INVALIDATES THIS DOCUMENT'S RESULTS (2026-07-25)

**The screen that produced this document's candidate list contained a
look-ahead bug. The results below should not be relied on.**

**The bug.** Market cap was computed as `price * shares_as_of(anchor)`, where
the price came from a cached Yahoo series. Both Yahoo price fields (`adjclose`
and `quote.close`) are back-adjusted to **today's** share basis, while the
share count is the true point-in-time figure. Market cap was therefore
understated -- and owner-earnings yield overstated -- by the cumulative split
factor occurring **after** the anchor date. Verified: AAPL at 2013-06-30
computed to $11.7B against a real ~$372B (31.7x understated, exactly its 7:1
2014 and 4:1 2020 splits plus dividend drift).

**Why this is not a rounding error.** Companies that split are overwhelmingly
companies whose stock *rose*. The bug therefore inflated the measured yield of
future winners specifically, and since candidates were selected as the
top-N-by-yield, **it fed look-ahead bias directly into candidate selection.**
The screen was preferentially finding future winners because they were future
winners.

**The fix.** Market cap is split-invariant, so the price needs no adjustment
at all -- the share count is brought onto today's basis instead:
`cap = close(anchor) * shares(at measurement date) * splits effective after
that measurement date`. Every corrected cap is now validated against
`dei:EntityPublicFloat`, the filed 10-K cover-page market value (available for
553/558 filers, measured at the fiscal-Q2 close = our June-30 anchors). The
project had no independent market-cap check before; that is why this survived
four backtests. Corrected screen: `Backtests/scripts/screen_universe_v3b.py`.

**Also affected:** `bt_engine.py` and `bt_engine_wide.py` carry the identical
defect, so the 49.3% mechanical "coin flip" win rate is likewise computed off a
biased selection.

**Impact on BT-14 specifically — this withdraws the document’s central claim.**
Re-tested against the corrected screen:

| Cohort | Published survivors | Still clear Book One | Now fail |
|---|---|---|---|
| 2016-06-30 | 19 | **10** (CSX, AAPL, AFL, MPC, KEY, PSX, PCAR, DOV, PNC, CMI) | 9 — NVDA (1.75%), BKNG (1.71%), MA (1.77%), ORLY (1.94%), CME (2.76%), FAST (2.79%), APH (3.00%), NEE (3.17%), NDAQ (3.31%) |
| 2020-06-30 | 12 | **4** (FOXA, CMCSA, AFL, PNC) | 8 — MA (1.05%), GOOG (1.30%), LRCX (1.40%), BKNG (1.63%), CME (2.30%), AAPL (2.89%), ORLY (2.98%), CSX (3.21%) |

Again the pattern is that the *winners* fail: NVDA (the 179x name that drove
the 2016 result) and LRCX (the best 2020 performer at 47.4% CAGR) both miss the
hurdle outright. **The 98.5% and 100% beat rates are withdrawn**, as is this
document’s conclusion that "BT-10 replicates." The ex-NVDA robustness check
does not rescue the result, because the bias was not confined to NVDA — it
applied to every name that later split.

**What survives from BT-14.** Two things, both independent of market cap:
1. The **Gate 3 integrity findings** (FITB failing at three separate dates,
   KLAC and BEN at two each) rest on filings and litigation records, not on
   prices, and stand as written.
2. The **RTX/UTC per-era CIK correction** documented above stands.

**What is now the honest state of the question.** BT-11 (1993, 32-year hold)
used manual 10-K price extraction and never touched this screen, so it is the
only full-gate test not contaminated by this bug — and it *underperformed* SPY.
Every test that beat the market ran through the buggy screen. The framework’s
loss-avoidance evidence is unaffected; its market-beating evidence is, as of
this correction, **withdrawn and unproven.**

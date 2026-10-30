# BACKTEST RESULTS — Book One (The Statute), Point-in-Time — 2026-07-22
Answers **B1** from `BACKTEST PLAN - Statute Point-in-Time 2010-2024.md`. Phases
BT-0 (data layer), BT-1 (pipeline proof), BT-2 (full loop) complete this pass.
B2-B4 (Graham's stricter bar, the whisper filter, sell rules) remain open —
see "What's next," below.

## METHOD (point-in-time, no look-ahead)
- **Universe**: 36 large/mega-cap non-financial names this project has already
  screened (S&P 500 subset used in the 2026-07 mechanical passes) — chosen for
  known CIK/ticker validity, not cherry-picked for backtest performance.
- **Rebalance dates**: June 30, every year 2013-2025 (13 dates × 36 names =
  up to 468 screen-year observations).
- **Fundamentals**: SEC XBRL companyfacts, **filtered by `filed` date ≤
  rebalance date** — a fact filed after the rebalance date is invisible to
  that observation, same discipline as every live run this project does.
  NI-proxy (worst of the trailing 5 filed fiscal years), matching the plan's
  stated B1 scope — not the full OE formula (that requires per-year
  maintenance-capex judgment this pipeline doesn't automate; a stated
  limitation, not an oversight).
- **Hurdle**: US 30yr Treasury (FRED DGS30) nearest the rebalance date,
  floored at 4% — all 36 names are large/mega-cap, so **no size premium**
  applied uniformly.
- **Prices**: Yahoo Finance daily adjusted close (dividend/split-adjusted —
  better than the plan's stooq fallback, which is now JS-walled and unusable).
- **Holding period**: exactly 1 year, no rebalancing, no sell discipline —
  pure "would a mechanical Book One pass have beaten SPY over the next year."
- **Coverage failures are logged, not hidden**: 114 of 468 possible
  observations dropped — 92 for insufficient trailing-NI history (recent
  IPOs/spinoffs: GEHC 2023, ZTS/CDW/PYPL circa 2013-2015 didn't have 5 filed
  years yet in early test dates), 22 for missing point-in-time shares data.
  Zero dropped for missing price or yield data. Full list:
  `2026-07-22 BT Coverage Log.csv`.

## HEADLINE RESULT — HONEST, NOT FLATTERING
| | n | mean 1yr fwd return | median | vs SPY mean | vs SPY median | win rate vs SPY |
|---|---|---|---|---|---|---|
| **Statute PASSES** | 71 | 18.74% | 13.92% | +0.88pp | **-1.38pp** | **49.3%** |
| Statute FAILS | 283 | 14.94% | 11.47% | +0.81pp | -4.05pp | 43.8% |

**The mechanical Book One screen, used alone, does not reliably beat SPY.**
Mean excess return is barely positive (+0.88pp) and driven by a right-skewed
tail of a few large winners (best case +114.5%); the **median** pass actually
**trailed** SPY by 1.4 points, and the win rate (49.3%) is a coin flip. Passes
also underperformed FAILS' win rate only marginally — the screen alone is not
demonstrating a robust edge on this universe/window.

## THE MORE INTERESTING FINDING: CONCENTRATION
Only **14 of the 36 names ever passed** the Statute across 13 years — this
was never a diversified 36-name signal. Two tickers account for nearly a
third of all pass-observations:
| Ticker | Years passed (of 13) |
|---|---|
| CMCSA | 12 |
| TSCO | 10 |
| HPQ | 7 |
| TROW | 7 |
| VZ | 6 |
| ELV | 6 |
| CTSH, HCA, BBY, SWKS | 4 each |
| PHM | 3 |
| COP | 2 |
| UPS, LOW | 1 each |

A bare earnings-yield screen persistently selects the **same handful of
perpetually-"statistically cheap" names** — cable (CMCSA), telecom (VZ),
tractor retail (TSCO), health insurance (ELV) — sectors the market has
priced at a discount for structural reasons (secular decline fear,
regulatory risk), not temporary mispricing of a wonderful business. That is
**exactly the value-trap pattern Gates 2-5 exist to filter out**, and this
backtest is the first hard evidence that the filter is load-bearing: Book
One alone is necessary but not sufficient. The framework's sequential-gate
design (moat → management → balance sheet → inversion, *before* valuation)
isn't just methodological caution — this data shows the bare mechanical
screen would have handed you Comcast and Verizon on repeat for over a
decade, not a rotating list of wonderful businesses having a bad quarter.

## LIMITATIONS, STATED PLAINLY
- **Survivorship bias favors the passes, if anything**: the universe is
  today's still-listed, still-relevant large caps — a name that was cheap in
  2016 and later went bankrupt or got delisted isn't in this universe at all.
  The fact that even this survivor-biased sample failed to show a clean edge
  is a stronger (more damning) result than if the universe had been randomly
  selected.
- **NI-proxy, not full OE** — a name could look cheap on trailing NI while
  failing the framework's actual Gate 4 (maintenance capex, working capital).
  This backtest could not and does not claim to test the full framework —
  only its cheapest, most mechanical layer (Book One in isolation).
- **No qualitative gates applied** — this is deliberately what Gates 1-5
  would have screened out of the CMCSA/VZ/TSCO repeat-list; this backtest
  cannot show what a "Gates 1-5 PASS + Book One PASS" combined signal would
  have returned, because gates 1-5 require human/model judgment this
  pipeline doesn't automate. That combined test is exactly what B3 (the
  whisper filter) and a future qualitative overlay would test.
- **36 names, one hold-period convention (exactly 1yr, no rebalancing)** —
  small enough that a handful of outlier years (the 2020 COVID snap-back,
  where passes averaged +58.1% vs SPY's +40.9%, entirely on the March 2020
  rebalance date) meaningfully move the aggregate mean.

## WHAT'S NEXT (per the original plan, not yet built)
- **B2**: test Graham's stricter 2×AAA-yield bar against the same universe —
  does a harder bar produce fewer, better passes?
- **B3**: the whisper filter — restrict to Statute passes that ALSO clear a
  conventionalized Book Two (g1=2%, moat-blind NARROW spread); does that
  shrink the CMCSA/VZ/TSCO repeat problem and lift the win rate?
- **B4**: sell-rule comparison (+50%-or-2-years vs. annual rebalance vs.
  buy-and-hold of passes).
- **Expand universe** beyond the 36 already-screened names — the current
  set was chosen for known-good CIKs, not to minimize the concentration
  problem; a larger, randomly-sampled universe would test whether the
  CMCSA/TSCO/VZ repeat-pattern is universal to bare E/P screens or an
  artifact of this particular 36-name list. **✅ DONE 2026-07-22** — see
  `2026-07-22 BT Wider Universe Results.md`. The coin-flip win rate
  replicated almost exactly (50.5% vs 49.3%) on a 132-name independent
  sample (only 10/132 overlap with this list) — strengthening the "no
  reliable edge" conclusion via out-of-sample replication. Concentration
  also replicated proportionally, but its *character* was revised: the
  repeat-passer list mixes real structural decliners (Intel) with
  temporarily-cheap quality names (Booking Holdings) — the screen can't
  tell them apart, which is the sharper argument for Gates 2-5.

## SELF-AUDIT
- [x] Point-in-time discipline: every fact gated on `filed` ≤ rebalance date
- [x] Coverage failures logged (114), not silently dropped from the narrative
- [x] Survivorship-bias direction stated (favors passes, if anything)
- [x] Result reported as found — a coin-flip win rate and a concentrated,
  value-trap-leaning pass list — not smoothed into a false "framework wins"
  headline
- [x] Raw results + coverage log committed alongside this writeup

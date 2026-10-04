# BACKTEST BT-16 — The Mechanical Test, Recomputed Without the Bug — 2026-07-25

The original mechanical result — a **49.3%** one-year win rate against SPY,
"a coin flip" — was produced by `bt_engine.py`, which carried the same
market-cap look-ahead bug as the main screen (see the CORRECTION sections in
BT-9/BT-10/BT-14 and commit `4e25d38`). Any number computed by that engine had
to be recomputed before it could be quoted again.

**The headline survives the correction almost exactly: 49.6%.**

## METHOD
The original design is preserved so the numbers stay comparable: every Book One
pass is held exactly one year from a June-30 anchor and compared with SPY over
the identical window, across 13 anchors (2013-2025).

Three things are better than the original run:
1. **The bug is fixed.** Market cap is `close(anchor) × shares(measurement
   date) × splits effective after that date`, and every cap is validated
   against `dei:EntityPublicFloat` (the filed 10-K cover-page market value).
2. **The universe is the full 503-name 2013 reconstruction**, not the 36
   hand-picked large caps the original used — 944 one-year holdings rather
   than a few hundred.
3. **Rule-based data-quality exclusions** (cap-below-float, implausible yield,
   float-verification for high yields), identical to BT-15's.

## RESULT

| Anchor | n | Win % vs SPY | Median pass | Mean pass | SPY | Median − SPY |
|---|---|---|---|---|---|---|
| 2013 | 77 | 49.4% | 23.06% | 24.08% | 23.68% | −0.62 |
| 2014 | 66 | 53.0% | 8.15% | 11.62% | 7.24% | +0.91 |
| 2015 | 96 | 47.9% | 2.32% | 3.06% | 3.97% | −1.65 |
| 2016 | 105 | 68.6% | 31.03% | 28.08% | 17.77% | **+13.26** |
| 2017 | 76 | 47.4% | 13.08% | 18.91% | 14.53% | −1.45 |
| 2018 | 68 | 39.7% | 5.37% | 3.31% | 10.91% | −5.54 |
| 2019 | 82 | 19.5% | −18.54% | −15.37% | 6.38% | **−24.92** |
| 2020 | 94 | 73.4% | 60.45% | 70.74% | 40.89% | **+19.56** |
| 2021 | 42 | 64.3% | −4.58% | −3.20% | −10.62% | +6.04 |
| 2022 | 64 | 28.1% | 7.63% | 11.09% | 19.42% | −11.79 |
| 2023 | 77 | 37.7% | 16.24% | 17.13% | 24.74% | −8.50 |
| 2024 | 57 | 64.9% | 23.89% | 21.53% | 14.71% | +9.18 |
| 2025 | 40 | 45.0% | 13.46% | 14.73% | 22.21% | −8.75 |

- **Total one-year holdings: 944**
- **Overall win rate vs SPY: 49.6%** (468/944)
- **Median of per-anchor (median pass − SPY): −1.45 pts**
- Median pass beat SPY at **5 of 13** anchors

## WHY THE NUMBER BARELY MOVED — AND WHY THAT IS THE INTERESTING PART
The original figures were 49.3% and a median trailing SPY by 1.4 points. The
corrected figures, on a far larger and cleaner sample, are 49.6% and −1.45
points. The conclusion was right, and it was right for a reason worth stating.

The look-ahead bug inflated the measured yield of companies that later split —
which is to say, companies whose stock eventually rose a lot. That biases
selection toward **long-run** winners. But "this company will be much larger in
eight years" says very little about **the next twelve months**. A one-year
holding period is therefore nearly immune to the bias, while the multi-year
full-gate tests (BT-10, BT-14) were devastated by it. Same bug, same engine,
opposite consequences — determined entirely by holding period.

This also means the two halves of the old README claim were never equally
sound: the "mechanical layer is a coin flip" half was robust all along, while
the "full gates beat the market" half was an artifact.

## THE REAL FINDING: REGIME, NOT SKILL
The per-anchor spread is enormous and one-directional in its logic. The
corrected screen selects deep-value cyclicals (see BT-15), so it wins when
value works and loses badly when it does not:

- **2019 anchor: −24.92 points, 19.5% win rate.** The one-year window from
  2019-06-30 runs straight into the COVID crash, which hit cheap cyclicals,
  banks and energy hardest.
- **2020 anchor: +19.56 points, 73.4% win rate.** The window starting at the
  post-crash trough caught the value rebound.
- **2016 anchor: +13.26 points.** Post-energy-crash recovery.
- **2022/2023 anchors: −11.79 and −8.50.** Mega-cap growth ran away from value.

A strategy whose one-year outcome swings from −25 to +20 points depending on
which regime follows is not exhibiting stock-picking skill. It is a cheapness
factor, and its results are dominated by when you happen to run it.

## WHAT THIS SETTLES
1. **The bare Book One screen does not beat the market**, now demonstrated on
   944 holdings across 13 anchors with the bug removed and every market cap
   validated against a filed source. This is much stronger evidence than the
   original 36-name test provided.
2. **It matches what the corpus predicts.** The 1993 letter tells the
   "know-nothing investor" to buy an index fund rather than run a formula; a
   mechanical yield screen delivering a 49.6% coin flip is precisely that.
3. **The case for the qualitative gates is unaffected either way.** This test
   says nothing about whether Gates 1/2/3/5 add value — it only re-establishes
   the floor they would have to beat. BT-15 sets that floor for multi-year
   holds; this sets it for one-year holds.

## LIMITATIONS
- **One-year holding periods only.** Nothing here speaks to the long holds the
  corpus actually advocates; BT-15 covers those.
- **No qualitative gates, no position sizing, no monitoring.**
- **Universe is the 2013 reconstruction at every anchor**, so companies that
  entered the index after 2013 can never be selected — increasingly
  understating the opportunity set at the later anchors.
- **Coverage gaps persist**: 83-136 of 503 names lack usable XBRL at each
  anchor, and names whose fiscal-Q2 date sits far from a June anchor cannot be
  float-validated.
- **Survivorship in price data**: companies acquired or delisted mid-window
  drop out of a given anchor's sample when a one-year-forward price is
  unavailable, rather than being carried at their takeout value.

## SELF-AUDIT
- [x] Recomputed on the corrected engine rather than continuing to quote a
  figure produced by known-buggy code
- [x] Original design (one-year hold, SPY comparison, June anchors) preserved
  so the new number is directly comparable to the one it replaces
- [x] Sample enlarged from 36 hand-picked names to the full 503-name universe,
  and every market cap validated against a filed source
- [x] The result *confirms* the prior conclusion — reported as such, with the
  mechanism (holding period determines sensitivity to the bias) explained
  rather than treated as luck
- [x] Per-anchor variation reported in full, including the two worst anchors,
  rather than only the aggregate
- [x] Data and scripts committed under `Backtests/`

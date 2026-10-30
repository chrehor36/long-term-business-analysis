# BACKTEST BT-15 — The Corrected Base Rate: Eight Anchors, No Hindsight — 2026-07-25

This is the first backtest in the program run on a screen with **no look-ahead
bug**. It establishes the honest base rate that the qualitative gates must
improve on, and it is deliberately computed and published *before* spending
research effort on those gates, so that the expensive step can be judged
against a known starting point rather than assumed to be worthwhile.

Background: the screen used by BT-9, BT-10 and BT-14 computed market cap as
`price × shares_at_anchor` using a price back-adjusted to today's share basis,
which understated market cap — and overstated owner-earnings yield — by each
company's post-anchor split factor. Because companies that split are
overwhelmingly companies whose stock rose, that fed look-ahead bias straight
into candidate selection. See the CORRECTION sections appended to BT-9, BT-10
and BT-14, and commit `4e25d38`.

## METHOD
1. **Corrected Book One screen** (`scripts/screen_universe_v3b.py`) at eight
   anchors, 2013-06-30 through 2020-06-30, over the same 503-name
   2013-reconstructed S&P 500 universe, SEC XBRL `filed`-date gated. Market cap
   is now `close(anchor) × shares(measurement date) × splits after that date`,
   and **every cap is validated against `dei:EntityPublicFloat`** — the filed
   10-K cover-page market value, available for 553/558 filers.
2. **Candidate selection** (`scripts/build_candidates.py`): top 45 by yield,
   after three data-quality guards — cap-below-float exclusion, an
   implausible-yield guard (>50%), and a float-verification requirement for
   yields above 20%.
3. **Gate 4** (`scripts/gate4_generic.py`): full owner-earnings formula
   (NI + D&A − capex − ΔWC) with the two-track Fortress Test — negative
   trough owner earnings fails outright; financial businesses must also clear
   the hard 10:1 assets/equity ceiling. Financial classification is derived
   from filing tags (deposits, premiums earned, policyholder benefits,
   separate-account assets, real-estate investment property), not a
   hand-maintained list.
4. **Forward returns** to 2026-07-24 from split- and dividend-adjusted prices,
   equal-weighted across every Gate-4 survivor. No qualitative gates applied —
   that is the point.

## RESULT — CORRECTED PASS COUNTS

| Anchor | Screened | Book One passes (corrected) | was (buggy) | Gate-4 survivors |
|---|---|---|---|---|
| 2013-06-30 | 367/503 | 79 | 141 | 38 |
| 2014-06-30 | 377/503 | 69 | 148 | 38 |
| 2015-06-30 | 381/503 | 99 | 181 | 38 |
| 2016-06-30 | 393/503 | 109 | 170 | 40 |
| 2017-06-30 | 396/503 | 79 | 153 | 39 |
| 2018-06-30 | 423/503 | 80 | 142 | 36 |
| 2019-06-30 | 404/503 | 85 | 124 | 37 |
| 2020-06-30 | 407/503 | 96 | 129 | 30 |

## RESULT — THE BASE RATE

Equal-weighted, all Gate-4 survivors held from each anchor to today:

| Anchor | Yrs | n | SPY CAGR | Basket CAGR | vs SPY | Median name | Names beating SPY |
|---|---|---|---|---|---|---|---|
| 2013 | 13.1 | 38 | 14.26% | 12.48% | **−1.78** | 10.34% | 11/38 (29%) |
| 2014 | 12.1 | 38 | 13.51% | 13.00% | **−0.51** | 11.03% | 12/38 (32%) |
| 2015 | 11.1 | 38 | 14.10% | 13.07% | **−1.03** | 11.89% | 13/38 (34%) |
| 2016 | 10.1 | 40 | 15.16% | 18.18% | **+3.02** | 12.93% | 17/40 (42%) |
| 2017 | 9.1 | 39 | 14.87% | 12.69% | **−2.19** | 12.32% | 13/39 (33%) |
| 2018 | 8.1 | 33 | 14.91% | 9.88% | **−5.03** | 9.97% | 7/33 (21%) |
| 2019 | 7.1 | 37 | 15.49% | 11.28% | **−4.21** | 10.38% | 8/37 (22%) |
| 2020 | 6.1 | 30 | 17.07% | 22.31% | **+5.24** | 19.47% | 18/30 (60%) |

**The basket beat SPY at 2 of 8 anchors.** Mean margin **−0.81 pts/yr**,
median **−1.41 pts/yr**. Across all eight dates the median individual survivor
beat SPY only about a third of the time.

## WHAT THE CORRECTED SCREEN ACTUALLY SELECTS
The character of the candidate lists changed completely once the bug was fixed,
and this is the most instructive part of the result. The buggy screen surfaced
quality compounders — AAPL, NVDA, MA, V, GOOG, BKNG, ORLY — because those are
the companies that later split, and splitting was precisely what inflated their
measured yield. The corrected screen surfaces **deep-value cyclicals**: Kohl's,
Macy's, Gap, Fossil, Harley-Davidson, Pitney Bowes, IBM, Exxon, refiners,
regional banks.

That is what a bare trough-earnings-yield screen is *supposed* to find, and it
is exactly the failure mode the framework's later gates were written to catch.
The two anchors where the basket won (2016, 2020) are both dates from which
deep value subsequently rallied hard — post-energy-crash and post-COVID-trough.
The worst two (2018, 2019) are the dates from which mega-cap growth ran away
from value. The mechanical layer is not a market-beating engine; it is a
cheapness detector whose results depend heavily on the regime that follows.

## WHAT THIS MEANS FOR THE FRAMEWORK
1. **The mechanical layer, correctly computed, underperforms SPY on average**
   over these eight anchors — consistent with, and now much better evidenced
   than, the earlier 49.3% one-year win-rate finding. It also matches what the
   corpus itself predicts: the 1993 letter tells the "know-nothing investor" to
   buy an index fund rather than run a formula.
2. **The bar for the qualitative gates is now precisely known.** Roughly 30% of
   survivors beat SPY. For the full 8-gate framework to beat the index, Gates
   1/2/3/5 must select disproportionately from that top third — repeatedly, at
   independent dates. That is a demanding but testable standard, and it is the
   right question for the next test.
3. **Nothing here contradicts the loss-avoidance evidence**, which rests on
   filings and litigation records rather than prices: Gate 4's leverage ceiling
   removed 12 balance-sheet-levered financials before the 2020 anchor
   (WFC 10.8:1, PRU 14.5:1, LNC 19.2:1, SPG 15.6:1, STT 15.2:1, JPM 12.0:1,
   AMP 21.8:1 among them), and the Gate 3 integrity findings stand as written.

## LIMITATIONS
- **No qualitative gates applied.** This is a base rate, not a test of the
  framework. It says what the cheap, automatable half does on its own.
- **Equal weighting**, no rebalancing, no monitoring or rotation. BT-12 showed
  monitoring moves results materially; none is applied here.
- **Top-45-by-yield truncation** is a framework convention, not a corpus rule.
  Pools ranged from 66 to 105 passers, so between 21 and 60 passers per date
  were never examined.
- **Coverage gaps persist**: 80-136 of 503 universe names lack usable XBRL at
  each anchor, and 38 (2013) to fewer at later dates could not be
  float-validated because their fiscal-Q2 date sits far from a June anchor.
- **Two truncated series** (AET, acquired by CVS in Nov 2018) are carried to
  their last traded price; three names (BIG, PDCO, TGNA) had no usable price
  data and were dropped. Both are logged rather than silently handled.
- **The universe is the 2013 reconstruction** for all eight anchors, so a
  company that entered the index after 2013 cannot be found at any date. This
  understates the opportunity set at the later anchors specifically.

## SELF-AUDIT
- [x] Run on the corrected screen; the bug that invalidated BT-9/10/14 is fixed
  and the fix is validated against an independent filed source
  (`dei:EntityPublicFloat`), which the project previously lacked entirely
- [x] Base rate computed and published BEFORE the expensive qualitative step,
  so that step is a decision rather than an assumption
- [x] Eight independent anchors reported together — not one date, and not
  filtered after seeing which looked better
- [x] Both winning dates and both worst dates identified, with the regime
  explanation stated rather than the average alone
- [x] Data-quality exclusions are rule-based from a validator, not a
  hand-maintained KNOWN_BAD list; every exclusion is logged with its reason
- [x] Financial classification derived from filing tags, with the deliberately
  excluded loose tags documented and the reason (mislabelling an industrial as
  financial imposes a leverage ceiling it was never meant to face)
- [x] Truncated and missing price series reported, not quietly dropped
- [x] All data, scripts and per-name returns committed under `Backtests/`

# BACKTEST BT-9 — Does This Actually Build Small, Efficient, Outperforming Portfolios? — 2026-07-22

BT-8 answered a different question than the one that matters: whether the
mechanical screen predicts bad *fates* (bankruptcy, impairment). That's a
risk-avoidance test, not the actual goal. **The framework exists to build
small, concentrated portfolios that outperform the index** — that's the
question this test answers directly, using real, subsequent, point-in-time-
correct returns, not a proxy.

## METHOD
- **Universe**: the 142 names that passed BT-8's point-in-time Book One
  screen as of **2018-06-30**, drawn from the real, reconstructed 2013
  S&P 500 (not survivor-selected).
- **Entry price**: the same point-in-time price used for the screen itself
  (2018-06-30, mostly Yahoo daily closes, some 10-K cover-page AMV
  extractions where no market-data source existed).
- **Exit price**: the most recent available price (~2026-07-22, ~8.06
  years later), **using each company's actual subsequent history**, not a
  static "still trading" assumption:
  - 131 names: still independently trading, current price used directly.
  - **11 names required real corporate-action tracking**, researched
    individually rather than assumed: **BIG** (Big Lots, Chapter 7,
    common equity cancelled — $0 recovery), **JWN** (Nordstrom, taken
    private May 2025, $24.25/share cash), **TGNA** (Tegna, acquired by
    Nexstar, closed Mar 2026, $22.00/share cash), **PDCO** (Patterson
    Cos, taken private by Patient Square Capital, Apr 2025, $31.35/share
    cash), **PBCT** (People's United, merged into M&T Bank, Apr 2022,
    0.118 MTB shares per PBCT share), **STI** (SunTrust, merged into
    BB&T/Truist, Dec 2019, 1.295 TFC shares per STI share), **RTN**
    (Raytheon, merged into United Technologies renamed RTX, Apr 2020,
    2.3348 RTX shares per RTN share — confirmed the Otis/Carrier spinoffs
    happened to *UTC* holders hours *before* the merger closed, so
    Raytheon holders have no claim on those spinoffs), **SLM** (Sallie
    Mae — its Navient spinoff was 2014, before this test's 2018 entry
    date, so SLM's own price already reflects the post-spinoff business;
    no adjustment needed), **SAI/ACE/GT** — three tickers that turned out
    to be simple identity issues, not real corporate actions: SAI is an
    old ticker for what trades today as SAIC (Science Applications
    International Corp), ACE Ltd renamed to Chubb Ltd (ticker CB) in
    2016, and GT (Goodyear Tire) was simply mislabeled "ACQUIRED" in
    BT-7's fate data — it's still independently trading.
  - **Systematically checked, not assumed**: every one of the 142 names'
    cached price series was checked for staleness (last data point >45
    days old) to catch buyouts the fate label — built earlier in this
    session, before some of these 2025-2026 deals closed — wouldn't have
    caught. This is how JWN, TGNA, PDCO, ACE, and SAI were actually found.
- **Return measure**: simple price return, no dividends, on both the
  portfolio side and the SPY benchmark — an apples-to-apples comparison,
  though the absolute CAGR figures on both sides understate what a real
  total-return investor would have earned.

## RESULT

| Portfolio | N | Total return | CAGR | vs. SPY (15.17% CAGR) |
|---|---|---|---|---|
| All 142 passers, equal-weight | 142 | 207.5% | 14.95% | -0.22 pts/yr |
| Top 30 by entry yield | 30 | 353.0% | 20.61% | **+5.45 pts/yr** |
| Top 20 by entry yield | 20 | 418.3% | 22.65% | **+7.48 pts/yr** |
| Top 10 by entry yield | 10 | 386.4% | 21.68% | **+6.51 pts/yr** |

**The full 142-name passer set is not a portfolio — it's closet-indexing.**
Equal-weighting every name that mechanically cleared the hurdle ties SPY
almost exactly (14.95% vs 15.17%). That's the expected, unremarkable
result of buying ~28% of the S&P 500's own constituents: you get the
index back, roughly. **This is itself an important, honest finding**: the
mechanical Book One screen alone, at full breadth, is not an edge. The
edge — if it exists — has to come from concentration, exactly as Buffett
and Munger have always said it does.

**Concentrating on the highest-yield (deepest margin-of-safety) passers is
where the real result shows up.** Ranked by entry yield and cut to the
top 10, 20, or 30, every tier beats SPY by 5-7.5 points of CAGR a year,
compounded over 8 years — the difference between turning $1 into ~$4.9
(top 20) versus ~$3.1 (SPY).

**AIV (Apartment Investment & Management, a REIT) was excluded from the
ranking as a flagged data-quality outlier, not a real 96.68%-yield
bargain** — GAAP net income is a poor metric for REITs (depreciation and
property-sale gains routinely distort it far more than for an operating
company), and a REIT "yielding" 24x the hurdle is a methodology artifact,
not a Buffett-style screaming buy. Including it barely moves the
numbers (top 10 CAGR: 21.99% with it vs. 21.68% without) — it's flagged
for correctness, not because it changes the conclusion.

## THE HONEST CAVEAT: this is concentration risk, not free money
The top-20 portfolio's mean return (418.3%) is carried disproportionately
by two extreme winners: **NVDA (+3,429%) and KLAC (+1,961%)**. Sorted,
the top-20's constituent returns run from -13.1% to +3,429.4% — a real
distribution, not a uniform beat.

**The median tells a sharper story than the mean:**
- **Top 10**: median total return 225.4% → **median CAGR 15.76%**,
  essentially tied with (very slightly ahead of) SPY's 15.17%. At this
  tightest concentration, the *typical* name is a market performer, and
  the portfolio-level outperformance is real and reasonably broad-based.
- **Top 20**: median total return 119.5% → **median CAGR 10.24%,
  *below* SPY.** Widening from 10 to 20 names dilutes quality — more than
  half the added names underperformed the index — and the portfolio's
  continued outperformance at this width leans much more heavily on
  carrying NVDA and KLAC specifically.

**This is not a flaw in the test; it's a finding about how concentrated
value investing actually works, and it matches what Buffett and Munger
have said about their own results** — a small number of exceptional
decisions, held, do the compounding work; the rest of the portfolio
doesn't need to be exceptional, it needs to not blow up (which the Book
One screen's whole other job — the BT-7/BT-8 discrimination test — is
built to check). The honest reading: **the tightest cut (top 10) shows
real, broad-based edge; wider cuts (top 20-30) still beat the index in
aggregate, but increasingly because they didn't miss the 1-2 big winners,
not because every constituent pulled its weight.**

## LIMITATIONS, STATED PLAINLY
- **Single entry date.** This is one draw (2018-06-30), not a
  multi-period test. A single 8-year window, however large the sample of
  names, is still one realization of market history — it does not by
  itself establish that concentrating on high-yield Book One passers
  reliably beats the index across *different* starting points. BT-6
  (98/98 portfolios beating SPY across 58 survivor-biased names, uniform
  1985-2026 window) is the closest thing this project has to a
  multi-decade check, but it wasn't point-in-time screened the way this
  universe is.
- **Price return only, no dividends**, on both sides. This understates
  the absolute return of both the framework portfolio and SPY, but
  shouldn't bias the *comparison* between them unless dividend yields
  were systematically different between the two groups (plausible, since
  many high-yield-on-earnings passers are also higher-dividend payers —
  not checked here).
- **Concentration means real dispersion, not a smooth beat** — see above.
  A concentrated top-10/20 portfolio built this way is not a "safer,
  smoother" way to beat the index; it is a smaller number of bets with a
  wider range of individual outcomes that, in aggregate and historically
  in this one sample, beat the market.
- **8 corporate-action tickers out of 142 (5.6%) required manual research**
  to get a correct exit value rather than a naive "still trading, use
  latest price" assumption — a reminder that even an 8-year holding
  period for a "buy and do nothing" mechanical portfolio isn't actually
  hands-off; real portfolios experience buyouts, spinoffs, and bankruptcies
  that must be tracked to get the return right.
- Yield-ranking uses the same worst-of-trailing-5-year NI / market cap
  metric as the Book One screen itself — it is a valuation-depth ranking,
  not a quality or moat-strength ranking. It says nothing about Gates 2-5.

## WHAT THIS SETTLES, AND WHAT'S STILL OPEN
1. **The full-breadth mechanical screen is not, by itself, an edge** — it
   ties the index. This confirms the framework's own design premise:
   Book One is a *floor* (avoid the disasters, per BT-7/BT-8), not a
   *portfolio*. The edge requires concentration on top of it.
2. **Concentrating on the highest-yield passers does show a real,
   sizeable edge in this one historical sample** — 5-7.5 points of CAGR a
   year over 8 years is not noise-sized.
3. **Still open**: repeat this exact test (screen date, rank, hold to
   today) at 2-3 *different* historical screen dates (e.g. 2014-06-30,
   2016-06-30, 2020-06-30) to see whether the concentrated-tier edge is a
   repeatable property of the method or an artifact of this one window
   (which happens to include the entire 2018-2026 mega-cap tech run,
   including NVDA's AI-driven re-rating — a favorable regime this
   specific window benefited from more than most historical windows
   would).
4. **Still open**: this ranked purely on Book One yield. The framework's
   actual process would also apply Gates 2-5 (moat, management,
   incentives, fortress balance sheet) before sizing a position — that
   qualitative filter was not applied here, and might change which names
   make a real top-10/20.

## ADDENDUM — THE MONTE CARLO CONTROL: is this yield-ranking, or just concentration? (2026-07-22, same day)
The single top-10/20/30-by-yield portfolio above is one specific selection.
Before crediting the framework's yield-ranking step with the result, the
obvious control is the same test BT-6 ran: **many random small
portfolios drawn from the same pool, to see if concentration alone — with
no ranking, just fewer names — is what's doing the work.**

**Method**: 500 distinct random portfolios, 9-11 names each, sampled
without replacement from the same 142-name point-in-time passer pool used
above. Same entry date (2018-06-30), same exit values (including every
corporate action already researched for BT-9's main test), same
price-only return convention.

### Result: random concentration alone does NOT reliably beat the index
| | Beat SPY | Mean CAGR | Median CAGR |
|---|---|---|---|
| **500 random 9-11-name portfolios** | **150 / 500 (30.0%)** | 13.87% | 12.69% |
| ...excluding any portfolio containing NVDA, KLAC, LRCX, or PWR | 29 / 378 (7.7%) | 11.49% | 11.67% |
| SPY (same window) | — | 15.17% | — |

**Only 30% of random small portfolios beat the index — most don't.**
SPY's own 15.17% CAGR sits at the **70th percentile** of the 500 random
portfolios: the typical random ~10-name slice of the passer pool
*underperforms* the market it was drawn from a subset of. Strip out the
minority of portfolios lucky enough to contain one of the four biggest
individual winners (NVDA, KLAC, LRCX, PWR) and the beat rate collapses to
7.7%. **Concentration by itself is not an edge — it's variance.** Most of
that variance lands below the index, not above it.

### But the yield-ranked portfolios are not one of the lucky ones — they sit in the top decile
| Portfolio | CAGR | Percentile vs. the 500 random draws |
|---|---|---|
| Top 10 by yield | 21.68% | **90.6th** |
| Top 20 by yield | 22.65% | **93.0th** |
| Top 30 by yield | 20.61% | **88.6th** |
| SPY | 15.17% | 70.0th |

**This is the more precise, more defensible version of BT-9's headline
claim.** It isn't "concentrating on ~10 passers beats the index" (false,
per the Monte Carlo control — 70% of the time it doesn't). It's **"ranking
the passers by margin-of-safety yield and taking the top slice
outperforms not just the index, but roughly 9 out of 10 same-sized random
selections from the identical pool."** That's a materially stronger,
narrower claim, and it's the one this project can actually stand behind:
the yield-ranking step — the specific mechanism the Buffett Statute
prescribes (buy the cheapest available margin of safety among names that
already cleared the qualitative bar) — is doing real, non-random
selective work, not just riding the same handful of lucky outlier stocks
that any concentrated slice might happen to contain.

**Still an open question, not resolved here**: whether that 88-93rd
percentile result is a repeatable property of yield-ranking as a method,
or whether this one 2018 window's top-yield list happened to contain
NVDA and KLAC for reasons unrelated to the ranking mechanism itself (i.e.
would yield-ranking still land in the top decile at a *different* entry
date, one that didn't happen to catch the start of an AI-driven
semiconductor re-rating?). This is the same "single entry date" limitation
already flagged above, now sharpened: the open test is not "does
concentration work" (the Monte Carlo control already answers that: not by
itself) but specifically "does yield-ranking replicate its top-decile
showing at other historical screen dates."

## CORRECTION — RTN's CIK was resolved to the wrong company (2026-07-24)
While extracting 1990s-era filing data for a separate, later backtest, a
research pass flagged that "RTN" and "RTX" in this project's resolved-CIK
map both pointed to the same CIK (101829). Checked directly against SEC
submissions data: **CIK 101829 has been United Technologies Corp's filer
identity continuously since 1994** (renamed Raytheon Technologies Corp in
2020, then RTX Corp in 2023) — it is NOT the pre-2020 Raytheon Company,
which was a separate, smaller, pure-play defense contractor with its own
distinct CIK (1047122, "Raytheon Co/", formerly "HE Holdings Inc"). This
project's earlier CIK resolution had mistakenly mapped ticker "RTN" to
United Technologies' CIK — meaning every mechanical figure computed for
"RTN" (net income, owner earnings, market cap, entry price) was actually
United Technologies' data, not Raytheon Company's, even though BT-10's
qualitative research (which drew on real-world knowledge of "Raytheon
Company" as a business) correctly discussed the real company.

**Corrected using Raytheon Company's own FY2018 10-K** (CIK 1047122,
filed Feb 2019): aggregate market value $55.0B as of June 29, 2018,
282,239,000 shares outstanding — implied price ≈ $194.87/share, consistent
with Raytheon's real ~$200 trading range in mid-2018 (the earlier,
wrong figure was $116.03, i.e., United Technologies' price). Using
Raytheon Company's real worst-of-trailing-5-year NI ($1.996B, FY2013)
against this corrected market cap: **yield = 3.57%, which FAILS the 4.00%
hurdle** (it had shown 4.90% under the wrong company's data). RTN is
removed from the 142-name passer set (now 141).

**Impact on this document's headline numbers: negligible.** RTN was never
a top-yield name (it wasn't in the top-30-by-yield concentrated
portfolios), so the correction only affects the full-142-passer
equal-weight test: CAGR moves from 14.95% to **14.92%** (vs SPY's 15.17%)
— the "full breadth ties the index" conclusion is unchanged. The Monte
Carlo control and the top-10/20/30-by-yield results in this document are
unaffected (RTN wasn't a member of any of those portfolios). **BT-10 is
affected more substantially** — RTN was one of that test's 19 full-gate
survivors — see the correction note in that document.

Found and corrected the same day it was discovered, per this project's
standing "correct forward, don't edit history" rule — the original
numbers above are left as originally reported, corrected here rather than
silently edited.

## SELF-AUDIT
- [x] Real point-in-time entry prices (same universe/date as BT-8)
- [x] Real subsequent exit values — every corporate action (bankruptcy,
  going-private, stock-for-stock merger, spinoff-predates-entry, ticker
  rename, mislabeled fate) individually researched and sourced, not
  assumed or defaulted to "still trading"
- [x] Systematic staleness check run across all 142 names to catch
  buyouts the (stale) BT-7 fate labels would have missed — not just the
  ones already known about
- [x] Both the flattering framing (concentrated tiers beat SPY by 5-7.5
  pts/yr) and the honest caveat (median constituent in the top-20 tier
  underperforms SPY; two names carry most of the excess return) reported
  together
- [x] Known data-quality outlier (AIV, a REIT on a GAAP-NI-based screen)
  flagged and excluded from the primary ranking, with the with/without
  comparison shown rather than silently dropped
- [x] All data (screen results, per-ticker returns, portfolio construction
  script) committed under `Backtests/`
- [x] The obvious "is this just concentration, or specifically yield-
  ranking?" control run and reported even though it undercuts the naive
  version of the headline claim (random small portfolios beat SPY only
  30% of the time — this is stated plainly, not buried)
- [x] The narrower, defensible claim (yield-ranking lands in the ~90th
  percentile of same-sized random draws) is the one actually asserted,
  not the broader, false one ("concentration beats the index")

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

**Impact on BT-9 specifically:** at the 2018-06-30 anchor, Book One passes fall
from **142 to 80** once corrected. The per-name entry prices, yields, and the
full-142 CAGR reported in this document are all computed from understated
market caps and are withdrawn.

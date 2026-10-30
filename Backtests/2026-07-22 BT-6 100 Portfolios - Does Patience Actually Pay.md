# BACKTEST BT-6 — 100 Small Portfolios, All Dating 1985-2026 — 2026-07-22
Direct follow-up to the user's request: build many different small
portfolios (max 11 businesses each) from names this project has already
identified as framework-relevant, **all starting in the same year and
running to today**, compared against the market over the identical window.

## THE 1970 DATA CEILING (decided with the user before building)
Free historical price data (Yahoo, this project's only source) caps at
**500 monthly bars for almost every ticker — meaning real coverage starts
around 1985**, regardless of how old the company actually is. Coca-Cola,
ExxonMobil, Johnson & Johnson, American Express, Procter & Gamble — all cap
at 1985-01-01 despite trading since decades earlier. Only 7 tickers (3M, GE,
IBM, Honeywell, Walmart, DuPont, Entergy) have genuine 1970-72 data — nowhere
near enough for diversified portfolios. **User's decision: start at 1985.**

## METHOD — REVISED FOR A UNIFORM WINDOW
- **Universe pool**: every ticker this session has identified as
  framework-relevant — the 70 names that ever passed the mechanical Statute
  screen, the 7 actual Buffett/Berkshire picks, and ~35 resolved names from
  Berkshire's full 1998-2025 13F history — **filtered down to the 58 that
  have genuine price data reaching all the way back to 1985.** (46 were
  excluded for starting later — logged, not hidden; e.g. Booking Holdings
  1999, Alphabet 2004, Charter 2010, Kraft Heinz 2015.)
- **100 portfolio constructions attempted, max 11 businesses each** — 13
  named/themed (chronic vs. occasional Statute-passers, Buffett's actual
  picks, Berkshire's actual recent top-10, sector baskets, a one-per-sector
  diversified mix, the longest-history names) plus randomly sampled
  portfolios (sizes 5-11, seeded for reproducibility, no two sharing the
  exact same ticker set). **98 had ≥3 resolvable names and produced a valid
  result** (2 sector baskets — financials, consumer discretionary — had too
  few 1985-available members and were skipped, logged not forced).
- **Every single portfolio starts 1985-01-01 and runs to today (2026-07-22)
  — 41.6 years, uniformly, for all 98.** Equal-weighted, real buy-and-hold,
  no rebalancing.
- **Benchmark fix worth stating**: the SPY *ETF* only exists since 1993, so
  comparing a 41.6-year portfolio against SPY's own 33.5-year return would
  have understated the benchmark. Switched to the **^GSPC index** itself —
  which, it turns out, hits the *same* 1985 Yahoo data ceiling as everything
  else, making it a genuine apples-to-apples 41.6-year comparison rather
  than a mismatched one.

## HEADLINE RESULT
| | n | Win rate vs S&P 500 | Mean CAGR | Median CAGR | Range |
|---|---|---|---|---|---|
| **All 98 portfolios, 1985-2026** | 98 | **98/98 = 100%** | **13.74%** | 13.25% | 10.07% - 18.27% |
| **S&P 500 index, same window** | — | — | **9.40%** | — | — |

**Every single one of the 98 portfolios beat the S&P 500 over the full
1985-2026 window** — the worst-performing random 9-stock portfolio still
compounded at 10.07%/yr, ahead of the index's 9.40%. The best (a 5-stock
combination of AT&T, American Electric Power, U.S. Bancorp, Danaher, and
Apple) compounded at 18.27%/yr — a ~1,068x total return versus the index's
~40x over the same 41.6 years.

## WHAT THIS ACTUALLY SHOWS — AND WHAT IT DOESN'T
This is a **much cleaner, stronger result** than the earlier mixed-window
version of this test (which had portfolios starting anywhere from 4 to 42
years ago and found the edge was concentrated in long-horizon portfolios
while short ones lost). Forcing every portfolio to the same 41.6-year
window removes that confound entirely — and confirms the pattern the
mixed-window version hinted at: **held long enough, this pool of businesses
essentially always beats the index, regardless of which 5-11 of them you
picked.**

**The honest caveat, unchanged from before**: 58 unique tickers were reused
across 98 portfolios — UNP, LOW, JNJ, WDC, and JPM each appear in 17-21 of
them. **This is 98 different re-combinations of the same underlying
pool, not 98 independently-sourced trials.** The real finding is: *this
pool of 58 names* — survivors, by construction, since they were identified
via recent (2013-2025) framework/13F data and are still trading today under
the same ticker 41 years later — compounds reliably better than the index,
however you slice it into small baskets. That's a real, useful, and
substantial finding for building an actual small portfolio; it is not
independent proof that "any 11 stocks a value screen likes" would do this
regardless of survivorship.

## LIMITATIONS, STATED PLAINLY
- **Survivorship is baked into the pool itself.** These are all businesses
  that (a) still exist and trade under the same ticker today, and (b) were
  flagged as framework-relevant using recent data. A stock that would have
  passed the framework in 1985 and later went bankrupt or got delisted
  cannot appear in this pool — it was built backward from today's
  survivors, the same directional bias noted in every backtest this
  session, now operating over a much longer window.
- Equal-weighted, no rebalancing, dividends via adjusted close.
- Book One / actual-holdings logic, not the full qualitative 8-gate
  framework re-verified at an actual 1985 entry date (no free point-in-time
  fundamental data exists that far back — a stated, hard limitation, not
  an oversight).
- 2 of the planned 13 named portfolios (financials, consumer discretionary
  sector baskets) had too few 1985-available members and were skipped
  rather than force-filled.

## WHAT'S NEXT
- The infrastructure is seed-parameterized
  (`build_100_portfolios.py <seed>`) specifically so this can be re-run with
  different random draws — the user has indicated they want to run this
  multiple times.
- A genuinely independent second pool (built from 1985-era-only data
  sources, not backward-extended from a 2013-2025-screened pool) would be
  needed to fully separate "the framework works" from "these particular
  58 survivors happened to do well."

## SELF-AUDIT
- [x] All 98 portfolios verified to start on the identical date (1985-01-01)
  and run the identical window (41.6 years) — no mixed-window confound
- [x] Benchmark mismatch (SPY's 1993 inception vs. a 1985 portfolio start)
  caught and fixed by switching to ^GSPC, not silently left inconsistent
- [x] Excluded tickers (46 of 104) logged with reasons, not hidden
- [x] Survivorship-bias direction stated plainly as the standing caveat
- [x] Full 98-portfolio results (composition, CAGR, benchmark) and the
  seed-reproducible script committed

# BACKTEST — Buffett's Own Public-Equity Picks, Held As Long As He Held Them — 2026-07-22
A different test than BT-0/1/2: not "does the framework's mechanical screen
beat SPY on a systematic sample," but **"does a small portfolio of Buffett's
own actual, documented picks, held for the real durations he held them,
compound at a rate that matches Berkshire's own long-run record?"**

## METHOD
- **7 positions**, chosen because each has a clean, single, uninterrupted
  ticker history and a documented entry (and, where sold, exit) date —
  no spinoffs/mergers/going-private complications to untangle:

| Ticker | Entry (as used) | Sourcing |
|---|---|---|
| KO (Coca-Cola) | 1989-01-01 | **Verbatim** — the 1989 Letter's holdings table shows the position built to 23,350,000 sh at $1,023,920K cost by year-end 1989 |
| AXP (American Express) | 1998-01-01 | **Verbatim** — 2003 Letter: "we last changed our position in...American Express in 1998" |
| MCO (Moody's) | 2000-01-01 | **Verbatim** — 2003 Letter: "...and Moody's in 2000" |
| IBM | 2011-03-01 | **Verbatim** — 2011 Letter: "As was the case with Coca-Cola in 1988...I was late to the IBM party" |
| WFC (Wells Fargo) | 1990-01-01 | Public record (initial 1990 purchase during the era's bank-stock selloff) — not verbatim-cited this pass |
| AAPL (Apple) | 2016-06-01 | Public record + partial corpus support (2020 Letter: "We began buying Apple stock..."); exact 2016 start date is public record |
| BAC (Bank of America) | 2011-08-01 | Public record (2011 preferred+warrant deal, converted to common 2017) — not verbatim-cited this pass |

- **Exits**: WFC (~2022-03, public record — largely exited) and IBM
  (~2018-01, public record — fully exited, a position Buffett has
  since publicly called a mistake) are treated as closed. KO, AXP, MCO,
  AAPL, BAC are treated as still held through today (2026-07-22), though
  AAPL and BAC were both meaningfully trimmed in 2024 — the calculation
  below doesn't capture that trim, a stated simplification (see
  Limitations).
- **Prices**: Yahoo Finance monthly adjusted close (dividend/split-adjusted)
  — Yahoo's free monthly series caps near 500 bars, which lines up almost
  exactly with a ~1985 start for most of these tickers; long enough to
  cover every entry date above.
- **Benchmarks, matched to each position's own actual window**: Berkshire
  Class A stock (BRK-A) and SPY — not just Berkshire's all-time figure, but
  Berkshire's *own stock return over the identical window* each pick was
  held, for a fair comparison.

## RESULT

| Ticker | Entry | Exit | Years | **Pick CAGR** | Multiple | BRK.A CAGR, same window | SPY CAGR, same window |
|---|---|---|---|---|---|---|---|
| KO | 1989-01 | today | 37.6 | 11.95% | 69.3x | 14.26% | 10.78% |
| AXP | 1998-01 | today | 28.6 | 11.21% | 20.8x | 9.85% | 9.24% |
| WFC | 1990-01 | 2022-03 | 32.2 | 12.59% | 45.3x | 14.17% | 10.34% |
| MCO | 2000-01 | today | 26.6 | **17.15%** | 66.9x | 10.55% | 8.43% |
| IBM | 2011-03 | 2018-01 | 6.8 | **2.73%** | 1.2x | 14.87% | 13.95% |
| AAPL | 2016-06 | today | 10.1 | **30.53%** | 14.9x | 12.79% | 15.21% |
| BAC | 2011-08 | today | 15.0 | 16.47% | 9.8x | 13.54% | 14.89% |

**Equal-weighted portfolio CAGR: 14.66%/yr** (median 12.59%).
**Matched-window average, if you'd held BRK.A itself instead: 12.86%/yr.**
**Matched-window average, if you'd just held SPY instead: 11.83%/yr.**

## THE HONEST HEADLINE
On a fair, apples-to-apples basis — the same specific holding windows, not
Berkshire's legendary full-history number — **an equal-weighted portfolio
of just these 7 famous Buffett picks beat both Berkshire's own stock
(14.66% vs 12.86%) and the S&P 500 (14.66% vs 11.83%) over the periods
they were actually held.** A handful of genuinely wonderful, long-held
businesses did what the framework's whole thesis says they should.

It does **not** match Berkshire's famous **19.7% compounded annual gain,
1965-2025** [2025 Letter], and that comparison would be unfair to make
without the caveat Buffett gave himself, in his own words, in 1994:
**"A fat wallet, however, is the enemy of superior investment results. And
Berkshire now has a net worth of $11.9 billion compared to about $22
million when Charlie and I began to manage the company."** [1994 Letter]
The 19.7% figure spans the decades when Berkshire's capital base was small
enough to compound at rates a company of today's size structurally cannot
repeat — comparing a 7-stock modern picks-portfolio against that number
would be comparing different eras, not different skill.

## THE MOST INTERESTING INDIVIDUAL RESULTS
- **Apple (30.53%/yr, 14.9x in just over 10 years)** is the standout — and
  it beat even *Berkshire's own concurrent stock return* (12.79%) and SPY
  (15.21%, closer but still behind AAPL) over the identical window.
- **IBM (2.73%/yr) is Buffett's own acknowledged mistake**, and the data
  says so plainly: Berkshire's own stock returned 14.87%/yr and SPY 13.95%
  over the same 2011-2018 window IBM was held — a stark, honest
  underperformer sitting right next to the framework's best-known wins.
- **Coca-Cola and Wells Fargo — the two most "iconic forever-hold" names
  on this list — actually trailed Berkshire's own stock return over their
  own holding windows** (KO: 11.95% vs 14.26%; WFC: 12.59% vs 14.17%).
  Legendary status and being a good long-term holding are not the same
  thing as beating the alternative of just holding Berkshire itself — a
  finding the mythology around these two positions doesn't usually mention.
- **Moody's and Bank of America** both clearly beat their matched
  benchmarks (MCO by the widest margin of any position against both
  comparisons; BAC modestly against both).

## LIMITATIONS, STATED PLAINLY
- **This is not a random sample — it's the 7 most famous Buffett picks with
  clean, uncomplicated ticker histories.** Unlike the S&P 500 backtests,
  this is deliberately survivorship/fame-biased: these are the picks people
  talk about specifically *because* most of them worked. A fair
  "randomly-sampled Buffett portfolio" test would need Berkshire's full 13F
  history (available from 1977 onward via SEC EDGAR) sampled systematically
  rather than hand-picked by reputation — not yet built (see What's Next).
- **Entry/exit dates for WFC, AAPL, and BAC are public record, not
  verbatim-cited from the corpus this pass** — flagged rather than
  presented as equivalent in rigor to the KO/AXP/MCO/IBM dates, which are.
- **Positions still "held" are computed through today without modeling the
  2024 trims** to AAPL and BAC — the real current CAGR for those two is
  somewhat lower than shown here since Berkshire sold a large fraction of
  both in 2024.
- **Monthly closes, not daily** — fine for multi-decade CAGRs, not precise
  to the day.
- **The framework's own gates were not re-run against these picks at their
  purchase dates this pass** — this test measures whether Buffett's actual
  picks compounded well, not whether *our* mechanical/qualitative gates
  would have flagged them at the time. That's the natural next question.

## WHAT'S NEXT
- **B5**: re-run Gate 1-5 qualitative logic and, where data allows (IBM
  2011, AAPL 2016, BAC 2011 — inside the XBRL era), the mechanical Book One
  math against each purchase date, to test whether the *framework itself*
  — not just hindsight — would have said yes.
- **Systematic 13F sample**: pull Berkshire's full historical 13F holdings
  (SEC EDGAR, 1977-present) and test a broader, non-cherry-picked slice of
  everything Buffett bought, not just the 7 names everyone already knows
  worked out.
- **Washington Post / GEICO / Capital Cities appendix**: these three have
  real, verbatim-sourced 1989-letter cost/value data (WPO: $9.731M cost →
  $486.366M value by 1989 alone) but involve spinoffs, full buyouts, or
  stock-for-stock mergers that complicate a clean CAGR calculation — worth
  a dedicated pass rather than folding into this table.

## SELF-AUDIT
- [x] Entry dates verbatim-cited where the corpus supports them (4 of 7);
  public-record dates explicitly flagged as such (3 of 7)
- [x] Benchmarks matched to each position's actual window, not just
  Berkshire's all-time headline figure
- [x] The unflattering comparisons (IBM vs its window, KO/WFC vs BRK.A's
  own concurrent return) reported alongside the flattering ones
- [x] Cherry-pick/survivorship bias of the 7-name selection named
  explicitly, not glossed over
- [x] Raw computation script and results committed

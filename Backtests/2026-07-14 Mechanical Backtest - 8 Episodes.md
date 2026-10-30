# Mechanical Backtest — 8 Historical Episodes
**Date: 2026-07-14.** Tests the MECHANICAL layer only (Gate 6-B Statute comparison, with
Book Two corroboration at extremes), using only figures knowable on the episode date.

## Design honesty (read first)
- **Gates 1–3 and 5 are NOT backtested.** Judging Coca-Cola's 1988 moat while knowing
  the ending is hindsight cosplay — the corpus names the trap [E1-02]. Only arithmetic
  that a spreadsheet could have run on the date is scored.
- **Episode selection is curated, not random** — famous, well-documented cases including
  Berkshire's own buys and misses plus deliberate false-positive candidates. n=8 is
  anecdote, not statistics. A systematic test needs point-in-time fundamentals data
  (Compustat/CRSP-class) we don't have.
- Earnings yield = trailing GAAP earnings yield (documented multiples), not full OE —
  a data limitation, flagged.
- 30-yr yields: FRED/Treasury annual or month averages for the episode date.

## The eight episodes

| # | Episode | Earnings yield | 30-yr | Statute verdict (on the date) | What happened | Score |
|---|---|---|---|---|---|---|
| 1 | **KO, 1988** (Buffett's buy, ~15×) | 6.7% | ~8.96% | Bare: **FAIL**. Coca-Cola clause (WIDE, 70% → 6.27%): **PASS** | ~10× by 1998 | ✓ via clause |
| 2 | **KO, 1998** (~45×) | 2.2% | ~5.58% | **FAIL** — not close; fails clause too (3.91%) | ~zero total return 1998→2011 | ✓ |
| 3 | **MSFT, Dec 1999** (~70×) | ~1.4% | ~6.3% | **FAIL** decisively | Dead decade; price halved, underwater ~13 yrs | ✓ |
| 4 | **S&P 500, Mar 2000** (P/E ~29) | ~3.4% | ~6.0% | **FAIL** at the index level | Lost decade (negative 2000–09) | ✓ |
| 5 | **IBM, 2011** (Buffett's buy, ~13× at $170) | ~7.7% | ~4.0% | **PASS** comfortably | ~+5% TOTAL over 6.5 yrs vs S&P +130%; Buffett exited 2018, called it a mistake | ✗ false positive |
| 6 | **AAPL, May 2016** (Buffett's buy, ~10.6×) | ~9.4% | ~2.6% | **PASS** — hugely | +335% by 2024 (Berkshire's numbers) | ✓ |
| 7 | **INTC, late 2019** (~12×) | ~8.1% | ~2.4% | **PASS** comfortably | roughly halved over 5 yrs | ✗ false positive |
| 8 | **NVDA, mid-2023** (trailing ~110×) | <1% | ~4.0% | **FAIL** | ~tripled anyway | ✗ false negative (by design) |

**Raw score: 5 correct / 2 false positives / 1 false negative.**

## What the results actually say

**1. The Statute has real teeth at extremes — in both directions.** Every famous
overvaluation episode (KO '98, MSFT '99, the 2000 index top) fails loudly, and the
subsequent dead decades followed. The corpus itself made this exact call in real time:
the 1999 Fortune essay [E4-08] and the 2001 market-cap/GNP warning [E4-09] are the
Statute's macro logic published by Buffett before the outcome. And the two great
Berkshire entries (KO '88, AAPL '16) both clear — KO only via the Coca-Cola clause,
**which is precisely the episode the clause is named for. The 1988 purchase FAILS the
bare Statute (6.7% vs 8.96%) — the clause isn't a loophole, it's the codification of
the single most famous exception in Berkshire history.**

**2. The false positives are the sequence argument, quantified.** IBM 2011 and INTC
2019 both passed the arithmetic and both destroyed capital vs the market. In both
cases the failure lived in Gate 2 territory — moat DIRECTION: IBM's revenue declined
five consecutive years while the cloud ate its franchise; Intel's process delays
(10nm) were public in filings and trade press from 2018. Cheapness passed the math;
the moat was narrowing. **The framework's core claim — qualitative gates before
valuation, a failed gate stops the analysis — is exactly the filter these two needed.**
That's not a defense we invented after the fact; it's the May-edition sequence
principle the corpus grounded via the five risk factors [E3-10]: certainty about the
business comes before price.

**3. The false negative is the design working as intended.** NVDA 2023 at 110× fails
and then triples. The framework will always miss these: it prices demonstrated owner
earnings, not future states of the world. The cost is opportunity, never capital —
the corpus's asymmetry ("Never risk permanent loss of capital" [E5-05]) accepts that
trade explicitly.

**4. Scope of the claim.** This validates the comparison-hurdle logic as a filter at
valuation extremes and confirms the gates carry weight arithmetic can't. It does NOT
prove the framework beats the market — that would need the full process (gates
included) run point-in-time across an unselected universe, which no honest backtest
of qualitative judgment can do. The framework's own verdict standard applies to
itself: judge over years of forward runs, minimum three [E1-03].

## Sources
KO 1988/1998 multiples: gurufocus/Science of Hitting compilation of Berkshire records.
IBM: $170 avg / 13× / ~5% total return incl. dividends (gurufocus, CNBC, Motley Fool).
AAPL: ~10.6× May 2016, +335% by 2024 (Benzinga/Nasdaq/CNN). MSFT/S&P/INTC/NVDA
multiples: contemporaneous public records. 30-yr yields: FRED DGS30/WGS30YR.

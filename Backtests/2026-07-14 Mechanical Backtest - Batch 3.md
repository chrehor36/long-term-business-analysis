# Mechanical Backtest — Batch 3 (8 more episodes)
**Date: 2026-07-14.** Stress tests: the 1972 two-sided market, the 1981–82 rate
extreme, a moat-evaporation false-positive hunt (Kodak), and two episodes whose
outcomes are documented inside the corpus itself. Same design and caveats as
Batches 1–2.

| # | Episode | Yield vs sovereign long bond | Mechanical verdict (on the date) | What happened | Score |
|---|---|---|---|---|---|
| 17 | **See's Candies, 1972** ($25M price; $2M after-tax on $8M tangible — the corpus's own numbers [E2-04]) | ~8.0% vs ~6.2% | Statute **PASS** | $13M after-tax by 1983 [1983 appendix]; $1.35B cumulative pre-tax on $32M added capital by 2007 [2007 letter] | ✓ |
| 18 | **McDonald's, late 1972** (Nifty Fifty, ~71×) | ~1.4% vs ~6.2% | **FAIL** | −70%+ by 1974; a dead decade — even though the BUSINESS ultimately proved great. Price was the mistake [E2-19 cuts both ways] | ✓ |
| 19 | **S&P 500, 1981 → Aug 1982** (two-phase) | 1981: ~11% vs ~13.5% → FAIL. Aug 1982: P/E < 7 → **14%+ vs ~13.3% → PASS** | Refused the market all through 1981; turned buyable at the low | 1981: market kept falling ✓. From Aug 1982: tripled in 5 years; +17%/yr for 18 ✓ | ✓✓ |
| 20 | **Cisco, Mar 2000** (~130–190×) | <1% vs ~5.9% | **FAIL** | −86%; below its 2000 high for two decades | ✓ |
| 21 | **Kodak, mid-2000** ($55–60; FY2000 EPS $4.57) | ~7.9% vs ~5.9% | Statute **PASS** | EPS $0.26 in 2001; −90%+; bankrupt 2012 | ✗ false positive |
| 22 | **Moody's, Mar 2009** (~$15–20; 2008 EPS $1.87) | ~10–12% vs ~3.6% | Statute **PASS** | ~20×+ over the following 12 years | ✓ |
| 23 | **Japanese trading houses, Aug 2020** (Berkshire's buy, ~6–8×) | ~13–16% vs JGB 30-yr ~0.6% | **PASS** — hugely (earnings-currency anchor) | Corpus-documented: cost $13.8B → value $23.5B by end-2024 plus rising yen dividends [2024 letter] | ✓ |
| 24 | **Home Depot, Dec 1999** (~65×) | ~1.5% vs ~6.3% | **FAIL** | $70 → $21 (2003); regained $70 only in 2013 — 14 dead years | ✓ |

**Batch 3: 7 correct / 1 false positive / 0 by-design misses.**

## RUNNING SCORECARD (24 episodes)
**18 correct · 3 false positives · 3 by-design misses · 0 false negatives among
value entries.**

## Findings

**1. August 1982 is the most surprising result of the whole study.** Expectation
going in: the Statute must break in a 13% Treasury world — nothing can clear that
hurdle, so it would miss the century's best entry point. What actually happened: it
refused the market through 1981 (P/E ~9, yield ~11% vs 13.5% — and prices kept
falling, so the refusal was right), and then the August 1982 bottom pushed the S&P
below 7× earnings — **the market itself rose to meet the hurdle**, yield 14%+ vs
~13.3%, and the Statute flipped to PASS within weeks of the generational low. It then
caught a triple in five years. The comparison logic scales to rate extremes without
amendment. Caveat honestly noted: the pass had near-zero cushion — starter-size
territory, which is what Book One grants anyway.

**2. The false-positive pattern is now 3-for-3 on the same failure mode.** IBM 2011
(revenue shrinking), Intel 2019 (process delays), Kodak 2000 (digital cameras — the
"close substitute" of the franchise test — in plain public view while film volumes
peaked). Every single mechanical false positive across 24 episodes is a **moat
direction** case: cheapness that passed the arithmetic while the franchise eroded in
data that was publicly available at the time. Gate 2's job description — direction,
proven with a filing-sourced metric — is not decoration. It is the entire difference
between this framework and a low-P/E screen.

**3. Two outcomes verified from inside the corpus.** See's (1983 appendix, 2007
letter) and the Japanese trading houses (2024 letter) — the framework scores its own
source documents' transactions correctly, purchase and outcome both on the record.

**4. Home Depot, both directions again.** FAIL at 65× in 1999 (correct: 14 dead
years); eliminated at Gate 4 in 2026 (declining OE, leveraged balance sheet). Same
company, different dates, different reasons, both stops. Verdicts are date-specific —
the framework has no opinion about companies, only about company-price-date triplets.

## Sources
See's: corpus (1983 letter appendix [E2-04], 2007 letter). MCD 71×:
Fesenmaier & Smith. S&P P/E below 7 in Aug 1982: multpl/macrotrends; 30-yr ~13.3%
summer 1982: FRED DGS30. Cisco/HD 1999 multiples: contemporaneous records. Kodak:
FY2000 10-K (quarterly diluted EPS $0.93/$1.62/$1.36/$0.66; quarter-end prices).
Moody's: 2008 10-K EPS, 2009 price records. Japan: corpus 2024 letter + purchase
records Aug 2020; JGB 30-yr ~0.6% (MoF).

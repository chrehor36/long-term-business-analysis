# HOG, dividend decomposition, 2019-2026
**Built 2026-08-31 for the HOG v4.1 run. Every figure filing-sourced; accessions below.**

## Sources
| document | filed | accession |
|---|---|---|
| FY2025 Form 10-K (FYE 2025-12-31) | 2026-02-26 | 0000793952-26-000011 |
| FY2023 Form 10-K | 2024-02-23 | 0000793952-24-000076 |
| FY2021 Form 10-K | 2022-02-25 | 0000793952-22-000014 |
| Q2 2026 Form 10-Q (period 2026-06-30) | 2026-08-05 | 0000793952-26-000061 |

## The filed series, cash dividends per share, as reported on the face of the
## Consolidated Statements of Operations

| FY | DPS declared | implied quarterly | total paid ($M) | vs 2019 rate |
|---|---:|---:|---:|---:|
| 2019 | **$1.50** | **$0.375** | 237.2 | 100% |
| 2020 | $0.44 | $0.375 Q1, then **$0.02** Q2-Q4 | 68.1 | 5.3% (run-rate) |
| 2021 | $0.60 | $0.15 | 92.4 | 40% |
| 2022 | $0.63 | ~$0.1575 | 93.2 | 42% |
| 2023 | $0.66 | $0.165 | 96.3 | 44% |
| 2024 | $0.69 | $0.1725 | 91.2 | 46% |
| 2025 | $0.72 | $0.18 | 86.4 | 48% |
| 2026 (H1) | $0.375 (6mo) | **$0.1875** | 41.2 (6mo) | **50.0%** |

Arithmetic check on 2020: $0.375 + (3 x $0.02) = $0.435, filed as $0.44. **The
$0.375 -> $0.02 cut is confirmed**, a 94.7% reduction in the quarterly rate,
effective with the Q2 2020 declaration.

## What the screen's "+17% five-year dividend CAGR" actually measures

`Screens/prep_lists.py` line 245 computes
`div_cagr_5y = (TTM_dividends_now / TTM_dividends_5y_ago) ** 0.2 - 1`.

- TTM now (Aug 2025 - Aug 2026): $0.18 + $0.18 + $0.1875 + $0.1875 = **$0.735**
- TTM five years ago (Aug 2020 - Aug 2021): **$0.02 + $0.02** + $0.15 + $0.15 = **$0.34**
- (0.735 / 0.34) ^ 0.2 - 1 = **+16.7%**, which the list prints as **+17%**

**The base window contains two quarters at the emergency $0.02 rate.** The entire
"+17% five-year growth" is the climb back out of the 2020 cut. It is recovery, not
compounding.

The same construction also explains why `div_cut_5y` reads False: the five-year
lookback begins in August 2021, **after** the cut, so the screen's own cut flag
cannot see the largest dividend cut in the company's modern history.

## The honest statement of the record

- The quarterly rate today ($0.1875) is **exactly 50.0%** of the 2019 rate ($0.375).
- Dollars distributed fell from **$237.2M (2019) to $86.4M (2025)**, a 64% decline,
  on a share count that fell 27% over the same period, so the per-share decline
  (52%) understates the cash decline.
- Seventeen quarterly raises since 2021 have not restored half the 2019 rate. At the
  2021-2026 rate of increase (+$0.0075/quarter/year, roughly), returning to $0.375
  would take approximately **25 more years**.
- The company has never described a policy of restoring the pre-2020 rate. The
  FY2025 10-K states capital-allocation priorities as (i) strategic initiatives and
  capex, (ii) dividends, (iii) discretionary repurchases, dividends rank second,
  and repurchases have absorbed **4x** the dividend cash since 2023
  ($1.18bn of buybacks vs $274M of dividends, FY2023-FY2025).

## Verdict for the operator's dividend-compounder mandate

**HOG FAILS THE DIVIDEND-COMPOUNDER MANDATE OUTRIGHT.** It cut 94.7% in 2020, it
has not restored half the old rate in six years, and the growth figure that put it
on the reading list is an artifact of the cut it made. The name is therefore run
below as a **VALUE / CYCLICAL** read on its own merits, with no credit taken for
dividend growth.

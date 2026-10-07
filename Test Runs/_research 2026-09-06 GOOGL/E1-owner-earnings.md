# E1 — ALPHABET OWNER EARNINGS, BY HAND, AND THE SCREEN REPRODUCTION
Compiled 2026-09-06. All $ millions. Source: SEC XBRL companyfacts (transcription/screening
per operator rule 4) with every FY2025 figure cross-checked by string match against the
filed FY2025 10-K HTML, acc. 0001652044-26-000018.

## CONVENTION: owner earnings = OCF − SBC − (c), per `THE FRAMEWORK v4.md` §Q4.

## THE SERIES

| year | OCF | SBC | capex | fin-lease ROU adds | (c)=capex+lease | **OE strict** | OE capex-only | OE deprec-end | capex/deprec | capex/revenue |
|---|---|---|---|---|---|---|---|---|---|---|
| 2013 | 18,659 | 3,343 | 7,358 | — | 7,358 | **7,958** | 7,958 | — | — | — |
| 2014 | 22,376 | 4,279 | 10,959 | — | 10,959 | **7,138** | 7,138 | — | — | — |
| 2015 | 26,024 | 5,203 | 9,915 | — | 9,915 | **10,906** | 10,906 | — | — | — |
| 2016 | 36,036 | 6,703 | 10,212 | — | 10,212 | **19,121** | 19,121 | — | — | 11.3% |
| 2017 | 37,091 | 7,679 | 13,184 | — | 13,184 | **16,228** | 16,228 | — | — | 11.9% |
| 2018 | 47,971 | 9,353 | 25,139 | — | 25,139 | **13,479** | 13,479 | — | — | 18.4% |
| 2019 | 54,520 | 10,794 | 23,548 | — | 23,548 | **20,178** | 20,178 | — | — | 14.5% |
| 2020 | 65,124 | 12,991 | 22,281 | — | 22,281 | **29,852** | 29,852 | — | — | 12.2% |
| 2021 | 91,652 | 15,376 | 24,640 | n/f | 24,640 | **51,636** | 51,636 | 66,003 | 2.40x | 9.6% |
| 2022 | 91,495 | 19,362 | 31,485 | 577 | 32,062 | **40,071** | 40,648 | 58,658 | 2.34x | 11.1% |
| 2023 | 101,746 | 22,460 | 32,251 | 564 | 32,815 | **46,471** | 47,035 | 67,340 | 2.70x | 10.5% |
| 2024 | 125,299 | 22,785 | 52,535 | 313 | 52,848 | **49,666** | 49,979 | 87,203 | 3.43x | 15.0% |
| 2025 | 164,713 | 24,953 | 91,447 | 1,606 | 93,053 | **46,707** | 48,313 | 118,624 | 4.33x | 22.7% |
| **TTM** | **185,675** | **28,147** | **132,402** | **1,902** | **134,304** | **23,224** | 25,126 | 132,291 | **5.25x** | **29.7%** |

TTM = FY2025 − H1-2025 + H1-2026, from the Q2-2026 10-Q (acc. 0001652044-26-000071):
OCF 164,713−63,897+84,859 · SBC 24,953−11,514+14,708 · capex 91,447−39,643+80,598 ·
fin-lease 1,606−606+902 · deprec 21,136−9,485+13,586 · revenue 402,836−186,662+229,692.

## THE SCREEN REPRODUCES EXACTLY — BOTH NUMBERS NAMED

`Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`:
`GOOGL,Alphabet Inc.,4097294,46910,91056,0.941,0.0114,-0.0413,0.0886,2.02,STEP UP…,0.113,,2025-12-31`

- **oe_bottom 46,910** = the **5-year FY2021–25 mean at the capex-plus-finance-lease end**.
  By hand: (51,636 + 40,071 + 46,471 + 49,666 + 46,707) / 5 = 234,551 / 5 = **46,910.2**. ✓
  *Reproducing this required finding that `capital_acquired()` adds
  `RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability` to cash capex. Capex alone
  gives 47,522.2, which is NOT the screen number. Same lesson the MSFT run recorded.*
- **oe_top 91,056** = the **3-year FY2023–25 mean at the depreciation end**.
  By hand: (67,340 + 87,203 + 118,624) / 3 = 273,167 / 3 = **91,055.7**. ✓
- spread 0.941 = (91,056 − 46,910) / 46,910 = 0.9411. ✓
- yield_bottom 0.0114 = 46,910 / 4,097,294. ✓

**Both rows reproduce to the million. Three of the last five runs found screen spreads that
would not reproduce; this one does, and — exactly as the AAPL run warned — reproducing is
not the same as being right.**

## THE FOURTH SPREAD DEFECT, REBUILT OVER MY OWN WINDOWS [E4-25]

`floor_screen.py` now emits `spread_caveat` for precisely this: the 0.941 spans only four
constructions (3y/5y × two capex ends) and **cannot see variation older than five years.**

**Strict end (c = capex + finance leases), my windows:**

| window | mean |
|---|---|
| 3-yr FY2023–25 | **47,615** |
| **5-yr FY2021–25 (the corpus default [E2-42])** | **46,910** |
| 8-yr FY2018–25 | 37,258 |
| 10-yr FY2016–25 | 33,341 |
| 13-yr FY2013–25 | 27,647 |
| **TTM to 2026-06-30** | **23,224** |

**Width at the strict end alone: 23,224 → 47,615 = 105%.** The screen says 94% across BOTH
capex ends. **My six windows at ONE end are already wider than the screen's whole range.**

**Full width, every construction: 23,224 (TTM strict) → 132,291 (TTM depreciation end) =
470%.** The screen understates the true width by roughly five times, and it understates it
in the flattering direction — a narrow spread reads as well-determined. [E4-25] says the
width IS the finding, so this is not a small error.

## THE FACT THE FILE TURNS ON

**Owner earnings at the strict end peaked at $51,636M in FY2021 and are $23,224M on the
last twelve months — DOWN 55% — while revenue over the same span rose 73%, from $257,637M
to $445,866M.**

This is the MSFT shape (−44% in four years on a 67% revenue rise) **but deeper and faster**:
Alphabet is down 55% in the same four years on a bigger revenue gain.

## THE [E5-20] TEST, AND THE BRIEF'S HYPOTHESIS (b) IS REFUTED

The brief allowed that "Alphabet's capex may be better matched to its depreciation, in which
case the honest owner-earnings number is much higher than MSFT's". **It is the reverse.**

| | GOOGL TTM | MSFT FY2026 | [E5-20] railroads |
|---|---|---|---|
| capex / depreciation | **5.25x** | 3.38x | — |
| **depreciation as share of total capex** | **19.1%** | 33% | **>60%** |
| capex / revenue | **29.7%** | 34.9% (42% w/ leases) | — |

[E5-20]: *"in the case of all railroads, merely spending their depreciation expense will not
keep them in the same place … the true maintenance capex … is higher than 60 percent of
[total capex]."* Alphabet's depreciation charge is **19.1%** of what it is actually spending.
**The D&A end of Alphabet's range is INVALID, not merely optimistic — and it is invalid by a
wider margin than Microsoft's was.**

Alphabet was squarely in [E3-44]'s default class as recently as FY2021 (capex/deprec 2.40x
is already high, but capex ran 9.6–12.2% of revenue FY2015–21 and OE rose with revenue).
It left that class in FY2024–25.

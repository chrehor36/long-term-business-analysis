# BLK COMPETITOR ROW - peer fee-rate evidence
# Research agent, 2026-09-19. PRIMARY FILINGS ONLY. Fetch and compute; no conclusions.
# THE ONE METRIC: recurring asset-management fee revenue / average AUM, in basis points,
# five fiscal years. Where the filer publishes its own rate, the filer's rate is used and
# its definition is quoted. Where the filer publishes only period-end AUM, the average of
# beginning and ending period-end AUM is used and labelled MY COMPUTATION.

---

## 1. STATE STREET (STT) - CIK 0000093751 - Investment Management line of business

**Documents.**
| tag | form | period | filed | accession | primary doc |
|---|---|---|---|---|---|
| FY2025 | 10-K | 2025-12-31 | 2026-02-19 | 0000093751-26-000124 | stt-20251231.htm |
| FY2023 | 10-K | 2023-12-31 | 2024-02-15 | 0000093751-24-000498 | stt-20231231.htm |
| FY2021 | 10-K | 2021-12-31 | 2022-02-17 | 0000093751-22-000424 | stt-20211231.htm |

**STT DOES NOT PUBLISH AN EFFECTIVE FEE RATE, AND DOES NOT PUBLISH AVERAGE AUM.**
Verified by full-text search of the FY2025 10-K: zero occurrences of "average assets under
management" or "average AUM". Only period-end AUM is given (Table 6, Table 9). The rate below
is therefore MY COMPUTATION on a (beginning + ending)/2 average.

**Management fee revenue, $M** - FY2025 10-K Table 2 TOTAL REVENUE and Table 14 INVESTMENT
MANAGEMENT LINE OF BUSINESS RESULTS (2025/2024/2023); FY2023 10-K Table 2 (2023/2022/2021).
The consolidated "Management fees" line equals the Investment Management segment's management
fees exactly (segment note: Investment Servicing management fees = $0 in all years).

| FY | mgmt fees $M | source |
|---|---|---|
| 2021 | 2,053 | FY2023 10-K Table 2 (0000093751-24-000498) |
| 2022 | 1,939 | FY2023 10-K Table 2 |
| 2023 | 1,876 | FY2025 10-K Table 2 (0000093751-26-000124) |
| 2024 | 2,124 | FY2025 10-K Table 2 |
| 2025 | 2,398 | FY2025 10-K Table 2 |

**AUM, period-end, $B** - Table 6 / Table 9 of the 10-K for each year.
2019: 3,116 | 2020: 3,467 | 2021: 4,138 (FY2021 10-K, 0000093751-22-000424)
2022: 3,481 | 2023: 4,102 | 2024: 4,715 | 2025: 5,665 (FY2025 10-K Table 9)

**RESTATEMENT FLAG.** The FY2023 10-K reported 2023 year-end AUM of **$4,128B**; the FY2025
10-K Table 9 shows the 2023 balance as **$4,102B** ($26B lower). I used the later figure.
Effect on the 2023 rate: 4.95 bps either way (4.947 vs 4.930).

**EFFECTIVE FEE RATE, bps - MY COMPUTATION (fees / average of beginning and ending AUM):**

| FY | avg AUM $B | fees $M | bps |
|---|---|---|---|
| 2021 | 3,802.5 | 2,053 | **5.40** |
| 2022 | 3,809.5 | 1,939 | **5.09** |
| 2023 | 3,791.5 | 1,876 | **4.95** |
| 2024 | 4,408.5 | 2,124 | **4.82** |
| 2025 | 5,190.0 | 2,398 | **4.62** |

**COMPARABILITY WARNINGS on STT (filer's own definitions, verbatim):**

1. **Performance fees are NOT separable.** FY2025 10-K, MD&A "Fee Revenue": *"While certain
   management fees are directly determined by the values of AUM and the investment strategies
   employed, management fees may reflect other factors, including performance fee arrangements,
   as well as our relationship pricing for clients."* And: *"Actively managed products may also
   include performance fee arrangements which are recorded when the fee is earned, based on
   predetermined benchmarks associated with the applicable account's performance."* No separate
   performance-fee line is disclosed, so unlike IVZ/TROW/BEN the STT numerator cannot be
   stripped of performance fees.
2. **Revenue where STT is not the manager is included.** FY2025 10-K Table 14 footnote (1) to
   Management fees: *"Includes revenues from SPDR(R) Gold Shares and SPDR(R) Gold MiniShares(SM)
   Trust AUM where we are not the investment manager but act as the marketing agent."*
3. **AUM definition** (FY2025 10-K Glossary, verbatim): *"Assets under management: The total
   market value of client assets for which we provide investment management strategy services,
   advisory services and/or distribution services generating management fees based on a
   percentage of the assets' market values. These client assets are not included on our balance
   sheet. Assets under management include managed assets lost but not liquidated."*
4. Revenue-recognition note, verbatim: *"Substantially all of our investment management fees
   are determined by the value of assets under management and the investment strategies
   employed."*
5. **UNRESEARCHED:** STT's average AUM as the filer would compute it (daily average). Artifact
   that would resolve it: STT quarterly earnings presentation / supplemental "Financial
   Highlights" package (Form 8-K EX-99), which may carry a daily/monthly average AUM series.
   Not fetched.

---

## 2. INVESCO (IVZ) - CIK 0000914208

**Documents.** All 10-K, calendar fiscal year.
| tag | period | filed | accession | primary doc |
|---|---|---|---|---|
| FY2025 | 2025-12-31 | 2026-02-24 | 0000914208-26-000079 | ivz-20251231.htm |
| FY2024 | 2024-12-31 | 2025-02-25 | 0000914208-25-000114 | ivz-20241231.htm |
| FY2023 | 2023-12-31 | 2024-02-21 | 0000914208-24-000219 | ivz-20231231.htm |
| FY2022 | 2022-12-31 | 2023-02-23 | 0000914208-23-000297 | ivz-20221231.htm |
| FY2021 | 2021-12-31 | 2022-02-18 | 0000914208-22-000319 | ivz-20211231.htm |

**IVZ PUBLISHES ITS OWN YIELDS** in the "Revenue yield (bps)" table in Item 7, and publishes
average AUM. Both requested figures below.

### (a) IVZ's published GROSS revenue yield, bps - the one series consistent across five years

| FY | U.S. GAAP gross revenue yield (bps) | source 10-K |
|---|---|---|
| 2021 | **48.7** | FY2021 and FY2022 and FY2023 10-K (all three agree) |
| 2022 | **44.5** | FY2022, FY2023, FY2024 10-K |
| 2023 | **40.4** | FY2023, FY2024, FY2025 10-K |
| 2024 | **37.4** | FY2024, FY2025 10-K |
| 2025 | **33.7** | FY2025 10-K (0000914208-26-000079) |

IVZ's own definition, verbatim (FY2025 10-K, footnote 2 to the AUM/yield table):
> *"U.S. GAAP gross revenue yield on AUM is equal to U.S. GAAP annualized total operating
> revenues divided by average AUM, excluding IGW AUM. The average AUM for IGW was $109.0
> billion in 2025 (2024: $88.6 billion, 2023: $87.2 billion). It is appropriate to exclude the
> average AUM of IGW as the revenues resulting from these AUM are not presented in our U.S.
> GAAP operating revenues. The U.S. GAAP gross revenue yield is not a good measure because the
> numerator excludes the management fees earned from CIP, although the denominator of the
> measure includes the AUM of these investment products."*

Note the filer itself says the gross yield "is not a good measure". Its numerator is TOTAL
operating revenues (management fees + service and distribution fees + performance fees +
other), so it is NOT a management-fee-only rate.

### (b) IVZ's published NET revenue yield, bps - THE DEFINITION CHANGED IN FY2025

| FY | net rev yield ex perf fees **ex QQQ** (pre-2025 definition) | net rev yield ex perf fees **incl. QQQ** (FY2025 definition) |
|---|---|---|
| 2021 | **39.1** (FY2022, FY2023 10-K) | not published |
| 2022 | **35.5** (FY2022, FY2023, FY2024 10-K) | not published |
| 2023 | **32.4** (FY2023, FY2024 10-K) | **28.4** (FY2025 10-K) |
| 2024 | **30.2** (FY2024 10-K) | **25.4** (FY2025 10-K) |
| 2025 | not published | **23.0** (FY2025 10-K) |

Also published FY2021 10-K vintage, on a third (older) definition that included QQQ AUM and
did not exclude performance fees the same way: net revenue yield on AUM 2021=35.1, 2020=37.7,
2019=40.3; before performance fees 2021=34.5, 2020=36.8, 2019=39.4.

IVZ's own definition of net revenue yield, verbatim (FY2025 10-K, Schedule of Non-GAAP
Information):
> *"management evaluates Net revenue yield on AUM, which is equal to Net revenues divided by
> Average AUM during the reporting period, as an indicator of the Net revenues we receive for
> each dollar of AUM we manage. Investment management fees are adjusted by renewal commissions
> and certain administrative fees. Service and distributions fees are primarily adjusted by
> distribution fees passed through to broker dealers for certain share classes and pass through
> fund-related costs..."*

And, verbatim, footnote 3 (FY2025 10-K) - the definition change:
> *"Performance fees are earned when defined performance metrics are achieved. Therefore, net
> revenue yield is calculated excluding performance fees. Net revenue yield includes net
> revenues from Invesco QQQ Trust beginning on December 20, 2025."*

Cause of the change, verbatim (FY2025 10-K footnote 1): *"Non-management fee earning flows
include Invesco QQQ Trust's flows prior to its restructuring from an UIT to an open-end fund
ETF on December 20, 2025."* Until 20 Dec 2025, IVZ earned NO management fee on QQQ, so QQQ AUM
was stripped from the yield denominator. Average QQQ AUM: 2025 $351.8B, 2024 $275.8B,
2023 $187.5B, 2022 $169.1B, 2021 $176.0B, 2020 $115.2B.

### (c) Management-fee-only rate - MY COMPUTATION, comparable to the STT/TROW/BEN construction

GAAP Investment management fees (FY2025 10-K Item 7 revenue table; FY2022 10-K Item 7 revenue
table) / IVZ's own published Average AUM:

| FY | IM fees $M | IVZ's avg AUM $B | bps |
|---|---|---|---|
| 2021 | 4,995.9 | 1,499.9 | **33.31** |
| 2022 | 4,358.4 | 1,452.5 | **30.01** |
| 2023 | 4,106.0 | 1,500.6 | **27.36** |
| 2024 | 4,342.3 | 1,712.2 | **25.36** |
| 2025 | 4,615.3 | 2,000.1 | **23.08** |

Performance fees are separately disclosed and therefore EXCLUDED from the numerator above:
2021 $56.1M, 2022 $68.2M, 2023 $46.7M, 2024 $46.4M, 2025 $41.5M - trivially small.

**COMPARABILITY WARNINGS on IVZ:**
1. **Denominator includes AUM the numerator earns nothing on.** Average AUM includes Invesco
   Great Wall (a JV carried at equity, its fees NOT in GAAP operating revenue: avg AUM $109.0B
   in 2025) and, through 2025, QQQ ($351.8B average in 2025) on which no management fee was
   earned. My (c) series is therefore biased DOWNWARD relative to a rate computed on
   fee-earning AUM only. This is the single largest non-comparability in the whole peer set.
2. **Three different published definitions in five years** (FY2021-vintage, ex-QQQ, and the
   FY2025 incl-QQQ). Do not splice them.
3. Gross yield numerator is total operating revenue, not management fees.

---

## 3. T. ROWE PRICE GROUP (TROW) - CIK 0001113169

**Documents.** All 10-K, calendar fiscal year.
| tag | period | filed | accession | primary doc |
|---|---|---|---|---|
| FY2025 | 2025-12-31 | 2026-02-13 | 0001628280-26-008002 | trow-20251231.htm |
| FY2024 | 2024-12-31 | 2025-02-14 | 0001113169-25-000007 | trow-20241231.htm |
| FY2023 | 2023-12-31 | 2024-02-16 | 0001113169-24-000007 | trow-20231231.htm |
| FY2021 | 2021-12-31 | 2022-02-24 | 0001113169-22-000005 | trow-20211231.htm |

**TROW PUBLISHES THE RATE AND PUBLISHES AVERAGE AUM.** It labels it "Investment advisory
annualized effective fee rate (EFR) (in bps)" and since the FY2024 10-K gives two versions.

| FY | EFR **with** performance-based fees (bps) | EFR **without** performance-based fees (bps) | avg AUM $B | advisory fees $M |
|---|---|---|---|---|
| 2021 | **44.4** | not published | 1,599.3 | 7,098.1 (incl. perf fees) |
| 2022 | **42.7** | **42.6** | 1,398.4 | 5,962.7 (ex perf fees 6.4) |
| 2023 | **42.2** | **41.9** | 1,362.3 | 5,709.5 (ex perf fees 38.2) |
| 2024 | **41.4** | **41.0** | 1,561.9 | 6,399.7 (ex perf fees 59.3) |
| 2025 | **39.6** | **39.4** | 1,677.3 | 6,602.3 (ex perf fees 37.4) |

Sources: 2025/2024/2023 from FY2025 10-K (0001628280-26-008002); 2024/2023/2022 from FY2024
10-K (0001113169-25-000007); 2021 from FY2021 10-K (0001113169-22-000005) and confirmed in the
FY2023 10-K (0001113169-24-000007), which shows "Annualized Effective Fee Rate (in bps)"
2023=42.2, 2022=42.7, 2021=44.4.

**ARITHMETIC VERIFIED, not assumed.** advisory fees / average AUM reproduces TROW's own
published EFR to within 0.1 bp in every one of the five years: 44.38, 42.64, 41.91, 40.97,
39.36. So TROW's EFR is exactly the metric this row asks for.

TROW's own description of how the underlying fees are struck, verbatim (FY2025 10-K, Item 1):
> *"Our investment advisory fees are generally computed using the value of assets under
> management at a contracted annual fee rate or an effective fee rate for those products with a
> tiered-fee rate structure. For the majority of our revenue, the value of the assets under
> management used to calculate the fees are based on a daily valuation."*

**COMPARABILITY WARNINGS on TROW:**
1. **A reclassification, FY2024 10-K, verbatim footnote (2):** *"Performance-based advisory fees
   were previously included in investment advisory fees. Prior periods were recast to reflect
   this change."* The recast reaches back only to 2022. **UNRESEARCHED: TROW's 2021 EFR
   excluding performance-based fees.** Artifact that would resolve it: TROW's 2021
   performance-based advisory fee amount, which is not broken out in the FY2021 10-K; a Q4-2021
   or Q4-2022 earnings release (8-K EX-99) supplemental table, or the FY2022 10-K
   (0001113169-23-000007) income statement, might carry it. Not fetched.
2. **2021 average AUM excludes acquired assets**, verbatim footnote (3) to the FY2021 10-K
   table: *"Average assets under management for 2021 does not include the impact of the acquired
   fee-basis assets under management related to the OHA acquisition."* The OHA (Oak Hill
   Advisors) close was 29 Dec 2021 - immaterial to a 2021 average, material to the 2022 step.
3. TROW's numerator is investment advisory fees only; administrative, distribution and servicing
   fees ($593.9M in 2025) are OUTSIDE it. This is the cleanest of the four numerators.
4. TROW uses a DAILY average AUM ("based on a daily valuation" for the majority of revenue);
   STT's rate above is a two-point average. Not strictly comparable at the second decimal.

---

## 4. FRANKLIN RESOURCES / FRANKLIN TEMPLETON (BEN) - CIK 0000038777 - FISCAL YEAR ENDS 30 SEPT

**Documents.** All 10-K, fiscal year ended September 30.
| tag | period | filed | accession | primary doc |
|---|---|---|---|---|
| FY2025 | 2025-09-30 | 2025-11-10 | 0000038777-25-000238 | ben-20250930.htm |
| FY2024 | 2024-09-30 | 2024-11-12 | 0000038777-24-000206 | ben-20240930.htm |
| FY2023 | 2023-09-30 | 2023-11-14 | 0000038777-23-000169 | ben-20230930.htm |
| FY2021 | 2021-09-30 | 2021-11-19 | 0000038777-21-000205 | ben-20210930.htm |

**BEN PUBLISHES THE RATE AND ITS DEFINITION IN THE SAME SENTENCE.** Verbatim (FY2025 10-K,
Item 7, Investment Management Fees):
> *"Our effective investment management fee rate excluding performance fees (investment
> management fees excluding performance fees divided by average AUM) was 40.5 and 41.1 basis
> points for fiscal years 2025 and 2024."*

And verbatim (FY2023 10-K, same passage):
> *"Our effective investment management fee rate excluding performance fees (investment
> management fees excluding performance fees divided by average AUM) was 42.1, 41.6 and 41.8
> basis points for fiscal years 2023, 2022 and 2021."*

BEN's average AUM definition, verbatim (FY2025 10-K, footnote 1 to the Average AUM table):
> *"Average AUM is calculated as the average of the month-end AUM for the trailing thirteen
> months."*
and in the MD&A overview it calls the same measure *"Simple monthly average AUM ('average
AUM')"* - the same wording appears in the FY2021 and FY2023 10-Ks, so the definition is stable
across all five years.

| FY (to 30 Sep) | published effective IM fee rate ex perf fees (bps) | IM fees $M | perf fees $M | avg AUM $B | my arithmetic check (bps) |
|---|---|---|---|---|---|
| 2021 | **41.8** | 6,541.6 | 258.6 | 1,504.1 | 41.77 |
| 2022 | **41.6** | 6,616.8 | 498.2 | 1,469.2 | 41.65 |
| 2023 | **42.1** | 6,452.9 | 550.1 | 1,400.4 | 42.15 |
| 2024 | **41.1** | 6,822.2 | 390.7 | 1,565.8 | 41.08 |
| 2025 | **40.5** | 6,981.8 | 474.0 | 1,606.7 | 40.50 |

Sources: rates 2021-2023 FY2023 10-K (0000038777-23-000169); 2024 and 2023 FY2024 10-K
(0000038777-24-000206); 2025 and 2024 FY2025 10-K (0000038777-25-000238). IM fees and avg AUM
from the Operating Revenues table and the Average AUM table of the FY2025 / FY2023 / FY2021
10-Ks. Performance-based fee amounts: FY2021/FY2022/FY2023 from the FY2023 10-K
(*"Performance-based investment management fees were $550.1 million, $498.2 million and $258.6
million for fiscal years 2023, 2022 and 2021"*); FY2024/FY2025 from the FY2025 10-K
(*"Performance fees were $474.0 million and $390.7 million for fiscal years 2025 and 2024"*).
**My arithmetic reproduces BEN's published rate in all five years to within 0.05 bp.**

**COMPARABILITY WARNINGS on BEN:**
1. **Fiscal year ends 30 September.** BEN's "FY2025" is Oct 2024 - Sep 2025. Against calendar-year
   STT/IVZ/TROW/BLK the series is offset by a quarter. Do not line the columns up naively.
2. **The numerator is gross of distribution.** BEN's own non-GAAP reconciliation subtracts an
   *"Allocation of investment management fees for sales, distribution and marketing expenses"*
   ($409.4M in FY2023, $470.3M in FY2021) from operating revenue. TROW keeps distribution fees
   in a separate revenue line and out of its advisory-fee numerator. So BEN's rate is on a
   wider numerator than TROW's by roughly 3 bps of AUM.
3. **Acquisition churn inside the window.** Legg Mason (closed FY2021, ~halved the legacy rate:
   the published rate falls 56.4 -> 47.3 -> 41.8 bps across FY2019-FY2021), Lexington (Apr 2022),
   Alcentra (Nov 2022), Putnam (1 Jan 2024). The flat 40-42 bps line is a composite of a
   declining organic rate and a changing mix, not one continuing book.
4. Average AUM is a 13-point month-end average; TROW is daily; STT is my 2-point average.


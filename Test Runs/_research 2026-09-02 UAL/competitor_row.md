# COMPETITOR ROW: United Airlines Holdings (UAL) and five US airline peers

Source: SEC XBRL `companyfacts` API plus the filed R-file financial statements on EDGAR.
Prepared 2026-09-02. All dollar figures in USD millions unless marked %.

**This document reports numbers and flags anomalies. It draws no conclusion and issues no
verdict** (operator rule 8: tools fetch and compute and are forbidden to conclude). Nothing
below should be read as a ranking, a moat claim, or a judgment about any of the six.

---

## 0. THE COMPANIES AND THEIR FILINGS

| Ticker | Registrant | CIK | FY end | Latest 10-K accession | Filed |
|---|---|---|---|---|---|
| UAL | United Airlines Holdings, Inc. | 0000100517 | 31 Dec | 0000100517-26-000023 | 2026-02-12 |
| DAL | Delta Air Lines, Inc. | 0000027904 | 31 Dec | 0000027904-26-000013 | 2026-02-11 |
| AAL | American Airlines Group Inc. | 0000006201 | 31 Dec | 0000006201-26-000014 | 2026-02-18 |
| LUV | Southwest Airlines Co | 0000092380 | 31 Dec | 0000092380-26-000004 | 2026-02-05 |
| ALK | Alaska Air Group, Inc. | 0000766421 | 31 Dec | 0000766421-26-000010 | 2026-02-12 |
| JBLU | JetBlue Airways Corp | 0001158463 | 31 Dec | 0001158463-26-000007 | 2026-02-12 |

**All six have 31 December fiscal year ends.** No fiscal-year alignment adjustment is needed,
and FY2025 is the latest filed fiscal year for all six.

Earlier-year balance sheets were read from the 10-K **for** that fiscal year, not merely the
newest filing that mentions the date. Accessions used for the FY2019 column:
UAL 0000100517-20-000010, DAL 0000027904-20-000004, AAL 0000006201-20-000023,
LUV 0000092380-20-000024, ALK 0000766421-20-000013, JBLU 0001158463-20-000012. For the
FY2017 and FY2018 columns, the FY2018 10-Ks: UAL 0000100517-19-000009,
DAL 0000027904-19-000003, AAL 0000006201-19-000009, LUV 0000092380-19-000022,
ALK 0000766421-19-000008, JBLU 0001158463-19-000018.

---

## 1. FIVE EXTRACTION DECISIONS, STATED BEFORE THE NUMBERS

**(a) Latest-filed value wins, not as-originally-filed.** Where a filer restated a
comparative, the restated figure is used, because it is the one presented on a basis
consistent with the later years. All six restated FY2017 operating income on adoption of
ASC 606. The as-originally-filed figures are in section 6 so the size of the difference is
visible.

**(b) `Revenues` was tagged 0 by ALK in its FY2017 10-K.** Alaska Air Group's FY2017 10-K
tags `us-gaap:Revenues` for FY2017 as literally zero. The FY2018 10-K reports the same
period as 7,894. The zero is a tagging artifact, not a fact, and decision (a) discards it.
Flagged because a naive first-value-wins extraction returns the zero.

**(c) Company extension tags are not in `companyfacts`, and neither are dimensioned facts.**
This is the binding constraint on Table A. UAL tags advance ticket sales and frequent flyer
deferred revenue as `ual:` extension elements. DAL, AAL and ALK present air traffic
liability and loyalty deferred revenue as `us-gaap` elements carrying an
`srt:ProductOrServiceAxis` dimension. The `companyfacts` API returns neither extension
elements nor dimensioned facts. Those lines were therefore read off the filed R-file
balance sheets directly and are cited to the accession.

**(d) `LongTermDebtAndCapitalLeaseObligations{Current}` is the balance-sheet line; the
`LongTermDebt*` pair is the debt-note component.** For every one of the six, the face of the
FY2025 balance sheet carries a single line combining long-term debt with finance leases.
Adding `FinanceLeaseLiability*` on top would double count. Where the combined tag is absent
for an earlier year (UAL FY2017 to FY2019, ALK FY2017 to FY2023, which presented debt and
leases on separate lines), the components are summed instead, and every such case is listed
in section 6.6.

**(e) The Table A denominator subtracts non-interest-bearing current liabilities as a
RESIDUAL, not as a sum of named lines.** Given (c), the named lines cannot be sourced
identically for all six. The residual is:

> NIBCL = `LiabilitiesCurrent` - (current debt and finance leases + `OperatingLeaseLiabilityCurrent`)

This is mechanically identical for all six, uses only face-of-balance-sheet totals, and
captures every non-debt current liability including the "other" lines a named-line sum would
miss. **It was verified line by line against all six filed FY2025 balance sheets and
reconciles exactly in every case** (section 6.1).

---

## 2. TABLE A. RETURN ON UNLEVERAGED NET TANGIBLE OPERATING ASSETS

### Definition, identical for all six companies and all years

> **Numerator** = operating income as filed, `us-gaap:OperatingIncomeLoss` (EBIT).
>
> **Denominator** = `Assets` - `Goodwill` - identifiable intangibles - (cash + short-term
> investments) - NIBCL, where NIBCL is the residual defined in 1(e).

Tags used for the denominator, by company:

| Component | UAL | DAL | AAL | LUV | ALK | JBLU |
|---|---|---|---|---|---|---|
| total assets | `Assets` | `Assets` | `Assets` | `Assets` | `Assets` | `Assets` |
| goodwill | `Goodwill` | `Goodwill` | `Goodwill` | `Goodwill` | `Goodwill` | **NOT TAGGED** |
| intangibles | `IntangibleAssetsNetExcludingGoodwill` | same | same | same | same | `FiniteLivedIntangibleAssetsNet` (FY2019+); **NOT TAGGED** FY2017-18 |
| cash | `CashAndCashEquivalentsAtCarryingValue` | same | **`Cash`** | same | same | same |
| short-term investments | `ShortTermInvestments` | `ShortTermInvestments` | `AvailableForSaleSecuritiesDebtSecuritiesCurrent` (FY2018+), `ShortTermInvestments` (FY2017) | `ShortTermInvestments` | `AvailableForSaleSecuritiesCurrent` (FY2017-19), `MarketableSecuritiesCurrent` (FY2023), `AvailableForSaleSecuritiesDebtSecuritiesCurrent` (FY2024-25) | `MarketableSecuritiesCurrent` |
| current liabilities | `LiabilitiesCurrent` | same | same | same | same | same |
| current operating lease | `OperatingLeaseLiabilityCurrent` | same | same | same | same | same |

**Tag substitutions, stated rather than made silently.**
- **JBLU goodwill: NOT TAGGED.** JetBlue carries no goodwill and has no goodwill line on the
  face of its balance sheet. The deduction is zero because the asset is absent, not because
  the tag is missing.
- **JBLU intangibles FY2017 and FY2018: NOT TAGGED.** `FiniteLivedIntangibleAssetsNet` begins
  at FY2019 (241). No substitute concept was used. Those two denominators are therefore
  overstated by an unknown amount of order 200, against a denominator near 7,100 to 8,000.
- **AAL cash: `CashAndCashEquivalentsAtCarryingValue` is NOT TAGGED.** American's face line is
  captioned "Cash" and carries `us-gaap:Cash`. `CashAndCashEquivalentsAtCarryingValue`
  exists in AAL's taxonomy but has no undimensioned 10-K instant facts. `Cash` is used and
  it is a different element from the one used for the other five.
- **ALK and JBLU: `ShortTermInvestments` is NOT TAGGED** for any year. ALK uses three
  different elements across the panel, listed above. JBLU uses `MarketableSecuritiesCurrent`
  throughout.
- **Restricted cash and noncurrent investments are excluded for all six.** Amounts excluded
  at FY2025: AAL 735 (restricted cash and short-term investments), ALK 28, JBLU 100 current
  restricted plus 249 noncurrent restricted plus 318 noncurrent investment securities.

### 2.1 Denominator components (USD m)

**FY2019, 31 Dec 2019 (pre-COVID comparison)**

| | assets | - goodwill | - intangibles | - cash+STI | - NIBCL | **= denominator** |
|---|---:|---:|---:|---:|---:|---:|
| UAL | 52,611 | 4,523 | 3,009 | 4,944 | 12,799 | **27,336** |
| DAL | 64,532 | 9,781 | 5,163 | 2,882 | 17,116 | **29,590** |
| AAL | 59,995 | 4,091 | 2,084 | 3,826 | 13,742 | **36,252** |
| LUV | 25,895 | 970 | 296 | 4,072 | 7,780 | **12,777** |
| ALK | 12,993 | 1,943 | 122 | 1,521 | 2,697 | **6,710** |
| JBLU | 11,918 | 0 (none) | 241 | 1,328 | 2,191 | **8,158** |

**FY2025, 31 Dec 2025 (latest fiscal year)**

| | assets | - goodwill | - intangibles | - cash+STI | - NIBCL | **= denominator** |
|---|---:|---:|---:|---:|---:|---:|
| UAL | 76,448 | 4,527 | 2,655 | 12,240 | 21,076 | **35,950** |
| DAL | 81,317 | 9,753 | 5,966 | 4,310 | 25,210 | **36,078** |
| AAL | 61,774 | 4,091 | 2,066 | 5,836 | 19,681 | **30,100** |
| LUV | 29,061 | 970 | 296 | 3,231 | 10,285 | **14,279** |
| ALK | 20,361 | 2,723 | 815 | 2,123 | 5,671 | **9,029** |
| JBLU | 16,570 | 0 (none) | 415 | 2,159 | 3,554 | **10,442** |

**All six years, denominator (USD m)**

| FY end | UAL | DAL | AAL | LUV | ALK | JBLU |
|---|---:|---:|---:|---:|---:|---:|
| 2017-12-31 | 19,416 | 19,674 | 28,621 | 13,939 | 4,670 | 7,138 |
| 2018-12-31 | 25,625 | 27,782 | 36,444 | 13,885 | 5,150 | 7,989 |
| 2019-12-31 | 27,336 | 29,590 | 36,252 | 12,777 | 6,710 | 8,158 |
| 2023-12-31 | 32,084 | 31,364 | 32,217 | 11,728 | 6,841 | 8,733 |
| 2024-12-31 | 33,004 | 32,843 | 30,783 | 13,437 | 8,208 | 9,436 |
| 2025-12-31 | 35,950 | 36,078 | 30,100 | 14,279 | 9,029 | 10,442 |

### 2.2 THE RATIO: operating income / unleveraged net tangible operating assets, %

| FY end | UAL | DAL | AAL | LUV | ALK | JBLU |
|---|---:|---:|---:|---:|---:|---:|
| 2017-12-31 | 18.6 | 30.3 | 14.8 | 24.4 | 25.9 | 13.6 |
| 2018-12-31 | 12.6 | 18.9 | 7.3 | 23.1 | 12.5 | 3.3 |
| **2019-12-31** | **15.7** | **22.4** | **8.5** | **23.1** | **15.8** | **9.8** |
| 2023-12-31 | 13.1 | 17.6 | 9.4 | 1.9 | 5.8 | (2.6) |
| 2024-12-31 | 15.4 | 18.3 | 8.5 | 2.4 | 6.9 | (7.2) |
| **2025-12-31** | **13.1** | **16.1** | **4.9** | **3.0** | **3.4** | **(3.5)** |

FY2020 to FY2022 are omitted from Table A because operating income was negative or
COVID-distorted for most of the panel and the ratio carries no meaning there. The operating
margins for those years are in Table C.

**FY2017 and FY2018 are NOT comparable to FY2019 and later. See section 4.2.**

---

## 3. TABLE B. RETURN ON TOTAL INVESTED CAPITAL INCLUDING WHAT WAS PAID FOR IT

### Definition

> **Numerator** = operating income, `us-gaap:OperatingIncomeLoss`.
>
> **Denominator** = total debt + total stockholders' equity, where total debt = current debt
> and finance leases + noncurrent debt and finance leases + `OperatingLeaseLiabilityCurrent`
> + `OperatingLeaseLiabilityNoncurrent`, and equity = `StockholdersEquity`.

Unlike Table A this denominator does not deduct goodwill, intangibles or cash. It is the
capital actually supplied, at its carrying amount, including the goodwill and intangibles
that acquisitions were paid for.

### 3.1 Components, FY2019 and FY2025 (USD m)

**FY2019, 31 Dec 2019**

| | debt+FL current | debt+FL noncurrent | op lease current | op lease noncurrent | **total debt** | equity | **denominator** |
|---|---:|---:|---:|---:|---:|---:|---:|
| UAL | 1,453 | 13,365 | 686 | 4,946 | **20,450** | 11,531 | **31,981** |
| DAL | 2,287 | 8,873 | 801 | 5,294 | **17,255** | 15,358 | **32,613** |
| AAL | 2,861 | 21,454 | 1,708 | 7,421 | **33,444** | **(118)** | **33,326** |
| LUV | 819 | 1,846 | 353 | 978 | **3,996** | 9,832 | **13,828** |
| ALK | 235 | 1,264 | 269 | 1,439 | **3,207** | 4,331 | **7,538** |
| JBLU | 344 | 1,990 | 128 | 690 | **3,152** | 4,799 | **7,951** |

**FY2025, 31 Dec 2025**

| | debt+FL current | debt+FL noncurrent | op lease current | op lease noncurrent | **total debt** | equity | **denominator** |
|---|---:|---:|---:|---:|---:|---:|---:|
| UAL | 4,426 | 20,562 | 631 | 5,417 | **31,036** | 15,282 | **46,318** |
| DAL | 1,605 | 12,507 | 809 | 5,353 | **20,274** | 20,853 | **41,127** |
| AAL | 3,753 | 25,254 | 1,058 | 5,905 | **35,970** | **(3,727)** | **32,243** |
| LUV | 324 | 4,577 | 312 | 768 | **5,981** | 7,981 | **13,962** |
| ALK | 721 | 4,834 | 197 | 1,141 | **6,893** | 4,118 | **11,011** |
| JBLU | 769 | 7,729 | 79 | 839 | **9,416** | 2,120 | **11,536** |

### 3.2 THE RATIO: operating income / (total debt + equity), %

| FY end | UAL | DAL | AAL | LUV | ALK | JBLU |
|---|---:|---:|---:|---:|---:|---:|
| 2017-12-31 | 15.6 | 27.9 | **17.4 (neg. equity)** | 25.6 | 20.0 | 16.4 |
| 2018-12-31 | 10.8 | 17.4 | **7.8 (neg. equity)** | 24.2 | 11.0 | 3.7 |
| **2019-12-31** | **13.4** | **20.3** | **9.2 (neg. equity)** | **21.4** | **14.1** | **10.1** |
| 2023-12-31 | 9.1 | 14.4 | **8.6 (neg. equity)** | 1.1 | 5.0 | (2.6) |
| 2024-12-31 | 11.0 | 15.7 | **7.8 (neg. equity)** | 1.7 | 5.3 | (5.8) |
| **2025-12-31** | **10.2** | **14.2** | **4.5 (neg. equity)** | **3.1** | **2.8** | **(3.2)** |

### 3.3 AAL EQUITY IS NEGATIVE IN EVERY YEAR IN SCOPE

`StockholdersEquity` for American Airlines Group, confirmed on the face of each filed
balance sheet as "Total stockholders' deficit":

| FY end | 2017 | 2018 | 2019 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|---:|
| AAL equity | (780) | (169) | (118) | (5,202) | (3,977) | (3,727) |

**The AAL figures in 3.2 are arithmetic, not a comparable rate of return, and should not be
ranked against the other five.** The deficit is *subtracted* from debt in the denominator,
so AAL's invested-capital base is reported smaller than the capital actually in the
business, and the resulting percentage is correspondingly larger than it would be on any
basis that did not net a deficit against debt. At FY2025 the deficit shrinks the denominator
by 3,727 on a debt base of 35,970, roughly 10%. At FY2023 it shrinks it by 5,202 on 40,663,
roughly 13%. **A reader wanting a like-for-like figure should use total debt alone as the
denominator**, which gives AAL 4.1% at FY2025 and 9.2% at FY2019 (for reference, on that
same debt-only basis UAL is 15.2% at FY2025 and DAL 28.7%).

Table A is unaffected by the deficit: its denominator is built from the asset side and
never touches the equity account.

---

## 4. TABLE C. OPERATING MARGIN, FY2017 to FY2025

Numerator `us-gaap:OperatingIncomeLoss`. Denominator
`us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax` for all company-years except
**ALK FY2017 to FY2021, which is `us-gaap:Revenues`** (ALK did not tag the contract-revenue
element until FY2022). Both are the total operating revenue line on the face of the income
statement.

### Operating income (USD m), `OperatingIncomeLoss`

| FY end | UAL | DAL | AAL | LUV | ALK | JBLU |
|---|---:|---:|---:|---:|---:|---:|
| 2017-12-31 | 3,618 | 5,966 | 4,231 | 3,407 | 1,208 | 973 |
| 2018-12-31 | 3,229 | 5,264 | 2,656 | 3,206 | 643 | 266 |
| 2019-12-31 | 4,301 | 6,618 | 3,065 | 2,957 | 1,063 | 800 |
| 2020-12-31 | (6,359) | (12,469) | (10,421) | (3,816) | (1,775) | (1,714) |
| 2021-12-31 | (1,022) | 1,886 | (1,059) | 1,721 | 685 | (80) |
| 2022-12-31 | 2,337 | 3,661 | 1,607 | 1,017 | 70 | (298) |
| 2023-12-31 | 4,211 | 5,521 | 3,034 | 224 | 394 | (230) |
| 2024-12-31 | 5,096 | 5,995 | 2,614 | 321 | 570 | (684) |
| 2025-12-31 | 4,713 | 5,822 | 1,467 | 428 | 303 | (368) |

### Total operating revenue (USD m)

| FY end | UAL | DAL | AAL | LUV | ALK | JBLU |
|---|---:|---:|---:|---:|---:|---:|
| 2017-12-31 | 37,784 | 41,138 | 42,622 | 21,146 | 7,894 | 7,012 |
| 2018-12-31 | 41,303 | 44,438 | 44,541 | 21,965 | 8,264 | 7,658 |
| 2019-12-31 | 43,259 | 47,007 | 45,768 | 22,428 | 8,781 | 8,094 |
| 2020-12-31 | 15,355 | 17,095 | 17,337 | 9,048 | 3,566 | 2,957 |
| 2021-12-31 | 24,634 | 29,899 | 29,882 | 15,790 | 6,176 | 6,037 |
| 2022-12-31 | 44,955 | 50,582 | 48,971 | 23,814 | 9,646 | 9,158 |
| 2023-12-31 | 53,717 | 58,048 | 52,788 | 26,091 | 10,426 | 9,615 |
| 2024-12-31 | 57,063 | 61,643 | 54,211 | 27,483 | 11,735 | 9,279 |
| 2025-12-31 | 59,070 | 63,364 | 54,633 | 28,063 | 14,239 | 9,062 |

### OPERATING MARGIN, %

| FY end | UAL | DAL | AAL | LUV | ALK | JBLU |
|---|---:|---:|---:|---:|---:|---:|
| 2017-12-31 | 9.6 | 14.5 | 9.9 | 16.1 | 15.3 | 13.9 |
| 2018-12-31 | 7.8 | 11.8 | 6.0 | 14.6 | 7.8 | 3.5 |
| 2019-12-31 | 9.9 | 14.1 | 6.7 | 13.2 | 12.1 | 9.9 |
| 2020-12-31 | (41.4) | (72.9) | (60.1) | (42.2) | (49.8) | (58.0) |
| 2021-12-31 | (4.1) | 6.3 | (3.5) | 10.9 | 11.1 | (1.3) |
| 2022-12-31 | 5.2 | 7.2 | 3.3 | 4.3 | 0.7 | (3.3) |
| 2023-12-31 | 7.8 | 9.5 | 5.7 | 0.9 | 3.8 | (2.4) |
| 2024-12-31 | 8.9 | 9.7 | 4.8 | 1.2 | 4.9 | (7.4) |
| 2025-12-31 | 8.0 | 9.2 | 2.7 | 1.5 | 2.1 | (4.1) |

---

## 5. TABLE D. DEBT, CASH AND LEVERAGE, LATEST FISCAL YEAR (FY2025, 31 Dec 2025)

| Component | tag |
|---|---|
| current maturities of debt and finance leases | `LongTermDebtAndCapitalLeaseObligationsCurrent` |
| noncurrent debt and finance leases | `LongTermDebtAndCapitalLeaseObligations` |
| current operating lease liability | `OperatingLeaseLiabilityCurrent` |
| noncurrent operating lease liability | `OperatingLeaseLiabilityNoncurrent` |
| equity | `StockholdersEquity` |

Verified against the face of each filed FY2025 balance sheet; all six use the combined
debt-and-finance-lease tag at FY2025, so `FinanceLeaseLiability*` is NOT added on top.

| | UAL | DAL | AAL | LUV | ALK | JBLU |
|---|---:|---:|---:|---:|---:|---:|
| Debt + fin leases, current | 4,426 | 1,605 | 3,753 | 324 | 721 | 769 |
| Debt + fin leases, noncurrent | 20,562 | 12,507 | 25,254 | 4,577 | 4,834 | 7,729 |
| Operating lease, current | 631 | 809 | 1,058 | 312 | 197 | 79 |
| Operating lease, noncurrent | 5,417 | 5,353 | 5,905 | 768 | 1,141 | 839 |
| **Total debt incl. all leases** | **31,036** | **20,274** | **35,970** | **5,981** | **6,893** | **9,416** |
| Cash and equivalents | 5,942 | 4,310 | 954 | 3,231 | 627 | 1,946 |
| Short-term investments | 6,298 | 0 | 4,882 | 0 | 1,496 | 213 |
| **Cash + short-term investments** | **12,240** | **4,310** | **5,836** | **3,231** | **2,123** | **2,159** |
| **Net debt** | **18,796** | **15,964** | **30,134** | **2,750** | **4,770** | **7,257** |
| Total stockholders' equity | 15,282 | 20,853 | **(3,727)** | 7,981 | 4,118 | 2,120 |
| **Debt / (debt + equity), %** | **67.0** | **49.3** | **see note** | **42.8** | **62.6** | **81.6** |

**AAL: debt + equity = 35,970 - 3,727 = 32,243, so the mechanical ratio is 111.6%.** That
number is reported only to show the arithmetic. A capital-structure ratio whose denominator
is smaller than its numerator because the equity account is negative does not measure
leverage on the same scale as the other five and should not be ranked against them.

**Short-term investments of 0 for DAL and LUV are real zeros**, shown as 0 on the face of the
filed balance sheet (LUV shows "Short-term investments 0" against 1,216 at FY2024). This is
unlike the ALK FY2017 revenue artifact in decision 1(b).

---

## 6. ANOMALIES AND WHERE THE COMPARISON BREAKS

### 6.1 The NIBCL residual reconciles exactly to the filed line items at FY2025

Confirming decision 1(e) against each filed balance sheet. Every row sums to the residual to
the dollar.

| | residual NIBCL | named lines from the filed balance sheet |
|---|---:|---|
| UAL | 21,076 | AP 4,567 + accrued salaries and benefits 3,900 + advance ticket sales 8,131 + frequent flyer deferred revenue 3,721 + other 757 |
| DAL | 25,210 | AP 5,226 + accrued salaries 4,906 + fuel card obligation 1,100 + other accrued 1,945 + air traffic liability 7,157 + loyalty deferred revenue 4,876 |
| AAL | 19,681 | AP 2,840 + accrued salaries and wages 2,128 + other accrued 2,916 + fuel financing 914 + air traffic liability 7,158 + loyalty program liability 3,725 |
| LUV | 10,285 | AP 1,991 + accrued liabilities 2,349 + air traffic liability 5,945 |
| ALK | 5,671 | AP 324 + accrued wages 881 + other accrued 1,055 + air traffic liability 1,689 + loyalty plan deferred revenue 1,722 |
| JBLU | 3,554 | AP 655 + air traffic liability 1,669 + accrued salaries and benefits 680 + other accrued 550 |

Of the named lines above, **only accounts payable is retrievable from `companyfacts` for all
six.** UAL's advance ticket sales and frequent flyer deferred revenue are `ual:` extension
tags; DAL's, AAL's and ALK's air traffic and loyalty lines are dimensioned
`ContractWithCustomerLiabilityCurrent` and `DeferredRevenue` facts. LUV
(`ContractWithCustomerLiabilityCurrent` = 5,945) and JBLU
(`ContractWithCustomerLiabilityCurrent` = 1,669) are the only two whose air traffic
liability is retrievable undimensioned. `AirTrafficLiabilityCurrent` is tagged only in
FY2017 to FY2018 by UAL, FY2017 by DAL and FY2017 by AAL, and never by LUV, ALK or JBLU.

### 6.2 ASC 842 was adopted on three different timetables. FY2017 and FY2018 are not comparable.

The lease standard put operating leases on the balance sheet. When each of the six did that
determines whether their FY2017 and FY2018 denominators contain their leased fleet at all.

| | FY2017 balance sheet | FY2018 balance sheet | FY2019 balance sheet |
|---|---|---|---|
| UAL | no operating leases | **recast**, leases added in the FY2019 10-K | leases |
| DAL | no operating leases | **adopted early, 1 Jan 2018**, leases present as filed | leases |
| AAL | no operating leases | **adopted early, 1 Jan 2018**, leases present as filed | leases |
| LUV | no operating leases | **NO operating leases** (adopted 1 Jan 2019, not recast) | leases |
| ALK | no operating leases | **NO operating leases** (adopted 1 Jan 2019, not recast) | leases |
| JBLU | no operating leases | **recast**, leases added in the FY2019 10-K | leases |

Evidence: DAL's FY2018 10-K balance sheet shows operating lease ROU assets 5,994 at 31 Dec
2018 against 0 at 31 Dec 2017; AAL's shows 9,151 against 0. LUV's and ALK's FY2019 10-K
balance sheets show 0 in the 31 Dec 2018 column. UAL's FY2018 10-K reports total assets of
44,792, which the FY2019 10-K restates to 49,024, a difference of 4,232 that is the
operating lease ROU asset; JBLU's moves from 10,426 to 10,959.

**Consequences, stated as facts and not adjusted for.**
- **At FY2017 none of the six carry operating leases.** Every FY2017 denominator in Tables A
  and B excludes the leased portion of the fleet, so every FY2017 percentage is computed on a
  smaller capital base than the FY2019 and later figures. The FY2017 row is higher than the
  FY2019 row for five of six companies, and this is a large part of why.
- **At FY2018 the panel is split four to two.** LUV's FY2018 denominators contain no lease
  liability at all while DAL's, AAL's, UAL's and JBLU's do. LUV's 23.1% in Table A and 24.2%
  in Table B at FY2018 are therefore not measured on the same basis as DAL's 18.9% and 17.4%.
  ALK is in the same position.
- **FY2019 onward is internally consistent** across all six. FY2019 and FY2025 are the two
  columns that can be compared without this caveat, which is why they are the two the tables
  bold.

### 6.3 Restatements: the value as originally filed differs from the value used

Decision 1(a) uses the latest-filed figure. The differences, all from ASC 606 adoption
except the ALK zero:

| | FY2017 EBIT as used | as originally filed | difference |
|---|---:|---:|---:|
| UAL | 3,618 | 3,498 | +120 |
| DAL | 5,966 | 6,114 | (148) |
| AAL | 4,231 | 4,058 | +173 |
| LUV | 3,407 | 3,515 | (108) |
| ALK | 1,208 | 1,260 | (52) |
| JBLU | 973 | 1,000 | (27) |
| JBLU FY2018 | 266 | 288 | (22) |
| **ALK FY2017 revenue** | **7,894** | **0** | **+7,894 (tagging artifact)** |

Balance-sheet restatements from ASC 842, same basis: UAL FY2018 assets 49,024 against 44,792
as filed, current liabilities 13,839 against 13,212, equity 10,042 against 9,995. JBLU FY2018
assets 10,959 against 10,426, current liabilities 2,525 against 2,418, equity 4,685 against
4,611. DAL, AAL, LUV and ALK are unchanged between the two filings.

### 6.4 Borrowings sitting inside current liabilities, outside the debt line

Two filers carry an interest-bearing current obligation that is not inside
`LongTermDebtAndCapitalLeaseObligationsCurrent`. Under the mechanically identical rule in
1(e) these remain inside NIBCL, which makes the Table A denominator smaller and the Table A
ratio larger for those two than a stricter reading would give.

| | item | tag | FY2025 | FY2024 | FY2019 | FY2018 | FY2017 |
|---|---|---|---:|---:|---:|---:|---:|
| DAL | fuel card obligation | `ShortTermNonBankLoansAndNotesPayable` | 1,100 | 1,100 | 736 | 1,075 | 1,067 |
| AAL | fuel financing | dimensioned, read from the R-file | 914 | 74 | none | none | none |

Effect if removed from NIBCL and added to debt: DAL FY2025 Table A denominator rises from
36,078 to 37,178 and the ratio falls from 16.1% to 15.7%; total debt rises to 21,374 and the
Table B ratio falls from 14.2% to 13.8%. AAL FY2025 denominator rises from 30,100 to 31,014
and the ratio falls from 4.9% to 4.7%; total debt rises to 36,884.

LUV additionally carried a "construction obligation" of 164 noncurrent at FY2019 (1,701 at
FY2018) which is a financing obligation on assets constructed for others and is not in the
debt line above.

**UAL's debt line contains sale-leaseback financial liabilities, and the FY2023 figure is on
a reclassified basis.** From FY2023 UAL's balance-sheet caption reads "long-term debt,
finance leases, **and other financial liabilities**", the last being obligations from
sale-leaseback transactions that failed sale accounting. The amount inside
`LongTermDebtAndCapitalLeaseObligations` that is neither `LongTermDebtNoncurrent` nor
`FinanceLeaseLiabilityNoncurrent`:

| UAL noncurrent | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| `LongTermDebtAndCapitalLeaseObligations` (used) | 27,413 | 25,203 | 20,562 |
| less `LongTermDebtNoncurrent` | 25,057 | 21,680 | 17,170 |
| less `FinanceLeaseLiabilityNoncurrent` | 91 | 68 | 378 |
| **= other financial liabilities** | **2,265** | **3,455** | **3,014** |

The FY2023 10-K itself (0000100517-24-000027) shows long-term debt 25,057 and long-term
finance leases 91 as separate lines totalling 25,148, with the 2,265 of sale-leaseback
liabilities sitting inside other noncurrent liabilities. The FY2024 10-K
(0000100517-25-000046) restates the FY2023 comparative onto the combined 27,413 line. Per
decision 1(a) the reclassified 27,413 is used, which is the basis consistent with FY2024 and
FY2025. On the FY2023-as-filed basis UAL total debt at FY2023 would be 34,474 rather than
36,739, and the Table B ratio 9.6% rather than 9.1%. Table A is unaffected: the
reclassification is entirely within noncurrent liabilities and does not touch
`LiabilitiesCurrent` or the Table A denominator.

### 6.5 Denominators moved for reasons other than operations

- **ALK acquired Hawaiian Holdings.** ALK goodwill rises from 1,943 at FY2023 to 2,724 at
  FY2024 and intangibles from 90 to 873. Total assets rise from 14,613 to 19,768 and revenue
  from 10,426 to 11,735, then to 14,239 at FY2025, a 21.3% single-year move, the largest in
  the panel. **ALK FY2024 and FY2025 are not like-for-like against ALK FY2019.** Note that
  Table A deducts goodwill and intangibles, so the purchase premium is removed from the
  Table A denominator but is fully present in Table B.
- **LUV's cash pile dominates its Table A denominator.** Cash plus short-term investments
  is 11,474 at FY2023 against a denominator of 11,728, and 8,725 at FY2024 against 13,437.
  Nearly half the balance sheet is deducted in those years. LUV's cash falls to 3,231 by
  FY2025 while treasury stock rises from 11,044 to 13,593, so the FY2023 to FY2025 movement
  in the LUV denominator is driven substantially by the deployment of cash into buybacks,
  not by a change in operating assets. Total assets fall from 36,487 to 29,061 over the same
  span.
- **UAL's cash plus short-term investments is 12,240 at FY2025, the largest in the panel**,
  and was 14,388 at FY2023 and 14,475 at FY2024 against pre-COVID 4,944 at FY2019. The Table
  A denominator deducts all of it.
- **JBLU reports negative operating income in every year FY2021 through FY2025.** Every
  JBLU ratio in Tables A and B for those years is a negative number divided by a positive
  capital base. It is reported as a signed percentage; a negative return is not a rate of
  return on the same scale as a positive one and its magnitude carries no ranking
  information.
- **AAL's Table A denominator has fallen every year in scope since FY2018** (36,444, 36,252,
  32,217, 30,783, 30,100) while UAL's and DAL's have risen. AAL total assets are 61,774 at
  FY2025 against 60,580 at FY2018, so the fall is in the deducted items, principally the
  growth in NIBCL from 13,148 to 19,681.

### 6.6 Tags recorded as NOT TAGGED, with no substitution made

| Company | Concept | Years | Note |
|---|---|---|---|
| JBLU | `Goodwill` | all | no goodwill exists; deduction is zero |
| JBLU | any intangibles element | FY2017, FY2018 | `FiniteLivedIntangibleAssetsNet` starts FY2019 |
| AAL | `CashAndCashEquivalentsAtCarryingValue` | all | `Cash` used instead, stated in 2 |
| AAL | `LongTermDebtNoncurrent` | all | combined tag used, per 1(d) |
| ALK, JBLU | `ShortTermInvestments` | all | alternates used, listed in 2 |
| LUV, JBLU | `LongTermDebtCurrent`, `LongTermDebtNoncurrent` | all | combined tag used, per 1(d) |
| ALK | `OperatingLeaseLiability` (total) | all | current plus noncurrent summed instead |
| all six | `Liabilities` (total liabilities) | all | none of the six tag it; not needed |
| UAL, LUV, ALK, JBLU | `AirTrafficLiabilityCurrent` | FY2019 onward | extension or dimensioned; see 6.1 |

Where a figure below the face of the balance sheet was needed and only a dimensioned or
extension fact existed, it was read from the filed R-file and is identified as such. No
different concept was ever substituted silently.

---

## 7. REPRODUCTION

Balance-sheet R-file URLs used for the FY2025 verification in 6.1:

- UAL https://www.sec.gov/Archives/edgar/data/100517/000010051726000023/R5.htm
- DAL https://www.sec.gov/Archives/edgar/data/27904/000002790426000013/R3.htm
- AAL https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/R5.htm
- LUV https://www.sec.gov/Archives/edgar/data/92380/000009238026000004/R3.htm
- ALK https://www.sec.gov/Archives/edgar/data/766421/000076642126000010/R3.htm
- JBLU https://www.sec.gov/Archives/edgar/data/1158463/000115846326000007/R3.htm

FY2019: UAL .../100517/000010051720000010, DAL .../27904/000002790420000004/R2.htm,
AAL .../6201/000000620120000023/R4.htm, LUV .../92380/000009238020000024/R2.htm,
ALK .../766421/000076642120000013/R2.htm, JBLU .../1158463/000115846320000012/R2.htm.

Figures other than those noted as read from an R-file come from
`https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json`, 10-K forms only, annual duration
facts of 340 to 380 days, USD units, undimensioned.

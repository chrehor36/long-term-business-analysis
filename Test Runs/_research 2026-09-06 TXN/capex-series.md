# TXN — filed capex, depreciation and P&L series, FY2013–FY2025 + TTM 6/30/26 (TASK 3)

**Source:** SEC XBRL `companyfacts` for CIK 0000097476, retrieved 2026-09-06 with
`User-Agent: Chris Hrehor chrehor36@gmail.com`. Every annual figure is the **as-originally-filed 10-K
value** for that fiscal year (form=10-K preferred over later restating filings). Raw JSON saved as
`_companyfacts.json` in this folder.

**Tags used:** `us-gaap:PaymentsToAcquirePropertyPlantAndEquipment` (capex),
`us-gaap:Depreciation` (TXN uses the pure `Depreciation` tag — it has **never** used
`DepreciationDepletionAndAmortization`; that concept returns HTTP 404 for this CIK. Amortization of
capitalized software is tagged separately and is small: $81M / $72M / $63M in 2025/2024/2023),
`NetCashProvidedByUsedInOperatingActivities`, `ShareBasedCompensation`, `NetIncomeLoss`,
`RevenueFromContractWithCustomerExcludingAssessedTax` (FY2016+) spliced with `SalesRevenueNet`
(FY2013–FY2015), `GrossProfit`, `OperatingIncomeLoss`, `ResearchAndDevelopmentExpense`,
`SellingGeneralAndAdministrativeExpense`, `PaymentsForRepurchaseOfCommonStock`, `InterestCostsCapitalized`.

**TTM construction:** FY2025 + six months ended 2026-06-30 − six months ended 2025-06-30, all three legs
taken from filed documents (FY2025 from the 10-K accession 0000097476-26-000059; both six-month legs from
the Q2 2026 10-Q accession 0000097476-26-000152, which presents both periods).

**Cross-check per operator rule 4:** capex FY2025 = $4,550M in XBRL; the filed Consolidated Statements of
Cash Flows in `txn-20251231.htm` line "Capital expenditures | (4,550) | (4,820) | (5,071)" — **agrees**.
TTM capex $3,312M computed here equals the $3,312M printed in the Q2 2026 10-Q free-cash-flow
reconciliation table — **agrees**.

---

## THE TABLE ($ millions, as filed)

| $ millions | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | TTM 6/30/26 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 12,205 | 13,045 | 13,000 | 13,370 | 14,961 | 15,784 | 14,383 | 14,461 | 18,344 | 20,028 | 17,519 | 15,641 | 17,682 | 19,453 |
| Gross profit | 6,364 | 7,427 | 7,560 | 8,240 | 9,614 | 10,277 | 9,164 | 9,269 | 12,376 | 13,771 | 11,019 | 9,094 | 10,083 | 11,346 |
| R&D expense | 1,522 | 1,358 | 1,280 | 1,370 | 1,508 | 1,559 | 1,544 | 1,530 | 1,554 | 1,670 | 1,863 | 1,959 | 2,083 | 2,084 |
| SG&A expense | 1,858 | 1,843 | 1,748 | 1,767 | 1,694 | 1,684 | 1,645 | 1,623 | 1,666 | 1,704 | 1,825 | 1,794 | 1,860 | 1,857 |
| Operating profit | 2,832 | 3,947 | 4,274 | 4,799 | 6,083 | 6,713 | 5,723 | 5,894 | 8,960 | 10,140 | 7,331 | 5,465 | 6,023 | 7,254 |
| Net income | 2,162 | 2,821 | 2,986 | 3,595 | 3,682 | 5,580 | 5,017 | 5,595 | 7,769 | 8,749 | 6,510 | 4,799 | 5,001 | 6,052 |
| Cash flow from operations | 3,384 | 3,892 | 4,268 | 4,614 | 5,363 | 7,189 | 6,649 | 6,139 | 8,756 | 8,720 | 6,420 | 6,318 | 7,153 | 8,667 |
| Free cash flow (see note) | *2,972* | *3,507* | *3,717* | 4,083 | 4,668 | 6,058 | 5,802 | 5,490 | 6,294 | 5,923 | 1,349 | *1,498* | *2,938* | *6,534* |
| **Capital expenditures** | **412** | **385** | **551** | **531** | **695** | **1,131** | **847** | **649** | **2,462** | **2,797** | **5,071** | **4,820** | **4,550** | **3,312** |
| **Depreciation** | **879** | **850** | **766** | **605** | **539** | **590** | **708** | **733** | **755** | **925** | **1,175** | **1,508** | **1,918** | **2,122** |
| Share-based compensation | 287 | 277 | 286 | 252 | 242 | 232 | 217 | 224 | 230 | 289 | 362 | 387 | 419 | 410 |
| Stock repurchases | 2,868 | 2,831 | 2,741 | 2,132 | 2,556 | 5,100 | 2,960 | 2,553 | 527 | 3,615 | 293 | 929 | 1,477 | 707 |
| Capitalized interest | — | — | — | — | — | — | — | — | 8 | 6 | 11 | 20 | 12 | 12 |

**CFO row, FY2013–FY2015:** `NetCashProvidedByUsedInOperatingActivities` has no full-year duration facts
before FY2016 on the companyconcept endpoint, so those three years were read directly out of the filed
statements: FY2014 10-K (accession 0000097476-15-000003, `txn-12312014x10xk.htm`) gives "Cash flows from
operating activities | 3,892 | 3,384 | 3,414" for 2014/2013/2012; FY2015 10-K (accession
0001564590-16-013126, `txn-10k_20151231.htm`) gives $4,268 for 2015. **Operator rule 4 satisfied: the filing
was read, not the tag.**

**Free cash flow row:** *italicised* figures are printed in the filings themselves —
$2,972 (2013) and $3,507 (2014) from the FY2014 10-K non-GAAP table, $3,717 (2015) from the FY2015 10-K,
$1,498 (2024) and $2,938 (2025) from the FY2025 10-K, $6,534 (TTM 6/30/26) from the Q2 2026 10-Q. Roman
figures for 2016–2023 are computed here as CFO − capex, which was TI's own definition in those years;
they are **derived, not transcribed**. Note the definition change: from FY2025 TI adds "proceeds from CHIPS
Act incentives" to the numerator (+$335M in 2025, +$1,179M in the TTM), so the 2024–TTM figures are not
computed on the same basis as the 2013–2023 figures. On the pre-2025 definition, FY2025 free cash flow
would be **$2,603M** and the TTM would be **$5,355M**.

## RATIOS

| ratio | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | TTM |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Capex / revenue | 3.4% | 3.0% | 4.2% | 4.0% | 4.6% | 7.2% | 5.9% | 4.5% | 13.4% | 14.0% | 28.9% | 30.8% | 25.7% | 17.0% |
| **Capex / depreciation** | 47% | 45% | 72% | 88% | 129% | 192% | 120% | 89% | 326% | 302% | **432%** | 320% | 237% | 156% |
| Depreciation / revenue | 7.2% | 6.5% | 5.9% | 4.5% | 3.6% | 3.7% | 4.9% | 5.1% | 4.1% | 4.6% | 6.7% | 9.6% | 10.8% | 10.9% |
| Gross margin | 52.1% | 56.9% | 58.2% | 61.6% | 64.3% | 65.1% | 63.7% | 64.1% | 67.5% | 68.8% | 62.9% | 58.1% | 57.0% | 58.3% |
| Operating margin | 23.2% | 30.3% | 32.9% | 35.9% | 40.7% | 42.5% | 39.8% | 40.8% | 48.8% | 50.6% | 41.8% | 34.9% | 34.1% | 37.3% |
| CFO / revenue | — | — | — | 34.5% | 35.8% | 45.5% | 46.2% | 42.5% | 47.7% | 43.5% | 36.6% | 40.4% | 40.5% | 44.6% |

## THE HALF-YEAR SPLIT THAT DRIVES THE TTM

| $ millions | H1 2025 | H1 2026 | change |
|---|---|---|---|
| Revenue | 8,517 | 10,288 | +20.8% |
| Gross profit | 4,888 | 6,151 | +25.8% |
| Operating profit | 2,887 | 4,118 | +42.6% |
| Net income | 2,474 | 3,525 | +42.5% |
| Cash flow from operations | 2,709 | 4,223 | +55.9% |
| **Capital expenditures** | **2,428** | **1,190** | **−51.0%** |
| **Depreciation** | **884** | **1,088** | **+23.1%** |
| R&D | 1,044 | 1,045 | +0.1% |
| Share-based compensation | 245 | 236 | −3.7% |

All from the Q2 2026 10-Q, accession 0000097476-26-000152, filed 2026-07-24.

---

## WHAT THE SERIES SHOWS

1. **The capex cycle has a shape and it is now clearly rolling over.** Baseline 2013–2020 was
$385M–$1,131M, averaging ~$650M, or 3–7% of revenue. From FY2021 the company steps to $2.5B, then $2.8B,
then a $5.07B peak in FY2023, $4.82B, $4.55B — **$19.70 billion over FY2021–FY2025**, against **$3.85
billion** across the preceding five years FY2016–FY2020. FY2016–FY2025 sums to **$23.55 billion**, which is
TI's own "about $24 billion to capital expenditures" over "a 10-year period from 2016 to 2025" — the two
agree, and note that TI's headline figure is a **ten**-year total, not the six-year cycle total. With the
guided $2–3bn for 2026, the full six-year elevated cycle FY2021–FY2026 will total roughly **$22 billion**. H1 2026 capex is $1,190M, an annualized $2.4B, inside the guided
$2–3B band and consistent with the guidance being met.

2. **Depreciation has not caught up and is still climbing.** Depreciation runs $539M–$925M through FY2022,
then $1,175M / $1,508M / $1,918M / $2,122M TTM. It is up 2.3x since FY2022 while revenue is down 3%.
Capex/depreciation is falling toward 1.0x from a 4.3x peak — the crossover has not happened yet but
is now visible. Depreciation is also being **held down** by the CHIPS Act asset-basis reduction: $353M of
2025 depreciation was suppressed by the credit (see `10k-findings.md` §2C), so gross-of-subsidy
depreciation was ~$2,271M in 2025, i.e. 12.8% of revenue rather than 10.8%.

3. **A maintenance-capex question sits underneath this.** TI does not disclose maintenance vs growth
capex anywhere in the filings — the split is UNRESEARCHED and there is no document in the SEC record that
resolves it. The two visible anchors are: (a) FY2013–FY2020 average capex of $650M on ~$14B of revenue
against depreciation of $500–900M in the same years, and (b) the FY2026 guided $2–3B on a $19.5B TTM
revenue base against $2.1B of TTM depreciation. Whether the guided 2026 number is a maintenance floor or
a trough is exactly the judgment the filings do not make for you.

4. **Buyback discipline vanished during the build and has not returned.** Repurchases ran $2.1–5.1B/yr
FY2013–FY2020 and collapsed to $527M / $3,615M / $293M / $929M / $1,477M in FY2021–FY2025, and to $707M
TTM. Dividends did the opposite: $4,557M / $4,795M / $4,999M in FY2023/24/25, exceeding net income in
FY2024 ($4,799M) and effectively equalling it in FY2025 ($5,001M vs $4,999M). Retained earnings fell
$26M in 2025 ($52,262M to $52,236M) — the company paid out more than it earned once dividend equivalents
on RSUs are counted.

5. **The build was debt-financed.** Long-term debt went from ~$5.8B pre-cycle to $14,048M total debt at
2025-12-31 ($13,548M long-term + $500M current). Interest and debt expense $353M / $508M / $543M in
2023/24/25. Cash and short-term investments fell from $7.58B to $4.88B during 2025.

6. **A $7.5B acquisition lands on top of the tail of the cycle.** Silicon Labs, announced 2026-02-04,
all cash, expected close H1 2027, to be funded with cash on hand plus debt; a $5B 364-day delayed-draw
term loan was arranged in June 2026. See `acquisitions.md`.

## PROVENANCE — capex figures by accession

| FY | form | accession | filed |
|---|---|---|---|
| 2013 | 10-K | 0000097476-14-000007 | 2014-02-24 |
| 2014 | 10-K | 0000097476-15-000003 | 2015-02-24 |
| 2015 | 10-K | 0001564590-16-013126 | 2016-02-24 |
| 2016 | 10-K | 0001564590-17-002142 | 2017-02-23 |
| 2017 | 10-K | 0001564590-18-002832 | 2018-02-22 |
| 2018 | 10-K | 0001564590-19-003839 | 2019-02-22 |
| 2019 | 10-K | 0000097476-20-000009 | 2020-02-20 |
| 2020 | 10-K | 0000097476-21-000006 | 2021-02-05 |
| 2021 | 10-K | 0000097476-22-000009 | 2022-02-04 |
| 2022 | 10-K | 0000097476-23-000007 | 2023-02-03 |
| 2023 | 10-K | 0000097476-24-000007 | 2024-02-02 |
| 2024 | 10-K | 0000097476-25-000007 | 2025-02-14 |
| 2025 | 10-K | 0000097476-26-000059 | 2026-02-06 |
| TTM | 10-Q | 0000097476-26-000152 | 2026-07-24 |

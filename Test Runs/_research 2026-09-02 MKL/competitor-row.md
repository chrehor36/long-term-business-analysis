# MKL COMPETITOR ROW — primary filings only

**Research date:** 2026-09-02
**Rule applied:** SEC EDGAR primary documents (10-K, 40-F) only. No aggregators.
Every figure carries the accession number of the document it was taken from.
Where a figure could not be obtained from a primary filing it reads
**NOT OBTAINED — <reason>**. Absence is recorded as a finding, never estimated.

**SEC requests made with** `User-Agent: Chris Hrehor chrehor36@gmail.com`

---

## 1. CIK RESOLUTION (source: https://www.sec.gov/files/company_tickers.json)

| Ticker | CIK | Registrant name as filed |
|---|---|---|
| MKL | 1096343 | MARKEL GROUP INC. |
| WTM | 776867 | WHITE MOUNTAINS INSURANCE GROUP LTD |
| RLI | 84246 | RLI CORP |
| KNSL | 1669162 | Kinsale Capital Group, Inc. |
| AXS | 1214816 | AXIS CAPITAL HOLDINGS LTD |
| WRB | 11544 | BERKLEY W R CORP |
| ACGL | 947484 | ARCH CAPITAL GROUP LTD. |
| FFH | 915191 | FAIRFAX FINANCIAL HOLDINGS LTD/ CAN (files 40-F) |
| BRK-B | 1067983 | BERKSHIRE HATHAWAY INC |

*(status: gathering — sections below are appended as each filing is read)*

---

## 2. GAAP CONSOLIDATED COMBINED RATIO — 5-YEAR SERIES (2021-2025)

Metric definition as filed: loss ratio + expense ratio, on a GAAP basis, consolidated
(not segment). Where a registrant does not publish a consolidated GAAP combined ratio,
the block records **NOT REPORTED** and states what is published instead.

### W. R. Berkley Corporation (WRB) — CIK 11544

| 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean |
|---|---|---|---|---|---|
| 89.6 | 89.3 | 89.7 | 90.3 | 90.7 | **89.92** |

Reported as "Consolidated / GAAP combined ratio" and as the "Total" line of the GAAP
underwriting-ratio table in Item 7 MD&A. Definition given in the filing: "Combined ratio
is the sum of the loss ratio and the expense ratio... A number in excess of 100 indicates
an underwriting loss; a number below 100 indicates an underwriting profit."

- 2025, 2024, 2023: FY2025 10-K, accession **0000011544-26-000005** (`wrb-20251231.htm`)
- 2023, 2022, 2021: FY2023 10-K, accession **0000011544-24-000005** (`wrb-20231231.htm`)
- 2023 cross-checks at 89.7 in both filings.

### RLI Corp. (RLI) — CIK 84246

| 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean |
|---|---|---|---|---|---|
| 86.8 | 84.4 | 86.6 | 86.2 | 83.6 | **85.52** |

Full five-year series taken from a single table, Item 1 "COMBINED RATIO AND STATUTORY
COMBINED RATIO", FY2025 10-K. Loss ratio / expense ratio / combined ratio by year:
45.0/38.6/83.6 (2025), 48.4/37.8/86.2 (2024), 46.7/39.9/86.6 (2023), 44.9/39.5/84.4 (2022),
46.5/40.3/86.8 (2021). The filing states these components are "presented in our GAAP
consolidated financial statements". RLI also publishes a separate *statutory* combined
ratio; the GAAP figure is the one recorded here.

- All five years: FY2025 10-K, accession **0001104659-26-018013** (`rli-20251231x10k.htm`)
- Filing also states a 30-year average combined ratio of 87.9 and a 30th consecutive year
  of underwriting profit in 2025.

### Kinsale Capital Group, Inc. (KNSL) — CIK 1669162

| 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean |
|---|---|---|---|---|---|
| 77.1 | 78.5 | 75.4 | 76.4 | 75.9 | **76.66** |

Kinsale's MD&A key-metrics table carries only two years per filing, so this series is
assembled from four 10-Ks with each year cross-checked in two filings where possible.

- 2025 (75.9) and 2024 (76.4): FY2025 10-K, accession **0001669162-26-000015**
- 2024 (76.4) and 2023 (75.4): FY2024 10-K, accession **0001669162-25-000010**
- 2023 (75.4) and 2022 (78.5): FY2023 10-K, accession **0001669162-24-000006**
- 2022 (77.9) and 2021 (77.1): FY2022 10-K, accession **0001669162-23-000009**

**Restatement flag — 2022.** The FY2022 10-K reports 2022 at **77.9** (loss 57.7, expense
20.2). The FY2023 10-K reports the same year at **78.5** (loss 56.3, expense 22.2). The
denominator definition changed between the two filings: FY2022 defines the loss ratio
against "net earned premiums"; FY2023 defines it against "the sum of net earned premiums
and fee income". The table above uses the later (78.5) basis for 2022 for comparability
with 2023-2025. **2021 (77.1) is only available on the older basis** and is therefore not
strictly comparable to the four later years. The five-year mean on the mixed basis is
76.66; using the older-basis 77.9 for 2022 it would be 76.54.

Definition as filed: "Combined ratio is the sum of the loss ratio and the expense ratio as
presented. A combined ratio under 100% indicates an underwriting profit."

### AXIS Capital Holdings Limited (AXS) — CIK 1214816

| 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean |
|---|---|---|---|---|---|
| 97.5 | 95.8 | 99.9 | 92.3 | 89.8 | **95.06** |

Consolidated combined ratio from the "Combined Ratio — The components of the combined
ratio were as follows" table in Item 7 MD&A. Built from the sum of net losses and loss
expenses ratio + acquisition cost ratio + general and administrative expense ratio, where
the G&A ratio includes unallocated corporate expenses (2.0% in 2025, 2.4% 2024, 2.6% 2023,
2.5% 2022, 2.7% 2021), so this is the consolidated and not the segment-sum figure.

- 2025, 2024, 2023: FY2025 10-K, accession **0001214816-26-000097** (`axs-20251231.htm`)
- 2023, 2022, 2021: FY2023 10-K, accession **0001214816-24-000024** (`axs-20231231.htm`)
- 2023 cross-checks at 99.9 in both filings.

Note on the 2023 spike: driven by an 8.1% adverse prior-year reserve development ratio
(vs (0.5)% in 2022), concentrated in the Reinsurance segment, whose 2023 combined ratio
was 107.6.

### Arch Capital Group Ltd. (ACGL) — CIK 947484

| 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean |
|---|---|---|---|---|---|
| 85.2 | 81.6 | 79.3 | 82.5 | 82.8 | **82.28** |

Source is the "Underwriting Ratios" block of the segment note (note 4, Segment
Information) in Item 8, **Total** column. Arch's segment table runs
Insurance | Reinsurance | Mortgage | Sub-Total | Other | Total. The Total column is the
consolidated underwriting total; corporate expenses, amortisation, interest and FX sit
below the underwriting line and are **not** in the ratio. Segment detail:

| | Insurance | Reinsurance | Mortgage | Sub-total | Other | Total |
|---|---|---|---|---|---|---|
| 2025 | 95.2 | 80.8 | 14.6 | — | n/a | 82.8 |
| 2024 | 94.8 | 83.2 | 12.6 | — | n/a | 82.5 |
| 2023 | 91.7 | 81.4 | 9.3 | — | — | 79.3 |
| 2022 | 95.0 | 92.2 | (7.7) | — | — | 81.6 |
| 2021 | 96.7 | 94.2 | 27.1 | 84.3 | 106.8 | 85.2 |

**Comparability flag — 2021.** 2021 is the only year with a populated "Other" column
(Watford Holdings, consolidated until its sale). Consolidated Total is 85.2; the
three-segment Sub-Total excluding Watford is **84.3**. The table above uses the
consolidated 85.2. On the Sub-Total basis for 2021 the five-year mean would be 82.10.

- 2025, 2024, 2023: FY2025 10-K, accession **0000947484-26-000017** (`acgl-20251231.htm`)
- 2023, 2022, 2021: FY2023 10-K, accession **0000947484-24-000020** (`acgl-20231231.htm`)
- 2023 cross-checks at 79.3 in both filings.

### White Mountains Insurance Group, Ltd. (WTM) — CIK 776867

| 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

**NOT REPORTED — White Mountains publishes no consolidated GAAP combined ratio.** It
publishes a combined ratio only for its insurance/reinsurance segment (Ark/WM Outrigger)
and, historically, for HG Global/BAM. There is no consolidated figure to report because
most of the group is not an insurance underwriter.

Reportable segments per the FY2025 10-K: "(1) Ark/WM Outrigger, (2) HG Global, (3) Kudu
and (4) Distinguished, with its remaining operating businesses, holding companies and
other assets included in Other Operations." Kudu is an asset-management capital provider,
Distinguished is an MGA/distribution business, HG Global is financial-guarantee
reinsurance. A group combined ratio across those is not a meaningful or a filed number.

What it does report — **Ark/WM Outrigger segment combined ratio**, from the "Combined
Ratio" table in Item 7:

| 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean |
|---|---|---|---|---|---|
| 87.4 | 81.8 | 79.6 | 81.8 | 81.4 | **82.40** |

Note 2021 and 2022 are Ark alone (WM Outrigger Re did not exist as a column until 2023);
2023-2025 are the Ark + WM Outrigger Re total, with Ark alone at 82.4 (2023), 83.1 (2024)
and 82.7 (2025). This is a **segment** ratio and is not the same construct as the
consolidated GAAP combined ratios recorded for WRB, RLI, KNSL, AXS and ACGL above.

- 2025, 2024, 2023: FY2025 10-K, accession **0001628280-26-012603** (`wtm-20251231.htm`)
- 2023, 2022, 2021: FY2023 10-K, accession **0000776867-24-000005** (`wtm-20231231.htm`)
- 2023 cross-checks at 79.6 in both filings.

### Fairfax Financial Holdings Limited (FFH) — CIK 915191, files 40-F

| 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean |
|---|---|---|---|---|---|
| 95.0 | 94.7 | 93.2 | 92.7 | 93.0 | **93.72** |

**NOT REPORTED AS US GAAP — Fairfax reports under IFRS, not US GAAP, and the combined
ratio it publishes is a non-GAAP supplementary measure covering only the property and
casualty insurance and reinsurance operations, not the consolidated group.** The figures
above are Fairfax's **undiscounted** combined ratio, which the filing calls "a traditional
performance measure of underwriting results within the property and casualty industry" and
which is the closest construct to the US GAAP combined ratios recorded above. Three
caveats:

1. **IFRS, not US GAAP.** Statements are "prepared in accordance with International
   Financial Reporting Standards as issued by the International Accounting Standards
   Board." A 40-F filer is not required to reconcile to US GAAP.
2. **Basis break at 2022.** IFRS 17 applies from 2022 (adopted 1 January 2023, 2022
   restated); 2021 is on the IFRS 4 basis. The FY2025 float table states the convention
   explicitly: "IFRS 17 basis for 2022 to 2025; IFRS 4 basis for 2010 to 2021."
3. **Scope.** The ratio covers the P&C insurance and reinsurance operations only. Life
   insurance and Run-off is excluded, as are the non-insurance companies. Fairfax's MD&A
   note (2) states: "Life insurance and Run-off is included in references to the insurance
   and reinsurance companies and excluded in references to the property and casualty
   insurance and reinsurance companies."

Fairfax also publishes a **discounted** combined ratio under IFRS 17 — "calculated as net
insurance service expenses expressed as a percentage of net insurance revenue" — which is
materially lower and is **not** comparable to a US GAAP combined ratio:
83.9 (2025), 81.4 (2024), 81.0 (2023), 84.6 (2022); no IFRS 17 discounted figure for 2021.

Segment detail on the undiscounted ratio (North American Insurers | Global Insurers and
Reinsurers | International Insurers and Reinsurers | Consolidated P&C):
2025 — 93.8 | 92.1 | 94.7 | **93.0**; 2024 — 93.7 | 91.0 | 97.3 | **92.7**;
2023 — 95.2 | 91.7 | 95.9 | **93.2**; 2022 — 92.9 | 94.8 | 99.3 | **94.7**.

- 2025, 2024: FY2025 40-F, accession **0001104659-26-024781**, Exhibit 99.3 (MD&A),
  `ffh-20251231xex99d3.htm`. The 40-F primary document itself contains no combined ratio.
- 2023, 2022: FY2023 40-F, accession **0001104659-24-032469**, Exhibit 99.3,
  `ffh-20231231xex99d3.htm`
- 2021: FY2021 40-F, accession **0001104659-22-030659**, Exhibit 99.3,
  `ffh-20211231xex99d3.htm`, from the text: "The consolidated combined ratio of the
  property and casualty insurance and reinsurance operations was 95.0% in 2021, producing
  an underwriting profit of $801.2 despite catastrophe and COVID-19 losses of $1,203.2
  (representing 7.5 combined ratio points)."

---

## 3. SUMMARY — GAAP CONSOLIDATED COMBINED RATIO, 2021-2025

| Company | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean | Basis |
|---|---|---|---|---|---|---|---|
| RLI | 86.8 | 84.4 | 86.6 | 86.2 | 83.6 | **85.52** | US GAAP consolidated |
| KNSL | 77.1 | 78.5 | 75.4 | 76.4 | 75.9 | **76.66** | US GAAP consolidated; 2022 restated basis, 2021 old basis |
| WRB | 89.6 | 89.3 | 89.7 | 90.3 | 90.7 | **89.92** | US GAAP consolidated |
| ACGL | 85.2 | 81.6 | 79.3 | 82.5 | 82.8 | **82.28** | US GAAP consolidated (segment-note Total) |
| AXS | 97.5 | 95.8 | 99.9 | 92.3 | 89.8 | **95.06** | US GAAP consolidated |
| FFH | 95.0 | 94.7 | 93.2 | 92.7 | 93.0 | **93.72** | **IFRS**, undiscounted, P&C ops only |
| WTM | — | — | — | — | — | — | **NOT REPORTED** at group level |
| WTM (Ark/WM Outrigger segment only) | 87.4 | 81.8 | 79.6 | 81.8 | 81.4 | *82.40* | segment ratio, not consolidated |

**Two of the seven do not have the metric as specified.** White Mountains publishes no
consolidated combined ratio at all — its group spans asset management (Kudu),
distribution (Distinguished) and financial guarantee (HG Global) alongside Ark, so the
number does not exist in its filings. Fairfax publishes one, but under IFRS rather than
US GAAP, on a scope limited to the P&C operations, and with a basis break between 2021
(IFRS 4) and 2022-2025 (IFRS 17).

Comparability caveats worth carrying forward: KNSL's 2021 sits on a superseded
denominator; ACGL's 2021 includes the consolidated Watford stub (84.3 excluding it); AXS
2021-2022 predates its exit from property reinsurance.

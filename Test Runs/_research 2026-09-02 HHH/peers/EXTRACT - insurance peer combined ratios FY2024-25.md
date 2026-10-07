# EXTRACT - Specialty insurance peer combined ratios and GWP, FY2025 and FY2024

**Purpose:** competitor row inputs for the HHH / Vantage run (Q2 franchise test).
**Nature:** TRANSCRIPTION ONLY. No conclusions drawn. All figures are GAAP, from each
company's FY2025 Form 10-K (fiscal year ended 2025-12-31), retrieved from SEC EDGAR
2026-09-03. Source HTML saved in this folder as `{TICKER}_10K_FY2025.htm`; stripped
text as `{TICKER}_text.txt`.

## Main table

| Ticker | FY2025 combined | FY2024 combined | FY2025 GWP ($M) | FY2024 GWP ($M) | Accession no. |
|---|---|---|---|---|---|
| KNSL | 75.9% | 76.4% | 1,977.2 | 1,870.3 | 0001669162-26-000015 |
| ACGL (consolidated, incl. mortgage) | 82.8% | 82.5% | 22,878 | 21,511 | 0000947484-26-000017 |
| ACGL - insurance segment only | 95.2% | 94.8% | 10,435 | 9,053 | 0000947484-26-000017 |
| ACGL - reinsurance segment only | 80.8% | 83.2% | 11,149 | 11,112 | 0000947484-26-000017 |
| WRB (consolidated) | 90.7% | 90.3% | 15,105.1 | 14,211.1 | 0000011544-26-000005 |
| AXS (consolidated) | 89.8% | 92.3% | 9,644.5 | 9,005.9 | 0001214816-26-000097 |
| RLI (consolidated) | 83.6% | 86.2% | 2,026.8 | 2,013.0 | 0001104659-26-018013 |
| **Vantage (subject, reference row)** | **95.3%** | **102.1%** | **1,624.7** | **1,397.0** | n/a (constructed from audited statements; per operator, not verified here) |

ACGL's consolidated total includes the mortgage segment (combined ratio 14.6% FY2025,
12.6% FY2024; GWP $1,305M / $1,351M), which is not comparable to a specialty P&C book;
the segment rows are given so the operator can choose the comparison basis. Segment GWP
rows include intersegment amounts, so they do not sum exactly to the consolidated total
(eliminations per filing footnote (1)).

## Ratio components (as reported)

| Ticker | FY2025 loss | FY2025 expense | FY2024 loss | FY2024 expense |
|---|---|---|---|---|
| KNSL | 55.1% | 20.8% | 55.8% | 20.6% |
| ACGL (consolidated) | 54.9% | 18.5% acq + 9.4% opex | 55.2% | 17.6% acq + 9.7% opex |
| WRB (consolidated) | 62.4% | 28.3% | 61.8% | 28.5% |
| AXS (consolidated) | 57.5% | 19.9% acq + 12.4% G&A | 59.5% | 20.2% acq + 12.6% G&A |
| RLI (consolidated) | 45.0% | 38.6% | 48.4% | 37.8% |

## Figure locations (verifiability, per the two-minute standard)

| Ticker | Combined ratio location | GWP location |
|---|---|---|
| KNSL | MD&A, "Results of Operations" summary table, p. 44 (`knsl-20251231.htm`); ratios confirmed in narrative below the table | Same MD&A table ($1,977,171K / $1,870,341K); also Item 1 division table and income statement |
| ACGL | Notes to Consolidated Financial Statements, Segment Information note, "Underwriting Ratios" rows of the FY2025 table (p. 122) and FY2024 table (p. 123) (`acgl-20251231.htm`); segment ratios also in MD&A segment tables | Same segment note tables, "Gross premiums written" row, Total column ($ millions) |
| WRB | MD&A, "Business Segment Results" table, p. 54 (`wrb-20251231.htm`), rows "GAAP combined ratio", Consolidated block | Same table, "Gross premiums written", Consolidated block ($15,105,069K / $14,211,090K) |
| AXS | MD&A, "Combined Ratio" components table, p. 64 (`axs-20251231.htm`) | MD&A "Underwriting Revenues" table ($9,644,514K / $9,005,888K); same totals in segment note |
| RLI | MD&A, "Underwriting Results" narrative ("$264 million on an 83.6 combined ratio in 2025, compared to $211 million on an 86.2 combined ratio in 2024"), p. 38 (`rli-20251231x10k.htm`); loss 45.0/48.4 and expense 38.6/37.8 in same section; 5-year GAAP ratio table also in Item 1, p. 10 | MD&A, "Gross Premiums Written and Net Premiums Earned" table, Grand total row ($2,026,846K / $2,013,048K) |

## Filing register

| Ticker | CIK | Form | Filed | Period | Primary document |
|---|---|---|---|---|---|
| KNSL | 0001669162 | 10-K | 2026-02-20 | 2025-12-31 | knsl-20251231.htm |
| ACGL | 0000947484 | 10-K | 2026-02-26 | 2025-12-31 | acgl-20251231.htm |
| WRB | 0000011544 | 10-K | 2026-02-27 | 2025-12-31 | wrb-20251231.htm |
| AXS | 0001214816 | 10-K | 2026-02-27 | 2025-12-31 | axs-20251231.htm |
| RLI | 0000084246 | 10-K | 2026-02-20 | 2025-12-31 | rli-20251231x10k.htm |

## Transcription notes

- All five FY2025 10-Ks were filed, so no substitute windows were needed.
- Arithmetic check: each combined ratio equals the sum of its reported components
  (KNSL 55.1+20.8=75.9; ACGL 54.9+18.5+9.4=82.8; WRB 62.4+28.3=90.7;
  AXS 57.5+19.9+12.4=89.8; RLI 45.0+38.6=83.6). Component sums may differ from the
  reported combined ratio by rounding per each filer's own footnote.
- WRB labels its ratios "GAAP combined ratio" explicitly. RLI presents both GAAP and
  statutory ratios; the figures above are the GAAP series (the statutory table is
  separately labeled in Item 1). KNSL, ACGL and AXS present a single (GAAP) series.
- AXS ratio denominators: loss and acquisition ratios on net premiums earned; the G&A
  ratio includes corporate expenses not allocated to segments (2.0% FY2025, 2.4% FY2024
  per filing footnote), so the consolidated combined ratio is not a pure underwriting
  segment ratio.
- Vantage row is included for calibration exactly as supplied by the operator and was
  not verified in this extract.

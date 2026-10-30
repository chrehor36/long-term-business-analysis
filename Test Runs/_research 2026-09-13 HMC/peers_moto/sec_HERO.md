---
## 3. Hero MotoCorp Ltd (NSE: HEROMOTOCO; BSE 500182) - not an SEC filer; fiscal year ends March 31 (FY3/22 = "FY 2021-22")

**Rung used:** company annual reports (English), downloaded from the company IR site (heromotocorp.com); the FY 2025-26
report was, per the company's own filing history, submitted to NSE/BSE (exchange filing copy not separately retrieved).
**All figures STANDALONE** (Hero MotoCorp Ltd), INR crore (1 crore = 10 million), units in lakh (1 lakh = 100,000).

**Segment (brief check):** Hero has no motorcycle segment. FY 2025-26 AR standalone note: "Therefore, based on the guiding principles given in Ind AS 108 on 'Operating Segments', the Company's business activity fall within a single operating segment, namely automotive segment." So "segment" = whole standalone company. No segment assets disclosed.

**Documents**
| Short name | Document | FYE | Published | URL |
|---|---|---|---|---|
| HERO-AR-26 | Integrated Annual Report 2025-26 | 2026-03-31 | filed with exchanges July 2026 (43rd AGM 2026-08-05) | https://www.heromotocorp.com/content/dam/hero-aem-website/in/en-in/company-section/investors/annual-report/annual-reports/2025-26/Hero_MotoCorp_IR_25_26_Web_final_v2_hq.pdf |
| HERO-AR-25 | Annual Report 2024-25 | 2025-03-31 | 2025 | https://www.heromotocorp.com/content/dam/hero-aem-website/in/en-in/company-section/investors/annual-report/annual-reports/2024-2025/hero_motocorp_ir_2024_25_c2c_v3.pdf |
| HERO-AR-24 | Annual Report 2023-24 | 2024-03-31 | 2024 | https://www.heromotocorp.com/content/dam/hero-aem-website/in/en-in/company-section/investors/annual-report/annual-reports/2023-2024/Hero_MotoCorp_AR_23-24_Web_final.pdf |
| HERO-AR-23 | Annual Report 2022-23 | 2023-03-31 | 2023 | https://www.heromotocorp.com/content/dam/hero-aem-website/in/investors/financial-results/annual-reports/annual-reports/Annual_Report_2022-23.pdf |

PDFs saved in `peers_moto/hero/` (text read page-by-page with pymupdf; page numbers below are PDF page indices). Publication date of each PDF: not printed on the pages read; the "July 2026" exchange-submission date for HERO-AR-26 is from a web-search snippet used only to locate the file, NOT verified against the exchange filing.

### Figures (standalone)
| FY (Mar) | "Revenue from operations" (Directors' Report) | EBITDA as reported | D&A ("Depreciation and amortisation expenses") | "Operating Profit Margin (%)" (MD&A Key Financial Ratios) | Computed (EBITDA - D&A) / Revenue | Units: "clocked sales of ... lakh units" | Source |
|---|---|---|---|---|---|---|---|
| FY3/22 | 29,245.47 | "(EBIDTA) stood at ... 11.52%"; chart 3,369 | 649.75 | 9.30% | 9.30% | 49.44 | HERO-AR-23 p57, p60 |
| FY3/23 | 33,805.65 | 11.79%; chart 3,986 | 656.96 | 9.85% | 9.85% | 53.29 | HERO-AR-23 p57, p60; HERO-AR-24 p66-67 |
| FY3/24 | 37,455.72 | 14.03%; chart 5,256 | 711.41 | 12.13% | 12.13% | 56.21 | HERO-AR-24 p66-67 |
| FY3/25 | 40,756.37 | 14.40%; 5,867.67 | 775.86 | 12.49% | 12.49% | 58.99 | HERO-AR-25 p59, p61; HERO-AR-26 |
| FY3/26 | 46,830.14 | 6,870.76 (computed margin 6,870.76 / 46,830.14 = 14.67%) | 798.00 | 12.97% | 12.97% | 64.69 | HERO-AR-26 p103, p105 |

"Chart" EBITDA values (INR crore, rounded) are from HERO-AR-26 "PERFORMANCE REVIEW" chart: FY26 6,871 / FY25 5,868 / FY24 5,256 / FY23 3,986 / FY22 3,369.
Computation (`peers_moto/hero_calc.py`): e.g. FY3/26 (6,870.76 - 798.00) = 6,072.76 / 46,830.14 = 12.97%, equal to the reported "Operating Profit Margin (%)" in every year, i.e. the reported ratio behaves as EBITDA less D&A over revenue from operations, excluding other income. The AR pages read do NOT state the ratio's formula; this equivalence is an arithmetic observation, not a filed definition.
Verbatim label trail: HERO-AR-23 directors' report: "Earnings before Interest, Depreciation and Taxes (EBIDTA) stood at 11.79% in FY 2022-23, as compared to 11.52% in FY 2021-22." HERO-AR-26: "Earnings before Interest, Taxes, Depreciation and Amortisation (EBITDA) stood at H 6,870.76 crore as compared to H 5,867.67 crore in FY 2024-25" (the "H" is the PDF's rupee-glyph extraction artifact).
Revenue composition: Revenue from operations includes spare parts and other operating revenue, not only vehicles; no split was transcribed.
Cross-check: FY3/23 revenue 33,805.65 identical in HERO-AR-23 (current year) and HERO-AR-24 (prior year); FY3/25 58.99 lakh units identical in HERO-AR-25 and HERO-AR-26.

### Units
"Motorcycles and Scooters Sold (No. of units in lakhs)" (HERO-AR-26 MD&A): 64.69 (FY26), 58.99 (FY25). Standalone company sales (the documents read describe them as the Company's sales; domestic plus exports; no affiliate/JV inclusion is stated). HERO-AR-26 p33 split: "58.43 lakh Motorcycles sold", "6.26 lakh Scooters sold". In thousands: FY22 4,944 / FY23 5,329 / FY24 5,621 / FY25 5,899 / FY26 6,469.

### Market share and pricing (verbatim, HERO-AR-26)
- p33: "28.7% Two-wheeler ICE market share (domestic)"
- p96: "These concerted efforts culminated in the Company achieving its highest-ever market share of 90%+ in the Deluxe 100 segment ... Similarly, in the Entry motorcycles segment, Hero MotoCorp strengthened its leadership with a market share of 58.9%."
- p94 (industry, MD&A): "This compelled OEMs to implement strict cost-optimisation programmes and selectively pass on price increases to consumers to protect profitability."
- p103: "Operating Profit Margin (%): Operating profit margin for the year has increase from 12.49% to 12.97%. This improvement is primarily due to better realisation, effective cost control & value engineering."


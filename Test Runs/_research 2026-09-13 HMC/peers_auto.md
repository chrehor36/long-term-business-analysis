# HMC run: automobile competitor row, transcription only (2026-09-13)

TRANSCRIPTION ONLY. No conclusions are drawn in this file; the run author draws them.
Raw documents (text-extracted) are saved in `Test Runs/_research 2026-09-13 HMC/peers_auto/`.
GM, Ford, Tesla, Stellantis are NOT redone here: see `Test Runs/_research 2026-09-13 TM/peers/COMPETITOR ROW - five-year industrial margins.md` (read only).

Sections: 1 spot-check; 2 Toyota; 3 Nissan; 4 Hyundai; 5 BYD; 6 Suzuki; SUMMARY; NOT DISCLOSED / BLOCKED (at the end).

---

## 1. SPOT-CHECK of the TM competitor row (read only)

File checked: `Test Runs/_research 2026-09-13 TM/peers/COMPETITOR ROW - five-year industrial margins.md`.
Text files checked are in the same folder. Both text files carry a header saying they are LOCAL
COPIES of .htm files originally saved in `_research 2026-09-01 GM` (not a fresh EDGAR download
on 2026-09-13); the accession in each header matches the competitor row's source table.

**(a) GMNA 2025 revenue 154,317 and EBIT-adjusted 10,452: FOUND, MATCHES.**
`GM_10K_FY2025.txt` (header: `ACCESSION: 0001467858-26-000013`), text line 2354-2356, under
"Note 23. Segment Reporting", table "At and For the Year Ended December 31, 2025", columns
`GMNA | GMI | Cruise | GM Financial | Total Reportable Segments`:
```
Net sales and revenue | $ | 154,317 | $ | 13,427 | $ | 1 | $ | 17,060 | $ | 184,805 |
Earnings (loss) before interest and taxes-adjusted | $ | 10,452 | $ | 737 | $ | ( 273 ) | $ | 2,802 | $ | 13,718 |
```
Also in MD&A, text lines 595-596: `Total net sales and revenue | $ | 154,317 | $ | 157,509 | ...`
and `EBIT-adjusted | $ | 10,452 | $ | 14,528 | $ | (4,077) | (28.1) | % | ...`.
Cross-foot (computed): 154,317 + 13,427 + 1 + 17,060 = 184,805 (matches the Total column).

**(b) Stellantis 2025 consolidated shipments 5,484: FOUND, MATCHES.**
`STLA_20F_FY2025.txt` (header: `ACCESSION: 0001605484-26-000021`), text lines ~2389-2420,
table "(thousands of units) | 2025 | 2024":
```
Total Consolidated shipments
 | 5,484
 | 5,415
```
Exact label is "Total Consolidated shipments" (the competitor row's column header uses that label).
Also line 360: "• 5,484 thousand vehicles shipped (refer to Financial Overview - Shipment
Information included elsewhere in ...". And the segment table (lines ~3380-3405) carries 5,484 in
both the "Total Segments" and "Total" rows. Cross-foot (computed): 1,472 + 2,490 + 453 + 1,000 +
61 + 8 = 5,484.

---

## 2. TOYOTA (Toyota Motor Corporation, CIK 1094517), JPY millions, IFRS

**Sources.** Local text copies in `Test Runs/_research 2026-09-13 TM/` (read only). The text files
carry no accession header; the file-to-accession mapping is from `batch1.py` in that folder and
matches Toyota's `submissions.json` (form, filingDate, reportDate, primaryDocument):
| Short | Document | FYE | Filed | Accession | Local text |
|---|---|---|---|---|---|
| T-26 | Form 20-F `d101983d20f.htm` | 2026-03-31 | 2026-06-10 | 0001193125-26-264811 | `20F_FY2026.txt` |
| T-25 | Form 20-F `d925022d20f.htm` | 2025-03-31 | 2025-06-18 | 0001193125-25-142326 | `20F_FY2025.txt` |
| T-24 | Form 20-F `d807954d20f.htm` | 2024-03-31 | 2024-06-25 | 0001193125-24-167462 | `20F_FY2024.txt` |
| T-23 | Form 20-F `d360541d20f.htm` | 2023-03-31 | 2023-06-30 | 0001193125-23-179181 | `20F_FY2023.txt` |
| T-22 | Form 20-F `d696693d20f.htm` | 2022-03-31 | 2022-06-23 | 0001193125-22-179197 | `20F_FY2022.txt` |
A 20-F/A for FYE 2023-03-31 exists (filed 2024-02-06, 0001193125-24-024814); its local text
(`20FA_2024-02-06_FY2023.txt`) contains no segment table (0 hits for the note heading).

**Note heading (T-26):** "5. Segment information", "(2) Segment information". Segment name is
**"Automotive"** (not "Automotive operations"; Item 5 MD&A uses "Automotive Operations Segment").
Row labels: "Revenues from external customers", "Inter-segment revenues and transfers", "Total",
"Operating expenses", "Operating income". T-26 note (1): *"The operating segments reported below
are the segments of Toyota for which separate financial information is available and for which
operating income/loss amounts are evaluated regularly by executive management in deciding how to
allocate resources and in assessing performance."*

### Verbatim segment-table rows (cells joined with " | " by `peers_auto/cells.py`; columns are
Automotive | Financial services | All other | Inter-segment Elimination/Unallocated Amount | Consolidated)

T-26, "As of and for the year ended March 31, 2026":
```
Revenues from external customers | 45,201,924 | 4,819,003 | 664,026 | - | 50,684,952
Inter-segment revenues and transfers | 215,779 | 38,112 | 987,387 | ( 1,241,278) | -
Total | 45,417,703 | 4,857,115 | 1,651,412 | ( 1,241,278) | 50,684,952
Operating expenses | 42,640,654 | 4,005,394 | 1,519,333 | ( 1,246,644) | 46,918,736
Operating income | 2,777,049 | 851,722 | 132,079 | 5,366 | 3,766,216
```
T-26, "As of and for the year ended March 31, 2025":
```
Revenues from external customers | 42,996,299 | 4,437,827 | 602,578 | - | 48,036,704
Total | 43,199,865 | 4,481,180 | 1,447,114 | ( 1,091,455) | 48,036,704
Operating income | 3,940,278 | 683,519 | 181,194 | ( 9,405) | 4,795,586
```
T-26 (same in T-25 and T-24), "As of and for the year ended March 31, 2024":
```
Revenues from external customers | 41,080,731 | 3,447,195 | 567,399 | - | 45,095,325
Total | 41,266,204 | 3,484,198 | 1,368,164 | ( 1,023,242) | 45,095,325
Operating income | 4,621,475 | 570,023 | 175,241 | ( 13,805) | 5,352,934
```
T-25 (same in T-24 and T-23), "As of and for the year ended March 31, 2023":
```
Revenues from external customers | 33,776,870 | 2,786,679 | 590,749 | - | 37,154,298
Total | 33,820,000 | 2,809,647 | 1,224,943 | ( 700,293) | 37,154,298
Operating income | 2,180,637 | 437,516 | 103,451 | 3,420 | 2,725,025
```
T-24 (same in T-23 and T-22), "As of and for the year ended March 31, 2022":
```
Revenues from external customers | 28,531,993 | 2,306,079 | 541,436 | - | 31,379,507
Total | 28,605,738 | 2,324,026 | 1,129,876 | ( 680,133) | 31,379,507
Operating income | 2,284,290 | 657,001 | 42,302 | 12,104 | 2,995,697
```
**Restatement check:** every overlapping year is identical across the three 20-Fs that show it
(FY3/22 in T-22, T-23, T-24; FY3/23 in T-23, T-24, T-25; FY3/24 in T-24, T-25, T-26; FY3/25 in
T-25, T-26). None found. Also: T-26 MD&A text *"Toyota's sales revenues from its automotive
operations were ¥45,417.7 billion in fiscal 2026, ¥43,199.8 billion in fiscal 2025, and ¥41,266.2
billion in fiscal 2024."*

### Margins (computed, `peers_auto/calc.py TM`)
| FY ended Mar | Automotive Total | Automotive Operating income | Margin on Total | Automotive external | Margin on external |
|---|---|---|---|---|---|
| 2026 | 45,417,703 | 2,777,049 | 6.11% | 45,201,924 | 6.14% |
| 2025 | 43,199,865 | 3,940,278 | 9.12% | 42,996,299 | 9.16% |
| 2024 | 41,266,204 | 4,621,475 | 11.20% | 41,080,731 | 11.25% |
| 2023 | 33,820,000 | 2,180,637 | 6.45% | 33,776,870 | 6.46% |
| 2022 | 28,605,738 | 2,284,290 | 7.99% | 28,531,993 | 8.01% |
| pooled | 192,309,510 | 15,803,729 | 8.22% | 191,587,817 | 8.25% |
These match the TM run file's series (7.99 / 6.45 / 11.20 / 9.12 / 6.11; pooled 8.22).

### Units: exact label "Toyota's consolidated vehicle unit sales" (thousands of units)
Item 5 table introduced by: *"The following table sets forth Toyota's consolidated vehicle unit
sales by geographic market based on location of customers for the past three fiscal years."*
(T-26: "past two fiscal years"). Verbatim Total rows:
- T-26: `Thousands of units | Year ended March 31, | 2025 | 2026 | ... | Overseas total | 7,372 | 7,513 | Total | 9,362 | 9,595`
- T-25: `2023 | 2024 | 2025 | ... | Overseas total | 6,753 | 7,450 | 7,372 | Total | 8,822 | 9,443 | 9,362`
- T-24: `2022 | 2023 | 2024 | ... | Overseas total | 6,306 | 6,753 | 7,450 | Total | 8,230 | 8,822 | 9,443`
- T-23: `2021 | 2022 | 2023 | ... | Overseas total | 5,521 | 6,306 | 6,753 | Total | 7,646 | 8,230 | 8,822`

| FY ended Mar | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| Consolidated vehicle unit sales (000) | 8,230 | 8,822 | 9,443 | 9,362 | 9,595 |

Item 4 ("Markets, Sales and Competition") definition, T-26 and T-24 verbatim: *"The vehicle unit
sales below reflect vehicle sales made by Toyota to unconsolidated entities (recognized as sales
under Toyota's revenue recognition policy), including sales to unconsolidated distributors and
dealers. Vehicles sold by Daihatsu and Hino are included in the vehicle unit sales figures set
forth below."*
Artifacts flagged, not smoothed: T-24 Item 4 table prints North America FY2024 as **"2.816"**
(period, not comma; Item 5 table in the same filing prints 2,816). T-22 Item 4 table gives units
unrounded (FY3/22 Japan 1,924,185; North America 2,393,912; ...). Outside the window, T-22 Item 5
prints FY3/2020 Total **8,955**; the TM run file's decade table shows FY20 **8,959** (source for
that figure not checked here).

---

## 3. NISSAN (Nissan Motor Co., Ltd.; not an SEC registrant), JPY millions, Japanese GAAP

**Sources.** English translations of the Securities Report ("Yukashoken-Houkokusho"), Nissan
global IR site. URLs located by web search on nissan-global.com; fetched directly 2026-09-13, all
HTTP 200. Saved as `peers_auto/NISSAN_fr<year>.pdf` and `.txt` (PyMuPDF).
| Short | Cover title (verbatim) | FYE | Filing date (as stated in the report) | URL |
|---|---|---|---|---|
| N-26 | "Financial Information as of March 31, 2026 (The English translation of the "Yukashoken-Houkokusho" for the year ended March 31, 2026)" | 2026-03-31 | "June 22, 2026, the date of filing this Securities Report" | https://www.nissan-global.com/EN/IR/FINANCIAL_RESULTS/ASSETS/FR/2025/PDF/fr2025.pdf (193 pp.) |
| N-25 | same form, "as of March 31, 2025" | 2025-03-31 | "June 23, 2025" | https://www.nissan-global.com/EN/IR/FINANCIAL_RESULTS/ASSETS/FR/2024/PDF/fr2024.pdf (196 pp.) |
| N-24 | same form, "as of March 31, 2024" | 2024-03-31 | "June 28, 2024" | https://www.nissan-global.com/EN/IR/FINANCIAL_RESULTS/ASSETS/FR/2023/PDF/fr2023.pdf (192 pp.) |
| N-23 | same form, "as of March 31, 2023" | 2023-03-31 | "June 30, 2023" | https://www.nissan-global.com/EN/IR/FINANCIAL_RESULTS/ASSETS/FR/2022/PDF/fr2022.pdf (184 pp.) |
| N-22 | same form, "as of March 31, 2022" | 2022-03-31 | "June 30, 2022" | https://www.nissan-global.com/EN/IR/FINANCIAL_RESULTS/ASSETS/FR/2021/PDF/fr2021.pdf (165 pp.) |
Note: the URL folder year is the fiscal year START (fr2025 = year ended March 2026).

**Segment definition (N-26, "Segment information", verbatim):** *"Businesses of the Group are
segmented into Automobile and Sales financing based on the features of products and services. The
Automobile business includes manufacturing and sales of vehicles and parts. The Sales financing
business provides sales finance services and leasing to support the sales activities of the
Automobile business."* and *"The segment profits are based on operating income. Inter-segment
sales are based on the price in arm's length transactions."*
The brief said "net sales and operating profit/loss". The note's row labels are **"Net sales" /
"Sales to third parties" / "Inter-segment sales or transfers" / "Total"** and **"Segment profits
(losses)"** (N-22), **"Segment profits"** (N-23 FY3/23, N-24), **"Segment profits (loss)"** (N-25,
N-26 current year), **"Segment profit (loss)"** (N-26 prior year). The segment is named
**"Automobile"**. Columns: Automobile | Sales financing | Total | Elimination of inter-segment
transactions | consolidated ("The year ended March 31, 20xx").

### Verbatim segment-note rows (cells joined " | " from the PDF text)
N-26 PDF p.141, "Current fiscal year (From April 1, 2025 to March 31, 2026)":
```
Sales to third parties | 10,760,298 | 1,247,590 | 12,007,888 | ― | 12,007,888
Inter-segment sales or | transfers | 159,808 | 70,412 | 230,220 | (230,220) | ―
Total | 10,920,106 | 1,318,002 | 12,238,108 | (230,220) | 12,007,888
Segment profits (loss) | (292,890) | 297,942 | 5,052 | 52,953 | 58,005
```
N-25 PDF p.145, "Current fiscal year (From April 1, 2024 to March 31, 2025)" (identical in N-26 p.138):
```
Sales to third parties | 11,437,856 | 1,195,358 | 12,633,214 | ― | 12,633,214
Total | 11,645,478 | 1,262,081 | 12,907,559 | (274,345) | 12,633,214
Segment profits (loss) | (267,979) | 285,647 | 17,668 | 52,130 | 69,798
```
N-24 PDF p.139, "Current fiscal year (From April 1, 2023 to March 31, 2024)" (identical in N-25 p.142):
```
Sales to third parties | 11,582,863 | 1,102,853 | 12,685,716 | ― | 12,685,716
Total | 11,782,516 | 1,161,778 | 12,944,294 | (258,578) | 12,685,716
Segment profits | 221,574 | 308,718 | 530,292 | 38,426 | 568,718
```
N-23 PDF p.134, "Current fiscal year (From April 1, 2022 to March 31, 2023)" (identical in N-24 p.136):
```
Sales to third parties | 9,591,859 | 1,004,836 | 10,596,695 | ― | 10,596,695
Total | 9,686,842 | 1,023,825 | 10,710,667 | (113,972) | 10,596,695
Segment profits | 42,952 | 311,908 | 354,860 | 22,249 | 377,109
```
N-22 PDF p.118, "Current fiscal year (From April 1, 2021 to March 31, 2022)" (identical in N-23 p.131):
```
Sales to third parties | 7,420,892 | 1,003,693 | 8,424,585 | ― | 8,424,585
Total | 7,475,648 | 1,031,729 | 8,507,377 | (82,792) | 8,424,585
Segment profits (losses) | (155,059) | 374,824 | 219,765 | 27,542 | 247,307
```
**Restatement check:** every year appears in two reports with identical figures. None found.
Extra year (N-22 prior year, FY3/21): Automobile Total 6,989,028; segment profits (losses) (437,021).

**Two automobile operating figures exist in the same report; both recorded.** N-26 MD&A
("(Business segments) a. Automobile"), verbatim: *"Net sales in the automobile business (including
intersegment sales) for the current fiscal year totaled ¥10,920.1 billion, decreasing by ¥725.4
billion (6.2%) from the prior fiscal year. Operating loss totaled ¥292.9 billion, deteriorating by
¥24.9 billion from the prior fiscal year, affected by factors including U.S. tariffs and unfavorable
foreign exchange rates, largely offset by cost reductions."* and *"Operating loss in the automobile
business including elimination of inter-segment transactions for the current fiscal year totaled
¥239.9 billion."* The second figure corresponds to the "Automobile & Eliminations" presentation
(N-26 Note 1: *"The financial data on Automobile & Eliminations represents the differences between
the consolidated figures and those for the Sales financing segment."*). Computed here as consolidated
operating income less Sales financing segment profit: 58,005 - 297,942 = (239,937), matching
¥239.9bn. Sales financing composition (N-26 Note 1, verbatim): *"The Sales financing segment for
the summarized consolidated balance sheet, summarized consolidated statement of income and
summarized consolidated statement of cash flows consists of Nissan Financial Services Co., Ltd.
(Japan), Nissan Motor Acceptance Company LLC (U.S.A.), Nissan Financial Services Mexico (Mexico),
Dongfeng Nissan Auto Finance Co., Ltd. (China), 13 other companies and the sales finance operations
of Nissan Canada, Inc. (Canada)."*
N-26 segment note also records two estimate changes in FY3/26 that raised "Automobile &
Eliminations" operating income: software useful life *"an increase of ¥11,068 million in operating
income"*; accrued warranty costs *"an increase of ¥36,603 million in operating income"*.

### Margins (computed, `peers_auto/calc.py NISSAN`)
| FY ended Mar | Automobile Total net sales | Automobile segment profit (loss) | Margin on Total | Margin on sales to third parties | Memo: Automobile & Eliminations op. income (computed) | Memo margin (on third-party auto sales) |
|---|---|---|---|---|---|---|
| 2026 | 10,920,106 | (292,890) | (2.68)% | (2.72)% | (239,937) | (2.23)% |
| 2025 | 11,645,478 | (267,979) | (2.30)% | (2.34)% | (215,849) | (1.89)% |
| 2024 | 11,782,516 | 221,574 | 1.88% | 1.91% | 260,000 | 2.24% |
| 2023 | 9,686,842 | 42,952 | 0.44% | 0.45% | 65,201 | 0.68% |
| 2022 | 7,475,648 | (155,059) | (2.07)% | (2.09)% | (127,517) | (1.72)% |
| pooled | 51,510,590 | (451,402) | (0.88)% | (0.89)% | (258,102) | (0.51)% |

### Units (units; "Production, orders received and sales" tables in the MD&A section)
Two tables per report, verbatim labels **"c. Actual sales (on a retail basis)"** (column "Number
of vehicles sold (on a retail basis: units)") and **"d. Actual sales (on a consolidated basis)"**
("Number of vehicles sold (on a consolidated basis: units)"). Total rows (Prior | Current | change):
- N-26: retail `Total | 3,346,248 | 3,151,164 | (195,084) | (5.8)`; consolidated `Total | 2,656,592 | 2,434,516 | (222,076) | (8.4)`
- N-25: retail `Total | 3,442,257 | 3,346,248 | (96,009) | (2.8)`; consolidated `Total | 2,785,614 | 2,656,592 | (129,022) | (4.6)`
- N-24: retail `Total | 3,305,204 | 3,442,257 | 137,053 | 4.1`; consolidated `Total | 2,450,765 | 2,785,614 | 334,849 | 13.7`
- N-23: retail `Total | 3,875,986 | 3,305,204 | (570,782) | (14.7)`; consolidated `Total | 2,293,575 | 2,450,765 | 157,190 | 6.9`
- N-22: consolidated `Total | 2,471,344 | 2,293,575 | (177,769) | (7.2)`. FY3/22 retail in N-22 text: *"Global sales of the Group (on a retail basis) for the year ended March 31, 2022 decreased by 4.3% year on year to 3,876 thousand units."* (unit-level figure 3,875,986 taken from N-23's prior-year column)

| FY ended Mar | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| Actual sales, retail basis (units) | 3,875,986 | 3,305,204 | 3,442,257 | 3,346,248 | 3,151,164 |
| Actual sales, consolidated basis (units) | 2,293,575 | 2,450,765 | 2,785,614 | 2,656,592 | 2,434,516 |
Footnotes (verbatim, N-26 retail table): *"1. The figures in China and Taiwan, which are included in
"Asia," represent the sales figures for the 12-month period from January 1 to December 31, 2025.
Those sold in Japan, North America, Europe, Other overseas countries and Asia (excluding China and
Taiwan) represent vehicles sold for the 12-month period from April 1, 2025 to March 31, 2026. 2. The
figures in China include Chinese joint venture, Dongfeng Motor Co., Ltd."* Consolidated table note
2 (N-25, N-26): *"The figures in China exclude Chinese joint venture, Dongfeng Motor Co., Ltd."*
(N-23 and N-24 consolidated tables carry only note 1.) **The reports do not use the word
"wholesale" for the consolidated-basis table**; the label is recorded as written.
Retail China (included in Asia): FY3/23 1,045,197; FY3/24 793,768; FY3/25 696,631; FY3/26 653,024.
N-26 production note: *"As Renault Nissan Automotive India Pvt. Ltd. was deconsolidated from the
Group as of July 31, 2025, the results for India reflect actual performance only for the four months
from April through July 2025."*

---

## 4. HYUNDAI MOTOR COMPANY (not an SEC registrant), KRW millions, K-IFRS; units in thousands

**Sources (all from hyundai.com, fetched 2026-09-13, HTTP 200 unless stated).** Audited consolidated
financial statements URLs follow the pattern the TM run found; presentation URLs were returned by
Hyundai's own IR endpoint `POST https://www.hyundai.com/wsvc/ww/quarterlyResults.detail.do`
(`year=<y>&lang=en`, field `presentationValue`), which is the data source of the IR page
"Quarterly Earnings".
| Short | Document (cover, verbatim) | Period | Audit report date | URL | Saved |
|---|---|---|---|---|---|
| HY-FS25 | (TM run, read only) "Consolidated Financial Statements for each of the two years in the period ended December 31, 2025" | 2025, 2024 | March 4, 2026 (per TM file) | `.../report-en/2025/2025-q4-consolidated-audit-report-en.pdf` | `TM/peers/HYUNDAI_2025_audit.txt` |
| HY-FS24 | "CONSOLIDATED FINANCIAL STATEMENTS FOR EACH OF THE TWO YEARS IN THE PERIOD ENDED DECEMBER 31, 2024" | 2024, 2023 | "March 5, 2025" | https://www.hyundai.com/content/dam/hyundai/ww/en/images/company/investor-relations/financial-Information/report-en/2024/2024-q4-consolidated-audit-report-en.pdf (110 pp.) | `HYUNDAI_2024_audit.pdf/.txt` |
| HY-FS23 | "CONSOLIDATED FINANCIAL STATEMENTS FOR THE YEAR ENDED DECEMBER 31, 2023" (auditor "Ernst & Young Han Young") | 2023, 2022 | "March 6, 2024" | https://www.hyundai.com/content/dam/hyundai/ww/en/images/company/investor-relations/financial-Information/report-en/2023/2023-q4-consolidated-audit-report-en.pdf (110 pp.) | `HYUNDAI_2023_audit.pdf/.txt` |
| HY-FS22 | 2022 statements | 2022, 2021 | n/a | https://www.hyundai.com/content/dam/hyundai/ww/en/images/company/investor-relations/financial-Information/report-en/2022/2022-q4-consolidated-audit-report-en.pdf | **HTTP 404** (not retried under other names) |
| HY-FS21 | "CONSOLIDATED FINANCIAL STATEMENTS AS OF AND FOR THE YEARS ENDED DECEMBER 31, 2021 AND 2020" (engagement partner Sang-Min Nam; firm name not in extracted text) | 2021, 2020 | "March 8, 2022" | https://www.hyundai.com/content/dam/hyundai/ww/en/images/company/investor-relations/financial-Information/report-en/2021/2021-q4-consolidated-audit-report-en.pdf (91 pp.) | `HYUNDAI_2021_audit.pdf/.txt` |
| HY-PT25 | Q4 2025 earnings presentation | 2025 vs 2024 | n/a | https://www.hyundai.com/content/dam/hyundai/ww/en/images/company/investor-relations/ir-events/pdf/en/2026/q4-2025-earnings-call-pt-en.pdf (25 pp.) | `HYUNDAI_PT_2025Q4.*` |
| HY-PT24 | Q4 2024 earnings presentation | 2024 vs 2023 | n/a | https://www.hyundai.com/content/dam/hyundai/ww/en/images/company/investor-relations/financial-Information/presentation/en/24/Q4-2024-earnings-call-pt-en.pdf (23 pp.) | `HYUNDAI_PT_2024Q4.*` |
| HY-PT23 | Q4 2023 earnings presentation | 2023 vs 2022 | n/a | https://www.hyundai.com/content/dam/hyundai/ww/en/images/company/investor-relations/financial-Information/presentation/en/23/q4-2023-earnings-call-pt-en-v2.pdf (22 pp.) | `HYUNDAI_PT_2023Q4.*` |
| HY-PT22 | Q4 2022 presentation | 2022 vs 2021 | n/a | https://www.hyundai.com/content/dam/hyundai/ww/en/images/company/investor-relations/financial-Information/presentation/en/22/2022-q4-presentation-en.pdf (28 pp.) | `HYUNDAI_PT_2022Q4.*` |
| HY-PT21 | Q4 2021 presentation | 2021 vs 2020 | n/a | https://www.hyundai.com/content/dam/hyundai/ww/en/images/company/investor-relations/financial-Information/presentation/en/21/2021-q4-presentation-en.pdf (27 pp.) | `HYUNDAI_PT_2021Q4.*` |

### Vehicle segment: verbatim note rows
Note number: "40. SEGMENT INFORMATION" (HY-FS21, HY-FS23); "37. SEGMENT INFORMATION" (HY-FS24,
HY-FS25). Segment definition (HY-FS23, verbatim): *"The Group's operating segments include vehicle
segment, finance segment and others segment. The vehicle segment is engaged in the manufacturing and
sale of motor vehicles. The finance segment operates vehicle financing, credit card processing and
other financing activities. Others segment includes the R&D, train manufacturing and other
activities."* Columns (2022 onward): Vehicle | Finance | Others | Consolidation adjustments | Total.
Footnotes: *"(\*1) Net sales represent sales from external customers."* *"(\*2) Total sales include
inter-company sales within the Group."*

HY-FS24 (same figures in HY-FS23), "For the year ended December 31, 2023":
```
Net sales (*1) | ₩ 130,149,921 ₩ 22,401,156 ₩ 10,112,502 ₩ - ₩ 162,663,579
Total sales (*2) | 212,367,654 | 22,688,779 | 11,985,990 | (84,378,844) | 162,663,579
Operating profit | 12,969,227 | 1,385,538 | 1,064,063 | (291,927) | 15,126,901
```
HY-FS23, "For the year ended December 31, 2022":
```
Net sales (*1) | ₩ 113,341,992 ₩ 20,037,912 ₩ 8,771,565 ₩ - ₩ 142,151,469
Total sales (*2) | 180,440,977 | 20,306,157 | 10,438,311 | (69,033,976) | 142,151,469
Operating profit | 7,910,469 | 1,844,571 | 581,718 | (511,830) | 9,824,928
```
HY-FS21, "For the year ended December 31, 2021" (columns Vehicle (\*1) | Finance | Others | Total;
**no Consolidation adjustments column and no Total sales row**):
```
(*1) Operating profit of the vehicle segment include internal transaction adjustments.
(*2) Net sales represent sales from external customers.
Net sales (*2) | ₩ 94,143,019 ₩ 16,782,412 ₩ 6,685,195 ₩ 117,610,626
Operating profit | 4,155,765 | 2,195,377 | 327,807 | 6,678,949
Inter-company sales | (52,033,375) | (318,479) | (1,352,273) | (53,704,127)
```
HY-FS24, "For the year ended December 31, 2024" (confirms the TM file's 2024 figures):
```
Net sales (*1) | ₩ 136,725,011 ₩ 28,446,650 ₩ 10,059,492 ₩ - ₩ 175,231,153
Total sales (*2) | 221,891,250 | 28,831,480 | 11,816,341 | (87,307,918) | 175,231,153
Operating profit | 11,074,739 | 1,795,249 | 1,032,844 | 336,760 | 14,239,592
```
2025 (TM text `HYUNDAI_2025_audit.txt`, re-read here):
`Net sales (*1) | ₩ 145,631,818 ₩ 30,232,775 ₩ 10,389,879 ₩ - ₩ 186,254,472 | Total sales (*2) | 232,879,832 | 30,552,655 | 12,454,155 (89,632,170) | 186,254,472 | Operating profit | 7,358,550 | 2,164,043 | 832,869 | 1,112,389 | 11,467,851`

**Basis break flagged, not resolved:** in 2021 the vehicle operating profit *"include internal
transaction adjustments"*; from the 2022 comparative onward the consolidation adjustments sit in a
separate column (2022 (511,830); 2023 (291,927); 2024 336,760; 2025 1,112,389). 2021 is therefore not
on the same basis as 2022-2025. The 2022 FS (which would show 2022 as first reported) was not
obtained (HTTP 404), so whether 2022 was re-presented in HY-FS23 is **not determined**. 2023 is
identical in HY-FS23 and HY-FS24.

### Margins (computed, `peers_auto/calc.py HYUNDAI`)
| Year | Vehicle Net sales (external) | Vehicle Total sales (incl. inter-company) | Vehicle operating profit | Margin on Net sales | Margin on Total sales |
|---|---|---|---|---|---|
| 2025 | 145,631,818 | 232,879,832 | 7,358,550 | 5.05% | 3.16% |
| 2024 | 136,725,011 | 221,891,250 | 11,074,739 | 8.10% | 4.99% |
| 2023 | 130,149,921 | 212,367,654 | 12,969,227 | 9.96% | 6.11% |
| 2022 | 113,341,992 | 180,440,977 | 7,910,469 | 6.98% | 4.38% |
| 2021 | 94,143,019 | 146,176,394 (computed: 94,143,019 + 52,033,375) | 4,155,765 | 4.41% | 2.84% |
| pooled | 619,991,761 | 993,756,107 | 43,468,750 | 7.01% | 4.37% |

### Units: "HMC Global Sales", slide "Global Wholesale / Retail Sales (Annual)" (thousand units)
These are **chart slides**; the numbers were read from rendered page images
(`HYUNDAI_PT_<year>Q4_p6.png`, `_p7.png` for 2025) and cross-checked against the PDF text layer
(e.g. HY-PT25 text layer: `4,142|4,138 |4,045|4,109`) and the printed percentage changes.
| Year | Wholesale | Retail Sales | Wholesale ex. China | Retail ex. China | Read from |
|---|---|---|---|---|---|
| 2025 | 4,138 | 4,109 | 4,008 | 3,981 | HY-PT25 PDF p.7 (slide 6) |
| 2024 | 4,142 | 4,045 | 4,014 | 3,887 | HY-PT25 (same in HY-PT24 p.6) |
| 2023 | 4,217 | 4,157 | 3,972 | 3,913 | HY-PT24 (same in HY-PT23 p.6) |
| 2022 | 3,943 | 3,962 | 3,689 | 3,702 | HY-PT23 (same in HY-PT22 p.6) |
| 2021 | 3,891 | 4,143 | 3,539 | 3,758 | HY-PT22 (same in HY-PT21 p.6) |
Footnotes on the "HMC Global Sales" box: HY-PT25 *"7 Including CV"*; HY-PT24 *"5 Including CV"*;
HY-PT23 *"5 Wholesales including CV"*; HY-PT22 *"4 Wholesales including CV"*; HY-PT21 *"4 Wholesale
including CV"*. Artifacts flagged: HY-PT22's "(Annual)" slide legend reads *"Q4 2021 Wholesale"* /
*"Q4 2022 Wholesale"* / *"Q4 2021 Retail Sales"* / *"Q4 2022 Retail Sales"* although the title says
Annual and the HMC Global Sales figures match the annual figures in HY-PT21 and HY-PT23. HY-PT22
footnote 5 (on the "Q4 2021 Wholesale" and "Q4 2021 Retail Sales" legend items): *"Sales number has
changed due to change of region classification for Europe, India, Russia and Others"*; the 2021
global totals are nonetheless the same in HY-PT21 and HY-PT22. Hyundai's 2025 press release figure
4,138,389 cited in the TM file is consistent with the 4,138 wholesale bar (press release itself
not used).

---

## 5. BYD COMPANY LIMITED (HKEX 01211), RMB thousands, PRC Accounting Standards (CAS) from the 2022 report

**Located via HKEXnews title search** (stock id 2696 from
`https://www1.hkexnews.hk/search/prefix.do?...&name=01211&market=SEHK`; search
`https://www1.hkexnews.hk/search/titleSearchServlet.do?...&stockId=2696&title=annual%20report&lang=E`).
All documents fetched 2026-09-13, HTTP 200, saved as `peers_auto/BYD_AR<year>.pdf/.txt` and
`BYD_PSV_<yyyymm>.pdf/.txt`. The annual reports are bilingual (English and Chinese); only English
text is quoted.
| Short | HKEXnews title (verbatim) | Published | URL |
|---|---|---|---|
| B-AR25 | "2025 Annual Report" | 27/03/2026 21:40 | https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0327/2026032703008.pdf (369 pp.) |
| B-AR24 | "Annual Report 2024" | 24/03/2025 21:39 | https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0324/2025032401238.pdf (374 pp.) |
| B-AR23 | "Annual Report 2023" | 26/03/2024 22:49 | https://www1.hkexnews.hk/listedco/listconews/sehk/2024/0326/2024032602585.pdf (352 pp.) |
| B-AR22 | "Annual Report 2022" | 28/03/2023 22:54 | https://www1.hkexnews.hk/listedco/listconews/sehk/2023/0328/2023032802305.pdf (363 pp.) |
| B-AR21 | "Annual Report 2021" | 29/03/2022 22:52 | https://www1.hkexnews.hk/listedco/listconews/sehk/2022/0329/2022032902748.pdf (315 pp.) |
| B-PSV25 | "VOLUNTARY ANNOUNCEMENT PRODUCTION AND SALES VOLUME FOR DECEMBER 2025" (a "(REVISED TITLE)" copy, 2026010100423.pdf, is byte-identical) | 01/01/2026 18:59 | https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0101/2026010100129.pdf |
| B-PSV24 | "... FOR DECEMBER 2024" | 01/01/2025 19:23 | https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0101/2025010100079.pdf |
| B-PSV23 | "... FOR DECEMBER 2023" | 01/01/2024 18:38 | https://www1.hkexnews.hk/listedco/listconews/sehk/2024/0101/2024010100099.pdf |
| B-PSV22 | "... FOR DECEMBER 2022" | 02/01/2023 18:11 | https://www1.hkexnews.hk/listedco/listconews/sehk/2023/0102/2023010200047.pdf |
| B-PSV21 | "... FOR DECEMBER 2021" | 03/01/2022 16:35 | https://www1.hkexnews.hk/listedco/listconews/sehk/2022/0103/2022010301472.pdf |
Auditor (B-AR25): "Ernst & Young Hua Ming LLP"; report signed "Shenzhen, PRC, 27 March 2026".

**The brief's segment name is not the document's.** There is no "automobile-related segment" in
the note. B-AR25 Notes to Financial Statements, "XVI. OTHER SIGNIFICANT MATTERS", "1. Segment
reporting", "(1) Operating segment", verbatim: *"The Group currently has two reportable segments as
follows: a) the mobile handset components, assembly and other products segment comprises the
manufacture and sale of mobile handset components such as housings and electronic components and
the provision of assembly service; b) the automobiles and related products and other products
segment comprises the manufacture and sale of automobiles and auto-related molds and components and
automobile leasing and after sales services, automobile power batteries, lithium-ion batteries,
photovoltaic products and iron battery products, rail transport and its related business."*
**So the segment includes batteries, photovoltaics and rail; it is not automobile-only.**

**The brief asked for "gross profit (or segment result)".** Segment gross profit is **not disclosed**
in the annual report text: note 45 "Operating revenue and operating costs" gives revenue and cost for
the group only, and segment revenue by place/timing; the MD&A gives group gross profit only. The
segment measure is **"Total profit"**, defined (B-AR25, verbatim): *"Segment performance is evaluated
based on reportable segment profit. The adjusted profit before tax is measured consistently with the
Group's profit before tax except that gains or losses arising from changes in fair value, finance
costs (excluding interest expenses on lease liabilities and exchange gains or losses), non-operating
income, other income, losses on disposal of assets, non-operating expenses, investment income
(excluding investment income from associates and joint ventures), income from sales of properties,
the corresponding costs and tax expenses, as well as administrative expenses incurred by the Company
as the Group's headquarter are excluded from such measurement."* This is a **pre-tax** measure, not
operating profit.

**Segment basis change (B-AR22, verbatim):** *"Due to the growth of the electric vehicle business,
the increase in correlation between the main business of rechargeable batteries and the electric
vehicle business during the Year, the management decided to consolidate the rechargeable batteries
and photovoltaic segment with the automobile, automobile-related products and other products segment
in the Year. The segment information for last year was restated on the basis of the current
Period."* B-AR22 also records the Audit Committee recommending *"the adoption of the China Accounting
Standards for Business Enterprises, the cessation of appointment of the international auditor"*.
B-AR21 (HKFRS, three segments) is therefore on a different basis; the restated 2021 from B-AR22 is
used in the series.

### Verbatim segment-note rows (English cells; columns: Mobile handset components, assembly and other products | Automobiles and related products and other products | Adjustments and eliminations | Total)
B-AR25 PDF p.347, "2025":
```
Revenue from external trading | 155,236,528 | 648,645,636 | 82,794 | 803,964,958
Revenue from inter-segment trading | 26,342,005 | 3,836,361 | (30,178,366) | –
Total | 181,578,533 | 652,481,997 | (30,095,572) | 803,964,958
Income from investments accounted for using the equity method | – | 1,007,213 | – | 1,007,213
Depreciation and amortisation | 5,326,998 | 71,456,480 | 1,082,994 | 77,866,472
Total profit | 2,749,565 | 28,417,336 | 8,586,148 | 39,753,049
```
B-AR25 PDF p.348, "2024" (identical in B-AR24 p.351):
```
Revenue from external trading | 159,608,577 | 617,381,933 | 111,945 | 777,102,455
Total | 179,132,433 | 620,730,928 | (22,760,906) | 777,102,455
Total profit | 4,246,624 | 36,332,561 | 9,101,492 | 49,680,677
```
B-AR24 p.352 and B-AR23 p.329, "2023" (identical):
```
Revenue from external trading | 118,576,910 | 483,453,318 | 285,126 | 602,315,354
Total | 131,428,550 | 489,233,672 | (18,346,868) | 602,315,354
Total profit | 4,334,950 | 31,107,896 | 1,825,791 | 37,268,637
```
B-AR23 p.330 and B-AR22 p.335, "2022" (identical; the equity-method row prints (685,885) in B-AR23 under "Share of losses of joint ventures and associates" and 685,885 in B-AR22; row label "Total profit/(losses)" in B-AR22):
```
Revenue from external trading | 98,815,054 | 324,691,175 | 554,406 | 424,060,635
Total | 107,580,364 | 328,662,919 | (12,182,648) | 424,060,635
Total profit/(losses) | 1,893,303 | 18,642,184 | 544,242 | 21,079,729
```
B-AR22 p.336, "2021 (restated)":
```
Revenue from external trading | 86,454,452 | 128,960,450 | 727,493 | 216,142,395
Revenue from inter-segment trading | 3,362,461 | 3,186,296 | (6,548,757) | –
Total | 89,816,913 | 132,146,746 | (5,821,264) | 216,142,395
Total profit/(losses) | 1,843,256 | 3,136,474 | (461,727) | 4,518,003
```
Memo, 2021 **as originally reported** (B-AR21 PDF p.181, HKFRS, columns Rechargeable batteries and
photovoltaic products | Mobile handset components, assembly service and other products | Automobiles
and related products and other products | Corporate and others | Total, RMB'000):
```
Sales to external customers | 15,402,042 | 85,545,672 | 109,659,458 | 692,746 | 211,299,918
Segment results | 432,509 | 1,853,047 | 3,187,865 | 35,434 | 5,508,855
```

### Margins (computed, `peers_auto/calc.py BYD`)
| Year | Segment Total revenue | Segment external revenue | Segment "Total profit" | Margin on Total | Margin on external | Memo: GROUP gross profit / revenue (B-AR25 Five-Year comparison) |
|---|---|---|---|---|---|---|
| 2025 | 652,481,997 | 648,645,636 | 28,417,336 | 4.36% | 4.38% | 142,659,797 / 803,964,958 = 17.74% |
| 2024 | 620,730,928 | 617,381,933 | 36,332,561 | 5.85% | 5.88% | 151,055,839 / 777,102,455 = 19.44% |
| 2023 | 489,233,672 | 483,453,318 | 31,107,896 | 6.36% | 6.43% | 111,916,409 / 602,315,354 = 18.58% |
| 2022 | 328,662,919 | 324,691,175 | 18,642,184 | 5.67% | 5.74% | 65,731,123 / 424,060,635 = 15.50% |
| 2021 (restated) | 132,146,746 | 128,960,450 | 3,136,474 | 2.37% | 2.43% | 26,916,097 / 216,142,395 = 12.45% |
| pooled | 2,223,256,262 | 2,203,132,512 | 117,636,451 | 5.29% | 5.34% | 17.65% |
2021 original HKFRS memo: automobiles segment results 3,187,865 / sales to external customers
109,659,458 = 2.91%. B-AR25 MD&A (verbatim): *"During the Year, the Group's gross profit decreased by
approximately 5.56% to approximately RMB142,660 million. Gross profit margin decreased from
approximately 19.44% in 2024 to approximately 17.74% during the Year."* The Five-Year comparison
prints rounded margins "18 | 19 | 19 | 16 | 12" and a header row "(Restated) | (Restated) |
(Restated)" whose column alignment is not recoverable from the text layer (flagged).

### Units: "New energy vehicle" Sales Volume, Year-to-date December (units)
From the December voluntary announcements (read from rendered page images and the text layer).
Table heading, verbatim (B-PSV25): *"The Board of the Company is pleased to announce that the total
production and sales volume of the Company for the month of December 2025 (Units):"*
| Year | New energy vehicle (sales) | of which "– Passenger vehicle" | "– Battery electric vehicle" | "– Plug-in hybrid electric vehicle" | "Oil-fueled vehicle" (sales) | "Total" (sales) | Source |
|---|---|---|---|---|---|---|---|
| 2025 | 4,602,436 | 4,545,423 | 2,256,714 | 2,288,709 | no row | 4,602,436 | B-PSV25 |
| 2024 | 4,272,145 | 4,250,370 | 1,764,992 | 2,485,378 | no row | 4,272,145 | B-PSV25 (same in B-PSV24) |
| 2023 | 3,024,417 | 3,012,906 | 1,574,822 | 1,438,084 | 0 | 3,024,417 | B-PSV24 (same in B-PSV23) |
| 2022 | 1,863,494 | 1,857,379 | 911,140 | 946,239 | 5,049 | 1,868,543 | B-PSV23 (same in B-PSV22) |
| 2021 | 603,783 | 593,745 | 320,810 | 272,935 | 136,348 | 740,131 | B-PSV22 (same in B-PSV21) |
Caveat printed in the announcements (B-PSV25, partial sentence as extracted): *"... subject to
adjustment and final confirmation. Shareholders and potential investors are advised to read the
financial results of the Company carefully when it is published."* The annual reports' English text
does **not** state BYD's own unit sales (text search for unit figures and "sales volume" found only
industry totals and qualitative statements). Units include commercial vehicles (NEV total less
passenger vehicles); B-PSV text page 2 carries the commercial-vehicle rows (labels lost in extraction).

---

## 6. SUZUKI MOTOR CORPORATION (not an SEC registrant), JPY millions; J-GAAP to FY3/24, IFRS from FY3/24 comparatives

**Sources (globalsuzuki.com, fetched 2026-09-13).** Suzuki labels fiscal years by start year:
"FY2025" = year ended March 31, 2026 (ASR cover, verbatim: *"In this document, "FY2025" refers to the
year ended March 31, 2026."*).
| Short | Document (verbatim title) | Covers | Date | URL | Status |
|---|---|---|---|---|---|
| S-ASR25 | "Annual Securities Report ... The 160th Business Term" (English translation; audited by PricewaterhouseCoopers Japan LLC) | FY2024, FY2025 (IFRS) | "[Filing Date] June 23, 2026" | https://www.globalsuzuki.com/ir/library/asr/pdf/asr_fy2025.pdf | 200, 219 pp. |
| S-ASR24 | "Annual Securities Report", 159th Fiscal Year | FY2023, FY2024 (IFRS; first-time adoption) | "[Filing Date] June 27, 2025" | https://www.globalsuzuki.com/ir/library/asr/pdf/asr_fy2024.pdf | 200, 227 pp. |
| (ASR FY2023, FY2022, FY2021) | same pattern `asr_fy2023.pdf`, `asr_fy2022.pdf`, `asr_fy2021.pdf` | | | https://www.globalsuzuki.com/ir/library/asr/pdf/asr_fy2023.pdf etc. | **HTTP 404** each |
| S-SUM23 | "Consolidated Financial Summary for FY2023 (April 1, 2023 – March 31, 2024) [Japanese GAAP]" | FY2022, FY2023 | "May 13, 2024" | https://www.globalsuzuki.com/ir/library/financialresults/pdf/2023/financial_summary.pdf | 200 |
| S-SUM22 | "Consolidated Financial Summary for FY2022 (April 1, 2022 – March 31, 2023) [Japanese GAAP]" | FY2021, FY2022 | "May 15, 2023" | https://www.globalsuzuki.com/ir/library/financialresults/pdf/2022/financial_summary.pdf | 200 |
| S-SUM21 | "Consolidated Financial Summary for FY2021 (1 April 2021 – 31 March 2022) [Japanese GAAP]" | FY2020, FY2021 | "11 May 2022" | https://www.globalsuzuki.com/ir/library/financialresults/pdf/2021/financial_summary.pdf | 200 |
| S-REF21..25 | "<Reference for FY20xx>" | units | 11 May 2022 / May 15, 2023 / May 13, 2024 / May 12, 2025 / May 14, 2026 | https://www.globalsuzuki.com/ir/library/financialresults/pdf/<year>/financial_reference.pdf | 200 each |
The Consolidated Financial Summaries and References are earnings releases (not audited annual
reports); J-GAAP years come from them because the English ASRs for those years returned 404.

**Segments (S-ASR25, verbatim):** *"The Company has four reportable segments of Automobile business,
Motorcycle business, Marine business, and Other business, based on the form of management
organization and the nature of products and services."* Automobile business main products: *"Mini
vehicles, sub-compact vehicles, standard-sized vehicles"*. J-GAAP measure (S-SUM22 footnote,
verbatim): *"\*1. Segment profit means operating profit in the consolidated statements of income."*

### Verbatim segment rows (columns: Automobile business | Motorcycle business | Marine business | Other business | Total | Adjustment | Consolidated/Total)
S-ASR25 PDF p.154, "FY2025 (April 1, 2025–March 31, 2026)", IFRS:
```
Revenue from external customers | 5,706,420 | 454,488 | 119,456 | 12,601 | 6,292,967 | － | 6,292,967
Total revenue | 5,706,420 | 454,488 | 119,456 | 12,601 | 6,292,967 | － | 6,292,967
Operating profit | 547,632 | 44,770 | 26,605 | 3,900 | 622,909 | － | 622,909
```
S-ASR25 PDF p.153 (identical in S-ASR24), "FY2024 (April 1, 2024–March 31, 2025)", IFRS:
```
Revenue from external customers | 5,305,217 | 398,131 | 109,684 | 12,128 | 5,825,161 | － | 5,825,161
Operating profit | 567,634 | 40,822 | 30,568 | 3,825 | 642,851 | － | 642,851
```
S-ASR24, "FY2023 (April 1, 2023–March 31, 2024)", IFRS:
```
Revenue from external customers | 4,869,579 | 365,041 | 111,665 | 11,235 | 5,357,523 | − | 5,357,523
Total revenue | 4,869,579 | 365,041 | 111,665 | 11,235 | 5,357,523 | − | 5,357,523
Operating profit | 423,940 | 39,086 | 27,435 | 3,371 | 493,834 | − | 493,834
```
S-SUM23, "FY2023(April 1, 2023 – March 31, 2024)", **J-GAAP** (same year, other basis):
```
Net Sales | 4,883,804 | 366,934 | 112,281 | 11,235 | 5,374,255 | － | 5,374,255
Segment Profit*1 | 398,173 | 39,013 | 25,230 | 3,144 | 465,563 | － | 465,563
```
S-SUM23 (identical in S-SUM22), "FY2022 (April 1, 2022 – March 31, 2023)", J-GAAP:
```
Net Sales | 4,162,163 | 333,151 | 134,569 | 11,759 | 4,641,644 | － | 4,641,644
Segment Profit*1 | 279,084 | 29,340 | 39,435 | 2,690 | 350,551 | － | 350,551
```
S-SUM22 (figures also present in S-SUM21), "FY2021 (April 1, 2021 – March 31, 2022)", J-GAAP:
```
Net sales | 3,204,877 | 253,458 | 97,981 | 12,064 | 3,568,380 | － | 3,568,380
Segment profit *1 | 152,832 | 10,859 | 24,017 | 3,750 | 191,460 | － | 191,460
```

### Margins (computed, `peers_auto/calc.py SUZUKI`)
| FY ended Mar | Basis | Automobile revenue / net sales | Automobile operating (segment) profit | Margin |
|---|---|---|---|---|
| 2026 | IFRS | 5,706,420 | 547,632 | 9.60% |
| 2025 | IFRS | 5,305,217 | 567,634 | 10.70% |
| 2024 | IFRS | 4,869,579 | 423,940 | 8.71% |
| 2024 | J-GAAP (memo) | 4,883,804 | 398,173 | 8.15% |
| 2023 | J-GAAP | 4,162,163 | 279,084 | 6.71% |
| 2022 | J-GAAP | 3,204,877 | 152,832 | 4.77% |
| pooled FY22-FY26 (J-GAAP FY22-23 + IFRS FY24-26, **mixed basis**) | | 23,248,256 | 1,971,122 | 8.48% |

### Units (thousand units), from S-REF (verbatim labels)
**(a) "[Units (Production & Sales)]" <Automobiles> "Sales Total"** (footnote \*2, S-REF25 verbatim:
*""Sales" means retail sales of SUZUKI brand vehicles (some are wholesale sales), including
license-built vehicles in part."* and *"FY2025 includes preliminary figures."*; OEM sales shown
separately *"(Not included above)"*).
**(b) "[Breakdown of Consolidated Revenue]" (S-REF24, S-REF25; "[Breakdown of Consolidated Net Sales]"
in S-REF22, S-REF23) Automobile "Total" Unit** (footnote \*3 verbatim: *"Units are wholesale sales
based on consolidated net sales."*).
| FY ended Mar | (a) Sales Total | (b) Consolidated revenue units, Automobile Total | of which India (b) | Source |
|---|---|---|---|---|
| 2026 | 3,320 | 3,572 | (1,975) | S-REF25 (a) text layer and p.3 image; (b) p.4 image |
| 2025 | 3,241 (S-REF25); **3,240** (S-REF24) | 3,439 | (1,905) | S-REF25; S-REF24 |
| 2024 | 3,168 | 3,370 (J-GAAP S-REF23; also 3,370 beside IFRS amount 4,869.6 in S-REF24 text) | (1,852) | S-REF23, S-REF24 |
| 2023 | 3,000 | 3,225 | (1,707) | S-REF22, S-REF23 |
| 2022 | 2,707 | 2,853 | (1,414) | S-REF21 (a); S-REF22 (b) |
Tables (b) were read from rendered page images (`SUZUKI_reference_<year>_p4.png`); (a) Sales Total
rows are from the text layer (`Sales Total | 2,571 | 2,707 | +136 | +5.3%` in S-REF21, `2,707 |
3,000` in S-REF22, `3,000 | 3,168` in S-REF23, `3,168 | 3,240` in S-REF24, `3,241 | 3,320` in
S-REF25). The FY3/25 figure differs by 1 between S-REF24 and S-REF25 (flagged, not resolved).

---

## SUMMARY (transcribed and computed above; measures differ by company and are not like-for-like)
Column years: Japanese companies fiscal years ended March of the stated year (FY3/22 .. FY3/26);
Hyundai and BYD calendar years 2021 .. 2025. Computation script: `peers_auto/calc.py` (output
saved in `peers_auto/calc_out.txt`).

| Company | Measure | Margins: FY3/22 or CY21 / FY3/23 or CY22 / FY3/24 or CY23 / FY3/25 or CY24 / FY3/26 or CY25 | 5-yr pooled | Units (five years, same order) | Source |
|---|---|---|---|---|---|
| Toyota automotive | IFRS segment "Operating income" / segment "Total" | 7.99% / 6.45% / 11.20% / 9.12% / 6.11% | 8.22% | "consolidated vehicle unit sales" (000): 8,230 / 8,822 / 9,443 / 9,362 / 9,595 | 20-F Note 5 and Item 5; accessions 0001193125-22-179197, -23-179181, -24-167462, -25-142326, -26-264811 |
| Nissan Automobile | J-GAAP "Segment profits (loss)" / segment "Total" net sales | (2.07)% / 0.44% / 1.88% / (2.30)% / (2.68)% | (0.88)% | "Actual sales (on a retail basis)" (units): 3,875,986 / 3,305,204 / 3,442,257 / 3,346,248 / 3,151,164; "on a consolidated basis": 2,293,575 / 2,450,765 / 2,785,614 / 2,656,592 / 2,434,516 | Securities Report English translations fr2021..fr2025.pdf (nissan-global.com) |
| Nissan memo | Consolidated op. income less Sales financing segment profit ("Automobile & Eliminations", computed) / third-party auto sales | (1.72)% / 0.68% / 2.24% / (1.89)% / (2.23)% | (0.51)% | same | same |
| Hyundai vehicle | K-IFRS segment "Operating profit" / "Net sales (\*1)" (external) | 4.41% / 6.98% / 9.96% / 8.10% / 5.05% | 7.01% | "HMC Global Sales" Wholesale (000): 3,891 / 3,943 / 4,217 / 4,142 / 4,138; Retail Sales: 4,143 / 3,962 / 4,157 / 4,045 / 4,109 | Audited consolidated FS 2021, 2023, 2024 (+2025 via TM); Q4 earnings presentations 2021-2025 (hyundai.com) |
| Hyundai vehicle (alt. denominator) | same / "Total sales (\*2)" incl. inter-company (2021 computed) | 2.84% / 4.38% / 6.11% / 4.99% / 3.16% | 4.37% | same | same; **2021 on a different basis** (adjustments inside vehicle OP) |
| BYD "Automobiles and related products and other products" (includes batteries, PV, rail) | CAS segment "Total profit" (adjusted **pre-tax**) / segment "Total" revenue | 2.37% (2021 restated) / 5.67% / 6.36% / 5.85% / 4.36% | 5.29% | "New energy vehicle" Sales Volume YTD Dec (units): 603,783 / 1,863,494 / 3,024,417 / 4,272,145 / 4,602,436 ("Total" incl. oil-fueled: 740,131 / 1,868,543 / 3,024,417 / 4,272,145 / 4,602,436) | HKEXnews Annual Reports 2021-2025; December production and sales volume announcements |
| BYD memo | GROUP gross profit / revenue (not segment) | 12.45% / 15.50% / 18.58% / 19.44% / 17.74% | 17.65% | same | B-AR25 Five-Year comparison |
| Suzuki Automobile business | J-GAAP "Segment profit" / "Net sales" (FY3/22-23); IFRS "Operating profit" / revenue (FY3/24-26) | 4.77% / 6.71% / 8.71% (IFRS; J-GAAP 8.15%) / 10.70% / 9.60% | 8.48% (mixed basis) | Consolidated revenue units, Automobile (000): 2,853 / 3,225 / 3,370 / 3,439 / 3,572; "Sales Total" (retail, some wholesale): 2,707 / 3,000 / 3,168 / 3,241 (3,240 in S-REF24) / 3,320 | Consolidated Financial Summaries FY2021-23; Annual Securities Reports FY2024-25; References FY2021-25 (globalsuzuki.com) |

Spot-check (Section 1): GM GMNA 2025 154,317 / 10,452 and Stellantis 2025 "Total Consolidated
shipments" 5,484 both FOUND and MATCH the TM competitor row.

---

## NOT DISCLOSED / BLOCKED
| Company | Item | Status / obstacle |
|---|---|---|
| Toyota | Local 20-F text files carry no accession header | Accessions mapped via `batch1.py` and `submissions.json` (read only); not re-downloaded |
| Toyota | FY3/20 unit total discrepancy (T-22 prints 8,955; TM run decade table shows 8,959) | Outside the window; source of 8,959 not checked |
| Nissan | The word "wholesale" | Not used for the unit table; the report's label is "on a consolidated basis" |
| Nissan | Segment pre-tax income for Sales financing | Not transcribed; segment measure is operating income |
| Hyundai | 2022 audited FS as first published | `.../report-en/2022/2022-q4-consolidated-audit-report-en.pdf` **HTTP 404**; 2022 taken from HY-FS23 comparative; whether 2022 was re-presented is not determined |
| Hyundai | 2021 comparability with 2022-2025 | 2021 FS: vehicle OP *"include internal transaction adjustments"*, no Total sales row; later years show consolidation adjustments separately |
| Hyundai | Annual report / business report (English) | Not obtained (not needed for the figures); units taken from chart slides in earnings presentations, read from rendered images |
| Hyundai | HY-FS21 auditor firm name | Not in the PDF text layer (engagement partner name only) |
| BYD | Automobile-only segment | NOT DISCLOSED: the reportable segment includes power batteries, lithium-ion batteries, PV, iron batteries, rail transport |
| BYD | Segment gross profit | NOT DISCLOSED in annual report text; only group gross profit; segment measure is pre-tax "Total profit" |
| BYD | 2021 on the current basis | Only as restated in B-AR22 (two segments, CAS); B-AR21 original (HKFRS, three segments) recorded as memo |
| BYD | Own unit sales in the annual reports | Not found in English text; units taken from HKEXnews voluntary monthly announcements, which state the figures are subject to adjustment and final confirmation |
| BYD | Five-Year comparison "(Restated)" column alignment | Not recoverable from text layer |
| Suzuki | English Annual Securities Reports FY2021-FY2023 | `asr_fy2023.pdf`, `asr_fy2022.pdf`, `asr_fy2021.pdf` **HTTP 404**; J-GAAP years taken from Consolidated Financial Summaries (earnings releases, not the ASR) |
| Suzuki | Consistent five-year basis | J-GAAP FY3/22-FY3/24, IFRS FY3/24-FY3/26; FY3/24 shown on both; pooled figure is mixed basis |
| Suzuki | FY3/25 retail "Sales Total" | 3,240 (S-REF24) vs 3,241 (S-REF25); not resolved; S-REF25 notes FY2025 includes preliminary figures |
| Suzuki | Captive finance, pricing bridge, capacity quotes | Not attempted (not in brief) |
| All added companies | Pricing bridge, capacity/pricing own-words quotes, captive-finance share | Not in this brief; not transcribed |

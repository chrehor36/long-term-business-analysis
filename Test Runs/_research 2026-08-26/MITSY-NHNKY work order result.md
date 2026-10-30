# MITSY / NHNKY retrieval work orders, result
Retrieved 2026-08-28. Primary sources only. All figures JPY millions as published, no conversion.

---

## ORDER 1: MITSUI & CO., LTD. (TSE 8031; ADR MITSY)

### Source document
| | |
|---|---|
| Document | Annual Securities Report ("Yukashoken Hokokusho"), 107th fiscal year, English translation. Consolidated financial statements audited; prepared in accordance with IFRS Accounting Standards as issued by the IASB. |
| URL | https://www.mitsui.com/jp/en/ir/library/securities/__icsFiles/afieldfile/2026/08/12/en_107yuho.pdf |
| Publication date | Japanese original issued 2026-06-12 (stated in the report: "issuance date of this report (June 12, 2026)", p. 95 of the body). English translation posted to the IR site 2026-08-12 (date in the file path). |
| Found via | https://www.mitsui.com/jp/en/ir/ then Securities Reports: https://www.mitsui.com/jp/en/ir/library/securities/index.html |
| Local copy | `Mitsui_AnnualSecuritiesReport_FY2026-03_en_107yuho.pdf` (10.8 MB, 324 PDF pages) in this folder |
| Standard | IFRS (as issued by the IASB), stated on body p. 215 (PDF p. 218). Presentation currency JPY, rounded to nearest million. USD column is a convenience translation at 160 JPY per USD as of 2026-03-31; not used here. |

### Figures, fiscal year ended March 31, 2026 (consolidated, Mn JPY)
| Item | FY ended 2026-03-31 | FY ended 2025-03-31 | Where |
|---|---|---|---|
| Cash flows from operating activities | 952,912 | 1,017,518 | Consolidated Statements of Cash Flows, body p. 214 (PDF p. 217) |
| Depreciation and amortization (OCF reconciliation line) | 333,248 | 313,730 | same statement |
| Purchases of property, plant and equipment | (1,108,399) | (346,147) | same statement, investing activities |
| Purchases of investment property | (1,187) | (12,671) | same statement, investing activities |
| Profit for the year attributable to owners of the parent | 833,971 | 900,342 | Consolidated Statements of Income, body p. 210 (PDF p. 213) |
| Basic EPS attributable to owners of the parent (JPY) | 291.12 | 306.73 | same statement |

Fiscal-year-end: **March 31, 2026** (annual closing date stated in Note 1, Reporting Entity).

### Shares
| Item | Count | Where |
|---|---|---|
| Shares issued (common stock), as of 2026-03-31 | 2,864,666,576 | body p. 95 (PDF p. 98), "Total Number of Shares"; unchanged as of report issuance date 2026-06-12 |
| Treasury stock, as of 2026-03-31 | 17,038,165 | body p. 104 (PDF p. 107), Status of Shareholders note *1 |
| Shares outstanding net of treasury, 2026-03-31 | 2,847,628,411 | COMPUTED: issued minus treasury; not a published line |

Cross-checks run: (a) every JPY figure above divided by the stated 160 JPY/USD convenience rate reproduces the printed USD column (e.g. 952,912 / 160 = 5,956; 1,108,399 / 160 = 6,927); (b) year-end dividend of 60 JPY per share totaling 170,858 Mn JPY (body p. 110) implies ~2,847.6M eligible shares, consistent with the computed net-of-treasury count; (c) 41,075,000 treasury shares were cancelled 2026-03-30 (note *15, body p. 104), which is why issued shares fell year on year.

Flag, as published: purchases of PP&E tripled year on year (346,147 to 1,108,399 Mn JPY). No cause is asserted here; the segment/commitments notes in the same report are where to look. For maintenance-vs-growth splitting under the framework, this line is total capex, not maintenance capex.

---

## ORDER 2: NHNKY, identity resolution and figures

### Identity: RESOLVED. NHNKY = NIHON KOHDEN CORPORATION (TSE 6849), unsponsored ADR.
Not Nihon Nohyaku. Nihon Kohden is a Tokyo-based medical electronic equipment maker (patient monitors, EEG/ECG, defibrillators/AEDs, ventilators), listed on the TSE Prime Market, code 6849.

Identity evidence (concordant, five independent quote/directory sources):
- Nasdaq: "Nihon Kohden Corporation ADR (NHNKY)" https://www.nasdaq.com/market-activity/stocks/nhnky
- Morningstar: "Nihon Kohden Corp ADR (NHNKY)" https://morningstar.com/stocks/otcm/nhnky/quote
- Google Finance: "Nihon Kohden Unsponsored ADR Representing Ord Shs (NHNKY)" https://www.google.com/finance/quote/NHNKY:OTCMKTS
- Robinhood: "Nihon Kohden Unsponsored…" https://robinhood.com/us/en/stocks/NHNKY/
- stockanalysis.com: Nihon Kohden Corporation, main listing Tokyo Stock Exchange 6849 https://stockanalysis.com/quote/otc/NHNKY/

Not obtained: the OTC Markets page itself (https://www.otcmarkets.com/stock/NHNKY/overview) timed out twice from this environment (bot protection). The five concordant sources above settle the identity question, which is a directory fact, not a financial figure.

### English IR: EXISTS
- IR top: https://www.nihonkohden.com/ir.html
- Financial results library: https://www.nihonkohden.com/ir/library/result.html
- Why the prior attempt got 403/404: the nihonkohden.com and nihonkohden.co.jp HTML pages sit behind a WAF that returns 403 to non-browser fetchers (reproduced here with a browser user-agent string as well). The PDF endpoints are NOT blocked; the results PDF below downloaded cleanly with curl. So English IR exists and its documents are retrievable; only HTML page scraping is blocked from this environment.

### Source document
| | |
|---|---|
| Document | "Consolidated Financial Results for the Fiscal Year Ended March 31, 2026 (Japan GAAP)" (kessan tanshin, English translation; translated from the Japanese original, which prevails) |
| URL | https://www.nihonkohden.com/ir/news/auto_20260512526491/pdfFile.pdf |
| Publication date | Dated May 14, 2026 on the document face (URL slug carries 20260512) |
| Local copy | `NihonKohden_FY2026-03_ConsolidatedFinancialResults_tanshin.pdf` (829 KB, 33 pages) in this folder |
| Standard | Japan GAAP. Amounts rounded DOWN to the nearest million yen (stated on p. 1). Company labels the year ended 2026-03-31 as "FY2025". |
| Caveat | This is the earnings release, unaudited at publication. The audited annual securities report is filed on EDINET in Japanese only (issuer: Nihon Kohden Corporation, securities code 6849; document: Yukashoken Hokokusho, filed circa late June 2026). Figures below are the tanshin's consolidated statements. |

### Figures, fiscal year ended March 31, 2026 (consolidated, Mn JPY, Japan GAAP)
| Item | FY ended 2026-03-31 | FY ended 2025-03-31 | Where |
|---|---|---|---|
| Net cash flows from operating activities | 21,055 | 15,286 | Consolidated Statements of Cash Flows, p. 18 |
| Depreciation and amortization | 4,757 | 4,066 | same statement |
| Amortization of goodwill (separate line under J-GAAP) | 1,064 | 124 | same statement |
| Purchase of property, plant and equipment | (5,727) | (7,126) | same statement, investing activities |
| Purchase of intangible assets | (2,131) | (1,583) | same statement, investing activities |
| Income attributable to owners of parent | 14,513 | 14,098 | Consolidated Statements of Income, p. 14 |
| Basic EPS (JPY) | 89.25 | 84.88 | p. 1 highlights |

Fiscal-year-end: **March 31, 2026**.

### Shares (tanshin p. 2, "Number of issued shares (common shares)")
| Item | Count |
|---|---|
| Total issued shares at end of period (incl. treasury), 2026-03-31 | 170,961,960 |
| Treasury shares at end of period, 2026-03-31 | 10,989,474 (includes ESOP-trust-held shares) |
| Average shares outstanding during the period | 162,607,042 |
| Shares outstanding net of treasury, 2026-03-31 | 159,972,486. COMPUTED: issued minus treasury; not a published line |

Note: each common share was split 2-for-1 effective 2024-07-01; per-share figures for both years shown are on a post-split basis (stated on pp. 1-2).

Cross-check run: 89.25 JPY basic EPS x 162,607,042 average shares = 14,512.7 Mn JPY, consistent with 14,513 published (rounded down).

---

## Unobtained / caveats, both orders
1. OTC Markets NHNKY page: timed out twice (bot protection). Identity settled via five concordant directories instead.
2. Nihon Kohden HTML IR pages: 403 behind WAF from this environment; URLs recorded above and verified to exist via search-engine indexing; PDF endpoints retrievable.
3. Nihon Kohden audited annual securities report: Japanese-only EDINET filing; the English figures above are from the company's own translated tanshin. If audited-statement confirmation is required, the EDINET filing (code 6849) is the document.
4. Mitsui English annual securities report is a translation of the audited Japanese original; the original prevails on discrepancy (standard disclaimer).
5. Both companies' ADR-level share counts (ADR ratio) were NOT pulled; counts above are ordinary shares.

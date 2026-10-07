# SONY run: G&NS competitor row, PEERS (Microsoft gaming, Nintendo, EA/TTWO context)
Built 2026-09-13 by a subagent. **Evidence gathering only; no moat verdict is reached here.**
Sony's own G&NS figures are handled by the main run. Status: COMPLETE (see section 5 for what
was not obtained and section 6 for defects in the brief).

Scripts and raw documents: `peers_games/` (fetch_ntdo.py, render.py, msft_seg.py,
fts_msft_price.py, fts_list.py; Nintendo PDFs + extracted text in `peers_games/ntdo/`, fetch log
`peers_games/ntdo/_fetch_log.txt`).

**Fiscal-year alignment (read before comparing).** Sony and Nintendo: April-March. Microsoft:
July-June. EA and TTWO: April-March. "Nintendo FY3/2026" = Apr 2025-Mar 2026 = the same window
as Sony's fiscal year ended March 2026. Microsoft FY2026 = Jul 2025-Jun 2026, which overlaps that
window by nine months only. No figure below is re-cut to a common window.

---
## 1. MICROSOFT (MSFT), CIK 0000789019. Rung 1, SEC 10-K

**Documents (all reused from disk, stripped primary-document text saved by the 2026-09-06 MSFT
run in `Test Runs/_research 2026-09-06 MSFT/`; not re-fetched):**

| Vintage | Period end | Accession | Primary doc | File on disk |
|---|---|---|---|---|
| FY2023 10-K | 2023-06-30 | 0000950170-23-035122 | msft-20230630.htm | MSFT_FY2023_10K.txt |
| FY2024 10-K | 2024-06-30 | 0000950170-24-087843 | msft-20240630.htm | MSFT_FY2024_10K.txt |
| FY2025 10-K | 2025-06-30 | 0000950170-25-100235 | msft-20250630.htm | MSFT_FY2025_10K.txt |
| FY2026 10-K | 2026-06-30 | 0001193125-26-323660 | msft-20260630.htm | MSFT_FY2026_10K.txt |

Source URL of FY2026 as recorded in the file header:
`https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm`.

### 1a. Table ($ millions)

| | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| Gaming revenue (FY2026: "XBOX (formerly Gaming)"), revenue-by-product note | 15,466 | 21,503 | 23,455 | 21,790 |
| Gaming revenue growth, as filed in MD&A | "decreased $764 million or 5%" | "increased $6.0 billion or 39%" | "increased $2.0 billion or 9%" | "decreased $1.7 billion or 7%" |
| Xbox content and services revenue growth, as filed | -3% | +50% (44 pts Activision) | +16% | -5% |
| Xbox hardware revenue growth, as filed | -11% | -13% | -25% | -29% |
| Xbox hardware revenue, $ | **NOT DISCLOSED** (growth % only, every vintage) | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED |
| Gaming operating income / margin | **NOT DISCLOSED** (no gaming profit line in any vintage) | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED |
| More Personal Computing segment revenue (FY2025/FY2026 recast basis) | 44,820 | 50,838 | 54,649 | 54,052 |
| MPC segment operating income (recast basis) | 10,038 | 11,959 | 14,166 | 14,386 |
| MPC operating margin, COMPUTATION (OI / revenue) | 22.4% | 23.5% | 25.9% | 26.6% |
| Capex / D&A at gaming or segment level | **NOT DISCLOSED** (see quote 1c.9) | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED |
| Unit metric (consoles, Game Pass members, MAU) | **NOT FILED** in any of these vintages | NOT FILED | NOT FILED | NOT FILED |

FY2022 Gaming revenue for the FY2023 growth base: 16,230 (FY2023 and FY2024 10-K revenue-by-product
tables). Gaming revenue growth recomputed from the note, COMPUTATION: FY2023 -4.7%, FY2024 +39.0%,
FY2025 +9.1%, FY2026 -7.1%; each matches the rounded MD&A figure.

**MPC is NOT gaming.** MPC also contains Windows OEM and Devices and Search advertising. The MPC
margin is a ceiling-or-floor-unknown proxy and must not be read as a gaming margin.

**Segment recast, flagged.** MPC as originally filed in the FY2023 10-K: revenue 54,734, operating
income 16,450 (FY2024 10-K: FY2024 revenue 62,032, operating income 19,309). The FY2025 10-K recast
FY2023 MPC to revenue 44,820 and operating income 10,038, and FY2024 to 50,838 / 11,959. The table
uses the recast basis for all four years so the series is one presentation. The Gaming revenue
line itself did not change between vintages (FY2023 = 15,466 in the FY2023, FY2024 and FY2025
10-Ks; FY2024 = 21,503 in the FY2024, FY2025 and FY2026 10-Ks; FY2025 = 23,455 in FY2025 and
FY2026). Cross-check of one figure per operator rule 4: Gaming FY2025 23,455 read in both the
FY2025 and FY2026 filed revenue-by-product tables.

**Acquisition distortion.** Activision Blizzard closed 2023-10-13 (FY2024 Q2). FY2024 and part of
FY2025 growth are acquired, not organic (quotes 1c.2, 1c.3).

### 1b. Segment table, verbatim flattening of the filed note (FY2026 10-K, acc 0001193125-26-323660)
"Segment revenue, cost of revenue, operating expenses, and operating income were as follows during
the periods presented: (In millions) Year Ended June 30, 2026 2025 2024 ... More Personal Computing
Revenue $ 54,052 $ 54,649 $ 50,838 Cost of revenue 23,481 25,238 24,892 Operating expenses 16,185
15,245 13,987 Operating income $ 14,386 $ 14,166 $ 11,959"
(FY2025 10-K, acc 0000950170-25-100235, same table: "More Personal Computing Revenue $ 54,649 $
50,838 $ 44,820 Cost of revenue 25,238 24,892 24,552 Operating expenses 15,245 13,987 10,230
Operating Income $ 14,166 $ 11,959 $ 10,038")
*Table cells flattened from HTML by `peers_games/msft_seg.py`; the pipes and line breaks of the
table are removed, the digits are not altered.*

### 1c. Verbatim source lines

1. FY2023 10-K (acc 0000950170-23-035122), MD&A, MPC:
   > "Gaming revenue decreased $764 million or 5% driven by declines in Xbox hardware and Xbox content and services. Xbox hardware revenue decreased 11% driven by lower volume and price of consoles sold. Xbox content and services revenue decreased 3% driven by a decline in first-party content, offset in part by growth in Xbox Game Pass."
2. FY2024 10-K (acc 0000950170-24-087843), MD&A, MPC:
   > "Gaming revenue increased $6.0 billion or 39% driven by growth in Xbox content and services. Xbox content and services revenue increased 50% driven by 44 points of net impact from the Activision Blizzard acquisition. Xbox hardware revenue decreased 13% driven by lower volume of consoles sold."
3. FY2025 10-K (acc 0000950170-25-100235), MD&A, MPC:
   > "Gaming revenue increased $2.0 billion or 9% driven by growth in Xbox content and services, offset in part by a decline in Xbox hardware. Xbox content and services revenue increased 16% driven by the impact of the Activision Blizzard acquisition and Xbox Game Pass. Xbox hardware revenue decreased 25% driven by lower volume of consoles sold."
4. FY2026 10-K (acc 0001193125-26-323660), MD&A, MPC:
   > "XBOX revenue decreased $1.7 billion or 7% driven by declines in XBOX content and services and XBOX hardware. XBOX content and services revenue decreased 5% on a prior year comparable that benefited from strong first-party content performance, offset in part by growth in XBOX Game Pass. XBOX hardware revenue decreased 29% driven by lower volume of consoles sold."
5. FY2026 10-K, MD&A, MPC operating expenses:
   > "Operating expenses increased $940 million or 6% driven by impairment and other related expenses in our XBOX business and continued investments in research and development compute capacity, AI talent, and data to support product development that benefits the entire portfolio."
   The amount of the XBOX impairment is **not stated** in any line containing "XBOX" in the FY2026 10-K. The goodwill note says: "No instances of impairment were identified in our May 1, 2026, May 1, 2025, or May 1, 2024 tests." and "No material impairments of intangible assets were identified during fiscal years 2026, 2025, or 2024."
6. FY2026 10-K, segment description (renaming):
   > "XBOX (formerly Gaming), including XBOX hardware and XBOX content and services, comprising first- and third-party content (including games and in-game content), XBOX Game Pass and other subscriptions, XBOX Cloud Gaming, advertising, and other cloud services."
7. Competition, the naming change. FY2023 10-K and FY2024 10-K (identical sentence):
   > "Our gaming platform competes with console platforms from Nintendo and Sony, both of which have a large, established base of customers."
   FY2025 10-K and FY2026 10-K:
   > "Our gaming platform competes with other console platforms."
   (Nintendo and Sony are no longer named from the FY2025 vintage. Fact recorded; no inference drawn.)
8. Revenue drivers, FY2026 10-K:
   > "XBOX revenue is mainly affected by subscriptions and sales of first- and third-party content, as well as advertising."
9. Segment D&A, FY2026 10-K segment note (same sentence in FY2023, FY2024, FY2025 10-Ks):
   > "Assets are not allocated to segments for internal reporting presentations. A portion of amortization and depreciation is included with various other costs in an overhead allocation to each segment. It is impracticable for us to separately identify the amount of amortization and depreciation by segment that is included in the measure of segment profit or loss."

### 1d. Pricing (for [E4-37] / [E2-44])
- **The only Xbox price statement in FY2023-FY2026 10-Ks** is quote 1c.1: "lower volume and price of consoles sold" (FY2023). FY2024-FY2026 attribute hardware declines to volume only.
- **No Xbox console price increase and no Game Pass price change is stated in any MSFT 10-K or 10-Q.** Screen via `tools/sources.py:fts_count()` (cik 0000789019), 2026-09-13: "Game Pass price" 0 hits (10-Q), 0 (10-K); "Xbox Game Pass Ultimate" 0 / 0; "higher prices of consoles" 0 / 0; "price of consoles" 9 (10-Q) / 3 (10-K), the latest 10-Q hit being period 2023-09-30 (acc 0000950170-23-054855) and the latest 10-K hit FY2023 (acc 0000950170-23-035122); "price increase" 1 / 1, which on opening is the Microsoft 365 Consumer price increase, not Xbox (FY2025 10-K: "growth in revenue per user from the price increase announced in January 2025"). A screen, not evidence (operator rule 8): the absence is of a *filed* statement; any price change announced outside SEC filings is not tested here.
- Prior project record: `Test Runs/_research 2026-09-06 MSFT/segments_units.md` section D.4: "No Xbox price level, price change amount, or console ASP is filed in any vintage." Unit withdrawals (same file, section B/C): Xbox consoles sold filed through FY2016 only; Xbox Game Pass members FY2020 only; Xbox Live MAU FY2016 only.

---
## 2. NINTENDO CO., LTD. (TSE 7974). Rung 3, company IR site, English

Not an SEC registrant. Reports under **Japanese GAAP** (annual report: "Consolidated financial
statements of Nintendo are prepared in accordance with accounting standards generally accepted in
Japan."). Sony reports under IFRS; operating-profit definitions are not identical.

**Documents fetched 2026-09-13 (all HTTP 200, saved in `peers_games/ntdo/`):**

| Document | Date | URL |
|---|---|---|
| Annual Report 2026 (FY ended 2026-03-31), 103 pp | posted 2026-07-06 | https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf |
| Annual Report 2025 (FY ended 2025-03-31), 103 pp | posted 2025-07-07 | https://www.nintendo.co.jp/ir/pdf/2025/annual2503e.pdf |
| Annual Report 2024 (FY ended 2024-03-31), 95 pp | posted 2024-07-08 | https://www.nintendo.co.jp/ir/pdf/2024/annual2403e.pdf |
| Consolidated Financial Highlights, FY3/2026 | 2026-05-08 | https://www.nintendo.co.jp/ir/pdf/2026/260508e.pdf |
| Consolidated Financial Highlights, FY3/2025 | 2025-05-08 | https://www.nintendo.co.jp/ir/pdf/2025/250508e.pdf |
| Consolidated Financial Highlights, FY3/2024 | 2024-05-07 | https://www.nintendo.co.jp/ir/pdf/2024/240507e.pdf |
| Financial Results Explanatory Material, FY3/2026 | 2026-05-08 | https://www.nintendo.co.jp/ir/pdf/2026/260508_4e.pdf |
| Financial Results Explanatory Material, FY3/2025 | 2025-05-08 | https://www.nintendo.co.jp/ir/pdf/2025/250508_4e.pdf |
| Financial Results Explanatory Material, FY3/2024 | 2024-05-07 | https://www.nintendo.co.jp/ir/pdf/2024/240507_3e.pdf |
| News release, "Notice Regarding Price Revisions for Nintendo Products and Services" | 2026-05-08 | https://www.nintendo.co.jp/corporate/release/en/2026/260508.html |
| Results briefing Q&A, FY3/2026 | 2026-05-08 (posted 05-13) | https://www.nintendo.co.jp/ir/pdf/2026/260511e.pdf |
| Financial Results Explanatory Material (with Notes), Q1 FY3/2027 | 2026-08-06 | https://www.nintendo.co.jp/ir/pdf/2026/260806_2e.pdf |
| "Regarding the Release of Nintendo Switch 2" | 2025-04-02 | https://www.nintendo.co.jp/ir/pdf/2025/250402e.pdf |

Document index obtained from `https://www.nintendo.co.jp/corporate/common/data/news_en.xml` (the IR
library page `ir/en/library/earnings/index.html` renders its list by JavaScript from that XML).

**Extraction artifacts, flagged.** PDF text layers, not OCR. The cash-flow statement text layer is
column-scrambled in both extractors tried (pymupdf and pdftotext -layout: e.g. "Depreciation 15,361
/ 1,555,399 / 415,599 2,613" pulls cells from other rows). **Cash-flow figures below were therefore
read off rendered page images** (`ntdo/2026_annual2603e.p66.png`, `2025_annual2503e.p68.png`,
`2024_annual2403e.p60.png`), not the text layer. The Consolidated Financial Highlights page 1 was
likewise read off images (`2026_260508e.p1.png`, `2025_250508e.p1.png`). Quotes below rejoin PDF
line breaks; the text layer shows "Pokémon Legends: Z-A– Nintendo Switch 2 Edition" with the dash
spacing as printed.

### 2a. Table (¥ millions unless stated)

| | FY3/2024 | FY3/2025 | FY3/2026 |
|---|---|---|---|
| Net sales | 1,671,865 | 1,164,922 | 2,313,051 |
| Operating profit | 528,941 | 282,553 | 360,117 |
| "Operating profit to net sales", as filed (Highlights) | 31.6% | 24.3% | 15.6% |
| of which dedicated video game platforms (revenue note, FY26 classification) | not re-read under new classification | 1,083,534 | 2,239,541 |
| IP related income, etc. | (old class: "mobile and IP related" ¥92.7bn) | 81,388 | 73,510 |
| Depreciation (cash-flow statement) | 17,856 | 15,361 | 15,854 |
| Purchase of PP&E and intangible assets (cash-flow statement) | 16,123 | 19,008 | 27,169 |
| Capex / net sales, COMPUTATION | 0.96% | 1.63% | 1.17% |
| Net cash from operating activities | 462,097 | 12,069 | 289,789 |
| Share of profit of equity-method entities (below operating profit; mainly The Pokémon Company) | 30,099 | 35,125 | 82,792 |
| Hardware units | Switch 15.70m | Switch 10.80m | Switch 2 19.86m; Switch 3.80m |
| Software units | Switch 199.67m | Switch 155.41m | Switch 2 48.71m; Switch 136.91m |
| Digital sales | ¥443.3bn | ¥326.0bn | ¥407.6bn |
| Proportion of digital sales (denominator = platform **software** sales, not total sales) | 50.2% | 53.5% | 54.6% |
| Annual playing users | not re-read | "remains above 100 million" | "exceeded 100 million" |
| Nintendo Switch Online subscribers | **NOT DISCLOSED** in any document read | NOT DISCLOSED | NOT DISCLOSED |

Single segment: capex and depreciation above are consolidated and are the comparable level.
FY3/2023 base, from the same statements: depreciation 11,040; purchase of PP&E and intangibles
22,190; digital sales ¥405.2bn, proportion 48.2%.
Cross-check (operator rule 4 analogue for rung 3): FY3/2026 net sales ¥2,313,051m and operating
profit ¥360,117m match across the Annual Report income statement, its "Consolidated financial data"
table, and the Consolidated Financial Highlights of 2026-05-08.

### 2b. Verbatim source lines

1. Annual Report 2026, MD&A p.17 (PDF page):
   > "In the fiscal year ended March 31, 2026, Nintendo Switch 2 got off to a good start following its launch in June 2025 and global sales continued to grow after that. The March release of Pokémon Pokopia (see note) was a factor in driving further hardware sales toward the end of the fiscal year, helping sales volume reach 19.86 million units for the full term."
   > "Nintendo Switch 2 software unit sales for the fiscal year reached 48.71 million units."
   > "Hardware sales for Nintendo Switch totaled 3.80 million units, demonstrating a level of continued demand for the system, which entered its 10th year since launch in March."
   > "Bolstered by these kinds of factors, Nintendo Switch software sales totaled 136.91 million units."
   > "Turning to the digital business for our dedicated video game platforms, digital sales totaled ¥407.6 billion (USD 2,563 million), up 25.0% year-on-year, mainly due to an increase in sales of downloadable versions of packaged software."
2. Annual Report 2026, MD&A p.18:
   > "Net sales reached ¥2,313.0 billion (USD 14,547 million; an increase of 98.6% year-on-year), of which sales outside of Japan were ¥1,778.1 billion (USD 11,183 million; an increase of 99.8% year-on-year, and 76.9% of total sales). Operating profit came to ¥360.1 billion (USD 2,264 million; an increase of 27.5% year-on-year)"
   > "Gross profit increased from the previous fiscal year by ¥198.7 billion (USD 1,249 million) to ¥908.9 billion (USD 5,716 million; an increase of 28.0% year-on-year). Selling, general and administrative expenses increased from the previous fiscal year by ¥121.2 billion (USD 762 million), mainly due to an increase in research and development expenses and advertising expenses"
3. Annual Report 2025, MD&A p.19:
   > "Hardware sales totaled 10.80 million units (a decrease of 31.2% year-on-year), and software sales totaled 155.41 million units (a decrease of 22.2% year-on-year)."
   > "Turning to our digital business for our dedicated video game platform, digital sales totaled ¥326.0 billion (USD 2,187 million; down 26.5% year-on-year), mainly due to a decrease in sales of Nintendo Switch downloadable versions of packaged software."
   > "Net sales reached ¥1,164.9 billion (USD 7,818 million; a decrease of 30.3% year-on-year) ... Operating profit came to ¥282.5 billion (USD 1,895 million; a decrease of 46.6% year-on-year)"
4. Annual Report 2024, MD&A p.19:
   > "Hardware sales for this period totaled 15.70 million units (a decrease of 12.6% year-on-year), and software sales totaled 199.67 million units (a decrease of 6.7% year-on-year)."
   > "Digital sales reached ¥443.3 billion (USD 2,935 million; an increase of 9.4% year-on-year), helped also by the depreciation of the yen."
   > "Net sales reached ¥1,671.8 billion (USD 11,071 million; an increase of 4.4% year-on-year) ... Operating profit came to ¥528.9 billion (USD 3,502 million; an increase of 4.9% year-on-year)"
5. Annual Report 2026, revenue note (p.92), definition of the platform line:
   > "*1 Includes net sales of hardware (including accessories and amiibo) and software (including downloadable versions of packaged software, download-only software, add-on content and Nintendo Switch Online)."
6. Financial Results Explanatory Material FY3/2026, p.6, digital definition:
   > "*1 Sales of downloadable versions of packaged software, download-only software, add-on content and Nintendo Switch Online, etc." / "*2 Proportion to total dedicated video game platform software sales"
7. Hit dependence, Annual Report 2026:
   > "The presence or lack of hit products and their sales volumes are deemed to have a significant impact on operating results, etc."

### 2c. Pricing (for [E4-37] / [E2-44]); verbatim, dated

1. **News release, 2026-05-08** (https://www.nintendo.co.jp/corporate/release/en/2026/260508.html):
   > "In light of changes in market conditions, and after considering the global business outlook, Nintendo will revise the manufacturer's suggested retail prices (MSRP) of the Nintendo Switch 2 system and Nintendo Switch systems in Japan as follows."
   Japan, effective 2026-05-25: Switch 2 Japanese-Language System ¥49,980 to ¥59,980; Switch (OLED Model) ¥37,980 to ¥47,980; Switch ¥32,978 to ¥43,980; Switch Lite ¥21,978 to ¥29,980 (tax included).
   > "Given that the impact of various changes in market conditions is expected to extend over the medium to long term, price revisions are also planned outside Japan as described below."
   Effective 2026-09-01: United States Switch 2 $449.99 to $499.99 (ex tax); Canada $629.99 to $679.99; Europe (My Nintendo Store) €469.99 to €499.99.
   > "Nintendo Switch Online is offered as a globally unified service, and pricing will be revised to support appropriate alignment among regions."
   Japan, effective 2026-07-01: individual 12 months ¥2,400 to ¥3,000; 1 month ¥306 to ¥400; 3 months ¥815 to ¥1,000; family 12 months ¥4,500 to ¥5,800; NSO + Expansion Pack individual ¥4,900 to ¥5,900, family ¥8,900 to ¥9,900.
   > "We sincerely apologize for the impact these price revisions may have on our customers and other stakeholders, and we deeply appreciate your understanding."
2. **Launch price, 2025-04-02** (250402e.pdf):
   > "Nintendo Switch 2 Japanese-Language System (Japan Only) will be released on June 5, 2025 at a manufacturer's suggested retail price of 49,980 yen (including tax)."
3. **Results briefing Q&A, 2026-05-08, President Furukawa** (260511e.pdf), A3:
   > "If the increase in costs were seen as something temporary that would subside relatively soon, then we could have pursued other options, such as working to improve productivity and expand the installed base while maintaining hardware prices."
   > "As a result, we felt that the profitability of our hardware would suffer significantly if we maintained our existing pricing, potentially impacting our business operations over this time frame. For the sustained growth of our dedicated video game platform business, it is important to maintain a healthy earnings structure for our overall business. For this reason, we made the difficult decision to reflect a portion of our costs in the selling price."
   A4:
   > "I will not discuss the specifics of how this price revision could impact Nintendo Switch 2 sales, but we recognize that this raises the barrier for entry to a certain extent for people deciding whether to make a purchase."
   A2:
   > "the rise in memory and other component prices did not have a major impact on the profitability of the hardware last fiscal year. However, we forecast that prices will continue to rise, and we believe this will gradually put pressure on the profitability of the hardware from this fiscal year onward."
4. **Financial Results Explanatory Material FY3/2026, 2026-05-08** (260508_4e.pdf), pp.10-13:
   > "An impact of approximately 100.0 billion yen due to rising component prices, particularly for memory, and tariff measures has been factored into costs of goods sold."
   > "The impact of these price revisions has also been reflected in our consolidated financial forecast"
   > "Reflecting strong launch-year sales and price revisions, we expect FY27 sales units to decline year-on-year. Even so, we believe this represents a solid level of adoption for Nintendo Switch 2 in its second year after launch"
   FY27 forecast table (company forecast, not a result): Switch 2 hardware 16.50m vs FY26 actual 19.86m ("-16.9 %").
5. **Q1 FY3/2027 Explanatory Material (with Notes), 2026-08-06** (260806_2e.pdf), p.4:
   > "First-quarter sales for Nintendo Switch 2 did not reach the level seen in the same quarter of last fiscal year, which was when the console launched. However, for a hardware system in its second year, sales compare favorably to the adoption trajectory of Nintendo Switch. In the Japanese market, where a price revision took effect on May 25, hardware sell-through has also remained solid."
   p.3:
   > "For the first quarter of the fiscal year, net sales decreased by 9.5% year-on-year to 517.8 billion yen, operating profit rose by 150.5% to 142.5 billion yen"
   > "We recorded approximately 300 million U.S. dollars as a reduction of cost of sales in connection with refunds of IEEPA tariffs. The tariffs related to the refunds were primarily borne by the company rather than passed on to consumers through product prices."

*Reader's note, not a verdict:* the company's own words tie the 2026 increases to cost pass-through
("reflect a portion of our costs in the selling price"), acknowledge a demand effect ("raises the
barrier for entry"), and forecast lower hardware units partly "reflecting ... price revisions". The
US/EU hardware increase took effect 2026-09-01, after every result above; its volume effect is not
yet in any filed document. The NSO subscription increase (Japan, 2026-07-01) has no disclosed
subscriber count against which to test volume.

---
## 3. CONTEXT ONLY: publisher economics (EA, TTWO). Not platform comparables

**Reused from disk, not re-fetched:** `Test Runs/_research 2026-09-03 HAS/competitor_row_games_lego.md`
(HAS run, 2026-09-03), which records the figures as cross-checked against the filed income
statements. EA FY2026 10-K acc 0001628280-26-033617 (a 10-K/A followed, acc 0001308179-26-000382);
TTWO FY2026 10-K acc 0001628280-26-037434. Both March year-ends, so the windows match Sony/Nintendo.

| $ millions | FY3/2024 | FY3/2025 | FY3/2026 |
|---|---|---|---|
| EA net revenue | 7,562 | 7,463 | 7,531 |
| EA operating income | 1,518 | 1,520 | 1,162 |
| EA operating margin (COMPUTATION in HAS file) | 20.1% | 20.4% | 15.4% |
| TTWO net revenue | 5,349.6 | 5,633.6 | 6,656.4 |
| TTWO income (loss) from operations | (3,590.6) | (4,391.1) | (104.2) |
| TTWO operating margin (as filed in TTWO MD&A) | (67.1)% | (78.0)% | (1.5)% |
| TTWO goodwill impairment (context) | 2,342.1 | 3,545.2 | 0 |

Verbatim carried from the HAS file: EA, "Operating income was $1,162 million, down 24 percent
year-over-year." EA on platform terms: "Many key commercial terms of our relationships with Sony
and Microsoft — such as manufacturing terms, delivery times, policies and approval conditions — are
determined unilaterally, and are subject to change by the console manufacturers." TTWO on Sony:
"The agreement requires us to submit products to Sony for approval and for us to make royalty
payments to Sony based on the number of units manufactured or revenue from digitally downloaded
content." and "Sony may terminate the agreement for any or no reason upon 30 days' notice."
Capex/D&A for EA and TTWO: NOT PULLED (context row only).

---
## 4. Summary row (same metric where one exists)

| Peer | Level of disclosure | Revenue FY24 / FY25 / FY26 | Operating margin FY24 / FY25 / FY26 | Units | Filed price statement |
|---|---|---|---|---|---|
| Microsoft gaming | revenue line inside MPC; no profit | $21.5bn / $23.5bn / $21.8bn (June FYs) | **not disclosed** (MPC proxy 23.5% / 25.9% / 26.6%, not gaming) | none filed | none for Xbox after FY2023 "lower volume and price" |
| Nintendo | consolidated = platform business (platform line 93.0% of FY25, 96.8% of FY26 sales, COMPUTATION) | ¥1,671.9bn / ¥1,164.9bn / ¥2,313.1bn | 31.6% / 24.3% / 15.6% (as filed) | hardware and software units, digital share | yes: hardware and NSO increases announced 2026-05-08 |
| EA (context) | consolidated | $7.56bn / $7.46bn / $7.53bn | 20.1% / 20.4% / 15.4% | n/a | not pulled |
| TTWO (context) | consolidated | $5.35bn / $5.63bn / $6.66bn | (67.1)% / (78.0)% / (1.5)% | n/a | not pulled |

---
## 5. NOT OBTAINED, and why

- **Microsoft gaming operating income / margin**: not disclosed in any FY2023-FY2026 10-K. Only MPC segment profit exists, and it mixes Windows, Devices and Search.
- **Microsoft Xbox hardware revenue in dollars**: not disclosed; growth percentages only.
- **Microsoft gaming capex / D&A**: not disclosed; the segment note calls D&A by segment "impracticable" to identify and says assets are not allocated to segments.
- **Microsoft unit metrics** (consoles, Game Pass members, MAU): not filed in FY2023-FY2026 (last filed FY2016 / FY2020 per `segments_units.md`).
- **Microsoft FY2026 XBOX impairment amount**: named in MD&A, amount not stated in any XBOX line of the 10-K.
- **Microsoft Xbox or Game Pass price increases**: no filed statement found (fts_count screen plus reading of 10-K text on disk). Company announcements outside SEC filings were not searched: the brief restricts to filed evidence.
- **Nintendo Switch Online subscriber count**: not disclosed in any of the 13 Nintendo documents read.
- **Nintendo FY3/2024 platform vs IP split under the FY26 classification**: the FY2026 annual report restates only FY3/2025; FY3/2024 is available only under the old "mobile and IP related" label (¥92.7bn) and was not reconciled.
- **Nintendo annual playing users as an exact number**: documents say "above 100 million" / "exceeded 100 million"; the chart values were not transcribed.
- **EA / TTWO capex and D&A**: not pulled (context row, optional in the brief).

---
## 6. Defects found in the brief

1. **"Same window" is impossible for Microsoft.** MSFT's June year-end overlaps Sony's March year by nine months. The brief lists FY2023-FY2025 plus FY2026; the table carries all four, unshifted.
2. **"Gaming operating income or margin" does not exist for Microsoft**, and MPC is not a usable substitute: it contains Windows and Search, and it was **recast in the FY2025 10-K** (FY2023 MPC operating income 16,450 as first filed vs 10,038 recast). A reader pulling MPC from different vintages gets different series.
3. **"Xbox hardware revenue" cannot be supplied as a number**: only growth rates are filed.
4. **Microsoft renamed the line in FY2026** ("XBOX (formerly Gaming)"). Searches on "Gaming revenue" miss the FY2026 figure.
5. **"Nintendo is single-segment, so its consolidated figures are the comparable"** holds for operating profit, but (a) Nintendo is Japanese GAAP while Sony is IFRS, (b) ~3-7% of sales is IP-related income, not platform, and (c) a large and growing equity-method profit from The Pokémon Company (¥82.8bn in FY3/2026) sits below operating profit, so any net-income or ordinary-profit comparison is not like-for-like.
6. **"Digital sales share" is ambiguous**: Nintendo's filed ratio is digital over *software* sales, not over total sales. Sony's comparable (if the main run uses one) must use the same denominator.
7. **Pricing test timing**: the brief asks for price increases "with flat demand"; the Nintendo US/EU hardware increase took effect 2026-09-01, after every period with reported results, so the volume response is not yet observable in filed documents. The Q1 FY3/2027 comment covers Japan only, and on sell-through, not shipments.
8. **Microsoft stopped naming Sony and Nintendo** as console competitors from the FY2025 10-K. If the main run's naming test (a moat is a relative claim) searches MSFT filings for "Sony", FY2025-FY2026 will read zero for this reason; the FY2023-FY2024 naming exists.

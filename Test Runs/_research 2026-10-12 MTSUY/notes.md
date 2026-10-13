# MTSUY research notes (2026-10-12)

Template copied before any fetch.

## Sources (all the company's own documents)
- JPX listed-company page for code 8058 (www2.jpx.co.jp/tseHpFront, 基本情報 > 適時開示情報) lists TDnet PDFs at
  www2.jpx.co.jp/disc/80580/<id>.pdf. mitsubishicorp.com refused (403); EDINET API needs a key; Wayback offline.
- English results FY2023 and FY2024 via LSE RNS PDFs (9867M_1-2024-5-2, 2381H_1-2025-5-2); FY2025 English results
  TDnet 140120260430515680 (also served by www2.infomart.co.jp).
- Raw PDFs and text dumps are in cache/ (gitignored).

## Balance sheets, year-end 31 March, yen bn (決算短信 statements of financial position)
| Mar | total assets | equity to owners | bonds+borrowings | cash | goodwill+intangibles | equity-method inv. | inventories | retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2016 | 14,916 | 4,593 | 6,043 | 1,501 | 291 | 2,870 | 1,034 | 3,226 |
| 2017 | 15,754 | 4,917 | 5,384 | 1,146 | 1,010 | 2,651 | 1,110 | 3,625 |
| 2018 | 16,037 | 5,332 | 4,954 | 1,005 | 1,003 | 3,050 | 1,204 | 3,984 |
| 2019 | 16,533 | 5,696 | 5,092 | 1,161 | 1,036 | 3,191 | 1,214 | 4,357 |
| 2020 | 18,033 | 5,227 | 5,760 | 1,323 | 1,395 | 3,246 | 1,294 | 4,674 |
| 2021 | 18,635 | 5,614 | 5,644 | 1,318 | 1,248 | 3,291 | 1,349 | 4,423 |
| 2022 | 21,912 | 6,880 | 5,643 | 1,556 | 1,222 | 3,503 | 1,777 | 5,204 |
| 2023 | 22,153 | 8,071 | 4,890 | 1,557 | 1,207 | 3,927 | 1,771 | 6,049 |
| 2024 | 23,460 | 9,044 | 5,128 | 1,252 | 743 | 4,501 | 1,724 | 6,452 |
| 2025 | 21,496 | 9,369 | 4,617 | 1,537 | 759 | 5,143 | 1,763 | 6,638 |
| 2026 | 24,152 | 9,441 | 5,747 | 1,841 | 913 | 5,213 | 2,077 | 6,954 |
(March 2020 total assets as restated in the following year's filing, 18,033; first printed 18,050.)

## Scripts
- scripts/owner_cash.py: owner cash by year from the cash-flow statements; scripts/q7.py: the range and fair price;
  scripts/check_ids.py: the citation check; scripts/extract.py: a first-pass label extractor (partial, superseded by
  reading the statements directly).

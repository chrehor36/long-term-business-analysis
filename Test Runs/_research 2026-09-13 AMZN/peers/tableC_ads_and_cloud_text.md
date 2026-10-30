# TABLE C: advertising competitor row, and cloud filed-text sweeps (AMZN run, 2026-09-13)

Research transcription only. No conclusion about Amazon's moat is drawn here. Figures from primary SEC filings on disk, read from the filed text (the on-disk .txt renders of the filed HTML), not from XBRL tags. "computed" marks arithmetic done here; "filed" marks a figure or percentage printed in the filing. All dollar figures in $ millions unless stated.

Search method: `peers/sgrep.py FILE REGEX` (case-insensitive, whitespace collapsed, table pipes stripped). Char offsets quoted as [@N] refer to that collapsed text.

Status: COMPLETE (C.1 to C.7), 2026-09-13.

## SOURCE REGISTER

| Tag | Company | Form | Period | Accession | File on disk |
|---|---|---|---|---|---|
| A25K | Amazon.com | 10-K | FY2025 (Dec 31, 2025) | 0001018724-26-000004 | `_research 2026-09-06 MSFT/AMZN_FY2025_10K.txt` |
| A24K | Amazon.com | 10-K | FY2024 | 0001018724-25-000004 | `AMZN_FY2024_10K.txt` |
| A23K | Amazon.com | 10-K | FY2023 | 0001018724-24-000008 | `AMZN_FY2023_10K.txt` |
| A22K | Amazon.com | 10-K | FY2022 | 0001018724-23-000004 (from file text and `_research 2026-09-13 AMZN/submissions.json`) | `AMZN_FY2022_10K.txt` |
| A21K | Amazon.com | 10-K | FY2021 | 0001018724-22-000005 (same) | `AMZN_FY2021_10K.txt` |
| A26Q2 | Amazon.com | 10-Q | Q2 2026 (Jun 30, 2026) | 0001018724-26-000026 | `_research 2026-09-13 AMZN/10Q_2026Q2.txt` |
| A26Q1 | Amazon.com | 10-Q | Q1 2026 | 0001018724-26-000014 | `10Q_2026Q1.txt` |
| AX25Q3 | Amazon.com | 8-K EX-99.1 | Q3 2025 release | 0001018724-25-000121 | `EX991_2025Q3.txt` |
| AX25Q4 | Amazon.com | 8-K EX-99.1 | Q4 2025 release | 0001018724-26-000002 | `EX991_2025Q4.txt` |
| AX26Q1 | Amazon.com | 8-K EX-99.1 | Q1 2026 release | 0001018724-26-000012 | `EX991_2026Q1.txt` |
| AX26Q2 | Amazon.com | 8-K EX-99.1 | Q2 2026 release | 0001018724-26-000024 | `EX991_2026Q2.txt` |
| G25K | Alphabet | 10-K | FY2025 | 0001652044-26-000018 | `_research 2026-09-06 MSFT/GOOGL_FY2025_10K.txt` |
| G24K | Alphabet | 10-K | FY2024 | 0001652044-25-000014 (submissions_GOOGL.json) | `GOOGL_FY2024_10K.txt` |
| G23K | Alphabet | 10-K | FY2023 | 0001652044-24-000022 (submissions_GOOGL.json) | `GOOGL_FY2023_10K.txt` |
| G21K | Alphabet | 10-K | FY2021 | 0001652044-22-000019 (file header) | `GOOGL_FY2021_10K.txt` (used only for the 2020 base year) |
| G26Q2 | Alphabet | 10-Q | Q2 2026 | 0001652044-26-000071 | `peers/GOOGL_10Q_2026Q2.txt` |
| M25K | Meta Platforms | 10-K | FY2025 | 0001628280-26-003942 | `peers/META_10K_FY2025.txt` |
| M24K | Meta Platforms | 10-K | FY2024 | 0001326801-25-000017 (submissions_META.json) | `_research 2026-09-07 PINS/META_10K_FY2024.txt` (not in the brief's file list; used only for the 2022 figure, flagged) |
| M26Q2 | Meta Platforms | 10-Q | Q2 2026 | 0001628280-26-050705 | `peers/META_10Q_2026Q2.txt` |
| W26K | Walmart | 10-K | FY2026 (Jan 31, 2026) | 0000104169-26-000055 (submissions_WMT.json) | `_research 2026-09-06 WMT/10k-fy2026-text.txt` |
| W27Q2 | Walmart | 10-Q | Q2 FY2027 (Jul 31, 2026) | 0000104169-26-000154 (submissions_WMT.json) | `10q-fy2027q2-text.txt` |
| WX | Walmart | 8-K EX-99.1 earnings releases | see C.1d | accessions from submissions_WMT.json, matched by release date printed in the exhibit | `_research 2026-09-06 WMT/8k-q?fy??-ex991.txt` |
| S26K | Microsoft | 10-K | FY2026 (Jun 30, 2026) | 0001193125-26-323660 | `_research 2026-09-06 MSFT/MSFT_FY2026_10K.txt` |
| O26K | Oracle | 10-K | FY2026 (May 31, 2026) | 0001193125-26-277521 | `_research 2026-09-06 MSFT/ORCL_FY2026_10K.txt` |
| O27Q1 | Oracle | 10-Q | Q1 FY2027 (Aug 31, 2026) | 0001193125-26-389274 | `peers/ORCL_10Q_FY2027Q1.txt` |

---

## C.1 ADVERTISING REVENUE

### C.1a Amazon "Advertising services" (filed; Note 10, Segment Information, table "Net sales by groups of similar products and services")

| Year | Advertising services | y/y (computed) | Read from |
|---|---|---|---|
| 2020 (base) | 19,773 | n/a | A21K Note 10 table (also A22K) |
| 2021 | 31,160 | +57.6% | A21K; same figure in A22K and A23K |
| 2022 | 37,739 | +21.1% | A22K; same in A23K, A24K |
| 2023 | 46,906 | +24.3% | A23K; same in A24K, A25K |
| 2024 | 56,214 | +19.8% | A24K; same in A25K |
| 2025 | 68,635 | +22.1% | A25K Note 10 table [@282494] |
| H1 2025 (six months ended Jun 30) | 29,615 | n/a | A26Q2, segment note table (six-month column) [@75996] |
| H1 2026 | 37,052 | +25.1% | A26Q2 same table |
| Q2 2025 / Q2 2026 (3 months) | 15,694 / 19,809 | +26.2% computed; release files "26 %" y/y and "26 %" y/y excluding F/X | A26Q2 table; AX26Q2 supplemental table [@33170] |

No restatement found: each year's figure is identical in every 10-K on disk that carries it (FY2021 through FY2025 10-Ks compared).

Computed: 2021 to 2025 compound growth 21.8% a year; advertising services share of FY2025 consolidated net sales (716,924) 9.6%.

Filed quarterly y/y growth excluding F/X, Advertising services (AX26Q2 supplemental table, six quarterly columns as printed): "Advertising services -- Y/Y growth, excluding F/X 19 % 22 % 22 % 22 % 22 % 26 %" (the six columns printed in that row correspond to Q1 2025, Q2 2025, Q3 2025, Q4 2025, Q1 2026, Q2 2026; column-to-quarter mapping read from the dollar row above it: "$ 13,921 $ 15,694 $ 17,703 $ 21,317 $ 17,243 $ 19,809").

Footnote definition, verbatim (A25K, Note 10, footnote (4) to the table): "(4)Includes sales of advertising services to sellers, vendors, publishers, authors, and others, through programs such as sponsored ads, display, and video advertising." (extraction artifact: no space after "(4)" in the text render). Same wording as footnote (5) in A21K and A22K, where the row order differed, and as footnote (4) in A26Q2 and AX26Q2.

Revenue recognition, verbatim (A25K, Note 1, Revenue): "Advertising services - We provide advertising services to sellers, vendors, publishers, authors, and others, through programs such as sponsored ads, display, and video advertising. Revenue is recognized as ads are delivered based on the number of clicks or impressions."

Segment location, verbatim (A25K, Note 10): "The North America segment primarily consists of amounts earned from retail sales of consumer products (including from sellers) and advertising and subscription services through North America-focused online and physical stores." The International segment sentence carries the same "advertising and subscription services" wording. Advertising is therefore inside the North America and International segments, not a segment of its own.

Release language (not financial statements; AX26Q1, CEO quote): "Advertising grew to over $70 billion in TTM revenue". AX26Q2, CEO quote: "Advertising had another strong quarter with 26% year-over-year growth."

### C.1b Alphabet advertising (filed; Note 2, Revenues, "Disaggregated Revenues" table; same figures in MD&A "Financial Results, Revenues")

| Year | Google Search & other | y/y | YouTube ads | y/y | Google Network | y/y | Google advertising (total) | y/y | Read from |
|---|---|---|---|---|---|---|---|---|---|
| 2020 (base) | 104,062 | n/a | 19,772 | n/a | 23,090 | n/a | 146,924 | n/a | G21K MD&A table |
| 2021 | 148,951 | +43.1% | 28,845 | +45.9% | 31,701 | +37.3% | 209,497 | +42.6% | G23K Note 2 (identical in G21K) |
| 2022 | 162,450 | +9.1% | 29,243 | +1.4% | 32,780 | +3.4% | 224,473 | +7.1% | G23K Note 2; same in G24K |
| 2023 | 175,033 | +7.7% | 31,510 | +7.8% | 31,312 | -4.5% | 237,855 | +6.0% | G25K Note 2; same in G23K, G24K |
| 2024 | 198,084 | +13.2% | 36,147 | +14.7% | 30,359 | -3.0% | 264,590 | +11.2% | G25K Note 2; same in G24K |
| 2025 | 224,532 | +13.4% | 40,367 | +11.7% | 29,792 | -1.9% | 294,691 | +11.4% | G25K Note 2 [@276943] |
| H1 2025 | 104,892 | n/a | 18,723 | n/a | 14,610 | n/a | 138,225 | n/a | G26Q2 Note 2 [@35161] |
| H1 2026 | 123,670 | +17.9% | 20,938 | +11.8% | 14,274 | -2.3% | 158,882 | +14.9% | G26Q2 Note 2 |
| Q2 2025 / Q2 2026 | 54,190 / 63,271 | +16.8% | 9,796 / 11,055 | +12.9% | 7,354 / 7,303 | -0.7% | 71,340 / 81,629 | +14.4% | G26Q2 Note 2 |

All y/y computed. Computed: Google advertising 2021 to 2025 compound growth 8.9% a year. Filed MD&A dollar changes, G25K: "Google Search & other revenues increased $26.4 billion from 2024 to 2025"; "YouTube ads revenues increased $4.2 billion from 2024 to 2025"; "Google Network revenues decreased $567 million from 2024 to 2025, primarily due to a decrease in AdSense revenues, partially offset by an increase in AdMob revenues."

Segment definitions, verbatim (G26Q2 MD&A): "Google Search & other, which includes revenues generated on Google search properties (including revenues from traffic generated by search distribution partners who use Google.com as their default search in browsers, toolbars, etc.), and other Google owned and operated properties like Gmail, Google Maps, and Google Play; • YouTube ads, which includes revenues generated on YouTube properties; and • Google Network, which includes revenues generated on Google Network properties participating in AdMob, AdSense, and Google Ad Manager."

Computed scale ratio (arithmetic only): Amazon advertising services / Google advertising = 14.9% (2021), 23.3% (2025), 23.3% (H1 2026).

### C.1c Meta advertising (filed; Note 2, Revenue, "Revenue disaggregated by revenue source and by segment"; also MD&A revenue table with filed % change)

| Year | Advertising | y/y computed | y/y filed | Read from |
|---|---|---|---|---|
| 2021 | not on disk | n/a | n/a | see C.7 |
| 2022 | 113,642 | n/a (2021 not on disk) | n/a | M24K MD&A revenue table (file outside brief list, flagged) |
| 2023 | 131,948 | +16.1% | "16 %" (M24K, "2023 vs 2022 % change") | M25K Note 2; same in M24K |
| 2024 | 160,633 | +21.7% | "22 %" (M25K) | M25K Note 2 |
| 2025 | 196,175 | +22.1% | "22 %" (M25K) | M25K Note 2 [@416292], MD&A [@325951] |
| H1 2025 | 87,955 | n/a | n/a | M26Q2 Note 2 [@30559] |
| H1 2026 | 114,387 | +30.1% | "30 %" (M26Q2 MD&A six-month column) | M26Q2 Note 2 and MD&A [@127892] |
| Q2 2025 / Q2 2026 | 46,563 / 59,363 | +27.5% | "27 %" | M26Q2 |

Filed MD&A, verbatim (M25K): "Advertising revenue in 2025 increased $35.54 billion, or 22%, compared to 2024 due to increases in ad impressions delivered and average price per ad." M26Q2: "Advertising revenue in the three and six months ended June 30, 2026 increased $12.80 billion, or 27%, and $26.43 billion, or 30%, respectively, compared to the same periods in 2025, due to increases in ad impressions delivered and average price per ad." Both filings: "the online commerce vertical was the largest contributor to the increase in advertising revenue" (M25K for 2025; M26Q2 for the three and six months ended June 30, 2026).

Computed: Meta advertising 2022 to 2025 compound growth 20.0% a year (Amazon advertising services over the same three years: 22.1% a year). Amazon advertising services / Meta advertising = 35.0% (2025), 32.4% (H1 2026).

### C.1d Walmart global advertising (Walmart fiscal years end January 31; FY2026 = Feb 1, 2025 to Jan 31, 2026)

10-K and 10-Q: no advertising revenue dollar amount and no advertising growth rate filed. Searches run on W26K and W27Q2: "advertising" (25 hits in W26K, 6 in W27Q2; every hit read), and "advertis[a-z]* (business|sales|revenue|net sales|grew|growth|increased)|Walmart Connect|global advertising" (1 hit in W26K, a comparable-sales definition; 0 in W27Q2). What the 10-K/10-Q do file:
- W26K, Note 1: "Financial, Advertising and Other Services The Company recognizes revenue from service transactions at the time the service is performed. Generally, revenue from services is classified as a component of net sales in the Company's Consolidated Statements of Income."
- W26K, Note 1 (vendor money): "certain advertising arrangements" are among supplier payments "accounted for as a reduction of cost of sales".
- W26K, MD&A: "we focus on our mix of businesses, including expanding our ecosystem in higher margin areas, such as digital advertising."
- W27Q2, MD&A (segment discussion, three instances): "Gross profit rate also benefited from continued growth in higher margin businesses, including advertising."
- W26K, Item 1 Competition: Walmart competes with "companies that offer services in digital advertising, fulfillment and delivery services, health and wellness and financial services."

Earnings releases (8-K Item 2.02, EX-99.1; furnished, not part of the 10-K/10-Q financial statements; flagged as a lower rung than the brief's files):

| Walmart period | Filed statement, verbatim | Release date (from exhibit) | 8-K accession | File |
|---|---|---|---|---|
| FY2022 | "Global advertising business 3 reached $2.1 billion"; footnote "3 Our global advertising business includes $1.6 billion recorded in net sales, and $0.5 billion recorded as a reduction to cost of sales, depending on the nature of the advertising arrangement." | February 17, 2022 | 0000104169-22-000009 | 8k-q4fy22-ex991.txt |
| FY2023 | "Global advertising business 3 grew nearly 30% to reach $2.7 billion, led by Walmart Connect in the U.S. and Flipkart Ads." | filed 2023-02-21 | 0000104169-23-000010 | 8k-q4fy23-ex991.txt |
| FY2024 | "Global advertising business 2 grew approximately 28% to reach $3.4 billion" | filed 2024-02-20 | 0000104169-24-000019 | 8k-q4fy24-ex991.txt |
| FY2025 | "Global advertising business 3 grew 27% to reach $4.4 billion" | February 20, 2025 | 0000104169-25-000010 | 8k-q4fy25-ex991.txt |
| FY2026 | "Global advertising business 3 grew 46% to nearly $6.4 billion, including VIZIO" | February 19, 2026 | 0000104169-26-000032 | 8k-q4fy26-ex991.txt |
| Q1 FY2026 (Feb-Apr 2025) | "Global advertising business 3 grew 50%, including VIZIO; Walmart Connect in the U.S. up 31%" | May 15, 2025 | 0000104169-25-000069 | 8k-q1fy26-ex991.txt |
| Q2 FY2026 (May-Jul 2025) | "Global advertising business 3 grew 46%, including VIZIO; Walmart Connect in the U.S. up 31%" | August 21, 2025 | 0000104169-25-000120 | 8k-q2fy26-ex991.txt |
| Q1 FY2027 (Feb-Apr 2026) | "Global advertising business 3 up 37%, with strength across segments. Walmart U.S. advertising up 36%" | May 21, 2026 | 0000104169-26-000095 | 8k-q1fy27-ex991.txt |
| Q2 FY2027 (May-Jul 2026) | "Global advertising business 3 up 38%, with strength across segments. Walmart U.S. advertising up 38%" | August 20, 2026 | 0000104169-26-000145 | 8k-q2fy27-ex991.txt |

The superscript digits ("3", "2") inside the quotes are footnote markers flattened by text extraction. Definition footnote from FY2023 onward, verbatim (e.g. FY2026 release): "Our global advertising business is recorded either in net sales or as a reduction to cost of sales, depending on the nature of the advertising arrangement." (FY2024 to FY2027 releases read "recorded in either net sales"). So Walmart's figure is not a revenue line on the Amazon basis; part is contra cost of sales.

Computed y/y from the rounded filed dollar amounts: FY2023 +28.6% (filed "nearly 30%"); FY2024 +25.9% (filed "approximately 28%"); FY2025 +29.4% (filed "27%"); FY2026 +45.5% (filed "46%", including VIZIO). The computed rates differ from the filed ones because the filed dollars are rounded to $0.1 billion; the filed rates govern. H1 FY2027 dollar amount: not filed (quarterly growth rates only). Computed scale ratio: Walmart FY2026 global advertising (~6,400) / Amazon 2025 advertising services (68,635) = 9.3% (periods offset by one month; Walmart figure includes contra-cost amounts).

---

## C.2 ADVERTISING UNIT METRICS

### Alphabet (filed; MD&A "Monetization Metrics")

Definitions, verbatim (G26Q2 MD&A): "paid clicks and cost-per-click pertain to traffic on Google Search & other properties, while impressions and cost-per-impression pertain to traffic on our Google Network properties." "Cost-per-click is defined as click-driven revenues divided by our total number of paid clicks and represents the average amount we charge advertisers for each engagement by users." "Cost-per-impression is defined as impression-based and click-based revenues divided by our total number of impressions, and represents the average amount we charge advertisers for each impression displayed to users."

| Metric (filed %) | FY2025 vs FY2024 (G25K) | Q2 2026 vs Q2 2025 (G26Q2) | H1 2026 vs H1 2025 (G26Q2) |
|---|---|---|---|
| Google Search & other: paid clicks change | 6% | 13% | 13% |
| Google Search & other: cost-per-click change | 7% | 3% | 4% |
| Google Network: impressions change | (7)% | (12)% | (10)% |
| Google Network: cost-per-impression change | 7% | 13% | 10% |

Verbatim table text, G25K [@190144]: "Google Search & other Paid clicks change 6 % Cost-per-click change 7 % Google Network Impressions change (7) % Cost-per-impression change 7 %". G26Q2 [@139586]: "Three Months Ended Six Months Ended June 30, 2026 June 30, 2026 Google Search & other Paid clicks change 13 % 13 % Cost-per-click change 3 % 4 % Google Network Impressions change (12) % (10) % Cost-per-impression change 13 % 10 %". YouTube: no unit or price metric filed (the metrics cover Search & other and Network only, per the definition above).

### Meta (filed; MD&A "Family of Apps Metrics" and "Revenue")

| Metric (filed) | FY2025 (M25K) | Q2 2026 (M26Q2) | H1 2026 (M26Q2) |
|---|---|---|---|
| Ad impressions delivered, y/y | +12% (2024: +11%) | +14% (Q2 2025: +11%) | +16% (H1 2025: +8%) |
| Average price per ad, y/y | +9% (2024: +10%) | +12% (Q2 2025: +9%) | +12% (H1 2025: +10%) |
| Family daily active people (DAP) | "3.58 billion on average for December 2025, an increase of 7% year-over-year" | "3.60 billion on average for June 2026, an increase of 3% year-over-year" | n/a |

Verbatim, M26Q2 MD&A [@128454]: "During the three and six months ended June 30, 2026, ad impressions delivered increased by 14% and 16%, respectively, year-over-year, as compared with increases of 11% and 8%, respectively, in the same periods in 2025." [@129151]: "During the three and six months ended June 30, 2026, the average price per ad increased by 12% in both periods, year-over-year, as compared with increases of 9% and 10%, respectively, in the same periods in 2025." M25K MD&A [@326351]: "In 2025, ad impressions delivered increased by 12%, as compared with an increase of 11% in 2024, year-over-year." and "In 2025, the average price per ad increased by 9%, as compared with an increase of 10% in 2024". M26Q2 risk factor: "in the first quarter of 2026, we experienced a slight decline on a quarter-over-quarter basis in the total number of Family daily active people that was driven by internet disruptions in Iran, as well as a restriction on access to WhatsApp in Russia."

### Amazon: is any advertising unit or price metric filed?

No advertising volume or price metric (impressions count or change, clicks, price per ad, cost-per-click) is filed in A25K, A26Q2 or A26Q1. Searches and results:

| Regex | A25K | A26Q2 | A26Q1 | AX25Q3 | AX25Q4 | AX26Q1 | AX26Q2 |
|---|---|---|---|---|---|---|---|
| "impressions" | 1 (revenue recognition sentence, "based on the number of clicks or impressions") | 0 | 0 | 0 | 0 | 0 | 0 |
| "price per" | 0 | 0 | 1 (OpenAI investment, "effective price per share") | 0 | 0 | 0 | 1 ("price performance", AWS product) |
| "cost-per" or "cost per" | 0 | 0 | 0 | 0 | 0 | 0 | 2 (see below) |
| "sponsored" | 5 (all the "sponsored ads" definition wording) | 2 (same) | 2 (same) | 1 (footnote) | 1 (footnote) | 2 (footnote; Rufus product bullet) | 1 (footnote) |
| "paid clicks" or "click" | 1 (revenue recognition sentence) | 0 | 0 | 1 ("1-Click shopping") | 1 (same) | 1 (same) | 1 (same) |

The only price-type advertising statement found is a product claim in a release highlight, not a business-wide metric. AX26Q2, verbatim: "Advertisers using Ads Agent see 8% lower cost-per-impression and 6% lower cost-per-acquisition than those that don't use it." (apostrophe rendered as a curly quote in the file). AX26Q1 highlight, verbatim: "Nearly 20% of shoppers who interact with a prompt in Rufus continue the conversation about that brand." AX26Q1 also: "Added Amazon Audiences for advertisers using Amazon Ads to buy advertising on Netflix, enabling brands to use Amazon's proprietary shopping, streaming, and browsing signals, to reach relevant Netflix audiences and drive even stronger performance."

---

## C.3 MARGINS OF THE ADVERTISING BUSINESSES (as filed)

### Alphabet Google Services (filed segment operating income; G25K Note 15 segment table and MD&A; G26Q2 segment note and MD&A)

| Period | Google Services revenues | Google Services operating income | Margin (computed) | OI y/y (computed) |
|---|---|---|---|---|
| 2023 | 272,543 | 95,858 | 35.2% | n/a |
| 2024 | 304,930 | 121,263 | 39.8% | +26.5% |
| 2025 | 342,721 | 139,404 | 40.7% | +15.0% |
| H1 2025 | 159,807 | 65,745 | 41.1% | n/a |
| H1 2026 | 184,177 | 80,133 | 43.5% | +21.9% |
| Q2 2025 / Q2 2026 | 82,543 / 94,540 | 33,063 / 39,544 | 40.1% / 41.8% | +19.6% |

Not a pure advertising margin: Google Services revenue includes "Google subscriptions, platforms, and devices" (48,030 in 2025; 25,295 in H1 2026). Alphabet files no advertising-only operating income (search: "advertising[^.]{0,80}(margin|operating income)" in G25K returned no segment-level advertising profit figure; the segment table is the finest cut). Also "Alphabet-level activities" (−16,760 in 2025) are held outside the segments: "(1)Alphabet-level activities primarily reflect expenses related to our shared AI research and development." Filed MD&A, G25K: "Google Services operating income increased $18.1 billion from 2024 to 2025. The increase in operating income was primarily driven by an increase in revenues, partially offset by an increase in expenses related to legal and other matters, TAC, and content acquisition costs." No margin percentage is filed; margins above are computed.

### Meta Family of Apps (filed segment table; M25K Note on segments [@496630]; M26Q2 [@97961])

| Period | FoA revenue | FoA income from operations | Margin (computed) | OI y/y (computed) |
|---|---|---|---|---|
| 2023 | 133,006 | 62,871 | 47.3% | n/a |
| 2024 | 162,355 | 87,109 | 53.7% | +38.6% |
| 2025 | 198,759 | 102,469 | 51.6% | +17.6% |
| H1 2025 | 89,048 | 46,736 | 52.5% | n/a |
| H1 2026 | 116,278 | 50,294 | 43.3% | +7.6% |
| Q2 2025 / Q2 2026 | 47,146 / 60,370 | 24,971 / 23,394 | 53.0% / 38.8% | −6.3% |

FoA revenue includes "Other revenue" (2,584 in 2025; 1,891 in H1 2026), so this is not an advertising-only margin either; advertising is 98.7% of FoA revenue in 2025 (computed 196,175 / 198,759). Filed M26Q2 MD&A on consolidated costs, verbatim: "The increase in costs and expenses was primarily due to increases in employee compensation, including severance expenses; infrastructure expenses related to our data centers, technical infrastructure, and third-party cloud services; legal-related costs; and third-party AI token costs."

### Amazon: is an advertising margin filed?

Not filed. Searches: regex "advertising[^.]{0,80}(margin|operating income|profit)|(margin|operating income|profit)[^.]{0,80}advertising" returned 0 hits in each of A25K, A26Q2, A26Q1, AX25Q3, AX25Q4, AX26Q1, AX26Q2. Segment operating income is filed only for North America, International and AWS (A25K Note 10: North America operating income 29,619; International 4,750; AWS 45,606 for 2025), and advertising sits inside North America and International per the segment definition quoted in C.1a. This matches the run's Q1 statement that no advertising margin is filed.

---

## C.4 TRAFFIC ACQUISITION COSTS (Alphabet)

Filed, MD&A "Costs and Expenses, Cost of Revenues" table ("cost of revenues, including TAC").

| Period | TAC (filed) | TAC y/y (computed) | TAC rate (filed) | TAC / Google advertising (computed check) | Source |
|---|---|---|---|---|---|
| 2024 | 54,900 | n/a | 20.7% | 20.7% | G25K MD&A [@192379] |
| 2025 | 59,926 | +9.2% | 20.3% | 20.3% | G25K MD&A |
| Q2 2025 | 14,705 | n/a | 20.6% (filed for "three and six months") | 20.6% | G26Q2 MD&A [@141768] |
| Q2 2026 | 16,179 | +10.0% | 19.8% (same) | 19.8% | G26Q2 |
| H1 2025 | 28,453 | n/a | 20.6% | 20.6% | G26Q2 |
| H1 2026 | 31,407 | +10.4% | 19.8% | 19.8% | G26Q2 |

TAC rate definition, verbatim (G25K Item 7, "Trends in Our Business and Financial Effect", subheading "Traffic Acquisition Costs Growth and Rate Changes"): "Our overall TAC as a percentage of our advertising revenues ("TAC rate") has been decreasing primarily due to a revenue mix shift from Google Network properties to Google Search & other properties."

G25K MD&A, verbatim: "The increase in TAC from 2024 to 2025 was largely due to an increase in TAC paid to distribution partners, primarily driven by growth in revenues subject to TAC. The TAC rate decreased from 20.7% to 20.3% from 2024 to 2025, primarily due to a revenue mix shift from Google Network properties to Google Search & other properties. The TAC rates on Google Search & other and Google Network revenues were substantially consistent from 2024 to 2025."

G26Q2 MD&A, verbatim: "The TAC rate decreased from 20.6% to 19.8% from the three and six months ended June 30, 2025 to the three and six months ended June 30, 2026, primarily due to a revenue mix shift from Google Network properties to Google Search & other properties. The TAC rate on Google Search & other revenues was substantially consistent from the three and six months ended June 30, 2025 to the three and six months ended June 30, 2026. The TAC rates on Google Network revenues reflected a slight increase from the three and six months ended June 30, 2025 to the three and six months ended June 30, 2026 due to a combination of factors, none of which were individually significant."

G25K MD&A, verbatim: "TAC as a percentage of revenues generated from ads placed on Google Network properties are significantly higher than TAC as a percentage of revenues generated from ads placed on Google Search & other properties, because most of the advertiser revenues from ads served on Google Network properties are paid as TAC to our Google Network partners."

Split of TAC between distribution partners and Network partners: not filed in G25K or G26Q2 (the GOOGL run's B2 notes date the last filed split to the Q3 2019 10-Q; not re-verified here beyond confirming no split table in G25K/G26Q2: regex "TAC to distribution partners|TAC to Google Network" 0 hits, see C.7).

Meta: no TAC amount filed. "traffic acquisition" appears only in cost-of-revenue descriptions. M25K (2 hits), verbatim: "Cost of revenue also consists of costs associated with partner arrangements, including traffic acquisition costs and credit card and other fees related to processing customer transactions". M26Q2 (1 hit), verbatim: "Cost of revenue also consists of processing fees and traffic acquisition costs, which include credit card and other fees related to processing customer transactions".

Amazon: "traffic acquisition" 0 hits in A25K and A26Q2. No TAC-equivalent line filed.

### C.1e Aside: Microsoft search advertising (filed, not requested, recorded because it is an advertising revenue line in a file already opened)

S26K, Note on revenue by significant product and service offerings (Item 8): "Search advertising 15,176 13,878 12,306" for fiscal years ended June 30, 2026, 2025, 2024 ($ millions). y/y computed: FY2026 +9.4%; FY2025 +12.8%.

---

## C.5 DOES THE PEER FILING NAME AMAZON OR AWS?

Search: regex "Amazon|\bAWS\b" (case-insensitive) over each 10-K, plus "Web Services" as a check.

| Filing | "Amazon" hits | "AWS" hits | "Web Services" hits |
|---|---|---|---|
| G25K (Alphabet 10-K FY2025) | 0 | 0 | 0 |
| M25K (Meta 10-K FY2025) | 0 | 0 | 0 |
| S26K (Microsoft 10-K FY2026) | 0 | 0 | 0 |
| O26K (Oracle 10-K FY2026) | 4 (in 3 sentences) | 0 as a standalone token | 2 |
| Also checked: G26Q2, M26Q2, O27Q1 | 0 each | 0 each | 0 each |

No instance found in G25K, M25K or S26K of Amazon or AWS being named. What those three name instead, verbatim, for context:

- G25K, Item 1, Competition (list of categories, no company named): "We face formidable competition in every aspect of our business, including but not limited to, from: •general purpose search engines and information services; •vertical search engines and e-commerce providers for queries on topics such as those related to travel, jobs, and health, which users may navigate directly to rather than go through Google; •online advertising platforms and networks, including online shopping and streaming services; ... •providers of enterprise cloud services; •AI model developers and providers of AI products and services; ..." (ellipses mine; omitted bullets are other categories). Also: "users, for whom other products and services are literally one click away".
- M25K, Item 1, Competition (no company named in the section opening): "We compete with companies providing connection, sharing, discovery, and communication products and services to users online, as well as companies that sell advertising to businesses looking to reach consumers and/or develop tools and systems for managing and optimizing advertising campaigns." Meta's risk factors do name TikTok ("competitive products and services, such as TikTok, that have reduced some users' engagement with our products and services"), not Amazon.
- S26K, Item 1, Competition: "Azure faces diverse competition from cloud service providers and open-source offerings." and "Our AI offerings compete with AI products from hyperscalers, as well as products from other emerging competitors and other open-source offerings, many of which are also current or potential partners." ("hyperscalers" unnamed.)

Oracle O26K, every sentence naming Amazon or AWS, verbatim:

1. Item 1, Business, "Competition": "Our enterprise cloud, software and hardware offerings compete directly with certain offerings from some of the largest and most competitive companies in the world, including Adobe Systems Incorporated, Alphabet Inc., Amazon.com, Inc., Cisco Systems, Inc., Intel Corporation, International Business Machines Corporation, Microsoft Corporation, Salesforce, Inc. and SAP SE, as well as other companies like Hewlett-Packard Enterprise and Workday, Inc."
2. Item 1, Business, "Information about our Executive Officers" (biographical, not competitive): "Prior to joining Oracle, he was a senior engineer at Amazon and Amazon Web Services from 2008 to 2014." (Mr. Magouyrk, Chief Executive Officer.)
3. Item 1A, Risk Factors: "OCI's multicloud services work with a number of our competitors' products, including Microsoft Azure, Amazon Web Services and Google Cloud." (surrounding sentences quoted in C.6.)

### Amazon A25K on advertising competition and AWS competition, verbatim

- Item 1, Business, "Competition": "Our current and potential competitors include: (1) physical, e-commerce, and omnichannel retailers, publishers, vendors, distributors, manufacturers, and producers of the products we offer and sell to consumers and businesses; (2) publishers, producers, and distributors of physical, digital, and interactive media of all types and all distribution channels; (3) web search engines, comparison shopping websites, social networks, web portals, virtual assistants, and other online and app-based means of discovering, using, or acquiring goods and services, either directly or in collaboration with other retailers, including through artificial intelligence; (4) companies that provide e-commerce services, including website development and hosting, omnichannel sales, inventory and supply chain management, advertising, fulfillment, customer service, and payment processing; (5) companies that provide fulfillment and logistics services for themselves or for third parties, whether online or offline; (6) companies that provide information technology services or products, including on-premises or cloud-based infrastructure, tools and services relating to artificial intelligence, and other services; (7) companies that design, manufacture, market, or sell consumer electronics, communications, and other electronic devices and services; (8) companies that sell grocery products online and in physical stores; (9) companies that provide advertising services, whether in digital or other formats; and (10) providers of virtual or in-person healthcare services."
- Same section: "We believe that the principal competitive factors in our retail businesses include selection, price, and convenience, including fast and reliable fulfillment. Additional competitive factors for our seller and enterprise services include the quality, speed, and reliability of our services and tools, as well as customers' ability and willingness to change business practices."
- Same section: "Some of our current and potential competitors have greater resources, longer histories, more customers, greater brand recognition, and greater control over inputs critical to our various businesses. They may secure better terms from suppliers, adopt more aggressive pricing, pursue restrictive distribution agreements that restrict our access to supply, direct consumers to their own offerings instead of ours, lock-in potential customers with restrictive terms, and devote more resources to technology, infrastructure, fulfillment, and marketing."
- Item 1A, "We Face Intense Competition": "Our businesses are rapidly evolving and intensely competitive, and we have many competitors across geographies, including cross-border competition, and in different industries, including physical, e-commerce, and omnichannel retail, e-commerce services, web and infrastructure computing services, electronic devices, digital content, advertising, grocery, healthcare, communications, and transportation and logistics services." And: "In addition, new and enhanced technologies, including search, web and infrastructure computing services, practical applications of artificial intelligence and machine learning, digital content, satellites, and electronic devices continue to increase our competition." And: "As a result of competition, our product and service offerings may not be successful, we may fail to gain or may lose business, and we may be required to increase our spending or lower prices, any of which could materially reduce our sales and profits."
- Item 1A (regulatory): "For example, we face a number of open investigations based on claims that aspects of our operations infringe competition-related or consumer protection rules or regulations, including aspects of Amazon's operation of its stores, including its fulfillment network and Prime, and certain aspects of AWS's offering of cloud services."
- Item 8, Note 7 - Commitments and Contingencies, legal proceedings (advertising practices named in allegations): "Some of the cases include allegations that Amazon has a monopoly in markets for online superstores, marketplace services, or intermediation services and that we unlawfully engage in anticompetitive practices relating to our pricing policies, selection of the Featured Offers, use of seller data, advertising practices, the structure of Prime, and promotion of our own products on our website."
A25K names no competitor company: "Microsoft", "Google", "Oracle" each 0 hits in A25K.

---

## C.6 CLOUD MULTI-SOURCING, SWITCHING, AND CROSS-HOSTING: FILED TEXT

### Hit counts (case-insensitive; whitespace-collapsed text)

| Term (regex) | A25K | A26Q2 | S26K | G25K | G26Q2 | O26K | O27Q1 |
|---|---|---|---|---|---|---|---|
| "multi-?cloud" | 0 | 0 | 2 | 0 | 1 | 11 | 0 |
| "multiple cloud" | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| "hybrid" | 0 | 0 | 4 | 0 | 0 | 10 | 1 |
| "\bswitch" | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| "migrat" | 0 | 0 | 3 (1 cloud, 2 immigration) | 3 (2 product, 1 immigration) | 0 | 9 | 1 |
| "interoperab" | 0 | 0 | 1 | 1 | 2 | 9 | 1 |
| "egress" | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| "data transfer" | 0 | 0 | 0 | 2 (privacy law) | 1 (privacy law) | 0 | 0 |
| "Azure" | 0 | 0 | 28 | 0 | 0 | 1 | 0 |
| "Google Cloud" | 0 | 0 | 0 | 49 | 43 | 1 | 0 |
| "\bOCI\b" | 0 | 0 | 0 | 0 | 0 | 36 | 0 |
| "Database@", "@AWS", "@Azure", "@Google" | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| "Amazon" / "AWS" | n/a | n/a | 0 / 0 | 0 / 0 | 0 / 0 | 4 / 0 | 0 / 0 |

"Oracle Database@AWS" or any "Database@" partnership name: no instance found in any of the seven files. The nearest filed language is Oracle's unnamed "Multicloud Database offerings" (below).

### Amazon (A25K, A26Q2)

No instance found of any switching, multi-cloud, hybrid, migration, interoperability, egress or data-transfer term in A25K or A26Q2 (all 0, table above). The only filed A25K text touching on customer change is the competitive-factor clause quoted in C.5: "customers' ability and willingness to change business practices."

Release (AX25Q4; a model-level, not provider-level, statement; contains the filing's own em dash): "Added 20+ fully-managed models on Amazon Bedrock, including from Amazon Nova as well as Anthropic, Google, OpenAI, NVIDIA, Qwen, Mistral AI, Stability AI, Cohere, MiniMax AI, and Moonshot AI—enabling customers to test and switch between models without rewriting code while accessing breakthrough capabilities in coding, reasoning, and agentic workflows." (leading bullet character dropped.)

AX26Q1 lists Meta among new AWS agreements, verbatim: "Announced new AWS agreements with OpenAI, Anthropic, Meta, NVIDIA, Uber, U.S. Bank, Fox Corporation, Southwest Airlines, U.S. Army, Bloomberg, Cerebras, AT&T, DTCC, Nokia, Fundamental, The National Geographic Society, NEURA Robotics, DXC, PGA TOUR, O2 Telefónica, NTT DOCOMO, Veolia, The Evri Group, Telenor, ModMed, Yotta Data Services, Parrot Analytics, U.S. Hunger, TGS, and more." (Meta's own M26Q2 describes "third-party cloud capacity arrangements" without naming a provider: "As of June 30, 2026, we had $349.31 billion of non-cancelable contractual commitments, comprising both short-term and long-term arrangements, most of which are related to third-party cloud capacity arrangements and other investments in technical infrastructure, and we continue to enter into additional significant contractual arrangements." Amazon, AWS: 0 hits in M26Q2.)

### Microsoft (S26K)

- Item 1: "We prioritize security above all else and we offer our customers integrated AI-driven products addressing security, compliance, identity, management, and privacy across customers' multi-cloud, application, and device assets."
- Item 1, Competition: "Azure's competitive advantage includes enabling a hybrid cloud, allowing deployment of existing datacenters with our public cloud into a single, cohesive infrastructure, and the ability to run at a scale that meets the needs of businesses of all sizes and complexities."
- Item 1A (platform competition; the one "switch" hit, context is devices and app marketplaces, not cloud): "Users may incur costs to move data and buy new content and applications when switching platforms."
- Item 7, MD&A, Intelligent Cloud: "Server products revenue increased 1% primarily driven by higher purchases of licenses running in multi-cloud environments, offset in part by continued customer shift to cloud."
- Item 1A (AI partners as Azure customers): "Our AI strategy also depends in part on strategic relationships with third parties that provide technologies, models, products, and services that enhance our offerings. These relationships may change over time, and many of these partners compete with us with respect to certain products and services. ... In some cases, these parties are significant customers of Azure and other cloud services. The economic benefits we expect to derive from these relationships, including through commercial arrangements, technology access, and Azure consumption, may not be realized or sustained. As we manage infrastructure capacity constraints and evolving customer demand, we may modify capacity allocations, deployment priorities, pricing, or other commercial arrangements. Strategic partners and other customers may likewise adjust their purchasing decisions, deployment strategies, workloads, or anticipated use of our products and services." (ellipsis mine; omitted sentence: "Changes in strategic priorities, contractual arrangements, our access to third-party technologies, or key commercial relationships could adversely affect the competitiveness of our AI products and services.")
- Item 1A: "The financial success of these investments depends on a number of uncertain factors, including customer demand for cloud-based and AI products and services and continued customer use of Azure to build, train, deploy, and run AI workloads, our ability to price and monetize those services at levels sufficient to recover our costs, competitive dynamics affecting pricing, and the pace of adoption of AI."
- Item 8, related party (OpenAI as customer): "For fiscal year 2026, we recorded revenue from commercial arrangements with OpenAI, inclusive of revenue-sharing payments, of $24.1 billion, and accounts receivable from OpenAI as of June 30, 2026 was $6.0 billion."

### Alphabet (G25K, G26Q2)

- G25K, Item 1 (Google Cloud product description; "migrate" in a product sense): "It can be used to migrate and modernize information technology (IT) systems and to train and serve various types of AI models." And: "•Data and Analytics: enables customers to migrate, clean, prepare, and feed data into their models."
- G25K, Item 1A (regulation; the only cloud-switching-adjacent legal text): "and the EU Data Act, which introduces new data portability requirements with respect to connected products (i.e., 'internet of things' products) and related services, as well as interoperability obligations on data processing services." G26Q2 Item 1A carries the same EU Data Act clause.
- G26Q2, Item 1, Note on acquisitions (Wiz): "This acquisition represents an investment by Google Cloud to accelerate our capabilities in multicloud and AI-driven security." (preceding sentence: "ur acquisition of Wiz for $ 29.5 billion, after purchase price adjustments and excluding post combination compensation arrangements", truncated start is a window artifact.)
- No sentence found in G25K or G26Q2 stating that Google Cloud customers use more than one provider, or that Google Cloud hosts another hyperscaler's service.

### Oracle (O26K, O27Q1)

- O26K, Item 1: "These models include cloud-based, on-premise and hybrid deployments, such as Oracle Exadata Cloud@Customer and multicloud options that enable customers to use Oracle cloud offerings in conjunction with other public clouds."
- O26K, Item 1: "•connectable among differing deployment models to enable interoperability and extensibility to easily move workloads among the Oracle Cloud, multicloud and other IT environments;"
- O26K, Item 1: "We continue to invest in OCI to improve features and performance; to expand the catalog of cloud-based infrastructure tools and services that we provide; to increase the capacity and geographic footprint to deliver these services; to simplify the processes for migrating workloads to the Oracle Cloud; and to provide customers with the ability to run workloads across different IT environments, the Oracle Cloud as well as other third-party clouds in both multicloud and hybrid deployment models."
- O26K, Item 1: "In addition, our OCI offerings include networking, connectivity and edge services that help connect customers' data centers and third-party clouds with our OCI services for the creation of distributed and multicloud architectures."
- O26K, Item 1 (cross-hosting): "•Oracle's Multicloud Database offerings, which are designed to enable organizations to deploy and run Oracle AI Database services, Oracle Autonomous AI Database and Oracle Zero Data Loss Autonomous Recovery Service within other hyperscale cloud IT environments. This allows customers to leverage AI and analytics services from their cloud providers with their enterprise data;"
- O26K, Item 1: "In addition, Oracle Autonomous AI Database is available in multicloud deployments on other hyperscale cloud IT environments."
- O26K, Item 1: "Oracle AI Database may be deployed in various IT environments, including Oracle Public Cloud, Oracle Exadata Cloud@Customer, OCI Dedicated Region, Oracle Alloy, Oracle multicloud, other cloud-based IT environments and on-premise data centers, among others."
- O26K, Item 1: "We offer our Oracle Engineered Systems through flexible deployment options, including on-premise, as a cloud offering in OCI, as a platform for Oracle AI Database services in Oracle multicloud partner data centers and as a hybrid cloud offering in customer data centers."
- O26K, Item 1: "We believe that we can market and sell our Oracle Cloud offerings together to help new and existing customers migrate their extensive installed base of on-premise and cloud-based applications and infrastructure technologies to the Oracle Cloud and we believe we are in the early stages of what we expect will be a material migration of our existing Oracle customer base from on-premise applications and infrastructure products and services to the Oracle Cloud."
- O26K, Item 1A, Risk Factors (the full passage around the AWS naming): "In addition, use of our competitors' technologies can influence a customer's purchasing decision or create an environment that makes it less efficient to utilize or migrate to Oracle products and services. For example, we offer our customers multicloud services whereby our customers can combine cloud services from multiple clouds with the goal of optimizing cost, functionality and performance. OCI's multicloud services work with a number of our competitors' products, including Microsoft Azure, Amazon Web Services and Google Cloud. This multicloud strategy could lead our customers to migrate away from our cloud offerings to our competitors' products or limit their purchases of additional Oracle products, either of which could adversely affect our revenues and profitability."
- O27Q1, Item 2: "These models include cloud-based, on-premise and hybrid deployments." And: "To address customer demand and enable customer choice, we have certain programs for customers to pivot their applications and infrastructure software licenses and the related software support to the Oracle Cloud for new deployments and to migrate to and expand with the Oracle Cloud for their existing workloads." No multicloud, Amazon, AWS, Azure or Google Cloud hit in O27Q1.
- O27Q1, Note 1 and Item 2 (RPO, for scale only): "Remaining performance obligations were $ 664 billion as of August 31, 2026 , of which we expect to recognize approximately 13 % as revenues over the next twelve months , 37 % over the subsequent month 13 to month 36 , 34 % over the subsequent month 37 to month 60 and the remainder thereafter." (spaces before commas and % are extraction artifacts.) Item 2: "The increase in remaining performance obligations as of August 31, 2026 in comparison to August 31, 2025 was primarily attributable to certain significant cloud contracts that were entered into during the period."

### Amazon statements on AWS pricing (A25K, A26Q2, AX25Q3 to AX26Q2)

Search: regex "lower prices|price reduction|pricing changes|pricing|\bprices?\b|long-term customer contracts" in A25K and A26Q2; "pric|lower cost|cost-effective|cheaper" in the four releases. Every AWS-related hit:

- A25K, Item 7, MD&A, Net Sales: "AWS sales increased 20% in 2025, compared to the prior year. The sales growth primarily reflects increased customer usage, partially offset by pricing changes primarily driven by long-term customer contracts."
- A25K, Item 7, Operating Income: "The increase in AWS operating income in 2025, compared to the prior year, is primarily due to increased sales, partially offset by spending on technology infrastructure that was primarily driven by additional investments to support AWS business growth."
- A26Q2, Item 2, MD&A, Net Sales: "AWS sales increased 37% in Q2 2026, and 33% for the six months ended June 30, 2026 compared to the comparable prior year periods. The sales growth primarily reflects increased customer usage, partially offset by pricing changes primarily driven by long-term customer contracts."
- A26Q2, Item 2, Operating Income: "The increase in AWS operating income in Q2 2026 and for the six months ended June 30, 2026, compared to the comparable prior year periods, is primarily due to increased sales, partially offset by spending on technology infrastructure that was primarily driven by additional investments to support AWS business growth."
- A25K Note 1, AWS revenue recognition: "Revenue is allocated to services using stand-alone selling prices and is primarily recognized when the customer uses these services, based on the quantity of services rendered, such as compute or storage capacity delivered on-demand."
- AX25Q4 highlight: "Used by over 90% of the top 1,000 AWS customers, Graviton is up to 40% more price-performant than leading x86 processors, and enables applications to run faster, reduce costs, and meet sustainability goals."
- AX26Q2 highlight: "Graviton delivers up to 30 to 40% better price-performance than comparable instances, and Graviton5 delivers up to 25% better compute performance than Graviton4." And: "Kiro is up to 50% more cost-effective than alternatives and tripled in usage quarter-over-quarter."
- AX26Q1 highlight: "Partnered with Uber to put Graviton4 chips to work on millions of daily rides and deliveries—matching riders with drivers in fractions of a second at lower cost—and leveraging Trainium3 to train the Al models that make every ride smarter over time." ("Al" for "AI" is an extraction or source typo; recorded as found.)
- AX25Q3: no AWS pricing statement found.
- No instance found of an AWS "price reduction" or "lower prices" statement specific to AWS in A25K or A26Q2 (the "lower prices" hits are retail: "To decrease our variable costs on a per unit basis and enable us to lower prices for customers, we seek to increase our direct sourcing, increase discounts from suppliers, and reduce defects in our processes.").

### AWS customer commitments, concentration and RPO (A26Q2, verbatim)

- A26Q2, Note 1, "Unearned Revenue": "Additionally, we have performance obligations, primarily related to AWS, associated with commitments in customer contracts for future services that we expect to fulfill but have not yet been recognized in our financial statements. For contracts with original terms that exceed one year, those commitments not yet recognized were approximately $ 496 billion as of June 30, 2026. The weighted-average remaining life of our long-term contracts is 6.4 years. The amount and timing of revenue recognition will be driven by customer usage and our performance in accordance with contractual obligations, which can extend beyond the original contractual duration and commitment. In Q1 2026, AWS and OpenAI Group PBC ("OpenAI") announced an expansion of the existing $ 38.0 billion multi-year commitment and commercial arrangement with OpenAI by $ 100.0 billion over 8.0 years, which includes contractual obligations related to the performance of AWS chips. In Q2 2026, AWS and Anthropic announced an expansion of the strategic collaboration and existing multi-year commitment by more than $ 100.0 billion over 10.0 years, which includes contractual obligations related to the performance of AWS chips."
- Comparison, A25K Note 1: "For contracts with original terms that exceed one year, those commitments not yet recognized were approximately $244 billion as of December 31, 2025. The weighted average remaining life of our long-term contracts is 4.1 years."
- Computed: $496 billion less $244 billion = $252 billion increase in six months; the two filed expansions sum to $100.0 billion (OpenAI) plus "more than $ 100.0 billion" (Anthropic) = more than $200 billion. Arithmetic only: the filing does not state what share of the $496 billion is OpenAI or Anthropic; a concentration percentage is not filed (see C.7).
- A26Q2, Note 2, Financial Instruments, OpenAI: "OpenAI — In Q1 2026, we and OpenAI entered into (i) a commercial arrangement primarily for the provision of AWS cloud services, which includes the use and performance of AWS chips, and (ii) a joint collaboration agreement pursuant to which certain services using OpenAI models will be made available to the Company and on AWS."
- A26Q2, Note 2, Anthropic: "In Q2 2026, we invested $ 5.0 billion in Anthropic Series G nonvoting preferred stock. We also amended our commercial arrangement primarily for the provision of AWS cloud services, which includes contractual obligations related to the performance of AWS chips. Additionally, we entered into a financing arrangement to make available to Anthropic an aggregate facility not to exceed $ 20.0 billion that will expire 30 months after an Anthropic liquidity event, including an initial public offering ("IPO"). At inception, there is no amount available to be drawn against and as we reach certain delivery milestones of compute capacity under the amended commercial arrangement, amounts under this facility are made available for Anthropic to draw upon at its discretion."
- A26Q2, Note 2: "As of December 31, 2025 and June 30, 2026, equity investments in private companies not accounted for under the equity-method, which primarily relate to nonvoting preferred stock in Anthropic and preferred stock in OpenAI, had a carrying value of $ 16.2 billion and $ 122.3 billion".
- A26Q2, Note 2: "Subsequent to June 30, 2026, we invested the remaining $ 21.3 billion Commitment Amount in shares of Series C Preferred Stock of OpenAI."
- A26Q2, Note 4, Commitments and Contingencies (names NVIDIA and Microsoft as co-defendants, not as competitors): "In May 2026, Xockets filed a complaint against Amazon.com, Inc., Amazon Web Services, Inc., Annapurna Labs (U.S.), Inc., NVIDIA Corporation, and Microsoft Corporation at the United States International Trade Commission alleging, among other things, that EC2 P6e-GB200 UltraServers, DGX Cloud with GB200 on AWS, SageMaker HyperPod, and EKS with P6e-GB200 UltraServers infringe U.S." (sentence continues past "U.S." in the filing; cut by the sentence splitter at the abbreviation.)
- Releases, capacity commitments (AX26Q1): "Secured a commitment from OpenAI to consume approximately two gigawatts (GW) of Trainium capacity through AWS infrastructure to power its frontier models and advanced workloads, which begins ramping in 2027." And: "Announced that Anthropic will secure up to five gigawatts (GW) of current and future generations of Amazon's Trainium chips to train and power their advanced AI models."

Extraction note: amounts in A26Q2 notes render as "$ 496 billion" with a space after "$" (XBRL inline tagging artifact); kept as found.

---

## C.7 NOT OBTAINED

| Item | Status | Search run |
|---|---|---|
| Meta advertising revenue FY2021 (and FY2020 base; so FY2022 y/y) | Not on disk. M25K covers 2023-2025, M24K covers 2022-2024. No Meta FY2021 or FY2022 10-K found in the repository (`find` for "*meta*" filenames). Companyfacts JSON has no advertising dimension. Not fetched: the brief limits sources to filings on disk. | file search; sgrep "Advertising [\$ ]*[0-9]{2,3},[0-9]{3}" in M24K, M25K |
| Walmart global advertising in the 10-K or 10-Q (dollars or growth) | Not filed in W26K or W27Q2. Obtained only from 8-K EX-99.1 releases (C.1d). | "advertising" (all 25 + 6 hits read); "advertis[a-z]* (business\|sales\|revenue\|net sales\|grew\|growth\|increased)\|Walmart Connect\|global advertising" |
| Walmart global advertising dollars for H1 FY2027 or H1 FY2026 | Not filed (quarterly growth rates only in releases). | releases q1fy26, q2fy26, q1fy27, q2fy27 read for "advertising" |
| Walmart advertising FY2022 growth rate | Not in the FY2022 release window read (dollar amount $2.1 billion only). | sgrep "advertising" in 8k-q4fy22-ex991.txt (3 hits) |
| Amazon advertising unit metrics (impressions, clicks, price per ad) | Not filed. | see C.2 table |
| Amazon advertising operating income or margin | Not filed. | see C.3 |
| Alphabet advertising-only operating income or margin | Not filed; Google Services includes subscriptions, platforms and devices. | "advertising[^.]{0,80}(margin\|operating income)" in G25K, G26Q2: 0 |
| Meta advertising-only operating income | Not filed; FoA includes other revenue. | segment table read |
| Alphabet YouTube unit or price metrics | Not filed. | monetization metrics table read in G25K, G26Q2 |
| Alphabet TAC split (distribution partners vs Network partners) | Not filed in G25K, G26Q2. | "TAC to distribution partners\|TAC to Google Network": 0 |
| Meta and Amazon TAC amounts | Not filed. | "traffic acquisition" (M25K 2, M26Q2 1, descriptive only; A25K 0, A26Q2 0) |
| Meta FY2025 or H1 2026 daily active people for Facebook alone | Not searched beyond Family DAP (not requested). | n/a |
| Share of Amazon's $496 billion commitments attributable to OpenAI or Anthropic | Not filed. | read full Unearned Revenue paragraph in A26Q2; "OpenAI\|Anthropic\|performance obligation\|backlog" sentence sweep |
| Any peer 10-K naming Amazon or AWS as a competitor, other than Oracle | No instance found in G25K, M25K, S26K (also G26Q2, M26Q2, O27Q1). | "Amazon\|\bAWS\b\|Web Services" |
| "Oracle Database@AWS" or other "@" partnership naming | No instance found in A25K, A26Q2, S26K, G25K, G26Q2, O26K, O27Q1. | "Database@\|@AWS\|@Azure\|@Google" |
| Egress fees or data-transfer charges as a switching cost | No instance found in the seven C.6 files ("data transfer" hits in G25K/G26Q2 are privacy-law text). | "egress", "data transfer" |
| Amazon filed statement on AWS price reductions | No instance found in A25K, A26Q2; only "pricing changes primarily driven by long-term customer contracts" and release price-performance claims. | see C.6 |
| MSFT 10-Q FY2026 Q2 (`peers/MSFT_10Q_FY2026Q2.txt`, accession 0001193125-26-027207 per file header) | Not swept: C.6 list in the brief names the MSFT FY2026 10-K only. | n/a |

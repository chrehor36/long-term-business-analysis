# COMPETITOR ROW: spread-based annuity insurers (research file, 2026-09-13)

Research agent output for the BN run. Facts only, no conclusions. Every figure carries document,
fiscal year, filing date and accession. Text extracts saved in this folder (`*_10K_FY*.txt`,
`BWS_20F_FY*.txt`, produced by `fetch.py` from sec.gov Archives with the SEC User-Agent).
Definitions differ between filers; they are quoted, not reconciled.

Status: COMPLETE 2026-09-13 (sections appended in order; summary table at the end).

---
## 1. BROOKFIELD WEALTH SOLUTIONS (BNT, CIK 0001837429) - the subject

Documents read (text extracts in this folder):
| FY | Form | Filed | Accession | File |
|---|---|---|---|---|
| 2025 | 20-F | 2026-03-26 | 0001837429-26-000008 | BWS_20F_FY2025.txt |
| 2024 | 20-F | 2025-03-27 | 0001837429-25-000009 | BWS_20F_FY2024.txt |
| 2023 | 20-F | 2024-03-28 | 0001837429-24-000006 | BWS_20F_FY2023.txt (filer then Brookfield Reinsurance, doc bamr-20231231) |

### Perimeter by year (as the 20-F states it)
- **FY2023**: "operating subsidiaries, North End Re Ltd., North End Re (Cayman) SPC, Brookfield Annuity Company, American National Group, LLC and Argo Group International Holdings, Inc." (FY2023 20-F, Parent Company note). Segments: Direct Insurance, Reinsurance, PRT. Argo closed November 16, 2023 (partial year). AEL held as an approximately 20% equity stake plus a reinsurance treaty, not consolidated. Total investments $39,838M at 12/31/2023.
- **FY2024**: "operating subsidiaries, which are: North End Re Ltd. ("NER Ltd."), North End Re (Cayman) SPC ("NER SPC"), Brookfield Annuity Company ("BAC"), American National Group Inc. ("ANGI") and Argo Group International Holdings, Inc." (FY2024 20-F). "In May 2024, American Equity Investment Life Holding Company ("AEL") became a wholly-owned subsidiary" (FY2025 20-F MD&A). AEL consolidated from May 2024 (about 8 months of FY2024). Total investments $92,966M at 12/31/2024.
- **FY2025**: "American National Group Inc. ("ANGI"), Clearbrook Group Holdings Inc. ("Clearbrook", renamed from Argo Group International Holdings, Inc. in January 2026), Blumont Annuity Company ("BAC Canada"), Blumont Annuity Company UK Ltd ("BAC UK"), North End Re Ltd. ("NER Ltd.") and North End Re (Cayman) SPC" (FY2025 20-F, MD&A Overview). Segments: Annuities, P&C, Life Insurance, Corporate and Other. Total investments $110,044M at 12/31/2025. **Just Group is NOT in FY2025**: the 20-F calls it a "proposed acquisition" expected to close "on or about April 1, 2026".

### (a) Spread metric
**Not filed in the BWS 20-F for any of FY2023-FY2025.** Searched all three 20-F texts for "gross spread", "cost of funds", "net investment spread" with a percentage, and every "%" adjacent to yield / return / spread / rate: the only hits are option-valuation inputs, debt coupons and product definitions. The 20-F uses "net investment spread" only as a product description (FY2023 20-F: "Insurers earn income on FIA contracts based on a net investment spread, which is the difference between income generated on investments supporting the liabilities and the interest that is credited to policyholders.").
The spread table quoted in the brief (NII 5.01%, real-asset gains 0.69%, cost of funds (3.45)%, gross spread 2.25%, average invested insurance assets $112,700M) appears in **Brookfield Corporation's** FY2025 40-F MD&A (and BN 6-K Q2 2026 releases in the parent folder), not in the BWS 20-F. BN's filing, BN's perimeter. It includes real-asset gains (0.69%) and a P&C cost of funds leg (0.55%).

Nearest filed items in the BWS 20-F (not a spread; different construction):
- **Weighted average crediting rate, Annuities PAB** (Note 18, whole-percent rounding as filed): FY2025 **4%**; FY2024 **4%**; FY2023 **2%**. Interest credited to annuity PAB $3,097M (2025), $2,484M (2024), $472M (2023). Annuity PAB end of year $89,371M / $80,046M / $22,456M. (FY2025 20-F Note 18; the FY2024 rollforward includes "Acquisition from business combination" $61,296M.)
- **Net investment income** (consolidated statement of operations, FY2025 20-F): $5,819M (2025), $4,264M (2024), $1,809M (2023). Investment related gains $485M / $369M / $425M. Net investment results from reinsurance funds withheld $54M / $422M / $128M.
- **DOE** (non-GAAP; "measures our ability to acquire net insurance assets at a positive margin, and invest these assets at a return that is greater than the cost of policyholder liabilities"): $1,699M (2025), $1,374M (2024), $745M (2023); Annuities segment DOE $1,663M / $1,220M / $595M (FY2025 20-F segment table). FY2023 20-F segments: Direct Insurance $576M, Reinsurance $155M, PRT $43M.

### (b) Invested assets (year-end GAAP "Total investments"; no average is filed)
12/31/2025 $110,044M; 12/31/2024 $92,966M; 12/31/2023 $39,838M; 12/31/2022 $30,295M. Excludes cash and equivalents: $13,014M (2025), $12,243M (2024), $4,308M (2023).

### (c) and (e) Affiliate (Brookfield) investments, as filed
- FY2025 20-F Note 26: "As of December 31, 2025, we held investments in related parties of $ 13.4 billion (2024 – $ 8.6 billion), not including equity method investments ... Our investments in related parties include Brookfield shares received under the Exchange Offer closed on November 16, 2023, valued at $ 2.1 billion as of December 31, 2025 (2024 – $ 1.8 billion), BAM shares contributed by Brookfield on June 25, 2025, valued at $ 3.4 billion as of December 31, 2025 (2024 – $ nil ) and approximately $ 4.3 billion of private loans issued to subsidiaries of Brookfield (2024 – $ 3.1 billion)."
- FY2025 20-F Note 8(c): equity-method-eligible investments "were $ 13.3 billion and $ 9.4 billion as of December 31, 2025 and 2024, respectively. Balance as of December 31, 2025 includes partial interests in Brookfield real estate investments totaling $ 6.0 billion (2024 – $ 4.5 billion) and $ 1.0 billion of common stock of Brookfield Business Partners L.P. ("BBU") for which a quoted market price is available (2024 – $ 901 million)."
- FY2024 20-F Note 26 (DIFFERENT DEFINITION, includes equity method): "As of December 31, 2024, we held investments in related parties of $ 12.5 billion, which include $ 1.7 billion of our investment in a Brookfield real estate private fund, $ 1.2 billion of real estate partnerships associated with Brookfield office and retail real estate properties and $ 901 million of our interest in BBU, to which we apply equity method of accounting (2023 – $ 8.2 billion)." The FY2025 20-F shows 2024 as $8.6B on the ex-equity-method basis; the two filed 2024 figures are different measures.
- FY2024 20-F: "purchased related party investments of $ 7.8 billion from Brookfield and its subsidiaries ... (2023 – $ 6.6 billion)". FY2023 20-F: "purchased related party investments of $ 6.6 billion (2022 – $ 3.3 billion) of which $ 1.6 billion (2022 – nil ) relates to a contributed investment associated with a Brookfield real estate private fund."
- Investment management fees to Brookfield: $243M (2025), $162M (2024), $64M (2023), $40M (2022) (Note 26 tables, FY2025 and FY2024 20-F). Cash on deposit with a Brookfield subsidiary $318M (2025), $493M (2024), $266M (2023).
- BAM is investment manager under the Investment Management Agreements: "Brookfield, as investment manager, will receive an asset management fee based on invested assets in the relevant Brookfield Account" (FY2025 20-F Item 7.B/10). The amount of assets under those agreements is not stated.
- **A percent of the portfolio managed by or invested with Brookfield is not stated** in any of the three 20-Fs. ARITHMETIC ONLY, NOT FILED: $13.4B related-party (ex-equity-method) / $110,044M total investments = 12.2% at 12/31/2025; adding the $6.0B Brookfield real estate and $1.0B BBU equity-method items gives $20.4B / $110,044M = 18.5%. The filer does not define numerator and denominator on a common basis.
- The "$13 billion deployed into Brookfield-managed strategies ... at an average yield of 8.5%" is BN 40-F language; not found in the BWS 20-F.

### (d) Product mix (gross annuity sales, FY2025 20-F MD&A; FY2023 column from the same table)
| $M | 2025 | 2024 | 2023 |
|---|---|---|---|
| Fixed Index (retail) | 9,032 | 5,522 | 2,206 |
| Fixed Rate (retail) | 6,236 | 5,132 | 3,938 |
| Variable | 393 | 372 | 63 |
| PRT | 1,879 | 4,814 | 1,469 |
| Funding agreements | 2,289 | 0 | 0 |
| Total | 19,829 | 15,840 | 7,676 |

FIA share of gross annuity sales (arithmetic, not filed): 45.6% (2025), 34.9% (2024), 28.7% (2023). No FIA share of reserves or PAB is stated. Variable annuities: "This product accounts for less than 1% of our annuities business."

### (e) Regulatory capital
- US: "As of December 31, 2025, the capital level of each of our U.S. insurance company subsidiaries exceeded 300% of their respective Authorized Control Levels, the minimum RBC requirement before any action level is triggered or considered." (FY2025 20-F, Item 4 regulation.) Same ">300% of ACL" wording at 12/31/2024 (FY2024 20-F) and 12/31/2023 (FY2023 20-F). **No numeric RBC ratio is filed.**
- Bermuda (BSCR/ECR) and Canada (LICAT): compliance statements only: "The Company has determined that it is in compliance with all capital requirements as of December 31, 2025 and 2024." No ratio filed.
- Statutory capital and surplus (FY2025 20-F Note 27, 12/31/2025 vs 12/31/2024, $M): American Equity Investment Life Insurance Company 2,761 / 3,214; American National Insurance Company 2,418 / 2,264; Freestone Re Ltd. 2,634 / 1,345; other ANGI insurance entities 482 / 2,045; NER Ltd. 106 / 135; BAC Canada 525 / 460.

---
## 2. APOLLO GLOBAL MANAGEMENT, Retirement Services segment (Athene) (CIK 0001858681)

| FY | Form | Filed | Accession | File |
|---|---|---|---|---|
| 2025 | 10-K | 2026-02-25 | 0001858681-26-000013 | APO_10K_FY2025.txt |
| 2024 | 10-K | 2025-02-24 | 0001858681-25-000034 | APO_10K_FY2024.txt |
| 2023 | 10-K | 2024-02-27 | 0001858681-24-000031 | APO_10K_FY2023.txt |

Perimeter: Athene consolidated by Apollo from the January 1, 2022 merger; the segment metric is Athene net of the ACRA non-controlling interests. 2021 is not in AGM's segment reporting (AGM 10-K series starts FY2022); not sourced.

### (a) Definitions (FY2025 10-K glossary, verbatim)
- "Net investment earned rate | Computed as income from Athene's net invested assets, excluding the proportionate share of the ACRA net investment income associated with the non-controlling interests, divided by the average net invested assets for the relevant period"
- "Cost of funds includes liability costs related to cost of crediting on deferred annuities, including, with respect to Athene's indexed annuities, option costs, and institutional costs related to institutional products, as well as other liability costs ... Other liability costs include DAC, DSI and VOBA amortization, certain market risk benefit costs, the cost of liabilities on products other than deferred annuities and institutional products, premiums, product charges ... Cost of funds is computed as the total liability costs divided by the average net invested assets"
- "Net investment spread measures Athene's investment performance plus its strategic capital management fees less its total cost of funds"
- Alternatives: the earned rate INCLUDES an "Alternative net investment earned rate" (10.01% in 2025) on alternative investments ("including investment funds and certain VIEs"), about 4.7% of net invested assets. SRE excludes "investment gains (losses), net of offsets". So: alternative-fund returns in; realized/unrealized gains on the fixed income book out. Denominator is average net invested assets for both legs.

### Spread table (MD&A "Net Investment Spread")
| | 2025 | 2024 | 2023 | 2022 | Source |
|---|---|---|---|---|---|
| Fixed income and other NIER | 5.01% | 4.86% | 4.45% | 3.22% | FY2025 10-K (2025-2023); FY2023 10-K (2022) |
| Alternative NIER | 10.01% | 8.03% | 7.22% | 10.42% | same |
| **Net investment earned rate** | **5.25%** | **5.03%** | **4.61%** | **3.66%** | same |
| Strategic capital management fees | 0.05% | 0.04% | 0.03% | 0.03% | same |
| **Cost of funds** | **(3.69)%** | **(3.29)%** | **(2.71)%** | **(1.98)%** | same |
| **Net investment spread** | **1.61%** | **1.78%** | **1.93%** | **1.71%** | same |
| Net investment earnings $M | 14,320 | 11,744 | 9,603 | n/r | FY2025 10-K |
| Cost of funds $M | (10,083) | (7,702) | (5,650) | (3,755) | FY2025 10-K; FY2023 10-K |
| Net investment spread $M | 4,368 | 4,147 | 4,025 | 3,210 | same |
| Spread Related Earnings $M | 3,361 | 3,224 | 3,108 | n/r | FY2025 10-K |
(n/r = not read for this column.)

### (b) Invested assets
- Net invested assets (year-end, non-GAAP): $292,414M (12/31/2025); $248,643M (12/31/2024) (FY2025 10-K); $217.4B (12/31/2023) (FY2024 10-K); $196.5B (12/31/2022) (FY2023 10-K). Average net invested assets is the denominator but no dollar figure is filed; FY2025 10-K text: "$39.1 billion of growth in Athene's average net invested assets".
- GAAP: "Athene had total investments, including related parties and consolidated VIEs, of $386.1 billion and $314.6 billion as of December 31, 2025 and December 31, 2024"; $259,173M at 12/31/2023; $212,147M at 12/31/2022 (FY2024 and FY2023 10-K tables).

### (c) Affiliate (Apollo) share
- "Apollo, through its asset management business, managed or advised $392.2 billion and $331.5 billion of AUM on behalf of Athene as of December 31, 2025 and December 31, 2024, respectively." (FY2025 10-K). $278.3B at 12/31/2023 (FY2024 10-K); $236.0B at 12/31/2022 (FY2023 10-K). Note the AUM figure exceeds Athene's GAAP total investments ($386.1B); AUM is Apollo's own measure; no percent is stated.
- "Our asset management business provides a full suite of services for Athene's investment portfolio, including direct investment management, asset allocation ..." (FY2025 10-K Item 1).
- Related party investments on Athene's balance sheet: $34,979M = **9.1%** of total investments incl. related parties and VIEs (12/31/2025); $28,884M = **9.2%** (2024) (FY2025 10-K); $25,842M = **9.9%** (2023) (FY2024 10-K); $23,960M = **11.2%** (2022) (FY2023 10-K). Percentages as filed. Consolidated VIE investments (largely investment funds) are a further $29,992M / 7.7% (2025), $23,424M / 7.4% (2024).
- Origination: "These direct origination strategies include investments sourced by (1) affiliated platforms that originate loans to third parties ... and (2) our asset management team's extensive network of direct relationships" (FY2025 10-K). No percent of the portfolio sourced by affiliated platforms is stated in the 10-K.

### (d) Product mix
- "FIAs are the largest percentage of Athene's net reserve liabilities." (FY2025 10-K Item 1.) No percentage given there.
- Policyholder account balances by product (FY2025 10-K notes, $M, year-end): Traditional deferred annuities 109,201 / 86,661 / 64,763; Indexed annuities 105,317 / 97,861 / 93,147; Funding agreements 85,555 / 54,768 / 32,350; Other investment-type 8,821 / 8,030 / 7,629 (2025 / 2024 / 2023). Indexed annuity share of that $308,894M total (arithmetic, not filed): 34.1% (2025), 39.6% (2024), 47.1% (2023). Weighted average crediting rate 2025: traditional deferred 4.7%, indexed 2.7%, funding agreements 4.6%.
- "As of December 31, 2025, approximately 36% of Athene's net reserve liabilities were generally non-surrenderable ... while 53% were subject to penalty upon surrender."

---
## 3. KKR & CO., Insurance segment (Global Atlantic) (CIK 0001404912)

| FY | Form | Filed | Accession | File |
|---|---|---|---|---|
| 2025 | 10-K | 2026-02-27 | 0001404912-26-000007 | KKR_10K_FY2025.txt |
| 2024 | 10-K | 2025-02-28 | 0001404912-25-000015 | KKR_10K_FY2024.txt |
| 2023 | 10-K | 2024-02-29 | 0001404912-24-000005 | KKR_10K_FY2023.txt |

Perimeter: "KKR acquired a majority controlling interest in Global Atlantic on February 1, 2021 (approximately 60%), and acquired the remainder of Global Atlantic on January 2, 2024, increasing our ownership to 100%." (FY2025 10-K). FY2021 is from February 1, 2021; FY2021-FY2023 segment earnings shown before and after the noncontrolling interest line.

### (a) Spread metric: NOT FILED as a rate
KKR's 10-K reports the insurance segment in dollars only: "Insurance Operating Earnings ... (i) Net Investment Income, (ii) Net Cost of Insurance, and (iii) General, Administrative, and Other Expenses." No net investment earned rate, no cost of funds rate, no spread percentage. Searched FY2025, FY2024, FY2023 10-K texts for "net investment spread", "cost of funds", "average net invested", "yield" and "%" near Global Atlantic: only narrative ("higher average portfolio yields", "higher average funding costs due to higher crediting rates"). The 8-K earnings release / supplement was not opened (brief permits it only when the 10-K lacks the metric: this is such a case, but see "could not source" in the summary).

Segment dollars ($ thousands, as filed):
| | 2025 | 2024 | 2023 | 2022 | 2021 (from Feb 1) |
|---|---|---|---|---|---|
| Net Investment Income | 7,224,118 | 6,328,822 | 5,377,817 | 4,112,244 | 3,329,570 |
| Net Cost of Insurance | (5,229,343) | (4,448,886) | (3,283,009) | (2,295,133) | (1,564,264) |
| General, Administrative and Other | (885,380) | (865,390) | (805,109) | (638,274) | (500,410) |
| Insurance Operating Earnings | 1,109,395 | 1,014,546 | 816,637 (after NCI (473,062)) | 724,762 (after NCI (454,075)) | n/r |
Sources: 2025-2024 FY2025 10-K; 2024-2023 FY2024 10-K; 2023-2022 and 2022-2021 FY2023 10-K. 2023 and 2022 figures reflect LDTI retrospective adoption (FY2023 10-K).

Definition note (FY2025 10-K, verbatim): "Insurance Operating Earnings excludes the impact of: (i) investment gains (losses) which include realized gains (losses) related to asset/liability matching investment strategies and unrealized investment gains (losses) and (ii) non-operating changes in policy liabilities and derivatives ... Insurance Operating Earnings includes (i) realized gains and losses not related to asset/liability matching investment strategies and (ii) the investment management costs that are earned by our Asset Management segment as the investment adviser of the Global Atlantic insurance companies." Whether alternative-fund returns are in segment NII is not separately stated in what was read.

### (b) Invested assets (GAAP, insurance section of consolidated statement of financial condition, $ thousands)
Investments: 192,009,748 (12/31/2025); 170,144,744 (12/31/2024) (FY2025 10-K); 141,370,323 (12/31/2023) (FY2024 10-K). No average filed.
"Global Atlantic FPAUM as of December 31, 2025 is $213 billion" (FY2025 10-K Item 1; the AUM history is a chart whose values are not in the text).

### (c) Affiliate (KKR) share: NOT FILED as an amount or percent
- Filed language only: "The investment management agreements between our investment manager and our insurance subsidiaries were approved by the applicable U.S. and Bermuda insurance regulators, and any changes to such agreements, including with respect to fees, must receive applicable regulatory approval." and "Global Atlantic primarily generates income by earning a spread between the investment income generated from originated assets and the required cost of benefits payable to policyholders." (FY2025 10-K).
- "As of December 31, 2025, $58 billion of Global Atlantic AUM is provided by these Global Atlantic sponsored vehicles" (third-party capital vehicles such as Ivy; this is sidecar capital, not affiliate-managed share).
- The segment definition names KKR's Asset Management segment "as the investment adviser of the Global Atlantic insurance companies" (FY2025 10-K).
- No percent of Global Atlantic's portfolio in KKR-managed funds or KKR-originated assets found.

### (d) Product mix
"As of December 31, 2025, 41% of Global Atlantic's reserves were in its individual markets and 59% were in its institutional markets." (FY2025 10-K Item 1.) No FIA share of reserves stated in what was read.

---
## 4. COREBRIDGE FINANCIAL (CRBG, CIK 0001889539), Individual Retirement segment

| FY | Form | Filed | Accession | File |
|---|---|---|---|---|
| 2025 | 10-K | 2026-02-11 | 0001889539-26-000022 | CRBG_10K_FY2025.txt |
| 2024 | 10-K | 2025-02-13 | 0001889539-25-000014 | CRBG_10K_FY2024.txt |
| 2023 | 10-K | 2024-02-15 | 0001889539-24-000006 | CRBG_10K_FY2023.txt |

Perimeter: Individual Retirement segment (fixed, fixed index, and from Q4 2024 registered index-linked annuities). **Recast in the FY2025 10-K**: "effective in the third quarter of 2025, our individual variable annuity business previously reported in the Individual Retirement segment, is now included within Corporate and Other ... Prior periods presented herein have been recast". So the FY2025 10-K series (ex-VA) and the FY2023/FY2024 10-K series (incl. VA) are different perimeters.

### (a) Definitions (FY2025 10-K, verbatim)
- "Base net investment spread means base yield less cost of funds, excluding the amortization of deferred sales inducement assets."
- "Base yield means the returns from base portfolio income including accretion and impacts from holding cash and short-term investments."
- "Base portfolio income includes interest, dividends and foreclosed real estate income, net of investment expenses and non-qualifying (economic) hedges."
- "Variable investment income includes call and tender income ... changes in market value of investments accounted for under the fair value option ... income from alternative investments" and is EXCLUDED from base yield. So: **alternatives and gains are OUT** of the Corebridge spread (contrast Athene: alternatives in; BN/BWS table: real-asset gains in).
- Cost of funds is not separately defined in words beyond the spread definition; the denominator (average invested assets) is not disclosed in dollars.

### Individual Retirement base net investment spread
| | 2025 | 2024 | 2023 | 2022 | 2021 |
|---|---|---|---|---|---|
| FY2025 10-K (VA recast out): Base yield | 5.17% | 5.22% | 4.97% | | |
| Cost of funds | (3.23)% | (2.95)% | (2.54)% | | |
| **Base net investment spread** | **1.94%** | **2.27%** | **2.43%** | | |
| FY2024 10-K (incl. VA): Base yield | | 5.13% | 4.89% | 3.98% | |
| Cost of funds | | (2.88)% | (2.47)% | (2.18)% | |
| Base net investment spread | | 2.25% | 2.42% | 1.80% | |
| FY2023 10-K (incl. VA): Base yield | | | 4.89% | 3.98% | 3.89% |
| Cost of funds | | | 2.47 | 2.18 | 2.15 |
| Base net investment spread | | | 2.42% | 1.80% | 1.74% |

FY2023 10-K by product (Individual Retirement, 2023 / 2022 / 2021): **Fixed index annuities** base yield 4.82% / 3.90% / 3.78%, cost of funds 2.01 / 1.54 / 1.39, **base net investment spread 2.81 / 2.36 / 2.39**; Fixed annuities 5.05% / 4.03% / 3.94%, 2.95 / 2.69 / 2.64, spread 2.10 / 1.34 / 1.30; Variable annuities 3.82% / 3.85% / 3.96%, 1.48 / 1.43 / 1.42, spread 2.34 / 2.42 / 2.54. Product-level spreads are not in the FY2024 or FY2025 10-K (searched "Fixed index annuities base net investment spread": 0 hits in both).

Dollars (FY2025 10-K, $M, 2025 / 2024 / 2023): base portfolio income 5,883 / 5,308 / 4,554; interest credited (3,347) / (2,720) / (2,122); base spread income 2,536 / 2,588 / 2,432; variable investment income 129 / 105 / 51.

### (b) Invested assets
- No Individual Retirement invested-asset figure or average invested assets found. Individual Retirement AUMA (assets under management and administration): $120,419M / $105,743M / $94,860M at 12/31/2025 / 2024 / 2023 (FY2025 10-K).
- Consolidated GAAP total investments: $265,258M (12/31/2025), $243,758M (12/31/2024) (FY2025 10-K balance sheet); $232,628M (12/31/2023) (FY2024 10-K).

### (c) Affiliate / external manager share
- "Historically, our investments have largely been managed by affiliated investment managers." (FY2025 10-K; this refers to AIG.)
- Blackstone: "As of December 31, 2025, Blackstone managed approximately $71.2 billion in book value of assets in our investment portfolio." ($68.8B at 12/31/2024, FY2024 10-K; $55.4B at 12/31/2023, FY2023 10-K.) "We expect Blackstone to invest primarily in Blackstone-originated investments". Blackstone is a shareholder: "Argon Holdco LLC, a wholly-owned subsidiary of Blackstone, owned approximately ... 12.5 % of the outstanding Corebridge Parent common stock" at 12/31/2025 (Nippon 24.6%, AIG 10.1%).
- BlackRock (not a shareholder per the same sentence): $91.9B (2025), $86.8B (2024), $85.3B (2023).
- No percent stated. ARITHMETIC ONLY: Blackstone $71.2B / $265,258M total investments = 26.8% (2025).

### (d) Product mix (Individual Retirement, FY2025 10-K)
Premiums and deposits $M (2025 / 2024 / 2023): Fixed annuities 8,881 / 11,380 / 7,880; Fixed index annuities 9,869 / 9,013 / 8,505; RILA 1,879 / 90 / 0; total 20,629 / 20,483 / 16,385.
Account value $M (12/31/2025 / 2024 / 2023): Fixed annuities 57,738 / 54,835 / 50,471; Fixed index annuities 52,904 / 46,245 / 39,594; RILA 2,144 / 89 / 0. FIA share of this account value (arithmetic, not filed): 46.9% / 45.7% / 44.0%.

---
## 5. F&G ANNUITIES & LIFE (FG, CIK 0001934850)

| Doc | Filed | Accession | File |
|---|---|---|---|
| FY2025 10-K | 2026-02-26 | 0001934850-26-000026 | FG_10K_FY2025.txt |
| FY2024 10-K | 2025-02-28 | 0001934850-25-000015 | FG_10K_FY2024.txt (downloaded, not needed beyond FY2025 comparatives) |
| FY2023 10-K | 2024-02-29 | 0001934850-24-000018 | FG_10K_FY2023.txt (downloaded, same) |
| 8-K EX-99.2 Q4 2025 Financial Supplement | 2026-02-19 | 0001934850-26-000021 | FG_8K_20260219_supplement.txt |
| 8-K EX-99.2 Q4 2024 Financial Supplement | 2025-02-20 | 0001934850-25-000006 | FG_8K_20250220_supplement.txt |
| 8-K EX-99.2 Q4 2023 Financial Supplement | 2024-02-21 | 0001934850-24-000014 | FG_8K_20240221_supplement.txt |

Perimeter: whole company, AUM net of flow reinsurance ("AUM is ... reported net of reinsurance assets ceded"). FNF owns approximately 70%.

### (a) Metric
The **10-K** files only yield on AAUM: "Yield on AAUM is calculated by dividing annualized GAAP net investment income by AAUM." FY2025 10-K: **5.12% (2025), 5.27% (2024), 4.80% (2023)**, "at amortized cost"; AAUM $55,384M / $51,574M / $46,044M. No cost of funds rate and no spread in the 10-K (searched "cost of funds", "net investment spread": cost of funds appears only inside the ROA definition). Therefore the 8-K EX-99.2 supplements were used for cost of funds, per the brief.

Definition (10-K and supplement): "Return on assets is comprised of net investment income, less cost of funds, flow reinsurance fee income, owned distribution margin and less expenses ... Cost of funds includes liability costs related to cost of crediting as well as other liability costs." Alternatives are IN: the adjusted investment income includes "Interest and investment income - alternatives (including short term mark- to-market)". Recognized gains are removed.

Supplement "Adjusted Return on Assets" (annualized YTD, % of AAUM):
| | FY2025 | FY2024 recast | FY2024 as first filed | FY2023 (Q4'24 supp.) | FY2023 (Q4'23 supp.) | FY2022 (Q4'23 supp.) |
|---|---|---|---|---|---|---|
| Adjusted interest and investment income / "Portfolio earned yield" | **5.08%** | 5.12% | 5.12% | 4.75% | 4.75% | 4.13% |
| Cost of funds | **(3.20)%** | (2.96)% | (3.03)% | (2.92)% | (2.80)% | (2.37)% |
| **Product margin** (the spread) | **1.88%** | 2.16% | 2.09% | 1.83% | 1.95% | 1.76% |
| AAUM YTD $M | 55,384 | 51,574 | 51,574 | 46,044 | 46,265 | 40,069 |
Recast note (Q4 2025 supplement): "Periods prior to March 31, 2025 have been recast to reflect updated definitions for cost of funds and flow reinsurance fee income". FY2023 differs between the Q4 2023 and Q4 2024 supplements as filed.
Yield on AAUM excluding alternatives and variable income (Q4 2025 supplement): 4.61% (2025), 4.61% (2024). Alternatives income $666M (2025), $589M (2024).

### (b) Invested assets
AUM $57,574M (12/31/2025), $53,817M (12/31/2024); AUM before flow reinsurance $73,090M / $65,274M. GAAP total investments at fair value $69,000M (12/31/2025), $59,503M (12/31/2024) (Q4 2025 supplement, invested assets summary).

### (c) Affiliate / manager share
- Blackstone is the manager but not an affiliate: "BIS is appointed as investment manager of substantially all assets in the general and separate accounts of those entities (the "F&G Accounts")" (FY2025 10-K Item 1 and Note Q). Related parties per Note Q are FNF and its directors/officers; an entity 50% owned by an affiliate of the Executive Chairman receives a participation fee from BIS. No percent of assets in FNF-affiliated investments stated.

### (d) Product mix
"For the year ended December 31, 2025, FIAs generated approximately 46% of our gross sales. The remaining 54% of sales were primarily generated from fixed rate annuities (26%), PRT sales (15%), funding agreements (12%) and IUL (1%)." (FY2025 10-K Item 1.)
GAAP net reserves (Q4 2025 supplement, $M, 12/31/2025 / 2024): Indexed annuities 31,251 / 30,141; fixed rate annuities 6,404 / 6,434; SPIA and other 1,521 / 1,564; IUL and other life 3,304 / 2,813; funding agreements 6,234 / 5,315; PRT 8,125 / 6,066; total 56,839 / 52,333. Indexed annuity share (arithmetic): 55.0% / 57.6%.

---
## 6. JACKSON FINANCIAL (JXN), EQUITABLE (EQH), LINCOLN (LNC)

- **JXN** (FY2025 10-K, filed 2026-02-24, 0001822993-26-000022, JXN_10K_FY2025.txt): no spread rate filed. The 10-K reports "spread income" in dollars by segment (e.g. "$152 million increase in spread income primarily due to $210 million higher net investment income, partially offset by $58 million higher interest credited") and uses "net investment spread" only in risk factors. EDGAR full-text screen (tools/sources.py fts_count, cik 0001822993): "net investment spread" 5 hits in 10-Ks, 2 in 8-Ks (EX-99.1 of 2023-05-10 and 2021-08-06, not annual series); "net investment earned rate" 0. Not a comparable filed metric. Not sourced.
- **EQH** (cik 0001333986): fts_count "net investment spread" 0 (10-K), 0 (8-K); "net investment earned rate" 0; "cost of funds" 0 in 10-Ks, 2 in 8-K exhibits (EX-99.2 filed 2026-03-26 acc 0000950142-26-000871, and a 2023-05-10 slide presentation). No 10-K spread metric; not opened further; not sourced.
- **LNC** (cik 0000059558): "net investment spread" 0; "net investment earned rate" 0; "cost of funds" 2 hits, both 2010 credit-agreement exhibits (EX-10.60). No comparable metric; not sourced.
(Hit counts are screens only; the 10-K texts for EQH and LNC were not downloaded.)

---
## SUMMARY TABLE (as filed; definitions NOT harmonised, see each section)

Key to the spread definitions: **BN/BWS** = NII yield + real-asset gains less life/annuity and P&C cost of funds, on average invested insurance assets (BN 40-F, not BWS). **APO** = net investment earned rate (fixed income + alternatives, no gains) + strategic fees less cost of funds (crediting, option costs, DAC/DSI/VOBA amortisation, other liability costs), on average net invested assets. **CRBG** = base yield (excludes alternatives, calls, fair-value changes) less cost of funds, Individual Retirement only. **FG** = adjusted investment income incl. alternatives mark-to-market less cost of funds (crediting plus other liability costs), on AAUM net of flow reinsurance.

| Firm | FY | Earned rate | Cost of funds | Net spread | Invested assets | Affiliate-managed share | Source accession |
|---|---|---|---|---|---|---|---|
| BWS (20-F) | 2025 | not filed | not filed (annuity PAB wtd crediting rate 4%) | not filed | $110,044M total investments YE | not stated; related-party investments $13.4B ex-equity-method + $6.0B Brookfield RE + $1.0B BBU equity method (arith. 12.2% / 18.5%) | 0001837429-26-000008 |
| BWS (20-F) | 2024 | not filed | not filed (4%) | not filed | $92,966M YE (AEL from May 2024) | not stated; $12.5B related party incl. equity method (FY24 20-F) or $8.6B ex (FY25 20-F) | 0001837429-25-000009 |
| BWS (20-F) | 2023 | not filed | not filed (2%) | not filed | $39,838M YE (pre-AEL) | not stated; $8.2B related party (FY24 20-F) | 0001837429-24-000006 |
| BN on BWS (40-F, per brief, not re-verified here) | 2025 | 5.01% + 0.69% real-asset gains | (3.45)% effective | 2.25% gross | $112,700M average | $13B deployed into Brookfield strategies in 2025 | BN FY2025 40-F |
| APO / Athene | 2025 | 5.25% (FI 5.01%, alts 10.01%) | (3.69)% | 1.61% | $292,414M net invested assets YE | Apollo manages/advises $392.2B AUM for Athene (> $386.1B GAAP investments); related-party investments 9.1% | 0001858681-26-000013 |
| APO / Athene | 2024 | 5.03% | (3.29)% | 1.78% | $248,643M NIA YE | $331.5B AUM; related party 9.2% | 0001858681-26-000013 |
| APO / Athene | 2023 | 4.61% | (2.71)% | 1.93% | $217.4B NIA YE | $278.3B AUM; related party 9.9% | 0001858681-26-000013; 0001858681-25-000034 |
| APO / Athene | 2022 | 3.66% | (1.98)% | 1.71% | $196.5B NIA YE | $236.0B AUM; related party 11.2% | 0001858681-24-000031 |
| KKR / Global Atlantic | 2025 | not filed (NII $7,224M) | not filed (net cost of insurance $5,229M) | not filed (IOE $1,109M) | $192,010M insurance investments YE | not stated (KKR is "investment adviser") | 0001404912-26-000007 |
| KKR / Global Atlantic | 2024 | not filed (NII $6,329M) | not filed ($4,449M) | not filed ($1,015M) | $170,145M YE | not stated | 0001404912-26-000007 |
| KKR / Global Atlantic | 2023 | not filed (NII $5,378M) | not filed ($3,283M) | not filed | $141,370M YE | not stated | 0001404912-25-000015 |
| CRBG Indiv. Retirement | 2025 | 5.17% base yield | (3.23)% | 1.94% | no segment figure; $265,258M consolidated YE | unaffiliated managers: Blackstone (12.5% holder) $71.2B, BlackRock $91.9B | 0001889539-26-000022 |
| CRBG Indiv. Retirement | 2024 | 5.22% recast (5.13% as filed) | (2.95)% ((2.88)%) | 2.27% (2.25%) | $243,758M consolidated YE | Blackstone $68.8B; BlackRock $86.8B | 0001889539-26-000022; 0001889539-25-000014 |
| CRBG Indiv. Retirement | 2023 | 4.97% recast (4.89%) | (2.54)% ((2.47)) | 2.43% (2.42%); FIA-only 2.81% | $232,628M consolidated YE | Blackstone $55.4B; BlackRock $85.3B | 0001889539-26-000022; 0001889539-24-000006 |
| CRBG Indiv. Retirement | 2022 | 3.98% | 2.18 | 1.80%; FIA-only 2.36% | not read | n/a | 0001889539-24-000006 |
| CRBG Indiv. Retirement | 2021 | 3.89% | 2.15 | 1.74%; FIA-only 2.39% | not read | n/a | 0001889539-24-000006 |
| FG | 2025 | 5.08% (10-K yield on AAUM 5.12%) | (3.20)% | 1.88% product margin | $55,384M AAUM; $69,000M GAAP investments YE | Blackstone (not an affiliate) manages "substantially all"; no affiliate share stated | 8-K 0001934850-26-000021; 10-K 0001934850-26-000026 |
| FG | 2024 | 5.12% (10-K 5.27%) | (2.96)% recast; (3.03)% as filed | 2.16% recast; 2.09% as filed | $51,574M AAUM | same | 0001934850-26-000021; 0001934850-25-000006 |
| FG | 2023 | 4.75% (10-K 4.80%) | (2.92)% (Q4'24 supp.); (2.80)% (Q4'23 supp.) | 1.83% / 1.95% | $46,044M / $46,265M AAUM | same | 0001934850-25-000006; 0001934850-24-000014 |
| FG | 2022 | 4.13% | (2.37)% | 1.76% | $40,069M AAUM | same | 0001934850-24-000014 |
| JXN, EQH, LNC | 2023-25 | not filed | not filed | not filed | not collected | not collected | see section 6 |

Status: COMPLETE for the scope above (2026-09-13). Research only; no conclusions drawn.

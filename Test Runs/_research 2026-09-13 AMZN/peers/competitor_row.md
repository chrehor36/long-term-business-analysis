# COMPETITOR ROW, AMZN run, 2026-09-13 (COMPLETE at the 14:40 resume: Table A by the killed session; Tables B and C, the naming sweep and the not-obtained lists by two transcription passes, written to their own files and summarised here)

Transcription and arithmetic only. No conclusion about Amazon's position is drawn in this file.
Primary SEC filings only (EDGAR primary documents). All figures USD millions unless stated.
Ratios and growth rates are arithmetic on the filed figures, computed here, unless marked "filed".
Stripped text of each filing read is saved in this folder (file name in the table below), or,
where it was already on disk from an earlier run, the path of that copy is given.

## DOCUMENTS READ

| Company | Form | Period | Filed | Accession | Text on disk |
|---|---|---|---|---|---|
| Microsoft (CIK 789019) | 10-K | FY ended 2026-06-30 | 2026-07-29 | 0001193125-26-323660 | `_research 2026-09-06 MSFT/MSFT_FY2026_10K.txt` (reused) |
| Microsoft | 10-K | FY ended 2025-06-30 | (earlier run) | 0000950170-25-100235 | `_research 2026-09-06 MSFT/MSFT_FY2025_10K.txt` (reused, recast check only) |
| Microsoft | 10-Q | six months ended 2025-12-31 | 2026-01-28 | 0001193125-26-027207 | `MSFT_10Q_FY2026Q2.txt` |
| Alphabet (CIK 1652044) | 10-K | FY2025 (Dec 31) | 2026-02-05 | 0001652044-26-000018 | `_research 2026-09-06 MSFT/GOOGL_FY2025_10K.txt` (reused) |
| Alphabet | 10-Q | six months ended 2026-06-30 | 2026-07-23 | 0001652044-26-000071 | `GOOGL_10Q_2026Q2.txt` |
| Oracle (CIK 1341439) | 10-K | FY ended 2026-05-31 | 2026-06-22 | 0001193125-26-277521 | `_research 2026-09-06 MSFT/ORCL_FY2026_10K.txt` (reused) |
| Oracle | 10-Q | quarter ended 2026-08-31 (Q1 FY2027) | 2026-09-11 | 0001193125-26-389274 | `ORCL_10Q_FY2027Q1.txt` |
| Amazon (CIK 1018724) | 10-K | FY2025 | (earlier run) | 0001018724-26-000004 | `_research 2026-09-06 MSFT/AMZN_FY2025_10K.txt` (reused, consolidated capex and net sales only) |

(Table B and C documents are appended below as they are read.)

---
## TABLE A, CLOUD

### A.1 Latest full fiscal year

| Filer / unit | FY end | Segment revenue | Segment operating income | Margin | Revenue growth y/y | Company capex / revenue | Company capex / depreciation |
|---|---|---|---|---|---|---|---|
| **Amazon, AWS** (reference) | 2025-12-31 | 128,725 | 45,606 | 35.4% | +19.7% (vs 107,556) | 131,819 / 716,924 = 18.4% | 131,819 / 41,860 = 3.15x (P&E-only depreciation, see note 1) |
| **Microsoft, Intelligent Cloud** | 2026-06-30 | 137,791 | 56,972 | 41.3% | +29.7% (vs 106,265; filed "30%") | 115,948 / 331,839 = 34.9% | 115,948 / 34,300 = 3.38x |
| **Alphabet, Google Cloud** | 2025-12-31 | 58,705 | 13,910 | 23.7% | +35.8% (vs 43,229) | 91,447 / 402,836 = 22.7% | 91,447 / 21,136 = 4.33x |
| **Oracle, cloud revenue (no cloud segment)** | 2026-05-31 | 33,989 total cloud (infrastructure 18,101; applications 15,888) | **not filed** (see note 4) | n/a | cloud +38.7% (vs 24,506); infrastructure +76.9% (vs 10,234); applications +11.3% (vs 14,272) | 55,663 / 67,357 = 82.6% | 55,663 / 7,623 = 7.30x |

Prior-year margins for the same units: AWS FY2024 37.0% (39,834 / 107,556); Microsoft Intelligent
Cloud FY2025 42.0% (44,589 / 106,265); Google Cloud FY2024 14.1% (6,112 / 43,229).

### A.2 Latest interim

| Filer / unit | Window | Revenue | Operating income | Margin | Same window prior year (rev / OI / margin) | Revenue growth y/y | Company capex / revenue | Company capex / depreciation |
|---|---|---|---|---|---|---|---|---|
| **Amazon, AWS** (reference) | H1 2026 (Jan-Jun) | 79,819 | 30,782 | 38.6% | 60,140 / 21,707 / 36.1% | +32.7% | not computed here (subject) | not computed here (subject) |
| **Microsoft, Intelligent Cloud** | H1 calendar 2026 (Jan-Jun), **derived** (note 2) | 73,987 | 29,708 | 40.2% | 56,629 / 23,235 / 41.0% | +30.7% | 86,072 / 172,893 = 49.8% (derived, note 2) | not computable on the same basis (note 2) |
| **Alphabet, Google Cloud** | H1 2026 (Jan-Jun) | 44,796 | 15,412 | 34.4% | 25,884 / 5,003 / 19.3% | +73.1% (note 3) | 80,598 / 229,692 = 35.1% (H1 2025: 39,643 / 186,662 = 21.2%) | 80,598 / 13,586 = 5.93x (H1 2025: 39,643 / 9,485 = 4.18x) |
| **Oracle, cloud revenue** | Q1 FY2027 (Jun-Aug 2026), one quarter | 11,607 total cloud (infrastructure 7,388; applications 4,219) | not filed | n/a | 7,186 (infrastructure 3,347; applications 3,839) | cloud +61.5%; infrastructure +120.7%; applications +9.9% | 28,499 / 19,345 = 147.3% (Q1 FY2026: 8,502 / 14,926 = 57.0%) | 28,499 / 3,156 = 9.03x (Q1 FY2026: 8,502 / 1,351 = 6.29x) |

**Notes to Table A**

1. Amazon depreciation denominator is property-and-equipment depreciation only (41,860), as
   established in `_research 2026-09-06 MSFT/competitor_row.md`; Amazon's cash-flow D&A line
   (65,756) is broader (includes capitalized content and operating lease assets). Capex 131,819
   and net sales 716,924 confirmed against the FY2025 10-K cash-flow statement and income
   statement text (lines 902 and 935 of the saved text). Microsoft depreciation is the P&E note
   figure, filed rounded: "During fiscal years 2026, 2025, and 2024, depreciation expense was
   $34.3 billion, $22.0 billion, and $15.2 billion, respectively." Alphabet depreciation is the
   cash-flow line "Depreciation of property and equipment". Oracle depreciation is the cash-flow
   line "Depreciation". Capex in every row is the cash line (Microsoft "Additions to property and
   equipment"; Alphabet "Purchases of property and equipment"; Oracle "Capital expenditures";
   Amazon "Purchases of property and equipment"). Finance-lease additions are excluded for all
   (Microsoft's finance-lease ROU additions of 24,608 in FY2026 are recorded in the earlier MSFT
   competitor row and would raise its ratios).
2. Microsoft files no calendar-half figures. H1 calendar 2026 = FY2026 10-K full year less the
   six months ended 2025-12-31 in the Q2 FY2026 10-Q: Intelligent Cloud revenue 137,791 - 63,804;
   operating income 56,972 - 27,264. H1 calendar 2025 = FY2025 (as shown in the FY2026 10-K)
   106,265 - 49,636 and 44,589 - 21,354 (prior-year column of the same 10-Q). Capex 115,948 -
   29,876; total revenue 331,839 - 158,946. The Microsoft 10-Q cash-flow statement carries a
   combined "depreciation, amortization, and other" line, not P&E depreciation, so no H1
   capex/depreciation is computed. Segment basis check: the FY2026 10-K and FY2025 10-K both show
   Intelligent Cloud FY2025 revenue 106,265 and FY2024 87,464; no segment recast found. The subtraction
   assumes the 10-Q six-month columns are on the same basis; no recast note was found in the 10-K.
3. Alphabet Q2 2026 10-Q, MD&A, verbatim: "Google Cloud revenues increased $11.1 billion and $18.9
   billion from the three and six months ended June 30, 2025 to the three and six months ended June
   30, 2026 primarily driven by growth in Google Cloud Platform largely from infrastructure and
   platform services. In addition, in the second quarter of 2026, we began recognizing revenue from
   the sale of TPU systems." The H1 2026 Google Cloud revenue therefore includes a hardware-sale
   component not present in the prior-year window; its amount is not separately stated in the text
   searched.
4. Oracle FY2026 10-K: "We have three businesses: cloud and software (formerly referred to as cloud
   and license); hardware; and services. Each business is comprised of a single operating segment."
   There is no cloud segment operating income. The nearest filed figure is the cloud-and-software
   business "Total Margin", which bundles cloud with software licence and support and excludes
   stock-based compensation, R&D, G&A and amortization, so it is **not** comparable to AWS,
   Intelligent Cloud or Google Cloud operating income. Recorded for completeness only:
   FY2026 revenue 58,530, total margin 34,468 (filed "59%"); FY2025 49,230, 30,930 (filed "63%").
   Q1 FY2027 revenue 17,157, margin 9,358 (54.5%); Q1 FY2026 12,907, 7,691 (59.6%).
   Oracle FY2026 10-K, verbatim: "Our cloud infrastructure revenues represented 53%, 42% and 35% of our total cloud revenues during fiscal 2026, 2025 and 2024, respectively." (Item 1)
   and "cloud applications and cloud infrastructure contributed 16% and 84%,
   respectively, to the constant currency growth in cloud revenues in fiscal 2026."
5. Microsoft Intelligent Cloud is wider than infrastructure cloud: the FY2026 10-K says it
   comprises "Server products and cloud services, including Azure and other cloud services ..."
   and Enterprise and partner services. Server products (on-premises licences) are inside the
   segment revenue. The 10-K gives Azure only as a growth rate, not in dollars: "Azure and other
   cloud services revenue grew 41%". Microsoft Cloud revenue (a wider, cross-segment measure)
   was "$214.4 billion, $168.9 billion, and $137.7 billion in fiscal years 2026, 2025, and 2024".

### A.3 Filed backlog / remaining performance obligations

| Filer | As of | Figure | Filed context, verbatim | Document |
|---|---|---|---|---|
| Microsoft | 2026-06-30 | $684bn total RPO; $678bn commercial RPO | "Revenue allocated to remaining performance obligations related to the commercial portion of revenue was $678 billion as of June 30, 2026, with a weighted average duration of approximately 2.3 years. We expect to recognize approximately 30% of both our total company remaining performance obligation revenue and commercial remaining performance obligation revenue over the next 12 months and the remainder thereafter." MD&A highlight: "Commercial remaining performance obligation increased 84% to $678 billion." | 10-K FY2026, 0001193125-26-323660, Note 12 Unearned Revenue (last paragraph) and MD&A overview |
| Alphabet | 2025-12-31 | $242.8bn | "As of December 31, 2025, we had $242.8 billion of remaining performance obligations ("revenue backlog"), primarily related to Google Cloud. ... We expect to recognize just over 50% of the revenue backlog as revenues over the next 24 months with the remainder to be recognized thereafter." | 10-K FY2025, 0001652044-26-000018, Note 2 Revenues, "Revenue Backlog" |
| Alphabet | 2026-06-30 | $519.5bn, of which $513.9bn Google Cloud | "As of June 30, 2026, we had $ 519.5 billion of remaining performance obligations ("revenue backlog"), of which $ 513.9 billion related to Google Cloud. ... We expect to recognize just over 50 % of the revenue backlog as revenues over the next 24 months with the remainder to be recognized thereafter." | 10-Q Q2 2026, 0001652044-26-000071, revenue note |
| Oracle | 2026-05-31 (and 2025-05-31) | $638bn ($138bn) | "Remaining performance obligations were $638 billion and $138 billion as of May 31, 2026 and 2025, respectively. The increase in remaining performance obligations as of May 31, 2026 in comparison to May 31, 2025 was primarily attributable to certain significant cloud contracts that were entered into during the period." | 10-K FY2026, 0001193125-26-277521, MD&A |
| Oracle | 2026-08-31 | $664bn | "Remaining performance obligations were $ 664 billion as of August 31, 2026 , of which we expect to recognize approximately 13 % as revenues over the next twelve months , 37 % over the subsequent month 13 to month 36 , 34 % over the subsequent month 37 to month 60 and the remainder thereafter." | 10-Q Q1 FY2027, 0001193125-26-389274, revenue note |
| Amazon (reference) | 2025-12-31 | ~$244bn (contracts >1 yr, "primarily related to AWS", weighted average remaining life 4.1 years) | as recorded in `_research 2026-09-06 MSFT/competitor_row.md` | 10-K FY2025, 0001018724-26-000004 |

Scope differences, stated: Microsoft's figure is company-wide (commercial portion includes
Microsoft 365, Dynamics, LinkedIn commercial as well as Azure); Alphabet's is company-wide with a
Google Cloud breakout only in the 10-Q; Oracle's is company-wide (cloud, support, hardware,
services). None is a pure infrastructure-cloud backlog.

### A.4 Filed statements about cloud pricing

Method: every sentence in the MSFT FY2026 10-K, MSFT Q2 FY2026 10-Q, GOOGL FY2025 10-K, GOOGL Q2
2026 10-Q, ORCL FY2026 10-K and ORCL Q1 FY2027 10-Q containing a price word (pric*, discount*)
and a cloud word (cloud, Azure, OCI, infrastructure, compute, GPU, TPU, capacity) was listed
(`pricegrep.py`, output read in full). **No filed statement of an executed cloud price increase or
price decrease was found in any of the six documents.** The filed pricing language is
risk-factor and strategy language, quoted verbatim:

- **Microsoft 10-K FY2026 (0001193125-26-323660), Item 1A Risk Factors, cloud and AI strategy risk:**
  "The financial success of these investments depends on a number of uncertain factors, including
  customer demand for cloud-based and AI products and services and continued customer use of Azure
  to build, train, deploy, and run AI workloads, our ability to price and monetize those services
  at levels sufficient to recover our costs, competitive dynamics affecting pricing, and the pace
  of adoption of AI."
- Same document, same section: "If these costs increase, remain elevated, or fail to decline, or if
  pricing for AI products and services declines as a result of competition, commoditization, or
  other market forces, our margins, financial condition, and results of operations could be
  adversely affected."
- Same document, same section: "As we manage infrastructure capacity constraints and evolving
  customer demand, we may modify capacity allocations, deployment priorities, pricing, or other
  commercial arrangements."
- **Microsoft 10-Q Q2 FY2026 (0001193125-26-027207), Part II Item 1A:** "We and our competitors continue
  to devote significant resources to developing and deploying cloud-based strategies and services
  for consumers and business customers, and pricing and delivery models are evolving."
- **Oracle 10-K FY2026 (0001193125-26-277521), Item 1A Risk Factors, cloud strategy risk:**
  "Additionally, the increasing prevalence of various cloud offering models by us and our
  competitors may unfavorably impact the pricing of our cloud and software offerings."
- Same document, competition risk factor: "If our competitors offer deep discounts on certain
  products or services or develop products that the marketplace considers more valuable, we may
  need to lower prices, introduce pricing models and offerings or offer other terms that are less
  favorable to us to compete successfully."
- **Alphabet 10-K FY2025 (0001652044-26-000018), Item 1A:** the only price sentences touching
  infrastructure concern Alphabet's own input costs ("availability and pricing of third-party
  equipment and other technical infrastructure operations costs, including network capacity,
  energy, and equipment costs"), not the price Google Cloud charges. Nothing on Google Cloud
  selling prices was found in the 10-K or the Q2 2026 10-Q.

---
## TABLE A, ADDENDUM (resume session, 2026-09-13): AMAZON'S OWN PRICING SENTENCE, WHICH THE A.4 SWEEP DID NOT COVER
A.4 swept the six PEER documents. The subject's own MD&A carries a filed pricing statement for AWS in every annual report read,
FY2015 to FY2025, and in the 10-Qs for Q3 2025 and Q2 2026, verbatim:
- FY2015 10-K (`_research 2026-09-06 MSFT/AMZN_FY2015_10K.txt`): "AWS sales increased 70%, 49%, and 69% in 2015, 2014, and 2013 ... The sales growth
  primarily reflects increased customer usage, partially offset by pricing changes. Pricing changes were driven largely by our continued efforts to reduce
  prices for our customers." and "The decrease in AWS segment operating income in absolute dollars in 2014 ... is primarily due to pricing changes".
- FY2017 10-K (0001018724-18-000005), FY2018 10-K (0001018724-19-000004), FY2019 10-K (0001018724-20-000004), FY2020 10-K (0001018724-21-000004), FY2021 10-K (0001018724-22-000005): the same
  two sentences ("partially offset by pricing changes. Pricing changes were driven largely by our continued efforts to reduce prices for our customers.").
- FY2022 10-K (0001018724-23-000004), FY2023, FY2024 (0001018724-25-000004), FY2025 (0001018724-26-000004), 10-Q Q3 2025 and 10-Q Q2 2026
  (0001018724-26-000026): "The sales growth primarily reflects increased customer usage, partially offset by pricing changes primarily driven by long-term
  customer contracts."
**Thirteen consecutive years (2013 to H1 2026) in which the filer says price moved against AWS revenue; no year found in which it says price added to it.**

## TABLE B, RETAIL AND MARKETPLACE
Full table with every accession, window and verbatim quote: `peers/tableB_retail.md`. Summary (USD millions unless stated; latest FY):

| Filer / unit | Window | Revenue | Growth | Op. margin | Marketplace or e-commerce measure | Source |
|---|---|---|---|---|---|---|
| Amazon North America | FY Dec-2025 / H1 2026 | 426,305 / 220,320 | +10.0% / +14.2% | 6.9% / 7.9% | 3P seller services 172,162 (+10.3%); seller unit mix 60-62% of paid units Q2 2024-Q2 2026 (EX-99.1 only) | 10-K 0001018724-26-000004; 10-Q 0001018724-26-000026 |
| Amazon International | same | 161,894 / 81,986 | +13.3% / +16.7% | 2.9% / 3.8% | | same |
| Walmart U.S. | FY Jan-2026 / H1 FY27 | 482,975 / 242,358 | +4.4% / +4.0% | 5.2% / 5.8% | eCommerce ~$99.6bn, +25.6% (filed dollars) | 10-K 0000104169-26-000055; 10-Q 0000104169-26-000154 |
| Walmart consolidated | same | 706,413 | +4.7% | 4.2% | global eCommerce ~$150.4bn, +24.4%; global advertising "nearly $6.4 billion", +46% incl. VIZIO (release) | same; 8-K 0000104169-26-000032 |
| eBay | FY2025 / H1 2026 | 11,100 / 6,223 | +8% / +17% | 20.5% / 20.7% | GMV 79,609; filed take rate 13.94% | 10-K 0001065088-26-000027 |
| MercadoLibre | same | 28,893 / 19,014 | +39.1% / +49.4% | 11.1% / 6.8% | GMV 65,037 (+26.4%); commerce services / GMV 19.6% | 10-K 0001099590-26-000006 |
| Shopify | same | 11,556 / 6,753 | +30.1% / +34.0% | 12.7% / 12.9% | GMV 378,441 (+29.5%); revenue / GMV 3.1% | 10-K 0001594805-26-000007 |
| PDD (RMB) | same | 431,846 / 218,587 | +9.7% / +9.5% | 21.6% / 21.7% | GMV not filed | 20-F 0001104659-26-050727 |

Fee conduct, filed: **no Amazon seller, fulfillment, referral or Prime fee change, and no Prime fee history, is stated in any Amazon document on disk**
(searches in tableB B.5(a)). Third-party seller services growth (ex-FX 7-16% by quarter) tracks paid-unit growth (8-17%) with seller unit mix flat at 60-62%.
eBay: "Consumers and merchants that sell goods on our platforms also have many alternatives, including general ecommerce marketplaces, such as Amazon and
Alibaba" and "Sellers may also choose to sell their goods through alternative channels, such as multi-channel services like Shopify". FTC and private suits
allege monopoly in "online superstores and marketplace services"; courts "denied dismissal of claims alleging that Amazon's pricing policies are an unlawful
restraint of trade" (10-K FY2024); Italy fine reduced to EUR 752M with remedial actions (10-K FY2025).

## TABLE C, ADVERTISING
Full table: `peers/tableC_ads_and_cloud_text.md`. Summary:

| Filer / line | 2025 revenue | 2025 growth | H1 2026 growth | Unit or price metric filed? | Margin filed? |
|---|---|---|---|---|---|
| Amazon advertising services | 68,635 | +22.1% | +25.1% | none | no (inside NA and International) |
| Alphabet Google advertising | 294,691 | +11.4% | +14.9% | paid clicks +13%, CPC +3% (Q2 2026) | Google Services 40.7% (incl. subscriptions and devices) |
| Meta advertising | 196,175 | +22.1% | +30.1% | impressions +14%, price per ad +12% (Q2 2026) | Family of Apps 51.6% (2025), 43.3% (H1 2026) |
| Walmart global advertising (release) | ~6,400 (FY Jan-2026) | +46% incl. VIZIO | +37% / +38% (Q1, Q2 FY27) | none | no |

Meta 10-K FY2025 and 10-Q Q2 2026: "the online commerce vertical was the largest contributor to the increase in advertising revenue".

## NAMES AMAZON AS A COMPETITOR?
- **Oracle** 10-K FY2026: yes, in Item 1 ("Amazon.com, Inc.") and Item 1A ("OCI's multicloud services work with a number of our competitors' products,
  including Microsoft Azure, Amazon Web Services and Google Cloud").
- **eBay** 10-K FY2025: yes, twice, in Item 1A (quoted above).
- **MercadoLibre** 10-K FY2025: not in Competition; named in a Mexican antitrust passage and as a cloud vendor ("our cloud providers, the largest of which are
  Amazon Web Services and Google Cloud Platform").
- **Alphabet, Meta, Microsoft, Walmart, Shopify, PDD**: no instance found (0 hits). Amazon's own 10-K names no competitor.

## CLOUD MULTI-SOURCING, FILED
- Microsoft 10-K FY2026: "higher purchases of licenses running in multi-cloud environments"; related party: "we recorded revenue from commercial arrangements
  with OpenAI, inclusive of revenue-sharing payments, of $24.1 billion" (AWS's OpenAI commitment: $38.0bn expanded by $100.0bn).
- Oracle 10-K FY2026: "we offer our customers multicloud services whereby our customers can combine cloud services from multiple clouds with the goal of
  optimizing cost, functionality and performance".
- Meta 10-Q Q2 2026: "$349.31 billion of non-cancelable contractual commitments ... most of which are related to third-party cloud capacity arrangements";
  Amazon's Q1 2026 release lists Meta among "new AWS agreements".
- Amazon 10-K FY2025 and 10-Q Q2 2026: no multi-cloud, switching, egress or migration sentence (0 hits).

## NOT OBTAINED
See B.7 and C.7 in the two table files. The load-bearing absences, stated: Amazon GMV and take rate; any Amazon fee change or Prime fee history;
Amazon advertising price, unit or margin figures; the OpenAI and Anthropic shares of the $496bn backlog; Microsoft Intelligent Cloud's
infrastructure-only margin. Not rowed: Alibaba (20-F filer, not fetched), Temu (inside PDD), Shein and the private and Chinese clouds
(no SEC filings), CoreWeave (not fetched). **None of the absences is load-bearing for the verdict recorded in the run file** (see Q2 there).

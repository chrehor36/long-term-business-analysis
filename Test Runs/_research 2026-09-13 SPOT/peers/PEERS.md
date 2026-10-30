# SPOT run - competitor row and label side: EVIDENCE ONLY

Gathered 2026-09-13. No moat verdict, no ranking, no substitute call. Every figure carries
document, filing date and accession (or URL); every qualitative claim a verbatim quote with
local file. Texts saved in this folder. SEC User-Agent `BRK research chrehor36@gmail.com`.

Status: COMPLETE 2026-09-13. Sections: Peer 1 TME; Peer 2 SIRI/Pandora; Peer 3 Apple, Alphabet, Amazon; Peer 4 label side (WMG, UMG, Sony); Peer 5 Deezer; LIMITS AND DEFECTS.
Quote check: `verify2.py` searches every blockquote in the saved source texts (116 checked; 3 not found whole, all three are sentences interrupted by a page footer in the extracted text and are flagged at the quote, or a parenthetical containing quote marks that the checker mis-splits, verified by hand).

---
## PEER 1: TENCENT MUSIC ENTERTAINMENT GROUP (TME; CIK 0001744676; 20-F filer; IFRS; RMB)

### Documents (rung 1, SEC primary filings, fetched 2026-09-13)

| Doc | Filed | Accession | Local file (stripped text; `.flat.txt` = same text with table cells joined by ` pipe `) |
|---|---|---|---|
| 20-F FY2025 | 2026-04-17 | 0001193125-26-160257 | `TME_20F_FY2025.txt` / `.flat.txt` (tme-20251231.htm) |
| 20-F FY2024 | 2025-04-23 | 0000950170-25-056949 | `TME_20F_FY2024.txt` / `.flat.txt` (tme-20241231.htm) |
| 20-F FY2023 | 2024-04-18 | 0000950170-24-045593 | `TME_20F_FY2023.txt` / `.flat.txt` (tme-20231231.htm) |
| 20-F FY2022 | 2023-04-25 | 0000950170-23-014459 | `TME_20F_FY2022.txt` / `.flat.txt` (tme-20221231.htm) |
| 20-F FY2021 | 2022-04-26 | 0001193125-22-120210 | `TME_20F_FY2021.txt` / `.flat.txt` (d242038d20f.htm) |
| Spotify 20-F FY2025 (for the reverse stake only) | 2026-02-10 | 0001628280-26-006874 | `..\20F_FY2025__ck0001639920-20251231.txt` (already on disk) |

### Figures, as filed (Item 5 operating-metrics table and "Results of Operations" table of each 20-F)

Each year's figure is taken from the 20-F for that fiscal year; later 20-Fs were checked and agree unless flagged.

| Line | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Unit |
|---|---|---|---|---|---|---|
| Online music paying users (annual average of quarters) | 68.6 | 84.2 | 100.9 | 117.6 | 125.1 | millions |
| Online music monthly ARPPU (subscription revenue only) | 8.9 | 8.6 | 10.0 | 10.8 | 11.8 | RMB |
| Online music MAUs | not tabulated in FY2021 20-F; 622 per FY2022 20-F (mobile) and FY2023 20-F (restated basis) | 588 as filed (FY2022 20-F, mobile MAUs); 620 restated (FY2023 20-F, incl. IoT) | 589 | 570 | 547 | millions |
| Online music paying ratio | 11.0% | 14.3% as filed; 13.6% restated (FY2023 20-F) | 17.1% | 20.6% | 22.9% | % |
| Music subscription revenue | 7,333 | 8,699 | 12,096 | 15,227 | 17,660 | RMB millions |
| Online music services revenue | 11,467 | 12,483 | 17,325 | 21,742 | 26,726 | RMB millions |
| Social entertainment services and others revenue | 19,777 | 15,856 | 10,427 | 6,659 | 6,176 | RMB millions |
| Total revenues | 31,244 | 28,339 | 27,752 | 28,401 | 32,902 | RMB millions |
| Cost of revenues | (21,840) | (19,566) | (17,957) | (16,376) | (18,367) | RMB millions |
| of which Service costs | 18,992 | 16,540 | 14,176 | 11,974 | 11,349 | RMB millions |
| Gross profit | 9,404 | 8,773 | 9,795 | 12,025 | 14,535 | RMB millions |
| Gross margin (as filed, consolidated) | 30.1% | 31.0% | 35.3% | 42.3% | 44.2% | % |
| Operating profit | 3,800 | 4,443 | 6,059 | 8,710 | 13,364 | RMB millions |

Sources: paying users / ARPPU / MAU / paying ratio: FY2021 20-F Item 5 table (columns 2019, 2020, 2021); FY2022 20-F Item 5 table (2020-2022); FY2023, FY2024, FY2025 20-F Item 5 tables. Subscription revenue: note (2) or (1) under each table and the "Key Components of Results of Operations" paragraph. Revenue, cost, gross profit, operating profit: "Results of Operations" table, each 20-F. Service costs: MD&A "Cost of revenues" paragraphs (FY2021 20-F for 2021; FY2023 20-F for 2022; FY2025 20-F cost-of-revenues table for 2023-2025).

FY2025 operating profit includes "the gain of RMB2,373 million (US$339 million) on deemed disposal of an associate" (FY2025 20-F MD&A, "Other gains, net"), the UMG consortium distribution. Flagged; not adjusted.

**Definition of the metrics (FY2025 20-F, Introduction):**
> "“monthly ARPPU” of our online music services for any given period refers to the monthly average of (i) the revenues of the relevant services for that period divided by (ii) the number of paying users of the relevant services for that period;"

> "“paying users” for our online music services (i) for any given quarter refers to the average of the number of users whose subscription packages remain active as of the last day of each month of that quarter; and (ii) for any given year refers to the average of the total number of paying users of the four quarters in that year; the number of those users who only purchase digital music singles and albums during a particular period are not included in the calculation of the number of paying users for our online music services for that period, because such users' purchasing patterns reflect specific releases, which may fluctuate from period to period;"

> "(1) The revenues used to calculate the monthly ARPPU of online music services include revenues from subscriptions only. The revenues from subscriptions for the periods indicated were RMB12,096 million, RMB15,227 million and RMB17,660 million (US$2,525 million), respectively." (FY2025 20-F, Item 5)

(Extraction note: `edgar.py strip_html` converts curly quotation marks to straight ones; the curly marks around the defined terms above were restored by hand from the filing convention and are not verified character-for-character.)

MAU restatement (FY2023 20-F, Item 5 note (1)):
> "Starting from the first quarter of 2023, online music MAUs began to include unique mobile and certain IoT devices. Accordingly, comparative figures for prior periods were updated to conform to the current presentation."

**Segment:** one reportable segment. FY2025 20-F Item 5: "Our chief operating decision maker has determined that we have only one reportable segment." Note 2.5: "the chief operating decision-makers and management personnel do not segregate the Group's business by product or service lines. Hence, the Group has only one operating segment."

### Content cost / royalty share: verbatim

Royalty amount is NOT separately disclosed. Service costs are disclosed but bundle royalties with live-streaming revenue-sharing fees and delivery costs:
> "(i) Service costs mainly comprised content costs of royalties, revenue sharing fees paid to content creators and content delivery costs that primarily consisted of server, cloud services and bandwidth costs." (FY2025 20-F, Note 8 Expenses by nature)

> "Our cost of revenues primarily includes service costs, which mainly comprise (i) content costs, which primarily consist of royalties paid to music labels and other content partners and our in-house production costs. Such costs are used to support both our online music services and social entertainment services;" (FY2025 20-F, Item 5)

Direction of royalty cost, stated without amounts:
> "The declined revenues from social entertainment services led to lower revenue sharing fees, which was the primary reason for the overall decrease in service costs, while our content costs of royalties increased year-over-year." (FY2025 20-F, MD&A 2025 vs 2024)

> "Our gross margin increased from 35.3% in 2023 to 42.3% in 2024. This increase in gross margin was primarily driven by strong revenue growth from music subscriptions and advertising services, as well as the ramp up of our own content. Additionally, our revenue growth outpaced the increase in content costs of royalties, which positively impacted our margins. Furthermore, the reduction in revenue-sharing ratio for live streaming performers also contributed to the margin improvement." (FY2024 20-F, MD&A)

> "The declined revenues from social entertainment services led to lower revenue sharing fees, which was the primary reason for the overall decrease in service costs, partially offset by the increase in content royalty costs." (FY2023 20-F, MD&A 2023 vs 2022)

> "This increase in gross margin was primarily due to the growth of revenues from music subscriptions and advertising services, and the ramp-up of our own content." (FY2023 20-F, MD&A)

> "This increase in gross margin was primarily due to the effective control and optimization of content costs including decreased revenue sharing fees for live streaming business." (FY2022 20-F, MD&A 2022 vs 2021)

> "This decrease in gross margin was primarily due to shifts in the revenues mix where revenue from online music accounts for a higher percentage of revenue but typically has a lower gross margin. Such decrease was also attributable to the increased investments in new product and content offering and content costs such as long-form audio." (FY2021 20-F, MD&A 2021 vs 2020)

How labels are paid, and the non-exclusive basis (FY2025 20-F, Item 4 "Content Sourcing Arrangements"):
> "We license musical recording rights and/or music publishing rights underlying music content mainly on terms ranging from one to three years from domestic and international music labels."

> "We pay music labels for licensed music content based on licensing fee and revenue-sharing incentive royalties. Under such fee arrangements, the amounts of licensing fees and incentive royalties depend on multiple factors including the type of content, the popularity of the performers, as well as our relationships with the licensors. Payments under the licenses are generally made in installments throughout the duration of the licenses."

> "Our licensing agreements with music labels and music copyright owners are on a non-exclusive basis."

Minimum guarantees (FY2025 20-F, Item 3.D):
> "Certain of our license agreements for music and long-form audio content require that we make minimum guarantees to copyright owners, that may be tied to our number of users or the amount of content used or distributed on our platform."

> "The duration of our license agreements that contain minimum guarantees is typically between one to three years, but our paying users may cancel their subscriptions at any time."

### Relations with the major labels: verbatim

> "Over the years, we have developed long-term relationships with a broad range of music labels, including major domestic and international labels across various music genres, enabling us to better serve the diverse musical preferences of our audience. For example, we renewed contracts with Sony Music Entertainment, Warner Music Group, and Bin-music in 2025 to enhance our timeless and classic music offerings." (FY2025 20-F, Item 4)

> "For example, our new multi-year contracts with Sony Music Entertainment introduced the 360 Reality Audio sound privilege for SVIP members, fostering a more immersive listening experience." (FY2025 20-F, Item 4)

End of exclusivity by regulator (FY2025 20-F, Item 3.D):
> "On July 24, 2021, the SAMR issued an Administrative Penalty Decision to Tencent regarding its acquisition of CMC in 2016. Pursuant to the decision, we shall implement a rectification plan to, among other things, terminate exclusive music copyright licensing arrangements within 30 days from the date of the decision. To comply with such decision, Tencent and we have terminated the exclusivity with upstream copyright holders subject to certain limited exceptions specified in the decision."

> "While we are pursuing non-exclusive collaborations with upstream copyright holders, there can be no assurance that all the licenses once exclusively available to us will remain available at royalty rates and on terms that are commercially reasonable or at all. In addition, the termination of exclusive copyright licensing arrangements may potentially lower the competition barriers in a way that benefits some of our competitors."

Equity tie to UMG (FY2025 20-F, Note 7, note i):
> "In March 2025, the consortium completed a transfer of the UMG shares held by the consortium to its members through distribution-in-kind. Following the distribution, the Group held directly 2 % equity interests in UMG and the Group designated the investment as financial assets at fair value through other comprehensive income."

Competition (FY2025 20-F, Item 4):
> "We primarily compete with other online music and audio entertainment providers in China for users' time and attention. Additionally, we face broader competition from various online content offerings, including long- and short-form videos, karaoke services, live streaming, radio services, literature, and games provided by other online service providers."

Litigation by the domestic rival (FY2025 20-F, Item 8):
> "In June 2024, NetEase Cloud Music Inc., together with some of its affiliates, (collectively, "NetEase") filed a lawsuit in the Zhejiang Provincial Higher People's Court against us and some of our affiliates, asserting claims of abuse of market dominance in relation to our music licensing practices in the Chinese market, among others."

### Cross-holdings Spotify / TME / Tencent: verbatim

TME side (FY2025 20-F, Item 6.E beneficial ownership table, as of March 31, 2026): row "Spotify (2) | 282,830,698 | 19.1 |" (Class A number and percent), total 282,830,698, 9.0% of total ordinary shares, 1.1% of aggregate voting power.

> "(2) The number of Class A ordinary shares beneficially owned represents 282,830,698 Class A ordinary shares held by Spotify AB, a company incorporated in Sweden, which is beneficially owned and controlled by Spotify Technology S.A. (NYSE: SPOT)."

> "pursuant to the Spotify Investor Agreement, Spotify has given Tencent a sole and exclusive right to vote our securities beneficially owned by Spotify and its affiliates, while pursuant to the Tencent Voting Undertaking, Tencent is obligated to vote 50% of the securities subject to the foregoing proxy from Spotify in proportion to votes cast for and against by non-Spotify shareholders" (FY2025 20-F, Item 6.E, note (1))

> "In December 2017, (i) we issued 282,830,698 ordinary shares to Spotify AB (a wholly owned subsidiary of Spotify Technology S.A., or Spotify), and (ii) Spotify, in exchange, issued 8,552,440 ordinary shares (after giving effect to a 40-to-one share split of Spotify's ordinary shares) to TME Hong Kong." (FY2025 20-F, Item 7.B)

> "In connection with our investment in Spotify, on December 15, 2017, an investor agreement was entered into by and among Spotify, TME, TME Hong Kong, Tencent and a wholly owned subsidiary of Tencent (together with TME, TME Hong Kong and Tencent, the "Tencent Investors") and certain Spotify parties, pursuant to which Spotify's co-founder has the sole and exclusive right to vote, in his sole and absolute discretion, any of Spotify's securities beneficially owned by the Tencent Investors or their controlled affiliates." (FY2025 20-F, Item 7.B)

> "The investments in listed equity securities mainly represented its investment in Spotify Technology S.A. ("Spotify") and UMG." (FY2025 20-F, Note 18; listed equity investments RMB 14,498 million at 2024-12-31 and RMB 26,217 million at 2025-12-31, not split by investee)

Spotify side (Spotify 20-F FY2025, 0001628280-26-006874, Item 6.E table as of December 31, 2025): row "Tencent (3) | 16,631,969 | 8.1 | %" of ordinary shares; voting-power cell carries footnote "(5)" instead of a percentage.

> "(3) Includes 4,276,200 ordinary shares held of record by TME Hong Kong, 9,076,240 ordinary shares held of record by Image Frame, 3,227,920 ordinary shares held of record by Tencent Mobility Limited, and 51,609 ordinary shares held by Distribution Pool Limited"

> "(5) Mr. Ek exercises voting power over the ordinary shares held of record by TME Hong Kong, Image Frame, Tencent Mobility Limited, and Distribution Pool Limited through his indirect ownership of D.G.E. Investments, which holds an irrevocable proxy with regard to these ordinary shares."

> "The Group's approximate 9 % investment in TME is carried at fair value through other comprehensive income." (Spotify 20-F FY2025, fair value note; TME investment €2,111 million at December 31, 2025 and €1,550 million at December 31, 2024)

Record-only note: TME's 20-F says 8,552,440 Spotify shares were issued to TME Hong Kong in 2017; Spotify's 20-F lists 4,276,200 held of record by TME Hong Kong at 2025-12-31. Neither passage read explains the difference. NOT reconciled.

### XBRL cross-check (operator rule 4)

companyfacts (CIK 1744676) `ifrs-full:Revenue`, CNY, FY2024, accession 0000950170-25-056949: 28,401,000,000. Filed statement: FY2024 20-F "Results of Operations" table, Total revenues 28,401 (RMB millions); the FY2025 20-F comparative column also 28,401. MATCH. `ifrs-full:GrossProfit` FY2024: 12,025,000,000 vs table 12,025. MATCH. (`companyfacts_1744676.json` saved.)

Defect: companyfacts has ingested the FY2025 20-F (0001193125-26-160257) for one dei fact only (EntityCommonStockSharesOutstanding 3,147,809,000); no FY2025 financial facts exist there. FY2025 figures above come from the filed document only.

### TME: not disclosed

- Royalty / content-cost amount, and royalty as % of music revenue: NOT DISCLOSED (bundled in service costs with live-streaming revenue sharing and bandwidth).
- Gross margin of online music alone: NOT DISCLOSED (one segment; consolidated gross margin only).
- Payments to any named label, or share of content spend by label: NOT DISCLOSED.
- Contractual royalty rate or label share of subscription revenue: NOT DISCLOSED.
- Advertising revenue amount inside online music: NOT DISCLOSED as a level in the passages read (the FY2025 MD&A gives only an increment, "RMB923 million", combining offline performances, artist-management services and advertising).
- TME share of the Chinese streaming market: no figure found in the passages read.

---
## PEER 2: SIRIUS XM HOLDINGS INC. (SIRI; CIK 0000908937; 10-K filer; US GAAP; US$) - PANDORA AND OFF-PLATFORM SEGMENT

### Documents (rung 1, SEC primary filings, fetched 2026-09-13)

| Doc | Filed | Accession | Local file |
|---|---|---|---|
| 10-K FY2025 | 2026-02-05 | 0000908937-26-000006 | `SIRI_10K_FY2025.txt` / `.flat.txt` (siri-20251231.htm) |
| 10-K FY2024 | 2025-01-30 | 0000908937-25-000005 | `SIRI_10K_FY2024.txt` / `.flat.txt` (siri-20241231.htm) |
| 10-K FY2023 | 2024-02-01 | 0000908937-24-000008 | `SIRI_10K_FY2023.txt` / `.flat.txt` (siri-20231231.htm) |
| 10-K FY2022 | 2023-02-02 | 0000908937-23-000006 | `SIRI_10K_FY2022.txt` / `.flat.txt` (siri-20221231.htm) |
| 10-K FY2021 | 2022-02-01 | 0000908937-22-000007 | `SIRI_10K_FY2021.txt` / `.flat.txt` (siri-20211231.htm) |

All five 10-Ks sit under CIK 908937 on EDGAR. The FY2024 and FY2025 10-Ks are filed by the post-Liberty-Media-transaction registrant; the FY2025 10-K segment note recasts the 2023 SiriusXM segment (e.g. 2023 "Other revenue" 329 vs 136 plus equipment 193 in the FY2023 10-K) but the 2023 Pandora and Off-platform column is identical in both filings. Only the Pandora column is used below.

### Figures, as filed (US$ millions unless stated; subscribers and MAUs in thousands)

| Line | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Source |
|---|---|---|---|---|---|---|
| Pandora monthly active users - all services (Dec 31) | 52,275 | 47,638 | 46,026 | 43,344 | 41,112 | MD&A operating-metrics table, each year's 10-K |
| Pandora self-pay subscribers (Dec 31) | 6,324 | 6,215 | 6,008 as filed; 6,053 in FY2024 10-K (incl. 45 Cloud Cover) | 5,774 (incl. 57 Cloud Cover) | 5,630 | same |
| Pandora paid promotional subscribers | 69 | 0 ("—") | 0 ("—") | not tabulated | not tabulated | same |
| Pandora weighted average subscribers | n/c | n/c | n/c | 5,929 | 5,698 | FY2025 10-K non-GAAP metrics table |
| Ad supported listener hours (billions) | n/c | n/c | n/c | 9.94 | 9.75 | same |
| Advertising revenue per thousand listener hours (RPM) | n/c | n/c | n/c | $100.59 | $91.78 | same |
| Subscriber revenue (segment) | 530 | 522 | 524 | 540 | 526 | segment note (FY2022 10-K for 2021-2022; FY2025 10-K for 2023-2025) and MD&A text |
| Advertising revenue (segment; on- and off-platform combined) | 1,542 | 1,576 | 1,589 | 1,606 | 1,615 | same |
| Total segment revenue | 2,072 | 2,098 | 2,113 | 2,146 | 2,141 | same |
| Revenue share and royalties | 1,140 | 1,250 | 1,292 | 1,270 | 1,308 | MD&A cost-of-services table and text, each year's 10-K; segment note FY2024-FY2025 |
| Segment cost of services (note basis, excl. share-based payment) | (1,329) | (1,443) | (1,475) | (1,441) | (1,471) | segment note |
| Segment gross profit | 743 | 655 | 638 | 705 | 670 | segment note |

n/c = not collected from that year's 10-K (the FY2025 10-K gives only 2024-2025 for these lines).

FY2021: the segment was named "Pandora" in the FY2021 10-K ("two reportable segments: Sirius XM and Pandora") and "Pandora and Off-platform" from the FY2022 10-K, which shows the same 2021 figures (2,072 revenue, 743 gross profit).

FY2025 MD&A cost-of-services table gives "Total Pandora and Off-platform cost of services | 1,475" and "Programming and content | 64"; the segment note gives 1,471 and 61. The note states share-based payment "has been excluded" from segment cost; the MD&A table does not exclude it. Both recorded; the difference is not reconciled line by line here.

COMPUTED (arithmetic only, `calc_siri.py`; not filed ratios):

| Ratio | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Revenue share and royalties / segment revenue | 55.0% | 59.6% | 61.1% | 59.2% | 61.1% |
| Segment gross profit / segment revenue | 35.9% | 31.2% | 30.2% | 32.9% | 31.3% |
| Subscriber revenue / segment revenue | 25.6% | 24.9% | 24.8% | 25.2% | 24.6% |

Defect in the ratio: "Revenue share and royalties" includes podcast revenue share and payments to third-party publishers and ad servers on off-platform ad sales, not only music royalties (definitions quoted below). Music royalties alone are NOT DISCLOSED.

### Definitions and drivers: verbatim

> "Pandora and Off-platform Revenue Share and Royalties includes licensing fees paid for streaming music, podcast content, and revenue share paid to third party publishers. Payments are made based on advertising impressions delivered or click-through actions, and these costs are recorded in the related period." (FY2025 10-K, MD&A)

> "For the years ended December 31, 2025 and 2024, revenue share and royalties were $1,308 and $1,270, respectively, an increase of 3%, or $38, and increased as a percentage of total Pandora and Off-platform revenue. The increase was driven by podcast revenue share, partially offset by a decline in the subscriber base." (FY2025 10-K, MD&A)

> "For the years ended December 31, 2024 and 2023, revenue share and royalties were $1,270 and $1,292, respectively, a decrease of 2%, or $22, and decreased as a percentage of total Pandora and Off-platform revenue. The decrease was primarily due to lower on-platform revenue, reduced listener hours, and decreased revenue share related to podcasts." (FY2024 10-K, MD&A)

> "For the years ended December 31, 2023 and 2022, revenue share and royalties were $1,292 and $1,250, respectively, an increase of 3%, or $42, and increased as a percentage of total Pandora and Off-platform revenue. The increase was primarily due to higher podcast revenue share driven by growth in podcast advertising revenue as well as higher royalty expense due to costs related to an increase in certain web streaming royalty rates." (FY2023 10-K, MD&A)

> "For the years ended December 31, 2022 and 2021, revenue share and royalties were $1,250 and $1,140, respectively, an increase of 10%, or $110, and increased as a percentage of total Pandora revenue. The increase was primarily due to costs related to the acquisition of rights to sell advertising in certain podcasts." (FY2022 10-K, MD&A)

> "For the years ended December 31, 2021 and 2020, revenue share and royalties were $1,140 and $937, respectively, an increase of 22%, or $203, but remained flat as a percentage of total Pandora revenue. The increase was primarily due to higher royalty rates associated with owned and operated revenue as well as higher AdsWizz revenue, the inclusion of Stitcher and the growth in other off-platform revenue." (FY2021 10-K, MD&A)

> "The majority of revenue from Pandora is generated from advertising on Pandora's ad-supported radio service. Pandora also derives subscription revenue from its Pandora Plus and Pandora Premium subscribers. Our Pandora and Off-platform business also sells advertising on other audio platforms and in widely distributed podcasts, which we consider to be off-platform services. As of December 31, 2025, Pandora had approximately 41.1 million monthly active users and 5.6 million subscribers." (FY2025 10-K, Item 7 overview)

> "For the years ended December 31, 2025 and 2024, Pandora and Off-platform subscriber revenue was $526 and $540, respectively, a decrease of 3%, or $14. The decrease was driven by a decline in the subscriber base, partially offset by the full-year impact of prior year price increases on Pandora subscription plans." (FY2025 10-K, MD&A)

> "Ad RPM is calculated by dividing advertising revenue by the number of thousands of listener hours of our Pandora advertising-based service." / "For the years ended December 31, 2025 and 2024, RPM was $91.78 and $100.59, respectively. The decrease was driven by lower advertiser demand in streaming music due to macroeconomic uncertainty." (FY2025 10-K, MD&A)

> "The number of subscribers to our SiriusXM service has declined for the past two years, including in 2025. Similarly, the number of monthly active users to our ad-supported Pandora service has declined consistently for several years, including in 2025. This loss of subscribers to our SiriusXM service and the decline in monthly active users to our Pandora ad-supported service is likely to continue in the future." (FY2025 10-K, Item 1A; a page number "20" and "Table of Contents" interrupt the sentence in the extracted text between "including in" and "2025")

> "(1) Pandora and Off-platform self-pay subscribers include Cloud Cover subscribers of 57 and 45 as of December 31, 2024 and 2023, respectively." (FY2024 10-K, MD&A metrics table note)

### How Pandora licenses music: verbatim (FY2025 10-K, Item 1)

> "Pandora must also license mechanical rights to offer the interactive features of the Pandora services. For our Pandora subscription services, copyright holders receive payments for these rights at the rates determined in accordance with the statutory license set forth in Section 115 of the United States Copyright Act. For the five-year period commencing January 1, 2023 and ending December 31, 2027, Pandora agreed to pay the greater of 15.1% of revenues or 26.2% of record label payments annually, rising over the five-year period to 15.35% of revenues or 26.2% of record label payments by 2027."

> "Interactive streaming services, such as Pandora Plus and Pandora Premium, do not qualify for the statutory license and those services must negotiate direct license arrangements with the owners of copyrights in sound recordings."

> "Pandora Services. For our Pandora services, we have entered into direct license agreements with major and independent music labels and distributors for a significant majority of the sound recordings that stream on the Pandora ad-supported service, Pandora Plus and Pandora Premium."

> "The royalty rates under many of those direct licenses, which cover a large majority of the sound recordings that we perform on Pandora, are indexed to the statutory rates established by the CRB."

Item 1A, FY2025 10-K:
> "The economic terms of these direct licenses are onerous and grant the licensors broad rights over the Pandora services. As a result of these terms, we may not be able to profitably operate the Pandora services. However, the economic terms of these direct licenses may be "market," given the rates paid by Pandora's competitors. Competition for Pandora's services are primarily offered by entities that provide music and entertainment services as a small part of a larger business, such as Apple, Google, Amazon and YouTube. These competitors have the ability to bear these onerous economic provisions to a much greater extent than our Pandora business. We have not been able to negotiate or obtain lower royalty rates under these direct licenses."

> "Several of these direct licenses also include provisions related to the terms of those agreements relative to other content licensing arrangements, which are commonly referred to as "most favored nation" clauses. These provisions have caused, and may in the future cause, our payments under those agreements to escalate substantially."

Same risk factor, FY2021 10-K (wording drift noted): "The economic terms of these direct licenses are onerous and, as a result, we may not be able to profitably operate the Pandora services. However, the economic terms of these direct licenses may be "market," given the rates paid by Pandora's competitors. Competition for Pandora's services are primarily offered by entities that provide music and entertainment services as a small part of a larger business, such as Apple, Google and Amazon. These competitors have the ability to bear these onerous economic provisions to a much greater extent than our Pandora business. We may not be able to negotiate or obtain lower royalty rates under these direct licenses." (FY2021 names Apple, Google and Amazon and says "may not be able to negotiate"; FY2025 adds YouTube and says "have not been able to negotiate".)

### What the 10-K says about competing with Spotify, Apple Music, Amazon, YouTube: verbatim

FY2025 10-K, Item 1, Competition:
> "Streaming and on-demand services, including Amazon Prime, Apple Music, Spotify, TikTok and YouTube, compete with our SiriusXM and Pandora services. The widespread deployment of Apple CarPlay and Android Auto has increased the visibility of these on-demand services in many vehicles and further strengthened their ability to compete with our SiriusXM and Pandora services for listeners."

> "Major online providers also make high fidelity digital streams available at no cost or, in some cases, for less than the cost of a satellite radio subscription. Certain of these services include advanced functionality, such as personalization and customization and allow the user to access large libraries of content. These services, in some instances, are also offered through devices sold by the service providers including Apple, Google and Amazon. These services compete with our services at home, in vehicles, and wherever audio entertainment is consumed."

FY2025 10-K, Item 1A:
> "Our subscribers and listeners can obtain similar content for free through Spotify, YouTube and other internet services as well as terrestrial radio stations. We also compete for the time and attention of our listeners with providers of other in-home and mobile entertainment services, and we compete for advertising sales with large scale online advertising platforms, such as YouTube, Amazon, Facebook and Google, and with traditional media outlets."

> "actions by our competitors, such as Spotify, Apple, Google, Amazon, YouTube and other audio entertainment and information providers."

> "competing effectively for advertising with other dominant online products and services, such as Spotify, Google, Facebook and YouTube, as well as other marketing and media outlets;"

FY2021 10-K, Item 1, Competition (for the start of the window):
> "Streaming and on-demand services, including Amazon Prime, Apple Music, Spotify and YouTube, compete with our Sirius XM and Pandora services."

### XBRL cross-check (operator rule 4)

companyfacts (CIK 908937) `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax`, FY2025 (2025-01-01 to 2025-12-31), accession 0000908937-26-000006: 8,558,000,000. Filed statement: FY2025 10-K segment note, "Total revenue | 6,417 | 2,141 | 8,558". MATCH. Same tag FY2021, accession 0000908937-22-000007: 8,696,000,000 vs FY2021 10-K segment note total 8,696. MATCH. (`companyfacts_908937.json` saved.) Segment (Pandora) figures are dimensioned facts and are not carried in companyfacts; they come from the filed notes only.

### SIRI / Pandora: not disclosed

- Music royalties alone (separate from podcast revenue share and off-platform publisher payments): NOT DISCLOSED.
- On-platform (Pandora) advertising revenue separate from off-platform (AdsWizz, podcasts, SoundCloud representation): NOT DISCLOSED as a level in the passages read.
- Pandora Plus vs Pandora Premium subscriber split, and subscription prices: NOT DISCLOSED in the 10-K (searched "per month", "monthly fee", "$x.99": no hits).
- Payments to named labels: NOT DISCLOSED.
- Pandora operating income (below gross profit): NOT DISCLOSED (segment measure is gross profit; operating costs are not allocated).

---
## PEER 3: APPLE, ALPHABET, AMAZON - IS MUSIC STREAMING DISCLOSED AT ALL? (latest 10-K, FY2025)

### Documents

| Doc | Filed | Accession / URL | Local file |
|---|---|---|---|
| Apple 10-K FY2025 (FYE 2025-09-27) | 2025-10-31 | 0000320193-25-000079 | `AAPL_10K_FY2025.txt` / `.flat.txt` (aapl-20250927.htm) |
| Apple 8-K Q4 FY2025 results, EX-99.1 | 2025-10-30 | 0000320193-25-000077 | `AAPL_8K_2025-10-30_EX991.txt` |
| Alphabet 10-K FY2025 | 2026-02-05 | 0001652044-26-000018 | `GOOGL_10K_FY2025.txt` / `.flat.txt` (goog-20251231.htm) |
| Alphabet 8-K Q4 2025 results, EX-99.1 | 2026-02-04 | 0001652044-26-000012 | `GOOGL_8K_2026-02-04_EX991.txt` |
| Amazon 10-K FY2025 | 2026-02-06 | 0001018724-26-000004 | `AMZN_10K_FY2025.txt` / `.flat.txt` (amzn-20251231.htm) |
| Amazon 8-K Q4 2025 results, EX-99.1 | 2026-02-05 | 0001018724-26-000002 | `AMZN_8K_2026-02-05_EX991.txt` |
| YouTube Blog, "20 years & 125 million subscribers later…", Lyor Cohen, Mar 05, 2025 (rung 3, company website, not a filing) | 2025-03-05 | https://blog.youtube/inside-youtube/20-years-125-million-subscribers-lyor-cohen/ | `YT_blog_2025-03-05_125m.txt` |
| YouTube Blog, "$8 Billion: YouTube's twin engine continues to fuel the future of music", The YouTube Team, Oct 23, 2025 (rung 3) | 2025-10-23 | https://blog.youtube/news-and-events/8-billion-youtubes-twin-engine-continues-to-fuel-the-future-of-music/ | `YT_blog_8billion.txt` |

Prior runs `Test Runs\2026-09-06 Run - AAPL Apple.md`, `...GOOGL Alphabet.md` and their `_research` folders were grepped for "subscri": no hits in the `.md` research files; nothing reused from them.

### Summary table: what is disclosed about music streaming

| Company | Music revenue | Music subscribers | Music margin | Music pricing in filing | Nearest disclosed line (FY2025, US$ millions) |
|---|---|---|---|---|---|
| Apple | NOT DISCLOSED | NOT DISCLOSED (10-K and Q4 FY2025 release both searched) | NOT DISCLOSED | NOT IN FILING | Services net sales 109,158 (FY2024 96,169; FY2023 85,200); Services cost of sales 26,844; Services gross margin 82,314 = 75.4% (FY2024 73.9%; FY2023 70.8%) |
| Alphabet | NOT DISCLOSED | NOT IN 10-K; "over 325 million paid subscriptions across consumer services" in the Q4 2025 earnings release (all Google consumer subscriptions, not music); "125 million YouTube Music and Premium subscribers globally, including trials" on the YouTube Blog only | NOT DISCLOSED | NOT IN FILING | Google subscriptions, platforms, and devices 48,030 (FY2024 40,340; FY2023 34,688) |
| Amazon | NOT DISCLOSED | NOT DISCLOSED (10-K and Q4 2025 release both searched) | NOT DISCLOSED | NOT IN FILING (release gives Alexa+ price only) | Subscription services 49,619 (FY2024 44,374; FY2023 40,209); "Total video and music expense" 22.4 billion (FY2024 20.4 billion), video and music not split |

Pricing search: "per month", "a month", "monthly fee", "price increase" in all three 10-Ks: no music-pricing hit (Apple's only hit is a supply-chain "price increases" sentence). None of the three 10-Ks mentions Spotify.

### Apple: verbatim (10-K FY2025, 0000320193-25-000079)

Item 1, Services:
> "The Company also offers digital content through subscription-based services, including Apple Arcade ® , a game service; Apple Fitness+ ® , a personalized fitness service; Apple Music ® , which offers users a curated listening experience with on-demand radio stations; Apple News+ ® , a news and magazine service; and Apple TV ® , which offers exclusive original content and live sports."

> "The Company operates various platforms, including the App Store ® , that allow customers to discover and download applications and digital content, such as books, music, video, games and podcasts."

(The spaces around "®" are extraction artifacts of the stripped HTML; quoted as extracted.)

MD&A:
> "Services net sales increased during 2025 compared to 2024 primarily due to higher net sales from advertising, the App Store and cloud services."

> "Services gross margin percentage increased during 2025 compared to 2024 primarily due to a different mix of services, partially offset by higher costs."

Item 1A (content licensing):
> "The Company contracts with numerous third parties to offer their digital content to customers. This includes the right to sell, or offer subscriptions to, third-party content, as well as the right to incorporate specific content into the Company's own services. The licensing or other distribution arrangements for this content can be for relatively short time periods and do not guarantee the continuation or renewal of these arrangements on commercially reasonable terms, or at all. Some third-party content providers and distributors currently or in the future may offer competing products and services, and can take actions to make it difficult or impossible for the Company to license or otherwise distribute their content. Other content owners, providers or distributors may seek to limit the Company's access to, or increase the cost of, such content. The Company may be unable to continue to offer a wide variety of content at commercially reasonable prices with acceptable usage rules."

Segments are geographic ("The Company's reportable segments consist of the Americas, Europe, Greater China, Japan and Rest of Asia Pacific."); Services is a product category, not a segment. Q4 FY2025 release (EX-99.1) names Apple Music only in the boilerplate: "breakthrough services including the App Store, Apple Music, Apple Pay, iCloud, and Apple TV."

### Alphabet: verbatim (10-K FY2025, 0001652044-26-000018)

Item 7 / Note 2 description of the revenue line:
> "consumer subscriptions, which primarily include revenues from YouTube services, such as YouTube TV, YouTube Music and Premium, and NFL Sunday Ticket, as well as Google One, which offers access to our most capable Gemini models;"

> "Google subscriptions, platforms, and devices revenues increased $7.7 billion from 2024 to 2025. The growth was primarily driven by an increase in subscriptions revenues. This increase was primarily due to the contribution from growth in paid subscriptions across both YouTube services and Google One."

> "Fluctuations in our Google subscriptions, platforms, and devices revenues have been, and may continue to be, affected by factors in addition to the general factors described above, such as changes in customer usage and demand, number of subscribers, and the timing of product launches."

Content cost description (music not separated from video):
> "content acquisition costs, which are payments to content providers from whom we license video and other content for distribution, primarily related to YouTube (we pay fees to these content providers based on revenues generated, subscriber counts, or a flat fee);"

> "The increase in other cost of revenues from 2024 to 2025 was primarily due to increases in content acquisition costs, largely for YouTube, depreciation expense, and other technical infrastructure operations costs."

Q4 2025 earnings release (8-K EX-99.1, 0001652044-26-000012), CEO quotation, NOT in the 10-K (searched "325 million" in the 10-K: 0 hits):
> "YouTube's annual revenues surpassed $60 billion across ads and subscriptions; we now have over 325 million paid subscriptions across consumer services, led by strong adoption for Google One and YouTube Premium."

YouTube Blog (rung 3; not a filing; not referenced by the 10-K):
> "125 million subscribers: I'm thrilled to announce that with your partnership, we've reached 125 million YouTube Music and Premium subscribers globally, including trials – an incredible milestone that many laughed off as impossible when we first launched." (Lyor Cohen, Mar 05, 2025; `YT_blog_2025-03-05_125m.txt`)

> "In the 12 months between July 2024 and June 2025, YouTube paid out over $8 billion to the music industry." / "We have over 125 million Music and Premium subscribers globally (including trials) and over 2 billion logged-in viewers who watch music videos each month." (The YouTube Team, Oct 23, 2025; `YT_blog_8billion.txt`)

Note for the row: the YouTube figure bundles YouTube Music with YouTube Premium (ad-free video) and counts trials; Spotify's reported subscriber count is not on that basis. Not reconciled; recorded as stated.

### Amazon: verbatim (10-K FY2025, 0001018724-26-000004)

Note (disaggregated net sales), footnote (5) to "Subscription services":
> "(5) Includes annual and monthly fees associated with Amazon Prime memberships, as well as digital video, audiobook, digital music, e-book, and other non-AWS subscription services."

Revenue recognition note:
> "Subscription services - Our subscription sales include fees associated with Amazon Prime memberships and access to content including digital video, audiobooks, digital music, e-books, and other non-AWS subscription services."

Cost of sales:
> "Cost of sales primarily consists of the purchase price of consumer products, inbound and outbound shipping costs, including costs related to sortation and delivery centers and where we are the transportation service provider, and digital media content costs where we record revenue gross, including video and music."

Content note:
> "We obtain video content, inclusive of episodic television and movies, and music content for customers through licensing agreements that have a wide range of licensing provisions including both fixed and variable payment schedules."

> "The total capitalized costs of video, which is primarily released content, and music as of December 31, 2024 and 2025 were $ 19.6 billion and $ 21.3 billion. Total video and music expense was $ 20.4 billion and $ 22.4 billion for the year ended December 31, 2024 and 2025. Total video and music expense includes licensing and production costs associated with content offered within Amazon Prime memberships, and costs associated with digital subscriptions and sold or rented content."

Item 1 (Amazon Music not named): "In addition, we offer subscription services such as Amazon Prime, a membership program that includes fast, free shipping on tens of millions of items, access to award-winning movies and series, live sports, and other benefits."

### Cross-reference from the other side (already on disk, not re-derived)

Sirius XM's FY2025 10-K (Peer 2 above) names Apple, Google, Amazon and YouTube as the providers of Pandora's competition "as a small part of a larger business". WMG's 10-Ks (Label side below) name the three plus Spotify as >10% customers or price-raisers.

### Big tech: not disclosed

- Apple Music: revenue, subscribers, margin, content cost, price. NOT DISCLOSED in 10-K or results release.
- YouTube Music: revenue, margin, content cost split between music and video. NOT DISCLOSED. Subscriber count appears only on the YouTube Blog (bundled with Premium, incl. trials); the release gives an all-consumer-subscriptions count.
- Amazon Music (Unlimited or Prime-included): revenue, subscribers, margin, price. NOT DISCLOSED; music expense is combined with video.

---
## PEER 4: THE LABEL SIDE (SUPPLIERS) - WMG, UMG, SONY

### Documents

| Doc | Filed / dated | Accession or URL | Local file |
|---|---|---|---|
| WMG 10-K FY2025 (FYE 2025-09-30) | 2025-11-20 | 0001319161-25-000034 | `WMG_10K_FY2025.txt` (copied from `..\..\_research 2026-09-13 SONY\peers_music\`) |
| WMG 10-K FY2024 | 2024-11-21 | 0001319161-24-000039 | `WMG_10K_FY2024.txt` (copied, same source) |
| WMG 10-K FY2023 | 2023-11-21 | 0001319161-23-000036 | `WMG_10K_FY2023.txt` (copied, same source) |
| WMG 10-K FY2022 | 2022-11-22 | 0001319161-22-000035 | `WMG_10K_FY2022.txt` (fetched 2026-09-13, wmg-20220930.htm) |
| WMG 10-K FY2021 | 2021-11-23 | 0001319161-21-000036 | `WMG_10K_FY2021.txt` (fetched 2026-09-13, wmg-20210930.htm) |
| UMG Annual Report 2025 | 2026 (publication date per SONY peers file) | https://assets.ctfassets.net/e66ejtqbaazg/7HObJrt5UDQfjjfKYN454B/201bf057190c5ed4ee185b04a34ec095/UMG_2025_Annual_Report.pdf | `..\..\_research 2026-09-13 SONY\peers_music\UMG_AR_2025.cols.txt` (not copied; read in place) |
| UMG Annual Report 2024 | 2025 | https://downloads.ctfassets.net/e66ejtqbaazg/3lVdyJmpf8DQTPMRcxChSQ/80752d027f61e3846f4b5e2a5a62a958/UMG_2024_Annual_Report.pdf | `..\..\_research 2026-09-13 SONY\peers_music\UMG_AR_2024.cols.txt` |
| Sony Group 20-F FY ended 2026-03-31 | 2026-06-18 | 0001193125-26-274893 (d28719d20f.htm) | `..\..\_research 2026-09-13 SONY\20F_FY2026.txt` |

**UMG evidence rung: 3.** UMG is not an SEC registrant (EDGAR holds only an ADR shell, CIK 0001890126, F-6EF filings, per the SONY peers file). Its annual reports are cited as company IR documents, English, from the files named above. Page numbers below are the PRINTED page footers ("Annual Report 2025 | NN") located by `scratchpad/foot.py`; the `.cols.txt` layout extraction interleaves columns in places, so only passages that read continuously were quoted.

### Figures: customer concentration (as filed)

WMG, share of total revenues (10-K customer-concentration note, each year):

| Customer | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Spotify | 18% | 17% | 18% ("Spotify AB") | 18% ("Spotify AB") | 20% ("Spotify AB") |
| YouTube | 11% | 12% | 12% | 12% | 12% |
| Apple | 13% | 11% | 11% | 11% | 11% |
| Top three digital accounts, % of total revenue (Item 1A) | ~42% | ~40% | ~41% | ~41% | ~43% |
| Top three digital accounts, % of Recorded Music revenue (Item 1) | ~45% | ~43% | ~41% | ~41% | ~45% |
| WMG total revenues (US$ millions, geographic note) | 5,301 | 5,919 | 6,037 | 6,426 | 6,707 |
| Recorded Music revenue from streaming services (US$ millions, MD&A) | 2,972 | 3,159 | 3,223 | 3,444 | 3,505 |

Spotify AB share of WMG accounts receivable (FY2025 10-K, credit-risk note): 20% at 2025-09-30, 18% at 2024-09-30.

UMG (unnamed customers), share of total revenues: 2023: 19%, 11%, 10%; 2024: 20%, 11%, 10%; 2025: 20%, 11%, 11% (AR 2024 p.202; AR 2025 p.213). UMG does NOT name the three customers. Top 50 music services: 98% (2024) and 97% (2025) of recorded music digital revenue (AR 2025 p.93).

COMPUTED, not filed (arithmetic on rounded filed percentages; error band roughly +/-0.5 percentage point of revenue, i.e. about +/-US$30 million): WMG revenue from Spotify = Spotify % x total revenues: FY2021 ~954; FY2022 ~1,006; FY2023 ~1,087; FY2024 ~1,157; FY2025 ~1,341 (US$ millions).

### WMG: verbatim

Customer concentration (FY2025 10-K, Note "Customer Concentration"):
> "In the fiscal year ended September 30, 2025, the Company had three customers, Spotify, YouTube and Apple, that individually represented 10% or more of total revenues, whereby Spotify AB represented 20%, YouTube represented 12% and Apple represented 11% of total revenues."

> "These customers’ revenues are included in both the Company’s Recorded Music and Music Publishing segments and the Company expects that the Company’s license agreements with these customers will be renewed in the normal course of business."

FY2021 10-K, same note:
> "In the fiscal year ended September 30, 2021, the Company had three customers, Spotify, Apple and YouTube, that individually represented 10% or more of total revenues, whereby Spotify represented 18 %, Apple represented 13 % and YouTube represented 11 % of total revenues. In the fiscal year ended September 30, 2020, the Company had two customers, Spotify and Apple, that individually represented 10% or more of total revenues, whereby Spotify represented 17 % and Apple represented 14 % of total revenues."

FY2022 10-K: "In the fiscal year ended September 30, 2022, the Company had three customers, Spotify, YouTube and Apple, that individually represented 10% or more of total revenues, whereby Spotify represented 17 %, YouTube represented 12 % and Apple represented 11 % of total revenues."

(The spaces before "%" in FY2021-FY2022 are extraction artifacts; quoted as extracted.)

Accounts receivable (FY2025 10-K):
> "As of September 30, 2025 and September 30, 2024, Spotify AB represented 20% and 18%, respectively, of the Company’s accounts receivable balance. No other single customer accounted for more than 10% of accounts receivable in either period."

Who sets price / wholesale (FY2025 10-K, Item 1A; heading and body):
> "We are substantially dependent on a limited number of digital music services for the online distribution and marketing of our music, and they are able to significantly influence the pricing structure for online music stores and may not correctly calculate royalties under license agreements."

> "We derive an increasing portion of our revenue from the licensing of music through digital distribution channels. We are currently dependent on a small number of leading digital music services. In fiscal year 2025, revenue earned under our license agreements with our top three digital music accounts, Spotify, Google/YouTube and Apple, accounted for approximately 43% of our total revenue. We have limited ability to increase our wholesale prices to digital music services as a small number of digital music services control much of the legitimate digital music business. If these services were to adopt a lower pricing model or if there were structural changes to other pricing models, we could receive substantially less for our music, which could cause a material reduction in our revenue, unless offset by a corresponding increase in the number of subscribers or transactions."

> "We currently enter into short-term license agreements with many digital music services and provide our music on an at-will basis to others. There can be no assurance that we will be able to renew or enter into new license agreements with any digital music service. The terms of these license agreements, including the royalties that we receive pursuant to them, may change as a result of changes in our bargaining power, changes in the industry, changes in the law or for other reasons."

The same "limited ability to increase our wholesale prices" sentence appears in all five 10-Ks FY2021-FY2025 (FY2021: "approximately 42% of our total revenue", top three named "Spotify, Apple and YouTube"; FY2022: "approximately 40%"; FY2023 and FY2024: "approximately 41%", named "Spotify, Google/YouTube and Apple").

Fees vary by service; contract length (FY2025 10-K, Item 1):
> "We enter into agreements with digital music services to make our music available for access in digital formats (e.g., streaming and downloads). We then provide digital assets for our music to these services in an accessible form. Our agreements with these services establish our fees for the distribution of our music, which vary based on the service. We typically receive accounting from these services on a monthly basis, detailing the distribution activity, with payments generally rendered on a monthly basis. Our agreements with digital music services generally last one to three years. In fiscal year 2025, Recorded Music revenue earned under our agreements with our top three digital music accounts, Spotify, YouTube and Apple, accounted for approximately 45% of our Recorded Music revenues."

Same catalogue to many services (FY2025 10-K, Item 1):
> "In connection with the digital distribution of our music, we currently partner with a broad range of digital music services, such as Amazon, Apple, Deezer, KKBox, Spotify, Tencent Music Entertainment Group and YouTube, and are actively seeking to develop and grow our digital business."

> "distributed in digital form to an expanded universe of digital partners, including streaming services such as those of Amazon, Apple, Deezer, SoundCloud, Spotify, Tencent Music and YouTube, radio services such as iHeart Radio and SiriusXM and other download services."

No WMG 10-K read states in terms that the identical catalogue is licensed to every service or that no service has exclusivity; the passages above list the partners only. "exclusiv" hits in the FY2025 10-K concern artist and songwriter contracts and the Delaware forum clause, not DSP licences.

Price increases by DSPs (FY2021 and FY2022; FY2023-FY2025 are quoted in the SONY peers file `..\..\_research 2026-09-13 SONY\peers_music.md`, verified there):
> "In addition to paid subscriber growth, we believe that, over time, streaming revenues will increase due to pricing increases as the broader market further develops. Streaming services are already at the early stages of experimenting with price increases. For example, in 2020 Spotify increased monthly prices for its services in Australia and several European and South American markets, and in 2021 Spotify increased prices in the U.S., the U.K. and other European markets. Spotify has reported positive early results, having seen no meaningful impacts to churn or customer intake in these markets. We believe the value proposition that streaming provides to consumers supports premium product initiatives." (FY2021 10-K, Item 1)

> "For example, in 2021 Spotify increased prices in the United States, the UK and other European markets. Spotify has reported positive early results, having seen no meaningful impacts to churn or customer intake in these markets. In 2022, Apple Music increased prices of its student plans in the United States, the UK and Canada, and Amazon Music Unlimited increased the prices of both its individual and family subscription plans." (FY2022 10-K, Item 1)

> "For example, in 2025, Spotify increased the price of its premium individual tier in multiple markets across South Asia, the Middle East, Africa, Europe, Latin America, and the Asia-Pacific region. In 2025, YouTube increased the prices of its individual and family plan tiers on both YouTube Premium and YouTube Music in Europe. In 2024, Amazon Music Unlimited increased the prices of both its individual and family subscription plans in the United States, Canada and the United Kingdom." (FY2025 10-K, Item 1)

> "Align Contractual Terms with the Music Industry’s Growth. The music industry is increasingly focused on price increases as a driver of growth to complement the sustained growth in global subscribers that has fueled the industry for over a decade. We continue to see progress in aligning our contracts with streaming services with this new paradigm, with a focus on economic certainty. Our collaboration with many of the largest tech companies in the world, including Google, Apple, Amazon, and Spotify, provides more opportunities for innovation, along with greater certainty around our economic participation as product offerings evolve." (FY2025 10-K, Item 1)

AI (FY2025 10-K, Item 1):
> "As a proactive measure, WMG and other major music rightsholders are collaborating with technology platforms, such as Spotify, to establish a responsible, artist-first framework for AI development."

Searched and NOT found in WMG 10-Ks FY2021-FY2025: "Streaming 2.0" (0 hits), "artist-centric" (0 hits). "DSP" appears only in the FY2025 10-K, as a defined term for true-up payments: "$4 million of incremental Recorded Music streaming revenue recognized from a Digital Service Provider (“DSP”) for performance obligations satisfied in previous periods (the “DSP True-Up Payments”)". WMG does not state its share of DSP revenue (the label royalty rate) in any 10-K read.

### UMG: verbatim (rung 3)

Customer concentration (AR 2025 p.213, Note on revenues):
> "In 2025, UMG had 3 customers that each individually represented over 10% of total revenues (3 customers in 2024) and which represented total revenues of 20%, 11% and 11% respectively (20%, 11% and 10% in 2024). Each customer reports revenues in both Recorded Music and Music Publishing segments."

(Extraction line breaks removed; words unchanged.)

AR 2024 p.202: "In 2024, UMG had 3 customers that each individually represented over 10% of total revenues (3 customers in 2023) and which represented total revenues of 20%, 11% and 10% respectively (19%, 11% and 10% in 2023)."

Spotify named as the largest DSP (AR 2025 p.4, CEO letter):
> "For example, on Spotify, the largest digital service provider (DSP), we had four of the top five artists globally in 2025, as well as six of the top ten albums and six of the top 10 songs."

DSP dependency (AR 2025 p.93, risk section):
> "UMG derives an increasing portion of its revenue from the licensing and distribution of music through digital distribution channels and partners with several hundred music services around the world. For the year ended December 31, 2025, the top 50 music services accounted for 97% of UMG’s recorded music digital revenue, as compared to 98% for the year ended December 31, 2024."

Same content to all DSPs (AR 2025 p.94, risk response):
> "While a number of digital service providers compete with each other in the music industry around the world, they all seek to work closely with UMG, the largest supplier of content to all of the digital service providers. This is because UMG’s artist content is a key driver of customer acquisition and retention for all of these platforms."

> "For example, we have partnerships that enable UMG’s content to be distributed by global, regional and local DSPs, including Spotify, Apple, YouTube, Amazon, Deezer, Tencent Music Entertainment and NetEase, among an increasingly important number of other partners."

AR 2025 p.101 (risk response, macro):
> "Furthermore, music consumption is relatively inexpensive compared to other forms of media entertainment, and DSP providers generally make all content available, thus not requiring multiple subscriptions."

Streaming 2.0 (AR 2025 p.5, CEO letter):
> "I’m particularly proud of our continued progress in reaching “Streaming 2.0” agreements with our DSP partners. These agreements encourage smarter customer segmentation, create greater consumer value and drive ARPU growth. In late 2024 and in 2025 we implemented Streaming 2.0 deals with Amazon, Spotify and YouTube, and we expect to enter into more such agreements in 2026."

Artist-Centric adoption (AR 2025 p.41):
> "We began in 2023 with several streaming DSPs’ adopting and exploring Artist-Centric principles. The engagement here included Deezer and Spotify, as well as Tidal and SoundCloud, as platforms"

(The sentence continues on the next page after a page break; quoted to the break.)

Price increases (AR 2024):
> "Subscription revenue saw growth of 8.2% year-over year, or 9.1% in constant currency, driven by the growth in global subscribers as well as impact of price increases at certain platforms." (p.30)

> "Subscription revenues grew by 8.2% or 9.1% in constant currency driven by the growth in global subscribers as well as the impact of price increases at certain platforms." (p.53, Financial Review; wording differs from p.30 by "the")

AR 2025 does not contain the string "price increase" (0 hits); the SONY peers file records the FY2025 subscription driver as "largely driven by the growth in global subscribers" (AR 2025 p.30).

UMG holds Spotify shares (AR 2025 p.57, Financial Review):
> "As of December 31, 2025, UMG held a portfolio of listed non-controlling equity interests (including Spotify) with an aggregate market value of approximately €3,404 million (before taxes), compared to €2,945 million as of December 31, 2024. The increase in market value during 2025 was due to the fluctuation in share price of our listed investments most notably of Spotify."

UMG does not state the size of its Spotify stake separately, nor its royalty share of DSP revenue, in the passages read. "wholesale" hits in AR 2025 concern physical wholesalers, mechanical royalties on physical products, and the Anthropic lyrics suit, not DSP pricing.

### Sony: verbatim (20-F FY ended 2026-03-31, 0001193125-26-274893)

Sony names no DSP customer and gives no customer-concentration percentage for Music in the passages read (string counts in `20F_FY2026.txt`: "Apple" 0, "YouTube" 0, "Tencent" 0; "Spotify" 10, all about the shareholding).

Sony holds Spotify shares, and the gain is linked to artist payments:
> "Shares of Spotify Technology S.A. (“Spotify”) held by Sony are classified as equity securities required to be measured at fair value through profit or loss. The revaluation of the Spotify shares, which reflects costs to be paid to Sony’s artists and distributed labels as well as the changes in the fair value of derivatives utilized to hedge exposure to market fluctuation risk, owned as of March 31, 2024, 2025 and 2026 resulted in an unrealized gain of 64,764 million yen (440 million U.S. dollars), 69,019 million yen (443 million U.S. dollars) and 9,919 million yen (74 million U.S. dollars), respectively."

How DSP contracts are recognized (right to remove content; minimum guarantees):
> "Digital revenues include revenues from contracts with digital streaming services typically recognized as a single performance obligation, which is ongoing access to intellectual property in an evolving library of content over the contract term, predicated on: (1) the business practice and contractual ability to remove specific content without a requirement to replace the content and without impact to minimum royalty guarantees and (2) the contracts not containing a specific listing of content subject to the license. For these contracts, revenues are recognized based on sales and usage royalties, except where there is a minimum royalty guarantee that is not expected to be recouped, or a fixed fee, which is recognized on a straight-line basis over the term of the contract."

(A page footer "F-2 6 / Table of Contents / SONY GROUP CORPORATION AND CONSOLIDATED SUBSIDIARIES" interrupts the last sentence between "guarantee that" and "is not expected" in the extracted text.)

MD&A driver, Music segment: "(+) Higher revenues from streaming services in Recorded Music and Music Publishing".

### Label side: not disclosed

- The labels' contractual share of DSP subscription revenue (royalty rate): NOT DISCLOSED by WMG, UMG or Sony in any document read. The only numeric rate formulas in this folder are (a) Pandora's US mechanical (publishing) rate under Section 115, quoted in Peer 2, and (b) Deezer's description of label payments as "market share" times a percentage of revenue, with the percentage not given (Peer 5).
- The pass-through share of any DSP consumer price increase to label revenue: NOT DISCLOSED (also recorded as NOT OBTAINED in the SONY peers file).
- UMG's three >10% customers are not named; the identity of UMG's largest customer as Spotify is NOT stated in the note (the CEO letter calls Spotify "the largest digital service provider (DSP)", which is a statement about DSP size, not UMG's customer ranking).
- Sony's Music customer concentration: NOT DISCLOSED in the 20-F passages read.
- An explicit statement that each label licenses its full catalogue non-exclusively to every DSP: NOT FOUND in WMG or Sony filings; UMG says "DSP providers generally make all content available" (p.101). TME states its own label licences are "on a non-exclusive basis" (Peer 1).

---
## PEER 5: DEEZER S.A. (Euronext Paris: DEEZR; IFRS; euros)

**Evidence rung: 3** (company IR site, English free translation). Deezer is not an SEC registrant. The Universal Registration Documents (URD) are filed with the AMF in French/XHTML; the English PDFs say of themselves: "This version of the Universal Registration Document in PDF format is a free translation of the official French version of the Universal Registration Document in XHTML format, which is available on the website of the Autorité des marchés financiers, as well as on the Company’s website." (URD 2022, pdf p.3). The French AMF originals were NOT fetched.

Fetchable on the first attempt from `https://www.deezer-investors.com/fin/` (probe `dz.py`, download and PyMuPDF extraction `deezer/dl.py`, 2026-09-13):

| Doc | Dated | URL | Local file |
|---|---|---|---|
| 2025 URD (EN), carries 2024 comparatives | filed with AMF 2026-04-29 (file name "26_04_29"; search-result release, not verified in the PDF) | https://www.deezer-investors.com/wp-content/uploads/2026/04/DZR2025_URD_EN_PDF_MEL_26_04_29.pdf | `deezer/DZR_URD_2025_EN.pdf`, `.txt` (268 pdf pages) |
| 2023 URD (EN), carries 2022 comparatives | 2024-04-30 (file name) | https://www.deezer-investors.com/wp-content/uploads/2024/04/DZR2023_DEEZER_URD_EN_2024_04_30pdf.pdf | `deezer/DZR_URD_2023_EN.pdf`, `.txt` (256 pdf pages) |
| 2022 URD (EN), carries 2021 comparatives | 2023-04-28 (file name "230428") | https://www.deezer-investors.com/wp-content/uploads/2023/04/DZR2022_DEEZER_URD_EN_MEL_230428.pdf | `deezer/DZR_URD_2022_EN.pdf`, `.txt` (274 pdf pages) |

The 2024 URD is linked on the IR page only as a French file (`Document-denregistrement-universel-2024-PDF.pdf`); not fetched. FY2024 figures come from the 2025 URD comparative column. Page references below are PDF page numbers of the extracted text (printed page numbers are about two lower).

### Figures, as reported (Section 5.1 "Key figures" / "Simplified income statement" of each URD)

| Line | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Source |
|---|---|---|---|---|---|---|
| Total subscribers (Dec 31, millions) | 9.6 | 9.4 | 10.5 | 9.7 | 9.1 | URD 2022 p.139; URD 2023 p.128; URD 2025 p.141 |
| Direct (B2C in URD 2022) subscribers | 5.7 | 5.6 | 5.6 | 5.3 | 5.7 | same |
| Partnerships (B2B in URD 2022) subscribers | 4.0 | 3.8 | 4.8 | 4.4 | 3.4 | same |
| Monthly ARPU, Direct / B2C (€) | 4.1 | 4.7 | 4.9 | 5.5 | 5.4 | same |
| Monthly ARPU, Partnerships / B2B (€) | 2.3 | 2.6 | 2.8 | 2.9 | 3.2 | same |
| Group ARPU (€) | 3.5 | 4.0 | n/c | 4.3 | 4.5 | URD 2022 p.139; URD 2025 p.143 |
| Total revenue (€ millions) | 400.0 | 451.2 | 484.7 | 541.7 | 534.0 | URD 2022 p.139; URD 2023 p.128; URD 2025 p.140 |
| Direct revenue | 282.7 (B2C) | 317.2 | 331.1 | 344.4 | 351.9 | same |
| Partnerships revenue | 107.4 (B2B) | 118.5 | 135.7 | 168.3 | 147.8 | same |
| Other revenue | 9.9 | 15.5 | 17.8 | 29.0 | 34.2 | same |
| Gross profit (IFRS) | 48.5 | 65.1 | 91.4 | 123.6 | 145.2 | URD 2022 p.141; URD 2023 p.130; URD 2025 p.144, p.146 |
| Adjusted gross profit (non-IFRS) | 84.1 | 98.0 | 110.3 | 133.7 | 135.5 | URD 2022 p.139; URD 2023 p.128; URD 2025 p.142 |
| Adjusted gross margin (as reported) | 21.0% | 21.7% | 22.7% | 24.7% | 25.4% | same |
| Cost of Revenue (IFRS) | n/c | n/c | n/c | 418.1 | 388.7 | URD 2025 p.143 |
| Operating income / loss (EBIT) | (120.6) | (166.7) | (64.4) | (27.5) | 9.3 | URD 2022 p.139; URD 2023 p.128; URD 2025 p.142 |

n/c = not collected. COMPUTED (arithmetic, not a filed ratio): IFRS gross profit / revenue: 12.1% (2021), 14.4% (2022), 18.9% (2023), 22.8% (2024), 27.2% (2025).

Flags:
- Segment names changed: URD 2022 uses "B2C" / "B2B" ("Direct – B2C", "Indirect – B2B"); URD 2023 onward "Direct" / "Partnerships". Figures for 2022 agree across the two URDs (5.6 / 3.8 / 9.4; revenue 317.2 / 118.5 / 15.5).
- Direct ARPU steps from €4.9 (2023, URD 2023) to €5.5 (2024, URD 2025). The 2024 URD that would show 2023 on the later basis was not fetched (French only); no restatement note was found in URD 2025 (searched "restated", "methodolog", ARPU definition). NOT reconciled.
- URD 2023 p.130 text reads: "Gross profit amounted to €91.4 million in 2023 compared to €65.1 million in 2022, representing a decrease of €26.3 million, or 40.4%." The figures show an increase; the word "decrease" is as printed in the English PDF. Quoted as extracted, not corrected.
- "Adjusted gross profit" excludes licence-agreement non-recurring items; URD 2025 p.146: "Adjusted gross profit corresponds to the gross profit (revenue less Cost of Revenue) excluding non‑recurring expenses related to license agreements such as costs relating to equity warrants and unused minimum guarantees."

### Deezer: verbatim

How labels are paid (URD 2025, pdf p.19-20, "Content licensing"):
> "Deezer typically pays record labels an amount equal to the label’s “market share” of certain content streamed on Deezer’s platform multiplied by a percentage of all subscription revenue received. For its free advertising‑based service, Deezer typically pays to record labels an amount equal to the label’s “market share” multiplied by a percentage of all advertising revenue received."

> "Under these arrangements, the “market share” is the percentage represented by the streams of a certain provider’s repertoire, calculated per month, per country and per offer."

> "As a key component of Deezer’s service offering, the Company has historically maintained contractual arrangements with the four recording providers it considers to be the most listened‑to content on Deezer’s platform (including the three major record labels – Universal Music Group, Sony Music Entertainment and Warner Music Group – as well as Merlin which licenses the rights of a group of independent record labels and distributors)."

(The percentage of revenue is not disclosed. Extracted text carries soft-hyphen and line-break artifacts, e.g. "most listened‑to"; words unchanged.)

Catalogue (URD 2025, pdf p.15):
> "The Company provides access to a full‑range catalog of high‑quality music, from essentially all labels, distributors and aggregators across the world."

Minimum guarantees (URD 2025, pdf p.40, risk factors):
> "In addition, the Group is currently subject to minimum guaranteed payment requirements (irrespective of the actual listening figures of subscribers and users) with certain rights holders and expects to continue to be so in the future, applicable either generally, in specific geographic markets or to specific offers through distribution partners."

Pricing (URD 2025, pdf p.28):
> "Deezer has been reviewing its pricing strategy and was the first major music streaming platform to raise prices globally. This move resulted in minimal subscription cancellations. Since then, all other major global platforms have followed this strategic move."

> "In 2025, with no further price increases implemented and a strategic focus on Family plan penetration, Direct ARPU decreased by (2.0)% year‑over‑year, reflecting the commercial success of Family subscriptions which, while dilutive on a per‑account basis, significantly boost household penetration, lifetime value, and retention."

Competitors named, with third-party share figures (URD 2025, pdf p.23 and p.24):
> "Deezer is the second largest player in France with a solid 27.8% market share of music streaming subscribers as of December 31, 2024, with competitors capturing the following: Spotify 40.9%, Apple Music 13.7%, Amazon Music 10.1%, YouTube Music 6.6%, and Other 1.0% (source: MIDiA Music subscriber market shares Q4 2024)."

> "Deezer competes for the time and attention of its users across different forms of media, including traditional broadcast, terrestrial, satellite, and Internet radio, other providers of on‑demand audio streaming services (e.g. Spotify, Amazon Music, Apple Music, YouTube Music, SoundCloud, Tidal), and other providers of in‑home and mobile entertainment such as cable television, video streaming services, social media and networking websites. Deezer competes to attract, engage, and retain users with other content providers based on a number of factors, including price, quality of user experience, features, content, perceptions of advertising load on its ad‑supported free service, brand awareness, and reputation."

Risk factor (URD 2025, pdf p.36):
> "other providers of audio streaming services, such as its principal competitors, Spotify, Amazon Music, Apple Music, YouTube Music, SoundCloud, Tidal, which all offer content and subscription offerings similar to the Group’s;"

Self-description versus conglomerates (URD 2023, pdf p.6; infographic page, the extraction scatters the layout, so the "#2" label and the words "Independent music platform globally *" are separated by other figures in the text) with footnote "Based on the latest numbers of subscribers published by MIDiA (as September 30, 2023); excludes non-independant players part of conglomerates (Apple Music, Amazon Music, YouTube Music, Tencent Music, NetEase Music and Yandex)." ("non-independant" as printed.)

Artist-centric model with UMG (URD 2025, pdf p.20):
> "Deezer, in partnership with Universal Music Group, introduced a groundbreaking evolution to the artist remuneration mechanism, marking the first substantial update in music streaming’s history."

> "As of December 31, 2025, around 89% of platform streams operate within this innovative framework."

Label licence charges (URD 2025, pdf p.144):
> "This change reflected the decrease in non‑recurring charges related to the licensing agreements signed with music labels between the end of 2020 and the beginning of 2021 as these contracts ended in H1 2024 and the reversal of legacy liabilities."

Evidence class of the MIDiA shares: Deezer quoting a third-party research firm inside its URD; the underlying measurement is not Deezer's.

### Deezer: not disclosed

- Royalty rate (the "percentage of all subscription revenue" paid to labels): NOT DISCLOSED.
- Content / royalty cost as a separate line: NOT DISCLOSED in the key-figures pages read (Cost of Revenue "mainly includes costs related to licensing rights, costs related to hosting infrastructure servers, network bandwidth costs and commissions charged by sales platforms and payment service providers", URD 2025 p.143).
- Monthly active users of the free tier: not collected.

---
## LIMITS AND DEFECTS

**What could not be obtained, and why**

1. **Label royalty rate / label share of DSP revenue.** Not disclosed by any label (WMG, UMG, Sony) or any DSP (TME, Pandora, Deezer, Apple, Alphabet, Amazon) in the documents read. The nearest numbers: Pandora's statutory US mechanical (publishing) formula, "the greater of 15.1% of revenues or 26.2% of record label payments" rising to 15.35% by 2027 (SIRI FY2025 10-K), which implies nothing about the sound-recording rate without the label payment figure; and Deezer's "market share" times "a percentage of all subscription revenue", with the percentage withheld.
2. **Music-only figures for Apple Music, YouTube Music, Amazon Music.** Revenue, margin, content cost and subscriber counts are not in the FY2025 10-Ks or the Q4 results releases. The only YouTube Music count found (125 million "YouTube Music and Premium subscribers globally, including trials") is on the YouTube Blog, rung 3, bundled with YouTube Premium and including trials. Apple and Amazon publish no music subscriber figure in any document read. The search for press figures was limited to the SEC results exhibits and the YouTube Blog; no Apple or Amazon newsroom or earnings-call transcript was fetched.
3. **TME royalty cost and online-music margin.** TME reports one segment; royalties sit inside "service costs" together with live-streaming revenue sharing and bandwidth. Consolidated gross margin is not a music gross margin; the social-entertainment share of revenue fell from 63.3% (2021) to 18.8% (2025), so the consolidated line mixes two businesses whose weights moved.
4. **Pandora music royalties alone.** "Revenue share and royalties" includes podcast revenue share and payments to third-party publishers on off-platform ad sales; on-platform vs off-platform ad revenue is not split. The computed "royalties / revenue" ratio (55-61%) is therefore not a music-royalty ratio.
5. **UMG customer identities.** UMG's three >10% customers are unnamed. WMG names Spotify, YouTube and Apple.
6. **Sony customer concentration.** Not found in the FY ended 2026-03-31 20-F passages searched ("Apple", "YouTube", "Tencent": 0 hits).
7. **Deezer 2024 URD in English.** Linked on the IR page only as a French PDF; not fetched. FY2024 figures come from the 2025 URD comparative column. The French AMF (XHTML) originals of all URDs were not fetched; the English PDFs are self-described free translations.
8. **WMG FY2019-FY2020 customer concentration.** Visible as comparatives in the FY2021 10-K note but not tabulated here (outside the window).

**Defects found in the sources (recorded, not corrected)**

- TME MAU series restated from Q1 2023 (IoT devices added): FY2022 MAU 588 as filed vs 620 restated; paying ratio 14.3% vs 13.6%.
- TME's 20-F says Spotify issued 8,552,440 shares to TME Hong Kong (2017); Spotify's FY2025 20-F lists 4,276,200 held of record by TME Hong Kong. Not reconciled.
- TME companyfacts carries only one dei fact for the FY2025 20-F; the XBRL cross-check was run on FY2024 (Revenue 28,401 and GrossProfit 12,025 RMB millions, MATCH).
- SIRI FY2023 Pandora self-pay subscribers: 6,008 (FY2023 10-K) vs 6,053 (FY2024 10-K, including 45 Cloud Cover). SIRI FY2025 Pandora cost of services: 1,475 (MD&A table) vs 1,471 (segment note, excluding share-based payment).
- SIRI's post-merger FY2025 10-K recasts the 2023 SiriusXM segment; the Pandora column is unchanged.
- Deezer URD 2023 p.130 calls a €26.3 million rise in gross profit a "decrease". Deezer Direct ARPU steps from €4.9 (2023, URD 2023) to €5.5 (2024, URD 2025) with no restatement note found.
- WMG FY2021-FY2022 texts carry "18 %" spacing artifacts; UMG `.cols.txt` column extraction interleaves text in places (only continuous passages quoted); edgar.py `strip_html` straightens curly quotes (the curly marks in TME definitions were restored by hand and are not character-verified).
- Three blockquotes contain page-footer interruptions in the source text (SIRI FY2025 Item 1A; Sony 20-F revenue-recognition note; UMG AR 2025 p.41 sentence cut at the page break). Each is flagged at the quote.

**Evidence classes used**

- Rung 1 (SEC filings): TME 20-Fs, SIRI 10-Ks, Apple/Alphabet/Amazon 10-Ks and 8-K EX-99.1, WMG 10-Ks, Sony 20-F, Spotify 20-F.
- Rung 3 (company websites, not regulator filings): UMG annual reports, Deezer URDs (English translations), YouTube Blog.
- Third-party figures quoted inside filings, labelled at the quote: Music & Copyright (via WMG, in the SONY peers file), MIDiA (via Deezer), Luminate and Goldman Sachs (via WMG FY2025 10-K, not transcribed).

**Computations in this file** (arithmetic only, labelled COMPUTED at each table): SIRI Pandora ratios (`calc_siri.py`), TME subscription/online-music shares (`calc_siri.py`, printed, not tabulated), WMG revenue from Spotify from rounded percentages, Deezer IFRS gross margin. None is a filed figure; none is a verdict.

**Scope kept:** no moat conclusion, no ranking, no substitute or non-substitute call. No file outside `Test Runs\_research 2026-09-13 SPOT\peers\` was edited; files in `_research 2026-09-13 SONY` were read and three WMG texts copied, not modified.


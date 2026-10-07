# SONY run: Music competitor row, PEERS (WMG, UMG, RSVR context)
Built 2026-09-13 by a subagent. Evidence gathering only; no moat verdict is reached here.
Status: COMPLETE 2026-09-13. Sections: WMG (rung 1), UMG (rung 3), RSVR (context, rung 1), not obtained, brief defects.
Scripts, text copies and PDFs: `peers_music/`. Quote check: `peers_music/verify2.py` (every blockquote searched in the source text; the only misses were column-extraction artifacts, checked by hand).

---
## PEER 1: WARNER MUSIC GROUP CORP. (CIK 0001319161, fiscal year ends September 30)

Documents read (rung 1, SEC primary filings, fetched 2026-09-13 with SEC User-Agent; text copies in `peers_music/`):

| Doc | Filed | Accession | File |
|---|---|---|---|
| 10-K FY2025 (FYE 2025-09-30) | 2025-11-20 | 0001319161-25-000034 | wmg-20250930.htm -> `WMG_10K_FY2025.txt` |
| 10-K FY2024 (FYE 2024-09-30) | 2024-11-21 | 0001319161-24-000039 | wmg-20240930.htm -> `WMG_10K_FY2024.txt` |
| 10-K FY2023 (FYE 2023-09-30) | 2023-11-21 | 0001319161-23-000036 | wmg-20230930.htm -> `WMG_10K_FY2023.txt` |

**Cross-check (operator rule 4):** XBRL companyfacts in accession 0001319161-25-000034 give
RevenueFromContractWithCustomerExcludingAssessedTax 6,707,000,000 (FY2025), OperatingIncomeLoss
694,000,000 (FY2025) and PaymentsToAcquirePropertyPlantAndEquipment 139,000,000 (FY2025). All three
match the filed statements read below. XBRL used for the cross-check only.

### Table: WMG, US$ millions, as filed

| Line | FY2023 | FY2024 | FY2025 | Source |
|---|---|---|---|---|
| Total revenues | 6,037 | 6,426 | 6,707 | FY2025 10-K Note 17 segment table |
| Recorded Music revenue | 4,955 | 5,223 | 5,408 | same |
| Music Publishing revenue | 1,088 | 1,210 | 1,306 | same |
| Recorded Music operating income | 875 | 916 | 850 | same |
| Music Publishing operating income | 200 | 238 | 224 | same |
| Corporate and eliminations operating loss | (285) | (331) | (380) | same |
| Total operating income | 790 | 823 | 694 | same |
| Recorded Music Adjusted OIBDA | 1,094 (MD&A) / 1,093 (note) | 1,282 | 1,269 | FY2024 10-K MD&A and Note 18; FY2025 10-K MD&A |
| Music Publishing Adjusted OIBDA | 296 | 330 | 361 | same |
| Total Adjusted OIBDA | 1,235 | 1,432 | 1,443 | same |
| Recorded Music revenue from streaming services | 3,223 (+2%) | 3,444 (+7%) | 3,505 (+2%) | MD&A, each year's 10-K |
| Music Publishing revenue from streaming services | 656 (+22%) | 752 (+15%) | 791 (+5%) | same |
| Capital expenditures | 127 | 116 | 139 | FY2025 10-K cash flow statement |
| Depreciation and amortization | 332 | 327 | 376 | same (FY2025: depreciation 118 + amortization 258 per Note 17) |
| Acquisition of music publishing rights and music catalogs (investing) | 114 | 187 | 195 | same |
| Investments and acquisitions of businesses, net of cash received | 126 | 40 | 46 | same |
| Royalty advances (operating working-capital line) | (191) | (222) | (312) | same |
| Payment of deferred and contingent consideration (financing) | 133 | 20 | 23 | same |
| Net cash provided by operating activities | 687 | 754 | 678 | same |

COMPUTED from the filed figures above (arithmetic only, `peers_music/calc_wmg.py`; no judgment):

| Ratio | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Recorded Music operating margin | 17.7% | 17.5% | 15.7% |
| Music Publishing operating margin | 18.4% | 19.7% | 17.2% |
| Total operating margin | 13.1% | 12.8% | 10.3% |
| Recorded Music Adjusted OIBDA margin | 22.1% | 24.5% | 23.5% |
| Music Publishing Adjusted OIBDA margin | 27.2% | 27.3% | 27.6% |
| Capex / revenue | 2.1% | 1.8% | 2.1% |
| Catalog acquisitions / revenue | 1.9% | 2.9% | 2.9% |
| CFO less capex less catalog acquisitions | 446 | 451 | 344 |

The last row is arithmetic, NOT owner earnings: it is not a multi-year maintenance figure, and it
treats all catalog buying as if it were a deduction. Flagged so no one reads it as (c).

### Which measure the segment note uses (it changed twice in three filings)

- **FY2023 10-K (0001319161-23-000036), Note 18:** "The Company evaluates performance based on several
  factors, of which the primary financial measure is operating income (loss) before non-cash
  depreciation of tangible assets and non-cash amortization of intangible assets (“OIBDA”). The
  Company has supplemented its analysis of OIBDA results by segment with an analysis of operating
  income (loss) by segment." FY2023 OIBDA as then filed: Recorded Music 1,080; Music Publishing 293;
  total 1,122.
- **FY2024 10-K (0001319161-24-000039), Note 18:** "During the three months ended December 31, 2023,
  the Company changed the measure used to evaluate segment profitability from OIBDA to Adjusted OIBDA
  which is consistent with how the Company's CODM evaluates the results of operations and makes
  strategic decisions about the business. For these reasons, the Company believes that Adjusted OIBDA
  represents the most relevant measure of segment profit and loss. All disclosures relating to
  segment profitability, including those for the fiscal years ended September 30, 2023 and 2022, have
  been revised as a result of this change."
- **FY2025 10-K (0001319161-25-000034), Note 17:** "The Company’s CODM, which is our Chief Executive
  Officer, allocates resources and evaluates performance based on several factors, including operating
  income (loss) and other financial measures." The note table presents operating income by segment;
  Adjusted OIBDA appears in MD&A.
- **Internal discrepancy found:** the FY2024 10-K MD&A table gives FY2023 Recorded Music Adjusted
  OIBDA of 1,094 and Corporate Adjusted OIBDA loss of (155); Note 18 of the same filing gives 1,093 and
  (154). Totals agree at 1,235. Both recorded above; not smoothed.
- **For a like-for-like row against Sony, use segment operating income (GAAP, present in all three
  years).** Adjusted OIBDA excludes amortization of acquired catalogs, which is the main cost of the
  catalog strategy.

### Verbatim source lines, WMG

**Segment revenue split (FY2025 10-K, Item 1):**
> "Our Recorded Music business, home to superstar recording artists such as Ed Sheeran, Bruno Mars, Cardi B and Dua Lipa, generated $5.408 billion of revenue in fiscal 2025, representing 81% of total revenues. Our Music Publishing business, which includes esteemed songwriters such as Twenty One Pilots, Lizzo and Katy Perry, generated $1.306 billion of revenue in fiscal 2025, representing 19% of total revenues."

**Streaming, FY2025 (FY2025 10-K, MD&A):**
> "Revenue from streaming services increased by $61 million, or 2%, to $3,505 million for the fiscal year ended September 30, 2025 from $3,444 million for the fiscal year ended September 30, 2024. Adjusted for the impact of the DSP True-Up Payments in the current and prior years and the BMG Termination and the Digital License Renewal in the prior year, Recorded Music streaming revenue grew by 5%."

> "Revenue from streaming services increased by $39 million, or 5%, to $791 million for the fiscal year ended September 30, 2025 from $752 million for the fiscal year ended September 30, 2024." (Music Publishing)

**Streaming, FY2024 (FY2024 10-K, MD&A):**
> "Revenue from streaming services increased by $221 million, or 7%, to $3,444 million for the fiscal year ended September 30, 2024 from $3,223 million for the fiscal year ended September 30, 2023. Adjusted for the impacts of the BMG Termination and the Digital License Renewal, Recorded Music streaming revenue grew by 9%."

> "Revenue from streaming services increased by $96 million, or 15%, to $752 million for the fiscal year ended September 30, 2024 from $656 million for the fiscal year ended September 30, 2023, which includes the impact of the CRB Rate Benefit of $24 million in the prior year. Excluding the impact of the CRB Rate Benefit, Music Publishing revenue from streaming services grew 19%, reflecting the continued market growth and timing of payments, and the favorable impact of foreign currency exchange rates of $3 million."

**Streaming, FY2023 (FY2023 10-K, MD&A):**
> "Revenue from streaming services grew by $64 million, or 2%, to $3,223 million for the fiscal year ended September 30, 2023 from $3,159 million for the fiscal year ended September 30, 2022 and was impacted by unfavorable foreign currency exchange rates of $57 million, or 2%. Streaming revenue reflects a lighter release schedule and the market-related slowdown in ad-supported revenue in the first half of the year, as well as the impact of an additional week in the prior year."

> "Revenue from streaming services grew by $117 million, or 22%, to $656 million for the fiscal year ended September 30, 2023 from $539 million for the fiscal year ended September 30, 2022." (Music Publishing)

**One-off items inside FY2024 and FY2025 revenue (FY2025 10-K, MD&A), needed before reading any growth rate:**
> "The prior year included $75 million of Recorded Music licensing revenue from a licensing agreement extension for an artist’s catalog (the “Licensing Extension”), $43 million of incremental Recorded Music streaming revenue recognized from the DSP True-Up Payments, and $30 million of Recorded Music streaming revenue from a deal with one of the Company’s digital partners (the “Digital License Renewal”), which resulted in upfront revenue recognition for the fiscal year ended September 30, 2024. In addition, revenue growth was unfavorably impacted by the BMG Termination, which resulted in $81 million of lower Recorded Music revenue compared to the prior year, of which $34 million was in streaming revenue and $47 million was in physical revenue. Adjusted for these items, total revenues increased by 8%, which includes $7 million of favorable currency exchange fluctuations."

**Cash used in investing (FY2025 10-K, MD&A):**
> "Cash used in investing activities of $340 million for the fiscal year ended September 30, 2025 consisted of $46 million relating to investments and acquisitions of businesses, $195 million to acquire music-related assets, and $139 million relating to capital expenditures, partially offset by $40 million of proceeds from the sale of investments."

**Customer concentration (FY2025 10-K, notes):**
> "In the fiscal year ended September 30, 2025, the Company had three customers, Spotify, YouTube and Apple, that individually represented 10% or more of total revenues, whereby Spotify AB represented 20%, YouTube represented 12% and Apple represented 11% of total revenues."

**Catalog-buying vehicle (FY2025 10-K, Item 1):**
> "We plan to accelerate our acquisition strategy, including through the Beethoven JV, which will allow for the purchase of up to $1.2 billion of catalogs across Recorded Music and Music Publishing. The Beethoven JV will leverage third-party capital to expand our buying power, accelerating our M&A initiatives, while also providing us with additional rights, revenue, and market share."

### WMG statements on DSP PRICE INCREASES (for [E2-44])

FY2025 10-K (0001319161-25-000034), Item 1:
> "In addition to paid subscriber growth, we believe that, over time, streaming revenues will increase due to pricing increases as the broader market further develops. For example, in 2025, Spotify increased the price of its premium individual tier in multiple markets across South Asia, the Middle East, Africa, Europe, Latin America, and the Asia-Pacific region. In 2025, YouTube increased the prices of its individual and family plan tiers on both YouTube Premium and YouTube Music in Europe. In 2024, Amazon Music Unlimited increased the prices of both its individual and family subscription plans in the United States, Canada and the United Kingdom. We believe the value proposition that streaming provides to consumers supports premium product initiatives."

> "Align Contractual Terms with the Music Industry’s Growth. The music industry is increasingly focused on price increases as a driver of growth to complement the sustained growth in global subscribers that has fueled the industry for over a decade. We continue to see progress in aligning our contracts with streaming services with this new paradigm, with a focus on economic certainty. Our collaboration with many of the largest tech companies in the world, including Google, Apple, Amazon, and Spotify, provides more opportunities for innovation, along with greater certainty around our economic participation as product offerings evolve."

FY2024 10-K (0001319161-24-000039), Item 1:
> "In addition to paid subscriber growth, we believe that, over time, streaming revenues will increase due to pricing increases as the broader market further develops. For example, in 2024 Spotify increased prices in the United States for the individual, duo, family and student plans. YouTube increased prices of its individual and family plan tiers on both YouTube Premium and YouTube Music in Europe, the Middle East, Singapore, Thailand, and Indonesia in 2024. In 2023, Apple Music increased prices of its individual and family plans in the United States, and Amazon Music Unlimited increased the prices of both its individual and family subscription plans. We believe the value proposition that streaming provides to consumers supports premium product initiatives. Additionally, in 2023, Deezer increased prices for all new premium and family subscriptions in key territories including France, UK, Spain, Italy and the Netherlands."

FY2023 10-K (0001319161-23-000036), Item 1:
> "In addition to paid subscriber growth, we believe that, over time, streaming revenues will increase due to pricing increases as the broader market further develops. Streaming services are already at the early stages of experimenting with price increases. For example, in 2023 Spotify increased prices in 65 countries for the individual, duo, family and student plans. For the second time in 12 months in 2023 Deezer increased prices for all new premium and family subscriptions in key territories including France, UK, Spain, Italy and the Netherlands. YouTube increased prices of its individual and family plan tiers on both YouTube Premium and YouTube Music in the United States in 2023. In 2022, Apple Music increased prices of its individual and family plans in the United States, and Amazon Music Unlimited increased the prices of both its individual and family subscription plans. We believe the value proposition that streaming provides to consumers supports premium product initiatives."

Reading note (not a verdict): these passages state that DSPs raised consumer prices and that WMG "believe[s]" streaming revenues will increase from it; none of the three filings quantifies how much of a DSP price rise reached WMG's revenue. The pass-through share is NOT OBTAINED from WMG filings.

### WMG statements on MARKET SHARE (third-party source named by WMG: Music & Copyright)

FY2025 10-K, Item 1, Competition:
> "According to Music & Copyright, in 2024, the three largest recorded music companies were Universal Music Group, Sony Music Entertainment and us, which collectively accounted for approximately 70% of global recorded music revenues. There are many mid-sized and smaller players in the industry that accounted for the remaining approximately 30%, including independent recorded music companies. Universal Music Group was the market leader with an approximately 32% global market share in 2024 after absorbing the bulk of the recorded music assets of the former EMI in late 2012, followed by Sony Music Entertainment with an approximately 23% share. We held an approximately 15% share of global recorded music revenues in 2024."

> "The music publishing industry is also highly competitive. Global music publishing revenue closed in on the $10 billion milestone for the first time in 2024. The three largest music publishing companies collectively accounted for approximately 60% of the global market in 2024 according to Music & Copyright. According to Music & Copyright, Sony Music Publishing was the market leader in music publishing in 2024 with an approximately 25% share (reflecting its ownership of the EMI music publishing assets). Universal Music Publishing was the second-largest music publisher with an approximately 23% share, followed by us at approximately 12%."

FY2024 10-K (calendar 2023 shares): "Universal Music Group was the market leader with an approximately 32% global market share in 2023 after absorbing the bulk of the recorded music assets of the former EMI in late 2012, followed by Sony Music Entertainment with an approximately 22% share. We held an approximately 16% share of global recorded music revenues in 2023." Publishing: "Sony Music Publishing was the market leader in music publishing in 2023 with an approximately 25% share (reflecting its ownership of the EMI music publishing assets). Universal Music Publishing was the second-largest music publisher with an approximately 23% share, followed by us at approximately 12%."

FY2023 10-K (calendar 2022 shares): "Universal Music Group was the market leader with an approximately 31% global market share in 2022 after absorbing the bulk of the recorded music assets of the former EMI in late 2012, followed by Sony Music Entertainment with an approximately 23% share. We held an approximately 16% share of global recorded music revenues in 2022." Publishing: "Sony Music Publishing was the market leader in music publishing in 2022 with an approximately 25% share (reflecting its ownership of the EMI music publishing assets). Universal Music Publishing was the second-largest music publisher with an approximately 23% share, followed by us at approximately 12%."

Evidence class: these shares are WMG quoting a third-party trade publication (Music & Copyright) inside a filed 10-K. They are filed statements, but the underlying measurement is not WMG's.

### WMG on HOW AN ATTACKER COMPETES (for [E2-45])

FY2025 10-K, Item 1A:
> "We compete with other recorded music companies and music publishing companies to identify and sign new recording artists and songwriters with the potential to achieve long-term success and to enter into and renew agreements with established recording artists and songwriters. In addition, our competitors may from time to time increase the amounts they spend to discover, or to market and promote, recording artists and songwriters or reduce the prices of their music in an effort to expand market share. We may lose business if we are unable to sign successful recording artists or songwriters or to match the prices offered by our competitors. Our Recorded Music business competes not only with other recorded music companies, but also with recording artists who may choose to distribute their own works (which has become an easy option as music is distributed online rather than physically) and companies in other industries (such as digital music services) that may choose to sign direct deals with recording artists or recorded music companies. Our Music Publishing business competes not only with other music publishing companies, but also with songwriters who publish their own works and companies in other industries that may choose to sign direct deals with songwriters or music publishing companies. In addition to competition from traditional music industry players, we also face competition from new entrants, including investment funds that make acquisitions or investments in recorded music or music publishing catalogs and the income streams derived therefrom."

Wording drift worth noting: the FY2023 and FY2024 10-Ks say self-distribution "has become more practicable" and name "(such as Spotify)"; the FY2025 10-K says it "has become an easy option" and names "(such as digital music services)".

### WMG on AI-GENERATED MUSIC AS A RISK

FY2025 10-K, Item 1:
> "AI also presents certain risks, including the unauthorized use of copyright-protected catalogs, and the unauthorized use of the images, voices or visual likeness of artists to train AI models. The use of AI models to produce unauthorized deepfakes of artists may result in works that compete with human-created content, and the proliferation of such AI-generated material could lead to market saturation and a consequent devaluation of human-created music. Additionally, AI-driven streaming fraud may impact compensation for artists, songwriters and rightsholders."

FY2025 10-K, Item 1A:
> "Generative AI could adversely affect our results."
> "There are new businesses which are taking the position that the use of copyright-protected material to train a generative AI model is fair use and does not require the consent of the copyright holder. This issue is the subject of multiple litigations, mostly in the United States. We are plaintiffs in some of those litigations. If there is a negative result in those litigations and those businesses could legitimately use our copyright-protected material without our consent to train an AI model that could create vast quantities of new musical works to compete with and dilute the impact of our copyright-protected material on digital music services, it could adversely affect our results."

> "Additionally, in its Global Music Report 2025, IFPI noted the danger of “streaming manipulation,” where bad actors upload tracks to digital music services that are produced using generative AI tools and then use “bots” to generate artificial streams of those tracks, which ultimately diverts royalties from legitimate copyright holders."

---
## PEER 2: UNIVERSAL MUSIC GROUP N.V. (Euronext Amsterdam: UMG; calendar year; IFRS; euros)

**Evidence rung: 3 (company IR site, English).** UMG is not an SEC registrant. EDGAR holds only an ADR
shell, "Universal Music Group N.V./ADR", CIK 0001890126, whose only filing form is F-6EF (checked
2026-09-13 via submissions JSON). All documents below were linked from
`https://investors.universalmusic.com/reports/` (fetched 2026-09-13) and are served from UMG's content
CDN `assets.ctfassets.net/e66ejtqbaazg/...` / `downloads.ctfassets.net/e66ejtqbaazg/...`.

| Doc | Dated | URL | Local copy |
|---|---|---|---|
| Annual Report 2025 (audited FS inside) | published 2026-03-26 per UMG release (search result, not verified in the PDF) | https://assets.ctfassets.net/e66ejtqbaazg/7HObJrt5UDQfjjfKYN454B/201bf057190c5ed4ee185b04a34ec095/UMG_2025_Annual_Report.pdf | `cache/UMG_AR_2025.pdf`, `UMG_AR_2025.cols.txt` |
| Annual Report 2024 (audited FS inside; carries FY2023 comparatives) | 2025 | https://downloads.ctfassets.net/e66ejtqbaazg/3lVdyJmpf8DQTPMRcxChSQ/80752d027f61e3846f4b5e2a5a62a958/UMG_2024_Annual_Report.pdf | `cache/UMG_AR_2024.pdf`, `UMG_AR_2024.cols.txt` |
| Q4 and FY2025 results release | 2026-03-05 | https://assets.ctfassets.net/e66ejtqbaazg/29H5pgbmmYOowQgJET2Wh8/4355ccb601037ecc345ccef3a9d9bc74/UMG_Q4___FY25_results_press_release.pdf | `UMG_PR_FY25.mu.txt` |
| Q4 and FY2024 results release | early 2025 | https://assets.ctfassets.net/e66ejtqbaazg/1Y06bSVvRmv2QhNwI9rb8c/879342db19bd0967324c084b9139d8c9/UMG_4Q___FY24_Press_release.pdf | `UMG_PR_FY24.mu.txt` |
| Q4 and FY2023 results release | early 2024 | https://assets.ctfassets.net/e66ejtqbaazg/1psEFHkZbqpN6GxbUUYhPL/eae1981f98c7c682e5d09a2b324e1df0/UMG_4Q___FY23_Press_Release.pdf | `UMG_PR_FY23.mu.txt` |

**The 2023 Annual Report itself was NOT fetched:** it is not linked from the /reports/ page. FY2023
figures below come from the FY2023 comparative columns of the audited 2024 Annual Report (and growth
rates from the FY2023 results release), which is the later and audited source.

**Cross-checks:** FY2025 revenue 12,507 and Adjusted EBITDA 2,810 agree between the AR 2025 Note 3
segment table (p.211) and the FY2025 results release. The AR 2025 Consolidated Statement of Cash Flows
(p.194) agrees line for line with the Financial Review cash-flow table (p.58).

**Extraction artifacts (flagged, not smoothed):** (1) `pdftotext -layout` DROPPED the euro sign from
the results releases (it printed "Revenue of 12,507 million"); those copies were deleted and the
releases re-extracted with PyMuPDF, which keeps "€". (2) AR 2025 p.42 and p.93 read "advancing Al and
fraud protections" in the text layer: "Al" (A, lowercase L) where "AI" is evidently meant. Quoted as
extracted. (3) AR 2025 p.92 reads "compared to €6,038 for the year ended December 31, 2024" with no
"million". Quoted as extracted.

### Table: UMG, € millions, as reported

| Line | FY2023 | FY2024 | FY2025 | Source |
|---|---|---|---|---|
| Revenues | 11,108 | 11,834 | 12,507 | AR 2024 Note 3 p.201 (FY23, FY24); AR 2025 Note 3 p.211 (FY25) |
| Recorded Music revenues | 8,461 | 8,901 | 9,456 | same |
| Music Publishing revenues | 1,956 | 2,121 | 2,260 | same |
| Merchandising and other revenues | 706 | 842 | 811 | same |
| Recorded Music operating profit (IFRS) | 1,393 | 1,752 | 1,985 | same |
| Music Publishing operating profit | 269 | 321 | 371 | same |
| Merchandising and other operating profit | 41 | 38 | 12 | same |
| Corporate centre operating profit | (285) | (336) | (370) | same |
| Operating profit (IFRS), total | 1,418 | 1,775 | 1,998 | same |
| Recorded Music EBITDA (company-defined) | 1,618 | 2,073 | 2,282 | AR 2024 p.201; FY25 release |
| Music Publishing EBITDA | 420 | 486 | 531 | same |
| EBITDA, total | 1,808 | 2,332 | 2,538 | same |
| Recorded Music Adjusted EBITDA | 2,042 | 2,275 | 2,423 | AR 2024 p.201; AR 2025 p.211 |
| Music Publishing Adjusted EBITDA | 470 | 511 | 549 | same |
| Adjusted EBITDA, total | 2,369 | 2,661 | 2,810 | same |
| Non-cash share-based compensation, total | 561 | 329 | 227 | same |
| Amortisation and depreciation expense, total | 382 | 409 | 446 | same |
| RM subscription revenue | 4,275 | 4,623 (AR24) / 4,624 (AR25) | 4,884 | AR 2024 p.202; AR 2025 p.212 |
| RM streaming revenue (UMG's term: ad-supported, see note) | 1,425 | 1,414 | 1,435 | same |
| RM subscription growth, reported / constant currency | +9.6% / +12.8% | +8.2% / +9.1% | +5.6% / +8.6% | results releases FY23, FY24, FY25 |
| RM streaming growth, reported / constant currency | +0.4% / +3.6% | -0.8% / +0.1% | +1.5% / +4.7% | same |
| Music Publishing digital revenue | 1,128 | 1,268 | 1,371 | AR 2024 p.202; FY25 release |
| Capital expenditures (cash flow) | (47) | (91) | (70) | AR 2024 p.184; AR 2025 p.194 |
| Other intangible assets investments | (74) | (92) | (125) | same |
| Catalogue investments (cash flow) | (178) | (266) | (345) | same |
| Purchases of consolidated companies, after acquired cash | (97) | (163) | (62) | same |
| Investments in equity affiliates | (81) | (390) | (198) | same |
| Royalty advances payments, net of recoupments | (100) | (186) | (402) | same |
| Net cash from operating activities before income tax paid | 2,278 | 2,104 | 2,142 | same |
| Net cash from operating activities | 1,885 | 1,755 | 1,739 | same |
| Free Cash Flow (company-defined) | NOT OBTAINED from AR (FY24 release layout garbled; not transcribed) | 523 | 702 | AR 2025 p.59 |

**Definitional warning for the row.** UMG's "streaming revenue" is NOT WMG's "revenue from streaming
services". UMG splits subscription from streaming, and the AR 2024 (p.30) calls the latter "Ad-supported
streaming revenues". WMG's streaming figure includes subscription. The comparable UMG number to WMG's
Recorded Music streaming line is subscription plus streaming: 5,700 / 6,037-6,038 / 6,319 (AR 2025 p.92
states "€6,319 million of subscription and streaming revenues"; the 2023 and 2024 sums are arithmetic
from the table above).

**Restatement noted:** AR 2024 gives 2024 subscription 4,623 and license and other 1,326; AR 2025
restates the 2024 comparatives as 4,624 and 1,325. Both recorded.

**Catalogue-spend definitions differ between UMG documents:** the FY2025 release says "Cash paid for
catalogue acquisitions, net of divestments of intangible assets, increased to €280 million in 2025
compared to €266 million in 2024." The audited cash flow statement shows "Catalogue investments (345)
(266)". Arithmetic: 345 less the 65 of "Proceeds from sales of property, plant, equipment and
intangible assets" equals 280; the same subtraction for 2024 (266 less 2) gives 264, not 266. The
release does not state its reconciling basis. Use the cash flow statement line.

COMPUTED from the table (arithmetic only, `peers_music/calc_umg.py`; no judgment):

| Ratio | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Recorded Music operating profit margin | 16.5% | 19.7% | 21.0% |
| Music Publishing operating profit margin | 13.8% | 15.1% | 16.4% |
| Total operating profit margin | 12.8% | 15.0% | 16.0% |
| Recorded Music Adjusted EBITDA margin | 24.1% | 25.6% | 25.6% |
| Music Publishing Adjusted EBITDA margin | 24.0% | 24.1% | 24.3% |
| (Capex + other intangible investments) / revenue | 1.1% | 1.5% | 1.6% |
| Catalogue investments / revenue | 1.6% | 2.2% | 2.8% |
| CFO less capex, other intangibles and catalogue investments | 1,586 | 1,306 | 1,199 |

FY2023 operating profit carries €561m of non-cash share-based compensation (FY2024: €329m; FY2025:
€227m), per the segment tables, so the FY2023 to FY2025 operating-margin rise is partly that line
falling. The last computed row is NOT owner earnings (it is after tax but before lease repayments and
treats every catalogue purchase as a deduction).

### Which measure the segment note uses

AR 2025, Note 3, p.211:
> "Segment Adjusted EBITDA is included in these disclosures because it is the primary measure of profit or loss used by UMG Management to assess each segment’s performance and make decisions about allocating resources. Adjusted EBITDA is a non-IFRS measure. Adjusted EBITDA is calculated as Operating Profit excluding amortisation of intangible assets, impairment of goodwill and other intangibles, depreciation of tangible assets including right of use assets, gains/losses on the sale of tangible assets including right of use assets and intangible assets, restructuring expenses, non-cash share-based compensation expenses and certain one-time items that are deemed by management to be significant and incidental to normal business activity."

The note tables still show segment Operating profit (IFRS) for every segment and year, which is why the
row above can carry operating profit like-for-like with WMG and Sony.

FY2025 results release, Appendix:
> "To calculate EBITDA, the accounting impact of the following items is excluded from the Operating Profit: i. amortisation of intangible assets; ii. impairment of goodwill and other intangibles; iii. depreciation of tangible assets including right of use assets; iv. (gains)/losses on the sale of tangible assets, including right of use assets and intangible assets; and v. restructuring expenses."
> "The difference between EBITDA and Adjusted EBITDA consists of non-cash share-based compensation expense and certain one-time items, that are deemed by management to be significant and incidental to normal business activity."

### Verbatim source lines, UMG financial

FY2025 release:
> "Revenue of €12,507 million increased 5.7% year-over-year, or 8.7% in constant currency, driven by growth across the Recorded Music and Music Publishing segments."
> "Recorded Music subscription revenue grew 5.6% year-over-year, or 8.6% in constant currency, and streaming revenue grew 1.5% year-over-year, or 4.7% in constant currency."
> "Excluding these amounts, Recorded Music Adjusted EBITDA in 2025 was €2,423 million, up 6.5% year-over-year, or 9.6% in constant currency, driven by revenue growth."
> "Excluding these amounts, Music Publishing Adjusted EBITDA of €549 million was up 7.4% year-over-year, or 10.0% in constant currency, driven by revenue growth"

AR 2025, Financial Review p.59:
> "the increase in Royalty advances payments net of recoupments (-€216 million) due to the timing of major artist renewals and extensions."
> "Catalogue investments in 2025 were higher than in 2024 (-€79 million) due to the timing of deals and investment in other intangible assets and capital expenditure was also slightly higher (-€12 million)."

FY2024 release:
> "Cash paid for catalogue acquisitions increased to €266 million in 2024 compared to €178 million in 2023 and included the acquisition of the remaining stake in RS Group in Thailand and the completion of a 2023 catalogue acquisition for which the cash had been previously paid into escrow."

FY2023 release:
> "Cash paid for catalogue acquisitions decreased to €178 million in 2023 compared to €359 million in 2022 and included the previously announced acquisitions of catalogues from RS Group in Thailand and Oriental Star Agencies, a British label focused on South Asian music, as well as several artist catalogue deals."
> "Recorded Music Adjusted EBITDA in 2023 was €2,042 million, up 7.5% year-over-year, or 11.0% in constant currency, driven by the growth in revenue."

Customer concentration, AR 2024 p.202:
> "In 2024, UMG had 3 customers that each individually represented over 10% of total revenues (3 customers in 2023) and which represented total revenues of 20%, 11% and 10% respectively (19%, 11% and 10% in 2023)."

DSP dependency, AR 2025 p.93:
> "For the year ended December 31, 2025, the top 50 music services accounted for 97% of UMG’s recorded music digital revenue, as compared to 98% for the year ended December 31, 2024. For the year ended December 31, 2025, 70% of UMG’s recorded music revenue was derived from digital channels, as compared to 70% for the year ended December 31, 2024."
> "UMG typically enters into relatively short-term agreements with digital music streaming services. There can be no assurance that UMG will be able to renew agreements on the same terms or enter into new agreements with any digital music service."

### UMG statements on DSP PRICE INCREASES (for [E2-44])

FY2023 results release (Q4 2023 commentary):
> "Subscription revenue grew 8.9% year-over-year, or 15.0% in constant currency, driven by the growth in global subscribers as well as the impact of price increases at certain platforms."

FY2024 results release (FY2024 commentary):
> "Subscription revenue grew 8.2% year-over-year, or 9.1% in constant currency, driven by growth in global subscribers and the benefit of price increases."

AR 2024, p.53 (Financial Review):
> "Subscription revenues grew by 8.2% or 9.1% in constant currency driven by the growth in global subscribers as well as the impact of price increases at certain platforms. Streaming revenue declined 0.8%, but grew by 0.1% in constant currency as the consumption grows but continues to shift from better monetized video platforms to short-form platforms, which are not yet as well monetized."

AR 2025, p.30 (FY2025, price increases NOT named as a driver):
> "Subscription revenue saw growth of 5.6% year-over-year, or 8.6% on a constant currency basis, largely driven by the growth in global subscribers."

AR 2025, p.42 ("Streaming 2.0", the contractual form of the price argument):
> "Under Streaming 2.0, we elevate our focus on maximizing customer value, while also continuing to grow the subscriber base."
> "We executed our first major Streaming 2.0 deal in late 2024 when we expanded our global partnership with Amazon, implementing artist centric initiatives, advancing Al and fraud protections and promoting revenue growth. In 2025, we signed new multi-year agreements with Spotify and YouTube platforms covering recorded music and music publishing that also embrace our Streaming 2.0 framework. These agreements provide for new paid-subscription tiers, the bundling of music and non-music content, and a richer audio and visual content catalog that we believe will benefit artists, songwriters, platforms and consumers alike."

AR 2025, p.92 (risk):
> "As subscription growth has slowed in established markets, UMG is focused on subscriber growth potential in lower average revenue per user ("ARPU") markets."

Reading note (not a verdict): UMG names price increases as a subscription driver in FY2023 and FY2024
and does not in the FY2025 AR sentence above; no UMG document read quantifies the price component
separately from subscriber growth. The pass-through share is NOT OBTAINED.

### UMG statements on MARKET SHARE

**NOT OBTAINED as a number from UMG.** Searched AR 2025 and AR 2024 (all pages) for "market share",
"global market share", "Music & Copyright", "MIDiA", "largest music company". UMG states a qualitative
claim only:
> "As part of the world’s largest music company, we are uniquely positioned to develop collaborative strategies between publishing and recorded music." (AR 2025 p.32; same sentence AR 2024 p.32)

and a regional one (AR 2025 p.176): "Increased market share in 10 high-potential markets or regions in
AMEA during 2025." Numeric shares for UMG, Sony and WMG come only from WMG's 10-K (Music & Copyright),
recorded in the WMG section. UMG's risk section names "Decline in subscription adoption, streaming
revenue and digital market share" as a risk heading (AR 2025 p.92).

### UMG on HOW AN ATTACKER COMPETES (for [E2-45])

AR 2025, p.91:
> "UMG’s competitors may become more successful at signing, marketing and promoting recording artists, for example if UMG’s competitors increase the amounts they spend to discover, or to market and promote, recording artists and songwriters or reduce the prices of their music in an effort to expand market share, which may adversely impact UMG’s business, results and financial position."
> "UMG also faces competition from traditional music industry players as well as new entrants, including investment funds whose investment thesis includes making acquisitions of collections of musical compositions, or "catalog acquisitions"."
> "In addition, changing business practices, particularly due to the emergence of new technologies and access to a global network of consumers, has and could further result in artists choosing to make content available to consumers directly without being affiliated with a label or an intermediary, or could result in music services playing some of the roles that UMG has traditionally played. In this regard, UMG also competes with certain of the music distribution platforms who distribute the works of artists and songwriters without the involvement of labels or intermediaries."

AR 2025, p.92:
> "UMG invests more money and expertise through its staff of industry specialists than any other recorded music company in signing and developing talent."

### UMG on AI-GENERATED MUSIC AS A RISK

AR 2025, p.96 (risk heading "Generative AI"; the p.90 risk matrix row extracts as "Generative AI High High", column headers not transcribed):
> "Generative AI poses challenges to UMG's intellectual property rights and use of generative AI could adversely affect UMG's business, financial condition, results of operations and prospects."
> "Such infringing AI-generated content, unlicensed training on UMG’s catalogues of copyright-protected artists content, and fraud could create vast quantities of works that include content and consumer engagement products improperly associated with artists and targeted at their fan bases. In addition, large-scale use of legitimately produced AI generated music could also create vast quantities of new musical works. Any of the foregoing may compete with consumption of, and dilute engagement with, UMG’s copyright-protected material on digital music services, including royalty pool dilution as well as undermine other licensing opportunities for UMG’s works, which could adversely affect UMG’s results."
> "UMG’s rights in NIL and merchandising are not as robust as they are in recorded music, and there is a risk that artists will work with third parties using AI to monetise those rights rather than through UMG."

AR 2025, p.92:
> "Large quantities of uploads with no meaningful engagement, including non-artist noise content delivered daily to digital platforms (including via the use of generative AI), or misattribution increase the challenges for marketing music to fans and policing infringements."

FY2025 results release (AI as licensing income, same year):
> "Excluding the Legal Settlements in the prior year, License and other revenue grew 26.8% in constant currency driven by strong live event and other related income, primarily in Japan, as well as by a compensatory payment as part of a strategic licensing agreement with an AI music platform."

---
## CONTEXT: RESERVOIR MEDIA, INC. (CIK 0001824403, fiscal year ends March 31; US$)

Context only, per brief. A catalog owner, publishing-weighted. Rung 1.

| Doc | Filed | Accession | File |
|---|---|---|---|
| 10-K FY2026 (FYE 2026-03-31) | 2026-05-28 | 0001104659-26-067615 | rsvr-20260331x10k.htm -> `RSVR_10K_FY2026.txt` |
| 10-K FY2025 (FYE 2025-03-31) | 2025-05-28 | 0001410578-25-001379 | rsvr-20250331x10k.htm -> `RSVR_10K_FY2025.txt` |

| Line (US$ millions, from whole-dollar statements) | FY2024 | FY2025 | FY2026 | Source |
|---|---|---|---|---|
| Revenues | 144.86 | 158.71 | 175.66 | Consolidated Statements of Income |
| Operating income | 24.58 | 35.06 | 38.23 | same |
| Amortization and depreciation | 24.99 | 26.30 | 30.78 | same |
| Music Publishing segment revenue | n/c | 107.41 | 116.80 | FY2026 10-K segment note |
| Recorded Music segment revenue | n/c | 44.25 | 51.51 | same |
| Music Publishing segment OIBDA | n/c | 37.34 | 40.89 | same |
| Recorded Music segment OIBDA | n/c | 22.75 | 26.86 | same |
| Purchases of music catalogs (investing) | 50.13 | 96.48 | 101.60 | Consolidated Statements of Cash Flows |
| Purchases of property and equipment | 0.23 | 0.08 | 0.48 | same |
| Net cash provided by operating activities | 36.19 | 45.28 | 50.14 | same |

n/c = not collected (FY2024 segment table sits in the FY2025 10-K in a cell-per-line layout; not
transcribed because RSVR is context only).

COMPUTED (arithmetic only): operating margin 17.0% / 22.1% / 21.8%; catalog purchases / revenue
34.6% / 60.8% / 57.8%; CFO less capex less catalog purchases -14.2 / -51.3 / -51.9. Segment OIBDA
margin FY2026: Music Publishing 35.0%, Recorded Music 52.1%.

Segment measure, FY2026 10-K segment note:
> "The Company’s CODM evaluates financial performance of its segments based on operating income before depreciation and amortization (“OIBDA”)."

DSP pricing, FY2026 10-K, Item 1:
> "Beyond growth in paying subscribers, we believe recent developments suggest that streaming pricing may have room for further optimization. In February 2026, Amazon Music raised prices for its Music Unlimited subscribers in the U.S. and U.K., following price increases in 2023. In February 2026, Spotify increased prices for U.S. premium subscribers. The increase marks Spotify’s third increase in three years. In 2024, Spotify increased prices for U.S. premium subscribers, following previous price raises in 2023 in 65 countries for the individual, duo, family and student plans. YouTube and Deezer have not increased prices since 2023, and Apple last raised prices of its individual and family plans in the U.S. in 2022."

**Conflict between filers, flagged:** RSVR (filed 2026-05-28) says "YouTube and Deezer have not
increased prices since 2023"; WMG's FY2025 10-K (filed 2025-11-20) says "In 2025, YouTube increased the
prices of its individual and family plan tiers on both YouTube Premium and YouTube Music in Europe", and
WMG's FY2024 10-K lists YouTube increases in 2024 in "Europe, the Middle East, Singapore, Thailand, and
Indonesia". RSVR's sentence may be U.S.-only in intent, but it does not say so. Neither is a DSP's own
filing; the DSP price history is secondary in both.

AI, FY2026 10-K, Item 1A heading:
> "The development, deployment, and use of Artificial Intelligence (AI), including Generative AI, presents challenges for protecting our intellectual property and the rights of our artists and songwriters and could adversely affect our business and results of operation."

---
## WHAT WAS NOT OBTAINED, AND WHY

1. **DSP price pass-through to labels, quantified.** Neither WMG (three 10-Ks) nor UMG (two ARs, three
   results releases) separates the price component of subscription growth from subscriber growth.
   The document that would resolve it is a DSP-label licence agreement, which is confidential; the
   nearest public proxy would be Spotify's own 20-F (ARPU and premium revenue by year), which is not a
   music-peer document and was not in scope.
2. **UMG's own numeric market share.** UMG states none in AR 2024 or AR 2025. Numeric shares exist only
   as WMG's citation of Music & Copyright.
3. **UMG 2023 Annual Report.** Not linked on the /reports/ page; FY2023 taken from the audited AR 2024
   comparatives instead.
4. **UMG FY2023 company-defined Free Cash Flow.** The FY2024 release table did not extract cleanly;
   not transcribed rather than guessed.
5. **Anime / Visual Media & Platform peer.** Not requested and not pulled (see brief defects below).
6. **WMG fiscal 2026 (FYE 2026-09-30).** Not yet filed as of 2026-09-13; a 10-K would be expected around
   November 2026. Quarterly 10-Qs for fiscal 2026 were not pulled.

## DEFECTS FOUND IN THE BRIEF

1. **The Sony Music segment includes "Visual Media & Platform" (anime), and the brief names no peer
   for it.** WMG, UMG and RSVR are all pure music. A segment-margin comparison of Sony Music against
   them is contaminated unless the main run strips Visual Media & Platform out of Sony's figure, or a
   separate anime peer is added.
2. **"Streaming revenue and growth" is not one metric across peers.** WMG's "revenue from streaming
   services" includes subscription; UMG's "streaming revenue" is ad-supported only and sits beside a
   separate subscription line. Taken literally, the brief would put WMG's 3,505 beside UMG's 1,435.
   The comparable UMG figure is subscription plus streaming (6,319 in FY2025).
3. **"Segment operating income (and OIBDA if that is what the segment note uses)" assumes a stable
   measure.** WMG's note changed its measure twice in three filings (OIBDA, then Adjusted OIBDA, then
   operating income). UMG's note measure is Adjusted EBITDA, which excludes share-based compensation
   (€561m in FY2023). The only measure present for all peers and all years is segment operating
   income/profit (GAAP/IFRS); that is the one to put beside Sony.
4. **Window mismatch.** "FY2023-FY2025" means years ending September (WMG), December (UMG) and March
   (RSVR, and Sony). No two peers share a year-end; the table is by each company's own fiscal year.
5. **Currency.** WMG and RSVR report in US$, UMG in €, Sony in ¥. No conversion was done here (none
   was asked for); margins are currency-neutral, absolute sizes are not comparable without it.
6. **"Cash paid for catalog acquisitions" is defined differently inside UMG's own documents** (release
   "net of divestments" 280 vs cash flow statement 345 for FY2025). Brief did not anticipate this; the
   cash flow statement line is used.

Status: COMPLETE for the scope of the brief (2026-09-13). No moat verdict is reached in this file.

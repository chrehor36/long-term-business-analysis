# SONY run: Pictures competitor row, PEERS (WBD, DIS, Lionsgate, Paramount, Comcast)
Built 2026-09-13 by a subagent. Evidence gathering only; no moat verdict is reached here.
Status: COMPLETE for the five peers in the brief (10-K evidence). Arithmetic by `peers_pictures/calc.py`; figures transcribed from the filed text of each 10-K (not XBRL).

## SUMMARY ROW (details, definitions and verbatim sources in sections 1-5 below)

**The five peers do NOT report one metric.** Three EBITDA-type measures (WBD Adjusted EBITDA, Comcast Adjusted EBITDA, Paramount Adjusted OIBDA), one contribution measure (Lionsgate segment profit, before non-film D&A), and one after-D&A measure (Disney segment operating income). All five keep film cost amortization INSIDE the measure; they differ on D&A of other assets, SBC, restructuring and which content impairments are excluded. Only WBD also files a segment operating income (MD&A reconciliation). Any comparison to Sony Pictures must state which Sony segment measure (taken from Sony's own filing by the main run; not checked here) is set against which peer measure.

| Peer / segment | Measure | FY2023 rev $m | FY2023 profit $m | margin | FY2024 rev $m | FY2024 profit $m | margin | FY2025 rev $m | FY2025 profit $m | margin |
|---|---|---|---|---|---|---|---|---|---|---|
| WBD Studios (Dec FY) | Adjusted EBITDA | 12,192 | 2,183 | 17.9% | 11,607 | 1,652 | 14.2% | 12,619 | 2,545 | 20.2% |
| WBD Studios (Dec FY) | Operating income (MD&A) | 12,192 | 211 | 1.7% | 11,607 | 529 | 4.6% | 12,619 | 1,674 | 13.3% |
| Disney Entertainment (Sept FY) | Segment OI | 40,635 | 1,444 | 3.6% | 41,186 | 3,923 | 9.5% | 42,466 | 4,674 | 11.0% |
| Disney Content Sales/Licensing and Other (Sept FY) | Segment OI (sub-segment, MD&A) | 9,048 | (179) | (2.0%) | 7,718 | 328 | 4.2% | 8,488 | 392 | 4.6% |
| Lionsgate Motion Picture (FY ends Mar of following year: FY2024 = Mar-2024) | Segment profit | FY2024: 1,666.0 | 312.4 | 18.8% | FY2025: 1,598.6 | 304.3 | 19.0% | FY2026: 1,617.1 | 278.9 | 17.2% |
| Lionsgate Television Production | Segment profit | FY2024: 1,330.1 | 146.8 | 11.0% | FY2025: 1,605.8 | 136.5 | 8.5% | FY2026: 1,044.6 | 124.5 | 11.9% |
| Paramount Filmed Entertainment (Dec FY) | Adjusted OIBDA | 2,957 | (119) | (4.0%) | 2,955 | (96) | (3.2%) | split: 1,593 Pred. / 1,736 Succ. | (100) / (132) | (6.3%) / (7.6%) |
| Comcast Studios (Dec FY) | Adjusted EBITDA | 11,625 | 1,269 | 10.9% | 11,092 | 1,404 | 12.7% | 11,286 | 1,099 | 9.7% |

Lionsgate columns are shifted: its FY2024/FY2025/FY2026 (years ending March) are placed under 2023/2024/2025 respectively. That is a CONVENTION for layout only (the fiscal year ending March 2024 covers mostly calendar 2023), not a filed alignment.

Content spend / film cost proxies (not the same definition across peers, see sections):
- WBD Studios "Content amortization and impairment expense": 5,074 / 5,692 / 3,106 (2023/2024/2025).
- Disney CS/L&O "Programming and production costs": 5,383 / 4,135 / 4,260 (FY2023/24/25).
- Lionsgate Motion Picture direct operating expense: 807.1 / 830.7 / 797.6 (FY2024/25/26); company-wide film and TV amortization 929.8 / 1,172.7 / 1,022.6.
- Paramount Filmed Entertainment content costs: 1,545 / 1,496 / 846 Pred. + 1,287 Succ. (Successor period on a pushed-down, written-up asset base).
- Comcast Studios "Programming and production": 7,958 / 7,257 / 7,441; company-wide amortization of owned content $7.8bn / $7.8bn / $8.0bn.

Intersegment revenue matters for the comparison: WBD Studios and Comcast Studios book licenses to their own streaming/networks as revenue at market value (Comcast intersegment 28-29% of Studios revenue); Paramount records "no intersegment licensing revenues or profits" for the licensor segment; Lionsgate's FY2024-FY2025 segment revenue includes large sales to then-consolidated Starz.

Literal phrase "hit-driven": zero hits in all peers' 10-Ks. Screen by `tools/sources.py:fts_count` ("hit-driven" and "hit driven", forms 10-K, each of the seven CIKs incl. Paramount Global and STRZ/old Lionsgate): 0 hits each, 2026-09-13; positive control "unpredictable and volatile" in WBD 10-Ks returned 12 hits, "difficult to predict" in LION 10-Ks returned 2, so the zeros are not a dead search. In the 10-K texts on disk, the whole word "hit" appears 6 times (WBD FY2024 and FY2025, LION FY2025 and FY2026), every time as promotional description of a title ("Other hit HBO series", "TLC’s breakout hit Baylen Out Loud", "long-running hit series"), never to describe the business model; "blockbuster" appears 0 times. The filings express the idea in other words ("unpredictable", "cannot be predicted with certainty", "limited number of content releases", "before we learn whether"); those verbatim lines are in each section.

### NOT OBTAINED, and why
- Paramount full-year 2025 segment Adjusted OIBDA: not filed. 2025 is split into Predecessor (Jan 1 to Aug 6) and Successor (Aug 7 to Dec 31) on different accounting bases; the filing provides a pro forma full-year REVENUE only (3,832). Adding the two OIBDA periods would cross a basis change and was not done.
- Segment operating income for Comcast Studios, Paramount Filmed Entertainment and Lionsgate segments: not reported by segment (D&A reconciled only in total).
- Studios-only film cost amortization for Comcast and Disney: not disclosed at segment level in the 10-K text read; company-wide or cost-line proxies given instead.
- Disney in-segment "film cost impairments" (inside CS/L&O OI): referenced in MD&A but not quantified in the text read.
- Allocation of Paramount's 2023/2024 programming charges ($2.37bn / $1.12bn) to Filmed Entertainment: not found.
- Paramount's new "Studios" segment (from Q1 2026) and WBD 2026 quarters: not pulled; outside the 10-K window of the brief.
- Status of the PSKY/WBD merger after the WBD 10-K date (2026-02-27): not checked.
- 10-K/As not read in full: DIS FY2023 10-K/A (acc. 0001744489-24-000064), LION FY2025 10-K/A (acc. 0001193125-25-167991). PSKY FY2025 10-K/A read at purpose paragraph: Part III only.

### Defects found in the brief
1. "Paramount (PARA ...)": `cik_for("PARA")` returns `0001826011 Banzai International, Inc.` The ticker has been reassigned. A run that trusted the ticker would pull the wrong company. Paramount Global is CIK 0000813828 (no current ticker); the FY2025 filer is Paramount Skydance Corp., PSKY, CIK 0002041610.
2. "Lionsgate Studios (LION) or Lions Gate Entertainment (LGF)": LGF-A / LGF.A are not in the SEC ticker map; the old Lions Gate Entertainment Corp. CIK 0000929351 is now STARZ ENTERTAINMENT CORP /CN/ and files a 10-KT for Dec-2025. The studio segments are in Lionsgate Studios Corp. (LION, CIK 0002052959).
3. "Paramount Filmed Entertainment, 2023-2025": 2025 does not exist as one period in the filing (predecessor/successor split), and the segment was dissolved into a new "Studios" segment from Q1 2026, which also absorbs Paramount's TV studios (previously in TV Media). The FY2023-2025 Filmed Entertainment series is therefore not comparable to Sony Pictures' film-plus-TV scope, nor to future Paramount reporting.
4. "Disney Entertainment segment ... Content Sales/Licensing within it": the sub-segment is titled "Content Sales/Licensing and Other" and includes stage plays, music and Industrial Light & Magic; the Entertainment segment as a whole is dominated by Linear Networks and DTC (DTC revenue 24,614 of 42,466 in FY2025), so Entertainment is not a studio comparator.
5. "same metric": the brief asks for "same metric, same window", but no two of the five peers file the same segment measure (see the metric note above), and fiscal windows differ (Disney September, Lionsgate March, others December).
6. Two of the five peers are parties to one pending transaction: WBD agreed on 2026-02-27 to be acquired by PSKY (verbatim in section 1). They may not be independent competitor rows going forward.

## Sources on disk
All filings saved as text under `peers_pictures/` (first two lines of each file carry the SEC URL and accession).
CIKs from `tools/sources.py:cik_for` (SEC company_tickers.json), 2026-09-13:
WBD 0001437107 · DIS 0001744489 · LION 0002052959 (Lionsgate Studios Corp.) · STRZ 0000929351 (STARZ ENTERTAINMENT CORP /CN/, former name LIONS GATE ENTERTAINMENT CORP /CN/) · PSKY 0002041610 (Paramount Skydance Corp) · CMCSA 0001166691.
Paramount Global CIK 0000813828 was taken from the SEC submissions JSON (it no longer carries a ticker in company_tickers.json).
**Brief defect found at CIK step:** `cik_for("PARA")` returns `0001826011 Banzai International, Inc.`, not Paramount. The ticker PARA has been reassigned. Paramount's successor filer is PSKY.

---
## 1. Warner Bros. Discovery (WBD), Studios segment

| FY (Dec) | Segment revenue $m | Segment Adjusted EBITDA $m | Adj. EBITDA margin | Studios operating income $m (MD&A reconciliation) | OI margin | Content amortization and impairment expense, Studios $m | as % of revenue |
|---|---|---|---|---|---|---|---|
| 2025 | 12,619 | 2,545 | 20.2% | 1,674 | 13.3% | 3,106 | 24.6% |
| 2024 | 11,607 | 1,652 | 14.2% | 529 | 4.6% | 5,692 | 49.0% |
| 2023 | 12,192 | 2,183 | 17.9% | 211 | 1.7% | 5,074 | 41.6% |

Margins computed by `peers_pictures/calc.py` (arithmetic only). Segment profit measure: **Adjusted EBITDA** (segment note). Operating income by segment is NOT in Note 23; it appears in the MD&A per-segment reconciliation table, which is where the OI column comes from.

Documents:
- 10-K FY2025, filed 2026-02-27, accession **0001437107-26-000020** (`WBD_10K_FY2025.txt`): revenue, Adj. EBITDA and content amortization for 2025, 2024, 2023 (Note 23); OI 2025 and 2024 (MD&A, Studios Segment table).
- 10-K FY2024, filed 2025-02-27, accession **0001437107-25-000031** (`WBD_10K_FY2024.txt`): OI 2023 = 211 (MD&A Studios Segment table). Cross-check: that filing shows 2023 revenue 12,192 and Adj. EBITDA 2,183, identical to the FY2025 filing.

Segment composition caveat (verbatim, FY2025 10-K Item 1): "WBD’s Studios segment includes the Warner Bros. Motion Picture Group (“WBMPG”), DC Studios, Warner Bros. Television Group (“WBTVG”), Consumer Products, Themed Entertainment and Brand Licensing, DC Comics Publishing, Content Licensing, Home Entertainment, Studio Operations, and Interactive Gaming."
Studios segment revenue includes inter-segment content licensing to WBD's own Streaming and networks; consolidated "Inter-segment eliminations | (3,857) | (2,782) | (2,269)" for 2025 | 2024 | 2023 (Note 23).

**Segment-measure definition, verbatim** (FY2025 10-K, Note 23 Reportable Segments):
> "The Company evaluates the operating performance of its segments based on financial measures such as revenues and Adjusted EBITDA. Adjusted EBITDA is defined as operating income excluding:
> •employee share-based compensation;
> •depreciation and amortization;
> •restructuring and facility consolidation;
> •certain impairment charges;
> •gains and losses on business and asset dispositions;
> •third-party transaction and integration costs;
> •amortization of purchase accounting fair value step-up for content;
> •amortization of capitalized interest for content; and
> •other items impacting comparability."

> "The accounting policies of the reportable segments are the same as the Company’s, except that certain inter-segment transactions that are eliminated for consolidation are not eliminated at the segment level. Inter-segment transactions primarily include advertising and content licenses. The Company generally records inter-segment transactions of content licenses at market value."

Content expense footnote (verbatim, Note 23): "(a) Content expense includes amortization, impairments, participations, residuals, development expense, and production costs, including talent costs, and is a component of costs of revenues. Content expense excludes content impairments and other development costs recorded in restructuring and other charges, amortization of purchase accounting fair value step-up for content, and amortization of capitalized interest for content as these items are excluded from the calculation of Adjusted EBITDA."
Studios "Content expense (a)" in the segment reconciliation: 7,108 (2025), 7,260 (2024), 7,112 (2023).

**Metric warning:** WBD's Adjusted EBITDA adds back D&A, SBC, restructuring, "certain impairment charges" and purchase-accounting content step-up. The gap to operating income is large (2023: Adj. EBITDA 2,183 vs OI 211; the largest 2023 reconciling item in the FY2024 10-K Studios table is "Impairment and amortization of fair value step-up for content | 96 | 995" for 2024 | 2023). It is not the same metric as operating income.

### WBD verbatim: hit-driven / unpredictable
FY2025 10-K, Item 1A (filed 2026-02-27, acc. 0001437107-26-000020):
> "The success of our business depends on the acceptance of our content and brands by our U.S. and international viewers, which may be unpredictable and volatile."

> "The production and distribution of television programs, feature films, sports and news content are inherently risky businesses because the revenue we derive and our ability to distribute our content depend primarily on consumer tastes and preferences that often change in unpredictable ways. [...] For example, generally, feature films that perform well upon initial release also have commercial success in subsequent distribution channels. Therefore, the underperformance of a feature film, especially an “event” film, i.e. one produced at higher cost and intended to reach a wider audience, upon its theatrical release can result in lower-than-expected revenues for our business which could limit our ability to create future content. We are required to make substantial investments in the production or acquisition and marketing of our television programs, feature films, sports and news content before we learn whether such content will reach anticipated levels of popularity with consumers."

FY2025 10-K, MD&A Studios Segment:
> "Fluctuations in results for our Studios segment may occur due to various factors, including (but not limited to) the timing and number of new film releases each quarter, the timing of marketing expenses recognized relative to (i.e., prior to) a film’s release, and the mix of content distributed each period."

Goodwill monitoring (FY2025 10-K, MD&A critical accounting estimates; the goodwill notes of the FY2025 and FY2024 10-Ks carry the same bullet with "the Company’s Studios reporting unit" in place of "our Studios reporting unit"):
> "•content licensing trends and volatility related to the performance of theatrical film and game slates in our Studios reporting unit; and"

FY2024 10-K (acc. 0001437107-25-000031), Note on goodwill:
> "The Studios reporting unit, which had headroom of 16%, and the Networks reporting unit, which had headroom of 12%, both had fair values in excess of carrying value of less than 20%."

### WBD verbatim: content impairments
FY2025 10-K, Note 9:
> "For the year ended December 31, 2025, total content impairments were $203 million."

> "For the year ended December 31, 2024, total content impairments were $558 million, of which content impairments and other content development costs and write-offs of $165 million were primarily due to the abandonment of certain titles in connection with the fourth quarter 2024 strategic realignment plan associated with the Warner Bros. Games group, and are reflected in restructuring and other charges in the Studios segment. (See Note 6.)"

> "For the year ended December 31, 2023, total content impairments were $326 million, of which content impairments and content development costs and write-offs of $115 million were primarily due to the abandonment of certain films in connection with the third quarter 2023 strategic realignment plan associated with the Warner Bros. Pictures Animation group and are reflected in restructuring and other charges in the Studios segment. (See Note 6.)"

FY2024 10-K, Note 9 (outside the window, context):
> "For the year ended December 31, 2022, total content impairments were $2,807 million. Content impairments of $2,756 million and content development write-offs of $377 million were due to the abandonment of certain content categories in connection with the strategic realignment of content following the Merger and are reflected in restructuring and other charges in the Studios, Networks and DTC segments. (See Note 6.)"

(These totals are company-wide, not Studios-only, except where the text attributes an amount to the Studios segment.)

### WBD structural context (verbatim, FY2025 10-K Item 1)
> "On February 27, 2026, the Company entered into an agreement and plan of merger, by and among the Company, PSKY and Prince Sub Inc., a wholly owned subsidiary of PSKY (“Merger Sub”) (as may be amended from time to time, the “PSKY Merger Agreement”), pursuant to which and subject to the terms and conditions therein, at the effective time, Merger Sub will merge with and into WBD, with WBD surviving as a wholly owned subsidiary of PSKY."

> "There can be no assurance that the PSKY Merger will occur in accordance with the expected plans or anticipated timeline, or at all."

Consequence for the row: two of the five peers (WBD and Paramount Skydance) are parties to a pending merger as of that filing. Status after 2026-02-27 NOT CHECKED here.

---
## 2. The Walt Disney Company (DIS), Entertainment segment and Content Sales/Licensing and Other

| FY (Sept/Oct year-end) | Entertainment revenue $m | Entertainment segment OI $m | margin | Content Sales/Licensing and Other revenue $m | CS/L&O operating income $m | margin | CS/L&O programming and production costs $m | as % of CS/L&O revenue | of which theatrical distribution revenue $m |
|---|---|---|---|---|---|---|---|---|---|
| FY2025 (ended 2025-09-27) | 42,466 | 4,674 | 11.0% | 8,488 | 392 | 4.6% | 4,260 | 50.2% | 2,592 |
| FY2024 (ended 2024-09-28) | 41,186 | 3,923 | 9.5% | 7,718 | 328 | 4.2% | 4,135 | 53.6% | 2,266 |
| FY2023 (ended 2023-09-30) | 40,635 | 1,444 | 3.6% | 9,048 | (179) | (2.0%) | 5,383 | 59.5% | 3,174 |

Entertainment segment "Programming and production costs" (segment note supplemental table): 22,273 (FY2025), 22,385 (FY2024), 23,912 (FY2023). This is the whole Entertainment segment (includes Linear Networks and DTC content), not film alone.
Margins computed by `peers_pictures/calc.py`. Segment profit measure: **segment operating income** (Disney's defined segment measure, which is NOT GAAP operating income: it excludes restructuring and impairment charges, among other things; see definition).

Documents:
- 10-K FY2025, filed 2025-11-13, accession **0001744489-25-000155** (`DIS_10K_FY2025.txt`): Entertainment revenue and segment OI FY2025/2024/2023 (Segment Information note); CS/L&O FY2025 and FY2024 (MD&A).
- 10-K FY2024, filed 2024-11-14, accession **0001744489-24-000276** (`DIS_10K_FY2024.txt`): CS/L&O FY2023 (MD&A table: revenue 9,048, "Operating Income (Loss) | $ | 328 | | $ | (179)"; programming and production costs (5,383)). Cross-check: FY2024 CS/L&O revenue 7,718 and OI 328 identical in both filings.
- Note on FY2024 vs FY2025 revenue lines: the FY2024 10-K splits "TV/VOD distribution" 2,255 and "Home entertainment distribution" 753; the FY2025 10-K combines them as "TV/VOD and home entertainment distribution" 3,008 for FY2024. Same total.
- A 10-K/A for FY2023 exists (filed 2024-01-24, acc. 0001744489-24-000064); NOT READ, as FY2023 figures were taken from the FY2024 and FY2025 10-Ks.

Segment composition caveat: CS/L&O is the closest Disney analogue to a film studio line but includes stage plays, music and Industrial Light & Magic. Verbatim (FY2025 10-K Item 1): "The majority of Content Sales/Licensing revenue is derived from distribution in the theatrical, TV/VOD and home entertainment windows. In addition, revenue is generated from music distribution, stage plays and post-production services through Industrial Light & Magic and Skywalker Sound." Also: "The Company also publishes National Geographic magazine, which is reported with Content Sales/Licensing."
Disney films also feed Disney+ and Hulu (the DTC line), so CS/L&O captures only the external/window sales of the studio output. The FY2025 10-K refers to "imputed license fees for content that is used on our DTC streaming services" in Ultimate Revenues estimates (critical accounting policies).

**Segment-measure definition, verbatim** (FY2025 10-K, Note 1 Segment Information):
> "Our operating segments report separate financial information, including segment revenues and operating income, which is evaluated regularly by the Chief Executive Officer, the Chief Operating Decision Maker (CODM), to allocate resources and to assess performance by monitoring results against those set out in our planning processes."

> "Segment operating results reflect earnings before corporate and unallocated shared expenses, restructuring and impairment charges, net other income, net interest expense, income taxes and noncontrolling interests. Segment operating income generally includes equity in the income of investees, except for our India joint venture, and acquisition accounting amortization of TFCF Corporation (TFCF) and Hulu assets (i.e. intangible assets and the fair value step-up for film and episodic costs) recognized in connection with the TFCF acquisition in fiscal 2019 (TFCF and Hulu Acquisition Amortization)."

(Text-extraction note: in the filing the sentence breaks across a page boundary between "recognized in" and "connection with", with page number "78" and "TABLE OF CONTENTS" in between. Joined here; nothing omitted except the page furniture.)

Reading of that sentence, checked against the raw HTML of the filing (no word dropped by extraction): the "except for" governs both the India joint venture AND the TFCF/Hulu acquisition amortization, i.e. that amortization is EXCLUDED from segment OI. Evidence, FY2025 10-K reconciliation of segment operating income to income before income taxes: "TFCF and Hulu acquisition amortization(3) | (1,576) | | (1,677) | | (1,998)" for FY2025 | FY2024 | FY2023 is a reconciling item below segment OI, of which "Step-up of film and episodic costs | 260 | 271 | 439". The same reconciliation shows "Restructuring and impairment charges(1) | (819) | | (3,595) | | (3,836)" below segment OI.

**Metric warning:** Disney segment OI is closer to operating income than WBD's or Comcast's Adjusted EBITDA (it is after depreciation and amortization: CS/L&O "Depreciation and amortization | (367) | | (371)" FY2025 | FY2024), but it excludes restructuring and impairment charges, including content impairments, which are booked outside the segment.

### Disney verbatim: hit-driven / unpredictable
FY2025 10-K (filed 2025-11-13, acc. 0001744489-25-000155), Item 1A:
> "Our businesses create entertainment, travel and consumer products, the success of which depends substantially on consumer tastes and preferences that change in often unpredictable ways. The success of our businesses depends on our ability to consistently produce compelling creative content, which may be distributed, among other ways, through DTC services, linear networks and theaters and used in theme park attractions, hotels and other resort facilities and travel experiences and consumer products. [...] Demand for certain out-of-home entertainment experiences, such as theater-going to watch movies, has not returned to levels that existed prior to the COVID-19 pandemic. [...] Moreover, we must often make substantial investments in content production and acquisition, acquisition of sports and other programming rights, theme park attractions, cruise ships or hotels and other facilities or customer facing platforms before we know the extent to which these products will earn consumer acceptance, and the market, economic or social conditions are sometimes significantly different from the ones we anticipated at the time of the investment decisions."

FY2025 10-K, Item 1 (Competition and Seasonality):
> "The operating results of Content Sales/Licensing fluctuate due to the timing and performance of releases in the theatrical, home entertainment and television markets. Release dates are determined by several factors, including competition and the timing of vacation and holiday periods."

FY2025 10-K, Critical Accounting Policies:
> "With respect to produced films intended for theatrical release, the most sensitive factor affecting our estimate of Ultimate Revenues is theatrical performance. Revenues derived from other markets subsequent to the theatrical release are generally highly correlated with theatrical performance. Theatrical performance varies primarily based upon the public interest and demand for a particular film, the popularity of competing films at the time of release and the level of marketing effort."

FY2024 10-K (acc. 0001744489-24-000276), MD&A CS/L&O:
> "Operating results from Content Sales/Licensing and Other increased $507 million, to income of $328 million from a loss of $179 million due to higher theatrical distribution results."

### Disney verbatim: content / film cost impairments
FY2025 10-K, MD&A CS/L&O:
> "Operating income increased $64 million, to $392 million from $328 million due to lower film cost impairments and higher TV/VOD and home entertainment distribution results, partially offset by a decrease in theatrical distribution results."

FY2025 10-K, Items Excluded from Segment Operating Income Related to Entertainment, footnote (2):
> "Fiscal 2025 includes $635 million for impairments of equity investments and $109 million for content impairments. Fiscal 2024 includes $1,287 million for goodwill impairments related to our general entertainment linear networks, $187 million for content impairments, $158 million for impairment of an equity investment and $38 million of severance."

FY2024 10-K, same table, footnote (1):
> "Fiscal 2023 includes $2,521 million for content impairments (net of the A+E gain), $425 million for a goodwill impairment related to our general entertainment linear networks, $248 million of severance, a $141 million impairment of an equity investment and $96 million of charges primarily related to exiting our businesses in Russia."

FY2024 10-K, MD&A CS/L&O:
> "The decrease in programming and production costs was due to lower production cost amortization attributable to the decreases in theatrical and TV/VOD distribution revenues, partially offset by higher film cost impairments."

(Note: "film cost impairments" referenced inside CS/L&O operating expenses are INSIDE segment OI; the "content impairments" in the Restructuring and impairment charges footnotes are OUTSIDE segment OI. The filing does not quantify the in-segment film cost impairments in the text read.)

---
## 3. Lionsgate Studios Corp. (LION), Motion Picture and Television Production segments

Filer: Lionsgate Studios Corp., CIK 0002052959. Its predecessor Lions Gate Entertainment Corp. (CIK 0000929351) is now named STARZ ENTERTAINMENT CORP /CN/ after the Starz separation. The FY2026 10-K treats Old Lionsgate as the accounting predecessor, so the three-year segment history is continuous.

| FY (ended Mar 31) | Motion Picture revenue $m | MP segment profit $m | MP margin | Television Production revenue $m | TV segment profit $m | TV margin | Total Studio Business revenue (before intersegment elim.) $m | Studio Business segment profit $m | margin |
|---|---|---|---|---|---|---|---|---|---|
| FY2026 | 1,617.1 | 278.9 | 17.2% | 1,044.6 | 124.5 | 11.9% | 2,661.7 | 403.4 | 15.2% |
| FY2025 | 1,598.6 | 304.3 | 19.0% | 1,605.8 | 136.5 | 8.5% | 3,204.4 | 440.8 | 13.8% |
| FY2024 | 1,666.0 | 312.4 | 18.8% | 1,330.1 | 146.8 | 11.0% | 2,996.1 | 459.2 | 15.3% |

Film cost data:
| FY | MP direct operating expense $m (includes film amortization and in-segment impairments) | as % MP revenue | Company-wide amortization of investment in film and TV programs $m | as % consolidated revenue ($m) | Film/TV impairments in MP direct operating expense $m | in TV Production $m | impairments outside segment (restructuring) $m |
|---|---|---|---|---|---|---|---|
| FY2026 | 797.6 | 49.3% | 1,022.6 | 38.9% (2,631.8) | 0.8 | 1.4 | 13.2 |
| FY2025 | 830.7 | 52.0% | 1,172.7 | 45.4% (2,584.7) | 19.7 | 6.7 | 7.2 |
| FY2024 | 807.1 | 48.4% | 929.8 | 37.9% (2,450.2) | 34.6 | 8.4 | 12.8 |

Consolidated operating income (loss), for reference: 97.1 (FY2026), (18.1) (FY2025), (14.5) (FY2024) (Note 16 reconciliation).
Margins computed by `peers_pictures/calc.py`. Segment profit measure: **segment profit** (gross contribution less segment G&A).

Documents:
- 10-K FY2026 (year ended 2026-03-31), filed 2026-05-27, accession **0002052959-26-000049** (`LION_10K_FY2026.txt`): all three years, Note 16 segment table and reconciliation; Note 4 amortization and impairments.
- 10-K FY2025, filed 2025-05-30, accession **0002052959-25-000010** (`LION_10K_FY2025.txt`): cross-check. That filing shows Motion Picture revenue "$ | 1,589.7 | $ | 1,656.3" and segment profit "$ | 307.6 | $ | 319.4" for FY2025 | FY2024. The FY2026 10-K recast adds the India streaming platform: 1,589.7 + 8.9 = 1,598.6 and 307.6 less 3.3 = 304.3 (FY2025); 1,656.3 + 9.7 = 1,666.0 and 319.4 less 7.0 = 312.4 (FY2024). Reconciles exactly to the recast footnote.
- A 10-K/A for FY2025 exists (filed 2025-07-29, acc. 0001193125-25-167991); NOT READ (likely Part III only; not verified).

Recast footnote (verbatim, FY2026 10-K Note 16): "(1) During the first quarter of fiscal 2026, the Company began reflecting the results of operations of its streaming platform in India within the Motion Picture segment as such operations are not a part of the disposal group of the Starz Business. Accordingly, the following amounts were reclassified from the former Media Networks segment to the Motion Picture segment in the years ended March 31, 2025 and 2024 to conform to the current period presentation: (i) revenue of $8.9 million and $9.7 million, respectively; [...] which resulted in gross contribution loss of $0.3 million and $4.3 million, respectively and segment loss of $3.3 million and $7.0 million, respectively. Additionally, the Company sold its streaming platform in India in December 2025."

Intersegment caveat: in FY2025 and FY2024, a large part of Lionsgate's segment revenue was sold to Starz (then consolidated): "Intersegment revenues | Studio Business: | Motion Picture | 3.1 | 203.3 | 128.2 | Television Production | 26.8 | 416.4 | 417.7" (FY2026 | FY2025 | FY2024). FY2026 segment revenue is therefore less inflated by internal sales than the prior years.

**Segment-measure definition, verbatim** (FY2026 10-K, Note 16):
> "The Company’s primary measure of segment performance is its Studio Business segment profit. Segment profit is defined as gross contribution (segment revenues, less segment direct operating and segment distribution and marketing expense) less segment general and administration expenses. Segment profit excludes, when applicable, corporate general and administrative expense, restructuring and other costs, share-based compensation, certain content charges as a result of changes in management and/or content strategy, certain benefits or expenses related to the COVID-19 global pandemic, unallocated rent cost and purchase accounting and related adjustments."

**Metric warning:** Lionsgate segment profit includes film cost amortization (in direct operating expense: "Amortization of investment in film and television programs [...] was included in direct operating expense") but excludes depreciation and amortization of other assets ("Adjusted depreciation and amortization" is a reconciling item below segment profit), SBC, corporate G&A and restructuring (including restructuring-related content write-downs). It is an EBITDA-like contribution measure, not operating income.

### Lionsgate verbatim: hit-driven / unpredictable
FY2026 10-K (filed 2026-05-27, acc. 0002052959-26-000049), Item 1A:
> "Lionsgate’s results of operations depend significantly on the commercial success of the motion picture, television and other content that it sells, licenses or distributes, the performance of which cannot be predicted with certainty. Viewer preferences and audience acceptance are difficult to predict and may be influenced by numerous factors beyond Lionsgate’s control, including critical reception, the format in which content is released, the talent involved, genre and subject matter, audience response, the quality and volume of content released by competitors, the availability of alternative forms of entertainment (including user-generated content), general economic conditions and other tangible and intangible factors."

> "Lionsgate’s results may be affected by the performance of a limited number of content releases in any given period."

> "Lionsgate’s operating results in any period may depend significantly on the performance of a limited number of motion pictures or television programs released or licensed during that period. As a result, the underperformance of one or more projects, whether due to audience reception, critical response, competitive releases, marketing execution, timing, or other factors, could have an adverse effect on Lionsgate’s revenues, operating results and profitability for that period."

> "This concentration risk may be exacerbated by the high upfront capital investment required to produce or acquire content and the inherent unpredictability of audience preferences. Losses or lower‑than‑expected returns from projects may not be offset by the performance of other content within the same period or fiscal year, and the impact of underperformance may extend beyond the initial release window."

FY2026 10-K, Item 1 (Competition):
> "In addition, our motion pictures compete for audience acceptance and exhibition outlets with films produced and distributed by other companies, while our television product competes with content distributed by both independent producers and major studios. As a result, the success of our motion picture and television businesses depend not only on the quality and acceptance of a particular film or program, but also on the quantity, quality and timing of competing content released into the marketplace, as well as our ability to license and produce content for networks and platforms at levels sufficient to generate satisfactory viewership and subscriber demand."

FY2026 10-K, Critical Accounting Estimates:
> "Due to the inherent uncertainties involved in making such estimates of ultimate revenues and expenses, these estimates have differed in the past from actual results and are likely to differ to some extent in the future from actual results. In addition, in the normal course of our business, some films and titles are more successful or less successful than anticipated."

### Lionsgate verbatim: film / content impairments
FY2026 10-K, Item 1A:
> "Lionsgate may incur significant write-offs if its projects do not perform well enough to recover costs."

> "If, in any reporting period, Lionsgate revises downward its estimates of total anticipated revenues for a film or other project or revises upward its estimated production or distribution costs, Lionsgate may be required to accelerate amortization or record impairment charges with respect to the remaining unamortized costs, even if impairment charges were previously recorded for that project. These write‑offs or impairment charges could be significant and could have a materially adverse effect on Lionsgate’s business, financial condition, operating results, liquidity and prospects."

> "In addition, low viewership for television programming produced by Lionsgate may result in the cancellation or non-renewal of a program, which could lead to significant programming impairments in a given period, and reduced license fees or other revenues in future periods."

FY2026 10-K, Note 4:
> "Amortization of investment in film and television programs was $1,022.6 million, $1,172.7 million and $929.8 million for the years ended March 31, 2026, 2025 and 2024, respectively, and was included in direct operating expense in the consolidated statements of operations."

> "(2)Impairments included in restructuring and other represent write-downs in connection with the restructuring of the Motion Picture and Television Production businesses. See Note 16 for further information."

FY2026 10-K, MD&A Motion Picture:
> "In fiscal 2026, a write-down of $0.8 million was recorded for investments in film included in the Motion Picture segment direct operating expense, as compared to $19.7 million in fiscal 2025."

FY2026 10-K, auditor critical audit matter ("Pre-release Film Impairments"):
> "Auditing the Company’s impairment evaluation for theatrical films prior to release is challenging and subjective as the key assumptions in the analysis include estimates of future anticipated revenues and box office performance, which may differ from future actual results."

(Text-extraction note: the last quote is the first sentence of the CAM paragraph as extracted; the table-cell separators in the text file were removed.)

---
## 4. Paramount Skydance Corp. (PSKY; predecessor Paramount Global), Filmed Entertainment segment

Which entity files: Paramount Skydance Corp., CIK 0002041610 (former name New Pluto Global, Inc.), filed the FY2025 10-K. Paramount Global (CIK 0000813828, former names ViacomCBS Inc., CBS CORP, VIACOM INC) filed through FY2024. The FY2025 10-K presents Paramount Global as **Predecessor** (to 2025-08-06) and PSKY as **Successor** (from 2025-08-07), with pushdown of the "Ultimate Parent's basis" at 2025-08-07. 2025 is therefore two periods on different accounting bases, shown separately below. No full-year 2025 segment Adjusted OIBDA is filed; the filing supplies only a pro forma full-year REVENUE.

| Period | Filmed Entertainment revenue $m | FE Adjusted OIBDA $m | margin | FE content costs $m | as % of revenue | of which Theatrical revenue $m |
|---|---|---|---|---|---|---|
| 2025-08-07 to 2025-12-31 (Successor) | 1,736 | (132) | (7.6%) | 1,287 | 74.1% | 154 |
| 2025-01-01 to 2025-08-06 (Predecessor) | 1,593 | (100) | (6.3%) | 846 | 53.1% | 475 |
| FY2025 Supplemental Pro Forma (filed; revenue only, includes pro forma Skydance adjustments) | 3,832 | NOT FILED | n/a | NOT FILED | n/a | 629 |
| FY2024 (Predecessor) | 2,955 | (96) | (3.2%) | 1,496 | 50.6% | 813 |
| FY2023 (Predecessor) | 2,957 | (119) | (4.0%) | 1,545 | 52.2% | 813 |
| FY2022 (context, outside window) | 3,706 | 272 | n/a | 1,924 | n/a | NOT PULLED |

Margins computed by `peers_pictures/calc.py`. Segment profit measure: **Adjusted OIBDA**. No segment operating income is filed.
Successor-period content costs reflect the pushdown revaluation of programming assets, so the 74.1% is not comparable to the Predecessor periods. Verbatim (FY2025 10-K MD&A): "Content costs for the Successor period include costs associated with Skydance’s content, and also reflect reductions in programming assets resulting from the pushdown of the Ultimate Parent’s basis. Programming assets decreased for our Direct-to-Consumer and TV Media segments and increased for our Filmed Entertainment segment as a result of the pushdown." So Filmed Entertainment's Successor content costs carry amortization of a written-UP film asset base.

Documents:
- 10-K FY2025, filed 2026-02-25, accession **0002041610-26-000011** (`PSKY_10K_FY2025.txt`): Note 17 segment table, Successor 2025, Predecessor 2025, 2024, 2023; MD&A Supplemental Pro Forma Revenues.
- 10-K/A FY2025, filed 2026-04-24, accession 0001140361-26-016758 (`PSKY_10KA_FY2025.txt`): READ the purpose paragraph only; it amends "Part III, Items 10, 11, 12, 13 and 14" and "does not otherwise change, modify or update the disclosures in, or exhibits to, the Initial Form 10-K."
- Paramount Global 10-K FY2024, filed 2025-02-26, accession **0000813828-25-000005** (`PARA_10K_FY2024.txt`): cross-check. Note 17 shows "Filmed Entertainment Adjusted OIBDA | (96) | (119) | 272" and revenues "2,955 | 2,957 | 3,706" for 2024 | 2023 | 2022. 2024 and 2023 identical to the PSKY 10-K.

Segment composition (verbatim, FY2025 10-K Note 17): "•Filmed Entertainment—In 2025, our Filmed Entertainment segment included Paramount Pictures, Paramount Players, Paramount Animation, Nickelodeon Studio, and Miramax, and during the Successor period also included Skydance’s animation, interactive/games, and sports divisions."
Television studios (CBS Studios, Paramount Television Studios) sat in TV Media, not Filmed Entertainment. Resegmentation (verbatim, same note): "In the first quarter of 2026, we transitioned our reporting structure into three new segments: Studios, Direct-to-Consumer, and TV Media. Under this structure, our new Studios segment will reflect the combination of the historical Filmed Entertainment segment with TV Media studio operations, consolidating our content creation activities." The 2026 10-Qs under the new Studios segment were NOT PULLED (outside the brief's 10-K window).

Intersegment licensing treatment (verbatim, Note 17): "For content that is licensed between segments, content costs are allocated across segments based on the relative value of the distribution windows within each segment. Accordingly, no intersegment licensing revenues or profits are recorded by the licensor segment." This differs from WBD, whose Studios segment records inter-segment content licenses "at market value". Paramount's Filmed Entertainment therefore gets no revenue for films that go to Paramount+; WBD Studios does.

**Segment-measure definition, verbatim** (FY2025 10-K, Note 17):
> "We present operating income excluding depreciation and amortization, stock-based compensation, programming charges, impairment charges, restructuring charges, transaction-related items, other corporate matters, and gain on dispositions, each where applicable (“Adjusted OIBDA”), as the primary measure of profit and loss for our operating segments in accordance with FASB guidance for segment reporting. Programming charges consist only of charges related to major strategic changes (see Note 4), and do not include impairment charges that occur as part of our normal operations, which are recorded within content costs in the tables below, where applicable, and are not excluded in Adjusted OIBDA."

Content costs definition (verbatim, FY2025 10-K MD&A): "Content costs include the amortization of costs of internally-produced television content, theatrical film content, and interactive game development; amortization of acquired program rights; other television production costs, including on-air talent; and participation and residuals expenses, which reflect amounts owed to talent and other participants in our content pursuant to contractual and collective bargaining arrangements."

**Metric warning:** Adjusted OIBDA is an EBITDA-type measure. It includes film cost amortization and ordinary-course content impairments (inside content costs) but excludes D&A of other assets, SBC, restructuring and "programming charges" tied to "major strategic changes". Filmed Entertainment Adjusted OIBDA was negative in every period in the 2023-2025 window, even on this favorable measure.

### Paramount verbatim: hit-driven / unpredictable
FY2025 10-K (PSKY, filed 2026-02-25, acc. 0002041610-26-000011), Item 1A:
> "The unpredictable and constantly shifting nature of consumer behavior, as well as evolving technologies and distribution models, have affected, and could continue to adversely affect, our business, financial condition or results of operations."

> "Our ability to maintain attractive brands and to create, distribute and/or license popular content is key to our success and ability to generate revenues. The revenues we generate primarily depend on our ability to consistently anticipate and satisfy consumer tastes and expectations in the U.S. and internationally. Consumer tastes and behavior change frequently, and it is a challenge to anticipate what will resonate with audiences at any given time. The popularity of our original and acquired content is affected by our ability to target key audiences; the quality and attractiveness of competing content; and the availability and popularity of alternative forms of entertainment and leisure activities, general economic conditions and other tangible and intangible factors, all of which can be unpredictable."

FY2025 10-K, Critical Accounting Policies:
> "For films intended for theatrical release, we believe the performance during the theatrical exhibition is the most sensitive factor affecting our estimate of Ultimate Revenues as subsequent markets have historically exhibited a high correlation to theatrical performance."

FY2025 10-K, MD&A Filmed Entertainment:
> "Adjusted OIBDA in each of the periods reflects the impact from recent theatrical releases."

Paramount Global FY2024 10-K (filed 2025-02-26, acc. 0000813828-25-000005), MD&A Filmed Entertainment:
> "Fluctuations in results for the Filmed Entertainment segment may occur as a result of the timing of the recognition of distribution costs, including marketing costs, which are generally incurred before and throughout the theatrical release of a film, while the revenues for the respective film are recognized as earned through the film’s theatrical exhibition and distribution to other platforms."

> "Adjusted OIBDA improved by $23 million, driven by the comparison against the costs incurred during the labor strikes and to resume film production in 2023, as well as higher profits from studio rental and production services in 2024. The impact from these items was partially offset by lower profits from recent theatrical releases, including from the timing of their release."

### Paramount verbatim: content impairments / programming charges
FY2025 10-K, Note 4 (Programming Charges):
> "During the fourth quarter of 2025, in connection with a review of our content portfolio following the closing of the Transactions, we decided to abandon certain Skydance content, principally development projects. As a result, we recorded programming charges totaling $41 million associated with this abandonment."

> "Programming charges in the Predecessor periods totaling $1.12 billion in 2024 and $2.37 billion in 2023 were the result of major changes in content strategy associated with the integration of certain product offerings and a shift to a global programming strategy. These changes resulted in the removal of significant levels of content from our platforms, abandonment of development projects, and termination of programming agreements, particularly internationally, including locally-produced content and domestic titles that no longer aligned with a shift to a global programming strategy. [...] The 2024 programming charges were comprised of $909 million for the impairment of content to its estimated fair value, as well as $209 million for development cost write-offs and contract termination costs. The 2023 programming charges were comprised of $1.97 billion for the impairment of content to its estimated fair value and $402 million for development cost write-offs and contract termination costs."

(These programming charges are company-wide and principally streaming/TV content strategy; their allocation to Filmed Entertainment was NOT FOUND in the text read. They are excluded from segment Adjusted OIBDA.)

FY2025 10-K, Critical Accounting Policies:
> "For content that is predominantly monetized on an individual basis, a television program or feature film is tested for impairment when events or circumstances indicate that its fair value may be less than its unamortized cost. [...] In addition, unamortized costs for internally-produced or licensed programming that has been abandoned are written off."

---
## 5. Comcast (CMCSA), Studios segment (NBCUniversal and Sky film and television studios)

| FY (Dec) | Studios revenue $m | of which intersegment (mostly licenses to Comcast Media/Peacock) $m | share | Theatrical revenue $m | Content licensing revenue $m | Segment Adjusted EBITDA $m | margin | Programming and production $m | as % of revenue | Marketing and promotion $m |
|---|---|---|---|---|---|---|---|---|---|---|
| 2025 | 11,286 | 3,205 | 28.4% | 1,621 | 8,199 | 1,099 | 9.7% | 7,441 | 65.9% | 1,773 |
| 2024 | 11,092 | 3,259 | 29.4% | 1,693 | 8,063 | 1,404 | 12.7% | 7,257 | 65.4% | 1,483 |
| 2023 | 11,625 | 3,317 | 28.5% | 2,079 | 8,231 | 1,269 | 10.9% | 7,958 | 68.5% | 1,579 |

Margins and shares computed by `peers_pictures/calc.py`. Segment profit measure: **Adjusted EBITDA**. No Studios segment operating income is filed (D&A is reconciled only in total: "Depreciation | (9,327)" and "Amortization | (6,884)" for 2025).
Company-wide (not Studios-only) amortization of owned content, Note 4: "(a) Amount includes amortization of owned content of $8.0 billion, $7.8 billion and $7.8 billion for the year ended December 31, 2025, 2024 and 2023, respectively, as well as participations and residuals expenses." A Studios-only film cost amortization figure was NOT FOUND in the 10-K.

Documents:
- 10-K FY2025, filed 2026-02-03, accession **0001628280-26-004994** (`CMCSA_10K_FY2025.txt`): Note 2 segment tables for 2025, 2024, 2023; Note 3 Studios revenue by type for all three years; MD&A Studios table 2025 and 2024.
- 10-K FY2024, filed 2025-01-31, accession **0001166691-25-000011** (`CMCSA_10K_FY2024.txt`): cross-check. MD&A Studios table: revenue "11,092 | 11,625", Adjusted EBITDA "$ | 1,404 | $ | 1,269", programming and production "7,257 | 7,958" for 2024 | 2023. Identical to the FY2025 10-K.
- Arithmetic check of the Note 2 column read (the text extraction drops empty cells): Studios 2025 revenue 11,286 less programming and production 7,441, marketing and promotion 1,773 and other 973 = 1,099, equal to the filed Adjusted EBITDA. 2024 and 2023 recompute to 1,405 and 1,270 against filed 1,404 and 1,269 (rounding in the filed components).

Segment composition (verbatim, FY2025 10-K Item 1): "Our Studios segment primarily includes our NBCUniversal and Sky film and television studio production and distribution operations."
Intersegment treatment (verbatim, Note 2 footnote (a)): "Revenue for licenses of content from Studios to Media is generally recognized at a point in time, consistent with the recognition of transactions with third parties, when the content is delivered and made available for use. The costs of these licenses in Media are recognized as the content is used over the license period. The difference in timing of recognition between segments results in an Adjusted EBITDA impact in eliminations, as the profits (losses) on these transactions are deferred in our consolidated results and recognized as the content is used over the license period." And: "Transactions between our segments generally include intercompany profit consistent with third-party transactions."

**Segment-measure definition, verbatim** (FY2025 10-K):
Note 2 footnote (e): "We use Adjusted EBITDA as the measure of profit or loss for our segments. For each of our segments, our chief operating decision maker uses Adjusted EBITDA to measure operational strength and performance, assist in the evaluation of underlying trends, and allocate resources in the annual budget and forecasting process. Adjusted EBITDA is also a significant performance measure in our annual incentive compensation programs. From time to time we may report the impact of certain events, gains, losses or other charges related to our segments within Corporate and other."

MD&A Non-GAAP Financial Measures: "We define Adjusted EBITDA as net income attributable to Comcast Corporation before net income (loss) attributable to noncontrolling interests, income tax expense, investment and other income (loss), net, interest expense, depreciation and amortization expense, and other operating gains and losses (such as impairment charges related to fixed and intangible assets and gains or losses on the sale of long-lived assets), if any. From time to time, we may exclude from Adjusted EBITDA the impact of certain events, gains, losses or other charges (such as significant legal settlements) that affect the period-to-period comparability of our operating performance."

Programming and production cost content (verbatim, MD&A Studios): "Programming and production costs primarily consists of the amortization of capitalized film and television production and acquisition costs; participations and residuals expenses; and distribution expenses."
Where content impairments sit (verbatim, Note 4): "We record charges related to impairments or content that is substantively abandoned to programming and production costs." So film impairments are INSIDE Studios Adjusted EBITDA for Comcast (unlike WBD, Disney and Paramount, which exclude some or all content impairments from their segment measures).

**Metric warning:** Comcast Adjusted EBITDA is before D&A (excluding film cost amortization, which stays in programming and production). It is not operating income. It is the most inclusive of the four EBITDA-type measures on content write-downs (all content impairments are inside), but it excludes the "Media, Studios and Theme Parks headquarters and other" overhead ((1,095) in 2025), which is not allocated to Studios.

### Comcast verbatim: hit-driven / unpredictable
FY2025 10-K (filed 2026-02-03, acc. 0001628280-26-004994), Item 1A:
> "Our success depends on consumer acceptance of our content, and our businesses may be adversely affected if our content fails to achieve sufficient consumer acceptance."

> "We create and acquire media, sports and entertainment content, the success of which depends substantially on consumer tastes and preferences that often change in unpredictable ways. To meet the changing preferences of our consumer markets, we must consistently create, acquire, market and distribute a broad array of content and theme park attractions. We have invested, and will continue to invest, substantial amounts in content, such as sports rights, the production of films and original content for television networks and streaming services, and in the creation of new theme parks and theme park attractions, before learning the extent to which they will earn consumer acceptance."

FY2025 10-K, Item 1 (Competition, Studios):
> "Our film and television studios compete for audiences with other major film and television studios, independent film producers and creators of content, as well as with alternative forms of entertainment. The competitive position of our studios primarily depends on the number of films and television series and episodes produced, their distribution and marketing success, and consumer response."

FY2025 10-K, Item 1 (Seasonality and Cyclicality):
> "Revenue in Studios fluctuates due to the timing, nature and number of films released in movie theaters, through DTC streaming services and viewing on demand, and on physical and digital home entertainment products. [...] We incur significant marketing expenses before and throughout the release of a film in movie theaters and as a result, we typically incur losses on a film prior to and during the film’s exhibition in movie theaters."

FY2025 10-K, Critical Accounting Estimates:
> "The most sensitive factor affecting our estimate of ultimate revenue for a film intended for theatrical release is the film’s theatrical performance, as subsequent revenue from the licensing and sale of a film has historically exhibited a high correlation to its theatrical performance."

### Comcast verbatim: film / content impairments
FY2025 10-K, Critical Accounting Estimates:
> "Capitalized film and television costs are subject to impairment testing when certain triggering events are identified. [...] Impairments of capitalized film and television costs were not material in any of the periods presented."

FY2025 10-K, Note 4:
> "Estimates of ultimate revenue and total costs are based on anticipated release patterns and distribution strategies, public acceptance and historical results for similar productions."


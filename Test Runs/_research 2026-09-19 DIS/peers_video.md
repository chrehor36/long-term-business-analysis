# DIS run — competitor row, video / streaming peers
**Gathered 2026-09-19. Source rule: SEC EDGAR primary documents only** (10-K, 10-Q, 8-K EX-99.1).
No aggregators, no press, no encyclopaedias. Every figure carries document, period and accession number.
Verbatim quotes are marked with `>` and carry their accession.

**Gathering only. No verdict, no moat conclusion — per the brief.**

**Registrants and CIKs confirmed from `https://www.sec.gov/files/company_tickers.json` and
`https://data.sec.gov/submissions/CIK##########.json`:**

| Ticker | Registrant name as filed | CIK | Latest 10-K accession | Period |
|---|---|---|---|---|
| NFLX | NETFLIX INC | 0001065280 | 0001065280-26-000034 | FY ended 2025-12-31 |
| CMCSA | COMCAST CORP | 0001166691 | 0001628280-26-004994 | FY ended 2025-12-31 |
| WBD | Warner Bros. Discovery, Inc. | 0001437107 | 0001437107-26-000020 | FY ended 2025-12-31 |
| PSKY | Paramount Skydance Corp | 0002041610 | 0002041610-26-000011 | FY ended 2025-12-31 |
| (pre-merger) | Paramount Global | 0000813828 | 0000813828-25-000005 | FY ended 2024-12-31 |
| AAPL | Apple Inc. | 0000320193 | 0000320193-25-000079 | FY ended 2025-09-27 |
| AMZN | AMAZON COM INC | 0001018724 | 0001018724-26-000004 | FY ended 2025-12-31 |

**CIK note — PARA.** The ticker symbol `PARA` in the SEC's own company-tickers file now maps to
**Banzai International, Inc. (CIK 0001826011)**, an unrelated registrant. The Paramount filer chain is
**Paramount Global, CIK 0000813828** (last 10-K: FY2024, accession 0000813828-25-000005; a 10-K/A
followed on 2025-04-25, accession 0001193125-25-096776) and then **Paramount Skydance Corp, CIK
0002041610**, whose FY2025 10-K (accession 0002041610-26-000011) is its **first** annual report.
Do not resolve Paramount by ticker.

---

## 1. NFLX — Netflix, Inc.
**Document read:** Form 10-K for the fiscal year ended December 31, 2025, filed 2026-01-23,
**accession 0001065280-26-000034**, primary document `nflx-20251231.htm`.
All figures **in thousands of USD** as filed (Netflix reports in thousands, not millions).

### Three-year figures

| Item | FY2025 | FY2024 | FY2023 | Where in the filing |
|---|---|---|---|---|
| Streaming revenues | 45,183,036 | 39,000,966 | 33,640,458 | MD&A "Financial Results"; Consolidated Statements of Operations |
| DVD revenues | — | — | 82,839 | same table (service discontinued in FY2023) |
| **Total revenues** | **45,183,036** | **39,000,966** | **33,723,297** | Consolidated Statements of Operations |
| Cost of revenues | 23,275,329 | 21,038,464 | 19,715,368 | MD&A "Cost of Revenues" |
| Cost of revenues as % of revenues (as filed) | 52% | 54% | 58% | same |
| **Operating income** | **13,326,603** | **10,417,614** | **6,954,003** | Consolidated Statements of Operations |
| **Operating margin (as filed)** | **29.5%** | **26.7%** | **20.6%** | MD&A "Financial Results" — the filer states the margin itself |
| Net income | 10,981,201 | 8,711,631 | 5,407,990 | Consolidated Statements of Operations |
| **Additions to content assets** (content cash spend) | **(17,096,617)** | **(16,223,617)** | **(12,554,703)** | Consolidated Statements of Cash Flows, operating section |
| Change in content liabilities | (610,838) | (779,135) | (585,602) | same |
| **Amortization of content assets** | **16,422,166** | **15,301,517** | **14,197,437** | same |
| Stock-based compensation expense | 368,449 | 272,588 | 339,368 | Cash-flow statement; agrees to the Statements of Stockholders' Equity |
| Net cash provided by operating activities | 10,149,273 | 7,361,364 | 7,274,301 | Consolidated Statements of Cash Flows |
| Purchases of property and equipment | (688,220) | (439,538) | (348,552) | investing section |
| **Free cash flow — COMPUTED, not filed** (OCF less purchases of PP&E) | **9,461,053** | **6,921,826** | **6,925,749** | my arithmetic from the two filed lines above |

**Cross-check per operator rule 4:** MD&A "Financial Results" total revenues of \$45,183,036 thousand for
FY2025 ties to the Consolidated Statements of Operations revenue line in Item 8 of the same document, and
the FY2025 net income of \$10,981,201 thousand ties across the Statements of Operations, the Statements of
Stockholders' Equity and the Statements of Cash Flows.

**FCF caveat.** The FY2025 10-K does **not** present a free-cash-flow figure or a free-cash-flow
reconciliation. The only non-GAAP measure reconciled in the document is constant-currency revenue.
"Free cash flow" appears in the filing solely as forward-looking-statement and risk-factor language
(e.g. "our membership acquisition and retention, revenues, operating income, net income, net cash provided
by operating activities and free cash flow"). The FCF row above is therefore **my computation**, labelled.

### Memberships and ARPU — DISCONTINUED. The latest 10-K omits both.
Netflix stopped reporting membership counts and per-membership revenue during FY2025, and says so in a
footnote to the MD&A results table. **No paid-membership count and no average revenue per membership is
disclosed anywhere in the FY2025 10-K.** Quoted:

> "During the year ended December 31, 2025, we discontinued the reporting of membership numbers, including
> average paying memberships and average monthly revenue per paying membership, focusing instead on revenue
> and operating margin as the primary financial metrics that we believe best represent our business
> performance."
> — Netflix 10-K FY2025, MD&A "Results of Operations" footnote (1), **accession 0001065280-26-000034**

Revenue is disclosed by region instead (FY2025 / FY2024 / FY2023, thousands): UCAN 19,957,152 /
17,359,369 / 14,873,783; EMEA 14,514,646 / 12,387,035 / 10,556,487; LATAM 5,357,521 / 4,839,816 /
4,446,461; APAC 5,353,717 / 4,414,746 / 3,763,727. The regional table header still reads "(in thousands,
except revenue per membership and percentages)" but **no revenue-per-membership column is populated**.

### On PRICE INCREASES — verbatim. This is the [E2-44] material.
All quotes from **accession 0001065280-26-000034**.

> "Revenues for the year ended December 31, 2025 increased 16% as compared to the year ended December 31,
> 2024, primarily due to the growth in memberships, price increases, and increased advertising revenue,
> partially offset by unfavorable changes in foreign exchange rates, net of hedging."
> — MD&A, "Revenues"

*The filer attributes a 16% revenue rise partly to price increases while memberships also grew. It does
not quantify the price component separately, and it gives no count of members lost to the increases.*

> "We primarily derive revenues from monthly membership fees for services related to streaming content to
> our members. We offer a variety of streaming membership plans, the price of which varies by country and
> the features of the plan. As of December 31, 2025, pricing on our paid plans ranged from the U.S. dollar
> equivalent of \$1 to \$37 per month, and pricing on our extra member sub accounts ranged from the U.S.
> dollar equivalent of \$2 to \$9 per month. We expect that from time to time the prices of our membership
> plans in each country may change and we may test other plan and price variations."
> — MD&A, "Revenues"

> "We have and may, from time to time, adjust our membership pricing, our membership plans, or our pricing
> model itself, including for example, the lower-priced ad-supported subscription plan. Similarly, we have
> increased enforcement of and will continue to enforce our terms of use to limit multi-household usage and
> shared viewing outside of a household. These and other adjustments we make may not be well-received by
> consumers, and could negatively impact our ability to attract and retain members, revenue and our results
> of operations."
> — Item 1A Risk Factors

> "If consumers do not perceive our service offering to be of value, including if we introduce new or adjust
> existing features, adjust pricing or service offerings, or change the mix of content in a manner that is
> not favorably received by them, we may not be able to attract and retain members, and accordingly, our
> revenue and results of operations may be adversely affected."
> — Item 1A Risk Factors

### On CHURN AND CANCELLATIONS — verbatim.
The word "churn" does **not** appear in the FY2025 10-K. The filer uses "canceled memberships" and
"cancel" instead, and gives **no churn rate, no gross additions figure and no cancellation count**.

> "We must continually add new members both to replace canceled memberships and to grow our business beyond
> our current membership base. Our ability to continue to attract and retain members will depend in part on
> our ability to consistently provide our members in countries around the globe with compelling content
> choices that keep our members engaged with our service..."
> — Item 1A Risk Factors, **accession 0001065280-26-000034**

> "Members cancel our service for many reasons, including a perception that they do not use the service
> sufficiently, that they need to cut household expenses, dissatisfaction with content, including any
> advertisements that may appear on our service, a preference for competitive services and customer service
> issues that they believe are not satisfactorily resolved. Adverse macroeconomic conditions, including as a
> result of inflation, may also adversely impact our ability to attract and retain members. If we do not
> grow as expected, given, in particular, that our content costs are largely fixed in nature, we may not be
> able to adjust our expenditures or increase our revenues, including by adjusting membership pricing,
> commensurate with the lowered growth rate such that our margins, liquidity and results of operations may
> be adversely impacted."
> — Item 1A Risk Factors

**Summary of the [E2-44] evidence at Netflix: qualitative only.** The filer says price increases helped
drive a 16% revenue rise and separately warns that pricing adjustments "may not be well-received"; it
quantifies neither the price effect nor the cancellation response, and it has removed the membership series
that would have let a reader infer it.

### Material subsequent-period fact disclosed in the same 10-K
> "On December 4, 2025, we entered into a definitive agreement and plan of merger with WBD to acquire WBD's
> streaming and studios businesses, including its film and television studios, HBO Max and HBO, which was
> amended and restated by the parties thereto on January 19, 2026 (as so amended and restated, the "Amended
> and Restated Merger Agreement"). WBD is a leading global media and entertainment company and will separate
> its Global Linear Networks business, Discovery Global, into a new publicly-traded company prior to the
> closing of the WBD transaction. Under the terms of the Amended and Restated Merger Agreement, each WBD
> stockholder will receive \$27.75 in cash (as may be adjusted in accordance with the terms of the Amended
> and Restated Merger Agreement) for each share of WBD common stock outstanding as of immediately prior to
> the closing of the WBD transaction, for a total equity value of approximately \$72.0 billion and an
> enterprise value of approximately \$82.7 billion (in each case, as of December 4, 2025). ... We expect the
> WBD transaction to close in 12-18 months from December 4, 2025, subject to receipt of required regulatory
> approvals, approval of WBD stockholders, the consummation of the separation and distribution of Discovery
> Global and other customary closing conditions."
> — Netflix 10-K FY2025, MD&A "Liquidity and Capital Resources", **accession 0001065280-26-000034**

---

## 2. CMCSA — Comcast Corporation
**Documents read:**
- Form 10-K for the fiscal year ended December 31, 2025, filed 2026-02-03, **accession 0001628280-26-004994**, primary document `cmcsa-20251231.htm`. (Note: the FY2025 10-K was filed through a different filer agent, so its accession prefix is 0001628280, not Comcast's own 0001166691.)
- Form 10-K for the fiscal year ended December 31, 2024, filed 2025-01-31, **accession 0001166691-25-000011**, primary document `cmcsa-20241231.htm` — used **only** to obtain the FY2023 Peacock revenue, cost and subscriber figures, which the FY2025 10-K does not repeat.

All figures **in millions of USD** as filed.

### CRITICAL LABEL WARNING
Comcast's segment profit measure is **Adjusted EBITDA**, which is **NOT operating income**. The filer
defines it itself:

> "We define Adjusted EBITDA as net income attributable to Comcast Corporation before net income (loss)
> attributable to noncontrolling interests, income tax expense, investment and other income (loss), net,
> interest expense, depreciation and amortization expense, and other operating gains and losses (such as
> impairment charges related to fixed and intangible assets and gains or losses on the sale of long-lived
> assets), if any. ... This measure should not be considered a substitute for operating income (loss), net
> income (loss), net income (loss) attributable to Comcast Corporation, or net cash provided by operating
> activities that we have reported in accordance with GAAP."
> — Comcast 10-K FY2025, "Non-GAAP Financial Measures", **accession 0001628280-26-004994**

Comcast reports **five** segments: Residential Connectivity & Platforms, Business Services Connectivity,
Media, Studios, Theme Parks. There is no single "Connectivity & Platforms" segment; it is two segments.
"Content & Experiences" is the grouping of Media + Studios + Theme Parks + headquarters.

### Segment table — three years, from the Segment Information note, FY2025 10-K
Revenue shown is **total segment revenue (external plus intersegment)**, the basis on which the MD&A
discusses each segment.

| Segment | Measure | FY2025 | FY2024 | FY2023 |
|---|---|---|---|---|
| Residential Connectivity & Platforms | Total revenue | 70,704 | 71,574 | 71,946 |
| | Segment Adjusted EBITDA | 26,653 | 27,338 | 26,948 |
| Business Services Connectivity | Total revenue | 10,237 | 9,701 | 9,255 |
| | Segment Adjusted EBITDA | 5,725 | 5,500 | 5,291 |
| **Media** (incl. Peacock) | Total revenue | **27,090** | **28,148** | **25,355** |
| | **Segment Adjusted EBITDA** | **3,196** | **3,130** | **2,955** |
| **Studios** | Total revenue | **11,286** | **11,092** | **11,625** |
| | **Segment Adjusted EBITDA** | **1,099** | **1,404** | **1,269** |
| **Theme Parks** | Total revenue | **9,836** | **8,617** | **8,947** |
| | **Segment Adjusted EBITDA** | **3,080** | **2,949** | **3,345** |
| Media/Studios/Theme Parks HQ and other | Adjusted EBITDA | (1,095) | (831) | (946) |
| **Total segment Adjusted EBITDA** | | **39,753** | **40,322** | **39,808** |
| Total consolidated revenue | | 123,707 | 123,731 | 121,572 |
| Income before income taxes | | 25,766 | 18,673 | 20,478 |

Theme Parks costs and expenses (MD&A): FY2025 6,756 vs FY2024 5,668 (+19.2%).
Media segment expense build FY2025: programming and production 17,866; marketing and promotion 1,773;
other 4,565.

**Cross-check per operator rule 4:** the segment-note Media revenue of \$27,090M for FY2025 ties to the
MD&A "Content & Experiences Overview" table and to the "Media Segment Results of Operations" table in the
same 10-K; Theme Parks Adjusted EBITDA of \$3,080M ties across all three presentations.

### Peacock — disclosed separately, but as revenue and costs, NOT as Adjusted EBITDA

| Peacock | FY2025 | FY2024 | FY2023 |
|---|---|---|---|
| Revenue (included in Media segment revenue) | \$5.4bn | \$4.9bn | \$3.4bn |
| Costs and expenses (included in Media segment) | \$6.5bn | \$6.7bn | \$6.1bn |
| **Implied loss — COMPUTED, not filed as a line** | **(\$1.1bn)** | **(\$1.8bn)** | **(\$2.7bn)** |
| **Paid subscribers (period end)** | **44 million** | **36 million** | **31 million** |

**Label warning.** Comcast does **not** publish a "Peacock Adjusted EBITDA" line. It publishes Peacock
revenue and Peacock costs and expenses, both as components of the Media segment. The loss row above is my
subtraction of the two disclosed figures and is **not a filed measure**; because the segment measure is
Adjusted EBITDA, the difference is an EBITDA-like figure and is **not operating income**.

FY2025 and FY2024, quoted:
> "Peacock generated revenue and costs and expenses of \$5.4 billion and \$6.5 billion in 2025,
> respectively, compared to \$4.9 billion and \$6.7 billion in 2024, respectively, including the Paris
> Olympics. Paid subscribers increased by 8 million to 44 million in 2025."
> — Comcast 10-K FY2025, MD&A consolidated operating results, segment highlights, **accession 0001628280-26-004994**

> "Media segment total revenue included \$5.4 billion and \$4.9 billion related to Peacock in 2025 and 2024,
> respectively, including amounts related to the Paris Olympics in 2024. We had 44 million and 36 million
> paid subscribers of Peacock as of 2025 and 2024, respectively. Peacock paid subscribers represent
> customers from which we recognize distribution revenue, including both customers that pay us directly and
> customers receiving the service through arrangements with companies who sell Peacock on our behalf. In
> these arrangements, paid subscribers are counted based on the terms of the arrangement when the related
> revenue is recognized. As a result, certain customers are counted when they activate their account, while
> other customers are counted when the Peacock service is made available to them as part of their bundled
> service offering regardless of whether it is activated. The increase in paid subscribers in 2025 is mainly
> due to the availability of Peacock through third-party bundled service offerings."
> — Comcast 10-K FY2025, MD&A "Media Segment Results of Operations", **accession 0001628280-26-004994**

*Note for the run: the subscriber definition is loose on its face. Comcast counts bundle-delivered
subscribers "regardless of whether it is activated", and attributes the 8-million FY2025 increase mainly
to third-party bundles. That is not the same unit as a direct paying Netflix or Disney+ subscriber.*

FY2023, quoted from the prior year's filing:
> "Media segment total revenue included \$4.9 billion and \$3.4 billion related to Peacock in 2024 and 2023,
> respectively, including amounts related to the Paris Olympics in 2024. We had 36 million and 31 million
> paid subscribers of Peacock as of 2024 and 2023, respectively."
> — Comcast 10-K FY2024, MD&A, **accession 0001166691-25-000011**

> "Media segment total costs and expenses included \$6.7 billion and \$6.1 billion related to Peacock in
> 2024 and 2023, respectively, including amounts related to the Paris Olympics in 2024."
> — Comcast 10-K FY2024, MD&A, **accession 0001166691-25-000011**

### Theme Parks capital expenditure and Epic Universe — PARTLY UNOBTAINABLE
**Comcast does NOT segment Theme Parks capital expenditure in the 10-K.** It breaks out capital
expenditure only for the Connectivity & Platforms business, and says so explicitly.

| Capex | FY2025 | FY2024 | FY2023 |
|---|---|---|---|
| Total consolidated capital expenditures (cash-flow statement) | 11,750 | 12,181 | 12,242 |
| Connectivity & Platforms capital expenditures (only segmented figure) | 8,723 | 8,286 | not given in this filing |
| — customer premise equipment | 2,192 | 2,013 | |
| — scalable infrastructure | 3,156 | 3,024 | |
| — line extensions | 2,689 | 2,691 | |
| — support capital | 686 | 557 | |
| **Non-C&P capex (Media + Studios + Theme Parks + corporate) — COMPUTED residual** | **3,027** | **3,895** | n/a |

> "Our most significant capital expenditures are within the Connectivity & Platforms business, and we expect
> that this will continue in the future. ... The table below summarizes the capital expenditures we incurred
> in our segments in the Connectivity & Platforms business in 2025 and 2024."
> — Comcast 10-K FY2025, MD&A "Capital Expenditures", **accession 0001628280-26-004994**

Also disclosed: the construction costs of Universal Beijing Resort "are presented separately in our
consolidated statements of cash flows", i.e. outside the capital-expenditures line above.

**Epic Universe: NO COST FIGURE IS FILED.** The FY2025 10-K names Epic Universe eleven times and never
gives its construction cost, nor its own revenue or profit. Everything disclosed is directional:

> "Capital expenditures decreased in 2025 primarily due to decreased spending on Epic Universe driven by the
> opening in May 2025, partially offset by increased spending by the Connectivity & Platforms businesses."
> — MD&A "Capital Expenditures", **accession 0001628280-26-004994**

> "Revenue increased primarily due to an increase in revenue at our theme parks in Orlando, driven by the
> opening of Epic Universe in May 2025. ... Adjusted EBITDA increased due to an increase in revenue,
> partially offset by an increase in costs and expenses. ... Capital expenditures continued to reflect
> significant spending for the development of Epic Universe in Orlando ahead of its opening."
> — MD&A, Theme Parks segment highlights, **accession 0001628280-26-004994**

> "Theme park segment revenue increased in 2025 primarily driven by our domestic theme parks, which included
> higher revenue at our theme parks in Orlando driven by the opening of Epic Universe in May 2025, partially
> offset by lower revenue at our theme park in Hollywood. ... Theme parks segment costs and expenses
> increased in 2025 primarily due to operating costs associated with Epic Universe."
> — MD&A "Theme Parks Segment Results of Operations", **accession 0001628280-26-004994**

> "We continue to invest significantly in existing and new theme park attractions, hotels and
> infrastructure, including Epic Universe in Orlando, which opened in May 2025, as well as in new
> destinations and experiences, including a Universal theme park and resort in the United Kingdom with a
> projected opening date in 2031, subject to various approvals."
> — MD&A, **accession 0001628280-26-004994**

Two further Epic Universe effects the filer names without sizing: consolidated depreciation and
amortization rose in 2025 partly from "increased depreciation due to the opening of Epic Universe in May
2025", and consolidated interest expense rose "primarily due to a decrease in capitalized interest driven
by the opening of Epic Universe".

*The measurable Epic Universe effect available from the filing: Theme Parks revenue +\$1,219M (+14.2%) on
costs +\$1,088M (+19.2%), for Adjusted EBITDA +\$131M (+4.5%). Against the three-year series, FY2025 Theme
Parks Adjusted EBITDA of \$3,080M is still \$265M BELOW the FY2023 figure of \$3,345M, with a new park now
open. Stated as observation, not conclusion.*

### The Versant separation — COMPLETED, and it is in the filing
> "On January 2, 2026, we completed the previously announced separation of Versant Media Group, Inc.
> ("Versant") into an independent, publicly traded company with its Class A common stock listed on The
> Nasdaq Stock Market under the ticker symbol "VSNT" (the "Separation"). The Versant business is comprised
> of certain of our former cable television networks, including MS NOW (formerly MSNBC), CNBC, USA Network,
> Golf Channel, E!, SYFY and Oxygen, and complementary digital platforms, including GolfNow, Fandango,
> Rotten Tomatoes and SportsEngine."
> — Comcast 10-K FY2025, Item 1 Business, **accession 0001628280-26-004994**

> "The Versant businesses were included in Comcast's Media segment and consolidated results for all periods
> presented, and accordingly the discussion that follows includes the Versant businesses unless otherwise
> indicated."
> — Item 1 Business, same accession

> "We operate our Media segment as a combined television and streaming business and will continue to do so
> following the Separation of the Versant business. We expect that the number of subscribers and audience
> ratings at our remaining linear television networks will continue to decline as a result of the competitive
> environment and shifting video consumption patterns, which we aim to mitigate over time by growth in both
> paid subscribers and advertising revenue at Peacock. We expect to continue to incur significant costs
> related to content and marketing at Peacock. ... We expect lower revenue and costs and expenses for the
> Media segment in 2026 as a result of the Separation of Versant."
> — MD&A, **accession 0001628280-26-004994**

Also disclosed: on the Separation, certain content licence agreements including sports rights "were
transferred to Versant in connection with the Separation, thereby reducing our programming and production
obligations by \$5.9 billion, of which \$1.5 billion was due" in the near term; and \$1.0bn aggregate
principal of 7.25% senior secured notes due January 2031 issued by Versant "ceased to be our contractual
obligation due to the completion of the Separation".

**Consequence for the three-year Media series above: it is NOT continuing-operations comparable to 2026.**
Versant was never a distinct business unit, sat inside Media for all three years shown, and was not
presented as a discontinued operation.

### On PRICE INCREASES, CHURN AND SUBSCRIBER RESPONSE — verbatim. [E2-44] material.
Comcast gives **no Peacock churn rate, no Peacock price-increase disclosure, and no Peacock ARPU.** The
word "churn" does not appear in the FY2025 10-K. What it does give is the cable side, where the
price/volume trade is stated plainly, and this is the most direct filer statement of the price-rise
trade-off anywhere in this peer set:

> "We also expect continued declines in video revenue as a result of domestic customer net losses due to
> shifting video consumption patterns and the competitive environment, although customer net losses
> typically mitigate the impact of continued rate increases on programming expenses, as well as continued
> declines in other revenue related to declines in wireline voice revenue."
> — Comcast 10-K FY2025, MD&A "Connectivity & Platforms", **accession 0001628280-26-004994**

> "In 2025, we simplified our broadband pricing structure and began offering a free wireless line for one
> year to new and existing domestic broadband customers, which we expect will improve customer retention and
> strengthen our ability to compete for new customers, but will negatively impact average domestic broadband
> revenue per customer."
> — MD&A "Connectivity & Platforms", same accession

*That is a filer stating it is cutting effective price to defend retention — the opposite direction to a
price rise, and recorded here as such.*

> "Domestic distribution revenue decreased in 2025, including the impact of the Paris Olympics in 2024.
> Excluding incremental revenue associated with this event, domestic distribution revenue increased in 2025
> primarily due to an increase in revenue at Peacock, partially offset by a decrease in revenue at our
> linear television networks. The decrease at our linear television networks was primarily due to a decline
> in the number of subscribers, partially offset by contractual rate increases."
> — MD&A "Media Segment Results of Operations", same accession

> "Average monthly total revenue per customer relationship is impacted by rate adjustments and changes in
> the types and levels of services received by our residential and business customers, as well as changes in
> advertising and other revenue and in foreign currency exchange rates."
> — MD&A, same accession

> "Programming expenses decreased in 2025 primarily due to a decline in the number of domestic video
> subscribers, partially offset by rate increases under our domestic programming contracts, an increase in
> programming expenses for our international sports networks and the impact of foreign currency."
> — MD&A, same accession

**The quantified price/volume outcome Comcast does file (FY2025 vs FY2024):** average monthly total
Connectivity & Platforms revenue per customer relationship \$131.77 vs \$130.57 (+0.9%), while total
customer relationships fell 967,000 to 50.8 million, domestic broadband customers fell 711,000 to 31.3
million, and domestic video customers fell 1.3 million to 11.3 million. Video revenue fell 5.1% to
\$26,387M. Connectivity & Platforms Adjusted EBITDA per customer relationship was \$52.71 vs \$52.75
(-0.1%). **Revenue per customer up 0.9%; the customer count down on every line; segment Adjusted EBITDA
down 2.5%.** All from accession 0001628280-26-004994.

---

## 3. WBD — Warner Bros. Discovery, Inc.
**Documents read:**
- Form 10-K for the fiscal year ended December 31, 2025, filed 2026-02-27, **accession 0001437107-26-000020**, primary document `wbd-20251231.htm`.
- Form 10-K FY2024, filed 2025-02-27, **accession 0001437107-25-000031**, primary document `wbd-20241231.htm` — used for the FY2023 segment operating income, FY2023 subscribers and FY2023 ARPU.
- Form 10-K FY2023, filed 2024-02-23, **accession 0001437107-24-000017** — used only to establish that no goodwill impairment was recorded in 2021, 2022 or 2023.

All figures **in millions of USD** as filed.

### Segment rename — read this before comparing to earlier files
> "In the first quarter of 2025, the Company renamed its DTC reportable segment to Streaming and its
> Networks reportable segment to Global Linear Networks."
> — WBD 10-K FY2025, Item 1 Business, **accession 0001437107-26-000020**

> "There have been no changes to the Company's reportable segments or the composition of the Company's
> reportable segments as a result of these actions."
> — same accession

So Streaming = the former DTC segment and Global Linear Networks = the former Networks segment, on the same
composition. The three-year series below is therefore continuous.

### WBD files BOTH Adjusted EBITDA AND segment operating income — so it is the one peer directly comparable to Disney's DTC operating income

| Segment | Measure | FY2025 | FY2024 | FY2023 |
|---|---|---|---|---|
| **Streaming** (HBO Max, HBO, discovery+) | Total revenues | **10,876** | **10,313** | **10,154** |
| | — Distribution | 9,444 | 9,022 | 8,703 |
| | — Advertising | 1,032 | 855 | 548 |
| | — Content | 388 | 428 | 886 |
| | — Other | 12 | 8 | 17 |
| | **Adjusted EBITDA** | **1,370** | **677** | **103** |
| | **Operating income (loss) — GAAP** | **(264)** | **(1,485)** | **(2,565)** |
| | Adjusted EBITDA margin (computed) | 12.6% | 6.6% | 1.0% |
| | **GAAP operating margin (computed)** | **(2.4)%** | **(14.4)%** | **(25.3)%** |
| **Studios** | Total revenues | **12,619** | **11,607** | **12,192** |
| | **Adjusted EBITDA** | **2,545** | **1,652** | **2,183** |
| | **Operating income — GAAP** | **1,674** | **529** | **211** |
| **Global Linear Networks** | Total revenues | **17,656** | **20,175** | **21,244** |
| | **Adjusted EBITDA** | **6,412** | **8,149** | **9,063** |
| | **Operating income (loss) — GAAP** | **2,692** | **(5,759)** | **3,322** |
| Corporate and inter-segment eliminations | Revenues | (3,855) | (2,774) | (2,269) |
| **Total revenues** | | **37,296** | **39,321** | **41,321** |
| **Total segment Adjusted EBITDA** | | **10,327** | **10,478** | **11,349** |

The FY2024 Global Linear Networks GAAP operating loss of \$(5,759)M contains the \$9,147M goodwill
impairment; Adjusted EBITDA excludes it. **This is exactly why Adjusted EBITDA is not operating income.**

Streaming segment cost build (FY2025 / FY2024 / FY2023), from the segment note:
content expense 6,145 / 6,183 / 6,454; personnel 760 / 773 / 844; marketing 1,000 / 1,147 / 1,313;
other segment expenses 1,601 / 1,533 / 1,440.

**Cross-check per operator rule 4:** Streaming revenue of \$10,876M FY2025 appears three times in the same
document — the MD&A Streaming segment table, the revenue-disaggregation note, and the segment-information
note — and agrees each time; Streaming Adjusted EBITDA of \$1,370M agrees between the MD&A segment table and
the segment note, and reconciles there to the \$(264)M GAAP operating loss.

### Streaming subscribers and ARPU

| | Dec 31 2025 | Dec 31 2024 | Dec 31 2023 |
|---|---|---|---|
| Total Domestic subscribers (m) | 59.2 | 57.1 | 52.0 |
| Total International subscribers (m) | 72.4 | 59.8 | 45.6 |
| **Total Streaming subscribers (m)** | **131.6** | **116.9** | **97.7** |
| Domestic ARPU | \$10.79 | \$11.89 | \$11.20 |
| International ARPU | \$3.80 | \$3.85 | \$3.85 |
| **Global ARPU** | **\$6.92** | **\$7.76** | **\$7.78** |

(FY2023 labelled "Total DTC subscribers" in the FY2024 filing; same measure.)

ARPU definition, quoted:
> "The Company defines Streaming Average Revenue Per User ("ARPU") as total subscription revenue plus net
> advertising revenue for the period divided by the daily average number of paying subscribers for the
> period. Where daily values are not available, the sum of beginning of period and end of period divided by
> two is used."
> — WBD 10-K FY2025, footnote to the Streaming ARPU table, **accession 0001437107-26-000020**

### Content spend

| Item | FY2025 | FY2024 | FY2023 |
|---|---|---|---|
| Content rights amortization and impairment (cash-flow add-back) | 11,855 | 13,946 | 16,024 |
| **"Film and television content rights, games and production payables, net" (cash-flow use — the filer's content cash-spend line)** | **(11,401)** | **(12,349)** | **(12,305)** |
| Total film and television content rights and games (balance sheet, noncurrent) | 19,114 | 19,102 | n/a |

**Label warning.** WBD does not present a line called "additions to content assets". Its cash-flow
statement shows the content spend net of production payables, on the line quoted above. It is therefore
**not** the same construction as Netflix's "Additions to content assets" or Disney's produced-and-licensed
content spend, and the three should not be treated as identical measures.

### Goodwill impairments since the April 2022 WarnerMedia merger — ONE, and it is large
| Year | Goodwill impairment | Reporting unit |
|---|---|---|
| 2021 (pre-merger, qualitative test) | none | — |
| 2022 | **none** | quantitative test, all units passed |
| 2023 | **none** | quantitative test, all units passed |
| **2024** | **\$9,147M** | **Global Linear Networks** |
| 2025 | **none** | qualitative test, all units passed |

> "The carrying value of the Global Linear Networks reporting unit exceeded its fair value and the Company
> recorded a non-cash goodwill impairment charge of \$9,147 million during the second quarter of 2024 in
> impairments and loss on dispositions in the consolidated statements of operations."
> — WBD 10-K FY2025, goodwill note, **accession 0001437107-26-000020**

> "Impairments and loss on dispositions were \$172 million and \$9,603 million in 2025 and 2024,
> respectively. The loss in 2024 was primarily attributable to a \$9,147 million non-cash goodwill
> impairment charge related to the Global Linear Networks re[porting unit]..."
> — MD&A, same accession

> "For the 2025 annual impairment test, the Company performed a qualitative goodwill impairment assessment
> for all of its reporting units and determined that it was more likely than not that the fair value of each
> reporting unit exceeded its carrying value..."
> — same accession

> "For the 2022 annual impairment test, the Company performed a quantitative goodwill impairment assessment
> for all reporting units consistent with the Company's accounting policy. The estimated fair value of each
> reporting unit exceeded its carrying value and, therefore, no impairment was recorded."
> — WBD 10-K FY2023, goodwill note, **accession 0001437107-24-000017**

> "As of October 1, 2023, the Company performed a quantitative goodwill impairment assessment for all
> reporting units. The estimated fair value of each reporting unit exceeded its carrying value and,
> therefore, no impairment was recorded. The Studios reporting unit, which had headroom of 15%..."
> — WBD 10-K FY2023, **accession 0001437107-24-000017**

*Note: \$9,147M is the GOODWILL impairment only. WBD separately carries "Impairment and amortization of
fair value step-up for content" of \$784M / \$1,139M / \$2,373M for FY2025 / FY2024 / FY2023 in its
Adjusted EBITDA reconciliation, and 2024 total "impairments and loss on dispositions" of \$9,603M.*

### Total debt

| | Dec 31 2025 | Dec 31 2024 |
|---|---|---|
| Bridge loan, 18-month maturity, 7.22% | 15,000 | — |
| Senior notes, maturities 5 years or less, 3.92% | 6,659 | 13,744 |
| Senior notes, 5–10 years, 4.37% | 3,509 | 7,853 |
| Senior notes, over 10 years, 5.17% | 7,677 | 17,930 |
| **Total debt (face)** | **32,845** | **39,527** |
| Debt net of discount/premium/issuance costs/acquisition fair-value adjustments | 32,567 | 39,505 |
| Current portion | (139) | (2,748) |
| **Noncurrent portion** | **32,428** | **36,757** |

> "Our consolidated indebtedness as of December 31, 2025 was \$32,567 million, of which \$139 million is
> current. In addition, we have the ability to draw down on a \$4,000 million revolving credit facility in
> the ordinary course..."
> — WBD 10-K FY2025, Item 1A Risk Factors, **accession 0001437107-26-000020**

As of December 31, 2025 the filer states the fair value of its outstanding senior notes including accrued
interest was \$15,205 million. Long-term debt repayment schedule: 139 / 16,483 / 1,409 / 2,274 / 1,354 /
11,186 — the \$15bn bridge loan sits in the second bucket.

### The announced separation — SUPERSEDED TWICE. This is the most important status item in this file.
The two-company separation into Streaming & Studios and Global Networks was announced in June 2025, then
overtaken. The latest filing says the following, and it changes what Netflix's own 10-K (filed five weeks
earlier) says:

> "In June 2025, the Company announced its plans to separate the Company into two publicly traded companies,
> Warner Bros. and Discovery Global, and in October 2025, the Company announced that the board of directors
> would evaluate a broad range of strategic options, including continuing to advance the separation of the
> Company, a transaction for the entire company or separate transactions for Warner Bros. and/or Discovery
> Global, as well as an alternative separation structure that would enable a merger of Warner Bros. and
> spin-off of Discovery Global."
> — WBD 10-K FY2025, Item 1 Business, **accession 0001437107-26-000020**

**Termination of the Netflix merger:**
> "In January 2026, the Company entered into an amended and restated agreement and plan of merger, by and
> among the Company, Netflix, Inc. ("Netflix"), Nightingale Sub, Inc., a wholly owned subsidiary of Netflix,
> and New Topco 25, Inc., a wholly owned subsidiary of WBD (the "Netflix Merger Agreement"), under which
> Netflix would have acquired the Streaming and Studios segments (subject to certain deviations) and certain
> other assets and liabilities, including the Company's film and television studios, HBO Max, and HBO,
> following the separation and distribution of Discovery Global to the Company's stockholders (the
> "Separation Transaction")."
> — same accession

> "Following the board of directors' determination that it had received a "Company Superior Proposal," as
> defined in the Netflix Merger Agreement, from PSKY and Netflix's waiver of its right to propose revisions
> to the Netflix Merger Agreement, on February 27, 2026, in accordance with the terms of the Netflix Merger
> Agreement, the Company terminated the Netflix Merger Agreement in connection with entering into the PSKY
> Merger Agreement (as defined below). In connection with the termination of the Netflix Merger Agreement,
> PSKY, on behalf of the Company, paid Netflix a termination fee of \$2.8 billion in cash (the "Netflix
> Termination Fee") as required by the terms of the Netflix Merger Agreement."
> — same accession

**The PSKY merger — the operative deal per the latest filing:**
> "On February 27, 2026, the Company entered into an agreement and plan of merger, by and among the Company,
> PSKY and Prince Sub Inc., a wholly owned subsidiary of PSKY ("Merger Sub") ... pursuant to which and
> subject to the terms and conditions therein, at the effective time, Merger Sub will merge with and into
> WBD, with WBD surviving as a wholly owned subsidiary of PSKY."
> — same accession

> "Upon completion of the PSKY Merger, each issued and outstanding share of WBD common stock (subject to
> certain exceptions) will be converted into the right to receive an amount in cash equal to \$31.00, without
> interest, plus, if the closing date of the PSKY Merger occurs after September 30, 2026, the Ticking
> Consideration..."
> — same accession

> "Concurrently with the execution of the PSKY Merger Agreement, Larry J. Ellison and an associated trust
> entered into a guarantee in favor of WBD to, among other things, jointly and severally guarantee certain
> payments by PSKY under the PSKY Merger Agreement, including \$45.72 billion of the Merger Consideration,
> and assist WBD with the consummation of the PSKY Merger."
> — same accession

> "In addition, PSKY's obligation to consummate the PSKY Merger is subject to WBD not having completed the
> separation of its Streaming & Studios business from its Global Linear Networks business nor having declared
> or made any dividend to WBD's stockholders to effectuate the separation. There can be no assurance that
> the PSKY Merger will occur in accordance with the expected plans or anticipated timeline, or at all."
> — same accession

> "The PSKY Merger Agreement contains certain customary termination rights for WBD and PSKY, including,
> without limitation, a right for either party to terminate if the PSKY Merger is not completed on or before
> March 4, 2027, subject to an extension to June 4, 2027 specified in the PSKY Merger Agreement. Termination
> under specified circumstances will require WBD to pay PSKY a termination fee of \$3.0 billion and reimburse
> PSKY for (i) any payment made by PSKY, which will in no event be more than \$1,528 million, in connection
> with WBD's obligation to complete the Junior Lien Exchange Offer (as defined herein) by December 30, 2026
> and (ii) the Netflix Termination Fee, or PSKY to pay WBD a termination fee of \$7.0 billion."
> — same accession

**STATUS PER THE LATEST FILING: the two-company separation is NOT going ahead as announced — the PSKY
merger is conditioned on WBD NOT completing it.** The segment presentation is unchanged because the CODM
made no corresponding management change through December 31, 2025.

### CORRECTION TO THE NETFLIX SECTION ABOVE
The Netflix FY2025 10-K (accession 0001065280-26-000034, filed 2026-01-23) describes the Netflix/WBD
merger agreement as live and expected to close in 12–18 months. **That agreement was terminated on
2026-02-27** per WBD's 10-K of the same date, accession 0001437107-26-000020, with a \$2.8 billion
termination fee paid to Netflix by PSKY on WBD's behalf. The Netflix quotation stands as filed; the fact
pattern has moved. Any use of the Netflix disclosure must carry this correction.

### On PRICE INCREASES, CHURN AND SUBSCRIBER RESPONSE — verbatim. [E2-44] material.
WBD gives **no churn rate and no gross additions figure**; the word "churn" does not appear in the FY2025
10-K. What it does give is **the clearest quantified price/volume outcome of any streamer in this set,
because it publishes ARPU alongside subscribers** — and in FY2025 ARPU fell while subscribers rose.

**Quantified, FY2025 vs FY2024 (all from accession 0001437107-26-000020):** subscribers +13% to 131.6m,
distribution revenue only +5%, Global ARPU **−11%** to \$6.92, Domestic ARPU **−9%** to \$10.79.

> "Distribution revenue increased 5% in 2025, primarily attributable to a 13% increase year-over-year in
> subscribers as a result of continued growth and global expansion of HBO Max, including new distribution
> deals, partially offset by the impact of the previously disclosed domestic wholesale deal renewal that
> occurred in the second quarter of 2025."
> — MD&A, Streaming segment, **accession 0001437107-26-000020**

> "Global ARPU decreased 11% in 2025, primarily attributable to broader wholesale distribution of HBO Max
> Basic with Ads, the impact of the previously disclosed domestic wholesale deal renewal that occurred in the
> second quarter of 2025, and growth in lower ARPU international markets."
> — MD&A, Streaming segment, same accession

> "Advertising revenue increased 20% in 2025, primarily attributable to an increase in ad-lite subscribers,
> partially offset by domestic pricing pressures."
> — MD&A, Streaming segment, same accession

The prior year is the opposite direction and is worth recording alongside it, because it is the one place
in this peer set where a filer says a price rise fed through:
> "Distribution revenue increased 5% in 2024, primarily attributable to a 20% increase in subscribers and an
> increase in pricing following the launch of Max in Europe and Latin America in 2024, partially offset by
> continued domestic linear wholesale subscriber declines."
> — WBD 10-K FY2024, MD&A, DTC segment, **accession 0001437107-25-000031**

> "Global ARPU increased 1% in 2024, primarily attributable to subscriber growth of the ad-lite tier
> domestically, higher pricing, and a continuing subscriber mix shift from linear wholesale, partially offset
> by growth in lower ARPU international markets."
> — WBD 10-K FY2024, MD&A, **accession 0001437107-25-000031**

On cancellations, qualitative only:
> "If existing subscribers, including those who receive subscriptions through wireless, broadband, or
> streaming bundling arrangements with third parties or through wholesale arrangements with MVPDs, cancel or
> discontinue their subscriptions for any reason, including as a result of selecting an alternative wireless
> or broadband plan that does not bundle our products, canceling or discontinuing their MVPD subscription, or
> due to the availability of competing offerings that are perceived to offer greater value compared to our
> streaming products, our business may be adversely affected. We would need to add new subscribers both to
> replace subscribers who cancel or discontinue their subscriptions and to grow our business."
> — Item 1A Risk Factors, **accession 0001437107-26-000020**

> "Their success and the success of other subscription-based streaming services we may offer in the future
> will be largely dependent on our ability to initially attract, and ultimately retain, subscribers. If we
> are unable to effectively market our streaming products or if consumers do not perceive the pricing and
> related features of our streaming products to be of value versus our competitors, we may not be able to
> attract and retain subscribers."
> — Item 1A Risk Factors, same accession

On the linear side, the same rate-up/volume-down pattern Comcast reports:
> "Distribution revenue decreased 6% in 2024, primarily attributable to an 8% decline in domestic linear
> subscribers for the year, partially offset by a 5% increase in domestic contractual affiliate rates. ...
> Declines in linear subscribers are expected to continue."
> — WBD 10-K FY2024, MD&A, Networks segment, **accession 0001437107-25-000031**

---

## 4. PARAMOUNT — Paramount Skydance Corp (successor) / Paramount Global (predecessor)
**Documents read:**
- Paramount Skydance Corp Form 10-K for the fiscal year ended December 31, 2025, filed 2026-02-25, **accession 0002041610-26-000011**, primary document `psky-20251231.htm`, **CIK 0002041610**. A 10-K/A followed on 2026-04-24, accession 0001140361-26-016758 (not read; the original carries the financial statements).
- Paramount Global Form 10-K for the fiscal year ended December 31, 2024, filed 2025-02-26, **accession 0000813828-25-000005**, primary document `para-20241231.htm`, **CIK 0000813828** — used for the FY2024 and FY2023 Paramount+ subscriber and revenue figures as originally reported.

All figures **in millions of USD** as filed.

### THE MERGER BREAKS THE SERIES. Read this before using any number below.
The transaction closed **August 7, 2025**, and it created a new basis of accounting. The registrant
therefore does **not** report a fiscal year 2025. It reports two stub periods.

> "On August 7, 2025 (the "Closing Date"), pursuant to a purchase and sale agreement, dated July 7, 2024,
> certain affiliates of investors of Skydance, comprised of entities controlled by the Ellison Family, and
> affiliates of RedBird Capital Partners..."
> — Paramount Skydance 10-K FY2025, Item 1 Business, **accession 0002041610-26-000011**

> "Pushdown of Ultimate Parent's Basis— At the time Paramount Global and Skydance became subsidiaries of
> Paramount Skydance Corporation, the Ellison Family controlled both Paramount Global and Skydance, and as a
> result, this transaction has been accounted [for] ..."
> — MD&A "The Transactions", same accession

> "Our consolidated financial statements and footnote disclosures are presented in distinct periods to
> indicate the pushdown of the Ultimate Parent's basis, which resulted in a new basis of accounting."
> — MD&A, same accession

> "As a result of the pushdown of the Ultimate Parent's basis, operating income, net loss from continuing
> operations attributable to Parent, and diluted EPS in the Successor [period are not comparable]..."
> — MD&A, same accession

> "On August 6, 2025, in connection with the Transactions ... all shares of Class A and Class B common stock
> of our predecessor, Paramount Global, were delisted from The Nasdaq Stock Market LLC ... Shares of
> Paramount Skydance Corporation Class B Common Stock now trade on the Nasdaq Stock Market LLC ("Nasdaq")
> under the ticker symbol "PSKY." All shares of Paramount Global Class A Common Stock and Class B Common
> Stock have been delisted from Nasdaq and have been cancelled and cease to exist."
> — Item 5, same accession

**Consequence: the four reporting columns are Successor Aug 7 – Dec 31 2025; Predecessor Jan 1 – Aug 6
2025; Predecessor FY2024; Predecessor FY2023. The two 2025 stubs cannot be added to get a GAAP 2025
figure, and the filer says so. It does supply a "Supplemental Pro Forma" combination FOR REVENUE ONLY, on
the explicit ground that revenue was not affected by the pushdown.**

> "Supplemental Pro Forma Revenues for the year ended December 31, 2025 reflect the combination of the
> Successor period from August 7 - December 31, 2025 and the Predecessor period from January 1 - August 6,
> 2025. While the Successor and Predecessor periods are distinct reporting periods, revenues were not
> impacted by the pushdown of the Ultimate Parent's basis and are supplementally presented on a combined
> basis to help investors view these revenues in a manner consistent with our management."
> — footnote to the segment revenue tables, same accession

**There is NO pro forma Adjusted OIBDA for full-year 2025.** So for DTC profitability in 2025 the only
filed figures are the two stubs: \$77M (Successor stub) and \$153M (Predecessor stub).

### Segment table, as the filing presents it — from the segment note, FY2025 10-K

| Segment | Measure | Successor Aug 7–Dec 31 2025 | Predecessor Jan 1–Aug 6 2025 | Predecessor FY2024 | Predecessor FY2023 |
|---|---|---|---|---|---|
| **TV Media** | Revenues | 7,082 | 9,977 | **18,779** | **20,085** |
| | — content costs | 3,464 | 4,956 | 9,199 | 9,861 |
| | — advertising and marketing | 247 | 328 | 689 | 761 |
| | — other | 1,743 | 2,626 | 4,543 | 4,672 |
| | **Adjusted OIBDA** | **1,628** | **2,067** | **4,348** | **4,791** |
| **Direct-to-Consumer** (Paramount+, Pluto TV, BET+) | Revenues | 3,497 | 5,087 | **7,632** | **6,736** |
| | — content costs | 1,767 | 2,712 | 4,415 | 4,459 |
| | — advertising and marketing | 656 | 749 | 1,341 | 1,751 |
| | — other | 997 | 1,473 | 2,373 | 2,189 |
| | **Adjusted OIBDA** | **77** | **153** | **(497)** | **(1,663)** |
| **Filmed Entertainment** | Revenues | 1,736 | 1,593 | **2,955** | **2,957** |
| | **Adjusted OIBDA** | **(132)** | **(100)** | **(96)** | **(119)** |
| Eliminations (revenue) | | (46) | (35) | (153) | n/a |
| **Total revenues** | | **12,269** | **16,622** | **29,213** | n/a |
| Corporate/Eliminations (OIBDA) | | (215) | (212) | (427) | (447) |
| Stock-based compensation | | (91) | (99) | (210) | (172) |
| **Total Adjusted OIBDA** | | **1,267** | **1,809** | **3,118** | n/a |
| Depreciation and amortization | | (590) | (204) | (392) | (418) |
| Programming charges | | (41) | — | (1,118) | (2,371) |
| Impairment charges | | — | (157) | (6,130) | (83) |
| Restructuring, transaction-related and other corporate | | (731) | (454) | (747) | 31 |
| Gain on dispositions | | — | 35 | — | — |
| **Operating income (loss) — GAAP** | | **(95)** | **1,029** | **(5,269)** | **(451)** |

Supplemental pro forma FY2025 revenue (filer's own combination): TV Media **17,059** (−9% vs 2024);
Direct-to-Consumer **8,584** (+12%); Filmed Entertainment **3,832** (−5%, and the Predecessor FY2024
pro forma comparative is restated to 4,013 to include Skydance).

**Label warning.** Adjusted OIBDA is Paramount's segment measure. It is **operating income before
depreciation and amortization, and before programming charges, impairment charges, restructuring,
transaction-related items, stock-based compensation and gains on dispositions.** It is **NOT operating
income**, and it is **not the same construction as Comcast's or WBD's Adjusted EBITDA either** — those two
also strip SBC, but the exclusion lists differ. The filer's own words on its non-GAAP measures:

> "Adjusted operating income before depreciation and amortization ("Adjusted OIBDA"), adjusted earnings from
> continuing operations before income taxes, adjusted provi[sion for income taxes] ... We use these measures
> to, among other things, evaluate our operating performance. These measures are among the primary measures
> used by management for planning and fo[recasting]..."
> — MD&A, non-GAAP section, **accession 0002041610-26-000011**

**Cross-check per operator rule 4:** TV Media Adjusted OIBDA of \$1,628M and DTC Adjusted OIBDA of \$77M for
the Successor period appear in both the MD&A segment summary table and the segment note of the same 10-K
and agree; FY2024 DTC revenue of \$7,632M and Adjusted OIBDA of \$(497)M in the PSKY segment note agree to
the Paramount Global FY2024 10-K, accession 0000813828-25-000005.

### Paramount+ subscribers and revenue

| | Dec 31 2025 | Dec 31 2024 | Dec 31 2023 |
|---|---|---|---|
| **Paramount+ global subscribers (m), as reported in the FY2025 10-K** | **78.9** | **76.1** (restated) | not given in this filing |
| Paramount+ global subscribers (m), as ORIGINALLY reported in the FY2024 10-K | — | **77.5** | **67.5** |
| **Paramount+ revenue** | **7,063** (pro forma; 2,897 Successor + 4,166 Predecessor) | **5,896** | **4,446** |

**The Dec-2024 subscriber count was restated downward by 1.4 million.** The definition changed:
> "Subscribers include customers who are registered for Paramount+, either directly through our owned and
> operated apps and websites, or through third-party distributors. Subscribers also include customers who are
> provided with access through a subscription bundle with a domestic linear video streaming service (vMVPD)
> or an international third-party distributor. Beginning in the fourth quarter of 2025, our subscriber count
> includes only paid subscriptions, and accordingly the subscriber count in each of the periods above
> excludes customers registered in a free trial, which totaled 1.4 million as of December 31, 2024.
> Subscriber counts reflect the number of subscribers as of the applicable period-end date."
> — Paramount Skydance 10-K FY2025, footnote to the Paramount+ subscriber table, **accession 0002041610-26-000011**

The prior definition, for contrast:
> "Our subscribers include paid subscriptions and those customers registered in a free trial."
> — Paramount Global 10-K FY2024, footnote to the same table, **accession 0000813828-25-000005**

### Paramount+ ARPU — NOT DISCLOSED. Could not obtain.
**Neither the Paramount Skydance FY2025 10-K nor the Paramount Global FY2024 10-K discloses an ARPU for
Paramount+ or for the Direct-to-Consumer segment.** The strings "ARPU" and "average revenue per" do not
appear in either document. No instance found in the filings searched (accessions 0002041610-26-000011 and
0000813828-25-000005). A crude revenue-per-subscriber can be computed from the two disclosed figures
(FY2025 pro forma \$7,063M / 78.9m subs ≈ \$7.46 per month; FY2024 \$5,896M / 77.5m ≈ \$6.34) but that is
**my arithmetic on a period-end denominator and is not the filer's measure** — it is not an ARPU as WBD
defines one (daily average paying subscribers), and it excludes Pluto TV and BET+ revenue while the
subscriber count excludes their users too.

### D2C profitability — the direction is the story, and it is filed
| | FY2023 | FY2024 | 2025 (two stubs) |
|---|---|---|---|
| DTC Adjusted OIBDA | **(1,663)** | **(497)** | **+77** (Successor) and **+153** (Predecessor) |

So the Direct-to-Consumer segment crossed into positive Adjusted OIBDA during 2025 on both sides of the
merger date. **This is Adjusted OIBDA, not operating income; Paramount does not publish a DTC-segment
operating income, so there is no directly Disney-comparable DTC operating income for Paramount at all.**

### Reporting structure changes again in 2026
> "In the first quarter of 2026, we transitioned our reporting structure into three new segments: TV Media,
> Direct-to-Consumer and Studios."
> — Paramount Skydance 10-K FY2025, Item 1 Business, **accession 0002041610-26-000011**

So Filmed Entertainment becomes Studios from Q1 2026, and the series will break a second time.

### On PRICE INCREASES, CHURN AND SUBSCRIBER RESPONSE — verbatim. [E2-44] material.
Paramount is the **only filer in this set that uses the word "churn"**, and it is also the clearest on
having raised price while subscribers grew.

> "Affiliate and subscription revenues during each of the Successor and Predecessor periods in 2025 and 2024
> reflect the benefit from subscriber growth and pricing increases for Paramount+ but were negatively
> impacted by linear subscriber declines. At December 31, 2025, there were 78.9 million Paramount+
> subscribers."
> — Paramount Skydance 10-K FY2025, MD&A, **accession 0002041610-26-000011**

> "On a pro forma basis, the growth of 4% in affiliate and subscription revenues for the year ended December
> 31, 2025 reflects an increase of 8% from higher streaming subscription fees, driven by subscriber growth and
> pricing increases for Paramount+, partially offset by decreases from lower linear affiliate fees."
> — MD&A, same accession

> "Subscription revenues during the Successor and Predecessor periods in 2025 and 2024 benefited from growth
> in subscribers and pricing for Paramount+. The 20% growth on a pro forma basis reflects these factors.
> Paramount+ subscribers of 78.9 million at December 31, 2025 increased 2.8 million from 76.1 million at
> December 31, 2024."
> — MD&A, Direct-to-Consumer segment, same accession

The "churn" language, from Item 1A:
> "In addition to attracting new users, we must also meaningfully engage existing users to minimize "churn"
> and maximize our advertising and subscription revenues. If consumers do not perceive our streaming services
> to be of value compared to competing services, including because we fail to introduce compelling new
> content and features, do not maintain competitive pricing, terminate or modify promotional or trial period
> offerings, change the mix of content in a manner that is unfavorably received, or offer an inferior consumer
> viewing experience, we may not be able to attract, engage and retain users, and our business, financial
> condition or results of operations could be adversely affected. If subscribers who receive access to our
> streaming services through third-party bundles, including through MVPDs, cancel or discontinue their
> subscriptions, including as a result of selecting an alternative bundle that does not include our services
> or canceling or discontinuing such bundled service, our business may be adversely affected."
> — Item 1A Risk Factors, **accession 0002041610-26-000011**

**No churn RATE is given.** The word is used only as a risk concept.

From the predecessor's filing, the one place a filer in this set dates a specific price rise and says it fed
through to revenue:
> "The 12% increase in subscription revenues was driven by growth in Paramount+ subscribers, including the
> migration of certain subscribers from Showtime's premium subscription streaming service, and the June 2023
> domestic pricing increases that we began to benefit from during the third quarter of 2023. Paramount+
> subscribers increased 10.0 million, or 15%, compared with December 31, 2023, reflecting growth in both
> domestic and international subscribers."
> — Paramount Global 10-K FY2024, MD&A, Direct-to-Consumer, **accession 0000813828-25-000005**

> "Affiliate and subscription revenues grew 1%, reflecting an increase of approximately 5% from higher
> streaming subscription fees, driven by subscriber growth and domestic pricing increases for Para[mount+]..."
> — Paramount Global 10-K FY2024, MD&A, **accession 0000813828-25-000005**

*Recorded observation, not conclusion: a June 2023 domestic price rise is followed by a 15% subscriber gain
over the following year and a 12% subscription-revenue gain. The filer gives no offsetting cancellation
figure, so the net is all that is observable.*

**Note on the WBD bid.** The PSKY FY2025 10-K discloses legal and professional fees in the Successor period
"associated with the Warner Bros. offer". The WBD merger agreement itself was signed February 27, 2026 —
see the WBD section above for its terms (\$31.00 per WBD share in cash, \$45.72bn guaranteed by Larry J.
Ellison and an associated trust, \$7.0bn reverse termination fee payable by PSKY).

---

## 5. AAPL — Apple Inc.
**Document read:** Form 10-K for the fiscal year ended September 27, 2025, filed 2025-10-31,
**accession 0000320193-25-000079**, primary document `aapl-20250927.htm`.
All figures **in millions of USD** as filed.

### CONFIRMED: Apple does not break out Apple TV. Services is the only relevant line.
**NO STREAMING-SEGMENT PROFITABILITY IS FILED.** Apple's reportable segments are **geographic**, not
product or service lines:

> "The Company manages its business primarily on a geographic basis. The Company's reportable segments
> consist of the Americas, Europe, Greater China, Japan and Rest of Asia Pacific. ... Although the reportable
> segments provide similar hardware and software products and similar services, each one is managed
> separately to better align with the location of the Company's customers and distribution partners and the
> unique market dynamics of each geographic region."
> — Apple 10-K FY2025, Item 1 Business and the segment note, **accession 0000320193-25-000079**

So the only profitability Apple files is (a) five geographic segments and (b) a two-line gross-margin split
between Products and Services. **There is no Apple TV revenue, no Apple TV subscriber count, no Apple TV
cost, no Apple TV or streaming operating income or loss, and no services-level profit below the gross-margin
line, anywhere in the FY2025 10-K.** The string "Apple TV+" does not appear at all; "Apple TV" appears twice
— once as the hardware product Apple TV 4K, once naming the service in the list of subscription services.

### Services revenue and Services gross margin — the only figures available

| Item | FY2025 (ended 2025-09-27) | FY2024 (2024-09-28) | FY2023 (2023-09-30) |
|---|---|---|---|
| **Services net sales** | **109,158** | **96,169** | **85,200** |
| Change vs prior year (as filed) | +14% | +13% | — |
| **Services gross margin (dollars)** | **82,314** | **71,050** | **60,345** |
| **Services gross margin percentage (as filed)** | **75.4%** | **73.9%** | **70.8%** |
| Total Products net sales — COMPUTED (total less Services) | 307,003 | 294,866 | 298,085 |
| iPhone | 209,586 | 201,183 | 200,583 |
| Mac | 33,708 | 29,984 | 29,357 |
| iPad | 28,023 | 26,694 | 28,300 |
| Wearables, Home and Accessories | 35,686 | 37,005 | 39,845 |
| **Total net sales** | **416,161** | **391,035** | **383,285** |
| Products gross margin | 112,887 | 109,633 | 108,803 |
| Products gross margin percentage | 36.8% | 37.2% | 36.5% |
| Total gross margin | 195,201 | 180,683 | 169,148 |
| Total gross margin percentage | 46.9% | 46.2% | 44.1% |
| **Total company operating income** | **133,050** | **123,216** | **114,301** |
| **Total company operating margin — COMPUTED** (operating income / total net sales) | **31.97%** | **31.51%** | **29.82%** |

Footnote to the category table, quoted:
> "Services net sales include amortization of the deferred value of services bundled in the sales price of
> certain products."
> — Apple 10-K FY2025, footnote (1) to net sales by category, **accession 0000320193-25-000079**

Geographic segment operating income FY2025 / FY2024 / FY2023: Americas 72,480 / 67,656 / 60,508; Europe
47,739 / 41,790 / 36,098; Greater China 26,917 / 27,082 / 30,328; Japan 13,955 / 12,454 / 11,888; Rest of
Asia Pacific 14,586 / 13,062 / 12,066; Corporate (42,627) / (38,828) / (36,587); Total 133,050 / 123,216 /
114,301.

**Cross-check per operator rule 4:** total net sales of \$416,161M for FY2025 appears in the geographic MD&A
table, the category MD&A table, the Consolidated Statements of Operations and the segment note of the same
document and agrees in all four; operating income of \$133,050M agrees between the Consolidated Statements of
Operations and the segment-note total.

### What the 10-K says about Services composition — verbatim
The full Services description, quoted from Item 1 Business, **accession 0000320193-25-000079**. This is the
whole of it; there is nothing more granular in the filing.

> "**Advertising** — The Company's advertising services include third-party licensing arrangements and the
> Company's own advertising platforms."

> "**AppleCare** — The Company offers a portfolio of fee-based service and support products under the
> AppleCare® brand. The offerings provide priority access to Apple technical support, access to the global
> Apple authorized service network for repair and replacement services, and in many cases additional coverage
> for instances of accidental damage or theft and loss, depending on the country and type of product."

> "**Cloud Services** — The Company's cloud services store and keep customers' content up-to-date and
> available across multiple Apple devices and Windows personal computers."

> "**Digital Content** — The Company operates various platforms, including the App Store®, that allow
> customers to discover and download applications and digital content, such as books, music, video, games and
> podcasts.
> The Company also offers digital content through subscription-based services, including Apple Arcade®, a game
> service; Apple Fitness+®, a personalized fitness service; Apple Music®, which offers users a curated
> listening experience with on-demand radio stations; Apple News+®, a news and magazine service; and Apple
> TV®, which offers exclusive original content and live sports."

> "**Payment Services** — The Company offers payment services, including Apple Card®, a co-branded credit
> card, and Apple Pay®, a cashless payment service."

**That single clause — "and Apple TV®, which offers exclusive original content and live sports" — is the
entirety of what the FY2025 10-K discloses about Apple's streaming service.** It sits inside Digital
Content, which sits inside Services, which sits inside the geographic segments. Apple TV is therefore one
unquantified item within one of five unquantified sub-categories of a \$109,158M revenue line whose only
disclosed profit measure is a gross margin.

The one place the filing acknowledges the economics of producing content:
> "The Company also produces its own digital content, which can be costly to produce due to intense and
> increasing competition for talent, content and subscribers, and may fail to appeal to the Company's
> customers."
> — Item 1A Risk Factors, **accession 0000320193-25-000079**

> "The Company contracts with numerous third parties to offer their digital content to customers. This
> includes the right to sell, or offer subscriptions to, third-party content, as well as the right to
> incorporate specific content into the Company's own services. The licensing or other distribution
> arrangements for this content can be for relatively short time periods and do not guarantee the continuation
> or renewal of these arrangements on commercially reasonable terms, or at all. ... Other content owners,
> providers or distributors may seek to limit the Company's access to, or increase the cost of, such content.
> The Company may be unable to continue to offer a wide variety of content at commercially reasonable prices
> with acceptable usage rules."
> — Item 1A Risk Factors, same accession

The filer's own explanation of the Services margin moves, which is as close as the filing gets to a mix
statement:
> "Services gross margin increased during 2025 compared to 2024 primarily due to higher Services net sales and
> a different mix of services. Services gross margin percentage increased during 2025 compared to 2024
> primarily due to a different mix of services, partially offset by higher costs."
> — MD&A "Gross Margin", same accession

### On PRICE INCREASES, CHURN AND SUBSCRIBER RESPONSE — NO INSTANCE FOUND
**No instance found in the filing searched** (Apple 10-K for FY ended September 27, 2025, accession
0000320193-25-000079). Apple discloses **no subscriber or paid-subscription count, no ARPU, no churn rate,
no gross additions, and no statement about subscriber response to any price change** for Apple TV or for any
other service. The words "churn", "price increase" and "cancellation" (in a subscriber sense) do not appear.
The only pricing language is generic market language — "aggressive price competition, downward pressure on
gross margins" — applied to the company's markets as a whole, not to a subscription service.

---

## 6. AMZN — Amazon.com, Inc.
**Documents read:**
- Form 10-K for the fiscal year ended December 31, 2025, filed 2026-02-06, **accession 0001018724-26-000004**, primary document `amzn-20251231.htm`.
- Form 10-K FY2024, filed 2025-02-07, **accession 0001018724-25-000004** — used only for the FY2023 video and music expense and capitalized-cost figures.

All figures **in millions of USD** as filed unless a quote states billions.

### CONFIRMED: Amazon does not break out Prime Video. NO STREAMING-SEGMENT PROFITABILITY IS FILED.
Amazon's three reportable segments are **North America, International and AWS**. Prime Video is not a
segment, not a sub-segment, and has no disclosed revenue, subscriber count, cost or profit. "Prime Video"
as a phrase does not appear in the FY2025 10-K at all; video revenue is folded into "Subscription services"
(for unlimited-viewing subscriptions), "Online stores" (for transactional digital sales) and "Other" (for
licensing and distribution of video content).

### "Subscription services" net sales — three years

| Net sales by group of similar products and services | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Online stores | 231,872 | 247,029 | 269,287 |
| Physical stores | 20,030 | 21,215 | 22,561 |
| Third-party seller services | 140,053 | 156,146 | 172,162 |
| Advertising services | 46,906 | 56,214 | 68,635 |
| **Subscription services** | **40,209** | **44,374** | **49,619** |
| AWS | 90,757 | 107,556 | 128,725 |
| Other | 4,958 | 5,425 | 5,935 |
| **Consolidated** | **574,785** | **637,959** | **716,924** |

**Subscription services is NOT a streaming revenue line.** Its composition, quoted:
> "Includes annual and monthly fees associated with Amazon Prime memberships, as well as digital video,
> audiobook, digital music, e-book, and other non-AWS subscription services."
> — footnote (5) to the net-sales-by-group table, Amazon 10-K FY2025, **accession 0001018724-26-000004**

> "Subscription services - Our subscription sales include fees associated with Amazon Prime memberships and
> access to content including digital video, audiobooks, digital music, e-books, and other non-AWS
> subscription services. Prime memberships provide our customers with access to an evolving suite of
> benefits that represent a single stand-ready obligation. Subscriptions are paid for at the time of or in
> advance of delivering the services. Revenue from such arrangements is recognized over the subscription
> period."
> — revenue recognition note, same accession

*The load-bearing phrase is "a single stand-ready obligation": Amazon accounts for the whole Prime bundle
as one performance obligation, so there is no accounting basis inside the filing on which Prime Video
revenue could be separated, even in principle.*

Relevant boundary note, quoted:
> "Digital media content subscriptions that provide unlimited viewing or usage rights are included in
> "Subscription services.""
> — footnote (1) to the same table, same accession

### Operating income by segment — three years

| Segment | Measure | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| **North America** | Net sales | 352,828 | 387,497 | 426,305 |
| | Operating expenses | 337,951 | 362,530 | 396,686 |
| | **Operating income** | **14,877** | **24,967** | **29,619** |
| | Operating margin — COMPUTED | 4.2% | 6.4% | 6.9% |
| **International** | Net sales | 131,200 | 142,906 | 161,894 |
| | Operating expenses | 133,856 | 139,114 | 157,144 |
| | **Operating income (loss)** | **(2,656)** | **3,792** | **4,750** |
| | Operating margin — COMPUTED | (2.0)% | 2.7% | 2.9% |
| **AWS** | Net sales | 90,757 | 107,556 | 128,725 |
| | Operating expenses | 66,126 | 67,722 | 83,119 |
| | **Operating income** | **24,631** | **39,834** | **45,606** |
| | Operating margin — COMPUTED | 27.1% | 37.0% | 35.4% |
| **Consolidated** | Net sales | 574,785 | 637,959 | 716,924 |
| | **Operating income** | **36,852** | **68,593** | **79,975** |
| | Operating margin — COMPUTED | 6.4% | 10.8% | 11.2% |
| | Net income | 30,425 | 59,248 | 77,670 |

**Cross-check per operator rule 4:** consolidated net sales of \$716,924M and operating income of \$79,975M
for FY2025 agree between the segment note and the Consolidated Statements of Operations of the same
document, and the three segment operating incomes sum exactly to \$79,975M (29,619 + 4,750 + 45,606).

### Video content costs — the disclosure, quoted with its figures
This is the single quantified video disclosure Amazon makes. It is in the "Digital Video and Music Content"
part of the significant-accounting-policies note, and it is a **combined video AND music** figure.

> "Our produced and licensed video content is primarily monetized together as a unit, referred to as a film
> group, in each major geography where we offer Amazon Prime memberships. These film groups are evaluated for
> impairment whenever an event occurs or circumstances change indicating the fair value is less than the
> carrying value. **The total capitalized costs of video, which is primarily released content, and music as of
> December 31, 2024 and 2025 were \$19.6 billion and \$21.3 billion. Total video and music expense was \$20.4
> billion and \$22.4 billion for the year ended December 31, 2024 and 2025.** Total video and music expense
> includes licensing and production costs associated with content offered within Amazon Prime memberships, and
> costs associated with digital subscriptions and sold or rented content."
> — Amazon 10-K FY2025, "Digital Video and Music Content" note, **accession 0001018724-26-000004**

The FY2023 figures, from the prior filing:
> "The total capitalized costs of video, which is primarily released content, and music as of December 31, 2023
> and 2024 were \$17.4 billion and \$19.6 billion. Total video and music expense was \$18.9 billion and \$20.4
> billion for the year ended December 31, 2023 and [2024]."
> — Amazon 10-K FY2024, same note, **accession 0001018724-25-000004**

| Video and music (Amazon's combined measure) | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| **Total video and music EXPENSE** | **\$18.9bn** | **\$20.4bn** | **\$22.4bn** |
| Total CAPITALIZED costs of video and music at year end | \$17.4bn | \$19.6bn | \$21.3bn |

**Comparability warning.** \$22.4bn is an **expense** (amortization plus content expensed as incurred),
not a cash spend, and it includes music. It is therefore **not** comparable to Netflix's "Additions to
content assets" (a cash figure, video only) and **not** comparable to Disney's produced-and-licensed content
spend. The nearest thing to it in this set is Netflix's amortization of content assets. Amazon gives **no
cash content-spend line at all** — its cash-flow statement rolls content into "Depreciation and amortization
of property and equipment and capitalized content costs, operating lease assets, and other" of \$48,663M /
\$52,795M / \$65,756M for FY2023 / FY2024 / FY2025, which cannot be decomposed from the filing.

Amortization policy, quoted:
> "We obtain video content, inclusive of episodic television and movies, and music content for customers
> through licensing agreements that have a wide range of licensing provisions including both fixed and
> variable payment schedules. When the license fee for a specific video or music title is determinable or
> reasonably estimable and the content is available to us, we recognize an asset and a corresponding liability
> for the amounts owed. We reduce the liability as payments are made and we amortize the asset to "Cost of
> sales" on an accelerated basis, based on estimated usage or viewing patterns, or on a straight-line basis. If
> the licensing fee is not determinable or reasonably estimable, no asset or liability is recorded and
> licensing costs are expensed as incurred. We also develop original video content for which the production
> costs are capitalized and amortized to "Cost of sales" predominantly on an accelerated basis that follows the
> estimated viewing patterns associated with the content."
> — same accession

> "The weighted average remaining life of our capitalized video content is 3.2 years."
> — same accession

On Prime as a marketing instrument rather than a profit centre:
> "While costs associated with Amazon Prime membership benefits and other shipping offers are not included in
> sales and marketing expense, we view these offers as effective worldwide marketing tools, and intend to
> continue offering them indefinitely."
> — MD&A "Operating Expenses", same accession

### On PRICE INCREASES, CHURN AND SUBSCRIBER RESPONSE — NO INSTANCE FOUND for video or Prime
**No instance found in the filings searched** (Amazon 10-K FY2025, accession 0001018724-26-000004; Amazon
10-K FY2024, accession 0001018724-25-000004). Amazon discloses **no Prime membership count, no Prime Video
subscriber count, no ARPU, no churn rate, no gross additions, and no statement of subscriber response to any
price change.** The word "churn" does not appear. "Membership fee" appears only in the revenue-recognition
description quoted above, with no amount and no history of changes.

The nearest thing to pricing commentary is directional and concerns the retail and AWS businesses, not
subscriptions:
> "North America sales increased 10% in 2025, compared to the prior year. The sales growth primarily reflects
> increased unit sales, including sales by third-party sellers, advertising sales, and subscription services.
> Increased unit sales were driven largely by our continued focus on price, selection, and convenience for our
> customers, including from our fast shipping offers."
> — MD&A "Results of Operations", **accession 0001018724-26-000004**

> "AWS sales increased 20% in 2025, compared to the prior year. The sales growth primarily reflects increased
> customer usage, partially offset by pricing changes primarily driven by long-term customer contracts."
> — MD&A, same accession

*Note the asymmetry worth recording: Amazon attributes growth to its focus on **price** (i.e. keeping it low)
and attributes an offset in AWS to **pricing changes** working against revenue. Nowhere does it report
raising a subscription price, and nowhere does it report a subscriber response.*

---

# SIDE-BY-SIDE: streaming / DTC revenue, profit, margin, content spend
**Latest full fiscal year available for each filer. READ THE LABEL COLUMN BEFORE COMPARING ANY TWO ROWS.**

Disney figures are as supplied by the operator from the **Disney FY2025 10-K, accession
0001744489-25-000155** (fiscal year ended 2025-09-27) and have not been re-derived here.

| Filer / service | Period | Streaming/DTC revenue | Profit figure | **THE FILER'S MEASURE — this is the label** | Streaming margin | Content spend | Accession |
|---|---|---|---|---|---|---|---|
| **Disney — Direct-to-Consumer segment** | FY2025 (to 2025-09-27) | **\$24,614M** | **\$1,327M** | **Segment operating income (GAAP-reconciled segment measure)** | **5.4%** | company-wide \$22,709M produced + licensed, of which licensed programming and rights \$12,887M and produced content \$9,822M — **COMPANY, NOT DTC** | 0001744489-25-000155 |
| **Netflix — whole company** | FY2025 (to 2025-12-31) | **\$45,183M** | **\$13,327M** | **Operating income (GAAP)** | **29.5% (filer states it)** | **\$17,097M "Additions to content assets" — CASH, from the cash-flow statement** (amortization \$16,422M) | 0001065280-26-000034 |
| **Comcast — Peacock** | FY2025 | **\$5.4bn** | **\$(1.1)bn — COMPUTED, NOT FILED** | **NO profit measure is filed for Peacock.** Comcast discloses Peacock revenue \$5.4bn and Peacock "costs and expenses" \$6.5bn; the difference is my subtraction and is EBITDA-like, **not operating income** | **(20.4)% — COMPUTED** | **not disclosed for Peacock**; Media segment programming and production \$17,866M covers linear plus Peacock | 0001628280-26-004994 |
| **Comcast — Media segment** (Peacock inside it) | FY2025 | \$27,090M | \$3,196M | **Segment Adjusted EBITDA — NOT operating income** | 11.8% | Media segment programming and production \$17,866M — **accrual, not cash** | 0001628280-26-004994 |
| **WBD — Streaming segment (HBO Max, HBO, discovery+)** | FY2025 | **\$10,876M** | **\$1,370M** | **Segment Adjusted EBITDA — NOT operating income** | **12.6%** | segment content expense \$6,145M — **accrual, not cash** | 0001437107-26-000020 |
| **WBD — Streaming segment, GAAP** | FY2025 | \$10,876M | **\$(264)M** | **Segment operating loss (GAAP) — the one figure directly comparable to Disney's DTC operating income** | **(2.4)%** | company cash line "Film and television content rights, games and production payables, net" \$(11,401)M — **whole company, net of payables** | 0001437107-26-000020 |
| **Paramount+ / Paramount Skydance DTC segment** | **FY2024 — last clean full year** | **\$7,632M** (Paramount+ alone \$5,896M) | **\$(497)M** | **Adjusted OIBDA — NOT operating income, and not the same exclusions as Adjusted EBITDA** | **(6.5)%** | DTC segment content costs \$4,415M — **accrual, not cash** | 0000813828-25-000005 |
| **Paramount+ / Paramount Skydance DTC segment** | 2025, TWO STUBS (no GAAP year exists) | Successor Aug 7–Dec 31 **\$3,497M**; Predecessor Jan 1–Aug 6 **\$5,087M**; filer's pro forma combination **\$8,584M** (Paramount+ alone \$7,063M) | Successor **\$77M**; Predecessor **\$153M**. **There is no filed full-year 2025 figure** | **Adjusted OIBDA — NOT operating income.** The filer publishes a pro forma REVENUE combination only, and says the periods are distinct because of pushdown accounting | **not computable on a filed basis**; the naive stub-sum \$230M / \$8,584M = 2.7% is **my arithmetic across non-additive periods — do not rely on it** | DTC content costs \$1,767M + \$2,712M = \$4,479M stub sum, **accrual, not cash, and not a filed annual figure** | 0002041610-26-000011 |
| **Apple — Apple TV** | FY2025 (to 2025-09-27) | **NOT DISCLOSED** | **NOT DISCLOSED** | **No streaming-segment profitability is filed.** Segments are geographic. The nearest line is Services net sales \$109,158M with Services gross margin \$82,314M / 75.4% — a gross margin over ALL services, not a streaming profit | **not disclosed** | **not disclosed** | 0000320193-25-000079 |
| **Amazon — Prime Video** | FY2025 | **NOT DISCLOSED** | **NOT DISCLOSED** | **No streaming-segment profitability is filed.** Segments are North America / International / AWS. Nearest line is Subscription services net sales \$49,619M, which is the whole Prime bundle plus music, audiobooks and e-books | **not disclosed** | **\$22.4bn total video AND music EXPENSE** (capitalized balance \$21.3bn) — an expense, not a cash spend, and it includes music | 0001018724-26-000004 |

### Where these are NOT comparable — stated plainly
1. **Adjusted EBITDA is not operating income.** Comcast's and WBD's segment measures strip depreciation,
   amortization, impairments, restructuring, transaction costs and (for WBD) share-based compensation.
   Disney's DTC \$1,327M is a segment **operating income**. The only like-for-like comparison against it in
   this whole file is **WBD Streaming's \$(264)M GAAP operating loss**. Comparing Disney's \$1,327M against
   WBD Streaming's \$1,370M Adjusted EBITDA would flatter WBD by roughly \$1.6bn of excluded charges.
2. **Adjusted OIBDA is not Adjusted EBITDA.** Paramount's measure also excludes programming charges,
   impairment charges and stock-based compensation, on a different exclusion list again. Three "Adjusted"
   measures, three definitions.
3. **Peacock has no filed profit measure at all.** Revenue minus "costs and expenses" is a subtraction I
   performed, and because the segment framework is Adjusted EBITDA, the result carries no depreciation or
   amortization and is not an operating result.
4. **Content spend is four different things across these filers.** Netflix's \$17,097M is **cash** additions,
   video only, whole company (which for Netflix is the streaming business). Disney's \$22,709M is
   **company-wide**, not DTC-only, so it cannot be divided by DTC revenue. WBD's \$11,401M is a **whole-company
   cash figure net of production payables**. WBD's, Comcast's and Paramount's segment content figures are
   **accrual expense** inside a segment. Amazon's \$22.4bn is an **expense including music**. No two of these
   are the same construction.
5. **Subscriber counts are not one unit.** Netflix has stopped publishing any. Comcast counts bundle
   recipients "regardless of whether it is activated". WBD counts each product subscription separately for
   multi-product subscribers. Paramount restated December 2024 down 1.4 million when it stopped counting free
   trials. Apple and Amazon publish none.
6. **Paramount's 2025 does not exist as a fiscal year.** Any "FY2025 Paramount" figure is either a stub, a
   revenue-only pro forma the filer supplies, or arithmetic the filer explicitly declines to do.

### Filed streaming subscriber and ARPU series, for completeness

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Netflix memberships | disclosed then; **discontinued during 2025 and absent from the FY2025 10-K** | | **not disclosed** |
| Netflix ARPU | discontinued with the above | | **not disclosed** |
| Peacock paid subscribers | 31m | 36m | **44m** |
| Peacock ARPU | not disclosed | not disclosed | not disclosed |
| WBD Streaming subscribers | 97.7m | 116.9m | **131.6m** |
| **WBD Global ARPU** | **\$7.78** | **\$7.76** | **\$6.92** |
| Paramount+ subscribers | 67.5m | 77.5m as first reported / 76.1m restated | **78.9m** |
| Paramount+ ARPU | **not disclosed in any filing read** | | |
| Apple TV subscribers / ARPU | **not disclosed** | | |
| Prime Video subscribers / ARPU | **not disclosed** | | |

---

# [E2-44] — SUBSCRIBER RESPONSE TO PRICE RISES: what the six filers actually say
Consolidated from the sections above. **Gathering only.**

| Filer | Is a price rise disclosed? | Is a subscriber response quantified? | Is a churn rate given? | Where |
|---|---|---|---|---|
| **Netflix** | Yes, qualitatively — "price increases" named as one of three drivers of a 16% revenue rise | **No.** No price effect isolated, no cancellations counted, and the membership series that would allow inference was **removed during 2025** | No. The word "churn" does not appear | 0001065280-26-000034 |
| **Comcast** | Yes on the linear/cable side, repeatedly: "continued rate increases", "contractual rate increases", "rate adjustments". **No Peacock price disclosure at all** | **Partly, and this is the strongest quantified case in the set — on cable, not streaming.** Revenue per customer relationship +0.9% to \$131.77 while customer relationships −967,000, broadband −711,000, video −1.3m, video revenue −5.1%, segment Adjusted EBITDA −2.5% | No | 0001628280-26-004994 |
| **WBD** | Yes for FY2024 ("an increase in pricing following the launch of Max in Europe and Latin America"); FY2025 discloses the **reverse** — ARPU fell | **Yes, and it is the clearest streaming case: FY2025 subscribers +13% while Global ARPU −11% to \$6.92 and Domestic ARPU −9%.** Distribution revenue grew only 5% on a 13% subscriber gain | No. The word "churn" does not appear | 0001437107-26-000020 and 0001437107-25-000031 |
| **Paramount** | **Yes, and dated:** "the June 2023 domestic pricing increases that we began to benefit from during the third quarter of 2023"; and for 2025 "subscriber growth and pricing increases for Paramount+" | **Partly — the net only.** Following the June 2023 rise, Paramount+ subscribers +10.0m (+15%) and subscription revenue +12%. No offsetting cancellation figure is given | **Uses the word "churn" — the only filer that does — but gives no rate** | 0002041610-26-000011 and 0000813828-25-000005 |
| **Apple** | **No instance found in the filing searched** (10-K for FY ended 2025-09-27) | No | No | 0000320193-25-000079 |
| **Amazon** | **No instance found in the filings searched** (10-Ks for FY2025 and FY2024). Amazon's only pricing statements run the other way: growth "driven largely by our continued focus on price", and AWS revenue "partially offset by pricing changes" | No | No | 0001018724-26-000004 and 0001018724-25-000004 |

### The verbatim core, one quote each, for the [E2-44] question
> "Revenues for the year ended December 31, 2025 increased 16% as compared to the year ended December 31,
> 2024, primarily due to the growth in memberships, price increases, and increased advertising revenue,
> partially offset by unfavorable changes in foreign exchange rates, net of hedging."
> — Netflix, **0001065280-26-000034**

> "We also expect continued declines in video revenue as a result of domestic customer net losses due to
> shifting video consumption patterns and the competitive environment, although customer net losses typically
> mitigate the impact of continued rate increases on programming expenses..."
> — Comcast, **0001628280-26-004994**

> "Global ARPU decreased 11% in 2025, primarily attributable to broader wholesale distribution of HBO Max
> Basic with Ads, the impact of the previously disclosed domestic wholesale deal renewal that occurred in the
> second quarter of 2025, and growth in lower ARPU international markets."
> — WBD, **0001437107-26-000020**

> "The 12% increase in subscription revenues was driven by growth in Paramount+ subscribers, including the
> migration of certain subscribers from Showtime's premium subscription streaming service, and the June 2023
> domestic pricing increases that we began to benefit from during the third quarter of 2023. Paramount+
> subscribers increased 10.0 million, or 15%, compared with December 31, 2023..."
> — Paramount Global, **0000813828-25-000005**

> "In addition to attracting new users, we must also meaningfully engage existing users to minimize "churn"
> and maximize our advertising and subscription revenues. If consumers do not perceive our streaming services
> to be of value compared to competing services, including because we fail to introduce compelling new content
> and features, do not maintain competitive pricing... we may not be able to attract, engage and retain
> users..."
> — Paramount Skydance, **0002041610-26-000011**

**Apple: no instance found in the filing searched — Apple Inc. Form 10-K for the fiscal year ended September
27, 2025, accession 0000320193-25-000079.**

**Amazon: no instance found in the filings searched — Amazon.com, Inc. Form 10-K for the fiscal year ended
December 31, 2025, accession 0001018724-26-000004, and Form 10-K for the fiscal year ended December 31, 2024,
accession 0001018724-25-000004.**

---

## FIGURES SOUGHT AND NOT OBTAINED, WITH THE REASON

| What was asked for | Status | Why |
|---|---|---|
| Netflix paid memberships and ARPU, FY2025 | **Not obtainable** | Discontinued during FY2025; the 10-K says so in terms and publishes neither. Not a search failure — an absence the filer states |
| Netflix free cash flow, as filed | **Not filed** | No FCF figure or reconciliation in the 10-K. Computed from OCF less purchases of PP&E and labelled as my computation |
| Peacock Adjusted EBITDA | **Not filed** | Comcast discloses Peacock revenue and Peacock "costs and expenses" only. The loss is my subtraction, labelled |
| Peacock ARPU | **Not filed** | No per-subscriber revenue for Peacock anywhere in the 10-K |
| Theme Parks capital expenditure, segmented | **Not filed** | Comcast segments capex only for the Connectivity & Platforms business. Non-C&P capex of \$3,027M (FY2025) is my residual and covers Media + Studios + Theme Parks + corporate together |
| Epic Universe construction cost | **Not filed** | Eleven mentions in the FY2025 10-K, no cost figure, no Epic-specific revenue or profit. Only directional statements |
| Epic Universe performance | **Partly** | Only inferable from the Theme Parks segment: revenue +\$1,219M, costs +\$1,088M, Adjusted EBITDA +\$131M — and FY2025 Adjusted EBITDA of \$3,080M remains \$265M below FY2023 |
| Comcast FY2023 Connectivity & Platforms capex breakdown | **Not in the FY2025 filing** | The capex table covers 2025 and 2024 only |
| WBD content cash spend on a Netflix-comparable basis | **Not filed that way** | Only the net-of-payables cash line and segment accrual content expense exist |
| Paramount+ ARPU | **Not filed, either side of the merger** | "ARPU" and "average revenue per" do not appear in accession 0002041610-26-000011 or 0000813828-25-000005 |
| A GAAP full-year 2025 for Paramount | **Does not exist** | Pushdown accounting splits the year at August 6/7 2025. The filer supplies a pro forma combination for REVENUE ONLY and declines to do so for Adjusted OIBDA |
| Paramount FY2023 total revenue and total Adjusted OIBDA | **Segment-level only** | The FY2025 segment note carries FY2023 by segment; consolidated FY2023 revenue and total Adjusted OIBDA are not in that four-column table |
| Apple TV+ revenue, subscribers, cost, profit | **Not filed** | Segments are geographic. Apple TV appears once as a service name. Confirmed absent |
| Prime Video revenue, subscribers, profit | **Not filed** | Segments are North America / International / AWS. "Prime Video" does not appear in the FY2025 10-K. Prime is accounted for as "a single stand-ready obligation" |
| Amazon video content CASH spend | **Not filed** | Only a combined video-and-music EXPENSE (\$22.4bn FY2025) and a capitalized balance. The cash-flow statement rolls content amortization into a \$65,756M composite line |
| A churn rate from any filer | **Not filed by any of the six** | Two filers use the word (Paramount as a risk concept, nobody as a metric). No rate, no gross additions, no cancellation count anywhere |

## Documents fetched, all from `https://www.sec.gov/Archives/edgar/data/...`
Text-stripped copies are in `Test Runs/_research 2026-09-19 DIS/peers/`.

| File | Registrant | Form / period | Accession | Primary document |
|---|---|---|---|---|
| NFLX_10K_FY2025.txt | Netflix, Inc. | 10-K FY2025 | 0001065280-26-000034 | nflx-20251231.htm |
| CMCSA_10K_FY2025.txt | Comcast Corp | 10-K FY2025 | 0001628280-26-004994 | cmcsa-20251231.htm |
| CMCSA_10K_FY2024.txt | Comcast Corp | 10-K FY2024 | 0001166691-25-000011 | cmcsa-20241231.htm |
| WBD_10K_FY2025.txt | Warner Bros. Discovery | 10-K FY2025 | 0001437107-26-000020 | wbd-20251231.htm |
| WBD_10K_FY2024.txt | Warner Bros. Discovery | 10-K FY2024 | 0001437107-25-000031 | wbd-20241231.htm |
| WBD_10K_FY2023.txt | Warner Bros. Discovery | 10-K FY2023 | 0001437107-24-000017 | wbd-20231231.htm |
| PSKY_10K_FY2025.txt | Paramount Skydance Corp | 10-K FY2025 | 0002041610-26-000011 | psky-20251231.htm |
| PARA_10K_FY2024.txt | Paramount Global | 10-K FY2024 | 0000813828-25-000005 | para-20241231.htm |
| AAPL_10K_FY2025.txt | Apple Inc. | 10-K FY2025 (to 2025-09-27) | 0000320193-25-000079 | aapl-20250927.htm |
| AMZN_10K_FY2025.txt | Amazon.com, Inc. | 10-K FY2025 | 0001018724-26-000004 | amzn-20251231.htm |
| AMZN_10K_FY2024.txt | Amazon.com, Inc. | 10-K FY2024 | 0001018724-25-000004 | amzn-20241231.htm |

No aggregator, press article, encyclopaedia or XBRL-only figure was used. Every number above is from a filed
document read in text, and the fetch script is `Test Runs/_research 2026-09-19 DIS/pf.py`.

# Company Run — Belden Inc. (BDC) — 2026-09-26
**WAVE 7 name 43 of 218. Claimed at dispatch 2026-09-26 ~01:47 by an unattended run agent (claim commit `a1d53b2e`). RESULT: Q1 IN, Q2 OUT (on the business); the file closed at Q2. Belden is an industrial networking, cable and connectivity maker; it is NOT a business development company despite the ticker.**

**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.49%** · date **09/25/2026** (the newest row on the curve at ~01:47 on 2026-09-26) · source (issuing authority) **US Treasury daily par yield curve, 30 Yr**, struck fresh for this run by `strike.py`; raw CSV saved as `Test Runs/_research 2026-09-26 BDC/treasury_2026.csv`. Prior rows 5.47% (09/24) and 5.40% (09/23). **Not inherited from any brief; FRED not used.**
- FX: the business reports in US dollars and is quoted in US dollars on the NYSE. About 42% of 2025 sales were to customers outside the US (10-K FY2025, Item 1), so part of the earnings is translated from euros and other currencies; the reporting currency and the quote currency are the same, and the sovereign is struck for the reporting currency. No ADR.

**Registrant.** CIK 0000913142, BELDEN INC., Delaware, fiscal year to December 31, St. Louis. Former names on EDGAR: Belden CDT Inc. (2004-2007), Cable Design Technologies Corp (1994-2004).

**Price, shares, cap.**
- Price **$112.45**, NYSE close **2026-09-25**, Yahoo chart endpoint (aggregator, live quote only, **flagged**); raw response saved as `price_raw.json`. Prior closes 110.80 (09/24), 114.13 (09/23).
- Shares **39,078,191** common, from the **cover of the 10-Q for the quarter to 2026-06-28, filed 2026-07-30, accession `0000913142-26-000034`**: *"As o f July 23, 2026, the Registrant h ad 39,078,191 out standing shares of common stock."* (extraction artifacts kept as extracted, PRIME RULE 1). `python Screens/cover_shares.py BDC` agrees and names one class only (*"Common stock, $0.01 par value"*). One class, one line on the cover; the charter question does not arise. The RUCKUS purchase of 2026-07-01 was paid in cash, so no shares were issued for it.
- **Market cap $4,394.3M** (112.45 x 39,078,191). The screen row carried $4,351M on 2026-09-02.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes (Note 4 acquisitions FY2025; the pro forma notes of the RUCKUS 8-K/A; segment and debt notes read at Q2 and beneath)
- **10-K for FY2025, filed 2026-02-17, accession `0000913142-26-000009`** (Items 1 and 7, the statements, Note 4); **10-Q for the quarter to 2026-06-28, filed 2026-07-30, accession `0000913142-26-000034`**; for the series, 10-Ks FY2023 `0000913142-24-000007`, FY2022 `0000913142-23-000008`, FY2021 `0000913142-22-000007`, FY2019 `0000913142-20-000008`, FY2016 `0000913142-17-000005`, FY2014 `0001193125-15-057344`; DEF 14A filed 2026-04-09 `0000913142-26-000011`; the deal 8-Ks listed below.
- **Figure cross-checked against the filed statement:** FY2025 net cash provided by operating activities **$354,864K** in the filed Consolidated Cash Flow Statements, equal to the tagged figure `tools/run.py` reads ($355M). FY2024 $352,076K and FY2023 $319,638K agree the same way.

**The screen's deal_note, opened: BELDEN IS THE ACQUIRER. The quote is not a spread; the perimeter changed on 2026-07-01.**
1. **8-K filed 2026-04-30, accession `0000913142-26-000020`, Items 1.01, 8.01, 9.01.** Belden and Vistance Networks, Inc. signed a Purchase Agreement *"pursuant to which the Company has agreed to purchase, and Vistance has agreed to sell, the RUCKUS reporting segment of Vistance (collectively, the "Business") in exchange for approximately $1.846 billion in cash, on a cash-free, debt-free basis"*. The exhibit the screen called EX-2.1 is the Purchase Agreement (`projectrocket-purchaseag.htm`). The same-day release (EX-99.1): *"At approximately 13x projected 2026 Adjusted EBITDA"*; *"Belden intends to temporarily pause share repurchases until leverage returns closer to our long-term target"*.
2. **8-K filed 2026-07-01, accession `0000913142-26-000029`, Items 1.01, 2.01, 2.03, 9.01: the deal CLOSED.** *"On July 1, 2026, the Company and Vistance consummated the RUCKUS Acquisition [...] the Company paid approximately $1.87 billion in cash, net of cash acquired"*, funded by *"a $1,850.0 million senior secured term loan credit facility"* at *"term SOFR plus 2.25%"*, amortizing 0.25% a quarter, maturing July 1, 2033, *"secured by a lien on substantially all of the assets of the Company and the guarantors"*, and which *"limits certain payments, including dividends"*.
3. **8-K/A filed 2026-09-11, accession `0000913142-26-000037`**: RUCKUS audited 2025 and Q1 2026 statements and the pro forma (EX-99.3). Read at Q2 and beneath; no termination, no vote (none was required; a cash purchase of a segment).
- **Size against the buyer: $1.87-1.91 billion is 43% of today's $4,394M cap**, paid entirely with new secured debt. RUCKUS is 20% of pro forma 2025 revenue ($686.8M of $3,402.0M, EX-99.3). **Every filed annual figure below is the pre-RUCKUS company; the company being priced is not the company that filed them.** This is carried to Q2 and Q4.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words, no management language.** Belden buys copper, optical fibre, plastics and electronic components, makes cable, connectors, patch panels, racks, industrial Ethernet switches, firewalls and signal-extension gear in plants in the US, Mexico, Europe, China, India and Tunisia, and sells them mostly through electrical and data distributors (the largest distributor was **about 14% of 2025 revenue**) off published price lists, with the rest direct to equipment makers and installers. In FY2025 it sold **$2,715.2M** at a **38.0% gross margin**; selling and administration took 19.6% of revenue, R&D 4.7%, amortization of acquired intangibles 2.0%, leaving **GAAP operating income of $315.7M (11.6%)**. Two segments: Automation Solutions (factories, warehouses, energy, transport; $1,495.8M revenue, segment EBITDA 21.0%) and Smart Infrastructure Solutions (buildings, data centres, broadband operators; $1,219.4M, segment EBITDA 12.1%). Copper is passed through: *"When the costs of raw materials increase, we are generally able to recover these costs through higher pricing of our finished products"*, with price lists *"which we update from time to time, with new prices typically taking effect a few weeks after they are announced"* (Item 1). Revenue moves mainly with the volume of the markets it serves: *"We generally expect that our unit sales volume will increase or decrease consistently with the market growth rate"* (MD&A). Backlog is short ($567.7M at 2025 year-end, almost all shipping within the year).
- **Since 2026-07-01 a third piece:** RUCKUS sells enterprise Wi-Fi access points, campus switches and cloud network management through channel partners: $686.8M of 2025 revenue at a **65.7% gross margin** but a **7.3% operating margin** after spending **17.9% of revenue on R&D** ($122.6M; RUCKUS audited combined statements in the 8-K/A, as carried into EX-99.3). **The year before it lost money: 2024 net sales $521.2M, operating loss $(30.0)M, gross margin 56.5%** (same audited statements).
- **The scarce input this business controls.** Brands with installed specification positions (Belden, Hirschmann, Alpha Wire, PPC, West Penn Wire, ProSoft), a distribution shelf, and the engineering to certify cable and connectivity to published standards. The registrant does not claim control of any input that others cannot buy: raw materials have *"either alternative sources of supply or access to alternative materials"*, and it names its own differentiation as *"our ability to offer complete network solutions that solve customer problems, the breadth of our product portfolio, the quality and performance characteristics of our products, our customer service, and our technical support"*. Recorded here as a fact about the unit economics; whether it is a franchise is Q2's question.
- **Will the fundamentals look broadly the same in ten years?** The **mechanics** have been the same since the FY2014 10-K: specified cable and connectivity and industrial networking gear, bought through distribution, copper passed through, volume following the markets. The **portfolio** has not been stable, and the filings show it plainly: Grass Valley (broadcast) bought March 2014 and sold July 2, 2020; Tripwire (cybersecurity software) bought January 2, 2015 and sold February 22, 2022; PPC Broadband and Miranda bought 2012; RUCKUS (enterprise Wi-Fi) bought July 1, 2026 for 43% of the company's market value. The company that will exist in ten years depends on what management buys and sells, not on what the plants make.
- **Relatively simple and stable in character [E3-31]?** The cable and connectivity business is simple. The mix is not stable. I can write how each piece makes money without management's language, and the filings let me trace each purchase and sale; the portfolio churn is a fact about capital allocation and the franchise, taken at Q2 and Q3, not a failure to understand how a cable, a switch or an access point earns money. **This is not [E4-46]'s months-of-study case**: the Q2 test turns on documents I have.
- **VERDICT: [x] IN**: the money is made visibly, by selling specified physical products through distribution at list prices that pass copper through, with volume set by the served markets; RUCKUS adds a high-gross-margin, high-R&D product line I can also describe. **IN is not a finding on the franchise, and it carries a stated caution, not a caveat on the evidence: the mix of what is owned has changed every few years.**
## Q2 — IS IT A FRANCHISE? **[E3-03]**

*Every Belden figure below is read from the filed statements and MD&A tables of the 10-Ks named at Step 0 (extractions `is_out.txt`, `bridges.txt`, `roc_out.txt`); RUCKUS figures from the audited combined statements in the 8-K/A of 2026-09-11 and from Vistance's FY2025 10-K. Peer margin series from XBRL (`peers_out.txt`), with one figure per peer checked against its filed statement (below).*

**[E3-03], criterion by criterion.** *"An economic franchise arises from a product or service that: (1) is needed or desired; (2) is thought by its customers to have no close substitute and; (3) is not subject to price regulation. The existence of all three conditions will be demonstrated by a company's ability to regularly price its product or service aggressively and thereby to earn high rates of return on capital."*

- **(1) Needed or desired [x]: passes.** Every building, factory, data centre and broadband network is wired and switched; $2,715.2M of 2025 revenue.
- **(2) No close substitute [ ]: fails, in the registrant's own words.** 10-K FY2025, Item 1, Competition: *"The markets in which we operate can be generally categorized as highly competitive with many players."* *"Based on available data for our served markets, we estimate that our market share across our segments ranges from approxim ately 5% to 15%."* *"The principal competitive factor in our markets is the ability to solve customer problems based on product features, quality, availability, price, customer support, and distribution coverage. [...] Some products are manufactured to meet published industry specifications and are less differentiated on the basis of product characteristics."* The customer is a distributor or contractor buying to a published standard: *"In general, our customers are not contractually obligated to buy our products exclusively, in minimum amounts, or for a significant period of time."* The company's own forward-looking statements list *"the presence of substitute products in the marketplace"* and *"competitive responses to our products"* as risks (EX-99.1 of 2026-07-01). **The newly bought RUCKUS line is described by its seller the same way**: *"The markets in which we participate are dynamic and highly competitive [...] The market for our products is also subject to rapid technological change"*, with named competitors *"Cisco Systems, Inc., Extreme Networks, Inc., Hewlett Packard Enterprise Development LP, Huawei Technologies Co., Ltd., and Ubiquiti Inc."* (Vistance 10-K FY2025, accession `0001193125-26-072523`, Item 1).
- **(3) Not subject to price regulation [x]: passes.** No administered price; Belden sets list prices.
- **The demonstration clause, read on the revenue bridges of every 10-K fetched (2013 to 2025).** Belden decomposes each year's revenue change in its MD&A. **Across twelve bridges the only named price factor is copper pass-through**, which moves both ways (*"Copper pass-through pricing contributed $36.7 million"* in 2025; *"Lower copper costs resulted in a $17.2 million decrease"* in 2019; *"Copper prices had a $117.2 million favorable impact"* in 2021), and passes cost through, which is not pricing power: Item 1 says so, *"When the costs of raw materials increase, we are generally able to recover these costs through higher pricing"*. **Price beyond copper appears once, in the inflation of 2022-2023**: *"Higher sales volume and favorable pricing from industrial automation, smart buildings, and broadband products resulted in a $365.0 million increase"* (2022, volume and price not separated) and *"Gross profit increased $38.7 million from 2022 to 2023 primarily due to favorable product mix and pricing. Gross profit margins were robust, expanding 280 basis points from 35.2% to 38.0%"* (FY2023 10-K). That window is shared with every maker of wire in America (Encore Wire's gross margin went from 15.2% in 2020 to 36.9% in 2022 and back to 25.5% in 2023, row below), which is [E2-58]'s *"supply-tight"* year, not a franchise's regular price. The MD&A's own statement of how the business grows is volume, not price: *"We generally expect that our unit sales volume will increase or decrease consistently with the market growth rate."*

**Margins and returns, Belden as filed** (continuing operations in each 10-K):

| year | revenue | gross margin | GAAP operating margin | source 10-K |
|---|---|---|---|---|
| 2012 | $1,840.7M | 30.8% | 5.9% | FY2014 |
| 2013 | $2,069.2M | 34.0% | 9.7% | FY2014 |
| 2014 | $2,308.3M | 35.5% | 7.1% | FY2014 / FY2016 |
| 2016 | $2,356.7M | 41.6% | 9.5% (10.5% before a $23.9M held-for-sale impairment) | FY2016 |
| 2017 | $2,087.2M | 38.4% | 11.2% | FY2019 |
| 2018 | $2,165.7M | 38.3% | 14.5% (11.6% without the $62.1M patent-litigation gain) | FY2019 |
| 2019 | $2,131.3M | 37.2% | 9.7% | FY2019 |
| 2020 | $1,752.2M | 32.9% | 8.6% | FY2022 |
| 2021 | $2,301.3M | 33.5% | 11.5% | FY2022 |
| 2022 | $2,606.5M | 35.2% | 13.9% (12.5% without the $37.9M gain on sale) | FY2022 |
| 2023 | $2,512.1M | 38.0% | 12.6% (12.2% without the $12.1M real-estate gain) | FY2025 |
| 2024 | $2,461.0M | 37.5% | 10.8% | FY2025 |
| 2025 | $2,715.2M | 38.0% | **11.6%** | FY2025 |

(2012-2016 carry Grass Valley's broadcast business inside continuing operations; from the FY2019 10-K on it is discontinued, and Tripwire from the FY2022 10-K. The perimeter changes under the series; no year shows the operating margin above 14.5% as filed.)

**Returns on capital [E3-46], the goodwill wedge reported separately [E2-43, E2-73]** (pretax operating income, one-offs out, against total assets less cash, right-of-use and discontinued assets, trade payables, accrued liabilities, deferred tax and other long-term liabilities; `roc.py`):

| year-end | operating income | on capital INCLUDING goodwill and intangibles | on net tangible operating assets |
|---|---|---|---|
| 2013 | $201.3M | **11.9%** | 37% |
| 2016 | $247.8M | **10.7%** | 67% |
| 2019 | $207.2M | **10.8%** | 61% |
| 2022 | $325.4M | **19.5%** | 58% |
| 2025 | $315.7M | **14.3%** | 41% |

The plants earn good returns on the tangible capital they use ([E2-73]'s measure for judging the operators). **The owner has earned 11-14% pretax on what was paid in most years**, peaking at 19.5% in the supply-tight 2022. **After RUCKUS it is lower**: on the pro forma balance sheet of EX-99.3 (capital including goodwill about $4,046M) the pro forma 2025 operating income was **$116.8M GAAP, 2.9%**, and **$442.5M, 10.9%**, even after adding back all $250.7M of amortization and the $75.0M inventory step-up. RUCKUS itself, for which $1,907.6M was paid (EX-99.3, Note 4), earned **$100.0M before amortization of purchased intangibles in 2025 (5.2% pretax on the price) and $19.9M in 2024 (1.0%)**.

**[E4-04] and the acquired line: the buyer's own filing says the advantage it bought lasts five years.** EX-99.3 values RUCKUS's *"Developed technologies"* at **$800,000K, amortized over 5.0 years**, and gives the reason: *"The preliminary useful life for the developed technology intangible asset was based on the estimated time that the technology provides us with a competitive advantage and thus approximates the period and pattern of consumption of the intangible asset."* Trademarks are given 3.0 years (*"the period of time we expect to continue to go to market using the trademarks"*). RUCKUS spent **17.9% of 2025 revenue on R&D** to stay current. This is [E4-04]'s *"moat that must be continuously rebuilt"* stated as an accounting estimate by the acquirer, and [E3-51]'s competitive destruction in the category Belden just bought 43% of its market value into. **Under the 2026-09-20 ruling this is a competence limit, recorded and not relied on**: the verdict below does not need it.

**[E4-23]:** no superstar dependence found; the business does not rest on one manager. **[E2-44], characteristic (2):** growth has been bought: goodwill and intangibles went from $1,150.0M (2013) to $1,436.6M (2025) to about $3,206M pro forma after RUCKUS.

**Direction [E4-32]:** flat on the core (operating margin 11.2% in 2017, 11.6% in 2025; returns including goodwill 10.7-14.3% outside 2022), and down on the whole after 2026-07-01 (the RUCKUS price earns less than the core).

**THE COMPETITOR ROW — required [E3-28].**

| Company | gross margin (own statement) | GAAP operating margin | window | source |
|---|---|---|---|---|
| **Belden** | 2016 41.6% · 2019 37.2% · 2021 33.5% · 2023 38.0% · 2025 38.0% | 9.5% · 9.7% · 11.5% · 12.6% · 11.6% | 2016-2025 | Belden 10-Ks above |
| **Amphenol** (connectors, cable assemblies, fiber; bought CommScope's connectivity and cable business in 2025) | 32.5% · 31.8% · 31.3% · 32.5% · 36.9% | **19.2% · 19.7% · 19.4% · 20.4% · 25.4%** | 2016-2025 | XBRL; 2025 checked against the filed 10-K FY2025 `0001104659-26-013549`: net sales $23,094.7M, operating income $5,868.6M |
| **CommScope, now Vistance Networks** (broadband and enterprise connectivity; the seller of RUCKUS) | 41.2% · 28.8% · 36.2% · 48.3% · 49.5% | 11.5% · **-6.1% · 2.9% · -35.4% · 2.5%** | 2016-2025 (perimeter shrank to RUCKUS and Aurora after 2023 divestitures) | XBRL; 2025 checked against the filed 10-K FY2025 `0001193125-26-072523`: net sales $1,931.6M, operating income $47.6M |
| **RUCKUS segment inside Vistance** | n/a | **2024 -8.2% · 2025 6.2%** (segment operating income $(44.8)M and $43.0M) | 2024-2025 | Vistance 10-K FY2025, segment table |
| **Corning** (whole company; optical communications is one segment) | 40.1% · 35.1% · 36.0% · 31.2% · 36.0% | 15.2% · 11.4% · 15.0% · 7.1% · 14.6% | 2016-2025 | XBRL; 2025 checked against the filed 10-K FY2025 `0000024741-26-000124`: net sales $15,629M, operating income $2,279M |
| **Encore Wire** (US copper building wire; bought by Prysmian 2024, last 10-K FY2023) | 12.8% · 13.0% · 33.5% · 25.5% · n/a | 5.4% · 5.6% · 27.0% · 17.6% · n/a | 2016-2023 | XBRL; 2023 checked against the filed 10-K FY2023 `0000850460-24-000017`: net sales $2,567,722K, operating income $451,373K |

- **Peers named: 4 SEC filers plus one segment**, of an industry the registrant calls *"highly competitive with many players"*. Not taken: the enterprise networking rivals the seller names for RUCKUS (Cisco, HPE, Extreme, Ubiquiti, Huawei), and the industrial networking and connectivity makers Belden meets in automation (several are foreign or private and file nothing with the SEC). **The verdict does not rest on the row**: it rests on the registrant's own statements under criterion (2) and its own revenue bridges.
- **What the row shows [E3-61]:** in connectivity, the same inputs and channels earn **Amphenol 19-25% operating margins every year, against Belden's 9-13%**: the business that does have an advantage in this field is not Belden. The seller of RUCKUS posted an operating loss in five of the ten years 2016-2025 (2019, 2020, 2022, 2023, 2024; XBRL series in `peers_out.txt`). Encore Wire shows what the 2021-2022 copper-and-supply window did to everyone's margin and how fast it went.
- **Untapped pricing power [E3-33], [E5-28]:** none claimed and none visible; a 5-15% share in a field of many players is not near-monopoly.
- **Class: [x] NONE** · **Direction: flat on the core, down after RUCKUS.**

**THE STRONGEST EVIDENCE AGAINST THIS VERDICT, hunted hardest [E4-26, E3-41, E4-51].**
1. **Gross margin rose from 33.5% (2021) to 38.0% (2023) and held at 37.5-38.0% through 2025**, and the FY2023 10-K credits *"favorable product mix and pricing"*. If price rose and held after copper and supply normalised, that is a price the customer paid for the brand.
2. **The tangible returns are high** (41-67% pretax on net tangible operating assets), and specified brands such as Belden and Hirschmann carry installed positions in industrial plants where a cable or switch failure stops a line.
3. **RUCKUS raised price in 2025**: Vistance's MD&A says RUCKUS operating income rose *"primarily due to higher sales volumes and pricing"*, and its gross margin went from 56.5% to 65.7%.
4. **Belden's R&D and solution selling are aimed at moving from product to system** (*"our ability to offer complete network solutions"*), which could make the whole less substitutable than the parts.

**Answered.** (1) The margin gain came in the window when Encore Wire's margin doubled and fell back; Belden's **operating** margin did not follow its gross margin up (12.6% in 2023, 10.8% in 2024, 11.6% in 2025, against 11.2% in 2017), because SG&A and R&D rose with it (*"strategic investments"*): the gross-margin gain was spent to hold position, which is [E3-62]'s second step, the gains *"flow through"* rather than *"stay home"*. (2) High returns on tangible assets with 11-14% on what the owner paid is [E2-43]'s distinction, and [E2-73] judges the operators with it, not the business. (3) One year of RUCKUS pricing after a year of losses, in a category whose buyer amortizes the technology over five years, is not *"regularly"*. (4) A strategy is not a moat [E4-32]: the filings show the direction flat. **None of the four reaches criterion (2)**, which the registrant answers against itself, and the attacker's test [E2-45] is answered by the row: Amphenol, with the same inputs and channels, earns about twice Belden's margin.

- **VERDICT: [x] OUT**: on the business. **[E3-03] criterion (2) fails in the registrant's own words** (*"highly competitive with many players"*, a 5-15% share, products *"manufactured to meet published industry specifications and [...] less differentiated"*, *"the presence of substitute products in the marketplace"*), and the line bought on 2026-07-01 is described by its seller the same way, against Cisco, HPE, Extreme, Huawei and Ubiquiti. **The demonstration clause fails on twelve years of the company's own revenue bridges**: the only regular price factor is copper passed through; the one period of real price (2022-2023) was the supply-tight window every wire maker shared, and it did not lift the operating margin, which was 11.2% in 2017 and 11.6% in 2025. **Returns on what the owner paid are 11-14% pretax in most years**, and about 11% on the pro forma company before any amortization, the new line earning 5.2% on its price in its best year. This is [E2-58]'s class, a business in which *"differentiation simply can't be made meaningful"* for most of what is sold, run by an operator whose tangible returns are good: [E2-37]'s remarkable textile company. **The file closes here.** Q3 to Q6 are not opened as gates; the material gathered beneath the close follows without verdicts.
## MATERIAL BENEATH THE CLOSE: recorded, not governing

*The file closed at Q2, OUT on the business. What follows is recorded the way the USPH, HUBG, WS and CAH runs recorded
theirs: no verdict box is ticked for Q3-Q6, nothing here reopens Q2, and nothing here is a clearance. It is written
because the brief asked for the working-capital, acquisition-line and SBC checks, and because the RUCKUS purchase
changes what the quote is buying in ways the next reader should know.*

### Q3 prompts (no verdict)
- **Weight case, had the gate opened: a GATE, on leverage [E3-29] and daily execution [E3-38].** After 2026-07-01 the
  company carries about **$3.15bn of gross debt** (senior subordinated notes $1,248.5M carrying value at 2026-06-28, all
  euro-denominated, due 2028, 2031 and 2033; the $1,850.0M secured term loan; $50.0M drawn on the revolver on
  2026-06-29) against **$1.26bn of book equity** at 2025 year-end and pro forma long-term debt of $3,053.1M (EX-99.3).
  The RUCKUS line competes on product cycles against Cisco, HPE and Huawei. **Control [E1-16]**: none; one class of
  common stock.
- **Honesty [E5-16]: no finding of personal misconduct in any document read** (10-Ks FY2014-FY2025, the 2026 10-Q, the
  2026 proxy, the deal 8-Ks). The filing index shows an 8-K Item 5.05 (code of ethics) on 2020-08-25 and 2025-08-27;
  neither was opened. Litigation was not searched.
- **[E4-29], EBITDA and adjusted-earnings promotion: FIRES, at full strength in the releases.** The 10-K MD&A carries a
  full *"Consolidated Adjusted EBITDA"* table beside the GAAP one; the deal release priced RUCKUS at *"approximately 13x
  projected 2026 Adjusted EBITDA"* and promised it would be *"Immediately accretive to Adjusted EPS"*; the Q2 2026
  release (EX-99.1 to the 8-K of 2026-07-30, accession `0000913142-26-000031`) headlines *"Adjusted EPS of $2.34, up 24%
  y/y"*. **The sharpest instance is the Q3 2026 guidance in the same release: GAAP EPS $0.69-$0.84 against Adjusted EPS
  $2.15-$2.30**, the gap led by *"Amortization of intangible assets"* of $0.94 a share. The largest piece of that
  amortization is the $800M of RUCKUS *"Developed technologies"* written off over five years, which the company's own
  pro forma note says is *"the estimated time that the technology provides us with a competitive advantage"*. **An
  expense the filer itself calls the cost of staying competitive is the item its headline removes**: [E5-41]'s reverse
  float, and [E2-26]'s half-owner test fails in the release (the 10-K reconciles it in full; the headline does not).
- **[E4-22] third flag, projections: FIRES** (quarterly EPS guidance every quarter; the 2025 proxy states strategic plan
  goals of *"10-12% compound annual EPS growth"* and *"Net leverage of 1.5X"*; the deal release: *"net leverage of ~1.5x
  by 2029"*). The [E3-48] action, past guidance against outturn, was **not performed**.
- **[E4-27], incentives, read in the DEF 14A of 2026-04-09 (`0000913142-26-000011`).** The annual cash incentive for the
  CEO and three other officers is *"Consolidated Net Income 40% | Consolidated EBITDA 30% | Consolidated Revenues 30%"*;
  the CEO's 2025 financial factor was 0.85 and his award $1,149,094. The PSUs (half of long-term pay) vest on *"relative
  total stockholder return and free cash flow"* over three years, and *"PSUs issued in February 2025 have the potential to
  be enhanced if Company achieves $10.00 or more of adjusted EPS by the end of 2028"*. The company-selected measure in the
  pay-versus-performance table is Adjusted EPS. **Pay does not vest on return on capital, on owner earnings per share, or
  on anything that charges the price of an acquisition**; 30% of the annual bonus rises with revenue, which a purchase
  supplies, and the EPS stretch is measured after excluding the amortization the purchase creates. A prompt, not a finding
  about motive.
- **[E2-30] institutional imperative, (2) acquisitions to soak up funds: a prompt, on the record.** Tripwire was bought
  on January 2, 2015 *"for a purchase price of $703.2 million"* (FY2016 10-K), impaired by $131.2M in 2021, and sold on
  February 22, 2022 *"for gross cash consideration of $350 million"* (FY2022 10-K). Grass Valley was bought in March 2014,
  impaired by $521.4M in 2019 and $113.0M in 2020, and sold on July 2, 2020 (proceeds from disposal of businesses $54.8M
  that year). RUCKUS was bought on 2026-07-01 for about $1.9bn with debt, at 5.2% pretax on the price in its best year
  (Q2). [E2-56]'s camouflage test applied: the core's tangible returns hide the purchases' returns in the blended series.
  **[E4-39]: no acquisition post-mortem against the announcement case found in any filing read.**
- **Buybacks [E5-08]**: $192.1M (2023), $134.3M (2024), $195.6M (2025, *"1.7 million shares [...] at an average price
  per share of $113.00"*), paused after the deal (*"Belden intends to temporarily pause share repurchases"*). Condition (1)
  was met before 2026. Condition (2), a material discount to value conservatively calculated, cannot be assessed without a
  gate that opened; the computation below puts no-growth value of the pre-RUCKUS company at the sovereign at about
  **$83-111 a share** (3-year owner earnings $180.5-240.5M over 5.49%, on 39.6M average shares), against which the 2025
  purchases at $113 were at or above the top. **Stated with the humility clause [E4-13]: they know the business better
  than I do.** A capital-allocation prompt, not a finding.
- **Serial issuance [E5-15]: not fired.** One issue in the window, the 2016 mandatory convertible preferred ($501.5M net),
  which paid $34.9M a year of preferred dividends 2017-2018 and converted in 2019 (shares outstanding 39.4M at 2018 year-end,
  45.5M at 2019 year-end); buybacks since have taken the count to 39.1M. Shares are also issued each year to the
  retirement plan (below).
- **Primary test [E2-01]**: net income over year-end equity 18.8% (2025), 22.3% (2022), with equity reduced by
  $911.9M of treasury stock; the series is flattered by buybacks and debt, so the Q2 table on operating capital is the
  honest read. **Cash-tax tell [E4-30]**: income taxes paid net of refunds $55.7M (2023), $45.3M (2024), $33.3M (2025)
  against pretax income $285.8M, $227.9M, $266.9M: about 19.5%, 19.9%, 12.5%; 2025 includes *"the release of uncertain
  tax position reserves"*. The tax note was not read further; a prompt only.
- **The half-owner test [E2-26]**: the 10-K discloses and reconciles every adjustment; the releases lead with the adjusted
  figure (above). Candor in the filing, promotion in the release: the CGNX pattern the queue's brief rule records.

### Q4 prompts: owner earnings the corpus's way [E2-23], every window [E4-25]
*OCF − SBC − stock paid into the retirement plan − (c), then preferred dividends; no net-income proxy. Every input typed
from the filed Consolidated Cash Flow Statements of the 10-Ks FY2014, FY2016, FY2019, FY2022 and FY2025, the equity
statements, and the income statements for the amortization of acquired intangibles. Script `oe.py`, output `oe_out.md`.*

**SBC: THE TAG RESOLVES, BUT THE SUBTRACTION WAS NOT COMPLETE.** The cash-flow line *"Share-based compensation"*
resolves in every filed year 2012-2025 ($12,374K to $30,015K), and the XBRL tag `ShareBasedCompensation` the screen used
equals it in every year it carries (2015-2025; the tag is absent from the annual frames for 2013 and 2014, where the
filed lines are $14,854K and $18,858K). **A second equity-settled expense sits outside that line**: the equity statements
carry *"Retirement Savings Plan stock contributions"* of **$2,654K (2020), $6,888K (2021), $7,017K (2022), $7,798K
(2023), $7,586K (2024), $9,044K (2025)**, and Note 18 confirms *"Benefits provided to employees under defined
contribution plans include cash and stock contributions by the Company"*. Paid in shares, it is a non-cash expense left
inside operating cash; it is stock compensation under [E5-06] and is subtracted here. The [E3-70] market-value measure was
not computed (no options granted to officers in 2025; RSUs and PSUs are valued at grant).

**The brief's wc_note, read: the 2021 payables swing did NOT make the cash.** FY2022 10-K cash-flow statement, 2021:
accounts payable **+$135,666K** (50% of the $272,055K OCF), but receivables **−$119,012K**, inventories **−$92,984K**,
accrued liabilities +$61,241K, income taxes −$6,448K, other assets −$12,693K, other liabilities −$20,642K: **working
capital as a whole consumed $54.9M in 2021** as revenue rose 31% ($1,752.2M to $2,301.3M). Payables financed part of
the receivable and inventory build; they did not create cash. 2022 consumed a further $53.8M. The same pattern shows in
2017 (payables +$100,752K, inventories −$84,088K). **The windows are not inflated by the swing; if anything 2021-2022
are depressed by the build.** The screen's flag reads one line in isolation; a note naming the net of all
working-capital lines would have answered itself.

**The brief's acq_note, read: there was no $589M net inflow. It is a tooling artefact.** The acquisition line was a
small inflow in two years only: **2020, $590K** (*"Cash from (used for) acquisitions and investments, net of cash
acquired | 590"*, FY2022 10-K) and **2025, $7,744K**, which Note 4 explains: *"During 2025, we received $ 7.9 million
related to an adjustment of the consideration paid"* for Precision Optical Technologies. **$589M is the SUM OF THE
ABSOLUTE VALUES over 2021-2025** ($73.3M + $104.6M + $106.7M + $296.5M + $7.7M): `Screens/floor_screen.py` line 711
prints *"NET CASH INFLOW on the acquisition line"* whenever any one year is negative, and labels the five-year gross
total with it. The real record is **$573M paid out net over 2021-2025** (plus $3.65M of intangible assets bought in 2021), plus RUCKUS in 2026. (Reported below as a
tooling defect, not patched.)

**Discontinued operations are inside the filed cash flows.** The FY2022 10-K: *"The Consolidated Cash Flow Statement
includes the results of our discontinued operations up to their disposal date - February 22, 2022 and July 2, 2020 for
Tripwire and Grass Valley, respectively."* So **2014-2020 carry Grass Valley** (which lost money: pretax $(9.8)M in
2018 before its 2019 impairment) and **2015-2022 carry Tripwire**. **Only 2023-2025 are the current perimeter before
RUCKUS**; 2022 carries Tripwire for 53 days. Each window below says what it contains.

**(c), a disclosed guess [E2-09].** The band runs from full capital expenditure to a depreciation proxy (cash-flow D&A
less the amortization of acquired intangibles, which is not a renewal cost; for 2017-2019 the discontinued Grass Valley
amortization given in the FY2019 note is also removed, and for 2020-2021 the disposal groups' amortization is removed
only where the notes give it, so the proxy is overstated in those years, the conservative direction). **Capex has run
above the depreciation proxy every year since 2018** ($136.2M against $76.1M in 2025, 1.8 times) while revenue grew
about 25% from 2018 to 2025 with acquisitions; the filings do not split capex into maintenance and growth. Belden is not
[E5-20]'s class by its own words (capex 5.0% of revenue), but the persistent excess and the inflation of 2021-2023
[E4-47] put the honest (c) **nearer the capex end**. Normalised down [E4-41]: the $62.1M patent-litigation gain of 2018
removed from that year's operating cash.

| FY | OCF | SBC | 401(k) stock | capex | D&A | depreciation proxy | OE, c = capex | OE, c = proxy | preferred dividends | **OE to common, low..high** | acquisitions paid | divestitures received |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2012 | 139.4 | 12.4 | 0.0 | 41.0 | 59.4 | 36.6 | 86.0 | 90.5 | 0.0 | **86.0..90.5** | 860.4 | 299.8 |
| 2013 | 164.6 | 14.9 | 0.0 | 40.2 | 94.5 | 43.6 | 106.1 | 109.5 | 0.0 | **106.1..109.5** | 10.0 | 3.7 |
| 2014 | 200.9 | 18.9 | 0.0 | 45.5 | 102.2 | 43.7 | 136.6 | 138.3 | 0.0 | **136.6..138.3** | 347.8 | -1.0 |
| 2015 | 241.5 | 17.7 | 0.0 | 55.0 | 150.3 | 46.6 | 168.7 | 177.2 | 0.0 | **168.7..177.2** | 695.3 | 3.5 |
| 2016 | 314.8 | 18.2 | 0.0 | 54.0 | 145.6 | 47.2 | 242.6 | 249.4 | 15.4 | **227.2..234.0** | 18.8 | 0.0 |
| 2017 | 255.3 | 14.6 | 0.0 | 64.3 | 149.7 | 45.7 | 176.4 | 195.0 | 34.9 | **141.5..160.1** | 166.9 | 0.0 |
| 2018 (patent gain out) | 289.2 | 18.5 | 0.0 | 97.8 | 148.6 | 49.8 | 110.7 | 158.8 | 34.9 | **75.8..123.8** | 84.6 | 40.2 |
| 2019 | 276.9 | 17.8 | 0.0 | 110.0 | 139.3 | 51.9 | 149.1 | 207.3 | 18.4 | **130.7..188.8** | 74.4 | 0.0 |
| 2020 | 173.4 | 20.0 | 2.7 | 90.2 | 108.7 | 79.6 | 60.5 | 71.0 | 0.0 | **60.5..71.0** | -0.6 | 54.8 |
| 2021 | 272.1 | 24.9 | 6.9 | 91.0 | 88.0 | 49.6 | 149.3 | 190.7 | 0.0 | **149.3..190.7** | 77.0 | 45.7 |
| 2022 | 281.3 | 23.7 | 7.0 | 105.1 | 88.7 | 50.2 | 145.5 | 200.4 | 0.0 | **145.5..200.4** | 104.6 | 334.6 |
| 2023 | 319.6 | 21.0 | 7.8 | 116.7 | 99.4 | 59.1 | 174.1 | 231.7 | 0.0 | **174.1..231.7** | 106.7 | 9.3 |
| 2024 | 352.1 | 27.5 | 7.6 | 129.1 | 115.7 | 66.9 | 187.9 | 250.0 | 0.0 | **187.9..250.0** | 296.5 | -1.3 |
| 2025 | 354.9 | 30.0 | 9.0 | 136.2 | 129.4 | 76.1 | 179.6 | 239.7 | 0.0 | **179.6..239.7** | -7.7 | 0.0 |

*$M. 2014 OCF as restated in the FY2016 10-K ($200,887K; the FY2014 10-K had $194,028K). 2013 OCF carries an accrued-tax
outflow of $89,427K, most likely tax on the 2012 business sale; left as filed (the conservative direction), not verified.*

| window | OE to common, mean | yield on $4,394.3M | acquisitions paid a year | divestitures received a year |
|---|---|---|---|---|
| FY2023-2025 (3y, the current perimeter before RUCKUS) | $180.5M..$240.5M | 4.11%..5.47% | $131.8M | $2.7M |
| **FY2021-2025 (5y, the default [E2-42]; Tripwire in 2021 and 53 days of 2022)** | **$167.3M..$222.5M** | **3.81%..5.06%** | $115.4M | $77.7M |
| FY2022-2025 (4y) | $171.8M..$230.5M | 3.91%..5.24% | $125.0M | $85.6M |
| FY2016-2025 (10y; Grass Valley to 2020, Tripwire to 2022) | $147.2M..$189.0M | 3.35%..4.30% | $92.1M | $48.3M |
| FY2016-2020 (5y) | $127.1M..$155.6M | 2.89%..3.54% | $68.8M | $19.0M |
| FY2012-2025 (14y, every filed cash-flow statement read) | $140.7M..$171.8M | 3.20%..3.91% | $202.5M | $56.4M |

**In words.** No year's owner earnings to common is near zero or negative; the low is **2020, $60.5-71.0M**, the COVID
year with Grass Valley's last half inside. The recent windows sit within $167-241M; the width is mostly the (c) band
(about $55-60M a year), because capex has run well above depreciation. The screen's $175-201M and `run.py`'s $189-201M
(3-year) sit inside this range; they omitted the retirement-plan stock ($7.6-9.0M a year) and used the full D&A as one
(c) end, which includes acquired amortization. **All of it describes a company that no longer exists**: see below.

**THE PERIMETER AFTER 2026-07-01 (the brief's deal question, answered from the filings).**
1. **RUCKUS's own owner earnings** (audited combined statements, 8-K/A): OCF **$167.3M (2025), $(14.6)M (2024)**; equity
   compensation $8.7M and $5.6M; capex $2.2M and $3.3M; so **$156.4M and $(23.5)M**. Working capital swung the two years
   in opposite directions (+$64.4M in 2025, of which payables +$34.0M and accrued liabilities +$44.5M; −$34.2M in 2024),
   so the two-year mean is **$66.4M as filed, $51.4M with working capital neutralised**. Its cash statements are a
   carve-out (*"Financing transactions with Parent, net"*), with no interest and stand-alone taxes.
2. **The price of it in interest.** The pro forma (EX-99.3, note T) adds **$115.0M a year** of term-loan interest and
   issuance-cost amortization (about $109.5M in cash, at SOFR + 2.25% on $1,850M); after tax at the 12.5-19.9% cash rate
   above, about $88-96M; plus the income lost on roughly $100M of cash used.
3. **Pro forma owner earnings to common, a guess [E2-09]: about $120M to $220M a year** (3-year Belden $180.5-240.5M, plus
   RUCKUS $51.4-66.4M, less $88-114M of new interest). **The purchase added to the numerator about what it added in
   interest, at best**; at the conservative end it subtracts. The default five-year base gives about $105-200M.
4. **The denominator**: goodwill and intangibles about $3,206M pro forma against $1,436.6M before; pro forma long-term
   debt $3,053.1M against $1,285.7M.

- **Great, good or gruesome [E4-20]**: the core earns 41-67% pretax on net tangible assets and 11-14% on what was paid;
  the purchases earn less, and the latest earns 1-5% on its price. Between **good** and **gruesome**, and the last
  purchase moves it toward the second. Not scored: the gate did not open.
- **Staying power [E5-11]**: (1) a reliable stream: owner earnings positive in every year 2012-2025, low $60.5M in 2020;
  (2) liquid assets: cash $348.7M at 2026-06-28 before the RUCKUS payment, pro forma $338.7M; revolver $400M; (3)
  near-term cash requirements: the **€350M 3.875% notes due 2028** (carrying $397.3M), the term loan's 1% a year
  amortization, and the covenants now on it (*"limits certain payments, including dividends"*, secured on *"substantially
  all of the assets"*). **Coverage [E2-54]**: pro forma 2025 interest $161.1M against pre-interest operating cash less capex
  of roughly $360-430M (Belden 2025: $354.9M OCF plus $43.2M interest paid less $136.2M capex = $261.9M; RUCKUS 2025:
  $165.1M as filed, about $101M with working capital neutralised): about two and a half times covered in a good year. **In a 2020-type year it is not
  covered**: Belden's 2020 operating cash less capex was $83.1M plus $58.9M of interest added back, about $142M, against
  $161M. **Leverage [E4-16]**: about 3.15bn gross against a 4.4bn quote, and the notes are in euros against a
  dollar-reporting company.
- **Named death, as a signature only: #10 THE CAMOUFLAGE, with leverage as a feature.** Cash from the core, which earns
  high returns on the plant it uses, has been recycled into lines that must re-win a technology race (Grass Valley
  broadcast, Tripwire software, now RUCKUS Wi-Fi, whose buyer amortizes the technology over five years); two of the three
  were written down by $765.6M in total and sold, and the third was bought with secured debt equal to 42% of the market
  value. **#11 THE PASS-THROUGH is present as a feature** (the 2022-2023 margin gain spent on SG&A and R&D; operating margin
  flat). **Quantified**: a 2020-type year (revenue −18%, owner earnings $60.5-71.0M) with the new $161M interest bill leaves
  owner earnings to common near zero or below; the company survives it on the revolver and the 2031-2033 maturities.
  **Not entered in the index's instances column** (file closed at Q2; the PAGP, CALM and USPH precedent). **No new
  shape.**

### COMPUTATION — NOT A CLEARANCE
*No box, no ranking, no entry language.* Price and count from Step 0 (**$112.45**, NYSE close 2026-09-25, aggregator,
flagged; **39,078,191 shares**; cap **$4,394.3M**). **Before RUCKUS**, on the default five-year window FY2021-2025, owner
earnings to common of **$167.3M to $222.5M are 3.81-5.06% of the cap**; on the three-year window, 4.11-5.47%; all against
the **5.49%** sovereign (US Treasury 30-year par, 09/25/2026, Step 0) and far below the ~10% floor **[E4-28]**. **After
RUCKUS**, on the pro forma guess of about **$120M-$220M, 2.7-5.0%**. At the floor with no growth, $120-220M capitalises to
**$1.2-2.2bn, about $31-56 a share**; at the sovereign with no growth, **$2.2-4.0bn, about $55-102 a share**, against
$112.45 quoted. The year-1 growth the quote needs to reach the floor is roughly **5-7% in perpetuity** on these earnings,
against a core whose operating margin was 11.2% in 2017 and 11.6% in 2025, and a volume that *"will increase or decrease
consistently with the market growth rate"*. **Windage count: ONE** (the conservative (c) end; no premium in the rate
**[E3-42]**). Upside ceiling **[E2-63]**: a 5-15% share in markets of many players.

### Q6: reversal conditions, in words (no alert: the file failed on the business)
The Q2 verdict would reopen on **filed evidence that Belden sets its own price**: several years of revenue bridges that
name price, apart from copper, as a regular positive factor outside a supply-tight year, with the **operating** margin
(not the adjusted EBITDA margin) rising toward the connectivity leader's (Amphenol 19-25%) and returns on capital including
goodwill rising above the 11-14% band; and **evidence that the RUCKUS line keeps its position without its technology
having to be re-bought every five years** (R&D falling as a share of its revenue while its share and price hold).
**Next dates**: the Q3 2026 10-Q (about late October 2026), the first quarter with RUCKUS consolidated and the purchase
price allocation; the FY2026 10-K (about February 2027) with the final allocation, the developed-technology life and the
first goodwill test.

---
⛔ **Q5 does not open: Q2 is OUT.** The computation above is headed as the protocol requires and carries no box.

## Q5: not opened. Q6: not opened as a gate (reversal conditions in words above).
---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN, Q2 OUT; the file closed at Q2; Q3-Q6 recorded beneath
      the close without boxes)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** (Q1 IN rests on the 10-K business
      descriptions FY2014-FY2025, the FY2025 statements and the RUCKUS audited statements, all read; the portfolio churn
      it records is a stated fact from the filings, not a gap in the evidence)
- [x] Every UNRESEARCHED verdict names the artifact and where it lives (none issued)
- [x] Every UNKNOWABLE verdict states what specifically cannot be known (none issued; [E4-04]'s perimeter close was not
      needed because [E3-03] criterion (2) fails first, in the registrant's own words)
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked (FY2025 OCF $354,864K in the filed
      statement = tag; FY2024 and FY2023 the same; each peer's revenue and operating income checked against its filed
      FY2025 or FY2023 10-K)
- [x] Owner earnings on a multi-year mean; every window FY2012-FY2025 published with both (c) ends and what perimeter each
      contains; no year near zero or negative (low: 2020, $60.5-71.0M); SBC resolves in every year and the retirement-plan
      stock outside the SBC line was found and subtracted; preferred dividends 2016-2019 subtracted; the RUCKUS pro forma
      shown as a guess (beneath the close)
- [x] Competitor row filled (Amphenol, CommScope/Vistance with its RUCKUS segment, Corning, Encore Wire: same two metrics,
      2016-2025; the enterprise-networking and foreign industrial rivals not taken and named; the verdict does not rest
      on the row)
- [x] Sovereign is for the earnings currency, from the issuing authority, dated (5.49%, US Treasury 30-year par,
      09/25/2026, struck fresh; FRED not used)
- [x] Value stated as a round-number range, not a point estimate (computation only)
- [x] One bar chosen, not both; windage count stated (ONE; no bar applied, Q5 not opened)
- [x] Prices dated; aggregator used for the live quote only and flagged ($112.45, 2026-09-25 close, Yahoo chart endpoint,
      raw response saved)
- [x] Run committed to git (claim `a1d53b2e`, Step 0 and Q1 `d728f8bf`, Q2 `5fda147d`, beneath the close `bef125c2`,
      this section and the fold after)

**Brief priors, each tested:**
1. *deal_note: an EX-2.1 with an 8-K Item 1.01 of 2026-04-30; target or acquirer?*: **ACQUIRER.** Belden agreed to buy the
   RUCKUS segment of Vistance Networks for about $1.846bn cash (8-K `0000913142-26-000020`), **closed 2026-07-01** for
   about $1.87bn net of cash acquired, funded by a $1,850.0M secured term loan (8-K `0000913142-26-000029`); the 8-K/A of
   2026-09-11 (`0000913142-26-000037`) carries the audited RUCKUS statements and the pro forma. No termination and no vote.
   The quote is an owner-earnings price for a company whose perimeter changed three months ago; it is not a spread.
2. *wc_note: accounts payable moved 50% of 2021 OCF*: **confirmed as a line, refuted as a distortion.** Payables +$135.7M
   of $272.1M, but working capital as a whole consumed $54.9M that year (receivables −$119.0M, inventories −$93.0M).
3. *acq_note: a $589M net cash inflow on the acquisition line*: **refuted; a tooling artefact.** Inflows were $0.59M
   (2020) and $7.7M (2025, a Precision price adjustment). $589M is the sum of absolute values over 2021-2025.
4. *Grass Valley and Tripwire sold in earlier years*: **confirmed from the filings**: Grass Valley bought March 2014,
   sold July 2, 2020; Tripwire bought January 2, 2015 for $703.2M, sold February 22, 2022 for $350M gross; both inside
   the filed cash flows until their disposal dates.
5. *spread_caveat: rebuild the width beyond the 5-year window*: **done**: 3, 4, 5, 10 and 14-year windows, both (c) ends.
6. *level_shift 1.33, no step; no single-year dependence*: consistent with the rebuilt table; the one low year (2020) is
   the COVID and Grass Valley year, and the patent gain of 2018 is removed.

**Errors of mine caught before commit:** (1) I first wrote the market cap as $4,394.4M; 112.45 x 39,078,191 is
$4,394.3M; corrected in Step 0 before the fold. (2) I first wrote the 2021-2025 acquisitions as $581M net; the filed lines
sum to $573.4M; corrected. (3) I first wrote the pro forma coverage as "$310-350M, about twice"; recomputed from the
filed lines it is $360-430M, about two and a half times; corrected. (4) I first wrote that CommScope lost money in "four
of the six years shown"; the row shows five years and the series has operating losses in five of ten; corrected.

**Tooling defects, reported, not patched:**
1. **`Screens/floor_screen.py` line 711 labels a five-year GROSS total "NET CASH INFLOW" whenever any single year of the
   acquisition tag is negative.** For Belden a $7.7M purchase-price refund in 2025 turned $573M of net acquisitions paid
   over 2021-2025 into *"NET CASH INFLOW on the acquisition line ($589M, 14% of cap)"*. The note should report the signed
   net and name the negative year, or fire only when the window's net is an inflow.
2. **The screen's `wc_note` reads one working-capital line in isolation.** It flagged payables at 50% of 2021 OCF without
   the offsetting receivable and inventory build; the whole working-capital change that year was a $54.9M use of cash.
   A note that prints the net of all working-capital lines beside the one line would answer itself.
3. **The screen and `tools/run.py` subtract only the `ShareBasedCompensation` line.** Belden also pays its retirement-plan
   match partly in its own shares ($2.7-9.0M a year 2020-2025, in the equity statement, not the cash-flow statement), a
   non-cash expense left inside operating cash. Any filer that funds a 401(k) match in stock carries the same omission.
4. **The screen's owner earnings use cash-flow D&A (which includes amortization of acquired intangibles) as one (c) end.**
   For an acquisitive filer that end is not a maintenance estimate; the depreciation proxy here removes it.
5. **The screen cannot see a perimeter change that happened after the last annual filing.** Every tagged figure for BDC
   predates the RUCKUS purchase of 2026-07-01, which added $1.85bn of debt and a business that lost money in 2024; the
   deal_note flagged the 8-K, which is what the flag is for, but no screened number reflects it.

## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- One line: **Belden makes specified cable, connectivity and industrial networking gear sold mostly through distributors,
  and on 2026-07-01 bought RUCKUS enterprise Wi-Fi for about $1.9bn of secured debt. The registrant calls its markets
  *"highly competitive with many players"* with a 5-15% share and products *"less differentiated"*; twelve years of its own
  revenue bridges name copper pass-through as the only regular price factor; the GAAP operating margin was 11.2% in 2017
  and 11.6% in 2025 while Amphenol earned 19-25% in the same field; returns on capital including goodwill were 11-14%
  pretax in most years and about 11% pro forma before any amortization, RUCKUS earning 5.2% on its price in its best year
  and its technology amortized over five years as the period of *"competitive advantage"*. [E3-03] criterion (2) fails on
  the filing and the demonstration clause fails on the bridges: [E2-37]'s remarkable textile company, with the
  adjusted-EPS headline three times GAAP.**
- **PASS/FAIL: FAIL at Q2 (OUT, ON THE BUSINESS).** Price **$112.45** (NYSE close 2026-09-25, aggregator, flagged) ×
  **39,078,191 shares** (10-Q cover for 2026-06-28, accession `0000913142-26-000034`) = cap **$4,394.3M**; sovereign
  **5.49%** (US Treasury 30-year par, 09/25/2026). Owner earnings to common before RUCKUS: five-year FY2021-2025
  **$167.3-222.5M (3.81-5.06%)**, three-year $180.5-240.5M (4.11-5.47%), ten-year $147.2-189.0M; after RUCKUS, a
  disclosed guess of about $120-220M (2.7-5.0%).
- **If UNRESEARCHED — THE WORK ORDER:** n/a.
- **If UNKNOWABLE:** n/a.

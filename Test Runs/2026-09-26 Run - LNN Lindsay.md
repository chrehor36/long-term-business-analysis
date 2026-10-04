# Company Run — Lindsay Corporation (LNN) — 2026-09-26
**WAVE 7 name 46 of 218. Claimed at dispatch 2026-09-26 by an unattended run agent (claim commit `94e59fcf`). RESULT: Q1 IN, Q2 OUT (on the business); the file closed at Q2.**

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
- rate **5.49%** · date **09/25/2026** (the newest row on the curve when struck, early on 2026-09-26) · source (issuing authority) **US Treasury daily par yield curve, 30 Yr**, struck fresh for this run by `strike.py` in the research folder; raw CSV saved as `Test Runs/_research 2026-09-26 LNN/treasury_2026.csv`. Prior rows 5.47% (09/24) and 5.40% (09/23). **Struck, not inherited. FRED not used.**
- FX: Lindsay reports in US dollars and is quoted in US dollars on the NYSE. The 10-K states *"Approximately 34 and 36 percent of total consolidated Company revenues were conducted in currencies other than the U.S. dollar in fiscal 2025 and 2024"* (euro, Brazilian real, South African rand, Turkish lira, Chinese renminbi named in Item 7A). The earnings currency is predominantly the dollar; the USD sovereign is used and the currency mix is stated rather than hidden. No ADR.

**Registrant.** CIK 0000836157, LINDSAY CORP, a Delaware corporation, Omaha, Nebraska; **fiscal year to August 31** (`submissions.json`: fiscalYearEnd 0831).

**Price, shares, cap.**
- Price **$114.25**, NYSE close **2026-09-25**, Yahoo chart endpoint (aggregator, live quote only, **flagged**); raw response saved as `price_raw.json`. Prior closes 112.76 (09/24), 115.84 (09/23), 114.91 (09/22), 115.00 (09/21).
- Shares **10,168,885** common, from the **cover of the 10-Q for the quarter to 2026-05-31, filed 2026-07-02, accession `0001193125-26-294516`**: *"As of June 30, 2026, 10,168,885 shares of the registrant’s common stock were outstanding."* Read by hand in the filing text and returned identically by `python Screens/cover_shares.py LNN` (*"(single class / undimensioned) 10,168,885"*). **One class**: the 10-Q balance sheet reads *"Preferred stock of $ 1 par value - authorized 2,000 shares; no shares issued and outstanding"*, and the 10-K cover calls the common *"all of which is voting"*. The count is struck at 2026-06-30; repurchases after that date are not in it (the 10-Q reports 667 thousand shares bought in the nine months to 2026-05-31 for $80.7M, under a new $150.0M authority of November 2025).
- **Market cap $1,161.8M** (114.25 x 10,168,885). The screen row's $1,158M is within 0.3%.

**The screen's fields, opened here (each a prompt to read, never a finding).**
- **`cap_flag` "CAP BELOW FILED PUBLIC FLOAT ... One of the two is wrong": neither is wrong; the two figures are two dates.** The 10-K FY2025 cover: *"The aggregate market value of Common Stock of the registrant, all of which is voting, held by non‑affiliates based on the closing sales price on the New York Stock Exchange, Inc. on February 28, 2025 was $ 1,435,554,352 ."* The close on 2025-02-28 was **$132.12** (Yahoo history, `px_hist.json`), so the float figure implies about 10.87 million non-affiliate shares, consistent with the 10,804,220 shares outstanding on the same cover at 2025-10-21. The screen's cap was struck at a later, lower price on a later, smaller count (10,168,885 after the FY2026 buybacks). **A float struck nineteen months ago at $132 exceeds a cap struck today at $114; nothing is mis-filed.** Same finding as the PPG run's cap flag.
- **`deal_note` empty, confirmed by reading the filing index**, not inherited. Every 8-K since 2024-06-01 was listed from the EDGAR submissions file: Items 2.02 (quarterly releases), 5.02 (officer changes: 2025-07-23, 2025-09-15, 2025-10-14, 2025-10-22, 2025-11-03, 2026-07-16, 2026-08-28), 5.07 (annual meetings), 7.01, and **one Item 1.01 with 2.03, on 2025-08-27 (`0000836157-25-000003`): the Fourth Amendment to the $50 million Wells Fargo revolving credit agreement**, read in full: it *"extends the termination date of the unsecured revolving credit facility from August 26, 2026 to August 26, 2030"*. **No Item 2.01 since 2015, no merger agreement, no tender offer, no DEFM14A or 425, and no Item 4.02 non-reliance notice anywhere in the filing index back to 2004.** The quote is not a spread. *(Recorded, not scored here: an NT 10-K was filed on 2019-10-31, the same day as the FY2019 10-K; a 10-K/A in 2009 and a 10-Q/A in 2012. Q3 material if Q3 opens.)*
- **`wc_note` "RATIO MEANINGLESS - NEAR-ZERO OCF ... Read the 2022 cash-flow statement": read.** FY2022 (10-K `0000950170-22-019799`): *"Net cash provided by operating activities 3,048"* on net earnings of $65,469K, because *"Receivables ( 47,514 )"* and *"Inventories ( 53,803 )"* absorbed the year, partly offset by *"Accounts payable 13,832"*. The build reversed in FY2023 (*"Inventories ... 40,954"* of release, operating cash $119,707K). The screen's warning holds: the 454% is meaningless; the dollars are a working-capital swing across a price-inflation and project-shipment year, carried to Q4 if Q4 opens.
- The level and best-year flags (*"STEP UP - normalize down [E4-41]"*, *"TWO YEARS JOINTLY CARRY THE WINDOW"*, *"EARLY HALF STRADDLES ZERO"*, *"FLAGS DISAGREE"*) and the spread caveat are carried to Q4, where they would be rebuilt from the filed statements.
- **Newer than the screen row.** The row's `newest_filing` is 2025-08-31 (the FY2025 10-K) and `newest_periodic` 2026-05-31. **No FY2026 10-K exists on EDGAR at the strike**: the fiscal year ended 2026-08-31, and the FY2025 10-K was filed on 2025-10-23, so the FY2026 annual report is not yet due. The latest periodic is the 10-Q for 2026-05-31 (read here). 8-Ks since it: 2026-07-02 (Item 2.02, the Q3 release), 2026-07-17 and 2026-08-28 (Item 5.02). Nothing later.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes (Item 1 competition and markets; Item 1A; Note 15 commitments and contingencies and Note 18 segments, as cited at Q2)
- **10-K for FY2025 (year to 2025-08-31), filed 2025-10-23, accession `0001193125-25-248751`** (Items 1, 1A, 7, 7A, 8); **10-Q for the quarter to 2026-05-31, filed 2026-07-02, accession `0001193125-26-294516`**; 8-K of 2025-08-27 (`0000836157-25-000003`, credit agreement). Earlier 10-Ks FY2010 to FY2024 for the series, named where used.
- **Figure cross-checked against the filed statement:** FY2025 *"Net cash provided by operating activities 132,910"* (and 95,761 for 2024, 119,707 for 2023) in the filed Consolidated Statements of Cash Flows, equal to the tag `NetCashProvidedByUsedInOperatingActivities` ($132.9M, $95.8M, $119.7M). *"Share-based compensation expense 8,059"* and *"Purchases of property, plant and equipment ( 42,496 )"* in the same statement equal the tags.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words, no management language.** Lindsay bends and galvanises steel tube, bolts it onto wheeled towers with gearboxes, motors and a control panel, and sells the finished irrigation machine (a centre pivot of about seven spans, a quarter-mile long, watering about 125-130 acres of a 160-acre quarter section) to about 200 independent US dealers and to dealers and project buyers abroad; the dealer designs the field layout, adds the well, pump, pipe and power, and erects the machine. The farmer pays for it if the extra yield and the saved water, labour and energy beat the cost, which the 10-K says turns on crop prices, net farm income, credit and the weather. A remote-control and monitoring subscription (FieldNET and FieldWise) and replacement parts ride on the installed base. Costs are steel and zinc (price-volatile), components, labour in Nebraska, Kansas, Brazil, France, Türkiye, China and South Africa, and freight. **Irrigation was $568.0M of the FY2025 $676.4M revenue (84%)**, split North America $273.8M and international $294.2M (of which a single MENA project customer was 13% of consolidated revenue). **Infrastructure ($108.4M, 16%)** sells the Road Zipper (a concrete-and-steel barrier and the machine that moves it across a lane, sold or leased for congestion relief and work zones), crash cushions and end terminals, road tape and rail signals, mostly to state transportation departments and contractors paid from federal highway money. FY2025: operating income $88.1M (13.0%), operating cash $132.9M, capital spending $42.5M, cash $250.6M against $115.0M of 3.82% senior notes due 2030.
- **The scarce input this business controls.** In irrigation, **a dealer network and a brand (Zimmatic) in a market four manufacturers share**, and an installed base that buys parts and a subscription; the product itself is fabricated steel from purchased coil. In infrastructure, **the Road Zipper patents, the barrier-transfer machine and a lease fleet**, and product qualification to the federal crash-test standard (MASH) that governs eligibility for federal reimbursement. Whether any of this is scarce enough to be a franchise is Q2's question; Q1 records that the scarce inputs are distribution, qualification and a niche machine, not a resource or a licence.
- **Will the fundamentals look broadly the same in ten years?** **Yes, on the filings.** The centre pivot has been Lindsay's product since 1955; the 10-K's three sources of demand (conversion from flood irrigation, replacement of old pivots, and dry-land conversion) and its drivers (crop prices, farm income, water) are the same in the FY2010 and FY2025 10-Ks, as is the risk-factor sentence on price competition (Q2). Revenue has moved between $358M (FY2010) and $771M (FY2022) with the farm cycle, and operating margin between 1.4% (FY2019) and 15.5% (FY2013), but what is sold and how it is paid for has not changed. The infrastructure half depends on federal highway authorisations (the IIJA programmes *"are scheduled to run through September 2026"*), which is an exposure, not a change of character.
- **Relatively simple and stable in character [E3-31]?** Simple: a steel machine sold through dealers into a farm-income cycle, and a road-safety product sold into a public-works budget. Stable in character, unstable in the level of earnings; the instability is a question of how reliable the earnings are (Q2, Q4), not of whether the business can be understood. **Not [E4-46]'s months-of-study case.**
- **VERDICT: [x] IN**: the money is made visibly, by selling and servicing steel irrigation machines through dealers to farmers whose purchases follow farm income, and road-safety equipment to highway agencies. **IN is not a finding on the franchise.**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

*Every Lindsay figure below is read from the filed 10-Ks for FY2010 to FY2025 (MD&A segment tables, selected-data tables, Item 1, Item 1A, balance sheets and cash-flow statements; extractions `seg.py`, `roc_out.txt`, `na_rev.txt`, `price_lang.txt` in the research folder). Accessions: FY2010 `0000950123-10-103822`, FY2011 `0000950123-11-092356`, FY2012 `0001193125-12-437101`, FY2013 `0001193125-13-403973`, FY2014 `0001193125-14-372388`, FY2015 `0001193125-15-348274`, FY2016 `0001193125-16-740910`, FY2017 `0000836157-17-000035`, FY2018 `0001564590-18-024810`, FY2019 `0000950123-19-009834`, FY2020 `0001564590-20-047271`, FY2021 `0001564590-21-051450`, FY2022 `0000950170-22-019799`, FY2023 `0000950170-23-054198`, FY2024 `0000950170-24-117056`, FY2025 `0001193125-25-248751`. Fiscal years end August 31.*

**[E3-03], criterion by criterion.** *"An economic franchise arises from a product or service that: (1) is needed or desired; (2) is thought by its customers to have no close substitute and; (3) is not subject to price regulation. The existence of all three conditions will be demonstrated by a company's ability to regularly price its product or service aggressively and thereby to earn high rates of return on capital."* The same 1991 passage: *"In contrast, “a business” earns exceptional profits only if it is the low-cost operator or if supply of its product or service is tight. Tightness in supply usually does not last long"* **[E3-43]**.

- **(1) Needed or desired [x]: passes.** Irrigation raises and steadies yields and saves water and labour; highway agencies buy barriers and crash cushions to separate traffic and meet a federal crash-test standard.
- **(3) Not subject to price regulation [x]: passes.** No filing read places Lindsay's prices under a rate regulator. Infrastructure products must meet MASH to be *"eligible for federal reimbursement"* (Item 1A), which governs what may be bought, not what it may cost; the buyers are public agencies spending federal and state highway money, and projects are won one at a time (*"Due to the project nature of the roadway construction and congestion management markets, the Company’s customer base changes from year to year"*, Item 1).
- **(2) No close substitute [ ]: FAILS for irrigation, 84% of revenue, in the registrant's own words and in the market leader's.**
  - Lindsay, Item 1 (FY2025): *"Four manufacturers control a substantial majority of the U.S. center pivot irrigation system market."* *"Competition also occurs in areas of price and seasonal programs, product quality, durability, controls, product characteristics, retention and reputation of local dealers, customer service, and, at certain times of the year, the availability of systems and their delivery time."* Internationally, *"The international irrigation market includes participation and competition by the leading U.S. manufacturers, as well as various regional manufacturers."*
  - Lindsay, Item 1A, **the same sentence in every 10-K from FY2010 to FY2025**: *"Due to price competition in the market for irrigation equipment and certain infrastructure products, the Company may not be able to recoup increases in these costs through price increases for its products, which would result in reduced profitability."* (FY2010-FY2014 read *"Because there is a level of price competition"*.) The registrant tells its owners, for sixteen years running, that it cannot count on passing its own cost increases to its customers.
  - **Valmont, the largest of the four, in its own 10-K** (FY2025, `0000102729-26-000007`): *"Competitors differentiate themselves based on product durability, reliability, pricing and value proposition, quality, and the service capabilities of local dealers."* *"Pricing in the industry can become highly competitive, particularly during periods of low demand."* *"In international markets [...] pricing often plays a more critical role."* The FY2014 10-K (`0001047469-15-001179`) said the same: *"We believe we are the leader of the four main participants in the mechanized irrigation business. Participants compete for sales on the basis of price [...] Pricing can become very competitive, especially in periods when market demand is low."* The customer's substitute is a Valmont, Reinke or T-L pivot from the dealer down the road, and the flood, drip and hose-reel alternatives the 10-K lists beside them.
  - **Infrastructure (16%) is mixed and is recorded under the evidence against below**: crash cushions *"compete with other vendors in the world market"*; the Road Zipper has *"limited competition"*.

**The demonstration clause, read on sixteen years of the filer's own figures.** The clause has two halves: the ability *"to regularly price its product or service aggressively"*, and *"thereby"* high returns on capital. They are read separately, because they come apart here.

*Half one: pricing.* What the MD&A says moved North American irrigation prices, year by year (`na_rev.txt`):

| fiscal year | MD&A on price | what moved the year |
|---|---|---|
| 2014 | (units named, no price) | *"a decline in the number of irrigation systems sold"*, *"Lower agricultural commodity prices"*; storms added about $27.0M |
| 2015 | (units named, no price) | *"Sustained low agricultural commodity prices, lower net farm income"* |
| 2016 | *"reduced market pricing from passing through lower steel costs"* | unit volume down |
| 2017 | *"higher average selling prices from passing through higher raw material costs"* | unit volume down |
| 2018 | *"higher average selling prices"* | unit volume up |
| 2019 | *"higher average selling prices"* | unit volume down, divestitures |
| 2020 | *"Irrigation system unit volume and average selling prices in fiscal 2020 were comparable"* | flat |
| 2021 | *"higher average selling prices"* | units up |
| 2022 | *"higher average selling prices"* | small unit increase, storm replacement |
| 2023 | *"Higher average selling prices compared to the prior year resulted from the pass through of higher raw material and other costs to customers"* | unit volume down |
| 2024 | *"slightly lower average selling prices"* | units up, shorter machines |
| 2025 | *"slightly lower average selling prices"* | unit volume down, *"softer market conditions"* |
| 9M FY2026 | *"slightly higher average selling prices"* | unit volume down; *"Persistent weakness in commodity markets and tempered farmer sentiment"* |

**Price follows steel, in the registrant's own explanation, in both directions** (down in 2016, up in 2017 and 2023, each called a pass-through), and slips when the farm market is soft (2024, 2025). That is the opposite of [E2-44]'s first characteristic, *"an ability to increase prices rather easily (even when product demand is flat and capacity is not fully utilized) without fear of significant loss of either market share or unit volume"*, and it is what the Item 1A sentence says it is. **The dollar record, in nominal terms**: consolidated revenue $690.8M in FY2013 and $676.4M in FY2025; irrigation segment revenue $626.0M in FY2013 and $568.0M in FY2025, across a period that includes the 2021-2023 steel pass-through. **No unit series is filed** ([E4-55]'s physical series cannot be built); the MD&A names unit volume down in FY2014, 2015, 2016, 2017, 2019, 2023, 2025 and 9M FY2026, and up in FY2018, 2021, 2022 and 2024.

*Half two: returns on capital.* The filer's own figures, three ways:

| fiscal year | company operating margin | irrigation segment margin (before corporate G&A) | infrastructure segment margin | pretax operating income / (debt + equity − cash and marketable securities) | the same, less goodwill and intangibles | the filer's own *"Return on invested capital"* (after tax, cash in the base) |
|---|---|---|---|---|---|---|
| 2010 | 10.6% | 15.8% | 11.1% | | | |
| 2011 | 11.8% | 16.1% | 10.9% | 32.1% | 48.5% | |
| 2012 | 11.9% | 16.9% | | 38.1% | 56.2% | |
| 2013 | 15.5% | 20.0% | | 46.8% | 69.0% | |
| 2014 | 12.7% | 17.0% | 4.5% | 37.2% | 55.3% | 13.5% |
| 2015 | 9.0% | 11.3% | 18.4% | 19.0% | 36.7% | 7.2% |
| 2016 | 6.7% | 11.7% | 19.6% | 12.9% | 24.0% | 6.1% |
| 2017 | 7.8% | 10.2% | 20.1% | 15.3% | 27.9% | 6.9% |
| 2018 | 7.1% | 9.5% | 22.1% | 16.7% | 27.7% | 5.9% |
| 2019 | 1.4% | 8.5% | 17.9% | 2.4% | 3.6% | 1.6% |
| 2020 | 11.4% | 11.7% | 33.4% | 19.8% | 29.7% | 10.7% |
| 2021 | 9.5% | 13.4% | 21.0% | 17.6% | 24.7% | |
| 2022 | 12.3% | 15.9% | 17.5% | 24.1% | 30.8% | |
| 2023 | 15.2% | 20.8% | 13.7% | 25.2% | 34.7% | |
| 2024 | 12.6% | 17.0% | 20.4% | 18.9% | 25.9% | |
| 2025 | 13.0% | 17.1% | 24.3% | 22.2% | 30.4% | |
| 9M FY2026 | 10.8% | 15.4% (18.1% a year earlier) | 16.6% (27.2%) | | | |

*(Segment margins are as first reported in each year's 10-K; the FY2016 10-K restated FY2015 irrigation to $52.1M from $50.8M after a resegmentation, and the FY2012-FY2014 infrastructure lines did not parse and are left blank rather than guessed. The filer's ROIC is from the FY2018 and FY2020 selected-data tables, which stopped after FY2020. FY2019 carries $15.1M of "Foundation for Growth" charges and divestiture losses. 9M FY2026 from the 10-Q: operating income $51,132K on revenue $474,297K; irrigation segment operating income $62,768K on $407,707K; infrastructure $11,061K on $66,590K.)*

**The returns are good and they are the industry's, not Lindsay's.** On the capital actually tied up in the business (net of the cash the filer holds), pretax returns ran 12.9-46.8% in every year but FY2019, and 24-69% on tangible capital: a pivot is fabricated from purchased steel in modest plants (net property $56-142M against $444-771M of revenue, FY2011-FY2025), so the capital a dollar of sales needs is small. But **the filer's own measure, after tax and with its cash in the base, was 5.9-7.2% in FY2015-FY2018 and 1.6% in FY2019**, which is the number its owners actually earned on what they had left in the company; and the level of returns in any year is set by the farm cycle the filer names every year (commodity prices, net farm income, storms, a Brazil credit cycle, a MENA project), not by a price the company set. **[E3-43]'s "a business" earns exceptional profits only as the low-cost operator or when supply is tight**; the competitor row below tests the first, and the MD&A's own year-by-year explanation rules out the second as a lasting cause. **[E3-46]**'s second question (*"Has it earned high returns on capital?"*) is answered yes on the operating capital and no on the owner's capital in the lean years; it is asked about the business, and it does not by itself supply the pricing half of [E3-03]'s demonstration.

**[E4-04] and [E4-23]:** the product is a maintained design (the pivot since 1955), not rebuilt from zero; no superstar dependence. Neither is relied on.

**Direction [E4-32]:** irrigation revenue in FY2025 below FY2013 in nominal dollars; infrastructure revenue between $78M and $131M with no trend (lumpy Road Zipper projects: a $27M UK project in FY2020, a $20M project in FY2025, *"a $20 million project that did not repeat"* in FY2026); the 10-K's Road Zipper sentence **lost its clause *"as there is not another moveable barrier product today comparable to the Road Zipper System"* in the FY2024 10-K** after carrying it from at least FY2010 to FY2023 (read in the FY2010, FY2015, FY2020, FY2021, FY2022, FY2023, FY2024 and FY2025 10-Ks). The filer does not say why; recorded as a prompt, not a finding.

**THE COMPETITOR ROW — required [E3-28].** Same metric for both filers: **irrigation segment operating income / irrigation segment revenue, before corporate expense**, each from its own filed 10-K segment note or MD&A table.

| year | Lindsay irrigation (fiscal year to Aug 31) | Valmont Irrigation, from FY2021 Agriculture (fiscal year to late Dec) | source, and the figure checked |
|---|---|---|---|
| 2010 | 15.8% | 14.0% | Valmont FY2012 10-K `0001047469-13-001680`: *"Irrigation segment 750,592 665,896 443,359"* (sales, 2012-2010) and *"Irrigation 143,605 107,759 61,973"* (operating income) |
| 2011 | 16.1% | 16.2% | same |
| 2012 | 16.9% | 19.1% | same |
| 2013 | **20.0%** | **20.6%** | Valmont FY2014 10-K `0001047469-15-001179`: *"Irrigation segment 759,159 882,174 750,592"*; *"Irrigation 128,145 181,498 143,605"* |
| 2014 | 17.0% | 16.9% | same |
| 2015 | 11.3% | 12.9% | Valmont FY2017 10-K `0000102729-18-000008`: *"Irrigation segment 644,372 567,973 605,771"*; *"Irrigation 101,498 90,945 78,218"* |
| 2016 | 11.7% | 16.0% | same |
| 2017 | 10.2% | 15.8% | same |
| 2018 | 9.5% | 15.6% | Valmont FY2020 10-K `0000102729-21-000012`: *"Irrigation segment 640,092 578,652 624,761"*; *"Irrigation 83,046 71,687 97,722"* |
| 2019 | **8.5%** | **12.4%** | same |
| 2020 | 11.7% | 13.0% | same |
| 2021 | 13.4% | 13.5% (Agriculture) | Valmont FY2023 10-K `0000102729-24-000013`: *"Agriculture 1,174,961 1,335,285 1,017,050"*; *"Agriculture 16,850 179,263 137,027"* |
| 2022 | 15.9% | 13.4% | same |
| 2023 | 20.8% | 1.4% (13.1% before *"impairment of certain goodwill and other intangible assets [...] totaling approximately $137.2 million"*) | same |
| 2024 | 17.0% | 12.8% | Valmont FY2025 10-K `0000102729-26-000007`: *"Total sales $ 1,020,750 $ 1,083,708"*, *"Operating income $ 92,076 $ 138,336"* |
| 2025 | 17.1% | 9.0% (includes *"$24.2 million of legal contingency reserves and $23.8 million of expected credit losses in Brazil"*) | same |

- **Peers named: 1 filer of the 3 other main US pivot makers**, plus the drip and regional makers abroad. **Not obtainable from SEC filings:** Reinke Manufacturing and T-L Irrigation (private, Nebraska; file nothing); Netafim (owned by Orbia, Mexico) and Rivulis (private) in drip; the regional makers in Brazil, Europe and Türkiye. In infrastructure: Valtir (the former Trinity Highway Products, private since 2021) and Hill & Smith (London-listed, no SEC filings) for crash cushions and barriers; no Road Zipper competitor is named by the filer. **The verdict does not rest on the row**: it rests on criterion (2) in the registrant's and the market leader's own words and on the registrant's sixteen-year pricing record.
- **What the row shows [E3-61]:** two of the four makers, reported on the same basis, **moving together with the farm cycle** (both peak in 2013 at about 20%, both trough in 2019 at 8.5-12.4%, both recover in 2020-2022). **Lindsay is not the low-cost operator on this record**: it earned less than Valmont in every year from 2015 to 2020, by 1.3 to 6.1 points, and more from 2022 to 2025, the years of its MENA project, Brazil and Valmont's own charges. A position that swaps places with the rival across the cycle is not [E2-58]'s *"cost advantage that is both wide and sustainable"*. The row shows position; it cannot show conduct, and here the conduct is described by both filers the same way: price competition that sharpens when demand is low.
- **Untapped pricing power [E3-33], [E5-28]:** not claimed. Four makers share the US market and Valmont calls itself the leader; neither is a near-monopoly, and a filer that warns for sixteen years that it may not recoup cost increases is not leaving price on the table.
- **[E2-53], the dominance test:** fails. No maker is dominant; the leader's margins in the lean years (12.4-16.0% in 2015-2019) are ordinary for the class, and Lindsay's own were lower.
- **[E2-45], the attacker's test:** a well-funded attacker faces a dealer network and a brand, not a barrier: two private Nebraska makers hold places among the four, and abroad *"various regional manufacturers"* compete where *"pricing often plays a more critical role"*.
- **[E4-37], the agony metric:** the registrant's own risk factor is the agony: price increases are *"passed through"* when steel rises and reversed when it falls.
- **Class: [x] NONE at the company level** (the Road Zipper is a narrow product position inside a 16% segment, below) · **Direction: flat to down in nominal irrigation dollars since FY2013; no unit series filed.**

**THE STRONGEST EVIDENCE AGAINST THIS VERDICT, hunted hardest [E4-26, E3-41, E4-51].**
1. **The returns on operating capital are high through the cycle.** Pretax 12.9-46.8% on capital net of cash in every year FY2011-FY2025 but FY2019, 24-69% on tangible capital, and 22.2% and 30.4% in FY2025. [E3-03]'s own words say a franchise is *"demonstrated by [...] high rates of return on capital"*, and [E3-46] asks exactly this question second.
2. **A consolidated four-maker oligopoly has behaved rationally.** Four makers remain (the FY2010 10-K: *"the center pivot irrigation system industry has seen significant consolidation of manufacturers over the years"*); prices were raised through the 2021-2023 inflation and irrigation margins rose from 13.4% to 20.8%; FY2026 shows *"slightly higher average selling prices"* in a weak market.
3. **The Road Zipper.** *"limited competition in its moveable barrier line"* for sixteen years, *"there is not another moveable barrier product today comparable"* until FY2023; infrastructure margins of 17.5-33.4% in FY2015-FY2025 apart from FY2023, above irrigation's.
4. **The installed base.** FieldNET and FieldWise subscriptions and replacement parts on a machine that lasts decades.
5. **Lindsay out-earned Valmont's irrigation business in FY2022-FY2025.**

**Answered.** (1) The high returns are a property of the product's low capital intensity, shared by the rival that reports on the same basis, and they move with the farm cycle in both filers; the pricing half of the demonstration clause, which the returns are supposed to come *"thereby"* from, is contradicted in the registrant's own MD&A (price follows steel both ways and slips in soft years) and its own Item 1A. What the owner actually earned after tax on the capital left in the company was 5.9-7.2% in FY2015-FY2018 on the filer's own measure. [E3-43] names this shape: good returns in an industry where supply is sometimes tight and the leader says pricing *"can become highly competitive, particularly during periods of low demand"*. (2) The inflation years are cost recovery, in the registrant's words (*"the pass through of higher raw material and other costs to customers"*); the FY2026 increase is *"slight"* and came with lower volume. Rational conduct among four makers is [E3-61]'s people residual, which the corpus says cannot be predicted from structure, and both filers describe it breaking down when demand falls. (3) The Road Zipper is a genuine narrow position, but it sits inside a segment that is 16% of revenue, its revenue comes in lumpy public projects (a single $20M project that did not repeat left FY2026's nine-month infrastructure revenue 21% lower), the product *"does compete with traditional “safety-shaped” concrete barriers"*, the buyers are public agencies spending authorised highway money, and the filer stopped saying in FY2024 that nothing comparable exists. The unit of the test is the company **[E4-08]**, and 84% of this company is irrigation. (4) The subscription and parts ride on machines that are sold in a price-competitive market; the remote technology is sold for any brand (*"works on any brand of electronic pivot and drip irrigation systems"*, Item 1), which is the opposite of lock-in. (5) Lindsay trailed Valmont in every year from 2015 to 2020 and led from 2022, the years of a single customer at 13% of revenue and of Valmont's impairment, legal and Brazil credit charges; a lead that alternates is not a low-cost position [E2-58].

- **VERDICT: [x] OUT**: on the business. **[E3-03] criterion (2) fails for irrigation, 84% of revenue, in the registrant's own words** (four manufacturers share the US market, competition *"in areas of price and seasonal programs"*, and for sixteen consecutive 10-Ks *"Due to price competition [...] the Company may not be able to recoup increases in these costs through price increases"*) **and in the market leader's** (*"Pricing in the industry can become highly competitive, particularly during periods of low demand"*). **The pricing half of the demonstration clause fails on the registrant's own year-by-year MD&A**: price passed through with steel down (FY2016) and up (FY2017, FY2023), and slipping in the soft years FY2024 and FY2025; [E2-44]'s first characteristic is not shown. The returns on operating capital are good, move with the farm cycle in step with Valmont's, and alternate in rank with Valmont's, which is [E3-43]'s *"a business"* and not the low-cost exception [E2-58]. The Road Zipper's narrow position does not carry a company that is 84% irrigation [E4-08]. **The file closes here.** Q3 to Q6 are not opened as gates; the material gathered beneath the close follows without verdicts.

## MATERIAL BENEATH THE CLOSE: recorded, not governing

*The file closed at Q2 OUT. What follows was gathered while the business questions were being read, and it is recorded so the next reader does not have to fetch it again. **None of it is a verdict, none of it can reopen Q2 [E2-37, E3-39], and the valuation arithmetic is headed as the protocol requires.***

### Q3 prompts (no verdict)

**Weight case, as it would be declared:** leverage low ($115.1M of 3.82% senior notes due 2030 against equity of $532.9M and cash of $154.8M at 2026-05-31; a $50M revolver undrawn); no control purchase; daily execution moderate (steel buying, dealer programmes, project bids abroad). Not declared as a gate, because the gate is not opened.

- **[E4-29] does not fire, in the 10-K, the release or the proxy.** The Q3 FY2026 release (8-K 2026-07-02, `0001193125-26-293405`, EX-99.1) reports revenue, operating income, operating margin, net earnings and EPS, and the words *EBITDA*, *adjusted* and *non-GAAP* do not appear in it. The FY2025 10-K uses EBITDA only for a covenant (*"a funded debt to EBITDA leverage ratio"*). **Pay** (DEF 14A 2025-11-21, `0001193125-25-290521`): the annual cash incentive is paid on *"Revenue (37.5%) Operating Margin (37.5%) Free cash flow (25%)"* (FY2025 actuals $676.4M and 12.8% against targets of $669.5M and 12.1%, paid 140% of target on the financial part); performance shares, half the long-term award, on relative TSR and ROIC equally, where *"Invested Capital means Total Interest-Bearing Debt plus Shareholders’ Equity"*; the FY2023-FY2025 grant paid 48% (*"relative total stockholder return at the 19 th percentile (resulting in a 0% of target payout for this component) and three-year average return on invested capital of 12%"*). **[E4-27], what pay vests on:** revenue carries 37.5% of the financial part of the cash incentive, which rewards the MENA-type project volume the MD&A says was *"dilutive to gross margin"*; recorded as a prompt.
- **[E4-22]'s third flag:** no numeric earnings guidance in the release; the outlook paragraph is qualitative (*"irrigation market conditions remain soft as growers await further trade certainty"*). The 10-K gives a capital-spending range only.
- **Officer turnover, dated to when it became public.** CFO Brian Ketcham announced retirement on 2025-07-23 (effective 2025-12-31); his successor Sam Hinrichsen gave notice on 2026-07-17 to leave on 2026-08-31, *"for personal reasons and there were no disagreements"* (8-K `0001193125-26-307817`); two vice presidents became interim co-CFOs from 2026-09-01 (8-K `0001193125-26-374348`). Eight 8-Ks carrying Item 5.02 since July 2025. A prompt for the next reader, not a finding.
- **The one late filing is explained on its face.** The NT 10-K of 2019-10-31 (`0001193125-19-279368`): *"Due to unforeseen technical problems arising at the Printer, the Printer was unable to carry out Lindsay’s instructions"*; the 10-K *"was accepted at 5:50 P.M. EDT on October 30, 2019"*, twenty minutes late. No Item 4.02 in the index back to 2004. The 2009 10-K/A and 2012 10-Q/A were not opened.
- **Candor [E2-26].** Segment tables with gross profit, operating expenses and operating income for both segments in every 10-K; the MD&A names price and volume separately each year, which is how this file could see that price follows steel. **Against:** no unit series is published, and the Road Zipper sentence dropped *"as there is not another moveable barrier product today comparable"* in FY2024 without comment.
- **Capital allocation, [E5-08] with the humility clause [E4-13].** Repurchases (10-K and 10-Q text): 497,899 shares for $41.1M (FY2014, about $82), 1,198,089 for $96.9M (FY2015, about $81; funded in the same year by the $115.0M senior notes, *"used [...] for general corporate purposes, including acquisitions and dividends"*), 688,790 for $48.3M (FY2016, about $70), 194 thousand for $22.5M (FY2024, about $116), 86 thousand for $11.5M (FY2025, about $134), and **667 thousand for $80.7M in the nine months to 2026-05-31 (about $121)**, under a new $150.0M authority. Against the computation below, the FY2026 purchases at about $121 sit above every floor value ($29-90 a share) and inside the sovereign range ($52-163); management knows the business better than this file does [E4-13]. Condition 1 holds (cash $154.8M after the purchases, debt fixed to 2030). Dividends $15.7M in FY2025 ($1.45 a share, against $0.325 in FY2010). Acquisitions about $145M over FY2010-FY2025 (LAKOS 2013 $29.0M, Elecsys and SPF 2015 $69.5M, $30.8M in FY2023, small ones in 2010, 2011 and 2020, and a $5.8M equity-method stake in Pessl Instruments in FY2025); the Foundation for Growth programme of FY2018-FY2019 cost $15.1M in FY2019 and divested businesses.
- **Honesty.** No finding of personal misconduct in any document read. Matters on the public record in the filings read: the X-Lite end-terminal product-liability suits and a relator's state false-claims suits after the federal False Claims Act case was dismissed in 2023 (the US found the allegations *"lack[ed] merit"*, Item 1A); environmental remediation at the Lindsay, Nebraska plant (Note 15).

### Q4 prompts: owner earnings the corpus's way [E2-23], every window [E4-25]

**Construction.** Operating cash flow as filed (the latest 10-K showing each year: FY2012 for 2010-2011, then each year from the 10-K two years later, FY2025 for 2023-2025), less share-based compensation, less (c). **No net-income proxy anywhere** (operator rule 5). **No discontinued operations** (the continuing-operations tag equals total operating cash in every year it exists). **SBC resolves every year and is complete**: the cash-flow line equals the equity statement (*"Share-based compensation expense 6,529"* in both for FY2023); the few restricted units settled in cash (5,793 units at 2025-08-31) are paid through operating cash already; no 401(k) match paid in stock is described; SBC is 8.6% of operating cash over sixteen years, so [E3-70]'s grant-value measure would not move the range. **No non-controlling interest** (the word does not appear in the FY2025 10-K). The Pessl equity stake is $5.8M; the [E3-04] look-through is immaterial and not added. **The D&A end takes out acquired-intangible amortisation** (tag `AmortizationOfIntangibleAssets`, $2.0-4.7M a year).

**(c), a disclosed judgment.** This is not [E5-20]'s class: the plants are modest (net property $142.3M at FY2025) and the product is assembled from purchased steel, so D&A is the corpus default [E3-44, E2-41] and **both ends are displayed as legitimate**. The capex end is the conservative one: total capex ran 0.7 to 2.3 times D&A (less amortisation), above it in ten of sixteen years, and the filer guides FY2026 capex to *"approximately $50 million to $55 million"* for *"modernization and productivity improvements planned at certain manufacturing facilities"*, part of which is maintenance by its own description (*"equipment replacement"*).

**By year ($M, `oe.py`, `oe_out.txt`):**

| fiscal year | OCF | SBC | D&A | of which acquired-intangible amortisation | total capex | OE, D&A end | OE, capex end |
|---|---|---|---|---|---|---|---|
| 2010 | 23.8 | 2.2 | 10.7 | 2.6 | 5.8 | 13.5 | 15.8 |
| 2011 | 43.1 | 3.5 | 11.7 | 2.8 | 8.4 | 30.6 | 31.2 |
| 2012 | 52.4 | 3.9 | 12.5 | 2.9 | 9.9 | 38.9 | 38.6 |
| 2013 | 57.5 | 4.6 | 12.6 | 2.8 | 11.1 | 43.1 | 41.8 |
| 2014 | 91.8 | 4.2 | 14.8 | 4.0 | 17.7 | 76.8 | 69.9 |
| 2015 | 49.3 | 3.3 | 16.4 | 4.7 | 15.2 | 34.2 | 30.7 |
| 2016 | 33.1 | 3.1 | 16.9 | 4.7 | 11.5 | 17.9 | 18.6 |
| 2017 | 39.4 | 3.6 | 16.7 | 4.4 | 8.9 | 23.6 | 27.0 |
| 2018 | 33.9 | 3.9 | 16.5 | 4.0 | 11.1 | 17.5 | 19.0 |
| 2019 | 3.8 | 4.2 | 14.0 | 2.9 | 23.2 | **-11.5** | **-23.6** |
| 2020 | 46.0 | 5.6 | 19.4 | 2.5 | 21.4 | 23.5 | 19.0 |
| 2021 | 44.0 | 6.2 | 19.2 | 2.2 | 26.5 | 20.8 | 11.3 |
| 2022 | 3.0 | 5.5 | 20.2 | 2.0 | 15.6 | **-20.6** | **-18.0** |
| 2023 | 119.7 | 6.5 | 19.3 | 2.0 | 18.8 | 95.9 | 94.4 |
| 2024 | 95.8 | 6.4 | 21.2 | 2.9 | 29.0 | 71.1 | 60.4 |
| 2025 | 132.9 | 8.1 | 20.9 | 2.2 | 42.5 | 106.2 | 82.4 |
| TTM to 2026-05-31 | 94.7 | 7.0 | 22.2 | (2.2 assumed) | 49.8 | 67.6 | 37.9 |

*(Figure cross-checked: FY2025 OCF 132,910, SBC 8,059, D&A 20,896, capex 42,496 in the filed statement. The FY2017 10-K restated FY2016 and FY2015 operating cash to 33,125 and 49,293 from 33,072 and 48,682; the later figures are used. TTM = FY2025 less nine months to 2025-05-31 plus nine months to 2026-05-31, from the 10-Q.)*

**Every window ending FY2025, on the cap of $1,161.8M:**

| window | capex end | D&A end | yield, capex end | yield, D&A end |
|---|---|---|---|---|
| 3y FY2023-25 | $79.0M | $91.0M | 6.80% | 7.84% |
| 4y FY2022-25 | $54.8M | $63.1M | 4.72% | 5.43% |
| **5y FY2021-25 (the corpus's default window [E2-42])** | **$46.1M** | **$54.7M** | **3.97%** | **4.71%** |
| 6y FY2020-25 | $41.6M | $49.5M | 3.58% | 4.26% |
| 7y FY2019-25 | $32.3M | $40.8M | 2.78% | 3.51% |
| 8y FY2018-25 | $30.6M | $37.9M | 2.63% | 3.26% |
| 9y FY2017-25 | $30.2M | $36.3M | 2.60% | 3.12% |
| **10y FY2016-25** | **$29.0M** | **$34.4M** | **2.50%** | **2.96%** |
| 11y FY2015-25 | $29.2M | $34.4M | 2.51% | 2.96% |
| 12y FY2014-25 | $32.6M | $37.9M | 2.80% | 3.27% |
| 13y FY2013-25 | $33.3M | $38.3M | 2.87% | 3.30% |
| 14y FY2012-25 | $33.7M | $38.4M | 2.90% | 3.30% |
| 15y FY2011-25 | $33.5M | $37.9M | 2.88% | 3.26% |
| **16y FY2010-25 (full span read)** | **$32.4M** | **$36.4M** | **2.79%** | **3.13%** |
| 16y without FY2023 and FY2025 | $24.4M | | 2.10% | |
| lean years FY2015-21 | $14.6M | $18.0M | 1.26% | 1.55% |

**Combined range across every window 3-16 years and both ends: $29.0M to $91.0M (2.5% to 7.8% on the cap).** Every window of six years or more sits at $29-50M (2.5-4.3%). **The bottom does not sit near zero on any window of three years or more, but two single years are below zero** (FY2019 -$23.6M, FY2022 -$18.0M on the capex end), and the seven lean years FY2015-FY2021 averaged $14.6M. **FY2023 and FY2025 carry 34% of the sixteen-year capex-end total.** [E4-41] instructs that favourable breaks be named and removed before the mean is trusted: **FY2023's $94.4M includes the release of the inventory FY2022 built** (*"Inventories ( 53,803 )"* in FY2022, *"40,954"* released in FY2023), so the three-year window that starts at FY2023 counts the release without the build and the four-year window is the honest short one; **FY2024-FY2026 carry the MENA project** (one customer at 13% of FY2025 revenue, deliveries into FY2026); storm-replacement demand is named by the MD&A in FY2014 (about $27.0M of revenue), FY2022 and FY2024; the IIJA highway money runs *"through September 2026"*. [E4-25]: the combined range is wide; whether it is too wide would be the Q4 finding had Q4 been opened.

**The screen row, refuted or confirmed.** *oe_bottom $46M* = this file's 5-year capex end ($46.1M): confirmed. *oe_top $89M* reproduces the 3-year window with full D&A including acquired-intangible amortisation (about $88.7M; $91.0M with the amortisation taken out); it sits on the window that counts the FY2023 inventory release without the FY2022 build. *level_shift 4.09 "STEP UP - normalize down [E4-41]"*: confirmed, and explained above (inventory release, MENA project, storms). *best_year_note "TWO YEARS JOINTLY CARRY THE WINDOW"*: confirmed (FY2023 and FY2025, 34% of the sixteen-year total). *level_note_oe "EARLY HALF STRADDLES ZERO"*: confirmed (FY2019 and FY2022 negative). *spread_caveat "CANNOT see variation older than the 5-year window"*: rebuilt here over sixteen years; the long windows are about two-thirds of the five-year figure. *wc_note*: the FY2022 cash-flow statement read at Step 0.

**Staying power [E5-11], scored as it would be.** (1) Operating cash positive every year FY2010-FY2025 but thin in FY2019 ($3.8M) and FY2022 ($3.0M). (2) Cash $154.8M at 2026-05-31 after $80.7M of buybacks ($250.6M at FY2025 year-end), plus the undrawn $50M revolver to 2030. (3) Near-term cash requirements: none large; the notes are due in February 2030; the X-Lite suits and the Nebraska remediation are accrued and not quantified here. **Interest paid $1.8M in FY2025 against operating cash net of all capex of $90.4M [E2-54].** Leverage is not how this business would die.

**The named death, as a signature only: #11 THE PASS-THROUGH** (the company survives but gains are passed to customers and suppliers, compressing the owner's return): price follows steel in both directions by the registrant's own account and slips in soft years, and the owner's after-tax return on its own measure was 5.9-7.2% through FY2015-FY2018 while the business stayed profitable at the operating line; **feature: [E2-58]'s supply-and-demand cycle** in a farm-income market (the seven lean years FY2015-FY2021 at $14.6M a year of capex-end owner earnings). Likelihood not stated: the file did not reach Q4. **Not entered in #11's instances column**, for the reason the PAGP, CALM, USPH, BDC, PPG and MATX folds gave. No new shape argued.

### COMPUTATION — NOT A CLEARANCE

*Arithmetic only, carrying no entry language; Q5 was not opened (operator rule 3).* On every window and both ends, $29.0M to $91.0M, over 10,168,885 shares: **at the ~10% floor [E4-28] with no growth, about $30 to $90 a share; at the sovereign (5.49%), about $50 to $165 a share**; on the sixteen-year capex end ($32.4M), about $30 at the floor and $60 at the sovereign; without FY2023 and FY2025 ($24.4M), about $25 and $45; **against $114.25**. The owner-earnings yield at the price is 2.5% to 7.8%, so reaching the ~10% floor needs **about 2 to 7.5 points of perpetual growth** on those bases (the screen's *growth_required* 6.0% sits inside that band); on every window of six years or more it needs about 5.7 to 7.5 points. Windage ONE (the capex end displayed beside the D&A default as the conservative end, stated above).

### Q6: reversal conditions, in words (no alert: the file failed on the business)

- A published record of irrigation price rising **in a year of flat or falling unit demand and flat or falling steel**, without volume loss, and held across the next soft year: [E2-44]'s first characteristic, which the registrant's MD&A has not shown in sixteen years.
- Lindsay's irrigation segment margin above Valmont's on the same basis **through a full farm downturn** (it was below in every year FY2015-FY2020), shown without a single large project in the year.
- The risk-factor sentence on price competition removed by the registrant, with the evidence for its removal filed.
- None of these would change the fact that four makers sell a substitute; a reversal would have to come from pricing conduct the filings do not now show.

## Q5: not opened. Q6: not opened as a gate (reversal conditions in words above).

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. **Q1 IN, Q2 OUT**; the file closed at Q2; Q3 to Q6 recorded beneath the close without verdicts.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests on the filings named.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives: none issued.
- [x] Every UNKNOWABLE verdict states what specifically cannot be known: none issued.
- [x] Step 0: the filing was read, with accession number (10-K FY2025 `0001193125-25-248751`, 10-Q to 2026-05-31 `0001193125-26-294516`); a figure was cross-checked (FY2025 OCF 132,910 = tag; SBC and capex likewise). No FY2026 10-K exists yet on EDGAR; stated.
- [x] Owner earnings on a multi-year mean (beneath the close); every window 3 to 16 years with both ends; the D&A end taken net of acquired-intangible amortisation; SBC complete; no NCI; no discontinued operations; no net-income proxy.
- [x] Competitor row filled from the one SEC filer among the three other main pivot makers (Valmont), identical construction, figures quoted from its filed segment notes; Reinke, T-L and the infrastructure rivals named as unobtainable; the verdict stated not to rest on the row.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated (US Treasury, 30 Yr, 09/25/2026, 5.49%), struck fresh; the 34% non-dollar revenue stated.
- [x] Value stated as a round-number range, not a point estimate (in the computation only; Q5 not opened).
- [x] One bar chosen, not both; windage count stated: n/a at Q5 (not opened); the computation's windage count is one.
- [x] Prices dated; aggregator used for live quotes only and flagged (Yahoo chart endpoint, close 2026-09-25).
- [x] Run committed to git with pathspecs (claim `94e59fcf`; Step 0 and Q1 `4856efae`; Q2 `53e89eb2`; this section and the register in the next commit; the fold after).
- [x] **Every ledger id cited in this file resolved against `principle_ledger.csv`** by script before the commit.
- [x] **The strongest evidence against the verdict is recorded and answered** [E4-26]: the high returns on operating capital, the rational four-maker oligopoly, the Road Zipper, the installed base, and Lindsay's lead over Valmont in FY2022-FY2025.

**Priors from the brief, tested.** The brief carried the screen row only and no business priors. Confirmed: the fiscal year ends in August; no FY2026 10-K is on EDGAR (the fiscal year ended 2026-08-31 and last year's 10-K was filed on 2025-10-23); `deal_note` is empty because nothing is deal-shaped; no Item 4.02. **The cap flag resolved the way the brief warned it might**: neither figure is wrong; the float is struck at $132.12 on 2025-02-28, the cap at $114.25 on a count 6% smaller. The 2022 cash-flow statement is a receivables and inventory build, reversed in FY2023.

**Tooling defects, reported, not patched.**
1. **`tools/run.py` prints *"GROWTH THE PRICE ASSUMES -15.3%"*** on a 6.78-7.63% yield against a 5.49% sovereign. At that yield the no-growth rate that equates price and value is about -1.3 to -2.1 points, not -15.3%; on the five-year window (3.97-4.71%) the price assumes about +0.8 to +1.5 points. **The third consecutive run with a growth figure of the wrong size or sign** (MATX -4.2%, PPG -9.2%).
2. **`tools/run.py`'s headline window (3 years, FY2023-FY2025) and the screen's `oe_top` count FY2023's release of FY2022's inventory build without the build** ($40,954K released in FY2023 against $53,803K built in FY2022), so *"1. THE YIELD 6.78% .. 7.63%"* is the most flattering window on the record; the four-year window ($54.8-63.1M, 4.7-5.4%) contains both halves. The `wc_note` flag found the 2022 year but nothing carries it to the window choice.
3. **The screen's `cap_flag` compares a float struck at the float's own date with a cap struck at a later price and count**, and calls one of them wrong. **Second run in three days where it fired on two dates and nothing was mis-filed** (PPG, LNN). The comparison that would test it is the float against the cap at the float's own date.
4. **The D&A end in `run.py` and the screen includes acquired-intangible amortisation** ($2.0-4.7M a year here), the older open ruling (resume state 11.5, item 2); small at Lindsay, recorded.
5. `cover_shares.py` worked on this filer and agreed with the cover read by hand.

## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- One line: **LNN FAIL at Q2 (OUT, on the business): an irrigation-equipment maker (84% of revenue) in a four-maker market where, in its own 10-K every year FY2010-FY2025, "Due to price competition [...] the Company may not be able to recoup increases in these costs through price increases", and where the market leader says "Pricing in the industry can become highly competitive, particularly during periods of low demand" ([E3-03] criterion 2); price follows steel both ways in the MD&A and slips in soft years, and irrigation margins move with Valmont's and alternate in rank ([E3-43]'s "a business"); the Road Zipper's narrow position sits in a 16% segment [E4-08]. Price $114.25 (2026-09-25) x 10,168,885 = $1,161.8M; owner earnings $29-91M over every window and both ends (2.5-7.8%), $29-50M on every window of six years or more.**
- **If UNRESEARCHED — THE WORK ORDER:** n/a
- **If UNKNOWABLE:** n/a

# ORLY research — Amazon and the channel

**Research file. Fetch-and-record only. No verdicts, no conclusions.**
Compiled 2026-09-02. Every figure carries its source and date. Gaps are marked **GAP**.

---

## 7. BLS CPI — annual average index values

**Source:** BLS Public Data API v2/v1, `https://api.bls.gov/publicAPI/v1/timeseries/data/`,
fetched 2026-09-02. Base 1982-84=100 except where noted. `M13` = annual average.
CUUR = CPI-U, US city average, **not seasonally adjusted**.

### 7a. CORRECTION TO THE BRIEF — series ID

The brief specified **`CUUR0000SETA02`** as "motor vehicle parts and equipment". **It is not.**
`SETA02` is **Used cars and trucks**. The fetched series shows 144.221 (2020) → 182.628 (2021)
→ 205.908 (2022), a +26.6% single-year jump — the used-vehicle price spike, not a parts series.

The correct item codes in the CPI taxonomy:

| Series ID | Item |
|---|---|
| `CUUR0000SETC` | **Motor vehicle parts and equipment** |
| `CUUR0000SETC01` | Tires |
| `CUUR0000SETC02` | Vehicle parts and equipment other than tires |
| `CUUR0000SETD` | Motor vehicle maintenance and repair |
| `CUUR0000SETA01` | New vehicles |
| `CUUR0000SETA02` | Used cars and trucks *(what the brief asked for by ID)* |
| `CUUR0000SA0` | All items |

Both the requested series and the correct one are recorded below.

### 7b. Annual average index values, 2013-2025

| Year | SA0 All items | **SETC Parts & equip** | SETC01 Tires | SETC02 Parts ex-tires | SETD Maint & repair | SETA01 New veh | SETA02 Used veh |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2013 | 232.957 | 146.422 | 131.040 | 162.159 | 261.641 | 145.783 | 149.887 |
| 2014 | 236.736 | 144.823 | 128.012 | 164.357 | 266.025 | 146.275 | 149.094 |
| 2015 | 237.017 | 144.236 | 126.535 | 166.066 | 270.717 | 147.135 | 147.120 |
| 2016 | 240.007 | 143.555 | 125.421 | 166.373 | 275.351 | 147.358 | 143.488 |
| 2017 | 245.120 | 143.041 | 124.014 | 167.676 | 280.827 | 146.992 | 138.259 |
| 2018 | 251.107 | 143.662 | 122.907 | 171.717 | 286.358 | 146.287 | 138.385 |
| 2019 | 255.657 | 146.437 | 125.019 | 175.566 | 296.000 | 146.834 | 139.763 |
| 2020 | 258.811 | 148.051 | 125.172 | 180.262 | 305.990 | 147.600 | 144.221 |
| 2021 | 270.970 | 155.100 | 132.215 | 186.165 | 317.945 | 156.240 | 182.628 |
| 2022 | 292.655 | 175.752 | 150.234 | 209.909 | 344.139 | 172.480 | 205.908 |
| 2023 | 304.702 | 180.806 | 153.289 | 218.957 | 383.829 | 178.899 | 191.222 |
| 2024 | 313.689 | 180.842 | 152.977 | 220.105 | 407.275 | 177.887 | 179.823 |
| 2025 | 321.943 | 184.705 | 156.637 | 222.910 | 431.435 | 178.462 | 184.931 |

### 7c. Derived — cumulative change, 2015 to 2025 (annual averages)

Recorded as arithmetic on the table above; no interpretation attached.

| Series | 2015 | 2025 | Change | CAGR |
|---|---:|---:|---:|---:|
| CPI-U all items (SA0) | 237.017 | 321.943 | **+35.83%** | +3.11%/yr |
| Motor vehicle parts & equipment (SETC) | 144.236 | 184.705 | **+28.06%** | +2.51%/yr |
| Tires (SETC01) | 126.535 | 156.637 | +23.79% | +2.16%/yr |
| Parts ex-tires (SETC02) | 166.066 | 222.910 | +34.23% | +2.99%/yr |
| Motor vehicle maintenance & repair (SETD) | 270.717 | 431.435 | **+59.37%** | +4.78%/yr |
| New vehicles (SETA01) | 147.135 | 178.462 | +21.29% | +1.95%/yr |
| Used cars and trucks (SETA02) | 147.120 | 184.931 | +25.70% | +2.32%/yr |

**Real (CPI-deflated) parts price, SETC / SA0, indexed 2015 = 100:**

| Year | SETC/SA0 real index (2015=100) |
|---:|---:|
| 2015 | 100.0 |
| 2016 | 98.3 |
| 2017 | 95.9 |
| 2018 | 94.0 |
| 2019 | 94.1 |
| 2020 | 94.0 |
| 2021 | 94.1 |
| 2022 | 98.7 |
| 2023 | 97.5 |
| 2024 | 94.8 |
| 2025 | 94.3 |

Sub-period detail: SETC **fell in nominal terms** every year from 2013 (146.422) to 2017
(143.041), a nominal decline of **-2.31%** across four years while all-items CPI rose +5.22%.
The nominal trough is 2017. Tires (SETC01) fell nominally from 131.040 (2013) to 122.907
(2018), **-6.21% nominal over five years**.

Note the divergence in the table: over 2015-2025 the price of **parts** rose slower than
CPI-U (+28.06% vs +35.83%), while the price of **labour to install them** (SETD, maintenance
and repair) rose far faster (+59.37%). Recorded as observation, not conclusion.

---

## 1. AMAZON'S PROFESSIONAL-INSTALLATION MOVE

**All dates verified. The "Ship-to-Store" program is the vehicle for the attack.**

### 1a. CORRECTION CARRIED FORWARD — Mavis / Pep Boys is 2026, NOT 2021

**Confirmed.** Mavis Tire Express Services agreed to acquire Pep Boys from Icahn
Enterprises L.P. for **$700 million in cash**, announced **2026-07-21**, closed
**2026-08-20**. Source: Mavis press release, `https://www.mavis.com/news/mavis-pep-boys/`,
corroborated by Modern Tire Dealer ("Mavis Completes Pep Boys Purchase") and Chain Store Age
(2026-08-21). Any date of 2021 for this transaction is wrong. See section 4.

### 1b. Timeline of Amazon installer partnerships

| Date | Event | Locations | Source |
|---|---|---:|---|
| **2018-07** | Monro pilot launches, greater Baltimore | **52** | AftermarketNews / Tire Business |
| **2018-07-26** | Monro agrees to become an Amazon.com tire installer (eastern US) | — | Tire Business |
| **2018-10-11** | Monro expands: +330 locations across 10 eastern states (GA, FL, IL, IN, OH, MD, MI, NY, TN, VA) | **~400** | AftermarketNews |
| **2018 (year)** | Sears Auto Center collaboration expanded | — | RetailDive |
| **2018-11-16** | **Pep Boys** takes Amazon Ship-to-Store tire installation national | **~1,000** | AftermarketNews |
| **2019** | Monro expands: +400 locations, 9 more central/western states | — | AftermarketNews |
| **2020-07-29** | Monro completes rollout to **entire store base**, 32 states | **1,200+** | Tire Review |

Monro quote (2020-07-29, CEO Brett Ponton): *"The rollout of our collaboration with
Amazon.com across our entire store base represents a key milestone in the development of our
online presence."*

Pep Boys quote (2018-11-16): *"Customers can now choose their neighborhood Pep Boys for the
fast, convenient and professional installation of any brand of tires they purchase on
Amazon.com."*

### 1c. What the service actually covers

Amazon's own category pages (`amazon.com` nodes 17738977011 "In-Store Installation
Automotive Services" and 17714886011 "Tires In-Store Installation Services") describe the
program as covering **tires, batteries and brakes**, not the full parts catalogue. Amazon
states service providers are Amazon-selected, background-checked, insured and licensed, and
that **service locations are visible only to buyers within roughly 30 miles of a service
center**, with coverage varying by product.

**Recorded observation, not conclusion:** the eight-year record above is a **tire-installation
programme that later added batteries and brakes**. No dated announcement was found extending
Amazon in-store installation to the general hard-parts catalogue. Searches for 2025-2026
expansion announcements returned nothing beyond the tires/batteries/brakes scope. Marked
**GAP** for any broader-catalogue installation move.

### 1d. The installer network is consolidating away from Amazon's counterparties

- **2025-11-08:** Carl Icahn disclosed a **~15% stake in Monro, Inc.** (CNBC). Monro is
  Amazon's nationwide tire installer. *(CNBC page returned HTTP 403 on direct fetch; headline
  and date confirmed via search index. Contents beyond the headline marked GAP.)*
- **2026-08-20:** Pep Boys, Amazon's other named national installer, passed to **Mavis**,
  which now operates **4,400+ service centers** in the US and Canada.

---

## 2. CARPARTS.COM (PRTS) — THE ONLINE-NATIVE PURE-PLAY

**CIK 0001378950. Still listed: Nasdaq Capital Market, ticker PRTS.** Not delisted as of
2026-09-02. Formerly U.S. Auto Parts Network, Inc.; rebranded CarParts.com **July 2020**.

### 2a. Net sales by fiscal year — from SEC XBRL company facts, 10-K figures only

Fiscal year is 52/53 weeks. `SalesRevenueNet` for FY2009-FY2017,
`RevenueFromContractWithCustomerIncludingAssessedTax` FY2017-FY2023,
`...ExcludingAssessedTax` FY2023-FY2025. Retrieved from
`data.sec.gov/api/xbrl/companyfacts/CIK0001378950.json`, 2026-09-02.

| Fiscal year | Period end | Net sales (USD) | YoY |
|---|---|---:|---:|
| FY2017 | 2017-12-30 | 303,366,000 | — |
| FY2018 | 2018-12-29 | 289,467,000 | -4.6% |
| FY2019 | 2019-12-28 | 280,657,000 | -3.0% |
| **FY2020** | 2021-01-02 | **443,884,000** | **+58.2%** |
| FY2021 | 2022-01-01 | 582,440,000 | +31.2% |
| FY2022 | 2022-12-31 | 661,604,000 | +13.6% |
| **FY2023** | 2023-12-30 | **675,729,000** | +2.1% (peak) |
| FY2024 | 2024-12-28 | 588,846,000 | -12.9% |
| FY2025 | 2026-01-03 | 547,525,000 | -7.0% |

Longer tail, same source: FY2009 176,288,000 · FY2010 262,277,000 · FY2011 327,072,000 ·
FY2012 304,017,000 · FY2013 254,753,000 · FY2014 283,508,000 · FY2015 290,833,000 ·
FY2016 303,324,000.

**Recorded:** revenue was **flat-to-declining 2011-2019** (327.1m in 2011 to 280.7m in 2019),
jumped **+58% in the COVID year**, peaked FY2023, and has fallen **-19.0% from peak** across
FY2024-FY2025.

### 2b. Losses and cash

Source: PRNewswire release **2026-03-05**, "CarParts.com Reports Fourth Quarter and Fiscal
Year 2025 Results", and 10-K accession **0001378950-26-000035** (filed 2026-03-05, FY ended
2026-01-03).

| Metric | FY2024 | FY2025 |
|---|---:|---:|
| Net sales | $588.8m | $547.5m |
| Net loss | ($40.6)m | **($50.4)m** |
| Loss per share | ($0.71) | ($0.82) |
| Adjusted EBITDA | — | ($14.0)m |
| Cash | — | $25.8m (at 2026-01-03) |

Q4 FY2025: net sales $120.4m (-10%), net loss ($11.6)m, adj. EBITDA ($2.2)m.

CEO David Meniane, in the 2026-03-05 release: *"Our path to free cash flow is not dependent
on a demand rebound. It's driven by higher contribution margins, a materially lower fixed cost
base, and improving capital efficiency through our partnerships. This is an execution story,
not a turnaround narrative."*

### 2c. Listing status, bid-price deficiency and reverse split — VERBATIM from the FY2025 10-K

> "On June 13, 2025, we received a deficiency letter from the Listing Qualifications
> Department of Nasdaq indicating that, for the last thirty consecutive business days, the bid
> price for our common stock had closed below the minimum $1.00 per share requirement for
> continued listing on The Nasdaq Global Market under Nasdaq Listing Rule 5450(a)(1). In
> accordance with Nasdaq Listing Rule 5810(c)(3)(A), we were provided an initial period of 180
> calendar days, or until December 10, 2025, to regain compliance."

> "In response, on December 9, 2025, we submitted an application to transfer the listing of our
> common stock from the Nasdaq Global Select Market to the Nasdaq Capital Market. On December
> 15, 2025, the Nasdaq Listing Qualifications department approved our request to transfer the
> listing of our common stock from the Nasdaq Global Select Market to The Nasdaq Capital
> Market."

> "…including by effecting a reverse stock split if necessary. If Nasdaq delists our common
> stock from trading on its exchange and we are not able to list our securities on another
> national securities exchange, we expect our securities could be quoted on an over-the-counter
> market. In such case, our stockholders' ability to trade, or obtain quotations of the market
> value of our common stock would be severely limited…"

**Reverse split executed after the 10-K:** 1-for-10, approved by shareholders May 2026,
**effective 2026-05-25 at 11:59pm ET**, split-adjusted trading from **2026-05-26**. Symbol
stays PRTS; new CUSIP 14427M206. Source: company announcement via TipRanks / Globe and Mail /
OCC Info Memo #59031 (2026-05-21).

**GOING CONCERN: none.** A search of the full FY2025 10-K text returns **zero hits** for
"going concern" and zero for "substantial doubt". Recorded as an absence, not as a comfort.

### 2d. Competition — VERBATIM from the FY2025 10-K, Item 1 (Business)

> "…the vehicle repair information and parts industry is competitive and highly fragmented,
> with products distributed across multiple channels, including direct-to-consumer eCommerce
> platforms, online marketplaces, specialty retailers, wholesale distributors and traditional
> brick-and-mortar stores. We compete with both online and offline retailers who offer original
> equipment manufacturer ("OEM"), aftermarket and private label parts to either the DIY or
> Do-It-For-Me ("DIFM") customer segments. Current or potential competitors include the
> following: ● national auto parts retailers such as Advance Auto Parts, AutoZone, Napa Auto
> Parts, O'Reilly Auto Parts and Pep Boys; ● large online marketplaces such as Amazon.com
> ("Amazon") and sellers on eBay; ● other online retailers of automotive products and auto
> repair information websites; ● local independent retailers or niche auto parts retailers;
> ● wholesale aftermarket auto parts distributors such as LKQ Corporation; and ● manufacturers,
> brand suppliers and other distributors selling online directly to consumers."

> "We believe the principal competitive factors in our market are helping customers easily find
> the correct parts for their vehicles, educating consumers on the service and maintenance of
> their vehicles, maintaining a proprietary product catalog that maps individual parts to
> relevant vehicle applications, broad product selection and availability, price, knowledgeable
> customer service, rapid order fulfillment and delivery, and easy product returns. We believe
> we compete favorably on the basis of these factors. However, some of our competitors may be
> larger, may have stronger brand recognition or may have access to greater financial,
> technical and marketing resources or may have been operating longer than we have."

Risk-factor heading, verbatim:

> "We face intense competition and operate in an industry with limited barriers to entry, and
> some of our competitors may have greater resources than us and may be better positioned to
> capitalize on the growing eCommerce auto parts market."

Note the FY2024 10-K carried the same list but named **CarQuest** as well; the FY2025 list
drops CarQuest and renames "Napa Auto Parts". Recorded as a wording change, no inference.

### 2e. Note — CARPARTS.COM SELLS ON AMAZON

From the same 10-K, Item 1:

> "We also sell our products through online marketplaces, including third-party auction sites
> like eBay and shopping portals including Amazon, which provide us with access to additional
> consumer segments."

> "Garage-Pro® products are offered primarily through Amazon, serving value-oriented consumers
> seeking dependable replacement parts."

Amazon is listed simultaneously as a **competitor** and as a **sales channel**. Recorded as
fact from the filing.

### 2f. Most recent state (2025-2026)

- **2025-09:** closed a **$35.7m strategic investment** from **A-Premium, ZongTeng Group and
  CDH Investments** (10-K Item 1; 8-K 2025-09-11).
- **2026-01-27:** sold its **Philippines subsidiary** to a third party (10-K, Note 12
  Subsequent Events). Headcount at 2026-01-03 was 1,186 (741 US, 445 Philippines).
- **Market data, 2026-09-02** (stockanalysis.com, an **aggregator, flagged per operator rule
  5**): share price **$7.93**, market cap **$64.12m**, shares out **8.07m**, 52-week range
  **$3.72 to $13.60** (all split-adjusted; divide by 10 for pre-split equivalents, i.e. a
  52-week low of about **$0.37** pre-split).

**Recorded arithmetic:** a **$64m** market capitalisation on **$548m** of FY2025 revenue.

---

## 3. ROCKAUTO — SIZING

**Private, family-owned, no SEC filings. No credible primary sizing exists.**

Founded **1999** by the Smith family, Madison, Wisconsin.

Estimates found, all from **commercial data vendors, none primary, all flagged**:

| Source | Figure | Note |
|---|---|---|
| Grips Intelligence | **$701.9m** online store sales, 2025 | vendor traffic/panel model |
| LeadIQ | **$50m to $100m** annual revenue (as of 2026-07) | firmographic vendor |
| LeadIQ | ~**92 employees**, 3 continents | firmographic vendor |
| ECDB | series 2015-2027 (not retrieved) | vendor model |

The spread between vendor estimates is **7x to 14x**. These are incompatible and cannot be
reconciled from public information.

**VERDICT: GAP.** No reliable revenue figure for RockAuto is obtainable. Do not use any of the
above as a fact. The only defensible statements are that RockAuto is private, US-based,
founded 1999, and headcount-light relative to its apparent catalogue breadth.

---

## 4. PEP BOYS / ICAHN AUTOMOTIVE AFTER THE 2015 TAKE-PRIVATE

### 4a. The transaction

- **2015-12:** Icahn Enterprises wins Pep Boys after a bidding war against **Bridgestone**.
  **$18.50/share, ~$1.031 billion** aggregate equity value.
- **2016-02-04:** acquisition **completed**.
- **At acquisition:** *"more than 800 locations in 35 states and Puerto Rico."*

### 4b. What Icahn did with it — the retail parts exit

- **2021-03:** Pep Boys announces **109 California stores** will be taken over by **Advance
  Auto Parts**; Icahn Automotive **leased 109 adjoining properties in California to Advance
  Auto Parts**. Conversions ran through 2021-2022. (Philadelphia Inquirer 2021-03-31;
  MyRGV 2021-05-04; AAP 10-Q FY2022 and 10-K FY2022.)
- **2021-06-03:** further store closures announced (Philadelphia Inquirer).
- Pep Boys **exited the retail auto parts business entirely** and repositioned as a **service
  and repair** chain. *"The company is no longer in the business of selling auto parts to
  walk-in customers."* Roughly **81 storefronts** (6,400 to 15,700 sq ft) adjoining Pep Boys
  service centers were put up for lease/sublease across 24 states. (Chain Store Age; direct
  fetch returned HTTP 403, content via search index. **Exact article date GAP.**)
- Reported footprint in the service-only format: *"more than 7,500 service bays in more than
  900 locations in 35 states and Puerto Rico."* (secondary sources, undated. **Flagged.**)

### 4c. The rest of Icahn Automotive

- **2018:** Icahn sells **Federal-Mogul** (parts manufacturing).
- **2023-01:** **Auto Plus**, which operated the majority of Icahn's **Aftermarket Parts**
  business, files a **voluntary bankruptcy petition**, ceases operations, and is
  **deconsolidated**.
- **Q4 2024:** Automotive segment agreed with a tenant to terminate a group of leases,
  effective 2025-03-31.
- **Q1 2025:** Icahn Enterprises **exited the Aftermarket Parts business** entirely.
  (IEP 10-K FY2024, accession 0001558370-25-001612; IEP 10-K FY2025.)
- **2025-10 / 2025-11:** Automotive segment transferred **$465 million of owned real estate**
  to IEP's **Real Estate segment**.
- **2025-11-08:** Icahn discloses a **~15% stake in Monro, Inc.** (CNBC).

### 4d. The end state

- **2026-07-21:** Mavis agrees to buy Pep Boys for **$700m cash** from Icahn Enterprises.
- **2026-08-20:** deal **effective / completed**.
- **Pep Boys at sale: "nearly 800 locations" nationwide.**
- **Mavis after the deal: "more than 4,400 service center locations"** across the US and Canada.

Quotes from the 2026-07-21 Mavis release:
David Sorbaro, Co-CEO of Mavis: *"Pep Boys is one of the most well-respected names in the
automotive aftermarket, and we look forward to welcoming it into the Mavis family."*
Carl C. Icahn, Chairman of IEP: *"We welcome the Mavis acquisition and are thankful to all of
the employees of Pep Boys who made this transaction possible."*

**Recorded arithmetic:** store count went from **"more than 800" (Feb 2016)** to **"nearly
800" (Aug 2026)**, approximately flat in count, but the **format changed completely**: from a
combined retail-parts-plus-service chain to a **service-only** chain, with the retail parts
business closed or handed to Advance Auto Parts, and the separate aftermarket parts
distribution arm (Auto Plus) bankrupt in 2023. Icahn's equity outlay of ~$1.03bn in 2016
returned **$700m in cash in 2026** for the Pep Boys asset, before the separately-retained
$465m of real estate transferred out in late 2025 and before ten years of interim cash flows.
No conclusion drawn.

Reported segment datapoint, for scale: Icahn automotive group sales were **$596m in Q4 2020**
vs **$703m in Q4 2019**.

---

## 5. AVERAGE AGE OF THE US LIGHT-VEHICLE FLEET

**Publisher:** S&P Global Mobility (the former automotive team of IHS Markit; earlier releases
carry the IHS Markit or Polk name). Released annually in **May**.

### 5a. Figures obtained, with the release that carries them

| Reference year | Average age, US light vehicles | Release date | Source |
|---:|---:|---|---|
| 2022 | **12.2 years** | 2022-05-23 | Businesswire, "Average Age of Vehicles in the US Increases to 12.2 years" |
| 2023 | **12.5 years** | 2023-05-15 | press.spglobal.com |
| 2024 | **12.6 years** | 2024-05-22 | press.spglobal.com |
| **2025** | **12.8 years** | **2025-05-21** | press.spglobal.com |

Note the arithmetic in the 2025 release: *"an increase of two months for the second
consecutive year"*, and the 2024 release: *"up by two months over 2023"*. The 2024 release's
own comparator is **12.4 years for 2023**, while the 2023 release headline is **12.5 years**.
**The series is restated between releases.** Recorded as a discrepancy, not reconciled.

**2015-2021: GAP.** Prior-year figures under the IHS Markit / Polk banner were not retrievable
from primary press releases within this time box. The only anchor recovered is that IHS Markit
reported average age *"approaches 12 years"* for 2021. The BTS table
(`bts.gov/content/average-age-automobiles-and-trucks-operation-united-states`) returned
**HTTP 403** and could not be read.

**2026: GAP / NOT FOUND.** No May-2026 S&P Global Mobility release was located. The most
recent figure on record remains **12.8 years (May 2025)**. A separate forecaster, **CCC**,
projects average age to reach **13 years by 2026**, flagged as a **third-party projection,
not an S&P Global Mobility measurement**.

### 5b. Sub-series from the 2025-05-21 release (reference year 2025)

| Measure | Figure |
|---|---:|
| Passenger cars, average age | **14.5 years** |
| Light trucks, average age | **11.9 years** |
| Vehicles in operation | **289 million** |
| New vehicle registrations, 2024 | **16+ million** (first time since 2019) |
| Scrappage rate | **4.5%** |
| Battery electric vehicles, average age | 3.7 years |
| Plug-in hybrids | 4.9 years (unchanged) |
| Traditional hybrids | 6.4 years (from 6.9 prior year) |

Also from that release: **passenger cars fell below 100 million for the first time since the
1970s**. And from Tire Review (2024-05-29) quoting S&P Global Mobility: vehicles under six
years old were ~**35% of the fleet in 2019** and are now **under 31%**.

---

## 6. US VEHICLE MILES TRAVELLED — FHWA TRAFFIC VOLUME TRENDS

**Source:** Federal Highway Administration, *Traffic Volume Trends*, **December issue of each
year**, at `fhwa.dot.gov/policyinformation/travel_monitoring/<YY>dectvt/`. Each December issue
states the cumulative estimate for that full calendar year. Fetched 2026-09-02.

| Year | Cumulative VMT (billions of vehicle miles) | Change vs prior year, as stated |
|---:|---:|---:|
| 2015 | **3,147.8** | +3.5% (+107.2 bn) |
| 2016 | **3,218.0** | +2.8% (+87.5 bn) |
| 2017 | **3,208.5** | +1.2% (+39.3 bn) |
| 2018 | **3,224.9** | +0.4% (+12.2 bn) |
| 2019 | **3,269.1** | +0.9% (+28.8 bn) |
| **2020** | **2,829.7** | **-13.2% (-430.2 bn)** |
| 2021 | **3,228.8** | +11.2% (+325.2 bn) |
| 2022 | **3,169.4** | +0.9% (+29.3 bn) |
| 2023 | **3,263.7** | +2.1% (+67.5 bn) |
| 2024 | **3,279.1** | +1.0% (+32.3 bn) |
| **2025** | **3,323.8** | +0.9% (+29.8 bn) |

**CAUTION — the levels and the percentage changes do not tie.** FHWA states the December
estimates *"are re-adjusted annually to match the vehicle miles of travel from the Highway
Performance Monitoring System."* Worked example: 2022 is reported at 3,169.4 bn and 2023 at
3,263.7 bn, a difference of +94.3 bn, but the 2023 report states the change as +67.5 bn.
Likewise 2016 (3,218.0) to 2017 (3,208.5) is a **decline in level** while the stated change is
**+1.2%**. **Use each year's level as first published, or use the stated percentage changes,
but do not mix them.** Recorded as a data caveat.

**Cross-check against a different FHWA product (operator rule 4):** Highway Statistics 2024
**Table VM-1** reports total annual VMT for **all motor vehicles** in 2024 as **3,294,031
million miles** (3.294 trillion). The December 2024 TVT figure is **3,279.1 billion**. The two
differ by ~15 bn (0.5%); VM-1 covers all motor vehicles including buses, motorcycles and
combination trucks on an HPMS basis. Both recorded; neither reconciled.

**Monthly 2025 detail** (seasonally adjusted, millions of miles), from the same series:
Q1 278,787 · Q2 286,871 · Q3 279,611 · Q4 265,855. January 2026 seasonally adjusted: 277,162.

**Recorded arithmetic, 2015 to 2025:** 3,147.8 bn to 3,323.8 bn = **+5.59% over ten years**,
a CAGR of **+0.55%/yr**. Peak-to-trough 2019 to 2020 was **-13.4%**; 2025 is **+1.67%** above
the 2019 pre-COVID level.

---

## SOURCE LEDGER FOR SECTIONS 1-6

| # | Source | Retrieved |
|---|---|---|
| 1 | mavis.com/news/mavis-pep-boys/ (press release, 2026-07-21) | 2026-09-02 |
| 1 | aftermarketnews.com — Pep Boys/Amazon national (2018-11-16) | 2026-09-02 |
| 1 | aftermarketnews.com — Monro/Amazon expansion (2018-10-11) | 2026-09-02 |
| 1 | tirereview.com — Monro all locations (2020-07-29) | 2026-09-02 |
| 1 | amazon.com nodes 17738977011, 17714886011 (service scope) | 2026-09-02 |
| 2 | SEC XBRL companyfacts CIK0001378950 | 2026-09-02 |
| 2 | SEC 10-K accession **0001378950-26-000035**, filed 2026-03-05, FY end 2026-01-03 | 2026-09-02 |
| 2 | SEC 10-K accession 0001378950-25-000036, filed 2025-03-26 | 2026-09-02 |
| 2 | PRNewswire FY2025 results release, 2026-03-05 | 2026-09-02 |
| 2 | OCC Info Memo #59031, 2026-05-21 (reverse split) | 2026-09-02 |
| 2 | stockanalysis.com/stocks/prts/ — **AGGREGATOR, quote only, flagged** | 2026-09-02 |
| 3 | Grips Intelligence / LeadIQ / ECDB — **all vendor estimates, flagged, GAP** | 2026-09-02 |
| 4 | ielp.com — Icahn Enterprises completes Pep Boys acquisition (2016-02-04) | 2026-09-02 |
| 4 | IEP 10-K FY2024 acc. 0001558370-25-001612; IEP 10-K FY2025 | 2026-09-02 |
| 4 | Philadelphia Inquirer 2021-03-31 and 2021-06-03 | 2026-09-02 |
| 5 | press.spglobal.com releases 2023-05-15, 2024-05-22, 2025-05-21 | 2026-09-02 |
| 5 | businesswire.com 2022-05-23 (12.2 years) | 2026-09-02 |
| 6 | fhwa.dot.gov Traffic Volume Trends, December issues 2015-2025 | 2026-09-02 |
| 6 | fhwa.dot.gov Highway Statistics 2024, Table VM-1 | 2026-09-02 |

**Failed fetches (HTTP 403), recorded so they are not silently treated as absent:**
`bts.gov` average-age table · `chainstoreage.com` Pep Boys parts-exit article ·
`cnbc.com` Icahn/Monro article. Facts drawn from these three carry search-index provenance
only and are flagged in place.

---

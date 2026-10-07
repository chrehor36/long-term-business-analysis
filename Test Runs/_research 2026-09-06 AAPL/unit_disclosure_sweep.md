# APPLE (AAPL), UNIT DISCLOSURE SWEEP
**CIK 0000320193 · research date 2026-09-06 · all documents from SEC EDGAR primary filings**
User-agent used: `Chris Hrehor chrehor36@gmail.com`

Tests being run: **[E4-55] physical-series test** (where units exist, monitor units) and
**[E2-49] metric-withdrawal test** (a yardstick withdrawn on deterioration is a Q3 flag).

---

## 0. THE FILING INVENTORY (from EDGAR submissions JSON)

Source: `https://data.sec.gov/submissions/CIK0000320193.json` and
`https://data.sec.gov/submissions/CIK0000320193-submissions-001.json`, both fetched 2026-09-06.

### 10-K vintages, FY2011 through FY2025

| FY (period end) | Filed | Accession | Primary document |
|---|---|---|---|
| FY2011 (2011-09-24) | 2011-10-26 | 0001193125-11-282113 | d220209d10k.htm |
| FY2012 (2012-09-29) | 2012-10-31 | 0001193125-12-444068 | d411355d10k.htm |
| FY2013 (2013-09-28) | 2013-10-30 | 0001193125-13-416534 | d590790d10k.htm |
| FY2014 (2014-09-27) | 2014-10-27 | 0001193125-14-383437 | d783162d10k.htm |
| FY2015 (2015-09-26) | 2015-10-28 | 0001193125-15-356351 | d17062d10k.htm |
| FY2016 (2016-09-24) | 2016-10-26 | 0001628280-16-020309 | a201610-k9242016.htm |
| FY2017 (2017-09-30) | 2017-11-03 | 0000320193-17-000070 | a10-k20179302017.htm |
| FY2018 (2018-09-29) | 2018-11-05 | 0000320193-18-000145 | a10-k20189292018.htm |
| FY2019 (2019-09-28) | 2019-10-31 | 0000320193-19-000119 | a10-k20199282019.htm |
| FY2020 (2020-09-26) | 2020-10-30 | 0000320193-20-000096 | aapl-20200926.htm |
| FY2021 (2021-09-25) | 2021-10-29 | 0000320193-21-000105 | aapl-20210925.htm |
| FY2022 (2022-09-24) | 2022-10-28 | 0000320193-22-000108 | aapl-20220924.htm |
| FY2023 (2023-09-30) | 2023-11-03 | 0000320193-23-000106 | aapl-20230930.htm |
| FY2024 (2024-09-28) | 2024-11-01 | 0000320193-24-000123 | aapl-20240928.htm |
| FY2025 (2025-09-27) | 2025-10-31 | 0000320193-25-000079 | aapl-20250927.htm |

No FY2026 10-K exists as of 2026-09-06 (Apple's FY2026 ends late Sept 2026).

### Transition-period 10-Qs and 8-Ks (FY2018 Q1 – FY2019 Q4)

| Form | Period | Filed | Accession | Primary document |
|---|---|---|---|---|
| 10-Q | 2017-12-30 (Q1 FY18) | 2018-02-02 | 0000320193-18-000007 | a10-qq1201812302017.htm |
| 8-K | 2018-02-01 (Q1 FY18 results) | 2018-02-01 | 0000320193-18-000005 | a8-kq1201812302017.htm |
| 10-Q | 2018-03-31 (Q2 FY18) | 2018-05-02 | 0000320193-18-000070 | a10-qq220183312018.htm |
| 8-K | 2018-05-01 (Q2 FY18 results) | 2018-05-01 | 0000320193-18-000067 | a8-kq220183312018.htm |
| 10-Q | 2018-06-30 (Q3 FY18) | 2018-08-01 | 0000320193-18-000100 | a10-qq320186302018.htm |
| 8-K | 2018-07-31 (Q3 FY18 results) | 2018-07-31 | 0000320193-18-000098 | a8-kq320186302018.htm |
| **8-K** | **2018-11-01 (Q4/FY18 results)** | **2018-11-01** | **0000320193-18-000142** | a8-kq420189292018.htm |
| **10-K** | **FY2018** | **2018-11-05** | **0000320193-18-000145** | a10-k20189292018.htm |
| 8-K | 2019-01-02 (revenue guidance revision) | 2019-01-02 | 0000320193-19-000002 | a8-kjanuary2019122019.htm |
| **10-Q** | **2018-12-29 (Q1 FY19)** | **2019-01-30** | **0000320193-19-000010** | a10-qq1201912292018.htm |
| 8-K | 2019-01-29 (Q1 FY19 results) | 2019-01-29 | 0000320193-19-000007 | a8-kq1201912292018.htm |
| 10-Q | 2019-03-30 (Q2 FY19) | 2019-05-01 | 0000320193-19-000066 | a10-qq220193302019.htm |
| 10-Q | 2019-06-29 (Q3 FY19) | 2019-07-31 | 0000320193-19-000076 | a10-qq320196292019.htm |
| 8-K | 2019-10-30 (Q4/FY19 results) | 2019-10-30 | 0000320193-19-000117 | a8-kq420199282019.htm |
| 10-K | FY2019 | 2019-10-31 | 0000320193-19-000119 | a10-k20199282019.htm |

*(sweep continues below, written incrementally)*

---

## 1. THE TERM SWEEP, machine count of disclosure terms, 14 10-K vintages

Method: each 10-K primary document downloaded from EDGAR, HTML stripped to text (table cells
piped), case-insensitive whole-word regex count. This is a **recorded sweep**: the terms
searched are listed; a zero is a searched zero, not an assumption.

| term searched | FY12 | FY13 | FY14 | FY15 | FY16 | FY17 | FY18 | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `unit sales` | 22 | 25 | 36 | 32 | 27 | 14 | **12** | **2** | 0 | 0 | 0 | 0 | 0 | 0 |
| `units sold` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `average selling price` | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `selling price` | 9 | 9 | 9 | 9 | 9 | 10 | 9 | **0** | 0 | 0 | 0 | 0 | 0 | 0 |
| `ASP` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `units` | 10 | 9 | 9 | 10 | 10 | 10 | 6 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |
| `installed base` | 2 | 3 | 4 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 0 |
| `active devices` | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| `active installed base` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `volume` | 3 | 3 | 5 | 3 | 5 | 5 | 3 | 3 | 4 | 3 | 3 | 4 | 1 | 1 |

Two facts fall straight out:

1. **`ASP` never appears in any Apple 10-K, FY2012–FY2025 (14 vintages, zero hits).** The
   phrase `average selling price(s)` appears only as **narrative** (`higher/lower average
   selling prices`), never as a disclosed number. Apple has **never** printed an iPhone ASP
   figure in a 10-K. Any ASP in this run is **derived** (net sales ÷ units) and is labelled as such.
2. The `unit sales` count collapses 12 → 2 between the FY2018 and FY2019 10-Ks, and the
   residual 2 in FY2019 are **narrative, not a table** (shown below).

---

## 2. THE UNIT SERIES, AS FILED (units in thousands)

Every figure below is the number as printed in the 10-K for that fiscal year, under the
caption **"Unit Sales by Product:"**.

| FY | 10-K accession | iPhone | iPad | Mac | iPod |
|---|---|---|---|---|---|
| 2012 | 0001193125-12-444068 | 125,046 | 58,310 | 18,158 (Desktops 4,656 + Portables 13,502) | 35,165 |
| 2013 | 0001193125-13-416534 | 150,257 | 71,033 | 16,341 | 26,379 |
| 2014 | 0001193125-14-383437 | 169,219 | 67,977 | 18,906 | 14,377 |
| 2015 | 0001193125-15-356351 | 231,218 | 54,856 | 20,587 | *(iPod line dropped)* |
| 2016 | 0001628280-16-020309 | 211,884 | 45,590 | 18,484 | n/a |
| 2017 | 0000320193-17-000070 | 216,756 | 43,753 | 19,251 | n/a |
| **2018** | **0000320193-18-000145** | **217,722** | **43,535** | **18,209** | n/a |
| 2019 | 0000320193-19-000119 | **ABSENT** | ABSENT | ABSENT | n/a |
| 2020–2025 | n/a | ABSENT | ABSENT | ABSENT | n/a |

### Exact table captions, verbatim

- **FY2012** (0001193125-12-444068): *"The following table shows net sales by operating segment
  and net sales and unit sales by product during 2012, 2011, and 2010 (dollars in millions and
  units in thousands):"*, row labels are `Desktops (a)`, `Portables (b)`, `Total Mac unit
  sales`, `iPod unit sales`, `iPhone units sold`, `iPad units sold`.
- **FY2013** (0001193125-13-416534): *"The following table shows net sales by operating segment
  and net sales and unit sales by product during 2013, 2012 and 2011 (dollars in millions and
  units in thousands):"*, rows now simply `iPhone`, `iPad`, `Mac`, `iPod`.
- **FY2014** (0001193125-14-383437), under heading **"Sales Data"**: *"The following table shows
  net sales by operating segment and net sales and unit sales by product during 2014, 2013 and
  2012 (dollars in millions and units in thousands):"*
- **FY2015** (0001193125-15-356351): *"The following table shows net sales by operating segment
  and net sales and unit sales by product during 2015, 2014 and 2013 (dollars in millions and
  units in thousands):"* ... iPod row **removed** this vintage; iPod folded into "Other Products".
- **FY2016** (0001628280-16-020309): *"The following table shows net sales by operating segment
  and net sales and unit sales by product during 2016 , 2015 and 2014 (dollars in millions and
  units in thousands):"*
- **FY2017** (0000320193-17-000070): *"The following table shows net sales by operating segment
  and net sales and unit sales by product for 2017 , 2016 and 2015 (dollars in millions and units
  in thousands):"*
- **FY2018** (0000320193-18-000145), **THE LAST ONE**: *"The following table shows net sales by
  reportable segment and net sales and unit sales by product for 2018 , 2017 and 2016 (dollars in
  millions and units in thousands):"*

In addition, FY2015–FY2018 each carry **three separate per-product tables** in a "Product
Performance" subsection, each captioned e.g. (FY2018, verbatim):

> *"The following table presents iPhone net sales and unit sales information for 2018 , 2017 and
> 2016 (dollars in millions and units in thousands):"*

with rows `Net sales`, `Percentage of total net sales`, `Unit sales`. Identical constructions
for iPad and for Mac. **All three disappear in FY2019.**

---

## 3. iPhone: UNITS vs REVENUE, AND THE DERIVED ASP

`Net sales` per the 10-K "Net Sales by Product" table; `Unit sales` per the "Unit Sales by
Product" table; **ASP is COMPUTED here, not disclosed** (net sales ÷ units). Caveat carried
forward: Apple's iPhone net sales line is footnoted *"Includes deferrals and amortization of
related software upgrade rights and non-software services"* (FY2015–FY2018 footnote (1)), so the
derived ASP is a revenue-per-unit, not a list price.

| FY | iPhone net sales ($M) | iPhone units (000) | **Derived ASP ($)** | Units YoY | Net sales YoY |
|---|---|---|---|---|---|
| 2012 | 80,477 *(line reads "iPhone and related products and services")* | 125,046 | 643.58 | +73% | +71% |
| 2013 | 91,279 | 150,257 | 607.49 | +20% | +13% |
| 2014 | 101,991 | 169,219 | 602.72 | +13% | +12% |
| **2015** | **155,041** | **231,218** | **670.54** | **+37%** | **+52%** |
| **2016** | **136,700** | **211,884** | **645.16** | **(8)%** | **(12)%** |
| **2017** | **141,319** | **216,756** | **651.97** | **+2%** | **+3%** |
| **2018** | **166,699** | **217,722** | **765.65** | **0%** *(printed as an em-dash %)* | **+18%** |
| 2019 | 142,381 | **NOT DISCLOSED** | **NOT COMPUTABLE** | n/a | (14)% |

**This is the [E4-55] Precision Steel shape, exactly.** In FY2018 the physical series went flat
(217,722 vs 216,756, printed by Apple as a dash for 0%) while dollar revenue rose 18%, the rise
came entirely from price. Apple's own MD&A says so, verbatim (FY2018 10-K, 0000320193-18-000145):

> *"iPhone net sales increased during 2018 compared to 2017 due primarily to a different mix of
> iPhones resulting in higher average selling prices."*

Contrast the prior year, where Apple credited volume (same document):

> *"iPhone net sales increased during 2017 compared to 2016 due to higher iPhone unit sales and a
> different mix of iPhones with higher average selling prices."*

And FY2016, where Apple conceded the unit decline in its own words (FY2016 10-K,
0001628280-16-020309):

> *"iPhone net sales and unit sales decreased during 2016 compared to 2015."*

iPad and Mac units, over the same window, were **already declining**: iPad 71,033 (FY13) →
43,535 (FY18), a 39% fall in six years; Mac 20,587 (FY15) → 18,209 (FY18).

**Peak iPhone units is FY2015 at 231,218 thousand. The metric was withdrawn three years after
the peak, in the first year the series stopped growing at all.**

---

## 4. DATING THE WITHDRAWAL PRECISELY

### 4.1 EDGAR full-text search, all Apple filings, term `"unit sales"`
Query: `https://efts.sec.gov/LATEST/search-index?q="unit sales"&ciks=0000320193`, run 2026-09-06.
**89 hits, first 2001-02-12, LAST 2019-10-31.** Complete tail of the hit list:

| date | form | accession |
|---|---|---|
| 2018-05-02 | 10-Q | 0000320193-18-000070 |
| 2018-08-01 | 10-Q | 0000320193-18-000100 |
| **2018-11-05** | **10-K (FY2018)** | **0000320193-18-000145** |
| 2019-01-30 | 10-Q | 0000320193-19-000010 |
| 2019-05-01 | 10-Q | 0000320193-19-000066 |
| 2019-07-31 | 10-Q | 0000320193-19-000076 |
| 2019-10-31 | 10-K (FY2019) | 0000320193-19-000119 |
| *(nothing after 2019-10-31)* | | |

The 2019 hits are **narrative only**. There is no unit-count table in any 2019 filing.

### 4.2 THE ANSWER

| | |
|---|---|
| **LAST document containing an actual unit COUNT** | **Form 10-K for FY2018, accession 0000320193-18-000145, filed 2018-11-05** (period 2018-09-29). Tables: "Unit Sales by Product:" plus three "Product Performance" tables for iPhone / iPad / Mac. |
| **LAST document of any kind with a unit count** *(two business days earlier)* | **Form 8-K filed 2018-11-01, accession 0000320193-18-000142, Exhibit 99.2**, captioned verbatim: *"Apple Inc. / Q4 2018 Unaudited Summary Data / (Units in thousands, Revenue in millions)"*. Q4 FY18 units: iPhone 46,889; iPad 9,699; Mac 5,299. **Rung note:** the 8-K body states *"The information contained in this Current Report shall not be deemed 'filed' for purposes of Section 18 of the Securities Exchange Act of 1934"*, so the data sheet is FURNISHED, not filed. The FY2018 10-K is therefore the last **filed** document with units. |
| **FIRST periodic report WITHOUT unit counts** | **Form 10-Q for Q1 FY2019, accession 0000320193-19-000010, filed 2019-01-30** (period 2018-12-29). |
| **FIRST earnings release without the unit data sheet** | **Form 8-K filed 2019-01-29, accession 0000320193-19-000007.** Its Item 9.01 exhibit list reads, in full: *"99.1 | Press release issued by Apple Inc. on January 29, 2019."* Exhibit 99.2, the data sheet, is simply gone. Compare the same list three months earlier (0000320193-18-000142): *"99.1 | Press release issued by Apple Inc. on November 1, 2018. / 99.2 | Data sheet issued by Apple Inc. on November 1, 2018."* |
| **FIRST 10-K without unit counts** | **Form 10-K for FY2019, accession 0000320193-19-000119, filed 2019-10-31.** |

**The withdrawal window is 2018-11-05 to 2019-01-30: 86 days.**

### 4.3 THE TRANSITION, QUOTED

Under the heading Apple used in FY2018, **"Product Performance"**, the FY2018 10-K reads
(0000320193-18-000145):

> *"The following table presents iPhone net sales and unit sales information for 2018 , 2017 and
> 2016 (dollars in millions and units in thousands):"*
> ... rows: `Net sales` / `Percentage of total net sales` / **`Unit sales`  217,722**

The Q1 FY2019 10-Q renames the heading to **"Products and Services Performance"** and the whole
section becomes (0000320193-19-000010, verbatim, in full):

> *"Beginning in the first quarter of 2019, the Company classified the amortization of the
> deferred value of Maps, Siri and free iCloud services, which are bundled in the sales price of
> iPhone, Mac, iPad and certain other products, in Services net sales. Historically, the Company
> classified the amortization of these amounts in Products net sales consistent with its
> management reporting framework. As a result, Products and Services net sales information for
> the first quarter of 2018 was reclassified to conform to the 2019 presentation.
> The following table shows net sales by category for the three months ended December 29, 2018
> and December 30, 2017 (dollars in millions):"*

followed by a five-row table (`iPhone`, `Mac`, `iPad`, `Wearables, Home and Accessories`,
`Services`) **with a revenue column only.** The per-product discussion is reduced to one
sentence each; the iPhone one reads:

> *"iPhone net sales decreased during the first quarter of 2019 compared to the same quarter in
> 2018 due to lower iPhone unit sales in all the reportable geographic segments."*

**Note the asymmetry.** In the same paragraph in which Apple stopped publishing units, it wrote
a full explanation of a *different* change, the Maps/Siri/iCloud reclassification. The removal of
the unit tables is **not mentioned at all.**

### 4.4 IS THE REASON IN A FILED DOCUMENT? RECORDED SWEEP, ZERO HITS

Searched, across the FY2018 10-K, the FY2019 10-K, the Q1/Q2/Q3 FY2019 10-Qs, the 2018-11-01 8-K
and both its exhibits, the 2019-01-02 8-K, and the 2019-01-29 8-K and its exhibit, for the terms:
`no longer`, `discontinu`, `will not`, `cease`, `change in disclosure`, `disclos`.

- `no longer`, **0 hits in all of: 10-K FY2018, 10-K FY2019, 10-Q Q1 FY2019, 10-Q Q2 FY2019,
  10-Q Q3 FY2019.**
- `disclos` in the 2018-11-01 press release (Ex 99.1), 1 hit, and it is *"Supplemental cash flow
  disclosure:"* in the cash-flow statement. Unrelated.
- The 2019-01-29 8-K body and its press release contain **no statement whatever** about the
  removal.

**FINDING: no filed or furnished SEC document from Apple states a reason for withdrawing unit
sales.** The company changed the disclosure silently in its periodic reports.

The reason publicly attributed to Apple was given by CFO Luca Maestri on the **Q4 FY2018 earnings
conference call, 2018-11-01**, which is a **TRANSCRIPT**, not an SEC document. **RUNG: unfiled
company statement (earnings call), the lowest rung used in this project.** Apple filed no 8-K
attaching or summarising that call: the 2018-11-01 8-K (0000320193-18-000142) has exactly two
exhibits, 99.1 (press release) and 99.2 (data sheet), and neither contains the explanation.
Because the standard here is VERBATIM ONLY from a named source on a stated rung, **no verbatim
reason is recorded in this file.** What is recordable on the filing rung is the *absence*: Apple
explained the accounting reclassification in the same paragraph and did not explain the metric
removal.

---

## 5. WHAT REPLACED IT: "ACTIVE INSTALLED BASE OF DEVICES", AND ITS RUNG

### 5.1 The rung test: is it in the 10-K?

`active devices` appears in the FY2018, FY2019, FY2020, FY2021, FY2022, FY2023, FY2024 and FY2025
10-Ks. **In every one of those vintages it is the same sentence, and it is about COMPETITORS**
(FY2018 10-K, 0000320193-18-000145, Item 1A Risk Factors, verbatim):

> *"In addition, some of the Company's competitors have broader product lines, lower-priced
> products and a larger installed base of active devices."*

The identical sentence appears in the Q1 FY2019 10-Q. The phrase `active installed base`, which
is what Apple calls its OWN metric, returns **ZERO hits in any Apple 10-K or 10-Q, all vintages,
on EDGAR full-text search**, and zero hits in the local text of all 14 downloaded 10-Ks.

> **Apple has never stated its own active-device count in a Form 10-K or Form 10-Q.**

### 5.2 Where it IS stated: 8-K Exhibit 99.1 press releases, furnished not filed

EDGAR FTS `"active installed base"` with `ciks=0000320193`: **13 hits, every one an 8-K exhibit.**
Every such 8-K carries the Item 2.02 legend *"shall not be deemed 'filed' for purposes of Section
18 of the Securities Exchange Act of 1934."*

### 5.3 THE ACTUAL SERIES: every number Apple has stated, verbatim, with rung

| Date | Filing / accession | Rung | Verbatim statement | Number |
|---|---|---|---|---|
| 2016-01-26 | 8-K 0001193125-16-438421, Ex 99.1 | furnished | *"our installed base recently crossed a major milestone of one billion active devices"* (Cook) | **1.0bn** |
| 2016-04-26 | 8-K 0001193125-16-556520, Ex 99.1 | furnished | *"our growing base of over one billion active devices"* (Cook) | >1.0bn |
| 2018-02-01 | 8-K 0000320193-18-000005, Ex 99.1 | furnished | headline *"Active Installed Base of Devices Reaches 1.3 Billion in January"*; body *"We've also achieved a significant milestone with our active installed base of devices reaching 1.3 billion in January. That's an increase of 30 percent in just two years"* | **1.3bn** |
| 2019-01-02 | 8-K 0000320193-19-000002, Ex 99.1 (Cook letter to investors) | furnished | *"Our installed base of active devices hit a new all-time high, growing by more than 100 million units in 12 months."* | +100m, no level |
| 2019-01-29 | 8-K 0000320193-19-000007, Ex 99.1 | furnished | *"Our active installed base of devices reached an all-time high of 1.4 billion in the first quarter, growing in each of our geographic segments."* | **1.4bn** |
| 2019-04-30 | 8-K 0000320193-19-000063, Ex 99.1 | furnished | *"the continued strength of our installed base of over 1.4 billion active devices"* | >1.4bn |
| 2020-01-28 | 8-K 0000320193-20-000008, Ex 99.1 | furnished | *"our active installed base of devices grew in each of our geographic segments and has now reached over 1.5 billion"* | **1.5bn** |
| 2020-04-30 · 2020-07-30 · 2020-10-29 · 2021-01-27 · 2021-04-28 · 2021-07-27 · 2021-10-28 · 2022-01-27 · 2022-04-28 · 2022-07-28 · 2022-10-27 | 8-K Ex 99.1, each quarter | furnished | *"all-time high"* / *"new all-time high"*, **NO NUMBER GIVEN** | none |
| 2023-02-02 | 8-K 0000320193-23-000005, Ex 99.1 | furnished | headline *"Installed base crosses 2 billion active devices"*; body *"we now have more than 2 billion active devices as part of our growing installed base"* | **2.0bn** |
| 2023-05-04 · 2023-08-03 · 2023-11-02 | 8-K Ex 99.1 | furnished | *"all-time high"*, **NO NUMBER** | none |
| 2024-02-01 | 8-K 0000320193-24-000005, Ex 99.1 | furnished | *"our installed base of active devices has now surpassed 2.2 billion, reaching an all-time high across all products and geographic segments"* | **2.2bn** |
| 2024-05-02 · 2024-08-01 · 2024-10-31 · 2025-01-30 · 2025-05-01 · 2025-07-31 · 2025-10-30 | 8-K Ex 99.1 | furnished | *"new all-time high"*, **NO NUMBER** | none |
| 2026-01-29 | 8-K 0000320193-26-000005, Ex 99.1 | furnished | *"our installed base now has more than 2.5 billion active devices"* | **2.5bn** |
| 2026-04-30 · 2026-07-30 | 8-K Ex 99.1 | furnished | *"new all-time high"*, **NO NUMBER** | none |

### 5.4 VERDICT ON THE REPLACEMENT METRIC

1. **It is not on the filing rung.** Zero appearances in any 10-K or 10-Q, 14 vintages swept.
   Every appearance is in an 8-K exhibit expressly not deemed filed under Section 18.
2. **It is not a series.** Seven rounded levels in eleven years (1.0 / 1.3 / 1.4 / 1.5 / 2.0 / 2.2
   / 2.5 billion), at irregular intervals, given only when a round number is crossed. Roughly
   thirty other quarters say *"all-time high"* with no figure at all. A yardstick quoted only
   when it reads well is not a yardstick.
3. **It is definitionally monotonic and undefined.** Sweep for a definition of "active device"
   across the 14 10-Ks and all 34 downloaded press releases: **zero definitional hits.** No
   measurement window, no counting rule, no auditor association. An unbounded cumulative-stock
   measure cannot fall the way a flow of units can. **The withdrawn metric could go down; the
   replacement metric, as constructed and as reported, essentially cannot.**
4. **Nothing replaced units inside the 10-K at all.** The FY2019 10-K substituted no physical
   measure whatsoever. What it added instead was the Products/Services **gross margin** split
   (see `segment_history.md`), which is a margin disclosure, not a volume one.

---

## 6. SUMMARY OF VERDICTS AND THE RECORDED ABSENCES

### 6.1 Verdicts

| test | reading | one-line basis |
|---|---|---|
| **[E4-55] physical series** | **FLAG** | Units existed and were monitorable through FY2018; iPhone units went 231.2m (FY15) to 217.7m (FY18), flat 0% in the final year, while iPhone revenue rose 18% on price alone. The physical series is now unobtainable from the filings for FY2019 onward. |
| **[E2-49] metric withdrawal** | **FLAG** | The yardstick was withdrawn 2018-11-05 to 2019-01-30, after three of three unit series had gone flat or negative, and no filed document states a reason. |
| replacement metric on the filing rung | **NO** | "Active installed base" appears in zero 10-Ks and zero 10-Qs; it exists only in 8-K Ex 99.1 press releases, expressly not deemed filed under Section 18. |
| **[E2-44] price vs volume attribution** | **absent from FY2024 onward** | Last volume attribution in any Apple 10-K is FY2023: *"lower Products volume."* Zero in FY2024 and FY2025. See `segment_history.md` §3. |

### 6.2 Recorded absences (searched zeros, not assumptions)

1. `ASP` across 14 10-K vintages FY2012-FY2025: **0 hits.**
2. `average selling price` as a disclosed figure across 14 vintages: **0 hits.** Only narrative use,
   which itself goes to 0 from FY2019.
3. `active installed base` in any Apple 10-K or 10-Q, EDGAR full-text search plus local text of
   all 14 downloaded 10-Ks: **0 hits.**
4. `no longer` / `discontinu` / `cease` / `change in disclosure` explaining the unit withdrawal,
   across the FY2018 10-K, FY2019 10-K, three FY2019 10-Qs, the 2018-11-01 8-K and both exhibits,
   the 2019-01-02 8-K, the 2019-01-29 8-K and its exhibit: **0 hits.**
5. A definition of "active device" (counting rule, measurement window) in any 10-K or in any of
   34 downloaded press releases: **0 hits.**
6. `unit sales` in any Apple SEC filing after 2019-10-31, EDGAR full-text search across all forms:
   **0 hits.**
7. `volume` used as a revenue or margin attribution in the FY2024 or FY2025 10-K: **0 hits**
   (the one `volume` in each is the stock-price-volatility risk factor).

### 6.3 Source manifest, everything relied on in these three files

All fetched from `https://www.sec.gov/Archives/edgar/data/320193/...` on 2026-09-06 with
user-agent `Chris Hrehor chrehor36@gmail.com`. Filing index from
`https://data.sec.gov/submissions/CIK0000320193.json` and `...-submissions-001.json`. Full-text
search from `https://efts.sec.gov/LATEST/search-index`.

**10-K, 14 vintages:** 0001193125-12-444068 · 0001193125-13-416534 · 0001193125-14-383437 ·
0001193125-15-356351 · 0001628280-16-020309 · 0000320193-17-000070 · 0000320193-18-000145 ·
0000320193-19-000119 · 0000320193-20-000096 · 0000320193-21-000105 · 0000320193-22-000108 ·
0000320193-23-000106 · 0000320193-24-000123 · 0000320193-25-000079

**10-Q:** 0000320193-18-000100 (Q3 FY18) · 0000320193-19-000010 (Q1 FY19) ·
0000320193-19-000066 (Q2 FY19) · 0000320193-19-000076 (Q3 FY19)

**8-K (all furnished under Item 2.02, not filed):** 0000320193-18-000005 (+Ex 99.2 data sheet) ·
0000320193-18-000067 (+Ex 99.2) · 0000320193-18-000098 (+Ex 99.2) · **0000320193-18-000142
(+Ex 99.1, +Ex 99.2, the last unit data sheet)** · 0000320193-19-000002 (Cook letter) ·
**0000320193-19-000007 (first release with no data sheet)** · 0000320193-19-000063 ·
0001193125-16-438421 · 0001193125-16-556520 · 0001628280-16-017762 · 0000320193-20-000008 ·
0000320193-20-000050 · 0000320193-20-000060 · 0000320193-20-000094 · 0000320193-21-000009 ·
0000320193-21-000055 · 0000320193-21-000063 · 0000320193-21-000104 · 0000320193-22-000006 ·
0000320193-22-000058 · 0000320193-22-000069 · 0000320193-22-000107 · 0000320193-23-000005 ·
0000320193-23-000063 · 0000320193-23-000075 · 0000320193-23-000104 · 0000320193-24-000005 ·
0000320193-24-000067 · 0000320193-24-000080 · 0000320193-24-000120 · 0000320193-25-000007 ·
0000320193-25-000055 · 0000320193-25-000071 · 0000320193-25-000077 · 0000320193-26-000005 ·
0000320193-26-000011 · 0000320193-26-000018

### 6.4 RUNG LADDER USED IN THESE FILES

| rung | what it covers here |
|---|---|
| **1. FILED** (10-K, 10-Q) | all unit counts through FY2018, all revenue and gross-margin figures, all MD&A attribution language |
| **2. FURNISHED** (8-K Ex 99.1/99.2, Item 2.02, "shall not be deemed filed") | quarterly unit data sheets through Q4 FY2018; **every** active-installed-base number Apple has ever stated |
| **3. UNFILED** (earnings-call transcript, press statement) | the only place a stated reason for the unit withdrawal exists. **Not quoted in these files**, per VERBATIM ONLY from a named source on a stated rung. |

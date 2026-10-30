# Company Run — Toyota Motor Corporation (TM, 7203.T) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

**Queue context.** First name in **WAVE 5** of `Screens/WATCHLIST RUN QUEUE.md` (the unpriced
watchlist businesses). The 2026-09-01 triage skipped it as *"foreign 20-F filer ... several still
return too few annual periods because their XBRL history is short, not because the business
is."* **Read here as UNLABELLED: a prompt to read the 20-F by hand, not a verdict.** The run
file was created before any fetch (write-early protocol). Research on disk:
`Test Runs/_research 2026-09-13 TM/`.

**Why the XBRL history is short, found rather than assumed.** Toyota reported under **US GAAP
through FY2020 (year ended 2020-03-31)** and moved to **IFRS from FY2021**, restating FY2020 as
the comparative. `companyfacts` therefore carries `ifrs-full` annual facts for **FY2020 to FY2025
only (six periods)**, and **the FY2026 20-F filed 2026-06-10 is not yet in `companyfacts` at all**
(`CashFlowsFromUsedInOperatingActivities` ends at 2025-03-31, checked 2026-09-13). The pre-2020
US GAAP history sits under a different namespace and a different basis. **So the screen saw six
stale periods; the filings hold ten years of the industrial/financial cash-flow split, in two
accounting bases, and this run reads all ten.**

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

### The earnings currency, established from the filing — and why the sovereign is the JGB

**The reporting currency is the yen** (¥ millions throughout; 20-F Note 2 basis: *"prepared in
accordance with IFRS Accounting Standards as issued by the IASB"*). **Most of the revenue is not
earned in Japan, and most of the booked operating profit is.** Both are filed, and both are stated:

| FY2026 (year ended 2026-03-31), ¥ millions | Japan | North America | Europe | Asia | Other | source |
|---|---|---|---|---|---|---|
| **Sales to external customers, by market** | 10,985,614 (**21.7%**) | 20,661,490 | 6,464,911 | 7,966,455 | 4,606,482 | 20-F Item 4.B table |
| **Sales revenues by location of external customers** | **7,942,616 (15.7%)** | 20,783,571 | 6,396,867 | 7,894,843 | 7,667,056 | 20-F Item 5.A, *"Sales Revenues by Location of External Customers"* |
| **Operating income, by location of the booking entity** | **2,321,038** | **(192,554)** | 357,743 | 869,826 | 328,966 | 20-F Item 5.A, geographic |
| same, FY2025 | **3,151,123** | 108,808 | 415,553 | 896,510 | 252,626 | 20-F Item 5.A |
| Vehicle units sold, FY2026 (000) | 2,082 (21.7%) | 2,934 (30.6%) | 1,183 | 1,759 | 1,637 | 20-F Item 4.B |

- **Two filed Japan revenue figures, and they differ:** the Item 4.B / Note 5(3) table (¥10,985,614M,
  21.7%) attributes revenue to the country of the selling entity; the Item 5.A table headed *"Sales
  Revenues by Location of External Customers"* gives ¥7,942,616M (15.7%). **By customer location,
  84.3% of FY2026 revenue came from outside Japan**; by selling entity, 78.3%. **And 63% of FY2026 regional operating
  income (2,321,038 of a 3,685,019 regional sum before eliminations) and 65% of FY2025's was booked
  by Japanese entities**, because Japan is the export base: *"For fiscal 2025 and 2026, exported
  vehicle unit sales were 1,941 thousand units and 2,001 thousand units, respectively"* (Item 5.A,
  Japan). North America **lost money at the booking-entity level in FY2026** (*"the impact of U.S.
  tariffs"*) while selling 30.6% of the units: the profit on a Camry built in Aichi and sold in
  Ohio is booked in yen in Japan.
- **The judgment, and its ground.** The sovereign enters as *"the currently observed rate for the
  currency the business earns in"* **[E4-15, E3-32]**. Toyota's cost base, its booked profit, its
  dividend, its buyback and its primary quote are all yen; its revenue is dominated by dollars.
  **The owner earnings are computed in yen and the cap is priced in yen, so the yen sovereign is the
  consistent pairing**, and mixing a USD sovereign into a yen yield would be the ATLKY currency
  defect inverted. **What the choice does NOT decide, stated so it cannot be leaned on later:** the
  [E4-28] floor of roughly 10% *"does not move with the sovereign"*, so the gap between the JGB
  (4.00%) and the US long bond (5.35%) moves only the points-over-sovereign display, never the
  quit-on line. The dollar exposure is carried into Q4 as a named risk (transaction exposure, and
  the North America segment already loss-making on tariffs), not into the rate **[E3-42]**.

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- **rate 3.995% (prints 4.00% through `tools/sources.py`) · tenor 30-year JGB · date 2026-09-10
  (latest row in the file; MOF posts the next business day, so 2026-09-11 is not yet published on
  2026-09-13) · source (issuing authority) Japan Ministry of Finance, official JGB curve,
  `https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv`, struck fresh
  2026-09-13 both through `sources.py` and by direct download** (saved as
  `_research 2026-09-13 TM/jgbcme.csv`). **The brief's 4.00% on 2026-09-10 is confirmed.**
- Rest of the long end the same day, for the record: 10Y 2.920% · 20Y 3.754% · **25Y 4.016%** ·
  30Y 3.995% · 40Y 4.003%. The curve is **flat-to-inverted beyond 25 years**; the 30-year is used
  because it is the tenor the tool and every prior run use, and the 25-to-40-year spread is 2bp,
  which changes nothing.
- Reference only (not used): USD 30-year **5.35%**, US Treasury daily par yield curve, 2026-09-11.
  EUR: `sources.py` failed on an SSL certificate error; not needed for this run.
- **FX: none required**, because the price is the **Tokyo quote in yen** and the earnings are yen.
- **ADR ratio, derived: 1 ADS = 10 common shares**, from the 20-F cover: *"Each American Depositary
  Share representing ten shares of the registrant's Common Stock."* **Checked against the quotes**:
  NYSE TM **$198.20** / 10 × USDJPY **153.554** = **¥3,043** per share, against the Tokyo close of
  **¥3,031** on the same date, a 0.4% gap explained by the two exchanges' different closing times.
  The ratio is confirmed; the ADR is not used for the cap.

### The share count, read by hand and walked forward (operator rule 4; `cover_shares.py` is blind to 6-Ks)

| date | count | what changed | document · accession |
|---|---|---|---|
| **2026-03-31** | **13,033,931,974 outstanding** | issued 15,794,987,460 less treasury 2,761,055,486; *"including 355,369,125 shares of common stock in the form of American Depositary Shares"* | **20-F cover**, 0001193125-26-264811 |
| 2026-03-31 | treasury **including** the ESOP trust: 2,761,602,986 | the note basis counts the 547,500 ESOP-trust shares as treasury; the cover basis does not | 20-F Note (equity) (2) |
| 2026-03-31 → 05-25 | **−1,192,330,962** | **self-tender at ¥3,067**, 2026-03-31 to 04-27, ¥3,656,879,060,454, settled 2026-05-25; **Toyota Industries tendered 1,192,330,920** and kept 1,242,720 after proration | 6-K 2026-04-28, 0001193125-26-183369 |
| 2026-06-30 | issued **14,594,987,460**; treasury incl. ESOP **2,753,153,800** ⇒ **11,841,833,660 outstanding** | 1,200,000,000 treasury shares retired 2026-06-30 (no change to outstanding); 634,900 restricted shares disposed 2026-06-30 | **Q1 FY2027 financial summary**, 6-K 2026-08-04, 0001193125-26-331392, Ex.99.1 (3) |
| 2026-08-05 → 08-31 | **−28,211,700** | open-market repurchase under the 2026-08-04 authority (up to 500M shares / ¥1,000bn to 2027-08-04), ¥86,494,175,900 | 6-K 2026-09-03, 0001193125-26-380869 |
| 2026-08-25 | ±0 on this basis | 1,154,400 treasury shares moved into the ESOP trust at ¥2,983.5; still treasury on the note basis | 6-K 2026-08-04 Ex.99.2; 6-K 2026-08-07, 0001193125-26-339003 |
| **2026-08-31** | **11,813,621,960 outstanding** | | walked by hand |

- **Basis used: the financial-statement basis, which treats ESOP-trust shares as treasury** (the
  Q1 FY2027 summary's own note). On the cover basis the count is higher by the trust's holding,
  about 1.7 million shares (547,500 at 2026-03-31 plus 1,154,400 added, less deliveries not
  disclosed): **0.01%, immaterial**, stated rather than chased.
- **Repurchases after 2026-08-31 are not yet disclosed** (the next monthly status notice falls in
  early October). At August's pace (28.2M shares in 19 trading days) the first nine trading days
  of September would retire roughly 13M more: **about 0.1% of the count, carried as a known
  unknown in the conservative direction** (the count used is slightly high, so the cap is
  slightly high and the yield slightly low).
- **Other share classes: NONE REMAIN.** Toyota issued **First Series Model AA Class Shares** on
  2015-07-24 (47,100,000 at 2017-03-31, 22,712,994 at 2021-03-31). *"Toyota completed the
  acquisition of all outstanding First Series Model AA Class Shares on April 2, 2021 and cancelled
  them on April 3, 2021"*, and the June 2021 AGM *"eliminate[d] the First Series Model AA Class
  Shares through the Fifth Series Model AA Class Shares as classes of Toyota's capital stock,
  effective June 16, 2021"* (20-F FY2022, Item 10.B). The FY2026 20-F contains the phrase zero
  times and states *"None of Toyota's shares of common stock entitles the holder to any
  preferential voting rights."*
- **Split history, for any per-share series used below:** a **5-for-1 split in October 2021** (the
  FY2021 cover reads 2,795,948,660 common; the FY2022 note reads 16,314,987,460 issued). Every
  per-share figure before FY2022 is multiplied by five before comparison.

### The price and the cap (aggregator for the live quote only, flagged)
- **Price ¥3,031** (Tokyo Stock Exchange close, **2026-09-11**, Yahoo Finance chart API, symbol
  7203.T; **aggregator, flagged**). Cross-check: ADR $198.20 (NYSE, same date) ⇒ ¥3,043.
- **Cap = ¥3,031 × 11,813,621,960 = ¥35,807bn (¥35.8 trillion).** In dollars at 153.554, about
  $233bn, **shown for orientation only and never used against yen earnings.**
- The market-cap rule in CLAUDE.md (`close × shares(measurement) × splits after measurement`) is
  satisfied trivially: no split after 2026-08-31.

### The filing was read — not tagged data **[E3-27, E4-14]**
- [x] MD&A (Item 5, including the three two-way Non-Financial / Financial Services statements)
  [x] cash-flow statement incl. detail lines [x] footnotes (segment note, equity, treasury stock,
  stock-based compensation, assets held for sale, quality-assurance liabilities, subsequent events)
- **Primary document: Form 20-F, fiscal year ended 2026-03-31, filed 2026-06-10, accession
  `0001193125-26-264811`, `d101983d20f.htm`, CIK 0001094517.** Auditor PricewaterhouseCoopers Japan
  LLC.
- Also read for the windows: 20-F FY2025 `0001193125-25-142326` · FY2024 `0001193125-24-167462` ·
  FY2023 `0001193125-23-179181` · FY2022 `0001193125-22-179197` · FY2021 (first IFRS)
  `0001193125-21-197902` · **US GAAP** FY2020 `0001193125-20-177015` · FY2019 `0001193125-19-178062`
  · FY2018 `0001193125-18-201591` · FY2017 `0001193125-17-211041`.
- 6-Ks read: every 6-K from 2025-03-03 to 2026-09-03 (49 filings including one 6-K/A; the list and texts are in the
  research folder), including the Q1 FY2027 financial summary (2026-08-04), the tender-offer
  notices (2025-06-03, 2025-10-06, 2026-01-14, 2026-03-06, 2026-03-30, 2026-04-28), the governance
  reports (2025-06-18, 2026-06-17) and the third and fourth certification recurrence-prevention
  progress reports (2025-05-30, 2025-09-09).
- **Figure cross-checked against the filed statement:** consolidated **net cash provided by
  operating activities ¥5,472,920 million** for FY2026, in the audited CONSOLIDATED STATEMENT OF
  CASH FLOWS, equals the MD&A's *"¥5,472.9 billion for fiscal 2026, compared with ¥3,696.9 billion
  for fiscal 2025"*; the FY2025 figure of **¥3,696,934 million** also matches `companyfacts`
  (`ifrs-full:CashFlowsFromUsedInOperatingActivities`, 2025-03-31) to the million.
- **A disclosure-location change, recorded because it bears on audit status:** through the FY2025
  20-F the three Non-Financial/Financial Services statements sat in the **notes to the
  consolidated financial statements** (FY2025 20-F: *"(iii) Consolidated Statement of Cash Flows on
  Non-Financial Services Businesses and Financial Services Business"* under NOTES); **in the FY2026
  20-F they sit in Item 5 MD&A.** The FY2025 figures are identical in both places (Non-FS operating
  cash 4,736,610 in each), so nothing was restated; the FY2026 split is simply presented outside
  the audited notes. Carried to Q3 as a prompt, not a flag.

### THE 2024 20-F/A — what it amended (the brief asked; opened and read)
**It was not one amendment but six, filed together on 2024-02-06**, one per fiscal year:
FY2016 `0001193125-24-024791`, FY2017 `-024795` (Amendment No. 3), FY2019 `-024798`, FY2020
`-024802`, FY2021 `-024808`, FY2023 `-024814` (Amendment No. 1). **All six amend the same single
item: the Iran sanctions disclosure under Exchange Act Section 13(r).** The FY2023 amendment's
explanatory note, verbatim: *"filed to disclose pursuant to Section 219 of the Iran Threat
Reduction and Syria Human Rights Act of 2012 additional information that Toyota Motor Corporation
became aware of after the Original Filing under 'Item 4.B — Business Overview — Disclosure of
Iranian Activities under Section 13(r) ...' Other than this additional compliance disclosure, no
part of the Original Filing is amended hereby."* The disclosed activity: *"Toyota Mobility Service
Co., Ltd. ... leased two vehicles to the Iranian embassy in Japan"* (FY2023); the FY2017 one:
*"Toyota Kirloskar Motor Private Limited ... sold one Toyota vehicle to the Iranian embassy in
India."* **No financial statement, share count or risk factor was amended. It is a late compliance
disclosure of immaterial transactions, found by the company and filed across six years at once**,
and it is weighed at Q3 as exactly that. (Earlier 20-F/As exist, filed 2017-10-23 and 2021-11-04
for other years; their subjects are not needed for any verdict and were not opened.)

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### Three businesses under one ticker, separated segment by segment from the filed note
**Source: 20-F FY2026 Note 5 (Segment information); Item 5 two-way statements; prior 20-Fs for the
series.** ¥ millions. Segment revenue includes inter-segment transfers.

| FY2026 | **Automotive** | **Financial services** | All other | Elim./unallocated | **Consolidated** |
|---|---|---|---|---|---|
| Revenue (total) | **45,417,703** | **4,857,115** | 1,651,412 | (1,241,278) | 50,684,952 |
| Operating income | **2,777,049** | **851,722** | 132,079 | 5,366 | 3,766,216 |
| Operating margin | **6.11%** | 17.5% | 8.0% | | 7.43% |
| Depreciation and amortization | 1,417,242 | 920,432 | 54,846 | — | 2,392,519 |
| Capital expenditures | 2,453,641 | **3,511,937** | 64,749 | 29,452 | 6,059,779 |
| Total assets | 33,182,372 | **53,741,709** | 4,066,133 | 14,532,118 | 105,522,331 |
| Equity-method investments | 4,763,577 | 124,393 | 304,242 | 150,336 | 5,342,548 |

**1. The vehicle business, in my own words.** Toyota builds about **9.6 million vehicles a year**
(9,595 thousand FY2026, including Daihatsu and Hino) and sells them to dealers and distributors it
does not consolidate. **Each vehicle brought ¥4.73 million of automotive revenue in FY2026
(45,417,703 ÷ 9,595) and left ¥289 thousand of segment operating profit, about $1,900 at 153.55.**
Costs are materials and parts bought from a supplier pyramid, labour concentrated in Japan (2,001
thousand of the 9,595 were exported from Japan), depreciation on plants and tooling, R&D, and the
warranty and recall accrual. **Margin is set by unit volume through the plants, model mix, the yen,
tariffs, and what has to be given back in incentives.** The filed decade:

| Automotive segment | FY17 | FY18 | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|---|---|---|---|
| Basis | US GAAP | US GAAP | US GAAP | IFRS | IFRS | IFRS | IFRS | IFRS | IFRS | IFRS |
| Revenue ¥bn | 25,082 | 26,398 | 27,079 | 26,800 | 24,652 | 28,606 | 33,820 | 41,266 | 43,200 | 45,418 |
| Operating income ¥bn | 1,693 | 2,011 | 2,039 | 2,013 | 1,607 | 2,284 | 2,181 | 4,621 | 3,940 | 2,777 |
| **Margin** | **6.75%** | **7.62%** | **7.53%** | **7.51%** | **6.52%** | **7.99%** | **6.45%** | **11.20%** | **9.12%** | **6.11%** |
| Units sold (000) | 8,971 | 8,964 | 8,977 | 8,959 | 7,646 | 8,230 | 8,822 | 9,443 | 9,362 | 9,595 |
| Revenue per unit ¥000 | 2,796 | 2,945 | 3,016 | 2,991 | 3,224 | 3,476 | 3,834 | 4,370 | 4,614 | 4,733 |

Sources: FY17-FY18 from 20-F FY2019 Item 5 segment table; FY19 and FY20 (US GAAP) from 20-F FY2020
Item 5; FY20 (IFRS restated) from 20-F FY2021 Note; FY21-FY23 from 20-F FY2023 Note; FY24-FY26 from
20-F FY2026 Note 5; units from each 20-F's *"consolidated vehicle unit sales by geographic market based
on location of customers"* table. **FY2020 appears on both bases (US GAAP 7.64% on 26,863,514 revenue;
IFRS 7.51% on 26,799,743); the IFRS figure is used in the series, and the 13bp basis gap is smaller
than any year-to-year move.**

**What the decade says, stated before any franchise question is asked:** units are **flat** (8.97M
to 9.60M, +0.7% a year, with a pandemic hole); revenue per unit rose **69%**, a mix of the weaker
yen and price/mix; the margin sits in a **6.1%-8.0% band in eight of ten years**; the two exceptions
are FY2024 (11.20%) and FY2025 (9.12%), and both had reversed by FY2026.

**2. The captive lender, in my own words.** Toyota Financial Services borrows in the bond and
commercial-paper markets (**¥40.9 trillion of Financial Services debt** at 2026-03-31: short-term
17,042,885 plus long-term 23,904,821, 20-F Item 5 two-way statement of financial position) and lends
it to Toyota buyers and dealers, or buys the car and leases it (**¥38,966.6 billion of finance
receivables, *"in North America 52.2%"***; ¥2,733,176M of equipment added to operating-lease fleets in
FY2026). It earns the spread between what it borrows at and lends at, less credit losses and
**residual-value losses on the lease book**. **¥53.7 trillion of segment assets on pre-tax income of
¥857bn: 1.6% on assets.** Its purpose, in the filing's own words: *"financing and vehicle leasing
operations to assist in the merchandising of Toyota's products."* **It is also the incentive
channel**: subsidised rates and supported residuals are how a manufacturer cuts price without
printing a lower sticker.

| Financial Services, pre-tax | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 | 7-yr sum |
|---|---|---|---|---|---|---|---|---|
| FS income before income taxes ¥bn | 285 | 493 | 657 | 433 | 572 | 673 | **857** | **3,969** |
| Non-FS income before income taxes ¥bn | 2,508 | 2,440 | 3,334 | 3,230 | 6,400 | 5,741 | 4,312 | 27,964 |
| **FS share of the two** | 10.2% | 16.8% | 16.5% | 11.8% | 8.2% | 10.5% | **16.6%** | **12.4%** |

Source: the two-way Consolidated Statement of Income in 20-F FY2022 (FY20-FY22), FY2024 (FY22-FY24),
FY2026 (FY25-FY26). **Unlike GM (89.9% of pre-tax from its finance arm in the GM run's latest year)
and Ford (the finance arm earned more than the whole group), Toyota's industrial business earns the
large majority of pre-tax profit in all seven years.** But the FS share **rises when the industrial
margin falls** (FY2021, FY2026): the lender stabilises reported profit, and that direction is
recorded for Q2.

**3. The investment holding, which the segment table hides.** The **Non-Financial Services**
income statement shows FY2026 operating income of **¥2,923,556M and "Other income (loss), net" of
¥1,387,992M** (FY2025: 4,118,908 and 1,622,539). **About a third of the industrial's pre-tax profit
is not from making cars**: the equity-method share of the group affiliates (¥542,072M non-FS,
FY2026), dividends received (¥424,816M, cash-flow line) and interest on a very large liquid position
(*"Liquid assets, which Toyota defines as cash and cash equivalents, time deposits, public and
corporate bonds and its investment in monetary trust funds were ¥22,117.9 billion as of March 31,
2026"*, Item 5). **This third business is being rearranged as the run is written** (Toyota
Industries taken private, ¥3.66 trillion of Toyota's own shares bought back from it, Hino
deconsolidated 2026-04-01), and that is read at Q3.

### The scarce input this business controls
**Not a single asset.** The candidates the filing names are the **Toyota Production System** (TPS,
*"which seeks to thoroughly eliminate waste and shorten lead times"*, Item 6), the **hybrid
powertrain at scale** (the line-up is classified *"largely into electrified vehicles and conventional
engine vehicles"*, Item 4.B), the **global dealer and distributor network**, and the **captive lender**
that lets it manage price through credit. **None is exclusive the way a trademark or a network is
exclusive**: every volume peer in the row has a production system, a dealer network and a captive lender (Tesla, which sells direct, is the exception on the last two), and hybrids
are sold by at least two filers in the row (Honda's 20-F: *"gasoline-electric hybrid systems and
gasoline-electric plug-in hybrid systems"*; Ford's 10-K: Ford Blue *"engineering iconic gas-powered and
hybrid vehicles"*). **Whether TPS amounts to a cost advantage "both wide and
sustainable" [E2-58] is a relative claim; it is Q2's question, answered from the competitor row,
not asserted here.**

### Will the fundamentals look broadly the same in ten years?
**The mechanism, yes; the product and the competitive set, less certainly, and the filing says so.**
Assembling vehicles from bought-in parts, selling them through dealers and financing them through a
captive lender has looked the same for the whole decade above. But the 20-F's first risk factor
reads: *"Toyota's ability to adequately respond to the recent rapid changes in the automotive market,
particularly shifts in consumer preferences to electrified vehicles, and to maintain its
competitiveness will be fundamental to its future success in existing and new markets and to
maintain its market share. There can be no assurances that Toyota will be able to compete
successfully in the future"*, and the stock-compensation note calls the period *"a once-in-a-century
transformation in the automotive industry."* **A business that describes its own industry that way
is not "relatively simple and stable in character" [E3-31] on the product axis**, and that is carried
forward by name to [E4-04] at Q2 and to the death list at Q4. **It does not fail Q1**, for the reason
it did not at GM and F: the question is whether I can understand how the money is made, and the
filing lays out the three businesses two-way, better than any US automaker does. **[E4-46]'s
five-minute test is passed**: the vehicle, lending and holding economics are each intelligible from
one filed table.

- **VERDICT: [x] IN.** The vehicle business (¥4.73M revenue and ¥289k operating profit per vehicle,
  on flat units and a margin in a 6-8% band in eight of ten years), the captive lender (¥53.7 trillion of assets earning 1.6%
  pre-tax, 12.4% of seven-year pre-tax profit) and the investment holding (about a third of the
  industrial's pre-tax income) are each understood from the filed statements, and **Toyota
  publishes the industrial/financial separation in all three statements**, the disclosure the GM
  and F runs had to reconstruct. **The ten-year product-transition risk is carried to Q2 and Q4 by
  name; it is not used to pass or fail this gate.**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The question the brief put, stated as a hypothesis to refute rather than a verdict:** GM and F both
failed here on excess-capacity language. **Does Toyota's filed cost and margin record differ?** If
Toyota has what the corpus calls *"a cost advantage that is both wide and sustainable"* **[E2-58]**,
it is the one automaker for which the commodity doctrine's exception could hold, and the run must
find it if it is there **[E4-26]**. The evidence is taken in this order: Toyota's own words, Toyota's
own ten-year causal bridge, Toyota's own returns, and then the competitor row.

### [E3-03], the three criteria, in the filing's own words

- **Needed or desired — [x] YES.** 9,595 thousand vehicles sold in FY2026 into roughly *"92 million
  units in 2025"* of world sales (Item 4.B, Toyota's own estimate).
- **No close substitute — [ ] FAILS, on Toyota's own risk factor, and in the same vocabulary as GM's
  and Ford's.** Item 3.D, first risk factor, verbatim: *"The worldwide automotive market is highly
  competitive. Toyota faces intense competition from automotive manufacturers in the markets in which
  it operates. In recent years, competition in the automotive industry has further intensified amidst
  difficult overall market conditions ... Factors affecting competition include product quality and
  features, safety, reliability, fuel economy, the amount of time required for innovation and
  development, pricing, customer service, financing terms and tax credits or other government policies
  in various countries. Increased competition may lead to lower vehicle unit sales, which may result in
  a further downward price pressure."* **And the over-capacity premise is Toyota's own**, Item 4.B:
  industry alliances exist because of *"the need to address excessive global capacity in the production
  of automobiles."* A customer choosing on *"reliability, fuel economy ... pricing ... financing
  terms"* is choosing among substitutes; that is what the sentence says. **Reliability is named as a
  factor of competition, which is the strongest thing the filing says for Toyota, and it is named as
  one factor among nine, not as a reason the customer has no alternative.**
- **Not subject to price regulation — [x] PASSES**, read through **[E2-59]** as at GM and F: no
  authority sets Toyota's transaction prices, but its costs are administered, and in FY2026 the
  administration ran against it: **U.S. tariffs cost ¥1,380.0 billion of operating income** (Item 5.A:
  *"The aggregate unfavorable impact of changes in expenses and expense reduction efforts includes the
  ¥1,380.0 billion impact of U.S. tariffs"*), **37% of the year's consolidated operating income of
  ¥3,766.2 billion.** Regulation neither caps nor floors this business; it taxes it.

### THE TEST THE BRIEF ASKED FOR: Toyota's own ten-year causal bridge **[E2-58], [E3-62]**
Toyota's filings carry something the GM and F runs did not have at the consolidated level for a
decade: **every 20-F attributes the year's change in consolidated
operating income to five named causes, including a line headed "Effect of cost reduction efforts."**
Ten consecutive years are filed. If Toyota's production system is a wide and sustainable cost
advantage, **this is the line where it must show, and [E3-62]'s second step is the question to ask of
it: *"how much is going to stay home and how much is just going to flow through to the customer."***

| Consolidated OI bridge, ¥bn | Marketing efforts | **Cost reduction efforts** | Exchange rates | Expenses / misc. costs | Other | **Total change** | source (20-F, Item 5.A) |
|---|---|---|---|---|---|---|---|
| FY2017 v FY2016 | +210 | **+440** | −940 | −530 | −39.6 | −859.6 | FY2017, US GAAP |
| FY2018 v FY2017 | −100 | **+165** | +265 | +60 | +15.5 | +405.5 | FY2018, US GAAP |
| FY2019 v FY2018 | +275 | **+80** | −50 | −165 | −72.3 | +67.7 | FY2019, US GAAP |
| FY2020 v FY2019 | −90 | **+170** | −305 | +45 | +155.3 | −24.7 | FY2020, US GAAP |
| FY2021 v FY2020 | −210 | **+150** | −255 | +70 | +43.5 | −201.5 | FY2021, IFRS |
| FY2022 v FY2021 | +860 | **−360** | +610 | −220 | −92.1 | +797.9 | FY2022 |
| FY2023 v FY2022 | +680 | **−1,290** | +1,280 | −525 | −415.7 | −270.7 | FY2023 |
| FY2024 v FY2023 | +2,000 | **+120** | +685 | −380 | +202.9 | +2,627.9 | FY2024 |
| FY2025 v FY2024 | +145 | **0** | +590 | −990 | −302.3 | −557.3 | FY2025 |
| FY2026 v FY2025 | +710 | **−120** | −195 | −2,030 | +605.7 | −1,029.3 | FY2026 |
| **TEN-YEAR SUM** | **+4,480** | **−645** | **+1,685** | **−4,665** | +100.9 | **+955.9** | |

*Reconciliation: FY2016 operating income ¥2,853.9bn (FY2017's ¥1,994.3bn plus the ¥859.6bn decline)
to FY2026 ¥3,766.2bn is +¥912.3bn; the bridge sums to +¥955.9bn; the ¥43.6bn gap is exactly the
FY2020 restatement from US GAAP (¥2,442.8bn) to IFRS (¥2,399.2bn). The table ties.*

**What the line means, from the filings' own definitions.** From FY2022 the line is described as
*"factors categorized as cost reduction efforts (including fluctuations in raw materials prices)"*,
and the gross engineering savings are stated beside it: FY2023, *"a ¥1,545.0 billion increase in
operating costs and expenses attributable to the impact of soaring materials prices"* against
continued value-engineering reductions; FY2024, *"a ¥265.0 billion reduction principally attributable
to value engineering activities"*; FY2025, *"a ¥240.0 billion reduction principally attributable to
value engineering activities and other cost reduction efforts concerning design-related costs"*, which
netted to **¥0.0bn**.

**THE READING, and it answers the brief's question directly.**
1. **The production system produces gross savings every year, ¥240-265 billion in each year the filing
   states the gross figure (FY2022, FY2024, FY2025).** That is real, filed, and it is the strongest fact in Toyota's favour.
2. **Net of input costs, the line summed to MINUS ¥645 billion over ten years.** Every yen the system
   saved in the decade, and ¥645bn more, was absorbed by materials and parts inflation. **A cost
   advantage that is wide shows up as operating income that stays home; this one did not stay home.**
3. **The whole decade's operating-income growth is smaller than the currency.** OI rose ¥912bn;
   **exchange rates alone contributed +¥1,685bn.** On the bridge's own attribution, without the
   currency line consolidated operating income would be **lower** than FY2016's (+912 − 1,685 = −773). **That is [E4-41]'s luck,
   named: a favourable exogenous break carried the level.**
4. **Price and volume ("marketing efforts", +¥4,480bn) were almost exactly consumed by expenses
   (−¥4,665bn).** In FY2026 the expense line includes the tariff; in earlier years the filings name
   labour, R&D, depreciation and quality costs. **[E3-62]'s second step, answered from Toyota's own
   attribution: the gains did not stick to the owners' ribs. The filing's own attribution sends them to
   input costs, expenses and the tariff.**
5. **The company says the same thing in words.** Item 4.B, FY2026: *"we have recently seen a
   significant rise in our break-even volume due to a combination of increases in investments in
   human resources and future-oriented investments and the impact of U.S. tariffs."* **A franchise's
   break-even does not rise with its costs; a price-taker's does.**

### [E2-44], the two-characteristic test

**(1) Can it raise prices *"even when product demand is flat and capacity is not fully utilized"*?**
The filed record does not isolate the condition cleanly (units rose 2.5% in FY2026), but the pieces
that are isolated say **price was raised and did not hold the margin.** FY2026: *"the ¥335.0 billion
impact of other marketing efforts such as price revisions"* and a further ¥210.0bn from volume and
mix, against the ¥1,380.0bn tariff and a total expense line of −¥2,030.0bn; the automotive margin fell
**9.12% to 6.11%**. FY2025, a year of flat-to-falling units (9,443k to 9,362k): marketing efforts
contributed **+¥145bn** against −¥990bn of expenses; margin **11.20% to 9.12%**. **Price rises were
available; they were an order of magnitude smaller than the cost the business had to absorb.**
**FAILS, on the direction of every year the condition approximately holds.**

**(2) Can it grow dollar volume *"with only minor additional investment of capital"*? No.**
| Automotive segment, Note 5 | FY2020 | FY2026 | change |
|---|---|---|---|
| Revenue ¥bn | 26,800 | 45,418 | **+69%** |
| Operating income ¥bn | 2,013 | 2,777 | +38% |
| Segment assets ¥bn | 19,450 | 33,182 | **+71%** |
| Segment assets excl. equity-method investments ¥bn | 15,640 | 28,419 | **+82%** |
| Capex / D&A (automotive) | 1.75x | 1.73x | never below 1.39x in seven years |
| Units (000) | 8,959 | 9,595 | +7% |

Revenue grew with assets, not ahead of them, and operating income grew at about half the rate of
the capital employed. **The incremental pre-tax return on the ¥12.8 trillion of added operating
segment assets (excluding equity-method stakes) FY2020 to FY2026 was ¥764bn ÷ ¥12,779bn = 6.0%**;
measured to FY2025 instead (¥1,927bn ÷ ¥9,276bn) it was 20.8%. **The end-date moves it by a factor of
three [E4-38]**, which is itself the finding: **the return on added capital is set by the cycle, not
by the business.**

### [E3-46] / [E2-43] — the second question about the business, as a number
Pre-tax operating return on automotive segment assets excluding equity-method investments (Note 5;
the *"unleveraged"* denominator the corpus prescribes; corporate cash is already outside segment
assets per the note): **FY20 12.9% · FY21 9.1% · FY22 11.4% · FY23 10.1% · FY24 19.1% · FY25 15.8% ·
FY26 9.8%. Seven-year mean 12.6%.** Respectable, above any bank-deposit rate, and **the two years above
15% are the supply-tight, weak-yen years FY2024-FY2025**; the five ordinary years average **10.7%**.
On equity (Q3's [E2-01] series below), a seven-year mean of about **11.5%**. **This is a well-run
business earning a moderate return in a cyclical industry, and the number does not describe the
"very high returns on capital employed over time" [E3-46] of a franchise.**

### [E4-04] — must the moat be continuously rebuilt? **Yes, and the filing measures it.**
- **Automotive capex has exceeded automotive depreciation in every one of the seven IFRS years**
  (1.75 · 1.50 · 1.39 · 1.40 · 1.59 · 1.59 · 1.73, Note 5), and industrial net capex has exceeded
  industrial D&A in **all ten years** of the two-way cash-flow statements (10-year mean **1.53x**, low
  1.28x FY2018), **on flat units.** The spending does not buy volume; it buys the next model cycle, the
  battery, the plant localisation the tariff now requires.
- **The replacement purchase is visible and partly failed**: 20-F Note 36 (subsequent events): *"TMC
  has decided in late May 2026, in light of the surrounding environment, to discontinue the development
  of LF-ZC ... it is not possible at this time to reasonably estimate such impact ... including potential
  costs such as compensation to business partners."* Honda wrote off ≈¥1.58 trillion of EV programmes
  in the same fiscal year (GM run research, Honda 20-F FY2026 Note (4)(d)). **The framework's scope
  test is "does the spending defend the same advantage, or buy its replacement?" The powertrain
  transition is a replacement purchase by definition, and Toyota's own note calls the period "a
  once-in-a-century transformation."**
- **Depreciation itself was lowered by an accounting choice**: 20-F FY2020, *"Toyota changed the
  depreciation method of the parent company and Japanese subsidiaries to the straight-line method,
  effective as of April 1, 2019. The impact of this change for fiscal 2020 was a decrease in
  depreciation expense of ¥173.2 billion, which positively impacted operating income but not net cash
  provided by operating activities."* Recorded here as evidence for [E5-20] at Q4, and as a
  metric-switch that was **announced with reasons** (the [E2-49] candour case, not the fired flag).

### The remaining Q2 tests
- **[E4-32] direction** — automotive margin **11.20% → 9.12% → 6.11%** over FY2024-FY2026; the
  company's own break-even *"significant rise"*; the finance arm's share of pre-tax income **8.2% →
  10.5% → 16.6%** over the same three years. **NARROWING**, on every observable the filing gives.
- **[E4-55] units** — the physical series is flat for a decade: **8,971k (FY2017) to 9,595k (FY2026),
  +0.7% a year**; Asia fell 1,838k to 1,759k in FY2026. Revenue per unit rose 69%; the units did not.
- **[E2-53] dominance** — no. About **10%** of world unit sales on Toyota's own denominator (9,595k of
  ~92 million), the largest single manufacturer and not a position that sets its own economics:
  North America, 30.6% of its units, **lost ¥192.6bn at the booking-entity level in FY2026.**
- **[E3-33] / [E5-28] untapped pricing power** — not claimed; claiming it means claiming *"a monopoly
  or a near monopoly."*
- **[E2-45] attacker's test** — the attack is in the filing: tariffs of ¥1,380bn a year on the
  export model from outside, and the risk factor's CASE competitors *"possibly resulting in industry
  reorganizations"* from inside. The ¥240-265bn of annual gross savings is the defence, and the bridge
  shows what it bought: a flat decade ex-currency.
- **[E4-36] which cause of success** — the one Toyota's record supports is **extreme performance over
  many factors** (quality, cost discipline, reliability, the hybrid): the cause the corpus lists, and
  the one the filed bridge shows is continuously competed for rather than owned.
- **[E4-23] key-person dependence** — **LOW, recorded in the business's favour**: no filing ties the
  vehicle business to a person. (The Chairman is central to the group reorganisation; that is Q3.)

### THE COMPETITOR ROW — required [E3-28]. Same metric, same window, filing-sourced.

**Built for this run** (`_research 2026-09-13 TM/peers/COMPETITOR ROW - five-year industrial
margins.md`, every figure with document, date and accession; two figures re-checked by hand against
the filed text: Honda FY2024 automobile segment profit ¥560,649M in the FY2024 20-F, and Stellantis
2023 segment AOI summing to €25,332M across its six segments in the FY2025 20-F). **Window: the
five latest fiscal years**, aligned so Toyota's and Honda's March year-ends sit beside the calendar
year that ends inside them (Toyota FY2026 = April 2025-March 2026, beside calendar 2025).

**THE METRIC PROBLEM, STATED BEFORE THE TABLE, because it decides how the row reads.** Toyota's
automotive segment measure is **IFRS operating income with every charge in it** (the ¥1,380bn tariff,
the ¥845bn of recall provisions). GM's segment measure is **EBIT-adjusted** (excludes, e.g., $8,709M of
GMNA "Adjustments" in 2025) and Stellantis's is **AOI** (excluded €25.4bn in 2025). **Comparing
Toyota's all-in number with their adjusted numbers flatters the peers.** So the row carries two lines:
each company's own segment measure, and the nearest **all-charges-in** figure each filing provides.

| Automotive margin, % | FY22 / CY21 | FY23 / CY22 | FY24 / CY23 | FY25 / CY24 | FY26 / CY25 | **5-yr pooled** | measure · source |
|---|---|---|---|---|---|---|---|
| **TOYOTA** automotive | **7.99** | **6.45** | **11.20** | **9.12** | **6.11** | **8.22** | IFRS segment operating income · 20-F Note 5 |
| GM (GMNA+GMI) | 9.82 | 9.83 | 8.59 | 8.65 | 6.67 | 8.60 | **EBIT-adjusted (non-GAAP)** · 10-K Note 23 |
| GM consolidated | 7.34 | 6.58 | 5.41 | 6.82 | 1.57 | 5.39 | GAAP operating income, **includes GM Financial** · 10-K |
| Ford (Blue+Model e+Pro) | 4.02 | 5.33 | 5.96 | 5.31 | 2.91 | 4.71 | segment EBIT (non-GAAP) · 10-K |
| Ford consolidated | 3.32 | 3.97 | 3.10 | 2.82 | (4.90) | 1.46 | GAAP operating income · 10-K |
| Honda automobile | 2.52 | (0.15) | 4.07 | 1.69 | **(9.96)** | (0.62) | IFRS segment profit · 20-F |
| *Honda motorcycle (memo)* | *14.25* | *16.80* | *17.27* | *18.29* | *18.21* | | *IFRS segment profit · 20-F* |
| Stellantis (six vehicle segments) | 12.54 | 13.67 | 13.65 | 5.90 | 0.49 | 9.61 | **AOI (non-GAAP)**; IFRS operating margin 2025 (17.1), 2024 2.4 · 20-F |
| Tesla automotive | 26.91 | 26.52 | 18.21 | 16.91 | 16.20 | | segment **gross** margin · 10-K |
| Tesla consolidated | 12.12 | 16.76 | 9.19 | 7.24 | 4.59 | 9.54 | GAAP income from operations (includes energy) · 10-K |
| Volkswagen Automotive Division | 6.4 | 7.1 | 7.0 | 5.6 | 1.8 | ≈5.6 (mean) | IFRS operating return on sales · Annual Report 2025, p.117 and p.667 (2021-23 company-stated ratios only) |
| Hyundai vehicle segment | n/o | n/o | n/o | 8.10 | 5.05 | | K-IFRS operating profit on external sales · 2025 audited statements, Note 37 |
| BYD | **blocked** | | | | | | IR site HTTP 504; the HKEX link found was Q1 2026, not the annual report |

| Other same-window facts | Toyota | GM | Ford | Honda | Stellantis | Tesla | VW |
|---|---|---|---|---|---|---|---|
| Units, latest vs five years earlier | 9,595k vs 8,230k (FY22) | 3,799k vs 2,859k wholesale | 4,394k vs 3,942k | 2,711k vs 2,424k autos | 5,484k vs 5,836k shipments | ~1.64m vs 936k | 9,022k vs 8,576k (Group) |
| Finance share of pre-tax, latest | **16.6%** | **89.9%** (GMF non-GAAP) | n/m (group loss) | n/m (group loss) | not disclosed | none | **35.9%** |
| Own words on capacity / pricing | *"excessive global capacity"* | *"excess capacity and high fixed costs"* | *"pricing pressure resulting from industry excess capacity"* | *"intensifying competition due to the rise of emerging Chinese EV companies"* | *"intense price competition resulting from ... excess global manufacturing capacity"* | (risk factors, competition) | *"Excess capacity in global automotive production ... increased pricing pressure"* |

- **Peers taken: 8 of the industry's at-scale competitors named in the brief** (GM, Ford, VW,
  Hyundai, Honda, Stellantis, BYD, Tesla): **five complete from SEC filings, VW on five years of
  company-stated ratios, Hyundai on two years, BYD blocked.** Per the framework, the gaps hold the
  class **PROVISIONAL for any upgrade**; they cannot create a moat the present row does not show,
  and the verdict below does not rest on them. **The row's limit [E3-61]:** it shows position, not
  conduct; *"I think you'd have to know the people involved."*
- **VW, Hyundai and BYD are not SEC registrants.** VW and Hyundai were read on rung 3 of the evidence
  ladder (company IR site, English), which the F run's precedent treated as unavailable; **BYD's rung 3
  failed on the obstacle recorded above. Can I name the document? Yes: BYD's 2025 annual report on
  HKEXnews.** It is a work order for any future upgrade, not for this verdict.

**WHAT THE ROW ESTABLISHES — and it answers the brief's question in both directions.**
1. **Toyota's filed margin record DOES differ from GM's and Ford's, and the difference must be said
   first [E4-26].** On an all-charges-in basis Toyota's automotive margin is **the highest in the row
   in each of the last three fiscal years** (11.20 vs Tesla 9.19; 9.12 vs Tesla 7.24; 6.11 vs Tesla
   4.59), and its five-year pooled 8.22% is **above every volume manufacturer's comparable figure**
   (GM 5.39% even with GM Financial inside it; VW ≈5.6%; Ford 1.46%; Honda automobile −0.62%), below
   only Tesla's 9.54%. **GM and Ford failed Q2 at the bottom of this row; Toyota sits at the top of the
   volume half of it.** This is the single strongest fact against the verdict below, and it is not
   dismissed.
2. **But the lead is not wide.** On the peers' own adjusted measures GM (8.60%) and Stellantis (9.61%)
   **beat** Toyota's all-in 8.22% over the same five years, and in the two supply-tight years (CY2021-22)
   Toyota was fourth or fifth of seven on the segment-measure line. **The width is roughly the charges
   the peers exclude**, and the charges Toyota avoided were the EV write-offs (Honda ≈¥1.58tn, Ford
   $13.8bn, Stellantis €9.1bn plus €6.6bn, GM $2.6bn impairment in the GM run's row). **Its lead in
   FY2025-FY2026 is the lead of the company that did not buy the replacement, not of the company whose
   cost of producing the same vehicle is lowest**, and the LF-ZC cancellation (Note 36) shows the
   replacement bill is not avoided, only later and smaller.
3. **And it is not sustainable on Toyota's own evidence.** The margin that leads the row fell from
   11.20% to 6.11% in two years; the company's own cost-reduction line summed to −¥645bn over ten
   years; the decade's operating-income growth was the currency's. **A cost advantage that is wide and
   sustainable [E2-58] would show up as a margin that holds while everyone else's falls. Toyota's fell
   by five points while leading.**
4. **Every filer in the row, including Toyota, names excess capacity or price competition in its own
   risk factors.** All seven filers with a five-year line (on the all-charges-in line where one exists) were lower in the
   latest year than five years earlier, Toyota included (7.99 → 6.11).
5. **Toyota is among the least finance-dependent of the captive-finance filers** (16.6% of pre-tax
   against GM's 89.9%, VW's 35.9% and Honda's 16.7-32.5% in FY2022-FY2025; Hyundai's mixed-basis 15.6% for
   2025 is the one lower figure): **the industrial business carries its own weight**, which is a real
   difference from GM and F and is recorded in its favour.

### THE FAIR COUNTER-CASE, stated as its best advocate would state it [E4-51]
*"I'm not entitled to have an opinion unless I can state the arguments against my position better
than the people who are in opposition."* **Toyota is the best volume car company in the world on
the filed numbers.** It leads every volume peer on all-in automotive margin over five years and in
each of the last three; its industrial business, not its lender, earns the profit; it did not write
off a BEV programme while Honda, Ford, Stellantis and GM wrote off tens of billions between them; its
production system saves ¥240-265bn a year in filed value engineering; its industrial balance sheet
carried ¥10 trillion of net cash at the year end; and it has sold 7.6 to 9.6 million vehicles a year for
a decade through a pandemic, a chip shortage and a tariff shock. **In an industry where the median company
destroys capital, the one that reliably earns 8-10% on its operating assets is a franchise of
competence, and a price-taker's doctrine misclassifies it.**

**What defeats it is the corpus's own definition, not a number.** The corpus does not ask whether
a business is the best in its industry; it asks whether customers believe it has *"no close
substitute"* **[E3-03]**, whether it can price *"even when product demand is flat"* **[E2-44]**, and
whether its advantage is *"wide and sustainable"* in a class where *"such exceptions are few"*
**[E2-58]**. Toyota's own risk factor lists nine factors of competition and says increased competition
*"may result in a further downward price pressure"*; its own bridge says the savings did not stay
home; its own margin fell five points in two years while leading; its own words say break-even
volume has risen significantly. **[E2-37] is the sentence for it: *"a textile company that allocates
capital brilliantly within its industry is a remarkable textile company — but not a remarkable
business."*** Toyota is a remarkable car company.

- **Class: [x] NONE** (a relative leader without a franchise; PROVISIONAL only for an upgrade, on the
  BYD, Hyundai and VW gaps) · **Direction: NARROWING** (automotive margin 11.20 → 9.12 → 6.11; break-even
  *"significant rise"*; tariffs ¥1,380bn; finance share of pre-tax 8.2% → 16.6%).
- **VERDICT: [x] OUT.** **[E3-03] criterion 2 fails on Toyota's own risk factor**, in the same
  excess-capacity vocabulary as GM and Ford. **[E2-58]'s exception is tested, not assumed, and it is
  not met**: the competitor row shows Toyota's record **does** differ from GM's and Ford's (it leads
  the volume half of the row on all-in margin), but the lead is **not wide** (inside the peers'
  excluded charges and behind GM and Stellantis on their own measures) and **not sustainable** (its
  own ten-year cost-reduction line is net negative; the margin halved in two years). **[E2-44] fails
  both limbs; [E4-04] excludes the class (capex above depreciation for ten years on flat units, a
  powertrain replacement under way); [E4-32] reads narrowing.** The best business in an industry
  without franchises is not thereby a franchise. **The entry run stops here [E5-13].**

---
⛔ **Q2 IS OUT. THE HARD SEQUENCE CLOSES THE FILE FOR ANY BUY DECISION.** Everything below is **FOR
THE RECORD**: the brief asked for the certification matters, the group reorganisation, the industrial
owner earnings over every window and both (c) ends, the named way it dies, and a price. **Q3 and Q4
are RECORDED, NOT GOVERNING; Q5 and Q6 carry operator rule 3's heading, COMPUTATION — NOT A
CLEARANCE, and no entry language.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — **RECORDED, NOT GOVERNING**
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`.* **Q2 is OUT; the hard sequence has
already closed the file. Nothing in this section can promote the name or reopen Q2 [E2-37, E2-38,
E3-39].** It is recorded because the brief asked for the certification matters, the cross-holdings,
the group reorganisation, the buybacks, pay and guidance, and because a reopening condition at Q6
needs the conduct record on file.

### STEP 1 — THE WEIGHT CASE, declared first
- [x] **Daily execution [E3-38, E2-70]** — a vehicle maker is smart-every-day: one design or test
  lapse surfaces years later as a recall or a certification order. FY2026 **additions to recall
  liabilities were ¥844,899M against ¥317,414M the year before** (Note 24 sub-table, *"Liabilities
  for recalls and other safety measures"*), and the certification matters below are exactly this
  failure class.
- [ ] **Control [E1-16]** — no; a public minority holding.
- [x] **Leverage [E3-29]** — the Financial Services balance sheet: **¥53,741,709M of assets on
  ¥6,644,162M of equity (assets less liabilities in the two-way statement), 8.1 to 1**; consolidated
  *"total interest-bearing debt was 108.2% of Toyota Motor Corporation shareholders' equity"* (Item 5.B).
  A 10% loss on FS assets would be ¥5.4 trillion, **13.5% of TMC equity.**
- **Case declared: BINARY GATE** (two of three). No price would compensate for an integrity finding.

### Honesty — the binary [E5-16], each matter dated to when it became PUBLIC
| public | matter | what the filing says (verbatim where quoted) | acted when learned? [E5-22] |
|---|---|---|---|
| 2020-04 | Thai subsidiary | *"In April 2020, Toyota reported possible anti-bribery violations related to a Thai subsidiary to the SEC and the U.S. Department of Justice ... In June 2025, the DOJ and SEC informed Toyota that they had closed their investigations"* | self-reported; closed without action disclosed |
| 2022-03-04 | **Hino** (66.16% voting, deconsolidated 2026-04-01) | *"identified past misconduct in relation to its applications for certification concerning the emissions and the fuel economy performance of certain of its engines"*; MLIT revoked type approvals; **US criminal resolution with the DOJ reached 2025-01-16, effective 2025-03-19**, civil resolution effective 2025-05-21: *"Hino agreed to the payment of criminal and civil penalties."* **The 20-F does not state the amount.** | Hino self-investigated; the amount's absence from TMC's filing is a candour prompt [E2-26], and penalty size is not seriousness in either direction [E5-22] |
| 2023-04 | **Daihatsu** (consolidated subsidiary) | *"announced vehicle model certification issues"*; Independent Third-Party Committee report December 2023 | Toyota placed *"more than 50 Toyota members"* in the workplaces |
| by 2024-06-25 (FY2024 20-F) | **Toyota Industries** (then 24.66% held) | named with Daihatsu and Hino in the FY2024 20-F's common-root-cause passage | as above |
| 2024-05-31 (MLIT instruction 2024-01-26) | **TMC itself** | *"confirmed that since 2014 seven models ... were tested ... using methods that differed from government standards"*; correction order July 2024; *"the MLIT indicated eight new cases involving seven vehicles that did not comply with the standards"*; recurrence-prevention reports (third 2025-05-30, fourth 2025-09-09) | **investigated on the regulator's instruction, not before it**; the MLIT's on-site work found more than the company's own review |
| 2024-02-06 | Iran §13(r) | six 20-F/As disclosing embassy vehicle leases/sales found after the original filings (Step 0) | late but volunteered; immaterial |

**The filing's own root-cause statement (20-F FY2024, Item 4.B), which is the most important sentence
in this section:** *"The root cause common to the irregularities at these three companies was a
disconnect between management and the genba (frontlines). Excessive pressure placed on workplaces led
to a lack of leeway and stifled communication, resulting in a weakened awareness of legal compliance
and irregularities becoming routine. Management failed to grasp the reality of workplaces and did not
change the environments that gave rise to irregularities. The management teams were responsible for
what happened."*

**The read.** [E4-22]'s first flag, *"There is seldom just one cockroach in the kitchen"*, **fires at
full strength**: certification testing failed at **four** group companies (Hino, Daihatsu, Toyota
Industries, TMC) across a decade of model years, and at TMC the regulator found more than the company
did. **Against that, three facts, all filed:** (i) no filing attributes the conduct to personal
dishonesty by TMC's directors; the company's own attribution is production pressure and a management
that *"failed to grasp the reality of workplaces"*, which is a competence and culture failure, the
class the corpus prices rather than refuses [E5-16, E3-57]; (ii) the company wrote *"The management
teams were responsible"* into an SEC filing, which is the [E2-26] positive pole, not the corpse
filing its own death certificate generously [E2-69]; (iii) every matter was followed by filed,
dated remediation. **[E5-17] caps all of it: "Sincerity and empathy can easily be faked."**

### THE GROUP REORGANISATION — what it cost Toyota, from the 6-Ks
**Live on 2026-09-13? No: completed.** 6-K 2026-06-15 (`0001193125-26-270230`): *"all of the
Transactions Involving TMC ... have been completed."* What TMC did, in the order the Master Agreement
of 2025-06-03 sets out:
1. **Did not tender its 74,100,604 Toyota Industries shares** (24.66%) into the ¥20,600 public tender
   offer by Toyota Asset Preparatory (established by **Toyota Fudosan**, *"an equity-method affiliated
   company of TMC"*); **sold them instead to Toyota Industries in a share repurchase at ¥16,972 a
   share** (price raised from ¥13,416 to ¥15,491 to ¥16,972 as the public price rose from ¥16,300 to
   ¥18,800 to ¥20,600; 6-K 2026-03-06 and 2026-03-30), about **¥1,257.6bn**, booking an expected
   consolidated gain of **¥576.9bn in FY2027** (non-recurring; excluded from owner earnings).
2. **Subscribed ¥800.0bn of non-voting preferred shares** in the offeror's parent, *"with a preferred
   dividend rate of 8.6% per annum (compounded)"*, increased from ¥706.0bn (6-K 2026-01-14). Stated
   purpose, verbatim: *"to invest the ample cash that the Company has accumulated to support the
   privatization of Toyota Industries, which has growth areas in non-automotive domain."*
3. **Bought back 1,192,330,962 of its own shares for ¥3,656,879,060,454** by self-tender at ¥3,067,
   **a 10% discount** to the lower of the prior close and the one-month average (6-K 2026-03-30), with
   a cap at ¥3,641.
**Net cash out of TMC: about ¥3.2 trillion** (3,656.9 + 800.0 − 1,257.6).

**The conflict, as filed (6-K 2026-03-30):** *"it is planned that Mr. Akio Toyoda ... who is the
Chairman of the Board of Directors and Representative Director of the Company and concurrently serves
as the Chairman of the Board of Directors and Representative Director of Toyota Fudosan, and Toyota
Fudosan will make capital contributions to the Parent Company of Toyota Industries' Offeror ... which
involves a potential risk of conflicts of interest between Mr. Toyoda and the Company."* Mitigation:
an Advisory Committee of three outside members, KPMG FAS as independent valuer, and *"Mr. Toyoda has
not participated in the Company's consideration of the Transactions Involving TMC"* (though his
written consent to the written resolutions was obtained, as the Companies Act requires). **The amount
of Mr. Toyoda's personal contribution is not stated in TMC's own filings**; TMC's notice refers the reader to the
offeror's own press release, which is not among the TMC 6-K exhibits read for this run. **A prompt, dated 2025-06-03, and the single sharpest one in
the file: the company's chairman is an investor in the vehicle the company is lending ¥800bn of
8.6% preferred money to.** The process is the Japanese Fair M&A Guidelines process and it is
documented; **[E2-68]'s asymmetry test — conduct where management holds the information advantage —
is exactly what this transaction is, and the filed process is the only evidence available.**

**Cross-shareholdings (6-K 2026-06-17, Report on Corporate Governance):** strategic holdings cut
*"to 114 (including 34 listed companies) as of March 31, 2026 from 200 (including 80 listed
companies) as of March 31, 2015"*, the Toyota Industries unwind being the largest. But the policy
reads: *"TMC will proceed with the sale of such shares **once it obtains consent from the issuer**
through a dialogue with the issuer."* **Toyota's shareholders' capital leaves a holding only with the
investee's permission. That is [E3-66]'s queue in one sentence: "almost every other constituency
stands higher in line."**

### STEP 2 — THE FLAGS
- [x] **weak accounting / cockroach [E4-22]** — fires, on the certification record above (a compliance
  cockroach, not an accounting one; no restatement found).
- [ ] unintelligible footnotes — no; the two-way statements are the clearest in the automotive row.
- [ ] **trumpeted projections [E4-22, E3-48]** — **does not fire on the record.** Toyota publishes an
  annual forecast, and has **under-promised**: FY2024 guided OI ¥3,000.0bn (6-K 2023-05-10) vs actual
  ¥5,352.9bn; FY2025 guided ¥4,300.0bn (6-K 2024-05-08) vs ¥4,795.6bn; FY2026 guided ¥3,800.0bn (6-K
  2025-05-08) vs ¥3,766.2bn (**−0.9%**); FY2027 guided ¥3,000.0bn (2026-05-08), revised to ¥3,400.0bn
  (2026-08-04). Three of four guides called for a decline. **[E5-30]'s ratchet exists (the forecast
  habit), but the record is conservative, not promotional.**
- [ ] serial share issuance [E5-15] — no; issued shares 16,314,987,460 (FY2024) to 14,594,987,460
  (2026-06-30).
- [ ] **EBITDA [E4-29]** — **zero occurrences** in the FY2026 20-F, the FY2026 results summary and
  presentation (6-K 2026-05-08) and the Q1 FY2027 summary and presentation (6-K 2026-08-04). Read in
  the furnished releases, per the CGNX rule, not only the annual report.
- [ ] filed-figure tells [E4-30] — cash taxes to pretax: FY2024 1,124,322/6,965,085 = 16.1%;
  FY2025 2,501,315/6,414,590 = 39.0%; FY2026 1,240,680/5,152,996 = 24.1%. Lumpy with Japanese
  interim-payment timing, not a falling trend.
- [ ] **metric-switching [E2-49]** — the FY2020 depreciation-method change was **announced with its
  quantified effect** (*"a decrease in depreciation expense of ¥173.2 billion"*): the candour case.
- **Prompt: disclosure location moved** — the three two-way statements left the audited notes for
  MD&A in the FY2026 20-F (Step 0). No figure changed.

### STEP 3 — THE PRIMARY TEST [E2-01]
Net income attributable to TMC ÷ average TMC shareholders' equity (balance sheets from the 20-Fs):
**FY20 10.0% · FY21 10.2% · FY22 11.5% · FY23 9.0% · FY24 15.8% · FY25 13.6% · FY26 10.1%; mean 11.5%.**
Leverage is inside it (the FS book), and so is the investment holding's income. Against [E5-40]'s ~12%
*"quite satisfactory"* for retained utility capital: at the line, not above it, in a business the
corpus would not call a utility.

**Half-owner test [E2-26]:** passes on the industrial/financial split (better than any peer in the
row) and on the written root cause; the unquantified Hino penalty and the unstated chairman
contribution are the two places it does not.

### The institutional imperative [E2-30]
- [ ] resists change — no: Hino deconsolidated, Toyota Industries unwound, strategic holdings halved.
- [x] **funds soak** — *"to invest the ample cash that the Company has accumulated"* into ¥800bn of
  preferred shares of a vehicle its chairman co-invests in. Fires, as a prompt.
- [ ] staff studies for the leader's craving — no evidence either way beyond the Advisory Committee
  and KPMG process, which is designed as the opposite.
- [ ] peers imitated — BEV spending is industry-wide (LF-ZC discontinued; Honda's ≈¥1.58tn write-off),
  recorded at Q2, not scored here.

### Capital allocation — the buyback conditions [E5-08, E4-31, E5-24]
- (1) Ample funds: **yes** (industrial cash ¥9,885bn and debt ¥2,800bn at 2026-03-31).
- (2) Material discount to conservatively calculated IV: **the ¥3,067 tender price put the pre-tender
  company at about ¥40.0 trillion (¥3,067 × 13,033,931,974); the conservative end of this run's range
  at the [E4-28] floor is about ¥20 trillion and the generous end about ¥35 trillion (Q5 below).
  CAPITAL-ALLOCATION FLAG**, stated with the humility clause: *"They also know a whole lot more about
  them than I do"* **[E4-13]**, and *"many CEOs never stop believing their stock is cheap"* **[E5-08]**.
  The filed purpose was not a value judgment at all: the tender existed to absorb Toyota Industries'
  9.15% holding *"without impairing the liquidity"* of the shares. **A cross-shareholding unwind paid
  for at a 10% discount to market is not the same act as a buyback at a discount to value.**
- (3) Information supplied [E4-31]: **yes**, extensively.
- **The August 2026 authority** (up to 500M shares / ¥1,000bn to 2027-08-04; 28.2M bought at an
  average ¥3,066 in August) runs at the same price level and carries the same flag.

### Pay [E4-27] *(the brief cited [E4-52], which is the lollapalooza row; the incentives row is [E4-27], and [E4-52] is used below only for converging prompts)*
Chairman Akio Toyoda: **¥2,113M** total FY2026 (fixed 396, bonus 620, share compensation 1,097)
against **¥1,949M** FY2025, **+8%**, in a year consolidated operating income fell 21.5% and net income
attributable fell 19.2%. The STI formula includes *"fluctuation of Toyota's market capitalization"*
(Item 6.B), the [E3-50] price-targeting prompt in a pay plan. ¥2.1bn is 0.05% of net income: **a
direction prompt, not a material cost.** Re-election support: 96.72% (2025), 95.97% (2026)
(extraordinary reports, 6-Ks 2025-06-13 and 2026-06-18).

### THE GUARDRAIL
- [x] Nothing here promotes the name; Q2 is OUT and stays OUT.
- [x] No great-manager dependence recorded at Q2 [E4-23].
- [x] No manager is the plan [E2-35, E2-36].

- **VERDICT: NOT ISSUED — Q2 closed the file.** *For the record only:* on the filings, **no integrity
  disqualifier at the registrant's board level was found**, and the file would read **IN on the
  binary with four converging prompts [E4-52]** (the four-company certification record, the chairman's
  co-investment, the ¥800bn "ample cash" preferred, the consent-gated sale policy) **and a live
  capital-allocation flag.** That reading is the absence of a found disqualifier, not a finding that
  anyone is honest [E5-17], and it would have been written as a gate with those prompts unresolved.

## Q4 — WILL IT SURVIVE? — **RECORDED, NOT GOVERNING**
**Q2 is OUT; the file is closed for any buy decision. This section is recorded because the operator's
output contract needs a price, and a price needs owner earnings; and because the brief asked for the
industrial owner earnings over every window, both (c) ends, SBC resolved, and the named way it dies.
No Q4 verdict governs anything.**

### Owner earnings — the one number **[E2-23]**, industrial perimeter
**Perimeter: the Non-Financial Services Businesses**, from the audited-until-FY2025 two-way
Consolidated Statement of Cash Flows (FY2026 in Item 5), because consolidated operating cash nets a
¥39 trillion lending book: in FY2026 Financial Services **consumed** ¥33,745M of operating cash while
earning ¥857,393M pre-tax, and in FY2024 it consumed ¥2,782,318M. The FS earnings enter separately,
as look-through, never through its cash flow.

**Construction (all ¥ millions; arithmetic in `_research 2026-09-13 TM/oe.py`, inputs transcribed from
the filed statements; FY2017-FY2019 US GAAP, FY2020-FY2026 IFRS):**
- **OCF** = *"Net cash provided by (used in) operating activities"*, Non-Financial Services.
- **(c), the judgment** = additions to fixed assets excluding equipment leased to others + additions
  to equipment leased to others + additions to intangible assets − proceeds from sales of each.
- **SBC** = filed stock-compensation expense (below).
- **(A)** = OCF − SBC − (c). **(B)** = OCF − SBC − D&A, **INVALID, display only.**
- **(D)** = (A) + Financial Services net income attributable to TMC (look-through of a wholly-owned
  lender's earnings, as the F run's construction (D)). **(E)** = (D) + undistributed equity-method
  earnings (share of profit less *"Dividends from associates and joint ventures accounted for under
  the equity method"*), the **[E3-04]** look-through.

| FY | basis | industrial OCF | (c) net capex | D&A | (c)/D&A | **(A)** | (B) invalid | FS NI | undistributed eq. | **(D)** | **(E)** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2017 | US GAAP | 2,564,310 | 1,246,440 | 939,795 | 1.33 | **1,317,870** | 1,624,515 | 152,157 | 181,734 | 1,470,027 | 1,651,761 |
| 2018 | US GAAP | 2,917,887 | 1,297,745 | 1,010,972 | 1.28 | **1,620,142** | 1,906,915 | 521,473 | 273,680 | 2,141,615 | 2,415,295 |
| 2019 | US GAAP | 2,707,336 | 1,448,666 | 1,033,528 | 1.40 | **1,258,670** | 1,673,808 | 227,799 | 155,744 | 1,486,469 | 1,642,213 |
| 2020 | IFRS | 2,623,364 | 1,589,009 | 855,863 | 1.86 | **1,030,355** | 1,763,501 | 218,060 | 101,831 | 1,248,415 | 1,350,246 |
| 2021 | IFRS | 2,634,200 | 1,532,117 | 928,533 | 1.65 | **1,098,083** | 1,701,667 | 369,824 | 145,928 | 1,467,907 | 1,613,835 |
| 2022 | IFRS | 3,126,101 | 1,592,390 | 1,060,079 | 1.50 | **1,529,711** | 2,062,022 | 480,716 | 307,789 | 2,010,427 | 2,318,216 |
| 2023 | IFRS | 3,682,203 | 1,822,044 | 1,240,749 | 1.47 | **1,856,159** | 2,437,454 | 292,334 | 293,431 | 2,148,493 | 2,441,924 |
| 2024 | IFRS | 6,970,082 | 2,085,782 | 1,303,053 | 1.60 | **4,883,329** | 5,666,058 | 411,114 | 303,129 | 5,294,443 | 5,597,572 |
| 2025 | IFRS | 4,736,610 | 2,170,027 | 1,413,066 | 1.54 | **2,563,750** | 3,320,711 | 484,129 | 88,426 | 3,047,879 | 3,136,305 |
| 2026 | IFRS | 5,479,380 | 2,481,528 | 1,472,087 | 1.69 | **2,995,274** | 4,004,715 | 618,430 | 248,531 | 3,613,704 | 3,862,235 |

Sources: two-way cash-flow statements in 20-F FY2019 (FY17-18, US GAAP), FY2020 (FY19), FY2022
(FY20-22), FY2025 (FY23-25), FY2026 (FY25-26); FS net income attributable from the two-way income
statements (FY17-FY19: FS net income, US GAAP split); equity-method dividends from the related-party
note of each 20-F (FY17-19: *"Dividends from affiliated companies accounted for by the equity method"*,
20-F FY2019 and FY2020). **The FY2020 basis gap, checked:** OCF less net capex is ¥1,071,384M on US
GAAP and ¥1,034,355M on IFRS (3.5%): IFRS moves capitalised development out of operating cash and
into intangible additions, and the two effects nearly cancel, so the ten-year window is shown with the
basis flagged, not spliced blind. **No year's figure differed between the two 20-Fs that each carry
it** (FY2023 operating cash 3,682,203 in the FY2023, FY2024 and FY2025 20-Fs).

**EVERY WINDOW, PUBLISHED [E4-25, E4-38]** (means, ¥bn):
| window | (A) industrial | (B) INVALID | (D) + FS NI | (E) + undistributed |
|---|---|---|---|---|
| **5-yr FY2022-FY2026 (corpus default [E2-42])** | **2,766** | 3,498 | 3,223 | **3,471** |
| 7-yr FY2020-FY2026 (IFRS only) | 2,280 | 2,994 | 2,690 | 2,903 |
| **10-yr FY2017-FY2026 (two bases)** | **2,015** | 2,616 | 2,393 | 2,603 |
| 3-yr FY2024-FY2026 | 3,481 | 4,330 | 3,985 | 4,199 |
| 5-yr excluding FY2024 (FY2021-23, FY2025-26) | 2,009 | 2,705 | 2,458 | 2,675 |

- **Short-window mean** (5 years, FY2022-FY2026, (A)): **¥2,766bn**
- **Long-window mean** (10 years, FY2017-FY2026, (A)): **¥2,015bn**
- **Spread, conservative end: 37%** (5-year over 10-year).
- **Combined range** across the valid constructions and all windows except the 3-year (which leans
  on FY2024): **¥2.0 trillion (A, 10-year) to ¥3.5 trillion (E, 5-year), a 1.72x range.**
- **Too wide to reach a conclusion [E4-25]?** Not for the question Q5 asks: **every point in it,
  on the ¥35.8 trillion cap, sits below the [E4-28] floor** (Q5 computation). It is too wide to rank,
  and does not need to be.
- **The distorted years, named [E5-11, E4-41]:** **FY2024 is the outlier** (industrial OCF ¥6.97
  trillion, 1.27x the next-highest year): the 20-F's bridge gives *"the ¥2,000.0 billion impact of marketing
  efforts"* and +¥685bn of exchange rates in the supply-tight, weak-yen year. **Removing it drops the
  5-year (A) from ¥2,766bn to ¥2,009bn**, the same level as the ten-year mean. FY2021 carries the
  pandemic; FY2022-FY2023 the semiconductor shortage and *"soaring materials prices"* (−¥1,290bn in
  FY2023); FY2018's FS net income of ¥521,473M carries the US tax-reform year; FY2020 carries the
  depreciation-method change; FY2025 operating cash is depressed and FY2026's flattered by Japanese
  tax-payment timing (industrial income taxes paid ¥2,347,622M against expense ¥1,446,627M in FY2025;
  ¥1,159,061M against ¥935,124M in FY2026), which the multi-year mean absorbs. **And the currency is
  the luck the whole decade rode (+¥1,685bn of operating income on the Q2 bridge)**; it is named
  rather than stripped, because a mechanical ex-FX restatement would be a second windage.

### Maintenance capex — a DISCLOSED JUDGMENT, and it is the exception class **[E3-44], [E5-20]**
**The D&A end is INVALID here, on four filed grounds:**
1. **Industrial net capex exceeded industrial D&A in all ten years, mean 1.53x, never below 1.28x,
   on units that grew 0.7% a year.** Spending that does not buy volume is spending to stand still.
2. **The company describes the spending as maintenance and replacement**, Item 5.B FY2026: *"Toyota
   will use its funds to efficiently invest in maintenance and replacement of conventional
   manufacturing facilities and the introduction of new products."*
3. **D&A was lowered by policy, not by the assets**: *"a decrease in depreciation expense of ¥173.2
   billion, which positively impacted operating income but not net cash provided by operating
   activities"* (20-F FY2020). The D&A default fell by 17% in one year with no change in what the
   plants needed.
4. **[E4-47]**: tooling bought in the yen of 2016 is replaced in the yen of 2026, and the 69% rise in
   revenue per unit is largely the yen and the price level.
**(c) = total net capex, the conservative end, for every row. Conservatism is spent here and only
here. WINDAGE COUNT: ONE.** The (B) column exists only to display the guess **[E2-23]**.
**Is (c) too high?** The strongest case that it is: some FY2023-FY2026 capex is battery and BEV
capacity whose purpose is future volume, not current volume. The filings do not separate it, and the
LF-ZC cancellation (Note 36) shows part of it is being written off rather than earning; **no filed
basis supports carving it out.**

**Stock compensation subtracted in full [E5-06] — RESOLVES, and is COMPLETE on a stated basis.**
Filed (20-F FY2026 Note 31(4)): *"Expenses related to stock-based compensation amounted to ¥971 million
in the year ended March 31, 2024, ¥2,833 million in the year ended March 31, 2025 and ¥2,578 million in
the year ended March 31, 2026."* FY2017-FY2019: *"There were no stock-based compensation expenses for
stock options as selling, general and administrative expenses for the years ended March 31, 2018, 2019
and 2020"* (20-F FY2020 Note 19), and the restricted-stock plan began in June 2019. **FY2020-FY2023:
no expense figure is filed; the subtraction used is the shareholder-approved ceiling of ¥4.0 billion a
year** (*"the maximum share compensation was set at 4.0 billion yen per year"*, 20-F FY2021-FY2023
Item 6), which exceeds every filed year and so errs toward lower owner earnings. **[E3-70]'s market
measure is satisfied by construction**: restricted shares are measured *"based on the market price of
TMC's shares"* at grant. **At ¥1-4bn against ¥2-3 trillion of owner earnings, SBC is 0.1% and cannot
move any conclusion; it is subtracted anyway.**

**Look-through [E3-04]:** construction (E) adds ¥88-308bn a year of undistributed equity-method
earnings. **Forward caveat, filed:** Toyota Industries was the largest affiliate and was sold on
2026-06-15; the ¥800bn preferred at 8.6% compounding replaces part of that look-through with a
contractual accrual whose cash depends on a leveraged buyout vehicle.

### Great, good, or gruesome? **[E4-20]**
- [ ] great · [x] **good, at the low edge** · [ ] gruesome
- **Evidence:** (A) is positive in every one of ten years (low ¥1.03 trillion, FY2020) and grew in
  yen, so it is not the gruesome account that *"earns little or no money."* But the capital it adds
  earns a cycle-dependent return: the incremental pre-tax return on automotive operating assets was
  **6.0% measured FY2020→FY2026 and 20.8% measured FY2020→FY2025** (Q2), and the ten-year bridge
  shows the operating-income growth came from the currency. **[E4-43]: the good class passes; this is
  its bottom edge, and nothing in the record shows the rate rising as the years pass.**

### Staying power — score all three **[E5-11]**. The industrial balance sheet is genuinely strong, stated first.
- **(1) Large and reliable earnings: YES.** (A) never below ¥1.0 trillion in ten years, through a
  pandemic, a chip shortage and a ¥1.38 trillion tariff year.
- **(2) Massive liquid assets: YES.** Industrial cash ¥9,885,097M plus current other financial assets
  ¥3,211,041M against industrial debt ¥2,800,078M at 2026-03-31: **net ¥10.3 trillion.** Group
  *"Liquid assets ... ¥22,117.9 billion."* Policy: on-hand funds to *"cover both six months of fixed
  costs in the automotive business and six months of refinancing requirements in the financial
  services business."* **After the year end: −¥3,656.9bn (self-tender, settled 2026-05-25), −¥800.0bn
  (preferred), +¥1,257.6bn (Toyota Industries shares), and the August buyback authority of up to
  ¥1,000bn: the industrial net cash falls to roughly ¥6-7 trillion before FY2027's own cash flow.**
  Still massive; about ¥3.2 trillion smaller than the balance sheet the 20-F shows.
- **(3) No significant near-term cash requirements: THE FINANCE ARM IS THE ONE THAT HAS THEM.**
  Financial Services *"Short-term and current portion of long-term debt"* **¥17,042,885M** due within a
  year, refinanced continuously in the bond and paper markets (FY2026 proceeds from long-term debt
  ¥12,408,438M; payments ¥11,087,637M). The industrial side's near-term requirements are dividends
  (¥1,238,974M FY2026), the buyback authority, and the unquantified LF-ZC partner compensation. **The
  industrial cash alone would cover about seven months of those maturities (9,885 ÷ 17,043), about nine
  with current financial assets; the policy is sized to six months of refinancing, and beyond that it
  depends on the markets staying open [E5-39].**
- **Leverage, named and quantified [E4-16, E3-29]:** FS assets 8.1x FS equity; consolidated
  interest-bearing debt 108.2% of TMC equity; **industrial interest paid ¥90,538M against industrial
  operating cash ¥5,479,380M less net capex ¥2,481,528M: covered 33 times [E2-54].** Terms [E3-52]:
  the FS debt is covenanted market debt with due dates, not float.
- **Jurisdiction [E3-66]:** a Japanese company whose strategic holdings are sold only *"once it
  obtains consent from the issuer"* and whose ¥3.2 trillion group reorganisation was structured around a
  founding-family-linked vehicle (Q3). **Public shareholders stand behind the group in the queue.**

### Name the specific way THIS business dies **[E2-27, E3-24]** — exposure, not experience **[E4-40]**
**The registered shapes, tested — the register stands at TEN, not the eight the brief's pointer lists**
(the RGTI and CNR runs stop at eight; BAM added the ninth and the concurrent SONY run the tenth, both
folded into the reading list on 2026-09-13): ORCL (contracted not to stop) — no; ARM (earns nothing for
owners after paying its people) — no, SBC is 0.1%; BE/HHH (too little history) — ten years filed; BA
(spends cash undoing past work) — partly (¥844.9bn of FY2026 recall provisions, Hino and certification
costs), not the dominant use; SWK (dividend by selling the business) — no, though FY2027's ¥576.9bn gain
on Toyota Industries is exactly the kind of year a reader must not annualise; ACVA/FLNC/NEGG (the
borrowed balance sheet, with FLNC's fixed-price variant already registered under the name "the
treadmill") — the FS arm borrows, the industrial does not; CNR (the long tail on a short cycle) — no
long fixed claims of that kind; RGTI (the equity is the revenue) — no; **BAM (the warehouse)** — no
syndication commitments; **SONY (the camouflage: the company survives, the owner's return dies, because
franchise legs' cash is recycled into legs that re-win a race every cycle and the consolidated series
hides the rate)** — **the nearest, and it shares the death but not the mechanism**: Toyota has no
franchise leg funding the race, and nothing is hidden, because the two-way statements and the causal
bridge print the rate. **None fits exactly.**

**AN ELEVENTH SHAPE, NAMED: THE PASS-THROUGH** *(first drafted as "the treadmill"; renamed before commit because FLNC's fold already registered that name for a variant of the sixth)*. A business that must spend more than its depreciation every
year to keep the same unit volume, in an industry where every competitor does the same, so that each
round of spending is individually rational and collectively neutralising **[E2-27]**, and where its
own filed savings are passed through to input costs, expenses and customers **[E3-62]**. It does not
die of insolvency. **It dies of return on capital**: the owner's claim compounds at the rate the
pass-through allows, which the filings put at a pre-tax return on operating assets of about 10-13% in
ordinary years, flattered in the lucky ones.

**Quantified from filed figures, two exposures:**
1. **The return exposure (likely).** FY2026 already shows it: automotive margin 6.11%, break-even
   volume *"significant rise"*, tariffs ¥1,380bn (37% of consolidated operating income), guidance for
   FY2027 operating income of ¥3,400bn (revised 2026-08-04) against ¥5,353bn two years earlier. **At
   the FY2026 automotive margin and FY2026 capex, (A) is about ¥3.0 trillion on ¥45 trillion of
   revenue; two further points of automotive margin (less than the three points lost FY2025 to FY2026)
   is ¥0.9 trillion a year of pre-tax operating income off it.**
2. **The lending tail (a low-level possibility), in [E3-24]'s own arithmetic.** If 10% of the
   ¥38,966.6bn of finance receivables produced losses averaging 30% of principal, the loss would be
   **¥1,169bn: 1.4 years of FY2026 FS pre-tax income, 2.9% of TMC equity, 11% of the year-end
   industrial net cash (about 17% of it after the post-year-end transactions).** It would not distress this balance sheet. The exposure the lease book adds is residual value
   on electrified vehicles, which Honda's FS already impaired by ¥81,833M in FY2026 (GM run research,
   Honda 20-F Note (4)).
- **Likelihood:** [x] **likely** (the pass-through, as a slow compression of return) · [ ] a real
  possibility · [x] **a low-level possibility** (a lending loss large enough to impair the franchise
  of the parent).
- **The bear case its holders would accept as fairly stated [E4-51]:** "Toyota will not fail; it
  will keep earning 10% on its operating assets in ordinary years, with the yen deciding whether that
  looks like 7% or 15% in any one year, and the owner will earn roughly what the business earns
  [E3-17]."

- **VERDICT: NOT ISSUED — Q2 closed the file.** *For the record only:* survival is not in doubt on
  any filed measure; staying power scores YES / YES / FS-dependent; owner earnings resolve over ten
  years in a 1.72x range. Had Q2 passed, this section would have read **IN on survival**, with the
  pass-through carried to Q5 as the reason the growth assumption must be near zero.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 is OUT. **What follows is the price the queue's
output contract requires, headed as operator rule 3 requires, and it carries no entry language.**

---
## Q5 — **COMPUTATION — NOT A CLEARANCE**

*Produced only because the queue's instruction requires every run to end with a price. Q1-Q4 do not
all show IN. No Q5 verdict is issued.*

**ONE BOOK [E3-34, E4-21].** No discounted cash flow was run as a decision artifact. The perpetuity
arithmetic below only inverts the quote into an implied growth rate (arithmetic in
`_research 2026-09-13 TM/q5.py`).

**1. THE YIELD** — owner earnings ÷ **market cap ¥35,807bn** (¥3,031 × 11,813,621,960, Step 0), beside
the **30-year JGB 4.00%** (3.995%, MOF, 2026-09-10):

| Owner-earnings basis (Q4) | OE ¥bn | yield | points over JGB | per share | growth the price implies at the JGB | growth needed to reach the ~10% floor |
|---|---|---|---|---|---|---|
| **(A) industrial, 10-yr — THE BOTTOM BOUNDARY [E5-34]** | **2,015** | **5.63%** | +1.63 | ¥171 | −1.6% | **+4.1%** |
| (A) industrial, 5-yr ex-FY2024 | 2,009 | 5.61% | +1.61 | ¥170 | −1.5% | +4.2% |
| (A) industrial, 7-yr | 2,280 | 6.37% | +2.37 | ¥193 | −2.2% | +3.4% |
| (D) + FS net income, 10-yr | 2,393 | 6.68% | +2.69 | ¥203 | −2.5% | +3.1% |
| (E) + undistributed affiliates, 10-yr | 2,603 | 7.27% | +3.27 | ¥220 | −3.1% | +2.6% |
| **(A) industrial, 5-yr (corpus default window)** | **2,766** | **7.72%** | **+3.73** | ¥234 | −3.5% | **+2.1%** |
| (D) + FS net income, 5-yr | 3,223 | 9.00% | +5.01 | ¥273 | −4.6% | +0.9% |
| **(E) + undistributed affiliates, 5-yr — THE GENEROUS END** | **3,471** | **9.69%** | +5.70 | ¥294 | −5.2% | **+0.3%** |
| *memo: (E) 3-yr, leans on FY2024* | *4,199* | *11.73%* | *+7.73* | *¥355* | | *−1.5%* |
| *memo: (B) 5-yr, the D&A end, INVALID* | *3,498* | *9.77%* | | | | |

**2. WHAT THE PRICE ALREADY ASSUMES.** At the bare sovereign, every construction implies owner
earnings **shrinking** 1.5% to 5.2% a year forever: **the quote is not demanding against the JGB.**
**Against the floor it is**: from the bottom boundary the price needs **+4.1% a year in perpetuity**,
and from the corpus-default five-year industrial figure **+2.1%**. **What the business has done:**
units +0.7% a year over ten years; consolidated operating income +2.8% a year FY2016-FY2026 in yen
(¥2,853.9bn to ¥3,766.2bn), **all of it and more attributable to the currency on Toyota's own bridge**
(Q2); FY2027 guided operating income ¥3,400bn, down 9.7%. **[E4-35]: sustained growth is the rare
event even among the best businesses, and [E4-44]: value cannot outgrow earnings.** The growth that
closes the gap from the bottom boundary is not in the record.

**3. WHAT YOU ARE PAID:** **+1.6 to +5.7 points over the JGB**, and +3.7 points on the corpus-default
industrial figure. **That spread is real, and it is the best fact for the price: Toyota's equity yields
well above its own sovereign.** The floor does not move with the sovereign.

**THE FLOOR, BEFORE ANY RANKING [E4-28, E3-13].** *"that's the figure we quit on ... that's true whether
short rates are 6 percent or whether short rates are 1 percent."* **Honest pre-tax expectancy at this
price: about 5.6% at the bottom boundary to about 10% at the generous end** (9.7% yield plus the
0.7%-a-year unit growth the decade shows, and the generous end includes the lender's retained
earnings, the affiliates' retained earnings, and the best supply-tight year in the record). **Below
roughly 10% everywhere except the top edge of the most generous construction. Not ranked; quit on.**
[E5-34] prices against *"the bottom boundary of our estimate"*, and at the bottom boundary (5.6%) it
would be quit on even if Q2 had passed; the generous end reaches the floor only by counting retained
earnings the owner cannot draw and a year the filings call supply-tight.

### THE PRICE — THE VALUE AS A ROUND-NUMBER RANGE [E4-01]
| | value of the equity | per share |
|---|---|---|
| **Against the [E4-28] 10% floor, zero growth, bottom boundary to generous end** | **¥20 trillion to ¥35 trillion** | **roughly ¥1,700 to ¥2,950** |
| Against the bare JGB 4.00%, zero growth (a display of the gravity, not a value) | ¥50 trillion to ¥87 trillion | roughly ¥4,250 to ¥7,350 |
| *memo: the ¥3,067 self-tender of April 2026, applied to the pre-tender count* | *¥40.0 trillion* | *¥3,067* |
| **CURRENT PRICE, TSE close 2026-09-11 (aggregator, flagged)** | **¥35.8 trillion** | **¥3,031 (NYSE ADR $198.20 = 10 shares)** |

**WHICH BAR:** [x] **Screamer test [E4-01]** — does the price already clear the conservative case,
with no margin added? **No. ¥3,031 sits above the whole floor-based range (¥1,700-¥2,950) and inside
the bare-sovereign range.** *"inside the range → no useful conclusion, move on"*; above the floor
range → no. **Windage count: ONE** (the (c) judgment at Q4). Bar 1's end margin is **not** applied: the
two bars are never run on the same number.

**What the buyer is paying for, in words.** At ¥3,031 the buyer pays about **13x the corpus-default
five-year industrial owner earnings and about 18x the ten-year figure** for a well-financed,
well-run vehicle maker that earns roughly 10-13% pre-tax on its operating assets in ordinary years,
holds a ¥39 trillion lender and a portfolio of group affiliates, and has turned a decade of real cost
savings into flat operating income once the yen is set aside. **The buyer is paying the floor price
for the lucky years, and the JGB price for the ordinary ones.**

**NO VERDICT ISSUED. The run stopped at Q2.**

---
## Q6 — **COMPUTATION — NOT A CLEARANCE.** WHAT WOULD PROVE THIS FILE WRONG, PRE-COMMITTED [E1-02]

**No position exists, so no [E2-28] hold read is required and no alert band is armed** (a price alert
on a name that failed on the business would be a category error: the QLYS ruling, FOLD step 4).
**Reopening conditions, in words, written before any future data arrives:**

1. **The Q2 refutation.** The **"Effect of cost reduction efforts" line in the consolidated
   operating-income bridge sums positive over a rolling five years that includes a materials-price
   upswing**, AND the automotive margin holds above **9%** through a year in which **units fall and
   the exchange-rate line is negative**. Both, in the same filed window. That would be the wide and
   sustainable cost advantage [E2-58] showing up where Toyota itself measures it.
2. **The competitor-row refutation.** Toyota's automotive margin exceeds **every** filer in the row
   (GM, Ford, Honda automobile, Stellantis, Tesla) **in each of five consecutive fiscal years**, not in
   the mean. A moat is a relative claim; a durable lead in every year is the relative evidence this
   file did not find.
3. **The price-only reopening does not exist.** Q2 failed on the business; a lower price does not
   create a franchise [E5-35]. **If both 1 and 2 were met**, the file reopens at Q2, and Q3's four
   converging prompts must then be resolved before any Q5 is run: the Hino penalty amount, the
   chairman's contribution to the Toyota Industries vehicle, the terms and cash yield of the ¥800bn
   preferred, and the consent-gated strategic-shareholding policy.
- *(CONVENTION: the 9% margin and the five-consecutive-year tests above are this run's stated thresholds, not corpus numbers; the 9% sits above the top of Toyota's own ordinary-year margin band (6.1-8.0%), and the five years match the corpus's default window [E2-42], so that a refutation cannot come from one lucky year.)*
- **Monitoring metric, stated [E4-32, E4-55]:** units by region and the cost-reduction line, not
  yen revenue or reported operating income.
- **Next catalysts:** the Q2 FY2027 results 6-K (early November 2026); the September 2026 repurchase
  status 6-K (early October 2026); the FY2027 20-F (June 2027), which will carry the first year
  without Hino and without the Toyota Industries look-through.

- **VERDICT: NOT ISSUED.** The file closed at Q2.

---
## SELF-AUDIT (operator rule 6)
- [x] Questions answered in order; no verdict skipped. **Q1 IN → Q2 OUT → stop.** Q3 and Q4 recorded
      under explicit NOT GOVERNING banners; Q5 and Q6 headed COMPUTATION — NOT A CLEARANCE.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests on the
      filed segment note and the two-way statements. The PROVISIONAL label at Q2 attaches to an
      upgrade the verdict does not make.
- [x] Every UNRESEARCHED item is named with where it lives: **BYD's 2025 annual report (HKEXnews)**
      for the competitor row; **the offeror's press release** for the chairman's contribution amount;
      **Hino's own disclosure** for the US penalty amount. None bears on the Q2 verdict.
- [x] No UNKNOWABLE verdict is used.
- [x] Step 0: the filing was read, with accession numbers for ten 20-Fs (six IFRS, four US GAAP), the
      six 20-F/As of 2024-02-06, and 49 6-Ks; **consolidated operating cash ¥5,472,920M cross-checked**
      between the audited statement and the MD&A, and FY2025's ¥3,696,934M against `companyfacts`.
- [x] Owner earnings on multi-year means; **five windows published** (3, 5, 5-ex-FY2024, 7, 10
      years); (c) disclosed as a judgment with [E5-20]'s exception class applied and the D&A end ruled
      INVALID on four filed grounds; the FY2020 accounting-basis gap measured (3.5%) rather than assumed.
- [x] **SBC resolves and is complete**: filed for FY2024-FY2026, filed as zero for FY2017-FY2019,
      bounded by the shareholder-approved ¥4.0bn ceiling for FY2020-FY2023 and subtracted at the
      ceiling.
- [x] Competitor row filled: **five peers complete from SEC filings, VW and Hyundai partial from
      rung 3, BYD blocked with the obstacle named**; the metric problem (all-in vs adjusted) stated
      before the table; two peer figures re-checked by hand.
- [x] Sovereign is for the earnings currency, **from the issuing authority (Japan MOF), dated
      2026-09-10, tenor 30 years**, struck fresh twice; the choice of yen argued from the filing and
      shown not to move the floor.
- [x] Share count **read by hand** from the 20-F cover and walked through the tender result, the Q1
      FY2027 summary and the August repurchase notice; treasury and ESOP-trust shares excluded; no
      other class remains (Model AA cancelled 2021-04-03).
- [x] Value stated as a round-number range, not a point estimate.
- [x] **One bar chosen (screamer), not both. Windage count: ONE**, at the (c) judgment.
- [x] Prices dated; aggregator (Yahoo) used for the live quotes only and flagged; ADR ratio derived
      and cross-checked against the Tokyo quote; the USD cap shown for orientation only and never used
      against yen earnings.
- [x] Every judgment carries a ledger id (operator rule 8). **97 distinct ledger ids cited in this
      file, all checked against `principle_ledger.csv`: 0 phantom.**
- [x] The analyst's own incentive, checked [E4-27, E4-26]: the brief's hypothesis ("does Toyota's
      record differ?") was pursued until it produced a fact that cuts against the verdict (Toyota
      leads the volume half of the row), and that fact is stated first in the row's findings and again
      below.
- [x] `python tools/check_framework.py` **PASS** before the final commit (267 ledger rows, 0 phantom
      citations, 0 unlabelled numbers).
- [x] Run committed to git by pathspec: Step 0 `f099802`, Q1 `11bedfd`, Q2 `8203b51`, Q3-Q4 `945f675`,
      Q5-Q6 and this audit `60d8335`; the fold (register entry, WAVE 5 strike, reading-list narrative) in the
      commit titled "TM fold".

## REGISTER
- **Verdict: [x] OUT (about the business).**
- **One line:** *Toyota is the best volume car company in the filed row and not a franchise: its own
  ten-year cost-reduction line nets to minus ¥645 billion, its decade of operating-income growth was the
  yen's, and the margin that leads its peers fell from 11.2% to 6.1% in two years.*
- **Work orders for any future upgrade (not for this verdict):** BYD 2025 annual report (HKEXnews,
  rung 4; the IR site returned HTTP 504); Hyundai 2021-2023 annual reports (hyundai.com, rung 3); VW
  2021-2023 absolute automotive figures (VW annual reports, rung 3).

---
# THE OUTPUT CONTRACT

## (a) THE PRICE — **COMPUTATION — NOT A CLEARANCE** (operator rule 3)
**Roughly ¥1,700 to ¥2,950 a share against the [E4-28] floor at zero growth (¥20 trillion to ¥35
trillion for the equity); roughly ¥4,250 to ¥7,350 against the bare 30-year JGB. Current price ¥3,031
(TSE close 2026-09-11; NYSE ADR $198.20 = 10 shares). Market capitalisation ¥35,807bn on 11,813,621,960
shares.** Owner earnings ¥2.0 trillion (industrial, ten-year, the bottom boundary) to ¥3.5 trillion
(five-year, with the lender's and the affiliates' retained earnings): **a 5.6% to 9.7% yield against a
4.00% sovereign.** No entry language attaches to any of this.

## (b) PASS / FAIL
# **FAIL — the file was closed by QUESTION 2.**
**Q1 IN · Q2 OUT · Q3 and Q4 recorded, not governing · Q5 and Q6 computation, not clearance.**

**The strongest single fact against this file's conclusion [E4-51]:** on an all-charges-in basis
**Toyota's automotive margin is the highest in the filed competitor row in each of the last three
fiscal years, and its five-year pooled 8.22% is above every volume manufacturer's comparable figure**
(GM 5.39% with its lender inside, VW about 5.6%, Ford 1.46%, Honda automobile −0.62%), while Honda,
Ford, Stellantis and GM wrote off their EV programmes. **GM and Ford failed Q2 at the bottom of this
row; Toyota is at the top of it.** The file's answer is that the lead is inside the charges the peers
exclude and behind GM and Stellantis on their own measures, that it halved in two years, and that
Toyota's own cost line shows the savings did not stay home. But the fact is filed, it is favourable,
and it is recorded without hedging.

### TOOLING AND DOCUMENT DEFECTS FOUND
1. **The triage's skip reason was right in effect and wrong in cause.** TM's `companyfacts` holds
   `ifrs-full` annual facts for **FY2020-FY2025 only**, because Toyota switched from US GAAP to IFRS
   with the FY2021 20-F (the US GAAP history sits under `us-gaap`, a different namespace and basis), and
   **the FY2026 20-F filed 2026-06-10 had not been ingested by `companyfacts` on 2026-09-13**, three
   months later. **The SONY run found the same ingestion lag for its FY3/26 20-F.** Two Japanese March
   filers, same gap: any screen that trusts `companyfacts` for a Japanese 20-F filer is a year stale.
2. **A basis change inside a filer's own history is invisible to a namespace-bound reader.**
   `annual()` accepting `ifrs-full` (the 2026-09-01 fix) is necessary and not sufficient: a ten-year
   window on a filer that changed GAAP needs both namespaces and a measured basis gap. The gap here
   was 3.5% of free cash in the overlap year; it will not always be small.
3. **The two-way statements moved from the audited notes (FY2021-FY2025 20-Fs) to Item 5 MD&A (FY2026
   20-F).** A parser keyed on *"NOTES TO CONSOLIDATED FINANCIAL STATEMENTS ... (iii) Consolidated
   Statement of Cash Flows on Non-Financial Services"* finds nothing in the FY2026 filing.
4. **`tools/sources.py` EUR leg failed** (`SSL: CERTIFICATE_VERIFY_FAILED` against the ECB data API);
   USD and JPY struck normally. Not needed here; the next euro filer (STLA is in WAVE 5) will hit it.
5. **Toyota does not furnish the monthly "Share Buyback Report" 6-K the SONY run recommended for
   Japanese ADRs**; it furnishes *"Notice Concerning the Status of the Repurchase of Shares"*, which
   gives the month's purchases but not the treasury balance. The treasury balance came from the
   quarterly financial summary. **The SONY method does not generalise to every Japanese filer.**
6. **`fts_count()` was not used**; every competitor naming and quote came from downloaded filings.

### DEFECTS IN THE BRIEF
1. **"The register holds 82 entries before this wave"** — the concurrent SONY run folded first, so the
   register held **83** when this run folded, and the check is 83 → 84.
2. **"the registered survival shapes (the RGTI and CNR runs list them)"** — those lists stop at eight;
   BAM added the ninth (the warehouse) and SONY the tenth (the camouflage). **And the name this run first
   drafted, "the treadmill", was already registered by the FLNC fold** for a variant of the sixth; the
   shape here is recorded as the eleventh, **THE PASS-THROUGH**.
3. **"pay [E4-52]"** — [E4-52] is the lollapalooza row; the incentives row is [E4-27] (the SONY run found
   the same defect in its brief).
4. **"ARM Arm Holdings run of 2026-09-12"** — the file is `2026-09-11 Run - ARM Arm Holdings.md` (the run
   was started 2026-09-11 and closed 2026-09-12).
5. **"a 20-F/A filed 2024-02-06 (0001193125-24-024814): open it and state what it amended"** — it is one
   of **six** 20-F/As filed that day (FY2016, FY2017, FY2019, FY2020, FY2021, FY2023), all amending only
   the Iran Section 13(r) disclosure. The pointer was accurate and incomplete.
6. **The competitor list names three non-SEC registrants (VW, Hyundai, BYD).** The F precedent treated
   them as UNKNOWABLE; the framework's evidence ladder has a rung 3 (company IR site, English), and VW
   and Hyundai were readable on it. **"Not an SEC registrant" is a rung, not a verdict.**
7. **The priors, framed to be refuted:** "GM and F failed on excess-capacity language; test whether
   Toyota's record differs" — **it differs, and still fails**: Toyota leads the volume half of the row;
   the lead is neither wide nor sustainable. "Q3: establish whether any take-private of a group company
   is live" — **not live; completed 2026-06-15**, at a net ¥3.2 trillion cash cost to TMC. **The [E2-49]
   metric-withdrawal prior: did not fire** (the FY2020 depreciation change was announced with its
   quantified effect).

# Company Run — GLOBALFOUNDRIES Inc. (GFS) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

**Queue context.** A name in **WAVE 5** of `Screens/WATCHLIST RUN QUEUE.md` (the unpriced watchlist businesses), the ninth
of the eleven foreign 20-F filers to be run (after TM, SONY, HMC, TSM, UMC, ERIC, SPOT, and alongside a concurrent STLA run).
The 2026-09-01 triage skipped it as *"foreign 20-F filer ... short XBRL history."* **Read here as UNLABELLED: a prompt to read the
20-F by hand, not a verdict.** The run file was created from the template before any fetch (write-early protocol). Research on
disk: `Test Runs/_research 2026-09-13 GFS/`. **The TSM and UMC runs of the same morning were read in full before anything was
built here; their foundry competitor row, their [E4-04], [E3-03](2) and [E2-44] readings and their survival shapes are precedent,
not conclusions: GlobalFoundries has a different business mix (specialty processes, no leading edge, fabs in the US, Germany and
Singapore, government funding, a controlling shareholder), and every figure below is taken from GFS's own filings.**

**Why the screen could not price it, found rather than assumed.** `companyfacts` (fetched 2026-09-13) carries namespaces **`dei`,
`ifrs-full` (260 tags) and `srt` only; no `us-gaap`**. GlobalFoundries reports under **IFRS as issued by the IASB, in US dollars**
(20-F FY2025 cover: *"International Financial Reporting Standards as issued by the International Accounting Standards Board ☑"*;
Item 5.E: *"prepared in accordance with International Financial Reporting Standards ("IFRS")"*). Measured (`facts_probe.py`):
`ifrs-full:CashFlowsFromUsedInOperatingActivities`, `PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities`,
`AdjustmentsForSharebasedPayments` and `DepreciationAndAmortisationExpense` each carry **unit USD, annual periods 2019-12-31
to 2025-12-31 (seven), from five 20-F accessions, including the FY2025 20-F `0001709048-26-000022`.**
- **The USD-only unit filter is NOT the cause** (the unit is USD).
- **companyfacts lag is NOT the cause** (FY2025 is ingested), unlike TM, TSM and UMC.
- **The cause is the tag names:** `tools/run.py GFS` returns *"GFS: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED."*
  because its lists carry only US-GAAP element names (`NetCashProvidedByUsedInOperatingActivities`), and `sources.annual()`
  searches `ifrs-full` with those same names. **ERIC's diagnosis, confirmed on a USD filer where the other two causes are absent.**
- **"Short history" is partly true and is not the reason:** seven annual cash-flow periods exist (2019-2020 as comparatives in
  the first 20-F, filed after the **October 2021 IPO**), which covers the framework's five-year default [E2-42] but not a ten-year
  window. **What that does to the width is stated at Q4.**

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

### The earnings currency, established from the filing
- 20-F FY2025 Item 3.D: *"The majority of our sales are denominated in U.S. dollars, and therefore, our revenue is not subject to
  foreign currency risk."* Item 11: *"we have costs, assets and liabilities denominated in foreign currencies, primarily the Euro,
  the Singapore dollar and the Japanese yen"*, hedged with forwards.
- Presentation currency US dollars; revenue by customer headquarters 2025: **United States $3,395M (50.0%)**, EMEA $1,710M, Other
  $1,686M (Note 31). Non-current assets 2025: **Singapore $4,364M, United States $3,608M, Germany $2,137M**, other $488M.
- Cash at 2025-12-31: United States $1,133M, Singapore $436M, other $240M (Note 6).
- **The judgment [E4-15, E3-32]:** revenue billed in dollars, statements in dollars, quote in dollars, cash mostly in the United
  States. **The USD sovereign is the natural pairing**, and no currency conversion enters any yield below. The euro and Singapore
  dollar cost base is a margin exposure, carried to Q4, not a reason to change the rate.

### Sovereign — struck fresh 2026-09-13 through `tools/sources.py` [E4-15, E3-32]
- **Rate used: USD 30-year 5.35%**, US Treasury daily par yield curve, **09/11/2026** (the issuing authority; `sources.sovereign("USD")`
  returned `(5.35, '09/11/2026', 'US Treasury daily par yield curve')`). The brief's 5.35% is confirmed, not inherited.
- **The [E4-28] floor of roughly 10% governs above it** (*"that's true whether short rates are 6 percent or whether short rates are
  1 percent"*).
- FX: none needed (USD earnings, USD quote). ADR: none (ordinary shares listed directly on Nasdaq, 20-F cover: *"Ordinary shares, par
  value US$0.02 per share | GFS | The NASDAQ Global Select Market"*).

### The share count, read by hand and walked forward — the issued-versus-outstanding trap checked explicitly
| date | count | what the filing says | document · accession |
|---|---|---|---|
| 2024-12-31 | 552,912,823 | *"555,888,455 and 552,912,823 shares issued and outstanding as of December 31, 2025 and 2024"* | 20-F FY2025 balance sheet (F-5) |
| **2025-12-31** | **555,888,455** | cover: *"As of December 31, 2025, 555,888,455 ordinary shares, par value US$0.02 per share, were outstanding."* Balance sheet: the same figure *"issued and outstanding"*; Note 17: *"556 million ordinary shares issued and outstanding"* | **20-F FY2025, `0001709048-26-000022`, filed 2026-02-27** |
| 2026-03-13 | −7,344,840 | *"7,344,840 ordinary shares of which were repurchased by the Company at a price equal to the price paid by the underwriters of $40.8450 per share"* (from Mubadala, inside its secondary offering) | 6-K 2026-03-13, `0001709048-26-000043` |
| 2026-03-13 | 549,072,416 | *"549,072,416 ordinary shares ... issued and outstanding as of March 13, 2026"* (information the issuer gave Mubadala) | Mubadala Schedule 13G/A No. 2, `0001140361-26-016895` |
| H1 2026 | about −2.3M | *"the Company repurchased an additional 2.3 million ordinary shares for $ 100 million for a weighted average price of $ 43.88 in open market transactions"* | Q2 2026 interim report, 6-K 2026-08-05, `0001709048-26-000219` |
| 2026-06-01 | 548,700,833 | *"548,700,833 ordinary shares were issued and outstanding"* (AGM record date) | 6-K 2026-06-15, `0001709048-26-000141` |
| **2026-06-30** | **548,751,082** | *"Ordinary shares, $ 0.02 par value, 548,751,082 and 555,888,455 shares issued and outstanding as of June 30, 2026 and December 31, 2025"* | **Q2 2026 interim statements, 6-K 2026-08-05, `0001709048-26-000219`** |
| **agreed 2026-09-03** | **+9,907,399** | *"GF will issue to the DOC 9,907,399 ordinary shares, par value $0.02 per share, of GF (the "Shares"), at an issuance price of $37.85 per share"* | **6-K 2026-09-08, `0001709048-26-000234`** (the latest 6-K) |

- **The ERIC trap, checked, and it does NOT fire.** The cover says *"outstanding"*; the balance sheet says the same number is *"issued
  and outstanding"*; repurchased shares are cancelled, not held in treasury (Note 17: *"On May 28, 2024, our Board of Directors resolved
  to cancel the 3.9 million shares"*; policy, Note 3: *"When the Company repurchases and cancels its own equity shares (treasury
  shares), the amount of consideration ... is deducted against the issued ordinary share capital"*). **Issued equals outstanding at
  every date in the table.** No treasury balance to exclude.
- **Count used: 558,658,481** = 548,751,082 (2026-06-30, filed) + 9,907,399 (the Department of Commerce issuance agreed 2026-09-03).
  **The larger count is used deliberately**: the agreement is signed and the 6-K says the shares *"will"* be issued; no filing
  read confirms the issuance completed by 2026-09-11, and leaving them out would understate the cap by 1.8%. **Arithmetic,
  recorded and not over-read:** 9,907,399 × $37.85 = **$375.0M**, the exact amount of *"an expected $375 million grant by the U.S.
  Department of Commerce, pursuant to a letter of intent"* for the quantum programme (Q2 2026 release, 6-K `0001709048-26-000218`).
  **No filing read states that the shares are the consideration for that grant**; the match is arithmetic only. Carried to Q3 and Q4.
- **Not in the count, stated:** open-market repurchases after 2026-06-30 under the *"approximately $ 100 million"* left on the
  authorisation (at most ~2.1M shares at $46.95; no filing reports any); 8.7M RSUs, 3.0M PSUs and 0.3M options outstanding at
  2025-12-31 (Item 6.B), carried to Q4 as SBC; no convertible or warrant found. **No split** (Yahoo `events.splits` null), so
  `close × shares(measurement) × splits after measurement` holds trivially.

### The price and the cap (aggregator for live quotes only, flagged)
- **Price US$46.95**, GFS Nasdaq close **2026-09-11** (Yahoo Finance chart API, `regularMarketTime` 2026-09-11 20:00 UTC; **aggregator,
  flagged**; `px.py` / `prices_2026-09-13.json`).
- **Cap = US$46.95 × 558,658,481 = US$26,229M** (US$25,764M on the filed 2026-06-30 count alone).
- **Price context, from filings and the same flagged series:** Mubadala sold to the public at **$50.75 (May 2024)** and **$42.00 (March
  2026)**; the company bought from Mubadala at $50.75 and **$40.845**; the Department of Commerce issuance is priced at **$37.85**;
  Mubadala's Form 144 of **2026-05-26** reports **22,000,000 shares with an aggregate market value of $1,979,120,000** ($89.96 a share).
  The quote went from $41.59 (2026-03-12) to **$89.96 (2026-05-26)** and back to **$46.95**: a doubling and a halving inside six months.

### Controlling shareholder, recorded at Step 0 because it moves the count and the cap
| date | Mubadala's shares | % | source |
|---|---|---|---|
| 2025-12-31 | 450,387,613 | 81.0% | 20-F FY2025 Item 7.A |
| 2026-03-31 | 423,042,773 | 77.05% | Schedule 13G/A No. 2, `0001140361-26-016895` |
| **2026-06-30** | **399,573,756** | **72.82%** | **Schedule 13G/A No. 3, `0001140361-26-032099`, filed 2026-08-10** |

FMR LLC 69,848,380 shares, 12.7% at 2026-06-30 (Schedule 13G/A, `0000315066-26-002033`). **Free float excluding Mubadala about
27%.** Control, the Shareholder's Agreement and the related-party terms are read at Q3.

### The filing was read — not tagged data **[E3-27, E4-14]**
- [x] MD&A (Item 5: operating results, single-sourced mix, LTAs, shipment utilisation, ASP, liquidity, cash flows) [x] cash-flow
  statement incl. detail lines (F-8, FY2025; F-9/F-8/F-6/F-8 in FY2021-FY2024) [x] footnotes (government grants, trade payables and
  contract liabilities, long-term debt, issued capital, share-based payments, related parties, segments and geography, customer and
  supplier concentration, subsequent events)
- **Primary document: Form 20-F, fiscal year ended 2025-12-31, filed 2026-02-27, accession `0001709048-26-000022`, `gfs-20251231.htm`,
  CIK 0001709048.**
- **Also read:** 20-F FY2024 `0001709048-25-000024` · FY2023 `0001709048-24-000013` · FY2022 `0001709048-23-000013` · FY2021
  `0001709048-22-000008` (which carries 2019 and 2020) · the IPO prospectus 424B4 `0001193125-21-313344` · every 6-K and exhibit
  2021-11-30 to 2026-09-08 (73 filings, `k/`), including the quarterly earnings releases and interim reports, the two Mubadala
  secondary offerings (424B7 2024-05-24 and 2026-03-12), the CHIPS Direct Funding Agreement release (2024-11-20), the Term Loan A
  prepayment (2025-01-02), the IBM settlement release (2025-01-02), the revolving credit agreement (2026-08-27) and the Department
  of Commerce Securities Issuance Agreement (2026-09-08); Schedules 13G/A of Mubadala and FMR; Form 144 filings 2026.
- **Figure cross-checked against the filed statement:** **Net cash provided by operating activities $1,731M for 2025** in the audited
  CONSOLIDATED STATEMENTS OF CASH FLOWS (F-8) equals the MD&A table (*"Cash provided by operating activities | $ | 1,731"*) and
  `companyfacts` `ifrs-full:CashFlowsFromUsedInOperatingActivities` 2025-12-31 **USD 1,731,000,000**. **One restatement found
  between vintages and resolved toward the later filing:** 2020 operating cash is **$1,005.9M** in the FY2021 20-F and **$1,004M** in
  the FY2022 20-F (re-presented in millions with interest and tax paid reclassified); the difference is immaterial and the later
  figure is used.

## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### The business, from the filing: a specialty foundry paid per wafer, on four sites in three countries
**Source: 20-F FY2025 Items 4 and 5, Notes 18, 31, 32; earlier 20-Fs for the series; quarterly earnings releases (6-K EX-99.1,
`qtr.py` / `qtr_out.json`).** Item 5: *"We generate the majority of our revenue from volume production and sales of finished
semiconductor wafers, which are priced on a per-wafer basis for the applicable design. We also generate non-wafer revenue from
rendering non-recurring engineering ("NRE") services, mask production, process qualification, pre-fabrication services such as
bump, test, and packaging, and earning intellectual property licenses and royalties."* Wafer fabrication was *"approximately 89%
of our net revenue in 2025."*

**What it does NOT make:** the leading edge. FY2021 20-F: *"we shifted our R&D efforts to focus on technologies where we can deliver
a highly-differentiated solution and discontinued our R&D-intensive single-digit node program"*, and the depreciation change of the
same year was justified as *"consistent with the Company's continuing portfolio shift from leading-edge to feature-rich trailing edge
technologies."* AMD's FY2025 10-K (read in the TSM run) buys its >7nm wafers *"primarily"* from GF and its ≤7nm wafers from TSMC.
**Its platforms** (Item 4): FinFET (12/14nm), FDX (22FDX, FD-SOI), RF-SOI, SiGe, RF GaN, BCD and high-voltage BCD, power GaN,
silicon photonics, feature-rich CMOS from 22nm to 180nm, and since 2025 processor IP (MIPS, and Synopsys' ARC business from June 2026).

**Revenue by end market, US$M** (20-F FY2025 Item 4; the FY2022 and FY2023 20-F text carries no dollar table, recorded as a limit):

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| Smart Mobile Devices | 3,023 (41%) | 3,048 (45%) | **2,678 (39%)** |
| Automotive | 1,046 (14%) | 1,206 (18%) | **1,410 (21%)** |
| Home and Industrial IoT | 1,604 (22%) | 1,267 (19%) | **1,189 (18%)** |
| Communications Infrastructure & Data Center | 863 (12%) | 577 (9%) | **745 (11%)** |
| Non-wafer revenue | 856 (11%) | 652 (10%) | **769 (11%)** |
| **Total** | **7,392** | **6,750** | **6,791** |

**Revenue, gross margin, wafer shipments and revenue per wafer** (revenue and wafer revenue from the 20-F statements and Note 18,
wafer revenue on the FY2024 re-presentation, *"access fees and other have been reclassified from wafer revenue to non wafer
revenue"* and *"Beginning in the fourth quarter 2023, underutilization charges have been included in wafer revenue"*; shipments are
the sum of the four quarterly release figures, thousands of 300mm-equivalent wafers):

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | H1 2026 |
|---|---|---|---|---|---|---|---|---|
| net revenue, US$M | 5,813 | 4,851 | 6,585 | 8,108 | 7,392 | 6,750 | 6,791 | 3,420 |
| gross margin | −9.2% | −14.7% | 15.4% | 27.6% | 28.4% | 24.5% | 24.9% | 28.0% |
| wafer revenue, US$M | | | | 7,301 | 6,536 | 6,098 | 6,022 | |
| shipments, k 300mm eq. | | | ~2,400 (filed: 2022 *"a 4.1% increase"*) | **2,472** | **2,211** | **2,124** | **2,345** | 1,204 |
| wafer revenue per wafer, US$ | | | | 2,954 | 2,956 | 2,871 | **2,568** | |
| **filed ASP change** | | | | **+17%** (*"ASP per wafer increased 17% year over year"*) | not stated; arithmetic **+0.1%** | **−3%** (*"the average selling price per wafer decreased by 3%"*) | **−10.4%** (*"a 10.4% decrease in average selling prices"*) | |
| **filed shipment utilisation** | 70% (300mm fabs) | 84% (300mm) | 106% (300mm) | 103% (300mm) / **101% (global fabs)** | **81%** | **77%** | **86%** | |

*(Quarterly shipments: 2022 625 / 630 / 637 / 580; 2023 511 / 573 / 575 / 552; 2024 463 / 517 / 549 / 595; 2025 543 / 581 / 602 / 619;
2026 579 / 625. The arithmetic ASP matches the filed changes: 2,871 / 2,956 = −2.9%; 2,568 / 2,871 = −10.6%. The utilisation basis
changed from "300mm fabs" to "global fabs" in the FY2023 20-F; both 2022 figures are filed.)* **2025 units were 5.1% below 2022.**

**Customer concentration** (Item 3.D and Note 32): *"Our ten largest customers in 2025, 2024 and 2023 accounted for approximately 63%,
65% and 72% of our wafer shipment volume"* (73% in 2019 and 2020, 67% in 2021, 70% in 2022). *"Customer A amounted to 16.4 %, 15.7 % and
17.0 % of total wafer revenue ... Customer B accounted for less than 10% of total wafer revenue in both 2025 and 2023, and 10.7 % in 2024.
Customer C amounted to 13.9 % of total wafer revenue in 2025."* The customers are named only as the top ten by volume: FY2024 20-F,
*"AMD, Cirrus Logic International (U.K.) Limited, Infineon Technologies AG, Media Tek Inc., NXP Semiconductors N.V., Qualcomm Global
Trading Pte. Ltd ("Qualcomm"), Qorvo International Ptd. Ltd, Samsung, Skyworks Solutions, Inc. and Sony Semiconductor Manufacturing
Corporation"* (FY2021 also pSemi; FY2022 and FY2023 Marvell). **Which one is Customer A is not filed.**

**The single-source claim, and what it covers** (Item 5): *"We define single-sourced products as those that we believe can only be
manufactured with our technology or cannot be manufactured elsewhere without significant customer redesigns"*, and *"single-sourced
business ... represented approximately 63% of wafer shipment volume in 2025."* The series: **61% (2020), 62% (2021), 65% (2022), 62% (2023),
64% (2024), 63% (2025).** **Three things about the number, stated so it is not over-read:** it is the company's own belief (*"we believe"*),
not a customer's statement; it measures **volume**, not revenue or margin; and FY2024 changed the name of the measure from single-sourced
*"business"* to single-sourced *"design wins"* in one sentence and kept *"business"* in another (a prompt carried to Q3, [E2-49]).

**Long-term agreements** (Item 5): *"Many of these contracts include customer advanced payments and capacity reservation fees in order to
secure future supply. As of December 31, 2025, the aggregate remaining revenue commitment reflected by LTAs was approximately $11
billion."* The filed series: **~$21bn (2021) → ~$22bn (2022) → ~$20bn (2023) → ~$14bn (2024) → ~$11bn (2025)**, and FY2023 and FY2024:
*"In light of current demand dynamics, our ability to enter into LTAs has diminished."* Contract liabilities (customer prepayments):
US$135M (2020) → **1,901 (2021)** → 1,918 → 1,983 (2023) → 1,584 → **1,230 (2025)** (Note 12 each year). Carried to Q2 and Q4.

**Capacity and plant** (Item 4.D): *"at the end of 2025 our total installed capacity was approximately 2.8 million wafers per annum"* (2,618
kwpa at 2023-12-31); four sites (Malta NY, Burlington VT, Dresden, Singapore) plus a non-wholly-owned China fab in the technology table;
*"more than 7,000 tools"*. Non-current assets 2025: Singapore US$4,364M, United States 3,608, Germany 2,137. The US fabs are *"Trusted
Foundry accredited"* (CHIPS release, 2024-11-20). **Cost is mostly fixed**: Item 5, *"we incur significant costs regardless of the number
of wafers we actually produce. These fixed costs include staffing, electricity, infrastructure, depreciation and maintenance costs"*;
depreciation and amortisation US$1,314M in 2025 (19.3% of revenue) after US$2,522M in 2020.

### Unit economics in my own words, no management language
A chip designer (an RF front-end maker for phones, an automotive microcontroller or power-chip maker, AMD for its older-node parts, an
optical-transceiver maker) designs a chip for one of GF's particular processes and pays GF per finished wafer. **The price depends on the
process** (a silicon-photonics or RF-SOI wafer is worth more than a plain 180nm CMOS wafer), on the contract (many big customers signed
multi-year agreements in 2021-2022, paying cash up front to reserve capacity and paying penalties when they took less), and on whether the
customer could move the design elsewhere. **Revenue is wafers shipped times that price; the cost is a plant whose depreciation, power and
people are there whether or not the wafers are made**, so the margin moves with how full the fabs are. When the fabs were overfull in
2021-2022, prices rose 17% and customers prepaid US$1.9bn; when they emptied to 77-81% in 2023-2024, contracts held the price in 2023 and
then the price fell 3% and 10% as those contracts rolled off and customers with two qualified foundries renegotiated (*"pricing
adjustments where customers are dual sourced"*, Item 5). The cash goes into keeping the tools current, into new capacity partly paid for
by governments (the US, New York, Singapore, the EU), and since 2024 into buybacks from the controlling shareholder and into buying
processor-IP and photonics businesses.

### The scarce input this business controls
**Qualified specialty processes that customers' designs are built on, so that moving a design means a redesign; together with scaled
capacity located outside China and Taiwan, some of it accredited to make chips for the US government.** The filing claims the first as
*"a significant number of products that can only be sourced from us"* and the second as *"We believe that our global footprint is one of
our key advantages, appealing to customers seeking geographically diversified suppliers."* **Both are the company's own claims and are
tested at Q2 against its customers' and competitors' filings.** What Q1 can say from the filing alone: the input is **not the leading-edge
node** (abandoned in 2018-2019), **not a patent position** (*"approximately 6,400 U.S.-issued patents"*, cross-licensed with *"AMD,
Samsung, TSMC and IBM"*), and it is partly **a location** that governments are paying to create.

### Will the fundamentals look broadly the same in ten years?
- **The model: yes.** Per-wafer foundry manufacturing for chip designers has run since GF's founding in 2009 (*"GF was established in 2009
  when a wholly-owned subsidiary of Mubadala, acquired Advanced Micro Devices, Inc.'s ("AMD") manufacturing operations in Dresden"*, Item
  4.A), and the mature and specialty processes change slowly (the FY2021 useful-life change rests on *"the ability to re-use production
  equipment over several technology cycles"*).
- **The mix: already moving, and by acquisition as well as by market.** Smart Mobile went 45% → 39% of revenue in one year and Automotive
  14% → 21% in two; 2025-2026 added five acquisitions (below) that put GF into licensing processor IP, which is a different business.
- **[E3-31]'s "constant change" clause is live in a narrower form than at TSMC**: GF does not re-buy a node every two years, but its FY2025
  20-F describes a strategy of pursuing *"physical AI"* and *"a comprehensive processor IP suite"*, and the price of its most-shipped
  application (smart mobile RF) fell on dual-sourcing in 2025. **Carried to Q2's [E4-04] test by name, not discharged here.**

### The perimeter in the window, from the filings, with dates (not from memory)
**Divestitures, all agreed before the IPO:**
- **Fab 3E, Singapore (200mm), to Vanguard** — *"on December 31, 2019, we sold our Fab 3E facility and operations in Tampines, Singapore to
  Vanguard for $236 million"* (FY2021 20-F). Before the five-year window.
- **ASIC business (Avera) to Marvell, 2019** — *"Proceeds from sale of fabrication facilities and ASIC business | 832,627"* thousand in 2019
  (FY2021 20-F cash-flow statement). Before the window.
- **East Fishkill (EFK) to ON Semiconductor** — agreed April 2019 (*"in return for $400 million in consideration and $30 million for a
  technology license"*), **completed 2022-12-31**: *"the Company completed the sale of the EFK business for a total purchase price of $ 406
  million, of which $ 170 million was received in prior years, and the remaining $ 236 million was received in January 2023"*; gain US$403M
  in 2022. **Inside the five-year window, and not separately disclosed**: no EFK revenue, profit or cash flow is filed (*"we have transferred
  a number of technologies from the EFK facility to our other global manufacturing sites to ensure continuous supply to key customers"*).
  **The gain is non-cash inside operating cash (adjusted out) and the proceeds sit in investing, so neither enters owner earnings; EFK's
  operating contribution in 2021-2022 cannot be rebuilt from any filing.** Handled at Q4 by showing the three-year 2023-2025 window, which is
  wholly on the post-EFK perimeter.

**Acquisitions, all completed:**

| deal | completed | consideration | document |
|---|---|---|---|
| Tagore Technology (GaN IP) | 2024 | inside *"Acquisitions, net of cash acquired (69)"* | 20-F FY2024 |
| **SMP**, remaining 51% from Broadcom's Avago Singapore | **2025-01-02** | **US$64M** | 20-F FY2025 Note 5 |
| **MIPS Holdings** (processor IP) | **2025-08-13** | **US$226M** (US$215M cash, US$11M replacement awards) | Note 5 |
| **InfiniLink** (optical connectivity design) | **2025-11-14** | **US$48M** | Note 5 |
| **Advanced Micro Foundry** (Singapore silicon photonics foundry) | **2025-11-18** | **US$453M** cash | Note 5 |
| **Synopsys' ARC Processor IP Solutions** | agreed 2026-01-13, **completed 2026-06-01** | **US$455M** (US$440M cash, US$4M contingent, US$11M replacement awards) | 20-F Note 33; Q2 2026 interim report |

**About US$1.3bn in eighteen months**, of which US$791M of consideration closed in 2025 (*"Acquisitions, net of cash acquired | ( 682 )"* in the 2025 cash-flow statement). Note 5: *"the effects of the acquisitions were not material to the
Company's consolidated financial statements"*; the auditor excluded all four 2025 targets from internal-control testing at under 1% of assets
and revenue each (AMF *"approximately 1%"* of assets). **Not a perimeter change for the owner-earnings mean on revenue or cash; carried to
Q3 as capital allocation and to Q4 as capital outlays outside capex.**

**Other filed arrangements, no perimeter change:** *"through a strategic partnership with a China-based foundry we are proceeding with plans
to enable our customers to access GF production ... to serve their domestic Chinese demand"* (Item 4.B; the partner is not named in the
text read, and the technology table's footnote says *"Not a wholly owned Fab"*). **No merger or combination with another foundry agreed,
completed or abandoned in any filing read** (recorded sweep: the five 20-Fs and every 6-K exhibit 2021-11-30 to 2026-09-08 for "merger",
"combination", "UMC", "United Microelectronics" and "Tower"; the only hits are competitor lists in risk factors, the IPO prospectus and the 2022 business
update). **The revolving credit agreement of 2026-08-21 and the Department of Commerce share issuance (2026-09-03) are
financing events, recorded at Q3 and Q4.**

### [E4-46] — five minutes, not five months
The mechanism fits the paragraph above and every figure is filed. **Whether the specialty processes are a franchise, what the plant costs
to maintain, and what the government money and the controlling shareholder do to the owner's share, are Q2, Q3 and Q4 questions with named
documents, not a Q1 competence gap.**

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *GF makes money one wafer at a time on specialty, not leading-edge, processes, at a price set by contract and by whether the customer can
  move the design, on a mostly fixed cost base whose margin follows utilisation. The single-source share (63% of volume) is the company's
  belief and is tested at Q2; the [E3-31] "constant change" clause is live in its narrower form (a mix shift and a move into processor IP)
  and is carried to Q2's [E4-04] test by name.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**Pre-registered before the row was built (operator rule 9, [E4-26]).** Two hypotheses are at risk of being favoured, in opposite
directions, and both are stated so the evidence can refute them: (a) *"GFS is UMC's OUT with a lower margin"*, the anchoring risk of
running this file hours after UMC closed at Q2; and (b) *"GFS is the foundry the precedents did not reach"*: 63% single-sourced volume
by its own measure, specialty processes UMC does not run, fabs outside China and Taiwan, Trusted Foundry accreditation, and governments
paying to put capacity where GF already is. **So the disconfirming evidence hunted hardest is: customers' own filings saying GF has no
substitute (against (a)), and GF's filed price and return through the 2023-2025 utilisation trough (against (b)).** TSMC failed only
[E4-04]; UMC failed [E3-03](2) and [E2-44](1). GFS is tested on its own filings, criterion by criterion.

### [E3-03], the three criteria, in the customers' and competitors' own filings
*"(1) is needed or desired; (2) is thought by its customers to have no close substitute and; (3) is not subject to price regulation."*

**(1) Needed or desired: YES.** US$6.8bn of revenue; top-ten customers by volume include AMD, Qualcomm, Samsung, Infineon, NXP, MediaTek,
Skyworks, Qorvo, Cirrus Logic and Sony Semiconductor (20-F FY2024 Item 4).

**(2) Thought by its customers to have no close substitute: MIXED ON THE WORDS, NO ON THE CONDUCT.** The customers' filed words, read in full
(screen `fts.py` / `fts_out.json` via `tools/sources.py:fts_count()`, then every hit document opened; latest annual reports in `peers/`):
- **For the claim — switching is costly where a design is built on GF's process:**
  - **Cirrus Logic**, 10-K FY2026 (`0000772406-26-000018`): wafers *"primarily supplied by GLOBALFOUNDRIES Inc., ("GlobalFoundries") and Taiwan
    Semiconductor Manufacturing Company, Limited ("TSMC")"*; *"If we experience manufacturing problems at a particular location ... we would be required to
    transfer manufacturing to a backup supplier. Transferring from a primary supplier to another facility would likely result in increased
    production costs and a delay in production. Further, such a transition may not be possible, particularly in a supply constrained
    environment. There are only a few foundries that are currently available for certain advanced processing technologies that we utilize."*
    And the location claim, in a customer's words: *"We recently joined our largest customer's American Manufacturing Program and are working
    with both our customer and GlobalFoundries to develop new process technologies for our products, including our efforts to manufacture for
    the first time at the Malta, New York facility."*
  - **AMD**, 10-K FY2025 (`0000002488-26-000018`): *"we rely primarily on GLOBALFOUNDRIES Inc. (GF) for wafers for microprocessor and GPU products
    manufactured at process nodes larger than 7 nm"*; *"GF, with respect to wafer purchases for our HPC products at the 12 nm and 14 nm technology
    nodes."*
  - **Navitas**, 10-K FY2025 (`0001821769-26-000007`): *"we consider our collaboration with United States based foundry partners, specifically
    GlobalFoundries for GaN and X-Fabs for SiC, to be a competitive advantage, as we believe that foreign semiconductor companies and companies
    that rely on foreign supply chains will be disadvantaged."*
- **Against the claim — the same customers name the substitutes, and GF names its own:**
  - **Cirrus Logic** buys from **both** GF and TSMC; its GF agreement is a contract that *"set wafer pricing ... through calendar year 2026"* and
    *"The Capacity Reservation Agreement requires GlobalFoundries to provide, and the Company to purchase, a defined number of wafers on a
    quarterly basis ... subject to shortfall payments"*, amended in February 2025 to respread the remaining quantities. **The customer paid
    a US$60M capacity reservation fee and prepaid US$195M *"in an effort to alleviate some of our future expected supply constraints"* (2021),
    not because no one else could make the part.**
  - **AMD**: *"We are party to a wafer supply agreement with GF where GF will provide a minimum annual capacity allocation to us and set pricing
    through 2026"*; and on its foundries in general, they *"could choose to prioritize capacity for other customers, increase the prices that they
    charge us on short notice"*. **AMD's GF dependence is its 12/14nm legacy products; its growth products are at TSMC.** The WSA's pricing ends
    in 2026.
  - **Qualcomm**, 10-K FY2025 (`0000804328-25-000085`): *"The primary foundry suppliers for our various digital, analog/mixed-signal, RF and PM
    integrated circuits include Taiwan Semiconductor Manufacturing Company (TSMC), Samsung Electronics and Global Foundries."* No split filed.
  - **Himax**, 20-F FY2025 (`0001104659-26-035507`): *"We have obtained our foundry services from TSMC, UMC, Vanguard, Macronix, Globalfoundries
    Singapore, PSMC, Nexchip and SKHYSI in the past few years."* **GF is one of eight** at high-voltage CMOS.
  - **Navitas**, same filing: GF is itself **the substitute** being qualified for TSMC's GaN (*"For GaN products, our existing wafer fabrication
    partner is TSMC ... Our US based GaN fabrication partner is GlobalFoundries"*, alongside Powerchip). GF wins that business by being a
    close substitute.
  - **Tower Semiconductor**, 20-F FY2025 (`0001178913-26-002318`): *"We compete most directly in the specialty segment with foundries such as
    GlobalFoundries (mainly in the RF space), Vanguard Semiconductor, DongBu, X-Fab, and Hua Hong Semiconductor. We also compete in certain areas
    with ... TSMC ... UMC ... and SMIC ... each also offers specialty process technology and capacity."* **Intel**, 10-K FY2025: *"Other Intel
    Foundry competitors include GlobalFoundries, UMC and SMIC, which primarily focus on mature process technologies."*
  - **GF's own 20-F FY2025**: *"Key competitors include Taiwan Semiconductor Manufacturing Company, Limited ("TSMC"), United Microelectronics
    Corporation ("UMC") and Semiconductor Manufacturing International Corporation. We also compete with the foundry operation services of some
    IDMs, such as Texas Instruments, Inc. ("Texas Instruments"), Samsung ... and, more recently, Intel. Other smaller dedicated foundry
    competitors include HuaHong Group, X-FAB Silicon Foundries, Tower Semiconductor Ltd., Vanguard International Semiconductor Corporation, and
    Powerchip."* And the sentence that decides it: **Smart Mobile Devices *"decreased by 12.1% year-over-year, primarily due to lower
    underutilization payments from customers and pricing adjustments where customers are dual sourced."*** GF's largest end market (39%) is
    where dual sourcing moved the price.
- **The single-source number, read against itself:** *"single-sourced business ... represented approximately 63% of wafer shipment volume in
  2025"* is the company's belief about **volume**; **37% of volume is by GF's own definition business that can be made elsewhere without
  significant redesign**, and the 63% is defined per product (*"cannot be manufactured elsewhere without significant customer redesigns"*), so
  it describes the cost of moving an existing design, not the competition for the next one: *"If we are unable to fill the funnel and convert
  enough opportunities into design wins and ultimately awards due to differentiation, pricing, competition, or any other reasons, there will be
  a material adverse impact"* (Item 3.D). **A design-level lock-in that is re-competed at every design is [E4-04]'s question, taken below.**

**(3) Not subject to price regulation: YES**, with the regime noted at [E2-59] below: US export controls, CHIPS funding conditions and Trusted
Foundry accreditation shape where GF may sell and build, not what it may charge.

### [E3-43]'s demonstration test — the tie-breaker the corpus supplies for criterion (2)
*"The existence of all three conditions will be demonstrated by a company's ability to regularly price its product or service aggressively and
thereby to earn high rates of return on capital."* **Return on average parent equity** (`row.py`, filed statements): **−16.7% (2020), −3.4%
(2021), 16.2% (2022), 9.7% (2023), −2.4% (2024, after a US$935M impairment; ~6.1% before it), 7.8% (2025)**; **five-year mean 5.6%**, without
leverage (net cash, Q4). **Accumulated deficit US$12,381M at 2025-12-31** (balance sheet). The one year above 10% is 2022, the shortage year, at
101-103% utilisation. **Not demonstrated.** Where the words of criterion (2) are mixed, the corpus's own test of it is the price and the return,
and both say no.

### [E2-44], the two-characteristic test — the decisive section
**(1) Can it raise prices "even when product demand is flat and capacity is not fully utilized"? NO. The price held for one year on contracts,
then fell twice, the second time as utilisation recovered.**

| | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| filed shipment utilisation (global fabs) | 101% | **81%** | **77%** | 86% |
| shipments, k 300mm eq. | 2,472 | 2,211 | 2,124 | 2,345 |
| **filed ASP change** | **+17%** | arithmetic +0.1% (not stated) | **−3%** | **−10.4%** |
| wafer revenue per wafer, US$ | 2,954 | 2,956 | 2,871 | 2,568 |
| contract liabilities (prepayments), US$M, year-end | 1,918 | 1,983 | 1,584 | 1,230 |
| LTA remaining revenue commitment | ~$22bn | ~$20bn | ~$14bn | ~$11bn |
| gross margin | 27.6% | 28.4% | 24.5% | 24.9% |

- **2023, the first trough year, held the price only because customers were contracted to pay for capacity they did not take.** From Q4 2023
  *"underutilization charges have been included in wafer revenue"* (FY2024 Note 17); Item 5: *"From time to time our wafer revenue consists of
  restructuring or underutilization payments from customers unable to meet their volume commitments."* The filings give no amount. **The
  price in 2023 is partly a penalty, not a price.**
- **2024: −3%** at 77% utilisation, *"largely due to shifts in the end market mix"*.
- **2025: −10.4%** while utilisation **rose** to 86%: *"primarily attributable to lower pricing from certain customers in specific end markets, as
  well as lower underutilization payments from customers under long term agreements"*, and in Smart Mobile, *"pricing adjustments where
  customers are dual sourced."* **As the 2021-2022 contracts rolled off, the price re-set to what the customers could get elsewhere.**
- **[E4-37]'s agony test reads as agony**: contract restructurings (Cirrus Logic's February 2025 amendment respreading quantities), falling
  underutilization receipts, and price adjustments to keep dual-sourced business.
- **2019-2020, the other low-utilisation years (70% and 84% at 300mm):** no ASP filed; gross margin −9.2% and −14.7% (on the pre-2021 depreciation
  lives, Q4).

**(2) Does dollar volume grow "with only minor additional investment of capital"? NO.** Revenue **US$5,813M (2019) → US$6,791M (2025), ×1.17**,
and **×1.03 from 2021**, after capex of **US$9,342M** (2019-2025; US$1,124M of grants received against it) and **US$1.3bn of acquisitions** in
2024-2026. Capex ran **26.8% and 37.7% of revenue in 2021-2022** (1.09× and 1.88× D&A) to meet the shortage; units in 2025 were 5.1% below 2022.
**Capital went in; volume did not come out.**

### [E2-58] — the commodity equation, in GF's own words
*"persistent over-capacity without administered prices (or costs) equals poor profitability"*; the one exception is *"a cost advantage that is
both wide and sustainable."* GF's 20-F FY2025 Item 3.D names the mechanism at its own nodes: *"the Chinese semiconductor industry, with
significant government support, has accelerated building its own foundry capacity, and shifted to focus domestic manufacturing on mature nodes
(i.e., 28nm and larger technology nodes), and China's foundry capacity is expected to grow faster than expected demand at those nodes"*;
*"China's decision to build capacity for China will likely have the dual effect of limiting the Chinese market (which will have a preference for
domestic sourcing) for other global suppliers like us and significantly increasing the competition we face globally"*; and *"the business we do
around the world outside of China, in markets in which Chinese semiconductor manufacturers are our direct competitors, also represents a
significant portion of our business."* **SMIC and Hua Hong added 49% to their capacity 2022-2025 on their own releases** (UMC run, cited, not
re-fetched). **A wide and sustainable cost advantage is not shown**: GF's gross margin is below UMC's in every year 2021-2025 and within two
points of Tower's (row below).

### [E2-59] — the part of the position that belongs to a regime
Much of what is distinctive about GF is location: *"Customer demand for diversified global semiconductor supply including non-China and non-Taiwan
based suppliers"* (Item 5), Trusted Foundry accreditation, Navitas's *"foreign supply chains will be disadvantaged"*, Cirrus Logic's customer's
*"American Manufacturing Program"*, and US$1.5bn of CHIPS funding plus US$570M from New York. **Those advantages are conferred by export controls,
tariffs and subsidy programmes that GF does not control**, and the corpus says what a regime moat is: the moat *"belongs to the regime, and 'That
day is gone' is how it ends."* **The Department of Commerce's 2026 decision to take GF shares at US$37.85 in exchange for what was announced as
a grant** (Step 0) shows the regime's terms can change after the fact. Recorded as a regime dependence, not scored as a franchise.

### [E4-04] — must the moat be continuously rebuilt?
*"A moat that must be continuously rebuilt will eventually be no moat at all."* **Scope test, part by part:**
1. **Does the spending defend the same advantage, or buy its replacement?** **Mostly it buys the next design win.** The lock-in is per product
   (*"cannot be manufactured elsewhere without significant customer redesigns"*); when a customer's product reaches end of life the design is
   re-competed (*"a reduction of revenue from wafer shipments to certain aerospace and defense ("A&D") customers with end-of-life products"*, Item
   5, 2025), and GF describes its commercial model as a *"design funnel to design award process"*. Unlike TSMC, GF does not re-buy a node every
   two years; like TSMC, the thing earning the price has to be won again. **What persists** is real and stated for the defence: the process
   platforms themselves (22FDX, RF-SOI, SiGe, silicon photonics) run for many product generations (the useful-life change of 2021 rests on
   *"the ability to re-use production equipment over several technology cycles"*), and the Trusted Foundry and US-site position.
2. **Does a lapse destroy the structure, or merely narrow it?** **The 2018-2019 record answers it for the leading edge**: GF stopped the
   single-digit node programme and lost that position entirely (AMD's leading products moved to TSMC). **For the specialty platforms the filed
   record is too short to answer**: seven annual periods since 2019, one shortage and one trough.
- **Direction [E4-32]: narrowing on every contractual metric** (LTA book ~$22bn → ~$11bn; prepayments US$1,983M → US$1,230M; underutilization
  receipts *"lower"*; price −10.4%), **with the single-source share flat at 61-65%** and new growth in automotive (+16.9%) and silicon photonics
  (Communications Infrastructure & Data Center +29.1% in 2025). **Units [E4-55]: 2,472k → 2,345k (2022-2025), −5.1%.**

### [E2-45] — the attacker's test
*"how I would like, assuming I had ample capital and skilled personnel, to compete with it."* Three attackers with capital are on file: **Tower**
(*"GlobalFoundries (mainly in the RF space)"* named as its most direct specialty competitor; capex 28.4-31.2% of revenue 2023-2025, row below),
**the Chinese mature-node build** (GF's own risk factor), and **Intel Foundry**, which names GF as a competitor. **GF's own response to an attacker is
filed: in March 2026 it sued Tower** (*"GlobalFoundries filed three lawsuits against the Company in the U.S. International Trade Commission and the
U.S. District Court for the Western District of Texas, alleging infringement of certain of its patents. The Company disputes these claims"*, Tower
20-F FY2025). A patent suit is a defence of the moat [E5-23], and it confirms the attacker is close enough to be sued; its outcome is not filed.

### THE COMPETITOR ROW — required [E3-28]. Same metric, same window, filing-sourced.

**Gross margin %:**

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| **GlobalFoundries** | −9.2 | −14.7 | 15.4 | 27.6 | 28.4 | 24.5 | **24.9** |
| TSMC | 46.0 | 53.1 | 51.6 | 59.6 | 54.4 | 56.1 | 59.9 |
| UMC | 14.4 | 22.1 | 33.8 | 45.1 | 34.9 | 32.6 | 29.0 |
| Tower Semiconductor | 18.6 | 18.4 | 21.8 | 27.8 | 24.8 | 23.6 | 23.2 |
| SMIC | *not SEC* | | | 38.0 | 19.3 | 18.0 | 21.0 |
| Hua Hong | *not SEC* | | 27.7 | 34.1 | 21.3 | 10.2 | 11.8 |
| Intel Foundry | *operating margin only* | | | | −38 | −76.8 | −57.9 |
| Vanguard International | *company IR rung HTTP 403 in the UMC run; MOPS not attempted* | | | | | | |
| Samsung Foundry | *not disclosed in any document on the shelf (TSM run)* | | | | | | |
| X-FAB, Powerchip | *not SEC registrants; not attempted in this run* | | | | | | |

**Return on average parent equity %:**

| | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean 2021-25 |
|---|---|---|---|---|---|---|---|
| **GlobalFoundries** | −16.7 | −3.4 | 16.2 | 9.7 | −2.4 | 7.8 | **5.6** |
| TSMC | 29.6 | 29.7 | 39.3 | 26.9 | 30.2 | 35.6 | 32.3 |
| UMC | 10.7 | 21.0 | 30.5 | 17.9 | 13.8 | 11.0 | 18.8 |
| Tower Semiconductor | 5.9 | 9.7 | 15.1 | 24.0 | 8.2 | 7.9 | 13.0 |

**Capex % of revenue:** GFS 13.3 · 12.2 · 26.8 · 37.7 · 24.4 · 9.3 · **10.6** (2019-2025, PP&E plus intangibles, gross of grants; the TSM run's
10.1 for 2019 is PP&E only) · Tower 15.5 · 24.8 · 20.8 · 21.8 · 31.2 · 30.4 · 28.4 · UMC 11.1 · 14.9 · 22.6 · 28.7 · 41.1 · 38.1 · 20.1 · TSMC
43.0 · 37.9 · 52.9 · 47.8 · 43.9 · 33.0 · 33.4 · SMIC 91% (2024) and 87% (2025).

*Sources: GFS from its filed statements (`row.py` / `row_out.json`; 20-F FY2021-FY2025, accessions at Step 0; the 2019-2020 figures from the FY2021
20-F and FY2022 re-presentation); **Tower recomputed here** from `companyfacts` us-gaap through its 20-F FY2025 `0001178913-26-002318` (it matches
the UMC run's row to the decimal; 2023 ROE includes the Intel merger-termination fee); TSMC and UMC from the TSM and UMC runs' filing-sourced
tables (TSMC 20-F `0001628280-26-025362`, UMC 20-F `0001193125-26-193757`); SMIC and Hua Hong from their own releases and HKEX filings as recorded in
the UMC run (**source rule: neither is an SEC registrant; the evidence ladder's company-IR and exchange rungs, cited there by document**); Intel
Foundry from the INTC run (10-K FY2025 Note 3). **Not re-fetched in this run: TSMC, UMC, SMIC, Hua Hong, Intel Foundry**, stated so the reader
knows which rows were re-verified.*

- **Peers named: 11 of the industry's ~12 real competitors** (TSMC, Samsung Foundry, Intel Foundry, UMC, SMIC, Hua Hong, Tower, Vanguard, Powerchip,
  X-FAB, TI's foundry services); **figures for 6** (five on gross margin, Intel on operating margin). **Missing: Samsung (undisclosed), Vanguard
  (blocked rung), Powerchip and X-FAB (not attempted), TI (not segmented).**
- **Does a missing peer make the class PROVISIONAL?** No, for the reason both precedents gave, and it is stronger here: the verdict rests on GF's own
  filed price (−10.4% where dual-sourced), its own return (5.6% five-year mean) and its customers' filed dual sourcing, **not on its rank in the row.**
  No figure Samsung, Vanguard, Powerchip or X-FAB could file would turn a falling price and a 5.6% return into pricing power. The gaps are a limit, not
  a work order that could change the verdict.
- **Relative position, stated fairly:** GF's gross margin is **below UMC's in every year 2021-2025**, **within about two points of Tower's in 2022, 2024 and 2025** (3.6 points above in 2023, 6.4 below in 2021), above SMIC's
  and Hua Hong's since 2023, and **its ROE is the lowest of the four SEC filers in every year of the table except 2022** (16.2% against Tower's 15.1%). **Its specialty mix earns a mature-node
  margin.**
- **[E3-61], the row's limit:** the row shows position, not conduct; it cannot show whether the Chinese build or a subsidised Intel will price below
  cost.

### Untapped pricing power [E3-33, E5-28]
Claiming the class is claiming near-monopoly [E5-28]. **GF cut price to dual-sourced customers in 2025 and names eleven competitors.** No
near-monopoly; no untapped pricing power. *(The 63% single-sourced share could in principle hide pricing power not yet used; the 2025 ASP fell on
the other 37%, and the filings give no evidence that the single-sourced wafers were repriced upward. Recorded, not scored.)*

### Key-person dependence [E4-23]
None found. The CEO changed in April 2025 (Caulfield to Executive Chairman, Breen to CEO) and the President and COO left in March 2026 with
no filed change in the business.

### THE FAIR COUNTER-CASE, stated as its best advocate would state it [E4-51]
*"GF is not a commodity foundry. Sixty-three percent of its wafers cannot move without a redesign, by the definition its auditors sign next to.
Its platforms (22FDX, RF-SOI, silicon photonics, GaN on US soil) are not UMC's or SMIC's; its RF position worth defending in court against Tower, and alone at scale in FD-SOI. The
2023-2025 price record is the unwinding of a shortage, not the discovery of a commodity: 2022's +17% was a spike, and 2025 is merely back to trend.
The world is splitting: customers' own filings (Cirrus Logic's largest customer's American Manufacturing Program, Navitas's 'foreign supply chains
will be disadvantaged') are paying for exactly what GF has, and the US government is now a shareholder. Silicon photonics grew 29% in a year and
data-center optics is the fastest-growing end market in the industry. H1 2026 gross margin 28.0%, the highest half-year since H2 2023. Ruling it out now is
[E3-47]'s error of omission."* **Every clause is filed** (20-F Items 4-5; Cirrus Logic and Navitas 10-Ks; the Q2 2026 release; Tower's 20-F).

**The answer on the filed record.** The counter-case establishes a **design-level switching cost** and a **location advantage**; both are granted.
It does not establish [E3-03]'s second criterion **as the corpus tests it** [E3-43]: a franchise shows itself as the ability to *"regularly price
... aggressively and thereby to earn high rates of return"*, and GF's filed record is a price that fell where customers had a second source, a
five-year ROE of 5.6%, and a contract book that halved as soon as supply loosened. **[E2-44] asks about the trough, and in the trough GF's price
was held up by penalty payments and then fell.** The location advantage is a regime [E2-59], set by export controls and subsidies GF does not
control. **The price of being wrong is recorded at [E3-47], not argued away; the 2026 upturn is recorded at Q6 as the evidence that would have to
persist through a full cycle.**

### CLASS AND DIRECTION
- Needed or desired [x] · **no close substitute [ ] — fails as the corpus tests it: customers' filings (Cirrus Logic, AMD, Qualcomm, Himax) name a
  second source; GF's own 2025 price cut was *"where customers are dual sourced"*; [E3-43]'s demonstration absent (ROE 5.6% five-year mean)** ·
  not price-regulated [x]
- **Must the moat be continuously rebuilt? YES, at the design level**: each product's lock-in ends with the product and the next design is
  re-competed through a *"design funnel"*. **Does success depend on a great manager? No [E4-23].**
- **Primary moat metric, filing-sourced, and its trend:** revenue per wafer US$2,954 (2022) → US$2,568 (2025); LTA book ~$22bn → ~$11bn;
  gross margin 28.4% (2023) → 24.9% (2025), 28.0% in H1 2026. **Direction: narrowing, with an H1 2026 upturn.**
- **Class: NONE — a specialty foundry with real design-level switching costs and a regime-conferred location advantage, earning a mature-node return;
  not a franchise.**

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  *OUT on [E3-03] criterion (2) as [E3-43] demonstrates it, and on [E2-44](1): the filed price held in the 2023 trough only on customers' shortfall
  payments, then fell 3% and 10.4%, the second time explicitly where customers are dual sourced, while the five-year return on equity averaged 5.6%
  and the contracted book halved. GF's single-source share (63% of volume, its own measure) is a real design-level switching cost and is recorded;
  its location advantage is a regime [E2-59]. Different in grounds from TSMC (which passed [E3-03] and failed [E4-04]) and close to UMC's, with a
  weaker return and a stronger specialty claim.* **The file closes here. Q3 to Q6 are RECORDED, NOT GOVERNING.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — **RECORDED, NOT GOVERNING**
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

⛔ **Q2 closed the file (OUT on [E3-03](2) as [E3-43] demonstrates it, and on [E2-44](1)). Everything from here to Q6 is recorded because
the queue's output contract requires a price and because the evidence was gathered; none of it governs, and none of it can reopen Q2**
(the guardrail: *"a strong Q3 cannot promote a name, repair Q2, or substitute for Q4"*).

### STEP 1 — THE WEIGHT CASE, declared first
- [x] **Daily execution [E3-38, E3-43]**: Q2 found GF to be *"a business"*, not a franchise; [E3-43]: *"a business, unlike a franchise, can be
  killed by poor management."* Capacity timing, contract pricing and design-win conversion are recurring decisions.
- [ ] **Control [E1-16]**: not as the determinant is defined (a minority buyer can exit). **But the company is controlled by someone else,
  and that is recorded here because it shapes every decision below**: Mubadala held **72.82%** at 2026-06-30 (Step 0).
- [ ] **Leverage [E3-29]**: no (net cash ~US$2.2bn at 2026-06-30, Q4).
- **Case declared: Q3 would be a BINARY GATE on the daily-execution determinant.** No price compensates **[E1-16, E3-29, E5-35]**.

### The controlling shareholder — what the filings say control permits [E3-66]
- **Board:** *"for so long as the Mubadala Entities, in the aggregate, beneficially own 50% or more of the ordinary shares held by the
  Mubadala Entities upon consummation of our IPO, MTIC will be entitled to nominate a number of designees ... representing a majority of our
  directors"*; five designees today (Antaki, Edelman, Halawa, Languille, Obeid). A Mubadala designee *"may only be removed with or without cause
  by MTIC"* (Item 6.C).
- **Consent rights until Mubadala falls below 30%** (Item 7.B): *"issuances of equity securities"*; *"acquisitions or dispositions in an amount
  exceeding $300 million in any single transaction or $500 million in any calendar year"*; *"incurring financial indebtedness in an amount
  exceeding $200 million"*; *"hiring or terminating our Chief Executive Officer, Chief Financial Officer or Chief Legal Officer"*; changes of
  control; *"any material change in the nature of the business"*. **Management's three key appointments need the controller's consent.**
- **The auditor follows the controller:** *"We will use our reasonable best efforts ... to select the same independent certified public
  accounting firm, or auditor, used by Mubadala"*; executed in January 2024, KPMG replaced by PwC because *"The audit committee of the MDGH Group
  selected a PwC member firm in December 2023"* (6-K 2024-01-24, `0001709048-24-000003`).
- **Controlled-company and foreign-private-issuer exemptions used** (Item 16G): director nominees need not be selected by independent
  directors, and *"the Shareholder Approval Requirements under Section 5635 of the Nasdaq listing rules"* do not apply (so share issuance
  can proceed without a shareholder vote that Nasdaq would otherwise require).
- **Related-party arrangements:** Tim Breen seconded from Mubadala as COO with *"GF's reimbursement obligations to an affiliate of Mubadala"*
  (US$4.3M in 2024, secondment ended 2024-12-31); a Consulting Services Agreement with Mamoura (a Mubadala affiliate) for *"strategic planning
  ... analysis of M&A and corporate development opportunities"*, US$1M in 2025, terminated May 2025; a Registration Rights Agreement under which
  *"All expenses of registration ... will be paid by us"*; the CEO (Mubadala 2010-2024), CFO (*"senior finance roles at Mubadala"*) and Chief Legal
  Officer (Mubadala 2006-2017) all came from the controller.
- **Where the minority stands in the queue [E3-66]:** a Cayman company, controlled by an Abu Dhabi sovereign investor, with the US government
  now a shareholder (the DOC shares carry *"voting restrictions"* and *"a prohibition on privately negotiated transfers to any competitor of GF"*).
  **The minority owner stands behind the controller's consent rights and the government's funding conditions.**

### Honesty — the binary [E5-16], each matter dated to when it became PUBLIC
| public | matter | the filed words | document |
|---|---|---|---|
| 2021-06-07/08 | GF and IBM sue each other over the 2015 Microelectronics acquisition agreements | *"IBM argues that it is entitled to a return of its $1.5 billion payment to the company and at least $1 billion in damages"*; fraud claim dismissed 2021-09-14, **reinstated on appeal 2022-04-07** | 20-F FY2021, FY2023 |
| **2025-01-02** | **settled** | *"resolving all litigation matters, inclusive of breach of contract, trade secrets and intellectual property claims ... The details of the settlement are confidential"* | 6-K `0001709048-25-000003` |
| 20-F FY2025 (and earlier) | export-control breaches | *"We have in the past inadvertently violated certain of these regulations resulting in warning letters or immaterial penalties, which in turn triggered events of default under certain of our debt agreements. Although our lenders agreed to waive the defaults..."* | 20-F FY2025 Item 3.D |
| **2024-04-29** (first) | **material weaknesses, ICFR not effective, 2023, 2024 and 2025** | *"The Company did not maintain an effective control environment due to the lack of the retention of personnel with an appropriate level of expertise"*; *"The material weaknesses resulted in immaterial errors to various accounts and disclosures during the years ended December 31, 2025, 2024 and 2023"* | 20-F FY2023, FY2024, FY2025 Item 15 |
| 2026-03 | GF sues Tower Semiconductor for patent infringement (ITC, W.D. Tex.) | *"The Company disputes these claims"* (Tower) | Tower 20-F FY2025 |

**The read.** No filing read records personal misconduct by a director or officer: the IBM fraud allegation was pleaded, reinstated on appeal
and **settled without an adjudication and on confidential terms**; the export breaches are described as inadvertent and immaterial and were
disclosed; the material weaknesses are competence failures in controls, not a finding of dishonesty. **[E5-22]:** penalty size is not the
test; *"they didn't act when they learned"* is. What the filings show GF did when it learned of the control weaknesses: hired *"Chief
Accounting Officer, VP of Finance Transformation"* and others in 2024-2025, and **still reported them unremediated two years later.**
**[E5-17]'s cap:** a pass is the absence of found disqualifiers, not a finding of honesty, and the IBM settlement's terms, the one place the
reader cannot see, are exactly where [E2-68]'s asymmetry sits.

### STEP 2 — THE FLAGS
- [x] **weak accounting [E4-22] — FIRES.** (a) **Material weaknesses in ICFR at three consecutive year-ends (2023-2025), with immaterial errors in
  all three years** (above). *"There is seldom just one cockroach in the kitchen."* (b) **The useful-life change in the IPO year**: *"we revised
  the estimated useful lives of our 200mm and 300mm production equipment from 5 and 8 years, respectively, to 10 years, beginning the first
  quarter of 2021. As a result, this benefited loss before income taxes by approximately $ 628 million for the year ended December 31, 2021"*
  (FY2022 20-F, `0001709048-23-000013`; the FY2021 20-F states the same benefit in thousands, *"$ 628,000"*, and its auditor's critical audit
  matter *"amounted to $628 million"*); the shares listed on 2021-10-28 and the IPO completed 2021-11-01. **Disclosed and quantified, which is the candor half; made in the listing year, which is the
  prompt half.** (c) The 2024 impairment of **US$935M** of Malta *"legacy investments"*, taken in Q4 2024, the last quarter before the CEO change
  announced 2025-02-05 **[E3-53]** (a big charge in one quarter; recorded as a prompt, and outside owner earnings, which run on cash).
- [ ] **unintelligible footnotes**: no; the notes are standard. **But Customer A, B and C are not named**, and the IBM settlement terms are withheld.
- [x] **trumpeted projections [E4-22] third flag — a guidance culture, conservative in execution [E3-48].** Quarterly guidance on revenue, gross
  margin, operating margin and EPS in every release since Q4 2021 (`k/`); **revenue at or above the guided range in all 18 quarters Q1 2022 to Q2
  2026 (above the top in 7), IFRS gross margin at or above the guided midpoint in all 18.** *"making significant progress towards our long-term
  financial model"* (2022 releases); the 2026 Investor Day's *"long-term financial framework"* is referenced but **no numeric long-term target
  was found in any filed exhibit** (recorded sweep of the 2026-05-07 6-K and the 2022 releases; the numbers were in a webcast, not a filing).
  **The record is beat-the-guide, not make-the-numbers; the ratchet [E5-30] is in place.**
- [ ] **serial share issuance [E5-15]: no, with one 2026 event.** Shares 548M (2022) → 556M (2025) → 548.75M (2026-06-30) after buybacks; the IPO's
  primary US$1,444M (2021); **+9,907,399 to the Department of Commerce agreed 2026-09-03** (Step 0).
- [x] **EBITDA promotion [E4-29] — FIRES.** *"Non-IFRS adjusted EBITDA"* is a row of the summary results table in **every** quarterly release from
  Q3 2021 to Q2 2026; *"Record adjusted EBITDA margin of 36.0%"* was a headline bullet (Q1 2022); adjusted EBITDA and its margin were **guided** in
  2022 (*"Adj. EBITDA | ... | $580 - $620 | EBITDA Margin (mid-point) | 31.6%"*, Q4 2021 release). Its definition removes *"depreciation and
  amortization, share-based compensation, restructuring charges, impairment charges ... litigation claims and acquisition related charges"*. In a
  business whose depreciation was **19-25% of revenue** in 2021-2025, the metric deletes the largest real cost [E5-41].
- [ ] **filed-figure tells [E4-30]**: cash taxes paid US$7M, 4M, 11M, 31M, 19M (2021-2025) against pretax income of −176, 1,532, 1,084, −170, 911:
  **structurally near zero** (loss carryforwards, incentives), **not a falling trend**; reported growth is not smooth.
- [x] **metric-switching [E2-49] — FIRES.** The performance-share yardstick changed as it read badly: 2022-2023 PSUs vested on *"absolute return on
  invested capital ("ROIC") and relative total shareholder return ("TSR") versus the SOX Index"*; **in September 2023, as the downturn arrived,
  *"the People and Compensation Committee of GlobalFoundries approved a modification to the 2023 PSUs, to adjust the return on invested capital
  ("ROIC") performance threshold"***; from 2024 the PSUs vest on *"revenue and adjusted free cash flow as a percentage of revenue and absolute
  TSR"* **with "targets set for each year annually"**. **Both original yardsticks (ROIC, and TSR relative to the index) were dropped**, which is
  *"disposition of the yardstick rather than disposition of the manager"*, and the new targets are re-set yearly, the opposite of *"pre-set,
  long-lived and small bullseyes"*. Also the single-source measure renamed from *"business"* to *"design wins"* in one FY2024 sentence (Q1), a
  smaller instance.
- [x] **dividends and issuance in the same season [E2-52] — a prompt.** The **first-ever dividend** was announced 2026-05-07 (*"$0.12 per share ...
  payable on July 14, 2026"*, with a framework to return *"up to 50% of trailing twelve-month Non-IFRS adjusted free cash flow"*), a second
  declared for October 2026; **9,907,399 shares were agreed to be issued to the Department of Commerce on 2026-09-03 for US$375M.** At ~549M shares
  the dividend is about US$66M a quarter. Money is fungible; the filings do not link the two, and neither does this file beyond recording them.
- [ ] **stock-price targeting [E3-50]**: *"absolute TSR"* is a PSU metric (prompt).

### STEP 3 — THE PRIMARY TEST [E2-01]
Return on average parent equity **−16.7% (2020) · −3.4 · 16.2 · 9.7 · −2.4 · 7.8% (2025)**, five-year mean **5.6%**, without leverage (Q2 row).
Parent equity US$7,176M (2020) → US$11,928M (2025), lifted by the IPO's US$1,444M. **Accumulated deficit US$12,381M.** **[E3-59]'s "hand they were
dealt"**: a business spun out of AMD's fabs, the IBM Microelectronics division and Chartered Semiconductor, re-based in 2018-2019 away from the
leading edge. **Against the row, the operators earned the lowest ROE of the four SEC foundries in five of six years.**

**The half-owner test [E2-26]:** end-market revenue, shipments (quarterly), utilisation, the single-source share, LTA commitments, contract-liability
roll-forwards and grant movements are given; **positive pole on operating disclosure.** **Against it:** customers anonymised as A, B and C; the IBM
settlement terms withheld; no dollar amount for underutilization payments inside wafer revenue; the Investor Day targets outside the filings;
Mubadala's senior executives (its CFO since 2004, its Chief Legal Officer, its Deputy Chief Strategy Officer) each described as *"an independent,
non-executive director pursuant to applicable Nasdaq rules"*, which is literally true of the rule and not what a reader means by independent.

### Capital allocation
- **Buybacks [E5-08, E4-31], every one of them from or beside the controller's exit:**

  | date | shares | price | from | document |
  |---|---|---|---|---|
  | 2024-05-28 | 3,940,886 | **US$50.75** | Mubadala (MTIC), inside its 18.7M-share secondary | 6-K `0001628280-24-025403`; 20-F FY2024 Note 31 |
  | 2026-03-13 | 7,344,840 | **US$40.845** | Mubadala (MTIC), inside its 27.3M-share secondary | 6-K `0001709048-26-000043` |
  | H1 2026 | ~2.3M | **US$43.88** avg | open market | Q2 2026 interim report |

  **US$600M in two years, US$500M of it paid to the controller.** Against this file's conservative floor range (Q5: roughly **US$5-25 a share** on
  valid multi-year bases with 0-10% growth), **every purchase was above the top of the value range, at 1.6 to 10 times it, not at a material discount. [E5-08]
  condition (2) fails — CAPITAL ALLOCATION FLAG**, stated with the humility clause **[E4-13]**: *"They also know a whole lot more about them than I
  do"*; this rests on this file's own range. **It binds position size, never the discount rate.** And [E4-31]'s third condition: the buybacks were
  priced to the underwriters' price in Mubadala's own offerings, not to a value the company published.
- **Mubadala's own conduct as seller:** 450.4M shares (81.0%, 2025-12-31) → 399.6M (72.82%, 2026-06-30); the Form 144 of **2026-05-26** covered
  **22,000,000 shares at an aggregate market value of US$1,979M (US$89.96)**, near the top of a price that had doubled since March, ten weeks after the company had bought 7.3M
  of its shares at US$40.845. **The company's purchase from the controller was made at less than half the price the controller's own May notice
  recorded**; the filings do not say why the company did not wait, and no value estimate was published with either purchase.
- **Capex against depreciation:** 0.23-0.29× in 2019-2020, **1.09-1.88× in 2021-2023**, **0.40-0.55× in 2024-2025**, then **US$723M in H1 2026** against
  US$325M a year earlier (Q4). **The spending follows the cycle**: starved before the IPO, flooded into the shortage, starved in the trough.
- **Acquisitions:** ~US$1.3bn in eighteen months (SMP, MIPS, InfiniLink, AMF, Synopsys ARC; Q1), four of them in design IP and photonics rather
  than wafer capacity. **No acquisition post-mortem found [E4-39]** (recorded sweep of the 20-F FY2025 and the 2026 6-Ks for the deal names plus
  "performance", "synergies achieved", "review": the only hits are the purchase-price allocations and the auditor's critical audit matter on AMF's
  intangibles).
- **Government money, and its strings:** the CHIPS Direct Funding Agreement *"contains restrictions with respect to certain "change of control"
  transactions, expansion of manufacturing capacity in certain countries, joint research or technology licensing in certain countries, as well as
  dividends and share repurchases"* (20-F FY2025 Item 3.D; **the restriction's terms are not quantified in any filing read**); an AMITC repayment
  reserve of **US$50M** (Note 30); and the 2026 conversion of an announced US$375M grant into Department of Commerce shares at US$37.85, 19% below the
  US$46.95 quote (Step 0; the link is arithmetic, not filed).
- **The institutional imperative [E2-30]:** [ ] resists change · **[x] projects soak up available funds, a prompt** (US$1.3bn of IP and photonics
  deals; the US$16bn *"over the next 10 or more years"* US plan contingent on subsidies) · [ ] staff studies · **[x] peer imitation, a prompt**
  (*"physical AI"*, *"AI-centric markets"*, a first dividend and a buyback framework in the same year as every peer's AI narrative).
- **[E3-40], loss of focus, a prompt:** a foundry buying processor-IP licensors (MIPS, ARC) is moving capital away from the base business into a
  different one.
- **Management turnover:** CEO changed April 2025; CFO John Hollister *"is leaving the company for personal reasons"* **"effectively immediately"**
  (2025-10-27); President and COO resigned effective 2026-03-02. Three of the top four roles changed in eleven months (prompt).

### Pay, and what it vests on [E4-27]
- Aggregate only (*"Under Cayman Islands law, we are not required to disclose compensation paid to our directors and executive officers on an
  individual basis"*): **US$68.2M** for directors and executive officers in 2025, with 0.7M RSUs and 0.7M PSUs.
- **AIP:** *"Financial and operational performance: 100% for all executives"*, times an individual OKR modifier of 0-150% *"Based on the discretion of
  the Board ... or CEO"*.
- **PSUs (70% of the CEO's LTI):** *"revenue and adjusted free cash flow as a percentage of revenue and absolute total shareholder return"*.
  **Adjusted free cash flow is defined as *"cash flow provided by (used in) operating activities less purchases of property, plant and equipment
  and intangible assets plus proceeds from government grants"*** (Q2 2026 release). **What that rewards, in this business:** it does not subtract
  SBC; it rises when capex is cut (2024-2025 capex at 0.40-0.55× D&A); it rises with customer prepayments and government grants; and it is set
  *"for each year annually"*. **[E4-27]: "Never, ever, think about something else when you should be thinking about the power of incentives."**
  The incentive points at the same levers that flatter the metric: under-spending on the plant, taking customers' cash early, and taking the
  state's.

### Converging prompts [E4-52]
**Seven prompts point the same way:** material weaknesses at three year-ends; a depreciation-life extension in the IPO year worth US$628M;
adjusted EBITDA in every results table; PSU yardsticks (ROIC, relative TSR) dropped as they read badly; US$500M of buybacks paid to the
controlling shareholder at prices well above any multi-year value range; a first dividend in the year shares were issued to the government; and
three of four top officers replaced in eleven months. **Together they are one reinforcing system toward presenting a better number and supplying
the controller's exit**, which is [E4-52]'s *"confluences ... acting in favor of a particular outcome"*. **Offsetting, on the record:** conservative
quarterly guidance beaten for eighteen quarters; every accounting change disclosed and quantified; the export breaches self-disclosed; the IBM
suit settled rather than lost; and net cash throughout.

### THE GUARDRAIL
- [x] Nothing in this Q3 is used to promote the name, repair Q2 or substitute for Q4 **[E2-37, E2-38, E3-39]**.
- [x] Key-person dependence: none found (Q2).
- [x] No great-manager thesis is relied on.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary — no integrity disqualifier found** — *with the weak-accounting flag (material
  weaknesses 2023-2025), the EBITDA flag, the metric-switching flag, a live capital-allocation flag on buybacks from the controller, and seven
  converging prompts [E4-52]. IN never promotes, and this one cannot: Q2 is OUT. A reader who weighs [E4-52]'s convergence as a disqualifier in
  itself would score this UNKNOWABLE; the framework says each flag is "a prompt to read, never a verdict" [E5-36, E5-38], and no conduct finding was
  located.*

## Q4 — WILL IT SURVIVE? — **RECORDED, NOT GOVERNING**

### Owner earnings — the one number **[E2-23]**
**Construction (CONVENTION, framework VI): operating cash flow − SBC − the change in customer prepayments − (c).** `oe.py` / `oe_out.json`, filed
cash-flow lines (`row.py`). **Run-specific choices, each disclosed:**
- **Customer prepayments are stripped, following the TSM run, and the reason is filed:** GF's *"Contract liabilities comprises contract liabilities
  for payments received in advance of the satisfaction of performance obligations for wafers"* and they run through **operating** cash (2021:
  *"an increase in trade and other payables of $1,829 million, which was driven principally by customer prepayments for future wafer shipments"*).
  Balances US$135M (2020) → 1,901 → 1,918 → 1,983 → 1,584 → **1,230 (2025)** → 954 (2026-06-30, of which 21 acquired with ARC). **Without the strip,
  2021 operating cash is overstated by US$1.77bn and 2024-2025 understated by US$0.4bn a year.** *(The UMC run did not strip because UMC's deposits
  sit in financing; GFS's sit in operating, so TSM's treatment applies.)* Both results are shown.
- **Government grants reduce (c)**: *"Where the grant relates to acquisition of assets, it is recognized as a reduction in the basis of the asset"*;
  proceeds US$335M (2019), 312, 83, 93, 143, 10, **148 (2025)**, in financing until 2022 and investing from 2023. **The 2026 Department of Commerce
  money arrives as a share issuance**, which is not in operating cash, not a grant in (c), and is counted instead in the share count (Step 0).
- **Interest received sits inside operating cash** (US$147M in 2025); net interest (received less paid) was **−100, −64, +2, +49, +88** (2021-2025),
  **five-year mean about −5**, so the five-year owner earnings neither include nor omit the net cash's return in any material way.
- **Tool-sale proceeds** (US$324M in 2021, US$170M in 2025, investing) are **not** deducted from (c) at either end; they would add about US$120M a year
  over 2021-2025 and are displayed, not used.
- **Acquisitions** (US$69M 2024, US$682M 2025, US$440M H1 2026, net of cash) are **displayed as a third deduction and put in neither end**, as the UMC
  run did.

**SBC: RESOLVES AND IS COMPLETE, and is MATERIAL, so [E3-70]'s measure is used.** The cash-flow add-back is filed every year: **0 (2019), 1, 223,
181, 150, 186, 200 (2025)** US$M. Grant-date value of RSU and PSU grants (share-based payment notes, RSUs valued *"based on the closing price of the
ordinary stock on the date of grant"*): **2022 US$236M (3,416,545 RSUs at $57.09 plus 571,277 PSUs at $70.85) · 2023 US$214M · 2024 US$226M · 2025
US$306M (6.8M RSUs at $36.25 plus 1.6M PSUs at $36.88)**, against charges of 181, 150, 186 and 200. **The grant value is used for 2022-2025** (the charge
for 2019-2021, where no grant table was read); it is 10-18% of operating cash. *(The ESPP's 20% company match and employer social charges on vesting
sit in operating cash already.)*

**Maintenance capex, the central judgment [E3-44, E2-41, E5-20].**
- **What the filing gives:** no maintenance split; *"we incur significant costs regardless of the number of wafers we actually produce"*; depreciation
  US$1.3-1.6bn a year (19-25% of revenue) on **10-year** tool lives since 2021; installed capacity *"approximately 2.8 million wafers per annum"* (2025)
  against 2,618 kwpa (2023).
- **The natural experiment in the filing, twice:** **2019-2020 capex ran at 0.23-0.29× D&A**, and **2021-2023 had to run at 1.09-1.88×** to catch up and
  meet the shortage; **2024-2025 ran at 0.40-0.55×**, and **H1 2026 capex was US$723M against US$325M** a year earlier. Spending below depreciation
  has been followed by catch-up both times.
- **The flat-revenue five years:** 2021-2025 revenue ×1.03, net capex US$7,500M against D&A US$7,574M (**0.99×**), **and over the same five years units
  fell 5.1% from 2022 and the price per wafer fell 13% from 2023.** **Spending depreciation did not keep the place** [E5-20].
- **The case: [E5-20]'s class, with a twist the filing forces.** GF is capital-intensive and depreciation-level spending did not hold units or price,
  so **(c) is at least D&A**. But GF's recent capex is *below* D&A, so the "D&A end" is here the **conservative** end in the trough windows, and the
  **low-capex end is the invalid one** there. The rule applied in every window: **where net capex is below D&A, the capex end is INVALID (a trough
  under-spend, shown by the 2019-2023 catch-up) and displayed only; where net capex is above D&A, both ends are carried.**
- **The two ends:** **capex end = capex (PP&E + intangibles) − grant proceeds**; **D&A end = the cash-flow depreciation and amortisation add-back.**
  *(Pre-2021 D&A runs on 5- and 8-year lives and is not comparable; 2019-2020 are displayed only.)*

**Owner earnings by year, US$M:**

| year | OCF | − SBC used | − Δ contract liabilities | net capex | D&A | **OE, capex end** | **OE, D&A end** | acquisitions (display) | net capex / D&A |
|---|---|---|---|---|---|---|---|---|---|
| 2019 | 497 | 0 | n/a | 438 | 2,678 | 59 | *−2,181 (pre-2021 lives)* | — | 0.16 |
| 2020 | 1,004 | 1 | −10 | 280 | 2,522 | 733 | *−1,509 (pre-2021 lives)* | — | 0.11 |
| 2021 | 2,839 | 223 | **+1,767** | 1,684 | 1,618 | **−835** | −769 | — | 1.04 |
| 2022 | 2,624 | 236 | +17 | 2,966 | 1,623 | **−594** | 749 | — | 1.83 |
| 2023 | 2,125 | 214 | +65 | 1,661 | 1,451 | 185 | 395 | — | 1.14 |
| 2024 | 1,722 | 226 | **−399** | 615 | 1,568 | *1,280 (INVALID)* | **327** | 69 | 0.39 |
| 2025 | 1,731 | 306 | **−354** | 574 | 1,314 | *1,206 (INVALID)* | **466** | 682 | 0.44 |
| TTM 2026-06 | 1,916 | 234 (charge) | −635 | 971 | 1,245 | *1,346 (INVALID)* | 1,072 | 1,103 | 0.78 |

*(TTM = FY2025 + H1 2026 − H1 2025 from the interim statements, 6-K `0001709048-26-000219` and `0001709048-25-000057`; one year is not [E2-23]'s
"average annual amount"; displayed only.)*

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25, E4-38]:**

| window | net capex / D&A | OE, capex end | OE, D&A end | less acquisitions (display) | without the prepayment strip (display) |
|---|---|---|---|---|---|
| **5-yr 2021-2025 (the default [E2-42])** | 0.99 (valid both ends) | **248** | **234** | 98 | 467 / 453 |
| 4-yr 2022-2025 | 0.98 (valid both ends) | 519 | 484 | 331 | |
| 3-yr 2023-2025 (post-EFK perimeter) | 0.66 (capex end INVALID) | *890 (display)* | **396** | 640 | |
| TTM to 2026-06-30 (display) | 0.78 | *1,346* | 1,072 | 243 | |

- **How few periods exist, and what that does to the width.** Seven annual cash-flow periods are filed (2019-2025); the first two sit before the IPO,
  before the 2021 useful-life change and before the EFK exit; **so only five comparable years exist, the five-year default consumes all of them,
  and no second five-year window can be built.** The 4-year and 3-year windows are sub-windows of the same five years, not independent tests. **A
  ten-year mean, the kind that averages a full cycle, cannot be built for GFS from any filing**; what the width below leaves out is therefore not
  a distorted year but an entire prior cycle.
- **Combined range, valid windows × valid ends: US$234M to US$519M a year** (5-yr D&A end to 4-yr capex end); **US$234-248M on the five-year default.**
  With acquisitions deducted, the five-year figure is **US$98M**; without the prepayment strip, **US$453-467M**. **The width across every construction
  shown is roughly 5×.**
- **Is the range too wide to reach a conclusion?** **As a level, nearly [E4-25].** For the only decision it feeds, no: **every construction, including
  the best trailing twelve months, yields below the 5.35% bond on the cap** (Q5).
- **The distorted years, named [E5-11, E4-41]:** **2021** (the prepayment inflow of US$1.77bn and the useful-life change); **2022** (the shortage: utilisation
  101-103%, ASP +17%, capex 1.88× D&A); **2024-2025** (capex below half of depreciation, flattering the capex end, and the prepayment run-off depressing
  operating cash). [E4-41] says normalise down for luck: **the five-year default contains the 2022 shortage and the 2021 prepayment year, both favourable
  to the D&A end.**
- **Growth record, for Q5:** revenue **+2.6% a year 2019-2025** (US$5,813M → 6,791M) and **+0.8% a year 2021-2025**; owner earnings show no trend that
  survives the window choice.

### Great, good, or gruesome? **[E4-20]**
- [ ] great · [ ] good · [x] **gruesome**
- **Evidence:** five-year owner earnings of US$234-248M on average parent equity of about US$9.9bn (2021-2025) is **about 2.4-2.5%**, while the business
  took in US$1.44bn of IPO equity, US$1.8bn of customer prepayments and US$0.5bn of grants and spent US$9.3bn of capex and US$1.3bn of acquisitions
  over 2019-2026; *"pays an inadequate interest rate and requires you to keep adding money at those disappointing returns."* **[E4-43]'s good class
  is not reached** on any valid window (the best, 4-yr capex end, is about 5% on equity).

### Staying power — score all three **[E5-11]**
- **(1) A large and reliable stream of earnings: NO.** Owner earnings negative in 2021 and 2022 at both ends, US$98-519M across constructions since.
- **(2) Massive liquid assets: YES.** At 2026-06-30: cash US$1,087M, marketable securities US$1,270M current and US$946M non-current (**US$3,303M**) against
  debt of US$1,122M: **net cash ~US$2.2bn** (leases US$556M excluded). A new **US$1.5bn** unsecured revolver (2026-08-21, maturing 2031) replaced the
  undrawn US$1.0bn facility; *"maximum consolidated leverage ratio of 4.00 to 1.00"*. **Undrawn facilities are not counted [E5-39].**
- **(3) No significant near-term cash requirements: MODERATE AND COVERED.** Capital commitments **US$800M, US$619M within twelve months** (2025-12-31);
  capex running at ~US$1.4bn annualised in H1 2026; dividends ~US$265M a year; ARC paid (US$440M); the US plan of *"more than $16 billion over the next 10
  or more years"* is expressly *"Subject to market requirements and customer demand as well as receipt of expected government funding"*. **Covered by
  net cash and ~US$1.9bn of trailing operating cash.**
- **Leverage, named and quantified [E4-16, E2-54]:** net cash; interest paid US$59M in 2025 against operating cash less net capex of ~US$1.16bn: **about
  20× coverage.** Term Loan A prepaid 2025-01-02 (*"The total amount of the prepayment was $664 million"*), after which *"assets pledged as common security
  ... were irrevocably and unconditionally released"*; remaining debt mainly the Singapore EDB loan (*"Other debt facilities | $ | 1,098"*). **Terms, not
  just quantity [E3-52]:** the CHIPS agreement's restrictions on dividends, buybacks and change of control, and the grants' forfeiture clauses
  (*"Certain investment grants are subject to forfeiture in declining amounts over the life of the agreement"*), are covenant-like liabilities with no
  amount on the balance sheet.

### Name the specific way THIS business dies **[E2-27, E3-24]** — exposure, not experience **[E4-40]**
**1. THE PASS-THROUGH (registered, eleventh, TM) — the dominant exposure.**
- **Mechanism:** a business that must keep spending to hold its place, whose price re-sets to what a customer with a second source will pay, in an
  industry where each round of capacity is individually rational and collectively neutralising [E2-27], and whose gains pass to customers [E3-62].
  GF names its own attacker: *"China's foundry capacity is expected to grow faster than expected demand at those nodes"* and *"the business we do around
  the world outside of China, in markets in which Chinese semiconductor manufacturers are our direct competitors, also represents a significant portion
  of our business."*
- **Quantified from filed figures:** 2025 itself (ASP −10.4%, wafer revenue per wafer US$2,871 → 2,568) took ~US$700M of revenue at 2025 volumes (2,345k
  × US$303) with gross margin held only by lower depreciation (D&A −US$254M) and fuller fabs. **The owner-earnings floor under that shape is the five-year
  record: US$98-248M a year, ~0.4-0.9% on the cap.**
- **Likelihood: [x] likely** (the Chinese mature-node build is filed by GF, by UMC and by SMIC and Hua Hong; the contract book that held price is halving).

**2. THE PATRON — a proposed fourteenth shape, flagged to the operator, not registered here.**
- **Mechanism:** the capacity that gives the business its distinctive position (US sites, Trusted Foundry, *"non-China and non-Taiwan"* supply) is paid for
  in part by a sovereign that sets the terms, can change them, and can take them back: restrictions on *"dividends and share repurchases"* and
  *"change of control"* transactions, milestone-conditioned disbursements, forfeiture and repayment clauses, and, in 2026, **an announced US$375M grant followed by a
  share issuance of exactly US$375M to the same department at US$37.85, 15% below the 2026-09-03 close (US$44.53) and 19% below the 2026-09-11 quote.** If the sovereign's objective changes, the filing says what
  follows: *"government agencies could seek to recover subsidies or grants from us"* and projects *"may be indefinitely delayed"*. **The owner's return
  dies not in the accounts but in the terms: the state keeps the strategic value of the plant it funded and the owner keeps the depreciation.**
- **Quantified from filed figures:** grants received US$1,124M (2019-2025); up to US$1.575bn CHIPS plus US$570M New York committed against a
  US$16bn plan; AMITC repayment reserve US$50M; the 2026 DOC issuance's cost to existing holders at the quote, (US$46.95 − 37.85) × 9,907,399 ≈
  **US$90M**. **At the level of the business, small against a US$26bn cap; at the level of strategy, it decides where and what GF may build.**
- **Why it is not an existing shape:** not THE ADDRESS (the plant is not in a disputed jurisdiction; it is in the funder's), not THE PASS-THROUGH (the gain
  passes to the state, not to customers), not THE BORROWED BALANCE SHEET (the money is a grant, not a customer's or supplier's balance sheet), not
  THE TENANT (SPOT's proposal, pending: GF owns its plant; its landlord is the regime, not a counterparty). **Recorded as a proposal for the
  operator's ruling (prime rule 5 governs structural additions to the register); the register is not changed by this run.**
- **Likelihood: [x] a real possibility** (a change of terms has already happened once, in 2026, on the grant-for-shares).

**3. THE CONTROLLER'S EXIT.** Mubadala holds 72.8% and has sold 50.8M shares in six months; its consent is required for issuance, large M&A,
debt and the CEO, CFO and CLO. **Quantified:** 399.6M shares, roughly a hundred trading days of the stock's volume at the three to five million shares a day in the flagged quote series; the company has so far absorbed US$500M of the sales. **A real possibility of mattering to the owner's return (price
overhang, buybacks at the seller's price); a low-level possibility of mattering to survival.**

**4. THE DOLLAR AND THE EURO/SINGAPORE COST BASE.** Revenue in dollars, costs in euros, Singapore dollars and yen, hedged with forwards. **A likely source
of volatility; a low-level possibility of mattering to survival.**

**THE SURVIVAL SHAPE: THE PASS-THROUGH (registered, eleventh), with THE PATRON proposed as a fourteenth and flagged to the operator.** Checked against the
twelve registered: ORCL (contracted not to stop) no; ARM (pay eats the cash) no, SBC 10-18% of operating cash; BE/RGTI (too little history) **partly**:
five comparable years, no full prior cycle, but enough to price; BA (cash undoes past work) no; SWK (the self-liquidating distribution) no, though a
first dividend began in the year shares were issued; ACVA/FLNC/NEGG (the borrowed balance sheet, treadmill, pendulum) no, the prepayments are unwinding,
not being relied on; CNR (long tail on a short cycle) no; BAM (warehouse) no; SONY/HMC (camouflage) no, the four acquisitions are small and disclosed;
**TM (the pass-through) yes**; TSM (the address) no: non-current assets 41% Singapore, 34% United States, 20% Germany, none in a disputed jurisdiction.

- **VERDICT (RECORDED, NOT GOVERNING): [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** → *OUT on [E4-20]: gruesome on every valid construction
  (owner earnings US$234-519M, about 2-5% on equity, five-year default ~2.3%). The company survives on every filed balance-sheet measure (net cash
  ~US$2.2bn, near-term requirements covered); the owner's return does not, and the likely mechanism is THE PASS-THROUGH.*

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 is OUT (and Q4, recorded, would be OUT). What follows is the arithmetic the queue's output
contract requires, headed as operator rule 3 requires.

---
## Q5 — **COMPUTATION — NOT A CLEARANCE**

**This section contains no entry language and confers no clearance. It is arithmetic.**

**The floor first [E4-28]:** *"that's the figure we quit on ... we don't want to buy equities where our real expectancy is below 10 percent. Now,
that's true whether short rates are 6 percent or whether short rates are 1 percent."*

**The cap:** **US$26,229M** (US$46.95 × 558,658,481, Step 0). Net cash at 2026-06-30 ~US$2,181M (US$3.90 a share), not added to the values below because
the five-year owner earnings already carry a net-interest line averaging about zero; adding it would lift every per-share value by ~US$4, shown in the
range.

**1. THE YIELD** (`q5.py` / `q5_out.json`):

| construction | OE US$M | yield on cap | vs USD 30-yr 5.35% | perpetual growth needed for 10% | decade growth needed (staged engine) |
|---|---|---|---|---|---|
| **5-yr D&A end** | **234** | **0.89%** | −4.46 | 9.0% | 30.8% |
| **5-yr capex end** | **248** | **0.95%** | −4.40 | 9.0% | 29.9% |
| 5-yr capex end less acquisitions (display) | 98 | 0.37% | −4.98 | 9.6% | 43.5% |
| 4-yr D&A end | 484 | 1.85% | −3.50 | 8.0% | 20.6% |
| **4-yr capex end** | **519** | **1.98%** | −3.37 | 7.9% | 19.7% |
| **3-yr D&A end** | **396** | **1.51%** | −3.84 | 8.4% | 23.4% |
| 3-yr capex end (INVALID, display) | 890 | 3.39% | −1.96 | 6.4% | 12.4% |
| 5-yr without the prepayment strip (display) | 467 | 1.78% | −3.57 | 8.1% | 21.1% |
| TTM D&A end (display) | 1,072 | 4.09% | −1.26 | 5.7% | 9.9% |

- **Every valid construction yields 0.9-2.0% on the cap: 3.4-4.5 points below the US bond and 8-9 points below the floor.** Even the best trailing twelve
  months at the D&A end, which a single year cannot be [E2-23], yields 4.1%.

**2. WHAT THE PRICE ALREADY ASSUMES**
- **Perpetual growth needed to reach 10%: 7.9-9.0% a year** on the valid bases. In the staged engine (ten years of growth, then 3%, discounted at 10%; it
  casts no vote [E3-34]): **decade growth of 20-31% a year from the valid multi-year bases, and 9.9% a year even from the best trailing twelve months.**
- **What the business has actually done:** revenue **+2.6% a year 2019-2025**, **+0.8% a year 2021-2025**; units 2,472k (2022) → 2,345k (2025); price per
  wafer −13% from 2023. **[E4-35]:** *"fewer than 10 of the 200 most profitable companies ... will attain 15% annual growth in earnings-per-share over the
  next 20 years."* **[E4-44]:** value *"cannot over the long term grow faster than its earnings do."*
- **In words: at US$46.95 the buyer pays about US$4 a share for net cash and about US$43 a share for a specialty foundry whose owner earnings would have to
  compound at 20-30% a year for a decade from any multi-year base, in a business whose revenue grew under 1% a year over the five years it has filed,
  whose price per wafer fell 13% in two years, whose Chinese competitors are building the capacity GF itself calls excess, and whose controlling
  shareholder is selling.** The quote doubled to US$89.96 in May 2026 and halved again; at US$46.95 the market is still capitalising the silicon-photonics,
  US-sourcing and AI narrative of the 2026 Investor Day, not the filed record.

**3. WHAT YOU ARE PAID**
- **Points over the sovereign: −3.4 to −4.5 on the valid means** (−1.3 on the best trailing year).

### THE PRICE — THE VALUE AS A ROUND-NUMBER RANGE [E4-01]
- **At the ~10% floor, on the valid multi-year bases, 0-10% growth for ten years then 3%: roughly US$5-25 a share** (5-yr D&A end 4.9 / 7.1 / 10.3; 5-yr
  capex end 5.3 / 7.6 / 11.0; 3-yr D&A end 8.4 / 12.1 / 17.5; 4-yr capex end 11.0 / 15.8 / 23.0), **about US$9-27 with net cash added.** **From the best
  trailing twelve months with 10% growth: ~US$47.**
- **Current price US$46.95 (Nasdaq, 2026-09-11). Above the entire range built on any multi-year window**; reached only by the single best trailing
  twelve months compounding 10% a year for a decade.
- **Screamer test [E4-01], for the record only:** the price is not below the conservative case; it is **four to nine times the conservative cases** (US$4.9-11.0 at 0-10% growth on the five-year bases).
  **Windage count: one** (the prepayment strip is a construction, shown both ways; SBC at grant value is the corpus's measure [E3-70], not windage; the
  discount rate is the floor, not a premium [E3-42]).
- **Verdict line: the file is closed at Q2; the price would also fail the floor.** No ranking position.

## Q6 — **COMPUTATION — NOT A CLEARANCE.** WHAT WOULD PROVE THIS FILE WRONG, PRE-COMMITTED [E1-02]
**No holding exists and nothing is armed.** Conditions under which a later run should reopen, set before any price moves them **[E1-02]**:
- **Reopen Q2 [E2-44] only on a full cycle of filed pricing:** a 20-F reporting a flat-or-rising ASP in a year when shipment utilisation is below ~80%
  **without** underutilization payments carrying it, **and** again in the next downturn, with gross margin holding above ~28%.
- **Reopen Q2 [E3-03](2) on customers' filings:** a named top-ten customer (AMD, Qualcomm, Skyworks, Qorvo, Cirrus Logic, NXP) describing GF as its sole
  qualified source for a product line **after** its current capacity agreement ends (AMD's and Cirrus Logic's run through 2026), or the single-source
  share re-stated as a share of **revenue**, rising.
- **Monitor [E4-32, E4-55]:** the LTA book (~$11bn at 2025-12-31, from ~$22bn), contract liabilities (US$954M at 2026-06-30), shipments (2,345k in 2025,
  1,204k in H1 2026), wafer revenue per wafer (US$2,568 in 2025), and the Tower patent suits' outcome.
- **Q3 would need:** the material weaknesses reported remediated in a 20-F; a PSU yardstick held constant for three years; any buyback made at a
  published discount to a disclosed value; and the IBM settlement's economics if ever disclosed.
- **Q4 would move off OUT** only on owner earnings above ~US$1.3bn a year (~5% on the cap) sustained over a five-year window with net capex at or above
  depreciation.
- **The operator's ruling requested on THE PATRON** (proposed fourteenth shape) before any later run registers it.
- **The price condition, for orientation only:** the multi-year floor range sits around US$5-25 a share; a price inside it would still meet a closed Q2.
  **Price appreciation and holding period are rejected as reasons [E2-28].**

- **VERDICT: NOT OPENED — no holding exists.**

---
## SELF-AUDIT (operator rule 6)
- [x] Questions answered in order; the file stopped at Q2 (OUT); Q3-Q6 recorded under explicit banners.
- [x] No question marked IN carries an "unverified" or "provisional" caveat. **Q1 IN** rests on filed tables; the Q3 binary (recorded) is IN with the
  cap stated.
- [x] No UNRESEARCHED verdict issued. Competitor gaps (Samsung undisclosed; Vanguard blocked; Powerchip, X-FAB not attempted; TI not segmented) stated as
  limits that cannot change the Q2 direction, with the reason.
- [x] No UNKNOWABLE verdict issued; the recorded Q4 is OUT on [E4-20], and the likelihoods of the named deaths are stated in the corpus's vocabulary.
- [x] Step 0: the 20-F read with accession `0001709048-26-000022`; 2025 operating cash cross-checked to the MD&A and `companyfacts`; a 2020 vintage
  restatement found and resolved toward the later filing; a `companyfacts` depreciation tag (US$1,168M for 2025) found to differ from the cash-flow
  add-back (US$1,314M), and **the filed add-back used throughout**.
- [x] Owner earnings on multi-year means (5-yr default, 4-yr, 3-yr; TTM displayed), both (c) ends with a stated validity rule, D&A pre-2021 marked
  non-comparable, SBC resolved and complete at grant value [E3-70], the prepayment strip applied with TSM's reason and shown both ways, grants in (c),
  acquisitions displayed, how few periods exist stated.
- [x] Competitor row: six peers with figures (TSMC, UMC, Tower, SMIC, Hua Hong on gross margin; Intel Foundry on operating margin) plus ROE for the four SEC
  filers; **Tower recomputed**, the others cited from the TSM and UMC runs' filing-sourced tables and marked as not re-fetched.
- [x] Sovereign for the earnings currency: USD, US Treasury daily par curve, 09/11/2026, struck through `tools/sources.py`.
- [x] Share count by hand, the issued-versus-outstanding trap checked (issued equals outstanding; cancelled repurchases), the DOC issuance included.
- [x] Value as a round-number range; one bar (screamer, for the record) with windage count one.
- [x] Prices dated; Yahoo used for live quotes only and flagged.
- [x] **EDGAR full-text search only through `tools/sources.py:fts_count()`**; 35 calls, **no HTTP error** (`fts_out.json`); every hit document opened.
- [x] Every ledger id cited was checked against `principle_ledger.csv` before commit.
- [x] Run committed to git by pathspec after each section.

**Errors of my own caught before commit, recorded:**
1. **I first counted the 2025 acquisitions as US$781M**; the four considerations sum to US$791M (US$682M net of cash acquired). Corrected before the Q1
   commit.
2. **I first wrote that GF's gross margin was "within about two points of Tower's"** without qualification; it was 6.4 points below in 2021 and 3.6 above
   in 2023. Narrowed before the Q2 commit.
3. **I first wrote that GF's ROE was the lowest of the four SEC foundries "in every year"**; in 2022 GF's 16.2% was above Tower's 15.1%. Corrected before
   the Q2 commit.
4. **I first put acquisitions inside the capex end of (c)**, which made the five-year capex end US$98M; the UMC precedent displays acquisitions outside both
   ends, and the choice is disclosed. Re-run (`oe.py`) with acquisitions displayed; both figures are in the table.
5. **I first labelled a six-year window "7-yr 2019-2025"** in `oe.py`; the 2019 strip is unavailable, so the window is 2020-2025. Relabelled, displayed only.
6. **My first quote of Cirrus Logic dropped "Limited ("TSMC")"** from the supplier name without an ellipsis, and paraphrased its prepayment reason;
   both restored to the filed words before the Q2 commit.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business, at Q2)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** GlobalFoundries is a specialty (not leading-edge) foundry with real design-level switching costs (63% of volume single-sourced by its
  own measure) and a regime-conferred US location, and it fails Q2 as the corpus tests a franchise: its filed price held in the 2023 trough only on
  customers' shortfall payments and then fell 3% and 10.4%, the second time *"where customers are dual sourced"*, while its five-year ROE averaged 5.6%,
  its contracted book halved and its customers' filings name second sources; recorded beneath the close, Q3 finds no integrity disqualifier but fires the
  weak-accounting (material weaknesses 2023-2025), EBITDA and metric-switching flags with US$500M of buybacks paid to the controlling shareholder at
  prices far above value, Q4 is gruesome (owner earnings US$234-519M on valid windows) with THE PASS-THROUGH likely and THE PATRON proposed, and the
  price (US$46.95) sits above the whole multi-year floor range of roughly US$5-25 a share.
- **If UNRESEARCHED — THE WORK ORDER:** none.
- **If UNKNOWABLE:** not applicable.

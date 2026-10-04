# Company Run — InterContinental Hotels Group PLC (IHG) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

**Queue context.** A name in **WAVE 5** of `Screens/WATCHLIST RUN QUEUE.md` (the unpriced watchlist businesses), the last of the
eleven foreign 20-F filers (after TM, SONY, HMC, TSM, UMC, ERIC, SPOT, STLA and GFS, and alongside a concurrent MBGL run). The
2026-09-01 triage skipped it as *"foreign 20-F filer ... short XBRL history."* **Read here as UNLABELLED: a prompt to read the 20-F by
hand, not a verdict.** The run file was created from the template before any fetch (write-early protocol). Research on disk:
`Test Runs/_research 2026-09-13 IHG/`. **No hotel company has been run in this project**; the competitor row is built from the five
US-listed peers' own 10-Ks, and the asset-light franchisor precedent (`2026-09-03 Run - MCD McDonalds.md`) and the restaurant runs are
read as method, not as conclusions about hotels.

**Why the screen could not price it, found rather than assumed.** `companyfacts` (fetched 2026-09-13) carries namespaces **`dei` and
`ifrs-full` (410 tags) only; no `us-gaap`**. IHG reports under **IFRS as issued by the IASB, in US dollars** (20-F FY2025 cover:
*"International Financial Reporting Standards as issued by the International Accounting Standards Board ý"*; Note 1 exchange rates
quoted as *"$ 1 equivalent"*; *"IHG changed the reporting currency of its Consolidated Financial Statements from sterling to US dollars
effective from the Half-Year Results as at 30 June 2008"*). Measured (`probe.py`): `ifrs-full:CashFlowsFromUsedInOperatingActivities`,
`PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities` and `AdjustmentsForSharebasedPayments` each carry **unit USD, eleven
annual periods 2015-12-31 to 2025-12-31, the newest from the FY2025 20-F `0000858446-26-000010`.**
- **The USD-only unit filter is NOT the cause** (the unit is USD).
- **companyfacts lag is NOT the cause** (FY2025 is ingested, filed 2026-02-26).
- **"Short XBRL history" is NOT true**: eleven annual cash-flow periods, more than the five-year default [E2-42] needs and enough for a
  ten-year window.
- **The cause is the tag names:** `python tools/run.py IHG` returns *"IHG: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED."*
  because its lists carry only US-GAAP element names. **GFS's diagnosis exactly: an IFRS filer in USD, blocked by tag names alone.**
- **A second defect the screen would have hit had it got past the first: the `dei` share count is wrong by 12%.** `dei:EntityCommonStockSharesOutstanding`
  reads **164,711,854 for both 2024-12-31 and 2025-12-31**, and **187,717,720 for both 2020-12-31 and 2021-12-31**. The FY2025 20-F cover
  repeats the FY2024 cover's figure, and that figure is **the issued count at 2024-12-31 including 6,241,782 treasury shares** (FY2024 20-F,
  Directors' Report: *"The Company's issued share capital at 31 December 2024 consisted of 164,711,854 ordinary shares of 20 340 ⁄ 399 pence
  each, including 6,241,782 shares held in treasury"*). **ERIC's trap fires here, and fires twice: issued, not outstanding; and a year stale.**
  Counted below by hand.

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

### What the company is, and what 2003 separated
- **Registrant:** InterContinental Hotels Group PLC, England and Wales, CIK 0000858446, ADSs on the NYSE (`IHG`), ordinary shares on the
  London Stock Exchange (`LON:IHG`). Former names in EDGAR: Six Continents PLC (to 2003-03-27) and Bass Public Limited Co (to 2000).
- **The 2003 separation, from the first IHG 20-F** (FY2003, filed 2004-04-08, `0001021231-04-000275`): *"'Separation transaction' or
  'Separation' refers to the transaction that separated Six Continents PLC's hotels and soft drinks businesses from its retail business,
  completed on April 15, 2003. The Separation resulted in two separately listed holding companies: (i) Mitchells & Butlers plc, which is the
  holding company of the retail business and Standard Commercial Property Developments Limited; and (ii) InterContinental Hotels Group PLC,
  which is the holding company for the hotels and soft drinks businesses"*. IHG then held Britvic (soft drinks) as well; the hotel-only,
  asset-light company priced here is the product of two decades of disposals and special returns (below). **Outside every data window
  used in this run.** `deal_note` and `name_change_note` returned nothing (brief); no pending combination found in the 6-Ks of 2025-26.

### The earnings currency, established from the filing
- **Presentation currency US dollars** since 30 June 2008 (above). **Dividends are declared in US cents** and converted to pence for
  payment (6-K 2026-09-11, `0001654954-26-008272`: *"an interim dividend for 2026 of 64.5 cents per share ... resulting in an applicable
  exchange rate of £1:US$1.3547. Accordingly, the amount payable will be 47.6 pence per ordinary share"*).
- **The London line now trades in US dollars. The brief's premise (London in pence) is out of date.** 6-K 2025-12-17
  (`0001654954-25-014037`): *"IHG confirms that a notification has been made to the London Stock Exchange for the currency change to USD to
  take effect from 8.00am (London time) on 2 January 2026. The change does not impact the nominal currency of IHG's shares, which will
  remain in GBP."* Every 2026 buyback report prices purchases in dollars (*"Average price paid per share: | $ 162.7580"*, 24 August 2026).
- **Revenue by location, Note 2 FY2025** (fee business, owned & leased and reimbursable; System Fund excluded by the company): **United States
  $1,965M (56.6%)**, United Kingdom $312M (9.0%), Rest of World $1,195M (34.4%), total $3,472M. **Segment operating profit 2025:** Americas
  **$836M (66% of $1,265M)**, EMEAA $303M, Greater China $99M, Central $27M.
- **Net debt by currency, 2025-12-31** (Performance review, including derivatives): borrowings **US dollar $3,257M**, sterling $1,175M, euro
  $5M; cash sterling $549M, US dollar $442M, renminbi $69M.
- **The judgment [E4-15, E3-32]:** statements, dividends, both quotes and two-thirds of segment profit are in dollars; the largest single
  country is the United States. **The USD sovereign is the natural pairing, and no currency conversion enters any yield below.** Sterling
  cost base and sterling bonds are a margin and translation exposure, carried to Q4, not a reason to change the rate.

### Sovereign — struck fresh 2026-09-13 [E4-15, E3-32]
- **Rate used: USD 30-year 5.35%**, US Treasury daily par yield curve, **09/11/2026** (the issuing authority; `sources.sovereign("USD")`
  returned `(5.35, '09/11/2026', 'US Treasury daily par yield curve')`). The brief's 5.35% is confirmed, not inherited.
- **Stated beside it, not used:** **GBP 20-year nominal par yield 5.65%** (Bank of England database series `IUDLNPY`, 2026-09-09; the BoE
  does not publish a 30-year par series in that database, and the BoE is the central bank, not the Debt Management Office that issues
  gilts: a rung below the issuing authority, flagged); **EUR 30-year 3.83%** (ECB AAA curve SR_30Y, 2026-09-10, `sources.py`). All three
  files: `sov.py`, `boe_IUDLNPY.csv`, `boe_XUDLUSS.csv`.
- **The [E4-28] floor of roughly 10% governs above it** (*"that's true whether short rates are 6 percent or whether short rates are
  1 percent"*).
- **FX: none needed for the cap.** Both quotes are in dollars. Recorded for context only: Bank of England spot `XUDLUSS` **US$1.3531 per £
  (2026-09-10)**; the company's own dividend rate **£1:US$1.3547** (three days from 2026-09-08).
- **ADR ratio, from the filing:** *"Each ADS represents one ordinary share"* (20-F FY2025, Shareholder information). Derived check:
  NYSE ADR close US$153.83 against London close US$153.50 on 2026-09-11, a 0.2% gap across different closing times; ratio 1:1 holds.

### The share count, read by hand and walked forward — the issued-versus-outstanding trap checked explicitly
| date | count | what the filing says | document · accession |
|---|---|---|---|
| 2024-12-31 | 164,711,854 issued, **incl. 6,241,782 treasury** | *"issued share capital at 31 December 2024 consisted of 164,711,854 ordinary shares ... including 6,241,782 shares held in treasury"* | 20-F FY2024, `0001193125-25-037543` |
| 2025 | −7,585,264 cancelled | *"As at 31 December 2025, 7,585,264 shares had been repurchased at an average price of £88.50 per share (approximately £671m)"* | 20-F FY2025, Shareholder information |
| **2025-12-31** | **157,126,590 issued, incl. 5,481,782 treasury** | *"The Company's issued share capital at 31 December 2025 consisted of 157,126,590 ordinary shares of 20 340 / 399 pence each, including 5,481,782 shares held in treasury"* | **20-F FY2025, `0000858446-26-000010`, filed 2026-02-26, Directors' Report** |
| 2025-12-31 (cover) | 164,711,854 "outstanding" | the 2024 issued count, repeated | same 20-F, cover page — **defective** |
| 2026-01-31 | 151,644,808 voting rights | *"issued share capital consists of 157,126,590 ordinary shares ... of which 5,481,782 ordinary shares are held in treasury. Therefore, the total number of voting rights in the Company is 151,644,808"* | 6-K 2026-02-02, `0001654954-26-000805` |
| 2026-02-17 | programme | *"a share buyback programme ... with aggregate value of up to USD 950 million ... The purpose of the Programme is to reduce the issued share capital of the Company and the Shares purchased will be cancelled"* | 6-K 2026-02-17, `0001654954-26-001292` |
| 2026-08-31 | 153,593,895 issued, 5,431,782 treasury, **148,162,113 voting rights** | Total Voting Rights and Capital, as at 31 August 2026 | 6-K 2026-09-01, `0001654954-26-008027` |
| **2026-09-03** | **147,858,757 in issue excluding 5,431,782 treasury** | *"Following the above transaction, the Company has 147,858,757 ordinary shares in issue (excluding 5,431,782 held in treasury)"* (purchase of 100,927 at an average US$159.6006) | **6-K 2026-09-04 (batch), `0001654954-26-008134`** — the last filed purchase report |

- **Walk, reconciled by arithmetic** (`bb.py`, 131 daily purchase reports parsed, `bb_out.json`): 3,836,051 shares bought 17 Feb - 3 Sep 2026
  for about **US$579M** at an average of about US$151. 151,644,808 − 3,836,051 = 147,808,757; the filed 147,858,757 is 50,000 higher,
  and the treasury balance fell by exactly 50,000 (5,481,782 → 5,431,782): **treasury shares transferred to the employee trust**, which
  moves them from "treasury" into "in issue". **Reconciles to the share.**
- **The ERIC trap, checked, and it FIRES — on the cover, not in the notes.** The 20-F cover field that asks for *"outstanding"* shares carries
  the **issued** count **including treasury**, and in FY2025 it is **the prior year's** issued count. The Directors' Report, the Total Voting
  Rights 6-Ks and the buyback reports are consistent with each other and are used.
- **Employee benefit trust — the filing treats its shares as not outstanding for EPS.** Note 10: basic shares = *"Weighted average number of
  ordinary shares in issue | 161.0"* less *"Weighted average number of treasury shares a | ( 6.6 )"*, footnote *"a. Includes other shares
  that do not receive dividends."* Directors' Report: *"at 31 December 2025, it [the ESOT] held 860,969 ordinary shares in the Company"*;
  the trustee *"has a policy of not voting"*. A further *"178,309 forfeitable shares"* sit with a nominee, allocated to participants who
  direct the votes: **kept in the count** (allocated to named people). **The ESOT's 860,969 are deducted**; the H1 2026 interim report gives
  no updated trust holding, so the year-end figure is the latest filed. The H1 2026 basic weighted average (**150.0 million**, 6-K
  2026-08-11, `0001654954-26-007436`) is consistent with a falling count through the year.
- **Count used: 146,997,788** = 147,858,757 (2026-09-03, filed) − 860,969 (ESOT, 2025-12-31, filed). Without the trust deduction:
  147,858,757 (+0.6%).
- **Not in the count, stated:** purchases 4-11 September 2026 (not yet reported; at the 2026 pace of roughly 100,000 a day, about 0.4M
  shares, 0.3%); share awards outstanding, carried to Q4 as SBC (*"As at 31 December 2025, there were no options outstanding"*); no
  convertible found.
- **Share consolidations — the split-invariant rule.** The 20-F's return-of-funds and dividend tables mark special returns *"Accompanied by a
  share consolidation"* in 2004, 2005, 2006, 2007, 2012, 2014, 2016, 2017 and the $500M special dividend *"Paid in January 2019"*. The flagged
  quote series lists the last ADR consolidation as **949:1000, January 2019** (London line 19:20). **No consolidation after the 2026-09-03
  measurement date**, so `close(anchor) × shares(measurement) × splits after measurement` holds with a factor of 1. **Any per-share series
  across 2019 is not comparable without the factor; the run uses totals, not per-share figures, for every multi-year comparison.**

### The price and the cap (aggregator for live quotes only, flagged)
- **Price US$153.83**, IHG ADS NYSE close **2026-09-11** (Yahoo Finance chart API, `regularMarketTime` 2026-09-11 20:00 UTC; **aggregator,
  flagged**; `px2.py` / `prices_daily_2026-09-13.json`). London line close the same day **US$153.50** (LSE, 15:47 UTC last print).
- **Cap = US$153.83 × 146,997,788 = US$22,613M** (US$22,745M without the trust deduction; **US$25,338M on the defective cover count, 12.1%
  too high**).
- **Price context, from the company's own purchase reports:** it paid **US$143.04** (17 Feb 2026) to **US$164.85** (26 Aug 2026) a share in
  2026, and **£76.60-£103.01 a month on average** in 2025 (20-F FY2025 monthly table). Net debt at 2025-12-31 **US$3,333M** (company
  definition, Performance review), so the enterprise the buyer pays for is roughly **US$26bn**.

### The filing was read — not tagged data **[E3-27, E4-14]**
- [x] MD&A (Performance review: Group, regions, cash flow summary, net debt by currency, capital allocation) [x] cash-flow statement incl. detail lines
  (Group statement of cash flows and Note 25 reconciliation, FY2019, FY2021, FY2022, FY2025; H1 2026 interim) [x] footnotes (accounting policies on key
  money, deferred revenue, loyalty and the System Fund; Notes 1, 2, 3, 10, 21, 22, 25, 27, 28, 31; legal proceedings; risk factors; remuneration report)
- **Primary document: Form 20-F (Annual Report and Form 20-F 2025), fiscal year ended 2025-12-31, filed 2026-02-26, accession
  `0000858446-26-000010`, `ihg-20251231.htm`, CIK 0000858446.** Auditor PricewaterhouseCoopers LLP, Birmingham.
- **Also on disk:** 20-F FY2024 `0001193125-25-037543` · FY2023 `0001193125-24-051757` · FY2022 `0001193125-23-057355` · FY2021
  `0001193125-22-063939` · FY2020 `0001193125-21-068584` · FY2019 `0001193125-20-052322` · FY2018 `0001193125-19-055722` · FY2003
  `0001021231-04-000275`; every 6-K from 2025-02-03 to 2026-09-11 (84 filings, `k/`), including the FY2025 results, the H1 2026 half-year
  report (`0001654954-26-007436`), the Q1 2026 and Q3 2025 trading updates, 131 daily buyback reports and the Total Voting Rights notices.
- **Figure cross-checked against the filed statement:** **Net cash from operating activities US$898M for 2025** in the audited Group statement
  of cash flows (page 182: *"Net cash from operating activities | 898 | 724 | 893"*) equals `companyfacts`
  `ifrs-full:CashFlowsFromUsedInOperatingActivities` 2025-12-31 **USD 898,000,000** (accession `0000858446-26-000010`). **Note what that line is
  under IFRS here:** it is **after interest paid (US$202M) and tax paid (US$307M)**, and **key money is inside it** (the company's own
  reconciliation adds back *"Capital expenditure: contract acquisition costs net of repayments | 179"*). Both facts are carried to Q4.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### What the 20-F says the money is, in three streams that must be kept apart
**2025 revenue, Note 3 (disaggregation) and the business model section, 20-F FY2025 `0000858446-26-000010`:**

| stream | 2025 $M | what it is, from the filing | whose money |
|---|---|---|---|
| Franchise and base management fees | 1,371 | *"We receive franchise fees based upon a fixed percentage of rooms revenue"*; managed: *"Fixed % of total hotel revenue as a management fee"* | IHG shareholders |
| Incentive management fees | 190 | *"typically a share of hotel gross operating profit after deduction of management fees"* (EMEAA 134, Greater China 36, Americas 20) | IHG shareholders, cyclical |
| Central revenue | 336 | *"principally from technology fee income and ancillary revenues including co-brand licensing fees and ... a portion of revenue from the consumption of certain IHG One Rewards points"* | IHG shareholders |
| **Revenue from fee business** | **1,897** | operating profit **$1,231M**, fee margin **64.8%** | |
| Owned & leased hotels | 544 | *"we record the entire revenue and profit of the hotel"*; **17 hotels, 4,191 rooms**; operating profit **$43M** | IHG shareholders, low margin |
| Insurance activities | 27 | captive | |
| **System Fund revenues** | **1,717** | owners *"pay assessments into it ... a marketing and reservation assessment and a loyalty assessment"*; *"The System Fund is not managed to surplus or deficit for IHG over the longer term, but for the benefit of hotels in the IHG system"* | **hotel owners' money, spent on their behalf** |
| Reimbursable revenues | 1,004 | managed-hotel staff costs *"shown as revenue with an equal matching employee cost, with no profit impact"* | pass-through |
| **Total revenue** | **5,189** | | |

**Only $2,468M of the $5,189M (48%) is the shareholders' business**, and the System Fund result (−$46M in 2025) and reimbursables are
excluded from segment profit because *"System Fund and reimbursable revenues and results are therefore not regularly reviewed by the
Chief Operating Decision Maker"* (Note 2).

### The unit economics, in my own words
- **A hotel owner builds or buys the hotel, carries the debt, employs (or pays for) the staff and bears the occupancy risk. IHG rents
  them a brand, a reservation system and a loyalty programme, and takes a slice of the room revenue off the top.** It owns 17 of 6,963
  hotels (Q4 2025 results 6-K, `0001654954-26-001290`: *"Franchised a | 5,886 ... | 748,178 | Managed | 1,060 ... | 273,808 | Owned &
  leased | 17 ... | 4,191"* rooms; *"a. Includes exclusive partner hotels"*). **73% of rooms franchised, 27% managed, 0.4% owned.**
- **The owner pays twice.** Fees to IHG (**$1,897M, 5.4% of the $35.2bn "total gross revenue in IHG's system"**) and assessments into
  the System Fund (**$1,717M, 4.9%**): **roughly a tenth of every hotel dollar**, before reimbursables. *(Arithmetic on filed figures; the
  gross-revenue base is the company's own non-GAAP measure, 20-F FY2025 "2025 in review".)*
- **A room adds fee revenue at almost no cost to IHG.** Fee revenue per open room was about **$1,850** in 2025 ($1,897M / 1,026,177 rooms,
  arithmetic). Americas fee margin **83.4%** (*"more than 90% of our hotels operating under our franchised model"*), EMEAA and Greater China
  lower because they are managed-weighted. The two drivers, in the filing's own words: *"increasing revenue per available room (RevPAR);
  and – expanding the number of rooms in our system."*
- **The price of adding a room is key money, and it is inside operating cash flow.** *"Amounts paid to hotel owners to secure management
  and franchise agreements ('key money') are treated as consideration payable to a customer. A contract asset is recorded which is
  recognised as a deduction to revenue over the initial term of the agreement."* Cash paid, net of repayments: **$61M (2019) → $64M
  (2020) → $42M → $64M → $101M → $237M (2024) → $179M (2025)** (Note 25 in each 20-F: *"Contract acquisition costs, net of repayments"*,
  a line inside *"Cash flow from operations"*). Contract assets on the balance sheet **$798M** at 2025-12-31 (non-current $751M, current
  $47M); the revenue deduction was **$52M** in 2025. **Key money almost tripled from 2023 to 2024 while net rooms growth moved from 3.8% to
  4.3%**: how much of it buys growth and how much buys retention is the (c) judgment at Q4.
- **The System Fund is float for the owners, with a structural accounting loss.** Loyalty assessments are deferred until members consume
  the points, so *"more revenue is deferred each year than is recognised in the Fund. This can lead to accounting losses in the Fund each
  year as the deferred revenue balance grows."* Deferred revenue on the balance sheet **$2,169M** (current $829M, non-current $1,340M),
  up $107M in 2025 and $214M in 2024. **The fund's cash sits inside IHG's consolidated operating cash flow**; Q4 strips it out.
- **Where IHG and the owners divide the fund, and it has moved once in IHG's favour.** From 2024, *"as agreed with the IHG Owners
  Association, a portion of revenue relating to the consumption of certain points sold is reported within fee business revenue"*: 50% of
  points sold to consumers in 2024 and 100% from 2025 (*"approximately $25m incrementally to revenue and operating profit from reportable
  segments in 2024"*, 20-F FY2024, *"approximately doubling the benefit"* in 2025). **About $50M of the 2025 fee business came across from
  the owners' fund by agreement.** Recorded here as the mechanism; weighed at Q2 and Q3.
- **Ancillary streams are the growth part of central revenue:** co-brand credit cards (upfront payments of $100M in 2024 and $37M in 2025
  *"which will be recognised over the term of those agreements"*), points sales, branded residences. Central revenue went **$239M → $336M
  (+41%)** in 2025.

### The scarce input this business controls
**A demand-generating system that an owner cannot build alone: 21 brands, the reservation channels and a loyalty programme of
*"over 160 million members who are responsible for 66% of room nights consumed globally"*, with *"83% of room revenue booked through
IHG-managed channels and sources"*** (20-F FY2025). The hotels, the land and the staff are not scarce and IHG does not own them. **Whether
the system is scarce to the owner, i.e. whether owners have a close substitute, is Q2's question, not Q1's**; Q1 needs only that the input
be nameable and the mechanism be understood, and both are.

### Scale and history, from the filings
| | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| Fee business revenue $M | 1,379 | 1,486 | 1,510 | 823 | 1,153 | 1,434 | 1,672 | 1,774 | 1,897 |
| Fee business op. profit $M | 731 | 793 | 813 | 278 | 570 | 805 | 992 | 1,085 | 1,231 |
| System gross revenue $bn | | | 27.9 | 13.5 | 19.4 | 25.8 | 31.6 | 33.4 | 35.2 |
| Global RevPAR change | | | −0.3% | **−52.5%** | +46.0% | | +16.1% | +3.0% | +1.5% |
| Net system size growth | | | +5.6% | +0.3% | −0.6% | +4.3% adj. | +3.8% | +4.3% | +4.0% (4.7% adj.) |
| Rooms at year-end | | | 883,563 | | | | | 987,125 | 1,026,177 |

*Sources: fee margin reconciliations in the 20-F FY2021 (2017-2021; 2021 re-presented to $1,144M for IFRS 17 in FY2023) and FY2023/FY2025
(2022-2025); system gross revenue: 20-F FY2020 (*"$ 13.5 bn 2019: $27.9bn"*), FY2021, FY2022, FY2023, FY2024 and FY2025 KPI pages; RevPAR and
net system size growth from the KPI pages of each 20-F; rooms 2019 from 20-F FY2019 (*"IHG System size increased by 5.6% to 883,563 rooms"*),
2024-2025 from the Q4 2025 results 6-K. Gaps are where the figure was not read in a comparable form, not where it does not exist.*

**The 2020 test, first look (the full [E2-44] read is Q2's):** RevPAR fell **52.5%**, fee business revenue fell **45.5%** ($1,510M → $823M),
and the system still grew **0.3%**. Fee business operating profit fell **66%**, because the cost base did not fall with revenue. **The
fee is a percentage of the owner's revenue, so IHG's revenue is exactly as cyclical as hotel revenue, less a cushion of fixed per-room
technology fees**; what it does not carry is the owner's operating leverage.

### Will the fundamentals look broadly the same in ten years?
**Yes, on the filed record.** The model, a percentage of hotel revenue for brand, distribution and loyalty, is the one every 20-F read
here describes from FY2018 to FY2025, and the capital-return table shows the owned estate and Britvic being turned into special returns
from 2004 onward (the 2003 company still held *"the hotels and soft drinks businesses"*; its own description of the fee model was not read
in the FY2003 document and is not claimed). The drivers (RevPAR, rooms) and the risks (owner economics, distribution intermediaries, loyalty competition,
travel cycles and shocks) are the same list in 2019 and 2025. **What could change the shape** is named and carried forward, not treated
as a Q1 failure: the direct-booking share against online travel agencies and AI-driven distribution (principal risk, *"The pace of
development in AI, generative AI and cloud platforms ... creates uncertainty"*); and the division of the loyalty economics between IHG and
the owners, which moved once in 2024.

### What would make this Q1 UNKNOWABLE, checked
- **Perimeter:** Ruby acquired for **$120M** (*"Purchase of brands | ( 120 )"*, 2025); Six Senses and Regent (2019: *"Acquisition of
  businesses, net of cash acquired | (292 )"*); Iberostar a commercial agreement (2022). **None changes what the company is**; each is
  displayed at Q4. No combination pending in the 6-Ks of 2025-26.
- **Accounting complexity:** two critical audit matters, **loyalty breakage** and **the allocation of expenses to the System Fund**
  (*"the significant judgment by management when developing the Group's internal policies in order to apply the principles agreed with
  the IHG Owners Association to expenses incurred"*, PwC, 16 February 2026). **Both sit inside the owners' fund, which Q4 separates**, and
  both are read at Q3 as prompts; neither makes the shareholders' fee stream hard to understand.
- **[E4-46] (five minutes, not five months):** the business fits in one sentence (a toll on hotel room revenue for a brand and a loyalty
  system, paid by owners who carry the property) and the difficult parts are named documents, not competence.

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  *IN on the filing: the three streams are separated by the company itself, the mechanism is stated in its words, the scarce input is
  nameable, and the model has been the same for two decades. Whether owners have a close substitute is Q2's.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The question put at the right altitude first, as the MCD run put it (2026-09-03): IHG's customer is the HOTEL OWNER, not the guest.** The
owner pays the fees and the fund assessments; the guest pays the owner. So [E3-03] asks whether **hotel owners** think the IHG system has *"no
close substitute"*. **And the one structural difference from McDonald's is the whole question:** McDonald's *"maintains control of the underlying
real estate and building"* at the end of each 20-year term; **IHG owns 17 of 6,963 hotels**, and at the end of a term the building stays with the
owner, who can fly another brand's flag over it.

- **Needed or desired [x]** — brand affiliation is the norm where IHG earns most: *"In 2025, approximately 73 percent of U.S. hotel rooms were
  brand-affiliated"* (Marriott FY2025 10-K, Item 1); IHG's system turned over **$35.2bn** of hotel revenue in 2025 and **66% of room nights** came
  from its loyalty members.
- **No close substitute [ ] — FAILS, on the evidence below.**
- **Not price-regulated [x]** — fees are private contract terms. (US state franchise laws regulate disclosure and termination, not price:
  Wyndham FY2025 10-K, *"imposing limits on a franchisor's ability to terminate franchise agreements or to withhold consent to the renewal"*.)

### The evidence on criterion 2, from IHG's own filings first
1. **IHG says owners have the bargaining position and that renewal terms may worsen.** 20-F FY2025, Risk factors: *"Competition with other hotel
   companies may generally reduce the number of suitable franchise, management and investment opportunities offered to the Group and increase the
   bargaining position of property owners seeking to become a franchisee or engage a manager. The terms of new franchise or management agreements
   may not be as favourable as current arrangements; the Group may not be able to renew existing arrangements on similarly favourable terms, or at
   all."*
2. **IHG pays owners to sign, and the price rose fastest exactly when growth was being bought.** Key money net of repayments: **$61M (2019), $64M,
   $42M, $64M, $101M, $237M (2024), $179M (2025)** (Note 25/26 in each 20-F). The company's own purpose statement: *"to secure representation for
   our brands in prime locations"*.
3. **IHG has cut owners' prices, not raised them — twice in the six years read.** 2020: *"Supplier discounts, fee relief and flexible payment
   options have all helped protect our owners' cash flow"* (20-F FY2020). **2024, in a year of +3.0% RevPAR**: *"We also lowered our standard loyalty
   assessment fee for owners during 2024, increased certain Reward Night reimbursements they receive back out of the System Fund when points are
   redeemed for stays and reduced the IHG ® Ignite marketing fee for participating hotels in the Americas and EMEAA"* (20-F FY2024). **[E4-37]:**
   *"you can almost measure the strength of a business over time by the agony they go through in determining whether a price increase can be
   sustained"*; this is the other side of that measure — a price **cut** to owners in a good year.
4. **What IHG gained in exchange was a re-division of the owners' fund, negotiated with the owners' association — also twice.** 2020: *"following
   communication with the IHG Owners Association ... Revenue arising from the licence of intellectual property under co-brand credit card agreements
   previously recorded within the System Fund was moved into Central revenue"* (+$20M revenue, +$21M segment profit in 2020, 20-F FY2021 Note 3).
   2024-25: points revenue *"as agreed with the IHG Owners Association"* (about $25M in 2024, about double in 2025). **The shareholders' take grew by
   bargaining with an organised counterparty, which is what a party with a close substitute does, not a party without one.**
5. **Owners sued the franchisor as a class.** *"Seven claims were filed in March 2022 against HHF, Six Continents Hotels, Inc., and the IHG Owner's
   Association, seeking class action status on behalf of the Group's franchisees ... The claims allege that the Group as franchisor, is engaged in
   unlawful business practices relating to numerous programmes, products and requirements"*; IHG won (*"dismissed with prejudice on 20 May 2025"*).
   Recorded as friction between franchisor and franchisees, **not** as a finding against IHG.
6. **The core toll, measured the only way IHG's filings allow (no royalty rate is disclosed in any 20-F read, FY2018-FY2025, recorded under the
   absence-claim rule as "not found").** Franchise and base management fees ÷ total gross revenue in IHG's system (Note 3 ÷ the company's KPI):
   **4.21% (2019), 4.49% (2020), 4.61% (2021), 4.45% (2022), 4.13% (2023), 4.06% (2024), 3.89% (2025)** — arithmetic. **Down 32bp from 2019 to 2025**
   (24bp with key money's revenue deduction added back). **Its limit, stated:** the denominator includes food and beverage at managed hotels and a
   changing regional mix (EMEAA and Greater China, where rates are lower, grew), so this is a proxy, not a rate; the franchised share of rooms *rose*
   from 69.6% to 72.9% over the same years, which should have pushed the ratio up. Including incentive and central fees, fee business revenue was
   **5.41% (2019) → 5.39% (2025)**, and about **5.25%** without the fund re-division.
7. **The counter-evidence, stated as strongly as I can [E4-51].** Owners rarely leave mid-term: removals ran *"in line with our historical underlying
   average"* of **1.5%** (2023) and 1.9% adjusted (2024, 2025) — an implied life of a hotel in the system of fifty years or more (arithmetic). **Through
   2020 the system still grew +0.3% (+2.2% excluding the terminated SVC management portfolio of 16.7k rooms)** and fee revenue fell less than RevPAR
   (−45.5% against −52.5%). **66% of room nights** come through IHG One Rewards and **83% of room revenue** through IHG channels — an independent owner
   who leaves gives that up. **These show switching is costly inside a term. They do not show owners lack a close substitute at the term** — the
   substitute is another brand family, which is exactly what the competitor filings below say they are.

### THE COMPETITOR ROW — required [E3-28]. Same metrics, filed, 2019 / 2020 / 2025
*Five SEC filers, full rows with every accession in `peers/*_row.md` (transcription only; companyfacts cross-checks matched on every peer). **Accor
does not file with the SEC** (no CIK; its registration documents are on the AMF rung of the evidence ladder, not fetched): **six of the seven
global systems taken**, and Accor's absence is stated rather than filled from memory.*

| | **IHG** | Marriott | Hilton | Hyatt | Wyndham | Choice |
|---|---|---|---|---|---|---|
| Rooms, YE2019 → YE2025 (000) | **884 → 1,026** | 1,381 → 1,780 | 972 → 1,351 | 223 → 373 | 831 → 869* | 591 → 657 |
| Rooms CAGR 2019-25 (arith.) | **2.5%** | 4.3% | 5.7% | 8.9%† | 0.8%* | 1.8% |
| Net rooms growth 2020 (filed or arith.) | **+0.3%** | +3.1% (arith.) | +5.1% | +5.5% (arith.) | −4% | +1.2% (arith.) |
| Net rooms growth 2025 | **+4.0% (4.7% adj.)** | +4.3% (arith.) | +6.7% | +7.3% (arith.)† | +4% | +0.5% (arith.) |
| RevPAR 2020 vs 2019 | **−52.5%** | −60.2% | −56.7% | −65.4% | −40% | −30.7% (US) |
| Fee revenue 2020 ÷ 2019 (arith.) | **0.545** | 0.440 | 0.493 | 0.393 | 0.648 | 0.678 (royalties) |
| **Disclosed royalty rate 2019 → 2020 → 2025** | **not disclosed** | not disclosed (*"four to seven percent of room revenues"*) | not disclosed; *"increases of in-place rates"* 2025 | not disclosed | **3.80% → 4.0% → 3.98%** global; US 4.5% → 4.5% → 4.76% | **US 4.86% → 4.94% → 5.14%** |
| Owner-price action 2024-25 | **cut loyalty assessment and Ignite fee (2024)** | — | in-place rates raised, RevPAR +0.4% | — | global rate −2bp, US +7bp | +8bp while US RevPAR −3.0% |
| Key money / contract acquisition, 2021 → 2025 ($M) | **42 → 179** | 210 → 434 | 200 → 231 | n/d → 134 | 32 → 112 (advances) | 38 → 83 |
| Loyalty members, 2025 / share of nights | **160M / 66%** | n/f / 68% global | 243M / n/f | 63M / 49% | 122M / 37% of check-ins | 74M / n/f |
| Typical franchise term | **not found in the FY2025 20-F** | 10-25 yrs | ~20 yrs new, 10-20 conversions | 20 yrs | 10-20 yrs | 10-30 yrs, with anniversary exits |
| Equity at YE2025 | **−$2,736M** | −$3,771M | −$5,359M | +$3,334M | +$468M | +$181M |
| Key money in the cash-flow statement | **operating** | operating | operating | operating | operating | operating |

*\*Wyndham recast its system to exclude Super 8 China from 2021; 2019 is as originally reported. †Hyatt includes acquisitions (ALG 2021, Playa 2025).
n/f = not found in the documents read; n/d = not disclosed as a line for that year. Sources: `peers/MAR_row.md`, `HLT_row.md`, `H_row.md`, `WH_row.md`,
`CHH_row.md` (FY2019, FY2020, FY2021, FY2024, FY2025 10-Ks, accessions listed there); IHG from the 20-Fs above.*

**What the row shows, metric by metric:**
- **Position, not dominance.** IHG's share of the six systems' rooms: **18.1% (2019) → 16.9% (2025)**; of the big three (IHG, Marriott, Hilton): **27.3% →
  24.7%** (arithmetic). **The direction is narrowing [E4-32, E4-55]** — in units, which is where [E4-55] says to look: IHG grew rooms 2.5% a year while
  Hilton grew 5.7% and Marriott 4.3%.
- **Every competitor names the others and says owners choose on price.** Marriott names *"Hilton, IHG Hotels & Resorts, Hyatt, Wyndham Hotels &
  Resorts, Accor, Choice Hotels, Best Western"* and says terms depend on *"the relative value and benefits of offerings otherwise available to hotel
  owners in the market"*; Hilton lists *"Intercontinental Hotel Group"* among its primary competitors and warns of *"negative pricing trends in the
  industry for management and franchise and related fees"*; Hyatt competes on *"the royalty fees charged"*; Wyndham: *"Competition may reduce fee
  structures, potentially causing us to lower our fees and/or offer other incentives"*; Choice: *"competition may require us to reduce or change fee
  structures, make greater use of financial incentives"* (all FY2025 10-Ks, Items 1 and 1A). **Hilton's brand table names Holiday Inn Express as a
  selected competitor of Hampton, and Crowne Plaza and Holiday Inn of DoubleTree.**
- **Owners do switch, at scale, between these systems.** Marriott: *"roughly 75,300 rooms converted from competitor brands"* (2024), *"roughly 33,400"*
  (2025); IHG: *"Conversions represented around half of openings"* (2025). A conversion into one system is a removal from another.
- **Through 2020 [E2-44], IHG held up in the middle, not at the top.** Its fee revenue ratio (0.545) beat Marriott, Hilton and Hyatt, whose luxury and
  urban mix fell harder, and trailed Wyndham and Choice, whose economy and midscale US roadside hotels fell least. **Relative to RevPAR** (fee decline
  ÷ RevPAR decline, arithmetic): IHG 0.87, Hilton 0.89, Wyndham 0.88, Marriott 0.93 — **no IHG-specific cushion.** And the rate itself: **Choice's filed US
  royalty rate rose in 2020 (4.86% → 4.94%) and in 2025 as US RevPAR fell 3.0% (5.06% → 5.14%)** — that is [E2-44](1), a price rise *"even when product
  demand is flat and capacity is not fully utilized"*, on the filed record. **IHG's filings show no disclosed rate, a flat-to-falling toll proxy and a
  2024 fee cut.**
- **[E2-44](2), dollar volume with minor additional capital: passes, for IHG and for the whole row** — the asset-light model is the industry's, not
  IHG's alone (negative equity at IHG, Marriott and Hilton from buybacks funded by the same kind of fee stream).

### The other Q2 tests
- **[E4-04], must the moat be continuously rebuilt?** No, in its basis: brands and a loyalty programme are defended, like Coca-Cola's advertising, not
  replaced like an ore body. **But does a lapse in spending destroy or narrow it [the scope test]?** Key money is the defence spending, and its
  quadrupling while share fell says the defence costs more each year to hold a narrowing position. **Great-manager dependence [E4-23]:** none found; the
  system runs with a CEO change (Keith Barr to Elie Maalouf, 2023) and no filed disruption.
- **[E3-33] untapped pricing power:** **no** — the 2024 filing records the opposite action, and [E5-28] reserves the class for *"a monopoly or a near
  monopoly"*; a 17% share of six systems is neither.
- **[E2-45] the attacker's test:** already being run, in the filings, by two larger attackers with bigger loyalty programmes and rising key money
  (Marriott $434M, Hilton $231M in 2025).
- **[E2-53] the dominance class:** no; no market in the row is described by any filer as having one winner.
- **[E3-46] returns on capital:** very high, and **industry-wide** — capital employed is small or negative across IHG, Marriott and Hilton, financed by
  owners' buildings and owners' loyalty float. A high return shared by six competitors for the same owners is the structure's return, not IHG's moat.
- **The row's limit [E3-61]:** it shows position, rates and actions; it cannot show how Marriott and Hilton will conduct the bidding for owners, and
  Accor (not an SEC filer) is outside it. **Neither limit changes the finding**: IHG's own filing and actions, not the peers', carry criterion 2.

- **Primary moat metric, filing-sourced, and its trend:** share of the six systems' rooms, **18.1% → 16.9%** (2019-2025); core toll proxy **4.21% →
  3.89%**; key money **$61M → $179M**. All three move the same way.
- **Class: [ ] WIDE [ ] NARROW [x] NONE (at the owner level) [ ] PROVISIONAL** · **Direction: narrowing.** *(The branded systems together hold a real
  advantage over independent hotels — 73% of US rooms are affiliated — but [E3-03] is asked of IHG's product, and hotel owners have at least five close
  substitutes that bid for the same buildings.)*
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  **OUT on [E3-03] criterion 2 as [E2-44](1) and [E4-37] test it**: hotel owners have close substitutes, and IHG's filed conduct is that of a seller
  facing them — rising payments to win contracts, fee cuts to owners in a year of RevPAR growth, fee-business gains obtained by negotiation with the
  owners' association, a filed warning that renewals may be on worse terms, and a share of the branded systems that has fallen for six years while a
  peer raised its filed royalty rate through 2020 and 2025. **Not UNKNOWABLE:** the documents that would resolve it were read, and they agree. **Not
  UNRESEARCHED:** Accor's absence does not bear on criterion 2, which IHG's own filings answer.

---
⛔ **THE FILE CLOSED AT Q2. Everything below is RECORDED, NOT GOVERNING** (operator protocol, rule 2; the queue's instruction that every run end with a
price and a pass/fail line). Q3 and Q4 are written because the evidence was gathered before Q2 closed and because the brief's questions about the
System Fund, key money and capital allocation are answered there; **no finding below can reopen Q2.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — RECORDED, NOT GOVERNING (file closed at Q2)
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE.**
- [x] **Daily execution** — the loyalty programme, distribution, brand standards and the bidding for owners are run every day, and Q2 found a
  business, not a franchise: *"a business, unlike a franchise, can be killed by poor management"* **[E3-43]**
- [ ] **Control** — no; a minority public holding, no controlling shareholder
- [ ] **Leverage** — moderate against cash flow (2.5x the company's EBITDA measure, 6.6x interest coverage), not a 20:1 balance sheet **[E3-29]**

**Case declared: BINARY GATE**, on daily execution as [E3-43] draws the line after a Q2 OUT (the GFS precedent). It governs nothing here.

**Honesty — binary, permanent, filings-based [E5-16].** Each matter dated to when it became public (20-F FY2025, Legal proceedings, as of 12 February 2026):
- **Franchisee class action**, filed March 2022, alleging *"unlawful business practices relating to numerous programmes, products and requirements"* —
  **ruled for IHG 9 December 2024, dismissed with prejudice 20 May 2025.** No finding against the company.
- **Antitrust class actions** (February and March 2024) against IHG *"and other hotel companies as well as revenue management software providers"*,
  alleging exchange of forward-looking information — **pending, motions to dismiss filed**; an industry-wide allegation, not adjudicated.
- **OTA price-display class action** (30 June 2025), **conversion-hotel franchise-law suit** (18 December 2025), **Canadian data-breach class action**
  (amended March 2018) — pending, unquantified.
- **Middle East opening-delay arbitration** (filed 11 December 2022) — *"The parties finalised a commercial resolution and the arbitration proceedings
  were terminated on 2 October 2025."*
- **No restatement:** the 20-F cover's box for *"the correction of an error to previously issued financial statements"* is unticked. **No integrity
  disqualifier found.** *A Q3 pass is the absence of found disqualifiers, not a finding that the managers are honest [E5-17].*

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30, E2-49].** *Each a prompt to read, never a verdict [E5-36, E5-38].*
- [x] **weak accounting — prompt, not a finding.** Two critical audit matters sit where *"'earnings' can be created by the stroke of a pen"* **[E2-50]**:
  **loyalty breakage** (*"the significant judgement and estimation by management when projecting members' future consumption activity"*) and **the
  allocation of expenses to the owners' System Fund** (*"the significant judgment by management when developing the Group's internal policies in order
  to apply the principles agreed with the IHG Owners Association to expenses incurred"*, PwC). **Every dollar of cost moved into the fund is a dollar of
  shareholder profit paid by owners**; the auditor tested it and found nothing to report. **Operating exceptional items in most years** ($186M 2019, $270M 2020, $100M of *"other operating exceptional items"* 2022, a $28M credit in 2023, none in 2024, $21M 2025, the last including a *"global efficiency programme"* with $10M more *"charged to the System Fund"*): real costs, kept inside owner
  earnings [E3-53, E5-33]. **And the cockroach on the SEC cover [E4-22]:** *"the number of outstanding shares ... as of the close of the period"* was given as
  **164,711,854 in both FY2024 and FY2025** — the 2024 issued count including treasury shares, **12.1% above the true economic count**, repeated unchanged
  a year later (dei also repeats 187,717,720 for 2020 and 2021). A disclosure error, not a financial-statement error; recorded as a prompt.
- [ ] **unintelligible footnotes** — no; the System Fund, key money and the Owners Association agreements are explained plainly.
- [x] **trumpeted projections / growth targets [E3-48], checked against outturn.** A *"growth algorithm"* runs through every report since 2023 and sets
  the EPS targets in pay; *"the 100–150bps average annual improvement [in fee margin] that is expected on a medium- to long-term basis"*; branded
  residence fees *"expected to be substantial in 2027 and beyond"*. **The record of the people who made them:** fee margin **delivered** (54.1% in 2019
  → 64.8% in 2025, +360bps in 2025 alone). **Net system size growth not delivered against the stated ambition**: *"our ambition to deliver industry-leading net System size growth"* (20-F FY2020) and *"our ambition of industry-leading net rooms growth"* (20-F FY2021) against a filed outturn of **2.5% a year 2019-25** versus Hilton **5.7%** and Marriott **4.3%** (Q2 row);
  the LTIP's relative NSSG leg vested *"between threshold and maximum"*. **Mixed: the cost promise kept, the growth promise missed.** No quarterly
  earnings guidance found.
- [ ] **serial share issuance [E5-15]** — no; the share count fell from 183M issued (1 January 2023) to 153.6M (31 August 2026) by cancellation.
- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRES as a prompt.** *"Adjusted EBITDA a | 1,332 | 1,189"* is reconciled in the performance
  review, **the capital-return policy is written on it** (*"net debt:adjusted EBITDA, where we aim for a ratio of 2.5–3.0x"*), and the headline is
  *"+16% Adjusted EPS b growth"* against basic EPS 490.9¢. The corpus's objection bites harder than usual here: IHG's "capital" is key money, which
  EBITDA adds back (*"Capital expenditure: contract acquisition costs net of repayments | 179"* is an add-back in the EBITDA reconciliation).
- [ ] **filed-figure tells [E4-30]** — cash tax paid ÷ profit before tax: **24.1% (2023), 34.4% (2024), 28.6% (2025)** (arithmetic; not falling); reported
  growth not smooth (2020 loss). Not fired.
- [x] **metric-switching [E2-49] — FIRES, with reasons given.** After 2020: *"Total gross revenue (TGR) has been removed from the LTIP metrics for the
  2021/23 cycle. TGR is heavily impacted by the pace of market RevPAR recovery which is very unpredictable and outside of management's control"* (20-F
  FY2020) — a yardstick discarded after it read badly, announced with reasons for future cycles (the candor half of [E2-49]). **Adjusted free cash flow
  re-presented upward** in the FY2024 20-F (2023: $819M → $837M; 2022: $565M → $615M). **Committee discretion used in both directions:** Ruby integration
  costs excluded from the 2025 APP operating profit outcome (*"approximately 1% lower as a proportion of target"* without it); people targets removed
  from the 2023-25 LTIP without replacement. **The [E2-49] prior fires here; its running tally (RESUME STATE §6) is recorded in the reading list as stale and is not restated.**
- For every box ticked, the filing's words are above.

**Incentives, and what pay vests on [E4-27].** *"Never, ever, think about something else when you should be thinking about the power of incentives."*
- **Annual bonus (APP):** operating profit from reportable segments, **room openings and room signings** (20-F FY2024: *"(operating profit from reportable
  segments, room openings and room signings)"*; 2025 outcome 56.5% of maximum, *"excellent performance for openings and room signings resulted in an
  overall outcome above target"*). **Pay rewards signings; key money buys signings; key money is added back in EBITDA and reaches the APP's operating-profit measure only through its amortisation over the contract term.**
- **LTIP 2025-27:** relative TSR, relative net system size growth **25%**, cash flow **20%**, **adjusted EPS 25%**, carbon and people 10% (20-F FY2024).
  *"Adjusted EPS targets incorporate assumed share buybacks as part of our ongoing shareholder return programme, so the Committee would not expect to adjust
  performance outcomes at the end of the performance period for buybacks made during the cycle"* (20-F FY2023). **The EPS target assumes the buyback, at
  whatever price.** The 2025-27 range was raised to **6-14% a year** (*"requires our earnings to increase by almost 50% over the performance period for full
  vesting"*).
- **Shareholders pushed back:** the 2025 Directors' Remuneration Policy passed with **69.51%** and the 2024 report with **79.00%** (AGM results 6-K,
  2025-05-08, `0001654954-25-005254`); *"the main areas raised were in relation to elements of the global peer group and the scale and/or structure of the
  changes to remuneration proposed"* (6-K 2025-08-20, `0001654954-25-009842`). *"The Committee stands by the appropriateness"* of both.

**STEP 3 — THE PRIMARY TEST [E2-01].** ROE is **undefined**: equity is negative (−$1,608M at 1 January 2023, −$2,736M at 31 December 2025), for the
reasons given at Q4. **[E2-43]'s unleveraged net tangible assets are also negative**: total assets $5,345M less intangibles $1,155M and cash $1,129M leaves $3,061M, against non-interest liabilities of about $3,474M, of which the owners' deferred revenue is $2,169M (arithmetic on the 2025 balance sheet: about −$0.4bn). **[E2-73], the operators' own capital:** fee business operating margin **54.1% (2019) → 64.8% (2025)**; fee business operating
profit **$813M → $1,231M**. *Judged against the hand dealt [E3-59]:* the same margins and negative equity sit at Marriott and Hilton; the structure,
not the managers, produces the return.

**The half-owner test [E2-26]:** mostly **passes** — the System Fund is separated at every line, the Owners Association transfers are quantified in the
year they happen, 2020's covenant waivers and dividend withdrawal are stated plainly. **Fails on one line**: the share count on the cover.

**The institutional imperative — score all four [E2-30].** *Not a fraud test.*
- [ ] resists any change in current direction — no; the asset disposals, the currency switch of the London line to US dollars (2026), the RCF refinancing
  without covenants are changes.
- [ ] projects/acquisitions materialise to soak up available funds — **not fired**: acquisitions are small (*"Acquisition of businesses, net of cash acquired | (292 )"* in 2019, the year of Six Senses; Ruby $120M in 2025);
  the surplus goes back to shareholders.
- [ ] staff studies produced to justify the leader's craving — no evidence in the filings.
- [x] **peer behaviour mindlessly imitated — prompt.** Brand proliferation (*"20 hotel brands"* in the FY2025 20-F, *"a family of 21 hotel brands"* in the 6-K of 2026-09-11, the latest additions Ruby, acquired for $120M, and Noted Collection),
  debt-funded buybacks to a leverage target, and key money escalation are the whole row's conduct (Marriott buybacks $3.3-4.0bn a year and key money
  $434M; Hilton negative equity −$5.4bn). **[E2-27]** is the name for decisions that are rational one by one and neutralise each other collectively.

**Capital allocation — the buyback conditions [E5-08, E4-31, E5-24].**
- **Scale:** buybacks **$500M (2022 programme), $750M, $800M, $900M, $950M (2026)**; since 2003, *"over £8 billion"* returned including nine special
  returns with share consolidations, the last **$500M paid January 2019**, fourteen months before the 2020 collapse.
- **(1) Ample funds for operations and liquidity?** **Partly borrowed**: net debt **$1,851M (end-2022) → $3,663M (mid-2026)** while **$3.8bn** was returned;
  bonds issued **$657M (2023), $834M (2024), $990M (2025)**. The programme is sized by the leverage target (*"leverage is expected to remain within our
  target range of 2.5–3.0x"*), not by a price.
- **(2) Repurchases at a material discount to conservatively calculated IV?** **FAILS on this run's IV, and the flag is live.** The company paid **US$143.04 to
  US$164.85** a share in 2026 (131 daily reports). This run's owner earnings put value at the ~10% floor at **roughly US$25-90 a share** across every base
  and 0-10% growth for a decade, and at the sovereign **roughly US$45-190** (Q5 computation). **The execution makes the price irrelevant by design:**
  *"GSI will make trading decisions in relation to the Programme independently of, and uninfluenced by, the Company with regard to the timing of the
  purchases"* (6-K 2026-02-17) — a dollar amount bought through a year, whatever the quote. [E5-24]: *"what is smart at one price is dumb at another."*
- **(3) Were shareholders given what they need to estimate value [E4-31]?** Largely yes (the fund is separated, key money disclosed); the cover share count
  is the exception.
- **CAPITAL ALLOCATION FLAG, with the humility clause [E4-13]:** *"it is natural for CEOs to be optimistic about their own businesses. They also know a whole
  lot more about them than I do."* This rests on my IV range; management knows the owners, the pipeline and the contracts better than I do. **Binds position
  size, never the discount rate.**
- **Converging flags [E4-52].** Pay on adjusted EPS that assumes buybacks + pay on signings + key money added back in EBITDA + a leverage policy written on
  EBITDA + buybacks executed blind to price and funded half by bonds: **one reinforcing system pointing toward more distributions, more signings bought and
  more leverage, whatever the price of the shares or of the owners.** *"Institutional dynamics, not venality"* [E2-30].

**THE GUARDRAIL.**
- [x] Nothing in this Q3 promotes the name; it cannot repair Q2 **[E2-37, E2-38, E3-39]**.
- [x] No great-manager dependence found [E4-23].
- [x] No manager-as-the-plan case arises [E2-35, E2-36].

- **VERDICT (recorded): [x] IN on the binary (no integrity disqualifier found)** · capital allocation flag live · [E4-52] convergence recorded ·
  *IN never promotes; the file is already closed at Q2.*

## Q4 — WILL IT SURVIVE? — RECORDED, NOT GOVERNING (file closed at Q2)
*The System Fund separation and the key-money judgment the brief asked for are answered here; nothing in this section can reopen Q2.*

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**The construction (CONVENTION, framework §VI: operating cash less SBC less (c)), with five IHG-specific choices, each disclosed:**
1. **Start from net cash from operating activities**, which under IHG's IFRS presentation is **after interest paid, interest received and
   tax paid**, and **already after key money** (*"Contract acquisition costs, net of repayments"* is a line inside cash flow from operations).
   The yield is therefore an equity yield on the market cap, with no second deduction for interest.
2. **Subtract the principal element of lease payments** (IFRS 16 moved it to financing; it is a real operating cost of leased hotels and
   offices, and the FY2019 free cash flow table restates it back to 2017).
3. **Subtract stock compensation in full [E5-06], and it must RESOLVE and be COMPLETE. It is in two places.** Note 25 carries
   *"Share-based payments cost"* under operating adjustments **and again** under *"System Fund adjustments"*. Note 27 (FY2025): *"Equity-settled |
   Operating profit before System Fund and reimbursables | 42 | 37 | 31 | System Fund | 25 | 23 | 20 | 67 | 60 | 51 | Cash-settled | ... | 5 | 7 |
   5 | 72 | 67 | 56"*. **The companyfacts tag `ifrs-full:AdjustmentsForSharebasedPayments` reads 47 / 44 / 36 (2025/24/23): the operating line only.
   A screen built on the tag would have understated SBC by about a third (25 of 72 in 2025).** Totals used: 27, 38 (2017-18, a single combined
   line), 42 (30+12), 32 (21+11), 41 (28+13), 46 (30+16), 56 (36+20), 67 (44+23), **72 (47+25)**. **[E3-70] grant value, displayed:** awards granted
   × average grant fair value (Note 27) = **$68.6M (2023), $78.5M (2024), $83.5M (2025)** equity-settled, against equity-settled charges of $51M,
   $60M, $67M: **about $17-19M a year more than the charge.** No options are granted (*"As at 31 December 2025, there were no options
   outstanding"*); awards are conditional shares, so the charge is close to grant value and the gap is shown, not added to the band.
4. **(c), maintenance capex: the company's own "gross maintenance" line** (*"Capital expenditure: gross maintenance"*, excluding key money):
   72, 60, 86, 43, 33, 44, 38, 31, **31**. **D&A default [E3-44], displayed as a third construction:** D&A excluding the System Fund plus the
   *"Contract assets deduction in revenue"* (key money's own amortisation). **This is not a capital-intensive business in [E5-20]'s sense**:
   total non-fund capex runs well under D&A, so the D&A end is not INVALID here; it is the high end of the guess, and it partly double-counts
   right-of-use depreciation against the lease principal already subtracted.
5. **Key money — the real (c) judgment, disclosed [E3-44, E2-23].** The company calls it growth: *"expenditure used to access strategic
   opportunities, particularly in high-quality and sought-after locations"*. The competitor filings call it the price of competing for owners:
   Marriott, *"our willingness to provide incentives to hotel owners to secure new agreements"*; Hilton, *"our access to and willingness to
   invest capital or provide other incentives or inducements"*; Wyndham, *"Competition may reduce fee structures, potentially causing us to lower
   our fees and/or offer other incentives"* (each FY2025 10-K, Item 1A). **Unit volume is maintained only by replacing removals**: IHG's
   removals rate is *"in line with our historical underlying average"* of **1.5%** (2023), **1.9%** (2024), **2.6% reported / 1.9% adjusted**
   (2025), against gross system growth of **5.3%, 6.2% and 6.6%**. **So roughly 30% of gross additions (1.5/5.3, 1.9/6.2, 1.9/6.6) replace rooms
   that left.** Band: **key money all growth (upper end) ↔ key money all maintenance (lower end)**; **judged central: 30% of key money is
   maintenance of unit volume.** The 30% is my judgment from the replacement ratio, not a filed figure.

**System Fund separation — the cash that belongs to the owners, removed [the brief's central Q1/Q4 instruction].** The fund's cash sits inside
consolidated operating cash flow in three places, all filed:
- **its result** (*"System Fund and reimbursable result"*: −34, −146, −49, −102, −11, −105, +19, −83, **−46**);
- **its non-cash add-backs** (Note 25 *"System Fund adjustments"*: D&A, impairments, associates; its SBC is handled once, in point 3);
- **its deferred-revenue float** (*"Increase in deferred revenue"*: 43, 141, 57, 1, 39, 108, 123, **214**, **107**), which is loyalty points
  collected and not yet consumed plus co-brand upfronts (*"$ 37 m ( 2024 : $ 100 m ) of initial upfront payments received in relation to US
  co-brand credit card agreements"*). The company's own accounting policy states the mechanism: *"more revenue is deferred each year than is
  recognised in the Fund. This can lead to accounting losses in the Fund each year as the deferred revenue balance grows."* **The whole
  increase is stripped**, including the co-brand upfronts, because upfront cash recognised over the term is a working-capital timing
  benefit, not earnings [E2-23]; this leans conservative by perhaps $37-100M in 2024-25 and is stated rather than netted.
- **The fund pays IHG interest on the cash IHG holds for it**: *"System Fund interest | 20 | 25"* (H1 2026 and H1 2025 income statement
  summary, 6-K `0001654954-26-007436`). **The fund's cash is on IHG's balance sheet and IHG pays for its use.** Confirmation that it is not
  shareholders' money.
- **Its capital expenditure** (*"Capital expenditure: gross System Fund capital investments"*: 142, 99, 98, 35, 19, 35, 46, 45, 43) is charged
  in the consolidated construction and not in the separated one, because in the separated one the fund's cash that pays for it is removed.

**The fund's total cash contribution to consolidated owner earnings** (result + non-cash ex SBC − its capex + deferred-revenue increase),
US$M: 2017 **−92**, 2018 **−55**, 2019 **+4**, 2020 **+12**, 2021 **+96**, 2022 **+62**, **2023 +182, 2024 +180, 2025 +118**. **For the last
three years the owners' fund supplied $118-182M a year of the consolidated cash that a screen would have credited to shareholders.**
*(2017-2018 fund lines are approximations: the non-cash add-back is fund D&A only, and the fund's SBC is not separately stated.)*

### Owner earnings by year, US$M (`oe.py`, `oe_out.json`; every input transcribed with its source in the script)
| | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| Consolidated, key money = maintenance | 350 | 477 | 368 | −38 | 511 | 485 | 725 | 535 | 722 |
| Consolidated, key money = growth | 407 | 531 | 429 | 26 | 553 | 549 | 826 | 772 | 901 |
| **Fund separated, key money = maintenance** | 442 | 532 | 364 | **−50** | 415 | 423 | 543 | 355 | 604 |
| **Fund separated, key money = growth** | 499 | 586 | 425 | **14** | 457 | 487 | 644 | 592 | 783 |
| Fund separated, D&A default [E3-44] | 442 | 512 | 374 | −78 | 357 | 431 | 578 | 515 | 695 |

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25]. 2020-21 are shown in and out, never silently dropped.**
| window (fund separated) | key money = maintenance | **central (30% of key money)** | key money = growth | D&A default | yield on US$22,613M (maint ↔ growth) |
|---|---|---|---|---|---|
| **5-yr 2021-2025 (default [E2-42]; includes 2021)** | **468** | **555** | **593** | 515 | **2.07% ↔ 2.62%** |
| 6-yr 2020-2025 (includes 2020) | 382 | 462 | 496 | 416 | 1.69% ↔ 2.19% |
| 5-yr 2019-2023 (includes 2020 and 2021) | 339 | — | 405 | 332 | 1.50% ↔ 1.79% |
| 7-yr 2019-2025 (all fund lines fully stated) | 379 | 454 | 486 | 410 | 1.68% ↔ 2.15% |
| 9-yr 2017-2025 (all IFRS 15/16 years) | 403 | 470 | 499 | 425 | 1.78% ↔ 2.20% |
| **4-yr 2022-2025 (excludes 2020-21)** | 481 | 583 | 626 | 555 | 2.13% ↔ 2.77% |
| **7-yr ex-trough 2017-19 + 2022-25** | 466 | 541 | 574 | 507 | 2.06% ↔ 2.54% |
| 3-yr 2023-2025 | 501 | 621 | 673 | 596 | 2.21% ↔ 2.98% |
| *Consolidated, for comparison: 5-yr* | *596* | — | *720* | — | *2.64% ↔ 3.18%* |

- **Short-window mean** (3-yr 2023-25, fund separated): **$501-673M**, central **$621M**.
- **Long-window mean** (9-yr 2017-25, fund separated): **$403-499M**, central **$470M**.
- **Combined range across every valid window and both (c) ends: $339M to $673M** (fund separated); **$382-673M** if the one window containing
  both trough years and no recovery (2019-23) is set aside, which it is not, only displayed.
- **Is that range too wide to reach a conclusion? No, not for the purpose it serves.** Its top is a **3.0%** yield against a 5.35% sovereign and a
  ~10% floor [E4-28]; every construction and window sits on the same side of both. The width is real and is carried forward, not resolved.
- **The distorted years, named [E5-11]:** **2020** (RevPAR −52.5%; owner earnings −$50M to +$14M), **2021** (recovery), **2018** (fund deficit of
  $146M), **2019 and 2025** (acquisitions of Six Senses, $292M, and Ruby, $120M, in investing, displayed and not in (c)). **Favourable breaks
  [E4-41]:** the **2024 Owners Association agreement** moves points revenue from the fund into the fee business (about $25M in 2024 and about
  twice that in 2025, company estimates), and **the 2024-25 co-brand upfronts** ($100M, $37M) lift consolidated cash. The first sits inside the
  separated figures as fee-business cash; the second is stripped. **Normalising the first out lowers the 2025 separated figures by about
  $35-40M after tax** (my arithmetic at IHG's 2025 cash-tax rate, not a filed figure).
- **What IHG calls its own number, for contrast:** *"Adjusted free cash flow a was an inflow of $893m"* (2025), which includes the fund's cash,
  subtracts ESOT share purchases ($10M) instead of the $72M SBC charge, and excludes exceptional cash and recyclable key money.
  **The separated central 5-year figure ($555M) is 62% of the company's 2025 headline.**

### Great, good, or gruesome? **[E4-20]**
- [x] **great in structure** — [ ] good — [ ] gruesome
- **Evidence:** the capital the business requires is key money plus a small maintenance budget: **$210M in 2025** ($179M + $31M) against fee
  business operating profit of **$1,231M**; the hotels, the land and most of the working capital belong to the owners, and the owners' float
  finances the loyalty liability. Fee business operating profit rose from **$813M (2019) to $1,231M (2025), +$418M**, against cumulative key money
  of **$748M** over 2019-25 and maintenance capex of **$306M** (arithmetic). Separated owner earnings on the growth end rose **$425M (2019) → $783M
  (2025)**. [E4-43]: the great class *"pays an extraordinarily high interest rate that will rise as the years pass"* fits the arithmetic; **the
  caveat is the direction of the price of growth**: key money went **$42M (2021) → $237M (2024) → $179M (2025)**, 4-6x the 2021 level while net
  rooms growth moved from −0.6% to 4.0-4.7%. The rate on incremental capital is still very high; it is falling, and Q2's row says why.

### Staying power — score all three **[E5-11]**
- **(1) A large and reliable stream of earnings: HALF.** Large ($1.2bn of fee business operating profit), **not reliable through a travel
  shock**: 2020 fee business operating profit **$278M (−66%)**, net cash from operating activities **$137M**, separated owner earnings **−$50M to
  +$14M**. The fee is a percentage of the owner's revenue, so it is exactly as cyclical as hotel revenue [Q1].
- **(2) Massive liquid assets: NO.** Cash **$1,129M** (2025-12-31), **$822M** (2026-06-30, H1 report), against net debt of **$3,333M → $3,663M**.
  The **$1.5bn RCF** (December 2025, matures 2030, *"The new facility does not contain financial covenant measures"*) is real but is a bank line,
  and [E5-39] counts none: *"We will never be dependent on the kindness of strangers."*
- **(3) No significant near-term cash requirements: HALF.** Bonds: **£350M 2.125% due 24 August 2026 ($475M)** and **€500M 2.125% due 15 May 2027
  ($594M)**, then £400M 2028, €600M 2029, €850M 2030, €750M 2031 (Note 21); the **$950M 2026 buyback** was about **$579M** done by 3 September
  (6-K parse); ordinary dividends about **$280M** a year; lease liabilities **$406M**. **All discretionary except the bonds**, and the bonds are
  covenant-light. The 2029 euro bonds carry a *"step-up coupon of 1.25% payable on the bonds maturing in 2029"* (*"The bonds maturing in 2030 and 2031 do not have a step-up coupon"*); its trigger was not read and is not claimed.
- **Leverage, named and quantified [E4-16, E3-29], and the policy that sets it:** *"net debt:adjusted EBITDA, where we aim for a ratio of
  2.5–3.0x"*; **2.07x (2022: $1,851M / $896M) → 2.50x (2025: $3,333M / $1,332M)** (arithmetic on the company's figures). **Net debt rose $1.81bn from
  end-2022 to mid-2026 while $3.8bn went out in buybacks and dividends** (2023 $790M + $245M, 2024 $804M + $259M, 2025 $897M + $270M, H1 2026
  $375M + $189M): roughly **47% of the distributions borrowed**. **[E2-60] (maintenance has a third dimension, financial strength): FIRES as a
  prompt** — leverage is rising to fund the payout, by design, toward a stated ratio; the ratio is on EBITDA, which [E4-29] would not use.
- **The coverage test [E2-54]:** interest paid **$202M** against cash flow from operations **$1,361M** less maintenance capex **$31M** (key money already
  inside): **6.6x** in 2025. **In 2020: $132M against $308M − $43M = 2.0x.**
- **The rehearsal is in the filings — 2020.** 20-F FY2020: *"our net debt: adjusted EBITDA ratio of 7.7x as at 31 December 2020 is outside of our
  previously stated aim to maintain a ratio of 2.5-3.0x"*; *"we secured covenant waivers up to and including 31 December 2021 for our $1.35bn
  syndicated and bilateral revolving credit facilities (RCF), further covenant relaxations in 2022"*; the going-concern note assumed *"£600m of
  CCFF due in March 2021 is repaid on maturity"* (the Bank of England's Covid Corporate Financing Facility); the 2019 final dividend was
  withdrawn (*"The Board withdrew its recommendation of a final dividend in respect of 2019 of 85.9¢ per share"*). **Twelve months earlier IHG had
  paid a $500M special dividend** (*"Paid in January 2019"*) with a share consolidation. It survived, with a central-bank facility and its banks'
  forbearance. [E5-39] is the corpus's name for that.
- **Jurisdiction [E3-66]:** an England and Wales plc under the Companies Act 2006, UK Corporate Governance Code, pre-emption rights (the 2025 AGM
  disapplication votes passed at 92.2% and 87.1%), a binding shareholder vote on pay policy that returned **69.5%** in 2025 and forced a consultation;
  NYSE ADSs. **Shareholders stand near the front of the queue here**; no controlling holder (*"IHG is not directly or indirectly owned or controlled
  by another company or by any government"*).
- **Negative equity, explained from the filing:** total equity **−$2,736M** (2025-12-31). Two causes, both filed: *"Other reserves"* of about
  **−$2.86bn**, which *"comprise the merger and revaluation reserves previously recognised under UK GAAP, together with the reserve arising as a
  consequence of the Group's capital reorganisation in June 2005"*; and **returns in excess of profit** (*"Since March 2003, the Group has returned
  over £8 billion of funds to shareholders by way of special dividends, capital returns and share repurchase programmes"*, total **£8,965M**;
  retained earnings column of the statement of changes in equity: **$607M at 1 January 2023, $396M at 31 December 2023, $34M at 31 December 2024**). **Leverage is judged on owner earnings and cash, not on
  book equity, and book equity says nothing either way.**

### Name the specific way THIS business dies **[E2-27, E3-24]**
**The registered shapes, rebuilt from the register because no single list exists on disk** (the GFS note): ORCL (contracted not to stop) · ARM
(earns nothing after paying its people) · BE/HHH (too little filed history) · BA (the cash is spent undoing past work) · SWK (the self-liquidating
distribution [E2-60]) · ACVA/FLNC/NEGG (the borrowed balance sheet, with the treadmill variant) · CNR (the long tail on a short cycle) · RGTI (the
equity is the revenue) · BAM (the warehouse) · SONY (the camouflage) · TM (the pass-through) · TSM (the address); **proposed, unregistered:** SPOT
(the tenant), GFS (the patron), MBGL (the dowry). *(ACMR's run also named "growth refilled by selling the subsidiary" and numbered it fifth; the
numbering on disk conflicts and is recorded, not resolved.)*

**The mechanism for IHG, in two legs, from what the filings show it is exposed to [E4-40]:**
1. **The fast leg — a 2020-class demand shock at a leverage target sized on normal EBITDA.** Quantified from filed figures: 2020 took adjusted
   EBITDA from $981M to $329M (−66%) and leverage to 7.7x. The same proportional fall on 2025's $1,332M gives about **$450M**, against **$3.66bn** of
   net debt (mid-2026): **about 8x**, with **$1.07bn of bonds due inside twelve months of the H1 balance sheet** against **$822M of cash**. What changed
   since 2020: the RCF has **no financial covenants**, so the waiver leg is gone [E3-52]; what did not change: the buyback is sized to keep leverage
   *"within our target range"*, so the balance sheet enters any shock at the top of the range. **Outcome: not death; a dividend and buyback stop, a
   rating step-up, possibly equity or state support, as in 2020. Likelihood: a low-level possibility** in any given decade; the corpus's
   [E2-55] asks for results *"under extraordinarily adverse conditions"*, and 2020 is the filed instance.
2. **The slow leg — the flag is re-flown.** IHG owns no building. Its revenue base is a portfolio of time-limited contracts with owners who, in
   IHG's own words, can gain *"the bargaining position of property owners seeking to become a franchisee or engage a manager"*, and whose renewals
   may not be *"on similarly favourable terms, or at all"*. Rivals with larger systems bid for the same buildings (Marriott **1,779,936 rooms**, Hilton
   **243 million** loyalty members, both FY2025 10-Ks). **The death is not a collapse but a margin migration: the fee take stays flat or slips, key money
   and owner concessions rise, and leverage set at a multiple of EBITDA converts the squeeze into lower distributions.** Quantified from filed
   figures: fee business revenue as a share of system gross revenue **5.41% (2019) → 5.39% (2025)**, **about 5.25% without the ~$50M moved from the fund
   by agreement** (arithmetic); key money **$61M → $179M**; the 2024 cut to *"our standard loyalty assessment fee for owners"*. **Likelihood: a real
   possibility** — the direction is visible in the filings; the pace is not.

**Against the register:** leg 1 is **SWK's self-liquidating distribution in its levered, not yet liquidating, form** (distributions partly borrowed
to a target ratio, [E2-60] firing as a prompt). Leg 2 is **none of the twelve**: it is closest to **THE TENANT** (proposed at SPOT) but inverted — SPOT
rents its one input from a few landlords who rent it to every rival; IHG rents its brand onto thousands of landlords' buildings, each of whom can take
the flag down at term and hoist a rival's. **Proposed name: THE FLAG** (a brand that flies over a building someone else owns). **The contrast that
defines it is on disk:** McDonald's, which *"maintains control of the underlying real estate and building"* at the end of each franchise term
(2026-09-03 run), is not a flag. **Flagged to the operator; the register is unchanged** (a sixteenth proposal, after THE TENANT, THE PATRON and THE
DOWRY, none registered).

- Likelihood: [ ] likely [x] a real possibility (leg 2) [x] a low-level possibility (leg 1)
- **VERDICT (recorded, not governing; on survival alone): IN** — separated owner earnings positive every year on the growth end and negative only in 2020 on the maintenance end, great in structure, coverage 6.6x, covenant-free RCF, a
  filed survival of the worst demand year in the industry's history; [E5-11] **1 of 3** (half, no, half), recorded as a weakness, not a death.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 is OUT. **The file is closed.** What follows is the price the queue requires every run to end
with, under operator rule 3.

---
## Q5 — COMPUTATION — NOT A CLEARANCE
*No entry language. No ranking. No bar chosen. Arithmetic on the Q4 figures (`q5.py`, `q5_out.json`).*

**The price and what the buyer is paying for, in words.** At **US$153.83** (NYSE ADS close 2026-09-11, aggregator flagged; London US$153.50) × **146,997,788**
shares (Step 0) = **US$22,613M**, plus about **US$3.7bn** of net debt (mid-2026), a buyer is paying for a share of the fees that hotel owners pay to fly
IHG's flags over buildings IHG does not own, after the owners' System Fund cash is set aside, after key money, and after the borrowing the company
has taken on to return capital. **The buyer is also paying for continued growth of 7-8% a year forever**, because that is what the quote requires to reach
the ~10% floor.

**1. THE YIELD** — owner earnings (fund separated) ÷ US$22,613M, beside the **USD 30-year 5.35%** (US Treasury, 09/11/2026):
| base | owner earnings | yield |
|---|---|---|
| 5-yr 2019-23 (both trough years, key money = maintenance) | $339M | 1.50% |
| **5-yr 2021-25 default, key money = maintenance** | **$468M** | **2.07%** |
| **5-yr 2021-25, central (30% of key money)** | **$555M** | **2.45%** |
| 5-yr 2021-25, key money = growth | $593M | 2.62% |
| 3-yr 2023-25, key money = growth | $673M | 2.98% |
| *consolidated 5-yr, fund cash left in, key money = growth (the screen's view)* | *$720M* | *3.18%* |

**Every construction is below the sovereign.** The best of them is 2.4 points below it.

**2. WHAT THE PRICE ALREADY ASSUMES** (perpetual growth needed at the quote, arithmetic):
- **at the ~10% floor [E4-28]: 6.8% (3-yr growth base) to 8.4% (lowest base); 7.4% on the central 5-yr base.**
- at the sovereign: 2.3% to 3.8%; 2.8% central.
- **What the business has done:** fee business operating profit **+7.2% a year 2019-25** (arithmetic, $813M → $1,231M, including two fund re-divisions and a
  cost programme); separated owner earnings on the growth end **+10.7% a year** from a 2019 base, $425M → $783M. **The floor case needs the best six years
  of fee growth, including the recovery from 2020, to continue in perpetuity** — [E4-35]'s base rate for sustained high growth is *"fewer than 10 of the 200
  most profitable companies"*, and [E4-44] caps the value at the growth of the earnings.

**3. WHAT YOU ARE PAID** — **−2.4 to −3.9 points** against the sovereign on the current yield, before growth.

**THE RANGE, round numbers, US$ a share** (owner earnings grown for ten years, then flat; 146,997,788 shares; not a value claim for an OUT file):
| base | at ~10%, 0% growth | at ~10%, 10% growth for a decade | at 5.35%, 0% growth | at 5.35%, 10% growth for a decade |
|---|---|---|---|---|
| $339M | ~23 | ~46 | ~43 | ~96 |
| $468M | ~32 | ~64 | ~60 | ~132 |
| **$555M central** | **~38** | **~76** | **~71** | **~157** |
| $673M | ~46 | ~92 | ~86 | ~190 |

- **At the ~10% floor: roughly US$25-90 a share across every base and 0-10% growth for a decade. The price of US$153.83 is above the whole range.**
- At the sovereign: roughly US$45-190; the price sits inside that range only where a decade of ~10% growth is assumed on the central or higher base.
- **What bounds the upside [E2-63]:** the fee take is flat to falling (Q2), the share of the branded systems is falling, and leverage is already at the
  company's target, so the per-share accretion from debt-funded buybacks cannot compound without the ratio.
- No alert band, no PORTFOLIO row (Q2 OUT; FOLD step 4).

## Q6 — WHAT WOULD PROVE ME WRONG — RECORDED, NOT GOVERNING
*Nothing is armed. The file closed at Q2 on the business; a price alert on it would be a category error (the QLYS ruling, 2026-09-07). The reopening
conditions are recorded in words.*

**What would reopen Q2 (each from a filing, none from a price):**
1. **A disclosed rate, rising.** IHG begins to disclose an effective royalty or fee rate and it rises through a flat-RevPAR year, as Choice's did in 2020 and
   2025 [E2-44](1).
2. **The toll proxy turns.** Franchise and base management fees ÷ total gross revenue in IHG's system rises for three consecutive years without a further
   re-division of the owners' fund.
3. **Key money falls while signings hold.** Contract acquisition cash below ~$100M a year with net system size growth at or above 4%.
4. **Share of the branded systems' rooms stops falling** against Marriott and Hilton for three years [E4-55].
5. **No further owner-price cuts** in the 20-F's owner section, and no further transfers negotiated with the Owners Association.

**What would confirm the OUT (the moat downgrade is slow [E4-17, E3-30]):** removals rising above the ~1.5-1.9% underlying rate; key money rising faster
than openings; a renewal cohort disclosed on worse terms; the loyalty contribution (66% of room nights) falling.

**Q3/Q4 items to watch if it is ever reopened:** net debt against separated owner earnings (not EBITDA) [E2-54]; buyback prices against value [E5-08]; the
System Fund expense allocation (critical audit matter); the cover share count corrected.

- **VERDICT: not reached (file closed at Q2).**

---
## SELF-AUDIT
- [x] Questions answered in order; the first non-IN verdict (Q2 OUT) closed the file; Q3-Q6 carry RECORDED, NOT GOVERNING banners
- [x] No question marked IN carries an "unverified" or "provisional" caveat (Q1 IN rests on Note 3, the accounting policies and the 20-F business model)
- [x] No UNRESEARCHED verdict; Accor's absence stated at Q2 with its evidence rung (AMF) and why it does not bear on criterion 2
- [x] No UNKNOWABLE verdict
- [x] Step 0: the filing was read (20-F FY2025 `0000858446-26-000010`, MD&A, cash-flow statement and Note 25 detail lines, footnotes 2, 3, 10, 21, 22, 25,
      27, 28, 31, legal proceedings, risk factors, remuneration report); net cash from operating activities $898M cross-checked to companyfacts
- [x] Owner earnings on multi-year means; nine windows including and excluding 2020-21; (c) band disclosed as a judgment with a stated central; SBC resolved in
      both places and complete; System Fund separated with its deferred-revenue float and capex
- [x] Competitor row filled from five 10-K filers, same metrics, 2019/2020/2025, companyfacts cross-checks matched; Accor stated as a limit
- [x] Sovereign for the earnings currency (USD argued from the filing), from the issuing authority, dated 09/11/2026; GBP (BoE 20-year, a rung below the
      issuer, flagged) and EUR stated beside it
- [x] Value stated as a round-number range under COMPUTATION — NOT A CLEARANCE; no bar chosen because no bar applies to a closed file
- [x] Prices dated; aggregator used for live quotes only and flagged
- [x] Every ledger id checked against `principle_ledger.csv` before commit (`ids.py`)
- [x] Run committed to git with a pathspec at Step 0, Q1, Q2 and Q3-Q6

**Own errors caught before commit, recorded (operator rule 6):**
1. I first wrote in Q1 that the FY2003 20-F describes the fee model; I had read only its separation definition. Corrected before the Q1 commit.
2. I first wrote that retained earnings turned negative after the 2024 buyback; the statement of changes in equity shows **$34M** at 31 December 2024.
3. I first quoted the 2029 bond step-up as a rating-downgrade coupon; the trigger was not read, and the quote was shortened to what was read.
4. I first wrote that the owners' deferred revenue alone exceeds the tangible operating assets; the arithmetic is closer than that and was replaced with the
   full net-tangible-asset calculation (about −$0.4bn).
5. I first gave a 2019 brand count (15) that no filing read supplied; replaced with the 20-F FY2025 and 2026 6-K counts.
6. My first owner-earnings design subtracted the System Fund's capex twice in the separated construction (removing the fund's net cash including capex
   from a base that had never charged it); caught before any figure was written and rebuilt as documented in `oe.py`.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** IHG passes Q1 (a toll on hotel room revenue for brand, distribution and loyalty, with the owners' System Fund separable from the filing) and
  **fails Q2 on [E3-03] criterion 2 as [E2-44](1) and [E4-37] test it**: hotel owners have close substitutes, and IHG's filed conduct — key money $61M →
  $179M (peak $237M), a 2024 cut to owners' loyalty assessment in a +3.0% RevPAR year, fee-business gains negotiated out of the owners' fund in 2020 and
  2024-25, a core toll proxy of 4.21% → 3.89%, and a share of the six branded systems' rooms falling 18.1% → 16.9% while Choice raised its filed royalty rate
  through 2020 and 2025 — is that of a seller facing them. **Price US$153.83 × 146,997,788 = US$22.6bn; separated owner earnings $468-593M on the five-year
  default (2.1-2.6%) against USD 5.35%; roughly US$25-90 a share at the ~10% floor; price above the whole range. PASS/FAIL: FAIL at Q2.**


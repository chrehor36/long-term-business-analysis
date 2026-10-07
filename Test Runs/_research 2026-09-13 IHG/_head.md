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
- [ ] MD&A  [ ] cash-flow statement incl. detail lines  [ ] footnotes — *ticked as each is read; see the bottom of Step 0 when complete*
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

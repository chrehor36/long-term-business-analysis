# Company Run — United Microelectronics Corporation (UMC) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

**Queue context.** A name in **WAVE 5** of `Screens/WATCHLIST RUN QUEUE.md` (the unpriced watchlist
businesses), the fifth of the eleven foreign 20-F filers to be run (after TM, SONY, HMC and TSM). The
2026-09-01 triage skipped it as *"foreign 20-F filer ... several still return too few annual periods
because their XBRL history is short, not because the business is."* **Read here as UNLABELLED: a prompt
to read the 20-F by hand, not a verdict.** The run file was created before any fetch (write-early
protocol; a first attempt at this run was cut off by the session limit before it wrote anything, and no
file or research folder from it existed). Research on disk: `Test Runs/_research 2026-09-13 UMC/`.
**The TSM run of the same morning is UMC's closest competitor on disk; it was read before anything was
built here, and its conclusions are not carried over** (UMC is a mature-node foundry; the evidence is
tested afresh).

**Why the screen could not price it, found rather than assumed.** `companyfacts` (fetched 2026-09-13)
carries `ifrs-full` annual facts for **FY2015 to FY2024** (ten periods in TWD, eight in USD), **and nothing
from the FY2025 20-F** (`0001193125-26-193757`, filed 2026-04-30). `CashFlowsFromUsedInOperatingActivities`
ends at 2024-12-31. **The history is not short; the newest year is missing.** Fifth 20-F filer in a row
(SONY, TM, HMC, TSM, UMC). **One refinement of the TSM explanation:** TSM's FY2025 20-F was filed under a
new filing-agent prefix (`0001628280`), which that run offered as a possible cause. **UMC's FY2025 20-F was
filed under the same prefix as its FY2024 20-F (`0001193125`), and is equally missing**, so the prefix is not
the cause; the source simply has not ingested FY2025 20-Fs filed in April 2026. This run reads FY2015-FY2025
from the filed 20-Fs.

*Dated note, 2026-09-13 ~10:40, added at the fold after the handoff note of 10:05 (commit `13c3678`, "why 20-F filers never priced")
landed while this run was open; the paragraph above is left as written.* That note measures three causes (a USD-only unit filter,
US-GAAP tag names, and companyfacts lag for some filers). **Measured on UMC:** `ifrs-full:CashFlowsFromUsedInOperatingActivities`
carries **TWD (24 facts) and USD (8 facts, the 20-F's convenience translations for FY2017-FY2024)**. So for UMC the US-GAAP tag names
blank the row, the lag is real (FY2025 absent), and **a USD-only reader given the IFRS element name would not see nothing: it would
see eight years of convenience-rate dollars**, a different currency defect from the blank one. None of this changes the run, which
reads the filed NT$ statements by hand.


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
**The functional and presentation currency is the NT dollar; most revenue is billed in US dollars; the plant is
spread across Taiwan, Singapore, China and Japan.** Filed:
- 20-F FY2025 Item 5: operating revenue rose 2.3% *"partially offset by a decline of 5.4% in average selling price
  from 2024 to 2025, and a 2.9% appreciation of the NTD against the U.S. dollar in 2025 compared to 2024"*; gross
  margin fell *"primarily due to an annual decline of 5.4% in average selling price and a 2.9% appreciation of the
  NTD against the U.S. dollar"*. The dollar exposure is operating, not balance-sheet: *"As of December 31, 2025, we
  had US$22 million outstanding in foreign currency forward contracts."*
- Cash is held *"primarily ... in U.S. dollars, New Taiwan dollars and Renminbi"* (Item 5.B).
- Capacity by site (Item 4 fab table, 12-inch equivalents, 2025): Taiwan fabs 3,219k of 5,163k (62%), Singapore
  Fab 12i 684k (13%), China Fab 8N and Fab 12X 789k (15%), Japan Fab 12M 471k (9%).

**The judgment, and its ground (the TSM run's pairing, re-argued for this filer rather than inherited).** The
owner earnings below are computed in NT$ from the NT$ cash-flow statement and the cap is priced in NT$ from the
Taipei quote, so **the TWD sovereign is the consistent pairing** [E4-15, E3-32]. The case for the USD sovereign is
real (dollar billing; [E4-01] names *"the yield on long-term U.S. bonds"*) and is shown beside it. **The [E4-28]
floor of roughly 10% does not move with the sovereign** (*"that's true whether short rates are 6 percent or whether
short rates are 1 percent"*), so the choice moves only the points-over-sovereign display, never the quit-on line.

### Sovereign — struck fresh 2026-09-13, same rungs as the TSM run [E4-15, E3-32]
**No TWD source exists in `tools/sources.py`, and none was added.** Fetched by hand (`sov.py` to `sov5.py`, files in
`sov/`):

| rung | what | tenor | yield | date | source · saved file |
|---|---|---|---|---|---|
| **ISSUING AUTHORITY (auction)** | Central Bank of the R.O.C.: *"The Bank, on behalf of the Ministry of Finance, conducted an auction of 30-Year Central Government Bonds (A15105) on May 26, 2026"*; coupon 1.8750%; bid-to-cover 1.55 | **30-year**, matures 2056-05-29 | **1.8140% weighted average accepted** (lowest 1.6600%, highest 1.9000%) | 2026-05-26 | `https://www.cbc.gov.tw/en/cp-448-191306-0372c-2.html` · `sov/cbc_cp-448-191306-0372c-2.html` (re-fetched today, unchanged) |
| same authority, newest auction on the list | CBC for the MOF, 5-Year A15108; bid-to-cover 1.57 | 5-year | 1.7790% w.a. | 2026-09-01 | `https://www.cbc.gov.tw/en/cp-448-192798-d1d6e-2.html` · `sov/` |
| **OFFICIAL SECONDARY CURVE (the dated observation used)** | Taipei Exchange Treasury Yield Curve, benchmark A15105: *"The Yield is based on Electronic Bond Trading System (EBTS) Volume-weighted Average Yield."* | **30-year** (29.714 yrs residual) | **1.8860%** | **2026-09-11** (the newest file listed on 2026-09-13; 09-12 and 09-13 are a weekend) | `https://www.tpex.org.tw/storage/bond_zone/tradeinfo/govbond/2026/202609/Curve.20260911-E.xls` · `sov/Curve.20260911-E.xls` and `.ods` |
| same file | 2Y 1.7104 · 5Y 1.8223 · 10Y 1.9205 · **20Y 2.1010** · 30Y 1.8860; fitted zero-coupon 30Y about 2.19% (cubic B-spline) and 2.17-2.19% (Svensson) | | | 2026-09-11 | same |

- **Rate used: TWD 30-year 1.89% (TPEx EBTS benchmark A15105, 2026-09-11), carried as a band of about 1.8-2.2%**
  across the issuing authority's 30-year auction (1.81%), the 20-year benchmark (2.10%) and the fitted 30-year zero
  rate. The longest liquid tenor is 30 years. **The figure matches the TSM run's to the basis point**, as it should on
  the same file; it was re-fetched, not copied.
- **Method defect found and recorded for the next Taiwan filer:** the TSM run's recorded endpoint path
  (`.../bond/tradeinfo/govDaily2`) returns **HTTP 404**; the working path is **`https://www.tpex.org.tw/www/en-us/bond/govDaily2`**
  (POST `date=YYYY/MM/DD&fileCode=Curve&response=json`), found in the TPEx page's own `API_PATTERN`
  (`/www/{LANG}/{ACTION}`, action `bond/govDaily2`). The `.xls` needs `xlrd`, which is not installed; the TPEx
  `convertToOds` endpoint returns an ODS that parses with the standard library.
- **Reference, not paired with the NT$ yield: USD 30-year 5.35%** (US Treasury daily par yield curve, 09/11/2026,
  struck 2026-09-13 through `tools/sources.py`).
- **FX (issuing authority): NT$31.638 per US$**, Central Bank of the R.O.C., NT$/US$ Closing Rate, **2026-09-11**
  (09-10: 31.548; 09-09: 31.505), `https://www.cbc.gov.tw/en/lp-700-2.html` · `sov/cbc_fx.html`. Used only for the ADR
  premium and orientation.
- **ADR ratio, derived: 1 ADS = 5 common shares.** 20-F FY2025 cover: *"American Depositary Shares, each representing
  five common shares"*; Note 6(19): *"UMC had 115 million and 117 million ADSs ... The total number of common shares of
  UMC represented by all issued ADSs were 576 million shares and 586 million shares as of December 31, 2024 and 2025
  ... One ADS represents five common shares"* (586 / 117 = 5.0); Q2 2026 report Note 6(19): *"147 million ... ADSs ...
  735 million shares"* at 2026-06-30. Depositary JPMorgan Chase Bank, N.A. **The ADS float grew from 87 million
  (2025-06-30) to 147 million (2026-06-30)**, recorded, not interpreted.

### The share count, read by hand and walked forward
| date | count | what changed | document · accession |
|---|---|---|---|
| **2025-12-31** | **12,588,156,344 issued and outstanding** | cover: *"12,588,156,344 Common Shares of Registrant issued and outstanding as of December 31, 2025"* | **20-F FY2025 cover**, `0001193125-26-193757` |
| Feb and Apr 2026 | about −12 million | *"In April 2026, February 2026 ... UMC has recalled and cancelled 2 million shares, 10 million shares ... of unvested restricted stocks"* | Q2 2026 consolidated report Note 6(19), 6-K 2026-07-29, `0001193125-26-322030` |
| **2026-05-05 to 05-20** | **30,551,000 bought into treasury** | *"No. of shares currently repurchased (shares): 30,551,000 ... Current average repurchase price per share (NTD): 101.33"*; purpose *"For transfer to employees"* (Q2 report Note 6(19)b) | 6-K 2026-06-29, `0001193125-26-286731` |
| 2026-06-30 | 12,577 million issued; 30,551 thousand treasury | Q2 report Note 6(19) | `0001193125-26-322030` |
| 2026-07-29 | −6,890,971 | Board: *"Cancelled shares: 6,890,971 shares ... Share capital after capital reduction: NT$125,700,938,990"* | 6-K 2026-07-29, `0001193125-26-322027` |
| **2026-08-10** | **12,539,542,899 outstanding** | registration completed: *"After the capital reduction: The paid-in capital is NT$125,700,938,990; the shares outstanding are 12,539,542,899 shares"* | **6-K 2026-08-14, `0001193125-26-350180`** |

- **Count used: 12,539,542,899**, the company's own filed "shares outstanding" after the August cancellation. It
  reconciles exactly: NT$125,700,938,990 / NT$10 = 12,570,093,899 issued, less 30,551,000 treasury = 12,539,542,899.
  **Treasury shares are excluded** (operator rule).
- **Convertible bonds issued after the count, not yet in it** (recorded for Q3 and Q5, because they are potential
  shares, not outstanding ones): the 1st domestic unsecured CB, proceeds *"totaling NT$12,120,000,000"* (6-K
  2026-08-05), conversion price **NT$146.0**; the 2nd, *"totaling NT$4,792,798,780"* (6-K 2026-09-02), conversion price
  **NT$130.7**; and the Board of 2026-08-26 resolved *"the 7th Unsecured Overseas Convertible Bonds ... Up to US$1.8
  billion"* (6-K `0001193125-26-365826`). **At their conversion prices the two domestic issues are about 83.0 million +
  36.7 million = ~120 million shares (0.95%)**; the overseas issue, unpriced, would be of the order of 400 million
  shares (~3%) at a conversion price near NT$140 (US$1.8bn × 31.638 / 140 ≈ 407 million, **an illustration, not a
  filed term**). No conversion is filed as of 2026-09-04.
- **Reciprocal holdings, displayed and not deducted.** UMC's associates hold UMC shares (Q2 2026 report Note 6(7)c,
  thousand shares, 2026-06-30): **Hsun Chieh Investment 441,371 · SIS 266,580 · Yann Yuan 196,563**. UMC owns 36.49%,
  18.08% and 26.78% of them (Attachment 7), so its look-through share of its own stock is about **262 million shares
  (2.1%)**. The IFRS balance sheet carries a *"Treasury stock"* line of NT$9,803,778 thousand in both 2024 and 2025 when
  no shares were bought (*"During 2023, 2024 and 2025, we did not purchase any of our common shares"*), and the
  equity statement carries *"Adjustments due to reciprocal stockholdings held by subsidiaries and associates"*: the
  deduction the accounts make is this look-through. **The cap below uses the legal count; on the look-through count
  (~12,278 million) every yield would be about 2% higher.** Stated so the smaller count is not quietly used.
- **No split after the measurement date**; `close × shares(measurement) × splits after measurement` holds trivially.

### The price, the ADR premium and the cap (aggregator for live quotes only, flagged)
| quote | close | date | NT$ per common share (1 ADS = 5; CBC NT$/US$ of the same date) |
|---|---|---|---|
| **TWSE 2303** | **NT$140.5** | **2026-09-11** | **140.5** |
| NYSE UMC | US$22.64 | 2026-09-11 | 143.3 at 31.638 → **+2.0%** over the same calendar day's Taipei close |
| NYSE UMC, prior session | US$22.12 | 2026-09-10 | 139.6 at 31.548 → **−2.1%** against TWSE 2026-09-10 (NT$142.5) |
| NYSE UMC | US$22.69 | 2026-09-09 | 143.0 at 31.505 → **+1.0%** against TWSE 2026-09-09 (NT$141.5) |

*(Yahoo Finance chart API, symbols 2303.TW and UMC; **aggregator, flagged**; `prices_2026-09-13.json`.)*

- **The ADR trades at parity within ±2%** (contrast TSM's +10-14%). **The quote used is the TWSE local close, NT$140.5.**
- **Cap = NT$140.5 × 12,539,542,899 = NT$1,761.8bn.** At the CBC's 31.638, about **US$55.7bn, shown for orientation only
  and never set against NT$ earnings.**
- **The price context, from the company's own filings, not the aggregator:** the treasury purchase averaged NT$101.33
  (May 2026); the 1st CB's reference price was NT$121.7 (late July), the 2nd CB's NT$124.5 (mid-August). The 2025
  20-F proposed a dividend of *"approximately NT$2.60 per common share"*, paid 2026-07-30 (ex 2026-07-08), so the price
  no longer carries it.

### Long-term equity investments: the listed stakes, valued from their own quotes and kept out of owner earnings
**The filing's own figure first.** Q2 2026 consolidated report Note 6(7): *"The carrying amount of investments accounted
for using the equity method for which there are published price quotations amounted to NT$30,031 million, NT$20,488
million and NT$19,088 million as of June 30, 2026, December 31, 2025 and June 30, 2025, respectively. The fair value of
these investments were NT$232,714 million, NT$54,202 million and NT$33,827 million."* **Fair value quadrupled in six months.**

**At 2026-09-11 quotes** (Yahoo, aggregator, flagged; share counts from Attachment 4 and Attachment 7 of the Q2 2026
report, held by UMC and its wholly owned investment subsidiaries at 2026-06-30):

| stake | how held | shares (thousand) | quote 2026-09-11 | NT$bn |
|---|---|---|---|---|
| **Unimicron (3037.TW)**, substrates/PCB | associate, 12.85% | 204,424 | 977.0 | **199.7** |
| Chipbond (6147.TWO) | FVOCI (UMC) 53,164 + FVTPL (Fortune Venture) 13,489 | 66,653 | 181.0 | 12.1 |
| Faraday (3035.TW) | associate, 13.80% | 35,963 | 169.5 | 6.1 |
| SIS (2363.TW) | associate, 18.08% | 92,648 | 50.7 | 4.7 |
| Novatek (3034.TW) | FVOCI; being delivered on exchangeable-bond conversions in June 2026 | 5,279 | 547.0 | 2.9 |
| Topoint (8021.TW) | FVTPL (Fortune Venture) | 4,586 | 418.5 | 1.9 |
| ITE Tech (3014.TW) | FVOCI | 13,960 | 130.5 | 1.8 |
| Holtek (6202.TW) | FVTPL | 22,144 | 55.2 | 1.2 |
| PixArt (3227.TWO) | FVTPL | 1,600 | 181.5 | 0.3 |
| **Total, the nine quoted stakes** | | | | **~230.7** |

- **About NT$231bn, 13.1% of the cap**, of which **Unimicron alone is NT$200bn (11.3% of the cap)**. The rest of Attachment 4
  (unlisted funds, preferred stock, United Industrial Gases, Shin-Etsu Handotai Taiwan, and smaller listed lines) carries
  about NT$15-20bn at filed fair value and is not re-quoted. **The two unlisted holding associates, Hsun Chieh
  (carrying NT$34.2bn) and Yann Yuan (NT$30.3bn), hold UMC's own shares and other listed stock**; not re-valued here.
- **Kept out of owner earnings:** the dividends these stakes pay arrive inside UMC's operating cash as *"Dividend
  received"* (NT$2,387M in 2025) and are **subtracted** in Q4, so the stakes are counted once, at market, in Q5.
- **What the stakes did to reported profit (a Q3 prompt, recorded here because it is where the number sits):** H1 2026
  net income attributable to the parent was **NT$58,431M against operating income of NT$26,226M** (Board 6-K 2026-07-29),
  because *"Share of profit or loss of associates and joint ventures"* was **NT$26,421M** in the half (NT$238M a year
  earlier) and other gains NT$8,169M. Attachment 7: Hsun Chieh's H1 2026 net income **NT$58,128M**, of which UMC recognised
  NT$21,210M. **None of it is operating cash.**

### The filing was read — not tagged data **[E3-27, E4-14]**
- [x] MD&A (Item 5: results, pricing, utilization, product mix, liquidity, capital expenditures) [x] cash-flow statement
  incl. detail lines (F-9, F-10) [x] footnotes (capital stock and treasury, associates and reciprocal holdings, investees,
  securities held, share-based payment, government grants, segment and geography)
- **Primary document: Form 20-F, fiscal year ended 2025-12-31, filed 2026-04-30, accession `0001193125-26-193757`,
  `d91630d20f.htm`, CIK 0001033767.**
- **Also read for the windows** (each carries three years of cash flows): 20-F FY2024 `0001193125-25-092142` · FY2023
  `0001193125-24-111429` · FY2022 `0001193125-23-119772` · FY2021 `0001193125-22-125284` · FY2020
  `0001564590-21-021578` · FY2019 `0001193125-20-121853` · FY2016 `0001193125-17-122107`. FY2014-FY2025 are covered from
  filed statements (`cfread.py` / `cfread_out.json`).
- **6-Ks read:** every 6-K exhibit filed 2023-01-01 to 2026-09-04 was fetched (`k/`); read in full for this file: the Q2
  2026 consolidated financial statements (2026-07-29, `0001193125-26-322030`), the Q2 2026 Board resolutions and
  expansion release (`0001193125-26-322027`), the CB resolutions (2026-06-03), the Economic Daily News clarification
  (2026-06-22), the Novatek disposals (June 2026), the dividend adjustment (2026-06-23), the buyback completion
  (2026-06-29), the CB pricing and proceeds (2026-07-30, 08-05, 08-14, 09-02), the RSA capital reduction (08-14), the
  overseas CB resolution (08-26), and the August revenue report (09-04).
- **Figures cross-checked against the filed statement:** **Net cash provided by operating activities NT$93,872,042
  thousand for 2024**, in the audited CONSOLIDATED STATEMENTS OF CASH FLOWS of the FY2025 20-F (F-9, comparative column),
  equals `companyfacts` `ifrs-full:CashFlowsFromUsedInOperatingActivities` 2024-12-31, **TWD 93,872,042,000**. **One
  disagreement found and resolved toward the filing:** `companyfacts` depreciation (NT$45,337M for 2024, NT$37,551M for
  2023) is not the cash-flow add-back (NT$45,472M, NT$37,758M), so **every (c) figure below uses the filed cash-flow
  line**, not the tag. **FY2025 revenue NT$237,553M** matches the MD&A (*"NT$232,303 million in 2024 to NT$237,553
  million"*).

## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### The business, from the filing: a foundry paid per wafer, at mature nodes, across four countries
**Source: 20-F FY2025 Items 4 and 5; quarterly results releases Q4 2022 to Q2 2026 (6-K exhibits, `guide.py` /
`guide_out.json`).** Item 4: *"Our primary business is the manufacture, or "fabrication", of semiconductors ... for
others. Using our own proprietary processes and techniques, we make chips to the design specifications of our many
customers."* Item 5: *"We price our products on either a per die or a per wafer basis, taking into account ... the
complexity of the technology, the prevailing market conditions, the order size, the cycle time, the strength and
history of our relationship with the customer and our capacity utilization. Because semiconductor wafer prices tend to
fluctuate frequently, we regularly review our pricing on a quarterly basis."*

**Revenue by process node, % of wafer sales** (20-F FY2025 Item 5):

| node | 2023 | 2024 | 2025 |
|---|---|---|---|
| 14nm and under | 0.0 | 0.0 | 0.0 |
| **28nm (the 20-F's row; the releases call it 22/28nm)** | 30.7 | 33.7 | **36.8** |
| 40nm | 13.7 | 13.8 | 16.1 |
| 65nm | 19.2 | 16.0 | 17.0 |
| 90nm | 9.6 | 10.7 | 7.6 |
| 0.11/0.13 micron | 10.6 | 10.2 | 7.4 |
| 0.15/0.18 micron | 9.4 | 10.1 | 9.5 |
| 0.25/0.35 micron | 4.8 | 4.4 | 4.3 |
| 0.50 micron or higher | 2.0 | 1.1 | 1.3 |

Q2 2026 release: *"Revenue from 22/28nm: 37%"*, *"22nm revenue representing 17.5% of second-quarter sales"*. **Nothing at
14nm or below produces revenue**; 63% of 2025 wafer sales came from 40nm and older.

**Revenue by application, % of wafer sales** (Item 4): Communication 45.1 / 42.1 / **41.4** · Consumer 24.0 / 28.4 /
**30.6** · Computer 11.0 / 13.5 / **11.6** · Others 19.9 / 16.0 / **16.4** (2023 / 2024 / 2025).

**Revenue by customer headquarters, %** (Item 4, *"by the location where our customers are headquartered"*): Taiwan 30.7 /
36.1 / **38.6** · China incl. Hong Kong 12.4 / 16.0 / **15.8** · USA 26.6 / 25.0 / **22.0** · Korea 13.9 / 11.3 / **10.7** ·
Europe 11.2 / 7.7 / **8.5** · Japan 5.2 / 3.9 / **4.4**.

**Customer concentration** (Item 3.D): *"Our top ten customers accounted for 62.0%, 55.6% and 57.0% of our operating
revenues in 2023, 2024 and 2025, respectively. Our largest customer from our wafer fabrication segment accounted for
13.1%, 10.4% and 11.8%."* Named (Item 4): *"premier integrated device manufacturers, such as Texas Instruments and Intel,
plus leading fabless design companies, such as MediaTek, Realtek and Novatek."* And: *"Our customers generally do not
have long-term agreements with us to purchase wafers, and many customers do not place purchase orders far in advance
... we do not typically operate with any significant backlog, except in periods of extreme capacity shortage."*
**Concentration is moderate and contracts are short**, the opposite of TSMC's two-customer shape.

**Capacity and utilisation** (Item 4 fab table, thousands of 12-inch equivalents; the annual MD&A series):

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| estimated capacity | 4,674 | 5,022 | 5,163 |
| actual output | 3,201 | 3,451 | 3,885 |
| **utilisation** | **68.5%** | **68.7%** | **75.2%** |

Twelve fabs: eight in Taiwan (Hsinchu 8-inch fabs and Fab 12A in Tainan, 1,629k, the largest), Fab 12i Singapore (684k),
Fab 8N Suzhou and Fab 12X Xiamen in China (442k + 347k), Fab 12M Mie, Japan (471k). Quarterly (releases): 90% (Q4 2022) ·
70 · 71 · 67 · 66 (Q4 2023) · 65 · 68 · 71 · 70 (Q4 2024) · 69 · 76 · 78 · 78 (Q4 2025) · 79 · **85% (Q2 2026)**, with
*"Capacity Utilization: 90%+"* guided for Q3 2026.

**The unit series, filed [E4-55]** (MD&A, foundry wafer shipments; 8-inch equivalents to 2022, 12-inch thereafter, the
filer's own conversion 9,945 / 2.25 = 4,420):

| | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| shipments, k 12-inch eq. | 2,608 | 2,743 | 3,039 | 3,159 | 3,195 | 3,961 | 4,383 | **4,420** | 3,195 | 3,446 | **3,870** |
| **ASP change, filed** | +1.1% | −1.8% | −4.9% | −3.4% | −2.9% | −0.5% | +14.6% | +21.3% | +6.3% | **−5.0%** | **−5.4%** |
| utilisation, filed | 89.8% | 88.6% | 94.4% | 93.1% | 88.7% | 96.9% | 104.4% | 100.6% | 68.5% | 68.7% | 75.2% |

*(2015-2022 shipments are the filed 8-inch figures ÷ 2.25; source sentences, e.g. FY2020 20-F: "a 24.0% increase in
foundry wafer shipment from 7,189 thousand 8-inch equivalent wafers in 2019 to 8,913 thousand"; FY2025 20-F: "from 3,446
thousand 12-inch equivalent wafers in 2024 to 3,870 thousand". ASP sentences: FY2016-FY2025 20-Fs, Item 5 "Pricing".)*
**2025 units are 12% below 2022**, and the 2025 figure was reached with the price falling.

### Unit economics in my own words, no management language
A chip company (a display-driver designer, a Wi-Fi and networking chip designer, a power-management or microcontroller
maker, sometimes a big integrated manufacturer topping up its own fabs) sends UMC a design. UMC runs silicon wafers
through a mature process, one it has usually run for years, and sells the finished wafers, priced per wafer and revised
every quarter. **Revenue is wafers shipped times a price that depends on the node and, as the filing says, on "the
prevailing market conditions" and "our capacity utilization".** The cost is mostly fixed: *"approximately 63.9%, 69.6%
and 70.8%, respectively, of our manufacturing costs consisted of depreciation, a portion of indirect material costs,
amortization of license fees, indirect labor and utilities costs"*. Depreciation alone was NT$56.4bn in 2025, 23.8% of
revenue. **So the margin is set by how full the fabs are and what the market will pay for an old node that other
foundries also run.** When the fabs fill (2021-2022) prices rise and gross margin reached 45.1%; when they empty
(2023-2025) prices are cut at the start of the year and gross margin fell to 29.0%. Cash then goes to new tools for the
next mature node the customers migrate to (28nm, then 22nm, now 12nm with Intel), to dividends, and in 2026 to new
capacity funded partly by convertible bonds.

### The scarce input this business controls
**Qualified, depreciated mature-node capacity with a long record of yields and customer qualifications, spread across
Taiwan, Singapore, China and Japan.** The filing's own claim is modest: *"We believe that our current level of pricing
is comparable to that of other leading foundries in each respective geometry."* **That sentence says the scarce input is
not scarce enough to price above peers**; Q2 tests it against the competitors' own numbers. What Q1 can say: the input
is not a patent (UMC holds *"more than 16,700"* patents but prices at parity), not a brand, and not a unique process; it
is plant, qualification history and customer relationships, plus a geographic spread (Singapore, Japan) that a
customer wanting non-China, non-Taiwan capacity may value.

### Will the fundamentals look broadly the same in ten years?
- **The model: yes.** UMC *"was incorporated in Republic of China (R.O.C.) in May 1980 and commenced operations in April 1982"*
  (20-F Note 1), and the customers' 2025 filings read at Q2 (Himax, Lattice, Allegro, AMD) still buy mature-node wafers from
  foundries; that buying pattern is filed, its persistence for ten years is this file's judgment. The node table has moved slowly: 28nm-and-below went 30.7% → 36.8% in three years, and 0.11-0.50 micron still makes 22.5%.
- **The technology: slower change than TSMC's, but not none, and the filer says so.** Item 5: *"Prices for wafers of a
  given level of technology generally decline over the processing technology life cycle. As a result, we have
  continuously been migrating to increasingly sophisticated technologies to maintain the same level of profitability."*
  **[E3-31]** (*"If a business is complex or subject to constant change, we're not smart enough to predict future cash
  flows"*) **is live, and it is carried to Q2's [E4-04] scope test by name**, as the TSM run did, not discharged here.
- **The price: not the same.** The unit series above shows the one thing that has changed most: a five-year run of price
  erosion before 2020, a shortage-driven spike, and renewed cuts. Whether that is cycle or structure is a Q2 question.

### The perimeter in the window, from the filings, with dates (the brief's instruction; not from memory)
- **No merger, combination or disposal of a foundry business was agreed, completed or abandoned in the filings read.**
  Recorded sweep: the FY2021-FY2025 20-Fs (Item 4 history and development; Note 6(7) investees) and every 6-K exhibit
  2023-01-01 to 2026-09-04 for "merger", "acquisition", "joint venture", "memorandum" and competitor names. **No instance
  found** of a combination with another foundry.
- **Intel, 12nm collaboration — agreed 2024-01-25, in force.** 20-F FY2025: *"On January 25, 2024, we entered into a
  collaboration with Intel Corporation (the "Collaboration"), pursuant to which the parties agreed to jointly develop and
  commercialize new 12nm-related technology ... The Collaboration provides for a long-term agreement between UMC and
  Intel"*; *"we currently expect production of 12nm products in 2027"*; terminable on *"failure to achieve certain
  business or operational milestones"* among other events. **It is a development and manufacturing collaboration using
  Intel's US fabs, not a change of perimeter**: no equity, no entity, no consolidation in the filings.
- **The June 2026 press report, and what the company filed.** 6-K 2026-06-22: the Economic Daily News reported *"United
  Microelectronics Corp. is collaborating with U.S. chipmaking giant Intel to manufacture chips using 12nm and 3nm process
  technologies."* The company's filed response: *"The Company does not comment on speculative reports or market rumors."*
  **No agreement beyond 12nm is filed.**
- **Polar Semiconductor MOU — signed 2025-12-04**, *"to explore collaboration on delivering scalable U.S.-based 8-inch
  production"*. Exploratory; no perimeter change filed.
- **USCXM (Xiamen) buy-out — completed July 2023**: *"After the completion of the transaction in July 2023, the Company and
  Hejian hold 100% of the shares of USCXM"* (US$664 million by UMC, US$120 million by Hejian). A minority buy-out inside
  the window; the 2023 financing statement's *"Decrease in other financial liabilities (21,209,443)"* thousand sits beside
  it. Carried to Q4 as a capital outlay in the window.
- **Associates re-classified**: SIS became an associate in August 2023 (bargain purchase gain NT$494M); Subtron merged into
  Unimicron in January 2023. Investments, not foundry perimeter.
- **Capacity added, 2026**: Board of 2026-07-29 approved capital budget execution of *"NT$ 148,680 million"* for Singapore
  P4 cleanroom and a new Tainan fab shell; the 20-F records Fab 12i P3 in Singapore (*"design capacity of 30,000 wafers
  per month, with production expected to commence in the second half of 2026"*). Organic, not perimeter.
- **Silicon photonics licence from imec, 2025-12-08**, and first *"mass-production delivery of 12-inch photonic ICs to a
  customer"* (Q2 2026 release). A new product line, recorded; no revenue figure filed.

### [E4-46] — five minutes, not five months
The mechanism fits in the paragraph above, every figure is filed, and the business is simpler than TSMC's (no leading
edge, no two-customer concentration). **Whether the mature-node position is a franchise, and what the plant really costs to
maintain, are Q2 and Q4 questions with named documents, not a Q1 competence gap.**

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *UMC makes money one wafer at a time at mature nodes, at a price it reviews quarterly against "prevailing market
  conditions", on a mostly fixed cost base whose margin moves with utilisation. The [E3-31] "constant change" clause is
  live on the filer's own words ("continuously been migrating ... to maintain the same level of profitability") and is
  carried to Q2's [E4-04] test by name.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**Pre-registered before the row was built (operator rule 9, [E4-26]).** Two hypotheses are at risk of being favoured, in
opposite directions, and both are stated so the evidence can refute them: (a) *"UMC is TSMC's OUT with worse numbers"*,
the anchoring risk of running this file half an hour after TSM; and (b) *"2026 is a new regime"*: utilisation 85% and
rising, AI-driven expansion, the Intel 12nm platform, customers wanting non-China capacity, and a share price that
tripled. **So the disconfirming evidence hunted hardest is: filed pricing power at mature nodes (against (a)), and the
full-cycle pricing record before the 2026 upturn (against (b)).** And UMC is tested on its own grounds, not on TSMC's:
TSMC failed only [E4-04] after passing [E3-03]; UMC is tested on [E3-03] first.

### [E3-03], the three criteria, in the customers' and competitors' own filings
**(1) Needed or desired: YES.** NT$237.6bn of revenue; customers include *"Texas Instruments and Intel ... MediaTek,
Realtek and Novatek"* (20-F Item 4).

**(2) Thought by its customers to have no close substitute: NO, on the customers' own filings.**
- **Himax Technologies**, 20-F FY2025 (`0001104659-26-035507`), a display-driver designer: *"We have obtained our foundry
  services from TSMC, UMC, Vanguard, Macronix, Globalfoundries Singapore, PSMC, Nexchip and SKHYSI in the past few years.
  These are among a select number of semiconductor manufacturers that provide high-voltage CMOS process technology
  required for manufacturing display drivers."* Eight named sources, UMC one of them; its supplier table adds SMIC.
- **Lattice Semiconductor**, 10-K FY2025 (`0001437749-26-004100`): *"Lattice partners with United Microelectronics
  Corporation ("UMC") and its subsidiary United Semiconductor Japan Corporation ("USJC") to manufacture our products on its
  130nm, 90nm, 65nm, and 40nm CMOS process technologies"*, and TSMC *"to manufacture our 350nm, 130nm, 55nm and 40nm
  products"*; *"We negotiate wafer volumes, prices, and other terms with our foundry partners ... on a periodic basis."*
  **The same nodes (130nm, 40nm) at two foundries.**
- **Allegro MicroSystems**, 10-K FY2026 (`0001193125-26-233537`): *"primarily United Microelectronics Corporation ("UMC"),
  Polar, Tower Semiconductor Ltd. ("Tower") and Taiwan Semiconductor Manufacturing Company ("TSMC")"*.
- **AMD**, 10-K FY2025 (`0000002488-26-000018`): *"We also utilize TSMC, United Microelectronics Corporation (UMC) and
  Samsung Electronics Co., Ltd. for our integrated circuits (IC) in the form of programmable logic devices."*
- **UMC's own filing concedes it**: *"We believe that our current level of pricing is comparable to that of other leading
  foundries in each respective geometry"* (20-F FY2025 Item 5, the same sentence in every 20-F FY2016-FY2025 read), and
  *"Our customers generally do not have long-term agreements with us to purchase wafers"* (Item 3.D).
- *(Screen, not evidence, operator rule 8: `tools/sources.py:fts_count()` on "United Microelectronics" in 10-K/20-F by CIK
  returned hits at Lattice 29, Tower 24, Qualcomm 20, Himax 20, AMD 14, Allegro 6, Intel 4; `fts_out.json`. The four
  customer documents above were opened and read. One call, GFS/"UMC", returned HTTP 500 and is recorded as an error, not a
  zero.)*

**(3) Not subject to price regulation: YES** (export controls bear on destinations and on nodes below 16nm, where UMC has no
revenue).

**Two of three. [E3-03] fails on criterion (2).** Named mature-node customers source the same nodes from several foundries,
and the filer describes its own price as at parity.

### [E3-43]'s demonstration test, run anyway
*"The existence of all three conditions will be demonstrated by a company's ability to regularly price its product or
service aggressively and thereby to earn high rates of return on capital."* Return on average parent equity (`row.py`,
companyfacts FY2016-FY2024 and the FY2025 20-F): **4.6% (2017) · 3.7 · 4.0 · 10.7 · 21.0 · 30.5 · 17.9 · 13.8 · 11.0% (2025)**.
**The three years 2017-2019 earned under 5% on equity while the fabs ran at 88.7-94.4% utilisation**, which is the condition
under which a franchise shows itself. The two high years are the 2021-2022 global shortage. **Not demonstrated.**

### [E2-44], the two-characteristic test — the decisive section
**(1) Can it raise prices "even when product demand is flat and capacity is not fully utilized"? NO, and it could not raise
them when capacity WAS nearly full.** The filed ASP record (20-F Item 5, each year; `row.py` index 2014 = 100):

| | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ASP change | +1.1% | −1.8% | −4.9% | −3.4% | −2.9% | −0.5% | +14.6% | +21.3% | +6.3% | −5.0% | −5.4% |
| utilisation | 89.8% | 88.6% | 94.4% | 93.1% | 88.7% | 96.9% | 104.4% | 100.6% | 68.5% | 68.7% | 75.2% |
| ASP index | 101.1 | 99.3 | 94.4 | 91.2 | 88.6 | 88.1 | 101.0 | 122.5 | 130.2 | 123.7 | **117.0** |

- **2016-2020: prices fell five years running, −12.9% cumulatively, at 88.6-96.9% utilisation**, described each year in the
  filer's words as *"the continuing nominal price erosion"* (FY2017, FY2018, FY2019 20-Fs).
- **2021-2023: the only price rises in eleven years came from the global shortage, utilisation above 100%** (*"the strong
  market demand primarily due to the recent trends in the semiconductor industry"*, FY2021 20-F).
- **2024-2025: the rise gave back, −10.1% in two years**, at 68.5-75.2% utilisation. The quarterly releases name the mechanism:
  Q4 2023 release, guidance *"ASP in USD: Will decrease by 5%"*; Q4 2024 release, *"ASP in USD: Will decrease by mid-single
  digit %"*; Q1 2025 release, *"the one-time pricing adjustment at the beginning of the year to reflect market conditions."*
- **[E4-37]'s agony test, which the TSM file could not run, CAN be run here, and it reads as agony**: an annual price cut
  announced in advance, guided, and attributed to *"market conditions"*.

**(2) Does dollar volume grow "with only minor additional investment of capital"? NO.** Revenue went from NT$144.8bn (2015)
to NT$237.6bn (2025), **×1.64**, while capex 2016-2025 was **NT$554.2bn against NT$469.1bn of depreciation (1.18×)** and capex
ran **11.1% to 61.9% of revenue** (41.8 · 61.9 · 29.6 · 13.0 · 11.1 · 14.9 · 22.6 · 28.7 · 41.1 · 38.1 · 20.1%, 2015-2025). The
low-capex years 2018-2019 (0.26-0.37× depreciation, net of grants) are the years revenue did not grow (NT$151.3bn → 148.2bn). **Growth came
when capital was spent, not otherwise.**

### [E2-58] — the commodity equation, and what Chinese mature-node capacity did (the brief's central question)
*"persistent over-capacity without administered prices (or costs) equals poor profitability"*; the one exception is *"a cost
advantage that is both wide and sustainable."*

**The capacity, from the Chinese foundries' own releases (evidence ladder: company IR in English, then HKEX; neither is an SEC
registrant):**

| end of year, monthly capacity, k 8-inch equivalent wafers | 2022 | 2023 | 2024 | 2025 | 2022→2025 |
|---|---|---|---|---|---|
| **SMIC** | 714.0 | 805.5 | 948 | 1,059 | **+48%** |
| **Hua Hong** | 324 | 391 | 391 | 486 | **+50%** |
| **the two together** | 1,038 | 1,197 | 1,339 | **1,545** | **+49%** |
| *UMC, for scale (annual estimated capacity ÷ 12, 8-inch eq.)* | *836* | *876* | *942* | *968* | *+16%* |

*Sources: SMIC "Q4_2022 Financials Presentation" and "Q4_2023 Financials Presentation" (smics.com, "Monthly Capacity" rows
714,000 and 805,500); SMIC "SMIC REPORTS 2024 FOURTH QUARTER RESULTS" (smics.com news 7918: "Monthly capacity was 948
thousand standard logic 8-inch equivalent wafers by the end of the year") and "2025 FOURTH QUARTER RESULTS" (news 7949:
"Monthly capacity was 1,059 thousand ... increased by around 111 thousand wafers"); Hua Hong "Reports 2023 Fourth Quarter
Results" (HKEX 2024020600549: "Monthly capacity was 391,000 8-inch equivalent wafers at the end of 4Q 2023", prior year 324),
"2024 Fourth Quarter Results" (HKEX 2025021300345, 391,000) and "2025 Fourth Quarter Results" (HKEX 2026021200389, 486,000).
**Definitions differ** (the Chinese figures are year-end monthly capacity; UMC's is estimated annual capacity), so the UMC
line is scale, not a like-for-like share. Saved in `peers/`.*

**What the new capacity did to prices, in the Chinese foundries' own words:**
- **SMIC** capex **US$7.33bn (2024) and US$8.1bn (2025) against revenue of US$8.03bn and US$9.33bn: 91% and 87% of revenue**
  (news 7918, 7949). Gross margin **38.0% (2022) → 19.3% (2023) → 18.0% (2024) → 21.0% (2025)**; its 2023 explanation: *"The
  competition within the industry was fierce. As a result, the Group's average capacity utilization rate declined, wafer
  shipment decreased and product mix changed. In addition, the Group was in high investment period, and depreciation increased"*
  (news 7895). **2025 utilisation 93.5%, gross margin 21.0%.**
- **Hua Hong** gross margin **27.7% (2021) · 34.1% (2022) · 21.3% (2023) · 10.2% (2024) · 11.8% (2025)**: 2023 *"mainly due to
  decreased average selling price and increased depreciation costs"*; 2024 *"mainly due to decreased average selling price and
  increased depreciation costs"*. **In 2025 it ran at 106.1% utilisation and earned an 11.8% gross margin.** A mature-node
  foundry that is overfull and earns 12% gross is the price the others are competing against.
- **GlobalFoundries**, 20-F FY2025 (`0001709048-26-000022`), the Western mature-node peer, names the mechanism: *"Following the
  implementation of those controls, the Chinese semiconductor industry, with significant government support, has accelerated
  building its own foundry capacity, and shifted to focus domestic manufacturing on mature nodes (i.e., 28nm and larger
  technology nodes), and China's foundry capacity is expected to grow faster than expected demand at those nodes."* Its risk
  heading: *"could lead to underutilization or significant ASP erosion for our fabrication facilities."*
- **UMC's filing**, same three years: ASP −5.0% and −5.4%; utilisation 68.5-75.2%; gross margin 34.9% → 32.6% → 29.0%; and
  the risk factor: *"New entrants and consolidations in the foundry business are likely to initiate a trend of competitive
  pricing and create potential overcapacity in legacy technology"* (20-F FY2025 Item 3.D).
- **What the record does NOT show, stated so it is not over-read [E3-61]:** UMC's filings never attribute a price cut to
  Chinese competitors by name (recorded sweep of the FY2023-FY2025 20-Fs and the 2023-2026 releases for "China", "Chinese",
  "SMIC", "Hua Hong", "local foundr": **no instance found** of a Chinese competitor named as the cause of UMC's price). The
  cuts coincide in time with the Chinese build and with a demand trough; **the filings do not separate the two causes, and
  this file does not claim to.** Either cause is [E2-58]'s mechanism: prices set by capacity the company does not control.
- **The disclosure change, carried to Q3:** the 20-F paragraph *"We believe that our primary competitors in the foundry
  services market are Taiwan Semiconductor Manufacturing Company Limited, Semiconductor Manufacturing International
  (Shanghai) Corporation and Globalfoundries Inc. ... Other competitors such as ... Hua Hong Semiconductor Manufacturing
  Corp. ..."* appears in every 20-F read from FY2016 to **FY2023** and is **absent from FY2024 and FY2025**, the two years the
  price fell.

**A cost advantage "both wide and sustainable"?** The row below shows UMC's gross margin above SMIC's and Hua Hong's in 2023-2025
(29.0% against 21.0% and 11.8% in 2025) and above GFS and Tower. **That is a real relative cost-and-mix position.** It is not
wide enough to hold price (the ASP fell) or return (ROE 11.0% in 2025, under 5% in 2017-2019), and it is not shown to be
sustainable against a competitor spending 87-91% of revenue on capacity with state support. **The exception is not established.**

### [E4-04] — must the moat be continuously rebuilt? The filer answers in its own words.
*"A moat that must be continuously rebuilt will eventually be no moat at all."* 20-F FY2025, Item 5: *"Prices for wafers of a
given level of technology generally decline over the processing technology life cycle. As a result, we have continuously been
migrating to increasingly sophisticated technologies to maintain the same level of profitability."* And Item 5.B: *"To
maintain competitiveness at the same capacity, we are required to make adequate investments in plant and equipment."* **The
spending buys the replacement** (28nm, then 22nm at *"17.5% of second-quarter sales"* in 2026, then 12nm with Intel from 2027),
**and a lapse does not merely narrow the position: the filer says the price of each node declines by itself.** Unlike TSMC, UMC
is not riding a wave at the front of it [E3-51]; it is following the wave at the price the followers set.

### [E2-45] — the attacker's test, and it has been run by a state
*"how I would like, assuming I had ample capital and skilled personnel, to compete with it."* SMIC and Hua Hong are that attacker,
on their own figures: capacity +49% in three years, SMIC capex near 90% of revenue, Hua Hong content at a 12% gross margin. **The
attacker did not need to beat UMC's technology; it needed only capacity at the same nodes.** Intel Foundry, the other attacker
with capital, chose to partner with UMC at 12nm rather than fight it, which says UMC's process know-how at mature nodes has value
to Intel; it does not say customers lack substitutes.

### THE COMPETITOR ROW — required [E3-28]. Same metric, same window, filing-sourced.

**Gross margin %:**

| | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **UMC** | 21.9 | 20.5 | 18.1 | 15.1 | 14.4 | 22.1 | 33.8 | **45.1** | 34.9 | 32.6 | **29.0** |
| TSMC | 48.7 | 50.1 | 50.6 | 48.3 | 46.0 | 53.1 | 51.6 | 59.6 | 54.4 | 56.1 | 59.9 |
| GlobalFoundries | — | — | — | — | −9.2 | −14.7 | 15.4 | 27.6 | 28.4 | 24.5 | 24.9 |
| Tower Semiconductor | — | 24.3 | 25.5 | 22.5 | 18.6 | 18.4 | 21.8 | 27.8 | 24.8 | 23.6 | 23.2 |
| SMIC | *not SEC* | | | | | | | 38.0 | 19.3 | 18.0 | 21.0 |
| Hua Hong | *not SEC* | | | | | | 27.7 | 34.1 | 21.3 | 10.2 | 11.8 |
| Intel Foundry | *operating margin only* | | | | | | | | −38 | −76.8 | −57.9 |
| Vanguard International | *company IR rung returned HTTP 403 to both fetchers (`vis.com.tw` press pages); MOPS not attempted* | | | | | | | | | | |
| Samsung Foundry | *not disclosed in any document on the shelf (TSM run)* | | | | | | | | | | |

**Operating margin %, UMC:** 7.5 · 4.2 · 4.4 · 3.8 · 3.3 · 12.4 · 24.3 · 37.4 · 26.0 · 22.2 · 18.5 (2015-2025). **Capex % of revenue,
peers:** Tower 17.4 → 28.4 (2016-2025), GFS 10.1 → 10.6 (2019-2025), SMIC 91% (2024) and 87% (2025).

*Sources: UMC `companyfacts` FY2015-FY2024 (cross-checked at Step 0) and 20-F FY2025 `0001193125-26-193757` (gross profit NT$68,906M
on revenue NT$237,553M; filed: "Our gross margin decreased from 32.6% in 2024 to 29.0% in 2025"); TSMC and GFS from the TSM run's
`row_out.json` (TSMC 20-F `0001628280-26-025362`, GFS 20-F `0001709048-26-000022`); Tower `companyfacts` us-gaap through its 20-F
FY2025 `0001178913-26-002318` (2023 operating margin 38.5% includes the Intel merger-termination fee, gross margin unaffected);
SMIC and Hua Hong as cited above; Intel Foundry from the INTC run (10-K FY2025 Note 3). Arithmetic in `row.py` / `row_out.json`,
`peers.py` / `peers/peers_out.json`.*

- **Peers named: 8 of the industry's ~9 scaled foundries** (TSMC, Samsung, Intel Foundry, GlobalFoundries, SMIC, Hua Hong, Tower,
  Vanguard, plus UMC); **metrics obtained for 6** (gross margin for TSMC, GFS, Tower, SMIC, Hua Hong; operating margin for Intel
  Foundry). **Missing: Vanguard (company rung blocked) and Samsung (not disclosed).**
- **Does a missing peer hold the class PROVISIONAL?** Not here, and the reason is direction, as in the TSM file: the verdict rests
  on UMC's own filed prices and returns and on its customers' filed sourcing, not on a ranking in the row. **No figure Vanguard or
  Samsung could file would turn a five-year price decline at 89-97% utilisation into pricing power.** The missing rows are
  recorded as a limit, not as a work order that could change the verdict.
- **Relative position, stated fairly:** UMC's gross margin sits **second in every year 2021-2025 among the six**, above every
  mature-node peer with figures, and its 2022 peak (45.1%) was the best mature-node year in the row. **A good position among
  commodity producers is still a position among commodity producers.**
- **[E3-61], the row's limit:** the row cannot show how SMIC and Hua Hong will price once their build finishes, and the corpus says
  Munger had no model for that.

### Untapped pricing power [E3-33, E5-28]
Claiming the class is claiming near-monopoly [E5-28]. **The filer claims parity pricing and its customers name up to eight
alternatives. No near-monopoly; no untapped pricing power.**

### THE FAIR COUNTER-CASE, stated as its best advocate would state it [E4-51]
*"You are reading the trough. In 2026 utilisation went 79% → 85% → 90%+ guided, Q2 2026 guidance was 'ASP in USD: Will increase by
low-single digit', the 8-inch portfolio is 'seeing a strong rebound', 22nm doubled, the board is building a new Tainan fab for AI
demand, and silicon photonics shipped its first 12-inch volume. China's capacity is for China: GlobalFoundries itself says Chinese
demand 'will have a preference for domestic sourcing', which pushes every non-Chinese customer who wants mature nodes outside China
toward the one scaled pure-play with fabs in Taiwan, Singapore and Japan and a US partner in Intel. UMC earns the best mature-node
margin in the row, eight points above SMIC's and more than twice Hua Hong's. The 2016-2019 record predates the geopolitical split. Ruling it out
now is [E3-47]'s error of omission."* **Every clause is filed** (Q2 2026 release; Q1 2026 guidance; GFS 20-F; the row).

**The answer on the filed record.** The counter-case establishes a **cycle turning up** and a **relative position**; both are granted.
It does not establish **[E3-03]'s second criterion** (the customers' own filings list the substitutes), and **[E2-44] asks about the
downturn, not the upturn**: the test is what happens to price when capacity is *not* full, and UMC's answer, filed in seven of
eleven years, is that price falls, and in 2016-2019 it fell even when capacity *was* full. **A preference for non-China capacity is a
regime [E2-59]** (*"the moat belongs to the regime"*), set by export controls and tariffs UMC does not control, and a regime is
*"how it ends"* when it changes. The 2026 upturn is recorded at Q6 as the evidence that would have to persist through a full cycle to
reopen this file. **The price of being wrong is recorded at [E3-47], not argued away.**

### CLASS AND DIRECTION
- Needed or desired [x] · **no close substitute [ ] — fails, on Himax, Lattice, Allegro and AMD's filings and UMC's own "comparable"
  pricing** · not price-regulated [x]
- **Must the moat be continuously rebuilt? YES**, in the filer's words (*"continuously been migrating ... to maintain the same level
  of profitability"*). **Does success depend on a great manager? No key-person dependence found [E4-23]**; the CEO changed in 2026
  (*"He was named Chief Executive Officer in 2026"*) with no filed change in the business. The filing lists key-person risk as
  boilerplate (*"Our future success to a large extent depends on the continued services of our Chairman and key executive
  officers"*), recorded, not a finding.
- **Primary moat metric, filing-sourced, and its trend: ASP index 2014 = 100 → 88.1 (2020) → 130.2 (2023) → 117.0 (2025); gross margin
  21.9% → 45.1% (2022) → 29.0% (2025).** Direction over 2022-2025: **narrowing**, with an upturn in H1 2026 (Q2 2026 gross margin
  32.5%).
- **Class: NONE — a commodity producer under [E2-58] with a better-than-peer cost and mix position, not a franchise.**

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  *OUT on [E3-03] criterion (2) and on [E2-44](1), with [E2-58]'s mechanism filed by UMC, its peers and the Chinese foundries, and
  [E4-04] confirmed in the filer's own words. Different grounds from TSM: TSMC passed [E3-03] at the leading edge and failed only
  [E4-04]; UMC fails the franchise definition itself. Its relative position among mature-node foundries is real and is recorded.*
  **The file closes here. Q3 to Q6 are RECORDED, NOT GOVERNING.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — **RECORDED, NOT GOVERNING**
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

⛔ **Q2 closed the file (OUT on [E3-03] and [E2-44]). Everything from here to Q6 is recorded because the queue's output contract
requires a price and because the evidence was gathered; none of it governs, and none of it can reopen Q2** (the guardrail: *"a
strong Q3 cannot promote a name, repair Q2, or substitute for Q4"*).

### STEP 1 — THE WEIGHT CASE, declared first
- [x] **Daily execution [E3-38, E3-43]**: Q2 found UMC to be *"a business"*, not a franchise, and a commodity producer under
  [E2-58]; [E3-43]: *"a business, unlike a franchise, can be killed by poor management."* Capacity timing (the 2026 Tainan fab shell
  and Singapore P4, NT$148.7bn of capital budget) and quarterly pricing are recurring decisions.
- [ ] **Control**: no. [ ] **Leverage**: no (net cash about NT$50.8bn at 2025-12-31, Q4).
- **Case declared: Q3 would be a BINARY GATE on the daily-execution determinant.** No price compensates **[E1-16, E3-29, E5-35]**.

### Honesty — the binary [E5-16], each matter dated to when it became PUBLIC
**The Micron / Fujian Jinhua trade-secret matter. Read from the company's own filings, in the order the public learned it.**

| public | what | the company's filed words | document |
|---|---|---|---|
| **2017-08-31** | Taichung District Prosecutors Office indictment under the R.O.C. Trade Secret Act | *"alleging that our employees misappropriated the trade secrets of Micron Technology Inc. ... We intend to defend vigorously against this allegation"* | 20-F FY2017 `0001193125-18-132616` |
| 2017-12-05 | Micron civil action, N.D. California | (same 20-F) | same |
| 2018-01-12 | UMC sues Micron's Chinese subsidiaries for patent infringement in the Fuzhou Intermediate People's Court | *"we filed three patent infringement actions with the Fuzhou Intermediate People's Court against, among others, Micron (Xi'an) Co., Ltd. and Micron (Shanghai) Trading Co., Ltd."* | 20-F FY2021, FY2022 |
| **2018-11-01** | US DOJ indictment and civil complaint unsealed | *"The indictment ... alleges that the Company and certain of its employees conspired to steal trade secrets of Micron"*; *"UMC regrets that the U.S. Attorney's Office brought these charges without first notifying UMC"* | 6-K 2018-11-02 `0001564590-18-026359` |
| 2018-11-03 | press reports of a fine up to US$20 billion | *"innocent is presumed unless and until proven guilty. The Company will ... raise a plea against such indictment"* | 6-K 2018-11-05 `0001564590-18-026604` |
| 2019-03-14 | US shareholder securities class action (10b-5) | settled after mediation; fairness hearing adjourned to April 2021 | 20-F FY2020 `0001564590-21-021578` |
| **2020-06-12** | **Taichung District Court: adverse criminal ruling** against *"UMC, two of its current employees and a former employee"* | UMC appealed | 20-F FY2021 `0001193125-22-125284` |
| **2020-10-29** | **US guilty plea, approved by the court** | *"the Company pleaded guilty to one lesser count of receiving and possessing stolen trade secret, agreed to pay a fine of $60 million USD and to cooperate with the U.S. Department of Justice during a three-year term of non-supervised probation"*; the same release: *"The one trade secret at issue in the guilty plea and Plea Agreement related to older technology that had been in mass production worldwide for several years."* | 6-K 2020-10-29 `0001564590-20-048490` |
| 2021-11-26 | global settlement with Micron | *"UMC will make a one-time payment of an undisclosed amount to Micron"* | 6-K 2021-11-26 `0001564590-21-058378` |
| **2022-01-27** | **Taiwan Intellectual Property and Commercial Court: UMC convicted** | *"sentenced UMC to a fine of NT$20,000,000 and a two-year term of probation"*; defendants *"UMC, two of its current employees and a former employee"*; UMC *"appreciates the fairness of the ruling"* | 6-K 2022-01-27 `0001564590-22-002561` |
| 2024-01-27 | Taiwan probation completed | *"UMC completed the probation period successfully and the sentence has been terminated"* | 20-F FY2023 `0001193125-24-111429` |
| 2025-2026 | no longer disclosed | FY2025 20-F Item 8: *"nor are there any other material litigation or non-litigation matters required to be disclosed"* | 20-F FY2025 |

**The read, under the corpus's own tests.**
- **[E5-16]**: *"We are understanding about business mistakes; our tolerance for personal misconduct is zero."* A theft of a competitor's
  trade secrets for use in a technology transfer to a third party is not a business mistake. **It ended in a criminal plea by the
  company in the United States and a criminal conviction of the company in Taiwan.**
- **[E5-22]**: the framework's reading is that penalty size is not seriousness, in either direction; the corpus's words: *"the main
  problem was they didn't act when they learned about it."* The fines (US$60 million; NT$20 million) were small beside the charges dismissed (the DOJ release itself cites *"alleged
  damages and penalties of $400 million USD to $8.75 billion USD"*). **What the filings show the company did when it learned**: it
  defended (*"We intend to defend vigorously"*) for over four years in Taiwan (indictment 2017-08-31, conviction 2022-01-27) and two in
  the US (unsealed 2018-11-01, plea 2020-10-29); it *"suspended the joint technology
  development activities with Jinhua"* (20-F FY2020); and at the Taiwan ruling of January 2022 **two of the convicted individuals were
  still described as "current employees."** Recorded sweep of the FY2021-FY2025 20-Fs, the 6-K of 2022-01-27 and every 6-K exhibit of 2023-2026 for "terminat",
  "dismiss" and "disciplin" within 250 characters of "Micron", "Jinhua" or "trade secret" (the hits were the civil case's dismissal and
  the probation's termination): **no instance found** of the employees being dismissed or disciplined.
- **[E2-68], conduct across an information asymmetry**: the plea release describes the stolen secret as *"older technology"*, a
  minimising frame on the one matter where the company holds the facts and the reader does not.
- **Dated to public, point-in-time**: every element above was public by **2022-01-27**; the plea by **2020-10-29**.
- **[E5-17]'s cap, and the scope question for the operator.** The individuals charged were one current and two former employees; **no
  director or executive officer is named as a defendant in any filing read**, and the 20-F does not say who approved the 2016 DRAM
  Technology Cooperation Agreement with Jinhua beyond the company itself. **But the plea and the Taiwan conviction are the company's
  own, the arrangement was a filed material contract of the company** (*"DRAM Technology Cooperation Agreement, dated May 13, 2016,
  between UMC and Fujian Jinhua"*, 20-F FY2020 Item 8, referring to Item 10.C), and the current Chairman (*"joined the Company in 1991"*,
  formerly CFO) and CEO (*"became Co-President in 2017"*) were both with the company throughout (20-F FY2025 Item 6).

**Recorded verdict on the binary: an integrity failure on the filed record — OUT, were Q3 governing.** *Flagged to the operator
(prime rule 2): this is the first run in the queue whose honesty verdict rests on a corporate criminal plea and conviction rather than
on an individual's conduct. [E5-16] speaks of "personal misconduct"; [E2-31] of *"managers who lack admirable qualities"*. Whether a corporation's plea attaches to
the managers who remained in office is a scope reading, and this file states it rather than settles it. A reader who scopes [E5-16] to
individuals only would score this UNKNOWABLE (the individual responsibility is not in any document), never IN.*

### STEP 2 — THE FLAGS
- [ ] **weak accounting [E4-22]**: no restatement found. **But one prompt, recorded:** the reciprocal holdings. UMC's associates Hsun
  Chieh (36.49% owned), SIS (18.08%) and Yann Yuan (26.78%) hold 904.5 million UMC shares; when UMC's share price tripled in 2026, **Hsun
  Chieh's H1 2026 net income was NT$58,128M and UMC recognised NT$21,210M of it** (Q2 2026 report, Attachment 7), inside a half-year net
  income of NT$58,431M against operating income of NT$26,226M. The filings do not say how much of Hsun Chieh's income is the revaluation of
  UMC's own shares. **A prompt to read, not a finding**; it sits wholly outside owner earnings.
- [ ] **unintelligible footnotes**: no; the Attachments are unusually complete.
- [x] **trumpeted projections [E4-22] third flag — FIRES as a prompt, with the record set beside it [E3-48].** Quarterly guidance on
  shipments, ASP, gross margin and utilisation every quarter (`guide.py`). **Fourteen quarters, guidance against the next quarter's
  outturn (Q1 2023 to Q2 2026): gross margin at or above the guided level in 12, below in 2** (Q3 2024: *"mid-30% range"*, outturn 33.8%;
  Q2 2025: *"approximately 30%"*, outturn 28.7%); **utilisation within or above guidance in all 14** (Q1 2025: 69% against *"approximately
  70%"*). No multi-year growth target was found in the releases read. **The record is conservative, not make-the-numbers.**
- [ ] **serial share issuance [E5-15]: a prompt in 2026, not a history.** Issued shares 12,624,318,715 (2016, incl. 400 million treasury) →
  11,724,318,715 (2019, after cancellations) → 12,588,156,344 (2025, after convertible conversions in 2020 and RSA grants of ~33 million a
  year) → 12,539,542,899 outstanding (2026-08-10). **Ten-year outstanding change: about +2.6%.** **In 2026 alone: NT$16.9bn of domestic
  convertibles (~120 million shares at conversion) and a resolution for up to US$1.8bn of overseas convertibles (of the order of 400 million
  shares, an illustration, Step 0).** Carried as a prompt.
- [ ] **EBITDA promotion [E4-29]**: **no.** Recorded sweep: *"EBITDA"* appears **zero** times in the FY2025 20-F and in **none** of the 291 6-K
  exhibit files fetched for 2023-2026. The headline metrics are gross margin, operating margin, EPS and utilisation.
- [ ] **filed-figure tells [E4-30]**: cash taxes as % of pretax income 17.1 (2015) · 49.2 · 23.0 · 47.0 · 12.9 · 0.1 · 3.3 · 4.3 · 23.4 · 17.5 ·
  **13.2% (2025)**: erratic (tax credits and loss carryforwards), **not a falling trend**; reported growth is not smooth.
- [x] **metric-switching and disclosure change [E2-49], a prompt:** the named-competitor paragraph (TSMC, SMIC, GlobalFoundries, Samsung,
  Intel, Hua Hong and others) present FY2016-FY2023, **absent from FY2024 and FY2025**, the two years of price cuts (Q2). Not a headline
  metric; a disclosure that disappeared as it became unflattering. **Prompt, not finding.**
- [x] **dividends and issuance in the same season [E2-52], a prompt:** the NT$32,704M cash dividend was paid 2026-07-30; convertible proceeds
  of NT$12,120M (2026-08-05) and NT$4,793M (2026-09-02) followed, and the US$1.8bn overseas issue was resolved 2026-08-26, **all "for
  purchase of machinery"**. Over 2021-2025, cash dividends of **NT$175.7bn** exceeded capex-end owner earnings of **NT$136.6bn** (Q4) and
  were covered by judged-end owner earnings (NT$233.7bn). **Money is fungible; the dividend is being maintained while the expansion is
  financed.**

### STEP 3 — THE PRIMARY TEST [E2-01]
Return on average parent equity **4.6% (2017) · 3.7 · 4.0 · 10.7 · 21.0 · 30.5 · 17.9 · 13.8 · 11.0% (2025)**, nine-year mean **13.0%**,
without leverage (net cash). Equity attributable to the parent **NT$212.8bn (2016) → NT$365.8bn (2025) → NT$443.9bn (2026-06-30**, Board
6-K, lifted by the associates' gains). **Adequate only in the shortage years.** **[E3-59]'s "hand they were dealt"**: against its row,
management earned the best mature-node gross margin every year 2021-2025 (Q2). **The operators ran a commodity business better than
their peers; the business is still a commodity business [E2-37].**

**The half-owner test [E2-26]:** node mix, application mix, customer geography, fab-by-fab capacity and utilisation, ASP change each year,
the quarterly guidance, and the full investee and securities attachments are given. **Positive pole on operating disclosure. Against it**:
the minimising plea release, the vanished competitor paragraph, and no disclosure of how much associate income is the revaluation of
UMC's own shares.

### Capital allocation
- **Buybacks [E5-08, E4-31]:** 2018 NT$6.15bn, 2019 NT$2.97bn (cancelled, *"for cancellation"*); 2020 NT$1.68bn (transferred to employees);
  **2026: 30,551,000 shares at an average NT$101.33 (NT$3.10bn), "For transfer to employees".** Against the conservative floor range in Q5
  (roughly NT$30-110 a share on valid bases, stakes included), **NT$101 is at the top of the range, not at a material discount. [E5-08]
  condition (2) fails — CAPITAL ALLOCATION FLAG**, stated with the humility clause **[E4-13]**: *"They also know a whole lot more about
  them than I do"*; this rests on this file's own value range. **It binds position size, never the discount rate.** The purchase was also
  for employees, not for cancellation, so it is compensation funded at market, not a return of capital.
- **Capex against depreciation:** 0.26-0.77× net of grants in 2017-2020 and 2025; 1.85-2.31× in 2022-2024 (Q4). **The spending follows the
  cycle**: under-spent in the trough of 2018-2019, over-spent into the 2022-2024 peak and glut, and in 2026 raised again (2026 capex
  *"revised upward to US$2 billion"* from US$1.5 billion; NT$148.7bn capital budget) as utilisation passed 85%.
- **Acquisitions:** USJC (Mie, Japan) 2019, NT$12.8bn; USCXM minority buy-out 2023, NT$21.2bn in financing cash flow; Unimicron capital
  injections; the TGVest private-equity fund commitment of up to NT$1.7bn (2026-07-29). **No acquisition post-mortem found [E4-39]**
  (recorded sweep of the FY2020-FY2025 20-Fs for USJC and USCXM returns: no instance found).
- **The institutional imperative [E2-30]:** [ ] resists change · **[x] projects soak up available funds, a prompt**: the Tainan fab shell
  and Singapore P4 approved the quarter utilisation reached 85%, financed with convertibles · [ ] staff studies · **[x] peer imitation, a
  prompt**: *"leveraging a disciplined, ROI-driven strategy"* for an AI-driven build is the language of every foundry's 2026 capacity release.
- **[E3-66], where a minority shareholder stands:** R.O.C. company law; ADS holders vote only through the depositary (*"holders of ADSs have
  limited ability to vote"*, Item 10). **And the board is seated partly through circular holdings**: the CEO sits as *"Representative of
  Silicon Integrated Systems Corp."* and the President and COO as *"Representative of Hsun Chieh Investment Co., Ltd."* (Item 6), both
  UMC associates that hold UMC shares (Hsun Chieh 3.51%, SIS 2.12%). **Management is seated in part by votes cast by companies management
  influences.** R.O.C. law strips the vote only from shares held by entities UMC owns more than 50% of (Item 10), which these are not.

### Pay, and what it vests on [E4-27]
- **Aggregate, not per person** (the 20-F does not give individual pay): *"The aggregate compensation paid and benefits in kind granted to
  our executive officers in 2025 were approximately NT$923.4 million (US$29.4 million), which included NT$286 million (US$9.1 million) as
  bonus"*; directors NT$48 million, *"the distribution percentage for directors is 0.1%"*.
- **Employee bonus: *"no less than 5% of such annual profits before tax as employee bonus"*** (Articles, Item 10), paid in cash and inside
  operating cash. **Pay rises with pretax profit**, including profit from associates' share-price gains.
- **RSAs** (Note 6(20)): four-year plans; vesting *"Beginning from the end of two years since the date of grant, those employees who fulfill
  both service period and performance conditions set by UMC"*; *"The 2024 restricted stock plan for employees includes market
  conditions"* (Monte Carlo valued). **The performance conditions are not specified in the 20-F** (recorded sweep: no instance found of the
  metric); **[E4-27]'s question, what the incentive rewards, cannot be fully answered from the filing**, and the market condition points at
  the share price **[E3-50]**, as a prompt.

### Converging prompts [E4-52]
**Five prompts point the same way:** an expansion approved at the top of a utilisation upswing; convertible issuance to fund it; a buyback
at the top of the value range; a share price that tripled in nine months (NT$47.20 at the December 2025 RSA measurement date, Note 6(20),
to NT$140.5); and a disclosure that stopped naming the Chinese competitors. **Together they are one reinforcing system toward more capacity
into an industry the Chinese foundries' own releases show adding 49% in three years**, which is [E2-58]'s mechanism (*"nothing fails like
success"*). **Offsetting, on the record:** conservative guidance beaten in 12 of 14 quarters; the phased design of the build (*"minimizing
upfront depreciation"*); and capex held at 0.35-0.57× depreciation in 2019-2020 when prices fell.

### THE GUARDRAIL
- [x] Nothing in this Q3 is used to promote the name, repair Q2 or substitute for Q4 **[E2-37, E2-38, E3-39]**.
- [x] Key-person dependence: none found (Q2).
- [x] No great-manager thesis is relied on; the manager's relative excellence among mature-node peers is recorded as operating skill in a
  commodity boat **[E2-37]**.

- **VERDICT (RECORDED, NOT GOVERNING): [ ] IN  [x] OUT (integrity failure is permanent)** — *on the company's 2020 US guilty plea and 2022
  Taiwan conviction for trade-secret offences, with convicted employees retained as of the 2022 filing and a minimising public account;
  the scope question (corporate plea against [E5-16]'s "personal misconduct") is flagged to the operator above. Separately live: the
  buyback capital-allocation flag, and five converging prompts toward capacity.*

## Q4 — WILL IT SURVIVE? — **RECORDED, NOT GOVERNING**

### Owner earnings — the one number **[E2-23]**
**Construction (CONVENTION, framework VI): operating cash flow − dividends received − equity-settled SBC − (c).** Run-specific, disclosed:
- **Dividends received are subtracted** (NT$2,387M in 2025) because the listed stakes that pay them are valued at market in Q5; counting
  both would count the stakes twice. **Interest received and paid stay in** (the cash that earns it is inside the cap).
- **TSMC's prepayment strip does NOT apply, and the reason is filed:** UMC's customer capacity deposits (*"Guarantee deposits mainly
  consisted of deposits of capacity reservation"*, NT$39.8bn at 2025-12-31) flow through **financing** activities (*"Increase in guarantee
  deposits 11,651,109 ... 2,827,304"* thousand, 2023 and 2025), so operating cash is not inflated by them. **Employee profit sharing**, as at
  TSMC, is a cash expense already inside operating cash (the Articles' *"no less than 5%"* of pretax profit).
- **Government asset grants reduce (c)**, as at TSMC (NT$5,098M in 2025).

**SBC: RESOLVES AND IS COMPLETE.** The cash-flow *"Share-based payment"* add-back is filed for every year: 0.8 (2015), — (2016), — (2017),
695.7, 366.2, 959.2, 1,745.7, 1,351.7, 1,031.9, 788.8, **491.3 (2025)**, NT$ millions (FY2016-FY2025 20-Fs; `cfread_out.json`). **[E3-70]'s
market-value measure, checked:** RSA grants at grant-date fair value (Note 6(20)) were NT$4,361M (2020 plan, 200,030 thousand shares at
NT$21.80), NT$67M (2021), NT$1,024M (2022), NT$1,307M (2023), NT$1,294M (2024), NT$1,371M (2025); the 2021-2025 mean of NT$1,013M is below the
mean charge of NT$1,082M, and both are about 1% of operating cash. **Immaterial either way; the charge is used.**

**Maintenance capex, the central judgment.**
- **What the filing gives:** *"To maintain competitiveness at the same capacity, we are required to make adequate investments in plant
  and equipment"* (Item 5.B); *"Prices for wafers of a given level of technology generally decline over the processing technology life
  cycle. As a result, we have continuously been migrating to increasingly sophisticated technologies to maintain the same level of
  profitability"* (Item 5); depreciation 23.8% of 2025 revenue; *"approximately ... 70.8%"* of manufacturing cost fixed.
- **The natural experiment in the filing:** in **2017-2020 net capex ran at 0.26-0.73× D&A** (four years below depreciation). In those
  years the ASP fell every year and ROE was 3.7-10.7%; in **2022-2024 capex ran at 1.85-2.31× D&A** to catch up and to build 22/28nm. **Spending
  less than depreciation did not keep the place** [E5-20].
- **The case: [E5-20]'s exception class. The D&A end is INVALID** and displayed only.
- **The two ends carried:**
  - **Capex end (conservative): net capex = PP&E + intangibles − asset grants**, all of it treated as required.
  - **Judged end: 1.093 × D&A**, the full-decade 2016-2025 ratio of net capex to D&A (net capex NT$540.5bn against D&A NT$494.6bn, `oe.py`), a decade
    that contains both the under-spend and the catch-up and over which the ASP index ended above its start (2014 = 100, 2025 = 117.0).
    **A guess, stated as one [E2-23]**: it over-states (c) by whatever share of the decade's capex bought organic capacity growth (the
    fab table shows capacity rising, part of it bought through the 2019 USJC acquisition, not capex), and under-states it if 22nm and 12nm
    tools cost more per wafer than the decade's mix.
  - **Acquisitions of capacity outside capex**, displayed, not in either end: USJC 2019 NT$12.8bn (investing); USCXM minority buy-out 2023
    NT$21.2bn (financing). **About NT$3.4bn a year over the decade.**

**Owner earnings by year, NT$ millions** (`oe.py` / `oe_out.json`):

| year | OCF | − div. received | − SBC | net capex | D&A | **OE, capex end** | **OE, judged end** | OE, D&A end (INVALID) | capex/D&A |
|---|---|---|---|---|---|---|---|---|---|
| 2015 | 59,788 | 917 | 1 | 61,338 | 45,472 | −2,467 | 9,175 | 13,398 | 1.35 |
| 2016 | 46,450 | 794 | 0 | 83,549 | 51,984 | **−37,893** | −11,155 | −6,328 | 1.61 |
| 2017 | 52,474 | 585 | 0 | 38,764 | 53,099 | 13,125 | −6,140 | −1,209 | 0.73 |
| 2018 | 50,935 | 782 | 696 | 13,299 | 52,049 | 36,158 | −7,425 | −2,592 | 0.26 |
| 2019 | 54,904 | 819 | 366 | 18,344 | 49,390 | 35,375 | −257 | 4,330 | 0.37 |
| 2020 | 65,745 | 1,042 | 959 | 28,112 | 48,908 | 35,632 | 10,294 | 14,836 | 0.57 |
| 2021 | 90,352 | 3,007 | 1,746 | 47,461 | 47,075 | 38,139 | 34,153 | 38,525 | 1.01 |
| 2022 | 145,861 | 4,133 | 1,352 | 82,710 | 44,170 | 57,666 | **92,105** | 96,207 | 1.87 |
| 2023 | 86,000 | 3,650 | 1,032 | 93,429 | 40,484 | **−12,111** | 37,074 | 40,834 | 2.31 |
| 2024 | 93,872 | 2,275 | 789 | 89,212 | 48,168 | 1,597 | 38,168 | 42,641 | 1.85 |
| 2025 | 99,864 | 2,387 | 491 | 45,636 | 59,259 | 51,350 | 32,223 | 37,727 | 0.77 |
| TTM 2026-06 | 109,619 | 3,147 | 539 | 45,195 | 62,850 | 60,738 | 37,246 | 43,083 | 0.72 |

*(TTM = FY2025 + H1 2026 − H1 2025, from the Q2 2026 consolidated report, which is an **"English Translation of Consolidated Financial
Statements Originally Issued in Chinese"** under Taiwan-IFRS, not the 20-F's IASB IFRS; displayed only.)*

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25, E4-38]:**

| window | OE, capex end | OE, judged end | D&A end (INVALID, display) |
|---|---|---|---|
| **5-yr 2021-2025 (the default [E2-42])** | **27,328** | **46,745** | 51,187 |
| 10-yr 2016-2025 | 21,904 | 21,904 | 26,497 |
| 3-yr 2023-2025 | 13,612 | 35,822 | 40,401 |
| prior 5-yr 2016-2020 | 16,480 | −2,937 | 1,807 |
| TTM to 2026-06-30 (display; one year is not [E2-23]'s "average annual amount") | 60,738 | 37,246 | 43,083 |

- **Combined range, valid windows × valid ends: NT$13.6bn to NT$46.7bn a year** (3-yr capex end to 5-yr judged end), **NT$27-47bn on the
  five-year default. The width is 3.4×.** *(The 10-year window's two ends coincide because the judged ratio is taken from that decade.)*
- **Is the range too wide to reach a conclusion?** **As a level, yes, very nearly [E4-25].** For the only decision it feeds, no: every valid
  construction yields under 3.1% on the cap ex-stakes (Q5).
- **The distorted years, named [E5-11, E4-41]:** **2022** (the shortage: ASP +21.3%, judged-end OE NT$92.1bn, twice any other year); **2016 and
  2023** (the capex peaks: capex-end OE −NT$37.9bn and −NT$12.1bn); **2018-2019** (capex below a third of depreciation flatters the capex end).
  [E4-41] says normalise the mean down for luck: **the five-year default contains 2022**; without it the four-year judged-end mean is
  NT$35.4bn.
- **Growth record, for Q5:** revenue 5.1% a year 2015-2025 (NT$); owner earnings show no trend that survives the window choice.

### Great, good, or gruesome? **[E4-20]**
- [ ] great · [ ] good · [x] **gruesome, at its border with good**
- **Evidence:** ten-year mean owner earnings NT$21.9bn against average parent equity of about NT$271bn is **about 8%** on the capital in the
  business, with the prior five years near zero at the judged end, while equity rose NT$153bn and capex repeatedly ran at 1.6-2.3×
  depreciation. It *"pays an inadequate interest rate and requires you to keep adding money"*. **The border, stated:** on the 2021-2025
  judged end the rate is about 14% (NT$46.7bn on ~NT$332bn), which is [E4-43]'s "good" class, and that window contains the shortage year.
  **The class depends on the window, which is itself [E4-25]'s answer.**

### Staying power — score all three **[E5-11]**
- **(1) A large and reliable stream of earnings: NO on reliability.** Operating cash is steady (NT$46-146bn, never negative), but owner earnings
  turned negative in 2016 and 2023 at the capex end.
- **(2) Massive liquid assets: YES.** At 2025-12-31: cash NT$110.7bn, current amortised-cost assets NT$12.5bn, current FVTPL NT$0.6bn; debt
  (short-term loans 8.4, current long-term 19.2, bonds 34.1, long-term loans 11.3) NT$73.0bn: **net cash about NT$50.8bn**, before the 2026
  convertible proceeds (NT$16.9bn). **Plus the quoted stakes, about NT$231bn at 2026-09-11 quotes**, larger than all debt three times over.
- **(3) No significant near-term cash requirements: MODERATE, AND COVERED.** 20-F Item 5.F: *"the total contractual cash obligations ... are
  NT$193,028 million (US$6,153 million), among which NT$86,811 million (US$2,767 million) will be due within one year"*; 2026 capex guided
  *"US$2 billion"* (~NT$63bn at 31.638); the 2026 dividend NT$32.7bn (paid). **Against net cash, NT$100bn of operating cash and NT$231bn of
  quoted stakes, covered.** Customer capacity deposits of NT$39.8bn are refundable liabilities in that table.
- **Leverage, named and quantified [E4-16, E2-54]:** net cash; interest paid NT$1.0bn in 2025 against operating cash less net capex of
  ~NT$54bn: **about 50× coverage**. Bonds are plain NT$ unsecured (e.g. *"five-year domestic unsecured corporate bond ... 1.99%"*); a 2020
  covenant breach at USCXM was waived (*"USCXM ... failed to comply with the loan covenant ... The waiver has been obtained as of April 21,
  2021"*, 20-F FY2020). **The 2026 convertibles add up to about NT$74bn of zero-coupon, equity-settleable claims.**

### Name the specific way THIS business dies **[E2-27, E3-24]** — exposure, not experience **[E4-40]**
**1. THE PASS-THROUGH (the eleventh registered shape, TM, 2026-09-13), in its sharpest form yet: the competitor's capacity is not
return-seeking.**
- **Mechanism:** a business that must spend to hold its place (*"To maintain competitiveness at the same capacity, we are required to make
  adequate investments"*), in an industry where each round of spending is individually rational and collectively neutralising [E2-27], and
  whose gains pass to customers [E3-62] (the ASP fell in seven of eleven years). **What sharpens it at UMC:** the capacity setting the price
  is built by competitors that report capex near 90% of revenue (SMIC) and earn 12% gross margins at 106% utilisation (Hua Hong), in a
  country whose policy GlobalFoundries' 20-F describes as *"Strong government support in China for their domestic capacity expansion"*.
  **It does not die of insolvency; the owner's return dies.** It is not a new shape.
- **Quantified from filed figures:** **2024-2025 itself (ASP −10.1% in two years)** took gross margin from 34.9% (2023) to 29.0% (2025) on UMC's own
  filing; **a repeat of 2016-2019 (ASP −12.9% over five years at full fabs)** at today's depreciation (NT$56.4bn, 23.8% of
  revenue) would put gross margin back toward the **14.4-18.1%** of 2017-2019 and ROE toward **4%**. On the owner-earnings table, the
  2016-2020 judged-end mean was **−NT$2.9bn a year**.
- **Likelihood: [x] likely** (as a slow compression of return through the next glut; the Chinese capacity is filed, built and rising).

**2. THE ADDRESS (the twelfth registered shape, TSM, 2026-09-13) — present, and less concentrated than at TSMC.**
- **Filed exposure:** capacity (Item 4 fab table, 2025, 12-inch equivalents) **Taiwan 3,219k (62.3%), China 789k (15.3%)**, Singapore 684k
  (13.2%), Japan 471k (9.1%). **77.6% of capacity sits in the two jurisdictions of the cross-strait dispute**; 22.4% (Singapore and Japan)
  outside it, against TSMC's ~20% of noncurrent assets outside Taiwan. The 20-F risk factors name *"geopolitical conflicts, including
  political relationships between U.S., China and Taiwan"*.
- **Likelihood: NOT STATABLE FROM ANY DOCUMENT**, for the reason recorded at TSM: no filing, corpus passage or nameable document assigns a
  probability to a cross-strait conflict. **Can I name the document that would resolve it? No.**

**3. THE PARTNER — Intel 12nm.** The collaboration is terminable on *"failure to achieve certain business or operational milestones"* and
*"certain change of control transactions"*; production is expected in 2027. **Quantified:** no revenue, investment or commitment amount is
filed; the exposure is to the 22nm-to-12nm migration path, not to the balance sheet. **A real possibility of failure; a low-level possibility
of mattering to survival.**

**4. THE DOLLAR.** 2025 gross margin fell partly on *"a 2.9% appreciation of the NTD"*; hedges US$22 million. **A likely source of volatility;
a low-level possibility of mattering to survival.**

**THE SURVIVAL SHAPE: THE PASS-THROUGH (registered, eleventh), with THE ADDRESS (registered, twelfth) as the unquantifiable second. No new
shape; the register stays at twelve.** Checked against all twelve: ORCL (contracted not to stop) no; ARM (pay eats the cash) no, SBC ~1% of
operating cash; BE/RGTI (too little history) no; BA (cash undoes past work) no, though the Micron settlement and fines were such cash in
2020-2021; SWK (distribution by selling the business) no; ACVA/FLNC/NEGG (the borrowed balance sheet) no, customer deposits are in financing
and covered; CNR (long tail) no; BAM (warehouse) no; SONY/HMC (camouflage) no, the investee income is disclosed, not hidden; **TM (the
pass-through) yes**; **TSM (the address) yes, secondary**.

- **VERDICT (RECORDED, NOT GOVERNING): [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [x] UNKNOWABLE** → *on mechanism 2 (the address: named and quantified,
  likelihood unstatable from any document), exactly as at TSM, and with the owner-earnings range (3.4×) and the great/good/gruesome class both
  turning on the window [E4-25]. On mechanism 1 alone the company survives and the owner's return is compressed, likely. Survival of the
  company is not in doubt on any filed balance-sheet measure.*

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 is OUT (and Q3, recorded, would be OUT; Q4, recorded, UNKNOWABLE). What follows is the
arithmetic the queue's output contract requires, headed as operator rule 3 requires.

---
## Q5 — **COMPUTATION — NOT A CLEARANCE**

**This section contains no entry language and confers no clearance. It is arithmetic.**

**The floor first [E4-28]:** *"that's the figure we quit on ... we don't want to buy equities where our real expectancy is below 10 percent.
Now, that's true whether short rates are 6 percent or whether short rates are 1 percent."* **The floor governs above both sovereigns.**

**The cap, and what it contains.** Cap **NT$1,761.8bn** (TWSE NT$140.5 × 12,539,542,899). **The nine quoted stakes (~NT$230.7bn, Step 0) are
separable and are priced at market, so the operating business is being bought for about NT$1,531.1bn (NT$122.1 a share); the stakes are
NT$18.4 a share.** Owner earnings exclude the stakes' dividends (Q4), so yields are shown on the ex-stakes figure.

**1. THE YIELD** (`q5.py` / `q5_out.json`):

| construction | OE NT$bn | yield on full cap | **yield ex-stakes** | vs TWD 30-yr 1.89% | vs USD 30-yr 5.35% | perpetual growth needed for 10% |
|---|---|---|---|---|---|---|
| 10-yr (both ends) | 21.9 | 1.24% | **1.43%** | −0.46 | −3.92 | 8.4% |
| **5-yr capex end** | **27.3** | 1.55% | **1.78%** | −0.10 | −3.57 | **8.1%** |
| **5-yr judged end** | **46.7** | 2.65% | **3.05%** | +1.17 | −2.30 | **6.7%** |
| 3-yr capex end | 13.6 | 0.77% | 0.89% | −1.00 | −4.46 | 9.0% |
| 3-yr judged end | 35.8 | 2.03% | 2.34% | +0.45 | −3.01 | 7.5% |
| TTM capex end (display) | 60.7 | 3.45% | 3.97% | +2.08 | −1.38 | 5.8% |
| TTM judged end (display) | 37.2 | 2.11% | 2.43% | +0.55 | −2.92 | 7.4% |
| 5-yr D&A end (INVALID, display) | 51.2 | 2.91% | 3.34% | +1.46 | −2.01 | 6.4% |

- **On the look-through share count** (reciprocal holdings deducted, Step 0) every yield is ~2% higher in proportion; **on the fully converted
  count** after the 2026 convertibles, ~4% lower. Neither moves a verdict.
- **Every valid construction yields between 0.9% and 3.1% ex-stakes: below or near the Taiwan 30-year bond, 2.3-4.5 points below the US bond.**

**2. WHAT THE PRICE ALREADY ASSUMES**
- **Perpetual growth needed to reach 10%: 6.7-9.0% a year** on the valid multi-year bases. In a staged engine (ten years of growth, then 3%,
  discounted at 10%; it casts no vote [E3-34]), the price needs **decade growth of 13.8% a year from the five-year judged end, 21.1% from the
  five-year capex end, 24.1% from the ten-year mean**, and **10.3% even from the best trailing twelve months at the capex end**.
- **What the business has actually done:** revenue **+5.1% a year** 2015-2025 (NT$); owner earnings with no trend that survives the window;
  ASP index 2014 = 100 → 117.0 in 2025. **[E4-35]:** *"fewer than 10 of the 200 most profitable companies ... will attain 15% annual growth in
  earnings-per-share over the next 20 years."*
- **In words: at NT$140.5 the buyer is paying NT$18 a share for listed stakes worth that at today's quotes (most of it Unimicron at NT$977),
  and about NT$122 a share for a mature-node foundry whose owner earnings would have to compound at roughly 14-24% a year for a decade from any
  multi-year base, in a business whose price has fallen in seven of the last eleven years and whose Chinese competitors added half again
  their capacity in three.** The price was NT$47.20 at the December 2025 RSA measurement date; the market has capitalised the 2026 upturn
  (utilisation 85% → 90%+ guided, ASP up) as if it were the new level.

**3. WHAT YOU ARE PAID**
- **Points over the sovereign: −1.0 to +1.2 against the TWD bond on the valid means (−2.3 to −4.5 against the USD bond).**

### THE PRICE — THE VALUE AS A ROUND-NUMBER RANGE [E4-01]
- **At the ~10% floor, stakes included at market, on the valid multi-year bases with 0-10% growth for ten years: roughly NT$30-110 a share**
  (10-yr: 39 / 48 / 62; 5-yr capex end: 44 / 56 / 72; 5-yr judged end: 62 / 82 / 111; 3-yr judged end: 52 / 67 / 89). **From the best trailing
  year at the capex end with 10% growth: ~NT$140.**
- **Current price NT$140.5 (TWSE, 2026-09-11). Above the entire range built on any multi-year window**; reached only by the single best trailing
  twelve months compounding 10% a year for a decade.
- **Screamer test [E4-01], for the record only:** the price is not below the conservative case; it is **3-4× the conservative cases**. **Windage
  count: one** (the capex-end (c); the growth cases are shown, not haircut; the discount rate is the floor, not a premium [E3-42]).
- **Verdict line: the file is closed at Q2; the price would also fail the floor.** No ranking position.

## Q6 — **COMPUTATION — NOT A CLEARANCE.** WHAT WOULD PROVE THIS FILE WRONG, PRE-COMMITTED [E1-02]
**No holding exists and nothing is armed.** Conditions under which a later run should reopen, set before any price moves them **[E1-02]**:
- **Reopen Q2 [E2-44] only on a full cycle of filed pricing:** the 20-F reporting a flat-or-rising ASP in a year when utilisation is below ~80%,
  **and** again in the next downturn, with gross margin holding above ~30%. One upturn year (2026) is not the test; the test is the trough.
- **Reopen Q2 [E3-03] on customers' filings:** a named customer (Himax, Lattice, Allegro, AMD) describing UMC as its sole qualified source at a
  node, or dropping alternatives it lists today.
- **Monitor the attacker [E4-32, E4-55]:** SMIC's and Hua Hong's year-end monthly capacity (1,059k and 486k 8-inch equivalents at end-2025) and
  gross margins (21.0% and 11.8%); a Chinese capacity build that stops, with their gross margins rising above UMC's, would change the [E2-58]
  reading. UMC's own shipment series (3,870k 12-inch equivalents in 2025, still 12% below 2022) is the unit check.
- **Q3 would need a written operator ruling on scope** (corporate plea and conviction against [E5-16]) before any future run scores the binary
  differently; **and** a filed disclosure of the 2026 buyback's economics and the RSA performance metrics.
- **Q4 would move off UNKNOWABLE** only with a document bearing on the address itself, or a capacity split materially outside Taiwan and China
  (Singapore P3 and P4, Japan, the Intel 12nm platform in the US) exceeding half of capacity.
- **The price condition, for orientation only:** the multi-year floor range sits around NT$30-110 a share; a price inside it would still meet a
  closed Q2. **Price appreciation and holding period are rejected as reasons [E2-28].**

- **VERDICT: NOT OPENED — no holding exists.**

---
## SELF-AUDIT (operator rule 6)
- [x] Questions answered in order; the file stopped at Q2 (OUT); Q3-Q6 recorded under explicit banners.
- [x] No question marked IN carries an "unverified" or "provisional" caveat. **Q1 IN** rests on the filed tables. No recorded gate is marked IN.
- [x] No UNRESEARCHED verdict issued. Competitor gaps (Vanguard: company rung HTTP 403; Samsung: not disclosed) stated as limits that cannot
  change the Q2 direction, with the reason.
- [x] The UNKNOWABLE verdict (Q4, recorded) states what cannot be known: the likelihood of a cross-strait conflict, and a level of owner
  earnings that depends on the window.
- [x] Step 0: the 20-F read with accession `0001193125-26-193757`; 2024 operating cash cross-checked to `companyfacts`; a tag/filing
  disagreement on depreciation found and resolved toward the filing.
- [x] Owner earnings on multi-year means (5-yr default, 10-yr, 3-yr, prior 5-yr), both (c) ends, D&A end INVALID under [E5-20], SBC resolved
  and complete (and checked at grant-date value), dividends received stripped because the stakes are valued at market, TSMC's prepayment
  strip shown not to apply (deposits in financing).
- [x] Competitor row: six peers with figures on the same metric and window (TSMC, GFS, Tower, SMIC, Hua Hong on gross margin; Intel Foundry on
  operating margin); non-SEC figures from the companies' own releases and HKEX, each cited.
- [x] Sovereign for the earnings currency: TWD, issuing authority's auction (CBC for the MOF, 2026-05-26) and the official exchange curve (TPEx,
  2026-09-11), 30-year, re-fetched; USD shown beside it. **Not added to `tools/sources.py`.**
- [x] Value as a round-number range; one bar (screamer, for the record) with windage count one.
- [x] Prices dated; Yahoo used for live quotes only and flagged; FX from the CBC; the stakes valued from their own quotes, flagged.
- [x] Every ledger id cited was checked against `principle_ledger.csv` before use (78 ids, all present).
- [x] Run committed to git by pathspec after each section.

**Errors of my own caught before commit, recorded:**
1. **I first wrote "Fab 8N Suzuki"**; the 20-F says Suzhou. Corrected before the Q1 commit.
2. **I first wrote in Q2's counter-case that UMC's margin was "twice SMIC's".** 29.0% against 21.0% is eight points, not double; corrected before
   the Q2 commit (Hua Hong's 11.8% is more than half, so "more than twice Hua Hong's" stands).
3. **I first wrote that UMC's price fell "four times in eleven years"**; the filed record is seven of eleven. Corrected before the Q2 commit.
4. **I first wrote that the low-capex years 2018-2020 were years revenue did not grow**; 2020 revenue grew 19.3%. Narrowed to 2018-2019 and
   corrected in the committed run file with this section's commit.
5. **My first TPEx call used the TSM run's recorded path and got HTTP 404**; the working path is recorded at Step 0 (a method defect in the
   precedent, not in the rate).
6. **One `fts_count` call (GFS, "UMC") returned HTTP 500**; recorded as an error, not as a zero.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business, at Q2)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** UMC is a mature-node foundry that runs its commodity better than its peers (best mature-node gross margin in the row every year
  2021-2025) and fails Q2 on the franchise definition itself: its customers' own filings name the substitutes, its own 20-F calls its price
  "comparable", and its filed ASP fell in seven of eleven years, including five straight at 89-97% utilisation and −10% in 2024-2025 while
  SMIC and Hua Hong added 49% to their capacity; recorded beneath the close, Q3 would be OUT on the company's 2020 US guilty plea and 2022
  Taiwan conviction for trade-secret offences (scope flagged), Q4 UNKNOWABLE on THE ADDRESS with THE PASS-THROUGH the likely death of the
  owner's return, and the price (NT$140.5, NT$122 ex-stakes) sits above every multi-year floor range.


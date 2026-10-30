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

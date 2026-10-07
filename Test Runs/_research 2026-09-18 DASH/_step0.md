## STEP 0: THE SKIP REASON, THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

Run unattended from scratch on 2026-09-18 (night, EDT); the template was copied and committed before any fetch (`e30b2f8`).
**This is a NEW NAME, not a holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.** WAVE 5, the second name in the
"no share count from dei: read the cover" row (META was the first). Research, scripts and downloaded filings are in
`Test Runs/_research 2026-09-18 DASH/`. **No DASH row exists in `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`**
(grepped: zero hits), so there is no screen row to carry. Every figure below is from DoorDash's own filings, fetched by this
run, with the accession.

### The entity, in every year used
CIK 0001792789, `submissions.json` (fetched by this run): *"DoorDash, Inc."*, SIC *"Services-Business Services, NEC"*,
`fiscalYearEnd` 1231 (correct: every 10-K reports a December 31 year end), one former name (*"DoorDash Inc"*, 2020-02-13 to
2021-02-24, a punctuation change). SEC `company_tickers.json`: *"{'cik_str': 1792789, 'ticker': 'DASH', 'title': 'DoorDash,
Inc.'}"*. One reporting entity throughout; IPO 2020-12-09 (*"33,000,000 shares of Class A common stock at the public offering
price of $102 per share"*, FY2022 10-K), so FY2020 is the first public year and FY2018-19 are pre-IPO figures carried in the
S-1-era comparatives. No shell, no reverse recapitalization (the DJT check does not apply).

**`submissions.json` gives `stateOfIncorporation` "NV", while every filing through the Q2 2026 10-Q says Delaware.** Both are
right: the 8-K of **2026-09-18** (accession `0001140361-26-037109`, Item 8.01): *"the reincorporation of the Company from the
State of Delaware to the State of Nevada (the " Nevada Reincorporation ") became effective on September 18, 2026, at 12:02 a.m.
Pacific Time"*, and *"the affairs of the Company ceased to be governed by the laws of the State of Delaware"*. It was approved
not at a meeting but by written consent of the founders and their trusts (8-K of 2026-08-11, `0001140361-26-032235`, Item 5.07:
*"certain stockholders ... holding at least a majority of the voting power ... adopted resolutions by written consent in lieu of
a meeting of stockholders"*; the Consenting Stockholders are Tony Xu, Andy Fang, Stanley Tang and their trusts), with an
information statement on Schedule 14C (DEF 14C, 2026-08-27, `0001140361-26-034688`). **The run is of the same company; the
charter that governs the share classes from today is the Nevada articles (Appendix C of the DEF 14C), read below. The
governance meaning is carried at Q3.**

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"no share count from dei: read the cover."* **A prompt to read, never a verdict.** The probe (`_probe_screen.py`,
copied from META's with the CIK changed; output `_probe_screen_output.txt`) shows companyfacts carries **one** dei element for
DoorDash, `EntityPublicFloat` (six facts, FY2021-25 10-Ks and the 10-K/A), and **no `EntityCommonStockSharesOutstanding` at
all**; `share_count_shift` returned **None** under both the current screen and the `a8bc84f` code (not measured, not stable: the
RIVN reading) and `shares_outstanding` returned None. **The META note's hypothesis (a dimensioned per-class cover) was tested on
the inline XBRL** of three filings (`dei.py`; raw documents `10Q_2026Q2_raw.htm`, `10K_FY2025_raw.htm`, `10KA_FY2025_raw.htm`),
and it holds, with one difference from META: **three classes, not two**. In the Q2 2026 10-Q (`0001792789-26-000050`):

- *"name="dei:EntityCommonStockSharesOutstanding" ... 408,992,917"* in context c-2, segment *"dimension="us-gaap:StatementClassOfStockAxis">us-gaap:CommonClassAMember"*, instant 2026-07-30;
- the same element in context c-3, *"us-gaap:CommonClassBMember"*, **24,302,737**;
- the same element in context c-4, *"us-gaap:CommonClassCMember"*, value tagged `format="ixt:fixed-zero"` over the word **"no"**.

The FY2025 10-K (`0001792789-26-000013`) and its 10-K/A (`0001792789-26-000035`) tag the same three dimensioned facts at
2026-02-12 (409,966,858 A; 24,459,494 B; zero C). **companyfacts publishes only undimensioned facts, so a cover tagged per class
never reaches it. For DASH the label was the META kind: a tagging convention for a multi-class cover (here three classes, one of
them empty), not a missing or stale count.** The other `a8bc84f` guards on facts filed by 2026-09-01: `scale_shift` **1.694**
(did not fire); `restatement_shift` (1.0, FY2019), a null and not a guard (the SNOW note). The `a8bc84f` `owner_earnings()`
priced the name (`{'5y_da': 68.0M, '5y_capex': 378.6M, '3y_da': 393.7M, '3y_capex': 838.0M}`), so **the count was the only
thing that stopped it.** The current screen prices it lower at the capex end (`5y_capex` 168.0M, `3y_capex` 579.7M) because it
now reads capitalised software as capital; that is not a verdict and is rebuilt from the filed statements at Q4.

**Restatement check:** the **10-K/A of 2026-05-06** exists and was read: *"We are filing this Amendment to correct a clerical
error in the report of KPMG LLP ("KPMG"), our independent registered public accounting firm"*; both covers leave the
error-correction box unticked (*"reflect the correction of an error to previously issued financial statements. ☐"*). No 10-Q/A
in the recent index. **No restatement of the business's figures exists.**

**One tag defect found and carried:** the current screen's `acquisition_flag` reports *"NET CASH INFLOW on the acquisition line
($4,222M ...)"* for FY2025, but the filed face reads *"Acquisitions, net of cash acquired | — | — | ( 4,151 )"* (FY2025 10-K).
The flag reads a sign or an element the face does not carry; the face is used. (Recorded under TOOLING NOTES.)

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by this run
  at 23:07 EDT (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned **(5.29, '09/17/2026')** a second later (`step0_out.txt`): the stale-cache defect
  again (META recorded its seventh occurrence; this is the eighth recorded). The issuing-authority figure is used. FRED not
  used. Struck by this run, not inherited from the brief or from META.
- **Earnings currency: USD, with a growing foreign share.** The company reports in dollars; Wolt (from 2022-05-31) and Deliveroo
  (from 2025-10-02) earn in euros, sterling and other currencies (the geography split is read at Q1). No ADR or FX conversion of
  the quote applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$192.94, the close of 2026-09-18** (Friday). Source: Yahoo Finance chart via `sources._chart("DASH", rng="1mo",
  max_age_h=0)` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`): `regularMarketPrice` 192.94,
  `regularMarketTime` 1789761601 = **16:00:01 EDT**, the closing print; the day's bar closes at 192.94 (range $192.35-$196.01).
  `tools/sources.price()` returned the same 192.94 stamped 2026-09-18.
- **The month, recorded rather than choosing a day:** 08-19 $220.22 · 08-26 $236.93 (the month's high close) · 09-01 $225.66 ·
  09-04 $211.73 · 09-08 $200.44 · 09-11 $201.95 · 09-17 $194.56 · 09-18 $192.94. **-19% from the 08-26 close.** The Q2 2026
  10-Q gives *"the closing price of the Company's Class A common stock of $ 184.53 on the last trading day of the quarter"*.
- **Primary-filing cross-check (Form 4s, `f4.py`, `form4_table.txt`):** Andy Fang sold on 2026-09-01 at $225.754-$232.231 in
  seven lots (`0001832390-26-000023`), inside Yahoo's 09-01 range ($225.26-$232.87); Stanley Tang sold on 2026-09-02 at
  $223.601-$227.229 (`0001832614-26-000032`), inside $222.11-$227.58; Gordon Lee sold 413 shares on 2026-09-04 at **$221.50**
  (`0001635648-26-000016`), inside $211.18-$222.05. **The aggregator's series is corroborated on three dates (inside the day's
  range; these are sales, not withholding at the close). No Form 4 exists for 2026-09-18.**
- **Split factor after the count's date (2026-07-30): 1.0.** `close` used, never `adjclose`.

### The share count: from the cover, with the accession, and the class treatment from the charter
- **Class A 408,992,917 + Class B 24,302,737 + Class C 0 = 433,295,654 shares**, from the cover of the **Form 10-Q for the
  quarter ended 2026-06-30, filed 2026-08-05, accession `0001792789-26-000050`**, the latest periodic filing: *"The registrant
  had outstanding 408,992,917 shares of Class A common stock, 24,302,737 shares of Class B common stock, and no shares of Class
  C common stock as of July 30, 2026."*
- **Cross-check against the filed balance sheet (rule 4):** the same 10-Q's face: *"408,925 Class A shares issued and outstanding
  as of ... June 30, 2026"* and *"24,331 Class B shares"* (thousands); the cover moves +68K A and -28K B in thirty days (B
  converting to A on founders' sales, above). The equity statement: *"Balances as of June 30, 2026 | $ | 11 | 433,256"*
  (thousand shares, all classes), against 433,296K on the cover. **Consistent.**
- **Why the classes are added, one for one.** The governing charter from 2026-09-18 is the Nevada Articles of Incorporation
  (DEF 14C Appendix C): *"2. Identical Rights . Except as otherwise provided in these Articles of Incorporation or required by
  applicable law, shares of Common Stock shall have the same designations, limitations, restrictions and relative rights
  (including as to dividends and other distributions, and any liquidation, dissolution or winding up of the Corporation but
  excluding voting and other matters as described in Section V.3 below), share ratably and be identical in all respects as to
  all matters"*; dividends *"paid pro rata, on an equal priority, pari passu basis"* (2.1) and liquidation *"distributed on an
  equal priority, pro rata basis to the holders of Common Stock"* (4), each unless the adversely treated class approves
  otherwise by separate class vote; splits must apply to all classes alike (2.3). Conversion: *"Each share of Class B Common
  Stock will automatically convert into one fully paid and nonassessable share of Class A Common Stock on the Final Conversion
  Date"* (5.1), and on any transfer to a non-Permitted Transferee (5.2(b)). The Delaware certificate it replaced carried the
  same clause (*"shall have the same rights and powers, rank equally ... share ratably and be identical in all respects"*,
  DEF 14C Appendix E, the Delaware certificate reproduced there, page E-5 onward). The one difference is votes: *"(a) Class A ... one vote"*,
  *"(b) Class B ... twenty votes"*, *"(c) Class C ... no voting rights"* (3.1). **Economically identical, so the cash-flow
  claim is the sum; the votes belong at Q3 (control), not in the count.**
- **Sold after the cover date: nothing found.** No equity offering, S-3 or 424B in the index after 2026-07-30; post-cover Form
  4s are founders' and officers' sales of existing shares (above). Buybacks: 6.8M shares at $155.25 in H1 2026 ($1.0bn),
  retired (10-Q Note 11), before the cover date.
- **Dilution not in the count:** **26,732 thousand unvested RSUs** at 2026-06-30 (including the CEO Performance Award's
  9,341,100 eligible PSUs) and 2,067 thousand options at a weighted $7.10 (10-Q Note 11): 6.6% of the cover count. The 2030
  convertible notes ($2.75bn, conversion price about $291.97, principal settled in cash) are out of the money, hedged to
  $291.97 and capped by warrants struck at $512.225 (about 9.4M shares each side). Shown beside the cap, not in it.

### The market cap
**$192.94 x 433,295,654 = US$83.60bn** (Class A $78.91bn; Class B at the Class A price, $4.69bn, which the charter's
identical-rights clause licenses). **With unvested RSUs and options: $89.16bn.** Split factor 1.0. Public float on the FY2025
10-K cover: $90.8bn at 2025-06-30 (companyfacts, the one dei element).

### THE DEAL CHECK: none live on the registrant as target
`sources.deal_filings("0001792789")` returned `([], [], '2026-02-18')` and `deal_note` returned empty (`step0_out.txt`). Read on
the recent submissions index (2022-04 to 2026-09): the only 425s are of **May 2022**, the Wolt stock acquisition (closed
2022-05-31); **no 425, SC TO, SC 13E-3, DEFM14A, PREM14A or SC 13D on this registrant since.** The Deliveroo offer ran under the
UK Takeover Code (8-Ks of 2025-05-06, `0001140361-25-017438`, and 2025-10-02, `0001140361-25-037039`), with DoorDash as buyer.
The one corporate action live today is the Nevada conversion, completed. **The quote is not a spread and buys this company.**

### The perimeter: what (c), the five-year mean and the cap must see
- **Wolt Enterprises Oy, closed 2022-05-31, paid in stock:** *"on May 31, 2022, the Company acquired Wolt Enterprises Oy (Wolt)
  in a business combination for $2,838 million"* (FY2022 10-K, auditor's critical audit matter); the cash-flow face shows *"Net
  cash acquired (used) in acquisitions | ( 28 ) | — | 71"* (FY2020/21/22), so the consideration was shares and never touched the
  cash-flow statement. **Inside every window from FY2022 on**; FY2021 is DoorDash alone.
- **SevenRooms, closed 2025-06-13, for cash:** *"Cash | $ | 902 | Deferred cash consideration | 250 | Total consideration | $ |
  1,152"*; goodwill $886M; revenue since acquisition *"not material"* (FY2025 10-K Note 4).
- **Deliveroo plc, closed 2025-10-02, for cash:** *"the Company acquired Deliveroo plc (Deliveroo) in a business combination for
  $3,724 million"*; *"eligible Deliveroo shareholders were entitled to receive 180 pence in cash for each Deliveroo share held"*
  (8-K 2025-10-02); goodwill $1,950M, intangibles $1,498M (lives 2-11 years), contingent liabilities $102M *"relate to
  outstanding legal provisions"*; revenue and net loss since acquisition *"$ 347 million and $ 49 million"*; pro forma FY2024
  revenue $11,984M against the reported $10,722M, FY2025 $14,743M against $13,717M (FY2025 10-K Note 4). Funded from cash and
  the **$2.75bn 0% Convertible Senior Notes due 2030** (May 2025; *"Proceeds from issuance of convertible notes, net of issuance
  costs | ... | 2,720"*), with a $680M note hedge and $341M of warrants. The face: *"Acquisitions, net of cash acquired | — | —
  | ( 4,151 )"* (FY2025).
- **HOW THE SPLICE IS HANDLED.** The five-year window FY2021-25 contains DoorDash alone (FY2021), DoorDash plus seven months of
  Wolt (FY2022), DoorDash plus Wolt (FY2023-24), and FY2025 with SevenRooms for 6.5 months and Deliveroo for one quarter. **No
  pro forma operating cash exists for any year** (the 10-K gives pro forma revenue and net income only; Deliveroo's own
  statements are filed in the UK, not with the SEC). So the run does **not** build a pro forma mean. It (i) computes owner
  earnings on the reported consolidated figures, (ii) charges the **cash** acquisitions ($4,151M in FY2025 plus the $20M
  deferred and later payments) in a separate column so the reader sees the mean with and without them (the SPGI and AEHR
  practice), (iii) records the Wolt stock consideration ($2,838M) as a share-count cost already inside the cover count, and
  (iv) reads H1 2026 (the first half-year with all three businesses inside) separately, because it is the only filed period
  that is not a splice.
- **Cash and liquidity at 2026-06-30** are read at Q4.

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2025 Form 10-K**, filed **2026-02-18**, accession **`0001792789-26-000013`** (`10K_FY2025.txt`), its **10-K/A** of
  2026-05-06 (`0001792789-26-000035`, the KPMG clerical correction), and the **Q2 2026 Form 10-Q**, filed **2026-08-05**,
  accession **`0001792789-26-000050`** (`10Q_2026Q2.txt`).
- Also read: the FY2022, FY2023 and FY2024 10-Ks (`0001628280-23-005131`, `0001628280-24-005600`, `0001628280-25-005715`); the
  Q3 2025 and Q1 2026 10-Qs (`0001792789-25-000020`, `0001792789-26-000037`); the DEF 14A of 2026-04-20
  (`0001792789-26-000018`); the DEF 14C of 2026-08-27 with the Nevada articles; the 8-Ks of 2025-05-06, 2025-05-27, 2025-05-28,
  2025-06-02, 2025-10-02, 2026-06-12, 2026-08-11 and 2026-09-18; the 8-K EX-99.1 earnings releases (listed at Q3); four Form 4s.
- **Figures cross-checked against the filed statement** (FY2025 10-K consolidated statement of cash flows, $M, FY2023/24/25):
  *"Net cash provided by operating activities | 1,673 | 2,132 | 2,431"*, *"Stock-based compensation | 1,088 | 1,099 | 1,051"*,
  *"Depreciation and amortization | 509 | 561 | 747"*, *"Purchases of property and equipment | ( 123 ) | ( 104 ) | ( 257 )"*
  and *"Capitalized software and website development costs | ( 201 ) | ( 226 ) | ( 348 )"* match companyfacts (`ocf`,
  `sbc_annual`, `da_annual`, `annual(CAPX_TAGS)`, and `capital_acquired` = the two capital lines summed: 324, 330, 605) to the
  million. The FY2022 10-K face (FY2020/21/22: operating cash 252, 692, 367; SBC 322, 486, 889) matches likewise. Revenue
  $8,635M / $10,722M / $13,717M matches.

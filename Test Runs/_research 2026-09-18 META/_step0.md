## STEP 0: THE SKIP REASON, THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

### The entity, in every year used
CIK 0001326801, `submissions.json` (fetched by this run): *"Meta Platforms, Inc."*, SIC *"Services-Computer Programming, Data
Processing, Etc."*, `fiscalYearEnd` 1231 (correct: every 10-K reports a December 31 year end), one former name (*"Facebook Inc"*,
2005-05-06 to 2021-10-27). SEC `company_tickers.json`: *"{'cik_str': 1326801, 'ticker': 'META', 'title': 'Meta Platforms,
Inc.'}"*. One Delaware corporation throughout (*"We were incorporated in Delaware in July 2004"*, FY2025 10-K Note 1); the 2021
rename changed no reporting key; no shell, no reverse recapitalization (the DJT check does not apply).

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"no share count from dei: read the cover."* **A prompt to read, never a verdict.** The brief-writer's probe
(`_probe_screen.py`, `_probe_screen_output.txt`, re-read by this run) shows companyfacts carries **one** dei element for Meta,
`EntityPublicFloat`, and no `EntityCommonStockSharesOutstanding` at all; `share_count_shift` therefore returned **None**, which is
"not measured", not "stable" (the RIVN reading). **The hypothesis (two share classes on the cover) was tested on the inline XBRL
of the latest 10-Q** (`dei.py`; the raw document `meta-20260630.htm`, accession `0001628280-26-050705`), and it holds exactly:
the cover tags the element twice, once per class, and **each fact carries a dimension**:

- *"name="dei:EntityCommonStockSharesOutstanding" ... 2,205,128,509"* in context c-2, whose segment is
  *"dimension="us-gaap:StatementClassOfStockAxis">us-gaap:CommonClassAMember"*, instant 2026-07-24;
- the same element in context c-3, segment *"us-gaap:CommonClassBMember"*, **342,377,716**.

companyfacts publishes only undimensioned facts, so a count tagged per class never reaches it. **So the label was, for META, a
tagging convention for a two-class cover: the count exists on every cover, split by class, and the screen could not see it.**
The other a8bc84f guards (probe output): `scale_shift` 1.372 (the largest one-year revenue step in the window, FY2020 to FY2021,
$86.0bn to $117.9bn, consecutive years; did not fire); `restatement_shift` (1.0, FY2017), a null and not a guard (the SNOW
note); no acquisition, working-capital, D&A, capex-funding or lease-capex flag fired. **No restatement exists:** no 10-K/A,
10-Q/A or NT filing in either submissions index read (2017-05 to 2026-09); the FY2025 10-K cover leaves the error-correction box
unticked (*"reflect the correction of an error to previously issued financial statements. ☐"*). **One presentation change was
found and is carried:** FY2023 capex is *"Purchases of property and equipment | ( 27,266 )"* beside *"Proceeds relating to
property and equipment | 221"* on the FY2023 10-K face and **27,045** (net) on the FY2025 10-K face; the FY2025 face is used for
FY2023-25 and the earlier faces for FY2017-22 (the proceeds line is $0.1-0.2bn a year).

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by this
  run at 22:03 EDT (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned **(5.29, '09/17/2026')** a second later (`step0_out.txt`): the stale-cache defect,
  reproduced a seventh time. The issuing-authority figure is used. FRED not used. Struck by this run, not inherited from AEHR (it
  agrees because it is the same day's print).
- **Earnings currency: USD.** The company reports in dollars; **62.8% of FY2025 revenue was billed to customers outside the
  United States** (US revenue *"$ 74.78 billion"* of $200,966M, FY2025 10-K Note 2), so the dollar result carries currency
  translation (FY2022: *"a $5.96 billion negative impact from the appreciation of the U.S. dollar"*, FY2022 10-K MD&A). No ADR
  or FX conversion of the quote applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$665.75, the close of 2026-09-18** (Friday). Source: Yahoo Finance chart via `sources._chart("META", rng="1mo",
  max_age_h=0)` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`): `regularMarketPrice` 665.75,
  `regularMarketTime` 1789761602 = 20:00:02 UTC = **16:00:02 EDT**, the closing print. The day's bar had not finalised (open
  686.82, high 690.15, low 660.80, close None: the BX and AEHR `close None` note again). `tools/sources.price()` returned the
  same 665.75 stamped 2026-09-18.
- **The month, recorded rather than choosing a day:** 08-19 $546.03 · 08-28 $578.02 · 09-02 $592.85 · 09-09 $653.69 · 09-15
  $670.24 · 09-17 $682.31 · 09-18 $665.75. **+22% in a month.**
- **Primary-filing cross-check (Form 4s, `f4.py`, `form4_table.txt`):** Christopher K. Cox sold 20,000 shares on 2026-09-15 at a
  weighted **$675.2278** (`0000950103-26-014140`), inside Yahoo's 09-15 range ($656.20-$678.87); Javier Olivan sold on
  2026-09-14 at **$657.73** (`0000950103-26-014061`), inside $649.22-$668.60; Cox on 2026-09-09 at $650.21 and $651.15
  (`0000950103-26-013860`), inside $638.56-$657.86. **The aggregator's series is corroborated on three dates (inside the day's
  range, not to the cent: these are sales, not withholding at the close); no Form 4 exists for 2026-09-18.**
- **Split factor after the count's date (2026-07-24): 1.0.** `close` used, never `adjclose`.

### The share count: from the cover, with the accession, and the A/B treatment from the charter
- **Class A 2,205,128,509 + Class B 342,377,716 = 2,547,506,225 shares**, from the cover of the **Form 10-Q for the quarter
  ended 2026-06-30, filed 2026-07-30, accession `0001628280-26-050705`**, the latest periodic filing: *"Class A Common Stock |
  $0.000006 par value | 2,205,128,509 | shares outstanding as of July 24, 2026 | Class B Common Stock | $0.000006 par value |
  342,377,716 | shares outstanding as of July 24, 2026"*. `Screens/cover_shares.py META` returns the same two figures and
  prints their sum as *"arithmetic sum, NOT a share count"*: **the addition is a judgment, made here from the charter.**
- **Why A and B are added, one for one.** The Amended and Restated Certificate of Incorporation (Exhibit 3.1 to the 10-Q filed
  2024-08-01, accession `0001326801-24-000069`, incorporated by reference in the FY2025 10-K exhibit list): *"3.1. Equal Status .
  Except as otherwise provided in this Restated Certificate of Incorporation or required by applicable law, shares of Class A
  Common Stock and Class B Common Stock shall have the same rights and powers, rank equally (including as to dividends and
  distributions, and upon any liquidation, dissolution or winding up of the corporation), share ratably and be identical in all
  respects and as to all matters."* Dividends *"shall be treated equally, identically and ratably, on a per share basis"* (3.3);
  liquidation *"entitled to receive ratably all assets"* (3.5); mergers *"made ratably on a per share basis among the holders of
  the Class A Common Stock and Class B Common Stock as a single class"* (3.6); each with a proviso allowing disparate treatment
  only with the disadvantaged class's separate approval. Conversion (Exhibit 4.6, Description of Capital Stock, 10-K filed
  2024-02-02, `0001326801-24-000012`): *"a share of Class B common stock may be converted at any time into one share of Class A
  common stock"*, and *"each share of Class B common stock will convert automatically into one share of Class A common stock upon
  any transfer"*, with limited exceptions. The one difference is votes: *"The holders of our Class B common stock are entitled to
  ten votes per share, and holders of our Class A common stock are entitled to one vote per share."* **The two classes are
  economically identical, so the cash-flow claim is the sum. The votes are not identical, and they belong at Q3 (control), not in
  the count.** The company counts them together too: basic EPS on 2,521M weighted shares FY2025, and *"Diluted EPS ... assumes
  the conversion of our Class B common stock to Class A common stock"* (10-Q Note 3).
- **Sold after the cover date: nothing found.** No equity offering: the S-3ASR of 2026-04-30 (`0001193125-26-194008`) carried a
  $25bn notes offering (8-K `0001193125-26-204128`, 2026-05-04: six tranches, 4.550% 2031 to 6.450% 2066); post-cover Form 4s
  are sales of existing shares. Buybacks were **zero** in H1 2026 (*"Repurchases of Class A common stock | — | ( 22,921 )"*, six
  months 2026/2025, 10-Q face).
- **Dilution not in the count:** **146,464 thousand unvested RSUs** at 2026-06-30 (5.7% of the cover count), and options on
  **20 million** Class A shares granted in H1 2026 at a weighted exercise price of **$2,788** (10-Q Note 10). Shown beside the
  cap, not in it (the cover is the rule).

### The market cap
**$665.75 x 2,547,506,225 = US$1,696.0bn** (Class A $1,468.1bn; Class B at the Class A price, $227.9bn, which the charter's
equal-status clause licenses). **With the unvested RSUs: $1,793.5bn.** The options are 4.2 times out of the money and are not
added. Split factor 1.0. Public float on the FY2025 10-K cover: *"approximately $ 1.6 trillion"* at 2025-06-30.

### THE DEAL CHECK: none live
`sources.deal_filings("0001326801")` returned `([], [], '2026-01-29')` and `deal_note` returned empty (`step0_out.txt`). Read on
both submissions indexes (2017-05 to 2026-09): **no 425, SC TO, SC 13E-3, DEFM14A, PREM14A or SC 13D filed on this registrant.**
The one S-4 (2022-11-15, `0000950103-22-019633`, effective 2022-11-23) followed the August 2022 notes offering (8-Ks of
2022-08-04 and 2022-08-09) and is not a business combination (no 425 or merger 8-K accompanies it). The 8-Ks filed since
2024-08 carry Items 2.02, 5.02, 5.03, 5.07 and 8.01 (the notes offerings of 2024-08, 2025-11 and 2026-05, and the 2025-12-12
notice of a derivative-suit settlement, read at Q3); **no Item 1.01 or 2.01.** **The quote is not a spread and buys this
company.**

### The perimeter: what (c) and the cap must see
- **Scale AI, a minority stake, 2025:** *"our minority investments in Scale AI for $ 13.80 billion, which was closed during 2025"*
  (FY2025 10-K Note 5), carried under the measurement alternative (*"We do not have significant influence over these investees'
  operations"*). Cash on the face: *"Purchases of non-marketable equity investments | ( 18,330 )"* FY2025 (Scale AI and others).
  Not consolidated; it contributes nothing to owner earnings and no look-through [E3-04] is possible (no investee earnings are
  filed). **Q4 carries the cash.**
- **The Louisiana data-centre Venture, October 2025, OFF the balance sheet:** *"At Venture formation, we contributed $ 4.30
  billion of held-for-sale assets, net of liabilities, and we received a one-time distribution of $ 2.55 billion. We hold a 20 %
  membership interest in the Venture, which is accounted for under the equity method ... The parties have committed to fund their
  respective pro rata share of approximately $ 27 billion in total estimated development costs."* Meta leases it back from 2029:
  *"The aggregate initial lease commitment is approximately $ 12.31 billion, with each property having an initial four-year lease
  term and options to renew for a total lease period of up to 20 years. In addition, we have provided residual value guarantees
  (RVG) with an aggregate threshold of approximately $ 28 billion"*; *"we are not the primary beneficiary and do not consolidate
  the variable interest entity (VIE). Our maximum exposure to loss related to the Venture was $ 45.95 billion as of December 31,
  2025"* (FY2025 10-K Note 5). (The filing calls it only "the Venture"; the name Hyperion appears in no filing read.) **A data
  centre built for Meta, managed by Meta, leased by Meta and guaranteed by Meta, 80% of whose construction cost does not pass
  through Meta's capex line.** Q4 carries it.
- **Leases not yet commenced and purchase commitments:** *"we have additional operating and finance leases, that have not yet
  commenced, with total lease obligations of approximately $ 103.77 billion, mostly for data centers, colocations, and network
  infrastructure"* (FY2025 10-K Note 7), and *"$ 131.05 billion of non-cancelable contractual commitments ... mostly related to
  third-party cloud capacity arrangements"* (Note 11). Both are read against the 2026-06-30 10-Q at Q4.
- **Acquisitions of businesses** are small on the face ($0.3-1.3bn a year FY2019-24, $4,231M in FY2025) and are shown in their
  own column at Q4.

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2025 Form 10-K**, filed **2026-01-29**, accession **`0001628280-26-003942`** (`10K_FY2025.txt`), and the **Q2 2026 Form
  10-Q**, filed **2026-07-30**, accession **`0001628280-26-050705`** (`10Q_2026Q2.txt`).
- Also read: the FY2019, FY2021, FY2022, FY2023 and FY2024 10-Ks (`0001326801-20-000013`, `-22-000018`, `-23-000013`,
  `-24-000012`, `-25-000017`) for the FY2017-24 statements, segment notes and the ad-price series; the Q3 2025 and Q1 2026 10-Qs
  (`0001628280-25-047240`, `0001628280-26-028526`); the DEF 14A of 2026-04-16 (`0001628280-26-025532`); the charter and the
  Description of Capital Stock (above); the 8-K EX-99.1 earnings releases for Q4 2021, Q4 2022, Q4 2023 and every quarter Q4
  2024 to Q2 2026; the 8-Ks of 2025-11-03, 2025-12-12 and 2026-05-04; five Form 4s filed 2026-09-08 to 2026-09-17.
- **Figures cross-checked against the filed statement** (FY2025 10-K consolidated statement of cash flows, $M, FY2025/24/23):
  *"Net cash provided by operating activities | 115,800 | 91,328 | 71,113"*, *"Share-based compensation | 20,427 | 16,690 |
  14,027"*, *"Depreciation and amortization | 18,616 | 15,498 | 11,178"*, *"Purchases of property and equipment | ( 69,691 ) |
  ( 37,256 ) | ( 27,045 )"* and *"Principal payments on finance leases | ( 2,524 ) | ( 1,969 ) | ( 1,058 )"* match
  companyfacts (the brief's tagged series) to the million, except FY2023 capex (tagged 27,266, the FY2023 10-K's gross figure,
  above) and FY2024 D&A (tagged 15,501, an earlier vintage, against 15,498 on the FY2025 face). Revenue *"$ 200,966 | $ 164,501 |
  $ 134,902"* matches.

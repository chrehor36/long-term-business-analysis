**Queue context.** A name in **WAVE 5** of `Screens/WATCHLIST RUN QUEUE.md` (the unpriced watchlist
businesses), the fourth of the eleven foreign 20-F filers to be run (after TM, SONY and HMC, which folded first). The
2026-09-01 triage skipped it as *"foreign 20-F filer ... several still return too few annual periods
because their XBRL history is short, not because the business is."* **Read here as UNLABELLED: a prompt
to read the 20-F by hand, not a verdict.** The run file was created before any fetch (write-early
protocol). Research on disk: `Test Runs/_research 2026-09-13 TSM/`.

**Why the screen could not price it, found rather than assumed.** `companyfacts` (fetched 2026-09-13)
carries `ifrs-full` annual facts for **FY2015 to FY2024** (ten periods in TWD, eight in USD) from eight
20-F accessions, **and nothing from the FY2025 20-F** (`0001628280-26-025362`, filed 2026-04-16).
`CashFlowsFromUsedInOperatingActivities` ends at 2024-12-31. The FY2025 20-F was filed under a
**different filing-agent prefix** (`0001628280`, against `0001193125` for FY2017-FY2024). **The history
is not short; the newest year is missing.** This is the fourth 20-F filer in a row (SONY, TM, HMC, TSM) where
the newest 20-F had not been ingested. This run reads FY2015-FY2025 from the filed 20-Fs.

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

**The functional and presentation currency is the NT dollar; substantially all revenue is in US dollars.**
Both are filed:
- 20-F FY2025, Note 4 (Foreign Currencies): *"The functional currency of TSMC and presentation currency of
  the consolidated financial statements are both New Taiwan Dollars (NT$)."*
- 20-F FY2025, Item 3.D risk factor: *"Substantially all of our sales are denominated in U.S. dollars and
  over half of our capital expenditures are denominated in currencies other than the NT dollar, primarily
  in U.S. dollars, Euros and Japanese yen ... every 1% depreciation of the U.S. dollar against the NT
  dollar would result in an approximately 0.3 percentage point decrease in our operating margin based on
  our 2025 results."*
- Item 5: *"weighted average exchange rates of the NT dollar per U.S. dollar appreciating from NT$ 32.13 in
  2024 to NT$ 31.11 in 2025."*
- Item 11: a 10% adverse FX move on monetary assets and liabilities would have cut 2025 net income by
  *"NT$ 1,987 million (US$ 63 million)"* after hedges. The balance sheet is hedged; **the exposure is the
  operating one** (US-dollar revenue against a largely NT$ domestic cost base, with over half of capex in
  foreign currencies).

**The judgment, and its ground.** The sovereign enters as *"the currently observed rate for the currency
the business earns in"* **[E4-15, E3-32]**. TSMC's revenue is invoiced in dollars; its books, its
functional currency, its dividend, its primary listing (TWSE 2330) and most of its operating cost base are
NT dollars. **The owner earnings below are computed in NT$ from the NT$ cash-flow statement and the cap is
priced in NT$ from the Taipei quote, so the TWD sovereign is the consistent pairing**; setting a USD rate
beside an NT$ yield is the ATLKY currency defect inverted. **The case for the USD sovereign is real and is
stated, not buried:** the cash is billed in dollars, the NT$ figure is a translation of dollar prices at the
year's rate, and **[E4-01]** itself names *"the yield on long-term U.S. bonds"* as the risk-free rate. The
two readings differ by **~3.2-3.5 points (TWD 1.9-2.2% against USD 5.35%)**, the widest sovereign gap in
the queue so far. **What the choice does NOT decide, stated so it cannot be leaned on later:** the
**[E4-28]** floor of roughly 10% does not move with the sovereign (*"that's true whether short rates are 6
percent or whether short rates are 1 percent"*), so the choice moves only the points-over-sovereign
display, never the quit-on line. **Both are shown at Q5; the floor governs above both.** The dollar
exposure is carried into Q4 as a named risk, never into the rate **[E3-42]**.

### Sovereign, for the currency the business EARNS in — the currently observed rate, never a forecast [E4-15, E3-32]

**No TWD source exists in `tools/sources.py` (USD, JPY, EUR only), and none was added** (a tool may remove
friction, never add a number). Fetched by hand, two rungs, both recorded:

| rung | what | tenor | yield | date | URL · saved file |
|---|---|---|---|---|---|
| **ISSUING AUTHORITY (auction)** | Central Bank of the Republic of China (Taiwan): *"The Bank, on behalf of the Ministry of Finance, conducted an auction of 30-Year Central Government Bonds (A15105)"*; coupon 1.8750%; bid-to-cover 1.55 | **30-year**, matures 2056-05-29 | **1.8140% weighted average accepted** (lowest 1.6600%, highest 1.9000%) | auction **2026-05-26** | `https://www.cbc.gov.tw/en/cp-448-191306-0372c-2.html` · `sov/cbc_cp-448-191306-0372c-2.html` |
| same authority, newer, shorter | CBC for the MOF, 20-Year A15107; bid-to-cover **1.04** | 20-year | 1.9040% w.a. (highest 2.2000%) | 2026-07-23 | `https://www.cbc.gov.tw/en/cp-448-192620-7e19c-2.html` |
| same authority, newest | CBC for the MOF, 10-Year reopening A15106R | 10-year | 1.9080% w.a. | 2026-08-07 | `https://www.cbc.gov.tw/en/cp-448-192691-2d2ec-2.html` |
| **OFFICIAL SECONDARY CURVE (the dated observation used)** | **Taipei Exchange (TPEx) Treasury Yield Curve**, benchmark A15105: *"The Yield is based on Electronic Bond Trading System (EBTS) Volume-weighted Average Yield."* | **30-year** (29.714 years residual) | **1.886%** | **2026-09-11** | `https://www.tpex.org.tw/storage/bond_zone/tradeinfo/govbond/2026/202609/Curve.20260911-E.xls` · `sov/Curve.20260911-E.xls` |
| same file | benchmarks 2Y 1.7104 · 5Y 1.8223 · 10Y 1.9205 · **20Y 2.101** · 30Y 1.886; fitted zero-coupon 30Y **2.176%** (cubic B-spline) and **2.189%** (Svensson) | | | 2026-09-11 | same |

- **Rate used: TWD 30-year 1.89% (TPEx EBTS benchmark A15105, 2026-09-11), carried as a band of about
  1.8-2.2%** across the issuing authority's May auction (1.81%), the 20-year benchmark (2.10%) and the
  fitted 30-year zero rate (2.18-2.19%). **Why the exchange curve beside the auction:** the CBC auction is
  the issuing authority's own print but is three and a half months old; TPEx is the official secondary
  market on which the MOF's bonds trade, and its file is dated to the observation. The two agree within
  8bp. **Rung stated: the issuing authority's auction is the anchor; the TPEx curve is the dated
  observation (evidence ladder, exchange rung).** The single volume-weighted 30-year print sits *below* the
  20-year (1.886 against 2.101), which is why the fitted zero rate is shown beside it.
- **The longest liquid tenor is 30 years; it is not shorter.** The MOF issued a 30-year bond in May 2026
  and TPEx quotes it. Its liquidity is thinner than the 10-year's (the 20-year auction covered only 1.04
  times); stated, and it changes no verdict because the floor governs.
- **Reference, not paired with the NT$ yield: USD 30-year 5.35%** (US Treasury daily par yield curve,
  issuing authority, **2026-09-11**, struck fresh 2026-09-13 through `tools/sources.py`).
- **FX (issuing authority): NT$31.638 per US$**, Central Bank of the Republic of China, *NT$/US$ Closing
  Rate* (interbank spot close), **2026-09-11**, `https://www.cbc.gov.tw/en/lp-700-2.html` (saved
  `sov/cbc_fx.html`). Used only to measure the ADR premium and to show a dollar cap for orientation.
- **ADR ratio, derived: 1 ADS = 5 common shares.** 20-F FY2025 Item 6: *"shares held in the form of ADSs
  (each ADS represents five (5) common shares)"*; Note 21: *"TSMC's total issued and outstanding ADSs were
  1,062.7 million units, representing 5,313.6 million common shares"* (5,313.6 / 1,062.7 = 5.000); the Q2
  2026 consolidated report repeats it at 2026-06-30 (*"1,062,690 thousand units, representing 5,313,451
  thousand common shares"*). Depositary: Citibank, N.A. (Item 7).

### The share count, read by hand and walked forward (`cover_shares.py` is blind to 6-Ks)

| date | count | what changed | document · accession |
|---|---|---|---|
| **2025-12-31** | **25,932,524,521 outstanding** | *"As of December 31, 2025 , 25,932,524,521 Common Shares, par value NT$10 each were outstanding."* | **20-F cover**, `0001628280-26-025362` |
| 2026-02-28 | 25,932,524,521 | Item 10: *"issued and outstanding as of December 31, 2025 and February 28, 2026 . No employee stock options were outstanding"* | same |
| 2026-03-01 | **−154,454** | *"we reclaimed 32,060 common shares, 81,394 common shares and 41,000 common shares formerly granted in the form of RSAs"*; cancellation resolved 2026-05-12 | same, Item 10; Q2 2026 report Note 21 |
| **2026-06-30** | **25,932,370 thousand issued and paid** (= 25,932,370,067) | Q2 2026 consolidated report, Note 21; no treasury stock on the 2026-06-30 balance sheet | 6-K 2026-08-14, `0001046179-26-000541` |
| July 2026 | no change | July month-end report: *"6. The cancellation of TSMC common shares: None."* | 6-K 2026-08-25, `0001046179-26-000545` |
| **~2026-09-01** | **25,932,364,992 (derived)** | Q1 2026 dividend fixed at NT$181,526,590,469 = NT$7.0 × 25,932,370,067; re-set to **NT$7.00000137** *"Due to the reclamation of shares from 2024 restricted stock awards"*: 181,526,590,469 / 7.00000137 = 25,932,364,992, **≈5,075 more shares reclaimed** | 6-K 2026-09-01, `0001046179-26-000552` |

- **Count used: 25,932,364,992.** The difference from the 20-F cover is 159,529 shares (0.0006%). Cross-check:
  the Q2 2026 release computes EPS *"Based on 25,932 million weighted average outstanding shares"* (6-K
  2026-07-16, `0001046179-26-000451`, Ex. 99.1).
- **Treasury shares: none.** The one buyback in the window (*"to repurchase 3.2 million shares"*, Board
  2024-06-05, for RSAs) was cancelled by Board resolution 2024-08-13 (Note 21).
- **Other classes: none.** One class of common share, one vote each (Q2 2026 report Note 21).
- **No split after the measurement date**; `close × shares(measurement) × splits after measurement` holds
  trivially.

### The price, the ADR premium and the cap (aggregator for the live quote only, flagged)

| quote | close | date | NT$ per common share (1 ADS = 5; CBC NT$/US$ of the same date) |
|---|---|---|---|
| **TWSE 2330** | **NT$2,410** | **2026-09-11** | **2,410** |
| NYSE TSM | US$433.24 | 2026-09-11 | 2,741 at 31.638 → **+13.7%** over the same calendar day's Taipei close |
| NYSE TSM, prior session | US$428.03 | 2026-09-10 | 2,701 at 31.548 → **+10.2%** over TWSE 2026-09-10 (NT$2,450); +12.1% over TWSE 2026-09-11 |

*(Yahoo Finance chart API, symbols 2330.TW and TSM; **aggregator, flagged**; saved
`prices_2026-09-13.json`. Taipei closes about thirteen hours before New York, so no same-instant pair
exists; the three pairings bracket it.)*

- **The ADR trades at a premium of about 10-14% to the local shares.** Its cause is not needed for any
  verdict and is not argued.
- **The quote used is the TWSE local close, NT$2,410**, because the earnings are NT$ and the local line is
  the cheaper claim on the same business. **Using the ADR would raise the cap ~12% and lower every yield
  below by the same proportion**; carried at Q5 in the direction that hurts.
- **Cap = NT$2,410 × 25,932,364,992 = NT$62,497bn (NT$62.5 trillion).** At the CBC's 31.638, about
  **US$1,975bn, shown for orientation only and never set against NT$ earnings.** The NT$7.0 Q1 2026
  dividend goes ex on 2026-09-16, after the price date, so the price still carries it (0.3%).

### The filing was read — not tagged data **[E3-27, E4-14]**
- [x] MD&A (Item 5: results, liquidity, capital expenditures) [x] cash-flow statement incl. detail lines
  (F-11 to F-13) [x] footnotes (share capital and treasury stock, RSAs and cash-settled share-based payment,
  employees' compensation, government grants, segment and geographic information, major customers, PP&E,
  commitments)
- **Primary document: Form 20-F, fiscal year ended 2025-12-31, filed 2026-04-16, accession
  `0001628280-26-025362`, `tsm-20251231.htm`, CIK 0001046179.**
- Also read for the windows: 20-F FY2024 `0001193125-25-083423` · FY2023 `0001193125-24-099840` · FY2022
  `0001193125-23-107214` · FY2021 `0001193125-22-104891` · FY2020 `0001193125-21-118512` · FY2017
  `0001193125-18-121866` (each carries three years of cash flows, so FY2015-FY2025 are covered from filed
  statements).
- 6-Ks read: the Q2 2026 consolidated report (2026-08-14); the quarterly earnings releases with guidance for
  Q3 2023 to Q2 2026 (twelve quarters); the Board resolutions of 2026-02-10, 2026-05-12 and 2026-08-11; the
  2026 AGM resolutions (2026-06-04); the August 2026 revenue report (2026-09-10); the July 2026 month-end
  report (2026-08-25); the dividend adjustment (2026-09-01); the VIS share sale (2026-05-15).
- **Figure cross-checked against the filed statement:** **Net cash generated by operating activities
  NT$1,826,177.1 million for 2024**, in the audited CONSOLIDATED STATEMENTS OF CASH FLOWS of the FY2025 20-F
  (F-11, comparative column), equals `companyfacts` `ifrs-full:CashFlowsFromUsedInOperatingActivities`
  2024-12-31, **TWD 1,826,177,100,000**. FY2025 **NT$2,274,975.6 million** (US$72,520.7M at the 20-F's
  convenience rate) is read from the filing because `companyfacts` does not have it. **Revenue NT$3,809.05bn
  for 2025** equals the 2026-02-10 Board resolution (*"Consolidated revenue totaled NT$3,809.05 billion and
  net income was NT$1,717.88 billion"*, 6-K `0001046179-26-000017`).
- **A new filing class, recorded for Q3:** EDGAR shows **42 Forms 3 filed on and after 2026-03-18 and 226
  Forms 4 since**, by TSMC directors and officers, a filing class that did not exist for this registrant
  before 2026. Read at Q3.

# Company Run — Taiwan Semiconductor Manufacturing Company Limited (TSM) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

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

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### The business, from the filing: one segment, one product, sold by the wafer
**Source: 20-F FY2025 Item 4 and Item 5; Note 38 (segments); Q2 2026 earnings deck (6-K 2026-07-16).**
Note 38: *"the Company has only one operating segment, the foundry segment. The foundry segment engages
mainly in the manufacturing, sales, packaging, testing and computer-aided design of integrated circuits and
other semiconductor devices and the manufacturing of masks."* The release boilerplate: *"TSMC deployed 305
distinct process technologies, and manufactured 12,682 products for 534 customers in 2025."*

**Revenue by process node, share of wafer revenue** (20-F FY2025 Item 5; Q2 2026 release and deck):

| node | 2023 | 2024 | 2025 | Q2 2026 |
|---|---|---|---|---|
| 2-nanometer | — | — | — | **3%** |
| 3-nanometer | 6% | 18% | **24%** | 30% |
| 5-nanometer | 33% | 34% | **36%** | 33% |
| 7-nanometer | 19% | 17% | 14% | 11% |
| **7nm and below ("advanced")** | **58%** | **69%** | **74%** | **77%** |
| 16nm | 10% | 8% | 7% | 6% (16/20nm) |
| 28nm | 10% | 7% | 7% | 6% |
| 40/45, 65, 90nm and older | 21% | 16% | 12% | 11% |

**Revenue by platform, NT$ millions** (20-F FY2025 Item 4, *"breakdown of our net revenue by platform"*):

| platform | 2023 | % | 2024 | % | 2025 | % |
|---|---|---|---|---|---|---|
| **High Performance Computing** | 934,769 | 43% | 1,476,891 | 51% | **2,192,931** | **58%** |
| Smartphone | 814,914 | 38% | 1,005,130 | 35% | 1,110,816 | 29% |
| Internet of Things | 161,917 | 8% | 165,516 | 6% | 191,047 | 5% |
| Automotive | 133,654 | 6% | 139,323 | 5% | 186,667 | 5% |
| Digital Consumer Electronics | 47,000 | 2% | 47,961 | 1% | 47,997 | 1% |
| Others | 69,482 | 3% | 59,487 | 2% | 79,596 | 2% |
| **Total** | **2,161,736** | | **2,894,308** | | **3,809,054** | |

*"The increase in our net revenue from 2024 to 2025 mainly came from High Performance Computing of NT$
716,040 million, or a 48% year-over-year increase."*

**Revenue by customer headquarters, NT$ millions** (Item 4: *"We categorize our net revenue mainly based on
the countries where our customers are headquartered"*):

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| **North America** | 1,470,215 (68%) | 2,031,326 (70%) | **2,875,270 (75%)** |
| Asia Pacific (ex China, Japan) | 174,947 (8%) | 284,308 (10%) | 329,269 (9%) |
| China | 267,154 (12%) | 331,673 (11%) | 327,503 (**9%**) |
| Japan | 132,072 (6%) | 144,240 (5%) | 150,428 (4%) |
| EMEA | 117,348 (6%) | 102,761 (4%) | 126,584 (3%) |

**Customer concentration** (Item 3.D and Note 38(b)(2)):
- *"our ten largest customers in 2023 , 2024 and 2025 accounted for approximately, 70% , 76% and 78% of our
  net revenue."*
- *"Our largest customer in 2023 , 2024 and 2025 accounted for 25% , 22% and 19% of our net revenue ... Our
  second largest customer ... 11% , 12% , and 17%."*
- Note 38: **Customer A** NT$352,271.2M (12%) in 2024 and **NT$726,974.3M (19%) in 2025**, below 10% in 2023;
  **Customer B** NT$546,550.9M (25%), 624,345.5M (22%), 645,178.7M (17%). **The largest customer changed
  identity in 2025**: B (25% in 2023) fell to second; A rose from under 10% to first. **The filing does not
  name either**, and this run does not name them.
- Note on receivables: *"As of December 31, 2024 and 2025 , the Company's ten largest customers accounted for
  93 % and 84 % of accounts receivable, respectively"* (credit concentration, Note 33).

**Where the assets sit** (Note 38(b)(1), noncurrent assets, NT$ millions, 2025-12-31): **Taiwan 3,102,343.0
(80.0%)** · United States 540,057.4 (13.9%) · Japan 117,403.2 (3.0%) · China 65,019.9 (1.7%) · EMEA 51,515.1
(1.3%). **The customers are 75% North American; the plant is 80% Taiwanese.**

**Capacity and capital** (Item 4): *"In 2025 , our annual capacity (in 12-inch equivalent wafers) exceeded 17
million wafers, compared to approximately 17 million wafers in 2024."* Capex *"NT$ 949,817 million, NT$
956,007 million and NT$ 1,272,411 million"* in 2023-2025; *"Our capital expenditures in 2026 are expected to be
between US$52 billion and US$56 billion"*; the Board of 2026-08-11 approved a further *"approximately
US$29,442.50 million"* of appropriations. Overseas: TSMC Arizona (Fab 21; *"Our first facility successfully
entered high volume production at the end of 2024. Construction of our second facility is ongoing, and the
construction of our third facility commenced in 2025"*); JASM, Kumamoto (Fab 23, 72.6% owned, *"volume
production commenced in December 2024"*); ESMC, Dresden (Fab 24, 70.0% owned, construction since 2024);
TSMC Nanjing and Shanghai; and a new image-sensor joint venture with Sony Semiconductor Solutions (Board
2026-08-11, subscription *"of not more than 282 billion Japanese yen"*).

**Wafer shipments (12-inch equivalent, thousands), the unit series [E4-55]** (quarterly decks): Q3 2023
2,902 · Q4 2023 2,957 · Q1 2024 3,030 · Q2 2024 3,125 · Q3 2024 3,338 · Q4 2024 3,418 · Q1 2025 3,259 · Q2 2025
3,718 (from the Q2 2026 deck's year-ago column) · Q3 2025 4,085 · Q4 2025 3,961 · Q1 2026 4,174 · Q2 2026
**4,336**. The Q3 2022 year-ago column in the Q3 2023 deck reads **3,974**, and Q4 2022 **3,702**: **units fell
27% year on year into Q3 2023 and did not exceed the Q3 2022 figure until Q3 2025**, while dollar revenue per wafer rose
throughout on the node mix.

### Unit economics in my own words, no management language
A chip designer (a phone maker, a GPU company, a hyperscaler designing its own accelerator) owns the design
and does not own a factory. It pays TSMC to turn silicon wafers into finished chips on a chosen process
generation. **TSMC is paid per processed wafer; the price per wafer rises steeply with how new the process
is**, so revenue is wafers shipped times the mix-weighted price. The cost is dominated by the plant: NT$679.7bn
of depreciation in 2025 (17.8% of revenue) on NT$3.1-4.3tn of net property, plant and equipment, plus
R&D at 6.5% of revenue to develop the next process, plus labour and materials. **Because the plant is a fixed
cost, utilisation and node mix drive the margin**: gross margin was 54.3% in Q3 2023 at 2,902k wafers and
67.7% in Q2 2026 at 4,336k. The cash cycle is: build the fab and fill it with equipment two to three years
ahead of demand, run the newest node at a premium while few can match it, keep the depreciated older fabs
running at lower prices for specialty and mature products, and spend the next generation's capex out of
the current generation's cash. **Customers pay in dollars; the plant and most people are in Taiwan and paid
in NT dollars.** Some customers prepay to reserve capacity (temporary receipts of NT$189.9bn at 2025-12-31,
Note 22).

### The scarce input this business controls
**Yielded, high-volume manufacturing capacity at the leading-edge process, together with the process know-how
to ramp each new node first.** 74% of 2025 wafer revenue came from 7nm and below; the 20-F claims volume
production of 7-, 5-, 3- and 2-nanometer *"prior to the implementation of those advanced process technologies
by competitors and many integrated device manufacturers"* (Item 4, R&D). **That is a claim this file tests
at Q2 against competitors' own filings; it is not taken from TSMC.** What Q1 can say from the filing alone:
the input is **not a patent, a licence or a brand**; it is accumulated manufacturing learning embodied in a
NT$4.3tn plant that must be re-bought at every node. The second scarce input is advanced packaging capacity
(CoWoS, SoIC), which the 20-F names among the 2026 capex uses (*"expanding capacity for specialty technologies
and advanced packaging"*).

### Will the fundamentals look broadly the same in ten years?
- **The model: yes, on the record.** TSMC *"pioneered the pure-play foundry business model when it was founded
  in 1987"*; the fabless-designer-plus-foundry division of labour has held for 38 years and has spread (the
  20-F: *"a growing trend among system companies designing their own semiconductors and working directly with
  the semiconductor foundries"*). Intel's own FY2025 10-K names the fallback of shifting manufacturing *"to
  third-party foundries, particularly TSMC"* (INTC run, 2026-09-07).
- **The technology: no, and by design.** The node table above turned over by more than half in three years (3nm
  6% → 24% → 30%; 2nm appears in Q2 2026). **[E3-31] names this directly** (*"If a business is complex or
  subject to constant change, we're not smart enough to predict future cash flows"*). **Where the constant
  change sits, stated so Q1 does not quietly absorb it:** the *product* changes every generation; the
  *economics of the product* (paid per wafer, premium at the newest node, plant-heavy, dollar revenue) have not
  changed across the filed decade. **Whether a moat that is re-won each node is a moat is precisely
  [E4-04]'s question, which the framework scopes at Q2** (*"does the spending defend the same advantage, or buy
  its replacement?"*). It is carried there, not answered here.
- **The mix: already moving.** HPC went 43% → 58% of revenue in two years; the largest customer changed; North
  America went 68% → 75%. **The fundamentals of how TSMC makes money are the same; what it makes money FROM is
  concentrating** into one application class and two customers (36% of 2025 revenue).

### [E4-46] — five minutes, not five months
The mechanism above is stated in one paragraph from the filing, and every figure in it is filed. **This is not
a business that needs months of study to see how it makes money.** The hard questions (whether the lead is
durable, what the plant really costs to maintain, what Taiwan's location does to survival) are Q2 and Q4
questions with named documents, not a Q1 competence gap.

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *The money is made one wafer at a time, priced by node, on a plant that is rebought each generation; the
  scarce input is yielded leading-edge capacity. The [E3-31] "constant change" clause is live and is carried
  to Q2's [E4-04] test by name, not discharged here.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**Pre-registered before the row was built (operator rule 9, [E4-26]):** the hypothesis most at risk of
being favoured is *"TSMC is a franchise"*, because every number in Q1 is excellent and because the corpus
itself praises this company by name (below). So the disconfirming case is hunted hardest: the [E4-04]
exclusion, the second [E2-44] characteristic, and what happened to the last leading-edge incumbent.

### [E3-03], the three criteria, in the customers' and competitors' own filings
**(1) Needed or desired: YES.** Revenue NT$3,809bn, 534 customers (Q1).

**(2) Thought by its customers to have no close substitute: YES AT THE LEADING EDGE, NO AT MATURE NODES.**
The customers' filed words, not TSMC's:
- **Broadcom** 10-K FY2025 (`0001730168-25-000121`): *"During fiscal year 2025, approximately 95% of the wafers
  manufactured by our CMs were produced by TSMC. We believe our wafer requirements represent a meaningful
  portion of TSMC's total production capacity. However, TSMC ... could choose or be required to materially
  prioritize capacity for other customers or reduce or eliminate deliveries to us on short notice."*
- **AMD** 10-K FY2025 (`0000002488-26-000018`): *"We rely on Taiwan Semiconductor Manufacturing Company Limited
  (TSMC) for the production of all wafers for microprocessor and GPU products at 7 nanometer (nm) or smaller
  nodes, and we rely primarily on GLOBALFOUNDRIES Inc. (GF) for wafers for microprocessor and GPU products
  manufactured at process nodes larger than 7 nm."*
- **Intel**, TSMC's would-be competitor, 10-K FY2025 (`0000050863-26-000011`): *"Our primary competitor in
  leading-edge semiconductor process technology is TSMC, which holds a leading position in manufacturing at
  scale for the most advanced nodes. We also compete directly with Samsung in this market. Other Intel
  Foundry competitors include GlobalFoundries, UMC and SMIC, which primarily focus on mature process
  technologies."* And on its own products: *"Some of our most advanced current and future products are or
  will be either exclusively manufactured by TSMC or reliant upon critical components, including various
  compute die, manufactured by TSMC"*; *"most of our competitors have longer and more established
  relationships with TSMC."*
- **The substitute that exists:** Nvidia's 10-K FY2026 (`0001045810-26-000021`): *"We utilize foundries, such as
  Taiwan Semiconductor Manufacturing Company Limited, or TSMC, and Samsung Electronics Co., Ltd., or Samsung,
  to produce our semiconductor wafers."* Qualcomm's 10-K FY2025 (`0000804328-25-000085`): *"The primary foundry
  suppliers ... include Taiwan Semiconductor Manufacturing Company (TSMC), Samsung Electronics and Global
  Foundries."* **Two of the largest designers name a second leading-edge source; neither quantifies the split.**
- **Mature nodes (26% of 2025 wafer revenue, 16nm and older):** GlobalFoundries' 20-F FY2025 names *"TSMC,
  ... UMC and Semiconductor Manufacturing International Corporation"* as key competitors, and AMD buys its
  >7nm wafers from GF. **At these nodes there are close substitutes, filed.**

**(3) Not subject to price regulation: YES**, with a regime caveat: export controls restrict what TSMC may
ship to *"specified destinations"* (Item 3.D); they constrain volume, not price.

**[E3-43]'s demonstration test** — *"The existence of all three conditions will be demonstrated by a
company's ability to regularly price its product or service aggressively and thereby to earn high rates of
return on capital"*: return on average parent equity **24.2% (2017) · 23.0 · 21.6 · 29.6 · 29.7 · 39.3 ·
26.9 · 30.2 · 35.6% (2025)**; 45.9% annualised in Q2 2026 (deck). **Passed, on the filed record.**

### [E2-44], the two-characteristic test
**(1) Price when demand is flat and capacity is not fully utilized — PASSED on revenue per wafer, with the
mix caveat stated.** The 2023 downturn is the test the filing supplies. Annual 12-inch-equivalent shipments
(20-F Item 5, each year's *"We shipped approximately ..."*): 2016 9.6M · 2017 10.4M · 2019 10.07M · 2020 12.40M
· 2021 14.18M · **2022 15.25M · 2023 12.00M** · 2024 12.91M · 2025 15.02M. **Units fell 21.3% in 2023; revenue
fell only 4.5%**, so NT$ revenue per shipped wafer rose **from ~148k to ~180k (+21%)**. The quarterly decks give
the same in dollars: **US$5,091 per wafer in Q3 2022 against US$5,955 in Q3 2023 (+17%)** while shipments fell
27%. **Caveat, stated so the number is not over-read:** TSMC files no like-for-like price. Its MD&A attributes
revenue growth to *"an increase in ASP due to a higher proportion of advanced technology"*, i.e. mix. The 20-F's
pricing paragraph: *"We establish pricing levels for specific periods of time with our customers, some of which
are subject to adjustment during the course of that period."* **What survives the caveat:** in the one filed
year of 21% unit decline, gross margin was **54.4%**, higher than any year in the row for any peer (UMC's best
45.1% in 2022; GFS's best 28.4% in 2023).

**(2) Dollar volume increases with only minor additional capital — FAILED, and not narrowly.** Revenue rose
NT$2,966bn from 2015 to 2025; **cumulative capex 2016-2025 was NT$7,042bn against NT$4,069bn of depreciation**
(ratio 1.73). Capex was **30.5-52.9% of revenue in every year** (33.4% in 2025); capex exceeded depreciation
in every year of the eleven (1.10x to 2.53x). Net PP&E went from NT$853bn (2015) to NT$4,303bn (2026-06-30).
**The growth was bought, every year, with capital.** This is the good-savings-account shape of [E4-20]
(Q4), not the See's shape.

### [E3-46] / the second question as a number
Gross margin **48.7% (2015) → 59.9% (2025)**, operating margin **37.9% → 50.8%**, ROE above 21% in all nine
computable years. **High returns on capital employed over time: yes.**

### [E2-45] — the attacker's test is not hypothetical; it has been run, and it is filed
*"how I would like, assuming I had ample capital and skilled personnel, to compete with it."* Two attackers with
ample capital and skilled personnel are on file:
- **Intel Foundry** (INTC run, 10-K Note 3): segment operating margin **−38% (2023), −76.8% (2024), −57.9%
  (2025)**; external foundry revenue **$547M → $159M → $307M**; and Intel's own filed fallback, *"we would expect,
  over time, to shift manufacturing to third-party foundries, particularly TSMC."*
- **Samsung Foundry**: Samsung Electronics is not an SEC registrant (INTC run: CIK 0000879316 holds only paper
  SUPPL/ARS and 13D/G filings, reports under Rule 12g3-2(b)). **The evidence ladder's third rung, the company's
  own English release, was read:** Samsung's *"Second Quarter 2026 Results"* (2026-07-30, Samsung Semiconductor
  Global Newsroom) gives *"The DS Division posted KRW 127.5 trillion in consolidated revenue and KRW 89.2
  trillion in operating profit"*, and for foundry only *"Earnings for the Foundry Business improved
  significantly prior to incentive-related provisions"*. **No separate foundry revenue or profit is given**
  (fetched via the newsroom page and summarised by the fetch tool, so the absence is recorded as "no instance
  found in that release", not as "does not exist"). **Samsung Foundry's margin is UNKNOWABLE from the shelf:
  no document states it.**
- **The corpus's own reading of the contest, 2023 meeting** (`Annual Meetings/2023 Annual Meeting.txt`, section
  26, transcript): *"Taiwan Semiconductor's one of the best managed companies and important companies in the
  world. And I think you'll be able to say the same thing five, or ten, or 20 years from now."* ... *"there's
  nobody in the chip industry that's in their league, at least in my view."* **This is not a ledger row; it is cited as shelf evidence under prime rule 4, verbatim from the transcript
  file, which carries its own "(PH)" marker on the questioner's name.** It is weighed below, at [E4-04], because it bears on the class and on
  Q4.

### THE COMPETITOR ROW — required [E3-28]. Same metric, same window, filing-sourced.

**Gross margin %** (IFRS gross profit / revenue):

| | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **TSMC** | 48.7 | 50.1 | 50.6 | 48.3 | **46.0** | 53.1 | 51.6 | 59.6 | **54.4** | 56.1 | **59.9** |
| **UMC** | 21.9 | 20.5 | 18.1 | 15.1 | 14.4 | 22.1 | 33.8 | **45.1** | 34.9 | 32.6 | 29.0 |
| **GlobalFoundries** | — | — | — | — | −9.2 | −14.7 | 15.4 | 27.6 | **28.4** | 24.5 | 24.9 |
| **Intel Foundry** | *no gross margin disclosed* | | | | | | | | | | |
| **Samsung Foundry** | *not disclosed in any document on the shelf* | | | | | | | | | | |
| **SMIC** | *not an SEC registrant* | | | | | | | | | | |

**Operating margin %**:

| | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **TSMC** | 37.9 | 39.9 | 39.4 | 37.2 | 34.8 | 42.3 | 40.9 | 49.5 | 42.6 | 45.7 | **50.8** |
| **UMC** | 7.5 | 4.2 | 4.4 | 3.8 | 3.3 | 12.4 | 24.3 | 37.4 | 26.0 | 22.2 | 18.5 |
| **GlobalFoundries** | — | — | — | — | −28.0 | −34.1 | −0.9 | 14.4 | 15.3 | −3.2 | 11.7 |
| **Intel Foundry** | | | | | | | | | **−38** | **−76.8** | **−57.9** |

**Capex as % of revenue** (the [E2-44](2) metric): TSMC 30.5 · 34.6 · 33.8 · 30.6 · 43.0 · 37.9 · 52.9 · 47.8 · 43.9 ·
33.0 · 33.4 · UMC 41.8 · 61.9 · 29.6 · 13.0 · 11.1 · 14.9 · 22.6 · 28.7 · 41.1 · 38.1 · 20.1 · GFS (2019-2025) 10.1 ·
12.2 · 26.8 · 37.7 · 24.4 · 9.3 · 10.6.

**Revenue multiple, same window:** TSMC ×4.52 (2015→2025, NT$) and ×3.56 (2019→2025); UMC ×1.64 and ×1.60; GFS
×1.17 (2019→2025, US$). **TSMC's share of the filed row rose in every sub-window.**

*Sources: TSMC `companyfacts` FY2015-FY2024 (transcription, newest vintage; FY2024 operating cash cross-checked
at Step 0) and the FY2025 20-F `0001628280-26-025362` (gross profit NT$2,281,294.0M, income from operations
NT$1,936,091.7M); UMC `companyfacts` FY2015-FY2024 and UMC 20-F FY2025 `0001193125-26-193757` (revenue
NT$237,553M, gross profit NT$68,906M, operating income NT$43,949M, *"Our gross margin decreased from 32.6% in
2024 to 29.0%"*); GlobalFoundries `companyfacts` (IFRS, US$) through its 20-F FY2025 `0001709048-26-000022`;
Intel Foundry from the INTC run (10-K FY2025 Note 3). Arithmetic in `row.py` / `row_out.json`.*

- **Peers named: 5 of the industry's 6 real leading or scaled foundries** (TSMC, Samsung Foundry, Intel Foundry,
  UMC, GlobalFoundries, SMIC); **metrics obtained for 3** (UMC and GFS in full, Intel Foundry on operating
  margin). **Samsung and SMIC are UNKNOWABLE from the shelf**, the INTC run's standing treatment. **This does
  not make the class PROVISIONAL in the direction that matters here**: the missing names are *additional*
  competitors, one of them (Samsung) the filed second source at Nvidia and Qualcomm. Adding them cannot
  widen TSMC's lead; it could only narrow it.
- **[E3-61], the row's limit:** the row shows position, not conduct. It cannot show whether Samsung or a
  subsidised Intel will price below cost to buy share, and the corpus says Munger had no model for that.

### Untapped pricing power [E3-33, E5-28, E4-37]
**Claiming the class is claiming near-monopoly [E5-28].** At the leading edge the customer filings above
support a near-monopoly *position* (95% of Broadcom's wafers; all of AMD's ≤7nm). **Whether pricing power is
untapped cannot be read from the filing**: TSMC files no price list, no price increase and no ASP (recorded
sweep of the FY2025 20-F for "average selling price", "pricing", "price increase" and "wafer price": the only
hits are the pricing paragraph quoted above and risk-factor references to customers' end-product ASPs). The
**observable** is margin against guidance, twelve quarters (Q3 2023 to Q2 2026; the Q2 2025 guidance read from the Q1 2025 release because that deck's text did not extract): **revenue landed at or above the top of the guided range in all twelve, gross margin at or above the range in all twelve (above the top in seven, by up to 4.3 points: Q3 2024, 57.8% against 53.5-55.5%), operating margin above the top in ten and at the top in two.** Never below. **[E4-37]'s agony test cannot be run from a filing that discloses no price decision.** No finding either way.

### [E4-04] — must the moat be continuously rebuilt? **Yes. The filer says so, the capital says so, and the last incumbent's record shows what a lapse does.**

**The full ledger row, not the fragment:** *"Our criterion of 'enduring' causes us to rule out companies in
industries prone to rapid and continuous change. Though capitalism's 'creative destruction' is highly
beneficial for society, it precludes investment certainty. A moat that must be continuously rebuilt will
eventually be no moat at all."* — **[E4-04]**, 2007 letter.

**The filer's description of its own industry** (20-F FY2025, Item 4, Research and Development): *"The
semiconductor industry is characterized by rapid technological changes, frequently leading to the
introduction of new technologies to meet customer demand and the obsolescence of recently introduced
technology and products. We believe that to remain technologically ahead of our competitors and maintain our
market position in the foundry segment, we need to be a technology leader in the semiconductor industry."*
And Item 3.D: *"The semiconductor industry and its technologies are constantly changing ... If we do not
anticipate these changes in technologies and rapidly develop new and innovative technologies, or our
competitors unforeseeably gain sudden access to additional technologies, we may not be able to provide
services on competitive terms."* **TSMC describes its position as conditional on continuous leadership, in
the language [E4-04] rules out.**

**The framework's scope test, answered part by part:**
1. **Does the spending defend the same advantage, or buy its replacement?** **It buys the replacement.** The
   premium is earned at the newest node, and the newest node is new plant: 3nm went 6% → 24% → 30% of wafer
   revenue in three years, 2nm entered at 3% in Q2 2026, and capex ran 1.10-2.53 times depreciation in every
   year. **What does carry across nodes** is real and is stated for the defence: the design ecosystem and
   *"305 distinct process technologies"*, the mature fabs (26% of wafer revenue from 16nm and older), the
   customer relationships Intel itself calls *"longer and more established"*, and the scale that lets the
   current node's cash (operating cash NT$2,275bn) fund the next node's plant (capex NT$1,272bn) when an
   attacker's cannot. **Those defend the ability to buy the replacement; they are not the thing that earns
   the premium.** (The KLAC run drew exactly this line on 2026-09-07: *"Intel's moat basis (the process
   node) must be wholly replaced every generation"*; KLA's spend defends platform families that persist.)
2. **Does a lapse destroy the structure, or merely narrow it?** **The filed record of the last leading-edge
   incumbent answers it.** Intel's gross margin was **61.0% in 2016 and 34.8% in 2025**, 26.2 points below where
   it started and 25.1 points below TSMC's 2025 figure; its most advanced products are now made *"exclusively"*
   by TSMC (INTC run, 10-K FY2016-FY2025). **A lapse did not narrow Intel's manufacturing lead; it transferred
   it, within about two node generations.** GlobalFoundries today competes only above 7nm (AMD's 10-K). **Nothing
   in TSMC's structure is filed as immune to the same mechanism**; its own risk factor names it.

**What the ten-year record shows, tested rather than assumed (the brief's instruction):** TSMC's margin and
filed relative position **held and widened through every node transition in the window** (16/12nm → 10nm →
7nm → 5nm → 3nm → 2nm): gross margin 48.7% → 59.9%, operating margin 37.9% → 50.8%, revenue ×4.5 against UMC's
×1.6, and the two filed attackers either losing money (Intel Foundry) or absent from the leading edge (GFS).
**Direction [E4-32]: widening, on every filed metric.**

**The class ruling, and why the record does not overturn it.** The framework carries this exact shape by
name: *"the long runs it does permit are **surfing runs**: 'when a surfer gets up and catches the wave and
just stays there, he can go a long, long time. But if he gets off the wave, he becomes mired in shallows'
[E3-51]. A surfing run is not a moat."* Munger's passage is about technology specifically (*"When technology
moves as fast as it does in a civilization like ours, you get a phenomenon that I call competitive
destruction"*). Of **[E4-36]'s four causes of extreme success**, TSMC's record draws on the first
(*"Extreme maximization ... of one or two variables"*: scale and node timing), the second (*"a bigger
combination drives success, often in nonlinear fashion"*: pure-play neutrality plus ecosystem plus scale) and
the fourth (*"Catching and riding some sort of big wave"*: smartphones, then AI; HPC 43% → 58% in two years).
**A ten-year record of staying on the wave is the surfing run doing what the corpus says it does; it is not
evidence that the wave has stopped moving.** Intel's record was longer than TSMC's is now.

**THE CORPUS TENSION, carried and not resolved by preference (prime rule 2).** The corpus authors *bought*
this company. The 2023 questioner: *"Berkshire bought a substantial position in Taiwan Semiconductor, and
contrary to its normal holding timeline, sold almost the entire position within a few short months."*
Buffett's answer gives the exit ground as location, not the business (*"I don't like its location. And I've
reevaluated that"*), and praises the competitive position without qualification. **So the corpus's own
practice on this name did not apply [E4-04] as a bar at the purchase, and its stated reason for leaving was
a Q4 matter.** Three things keep this from overturning the class ruling, each stated so the operator can
dispute it: (a) the passage is a transcript answer about why a position was *sold*, and names no criterion
under which it was bought; (b) the same answer says *"I'd rather find marvelous people — and I won't find it
in the chip industry"* (transcript wording, left as filed; its sense is ambiguous and it is not leaned on
either way); (c) [E4-04] is a written criterion restated in a letter, and the framework's own open questions
already carry rule-against-practice tensions without grading them (Open Question 3). **This is flagged to the
operator as a place where corpus practice and a framework criterion disagree on a named company. Changing
how [E4-04] scopes leading-edge manufacturers would be a structural change and requires a written case
(prime rule 5); this run does not make it.**

### THE FAIR COUNTER-CASE, stated as its best advocate would state it [E4-51]
*"TSMC is not a surfer; it is the ocean. Every leading-edge chip designer on earth, including its only two
funded attackers, buys from it. The thing that persists across nodes is not the plant but the compounding
of yield learning, a design ecosystem no customer wants to leave, and a cash flow that funds each node before
competitors can fund theirs. Intel lost because it was an integrated manufacturer with one customer (itself)
and no external volume to learn on; TSMC has 534. Margins rose through five node transitions and a 21% unit
decline. The corpus authors bought it and called it peerless; they sold for location, which is a survival
question, not a franchise question. Ruling it out at Q2 is the error of omission [E3-47] the corpus rates as
most expensive."* **Each clause is supported by a filed number above.** The answer on the filed record: the
counter-case establishes **position, scale and direction**, all of which this file grants. It does not
establish that the premium-earning asset is anything other than the current node, which the filer itself
says must be re-won by *"rapidly develop[ing] new and innovative technologies"*, at a capital cost of a third
of revenue, against attackers the filer says have *"greater financial and other resources ... such as the
possibility of receiving direct or indirect government subsidies."* **[E4-04] rules out the industry for the
certainty it precludes, not for the leader's current numbers**, and the price of this ruling if wrong is
recorded at [E3-47] rather than argued away.

### CLASS AND DIRECTION
- Needed or desired [x] · no close substitute [x] **at the leading edge, not at mature nodes** · not
  price-regulated [x]
- **Must the moat be continuously rebuilt? YES** (filer's own words; capex 1.10-2.53x depreciation every year;
  the Intel record for a lapse). **Does success depend on a great manager? No key-person dependence found
  [E4-23]**: the 20-F records C.C. Wei as *"CEO and Vice Chairman from June 2018 to June 2024"* and now Chairman and
  CEO, so the widening record spans two leadership arrangements; recorded, not a defect.
- Primary moat metric and trend: gross margin 48.7% → 59.9% (2015-2025), 67.7% in Q2 2026; **WIDENING**.
- **Class: POSITION DOMINANT, franchise class NONE under [E4-04] (a surfing run [E3-51]).** Direction of the
  position: widening.

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  *OUT on [E4-04], not on [E3-03]. TSMC passes the three franchise conditions at the leading edge on its
  customers' and its competitors' own filings, and passes [E3-43]'s return test; it fails [E2-44]'s second
  characteristic outright and falls in [E4-04]'s excluded class on its own description of its industry and on
  the capital it must spend to stay in position. The ten-year record is a surfing run at its best. The corpus
  tension (the 2022 purchase, the 2023 praise) is recorded above and flagged, not resolved.*
  **The file closes here. Q3 to Q6 are RECORDED, NOT GOVERNING.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — **RECORDED, NOT GOVERNING**
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

⛔ **Q2 closed the file (OUT on [E4-04]). Everything from here to Q6 is recorded because the queue's output
contract requires a price and because the evidence was gathered; none of it governs, and none of it can
reopen Q2 (the guardrail: "a strong Q3 cannot promote a name, repair Q2, or substitute for Q4").**

### STEP 1 — THE WEIGHT CASE, declared first
- [x] **Daily execution** **[E3-38, E3-43]**: Q2 found TSMC to be *"a business"*, not a franchise, in [E3-43]'s
  sense (*"a business earns exceptional profits only if it is the low-cost operator or if supply of its product
  or service is tight ... a business, unlike a franchise, can be killed by poor management"*). The decision
  that matters recurs every node: NT$1.27tn of capex in 2025, US$52-56bn guided for 2026, and a further
  US$29.4bn appropriated on 2026-08-11. **A wrong node bet is Intel's filed record.**
- [ ] **Control**: no; a minority owner can exit. [ ] **Leverage**: no (Q4).
- **Case declared: Q3 would be a BINARY GATE on the daily-execution determinant.** No price compensates a
  failure here **[E1-16, E3-29, E5-35]**.

### Honesty — the binary [E5-16], each matter dated to when it became PUBLIC
- **Export-control self-report (public in the FY2024 20-F, filed 2025-04-17, repeated FY2025):** *"In October
  2024, we notified relevant U.S. and Taiwan authorities that one type of our customer's chip manufactured by
  us might have been diverted to a restricted entity or incorporated into a restricted entity's product, and
  since then have been cooperating with the authorities' requests for additional information and
  documents."* **Read as the candor case [E2-68]**: the company holding the information advantage reported it
  and disclosed it in the annual report; no penalty is filed. **Open, carried to Q6.**
- **Legal proceedings (20-F Item 8):** one material matter, the Marlin/Longitude patent complaints at the ITC
  (instituted 2025-03-21); *"Other than the matter described above, we were not a party to any material
  litigation."* Ordinary course.
- **Insider conduct under the new filing class:** 42 Forms 3 from 2026-03-18 and 226 Forms 4 since (read in
  `form34_summary.json`): **220 purchase lines**, almost all small ESPP and LTI-trust purchases (footnotes:
  *"Common Shares purchased by the administrator of the issuer's Employee Stock Purchase Plan"*; *"purchased by
  a trust with cash received under the issuer's Long-Term Incentive ('LTI') Bonus Plan"*); **2 sales** (the
  largest 200,000 shares on 2026-05-19 at NT$2,210 by Chuang Tzu-Sou, holding 2,495,165 after) and gifts. **No
  pattern of material selling.**
- **No integrity disqualifier found. A Q3 pass is the absence of found disqualifiers, not a finding that the
  managers are honest [E5-17].** The corpus's own read of these managers (*"one of the best managed companies
  ... marvelous people"*, 2023 meeting) is recorded and **not used to score this gate** (the guardrail, and
  [E5-17]'s *"Sincerity and empathy can easily be faked"* cuts against leaning on anyone's impression,
  including Buffett's).

### STEP 2 — THE FLAGS
- [ ] **weak accounting [E4-22]**: no instance found. Equity-settled SBC is expensed (NT$1,246.1M in 2025);
  employee profit sharing (NT$103,073.0M for 2025) is expensed and paid in cash; a published reconciliation of
  Taiwan-IFRS to IASB-IFRS accompanies the 20-F (6-K 2026-04-16, *"net income attributable to shareholders of
  the parent of NT$1,717,883 million"* under Taiwan-IFRS). Depreciation of machinery over *"5 years"*, which is
  fast, not flattering.
- [ ] **unintelligible footnotes**: no. The investee table in the quarterly consolidated report even gives each
  overseas subsidiary's result (below).
- [x] **trumpeted projections [E4-22] third flag, and [E5-30]'s ratchet — FIRES as a prompt.** Quarterly
  guidance on revenue, gross margin and operating margin every quarter, and **a five-year target** in the Q4
  2025 deck (6-K 2026-01-15): *"From 2024 to 2029, management expects: Revenue CAGR to approach 25% in US dollar
  terms ▪ Long-term gross margin to be 56% and higher through the cycle ▪ ROE to be high-20s% through the
  cycle."* **[E3-48]'s remedy, applied: twelve quarters of guidance against outturn (Q3 2023 to Q2 2026) — revenue
  at or above the top of the range in all twelve; gross margin at or above the range in all twelve, above the
  top in seven; operating margin above the top in ten.** Never missed. The record is the opposite of
  make-the-numbers: the guidance is set low and beaten. **The flag stays a prompt, not a finding: a guidance
  culture this conservative is still a ratchet [E5-30], and a 25% five-year revenue CAGR is a growth
  expectation of exactly the kind [E4-35] puts at fewer than one in twenty.**
- [ ] **serial share issuance [E5-15]**: no. 25,932,364,992 shares against 25,932,524,521 at 2025-12-31; the only
  movement for years is RSA grants and reclaims in the low millions.
- [ ] **EBITDA promotion [E4-29]**: no. The word appears **once** in the FY2025 20-F, as a covenant in a subsidiary
  loan (*"the ratio of the Company's annual debt to earnings before interest, taxes, depreciation, and
  amortization (EBITDA) not to exceed a certain multiple"*), **zero times** in the twelve earnings decks and
  releases read, and once in the Q2 2026 consolidated report (the same covenant). The headline metrics are
  gross, operating and net margin, EPS and ROE, all GAAP-basis (Taiwan-IFRS).
- [ ] **filed-figure tells [E4-30]**: cash taxes as % of pretax income: 11.7% (2015) · 11.9 · 16.1 · 11.4 · 13.3 ·
  8.8 · 12.6 · 7.6 · 16.3 · 13.1 · **13.1% (2025)** — **not falling**; reported growth is not smooth (2019 +3.7%,
  2023 down 4.5%).

### STEP 3 — THE PRIMARY TEST [E2-01]
Return on average parent equity, from `row.py`: **24.2% (2017) · 23.0 · 21.6 · 29.6 · 29.7 · 39.3 · 26.9 · 30.2 ·
35.6% (2025)**, without leverage (Q4: net cash). Balance sheet first: equity attributable to the parent
NT$1,359bn (2016) → NT$5,420bn (2025) → NT$6,433bn (2026-06-30, Board 6-K). **High and rising on a quadrupled
base.**

**The half-owner test [E2-26]:** the reporting gives node mix, platform mix, geography, the two largest
customers' revenue, the capacity-reservation prepayments by year, the government grants by year, the currency
sensitivity, and each overseas subsidiary's result. **The positive pole.** The one thing an owner would want and
does not get: **gross margin by site (the overseas fabs' margin dilution)**, recorded sweep of the FY2025 20-F
and the twelve decks' text for "overseas fab" and "dilution": **no instance found**; it is given only on the
earnings calls, which are not on this project's shelf.

### Capital allocation — the overseas fabs, subsidies and dividends
- **TSMC Arizona** (Q2 2026 consolidated report, investee table, NT$ thousands): original investment
  **NT$759,561,260 thousand at 2026-06-30** (NT$672,616,510 thousand at 2025-12-31); **net income of the investee
  for H1 2026 NT$36,066,488 thousand**; TSMC purchased NT$84,003,238 thousand from it in the half. **About
  NT$36bn of half-year profit on NT$760bn invested: roughly 9-10% annualised on cost, before judging whether the
  intercompany price is at market.** **JASM**: investment NT$68.4bn, H1 2026 net income NT$1.68bn.
- **Government grants received**: NT$47.5bn (2023), NT$75.2bn (2024), NT$76.3bn (2025), NT$0.6bn (H1 2026); Note 30:
  *"The agreements include the construction timelines and other conditions that must be complied with"*; Item
  3.D: noncompliance *"could ... obligate us to repay all or a portion of amounts already received."* The CHIPS
  Act award is *"up to US$6.6 billion in total direct funding and up to US$5 billion of proposed loans"*; ESMC
  *"up to EUR5 billion state aid."*
- **Capex against depreciation**: 1.10x to 2.53x in every year 2015-2025, 2.16x on the trailing twelve months.
- **Dividends**: cash dividends paid NT$116.7bn (2015) → NT$466.8bn (2025); now NT$7.0 a quarter (~NT$726bn a year
  at the current count). **Funded by operations, not issuance [E2-52]**: net bond issuance 2025 +NT$32.6bn against
  NT$2,275bn of operating cash. Dividends 2021-2025 total NT$1,672.6bn against five-year capex-end owner earnings
  of ~NT$2,939bn (Q4): covered.
- **Buybacks [E5-08, E4-31]**: none beyond 3.2M shares for RSAs (2024). At a price above every conservative value
  in Q5, not buying back is rational, not the [E2-51] refusal.
- **The institutional imperative [E2-30]**: [ ] resists change; [ ] projects soak up funds (capex is customer-demand
  led on the filed prepayment and utilisation record); [ ] staff studies; **[x] peer imitation, as a prompt**: the US,
  Japanese and German fabs were built under incentive programs every competitor is also chasing, and the 20-F
  names the Section 232 investigation into semiconductor imports (Item 3.D). Whether Arizona is a return decision
  or a political one cannot be read from the filing; its H1 2026 profit above is the best filed evidence that it
  is not merely political.
- **[E3-66], where a minority shareholder stands**: Note 36(a): *"Under a technical cooperation agreement with
  Industrial Technology Research Institute, the R.O.C. Government or its designee approved by TSMC can use up to
  35 % of TSMC's capacity provided TSMC's outstanding commitments to its customers are not prejudiced ... the
  R.O.C. Government did not invoke such right."* The National Development Fund of the R.O.C. *"owned 6.38% of
  TSMC's outstanding shares as of February 28, 2026"* and *"has served as our director since our founding."*
  **The state stands in the queue ahead of capacity, by contract, on paper.** Recorded for Q4.

### Pay, and what it vests on [E4-27]
*(The brief cited [E4-27] for incentives, which is correct; [E4-52] is used only for converging prompts.)*
- **CEO C.C. Wei, 2025** (20-F Item 6): salary NT$17.3M, bonus (*"Included cash bonus and profit sharing bonus"*)
  NT$895.8M, stock awards NT$367.1M, other (*"Included LTI bonus plan"*) NT$1,142.5M, **total NT$2,422.7M
  (US$77.2M)**.
- **What it vests on**: employee profit sharing is set by the Articles at *"at least one percent of our annual
  profits"* (NT$103.1bn for 2025); executive RSAs vest on **TSMC's total shareholder return relative to the S&P
  500 IT Index** (*"Above the Index by X percentage points: 50% + X * 2.5%, with the maximum of 100%"*) with a
  ±10% ESG modifier; the LTI (from 2025) on *"company-level financial indicators, total shareholder return
  performance relative to a peer group and ESG achievements."*
- **The incentive read**: pay rises with **profits** and with **relative share price**. Neither is a return on the
  capital employed, and the business spends a third of revenue on capital. **[E3-50] prompt**: a relative-TSR
  vesting schedule points management at the stock price; [E4-27] says look first at what the incentive rewards,
  and here it rewards profit growth bought with capital and price outperformance, not return on the next node's
  capital. **A prompt, not a finding**: ROE has in fact risen.
- **Clawback**: *"the TSMC Clawback Policy in August 2023"* (Exhibit list). Present.

### Converging prompts [E4-52]
Three prompts point the same way: **a five-year growth target**, **profit- and TSR-based pay**, and **a capex
budget that grows with each guidance raise** (US$52-56bn for 2026, plus US$29.4bn more appropriated in August).
**Together they are one reinforcing system toward more capacity**, which is exactly [E2-58]'s mechanism if AI
demand turns (*"the rebound to prosperity frequently produces a pervasive enthusiasm for expansion that, within a
few years, again creates over-capacity"*). **Offsetting, on the record:** the 2023 downturn, where capex held at
1.82x depreciation and gross margin held at 54.4%, and the conservative guidance record.

### THE GUARDRAIL
- [x] Nothing in this Q3 is used to promote the name, repair Q2 or substitute for Q4 **[E2-37, E2-38, E3-39]**.
- [x] Key-person dependence: none found (Q2).
- [x] No great-manager thesis is being relied on.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary — no integrity disqualifier found** — with the
  guidance-culture prompt, the pay-on-price prompt and the capacity-enthusiasm convergence live. *IN never
  promotes, and this one cannot: Q2 is OUT.*

## Q4 — WILL IT SURVIVE? — **RECORDED, NOT GOVERNING**

### Owner earnings — the one number **[E2-23]**
**Construction (CONVENTION, framework VI): operating cash flow − equity-settled SBC − (c).** **One run-specific
adjustment, disclosed:** minus the year's change in customers' *"temporary receipts"* (*"payments made by
customers to the Company to retain the Company's capacity ... either by refund or by accounts receivable
offsetting"*, Note 22), because that cash is a customer advance, not earnings. Balances: 0 (2020) · NT$185,994.2M
(2021) · 276,122.8 · 278,294.6 · 291,101.8 · **189,858.2 (2025)** · 234,225.1 (2026-06-30). **Without it, 2021
operating cash is overstated by NT$186bn and 2025 understated by NT$101bn.**

**SBC: RESOLVES AND IS COMPLETE.** The cash-flow statement's *"Share-based compensation"* add-back is filed for
every year: none (2015-2018; the FY2017 statement carries no such line and the FY2020 statement shows "—" for
2018), 2.8 (2019), 6.6, 7.8, 302.4, 483.0, 1,242.7, **1,246.1 (2025)**, NT$ millions. **The rest of employee
equity-like pay is cash and already inside operating cash**: profit sharing (NT$103,073.0M for 2025, paid in cash,
*"Employees' cash profit sharing bonus"*), the cash-settled share-based payment plan (Note 28(b), a liability
remeasured through profit or loss), and the LTI (*"credited to a trust for the purchase of common shares"*, a cash
purchase). **[E3-70]'s market-value measure is immaterial here**: 2,353,000 RSA units granted in 2024 at a
weighted fair value of NT$662.42 is NT$1.56bn, 0.07% of 2025 operating cash.

**Maintenance capex, the central judgment — what the filing gives to make it, and what it does not.**
- **What it does not give:** no split of capex into maintenance and growth; *"maintenance"* appears in no capex
  disclosure. Item 4 lists the 2026 uses as capacity *"mainly for 2-nanometer and 3-nanometer nodes"*, specialty
  and advanced packaging, and R&D projects.
- **What it does give:** (1) machinery depreciated over *"5 years"*, so D&A turns over fast; (2) capex above
  depreciation in **every** year 2015-2025 (1.10x to 2.53x), **including 2023, when units fell 21% and capex was
  still 1.82x depreciation** — no volume growth was needed that year, and the spending continued because the
  next node had to be built; (3) Q2's finding that **holding competitive position means re-buying the leading
  node**, which is maintenance in [E2-23]'s own words (*"requires to fully maintain its long-term competitive
  position and its unit volume"*); (4) government grants that reduce the owner's cash cost (NT$76.3bn in 2025).
- **The case: [E5-20]'s exception class.** A business whose own filing says position depends on continuous
  technology leadership, whose capex has exceeded depreciation every year for eleven, and whose downturn year
  shows no retreat to depreciation, **is the class where "merely spending their depreciation expense will not
  keep them in the same place."** **The D&A end is INVALID** and is displayed only.
- **The two ends carried (the judgment band):**
  - **Capex end (conservative): total capex + intangibles − government grants**, i.e. treat all of it as
    required. Over-states (c) by whatever share is genuine volume growth (units 9.6M → 15.0M, 2016-2025).
  - **Judged end: 1.336 × D&A**, the capex-to-depreciation ratio of the three flattest revenue years on file
    (**2017-2019**: revenue +3.1%, +5.5%, +3.7%; net capex NT$1,121.5bn against D&A NT$839.6bn), when volume growth
    was small and node migration (10nm, 7nm) continued. **A guess, stated as one [E2-23]: "(c) must be a guess."**
    It under-states (c) if tool cost per wafer has risen faster since 2019 (EUV at 3nm and 2nm) than in 2017-2019.

**Owner earnings by year, NT$ millions** (`oe.py` / `oe_out.json`):

| year | OCF | − SBC | − Δ temp. receipts | net capex | D&A | **OE, capex end** | **OE, judged end** | OE, D&A end (INVALID) | capex/D&A |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 539,835 | 0 | 0 | 330,751 | 223,828 | 209,083 | 240,857 | 316,006 | 1.48 |
| 2017 | 585,318 | 0 | 0 | 332,437 | 260,143 | 252,881 | 237,834 | 325,175 | 1.28 |
| 2018 | 573,954 | 0 | 0 | 322,682 | 292,546 | 251,272 | 183,187 | 281,408 | 1.10 |
| 2019 | 615,139 | 3 | 0 | 466,336 | 286,884 | 148,800 | 231,932 | 328,252 | 1.63 |
| 2020 | 822,666 | 7 | 0 | 515,711 | 331,725 | 306,948 | 379,560 | 490,935 | 1.55 |
| 2021 | 1,112,161 | 8 | 185,994 | 847,408 | 422,395 | **78,750** | 361,947 | 503,764 | 2.01 |
| 2022 | 1,610,599 | 302 | 90,129 | 1,082,575 | 437,254 | 437,593 | 936,108 | 1,082,914 | 2.48 |
| 2023 | 1,241,967 | 483 | 2,172 | 907,789 | 532,191 | 331,523 | 528,441 | 707,122 | 1.71 |
| 2024 | 1,826,177 | 1,243 | 12,807 | 889,718 | 662,797 | 922,409 | 926,800 | 1,149,331 | 1.34 |
| 2025 | 2,274,976 | 1,246 | **−101,244** | 1,206,299 | 688,096 | **1,168,675** | **1,455,852** | 1,686,877 | 1.75 |
| TTM 2026-06 | 2,634,679 | 683 | 12,310 | 1,490,809 | 688,888 | 1,130,877 | 1,701,507 | 1,932,798 | 2.16 |

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25, E4-38]:**

| window | OE, capex end | OE, judged end | D&A end (INVALID, display) |
|---|---|---|---|
| **5-yr 2021-2025 (the default [E2-42])** | **587,790** | **841,830** | 1,026,001 |
| 10-yr 2016-2025 | 410,793 | 548,252 | 687,178 |
| 3-yr 2023-2025 | 807,536 | 970,364 | 1,181,110 |
| prior 5-yr 2016-2020 | 233,797 | 254,674 | 348,355 |
| TTM to 2026-06-30 (display; one year is not [E2-23]'s "average annual amount") | 1,130,877 | 1,701,507 | 1,932,798 |

- **Combined range, valid windows × valid ends: NT$411bn to NT$970bn a year** (10-yr capex end to 3-yr judged
  end), **NT$588-842bn on the five-year default.** Net interest after tax adds NT$19-49bn by window (interest
  received sits in investing activities, so operating cash excludes it; the cap includes the cash that earns it).
- **Is the range too wide to reach a conclusion?** Nearly so as a level (2.4x end to end), **but not for the only
  decision it feeds**: every valid construction yields under 1.6% on the cap (Q5), so the width cannot change
  the price verdict. Recorded, not resolved by preference.
- **The distorted years, named [E5-11, E4-41]:** **2021** (the prepayment inflow and the 7nm/5nm capacity build:
  capex-end OE only NT$78.8bn); **2023** (the downturn); **2025 and 2026, a favourable exogenous break**: HPC
  revenue +48% on AI demand and gross margin above every prior year. [E4-41] says normalize the mean down for luck
  before trusting it; the TTM figure is shown and not used as the base for that reason.
- **Growth record, for Q5:** judged-end OE compounded **22.1% a year 2016-2025**; the three-year capex-end mean
  compounded 19.1% a year between 2016-18 and 2023-25; revenue 16.3% a year 2015-2025 (NT$).

### Great, good, or gruesome? **[E4-20]**
- [ ] great · [x] **good** · [ ] gruesome
- **Evidence:** it *"pays an attractive rate of interest that will be earned also on deposits that are added"*:
  ROE 21.6-39.3% while equity quadrupled, with each year's added capital (capex 1.1-2.5x depreciation) earning at
  the same or higher rates. **Not great**, because great requires little added capital, and TSMC reinvests a third
  of revenue. **[E4-43]: the good class passes Q4; it ranks below great at Q5, and that is all.**

### Staying power — score all three **[E5-11]**. The balance sheet is strong, stated first.
- **(1) A large and reliable stream of earnings: YES, large; reliable within a cycle.** Operating cash never below
  NT$529.9bn in eleven years; the worst drawdown (2023) was −22.9% on operating cash with profit still NT$851bn.
- **(2) Massive liquid assets: YES.** Cash and marketable securities **NT$3,518.01bn** at 2026-06-30 (37.5% of total
  assets; Q2 2026 deck), against long-term interest-bearing debt NT$864.27bn: **net cash about NT$2.65tn.**
- **(3) No significant near-term cash requirements: THE LARGEST IN THE QUEUE IN ABSOLUTE TERMS, AND COVERED.**
  20-F contractual obligations at 2025-12-31, less than one year: **capital purchase obligations NT$1,220,393M**,
  long-term debt NT$156,822M, temporary receipts NT$146,559M, leases NT$4,381M: **NT$1,528bn**, plus dividends at
  ~NT$726bn a year. **Total ~NT$2.25tn against NT$3.5tn of liquid assets and ~NT$2.6tn of trailing operating cash.
  Covered roughly 2.7x by the two together.** A 2023-shaped year (operating cash −23%) does not break it.
- **Leverage, named and quantified [E4-16]:** net cash; interest paid NT$19.1bn in 2025 against operating cash
  less capex of ~NT$1,000bn, **~52x coverage [E2-54]**. Guarantees to TSMC Arizona outstanding NT$346.9bn and to
  TSMC Global NT$170.9bn (August 2026 revenue report), intra-group. **Covenants** exist on one subsidiary loan
  (Note 19, the EBITDA multiple); **the parent's bonds are plain NT$ bullets** (e.g. *"115-3 ... NT$14.0 ... 2.03%
  ... Bullet repayment"*, July 2026 month-end report).

### Name the specific way THIS business dies **[E2-27, E3-24]** — exposure, not experience **[E4-40]**
**1. THE ADDRESS — the dominant exposure, and the corpus's own reason for leaving.**
- **Mechanism:** the plant that earns the premium is in one place a foreign power disputes. 20-F Note 38:
  **noncurrent assets NT$3,102,343.0M in Taiwan, 80.0% of the total**; Item 3.D: *"The majority of our principal
  executive officers and our principal production facilities are located in the R.O.C., and the majority of our
  net revenue is derived from our operations in the R.O.C."*; the risk named: *"military conflicts, the risk of
  outbreak of war or hostilities."* **The filing's only direct reference to cross-strait relations is about the
  share price** (*"the financial markets have viewed certain past developments in relations between the R.O.C. and
  the P.R.C. as occasions to depress general market prices"*), unchanged in substance since the FY2017 20-F.
- **Quantified from filed figures:** if Taiwan output stopped, what remains is the 20% of noncurrent assets
  outside Taiwan: United States NT$540.1bn, Japan NT$117.4bn, China NT$65.0bn, EMEA NT$51.5bn. TSMC Arizona earned
  NT$36.1bn in H1 2026 (investee table). **Against a cap of NT$62.5tn, the non-Taiwan earning base on file is on
  the order of NT$70-100bn a year (Arizona annualised, JASM small, Nanjing not separated): about 0.1-0.2% of the
  cap.** The liquid assets (NT$3.5tn) are the owner's buffer only to the extent they are held and accessible
  outside Taiwan; the filing does not give their location. **Separately, and by contract, the R.O.C. Government
  may use up to 35% of capacity (Note 36(a)).**
- **The corpus, on this exact exposure** (`Annual Meetings/2023 Annual Meeting.txt`, transcript): *"I don't like
  its location. And I've reevaluated that. I mean, I don't think it should be any place but Taiwan, although they
  will be, obviously, opening up chip capacity in this country."* ... *"I feel better about the capital that we've
  got deployed in Japan than Taiwan. I wish it weren't so, but I think that's the reality. And I've reevaluated
  that in the light of certain things that were going on."* The exit was the **[E2-40]** crystallized-view sale
  (*"sold almost the entire position within a few short months"*), and the ground was **[E3-66]**'s jurisdiction
  factor that *"doesn't lose share of force just because some 'expert' can better measure other types of force."*
- **Likelihood: NOT STATABLE FROM ANY DOCUMENT.** The vocabulary requires one of *likely / a real possibility /
  a low-level possibility* **[E3-24]**. No filing, no corpus passage and no document this run can name assigns a
  probability to a cross-strait conflict; Buffett's own answer states a preference and a reevaluation, not a
  likelihood. **Can I name the document that would resolve it? No.** **So this mechanism, were Q4 governing,
  would return UNKNOWABLE, not IN**: the mechanism is named and quantified, and the one number the corpus requires
  (the likelihood) cannot be supplied without writing an opinion.

**2. THE SURFER FALLS OFF — [E4-04]'s mechanism.** A node lost to Samsung or Intel. **Quantified:** advanced nodes
were 77% of Q2 2026 wafer revenue; on Intel's filed path the gross margin moved 26 points in nine years, and on the
row's filed ranges a foundry without the leading edge earns UMC's 29.0% or GlobalFoundries' 24.9% gross margin
against TSMC's 59.9%. **Likelihood: a real possibility over a decade**, on Intel's filed record, and **a
low-level possibility within any two-year node**, on TSMC's filed record of five consecutive transitions.

**3. THE CAPACITY WAVE BREAKS — [E2-58], [E2-27].** Two customers are 36% of revenue, HPC is 58%, capex guidance
rises with demand, and capital purchase obligations were NT$1.53tn at 2025-12-31. **Quantified on the one filed
analogue:** in 2023 units fell 21%, operating cash fell 23% and capex-end owner earnings fell from NT$437.6bn to
NT$331.5bn; the company stayed highly profitable. A worse break in a larger plant would compress owner earnings
toward the 10-year mean (NT$411-548bn) from a NT$1.1-1.7tn trailing level. **The company survives it; the owner's
return does not survive a purchase at a price built on the trailing level.** **Likelihood: a real possibility.**

**4. THE DOLLAR.** *"every 1% depreciation of the U.S. dollar against the NT dollar would result in an approximately
0.3 percentage point decrease in our operating margin."* A 10% NT$ appreciation costs ~3 points of operating
margin. **A low-level possibility of mattering to survival; a likely source of volatility.**

**THE SURVIVAL SHAPE — A TWELFTH: THE ADDRESS.** Checked against all eleven (ORCL, ARM, BE, BA, SWK,
ACVA/FLNC/NEGG with the treadmill and pendulum variants, CNR, RGTI, BAM's WAREHOUSE, SONY's CAMOUFLAGE, TM's
PASS-THROUGH). **None fits.** Nothing is contracted not to stop beyond ordinary purchase commitments (not ORCL); pay
does not eat the cash (not ARM); the history is long (not BE or RGTI); no cash undoes past work (not BA); the
distribution is covered (not SWK); no one else's balance sheet is borrowed (not ACVA); there is no long tail (not
CNR); no warehouse (not BAM); nothing is camouflaged (the overseas subsidiaries' results are published, not SONY);
and **the savings do not pass through** (margins rose through the capex race, the opposite of TM). **THE ADDRESS:
a business that wins its race, keeps its gains and is financially impregnable, whose earning plant sits at one
address inside a disputed jurisdiction. The death is not in the accounts; the accounts show only where the assets
are. The likelihood cannot be read from any document, so the file cannot assign one.** **The register would stand
at TWELVE.**

- **VERDICT (RECORDED, NOT GOVERNING): [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [x] UNKNOWABLE** → *on mechanism 1: named
  and quantified, likelihood unstatable from any document. On mechanisms 2-4 alone, and on the three strengths,
  Q4 would read IN (good, not great; net cash; near-term requirements covered ~2.7x).*

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 is OUT (and Q4, recorded, would be UNKNOWABLE). What follows
is arithmetic the queue's output contract requires (a price from every run), headed as operator rule 3 requires.

---
## Q5 — **COMPUTATION — NOT A CLEARANCE**

**This section contains no entry language and confers no clearance. It is arithmetic.**

**The floor first [E4-28]:** *"that's the figure we quit on ... we don't want to buy equities where our real
expectancy is below 10 percent. Now, that's true whether short rates are 6 percent or whether short rates are 1
percent."* Two sovereigns are shown (Step 0); **the floor governs above both, and the choice between them moves
nothing below.**

**1. THE YIELD** — owner earnings ÷ cap of **NT$62,497bn** (TWSE NT$2,410 × 25,932,364,992), `q5.py`:

| construction | OE NT$bn | yield | vs TWD 30-yr 1.89% | vs USD 30-yr 5.35% | perpetual growth needed for 10% |
|---|---|---|---|---|---|
| 10-yr capex end | 411 | 0.66% | −1.23 | −4.69 | 9.3% |
| 10-yr judged end | 548 | 0.88% | −1.01 | −4.47 | 9.0% |
| **5-yr capex end** | **588** | **0.94%** | −0.95 | −4.41 | **9.0%** |
| **5-yr judged end** | **842** | **1.35%** | −0.54 | −4.00 | **8.5%** |
| 3-yr capex end | 808 | 1.29% | −0.59 | −4.06 | 8.6% |
| 3-yr judged end | 970 | 1.55% | −0.33 | −3.80 | 8.3% |
| TTM capex end (display) | 1,131 | 1.81% | −0.08 | −3.54 | 8.0% |
| TTM judged end (display; [E4-41] luck not removed) | 1,702 | 2.72% | +0.84 | −2.63 | 7.1% |
| 5-yr D&A end (INVALID, display) | 1,026 | 1.64% | −0.24 | −3.71 | 8.2% |

- Net interest after tax (NT$19-49bn by window) adds **0.03-0.08 points**. **On the ADR quote** (~12% premium) every
  yield is ~11% lower.
- **Every valid construction yields below the Taiwan 30-year bond.** Only the trailing twelve months at the judged
  end, the single best year on file and inside the AI boom, clears it, by 0.84 points.

**2. WHAT THE PRICE ALREADY ASSUMES**
- **Perpetual growth needed to reach 10%: 8.5-9.3% a year on the five- and ten-year means; 7.1% from the best trailing
  year.** In a staged engine (10 years of growth, then 3%, discounted at 10%; it casts no vote [E3-34]):

| base | NT$ per share, zero growth | 10 yrs at 10% | 10 yrs at 15% | 10 yrs at 20% |
|---|---|---|---|---|
| 5-yr capex end | 227 | 560 | 812 | 1,173 |
| 5-yr judged end | 325 | 802 | 1,163 | 1,681 |
| 3-yr judged end | 374 | 925 | 1,341 | 1,937 |
| TTM judged end | 656 | 1,622 | 2,351 | **3,397** |

- **What the business has actually done:** judged-end owner earnings +22.1% a year 2016-2025; revenue +16.3% a year
  2015-2025 (NT$); management's own target *"Revenue CAGR to approach 25% in US dollar terms"* for 2024-2029.
- **In words: at NT$2,410 the buyer is paying for the best trailing twelve months the company has ever filed to keep
  compounding at ~15-20% a year for a decade, with the Taiwan address carried at no cost.** From any multi-year mean
  the same price needs ~20%+ for a decade. **[E4-35]:** *"fewer than 10 of the 200 most profitable companies ...
  will attain 15% annual growth in earnings-per-share over the next 20 years."* TSMC has done it for a decade; the
  price requires it to do it again from a base four times larger, through an [E4-04] industry. **[E4-44]'s bound:**
  the value cannot grow faster than the earnings over the long term, so the whole case is the earnings path.

**3. WHAT YOU ARE PAID**
- **Points over the sovereign: −0.3 to −1.2 against the TWD bond on the valid means (−3.8 to −4.7 against the USD
  bond).** The buyer is paid less than the Taiwan government pays, before growth.

### THE PRICE — THE VALUE AS A ROUND-NUMBER RANGE [E4-01]
- **At the ~10% floor, on the valid multi-year bases (5-yr and 3-yr, capex and judged ends), with 10-15% growth for
  ten years: roughly NT$550-1,350 a share.** Stretched to 20% for ten years: up to ~NT$1,950. **From the single best
  trailing year with 15-20% for ten years: NT$2,350-3,400.**
- **Current price NT$2,410 (TWSE, 2026-09-11).** **Above the entire range built on any multi-year window**; inside
  only the range built on the best trailing year plus a decade of 15%+ growth.
- **Screamer test [E4-01], stated for the record only:** the price is not below the conservative case; it is above
  every conservative case by 2-4x. **Windage count: one** (the conservative-end (c) at the capex end; the growth
  cases are shown, not haircut; the discount rate is the floor, not a premium [E3-42]).
- **Verdict line: the file is closed at Q2; the price would also fail the floor.** No ranking position.

## Q6 — **COMPUTATION — NOT A CLEARANCE.** WHAT WOULD PROVE THIS FILE WRONG, PRE-COMMITTED [E1-02]
**No holding exists and nothing is armed.** Recorded, in words, are the conditions under which a later run should
reopen Q2 or Q4, set before any price moves them **[E1-02]**:
- **Reopen Q2 [E4-04] only on a written case, approved by the operator (prime rule 5)** that the corpus scopes
  leading-edge foundry manufacturing out of the "rapid and continuous change" class, **or** on filed evidence that
  TSMC's premium is earned on something that does not have to be re-bought each node (for example, the mature-node
  and packaging share of gross profit rising while leading-edge capex falls toward depreciation for a full node
  cycle). **The 2023-meeting tension recorded at Q2 is the natural subject of that written case.**
- **Q2 would move toward NONE on position** (monitoring **[E4-32], [E4-55]**): a leading-edge customer filing that
  moves a named share of its wafers away (Broadcom's *"approximately 95%"* falling; AMD's *"all wafers ... at 7
  nanometer (nm) or smaller"* qualified by a second source); gross margin below the top of its guided range for
  two consecutive quarters; Intel Foundry or Samsung Foundry disclosing a positive foundry operating margin with
  external revenue.
- **Q4 would move off UNKNOWABLE** only with a document that bears on the address risk itself: a materially
  different geographic split of noncurrent assets (Taiwan below ~50%), or a filed change in the R.O.C.
  capacity-use clause. **No document assigns a probability to a cross-strait conflict, and none is expected.**
- **Q3 prompts to re-read:** the export-control self-report's outcome; the next five-year target and whether it is
  revised after a miss; any change in the RSA/LTI vesting basis.
- **The price condition, for orientation only:** the multi-year floor range sits around NT$550-1,350 a share; a
  price inside it would still meet a closed Q2. **Price appreciation and holding period are rejected as reasons
  [E2-28].**

- **VERDICT: NOT OPENED — no holding exists. [E2-40]'s fast-exit doctrine is the corpus's own action on this name
  (2022-2023) and is recorded at Q4, not armed here.**

---
## SELF-AUDIT (operator rule 6)
- [x] Questions answered in order; the file stopped at Q2 (OUT); Q3-Q6 recorded under explicit banners.
- [x] No question marked IN carries an "unverified" or "provisional" caveat. **Q1 IN** rests on the filed tables;
  **Q3 IN (recorded)** is the absence of disqualifiers, worded as such.
- [x] No UNRESEARCHED verdict issued. The Samsung and SMIC competitor gaps are UNKNOWABLE from the shelf (no SEC
  filing exists; Samsung's own English release gives no foundry figure), recorded, and stated not to widen the class.
- [x] The UNKNOWABLE verdict (Q4, recorded) states what cannot be known: the likelihood of a cross-strait conflict.
- [x] Step 0: the 20-F read with accession `0001628280-26-025362`; operating cash 2024 cross-checked to
  `companyfacts`; revenue 2025 cross-checked to the Board 6-K.
- [x] Owner earnings on multi-year means (5-yr default, 10-yr, 3-yr), window stated, capex band disclosed as a
  judgment, the D&A end marked INVALID under [E5-20], SBC resolved and complete, the prepayment adjustment disclosed.
- [x] Competitor row filled for 3 of 5 named competitors on the same metric and window, limits stated.
- [x] Sovereign for the earnings currency: **TWD, issuing authority's auction (CBC for the MOF, 2026-05-26) and the
  official exchange curve (TPEx, 2026-09-11)**, tenor 30 years, dated; USD shown beside it. **Not added to
  `tools/sources.py`.**
- [x] Value as a round-number range; one bar (screamer, for the record) with windage count one.
- [x] Prices dated; Yahoo used for live quotes only and flagged; FX from the CBC.
- [x] Every ledger id cited was checked against `principle_ledger.csv` before use (E1-02 through E5-43 as used).
- [x] Run committed to git by pathspec after each section.

**Errors of my own caught before commit, recorded:**
1. **I first wrote that gross margin beat the top of guidance in "every one of eleven quarters".** Re-read
   against the decks: it was at or above the range in all twelve and **above the top in seven**; corrected before
   the Q2 commit.
2. **I first cited receivables concentration as Note 35 with the sentence cut off at "93 % and".** Note 35 is
   Pledged Assets; the sentence is in Note 33 and reads *"93 % and 84 % of accounts receivable"*; corrected in
   the run file before the Q3-Q6 commit.
3. **I first wrote "units took until Q3 2025 to pass the 2022 peak".** The decks give only Q3 and Q4 2022; the
   2022 peak quarter is not on disk; reworded to the Q3 2022 figure before the Q1 commit.
4. **A bash heredoc with apostrophes failed** writing Step 0 (the brief warned); rewritten through the Write tool.
5. **I first built the GlobalFoundries series on `us-gaap` tags** and got nothing; GFS files IFRS; re-run on
   `ifrs-full`.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business, at Q2)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** TSMC passes every franchise condition at the leading edge on its customers' and its competitors'
  own filings and earns the best margins and returns in its row, widening through five node transitions, and fails
  Q2 on [E4-04]: its own 20-F describes an industry of *"rapid technological changes"* in which position depends on
  continuous leadership, bought with capex above depreciation in every year; recorded beneath the close, Q3 finds no
  disqualifier, Q4 would be UNKNOWABLE on THE ADDRESS (80% of the plant in Taiwan, the corpus's own exit reason),
  and the price (NT$2,410) sits above every multi-year floor range.

---
# THE OUTPUT CONTRACT

## (a) THE PRICE — **COMPUTATION — NOT A CLEARANCE** (operator rule 3)
**NT$2,410** (TWSE 2330 close, 2026-09-11, Yahoo, aggregator flagged; NYSE ADR US$433.24 the same day, **1 ADS = 5
shares** per the 20-F, a **~10-14% premium** at the CBC's NT$31.638) × **25,932,364,992 shares** = cap
**NT$62,497bn** (~US$1,975bn for orientation). Yield **0.66-1.55%** on valid multi-year owner earnings
(**0.94-1.35% on the five-year default**) against the **TWD 30-year 1.89%** (TPEx, 2026-09-11; CBC auction 1.814%,
2026-05-26) and the **USD 30-year 5.35%**; **floor range roughly NT$550-1,350 a share** on multi-year bases with
10-15% growth for a decade; **price above the whole range.**

## (b) PASS / FAIL
# **FAIL — the file was closed by QUESTION 2 (OUT on [E4-04]).**

### DEFECTS IN THE BRIEF
1. **The brief's pre-check facts all confirmed**: 20-F accession and date, the 6-K of 2026-09-10, no deal or name
   change. **One clarification:** the cause of the triage skip was, again, the newest 20-F not in `companyfacts`
   (fourth in a row, after SONY, TM and HMC), not a short history; TSMC has ten `ifrs-full` years.
2. **The brief framed the Taiwan sovereign's source as "the Central Bank ... or the Ministry of Finance, or the
   Taipei Exchange's official government bond yield curve if that is the published authority source."** Found:
   the MOF issues, the **CBC runs the auctions "on behalf of the Ministry of Finance"** and publishes the results
   (the issuing-authority print, but only on auction days), and **TPEx publishes the daily curve** (an exchange,
   one rung down). **Both are needed for a dated issuing-authority-anchored rate**; the run records both.
3. **The brief did not mention the corpus's own transaction in this name** (the 2023 meeting, section 26). It is
   the single most relevant corpus passage for Q2 and Q4 and is now recorded at both. Not a defect of the brief's
   instructions; a gap worth adding to future briefs for any name Berkshire has owned.

### TOOLING AND DOCUMENT DEFECTS FOUND
1. **`companyfacts` has not ingested the FY2025 20-F** (filed under a new agent prefix, `0001628280`). Fourth
   consecutive 20-F filer with the newest year missing (SONY, TM, HMC, TSM). **Source limit, not a tool bug**; the 20-F was read by hand.
2. **`tools/sources.py` has no TWD sovereign.** Left alone as instructed. The by-hand method (CBC auction page +
   TPEx `govDaily2` POST with `date=YYYY/MM/DD&fileCode=Curve&response=json`, then the dated `.xls`) is recorded in
   Step 0 so the next Taiwan filer (UMC is next in wave 5) can repeat it in minutes.
3. **`cover_shares.py` cannot see a 6-K count** (known limit). TSMC's count was derived from a dividend-per-share
   adjustment 6-K, a method worth reusing for Taiwanese filers that publish these adjustments.
4. **The 2025 Q2 deck (`a2q25presentatione_6kxwm.htm`) strips to 80 characters** (image-only); guidance for that
   quarter was read from the Q1 2025 release.
5. **The framework and the corpus disagree on a named company, flagged for the operator (prime rule 2):** [E4-04]
   as the framework scopes it excludes leading-edge manufacturing (INTC, SONY I&SS, now TSMC), while the corpus
   authors bought TSMC in 2022 and left for location, not franchise, reasons. **Not resolved here; a structural
   question needing a written case (prime rule 5).**


---
## ADDENDUM 2026-09-20 - Q2 re-read under the corpus ruling on [E4-04]: UNKNOWABLE, not OUT on the business
*Operator rule 6: corrected here, not by editing the text above. The ruling is in `Framework/THE FRAMEWORK v4.md`, Q2, "The verdict form [E4-04] takes", with its rows E2-75, E3-72 to E3-75, E4-57, E4-58 and E5-51 to E5-53; the case is `Framework/v4/RULING CASE 2026-09-20 ...`.*

**What this file found stands.** TSMC passes [E3-03] on its customers own filings; capex ran 1.10 to 2.53 times depreciation in every filed year; the filer says it must "remain technologically ahead" to keep its position; and its share and margin held through five node transitions (gross margin 48.7% to 59.9%, 54.4% in the 2023 downturn). **What changes is the verdict those facts support.** The corpus applies [E4-04] as a competence limit, not a fourth franchise criterion [E4-57, E4-58, E3-72]; the unit of the test is the company [E4-08]; and the one TSMC passage on the shelf rates the business at the top of its industry with a twenty-year horizon and sells it on location alone [E5-53]. The question the rule then asks is whether the advantage is **rebuilt from zero** each generation or **maintained**: this file carries evidence for both readings (a lead re-won each node, and a lead that has never been lost across five nodes), and cannot settle it from filings. **That is the perimeter case exactly: Q2 is UNKNOWABLE, closed without prejudice, not OUT on the business.**

**And the sequence would close the file at Q4 either way.** Had Q2 read IN, Q3 was recorded IN and Q4 was recorded UNKNOWABLE on the twelfth shape, THE ADDRESS, whose likelihood no document states. That is the reason the corpus itself gives for the sale: "I don't like its location" [E5-53]. The price computation is unchanged and remains headed COMPUTATION - NOT A CLEARANCE; no band is armed.

**Pass/fail line as re-read: FAIL, closed at Q2 UNKNOWABLE (without prejudice), with Q4 UNKNOWABLE on location recorded beneath it.**

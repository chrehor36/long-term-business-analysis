# Company Run — CORE NATURAL RESOURCES, INC. (CNR) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*Run opened 2026-09-13. CNR was carried in the tier-2 roster **unpriced on a PERIMETER guard**:
Core Natural Resources is CONSOL Energy combined with Arch Resources in an all-stock merger,
and the share count is ~1.69x its level two years earlier. The screen row is therefore not
used; every owner-earnings figure in this file is rebuilt from the two companies' own filed
cash-flow statements. Sovereign, price and share count are struck fresh here (operator rule
5). Every gate is open; no gate was briefed as short. Research folder:
`Test Runs/_research 2026-09-13 CNR/` (filing dumps pattern-ignored; the scripts that fetched
and flattened them are kept).*

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

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- **rate 5.35%** · **date 2026-09-11** · source: **US Treasury daily par yield curve, 30-year,
  from the issuing authority**, struck 2026-09-13 via `tools/sources.py:sovereign("USD")`, which
  returned `(5.35, '09/11/2026', 'US Treasury daily par yield curve')` — the Treasury rung, not
  the FRED fallback. 2026-09-12 and 09-13 are a weekend, so the 09/11 print is the currently
  observed rate. Read fresh, not inherited; it agrees with the brief.
- **Earnings currency: USD.** Core reports in dollars. More than half of coal revenue is
  EXPORT (FY2025: $2,308.2M of $4,129.5M, 55.9%, 10-K Note 3), but the filing's revenue table
  and its sales contracts are stated in dollars; the currency exposure is a price exposure
  (seaborne benchmarks), not a translation one. **No FX conversion; no ADR** — a Delaware
  corporation listed on the NYSE.

**THE SHARE COUNT — 49,636,257, CONFIRMED OFF THE COVER.**
- `python Screens/cover_shares.py CNR` → *"10-Q filed 2026-08-06, period 2026-06-30, accession
  0001710366-26-000054 · Common Stock, $0.01 par value 49,636,257"*. **Confirmed by reading the
  cover of the filed document itself**: *"Core Natural Resources, Inc. had 49,636,257 shares of
  common stock, $0.01 par value, outstanding at July 31, 2026."* One class; no preferred issued.
- Weighted-average basic shares, Q2 2026: 50,426,638; diluted 50,468,153 (10-Q, EPS note). The
  cover sits 1.6% below the quarter's weighted average because the buyback continued into July.

**PRICE AND CAP.**
- **Price $97.47**, close of **2026-09-11** (aggregator via `tools/sources.py:price`, **flagged**
  — operator rule 5, live quotes only).
- **Cap = 49,636,257 × $97.47 = $4,838.0M.**
- `tools/run.py CNR` reproduces the same cap ($4.84B on 49.6M shares) — and then **commits the
  exact perimeter error the queue guard refused**: its three-year window divides standalone
  CONSOL FY2023 and FY2024 plus combined Core FY2025 by the combined cap, and prints a yield of
  3.44%–6.58%. **That output is not used anywhere in this file.** Recorded as a tooling defect:
  the perimeter guard lives in the queue regeneration, not in `run.py`.
- **A second stale-row defect, found reading the older queue:** `Screens/2026-09-01 MASTER RUN
  QUEUE.csv` names the CNR row **"Cornerstone Building Brand · Silver Ores"** — a stale ticker-to-name
  mapping: neither the name nor the industry is Core's.
  The 2026-09-02 corrected queue carries no CNR row at all (unpriced). Neither row is used.

**THE MERGER — the perimeter this whole file turns on.**
- **Close date: 2025-01-14.** 8-K filed 2025-01-15, accession `0001193125-25-007135`, Item 2.01:
  *"On January 14, 2025 (the "Closing Date"), Core Natural Resources, Inc. (formerly known as
  CONSOL Energy Inc.) … completed its previously announced merger of equals transaction with
  Arch Resources, Inc."* Merger agreement dated **2024-08-20**.
- **Exchange ratio: 1.326.** Same 8-K: each Arch share *"was automatically converted into the
  right to receive 1.326 shares of common stock … (the "Exchange Ratio")"*. Arch RSUs and PSUs
  fully vested at the Effective Time (PSUs at the greater of target or actual) and converted at
  the same ratio; CONSOL's own RSUs and PSUs also fully vested.
- **Accounting acquirer: CONSOL.** FY2025 10-K Note 2: *"the Company issued 24.3 million shares
  of its common stock, which represents approximately 45 % of the issued and outstanding shares
  … the equity portion of the purchase consideration was $ 2,481,368"* (thousands); total
  consideration **$2,577.0M** including the $95.6M effective settlement of the Arch tax-exempt
  bonds CONSOL bought the day before closing. **Purchase accounting stepped Arch's PP&E up by
  ~$1.4bn** (Note 2), which is why FY2025 D&A is **$621.1M against $223.5M** for standalone
  CONSOL in FY2024 — a fact that matters at (c).
- **No divestiture was required.** S-4/A: *"The waiting period with respect to the notification
  and report forms filed under the HSR Act expired at 11:59 p.m. Eastern Time on October 11,
  2024"*; Brazil, Poland and China cleared by 2024-10-17. **A divestiture WAS contemplated — in
  the rival bid Arch rejected**: *"Company B shared a draft merger agreement … [that] contemplated
  that Arch would negotiate a divestiture of certain assets ahead of signing in order to address
  the regulatory concerns"*, and Arch's board chose CONSOL as posing *"significantly less risk and
  uncertainty"* (S-4/A, Background of the Merger). So the perimeter is the two companies whole;
  the only pre-closing transaction was the bond purchase above.
- **The company's own pro forma, OPENED rather than trusted by filename.** The **8-K/A filed
  2025-02-18, accession `0001193125-25-028132`**, is the real Item 9.01(b) pro forma — its
  explanatory note: *"This Amendment No. 1 … is being filed by the Company to include the
  financial statements of Arch and the pro forma financial information required under Items
  9.01(a) and 9.01(b)"*. **But it contains no statements of its own**: EX-99.1 incorporates Arch's
  FY2023 10-K Item 8, EX-99.2 Arch's Q3 2024 10-Q, and EX-99.3 *"the information under the caption
  'Unaudited Pro Forma Condensed Combined Financial Information' of CONSOL's Amendment No. 1 to
  Registration Statement on Form S-4 filed on November 18, 2024"*. So the pro forma was read at
  its source: **S-4/A, accession `0001193125-24-261026`**, which carries a combined **income
  statement** (FY2023 and 9M2024) and **balance sheet** (2024-09-30) — **and no combined
  cash-flow statement.** The S-4/A's list of what it presents has none. That absence decides the
  method in Q4: the pro forma owner earnings below are built by adding the two companies' own
  audited cash-flow statements, line by line, and reconciled to the filed pro forma where a line
  exists to reconcile to.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Anchor annual: Form 10-K, FY ended 2025-12-31, filed 2026-02-17, accession
  `0001710366-26-000007`** (`cnr-20251231.htm`). Read: Item 1 (business, mining complexes,
  marketing, competition, regulation), Item 1A, Item 2 (properties, reserves and production),
  Item 7 MD&A with the segment cost and price tables, the four statements, and the notes on the
  merger, revenue, inventories, PP&E, the Leer South event, income taxes, debt, pension and OPEB,
  coal workers' pneumoconiosis, workers' compensation, asset retirement obligations, commitments
  and contingencies, SBC, segments and the capital-return program.
  **10-K/A filed 2026-02-27, accession `0001710366-26-000009`** — opened: it refiles the S-K 1300
  technical report summary (EX-96.1) and consents; no change to the statements.
- **The current perimeter document: Form 10-Q, quarter ended 2026-06-30, filed 2026-08-06,
  accession `0001710366-26-000054`** — statements, notes, MD&A and Part II.
- **The pre-close record, both companies, every year the pro forma uses:** CONSOL 10-Ks FY2021
  `0001437749-22-003140` (2022-02-11) · FY2022 `0001710366-23-000005` (2023-02-10) · FY2023
  `0001710366-24-000006` (2024-02-09) · FY2024 `0001710366-25-000010` (2025-02-20; filed after the
  close under the Core name but covering standalone CONSOL). **Arch** (CIK 1037676) 10-Ks FY2021
  `0001558370-22-001243` (2022-02-16, carrying FY2019-21 cash flows) · FY2022
  `0001558370-23-001458` (2023-02-16) · FY2023 `0001558370-24-001229` (2024-02-15) · and its last
  periodic report, **10-Q for 2024-09-30, `0001558370-24-014411`** (2024-11-05). **Arch filed no
  FY2024 10-K** — the merger closed fourteen days after its year end — **so Arch's Q4 2024 cash
  flow was never filed by anyone.** Named in Q4 as the pro forma's hole.
- **8-K EX-99.1 earnings releases, fetched before scoring [E4-29] and [E4-22]'s third flag**:
  Q4 2024 (`0001710366-25-000008`), Q1 2025 (`0001193125-25-115451`), Q2 2025
  (`0001193125-25-173024`), Q3 2025 (`0001710366-25-000029`), Q4 2025 (`0001710366-26-000005`),
  Q1 2026 (`0001710366-26-000040`), Q2 2026 (`0001710366-26-000053`); the closing release
  (EX-99.1 to `0001193125-25-007135`); the 2025-03-28 release (`0001193125-25-066237`, Items 7.01
  and 8.01).
- **DEF 14A filed 2026-03-16, accession `0001710366-26-000017`.**
- **Figure cross-checked against the filed statement:** *Net Cash Provided by Operating
  Activities*, FY2025 Consolidated Statements of Cash Flows, **$305,752 thousand** — XBRL
  `NetCashProvidedByUsedInOperatingActivities` 305.8. Also checked in the same statement:
  *Stock-Based Compensation* **$32,918** (XBRL 32.9), *Depreciation, Depletion and Amortization*
  **$621,067** (XBRL 621.1), *Capital Expenditures* **$(284,581)** (XBRL 284.6). **On the Arch
  side**, which the pro forma depends on: FY2023 *Cash provided by operating activities*
  **$635,374** in Arch's filed 10-K (XBRL 635.4), *Employee stock-based compensation expense*
  **$25,443** (XBRL 25.4), *Capital expenditures* **$(176,037)** (XBRL 176.0).
- *No ladder rung was blocked. Everything above is SEC EDGAR rung 2; the only aggregator input is
  the live quote, flagged.*

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
### Unit economics in my own words

Core digs coal out of the ground in four places, washes most of it, and puts it on a train. It
is paid per ton, and the price per ton is set by somebody else's market. There are three
businesses and a toll road:

| segment (FY2025 10-K, MD&A reconciliation tables) | tons sold | realised revenue / ton | cash cost / ton | cash margin / ton | where the price comes from |
|---|---|---|---|---|---|
| **High CV Thermal** — the Pennsylvania Mining Complex (three longwall mines on the Pittsburgh No. 8 seam) plus West Elk, Colorado | 30.6M | **$60.34** | $40.99 | $19.35 | seaborne thermal (*"Newcastle prices … API2 pricing"*, MD&A) and domestic power contracts |
| **Metallurgical** — Leer and Leer South longwalls (High-Vol A), Beckley, Mountain Laurel, Itmann | 9.0M | **$102.36** (coking coal $113.91) | $96.13 | $6.23 | *"metallurgical coal benchmark prices"* |
| **Powder River Basin** — Black Thunder and Coal Creek surface mines, Wyoming | 48.9M | **$14.46** | $13.15 | $1.31 | multi-year domestic power contracts |
| **Core Marine Terminal**, Baltimore | 18.1M throughput | — | — | Adjusted EBITDA $56.8M on $87.7M revenue | a toll; **~83% of the tonnage was the PAMC's own coal** (Item 1) |

*(Per-ton measures are the company's non-GAAP ratios, reconciled to cost of sales in the filed
MD&A. "Cash cost" excludes transportation, idle-mine costs — $136.6M in FY2025, including the Leer
South fire — and DD&A. Those exclusions are scored at Q3.)*

So the money is made on the gap between an **external price** and an **internal cost per ton**.
The company controls the cost; the filing says in plain words that it does not control the
price: domestic thermal prices depend on *"the supply-demand balance for our products … prices for
other competing sources of energy used for electric power generation, such as natural gas … prices
for coals from other basins that compete in these same regions"*, and export prices on *"the
supply-demand balance of seaborne thermal coal … the supply-demand balance of seaborne
metallurgical coal … prices for other export coals that compete in these same markets"* (10-K
FY2025, Item 1, *Coal Contracts and Pricing*). Domestic contracts are *"typically fixed"* for *"one
year or longer"*; export sales were historically *"spot or shorter-term contracts with pricing
determined closer to the time of shipment or based on a market index"*. The contract book smooths
the timing; it does not set the level.

**Revenue decomposes directly into tons × price, as [E4-55] asks, and the physical series is
filed.** The volume side has a hard ceiling: the PAMC's *"full-capacity production … is
approximately 28.5 million clean tons of coal annually"* (Item 1) and it sold 24.1M-27.4M tons in
every year 2022-2025 (27.4M in 2025 = the segment's 30.6M less West Elk's 3.2M) — **it is already
near the top**. So the upside in this business is almost
entirely **price**, and volume can only grow by spending capital on new longwalls (Leer South
2019-21, Itmann 2019-22, Leer West next). That is **[E2-63]**'s ceiling in its plainest form:
*"the great majority of operating businesses have a limited upside potential also unless more
capital is continuously invested in them."*

### The physical and price series, both companies, every filed vintage

**Pennsylvania Mining Complex** (CONSOL 10-Ks FY2021-FY2024; FY2025 is the High CV Thermal
segment, which adds West Elk's 3.2M tons at ~$52/ton realised and ~$50/ton cash cost):

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 (High CV) | Q2 2026 |
|---|---|---|---|---|---|---|---|---|
| tons sold (M) | 27.3 | 18.7 | 23.7 | 24.1 | 26.0 | 25.7 | 30.6 | 8.4 (qtr) |
| realised $/ton | 47.17 | 41.31 | 45.75 | 69.89 | 77.74 | 65.54 | 60.34 | 58.11 |
| cash cost $/ton | 30.97 | 29.12 | 28.25 | 34.56 | 36.10 | 37.89 | 40.99 | 38.58 |
| cash margin $/ton | 16.20 | 12.19 | 17.50 | 35.33 | 41.64 | 27.65 | 19.35 | 19.53 |

**Arch metallurgical** (Arch 10-Ks FY2021-FY2023; 10-Q Q3 2024 for nine months; FY2025 is Core's
Metallurgical segment, which includes legacy CONSOL's Itmann):

| | 2020 | 2021 | 2022 | 2023 | 9M 2024 | 2025 (Core Met) | Q2 2026 |
|---|---|---|---|---|---|---|---|
| tons sold (M) | 7.0 | 7.7 | 7.8 | 9.3 | 6.8 | 9.0 | 2.6 (qtr) |
| coal sales $/ton | 74.17 | 126.44 | **223.91** | 166.11 | 131.76 | **102.36** | 114.13 |
| cash cost $/ton | 61.13 | 68.84 | 93.61 | 89.08 | 93.08 | 96.13 | 85.65 |
| cash margin $/ton | 13.04 | 57.60 | **130.30** | 77.03 | 38.69 | **6.23** | 28.48 |

**Arch thermal** (PRB plus West Elk until 2024; FY2025 is Core's PRB segment alone):

| | 2020 | 2021 | 2022 | 2023 | 9M 2024 | 2025 (PRB) | Q2 2026 (PRB) |
|---|---|---|---|---|---|---|---|
| tons sold (M) | 55.7 | 65.3 | 70.4 | 65.6 | 37.7 | 48.9 | 10.2 (qtr) |
| $/ton | 13.55 | 13.95 | 19.50 | 17.48 | 17.46 | 14.46 | 14.28 |
| cash cost $/ton | 13.00 | 11.35 | 14.57 | 15.61 | 17.17 | 13.15 | **14.85** |
| cash margin $/ton | 0.55 | 2.60 | 4.93 | 1.87 | 0.28 | 1.31 | **(0.57)** |

*(Q2 2026 column from the EX-99.1 release of 2026-08-06, `0001710366-26-000053`. The 10-Q for the
same quarter carries no per-ton table, so the release is the only filed source for it.)*

### [E3-31] — can these cash flows be predicted at all? Answered from the filed volatility

The pro forma combined record — the two companies' filed figures added, reconciled to the
company's own pro forma where one exists (S-4/A: FY2023 combined revenue **$5,750.0M** = CONSOL
$2,568.9M + Arch $3,163.1M + $18.0M reclassification; FY2025 10-K Note 2: pro forma FY2024
**$4,599.3M**, FY2025 **$4,215.5M**):

| pro forma, combined | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| revenue (sum of filed lines; 2024-25 the Note 2 pro forma) | $2,489M | $3,467M | $5,826M | $5,750M | $4,599M | $4,215M |
| net income (sum of filed; 2024-25 Note 2 pro forma) | **−$354M** | $372M | **$1,798M** | $1,120M | $81M | **−$110M** |
| owner earnings, total capex + finance-lease principal (Q4 build) | **−$239M** | $111M | **$1,457M** | $1,089M | $467M* | **−$24M** |

*\*2024 pairs CONSOL's calendar year with Arch's four quarters to 2024-09-30 — see Q4.*

**Net income moved from −$354M to +$1,798M and back to −$110M in five years; owner earnings from
−$239M to +$1,457M to −$24M. The met margin per ton moved twenty-one-fold, $6 to $130, on
cost per ton that moved only 1.6x.** The variance is almost entirely the price, and the price is
the one input the filing says is set outside the company. By the terms of [E3-31] this business
is **simple** — rock, a washing plant, a train, a price — and **not stable in character** in the
one variable that sets its earnings.

**But Q1 asks whether I can understand how it makes money, not whether I like the answer.** I can
read the whole mechanism off the filings, and I can decompose every year's result into tons,
price and cost from the companies' own tables. A business that is understood and unstable is a
**Q2** matter — the commodity doctrine **[E2-58]** is filed there — and a **Q4** matter, where
the spread across windows is itself the range **[E4-25]**. Marking Q1 OUT on price volatility
would smuggle the moat verdict into the understanding gate (the OXY precedent, 2026-09-01, same
reasoning). **[E4-46]** does not bite either: this is not a business that would take *"five
months"* of study; the filings answered it.

### The scarce input this business controls

**Specific coal in specific seams, and one terminal.** Not the price.
- **The Pittsburgh No. 8 seam at the PAMC**: *"529.0 million tons of recoverable coal reserves that
  are sufficient to support approximately 20 years of full-capacity production"* at ~12,900-13,000
  Btu/lb, *"a large contiguous formation of high-Btu coal that is ideal for high-productivity,
  low-cost longwall operations"* (Item 1).
- **The Lower Kittanning High-Vol A seam at the Leer Complex**: 170.2M tons, of which **Leer 29.4M,
  Leer South 57.0M, Leer West 83.8M** (the undeveloped third longwall). Leer produced 5.1M tons in
  2025 — **about six years of reserves at that rate**. The Leer Complex's twenty-plus-year life
  depends on *building* Leer West.
- **The Core Marine Terminal**: *"the only major East Coast coal terminal served by both Norfolk
  Southern and CSX railroads"*, ~20M tons/year capacity (Item 1). Real, and small: $56.8M of
  segment Adjusted EBITDA in FY2025, and most of its volume is the company's own coal.

**A reserve is scarce in the ground and depleting in the ledger.** Every ton sold is a ton of the
scarce input gone; the input has to be replaced by developing the next panel, the next mine, the
next lease. That is a Q2 fact under [E4-04]'s *"depleting assets"* scope, recorded here because it
is what the business *is*.

### Will the fundamentals look broadly the same in ten years?

**The mechanism will. The markets are the open question, and the filing names both threats.**
- **73% of 2025 tons went to electric power generation** (Item 1). The filing's own competition
  section: *"Indirect competition for sales of thermal coal from natural gas-fired power plants …
  has the most potential to displace a significant amount of coal-fired electric power generation
  in the near term"*, and renewable mandates plus *"falling costs for wind and solar energy
  technologies"* *"have made alternative fuel sources more competitive with coal."* Against that,
  the 2025-26 releases cite AI data-centre power demand and April 2025 executive orders *"intended
  to … ensure the long-term preservation of the U.S. coal fleet"* — **a regime, not a franchise**,
  and [E2-59] is filed at Q2 for exactly that.
- **Metallurgical coal**: *"competition for production of steel from non-coal sources, including
  electric arc furnaces or other alternative processes … may limit demand for our product"*
  (Item 1). The Q2 2026 release: *"two years of contraction in global hot metal output, and coking
  coal price assessments on the U.S. East Coast continue to lag Australian price indices by a
  historically wide margin."*
- **The reserves will be different reserves.** Leer runs out inside the decade on its 2025 rate;
  PAMC's 20 years is at full capacity.

- **VERDICT: [x] IN.** The business is understood from its own filings: an external price, a
  controllable cost, a depleting reserve, a capacity ceiling. **Its instability is recorded and
  carried to Q2 (the commodity doctrine) and Q4 (the range), where the corpus files it.** No
  "provisional" caveat attaches to the understanding itself.

## Q2 — IS IT A FRANCHISE? **[E3-03]**
**Where the corpus files this business.** A coal producer sells a product graded by Btu, sulphur,
ash and volatility, priced off benchmarks. The corpus's doctrine for that class is **[E2-58]**:
*"In many industries, differentiation simply can't be made meaningful. A few producers in such
industries may consistently do well if they have a cost advantage that is both wide and
sustainable. By definition such exceptions are few … For the great majority of companies selling
'commodity' products, a depressing equation of business economics prevails: persistent
over-capacity without administered prices (or costs) equals poor profitability."* **The
low-cost-producer exception is the only route to a franchise here, and it has two words in it:
WIDE and SUSTAINABLE.** The file tests both against the filed peer row.

### THE BULL CASE, built at full strength before it is tested [E4-26, E4-51]

As a holder would state it, from the company's own filings:
- **Two first-quartile longwall platforms on scarce seams.** *"the Leer Complex longwall mines …
  anchor our large-scale, first-quartile metallurgical franchise. The Leer Complex mines
  consistently rank among the lowest-cost U.S. metallurgical mines and produce a product quality
  that we believe is recognized and sought-after worldwide"* (10-K FY2025, Item 1). The PAMC:
  *"averaging 7.45 tons of coal production per employee hour in 2025"*, on a seam *"ideal for
  high-productivity, low-cost longwall operations"*, with 529.0M tons — twenty years (Item 1).
  Arch, before the merger, on Leer South: it *"is expected to enhance our already advantageous
  position on the U.S. cost curve; strengthen our coking coal profit margins across a wide range of
  market conditions"* (Arch 10-K FY2021).
- **A logistics asset nobody else has**: *"the only major East Coast coal terminal served by both
  Norfolk Southern and CSX railroads"* (Item 1), plus 35% of the Dominion Terminal.
- **A product that sells as a substitute upward**: *"Core continues to make good progress in
  marketing its Leer brand coal as an advantageous and high value-in-use substitute for Australian
  premium low-vol coals"* (EX-99.1 2026-08-06).
- **A contract book that smooths the price**: 2026 committed and priced — 30.9M High CV tons at
  **$58.00**, 50.3M PRB tons at **$14.27**, 6.0M coking tons at **$120.86** (2026 guidance, same
  release). *"approximately 95% of our sales in 2025 were to customers that were in both our and
  Arch's 2024 portfolio"* (Item 1).
- **And the number the bull case rests on**: in **Q2 2026**, with Leer South's longwall back, the
  met segment's cash cost fell to **$85.65/ton** and its cash margin rose to **$28.48** — while
  Peabody's Seaborne Met margin was **−$7.04** and Coronado's Australian operations were at **−$26.9**
  for the half (peer row below). **Core is not the marginal producer.** At a trough price the
  marginal producers lose money and Core does not.

That is the strongest honest form. Now the tests.

### [E3-03] — the three criteria
- **(1) Needed or desired — [x] yes.** Steel mills and power plants buy it.
- **(2) Thought by its customers to have no close substitute — [ ] NO, on the company's own words.**
  *"The coal industry is highly competitive, with numerous producers selling into all markets that
  use coal. There are numerous large and small producers in all coal-producing basins of the U.S.,
  and we compete with many of these producers"*; *"The most important factors on which we compete
  are coal price, coal quality and characteristics, transportation costs and reliability of
  supply"* (10-K FY2025, Item 1, *Competition*). Domestic thermal prices depend on *"prices for coals
  from other basins that compete in these same regions"*; export prices on *"prices for other export
  coals that compete in these same markets"* (Item 1). **The competitors name Core back**: Peabody's
  FY2025 10-K lists *"Core Natural Resources, Inc."* among its *"principal U.S. direct coal supply
  competitors"* **and** among its *"Major international direct competitors"* in met coal; Alliance's
  FY2025 10-K lists it among *"Our principal competitors"*; Ramaco names *"Arch Resources, Inc. (now a
  subsidiary of Core Natural Resources)"*. And the bull case's own best line is that Leer coal is *"a
  … substitute for Australian premium low-vol coals"* — **a product sold as a substitute is not a
  product without one.**
- **(3) Not subject to price regulation — [x] largely yes, with a regime in the cost line.** Prices
  are market-set. But the 2026 PRB guidance *"Reflects the expected impact of the recently enacted
  royalty rate reduction on federal coal leases"*, met coal became a *"critical material"* under
  Section 45X for *"a 2.5% monetizable tax credit on production-related costs beginning in 2026 and
  sunsetting at the end of 2029"*, and April 2025 executive orders aim *"to ensure the long-term
  preservation of the U.S. coal fleet"* (10-K FY2025, MD&A). **[E2-59]**: administered help floors a
  commodity business; *"the moat belongs to the regime."*

### THE COMPETITOR ROW — required [E3-28]
*Built from each company's own 10-K/10-Q primary documents; every figure, document and accession is
in `Test Runs/_research 2026-09-13 CNR/peers/PEER_ROW.md`. Three figures were re-verified by this
run against the cached filings: HCC FY2025 cash cost $111.66/metric ton, BTU PRB FY2025 cost
$11.56/ton, AMR FY2025 non-GAAP cost $102.23/ton.* **The measures are each company's own and are NOT
like-for-like** — units (short vs metric tons), price bases (FOB mine, FOB port) and cost bases
(freight and royalties in or out; idle costs in or out) differ, and the file lists each. **The row
is read for position within each year and for direction across years, not as a league table of
dollars.** Margin = realised price less cash cost per ton; Core's excludes transport and idle costs.

**Metallurgical — cash margin per ton (price / cost / margin):**

| | 2021 | 2022 | 2023 | 2024 | 2025 | Q2 2026 (3 mo) |
|---|---|---|---|---|---|---|
| **Arch → Core Met** (short tons) | 126.44 / 68.84 / **57.60** | 223.91 / 93.61 / **130.30** | 166.11 / 89.08 / **77.03** | 131.76 / 93.08 / **38.69** (9M) | 102.36 / 96.13 / **6.23** | 114.13 / 85.65 / **28.48** |
| **Warrior Met Coal (HCC)** (metric; cost incl. freight & royalties) | 180.43 / 96.43 / **84.00** | 334.89 / 138.35 / **196.54** | 241.64 / 132.60 / **109.04** | 207.32 / 138.10 / **69.22** | 146.20 / 111.66 / **34.54** | 151.91 / 101.99 / **49.92** |
| **Alpha Metallurgical (AMR)** (short; excl. freight & idle) | 115.18 / 77.71 / **37.47** | 225.45 / 108.22 / **117.22** | 179.40 / 111.67 / **67.73** | 142.66 / 112.01 / **30.64** | 117.08 / 102.23 / **14.85** | 118.71 / 103.07 / **15.64** |
| **Ramaco (METC)** (FOB mine, whole $) | 109 / 70 / **39** | 207 / 108 / **99** | 170 / 110 / **60** | 140 / 105 / **35** | 120 / 98 / **22** | 116 / 99 / **17** |
| **Peabody Seaborne Met (BTU)** (short) | 131.83 / 99.55 / **32.28** | 243.78 / 125.92 / **117.86** | 188.66 / 125.18 / **63.48** | 144.97 / 122.77 / **22.20** | 120.88 / 114.31 / **6.57** | 148.04 / 155.08 / **(7.04)** |
| **Coronado — Australia** (metric; operating cost) | 113.1 / 98.2 / **14.9** | 208.9 / 158.3 / **50.6** | 167.0 / 170.5 / **(3.5)** | 153.1 / 156.3 / **(3.2)** | 112.9 / 131.3 / **(18.4)** | 6M: **(26.9)** |
| **Coronado — United States** (metric; operating cost) | 128.6 / 81.3 / **47.3** | 225.2 / 115.0 / **110.2** | 198.4 / 132.9 / **65.5** | 156.7 / 136.5 / **20.2** | 143.4 / 133.7 / **9.7** | 6M: **13.4** |

**High calorific value / eastern thermal — cash margin per ton:**

| | 2021 | 2022 | 2023 | 2024 | 2025 | Q2 2026 |
|---|---|---|---|---|---|---|
| **CONSOL PAMC → Core High CV** | 45.75 / 28.25 / **17.50** | 69.89 / 34.56 / **35.33** | 77.74 / 36.10 / **41.64** | 65.54 / 37.89 / **27.65** | 60.34 / 40.99 / **19.35** | 58.11 / 38.58 / **19.53** |
| **Alliance — Illinois Basin (ARLP)** (2024-26 computed from filed totals) | 39.25 / 27.55 / **11.71** | 50.60 / 33.43 / **17.17** | 55.21 / 34.84 / **20.37** | 56.44 / 37.81 / **18.64** | 52.09 / 34.71 / **17.38** | 51.87 / 35.99 / **15.88** |
| **Alliance — Appalachia (ARLP)** | 51.28 / 34.42 / **16.86** | 76.86 / 40.42 / **36.44** | 86.98 / 53.15 / **33.84** | 83.53 / 64.67 / **18.87** | 81.99 / 63.82 / **18.18** | 63.57 / 46.22 / **17.34** |
| **Peabody — Seaborne Thermal (BTU)** | 54.09 / 33.64 / **20.45** | 86.07 / 44.65 / **41.42** | 85.94 / 48.66 / **37.28** | 73.88 / 47.71 / **26.17** | 58.97 / 44.55 / **14.42** | 74.85 / 57.93 / **16.92** |
| **Peabody — Other U.S. Thermal (BTU)** | 40.75 / 31.04 / **9.71** | 51.82 / 38.63 / **13.19** | 54.77 / 41.98 / **12.79** | 56.38 / 46.04 / **10.34** | 52.82 / 47.49 / **5.33** | 55.26 / 46.13 / **9.13** |

**Powder River Basin — cash margin per ton:**

| | 2021 | 2022 | 2023 | 2024 | 2025 | Q2 2026 |
|---|---|---|---|---|---|---|
| **Arch Thermal (PRB + West Elk) → Core PRB** | 13.95 / 11.35 / **2.60** | 19.50 / 14.57 / **4.93** | 17.48 / 15.61 / **1.87** | 17.46 / 17.17 / **0.28** (9M) | 14.46 / 13.15 / **1.31** | 14.28 / 14.85 / **(0.57)** |
| **Peabody — PRB (BTU)**, the basin's other giant | 10.99 / 9.46 / **1.53** | 12.89 / 12.06 / **0.83** | 13.74 / 11.98 / **1.76** | 13.81 / 12.07 / **1.74** | 13.64 / 11.56 / **2.08** | 13.63 / 14.06 / **(0.43)** |

- **Peers taken: 6 companies with filed per-ton series** (AMR, HCC, METC, BTU in four segments, ARLP in
  two, and Coronado as the only US-GAAP Australian met series) **of roughly 25 competitors the
  filings name** (Peabody's two lists alone name ACNR, Eagle Summit, Foresight, Hallador, Kiewit,
  NTEC, Anglo American, BHP, Foxleigh, Glencore, Jellinbah, KRU, Oak Grove, Stanmore, QCoal,
  Whitehaven, Yancoal; Ramaco adds Blackhawk).
- **Unavailable, and the limit stated:** the private US producers (ACNR, Blackhawk, Foresight,
  Kiewit, NTEC) file nothing; BHP (20-F) and Teck (40-F) file on IFRS with different units, fiscal
  years and segment definitions (not fetched); Glencore has no annual report on EDGAR. **Why this
  does not make the class PROVISIONAL:** the OUT below rests on (i) criterion (2) in Core's own words,
  (ii) Core's own margin collapsing to $6.23 (met) and $1.31 (PRB) a ton in 2025, and (iii) the
  position against the filed US peers. None of those can be reversed by a missing foreign row: a
  wide advantage over BHP or Anglo would not make a $6 margin wide, and a narrow one would only
  confirm it.

### THE TESTS, on the row

**1. Is the cost advantage WIDE? — NO.**
- **In metallurgical coal the widest filed margin belongs to Warrior, not Core, in every year
  2021-2025 and in Q2 2026** — on a cost measure that *includes* freight and royalties, which Core's
  excludes. Warrior's FY2025 10-K: *"We believe our mines are some of the lowest cost steelmaking
  coal mines in North America"* and Blue Creek *"further improving our position in the first-quartile
  global cost curve."* Arch/Core ranked **second** in 2021-2024 and Q2 2026 and **last-but-one** in 2025
  (the Leer South fire year).
- **Core's margin over the next US producer was a few dollars, and shrinking**: over Alpha, **+$20.13
  (2021) → +$13.08 → +$9.30 → +$8.05 (2024) → −$8.62 (2025) → +$12.84 (Q2 2026)**; over Ramaco, +$18.60 →
  +$31.30 → +$17.03 → +$3.69 → −$15.77 → +$11.48. A spread of **$8-13 a ton on a $100-120 price** is not
  the *"wide"* of [E2-58].
- **The advantage over the marginal producer is real and it is the bull case's best fact** — Core
  +$28.48 against Peabody Seaborne Met −$7.04 in Q2 2026. **But the same row shows what that margin
  buys at the trough: $6.23 a ton for a full year (2025)**, when Peabody's seaborne met was +$6.57. In
  the year the cost position was supposed to protect the margin, it did not.
- **High CV thermal: the PAMC's advantage was the export price, not the cost.** Its cash cost
  ($40.99 in 2025) is **above** Alliance's Illinois Basin ($34.71) and level with Alliance's whole coal
  operation ($41.29). Its margin premium over Alliance Illinois Basin went **+$5.79 (2021) → +$18.16 →
  +$21.27 (2023) → +$9.01 → +$1.97 (2025) → +$3.65 (Q2 2026)** — it rose with seaborne prices and fell
  back with them. The cost did not create it.
- **PRB: no advantage at all.** Core's PRB cash cost ($13.15, 2025) is **higher** than Peabody's
  ($11.56); both earned **$1-2 a ton** in 2025 and **both went negative in Q2 2026**. This is [E2-58]'s
  equation observed directly, and it is **48.9M of Core's 88.5M tons**.

**2. Is it SUSTAINABLE? — NO; the costs ratchet and the prices do not.**
- **Cash cost per ton, 2021 → 2025, same window for every row:** Arch/Core met $68.84 → **$96.13,
  +40%** (+57% from 2020's $61.13); PAMC/High CV $28.25 → **$40.99, +45%**; Arch thermal/PRB $11.35 →
  $13.15, +16%. Peers: Alpha +32%, Warrior +16%, Ramaco +40%, Peabody PRB +22%, Alliance Illinois Basin
  +26%. **Core's met cost rose faster than Warrior's and Alpha's; its PAMC cost faster than every
  thermal peer's.**
- **The 2022 spike and its unwind is the controlled experiment [E2-44].** Arch met cost rose
  **+36% into the spike** ($68.84 → $93.61, 2021 → 2022) and **never came back** ($96.13 in 2025) while
  price went $223.91 → $102.36. PAMC cost rose every year 2021-2025 while price went $77.74 → $60.34.
  That is **[E3-62]'s second step** in the coal ledger: productivity gains and price spikes do not
  *"stick to our ribs"* — the price returns to the customer's benchmark, the costs stay.
- **The company's own technical reports moved the same way.** Arch's S-K 1300 reserve estimates for
  Leer South assumed an *"average cash cost per short ton of $52.39"* (Arch 10-K FY2021) and then
  **$75.99** two years later (Arch 10-K FY2023) — +45% in the qualified person's own assumption for the
  flagship's newest mine.
- **[E4-47]**: inflation *"destroys it very unequally"*; a business that must replace equipment,
  labour and supplies in current dollars and sell at a benchmark is the class it destroys.

**3. [E2-44] — both halves.**
- **(1) Can it raise prices *"even when product demand is flat and capacity is not fully
  utilized"*? — NO.** The company's own Q2 2026 release: *"With the U.S. coal fleet operating at an
  average capacity factor of less than 50 percent"* — and PAMC realisation fell four years running
  ($77.74 → $65.54 → $60.34 → $58.11) while its sales volume rose. It took volume at the market's
  price.
- **(2) Can it grow dollar volume *"with only minor additional investment of capital"*? — NO.** The
  PAMC is at its 28.5M-ton capacity (Q1); new volume has meant new longwalls — Leer South (Arch capex
  **$266.4M / $285.8M / $245.4M** in 2019-2021 against D&A of ~$112-122M) and Itmann (CONSOL) — and
  the Leer Complex's next decade needs Leer West.

**4. [E4-04] — must the moat be continuously rebuilt? YES, and in the excluded sense.** The basis is a
*depleting asset*: Leer holds **29.4M tons against 5.1M produced in 2025** (Q1). Holding volume means
**buying the replacement** — developing Leer West, extending the PAMC into unpermitted reserves (152.6M
of Enlow Fork's 228.3M tons are unpermitted, Item 1) — which is the Rhodes Ridge case, not the
Coca-Cola case. **And [E2-45] — the attacker's test — was not hypothetical:** Warrior *"commenced
longwall operations at the Blue Creek mine in October 2025, eight months ahead of schedule and on
budget"*, a new first-quartile longwall selling into the same seaborne market in the same year Core's
flagship was sealed.

**5. [E4-36] and [E3-51] — where the record came from.** 98% of the pro forma owner earnings of
2019-2023 were earned in 2022-2023 (Q4): the Ukraine-war price spike. That is **wave-riding** — the
fourth cause, and the unownable one. *"The advantage lives in the wave, not the surfer."*

**6. Primary moat metric and direction [E4-32, E4-55].** Cash margin per ton against the peer row:
**narrowing** on every segment across 2023 → 2025 (met premium over Alpha $9.30 → −$8.62; PAMC
premium over Alliance IB $21.27 → $1.97; PRB level with Peabody at ~zero), with a Q2 2026 rebound in
met as Leer South returned. **Units [E4-55]:** PAMC volume flat at capacity; PRB 48.9M tons, guided
47-50M for 2026 — no hidden unit decline, and no unit growth without capital.

- **Untapped pricing power [E3-33]:** none. **[E5-28]**: the class requires *"a monopoly or a near
  monopoly"*; Core is one of ~25 named competitors in a market whose price it reads off an index.
  **[E4-37]**'s agony metric does not apply — there is no price decision to agonise over.
- **Key-person dependence [E4-23]:** none found; the business does not need a surgeon. It needs a price.
- **The row's limit [E3-61]:** it shows position, not conduct; it cannot say whether the next glut
  will be disciplined. The corpus says that is not knowable from structure.
- **The terminal**, for completeness: a genuine two-railroad asset earning $56.8M of segment Adjusted
  EBITDA on $87.7M of revenue — **2.1% of Core's revenue**, and **~83% of its tonnage is the PAMC's own
  coal**. A toll road whose traffic is the owner's commodity inherits the commodity's economics.

- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: narrowing 2023 → 2025; a
  met-segment rebound in Q2 2026 on Leer South's restart.**
- **VERDICT: [x] OUT — on the business, permanent for this file.** Three independent filed grounds,
  any one sufficient:
  1. **[E3-03] criterion (2) fails in the filer's own words**: *"numerous producers selling into all
     markets that use coal"*, competing on *"coal price, coal quality and characteristics,
     transportation costs and reliability of supply"*, named as a direct competitor by Peabody and
     Alliance, and marketing its best coal as *"a … substitute"* for someone else's.
  2. **[E2-58]'s exception is not met.** The cost advantage is **not wide** (second to Warrior in
     every met year, $8-13 a ton over Alpha; below Alliance on thermal cost; above Peabody on PRB
     cost; **$6.23 and $1.31 a ton** of margin in 2025) and **not sustainable** (met cost +40% and PAMC
     cost +45% over 2021-2025, faster than Warrior and Alpha; the flagship's own reserve-report cost
     assumption +45% in two years).
  3. **[E4-04]'s excluded class**: a depleting basis whose replacement must be bought, in an industry
     where a competitor built a new first-quartile longwall in the same year.

  **[E5-35]: entry is closed at any price** — *"What you can't do is turn any investment into a good
  deal by paying little."* **[E5-13]: most names should end here, and that is the system working.**

**The prior was OUT. It was framed to be refuted [E4-26] — the bull case above is the attempt, and its
strongest fact (a $28.48 met margin in Q2 2026 while Peabody lost money) is real. It did not refute
the prior, because one good quarter at a trough is not "wide", and 2025 was not "sustainable".**

---
⛔ **Q3, Q4 AND Q5 DO NOT OPEN FOR ENTRY.** Q1 IN · **Q2 OUT** — the hard sequence closes the file.
**Everything below is RECORDED, NOT GOVERNING, at the brief's instruction** (the capital-return test,
the rebuilt pro forma owner earnings, the senior claims, the survival shape, the price). **Operator
rule 3 governs every number below; none of it is entry language.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> ⛔ **RECORDED, NOT GOVERNING.** Q2 closed the file OUT on the business. The hard sequence means
> nothing below can reopen it — the framework's guardrail (Q3 can stop a run, it can never start
> one; a strong Q3 cannot promote a name, repair Q2, or substitute for Q4) rests on **[E2-37, E2-38, E3-39]**. Q3 is
> written because the brief asked for the capital-return test against owner earnings, and because
> the sharpest facts in this company's filings are here. **No entry language.**

**STEP 1 — DECLARE THE WEIGHT CASE.**
- [x] **Daily execution** — have-to-be-smart-every-day **[E3-38]**. An undifferentiated product
  *magnifies* the manager **[E2-70]**, and an underground longwall is decided shift by shift: the
  Leer South fire idled the flagship met mine for eleven months (sealed 2025-01-13, longwall
  resumed December 2025) and cost **$101M** of extinguishment and idle costs (10-K FY2025, MD&A);
  three MSHA section 107(a) imminent-danger orders were reported in 2026 alone (8-Ks 2026-01-12,
  2026-05-04, 2026-05-19 — methane at Mountaineer II twice and at Leer South, the last vacated by
  MSHA as never having existed).
- [ ] **Control** — a minority holder can sell **[E1-16]**.
- [ ] **Leverage** — financial leverage is low (debt and finance leases **$447.6M** against equity
  of $3,718.9M at 2026-06-30) **[E3-29]**. The senior claims that matter are the legacy
  liabilities, scored at Q4.

**Case declared: Q3 is a BINARY GATE on the daily-execution determinant.** No price compensates
for a failure here **[E5-35]** — moot, because Q2 has already closed the file.

**Honesty — binary, dated to when each matter became public [E5-16].** No finding of personal
misconduct was located in the 10-K, the 10-Q, the proxy or the 8-Ks read. Matters on the record,
none an integrity finding:
- **UMWA 1974 Pension Plan indemnification suit** (public 2024-03-07; summary judgment for the
  former parent 2024-11-08): an accrual of **$67.9M**, the present value of five years of payments
  indemnifying CNX's $75.0M settlement (CONSOL 10-K FY2024, Note 23). A contract dispute under the
  2017 separation agreement, lost.
- **UMWA 1992 Benefit Plan litigation** over Murray Energy's retirees (public 2020-05-02), open.
- **A transcription error in the filing itself**: the FY2024 10-K says the partial summary judgment
  was granted by *"the Superior Court of the State of Delaware"*; the FY2025 10-K's MD&A says
  *"filed by the Supreme Court of the State of Delaware"*. The earlier (and the note's) wording is
  the correct court. Recorded as a care-of-disclosure prompt, not a flag.

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30].** *Each is a prompt to READ, never a verdict
[E5-36, E5-38].* The 8-K EX-99.1 releases were read before scoring, per the CGNX instruction.

- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRES, and it reaches the pay line.** Every
  release since the merger carries *"adjusted EBITDA"* in its headline, beside net income (Q2 2026: *"Reports net
  income of $126 million and adjusted EBITDA of $324 million"*). The proxy pays on it: **50% of the
  2025 short-term incentive is Adjusted EBITDA**, and the long-term plan's 45% weight is *"ICP Free
  Cash Flow"*, defined as *"Adjusted EBITDA*; less capital expenditures; less interest expense; plus
  proceeds from asset sales"* — a figure that never sees working capital, reclamation payments,
  black-lung and retiree-medical cash, or SBC. ICP Free Cash Flow FY2025: **$187.8M**, against
  owner earnings of **−$24.3M** (Q4).
- [x] **Metric adjusted into the bullseye [E2-49] — FIRES, to the dollar.** DEF 14A filed
  2026-03-16, note (1) to the 2025 STIC table: *"the Board determined that it was appropriate to add
  $75,774,000 to our Adjusted EBITDA* results of $512,066,000 under the 2025 STIC to capture the
  impact of the expected, but not yet received, insurance proceeds related to the fire at the Leer
  South Mine."* The table's **threshold is $587,840,000**. **$512,066,000 + $75,774,000 =
  $587,840,000.** The adjustment added exactly the amount needed to lift a below-threshold result
  (a 0% payout on half the plan) to the threshold itself (a 25% payout), and it did so with cash the
  proxy itself calls *"not yet received."* The proceeds did later arrive — the claim settled in
  June 2026 for $154.5M — so the adjustment was not fiction; **the tell is the precision, not the
  existence.** [E5-38] governs how this is read: it is a board playing a game with a number that
  came to it, which is a flag on the accounting of pay, not a finding about anyone's honesty.
- [x] **The except-for flag [E2-57] — FIRES.** "Cash cost of coal sold" per ton excludes idle-mine
  costs ($136.6M in FY2025, including the fire) and "Other Adjustments" to Adjusted EBITDA were
  **$98.8M in 2025 and $98.3M in 2024** (proxy Appendix A) — two consecutive years of roughly $100M
  of "non-recurring" items. The 2024 set included the $67.9M UMWA 1974 accrual; 2025 included $66M
  of merger costs. **[E5-33]: these are real costs and they are in owner earnings below.**
- [x] **Trumpeted projections [E4-22 third flag] — FIRES in form; the record is decent.** Synergy
  target raised twice in two quarters — *"$110 million to $140 million"* (closing, 2025-01-14) →
  *"$125 and $150 million"* (Q1 2025) → *"between $150 million and $170 million"* (Q2 2025) — and
  then **no quantified synergy figure in any later release**; the proxy says only *"Captured – or
  set the stage to capture – merger-related synergies significantly above our original estimate."*
  A target announced, raised, raised, then retired into an unquantified phrase is **[E2-49]'s
  yardstick-disposal shape** as a prompt; it is not proof the synergies are absent. **[E3-48] —
  the guidance record against outturn, FY2025** (guidance in EX-99.1 of 2025-02-20 vs 10-K
  actuals): coking tons 7.5-8.0M → **7.6M** ✓ · High CV tons 29-31M → **30.6M** ✓ · PRB tons 36-40M
  → **48.9M** (beat) · met cash cost $96-100 → **$96.13** ✓ (on a measure that excludes the fire) ·
  High CV cash cost $38-40 → **$40.99** ✗ · PRB cash cost $13.75-14.25 → **$13.15** (beat) · capex
  $300-330M → **$284.6M** (under) · High CV priced $61-63 → realised **$60.34** ✗. **Operating
  guidance mostly met; the misses were on price, which management does not set.** That is a point
  in their favour.
- [x] **Free cash flow defined to include the acquired company's cash — FIRES, the sharpest flag
  in the file.** Every 2025-26 release defines free cash flow as *"net cash provided by operating
  activities plus proceeds from sales of assets and **unrestricted cash proceeds from the Merger
  with Arch Resources, Inc.**, less capital expenditures and investments in mining-related
  activities."* Q1 2025 (EX-99.1, 2025-05-08): *Net Cash Used in Operating Activities* **−$109,638K**
  · capex −$64,822K · asset sales $6,003K · **Unrestricted Cash Proceeds from Merger $217,593K** ·
  **Free Cash Flow $49,136K**. Without the acquired cash the quarter was **−$168.5M**. The proxy
  letter's FY2025 *"free cash flow of $246.1 million"* is the same construction: **$217.6M of it is
  Arch's cash** (proxy Appendix A), leaving **$28.5M**. *Is this candor or its opposite* **[E2-26]**?
  The reconciliation is printed every quarter, so nothing is hidden from a reader of the table; but
  the headline number and the capital-return target are computed on it (below), and a
  half-owner would want to be told in the headline that the program's first year was paid out of
  the balance sheet it bought. Scored as a flag on presentation, with the reconciliation's
  existence recorded in management's favour.
- [x] **Serial share issuance [E5-15] — does NOT fire as promotion; recorded.** Two issuances, both
  acquisitions for stock: **8.0M shares** for the CONSOL Coal Resources roll-up (2020) and **24.3M**
  for Arch (2025) (XBRL `StockIssuedDuringPeriodSharesAcquisitions`, cross-read to the FY2025 10-K
  Note 2). Between them, repurchases. Arch's own record carried warrant exercises ($19.5M in 2022, $44.2M in 2023,
  cash-flow statements) and a 2020 convertible. Not the promotion pattern; the stock-deal law
  **[E5-44]** is scored below.
- [ ] **Weak accounting / unintelligible footnotes** — the notes are long but legible; the pro forma
  was correctly filed by incorporation; the 10-K/A refiled only two wrong images in a technical
  report (*"Due to administrative error"*).
- [ ] **[E4-30] fraud tells** — no smoothing (the series is violently unsmooth); cash taxes paid
  $0.5M in 2025 on a pretax loss, $39.2M in 2024 — consistent with the income, not a tell.

**The flags converge [E4-52].** EBITDA as headline and pay metric + a pay metric adjusted to its
threshold to the dollar + a free cash flow that counts the target's cash + a synergy yardstick
retired unquantified. Read together they are one system pointing the same way — **toward numbers
that look better than owner earnings** — and the corpus treats a confluence as a different event
from a sum. It stays a prompt, not a verdict, because the reconciliations are all printed.

**STEP 3 — THE PRIMARY TEST [E2-01].** Return on equity capital, multi-year, no gimmicks. Each
company on its own filed equity (net income ÷ year-end equity), then Core:

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | TTM 2026-06 |
|---|---|---|---|---|---|---|---|---|
| CONSOL NI / equity | 76.0 / 435.2 = 17% | −9.8 / 553.5 = −2% | 34.1 / 672.8 = 5% | 467.0 / 1,165.8 = 40% | 655.9 / 1,343.4 = 49% | 286.4 / 1,568.2 = 18% | — | — |
| Arch NI / equity | 233.8 / 640.5 = 37% | −344.6 / 283.6 = −122% | 337.6 / 683.9 = 49% | 1,330.9 / 1,365.6 = 97% | 464.0 / 1,479.5 = 31% | — | — | — |
| **Core** NI / equity | | | | | | | **−153.2 / 3,678.2 = −4%** | **100.1 / 3,718.9 = 3%** |

*(TTM net income = FY2025 −$153.2M − H1 2025 −$105.8M + H1 2026 $147.5M. Core's equity carries
Arch at the $2.58bn purchase price; on [E2-73]'s operator denominator — the capital the managers
actually work with — the historical combined book of ~$3.0bn at the close (CONSOL $1,568.2M at 2024-12-31 plus Arch
$1,444.0M at 2024-09-30) would lift 2025 to
about −5% and the TTM to about 3.5%; the conclusion does not move.)* **The "earnings rate on equity
capital" is the coal price with a lag: −122% to +97% at Arch, −2% to +49% at CONSOL.** A primary
test built to read the manager reads the benchmark here; **[E2-37]** is the right lens — *"far more
a function of what business boat you get into than it is of how effectively you row."*

**The half-owner test [E2-26].** Mixed. In favour: one-time items are quantified line by line in
the MD&A (fire costs $101M, insurance $19.4M, merger costs $66M, the UMWA accrual $68M); the
pro forma was filed; guidance tables are specific and mostly met. Against: the free-cash-flow
construction above, and a proxy note that tells the reader of an adjustment made to hit a pay
threshold without saying that is what it did.

**The institutional imperative — score all four [E2-30].**
- [x] **Resists change in direction** — *not ticked as resistance; recorded as the opposite risk.*
  The strategy statement adds rare earth elements, carbon foam, battery anodes and *"critical
  minerals and advanced materials"* (10-K Item 1), with **10%** of the 2025 LTIP weighted on *"Core Innovations
  revenue growth"* (proxy). Prompt for **[E3-40]** loss-of-focus: small in dollars, written into pay.
  *(Box ticked for the innovation-pay prompt, not for resistance.)*
- [x] **Acquisitions materialise to soak up funds** — two all-stock combinations in five years (CCR
  2020, Arch 2025), the second at a price-cycle high in the counterparty's recent history. Prompt,
  not a finding: Arch's board also had a rival bidder (*"Company B"*, S-4/A).
- [ ] **Staff studies justify the leader's craving** — the S-4/A fairness analyses (Moelis for
  CONSOL, PWP for Arch) are the usual banker work; no filed evidence of a craving they were built to
  serve.
- [x] **Peer behaviour imitated** — **capital returns peaked with the price, at both companies and
  in the same years**: Arch paid **$456.4M of dividends in 2022** and bought back $156.8M; CONSOL
  bought back **$399.4M in 2023**; Arch had bought back **$827M in 2017-2019** and then, in 2020,
  lost $344.6M and issued a convertible. Buying at the top of the cycle and issuing at the bottom is
  the pattern **[E5-24]** names: *"what is smart at one price is dumb at another."*

**Capital allocation — the capital return against owner earnings [E2-60, E2-52] — the SWK test the
brief asked for.** The framework was adopted 2025-02-18: *"around 75 percent of free cash flow,"*
mostly buybacks plus a $0.10 quarterly dividend.

| six quarters, Q1 2025 → Q2 2026 | $M | source |
|---|---|---|
| returned to stockholders | **360.1** (repurchases 329.2 for 4.3M shares at avg $77.04; dividends ~30.9) | EX-99.1 2026-08-06 |
| "free cash flow" as the company defines it | **449.6** (49.1 + 131.1 + 38.9 + 27.0 + 55.5 + 148.0) | six EX-99.1 reconciliations |
| — of which Arch's acquired unrestricted cash | **217.6** | EX-99.1 2025-05-08; proxy Appendix A |
| free cash flow excluding the acquired cash | **232.0** | computed |
| — of which Leer South insurance cash in H1 2026 | ~97 ($9.1M Q1, $88.1M Q2) | 10-Q Note / EX-99.1 2026-08-06 |
| **owner earnings, same six quarters** (OCF − SBC − capex − finance-lease principal) | **145.6** (FY2025 −24.3; H1 2026 169.9) | Q4 construction |
| **net cash** (cash + short-term investments − debt and finance leases) at the close → 2026-06-30 | **≈ +384 → +26**, a fall of **≈ 358** | CONSOL 10-K FY2024 balance sheet; Note 2; 10-Q 2026-06-30 |

**The program's own terms say where the money comes from**: *"Any repurchases are to be funded from
available cash on hand or short-term borrowings"* (10-K FY2025, Note 4). **The company says it returned
"approximately 80 percent of its free cash flow." On owner earnings
it returned about 250%; on its own free cash flow without the target's cash, about 155%. The net
cash the two companies brought to the close fell by about the amount returned.** The distribution
was funded by the balance sheet the merger delivered — cash Arch's shareholders were paid for in
stock — plus insurance proceeds and new debt, not by owner earnings.

**Is that [E2-52] or [E2-60]?** [E2-52] (*"dividends that can be paid out only if someone promises
to replace the capital distributed"*) needs a replacement of capital; here the replacing capital
was **Arch's cash, bought with 24.3M new shares** — it fires in substance, not in the letter, and
it is recorded that way. **[E2-60]** fires directly: *"its financial strength"* is one of the three
things maintenance must preserve, and a payout that runs net cash from ~$384M to ~$26M in eighteen
months while owner earnings are $146M consumed strength to pay. **This is the SWK shape's sibling
— not a dividend paid by selling the business, but a buyback paid by spending the acquired
balance sheet.** Management's own defence is on the record and deserves stating at full strength
**[E4-13]**: they expect *"strong and improving free cash flow"* in 2026 on a restored Leer South,
and they bought at an average $77.04 against a $97.47 quote today. **They also know a whole lot
more about the mines than I do.**

**The two buyback conditions [E5-08], and the third [E4-31].**
- (1) *Ample funds for operations and liquidity?* Liquidity was **$1,016M** at 2026-06-30 including
  $474M of cash and short-term investments (10-Q) — ample on the day; but see Q4 strength 3.
- (2) *A material discount to intrinsic value, conservatively calculated?* **Not demonstrable.**
  The conservative end of the owner-earnings range in Q4 is below zero on the post-close record; no
  conservative calculation available to an outside owner shows a discount. **CAPITAL ALLOCATION
  FLAG**, with the humility clause **[E4-13]**, binding position size only — and there is no
  position.
- (3) *[E4-31] Shareholders supplied the information to estimate value?* The per-ton tables and
  reconciliations are good; the headline free cash flow is not.
- **Stock deals run the same law in shares [E5-44]:** CONSOL gave 24.3M shares worth $2.48bn at the
  2025-01-13 close for Arch. Whether their intrinsic value exceeded Arch's is the question the
  corpus asks; on the evidence in Q4 — Arch's segments earned a met margin of $6.23/ton and a PRB
  margin of $1.31/ton in their first combined year and the target's pre-tax loss was $431.4M since
  closing (Note 2) — no conservative case for Arch's value at the price was available either.

**THE GUARDRAIL.**
- [x] Nothing in this Q3 promotes the name.
- [x] **Key-person dependence:** Arch's CEO, Paul Lang, *"separated from service"* on 2025-10-06,
  nine months into a merger of equals (8-K 2025-10-08); CONSOL's Brock holds chair and CEO; the CFO
  role changed hands 2026-08-18 (8-K 2026-08-19). Recorded at Q2 as a defect only if the business
  needed one person — it does not; it needs a price.
- [x] **Is the manager the plan?** The 2026 releases' plan is *"our marquee operating segments now
  shifting into high gear"* and markets that *"rebound"* — the plan is the price **[E2-36]**.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN — no disqualifier found**, with **a live
  CAPITAL-ALLOCATION FLAG and a converging presentation flag [E4-52]** (EBITDA pay, the threshold
  adjustment to the dollar, the acquired-cash free cash flow, the retired synergy yardstick).
  *IN = no integrity finding. NOT a finding that the managers are honest — "sincerity and empathy
  can easily be faked" [E5-17]. IN never promotes, and here it has nothing to promote.*

## Q4 — WILL IT SURVIVE?

> ⛔ **RECORDED, NOT GOVERNING.** Q2 closed the file. Q4 is written in full because the brief asked
> for the rebuilt owner earnings, the senior claims and the survival shape, and because the
> merger perimeter is the whole reason CNR was carried unpriced. **No entry language.**

### THE MERGER PERIMETER — how the break is handled, decided before any mean is taken

**The structural break is dated: 2025-01-14** (Step 0). Standalone CONSOL before; CONSOL plus Arch
after; the share count 29.7M weighted average in 2024 → 51.4M in 2025. **A mean that mixes
standalone CONSOL years with combined Core years, divided by a combined market cap, is refused** —
that is exactly the construction `tools/run.py` printed (Step 0) and the queue guard refused.

**Is a pro forma honest here? Yes, for the pre-close years, on four tests — and it has three named
holes.**
1. **Both companies filed complete audited cash-flow statements for every pre-close year the
   windows use** (CONSOL FY2019-FY2024; Arch FY2019-FY2023 plus nine months of 2024). Nothing is
   estimated; the pro forma is addition.
2. **No inter-company eliminations are needed.** S-4/A: *"Arch and CONSOL have not had any
   historical material relationship prior to the merger. Accordingly, no pro forma adjustments were
   required to eliminate activities between the companies."*
3. **No divestiture changed the perimeter** (HSR expired 2024-10-11 with no remedy, Step 0).
4. **It reconciles to the company's own pro forma where a line exists.** The filed pro forma has no
   cash-flow statement (Step 0), so the reconciliation is to revenue and to the bridge from net
   income: S-4/A FY2023 combined revenue **$5,750,016K** = CONSOL $2,568,877K + Arch $3,163,102K +
   $18,037K presentation reclassification — **the arithmetic sum, to the thousand**. Nine months
   2024: $1,641,020K + $1,924,008K + $33,567K = **$3,598,595K** ✓. Pro forma FY2023 net income
   **$990,996K** against the historical sum of $1,119,930K: the −$128.9M bridge is D&A on the
   purchase-price step-up (−$89.9M, **non-cash**), transaction costs (−$58.0M, cash, one-time),
   accelerated CONSOL awards (−$21.5M, **non-cash**), interest saved (+$6.2M) and tax (+$34.3M,
   mostly deferred). **Of the bridge only the $58.0M of deal costs and ~$6M of interest are cash**,
   so the pro forma operating cash flow is the sum of the two filed operating cash flows with those
   two noted, which is what the table below uses.

**The holes, named:**
- **Arch's Q4 2024 cash flow was never filed** (Arch filed no FY2024 10-K). Pro forma 2024 therefore
  pairs CONSOL's calendar 2024 with **Arch's four quarters to 2024-09-30** (FY2023 − 9M2023 +
  9M2024, all filed). It is misaligned by one quarter and labelled that way everywhere it appears.
  The Note 2 pro forma revenue implies Arch's FY2024 revenue was ~$2,435M (4,599.3 − 2,164.4),
  so its missing Q4 was roughly $0.5bn of revenue — about 11% of the combined year.
- **Arch's 2025-01-01 → 01-13 stub** is in no cash-flow statement (Core's FY2025 includes Arch only
  from the close). Thirteen days; immaterial, noted.
- **Synergies claimed and not in the pre-close numbers**: $110-140M at close, raised to $150-170M
  (Q3). The pre-close pro forma carries none; the post-close record carries whatever was captured,
  unquantified by the company. **An owner reading the pre-close pro forma as the combined company's
  earning power would therefore UNDERSTATE by the synergies and OVERSTATE by the price regime** —
  and the second is an order of magnitude larger (below).
- **Also outside the pro forma:** CONSOL's 2019-2020 cash flow included the CONSOL Coal Resources LP
  minority (distributions to it $22.2M in 2019, $5.6M in 2020) before the 8.0M-share roll-up; the
  cost of Arch's awards accelerated at the close sits in the purchase price, not in any SBC line.

**THE (c) JUDGMENT, disclosed [E2-23, E3-44].** This is a capital-intensive miner, the exception
class of **[E5-20]**: the D&A end is **INVALID** as a maintenance guess, twice over.
- **Pre-close** combined D&A ran **$319M-$388M** against total capex plus finance-lease principal of
  **$369M-$455M** — spending exceeded depreciation in 2019-2022 (by $9M-$136M a year) and ran
  $19M and $9M below it in 2023 and 2024, after the Leer South and Itmann builds were done.
- **Post-close** D&A is **$621.1M** because purchase accounting stepped Arch's PP&E up by ~$1.4bn
  (Note 2; MD&A: *"The assets acquired in the Merger resulted in an additional $382 million of
  depreciation, depletion and amortization expense"*). That step-up is the amortisation of a price
  paid in shares, not a renewal cost. The D&A column is shown below only to display the guess.
- **(c) is therefore judged from total capital expenditure PLUS finance-lease principal.** The
  finance leases are how mining equipment is bought on this balance sheet: finance-lease
  obligations rose from $57.7M to **$127.5M** in six months to 2026-06-30 (10-Q Note 13) and
  *"Equipment Financing"* of **$66.1M** in H1 2025 and $14.3M in H1 2026 was a **non-cash** investing
  item (10-Q cash-flow supplemental). Leaving the principal out would count equipment the business
  requires as if it were free. **Band:** capex + lease principal (the judgment) · capex alone (the
  optimistic display).
- **Where in the band, and the direction of the remaining error:** total capex in 2019-2022
  includes growth builds — Arch's Leer South longwall (started 2021, Arch 10-K FY2021) and CONSOL's
  Itmann mine (construction from 2019, full production 2022, CONSOL 10-K FY2021). So pre-close
  total capex **overstates** maintenance in those years. **Against that**: the PAMC is at capacity
  (Q1), Leer has about six years of reserves at its 2025 rate, and holding unit volume means
  developing Leer West — a replacement cost that total capex will have to carry. The company's own
  forward guide is **$325-375M for 2026** (EX-99.1 2026-08-06) against $284.6M spent in 2025. **The
  judgment sits at the capex-plus-leases end, and the capex end is displayed, not endorsed.**
- **SBC resolves and is complete [E5-06]:** cash-flow add-back FY2025 **$32,918K** vs Note 18 total
  expense **$32,943K** (within $25K); CONSOL and Arch add-backs resolve in every year 2019-2024 (Arch
  *"Employee stock-based compensation expense"*); the 401(k) match ($32.1M in 2025, Note 17) is cash
  and already inside operating cash flow. No stock-settled plan outside the SBC line was found.
  [E3-70]'s market-value measure is not binding here: SBC ran 2-15% of operating cash (15% in 2020's
  trough, 11% in 2025, 2% in the TTM).
- **Asset-retirement cash is already inside operating cash flow** (*"Payments on Asset Retirement
  Obligations"*, $36.2M in 2025; Arch *"Reclamation work completed"*), as are black-lung, retiree
  medical and workers' compensation benefit payments. **Arch's contributions to its PRB reclamation
  fund** ($20.0M 2021, **$116.0M 2022**, $6.3M 2023) are also inside Arch's operating cash flow; they
  are a transfer to a restricted asset, so the table shows them separately as a display.

### Owner earnings — the one number **[E2-23]**

$M; OE = operating cash flow − SBC − capex − finance-lease principal. Pro forma years add the two
filed statements; 2025 and the TTM are Core as filed. Script: `Test Runs/_research 2026-09-13
CNR/oe.py`.

| year | OCF | SBC | capex | lease principal | D&A | **OE (capex + leases)** | OE (capex only) | OE (D&A, display) | Arch reclamation-fund contribution inside OCF |
|---|---|---|---|---|---|---|---|---|---|
| 2019 PF | 664.3 | 34.7 | 436.1 | 18.5 | 318.7 | **174.9** | 193.4 | 310.8 | — |
| 2020 PF | 190.4 | 29.0 | 371.8 | 28.3 | 332.3 | **−238.7** | −210.4 | −170.9 | — |
| 2021 PF | 543.9 | 27.2 | 378.2 | 27.4 | 344.9 | **111.0** | 138.5 | 171.8 | 20.0 |
| 2022 PF | 1,860.5 | 35.3 | 344.2 | 24.5 | 360.2 | **1,456.5** | 1,481.0 | 1,465.1 | 116.0 |
| 2023 PF | 1,493.3 | 35.5 | 343.8 | 25.3 | 387.7 | **1,088.7** | 1,114.0 | 1,070.1 | 6.3 |
| 2024 PF* | 870.3 | 32.9 | 359.9 | 10.5 | 379.8 | **467.0** | 477.5 | 457.6 | 7.5 |
| **2025 Core** | 305.8 | 32.9 | 284.6 | 12.6 | 621.1 | **−24.3** | −11.7 | −348.2 | — |
| **TTM to 2026-06-30** | 565.1 | 9.5 | 305.6 | 23.3 | 643.3 | **226.7** | 250.0 | −87.8 | — |

*\*2024 PF = CONSOL FY2024 + Arch four quarters to 2024-09-30.* Cross-checks: each component is a
filed line (Step 0 lists the documents); CONSOL FY2023 OCF $857,949K and Arch FY2023 $635,374K sum
to the $1,493.3M shown. The standalone components are printed by the script for every year.

**MORE THAN ONE WINDOW — EVERY WINDOW IS PUBLISHED [E4-25, E4-38].** Means, $M:

| window | what it is | OE (capex + leases) | OE (capex only) |
|---|---|---|---|
| 2019-2023, five years | **pre-close pro forma, the corpus default window [E2-42]** | **518.5** | 543.3 |
| 2021-2023, three years | pre-close pro forma, the price spike | **885.4** | 911.2 |
| 2020-2024, five years | pro forma, last five pre-close years | **576.9** | 600.1 |
| 2021-2025, five years | pro forma into the first combined year | **619.8** | 639.9 |
| 2024, 2025, TTM | the trough to date | **223.1** | 238.6 |
| FY2025 | post-close record, one year | **−24.3** | −11.7 |
| TTM to 2026-06-30 | post-close, latest | **226.7** | 250.0 |

**Does any of these cross the close?** The five-year 2021-2025 window and the trough window both
end in combined years. They are admissible **only because every pre-close year in them is itself a
combined pro forma year** — the same two businesses on both sides of the date. What is refused is
the standalone-CONSOL-plus-Core mix; the 2024 row's one-quarter misalignment is carried as a label.

**[E4-41] — NORMALIZE THE MEAN DOWN FOR LUCK, BEFORE TRUSTING IT.** Two favourable exogenous breaks
sit in the windows and are named:
1. **The 2022-2023 price spike.** Arch's own explanation: coking indices *"retreating from the
   historical highs seen in the year ended December 31, 2022, in the aftermath of the Russian
   invasion of Ukraine"* (Arch 10-K FY2023, MD&A). Those two years carry **$2,545M of the $2,592M
   cumulative pro forma owner earnings 2019-2023 — 98%**. Strip them and the other three pre-close
   years average **$15.7M**; the five non-spike years on record (2019, 2020, 2021, 2024 PF, 2025)
   average **$98.0M**.
2. **Insurance proceeds in the TTM**: ~$97M of Leer South recoveries collected in H1 2026 (Q3), which
   repay costs borne in FY2025. The pair nets out across FY2025+TTM; the TTM alone is flattered.

**THE COMBINED RANGE.** Single years run **−$239M to +$1,457M**. Window means run **−$24M to +$885M**.
Normalized for the spike, the pre-close record is **~$16M-$98M a year**; the post-close record is
**−$24M (FY2025) to +$227M (TTM, flattered by insurance)**.

- **Is that range too wide to reach a conclusion? YES — and that is the verdict [E4-25]:** *"Usually,
  the range must be so wide that no useful conclusion can be reached."* The conservative end is
  below zero; the richest window mean ($885M) is nine times the non-spike mean ($98M). **No window can be picked and
  defended**, and the corpus forbids trying.
- **The spread is also a Q4 finding [E5-11]:** the distorted years are not one pandemic or one
  acquisition — **they are the price**, which is the business's permanent condition (Q1, Q2).

### Great, good, or gruesome? **[E4-20]**
- [ ] great
- [ ] good
- [x] **gruesome at the trough, good only on the wave.** It requires $325-375M of capital a year
  (2026 guide) to hold volume, and in the five non-spike years it earned an average **$98M** of owner
  earnings on combined equity of roughly $3bn — *"an inadequate interest rate and requires you to
  keep adding money at those disappointing returns."* In 2022-2023 it earned 40-97% on equity
  (Q3). [E4-43]'s *good* class needs the return to hold on added capital; here it holds only while
  the price does. The class is decided by the wave, which is **[E3-51]**'s surfing run, not a class.

### Staying power — score all three **[E5-11]**, the worst case **[E2-55]**
- **(1) A large and reliable stream of earnings — NO.** Owner earnings were negative in 2020 and 2025
  and ranged from −$239M to +$1,457M in single years.
- **(2) Massive liquid assets — PARTIAL.** Cash and short-term investments **$474M**; total liquidity
  **$1,016M** after $268M of letters of credit (10-Q 2026-06-30). Against it: the legacy claims below
  (~$1.2bn) and surety bonds of **$1,062.5M**. Restricted cash posted as collateral rose from **$39.3M
  to $169.0M** during 2025 (Note 1) — liquid assets moved out of reach by the bonding market.
- **(3) No significant near-term cash requirements — NO.** The 10-Q's own list for the next twelve
  months: *"$70 million on its long-term debt and operating and finance lease obligations, including
  interest; $68 million on its employee-related long-term liabilities … $98 million on its
  environmental obligations and $158 million on its other current liabilities"* — **$394M**, before
  capital expenditure of **$325-375M** (2026 guide) and a capital-return target of ~75% of free cash
  flow. **The capital return is the only discretionary line in that list, and it is the one that has
  been consuming net cash (Q3).**
- **Leverage, named [E4-16, E3-29]:** debt and finance leases **$447.6M** (10-Q), of which $307M is
  tax-exempt bonds at 5.00-5.45% with mandatory tender in March 2035 — long-dated, low-coupon, the
  good kind **[E3-52]**. Covenants: maximum first-lien gross leverage, total net leverage, minimum
  interest coverage (Note 13; in compliance, 0.28x / 0.03x / 35.1x at 2025-12-31), all computed on
  a *"Consolidated EBITDA"* — **[E2-54] asks the other question**: interest of **$40.1M** in 2025
  against owner earnings of −$24.3M was **not** covered out of cash flow net of capex; the TTM's
  $226.7M covers it 5.7x, with the insurance.

### THE CLAIMS SENIOR TO SHAREHOLDERS — from the notes, FY2025 10-K (2025-12-31) unless stated

| claim | amount | cash paid 2025 | the note's own words / source |
|---|---|---|---|
| **Asset retirement obligations** (mine reclamation, perpetual water treatment, gas-well plugging) | **$534.7M** (current $38.7M); **$522.2M** at 2026-06-30 | $36.2M | Note 8: $247.7M → $534.7M, **$254.5M assumed with Arch**, accretion $42.3M, revisions +$26.4M |
| — funds held against it | **$148.9M** (PRB fund $131.6M; Pennsylvania water trust $17.3M) | contributions $2M/yr min to the trust | Note 8: the fund *"will serve to defease the long-term asset retirement obligation for its Powder River Basin thermal asset base"*; PADEP trust for *"22 legacy mine water treatment systems"* at a PV of $74.8M |
| **Coal workers' pneumoconiosis (black lung)** | **$285.7M**; $280.9M at 2026-06-30 | $28.3M | Note 16: $161.9M → $285.7M, **$118.6M assumed with Arch**; self-insured |
| — the collateral rule | 100% of projected black-lung liabilities | — | Note 16: OWCP final rule effective 2025-01-13 *"requires a security amount equal to 100% of a self-insured operator's projected black lung liabilities"*; 10-Q: in July 2026 the OWCP *"published proposed rule changes … which eliminates the 100% collateral requirement"* — **a regime moving in the company's favour, not a certainty** |
| **Retiree medical (OPEB)** | **$205.5M**, unfunded; $203.8M at 2026-06-30 | $18.2M | Note 15: $41.4M assumed with Arch; *"no assets in the OPEB Plan"* |
| **Workers' compensation** | **$46.8M** self-insured + **$41.0M** insured plan acquired ($4.5M reimbursable) | $11.7M | Note 16 |
| **Pension** | qualified plan **overfunded** by $49.6M (assets $515.4M vs PBO $489.1M incl. non-qualified); non-qualified **$23.3M** unfunded | $1.7M contributions | Note 15: frozen 2015; no 2026 trust contribution expected |
| **Coal Act multi-employer (UMWA Combined Fund, 1992 Plan)** | **~$29.9M**, off balance sheet | $3.2M | Note 17 |
| **UMWA 1974 Plan indemnification** | accrual **$67.9M** PV at 2024-11-08 over five years | in other liabilities | CONSOL 10-K FY2024 Note 23 |
| **Surety bonds** (not liabilities — performance promises) | **$1,072.0M** (environmental $859.4M); $1,062.5M at 2026-06-30 | — | Note 22 |
| **Letters of credit** | **$268.4M** | — | Note 22 |

**Total recognized legacy claims ≈ $1.17bn** (ARO $534.7M + black lung $285.7M + OPEB $205.5M +
workers' comp $87.8M + non-qualified pension $23.3M + Coal Act $29.9M), **≈ $1.02bn net of the
$148.9M of reclamation funds** — about **21% of the market cap**, against **$447.6M** of funded debt.
These claims are paid in cash every year regardless of the coal price: **~$98M in 2025** (ARO
$36.2M + black lung $28.3M + OPEB $18.2M + workers' comp $11.7M + Coal Act $3.2M), already inside the
operating cash flow above — which is why owner earnings are the right place to see them and why a
cash-flow screen never does. **The merger roughly doubled every one of them**: Arch brought $254.5M
of ARO, $118.6M of black lung and $41.4M of OPEB.

### Name the specific way THIS business dies **[E2-27, E3-24]** — at the strength its holders would accept [E4-51]

**The mechanism: a price trough long enough to outlast the balance sheet, in a business whose
senior claims do not shrink with the price and grow when a mine closes.**

*The holders' case first, stated fairly:* Core has almost no funded debt, $1.0bn of liquidity, two
first-quartile longwall complexes, a contract book (2026: 30.9M High CV tons priced at $58.00, 50.3M
PRB tons at $14.27, 6.0M coking tons at $120.86 — EX-99.1 2026-08-06), a paid insurance claim, a
45X credit on met coal production costs from 2026 to 2029, a federal PRB royalty cut, and an
administration protecting the coal fleet. A trough does not kill a company with no maturities before
2035.

*The arithmetic that answers it,* **modelling exposure, not experience [E4-40]**:
- **At FY2025's prices and costs, the business did not cover its own reinvestment**: owner earnings
  −$24.3M with capex of $284.6M. At the **2026 capex guide's midpoint of $350M**, the same year is
  about **−$90M**. The met segment's cash margin was **$6.23/ton** and the PRB's **$1.31/ton**; in
  Q2 2026 the PRB's was **−$0.57/ton**.
- **The cash the company had to meet that** went from ≈$384M of net cash at the close to ≈$26M
  (Q3), largely into buybacks. A second trough year at 2025's economics with the program running
  consumes the rest; the revolver ($600M, due 2029, EBITDA covenants) and the receivables facility
  then carry it.
- **What does not shrink:** ~$98M a year of legacy benefit and reclamation cash, $1.06bn of surety
  bonds whose collateral the bonding market sets (restricted cash +$130M in 2025), and the black-lung
  collateral rule if the July 2026 proposal does not become final.
- **What grows when a mine closes:** closure brings forward the ARO (the PRB fund exists precisely
  because Arch was *"shrinking our operational footprint at our Powder River Basin operations"* and
  pursuing *"strategic alternatives for our thermal assets, including … potential divestiture"* —
  Arch 10-K FY2023) and ends the revenue that pays the black-lung and retiree tails. PRB is 48.9M of
  Core's 88.5M tons at a $1.31 margin; its thermal demand is the one the filing says gas and
  renewables displace.
- **The outcome:** not a default — there is too little debt — but **a decade in which the business
  pays its retirees, its reclamation and its equipment and returns nothing, while the reserve
  depletes.** That is the permanent-impairment form [E5-29] means, and it requires no bankruptcy.

**Likelihood: [x] a real possibility** (a multi-year trough at 2025 economics: the met realisation has
been $102-$132 a ton since 2024 against $224 in 2022, and East Coast coking coal *"continue[s] to lag Australian
price indices by a historically wide margin"*, EX-99.1 2026-08-06) · a **low-level possibility** of
insolvency on the current debt stack.

**THE SURVIVAL SHAPE — compared against the six named.** Not ORCL (nothing is contracted not to
stop); not ARM (SBC is 3-11% of operating cash, not all of it); not BE (the pro forma gives seven
filed years); not BA (no cash is being spent undoing past work, though the Leer South fire was a
year of it). **Nearest to SWK** — the distribution was not funded by owner earnings — **but the
source differs**: SWK sold the business; Core spent the balance sheet it acquired. And not
ACVA/FLNC — nobody lends Core its balance sheet; its senior claimants are retirees, miners with
black lung and the reclamation regulator. **A seventh shape, named: THE LONG TAIL ON A SHORT CYCLE**
— a price-taker whose senior claims (reclamation, black lung, retiree medical) are fixed in dollars
and measured in decades, set against earnings that are set by a commodity cycle measured in years.
Survival depends on the **average price across the tail**, not on any one year; the balance sheet is
the only buffer between the two clocks, and in this file the buffer was paid out.

- **VERDICT (RECORDED, NOT GOVERNING): [x] OUT on staying power** — two of [E5-11]'s three strengths
  fail (no reliable stream; significant near-term cash requirements) and the third is partial —
  **and the owner-earnings range is too wide for a conclusion [E4-25]**, which on its own would be
  UNKNOWABLE. Both are recorded; neither governs, because Q2 already closed the file.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
*Q2 closed the file. This block exists so that no reader has to guess what the quote implies; it
carries no entry language, ranks nothing, and applies no margin of safety (operator rule 3).*

**Inputs:** price **$97.47** (2026-09-11 close, aggregator, flagged) × **49,636,257** shares (10-Q
cover, `0001710366-26-000054`) = cap **$4,838.0M** · sovereign **5.35%** (US Treasury 30-year,
2026-09-11). Owner earnings are after interest, cash taxes and every legacy benefit and reclamation
payment (all inside operating cash flow), so they are set against the equity cap directly; net debt
of roughly **$0** (cash and short-term investments $474M against debt and finance leases $447.6M)
does not move the answer.

**1. THE YIELD — on every window Q4 published, none picked**

| owner-earnings base (capex + lease principal) | $M | yield | vs sovereign 5.35% |
|---|---|---|---|
| pre-close pro forma, 2021-2023 (the spike) | 885.4 | **18.3%** | +12.9 pts |
| pro forma, 2021-2025 | 619.8 | **12.8%** | +7.5 pts |
| pro forma, 2020-2024 | 576.9 | **11.9%** | +6.6 pts |
| **pre-close pro forma, 2019-2023 — the corpus's five-year default [E2-42]** | 518.5 | **10.7%** | +5.4 pts |
| post-close TTM to 2026-06-30 (includes ~$97M of insurance) | 226.7 | **4.7%** | −0.7 pts |
| trough to date: 2024 PF, 2025, TTM | 223.1 | **4.6%** | −0.7 pts |
| **[E4-41]-normalized: the five non-spike years on record** (2019, 2020, 2021, 2024 PF, 2025) | 98.0 | **2.0%** | −3.3 pts |
| post-close FY2025 | −24.3 | **−0.5%** | −5.9 pts |

**THE FLOOR [E4-28].** The ~10% honest expectancy is cleared **only on windows that contain 2022 and
2023**, and those two years are 98% of the pre-close five-year total (Q4). On the [E4-41]-normalized
record, on the post-close record, and on the trough-to-date record, the price yields **−0.5% to
4.7%** — below the sovereign, far below the floor. The corpus's instruction is to strip a favourable
exogenous break before trusting the mean; stripped, the name is quit on.

**2. WHAT THE PRICE ALREADY ASSUMES**
- **Year-1 growth needed to justify the quote at the bare 5.35%** (perpetuity arithmetic, the engine
  only): on the normalized $98M base, **+3.3% a year forever**; on the TTM $227M, **+0.7%**. **To reach
  the ~10% floor instead**: **+8.0%** on the normalized base, **+5.3%** on the TTM.
- **In words — what the buyer at $97.47 is paying for:** owner earnings of about **$484M a year** to
  earn the floor with no growth. The pro forma business has produced that in **two years of the seven
  on record** — 2022 and 2023, the war-spike years — and in no other. **The price is a bet that the
  2022-2023 price regime returns, or recurs often enough to average in.**
- **What the business has actually done:** volume is capacity-capped (PAMC at ~28.5M tons full
  capacity, already selling 24-27M); price is set by benchmarks it does not control; cost per ton has
  risen 45-57% since 2020-21 (Q2). **The ceiling [E2-63]** is explicit: *"limited upside potential
  also unless more capital is continuously invested"* — growth here is a new longwall, not a price
  increase.
- **The base rate [E4-35]** on sustained growth applies to the 8.0% case: a fewer-than-one-in-twenty
  event among the best businesses, asked of a depleting commodity producer.

**3. WHAT YOU ARE PAID**
- On the normalized record: **−3.3 points** under the sovereign. On the post-close TTM: **−0.7
  points**. Over the sovereign only on spike-inclusive windows.

**WHERE CERTAINTY IS PRICED [E3-42]:** not reached — sovereign used bare, no premium, no margin.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01] — arithmetic at the ~10% floor, not a valuation:**
- normalized non-spike record ($98M): **roughly $1bn, ~$20 a share**
- post-close TTM ($227M, with insurance): **roughly $2.3bn, ~$45 a share**
- pre-close five-year pro forma ($519M, spike included): **roughly $5.2bn, ~$105 a share**
- **current price $97.47** — at the top of that span, inside only the spike-inclusive case.

**WHICH BAR?** Neither — **[ ] Normal method [ ] Screamer test**, both closed by the hard sequence. For
the record only: **the price is not below the conservative case; it sits above every case that
excludes 2022-2023.** **Windage count: 0.**

- **VERDICT: not opened — Q2 OUT. Ranking position: none.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Nothing is bought, so nothing is sold, and no price alert is armed.** A name that failed at Q2
failed on the business; an alert would be a category error (the QLYS ruling, 2026-09-07). **The
refutation conditions, written in advance [E1-02], for whoever reopens this name:**

**What would reverse Q2 OUT — each a filed fact, not a price:**
1. **A cost advantage shown to be WIDE through a trough.** A multi-year filed record in which Core's
   met or High CV cash margin per ton stays materially positive **while the peer row's goes to zero or
   below** — the [E2-58] exception evidenced relatively, not asserted. The 2025 record is the opposite:
   met $6.23/ton, PRB $1.31/ton.
2. **A cost advantage shown to be SUSTAINABLE.** Cash cost per ton flat or falling in real terms over
   five years **[E4-32]**, not the +45% (PAMC, 2021-2025) and +57% (Arch/Core met, 2020-2025) on record,
   and technical-report cost assumptions that stop being revised up (Leer South $52.39 → $75.99, Arch
   10-Ks FY2021 → FY2023).
3. **A price the company sets.** An MD&A that attributes realised price to the company's own pricing
   decisions rather than to *"Newcastle prices"*, *"API2 pricing"* and *"benchmark prices"* — the test
   of [E3-03] criterion 2.
4. **The regime test [E2-59].** Profits that hold if the 45X met-coal credit (sunsets 2029), the federal
   royalty reduction and the executive-order support for the coal fleet are removed. Until then the
   floor belongs to the regime.

**What would reverse the recorded Q3 flags:** synergy capture quantified against the $110-140M
announcement case in a filing **[E4-39]**; free cash flow restated without the acquired cash; a
capital-return target stated against owner earnings or against a published intrinsic-value
estimate **[E5-25]**; no pay metric adjusted to its threshold.

**What would reverse the recorded Q4 OUT:** positive owner earnings, after capex and lease principal,
on a five-year **post-close** window that does not depend on a price spike or insurance; net cash
rebuilt rather than distributed; the black-lung collateral proposal final.

**Monitoring dates — for a reader, not triggers:**
- **Q3 2026 10-Q / EX-99.1 (expected early November 2026):** H2 2026 capital return against owner
  earnings; PRB volumes and the −$0.57/ton Q2 margin; whether the insurance-flattered H1 repeats.
- **FY2026 10-K (February 2027):** 2026 outturn against the $325-375M capex guide and the $86-91 met
  cash-cost guide; any quantified synergy statement; Leer West development spending.
- **The OWCP black-lung collateral rule** — final form of the July 2026 proposal.
- **2029-04-30** revolver maturity; **March 2035** mandatory tender of the $307M tax-exempt bonds;
  **2029 year-end** 45X sunset.

**The sell rule [E2-28]** — not applicable; nothing held. **The monitoring question [E3-30]:** is the
2024-2026 margin compression an aberrational cycle or a permanent slip? **This file's answer is that
the question is moot at Q2**: even if the cycle turns, the business is a price-taker whose best years
come from the wave **[E3-51]**, and a franchise is not a claim about when the wave returns.

**Position size:** **zero** — the business failed Q2 **[E3-45]**.

- **VERDICT: not reached — the file closed at Q2. Refutation conditions recorded above; nothing armed.**

---
## SELF-AUDIT
- [x] Questions answered in order; **Q2 is the first non-IN and it closes the file**; Q3 and Q4 are
      recorded under an explicit NOT GOVERNING banner at the brief's instruction; Q5 is headed
      COMPUTATION — NOT A CLEARANCE and carries no entry language; Q6 arms nothing
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — Q1 IN rests on the
      filed mechanism; two general-knowledge statements found in my own drafts (the fate of the
      prior holder of the CNR ticker; Arch's bankruptcy history) were deleted before commit because
      no filing read here states them
- [x] Every UNRESEARCHED verdict names the artifact — **none used**
- [x] Every UNKNOWABLE verdict states what cannot be known — none governs; Q4 records that the
      owner-earnings range is too wide for a conclusion [E4-25], and names why (the price)
- [x] Step 0: the filing was read, with accession numbers; figures cross-checked — FY2025 OCF
      $305,752K, SBC $32,918K, D&A $621,067K, capex $(284,581)K against XBRL; Arch FY2023 OCF
      $635,374K, SBC $25,443K, capex $(176,037)K; the S-4/A pro forma revenue reproduced as the
      arithmetic sum to the thousand; three peer figures re-verified in the cached peer filings
- [x] **Merger perimeter handled explicitly**: close date and exchange ratio from the 8-K; the 8-K/A
      opened (it incorporates, it does not contain) and the S-4/A pro forma read at source; pro forma
      owner earnings built by adding two sets of audited cash-flow statements; the holes named (Arch
      Q4 2024 unfiled, the 13-day stub, synergies); no mean mixes standalone CONSOL with Core; every
      window published
- [x] Owner earnings on multi-year means; seven windows stated; (c) disclosed as a judgment with
      [E5-20] applied (D&A end invalid, twice); finance-lease principal included; SBC verified
      resolved and complete; [E4-41] normalization stated
- [x] Competitor row filled — 6 companies with filed per-ton series across three coal classes, of ~25
      named competitors; foreign and private limits stated, with the reason the class is NONE rather
      than PROVISIONAL
- [x] Sovereign is for the earnings currency, from the issuing authority (US Treasury), dated 2026-09-11
- [x] Value stated as round-number arithmetic at the floor, not a point estimate, under the
      computation heading
- [x] No bar chosen — both closed by Q2; windage count 0
- [x] Price dated (2026-09-11 close); aggregator used for the live quote only and flagged
- [x] Run committed to git with a pathspec after every section (Step 0, Q1, Q2, Q3-Q6, register)

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line: FAIL at Q2 (OUT, on the business).** Core Natural Resources is a price-taker by its own
  description — *"numerous producers selling into all markets that use coal"* — whose cost position
  is second to Warrior's in met coal, level with or behind Alliance and Peabody in thermal and the
  PRB, and whose costs ratcheted faster than its peers' through the 2022 spike and its unwind, so the
  low-cost exception of [E2-58] is neither wide ($6.23 met and $1.31 PRB margin per ton in 2025) nor
  sustainable (+40% met, +45% PAMC cash cost per ton, 2021-2025).
- **Price: $97.47** (2026-09-11) × 49,636,257 = **$4,838.0M**. COMPUTATION — NOT A CLEARANCE: yield
  **−0.5% to 18.3%** across the published windows; **2.0%** on the [E4-41]-normalized record; the ~10%
  floor is cleared only by windows containing 2022-2023.
- **Recorded, not governing:** Q3 IN (no disqualifier) with a live capital-allocation flag and
  converging presentation flags; Q4 OUT on staying power, the range too wide for a conclusion.

### PRIORS — which were refuted [E4-26]
- **Q2 OUT — NOT refuted.** The bull case was built first; its best fact (a $28.48 met margin in Q2
  2026 while Peabody's seaborne met lost $7.04) is real, and did not make one quarter "wide".
- **"The Pennsylvania Mining Complex's longwall cost position is the bull case" — REFUTED in part.**
  The PAMC's filed cash cost ($40.99, 2025) is *above* Alliance's Illinois Basin ($34.71); its margin
  premium came from export prices and fell from +$21.27 (2023) to +$1.97 (2025). **The stronger
  cost-position case in this company is the Leer Complex, and even there Warrior is lower.**
- **"Q4 is where a coal company dies" — CONFIRMED in substance, REFUTED in mechanism.** Not a debt
  death — funded debt is $447.6M, mostly long-dated tax-exempt bonds; the claims that matter are
  reclamation, black lung and retiree medical (~$1.17bn with workers' comp and the Coal Act), and the
  balance sheet that stood between them and the cycle was paid out.
- **[E5-20] "the D&A end may be INVALID" — CONFIRMED, and in the opposite direction after the close**:
  post-close D&A ($621M) overstates maintenance because of the ~$1.4bn purchase-price step-up, while
  pre-close D&A understated it in 2019-2022.
- **"Get the pension" — the pension is not the claim.** The qualified plan is overfunded by $49.6M;
  the unfunded senior claims are OPEB ($205.5M) and black lung ($285.7M).
- **"Q1: can the cash flows be predicted at all [E3-31]"** — answered from the filed volatility: the
  mechanism is simple, the level is not stable; carried to Q2 and Q4 rather than closed at Q1 (the
  OXY precedent).

### THE STRONGEST SINGLE FACT AGAINST THIS CONCLUSION
**In Q2 2026, with the Leer South longwall restored, Core's met segment earned $28.48 a ton at an
$85.65 cash cost while Peabody's seaborne met lost $7.04 and Coronado's Australian operations lost
$26.90 a tonne over the half.** That is a cost position above the marginal producer at a trough price
— exactly the shape the [E2-58] exception describes. The file's answer: it is one quarter; the full
year 2025 margin was $6.23; Warrior's was wider in every year; and the five-year cost trend runs the
wrong way. **If the next eight quarters show Q2 2026's spread held against the whole row, Q2 reopens
(Q6, condition 1).**

### TOOLING DEFECTS FOUND
1. **`tools/run.py` has no perimeter guard.** It priced CNR at a 3.44%-6.58% yield by averaging
   standalone CONSOL FY2023-FY2024 with combined Core FY2025 over the combined cap — the exact error the
   queue regeneration refused. The guard lives in one path and not the other: another two-paths split
   of the kind the resume note records (capitalised software, the share-count denominator, the
   restatement vintage, `run.py`'s vintage routing).
2. **`Screens/2026-09-01 MASTER RUN QUEUE.csv` maps CNR to "Cornerstone Building Brand · Silver
   Ores"** — a stale ticker-to-name mapping in a superseded file; the corrected queue carries no CNR
   row. Harmless now; a reader of the old file would have been told the wrong company.
3. **No tool reads finance-lease principal into (c).** Core buys mining equipment through finance
   leases ($57.7M → $127.5M in six months; $66.1M of non-cash equipment financing in H1 2025); an
   owner-earnings construction that subtracts only `PaymentsToAcquirePropertyPlantAndEquipment`
   understates maintenance on every equipment-lease-heavy miner. **A prompt, not a new number** — the
   run subtracted the filed financing line by hand.
4. **Arch's reclamation-fund contribution sits inside operating cash flow** ($116.0M in 2022) — a
   screen reading OCF sees a restricted-asset transfer as an operating cost. Displayed, not adjusted.
5. **The S-K 1300 "average cash cost per short ton" in reserve footnotes is an untapped time series**
   (Leer South $52.39 → $75.99, Arch 10-Ks FY2021 → FY2023): a qualified person's own cost assumption,
   filed yearly, and a direct [E2-58] sustainability read for every US miner. Not built; recorded.

### DEFECTS IN THE BRIEF
1. **"Arch filed its own 10-Ks through FY2023; CONSOL through FY2024"** is right, and the brief did not
   draw the consequence: **Arch's Q4 2024 cash flow was never filed by anyone**, so a pro forma FY2024
   cannot be built from filed statements alone. The run used Arch's four quarters to 2024-09-30 and
   labelled the misalignment.
2. **"Read the pro forma financial information the company itself filed (8-K/A or S-4) and reconcile
   to it"** — the filed pro forma has **no cash-flow statement**, so owner earnings cannot be reconciled
   to it directly; the reconciliation was done to revenue (exact to the thousand) and to the
   net-income bridge (identifying which adjustments are cash). The instruction assumed a line that
   does not exist.
3. **"Teck/BHP/Glencore (foreign — state the limit)"** omitted the one foreign-operations met producer
   that files US-GAAP 10-Ks: **Coronado Global Resources**, whose Australian series is the only filed
   marginal-producer comparator — and it supplied the bull case's best contrast.
4. **The six named survival shapes did not contain this one.** Core is nearest SWK (a distribution
   not funded by owner earnings) but spent an acquired balance sheet rather than selling the
   business; the file names a seventh, THE LONG TAIL ON A SHORT CYCLE.
5. **"[E2-63] can be decomposed directly"**, set beside the units series - **[E2-63] is the capped-upside row**
   (*"limited upside potential also unless more capital is continuously invested"*); the units test is **[E4-55]**.
   This run used [E2-63] for the ceiling it states (Q1, Q5). The NEGG run found the same line in its brief.

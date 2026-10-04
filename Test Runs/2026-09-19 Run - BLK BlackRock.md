# Company Run — BlackRock, Inc. (BLK) — 2026-09-19

**STATUS: COMPLETE AND FOLDED, register entry 124.** Created from the template before any fetch,
under the write-early protocol (`Screens/WATCHLIST RUN QUEUE.md`), and written and committed
question by question as each closed. WAVE 6 of the operator's watchlist queue.
**VERDICT: Q1 IN · Q2 OUT (on the business) · Q3 IN · Q4 IN · Q5 below the floor · Q6 IN** — with
Q3, Q4 and Q6 **RECORDED, NOT GOVERNING** and Q5 headed **COMPUTATION — NOT A CLEARANCE**, because
the file closed at Q2. Survival shape **#11 THE PASS-THROUGH**, with **#24 THE BOUGHT AVERAGE**
proposed. Nothing armed.
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

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
- rate **5.34 %** · date **2026-09-18** · source (issuing authority) **US Treasury daily par yield
  curve, 30-year, struck fresh for this run on 2026-09-19 via `python tools/sources.py`.** Not
  inherited from any brief and not taken from FRED.
- FX: **none needed.** BlackRock reports in USD and earns overwhelmingly in USD (the Americas were
  **68% of total AUM and 67% of total base fees and securities lending revenue for 2025**;
  EMEA 25%/28%, Asia-Pacific 7%/5% — 10-K FY2025 MD&A). The non-USD share is a Q4 translation
  exposure, recorded there, not an FX adjustment to the sovereign.

### THE REGISTRANT — established from the filings, as the brief required

**Two CIKs exist and the history does NOT span both.** `tools/sources.py:cik_for("BLK")` returns
**CIK 0002012383, "BlackRock, Inc."** EDGAR's submissions file for that CIK carries
`formerNames` = **["BlackRock, Inc.", "BlackRock Funding, Inc. /DE"]**. The older registrant,
**CIK 0001364742**, is today named **"BlackRock Finance, Inc."**, with `formerNames` =
**["BlackRock Inc.", "BlackRock, Inc.", "New BlackRock, Inc."]**, and its **last 10-K was for
FY2023** (`0000950170-24-019271`, filed 2024-02-23); its filing stream stops on 2024-10-01.

The filing states the mechanism: *"In October 2024, in connection with the closing of the GIP
Transaction, New BlackRock also entered into a guarantee … pursuant to which New BlackRock fully
and unconditionally guaranteed, on a senior unsecured basis, the remaining obligations of Old
BlackRock with respect to its previously issued senior unsecured notes"*, and elsewhere
*"BlackRock Finance, Inc. (formerly known as BlackRock, Inc.) (\"Old BlackRock\")"*. The new
holding company files today; the old company survives as a co-obligor and guarantor, and the
10-K publishes combined summarised Obligor Group financials for the two.

**The consequence, and it is a live trap for any XBRL-driven pull:** `companyfacts` for CIK
2012383 begins at **FY2024** (288 tags); the 2009-2023 history sits only under CIK 1364742
(557 tags). **A single-CIK XBRL fetch on BLK returns two years of data and no error.** Every
pre-2024 figure in this run is read from the old registrant's own 10-Ks, named below.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary document: 10-K for FY2025, `blk-20251231.htm`, filed 2026-02-25, accession
  `0001193125-26-071966`, CIK 0002012383.** Read: Item 1 (Business, incl. the technology and
  competition discussion), Item 1A Risk Factors, Item 7 MD&A (AUM roll-forwards by product type,
  client type and active/index, the base-fee/average-AUM tables, the non-GAAP reconciliations, the
  CIP cash-flow reconciliation and the liquidity tables), the consolidated statements of income,
  cash flows and financial condition, and the notes on revenue, acquisitions, borrowings,
  contingent consideration, stock-based compensation and CIPs.
- **Also read in full:** 10-Q for Q2 2026, `blk-20260630.htm`, filed 2026-08-06, accession
  `0001193125-26-337177`; 10-K FY2023, accession `0000950170-24-019271` (old registrant); 10-K
  FY2022, accession `0000950170-23-004343` (old registrant), for the 2021-2023 fee-rate inputs.
- **Figure cross-checked against the filed statement:** the FY2025 **total revenue of $24,216M**
  appears in the consolidated statement of income and reconciles line by line to the
  revenue-by-product-type footnote: base fees and securities lending **$19,179M** (of which
  securities lending **$705M**) + performance fees **$1,424M** + technology services and
  subscription **$1,981M** + distribution fees **$1,355M** + advisory and other **$277M** =
  **$24,216M**. Independently, the base-fee total re-adds from its ten product lines
  (2,167 + 6,043 + 2,018 + 1,532 + 1,332 + 2,350 + 669 + 1,321 + 502 + 1,245 = **19,179**).
  Second cross-check: **operating cash flow of $3,927M** on the GAAP cash-flow statement equals the
  GAAP column of the CIP reconciliation table, whose "excluding CIPs" column is **$7,463M**.
- *If the filing could not be obtained → **UNRESEARCHED**. Name the ladder rung that failed
  and the obstacle.* — **Not reached. Rung 2 (SEC EDGAR primary documents) served every figure.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### Unit economics in my own words, no management language

**BlackRock keeps a sliver of other people's savings every year for as long as the savings stay.**
At 2026-06-30 it had contracts over **$15,344,624 million** of client money. On the full-year 2025
average balance of **$12,603,633M** it kept **$19,179M** — **15.22 basis points, or $1.52 a year
per $1,000 of somebody else's money.** That single line is **79.2%** of 2025 revenue. The rest:
performance fees **$1,424M (5.9%)**, earned only when a return beats a contractual hurdle;
subscription software — Aladdin, eFront, Preqin, Aladdin Wealth, Cachematrix — **$1,981M (8.2%)**;
distribution fees **$1,355M (5.6%)**, which are collected and then largely paid away again (the
matching "distribution and servicing costs" were $2,460M); and advisory and other **$277M (1.1%)**.

On the cost side the business is people and pass-throughs. Employee compensation and benefits
**$8,446M** is 34.9% of revenue. Sales, asset and account expense **$4,460M** (distribution and
servicing $2,460M, direct fund expense $1,767M, sub-advisory $233M) is 18.4% and is mostly money
moving through to intermediaries and funds. General and administration **$2,731M**. There is almost
no plant: **purchases of property and equipment were $375M** against $24,216M of revenue — 1.5%.

**The three things that make the money move, in order of size:**
1. **The market.** In 2025 AUM rose $2,490,267M, of which **$1,483,629M was market appreciation
   and $220,541M was currency**, against $698,261M of net inflows. Roughly two-thirds of the
   revenue growth in a good year is the world's equity markets going up, and it reverses.
2. **The flow.** Net inflows of $698,261M in 2025 on an opening $11,551,251M is 6.0% organic asset
   growth; management reports the same thing priced, as *"9% organic base fee growth"*.
3. **The price.** This is the one the owner should watch, and it is the subject of Q2.

**The perimeter, because two things in these statements are not the owner's and the filer says so.**
(a) **Consolidated investment products (CIPs)** — funds BlackRock seeds or holds a controlling
interest in are consolidated line by line, then almost all of the equity is stripped out again as
noncontrolling interests. At 2025-12-31 CIPs carried **$3,215M of assets and $2,757M of the NCI**,
and the filer publishes a balance sheet with that column removed. (b) **Separate account assets
and collateral held under securities lending agreements — $68,020M — are matched dollar for dollar
by an identical liability**; they gross up total assets from $98,763M to $169,998M and change
nothing. Both separations are the filer's own, quantified at every line, which is what the
half-owner test asks for **[E2-26]**; the run uses them at Q4 rather than inventing its own.

### The scarce input this business controls

**Not the index, and not the price.** The indices are licensed from S&P, MSCI and FTSE. The price
is set by competition and is falling (Q2). What BlackRock does control is **secondary-market
liquidity in listed index vehicles, and the installed base of Aladdin.**

- **ETF liquidity is self-reinforcing and cannot be bought.** ETFs are 42% of long-term AUM and
  produced 45% of long-term base fees. A fund's usefulness to a trader rises with its own trading
  volume, and volume goes where the spread is thinnest — a genuinely scarce input, because a rival
  with identical holdings and a lower fee still cannot manufacture the order book.
- **Aladdin is an installed operating system.** *"Aladdin assignments are typically long-term
  contracts that provide recurring revenue"* and the client runs its whole investment operation on
  it. Switching means re-plumbing a firm.
- **What is NOT scarce:** the product itself. An S&P 500 index fund is a commodity to four decimal
  places, and Q2 tests exactly that.

### Will the fundamentals look broadly the same in ten years?

**Yes, and this is the strongest thing about the name.** A fee on a balance, billed monthly, over
assets people hold for decades. Nothing here needs a new product cycle, a fab, a drug approval or a
content slate. The mechanism in 2036 is the mechanism in 2016. **What will not look the same is the
rate**, and the framework's own instruction is that the direction of the moat metric outranks its
existence **[E4-32]** — so the durability of the *mechanism* is a Q1 finding and the durability of
the *price* is a Q2 finding. They are not the same question and this run keeps them apart.

**Is it simple and stable in character [E3-31]?** Yes on both, with the perimeter above stated.
Nothing in this business requires a forecast of a product, a technology or a commodity price.
**[E4-46]** is satisfied: this was decidable from the filings inside one reading, not five months.

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____
  *A fee measured in hundredths of a percent on a balance of other people's savings, 79.2% of
  revenue, with the two non-owner columns of the balance sheet separated by the filer itself.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

### The three criteria, one line each

- **Needed or desired [x] — yes, unambiguously.** $698,261M of net inflows in 2025 and $867,778M in
  the twelve months to 2026-06-30. Nobody has to be persuaded to want an index fund.
- **No close substitute [ ] — NO, and this is where the file turns.** Two sections below.
- **Not subject to price regulation [x] — correct, there is no price regulation.** But note what
  [E2-59] warns: regulation *caps* a franchise and *floors* a commodity business, and neither
  creates the class. There is no administered price here at all. The price is set by competition,
  and the filing says so in Item 1A.

### Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]**

**Not a great manager.** The iShares platform survives any individual, and **[E4-23]** is satisfied:
nobody needs to know who runs an S&P 500 tracker. **No key-person moat defect is recorded here**,
and this run does not use Q3 to promote or demote the name.

**But the basis of the advantage is being periodically replaced with purchased product, and that is
the class [E4-04] excludes.** The framework's test is *"does a lapse in spending destroy the
structure, or merely narrow it — and does the spending defend the same advantage, or buy its
replacement?"* On these filings the spending buys the replacement:

| | GIP | Preqin | HPS |
|---|---|---|---|
| closed | 2024-10-01 | 2025-03-03 | 2025-07-01 |
| consideration, net of cash acquired | **$12,949M** | **$3,123M** | **$12,221M** |
| paid in | $2,913M cash + **6.9M shares at $5,904M** (struck at ~$855 after a two-year registration discount off a $950 quote) + **$4,200M deferred stock** | **$3,219M cash** | **8.5M Subco Units at $8,452M** + **$3,400M deferred units** + $613M of debt repaid |
| goodwill | **$10,278M of $12,949M — 79.4%** | $2,377M of $3,123M — 76.1% | $6,841M of $12,221M — 56.0% |

**$28.3 billion in twenty-one months, $22.0 billion of it paid in the company's own paper, with
$8,429M of contingent consideration still outstanding — GIP 4.0 to 5.2 million shares, HPS 2.8 to
4.4 million Subco Units.** Add the closing paper to the contingent maximum and **up to 25.0 million
shares and units — 15.4% of the 162.5 million now outstanding — will have been handed to the sellers
of two private-markets managers.** Goodwill and intangibles went from $33,643M at 2022-12-31 to
**$63,251M at 2025-12-31, against total BlackRock, Inc. stockholders' equity of $55,888M: tangible
equity is NEGATIVE $7,363M**, against positive $4,101M three years earlier. ElmTree and SpiderRock
sit inside the same programme and inside the $120,961M of AUM the roll-forward labels "Acquisitions".

**Why that is a Q2 finding and not merely a Q3 one is arithmetic, and it is in the next section:
the price of everything BlackRock already owned fell in every single year, and the only thing that
stopped the blended rate falling was the bought book.** The spending is not defending the same
advantage. It is buying a different, higher-priced product to hold up an average.

### Primary moat metric, filing-sourced, and its trend

**The metric is the effective fee rate on average assets under management, in basis points** — base
fees (investment advisory, administration fees and securities lending revenue) divided by the
filer's own full-year average AUM, which BlackRock defines as *"the average of the month-end spot
AUM amounts for the trailing thirteen months."* It is the right metric for the reasons the BAM run
of 2026-09-13 gave and this run re-tested: it **is** the price of the product, so it is what
**[E2-44]** (raise prices with flat demand), **[E3-33]** (untapped pricing power) and **[E4-37]**
(the agony of a price increase) are actually about; every competitor files it or its inputs; and it
is the first thing to move when close substitutes exist. **No figure was inherited from the BAM
row: all of them were recomputed here from the filings.**

**Sources: 10-K FY2025 `0001193125-26-071966` (2024, 2025); 10-K FY2023 `0000950170-24-019271`
(2022, 2023); 10-K FY2022 `0000950170-23-004343` (2021); 10-Q Q2 2026 `0001193125-26-337177`
(H1 2026). Arithmetic and inputs: `Test Runs/_research 2026-09-19 BLK/feerates.py`, output in
`feerates.txt`.**

| segment, bp on average AUM | 2021 | 2022 | 2023 | 2024 | 2025 | H1-26 ann. | **2021→2025** |
|---|---|---|---|---|---|---|---|
| **TOTAL** | **16.29** | **16.15** | **15.62** | **14.90** | **15.22** | **15.25** | **−6.6%** |
| **ETFs (all)** | **20.41** | **19.21** | **18.48** | **17.31** | **16.92** | **17.14** | **−17.1%** |
| Equity, active | 55.14 | 50.38 | 48.82 | 46.93 | 43.65 | 42.02 | **−20.8%** |
| Fixed income, active | 20.79 | 19.44 | 17.55 | 17.23 | 17.06 | 16.95 | **−18.0%** |
| Multi-asset, active | 19.21 | 17.94 | 15.28 | 13.55 | 12.42 | 12.03 | **−35.4%** |
| Non-ETF index | 3.83 | 3.80 | 3.79 | 3.52 | 3.52 | 3.47 | **−8.1%** |
| Private markets / illiquid alts | 70.49 | 66.71 | 69.64 | 77.36 | **89.85** | 80.06 | **+27.5%** |
| Cash management | 6.61 | 12.01 | 13.05 | 13.01 | 12.76 | 12.72 | +93.1% |

**Read it in the order that matters.**

1. **Every product BlackRock owned throughout the window got cheaper. Every single one.** ETFs
   −17.1%, active equity −20.8%, active fixed income −18.0%, active multi-asset −35.4%, non-ETF
   index −8.1%. **There is no organically-owned line in this company whose price rose.**
2. **The two lines that rose did not rise on price.** Cash management's 6.61bp in 2021 is a
   zero-interest-rate artefact — money-market fee waivers, and the filer states *"Investment
   advisory and administration fees for investment funds are shown **net of fee waivers**"*; from
   2022 the series reads 12.01 → 13.05 → 13.01 → **12.76 → 12.72, which is falling.** Private
   markets rose +27.5% because **GIP and HPS were bought**: that leg's average AUM went from
   $154,597M to $261,535M in a single year, $101,017M of it arriving as "Acquisitions" in the
   filer's own roll-forward, and the acquired books price higher than the legacy alternatives did.
3. **Take the bought leg out and the total is not flat — it is down 13.4%:** ex-private-markets,
   **15.74bp (2021) → 13.64bp (2025)**. The 15.22bp of 2025 is a mix effect purchased for
   $28.3 billion.
4. **The second reading says the same thing without using a rate at all.** AUM $10,010,143M at
   2021-12-31 → **$14,041,518M at 2025-12-31, +40.3%.** Base fees **$15,260M → $19,179M, +25.7%.**
   **Revenue grew 14.6 percentage points slower than the assets it is charged on over four years —
   and that is *after* $28.3bn of acquired, higher-priced AUM was added to the numerator.** This is
   **[E4-55]** inverted, exactly as the BAM run found it: volume flatters the dollars while the
   price per unit falls, and the rate is the honest series.
5. **Direction is what the framework weighs. [E4-32]:** the moat *widened every year* is *"the
   primary criterion of a great business"* — *"that does not necessarily mean that the profit is
   more this year than last year."* Here the profit is more and the moat is narrower. Every
   direction available in these filings points the same way.

**The filer says it, in Item 1A, and the word to notice is "additional":** *"This evolution,
together with the introduction of new technologies, as well as regulatory changes, continues to
alter the competitive landscape for investment managers, **which may lead to additional fee
compression** or require BlackRock to invest more to modify or adapt its product offerings to
attract and retain customers … Increased competition on the basis of any of these factors,
**including competition leading to fee reductions on existing or new business**, may cause the
Company's AUM, revenue and earnings to decline."* A business with no close substitute does not warn
about *additional* fee compression, because it has no first instalment to add to.

**And in Item 1 the filer names price as a competitive factor and claims no pricing power anywhere:**
*"Key competitive factors include investment performance track records, **the efficient delivery of
beta for index products**, investment style and discipline, **price**, client service and brand name
recognition."* "The efficient delivery of beta" is a description of a commodity, written by the
market leader.

**One more line from the MD&A, about a third of the assets:** *"institutional non-ETF index
assignments tend to be very large (multi-billion dollars) and **typically reflect low fee rates**.
Net flows in institutional index products generally have a small impact on BlackRock's revenues and
earnings."* **Non-ETF index is 29.8% of average AUM and 6.9% of base fees, at 3.52bp.** Four
trillion dollars of AUM are, on the company's own account, nearly immaterial to its earnings.

### THE COMPETITOR ROW — required **[E3-28]**

> *"I can't be an intelligent owner of a business unless I know what all the other businesses in
> that industry are doing."* — **[E3-28]**

**One specification for every line: the effective fee rate on average assets under management, in
basis points, from that company's own filing, for the five most recent fiscal years.** Where the
filer publishes the rate, the filer's rate is used and its definition is quoted; where it publishes
only period-end AUM, the average of beginning and ending AUM is used and labelled as computation,
not disclosure. Supporting evidence, verbatim definitions, accession numbers and arithmetic checks:
`Test Runs/_research 2026-09-19 BLK/peers/PEER_ROW.md`.

| Company | metric, as the filer defines it | 2021 | 2022 | 2023 | 2024 | 2025 | direction | source accession |
|---|---|---|---|---|---|---|---|---|
| **BLK (subject)** | base fees ÷ 13-month average AUM | **16.29** | **16.15** | **15.62** | **14.90** | **15.22** | **−6.6%; −13.4% ex private markets** | `0001193125-26-071966` |
| **State Street (STT)** | management fees ÷ average of opening and closing AUM — **my computation: STT publishes neither a fee rate nor an average AUM** | 5.40 | 5.09 | 4.95 | 4.82 | **4.62** | **−14.4%** | `0000093751-26-000124`, `0000093751-24-000498` |
| **Invesco (IVZ)** | its own *"U.S. GAAP gross revenue yield on AUM"* | 48.7 | 44.5 | 40.4 | 37.4 | **33.7** | **−30.8%** | `0000914208-26-000079` |
| **Invesco (IVZ)** | its own *"Net revenue yield ex performance fees"* — **definition changed in FY2025 to include QQQ; do not splice** | 39.1 | 35.5 | 32.4 / 28.4 | 30.2 / 25.4 | **23.0** | **down on every vintage** | `0000914208-26-000079`, `0000914208-25-000114` |
| **Invesco (IVZ)** | investment management fees ÷ its own published average AUM — my computation, matched to the others' construction | 33.31 | 30.01 | 27.36 | 25.36 | **23.08** | **−30.7%** | `0000914208-26-000079`, `0000914208-23-000297` |
| **T. Rowe Price (TROW)** | its own *"Investment advisory annualized effective fee rate (EFR)"*, excluding performance-based fees | 44.4 *(incl. perf. fees; the ex-perf. recast starts 2022)* | 42.6 | 41.9 | 41.0 | **39.4** | **−11.3% on the ex-perf. series, 2022→2025** | `0001628280-26-008002`, `0001113169-25-000007`, `0001113169-22-000005` |
| **Franklin Resources (BEN)**, FY to 30 Sep | its own *"effective investment management fee rate excluding performance fees (investment management fees excluding performance fees divided by average AUM)"*, on a 13-month average AUM | 41.8 | 41.6 | 42.1 | 41.1 | **40.5** | **−3.1%**, and a composite: Legg Mason, Lexington, Alcentra and Putnam all closed inside the window | `0000038777-25-000238`, `0000038777-23-000169` |
| **Blackstone (BX)** | management and advisory fees ÷ fee-earning AUM; the firm's own *"Annualized Base Management Fee Rate"* is **0.86%** | — | — | — | — | **92.2** *(86.2 on base fees)* | flat-to-down on its own disclosure | `0001193125-26-082531` *(figure from the committed BAM row of 2026-09-13; **not recomputed in this run**)* |
| **Brookfield Asset Mgmt (BAM)** | base management fees ÷ fee-bearing capital | — | — | 90.4 | 85.0 | **85.8** *(82.4 annualised in H1 2026)* | **down 8bp in two and a half years** | `0001628280-26-013098` *(committed BAM row; **not recomputed**)* |

- **Peers named: 8 lines covering 6 filing-sourced competitors**, plus the substitution test below,
  out of an industry that has perhaps a dozen real competitors to the index and ETF business and
  another dozen in private markets. **Buffett says eight [E3-28]; this row runs eight lines and
  names every one it could not pull.**

**THE DECISIVE READING OF THE ROW, and it is not that BlackRock is cheapest.** Of course it is
cheapest: 15.22bp against TROW's 39.4 and BEN's 40.5 is a statement about **product mix**, not about
franchise. BlackRock sells index beta; they sell active management. **What the row actually shows is
that the price of every asset-management product on it is falling at the same time, and that
BlackRock is falling too.** Six independent filers, six different definitions, six different
fiscal calendars, and one direction: **−6.6%, −14.4%, −30.8%, −11.3%, −3.1%, and −8bp on
fee-bearing capital.** **[E3-03] criterion 2 is a claim about the customer's alternatives, and the
customer is getting a better price every year from everybody.** This is [E2-58]'s equation applied
to a fee rather than a commodity price: capacity is ample, nobody administers the price, and the
long-run profitability is set by how often supply is tight — which, in an industry where the
marginal unit of index capacity costs almost nothing to add, is never.

### THE SUBSTITUTION TEST, which is criterion 2 at its sharpest

The competitor row is a *revenue* comparison across different products. Criterion 2 asks something
narrower: **is there a close substitute for the thing BlackRock actually sells?** For the product
that is 42% of long-term AUM and 45% of long-term base fees, the answer can be read off two
SEC-filed prospectuses, side by side, to the basis point.

| fund | manager | index tracked | total annual fund operating expenses, **2026** | same fund, **2021** | filing |
|---|---|---|---|---|---|
| **iShares Core S&P 500 ETF (IVV)** | **BlackRock Fund Advisors** | S&P 500 | **0.03%** | **0.03%** | iShares Trust 485BPOS, filed 2026-07-27, acc. `0001193125-26-318131`; 2021 filed 2021-07-26, acc. `0001193125-21-223259` |
| **Vanguard 500 Index Fund, ETF Shares (VOO)** | Vanguard | S&P 500 | **0.03%** | **0.03%** | Vanguard Index Funds 485BPOS, filed 2026-04-28, acc. `0000036405-26-000181`; 2021 filed 2021-04-29, acc. `0001683863-21-002763` |
| **SPDR S&P 500 ETF Trust (SPY)** | State Street Global Advisors | S&P 500 | **0.0945%** (capped by waiver to 2027-02-01) | **0.0945%** | SPDR S&P 500 ETF Trust 485BPOS, filed 2026-01-26, acc. `0001193125-26-022316`; 2021 filed 2021-01-14, acc. `0001193125-21-008848` |
| **iShares Core S&P Total U.S. Stock Market ETF (ITOT)** | **BlackRock Fund Advisors** | S&P Total Market | **0.03%** | — | acc. `0001193125-26-318131` |
| **Vanguard Total Stock Market Index Fund, ETF Shares (VTI)** | Vanguard | CRSP US Total Market | **0.03%** | **0.03%** | acc. `0000036405-26-000181`; 2021 acc. `0001683863-21-002763` |

**Two managers, the same index, the same exposure, the same price to four decimal places, for at
least five years.** That is not a near-substitute; on the only dimension a buyer of beta can
compare — cost of tracking — **it is the same product.** And the rival is structurally unable to be
out-priced: Vanguard's management company is owned by the funds it manages and runs them at cost, so
there is no margin to defend and no shareholder to disappoint. **[E3-03] criterion 2 fails on a
filed document, not on an inference.**

**What the substitution test does NOT say, stated at full strength because [E4-26] requires the
disconfirming read on the favourite hypothesis.** It does not say iShares has no advantage. iShares
crossed **$6 trillion** in AUM and *"roughly doubl[ed] in three years"* (8-K EX-99.1, 2026-07-15),
and the secondary-market liquidity of IVV is a genuine, unbuyable asset — a trader will pay a wider
implicit cost in a thinner fund at the same expense ratio. That is why iShares keeps winning share
at 3bp. **But an advantage that shows up as volume at a price you cannot raise is a scale advantage,
not a franchise**, and the framework has a name for what it does to the owner: **[E3-62]**'s second
step — *"how much is going to stay home and how much is just going to flow through to the
customer"*. The answer is in the table above: the savings went to the customer. Fee rate down 17.1%
on ETFs while ETF AUM rose 84% and ETF revenue rose 33%.

### The remaining Q2 tests, each answered

- **Untapped pricing power [E3-33, E5-28] — NO, and the opposite.** Claiming this class is claiming
  *"a monopoly or a near monopoly"* **[E5-28]**. BlackRock has ~13% of a market where the number two
  charges the identical price at cost and the number three is $6.6 trillion in the same product.
  There is no filed evidence of a price BlackRock could raise and has not. **[E4-37]**'s inverse
  metric — the agony of a price increase — cannot even be measured here, because in five years of
  filings **there is not one instance of a price increase to agonise over.** Rates went one way.
- **The two-characteristic test [E2-44] — fails on the first half, passes on the second.** Can it
  raise prices with flat demand and spare capacity? No: it cut them with *rising* demand. Can it
  grow dollar volume with only minor additional capital? **Yes, emphatically** — $375M of capex on
  $24.2bn of revenue, and AUM up $4.0 trillion in four years with no plant. **A business that
  passes the second half and fails the first is the definition of an efficient commodity producer.**
- **The second question is a number [E3-46]** — high returns on capital employed over time. GAAP
  return on average BlackRock, Inc. equity: **14.3% (2023), 14.7% (2024), 10.7% (2025)**, and
  **[E2-43]**'s unleveraged-net-tangible-assets denominator is now **negative**, so the honest
  reading is that the operating business earns a very high return on the tangible capital it uses
  and the *purchase price* of the acquired managers has been added to the denominator the
  shareholder actually funded. Both facts are true and both belong in the file.
- **The dominance class [E2-53] — NO.** *"Once dominant, the newspaper itself, not the marketplace,
  determines just how good or how bad the paper will be."* BlackRock is the largest manager on
  earth and **does not determine its own price**; the marketplace does. It is the clearest possible
  negative on this test: maximum scale, zero price-setting.
- **The attacker's test [E2-45].** With ample capital and skilled people, how would I compete with
  it? Exactly as Vanguard does: file the same index fund at the same 3bp and win on cost of capital,
  because a client-owned manager needs no margin. That attack is **already running and already
  works**, which is why criterion 2 fails.
- **Four causes of extreme success [E4-36] — which one is this?** Not an extreme max/min of one
  variable, not a nonlinear combination. It is **wave-riding [E3-51]**: the four-decade migration of
  the world's savings from active to index vehicles, which BlackRock rode better than anyone.
  *"When a surfer gets up and catches the wave and just stays there, he can go a long, long
  time."* **A surfing run is not a moat; the advantage lives in the wave.** The BAM run rejected
  wave-riding as a moat under [E3-51] and the same rejection applies here, to a different wave —
  with one honest difference recorded below.
- **Units, where units exist [E4-55].** The physical series here is AUM and it is rising strongly;
  the price series is falling. That is the inverse of Precision Steel and it is the benign form of
  the test: the franchise is not hiding a volume collapse behind price rises. **It is hiding a price
  collapse behind volume rises**, and the framework's answer is the same — take the honest series.

### THE CASE FOR IN, BUILT AT FULL STRENGTH AND REJECTED **[E4-26, E4-51]**

*[E4-51] requires a bear case its holders would accept as fairly stated. The same discipline is owed
to the bull case at the gate that closes the file.*

**The strongest case for a franchise, stated as its holders would state it.** BlackRock is not
selling a commodity; it is selling **access to the deepest pool of secondary liquidity in listed
index vehicles**, and that is not replicable with money. Iron evidence: it has taken share for a
decade at a price identical to Vanguard's, which means buyers are choosing iShares *for something
other than price* — the order book, the securities-lending revenue shared back into the fund, the
options market built on the ETF, the ability to trade $10bn in an afternoon. Aladdin is a second,
genuinely different business: **$1,981M of revenue growing 10.5% organically, on long-term
contracts, with an installed base that cannot switch cheaply.** The private-markets build is not a
treadmill but a one-time widening of the product set into the only part of the industry where fees
are 90bp instead of 3bp, and the earn-out revaluing **upward by $720M** in 2025 says HPS is
outperforming the case underwritten at the deal. And the total fee rate has been **essentially flat
for two years — 14.90, 15.22, 15.25 — while AUM went from $11.6tn to $15.3tn**: the compression is
decelerating, not accelerating. Cash management, 7% of AUM, is now a structurally profitable
12-13bp business it was not in 2021.

**Why it does not carry, one line each:**
1. **Criterion 2 is decided on a filed document, not on a judgment.** IVV 0.03%, VOO 0.03%, five
   years unchanged. A franchise is *"thought by its customers to have no close substitute"*
   **[E3-03]**, and the customer can read both prospectuses in a minute.
2. **Every organic product got cheaper, every year, without exception.** Direction outranks
   existence **[E4-32]**, and there is no counter-direction anywhere in the table.
3. **The flat blended rate is bought, not earned.** Strip the acquired private-markets book and the
   rate fell 13.4%. $28.3bn — $22.0bn of it in shares and units, up to 15.4% of the company — is
   what "flat" cost, and the moat's basis is being replaced rather than defended **[E4-04]**.
4. **The advantage is scale on a wave [E3-51, E4-36]**, and the gains from scale went to the buyer,
   not to the owner **[E3-62]**. Twenty-five per cent revenue growth on forty per cent asset growth
   is the arithmetic of a pass-through.
5. **Aladdin is real and it is 8.2% of revenue.** It cannot carry the classification of the other
   91.8%, and its own fees are *"generally determined using the value of positions on the Aladdin
   platform"* — i.e. partly the same market-linked base as everything else. Q4 records it; Q2
   cannot promote the whole on a twelfth.
6. **There is no untapped pricing power and no instance of a price increase in five years of
   filings [E3-33, E5-28, E4-37].**

**A conclusion that required fighting for it is worth less, not more [E4-18].** This one needed no
fighting: the subject's own Item 1A warns of *additional* fee compression, its own Item 1 lists
price as a competitive factor, and its own rate table falls in every organic line.

- **Class: [ ] WIDE  [ ] NARROW  [ ] NONE  [ ] PROVISIONAL → the class is NARROW AND NARROWING.**
  **Direction: DOWN, in every organically-owned product, in every year measured.**
- **Any peer unavailable?** **Yes, two, and both are named with the artifact that would resolve
  them, and neither can reverse the finding:**
  - **Vanguard** — the management company files no 10-K (it is owned by the funds it manages and
    has no public equity). **Resolved differently and better:** its *funds* file with the SEC, and
    the price of the actual substitute is taken from its own 485BPOS above. Not UNRESEARCHED.
  - **Fidelity (FMR LLC)** — private, no 10-K. **UNRESEARCHED, artifact named:** the Fidelity
    Concord Street Trust 485BPOS containing the fee table for the Fidelity ZERO index funds
    (CIK 0000819118; the four 2026 filings located — `0000819118-26-000018`, `-26-000072`,
    `-26-000136`, `-26-000137` — carry the Part C exhibit lists and the ZERO funds' names but the
    prospectus fee tables were not located in them). It matters only in one direction: a rival
    charging **zero** would strengthen the criterion-2 failure, never reverse it.
  - **Amundi** — **not an SEC registrant** (Euronext Paris). **UNRESEARCHED, artifact named:**
    Amundi's Universal Registration Document / annual report, English edition, which publishes a fee
    margin in basis points. Same one-directional logic: Amundi is a price-taker in European ETFs and
    has been cutting, not raising.
  - **The moat class is NOT held PROVISIONAL on these two absences**, and the reason is the one the
    BAM run gave: the row already decides, and the two missing filers can only push the same way.
    Holding the class provisional here would be *"narrowing assumptions until the answer appears"*
    in reverse **[E4-18]**.

- **VERDICT: [ ] IN  [x] OUT — ON THE BUSINESS. Permanent.**
  **Criterion 2 of [E3-03] fails on a filed price.** The product that is 42% of long-term AUM and
  45% of long-term base fees is sold by a rival at **0.03% against BlackRock's 0.03%**, unchanged
  for five years, and that rival is structurally incapable of needing a margin. Every organically
  owned product's price fell in the measured window — ETFs −17.1%, active equity −20.8%, active
  fixed income −18.0%, active multi-asset −35.4%, non-ETF index −8.1% — and the blended rate held
  only because **$28.3 billion, $22.0 billion of it in the company's own shares and units, bought a
  higher-priced book [E4-04]**. Base fees grew **14.6 points slower than the assets they are charged
  on** over four years **[E4-55]**. There is no untapped pricing power and not one filed instance of
  a price increase **[E3-33, E5-28, E4-37]**. The record is a **surfing run [E3-51, E4-36]** on the
  indexing wave, and the gains from scale flowed to the customer **[E3-62]**. **[E2-53]** is the
  sharpest single reading: the largest asset manager that has ever existed does not set its own
  price.
  *Not UNRESEARCHED: the row is complete on one metric, one window, from primary filings, and the
  substitution test is decided from two prospectuses. Not UNKNOWABLE: the evidence is in and it
  decides. **This is a very good business. It is not a franchise.***

**⛔ THE FILE CLOSES HERE. Q3, Q4, Q5 and Q6 below are RECORDED, NOT GOVERNING** — written because
the operator's instruction of 2026-09-01 requires a price and a refutation record on every name, and
because a run that stops writing at the closing gate destroys the evidence a future reader would
need to reopen it. **Q5 carries the heading `COMPUTATION — NOT A CLEARANCE` (operator rule 3) and
no entry language appears anywhere below.**

**THE COMPETITOR ROW — required [E3-28].** A moat is a claim about *relative* position.

| Company | same metric | same window | source |
|---|---|---|---|
| **[subject]** | | | |
| | | | |
| | | | |

- Peers named: ____ of the industry's ____ real competitors. *(Buffett says eight; take as
  many as the industry has and say how many you took.)*
- Any peer unavailable (private / foreign / unsegmented)? → **moat class PROVISIONAL**, and
  that is **UNRESEARCHED** until the filings are pulled.
- **Untapped pricing power** — could a manager raise the return simply by raising prices,
  and has not? **[E3-33]** ____
- Class: [ ] WIDE [ ] NARROW [ ] NONE [ ] PROVISIONAL · Direction: ____
- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — **RECORDED, NOT GOVERNING**
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`. The file closed at Q2 on the
business. Nothing below can reopen it, and nothing below is used to promote the name
**[E2-37, E2-38, E3-39]**.*

**STEP 1 — THE WEIGHT CASE.**
*How much damage can this manager do before I can react?*
- [x] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**Case declared, and why: Q3 would be a BINARY GATE.** The 1977 root **[E2-70]** is the
governing one: where *"their only products are promises"*, an undifferentiated product
**magnifies** the manager. That is a literal description of this business as Q2 found it —
BlackRock's product is a promise (to track, to manage risk, to act as fiduciary, to keep
Aladdin running) delivered every day across $15.3 trillion of other people's money, and Q2
established that the product itself is undifferentiated from Vanguard's. A single conduct or
operational failure — in securities lending, in proxy voting, in a fund's tracking, in the
Aladdin platform on which clients run their own operations — is not recoverable by price.
**Leverage is NOT ticked:** borrowings $12,768M against $55,888M of equity is 0.23x, there is
no maturity before March 2027, and the $68,020M of separate-account assets is matched dollar
for dollar by an identical liability. **Control is NOT ticked:** this is a public-market
position with a daily exit.

**Honesty — binary, permanent, filings-based [E5-16].** *"understanding about business
mistakes; tolerance for personal misconduct is zero."*
- **No personal-misconduct matter is found in the filings.** The Note 16 contingencies
  disclosure is the standard receives-subpoenas-from-time-to-time language plus one named case.
- **The one named matter, dated as the filing dates it:** *"BlackRock is currently defending a
  lawsuit filed by thirteen state Attorneys General in Federal Court in the Eastern District of
  Texas against BlackRock, State Street, and Vanguard, alleging antitrust violations on the
  theory that the three companies conspired to artificially suppress coal supply. Four states
  are also pursuing alleged violations of state consumer protection laws regarding statements on
  BlackRock fund websites. **In 2025, the court largely denied defendants' motion to dismiss.**"*
  (10-K FY2025, `0001193125-26-071966`, Note 16.) **Read under [E5-22]** — penalty size is not
  seriousness in either direction, and the failure that counts is not acting when you learn. This
  is a live, surviving antitrust claim against the three largest index managers jointly, and the
  survival of a motion to dismiss is a fact, not a finding. **It is not a conduct disqualifier on
  the filed record, and it is recorded as a matter to watch, not as a verdict.**
- **[E5-16] is satisfied in the only form the corpus permits [E5-17]: no disqualifier was found.
  That is not a finding that these managers are honest.**

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30, E2-49, E3-50, E2-57, E3-53, E2-52].**
*Accounting and disclosure, not litigation. Each is a prompt to READ, never a verdict
**[E5-36]**, and a fired flag is not a venality finding **[E5-38]**.*

- [ ] **weak accounting — NOT FOUND, and in several places the accounting is better than it
  needed to be.** Stock compensation is expensed in full. Consolidated investment products are
  consolidated line by line and then *separated for the reader* in a published reconciliation.
  Contingent consideration is marked to fair value through income, and the 2025 mark was a
  **$720M charge taken to the income statement**, not buried. Deferred tax liabilities of
  $4,618M are disclosed against the acquired intangibles. No pension assumption issue.
- [ ] **unintelligible footnotes — NO. The opposite.** The filer publishes (a) a consolidated
  balance sheet with the CIP and separate-account columns removed to an "As Adjusted" column,
  (b) a GAAP-to-excluding-CIPs cash-flow reconciliation for two full years, (c) the full
  non-GAAP reconciliation line by line, and (d) in the proxy, the BPIP payout matrix in advance.
  This run's Q4 owner-earnings separation of the consolidated funds is **performed using the
  filer's own arithmetic**, which is the strongest available evidence on [E2-26].
- [x] **trumpeted earnings projections / growth targets — FIRES.** In the 10-K strategy section:
  *"BlackRock's investments in infrastructure, private credit, and alternatives-to-wealth
  underpin its **ambition to raise $400 billion in private markets by 2030**."* In the Q2 2026
  earnings release (8-K EX-99.1, 2026-07-15, `0001193125-26-304013`), the CEO: *"**8% organic
  base fee growth – well in excess of our target**"*, *"a nearly 46% adjusted operating margin,
  double-digit EPS growth, and increasing capital return"*, *"I've never been more optimistic
  about the growth"*. **[E5-30] is the reason this matters more than it looks:** *"once you
  start it, it's all over. You can't quit … And forecasting earnings, I can't imagine anything
  more destructive."* A target the CEO measures himself against in public every ninety days is a
  ratchet, not a fact about 2026. **[E4-35]** sets the base rate the $400bn-by-2030 ambition has
  to face: fewer than 10 of the 200 most profitable companies were wagered to compound EPS at
  15% for twenty years, and *"lofty targets corrode CEO behavior"* is the flag itself.
- [x] **serial share issuance — FIRES on the facts, and the reading changes what it means.**
  **6.9M shares for GIP, 8.5M Subco Units for HPS, and 4.0-5.2M + 2.8-4.4M more contingent — up
  to 25.0M shares and units, 15.4% of the 162.5M outstanding.** But **[E5-15]** describes a
  *dribble-out* pattern — *"one of the surest indicators of a promotion-minded management, weak
  accounting, a stock that is overpriced and — all too often — outright dishonesty"* — and this
  is not that: it is acquisition consideration, disclosed at every line, alongside $1.6bn of
  annual repurchase. **The flag's proper destination is [E5-44], not [E5-15]:** *"The intrinsic
  value of the shares you give in an acquisition **must not be greater than the intrinsic value
  of the business you receive**."* Measured at IV, not at quote. On the closing paper alone,
  $22.0bn of shares and units bought books producing **$2,350M of base fees and $695M of
  performance fees in 2025 — 7.2x combined fee revenue**, before the contingent $8,429M. The GIP
  shares were struck at **~$855 after a two-year registration discount off a $950 quote**, which
  is a real, disclosed, shareholder-favouring haircut. **Judgment recorded: not obviously wrong,
  not obviously right, and not resolvable from the filings. It is not scored as a disqualifier.**
- [x] **adjusted-earnings promotion [E4-29] — FIRES AT FULL STRENGTH on the adjusted-earnings
  limb, and reads CLEAN on the EBITDA limb.** *The CGNX standing rule of 2026-09-07 was
  followed: the 8-K EX-99.1 earnings release and the proxy were both pulled before scoring this
  flag.* **The word "EBITDA" appears zero times in the FY2025 10-K, zero times in the Q2 2026
  earnings release, and zero times in the 2026 proxy.** That deserves saying plainly: BlackRock
  does not do the thing the corpus calls *"a particularly pernicious practice"*. What it does
  instead:
  - **The earnings release headline is the adjusted number:** *"BlackRock Reports Second Quarter
    2026 Diluted EPS of $12.19, **or $13.91 as adjusted**"*. The phrase "as adjusted" appears
    **35 times** in that release.
  - **FY2025 GAAP diluted EPS $35.31; "as adjusted" $48.09 — a gap of $12.78, 36.2%.** In 2024
    the same gap was $1.60, 3.8%. **The gap grew nine-fold in one year.**
  - **GAAP operating margin fell 37.1% → 29.1%. "Operating margin, as adjusted" went 44.5% →
    44.1%.** The add-backs that did it: amortisation and impairment of intangibles **$775M**,
    **acquisition-related compensation costs $738M**, acquisition transaction costs $122M, the
    contingent-consideration mark **$720M**, the Charitable Contribution $109M, the restructuring
    charge $39M, deferred-comp market moves $52M — **$2,555M in 2025 against $536M in 2024.**
  - **The denominator is reduced too**, which raises the margin independently of the numerator:
    revenue for the margin measure is $21,756M rather than $24,216M, after removing $1,355M of
    distribution fees and $1,105M of investment advisory fees.
  - **[E3-53] and [E5-33] govern two of the add-backs directly.** Restructuring charges and
    retention compensation are *real costs*, and *"to tell owners year after year, 'Don't count
    this' … is misleading."* $738M of pay to retain people the company bought is the most
    ordinary cost imaginable. **[E2-57]** is the same point from the other side: the adjusted
    apparatus is *"except for"* institutionalised at eight lines, and *"you must count the runs
    scored against you in all nine innings."*
  - **Why it matters here and not only as a disclosure point:** the 10-K states that the Company
    uses operating margin, as adjusted, *"to determine the long-term and annual compensation of
    the Company's senior-level employees."* **The pay metric is the metric that excludes the cost
    of the acquisitions.** That is **[E4-27]**: *"Never, ever, think about something else when
    you should be thinking about the power of incentives."*
- [ ] **filed-figure tells [E4-30] — DO NOT FIRE.** *Cash taxes as a share of pretax income:*
  **33.3% (2021), 17.0%, 19.5%, 20.5%, 30.2% (2025)** — cash taxes paid $2,298M on $7,619M of
  pretax income in 2025, against a 22.0% book rate. **Rising, not falling**, and cash tax above
  book tax in the latest year. *Smoothness:* GAAP operating income **7,450 → 6,385 → 6,275 →
  7,574 → 7,045** is visibly lumpy; nothing is unnaturally smooth. **The smooth series is the
  adjusted one**, which is the point already made above, not a separate tell.
- [x] **metric-switching [E2-49] — FIRES as a prompt; the reading is genuinely mixed, and the
  positive half is real.**
  - *Three definitional changes inside the window, each disclosed with a reason and with prior
    periods recast:* non-GAAP definitions updated in Q1 2023 to exclude deferred-cash-comp market
    moves; the AUM and base-fee product-line presentation reclassified in Q1 2025 (*"Such line
    items have been reclassified for 2023 and 2024 to conform to this new presentation"*, with
    the reclassified 2024 figures pointed to an 8-K exhibit); and, **in Q3 2025, at the moment of
    the HPS closing**, adjusted EPS redefined to *"assume all outstanding Subco Units issued as
    part of the consideration for the HPS Transaction have been exchanged … on a one-for-one
    basis"*. Announcing a change ahead with reasons is the candour case [E2-49] explicitly
    allows, and all three qualify on that test.
  - **But the yardstick was not discarded — it was kept because it is insulated.** The BPIP
    target for adjusted operating margin was **raised from 41.5% (2023-2025 cycle) to 44.0%
    (2026-2028 cycle)** while GAAP operating margin **fell from 37.1% to 29.1%**. The pay
    bullseye moved up 2.5 points while the filed number moved down 8.
  - **The positive half, and it is strong.** BlackRock publishes the entire BPIP payout matrix in
    advance and then reports the prior cycle's outturn against its own pre-set target:
    *"BlackRock achieved above-target level results in the 2023-2025 performance cycle, with
    three-year average annual Organic Revenue Growth of **$716 million** (above Target Level of
    **$640 million**) and Operating Margin, as adjusted, of **43.4%** (above Target Level of
    **41.5%**). Accordingly, participants received … **116.6%** of the base number of units."*
    **That is [E2-49]'s demand for "pre-set, long-lived and small bullseyes" honoured almost to
    the letter, and it is the [E3-48] artifact done well** — guidance set, published in advance,
    and outturn reported against it. It is recorded as a credit.
- [ ] **dividends funded by issuance [E2-52] — DOES NOT FIRE.** Dividends and Subco distributions
  $3,347M against ex-CIP operating cash of $7,463M; no equity was raised for cash.
- [x] **stock-price targeting [E3-50] — FIRES, and this is the sharpest single finding in the
  file.** The 2026 proxy (`0001308179-26-000262`, filed 2026-04-10) prints the **"2025 NEO
  Pre-Set Performance Scorecard"**. Under *Financial Performance · Priority 1: Drive profitable
  growth*, the scored measures are, in the proxy's own order:
  > *"◦ **Next 12-Month P/E Multiple (including relative premium)** ◦ **Total Shareholder
  > Return** ◦ Diluted EPS, as adjusted ◦ Operating Income, as adjusted"*

  **[E3-50]** describes managers whose premise is *"that their job at all times is to encourage
  **the highest stock price possible** (a premise with which we adamantly disagree)"*, and names
  the next step: *"unadmirable accounting stratagems."* **Writing the forward price/earnings
  multiple — and the relative premium to peers — into the CEO's pre-set scorecard is that premise
  formalised into a pay formula.** It is not the share price as an outcome; it is the
  *multiple the market applies* as a scored objective. The positive doctrine the corpus states
  instead is a price *"in a narrow range centered at intrinsic business value"*, with
  overvaluation as unwelcome as undervaluation. Nothing in this proxy expresses that preference.
- [x] **restructuring charge [E3-53] — FIRES, small.** $39M (2025), nil (2024), $61M (2023),
  $91M (2022). Each disclosed and each added back in the adjusted metric. **This run's owner
  earnings are computed from cash flow, so the charges stay in the mean, as [E5-33] requires.**

**CONVERGING FLAGS ARE A DIFFERENT EVENT [E4-52].** Four of the fired flags point one way:
(a) an adjusted-earnings apparatus that grew its gap to GAAP EPS to $12.78; (b) a pay scorecard
that scores the forward P/E multiple and total shareholder return; (c) buybacks announced as a
**dollar quantity in advance** rather than as a price condition (below); (d) a $400bn-by-2030
target and a quarterly organic-base-fee-growth target the CEO measures himself against in
public. **Read together, as [E4-52] instructs — *"extreme consequences from confluences … it
dominates life"* — they describe a management system optimised for the share price and scored on
a metric that excludes the cost of the acquisitions the system is making.** Two corpus
constraints bind the reading and are applied: **[E5-38]** — a fired flag is not a venality
finding, and people one would trust with one's wallet *"would play games with any number that
came to them"*; and **[E2-30]**'s last clause — *"Institutional dynamics, not venality or
stupidity, set businesses on these courses."* Every one of these practices is the industry
standard. That is the point of [E2-30], not an excuse for it.

**STEP 3 — THE PRIMARY TEST [E2-01].** *"The primary test of managerial economic performance is
the achievement of a high earnings rate on equity capital employed (without undue leverage,
accounting gimmickry, etc.) **and not the achievement of consistent gains in earnings per
share**."* Balance sheet before income statement.

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Total BlackRock, Inc. stockholders' equity, year end ($M) | 37,693 | 37,744 | 39,347 | 47,495 | **55,888** |
| Net income attributable to BlackRock, Inc. ($M) | 5,901 | 5,178 | 5,502 | 6,369 | **5,553** |
| **Return on average equity, GAAP** | **16.2%** | **13.7%** | **14.3%** | **14.7%** | **10.7%** |
| Return on average equity, "as adjusted" net income | — | — | — | 15.2% | 15.0% |
| Goodwill + intangibles, net ($M) | — | 33,643 | 33,782 | 46,692 | **63,251** |
| **Net tangible equity ($M) [E2-43]** | — | **+4,101** | **+5,565** | **+803** | **−7,363** |
| Diluted EPS, GAAP | 38.22 | 33.97 | 36.51 | 42.01 | **35.31** |
| Diluted EPS, as adjusted | — | — | — | 43.61 | **48.09** |

**The series is the test's own opposition, running in both directions at once.** GAAP return on
the equity shareholders actually funded **fell from 14.7% to 10.7%**, and GAAP EPS fell from
$42.01 to $35.31 — while **adjusted EPS rose 10% to $48.09**, the metric used to set senior pay
held at 44.1%, and the CEO was rated **"Far Exceeds Expectations"** with a total incentive award
of **$43.5 million, up 24%**, on total annual compensation of **$45.0 million**. [E2-01] was
written to prefer the first number and distrust the second, and here they disagree by the widest
margin in the window.

**[E2-43] must be applied and it changes the denominator question.** *"Unleveraged net tangible
assets"* is *"the best guide to the economic attractiveness of the operation"*, with the goodwill
wedge reported separately, never hidden in book equity. **BlackRock's net tangible equity is
negative $7,363M**, so a return-on-tangible-equity figure cannot be computed at all. The honest
statement of the two facts: **the operating business earns an extremely high return on the
tangible capital it employs** (it employs almost none — $1,256M of property and equipment), **and
the purchase price of the acquired managers has been added to the equity the shareholder funded**,
which is why the reported rate fell. **[E2-73]** is the third denominator and it says the same
thing from the operator's side: *"what we pay for a business does not affect the amount of
capital its manager has to work with."*

**The half-owner test [E2-26] — PASSES, and it is the strongest thing in this Q3.** *"the
business facts that we would want to know if our positions were reversed."* This filer hands the
reader the separations the reader would otherwise have to construct: the CIP cash-flow
reconciliation, the balance sheet with the CIP and separate-account columns stripped, the
line-by-line non-GAAP bridge, the reclassified prior-year product lines with a pointer to where
they were published, and the pay matrix in advance with its outturn. **The one-time items are
quantified separately at every line, which is exactly the passing case the framework names.**
What the reporting does *not* do is prefer the GAAP number in its own headlines.

**The institutional imperative — score all four [E2-30].** *Not a fraud test.*
- [ ] **resists any change in current direction — NO, the opposite.** It changed direction hard,
  and fast, into private markets and data.
- [x] **projects/acquisitions materialise to soak up available funds — YES.** $28.3bn of
  acquisitions in twenty-one months after a decade in which the largest deal was eFront at
  roughly $1.3bn. The funds available were the share price and a $3bn/$2.5bn pair of note issues
  raised *in advance of* the GIP and Preqin closings, which the 10-K states explicitly.
- [x] **staff studies produced to justify the leader's craving — PARTLY, and disclosed.** Both
  contingent-consideration fair values were *"determined by using the income approach **with the
  assistance of a third-party valuation specialist**"*, on Level 3 inputs including *"estimates
  of the timing and amounts of fundraising and fee related earnings forecasts, cost of equity,
  and future stock price performance."* **[E3-58]** warns that solving capital allocation *"by
  either having a staff that does it, or by hiring consultants"* is *"a terrible mistake"*. The
  valuations were outsourced; whether the decisions were cannot be read from the filing.
- [x] **peer behaviour mindlessly imitated — YES, and it is the clearest of the four.** Every
  large traditional manager bought private-markets capability in the same window: Franklin bought
  Lexington, Alcentra and Putnam; T. Rowe bought Oak Hill Advisors; the pattern is visible in the
  peer 10-Ks pulled for the Q2 row. BlackRock is the largest instance of a universal industry
  move. *"Institutional dynamics, not venality or stupidity, set businesses on these courses."*

**Capital allocation — the buyback conditions [E5-08], with [E4-31]'s third:**
- **(1) ample funds for operations and liquidity? YES.** $11,007M of own cash (CIP cash removed),
  $7,463M of ex-CIP operating cash in 2025, no debt maturity before March 2027, and a $5.9bn
  undrawn facility that **[E5-39]** says not to count.
- **(2) repurchases at a material discount to conservatively calculated IV? FAILS on this run's
  own numbers.** 2025: *"the Company repurchased an aggregate of 1.6 million shares and share
  equivalents for approximately $1.6 billion"* — roughly $1,000 a share, and the Item 5 table for
  October-December 2025 shows **103,520 shares and 370,558 Subco Units at an average price of
  $1,073.40**. Q5 below computes an honest owner-earnings yield of **2.7% to 3.0%** at
  $1,069.78 against a **5.34%** sovereign. On those figures the shares are not at a material
  discount to a conservatively calculated value; they are above any conservative value this run
  can defend.
- **And the form of the commitment is itself the [E5-24] problem.** The Q2 2026 release announces
  *"Increasing planned quarterly share repurchases to **$550 million**"* and *"our conviction in
  the growth ahead for BlackRock led us to increase our **planned level of 2026 share repurchases
  to $2 billion**."* **[E5-24]**: *"what is smart at one price is dumb at another."* A
  pre-announced dollar quantity is a commitment to buy at whatever price arrives, which is the
  opposite of a price condition. Contrast **[E5-25]**, where compliance was made real by
  publishing **both conditions as numbers in advance** — the 110%-of-book ceiling and the $20bn
  liquidity floor. BlackRock publishes the quantity and not the price test. **[E2-51]** cuts the
  other way and is recorded for balance: a manager who *refuses* repurchases when they are
  clearly in owners' interests *"reveals more than he knows of his motivations"* — BlackRock is
  not that manager.
- **(3) [E4-31]'s third condition — shareholders supplied all the information needed to estimate
  value? YES.** The disclosure is good enough that this run could build the whole file from it.
- → **CAPITAL ALLOCATION FLAG, LIVE**, stated with the humility clause **[E4-13]**: this rests on
  *our* IV range, *"it is natural for CEOs to be optimistic about their own businesses. They also
  know a whole lot more about them than I do,"* and **[E5-08]**'s own note that *"many CEOs never
  stop believing their stock is cheap"* — infractions here are innocent. **The flag binds
  position size, never the discount rate. No position is being taken: the file closed at Q2.**

**THE GUARDRAIL — checked before the verdict.**
- [x] Confirmed: **nothing in this Q3 is used to promote the name.** A strong manager cannot
  repair Q2 or substitute for Q4 **[E2-37, E2-38, E3-39]**. The Q2 verdict was written before
  this section and is untouched by it.
- [x] **This business does not require a great manager**, and that was recorded at Q2 as the
  absence of a key-person defect **[E4-23]**, not here as a strength.
- [x] **No great-manager case is being made.** There is no excisable cancer and no Pygmalion
  **[E2-35, E2-36]**: the franchise question failed on price, which no manager can excise.
- **And [E5-32]'s cap is carried:** audited does not mean true. Salomon's books carried an
  invented daily number signed for twelve years. Every filing-based test above sits under
  **[E5-17]**'s ceiling — *"People are not that easy to read. Sincerity and empathy can easily be
  faked."*

- **VERDICT: [x] IN — no disqualifier found. RECORDED, NOT GOVERNING** (the file closed at Q2),
  **with a LIVE CAPITAL ALLOCATION FLAG and four converging disclosure flags [E4-52].**
  *IN = the absence of found disqualifiers, **not** a finding that the managers are honest
  **[E5-17]**. IN never promotes. The sharpest adverse finding is [E3-50]: the forward P/E
  multiple, including its relative premium, is a scored measure in the CEO's pre-set pay
  scorecard. The sharpest favourable finding is [E2-49] and [E3-48] honoured: the pay bullseyes
  are published in advance and the prior cycle's outturn is reported against them.*

## Q4 — WILL IT SURVIVE? — **RECORDED, NOT GOVERNING**

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

### FIRST — HOW THE CONSOLIDATED FUNDS WERE SEPARATED, because the reported line is unusable

**The GAAP operating cash flow of this company is not the owner's cash and the filer says so.**
Funds BlackRock seeds or controls are consolidated line by line ("CIPs"), and **the funds' own
securities purchases sit inside OPERATING activities** while **the money the outside investors put
in to buy them sits inside FINANCING**. The two halves of one transaction are in different
sections, so the reported number moves with fund seeding rather than with the business:

| ($M) | 2023 | 2024 | 2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|
| **Operating cash flow, GAAP, as filed** | 4,165 | 4,956 | **3,927** | 236 | **247** |
| of which: "Net (purchases) proceeds within CIPs" | (1,780) | (2,672) | **(4,214)** | — | — |
| financing: "Net subscriptions received … from noncontrolling interest holders" | +1,627 | +2,405 | **+3,827** | — | — |
| **Impact on cash flows of CIPs (filer's own column)** | (1,519) | (2,311) | **(3,536)** | (1,743) | **(2,859)** |
| **Operating cash flow EXCLUDING CIPs (filer's own column)** | **5,684** | **7,267** | **7,463** | **1,979** | **3,106** |

**In 2025 the reported figure understates the owner's operating cash by $3,536M — 47% of the
truth.** This run therefore uses the filer's own **"Cash Flows Excluding Impact of CIPs"**
reconciliation, published in the 10-K MD&A for 2024 and 2025 (`0001193125-26-071966`), in the
FY2023 10-K for 2022 and 2023 (`0000950170-24-019271`), in the FY2022 10-K for 2021
(`0000950170-23-004343`), and in the 10-Qs for the half-years. It is a non-GAAP measure and it is
flagged as one — but it is a *reconciliation*, quantified at every line, and the same separation is
published on the balance sheet, where a CIPs column of **$3,215M of assets and $2,757M of the
noncontrolling interests** is struck out alongside **$68,020M of separate-account assets matched
dollar for dollar by an identical liability**. **Total assets go from $169,998M to $98,763M once
what is not the owner's is removed. This is the insurer and Up-C treatment applied to a fund
consolidator, and here the filer did the arithmetic for us [E2-26].**

*Two further separations, recorded:* **[E3-04]** look-through — equity-method investees produced
$51M of earnings in 2025 and paid $429M of distributions, so there is nothing to add back; the
yield is not understated on that account. **[E2-23] constraint 3** — the working-capital increment
is netted inside operating cash flow from one audited line, which is why the CONVENTION uses cash
flow at all; the largest single swings were accrued compensation **+$659M (2025)** and **−$711M
(2022)**, which broadly cancel across the window.

**A seasonality warning that no annualisation may ignore.** Year-end incentive compensation is
accrued through the year and paid in the first quarter, so **H1 ex-CIP operating cash was $1,979M
in 2025 against $7,463M for the full year — 26.5%.** H1 2026 was $3,106M. **A trailing-twelve-month
figure built from a half-year is wrong by a factor of nearly two in either direction.** The TTM to
2026-06-30 is $7,463 − $1,979 + $3,106 = **$8,590M**, which is reported below as a fact and is
**not** used as the mean.

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].** *"Using precise numbers is,
in fact, foolish; working with a range of possibilities is the better approach."*
Arithmetic: `Test Runs/_research 2026-09-19 BLK/oe.py` and `oe2.py`, outputs in `oe.txt`, `oe2.txt`.

- **Long-window mean (2021-2025, the corpus default [E2-42, E1-03]):** ex-CIP operating cash
  **$6,450.0M**, less stock pay at the larger of charge and grant value **$1,101.0M**, less (c) →
  **$4,756.0M** at the D&A end, **$4,979.4M** at the capex end.
- **Short-window mean (2023-2025):** ex-CIP operating cash **$6,804.7M**, less stock pay
  **$1,297.7M**, less (c) → **$4,796.3M** at the D&A end, **$5,182.3M** at the capex end.
- **Spread, conservative end:** the two conservative ends are **$4,756.0M** and **$4,796.3M** —
  **0.8%.** The window choice barely matters, which is itself worth recording: there is no
  distorted year doing the work.
- **Combined range (window spread × capex band × SBC measure): $4,756M to $5,583M**, a width of
  **17.4%** around the midpoint. **Is that too wide to conclude [E4-25]? No.** Every end of it
  produces the same Q5 answer by a wide margin, and the framework's instruction is to close the
  file when the range cannot decide — here it decides at every end.
- **A wide spread is also a Q4 finding [E5-11] — and there is no wide spread here.** The window
  spread is 0.8%. What IS distorted is the *per-share* series, below, and the distortion is the
  acquisition programme, not a pandemic or a disposal.

**Owner earnings by year, and per share — the series the total hides:**

| ($M unless stated) | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Operating cash flow excluding CIPs | 6,168 | 5,668 | 5,684 | 7,267 | **7,463** |
| Stock pay, the larger of charge and grant value **[E3-70]** | 786 | 826 | 707 | 1,379 | **1,807** |
| (c) at the capex end | 341 | 533 | 344 | 255 | 375 |
| (c) at the D&A end | 415 | 418 | 427 | 579 | **1,126** |
| **Owner earnings, c = capex** | 5,041 | 4,309 | 4,633 | 5,633 | **5,281** |
| **Owner earnings, c = D&A** | 4,967 | 4,424 | 4,550 | 5,309 | **4,530** |
| Diluted weighted-average shares incl. Subco Units (millions) | 154.4 | 152.4 | 150.7 | 151.6 | **160.9** |
| **Owner earnings PER SHARE, c = capex** | 32.65 | 28.27 | 30.74 | **37.16** | 32.82 |
| **Owner earnings PER SHARE, c = D&A** | 32.17 | 29.03 | 30.19 | **35.02** | **28.15** |

**The per-share read is the one that matters and it is the DIS-style finding.** On the D&A end,
owner earnings per share **peaked at $35.02 in 2024, fell 19.6% to $28.15 in 2025, and are 12.5%
BELOW where they were in 2021.** On the capex end they are **flat over four years: $32.65 →
$32.82, +0.5%.** Assets under management rose **40.3%** over the same four years. **Whichever end
of the band you take, four years of forty-per-cent asset growth produced no growth at all in owner
earnings per share.** That is the Q2 finding arriving in the cash: the price fell, the share count
rose, and the volume made up the difference in dollars but not per share.

- **Maintenance capex — a DISCLOSED JUDGMENT, and here the corpus default runs BACKWARDS.
  Stated openly, because [E2-23] says "(c) must be a guess."**
  The corpus default is D&A **[E3-44, E2-41]**, and the named exception class is the
  capital-intensive filer where D&A *understates* renewal **[E5-20, E4-47]**. **BlackRock is the
  mirror image of that exception: D&A OVERSTATES required maintenance, because $775M of the
  $1,126M of 2025 D&A — 68.8% — is amortisation of intangibles acquired in the GIP, Preqin and HPS
  deals**, and none of that is a capital expenditure the business must make to hold its position
  and volume. It is the write-off of a purchase price already paid — paid in shares and units that
  are **already in the 160.9M denominator above**. Deducting it in (c) as well would charge the
  same cost twice.
  **The judgment, stated: (c) is judged at the capex end — total purchases of property and
  equipment, five-year mean $369.6M — and the acquisition cost enters through the share count and
  the goodwill wedge, not through (c).** The D&A end is carried as the display of the alternative,
  not because it is invalid but because it double-counts. Note that even the capex end is already
  conservative: it uses *total* capex, with no maintenance/growth split, because the filing
  discloses none.
  **Band used: $369.6M to $593.0M (five-year means).** Property and equipment net is $1,256M
  against $24,216M of revenue; this is not a capital-intensive business by any reading.
- **THE THIRD END, disclosed rather than folded into the band, because it is the real (c) question
  for this company.** [E2-23]'s (c) is what the business *requires* to *"fully maintain its
  long-term competitive position"*. Q2 established that BlackRock's blended fee rate held only
  because it bought GIP, Preqin and HPS. **If the acquisition programme is maintenance, then (c)
  includes it**, and the arithmetic is brutal: five-year mean cash paid for acquisitions $1,545.4M
  plus five-year mean stock and units issued for acquisitions $2,919.6M = **$4,465.0M a year**,
  which takes five-year owner earnings from $4,756M to **$291M.**
  **This run does NOT adopt that end, and says why.** Unit volume does not require it: AUM grew
  $698,261M organically in 2025 against $120,961M from acquisitions, and the filer's own
  roll-forward keeps the two apart. The acquisitions bought a *new, higher-priced product line*,
  which is growth, not maintenance. **But the third end is recorded because it is the honest
  statement of what the reader is being asked to believe: that $28.3 billion in twenty-one months
  was optional.** If a future reader concludes it was not optional, owner earnings are an order of
  magnitude smaller, and that judgment is where this file would be reopened.
- **Stock compensation subtracted in full [E5-06], and at the [E3-70] measure, not the charge.**
  The corpus requires *"an amount equal to what the company could have realized by publicly
  selling options of like quantity and structure"*; the reported charge is *"the floor of the
  subtraction, not the measure."* From the stock-compensation note: **grant-date fair market value
  of RSUs granted was $1.7bn (2025), $1.1bn (2024), $565M (2023), $662M (2022), $664M (2021)**,
  plus performance-based RSUs granted of **$107M, $279M, $142M, $164M, $122M**. Totals **$1,807M,
  $1,379M, $707M, $826M, $786M** against charges of **$1,307M, $753M, $630M, $708M, $734M**:
  **grant value exceeds the charge in all five years, by 38% in 2025 and 83% in 2024.** The larger
  figure is used throughout. **SBC RESOLVES and is COMPLETE**: `ShareBasedCompensation` is present
  on the face of the cash-flow statement in every year of both windows, and the grant-value
  disclosure covers every year — neither `SBC_UNRESOLVED` nor `SBC_PARTIAL` applies.
- *If the capex band changes the verdict → **UNKNOWABLE**.* **It does not.** Both ends produce the
  same Q5 answer and the same Q4 answer.
- **Windage count: ONE at Q4** — the SBC measure is taken at the larger of two disclosed figures,
  which is conservative; the (c) judgment is *not* a second application, because it was argued from
  the composition of the D&A line rather than chosen for conservatism, and the conservative
  alternative is displayed beside it. **[E4-11, E4-48]**: the margin is applied once, at the end,
  and Q5 below never reaches a margin because it fails at the floor.

### Great, good, or gruesome? **[E4-20]**
- [ ] great — high return, rising, little capital needed
- [x] **good — attractive return, earned also on added capital**
- [ ] gruesome — grows, eats capital, earns little
- **Evidence, and the word that decides it is "rising".** *"The great one pays an extraordinarily
  high interest rate **that will rise as the years pass**. The good one pays an attractive rate of
  interest that will be earned also on deposits that are added."* BlackRock is unambiguously the
  second and unambiguously not the first: the return is attractive and it is earned on every dollar
  of added AUM with almost no incremental capital ($375M of capex on $24.2bn of revenue), **and the
  rate is falling, not rising — 16.29bp to 15.22bp blended, and down in every organic line.**
  **[E4-43] governs the consequence: the good class PASSES.** *"nothing shabby about earning $82
  million pre-tax on $400 million of net tangible assets."* Only gruesome fails Q4. **This is
  nowhere near gruesome**: it consumes no capital to grow and it earns a high return on the
  tangible capital it uses. It ranks below great at Q5, and that is all [E4-20] does here.

### Staying power — score all three **[E5-11]**
- **(1) large and reliable stream of earnings — PASS, and it is the most reliable revenue line in
  this queue.** $19,179M of base fees billed as a percentage of a $14 trillion balance, monthly,
  under contracts that renew by default. The reliability is qualified by market level, not by
  customer decision: in the worst recent year (2022, global equities down roughly a fifth) base
  fees fell only **5.3%**, from $15,260M to $14,451M, and operating income stayed above $6.3bn.
  **[E3-55]** applies: volatility with a certain mechanism is not a defect.
- **(2) massive liquid assets — PASS, with the bank line NOT counted [E5-39].** Own cash
  **$11,007M** after removing the CIPs' $461M. Investments ex-CIP $10,704M, of which an unknown
  part is illiquid seed and co-investment capital, so it is not counted as liquid either. The
  filer's own "total liquidity resources" of $16,907M includes **$5,900M of undrawn revolver**,
  which *"the kindness of strangers"* rule excludes. **$11.0bn of unencumbered cash against
  $12.8bn of long-term debt and $614M of annual interest.**
- **(3) no significant near-term cash requirements — PASS, and this is the one that usually kills,
  so the detail matters.** Long-term borrowings **$12,875M at maturity value, carrying $12,768M,
  with the earliest maturity $700M in March 2027 and $800M in July 2027**, and the ladder running
  to 2055. No commercial paper outstanding at either 2025-12-31 or 2026-06-30 against a $5bn
  programme. The obligations that could bite:
  - **$2.4bn of unfunded capital commitments to sponsored products, "callable on demand at any
    time"** — the only genuinely on-demand item, and it is a third of one year's owner earnings.
  - **$8,429M of contingent consideration — and it is payable in SHARES AND UNITS, not cash.**
    GIP 4.0-5.2M shares, HPS 2.8-4.4M Subco Units. **This is [E3-52]'s animal turned into an
    earn-out: a very large liability with no cash due date and no covenant.** It is a severe
    dilution item and a trivial solvency item, and the two must not be confused.
  - Dividends and Subco distributions **$3,347M in 2025**, with the 2026 dividend raised 10%
    ($5.73 a quarter × 4 × ~162.5M ≈ $3.7bn), plus a **$2.0bn announced 2026 buyback**.
    Both discretionary.
- **[E2-54]'s coverage test, run as written:** *"all interest, both payable and accrued,
  comfortably met out of current cash flow net of ample capital expenditures."* Ex-CIP operating
  cash $7,463M less capex $375M = **$7,088M against $614M of interest expense — 11.5x**; cash
  interest paid was $482M, so 14.7x on cash. **Zips no wallet.**
- **Leverage, named and quantified [E4-16, E3-29]** — *no ratio ceiling exists in this framework
  and the corpus supplies none for subject companies*: borrowings **$12,768M** against total
  BlackRock, Inc. stockholders' equity **$55,888M = 0.23x**, and against ex-CIP operating cash
  **1.7x**. Against **negative** net tangible equity the ratio is undefined, which is the honest
  statement of where the debt sits: **it is secured by a fee stream, not by assets.** Note the
  structural point recorded at Step 0: the notes are issued by New BlackRock and guaranteed by Old
  BlackRock, or the reverse, with combined Obligor Group financials published — so the debt sits
  at the top of the house and is not ring-fenced away from the fee stream.
- **[E2-60]'s third dimension of maintenance — RECORDED AS A CAUTION, not a failure.** Restricted
  earnings are those whose payout costs *"its financial strength"*. In 2025 dividends and Subco
  distributions $3,347M plus share and unit repurchases $1,951M = **$5,298M against owner earnings
  of $4,530M (D&A end) to $5,281M (capex end)**, with net new borrowing of $284M and $167M of
  option proceeds making up the rest. **The company distributed essentially all of its owner
  earnings, and slightly more than the conservative measure of them, and has announced a larger
  distribution for 2026.** That is not oblivion — the balance sheet absorbed it easily — but it
  means the acquisition programme is funded by paper because the cash is committed.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40, E4-51]**

**First, the honest framing. This company does not die; the owner's return does.** [E4-51]
requires the argument against my position stated better than its opponents would state it, so:
**a holder would say BlackRock is the most survivable business in this queue, and on Q4's own three
tests they are right.** It has no plant, no inventory, no leverage worth the name, no near-term
cash call, and a revenue line that fell 5.3% in the worst equity market in fifteen years.

**Mechanism 1 — THE PASS-THROUGH, shape #11, and it is the death of the return, not of the
company.** The scale gains of index management flow to the buyer, not to the owner **[E3-62]**:
*"how much is going to stay home and how much is just going to flow through to the customer."*
Quantified from the filings and already shown at Q2: **ETF average AUM +60.3% from 2021 to 2025
while the ETF fee rate fell 17.1%; total AUM +40.3% while base fees rose 25.7%; owner earnings per
share flat to −12.5% over the same four years.** Extend the trend and the arithmetic is simple:
at the observed rate of compression (−1.6% a year blended, −4.6% a year on ETFs), AUM must compound
at roughly 5% a year merely to hold base fees level. **Likelihood: already happening — this is not
a forecast, it is the filed record.**

**Mechanism 2 — the market, which is the same mechanism with a shorter fuse.** 57.9% of the
$15,344,624M of AUM at 2026-06-30 is equity. Modelled at the 2025 blended rate of 15.22bp:

| scenario | AUM after | change | base fees at 15.22bp | vs 2025 actual $19,179M |
|---|---|---|---|---|
| equity −30%, everything else −5% | $12,355,334M | −19.5% | $18,805M | −2.0% |
| equity −40%, everything else −10% | $11,143,691M | −27.4% | $16,961M | −11.6% |
| equity −50%, everything else −15% | $9,932,048M | −35.3% | $15,117M | −21.2% |

*(Limit stated: applying the blended rate understates the hit, because equity prices above the
blend and the mix would shift toward lower-fee fixed income and cash. Directionally the model is
conservative in the wrong direction and is shown anyway rather than tuned.)* **Even the worst row
leaves base fees above their 2021 level and interest covered many times over. Likelihood of the
middle row over a decade: a real possibility. Consequence: a poor decade for the owner, not an
impairment.**

**Mechanism 3 — the one place a real balance-sheet loss lives, and it is the securities-lending
indemnity. Consider some mathematics [E3-24].** From Note 16: *"The amount of securities on loan
as of December 31, 2025 and subject to this type of indemnification was approximately **$353
billion**"*, against *"cash and securities totaling approximately **$375 billion**"* held as
collateral — **106.2%**, and the filing states minimum collateral *"generally ranging from
approximately 102% to 112%"*. The filer's conclusion: *"The fair value of these indemnifications
was not material at December 31, 2025."*

| if borrowers holding … | default with a collateral shortfall of … | loss | = % of $55,888M equity | = % of 2025 net income |
|---|---|---|---|---|
| 5% of the loaned book ($17.7bn) | 15% | **$2,648M** | 4.7% | 48% |
| 20% of the loaned book ($70.6bn) | 15% | **$10,590M** | 18.9% | 191% |
| 20% of the loaned book ($70.6bn) | 30% | **$21,180M** | 37.9% | 381% |

**[E4-40] is the governing instruction here: model exposure, not experience.** *"all of us in the
industry made a fundamental underwriting mistake by focusing on experience, rather than exposure."*
The experience is spotless and the framework says a benign loss history is *"not only useless, but
actually dangerous"* as a guide. A 2-12% collateral buffer against a portfolio of equities lent to
banks and broker-dealers is a buffer against ordinary volatility, not against a simultaneous
counterparty failure and a gap-down. **Likelihood: [x] a low-level possibility** — the collateral
is marked daily, borrowers are *"primarily … highly rated banks and broker-dealers"*, and the
middle row would require a systemic event. **But it is the only mechanism in this file that can
take a fifth of the equity, and it is the one an investor in a "capital-light" asset manager would
not think to look for.**

**Mechanism 4 — dilution, which is a certainty rather than a risk.** $8,429M of contingent
consideration payable in **4.0-5.2M shares plus 2.8-4.4M Subco Units**: up to **9.6M more units on
162.5M, +5.9%**, and the earn-out was revalued **upward by $720M in 2025**, meaning it is tracking
toward the top of the range. **Likelihood: likely.** It costs the owner ~6% of everything and
appears nowhere in the adjusted earnings.

- **VERDICT: [x] IN — RECORDED, NOT GOVERNING** (the file closed at Q2).
  All three staying-power strengths pass, interest is covered 11.5x out of cash flow net of capex,
  the earliest maturity is March 2027, and the largest liability on the balance sheet is payable in
  paper. Owner earnings are **$4,756M to $5,583M** across two windows and both ends of (c), a
  17.4% band that decides the same way at every end, with **SBC resolved, complete, and taken at
  the grant-value measure [E3-70]**. The business survives every mechanism this run can name.
  **The finding that matters is not about survival: owner earnings PER SHARE are flat to 12.5%
  lower than four years ago on 40.3% more assets.** The survival shape is **#11 THE PASS-THROUGH**,
  with a proposed feature recorded at the register below.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND? — **COMPUTATION — NOT A CLEARANCE**

> ⛔ **OPERATOR RULE 3.** Q2 is **OUT on the business**. Q1-Q4 do **not** all show IN, so Q5 is not
> open. Everything below is arithmetic produced to discharge the operator's instruction of
> 2026-09-01 that every name carries a price. **It is not a clearance, it is not a valuation
> opinion for entry, and no entry language appears in it.** Arithmetic:
> `Test Runs/_research 2026-09-19 BLK/q5.py`, output in `q5.txt`.

**THE PRICE, AND THE SHARE COUNT.**
- **Price: US$1,069.78, the close of 2026-09-18.** Source: `tools/sources.py price("BLK")`, which
  reads an aggregator chart endpoint. **FLAGGED as an aggregator, used for the live quote only**,
  as operator rule 5 permits. Cross-check that the order of magnitude is right from a primary
  document: the FY2025 10-K states *"the intrinsic value of outstanding performance-based RSUs was
  $726 million reflecting **a closing stock price of $1,070**"* at 2025-12-31.
- **Share count: 162,476,186 — 154,869,259 shares of common stock plus 7,606,927 Class B-2 common
  units of BlackRock Saturn Subco, LLC, exchangeable one-for-one into common stock.** Taken
  verbatim from the cover of the latest periodic filing, **as of 2026-07-31, 10-Q accession
  `0001193125-26-337177`**: *"As of July 31, 2026, there were 154,869,259 shares of the
  registrant's common stock outstanding (162,476,186 on a fully diluted basis, including 7,606,927
  Class B-2 common units of a consolidated subsidiary, BlackRock Saturn Subco, LLC, which are
  exchangeable on a one-for-one basis into common stock of the registrant)."*
  **The Subco Units are included because they are economically common stock** — they carry the HPS
  sellers' claim on the same earnings, the filer itself adds them to diluted shares and to its own
  "shares outstanding including Subco Units" line, and the contingent consideration will issue
  more of them. Excluding them would understate the price of the business by 4.7%.
- **Market capitalisation: US$173,814M** (on common stock alone, $165,676M — shown so the reader
  can see the size of the choice).
- **Split-invariance: `tools/sources.py split_factor_after("BLK","2026-06-30")` returns 1.0.** No
  split intervenes between the measurement date and the anchor.

**THE FLOOR, BEFORE ANY RANKING [E4-28, E3-13].** *"that's the figure we quit on … we don't want to
buy equities where our real expectancy is below 10 percent. Now, that's true whether short rates
are 6 percent or whether short rates are 1 percent."*

- Owner earnings, after tax, from Q4: **$4,756M to $5,583M**.
- Grossed to a pre-tax expectancy at the 2025 **book** rate of 22.0%: **$6,097M to $7,158M**; at the
  2025 **cash** rate of 30.2%: $6,814M to $7,999M. The conservative (book-rate) figures are used.
- **Honest pre-tax expectancy at this price: 3.51% to 4.12%, plus growth of roughly zero** —
  because owner earnings **per share** compounded at **+0.13% a year (c = capex) to −3.28% a year
  (c = D&A)** over 2021-2025, on the filed series in Q4.
- **THE FLOOR IS ~10%. THE SHORTFALL IS 5.9 TO 6.5 POINTS.** To reach the floor from this price the
  business would have to compound owner earnings per share at **5.88% to 6.49% a year, in
  perpetuity**, against a four-year record of zero. **[E4-35]** sets the burden of proof that
  belongs on that belief and it is heavy; **[E4-44]** sets the second bound — *"the value of an
  asset, whatever its character, cannot over the long term grow faster than its earnings do"*.
- **BELOW THE FLOOR. The name is not ranked; it is quit on [E4-28]. The ranking lines below are
  therefore not filled in.**

**1. THE YIELD**
- owner earnings **$4,756M to $5,583M** ÷ market cap **$173,814M** = **2.74% to 3.21%** ·
  sovereign **5.34%** (US Treasury 30-year par yield, 2026-09-18, issuing authority).
- On common stock alone: 2.87% to 3.37%. **Either way, the owner's earnings yield is roughly
  half the government bond.**

**2. WHAT THE PRICE ALREADY ASSUMES**
- Perpetual growth implied at the bare sovereign, no risk premium added **[E3-42]**:
  g = 5.34% − 2.74% = **2.60%** at the conservative end; 5.34% − 3.21% = **2.13%** at the
  optimistic end.
- **What the business has actually done: 0.0% to −3.3% a year in owner earnings per share over four
  years, on 40.3% more assets under management.** The quote requires perpetual real-ish growth from
  a business whose per-unit price has fallen every year in every organically owned product.

**3. WHAT YOU ARE PAID**
- **−2.60 to −2.13 points versus the sovereign.** The buyer accepts about two and a half points
  *less* than the 30-year Treasury, in exchange for the growth above.

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].**
- Sovereign used **5.34%** — **the bare rate, no per-name premium added.** *"It may look
  mathematical. But it's mathematical gibberish."*
- Certainty was handled twice and neither place is the rate: at the understanding gate (**Q1 IN** —
  this business is understandable) and in the end discount, which is never reached because the
  floor already fails.
- **Windage count: ONE, and it was applied at Q4** — stock pay taken at the larger of the reported
  charge and the [E3-70] grant-date market value. No second application here. **[E4-11, E4-48]**.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — *"Using precise numbers is, in fact, foolish."*
- **Conservative — owner earnings capitalised at the bare sovereign with no growth:
  roughly $550 to $650 a share** ($89,064M to $104,551M).
- **Optimistic — the same range with 2% perpetual growth allowed (r − g = 3.34%):
  roughly $875 to $1,030 a share** ($142,395M to $167,156M).
- **Current price: $1,069.78 a share, $173,814M.**
- **The price sits ABOVE the whole range, including the optimistic end that already grants
  perpetual 2% growth to a business whose per-share owner earnings have not grown in four years.**

**WHAT THE BUYER IS PAYING FOR, IN WORDS** — required by the brief, and it is the most useful
paragraph here.
At $1,069.78 the buyer pays **$173.8 billion** for **$4.8 to $5.6 billion** of owner earnings:
**31 to 37 times**. Put in the units of the business itself, the buyer pays **1.13% of the $15.3
trillion of assets under management** for the right to earn **0.152% a year** on them — **nine
years of gross base fees, before a single cost, just to return the purchase price.** The multiple
of GAAP net income is 31.3x; of "as adjusted" net income, 22.5x; of book value per share, 2.88x.
**So what is actually being bought, in plain words:** a toll of fifteen hundredths of one per cent
on the world's savings, which has been cut in every product every year for five years, plus an
option on two things — that the $28.3 billion of purchased private-markets managers reach the
stated *"ambition to raise $400 billion in private markets by 2030"* at ninety basis points instead
of fifteen, and that Aladdin keeps compounding at ten per cent organically from 8.2% of revenue.
**Those two options are the entire difference between $650 and $1,070 a share.** The buyer is not
paying for the fee stream; the fee stream at the bare sovereign is worth about six hundred dollars
a share. The buyer is paying roughly **$450 a share, some $73 billion, for the private-markets and
technology options**, against $8.4 billion of contingent consideration still to be issued in paper
to the people who sold them.

**WHICH BAR** *(never both on the same number)*
- [ ] **Normal method [E4-11]** — not used. It is not reached: the floor fails before a margin is
      applied, and applying a margin to a price already above the optimistic end would be theatre.
- [x] **Screamer test [E4-01]** — does the price already clear the **conservative** case? **No. The
      price is above the whole range.** Three outcomes, and this is the third: *price above the
      whole range → no.* **[E3-25]**: *"it ought to just kind of scream at you."* It does not.

- **VERDICT: would be a FAIL ON PRICE, and BELOW THE FLOOR, had the gates been reached. NOT
  RANKED — quit on [E4-28]. No ranking position is assigned. This is a COMPUTATION, NOT A
  CLEARANCE.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Nothing is held and nothing is being bought, so there is no sell rule to pre-commit. What [E1-02]
requires instead is that the yardsticks be written down BEFORE the fact, so the reopening of this
file is decided by evidence and not by a later mood:** *"I believe in establishing yardsticks prior
to the act."* **Nothing is armed. No band goes into `tools/alerts.json` and no `PORTFOLIO.md` row is
added, because the file closed at Q2 on the BUSINESS** — a price alert on a business rejected for
what it is would be a category error (the QLYS ruling, 2026-09-07).

**THE REFUTATION RECORD — what would prove this Q2 verdict wrong, stated so a future reader can
test it against a filing rather than against my judgment.**

| # | the claim this run made | the filed fact that would refute it | where it would appear |
|---|---|---|---|
| 1 | The ETF price is competed away and cannot be raised | **iShares Core S&P 500 (IVV) raises its total annual fund operating expense ratio above 0.03% and does not lose share**, or Vanguard raises VOO above 0.03% first | iShares Trust 485BPOS; Vanguard Index Funds 485BPOS |
| 2 | The blended fee rate holds only because product was bought | **The total effective fee rate rises for three consecutive years EX the private-markets leg** (base fees less private-markets fees ÷ average AUM less private-markets average AUM), from the 13.64bp of 2025 | 10-K MD&A, the base-fee and average-AUM-by-product tables |
| 3 | Base fees grow slower than the assets they are charged on | **Base-fee growth exceeds average-AUM growth for two consecutive years** | same tables |
| 4 | Owner earnings per share are going nowhere | **Owner earnings per share above $37.16 (the 2024 capex-end peak) for two consecutive years**, computed on ex-CIP operating cash less stock pay at the larger of charge and grant value | 10-K cash-flow statement, the CIP reconciliation, the stock-compensation note, the cover share count |
| 5 | The private-markets build is an option, not a franchise | **Private-markets fee-paying AUM reaches the stated $400bn by 2030 at a fee rate at or above 89.85bp, with no further acquisition consideration issued** | 10-K AUM roll-forward and revenue-by-product tables |
| 6 | Aladdin is too small to reclassify the whole | **Technology services and subscription revenue exceeds 20% of total revenue with organic ACV growth above 15%**, i.e. it becomes the business rather than a twelfth of it | 10-K revenue table and the ACV disclosure |

**THE MONITORING METRIC, if this name is ever looked at again: the effective fee rate by segment,
ex acquisitions.** **[E4-32]** — direction outranks existence — and **[E4-37]** — *"you can almost
measure the strength of a business over time by the agony they go through in determining whether a
price increase can be sustained."* The day a BlackRock filing describes an attempt to raise a price
is the day this file should be reopened. There is no such passage in five years of filings.

**[E4-17] and [E3-30] on how a view like this one should change:** *"beliefs change quite
gradually"*, and the monitoring question is *"whether this erosion is just part of an aberrational
cycle … or whether the business has slipped in a way that permanently reduces intrinsic business
values."* The finding here is not an erosion of BlackRock's *position* — its position is
strengthening, and iShares crossed $6 trillion. **It is that the position does not carry a price.**
That is a slower and more permanent thing than a cycle, and the refutation table above is
deliberately built out of three-consecutive-year and two-consecutive-year tests so that one good
quarter cannot reopen it and three good years must.

**The sell rule [E2-28] — recorded for completeness, not applied:** two triggers (the market
judging the business more valuable than the facts indicate; funds needed for something more
undervalued or better understood) and three hold conditions (return on equity capital
satisfactory, management competent and honest, market not overvaluing). **Not applicable: no
position exists.** Price appreciation and holding period remain explicitly rejected as reasons to
sell.

**Position size — a judgment, stated [E3-45]: ZERO, and not because of the price.** The business
failed Q2. **[E5-35]**: *"You can turn any investment into a bad deal by paying too much. What you
can't do is turn any investment into a good deal by paying little."* A lower price would make this
a cheaper non-franchise, which is a different thing from an opportunity. **Sized down further, if
that were possible, by the live capital-allocation flag at Q3.**

- **VERDICT: [x] IN** — the refutation record is written, dated, and tied to named filed series
  with thresholds pre-committed **[E1-02]**. Nothing is armed.

## SELF-AUDIT
*Operator rule 6: a run is incomplete until its self-audit is checked. Violations found later are
corrected in an addendum, never by editing history.*

- [x] **Questions answered in order; no verdict skipped.** Q1 IN → Q2 OUT → the file closed → Q3,
      Q4 and Q6 written as **RECORDED, NOT GOVERNING** and Q5 headed **COMPUTATION — NOT A
      CLEARANCE** under operator rule 3.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1, Q3, Q4 and Q6
      are each IN on filed evidence. The moat class was NOT left PROVISIONAL, and the reason is
      argued in the Q2 verdict rather than asserted.
- [x] **Every UNRESEARCHED verdict names the artifact and where it lives.** There are no
      UNRESEARCHED gate verdicts. Two *peer* items are marked UNRESEARCHED inside Q2 with their
      artifacts named: the Fidelity Concord Street Trust 485BPOS fee table for the Fidelity ZERO
      funds (CIK 0000819118; four 2026 accessions listed, none of which carried the prospectus fee
      tables), and Amundi's English-language Universal Registration Document. Both are shown to be
      one-directional: neither can reverse the finding.
- [x] **Every UNKNOWABLE verdict states what specifically cannot be known.** There are none.
- [x] **Step 0: the filing was read, with accession number; a figure was cross-checked.** 10-K
      FY2025 `0001193125-26-071966`; total revenue of $24,216M reconciled two independent ways, and
      operating cash flow of $3,927M tied to the GAAP column of the CIP reconciliation. Four more
      filings read in full, each with its accession.
- [x] **Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.**
      Five-year (the corpus default) and three-year windows; the (c) band $369.6M-$593.0M with the
      reason the corpus default runs backwards here argued from the composition of the D&A line;
      and a third end quantified and explicitly not adopted.
- [x] **Competitor row filled**, one specification, eight lines, six filing-sourced competitors,
      accessions on every line, definitions quoted verbatim, and two comparability flags carried
      rather than smoothed (STT publishes no average AUM and no rate; IVZ changed its own yield
      definition in FY2025; BEN runs a September year; BX and BAM are carried from the committed
      BAM row of 2026-09-13 and **flagged as not recomputed in this run**).
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.** USD 5.34%,
      US Treasury daily par yield curve, 2026-09-18, struck fresh for this run; not FRED and not
      inherited from the brief. The earnings currency is USD (the Americas are 68% of AUM and 67%
      of base fees).
- [x] **Value stated as a round-number range, not a point estimate.** Roughly $550-$650 conservative
      and $875-$1,030 optimistic, against a price of $1,069.78.
- [x] **One bar chosen, not both; windage count stated.** The screamer test **[E4-01]** only; the
      normal method is explicitly not used. **Windage count: ONE**, applied at Q4 (stock pay at the
      larger of charge and grant value).
- [x] **Prices dated; aggregator used for live quotes only and flagged.** $1,069.78 at the
      2026-09-18 close, from `tools/sources.py price()`, flagged as an aggregator, with the 10-K's
      own *"a closing stock price of $1,070"* at 2025-12-31 as an order-of-magnitude cross-check.
- [x] **Every judgment cited by ledger id, and every id checked against `principle_ledger.csv`
      before use.** **108 distinct ledger ids** are cited in this file and all 108 were verified
      present in the 267-row `principle_ledger.csv` by script; **zero phantom citations**.
- [x] **`python tools/check_framework.py` PASSES** — recorded in the fold commit.
- [x] **Run committed to git**, in six pathspec commits: the skeleton before any fetch, then
      Step 0 + Q1, Q2, Q3, Q4, and Q5 + Q6 + audit.
- [x] **Write-early protocol followed.** The run file was created from the template as the first
      action, before any fetch, and every question was written and committed as it closed.
      Research written to `Test Runs/_research 2026-09-19 BLK/` as it was gathered.

**ONE THING THIS RUN GOT WRONG AND CORRECTED ITSELF, recorded rather than hidden.** The first
attempt at the competitor row was delegated to a helper agent, which exhausted the session limit
before it finished. Its partial output was on disk (`peers/PEER_ROW.md`) and was **verified figure
by figure against the downloaded filings by this session** before use — TROW's *"EFR without
performance-based fees 39.4 41.0 41.9"*, BEN's *"was 40.5 and 41.1 basis points for fiscal years
2025 and 2024"*, IVZ's *"revenue yield (2) 33.7 37.4 40.4"* and *"Net revenue yield ex performance
fees (3) 23.0 25.4 28.4"*, and STT's *"Management fees (1) $ 2,398 $ 2,124 $ 1,876"* were each
re-read in the filing text. The six ETF prospectus accessions were recovered by matching the
on-disk file sizes against EDGAR's own filing indexes and are recorded in Q2. **Nothing in the row
rests on a figure this session did not see in a filing.**

## REGISTER
- Verdict: [ ] IN  **[x] OUT (about the business)**  [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- **One line: BLK fails Q2 — the product that is 42% of long-term AUM and 45% of long-term base
  fees is sold by Vanguard at an identical 0.03%, unchanged for five years; every organically owned
  fee rate fell over 2021-2025 (ETFs −17.1%, active equity −20.8%, active fixed income −18.0%,
  active multi-asset −35.4%, non-ETF index −8.1%) and the blended 15.22bp held only because $28.3bn
  — $22.0bn of it in the company's own shares and units — bought a higher-priced private-markets
  book; base fees grew 14.6 points slower than the assets they are charged on, and owner earnings
  per share are flat to 12.5% lower than four years ago on 40.3% more AUM.**
- **Price US$1,069.78 (close 2026-09-18, aggregator, flagged) · share count 162,476,186 (154,869,259
  common + 7,606,927 Subco Units) from the 10-Q cover as of 2026-07-31, accession
  `0001193125-26-337177` · market cap US$173,814M · sovereign 5.34% (US Treasury, 2026-09-18) ·
  FAIL at Q2, OUT on the business. Q5 below the floor at 3.5-4.1% pre-tax expectancy against ~10%,
  and above the whole value range — headed COMPUTATION, NOT A CLEARANCE.**
- **If UNRESEARCHED — THE WORK ORDER:** not applicable to any gate. The two peer work orders are
  recorded in Q2 with artifacts named.
- **If UNKNOWABLE:** not applicable.

### THE SURVIVAL SHAPE **[E5-11]**
**#11 THE PASS-THROUGH is the mechanism** — *"the company survives but gains are passed to
customers and suppliers, compressing the owner's return."* The filed evidence: ETF average AUM
+60.3% from 2021 to 2025 while the ETF fee rate fell 17.1%; total AUM +40.3% while base fees rose
25.7%; owner earnings per share flat to −12.5%. **[E3-62]**'s second step answers the question the
shape asks: the savings from scale went home to the customer, not to the owner.

**PROPOSED, PENDING THE OPERATOR — a new shape, argued rather than asserted: THE BOUGHT AVERAGE.**
*The mechanism, in one line: the price of everything the business already owns falls every year, and
the owner buys higher-priced businesses with its own shares so that the blended price stands still —
so the decline is invisible in the headline while the share count and the goodwill rise, and the
owner pays for the appearance of stability in dilution.*
**Why it is not #11 alone:** the pass-through describes where the gains go; this describes **how the
loss is concealed**. BlackRock's blended rate reads 16.29 → 15.22bp, a 6.6% decline that looks
survivable; the organic rate fell 13.4% and every component fell between 8% and 35%, and the
difference is $28.3bn of purchased mix. **Why it is not #21 THE ROLL-UP:** SoundHound's revenue
*line* was bought while the businesses it owned throughout shrank. BlackRock's revenue line grows
organically and strongly — $698bn of net inflows in 2025. **It is the price per unit, not the
revenue, that is bought.** **Why it is not #10 THE CAMOUFLAGE:** there is no weak leg burning the
strong leg's cash; every leg is profitable. What is camouflaged is a *rate*, by a *purchase*, paid
for in *equity*. **Tells a reader can check on any filer:** a blended unit price roughly flat while
every disclosed component falls; goodwill and intangibles crossing book equity (here $63,251M
against $55,888M, tangible equity **−$7,363M**); and the share count rising by acquisition
consideration faster than buybacks retire it (up to 25.0M shares and units, 15.4%, against $1.6bn a
year of repurchase). **Numbering is left to the folding session, which must count the current index
rather than trust this file.**

### THE STRONGEST SINGLE FACT AGAINST MY CONCLUSION **[E4-26, E4-51]**
**iShares crossed $6 trillion in AUM and roughly doubled in three years while charging the same
0.03% as Vanguard on the flagship — which means buyers are choosing BlackRock for something that is
not price, and that something is not in my fee-rate series.** If the reason is secondary-market
liquidity, the options complex built on the ETFs, the securities-lending revenue returned to the
funds, or the ability to move ten billion dollars in an afternoon, then BlackRock owns a real and
unbuyable advantage that simply does not show up as price — and the framework's own **[E3-33]**
warns that *"a screen on realised returns alone misses this class entirely."* My answer is that an
advantage which shows up as volume at a price you cannot raise is scale, not franchise, and
**[E3-62]** says where the gains from scale go in that case. **But I record that a holder who
believes iShares' liquidity is a durable toll that will eventually be priced would read the same
filings and reach IN at Q2, and the fact they would cite is the $6 trillion, not a projection.**

### DEFECTS FOUND IN THE BRIEF AND THE TOOLING
1. **`tools/sources.py:_get()` defaults to `WEB_UA` = `Mozilla/5.0`, and `www.sec.gov/Archives`
   returns HTTP 403 to it.** Every primary-document fetch in this run failed until `headers=SEC_UA`
   was passed explicitly. The default is wrong for the rung of the evidence ladder the framework
   uses most. **Suggested fix: default `_get` to `SEC_UA` for any `sec.gov` host**, which changes no
   number and removes a trap that costs every new run a failed call.
2. **`cik_for("BLK")` returns the right CIK and a misleading history, and nothing warns.** CIK
   0002012383 files today; its `companyfacts` begins at **FY2024** because the holding company was
   only created in October 2024. The 2009-2023 history sits under CIK 0001364742, now named
   BlackRock Finance, Inc. **A single-CIK XBRL pull on BLK returns two years of data and no error**,
   which is the same defect class the resume-state note records for `level_shift` and
   `working_capital_flag`: a diagnostic that does not reach the reader. **Suggested fix: have
   `name_change_note()` fire on a `formerNames` entry that differs in corporate form (it returned an
   empty string here), or have `annual()` refuse when fewer than five annual periods resolve.**
3. **The brief's instruction to find the CIK myself was correct and load-bearing.** Any run that had
   taken a CIK from a brief would have silently built a two-year series for a company with seventeen
   years of filings.
4. **The brief's "Aladdin is the part that may behave unlike the rest" was a hypothesis and it is
   half right, which is the useful answer.** Aladdin does behave differently in contract form
   (long-term, recurring, 16% organic ACV growth) and **does not** behave differently in its fee
   base: *"Fees earned for technology services are primarily recorded as services are performed over
   time and are **generally determined using the value of positions on the Aladdin platform**, or on
   a fixed-rate basis."* Its revenue is partly market-linked, like everything else. And it is
   **8.2% of total revenue**, which is too small to reclassify the other 91.8%.
5. **No defect found in the brief's framing of the fee-rate test.** It named the decisive series
   correctly before the data was pulled, and the data confirmed it. The instruction *not* to inherit
   BAM's conclusions mattered: BlackRock's rate decline has a different cause (customer substitution
   at a commodity price) from BAM's (related-party mix), and the two runs reach the same verdict for
   different reasons.
6. **One instruction in the original brief caused the session loss and is worth recording as a
   process defect, not a content one:** delegating the competitor row to a helper agent. The
   coordinator's correction — fetch peer data in-session — is the right rule for a run of this size,
   and the write-early protocol is what saved the partial peer file.

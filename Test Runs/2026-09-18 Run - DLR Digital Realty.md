# Company Run — Digital Realty Trust, Inc. (DLR) — 2026-09-18
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs. **This is a NEW NAME, not a
holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.**

Filled top to bottom. **Stop at the first verdict that is not IN.** Run unattended from scratch
(no prior run file for DLR exists). WAVE 5, the last of the eight "capex unresolved [E5-20]" names.
Research, scripts and downloaded filings are in `Test Runs/_research 2026-09-18 DLR/`; DLR filings
fetched earlier today for the EQIX competitor row are cited in place at
`Test Runs/_research 2026-09-18 EQIX/peers/` (not re-fetched).

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Asked aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0: THE ROUTING NOTE, THE RATE, THE PRICE, THE PERIMETER, AND THE FILING

### The REIT routing note, checked on disk rather than followed
The wave 5 table says *"EQIX and DLR are REITs: the prepped reading list routes REITs to a sector
method first; a run states that and the verdict follows."* **`Framework/` was listed by this run on
2026-09-18** and holds: the two audit/synopsis files of 2026-08-26, the two archives, `CHANGELOG.md`,
`INVENTIONS - deleted and why.md`, `PLAIN ENGLISH - what this is and how it works.md`, `README.md`,
**one** sector method (`SECTOR METHOD - owner earnings for insurers and float-bearing holding
companies.md`), `THE FRAMEWORK v4.md`, `THE HOLDINGS FRAMEWORK.md` and the `v4/` folder. **There is no
REIT sector method.** The EQIX run found the same this morning and nothing has been added since. v4
says *"If a rule is not here, it is not in force"*, so **v4 is applied as written** and no REIT method
is invented (PRIME RULE 3). Digital Realty's own measures (FFO, Core FFO, AFFO, Adjusted EBITDA,
"recurring capital expenditures") are READ below as the company's claims, never adopted as the
run's definitions. The insurer method is not owed: Digital Realty is funded by notes, bank lines,
share issuance, joint-venture partners and asset sales, not by float.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.29%** · **09/17/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority.**
  Struck by this run: the cached curve was deleted and `tools/sources.sovereign("USD")` re-fetched
  it at about 18:10 UTC on 2026-09-18, returning `(5.29, '09/17/2026', 'US Treasury daily par yield
  curve')` (`step0_out.txt`). 09/17 is the newest row published (the 09/18 curve appears after the
  close). FRED was not used.
- **The earnings currency is not only USD, recorded rather than smoothed.** Annualized rent by metro
  at 2025-12-31 (10-K MD&A, portfolio including unconsolidated entities at 100%): Northern Virginia
  21.4%, Chicago 7.1%, **Frankfurt 6.1%, London 4.5%, Singapore 4.5%**, Dallas 4.3%, **Paris 4.1%,
  Amsterdam 4.1%**, New York 4.0%, **Sao Paulo 3.8%, Johannesburg 3.5%**, Silicon Valley 3.5%,
  Portland 3.0%, **Tokyo 2.3%, Zurich 1.7%**, other 22.1%. The 10-K names the exposures: *"Our primary
  currency exposures are to the Euro, Japanese yen, British pound sterling, Singapore dollar, South
  African rand and Brazilian real."* Europe held 107 of 221 consolidated buildings at 2025-12-31.
  Precedent in this queue (CL, SPGI, EQIX) prices a USD reporter against the USD sovereign and names
  the currency at Q4; this run does the same. **The USD 30-year is the highest of the three
  sovereigns on file (EUR 3.83%, JPY 4.00%, last struck 2026-09-10/13), so it is the harder bar.**

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$184.26, the close of 2026-09-17**, the last COMPLETED close. Source: Yahoo Finance daily chart
  series via `sources._chart("DLR", rng="1mo")` (aggregator, permitted for live quotes only,
  **flagged**; `price_out.txt`). Bar: open 183.22, high 185.02, low 182.76, close 184.26.
- **`tools/sources.price()` was NOT used for the struck price.** At about 18:10 UTC on 2026-09-18,
  market open, it returned `(183.84, '2026-09-18', 'USD')`; the chart meta shows
  `regularMarketPrice 183.855` at `regularMarketTime 2026-09-18 18:10:47` UTC. An intraday price
  stamped with today's date while the docstring says "Latest close". **The TOST and EQIX defect
  reproduces on a third name.**
- Recent closes: 09-10 $185.37 · 09-11 $188.58 · 09-14 $179.14 · 09-15 $179.27 · 09-16 $181.07 ·
  09-17 $184.26. Last dividend in the series **$1.22** (ex-date 2026-09-15).
- **Primary-filing cross-checks of the aggregator (two, both corroborate):**
  1. Form 4, accession **`0001500081-26-000009`**, filed 2026-08-31: director Mark R. Patterson sold
     200 shares on **2026-08-27 at $193.96**. The Yahoo bar for 08-27 is low $191.48, high $196.83.
     **Inside the range.**
  2. 8-K of 2026-07-01, accession **`0001193125-26-292577`**: *"On July 1, 2026, Blackstone completed
     an underwritten public offering of 12,310,249 shares of common stock ... at a price per share to
     the public of $185.00."* A negotiated block price, not a trade print, but in the same range as the
     September closes.

### The share count: from the cover, with the accession
- **370,036,176 shares**, from the cover of the Q2 2026 Form 10-Q (period ended 2026-06-30, filed
  **2026-07-31**, accession **`0001104659-26-089296`**): *"Digital Realty Trust, Inc.: Class
  Outstanding at July 29, 2026 Common Stock, $.01 par value per share 370,036,176"*.
  `Screens/cover_shares.py DLR` returns the same figure from the same accession, *"(single class /
  undimensioned)"*.
- **ERIC trap checked**: the 2026-06-30 balance sheet reads *"370,010 and 343,557 issued and
  outstanding as of June 30, 2026 and December 31, 2025"* (thousands). Issued equals outstanding; there
  is no treasury stock. **SPGI trap checked**: no exclusion clause on the cover.
- **The non-voting class is inside the count.** 12,310,249 shares of non-voting common stock were
  issued to Blackstone on 2026-06-30 and converted to common on transfer on 2026-07-01 (8-K
  `0001193125-26-292577`), four weeks before the cover date.
- **The count grew 7.7% in seven months.** 343,557 thousand (2025-12-31) to 370,010 thousand
  (2026-06-30): about **13.5 million ATM shares** at an average $184.94 (net $2.5bn), **12.3 million**
  to Blackstone, the rest awards and unit exchanges (10-Q Note 10). A new **$7.5bn** ATM programme was
  opened on 2026-05-04 (8-K `0001193125-26-202581`), **$6.3bn** unused at 2026-06-30.

### The perimeter between the business and the common holder: stated, not blended
The owner-earnings figures below are built from the consolidated cash-flow statement, which is the
Operating Partnership's. Four claims sit between that cash and the common holder:
1. **Operating-Partnership common units held by third parties**: *"Limited Partners, 6,665 and 6,189
   units issued and outstanding as of June 30, 2026 and December 31, 2025"* (thousands; 1.8% of the
   OP), redeemable for cash or, at the Parent's option, one share each. **Treatment: they share the
   OP's cash one-for-one with a share, so the owner-earnings denominator is common shares PLUS these
   units (376.70 million).** The struck cap uses the cover count; the perimeter-consistent cap adds
   the units at the same price. Both are shown at Q5.
2. **Preferred stock**: series J, K and L, *"$ 755,000 liquidation preference ( $ 25.00 per share),
   30,200 shares issued and outstanding"* (thousands), dividends **$40.7M a year** (FY2023-25 income
   statements). A senior claim: deducted from owner earnings, never added to the cap.
3. **Teraco minority (redeemable noncontrolling interest, $1,567M at 2026-06-30)** and
   **noncontrolling interests in consolidated joint ventures** ($421M at 2025-12-31; *"Depreciation
   related to non-controlling interests | (86,159)"* in FY2025). Their share of consolidated cash is
   not the common holder's; handled at Q4.
4. **Share overhang not in the cover count, shown separately [E2-26]**: **2,337,036 shares** issued to
   buy Columbia Capital (8-K `0001193125-26-357083` of 2026-08-19 registers their resale, *"shares of
   common stock that were issued as consideration"*), plus up to **1,457,506** more on earn-out
   milestones; **3,425,031 shares** due in H2 2026 to settle the Teraco put (10-Q Note 10); **517,475
   OP units** issued for the Astra Enterprise Park land (April 2026, inside the 6,665k above); any ATM
   sales after 2026-06-30 (unknown until the Q3 10-Q). Together about **7.2 million shares (+1.9%)**
   known and pending.

### The market cap
- $184.26 × 370,036,176 = **US$68,182.9M**. Split factor after 2026-07-29 = **1.0**
  (`sources.split_factor_after`); `close` used, never `adjclose`.
- Perimeter-consistent (common plus third-party OP units): $184.26 × 376,701,176 = **US$69,410.9M**.
- With the known pending shares (Columbia 2.34M, Teraco 3.43M): about **US$70.5bn** before the
  earn-out and any post-June ATM sales. Displayed, not blended.

### LIVE-DEAL CHECK: re-queried by this run, not inherited
- `sources.deal_filings("0001297996")` returned `([], [], '2026-02-13')`: no merger, tender or
  exchange form and no flagged 8-K.
- **Every 8-K since 2024-01-01 with Items 1.01, 2.01, 3.02, 3.03, 7.01 or 8.01 was listed and the
  2025-2026 ones were read** (`fetch8k.py`): note issues and credit agreements (2024-09-13, 2024-09-30,
  2024-11-12, 2025-01-14, 2025-06-25, 2025-11-21), ATM agreements (2024-12-23, 2026-02-17,
  2026-05-04), and the **2026 perimeter events**: the Astra land purchase and Columbia Capital and
  Teraco-put agreements (8-K `0001193125-26-276844`, 2026-06-22), the **Blackstone joint-venture
  buy-in** (8-K `0001193125-26-288761`, 2026-06-29, completed 2026-06-30 per `0001193125-26-292577`),
  and the Columbia Capital resale registration (2026-08-19). **All of these are Digital Realty buying;
  none is an offer for Digital Realty's shares. The quote is an owner-earnings price, not a spread.**
  They are perimeter changes and are carried into Q4.

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2025 Form 10-K**, period ended 2025-12-31, filed **2026-02-13**, accession
  **`0001104659-26-015365`** (`dlr-20251231x10k.htm`; text at `../_research 2026-09-18 EQIX/peers/DLR_10K_FY2025.txt`).
- **Q2 2026 Form 10-Q**, filed **2026-07-31**, accession **`0001104659-26-089296`**; Q1 2026 10-Q
  (`0001104659-26-054255`).
- Also read: 10-Ks FY2014-FY2024 (FY2014 `0001297996-15-000010`, FY2015 `0001297996-16-000124`, FY2016
  `0001297996-17-000020`, FY2017 `0001297996-18-000026`, FY2018 `0001297996-19-000032`, FY2019
  `0001558370-20-001906`, FY2020 `0001558370-21-002191`, FY2021 `0001558370-22-002195`, FY2022
  `0001558370-23-002087`, FY2023 `0001558370-24-001575`, FY2024 `0001558370-25-001424`); 8-K EX-99.1
  releases and EX-99.2 supplements for Q4 2021-Q4 2025 and Q2 2026 (on disk in the EQIX peers
  folder); the **DEF 14A of 2026-04-17** (`0001308179-26-000296`); the Interxion closing 8-K of
  2020-03-13 (`0001193125-20-072868`) and the DuPont Fabros closing 8-K of 2017-09-14
  (`0001193125-17-285083`); the 8-Ks listed above.
- **Figures cross-checked against the filed statement** (FY2025 consolidated statement of cash flows):
  *"Net cash provided by operating activities | 2,412,136"*, *"Depreciation and amortization |
  1,894,636"* and *"Improvements to investments in real estate | ( 3,181,179 )"* all match companyfacts
  exactly (`NetCashProvidedByUsedInOperatingActivities`, `DepreciationAndAmortization`,
  `PaymentsToDevelopRealEstateAssets`, accession `0001104659-26-015365`). **The fourth line is the
  finding of Q4**: *"Amortization of share-based compensation | 93,766 | 75,606 | 80,532"* is on the
  face and **in no element companyfacts carries** (searched by value across every namespace in the
  file), and the capex line sits under `PaymentsToDevelopRealEstateAssets`, **which no `CAPX_TAGS`
  element reaches.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### The unit economics, in my own words, without management's language
Digital Realty buys land where the electricity grid can deliver a great deal of power, puts up
buildings, fits them with power and cooling plant, and rents the powered space. It rents it two
ways. **Small customers** take a few cabinets or a cage for two to five years at a high price per
unit of power, and pay a monthly fee for each cable to another customer in the building. **Very
large customers** (cloud and software companies) take whole halls or buildings for five to fifteen
years at a much lower price per unit of power. It passes most of the electricity bill through at
cost. Then it does a second thing a pure landlord does not: **it sells large stakes in finished or
half-finished buildings to pension funds and private-equity partners at more than it cost to build
them, keeps 20-50%, and charges the partners fees to run them.**

FY2025, from the 10-K income statement and the 8-K EX-99.1 supplement of 2026-02-05 (accession
`0001104659-26-010887`), $M:

| line | FY2025 | share |
|---|---:|---:|
| Rental revenues (space and power capacity) | 4,084.5 | 66.8% |
| Tenant reimbursements, utilities (electricity passed through) | 1,254.5 | 20.5% |
| Tenant reimbursements, other | 151.2 | 2.5% |
| Interconnection and other | 478.7 | 7.8% |
| Fee income (managing and developing for partners) | 137.2 | 2.2% |
| Other | 6.6 | 0.1% |
| **Total operating revenues** | **6,112.7** | |
| Utilities expense (against 1,254.5 recovered) | (1,426.5) | |
| Other property operating, maintenance, taxes, insurance | (1,300.3) | |
| General and administrative | (565.5) | |
| Transactions and integration | (185.1) | |
| Depreciation and amortization | (1,894.6) | |
| Impairment and other | (82.3) | |
| **Operating income** | **658.5** | **10.8%** |
| *below the line:* gain on disposition of properties | 995.6 | |

Read as a landlord and a developer:
1. **Two rents, very different prices.** Annualized rent at 2025-12-31 (supplement, "Lease Expirations
   - By Size", consolidated plus managed unconsolidated at DLR's share): **0-1 MW $1,462M (34.9%) at
   $329 per kW per month; >1 MW $2,506M (59.8%) at $132 per kW per month**; other (shell, storage,
   office) $226M (5.4%). The large-customer product is 60% of the rent and sells a unit of power at
   40% of the small-customer price. The 10-K describes the two: *"(0 to 1 MW) Small (one cabinet) to
   medium (75 cabinets) deployments ... Contract length generally 2-5 years"* and *"(> 1 MW) Scale
   from medium to very large deployments ... Contract length generally 5-10+ years."*
2. **The toll is small here.** Interconnection and other is **7.8%** of revenue on *"over 232,000
   cross connects"* (10-K Item 1), about $2,060 a year per connection if all of the line were
   cross-connects, which it is not (the line includes "other"). Equinix's is 18.0% (EQIX run).
3. **Concentration.** The top 20 customers are **50.9%** of annualized recurring revenue; the two
   largest, *"Fortune 50 Software Company"* **11.7%** and *"Oracle Corporation"* **9.0%**, are 20.7%.
   **Equinix is the sixth-largest customer (2.0%).**
4. **The plant.** Gross operating real estate at cost **$31,359M** plus construction in progress and
   space held for development **$4,977M** and land held **$91M** (Note 5); goodwill **$9,712M** and
   intangibles **$2,135M** from the DuPont Fabros (2017), Interxion (2020) and Teraco (2022)
   acquisitions; **$3,428M** in unconsolidated entities. Revenue is **19 cents per dollar of gross
   operating real estate** a year; operating income is **2.1%** of it.
5. **The developer-seller.** Gains on disposition of properties, FY2015-25: **$95M, $170M, $40M,
   $80M, $335M (incl. deconsolidation), $317M, $1,381M, $177M, $901M, $596M, $996M**; *"Proceeds from sale of assets"*
   **$7,967M over FY2021-25** (cash-flow statements). The
   10-K: *"As circumstances warrant, our Operating Partnership may dispose of stabilized assets or
   enter into joint venture arrangements with institutional investors or strategic partners"*, and
   the FY2025 fund contribution alone *"recognized a gain on disposition of approximately $873
   million"* on *"approximately $937 million of gross proceeds"*. **89 of the 310 data centres are
   held in unconsolidated entities.**

**How the money is financed, which Q1 must state because it shapes every later gate** (FY2025 cash-flow
statement): operating cash **$2,412M**; improvements to real estate **$3,181M**; acquisitions **$321M**;
investments in unconsolidated entities **$519M**; dividends and distributions **$1,728M**. The gap was
filled by **$1,620M of asset sales**, **$1,106M of new shares** and net new notes. In 2024 the share
issuance was **$3,651M**; in H1 2026 alone **$2.5bn** through the ATM plus **$2.35bn** of shares paid
to Blackstone. The Parent must distribute *"90% of its taxable income"* and says so plainly: *"our
Operating Partnership cannot rely on retained earnings to fund its ongoing operations to the same
extent that other companies whose parent companies are not REITs can."*

### The scarce input this business controls
**Land with grid power already committed, in the metros where demand is.** The 10-K: *"we estimate
that our land and other space held for, or actively under, construction could accommodate over 3,500
megawatts of additional data center capacity, including more than 1,000 additional megawatts
developable in Northern Virginia"*; the Astra Enterprise Park purchase of April 2026 came with *"an
agreement with the local utility for 600 megawatts of utility power to be provided by early 2028"*
(8-K `0001193125-26-288761`). **A second, narrower input, in the retail product only**: the
interconnected populations of certain gateway buildings, *"densely connected data communities that are
difficult for competitors to replicate"* (10-K Item 1), which is the Equinix-type asset at a smaller
scale. **A third is access to capital** at investment grade and through partners, which the business
consumes faster than it earns (above).

Named precisely because Q2 turns on it: **power-ready land is scarce this decade; it is not owned
exclusively.** The 10-K's own competition paragraph names *"Equinix, Inc. and NTT; various private
operators in the U.S.; as well as Global Switch Holdings Limited and various regional operators"*, and
the MD&A says *"the growing acceptance by private institutional investors of the data center asset
class has generally pushed capitalization rates lower, as such private investors may often have lower
return expectations than us."*

### Will the fundamentals look broadly the same in ten years?
**The mechanism, yes**: powered rooms rented by the kilowatt to companies that do not want to build
their own, electricity passed through, large customers on long leases. **The customer mix and the
plant, not necessarily.** Hyperscale and AI demand now sets the large-lease price, and the filings say
power density is changing what a building must be (Q2 and Q4 take this up). **The capital structure,
certainly not the same**: in ten years the share of the portfolio held through funds and joint
ventures, which rose from a handful of partnerships to 89 buildings, a listed Singapore REIT, a US
fund with *"more than $3 billion of equity commitments"* and a new fund-management acquisition
(Columbia Capital, 2026), may be larger again.

**The honest limits, stated rather than smoothed.** (1) The perimeter moves every year: assets are sold
into funds at gains, partners' stakes are bought back (Blackstone, June 2026, $3.5bn), minority puts
settle in shares (Teraco), and a promote paid on the company's own purchase was booked as revenue
(Q2 2026, $201M; Q3 reads it). The ACCOUNTING of what the common holder owns is harder than the
business. (2) **48.2% of FY2025 revenue was earned outside the US** and **61% of net investments in properties sit
there** (Note 20: $2,945.0M of $6,112.7M; $16,212.5M of $26,433.6M), in six named currencies.
(3) The development-and-sale layer means reported net income is mostly gains ($996M of $1,313M in
FY2025), so no net-income figure is used anywhere in this run.

- **VERDICT: [x] IN**
  *The unit economics are writable in plain words (rent by the kilowatt in two very different
  products, electricity passed through, buildings sold down to partners at a developer's margin, all
  financed by issuance, borrowing and sales); the scarce input is nameable (power-ready land in demand
  metros, plus gateway populations in the retail product); the mechanism will be recognisable in ten
  years **[E3-31]**. The complexity is in the perimeter and the financing, which Q3 and Q4 must read,
  not in how a kilowatt is rented. Whether any of it is a franchise is a relative claim, and it is Q2's.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

### WHAT IS BEING TESTED, AND THE PRIOR THIS RUN WAS TOLD TO DISTRUST
Q1 named two products and two scarce inputs: **power-ready land in demand metros**, which the large
(>1 MW) product sells, and **the connected populations of some gateway buildings**, which the small
(0-1 MW) product and the interconnection line sell. [E3-03]'s test is that the customer thinks there is
*"no close substitute"*, and its demonstration clause is *"a company's ability to regularly price its
product or service aggressively and thereby to earn high rates of return on capital"* (1991 letter).

**The prior to refute.** This morning's EQIX run built a competitor row, on a metric chosen to judge
Equinix, in which Digital Realty's (operating income + D&A) / average gross plant was **6.9-7.4%**. The
easy move is to import that row. **It is not imported.** Every DLR figure below is rebuilt from DLR's
own filings, the row is rebuilt for DLR's products (the wholesale and hyperscale peers, not only the
colocation ones), and the one place the EQIX row was unfair to DLR is corrected first: its denominator
included **$5.1bn of construction in progress and land held**, which earns nothing until delivered.
On operating real estate alone (the Schedule III gross, `RealEstateGrossAtCarryingValue`, equal to
Note 5's *"Investments in operating properties"* at cost), and with impairments added back, **DLR's
return on plant is 8.7-8.9% for FY2023-25, not 6.9-7.4%** (`q2calc.py`). The case for DLR is also
stronger than the EQIX row showed on pricing: the >1 MW product's cash renewal spread in H1 2026 was
**+48.7%**, and the backlog of signed-not-commenced leases rose from **$817M to $1.4bn** at DLR's share in six
months (part of the rise is the Blackstone stakes bought in June, whose three buildings are 100%
pre-leased). Both are recorded at full strength below.

### THE THREE CONDITIONS **[E3-03]**
**(1) Needed or desired: IN.** More than 5,000 customers; bookings of $175M (Q4 2025) and $208M
(Q2 2026) of annualized rent at DLR's share; *"a record total backlog of $1.9 billion of annualized GAAP
base rent at 100% share"* (release of 2026-07-23, `0001104659-26-086270`); portfolio occupancy by IT
load 89.8% at 2026-06-30.

**(3) Not subject to price regulation: IN.** No regime sets rent. Electricity is recovered from
customers (*"Tenant reimbursements - Utilities | ... 1,254,457"*, FY2025), a pass-through of an input,
not an administered price; [E2-59] is not engaged.

**(2) No close substitute: NOT SHOWN for the large product, which is 60% of the rent; a narrow
position for the small product.** The evidence, product by product:

1. **The large product's customer can build the thing itself, and the filing sells to that
   customer.** 10-K Item 1: *"For customers who possess the ability to build and operate their own
   infrastructure, our Powered Base Building® solution provides the physical location, requisite power
   and network access necessary to support a state-of-the-art data center."* The customers are the
   self-builders: *"Fortune 50 Software Company"* 11.7% and *"Oracle Corporation"* 9.0% of annualized
   recurring revenue; *"Our top three customers represented approximately 26%"*; *"20 of our 310 data
   centers are occupied by single customers, including data centers occupied solely by our top three
   customers"* (Item 1A). A customer that is a quarter of your revenue and can build its own building
   has a close substitute by definition.
2. **The large product is priced like credit, not like a franchise.** DLR's own purchase of
   Blackstone's joint-venture stakes (8-K `0001193125-26-288761`, 2026-06-29): three hyperscale
   buildings *"100% leased to three distinct investment-grade hyperscale customers ... supported by
   15-year leases with a blended average Aa3/AA- credit-rating and 3.6% annual rent escalators"*, bought
   at *"an estimated initial stabilized capitalization rate of over 6.5%"*. A 15-year lease to an AA-
   tenant at an initial 6.5% yield, against a US 30-year Treasury at 5.29%, is a long corporate bond
   with a building attached. The price of the product is set by the tenant's credit and the market's
   cap rate, and DLR says who sets the cap rate: *"the growing acceptance by private institutional
   investors of the data center asset class has generally pushed capitalization rates lower, as such
   private investors may often have lower return expectations than us"* (10-K MD&A).
3. **The price series, units and dollars [E4-55]: the large product's price follows the supply cycle
   in both directions.** Renewal rent change by product, DLR's own filings (GAAP from each 10-K's
   leasing table; cash from the 8-K supplements):

| year | small product GAAP | large product GAAP | small product cash | large product cash | all products cash | source |
|---|---:|---:|---:|---:|---:|---|
| 2014 | colocation 5.6% | Turn-Key Flex 6.3%, shell 26.5% | | | | FY2014 10-K |
| 2015 | 6.6% | 4.8%, shell 33.7% | | | | FY2015 10-K |
| 2016 | 4.1% | 10.2%, shell 22.9% | | | | FY2016 10-K |
| 2017 | 3.4% | 4.0%, shell 25.4% | | | | FY2017 10-K |
| 2018 | 0.3% | 7.2%, shell 25.2% | | | | FY2018 10-K |
| 2019 | 2.2% | 2.3%, shell 15.0% | | | | FY2019 10-K |
| 2020 | 0-1 MW 0.7% | >1 MW 3.4% | | | | FY2020 10-K (products redefined) |
| 2021 | 1.8% | **(6.6)%** | 1.0% | **(11.9)%** | **(3.1)%** | FY2021 10-K; Q4 2021 supplement |
| 2022 | 3.6% | 0.5% | 3.4% | **(3.3)%** | 1.8% | FY2022 10-K; Q4 2022 supplement |
| 2023 | 5.7% | 21.0% | 4.9% | 9.2% | 6.8% | FY2023 10-K; Q4 2023 supplement |
| 2024 | 5.0% | 27.4% | 4.2% | 14.4% | 9.0% | FY2024 10-K; Q4 2024 supplement |
| 2025 | 4.6% | 27.0% | 4.1% | 12.3% | 6.7% | FY2025 10-K; Q4 2025 supplement |
| H1 2026 | 5.3% | 65.6% | 4.7% | **48.7%** | 15.9% | Q2 2026 10-Q and supplement |
| LTM to Q2 2026 | | | 4.5% | 28.4% | 11.0% | Q2 2026 supplement (`Cash Rent % Change kW / NRSF`) |

   The large product's cash renewals **rolled down 11.9% in 2021 and 3.3% in 2022**, when supply was
   ample, and rolled up 9-49% from 2023, when it was tight. The FY2021 10-K's outlook was that 2022
   renewals would be *"generally ... consistent with the rates currently being paid"*; every 10-K since
   expects them *"to be positive"*. The same product in another filer's words in the soft year:
   CyrusOne, FY2021, *"Rates contracted with our customers that renewed in 2021 were lower than the
   rates previously in effect, a trend that we expect to continue and to be driven by increases in data
   center supply and cloud company offerings"* (`0001553023-22-000009`). **That is [E2-58]'s signature,
   long-term profitability set by *"the ratio of supply-tight to supply-ample years"*, observed in one
   filer's price series in five years.** The per-kW figures say the same: large-product renewals
   repriced from **$159 to $265 of cash rent per kilowatt** in Q2 2026 (supplement's unit), while
   in-place large rent averages **$132 per kW per month** (lease-expiration table) and new large leases
   were signed at **$181 per kW** (GAAP) in Q4 2025.
4. **The small product: steady, modest, positive, with high churn.** Cash renewals +1.0% to +4.9% a
   year through the cycle, including the soft years; but churn in that product runs **9.2%, 7.1%, 6.3%,
   7.8%, 8.5% (FY2021-25) and 8.3% LTM**, against 3.2-6.6% for the large product (supplements). It is
   the Equinix-type asset at a third of the scale: interconnection is **7.8%** of revenue against
   Equinix's 18.0%, and *"232,000 cross connects"* against Equinix's *"more than 500,000"*.

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4)*
**Built for DLR's products, not imported.** Taken: the large-product (wholesale and hyperscale)
filers **DuPont Fabros** (DLR bought it in 2017; last 10-K FY2016), **CyrusOne** (last FY2021), **QTS**
(last FY2020), **Switch** (last FY2021) and **American Tower's Data Centers segment**; the small-product
and interconnection filers **Equinix**, **CoreSite** (last FY2020) and **Cyxtera** (bankrupt 2023);
**Iron Mountain's** data-centre segment (no segment assets). **Nine examined; four still file** (DLR,
Equinix, AMT, Iron Mountain); the private builders now doing most of the large-product building
(Vantage, STACK, Aligned, QTS and CyrusOne under private owners) and the hyperscalers' own building
file no operating metrics (EQIX run's EDGAR full-text log, `../_research 2026-09-18 EQIX/peers/PEER_ROW.md`,
not repeated). Stale filers are marked; they are the only filed record of the large product outside DLR.

**ROW A: RETURN ON OPERATING REAL ESTATE, (operating income + D&A) / average Schedule III gross real
estate, same element (`RealEstateGrossAtCarryingValue`; Switch, a non-REIT filer, on gross property,
plant and equipment), each filer's last three filed years** (`rowcalc.py`, companyfacts 10-K facts,
earliest filed vintage; one figure per filer checked against the filed text: CyrusOne FY2021
*"Operating income | 39.3"* and *"Depreciation and amortization | 499.2"*, `0001553023-22-000009`):

| company | product | year 1 | year 2 | year 3 | years |
|---|---|---:|---:|---:|---|
| **Digital Realty** | both, 60% large | **8.3%** (8.7% ex-impairment) | **8.2%** (8.9%) | **8.7%** (8.9%) | FY2023-25 |
| Equinix | small + interconnection | 13.0% | 12.2% | 12.6% | FY2023-25 |
| CoreSite (stale) | small + interconnection | 14.5% | 12.9% | 11.9% | FY2018-20 |
| Switch (stale; gross PP&E) | large and small | 10.2% | 10.5% | 8.2% | FY2019-21 |
| CyrusOne (stale) | large | 8.5% | 7.5% | 7.3% | FY2019-21 |
| QTS (stale) | large | 6.5% | 7.6% | 7.3% | FY2018-20 |
| DuPont Fabros (stale) | large only | 8.9% | 4.6% (impairment year) | 9.7% | FY2014-16 |
| AMT Data Centers | small + large, US | | 6.9% | 7.7% | FY2024-25, segment profit (already pre-D&A) over Schedule III gross (EQIX row) |
| Cyxtera | small | | | 1.7% (8.1% before a goodwill impairment) | FY2022 |
| Iron Mountain data centres | not split by product | | | | not computable, no segment assets |

**What Row A shows.** The row splits by product, not by name. **The small-product-plus-interconnection
filers (Equinix, CoreSite) earn 12-15%; the large-product filers (CyrusOne, QTS, DuPont Fabros, AMT)
earn 7-10%; Digital Realty, 60% large, earns 8.2-8.9%, inside the large-product cluster.** Its
position is the product's, not its own. And **its own series has drifted down**, on the same
formula: **9.3% (FY2015), 10.6%, 9.1%, 9.7%, 9.8%, 9.6%, 9.3%, 8.7%, 8.3%, 8.2%, 8.7% (FY2025)**
(ex-impairment 9.3-10.6% in FY2015-19, 8.7-8.9% in FY2022-25).

**ROW B: THE COMPANY'S OWN RECURRING CAPITAL EXPENDITURE against real-estate D&A** (the EQIX row,
reproduced from DLR's supplements): DLR **19.7%, 17.7%, 18.5%** (FY2023-25: $327.0M, $305.7M,
$343.9M against $1,657.2M, $1,730.1M, $1,855.1M); Equinix 11.8-13.7%. Q4 takes this up.

**ROW C: CAPITAL SPENT TO GROW, the second half of [E2-44].** DLR's *"Improvements to investments in
real estate"* as a share of revenue: **41.8% (FY2015), 35.4%, 46.8%, 43.5%, 44.8%, 52.9%, 56.9%,
56.3%, 64.4%, 51.0%, 52.0% (FY2025)**, before acquisitions and joint-venture contributions; AMT Data
Centers 51-63%; Iron Mountain data centres 198-233%; Equinix 32-58% (EQIX run).

**ROW D: CHURN.** DLR total **7.2%, 6.5%, 4.8%, 6.2%, 5.4%** (FY2021-25); CyrusOne 3.5-3.6% (stale);
Switch 0.6-0.9% (stale); Iron Mountain data centres 3.5-7.0% (2022-24); Cyxtera 10-11% (EQIX row).

**ROW E: WHAT THE OWNER GOT PER SHARE.** Operating income + D&A + impairment per diluted share:
**$7.00 (FY2015), $7.94, $7.56, $8.40, $8.42, $7.35, $7.76, $7.29, $7.56, $7.34, $7.57 (FY2025): 0.8%
a year for ten years**, while diluted shares rose **150%** (138.9M to 347.8M) and gross operating real
estate rose from $10.9bn to $31.4bn. NAREIT FFO per share (10-Ks): **$4.88 (FY2015) to $6.94 (FY2025),
3.6% a year; $6.39 (FY2018) to $6.94, 1.2% a year.** Core FFO per diluted share (computed from the
supplements' *"Core FFO available to common stockholders and unitholders"* over diluted shares and
units): **$6.22 (FY2020) to $7.39 (FY2025)**, 3.5% a year. The dividend has been **$4.88 a share since
2022** ($1.22 a quarter). *Fairness note, [E4-51]: this is operating earnings; the gains on selling
buildings to partners ($4.05bn over FY2021-25) are real value realised and sit outside it; Q4 prices
them.*

**Who names whom.** DLR names *"Equinix, Inc. and NTT; various private operators in the U.S.; as well as
Global Switch Holdings Limited"* (FY2025 10-K); CoreSite, Switch and Cyxtera named DLR; Equinix has named
no competitor since FY2019 and is DLR's sixth-largest customer.

### WHAT THE ROW SHOWS, AND WHAT IT DOES NOT
- **Position: DLR earns what the large product earns.** Rebuilt on DLR's own products and on the
  fairer denominator, DLR sits where every wholesale filer sits (7-10%), below the colocation-and-
  interconnection filers (12-15%). The prior was wrong in its number (6.9-7.4% understated DLR by
  about 1.5 points) and right in its conclusion.
- **Pricing: the market's, in both directions.** The 2023-26 renewal spreads are real and are the
  strongest fact in the file for IN. They were preceded by two years of large-product roll-downs, the
  company's own outlook sentence changed with the market, and a competitor filed the same roll-down in
  the same year. **A price that falls when supply is ample is not a price the company sets.**
- **Returns: not high, and not rising.** [E3-46]: *"the best businesses, by definition, are going to be
  businesses that earn very high returns on capital employed over time."* 8-9% before any maintenance
  and before G&A on the plant, from a filer that must spend half its revenue on new plant, is not that.
- **[E3-61], the row's limit:** it cannot show how the private builders funded by lower-return capital,
  and the hyperscalers building for themselves, will price the capacity now under construction. DLR's
  own development table shows **769 MW** under way at a total cost of **$10.1bn** and *"expected
  yields"* of **11.9%** (Q4 2025 supplement); no other builder's development table was read by this run.

### THE OTHER Q2 TESTS
- **[E2-44] two-characteristic test.** (1) *"an ability to increase prices rather easily (even when
  product demand is flat and capacity is not fully utilized)"*: **FAILS for the large product** on the
  2021-22 record (rolled down while consolidated occupancy was 82.5-83.5%, FY2021-22 10-Ks); **shown weakly for the small product**
  (+1-5% through the cycle, with 8% churn). (2) *"an ability to accommodate large dollar volume
  increases in business ... with only minor additional investment of capital"*: **FAILS outright**:
  35-64% of revenue in new plant every year FY2015-25, and 2026 guidance of *"$3,250 - $3,750 million"*
  of development capex net of partners.
- **[E4-04]: engaged in the company's own words; the scope test answers "replacement" for the plant.**
  Item 1A: *"The tenant improvements may also become outdated or obsolete as the result of technological
  change, the passage of time or other factors, including the recent acceleration in AI adoption and
  rapid advancements in compute, cooling and power technologies"*; *"Our power and cooling systems are
  difficult and expensive to upgrade"*; *"Continued AI adoption could result in evolving infrastructure
  needs, particularly around power density for advanced computing."* v4 asks whether the spending
  defends the same advantage or buys its replacement. For a landlord whose advantage is powered
  capacity, **the capacity is what wears out and is rebuilt**; the land and the grid connection are
  what persist, and those are the part a competitor with capital can also buy.
- **[E2-45] the attacker's test.** The attacker exists, is funded and is named by DLR itself: the
  private investors with *"lower return expectations than us"*, and the customers who can build. DLR
  also finances the attackers' model: it sells 75-80% stakes in its own buildings to such investors at a
  developer's margin (Q1).
- **[E2-58] the commodity doctrine.** *"persistent over-capacity without administered prices (or
  costs) equals poor profitability"*, and the exception is *"a cost advantage that is both wide and
  sustainable"*. Row A shows no wide cost advantage: DLR's return is its product cluster's. The large
  product's own price history (above) is the supply cycle.
- **[E4-36] which cause of extreme success?** **Wave-riding**: cloud, then AI, demand for power. The
  ownable part is the land already connected to power; the wave sets the price.
- **[E4-32] direction: flat to narrowing.** Return on operating real estate 9.3-10.6% (FY2015-19) to
  8.2-8.9% (FY2022-25); operating earnings per share flat for ten years.
- **[E3-33] untapped pricing power: REFUSED** under **[E5-28]**: *"a monopoly or a near monopoly"* is
  what the claim requires, and DLR's customers are its largest counterparties with the option to build.
  The 2026 renewal spreads are prices being raised, not held back; they show the market lifting, and
  the 2021 roll-down shows the market lowering.
- **[E2-53] the dominance class: not available.** Northern Virginia is 21.4% of annualized rent and
  DLR is one of several builders there with power under contract.
- **[E4-23] key-person**: none recorded.

### WHAT THE FRANCHISE CASE RESTS ON, AT FULL STRENGTH **[E4-26, E4-51]**
The best case for IN, stated so its holders would accept it: **power is the binding constraint of this
decade and DLR holds a large bank of it** (3,500 MW developable, 1,000 MW in Northern Virginia, 600 MW
contracted at Astra); **renewal prices on the large product rose 48.7% in H1 2026 and on the small
product in every year FY2014-25 (GAAP)**; the **backlog is a record $1.4bn** at DLR's share; **private
capital pays DLR more than its cost for finished buildings** (the FY2025 fund contribution produced an
$873M gain), which says the market values what DLR builds above what it spends; and the company's
**expected development yields of 11.9%** exceed the 6.5% cap rate at which such buildings trade. Each
fact is true and each is recorded. **What defeats it**: [E3-03] asks for pricing power shown
*regularly* and for *high returns on capital*. The eleven-year record shows the large product's price
falling when supply was ample, the return on operating plant at 8-9% (the large-product cluster's, and
drifting down), operating earnings per share flat while the share count rose 150%, and new capital of
about half of revenue every year to grow at all. **The development margin is a builder's spread in a
tight market, available to every builder with land and power and financed by the very investors DLR
says accept lower returns; [E2-58]: *"nothing fails like success."*** The small product is a genuine
narrow position of the Equinix kind, at a third of the revenue share and with higher churn, and it
cannot be separated from the large product in any filed profit or capital figure.

### CLASS AND VERDICT
- Needed or desired **[x]** · no close substitute **[ ]** (not shown for the large product, 60% of rent,
  whose customers can build and whose price follows the supply cycle; a narrow position for the small
  product) · not price-regulated **[x]**
- **Class: NARROW position in the small product; NO franchise as [E3-03] demonstrates one in the large
  product, which dominates the economics.** **Direction: returns on plant flat to narrowing over ten
  years; per-share operating earnings flat.**
- **The gate does not close on missing evidence.** The private builders' numbers are unfiled and the
  stale peers are four to ten years old; neither is what fails the gate. It fails on DLR's own filed
  returns, its own price history, its own capital intensity and its own sentences about customers who
  can build and investors who accept less. A private builder earning more would not give DLR the
  missing high return on capital; one earning less would confirm the finding.

**VERDICT: [ ] IN  [x] OUT**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
*OUT on the business: [E3-03]'s demonstration clause and [E3-46] fail on DLR's own eleven-year record
(8-9% before maintenance on operating plant, the large-product cluster's return, drifting down; per-share
operating earnings flat for ten years); [E2-44](2) fails outright and (1) fails for the large product on
the 2021-22 roll-downs; [E2-58]'s supply-cycle signature is in the large product's own price series;
[E4-04] is engaged in the company's own words. Not a finding that Digital Realty is badly run or a poor
landlord: it owns a scarce bank of power-ready land in a tight market, and the file records that at
full strength. **The file closes here.** Q3-Q6 below are RECORDED, NOT GOVERNING, as at EQIX, TOST and
the other Q2 closes in wave 5.*

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the
> queue asks every run for a price and because the evidence was gathered; it decides nothing and
> cannot reopen Q2 [E2-37, E3-39].

### STEP 1 - THE WEIGHT CASE
- [ ] **Daily execution** **[E3-38]**: not ticked for operations. Leases run 2-5 years (small) and
  5-15 years (large); average remaining lease term about five years (10-K MD&A). **But the capital
  programme is continuous and large**: *"$3,250 - $3,750 million"* of development capital guided for
  2026 net of partners, **$3.5bn** paid for Blackstone's joint-venture stakes in June 2026, land banks
  bought every quarter. The weight lives in capital allocation, and it is read there.
- [ ] **Control** **[E1-16]**: not ticked; a minority public holding.
- [ ] **Leverage** **[E3-29]**: not ticked, and quantified: **$18.4bn** of debt at 2025-12-31 (92.2%
  fixed or swapped, effective rate 2.90%) against book equity of **$23.3bn** and a market value of
  about **$68bn**; plus **$1.9bn** of DLR's share of unconsolidated entities' secured debt (10-K
  "Off-Balance Sheet Arrangements"). Not the 20:1 bank case.

**Case declared: a qualitative OVERLAY**, with the capital programme and the joint-venture
transactions named as the place a weak or conflicted manager would do the damage.

### THE BINARY - honesty **[E5-16]**, each matter dated to when it became public
- **Litigation**: FY2025 10-K Item 3: *"As of December 31, 2025, we were not a party to any legal
  proceedings which we believe would have a material adverse effect on our operations or financial
  position."* No regulatory inquiry, restatement or auditor change was found in any filing read (KPMG
  auditor *"since 2004"*; clean opinions on the statements and on internal control, FY2025).
- **Directors tied to counterparties, disclosed unprompted** (DEF 14A, 2026-04-17, `0001308179-26-000296`):
  *"In December 2023, Digital Realty and Blackstone Inc. announced a $7 billion joint venture ...
  William G. LaPerch and Stephen R. Bolze serve as advisors to Blackstone"*, with like disclosures for a
  TPG adviser and a Realty Income director; *"The Board reviewed and approved each of the foregoing
  transactions, and in each case determined that the transaction does not constitute a 'related party
  transaction' requiring disclosure."* Disclosure beyond the requirement is the candor direction
  [E2-69]. Bolze joined the Board and its Audit Committee on 2026-01-01 (8-K `0001104659-25-121124`),
  six months before the company bought Blackstone out (below).
- **No disqualifier found.** Per [E5-17] this is the absence of found disqualifiers, not a finding
  that the managers are honest.

### THE INCENTIVE READ **[E4-27]**: the promote on the company's own purchase
The single sharpest Q3 fact in the file, recorded in the filings' own words and not characterised
beyond them:
1. **2025-08-27** (8-K `0001558370-25-011812`): the Board adopted a Carried Interest Plan under which
   executives receive a share of *"carried interest or promote distributions"* from the company's
   joint ventures and funds; the CEO holds **4.5%**, the CFO **1.5%**, the General Counsel **0.5%** of
   each carry vehicle (DEF 14A); up to **50%** of promotes may go to employees; and service vesting
   *"will accelerate and be deemed fully satisfied"* on the first payment date on which the performance
   hurdles are met.
2. **2026-06-29/30** (8-K `0001193125-26-288761`; the Q2 2026 10-Q's acquisitions note): Digital Realty bought Blackstone's 64%
   of two development joint ventures for **$1,231M of cash and $2,346M of stock**. The 10-Q: *"the
   Company recognized $ 201 million of promote income, within Fee income and other and $ 14 million of
   promote expense ... Promote income relates to incentive fees based primarily on the investment's total
   return over certain financial hurdles related to the third party investor, which were achieved at the
   closing of the June 2026 Acquisition. Promote expense relates to the Digital Realty 2025 Carried
   Interest Plan"*, with **$35M** more unrecognized. The same note puts *"the company-earned promote
   ($ 201 million)"* **inside the capitalised cost of the assets acquired.**
3. **So the partner's return cleared its hurdle at the price Digital Realty itself paid; the company
   booked $201M of revenue from that price; and employees are entitled to cash from it under a plan in
   which the three named officers hold carry percentages.** Whether the named officers' carry vehicle
   covers these two joint ventures is not stated in any document read; the 10-Q's $14M plus $35M says the Plan pays on
   this promote. **Named document that would resolve it: the Q3 2026 10-Q and the 2027 proxy.**
4. **The release led with the promote-inclusive figure**: *"Reported Core FFO per share of $2.65 in 2Q26,
   compared to $1.87 in 2Q25; reported Core FFO per share (excluding net promote) of $2.13 in 2Q26"*
   (release of 2026-07-23). The promote was quantified separately at every line and the 2026 outlook
   moved to the ex-promote basis, which is the candor side of [E2-26]; the headline order is the other
   side. **[E2-50]**: *"Where 'earnings' can be created by the stroke of a pen, the dishonest will
   gather"* is a warning about a class of transaction, not a finding about these people [E5-38].

### STEP 2 - THE FLAGS. *Each is a prompt to READ, never a verdict.*
- [x] **EBITDA / adjusted-earnings promotion [E4-29]: FIRES, in the headline and the pay.** The
  balance-sheet policy is *"a debt-to-Adjusted EBITDA ratio of 5.5x"* (10-K Item 1); every release
  reports Adjusted EBITDA; **45% of the CEO's 2025 bonus was Core FFO per share** (DEF 14A: threshold
  $7.00, target $7.10, maximum $7.20, *"Achieved in 2025 ... $7.39"*; bonuses 170-185% of target).
  Core FFO adds back real-estate depreciation. **Against it, the 10-K says the thing in plain words**:
  *"because FFO excludes depreciation and amortization and captures neither the changes in the value of
  our data centers that result from use or market conditions, nor the level of capital expenditures ...
  necessary to maintain the operating performance of our data centers, all of which have real economic
  effect ... the utility of FFO as a measure of our performance is limited."* The disclosure concedes
  [E4-29]'s point; the pay ignores it.
- [x] **Serial share issuance [E5-15]: FIRES.** Diluted shares **133.6M (FY2014) to 347.8M (FY2025),
  +160%**; 370.0M at 2026-07-29; a new **$7.5bn** ATM programme in May 2026; stock paid for DuPont
  Fabros (2017), Interxion (2020), the Teraco put (2026), Blackstone's stakes (2026) and Columbia
  Capital (2026).
- [x] **Dividends funded by issuance [E2-52]: FIRES, the EQIX pattern.** Dividends and distributions
  paid FY2015-25 **$12,748M**; cash raised from common and preferred issuance, net, **$12,886M** (and
  $1,536M of preferred redeemed). FY2021-25: **$7,712M** paid, **$8,065M** raised. The payout exists
  because the capital is replaced.
- [ ] **Projections [E4-22], the record [E3-48]**: guidance set against outturn, the company's own
  Core FFO per share: 2022 guided **$6.80-6.90**, delivered about **$6.70** (below; constant-currency
  $6.91); 2023 **$6.65-6.75**, delivered **$6.59** (below); 2024 **$6.60-6.75**, delivered **$6.72**;
  2025 **$7.00-7.10**, delivered **$7.39** (above); 2026 **$7.90-8.00**, raised to **$8.15-8.20** ex
  promote. Two misses reported as misses in five years: not the unnaturally smooth record [E4-30]
  describes. Not ticked; the guidance culture itself is noted under [E5-30].
- [ ] **Weak accounting / unintelligible footnotes**: not ticked. SBC is expensed; the JV and fund
  notes are long but legible; the promote's dual treatment (revenue and capitalised cost) is disclosed
  in the note.
- [ ] **Metric-switching [E2-49]**: not ticked. *"Core FFO (excluding net promote)"* was introduced in
  Q2 2026 to separate a windfall from the guided number, i.e. to make the guided number smaller; that
  is the direction [E2-49] does not describe. The 2020 product redefinition (Turn-Key Flex/colocation
  to 0-1 MW/>1 MW) followed the Interxion merger, not a deterioration.
- [ ] **Filed-figure tells [E4-30]**: cash taxes are not informative for a REIT (income tax expense
  $32.0M on $1,345M pretax, *"US REIT Status | ( 318,874 )"*); growth is not smooth (Row E at Q2).

### STEP 3 - THE PRIMARY TEST **[E2-01]**, scoped by **[E2-43]**
- **Return on common equity** (net income to common over average stockholders' equity less preferred,
  `q3calc.py`): **2.6% (FY2017), 2.8%, 5.8%, 2.1%, 9.9%, 2.0%, 5.2%, 2.9%, 5.9% (FY2025)**; **excluding
  gains on selling property: 2.0%, 1.9%, 1.9%, -0.4%, 1.8%, 0.9%, 0.0%, -0.2%, 1.3%.** The earnings rate
  on equity comes almost entirely from selling buildings.
- **[E2-43] unleveraged net tangible assets**, the right denominator for a filer whose book equity is
  inflated by three stock-paid acquisitions ($9.7bn of goodwill): (operating income + impairment +
  acquired-intangible amortization) over average net investments in properties = **3.7% (FY2023), 3.7%
  (FY2024), 3.8% (FY2025)**, pre-tax (a REIT pays little tax), before interest, and before the
  developer's gains.
- **[E2-73] the operators' own return** (what they have to work with, not what was paid): the Row A
  figure at Q2, 8.2-8.9% before D&A on operating plant, drifting down from 9.3-10.6%.

### CANDOR - THE HALF-OWNER TEST **[E2-26]**
**Passes on disclosure, with two reservations.** For: the FFO sentence above; recurring capital
expenditure defined in words (*"non-incremental building improvements required to maintain current
revenues ... do not include ... costs which are incurred to bring a building up to Digital Realty's
operating standards"*); renewal spreads published by product in both directions, including the 2021
roll-down (*"rolled down 3.9% on a cash basis"*, Q4 2021 release); the related-director disclosure; the
promote separated. Against: the promote-inclusive figure led the Q2 2026 headline; and the churn and
cash spreads a half-owner most wants appear only in furnished 8-K supplements, never in the 10-K.

### RATIONALITY IS CAPITAL ALLOCATION
- **Buybacks [E5-08]**: none (*"REPURCHASES OF EQUITY SECURITIES ... None."*). Condition (1) fails in
  any case (the business consumes more cash than it makes, Q4); the refusal tell [E2-51] is not
  engaged.
- **Stock deals [E5-44]**: *"The intrinsic value of the shares you give in an acquisition must not be
  greater than the intrinsic value of the business you receive."* On this run's own range (Q5, about
  $20-50 a share on central (c)), the 2026 stock deals paid in shares valued at about **$190.6**
  (Blackstone: $2,346,087,437.83 over 12,310,249 shares) and **$188.1** (Teraco put: $644.4M over
  3,425,031 shares) gave paper worth far less than its quote. **By [E5-44]'s law that favoured the existing holders who received the business,
  and it is recorded that way**; the same arithmetic says the ATM issuance of 2025-26 (average
  $173.09 in 2025, $184.94 in H1 2026) was at a premium to owner-earnings value.
- **The institutional imperative [E2-30]**: (1) resists change: not scored. (2) acquisitions soak up
  funds: **ticked**, land banks bought every quarter (Astra $482M, Q2 2026 land and buildings $213M,
  2025 land $309M), a fund-management firm (Columbia Capital) and a partner buy-out paid largely in
  stock. (3) staff studies for the leader's craving: not observable. (4) peer imitation: not scored;
  the fund model is common in the industry but no filing states imitation.
- **Pro-Am [E2-56]**: the blended record camouflages nothing here because nothing is blended: one
  segment, one product family. What it camouflages is time: per-share operating earnings flat for ten
  years (Q2 Row E) behind a doubling of revenue.

### THE GUARDRAIL
- [x] Nothing in this Q3 is used to promote the name; the file is closed at Q2 [E2-37, E2-38, E3-39].
- [x] No key-person dependence recorded at Q2 [E4-23].
- [x] No great-manager case is made [E2-35, E2-36].

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary** (no disqualifier found) · overlay case ·
  flags live: [E4-29] in headline and pay, [E5-15] serial issuance, [E2-52] dividends matched by
  issuance, **the promote on the company's own purchase [E4-27]** with its officer allocation a named
  open document · [ ] OUT [ ] UNRESEARCHED [ ] UNKNOWABLE.
  *IN = no disqualifier found. NOT a finding that the managers are honest [E5-17]. IN never promotes.*

## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the
> queue asks every run for a price and because the (c) question is the one this name was queued
> on; it decides nothing and cannot reopen Q2 [E2-37, E3-39].

### THE SKIP REASON, TESTED ON THE FILING RATHER THAN INHERITED
The wave 5 label is *"capex unresolved [E5-20]: build (c) by hand from the filing"*. The checks the
dated notes ask for, in order (`oe_screen.py`, `oe_screen_out.txt`, companyfacts fetched today):

**(a) The current `owner_earnings()` does NOT price DLR, and it now stops one step earlier than the
label says.** It returns **`SBC_UNRESOLVED`**. The face of the cash-flow statement carries *"Amortization
of share-based compensation | 93,766 | 75,606 | 80,532"* (FY2025 10-K), and **no element in companyfacts
carries those values** (searched by value across `dei`, `invest`, `srt`, `us-gaap`, `ecd`, `ffd`): Digital
Realty tags stock compensation under an element companyfacts does not publish, so `sbc_annual()` returns
nothing for any year. This is the 2026-09-12 SBC fix (RESUME STATE item 3F) working as designed: before
it, the screen would have substituted zero.

**(b) Behind it, a REAL TAG GAP, not the AMZN/CL artefact: the capex line sits under an element no
`CAPX_TAGS` member reaches, for every year.** `CAPX_TAGS` is `PaymentsToAcquirePropertyPlantAndEquipment`,
`PaymentsToAcquireProductiveAssets`, `PaymentsForCapitalImprovements`; `annual(f, CAPX_TAGS)` returns
**`{}`** for DLR. The face line *"Improvements to investments in real estate | ( 3,181,179 )"* is tagged
**`PaymentsToDevelopRealEstateAssets`**, which carries **FY2009-FY2025 without a hole** ($392.4M in
FY2009 to $3,181.2M in FY2025). `capital_acquired()` returns two empty series. **So the triage's
`CAPEX_UNRESOLVED` was a true reading of the screen, and it still is**: the first name in this row where
the label was right on the day it was written and is right today.

**(c) A second real-estate capital line, as the EQIX note asked.** `PaymentsToAcquireRealEstate`
carries FY2009-FY2018 (acquisitions of real estate, $24.3M to $1,560.1M a year) and stops; the face then
carries *"Cash paid for acquisitions"* (FY2018-20) and *"Cash paid for business combination / asset
acquisitions, net of cash acquired"* (FY2021-25). The screen's `ACQ_TAGS` series has FY2020 and FY2025
and **no value for FY2021-24**, and reads **$309.0M** for FY2025 against **$321.2M** on the face. And a third capital outflow no tag list names:
*"Investments in and advances to unconsolidated entities"* (**$519.1M** FY2025, `PaymentsToAcquireEquityMethodInvestments`),
the company's share of building inside its joint ventures and funds. **Overlapping elements with
different values** (the TOST and EQIX checks): `PaymentsToAcquireBusinessesNetOfCashAcquired` carries
two values for FY2018 ($2,090.5M and $1,679.8M) and two for FY2019 ($75.7M and $0.0M); `annual()` keeps
the earliest filed vintage. Outside every window priced here.

**(d) What the D&A is made of.** FY2025 *"Depreciation and amortization | 1,894,636"* (face):

| component | FY2025 $M | source |
|---|---:|---|
| depreciation of buildings, improvements, tenant improvements; amortisation of deferred leasing costs | about 1,624 | residual |
| **amortisation of acquired intangibles** (customer relationships, in-place leases, from DuPont Fabros, Interxion, Teraco) | **231.3** | *"Amortization of customer relationship value, acquired in-place lease value and other intangibles ... $ 231.3 million"* |
| non-real-estate depreciation | 39.5 | FFO reconciliation, *"Non-real estate depreciation | (39,492)"* |

**12% of the D&A is acquisition accounting (the SPGI kind), 88% is plant.** `da_annual()` returns
`DepreciationAndAmortization` = $1,894.6M, the face total, exactly; no NVDA-type defect.

**(e) [E5-20] asked separately, on the filing: YES, the exception class applies, on capital intensity,
and the replacement-cost evidence is WEAKER than at EQIX.** The filed facts, both ways:
1. **Capital intensity beyond a railroad's.** Gross operating real estate **$31,359M** against revenue
   **$6,113M (5.1x)**, before construction in progress ($4,977M), goodwill and joint ventures;
   improvements alone **35-64% of revenue every year FY2015-25**. v4 names the class
   (*"Where the business is capital-intensive"*, with railroads, airlines and utilities as its
   examples) and the consequence (*"the D&A end of any owner-earnings range is INVALID"*).
2. **Obsolescence named in the company's own words**: *"Our power and cooling systems are difficult
   and expensive to upgrade"*; tenant improvements *"may also become outdated or obsolete as the result
   of ... rapid advancements in compute, cooling and power technologies"* (Item 1A).
3. **Old plant is written down and sold rather than renewed through capex**: impairments of *"certain
   non-core properties in secondary U.S. markets"* **$118.4M, $191.2M, $78.6M (FY2023-25)**; *"we sold
   non-core data centers in the Atlanta, Miami, Boston and Dallas metro areas"* (FY2025).
4. **But against the exception, recorded at full strength**: **no useful-life shortening** was found
   (buildings and improvements *"5 - 39 years"*, machinery and equipment *"7 - 15 years"*, FY2025 10-K,
   unchanged in the policy text read), unlike AMZN and EQIX; and **the replacement cost is not running
   away**: the development tables give total cost per MW under construction of about **$12.7M (Q4
   2021: $3,234.8M for 254.6 MW), $12.6M (2022), $13.2M (2023), $11.5M (2024), $13.1M (Q4 2025: $10.1bn
   for 769 MW) and $14.4M (Q2 2026: $20.2bn for 1,402 MW)** (supplements), about 1.14x the FY2021-25
   average at mid-2026, against EQIX's doubling per cabinet. (Both the Q4 2021 and Q4 2025 tables
   state that cost includes a pro rata share of acquisition and infrastructure cost; the layout changed
   in the Q4 2024 supplement and the later tables include joint-venture projects, so the series is
   approximate.)

**So v4's rule applies as written: the D&A end is INVALID and (c) is judged upward from total capex.
The capex-less-growth route EQIX used cannot be built here**: Digital Realty filed no consistent
capacity series (MW in service) for FY2021-25 (the 10-Ks read report the portfolio in square feet; the
*"White Space IT Load"* MW table appears in the Q2 2026 10-Q), so growth capex cannot be measured independently of the company's own development label. That
limit is recorded, not smoothed.

**Of the eight names now run from this row: ABNB a real presentation gap, AMZN none, NVDA a tag gap plus
a history gap, CL a tag gap, SPGI a tag gap plus a (c) question about acquisitions, TOST a tag gap plus a
definition break, EQIX no tag gap but a mis-assigned early value and an unread real-estate line, and DLR
a REAL tag gap on every year (capex under `PaymentsToDevelopRealEstateAssets`) behind an SBC element
companyfacts does not publish; the [E5-20] exception class applies at AMZN, EQIX and DLR.**

### (c): THE DISCLOSED JUDGMENT
*"(c) must be a guess"* [E2-23]. The band, FY2025, from filed figures (`oe.py`):

| route | (c) FY2025 | how |
|---|---:|---|
| the company's *"recurring capital expenditures"* | $343.9M | *"non-incremental building improvements required to maintain current revenues"*; **rejected as (c)**: 18.5% of real-estate D&A would renew the plant about once in 90 years, and the definition excludes *"costs which are incurred to bring a building up to Digital Realty's operating standards"* |
| **central: plant depreciation** (D&A less acquired-intangible amortisation) | **$1,663.3M** | not the D&A default: the renewal cost judged at the observed build cost, which (e) shows has not risen materially (build cost per MW about flat FY2021-25, 1.14x at mid-2026) |
| **conservative: plant depreciation at current build cost, plus the wear written off** | **$2,030.6M** | $1,663.3M x 1.143 (Q2 2026 cost per MW over the FY2021-25 average) + $129.4M (FY2023-25 mean impairment of older plant) |
| total improvements (all growth included) | $3,181.2M | the ceiling; displayed |

Stock compensation is subtracted in full at the face figure [E5-06]; the capitalised compensation of
construction staff (*"$ 140.6 million"* FY2025) and capitalised interest (*"$ 127.2 million"*) sit inside
the improvements line, i.e. with growth, and are not added to (c).

### OWNER EARNINGS - THE ONE NUMBER **[E2-23]**
Construction (CONVENTION, v4 section VI): operating cash flow, less stock-based compensation, **less the
preferred dividends** (a senior claim), **less the Teraco minority's share** (*"The Teraco noncontrolling
share of FFO was $63,566, $46,953, and $39,386"*, FY2025-23; $11,919 FY2022), less (c). Every figure from
the filed cash-flow statements (10-Ks FY2017, FY2020, FY2023, FY2025; 10-Q Q2 2026). Never a net-income
proxy: net income here is mostly gains.

| $M | FY2016 | FY2017 | FY2018 | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| operating cash flow | 911.2 | 1,023.3 | 1,385.3 | 1,513.8 | 1,706.5 | 1,702.2 | 1,659.4 | 1,634.8 | 2,261.5 | 2,412.1 |
| SBC (face) | 17.4 | 20.5 | 27.2 | 34.9 | 74.6 | 84.1 | 92.5 | 80.5 | 75.6 | 93.8 |
| preferred dividends | 83.8 | 68.8 | 81.3 | 75.0 | 76.5 | 45.8 | 40.7 | 40.7 | 40.7 | 40.7 |
| Teraco minority share | | | | | | | 11.9 | 39.4 | 47.0 | 63.6 |
| plant depreciation (c central)* | 518.7 | 595.0 | 770.3 | 809.5 | 1,010.5 | 1,223.7 | 1,324.6 | 1,442.9 | 1,531.4 | 1,663.3 |
| company "recurring" capex | | | | | 210.7 | 217.1 | 266.5 | 327.0 | 305.7 | 343.9 |
| improvements to real estate | 758.1 | 1,150.6 | 1,325.2 | 1,436.9 | 2,064.1 | 2,520.8 | 2,643.1 | 3,525.6 | 2,831.7 | 3,181.2 |
| **OE, central (c)** | **291** | **339** | **507** | **594** | **545** | **349** | **190** | **31** | **567** | **551** |
| OE, conservative (c) | 88 | 125 | 267 | 349 | 271 | 44 | -129 | -304 | 219 | 184 |
| *display:* OE, company (c) [rejected] | | | | | 1,345 | 1,355 | 1,248 | 1,147 | 1,793 | 1,870 |
| *display:* OE, all improvements as (c) | 52 | -217 | -48 | -33 | -509 | -949 | -1,129 | -2,051 | -734 | -967 |
| *below the line:* gains on selling property | 170 | 40 | 80 | 335 | 317 | 1,381 | 177 | 901 | 596 | 996 |

\* *FY2016-20: the cash-flow line "Depreciation and amortization of buildings and improvements, tenant
improvements and acquired ground leases"; FY2021-25 the face adopted one D&A line, so plant depreciation
is D&A less the acquired-intangible amortisation from the notes, which also leaves in about $40M of
non-real-estate depreciation and the deferred-leasing-cost amortisation. A definition break at FY2021,
disclosed; it makes FY2021-25 (c) slightly higher, i.e. conservative.*

**MORE THAN ONE WINDOW [E4-25, E4-38], and THE PERIMETER REFUSAL.** Every window crosses a perimeter
change, because the business is built on them: DuPont Fabros (September 2017, stock), Interxion (March
2020, stock), the Ascenty and Digital Core REIT deconsolidations (2019, 2021), Teraco (August 2022),
the stake sales to Blackstone, Mitsubishi, GI Partners, TPG, Brookfield and the Fund (2023-25), and the
Blackstone buy-in (June 2026, $5.2bn of assets, after the last full year). **No filing gives pro forma
operating cash flow for any of them; a pro forma rebuild is refused, as at DKS, CNR and STLA**, and the
windows are shown as filed, with the per-unit series beside them:

| window | OE central (c) | OE conservative (c) | OE company (c) [display] | gains realised, mean | OE central per diluted share and unit |
|---|---:|---:|---:|---:|---:|
| **five-year default [E2-42], FY2021-25** | **$337M** | **about $3M (zero)** | $1,483M | $810M | $1.20 (FY2021) to $1.59 (FY2025) |
| three-year, FY2023-25 | $383M | $33M | $1,603M | $831M | |
| ten-year, FY2016-25 (crosses two stock mergers; display only) | $396M | $111M | n/a | $499M | $2.01 (FY2020, first year with units filed) |
| **FY2025** | **$551M** | **$184M** | $1,870M | $996M | $1.59 |
| TTM to 2026-06-30 | about $995M | | | | includes Singapore insurance recoveries (*"$ 112.8 million recognized in Other income, net"*); display |

**The combined range on the default window runs from about zero to about $0.55bn (FY2025 central),
with the five-year central near $0.34bn.** [E4-25]: *"Usually, the range must be so wide that no useful
conclusion can be reached."* The spread is itself a Q4 finding [E5-11]: FY2023's operating cash
(**$1,634.8M**, below FY2020's) carries a $380M working-capital outflow in a year of $2.6bn of asset
sales, and the per-unit central fell from **$2.01 (FY2020) to $1.59 (FY2025)**.

**The gains are not owner earnings, and they are not nothing.** $4.05bn of gains over FY2021-25 is the
developer's margin realised by selling 75-80% stakes in finished buildings; it is value created by the
growth capex and taken as cash by shrinking the perimeter. [E4-41] asks for favourable exogenous breaks
to be removed; this is not exogenous, so it is displayed beside the owner earnings (and at Q5), not
netted into them and not deleted.

**Stock compensation**: 3.9% of operating cash FY2025, 4.4% over FY2021-25. Not the ARM/TOST shape.

### GREAT, GOOD, OR GRUESOME? **[E4-20, E4-43]**
- [ ] great · [ ] good · [x] **gruesome-leaning, on the incremental numbers**
FY2015 to FY2025, gross operating real estate rose **$20.4bn** ($10.9bn to $31.4bn) and goodwill **$9.4bn**,
while operating income + D&A + impairment rose **$1,659M**: **8.1% on the added plant, 5.6% with the
goodwill**, before any maintenance (`q2calc.py`). Operating income alone rose from $401.9M to $658.5M. Per
diluted share, operating income + D&A rose **0.8% a year** for ten years. [E4-20]'s gruesome account
*"requires you to keep adding money at those disappointing returns"*; [E4-43] passes the good class at
roughly 20% pre-tax on net tangible assets, and DLR earns **3.7-3.8%** on net tangible real estate
(Q3). The company's own view is the 11.9% *"expected yields"* on the development book; the realised
decade is the record.

### STAYING POWER - score all three **[E5-11]**
- **(1) A large and reliable stream of earnings: YES.** Rent under leases averaging about five years
  remaining, the large ones 10-15 years to investment-grade tenants; *"the 20 largest customers ...
  approximately 51%"*; operating cash $2.4bn.
- **(2) Massive liquid assets: NO.** **$1,864.8M** of cash at 2026-06-30 against **$18,767.6M** of debt
  (62.9% in euros). The $4.5bn revolver is a bank line [E5-39].
- **(3) No significant near-term cash requirements: NO.** Open construction commitments **$4.1bn**
  (2026-06-30); remaining 2026 capex guided **$2.8-3.3bn**; debt maturities **$825M** (rest of 2026),
  **$2,165M** (2027, including the $726M construction loan assumed from Blackstone's joint venture),
  **$2,530M** (2028); dividends and distributions about **$1.7-1.8bn** a year; the rest of the Teraco put
  (23% of Teraco, puttable to January 2028 and callable from February 2028). Financed every year by the ATM, the bond
  market and asset sales.
- **Score: 1 of 3.** **Leverage [E4-16, E3-29]:** $18.8bn of debt plus DLR's **$1.9bn** share of
  joint-venture debt, against book equity of $28.0bn and a market value of about $69bn. **[E2-54]'s
  coverage test, as written:** FY2025 cash interest (**$380.5M** paid + **$127.2M** capitalised = $507.7M)
  against operating cash before interest ($2,792.6M) net of ample capital expenditure (central (c)
  $1,663.3M): **$1,129.3M, 2.2x covered**; at conservative (c) ($2,030.6M), **$762.0M, 1.5x**. Thinner
  than Equinix's 4.4x. **[E3-52] terms**: mostly fixed-rate senior notes (effective **2.90%**), the new
  ones at **3.75-4.25%** (euro notes, 2025) and guided at **4.0-4.5%**: every refinancing costs more.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**
**The mechanism: the capacity race, refinanced.** Everyone with land and power is building for the same
hyperscale tenants with capital that, in the company's own words, accepts *"lower return expectations
than us"*; [E2-27]: *"viewed collectively, the decisions neutralized each other and were irrational ...
After each round of investment, all the players had more money in the game and returns remained
anemic."* The large product's price has already shown it will fall when supply is ample (2021-22 cash
roll-downs of 11.9% and 3.3%), while the company's cost of debt rises as 2.9% notes roll into 4%+ ones.

**Quantified from filed figures.** Large-product annualized rent is **$2,506M**, of which about 6% a year
expires (2026: $260M; 2027: $258M; supplement). A repeat of 2021's **-11.9%** on expiring large leases
costs about **$31M a year, compounding**; the bigger exposure is the **$20.2bn development book** (Q2
2026, 1,402 MW, 54% leased) leasing into an ample market below its 11.5% expected yield. On the debt
side, **each 1 point on $18.8bn as it refinances is about $188M a year, a third of FY2025 central owner
earnings**; about **$5.5bn** matures by the end of 2028. The dividend (about **$1.8bn**) already exceeds
central owner earnings more than three times over. **The business does not go broke**: investment-grade,
laddered fixed-rate debt, 2.2x interest cover on central (c), and a market for its buildings deep enough
to sell $1.6-2.6bn a year in FY2023-25. **It dies as an investment the way [E2-27] describes**, with owners' capital
replaced each year by new owners'.

- Survival shapes (`Screens/SURVIVAL SHAPES - index.md`): **#6 THE BORROWED BALANCE SHEET** (dividends
  of $12.7bn FY2015-25 matched by $12.9bn of equity raised; growth funded by notes and asset sales), with
  **#11 THE PASS-THROUGH** (the capacity race hands the gains to hyperscale tenants) as the mechanism and
  **#9 THE WAREHOUSE** as a feature (the company builds on its own balance sheet, sells stakes into funds
  it manages, and buys partners back with its own stock, earning a promote on the purchase). **No new
  shape is proposed.**
- **Exposure, not experience [E4-40]:** FY2023-H1 2026 is the tightest market in the record; the filed
  2021-22 roll-downs are the exposure the recent experience hides.
- **Likelihood: [ ] likely [x] a real possibility [ ] a low-level possibility** for a price-led
  compression of large-product returns; **a low-level possibility** for insolvency.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on survival**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *It survives: investment-grade, laddered fixed-rate debt, 2.2x interest cover on central (c), a deep
  market for its buildings. But staying power scores 1 of 3; the five-year owner-earnings range runs
  from about zero to about $0.55bn with a central near $0.34bn, on a perimeter no window holds still;
  and per-unit owner earnings fell from $2.01 (FY2020) to $1.59 (FY2025).*

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
*Q5 does not open: Q2 is OUT. The arithmetic below is recorded because the queue asks every run for
a price, and it carries no entry language. It is not a ranking and it arms nothing.*

**The pair:** price **US$184.26**, the **2026-09-17 close** (Yahoo daily chart, aggregator, flagged;
corroborated by Form 4 `0001500081-26-000009` at $193.96 on 2026-08-27, inside that day's range) x
**370,036,176 shares** (10-Q cover, accession `0001104659-26-089296`, as of 2026-07-29; issued equals
outstanding) x split factor **1.0** = **market capitalisation US$68,182.9M**. On the perimeter the
owner earnings are measured on (the Operating Partnership's cash, shared one-for-one with the 6,665
thousand third-party common units): **US$69,411.0M**, used for every yield below. **Sovereign USD
30-year 5.29%**, US Treasury daily par yield curve, the issuing authority, **09/17/2026**. Pending
shares (Columbia Capital 2.34M issued after the cover date, the Teraco put 3.43M, up to 1.46M more on
the Columbia earn-out) would add about 2% to the count and are not blended.

Owner earnings are levered (operating cash is after interest paid), so no debt is added to the cap;
preferred dividends and the Teraco minority are already deducted (Q4). **Interest income is not
separately disclosed** (it sits in *"Other income, net"*, $161.1M FY2025, with FX and insurance items),
so it is left in owner earnings and the $1,864.8M of cash is left in the cap; the two roughly offset
(cash is 2.7% of the cap).

| construction | owner earnings | yield on $69.4bn | vs 5.29% | perpetual growth needed to reach ~10% |
|---|---:|---:|---:|---:|
| **central (c), five-year default FY2021-25** | **$337M** | **0.49%** | **-4.80 pts** | **9.5%** |
| central (c), three-year FY2023-25 | $383M | 0.55% | -4.74 pts | 9.5% |
| **central (c), FY2025** | **$551M** | **0.79%** | **-4.50 pts** | **9.2%** |
| central (c), TTM to 2026-06-30 (insurance-flattered) | about $995M | 1.43% | -3.86 pts | 8.6% |
| conservative (c), FY2025 | $184M | 0.26% | -5.03 pts | 9.7% |
| conservative (c), five-year | about $3M | 0.00% | -5.29 pts | 10.0% |
| *display:* central FY2025 plus the five-year mean of realised gains ($810M) | $1,361M | 1.96% | -3.33 pts | 8.0% |
| *display:* the company's own (c), FY2025 (rejected at Q4) | $1,870M | 2.69% | -2.60 pts | 7.3% |
| *display:* the company's AFFO, FY2025 | $2,268M | 3.27% | -2.02 pts | 6.7% |
| *display:* the company's Core FFO, FY2025 | $2,558M | 3.69% | -1.60 pts | 6.3% |

(`q5.py`, `q5_out.txt`.)

**1. THE YIELD.** On central (c): **0.5% (five-year) to 0.8% (FY2025)** against **5.29%**. **Even on the
company's own maintenance figure, rejected at Q4, the yield is 2.7%; on AFFO, 3.3%; on Core FFO, the
number the CEO's bonus is paid on, 3.7%. Adding back every dollar of the developer's gains still gives
2.0%. No construction on disk, the company's included, reaches the bond.**

**2. WHAT THE PRICE ALREADY ASSUMES.** About **9.2% a year of growth in perpetuity** from FY2025's
central owner earnings to reach the ~10% floor [E4-28], and about **4.5%** merely to match the bond.
**What the business has actually done**: operating income + D&A per diluted share **+0.8% a year for ten
years**; central owner earnings per diluted share and unit **$2.01 (FY2020) to $1.59 (FY2025)**; Core FFO
per share $6.22 to $7.39 (FY2020-25), 3.5% a year. [E4-35]'s base rate is the burden: fewer than one in
twenty of the best businesses sustain 15% for twenty years, and this case needs about 9% forever. **[E4-44]
and [E2-63] are the binding bounds**: value cannot outgrow earnings, and growth here is bought with new
capital at about 8% before maintenance on the added plant (5.6% with the goodwill), with the share count
growing to pay for it.

**3. WHAT YOU ARE PAID.** **Minus 4.5 to minus 4.8 points against the sovereign** on central (c); minus
2.0 points on the company's own AFFO.

**Certainty is not priced in the rate [E3-42].** Sovereign used 5.29%, bare. No per-name premium.

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-01]**
Value per share and unit = owner earnings / (0.10 - g), over 376.70M shares and third-party units:

| owner earnings | g = 3% | g = 5% | g = 7% | g = 8% |
|---|---:|---:|---:|---:|
| **central (c), FY2025 ($551M)** | $21 | $29 | $49 | $73 |
| central (c), five-year ($337M) | $13 | $18 | $30 | $45 |
| *display:* company (c), FY2025 ($1,870M) | $71 | $99 | $165 | $248 |

**Value, in round numbers: roughly $20 to $50 a share** on central (c) at 3-7% perpetual growth.
**Current price: $184.26, above the whole range**, reached only by granting the company's own
maintenance figure AND about 7% growth forever. **At the conservative (c) no value can be computed on
the five-year window.**

**Which bar:** the screamer test [E4-01] only, because the file is closed and no margin is applied.
**Above the whole range.** **Windage count: ONE** ((c) judged up from total capex at the central
end; the conservative end shown as a bound, not spent as a second margin; growth rates displayed, not
chosen).

- **VERDICT: none. Q5 did not open (Q2 OUT).** Had every gate been IN, the computation shows a 0.5-0.8%
  business yield against a 5.29% sovereign and a ~10% floor [E4-28]: below both, **FAIL** on price as
  well, on every construction including the company's own.

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

> **RECORDED, NOT GOVERNING.** Nothing is owned and nothing is armed. These are the conditions on
> which the file would be REOPENED at Q2 [E1-02]; a Q2 OUT is a finding about the business, so a
> price alert would be a category error (the QLYS ruling, 2026-09-07).

**What would reopen Q2 (each observable in a filing):**
1. **Returns on operating plant that rise while the plant grows.** (Operating income + D&A +
   impairment) over average Schedule III gross real estate back above its FY2015-19 level
   (**9.3-10.6%**) and rising for three consecutive 10-Ks, with development capex at the guided pace.
   That is [E3-03]'s *"thereby to earn high rates of return on capital"*.
2. **Large-product pricing that holds through a supply-ample year.** The >1 MW cash renewal spread
   staying positive in a year in which the company's own outlook sentence reverts from *"to be
   positive"* to *"generally ... consistent with the rates currently being paid"* (the FY2021 wording),
   or in which a competitor files a roll-down. The 2021-22 record is the test it failed.
3. **Per-share earnings that grow without the share count.** Operating income + D&A per diluted share
   (FY2025 $7.57) rising faster than 3% a year for three years while diluted shares grow less than 2%
   a year: [E2-44](2)'s *"only minor additional investment of capital"*.
4. **A maintenance disclosure that meets the corpus's (c).** A filed figure for the capital needed to
   keep existing buildings at current power density and unit volume, whatever the company calls it.

**Thesis-confirming (for the OUT):** large-product renewal spreads turning negative as the 1,402 MW
pipeline (54% leased at Q2 2026) delivers; the stabilized-portfolio occupancy (83.7% at Q4 2025)
falling as capacity is added; impairments of *"non-core properties"* recurring; dividends continuing to
exceed owner earnings with issuance and asset sales filling the gap; promotes on partner buy-outs
recurring in Core FFO.

**Next dated documents:** the Q3 2026 10-Q and earnings release (late October 2026; the Teraco put
settlement, the Columbia Capital closing, and whether the named officers' carry covered the June
promote), the FY2026 10-K (February 2027), and the 2027 proxy.

**Position size:** none. **VERDICT (RECORDED, NOT GOVERNING): not applicable; the file closed at Q2
and the reopening conditions are recorded above.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN → **Q2 OUT, the file closed**; Q3-Q6
  recorded beneath explicit RECORDED, NOT GOVERNING banners, as at EQIX and TOST.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the
  filed income statement, supplement and property note. The stale peers and unfiled private builders
  at Q2 are named and are not what closes the gate.
- [x] No UNRESEARCHED verdict was returned. One open document is named inside a recorded section (the
  officers' carry allocation for the June 2026 promote: Q3 2026 10-Q, 2027 proxy); it governs nothing.
- [x] No UNKNOWABLE verdict was returned.
- [x] Step 0: the filing was read with accession numbers; three figures on the face of the FY2025
  cash-flow statement cross-checked to companyfacts, and a fourth (stock compensation) found to be in
  no published element, which is the Q4 finding; one peer figure (CyrusOne FY2021) checked to its filed
  text.
- [x] Owner earnings on multi-year windows (five-year default, three-year, ten-year display, FY2025,
  TTM), hand-built from the filed cash-flow statements; (c) disclosed as a judgment with the company's
  figure displayed and rejected; the perimeter refusal stated because every window crosses a merger,
  a deconsolidation or a stake sale.
- [x] Competitor row rebuilt for DLR's products from filings (nine examined, four current filers),
  not imported from the EQIX run; the EQIX row's DLR figure corrected on the fairer denominator.
- [x] Sovereign for the reporting currency (USD), from the issuing authority, dated 09/17/2026,
  re-struck by this run; the 48.2% non-US revenue named.
- [x] Value stated as a round-number range under a COMPUTATION — NOT A CLEARANCE heading.
- [x] One bar (the screamer test); windage count one.
- [x] Price dated as a close, aggregator flagged, corroborated by a Form 4 inside the day's range.
- [x] Run committed to git after every gate, with a pathspec.
- [x] Every ledger id cited was looked up in `principle_ledger.csv` (`led.py`) before it was written.
- [x] No em dashes in anything this run wrote (the template's own headings and the required
  `COMPUTATION — NOT A CLEARANCE` heading carry them).
- [x] Never presented as proven to beat the market; nothing here claims it.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **Q3, corrected before the next gate (commit `64030e7`)**: the first committed wording said
   employees *"including the executives who negotiated the purchase"* are entitled to cash from the
   June 2026 promote. No document read says who negotiated, or that the named officers' carry vehicle
   covers those joint ventures; the sentence now states the officers' carry percentages and names the
   allocation as open.
2. **Q4, corrected before Q5 (commit `f77e9b3`)**: a parenthesis said the development table's cost
   definition *"widened in the Q4 2024 supplement"* to include acquisition and infrastructure cost. The
   Q4 2021 supplement's footnote already includes them; the note now says the layout changed and the
   later tables include joint-venture projects.
3. **Drafts corrected before commit, recorded because they were mine**: a Q2 draft said the backlog
   *"doubled"* ($817M to $1.4bn is +71%, and part of it was bought with the Blackstone stakes); a Q2
   draft asserted that other builders' development tables show similar yields (none was read; the
   sentence was removed); a Q3 draft said every stock deal was paid in shares quoted at $150-190,
   which no filing read supports for the 2017 and 2020 mergers (replaced with the 2026 deal prices
   derived from the 8-Ks); a Q4 draft gave
   SBC as 4.8% of operating cash over FY2021-25 (it is 4.4%).
4. **A placeholder preferred balance for FY2015 in `q3calc.py`** (`prefv`) was not from a filing; the
   FY2016 return-on-equity figure that used it is not reported anywhere in the run.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **The five kinds of capex gap it offered did not include what DLR has.** The brief asked which of
   *"tag change, tag overlap with different values, history hole, presentation change, or none"* the
   label was. It was none of them: the capex line sits under `PaymentsToDevelopRealEstateAssets` in
   **every** year FY2009-25, an element no `CAPX_TAGS` member reaches, so the triage's label was simply
   right; **and the current screen stops one step earlier, on `SBC_UNRESOLVED`**, because DLR's stock
   compensation is in no element companyfacts publishes. The brief pointed at the EQIX real-estate
   line; the real-estate line here IS the capex line.
2. **The perimeter list stopped at 2022.** The brief named Interxion (2020, confirmed: closing 8-K
   `0001193125-20-072868`) and Teraco (2022, confirmed: *"On August 1, 2022, we completed our acquisition
   of a majority interest in Teraco"*). It did not name DuPont Fabros (2017, stock), the 2019 and 2021
   deconsolidations, or **the largest perimeter change in the record, which sits after the last full
   year**: the June 2026 Blackstone buy-in ($3.5bn for 64% of two joint ventures, $5.2bn of assets
   capitalised, 12.3M shares), with the Teraco put (3.43M shares), Columbia Capital (a fund manager,
   2.34M shares plus an earn-out) and the Astra land ($482M) in the same quarter.
3. **The prior about the EQIX row was wrong in its number, and the brief's figure carried the error.**
   The brief quoted DLR's return on plant as *"6.9-7.4%"*. That row's denominator included about $5bn
   of construction in progress and land held; on operating real estate, ex-impairment, the figure is
   **8.7-8.9%** (FY2023-25). The brief was right that the row should not be imported, and the corrected
   figure still sits in the large-product cluster, so the conclusion survives the correction.
4. **The brief did not anticipate the promote.** Its Q3 prompts were the 8-K earnings releases and
   [E4-29]/[E4-22]; the sharpest Q3 fact is a $201M promote booked as revenue on the company's own
   purchase price, with a carried-interest plan for employees adopted ten months earlier. Recorded at
   Q3, not governing.
5. **The REIT routing note** pointed at a sector method that does not exist; the brief said so and was
   right. Recorded at Step 0.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`tools/sources.price()` returns an intraday `regularMarketPrice` stamped with today's date** while
  its docstring says *"Latest close."* Third name (TOST, EQIX, DLR).
- **`floor_screen.CAPX_TAGS` does not reach `PaymentsToDevelopRealEstateAssets`**, where DLR files its
  whole capex line every year FY2009-25 (and where other REITs may). Adding it would change a number,
  so it is a proposal for the operator, not a fix made here; with it, the EQIX proposal
  (`PaymentsToAcquireRealEstate`) would cover the two data-centre REITs' two capital lines.
- **SBC in a non-published element**: DLR's *"Amortization of share-based compensation"* is in no
  element companyfacts carries. `SBC_UNRESOLVED` is the right answer; no tag rule recovers it (the
  resume note's source-limit class).
- **`ACQ_TAGS` misses DLR's FY2021-24 acquisitions** (the screen series has FY2020 and FY2025 only)
  and reads $309.0M for FY2025 against $321.2M on the face.
- **A same-element denominator for REIT peers exists**: `RealEstateGrossAtCarryingValue` (Schedule
  III gross) resolves for DLR, EQIX, CyrusOne, QTS, CoreSite and DuPont Fabros, and equals DLR's
  operating real estate at cost excluding construction in progress. It gives a row without per-filer
  hand definitions (`rowcalc.py`).
- `Screens/cover_shares.py DLR` matched the 10-Q cover exactly.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**Read the price series of the product, through a cycle, before reading the latest spread.** DLR's
2026 renewal spreads (+48.7% cash on large leases) are the strongest fact for a franchise in the file;
the same filer's 2021-22 roll-downs (-11.9%, -3.3%), and a competitor's same-year sentence, turn them
into [E2-58]'s supply cycle. Every REIT and every capacity business files renewal or rate tables; the
series, not the quarter, is the moat evidence.

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** DLR FAILS AT Q2 (OUT, on [E3-03]'s demonstration clause and [E3-46]: rebuilt for DLR's
  own products, return on operating plant 8.2-8.9% (FY2023-25), the large-product cluster's return and
  drifting down from 9.3-10.6%; large-product cash renewals -11.9% (2021) to +48.7% (H1 2026), the
  supply cycle [E2-58]; per-share operating earnings +0.8% a year for ten years with shares +150%;
  [E2-44](2) fails on capex of 35-64% of revenue; [E4-04] engaged in the company's own words). Q1 IN;
  Q3 IN on the binary (recorded; [E4-29] in the pay, serial issuance, dividends matched by issuance,
  a $201M promote booked on the company's own purchase); Q4 IN on survival (recorded; a real tag gap
  behind `SBC_UNRESOLVED`; [E5-20] exception class applies on capital intensity; five-year owner
  earnings about zero to $0.55bn, central about $0.34bn; staying power 1 of 3); price $184.26 x
  370,036,176 = $68.2bn, headed COMPUTATION — NOT A CLEARANCE: 0.5-0.8% business yield against a
  5.29% sovereign; Q6 arms nothing.
- Work order: none. UNKNOWABLE: none.

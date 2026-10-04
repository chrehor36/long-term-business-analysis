# Company Run — O'REILLY AUTOMOTIVE, INC. (ORLY) — 2026-09-02
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

**THE BRIEF'S PRE-REGISTRATION, RECORDED BEFORE COMPUTING [E4-26, E3-41].** The operator
states his prior in writing: *"I expect Q2 OUT and I am aware that expectation is now
thirteen names old… Argue against me."* Five specialty retailers have closed at Q2 in this
queue (AEO, NKE, DG, ULTA, DKS). This run is therefore framed to **refute the operator's
prior**, not to confirm it: the distribution-density case is built at full strength in
Q2 BEFORE any test is run against it, and every test that acquits ORLY is reported as an
acquittal. The analyst's own incentive — a sixth Q2 OUT is the cheap answer and the
pattern-consistent one — is the [E4-27] incentive this protocol names.

**Research folder:** `Test Runs/_research 2026-09-02 ORLY/`

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
- rate **5.27 %** · date **2026-09-01** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year constant maturity.** Not FRED; `tools/sources.py` was corrected to the
  Treasury on 2026-09-02 and returns `(5.27, '09/01/2026', 'US Treasury daily par yield curve')`.
- FX: **none required.** ORLY earns in USD. Mexico (112 stores) and Canada (26 stores) are
  **138 of 6,585 stores, 2.1%**; the filer reports **one operating segment**. USD is the
  earnings currency on the filing's own face.

**STAGE 0 — SHARE COUNT READ BY HAND OFF THE 10-Q COVER** *(four names in this project have
been caught on stale counts: LEVI, NKE, DKS, PINS)*:
> *"Indicate the number of shares outstanding of each of the issuer's classes of common stock
> as of the latest practicable date: Common stock, $0.01 par value - **808,960,792** shares
> outstanding as of **August 3, 2026**."* — 10-Q for the quarter ended 2026-06-30, cover page

- **Single class.** No A/B structure (contrast BRK-B). Nasdaq: ORLY.
- **A 15-for-1 forward split completed 2025-06-10**, from the 10-K: *"On June 10, 2025, the
  Company completed a **15-for-1 forward stock split** of our common stock. All share and per
  share information … has been retrospectively adjusted."* The screen's split-invariance rule
  bites hard here: the FY2023 tagged `CommonStockSharesOutstanding` is **59,072,792 pre-split**
  in accession `0000898173-25-000008`, while FY2024 is **862,232,760 post-split** in
  `0000898173-26-000009`. Any series that mixes accessions across 2025-06-10 is off by **15x**.
  All per-share figures below are stated **post-split**.
- price **$86.86** · date **2026-09-02** · *aggregator, flagged — live quote only, operator
  rule 5.* Pre-split equivalent $1,302.90.
- **market cap = 808,960,792 × $86.86 = $70,266M.**

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K, FY ended 2025-12-31, filed 2026-02-27, accession `0000898173-26-000009`**
    (`orly-20251231x10k.htm`)
  - **10-Q, quarter ended 2026-06-30, filed 2026-08-07, accession `0000898173-26-000045`**
  - **DEF 14A, filed 2026-03-27, accession `0000898173-26-000014`**
- figure cross-checked against the filed statement: **operating income FY2025 $3,460,612
  thousand** — XBRL `OperatingIncomeLoss` matches the 10-K's own ten-year Selected Financial
  Data table line "Operating income" at page 30 of the filed document. Second cross-check:
  **shareholders' DEFICIT $(763,352) thousand**, XBRL `StockholdersEquity` against the filed
  balance sheet line "Total shareholders' deficit."
- Ladder rung used: **rung 2, SEC EDGAR primary documents.** No rung blocked.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.**

O'Reilly buys automotive replacement parts from manufacturers and resells them out of 6,585
small shops. It does not fix cars and it does not sell tires — the 10-K says so in terms:
*"We do not sell tires or perform for-fee automotive repairs or installations."* Two customers
buy from the same shelf:

1. **A person whose car is broken (DIY).** $8,766M of FY2025 sales, 49.3%. He wants the right
   part today, and he is not price-shopping a $40 alternator across town while his car sits.
2. **A repair shop whose bay is occupied by a broken car (DIFM / "professional service
   provider").** $8,652M, 48.7%. His economics are the ones that matter. A repair bay bills by
   the hour. A bay holding a car that is waiting on a part bills nothing. So he pays for
   **arrival time**, not for the part.

The gross margin is **51.6%** (FY2025: $9,174M on $17,782M) — which for a reseller of other
people's manufactured goods is the tell that the customer is not buying the part. He is buying
*having the part*. The 48.4 points of cost are the merchandise; the 51.6 points are inventory
that sat somewhere close enough.

So the arithmetic of one store: about **$2.7M of annual sales** (FY2025 sales per
weighted-average store $2,728 thousand) out of **~8,000 sq ft** on a mostly-leased pad,
carrying *"approximately 24,000 SKUs"*, restocked from one of **399 Hub stores** (18,300 sq
ft, 63,000 SKUs, up to ~115,000 in select markets) and one of **32 DCs** (*"over 156,000
SKUs"*, 14.0 million operating square feet). **The cost of the network is the product.**
ORLY's own 10-K states the capital form of this plainly: *"Our dual market strategy requires significant capital, including the capital
expenditures required for our distribution and store networks and working capital needed to
maintain inventory levels necessary for providing products to both the DIY and professional
service provider portions."*

**The float mechanism, which is the real earnings engine and is not in the income statement.**
Accounts payable were **123.9% of inventory** at FY2025 ($7,104M against $5,731M). The
suppliers finance the entire inventory and $1.37bn besides. Inventory turns **1.6x** — this is
deliberately *slow* inventory, because the slow-moving SKU is the whole point — and it is
carried at someone else's expense. That is why a business with negative book equity is not
distressed: the negative equity is a buyback artifact sitting on top of a supplier-funded
working-capital position.

**The scarce input this business controls.** Not the part — every competitor buys the same
part from the same handful of manufacturers. It is **the physical position of inventory
relative to repair bays**: 6,585 stores, **399 Hub stores averaging 18,300 sq ft with 63,000
SKUs (up to ~115,000 in select markets)**, and 30 distribution centres, arranged so a part
can be in a specific bay within the hour. That network was assembled over 68 years and its
replication cost is a real number, not a brand claim.

**Will the fundamentals look broadly the same in ten years?** The mechanism — a car breaks,
somebody needs a specific part fast, someone must hold that part nearby — is as stable as the
US light-vehicle fleet, which turns over across ~15-20 years and is measured in the hundreds
of millions. **The composition of the parts basket is a genuine open question** (electrified
powertrains delete a large share of the maintenance basket) and is taken up at Q2 and Q4 as a
death mechanism, not waved away here. But the *business* — hold parts near bays, charge for
arrival time — is [E3-31]'s *"relatively simple and stable in character."* One segment, one
country to 97.9%, no financial subsidiary, no equity-method stakes, no reinsurance, no
percentage-of-completion. Revenue is cash on the day.

**A ten-year test of the understanding [E4-46].** The 10-K's own ten-year table is published
in the filing and I can read the whole business off it in five minutes: sales, stores, square
footage, sales per store, sales per square foot, comparable sales, OCF, capex, total debt,
equity. This is not a five-month business.

- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**CLASS: NARROW, and WIDENING relative to every peer that files. VERDICT: IN.**
**This breaks a run of thirteen consecutive Q2 closures and five consecutive specialty-retail
closures. The reasons are set out below, and so is the strongest fact against them.**

- Needed or desired **[x]** · no close substitute **[x]** *(qualified — see criterion 2)* ·
  not price-regulated **[x]**

### The case FOR, built at full strength BEFORE it is tested [E4-51]

The operator's brief asked for this and the framework requires it: *"I'm not entitled to have
an opinion unless I can state the arguments against my position better than the people who
are in opposition."* Here the position under attack is the operator's own stated prior.

1. **The product is arrival time, and arrival time is a physical asset.** 6,585 stores, **399
   Hub stores**, **32 DCs of 14.0 million operating square feet**. From the 10-K: *"More than
   95% of our stores receive **multiple same-day deliveries and deliveries on weekends** of
   hard to find parts from our DCs and Hub stores."* DCs run *"five-night-a-week delivery,
   primarily via a **Company-owned fleet**"*, and metro stores get *"multiple daily
   deliveries… many of which receive this service **seven days per week**."* An alternator
   that arrives in thirty minutes is not the same product as one that arrives tomorrow,
   because the customer's cost is an idle repair bay, not the part.
2. **The attacker's test [E2-45] has already been run, in public, at length, by the strongest
   possible attacker — and the filings record the outcome.** ORLY's own 10-K names
   *"online retailers … (such as Wal-Mart Stores, Inc. and **Amazon.com, Inc.**)"* as
   competitors. Over the decade of that attack: **revenue $8,593M → $17,782M (+107%)**,
   operating margin **19.77% → 19.46%** (−31bp over nine years), and return on unleveraged
   net tangible operating assets **73.4% → 74.6%, RISING.** The attacker's test is not a
   thought experiment here. It is a completed natural experiment and the incumbent won it.
3. **The category's weak player was destroyed, and the share went to the incumbents, not out
   of the channel.** Advance Auto Parts, five years apart, from its own 10-Ks: revenue
   **$10,106M → $8,601M (−14.9%)**, operating margin **+7.42% → −0.50%**, return on
   unleveraged NTOA **23.4% → −2.0%**, operating cash flow **+$970M → −$46M**. If Amazon were
   taking the category, ORLY and AZO would be shrinking with AAP. They are not.
4. **The deflated physical series — this project's sharpest instrument — ACQUITS.** Detail
   below; it is the fourth acquittal (DICK'S, AEO, ULTA, now ORLY) and it is reported as an
   acquittal because that is what it is.
5. **[E2-49] metric-switching DOES NOT FIRE, and the near-miss is instructive.** Detail below.
6. **[E4-37]'s inverse metric — the agony test — passes, and it passes CURRENT.** Detail below.
7. **[E4-23] key-person dependence: none found.** CEO Brad Beckham is a **29-year Team
   Member** who *"began as a Parts Specialist"*; the President, the CFO, the EVP of Store
   Operations and most SVPs are 17-34 year lifers on a stated *"promote from within"*
   policy. The filer records *"**33 consecutive years of record revenues and earnings and
   positive comparable store sales results** since becoming a public company in April of
   1993"* — a span covering several CEOs. The moat does not leave when a person leaves;
   this is the Mayo Clinic side of [E4-23], not the surgeon side.

### [E4-04] — must the moat be CONTINUOUSLY REBUILT, or continuously DEFENDED?

The corpus scopes this itself: what "enduring" excludes is *"the moat whose **basis must be
periodically replaced**"* — rapid-change industries, depleting assets — not moats needing
continuous *defence*, which is prescribed for every moat **[E5-23, E3-49]**. **The test: does
a lapse in spending destroy the structure, or merely narrow it — and does the spending defend
the same advantage, or buy its replacement?**

**ORLY's spending defends the same advantage.** If ORLY stopped opening stores tomorrow, its
6,585 existing locations and 32 DCs would still sit the same distance from the same repair
bays. Real estate position and inventory position do not deplete. This is **not** the Mitsui
Rhodes-Ridge shape (buying a replacement deposit) and it is **not** the fashion-retailer
shape that closed AEO and NKE. **[E4-04] does not exclude ORLY**, and that is a real and
non-obvious finding, not a courtesy.

**Nor is this a surfing run [E3-51].** The wave — an aging US fleet and rising parts
complexity — is real and is named in ORLY's own MD&A, but ORLY is *gaining share inside the
wave while a peer with the same wave drowns*. A wave does not explain AAP.

### [E3-03] CRITERION 2 — the whole question, argued both ways

**AGAINST — and this is the strongest fact against my own conclusion, stated first [E4-26]:**

> **AutoZone is not a distant competitor. It is a larger, equally profitable, structurally
> identical one, and it sells the identical part.** FY2025: revenue **$18,939M** (larger than
> ORLY's $17,782M), gross margin **52.62%** (HIGHER than ORLY's 51.59%), operating margin
> **19.06%** (31bp below ORLY). Same dual-market strategy, same hub-and-DC architecture, same
> negative-equity buyback machine, same suppliers — Bosch, Denso, Dorman, Gates, Moog, Wix.
> **There is no product differentiation whatsoever.** A repair shop in most US markets holds
> accounts with two or three of ORLY, AZO, NAPA and a regional jobber, and can have any of
> them deliver the same part the same day. On a plain reading of *"is thought by its customers
> to have no close substitute"*, a shop with three same-day suppliers does not think that.

**And the second-strongest, which is empirical:** if distribution density alone were the moat,
**AAP should not have collapsed** — it had ~4,800 stores, a national DC network, a
professional business and the same suppliers, and it still went to a −0.5% operating margin.
Density was necessary and *not sufficient*. What separated ORLY from AAP was execution, which
is [E3-43]'s *"a business, unlike a franchise, can be killed by poor management"* — the
sentence that turns Q3 into a gate.

**FOR — the corpus's own operational tests for criterion 2, which are about conduct, not
structure:**

Criterion 2 is a claim about what customers *think*, and the corpus supplies two ways to read
that off filed conduct rather than off market structure.

**(a) [E4-37], the inverse metric — the agony test.** *"you can almost measure the strength
of a business over time by the agony they go through in determining whether a price increase
can be sustained… it's not a great business when you have to have a prayer session before you
raise your prices a penny."*

ORLY's FY2025 MD&A, verbatim:
> *"Average ticket values benefited from increases in average selling prices on a same-SKU
> basis … driven by increases in acquisition costs of inventory, **principally resulting from
> increased tariffs, which were passed on in selling prices.**"*

and the Inflation section:
> *"To the extent our acquisition costs increased due to price increases industry wide, we
> have typically been able to **pass along these increased costs through higher retail
> prices** … As a result, we do not believe inflation has had a material adverse effect on
> our operations."*

**Outcome, from the filings:** gross margin **51.4% in Q2 2026 against 51.4% a year earlier**;
**51.5% for the half against 51.4%**; and comparable store sales **ACCELERATING — +4.7%
(FY2025) → +7.0% (H1 2026) → +6.0% (Q2 2026)**. A full tariff pass-through with margin held
and comps accelerating is yawn-pricing. **There is no prayer session in this filing.**
Contrast the finding that closed DKS eight days ago: an 8-K conceding conditions *"became
increasingly promotional, and we took action to remain competitively priced."* **The word
"promotional" does not appear in ORLY's 10-Q at all.**

**(b) [E2-44], the two-characteristic test.** *"can it raise prices even when product demand
is flat and capacity is not fully utilized"*, and *"grow dollar volume with only minor
additional investment of capital"*?
- **Characteristic (a): PASSES, and strongly.** Product demand in UNITS is not flat — it is
  **falling** on half the business (DIY transaction counts negative in every non-pandemic
  year disclosed, below) — and ORLY raised prices into it without losing margin or share.
  That is the harder version of the test.
- **Characteristic (b): FAILS.** Capex went **$443M (2021) → $1,169M (2025)**, 2.29x D&A,
  while operating cash flow **FELL $3,207M → $2,762M**. Dollar volume grew +33.4% and owner
  earnings fell **−43.1%**. This is carried to Q4, where it is decisive, and it is the reason
  the class below is NARROW rather than WIDE.

**RESOLUTION.** Criterion 2 is **satisfied, at NARROW width, on conduct evidence, with the
AutoZone substitute recorded as a permanent cap on the class.** The corpus does not require
monopoly for franchise status — [E5-28] reserves near-monopoly for the *untapped pricing
power* class **[E3-33]**, not for [E3-03] — and the canonical franchise competed with Pepsi
throughout. What criterion 2 asks is whether customers behave as though a close substitute
exists. **The filed conduct says they do not: full cost pass-through, stable gross margin,
accelerating comps, rising professional transaction counts, and share taken from a
same-density competitor.**

### THE ATTACKER'S TEST [E2-45] — WHAT ACTUALLY HAPPENED, ESTABLISHED EMPIRICALLY

The brief asked for this the way the ULTA run established Sephora's 1,149 Kohl's shops and
the DG run established Dollar Tree's $6.34bn Family Dollar write-off. Research file:
`_research 2026-09-02 ORLY/amazon_and_channel.md`.

**1. Amazon's installer push is a TIRE business, and ORLY does not sell tires.** The dated
record: Monro pilot **July 2018** (52 stores, Baltimore), expanded **October 2018** (~400),
completed **July 2020** (1,200+ stores, 32 states); Pep Boys national **November 2018**
(~1,000 locations); Sears Auto the same year. **Scope was tires, later plus batteries and
brakes — never the general hard-parts catalogue**, and **no 2025-2026 expansion announcement
was found** (recorded as a GAP, not as an absence). Against this, ORLY's 10-K states flatly:
*"We do not sell tires or perform for-fee automotive repairs or installations."* **The
attack landed in an adjacent category.**

**2. The online-native pure-play is the natural experiment, and it is losing.**
CarParts.com (PRTS, CIK 0001378950), from its own filings: revenue peaked **FY2023 $675.7M**,
then $588.8M, then **$547.5M (FY2025) — −19% from peak**; net loss widened to **$(50.4)M**;
Nasdaq bid-price deficiency letter **2025-06-13**; moved to the Capital Market **2025-12-15**;
**1-for-10 reverse split effective 2026-05-25**; market capitalisation **$64M on $548M of
revenue**. Its own 10-K names Amazon as **both a competitor and a sales channel**. *(No
going-concern language — zero hits. Recorded, so this is not overstated.)*

**3. Both of Amazon's named national installers changed hands, and the parts business inside
them was liquidated.** Pep Boys: **$1.03bn** of equity paid by Icahn in **February 2016** for
*"more than 800 locations"*; sold to Mavis for **$700M cash, announced 2026-07-21, closed
2026-08-20**, at *"nearly 800"* centres. **Store count roughly flat; the format completely
changed — it exited retail parts, and leased 109 California properties to Advance Auto Parts
in 2021.** Icahn's parts distributor **Auto Plus filed for bankruptcy in January 2023**, and
Icahn Enterprises **exited Aftermarket Parts entirely in Q1 2025.**
*(Brief correction carried: the Mavis/Pep Boys transaction is **2026**, not 2021.)*

**What the decade of attack produced: the attacker's installer partners exited the parts
business, the online-native pure-play lost 19% of its revenue and did a reverse split, the
weakest incumbent went to a negative operating margin — and ORLY doubled revenue while
raising its return on operating assets.** That is as complete a run of [E2-45] as this
project has been able to observe on any name, and the incumbent won it.

**4. The demand series, which is the check on the other direction.** US vehicle miles
travelled, FHWA Traffic Volume Trends, December issues: **3,147.8bn (2015) → 3,323.8bn
(2025)**, trough 2,829.7bn (2020). **That is +5.6% over ten years — about +0.55% a year.**
Average light-vehicle age, S&P Global Mobility: **12.2 (2022) → 12.5 (2023) → 12.6 (2024) →
12.8 (2025)**; 2015-2021 and 2026 are **GAPs**, and the series is **restated between
releases** (the 2024 release cites 12.4 for 2023 against the 12.5 headline), so it is used
directionally only. **The brief called the aging fleet and miles driven "a real demand
series" and it is — but it is a slow one.** Miles driven grew 0.55%/yr while ORLY's revenue
grew 8.4%/yr. **The growth came from share and from price, not from the road.** That bounds
the Q5 growth case and is carried there.

### THE DEFLATED PHYSICAL SERIES — the DG instrument. **IT DOES NOT CONVICT.**

Built on DG (nominal $273→$270→$273, real **$273→$217**, five straight declines); replicated
on Foot Locker (**−24.7% real**) and UAL (**real PRASM −6.2%**); acquitted DICK'S (**+15%
real**), AEO and ULTA. **Run honestly on ORLY, it acquits — and I report that as the result
even though a conviction would have been the pattern-consistent answer.**

Source: the 10-K's own **ten-year Selected Financial Data table**, accession
`0000898173-26-000009`. Deflator: BLS CPI-U all items, annual averages, **240.007 (2016) →
321.943 (2025)**.

| | 2016 | 2019 | 2021 | 2023 | 2025 | nominal | **REAL (CPI-U)** |
|---|---|---|---|---|---|---|---|
| Sales per wtd-avg **store**, $k | 1,826 | 1,881 | 2,298 | 2,578 | **2,728** | **+49.4%** | **+11.4%** |
| …in 2016 dollars | 1,826 | 1,766 | 2,035 | 2,031 | **2,034** | | +1.20%/yr |
| Sales per wtd-avg **square foot**, $ | 251 | 255 | 307 | 340 | **346** | **+37.8%** | **+2.8%** |
| …in 2016 dollars | 251 | 239 | 272 | 268 | **258** | | +0.30%/yr |

**Deflated instead by the category price index** (BLS CPI-U *motor vehicle parts and
equipment*, SETC, 143.555 → 184.705 — the closer proxy to a units series, since it strips the
price of the actual goods): sales per store **+16.1% real**, per square foot **+7.1% real**.

**Every construction is positive. The instrument does not replicate.** For completeness and
per **[E4-38]** — *"growth-rate presentations can be significantly distorted by a calculated
selection of either initial or terminal dates"* — every base year is published:
- **vs 2016 (10-year):** per store **+11.4%** real, per sq ft **+2.8%** real
- **vs 2019 (pre-pandemic):** per store **+15.2%** real, per sq ft **+7.7%** real
- **vs 2021 (pandemic peak):** per store **−0.1%** real, per sq ft **−5.1%** real

**The honest qualification, and it matters:** real productivity per square foot has fallen in
**6 of the 9 years**, and has fallen in **three of the last four**, from a 2021 real peak of
$272 to $258. **Real sales per store have been flat for four years** ($2,035 in 2021 → $2,034
in 2025). ORLY is not the DG conviction and it is not the DICK'S clean acquittal either — it
is **real growth that stopped in 2021 and has been replaced by store-count growth.** Store
count rose +13.8% over those same four years. That finding is carried into Q4 and Q5, where it
is what the price has to be tested against.

### [E4-55] — THE UNITS SERIES. **ORLY DISCLOSES IT. THE PEERS DO NOT. AND IT IS NEGATIVE.**

**The brief's premise was that ORLY *"historically has NOT split price from volume"* and that
*"if not, that absence is the finding."* THE BRIEF IS WRONG, and the correction is the more
interesting result: ORLY splits ticket from transactions in every 10-K, and its three largest
competitors split neither.**

Occurrence counts, raw filed HTML with tags stripped so a phrase broken across `<span>`
elements cannot produce a false negative:

| Filing | FY | Accession | "average ticket" | "transaction count" |
|---|---|---|---|---|
| **ORLY** `orly-20251231x10k.htm` | 2025 | 0000898173-26-000009 | **4** | **4** |
| AZO `azo-20250830x10k.htm` | 2025 | 0001104659-25-102611 | **0** | **0** |
| AZO `azo-20200829x10k.htm` | 2020 | 0001558370-20-011748 | **0** | **0** |
| AAP `aap-20260103.htm` | 2025 | 0001193125-26-051305 | **0** | **0** |
| AAP `aap-20210102.htm` | 2020 | 0001158449-21-000036 | **0** | **0** |
| GPC `gpc-20251231.htm` | 2025 | 0000040987-26-000003 | **0** | **0** |
| GPC `gpc-20201231.htm` | 2020 | 0000040987-21-000009 | **0** | **0** |

AZO's five-year table decomposes same-store sales by **geography** (domestic / international /
constant currency) and never by units versus price. AAP's only "traffic count" hit is site
selection; its only "units sold" hit is a warranty accrual. **The [E4-55] physical series
cannot be built for AZO, AAP or GPC from their 10-Ks at all.**

**THE ORLY SERIES, read out of nine years of MD&A** (direction is disclosed; magnitude is
not):

| FY | DIY transaction counts | Professional transaction counts | source |
|---|---|---|---|
| 2017 | **NEGATIVE** | **NEGATIVE** | 10-K FY2017 |
| 2019 | **NEGATIVE** | positive (net *"flat for the year"*) | 10-K FY2019 |
| 2020 | positive *(pandemic + stimulus)* | positive *(pandemic + stimulus)* | 10-K FY2020 |
| 2022 | **NEGATIVE** | positive | 10-K FY2022 |
| 2024 | **NEGATIVE** | positive | 10-K FY2024 |
| 2025 | **NEGATIVE** | positive | 10-K FY2025 |
| H1 2026 | **NEGATIVE** | positive | 10-Q 2026-06-30 |

**DIY customer transaction counts have been negative in every year disclosed except the
pandemic. That is 49.3% of revenue with a falling physical unit count.** And ORLY has
published the structural reason, in nearly the same words, since at least FY2019:

> *"These better-engineered, more technically advanced vehicles **require less frequent
> repairs**, as the component parts are more durable and last for longer periods of time. The
> resulting **decrease in repair frequency creates pressure on customer transaction counts**;
> however, when repairs are needed, the cost of replacement parts is, on average, greater,
> which is a benefit to average ticket values."*

**Is this the Precision Steel pattern [E4-55]** — *"pounds fell 69M → 46M while price rises
held dollar revenue level … a serious reverse, not likely to disappear in some 'bounce back'
effect"*? **I judge NO, and the distinction is load-bearing rather than convenient.** Precision
Steel was losing physical volume *to competitors* in a shrinking business, with flat dollar
revenue. ORLY's transaction count falls because **each vehicle needs fewer repairs**, while
the value per repair rises — and the deflated *dollar* series per store is **up 11.4% real**,
not flat. Volume lost to a rival and volume lost to product durability are different
mechanisms with different endings. **But the durability trend is permanent, one-directional,
and disclosed by the company itself, and it is the named death mechanism at Q4.**

**The DIY/DIFM split makes the same point in dollars** (10-K revenue disaggregation note):

| | FY2023 | FY2024 | FY2025 | 2y nominal | **2y REAL (CPI-U)** |
|---|---|---|---|---|---|
| **DIY** | $8,248M | $8,473M | $8,766M (49.3%) | +6.27% | **+0.58%** |
| **Professional (DIFM)** | $7,246M | $7,836M | $8,652M (48.7%) | **+19.40%** | **+13.01%** |

**ORLY is one growing business bolted to one stagnant one.** DIFM is real-terms compounding at
~6%/yr and crossed 48.7% of sales; DIY is flat in real terms with falling units. The brief's
claim that *"DIFM is roughly half the business"* is confirmed exactly — and the half that is
growing is the half where the density argument applies.

### THE COMPETITOR ROW — required [E3-28]

**Metric definition, stated once and applied identically to all four** *(CONVENTION — the
AEO / NKE / ULTA / DKS attacker metric, rebuilt from the same XBRL tags for every company)*:
**Net tangible operating assets = total assets − cash − short-term investments − goodwill −
other intangibles − operating-lease ROU assets − (total current liabilities − current debt −
current operating-lease liabilities); Return = operating income ÷ that denominator.**

| | **ORLY** | **AZO** | **AAP** | **GPC (NAPA)** |
|---|---|---|---|---|
| FY end | 2025-12-31 | 2025-08-30 | 2026-01-03 | 2025-12-31 |
| accession | `-26-000009` | `0001104659-25-102611` | `0001193125-26-051305` | `0000040987-26-000003` |
| Revenue, $M | 17,782 | **18,939** | 8,601 | **24,300** |
| Gross margin | 51.59% | **52.62% — 1st** | 43.40% | 36.79% |
| Operating margin | **19.46% — 1st** | 19.06% | **(0.50)% — last** | 7.36% |
| **Return on unleveraged NTOA** | **74.6% — 1st** | 56.8% | **(2.0)% — last** | 43.1% |
| **Same, five years earlier** | 73.4% | 64.9% | 23.4% | 50.1% |
| **DIRECTION [E4-32]** | **+1.2pt — the ONLY riser** | **−8.1pt** | **−25.4pt** | **−7.0pt** |
| *…but vs ORLY's own FY2022 peak* | ***−30.3pt*** *(see the [E4-38] correction below)* | | | |
| Same, operating leases capitalised in | **49.2% — 1st** | 37.8% | (1.0)% | 28.7% |
| Owner earnings (OCF−SBC−capex), $M | 1,558 | 1,790 | **(334)** | 372 |
| OE as % of revenue | 8.76% | **9.45% — 1st** | (3.88)% | 1.53% |
| Book equity, $M | **(763)** | **(3,414)** | 2,198 | 4,423 |
| capex / D&A | **2.29** | 2.16 | 0.93 | 0.87 |

- **Peers named: 4 of the 4 national chains that file with the SEC.** Buffett says eight; **the
  industry does not have eight scale competitors that file.** The remaining competition ORLY
  names — regional chains, independent jobber stores, automobile dealers, Wal-Mart and Amazon —
  is either private, or does not report auto parts as a segment. That is stated, not stretched:
  the row is complete for every SEC-registered national competitor, so the class is **NOT
  PROVISIONAL**. GPC's operating income is **CONSTRUCTED as gross profit less SG&A** because
  GPC's income statement presents no operating-income subtotal and tags none; flagged here.
- **What the negative equity does to the metric, since the brief rightly warned about it.**
  The ULTA run correctly discounted BBWI's 78.7% sitting on −$1,281M of equity. **That
  correction does not apply here, and the reason is in the denominator's construction.** NTOA
  subtracts cash and non-interest-bearing current liabilities from assets; it does **not**
  subtract debt, and debt does not enter it. ORLY's 74.6% is computed on a **$4,637M operating
  asset base**, not on a −$763M equity base, so buyback-driven negative equity cannot inflate
  it. **[E2-43] chose this denominator for exactly this reason** — *"the best guide to the
  economic attractiveness of the operation"*. AZO carries a **four-and-a-half-times larger**
  equity deficit (−$3,414M) and scores **18 points LOWER**, which is the direct demonstration
  that the metric is not reading leverage.
- **The real distortion in this metric is not leverage — it is supplier financing, and it
  should be named.** ORLY's accounts payable are **123.9% of inventory** ($7,104M against
  $5,731M): the suppliers fund the entire inventory and $1.37bn besides. Because the
  denominator subtracts current liabilities, that financing shrinks it and lifts the return.
  This is genuine — it is capital the owners do not supply — but it is a **negotiated position
  that can reverse**, and it has been *increasing*: AP/inventory was **105.7% in 2016** and
  **114.5% in 2020**. A meaningful share of the improvement in this metric over the decade is
  suppliers extending terms, not stores getting better. Carried to Q4 as a working-capital
  exposure.
- **Untapped pricing power [E3-33]: NO, and the claim is not made.** [E5-28] scopes the class
  to *"a monopoly or a near monopoly"*; a four-player national market with private jobbers is
  not that. ORLY prices to pass costs through, not below what it could charge.
- **[E3-61]'s limit on the row, stated:** *"In some businesses, the participants behave like a
  demented Kellogg. In other businesses, they don't … I think you'd have to know the people
  involved."* The row shows ORLY 1st and rising and AAP last and collapsed. It **cannot** show
  whether AZO will start a price war, and nothing here forecasts that it will not.

### [E2-49] METRIC-SWITCHING — **DOES NOT FIRE. This is the sharpest single point for ORLY.**

*"Yardsticks seldom are discarded while yielding favorable readings. But when results
deteriorate, most managers favor disposition of the yardstick rather than disposition of the
manager"* — demand *"pre-set, long-lived and small bullseyes."*

This test has fired on **HD** (sales per retail square foot withdrawn after three declines),
**QCOM** (MSM units withdrawn after a 32.7% fall), **ULTA** (three switches in one year) and
**DKS** (net sales per square foot dropped from Item 6 after six declines).

**Every operating and financial metric ORLY published in its FY2020 10-K is still published in
its FY2025 10-K.** Compared line by line across the two Selected Financial Data tables
(`0000898173-21-000012` vs `0000898173-26-000009`): comparable store sales %, sales, gross
profit, operating income, net income, EPS basic and diluted, total assets, total debt,
shareholders' equity/deficit, inventory turnover, accounts-payable-to-inventory, cash from
operations, capital expenditures, free cash flow, Team Members, total store count, domestic
store count, Mexico store count, store square footage, **sales per weighted-average store**,
and **sales per weighted-average square foot**. Nothing dropped; Canada store count added in
2024 when Canada was entered.

**ORLY has continued to publish sales per weighted-average square foot through the exact
period in which it fell in real terms in three of four years — the identical metric HD
withdrew after three declines and DKS dropped after six.** Under [E2-49] that is the candor
case, not the flag.

**The one near-miss, recorded rather than buried:** the FY2025 10-K contains **"Non-GAAP
EBITDAR"** and **"Non-GAAP adjusted debt"**. Read in place, these are **the covenant
calculation required by the Credit Agreement** (minimum fixed-charge coverage 2.50:1.00,
maximum leverage 3.50:1.00), presented in the *Debt Covenants* section, **reconciled line by
line from GAAP net income**, with the filer's own limitation language: *"Material limitations
of these non-GAAP measures are that such measures do not reflect actual GAAP amounts. We
compensate for such limitations by presenting … a reconciliation to the most directly
comparable GAAP measures."* The same disclosure appears in the FY2020 10-K, so there is no
switch. **[E4-29] is about *trumpeting* EBITDA as though depreciation were not an expense.
ORLY neither headlines it nor pays on it, and its income statement leads with GAAP operating
income.** The flag is recorded as NOT FIRING, and the distinction is stated so a later reader
can disagree with it on the evidence.

### Class and verdict

- **Primary moat metric, filing-sourced, and its trend: return on unleveraged net tangible
  operating assets, 73.4% (FY2020) → 74.6% (FY2025) — 1st of four and the only one rising**,
  against AZO −8.1pt, GPC −7.0pt and AAP −25.4pt. **[E4-32]: direction outranks existence.**

**[E4-38] CORRECTION TO THE LINE ABOVE, MADE AGAINST MY OWN FINDING.** *"growth-rate
presentations can be significantly distorted by a calculated selection of either initial or
terminal dates."* The five-year peer window starts at **FY2020, which is a pandemic-inflated
base for this industry**, and reading ORLY as "the only riser" off that base flatters it. The
full ten-year series, built from the same tags, says something different and it is published
here in full rather than summarised:

| FY | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Return on unleveraged NTOA** | 59.3% | 56.0% | 56.0% | 52.5% | 73.4% | 99.1% | **104.9%** | 99.1% | 90.1% | **74.6%** |
| Same, operating leases capitalised in | 59.3% | 56.0% | 56.0% | 34.4% | 45.7% | 59.2% | **60.0%** | 58.8% | 54.8% | **49.2%** |

**The peak was FY2022 at 104.9%, and the metric has now fallen for three consecutive years —
104.9% → 99.1% → 90.1% → 74.6%, a 30.3-point decline.** Against 2016 it is still up 15.3
points; against the peak it is down by more than the entire gap between ORLY and AutoZone.
**The peer row is still valid** — the same base year was used for every company, and every
peer fell further over the identical window — but "the only one rising" is a statement about
a window, and the absolute trend is DOWN.

**The mechanism, from the same series: the denominator is growing far faster than the
numerator.** NTOA **$2,816M (2022) → $4,637M (2025), +64.7%**, driven by inventory ($4,359M →
$5,731M) and the capex surge, while operating income grew only **+17.1%**. The incremental
return on the capital added over those three years is **507 / 1,821 = 27.8%** — still a good
number, and squarely [E4-43]'s *good* class rather than the *great* class, but a quarter of
the average it is diluting. **This is [E2-44] characteristic (b) failing, measured a second
and independent way**, and it is the reason the class is NARROW and the reason Q4 will matter
more than Q2 on this name.
- **Class: [x] NARROW · Direction: WIDENING relative to peers, NARROWING in absolute
  productivity.** Both halves are true and the run refuses to report only the flattering one:
  ORLY is taking share and raising returns *while* its own real sales per square foot have
  fallen from the 2021 peak and its DIY unit counts fall every year.
- **NOT WIDE**, for two filed reasons: AutoZone is a structurally identical competitor with a
  higher gross margin, and **[E2-44] characteristic (b) fails outright** — dollar volume is no
  longer growing on minor additional capital.
- **VERDICT: [x] IN**

**What would have made this OUT, so the standard is legible:** a promotional-pricing
concession of the DKS kind; gross margin erosion; the deflated series replicating the DG
pattern; a dropped yardstick; or professional transaction counts turning negative. **None of
those is present, and three of them were specifically looked for.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**VERDICT: IN — no disqualifier found. One live CAPITAL-ALLOCATION FLAG and one live
PROJECTIONS FLAG, both quantified below. IN never promotes.**

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- **[x] Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]** — *no; marketable security, exit at will*
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]** — *no; see below*

**CASE DECLARED: Q3 IS A BINARY GATE, and no price compensates.** The reason is not a
judgment about these managers; it is a filed fact about this industry. **[E3-43]:**
*"franchises can tolerate mis-management… a business, unlike a franchise, **can be killed by
poor management**."* Q2 found the class NARROW rather than WIDE, and the evidence that forced
that was **Advance Auto Parts**: the same national store network, the same DCs, the same
suppliers, the same aging fleet — and **operating margin +7.42% → −0.50% and return on
unleveraged NTOA 23.4% → −2.0% in five years.** A business in which a peer with an
equivalent asset base can be driven to a negative operating margin by execution alone is a
have-to-be-smart-every-day business. **The product is undifferentiated and the differentiation
is service, delivered by 93,072 people across 6,585 buildings, every day.** That is [E2-70]'s
magnification condition in a retail form.

**On leverage, declared and quantified rather than screened** *(there is no ratio ceiling in
this framework and the corpus supplies none)*: total debt **$6,017M** against operating income
of **$3,461M** and OCF of **$2,762M**; the filer's own covenant computations give a
**consolidated leverage ratio of 1.92x** (limit 3.50x) and a **fixed-charge coverage ratio of
6.08x** (minimum 2.50x). **Book equity is −$763M, but that is a buyback artifact, not
gearing** — the negative number is repurchased stock charged against retained earnings, and
the operating asset base is a positive $4,637M. The [E3-29] condition is about errors in
*assets* destroying *equity* at 20:1 gearing; that is not this balance sheet. **Not ticked —
and Q3 is a gate anyway on the first criterion.**

**Honesty — binary, permanent, filings-based [E5-16].** *"understanding about business
mistakes; tolerance for personal misconduct is zero."* Each matter dated to when it became
PUBLIC:
- **No disqualifying matter found.** Item 3 Legal Proceedings, FY2025 10-K, in full: *"The
  Company is currently involved in **litigation incidental to the ordinary conduct** of the
  Company's business."* Plus ordinary-course motor-vehicle-accident litigation from operating
  a large delivery fleet, named in Item 1A.
- **No restatement, no material weakness, no clawback.** The FY2025 10-K cover-page
  error-correction and incentive-recovery checkboxes are both **unchecked**; the auditor's
  internal-control opinion is unqualified.
- **Per [E5-17] and [E5-26], this is the ABSENCE OF FOUND DISQUALIFIERS, not a finding that
  these managers are honest.** *"Sincerity and empathy can easily be faked"*, and the Sokol
  calibration is that a decade of strong record preceded the failure.

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30].** *An open list. Each is a prompt to READ,
never a verdict.*

- [ ] **weak accounting — NOT FIRING.** Stock compensation is expensed ($35.1M). **No pension
      plan** — the profit-sharing plan is defined-contribution, so there is no discount-rate or
      return assumption to be fanciful about. Inventory is on **LIFO**, the conservative
      election, and the filer discloses the gap: *"The replacement cost of inventory was
      **$6.25 billion** and $5.32 billion as of December 31, 2025 and 2024"* against a $5.73bn
      carrying value — i.e. it tells you the number that would make it look better.
- [ ] **unintelligible footnotes — NOT FIRING.** 20 notes, plain English, no structured
      entities of consequence (five tax-credit VIEs, maximum exposure **$12.8M**, equity method,
      disclosed).
- **[x] trumpeted earnings projections / growth targets — FIRING. This is a real flag and it
      is the one that would matter if the culture ever cracked.** ORLY issues **full-year
      guidance on nine lines** — comparable store sales, total revenue, gross margin, operating
      margin, effective tax rate, diluted EPS, operating cash flow, capital expenditures and
      free cash flow — and **revises it intra-year**. **[E5-30]:** *"once you start it, it's all
      over. You can't quit… **And forecasting earnings, I can't imagine anything more
      destructive.**"* And the streak language compounds it: the filer advertises **"33
      consecutive years of record revenues and earnings and positive comparable store sales."*
      A company 33 years into an unbroken streak has an enormous standing incentive not to break
      it in year 34 **[E4-27]**. **Recorded as a live flag, not as a finding of manipulation.**
- [ ] **serial share issuance [E5-15] — NOT FIRING; the reverse.** Shares outstanding are down
      **61.8%** since 2010 on a split-adjusted basis. Dilution from options and the ESPP is
      real but small — SBC is **0.20% of revenue**.
- [ ] **EBITDA / adjusted-earnings promotion [E4-29] — NOT FIRING.** Adjudicated in full at Q2:
      "Non-GAAP EBITDAR" and "Non-GAAP adjusted debt" appear only as the **Credit Agreement
      covenant computation**, reconciled line by line from GAAP net income, with the filer's own
      limitation language, and present identically in FY2020. **The earnings release leads with
      GAAP operating income and GAAP EPS, and the incentive plan pays on GAAP operating income,
      not on EBITDA** — contrast UAL, whose 2025 pay metric was switched to *Adjusted EBITDAR
      Margin*, and DKS, which paid on *Adjusted Non-GAAP EBT*. **There is no adjusted-EPS
      measure anywhere in this filing** and the word "restructuring" appears **once**, in
      boilerplate. **[E2-57]'s "except for" is absent from the lexicon.**
- **[~] filed-figure tells [E4-30] — the cash-tax tell RUNS THE OPPOSITE WAY; the smoothness
      tell is noted.** Income taxes paid net, as a share of reported pretax income — the only
      three years the filer discloses, ASU 2023-09 having required the table from FY2025 with
      comparatives:

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Cash taxes paid, net | $315.1M | $640.4M | $1,067.5M |
| Pretax income | $3,004.8M | $3,045.1M | $3,240.2M |
| **Cash tax / pretax** | **10.49%** | **21.03%** | **32.95%** |

**[E4-30]'s tell is cash taxes FALLING as a share of reported pretax income** — *"This plainly
increased their chances of attracting undesired questions."* **ORLY's has TRIPLED.** The 2023
trough coincides with the capex step from $563M to $1,006M and is consistent with accelerated
tax depreciation reversing out across 2024-2025; the tax-credit VIEs are far too small to
explain it ($0.5M of credits recognised in 2023). **Stated as a limit: only three years are
disclosed, so no longer series can be built, and this is a weak read in both directions.**
On smoothness — 33 consecutive years of record earnings is a smooth *reported* series, but the
underlying cash is not smooth at all: **OCF fell 14.0% in 2025 and owner earnings fell 43.1%
from 2021.** The smoothing, such as it is, sits between cash and earnings, and Q4 is where
that is priced.

**STEP 3 — THE PRIMARY TEST [E2-01].** *"the achievement of a high earnings rate on equity
capital employed (without undue leverage, accounting gimmickry, etc.) and not the achievement
of consistent gains in earnings per share."*

**Equity capital employed is NEGATIVE (−$763M), so the ratio as literally written is
meaningless — it would return −332%.** The corpus scopes its own test for exactly this case:
**[E2-47]** carves out unusual debt-equity ratios, and **[E2-43]** directs that for
acquisitive or leveraged filers the denominator is **unleveraged net tangible assets** —
*"the best guide to the economic attractiveness of the operation"*. That denominator is used,
and the goodwill wedge ($948M, 5.7% of assets, from small bolt-ons) is reported separately
rather than hidden in book equity.

**Years used: ten, FY2016-FY2025.** The series is published in full at Q2 above: **59.3, 56.0,
56.0, 52.5, 73.4, 99.1, 104.9, 99.1, 90.1, 74.6%.** **[E2-01] passes on level and fails on
direction** — a decade mean near 76% is a very high earnings rate on capital employed, and the
last three years are three consecutive declines from the peak.

**And note what [E2-01] was written in opposition to.** ORLY's *EPS* series is smooth and
rising — $0.72 → $2.97, up in all ten years, +10% in FY2025. **The EPS series is the flattered
one**, because the denominator is bought back at ~$2.1-3.1bn a year. Net income rose **6%** in
FY2025 while diluted EPS rose **10%**; the 4-point wedge is repurchase, not operations.
**[E2-01] exists to make the run look at the first number and not the second, and on the first
number the trend is down.**

**The half-owner test [E2-26]** — *"the business facts that we would want to know if our
positions were reversed"*: **PASSES, and better than most names in this queue.**
- It publishes **sales per weighted-average square foot** through years in which that number
  fell in real terms — the metric HD withdrew after three declines.
- It publishes the **units-versus-price decomposition** of comps that **none of AZO, AAP or
  GPC publishes**, including the unflattering half (*"a decrease in transaction counts for DIY
  customers"*), every year.
- It states the **structural headwind against its own business** in its own MD&A and has
  restated it for at least seven years: *"better-engineered, more technically advanced vehicles
  **require less frequent repairs** … The resulting **decrease in repair frequency creates
  pressure on customer transaction counts**."*
- It discloses **LIFO replacement cost** ($6.25bn vs $5.73bn carrying), which makes the balance
  sheet look worse than it is.
- **[E3-48] on the guidance record — pulled and set against outturn, as the corpus requires.**
  FY2025 guidance issued 2025-02-05 (8-K exhibit 99.1, accession `0000898173-25-000005`)
  against FY2025 actual:

| FY2025 | guided (2025-02-05) | actual | outcome |
|---|---|---|---|
| Comparable store sales | 2.0% – 4.0% | **4.7%** | **beat the top** |
| Total revenue | $17.4 – 17.7bn | **$17.78bn** | **beat the top** |
| Gross margin | 51.2% – 51.7% | 51.6% | in range |
| Operating margin | 19.2% – 19.7% | 19.5% | in range |
| Diluted EPS *(split-adj)* | $2.84 – $2.87 | **$2.97** | **beat the top** |
| **Operating cash flow** | **$2.8 – 3.2bn** | **$2.762bn** | **MISSED the bottom** |
| Capital expenditures | $1.2 – 1.3bn | $1.169bn | below (favourable) |
| **Free cash flow** | **$1.6 – 1.9bn** | **$1.563bn** | **MISSED the bottom** |

**ORLY beat its own guidance on every income-statement line and missed it on both cash-flow
lines.** That is the shape of this whole company in one table, it comes from management's own
published numbers, and **it is the single most useful thing the projections flag produced.**
And the candor read is genuinely good: on the prior year the CEO wrote, in the earnings
release, *"**While our 2024 results were below our expectations entering the year**"* — a
company managing the narrative does not put that sentence in the first paragraph.

**The institutional imperative — score all four [E2-30].** *Not a fraud test: "institutional
dynamics, not venality or stupidity."*
- [ ] **resists any change in current direction — NO.** Entered Mexico (2019, Mayasa), Canada
      (2024, Vast Auto), built OReillyPro.com and a professional mobile app, relocated the
      Atlanta DC and opened a greenfield Virginia DC.
- **[x] projects/acquisitions materialise to soak up available funds — FIRING, and it is the
      most substantive imperative finding.** **Capital expenditures went $443M (2021) → $563M
      → $1,006M → $1,023M → $1,169M (2025), and are GUIDED to $1.3-1.4bn for 2026** — against
      D&A of $511M, i.e. **2.5-2.7x depreciation.** Over the same span operating cash flow
      *fell* from $3,207M to $2,762M. The distribution build is a real project with a real
      rationale, and the incremental return on the capital added since 2022 is a respectable
      27.8% — **but the pattern is exactly [E2-30](2), and the run records it as such rather
      than accepting the strategic rationale at face value.** This is carried to Q4 as the (c)
      judgment and it is where this name is actually decided.
- [ ] **staff studies produced to justify the leader's craving — no evidence found.** No
      consultant-led programme, no banker-led M&A; acquisitions are jobber-store bolt-ons.
      **[E3-58]'s outsourced-allocation flag does not fire.**
- **[x] peer behaviour mindlessly imitated — FIRING, mildly, and it should be named.** The
      negative-equity, buy-back-everything capital structure is **AutoZone's invention**, run
      by AZO since the late 1990s, and ORLY adopted it wholesale — **both companies now carry
      negative book equity built the same way** (ORLY −$763M, AZO −$3,414M). The imitation has
      worked spectacularly to date. It is recorded because [E2-30](4) is about the *mechanism*
      of the decision, not its outcome, and because a strategy adopted by imitation is
      typically abandoned late.

### CAPITAL ALLOCATION — THE BUYBACK, AS A MAIN EVENT [E5-08]

**The record, from 10-K Note 11 and 10-Q Note 9 — this is one of the most complete repurchase
records this project has read.**

> *"The Company has repurchased a total of **1.5 billion shares** of its common stock under its
> share repurchase program since the inception of the program in January of 2011 and through
> **August 7, 2026**, at an **average price of $20.33**, for a total aggregate investment of
> **$30.4 billion**."* — 10-Q, quarter ended 2026-06-30, accession `0000898173-26-000045`

Shares outstanding, split-adjusted: **2,115,383,160 (FY2010) → 808,960,792 (2026-08-03) =
−61.8%.** Cumulative authorisation **$31.8bn**, raised by $2.0bn three times
(2024-11-22, 2025-11-18, **2026-06-01**). *(That June 2026 board resolution is the XBRL context
`2026-06-01` — a buyback authorisation, not the stock split, which was 2025-06-10.)*

**THE TRANCHE RECORD — because [E5-24] says *"what is smart at one price is dumb at another"***
*(net shares retired are derived from year-end counts and therefore net of option/ESPP
issuance; the FY2024, FY2025 and 2026 average prices are the filer's own disclosed figures)*:

| period | $ invested | avg price paid | vs today's $86.86 |
|---|---|---|---|
| **Whole program, Jan 2011 → 2026-08-07** | **$30,400M** | **$20.33** | **−76.6%** |
| FY2024 | $2,076.5M | **$71.50** | −17.7% |
| FY2025 | $2,096.8M | **$92.26** | **+6.2%** |
| Jan 1 → Feb 27, 2026 | $436.3M | **$93.61** | **+7.8%** |
| **H1 2026 (six months)** | **$2,432.8M** | **$91.17** | **+5.0%** |
| Q2 2026 alone | $1,509.9M | $90.40 | +4.1% |
| Jul 1 → Aug 7, 2026 | $658.5M | $87.01 | +0.2% |

**(1) Ample funds for operations and liquidity? — YES, on the filed figures.** OCF $2,762M
against capex $1,169M leaves $1,563M of free cash flow; the covenant ratios sit at roughly
half their limits; there is **no current portion of long-term debt** in the FY2025 balance
sheet (verified by footing total current liabilities: 7,103,684 + 297,304 + 119,603 + 240,072
+ 13,957 + 439,907 + 561,294 = **8,775,821**, exactly the filed total, with no debt line in
it). **Condition 1 passes.** *(The near-term maturity picture is tested properly at Q4
[E5-11]; it is not free of issues there.)*

**(2) Repurchases at a MATERIAL DISCOUNT to conservatively calculated intrinsic value?**

**FOR THE PROGRAM AS A WHOLE: emphatically yes, and it is one of the best buyback records in
this project's files.** $30.4bn deployed at an average of **$20.33** against a $86.86 quote —
**4.3x on the money**, 61.8% of the company retired. This is [E2-48]'s superstar tell in its
literal form: *"these champs have made very few deals in recent years, and often have found
**repurchase of their own shares to be the most sensible employment of corporate capital**."*
ORLY has made no acquisition larger than a 23-store bolt-on in fifteen years and has returned
essentially all discretionary capital through repurchase. **The comparison is favourable to
every prior case in this queue:** LOW bought inside its value range; **SHW failed outright**
($10.3bn at $255-345 with no tranche clearing the bond); **CHE spent $1,726.7M above its
range**. ORLY's cumulative record beats all three.

**FOR THE RECENT TRANCHES: NO — and this is a live CAPITAL-ALLOCATION FLAG.**

The conservative value work is at Q5 and is headed **COMPUTATION — NOT A CLEARANCE** until
Q4 closes. Taking only its conservative construction — owner earnings of **$1,539M-$2,598M**
capitalised at the **5.27%** sovereign with **no growth term** — the zero-growth value range is
**$36 to $61 per share**. **Every tranche since FY2024 was executed above the top of that
range**, and the FY2025, Q1-2026 and Q2-2026 tranches were executed at **$92.26, $93.61 and
$90.40** — 50% or more above it.

**And the rate accelerated as the price rose, which is the part that actually fires the flag:**

> **H1 2026 repurchases were $2,432.8M — more, in six months, than the $2,096.8M spent in the
> whole of FY2025 — at the highest average price in the program's history, and 106.8% above
> the $1,176.6M spent in H1 2025.**

[E5-08]'s second condition is not "buy back stock"; it is *"its stock is selling at a
**material discount** to the company's intrinsic business value, conservatively calculated."*
A programme that spends *more* as the price rises is being run to a **dollar budget**, not to a
discount. **[E4-50]** describes the opposite behaviour as correct — *"very aggressively, using
up all cash on hand and also borrowing funds"* — but **the discount does the licensing**, and
here the aggression arrived without it. **[E5-25]** shows what real compliance looks like:
Berkshire published **both conditions as numbers in advance** — the 110%-of-book limit, the
$20bn liquidity floor. **ORLY publishes neither.** It publishes an authorisation dollar amount,
which is a budget, and the disclosure never names a price or value condition at all.

**[E4-31]'s third condition — the register must be adequately informed to estimate value —
PASSES**, and generously: the ten-year table, the units decomposition, the LIFO replacement
cost and the guidance-versus-outturn record are all published.

**THE HUMILITY CLAUSE, and it is not a formality here [E4-13, E5-08]:** *"it is natural for
CEOs to be optimistic about their own businesses. **They also know a whole lot more about them
than I do**"* and *"infractions, even serious ones, are innocent; many CEOs never stop
believing their stock is cheap."* This flag rests entirely on **my own zero-growth
construction**, and a zero-growth construction is a hard test for a company that has grown
revenue at **8.4% a year for a decade** and whose comps accelerated to **+7.0%** in H1 2026.
**At a 3% perpetual growth assumption the same arithmetic puts value comfortably above the
price and the recent tranches back inside the range.** The flag is therefore stated for what it
is: **management's implied valuation requires growth that my Q5 will not underwrite, and one of
us is wrong.** Management has been right about this stock for fifteen years and I have been
looking at it for one day.

**Per the framework, this flag BINDS POSITION SIZE, NEVER THE DISCOUNT RATE.**

**THE GUARDRAIL — checked before writing the verdict.**
- **[x] Confirmed: nothing in this Q3 is being used to promote the name.** The buyback record
  is the best fact in this file and **it does not move the name up.** [E2-37]: *"a textile
  company that allocates capital brilliantly within its industry is a remarkable textile
  company — but not a remarkable business."* **[E3-39]:** *"averaged out, betting on the
  quality of a business is better than betting on the quality of management."* Q5 is priced off
  owner earnings and the sovereign, and not one dollar of the $30.4bn record enters it.
- **[x] Key-person dependence recorded at Q2 as a moat matter, not here as a strength** — and
  it was recorded as ABSENT: a 29-year lifer CEO, promote-from-within, 33 years of results
  across several CEOs. **[E4-23]'s Mayo Clinic side.**
- **[x] Is a great manager the reason to act?** **No, and it must not be.** The franchise is
  intact and there is no excisable cancer to fix **[E2-35, E2-36]** — this is not a turnaround
  and the manager is not the plan.
- **[x] [E3-40] loss of focus — NOT PRESENT.** No hubris acquisition, no diversification away
  from the base business, no adjacent-category adventure. Capital goes to stores, DCs and the
  company's own stock. **[E5-45]'s ABCs** — arrogance, bureaucracy, complacency — are a Q6
  monitoring item and show no current tell.
- **VERDICT: [x] IN**
  *IN = no disqualifier found. **NOT a finding that the managers are honest** — "sincerity and
  empathy can easily be faked" **[E5-17]**; "Charlie and I would not have spotted it"
  **[E5-32]**. **IN never promotes.***

**Two live flags carried forward, neither of them disqualifying and both quantified:**
1. **PROJECTIONS [E4-22, E5-30]** — nine-line annual guidance, revised intra-year, plus a
   33-year advertised streak. The ratchet is the risk, not this year's numbers.
2. **CAPITAL ALLOCATION [E5-08](2)** — $2,432.8M of repurchase in H1 2026 at $91.17, *more in
   six months than in all of FY2025*, at the highest price in the program's history, above the
   top of my own zero-growth range. **Binds position size, never the discount rate.**

**And the flags do NOT converge [E4-52].** The lollapalooza test asks whether several flags
point at one outcome as a reinforcing system. Here they point in **opposite** directions: the
projections flag and the buyback flag both push toward *managing the share price*, but the
disclosure conduct pushes the other way — the units decomposition, the retained square-foot
metric, the LIFO replacement cost, the admitted guidance miss, zero adjusted-EPS, zero
restructuring charges, and cash taxes tripling as a share of pretax. **A management running the
[E3-50] stock-price-targeting playbook does not publish the numbers that make its own results
look worse.** That is why this is IN with flags rather than UNRESEARCHED.

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**VERDICT: IN — it survives. But the owner-earnings series is the worst news in this file,
and it is the reason a name that passed Q2 and Q3 is going to fail on price.**

### OWNER EARNINGS BY YEAR — and the fact that governs the rest of the run

*CONVENTION: owner earnings = operating cash flow − share-based compensation − (c). OCF nets
the working-capital change from one audited line. SBC subtracted in full **[E5-06]** — and it
is trivially small here, **$35.1M, 0.20% of revenue**, so [E3-70]'s market-value objection to
using the accounting charge cannot move the answer.*

| FY | OCF | SBC | capex | D&A | **OE @ capex** | OE @ D&A | yoy |
|---|---|---|---|---|---|---|---|
| 2016 | 1,510,713 | 18,859 | 476,344 | 217,866 | 1,015,510 | 1,273,988 | |
| 2017 | 1,403,687 | 19,401 | 465,940 | 233,845 | 918,346 | 1,150,441 | −9.6% |
| 2018 | 1,727,555 | 20,176 | 504,268 | 258,937 | 1,203,111 | 1,448,442 | +31.0% |
| 2019 | 1,708,479 | 21,921 | 628,057 | 270,875 | 1,058,501 | 1,415,683 | −12.0% |
| 2020 | 2,836,603 | 22,747 | 465,579 | 314,635 | 2,348,277 | 2,499,221 | +121.8% |
| **2021** | 3,207,310 | 24,656 | 442,853 | 328,217 | **2,739,801** | 2,854,437 | +16.7% |
| 2022 | 3,148,250 | 26,458 | 563,342 | 357,933 | 2,558,450 | 2,763,859 | **−6.6%** |
| 2023 | 3,034,084 | 27,511 | 1,006,264 | 409,061 | 2,000,309 | 2,597,512 | **−21.8%** |
| 2024 | 3,049,576 | 28,931 | 1,023,387 | 461,892 | 1,997,258 | 2,558,753 | **−0.2%** |
| **2025** | 2,761,993 | 35,115 | 1,168,815 | 511,230 | **1,558,063** | 2,215,648 | **−22.0%** |
| **TTM to 2026-06-30** | 3,289,439 | 33,815 | 1,133,180 | 537,714 | **2,122,444** | 2,717,910 | *recovering* |

> **From the 2021 peak to FY2025, owner earnings fell 43.1% across FOUR CONSECUTIVE DECLINES,
> while revenue rose 33.4%.** That is the whole of [E2-44] characteristic (b), stated in
> dollars: **the dollar volume grew and the owner earnings did not follow.**

**And the TTM figure partially reverses it — which must be reported and must be discounted.**
Owner earnings for the twelve months to 2026-06-30 are **$2,122M**, back near the four-year
mean, because H1-2026 OCF rose **$527M** year on year. **But net income rose only $112M of
that.** The condensed cash-flow statement attributes the difference to working capital and
timing: *"Other"* **+$455,557k** against **−$227,014k** a year earlier (a $683M swing, and the
condensed statement does not disaggregate it), and *"Income taxes payable"* **−$33,836k**
against **+$314,779k** (a $349M swing the other way). **Roughly $415M of a $527M improvement is
not earnings.** The TTM number is carried in the range as the top end; it is not treated as the
run rate.

### THE (c) JUDGMENT — a disclosed guess, argued rather than defaulted **[E2-23, E3-44, E5-20]**

**Which case is this?** **capex/D&A = 2.29x in FY2025**, and management's own FY2026 guidance is
**capex $1.3-1.4bn against FY2025 D&A of $511M — 2.5x to 2.7x.** On the raw ratio this looks
like the [E5-20] exception class where *"the D&A end … is INVALID."*

**It is NOT the exception class, and the reasons are filed facts:**
1. **The corpus's own test is whether the filer says depreciation understates renewal. ORLY's
   does not, anywhere.** There is no "adjusted capital expenditures" measure — contrast UAL,
   which publishes one that adds back lease-financed aircraft, and whose own filing therefore
   convicted it.
2. **The excess is buying UNITS, not renewing them.** ORLY opened **207 net new stores in
   2025** and guides **225-235 for 2026** on a 6,585 base, and it **OWNS 2,791 of its 6,585
   stores (42.4%)** — from Item 2: *"2,791 stores were owned, 3,728 stores were leased from
   unaffiliated parties, and 66 stores were leased from entities that include one or more of
   our affiliated directors."* Land and buildings for a store that does not yet exist are not
   *"required to fully maintain … its unit volume."* [E2-23]'s (c) is explicitly about
   maintaining unit volume, and ORLY's unit volume is rising 3.4% a year.
3. **The step is datable and attributable.** Capex was $443M in 2021 and $563M in 2022, then
   stepped to $1,006M in 2023 and has stayed there. Store openings rose only ~25% across that
   span. The increment is the distribution build — the **Atlanta DC relocation (Q4 2024)** and
   the **greenfield Virginia DC (2025)**, both named in the earnings releases.

**Against that, three reasons the D&A end is nonetheless too generous:**
1. **[E4-47]:** *"inflation destroys value, but it destroys it very unequally"* — replacement
   capex in current dollars outruns depreciation charged in old dollars. **CPI-U rose 34.1%
   over this window.** ORLY's D&A is on historical cost for a fleet built over decades.
2. **42.4% of the store fleet is owned real estate that must eventually be renewed**, and
   buildings depreciate over 30-40 years — a schedule that flatters near-term D&A.
3. **The ULTA cash-rent ruling applies and cuts BOTH ways here.** ORLY leases **3,794 of 6,585
   stores (57.6%)**, and **rent expense of $490.4M (FY2025)** runs through OCF as cash, so the
   renewal of that 57.6% is already expensed above the owner-earnings line — which *supports*
   the D&A end. But the 42.4% it owns is not.

**THE ASC 842 FINANCE-LEASE CHECK: `"finance lease"` appears ZERO times in the FY2025 10-K.**
ORLY has no finance leases and no finance-lease additions to add back to (c). **Immaterial for
the sixth run running** — the addendum of 2026-09-01 that found this omission in the COST and
HD runs has now been checked on six consecutive names and found nothing.

**THE [E2-23] WORKING-CAPITAL CARVE-OUT APPLIES, AND IT IS THE LIFO CASE EXACTLY.** The source's
own parenthetical: *"businesses following the **LIFO inventory method** usually do not require
additional working capital if unit volume does not change."* **ORLY is on LIFO** — *"Cost has
been determined using the last-in, first-out ('LIFO') method"* — so the increment is not added
on top. It is inside OCF regardless, and it has been a **source** of cash, not a use: accounts
payable at **123.9% of inventory** means suppliers fund the working capital.

**(c), STATED AS THE GUESS THE CORPUS DEMANDS.** Constructing it from the filing: 207 net new
stores in 2025, of which ~42% owned; a blended new-store cost of roughly $1.4-1.7M gives
**~$300-350M of store growth capex**, and a greenfield DC is a further **$100-200M**. That puts
growth capex near **$400-550M** and **maintenance capex near $620-770M** — **above D&A ($511M)
and well below total capex ($1,169M)**. **Call it ~$700M, and label it what it is: a guess,
per [E2-23]'s own "(c) must be a guess."** The band from D&A to total capex is carried anyway,
because the guess does not need to be trusted:

### THE WINDOWS — every one published, none preferred **[E4-25, E2-42, E4-38]**

*"a series of calculations is presented so that you can decide for yourself which period is
most meaningful"* **[E4-38]**. Five years is the corpus default **[E2-42, E1-03]**.

| window | (c) = total capex | (c) = D&A |
|---|---|---|
| **5-year default, 2021-2025 [E2-42]** | **$2,171M** | **$2,598M** |
| 4-year ex-2021 stimulus [E4-41] | $2,029M | $2,534M |
| 3-year, 2023-2025 | $1,852M | $2,457M |
| 10-year, 2016-2025 | $1,740M | $2,078M |
| 8-year ex-2020/21 [E4-41] | **$1,539M** | $1,928M |
| TTM to 2026-06-30 | $2,122M | **$2,718M** |
| FY2025 alone (most recent audited) | $1,558M | $2,216M |

- **Short-window mean** (5y, 2021-2025): **$2,171M @ capex / $2,598M @ D&A**
- **Long-window mean** (10y, 2016-2025): **$1,740M @ capex / $2,078M @ D&A**
- **Spread, conservative end:** the 5-year and 10-year conservative ends differ by **24.8%**
- **COMBINED RANGE (window spread × capex band): $1,539M to $2,718M — a width of 76.6%**
- **[E4-41] normalise DOWN for luck, applied:** **2020 and 2021 are a named favourable
  exogenous break** — pandemic stimulus plus a DIY repair boom, and ORLY's own FY2020 MD&A says
  so: *"as the government stimulus and enhanced unemployment benefits reached consumers, we saw
  a reversal in transaction counts."* Every window excluding those years is shown, and they are
  the lower ones. The mean is not trusted at its 2021-inclusive level.
- **IS THE RANGE TOO WIDE TO REACH A CONCLUSION [E4-25]? NO — and this is the point that lets
  the file proceed.** A 76.6% width would normally close a file. It does not close this one
  **because the entire range sits on one side of the sovereign**: the yield runs **2.19% to
  3.87% against 5.27%**, so the top of the most generous construction is still **140 basis
  points below the bond**. **The capex band does not change the verdict**, and therefore the
  template's UNKNOWABLE trigger does not fire.
- **What the wide spread IS telling me [E5-11]:** not a single distorted year but a **trend** —
  four consecutive declines. **A mean across a monotonically falling series is a historical
  average, not a central estimate of the future**, and that is a Q4 finding in its own right.
  **[E3-55] does not rescue it:** the corpus tolerates volatility *"about which we're extremely
  confident as to the business result"* — See's losing money eight months a year is noise
  around a certain mechanism. **This is not bounce; it is direction**, and the direction has a
  named cause (capex up 164%, OCF down 13.9% from 2021).

### GREAT, GOOD, OR GRUESOME? **[E4-20]**

- [ ] **great** — *"high interest rate that will rise as the years pass"*. **NO.** The return is
  high (74.6% on unleveraged NTOA) but it has **fallen for three consecutive years** from
  104.9%, and the capital requirement is rising, not minor.
- **[x] good** — *"an attractive rate of interest that will be earned also on deposits that are
  added."* **YES, and this is the honest class.** The capital added since FY2022 —
  **$1,821M of net tangible operating assets** — earned an incremental **$507M of operating
  income, a 27.8% incremental return.** **[E4-43] governs and it says the good class PASSES:**
  *"may well prove to be a satisfactory investment … nothing shabby about earning $82 million
  pre-tax on $400 million of net tangible assets"* (20.5%). **[E5-40]** puts *"quite
  satisfactory"* at ~12% on retained capital. ORLY's 27.8% clears both comfortably.
- [ ] **gruesome** — *"grows, eats capital, and earns little."* **NO.** It grows and eats
  capital, but 27.8% incremental is not "little", and [E4-20]'s condition for gruesome is
  explicit: *"unless the cash they consume gets to earn a reasonable return."* It does.

**GOOD, NOT GREAT. And [E4-43] is clear that good ranks below great at Q5 and that is all.**
This matters: the pattern-consistent conclusion would be gruesome, and gruesome would be wrong.

### STAYING POWER — score all three **[E5-11]**

**(1) A large and reliable stream of earnings — PASSES, and strongly.** $2,538M of net income
and $2,762M of OCF; **33 consecutive years of positive comparable store sales**; and the demand
is genuinely counter-cyclical — revenue and operating income both **rose in 2008 and 2009**
($1,628M → $2,327M of gross profit through the financial crisis), because a recession makes
people repair cars rather than replace them.

**(2) Massive liquid assets — FAILS. This is thin and it should be said plainly.** Cash at
2026-06-30 is **$262.2M against $17.4bn of assets — 1.5%.** Working capital is **NEGATIVE
$2,375M** (current assets $7,200M against current liabilities $9,575M). The liquidity is an
**undrawn $2.25bn revolving credit facility maturing March 2030** — which is a **bank line**.
**[E5-39]:** *"We will never be dependent on the kindness of strangers … cash is a lot like
oxygen: you don't notice it 99.9 percent of the time. But if it's absent, it's the only thing
you notice"* — **no bank lines counted, no commercial paper, nothing depended on.** By that
standard, strength (2) does not pass.

**(3) No significant near-term cash requirements — PASSES ONLY BECAUSE THE BUYBACK IS
DISCRETIONARY, and that qualification is the finding.** From the 10-Q debt note at
2026-06-30:

| near-term call | amount |
|---|---|
| Commercial paper (4.065% wtd avg), rolling | **$1,345,000k** |
| 5.750% Senior Notes **due 2026** | **$750,000k** |
| 3.600% Senior Notes due 2027 | $750,000k |
| FY2026 capital expenditure guidance | $1,300,000-1,400,000k |
| **Cash on hand** | **$262,181k** |

**Note the classification: the balance sheet shows ZERO current debt.** The $750M of notes due
2026 and the $1,345M of commercial paper both sit in **long-term debt**, which is permissible
because the revolver gives the intent and ability to refinance long-term — **but it means a
reader taking the current-liabilities line at face value sees no near-term maturity at all.**
This is exactly the necessity [E5-11] says is *"the one most often skipped."*

**Why it still passes:** ORLY generated **$1,563M of free cash flow in FY2025 and $2,122M of
TTM owner earnings** against $750M of 2026 maturities. Free cash flow alone covers the
maturity twice over — **provided the buyback stops.** The buyback is entirely discretionary and
can be halted by a board resolution. **This is the material distinction from UAL**, which
failed (3) outright five days ago with **$18.3bn of contracted calls against $12.2bn of liquid
assets** and *contractual* aircraft commitments that could not be switched off. ORLY's
near-term calls are $2.1bn against $2.8bn of annual operating cash flow. **Different animal.**

**Leverage, named and quantified [E4-16, E3-29, E2-54, E3-52]** — *there is no ratio ceiling in
this framework and the corpus supplies none:*
- Total principal debt **$7,045M** at 2026-06-30, up from **$4,372M** at FY2022 — **+61.2% in
  three and a half years.**
- Interest expense **$235.1M (FY2025)**; **[E2-54]'s coverage test** — *"all interest, both
  payable and accrued, comfortably met out of current cash flow **net of ample capital
  expenditures**"* — gives **$2,762M − $1,169M = $1,593M against $235M, i.e. 6.8x. PASSES
  comfortably**, and this is the test EBITDA-based covenants are built to avoid.
- The filer's own covenant ratios: leverage **1.92x** (limit 3.50x), fixed-charge coverage
  **6.08x** (minimum 2.50x).
- **[E3-52], read the terms not just the quantity:** the largest liability is **$7,385M of
  accounts payable** — covenant-free trade credit with no acceleration clause, the closest
  thing this business has to float. The senior notes are unsecured with light covenants (liens,
  sale-leaseback, merger). **The genuinely fragile piece is the $1,345M of commercial paper**,
  which is not covenanted but is not committed either.
- **Refinancing exposure, quantified:** the **1.750% notes due 2031** and **3.600% notes due
  2027** were issued in a zero-rate era. ORLY's March 2026 issue priced at **5.100%**. Repricing
  those two tranches ($1.25bn) from a ~2.7% blended coupon to ~5.1% costs roughly **$30M a
  year**; repricing the whole $7.0bn stack over time from the current ~3.9% effective rate to
  5.1% costs roughly **$84M a year**. Real, but small against $3.5bn of pre-tax cash flow.

### **[E2-60] — THE DISTRIBUTION TEST. IT FIRES, AND THE ARITHMETIC IS NEARLY EXACT.**

*"restricted earnings are those whose payout costs the business its ability to maintain its
unit volume of sales, its long-term competitive position, **its financial strength** … where
leverage rises to fund the payout, **(c) was understated**, and a company that consistently
distributes restricted earnings is **destined for oblivion**."*

| period | OE @ capex | buybacks | **gap** | total debt | Δ debt |
|---|---|---|---|---|---|
| FY2022 | 2,558,450 | 3,282,265 | **723,815** | 4,371,653 | +544,675 |
| FY2023 | 2,000,309 | 3,151,155 | **1,150,846** | 5,570,125 | +1,198,472 |
| FY2024 | 1,997,258 | 2,076,529 | 79,271 | 5,520,932 | −49,193 |
| FY2025 | 1,558,063 | 2,096,962 | **538,899** | 6,016,904 | +495,972 |
| H1-2026 | 1,469,850 | 2,433,023 | **963,173** | 7,014,543 | +997,639 |
| **cumulative** | | | **$3,456,004k** | | **+$3,187,565k** |

> **Over three and a half years ORLY distributed $3.456 billion more than it earned as an
> owner, and its debt rose by $3.188 billion. The ratio is 0.92 to 1.** The excess
> distribution was borrowed, and the correspondence is close enough that no other explanation
> is needed.

**H1-2026 makes it explicit on the face of the cash-flow statement:** $847,365k of long-term
debt issued and $651,888k of net commercial paper drawn against $500,000k repaid — **$999,253k
of net new borrowing** — in the same six months as **$2,433,023k of repurchases**.

**[E2-60]'s conclusion is that where leverage rises to fund the payout, (c) was understated.**
Applied here it means the honest (c) is nearer the total-capex end than the D&A end — which is
where this run has put it. **It also retroactively qualifies [E5-08] condition 1 at Q3: ample
funds for operations, yes; ample funds for THIS SCALE of repurchase, no — the difference has
been borrowed.**

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**

**[E4-40] first, because it disciplines everything below: model EXPOSURE, not EXPERIENCE.**
*"all of us in the industry made a fundamental underwriting mistake by focusing on experience,
rather than exposure."* ORLY's experience is 33 consecutive years of records. That record is
*"not only useless, but actually dangerous"* as a guide. What follows comes from what the
filing shows the business is exposed to.

**MECHANISM 1 — THE SLOW ONE, AND IT IS THE COMPANY'S OWN DISCLOSURE. Vehicle durability
retires the DIY half.**

ORLY has published the mechanism for at least seven years: *"better-engineered, more
technically advanced vehicles **require less frequent repairs** … The resulting **decrease in
repair frequency creates pressure on customer transaction counts**."* **DIY transaction counts
have been negative in every year disclosed except the pandemic**, and DIY is **$8,766M, 49.3%
of revenue**, growing **+0.58% in real terms over two years — i.e. not at all.**

*Quantified from filed figures:* DIY real growth of zero, held against a store base growing
**3.4% a year**, means real DIY sales per store fall ~3.3% a year. Real sales per square foot
have **already fallen from $272 (2021) to $258 (2025)**. If the offset — average ticket — is
exhausted (and FY2025's ticket gain was explicitly attributed to a **one-time tariff
pass-through**), then real sales per square foot continue at roughly −1.5%/yr, and the 19.5%
operating margin comes under the fixed-cost deleverage that a 3.4%/yr store build makes worse.
**Outcome: not death, but the permanent end of real per-store growth — which is precisely what
Q5 cannot pay 32x owner earnings for.**
**Likelihood: [x] likely.** It is already happening and the company says so.

**MECHANISM 2 — THE FAST ONE. Simultaneous tightening of trade credit and commercial paper
against negative working capital.**

This is the [E3-24] *"Consider some mathematics"* exercise. ORLY funds itself with other
people's money at both ends: **$7,385M of accounts payable at 123.9% of inventory**, and
**$1,345M of commercial paper**, against **$262M of cash** and **negative $2,375M of working
capital**. Both sources tighten in the same event, because both are unsecured short-term credit
extended on the strength of the same credit rating.

*Quantified from filed figures:*

| call in a credit event | amount |
|---|---|
| AP reverting from 123.9% to its **2016 level of 105.7%** of inventory | **$1,046M** |
| Commercial paper unable to roll | **$1,345M** |
| 5.750% Senior Notes due 2026 | **$750M** |
| **Total** | **$3,141M** |
| Against: cash | $262M |
| Against: undrawn revolver (committed to March 2030) | $2,250M |
| **Shortfall** | **$629M** |

The shortfall is closed by suspending the buyback for one quarter — $2.4bn a half is more than
enough. **So this is survivable, and the arithmetic says so.** But note what it costs: the
company would be forced to stop repurchasing at exactly the moment its stock was cheapest,
which is the [E2-64] point run backwards — Berkshire borrowed *before* the need precisely so
that *"the most attractive opportunities"* could be taken when *"credit is extremely expensive
— or even unavailable."* **ORLY has done the opposite: it has spent its balance-sheet capacity
buying stock at $91 and would enter a credit event with $262M of cash.**
**Likelihood: [x] a low-level possibility** for the simultaneous version. **The debt-funded
distribution continuing until it constrains the business is [x] a real possibility**, and the
[E2-60] table above is three and a half years of evidence for it.

**[E4-51] — the bear case as its holders would state it, which is the harder direction here.**
The best argument against my own Q4 finding: *the owner-earnings decline is a capital-cycle
artifact, not deterioration. ORLY spent 2023-2026 building distribution capacity — two new DCs
— that will be depreciated over decades and will not repeat. Strip the DC build and capex
returns toward $700-800M, at which point owner earnings are $2.0-2.1bn and rising, TTM owner
earnings have ALREADY recovered to $2,122M, H1-2026 capex FELL 6.1% year on year, and comps
are accelerating to +7.0%.* **That argument is strong, it is supported by the TTM figure, and I
cannot refute it from the filings.** What I can say is that it does not change the Q5 answer:
even at the highest construction in the range, $2,718M, the yield is 3.87% against a 5.27%
sovereign.

- **VERDICT: [x] IN** — it survives. Strength (2) fails on the corpus's stated standard and
  strength (3) passes only because the buyback is discretionary; neither is a solvency
  question. The business is *good*, not *great*, and [E4-43] says good passes.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**This is a genuine Q5, not a `COMPUTATION — NOT A CLEARANCE`. Q1, Q2, Q3 and Q4 each returned
IN, so the hard sequence is satisfied and the price may be reported with a verdict attached.
It is the first name from this watchlist to get here.**

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on … we don't
want to buy equities where our real expectancy is below 10 percent. Now, that's true whether
short rates are 6 percent or whether short rates are 1 percent."*

**Honest pre-tax expectancy at this price: 7.1% to 8.7%. Below roughly 10%. THE NAME IS NOT
RANKED — IT IS QUIT ON.**

Expectancy = owner-earnings yield + the growth in owner earnings the business has actually
delivered:

| construction | yield | + 10-yr owner-earnings growth | **= expectancy** |
|---|---|---|---|
| conservative — $1,539M (8y ex-pandemic @ capex) | 2.19% | +4.87% | **7.06%** |
| **judged central — $2,269M** *(below)* | **3.23%** | **+4.87%** | **8.10%** |
| generous — $2,718M (TTM @ D&A) | 3.87% | +4.87% | **8.74%** |

**Why owner-earnings growth is the right rate and operating-income growth is not.** Revenue
compounded at **8.42%** a year over the decade and operating income at **8.23%**; using either
would lift expectancy above 10% and clear the floor. **Owner earnings compounded at 4.87%**,
and at **−13.2% a year** over the last four. The whole of the difference is capital intensity
— capex 2.29x D&A against 2.19x a decade ago but on a tripled base — **and capital intensity is
exactly the thing being valued.** [E2-01] exists to stop a run reaching for the flattered
series; substituting operating-income growth here would be that error, and would be the third
generous assumption stacked on two others. **[E4-18]: a conclusion that required fighting for
it is worth less, not more.**

**One book. Owner earnings against the bond.** No DCF was run; none was needed
**[E3-34, E4-21]**.

**1. THE YIELD**
- owner earnings **$1,539M – $2,718M** (judged **$2,269M**) ÷ market cap **$70,266M**
  = **2.19% – 3.87%**, judged **3.23%** · sovereign **5.27%**
- **Every construction in the range is below the bond.** The best of them is **140 basis points
  below**; the judged case is **204 basis points below**; the conservative case is **308 basis
  points below**.

**The judged central case, stated so it can be checked.** Four-year window 2022-2025 (the
five-year default [E2-42] with 2021's stimulus year removed under [E4-41]): mean OCF
**$2,998M**, mean SBC **$29.5M**, and **(c) = $700M**, the disclosed guess built at Q4 from 207
net new stores at ~42% owned plus a greenfield DC. **Owner earnings $2,269M.**

**2. WHAT THE PRICE ALREADY ASSUMES**
- **Perpetual growth needed merely to MATCH the 5.27% sovereign: +1.40% to +3.08%** (judged
  **+2.04%**). *That is achievable, and it is the strongest thing that can be said for the
  price.*
- **Perpetual growth needed to reach the [E4-28] 10% floor: +6.13% to +7.81%** (judged
  **+6.77%**).
- **What the business has actually done:** owner earnings **+4.87%/yr over ten years** and
  **−13.2%/yr over four**; revenue +8.42%/yr; operating income +8.23%/yr; **real** sales per
  square foot **+0.30%/yr**; **US vehicle miles travelled +0.55%/yr**.
- **[E4-35]'s base rate applied:** the required 6.8% is not the 15% the corpus wagers against,
  so the base rate does not by itself refuse it. **But it must be perpetual**, and the series
  it must be perpetual in is the one that has fallen for four years.
- **[E4-44]'s second bound:** *"the value of an asset … cannot over the long term grow faster
  than its earnings do."* Multiple expansion is not a term in this answer, and the EPS series —
  +17.1%/yr, nearly double the growth in net income — is **buyback arithmetic, not earnings.**
- **[E2-63] — what bounds the upside, stated rather than left open.** ORLY puts its own US
  addressable market at **$165-175bn** and holds ~10.4% of it. Store count can grow (AZO
  operates a larger domestic base), parts prices grow ~2.5%/yr, and miles driven grow 0.55%/yr.
  **A ~6% revenue path is credible. A 6.8% OWNER-EARNINGS path requires capex intensity to fall
  back to its pre-2023 relationship and stay there** — which is the bull case at Q4, which I
  could not refute and cannot underwrite either.

**3. WHAT YOU ARE PAID**
- **−140 to −308 basis points versus the sovereign**, judged **−204 bp**, before any growth.
- **You are paid less than the government bond to take equity risk in a good, not great,
  business whose owner earnings have fallen for four years.**

**THE CERTAINTY QUESTION — and a defect in the template, reported.** *The template's
"CERTAINTY SPREAD [E3-13] … a floor of +3% over the long bond" block is a **v4.0 leftover that
contradicts the governing document.** v4.1's rewritten section says the opposite:* **[E3-42]**
*"If you say I'm going to stick an extra 6 percent in on the interest rate … that's kind of
nonsense … **mathematical gibberish** … use the government bond rate."* **No per-name risk
premium was put in the rate. The bare 5.27% sovereign was used.** Certainty is priced once,
at the Q1 understanding gate and in the end discount — and the end discount is not reached
here, because the price is above the whole range without one.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01, E4-25]** — *"Using precise numbers is, in fact,
foolish."*

| basis | conservative | judged | generous |
|---|---|---|---|
| **Zero growth, at the 5.27% sovereign** | **~$36/sh** | **~$53/sh** | **~$64/sh** |
| Zero growth, at the [E4-28] 10% floor | ~$19/sh | ~$28/sh | ~$34/sh |
| *At 3% perpetual growth, at the sovereign* | *~$84/sh* | *~$124/sh* | *~$148/sh* |
| **CURRENT PRICE** | | **$86.86** | |

**Reported value range: roughly $35 to $65 per share, judged ~$53.** The 3% growth row is
published because [E4-38] requires every construction to be shown and because it is the row on
which management's own buyback is implicitly priced — **but it is not the answer**, for the
reason [E4-25] gives: at a 3% growth term against a 5.27% discount rate the denominator is
2.27% and the output moves 44% for every 100bp of assumption. **A number that sensitive to an
unobservable is not an estimate; it is the assumption restated.**

**THE FLOOR, THEN THE RANKING [E4-28, E4-21, E3-45].**
- **The floor is not cleared.** Expectancy 7.1%-8.7% against a ~10% quit-figure. **The name is
  therefore NOT RANKED.** *"that's the figure we quit on"* — and the floor does not move with
  the sovereign.
- **Points over sovereign, this name: −1.4 to −3.1.** Against the opportunity set: the money
  goes to **[E2-74]'s parking place** — the 30-year Treasury at 5.27%, which pays more, with
  certainty, than the best construction of this equity. **Nothing in this queue has yet cleared
  the floor either; ORLY is the closest any name has come, and it is still 1.3 points short at
  its most generous.**
- **[E4-45]'s switching threshold is not engaged** — there is no holding to displace.

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [ ] Normal method [E4-11] — **not used.** No end margin was applied, because none is needed:
      the price is above the entire range before any margin. Applying one would be theatre.
- **[x] Screamer test [E4-01]** — *"does the price already clear the conservative case?"*
      **Conservative case ~$36/share. Price $86.86.** The three outcomes are: below the
      conservative case → act; inside the range → no useful conclusion; **above the whole range
      → no.** **The price is 34% above the TOP of the zero-growth range and 141% above its
      bottom. This is the third outcome.** *"it ought to just kind of scream at you"*
      **[E3-25]** — and [E3-65]'s worked screamer was the Washington Post at **20% of private
      value**. ORLY trades at roughly **164% of the top of its zero-growth value.**
- **Windage count: ONE.** *(a) (c) was carried as a full band and a judged midpoint, not
  pushed to the conservative end; (b) all seven windows were published rather than the lowest
  chosen; (c) growth was taken at the realised ten-year owner-earnings rate, not haircut; (d)
  no risk premium in the rate [E3-42]; (e) no end margin.* **Conservatism is spent once
  [E4-11], at the single point of insisting owner-earnings growth rather than operating-income
  growth is the relevant rate — and that is a definitional choice the corpus makes for me
  [E2-01, E2-23], not a windage application.**

- **VERDICT: [x] IN** *(the question is answered — the evidence is here and it produces a
  number)* · **ranking position: NOT RANKED — below the [E4-28] floor, and therefore quit on
  rather than placed.**

**PLAIN ANSWER: at $86.86 you are paid roughly 3.2% to own a business that yields less than the
government bond and whose owner earnings have fallen 43% in four years. The answer is no, and
it is a price answer, not a business answer.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**There is no position, so Q6 is written as what the operator asked for: a RE-READ BAND and a
pre-registered watch list. [E1-02]:** *"I believe in establishing yardsticks **prior to the
act**."* Writing them now, with no position and no anchoring, is when they are worth most.

### THE RE-READ BAND — the price at which this file reopens

Computed from the judged owner earnings of **$2,269M** and the [E4-28] floor of 10%, since the
floor is what refused it:

| assumption | price that clears a 10% expectancy | vs $86.86 |
|---|---|---|
| zero perpetual growth | **~$28** | −68% |
| +3.0% perpetual growth | **~$40** | −54% |
| +4.87% growth *(the realised 10-yr owner-earnings rate)* | **~$55** | −37% |
| +4.87% growth **and** owner earnings recovering to ~$2,665M *(capex normalising to ~$800M on OCF of ~$3.5bn)* | **~$64** | −26% |

**RE-READ BAND: $40 – $65.** Below $65 on a recovered owner-earnings figure, or below $55 on
today's, this file is worth reopening. **Above $65 it is not, at any owner-earnings figure this
run can defend.** *(At the bare sovereign rather than the floor, the same arithmetic gives
~$53 judged and ~$64 at the generous end — which is why $65 is the ceiling of the band on
either test.)*

**Pre-committed before entry [E1-02]:**
- **Thesis-confirming metric: OWNER EARNINGS, not EPS and not comps.** Specifically **operating
  cash flow less capital expenditure**, annually. The thesis reopens if that figure returns
  above **$2.4bn** on capex at or below **$1.0bn** — i.e. if the 2023-2026 capex step proves to
  be the capital cycle management says it is. **H1-2026 is the first evidence for it: capex
  fell 6.1% year on year.**
- **Thesis-breaking metrics and their thresholds** *(any one of these, and the business case at
  Q2 is downgraded, not just the price)*:
  1. **PROFESSIONAL transaction counts turning negative.** DIY has been negative for years and
     is in the thesis. **The DIFM half is the entire franchise argument.** The MD&A states the
     direction every quarter, so this is monitorable at no cost.
  2. **Gross margin below 51.0%** for two consecutive quarters *(51.4% in Q2-2026; 51.6%
     FY2025)*, or the word **"promotional"** appearing in an ORLY MD&A. That single word closed
     DKS.
  3. **Sales per weighted-average square foot disappearing from the 10-K.** [E2-49]. The metric
     is currently published and currently falling in real terms; its removal would be the
     yardstick being disposed of instead of the manager.
  4. **AP-to-inventory falling below 110%** — the supplier financing that funds the balance
     sheet unwinding. It is 123.9% now and 105.7% in 2016; a reversion is **$1.0bn of cash**.
  5. **Debt above ~$8.5bn** without a matching rise in owner earnings — [E2-60] continuing past
     the point where the buyback is discretionary rather than structural.
- **Next catalyst dates:** Q3-2026 earnings, expected **late October 2026** (the FY2025 Q3 8-K
  was 2025-10-22); FY2026 results and FY2027 guidance, expected **early February 2027**
  (FY2025's was 2026-02-04). **FY2026 guidance to check against: comps 3.0-5.0%, revenue
  $18.7-19.0bn, operating margin 19.2-19.7%, EPS $3.10-3.20, OCF $3.1-3.5bn, capex
  $1.3-1.4bn, free cash flow $1.8-2.1bn.** H1 comps of +7.0% are already above the top of the
  guided range; **the line to watch is OCF, which missed its guided range last year.**

**The sell rule [E2-28]** — two triggers, three hold conditions. *No position, so recorded as
the standard that would govern one:*
- **SELL if the market judges it more valuable than the facts indicate** — **this is the
  current state.** At $86.86 against a judged ~$53, the market is doing exactly that. It is a
  reason not to buy; for a holder it would be trigger 1.
- **SELL if funds are needed for something more undervalued or better understood** — the
  30-year Treasury at 5.27% is presently better understood and better paid **[E2-74]**.
- **HOLD conditions, scored:** return on capital satisfactory — **YES but deteriorating**
  (74.6%, three straight declines from 104.9%); management competent and honest — **YES, no
  disqualifier found**, with two live flags; market does not overvalue — **FAILS.**
- *Price appreciation and holding period are **explicitly rejected** as reasons to sell, and
  neither is used here.*

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** *"we sell — really
when we reevaluat[e] the economic characteristics of the business … And those beliefs change
quite gradually."* **The monitoring question [E3-30]: is this erosion an aberrational cycle, or
has the business slipped in a way that permanently reduces intrinsic business values?**

**My answer, stated so it can be held against me: PART CYCLE, PART PERMANENT, and the two are
separable.**
- **Cyclical:** the capex step. Two distribution centres were built in three years; they do not
  repeat annually; H1-2026 capex is already down 6.1%. **This part I expect to reverse.**
- **PERMANENT:** the DIY unit decline. It is not a cycle — it is vehicle durability, it is
  disclosed by the company as structural, it has run in every non-pandemic year since at least
  2017, and **no repair-frequency series turns back up**. Half the business has a permanently
  falling unit count offset by a rising ticket, and the ticket offset in FY2025 was **a
  one-time tariff pass-through**, which does not recur.

**[E4-17] is why this is a Q6 note and not a Q2 OUT:** the belief that this is permanent should
form gradually, and one run is not gradual. **[E2-40] is the counterweight** — once a view has
crystallized, delay is the graver error. **It has not crystallized. It is one year of reading.**

**Do not trim winners [E5-14]** — not applicable; no position.
**POSITION SIZE — a judgment, stated: ZERO.** Not because the business failed, but because
**[E5-35]** governs: *"You can turn any investment into a bad deal by paying too much."* And had
the price been right, the size would still have been sized **DOWN** from whatever the rank
justified, because a **[E5-08] capital-allocation flag is live** and the framework says such a
flag **binds position size** — *"sized DOWN if a capital-allocation flag is live."*

- **VERDICT: [x] IN** — the exit and re-entry standards are written, pre-committed, and
  measurable from documents that arrive on a known schedule.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. **Q1 IN · Q2 IN · Q3 IN · Q4 IN · Q5 IN
      (not ranked — below the floor) · Q6 IN.**
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** The moat class
      is **NARROW**, not PROVISIONAL: all four SEC-registered national competitors were pulled.
- [x] No UNRESEARCHED verdict was returned. *(Two GAPs are recorded inside the evidence and
      neither drives a verdict: US fleet-age years 2015-2021 and 2026, and any 2025-26 Amazon
      installer expansion. Both are named in `_research 2026-09-02 ORLY/amazon_and_channel.md`.)*
- [x] No UNKNOWABLE verdict was returned. **The 76.6% owner-earnings width was tested against
      the UNKNOWABLE trigger and does not fire, because the entire range lies below the
      sovereign and the capex band therefore does not change the verdict.**
- [x] Step 0: the filing was read — MD&A, cash-flow statement including detail lines, and
      footnotes — with accession numbers `0000898173-26-000009` (10-K), `0000898173-26-000045`
      (10-Q) and `0000898173-26-000014` (DEF 14A). **Two figures cross-checked against the filed
      statements**: FY2025 operating income $3,460,612k (XBRL vs the filed ten-year table), and
      total current liabilities $8,775,821k **footed line by line** from the filed balance sheet
      to prove there is no current debt inside it.
- [x] Owner earnings on a multi-year mean; **seven windows published, none preferred**; capex
      band disclosed as a judgment and **argued rather than defaulted**, with (c) stated as the
      guess [E2-23] requires.
- [x] Competitor row filled — 4 of the 4 SEC-registered national chains, same metric, same
      definition, same window, filing-sourced. GPC's constructed operating income is flagged in
      place.
- [x] Sovereign is for the earnings currency (USD, 97.9% of stores), **from the issuing
      authority** — US Treasury daily par yield curve, 5.27%, dated 2026-09-01. Not FRED.
- [x] Value stated as a round-number range (~$35–$65, judged ~$53), not a point estimate.
- [x] One bar chosen — **the screamer test [E4-01]**, third outcome. Windage count stated: ONE.
- [x] Prices dated; **aggregator used for the live quote only and flagged** ($86.86,
      2026-09-02). **Share count hand-read off the 10-Q cover: 808,960,792 at 2026-08-03.**
- [x] Run committed to git after every question.

**One item found after Q3 was written, recorded rather than back-fitted (operator rule 6):**
**66 of ORLY's 6,585 stores are leased from entities that include affiliated directors or their
immediate families**, under master lease agreements expiring 2026-06-30 to 2031-03-31. It is
disclosed in Item 2 and Note 16, the filer states the terms are *"comparable to those of third
parties"*, and at ~1.0% of the store base it cannot move a verdict. **It does not change Q3 and
is not being used to.**

## REGISTER
- **Verdict: [x] IN on all six questions — and NOT RANKED at Q5, which is a price refusal, not
  a business refusal.**
- **One line:** *O'Reilly is a genuine narrow franchise with a real distribution moat, an
  honest filing and one of the best buyback records this project has read — and at $86.86 it
  yields 2.19%–3.87% against a 5.27% government bond, with owner earnings down 43% in four
  years, so it is quit on rather than ranked.*
- **Not UNRESEARCHED and not UNKNOWABLE.** The evidence is in and it produces a number.

---

## THE OUTPUT CONTRACT

**PRICE: $86.86** (2026-09-02, aggregator quote, flagged) · market cap **$70,266M** on
**808,960,792** shares hand-read from the 10-Q cover · sovereign **5.27%** (US Treasury 30-year
par yield, 2026-09-01, issuing authority).

**Value, zero growth, at the sovereign: roughly $35 to $65 per share, judged ~$53.**
**Re-read band: $40 – $65.**

# **FAIL — at Q5, on price.**

**All four business gates returned IN. Q1 IN, Q2 IN, Q3 IN, Q4 IN.** The file was closed by
**[E4-28]'s floor** at Q5: honest pre-tax expectancy **7.1%–8.7%** against the ~10% *"figure we
quit on"*, and an owner-earnings yield of **2.19%–3.87%** against a **5.27%** sovereign — below
the bond on **every** construction of the window and the capex band.

**This is the first name in this watchlist queue to clear Q2, and the first to reach Q5.**
Thirteen consecutive names, and five consecutive specialty retailers, had closed at Q2 before
it. **It did not fail as the sixth confirmation; it failed as an eighth name that cleared the
business and lost on price** — joining COST, LOW, ITW, RPM, CSL, SHW and HD, and the first of
those to come from this list.

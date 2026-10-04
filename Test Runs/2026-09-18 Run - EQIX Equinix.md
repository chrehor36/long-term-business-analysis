# Company Run — Equinix, Inc. (EQIX) — 2026-09-18
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs. **This is a NEW NAME, not a
holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.**

Filled top to bottom. **Stopped at the first verdict that is not IN.** Run unattended from
scratch (no prior run file). Research, scripts and downloaded filings are in
`Test Runs/_research 2026-09-18 EQIX/`.

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

---
## STEP 0: THE ROUTING NOTE, THE RATE, THE PRICE, AND THE FILING

### The REIT routing note, checked on disk rather than followed
The wave 5 table says *"EQIX and DLR are REITs: the prepped reading list routes REITs to a sector
method first; a run states that and the verdict follows."* **`Framework/` was listed by this run on
2026-09-18: it holds one sector method, `SECTOR METHOD - owner earnings for insurers and
float-bearing holding companies.md`, and no sector method for REITs.** The routing note points at a
document that does not exist. v4 says *"If a rule is not here, it is not in force"*, so **v4 is
applied as written** and no REIT method is invented (PRIME RULE 3). Equinix's own REIT metrics
(FFO, AFFO, Adjusted EBITDA, "recurring" capital expenditures) are READ below as the company's
claims, not adopted as the run's definitions. The insurer method is not owed either: Equinix is
not funded by float (it is funded by senior notes and share issuance, both shown below).

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.29%** · **09/17/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing
  authority.** The cached curve was deleted and re-fetched by `tools/sources.sovereign("USD")`
  at 17:40 UTC on 2026-09-18, returning `(5.29, '09/17/2026', 'US Treasury daily par yield
  curve')`; 09/17 is the newest row on the file (the 09/18 curve is published after the close).
  FRED was not used. Struck by this run, not inherited.
- **The earnings currency is not only USD, and that is recorded rather than smoothed.** Revenue
  attributed to the US was **$3.6bn of $9,217M (39%)** in FY2025 (Note 18); EMEA is 34% and
  Asia-Pacific 21% of revenue. Equinix reports in USD, borrows in EUR, CHF, SGD, CAD and USD, and
  hedges. Precedent in this queue (CL, SPGI) prices a USD reporter against the USD sovereign and
  names the currency exposure at Q4; this run does the same. **The USD 30-year is the higher of
  the three sovereigns on file (EUR 3.83% and JPY 4.00% as last struck on 2026-09-10/13), so
  using it is the harder bar, not the easier one.**

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$1,025.94, the close of 2026-09-17**, the last COMPLETED close. Source: Yahoo Finance daily
  chart series (aggregator, permitted for live quotes only, **flagged**).
- **`tools/sources.price()` was NOT used for the struck price.** At 17:40 UTC on 2026-09-18,
  with the market open, it returned `(1028.07, '2026-09-18', 'USD')`: `regularMarketTime`
  17:40:16 UTC, i.e. an INTRADAY `regularMarketPrice` stamped with today's date, while its
  docstring says *"Latest close."* **The TOST defect reproduces on a second name.**
- Five prior closes: 09-11 $1,037.72 · 09-14 $998.72 · 09-15 $1,006.98 · 09-16 $1,016.16 ·
  09-17 $1,025.94. The last dividend in the series is **$5.16** (ex-date 2026-08-19).
- **Primary-filing cross-check of the aggregator:** EDGAR shows no Form 4 after 2026-08-06 with a
  transaction price in September; the nearest primary price is the **forward sale agreements
  executed May-June 2026 at a weighted average $1,070.52** (10-Q Note 10, accession
  `0001101239-26-000147`), which is a forward price net of commissions, not a trade print. **Recorded
  as a limit, as SPGI did: no primary-filing price exists to confirm the September quote.**

### The share count: from the cover, with the accession
- **98,671,686 shares**, as of **2026-07-28**, from the cover of the Q2 2026 Form 10-Q, accession
  **`0001101239-26-000147`**, filed 2026-07-29: *"The number of shares outstanding of the
  registrant's Common Stock as of July 28, 2026 was 98,671,686 ."* `Screens/cover_shares.py EQIX`
  returns the same figure from the same accession, *"(single class / undimensioned)"*.
- **One class.** The cover registers one equity security (*"Common Stock, $0.001 | EQIX"*) plus
  seven series of senior notes. The 2026-06-30 balance sheet: *"300,000 shares authorized; 98,731
  issued and 98,671 outstanding in 2026"* (thousands). **ERIC trap checked**: issued exceeds
  outstanding by 60 thousand shares, which are treasury (*"Treasury stock, at cost; 60 shares in
  2026"*), so outstanding is the right count. **SPGI trap checked**: no exclusion clause on the
  cover. No preferred is outstanding (the preferred certificate in the exhibit index is historical).
- **A forward overhang, quantified separately [E2-26]:** *"Forward Sale Agreements Executed |
  January 2027 | May 2026 to June 2026 | 465 | 1,070.52 | 498"* (thousand shares, $ per share,
  $M). **465,000 shares (+0.47%)** will be issued on physical settlement by January 2027 against
  about $498M of cash. Not in the cover count; shown as a sensitivity at Q5, not blended.

### The market cap
- $1,025.94 × 98,671,686 = **US$101,231.2M**. Split factor after 2026-07-28 = **1.0** (no split in
  the window); `close` used, never `adjclose`. With the forward shares settled: 99,136,686 ×
  $1,025.94 = $101,708.3M, against $498M of cash received.

### LIVE-DEAL CHECK: re-queried by this run, not inherited
- `sources.deal_filings("0001101239")` returned `([], [('8-K', '2026-07-29',
  '0001101239-26-000148')], ...)`: no merger, tender or exchange form, and one 8-K flagged for
  reading. **Read on the document:** it is Item 1.01/1.02/2.03, *"Equinix, Inc. ... entered into a
  Credit Agreement"* with a bank syndicate: a revolving credit facility, not a deal.
- Every 8-K since 2024-01-01 with Items 1.01, 2.01, 7.01 or 8.01 was fetched and its item text
  read: senior-note issues (2024-05-30, 2024-08-22, 2024-09-03, 2024-11-22, 2025-05-19,
  2025-11-13, 2025-11-24, 2026-03-05, 2026-05-07, 2026-08-06), the ATM equity distribution
  agreement (2024-10-01), the Audit Committee investigation (2024-03-25), the CEO transition
  (2024-03-12, 2024-06-03), the SEC closure (2025-11-20), the Analyst Day (2025-06-26) and a CFO
  appointment (2026-03-10). **No merger, tender or spin involves EQIX. The quote is an
  owner-earnings price, not a spread.**

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2025 Form 10-K**, period ended 2025-12-31, filed **2026-02-11**, accession
  **`0001101239-26-000032`**, primary document `eqix-20251231.htm`.
- **Q2 2026 Form 10-Q**, period ended 2026-06-30, filed **2026-07-29**, accession
  **`0001101239-26-000147`**; and the Q1 2026 10-Q (`0001101239-26-000091`).
- Also read: every 10-K from FY2015 to FY2024 (cash-flow statements FY2015-2025 and the AFFO
  reconciliations that carry "recurring capital expenditures" back to FY2013); the 8-K EX-99.1
  earnings releases of 2024-02-14, 2025-02-12, 2025-04-30, 2025-07-30, 2025-10-29, 2026-02-11,
  2026-04-29 and **2026-07-29** (`0001101239-26-000145`); the 8-K/A of 2025-07-31; the DEF 14A of
  **2026-04-02** (`0001101239-26-000073`) and 2025-04-10.
- **Figures cross-checked against the filed statement** (FY2025 consolidated statement of cash
  flows, F-8): *"Net cash provided by operating activities | 3,911"*, *"Stock-based compensation |
  498"*, *"Depreciation, amortization and accretion | 2,066"* and *"Purchases of other property,
  plant and equipment | ( 4,311 )"* all match companyfacts exactly. **The fourth match is the
  finding of Q4**: the capex tag the screen reads carries the *"other property, plant and
  equipment"* line only, and the face of the same statement carries a second capital line the
  screen does not read: *"Real estate acquisitions | ( 994 ) | ( 337 ) | ( 384 )"*.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### The unit economics, in my own words, without management's language
Equinix builds or leases buildings full of power and cooling, divides them into cabinets, and rents
each cabinet by the month to companies that want their computers in a secure room with a lot of
other companies' computers. Then it charges both parties a monthly fee for each cable run between
them. That is the business.

FY2025, from Note 18 (segment note, accession `0001101239-26-000032`), $M:

| line | FY2023 | FY2024 | FY2025 | share of FY2025 |
|---|---:|---:|---:|---:|
| Colocation (space and power) | 5,765 | 6,058 | 6,475 | 70% |
| Interconnection (cables and virtual links between customers) | 1,395 | 1,519 | 1,655 | 18% |
| Managed infrastructure | 452 | 467 | 466 | 5% |
| Other (leasing, hedging) | 133 | 140 | 143 | 2% |
| Non-recurring (installation, professional services, fees from the xScale joint ventures) | 443 | 564 | 478 | 5% |
| **Total revenue** | **8,188** | **8,748** | **9,217** | |
| Income from operations | 1,443 | 1,328 | 1,848 | 20.0% margin |

Read as a landlord and a toll:
1. **The rent.** 299,300 cabinets were billed at the end of FY2025 across 255 consolidated IBX
   buildings with 392,300 cabinets of capacity (76-79% utilised by region). Recurring revenue of
   $8,739M over about 295,000 average billed cabinets is **roughly $2,470 a cabinet a month**, all
   in. The filing's own measure, *"MRR per Cabinet"* in Q4, was **$2,694 (Americas), $2,418
   (EMEA), $2,355 (Asia-Pacific)**. Part of that is electricity passed through: the FY2023 10-K
   says EMEA growth was *"primarily due to power price increases in various European countries in
   response to the increased cost of utilities"*, and the FY2024 10-K records *"net power price
   decreases in response to the decreased cost of utilities"* the next year.
2. **The toll.** *"Equinix Cross Connects provide a point-to-point cable link between two Equinix
   customers in the same data center"* (10-K Item 1). With *"more than 500,000 interconnections"*,
   $1,655M of interconnection revenue is about **$3,300 a year, or $275 a month, per connection**.
   A cross-connect is a length of fibre inside a building Equinix already owns, so this line is the
   one with almost no incremental plant behind it.
3. **The plant.** Gross property, plant and equipment was **$36,972M** at 2025-12-31 (core systems
   $15,100M, buildings $11,170M, land $2,757M, construction in progress $2,827M, internal-use
   software $2,472M, leasehold improvements $2,210M, personal property $436M). Revenue is **25
   cents per dollar of gross plant** a year. Income from operations is **5.0%** of gross plant.
   **This is a capital-heavy rent business with a light toll attached, not a light business.**
4. **The hyperscale side is off the balance sheet.** *"xScale data centers ... are developed and
   operated through our joint venture partnership arrangements"*, in which Equinix holds about 20%
   (Note 5; carrying value $551M). Equinix earns fees from them (the non-recurring line) and its
   share of their income is small (*"insignificant"* for EMEA 1). The run treats the xScale JVs as
   a perimeter note, not as the business; [E3-04]'s look-through would add almost nothing because
   the JVs are described as *"not ... self-sustaining"*.

Costs, FY2025: segment cost of revenues (before depreciation and stock pay) **$2,959M**, of which
the 10-K names utilities, rent on leased buildings, bandwidth, site staff, repairs and security as
the largest parts; selling and administrative **$1,728M** on the same basis. Adjusted EBITDA
(the company's measure) $4,530M; depreciation, amortisation and accretion **$2,066M**; stock pay
$498M.

**How the money is financed, which Q1 must state because it shapes every later gate:** in FY2025
operating cash was **$3,911M**, capital spending **$5,305M** ($4,311M other plant + $994M real
estate), dividends **$1,856M**. The gap was filled by **$4,311M of new senior notes** (and $99M of
shares under the ATM programme). Equinix is a REIT: *"We expect all of our 2025 quarterly
distributions and other applicable distributions to equal or exceed our REIT taxable income"*.
It pays out, then borrows and issues shares to build.

### The scarce input this business controls
**The meeting place.** *"More than 2,000 network service providers offer access to the world's
internet routes inside our IBX data centers"* (Note 1), plus *"a leading market share of cloud
on-ramps"* (Item 1). A company that needs to connect to many networks, clouds and trading
counterparties at once needs to be in the building where they already are. The building and its
power can be copied with capital; **the population of the building is what is scarce**, and it
accumulated over 27 years. The 10-K states the mechanism in its own words: *"As more customers
choose Equinix ... it benefits their suppliers and business partners to colocate in the same data
centers and connect directly with each other."* A second scarce input, shared with every rival, is
**power and permitted land in constrained metros** (*"We could face power limitations in our
existing IBX data centers"*, MD&A).

Named precisely, because Q2 turns on it: the scarce input is the ecosystem in particular
buildings, **not** data-centre space in general. Space in general is a commodity built by
anyone with capital; the 10-K's own risk factor says competitors *"may adopt aggressive pricing
policies, especially if they are not highly leveraged or have lower return thresholds than we
do."*

### Will the fundamentals look broadly the same in ten years?
**The mechanism, yes.** Companies will still need to put equipment in a secure, powered room near
the networks and clouds they exchange traffic with, and the owner of the room will still charge
rent and a fee per connection. **The equipment inside the room, no.** The MD&A: *"This increased
power consumption, which we expect to accelerate with the adoption of AI, has driven us to build
out our new IBX data centers to support power and cooling needs twice that of previous IBX data
centers"*; and cost of revenues rose partly on *"acceleration of depreciation expense for certain
assets with shortened useful lives"*. That is a question about whether the moat must be rebuilt
(**[E4-04]**, Q2) and about what maintenance costs (**(c)**, Q4), not about whether the
money-making mechanism is understandable. It is.

**The honest limits, stated rather than smoothed.** (1) Five currencies of debt, three regions,
REIT and taxable subsidiaries, joint ventures, and a company-defined "recurring" capital line
disputed publicly by a short seller in 2024 make the ACCOUNTING harder than the business; that is
a Q3 and Q4 matter. (2) Revenue is 39% US; the rest is earned in euros, sterling, yen, Singapore
dollars and others.

- **VERDICT: [x] IN**
  *The unit economics are writable in plain words (rent per cabinet, fee per cable, on a large
  plant financed by debt and issuance); the scarce input is nameable (the population of
  particular buildings); the mechanism will be recognisable in ten years **[E3-31]**. Whether the
  population is a franchise is a relative claim, and it is Q2's.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

### WHAT IS BEING TESTED
Q1 named the scarce input as **the population of particular buildings**: the networks, clouds and
counterparties already present, which a newcomer must join rather than recreate. The franchise
claim is that customers regard an Equinix building as having **no close substitute** once their
counterparties are in it, and that Equinix can price accordingly. [E3-03] states how the claim
shows itself: *"The existence of all three conditions will be demonstrated by a company's ability
to regularly price its product or service aggressively and thereby to earn high rates of return on
capital."* (1991 letter.) **Both halves of that sentence are tested below on Equinix's own filings
first: the pricing, and the return on capital.** The claim is also split, because the filing splits
the revenue: the **toll** (interconnection, $1,655M, 18%) and the **rent** (colocation and managed
infrastructure, $6,941M, 75%).

### THE THREE CONDITIONS **[E3-03]**

**(1) Needed or desired: IN.** 299,300 cabinets billed, 500,000+ interconnections, over 10,500
customers, recurring revenue above 90% of the total every year for three years, and *"more than
90% of our monthly recurring revenue bookings came from existing customers"* (MD&A).

**(3) Not subject to price regulation: IN, with one note.** No regime sets Equinix's rent or
cross-connect fees. Electricity is re-priced to customers as costs move, in both directions
(*"power price increases ... in response to the increased cost of utilities"*, FY2023 10-K; *"net
power price decreases in response to the decreased cost of utilities"*, FY2024 10-K). That is a
pass-through of an input cost, not a regulated price, and [E2-59] is not engaged. It does mean that
part of the per-cabinet revenue series moves with power prices and not with pricing power, which is
why the price test below is read in the Americas, where the filing names no power pass-through
event.

**(2) No close substitute: SHOWN FOR THE TOLL, NOT SHOWN FOR THE RENT, and the filing itself now
qualifies the toll.**

1. **The toll: the strongest evidence in the file for the claim.** Interconnection revenue grew
   from **$893.6M (FY2019) to $1,655M (FY2025), 10.8% a year**, and from 17.0% to 18.0% of revenue
   in FY2023-25. Interconnections rose from about **462,000 (end FY2023) to 482,000 (end FY2024) to
   more than 500,000 (end FY2025)** (releases of 2024-02-14, 2025-02-12, 2026-02-11), so revenue per
   interconnection rose about **4.7% in FY2025** (about $3,220 to $3,370 a year) on top of about 4%
   unit growth. A customer who needs 2,000 networks and the clouds' on-ramps in one room has few
   rooms to choose from. **But the newest filing qualifies it in the company's own words**, a
   sentence absent from every earlier filing read: *"certain network, cloud and content providers
   may seek to offer connectivity and interconnection through alternative models that bypass
   colocation environments, and increased customer adoption of these alternatives could reduce
   demand for our interconnection offerings"* (10-Q for Q2 2026, `0001101239-26-000147`). And the
   10-K concedes the advantage is local: *"In certain of our markets, the limited number of carriers
   available reduces that advantage. As a result, we may need to adapt our key revenue-generating
   offerings and pricing to be competitive in those markets."*
2. **The rent: a contested market, on the filer's own page.** FY2025 10-K Item 1A: *"The global
   multi-tenant data center market is highly fragmented. It is estimated that we are one of more
   than 2,400 companies that provide these offerings around the world"*, and *"Some of our
   competitors may adopt aggressive pricing policies, especially if they are not highly leveraged or
   have lower return thresholds than we do. As a result, we may suffer from pricing pressure"*. The
   Q2 2026 10-Q adds: *"if the market was to experience an event of excess data center capacity,
   capacity originally developed to serve wholesale or hyperscale requirements could be redirected
   toward the enterprise colocation markets in which we operate, increasing available supply and
   intensifying competition and pricing pressure in our core business."*
3. **The price series, units and dollars [E4-55], in the region without a named power pass-through
   event.** Americas *"MRR per Cabinet"*, Q4 of each year (10-K portfolio tables): **$2,415 (FY2020),
   $2,342, $2,419, $2,527, $2,550, $2,694 (FY2025): +11.6% in five years, about 2.2% a year**, with
   cabinets billed in the Americas up from 86,800 to 123,700. Over the same years the company's own
   **project cost per sellable cabinet rose from $58.7k to $126.2k** (the year-end construction
   tables), and the 10-K says customers now draw *"an increasing amount of power per cabinet"*. **The
   rent per cabinet has not kept pace with what a cabinet costs to build.** EMEA's rise ($1,530 to
   $2,418) is mostly the power pass-through the FY2023 and FY2024 10-Ks name.
4. **No agony document, and no churn figure.** [E4-37] asks for the prayer session before a price
   rise. Equinix files no customer letter on price, no renewal spread and no churn rate in any 10-K,
   10-Q or earnings release read (the words appear only in risk factors); its revenue-recognition
   note says *"Certain contracts include terms related to price arrangements such as price increases
   and free months"*, and the 2026-07-29 release cites *"firm pricing"* without a number. The
   Annualized Gross Bookings definition is *"adjusted for the impact of pricing changes on existing
   contracts"*, again without the number. **The company's churn is published only in investor
   materials on its IR site (the next rung), which this run did not fetch; its absence from the
   filings is recorded, not scored.**

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4)*
Built for this run from filings (`peers/PEER_ROW.md`, every cell with an accession). Taken: **Digital
Realty (DLR)**, **American Tower's Data Centers segment (CoreSite)**, **Iron Mountain's Global Data
Center segment**, **Cyxtera** (bankrupt 2023), and the stale last filings of **CyrusOne, QTS, Switch
and CoreSite** (all taken private or acquired 2021-22). Private operators (Vantage, Stack, Aligned,
NTT GDC, Cologix, Flexential, DataBank) and hyperscaler self-build are **not measured by any filing
found** (EDGAR full-text: they appear only as ABS-15G securitisation filers, fund holdings and CMBS
trust exhibits; queries and hit counts in the row file). **Nine examined, four current filers
numbered.** The universal-filing route (the SPGI Form NRSRO lesson) was tried through the ABS-15G
securitisation filings and does not resolve: those are third-party due-diligence reports, not
operating metrics.

**ROW A: RETURN ON PLANT, (operating income + D&A) / average gross plant, same formula, FY2023-25:**

| company | FY2023 | FY2024 | FY2025 | basis |
|---|---:|---:|---:|---|
| **Equinix** | **11.9%** | **11.1%** | **11.6%** | 10-K statements and PP&E note |
| Digital Realty | 7.0% | 6.9% | 7.4% | DLR 10-Ks FY2023-25 (FY2025 `0001104659-26-015365`); gross investments in properties incl. CIP and land; 7.4-7.6% with impairments added back |
| AMT Data Centers | | 6.9% | 7.7% | segment operating profit over Schedule III gross real estate (`0001053507-26-000035`); 3.9-5.3% on segment total assets incl. CoreSite goodwill |
| Iron Mountain data centers | | | | not computable: no segment assets (segment Adjusted EBITDA margin 42.0% to 51.8%, 2021-25) |
| Cyxtera, FY2022 | | | 1.7% (8.1% before a goodwill impairment) | last 10-K (`0001794905-23-000010`) |

**Equinix earns about 1.6 times Digital Realty's return on the same kind of plant, the widest
measurable gap in the row.** That is the relative position, filed, at full strength. **And its own
series is falling**: the same ratio was **15.3% (FY2016), 15.2%, 14.8%, 14.4%, 12.5%, 12.2%, 11.8%,
11.9%, 11.1%, 11.6% (FY2025)** (`returns.py`).

**ROW B: INTERCONNECTION, share of revenue:**

| company | FY2023 | FY2024 | FY2025 | note |
|---|---:|---:|---:|---|
| **Equinix** | **17.0%** | **17.4%** | **18.0%** | segment note; 500,000+ interconnections, the only count filed |
| Digital Realty | 7.7% | 8.0% | 7.8% | "Interconnection and other", 8-K supplements only; no count |
| AMT Data Centers | 14.0% | 14.3% | 14.4% | "Non-lease property revenue", which includes interconnection; no count |
| Switch (stale, FY2021) | | | 17.9% | "Connectivity", broader than interconnection |
| CoreSite (stale, FY2020) | | | 13.9% | |

**ROW C: RENEWAL PRICING AND CHURN (Equinix files neither):**

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---:|---:|---:|---:|---:|---:|
| DLR renewal rent change, cash, all products | (3.1)% | 1.8% | 6.8% | 9.0% | 6.7% | 15.9% |
| DLR renewals, 0-1 MW (retail colocation, the product Equinix sells), cash | 1.0% | 3.4% | 4.9% | 4.2% | 4.1% | 4.7% |
| DLR churn, total | 7.2% | 6.5% | 4.8% | 6.2% | 5.4% | 5.5% LTM |
| Iron Mountain data-centre churn | | 3.5% | 5.7% | 7.0% | | |

CyrusOne, FY2021 (stale, `0001553023-22-000009`): *"Rates contracted with our customers that renewed
in 2021 were lower than the rates previously in effect, a trend that we expect to continue and to be
driven by increases in data center supply and cloud company offerings."*

**ROW D: THE COMPANY'S OWN MAINTENANCE CAPEX against D&A:** Equinix **11.8%, 12.4%, 13.7%**
(FY2023-25); **Digital Realty 19.7%, 17.7%, 18.5%** (recurring capex over real-estate D&A). Equinix's
"recurring" figure is the lowest in the row relative to its depreciation (Q4 takes this up).

**Who names whom.** Digital Realty names Equinix as a competitor in every 10-K FY2021-25
(*"including Equinix, Inc. and NTT"*), as did Cyxtera, CoreSite and Switch. **Equinix is also Digital
Realty's sixth-largest customer** (14 locations, $95.6M of annualised rent, DLR FY2025 10-K): it rents
capacity from its closest rival. **Equinix named competitors in its 10-Ks through FY2018** (*"CoreSite,
Digital Realty Trust, Global Switch, Interxion and Telehouse"*) **and has named none since FY2019.**

### WHAT THE ROW SHOWS, AND WHAT IT DOES NOT
- **Position: Equinix is the best business in its industry on the filed record.** Its return on
  plant is about 1.6x the nearest filer's, its interconnection share is the highest, and it is the
  one name every competitor lists. That is recorded at full strength.
- **But the best return in the row is a modest return in absolute terms, and it is falling.** 11.6%
  of gross plant is before any maintenance and before tax; after depreciation, income from
  operations was **8.6% of average net plant (FY2025) and 7.0-8.6% in every year FY2020-25, against
  9.6-10.7% in FY2015-19** (`returns.py`); net income on average equity was **7.0% over five years**
  on debt of about 1.4x equity. [E3-03]'s demonstration is *"to regularly price its product or
  service aggressively and thereby to earn high rates of return on capital"*; [E3-46]: *"the best
  businesses, by definition, are going to be businesses that earn very high returns on capital
  employed over time."* **The row shows Equinix as the least capital-hungry earner in a capital-heavy
  industry, not as a business earning very high returns.**
- **The pricing in this window is the market's, not Equinix's.** Digital Realty's renewals rose
  6.7% cash in FY2025 and 15.9% in H1 2026; even its retail 0-1 MW renewals rose 4.1-4.9% a year.
  Equinix's Americas rent per cabinet rose about 2.2% a year FY2020-25. A tight market lifted every
  landlord; the filed evidence does not show Equinix pricing above it. The same row shows the
  opposite regime is recent history: DLR renewals rolled **down** 3.1% in FY2021, and CyrusOne filed
  that renewals were repricing lower on new supply.
- **[E3-61], the row's limit:** it shows position and returns; it cannot show how Digital Realty,
  the private operators funded by securitisation, and the hyperscalers will price the capacity now
  being built.

### THE OTHER Q2 TESTS
- **[E4-04]: engaged, on the company's own words, and the scope test answers "replacement" for the
  plant.** *"Because many of our IBX data centers were built a number of years ago, the current
  demand for power may exceed the designed electrical capacity in these IBX data centers"*; new
  builds carry *"power and cooling needs twice that of previous IBX data centers"*; useful lives
  were shortened in FY2024 and FY2025; and *"If we fail to invest before or contemporaneously with
  our competitors, our results of operations could suffer."* v4's scope test asks whether the
  spending defends the same advantage or buys its replacement. **The ecosystem is defended; the
  building that houses it is replaced**, at a cost per cabinet that doubled in five years. Does a
  lapse in spending destroy the structure or merely narrow it? The filing's answer is that an
  un-upgraded building cannot fully use its own space (*"our ability to fully utilize the space in
  those IBX data centers may be impacted"*): the structure narrows building by building. [E5-23]
  licenses defence; it does not turn a plant that must be rebuilt at twice the unit cost into an
  enduring moat.
- **[E2-44] two-characteristic test.** (1) *"an ability to increase prices rather easily (even when
  product demand is flat and capacity is not fully utilized)"*: **not shown.** Utilisation is 79%,
  76% and 73% by region, prices rose with the whole market in a tight window, and no filed renewal or
  price figure exists for Equinix. (2) *"an ability to accommodate large dollar volume increases in
  business ... with only minor additional investment of capital"*: **FAILS outright.** Capital
  spending ran **31.6-57.6% of revenue every year FY2015-25**, and the company now guides **$5-7bn a
  year** of capex for 2027-2029 against revenue of about $10bn.
- **[E2-45] the attacker's test.** The attacker exists and is funded: the Q2 2026 10-Q's *"excess
  data center capacity"* sentence, Digital Realty building in the same metros, and private operators
  financed through securitisation. An attacker cannot reproduce the population of Equinix's oldest
  buildings; it can build the rooms next door, and the filings show it doing so.
- **[E2-58] the commodity doctrine**: *"persistent over-capacity without administered prices (or
  costs) equals poor profitability"*, with long-run profitability set by *"the ratio of
  supply-tight to supply-ample years"*. The filed record FY2023-H1 2026 is supply-tight (DLR renewals
  up 15.9%); FY2021 was supply-ample (renewals down). Equinix's return on plant fell through both.
- **[E4-36] which cause of extreme success?** A **nonlinear combination** (interconnection density
  times global footprint) that is real and partly ownable, **riding a wave** (cloud, then AI demand
  for capacity). The ownable part is the toll; the wave part is the rent.
- **[E4-32] direction: NARROWING on the one measure filed consistently.** Return on gross plant from
  about 15% (FY2016-17) to 11.6% (FY2025); operating income on net plant from about 10% to 8.6%.
  [E4-32]: *"that does not necessarily mean that the profit is more this year than last year"*;
  profit grew, the return on the capital did not.
- **[E3-33] untapped pricing power: REFUSED** under [E5-28]: one of *"more than 2,400"* providers is
  not a near monopoly, and no filed figure shows price held back.
- **[E2-53] the dominance class: not available** for the rent; arguable only within particular
  buildings for the toll, and the company itself says the advantage is weaker where carriers are few.
- **[E4-23] key-person**: none; CEO, CFO and CAO all changed in 2024-2026.

### WHAT THE FRANCHISE CASE RESTS ON, AT FULL STRENGTH **[E4-26, E4-51]**
The best case for IN, stated so its holders would accept it: the interconnection ecosystem is a
network effect built over 27 years that no competitor has matched (the highest interconnection share
in the row, the only count filed, revenue per connection rising); Equinix earns 1.6x its nearest
rival's return on the same kind of plant; more than 90% of bookings come from existing customers;
every competitor names it; and demand for capacity is the strongest on record. **Each fact is true
and each is recorded.** What defeats it is that [E3-03] asks for the franchise to show itself in
**high returns on capital**, and the filed record shows the best business in the row earning about
8-9% before tax on its net plant, falling for a decade, while needing **a third to more than half of
revenue in new capital every year** to grow at all. **The toll cannot be separated from the rent**:
interconnection revenue exists only inside buildings whose space and power are sold in a market of
2,400 providers, and no filing separates the toll's profit or capital from the whole. SPGI passed on
one separable leg (ratings, 48.5% of profit, its own segment); **Equinix has no separable leg to
pass on.**

### CLASS AND VERDICT
- Needed or desired **[x]** · no close substitute **[ ]** (shown for the toll within particular
  buildings; not shown for the rent, and qualified by the company's own new bypass and oversupply
  sentences) · not price-regulated **[x]**
- **Class: NARROW position, NO franchise as [E3-03] demonstrates one.** The best-positioned landlord
  in a capital-heavy, contested industry, with a real toll attached. **Direction: returns on plant
  narrowing for ten years.**
- **The gate does not close on missing evidence.** Equinix's churn (IR site) and the private
  operators' numbers are unnumbered, and neither is what fails the gate: it fails on filed returns on
  capital, filed capital intensity, and the company's own risk-factor sentences. A churn figure of
  any size would not supply the missing high return on capital.

**VERDICT: [ ] IN  [x] OUT**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
*OUT on the business: [E3-03]'s demonstration clause (high returns on capital) and [E3-46] fail on
the filed record even though Equinix leads the filed row; [E2-44](2) fails outright; [E4-04] is
engaged in the company's own words and the scope test answers "replacement" for the plant. Not a
finding that Equinix is a poor business: on the filed record it is the best operator in its
industry. **The file closes here.** Q3-Q6 below are RECORDED, NOT GOVERNING, as at TOST and the other
Q2 closes in wave 5.*

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the
> queue asks every run for a price and because the evidence was gathered; it decides nothing and
> cannot reopen Q2 [E2-37, E3-39].

### STEP 1 - THE WEIGHT CASE
- [ ] **Daily execution** **[E3-38]**: not ticked for operations. Contracts run *"one to five
  years in length, and thereafter automatically renews in one-year increments"*, and *"more than
  90% of our monthly recurring revenue bookings came from existing customers"*: the operating
  business is a landlord's, smart-once per building. **But the capital programme is continuous and
  large**: total capital expenditure guided at **$5.0-6.0bn for 2026** and **$5.0-7.0bn a year for
  2027-2029** (release of 2026-07-29), i.e. 5-7% of today's market value committed each year. The
  weight lives in capital allocation, and it is read there below.
- [ ] **Control** **[E1-16]**: not ticked; a minority public holding, one share class.
- [ ] **Leverage** **[E3-29]**: not ticked, and quantified rather than waved: senior notes and
  loans of about **$19.7bn** at 2026-06-30 (plus **$3.0bn** issued on 2026-08-06), finance-lease
  liabilities **$2.3bn**, against book equity of **$14.4bn** and a market value of about $101bn.
  Not the 20:1 bank case [E3-29]; an asset error does not wipe out the equity.

**Case declared: a qualitative OVERLAY**, with the capital programme named as the place a weak
manager would do the damage.

### THE BINARY - honesty **[E5-16]**, each matter dated to when it became public
- **2024-03-20 (public the same day, 8-K of 2024-03-25, `0001104659-24-038175`):** *"a short seller
  report was published about us, which contained certain allegations related to components of our
  operating results and other strategic matters. As a result, the Audit Committee of our Board of
  Directors commenced an independent investigation"*; a subpoena from the **U.S. Attorney's Office
  for the Northern District of California** followed, and on **2024-04-30** a subpoena from the
  **SEC**. **The short seller's report is not a filing and was not read by this run; the brief
  describes it as concerning AFFO and maintenance capital expenditure. The company's filings never
  name the allegations beyond "components of our operating results".**
- **2024-05-08 (Q1 2024 release, 8-K `0001628280-24-021695`):** *"Based on the findings of the
  independent investigation, the Audit Committee has concluded that Equinix's financial reporting
  has been accurate, and that the application of its accounting practices has resulted in an
  appropriate representation of its operating performance ... the Audit Committee did not identify
  any accounting inconsistencies or errors requiring an adjustment to, or restatement of, previously
  issued financial statements or non-GAAP measures."* Seven weeks from report to conclusion; the
  2025 proxy records **36 Audit Committee meetings in 2024**.
- **2025-11-19 (8-K of 2025-11-20, `0001101239-25-000074`):** *"the Company received correspondence
  from the SEC indicating that the agency had concluded its investigation and does not intend to
  recommend an enforcement action. The Company also does not expect any further related action from
  the NDCA."*
- **Litigation (FY2025 10-K Item 3):** the securities class action (class period 2019-05-03 to
  2024-03-24) was partly dismissed on 2025-01-06, then settled; *"The case was dismissed with
  prejudice on December 19, 2025, and the settlement was covered entirely by our insurance."* Two
  derivative suits were voluntarily dismissed in 2025; **a third, in Delaware (filed 2025-08-06),
  alleging insider trading by directors and officers, has a motion to dismiss pending.**
- **Leadership turnover after the investigation, recorded without inference:** CEO Meyers to
  Fox-Martin (announced **2024-03-12**, eight days BEFORE the report, *"as part of a planned
  succession process"*); CFO Keith Taylor's retirement announced **2025-12-03**, two weeks after the
  SEC closure letter, successor from Eaton from 2026-03-16; Chief Accounting Officer Simon Miller's
  retirement (effective 2026-07-31), *"not due to any disagreement with the Company on any matter
  relating to the Company's financial statements"*; the Chief Sales Officer and Chief Business
  Officer left in 2026.
- **No disqualifier found.** Per [E5-17] this is the absence of found disqualifiers, not a finding
  that the managers are honest; and per [E5-22] the outcome of the inquiries (no action) is not
  evidence of seriousness in either direction. **The part of the 2024 episode that is a filed fact,
  and that this run can judge itself, is the capital-expenditure disclosure. It is read under the
  flags below and at Q4 (c), where it belongs.**

### STEP 2 - THE FLAGS. *Each is a prompt to READ, never a verdict.*
- [x] **EBITDA / adjusted-earnings promotion [E4-29]: FIRES AT FULL STRENGTH, and the filing says
  the thing [E4-29] calls nonsense in so many words.** FY2025 10-K Item 7: *"Both measures eliminate
  the impacts of depreciation and amortization, which are derived from historical costs and we
  believe are not indicative of current or future expenditures"*. [E4-29], 2002 letter: *"Doing so
  implies that depreciation is not truly an expense, given that it is a 'non-cash' charge. That's
  nonsense."* Adjusted EBITDA and AFFO head every release (Q2 2026: *"Adjusted EBITDA $1.396
  billion, a record adjusted EBITDA margin of 53%"*; *"AFFO ... $11.78 per share"*), guidance is
  given in both, and **pay is funded on AFFO**: DEF 14A of 2026-04-02 (`0001101239-26-000073`),
  *"Short-term incentive compensation is earned under our annual incentive plan, which in 2026 will
  be funded based upon our performance against equally weighted revenue and AFFO/Share targets"*,
  and the PSUs vest on *"revenue and AFFO/Share goals"* plus relative TSR. AFFO FY2025 was
  **$3,761M against GAAP net income of $1,350M**; the bridge adds back **$2,050M of depreciation and
  amortisation and $498M of stock pay** and deducts **$284M of "recurring capital expenditures"**.
- [x] **The incentive [E4-27], stated as the incentive and not as a finding of conduct.** AFFO per
  share, on which the bonus is funded, deducts only the capital spending the company classifies as
  **recurring** (*"expenditures to extend the useful life of data centers or other assets that are
  required to support current revenues"*). Every dollar classified as non-recurring instead raises
  the bonus metric by a dollar. Recurring capex has run **10.9-16.9% of D&A since FY2016** (13.7% in
  FY2025). *"Never, ever, think about something else when you should be thinking about the power of
  incentives"* [E4-27]. The Audit Committee and the SEC examined the classification and found
  nothing to correct; the incentive nevertheless exists, and it is why this run sets (c) itself at
  Q4 rather than adopting the company's line.
- [x] **A claim withdrawn without comment [E2-26].** Every 10-K from FY2019 to FY2024, and every
  10-Q to Q2 2025, justified excluding depreciation with this sentence: *"The construction costs of
  an IBX data center do not recur with respect to such data center, and future capital expenditures
  remain minor relative to our initial investment throughout its useful life."* **It is absent from
  the Q3 2025 10-Q (filed 2025-10-29) onward**, including the FY2025 10-K and both 2026 10-Qs,
  replaced by the shorter *"derived from historical costs and we believe are not indicative of
  current or future expenditures"*. The change came three weeks before the SEC closure letter; no
  filing explains it. The direction is toward caution (a strong factual claim stopped being made),
  which [E2-69] says to judge by direction; the omission of any explanation is what [E2-26] asks
  about. **Recorded as a prompt; it bears directly on (c) at Q4.**
- [x] **Trumpeted projections [E4-22 third flag]: FIRES.** Quarterly and annual guidance on
  revenue, Adjusted EBITDA, AFFO and AFFO per share, and a multi-year outlook: Analyst Day
  2025-06-25 (8-K `0001101239-25-000013`), *"AFFO per share growth of 5% - 9% each year from 2025
  through 2029"* and *"8% or greater dividend per share growth each year"*; raised on 2026-07-29 to
  AFFO per share growth of **9-12%** a year and total capex of **$5.0-7.0bn** a year. **[E3-48]
  record:** FY2024 revenue guided $8.793-8.893bn, **came in at $8,748M, below the range**; AFFO per
  share guided $34.58-35.31, came in at $35.02, inside. FY2025 revenue guided $9.033-9.133bn, came in
  at $9,217M, above; AFFO per share $36.69-37.51 against **$38.33**, above; **total capex guided
  $3.222-3.472bn against $4,311M of other plant plus $994M of real estate**. Mixed on earnings, and
  consistently exceeded on spending. **[E4-35]**: 9-12% a year of per-share growth for four years
  is a claim the corpus prices as rare.
- [x] **Metric-switching [E2-49]: FIRES, small.** DEF 14A 2026: *"Results for the fabric attach
  growth rate in 2025 were below threshold, which led to a payout of 90% for the goal"*, and in the
  same document *"the Talent, Culture and Compensation Committee approved an interconnection revenue
  metric for the strategic modifier to the 2026 annual incentive plan, replacing the prior metric
  related to Equinix Fabric"*. [E2-49]: *"Yardsticks seldom are discarded while yielding favorable
  readings."* The reason given is alignment with strategy; the order of events is the one the flag
  describes. It is a ±10% modifier, not the core metric. **The [E2-49] prior stands at seven fires
  and six failures** after this run.
- [x] **Serial share issuance [E5-15]: FIRES.** Diluted weighted shares **58.5M (FY2015) to 98.1M
  (FY2025), +67.7%**; **$11,141M** raised in public and ATM offerings FY2015-2025; a new forward of
  465,000 shares executed May-June 2026 and $700M still available under the 2024 ATM programme.
- [x] **Dividends funded by issuance [E2-52]: FIRES, and the match is almost exact.** FY2015-2025:
  dividends paid **$11,234M**; equity raised **$11,141M**; operating cash **$25,359M** against capital
  spending (other plant plus real estate) of **$27,884M** and acquisitions of **$9,393M**. Over eleven
  years every dollar of dividend was replaced by a dollar of new shares, and operating cash did not
  cover even the plant. [E2-52]: *"Beware of 'dividends' that can be paid out only if someone
  promises to replace the capital distributed."* The company's defence would be that the issuance
  funded growth, not the dividend; Q4 tests that on the owner-earnings line, where the dividend
  exceeds owner earnings at the corpus's default (c) in **every one of the eleven years**.
- [ ] **Weak accounting / period-shifting [E4-22 first flag, E4-34]: NOT FIRED, three prompts.**
  (1) The 8-K/A of 2025-07-31 (`0001101239-25-000035`) corrected *"inadvertent errors"* in the Q2
  2025 release's cash-flow statement (*"Maturity of short-term investments", "Business
  acquisitions, net of cash acquired", and "Proceeds from mortgage and loans payable"* and the
  subtotals), one day after furnishing it; the 10-Q was not affected. (2) **Interest capitalised
  into construction** rose from $36M (FY2024) to **$79M (FY2025)** and **$70M in H1 2026 alone**;
  it leaves operating cash and sits in capex, which is correct GAAP and moves cost out of the
  operating line during a building boom. (3) **Stock pay capitalised into construction**, $60M,
  $77M, $69M (FY2023-25), appears in neither the expensed SBC nor cash capex. Both are handled at Q4.
- [ ] **Unintelligible footnotes**: not fired; the notes are long and plain.
- [ ] **Filed-figure tells [E4-30]**: not fired. Cash taxes over pretax income 13.6%, 19.0%, 13.7%
  (FY2023-25), explained by REIT status, not falling; growth is not smooth (FY2024 revenue missed
  guidance, net income fell).
- [ ] **Stock-price targeting [E3-50]**: no instance found; the 2024 proxy changes added a cap on
  rTSR payouts when absolute TSR is negative, which runs the other way.

### STEP 3 - THE PRIMARY TEST **[E2-01]**, scoped by **[E2-43]**
Net income over average equity: **3.6%, 4.2%, 5.2%, 6.3%, 3.8%, 4.6%, 6.3%, 8.1%, 6.3%, 9.8%**
(FY2016-25); **ten-year mean 5.8%, five-year mean 7.0%**, with debt of about 1.4x book equity.
Excluding goodwill from the denominator (the [E2-43] direction for an acquisitive filer): five-year
**13.0%**, ten-year **12.4%**. Operating income over average net plant: **9.7% (FY2016) falling to
7.0-8.6% (FY2020-25)**. The primary test asks for *"a high earnings rate on equity capital employed
(without undue leverage ...)"*: five years at 7.0% on book equity, on a leveraged balance sheet, is
not it. [E2-42]'s red light (*"falls much below the return on equity earned ... by American
industry in aggregate"*) is not quantified here because no aggregate figure is on disk; the
[E5-40] yardstick (~12% on retained utility capital *"quite satisfactory"*) is met only on the
goodwill-excluded measure.

### CANDOR - THE HALF-OWNER TEST **[E2-26]**
**Mixed, leaning against.** For: the Audit Committee's conclusion was published in the next
release; the SEC closure was 8-K'd within a day; recurring capex has been published in every AFFO
reconciliation since at least FY2013, so a reader can compute the gap to depreciation; power
pass-through is named when it moves revenue. Against: the public narrative, the guidance and the
pay all run on measures that remove depreciation and stock pay; the filings never state what the
2024 allegations were; and the one sentence that directly answered the maintenance question was
withdrawn in 2025 without a word.

### RATIONALITY IS CAPITAL ALLOCATION
- **Buybacks [E5-08, E4-31]**: none; a REIT that distributes and issues. Not engaged. The mirror
  case is issuance: **shares sold at $657.75-$1,070.52** (forwards settled 2023 and executed 2026).
  Selling stock above intrinsic value is good for continuing owners; below it, costly. Q5's
  computation puts owner-earnings value per share below every one of those prices at the D&A and
  capex-built ends of (c) at any growth rate up to 7%, so **on this run's arithmetic the issuance was
  sold dear, which favours the holders who did not buy it** ([E5-44]'s law read in reverse: the
  paper given was worth less than the cash received).
- **Acquisitions [E3-40, E2-56, E4-39]**: **$9,393M** FY2015-2025 (Telecity 2016, the Verizon data
  centres 2017, Bell Canada's 2020, MainOne and Entel 2022, TIM 2025 and others); goodwill **$5,984M**.
  One visible failure: **Packet (2020), renamed Equinix Metal, wound down in 2024** with part of
  the **$233M** FY2024 impairment (*"as a result of the Equinix Metal Wind Down"*). No acquisition
  post-mortem against the announcement case was found in the filings read ([E4-39]'s
  rare-positive tell absent).
- **Institutional imperative [E2-30]**: (1) resist change: not seen (the CEO, CFO and CAO all
  changed); **(2) projects to soak up funds: a prompt** (capex guidance raised by **$1.4bn** within
  the year and the long-term capex outlook from $3-4bn to $5-7bn a year on AI demand); (3) staff
  studies: no evidence either way; **(4) imitation: the filing states the premise itself**, *"If we
  fail to invest before or contemporaneously with our competitors, our results of operations could
  suffer."* [E2-27] is the corpus's warning about exactly that sentence.
- **Pay in stock to conserve cash**: 8-K of 2025-02-11, the bonus is paid in fully vested RSUs
  because *"This payment in fully vested RSUs for 2025 allows Equinix to retain more cash in the
  business to fund our investments"*. That converts a cash cost into stock pay; [E5-06] counts it
  either way, and Q4 subtracts it in full.

### THE GUARDRAIL
- [x] Nothing here promotes the name; Q2 is closed and a strong Q3 could not repair it
  [E2-37, E2-38, E3-39].
- [x] Key-person dependence: none; the CEO, CFO and CAO all changed in 2024-2026 and the business
  ran on [E4-23].
- [x] No manager is the plan [E2-35, E2-36].

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary**  [ ] OUT  [ ] UNRESEARCHED
  [ ] UNKNOWABLE
  *IN = no disqualifier found, not a finding of honesty [E5-17]. Overlay case. Carried: [E4-29]
  fires at full strength and in the pay; the [E4-27] incentive runs through the recurring/non-
  recurring capex line; the "future capital expenditures remain minor" sentence withdrawn in 2025
  without comment; guidance culture with spending consistently above guide; [E2-49] fires small;
  serial issuance; dividends matched almost exactly by issuance over eleven years [E2-52].*

---
## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the
> queue asks every run for a price and because the (c) question is the one this name was queued
> on; it decides nothing and cannot reopen Q2 [E2-37, E3-39].

### THE SKIP REASON, TESTED ON THE FILING RATHER THAN INHERITED
The wave 5 label is *"capex unresolved [E5-20]: build (c) by hand from the filing"*. The five
checks the dated notes ask for, in order:

**(a) The current `owner_earnings()` prices the name.** On the companyfacts fetched today:
`{'5y_da': 885,930,800, '5y_capex': -559,919,800, '3y_da': 1,028,973,667, '3y_capex': -602,214,000}`.
So on the current screen the label is the AMZN/CL kind of **tooling artefact**: the
`CAPEX_UNRESOLVED` of the 2026-09-01 triage no longer fires. **But the priced numbers are wrong in
two places, below.**

**(b) Early-year facts: a hole of a different kind, a WRONG VALUE rather than a missing one.**
`PaymentsToAcquireProductiveAssets` carries FY2010-FY2025, but for FY2010-FY2013 the values
`annual()` returns are **$14.9M, $28.1M, $24.7M and $74.3M**, which are Equinix's **real estate
purchases** (`PaymentsToAcquireRealEstate` carries the same $24.7M and $74.3M). The same element
also holds **$1,098.6M (FY2012)** and **$696.8M / $572.4M (FY2013)**, the plant figures; `annual()`
keeps one value per year and kept the small one. The screen's owner earnings for FY2010-13
(**+$309M, +$488M, +$523M, +$427M**) are therefore overstated by roughly $1bn a year. They sit
outside every window priced here, but a ten-year-plus window on the screen would be wrong.

**(c) Overlapping capex elements carry DIFFERENT values, and the screen reads only one line of two.**
The face of the cash-flow statement carries two capital lines every year: *"Real estate
acquisitions | ( 994 ) | ( 337 ) | ( 384 )"* and *"Purchases of other property, plant and
equipment | ( 4,311 ) | ( 3,066 ) | ( 2,781 )"* (FY2025 10-K). `CAPX_TAGS` reaches the second
(`PaymentsToAcquireProductiveAssets` = $4,311M, exact) and **never the first**
(`PaymentsToAcquireRealEstate`, $994M in FY2025, $2,878M over FY2015-25). Separately,
`capital_acquired()` **adds** `RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability`
($236M FY2025, non-cash lease additions), which is a legitimate capital addition but a different
one from the cash principal repaid on the same leases (*"Repayments of finance lease liabilities |
( 155 )"*, in financing). **The screen's capex end therefore omits real estate and uses non-cash
lease additions; this run's hand build uses real estate plus the cash lease principal.** The
difference in FY2025 is $994M + $155M - $236M = **$913M** of capital spending the screen's
`5y_capex` end does not see. The hand build is below.

**(d) What the D&A is made of.** FY2025 *"Depreciation, amortization and accretion | 2,066"* (face)
is, from the FFO/AFFO reconciliation and the notes:

| component | FY2025 $M | source |
|---|---:|---|
| **real estate depreciation** (buildings, core systems: electrical and mechanical plant, leasehold improvements, finance-lease buildings) | **1,282** | *"Real estate depreciation | 1,282"* |
| non-real-estate depreciation (internal-use software, 3-5 year life; personal property) | 568 | *"Non-real estate depreciation expense | 568"* |
| amortisation of acquired intangibles (customer relationships) | 200 | *"Amortization expense | 200"* |
| accretion (asset retirement obligations) | about 16 | residual; *"Accretion expense adjustment | 16"* |

**`da_annual()`'s NVDA defect does not bite here**: it returns
`DepreciationAmortizationAndAccretionNet` = $2,066M, the face total, exactly. (The element
`DepreciationDepletionAndAmortization` carries $2,050M, the segment note's total without
accretion.) **90% of the D&A is plant and software; 10% is acquired intangibles**, so unlike SPGI
the band is about plant.

**(e) [E5-20] asked separately, on the filing: YES. Equinix is in the exception class, and the
company's own "recurring" figure points the other way.** Four filed facts:
1. **Capital intensity of a utility.** Gross plant $36,972M against revenue $9,217M (4.0x); capital
   spending (other plant plus real estate) **31.6-57.6% of revenue** every year FY2015-25.
2. **The filer shortened useful lives, twice.** FY2024 10-K: *"approximately $64 million of higher
   depreciation expense driven by IBX data center expansions and acceleration of depreciation
   expense for certain assets with shortened useful lives"* (Americas; $27M and $19M likewise in the
   other regions), and *"We evaluated the estimated useful lives of our property, plant and
   equipment, and made certain revisions to these estimates during the years ended December 31,
   2025 and 2024"* (FY2025 10-K). This is the AMZN trigger in this queue.
3. **The replacement costs more than the original [E4-47].** The year-end tables of projects under
   construction give total project capex per sellable cabinet of **$58.7k (FY2020), $61.3k, $62.2k,
   $80.0k, $101.8k and $126.2k (FY2025)**. Gross plant excluding land and construction in progress
   is **$80.0k per cabinet of capacity** on the books. Depreciation charged on $80k does not renew a
   cabinet that now costs $126k to build. [E4-47]: *"inflation destroys value, but it destroys it
   very unequally"*.
4. **The old plant cannot serve today's customer at the same unit volume.** *"Because many of our
   IBX data centers were built a number of years ago, the current demand for power may exceed the
   designed electrical capacity in these IBX data centers. As power, not space, is a limiting factor
   in many of our IBX data centers, our ability to fully utilize the space in those IBX data centers
   may be impacted"*, and the company is *"considering redevelopment of certain sites"* (FY2025 10-K
   Item 1A; the construction table includes *"MI1 redevelopment | Miami"*, 475 cabinets, $59M).
   Keeping an old building's unit volume is, in [E2-23]'s words, what *"the business requires to
   fully maintain its long-term competitive position and its unit volume"*; the company classifies
   such work as non-recurring.

**So v4's rule applies as written: the D&A end is INVALID, not merely optimistic, and (c) is
judged upward from total capex.** And the company's own measure runs the other way: *"recurring
capital expenditures"* have been **10.9-16.9% of D&A every year FY2016-25** ($284M against $2,066M
in FY2025), a level that would renew the plant roughly once a century. The sentence that justified
it (*"future capital expenditures remain minor relative to our initial investment throughout its
useful life"*) was withdrawn from the filings in October 2025 (Q3).

**Of the seven names now run from this row: ABNB had a real presentation gap, AMZN had no gap, NVDA
a tag gap plus a history gap, CL a tag gap only, SPGI a tag gap plus a (c) question about
acquisitions, TOST a tag gap plus a definition break, and EQIX has NO tag gap now but a
mis-assigned early-year value and a second capital line (real estate) the screen never reads; and
the [E5-20] exception class applies at EQIX, the second name after AMZN.**

### (c): THE DISCLOSED JUDGMENT, BUILT THREE WAYS
*"(c) must be a guess"* [E2-23]. Three routes, FY2021-25, each from filed figures
(`c_triangulate.py`):

| route | (c) a year, FY2021-25 | how |
|---|---:|---|
| the company's "recurring capital expenditures" | **$228M** | AFFO reconciliations; **rejected as (c)**, for the four reasons above and because pay is funded on the metric it feeds (Q3) |
| depreciation only / total D&A (the corpus default, INVALID here as an END, kept as a yardstick) | $1,657M / $1,863M | face of the cash-flow statement |
| **total capex less growth** | **$1,150M to $1,998M** | $17,353M of capital spending, less the cost of **81,800 cabinets of capacity added** (310,500 to 392,300) at the filed project cost of $58.7k-$101.8k a cabinet (0-15% of the added capacity assumed acquired rather than built, because no filing counts it), less **$3,276M** of land and construction in progress bought ahead of use |
| **replacement cost** | **about $2,940M (FY2025)** | FY2025 depreciation excluding intangibles ($1,866M) scaled by the current project cost over the book cost per cabinet ($126.2k / $80.0k = 1.58) |

**Two independent routes (depreciation, and capex less growth) land within the same band, about
$1.2-2.0bn a year. The company's figure is one-seventh of the bottom of it.** The judgment: **(c)
central = total capex less growth, mid-point about $1.6bn a year over FY2021-25 (about $1.87bn at
FY2025's scale, i.e. depreciation excluding intangibles); (c) conservative = replacement cost,
about $2.9bn at FY2025.** Finance-lease principal ($149M a year mean) is added to (c) at both ends,
because it is the cash cost of buildings held on finance leases and sits in financing; stock pay
capitalised into construction ($60M, $77M, $69M FY2023-25) is subtracted too, because it is in
neither the expensed SBC nor cash capex (the TOST treatment).

### OWNER EARNINGS - THE ONE NUMBER **[E2-23]**
Construction (CONVENTION, v4 section VI): operating cash flow, less stock-based compensation, less
(c). Every figure from the filed cash-flow statements (10-Ks FY2017, FY2020, FY2022, FY2025; 10-Qs
Q2 2025 and Q2 2026), never a net-income proxy. SBC resolves for every year on the face and is
subtracted in full [E5-06]; **the screen's `sbc_annual()` max-rule picks $311.0M for FY2020 where
the face says $295.0M** (a P&L element against the cash-flow add-back, the ARM limit in the resume
note); the hand build uses the face.

| $M | FY2016 | FY2017 | FY2018 | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | TTM 2026-06 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| operating cash flow | 1,019 | 1,439 | 1,815 | 1,993 | 2,310 | 2,547 | 2,963 | 3,217 | 3,249 | 3,911 | 3,942 |
| SBC (face) | 156 | 176 | 181 | 237 | 295 | 364 | 404 | 407 | 462 | 498 | 531 |
| D&A (face) | 837 | 1,043 | 1,228 | 1,285 | 1,423 | 1,656 | 1,736 | 1,844 | 2,011 | 2,066 | 2,185 |
| other plant capex | 1,113 | 1,379 | 2,096 | 2,080 | 2,283 | 2,752 | 2,278 | 2,781 | 3,066 | 4,311 | 5,406 |
| real estate | 28 | 95 | 182 | 169 | 200 | 202 | 248 | 384 | 337 | 994 | 1,119 |
| finance-lease principal | 114 | 94 | 104 | 127 | 115 | 166 | 134 | 149 | 140 | 155 | about 155 |
| company "recurring" capex | 142 | 168 | 203 | 186 | 161 | 199 | 189 | 218 | 250 | 284 | 284 |
| **OE, company (c) [displayed, rejected]** | 608 | 1,002 | 1,328 | 1,444 | 1,739 | 1,819 | 2,236 | 2,443 | 2,397 | 2,974 | 2,972 |
| OE, (c) = total D&A [INVALID end] | 27 | 221 | 407 | 471 | 592 | 527 | 823 | 966 | 776 | 1,347 | 1,226 |
| OE, (c) = all capital spending incl. growth | -392 | -304 | -748 | -619 | -583 | -935 | -101 | -564 | -833 | -2,116 | -3,338 |

**MORE THAN ONE WINDOW [E4-25, E4-38], with the judged (c):**

| window | OCF - SBC - lease principal - capitalised SBC | **(c) central: capex less growth** | **(c) conservative: replacement cost** | (display) company (c) | (display) D&A end |
|---|---:|---:|---:|---:|---:|
| **five-year default [E2-42], FY2021-25** | 2,561 | **about $0.96bn** (range $0.56-1.41bn) | **about zero** (-$0.06bn) | $2.37bn | $0.89bn |
| three-year, FY2023-25 | 2,787 | about $1.1bn | about zero | $2.61bn | $1.03bn |
| ten-year, FY2016-25 | about 2,000 | about $0.7bn | slightly negative (about -$0.1bn) | $1.80bn | $0.62bn |
| **FY2025** | 3,189 | **about $1.32bn** | **about $0.25bn** | $2.97bn | $1.35bn |
| TTM to 2026-06-30 | 3,187 | about $1.2bn | about $0.05bn | $2.97bn | $1.23bn |

*(Ten-year and TTM central figures scale route 2 by the D&A of the window; the replacement-cost end
applies the 1.58 ratio to each window's depreciation. Arithmetic in `oe.py` and `c_triangulate.py`.)*

**The combined range on the default window runs from about zero to about $1.4bn, with a central
figure near $1.0bn. It touches zero in words: at replacement cost, the five-year business has
earned approximately nothing for its owners after keeping its plant current.** [E4-25]: *"Usually,
the range must be so wide that no useful conclusion can be reached."*

**Interest income is inside operating cash**: $193M in FY2025 ($137M, $94M before), earned on
cash and short-term investments averaging about $2-3bn; removed at Q5 with the cash.

**Stock compensation**: 12.7% of operating cash in FY2025, 13.4% over FY2021-25, 13.0% over
FY2016-25. Not the ARM/TOST shape; subtracted in full.

**Per share, the SPGI construction.** Owner earnings per diluted share with (c) at
depreciation excluding intangibles (the central level): about **$6.3 (FY2021, $567M on 90.4M
shares)** to **$13.5 (FY2025, $1,323M on 98.1M)**; at the displayed D&A end $5.83 to $13.73.
Diluted shares rose **67.7% FY2015-25** and **11.0% FY2020-25**, so per-share growth runs about a
tenth below total growth over the last five years.

### GREAT, GOOD, OR GRUESOME? **[E4-20, E4-43]**
- [ ] great
- [ ] good
- [x] **gruesome-leaning, on the incremental numbers**
FY2015-2024 Equinix invested **$31.7bn** (other plant $20,695M + real estate $1,884M + acquisitions
$9,142M). Income from operations rose from **$567M (FY2015) to $1,848M (FY2025): +$1,281M, 4.0%
pre-tax on the capital added**; operating income plus D&A rose **$2,822M, 8.9%**, before any
maintenance. New senior notes in 2026 carry **4.40%, 4.70%, 3.95% and 4.75%** coupons (8-Ks of
2026-03-05 and 2026-05-07). [E4-20]'s gruesome account *"both pays an inadequate interest rate and
requires you to keep adding money at those disappointing returns"*; [E4-43] passes the good class
at roughly 20% pre-tax on net tangible assets. A 4% incremental operating return on a programme
the company now guides at **$5-7bn a year** is on the gruesome side of that line, on this run's
(c). On the company's own AFFO view it looks good; that view is the one Q3 and (c) above decline.

### STAYING POWER - score all three **[E5-11]**
- **(1) A large and reliable stream of earnings: YES.** Recurring revenue above 90% of the total,
  contracts of 1-5 years renewing annually, operating cash $3.9bn, no customer above 3% of recurring
  revenue.
- **(2) Massive liquid assets: NO.** **$2,224M** of cash and short-term investments at 2026-06-30
  (*"Cash and cash equivalents | $ | 979"*, *"Short-term investments | 1,245"*) against about
  **$19.7bn** of senior notes and loans (and $3.0bn more issued 2026-08-06). The $4.0bn revolver is a
  bank line and [E5-39] does not count it (*"We will never be dependent on the kindness of
  strangers"*).
- **(3) No significant near-term cash requirements: NO.** 2026: **$4,912M** of purchase commitments
  (*"primarily for real estate purchases, IBX infrastructure equipment not yet delivered and labor
  not yet provided"*), **$1,317M** of debt maturities, and **about $2,039M** of expected dividends
  (release of 2026-07-29), against operating cash of about $3.9bn. 2027: $1,995M of commitments and
  $1,764M of maturities. The gap is financed by the bond and equity markets every year.
- **Score: 1 of 3.** **Leverage, named and quantified [E4-16, E3-29]:** about $19.7bn of notes and
  loans plus $2.3bn of finance leases and $1.4bn of operating leases, against Adjusted EBITDA of
  $4.5bn; maturities spread **$1.3-2.7bn a year** to 2030 and **$9.6bn thereafter**. **[E2-54]'s
  coverage test, run as written:** cash interest ($448M paid + $79M capitalised = $527M) against
  operating cash before interest ($4,359M) net of ample capital expenditure ((c) central $1.87bn +
  lease principal $0.16bn): **$2.34bn, 4.4x covered**; at replacement-cost (c), **$1.26bn, 2.4x**.
  The interest is comfortably met. **[E3-52] terms**: the debt is fixed-rate senior unsecured notes
  across seven currencies, not covenanted bank debt due next year.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**
**The mechanism: the capacity race, paid for twice.** Named in the company's own words in its
newest filing: *"if the market was to experience an event of excess data center capacity,
capacity originally developed to serve wholesale or hyperscale requirements could be redirected
toward the enterprise colocation markets in which we operate, increasing available supply and
intensifying competition and pricing pressure in our core business"*, and *"certain network, cloud
and content providers may seek to offer connectivity and interconnection through alternative models
that bypass colocation environments"* (10-Q for Q2 2026, `0001101239-26-000147`; both sentences
new in that filing). [E2-27]: *"viewed collectively, the decisions neutralized each other and were
irrational ... After each round of investment, all the players had more money in the game and
returns remained anemic."* The filing itself states the premise that forces the race: *"If we fail
to invest before or contemporaneously with our competitors, our results of operations could
suffer."*

**Quantified from filed figures.** The business earns its central owner earnings of about $1.3bn
(FY2025) on $9.2bn of revenue. **Each 1% of recurring revenue lost to price is about $87M**
($8,739M x 1%). A 5% price concession across recurring revenue (the Americas MRR per cabinet rose
only 11.6% in five years, so 5% is less than half a decade of increases) removes about **$437M, a
third of central owner earnings**. At the same time the **$4.9bn of 2026 purchase commitments**
cannot be cancelled, the dividend (**$2.0bn**, *"Dividend per Share Growth ... Approximates AFFO per
Share Growth"*) already exceeds central owner earnings, and the replacement-cost (c) says the plant
already absorbs most of what is left. **The business does not go broke: fixed-rate long-dated notes,
4.4x interest cover, an investment-grade issuer.** **It dies as an investment the way [E2-27]
describes: more money in the game each round and the return anemic**, with the owner's dividend
financed by new owners.

- Survival shapes (`Screens/SURVIVAL SHAPES - index.md`): **#6 THE BORROWED BALANCE SHEET** (the
  business runs on other people's money it must keep rolling: $11.1bn of equity raised FY2015-25
  and senior notes outstanding grown to $18.4bn at FY2025, funding plant, dividends and
  acquisitions), with **#11 THE PASS-THROUGH**
  (gains of the capacity race passed to customers) as the mechanism and **#1 CONTRACTED NOT TO STOP**
  ($8.4bn of purchase commitments) as a feature. **No new shape is proposed**: the distinctive thing
  here (renewal at current cost booked as growth, and a dividend set by a measure that excludes it)
  is a (c) finding, recorded above, not a new way to die.
- **Exposure, not experience [E4-40]:** the filed record (FY2015-25) is a decade of rising demand
  ending in an AI build-out; the company's new oversupply sentence is about exposure the record has
  not yet shown.
- **Likelihood: [ ] likely [x] a real possibility [ ] a low-level possibility** for a price-led
  compression of returns in colocation (the company added the risk sentence in its latest filing);
  **a low-level possibility** for insolvency.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on survival**  [ ] OUT  [ ] UNRESEARCHED
  [ ] UNKNOWABLE
  *It survives: 4.4x interest cover on central (c), long-dated fixed-rate debt, reliable recurring
  revenue. But staying power scores 1 of 3, the incremental return is about 4% pre-tax, and on the
  five-year default window the owner-earnings range runs from about zero (replacement-cost (c)) to
  about $1.4bn, central near $1.0bn: at the bottom, [E4-25]'s "no useful conclusion".*

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
*Q5 does not open: Q2 is OUT. The arithmetic below is recorded because the queue asks every run for
a price, and it carries no entry language. It is not a ranking and it arms nothing.*

**The pair:** price **US$1,025.94**, the **2026-09-17 close** (Yahoo daily chart, aggregator,
flagged; 2026-09-18 had not closed) x **98,671,686 shares** (10-Q cover, accession
`0001101239-26-000147`, as of 2026-07-28; one class) x split factor **1.0** = **market
capitalisation US$101,231.2M**. Less **$2,224M** of cash and short-term investments at 2026-06-30
= **US$99,007.2M** for the business. **Sovereign USD 30-year 5.29%**, US Treasury daily par yield
curve, the issuing authority, **09/17/2026**. With the 465,000 forward shares settled: cap
$101,708.3M against $498M of cash to be received, a 0.0% change in the yields below to one decimal.

Owner earnings are levered (operating cash is after interest paid), so no debt is added to the cap;
interest income ($193M FY2025, $93M five-year mean) is removed and the cash carried separately, so
it is counted once.

| construction | owner earnings | yield, business ex-interest | vs 5.29% | perpetual growth needed to reach ~10% |
|---|---:|---:|---:|---:|
| **central (c), five-year default FY2021-25** | **$961M** | **0.88%** | **-4.41 pts** | **9.1%** |
| **central (c), FY2025** | **$1,323M** | **1.14%** | **-4.15 pts** | **8.9%** |
| conservative (c) (replacement cost), FY2025 | $246M | 0.05% | -5.24 pts | 10.0% |
| conservative (c), five-year | about -$57M | negative | | not computable |
| *display:* D&A end FY2025 (INVALID end in this class) | $1,347M | 1.17% | -4.12 pts | 8.8% |
| *display:* the company's own (c), FY2025 (rejected at Q4) | $2,974M | 2.81% | -2.48 pts | 7.2% |
| *display:* the company's AFFO, FY2025 | $3,761M | 3.60% | -1.69 pts | 6.4% |

**1. THE YIELD.** On the central (c): **0.9% (five-year) to 1.1% (FY2025)** against a sovereign of
**5.29%**. **Even on the company's own maintenance figure, rejected at Q4, the yield is 2.8%; even
on AFFO, the company's own headline measure, it is 3.6%. No construction on disk, the company's
included, reaches the bond.**

**2. WHAT THE PRICE ALREADY ASSUMES.** From FY2025's central owner earnings, about **8.9% a year of
growth in perpetuity** to reach the ~10% floor, and about **4.2%** merely to match the bond. **What
the business has actually done**: owner earnings per diluted share at the central level rose from
about $6.3 (FY2021) to $13.5 (FY2025); on the company's own measure AFFO per share rose 9% in FY2025
and is guided at 9-12% a year to 2029. [E4-35]'s base rate is the burden: fewer than one in twenty of
the best businesses sustain 15% for twenty years, and this case needs about 9% forever **on top of
a capital programme of $5-7bn a year that consumes more cash than the business makes** (Q4). **[E4-44]
and [E2-63] are the binding bounds**: value cannot outgrow earnings, and growth here is bought with
new capital at about a 4% incremental pre-tax operating return (Q4), which [E2-63]'s *"unless more
capital is continuously invested"* describes exactly.

**3. WHAT YOU ARE PAID.** **Minus 4.1 to minus 4.4 points against the sovereign** on the central (c);
minus 1.7 points on the company's own AFFO.

**Certainty is not priced in the rate [E3-42].** Sovereign used 5.29%, bare. No per-name premium.

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-01]**
Value per share = (owner earnings less interest income) / (0.10 - g), plus the $2,224M of cash,
over 98.67M shares:

| owner earnings | g = 3% | g = 5% | g = 7% | g = 8% |
|---|---:|---:|---:|---:|
| **central (c), FY2025 ($1,130M ex-interest)** | $186 | $252 | $404 | $595 |
| central (c), five-year ($868M ex-interest) | $148 | $198 | $316 | $462 |
| *display:* company (c), FY2025 ($2,781M ex-interest) | $425 | $586 | $962 | $1,432 |

**Value, in round numbers: roughly $200 to $400 a share** on the central (c) at 3-7% perpetual growth.
**Current price: $1,025.94, above the whole range**, and reached only by granting the company's own
maintenance figure AND about 7% growth forever. **At the conservative (c) no value can be computed
on the five-year window.**

**Which bar:** the screamer test [E4-01] only, because the file is closed and no margin is applied.
The conservative end is about zero; the price is above every construction but the company's own at
7%+ growth. **Above the whole range.** **Windage count: ONE** ((c) judged up from total capex, with
the replacement-cost end shown as the conservative bound rather than spent as a second margin; the
growth rates are displayed, not chosen).

- **VERDICT: none. Q5 did not open (Q2 OUT).** Had every gate been IN, the computation shows a
  0.9-1.1% business yield against a 5.29% sovereign and a ~10% floor [E4-28]: below both, **FAIL** on
  price as well, on every construction including the company's own.

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

> **RECORDED, NOT GOVERNING.** Nothing is owned and nothing is armed. These are the conditions on
> which the file would be REOPENED at Q2 [E1-02]; a Q2 OUT is a finding about the business, so a
> price alert would be a category error (the QLYS ruling, 2026-09-07).

**What would reopen Q2 (each observable in a filing):**
1. **Returns on plant that rise while the plant grows.** Operating income over average net plant
   back above its FY2015-19 level (**9.6-10.7%**) and rising for three consecutive 10-Ks, with
   capital spending at the $5-7bn guided pace. That is [E3-03]'s *"thereby to earn high rates of
   return on capital"* and [E3-46], which the FY2020-25 record (7.0-8.6%) does not show.
2. **Price that outruns build cost.** The Americas *"MRR per Cabinet"* (FY2025 $2,694) rising faster
   than the project cost per sellable cabinet in the year-end construction table (FY2025 $126.2k),
   for three years: the evidence that customers pay for the ecosystem and not merely for space and
   power.
3. **The interconnection toll holding its price as the bypass risk arrives.** Interconnection revenue
   per interconnection (about $3,370 a year in FY2025, +4.7%) continuing to rise, and the Q2 2026
   10-Q's new sentence about providers who *"bypass colocation environments"* not turning into a
   named decline in a later 10-K.
4. **A maintenance disclosure that meets the corpus's (c).** A filed statement of the capital
   required to keep existing buildings at current power density and unit volume, whatever the
   company calls it, against which [E2-23]'s (c) can be read directly rather than triangulated.

**Thesis-confirming (for the OUT):** project cost per cabinet rising faster than MRR per cabinet;
cabinet utilisation (Americas 79%, EMEA 76%, Asia-Pacific 73% at FY2025) falling as capacity is
added; the oversupply and bypass sentences moving from risk factors into the MD&A's explanation of
results; dividends continuing to exceed owner earnings with issuance and debt filling the gap.

**Next dated documents:** the Q3 2026 10-Q and earnings release (late October 2026), the FY2026 10-K
(February 2027, which will carry the FY2026 useful-life review and the next construction table), and
the 2027 proxy (whether AFFO per share remains the bonus metric).

**Position size:** none. **VERDICT (RECORDED, NOT GOVERNING): not applicable; the file closed at Q2
and the reopening conditions are recorded above.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN → **Q2 OUT, the file closed**; Q3-Q6
  recorded beneath explicit RECORDED, NOT GOVERNING banners, as at TOST and NVDA.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the
  filed segment note and property note. The row's PROVISIONAL cells (private operators) are named at
  Q2 and are not what closes the gate.
- [x] No UNRESEARCHED verdict was returned; the unnumbered peer cells name their artefacts.
- [x] No UNKNOWABLE verdict was returned.
- [x] Step 0: the filing was read with accession numbers; four figures on the face of the FY2025
  cash-flow statement cross-checked to companyfacts, one of which exposed the capex line the
  screen does not read.
- [x] Owner earnings on multi-year windows (five-year default, three-year, ten-year, FY2025, TTM),
  hand-built from the filed cash-flow statements; (c) disclosed as a judgment built three ways, the
  company's figure displayed and rejected with reasons, the D&A end kept only as a yardstick because
  v4 makes it INVALID in the exception class.
- [x] Competitor row filled from filings, with what could not be numbered stated.
- [x] Sovereign for the reporting currency (USD), from the issuing authority, dated 09/17/2026,
  re-struck by this run; the non-USD share of earnings named.
- [x] Value stated as a round-number range under a COMPUTATION — NOT A CLEARANCE heading.
- [x] One bar (the screamer test); windage count one.
- [x] Price dated as a close, aggregator flagged; no primary-filing price in the window, recorded as
  a limit.
- [x] Run committed to git after every gate, with a pathspec.
- [x] Every ledger id cited was checked to exist in `principle_ledger.csv` before it was written.
- [x] No em dashes in anything this run wrote (the template's own headings and the required
  `COMPUTATION — NOT A CLEARANCE` heading carry them).
- [x] Never presented as proven to beat the market; nothing here claims it.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **DATED CORRECTION, 2026-09-18, to Step 0 (the price cross-check). Step 0 says *"EDGAR shows no
   Form 4 after 2026-08-06 with a transaction price in September"* and records the cross-check as a
   limit. That was written without querying the Forms 4, and it is wrong.** EDGAR, re-queried at the
   audit, carries Forms 4 of 2026-09-03 (`0001101239-26-000152`) and 2026-09-08
   (`0001101239-26-000153`), reporting person Michael Shane Paladin: open-market sales on
   **2026-09-02 at $1,008.0191 and $1,018.43**, and on **2026-09-04 at $1,035.01**. The Yahoo bars
   are 09-02 low $1,002.24 / high $1,025.61 and 09-04 low $1,031.26 / high $1,048.34. **All three
   filed prices sit inside the filed days' ranges: the aggregator series IS corroborated by a primary
   document, as at TOST.** Step 0 is left as written (operator rule 6); this note governs.
2. **Q4 draft arithmetic, corrected before commit.** The three-year, ten-year and TTM rows of the
   windows table and the per-share line were first written from a scaling I had not run; recomputed
   from `oe.py` before the section was committed. Nothing wrong reached a commit.
3. **A heredoc containing apostrophes failed** while writing Q2 (the environment limit the brief
   names); nothing was appended by the failed call, which was verified before the section was
   rewritten through a file.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **The five capex checks were framed as tag questions, and EQIX's problem was not a tag.** The
   current screen prices EQIX (no `CAPEX_UNRESOLVED`); the defects are (i) the same element holding
   different values in FY2010-13, where `annual()` kept the real-estate figure and dropped the plant
   figure, and (ii) **a second capital line on the face, "Real estate acquisitions", that no
   `CAPX_TAGS` element reaches** ($994M in FY2025). "Check whether overlapping capex tags carry
   different values" would not have found (ii); reading the face of the statement did.
2. **The short-seller characterisation is the brief's, not the filings'.** The brief says the 2024
   report was *"about AFFO and maintenance capex"*. No Equinix filing names the allegations beyond
   *"certain allegations related to components of our operating results and other strategic
   matters"*, and the report itself is not a filing. Recorded as unverified at Q3; the (c) judgment
   was made on the filed capex record, independently of what the report said.
3. **The brief's hypothesis that the company's recurring capex is "ITS definition of maintenance"
   was right, and the brief under-stated how far it sits from the corpus's**: 11-17% of D&A for ten
   years, the lowest ratio in the filed row (Digital Realty's is 18-20%), justified until October
   2025 by a sentence the company then withdrew.
4. **The brief did not anticipate the [E5-20] exception class applying.** It listed the six prior
   names and that the class had applied at AMZN alone; here it applies (shortened lives, project cost
   per cabinet doubled, old buildings short of power).
5. **The REIT routing note** pointed at a sector method that does not exist; the brief said so and
   was right. Recorded at Step 0.
6. **The "SKIPPED WITH A REASON" section of the queue** says of this row *"the only available
   construction is the D&A end and the corpus calls it INVALID for this class"*. For EQIX today both
   ends price on the screen; what is wrong is the capex end's completeness, not its availability.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`tools/sources.price()` returns an intraday `regularMarketPrice` stamped with today's date** while
  its docstring says *"Latest close."* Reproduced on a second name (TOST, then EQIX at 17:40 UTC).
- **`floor_screen.CAPX_TAGS` does not reach `PaymentsToAcquireRealEstate`.** For a filer that splits
  real estate from other plant on the face (EQIX; possibly every data-centre REIT, DLR next in the
  queue), the capex end omits a real capital line. Adding the element would change a number, so it
  is a proposal for the operator, not a fix made here.
- **`floor_screen.annual()` keeps one value where one element carries several for the same year**
  (EQIX FY2012: $24.7M and $1,098.6M), and here kept the wrong one. Harmless inside five years;
  wrong for any longer window.
- **`capital_acquired()` adds non-cash finance-lease additions** where the cash cost is the lease
  principal in financing; the two differ ($236M against $155M in FY2025). A judgment, disclosed.
- **`sbc_annual()` max-rule** picks $311.0M for FY2020 against $295.0M on the face (the ARM-type
  limit in the resume note). Conservative in direction.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**Price the company's maintenance claim against its own construction table.** Equinix publishes,
every year, the capex and sellable cabinets of each project under construction. Dividing one by the
other ($58.7k per cabinet in FY2020, $126.2k in FY2025) against the book cost per cabinet ($80.0k)
turned an argument about "recurring" capex into an observed replacement cost, from the filer's own
page. Any builder of plant that publishes a project table can be tested the same way.

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** EQIX FAILS AT Q2 (OUT, on [E3-03]'s demonstration clause and [E3-46]: the best
  return on plant in the filed row, about 1.6x Digital Realty's, but about 8-9% pre-tax on net plant
  and falling for a decade; [E2-44](2) fails outright on capex of 32-58% of revenue; [E4-04] engaged,
  the plant is replaced at twice the unit cost). Q1 IN; Q3 IN on the binary (recorded; SEC closed its
  inquiry without action; [E4-29] in the pay; the capex-minor sentence withdrawn in 2025; dividends
  matched by issuance over eleven years); Q4 IN on survival (recorded; [E5-20] exception class
  applies; five-year owner earnings about zero to $1.4bn, central about $1.0bn; staying power 1 of 3);
  price $1,025.94 x 98,671,686 = $101.2bn, headed COMPUTATION — NOT A CLEARANCE: 0.9-1.1% business
  yield against a 5.29% sovereign; Q6 arms nothing.
- Work order: none. UNKNOWABLE: none.

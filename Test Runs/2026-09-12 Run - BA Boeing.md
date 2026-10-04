# Company Run — The Boeing Company (BA) — 2026-09-12
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

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never a
forecast **[E4-15, E3-32]**:
- rate **5.35%** · date **2026-09-11** (the most recent published print; the 2026-09-12 curve
  is not yet posted) · source **US Treasury daily par yield curve, 30-year par yield**, struck
  directly from `home.treasury.gov/.../daily-treasury-rates.csv/2026/all` for this run. The
  adjacent tenors on the same print: 20-yr 5.38%, 10-yr 4.96%. FRED DGS30 not used; the
  Treasury is the issuing authority.
- FX / ADR: none. Boeing reports in USD and earns predominantly in USD (commercial aircraft
  are priced in dollars worldwide), so the earnings currency and the quote currency agree.

**Price and share count, re-struck by this run — the queue's cap is not taken on trust:**
- price **$210.45**, close of **2026-09-11**, Yahoo Finance — *aggregator, used for the live
  quote only and flagged as such* (operator rule 5).
- shares **790,370,020**, read off the **cover of the 10-Q for the period ended 2026-06-30,
  filed 2026-07-28, accession 0001628280-26-050038** (`Screens/cover_shares.py BA`, single
  class, undimensioned).
- **market cap = 790,370,020 × $210.45 = $166,333M.** The queue row carried $165,440M; the
  difference is 0.5% and is a price-date difference, not a count error. **The queue's cap
  survives the re-strike here** — but see the dilution note at Q4: the count itself has moved
  31% in seven years, and $5,750M of mandatory convertible preferred sits on top of it.

**The filing was read** — not tagged data **[E3-27]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **primary document: FY2025 Form 10-K, period 2025-12-31, filed 2026-01-30, accession
  0001628280-26-004357** (`ba-20251231.htm`).
- **secondary: Form 10-Q, period 2026-06-30, filed 2026-07-28, accession 0001628280-26-050038**
  — the newest periodic filing, and it changes the reading materially (see Q4).
- also read: FY2024 10-K (acc 0000012927-25-000015), FY2023 10-K (0000012927-24-000010),
  FY2022 10-K (0000012927-23-000007), FY2020 10-K (0000012927-21-000011), FY2018 10-K
  (0000012927-19-000010), FY2015 10-K (0000012927-16-000099) for the delivery and
  reach-forward series; DEF 14A filed 2026-03-06 (0001193125-26-096787).
- **figure cross-checked against the filed statement:** FY2025 net cash provided by operating
  activities. XBRL `NetCashProvidedByUsedInOperatingActivities` = $1,065M; the Consolidated
  Statements of Cash Flows in the FY2025 10-K reads **"Net cash provided/(used) by operating
  activities 1,065"**. Agrees. Two further cross-checks: total backlog **$682,207M** (MD&A
  table and the remaining-performance-obligation note agree), and **Advances and progress
  billings $59,404M** (balance sheet and contract-liability note agree).
- **A THIRD CROSS-CHECK THAT DID NOT AGREE, and it is a finding of this run.** The cash-flow
  statement carries a non-cash add-back the screen never saw: **"Treasury shares issued for
  401(k) contribution — 1,530 / 1,601 / 1,515"** (FY2025 / FY2024 / FY2023). This is employee
  compensation settled in Boeing stock, added back to operating cash flow beside the $426M of
  "Share-based plans expense". XBRL surfaces it only for FY2010-12 and FY2020
  (`StockIssuedDuringPeriodValueEmployeeBenefitPlan`); for every year since FY2021 it exists
  **only in the filed statement**. See the defect note at Q4.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Three businesses under one roof,
and they do not make money the same way.

**BCA (Commercial Airplanes, 46% of FY2025 revenue).** Boeing takes an order years ahead,
collects a deposit and staged progress payments while it builds, and collects the balance at
delivery. Revenue is recognised at delivery for most commercial programmes. The cost side is
the hard part: a new programme spends billions before the first unit is sold, and the early
units cost far more to build than the late ones. Boeing therefore does not book the cost of
the unit it just built — it books **the average cost it expects over an estimated number of
future units, the "accounting quantity"**, and capitalises the difference. The filing names
the mechanism itself: *"The accounting quantity is our estimate of the quantity of airplanes
that will be produced for delivery under existing and anticipated contracts … It is a key
determinant of the gross margins we recognize on sales of individual airplanes throughout a
program's life."* When expected lifetime cost rises above expected lifetime revenue, the whole
future loss is recognised at once — a **reach-forward loss**. So the earnings line is a running
estimate of a decade of future costs, revised quarterly, and **the cash line is the only thing
that is not an estimate.** This is why the framework's one number is the right number here and
why reported earnings are not.

**BDS (Defense, Space & Security, 30%).** Cost-type and fixed-price contracts with the US
government and foreign militaries; revenue accrues over time as costs are incurred. The
fixed-price development contracts are the ones that bleed: KC-46A, T-7A, VC-25B, MQ-25,
Starliner. BDS lost money in each of FY2023, FY2024 and FY2025.

**BGS (Global Services, ~23%).** Spare parts, maintenance, modifications, training and (until
2025) digital aviation software. This is the aftermarket leg and it is the only one that
reliably earns: 17-18% operating margins in FY2023-24.

**The money, therefore, comes from three places and only one is a business in the ordinary
sense.** (1) Selling aircraft at a gross margin set by a decade-long cost estimate. (2)
Servicing the installed base at a real margin. (3) **Being paid before the work is done.** The
third is not a footnote: **customers had $59,404M of advances and progress billings with
Boeing at 2025-12-31**, against $10,921M of cash. Boeing is financed by its customers on a
scale that dwarfs its own equity.

**The scarce input this business controls.** Not a factory, not a patent, not a brand — it is
**a type certificate and the installed base that flows from it.** A certified narrowbody
airframe, the pilot type ratings tied to it, the airline maintenance organisations built
around it, and the 9,240 cumulative 737 deliveries whose operators now need parts. **And the
filing states that Boeing does not control the rate at which it may use it:** the FAA cap on
737 production (Q2). The scarce input is controlled jointly with a regulator.

**Will the fundamentals look broadly the same in ten years?** The demand side, yes: air
traffic grows, aircraft have 25-year lives, and two airframers certify large commercial jets.
The Boeing-specific fundamentals, **no** — and the filing says so. FY2025 carried $5,283M of
new reach-forward losses on 777X and 767; FY2024 carried $4,079M; FY2020 carried $6,493M on
777X alone. A programme whose accounting quantity and delivery date have moved every year for
six years is not "relatively simple and stable in character."

**And here is the [E4-46] test, asked honestly.** Is this a named filing inside an understood
business, or a business that would take months of study? I can state the unit economics, name
the scarce input, and read the cash. The mechanism is complicated but it is not opaque: the
filing discloses the accounting quantity, the deferred production cost, the reach-forward
losses by programme and the customer advances, each as a number. **Q1 is IN, and it is IN on
the cash line rather than the earnings line** — the thing I claim to understand is that
Boeing's reported earnings are an estimate of the next decade and its operating cash flow is
not. That is enough to carry the later questions.

**The delivery and revenue series, filed, because [E4-55] has a real physical series here**
(BCA deliveries including intercompany, from the 10-Ks named at Step 0):

| FY | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **BCA deliveries** | 648 | 723 | 762 | 748 | 763 | **806** | 380 | 157 | 340 | 480 | 528 | 348 | **600** |
| **Total revenue $M** | 86,623 | 90,762 | 96,114 | 93,496 | 94,005 | **101,127** | 76,559 | 58,158 | 62,286 | 66,608 | 77,794 | 66,517 | 89,463 |

**Read the two rows together and the [E4-55] shape is there.** FY2025 units are **74% of the
FY2018 peak**; FY2025 dollars are **88%** of it. Seven years on from the peak the physical
series has not recovered, and the dollar series is closer to recovered than the unit series
is. [E4-55] is explicit that this is how a shrinking franchise hides — *"a serious reverse, not
likely to disappear in some 'bounce back' effect"* — and that the physical series is the honest
one. The counter-reading, stated fairly: mix moved toward widebodies and inflation ran through
prices, so part of the gap is legitimate. Both readings are carried; the unit series is the one
Q2 is scored against.

**Segment record, filed (FY2025 10-K MD&A):**

| $M | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| BCA revenue | 33,901 | 22,861 | 41,494 |
| **BCA operating result** | **(1,635)** | **(7,969)** | **(7,079)** |
| BCA margin | (4.8)% | (34.9)% | (17.1)% |
| BDS revenue | 24,933 | 23,918 | 27,234 |
| **BDS operating result** | **(1,764)** | **(5,413)** | **(128)** |
| BDS margin | (7.1)% | (22.6)% | (0.5)% |
| BGS revenue | 19,127 | 19,954 | 20,923 |
| **BGS operating result** | **3,329** | **3,618** | **13,474** |
| BGS margin | 17.4% | 18.1% | **64.4%** |

**The 64.4% is not a margin, and the filing says so in its own words:** *"BGS earnings from
operations in 2025 increased by $9,856 million compared with 2024, primarily due to a 2025
gain on the Digital Aviation Solutions Divestiture of $9,566 million."* Strip it and BGS
earned $3,908M on $20.9bn, an 18.7% margin — in line with FY2024. **Strip it from the company
and FY2025's positive net income of $2,235M becomes a loss of roughly $7.3bn.** The one
positive year in the queue's series is a disposal, not a business. This is [E4-41] on the
nose: the corpus's only pro-forma that ever disclosed earnings too *high* — *"about $500
million less than we actually reported"* — and the favourable exogenous break is named and
removed before the mean is trusted. **It is removed here at the earnings line; it never
entered the cash line**, because the $9,672M "Gain on dispositions, net" is subtracted out in
the operating section and the $10,585M of proceeds sits in investing. So the owner-earnings
arithmetic below is already clean of it — which is itself the argument for the cash
construction.

- **VERDICT: [x] IN**
  *IN on the ground that the unit economics, the scarce input and the accounting mechanism are
  all statable from the filing, and the cash line is readable without management's estimates.
  Not IN on the ground that the business is stable — it is not, and that finding is carried
  forward to Q2 and Q4 rather than used to close Q1.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

### FIRST, THE CASE AT FULL STRENGTH — the prior I was asked to attack, built to be worth attacking

**The duopoly case, and it is a real one.** Two companies on earth hold type certificates for
large commercial jet aircraft in volume. An airline that has standardised on the 737 has
bought type ratings for its pilots, tooling and manuals for its maintenance organisation,
spares pools, simulators and gate infrastructure around that airframe; switching means
retraining crews and rebuilding a maintenance base. The order book is contracted a decade
out: **$682,207M of total backlog at 2025-12-31, of which BCA $567,290M**, which the filing
says converts *"approximately 13% … through 2026 and approximately 55% through 2029, with the
remainder thereafter."* The installed base is 9,240 cumulative 737 deliveries and 1,249 787s,
each of which needs parts, checks and modifications for twenty-five years, and BGS earns
17-19% margins servicing them. A new entrant needs a decade, tens of billions and a
regulator's signature before it sells one aircraft. **[E3-03] criterion (1) — needed or
desired — passes without argument. Criterion (2) — no close substitute — passes for the
installed base and passes narrowly for new sales.**

That is the case. It is genuinely strong, and it is why the prior in the brief was IN NARROW.

### NOW THE ATTACK — and the filing supplies every weapon

**[E3-03] CRITERION (3) FAILS ON THE FILING'S OWN WORDS, AND IT FAILS IN THE HARDEST WAY.**
Criterion (3) is *"is not subject to price regulation."* Boeing's problem is worse than price
regulation: **its output volume is set by a regulator.** The FY2025 10-K says it twice, in
two separate parts of the document, in the same sentence:

> **"Since the 737-9 door plug accident in January 2024, the 737 program may only increase
> production rates and/or implement new production lines with the concurrence of the FAA."**
> — FY2025 10-K, Critical Accounting Estimates; the same sentence appears in Item 1 as *"The
> 737 program may only increase production rates and/or implement new production lines with
> the concurrence of the FAA."*

And the operative history, filed: *"Throughout 2025, the rate recovered from below 38 aircraft
per month at the beginning of the year to 42 per month during the fourth quarter. **In October
2025, after extensive reviews of the key performance indicators (KPIs), the FAA and Boeing
jointly agreed** the KPIs and rate readiness process guided by our Safety Management System
supported an increase of the 737 production rate to 42 per month. The program plans to
increase the production rate from 42 to 47 in 2026 **with the concurrence of the FAA**."*

**[E2-59] is the exact corpus row for this, and it cuts against Boeing rather than for it.**
[E2-59] says administered pricing can *floor* a commodity business's profits — the regime,
not the company, owns the moat, and *"That day is gone"* is how it ends. Boeing has the
mirror image: **an administered CEILING on volume.** The framework's own formulation is that
regulation *caps* a franchise ([E3-03] criterion 3) and *floors* a commodity business, and
**neither creates the class.** Here it caps. The most profitable single act available to
Boeing's commercial business — build more 737s, the one programme that works — requires a
government agency's agreement, renewed at intervals, on evidence about defect rates. That is
not a franchise attribute; it is the opposite of one.

**[E3-03] criterion (3) therefore FAILS as filed.**

### [E2-44] — BOTH HALVES, AND BOEING ANSWERS THE FIRST HALF ITSELF

**Half one: can it raise prices even when demand is flat and capacity is not fully utilised?**
The company's own words, in the MD&A, twice in the same document, about two different
segments:

> **"This market environment has resulted in intense pressures on pricing and other
> competitive factors, and we expect these pressures to continue or intensify in the coming
> years."** — FY2025 10-K, BCA Business Environment and Trends

> **"Aviation services is a competitive market with many domestic and international
> competitors. This market environment has resulted in intense pressures on pricing, and we
> expect these pressures to continue or intensify in the coming years."** — the same 10-K, BGS

**A company with no close substitute does not describe its own market that way, and it
certainly does not forecast the pressure intensifying.** This is [E2-44] answered in the
negative by the subject, in a document signed under penalty. **Boeing is taking price, not
setting it.**

**Half two: can it grow dollar volume with only minor additional investment of capital?** No,
and the numbers are large. Capex ran $2,942M in FY2025 against $1,953M of depreciation, and
$2,008M in the first half of 2026 alone. Research and development ran $3,180M in FY2025
(BCA $2,202M). And the capital that matters most is not on the capex line at all: **$11,777M
of deferred production costs on the 737 and $13,859M on the 787** — costs already spent,
capitalised, and recoverable only if enough future units are built and sold. Of the 787
total, **$2,198M "are expected to be recovered from units included in the program accounting
quantity that represent expected future orders"** — $2.2bn of spent cash whose recovery
depends on orders that do not exist yet.

**[E2-44] FAILS on both halves.**

### [E4-37] — THE AGONY METRIC, AND IT IS QUANTIFIED ON THE BALANCE SHEET

[E4-37] says you can *"almost measure the strength of a business over time by the agony they
go through in determining whether a price increase can be sustained"* — and *"it's not a great
business when you have to have a prayer session before you raise your prices a penny."*

**Boeing is past the prayer session. It is paying its customers.** Filed, all of it:

| the agony, filed | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| concessions paid in cash to 737 MAX customers (MD&A) | $0.4bn | $0.9bn | $0.2bn |
| 737-9 customer considerations reducing revenue | — | $443M | — (absent) |
| **accrued "Other customer concessions and considerations"** (balance sheet) | | **$1,552M** | **$1,696M** |
| **accrued "Forward loss recognition"** (balance sheet) | | **$7,634M** | **$6,711M** |

And the pricing mechanism itself, from Critical Accounting Estimates: *"The sales prices for
all undelivered units within the accounting quantity include an escalation adjustment for
inflation that is updated quarterly, **as well as customer consideration driven by delivery
delays.**"* **Boeing's own forward price assumption is net of money it expects to pay
customers for being late.** That is the MRVL customer-warrant finding at a hundred times the
scale: this is not a franchise extracting rent from a captive base, it is a supplier
compensating a captive base for failing it.

### THE REACH-FORWARD LOSSES — the instrument the brief named, and it fires

A reach-forward loss is the filing's own admission that a programme will lose money over its
entire remaining life. The filed record:

| programme | FY2020 | FY2024 | FY2025 |
|---|---|---|---|
| 777X | $6,493M | $3,499M | **$4,899M** |
| 767 | — | $580M | $384M |
| BDS five largest fixed-price development programmes | — | **~$5,000M** | (net catch-up −$1,377M) |

**777X: launched 2013; the FY2025 10-K says it is "currently expecting first delivery in
2027."** Fourteen years, four reach-forward losses, and not one aircraft delivered. And the
FY2025 loss would have been larger but for an estimate change disclosed in the same sentence:
*"The impact of these changes on estimated revenues and costs were **partially offset by the
100-unit accounting quantity increase**, resulting in an incremental reach-forward loss of
$4,899 million during 2025."*

**And management's own estimates, set against outturn — the [E3-48] test with management's own
table:**

| net cumulative catch-up adjustments (FY2025 10-K) | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| decrease to revenue | ($1,706M) | ($2,794M) | ($916M) |
| **decrease to earnings from operations** | **($2,943M)** | **($6,562M)** | **($1,377M)** |
| decrease to diluted EPS | ($5.43) | ($9.83) | ($1.53) |

**$10,882M of negative revisions in three consecutive years, every one in the same
direction.** [E3-48]'s remedy is to demand *"the record of the people who made the
projections,"* and Boeing publishes that record itself. Read as a Q2 fact rather than a Q3
one: a business whose decade-out cost estimates are wrong by $10.9bn in three years in one
direction does not have the pricing control a franchise implies. (Read as a Q3 fact it is
also a **candor credit** — the table exists, is quantified per-share, and names the
programmes. See Q3.)

### [E4-04] AND [E4-32] — REBUILD, AND DIRECTION

**Must the moat be continuously rebuilt?** Partly, and this is the harder call. The type
certificate is not a depleting asset; the 737's certificate has earned money for
fifty-nine years, and that is the strong form of enduring. But **the certificate must be
re-earned per derivative**: the 737-7 and 737-10 are not certified at the date of the latest
filing; the 777-9 is not certified; each requires a multi-year regulatory process Boeing does
not control (*"We are following the lead of the FAA … the ultimate timing will be determined
by the regulators"*). Under the [E5-23]/[E3-49] test the framework sets — *does a lapse in
spending destroy the structure, or merely narrow it, and does the spending defend the same
advantage or buy its replacement?* — Boeing's $3.2bn of annual R&D and its $25.6bn of
deferred production costs are **buying replacement certificates, not defending one**. That
puts it nearer the excluded class than Coca-Cola's advertising.

**[E4-32], direction, which outranks existence.** The moat has **narrowed**, on filed
evidence and not on opinion:
1. **The unit series [E4-55]**: 806 deliveries in FY2018, 600 in FY2025 — 74% of peak seven
   years later, while revenue recovered to 88%. Dollars recovering faster than units is the
   Precision Steel shape.
2. **The output rate is now licensed by a third party** (the FAA concurrence sentence),
   which was not true before January 2024.
3. **Boeing bought back its own largest supplier because the supplier was failing**, and paid
   $2,571M of consideration that went to settle Spirit's obligation to **Airbus** — the
   competitor — in the process. Spirit closed 2025-12-08 and is *"approximately 9 percent of
   Total assets"* per the auditor's internal-control report. Vertical re-integration of a
   failed supplier is a repair, not a widening.
4. **BCA has lost money in each of FY2019-FY2025 inclusive**, seven consecutive years, on the
   filed segment line.

There is no reading of those four in which the moat widened. **[E4-32]'s "primary criterion of
a great business" is failed.**

### [E3-33] / [E5-28] — UNTAPPED PRICING POWER: NO

Could a manager raise the return simply by raising prices, and has not? **No.** [E5-28] scopes
the class: claiming it is claiming *"a monopoly or a near monopoly."* Boeing is half a
duopoly with a named third entrant (*"aggressive international competitors … such as Airbus
and entrants from China"*), and the company states that pricing pressure is intense and
intensifying. The untapped-pricing-power class does not apply.

### [E2-45] — THE ATTACKER'S TEST

With ample capital and skilled people, how would I compete with Boeing? **I would not need to
attack it; I would wait.** The narrowbody backlog is a decade long, which means the marginal
order is for a delivery slot in the 2030s — and the customer choosing a slot is comparing
Boeing's ability to deliver on schedule against Airbus's. Boeing's filed record on schedule
is the reach-forward table above. The attack that works is the one Airbus is already running:
take the slot demand Boeing cannot serve because its rate is capped, and let Boeing's own
delay compensation do the rest. **COMAC's attack is slower and needs a Western certificate,
but the filing names it.** The honest counter-point: an attacker cannot take the installed
base, and BGS's aftermarket annuity is the one leg of Boeing genuinely hard to assault.

### [E4-36] — WHICH OF THE FOUR CAUSES?

Boeing's historic record — FY2018's $101bn of revenue and $13.0bn of owner earnings — came
from **wave-riding plus one extreme variable**: a two-decade air-traffic boom against a
structurally duopolised supply side. The wave is intact; **Boeing got off it.** [E3-51]'s
surfer image is the right one and it is the unflattering half: the advantage lived in the
wave, and the wave is still there — Airbus is on it.

### THE COMPETITOR ROW — required **[E3-28]**. A moat is a claim about *relative* position.

### THE COMPETITOR ROW — required **[E3-28]**. A moat is a claim about *relative* position.

**Same metric, same window (latest full fiscal year), filing-sourced.** Owner earnings on this
framework's own construction: **OCF − SBC − (c)**, both (c) ends. Peer figures built from SEC
XBRL against the named 10-K/20-F and re-derived, not taken from a data vendor.

| Company | FY2025 revenue | operating margin | OCF | OE at capex end | OE at D&A end | source |
|---|---|---|---|---|---|---|
| **BOEING (BA)** | **$89,463M** | **+4.8%** *(−1.1% ex the $9,566M disposal gain)* | **$1,065M** | **−$2,303M** *(−$3,833M with the 401(k) stock)* | **−$1,314M** *(−$2,844M)* | 10-K acc 0001628280-26-004357 |
| **AIRBUS SE** | **€73,420M** | **9.7% EBIT Adj / 8.3% EBIT reported** | **€7,995M** | **+€3,721M** | **+€4,552M** | own FY2025 results + IFRS financial statements; **not an SEC registrant** |
| Lockheed Martin (LMT) | $75,048M | 10.3% | $8,557M | **+$6,604M** | +$6,566M | 10-K FY2025 |
| RTX Corporation (RTX) | $88,603M | 10.5% | $10,567M | **+$7,421M** | +$5,670M | 10-K FY2025 |
| General Dynamics (GD) | $52,550M | 10.2% | $5,120M | **+$3,763M** | +$4,000M | 10-K FY2025 |
| Northrop Grumman (NOC) | $41,954M | 10.8% | $4,757M | **+$3,188M** | +$3,166M | 10-K FY2025 |
| Textron (TXT) | $14,799M | n/a (segment presentation) | $1,312M | **+$848M** | +$830M | 10-K FY2025 |
| TransDigm (TDG) | $8,831M | **47.2%** | $2,038M | **+$1,664M** | +$1,519M | 10-K FY2025 |
| HEICO (HEI) | $4,485M | 22.7% | $934M | **+$827M** | +$704M | 10-K FY2025 |
| Embraer (ERJ) | $7,578M | 8.0% | $870M | **+$386M** | +$611M | 20-F FY2025 |
| Spirit AeroSystems (SPR) | $6,317M *(FY2024, its last)* | **−28.3%** | −$1,121M | **−$1,311M** | −$1,480M | 10-K FY2024 — **see note** |

- **Peers named: 10, of an industry that has about that many real comparables** — two airframers
  (BA, Airbus) plus Embraer at the regional end, four US defence primes (LMT, RTX, GD, NOC),
  Textron on the business-jet and light-military end, and two aftermarket specialists (TDG, HEI)
  who are the right comparators for BGS. Buffett says eight **[E3-28]**; this is ten.
- **THE AIRBUS LIMIT, STATED RATHER THAN STRETCHED.** Airbus SE files nothing with the SEC; its
  US quote EADSY is an unsponsored ADR. The queue's own ruling is that such a name is
  **UNKNOWABLE, not UNRESEARCHED** as a run subject. But it is **not unknowable as a competitor
  row entry**: Airbus publishes audited IFRS statements and a full results release in English on
  its own IR site, which is rung three of the evidence ladder ("company IR site (English)"). The
  FY2025 figures above come from that release and the accompanying financial statements, both
  saved to this run's research folder. **Ladder rung used: 3. Rung blocked: 2 (SEC EDGAR
  primary) — no filing exists.** The comparison is therefore IFRS-against-US-GAAP and
  euro-against-dollar, and EBIT Adjusted is Airbus's own non-GAAP measure; reported EBIT is
  given beside it so the comparison does not rest on the adjusted number.
- **SPIRIT AEROSYSTEMS: CHECKED, AND IT IS NO LONGER A COMPETITOR — IT IS A SEGMENT.** The
  FY2025 Boeing 10-K states the acquisition closed **2025-12-08**, and the auditor's
  internal-control report says management *"excluded from its assessment the internal control
  over financial reporting at Spirit AeroSystems Holdings, Inc., which was acquired on December
  8, 2025, and whose financial statements constitute approximately 9 percent of Total assets."*
  Spirit's last annual filing is its **FY2024 10-K, filed 2025-02-28, accession 0001628280-25-009088**; there is no FY2025 10-K. It is no longer an SEC registrant: **Form 25-NSE filed 2025-12-08 (acc 0000876661-25-000941)** and **Form 15-12G filed 2025-12-18 (acc 0001193125-25-324804)**; `cover_shares.py SPR` returns NOT AN SEC REGISTRANT. Its FY2024 state was revenue $6,316.6M, operating loss $(1,786.1)M and shareholders' equity of **$(2,621.5)M**. Its row is shown
  as at FY2024 and labelled, because Boeing bought the thing whose numbers those are.

**WHAT THE ROW SAYS, AND IT IS NOT WHAT EITHER PRIOR EXPECTED.**

**1. Boeing is the only negative entry in the row, and it is negative by a wide margin.** Eight
of nine live peers earn positive owner earnings at **both** (c) ends. The ninth negative entry
is Spirit — which Boeing has now bought.

**2. The duopoly is a franchise. Airbus is holding it; Boeing is not.** In the same year, the
same demand environment, the same supply chain and the same regulatory world:

| FY2025, commercial aircraft | Airbus | Boeing BCA |
|---|---|---|
| **aircraft delivered** | **793** | **600** |
| commercial revenue | €52,600M | $41,494M |
| **commercial operating result** | **+€5,470M** (EBIT Adj, 10.4%) | **−$7,079M** (−17.1%) |
| whole company free cash flow / owner earnings | **+€4,753M** | **−$2,303M to −$3,833M** |
| **net cash / (net debt)** | **+€12,171M** | **($25,878M)** at 2026-06-30 |
| order book / backlog | €618,824M | $682,207M |
| 2026 own guidance | ~870 deliveries, ~€7.5bn EBIT Adj | 737 rate 42→47 *"with the concurrence of the FAA"* |

**Airbus delivered 32% more aircraft than Boeing and earned roughly €5.5bn on the leg where
Boeing lost $7.1bn — a margin gap of about 27 points on the same product in the same year.**

**3. And that is exactly what [E3-61] warns the row cannot resolve, which is the finding.**
*"In some businesses, the participants behave like a demented Kellogg. In other businesses,
they don't … I think you'd have to know the people involved."* The row shows position; it
cannot show conduct. **But it does something the framework needs more: it removes the
industry as the explanation.** Boeing's seven consecutive years of BCA operating losses cannot
be attributed to air traffic, to fuel, to tariffs, to the supply chain or to the cycle,
because the other half of the duopoly ran the same gauntlet and printed a 10.4% margin and
€12.2bn of net cash. **The environment is not the cause. That closes off the one reading under
which Boeing's record is a cyclical dip rather than a position failure.**

**4. The aftermarket peers locate where the rent in this industry actually sits.** TDG at 47.2%
and HEI at 22.7% operating margins, both throwing off owner earnings equal to 80%+ of their
operating cash, against BGS's 18-19%. The aftermarket is the franchise leg of aerospace, and
**Boeing sold $10.55bn of it in October 2025** (Digital Aviation Solutions) to fund the rest.

- Any peer unavailable (private / foreign / unsegmented)? **Airbus is foreign and unfiled with
  the SEC; it is included at ladder rung 3 with the limit stated, not held PROVISIONAL, because
  its audited statements and results release are public in English.** No peer is missing. The
  moat class is therefore **not** PROVISIONAL.
- **Untapped pricing power — could a manager raise the return simply by raising prices, and has
  not? [E3-33] NO.** [E5-28] scopes the class to *"a monopoly or a near monopoly"*; Boeing is
  half a duopoly whose own MD&A forecasts intensifying price pressure, and whose forward price
  assumption is **net of compensation owed to customers for delay**. The class does not apply.
- **Class: [ ] WIDE [ ] NARROW [x] NONE — for the company as filed** (BGS alone would be NARROW;
  see below) · **Direction: NARROWING**, on four independent filed measures.


**TWO ADDITIONS TO THE ROW, AND THE SECOND IS EVIDENCE AGAINST THE VERDICT ABOVE.**

**First, Airbus on this framework's own construction, not on its own non-GAAP measure.** From
the FY2025 IFRS financial statements rather than the press release: **operating cash flow
€7,995M, capex €3,964M, D&A €3,133M, IFRS 2 share-based payment €310M** — so owner earnings of
**+€3,721M at the capex end and +€4,552M at the D&A end.** Set beside Boeing's **−$2,303M /
−$1,314M** (or **−$3,833M / −$2,844M** once the 401(k) stock is subtracted, which is the correct
subtraction — see Q4). Figures are in **euro and are not converted**; a valuation of Airbus
would run against the EUR curve, not the 5.35% USD print. Airbus's unit backlog is **8,754
aircraft** against Boeing's roughly 6,130 undelivered firm orders — **43% larger.**

**Second, and it is the strongest single fact against the Q2 OUT: airframe manufacturing is a
thin-margin leg for everyone, not only for Boeing.** From the same-window filings: **Lockheed
Aeronautics 6.9%** (down from 10.3% in FY2023, carrying a $950M classified reach-forward loss
in FY2025), **Northrop Aeronautics Systems 6.3%** (a $477M B-21 LRIP loss provision), **Pratt &
Whitney 7.9%**, **Embraer Commercial Aviation 2.7%**. Where the peers earn 10%+ at company
level they earn it on **aftermarket and electronics** — RTX Collins 16.3%, HEICO Flight Support
24.1%, TransDigm 47.2%, Embraer Services & Support 15.5% — exactly the leg Boeing sold $10.55bn
of. **Two honest readings follow, and they point opposite ways.** (a) The whole industry takes
reach-forward losses on new airframe programmes, so Boeing's are a genre feature rather than a
moat failure. (b) Nobody else's airframe leg is at **−17.1%**, and the one direct comparable,
Airbus Commercial, is at **+10.4% on 32% more deliveries in the same twelve months.** The gap
between a thin positive and a deep negative is the whole question, and the verdict above rests
on (b). **Reading (a) is why this file is worth re-opening on the reversal conditions rather
than forgotten.**

**ONE GAP IN THE ROW, DISCLOSED.** **GE Aerospace is an SEC filer and is not in this row.** It
is the most relevant absent comparable — the other half of the narrowbody engine duopoly and a
very large aftermarket annuity. It is recorded as **UNRESEARCHED for the row** (artifact: GE
Aerospace FY2025 10-K on EDGAR; nothing blocked it but time). Its absence does not change the
verdict, because the verdict turns on Airbus and on Boeing's own segment line, and ten peers
were taken where [E3-28] asks for eight. **A second, smaller gap: HEICO's ten-year share-count
change reads +66.1%, which is a stock-split artifact and is flagged UNRESEARCHED rather than
used.**

### THE VERDICT, AND THE CASE AGAINST IT STATED FIRST **[E4-51]**

**The strongest case for IN, stated as its holders would state it.** Two airframers certify
large commercial jets; the barrier is a decade and tens of billions; the backlog is $682bn and
a decade deep; 85% of it is with non-US airlines, so it is not a US-cycle asset; the installed
base of 9,240 737s and 1,249 787s needs parts for twenty-five years and BGS earns 18-19%
servicing it; the 737 rate has already recovered 38 → 42 a month with 47 planned; the FY2025
delivery count rose 72% year on year; and Boeing's problems are self-inflicted, which means
they are fixable by different people — the [E2-35]/[E2-36] excisable-cancer case. On that
reading the right verdict is IN NARROW and the failure, if any, belongs at Q4.

**That case is real, and it loses on four filed facts.**

1. **[E2-53] — the dominance test, which is the strongest reading of franchise, FAILS.** *"Once
   dominant, the newspaper itself, not the marketplace, determines just how good or how bad the
   paper will be. **Good or bad, it will prosper.**"* Boeing did not prosper. It lost money in
   BCA in **each of FY2019 through FY2025 — seven consecutive years** — and the competitor row
   proves the marketplace was not the reason. [E2-53]'s whole point is that a franchise's
   *position* sets the economics and execution does not; here execution set them, and the
   position did not carry it. **That is a finding about the business, not about the managers**,
   and [E5-18] says so in the corpus's own words: *"if it won't stand a little mismanagement
   it's not much of a business."* Boeing's did not stand it — it went to negative shareholders'
   equity and came back to the market for $23.9bn.
2. **[E2-44] fails on both halves, and the company says so itself.** *"This market environment
   has resulted in intense pressures on pricing and other competitive factors, and we expect
   these pressures to continue or intensify in the coming years."* — the FY2025 10-K, about BCA;
   the same sentence appears about BGS. And dollar growth requires $2.9bn of capex, $3.2bn of
   R&D and $25.6bn of capitalised deferred production cost.
3. **[E3-03] criterion (2) fails as filed for the 46% that is BCA.** The MD&A: competitors
   *"offer competitive products and have access to most of the same customers and suppliers."*
   A close substitute exists, the company names it, and the row measures it. Criterion (2)
   survives only for the installed base and the aftermarket.
4. **[E3-03] criterion (3) and [E2-59].** Prices are not regulated. **Output is.** *"Since the
   737-9 door plug accident in January 2024, the 737 program may only increase production rates
   and/or implement new production lines with the concurrence of the FAA."* Under [E2-59] the
   advantage conferred or withheld by a regime belongs to the regime — *"That day is gone"* is
   how it ends — and here the regime withholds rather than confers.

Add **[E4-32]**, which the framework says outranks existence: narrowing on units (806 → 600),
on regulatory freedom (unconstrained → FAA concurrence), on vertical position (bought its
failing supplier, and funded $2,571M that went to settle that supplier's obligation to
Airbus), and on segment profitability (seven years of BCA losses). Add **[E4-37]**: the agony
metric is past the prayer session — **$1,696M of accrued customer concessions, $6,711M of
accrued forward losses, and a forward price assumption explicitly net of *"customer
consideration driven by delivery delays."***

**There is no version of the franchise test in this framework that Boeing passes on the filed
FY2025 record.** The franchise belongs to the industry structure; Airbus is collecting it.

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**THE FILE CLOSES HERE.** Q3 and Q4 below are **recorded, not governing** — they were completed
because the brief asked for the [E5-11] comparison against three other survival shapes and
because a Q2 OUT that had not read the cash would be an opinion. They change nothing: this is
**OUT on the business** at Q2.

**THE REVERSAL CONDITION, in words, because a Q2 OUT takes no price alert** (the QLYS ruling,
2026-09-07). This verdict reverses only on evidence, and the evidence has a shape:
1. **BCA posts an operating profit for a full fiscal year** — any positive number ends the
   seven-year run and is the single cleanest refutation.
2. **The FAA concurrence condition is lifted**, or the 737 rate reaches and holds a level Boeing
   sets rather than negotiates, so that [E3-03](3) and [E2-59] stop biting.
3. **The reach-forward-loss series stops.** A fiscal year with no new reach-forward loss on any
   programme, and the accrued "Forward loss recognition" balance falling toward zero from
   $6,711M.
4. **The delivery series exceeds 806** — the FY2018 peak — which is the [E4-55] test passing on
   the physical series rather than the dollar one.
5. **Accrued "Other customer concessions and considerations" falls materially from $1,696M**,
   which is the [E4-37] agony metric reversing.

None of these can be inferred from a price. All five are read off a 10-K.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

⚠️ **RECORDED, NOT GOVERNING. Q2 returned OUT and the file closed there.** This section exists
because the brief asked for it and because a Q2 OUT written without reading the manager record
would be an opinion. Nothing here promotes anything — and per the guardrail, a strong Q3 cannot
repair Q2 anyway **[E2-37, E2-38, E3-39]**.

**STEP 1 — THE WEIGHT CASE, DECLARED FIRST.** *How much damage can this manager do before I can
react?*
- [x] **Daily execution [E3-38, E3-43, E2-70]** — **TICKED, and this is the company where it is
      least arguable.** Every airframe must be built correctly every day, and the filed
      consequence of one day's failure is on the record: a door plug detached on 2024-01-05, the
      FAA *"imposed certain additional requirements and restrictions"*, the 737 rate went below
      38 a month, FY2024 operating cash flow was **−$12,080M**, and the rate has required FAA
      concurrence ever since. This is not a have-to-be-smart-once business.
- [ ] **Control [E1-16]** — not ticked; a marketable security, exitable.
- [x] **Leverage [E3-29]** — **TICKED. $165,870M of assets on $6,115M of total equity at
      2026-06-30 — 27:1**, with $45,900M of debt. [E3-29]'s test is *"small asset errors destroy
      equity"*, and here a single reach-forward loss of the size already taken on the 777X
      ($4,899M in FY2025 alone) exceeds three-quarters of total equity. It has happened: equity
      was **−$23,552M at 2024-09-30**.

**TWO OF THREE TICKED → Q3 IS A BINARY GATE AND NO PRICE COMPENSATES [E1-16, E3-29, E5-35].**
*"You can turn any investment into a bad deal by paying too much. What you can't do is turn any
investment into a good deal by paying little."*

### HONESTY — binary, permanent, filings-based, each matter dated to when it became PUBLIC **[E5-16]**

**The filed criminal record, from Note 23 of the FY2025 10-K (acc 0001628280-26-004357), verbatim:**

> **"On May 29, 2025, Boeing and the Department of Justice (the Department) entered into a
> non-prosecution agreement (the Agreement) to resolve the Department's determination that
> Boeing did not fulfill its obligations under the January 2021 deferred prosecution agreement**
> relating to the October 2018 Lion Air flight 610 accident and the March 2019 Ethiopian
> Airlines flight 302 accident (the MAX accidents). **The Agreement requires, among other
> things, Boeing to pay a fine of $244 and provide $445 of additional compensation for the
> family members of those who died in the MAX accidents.** … **On November 6, 2025, the U.S.
> District Court for the Northern District of Texas (the Court) approved the Motion; however,
> representatives of family members appealed the Court's decision, which appeal is pending
> before the U.S. Court of Appeals for the Fifth Circuit."**

The chronology, all filed and all dated: **2021-01-07** DPA entered · **2024-01-05** the 737-9
door plug detaches, three years into the DPA · **2024-05-14** the DOJ determines Boeing *"did
not fulfill our obligations under the DPA"* · **2024-07-24** a proposed guilty plea, $244M fine,
≥$455M of compliance investment and a three-year independent compliance monitor ·
**2024-12-05** the court **rejects** the plea · **2025-05-29** a non-prosecution agreement
instead, $244M + $445M, **$689M held in escrow and carried as a named balance-sheet line,
"Non-prosecution agreement liability"** · **2025-11-06** dismissal approved · appeal pending.

**Two things must be said about this and neither is comfortable.**

**(a) The strongest case for a permanent OUT, stated at full strength [E4-51].** [E5-22] is the
exact calibration row: the Wells Fargo error was reading a $185M fine as small, and *"the
failure that counts is **they didn't act when they learned.**"* Boeing learned in 2019. It
signed a deferred prosecution agreement in January 2021. **A door plug left the airframe in
January 2024 and the DOJ then found the agreement had not been fulfilled.** That is not a fine
being read as small; that is a three-year window in which the company was under a criminal
agreement about safety and the safety failure recurred. And the disclosure detail sharpens it:
**the $455M compliance investment and the three-year independent monitor were terms of the
REJECTED plea and do not appear in the FY2025 10-K's description of the agreement that replaced
it.** The FY2024 note's reassurance — *"the outcome … will not have a material effect"* — was
also dropped from the FY2025 note, which is a deviation **toward** candor **[E2-69]** but is
also the company withdrawing its own comfort.

**(b) Why it is not recorded as OUT here.** [E5-16]'s binary is about **persons** — *"our
tolerance for personal misconduct is zero"* — and [E2-57] says *"the real mistake is not the
act, but the actor."* The actors are gone: Ortberg became CEO in August 2024, hired from
outside, and the CFO is also new. The corpus's method is to date each matter to when it became
public and to judge the actor in place. **So the record is stated, not scored, and the verdict
below is the narrow corpus one — the absence of a found disqualifier in the conduct of the
management in place, never a finding that these managers are honest [E5-17].**

### THE FLAGS **[E4-22, E5-15, E4-29]** — prompts to read. I read them, and they do not all fire.

**[E4-29] — EBITDA / adjusted-earnings promotion: DOES NOT FIRE. This is a genuine credit and
it survived the CGNX test.** The companion rule from the CGNX run is to pull the 8-K EX-99.1
earnings releases before scoring this flag, because a run reading only the annual report scores
clean a company whose public narrative runs on a non-GAAP metric. **Four EX-99.1 releases were
pulled** (Q2 2026, Q1 2026, Q4 2025, Q3 2025) **plus the 10-K, the Q2 2026 10-Q and the proxy.
The word "EBITDA" appears ZERO times in any of them.** There is no "adjusted EPS" and no
"adjusted earnings". Every headline bullet leads with GAAP: *"GAAP loss per share of ($0.67)
and core loss per share (non-GAAP) of ($0.76)."* And note the direction — **"core" excludes only
the FAS/CAS pension adjustment, so in 2026 core is WORSE than GAAP.** A non-GAAP measure that
makes the company look worse is the opposite of the [E4-29] behaviour. **Flag clean, and stated
as such rather than skimmed.**

- [ ] weak accounting — **not ticked on the accounting itself.** Stock compensation IS expensed;
      the 401(k) stock contribution is disclosed on its own line in the cash-flow statement (the
      screen missed it, the filing did not); pension assumptions are **not** fanciful (discount
      rate 5.30%, **expected return on plan assets 6.00%** in each of the last three years —
      conservative against a 5.35% 30-year Treasury). One mild item: the market-related value
      of plan assets is **$1,398M above fair value** under asset smoothing.
- [x] **unintelligible footnotes — TICKED, in a modern form.** The proxy's 2025 goals-and-outcomes
      chart, which carries the per-metric weights and the target-versus-actual behind the payout,
      **is published as a JPEG image rather than text.** The individual weights that produce the
      131% cannot be verified from the filed document. [E4-22]'s second flag is about a reader
      being unable to reconstruct the number, and here the reader cannot.
- [x] **trumpeted projections — TICKED, and this is the sharpest [E3-48] record in the queue.**
      Boeing gives **no numeric free-cash-flow guidance at all** — which is the [E5-30] ratchet
      avoided, and a credit. What it does give, in the filings themselves, is **schedule
      commitments**, and their record is this:

  | 777X first delivery, as stated in successive 10-Ks | the target |
  |---|---|
  | FY2015 10-K | **2020** |
  | FY2020 10-K | **late 2023** |
  | FY2023 10-K | **2025** |
  | FY2024 10-K | **2026** |
  | FY2025 10-K and Q2 2026 10-Q | **2027** |

  **Launched 2013. Five successive targets, five misses, zero aircraft delivered, and
  $14,891M of cumulative reach-forward losses ($6,493M + $3,499M + $4,899M).** [E3-48]'s stated
  remedy is to demand *"the record of the people who made the projections"* — the record is
  above. The 737 MAX 7/MAX 10 record is the same shape: *"currently going through FAA
  certification"* in the FY2022 10-K, still uncertified four annual reports later, with
  undelivered MAX 7/10 inventory at **"approximately 35" at each of three consecutive year-ends
  and "approximately 40" at 2026-06-30** — and **37% of undelivered 737 orders are those two
  uncertified models** (the -10 alone is 31%).
- [x] **serial share issuance — TICKED [E5-15].** *"one of the surest indicators of a
      promotion-minded management…"* The filed record: **October 2024, 129,375,000 common shares
      for $18,181M net, plus 115,000,000 depositary shares representing 5,750,000 shares of 6.00%
      Series A Mandatory Convertible Preferred for $5,651M net — $23,832M in two days.** December
      2025, a further **22,977,008 shares** issued for Spirit. Basic weighted-average shares
      **606.1M (FY2023) → 647.2M (FY2024) → 760.0M (FY2025), +25.4% in two years**, with
      **33.5-40.2 million more** contracted to arrive on the mandatory conversion date of
      **2027-10-15**. *The counter-point, stated: this was a solvency raise by a company with
      negative book equity, not a promotion. [E5-15]'s flag is still a prompt to read and what
      it points at is the allocation record below.*
- [ ] filed-figure tells **[E4-30]** — **not ticked, and pointing the other way.** [E4-30]'s tell
      is *unnaturally smooth* reported growth. Boeing's reported series is the least smooth in
      the queue: net income $10,460M → −$636M → −$11,873M → −$4,202M → −$4,935M → −$2,222M →
      −$11,817M → +$2,235M. Cash taxes are not falling as a share of pretax income because
      pretax income has been negative. **The filed-figure fraud tells cannot fire on a company
      whose figures are this ugly** — which is itself an observation worth recording.
- [x] **metric-switching [E2-49] — TICKED ON SUBSTANCE, CLEAN ON TIMING, and the split matters.**
      [E2-49]'s operational form: *a switch that follows deterioration fires; one announced ahead
      with reasons is the candor case.* Three changes between the 2025 and 2026 proxies:
      1. the annual-incentive earnings metric moved from **Operating Earnings (2024)** to **Core
         Earnings/(Loss) Per Share, a non-GAAP measure (2025)**;
      2. safety weight moved from *"exclusively focused on safety and quality … performance in
         safety and quality accounted for **60%** of that [Commercial Airplanes] business unit's
         incentive score"* (2024) to **an unweighted slice of a 20% enterprise bucket** (2025),
         with the proxy's own words: *"Specific weightings were not assigned to any specific
         goal; rather, the final operational performance score was determined by the
         Compensation Committee based on a **holistic review**"*;
      3. the 2025 long-term grant switched **from performance share units to premium-priced
         options — 55% PPSO / 45% time-vesting RSU, no performance condition at all** — because,
         verbatim, it was *"necessary due to the uncertainty of our business environment."*
      **The timing is the candor case: all three were pre-announced in the March 2025 proxy with
      stated reasons, not switched after the fact.** The substance is the flag: in the year after
      the door-plug accident, the safety weight was diluted and the performance condition was
      removed.

### **[E4-52] — THE FLAGS THAT CONVERGE ARE A DIFFERENT EVENT, AND THEY CONVERGE HERE ON THE PAY**

*"extreme consequences from **confluences** of psychological tendencies acting in favor of a
particular outcome."* Four facts from the same proxy, pointing one way:

1. The 2025 annual incentive is **80% financial (free cash flow, core EPS, revenue) + 20%
   holistic safety**, times an individual multiplier of 0-120%.
2. **The adjustments, verbatim:** *"For 2025, free cash flow was adjusted **upward** from ($1.9B)
   to ($0.5B), core earnings/(loss) per share was adjusted **downward** from $1.19 to ($10.72),
   and revenue was adjusted **upward** from $89.5B to $89.8B."* The EPS adjustment is
   dramatically **against** the company and is a real candor point. The free-cash-flow
   adjustment moved $1.4bn **in its favour**, on the metric the proxy itself calls its most
   important.
3. **The One Company Score came out at 131%, and the individual multiplier was 100% for all six
   named executives** — in a year whose filed free cash flow was **−$1,877M** and whose owner
   earnings were **−$2,844M to −$3,833M**.
4. **The long-term plan, by contrast, paid nothing:** *"Payout of 0% for three-year performance
   stock units (PSUs) granted in 2023 … below-threshold performance against three-year
   cumulative free cash flow goals."* And the 2025 replacement grant carried no performance
   condition.

**Read as one system rather than four prompts: the long-horizon instrument measured the thing
that matters and paid zero, and it was replaced with an instrument that cannot pay zero, while
the short-horizon instrument paid 131% on an adjusted version of the same metric.** CEO total
compensation was **$23,581,389** for 2025 (salary $1.5M, stock $7,874,818, options $9,624,959,
non-equity incentive $3,930,000 against a $3,000,000 target, other $651,612); the CFO received
**$8,500,000 of one-time cash** to replace equity clawed back by a prior employer. Pay ratio
166x on a median employee of $141,933 — **a median last identified in 2023.**
*This is [E4-52] recorded as the lollapalooza it is. It is not a fraud finding [E2-30].*

### STEP 3 — THE PRIMARY TEST **[E2-01]**, AND IT HAS NO DENOMINATOR

*"The primary test of managerial economic performance is the achievement of a high earnings rate
on equity capital employed (without undue leverage, accounting gimmickry, etc.)."*

| total shareholders' equity/(deficit), $M | | | | | | | |
|---|---|---|---|---|---|---|---|
| 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | **2025** | **2026-06-30** |
| (8,617) | (18,316) | (14,999) | (15,883) | (17,233) | (3,908) | **+5,454** | **+6,100** |

**Return on equity is not computable for FY2019 through FY2024 — six consecutive fiscal years —
because the denominator was negative.** That is not an inconvenience; on [E2-01]'s own terms it
is the answer. And the caption in Boeing's own balance sheet moved from *"Total shareholders'
deficit"* to *"Total shareholders' equity/(deficit)"* to *"Total shareholders' equity"* as the
sign changed, which is at least honest labelling.

**And the return to positive equity is not trading.** The $9,362M swing in FY2025 came
substantially from the **$9,566M Digital Aviation Solutions divestiture gain**, $4,357M of
treasury stock released for the Spirit purchase, and $2,477M of additional paid-in capital.
Equity is **3.7% of total assets** at 2026-06-30 and **retained earnings FELL $620M in the first
half of 2026** on a −$435M net loss. So the [E2-01] series, on its first computable year, is
built on an asset sale.

**[E2-43]'s scoped denominator** — unleveraged net tangible assets, with the goodwill wedge
separate — makes it worse, not better: goodwill rose from $8,084M to $17,275M in FY2025 on the
Spirit purchase, so tangible equity at 2025-12-31 is **$5,454M − $17,275M − $1,567M of acquired
intangibles = −$13,388M.** **On the corpus's own preferred denominator, Boeing's equity is still
negative.** *This is a number, not a judgment; I state it because [E2-43] asks for it.*

### THE HALF-OWNER TEST **[E2-26]** — and this is where Boeing does best

*Does this reporting tell me what I would want to know if the positions were reversed?* **Largely
yes, and I did not expect that.** The one-time items are quantified separately at every line:
the $9,566M disposal gain is named in the segment discussion **and** backed out in the cash-flow
statement; the reach-forward losses are given by programme and by year; abnormal production
costs are disclosed separately ($30M / $256M / $1,014M for FY2025/24/23); the accounting-quantity
increases are disclosed **and** their offsetting effect on the 777X loss is stated in the same
sentence; the 401(k) stock contribution has its own cash-flow line.

**And the corpus's positive pole [E2-67] is present in substance.** Berkshire published a table
of its own reserving errors *"so you can … judge whether we may have some systemic bias"*,
naming the direction. Boeing publishes the equivalent:

| net cumulative catch-up adjustments | FY2023 | FY2024 | FY2025 | three-year total |
|---|---|---|---|---|
| decrease to earnings from operations | ($2,943M) | ($6,562M) | ($1,377M) | **($10,882M)** |
| decrease to diluted EPS | ($5.43) | ($9.83) | ($1.53) | — |

**Three consecutive adverse years, quantified per share, no favourable year presented.** That
table is the systemic bias, published by the company, in the direction that embarrasses it.
Under [E2-67] that is the candor read, and it is a credit. *Its content, of course, is the
indictment: management's own decade-out estimates were wrong by $10.9bn in three years, always
the same way.* **[E2-72] authorship** is also satisfied in form — the proxy and the letters are
signed, the CEO's statements are attributed.

**The auditor's-eye test [E4-34].** Deloitte & Touche, Seattle, *"auditor since at least 1934"*,
unqualified on both the statements and internal control. **Three critical audit matters, and all
three are the same thing: contract and programme cost estimation** — fixed-price development
contracts (KC-46A, Commercial Crew, VC-25B, T-7A, MQ-25); **777X programme accounting**; **737
programme accounting**. The auditor describes itself *"performing a lookback analysis on
management's ability to estimate certification timing and production unit time"* and conducting
*"internet searches to identify reports related to the regulatory environment and customer
statements … whether any contradictory evidence existed."* **The auditor is running the [E3-48]
test on management, and says so in the filing.** [E4-34]'s fourth question — period-shifting —
is precisely what programme accounting does by design, disclosed rather than concealed. And
[E2-50] applies with full force: *"Where 'earnings' can be created by the stroke of a pen, the
dishonest will gather"* — Boeing's earnings are created by the stroke of a pen (the accounting
quantity), which is why this run priced it on cash and not on earnings.

### RATIONALITY — CAPITAL ALLOCATION, AND THIS IS THE FLAG THAT LANDS

**The filed record, in two numbers.**

| | |
|---|---|
| buybacks, FY2013-FY2019 | **$43,441M** |
| common dividends, FY2013-FY2019 | **$20,821M** |
| **total returned to shareholders in seven years** | **$64,262M** |
| equity raised, FY2024 | **$23,832M** ($18,181M common + $5,651M preferred) |
| senior notes issued, FY2024 | **$10,000M at 6.259%-7.008%** |
| common dividend today | **suspended since 2020; not reinstated** |

**[E5-08] condition (1) — *"a company has ample funds to take care of the operational and
liquidity needs of its business"* — is the condition that failed, and it failed absolutely.**
Boeing returned $64.3bn in the seven years to 2019 and then required $23.8bn back from the
market in a single week of October 2024, having passed through six year-ends of negative book
equity. **[E5-24] is the governing row:** *"whether the money is slated for acquisitions or
share repurchases … **what is smart at one price is dumb at another.**"* And **[E2-52]** is the
shape of it: *"Beware of 'dividends' that can be paid out only if someone promises to replace
the capital distributed."* The promise-keeper turned out to be the 2024 shareholder, at a price
far below the buyback average.

**[E2-51]'s inverse does not apply** — Boeing is not refusing repurchases when they are
obviously right; it has no funds for them. **[E5-25]'s compliance standard** — publish both
conditions as numbers in advance, with a liquidity floor, because *"financial strength that is
unquestionable takes precedence over all else"* — is not met and was never attempted.

- (1) ample funds for operations and liquidity? **NO**, on the filed record above.
- (2) repurchases at a material discount to conservatively calculated IV? **Not applicable
      today; and on the FY2013-19 record, no — $43.4bn was spent at prices the company later
      raised equity 50%+ below.**
- → **CAPITAL ALLOCATION FLAG: LIVE**, stated with the humility clause **[E4-13]**: this rests on
  our own IV range and *"they also know a whole lot more about them than I do."* **[E5-08]:**
  *"infractions, even serious ones, are innocent; many CEOs never stop believing their stock is
  cheap."* **The flag binds position size, never the discount rate — and there is no position
  to size, because Q2 is OUT.**

**THE INSTITUTIONAL IMPERATIVE — score all four [E2-30].** *Not a fraud test: "institutional
dynamics, not venality or stupidity."*
- [x] **resists any change in current direction** — the 777X was not cancelled after four
      reach-forward losses totalling $14.9bn and fourteen years; the accounting quantity was
      **raised** instead (+150 units on the 777X, +800 on the 737, +100 on the 787 in FY2025).
- [ ] projects/acquisitions materialise to soak up available funds — **not ticked, and the
      opposite is true.** There were no available funds. The one large acquisition, Spirit, was
      a **repair of a failing supplier** that the 10-K describes as having required Boeing
      funding *"since 2023 … to support its liquidity, rate readiness, and 787 tooling."* And
      Boeing **sold** $10.55bn of its best-margin business. Divesting the good leg to fund the
      bad one is a real finding, but it is not [E2-30](2).
- [x] **staff studies produced to justify the leader's craving** — ticked in its filed form: each
      accounting-quantity increase is supported by *"firm orders, letters of intent from
      prospective customers and market studies"*, and each increase lowers reported cost per
      unit. The studies are real; the direction of their effect on the reported number is one-way.
- [ ] peer behaviour mindlessly imitated — **not ticked.** Nothing in the filings shows Boeing
      following Airbus or the primes; if anything the failure is idiosyncratic, which is
      [E3-61]'s point.

**[E2-56] — judge retention segment by segment, never on the blended return.** *"Their marvelous
core businesses … camouflage repeated failures in capital allocation elsewhere."* Boeing is the
inverse Pro-Am: **BGS, the marvellous core business at 18-19% margins, was camouflaging BCA and
BDS — and then it was partly sold.** BDS has consumed capital and produced $5.0bn of losses on
five fixed-price development programmes in FY2024 alone. **[E3-54]'s retention test** — at least
$1 of market value per $1 retained, five-year rolling — cannot run: nothing was retained;
capital was raised.

### THE GUARDRAIL — checked before the verdict

- [x] Confirmed: **nothing in this Q3 is used to promote the name.** It cannot be — Q2 is OUT.
- [x] **Does this business REQUIRE a great manager? YES, and that is recorded at Q2 as a moat
      defect [E4-23], not here as a strength.** The competitor row is the proof: identical
      structure, 27 points of margin difference. *"if a business requires a superstar to produce
      great results, the business itself cannot be deemed great."* **This is the single most
      important line in this Q3, and it is a Q2 finding.**
- [x] **Is the franchise already intact and the damage excisable, or is the manager the plan?
      [E2-35, E2-36]** — **the manager is the plan.** The bull case for Boeing today is
      explicitly a turnaround case: a new CEO from outside, a new CFO, a re-integrated supply
      chain, a quality system being rebuilt. [E2-36] distinguishes *"extraordinary business
      franchises with a localized excisable cancer"* from *"the true 'turnaround' situation in
      which the managers expect — and need — to pull off a **corporate Pygmalion.**"* Boeing's
      damage is not localised: it spans BCA's margin, BDS's fixed-price book, the regulator's
      consent, the balance sheet and the share count. **Only the first class is buyable, and
      this is the second.** And [E4-49] states the base rate: the history of persuading
      managements to change course is *"poor"* — Munger: *"Worse than poor."*

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  — **IN in the narrow corpus sense ONLY: no disqualifier found in the conduct of the management
  in place**, which took office in August 2024 after the events on the record. *Written exactly
  as [E5-17] requires: this is the absence of a found disqualifier, not a finding that the
  managers are honest — "sincerity and empathy can easily be faked", and [E5-26]'s Sokol
  calibration warns that a decade of good record precedes the failure. It is a **fragile IN on a
  BINARY gate** with a **live capital-allocation flag**, a ticked [E2-49] substance flag, a
  ticked [E5-15] flag, a ticked [E4-22] footnote flag, and an [E4-52] convergence on the pay.
  **If the actors who breached the 2021 DPA were still in place this would be a permanent OUT
  under [E5-16], and that sentence is the honest summary of the record.** IN never promotes, and
  here it promotes nothing: Q2 already returned OUT.*

## Q4 — WILL IT SURVIVE?

⚠️ **RECORDED, NOT GOVERNING. Q2 returned OUT.** Built in full because the brief asked for the
[E5-11] comparison against three other survival shapes, and because the screen's four
constructions had to be rebuilt before anything could be said about them.

### THE DEFECT IN THE QUEUE'S NUMBER, FOUND BEFORE ANYTHING ELSE

**The queue row reads `oe_bottom_m -4429 | oe_top_m -3392`, a spread of $1,037M. Both ends
reproduce to within $4M and both are wrong, in the same direction, for two independent reasons.**

**Reason one — the spread is a WINDOW artifact, not a capex band.** `floor_screen.owner_earnings`
computes four constructions, `{5y, 3y} × {D&A, capex}`, and reports min and max. Rebuilt
exactly: 5y_D&A −3,563 · 5y_capex **−3,388** · 3y_D&A −4,076 · 3y_capex **−4,426**. The minimum
and the maximum **both sit at the capex end**. So the published "spread" measures the difference
between a three-year and a five-year mean and says nothing at all about the maintenance-capex
judgment. **This is the INTC finding of 2026-09-07 replicating on the same sub-class** — there
the two ends were a 3-year investing-capex mean against a 5-year depreciation mean on a
superseded OCF. Here there is no restatement, but the structural defect is identical: *a spread
that is advertised as a capex band and is actually a window difference.* The triage note's
warning — *"a tight spread here is not safety"* — was right in substance and again wrong about
what the spread was.

**Reason two — and this is a NEW defect, the same class as the SBC-of-zero found by BE on
2026-09-12, in a place the SBC fix does not reach.** Boeing's consolidated cash-flow statement
carries **two** equity-settled compensation add-backs, not one:

> Non-cash items –
> **Share-based plans expense** — 426 / 407 / 690
> **Treasury shares issued for 401(k) contribution** — **1,530 / 1,601 / 1,515**
> *(FY2025 / FY2024 / FY2023; FY2025 10-K, Consolidated Statements of Cash Flows)*

The second line is employee retirement compensation **settled in Boeing stock instead of cash**,
added back to operating cash flow exactly as SBC is. **The screen subtracts the first and not the
second, because XBRL does not carry the second.** `StockIssuedDuringPeriodValueEmployeeBenefitPlan`
resolves for FY2010-12 and FY2020 only; from FY2021 the number exists **solely in the filed
statement**. The filed series, read out of five 10-Ks and two 10-Qs:

| $M | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---|---|---|---|---|---|---|
| Share-based plans expense | 250 | 833 | 725 | 690 | 407 | 426 | 264 |
| **Treasury shares issued for 401(k)** | **195** | **1,233** | **1,215** | **1,515** | **1,601** | **1,530** | **855** |
| **total equity-settled compensation** | **445** | **2,066** | **1,940** | **2,205** | **2,008** | **1,956** | **1,119** |

**[E5-06] is unambiguous — *"To say 'stock-based compensation' is not an expense is even more
cavalier"* — and [E3-70] is stricter still: the measure is what the company could have realised
by publicly selling equity of like quantity, so the reported charge is the FLOOR of the
subtraction, not the measure.** A 401(k) match paid in shares is compensation by any reading, and
it is added back to OCF, so not subtracting it overstates owner earnings by **$1.5-1.6bn a
year.** Before FY2020 the line does not exist because the match was paid in cash — already
inside OCF as an outflow — so it is correctly zero for FY2008-2019 and must not be double-counted.

**Two further notes for the record.** (a) Boeing also settled **pension** contributions in stock:
*"Treasury shares contributed to pension plans — 952 / 2,048 / 3,000"* for FY2022/21/20. These
are **not** subtracted below, because their path through the operating section is not separable
from the "Pension and other postretirement plans" line; the omission is **conservative against
this run's conclusion** (subtracting them would make owner earnings worse). (b) The four FY2025
constructions in the queue also carry the **$9,566M Digital Aviation Solutions gain** correctly —
it is backed out of the operating section as part of *"Gain on dispositions, net (9,672)"*, so
the cash construction was never contaminated by it. That is the one thing the screen got right
that a net-income proxy would have got catastrophically wrong.

### Owner earnings — the one number **[E2-23]**

**WHICH YEARS DESCRIBE THE BUSINESS THAT EXISTS NOW. The choice, stated and justified.**

The brief is right that there is no stable multi-year figure here. `best_year_dep 12.634` means
dropping the best two years moves the mean by **more than twelve times**; both level tests refuse
because the early half straddles zero; and a single payables line moved by 111% of a year's
operating cash. **The correct response is not to pick a window and defend it — [E4-38] forbids
exactly that** (*"growth-rate presentations can be significantly distorted by a calculated
selection of either initial or terminal dates"*), and its remedy, worked on Berkshire's own
record, is to **publish every window.** So every window is published below.

**But the run must still say which years describe the business that exists now, and there is a
dated structural break rather than a matter of taste. The break is FY2019.** On 2019-03-13 the
737 MAX was grounded worldwide. Seven things changed across that line and **none of them has
changed back**:

| | before FY2019 | now (latest filing) |
|---|---|---|
| BCA deliveries | 723-806 a year | **600** (FY2025) |
| BCA operating result | profit every year | **loss in each of FY2019-FY2025** |
| who sets the 737 output rate | Boeing | **the FAA, by concurrence, since Jan 2024** |
| total debt | $13,847M (2018-12-31) | **$54,098M** (2025-12-31) |
| interest and debt expense | $475M (FY2018) | **$2,771M** (FY2025) |
| weighted-average basic shares | 579.2M (FY2018) | **759.8M** (FY2025), 790.4M on the cover |
| the 401(k) match | paid in cash | **paid in stock, $1,530M in FY2025** |

**A mean that mixes FY2008-2018 with FY2019-2025 is [E4-25]'s "averaging two different
businesses" — the same error the queue's own SIGN CHANGE sub-class was written to prevent, except
that here the sign changed downward.** The business that exists now is **FY2019-FY2025 and the
trailing twelve months**. Pre-break windows are published for completeness and are labelled as
describing a different company; they are not averaged into the answer.

**Owner earnings by year — OCF less ALL equity-settled compensation less (c), both (c) ends:**

| FY | OCF | SBC | 401(k) stock | D&A | capex | **OE (D&A end)** | **OE (capex end)** |
|---|---|---|---|---|---|---|---|
| 2008 | (401) | 209 | 0 | 1,013 | 1,674 | (1,623) | (2,284) |
| 2009 | 5,603 | 238 | 0 | 1,066 | 1,186 | 4,299 | 4,179 |
| 2010 | 2,952 | 215 | 0 | 1,746 | 1,125 | 991 | 1,612 |
| 2011 | 4,023 | 186 | 0 | 1,675 | 1,713 | 2,162 | 2,124 |
| 2012 | 7,508 | 193 | 0 | 1,811 | 1,703 | 5,504 | 5,612 |
| 2013 | 8,179 | 206 | 0 | 1,844 | 2,098 | 6,129 | 5,875 |
| 2014 | 8,858 | 195 | 0 | 1,906 | 2,236 | 6,757 | 6,427 |
| 2015 | 9,363 | 189 | 0 | 1,833 | 2,450 | 7,341 | 6,724 |
| 2016 | 10,496 | 190 | 0 | 1,889 | 2,613 | 8,417 | 7,693 |
| 2017 | 13,346 | 202 | 0 | 2,047 | 1,739 | 11,097 | 11,405 |
| 2018 | 15,322 | 202 | 0 | 2,114 | 1,722 | **13,006** | **13,398** |
| **2019** | (2,446) | 212 | 0 | 2,271 | 1,834 | **(4,929)** | **(4,492)** |
| 2020 | (18,410) | 250 | 195 | 2,246 | 1,303 | **(21,101)** | **(20,158)** |
| 2021 | (3,416) | 833 | 1,233 | 2,144 | 980 | **(7,626)** | **(6,462)** |
| 2022 | 3,512 | 725 | 1,215 | 1,979 | 1,222 | **(407)** | **350** |
| 2023 | 5,960 | 690 | 1,515 | 1,861 | 1,527 | **1,894** | **2,228** |
| 2024 | (12,080) | 407 | 1,601 | 1,836 | 2,230 | **(15,924)** | **(16,318)** |
| 2025 | 1,065 | 426 | 1,530 | 1,953 | 2,942 | **(2,844)** | **(3,833)** |

*FY2007 is excluded: the D&A tag does not resolve for it, so 18 filed years are used, not 19.
**SBC resolves for every one of the 18**, as required after the BE defect.*

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25]. Every window, published [E4-38]:**

| window | n | **OE, D&A end** | **OE, capex end** |
|---|---|---|---|
| FY2008-2025 (18y, everything filed) | 18 | +730 | +782 |
| FY2016-2025 (10y) | 10 | (1,842) | (1,619) |
| *— a different company —* | | | |
| FY2011-2018 (8y, pre-grounding) | 8 | **+7,552** | **+7,407** |
| FY2014-2018 (5y, pre-grounding) | 5 | **+9,324** | **+9,129** |
| *— the business that exists now —* | | | |
| **FY2019-2025 (7y, the whole post-grounding era)** | 7 | **(7,277)** | **(6,955)** |
| **FY2021-2025 (5y, the corpus default window [E2-42])** | 5 | **(4,981)** | **(4,807)** |
| **FY2022-2025 (4y)** | 4 | **(4,320)** | **(4,393)** |
| **FY2024-2025 (2y, post-door-plug)** | 2 | **(9,384)** | **(10,076)** |
| FY2025 (1y — shown, not used; [E2-23] requires a multi-year figure) | 1 | (2,844) | (3,833) |
| **TTM to 2026-06-30** (FY2025 10-K less H1-2025 10-Q plus H1-2026 10-Q) | — | **(585)** | **(2,238)** |

- **Short-window mean** (FY2022-2025, 4y): **−$4,320M to −$4,393M**
- **Long-window mean** (FY2019-2025, 7y): **−$7,277M to −$6,955M**
- **Spread, conservative end:** the conservative end of the honest range is **−$10,076M** (the
  two post-door-plug years at the capex end) and the least unfavourable **−$585M** (the trailing
  twelve months at the D&A end, which is the invalid end — see below).
- **COMBINED RANGE, every multi-year window × both (c) ends: −$10,076M to +$9,324M — a width of
  $19,399M.** The queue published a width of **$1,037M**. **The real width is nineteen times the
  published one.**
- **COMBINED RANGE, restricted to the business that exists now: −$10,076M to −$4,320M.**
  **NEGATIVE ON EVERY CONSTRUCTION, EVERY POST-BREAK WINDOW, AND BOTH (c) ENDS. The trailing
  twelve months, the most favourable honest construction available, is −$585M to −$2,238M.**
- **Is that range too wide to reach a conclusion [E4-25]?** The *full* range is — +$9.3bn to
  −$10.1bn reaches nothing. **The post-break range is not: it reaches a conclusion, and the
  conclusion is that there are no owner earnings.** That distinction is the whole value of
  dating the break. And note that the [E3-55] scope test does not rescue it: *"If we have a
  business about which we're extremely confident as to the business result, we would prefer that
  it have high volatility than low volatility"* — but that requires a certain endgame, and
  Boeing's endgame is a regulator's consent and three uncertified aircraft.
- **The distorted years, named [E5-11]:** FY2020-21 carry COVID; FY2024 carries the door-plug
  accident **and** the IAM 751 work stoppage; FY2025 carries the $9,566M disposal gain (which
  never touched the cash line) and $5,283M of reach-forward losses; FY2019 carries the grounding.
  **Five of seven post-break years are distorted, and there is no undistorted year to fall back
  on.** [E4-41] requires normalising **down** for favourable breaks, which is the only direction
  the corpus authorises — and the one large favourable break in the window is the disposal gain,
  already excluded.

**MAINTENANCE CAPEX — (c) as a DISCLOSED JUDGMENT [E2-23], with the corpus default and its
exception class.**

D&A is the default proxy for (c) **[E3-44, E2-41]**: *"the depreciation charge is not
inappropriate in most companies to use as a proxy for required capital expenditures"* … *"At 95%
of American businesses."* **Boeing is in the exception class, and for a reason more specific than
capital intensity.**

1. **The mechanical test fails.** FY2025 capex $2,942M against D&A $1,953M — **capex is 1.51× the
   depreciation charge**, and H1 2026 is worse at $2,008M against $1,169M (**1.72×**). A business
   spending half again its depreciation charge on plant is not one whose depreciation describes
   renewal.
2. **And the decisive point is that Boeing's real maintenance investment is not on the capex line
   at all.** What Boeing must renew is **type certificates**, and the spending that renews them
   runs through **research and development ($3,180M in FY2025)** and through **capitalised
   deferred production costs and non-recurring tooling ($11,777M + $750M on the 737, $13,859M +
   $1,366M + $932M on the 787, $651M + $1,816M on the 777X — roughly $31.2bn in inventory)**.
   **The $1,953M depreciation charge contains nothing whatsoever for the eventual replacement of
   the 737.** [E5-20]'s railroad logic applies with more force here than to a railroad: *"merely
   spending their depreciation expense will not keep them in the same place."*
3. **[E4-47]** reinforces it: replacement cost in current dollars against depreciation charged on
   pre-2019 tooling.

**So the D&A end of this band is INVALID, not merely optimistic, and it is shown only as a
display of the guess [E5-20]. The honest (c) is at or above total capex, and arguably above it
once R&D and deferred production costs are considered.** Band used: **D&A (invalid) to total
capex (the floor of the honest guess)**. Where it sits in the band and why, from the filing: at
or beyond the capex end, because the 777X reach-forward losses are the filed measurement of
renewal spending exceeding what the programme will return.

**And it does not change the verdict, which is worth stating plainly.** Every post-break window
is negative at **both** ends. The (c) judgment, the one place a run can flatter a name, cannot
flatter this one. Windage count for the range: **one** — the (c) judgment. No second
conservatism is applied.

**Stock compensation subtracted in full [E5-06]:** yes, **and in the full amount the filing
discloses** — $1,956M for FY2025, being $426M of share-based plans expense plus $1,530M of
treasury shares issued for the 401(k) contribution. **That is 184% of FY2025 operating cash
flow.** *(Under [E3-70] even this is the floor, since the measure is market value.)*

### Great, good, or gruesome? **[E4-20]**

- [ ] great — [ ] good — [x] **GRUESOME**, and on the definition's own words rather than by
      inference.

*"Finally, the gruesome account both **pays an inadequate interest rate and requires you to keep
adding money at those disappointing returns.**"*

**Boeing pays a negative rate and required $23,832M of added deposits in October 2024.** That is
not an analogy; it is the definition satisfied literally. **[E4-43]'s guard is checked and does
not rescue it:** the *good* class passes — *"nothing shabby about earning $82 million pre-tax on
$400 million of net tangible assets"* — but the good class requires a positive return on the
added capital, and **[E5-40]** puts the satisfactory level at about **12% on retained capital**.
The return on the $23.8bn raised in FY2024 is, on the following year's owner earnings,
**negative**. And [E4-20]'s own escape clause — cash-consuming is gruesome *"unless the cash they
consume gets to earn a reasonable return"* — is closed by the same number.

**And note the additional feature that makes this worse than the textbook gruesome business:
Boeing did not even grow.** [E4-20]'s gruesome account *"grows rapidly, requires significant
capital to engender the growth, and then earns little or no money. Think airlines."* Revenue in
FY2025 ($89,463M) is **below** FY2018 ($101,127M) and units are 74% of the peak. **It consumed
the capital without the growth.**

### Staying power — score all three **[E5-11]**

*"(1) a large and reliable stream of earnings; (2) massive liquid assets and (3) no significant
near-term cash requirements. **Ignoring that last necessity is what usually leads companies to
experience unexpected problems.**"* Scored on the worst case, not the expected one **[E2-55]**.

**(1) A LARGE AND RELIABLE STREAM OF EARNINGS — FAILS.** Net earnings attributable to
shareholders: **−$636M, −$11,817M** *(FY2020)*, **−$4,202M, −$4,935M, −$2,222M, −$11,817M** —
six consecutive negative years FY2019-FY2024 — then **+$2,235M in FY2025, of which $9,566M is a
disposal gain**, then **−$435M in H1 2026.** BCA has not earned an operating profit since
FY2018. Reliable is the wrong word; positive is the wrong word.

**(2) MASSIVE LIQUID ASSETS — PARTIAL, AND DETERIORATING.** At 2026-06-30: **cash $7,239M +
short-term and other investments $12,783M = $20,022M.** Six months earlier it was $10,921M +
$18,479M = **$29,400M** — **down $9,378M in half a year**, of which $8,376M went to debt
repayment. [E5-39] is the standard: *"We will never be dependent on the kindness of
strangers"* — **no bank lines counted, no commercial paper, nothing depended on.** On that
standard the number is $20.0bn, and the run rate against it is computed below. [E2-64]'s
offensive reading — a balance sheet built for the storm is also built to buy in it — does not
apply: Boeing bought Spirit with **stock** (22,977,008 shares) because it did not have the cash.

**(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — FAILS, AND THIS IS THE ONE THAT USUALLY
KILLS.** Assembled from the filings, all dated 2025-12-31 unless stated:

| the near-term claims | amount |
|---|---|
| scheduled debt principal, next three years (the 10-K's own figure) | **$15,493M** *("approximately $15.5 billion … over the next three years")* |
| — of which FY2026 | $8,351M *(largely settled: H1 2026 debt repayments were $8,376M)* |
| airplane financing commitments, total | **$15,229M** |
| — **of which to customers Boeing believes are BELOW investment grade** | **$11,904M** |
| — earliest potential funding, 2026 / 2027 / 2028 | $2,362M / $4,228M / $3,715M |
| accrued **"Forward loss recognition"** — contracted future cash losses | **$6,711M** |
| accrued **"Other customer concessions and considerations"** | **$1,696M** |
| standby letters of credit and surety bonds | **$3,295M** |
| mandatory convertible preferred dividends | **up to $345M a year to 2027-10-15** |
| pension: gross benefits paid, per year, against a $51,425M PBO | **$4,507M** |
| non-prosecution agreement, in escrow | **$689M** |

**And the item that is not a maturity but is the real one: $64,059M of advances and progress
billings at 2026-06-30.** [E3-52] is the right corpus row and it must be read in **both**
directions. Float and deferred taxes are *"liabilities **without covenants or due dates**
attached to them … the benefit of debt … but saddle us with none of its drawbacks."* Customer
advances share the covenant-free, long-dated form — **and they differ in the one way that
matters: they are discharged by building aircraft, and on the loss-making programmes the cost of
building exceeds the cash received.** That is what a reach-forward loss *is*. **Boeing holds
$64bn of customers' money and expects to lose a further $4.9bn discharging the 777X portion of
it. This is the inverse of float:** float is money you hold and invest, with the loss capped at
the underwriting result; this is money you have already spent, with the obligation costing more
than the cash.

*The fair counter-point, stated: Boeing has no financial covenants that this run could find, the
maturity ladder after FY2026 is modest ($4.4bn, $2.7bn, $2.5bn), the mandatory convertible
settles in **shares** not cash, and the pension is roughly funded ($51,425M PBO against ~$47bn
of assets, net accrued liability $4,108M). A near-term default is **not** the named death.*

**[E2-54] — THE COVERAGE TEST, AND IT IS THE CLEAREST FAIL IN THE FILE.**
*"whenever someone creates a capital structure that does not allow **all interest, both payable
and accrued, to be comfortably met out of current cash flow net of ample capital expenditures —
zip up your wallet.**"*

| | cash flow net of capex | interest and debt expense | coverage |
|---|---|---|---|
| FY2018 (pre-break) | $15,322 − $1,722 = **+$13,600M** | $475M | **28.6×** |
| FY2023 (best post-break year) | $5,960 − $1,527 = **+$4,433M** | $2,459M | **1.80×** |
| **FY2024** | −$12,080 − $2,230 = **−$14,310M** | $2,725M | **negative numerator** |
| **FY2025** | $1,065 − $2,942 = **−$1,877M** | **$2,771M** | **negative numerator** |
| **TTM to 2026-06-30** | $3,639 − $3,849 = **−$210M** | ~$2,700M | **negative numerator** |

**Capex comes out first, and when it does there is nothing left to pay interest with in three of
the last four periods.** The interest is being paid out of customer advances and the balance
sheet. **[E2-54] FAILS.** And [E5-29]'s guard is checked: this is not volatility being mistaken
for risk — a volatile earnings stream with certain coverage passes, and **this coverage is not
certain, it is absent.**

**Leverage, named and quantified [E4-16, E3-29] — no ratio ceiling exists in this framework and
the corpus supplies none for subject companies, so here are the numbers and the judgment.**
Total debt **$45,900M** at 2026-06-30 ($4,565M current + $41,335M long-term) against **$20,022M**
of liquid assets: **net debt $25,878M**. Total assets $165,870M on total equity $6,115M —
**27:1**. On [E2-43]'s scoped denominator, tangible equity is **negative** (equity $5,454M less
goodwill $17,275M less acquired intangibles $1,567M at 2025-12-31). **[E4-16]:** *"Whenever a
bright person, a really bright person, goes broke that has a lot of money, it's because of
leverage."* The judgment: **this is a leveraged balance sheet carried by customer prepayments and
kept solvent in 2024 by a $23.8bn equity issue, and the framework's own [E2-55] standard —
*"we do not wish it to be only likely that we can meet our obligations; we wish that to be
certain"* — is not met.**

### THE TEN-YEAR SHARE COUNT — because the brief asked, and the answer is larger than it looks

| | shares |
|---|---|
| weighted-average basic, FY2015 | 686.9M |
| weighted-average basic, **FY2018 trough** | **579.2M** |
| weighted-average basic, **FY2019 trough** | **565.4M** |
| weighted-average basic, FY2023 | 606.1M |
| weighted-average basic, FY2024 | 647.2M |
| weighted-average basic, **FY2025** | **759.8M** |
| **on the cover of the 10-Q for 2026-06-30** | **790,370,020** |
| **plus mandatory conversion, on or about 2027-10-15** | **+33,511,000 to +40,215,500** *(5,750,000 × 5.8280 to 6.9940)* |
| plus $230M Spirit Exchangeable Notes at 6.7067 per $1,000 | +~1.5M |
| **contracted fully-diluted count** | **≈824M to 832M** |

**Ten-year change, FY2015 → FY2025: +10.6% basic (+9.7% diluted).** That understates it badly,
because FY2015 is mid-buyback. **Against the FY2019 trough the count is up 34.4% already and is
contracted to reach +46% to +47%.** And the common ranks **junior** to the preferred for both
dividends and liquidation. The common dividend has been **suspended since 2020** and the only
dividend paid is up to $345M a year on the preferred.

**Set that against $43,441M of buybacks in FY2013-FY2019.** Boeing retired shares at prices it
later issued at a large discount to. That is the [E5-24] finding recorded at Q3, and its Q4
consequence is this: **the owner's claim on whatever Boeing eventually earns has been diluted by
roughly a third, and the dilution is not finished.**

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24]**

**Modelled from EXPOSURE, not experience [E4-40]** — *"all of us in the industry made a
fundamental underwriting mistake by focusing on experience, rather than exposure."* The bear case
is stated as [E4-51] requires: so that a holder would accept it as fairly put.

**DEATH 1 — THE ACCOUNTING QUANTITY UNWINDS, AND THE DEFERRED PRODUCTION COSTS BECOME CHARGES.**
*The mechanism.* Programme accounting capitalises the excess of early-unit cost over the
estimated average cost across the accounting quantity. The filed balances at 2025-12-31: **737
deferred production costs $11,777M** (up from $9,679M) **plus $750M of unamortised tooling**;
**787 deferred production costs $13,859M** (up from $13,178M) **plus $1,366M of tooling and
$932M of supplier advances**. Recovery is asserted against the accounting quantity — and the
accounting quantity **rose in FY2025 on all three programmes: 737 from 11,600 to 12,400 (+800),
787 from 1,800 to 1,900, 777X from 500 to 650.** Each increase lowers estimated average cost and
therefore raises reported margin. **And $2,198M of the 787 balance is expected to be recovered
*"from units included in the program accounting quantity that represent expected future
orders"* — $2.2bn of spent cash whose recovery depends on orders that do not exist.**
*Quantified.* If the 737 rate does not reach and hold 47, or a quality event recurs, or demand
softens, the accounting quantity must come down. A 10% reduction on the 737 spreads $12,527M of
unrecovered cost over 1,240 fewer units, and the 777X is the worked precedent of what happens
next: **$14,891M of cumulative reach-forward losses on a single programme.** A 737 or 787
reach-forward loss of even half the 777X's two-year total ($8,398M) — roughly **$4.2bn — exceeds
two-thirds of total equity ($6,115M) and returns Boeing to negative book equity**, where it sat
at every year-end from 2019 to 2024 and at **−$23,552M** as recently as 2024-09-30.
*Likelihood:* **[x] a real possibility.** Not a certainty: the 737 rate is rising and deliveries
grew 72% in FY2025.

**DEATH 2 — THE CUSTOMER-ADVANCE TREADMILL STOPS. This is the one the brief asked about, and the
answer is yes, unambiguously.**
*The mechanism.* Boeing's operating cash flow is, to a first approximation, the change in what
its customers and suppliers have lent it. Filed, from the cash-flow statements:

| $M | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | **H1 2026** |
|---|---|---|---|---|---|---|---|
| **operating cash flow** | (18,410) | (3,416) | 3,512 | 5,960 | (12,080) | 1,065 | **1,185** |
| change in advances and progress billings | (1,060) | 2,505 | 108 | 3,365 | 4,069 | (723) | **+4,660** |
| change in accounts payable | (5,363) | (3,783) | 838 | 1,672 | (793) | 724 | **+1,381** |
| **both lines together** | (6,423) | (1,278) | 946 | **5,037** | 3,276 | 1 | **+6,041** |
| **OPERATING CASH FLOW EXCLUDING BOTH LINES** | (11,987) | (2,138) | 2,566 | **+923** | **(15,356)** | **1,064** | **(4,856)** |

**Read the last column. In the six months to 2026-06-30 Boeing reported +$1,185M of operating
cash flow while taking $6,041M of additional money from its customers and suppliers. Excluding
those two lines the business consumed $4,856M of cash in half a year.** And FY2023 — the best
post-break year — was 84% the same thing: $5,037M of the $5,960M. **The queue's `wc_note` is
confirmed exactly: accounts payable moved −$3,783M in FY2021 against operating cash flow of
−$3,416M, which is 111%.**
*Quantified.* Advances rose $4,655M in one half-year (to $64,059M). **They fell $723M in FY2025.**
If they merely stop growing — the FY2025 experience, not a hypothetical — the half-year run rate
of −$4.9bn implies roughly **−$7bn to −$9bn a year against $20,022M of liquid assets: under
three years before the equity market is needed again.** In October 2024 it was needed and it
cost the register $23.8bn and 129 million shares.
*Likelihood:* **[x] a real possibility**, and it has a filed precedent in FY2025.

**DEATH 3 — THE 35% OF THE ORDER BOOK THAT IS NOT CERTIFIED.**
*The mechanism.* **37% of undelivered 737 orders are for the MAX 7 and MAX 10 — models that are
not certified**, four annual reports after the FY2022 10-K said they were *"currently going
through FAA certification."* The 777-9 is not certified and first delivery has moved 2020 → late
2023 → 2025 → 2026 → 2027. Undelivered 777X firm orders are **560 units**.
*Quantified.* 37% of 4,404 undelivered 737 orders is roughly **1,630 aircraft**; with the 560
777Xs that is **~2,190 of roughly 6,130 undelivered firm orders — 36% of the unit backlog —
awaiting a certificate Boeing does not control.** Undelivered MAX 7/10 inventory has sat at
"approximately 35" airframes at three consecutive year-ends and **"approximately 40" at
2026-06-30** — aircraft built, paid for in part, and undeliverable. And the customers hold
remedies: *"A number of our customers have contractual remedies, including compensation for late
deliveries or rights to reject individual airplane deliveries based on delivery delays."*
*Likelihood:* **[x] likely** that certification slips again at least once; **a low-level
possibility** that any of the three is never certified.

**DEATH 4 — [E2-27]'s OWN MECHANISM, AND IT IS THE ONLY ONE THAT IS NOT BOEING-SPECIFIC.**
*"Viewed individually, each company's capital investment decision appeared cost-effective and
rational; viewed collectively, the decisions neutralized each other and were irrational."*
Boeing plans 47 a month and a new 737 line; Airbus guides to ~870 deliveries in 2026 and is
ramping the A320 family. Two suppliers adding narrowbody capacity into the same slot demand, in
a market whose backlog is a decade deep, is the textile-loom shape **[E3-62]**: the productivity
gains flow to the airlines, not to the ribs of the owner. *Likelihood:* **[x] a low-level
possibility** on the decade the filings cover; the backlog is genuinely long.

**WHAT DOES *NOT* KILL IT, SO THE BEAR CASE IS NOT OVERSTATED.** Boeing is not going to be
liquidated. The backlog is $682bn; the type certificates have fifty years of life in them; BGS
earns 18-19%; the maturity ladder past FY2026 is modest and this run found no financial
covenants; the mandatory convertible settles in shares; the pension is roughly funded; the US
government will not let the only American large-jet airframer and the KC-46/VC-25B/F-15EX
supplier fail. **The death here is not insolvency. It is the same as ORCL's in form and worse in
substance: a company that arrives in 2032 larger, more diluted, and worth no more per share,
having paid out its cash in reach-forward losses, concessions, rework and interest.**

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** — *recorded, not governing;
  Q2 already closed the file.* **OUT on the business:** gruesome on [E4-20]'s literal definition,
  [E2-54] coverage negative in three of four recent periods, [E5-11] strengths (1) and (3) failed
  and (2) deteriorating, and owner earnings negative on **every** window describing the business
  that exists now, at **both** (c) ends, and on the trailing twelve months.

### THE [E5-11] VERDICT AGAINST THE THREE SHAPES — ORCL, ARM, BE

| | **ORCL** (2026-09-06) | **ARM** (2026-09-11) | **BE** (2026-09-12) | **BOEING** |
|---|---|---|---|---|
| where it closed | Q4 OUT | Q4 OUT | Q2 OUT | **Q2 OUT** |
| the shape | **contracted not to stop** | **earns nothing after paying its people** | **too little filed history to judge** | **see below** |
| (1) reliable earnings | **passes** — a $19.8bn annuity | **passes** — royalties on old designs | thin | **FAILS** — six negative years, BCA negative seven |
| (2) liquid assets | $63.9bn | $3.9bn, no debt | adequate | **$20.0bn, down $9.4bn in six months** |
| (3) near-term cash needs | **FAILS** — ~$80.7bn/12mo | **passes** | passes | **FAILS** — $15.5bn of debt in three years, $15.2bn of financing commitments ($11.9bn sub-IG), $6.7bn of accrued forward losses |
| [E2-54] coverage | **negative** (−$23,686M) | positive | n/a | **negative** (−$1,877M FY2025; −$210M TTM) |
| filed history | long | short (post-IPO) | **too short** | **18 years — the longest in the group** |

**Boeing carries BOTH the ORCL feature and the ARM feature, and neither is the fourth thing.**

- **The ORCL feature is present.** $15,229M of airplane financing commitments ($11,904M to
  sub-investment-grade customers), $6,711M of accrued forward losses, and $64,059M of customer
  advances discharged by building at a negative margin. Boeing is **contracted not to stop.**
- **The ARM feature is present and it is WORSE than ARM's.** ARM's finding was stock compensation
  equal to 97% of operating cash flow over its whole listed life. **Boeing's equity-settled
  compensation was $1,956M against $1,065M of operating cash flow in FY2025 — 184% — and
  $1,119M against $1,185M in H1 2026, 94%.** Boeing pays its retirement match in stock. **The
  highest equity-compensation-to-operating-cash ratio this queue has recorded.**
- **The BE feature is absent.** Boeing has 18 years of filed annual history. Nothing here is
  UNKNOWABLE for want of evidence.

**AND THERE IS A FOURTH SHAPE. It needs its own name: THE CASH IS SPENT UNDOING PAST WORK.**
ORCL's cash bought datacentre assets that might yet earn; ARM's cash went to its own engineers,
who build the next architecture; BE's cash bought a factory it had too little history to judge.
**Boeing's cash goes to its own defects.** The filed lines, FY2023-FY2025 alone: **$14,891M of
cumulative 777X reach-forward losses** (fourteen years, no deliveries), **$964M of 767
reach-forward losses**, **~$5,000M of BDS fixed-price development losses in FY2024**,
**$10,882M of adverse cumulative catch-up adjustments in three years**, **$1,300M of abnormal
production costs** ($30M + $256M + $1,014M), **$1,500M of cash concessions to 737 MAX customers**
($0.2bn + $0.9bn + $0.4bn), **$443M of 737-9 customer considerations**, **$689M to the DOJ and
the families**, and **$1,696M still accrued as customer concessions owed.** None of it builds
anything. **Every dollar is the price of work already done badly, and the framework has no
category for a business whose principal use of capital is remediation — so it gets one here.**

**On [E4-20]'s savings-account image, the four shapes line up like this:** ORCL is an account
that keeps demanding deposits for a branch under construction. ARM is an account whose interest
is paid to the bank staff. BE is an account with no statement history. **Boeing is an account
that charges you for the last three years of its own errors, and asks you to top it up while it
does.**

---
⛔ **Q5 DOES NOT OPEN. Q2 returned OUT.** UNRESEARCHED and UNKNOWABLE both close the file and
neither is a pass; **OUT closes it permanently.** What follows is arithmetic, produced because
the operator's standing instruction of 2026-09-01 is that every run in this queue ends with a
price and a pass/fail line. It carries no entry language.

---
# COMPUTATION — NOT A CLEARANCE

*(Operator rule 3. Q1-Q4 did not each show IN; Q2 returned OUT. This block is a price, not a
verdict, and nothing in it may be read as an argument for or against buying.)*

**The inputs, each dated and sourced:**
- **price $210.45**, close of **2026-09-11**, Yahoo Finance — aggregator, live quote only, flagged.
- **shares 790,370,020**, cover of the 10-Q for the period ended 2026-06-30, **accession
  0001628280-26-050038**.
- **market capitalisation $166,333M.**
- **plus the prior claim:** $5,750M aggregate liquidation preference of the 6.00% Series A
  Mandatory Convertible Preferred, which ranks **ahead** of the common for both dividends and
  liquidation. **Total equity claim $172,083M.**
- **sovereign 5.35%**, 30-year US Treasury par yield, **2026-09-11**, struck from the Treasury's
  own daily curve. **The bare rate. No per-name premium added [E3-42].**

**1. THE YIELD — owner earnings ÷ market capitalisation, beside the sovereign.**

| construction | owner earnings | yield | vs sovereign |
|---|---|---|---|
| **TTM to 2026-06-30, D&A end** *(the end [E5-20] calls INVALID here)* | **−$585M** | **−0.35%** | **−5.70 pts** |
| **TTM to 2026-06-30, capex end** | **−$2,238M** | **−1.35%** | **−6.70 pts** |
| FY2022-2025 (4y), capex end | −$4,393M | −2.64% | −7.99 pts |
| FY2019-2025 (7y), capex end | −$6,955M | −4.18% | −9.53 pts |
| FY2024-2025 (2y), capex end | −$10,076M | −6.06% | −11.41 pts |
| *for reference only — a different company:* FY2014-2018 (5y) | +$9,129M | +5.49% | +0.14 pts |
| *for reference only:* **the best single year in 18 filed** (FY2018) | **+$13,398M** | **+8.05%** | **+2.70 pts** |

**Every construction describing the business that exists now is negative. The yield is negative
on both (c) ends and on every post-break window, including the trailing twelve months.**

**2. WHAT THE PRICE ALREADY ASSUMES — and this is the honest way to state it.**
A negative numerator has no growth rate that reaches a positive yield in finite time, so the
question is inverted and asked in dollars instead of percentages, as the brief requires:

- to yield the **5.35% sovereign** at $210.45, Boeing must earn **$8,899M** of owner earnings a
  year.
- to clear the **~10% floor [E4-28]**, it must earn **$16,633M**.
- **the most it has ever earned, in eighteen filed years, is $13,398M — in FY2018, on 806
  deliveries, with 579M shares and $13,847M of debt.**

**So: repeat the single best year in Boeing's filed history, exactly, and the buyer at $210.45
receives 8.05% — below the figure the corpus quits on** *("that's the figure we quit on … whether
short rates are 6 percent or whether short rates are 1 percent" — [E4-28])*. **On the full equity
claim including the preferred it is 7.79%.** To clear the floor the company must earn **24% more
than its best year ever**, while carrying **31% more shares than it had in that year** and
**33.5-40.2 million more contracted for 2027-10-15**.

*What the business has actually done, for the comparison [E4-35] demands:* revenue is **below**
FY2018, units are **74%** of FY2018, and owner earnings have been negative in five of the last
seven years. **[E4-35]'s base rate** — *"fewer than 10 of the 200 most profitable companies … will
attain 15% annual growth in earnings-per-share over the next 20 years"* — is not even the right
test here, because the required move is not growth from a base; it is a **return from negative to
a record, plus 24%.**

**3. WHAT YOU ARE PAID.** **−5.70 to −11.41 points versus the sovereign**, depending on
construction; **−6.70 points** on the trailing twelve months at the honest (c) end. **A buyer at
$210.45 is paid nothing and funds the shortfall.**

**IN WORDS, WHAT THE BUYER AT TODAY'S PRICE IS PAYING FOR.** $166.3bn (and a $5.75bn prior claim
ahead of it) buys: a $682bn backlog whose conversion is licensed by the FAA; 36% of that unit
backlog awaiting certificates the company does not control; a commercial segment that has lost
money for seven consecutive years while its only competitor earned a 10.4% margin on 32% more
deliveries; $64bn of customers' money that is discharged by building aircraft at a negative
margin; $25.6bn of production costs already spent and capitalised against units not yet ordered;
an equity-settled compensation bill that was 184% of last year's operating cash flow; and a share
count up a third from the trough with more contracted. **The buyer is not paying for earnings —
there are none. The buyer is paying for the proposition that a fourteen-year-late aircraft will
certify, that a regulator will consent to a higher rate, and that a duopoly position will
eventually be monetised by people who have not yet monetised it.** That proposition may come
true. **It is not a yield, and it is not what this framework buys.**

**THE FLOOR, FIRST [E4-28].** Honest pre-tax expectancy at this price: **negative on every
construction of the business that exists now; 8.05% even on a repeat of the best year in
eighteen.** **Below roughly 10% the name is not ranked — it is quit on, whatever the sovereign
is.** Boeing is quit on twice over: once at Q2 on the business, and once here on the arithmetic.
**The ranking lines are therefore not filled in** [E4-21, E3-45].

**Value as a round-number range [E4-01].** *"Using precise numbers is, in fact, foolish."*
On the only cash construction that describes the company as filed, **owner earnings are negative
and the owner-earnings value of the equity is not a positive number.** A round-number range is
refused rather than invented: **there is no owner-earnings value to state.** What can honestly be
said is that at the sovereign rate a business earning its own best-ever year would be worth
roughly **$250bn**, and one earning the pre-break five-year mean roughly **$170bn**, and one
earning what it actually earns, **nothing** — and the quote sits at $166bn. **Current price
$210.45.**

**WHICH BAR? NEITHER, and that is the finding.** The normal method [E4-11] needs a value to apply
a margin to; the screamer test [E4-01] needs a conservative case for the price to clear. **The
conservative case here is −$10,076M and the optimistic case describing this company is −$585M.
The price is above the whole range** — [E4-01]'s third outcome, *"no"*. **Windage count: one** —
the (c) judgment at Q4. No second conservatism was applied, and none was needed.

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Not opened as a hold/sell question — there is no position and none is contemplated.** Recorded
as the **refutation conditions** the framework requires of any closed file, pre-committed in
writing per **[E1-02]** — *"I believe in establishing yardsticks prior to the act"* — so that a
future re-opening is triggered by evidence and not by a price move.

**THESIS-BREAKING METRICS, each read off a 10-K, each with a threshold.** The file re-opens at
Q2 if **three or more** of these turn, and is re-read if any single one does:

1. **BCA posts a full-year operating profit.** Threshold: any positive number. This ends a
   seven-year run and is the single cleanest refutation of the [E2-53] finding.
2. **No new reach-forward loss on any programme for a full fiscal year**, with the accrued
   *"Forward loss recognition"* balance falling from **$6,711M** toward zero.
3. **The FAA concurrence condition disappears from the 10-K**, or the 737 rate reaches and holds
   a level Boeing sets rather than negotiates. Threshold: the sentence *"may only increase
   production rates … with the concurrence of the FAA"* absent from an annual report.
4. **BCA deliveries exceed 806** — the FY2018 peak — which is [E4-55] passing on the physical
   series rather than the dollar one.
5. **Owner earnings positive at the CAPEX end on a five-year mean**, with the full equity-settled
   compensation of $1.9bn+ a year subtracted. Threshold: > $0 on FY2022-2026 or later.
6. **[E2-54] coverage above 1× on a five-year basis**: operating cash flow less capital
   expenditure exceeding interest and debt expense.
7. **Accrued "Other customer concessions and considerations" falls materially from $1,696M**, the
   [E4-37] agony metric reversing.
8. **The 777-9, 737-7 and 737-10 are all certified and delivering**, removing the 36% of the unit
   backlog that depends on a third party's signature.

**THESIS-CONFIRMING METRICS** (the file stays closed while these hold): advances and progress
billings continuing to fund operating cash flow; the accounting quantity rising in years when
margin is needed; equity-settled compensation above 100% of operating cash flow; the share count
rising toward the contracted 824-832M.

**Next catalyst dates, filed:** Q3 2026 results (late October 2026) · **mandatory conversion of
the preferred, 2027-10-15** · the FY2026 10-K (late January 2027), which will show whether the
737 rate reached 47 and whether the 777-9 delivered in 2027 as now stated · the Fifth Circuit
appeal on the DOJ dismissal, pending.

**NO PRICE ALERT IS ARMED, and that is a rule not an omission** (the QLYS ruling, 2026-09-07).
**This name failed at Q2, on the BUSINESS. A price alert on a business finding is a category
error** — a lower price does not make a seven-year segment loss into a franchise, and [E5-35] is
the law: *"You can turn any investment into a bad deal by paying too much. What you can't do is
turn any investment into a good deal by paying little."* The reversal conditions above are read
off filings, on the schedule above.

- **VERDICT: [x] OUT** — *carried from Q2; not independently opened.*

---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN → Q2 OUT → file closed. Q3, Q4,
      the Q5 computation and Q6 are marked **RECORDED, NOT GOVERNING** at their heads.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN is on
      filed unit economics and the filed cash line. Q3's IN is the narrow corpus form — *the
      absence of a found disqualifier in the conduct of the management in place* — and is written
      as [E5-17] requires, with the record that would make it an OUT if the actors remained
      stated in full rather than hedged. **The moat class is NOT held PROVISIONAL:** ten peers
      were taken, Airbus included at ladder rung 3 with its limit stated.
- [x] Every UNRESEARCHED verdict names the artifact: **two, both inside the competitor row, both
      non-governing** — GE Aerospace's FY2025 10-K on EDGAR (absent from the row; nothing blocked
      it but time), and HEICO's ten-year share-count change (a split artifact, flagged rather than
      used). Also recorded: **the NTSB findings on the door plug are UNRESEARCHED from the
      filings** — *"NTSB" does not appear in the FY2025 10-K.*
- [x] No UNKNOWABLE verdict was returned. *(Boeing has 18 years of filed annual history; nothing
      here is indeterminate for want of evidence. That is the BE contrast.)*
- [x] **Step 0: the filing was read**, with accession numbers for seven 10-Ks, two 10-Qs, two
      proxies and four 8-K EX-99.1 releases. **Figure cross-checked:** FY2025 operating cash flow,
      XBRL $1,065M against the filed Consolidated Statements of Cash Flows *"1,065"*. Two further
      checks agreed (backlog $682,207M; advances $59,404M). **One cross-check DISAGREED and became
      the run's main arithmetic finding:** the *"Treasury shares issued for 401(k) contribution"*
      line, which exists in the filing and not in XBRL from FY2021 on.
- [x] **Owner earnings on a multi-year mean; eleven windows stated; the capex band disclosed as a
      judgment** with the D&A end declared **INVALID** under [E5-20] and the reason given from the
      filing. **Never via a net-income proxy** — and the FY2025 net income of +$2,235M is exactly
      why, since $9,566M of it is a disposal gain.
- [x] **Competitor row filled** — ten peers, same metric, same window, filing-sourced, with the
      Airbus ladder rung and the SPR deregistration accessions named.
- [x] **Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury),
      dated 2026-09-11.** The Airbus comparison is left in **euro, unconverted**, with the note
      that a valuation of Airbus would run against the EUR curve.
- [x] Value **refused** as a positive range rather than invented; the price is stated as a dated
      number.
- [x] **One bar chosen — neither applies, stated as the finding. Windage count: one.**
- [x] **Prices dated; the aggregator is used for the live quote only and flagged.** The share
      count came off a filing cover, not the aggregator.
- [x] Run committed to git after every gate, by file name.
- [x] `python tools/check_framework.py` run before the final commit.

## REGISTER
- **Verdict: [ ] IN  [x] OUT (about the business)  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
- **PASS/FAIL: FAIL. The file closed at Q2.** Q1 IN · **Q2 OUT** · Q3 IN and Q4 OUT recorded,
  not governing · Q5 not opened (computation only) · Q6 recorded as reversal conditions.
- **PRICE: $210.45** (close 2026-09-11) · **shares 790,370,020** (10-Q cover, period 2026-06-30,
  acc 0001628280-26-050038) · **cap $166,333M** · **sovereign 5.35%** (30-yr UST, 2026-09-11).
- **One line:** *The industry position is a franchise and Airbus is the one holding it — 793
  deliveries and a 10.4% commercial margin against Boeing's 600 and −17.1% in the same twelve
  months — so the environment cannot explain seven consecutive years of BCA operating losses; the
  737's output rate now requires FAA concurrence; the company's own MD&A forecasts intensifying
  price pressure; and the rebuilt owner-earnings range for the business that exists now is
  **−$10,076M to −$4,320M**, negative at both (c) ends on every post-break window and on the
  trailing twelve months.*
- **Not UNRESEARCHED and not UNKNOWABLE:** the evidence is in, it is 18 years deep, and it is not
  indeterminate.


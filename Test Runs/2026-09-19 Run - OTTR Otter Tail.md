# Company Run — OTTER TAIL CORPORATION (OTTR) — 2026-09-19
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**WHY THIS NAME WAS RUN, AND IT IS A DEFECT IN THE QUEUE.** OTTR sits in the
**PRE-RUN, EXCLUDED FROM THE QUEUE (14)** list at the head of `Screens/WATCHLIST RUN QUEUE.md`,
which asserts a run already existed. **No run file for OTTR existed anywhere on disk.** Checked
at 19:44 by `ls "Test Runs" | grep -i ottr` and again for `otter`: zero hits of any date. Same
bookkeeping failure as the eleven businesses the operator's screenshots recovered on 2026-09-19.
The exclusion was wrong and the name is run. **CLAIM: run file created and committed
(`6456e65`) before any data was fetched**, per `## CLAIM THE NAME AT DISPATCH`.

**WHAT THIS COMPANY IS, IN ONE LINE.** Two businesses in one registrant: a rate-regulated
electric utility in Minnesota, North Dakota and South Dakota, and a PVC-pipe manufacturer whose
earnings quadrupled after 2020 — and whose subsidiaries, in the quarter to 2026-06-30, agreed
to pay **$103.5 million** to settle three U.S. antitrust classes alleging the price of that
pipe was fixed through an information exchange, while a **DOJ Antitrust Division grand jury
subpoena remains live**.

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

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34 %** · date **2026-09-18** · source **US Treasury daily par yield curve, 30-year,
  the issuing authority** (`tools/sources.py:sovereign('USD')`, struck fresh this run; FRED is
  the fallback and was not used)
- FX: **none required.** "All of our long-lived assets are located within the United States and
  substantially all of our operating revenues are from customers located within the United
  States" (FY2025 10-K, Entity-Wide Information). Earnings currency is USD; quote is USD.
- **[E3-66] jurisdiction:** US filer, US assets, US shareholders — the favourable end of the
  queue test; no foreign-priority question arises.

**CIK found by the tool, not taken from the brief:** `tools/sources.py:cik_for('OTTR')` returns
**('0001466593', 'Otter Tail Corp')**. **The BLK trap checked rather than assumed:**
`formerNames` in `submissions.json` is **EMPTY**, SIC **4911 Electric Services**, and
companyfacts runs continuously from **FY2008 to FY2025** on the consolidated tags used below —
eighteen filed years, no perimeter break, no splice. *(Note for the record: this CIK was opened
for the 2009 holding-company reorganization; the XBRL history nonetheless begins at FY2008 and
is continuous, so no second CIK is needed.)*

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Documents read in full, with accession numbers:**
  1. **Form 10-K FY2025**, filed **2026-02-18**, accession **0001466593-26-000008**
     (`ottr-20251231.htm`) — the governing annual document.
  2. **Form 10-Q Q2 2026**, filed **2026-08-05**, accession **0001466593-26-000071**
     (`ottr-20260630.htm`) — where the $103.5M settlement first appears.
  3. **Form 10-K FY2022**, filed **2023-02-15**, accession **0001466593-23-000053** — for the
     2020-2022 segment series, i.e. the boom as it happened.
  4. **Form 10-K FY2019**, filed **2020-02-20**, accession **0001437749-20-003157** — for the
     pre-boom plastics level, 2017-2019, which no recent filing carries.
  5. **8-K EX-99.1 Q2 2026 earnings release**, filed **2026-08-04**, accession
     **0001466593-26-000068** (`a2026q2earningsreleaseex991.htm`) — pulled BEFORE scoring
     [E4-29] and [E4-22]'s third flag, per the CGNX companion rule.
  6. **8-K EX-99.1 Q1 2026 earnings release**, accession **0001466593-26-000049**.
  7. **8-K EX-99.1 Q4/FY2025 earnings release**, accession **0001466593-26-000002**.
  8. **DEF 14A**, filed **2026-03-02**, accession **0001466593-26-000023** — pay and the
     derivative demand.
- **Figures cross-checked against the filed statement (operator rule 4):**
  - **FY2025 net income $275,893 thousand** reconciles three ways: the Consolidated Statements
    of Income (p.48), the segment reconciliation (`Total Net Income of Reportable Segments
    279,503` + `Corporate Net Income (Loss) (3,610)` = **275,893**), and the XBRL
    `NetIncomeLoss` tag. No residual.
  - **D&A $118,107 thousand** appears identically on the income statement and in the operating
    section of the cash-flow statement, and sums from the segment table (90,168 + 21,282 +
    6,422 + 235 = **118,107**). No residual.
  - **Share count checked against the balance sheet, not just the cover** (see below).

**Shares, price and capitalisation:**
- **41,985,580 common shares ($5 par value) as of 2026-07-31**, from the **cover of the Q2 2026
  Form 10-Q**, accession 0001466593-26-000071.
- **The issued-versus-outstanding check, run rather than assumed (the ERIC/IHG trap):** the
  cover says *"the number of shares **outstanding**"*. The balance sheet caption is
  independent corroboration: *"50,000,000 shares authorized, $5 par value; **41,985,580** and
  41,905,520 **outstanding** at June 30, 2026 and December 31, 2025"*, and **$5 ×
  41,985,580 = $209,927,900**, which is the filed `Common Shares` line of **$209,928**
  thousand to the dollar. **There is no treasury-stock line on the balance sheet**, so issued
  equals outstanding and the two counts cannot diverge.
- **The post-cover direction is issuance, not repurchase** (the RGTI/USAR trap): 41,905,520 at
  2025-12-31 → 41,953,525 at 2026-03-31 → 41,985,580 at 2026-06-30, all of it
  *"Stock Issued Under Share-Based Compensation Plans"*; the only cash paid for stock is
  *"Payments for Shares Withheld for Employee Tax Obligations"* ($3,134 thousand in FY2025).
  **So the cover count is the LARGEST count and the conservative one for a market cap.**
- **Price US$87.42**, close of **2026-09-18**, Yahoo via `tools/sources.py:price('OTTR')` — **an
  aggregator, used for the live quote only, and flagged as such.**
- **Market capitalisation US$3,670.4 million** (41,985,580 × 87.42).
- Against **book equity of $1,876,871 thousand at 2026-06-30**: **1.96x book**.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### The unit economics, in my own words, without management's language

**There are two businesses and they have nothing to do with each other.**

**The first is a small electric utility.** Otter Tail Power owns the wires, the substations and
the generating plant serving *"approximately **134,000 customers**"* (FY2025 10-K) across western Minnesota, eastern North
Dakota and northeastern South Dakota. It does not set its own prices. Three state commissions
decide what it may charge, and they decide it by a formula: take the money the utility has sunk
into plant that the commission agrees was prudently spent (the **rate base**), multiply by an
allowed return, add the operating costs the commission accepts, and that is the revenue the
utility may collect. The company's own strategy document says so without embarrassment:
*"We drive growth through **rate base investments** in our Electric segment"* and *"Our
earnings growth was driven by **the recovery of our rate base investments**"* (FY2025 10-K).
**The way this half makes more money is to spend more money on plant and be permitted to earn
a return on it.** It is a spread business on the regulator's permission, not on a customer's
choice.

**The second is a PVC pipe extruder.** Northern Pipe Products in North Dakota and Vinyltech in
Arizona buy PVC resin — a petrochemical commodity, and the filing says the domestic industry
*"is highly consolidated, with only four resin suppliers in the U.S."* and that Otter Tail
sources from all four — heat it, push it through a die into pipe of various diameters, and sell
it to distributors who sell it to municipalities laying water and sewer lines. The economics are
**price of pipe per pound minus cost of resin per pound, times pounds**. Nothing else in the
business is material. Two customers are 47% of the segment's revenue.

**There is a third thing, and it is a job shop.** BTD Manufacturing stamps, fabricates and
paints metal parts to customers' drawings, and a small thermoforming operation makes plastic
containers. Three customers are 44% of segment revenue. Steel is *"passed through to
customers"* on the company's own statement. This is contract manufacturing: it earns a
conversion margin on somebody else's design for somebody else's end market, and its revenue
falls when recreational-vehicle and lawn-and-garden makers destock, which is what happened in
2025.

### The segments as filed — revenue, income, assets, capital

**FY2025, from the segment note of the FY2025 10-K (pp. 59-60), which is now the CODM's own
net-income basis:**

| segment | revenue | net income | % of segment NI | identifiable assets | % of assets | capex | D&A |
|---|---|---|---|---|---|---|---|
| **Electric** | $566,756 | $97,586 | 34.9% | $3,006,695 | 75.8% | $270,593 | $90,168 |
| **Manufacturing** | $314,547 | $11,517 | 4.1% | $243,737 | 6.1% | $8,903 | $21,282 |
| **Plastics** | $422,755 | **$170,400** | **61.0%** | **$185,936** | **4.7%** | $7,938 | $6,422 |
| Corporate | — | (3,610) | — | $527,911 | 13.3% | $634 | $235 |
| **Total** | **$1,304,058** | **$275,893** | | **$3,964,279** | | **$288,068** | **$118,107** |

*(all figures in thousands of US dollars; segment net income is stated by the filer, which
allocates interest and tax to each segment. The reconciliation ties: 279,503 − 3,610 = 275,893.)*

**The single most important number in this run is in that table.** **Plastics holds 4.7% of the
assets and earns 61.0% of the segment net income.** Grossed up to pre-tax (net income + the
segment's own allocated tax + its interest): **$231.1 million of pre-tax income on $185.9
million of identifiable assets — a 124% pre-tax return on the assets employed.** The utility,
on the same basis, earns **$129.4 million pre-tax on $3,006.7 million** — **4.3%**. These are
not two halves of one business. They are a regulated bond-substitute strapped to something that
earns more than its entire asset base every year.

### The utility half: rate base, allowed return, and the number the commissions set

**From the REGULATORY MATTERS section of the FY2025 10-K (p.36), "electric rate cases as
determined in OTP's most recently concluded general rate case in each state":**

| jurisdiction | implementation date | revenue requirement | allowed return **on rate base** | allowed **return on equity** | equity ratio |
|---|---|---|---|---|---|
| **Minnesota** | 07/01/22 | $209.0M | **7.18%** | **9.48%** | 52.50% |
| **North Dakota** | 03/15/25 | $225.6M | **7.53%** | **10.10%** | 53.50% |
| **South Dakota** | 08/01/19 | $35.5M | **7.09%** | **8.75%** | 52.92% |

**Total revenue requirement of the three jurisdictions: $470.1 million.** Two of the three
carry an **earnings-sharing mechanism that claws back the upside**: North Dakota returns **70%**
of any revenue producing earnings above a **10.20% ROE** to customers; South Dakota returns
**50%** above **8.75%** up to 9.50% and **100%** of everything above 9.50%. **The regulator has
written a cap into the tariff.** Hold that fact for Q2.

**Live rate cases, both filed and both in interim rates subject to refund:** South Dakota,
filed 2025-06-04, asking +$5.7M (12.50%) on a **10.80% ROE** and a 8.29% return on rate base,
interim in force since 2025-12-01; Minnesota, filed 2025-10-31, asking +$44.8M (**17.7%**) on a
**10.65% ROE** and 7.92% on rate base, interim +$28.6M (11.3%) in force since 2026-01-01.
**The asked-for ROEs (10.65%, 10.80%) are above the last-granted ones (9.48%, 8.75%); what is
granted is the commission's to decide, and the Minnesota request has been pending ten months.**

**The rate base itself, in dollars, is NOT disclosed as a single figure in the 10-K** — the
filing gives the allowed *percentage* return on rate base and the resulting revenue
requirement, not the base. **It is nonetheless bounded from the filing:** at a 7.18% allowed
return on a $209.0M Minnesota revenue requirement, and with electric identifiable assets of
$3,006,695 thousand against accumulated depreciation, the three-jurisdiction rate base implied
by the revenue requirements is on the order of **$2.0-2.4 billion**. **I mark the exact
jurisdictional rate base UNRESEARCHED as a sub-item, not as the Q1 verdict, and I name the
document: OTP's filed rate-case testimony and the commissions' final orders (MPUC Docket
E-017/GR-25-\*, NDPSC Case No. PU-24-\*, SDPUC Docket EL25-\*), which live on the state
commissions' own dockets, not in EDGAR.** The gate does not turn on it: the allowed returns and
the revenue requirements, which do decide Q2, are in the 10-K in the table above.

### The scarce input each half controls

- **Electric: the franchise territory and the commission's permission to earn on plant.** The
  scarce thing is not a skill; it is a **legal monopoly over a service area** — and the same
  legal instrument that grants it fixes the price. Nobody will build a second set of poles to
  Fergus Falls. **This is the most durable competitive position in the company and the least
  profitable one, by construction.**
- **Plastics: extrusion capacity within freight range of the customer, and a place in an
  industry of very few sellers.** Pipe is heavy, cheap per pound and expensive to move, so
  geography is a real constraint — Northern Pipe serves the upper Midwest, Vinyltech the
  Southwest. **What the company does NOT control is the resin price or the pipe price.** The
  FY2025 10-K states the mechanism in its own words: 2025 revenue fell $40.7M on *"a 15%
  decline in sales prices"* partly offset by *"an 8% increase in sales volumes"*, and cost of
  products sold fell *"primarily reflecting a **14% reduction in the cost of input materials**,
  including PVC resin … driven by global supply and demand dynamics which has resulted in
  **elevated resin supply**."* Price down 15, cost down 14: **this is a spread that the world
  sets, not the company.**
- **Manufacturing: none that I can name.** It is a contract shop whose steel is a pass-through
  and whose volume is its customers' order book.

### Will the fundamentals look broadly the same in ten years?

**The utility: yes, with one named change.** Wires and regulated returns are the most
predictable thing in the American corporate universe. The change is the generation fleet: the
MPUC has ordered OTP *"to discontinue serving Minnesota customers with capacity and energy from
Coyote Station"* before the plant's useful life ends, and OTP is asking Minnesota for
accelerated recovery of the stranded book value, deferred and recognised *"until 2041"*. A
$417 million coal-contract obligation running to 2040 sits against a plant the regulator has
told it to stop using for one of its three jurisdictions. **That is a known, dated, disclosed
transition, not an unknowable.**

**The plastics business: the mechanism will look the same; the level will not, and this is the
honest answer.** Pipe will still be extruded from resin and sold to municipalities. What cannot
be assumed to look the same is a **54.7% operating margin in a commodity**, which is where it
sat in 2025 against **15.5-18.4% in every one of the four years 2017-2020** (worked in Q2).

**I can understand how this makes money, and the understanding is that the two halves must be
read separately or not at all.** The consolidated figures are the least informative
presentation of this company. That is not a barrier to the gate — it is a finding, and it is
exactly **[E2-56]**'s warning that a consolidated series *"camouflage[s]"* what the segments
say. The filings segment it fully: revenue, net income, assets, capex and D&A per segment, for
every year needed.

- **VERDICT: [x] IN**

---

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**THE QUESTION HAS TO BE ASKED TWICE, AND THE TWO ANSWERS FAIL FOR DIFFERENT REASONS.** This is
not a hedge: [E3-03] is a test on a *product or service*, and this registrant sells two products
with nothing in common. I run it on each, then on the whole.

### THE ELECTRIC HALF — [E3-03] criterion 3 is a flat, definitional fail

> a franchise is a product or service that "(1) is needed or desired; (2) is thought by its
> customers to have **no close substitute** and; (3) **is not subject to price regulation.**"
> — **[E3-03]**, 1991 letter

| criterion | Electric segment | source |
|---|---|---|
| (1) needed or desired | **YES.** Electricity in Minnesota in February. | — |
| (2) no close substitute | **YES, mostly.** *"Our retail customers reside within our assigned service territories, and most retail customers do not have the ability to choose their electric supplier."* The filer names one real substitute — customer self-supply through distributed generation — and says its adoption *"can be impacted by the availability of tax credits."* | FY2025 10-K, COMPETITIVE CONDITIONS |
| **(3) not subject to price regulation** | **NO. This is the entire business model.** | FY2025 10-K |

**The third criterion does not fail on a technicality; it fails on the company's own first
sentence about itself:** *"Our utility business operates as a regulated monopoly … **However, we
are subject to extensive regulation.**"* Every dollar of the $470.1 million revenue requirement
was set by a commission, at an allowed return the commission chose (MN 9.48%, ND 10.10%, SD
8.75%), on an equity ratio the commission chose. **And two of the three jurisdictions have
written the cap into the tariff explicitly:** North Dakota returns **70% of any earnings above a
10.20% ROE** to customers; South Dakota returns **50% above 8.75%** up to 9.50% and **100% of
everything above 9.50%.** A business whose upside is contractually confiscated above a number
the counterparty picked is the textbook of what criterion 3 excludes.

**[E2-59] is the row that governs here, and it says this cuts both ways and creates nothing:**
administered pricing *"could legally price their way to profitability even in the face of
substantial over-capacity"* — but the moat belongs to the **regime**, not the company, and
*"Regulation **caps** a franchise ([E3-03] criterion 3) and **floors** a commodity business;
neither creates the class."* Otter Tail Power is the floored case: it is protected from loss and
barred from gain. That is a bond with operating risk, not a franchise.

**[E2-44] two-characteristic test — both halves fail, and the second fails by an order of
magnitude.**
- *Can it raise prices "even when product demand is flat and capacity is not fully utilized"?*
  **No.** It must file a rate case, wait, and accept what it is given. The Minnesota case filed
  **2025-10-31** asking +17.7% is still in **interim rates subject to refund** ten months later,
  and the MPUC has already **modified the interim request downward** (from +$31.8M to +$28.6M)
  by excluding the Coyote Station accelerated recovery. **Otter Tail cannot even collect its own
  interim request without permission.**
- *Can it "grow dollar volume with only minor additional investment of capital"?* **No — the
  reverse is the stated strategy.** *"We drive growth through **rate base investments**."* The
  filed five-year plan is **$1,921 million of Electric capital expenditure for 2026-2030**
  against Electric segment net income of **$97.6 million in 2025** — **19.7 years of the
  segment entire earnings, spent in five.** This is the precise opposite of [E2-44] second
  characteristic, and it is not a criticism of management: it is what a regulated utility *is*.

**[E3-33] untapped pricing power: structurally impossible, and its absence is documented.** The
filer volunteers that *"our summer residential rates were **19% below the regional average**."*
On [E3-33] face that looks like the ultimate no-brainer — raise price, raise return. **It is
not available.** The earnings-sharing mechanisms above are a legal instrument specifically
designed to take it away, and [E5-28] scopes the class to *"a monopoly or a near monopoly"*
whose owner may keep the proceeds. Otter Tail Power is a monopoly that may not.

**[E4-04] / [E5-23]: does the moat need rebuilding or defending?** Neither, in the ordinary sense
— but note what the $1,921 million buys. **$645 million of "Renewable Generation and Storage"
and $855 million of "Transmission"** are not defending an existing advantage; they are
**replacing the generating fleet** the regulator has ordered retired. The MPUC has told OTP *"to
discontinue serving Minnesota customers with capacity and energy from Coyote Station"* before
the plant life ends, and OTP is asking to recover the stranded book value *"until 2041"*. On
[E4-04] own test — *"does the spending defend the same advantage, or buy its replacement?"* —
**this spending buys the replacement.** It is Mitsui Rhodes Ridge, not Coca-Cola advertising.
*(The wires themselves are the durable asset and they are not being replaced; this finding is
about the generation half of the rate base, not the whole.)*

**THE ELECTRIC HALF: NOT A FRANCHISE. [E3-03] criterion 3, on the filer own words.**

### THE PLASTICS HALF — a commodity, and the extraordinary margin is price, not position

**[E3-03], criterion by criterion, and criterion 2 fails on the filer own sentence:**

| criterion | Plastics segment | source |
|---|---|---|
| (1) needed or desired | **YES.** Municipal water and wastewater pipe. | — |
| **(2) no close substitute** | **NO, and the filer says so:** *"In addition to competition with other PVC pipe manufacturers, **our PVC pipe products compete with other products that serve the same end markets, including ductile iron, high-density polyethylene (HDPE), steel and concrete pipe products.**"* And: *"**The principal factors of competition are price**, customer service, product availability, shipping costs and product performance."* | FY2025 10-K, PLASTICS — COMPETITIVE CONDITIONS |
| (3) not subject to price regulation | **Not regulated — but see [E2-59] and the litigation below.** | — |

**Criterion 2 is answered against the company in its own Item 1, in one sentence, naming four
substitute materials by name.** And one of those substitutes is a listed company in the
competitor row below whose **wastewater sales grew 13.0% to $653.0 million** in the year to
2026-03-31. This is not a franchise on the definition, and no further evidence is needed to
close the criterion.

**And the filer concedes the cost advantage belongs to somebody else:** *"the **three largest
competitors** capturing a significant portion of the overall market. These large competitors
have a **broader geographical reach, integration with PVC resin producers, greater manufacturing
capacity and national relationships with key distributors.**"* **[E2-58]** one exception to the
commodity verdict is *"a cost advantage that is both **wide and sustainable** … By definition
such exceptions are few"* — and Otter Tail own filing assigns the integration, the scale and
the distribution to its three largest rivals. **The exception is held by the other side of the
table.** Otter Tail sources resin from *"only four resin suppliers in the U.S."*, and on the
filer own account its largest competitors are integrated with resin producers.

### THE PHYSICAL SERIES — [E4-55], and it is the sharpest fact in this run

> **Where units exist, monitor units [E4-55]:** Precision Steel pounds fell 69M to 46M while
> price rises held dollar revenue level — *"a serious reverse, not likely to disappear in some
> 'bounce back' effect."* **Dollar revenue flattered by pricing is how a shrinking franchise
> hides; the physical series is the honest one.**

**Otter Tail discloses the unit series, in its own MD&A, every year. Here it is, assembled from
six 10-Ks:**

| year | Plastics revenue | operating income | **operating margin** | **pounds sold, % chg** | **pounds index (2020=1.00)** | price/lb, % chg |
|---|---|---|---|---|---|---|
| 2017 | $185,075 | $29,644 | **16.0%** | — | — | — |
| 2018 | $197,840 | $32,917 | **16.6%** | — | — | — |
| 2019 | $183,257 | $28,439 | **15.5%** | **−4.2%** | — | −3.3% |
| **2020** | $205,249 | $37,823 | **18.4%** | — | **1.000** | — |
| 2021 | $380,229 | $132,760 | **34.9%** | **+1.7%** | 1.017 | **+82.1%** |
| 2022 | $512,527 | $264,578 | **51.6%** | **−19%** | 0.824 | **+66%** |
| 2023 | $418,026 | $254,402 | **60.9%** | **−14%** | 0.708 | ~−5% (derived) |
| 2024 | $463,441 | $271,905 | **58.7%** | **+27%** | 0.900 | **−12%** |
| 2025 | $422,755 | $231,079 | **54.7%** | **+8%** | **0.972** | **−15%** |

*(dollars in thousands, from the Plastics segment tables of the FY2019, FY2021, FY2022, FY2023,
FY2024 and FY2025 10-Ks; the volume and price percentages are each the filer own stated figure
in the MD&A of the year in question. 2023 price change is DERIVED, not quoted, and is labelled
as such.)*

**THE CROSS-CHECK, AND IT CLOSES (operator rule 4 applied to the series that decides the
gate).** Chaining the filer own volume changes gives a 2025 pounds index of **0.972**. Revenue
rose from $205,249 to $422,755, an index of **2.059**. So the implied price index is 2.059
divided by 0.972 = **2.119**. Chaining the filer own *price* changes independently
(1.821 x 1.66 x ~0.948 x 0.88 x 0.85) gives **2.12**. **The two chains agree to within 1%,
computed from two disjoint sets of disclosed percentages.**

**What that table says, in one sentence: Otter Tail sold slightly FEWER pounds of pipe in 2025
than in 2020, and earned 6.1 times as much operating income from them, because the price per
pound is 2.1 times higher.** There is no volume story. There is no cost story — resin cost fell
14% in 2025 and 13% in 2024, and the filer says supply is *"elevated"*. **There is only price.**

**[E2-58] is the governing row and it is answered:** *"persistent over-capacity without
administered prices (or costs) equals poor profitability"*, long-term profitability set by
*"the ratio of supply-tight to supply-ample years"*, and *"nothing fails like success."* The
filer own 2021 explanation is the supply-tight year, stated as luck: the 82.1% price rise was
*"largely due to the combination of PVC resin **supply constraints** … Resin supply was
negatively impacted during the year by **production disruptions caused by extreme weather events
in the Gulf Coast region** of the U.S."* **A hurricane is not a moat.** This is **[E3-51]**
surfing run — *"the advantage lives in the wave, not the surfer"* — and on **[E4-36]** four
causes it is cause four, wave-riding, which the corpus lists precisely because it is the one
that is not ownable.

**And prosperity has already bred the glut, by Otter Tail own hand.** The 2025 volume rise of
8% is *"largely driven by additional production capacity following the completion of the first
phase of our expansion project at Vinyltech in late 2024"* — capacity added at the top of the
price cycle, which is the mechanism [E2-58] names. **[E3-62] second step** asks of any such
capex *"how much is going to stay home and how much is just going to flow through to the
customer"*; in a business whose *"principal factor of competition is price"* the answer the
corpus gives is that it flows through, and the 15% price decline in the first full year of the
new capacity is consistent with exactly that.

### THE COMPETITOR ROW — TWO ROWS, BECAUSE THERE ARE TWO BUSINESSES

> "**I can't be an intelligent owner of a business unless I know what all the other businesses
> in that industry are doing.**" — **[E3-28]**

#### ROW A — the PVC and plastic-pipe chain. Metric: **consolidated GAAP operating margin, every filed year FY2019-FY2025**, each cell computed from that filer own XBRL `OperatingIncomeLoss` divided by revenue from its own 10-K.

| company | what it makes | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | **peak to 2025** |
|---|---|---|---|---|---|---|---|---|---|
| **OTTR — Plastics segment** | PVC water/sewer pipe | **15.5** | **18.4** | **34.9** | **51.6** | **60.9** | **58.7** | **54.7** | **60.9 to 54.7 (−6.2 pts)** |
| **Westlake (WLK)** | PVC resin + PVC pipe/fittings + housing | 8.1 | 5.7 | 23.8 | 19.3 | 5.8 | 7.2 | **−14.1** | 23.8 to −14.1 (**−37.9**) |
| **Atkore (ATKR)** | PVC conduit + steel conduit (**co-defendant**) | 11.7 | 13.6 | 27.3 | 31.5 | 25.4 | 19.5 | **0.8** | 31.5 to 0.8 (**−30.7**) |
| **Olin (OLN)** | chlor-alkali, the PVC resin chain | 2.9 | −13.0 | 20.8 | 19.0 | 10.4 | 4.5 | **0.1** | 20.8 to 0.1 (**−20.7**) |
| **Advanced Drainage (WMS)** | **HDPE pipe — the named substitute** | −5.7 | 17.4 | 14.9 | 23.4 | 25.5 | 22.6 | **20.3** | 25.5 to 20.3 (−5.2) |
| **NWPX Infrastructure (NWPX)** | engineered **steel** water pipe — a named substitute | n/a\* | n/a\* | n/a\* | n/a\* | n/a\* | n/a\* | n/a\* | — |

*\*NWPX revenue is tagged under a different element across the window and its operating income
alone ($29M, $26M, $16M, $45M, $34M, $48M, $51M for 2019-2025) will not make a like-for-like
margin without re-deriving revenue from its statements. **The cell is stated as unavailable
rather than filled with a different metric.** Its direction is nonetheless recorded: steel water
pipe operating income **rose** across the window, 2019 to 2025, which is what a substitute
taking share looks like.*

*Fiscal years: WLK, OLN, NWPX and OTTR are December; ATKR is September; WMS is March. Each
company year is labelled by the calendar year its fiscal year predominantly falls in. This is
a comparability limit and it is stated, not smoothed.*

*WLK 2025 figure includes **$727 million of goodwill and long-lived asset impairment** and
$624 million of restructuring in its Performance and Essential Materials segment; its
**Housing and Infrastructure Products segment**, which contains the PVC pipe, earned $587
million on $4,148 million (**14.2%**), against $807 million on $4,317 million (**18.7%**) in
2024 and $710 million on $4,212 million (16.9%) in 2023. **That cell is the fairer pipe
comparison and it is 14.2% against Otter Tail 54.7%.** It is nonetheless not pure pipe:
"Infrastructure Products" is only $635 million of HIP $4,148 million, the rest being siding,
trim, windows, roofing and compounds. **Both limits are disclosed.***

*ATKR reports segment profit only as **Adjusted EBITDA**, which is a non-GAAP measure and a
[E4-29] flag **on Atkore, not on Otter Tail**: its Electrical segment (the PVC conduit one) went
from a **30.9%** Adjusted EBITDA margin in FY2024 to **16.5%** in FY2025, on net sales down 15.1%
*"primarily attributed to lower average selling prices of $355.1 million."* **The consolidated
GAAP cell in the row above, 0.8%, includes $214.4 million of asset impairment; without it the
margin is about 8.3%. Both are disclosed; neither is near 54.7%.**

**Peers named: five listed companies plus one whose cell could not be made comparable, against
an industry the filer says has three dominant players it does not name. Buffett says eight
[E3-28]; I took six and I say six.**

**THE PRIVATE HALF OF THE INDUSTRY IS NOT AVAILABLE AND THE LIMIT IS STATED, NOT PAPERED OVER.**
The largest PVC pipe manufacturers in North America include **JM Eagle**, **Diamond Plastics**
and **IPEX** — all privately held and none an SEC registrant; **Shintech Inc.**, the largest PVC
resin producer in the United States, is a wholly-owned subsidiary of **Shin-Etsu Chemical Co.,
Ltd.**, which files in Japan and publishes no US PVC pipe segment. **These filers publish no US
GAAP segment data at all, so no cell exists for them at any effort**, and under the four verdicts
that is **UNKNOWABLE for those cells, not UNRESEARCHED** — the same ruling the queue already
applies to non-registrants. **This does NOT hold the moat class PROVISIONAL, because criterion 2
has already failed on the filer own sentence naming four substitute materials, and a missing
private cell cannot un-fail it.**

**WHAT ROW A SAYS, AND IT IS NOT WHAT I EXPECTED.** **Every other participant in the PVC chain
has given the 2021-22 windfall back essentially in full.** Westlake is at −14.1%, Atkore at
0.8%, Olin at 0.1% — all three below where they started in 2019. **Otter Tail alone has kept
almost all of it: 60.9% at the peak, 54.7% now, against 15.5-18.4% in the four years before.**

**That is either [E2-58] rare exception, or it is the thing three federal classes and a grand
jury are asking about. I take the question seriously in both directions [E4-51], and the
evidence points one way.**

- **Against the exception:** a cost advantage that is *wide and sustainable* does not appear in
  2021 and vanish from the four years before it. In 2017-2020 Otter Tail Plastics margin was
  **15.5, 16.6, 15.5, 18.4** — inside the pack, and in 2020 only 4.8 points above Atkore 13.6%.
  There was no structural cost advantage then and the filing names no new one since. **The only
  thing that changed is the price per pound, and the pounds did not change at all.**
- **For the exception, stated as its holders would state it [E4-51]:** Otter Tail pipe is sold
  into **municipal water and wastewater**, funded by public infrastructure budgets, while
  Atkore conduit sells into non-residential electrical construction and Westlake products
  into housing — and those two end markets fell while municipal water spending did not. Freight
  economics make pipe a regional business and Otter Tail two plants sit in under-served
  geographies. **That is a real argument and it explains the 2024-25 volume recovery. It does
  not explain a price per pound still 2.1x its 2020 level while resin, the dominant input, is in
  "elevated" supply and every rival realised price has collapsed.**
- **And the filer itself takes the against side.** FY2025 10-K, Item 1: *"our earnings growth
  rate has exceeded our long-term targeted growth rate **primarily due to market conditions
  within the PVC pipe industry** … Currently, we expect these industry conditions to **gradually
  normalize through 2027**. As they do, we expect earnings and cash flow generation within our
  Plastics segment to **moderate from current levels.**"* **Management own forward statement is
  that the level is a market condition and it is going away.** Under [E3-03] that settles it:
  you cannot call a franchise something whose owner tells you it will normalise.

### THE ADMINISTERED-PRICE FINDING — [E2-59], and this is where the row limit [E3-61] bites

> **[E2-59]:** administered pricing (regulation, **cartel**) can floor a commodity business
> profits … but **the moat belongs to the REGIME**, and *"That day is gone"* is how it ends.

> **[E3-61]:** identical structures produce opposite outcomes — *"In some businesses, the
> participants behave like a demented Kellogg. In other businesses, they don't … **I think
> you'd have to know the people involved.**"* The row shows position; **it cannot show conduct.**

**The row above shows an anomaly it cannot explain, and the filings name the mechanism that is
being litigated as the explanation.** From the Q2 2026 10-Q, Note 10, filed 2026-08-05, which
makes this current and not historical:

- **Since August 2024**, Northern Pipe Products, Vinyltech Corporation and Otter Tail Corporation
  have been defendants, with **"more than twenty other PVC pipe manufacturers"** and **Oil Price
  Information Systems, LLC (OPIS)**, in **In re: PVC Pipe Antitrust Litigation**, No.
  1:24-cv-07639, N.D. Ill., in three putative classes — direct purchasers, non-converter seller
  purchasers, and end users — alleging the defendants *"**conspired to fix, raise, maintain and
  stabilize the price** of PVC municipal pipe, PVC plumbing pipe, PVC electrical pipe and PVC
  pipe fittings"* by *"**improperly exchang[ing] confidential information through OPIS**"*.
  Plaintiffs sought **treble damages**.
- **In the quarter to 2026-06-30 Otter Tail settled all three classes**: $39.5M to the direct
  purchasers, **$34.0M** to the non-converter sellers, **$30.0M** to the end users — **$103.5
  million**, recognised as `Legal Settlement Expenses` on the face of the income statement and
  charged **to the Plastics segment**. $73.5M was paid into escrow in June 2026 and $30.0M in
  July 2026, from cash on hand. **The company records the standard non-admission** — *"does not
  constitute an admission by the Company of any wrongdoing, fault, or liability"* — and says it
  *"believes it has factual and legal defenses and was prepared to continue litigating."*
- **A DOJ Antitrust Division grand jury subpoena, received August 2024, is live.** On
  **2026-07-01 the DOJ moved to extend its discovery stay to 2026-12-31.** A criminal
  investigation that is still asking for time is not a closed matter.
- **A Canadian nation-wide class action** (S-257310, Supreme Court of British Columbia, filed
  2025-09-26) alleging the same information-exchange conspiracy under the Competition Act is
  **not settled** and is being defended.
- **A shareholder derivative demand** (letter of 2025-05-20) asks the Board to sue its own
  current and former officers and directors over the same conduct. *"At this time, we are unable
  to determine the likelihood of any outcome related to this matter."*

**THE CO-DEFENDANT FILING DATES THE ALLEGED PERIOD, AND IT IS THE EXACT PERIOD OF THE MARGIN
EXPANSION.** Atkore FY2025 10-K (accession 0001628280-25-054049) describes the same case with
a precision Otter Tail own filing does not use: the suits *"generally allege anticompetitive
conduct related to the price of PVC pipes sold in the United States **between approximately 2021
and the present**"*, through *"their contribution of information to, and readership of, a weekly
report called **'PVC & Pipe Weekly'** published by defendant Oil Price Information Service,
LLC."* And: **"A settlement between OPIS and plaintiffs was preliminarily approved in July 2025,
obligating OPIS to pay certain monies and to COOPERATE WITH PLAINTIFFS."** Atkore itself has
**not** settled and *"plans to vigorously defend itself."*

**Set that date against the table above. The alleged conduct period begins in 2021. The Plastics
operating margin was 18.4% in 2020 and 34.9% in 2021.**

**I am not making a finding of wrongdoing, and the framework forbids me to. [E5-38]** is explicit
that a fired flag is not a venality finding, and **[E5-22]** that penalty size is not seriousness
in either direction. **What I am making is a Q2 finding about the SOURCE OF THE MARGIN, which is
a different question and is the one Q2 asks.** Either:

1. the price level 2021-2025 was a market outcome — in which case the row shows every comparable
   participant has already lost it and Otter Tail management says its own will normalise
   through 2027; **no franchise**; or
2. the price level was to some degree administered through the information exchange — in which
   case **[E2-59]** governs directly: *the moat belongs to the regime*, the regime is a weekly
   trade report whose publisher has settled and agreed to cooperate with the plaintiffs, and the
   DOJ is still convening a grand jury. **"That day is gone" is how it ends, and it is ending in
   a federal courtroom in the Northern District of Illinois.**

**There is no third branch in which this is a durable competitive advantage owned by the
company.** Both branches are Q2 fails, which is why this gate closes on the business regardless
of how the litigation is finally decided — and that is the honest form of the finding, because
the litigation outcome is genuinely unknown.

#### ROW B — the electric half. Metric: **most recently granted allowed return on equity**, each cell from that utility own 10-K.

| company | jurisdiction / service | allowed ROE | source |
|---|---|---|---|
| Avista (AVA) | **Alaska (AEL&P)** | **11.45%** | AVA FY2025 10-K, accession 0001193125-26-067872 |
| **Black Hills (BKH)** | Nebraska Gas, settled | **9.85%** *(requesting 10.5% in a pending review)* | BKH FY2025 10-K, 0001193125-26-046028 |
| **OTTR** | **North Dakota, 03/15/25** | **10.10%** *(with 70% of anything above 10.20% returned to customers)* | FY2025 10-K, 0001466593-26-000008 |
| NorthWestern (NWE) | Montana Colstrip Unit 4, 02/2026 | 10.00% | NWE FY2025 10-K, 0001993004-26-000006 |
| ALLETE (ALE) | Superior Water Light & Power (WI), 2024 case | 9.80% | ALE FY2024 10-K, 0000066756-25-000013 |
| Avista (AVA) | Washington | 9.80% | AVA FY2025 10-K |
| **ALLETE (ALE)** | **Minnesota Power — the SAME STATE** | **9.65%** | ALE FY2024 10-K |
| NorthWestern (NWE) | Montana electric delivery, 02/2026 | 9.65% | NWE FY2025 10-K |
| NorthWestern (NWE) | Montana natural gas, 02/2026 | 9.60% | NWE FY2025 10-K |
| IDACORP (IDA) | Idaho revenue-sharing threshold | 9.60% *(9.12% floor for ADITC amortisation)* | IDA FY2025 10-K, 0001057877-26-000028 |
| Avista (AVA) | Idaho / Oregon settlements | 9.4-9.6% | AVA FY2025 10-K |
| **OTTR** | **Minnesota, 07/01/22** | **9.48%** | FY2025 10-K |
| NorthWestern (NWE) | Great Falls Gas, 10/2018 | 9.20% | NWE FY2025 10-K |
| **OTTR** | **South Dakota, 08/01/19** | **8.75%** *(50% of anything above returned, 100% above 9.50%)* | FY2025 10-K |

**Peers named: five listed small and mid-cap regulated utilities, fourteen jurisdictional cells.
The industry has roughly fifty investor-owned electric utility holding companies; I took five
comparable by size and geography and I say five.**

**WHAT ROW B SAYS: there is nothing to own here.** Otter Tail three allowed ROEs bracket the
peer distribution — its North Dakota 10.10% is near the top, its Minnesota 9.48% is **below
ALLETE Minnesota Power at 9.65% in the same state and before the same commission**, and its
South Dakota 8.75% is **the single lowest cell in the table and has not been reset since
August 2019.** The spread across the whole group is about 270 basis points and it is set by
commissioners, not by competitive position. **There is no relative advantage to measure because
the variable that determines the return is not a competitive variable.**

**And one cell of Row B is a fact about the asset class rather than a company: ALLETE, the
Minnesota peer, was taken private and its last 10-K is FY2024.** The row is thinner than it was
because the market for these assets clears at prices private capital will pay for a regulated
return stream. That is a valuation observation, recorded here and carried to Q5 rather than used
at Q2.

**ONE CANDOR DIFFERENCE FOUND WHILE BUILDING ROW B, AND IT IS OWED TO Q3.** NorthWestern
publishes, for every jurisdiction, the **Authorized Rate Base in dollars** and the **Year-end
Estimated Rate Base in dollars** beside the allowed ROE ($3,176.2M authorized against $3,425.6M
estimated for Montana electric alone). **Otter Tail publishes the allowed *percentage* return on
rate base and the revenue requirement, and not the rate base.** A shareholder cannot compute
OTP earned return on rate base from the 10-K. See Q3, [E2-26].

### The remaining Q2 tests, answered

- **[E2-53] the dominance class** — *"Once dominant, the newspaper itself, not the marketplace,
  determines just how good or how bad the paper will be."* **Electric: the position is dominant
  and the commission, not the marketplace AND not the company, determines the economics — which
  is the dominance class with the profit removed. Plastics: not dominant; the filer names three
  larger competitors.**
- **[E3-46] the second question is a number** — return on capital employed. **Plastics: 123.9%
  pre-tax on identifiable segment assets, extraordinary and shown above to be price. Electric:
  4.3%. Manufacturing: 6.9%.** Two of the three are poor and the third is the one under
  litigation.
- **[E2-45] the attacker test** — *"how I would like, assuming I had ample capital and skilled
  personnel, to compete with it."* **Electric: I could not, and would not want to — I would be
  buying a 9.5% allowed return on capital I had to raise.** **Plastics: I would build extrusion
  lines next to the two plants, which is exactly what the filer did to itself at Vinyltech in
  2024, and which is why volume rose 8% and price fell 15% in the same year.** The attacker test
  is failed by the subject own capital plan.
- **[E4-32] direction over existence, and [E4-55] unit rule as the instrument.** **Plastics:
  pounds sold in 2025 are 2.8% BELOW 2020 and price per pound is falling 12-15% a year for three
  consecutive years. The direction is down on both the physical series and the price.**
  **Electric: rate base is growing, which for a regulated utility is the only growth there is;
  direction up on size, flat on return.**
- **[E4-37] the agony metric** — *"you can almost measure the strength of a business over time by
  the agony they go through in determining whether a price increase can be sustained."* **In 2021
  Otter Tail raised the price per pound 82.1% and volume ROSE 1.7%. That is the yawn end of the
  scale, and it is the single strongest fact I have found in the company favour.** It is also
  the fact the litigation is about, and by 2024-25 the same business is taking **−12% and −15%**
  on price without being able to stop it. **The metric has already detected the downgrade in real
  time, which is precisely its stated use.**
- **[E4-23] key-person dependence:** no evidence found; this is not a superstar-dependent
  business in either half. **Recorded as absent, not as a strength.**

### VERDICT

- Needed or desired **[x]** (both halves) · no close substitute **[ ] FAILS** (Plastics, on the
  filer own sentence) · not price-regulated **[ ] FAILS** (Electric, definitionally)
- Class: **[ ] WIDE  [ ] NARROW  [x] NONE**  ·  **Direction: DOWN on both halves** — Plastics on
  price and pounds, Electric on nothing that is ownable
- **VERDICT: [x] OUT**

**OUT on the business, on three independent grounds, any one of which closes the gate:**

1. **The Electric half fails [E3-03] criterion 3 by definition** — extensive price regulation is
   the business model, with earnings-sharing clawbacks written into two of three tariffs — and
   fails **[E2-44]** on both characteristics, the second by 19.7 years of segment earnings.
2. **The Plastics half fails [E3-03] criterion 2 on the filer own sentence**, which names
   ductile iron, HDPE, steel and concrete as competing for the same end markets and says *"the
   principal factors of competition are price."*
3. **The Plastics margin is price and not position, proven from the filer own unit series**:
   pounds sold in 2025 are **2.8% below 2020** while operating income is **6.1x**, the 2021
   trigger was a **Gulf Coast hurricane** on the filer own account [E3-51], every comparable
   listed participant has surrendered the windfall (Westlake −14.1%, Atkore 0.8%, Olin 0.1%),
   management itself expects *"these industry conditions to gradually normalize through 2027"*,
   and the alternative explanation for why Otter Tail has not yet normalised is the subject of
   **$103.5 million of settlements paid, a live DOJ grand jury subpoena, an unsettled Canadian
   class action and a shareholder derivative demand** — which is **[E2-59]** administered-price
   case, where *"the moat belongs to the regime."*

**Q3, Q4 and Q5 below are RECORDED, NOT GOVERNING.** The file is closed at Q2. They are written
because the queue requires a price either way and because the findings are owed to the register.

---

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*
**RECORDED, NOT GOVERNING. The file closed at Q2 OUT on the business.** Q3 cannot reopen it —
**[E2-37, E2-38, E3-39]**: *"a textile company that allocates capital brilliantly within its
industry is a remarkable textile company — but not a remarkable business."* **Everything below,
including several findings that are to this management credit, promotes nothing.**

### STEP 1 — THE WEIGHT CASE, DECLARED FIRST

| determinant | verdict | why |
|---|---|---|
| **Daily execution [E3-38, E3-43, E2-70]** | **TICKED** | Q2 found no franchise in either half. **[E3-43]** is explicit that the distinction is franchise versus business: *"franchises can tolerate mis-management… **a business, unlike a franchise, can be killed by poor management**."* With Q2 OUT, both halves are *a business*, and the commodity half prices an undifferentiated product against substitutes every week. |
| **Control [E1-16]** | not ticked | a minority position in a listed company; exit is a market order. |
| **Leverage [E3-29]** | **not ticked, and this is a real finding** | year-end **equity ratio to total capital 62.8%** on the filer own statement; $1,107M of debt obligations against $1,876.9M of book equity at 2026-06-30, **0.59x**. For a rate-regulated utility that is conservative — the commissions themselves authorise only 52.5-53.5% equity layers, so **Otter Tail carries MORE equity than its own tariffs assume.** |

**CASE DECLARED: Q3 IS A BINARY GATE, on the daily-execution limb, and it is a gate because Q2
said there is no franchise to absorb error.** No price compensates **[E1-16, E3-29, E5-35]**.

### HONESTY — the binary, and this is where the run must be most careful

> "Disappointments are inevitable. **We are understanding about business mistakes; our tolerance
> for personal misconduct is zero.**" — **[E5-16]**

**The facts, each dated to when it became PUBLIC:**
- **August 2024** — the consolidated PVC pipe antitrust class actions are filed; the DOJ
  Antitrust Division grand jury subpoena is received.
- **2025-05-20** — a shareholder derivative demand letter reaches the Board alleging *"securities
  law violations, breaches of fiduciary duties, and unjust enrichment by certain current and
  former officers and directors."*
- **August 2025** — amended complaints add allegations.
- **2025-09-26** — the British Columbia class action is filed.
- **Q2 2026** — **$103.5 million** paid to settle all three US classes, **with an express
  non-admission**, and the company states it *"believes it has factual and legal defenses and was
  prepared to continue litigating."*
- **2026-07-01** — the DOJ moves to extend its discovery stay to **2026-12-31**. The criminal
  matter is open.

**I make no integrity finding, in either direction, and the framework requires that restraint
twice over.** **[E5-38]**: people Buffett would trust with his wallet *"would play games with any
number that came to them"* — the flag reads the accounting, **[E5-16]** judges the person on
conduct, and the two tests stay distinct. **[E5-22]**: penalty size is not seriousness **in
either direction** — $103.5 million is not proof, and a non-admission is not exoneration. **And
[E5-17] caps the whole exercise:** *"People are not that easy to read. Sincerity and empathy can
easily be faked"*, with Buffett own concession on a reserve fraud: *"Charlie and I would not have
spotted it."*

**So the honesty binary is split into two sub-questions, and the four verdicts answer them
differently:**
1. **What exactly is alleged, in the plaintiffs own words?** → **UNRESEARCHED.** The artifact is
   nameable: **the three amended class complaints in In re: PVC Pipe Antitrust Litigation, No.
   1:24-cv-07639 (N.D. Ill.), filed August 2025.** Where it lives: the court docket, i.e. **PACER
   / CourtListener.** **Ladder rung that fails: there is no rung.** The evidence ladder in
   `THE FRAMEWORK v4.md` runs SEC XBRL → EDGAR primary → IR site → exchange filings → EDINET →
   competitor filings, and **court dockets are not on it.** I read the two best available
   substitutes instead — Otter Tail own Note 10 and **the co-defendant Atkore fuller description
   of the same case**, which is a competitor filing and therefore on the ladder.
2. **Did the conduct occur?** → **UNKNOWABLE today.** The determining events have not happened:
   the DOJ has not charged or declined, the Canadian case is undecided, the Board has not
   answered the derivative demand, and the US settlements resolve the claims without deciding
   them. No document that exists resolves it, which is the test **[E4-19]** sets.

**THE VERDICT LANGUAGE MATTERS AND I WRITE IT THE WAY THE FRAMEWORK SAYS:** *"A Q3 pass is the
absence of found disqualifiers, not a finding that the managers are honest"* **[E5-17]**. **On
the filings as they stand I found no disqualifier — and I also cannot close the binary, because
a live federal grand jury matter on the exact source of 61% of this company segment earnings is
not an absence.**

### STEP 2 — THE FLAGS. Each is a prompt to READ, and I read each one.

| flag | verdict | what the filing actually says |
|---|---|---|
| weak accounting **[E4-22]** | **read, does not fire** | see the 10-K/A below |
| unintelligible footnotes | **does not fire** | the footnotes are plain, and the segment note gives revenue, every significant expense, net income, capex, D&A and identifiable assets **per segment, per year.** This is better than most of the queue. |
| **trumpeted projections [E4-22, E5-30]** | **FIRES** | see below |
| **serial share issuance [E5-15]** | **does not fire, emphatically** | **zero** equity raised 2021-2025 (`ProceedsFromIssuanceOfCommonStock` is $696k in 2021 and **nil** in 2022 and 2023); the count went 41,469,879 → 41,985,580 over five and a half years, **+1.24%**, entirely employee plans. |
| **EBITDA promotion [E4-29]** | **CLEAN, and the check was run the hard way** | see below |
| filed-figure tells **[E4-30]** | **read, does not fire** | see below |
| **metric-switching [E2-49]** | **FIRES, and it is the sharpest finding in Q3** | see below |
| **except-for [E2-57]** | **FIRES, same event** | see below |
| restructuring charge **[E3-53, E5-33]** | **does not fire on form; the charge IS in the income statement** | the $103.5M sits on the face of the Consolidated Statements of Operations as its own line, `Legal Settlement Expenses`, and is charged to the Plastics segment. Nothing is dumped into a quarter to clear the ground. **It is a real cost of the Plastics business and it stays in the owner-earnings mean [E5-33].** |
| dividends funded by issuance **[E2-52]** | **does not fire** | cumulative dividends 2021-2025 **$373.0M** against cumulative operating cash of **$1,863.8M** and **zero net share issuance.** No Peter, no Paul. |
| stock-price targeting **[E3-50]** | no evidence found | — |
| delegated allocation **[E3-58]** | no evidence found | no banker-led M&A; no acquisitions at all in the window. |

**THE 10-K/A, WHICH I WOULD HAVE MISSED HAD I NOT LISTED THE AMENDED FILINGS.** A **Form 10-K/A,
Amendment No. 1, accession 0001466593-26-000015, filed 2026-02-23** — five days after the
original — states its purpose in plain English: *"filing this Amendment for the **sole purpose of
correcting the date of the Report of Independent Registered Public Accounting Firm** … **from
February 19, 2025 to February 18, 2026**."* **The FY2025 annual report as originally filed
carried the PRIOR YEAR date on Deloitte & Touche LLP audit report.** New officer certifications
were filed with the amendment.
**How I score it, and I score it against [E2-69], which tells me to judge deviations by
DIRECTION.** This is a stale template date on the auditor report, found and corrected by the
filer within five days, with the reason stated exactly and nothing else touched. Berkshire own
precedent in that row is a *deviation toward candor*; the flag is for *"the corpse filing its own
death certificate generously."* **It is the smallest possible control lapse and the correction is
the candid form. The cockroach flag does not fire — and I record that I went looking, because
[E4-22] says there is seldom just one, and I found no second one.** The ICFR attestation in the
amended Item 8 is unqualified and no material weakness is reported.

**[E4-29] EBITDA — CLEAN, AND THE CGNX COMPANION RULE IS WHAT MADE THE ANSWER TRUSTWORTHY.** The
queue standing instruction is to pull the latest **8-K EX-99.1 earnings release** before scoring
this flag, because *"a run that reads only the annual report will score clean a company that has
built its public narrative on a non-GAAP metric."* I pulled **three** of them. **The word EBITDA
appears ZERO times in the Q4/FY2025 release, ZERO times in the Q1 2026 release, ZERO times in the
Q2 2026 release, and ZERO times in the 2026 proxy statement.** It appears **three times in the
whole FY2025 10-K**, and I read all three: every one is inside the **goodwill impairment
valuation methodology** (*"multiples derived from comparable enterprise values to earnings before
interest, taxes, depreciation and amortization (EBITDA) of select peer companies"*, *"an
appropriate EBITDA multiple"*, and the sensitivity *"a 1.0x decrease in the assumed EBITDA
multiple would not lead to a goodwill impairment charge"*). **That is the one legitimate use of
the measure — valuing a reporting unit against peers — and it is not promotion.** This is the
exact inverse of Cognex: clean 10-K **and** clean releases. **Recorded as a positive.**

**[E4-30] THE FILED-FIGURE TELLS — read, explained, and they do not fire.**
- **Unnaturally smooth reported growth: absent.** Net income ran $95.9M → $176.8M → $284.2M →
  $294.2M → $301.7M → **$275.9M**, and the June 2026 quarter was a **$7.6 million net loss**.
  Nobody engineering smoothness produces that series.
- **Cash taxes as a share of reported pretax income:** 4.6% (2019), 4.5% (2020), 4.0% (2021),
  12.1% (2022), 12.7% (2023), **15.7% (2024)**, **3.4% (2025)**. **The direction that fires this
  flag is FALLING cash tax as earnings rise, and Otter Tail did the opposite through the
  windfall** — cash taxes rose almost fourfold as a share while earnings rose. **The 2025 drop to
  3.4% is real and I chased it.** It is explained on the face of the rate reconciliation:
  **`Energy Related Tax Credits` of −$29,773 thousand, −9.2 percentage points**, up from −5.5
  points in 2024 and −4.8 in 2023, plus a **$33,187 thousand deferred tax charge** in the
  operating section of the cash-flow statement, so current tax of ~$13.2M against cash paid of
  $11.1M. The credits are wind production and investment tax credits at the utility and the filer
  says they flow into customer rates. **Disclosed, arithmetically consistent, does not fire.**

**[E4-22] THE THIRD FLAG — TRUMPETED PROJECTIONS — FIRES, AND THEN THE OUTTURN RECORD [E3-48] IS
THE BEST THING IN THIS RUN.** The company publishes an annual diluted EPS guidance range every
February, updates it quarterly, and states a standing long-term target: *"Our long-term financial
objectives include achieving a compounded annual growth rate in **earnings per share in the range
of 7 to 9%**"*, with *"an annual increase in our dividend to be in the range of **6 to 8%**."*
**[E5-30]** is the reason this is a flag at all and not a triviality: *"once you start it, it is
all over. You can't quit … And forecasting earnings, I can't imagine anything more
destructive."* **A guidance culture is a ratchet, and this one is running.**

**[E3-48] says the action on the flag is to pull the company own past guidance and set it
against outturn. I did, from five separate 8-K EX-99.1 releases:**

| year | initial guidance, stated in February of that year | actual diluted EPS | **outturn vs midpoint** |
|---|---|---|---|
| 2022 | **$3.78 - $4.08** | **$6.78** | **+72.5%** |
| 2023 | **$3.76 - $4.06** | **$7.00** | **+79.0%** |
| 2024 | **$5.13 - $5.43** | **$7.00** *(as reported for 2023; 2024 actual $7.17)* | **+35.8%** |
| 2025 | **$5.68 - $6.08** | **$7.17** *(2024 actual)* / **$6.55** *(2025 actual)* | **+11.4%** on 2025 |
| 2026 | **$5.22 - $5.62**, cut in August to **$3.84 - $4.24** | pending | — |

*(Sources: 8-K EX-99.1 releases of 2022-02-15 (acc. 0001466593-22-000006), 2023-02-14
(0001466593-23-000050), 2024-02-13 (0001466593-24-000034), 2025-02-18 (0001466593-25-000027) and
2026-02-17 (0001466593-26-000002). Actual diluted EPS from the Consolidated Statements of Income
of the corresponding 10-K. **The 2024 and 2025 rows are labelled with both the guidance year and
the actual it should be compared with, because the guidance is initiated in February FOR that
year; the comparison that matters is guidance-for-year-N against actual-for-year-N: 2022 $3.93
midpoint vs $6.78; 2023 $3.91 vs $7.00; 2024 $5.28 vs $7.17; 2025 $5.88 vs $6.55.**)*

**Four consecutive years of guiding LOW and beating by 72.5%, 79.0%, 35.8% and 11.4%.** In
February 2022, having just reported $4.23 for 2021, they guided 2022 to **$3.78-$4.08 — below the
year just finished** — and delivered $6.78. **[E3-48]** asks for *"the record of the people who
made the projections"*, and this record is the opposite of the flag danger: this is not a
management that *"always promise[s] to make the numbers"* and would therefore be *"tempted to
make up the numbers."* **They under-promised for four years running and the beats are shrinking
in exactly the pattern a reverting commodity price predicts (+72.5, +79.0, +35.8, +11.4).**
**Recorded as a positive, and as a second independent confirmation of the Q2 finding: management
has never been able to forecast the plastics price, which is what a price you do not control
looks like from the inside.**

**[E2-49] METRIC-SWITCHING — FIRES, AND THE TIMING IS EXACT.**

> *"Yardsticks seldom are discarded while yielding favorable readings. But when results
> deteriorate, most managers favor **disposition of the yardstick rather than disposition of the
> manager**"* — demand *"pre-set, long-lived and small bullseyes"* — **[E2-49]**

**The operational form of this test is to compare the headline metric across successive filings.
I did, on three consecutive 8-K EX-99.1 releases, and the count is unambiguous:**

| earnings release | accession | occurrences of the word "adjusted" |
|---|---|---|
| Q4/FY2025, February 2026 | 0001466593-26-000002 | **0** |
| Q1 2026, May 2026 | 0001466593-26-000049 | **0** |
| **Q2 2026, August 2026 — the quarter of the $103.5M charge and the $7.6M net loss** | 0001466593-26-000068 | **18** |

**In the quarter results deteriorated, three new non-GAAP yardsticks were introduced at once** —
**Adjusted Net Income, Adjusted Earnings per Share and Adjusted Return on Equity** — and a
**second, parallel guidance range was initiated**: *"We are updating our 2026 diluted earnings per
share guidance range to **$3.84 to $4.24** from $5.22 to $5.62 primarily due to the impact of the
settlement agreements … We are **initiating an adjusted diluted earnings per share guidance range
of $5.68 to $6.08** which excludes the after-tax impact of the litigation settlement expense
**and reflects an increase from our original guidance range.**"*

**Read that last clause carefully. The new yardstick is set $0.46 ABOVE the guidance the company
gave before the settlement was known.** A shareholder reading only the adjusted number is told
2026 is a **better** year than originally promised, in the year the company paid $103.5 million
and lost money in a quarter.

**The arithmetic reconciles, and I give that credit:** $5.22 + $0.46 of genuine operating
improvement − **$1.84** of settlement per share = **$3.84**, and the release states the $1.84
reconciling item and the 380 basis points of ROE explicitly. That is the disclosed form, and
**[E2-49]** own carve-out is that a switch *"announced ahead with reasons"* is the candor case.
**This one was not announced ahead. It arrived with the loss.**

**And [E2-57] fires on the same event — the ninth-inning rule:** *"'except for' should be excised
from the lexicon. If you are going to play the game, **you must count the runs scored against you
in all nine innings.** … the real mistake is not the act, but the actor."* **The $103.5 million is
the cost of the way the Plastics segment earned its money.** It is not a flood, a fire or a
one-off tax item; it is the settlement of claims about the pricing that produced the earnings the
adjusted measure is reporting. **Excluding it while keeping the revenue it relates to is the
single most questionable presentation choice in this file.**

**AND THE ADJUSTED ROE ADJUSTS THE DENOMINATOR TOO.** The definition, verbatim: *"Adjusted Return
on Equity as annual Adjusted Net Income divided by the average of total consolidated
shareholders equity **excluding the impact of legal settlement expenses** and the related income
tax benefit"* — so the equity the settlement consumed is **added back to the denominator** as well
as to the numerator, which raises the ratio twice. The release states the effect: it *"increases
anticipated return on equity by **380 basis points**."* **[E2-01]** defines the primary test as
*"a high earnings rate on equity capital employed (**without undue leverage, accounting
gimmickry, etc.**)"*, and adjusting both halves of a return ratio for the same charge is the
kind of thing that clause is pointed at. **Recorded as a live Q6-style watch item: the
compensation plans are also ROE-based (below), and the 2026 proxy will show whether the adjusted
figure reaches the pay calculation.**

**[E4-52] DO THE FLAGS CONVERGE? PARTLY, AND THE HONEST ANSWER IS NARROWER THAN THE LOLLAPALOOZA.**
Three flags fire — the standing EPS growth target, the metric switch, and the except-for
adjustment — and **all three point the same way: toward presenting a smoother and higher earnings
picture at the exact moment the plastics windfall reverses.** That is a real confluence and
**[E4-52]** says to treat it as one reinforcing system rather than three prompts.
**But [E4-52] lollapalooza is a confluence acting *in favor of a particular outcome*, and I
cannot find the outcome.** The classic completion of this pattern — raise equity on the flattered
number, or buy something with it — **did not happen and could not have**: **zero shares issued,
zero acquisitions, zero buybacks, and the cash dividend covered 4.8 times by operating cash.**
**So I record a PRESENTATION convergence and explicitly refuse to call it an allocation or
financing convergence, because the filings show neither.** That distinction is the whole read.

### STEP 3 — THE PRIMARY TEST [E2-01]. Earnings rate on equity capital employed, multi-year.

> "**The primary test of managerial economic performance is the achievement of a high earnings
> rate on equity capital employed** (without undue leverage, accounting gimmickry, etc.) **and
> not the achievement of consistent gains in earnings per share.**" — **[E2-01]**

| year | net income | average shareholders equity | **ROE on average equity** | ROE on year-end equity |
|---|---|---|---|---|
| 2019 | $86,847 | $755,173 | **11.5%** | 11.1% |
| 2020 | $95,851 | $826,224 | **11.6%** | 11.0% |
| 2021 | $176,769 | $930,872 | **19.0%** | 17.8% |
| 2022 | $284,184 | $1,104,047 | **25.7%** | 23.3% |
| 2023 | $294,191 | $1,330,162 | **22.1%** | 20.4% |
| 2024 | $301,662 | $1,555,753 | **19.4%** | 18.1% |
| 2025 | $275,893 | $1,765,130 | **15.6%** | 14.8% |

*(net income and equity from the filed balance sheets and income statements, FY2019-FY2025
10-Ks, cross-checked against the XBRL `NetIncomeLoss` and `StockholdersEquity` series.)*

**[E2-43] denominator scoping, run rather than skipped:** the row says that for acquisitive or
leveraged filers the denominator should be **unleveraged net tangible assets** with the goodwill
wedge reported separately. **Here the adjustment is immaterial and that is itself the finding:
goodwill has been a flat $37,572 thousand for six consecutive years** (2020 through 2025, no
additions, no impairments) **and finite-lived intangibles have amortised from $10,144 to $4,642
thousand.** Together **$42.2 million against $1,861.8 million of book equity — 2.3%.** There is
no goodwill wedge to hide anything in, because **there have been no acquisitions.** Book equity is
very nearly tangible equity, so the series above needs no restatement.

**WHAT THE SERIES SAYS. The pre-boom ROE is 11.5%, the boom peak is 25.7%, and it has decayed
25.7 → 22.1 → 19.4 → 15.6 in three straight years.** The trajectory is unmistakably toward the
11-12% a regulated utility with a small manufacturing tail earns, and management says so in
writing. **[E4-41]** requires exactly this: *normalize the mean DOWN for luck* — *"favourable
exogenous breaks in the window are named and removed before the mean is trusted."* **The
favourable break is named (a Gulf Coast hurricane and a resin shortage), it is quantified (the
price per pound is 2.12x its 2020 level on 0.972x the pounds), and the Q4 arithmetic below removes
it and shows the answer both ways.**

**[E3-59] the two yardsticks:** *"one is how well they run the business"* judged against *"the
hand they were dealt"*, and *"how well that they treat their owners."* **Against the hand dealt,
this management ran the utility competently** (Electric segment net income $66.8M → $97.6M over
five years, retail rates 19% below the regional average, 87th consecutive year of dividends) **and
did not do anything foolish with an enormous windfall.** On treating owners: see the allocation
section, which is the strongest part of the file, and the presentation section above, which is the
weakest.

### CAPITAL ALLOCATION — where the plastics windfall actually went, in dollars

**Cumulative 2021-2025, from the filed cash-flow statements:**

| use | amount | share of operating cash |
|---|---|---|
| **Capital expenditure** | **$1,276,815** | 68.5% |
| — of which Electric segment | ~$1,030,000 | 55% |
| — of which Manufacturing and Plastics | ~$155,000 | 8% |
| **Dividends paid** | **$373,010** | 20.0% |
| **Acquisitions** | **$0** | **0%** |
| **Share repurchases** | **$0** | **0%** |
| **New equity issued** | **$696 thousand, all 2021, nil thereafter** | ~0% |
| Cash balance built | **$1,537 → $386,193 (+$384,656)** | — |
| New long-term debt issued | $220,000 (2024 $120M, 2025 $100M) | — |
| **Total operating cash generated** | **$1,863,767** | 100% |

*(dollars in thousands. Operating cash, capex, dividends, debt issuance and the cash balance are
each the filed line; the Electric/non-Electric capex split is summed from the segment capital
expenditure tables of the FY2022, FY2024 and FY2025 10-Ks.)*

**[E2-30] THE INSTITUTIONAL IMPERATIVE — SCORED, AND THE SECOND BEHAVIOUR DID NOT FIRE, WHICH IS
THE STRONGEST SINGLE FINDING IN THIS Q3.**
- **(1) resists any change in current direction** — **no.** The generation fleet is being replaced
  under regulatory order, coal is being retired ahead of book life, and the plan says so in
  dollars.
- **(2) *"corporate projects or acquisitions will materialize to soak up available funds"* —
  **DID NOT HAPPEN.** A company whose earnings tripled on a commodity price spike, holding
  $386 million of cash, **bought nothing.** Goodwill is unchanged for six years. **This is the
  behaviour [E2-30] predicts and the corpus treats as near-inevitable, and this management did not
  do it.** What they did instead was spend on their own rate base at a regulated return and hand
  20% of the cash to shareholders. **Recorded, unambiguously, in their favour.**
- **(3) staff studies to justify a craving** — no evidence found; no acquisition to justify.
- **(4) *"the behavior of peer companies will be mindlessly imitated"*** — **structurally
  unavoidable on the utility half**, where the allowed ROE is literally set by reference to peers
  (the proxy says the LTI target is calibrated against *"Otter Tail Power Company authorized
  return on equity and **EEI Index and regional peer utility return on equity history and
  trend**"*). That is imitation written into the pay plan by the regulator design, not by
  management choice. **Noted, not scored against them.**

**[E2-56] THE PRO-AM EFFECT, AND HERE IS THE REAL ALLOCATION QUESTION.** *"Their marvelous core
businesses … **camouflage repeated failures in capital allocation elsewhere**"* — judge retention
**segment-by-segment, incrementally, never on the blended return.** Done:

| segment | 2025 pre-tax income | identifiable assets | **pre-tax return on segment assets** | 2025 capex |
|---|---|---|---|---|
| **Plastics** | $230,399 | $185,936 | **123.9%** | **$7,938** |
| Manufacturing | $16,900 | $243,737 | **6.9%** | $8,903 |
| **Electric** | $129,420 | $3,006,695 | **4.3%** | **$270,593** |

**The cash from the 123.9% business is being invested, almost in its entirety, in the 4.3%
business.** Incrementally, what the utility retention buys is the **allowed ROE**: 9.48% in
Minnesota, 10.10% in North Dakota, 8.75% in South Dakota — **and two of those are subject to
earnings-sharing clawbacks above the allowed level.**

**The corpus has a number for exactly this judgment and Otter Tail sits below it. [E5-40]:**
**~12% on retained utility capital is *"quite satisfactory"*** — a return-on-retention judgment
about an owned business, explicitly distinct from the [E4-28] entry floor. **Otter Tail three
allowed ROEs are 8.75%, 9.48% and 10.10%, every one of them below 12%, and its whole five-year
$1,921 million Electric capital plan earns at those rates.** **That is a capital-allocation
finding, stated with [E4-13] humility clause:** *"it is natural for CEOs to be optimistic about
their own businesses. **They also know a whole lot more about them than I do**"* — and it is not
a charge of folly, because **there is nowhere better inside this company to put the money.** The
Plastics segment cannot absorb it (it takes $8 million a year of capex and adding capacity is
what compressed its own price), and buying something outside the circle is the behaviour
[E2-30](2) warns against. **The finding is about the STRUCTURE, not the people: this company
generates cash in a business that cannot use it and must deploy it in a business that earns
9-10% by law.** It binds position size and nothing else.

**[E3-54] THE RETENTION TEST — RUN, AND IT PASSES.** At least $1 of market value per $1 retained,
five-year rolling.
- Retained 2021-2025 = cumulative net income **$1,332,699** less dividends **$373,010** =
  **$959,689 thousand.**
- Market value at **2020-12-31**: **41,469,879 shares** (filed, FY2020 10-K balance sheet)
  × **$42.61** close — the split-invariant construction, and there have been **no splits in ten
  years** on the dividend-and-split event series — = **$1,766.8 million.** *(The 2020 close is a
  dated aggregator quote and is flagged as such.)*
- Market value at **2026-09-18**: **$3,670.4 million.**
- Gain **$1,903.6 million** on **$959.7 million** retained = **$1.98 of market value per $1
  retained. PASSES, roughly double the bar.**

**And the corpus own 2009 self-correction of this test is a market-versus-index comparison, which
the filer publishes itself.** FY2025 10-K performance graph, $100 invested 2020-12-31 with
dividends reinvested: **OTTR $219.89, EEI Index $143.83, Nasdaq $186.96.** Otter Tail beat both.
**Recorded in their favour — and immediately qualified, because Q2 showed where the return came
from: a hurricane, a resin shortage, and a price the company does not set.** Neither the retention
test nor the TSR table distinguishes skill from the wave, which is why [E3-54] is scored at Q3 and
the wave is judged at Q2.

**BUYBACKS — the two conditions [E5-08], plus the third [E4-31], plus the refusal tell [E2-51].**
- **(1) ample funds for operations and liquidity? YES, abundantly.** *"total available liquidity
  of $705.5 million"* at 2025-12-31, $386.2M of it cash.
- **(2) repurchases at a material discount to conservatively-calculated intrinsic value?** **The
  question does not arise: there were no repurchases at all, in any year 2021-2025.**
- **[E2-51] is the row that applies to a refusal:** *"A manager who consistently turns his back on
  repurchases, **when these clearly are in the interests of owners**, reveals more than he knows
  of his motivations."* **I decline to fire this flag, and I say why.** The clause *"when these
  clearly are in the interests of owners"* is a condition, and it was not met: the shares traded
  at **1.96x book** while **61% of segment earnings came from a business whose own management said
  would normalise**, which is the opposite of a demonstrated material discount. **[E5-24]**: *"what
  is smart at one price is dumb at another."* Buying back stock priced on peak commodity earnings
  would have been the error, not the omission. **And the cash had a named use: a $2,050 million
  five-year capital plan and, as it turned out, $103.5 million of settlements paid from cash on
  hand.** Stated with the **[E4-13]** humility clause.

**[E4-27] PAY — and the incentive is the [E2-01] metric itself, which is unusual and good.**
From the DEF 14A of 2026-03-02 (accession 0001466593-26-000023):
- **Annual cash incentive financial measures for 2025: Corporate Return on Equity** (for the CEO,
  CFO and General Counsel) **and Electric Platform Return on Equity** (for the utility president),
  plus non-financial measures for **workplace safety**, People & Culture and renewable-energy
  goals. **Capped at 200% of target.**
- **Long-term: performance shares vesting on (i) three-year adjusted ROE and (ii) total
  shareholder return relative to a peer group**; the ROE target is *"established … based on an
  evaluation of prior years annual adjusted ROE, Otter Tail Power Company authorized return on
  equity and EEI Index and regional peer utility return on equity history and trend."* Performance
  shares cap at **150%**.
- **Segregation of the windfall from the utility pay, and it is deliberate design:** the utility
  president is paid on **Electric Platform ROE**, not corporate ROE, so the man running the
  regulated business was **not** paid on the PVC price. *"the Electric Platform Return on Equity
  exceeded the threshold level"* — threshold, not target. **The corporate officers WERE paid on a
  Corporate ROE inflated by the windfall**, and the proxy says so approvingly: *"We produced a
  **utility sector leading return on equity of 16 percent** on an equity layer of 63 percent."*
  **[E4-41]** is the answer to that boast: a 16% ROE built on a price the company does not set is
  luck, and *"never, ever, think about something else when you should be thinking about the power
  of incentives"* **[E4-27]** is why it matters that a pay plan counted it.
- **And yet the money did not follow the windfall, which is the fact that decides this
  sub-section.** CEO **Non-Equity Incentive Plan Compensation: $1,403,783 (2023), $1,473,907
  (2024), $1,471,194 (2025)** — **essentially flat, +4.8% over two years**, across the peak and the
  decline. Total CEO compensation $5,823,726 → $6,388,314 → **$6,792,688**, **+16.6% over two
  years**, against net income that **fell** from $294.2M to $275.9M. **CEO total pay is 2.5% of
  2025 net income and the base salary is $867,578.** **There is no pay explosion to find here, and
  I looked for one.**
- **The candor line, quoted because it is the thing that will matter next year:** *"For 2025, there
  were **no adjustments to GAAP results** for purposes of determining awards under the Executive
  Annual Incentive Plan"* and *"For 2025, there was **no adjustment to ROE** made for calculation
  of performance share outcomes."* **Stated plainly, and it is the right answer. The test is
  whether it survives 2026**, the year of the $103.5 million and the newly-minted Adjusted ROE
  that the company itself says runs **380 basis points** above the GAAP figure. **That is the
  single most checkable Q3 prediction this file makes: read the 2027 proxy.**

**[E2-26] THE HALF-OWNER TEST — mostly passed, with one specific failure I can name.**
*Does this reporting tell me what I would want to know if the positions were reversed?*
**Passes:** the segment note gives revenue, significant expenses, net income, capex, D&A and
identifiable assets for all three segments for three years; **the MD&A gives the price and volume
percentage changes for PVC pipe every single year, which is what made Q2 unit series possible at
all**; the $103.5M settlement is its own income-statement line rather than buried; the tax
reconciliation is itemised; and management states in the annual report, unprompted, that its best
business earnings *"will continue to decline through 2027."* **A company hiding a reverting
commodity would not publish the price per pound.**
**Fails, in one place, and I found it by building Row B:** **Otter Tail does not disclose its rate
base in dollars.** The regulatory table gives the allowed *percentage* return on rate base and the
revenue requirement, and no base. **NorthWestern Energy, in the same table in its own 10-K,
publishes both `Authorized Rate Base (millions)` and `Year-end Estimated Rate Base (millions)`
for every jurisdiction** — $3,176.2M authorized against $3,425.6M estimated for Montana electric
alone. **A NorthWestern shareholder can compute the gap between authorised and actual rate base
and therefore the regulatory lag; an Otter Tail shareholder cannot.** For a company whose entire
stated growth strategy is *"rate base investments"*, **that is the one number a half-owner would
most want and it is not there.** It is not a flag under [E4-22]; it is a disclosure gap against a
demonstrated peer standard, and it is the artifact the Q1 UNRESEARCHED sub-item names.

**[E4-39] the candid acquisition post-mortem:** not applicable — **no acquisitions** in the window.
Recorded as absent rather than as a failure.

**[E4-34] the auditor eye test, fourth question — *"any action with the purpose and effect of
moving revenues or expenses from one reporting period to another"*:** I looked and found the
opposite of period-shifting. The $103.5 million was recognised **in full in the quarter the
settlement agreements were executed**, including the $30.0 million EUP tranche that was not paid
until July, and the filer warns forward that *"it is reasonably possible that our estimate of a
loss, if any, arising from these matters could change in the near term."* **That is a charge taken
early and flagged as unstable, not one deferred.**

### THE GUARDRAIL — checked before the verdict is written

- [x] **Confirmed: nothing in this Q3 is being used to promote the name.** Q2 is OUT and stays
      OUT. Four real positives sit above — no acquisitions with a windfall, no issuance, a clean
      [E4-29], and four years of conservative guidance beaten — and **[E2-37]** governs every one
      of them: *"a good managerial record (measured by economic returns) is **far more a function
      of what business boat you get into** than it is of how effectively you row."* **This is a
      competent crew in a regulated boat with a commodity outboard motor, and [E3-39] ranks the
      boat above the crew.**
- [x] **Key-person dependence** recorded at Q2 as absent, not here as a strength **[E4-23]**.
- [x] **Is a great manager the reason to act?** No, and the [E2-36] excisable-cancer branch does
      not open: there is no *"extraordinary business franchise"* for a surgeon to operate on — Q2
      found none.
- [x] **[E3-40] loss of focus** — *"capital wandering away from the base business"*: **not found.**
      The capital went into the base business. **This is the one damage vector the corpus says
      worries it most, and it is absent.**
- [x] **[E5-45] the ABCs — arrogance, bureaucracy, complacency:** the only specimen is the proxy
      *"utility sector leading return on equity of 16 percent"*, which is a windfall described as
      an achievement. **A small one, and it is one line.**

### VERDICT

- **VERDICT: [x] UNKNOWABLE → the honesty binary cannot be closed while the DOJ Antitrust
  Division grand jury matter on the pricing of this company PVC pipe is open, the Canadian class
  action is undecided and the Board has not answered the derivative demand. RECORDED, NOT
  GOVERNING — the file closed at Q2 OUT.**
  - **What specifically cannot be known:** whether the conduct alleged in the PVC pipe information
    exchange occurred. No document that exists resolves it; the settlements expressly do not.
  - **The one UNRESEARCHED sub-item, with its artifact and its blocked rung:** the three amended
    class complaints in **No. 1:24-cv-07639 (N.D. Ill.), August 2025**, which live on **PACER /
    CourtListener** — **not a rung on this framework evidence ladder.** The ladder-legal
    substitutes were read: Otter Tail Note 10 and **Atkore fuller account of the identical case,
    which IS a competitor filing and IS on the ladder.**
  - **What I did find, stated the way [E5-17] requires:** on the filings as they stand, **no
    disqualifier found** — and that is not a finding that the managers are honest. Two flags fire
    hard (**[E2-49]** metric-switching and **[E2-57]** except-for, both on the Q2 2026 release),
    one fires as a standing prompt (**[E4-22]** projections, answered well by the outturn record),
    and five that commonly fire in this queue do not fire at all: **no EBITDA promotion, no serial
    issuance, no acquisitions, no dividends funded by issuance, no smoothed earnings series.**

---

## Q4 — WILL IT SURVIVE?
**RECORDED, NOT GOVERNING.** The file closed at Q2 OUT on the business. Every figure below is
built anyway, because the queue output contract requires a price and because the arithmetic turns
out to be a second, independent reason this name goes nowhere.

### Owner earnings — the one number **[E2-23]**

**THE CONVENTION, STATED:** owner earnings = **multi-year mean operating cash flow, less
share-based compensation, less the (c) guess.** Operating cash flow nets the working-capital
change from one audited line, which is [E2-23] constraint 3 applied. Script and output:
`Test Runs/_research 2026-09-19 OTTR/oe.py` and `oe_output.txt`.

#### (c) IS A DISCLOSED JUDGMENT, AND THE TWO HALVES GET DIFFERENT TREATMENT — [E5-20]

> "in the case of all railroads, **merely spending their depreciation expense will not keep them
> in the same place** … the true maintenance capex … is **higher than 60 percent** of [total
> capex]" — **[E5-20]**; and the framework rule built on it: *"Where the business is
> capital-intensive — railroads, airlines, **utilities**, anything whose own filing says
> depreciation understates renewal — **the D&A end of any owner-earnings range is INVALID, not
> merely optimistic**, and (c) is judged upward from total capex."*

**The framework names utilities in that sentence. 75.8% of this company assets are the
utility. So the D&A end is INVALID here as a matter of the governing document, and I show it only
as a display of the guess, marked invalid in every table.**

**The two halves, and I state how I treated each:**

| | **Electric** | **Manufacturing + Plastics** |
|---|---|---|
| FY2025 capex | **$270,593** | $16,841 |
| FY2025 D&A | **$90,168** | $27,704 |
| capex ÷ D&A | **3.00x** | **0.61x** |
| **which corpus rule governs** | **[E5-20] — D&A INVALID, judge (c) up from capex** | **[E3-44] / [E2-41] — D&A is the DEFAULT and it is the higher figure, so it is conservative here** |

**That table is why a single consolidated (c) would be wrong in both directions at once**: it
would understate the utility and overstate the manufacturing platform.

**THE (c) JUDGMENT, BUILT FROM THE FILER OWN FIVE-YEAR PLAN.** The FY2025 10-K publishes
anticipated capital expenditure for **2026-2030 by category** — which is precisely the
disaggregation [E2-23] needs and most filers do not give:

| Electric category, 2026-2030 | total | per year | is it maintenance under [E2-23]? |
|---|---|---|---|
| Renewable Generation and Storage | **$645M** | $129.0M | **YES.** It **replaces** the coal fleet the MPUC has ordered retired. The utility cannot keep selling the same MWh to the same customers without it. |
| Transmission | **$855M** | $171.0M | **NO — growth.** MISO regional build that expands the rate base. |
| Distribution | **$268M** | $53.6M | **YES.** Poles, wires, meters. |
| Other | **$153M** | $30.6M | **YES.** |
| **Electric total** | **$1,921M** | $384.2M | |
| Manufacturing + Plastics | **$129M** | $25.8M | **YES**, and it is below that platform D&A of ~$27.7M |
| **TOTAL PLAN** | **$2,050M** | **$410.0M** | |

**(c) JUDGMENT = $213.2M (Electric renewal) + $25.8M (Manufacturing Platform) = $239.0M a year.**
**That is 2.02x consolidated D&A of $118.1M**, which is [E5-20] describing itself: spending
depreciation would not keep this company in the same place, and I have said by how much and from
which filed lines. **$171.0M a year of Transmission is EXCLUDED from (c) as growth — that is the
one place I have been generous to the company, and it is disclosed.**

**SBC — RESOLVES, AND IT IS COMPLETE.** Eighteen consecutive filed years, FY2008 through FY2025,
**every year present and every year non-zero**: 3,850 / 3,563 / 2,923 / 2,177 / 1,311 / 1,456 /
1,783 / 1,716 / 3,178 / 3,642 / 4,441 / 5,958 / 6,284 / 6,908 / 6,814 / **7,753 / 9,529 / 9,119**.
No zero to trip the SBC-of-zero defect recorded on 2026-09-12. Subtracted **in full** [E5-06].
**And [E3-70] checked rather than assumed** — *"the measure is market value, not the accounting
charge … subtract an amount equal to what the company could have realized by publicly selling
options of like quantity and structure."* **There are no options.** The plans grant restricted
stock and performance shares, and the filing gives the market-value cross-check directly: the
**fair value of vested awards in FY2025 was $3.6 million (restricted) plus $5.5 million
(performance) = $9.1 million**, against a charge of **$9,119 thousand**. **Charge equals market
value; the [E3-70] uplift is nil.** SBC is **2.36% of FY2025 operating cash** — trivial, and
survival shape #2 does not apply.

#### THE WINDOWS — EVERY ONE, AS [E4-38] REQUIRES, NOT A CHOSEN ONE

> *"growth-rate presentations can be significantly distorted by **a calculated selection of either
> initial or terminal dates**"* — **[E4-38]**, whose remedy is to publish **every** window.

**AS FILED. Owner earnings, $ thousands, and the yield on a $3,670.4 million market cap:**

| window | **(c) = total capex** | **(c) = THE JUDGMENT, $239.0M** | (c) = D&A ***INVALID [E5-20]*** |
|---|---|---|---|
| 3y 2023-25 | $94,321 — **2.57%** | $166,605 — **4.54%** | $297,877 — *8.12%* |
| 4y 2022-25 | $123,581 — **3.37%** | $160,827 — **4.38%** | $295,882 — *8.06%* |
| **5y 2021-25 (the [E2-42] default)** | **$109,366 — 2.98%** | **$125,729 — 3.43%** | $263,301 — *7.17%* |
| 6y 2020-25 | $63,486 — **1.73%** | $99,214 — **2.70%** | $240,018 — *6.54%* |
| 7y 2019-25 | $50,375 — **1.37%** | $76,480 — **2.08%** | $220,157 — *6.00%* |
| **TTM to 2026-06-30** | **−$89,516 — −2.44%** | $160,068 — **4.36%** | $278,994 — *7.60%* |
| **TTM, adjusted for the escrow actually paid (below)** | **−$163,016 — −4.44%** | **$86,568 — 2.36%** | $205,494 — *5.60%* |

**AS-FILED BAND: −$163.0 million to +$297.9 million, i.e. −4.44% to 8.12%. IT SPANS ZERO.**
**Strike the invalid D&A column, as [E5-20] requires, and the legitimate band is −4.44% to
+4.54% — which still spans zero, and whose best cell is 4.54%.**

**THE ESCROW ADJUSTMENT, AND I FOUND IT ONLY BY READING THE CASH-FLOW DETAIL LINES.** The Q2 2026
cash-flow statement adds back **`Legal Settlement Expenses | 103,500`** as a non-cash item — and
the **$73.5 million that Northern Pipe and Vinyltech actually paid into the settlement escrow in
June 2026 appears nowhere as an outflow**, because the statement reconciles *"Cash, Cash
Equivalents **and Restricted Cash**"* and the escrow is inside the ending balance. **So the filed
H1 2026 operating cash of $182,711 thousand overstates the cash available to owners by $73.5
million.** The money has left the company control — it is restricted *"until such time the
related settlement agreements receive final court approval and the funds are disbursed to the
class members"* — and a further **$30.0 million went out in July 2026**, in the quarter after the
TTM window closes. **I show the TTM both ways and the adjusted row is the honest one.** *(This is
not an accounting criticism: the presentation is what ASU 2016-18 requires. It is a reading
finding, and it is why the framework insists on the detail lines [E3-27].)*

**THE SPREAD IS ITSELF A Q4 FINDING [E5-11], AND I CAN NAME EVERY DISTORTION IN IT:**
1. **FY2020 capex of $371,553 thousand** — the Merricourt wind and Astoria Station build, a single
   year at **4.5x that year D&A**. It is why the 6- and 7-year capex-end cells are the lowest in
   the table. A real historical fact, not an artifact, and **not silently dropped [E4-25]**.
2. **H1 2026 capex of $324,755 thousand against H1 2025 of $124,239** — a **161% increase in one
   half-year**, consistent with the plan $467M for 2026, which is why the TTM capex-end cell is
   negative. **The TTM is the most front-loaded capex period in the company history and it is
   labelled as such rather than presented as a run rate.**
3. **The plastics boom sits in every window from 2021**, which is the next section.
4. Note what is NOT a distortion: **the $103.5 million settlement charge stays in.** **[E5-33]**:
   *"to tell owners year after year, 'Don't count this' … is misleading"*, and even a disclosed
   one-time rebasing is *explained for years*, never annualized away. **The company adjusted
   measure excludes it; this run does not.**

#### WITHOUT THE PLASTICS BOOM — SHOWN SEPARATELY, NEVER SILENTLY DROPPED [E4-25, E4-41]

> **[E4-41]:** *normalize the mean DOWN for luck* — Berkshire own pro-forma stripped a no-megacat
> year and a bond tailwind, *"about $500 million less than we actually reported."* **Favourable
> exogenous breaks in the window are named and removed before the mean is trusted.**

**The break is named and it is not a judgment call: the filer says it was a Gulf Coast hurricane
and a resin shortage.** The baseline is **four filed years untouched by it**, 2017-2020:
**mean Plastics operating margin 16.7%**, mean Plastics operating income **$32,206 thousand**.

**Two normalisation methods, because one of them has to be wrong and I will not pick silently:**
- **METHOD A** — price **actual** revenue at the **pre-boom 16.7% margin.** Respects six years of
  inflation and mix; assumes the revenue line itself is normal, which flatters the result because
  much of the revenue rise IS the abnormal price.
- **METHOD B** — hold the **pre-boom dollar income**, scaled by the **pounds index** from Q2.
  Uses the physical series, which is the honest one [E4-55]; ignores inflation, so it is harsh.

| year | filed Plastics operating income | method A normal | method B normal | after-tax excess removed, A | B |
|---|---|---|---|---|---|
| 2021 | $132,760 | $63,496 | $32,753 | $51,227 | $73,964 |
| 2022 | $264,578 | $85,589 | $26,538 | $132,378 | $176,052 |
| 2023 | $254,402 | $69,808 | $22,802 | $136,523 | $171,288 |
| 2024 | $271,905 | $77,392 | $28,985 | $143,859 | $179,660 |
| 2025 | $231,079 | $70,598 | $31,304 | $118,690 | $147,751 |

*(taxed at the Plastics segment own filed FY2025 effective rate, **26.0%** = $59,999 ÷ $230,399.)*

**OWNER EARNINGS WITHOUT THE BOOM, every window, both (c) ends, both methods:**

| window | method A: capex end | A: judgment | A: D&A *(invalid)* | method B: capex end | B: judgment | B: D&A *(invalid)* |
|---|---|---|---|---|---|---|
| 3y 2023-25 | **−$38,703** | **$33,581** | *$164,853* | **−$71,913** | **$371** | *$131,644* |
| 4y 2022-25 | **−$9,282** | **$27,965** | *$163,020* | **−$45,107** | **−$7,861** | *$127,195* |
| **5y 2021-25** | **−$7,170** | **$9,193** | *$146,766* | **−$40,377** | **−$24,014** | *$113,558* |
| 6y 2020-25 | **−$33,627** | **$2,101** | *$142,905* | **−$61,300** | **−$25,572** | *$115,232* |
| 7y 2019-25 | **−$32,864** | **−$6,760** | *$136,918* | **−$56,584** | **−$30,479** | *$113,198* |

**NORMALISED BAND: −$71.9 million to +$164.9 million, i.e. −1.96% to +4.49%; and with the invalid
D&A column struck, −1.96% to +0.91%.**

**WHAT THAT MEANS IN ONE SENTENCE: strip the boom, treat the utility as the framework says a
utility must be treated, and this company produces owner earnings of approximately NOTHING —
between minus two per cent and plus one per cent of its market capitalisation.** The entire
positive number in the as-filed table is the plastics price, and the plastics price is the thing
Q2 found is not owned, is reverting, is 2.12x its 2020 level on 0.972x the pounds, and is the
subject of a federal grand jury.

**[E4-25]: IS THE RANGE TOO WIDE TO REACH A CONCLUSION?** **About the LEVEL, yes** — −$163M to
+$298M is not a value estimate, and the corpus says *"Usually, the range must be so wide that no
useful conclusion can be reached"* is the normal outcome. **About the DECISION, no, and this is
the one case where a useless range is still a finished answer:** the range is bounded above at
**8.12% even at the construction the framework declares INVALID**, and at **4.54%** at the best
legitimate one. **Every single cell in both tables — thirty-nine of them — is below the ~10%
[E4-28] floor.** A range whose maximum is under the floor does not need narrowing.

#### Great, good, or gruesome? **[E4-20]** — and the answer has to be given per half

- **Electric: GOOD, at the bottom of the good class, and below the corpus own satisfactory mark.**
  **[E4-43]** is explicit that the good class *passes*: capital-hungry growth *"may well prove to
  be a satisfactory investment."* But **[E5-40]** puts a number on it — **~12% on retained
  utility capital is *"quite satisfactory"*** — and Otter Tail retains at allowed ROEs of
  **8.75%, 9.48% and 10.10%**, every one below 12%, two of them with clawbacks above the allowed
  level. **It pays an attractive-ish rate, earned also on deposits added, and the rate is set by
  someone else at under twelve per cent.**
- **Plastics: none of the three, and that is the finding.** It has the *cash* characteristics of
  the **great** account — $7.9 million of capex against $422.8 million of revenue and a 123.9%
  pre-tax return on its assets — and none of its durability. **[E4-20]** great account *"pays an
  extraordinarily high interest rate **that will rise as the years pass**."* This one has fallen
  for three consecutive years on management own stated expectation of further decline. **It is a
  great account with a maturity date, which is not a savings account at all.**
- **Manufacturing: the weakest of the three and nobody notices.** $16.9 million pre-tax on
  $243.7 million of assets — **6.9%** — with revenue down from $402.8M (2023) to $314.5M (2025),
  a **−21.9% two-year decline**, and three customers at 44% of it.
- **CONSOLIDATED: GOOD.** And the shape of it is what matters: **the capital-consuming half is the
  one earning 9-10% by law, and the half that needs no capital is the half that is reverting.**

#### Staying power — score all three **[E5-11]**

> "**(1) a large and reliable stream of earnings; (2) massive liquid assets and (3) no significant
> near-term cash requirements.** **Ignoring that last necessity is what usually leads companies to
> experience unexpected problems**" — **[E5-11]**

**(1) A large and reliable stream of earnings — PASS, on the Electric half only.** Electric
segment net income $66.8M (2020) → $72.5M → $80.0M → $84.4M → $91.0M → **$97.6M (2025)**, six
consecutive years of increase, from a regulated monopoly serving ~134,000 customers whose retail
rates are 19% below the regional average. **That is as reliable as an earnings stream gets.** The
Plastics stream is large and, on the company own written statement, **not reliable** — and it is
61% of segment net income.

**(2) Massive liquid assets — PASS, with a live deduction.** *"total available liquidity of $705.5
million"* at 2025-12-31, of which **$386,193 thousand cash.** **But at 2026-06-30 the balance is
$351,883 thousand of cash, cash equivalents AND RESTRICTED CASH, of which $73,500 is the
settlement escrow** — so roughly **$278 million unrestricted** — and **a further $30.0 million
left in July 2026**, leaving on the order of **$248 million.** Still substantial against $1,107
million of debt. **Pass, and the deduction is stated rather than netted quietly.**

**(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — FAIL, AND THIS IS THE ONE THE CORPUS SAYS
USUALLY KILLS.**
- The filed plan is **$467 million of capex in 2026 and $574 million in 2027**, against operating
  cash that has never exceeded **$452.7 million** in any year.
- **H1 2026 already proves the gap:** capex **$324,755** against operating cash **$182,711** — a
  **$142.0 million shortfall in six months** — funded by **$170,000 thousand of new long-term
  debt** raised in the half.
- **Contractual obligations at 2025-12-31: $140 million of debt due within one year plus $47
  million of interest**, and **$2,533 million in total** including **$417 million of coal
  obligations running to 2040** under the Coyote Creek Lignite Sales Agreement, a
  take-or-pay structure whose price *"reflects the cost of production, along with an agreed-upon
  profit and capital charge"* on a plant one of its three regulators has ordered it to stop using.
- **And the filer says it plainly:** *"**Debt financing will be required in the five-year period
  from 2026 through 2030** to refinance maturing debt and to finance our planned capital
  investments."*
- **[E5-39]** is the standard: *"We will never be dependent on **the kindness of strangers** …
  cash is a lot like oxygen."* **Otter Tail capital plan is dependent on the debt markets being
  open for five consecutive years.** For a regulated utility that is normal, and the regulator
  allows a return on the capital raised — **but "normal for the industry" is not the test [E3-29]
  taught about leverage ratios, and strength 3 is scored FAIL on the filer own sentence.**

**LEVERAGE, NAMED AND QUANTIFIED — there is no ratio ceiling in this framework and I do not
invent one.** Debt obligations **$1,107 million** against book equity of **$1,876.9 million** at
2026-06-30 = **0.59x**. Year-end **equity ratio to total capital 62.8%** on the filer own
statement — **higher than the 52.5-53.5% equity layers the commissions themselves authorise**,
which means Otter Tail is financed more conservatively than its own tariffs assume. Weighted-average
interest rate on outstanding borrowings **4.95%** at 2026-06-30, **below the 5.34% sovereign.**
Investment-grade ratings; all financial covenants complied with at 2025-12-31.

**[E2-54] THE COVERAGE TEST, which is the one the corpus actually supplies:** *"whenever someone
creates a capital structure that does not allow **all interest, both payable and accrued, to be
comfortably met out of current cash flow net of ample capital expenditures — zip up your
wallet.**"*
- On **total capex**: (OCF $385,985 − capex $288,068) ÷ interest paid $45,701 = **2.14x.**
- On the **(c) judgment**: (OCF $385,985 − $239,000) ÷ $45,701 = **3.22x.**
- **Both clear "comfortably", and that is the correct answer: this company is not going to fail.**
  The test is passed and I say so.

**[E3-52] read the terms, not just the quantity:** $805 million of the $1,107 million is due
**beyond five years**; only $140 million within one; $50.0 million of 5.49% notes due 2035 and
$50.0 million of 5.98% notes due **2055**. Long-dated, covenanted but complied with, and at rates
at or below the sovereign. **This is well-termed debt.**

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24]**

**IT DOES NOT DIE. THE OWNER RETURN DIES, AND I CAN QUANTIFY IT FROM FILED FIGURES.**

**THE MECHANISM, in one sentence.** A temporary, un-owned excess return in a small unregulated leg
is being converted, dollar for dollar, into **permanent regulated rate base earning 8.75-10.10% by
law** — and when the excess reverts, as management says it will by 2027 and as every listed peer
already has, the buyer who paid $87.42 for consolidated earnings of $6.55 owns a utility earning
its allowed return, with the windfall cash already poured into the ground in Minnesota where a
commissioner decides what it yields.

**QUANTIFIED, FROM FILED FIGURES [E3-24]:**
- Full reversion of Plastics operating income from the filed **$231,079** to the pre-boom margin on
  2025 revenue (**$70,598**) = **−$160,481 thousand pre-tax**, **−$118,690 after tax** at the
  segment 26.0% rate.
- On 42,117 thousand diluted shares that is **−$2.82 per share**, taking FY2025 diluted EPS of
  **$6.55 to $3.73.**
- **Cross-check against management own forecast:** the company 2026 GAAP guidance midpoint is
  **$4.04** and its adjusted midpoint **$5.88**. **My full-reversion figure of $3.73 sits BELOW
  the company GAAP guidance**, i.e. the reversion is **not yet complete in their own 2026
  forecast** — which is consistent with their words (*"gradually normalize through 2027"*) and
  means the decline still has further to run on their arithmetic as well as mine.
- **At $3.73 of EPS the company is entirely solvent:** ~$157 million of net income, interest paid
  $45.7 million, a 62.8% equity layer, and an 88th consecutive dividend year. **Nothing breaks.**
- **What breaks is the price.** At $87.42 that is **23.4x** the reverted figure, for a business
  whose surviving engine is legally capped at a sub-10% return on equity.

**LIKELIHOOD: [x] LIKELY.** Not a possibility — the reversion is already four years in progress on
the filer own disclosed series (price per pound −5%, −12%, −15% in 2023, 2024, 2025), **every
comparable listed participant has already completed it** (Westlake to −14.1%, Atkore to 0.8%, Olin
to 0.1%), **and management states it in the annual report and repeats it in the earnings
release.** The only open question is the end level and the date.

**[E4-40] MODEL EXPOSURE, NOT EXPERIENCE** — *"all of us in the industry made a fundamental
underwriting mistake by **focusing on experience, rather than exposure**."* So, two further
exposures the recent record does not show, each stated with its own likelihood:
- **The antitrust tail beyond the US settlement — A REAL POSSIBILITY, and unquantifiable from any
  filing.** The **DOJ Antitrust Division grand jury** matter is open and the DOJ asked on
  2026-07-01 to extend its stay to **2026-12-31**. The **British Columbia class action is
  unsettled** and the plaintiffs seek *"general damages … punitive damages."* The **derivative
  demand is unanswered.** The US settlement cost **$103.5 million — 2.8% of the market
  capitalisation** — and there is **no filed figure that bounds the rest.** Under [E4-19] that
  specific magnitude is **UNKNOWABLE**, and it is the honest label: the company itself says *"we
  are unable to determine the likelihood of any outcome."*
- **Coyote Station stranded cost — A LOW-LEVEL POSSIBILITY, and small.** The MPUC has ordered OTP
  to stop serving Minnesota customers from Coyote Station before its life ends, and OTP has asked
  for accelerated recovery of the jurisdictionally allocated remaining investment, stated at *"a
  $4.3 million annual impact"* deferred *"until 2041"*. **The MPUC has already excluded that item
  from interim rates.** Fifteen years at $4.3 million is roughly **$65 million** of book value at
  stake — about **1.8% of the market capitalisation.** Real, disclosed, and not material to
  solvency.

**AGAINST THE SHAPES INDEX — I propose a new one, and I say why the existing ones do not fit.**
Checked against `Screens/SURVIVAL SHAPES - index.md` (twenty-seven rows, maximum number 26):
- **#11 THE PASS-THROUGH is present as a FEATURE, not the mechanism.** The plastics gains are
  going back to buyers — price −15% against input cost −14% in 2025, and the new Vinyltech
  capacity arrived in the same year the price fell — but the pass-through describes the plastics
  leg only, and the company overall return does not die from it, because plastics is 4.7% of the
  assets.
- **#10 THE CAMOUFLAGE does not fit**, and this is the closest miss. Camouflage requires cash from
  a strong leg recycled into legs that *"must re-win a race each cycle."* **The Electric segment
  does not re-win any race.** It has a legal monopoly and a guaranteed-return formula. It is not a
  bad business that eats the good business cash; it is a **capped** business that eats it.
- **#5 THE SELF-LIQUIDATING DISTRIBUTION does not fit:** the dividend is 20% of operating cash and
  covered 4.8x; nothing is being sold to pay it.
- **#20 THE WAVE (AEHR) does not fit:** that is one customer capacity cycle in one new market.
  This was an economy-wide supply shock in a commodity input, affecting every participant, and
  Otter Tail volume never rose — it fell.

**PROPOSED #27 — THE CONVERTED WINDFALL.** *A temporary excess return in a small unregulated leg,
caused by an exogenous supply shock the company did not create and does not control, is converted
dollar for dollar into permanent regulated rate base earning a return the counterparty sets below
the buyer hurdle. The company gets larger, safer and more predictable with every dollar of the
conversion; the reported earnings then revert toward the regulated level, on the company own
schedule; and the owner who capitalised the windfall earnings owns a utility. Nothing fails, no
covenant breaks, no dividend is cut — the windfall is simply gone, and irreversibly, because the
money is in the ground and the return on it is set by law.*
**Its tells, checkable on any filer:** a segment holding under 10% of assets and over half of
segment income; that segment capex a fraction of its depreciation while another segment capex is
a multiple of its own; the filer own price-per-unit disclosure showing the whole gain is price
while the unit series is flat or down; a five-year capital plan in the capped segment worth more
than a decade of that segment earnings; and an allowed return below the [E5-40] ~12% mark.
**Distinct from #10 because there is no race and no weak leg — the destination business is
excellent at what it does and legally prevented from earning more.**

- **VERDICT: [x] UNKNOWABLE** *(recorded, not governing — the file closed at Q2)*
  **What specifically cannot be known:** the sustainable level of Plastics earnings, and therefore
  the level of owner earnings. The band is **−$163.0M to +$297.9M as filed** and **−$71.9M to
  +$164.9M stripped of the boom**, and it **spans zero on the conservative construction in every
  window.** **[E4-25]**: *"Usually, the range must be so wide that no useful conclusion can be
  reached"* — and that is the verdict, honestly, rather than resolved by preference.
  **The one thing the width does NOT obscure: every one of the thirty-nine cells computed above is
  below the ~10% [E4-28] floor, including the cells the framework declares invalid for being too
  generous.**
  Survival itself is not in question: **[E2-54] coverage 2.14x to 3.22x, a 62.8% equity layer,
  $805M of $1,107M of debt due beyond five years, and 87 consecutive years of dividends.**

---

## Q5 — COMPUTATION — NOT A CLEARANCE

⛔ **Q5 DID NOT OPEN. Q2 returned OUT on the business, so under operator rule 2 no Q5 output may
be reported as a clearance and this block carries NO ENTRY LANGUAGE.** It is produced because the
queue output contract requires every run to end with a price either way (operator rule 3 and the
`WATCHLIST RUN QUEUE.md` heading), and because the arithmetic is an independent second reason the
name goes nowhere.

### The price, and what the buyer is paying for, in words

- **Price US$87.42**, close of **2026-09-18**, Yahoo via `tools/sources.py:price('OTTR')` — an
  **aggregator, live quote only, flagged.**
- **41,985,580 shares** off the Q2 2026 10-Q cover, accession 0001466593-26-000071, checked
  against the $5 par line and the absence of treasury stock.
- **Market capitalisation US$3,670.4 million.**
- **Sovereign 5.34%**, US Treasury 30-year par yield curve, 2026-09-18, issuing authority.
- **1.96x** the 2026-06-30 book value per share of **$44.70**.
- **13.3x** FY2025 diluted EPS of $6.55 · **21.6x** the company own 2026 GAAP guidance midpoint of
  **$4.04** · **23.4x** the fully-reverted $3.73 computed at Q4.
- Dividend **$2.31** annualised (four times the $0.5775 declared 2026-01-08) = a **2.64%** yield,
  against a **5.34%** sovereign. **The dividend yields 2.70 points LESS than a thirty-year
  Treasury.**

**WHAT THE BUYER IS ACTUALLY PAYING FOR, WITHOUT MANAGEMENT LANGUAGE AND WITHOUT MINE.** At
$87.42 a buyer pays $3.67 billion for two things. **The first is a small electric utility in three
sparsely-populated states** that owns about three billion dollars of plant, is legally permitted to
earn **9.48%, 10.10% and 8.75%** on the equity portion of it, must give back **70%** of any North
Dakota earnings above 10.20% and **100%** of any South Dakota earnings above 9.50%, and intends to
spend **$1,921 million** on more of it over the next five years — nineteen years of that segment
current earnings — funded partly by borrowing, because the plan exceeds the cash. **The second is
a PVC pipe extruder that sold fewer pounds of pipe in 2025 than in 2020 and earned 6.1 times as
much money from them**, because a hurricane closed Gulf Coast resin plants in 2021 and the price
per pound is still 2.12 times its 2020 level — a price every comparable listed competitor has
already lost, which the company own annual report says will *"gradually normalize through 2027"*,
and which is the subject of **$103.5 million already paid** to settle three antitrust classes, an
**open DOJ Antitrust Division grand jury subpoena**, an unsettled Canadian class action and an
unanswered shareholder derivative demand. **The buyer is paying 22 times a normal year of owner
earnings for a capped return and a reverting windfall.**

### 1. THE YIELD — owner earnings ÷ market cap, beside the sovereign

| construction | owner earnings | **yield** | **vs the 5.34% sovereign** |
|---|---|---|---|
| 3y 2023-25, (c) judgment — **the most favourable legitimate cell in the file** | $166,605 | **4.54%** | **−0.80 pts** |
| 5y 2021-25, (c) judgment — **the [E2-42] default window** | $125,729 | **3.43%** | **−1.91 pts** |
| 7y 2019-25, (c) judgment | $76,480 | **2.08%** | **−3.26 pts** |
| 5y 2021-25, (c) = total capex | $109,366 | **2.98%** | **−2.36 pts** |
| 3y 2023-25, (c) = total capex | $94,321 | **2.57%** | **−2.77 pts** |
| TTM to 2026-06-30, escrow-adjusted, (c) judgment | $86,568 | **2.36%** | **−2.98 pts** |
| **ex-boom (method A), 3y, judgment** | $33,581 | **0.91%** | **−4.43 pts** |
| **ex-boom (method B), 7y, judgment** | −$30,479 | **−0.83%** | **−6.17 pts** |
| *3y, (c) = D&A — **INVALID for a utility [E5-20]**, shown only as the display of the guess* | *$297,877* | *8.12%* | *+2.78 pts* |

**EVERY LEGITIMATE CONSTRUCTION YIELDS LESS THAN THE GOVERNMENT BOND.** The single cell that
clears the bond is the one the governing framework declares invalid for exactly this class of
business. **The bare sovereign is used, with no per-name premium added [E3-42]** — certainty is
priced at the understanding gate and in the end discount, never in the rate.

### 2. WHAT THE PRICE ALREADY ASSUMES

- **Owner earnings required for an honest 10% pre-tax expectancy at this price: $367.0 million.**
  The best legitimate figure in the file is **$166.6 million.** **The price needs owner earnings to
  be 2.20 times larger than the most favourable legitimate measurement of them.**
- **Expressed as growth**, at a 10% discount rate the quote requires **5.46% perpetual growth in
  owner earnings.** Merely to match the 5.34% sovereign it requires **0.80% perpetual growth.**
- **What the business has actually done.** Owner earnings on the (c) judgment read $76.5M (7y) →
  $125.7M (5y) → $166.6M (3y), which *looks* like 5.46% growth is conservative. **It is the boom
  rolling forward through the window, and the ex-boom series is the answer:** −$6.8M (7y) →
  $9.2M (5y) → $33.6M (3y) on method A, and **negative in four of five windows on method B.**
  The physical series is flat to down: **pounds of pipe 0.972x the 2020 level; Manufacturing
  revenue $402.8M (2023) → $314.5M (2025), −21.9%.** The only unit that is growing is the
  **rate base**, and growth in rate base is growth in the *denominator* as much as the numerator.
- **[E4-44] the second bound:** *"the value of an asset, whatever its character, **cannot over the
  long term grow faster than its earnings do.**"* The quote implies 5.46% forever from a company
  whose 61%-of-earnings engine its own management says is normalising and whose 75.8%-of-assets
  engine is capped by statute.
- **[E4-35] the base rate on the growth belief:** *"fewer than 10 of the 200 most profitable
  companies in 2000 will attain 15% annual growth in earnings-per-share over the next 20 years."*
  5.46% is not 15%, so the required growth is not extreme — **which is why the failure here is not
  a growth argument at all. It is that the starting yield is 4.54% against a 5.34% bond, and the
  growth is required merely to reach the floor, not to beat it.**
- **[E2-63] STATE THE CEILING, and this company has one written into its tariffs.** The WPPSS
  analysis capped its own upside at face value; here the cap is legal text: **North Dakota returns
  70% of earnings above a 10.20% ROE; South Dakota returns 50% above 8.75% and 100% above 9.50%.**
  **75.8% of the assets sit behind a stated statutory ceiling on the return**, and the remaining
  upside lives in a commodity price the filer does not set and the DOJ is investigating. **The
  upside is bounded by the same documents that guarantee the downside.**

### 3. WHAT YOU ARE PAID

**At $87.42 the buyer is paid MINUS 0.80 points over the sovereign at the most favourable
legitimate construction, minus 1.91 points at the framework default five-year window, and minus
4.43 points once the named windfall [E4-41] is removed.** You are paid less than nothing to own
the operating risk, the regulatory risk, the reversion and the open criminal antitrust matter.

### THE FLOOR — [E4-28], and it is not close

> *"that's the figure we quit on … we don't want to buy equities where our real expectancy is
> below 10 percent. Now, **that's true whether short rates are 6 percent or whether short rates
> are 1 percent.**"* — **[E4-28]**

**Honest pre-tax expectancy at this price: 4.54% at the very best, 3.43% at the framework default
window, 0.91% once the boom is removed.** Every figure is **below roughly 10%.**
**The name is not ranked. It is quit on.** And it is quit on twice over: **it is below the floor,
and it is below the bond as well** — which is rarer than the floor failure and worth naming,
because most names that fail [E4-28] at least clear the sovereign. **Otter Tail does not.** *(This
is the inverse of the Berkshire case CLAUDE.md names — above the bond, below the floor. OTTR is
below both.)*

### THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]

| basis | 7y owner earnings | 5y | 3y |
|---|---|---|---|
| at the ~10% floor (10x) | **$18** | **$30** | **$40** |
| at the bare 5.34% sovereign (18.7x) | **$34** | **$56** | **$74** |

**So, in round numbers: roughly $20 to $40 a share against the [E4-28] floor, and roughly $35 to
$75 a share against the bare sovereign. Ex-boom, the floor-based range collapses toward nil to
about $8.** **The price is $87.42 — above the top of every range computed.**

### WHICH BAR — and only one

- [ ] Normal method [E4-11]
- [x] **SCREAMER TEST [E4-01].** *"Take the conservative end of the range and ask whether the price
  already clears it. **No margin is added on top.**"* Three outcomes: below the conservative case →
  act; inside the range → no useful conclusion, move on; **above the whole range → no.**
  **OUTCOME: the price is ABOVE THE WHOLE RANGE on both bases. The answer is no, and no margin was
  subtracted to get there, which is the cleanest form of the answer available.**
- **WINDAGE COUNT: ONE.** Conservatism is spent once **[E4-11, E4-48]** — *"try to be as realistic
  as you can on those numbers, but with any errors being on the conservative side. And then when
  you get all through, you apply the margin of safety."* The single place I applied it is the
  **removal of the named windfall [E4-41]**, and **even that is shown side by side with the
  as-filed figures rather than replacing them**, so the reader can refuse it. **No end margin was
  applied**, because Bar 2 forbids one and because the price clears nothing before any margin. **I
  was also generous in one direction and say so: $171.0 million a year of Transmission capex was
  excluded from (c) as growth.** The net of the two is not stacked conservatism.

- **VERDICT: [x] UNKNOWABLE on the value; and on the price, QUIT ON at the [E4-28] floor.**
  **Ranking position: NOT RANKED.** A candidate below the floor is not ranked [E4-28], and the file
  was already closed at Q2 in any case.

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**There is nothing to sell. The file closed at Q2 OUT on the business.** Per the **QLYS ruling of
2026-09-07**, a name that failed on the business gets **no price alert and no `PORTFOLIO.md`
row** — a price band on a business finding is a category error. What is recorded instead is the
**reversal condition in words**, pre-committed now rather than reverse-engineered later
**[E1-02]**.

### WHAT WOULD HAVE TO BECOME TRUE FOR THIS FILE TO BE WRONG

**Q2 fell on three independent grounds and a reopening needs ALL THREE to fall, not one.**

1. **The Electric half fails [E3-03] criterion 3 by definition.** **This cannot be reversed by any
   event short of deregulation of retail electricity in Minnesota, North Dakota and South
   Dakota.** It is the permanent limb of the verdict. *(A reader who disagrees with the framework
   on this point should note it is the framework, not this run: [E3-03] names price regulation as
   an exclusion, and [E2-59] explains why regulation floors a commodity business without creating
   a franchise.)*
2. **The Plastics half fails criterion 2 on the filer own sentence** naming ductile iron, HDPE,
   steel and concrete. **Reversal would require the filing itself to change** — i.e. Otter Tail
   asserting, and the competitor row supporting, that municipal water pipe has no close substitute.
   HDPE competitor Advanced Drainage grew wastewater sales **13.0%** in the year to 2026-03-31, so
   the evidence is moving the other way.
3. **The Plastics margin is price, not position.** **This is the one limb with a nameable
   falsifier, and here it is, as a pre-registered test:** *if, by the FY2028 10-K, the Plastics
   segment operating margin is still at or above 45% while **pounds sold have grown at least 15%
   above the 2020 base** and the price per pound has stopped falling, then a durable cost or
   distribution advantage exists that I could not see in the 2017-2020 record, and this limb is
   refuted.* **Every element is a figure Otter Tail already publishes annually.** As of the FY2025
   10-K the pounds index is **0.972** and the price has fallen three years running.

### THE MONITORING SERIES — and it is short, because the filer publishes exactly the right numbers

**[E4-17, E3-30]:** *is this erosion an aberrational cycle, or has the business slipped in a way
that permanently reduces intrinsic value?* The framework says beliefs change gradually, and
**[E4-55]** says where units exist, monitor units. Four lines, all annual, all in the MD&A:
1. **Pounds of PVC pipe sold, % change** — the honest series. 2020 = 1.000; now 0.972.
2. **Price per pound, % change** — −5%, −12%, −15% in 2023, 2024, 2025. **The reversion clock.**
3. **Plastics segment operating margin** — 60.9% → 58.7% → 54.7%. Pre-boom was **15.5-18.4%.**
4. **The allowed ROE granted in the pending Minnesota and South Dakota rate cases** — asked
   10.65% and 10.80%, last granted 9.48% and 8.75%. **This is the one number that decides what the
   $1,921 million of Electric capex is worth**, and it is [E5-40]'s ~12% test applied forward.

### THREE DATED CATALYSTS ALREADY ON THE CALENDAR

- **2026-12-31** — the date to which the DOJ moved, on 2026-07-01, to extend its discovery stay.
- **The MPUC final order in the Minnesota rate case** filed 2025-10-31, with interim rates in force
  since 2026-01-01 and **subject to refund**; likewise the SDPUC case filed 2025-06-04 with interim
  rates since 2025-12-01. **Both interim collections can be clawed back.**
- **The 2027 proxy statement** — the single most checkable prediction this file makes. For 2025 the
  company disclosed *"there were **no adjustments to GAAP results**"* for annual incentive awards
  and *"no adjustment to ROE"* for performance shares. **The Q2 2026 release created an Adjusted
  ROE that the company says runs 380 basis points above the GAAP figure. Whether that number
  reaches the pay calculation is the [E2-49] and [E4-27] test, and the answer arrives in about six
  months.**

### WHAT A REVERSAL WOULD NOT BE

**A lower price is not a reversal.** Q2 is a finding about the business, and **[E3-29]/[E5-35]**
govern: *"What you can't do is turn any investment into a good deal by paying little."* Q3 was
declared a **binary gate** on the daily-execution limb, which is the one place the corpus says
cheapness is ruled out as a remedy. **A cheaper Otter Tail is a cheaper capped utility with a
reverting commodity leg and an open criminal antitrust matter.**

- **Position size: NIL.** No position, no alert band, no `PORTFOLIO.md` row.
- **VERDICT: [x] OUT** *(carried from Q2; Q6 records the reversal conditions, it does not reopen
  the file)*

---
## SELF-AUDIT

- [x] **Questions answered in order; no verdict skipped.** Q1 IN → **Q2 OUT** → Q3, Q4, Q5, Q6
      written and each explicitly headed **RECORDED, NOT GOVERNING**, with Q5 headed
      **COMPUTATION — NOT A CLEARANCE** and carrying no entry language (operator rules 2 and 3).
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** The only IN in
      this file is **Q1**, and it rests on six 10-Ks, a 10-Q, a 10-K/A, three 8-K EX-99.1 releases
      and a proxy, all read, all with accession numbers. **The moat class is NOT held PROVISIONAL**
      — criterion 2 failed outright on the filer own sentence, and the unavailable private-peer
      cells are marked UNKNOWABLE with the reason, which cannot un-fail a failed criterion.
- [x] **Every UNRESEARCHED verdict names the artifact and where it lives.** Two, both sub-items
      rather than gate verdicts: (i) **the jurisdictional rate base in dollars** — OTP rate-case
      testimony and the commissions final orders, on the MPUC / NDPSC / SDPUC dockets, not EDGAR;
      (ii) **the three amended class complaints in No. 1:24-cv-07639 (N.D. Ill.), August 2025** —
      on PACER / CourtListener, and **court dockets are not a rung on this framework evidence
      ladder**, which is stated as the obstacle. The on-ladder substitute was used: **Atkore
      fuller account of the identical case in its own 10-K.**
- [x] **Every UNKNOWABLE states what specifically cannot be known.** Q3: whether the alleged PVC
      pipe information-exchange conduct occurred — no existing document resolves it and the
      settlements expressly do not. Q4/Q5: the sustainable level of Plastics earnings, hence of
      owner earnings; the band spans zero on the conservative construction in every window.
      The magnitude of the remaining antitrust tail: no filed figure bounds it and the company says
      so itself.
- [x] **Step 0: the filing was read, with accession numbers; figures cross-checked.** Three
      cross-checks, each on a number that drives a finding: **FY2025 net income $275,893** ties
      three ways (income statement, segment reconciliation 279,503 − 3,610, XBRL); **D&A $118,107**
      ties across the income statement, the cash-flow statement and the segment table; and the
      **share count** ties to the $5 par line ($209,928 thousand) with no treasury stock.
      **Plus the one that mattered most: the Plastics price/volume series cross-checked by two
      disjoint chains of the filer own percentages, agreeing to within 1%.**
- [x] **Owner earnings on a multi-year mean; windows stated; capex band disclosed as a judgment.**
      Five annual windows plus TTM plus an escrow-adjusted TTM, three (c) constructions, and the
      whole set repeated on two independent boom-normalisations — **thirty-nine cells**, every one
      shown. **[E5-20] applied per half with the ratios (Electric 3.00x, Manufacturing Platform
      0.61x) and the D&A end marked INVALID everywhere it appears.**
- [x] **Competitor row filled.** Two rows: six names in the PVC/plastic-pipe chain on a uniform
      GAAP operating-margin basis for seven years, and five utilities across fourteen
      jurisdictional allowed-ROE cells. Every comparability limit disclosed (fiscal-year
      mismatches, WLK impairments and segment mix, ATKR non-GAAP basis and impairment, NWPX cell
      unavailable, the four private/foreign filers).
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.** 5.34%, USD,
      US Treasury daily par yield curve, 2026-09-18. FRED not used.
- [x] **Value stated as a round-number range**, not a point estimate: ~$20-$40 at the floor,
      ~$35-$75 against the bare sovereign.
- [x] **One bar chosen, not both; windage count stated.** Screamer test only. Windage = **one**,
      shown alongside the unadjusted figures, with the one generous choice (Transmission excluded
      from (c)) disclosed in the same paragraph.
- [x] **Prices dated; aggregator used for live quotes only and flagged.** $87.42 at 2026-09-18 and
      $42.61 at 2020-12-31, both Yahoo via `tools/sources.py`, both flagged; the 2020 cap built
      split-invariantly (close at anchor × filed shares at measurement, no splits in ten years).
- [x] **`python tools/check_framework.py` PASSES** — run before each of the five commits.
- [x] **Run committed to git**, with a pathspec on every commit
      (`git commit -F <file> -- <paths>`), so no concurrent session staged work was swept in. JPM
      and TFC were running in this tree throughout.
- [x] **Operator rule 9 applied to myself.** I came into this run expecting the plastics collapse
      the brief described and **the competitor row refuted my prior**: Otter Tail has NOT given the
      windfall back while every listed peer has. **I wrote the case for the exception before I
      wrote the case against it**, and the thing that decided it was not the litigation — it was
      the filer own unit series, which shows the pounds are flat and the whole gain is price.

## REGISTER

- **Verdict: [x] OUT (about the business)** — at **Q2**.
- **One line:** **OTTR (Otter Tail Corporation), 2026-09-19 — FAIL at Q2, OUT ON THE BUSINESS.**
  Price **US$87.42**, close 2026-09-18; **41,985,580 shares** off the Q2 2026 10-Q cover, accession
  **0001466593-26-000071**; cap **US$3,670.4M**; sovereign **5.34%**. **No OTTR run file existed
  anywhere on disk — the PRE-RUN exclusion list was wrong.** Two businesses in one registrant: the
  Electric half fails **[E3-03] criterion 3** definitionally, with earnings-sharing clawbacks in
  two of three tariffs and **$1,921M** of 2026-30 capex against **$97.6M** of segment net income;
  the Plastics half fails **criterion 2** on the filer own sentence naming ductile iron, HDPE,
  steel and concrete, and its **54.7% operating margin against 15.5-18.4% in 2017-2020 is price,
  not position** — **pounds sold in 2025 are 2.8% BELOW 2020** while segment operating income is
  **6.1x**, price per pound **2.12x**, the 2021 trigger a Gulf Coast hurricane on the filer own
  account **[E3-51]**, and **every comparable listed participant has already surrendered the
  windfall** (Westlake **−14.1%**, Atkore **0.8%**, Olin **0.1%** consolidated GAAP operating
  margin in 2025). Management says the conditions *"gradually normalize through 2027."* The
  unexplained residual is the subject of **$103.5M of PVC pipe antitrust settlements charged to the
  Plastics segment in Q2 2026**, an **open DOJ grand jury subpoena** (stay extended to 2026-12-31),
  an unsettled **Canadian** class action and an unanswered **derivative demand** — **[E2-59]**: the
  moat belongs to the regime. Q3 **UNKNOWABLE** on the honesty binary, recorded not governing, with
  **[E2-49]** metric-switching firing exactly (the word "adjusted": **0** occurrences in the Q4
  2025 and Q1 2026 releases, **18** in the Q2 2026 release) and five findings in the company favour
  that promote nothing **[E2-37]**. Q4 **UNKNOWABLE**: owner earnings **−$163.0M to +$297.9M** as
  filed and **−$71.9M to +$164.9M** ex-boom, spanning zero, **all thirty-nine cells below the ~10%
  [E4-28] floor** including the invalid D&A cells; proposed shape **#27 THE CONVERTED WINDFALL**.
  Q5 below the gate: honest pre-tax expectancy **4.54% at best, 3.43% at the default window, 0.91%
  ex-boom — below the floor AND below the 5.34% sovereign**, which is rarer than a floor failure
  and is the sharpest single number in the file.
- **If UNKNOWABLE (Q3, Q4, Q5 — all recorded, not governing):** whether the alleged information-
  exchange conduct occurred; the sustainable level of Plastics earnings; the magnitude of the
  antitrust tail beyond the US settlement. None of the three is required to close the file, which
  closed on **[E3-03]** at Q2.

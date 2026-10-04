# Company Run — BLOOM ENERGY CORPORATION (BE) — 2026-09-12
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*Run opened 2026-09-12 by an agent killed by a model usage cap after stocking the research
folder but before Step 0 was written; resumed the same day with the research reads intact.
Sovereign, price and share count all re-struck on resumption per operator rule 5 — the
screen row's cap was a hand override **frozen at 2026-09-02** and is not used. Research
folder: `Test Runs/_research 2026-09-12 BE/` (filing dumps and `cache/` pattern-ignored).*

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
  from the issuing authority** (`daily_treasury_yield_curve`, struck 2026-09-12; the
  2026-09-12 print was not yet published at the time of reading, so 09/11 is the currently
  observed rate). The row read: `09/11/2026 … 20 Yr 5.38, 30 Yr 5.35`. **FRED DGS30 was not
  used.** Two other runs used 5.35% on 2026-09-11; this figure was read fresh from the
  Treasury CSV and not inherited.
- **Earnings currency: USD.** Bloom reports in US dollars, and the filing states the
  concentration directly: *"In the years ended December 31, 2025, 2024 and 2023, **total
  revenue in the U.S. was 81%, 74% and 70%**, respectively, of our total revenue"* (FY2025
  10-K, Note 2, Geographic Risk). The non-US remainder is *"primarily, the Republic of Korea,
  Japan, India and Taiwan … and several European countries"*, and the Korean volume runs
  through **dollar-denominated take-or-pay purchase commitments** with SK ecoplant under the
  Second Amended and Restated Preferred Distributor Agreement. Non-dollar cost exposure
  exists (the Korean JV, an India footprint) but it is an **exposure**, not a repricing of
  the earnings currency. **No FX conversion is needed and no ADR ratio applies** — BE is a
  Delaware corporation with a single class of common stock listed on the NYSE.
- **Share count and cap — the screen's cap was a HAND OVERRIDE frozen at 2026-09-02 and it
  is wrong.** Count read off the cover, not summed: **294,527,346 shares of Common Stock,
  $0.0001 par value, as of 2026-07-22**, from the cover of the **10-Q/A for the quarter ended
  2026-06-30, filed 2026-07-29, accession `0001628280-26-050325`** — *"The number of shares
  of the registrant's common stock outstanding as of July 22, 2026 was as follows: Common
  Stock, $0.0001 par value, 294,527,346 shares."* The same count appears on the cover of the
  original 10-Q (`0001628280-26-050247`). **The multi-class question is settled BY THE FILING
  and required no judgment to sum:** *"On May 27, 2026, the Company filed with the Delaware
  Secretary of State a Certificate of Second Amendment to its Restated Certificate of
  Incorporation which (among other things) **renamed its Class A common stock as common stock
  and eliminated outdated references to Class B common stock.** Prior to such amendment, the
  Company had 470,092,742 shares of Class B common stock authorized, but as of December 31,
  2025, **no such shares were issued or outstanding**"* (10-Q/A footnote 13). Preferred: *"There
  were no shares of preferred stock issued or outstanding as of June 30, 2026, and December
  31, 2025."* **One class, one count.** `cover_shares.py` returned exactly this and refused to
  sum, correctly — there was nothing to sum.
- **Price $275.75**, close of **2026-09-11** (aggregator, **flagged**, operator rule 5 —
  aggregators for live quotes only). **Cap = 294,527,346 × $275.75 = $81,216M.**
  **The screen row carried cap_m 63,995**, being the same share count at **$217.28 frozen at
  2026-09-02**. The price rose **26.9% in nine days** and the queue's cap is understated by
  **$17.2bn**. This is the **eighth** run to find the queue's cap wrong, and the first where
  the count was right and only the price was stale.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Form 10-K, FY ended 2025-12-31, filed 2026-02-09, accession `0001628280-26-006516`**,
  primary document `be-20251231.htm` — the anchor annual document. Read: Item 1 (business,
  the four revenue lines, manufacturing, customers, ITC and incentives), Item 1A risk
  factors, Item 7 MD&A (including the deferred-revenue-and-customer-deposit walk), the four
  statements, and Notes 2 (policies), 3 (revenue recognition, contract balances, deferred
  revenue roll-forward), 8 (outstanding loans and security agreements), 12 (commitments and
  contingencies), 15 (stock-based compensation), 17 (SK ecoplant / related party), 19
  (segment).
- **The full 10-K series FY2018 → FY2025, eight consecutive annual documents**, so that
  every owner-earnings window below rests on filed statements rather than on one vintage:
  FY2018 `0001664703-19-000008` (2019-03-22) · FY2019 `0001664703-20-000013` (2020-03-31) ·
  FY2020 `0001664703-21-000017` (2021-02-26) · FY2021 `0001664703-22-000034` (2022-02-25) ·
  FY2022 `0001628280-23-004301` (2023-02-21) · FY2023 `0001628280-24-005035` (2024-02-15) ·
  FY2024 `0001628280-25-008747` (2025-02-27) · FY2025 `0001628280-26-006516` (2026-02-09).
- **Form 10-Q, quarter ended 2026-06-30, filed 2026-07-28, accession `0001628280-26-050247`,
  and the Form 10-Q/A for the same quarter filed 2026-07-29, accession
  `0001628280-26-050325`** — **the current perimeter documents, and the location of this
  file's central finding.** Also read: 10-Q 2026-03-31 `0001628280-26-028021`, 10-Q
  2025-09-30 `0001628280-25-046844`, 10-Q 2025-06-30 `0001628280-25-037074`.
- **Form 424B4, IPO prospectus, filed 2018-07-26, accession `0001193125-18-227590`** — read
  for the pre-IPO going-concern and accumulated-deficit history, the original unit economics
  disclosure, and the **only vintage carrying a filed installed-base and cost-per-kilowatt
  series back to 2013**.
- **Fourteen Form 8-K exhibits**, every quarterly EX-99.1 from Q4 2024 to Q2 2026 plus the
  Q1 and Q2 2026 EX-99.2 supplemental financials — pulled **before** scoring `[E4-29]` and
  `[E4-22]`'s third flag, per the standing CGNX instruction. Full list at Q3.
- **Three DEF 14As**: 2024-03-26, 2025-04-02, 2026-04-08 — read for `[E4-52]` pay metrics.
- **Figure cross-checked against the filed statement:** *Net cash provided by operating
  activities*, FY2025 Consolidated Statements of Cash Flows, **$113,949 thousand** — agrees
  with XBRL `NetCashProvidedByUsedInOperatingActivities` 113,949,000 for FY2025. Checked at
  three more lines in the same statement: *Stock-based compensation expense* **$139,406**,
  *Purchase of property, plant and equipment* **$(56,759)**, *Depreciation and amortization*
  **$50,566**. And the line this file turns on, read off the statement itself rather than
  off a tag: *Deferred revenue and customer deposits* **$(142,605) / $139,868 / $(42,635)**
  for FY2025 / FY2024 / FY2023.
- *No ladder rung was blocked. Everything above is SEC EDGAR rung 2; the only aggregator
  input in the file is the live quote, flagged above.*

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Bloom builds a box. The box is a
stack of solid-oxide ceramic fuel cells that oxidises natural gas (or hydrogen, or biogas)
electrochemically instead of burning it, and produces direct current on the customer's own
land, behind the meter, without a turbine and without a grid connection. It sells the box
outright, at a price per kilowatt of nameplate capacity. It then sells four separate things
off the same installed box, and **the filing breaks all four out, with a matched cost line
for each**:

1. **Product** — the box itself, sold to a buyer who is usually **not the end user of the
   power**: a financier, a distributor, or a project-finance affiliate. Revenue is recognised
   on customer acceptance.
2. **Installation** — putting the box on the pad, connecting gas and wiring. Optional to the
   customer; often done by the customer or a local contractor instead.
3. **Service** — an annual operations-and-maintenance contract that, crucially, **replaces the
   fuel-cell stacks as they degrade**. Billed *"generally received at the beginning of each
   service year"* and renewable annually at the customer's option. This is the line the bull
   case calls the annuity.
4. **Electricity** — Bloom (or a vehicle it consolidates) owns the box and sells the output
   under a PPA or a capacity payment.

**So the money is made three ways and one of them is not a business.** The box is sold at a
gross margin; the stack replacement is sold as a subscription; the electricity is sold as a
utility. Installation is a pass-through that Bloom has never once sold at a profit.

**THE FOUR LINES, FILED, EVERY YEAR OF THE LISTED LIFE** — revenue and its own matched cost
of revenue, from the Consolidated Statements of Operations of the FY2020, FY2022 and FY2025
10-Ks and the Q2 2026 10-Q. **Gross margin by line, in per cent:**

| year | product | installation | service | electricity | total | revenue $m |
|---|---|---|---|---|---|---|
| 2018 | 29.8 | **−39.8** | **−20.9** | 38.4 | 16.7 | 632.6 |
| 2019 | 21.9 | **−25.7** | **−4.6** | **−5.8** | 12.4 | 785.2 |
| 2020 | 35.8 | **−14.4** | **−20.7** | 26.9 | 20.9 | 794.2 |
| 2021 | 28.9 | **−14.7** | **−2.8** | 35.0 | 20.3 | 972.2 |
| 2022 | 30.0 | **−13.0** | **−11.6** | **−115.0** | 12.4 | 1,199.1 |
| 2023 | 35.4 | **−13.9** | **−20.7** | **−117.2** | 14.8 | 1,333.5 |
| 2024 | 36.8 | **−5.8** | **−0.7** | 26.3 | 27.5 | 1,473.9 |
| 2025 | 35.2 | **−0.9** | **+10.0** | 46.3 | 29.0 | 2,024.0 |
| H1 2026 | 35.6 | **−14.3** | **+16.1** | 27.5 | 32.0 | 1,816.4 |

**THE ANNUITY LOST MONEY FOR SEVEN OF ITS FIRST EIGHT YEARS.** The service line — the
long-dated, contractually recurring, automatically renewing line that every bull case for
this company describes as the razor-blade — carried a **negative** gross margin in 2018,
2019, 2020, 2021, 2022, 2023 and 2024, and first turned positive in **2025, at 10.0%**. The
brief predicted the AMAT shape and the filing delivers it **more severely than at AMAT**:
Applied Materials' service line earned 33.4% against a 54.2% product margin, a ratio of
0.62. **Bloom's most recent quarter is Service 18.7% against Product 36.5% — a ratio of
0.51 — and Bloom's own EX-99.2 supplemental prints both numbers side by side** (Q2 2026
supplemental, 2026-07-28, accession `0001628280-26-050150`, slide 18). **The recurring line
is the WORST of the three real businesses, not the best.** It is a stack-replacement
obligation sold at cost, and for seven years below cost.

**The reason is mechanical and the filing says it: the service contract is a warranty on a
consumable.** *"Cost of service revenue consists of costs incurred under maintenance service
contracts for all customers … and extended maintenance-related **product repair and
replacement costs**"* (FY2022 10-K). Bloom has *"increased the life of our fuel cells by over
two and half times"* since the first generation (FY2025 10-K, R&D) — which is exactly why the
margin finally turned: **the annuity is only profitable to the extent the product stops
needing the annuity.** The two lines are in direct economic opposition.

**THE UNIT SERIES — [E4-55] RUN, AND THE ANSWER IS THE OPPOSITE OF THE BULL CASE.** *"Where
units exist, monitor units … Dollar revenue flattered by pricing is how a shrinking franchise
hides; the physical series is the honest one."* Bloom filed a real physical series — product
accepted in 100-kilowatt equivalents, megawatts accepted net, **product cost per kilowatt**
and installation cost per kilowatt — in the MD&A Key Operating Metrics of every 10-K from
FY2018 to FY2023. Set against the filed product revenue and product cost of revenue for the
same years:

| year | MW accepted | product rev / kW | cost of product rev / kW | **filed product cost / kW** | **gross $ / kW** |
|---|---|---|---|---|---|
| 2016 | — | — | — | **$4,457** | — |
| 2017 | 62.2 | — | — | **$3,292** | — |
| 2018 | 80.9 | $4,952 | $3,477 | **$3,372** | **$1,475** |
| 2019 | 119.4 | $4,668 | $3,647 | **$2,881** | **$1,021** |
| 2020 | 132.6 | $3,911 | $2,509 | **$2,368** | **$1,402** |
| 2021 | 188.0 | $3,529 | $2,509 | **$2,346** | **$1,021** |
| 2022 | 228.0 | $3,863 | $2,703 | **$2,453** | **$1,160** |
| 2023 | 268.0 | $3,639 | $2,351 | **$2,108** | **$1,288** |
| 2024 | **not filed** | — | — | **METRIC DISCARDED** | — |
| 2025 | **not filed** | — | — | **METRIC DISCARDED** | — |

*The reconstruction reconciles to the filing to within $2/kW, which is the check that the
series is being read correctly: FY2023 filed product cost $2,108/kW plus period manufacturing
costs not in product cost $64,892k ÷ 268MW = $242/kW gives $2,350/kW against $2,351/kW
computed from the income statement; FY2022 gives $2,701 against $2,703.*

**[E2-44], both halves, answered from the filed series — and the answer is that the cost
curve was handed to the customer.** Product cost per kilowatt fell **$1,264** between 2018
and 2023 ($3,372 → $2,108, −37.5%). Product **price** per kilowatt fell **$1,313** over the
same six years ($4,952 → $3,639, −26.5%). **The customer took 104% of the cost reduction.**
Gross profit per kilowatt — the number that decides whether a cost curve is an owner's asset
— went $1,475 → $1,021 → $1,402 → $1,021 → $1,160 → $1,288. **The best year in the series is
the first one.** Six years of engineering, automation and scale produced **less** gross profit
per kilowatt in 2023 than in 2018.

This is **[E3-62]**'s second step, worked: *"none ever asks how much is going to stay home and
how much is just going to flow through to the customer"* — and the filed answer is that it
flowed through, which is the textile-loom outcome, *"Nothing was going to stick to our ribs as
owners."* On the first test [E2-44] asks — can it raise prices when demand is flat and capacity
is not fully utilised — the filed record through 2023 is **no, it cut them 26.5%.**

**AND THE SERIES WAS THEN DELETED.** The FY2024 10-K removed all four unit metrics, in the
company's own words: *"We have determined that the foregoing metrics **no longer reflect key
operating metrics** of the company and therefore **we will no longer report on these metrics**
in our reports … our Energy Server product (electricity-only power module) cost is becoming a
widely varying portion of the overall value of the energy solution we provide, and **trends in
costs and selling prices per kilowatt are less representative** of our overall business
performance … These factors can **distort the cost or revenue per kilowatt metrics**.
Management relies primarily on revenue, **non-GAAP gross and operating margins**, as well as
cash flows from operating activities to manage operations."* **This is scored at Q3 under
[E2-49], where it belongs; recorded here because it is the reason the table above stops.**

**The scarce input this business controls.** Not gas, which anyone can buy. Not the grid,
which it deliberately avoids. **It is the ceramic electrolyte and the stack manufacturing
process** — *"complex applied materials, processing and packaging challenges … many
proprietary advanced material science solutions … as of December 31, 2025, includes **62 PhDs**"*
(FY2025 10-K) — plus, at this moment and not durably, **installed megawatts of manufacturing
capacity that can be delivered in months rather than years**: ~1 GW at Fremont, *"plans to
double the Fremont facility's annual production capacity from approximately 1 GW to 2 GW by
the end of 2026."* The scarce input the CUSTOMER is buying is not the fuel cell. It is
**time** — electrons on a data-centre pad before an interconnection queue clears. Whether
that is Bloom's scarce input or the grid operator's temporary failure is the whole of Q2.

**A perimeter fact that has to sit at Q1, because it changes what "makes money" means.** In
FY2025, **$862.1 million of revenue — $809.8M product and $52.3M installation, 42.6% of total
revenue — was recognised on sales of Energy Server systems to the "Fund JVs"**, joint ventures
Bloom itself co-created with Brookfield Asset Management in August 2025 and in which Bloom
holds **9.9%, 9.9% and 15.0%** passive equity interests, accounted for under the equity method
(FY2025 10-K Note 7 and Note 12). Total related-party revenue FY2025: **$892.0M = 44.1%** of
revenue, against $338.6M (23.0%) in FY2024 and $487.2M (36.5%) in FY2023. Bloom's own share of
the profit on those sales was eliminated — that is the whole of the **$40.4M "equity in loss of
unconsolidated affiliates"**: *"all of which related to intra-entity profit from sale of assets
eliminated in accordance with ASC 323."*

**This is understandable, and it is not circular.** Brookfield, not Bloom, is the primary
beneficiary and supplies the capital — *"a prospective financing framework structure … of up
to **$5.0 billion over five years**"*, housed in *"an AI Infrastructure Fund created by
Brookfield"* — Bloom's **maximum exposure to loss is $45.7M** and *"The Fund JVs' creditors do
not have recourse to our general credit."* Bloom put in $36.5M of equity and sold $862M of
product into the structure. **The 42.6% is third-party project finance wearing a related-party
label, not revenue Bloom funded.** But it must be named, because Bloom also **changed the
definition of "customer" in the FY2025 concentration note to accommodate it**: *"'customer'
refers to the contractual counterparty to which we sell our products … which in certain
transactions **may be a project-finance affiliate rather than the ultimate end user**."*

**Will the fundamentals look broadly the same in ten years?** The **product** will: a box that
converts a hydrocarbon to electricity at a site, sold at a price per kilowatt against a cost
per kilowatt, is as stable a unit economic as exists. The **demand** will not, and the filing
does not pretend otherwise — 2026 revenue is guided to roughly double on AI data-centre orders
that did not exist in 2023, and the risk-factor list includes *"any actual or perceived
slowdown in the adoption of AI resulting in a slower expansion of AI data centers"* and *"the
availability of rebates, tax credits and other tax benefits."* **Q1 does not require the
demand to be predictable; it requires the money-making mechanism to be understandable, and it
is.** Where the ten-year question bites is Q2 (is the advantage ownable) and Q4 (does it
survive the order book reversing), and both are taken there.

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____

*IN, and narrowly. Four filed revenue lines with four matched cost lines, a physical unit
series for six years, a reconciled cost-per-kilowatt build, and a fully disclosed
project-finance perimeter. The business is legible. What the legibility reveals is adverse —
the recurring line is the worst line, and the cost curve went to the customer — but that is a
Q2 finding, not a failure to understand. **The one thing I cannot compute is the 2024–2026
unit series, because the registrant stopped filing it**; that is not UNRESEARCHED, because no
document exists that would resolve it (no 8-K, no supplemental, no deck carries megawatts
accepted or cost per kilowatt for 2024 or 2025 — the fourteen exhibits on disk were checked).
It is scored where it belongs: as a **[E2-49] metric-switching flag at Q3** and as the reason
the Q2 moat metric has no current reading.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

### THE BULL CASE, BUILT AT FULL STRENGTH FIRST — because [E4-51] requires it
*"I'm not entitled to have an opinion unless I can state the arguments against my position
better than the people who are in opposition."* The brief asked for this and it deserves it,
because **this is the strongest bull case any name in this queue has presented.**

1. **The customer's alternative has a four-to-seven-year lead time and Bloom's has months.**
   This is not Bloom's claim alone; it is the industry's. FuelCell Energy's own FY2025 10-K:
   *"Our ability to rapidly deploy modular, high-density fuel cell systems could enable data
   centers to bring multi-megawatt capacity online **in months** (once all permits are
   secured), compared to **3–7 years** for traditional utility or gas turbine solutions"* and
   *"Gas turbine queues: Large-scale behind-the-meter generation faces 3–5-year procurement
   and construction timelines due to equipment shortages and supply chain bottlenecks"*
   (accession `0001104659-25-122302`). A data centre earning hundreds of millions a year per
   hundred megawatts will pay almost anything for four years of time.
2. **The filed numbers have turned, hard, and they are audited.** H1 2026 revenue $1,816.4M
   against $727.3M (+150%); product revenue $1,588.8M against $508.5M (+212%); **GAAP
   operating income $254.4M against a $22.6M loss; GAAP net income $272.5M.** Not a one-off
   gain — the Q2 2026 income statement shows it arriving through operating income.
3. **The customer's capital constraint has been removed by a third party.** Brookfield
   Asset Management: *"a prospective financing framework structure … of up to **$5.0 billion
   over five years** … housed in an AI Infrastructure Fund created by Brookfield"* (FY2025
   10-K Note 7). Bloom contributes only 9.9% passive equity and *"The Fund JVs' creditors do
   not have recourse to our general credit."*
4. **The balance sheet is now a fortress, not a liability.** $2,666.9M of cash at 2026-06-30
   against $2,530.3M of total debt principal — **net cash** — and the debt is **$2.5bn of
   ZERO-coupon convertible notes due November 2030.**
5. **The technology barrier is real and is demonstrated by the failure of everyone else.**
   The two pure-play comparables both lose money at the gross line: FuelCell Energy's FY2025
   gross margin is **−16.7%** and Plug Power's **−34.1%**. Bloom's is **+29.0%**. Twenty-three
   years and $5.3bn of contributed capital bought something they do not have.
6. **The subsidy came back.** *"Under the OBBBA, fuel cell property is now eligible for a 30%
   ITC under Section 48E **without regard to emissions** for projects beginning construction
   after December"* 2025 (FY2025 10-K) — after the 50% §48(a) credit had expired 2024-12-31.
7. **Management's claim, which is a claim and not evidence, is total adoption:** *"all the
   major US hyperscalers and over a dozen US neoclouds, AI labs, and colocation data center
   operators have validated and approved our power solutions for their AI factories. **Bloom
   is now a standard for AI onsite power**"* (Q2 2026 EX-99.1, 2026-07-28).

**That case is strong on demand and on the balance sheet. It fails as a FRANCHISE claim, and
what fails it is the registrant's own disclosure.**

### THE THREE CRITERIA [E3-03]
- **Needed or desired — [x] YES, emphatically.** No argument. The demand is documented by
  every filer in the sector.
- **No close substitute — [ ] NO. FAILED, ON BLOOM'S OWN WORDS.** The FY2025 10-K's own
  *"Energy Server Systems Competition"* section names the substitutes and then concedes
  functional equivalence: *"We primarily compete against alternative sources of electricity
  generation which provide firm, always on power. In addition to power provided by
  **centralized utility grids** … we primarily compete against OEMs providing onsite firm
  resources which are: **Gas reciprocating engines** … **Small gas turbines** … **Combined
  cycle plants** … The Bloom Energy Server system **can achieve similar efficiencies as
  combined cycle plants** after accounting for the transmission and distribution losses for
  onsite deployment."* Three named close substitutes plus the grid, and a stated parity on
  efficiency. **And then the registrant locates its own advantage, in its own words, not in
  the product but in the queue:** *"due to its **relative ease in permitting and
  installation** compared to the above mentioned products, the Energy Server can be deployed
  rapidly, **giving us a competitive advantage when customers have an urgent need for
  power**."*
- **Not price-regulated — [x] technically yes, but [E2-59] governs and it cuts the other
  way.** *"Although we generally are not regulated as a utility, existing and future federal,
  state, international and local government statutes and regulations concerning electricity
  **heavily influence the market** for our products"* (FY2025 10-K). The Investment Tax Credit
  went **50% → 0% → 30% in twenty-four months**: the §48(a) *"investment tax credit … of up to
  50% for fuel cells … **expired on December 31, 2024**"*; nothing in 2025 except
  safe-harboured projects; §48E at 30% restored by the OBBBA of 2025-07-04 for construction
  beginning after 2025-12-31. **[E2-59] is exact about what that means:** administered pricing
  *"can legally price their way to profitability even in the face of substantial
  over-capacity"* — but *"the moat belongs to the **regime**"*, and *"That day is gone"* is how
  it ends. A 30% credit on tax basis is the difference between the product clearing and not
  clearing against a gas engine, and Congress owns it, not Bloom.

### THE SURFING RUN — [E3-51], AND IT IS THE WHOLE OF THIS FILE'S Q2
*"when a surfer gets up and catches the wave and just stays there, he can go a long, long
time. But if he gets off the wave, he becomes mired in shallows … **A surfing run is not a
moat; the advantage lives in the wave, not the surfer.**"* Bloom's own stated advantage is
**permitting speed against an interconnection queue** — that is, against a temporary failure
of somebody else's asset. Ask **[E4-36]**'s question, which of the four causes of extreme
success this record comes from, *"because only some of them are ownable"*: this is
**wave-riding**. The grid's four-to-seven-year queue is not Bloom's property, is not
defensible by Bloom, and is being attacked by every turbine and genset maker named below with
balance sheets ten to thirty times Bloom's.

### THE PRIMARY MOAT METRIC, FILING-SOURCED, AND ITS TREND — AND IT IS FLAT
Two readings, both from the filings, both adverse:

**(a) Gross profit per kilowatt of product accepted, 2018–2023** (the physical metric
[E4-55] demands, built at Q1 above): **$1,475 → $1,021 → $1,402 → $1,021 → $1,160 →
$1,288.** The best year is the first. Price per kW fell $1,313 while cost per kW fell $1,264
— **the customer took 104% of the cost curve.** That is [E3-62]'s second step answered
against the owner, and [E2-44]'s first half — can it raise prices when demand is flat —
answered **no, it cut them 26.5%.**

**(b) PRODUCT gross margin across the AI demand shock — the reading that does not need the
deleted metric, and it is the decisive one:** **35.4% (2023) · 36.8% (2024) · 35.2% (2025) ·
35.6% (H1 2026) · 36.5% (Q2 2026).** **Revenue tripled and the product gross margin did not
move.** A business with pricing power inside a generational shortage of its product expands
its product margin. Bloom's is flat within 1.3 points across four years. The *total* gross
margin did rise, 14.8% → 32.0%, and **every point of that rise is mix and the absence of
impairments**, not price: the loss-making service, installation and electricity lines shrank
from 26.9% of revenue in 2023 to 12.5% in H1 2026, and the $130.1M (2023) and $115.3M (2022)
PPA impairments dropped out of cost of revenue. **The margin expansion the bull case cites is
arithmetic, not pricing.**

**[E4-32] direction outranks existence.** On both metrics the direction is **flat to down**.

### **[E4-04]** — must the moat be continuously rebuilt?
**Yes, and it is the excluded kind.** Apply the framework's own test: *"does a lapse in
spending destroy the structure, or merely narrow it — and does the spending defend the same
advantage, or **buy its replacement**?"* Bloom's advantage is a cost-per-kilowatt curve that
must be cut every year to stay ahead of gas turbines whose cost curve is also falling, plus
manufacturing capacity that must be doubled to serve the current order book ($200M Fremont,
*"plans to double … from approximately 1 GW to 2 GW by the end of 2026"*). R&D ran $186.0M in
2025 and $115.7M in H1 2026 alone. **The spending buys the replacement, not the defence of the
same advantage** — the Mitsui/Rhodes-Ridge side of the test, not the Coca-Cola side. And
**[E4-47]** compounds it: an asset-heavy filer in a high-cost-of-capital environment.

### **Does success depend on a great manager? — recorded HERE as a Q2 moat defect [E4-23]**
KR Sridhar founded the company in 2001, is Chairman and CEO, and is the author of the
technology and of every strategic pivot (Korea, hydrogen, electrolyzers, AI data centres).
*"if a business requires a superstar to produce great results, **the business itself cannot be
deemed great**… The partnership's moat will go when the surgeon goes."* Recorded at Q2 as
instructed, **not** at Q3 as a strength.

### THE COMPETITOR ROW — required **[E3-28]**
**Same metric, same window, filing-sourced.** Each company's own most recent completed fiscal
year. Gross margin from the filed income statement; owner earnings on this framework's
convention (operating cash flow less stock compensation less capital expenditure, the
**capex** end of (c)), in $ millions, from each filer's own XBRL cross-checked to form type.

| Company | FY end | gross margin | **owner earnings, capex end ($m)** | **does it name Bloom Energy?** | source |
|---|---|---|---|---|---|
| **BLOOM ENERGY (BE)** | 2025-12-31 | **29.0%** | **−82** | — | 10-K `0001628280-26-006516` |
| Caterpillar (CAT) | 2025-12-31 | **33.8%** | **+8,676** | **NO** — zero occurrences of "Bloom"; zero of "fuel cell" | 10-K `0000018230-26-000008` |
| Generac (GNRC) | 2025-12-31 | **38.3%** | **+218** | **NO** — "fuel cells" once, as a watch item | 10-K `0001437749-26-004568` |
| Cummins (CMI) | 2025-12-31 | **25.3%** | **+2,293** | **NO** — the one "Bloom" hit is *Bloomberg* in the pension note | 10-K `0000026172-26-000009` |
| GE Vernova (GEV) | 2025-12-31 | **19.8%** | **+3,453** | **NO** — zero "fuel cell", zero "solid oxide" | 10-K `0001996810-26-000015` |
| FuelCell Energy (FCEL) | 2025-10-31 | **−16.7%** | **−155** | **YES — once, to say it REMOVED Bloom** | 10-K `0001104659-25-122302` |
| Plug Power (PLUG) | 2025-12-31 | **−34.1%** | **−698** | **NO** — zero "Bloom", zero "solid oxide" | 10-K `0001104659-26-022286` |
| Ballard (BLDP) | 2025-12-31 | **form-limited, see below** | **not computable on this shelf** | **NO** | **Form 40-F** `0001628280-26-017045` |

**BLDP — the form, stated as the brief required.** Ballard files a **Form 40-F**, not a 10-K
and not a 20-F: *"The Company is a Canadian issuer eligible to file its annual report pursuant
to Section 13 of the … Exchange Act on Form 40-F. The Company is a 'foreign private issuer' as
defined in Rule 3b-4."* It reports under **IFRS, not US GAAP** — *"prepared … in accordance
with International Financial Reporting Standards ('IFRS') as issued by the International
Accounting Standards Board"* — with **no US-GAAP reconciliation** under the MJDS route, and the
40-F is a thin cover incorporating the Annual Information Form, the audited statements and the
MD&A by reference. **Its figures are therefore not the same metric** and are not placed in the
row: an IFRS gross margin and an IFRS-16 cash-flow statement are a different measurement, and
forcing them into a US-GAAP row would be the error the row exists to prevent. 300,784,816
common shares at 2025-12-31.

**Wärtsilä and Siemens Energy — the limit stated, as required.** Neither files an SEC annual
report. Under this queue's own standing ruling on non-SEC registrants the correct verdict for
their figures is **UNKNOWABLE, not UNRESEARCHED** — no document exists on this project's
citation shelf that would resolve them. They appear in the row only as **named by the peers**:
Caterpillar names *"Rolls-Royce Power Systems AG and Siemens Energy AG"*; GE Vernova names
*"Siemens Energy, Mitsubishi Power, Westinghouse, Framatome, and Rolls-Royce."*

- **Peers named: 7 of roughly 12 real competitors in on-site firm power.** The full set named
  across the peer filings themselves is Caterpillar, Cummins, Generac, GE Vernova,
  Rolls-Royce/MTU, Siemens Energy, Mitsubishi Power, Rehlko (Kohler), INNIO, Deutz, Weichai,
  plus the two pure-plays FCEL and PLUG. I took every SEC annual filer and named the five that
  are not.
- **Why the missing five do NOT make this moat class PROVISIONAL.** The framework holds a moat
  class PROVISIONAL where peer data is unavailable — **and that rule exists to stop a moat
  being CLAIMED on an incomplete row.** Here the row is being used to **deny** one, and the
  five missing names are all larger, better-capitalised turbine and engine makers whose
  absence can only make Bloom's relative position worse, never better. The class below is
  determined by Bloom's own filings; the row corroborates and does not carry it.

**WHAT THE ROW SHOWS, AND IT IS AN ASYMMETRY.**
1. **Bloom's gross margin is in the MIDDLE of the incumbent pack, not above it. Generac — a
   genset packager that buys engines and bolts them to alternators — earns 38.3%, nine points
   MORE than Bloom's 29.0%, and Caterpillar earns 33.8%.** A twenty-three-year proprietary
   materials-science platform with 62 PhDs earns a lower gross margin than the companies
   assembling commodity hardware. That is the single hardest fact in the row against the moat
   claim, and it is not a cyclical reading: Bloom's 29.0% is its **best year ever**.
2. **Bloom is invisible in the competitive self-description of every incumbent.** CAT, CMI and
   GNRC name each other reciprocally — a closed, mutually-acknowledged oligopoly — and none
   lists Bloom. GEV's named set is turbines and grid gear. Both CAT and GNRC describe **the
   same opportunity Bloom sells into** while naming no fuel-cell firm: CAT — *"we are starting
   to see orders for **prime power** trend higher as **data center customers look for
   alternative power solutions** to keep pace with their growth"*; GNRC — *"Our C&I BESS
   solutions are primarily targeted at **'behind-the-meter'** applications."* **[E3-61] caps
   what this can mean:** the row shows position, not conduct, and a competitor's Item 1 naming
   practice reflects materiality thresholds as much as market reality. Two readings are live
   and this file cannot settle which — Bloom is too small to appear, or the incumbents do not
   yet compete for the same socket. **Neither reading supplies a moat.**
3. **The one firm that engages Bloom's architecture attacks it on the merits and demotes it.**
   FuelCell Energy: *"Compared to **solid oxide** and PEM fuel cells, we believe that our
   carbonate fuel cells demonstrate **longer stack life**, robust biogas operation, **minimal
   performance derate**, and advanced contaminant management"* — the stack-life attack is
   aimed precisely at the line that made Bloom's service margin negative for seven years. And
   in the same document: *"In updating our 2024 Peer Group to create our 2025 Peer Group …
   **Bloom Energy Corporation** and Altus Power, Inc. **were removed**."* FCEL retained Ballard
   and Plug and dropped Bloom — it no longer regards Bloom as a comparable.

### **Untapped pricing power — [E3-33]**
**No, and the claim is not available.** [E5-28] scopes the class: *"If you name some business
that has incredible pricing power, you're talking about a business that's **a monopoly or a
near monopoly**"* — and the competitor row above does not support near-monopoly in on-site firm
power. More directly: a manager **could not** raise the return by raising prices, because the
filed record is that Bloom **cut** price per kilowatt 26.5% between 2018 and 2023, and then held
product gross margin flat at ~35-36% through the largest demand shock in the history of
distributed generation. **The one moment in twenty-three years when Bloom had the leverage to
take price, it did not take it.** That is the [E3-33] test failed from the other direction.

### **Customer concentration — filed percentages, across vintages**
| year | top counterparties, % of total revenue | related-party revenue |
|---|---|---|
| 2022 | **38% + 37% = 75%** in two | — |
| 2023 | **37% (related party) + 26% = 63%** in two | $487.2M = 36.5% |
| 2024 | **23% (related party) + 16% + 14% = 53%** in three | $338.6M = 23.0% |
| 2025 | **43% (related party) + 13% + 12% = 68%** in three | **$892.0M = 44.1%** |

**AND THE MOST RECENT QUARTER IS THE WORST CONCENTRATION IN THIS QUEUE: ONE CUSTOMER WAS 73%
OF REVENUE.** This is why the **10-Q/A of 2026-07-29** exists, one day after the 10-Q. Its
Explanatory Note, verbatim: *"The purpose of this amendment … is to address **a transposition
of references to 'six months' and 'three months'** in the Form 10-Q under Item 1 – Financial
Statements, Note 1 … Concentration of Risk – Customer Risk."* The corrected paragraph: *"During
the six months ended June 30, 2026, revenue from two customers, the second of which is our
related party … accounted for approximately **44% and 21%** of our total revenue. **During the
three months ended June 30, 2026, revenue from one customer, which is not our related party,
accounted for approximately 73% of our total revenue.**"* **73% of $1,065.4M = roughly $778M
of one quarter's revenue from a single unnamed non-related counterparty.** *(The amendment
itself is a candor point in Bloom's favour and is scored as one at Q3 under [E2-69] — the
error understated the single-quarter concentration and Bloom corrected it unprompted within 24
hours. The FACT it corrected to is the Q2 finding.)*

*(FY2023–FY2025 10-Ks, Note 1, Concentration of Risk — Customer Risk.)* **SK ecoplant was the
related party from 2023-09-23 and ceased to be one on 2025-07-10** when it sold 10,000,000
shares and fell to 5.8%; it sold 2,608,000 more on 2025-08-14 and 3,912,000 on 2025-09-29, and
held **2.5% at 2025-12-31.** **The take-or-pay partner sold down 70% of its stake in the year
Bloom's order book exploded.** That is a filed fact about the counterparty's own view and it
belongs in the Q2 read. The 43% counterparty in 2025 is the **Brookfield Fund JVs**, and Bloom
changed the definition of "customer" in the note to accommodate it: *"'customer' refers to the
contractual counterparty … which in certain transactions **may be a project-finance affiliate
rather than the ultimate end user**."* Concentration is **not** improving: 2025 is worse than
2024 on every reading.

### **The contracted order book, since the bull case rests on it — and it is small**
**Bloom discloses no backlog figure at all.** What it does disclose, at 2026-06-30, is
unsatisfied performance obligations of **$442.4M** (product and installation, *"within the next
1 to 2 years"*) plus **$51.7M** (service, over 1 to 25 years) = **$494.1M of contracted,
filed obligations** — against FY2026 revenue guidance of **$3.9–4.2bn.** The AEP *"1 GW supply
framework agreement"* and the Brookfield *"up to $5.0 billion over five years"* are
**frameworks subject to conditions**, not performance obligations: the Brookfield structure
covers *"future Bloom Energy fuel cell projects that **meet certain investment criteria and
contractual criteria or are otherwise approved by Brookfield**"*, with *"periodic review by
Brookfield of Bloom's fuel cell project pipeline."* **This is the ORCL shape in miniature and
it must be said plainly: roughly 87% of guided 2026 revenue is not in a filed performance
obligation.** It may well arrive. It is not contracted in the filings.

- **Class: [ ] WIDE  [ ] NARROW  [x] NONE  [ ] PROVISIONAL**
  · **Direction: FLAT on product gross margin (35.4% → 36.5% across a tripling of revenue),
  DOWN on gross profit per kilowatt (peak 2018), and the physical metric was withdrawn.**
- **VERDICT: [ ] IN  [x] OUT**  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____

**⛔ Q2 OUT CLOSES THE FILE. The reason, in one paragraph, and every element of it is the
registrant's own disclosure.** [E3-03] criterion (2) fails because Bloom's own competition
section names three close substitutes and concedes efficiency parity with one of them, then
locates its advantage in **permitting speed against somebody else's interconnection queue** —
which [E3-51] calls a wave and not a moat, and [E4-36] calls the one cause of extreme success
that is **not ownable**. [E2-44] and [E3-62] fail because Bloom's own six-year unit series
shows the customer taking 104% of the cost curve, and its own income statement shows product
gross margin **flat at 35–36% while revenue tripled** — the single moment it had the leverage
to take price and did not. [E4-04] fails because the spending buys the advantage's replacement
rather than defending the same advantage. And the competitor row's hardest fact is that
**Generac, a genset packager, earns a nine-point higher gross margin than Bloom's best year
ever.** *This is an OUT about the FRANCHISE, not about survival — the balance sheet is net cash
and Q4 below shows why. Under [E2-28]/[E4-17] the reversal condition is recorded in words at
Q6, and per the QLYS ruling of 2026-09-07 **no price alert is armed on a name that failed on
the business.***

---
# ⛔ EVERYTHING BELOW THIS LINE IS RECORDED BELOW THE GATE
**Q2 returned OUT and closed the file.** Q3 and Q4 below were commissioned by the brief and are
recorded because they are **findings about the business**, which the framework wants written
down. **No verdict below is a clearance**, none of them can reopen Q2, and Q5 carries the
heading operator rule 3 requires. They are here because the brief pre-registered specific
hypotheses about [E5-11], the ORCL and ARM comparison, and the deposit line, and a brief's
hypotheses must be answered whether or not the gate they were aimed at was reached — otherwise
the run gets to choose which of its own predictions it grades.

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?  ·  **RECORDED BELOW THE GATE**
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**None ticked → Q3 is a qualitative OVERLAY.** Record findings; manager quality alone does
not stop the run. **Any ticked → Q3 is a BINARY GATE and no price compensates.**

**Case declared: [x] DAILY EXECUTION. Q3 IS A BINARY GATE.** Bloom is a
have-to-be-smart-every-day business on all three of [E3-38]'s tests and the 1977 root
**[E2-70]** applies almost literally. Product revenue is recognised **on customer acceptance
of a physical installation** — 2,682 separate acceptances in the last year they counted them —
each requiring a site, a gas connection, a permit, a crane and a signature; a manufacturing
line being doubled from 1 GW to 2 GW; a 20-plus-year O&M obligation on every box ever shipped,
with stack-replacement cost estimated at contract inception; and a revenue-recognition policy
the auditor has designated a **critical audit matter for six consecutive years** precisely
because *"the timing of product revenue recognition (i.e., customer acceptance)"* requires
*"the degree of auditor judgment."* Nothing here is a have-to-be-smart-once asset. **Leverage
is NOT ticked** (net cash, zero-coupon debt — see Q4) and **control is not applicable**.
**Because daily execution is ticked, no price compensates for a Q3 failure — and Q3 does not
fail. It fires six flags and none of them is a conduct finding.**

**Honesty — binary, permanent, filings-based [E5-16].** *"understanding about business
mistakes; tolerance for personal misconduct is zero."* Each matter dated to when it became
PUBLIC, so the test stays point-in-time honest.

**NO DISQUALIFIER FOUND.** Read for it across eight 10-Ks, five 10-Qs, three DEF 14As and the
424B4: **no SEC enforcement action, no restatement after 2020, no executive misconduct matter,
no auditor disagreement, no late filing, and — checked explicitly because the brief asked —
NO GOING-CONCERN QUALIFICATION AND NO "SUBSTANTIAL DOUBT" LANGUAGE IN ANY VINTAGE, INCLUDING
THE 424B4.** Zero occurrences of either phrase in the 2018 IPO prospectus, the FY2018 10-K,
the FY2019 10-K (the restatement year), the FY2020, FY2023 or FY2025 10-Ks. *This refutes a
reasonable prior. A company that reached its IPO with an accumulated deficit of $2.3 billion
and burned cash for a further seven years never received one.*

**One dated accounting matter, and it is the flag below, not a conduct finding.** Became
public **2020-03-31** with the FY2019 10-K: *"we reached a determination to **restate** our
consolidated financial statements"*, *"We identified **a material weakness**"*, and *"internal
control over financial reporting **was not effective** because of the material weakness."* The
same twelve months carried an **auditor change** — PwC's report says *"We served as the
Company's auditor from 2009 to 2020"*; Deloitte's says *"We have served as the Company's auditor
since 2020."* **Point-in-time honest: an analyst on 2020-03-31 saw a restatement, a material
weakness and an auditor change inside one year — [E4-22]'s first flag at full strength, and
"seldom just one cockroach in the kitchen" would have been the right response then.** An
analyst today sees **six consecutive unqualified ICFR opinions after it** (FY2020 through
FY2025, Deloitte). The flag fired, and it was remediated. Recorded, not carried forward as a
live disqualifier.

**STEP 2 — THE FOUR FLAGS [E4-22, E5-15].** *Accounting and disclosure, not litigation. Each
is a prompt to READ, never a verdict.*
- [x] **weak accounting** — fired 2020-03-31 (restatement + material weakness + auditor change,
      above); **remediated, six clean ICFR opinions since.** Not live.
- [ ] unintelligible footnotes — **NOT TICKED, and it is a genuine strength.** The Fund JV note
      (Note 7) discloses the equity percentages, the maximum exposure to loss built up in three
      named components, the intra-entity profit elimination mechanism, and the absence of
      recourse. The Oracle warrant note walks $12.9M + $311.0M of APIC to a $91.0M current and
      $215.5M long-term asset and a $17.9M cumulative revenue reduction. **These are hard things
      disclosed clearly.**
- [x] **trumpeted earnings projections / growth targets — FIRED, at full strength.** Four
      forward metrics guided for FY2026 and **every one of them is non-GAAP**: *"Revenue
      $3.9B – $4.2B … Non-GAAP Gross Margin ~34% … Non-GAAP Operating Income $800M – $900M …
      Non-GAAP EPS $2.55 – $2.85"* (Q2 2026 EX-99.2, slide 5, raised from the prior guide).
      Plus the CEO's *"**Bloom is now a standard for AI onsite power**"* and *"all the major US
      hyperscalers … have validated and approved our power solutions"* (Q2 2026 EX-99.1).
      **[E5-30] is the reason this matters:** *"once you start it, it's all over. You can't
      quit … And forecasting earnings, I can't imagine anything more destructive."*
- [x] **serial share issuance — FIRED, quantified [E5-15].** All classes, off the covers:
      **112,904,662** (2019-02-28: 58,462,298 A + 54,442,364 B) → 125,103,955 → 171,833,606 →
      177,117,368 → 206,096,097 → 224,973,118 → 230,398,527 → 280,548,215 → **294,527,346**
      (2026-07-22). **+160.9%, a 2.61x, in 7.4 years**, over which cumulative owner earnings
      were **NEGATIVE $1.88 billion** (Q4 below). Fully diluted Q2 2026: **323.3M against
      287.3M basic** (EX-99.2 slide 17), a further 12.5%. *(Class B was economically equivalent
      — ten votes, same participation — and all of it converted to Class A on 2023-07-27, so the
      sum across classes is the right series and no charter judgment is smuggled in.)*
- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRED, AND THIS IS THE SHARPEST
      READING IN THE FILE.** *"Trumpeting EBITDA … is a particularly pernicious practice…
      That's nonsense."* **Adjusted EBITDA is a headline metric in every one of the fourteen
      8-K exhibits on disk**, with its own five-year history printed (2021 $14.0M · 2022 $30.1M
      · 2023 $81.8M · 2024 $160.7M · 2025 $271.6M; Q2 2026 $253.4M). And the mechanism is
      **stated by the company itself, in the guidance footnote**: *"Bloom Energy is **not able
      to provide a quantitative reconciliation** of non-GAAP gross margin, non-GAAP operating
      expenses, non-GAAP operating income, and non-GAAP EPS measures to the corresponding GAAP
      measures without unreasonable efforts due to the uncertainty regarding, and the potential
      variability of, **reconciling items such as stock-based compensation expense**."*
      **Bloom guides $800–900M of "operating income" on a measure that deletes stock
      compensation, and says in the same sentence that it cannot tell you how much stock
      compensation there will be.** The deleted amount is not small: **non-GAAP operating income
      $221.0M against GAAP $72.8M in FY2025 — the entire $148.2M gap is $145.0M of stock
      compensation plus $2.4M of restructuring**; in FY2023 it was $19.2M against **negative
      $208.9M**. *The CGNX companion instruction is discharged: the FY2025 10-K is clean of
      "Adjusted EBITDA" and the flag lives entirely in the furnished exhibits. A run that read
      only the annual report would have scored this clean.*
- [x] **filed-figure tells [E4-30] — one fires and one does not.** *Unnaturally smooth growth:*
      **NO** — the record is violently unsmooth (owner earnings −$541M in 2023 to +$444M TTM),
      and [E5-29] is explicit that volatility is not the tell. *Cash taxes as a share of pretax
      income:* **not computable as a fraud tell and stated rather than forced** — Bloom paid
      $1,706k / $1,424k / $1,455k of cash income tax in 2025/2024/2023 against pretax **losses**
      in all three years, on $2.97bn of federal NOLs; a falling cash-tax ratio has no meaning
      where the denominator is negative. **Recording the absence rather than manufacturing a
      reading, per the absence-claim rule.**
- [x] **SIXTH FLAG — METRIC-SWITCHING [E2-49]. FIRED, AND IT IS THE STRUCTURAL FINDING.**
      *"Yardsticks seldom are discarded while yielding favorable readings. But when results
      deteriorate, most managers favor **disposition of the yardstick rather than disposition
      of the manager** … demand pre-set, long-lived and small bullseyes."* Bloom published
      **product accepted, megawatts accepted net, product cost per kilowatt and installation
      cost per kilowatt** in the MD&A of every 10-K from FY2018 to FY2023 — six years, four
      metrics, a real physical bullseye. **The FY2024 10-K deleted all four**: *"We have
      determined that the foregoing metrics **no longer reflect key operating metrics** of the
      company and therefore **we will no longer report on these metrics** … trends in costs and
      selling prices per kilowatt are **less representative** of our overall business
      performance … These factors can **distort** the cost or revenue per kilowatt metrics.
      Management relies primarily on revenue, **non-GAAP gross and operating margins**, as well
      as cash flows from operating activities to manage operations."* **The test [E2-49] sets is
      whether the switch FOLLOWS deterioration or is announced ahead with reasons. The filed
      answer is that it follows it:** gross profit per kilowatt had gone $1,475 → $1,288 over
      six years and the discarded year's own last reading, 2022, was a **$107/kW INCREASE in
      product cost**, the only increase in the series. Reasons were given, at length, and they
      are not absurd — solution complexity really does vary. But the yardstick that went was the
      physical one **[E4-55]**, and the yardstick that replaced it is the one management is
      **paid on** and the one that **deletes stock compensation**. *A candor case would have
      kept the unit series and added the solution metric beside it.*
- [ ] **SEVENTH — dividends funded by issuance [E2-52]: NOT TICKED, and it is nearly nothing.**
      Bloom paid $947k (2025), $1,468k (2024) and $925k (H1 2026) of "Dividend paid". Traced:
      this is the Korean JV distributing to SK ecoplant as the 60% holder, not a Bloom dividend.
      No Bloom common dividend has ever been paid.
- [x] **EIGHTH — stock-price targeting [E3-50]. FIRED, and then partly withdrawn.** The 2021
      CEO award contained **1,000,000 PSUs that *"would have vested based on future stock price
      performance through 2030"*** — a pay instrument whose bullseye is the quote itself, which
      is the premise *"with which we adamantly disagree."* **Sridhar consented to their
      cancellation** as part of the 2025 Equity Package, and the 2026 proxy frames it as *"Dr.
      Sridhar's commitment to the Company's long-term"* interests. **A withdrawal in the right
      direction, recorded as such.** What replaced it is the [E4-52] problem below.
- [ ] **NINTH — the "except for" flag [E2-57]: NOT TICKED in the 10-K.** But note the direction
      of travel: the non-GAAP reconciliations add back *"Restructuring"*, *"Impairment of
      assets"*, *"Loss on debt extinguishment and conversion inducement expenses"* ($98.6M in
      2025) and *"Effects of assets buyout and repowering"* — which is [E5-33]: *"to tell owners
      year after year, 'Don't count this' … is misleading."* **The $130.1M of 2023 and $115.3M
      of 2022 PPA impairments are added back to Adjusted EBITDA, and they are real costs of real
      fuel cells that stopped working.** They stay in the owner-earnings mean at Q4.
- [ ] **TENTH — the restructuring charge [E3-53]: NOT TICKED as a pattern.** Restructuring is
      $2.4M (2025), −$0.4M (2024), $9.2M (2023) — immaterial against revenue. No
      dumped-into-one-quarter behaviour found.

**STEP 3 — THE PRIMARY TEST [E2-01].** Earnings rate on equity capital employed, *without
undue leverage or accounting gimmickry* — **not** EPS growth. Multi-year series, balance
sheet before income statement.

**Balance sheet first, and it is the whole answer.** At 2026-06-30, after the best half-year
in the company's history: **additional paid-in capital $5,332,587k against an accumulated
deficit of $3,720,965k.** At the 2018 IPO the prospectus disclosed an *"accumulated deficit of
**$2.3 billion**"*; at 2025-12-31 it was **$3,986,983k**. **Sixty-nine point eight per cent of
every dollar of capital ever contributed to this company has been consumed**, and that is
after the $266.9M earned back in H1 2026.

**The series, on equity attributable to common stockholders:**
| window | net income attributable | equity | rate |
|---|---|---|---|
| FY2023 | **−$302,116k** | $502,078k (year-end) | **−60.2%** |
| FY2024 | **−$29,227k** | $562,471k (year-end, 229,142,474 shares) | **−5.2%** |
| FY2025 | **−$88,434k** | $768,641k | **−11.5%** |
| **TTM to 2026-06-30** | **+$244,942k** | avg $1,190,320k | **+20.6%** |
| **whole life, on contributed capital [E2-73]** | **−$3,720,965k cumulative** | $5,332,587k paid in | **−69.8%** |

**[E2-73] decides which denominator answers the question the corpus asks:** *"the managers of
the units should be judged by the returns they achieve on **the underlying assets**; what we pay
for a business does not affect the amount of capital its manager has to work with."* The
capital this management has had to work with is **$5.33bn of contributed equity plus $2.5bn of
zero-coupon convertible notes = $7.83bn**, and the cumulative return on it is a **$3.72bn
deficit**. On that denominator the TTM's $244.9M is **3.1%**. **The 20.6% reading is real and
it is one year old; the 3.1% reading is real and it is twenty-five years old. Both are stated
because reporting only one of them is how this test gets gamed**, and [E2-01] exists *"in
opposition to the metric managements game."*

**The half-owner test [E2-26]:** does this reporting tell me what I would want to know if the
positions were reversed?

**MIXED, and the split is clean — the footnotes pass and the headline does not.** The things I
would most want to know, I was told, in the footnotes, unprompted and in detail: that 42.6% of
FY2025 revenue went to joint ventures Bloom part-owns, with the equity percentages, the
elimination mechanism and the $45.7M maximum exposure to loss; that $324.4M of stock was handed
to a customer's customer, with the Black-Scholes assumptions, the grant date, the exercise date
and the $17.9M cumulative revenue charge; that one customer was 73% of last quarter's revenue,
**volunteered in an amendment filed one day later to correct an error that had made the
concentration look smaller** — which is **[E2-69]**, a deviation toward candor, and it is
scored in Bloom's favour. What I would NOT learn from the headline is that the $800–900M of
guided 2026 "operating income" is a number from which stock compensation of unstated size has
been removed, or how many megawatts Bloom shipped, or what it now costs to make a kilowatt.
**The one-time items are quantified separately at every line ([E2-26]'s passing condition) and
then also buried in an adjusted figure ([E2-26]'s failing condition) — Bloom does both.**

**The institutional imperative — score all four [E2-30].** *Not a fraud test: "institutional
dynamics, not venality or stupidity."*
- [ ] **resists any change in current direction — NOT TICKED, the reverse.** This management has
      changed direction repeatedly and mostly correctly: Korea distribution (2018), hydrogen and
      electrolyzers (2021), carbon capture, and the pivot to AI data centres (2024). It also
      **exited** things: the last consolidated PPA Entity sold August 2023; the PPA portfolios
      repowered and sold to financiers; $130.1M of PPA impairments taken. **A management that
      writes off its own projects is not the [E2-30] type.**
- [x] **projects/acquisitions materialise to soak up available funds — TICKED, one instance,
      and it is $2.5 billion.** Bloom raised **$2,500,000k of zero-coupon convertible notes in
      FY2025** (cash-flow statement, *Proceeds from issuance of debt*) against total FY2025
      capex of **$56,759k** and a stated capacity plan costing a fraction of it. Cash went from
      $950,971k to $2,481,580k to **$2,666,859k**. **Bloom now holds $2.67bn of cash it has no
      filed use for**, against the entire company having consumed $1.88bn of owner earnings in
      eight years. The filing's own statement of purpose is thin: *"We intend to fund these
      capital expenditures from cash on hand as well as cash flow expected to be generated from
      operations."* **[E2-64] is the defence and it is a real one** — *"the most attractive
      opportunities may present themselves at a time when credit is extremely expensive — or even
      unavailable"* — and raising free money while the window was open is defensible. **The flag
      is not that they raised it; it is that $2.67bn of unallocated cash in the hands of a
      management paid on revenue growth is exactly the condition [E2-30](2) describes.**
- [ ] staff studies produced to justify the leader's craving — **NOT FOUND** in the filings.
      Recorded as not found, not as absent.
- [x] **peer behaviour mindlessly imitated — TICKED, weakly, on the non-GAAP apparatus.** The
      Adjusted-EBITDA-plus-non-GAAP-EPS guidance format is the sector convention, adopted
      wholesale. That is imitation of a disclosure practice, not of a capital decision, and it is
      the lightest of the four.

**Capital allocation — the two buyback conditions [E5-08]:**
- **(1) ample funds for operations and liquidity? YES, overwhelmingly** — $2,666,859k of cash
  against $2,530,341k of total debt principal, of which $2.5bn is zero-coupon and due 2030.
- **(2) repurchases at a material discount to conservatively calculated IV? NOT APPLICABLE —
  BLOOM HAS NEVER REPURCHASED A SHARE, AND THAT IS THE CORRECT DECISION.** At $275.75 against
  the value range computed at Q5, a buyback would destroy owner value. **[E2-51]'s "the refusal
  is a tell too" does NOT fire**, because the refusal is only a tell *"when these clearly are in
  the interests of owners"* — and here they clearly are not. **No capital-allocation flag on
  this ground.** [E5-24] governs and it cuts for management: *"what is smart at one price is
  dumb at another."*

**BUT THERE IS A CAPITAL-ALLOCATION FLAG, AND IT IS A SINGLE QUANTIFIED DECISION IN Q2 2026.**
**The Oracle net-settlement inducement. Bloom paid $72.3 million of its own stock for nothing
that accrues to its owners.** The filed facts, verbatim and in order (Q2 2026 10-Q, Note 3):
- A warrant on **3,531,073 shares at $113.28**, granted 2026-04-09, fair value **$251.6M**.
- *"On May 1, 2026 … Oracle completed a **cashless exercise** of the Warrant, resulting in the
  issuance of **1,905,433 shares**… Under the terms of the warrant agreement, **Oracle could
  elect either net or gross settlement.** Because the net settlement would result in **1.4
  million fewer shares** being issued than a gross settlement, **we agreed to issue Oracle an
  additional 248,798 shares of common stock as an inducement for Oracle to elect net
  settlement.** These incremental shares represented additional consideration with a fair value
  of **$72.3 million**. As a result, the aggregate fair value of the shares issued upon exercise
  of the Warrant, including the incremental shares, was **$324.4 million**."*

**The arithmetic, from those figures alone.** Gross settlement would have paid Bloom
**3,531,073 × $113.28 = $400.0 million in cash** and issued 3,531,073 shares. Net settlement
paid Bloom **nothing** and issued 2,154,231 shares — **1,376,842 fewer**, which at the $290.59
per share implied by the $72.3M valuation of the 248,798 inducement shares is worth **$400.1
million.** **The swap of cash for shares is a wash by construction — that is what a cashless
exercise is. The $72.3 million inducement is therefore the entire economic content of the
decision, and all of it went out.** Bloom's stated object was to issue fewer shares; the shares
it "saved" reappear anyway in the diluted count (323.3M against 287.3M basic). **Bloom forwent
$400.0M of cash and paid $72.3M of stock to make its share count 1.4 million smaller.**

**[E5-44] is the governing rule and it sharpens the reading rather than softening it:** *"The
intrinsic value of the shares you give … **must not be greater than the intrinsic value of the
business you receive**"* — measure the paper at IV, not at quote. Against the Q5 range below,
Bloom's paper is worth far less than $290.59, so in IV terms the $72.3M gift is smaller than it
looks — **and that makes the decision worse, not better, because it means Bloom was holding
$2.67bn of cash and chose to pay with the one currency it should have been hoarding, while
handing back $400M of cash it could have kept.** **[E3-50]** names what the motive looks like:
managers whose premise is *"that their job at all times is to encourage the highest stock price
possible (a premise with which we adamantly disagree)"*, optimising a reported share count.

**Stated with the humility clause [E4-13], which is mandatory here:** *"it is natural for CEOs
to be optimistic about their own businesses. **They also know a whole lot more about them than I
do.**"* Oracle's negotiating position is not in the filing. Bloom may have been buying a
relationship worth multiples of $72.3M, or complying with a term it had already conceded in
October 2025. **This rests on filed arithmetic and not on knowledge of the negotiation, and
under [E4-13] it binds position size, never the discount rate.** There is no position to size.
**[E4-52] — THE FLAGS CONVERGE, AND THAT IS A DIFFERENT EVENT FROM A LIST OF FLAGS.**
*"extreme consequences from **confluences** of psychological tendencies acting in favor of a
particular outcome … it dominates life."* **Five findings above point at one outcome, and the
pay plan names it.** Pay metrics, from the three DEF 14As (2024-03-26, 2025-04-02, 2026-04-08):
- PSUs *"eligible to vest based on achievement of **product revenue growth** and **adjusted
  product gross margin** goals over a three-year performance period, each weighted equally at
  50%, with Dr. Sridhar eligible to receive **up to 300% of target**."*
- The 2023 LPSUs: *"the Company's achievement of **product and service revenue** compound annual
  growth rate … and **non-GAAP gross margin** over a three-year performance period, weighted
  **60%** and **40%**, respectively"*, with targets *"set at 26% for CAGR and 26%, 27%, and 27%
  for non-GAAP gross margin"*. 2025 PSUs certified at **59% of target**.
- CEO total compensation: **$1,704,008 (2023) · $44,961,745 (2024), including a $42,394,800
  stock award · $3,502,747 (2025)**.

**THE CONFLUENCE, LAID OUT:** *(i)* the four **physical** unit metrics were deleted in FY2024;
*(ii)* all four FY2026 guidance metrics are **non-GAAP**; *(iii)* management is paid on **revenue
growth** and **adjusted / non-GAAP gross margin** — **there is no return-on-capital metric and no
owner-earnings metric anywhere in the plan**; *(iv)* the company **states it cannot quantify the
stock compensation** its guided profit measure excludes; *(v)* the share count rose **2.61x in
7.4 years**; and *(vi)* $72.3M was paid to make the reported share count 1.4 million smaller.
**Not six prompts. One reinforcing system whose output is a non-GAAP margin on a growing revenue
line, with the cost of the equity used to buy that growth removed from the measure the plan pays
on.** *And [E2-49]'s remedy is the exact one Bloom moved away from: "demand pre-set, long-lived
and small bullseyes." Cost per kilowatt was one. It is gone.*

**RELATED PARTIES — READ, as the brief required, and the SK ecoplant read is not what I
expected.** SK ecoplant was *"a related party from September 23, 2023 through July 10, 2025"*
— both a shareholder (23,491,701 Class A shares, 10.3% at 2024-12-31) and the take-or-pay
distributor for Korea (500 MW 2022–2024, plus 250 MW through 2027). **It sold down and out:**
10,000,000 shares on 2025-07-10 (to 5.8%, *"ceased to be a related party"*), 2,608,000 on
2025-08-14, 3,912,000 on 2025-09-29, leaving **2.5% at 2025-12-31.** **A strategic partner that
put $311.0M of preferred into Bloom in 2023 sold roughly 70% of its stake during 2025 — the year
the AI order book arrived.** That is not a governance flag; it is a counterparty's own revealed
view, and it is recorded because it is filed. Related-party pricing is asserted arms-length
(*"transacted at arms-length and prevailing market terms"*) and the amounts are fully tabulated
each year. **The related-party disclosure passes; what it discloses is adverse.**

**THE GUARDRAIL — check before writing the verdict.**
- [x] **Confirmed: nothing in this Q3 is being used to promote the name.** It could not be —
      Q2 already closed the file, and a Q3 that read clean would not reopen it **[E2-37, E2-38,
      E3-39]**. *"a textile company that allocates capital brilliantly within its industry is a
      remarkable textile company — but not a remarkable business."*
- [x] **Key-person dependence IS recorded at Q2 as a moat defect [E4-23]**, not here as a
      strength. KR Sridhar, founder 2001, Chairman and CEO, author of the technology and of
      every pivot. Written at Q2 above.
- [x] **Is the manager the plan? [E2-35, E2-36]** — not applicable in the buy direction, since
      the franchise is not intact to begin with. There is no *"localized excisable cancer"*
      here: the thing that would need repairing is the absence of a moat, which is *"a corporate
      Pygmalion"* and not buyable.

- **VERDICT: [x] IN**  [ ] OUT (integrity failure is permanent)  [ ] UNRESEARCHED → ____
  [ ] UNKNOWABLE → ____ — **AS A BINARY GATE, and it is a thin IN with six flags live.**

*IN = **no disqualifier found**, and nothing more. **[E5-17]** caps it: *"People are not that
easy to read. Sincerity and empathy can easily be faked."* This is not a finding that Bloom's
managers are honest; it is the recorded absence of a found disqualifier, across eight 10-Ks,
five 10-Qs, three proxies and the 424B4. **Six flags fired — weak accounting (2020, remediated),
trumpeted projections, serial issuance, EBITDA promotion, metric-switching, stock-price
targeting (withdrawn) — and one $72.3M capital-allocation decision.** They converge under
[E4-52], which is why the gate is thin rather than comfortable. **And the honest counterweight,
which must be stated because [E4-26] requires hunting disconfirming evidence hardest for one's
own hypothesis: this management disclosed the 73% customer by amending its own filing to make
the number look worse; it discloses the Fund JV perimeter, the maximum loss exposure and the
Oracle warrant mechanics in full; it took $245M of impairments on its own failed projects; it
never obtained a going-concern qualification in twenty-five years of losses; and its CEO
voluntarily cancelled 1,000,000 stock-price-linked PSUs. [E5-38] applies — a fired flag is not
a venality finding.***

## Q4 — WILL IT SURVIVE?  ·  **RECORDED BELOW THE GATE**

### FIRST: WHAT THE DEPOSIT LINE DID TO OPERATING CASH — the brief's central prior, cross-checked to the dollar across every year
**The prior, stated in the brief: "customer deposits and prepayments on AI-data-centre fuel-cell
orders are funding the operating cash line."** **It is right in two of the three periods where
Bloom reported positive operating cash, wrong in the third, and the third is the one that matters
for the sign of owner earnings.** Every figure below is the line *"Deferred revenue and customer
deposits"* read **off the filed Consolidated Statements of Cash Flows**, not off a tag:

| year | operating cash flow | **deposit line** | **OCF NET OF THE DEPOSIT LINE** | deposit line as % of OCF |
|---|---|---|---|---|
| 2018 | −$91,948k | −$21,774k | −$70,174k | — |
| 2019 | +$163,770k | +$37,146k | **+$126,624k** | 22.7% |
| 2020 | −$98,796k | −$12,972k | −$85,824k | — |
| 2021 | −$60,681k | −$22,677k | −$38,004k | — |
| 2022 | −$191,723k | +$35,156k | −$226,879k | — |
| 2023 | −$372,531k | −$42,635k | −$329,896k | — |
| **2024** | **+$91,998k** | **+$139,868k** | **−$47,870k** | **152.0% — the screen's flag, reproduced exactly** |
| **2025** | **+$113,949k** | **−$142,605k** | **+$256,554k** | **the line RAN THE OTHER WAY and OCF was still positive** |
| **H1 2026** | **+$300,042k** | **+$301,232k** | **−$1,190k** | **100.4%** |
| H1 2025 | −$323,793k | −$178,807k | −$144,986k | — |
| **TTM to 2026-06-30** | **+$737,784k** | **+$337,434k** | **+$400,350k** | **45.7%** |

**THE THREE ANSWERS, PLAINLY.**
1. **FY2024 — the prior is CONFIRMED AND THEN SOME.** Operating cash was $92.0M and the deposit
   line supplied $139.9M of it. **Net of customer deposits, FY2024 operating cash was NEGATIVE
   $47.9M.** The screen's `wc_note` fired at 152% and reproduces to the dollar.
2. **FY2025 — the prior is REFUTED, and this is the single strongest fact in the file AGAINST my
   own conclusion.** The deposit line **reversed by $142.6M** — customer deposits fell from
   $220,115k to $78,207k, *"primarily driven by a **lower level of new customer deposits**
   compared to the prior year"* — **and operating cash was still positive at $113.9M.** Net of the
   deposit swing, FY2025 operating cash was **+$256.6M.** The deposit line was a drag of 125% of
   reported OCF and the number stayed positive anyway. **A deposit-funded operating cash line
   cannot do that.**
3. **H1 2026 — the prior is CONFIRMED to within $1.2 million, in the most recent period.**
   Operating cash $300,042k; the deposit line $301,232k. **Net of it, operating cash for the first
   half of 2026 was NEGATIVE $1,190k.** Customer deposits rose from $78,207k to **$360,568k**,
   +$282.4M: *"primarily driven by **receipt of new deposits associated with recently executed
   customer agreements** and milestone payments on ongoing projects, partially offset by certain
   deposits becoming non-refundable."* The company's own MD&A puts the year-over-year swing at
   *"an increase of $122.4 million attributable to deferred revenue and customer deposits."*

**SO: OPERATING CASH IS NOT OWNER EARNINGS AT BLOOM, AND THE DELL LESSON APPLIES — BUT NOT AS THE
BRIEF PREDICTED IT.** At DELL one working-capital line *was* the entire owner-earnings series. At
Bloom the deposit line is **45.7% of trailing operating cash**, not 100%, and the reason is that
the two most recent half-years are entirely different in composition: **H2 2025 generated
$437,742k of operating cash of which the deposit line supplied only $36,202k — $401,540k, or
92%, came from the business itself; H1 2026 generated $300,042k of which the deposit line
supplied $301,232k — 100.4%.** The deposit line is not funding the business. **It is making the
business's cash generation unreadable half-year by half-year**, which is a different and, for Q4,
more relevant defect: *every single reported operating-cash figure at Bloom is dominated by the
timing of refundable customer prepayments on orders not yet delivered.* **Both halves of the
statement must be carried:** the TTM owner-earnings number below is positive with the deposit
inflow **and it is still positive without it**, at **+$106.8M against +$444.2M** — a 76% haircut
that does not change the sign.

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].** *"Using precise numbers is,
in fact, foolish; working with a range of possibilities is the better approach."* Do **not**
pick a window and defend it; carry the spread alongside the capex band.
**OWNER EARNINGS BY YEAR**, on the framework's convention — operating cash flow less stock
compensation less the (c) guess — every input read off a **filed** Consolidated Statement of Cash
Flows (FY2018–19 from the FY2020 10-K; FY2020–22 from the FY2022 10-K; FY2023–25 from the FY2025
10-K; H1 from the 2026-06 10-Q). In $ thousands:

| year | OCF | **SBC** | capex | D&A | **OE, capex end** | **OE, D&A end** |
|---|---|---|---|---|---|---|
| 2018 | −91,948 | 168,482 | 45,205 | 53,887 | **−305,635** | −314,317 |
| 2019 | +163,770 | 196,291 | 51,053 | 78,584 | **−83,574** | −111,105 |
| 2020 | −98,796 | 73,893 | 37,913 | 52,279 | **−210,602** | −224,968 |
| 2021 | −60,681 | 73,274 | 49,810 | 53,454 | **−183,765** | −187,409 |
| 2022 | −191,723 | 112,259 | 116,823 | 61,608 | **−420,805** | −365,590 |
| 2023 | −372,531 | 84,480 | 83,739 | 62,609 | **−540,750** | −519,620 |
| 2024 | +91,998 | 82,424 | 58,852 | 53,048 | **−49,278** | −43,474 |
| 2025 | +113,949 | 139,406 | 56,759 | 50,566 | **−82,216** | −76,023 |
| **TTM to 2026-06** | **+737,784** | **180,500** | **113,078** | **53,009** | **+444,206** | +504,275 |

**EIGHT CONSECUTIVE NEGATIVE YEARS AND THEN ONE POSITIVE TRAILING YEAR. Cumulative owner earnings
FY2018–FY2025 at the capex end: NEGATIVE $1,876,625 thousand — $1.88 billion consumed in eight
years.**

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25], and [E4-38] says publish EVERY
window, so here is every window:**

| window | **capex end** | **D&A end** |
|---|---|---|
| FY2018–25 (8y) | −$234,578k | −$230,313k |
| FY2019–25 (7y) | −$224,427k | −$218,313k |
| **FY2021–25 (5y — the corpus default [E2-42])** | **−$255,363k** | −$238,423k |
| FY2022–25 (4y) | −$273,262k | −$251,177k |
| FY2023–25 (3y) | −$224,081k | −$213,039k |
| FY2024–25 (2y) | −$65,747k | −$59,748k |
| FY2025 (1y) | −$82,216k | −$76,023k |
| **TTM to 2026-06-30** | **+$444,206k** | **+$504,275k** |

- **Short-window mean** (TTM to 2026-06-30): **+$444.2M** at the capex end.
- **Long-window mean** (FY2018–25, eight years): **−$234.6M** at the capex end.
- **COMBINED RANGE, across every window and both (c) ends: −$273,262k to +$504,275k.**
  **WIDTH IN DOLLARS: $777,537 thousand — $777.5 million. WIDTH IN A WORD: TOTAL.**
  **The range does not merely span a wide band; IT SPANS ZERO, and it changes sign between the
  corpus's own default window and the trailing year.** With the D&A end struck out (below), the
  range is **−$273.3M to +$444.2M, a width of $717.5M.**
- **Net of the deposit line**, every window moves down and the TTM narrows to **+$106,772k** at
  the capex end. The full deposit-net series (capex end): 2018 −$283,861k · 2019 −$120,720k ·
  2020 −$197,630k · 2021 −$161,088k · 2022 −$455,961k · 2023 −$498,115k · 2024 −$189,146k ·
  2025 **+$60,389k** · **TTM +$106,772k.** **On this construction the business first earned
  money for owners in FY2025, and the amount was $60.4 million.**

**IS THAT RANGE TOO WIDE TO REACH A CONCLUSION? YES, AND [E4-25] SAYS THAT IS THE VERDICT.**
*"Using precise numbers is, in fact, foolish; working with a range of possibilities is the better
approach. **Usually, the range must be so wide that no useful conclusion can be reached.**"* A
$717.5M range that changes sign, on a business whose market capitalisation is $81.2bn, does not
support any owner-earnings statement at all. **And the reason is nameable, which is what [E5-11]
asks for.**

**THE DISTORTED PERIOD, NAMED — AND IT IS NOT A DISTORTION, IT IS A LEVEL SHIFT.** [E3-55] draws
the line the framework requires here: *"If we have a business about which we're extremely
confident as to the business result, we would prefer that it have high volatility"* — the spread
measures **distortion and uncertainty about the LEVEL**, and where only the year-to-year figure
bounces the bounce is noise. **This is not noise. The level moved, and it is datable:** the AEP
1 GW framework and its 100 MW order (2024, with a $100.0M letter of credit issued 2024-12-14);
the Brookfield $5.0bn AI Fund structure (**August 2025**); the Oracle partnership (**2025-10-28**).
Revenue went $1,473.9M (FY2024) → $2,024.0M (FY2025) → **$1,816.4M in six months** with $3.9–4.2bn
guided. **The business that produced +$444.2M of owner earnings has TWO QUARTERS of filed history.**
**[E2-42] requires "not less than a five-year test as a rough yardstick of economic performance."
Bloom's current business has two quarters.** This is the HHH shape the queue already ruled on:
**a filed history that describes a different company than the one the market cap prices.**

**AND THE TIER-3 TRIAGE PUT BLOOM IN THE WRONG SUB-CLASS.** The queue filed BE under *"NEGATIVE ON
EVERY CONSTRUCTION — bottom AND top … no owner earnings exist on any window or either capex end.
These runs are the cheapest in the queue."* **That is false, and the filings say so: the trailing
year is +$444.2M at the capex end and +$504.3M at the D&A end.** BE belongs in the sub-class two
rows down — *"**SIGN CHANGE — recoveries**: early years loss-making, recent years positive, so the
multi-year mean is averaging two different businesses [E4-25]. **The run must date the inflection
and refuse the blended mean**"* — with ACMR, ALKT and ACVA. **The inflection is dated above. The
blended mean is refused, in both directions: I will not use FY2018–23 to price the 2026 business,
and I will not use two quarters to underwrite it.**

- **Maintenance capex — a DISCLOSED JUDGMENT [E2-23], and the D&A END IS INVALID HERE.**
  **[E5-20] applies and the brief predicted it correctly.** The default is D&A **[E3-44, E2-41]**
  — *"at 95% of American businesses, capital expenditures that over time roughly approximate
  depreciation are a necessity"* — **but Bloom's own filing places it in the exception class**:
  TTM capex is **$113,078k against D&A of $53,009k, 2.13x**, and the filing says it is going
  higher: *"We expect to continue making **substantial capital investments** over the next few
  quarters to expand production capacity at our Fremont, California manufacturing facility …
  part of our strategic plan to increase capacity to approximately **2 GW by the end of 2026**."*
  A company doubling its manufacturing line cannot maintain its unit volume out of a depreciation
  charge struck on a 1 GW asset base. **The D&A end of every row above is struck out, not carried
  as an equally legitimate answer** — which is exactly what the framework says the band is for:
  *"The band survives only as a display of the guess, never as two equally legitimate answers."*
  **[E4-47]** reinforces it for an asset-heavy filer building in current dollars.
- **Band used: total capex only, the CAPEX END, as the sole legitimate construction. (c) judged
  UP from it.** My disclosed judgment — and it is a guess, as [E2-23] insists: *"(c) must be a
  guess"* — is that maintenance (c) for this business sits at roughly **$150M a year**, above the
  $113.1M of trailing total capex, because (i) the 2 GW build is a capacity addition whose
  *replacement* obligation arrives behind it, (ii) [E2-23]'s **working-capital increment is
  required here and the filing proves it**: H1 2026 alone absorbed **−$115,057k of inventories,
  −$187,654k of contract assets and −$89,590k of receivables** on revenue growing 150%, and (iii)
  **[E2-60]**: financial strength is part of what (c) must maintain, and a business whose
  reported operating cash swings on refundable customer prepayments requires a cash buffer to
  hold its position. **At (c) = $150M, TTM owner earnings are +$407.3M; net of the deposit line,
  +$69.9M.** The sign does not change at any (c) I can defend — **which is why the verdict below
  does NOT rest on the capex band.**
- **Stock compensation subtracted in full [E5-06]: YES, $180,500k over the trailing twelve months,
  and $1,030,941k over the whole listed life.** *"To say 'stock-based compensation' is not an
  expense is even more cavalier."* **And [E3-70] says the reported charge is only the FLOOR of the
  subtraction where SBC is material** — *"an amount equal to what the company could have realized
  by publicly selling options of like quantity and structure."* **Bloom gives the measure of the
  gap itself: it valued 248,798 shares handed to Oracle at $72.3 million, i.e. $290.59 each, while
  the accounting charge for employee awards is struck at grant-date fair value on a stock that has
  gone from $86.89 (2025 year-end close, per the proxy) to $275.75.** The $180.5M is the floor.
- *If the capex band changed the verdict it would be UNKNOWABLE **[E4-25]**. **It does not — the
  window does.** Stated so the two reasons are not confused.*

### Great, good, or gruesome? **[E4-20]**
- [ ] great — high return, rising, little capital needed
- [ ] good — attractive return, earned also on added capital
- [ ] gruesome — grows, eats capital, earns little
- [x] **THE CLASSIFICATION CANNOT BE MADE, AND REFUSING TO MAKE IT IS THE HONEST ANSWER.**

**The eight-year record is textbook gruesome, word for word.** *"The worst sort of business is one
that **grows rapidly, requires significant capital to engender the growth, and then earns little
or no money.** Think airlines … Investors have poured money into a bottomless pit, **attracted by
growth when they should have been repelled by it.**"* Revenue grew **4.9x** (2018 $632.6M → TTM
$3,113.2M). Capital consumed: **$1.88bn of owner earnings over eight years**, plus a **$3.72bn
accumulated deficit** against **$5.33bn of contributed capital**. Money poured in: $2.5bn of
converts, $311.0M of SK preferred, and 181.6 million net new shares. **On the FY2018–FY2025 record
this is the gruesome account, and it is not a close call.**

**And the trailing twelve months are not gruesome on any reading.** Owner earnings +$444.2M at the
capex end (+$407.3M at my (c) = $150M); product gross margin 36.5%; GAAP operating margin 17.1% in
Q2 2026; return on average equity +20.6%. [E4-43] warns explicitly against over-reading the test —
the **good** class *passes*, and *"What makes cash-consuming gruesome is only 'unless the cash they
consume gets to earn a reasonable return.'"* **For two quarters, the cash consumed has earned a
return that would clear [E5-40]'s ~12% "quite satisfactory" bar several times over.**

**[E4-25] and the triage rule forbid blending these into one classification, and I refuse to.** A
"gruesome" verdict would be applying a 2018–2023 record to a business whose product mix, customer
set, financing structure and margin structure all changed in 2025. A "good" verdict would be
underwriting a capital-intensive manufacturer on two quarters. **The classification requires the
five-year test [E2-42] the business has not yet lived through.**

### Staying power — score all three **[E5-11]**
- **(1) a large and reliable stream of earnings — LARGE, ✓. RELIABLE, ✗, AND THIS IS THE ONE THAT
  FAILS.** Large: TTM revenue $3,113.2M, gross profit ~$935M, operating income $254.4M in H1.
  Reliable: **eight consecutive negative owner-earnings years, a $777.5M range across windows that
  changes sign, and a reported operating-cash figure whose composition flips between 8% and 100%
  customer-prepayment-driven from one half-year to the next.** [E5-29] is the right discipline here
  — *"Volatility is far from synonymous with risk"* — and this is not volatility around a known
  level; **it is an unestablished level.** *"Ignoring that last necessity is what usually leads
  companies to experience unexpected problems"* is about strength (3); here it is strength (1) that
  is unproven.
- **(2) massive liquid assets — ✓ PASSES, UNAMBIGUOUSLY, AND THIS REFUTES THE BRIEF'S PRIOR.**
  At 2026-06-30: **cash and cash equivalents $2,666,859k** plus restricted cash $1,050k =
  **$2,667,909k** against **total debt principal of $2,530,341k**. **Bloom is in a NET CASH
  position.** Cash went $745,178k (2023) → $950,971k (2024) → $2,481,580k (2025) → $2,688,508k
  (2026-06-30, incl. restricted). [E5-39]'s test — *"cash is a lot like oxygen"*, nothing depending
  on *"the kindness of strangers"* — is met: **no revolver is drawn, no commercial paper, and the
  Fund JV creditors have no recourse.**
- **(3) no significant near-term cash requirements — ✓ PASSES, AND BY A LARGE MARGIN.** Current
  debt at 2026-06-30 is **$7,269k**, being $4,686k of residual Green Notes and a $2,583k Korean JV
  term loan. The **$2,500,000k of 0% Convertible Senior Notes mature November 2030 and pay NO
  INTEREST** — *"0 % Convertible Senior Notes due November 2030 … 0.0 %"*. Their initial conversion
  price is **$194.97** (rate 5.1290 per $1,000, = 12,822,500 shares) against a $275.75 quote, and
  the conversion trigger quarter-end has already passed (March 31, 2026) — **so the most likely
  outcome is that $2.5bn of debt is extinguished into 12.8M shares, 4.4% dilution, and never has
  to be repaid in cash.** *"We and all of our subsidiaries were in compliance with all financial
  covenants as of June 30, 2026."*
- **Leverage, named and quantified [E4-16, E3-29]:** total debt principal **$2,530,341k**, of which
  **98.8% is a zero-coupon convertible due in four years and three months** and 0.1% is
  non-recourse. **Cash interest paid was $10,676k in H1 2026** (down from $26,660k). *"There is no
  leverage ratio in this framework and the corpus supplies none"* — so it is judged: **this is the
  cheapest large capital structure in this queue.** **[E3-52] is the right lens and it favours
  Bloom**: *"liabilities without covenants or due dates … the benefit of debt … but saddle us with
  none of its drawbacks."* Zero-coupon, long-dated, convertible above the strike is close to that
  animal. **The customer deposits are NOT** — see the death mechanism.
- **[E2-54] COVERAGE, COMPUTED: *"all interest, both payable and accrued, to be comfortably met out
  of current cash flow net of ample capital expenditures."*** TTM interest expense **$42,547k**;
  TTM operating cash less capex **$624,706k**. **Coverage 14.7x.** Net of the deposit line:
  $287,272k / $42,547k = **6.8x.** **"Zip up your wallet" does not apply. This test passes on
  either construction.**

### Name the specific way THIS business dies **[E2-27, E3-24]**
**The mechanism, and it is the one the brief named: a deposit-funded order book that reverses.**
Bloom's revenue is recognised on **physical customer acceptance** of boxes built to order for a
handful of counterparties — **73% of last quarter's revenue from one of them** — against
**refundable** prepayments: *"Billings to customers are recorded within deferred revenue when
related to performance obligations that have not yet been satisfied, and **within customer deposits
if payments are refundable**."* If AI data-centre capex pauses, the sequence is: new deposits stop
(seen already, in FY2025: *"a lower level of new customer deposits compared to the prior year"*,
$220.1M → $78.2M); the refundable portion is called; inventory and contract assets built against
those orders become unsaleable to anyone else; and the 20-year O&M book — the line that lost money
for seven of eight years — becomes the only revenue left, at a 16–19% gross margin against a fixed
cost base sized for 2 GW.

**Quantified from filed figures, and the outcome.** The exposure at 2026-06-30: **customer deposits
$360,568k** (refundable portion not disclosed — the one number I would want and do not have),
**inventories** and **contract assets $241,186k → materially higher after H1's −$187,654k build**,
and a manufacturing base being doubled. **Against that: $2,666,859k of cash, $7,269k of current
debt, and no interest obligation until 2030.** **Model the extreme, per [E2-55] — *"acceptable
long-term results under extraordinarily adverse conditions"* — and [E4-40]'s discipline, model
EXPOSURE not experience.** Suppose **every** customer deposit is refundable and every one is called
($360.6M), the entire contract-asset balance is written off ($241.2M), inventories are halved
against a 2025 year-end balance and TTM build, and Bloom returns to its FY2023 burn rate of
$372.5M of operating cash outflow a year. **Total first-year cash cost: roughly $1.1–1.3 billion.
Bloom survives it with over $1.3 billion of cash left, no covenant to breach, and no maturity
until November 2030.** **The likelihood of insolvency on those numbers is: [x] a low-level
possibility — and that is the same vocabulary [E3-24] uses for a case it says "would not distress
us."** What the reversal would destroy is the **equity value at $81.2 billion**, not the company.

- Likelihood of the DEATH mechanism: [ ] likely [ ] a real possibility [x] **a low-level
  possibility.** Likelihood of the **order book reversing** without killing the company: **a real
  possibility**, and it is a Q5/Q6 matter, not a Q4 one.
- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [x] UNKNOWABLE → see below**

**UNKNOWABLE, and the separating test is asked aloud as the framework requires: "Can I name the
document that would resolve this?"** **NO — and that is precisely why it is not UNRESEARCHED.**
The document that would resolve it is **the FY2026 and FY2027 Form 10-K**, i.e. three to five years
of filed statements under the post-2025 order book, satisfying [E2-42]'s *"not less than a
five-year test."* **Those documents do not exist yet.** Every filing that DOES exist is on disk and
has been read. **What specifically cannot be known: whether the 35–36% product gross margin, the
$444M of trailing owner earnings and the 17% operating margin are the level of this business or the
peak of a two-year demand shock — because the business has lived at that level for two quarters,
its own registrant deleted the physical unit series that would let an owner test price against cost
across the transition, and half its trailing operating cash arrived as refundable prepayments on
orders not yet delivered.**

**[E3-47] requires hesitating here and the hesitation is recorded:** *"our most egregious mistakes
fall in the omission, rather than the commission, category… their invisibility does not reduce
their cost."* **If Bloom compounds from here, this closed file is an error of omission, and it is
named as such in advance rather than excused afterwards.** What makes the closure cost nothing in
practice is Q5: at $275.75 there is no construction, filed or guided, that gets within a factor of
nine of the floor. **The file would close on price even if Q4 had cleared.**

**AND THE BRIEF'S THREE-WAY QUESTION, ANSWERED DIRECTLY: it is NEITHER the ORCL shape NOR the ARM
shape.**
- **NOT the ORCL shape.** ORCL failed because a contracted claim was contradicted by the filed
  balance sheet — *"contracted not to stop."* Bloom's balance sheet is the opposite: **net cash,
  zero-coupon debt, $7.3M of current maturities, 14.7x interest coverage.** Bloom carries a
  *related* ORCL defect — **$494.1M of filed performance obligations against $3.9–4.2bn of guided
  revenue, roughly 87% uncontracted** — but it is a Q2 problem about the order book's firmness, not
  a Q4 problem about solvency. **Bloom has no ORCL-style obligation it cannot stop.**
- **NOT the ARM shape, on the current year — but it IS the ARM shape over the life, and worse in
  kind.** ARM closed because **SBC consumed 96.6% of operating cash over its listed life**.
  Bloom's trailing ratio is **SBC $180,500k / OCF $737,784k = 24.5%** — better than CRWD 68.0
  (which closed that file), PINS 68.6, QLYS 24.9, and level with CRM 23.4 and SHOP 22.1. **On the
  current run-rate Bloom's stock discipline is unremarkable, not disqualifying.** But **over the
  whole listed life the ratio is not computable because the denominator is negative: FY2018 through
  H1 2026, Bloom generated NEGATIVE $145,920k of operating cash and paid its people $1,030,941k in
  stock.** ARM at least had cash for the stock to consume. **And Bloom adds a category ARM did not
  have: $324.4 million of stock paid to a CUSTOMER in a single quarter.** Adding it to trailing SBC
  gives **$504,900k of equity handed out against $737,784k of operating cash = 68.4%, which is the
  CRWD reading that closed that file** — though the warrant is properly capitalised and amortised,
  so charging it to one year overstates the accounting expense while stating the **cash-equivalent
  value transferred** correctly. **Both readings are recorded; neither is presented as the only
  one.**
- **What it IS: the HHH shape.** *"the filed history describes a different company than the cap
  prices"* — with two quarters where HHH had 26 days.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

# 🛑 COMPUTATION — NOT A CLEARANCE
**Operator rule 3.** Q2 returned OUT and Q4 returned UNKNOWABLE. **Q5 is not open and nothing
below is an entry signal, a ranking position, or a price at which this name becomes buyable.**
It is here because this queue requires every run to end with a price (operator instruction,
2026-09-01, rule 1) and because the brief asked, in words, what the buyer at this price is
paying for. **No entry language appears below and none may be inferred from it.**

### WHAT THE BUYER AT $81.2 BILLION IS PAYING FOR, IN WORDS
He is paying **$81,216 million** for a business that has earned its owners **negative $1.88
billion over the eight filed years to 2025-12-31** and **positive $444 million in the twelve
months to 2026-06-30**, of which **$337 million arrived as refundable customer prepayments on
boxes not yet delivered.** He is paying **26.1x trailing revenue** and **331x trailing GAAP net
income**, and **102x the midpoint of the FY2026 non-GAAP earnings per share the company guides on
a measure from which it says it cannot quantify the stock compensation it has removed.** He is
buying a manufacturing business whose **product gross margin did not move — 35.4%, 36.8%, 35.2%,
35.6%, 36.5% — while its revenue tripled**, whose **most recent quarter took 73% of its revenue
from one unnamed counterparty**, and whose stated competitive advantage is, in the registrant's
own words, *"relative ease in permitting and installation … when customers have an urgent need for
power"* — **that is, he is paying $81.2 billion for the duration of somebody else's
interconnection queue.**

**He is not paying for a fraud, a broken balance sheet, or a company at risk of failing.** He is
paying for four to seven years of grid dysfunction, priced as though it were permanent and as
though the cost curve would stop flowing to the customer, which on six years of Bloom's own filed
unit data it never has.

### THE ARITHMETIC
**1. THE YIELD.** Owner earnings ÷ market cap, every construction, against the sovereign:

| construction | owner earnings | **yield on $81,216M** | sovereign |
|---|---|---|---|
| **TTM to 2026-06, capex end** (the most favourable filed number in the file) | +$444.2M | **0.55%** | 5.35% |
| TTM at my disclosed (c) = $150M | +$407.3M | **0.50%** | 5.35% |
| **TTM net of the customer-deposit inflow** | +$106.8M | **0.13%** | 5.35% |
| **FY2021–25, the corpus default five-year window [E2-42]** | −$255.4M | **−0.31%** | 5.35% |
| FY2018–25, eight years | −$234.6M | −0.29% | 5.35% |
| *FY2026 guided non-GAAP operating income, midpoint — **not owner earnings**, stock compensation excluded* | *$850M* | *1.05%* | 5.35% |

**Every construction, filed or guided, is under 1.1%. The best one is 0.55%.**

**2. WHAT THE PRICE ALREADY ASSUMES.** Not a year-1 growth rate — a multiple, because the gap is
too large for a growth rate to be the honest framing. **To yield the bare sovereign of 5.35% this
price requires owner earnings of $4,345M: 9.8x the trailing figure. To clear the [E4-28] floor of
roughly 10% it requires $8,122M: 18.3x the trailing figure, and 2.6x TTM REVENUE.** What the
business has actually done: **negative owner earnings in eight of the nine measurable periods, and
a product gross margin flat to within 1.3 points across the largest demand shock in the history
of distributed generation.** **[E4-35] is the base rate this belief must face:** *"I would wager
you a very significant sum that **fewer than 10 of the 200 most profitable companies** in 2000
will attain **15% annual growth in earnings-per-share over the next 20 years**."* Getting to the
floor from here needs roughly **25% a year for a decade** and then a perpetuity at the bond. **The
burden of proof for that, in writing, against those odds, is not discharged by two quarters.**
**[E4-44]** caps it: *"the value of an asset … **cannot over the long term grow faster than its
earnings do**."*

**3. WHAT YOU ARE PAID.** At $275.75 the return is **0.55% against a 5.35% sovereign =
MINUS 4.80 PERCENTAGE POINTS.** On the corpus's five-year default window it is **minus 5.66
points.** **The buyer is paid nothing to own a manufacturer instead of a Treasury bond, and on
the framework's own default window he is paid less than nothing.**

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].**
- **Sovereign used: 5.35% — the bare rate. No per-name premium has been added**, and none may be:
  *"I tend to think that's kind of nonsense… It may look mathematical. But it's **mathematical
  gibberish**."*
- Certainty was handled **twice and neither place is the rate**: at Q1 (understanding — the
  mechanism is legible, so Q1 passed) and in the end discount below. **Windage count: ONE.** The
  only place conservatism is applied is the end margin; the inputs above are the filed figures.
  *(The (c) = $150M judgment is an input struck at the realistic level [E4-48] requires, not a
  second application of conservatism — it is 1.33x trailing capex on a line being doubled, which
  is realistic rather than punitive, and the deposit-net row is shown as a SEPARATE construction
  rather than folded in, precisely so that no number below stacks two haircuts.)*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — round numbers because *"a figure like '$71.84'
claims a precision this method cannot support"*:
- **Conservative: roughly $5 a share.** TTM owner earnings net of the deposit inflow ($106.8M)
  capitalised at the [E4-28] floor of 10%, plus net cash of ~$137M, over 294,527,346 shares.
- **Optimistic: roughly $20 a share.** Full credit for the guided FY2026 non-GAAP operating income
  of $850M, **less** the stock compensation that measure excludes (run-rating H1 2026's $100.4M to
  ~$200M) **less** (c) of $150M = ~$500M, capitalised at the same 10% floor, plus net cash. *No tax
  drag is applied, which is generous: Bloom paid $1.7M of cash income tax on $2.97bn of federal
  NOLs.*
- **CURRENT PRICE: $275.75.** **The price is roughly 14x to 55x the computed value.**
- **[E2-63] — name what bounds the upside, not just the yield.** It is bounded by the same thing
  that bounds every manufacturer: *"unless more capital is continuously invested."* Bloom's own
  plan is to double the line to 2 GW; its own filed record is that price per kilowatt fell faster
  than cost per kilowatt. **The upside is bounded by the gross profit per kilowatt, and that
  number peaked in 2018.**

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- **Floor verdict: honest pre-tax expectancy at $275.75 is 0.55% on the most favourable filed
  construction, against a floor of roughly 10%. BELOW THE FLOOR BY A FACTOR OF EIGHTEEN. QUIT ON.**
  *"that's the figure we quit on … that's true whether short rates are 6 percent or whether short
  rates are 1 percent."*
- **The lines below the floor are therefore NOT FILLED IN**, per the template's own instruction.
  No points-over-sovereign ranking, no position in the opportunity set, no ranking number.
  *"Take the best available, or nothing."*
- **This is the widest floor miss in the queue to date, and it is worth recording as a calibration
  point: Bloom would have to earn 2.6x its entire trailing revenue in owner earnings to become
  rankable at this price.**

**WHICH BAR? [x] NEITHER APPLIES, AND SAYING SO IS THE CORRECT ANSWER.**
- [ ] **Normal method [E4-11]** — not run. A margin of safety is applied to a value in order to
      decide an entry price. **There is no entry decision here: Q2 closed the file on the business
      and the floor miss is a factor of eighteen. Applying a margin would imply the exercise had a
      buy at the end of it.**
- [ ] **Screamer test [E4-01]** — run and answered, which is the one thing worth stating: the price
      is **far above the whole range**, which is [E4-01]'s third outcome, **"no."** Not *"inside the
      range — no useful conclusion"*; **above it, by an order of magnitude.**
- **Windage count: ONE**, stated above.

- **VERDICT: [ ] IN  [ ] UNRESEARCHED  [x] NOT OPENED — Q2 OUT and Q4 UNKNOWABLE close the file
  ahead of this question · ranking position: NONE, the name is not ranked, it is quit on [E4-28].**

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**THERE IS NO POSITION, SO THERE IS NO SELL RULE.** [E1-02] requires yardsticks *"prior to the
act"* and there is no act. **What Q6 records instead is the REVERSAL CONDITION — what would have
to appear in a future filing to make Q2 wrong — because per the QLYS ruling of 2026-09-07 a name
that failed on the business gets a reversal condition in words and NOT a price alert.**

**Pre-committed, and pre-registered now so it cannot be rationalised later [E4-26]:**
- **THE Q2 REVERSAL CONDITION — what would make me wrong about the moat, and it is one number.**
  **PRODUCT gross margin must rise materially and hold above roughly 45% for two consecutive full
  years**, on filed 10-K income statements, while product revenue grows. That is the only thing
  that can demonstrate what six years of filed unit data denied: that the cost curve is staying
  home rather than flowing to the customer. **Flat at 35–36% on rising volume is the reading that
  closed this file, and it is the reading that must change.** *Total* gross margin rising does not
  count — it moved from 14.8% to 32.0% on mix and the absence of impairments while the product
  line did not move at all, and that is the trap this file walked into and out of.
- **THE SECOND REVERSAL CONDITION, and it is a disclosure act rather than a number:** **Bloom
  reinstating a physical unit series** — megawatts accepted and product cost per kilowatt, or any
  successor metric that lets an owner divide dollars by a physical quantity. **[E2-49]** says the
  discarding of a yardstick is itself the finding; **the reinstatement would be the strongest
  possible counter-signal, and it costs management nothing if the numbers are good.** *Pre-registered
  so it cannot be rationalised away: if Bloom republishes cost per kilowatt and it has fallen while
  price has held, Q2 was wrong and this file must be reopened, not defended.*
- **THE Q4 RESOLUTION DATE — the document that does not yet exist, named with its date.** **The
  FY2026 Form 10-K, expected on or about 2027-02-09** (Bloom has filed its 10-K in the first half
  of February for four consecutive years: 2023-02-21, 2024-02-15, 2025-02-27, 2026-02-09). That
  filing gives a **third** full year in the new order book and the first audited full-year cash
  flow statement under it. **The FY2027 10-K, on or about 2028-02** brings the window to [E2-42]'s
  five-year minimum measured from the 2024 inflection. **Q4's UNKNOWABLE has a calendar, and it is
  2027 for a partial answer and 2029 for the framework's own default window.**
- **THE THESIS-BREAKING METRIC FOR THE BULL, PRE-REGISTERED AGAINST MYSELF:** **customer deposits.**
  They were $220,115k (2024-12-31) → $78,207k (2025-12-31) → **$360,568k (2026-06-30).** If the
  next two 10-Qs show that balance falling while revenue grows, the order book is being converted
  and the business is real. **If it falls while revenue falls, the death mechanism named at Q4 has
  started.** One line, two filings, no ambiguity.
- **Next catalyst date: the Q3 2026 10-Q and its EX-99.1, expected late October 2026** (2025-10-28,
  2024-10-29 precedents). **The single number to read first is the concentration paragraph in
  Note 1** — whether the 73% single-customer quarter repeats — **and the second is whether FY2026
  guidance is reaffirmed at $3.9–4.2bn.**

**The sell rule [E2-28] — recorded as inapplicable, with the reason, rather than left blank:**
- SELL if the market judges it more valuable than the facts indicate — **N/A, no holding. But
  noted: at 26.1x trailing revenue this condition is already satisfied on the facts this file
  found, which is why there is nothing to buy rather than something to sell.**
- SELL if funds are needed for something more undervalued or better understood — **N/A.**
- HOLD while: return on equity capital satisfactory / management competent and honest / market does
  not overvalue — **N/A. Of the three, the first is unproven (Q4) and the third fails (Q5).**
- *Price appreciation and holding period are **explicitly rejected** as reasons to sell.* **Noted,
  and it cuts the other way here: the fact that BE rose 26.9% in the nine days between the screen's
  frozen price and this run's is NOT a reason to do anything, and the queue's frozen cap is
  corrected at Step 0 for accuracy, not because the move means anything.**

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring
question: is this erosion an aberrational cycle, or has the business slipped in a way that
permanently reduces intrinsic value?

**Inverted, because there is no holding: is the IMPROVEMENT an aberrational cycle, or has the
business improved in a way that permanently RAISES intrinsic value?** That is [E3-30]'s question
run in the direction this file needs, and **[E4-17]** supplies the discipline: *"those beliefs
change quite gradually."* Two quarters is not gradual and it is not enough. **The counterweight,
recorded because [E2-40] is the other half of Q6:** *"we made an even more serious mistake in not
selling them … when our present views began to crystallize"* — **slow to conclude, fast once
concluded.** Nothing has crystallized here in Bloom's favour; if it does, in the filings named
above, the obligation is to act on it quickly rather than to defend this file.

**Do not trim winners [E5-14].** **Position size: ZERO.** *(No position exists. A capital-allocation
flag IS live — the $72.3M Oracle inducement at Q3 — which under [E4-13] would bind size downward if
there were a size to bind. There is not.)*

- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [x] N/A — no position, and Q2 closed the
  file. The reversal conditions above are recorded in words in place of a price alert, per the QLYS
  ruling of 2026-09-07.**

---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN → Q2 **OUT (closes the file)** →
      Q3 and Q4 recorded BELOW THE GATE under an explicit banner → Q5 headed **COMPUTATION — NOT A
      CLEARANCE** per operator rule 3 → Q6 recorded as a reversal condition. **No section below Q2
      claims to be a clearance and none can reopen Q2.**
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on
      filed income statements and a reconciled unit series. Q3 IN is written explicitly as *"the
      recorded absence of a found disqualifier"* per [E5-17], which is the framework's own wording,
      not a hedge.
- [x] **No UNRESEARCHED verdict was returned**, and the distinction was tested aloud at both
      non-IN verdicts. Q4's UNKNOWABLE names the document that would resolve it (**the FY2026 and
      FY2027 Form 10-K, dated at Q6**) and states that it **does not yet exist**, which is what
      makes it UNKNOWABLE rather than a work order.
- [x] **Every UNKNOWABLE states what specifically cannot be known** — Q4, in full: whether the
      35–36% product margin and $444M of trailing owner earnings are this business's level or a
      two-year peak, given two quarters of history, a withdrawn unit series, and 45.7% of trailing
      operating cash arriving as refundable prepayments.
- [x] **Step 0: the filing was read, with accession numbers, and a figure was cross-checked** —
      FY2025 OCF **$113,949k** on the filed statement against XBRL, plus SBC $139,406k, capex
      $56,759k and D&A $50,566k. **Eight 10-Ks, five 10-Qs (incl. the 10-Q/A), fourteen 8-K
      exhibits, three DEF 14As and the 424B4**, every accession recorded.
- [x] **Owner earnings on a multi-year mean; EIGHT windows published [E4-38]; the capex band
      disclosed as a judgment and the D&A end STRUCK OUT under [E5-20]** with the filing's own
      capacity-doubling language as the reason. (c) disclosed at ~$150M as a guess per [E2-23].
      **Stock compensation subtracted in full [E5-06], with [E3-70]'s floor caveat stated.**
- [x] **Competitor row filled — 7 SEC annual filers, same metric, same window, each with its
      accession — and the 5 unavailable named.** The moat is **NOT** marked PROVISIONAL, and the
      reason is stated in the file: the PROVISIONAL rule exists to stop a moat being *claimed* on
      an incomplete row, and here the row *denies* one while the missing names are all larger and
      better-capitalised. **Ballard excluded from the row with its form (40-F) and basis (IFRS)
      stated, rather than forced into a US-GAAP column.**
- [x] **Sovereign is for the earnings currency (USD, 81% of revenue), from the issuing authority
      (US Treasury daily par yield curve, 30-year), dated 2026-09-11, struck fresh.** FRED not used.
- [x] **Value stated as a round-number range** — roughly $5 to $20 a share — not a point estimate.
- [x] **One bar chosen — NEITHER, with the reason** — and the **windage count is ONE**, stated, with
      an explicit note on why the (c) judgment and the deposit-net row do not stack a second haircut.
- [x] **Prices dated; the aggregator flagged and used for the live quote only.** $275.75, close of
      2026-09-11. **The share count came off a filed cover, not an aggregator, and the charter
      question was settled by the filing rather than by summing.**
- [x] **Run committed to git after every question**, by file name, never `git add -A`.

## REGISTER
- **Verdict: [x] OUT (about the business), at Q2.** *(Q4, recorded below the gate, would
  independently have returned UNKNOWABLE; Q5, below the gate, misses the floor by a factor of
  eighteen. The file closes at Q2 and the register records that.)*
- **One line: Bloom's stated competitive advantage is the length of somebody else's
  interconnection queue, and its own filed unit series shows the customer taking 104% of six years
  of cost reduction while its product gross margin sat flat at 35–36% through a tripling of
  revenue — so there is no franchise, at $275.75 for $81.2bn against 0.55% of owner-earnings yield.**
- **If UNRESEARCHED — N/A. No UNRESEARCHED verdict was returned.** Every document named in the
  brief was on disk and read; no ladder rung was blocked; the only fetch this run performed was the
  seven peer 10-Ks/40-F for the competitor row and the Treasury curve.
- **If UNKNOWABLE (Q4, below the gate): what specifically cannot be known** — whether the trailing
  twelve months are the level or the peak of this business. The resolving documents are the
  **FY2026 10-K (~2027-02-09)** and the **FY2027 10-K (~2028-02)**, and they do not exist yet.

---
## PRICE AND PASS/FAIL — the queue's mandatory line (operator instruction, 2026-09-01)
**PRICE: $275.75** (close 2026-09-11, aggregator, flagged) **× 294,527,346 shares** (cover of the
10-Q/A for the quarter ended 2026-06-30, as of 2026-07-22, accession `0001628280-26-050325`) **=
CAP $81,216M.** Sovereign **5.35% USD**, US Treasury 30-year par yield, 2026-09-11.
**FAIL. The question that closed the file is Q2 — IS IT A FRANCHISE — and the verdict is OUT on
the business.** Owner-earnings yield at this price: **0.55%** on the single most favourable filed
construction in the file, **−0.31%** on the corpus's default five-year window, against a floor of
roughly 10%.

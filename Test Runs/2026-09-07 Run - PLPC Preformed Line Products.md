# Company Run — PREFORMED LINE PRODUCTS COMPANY (PLPC) — 2026-09-07
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

---
## THE SCREEN ROW THAT PROMPTED THIS RUN — a prompt to read, never a score (operator rule 8)

```
cap_m 1900 | oe_bottom_m 27 | oe_top_m 58 | spread 1.096
yield_bottom 1.44% | vs_sovereign -3.80 pts | growth_required 8.56%
level_shift 2.68  STEP UP - normalize down [E4-41]
best_year_dep 0.154 | acq_note: (none) | da_note: (none)
newest_filing 2025-12-31
```

Every one of those numbers is re-derived below from the filed statements. Where the
re-derivation disagrees with the row, the filing governs (operator rule 4).

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.24 %** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-year
  (the issuing authority; FRED DGS30 is the fallback, not the source)**
- FX: PLPC reports in USD and roughly two-thirds of revenue is domestic. It is nonetheless a
  materially foreign-earning filer (see Q1) — the currency exposure is recorded at Q4, not
  handled by swapping the sovereign, because **the reporting and dividend currency is USD**.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K FY2025**, period 2025-12-31, filed **2026-03-05**, accession **0000080035-26-000007**
  - **10-Q Q2 2026**, period 2026-06-30, filed 2026-07-30, accession **0000080035-26-000030**
  - **DEF 14A**, filed 2026-03-20, accession **0000080035-26-000011**
  - **10-K FY2024** accession 0001628280-25-012640 · **FY2023** 0000950170-24-028605 ·
    **FY2022** 0000950170-23-006020 · **FY2021** 0000950170-22-002892 ·
    **FY2020** 0001564590-21-011273
- figure cross-checked against the filed statement: **see the cross-check block below.**

**SHARE COUNT — read off the cover of the LATEST periodic filing, not the 10-K.**
`python Screens/cover_shares.py PLPC`:
```
PLPC  PREFORMED LINE PRODUCTS CO
   10-Q filed 2026-07-30, period 2026-06-30, accession 0000080035-26-000030
   Common Shares, $2 par value per share                 4,888,701
```
**ONE class only.** The tool's refusal to sum classes does not bite here; the charter question
does not arise. 4,888,701 shares — this is a genuinely tiny share count and it matters at Q3
and Q6 (thin quote).

**Price:** **$398.45**, 2026-09-04 close, Yahoo Finance — *aggregator, used for the live quote
only, and flagged as the protocol requires.* Market cap **$1,948M**.

*(Price history, same source, for the record: ~$128 Oct-2024, ~$142 May-2025, ~$206 Dec-2025,
~$398 Sep-2026. The quote has roughly tripled in fourteen months. Nothing in the filed
statements tripled. This is recorded here, not at Q5, because it is a fact about the price.)*

---
## CROSS-CHECK — tagged data against the filed statement (operator rule 4)

Companyfacts XBRL against the **Statements of Consolidated Cash Flows, FY2025 10-K page 33**
(accession 0000080035-26-000007):

| line | XBRL | filed statement | agree |
|---|---|---|---|
| Net cash provided by operating activities 2025 | 73.47 | **$73,467** | yes |
| ... 2024 | 67.48 | **$67,480** | yes |
| ... 2023 | 107.64 | **$107,642** | yes |
| Capital expenditures 2025 | 40.13 | **$(40,132)** | yes |
| Depreciation and amortization 2025 | 23.03 | **$23,030** | yes |
| Share-based compensation 2025 | 4.96 | **$4,955** | yes |

The tagged series is transcription and it transcribed correctly. It is still not the evidence
**[E3-27]** — the detail lines below are, and they are where this run's judgments come from.

**The D&A series, printed raw and eyeballed** — the brief asked for this because `da_note` is
empty and the flag has a $5M materiality floor that a company this small could hide a real
break under. Filed D&A, $M: 2013 **12.09** · 2014 **12.86** · 2015 **11.53** · 2016 **12.00** ·
2017 **12.79** · 2018 **12.44** · 2019 **13.75** · 2020 **13.84** · 2021 **15.56** ·
2022 **16.43** · 2023 **18.91** · 2024 **20.83** · 2025 **23.03**. Thirteen years, monotone
after 2018, largest single step +2.5 (2022→2023). **No discontinuity. The empty `da_note` is
correct here** — the flag did not miss anything. *(Recorded because the brief was right to
ask; a negative finding checked is worth writing down.)*

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.**

PLPC makes the small metal and plastic parts that hold a cable onto a structure and keep
water out of a splice. The signature product is a helix: a stiff wire coiled into a spiral
that grips a conductor by wrapping around it, so a lineman can terminate or support a cable
by hand, up a pole, in weather, without tools or torque specs. Around that sit string
hardware, insulators, connectors, vibration dampers, wildlife guards, and — the other half of
the company — plastic splice closures that seal a fibre joint against the outdoors.

The economics of the part are the economics of a cheap component with an expensive
consequence. A deadend costs the utility tens of dollars. The conductor it holds costs
millions per mile and the outage it prevents costs more than either. So the buying decision
is not made at the moment of purchase. It is made **years earlier**, when the utility's
engineering standard names an approved part and the part goes into the construction
specification. After that, a crew orders it from a distributor and it ships from stock —
*"Most orders can be shipped within a two to four-week period"* (FY2020 10-K, Backlog Orders).
Backlog at end-2025 was $232.8M on $669.3M of sales — **about four months of revenue** — and
the 10-K says the company *"does not have a wide variation in sales from quarter to quarter."*

So the revenue is **replenishment against somebody else's construction and maintenance
programme**, not project tender. It behaves like a consumable with a catalogue. But the
customer's own budget is a capital budget — utility transmission-and-distribution spend and
telecom fibre-to-the-home build — so **the volume is a derivative of another industry's capex
cycle.** That is the answer to the brief's first prior, and it is not a matter of inference:
the filed backlog series prints the cycle directly (Q2 below).

Who buys: *"public and private energy utilities and communication companies, cable operators,
governmental agencies, contractors and subcontractors, distributors and value-added
resellers."* Concentration is low and falling — the largest customer was **12.5% of revenue in
2022, 11.6% in 2023, 11.1% in 2024, 10.7% in 2025** (each 10-K, Item 1).

Revenue by product, FY2025 / FY2024 / FY2023 (10-K Item 1): **Energy 71% / 71% / 64** ·
**Communications 22% / 22% / 29%** · **Special Industries 7% / 7% / 7%**. Revenue by
geography, FY2025 (MD&A): PLP-USA **$312.6M**, Asia-Pacific **$114.8M**, EMEA **$133.1M**,
The Americas **$108.8M**. **Roughly 53% of sales are outside the United States**, made in 26
plants in 20 countries. That is not an export model; it is local manufacture for local
utilities, which is why the plants exist at all.

**The scarce input this business controls.**

It is **not** the raw material. Galvanized wire, stainless, aluminium rod and plastic resin are
commodities, and the 10-K says so: *"multiple sources of supply,"* *"a number of reliable
suppliers."* PLPC is a price-taker on input.

What it controls is the **specification position**, and the filing quantifies it rather than
asserting it: **75 US and 104 international patents in 21 countries**, 38 US and 97
international applications pending; **35 US and 242 international trademark registrations in
47 countries**; a **38,000-square-foot Research and Engineering Center** whose vibration,
tensile and environmental testing the company calls *"one of the most sophisticated in the
world in its specialized field"*; and *"a long-standing leadership role in many key
international technical organizations which are charged with the responsibility of
establishing industry-wide specifications and performance criteria, including IEEE, CIGRE and
IEC."* The company sits on the bodies that write the standard its parts are then tested
against. Alongside that: 26 plants inside the markets they serve, which is what lets it be
the supplier called at 3am after an ice storm.

Note what this is **not**: it is not a cost advantage. PLPC's advantage, if it is one, is on
the approval and service side, not the manufacturing-cost side. That distinction decides Q2.

**Will the fundamentals look broadly the same in ten years?**

For the Energy 71%: yes. Conductors will still be hung on structures, they will still gallop
and vibrate, and the parts that stop them will still be helices and dampers. The physics does
not have a software substitute.

For the Communications 22%: **not entirely, and the filing says so first.** The 10-K's own
risk list names *"technological developments that affect longer-term trends for communication
lines, such as wireless communication"* and *"the decreasing demand for product supporting
copper-based infrastructure."* This is a real, named, management-disclosed erosion vector on
roughly a fifth of revenue. It is carried into Q2 as a moat question and into Q6 as the
monitoring metric, not waved away here.

**[E4-46] check** — *"if we can't make a decision in five minutes, we can't make it in five
months."* This business took five minutes. There is no unconsolidated vehicle, no float, no
percentage-of-completion, no capitalised development, no adjusted-earnings bridge. One share
class, one auditor, thirteen years of clean tagged data that ties to the filed statements.
Whatever kills this run, it will not be that the business is unintelligible.

- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**This is the gate the brief said would be hard, and it was. Most of the evidence is in PLPC's
own Item 1, and it runs both ways. I put the strongest version of each side down before writing
a class [E4-51].**

### [E3-03], the three criteria, against the company's own words

**(1) Needed or desired — YES, without qualification.** You cannot build or maintain an
overhead line without this class of part. Demand is not discretionary and cannot be met by
doing without.

**(2) "Thought by its customers to have no close substitute" — the company says otherwise, in
Item 1, in its own voice, in every vintage read (FY2020–FY2025):**

> *"All of the markets that the Company serves are highly competitive. In each market, **the
> principal methods of competition are price, performance, and service.**"*

> *"Domestically, there are **several competitors for formed wire products.** … However, the
> Company's formed wire products **compete against other pole line hardware products
> manufactured by other companies.**"*

> *"The OSP closure market is **one of the most competitive product areas for the Company**,
> with a number of primary competitors and several smaller niche competitors that **compete at
> all levels in the marketplace.** The Company believes that it is **one of four leading
> suppliers** of OSP closures."*

Three concessions are in those sentences. **Price is named first** among the methods of
competition. The core product competes not only against copies of itself but against a
different mechanical solution to the same problem — *other pole line hardware*. And on the 22%
of revenue that is Communications, the company places itself as **one of four**, in what it
calls one of its most competitive product areas.

Against that sits the one dominance claim it does make, unchanged in all six 10-Ks read: *"The
Company believes that it is **the world's largest manufacturer of formed wire products** for
energy and communications markets."* That is a real claim and I do not dismiss it. But note its
scope — **largest maker of one product family**, not sole maker — and note that the very next
sentence says that family competes against other hardware.

**(3) Not subject to price regulation — YES, and the answer has an edge.** PLPC's prices are
not regulated. Its **customers'** are. A regulated utility passes hardware cost into rate base,
which softens price resistance; the same regulation imposes prudency review and competitive
procurement, which hardens it. **[E2-59]** governs: regulation *floors* a commodity business
and *caps* a franchise, and *"neither creates the class."* No franchise credit is taken here.

### [E4-04] — must the moat be rebuilt, or merely defended?

**Split, and the split matters.** The patent estate — **75 US and 104 international patents in
force in 21 countries, with 38 US and 97 international applications pending** — is by
construction a **rebuilt** moat: *"U.S. patents are issued for terms of 20 years … U.S. and
international patents are **not renewable after expiration of their initial term.**"* The
company must keep filing to stand still.

But the patent estate is not the load-bearing asset, and the filing is candid about it: the
company *"does not believe that **any single patent, or group of related patents, is essential
to the Company's business as a whole**."* The load-bearing asset is the **approval and
specification position** — the IEEE/CIGRE/IEC standards seats, the 38,000-sq-ft test
laboratory, the 35 US and **242 international trademark registrations in 47 countries**
(trademarks *are* perpetually renewable), and the fact that once a utility's engineering
standard names a part, it is not revisited for years. That is **defended, not replaced** —
[E5-23]'s *"working at improving your own moat … all of the time"*, not [E4-04]'s exclusion.

**[E4-23] key-person check: NO defect found.** Nothing in the filing makes the moat contingent
on a named individual. The family-control question below is a governance matter, recorded at
Q3, not a moat defect. **This is recorded here rather than at Q3 precisely so a warning about
the business cannot be read as a compliment to the person.**

**[E4-36], which of the four causes?** Not a nonlinear combination. Partly **wave-riding**, and
the wave is visible in the filed backlog below. The durable part is closest to **extreme
performance on one variable**: seventy-nine years of doing one narrow mechanical thing and
being the world's largest at it.

### THE INSTRUMENT THE BRIEF ASKED FOR — [E4-55], and what PLPC actually files

The brief said [E4-55] should be live here in a way it was not for software: *"Where units
exist, monitor units … Dollar revenue flattered by pricing is how a shrinking franchise hides;
the physical series is the honest one."*

**The finding is mixed, and it needs stating exactly.**

**There is NO unit-volume series. The brief's expectation was wrong.** I searched all six
10-Ks (FY2020–FY2025) for *pounds, tonnage, tons, metric tons, units shipped, unit volume,
kilometers, linear feet*. **Zero hits outside the raw-materials paragraph.** PLPC files no
shipped-unit count, no weight, no capacity figure and no ASP. Its MD&A discusses volume in
every vintage — *"higher volumes in communications and energy product sales,"* *"lower volumes
… due to customer destocking"* — and **never quantifies it once.** On the strict [E4-55]
instrument, **PLPC is in the same position as KLAC and QLYS: the honest series does not exist.**
That is the answer to the brief's expectation that a hardware manufacturer would file one. It
does not. *(And the peer row below sharpens the point: **Hubbell does** — it quantifies price
and unit volume separately in its MD&A, in words, every year. The disclosure is available in
this industry. PLPC chooses not to make it.)*

**But three non-dollar or non-revenue series DO exist, and one of them is the best cycle
instrument this queue has found on a small industrial:**

| year-end | **order backlog $M** (firm orders, Item 1) | employees | mfg plants |
|---|---|---|---|
| 2019 | **111.2** | — | — |
| 2020 | **115.1** | 2,969 | — |
| 2021 | **242.9** | 2,927 | — |
| 2022 | **379.4** | 3,261 | — |
| 2023 | **172.6** | 3,520 | 26 |
| 2024 | **191.0** | 3,401 | 25 |
| 2025 | **232.8** | 3,734 | 26 |

Backlog is dollar-denominated, so it is not immune to the price flattering [E4-55] warns
about. It is nonetheless **not revenue**: it is firm orders not yet shipped — *"All customer
orders entered are firm at the time of entry"* — and it leads revenue by roughly four months
(232.8/669.3 x 12 = 4.2 months). And it prints, with no interpretation required, the thing the
brief asked me to test:

**Backlog x3.3 in two years (115.1 → 379.4), then −55% in a single year (379.4 → 172.6), then
two years of partial recovery.** The filer names the mechanism itself, in the FY2023 10-K:
*"The Company's order backlog **has returned to more normalized levels as a result of the
inventory destocking that has occurred**, primarily in the communications markets."*

**That settles the brief's second mandatory correction.** The `level_shift 2.68 STEP UP` flag
is pointed at a real event but has the event wrong. This is not a new level. It is a
**double-order-and-destock cycle** riding on a grid and fibre capex wave: customers over-ordered
into the 2021–22 shortage, then stopped ordering in 2023–24 while working off their own
shelves. [E4-41] requires favourable exogenous breaks in the window to be **named and removed
before the mean is trusted**, and this one is named by the filer, in its own 10-K, in words.

### THE PASS-THROUGH TEST — the sharpest instrument available, and it REFUTES my prior

The brief's bear case was *"commodity metal-bashing with no pricing power."* The test it named
was gross margin through the input-cost spike. **The test was run and the bear case loses it.**

**Consolidated gross margin, filed, %:** 2016 **32.5** · 2017 **31.4** · 2018 **31.4** ·
2019 **31.6** · 2020 **33.0** · 2021 **32.1** · 2022 **33.8** · 2023 **35.1** · 2024 **32.0** ·
2025 **31.2**

**PLP-USA segment gross margin, filed** — the clean read, because there is no FX in it and it
is where the tariffs and the LIFO charge land: 2020 **37.3** · 2021 **34.1** · 2022 **38.0** ·
2023 **40.2** · 2024 **34.9** · 2025 **33.9**

**2021–2023, the input-cost spike.** The US segment gave up **3.2 points in 2021**, then took
back **3.9 in 2022 and a further 2.2 in 2023** — ending the episode **6.1 points above where it
started**. The company narrated the mechanism in advance, in the FY2021 10-K: *"To offset these
increased costs, the Company implemented several price increases in the U.S. and
internationally in 2021. **Due to the large volume in the Company's backlog, tailwinds from
these increases are expected in 2022.**"* **The pass-through is complete, and it lags by about a
year — exactly the lag a four-month firm backlog priced at order date would produce.**

**2025, the tariff shock — the harder test, and the more impressive answer.** The FY2025 10-K
discloses **$15.1M of tariff cost** and **$9.0M of LIFO valuation charges**, both attributed to
PLP-USA. That is **$24.1M against $312.6M of PLP-USA revenue — a 7.7-point cost shock in one
year.** PLP-USA gross margin fell from 34.9% to **33.9%**: a **1.0-point** give. Held at the
2024 margin, 2025 PLP-USA gross profit would have been $109.1M; it was **$105.9M**. **PLPC
absorbed $3.2M of a $24.1M shock and passed through roughly 87% of it inside twelve months.**

**A business with no pricing power does not do that.** My prior was wrong, the brief invited me
to say so [E4-26], and it is said. **This is the single strongest fact in PLPC's favour in this
run.**

**Now the counterweight, which belongs in the same breath.** Passing *cost* through is not
taking *price*. **[E2-44] half one** asks whether the business can raise prices *"even when
product demand is flat and capacity is not fully utilized."* The 2024 test — PLP-USA revenue
**−23%**, gross margin **−5.3 points** — cannot answer it, because the filing attributes the
fall to *"lower sales volumes and unfavorable product mix"*, which is fixed-cost absorption
inside COGS, not price. **So half one is not evidenced either way and I do not claim it.** And
**[E4-37]**'s inverse metric fires quietly in every single vintage: the 10-K has said, FY2021
through FY2025 without a break, that *"any price increases **may have a negative effect on
demand.**"* That is not the yawn end of the scale.

**[E2-44] half two — grow dollar volume "with only minor additional investment of capital" —
FAILS, and not narrowly.** Revenue 2018 → 2025 rose **59%** ($420.9M → $669.3M). Shareholders'
equity over the same window rose **91%** ($249.4M → $475.5M); total assets **82%**. Cumulative
capex 2018–2025 was **$212.7M against $134.8M of depreciation — 1.58x.** Growth here is bought,
not thrown off.

### [E3-46] — the second question about the business, and it is a number

*"the best businesses, by definition, are going to be businesses that earn **very high returns
on capital employed over time**."*

Return on **beginning** shareholders' equity, and on beginning net **tangible** equity (goodwill
and identified intangibles removed per **[E2-43]**), from filed figures:

| | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | **mean** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **ROE %** | 5.1 | 2.7 | 7.0 | 5.7 | 11.1 | 9.3 | 11.1 | 12.2 | 17.2 | 17.7 | 8.9 | 8.4 | **9.7** |
| **ROTE %** | 5.7 | 3.2 | 8.0 | 6.4 | 12.5 | 10.3 | 13.2 | 14.4 | 18.9 | 19.2 | 9.6 | 8.9 | **10.9** |

**Twelve years; mean 9.7% on equity and 10.9% on tangible equity; the only two strong years
(2022–23) sit exactly on the backlog peak.** That is not *"very high returns on capital employed
over time."* It is a decent, cyclical, high-single-digit return that has spent as much time
below 9% as above 12%.

**And the incremental is worse than the average** — the [E2-56] test, judge retention
incrementally and never on the blended return. Between 2018 and 2025, both off-peak years:
**equity +$226.1M, net income +$8.7M — a 3.8% return on the incremental equity over seven
years.** On the trailing twelve months to 2026-06-30 (net income **$43.1M** = FY2025 $35.283M −
H1-2025 $24.222M + H1-2026 $32.032M) the incremental improves to **6.7%**; on an annualised
H1-2026 run rate it would improve a great deal more. **The honest statement is that the
incremental return depends entirely on whether 2026 is the new level or the next peak** — and
the backlog series above is the reason to doubt it is the new level.

### [E2-58] — the commodity doctrine, and the route the brief asked me to test

*"persistent over-capacity without administered prices (or costs) equals poor profitability"*,
with one exception: *"a cost advantage that is both **wide and sustainable** … By definition
such exceptions are few."*

**Over-capacity: the company discloses it.** Item 2, FY2025: *"The extent to which we utilize
our properties varies by property … **Most of our manufacturing facilities remain capable of
handling volume increases.**"* Spare capacity, stated, across 26 plants.

**Administered prices: none.** No regulation, no cartel, and the one live government
intervention runs **against** the company at $15.1M of tariff cost.

**And the cost-advantage exception — PLPC does not claim it, so I will not claim it for them.**
The five competitive advantages Item 1 lists are *a strong and stable workforce*, *the Research
and Engineering Center*, *vertical integration*, *"an extra measure of service in cases of
emergency, storm damage"*, and *proximity to customers worldwide*. **Four of the five are
service and engineering claims. One — vertical integration — is a cost claim, asserted with no
number attached.** Nothing in any of the six 10-Ks quantifies a unit-cost advantage over anyone.

**So the [E2-58] rescue route is not available on the evidence, and that is a different failure
from the one the brief anticipated.** The QLYS ruling of 2026-09-07 held that the
wide-and-sustainable cost advantage rescues *profitability* without granting *franchise entry*.
**PLPC does not reach that door: it has no filed cost advantage to be rescued by.** What it has
instead is a **spend-to-hold** position, and the income statement prices it. FY2025: gross
profit **$208.5M (31.2% of sales)**, costs and expenses **$153.4M (22.9%)**, operating income
**$55.1M (8.2%)**. **Roughly three-quarters of the gross margin is consumed by the selling,
engineering and administrative machine that produces the approval position in the first
place.** The advantage is real. It is being spent, not banked. And **[E3-62]**'s second step —
*"how much is going to stay home and how much is just going to flow through to the customer"* —
is answered by the peer row below: the gross margin is competitive; the operating margin is
not.

### [E2-53] dominance / [E3-33] untapped pricing power / [E4-32] direction

- **[E2-53] dominance class — NO.** *"Once dominant, the newspaper itself, not the marketplace,
  determines just how good or how bad the paper will be."* PLPC's own words put the marketplace
  in charge: *"the principal methods of competition are price, performance, and service."*
- **[E3-33] untapped pricing power — NO, and [E5-28] forecloses the claim.** *"If you name some
  business that has incredible pricing power, you're talking about a business that's a monopoly
  or a near monopoly."* PLPC is one of *several* in formed wire and **one of four** in OSP
  closures, by its own count. The class cannot be claimed.
- **[E4-32] direction — FLAT, on the only continuous metric available.** Consolidated gross
  margin was **32.5%** in 2016 and **31.2%** in 2025; the ten-year line is flat to slightly
  down. Revenue per employee moved from **$157k** (2020) to **$179k** (2025) — roughly US
  inflation. **The moat is not visibly widening.** It is also not visibly narrowing, which is
  the honest other half, and the reason this verdict is a close one.

---

## THE COMPETITOR ROW — required [E3-28]. A moat is a claim about *relative* position.

**Peers taken: 6 named below, plus one acquired comparable, from an industry with no clean
count.** PLPC has no single-name public pure comparable — nobody else is a listed
formed-wire-and-splice-closure company. I therefore took the six listed manufacturers that sell
engineered hardware into the same two customer pools (electric utility T&D, and telecom
outside-plant), plus Encore Wire for the pre-acquisition years. **Buffett says eight [E3-28];
this industry does not have eight listed comparables, and I say so rather than padding.**

**Same metric, same window, filing-sourced (SEC XBRL companyfacts, cross-checked to filed
statements for PLPC and Hubbell). Window: fiscal 2019–2025, seven years.** Fiscal-year labels
are the filer's own: HUBB/VMI/NVT/PLPC are December; **AZZ is February-end**, **ATKR is
September-end**, **THR is March-end** — so their "2025" covers a different twelve months, which
is stated rather than silently aligned.

| Company | gross margin, 7yr mean | **operating margin, 7yr mean** | op margin FY2025 | ROE on beginning equity, 7yr mean | revenue CAGR 19→25 |
|---|---|---|---|---|---|
| **PLPC (subject)** | **32.7%** | **9.3%** | **8.2%** | **12.1%** | **7.0%** |
| Hubbell (HUBB) | 31.4% | **16.0%** | **20.7%** | **24.4%** | 4.1% |
| nVent (NVT) | 38.8% | 14.0% | 15.8% | 12.4% | 9.9% |
| Atkore (ATKR) | 32.8% | 18.5% | 0.8% | 75.2% *(post-LBO equity; not comparable)* | 6.8% |
| Thermon (THR) | 42.3% | 11.1% | 16.0% | 6.9% | 3.8% |
| AZZ | 23.1% | 11.2% | 15.0% | 8.4% | 8.6% |
| Valmont (VMI) | 27.6% | 9.2% | 10.1% | 17.2% | 6.8% |
| Encore Wire (WIRE) | *acquired by Prysmian 2024; series ends FY2023* | 17.6% (FY23) | — | 20.5% (FY23) | 19.1% (19→23) |

**Sources:** SEC XBRL companyfacts for each CIK, annual (10-K, ~365-day) facts only. Hubbell
segment figures read from the filed FY2025 10-K MD&A. ATKR's ROE is computed on an equity base
that was negative or near-zero after its LBO and is **not comparable** — it is shown because
suppressing it would be selection, and it is labelled rather than used.

### WHAT THE ROW SAYS, AND IT IS NOT WHAT I EXPECTED

**1. PLPC's gross margin is fully competitive. Its operating margin is the worst in the row.**
32.7% gross against a peer set spanning 23.1% to 42.3% — PLPC sits in the middle, above
Valmont and AZZ. But **9.3% operating margin against a peer mean of 13.5%**, and it is last or
second-last in every single year. **The gap is entirely below the gross line.** That is the
[E3-62] answer in one number: whatever advantage the approval position confers shows up in
price realisation (gross margin), and is then spent on the selling, engineering and
administrative apparatus before it reaches the owner.

**2. The nearest true competitor earns two and a half times PLPC's operating margin on the same
customers.** **Hubbell's Utility Solutions segment** — of which **Grid Infrastructure is
$2,748.2M of $3,672.3M** — sells connectors, pole line hardware and substation fittings to US
utilities. Filed segment operating margin: **21.4% (2023), 20.3% (2024), 21.5% (2025)** GAAP.
PLPC company-wide: **12.6%, 8.5%, 8.2%.** Hubbell's Grid Infrastructure business alone is
**four times PLPC's entire revenue.**

**3. And Hubbell can do the thing [E2-44] half one asks about, in writing, where PLPC cannot be
shown to.** Hubbell's FY2025 10-K: Utility Solutions organic growth came from *"a **low single
digit increase in price**, partially offset by a **low single digit percentage decrease in unit
volumes**"* — and margin expanded 120bp. **A price increase taken and held into falling unit
volume, disclosed as such.** In FY2024 it did the same thing: *"a mid single digit percentage
decrease in unit volumes partially offset by a low single digit increase in price
realization."* **PLPC files no equivalent sentence in any vintage.** This is [E2-44] half one
passed by the competitor and unevidenced by the subject, on the same metric in the same window
— which is exactly what the competitor row exists to surface.

**4. Nobody names PLPC.** EDGAR full-text search (which covers 2001 onward), phrase *"Preformed
Line Products"*: **1,455 substantive filings across 65 registrants**, and after removing fund
holdings (NPORT-P 27,471 hits, 13F-HR 1,868, N-PX 1,786) and PLPC's own filings, **the
industrial mentions are almost entirely compensation peer groups** — AZZ names it in thirteen
consecutive DEF 14As and never in a 10-K; CECO Environmental the same; HNI, Sterling
Construction, Mosaic, RG Barry, Rocky Brands, Invacare all in proxies only. **Optical Cable
Corp** names it in 10-Ks and 10-Qs from 2008 to 2015 — following an 8-K of 2008-06-02 carrying
a purchase agreement as exhibit 2.1, i.e. **as the seller of a divested business, not as a
competitor.** **Hubbell, Valmont, nVent, Atkore, Thermon and Encore Wire name Preformed Line
Products in zero filings of any type.** In an industry that does not name competitors at all —
Hubbell's own competition section says it *"cannot specify with precision the number of
competitors in each product category or their relative market position"* — this is weak
evidence rather than none, and I grade it that way: **it does not show PLPC is unimportant; it
shows PLPC is not important enough to be named by the people who would know.**

**5. The row's own limit, stated [E3-61].** *"In some businesses, the participants behave like a
demented Kellogg. In other businesses, they don't … I think you'd have to know the people
involved."* The row shows position. It cannot show conduct. Nothing here predicts whether these
seven firms will compete rationally in the grid build-out now in front of them, and the corpus
says even Munger had no model for that.

**6. And what the row does in PLPC's favour, because it must be said [E4-26].** PLPC's **gross
margin has been more stable than any peer's**: a 3.9-point range (31.2–35.1) over seven years,
against Atkore's **25.9 → 41.9 → 23.7** and Encore Wire's **13.0 → 36.9**. Two of these
"peers" are commodity converters whose margins are a spread on copper and steel; PLPC's plainly
are not. **On the [E2-58] question of whether this is a commodity business, the row answers
NO** — PLPC's margin series does not look like a commodity converter's. It looks like a
differentiated small manufacturer that cannot get operating leverage.

### THE Q2 VERDICT

- **Class: NARROW.** · **Direction: FLAT** — not widening on any continuous filed metric, not
  visibly narrowing either, with one named erosion vector (copper/wireless substitution) live on
  ~22% of revenue by management's own risk disclosure.
- **VERDICT: [x] OUT — on [E3-03] criterion (2), and secondarily on [E2-44] half two and
  [E3-46].**

**THE CASE FOR IN, STATED AS WELL AS I CAN STATE IT [E4-51].**

> PLPC has been **the world's largest manufacturer of formed wire products** for decades and
> says so in every 10-K. It holds **179 patents and 277 trademark registrations across 47
> countries**, sits on the IEEE, CIGRE and IEC committees that write the specifications its
> parts are tested against, and runs a test laboratory it calls *"one of the most sophisticated
> in the world in its specialized field."* Its parts are cheap, its customers' failure costs are
> enormous, and its products are written into utility engineering standards that are not
> revisited for years. **It passed through 87% of a 7.7-point tariff-and-LIFO cost shock inside
> twelve months**, and it recovered the entire 2021 input-cost spike within two years with three
> points to spare. Its gross margin is the most stable in its peer row. It has **26 plants in 20
> countries** so it can supply a storm-restoration order locally, in a business where the
> alternative to *supply now* is a dark grid. Twelve-year mean ROTE of **10.9%** is not a bad
> business; it is [E4-20]'s **good** account, and [E4-43] says the good class **passes**.

**Why it still does not carry the gate.**

1. **Criterion (2) is a question about what customers think, and the only filed answer is the
   company's own, given six times: the markets are "highly competitive" and the first named
   method of competition is "price."** A product *"thought by its customers to have no close
   substitute"* does not get described that way by the firm that sells it — least of all when
   the same paragraph concedes that its flagship *"compete[s] against other pole line hardware
   products manufactured by other companies"* and places it as **one of four** in its second
   business.
2. **[E2-44] half two fails outright and half one cannot be evidenced.** 59% more revenue
   required 91% more equity and 1.58x depreciation in capex. And [E4-37]'s inverse metric —
   *"the agony they go through in determining whether a price increase can be sustained"* —
   fires in every vintage, in the same sentence each time: *"any price increases may have a
   negative effect on demand."*
3. **[E3-46] answers in a number and the number is 9.7%.** Twelve years, mean ROE 9.7%, mean
   ROTE 10.9%, with the incremental return on the last seven years' retained equity at
   **3.8%**. The corpus asks for *"very high returns on capital employed over time"* and this
   is not that.
4. **The competitor row makes the position relative, and relatively PLPC is last.** 9.3% mean
   operating margin against Hubbell's 16.0% and a 13.5% peer mean, on a gross margin that is
   mid-pack — the shortfall is all operating leverage. **[E2-58]'s one exception is a cost
   advantage that is wide and sustainable, and PLPC files no cost advantage at all.** It has a
   service and approval advantage that costs 22.9% of revenue a year to keep.
5. **[E4-55] cannot be run and the absence is not neutral here, because a peer runs it.**
   Hubbell separates price from unit volume in words every year. PLPC has never quantified
   volume in any vintage. The honest series does not exist, and the framework does not grade an
   unmeasurable moat IN.

**WHAT WOULD FLIP THIS VERDICT, NAMED IN ADVANCE SO IT IS FALSIFIABLE.** Any one of:
**(a)** consolidated operating margin at or above **13%** for three consecutive years, which
would mean the approval position is finally reaching the owner rather than the cost base;
**(b)** a filed unit, tonnage or ASP series in any vintage, so that [E4-55] becomes runnable;
**(c)** a disclosed list-price increase taken and held into a year of flat or falling volume,
which is [E2-44] half one; or **(d)** backlog holding above **$230M for eight consecutive
quarters**, which would convert the 2021–25 swing from a cycle into a level. **Each is a
document I can name, so this verdict is reviewable — but it is OUT and not UNRESEARCHED,
because every document that exists has been read and they answer the question as it stands.**

**Q2 CLOSES THE FILE. Everything below this line is recorded because the operator's brief asked
for it and because a closed file still owes the register its findings. None of it is a verdict,
and per operator rule 2 none of it can promote the name.**

---

# TESTS RUN BELOW THE CLOSED GATE — RECORDED, NOT VERDICTS

Q2 returned OUT. Per operator rule 2 the file is closed and **nothing below promotes the
name.** It is written because the operator's brief commissioned specific work, because a closed
file still owes the register its findings, and because three of the items below are **defects in
the tooling that will affect other runs.**

## A. OWNER EARNINGS — THE SIX-WINDOW REBUILD THE BRIEF DEMANDED
### **COMPUTATION — NOT A CLEARANCE**

Method, per the standing convention: **owner earnings = operating cash flow − share-based
compensation − (c)**, where (c) is the disclosed judgment **[E2-23]**. All figures from the
**filed** Statements of Consolidated Cash Flows (FY2020 10-K `0001564590-21-011273`, FY2022
10-K `0000950170-23-006020`, FY2025 10-K `0000080035-26-000007`). 2016–2017 are XBRL-only and
are excluded from every headline window; they are shown so the reader can see them.

| yr | OCF | SBC | OCF−SBC | D&A | capex | capex/D&A | **OE @capex** | **OE @D&A** | acq | source |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 26.0 | 1.4 | 24.6 | 12.0 | 24.7 | 2.06 | −0.1 | 12.6 | 0 | xbrl |
| 2017 | 33.8 | 3.1 | 30.8 | 12.8 | 11.2 | 0.88 | 19.5 | 18.0 | 0 | xbrl |
| 2018 | 23.0 | 4.2 | 18.7 | 12.4 | 9.5 | 0.77 | **9.2** | **6.3** | 0 | FILED |
| 2019 | 27.2 | 4.4 | 22.8 | 13.7 | 29.5 | 2.14 | **−6.6** | **9.1** | 18.9 | FILED |
| 2020 | 41.6 | 4.1 | 37.6 | 13.8 | 24.6 | 1.78 | **13.0** | **23.7** | 0 | FILED |
| 2021 | 33.6 | 4.2 | 29.4 | 15.6 | 18.4 | 1.18 | **11.1** | **13.9** | 0 | FILED |
| 2022 | 26.2 | 4.6 | 21.6 | 16.4 | 40.6 | 2.47 | **−19.0** | **5.1** | 16.2 | FILED |
| 2023 | 107.6 | 4.9 | 102.7 | 18.9 | 35.3 | 1.87 | **67.4** | **83.8** | 12.1 | FILED |
| 2024 | 67.5 | 3.4 | 64.1 | 20.8 | 14.7 | 0.70 | **49.4** | **43.2** | 0 | FILED |
| 2025 | 73.5 | 5.0 | 68.5 | 23.0 | 40.1 | 1.74 | **28.4** | **45.5** | 4.7 | FILED |

**EIGHT WINDOWS x TWO (c) ENDS** — six ending at 2025, plus two with alternative **terminal**
dates, because **[E4-38]** names the disease (*"a calculated selection of either initial or
terminal dates"*) and its remedy is to publish every window:

| window | OE @total capex | OE @D&A | yield @capex | yield @D&A |
|---|---|---|---|---|
| 3yr 2023–25 | 48.4 | **57.5** | 2.48% | 2.95% |
| 4yr 2022–25 | 31.5 | 44.4 | 1.62% | 2.28% |
| **5yr 2021–25** *(the corpus default window [E2-42])* | **27.4** | **38.3** | **1.41%** | **1.97%** |
| 6yr 2020–25 | 25.0 | 35.9 | 1.28% | 1.84% |
| 7yr 2019–25 | 20.5 | 32.0 | 1.05% | 1.64% |
| 8yr 2018–25 | 19.1 | 28.8 | 0.98% | 1.48% |
| 5yr 2019–23 *(alt terminal)* | 13.1 | 27.1 | 0.67% | 1.39% |
| 5yr 2018–22 *(alt terminal)* | **1.5** | 11.6 | 0.08% | 0.60% |

*(Yields on a market capitalisation of **$1,948M** — 4,888,701 shares x $398.45, 2026-09-04.)*

### THE WIDTH, AND WHY I REFUSE TO EXPRESS IT AS A PERCENTAGE

**The rebuilt range is $1.5M to $57.5M of owner earnings.** The published screen row was **27 to
58**, a spread of **1.096 = 109.6%**, and the row's own caveat said it was four constructions
(3yr/5yr x two capex ends) and could not see variation older than five years. **It could not,
and the variation it could not see is most of the variation there is.**

But **I will not publish the percentage**, and the refusal is the point. $(57.5 − 1.5)/1.5$ is
**3,733%**, and that number is manufactured, not measured: the denominator is $1.5M on a series
whose own annual values run from **−$19.0M to +$67.4M**. This is the identical defect the DAL
run of 2026-09-07 hit when its rebuilt range crossed zero, and the identical defect
`level_shift` was patched for twice — **a ratio is not informative near zero even where it
computes.** The honest statement is the one in dollars: **owner earnings over the last eight
years have run from about −$19M to +$67M in single years, and every multi-year mean that can be
built from filed data lands between about $1M and $58M.**

**[E4-25]: "Usually, the range must be so wide that no useful conclusion can be reached."** On
owner earnings, that is this file's answer — and per **[E5-11]** the width is itself a Q4
finding, not merely a valuation inconvenience. **The distorted years are named**: 2022 (a
$37.0M inventory build and a $28.0M receivable build, $58.3M of working-capital drag, against
$40.6M of capex) and 2023 (the mirror image, a $14.3M working-capital release). The swing from
2022 to 2023 was **+$72.6M of pure working capital** against an OCF move of +$81.5M. **Nine
tenths of the 2023 "record cash year" was the 2022 inventory coming back.**

**[E3-55] scoping, honestly applied.** *"If we have a business about which we're extremely
confident as to the business result, we would prefer that it have high volatility."* Some of
PLPC's width is exactly that benign kind — a working-capital cycle that nets to zero over a
full cycle, which is why the long windows (7yr $20.5M–$32.0M, 8yr $19.1M–$28.8M) are tighter
and more trustworthy than the short ones. **But not all of it is.** The capex line moved from
0.70x D&A to 2.47x D&A inside the same eight years, and that is a decision, not a cycle.

### THE (c) JUDGMENT — DISCLOSED, NOT COMPUTED **[E2-23, E3-44, E2-41, E5-20]**

*"(c) must be a guess — and one sometimes very difficult to make."*

**The default is D&A [E3-44, E2-41].** *"by and large, the depreciation charge is not
inappropriate in most companies to use as a proxy for required capital expenditures."*

**Is PLPC in [E5-20]'s exception class — railroads, airlines, utilities, "anything whose own
filing says depreciation understates renewal"? NO, and the filing is explicit about why.**
Capex ran **1.58x depreciation cumulatively over 2018–2025** ($212.7M against $134.8M), which is
the pattern the brief told me to watch for. But the FY2025 10-K says what the money bought:
*"In 2025, we used cash of $40.1 million for capital expenditures, **of which $24.8 million
relates to the construction of the new Poland facility and purchase of the new Spain
facility.**"* That is **62% of the year's capex identified, by the filer, as new plant in new
countries** — capacity that adds unit volume, not capex that maintains it. **[E2-23] defines (c)
as what is required "to fully maintain … its unit volume."** New plants in Poland and Spain do
not maintain unit volume; they raise it. **On the filing's own disclosure, 2025 maintenance
capex is nearer $15.3M than $40.1M — which is BELOW the $23.0M depreciation charge.**

**Therefore the D&A end of the band is VALID here.** [E5-20] does not apply and I will not
apply it: PLPC's own filing attributes the capex excess to expansion, not to renewal.

**Where in the band (c) actually sits, as a judgment: nearer the D&A end, but above it.** Two
filed reasons. First, the growth attribution above. Second, **[E4-47]**: *"inflation destroys
value, but it destroys it very unequally"* — replacement in current dollars outruns
depreciation charged in old dollars, and PLPC's gross PP&E of **$461.0M carries $238.3M of
accumulated depreciation (51.7% written down)** across plants in a company incorporated in
1947. A D&A charge struck on that base understates cash renewal cost. **So: (c) ≈ D&A plus a
margin, and the OE@D&A column is the upper bound of the honest band, not the centre of it.**

**Windage count: ONE.** The band is realistic input, not conservatism. No margin of safety has
been applied anywhere above **[E4-11, E4-48]**.

**Working capital [E2-23] constraint 3.** The corpus's own LIFO carve-out is only *partly*
available here: the FY2025 10-K reports that LIFO covers *"certain material, mainly in the U.S.,
totaled approximately $45.8 million"* of **$168.0M** of gross inventory — **27%**. The other 73%
is FIFO and does require working capital as volume grows. The OCF-based convention nets the
whole increment from one audited line, which is the correct treatment and is why the 2022–23
swing appears in the series rather than being hidden.

**Stock compensation subtracted in full [E5-06]**, $3.4M–$5.0M a year. **[E3-70]** notes the
measure should be market value rather than the accounting charge; PLPC grants **RSUs, not
options** (the FY2026 proxy: *"none of the NEOs had any option or option-like awards outstanding
in 2025"*), so grant-date fair value and market value coincide and the reported charge is the
right subtraction rather than a floor.

### THE H1-2026 READ — the sharpest single fact in this file

The 10-Q for the six months to 2026-06-30 (accession `0000080035-26-000030`) shows **the best
half-year of reported earnings in the company's history**: net sales **$389.0M** (+22%),
operating income **$41.6M** (+38%), net income **$32.0M** (+32%), diluted EPS **$6.62** against
$4.89.

**Owner earnings for the same half-year did not move at all.** OCF **$31.3M** (against $32.6M a
year earlier — *down*), SBC $4.7M, capex $17.0M, D&A $12.4M. **OE@capex = $9.6M; OE@D&A =
$14.1M.** Annualised, **$19M to $28M** — indistinguishable from the five-year mean of $27.4M to
$38.3M, and *below* it at the conservative end. The bridge is **$18.5M of working capital
consumed in six months** plus capex running at 1.4x depreciation.

**Record earnings; unchanged owner earnings.** That is the whole reason the framework has an
owner-earnings definition at all, and it is why net income was never going to be an acceptable
proxy here.

---

## B. THREE TOOLING FINDINGS — one confirmation, one correction, one new defect

**1. `da_note` (empty) — CONFIRMED CORRECT.** The brief was right to ask, because the flag has a
$5M materiality floor and PLPC is small enough to hide a break under it. The raw filed D&A
series is thirteen years long, monotone after 2018, and its largest single step is +$2.5M
(2022→2023). **No discontinuity. The empty note is not a miss.** *(Full series printed in the
cross-check block above.)*

**2. `best_year_dep 0.154` — the figure is right and the coordinator's mid-run correction is
right, but the SERIES is the wrong one, and on the right series the answer is four times
larger.** `best_year_dependence()` runs leave-one-out on a **nine-year operating-cash series**.
Reproduced exactly on PLPC's OCF 2017–2025: **0.154, "one year is doing heavy lifting."** Run on
the series the flag is actually being used to judge:

| series | `level_shift` | `best_year_dependence` |
|---|---|---|
| **OCF** (what the screen uses) | **2.68** "STEP UP — normalize down" | **0.154** one year doing heavy lifting |
| **OE @capex** | **`None`** — *"EARLY HALF STRADDLES ZERO … a ratio against it is undefined in substance even where it computes (it gives 10.69x). The level HAS changed and the multi-year mean is averaging TWO DIFFERENT BUSINESSES."* | **0.586** *"TWO YEARS JOINTLY CARRY THE WINDOW — the exact two-year-boom shape leave-one-out cannot see"* |
| **OE @D&A** | **4.48** "STEP UP — normalize down" | **0.253** *"ONE YEAR CARRIES THE WINDOW"* |

**This is a new defect and it is general, not PLPC-specific.** The flags are computed on
**operating cash**, which does not net capital expenditure. For a filer whose capex swings from
**0.70x to 2.47x depreciation** inside eight years, the OCF series and the owner-earnings series
are **different animals**, and they return different flags with different verdicts — including
one (`None`, straddles zero) that the OCF series cannot produce and that fires the moment the
correct series is used. **The zero-straddle guard the PINS run added hours ago is working; it
simply never gets a chance to fire, because it is being fed the wrong series.**
**Recommendation for the tooling: run both flags on the OE@capex series alongside OCF, and carry
both in the CSV.** The cost is one extra column; the benefit is that the flag stops describing a
cash-collection cycle when the run needs it to describe an earnings level.

**3. `spread 1.096` — the caveat is live and the true width is not expressible as a
percentage.** Published 109.6% (27.4 → 57.5, four constructions). Rebuilt over eight windows and
both (c) ends: **$1.5M to $57.5M**, whose percentage form (3,733%) is an artefact of a
near-zero denominator and is **refused** here for the same reason `level_shift` refuses its
ratio. **That makes PLPC the tenth consecutive run to find the true width larger than published,
and the second after DAL where the arithmetic form of "width" breaks down entirely.** The
suggestion I would make: where the rebuilt bottom is within, say, one standard deviation of zero
on the underlying annual series, the CSV should carry the **dollar range and a word**, not a
ratio.

---

## C. Q3 ITEMS — NO VERDICT IS WRITTEN; THE GATE IS CLOSED **[E2-01, E4-22, E5-08, E2-30]**

**The weight case, declared because a run that does not declare it has not done Q3.**
Daily execution **[E3-38]** — no; the product ships from a catalogue against a firm backlog.
Control **[E1-16]** — no; this would be a minority position. Leverage **[E3-29]** — no; total
debt $39.5M against $475.5M of equity, and interest income exceeds interest expense.
**None ticked → Q3 would be a qualitative OVERLAY, not a binary gate.**

### Who controls this company

**One share class only** — Common Shares, $2 par — so `cover_shares.py`'s refusal to sum classes
does not bite and the charter question does not arise. **4,888,701 shares outstanding** on the
10-Q cover of 2026-07-30. Proxy of 2026-03-20, ownership as of 2026-03-05:

| holder | shares | % |
|---|---|---|
| **Robert G. Ruhlman** (Executive Chairman) | 1,475,081 | **30.1%** |
| **Randall M. Ruhlman** (not an officer or director) | 1,147,610 | **23.4%** |
| Dimensional Fund Advisors | 307,486 | 6.3% |
| all executive officers and directors as a group (16) | 1,615,502 | 33.0% |

The two Ruhlman brothers' holdings overlap in **281,538 co-trusteed shares**, so their combined
unique position is **2,341,153 shares — 47.9% of the company.** Robert G. Ruhlman is Executive
Chairman and **is named in the segment footnote as the chief operating decision maker** — not the
CEO. His son **J. Ryan Ruhlman is President and a director**; his daughter **Maegan A. R. Cross
is a director**. **This is a controlled company in substance while filing as an ordinary one.**

### The thin-quote question, answered — and it is a fact about the price, not the business

The brief asked whether the float is small enough that the quote is thin. **It was, and it
violently is not any more, and the change is the story.** Median daily volume, aggregator-sourced
and flagged as such:

| | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 YTD |
|---|---|---|---|---|---|---|---|
| median shares/day | 5,700 | 7,850 | 10,800 | 13,400 | 12,350 | **54,250** | **109,250** |
| median $/day | $0.3M | $0.5M | $0.7M | $1.8M | $1.6M | **$8.3M** | **$35.8M** |

**Volume is up 19x since 2020 and dollar volume 119x, while the share count has FALLEN and the
two brothers have not sold to the market.** The free float is roughly **2.4M shares**; at
109,250 shares a day, **about 4.5% of the entire free float changes hands every trading day.**
The quote is not thin. It is the opposite: a very small float being turned over at a rate that
has nothing to do with a utility hardware maker's fundamentals. **Nothing in the filed
statements moved 3x between mid-2025 and mid-2026. The crowd did.** Per the brief's own
instruction, that is stated plainly as **a fact about the price**.

### The buyback — [E5-08]'s two conditions, [E4-31]'s third, and a related-party structure

**Every buyback dollar is split in the cash-flow statement into two lines, and the split is the
finding.** From the filed statements, $M:

| | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | H1-26 | **total** |
|---|---|---|---|---|---|---|---|---|---|---|
| open-market treasury | 0.19 | 2.80 | 5.84 | 0.18 | 0.16 | 0.73 | 0.23 | 1.05 | 0.94 | **12.10** |
| **from related parties** | 3.97 | 4.03 | 3.63 | 5.09 | 5.31 | **18.16** | 8.38 | 8.71 | **11.29** | **68.56** |

**85% of every buyback dollar over eight and a half years — $68.6M — went to buying shares from
the company's own officers and directors.** The practice is unbroken in every year filed, and
**H1-2026 alone ($11.3M) is larger than any full year except 2023.**

**It is disclosed in unusual detail, and that matters.** The 2026 proxy lists each 2025 purchase
by name, date, share count and price: Robert G. Ruhlman 10,000 shares at $154.28 (4 Aug 2025);
J. Ryan Ruhlman 3,274 at $137.08 and 2,555 at $143.27; the CFO 3,000 at $154.28; the CEO 3,904
at $188.37; and seven more. **Every one is struck at "a 30-day average price per share"** and all
are approved in advance by the Audit Committee. That is a fair-process structure, not a
negotiated insider bailout, and the pricing rule removes the discretion that would make it one.

**But three things are true at once and all belong in the register.**
1. **The company is the standing bid for insider stock.** In a float this size, the officers'
   exit liquidity *is* the buyback. That is a real allocation of shareholder capital to a
   purpose other than value per share.
2. **[E5-08] condition (2) fails on my own numbers, and the humility clause [E4-13] applies.**
   Purchases were struck at **$137–$221** through 2025 against a conservative value range
   computed below of roughly **$60–$120** at the [E4-28] floor. This rests on my range, not
   theirs, and *"they also know a whole lot more about them than I do."* **[E5-24]** governs:
   *"what is smart at one price is dumb at another."*
3. **The direction cuts the other way on timing, and it should be said [E4-26].** The Executive
   Chairman sold 10,000 shares to the company at **$154.28** in August 2025. The stock is
   **$398.45** today. **He sold the bottom quartile of his own year.** Whatever this practice is,
   it is not insiders picking the top.

**[E4-31]'s third condition — "shareholders should have been supplied all the information they
need for estimating that value" — is the one I would press.** PLPC files segment revenue, gross
profit, costs, net income, assets and long-lived assets; it files backlog; it files a thirteen-
year clean D&A series. It files **no unit volume, no ASP, and no split of price from volume in
any vintage** — the disclosure Hubbell makes every year. A register asked to price a repurchase
is missing the series that would let it.

**[E2-51]'s refusal flag does not fire** — this management repurchases, and the share count has
fallen from 4,931k (2022 average basic) to **4,774k** (Q2-2026 average basic).

### Compensation, and the metric they pay themselves on

**The metric is right and the bar is low.** The annual cash incentive is *"tied directly to the
financial performance of the Company on a sliding scale of return on shareholders' equity …
based on the Company's **pre-tax income as a percentage of average shareholder's equity
(adjusted for foreign currency translation)** and assessed over a range of **3% to 11%**. The
implied target is 7%."*

**[E2-01] is emphatic that this is the right yardstick** — *"the achievement of a high earnings
rate on equity capital employed … and not the achievement of consistent gains in earnings per
share."* PLPC pays on return on equity, not on EPS, not on TSR, not on adjusted EBITDA. **The
metric has not been switched in the five years disclosed, which passes [E2-49].** Credit where
it is due; most filers in this queue do worse.

**But the scale pays MAXIMUM at an 11% pre-tax return on equity** — roughly **8.5% after tax at
2025's 22.6% effective rate**. The corpus asks for *"a high earnings rate"*; a plan whose
ceiling is a high-single-digit after-tax ROE has set the bullseye where the twelve-year mean
already sits. **[E2-49]** asks for *"pre-set, long-lived and small bullseyes"* — this one is
pre-set and long-lived, and it is not small.

**Reported plan outcomes** (2026 proxy, pay-versus-performance table): **2021 16.9% · 2022 21.0%
· 2023 20.8% · 2024 12.3% · 2025 13.3%.** Every year at or above the 11% maximum. **Every NEO
earned 100% of the maximum bonus in every one of the five years disclosed.** The
filed-statement return on beginning equity for the same years was **12.2, 17.2, 17.7, 8.9,
8.4%** — the plan's numerator is pre-tax and its denominator is adjusted, so it reads roughly
five points higher than the shareholder's own return, and in 2024–25 it reads *above* the
maximum while the shareholder's return was **under 9%**.

**And the Compensation Committee then went above the formula:** *"The Compensation Committee
approved an **additional 10% discretionary bonus** for Mr. Robert G. Ruhlman."* A discretionary
top-up on a plan already paying its maximum is the behaviour **[E2-30]** describes as
institutional rather than venal, and it is recorded that way.

**Scale, against the owner's share.** FY2025 summary compensation: Robert G. Ruhlman
**$4,993,779**; Dennis F. McKenna (CEO) $3,287,390; J. Ryan Ruhlman $1,962,790; Andrew S. Klaus
$1,584,133; John M. Hofstetter $1,346,553 — **$13.17M for five people against $35.28M of net
income attributable to shareholders: 37.3%.** The Executive Chairman alone is **14.2%** of net
income. The 10-K's tax footnote confirms the level independently: *"A $1.7 million, or 3.8%, net
increase resulting from **non-deductible officers' compensation**"* (and $2.0M in 2024) — the
§162(m) disallowance, which only bites above $1M a head. **Median employee pay $23,285; CEO pay
ratio 214:1.**

**Perquisites.** *"The Executive Chairman, CEO and President are permitted to use the Company's
aircraft for personal purposes."* The aircraft is not a lease: on 19 January 2021 the company
took a **$20.5M term loan from PNC Equipment Finance for the full purchase price of a new
corporate aircraft** ($10.6M outstanding at 2025-12-31), and it sits inside the PP&E note under
*"Machinery, equipment and aircraft."* **$20.5M is 58% of a year's net income and roughly 1% of
the company's market value at today's inflated price.** Also disclosed: club dues for three NEOs
and one director, personal financial advice for the Executive Chairman, tax advice for all
executive officers.

### The flags **[E4-22, E4-29, E5-15, E4-30]** — and most of them do not fire

- **Weak accounting — NO.** Ernst & Young; no disagreements; ICFR effective; no restatement in
  any vintage read.
- **Unintelligible footnotes — NO.** They are short, plain and complete. The inventory note
  gives the LIFO reserve, the LIFO-costed subtotal and the year's LIFO charge separately.
- **Trumpeted projections — NO.** No guidance is issued. There is no earnings-call guidance
  practice to set against outturn, which means **[E3-48]** cannot be run and **[E5-30]**'s
  ratchet has not been started.
- **Serial share issuance [E5-15] — NO.** The count falls.
- **EBITDA / adjusted-earnings promotion [E4-29] — NO, and this is a genuine positive.**
  **Zero occurrences of "EBITDA" and zero occurrences of "adjusted net income / earnings / EPS /
  operating income" in the FY2025 10-K and in the 2026 proxy.** The only non-GAAP measure used
  anywhere is currency-translation impact, and it is disclosed **by segment, on both net sales
  and net income, in a table, with the amounts named.** In a queue where this flag fires almost
  everywhere, PLPC does not touch it.
- **Filed-figure tells [E4-30] — NO.** Cash taxes paid as a share of pre-tax income: **2019
  24.8% · 2020 19.0% · 2021 34.6% · 2022 19.8% · 2023 26.6% · 2024 25.8% · 2025 25.1%.** No
  downward drift. And reported growth is conspicuously **un**smooth — revenue −11% then +13%,
  net income 63.3 → 37.1 → 35.3 — which is the opposite of the engineered-smoothness tell.
- **[E3-53] restructuring charges — effectively NO.** One goodwill impairment ($6.5M, 2022) and
  one loss on exit of a business ($1.0M, 2022), both left in the income statement. The 2025 US
  pension termination charge of **$11.657M** is quantified separately on the income statement,
  in the cash-flow reconciliation, in the tax rate walk and in the MD&A — **[E2-26]**'s
  half-owner test passed at every line. Both sit in the owner-earnings mean per **[E5-33]**, as
  they should.
- **[E2-52] dividends funded by issuance — NO.** Dividends $4.1M a year against $73.5M of OCF.
- **[E3-50] stock-price targeting — NO** filed evidence.

### Capital allocation, and the dividend that did not move for a generation

The FY2025 MD&A: *"Our strong liquidity also allowed us to increase our quarterly dividend by 5%
to $0.21 per share in the fourth quarter of 2025, **the first such increase since the Company's
shares began trading on NASDAQ stock exchange in 2001.**"*

**A flat $0.80 annual dividend for twenty-four years**, on a business whose revenue rose from
roughly $170M to $669M over the same span, and whose retained earnings rose from $200M-ish to
**$584.4M**. Read one way that is admirable discipline — every dollar retained and reinvested.
Read the other way it is **[E2-30](1)**, *"an institution will resist any change in its current
direction"*, for a quarter of a century, and the reinvestment earned **9.7% on equity on a
twelve-year mean** and **3.8% on the last seven years' increment.**

**[E3-54]'s scored retention test, five-year rolling: PASSES, and the pass is uninformative.**
Retained 2021–2025 = $225.8M of net income less $20.5M of dividends less $48.0M of buybacks =
**$157.3M**. Market capitalisation went from about **$337M** (4.92M shares x $68.44, 2020-12-31)
to about **$1,002M** (4.85M x $206.71, 2025-12-31) — **$4.23 of market value per $1 retained.**
But **[E4-44]** immediately voids the inference: *"the value of an asset, whatever its
character, cannot over the long term grow faster than its earnings do."* Earnings over that
window went **$29.8M → $35.3M, +18%**, while the quote went **+202%**. The retention test passed
on multiple expansion, and multiple expansion is not a perpetual term.

**[E2-30], the four behaviours, scored.** (1) resists change in current direction — **yes**, on
the dividend, on the disclosure format, and on a compensation plan whose maximum has been earned
five years running. (2) projects to soak up funds — **no**; acquisitions are small ($4.7M JAP
Telecom in 2025, $12.1M in 2023, $16.2M in 2022) and the new plants are in the core business.
(3) staff studies for the leader's craving — **not observable**. (4) peer imitation — **no**; if
anything PLPC's disclosure is idiosyncratically its own.

**[E3-58] delegation of allocation — no evidence of it.** No banker-led M&A programme, no
consultant-driven restructuring.

---

## D. Q4 ITEMS — RECORDED, NOT A VERDICT

**Great, good or gruesome [E4-20]? GOOD, at the low end of good.** Not great — the returns are
not high and do not rise (twelve-year mean ROE 9.7%). Not gruesome — it does not consume cash to
earn nothing; it earns roughly its cost of capital on added capital and pays a dividend.
**[E4-43] is explicit that the good class passes** — *"nothing shabby about earning $82 million
pre-tax on $400 million of net tangible assets"* — and **[E5-40]** puts ~12% on retained capital
at *"quite satisfactory."* **PLPC's twelve-year mean is 10.9% on tangible equity, just under
that.** It is a fair business at a fair return. It is not a franchise, which is what Q2 decided.

**Staying power, all three scored [E5-11].**
1. **A large and reliable stream of earnings — LARGE, NOT RELIABLE.** Operating income
   $84.2M → $50.8M → $55.1M in three consecutive years; owner earnings negative in two of the
   last eight.
2. **Massive liquid assets — ADEQUATE, NOT MASSIVE.** $76.2M cash at 2026-06-30 ($83.4M at
   year-end), plus $52.0M unused under the facility, against $39.5M of total debt. *"The
   majority of our cash is held outside the U.S."* — a real constraint on its US usability, and
   the company says so.
3. **No significant near-term cash requirements — PASSES, and this is the one that usually
   kills.** Total debt $39.5M against $475.5M of equity; bank-debt-to-equity **8.3%**. The
   longest commitment is the Poland plant loan (up to PLN100.3M / $27.9M, $12.6M drawn, maturing
   2035, amortising PLN5.3M in 2026 rising to PLN9.6M a year 2028–34) and the aircraft loan
   ($10.6M, $2.1M current). **[E2-54]'s coverage test is passed trivially: H1-2026 interest
   expense was $471k against interest INCOME of $1,411k.** PLPC is net-interest-positive.
   **[E5-39]**: no dependence on the kindness of strangers.
   **[E3-66] jurisdiction:** a US filer, so US shareholder priority applies — but **53% of
   revenue and the majority of cash sit in 19 other countries**, and repatriation is disclosed
   as neither intended nor foreseen.

**[E4-16] leverage, named and quantified:** total debt $39.5M, 8.3% of equity, covenanted for
net worth and profitability, in compliance. **No ratio ceiling exists in this framework and none
is asserted.** This is not a leverage story.

### THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**

**It does not go bankrupt. Naming insolvency here would be modelling experience rather than
exposure [E4-40], and the exposure is not on the balance sheet — it is in the operating
leverage.**

**The mechanism: PLPC's cost base is fixed and its revenue is a derivative of somebody else's
capital budget.** Costs and expenses were **$153.4M in 2025, 22.9% of sales**, and they are
people, plants and engineering — 3,734 employees across 26 plants in 20 countries, hired to hold
an approval position. The revenue that pays for them arrives through a **four-month backlog**
that the filed series shows can halve in twelve months.

**Consider some mathematics [E3-24].** This has already run once, inside the window, and the
filings record the result. **2024: revenue fell 11% ($669.7M → $593.7M) and operating income fell
40% ($84.2M → $50.8M).** Downward operating leverage of **3.6x**. Apply the same arithmetic to
the current cost base: an 11% revenue decline from 2025's $669.3M, with gross margin held at
31.2% and costs and expenses held at $153.4M, takes gross profit to about **$186M** and operating
income to about **$32M** — a **42% fall** — and a 20% decline takes operating income to roughly
**$14M**, a **75% fall**. **At the current market capitalisation of $1,948M, the second case is
90 times operating income.**

**Likelihood: a real possibility, and the highest-quality evidence for it is the filer's own
backlog table.** Backlog stood at $379.4M at end-2022 and $172.6M twelve months later. It is
$232.8M today, having risen 22% in a year into a grid and data-centre power build-out that
everyone in the market can see. **The exposure is not that PLPC is fragile. It is that a
cyclical business with 3.6x downward operating leverage is being priced at 55x its most recent
full-year net income and roughly 34x the most optimistic owner-earnings construction that can be
built from ten years of filed data.**

**The second mechanism, slower and management-named: the Communications 22%.** The 10-K's own
risk list names *"technological developments that affect longer-term trends for communication
lines, such as wireless communication"* and *"the decreasing demand for product supporting
copper-based infrastructure."* Communications was **29% of revenue in 2023 and 22% in 2024 and
2025** — roughly **$194M falling to $147M, −24% in two years**, while Energy rose. This is a
named, filed, management-disclosed erosion on a fifth of the business, and it is the Q6
monitoring item.

**The bear case, stated as its holders would state it [E4-51]:** *You are buying a good, small,
family-controlled cyclical manufacturer at three times what it cost fourteen months ago, on
earnings that are at a cycle high, at a moment when its own filed backlog has round-tripped once
already inside five years, at a price where the entire twelve-year mean of its owner earnings
buys you a 1.4% yield against a 5.24% government bond. The business will be fine. The price is
the risk.*

---

## E. Q5 — **COMPUTATION, NOT A CLEARANCE** (operator rule 3)

**Q5 does not open. Q2 returned OUT. This block carries no entry language and casts no vote.**

- **Price** $398.45 (2026-09-04, aggregator, flagged) · **shares** 4,888,701 (10-Q cover,
  accession 0000080035-26-000030) · **market capitalisation $1,948M**
- **Sovereign** **5.24%** USD, US Treasury 30-year par yield, 2026-09-04, issuing authority

**1. THE YIELD.** Owner earnings **$27.4M–$38.3M** on the corpus's default five-year window
[E2-42] ÷ $1,948M = **1.41% to 1.97%**, against a sovereign of **5.24%**. Across all eight
windows and both (c) ends: **0.08% to 2.95%.** **Every single construction is below the bond.**
The best one — the three-year window at the D&A end, containing the working-capital release
year — pays **2.95%**, which is **229 basis points below** a riskless Treasury.

**2. WHAT THE PRICE ALREADY ASSUMES.** To reach the **[E4-28]** floor of ~10% from a 1.41%
starting yield requires perpetual growth of **8.59%** — which reproduces the screen row's
`growth_required 8.56%` almost exactly, and confirms that the row's figure is computed against
the 10% floor and not against the bond. To reach merely the **sovereign** requires perpetual
growth of **3.27%**. What the business has actually done: revenue CAGR **7.0%** (2019–25); net
income CAGR **4.1%** (2018–25); **owner earnings: no trend at all** — the eight-year mean
($19.1M–$28.8M) is lower than the five-year mean ($27.4M–$38.3M) only because the earlier years
contain the negatives. **[E4-35]** is the governing base rate: *"fewer than 10 of the 200 most
profitable companies … will attain 15% annual growth in earnings-per-share over the next 20
years."* An 8.6% **perpetual** rate is a weaker claim than 15% for twenty years but a longer
one, and the burden of proof sits with whoever asserts it. **This file does not assert it.**

**3. WHAT YOU ARE PAID.** **−3.83 to −2.29 points against the sovereign** — you are paid *less*
than the government bond, before any equity risk, before the cyclicality, and before the
operating leverage quantified above. *(The screen row said −3.80; it reproduces.)*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01].** Owner earnings of $27M–$58M capitalised:
- at the **[E4-28] ~10% floor**: **roughly $270M to $580M — about $55 to $120 a share**
- at the **bare sovereign 5.24%**, no risk premium, no growth, which is the most generous
  construction the framework permits **[E3-42]**: **roughly $520M to $1,100M — about $105 to
  $225 a share**
- **current price: $398.45**

**THE FLOOR VERDICT [E4-28].** Honest pre-tax expectancy at this price is **1.4% to 2.9%**
against a floor of roughly 10%. *"That's the figure we quit on."* **Below the floor, the name is
not ranked — it is quit on, and the ranking lines are not filled in.** It is also below the bond,
which is the rarer and simpler observation: **Berkshire is the framework's noted case of a name
above the bond and below the floor; PLPC at $398.45 is below both.**

**Which bar?** Neither is reached. **Bar 2 [E4-01], the screamer test**, is the only one that
could apply to a name at this yield, and its answer is the third outcome: **the price is above
the whole range.** No margin of safety is applied, because a margin is applied to a value you
have arrived at, and the price is already 1.8x the top of the most generous construction.
**Windage count: one — the (c) band, which is realistic input, not conservatism.**

---

## F. Q6 ITEMS — RECORDED FOR THE REGISTER, NOT A VERDICT **[E1-02, E2-28, E4-17, E3-30]**

Pre-committed now, so that a future re-run is judged against a yardstick set before the fact
**[E1-02]**:

- **Thesis-breaking metric for the Q2 OUT, in order of information value:**
  **(1) consolidated operating margin ≥13% for three consecutive years** — the approval position
  finally reaching the owner rather than the cost base; **(2) any filed unit, tonnage or ASP
  series**, which would make [E4-55] runnable for the first time; **(3) a disclosed list-price
  increase taken and held into flat or falling volume**, which is [E2-44] half one; **(4) order
  backlog above $230M for eight consecutive quarters**, converting the 2021–25 swing from a
  cycle into a level.
- **Thesis-confirming metric:** order backlog, filed annually in Item 1, read beside
  Communications as a percentage of revenue. **A backlog fall toward $170M with Communications
  below 20% is the 2023 episode repeating.**
- **Monitoring question [E3-30]:** *is this erosion an aberrational cycle, or has the business
  slipped in a way that permanently reduces intrinsic value?* On Communications the filing says
  the erosion is **technological, not cyclical** — copper displacement and wireless substitution
  are named by management. On Energy the swing is plainly cyclical.
- **Next catalysts:** Q3-2026 10-Q (~end October 2026); **FY2026 10-K (~early March 2027), which
  carries the next annual backlog figure and the next employee and plant counts** — the three
  physical-adjacent series this file relies on.
- **Position size:** **none.** The gate closed at Q2 and the price is below the sovereign.

---

## SELF-AUDIT

- [x] Questions answered in order; the file stopped at the first verdict that was not IN
- [x] No question marked IN carries an "unverified" or "provisional" caveat
- [x] Q2's OUT is a finding about the business from read filings, not a diligence gap — every
      document that would resolve it has been read, and what would flip it is named in advance
- [x] Step 0: the filing was read (MD&A, cash-flow statement including detail lines, footnotes),
      with accession numbers; six figures cross-checked against the filed statements
- [x] Share count read off the cover of the **latest periodic filing** (10-Q, 2026-07-30), not
      the 10-K; one share class, so no summing judgment arises
- [x] Owner earnings on multi-year means; **eight** windows and both (c) ends; capex band
      disclosed as a judgment with the filing's own growth-capex attribution cited
- [x] Competitor row filled — six listed peers plus one acquired comparable, same metric, same
      window, filing-sourced; the count is stated rather than padded to eight
- [x] Sovereign is for the earnings currency, from the issuing authority, dated
- [x] Value stated as a round-number range, not a point estimate
- [x] One bar named; windage count stated (one)
- [x] Prices dated; aggregator used for the live quote and the volume series only, and flagged
      in both places
- [x] Every Q5 figure carried under **COMPUTATION — NOT A CLEARANCE**; no entry language
- [x] Run committed to git after each gate

## REGISTER

- **Verdict: OUT (about the business, at Q2).**
- **One line:** the world's largest maker of formed wire products, which passed through 87% of a
  7.7-point tariff shock in a year and whose own backlog table prints its cycle honestly, is
  nonetheless not a franchise — it says in every 10-K that its markets are *"highly competitive"*
  and that the first method of competition is *"price"*, it earns 9.7% on equity across twelve
  years against a nearest competitor's 24.4%, and at $398.45 it yields **1.4% to 2.9%** against
  a **5.24%** government bond.
- **Q1 IN · Q2 OUT · Q3 not reached · Q4 not reached · Q5 not reached · Q6 not reached.**

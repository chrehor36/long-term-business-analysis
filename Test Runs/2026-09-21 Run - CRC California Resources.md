# Company Run - California Resources Corporation (CRC) - 2026-09-21
**VERDICT: Q1 IN / Q2 OUT.** The file closed at the franchise question. Q3-Q6 material is
recorded beneath the close with no verdict box ticked (operator rule 2), and the valuation
arithmetic is headed **COMPUTATION — NOT A CLEARANCE** (operator rule 3).
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS - every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order - not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation - it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 - THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** - the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34 %** · date **09/18/2026** · source (issuing authority) **US Treasury daily par yield
  curve, 30 Yr column, struck fresh this run by `python tools/sources.py`.** Not inherited from any
  brief or prior run. FRED DGS30 was not used; the Treasury is the issuing authority (operator rule 5).
- FX: **none.** CRC sells crude, NGLs, natural gas and electricity in the United States and reports
  in USD. Earnings currency and quote currency are the same. No ADR ratio.

**The price, the share count and the cap - re-struck, not inherited:**
- price **$53.02**, 2026-09-21, **aggregator quote, flagged as such** (via `tools/run.py`;
  aggregators for live quotes only, operator rule 5).
- shares **88,819,893** of Common Stock, the cover-page count of the **10-Q for the period ended
  2026-06-30, filed 2026-08-10, accession 0001609253-26-000130** (`Screens/cover_shares.py CRC`).
  **One class only** - nothing was summed. The registration line on the 10-K cover reads
  "Common Stock | CRC | New York Stock Exchange" and Item 12(g) is "None". The FY2025 10-K cover
  carries 88,597,474 at January 31, 2026; the later periodic governs.
- **cap = 88,819,893 × $53.02 = $4.71 billion.** The screen row carried `cap_m` 4,639. The re-strike
  is **1.5% higher** and **the screen's cap survives.** No BELFB-class (6.29x) or FC-class (18%)
  error here.

**The filing was read** - not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **Form 10-K for the fiscal year ended December 31, 2025, filed
  2026-03-02, accession 0001609253-26-000051**, primary document `crc-20251231.htm`. Also read:
  **Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-10, accession 0001609253-26-000130**;
  the **8-K of 2026-08-10, accession 0001609253-26-000127** (Items 2.02, 9.01) with its EX-99.1
  earnings release; and the three Item 1.01 8-Ks of **2026-03-23 (0001609253-26-000084)**,
  **2026-04-17 (0001609253-26-000086)** and **2026-06-26 (0001609253-26-000120)**.
- figure cross-checked against the filed statement: **net cash provided by operating activities of
  $865 million (2025), $610 million (2024) and $653 million (2023)**, read off the Consolidated
  Statements of Cash Flows in the 10-K (page 89 of the filing), against the same three numbers
  produced by `tools/run.py` from XBRL. **They agree.** **Capital investments of $(322), $(255) and
  $(185) million** on the same statement also agree. **Stock-based compensation of $39, $40 and $48
  million** was checked against Note 10 Stock-Based Compensation, line "Total stock-based
  compensation expense" - it **RESOLVES and is COMPLETE**; no `SBC_UNRESOLVED`, no `SBC_PARTIAL`.
  Note that SBC does **not** appear as its own line in the cash-flow statement: it sits inside
  "Other non-cash charges to income, net" of $187 / $139 / $103 million, which is why the footnote
  had to be opened. This is the Bloom-class trap and it was checked, not assumed.

### THE PERIMETER, ESTABLISHED FROM THE FILINGS BEFORE ANY SERIES IS BUILT
*The screen's `acq_note` said "$1,345M of acquisitions, 29% of cap, inside the window - the
numerator and denominator may be different companies." It is worse than the note knew: **there are
four perimeters here, not two.***

| break | date | what changed | source |
|---|---|---|---|
| Spin-off from Occidental | 25 Nov 2014 | CRC became a separate registrant | Separation and Distribution Agreement dated 25 Nov 2014, exhibit 2.1 to the FY2025 10-K |
| **Chapter 11 emergence** | Oct 2020 | fresh start; a new balance sheet | "Amended Debtors' Joint Plan of Reorganization Under Chapter 11 of the Bankruptcy Code (filed as Exhibit 2.1 to the Registrant's Current Report on Form 8-K filed October 19, 2020 and incorporated herein by reference)" - FY2025 10-K exhibit 2.2; and "our emergence from bankruptcy" at the equity-compensation-plan table |
| **Aera Merger** | 1 Jul 2024 | all-stock; "nearly doubled the size of our asset base" | FY2025 10-K: "On July 1, 2024 ... we obtained all of the ownership interests in Aera Energy LLC (Aera) in an all" -stock transaction; $853M of cash used, $646M of ARO assumed |
| **Berry Merger** | 18 Dec 2025 | all-stock; 5,572,115 shares, ~6% of CRC | FY2025 10-K: "The Berry Merger closed on December 18, 2025 and we issued 5,572,115 shares of our common stock, which represented 0.0718 shares of our common stock for each outstanding share of Berry stock ... the former Berry stockholders owned approximately 6% of CRC."; $440M of cash used, $151M of ARO assumed |

**So: what is the owner-earnings series a series OF?** Three different companies in three years.
- **2023** is CRC standalone, post-emergence: **86 MBoe/d**.
- **2024** is CRC plus **six months** of Aera: **110 MBoe/d**.
- **2025** is CRC plus twelve months of Aera plus **thirteen days** of Berry: **138 MBoe/d**.
- **2026** will be the first year that is any one company for twelve months.

The filing says it in its own words: *"Our consolidated results of operations include the results of
Berry beginning December 18, 2025, the closing date of the Berry Merger. Our consolidated results of
operations include the results of Aera beginning July 1, 2024, the closing date of the Aera"* Merger
(FY2025 10-K, MD&A). **A five-year mean across 2021-2025 averages a company producing 86 MBoe/d with
a company producing 138 MBoe/d and reports the result as one number.** It is not one number. The
screen's `years_filed` of **14**, against a registrant that first filed in 2014, spans **all four**
breaks. The `level_note_oe` flag - **EARLY HALF STRADDLES ZERO, pre-window low of minus $274.0M** -
is that fact showing up as arithmetic: the minus $274M is the pre-emergence company under a
different capital structure, and **it is not this company's record**. The `flags_disagree` warning
has the same root: one construction of the series sees a level shift where the other does not,
because there genuinely are level shifts, four of them, and neither construction knows where.

**Held as a standing caveat on every number below**, and the reason this run builds the series on
the **three years the filing itself presents side by side (2023, 2024, 2025)**, saying at each step
what each year is a year of, rather than reporting a five- or nine-year mean of four different
companies.

---
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words, no management language.** CRC owns roughly **1,986 thousand net
  mineral acres** in California and Utah, **75% of it held in fee**, and pumps oil out of old fields
  - Belridge, Elk Hills, Midway-Sunset, Wilmington - discovered between the 1800s and the 1920s.
  Much of it is heavy oil that will not flow on its own, so CRC **buys natural gas, burns it to
  raise steam, injects the steam to thin the oil, and lifts what comes back.** It sells that oil to
  a short list of California refineries. In 2025 it produced **50 MMBoe (138 MBoe/d)** and booked
  **$2,910 million of oil, natural gas and NGL sales**. The arithmetic of one barrel, from the
  filing's own per-Boe table (FY2025 10-K, Production, Price and Cost History, and the oil and gas
  segment table): revenue is the **realized oil price of $66.52/Bbl** (2025, before hedges); against
  it sit **operating costs of $25.42/Boe**, **DD&A of $9.77/Boe**, **taxes other than on income of
  $4.03/Boe**, **field transportation of $0.81/Boe** and **segment G&A of $0.85/Boe**. Energy - the
  gas burned to make the steam - was **$374 million of 2025 operating cost**, so a large slice of
  the cost line is itself a commodity price moving independently of the one on the revenue line.
  There are two smaller legs: a **550 MW cogeneration plant at Elk Hills** that powers the fields
  and sells surplus electricity, and a **carbon management segment (Carbon TerraVault)** that
  produced **segment losses of $(66)M, $(94)M and $(86)M in 2023, 2024 and 2025** and no meaningful
  revenue.
- **The scarce input this business controls:** the **fee mineral acreage in California**, and the
  **state permits to drill into it and to inject into it**. Not the oil. The oil price is set
  offshore and the filing now says so outright: *"In 2025, the marketing arrangements for the
  majority of our production no longer rely on local postings but are instead based directly on
  Brent prices subject to applicable adjustments."* The acreage is genuinely scarce - three quarters
  held in fee, in a state that has permitted very little new drilling for years - and that scarcity
  is the whole of what CRC controls.
- **Will the fundamentals look broadly the same in ten years?** **In kind yes; in level, the filing
  itself says no.** The mechanics (pump, sell at an index, spend to offset decline) are as simple in
  2036 as in 2026, and I can write them down without management's language, which is what [E3-31]
  asks. But three items in this filing are changes already in motion, not forecasts, and they are
  recorded here so they are not discovered later at Q2 and Q4: **Phillips 66 closed its Wilmington
  refinery in October 2025**; **Valero confirmed in January 2026 that it will cease refining at
  Benicia**; and in **December 2025** the San Pablo Bay Pipeline - the filing's *"primary inland
  pipeline carrying crude from California fields to Bay Area refiners"* - had its shipments
  *"effectively suspended after refinery demand declined and producers ceased nominations, reducing
  volumes to zero. The closure of this pipeline effectively eliminated our access to Bay Area
  refineries and we modified our marketing, transportation and shipping arrangements to reach
  alternative markets in Southern California. As a result, we expect to experience higher
  transportation costs."*
- **The cash-consuming leg is recorded here and does not travel.** Carbon TerraVault is a separate
  question from the producing business. **[E5-40]** is the corpus's line on a cash-consuming
  business - what makes one gruesome is *"unless the cash they consume gets to earn a reasonable
  return"* - and it is answered at Q4 on this filing, never borrowed as a reason to like the whole.
- **VERDICT: [x] IN**  *(the business is "relatively simple and stable in character" in the sense
  [E3-31] asks about: the unit economics fit in a paragraph written without management's words, and
  the scarce input is nameable. A one-foot bar [E4-18], not a seven-foot one. Nothing in this
  verdict is provisional and nothing in it is general knowledge; every figure above is off the
  filed 10-K.)*

## Q2 - IS IT A FRANCHISE? **[E3-03]**

**The three criteria, each answered on the filing:**
- **(1) needed or desired - [x] YES.** California consumes far more crude than it produces and
  CRC's barrels go straight into the refinery gate. Not in dispute.
- **(2) no close substitute - [ ] NO, and CRC's own competition paragraph says so.** *"We also
  compete with foreign oil and gas companies since California imports over 75% of the oil it
  consumes and nearly 95% of its natural gas needs."* (FY2025 10-K, Competition.) **There is a
  perfect substitute for every barrel CRC sells, it arrives by ship, and it supplies three
  quarters of the market already.** The filing goes further and says the price itself is now set
  by that substitute: *"In 2025, the marketing arrangements for the majority of our production no
  longer rely on local postings but are instead based directly on Brent prices subject to
  applicable adjustments."* A product priced off the substitute's index is the definition of a
  close substitute existing.
- **(3) not subject to price regulation - [x] YES, prices are not regulated** - but the third
  criterion is the one that matters least here, and **[E2-59]** is the reason: administered
  pricing *floors* a commodity business and does not create a franchise. CRC has no floor; it has
  the opposite, a California regulatory regime that constrains its *costs and permits* while
  leaving its price to Brent. Criterion 3 passes and buys nothing.

**THE CLAIMED EXCEPTION, AND IT IS A REAL DOOR.** **[E2-58]** is written about exactly this
business: *"persistent over-capacity without administered prices (or costs) equals poor
profitability"*, with long-run profitability set by *"the ratio of supply-tight to supply-ample
years"* - and it names **one** exception: *"a cost advantage that is both **wide and sustainable**
… By definition such exceptions are few."* CRC discloses such an advantage in its own words, and
the same sentence the 2026-07-16 run found is still in the FY2025 filing, verbatim:

> "We believe that our proximity to the California refineries gives us a competitive advantage over
> importers due to lower transportation costs. Further, California refineries are generally designed
> to process crude with characteristics similar to those of our production."
> - FY2025 10-K, **Competition**

**That claim is testable, and the competitor row is what tests it, because a moat is a relative
claim [E3-28].** It was not tested in 2026-07-16, because that run built no row.

### THE COMPETITOR ROW - required **[E3-28]**. Same metric, same window, filing-sourced.

**Metric A: the realized oil price, without derivative settlements, FY2025, against Brent of
$68.22** - the direct measurement of the claimed location advantage.
**Metric B: the filer's own headline per-Boe operating/production cost, FY2025** - the direct
measurement of **[E2-58]**'s exception. Each filer's definition is named, because they differ.

| Company | realized oil, $/Bbl, FY2025, ex-derivatives | % of Brent $68.22 | headline operating cost, $/Boe | what that cost line is | production, MBoe/d | source |
|---|---|---|---|---|---|---|
| **CRC (subject)** | **$66.52** | **97.5%** | **$25.42** | "Operating costs" = energy ($374M) + non-energy ($859M); excludes field transport $0.81 and taxes other than income $4.03 | 138 | 10-K FY2025, acc. 0001609253-26-000051 |
| OVV (Ovintiv), USA segment | $65.66 | 96.2% | $9.95 | "Average Production Cost per BOE", USA | 205 (total co.) | 10-K FY2025, acc. 0001193125-26-064309 |
| MTDR (Matador) | $64.99 | 95.3% | $9.13 | lease operating $5.50 + transportation & processing $0.88 + midstream operating $2.75 | 207 | 10-K FY2025, acc. 0001520006-26-000002 |
| MGY (Magnolia) | $63.18 | 92.6% | $6.96 | "Average lease operating costs per boe (including gathering, transportation)" | 100 | 10-K FY2025, acc. 0001698990-26-000005 |
| CVX (Chevron), **U.S. upstream** | $62.25 | 91.2% | $10.35 | "Average production costs, per barrel", U.S., Table IV | n/d (US segment) | 10-K FY2025, acc. 0000093410-26-000078 |
| CRGY (Crescent Energy) | $62.21 | 91.2% | $15.48 | "Average Production Costs per Boe", total | 260 | 10-K FY2025, acc. 0001866175-26-000026 |
| AMPY (Amplify Energy) | $60.76 | 89.1% | $20.99 | "Lease operating expense" per Boe | 18.4 | 10-K FY2025, acc. 0001104659-26-025299 |
| **BRY (Berry Corp) - FY2024, the last standalone year** | $73.70 *(vs Brent $79.86)* | **92%** *(the filing's own figure)* | **$24.31** *(LOE, unhedged; $34.21 in 2023)* | "Lease operating expenses", energy $11.21 + non-energy $13.10 | 25 | 10-K FY2024, acc. 0001705873-25-000018 |

**Peers named: 7**, against a US-listed upstream set numbering in the dozens. Buffett says eight
**[E3-28]**; I took seven and chose them to span the four things that could decide this question:
**the California twin operating the same rocks (BRY)**, **the "major international oil company which
operate in California" that CRC's own filing names (CVX, at its U.S. segment)**, **the other
California producer (AMPY, offshore Beta)**, and **four diversified or shale independents (OVV,
MTDR, MGY, CRGY)** as the cost baseline. No peer was unavailable, so the moat class is **not
PROVISIONAL** - it is measured.
**BRY carries a window caveat, stated rather than hidden:** Berry ceased to be a registrant when
CRC bought it on 18 December 2025, so its last filed year is FY2024 and it is shown against FY2024's
Brent, in the FY2024 column, as its own 10-K reports it.

### WHAT THE ROW SAYS

**1. The location advantage is REAL and it is MEASURABLE. The 2026-07-16 run was right to record
it.** CRC realizes **97.5% of Brent**, the top of this row, against a spread running down to 89.1%.
Expressed in dollars: CRC nets roughly **$1 to $6 per barrel more than the other six**, and the
mechanism is the one the filing states - a landed barrel from overseas pays freight into
California, and CRC's does not.

**2. And it is a BASIN attribute, not a company advantage - which is exactly what the row is for.**
Berry, operating the same San Joaquin steamfloods with the same 54 steam generators, realized
**92% of Brent** on its own filing's own arithmetic, and states the reason in the same words:
*"California oil prices are Brent-influenced as California refiners import approximately 76% of the
state's demand from OPEC+ countries and other waterborne sources"* (BRY FY2024 10-K). **A rent that
accrues to every producer in the geography is a property of the geography.** It is not a moat
*over the competitors*, which is the only kind [E3-28] recognises. And CRC has now bought the one
neighbour it could have been measured against, which removes the comparison rather than winning it.

**3. The cost side is the opposite of [E2-58]'s exception, and it is not close.** CRC's operating
cost of **$25.42/Boe is the highest in the row** - **2.6x** MTDR's fully-loaded $9.13, **3.7x**
MGY's $6.96, **2.5x** Chevron's U.S. $10.35 - and it is matched only by the two other California
producers (BRY $24.31, AMPY $20.99). The mechanism is in Q1: CRC must **buy natural gas and burn
it** to raise steam before the heavy oil will move, so **$374 million of 2025 operating cost is
itself a purchased commodity.** [E2-58] asks for a cost advantage *"both wide and sustainable."*
**What the filings show is a cost DISadvantage, and a wide one.**

**4. The two effects do not net in CRC's favour. Built in full, both stacks named, FY2025:**

| | CRC | MTDR |
|---|---|---|
| revenue per Boe | $2,910M ÷ 50 MMBoe = **$58.20** | oil 43,699 MBbl × $64.99 + gas 191.3 Bcf × $2.08 = $3,238M ÷ 75,581 MBoe = **$42.84** |
| operating cost | (25.42) | lease operating (5.50) + transport & processing (0.88) + midstream (2.75) = (9.13) |
| taxes other than on income | (4.03) | (3.65) |
| field transportation | (0.81) | *(in the 0.88 above)* |
| G&A | (0.85) *(segment)* | (1.81) |
| **cash margin per Boe, pre-DD&A** | **$27.09** | **$28.25** |

CRC starts **$15.36/Boe ahead on revenue** - its barrels are 79% oil against MTDR's 58%, and it
gets the Brent-linked California price - and it gives back **$16.52/Boe on costs**. **The location
rent is smaller than the cost gap.** The "competitive advantage" the filing claims is real, it is
worth a few dollars a barrel, and it is more than consumed before the cash reaches the owner.
*(Definitional caveat, stated: MTDR reports NGLs inside the natural-gas stream rather than
separately, so its revenue line is built from the two components its 10-K gives. Both stacks use
each filer's own per-Boe table; neither is re-based.)*

**5. The advantage is not merely narrow - the filing shows the ground eroding under it in real
time.** A transportation-cost advantage over importers is worth exactly what the refineries that
buy the barrels are worth, and in the fifteen months to this filing:
- **Phillips 66 closed its Wilmington refinery** (October 2025);
- **Valero confirmed in January 2026 it will cease refining at Benicia**;
- **the San Pablo Bay Pipeline** - *"the primary inland pipeline carrying crude from California
  fields to Bay Area refiners"* - had shipments *"effectively suspended … reducing volumes to
  zero. The closure of this pipeline **effectively eliminated our access to Bay Area refineries**
  and we modified our marketing, transportation and shipping arrangements to reach alternative
  markets in Southern California. As a result, **we expect to experience higher transportation
  costs**"* (FY2025 10-K).
The company's own summary of the risk: *"The loss of refineries in the Bay Area and related
pipeline transportation capacity and any additional closures in the future could increase our
transportation costs and negatively impact realizations."* **[E4-32]** asks for the direction, not
the existence, and says the moat widened every year is *"the primary criterion of a great
business."* **This one is narrowing, on the company's own disclosure, and the narrowing mechanism
is the disappearance of the customer.**

### THE OTHER Q2 TESTS

- **Must the moat be continuously rebuilt? [E4-04], as scoped by the framework's own paragraph.**
  The framework names the excluded class directly: *"what 'enduring' excludes is the moat whose
  **basis must be periodically replaced** — rapid-change industries, **depleting assets**."* CRC is
  a depleting asset by construction. Its own production bridge shows **natural decline of (4), (7)
  and (6) MBoe/d in 2025, 2024 and 2023**, and the only line that ever offsets it is
  **"Acquisitions: 30, 34, —"**. That is the Rhodes Ridge case the framework names: **the spending
  buys a replacement deposit, it does not defend the same advantage.** Coca-Cola's advertising
  defends the same trademark; CRC's $1,293 million of cash and roughly 40% of its share count
  bought different rocks.
- **Does success depend on a great manager? [E4-23].** Not decisively; the assets are the story.
  Recorded here rather than at Q3 so a warning is not read as a compliment. **What the position
  DOES depend on is the operator's steam-injection and abandonment permits from CalGEM**, which is
  a regulatory dependence and not a managerial one.
- **[E3-46] - the second question about the business is a number: returns on capital.** Net income
  on year-end stockholders' equity, off the filed balance sheets, five years post-emergence:

  | | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|
  | net income, $M | 612 | 524 | 564 | 376 | 363 |
  | year-end equity, $M | 1,688 | 1,864 | 2,219 | 3,538 | 3,674 |
  | **return on equity** | **36.3%** | **28.1%** | **25.4%** | **10.6%** | **9.9%** |

  No goodwill sits in that denominator - the FY2025 balance sheet carries none - so book equity is
  already the **unleveraged net tangible** denominator **[E2-43]** asks for in an acquisitive
  filer. The series does what a commodity series does: it tracks the price. Brent ran $82.22 →
  $79.84 → $68.22 across 2023-2025 and the return fell with it, while the denominator grew by
  issuance. **[E2-58]** again: *"the ratio of supply-tight to supply-ample years"*, and 2025 was
  ample - the filing's own reason for the lower price is *"an increase in global oil production
  beginning in later 2025 as both OPEC+ and non-OPEC countries increased production."*
- **[E2-44], the two-characteristic test. Both fail.** *Can it raise prices when demand is flat and
  capacity is not fully utilized?* **No** - the price is Brent, set elsewhere; the filing does not
  even claim otherwise. *Can it grow dollar volume with only minor additional investment of
  capital?* **No** - the 60% production growth from 86 to 138 MBoe/d cost **$1,293 million of cash
  plus an all-stock merger that nearly doubled the asset base**.
- **[E4-37], the inverse metric.** Buffett measures a business by *"the agony they go through in
  determining whether a price increase can be sustained."* CRC does not have the agony, because it
  does not have the meeting: there is no price to raise. This sits **below** the agony case, not
  above it.
- **[E3-33] / [E5-28], untapped pricing power: NO, and the claim is not available.** [E5-28] scopes
  the class - *"If you name some business that has incredible pricing power, you're talking about a
  business that's a monopoly or a near monopoly"* - and the competitor row above is what a claim
  of near-monopoly would have to survive. CRC is the largest operator in California and still
  realizes an index price against a substitute that supplies 75% of its market.
- **[E2-53], the dominance class.** CRC's strategy section says *"We are the largest operator in
  California and currently operate all of our core oil and gas fields."* That is true and it is not
  [E2-53]. The newspaper *"itself, not the marketplace, determines just how good or how bad the
  paper will be"*; CRC determines none of its price. **Largest is not dominant when the marketplace
  still sets the number.**
- **[E4-36], which of the four causes of extreme success?** The record such as it is comes from
  **wave-riding**: high oil prices in 2021-2023 produced 25-36% returns on equity, and the ebb of
  2025 produced 9.9%. **[E3-51]**: *"when a surfer gets up and catches the wave … he can go a long,
  long time. But if he gets off the wave, he becomes mired in shallows."* **A surfing run is not a
  moat; the advantage lives in the wave.**
- **The row's limit, stated [E3-61].** The row shows position and cannot show conduct. It is not
  being asked to here: the failure is structural, not behavioural.

- Class: **[x] NONE** · Direction: **narrowing** - refinery closures and the San Pablo Bay pipeline
  suspension, both disclosed in this filing, shrink the customer base the transportation-cost
  advantage is measured against.
- **VERDICT: [x] OUT** - *evidence is here and the business fails; stop, permanent.*

**The grounds, each independently sufficient and each from a filed document:**
1. **[E3-03] criterion 2 fails on CRC's own competition paragraph.** A close substitute exists,
   arrives by ship, supplies over 75% of the market, and now sets the price CRC receives
   ("based directly on Brent prices").
2. **[E2-58]'s one exception was opened, measured against seven peers, and CRC is on the wrong
   side of it.** The disclosed transportation-cost advantage is worth about $1-6/Bbl of realization
   and is offset by an operating cost of $25.42/Boe, the highest in the row and 2.5-3.7x the shale
   peers. A cost *dis*advantage of that width is not *"a cost advantage that is both wide and
   sustainable."*
3. **The rent that does exist belongs to the basin, not to CRC**, which is why the only other
   California operator in the row shows the same two numbers.

**Asked aloud, as the framework requires on every non-IN verdict: "Can I name the document that
would resolve this?"** There is nothing left to fetch. The competition paragraph, the marketing
paragraph, the per-Boe cost table and seven peers' equivalent tables are all in hand and they agree.
This is **OUT**, not UNRESEARCHED and not UNKNOWABLE - the evidence is in and the business fails.

*(On [E4-04] and the 2026-09-20 verdict-form ruling: that ruling routes a name which **passes**
[E3-03] but whose durability cannot be judged from filings to UNKNOWABLE. CRC does not pass
[E3-03], so the ruling does not reach it. The depleting-asset finding above is recorded as
corroboration, not as the operative ground.)*

---
# ⛔ THE FILE IS CLOSED AT Q2.

**Operator rule 2: the hard sequence.** Q2 returned **OUT**, so no further verdict box is
ticked anywhere below this line, and **Q5 does not open.** Everything that follows was
gathered before the close or immediately after it and is recorded, per operator rule 2, as
**material beneath the close** - because throwing it away would mean the next reader has to
fetch it again, and because two of the findings below (the disclosed maintenance-capital
number and the spread rebuild) correct things this project's own tooling and screen row said.

**None of it is a verdict. None of it promotes anything. Q2 OUT is permanent.**

---
## Q3 MATERIAL - no verdict box ticked

**The weight case, declared anyway** *(this is how Q3 would have been scored, had the run
reached it)*: **Daily execution - NO.** An oil field is a have-to-be-smart-once asset;
[E3-43]'s magnified-manager class is the undifferentiated promise, not the producing well.
**Control - NO**, a marketable minority stake. **Leverage - NO**, on the numbers below.
So Q3 would have been a **qualitative OVERLAY**, not a gate. It is written here as an overlay.

### [E4-29] and [E4-22]'s third flag - scored on the 8-K EX-99.1, not on the 10-K

The FY2025 **10-K** is clean on this: the word EBITDA is not its headline. **The furnished
earnings release is not.** From the Q2 2026 release, **8-K of 2026-08-10, accession
0001609253-26-000127, Exhibit 99.1**, second headline bullet:

> "Reported net income of $514 million which includes the non-cash gain from changes in the
> fair value of outstanding commodity derivatives, **adjusted net income of $88 million and
> $338 million of adjusted EBITDAX**"

and the guidance table on the same document:

> "**Adjusted EBITDAX ($ millions) | $285 - $325 | $1,200 - $1,300**" - 3Q26E and Total Year 2026E

**[E4-29] fires.** *"Trumpeting EBITDA … is a particularly pernicious practice. Doing so
implies that depreciation is not truly an expense, given that it is a 'non-cash' charge.
**That's nonsense.**"* And **[E5-41]** names the mechanism precisely for this business:
*"Depreciation is where you spend the money first … and record the expense later. And it's
**reverse float**."* CRC is the pure case - it spends cash to drill a well, the oil comes out
over years, and adjusted EBITDAX deletes the already-spent money. The X is worse than the
plain measure: EBITDA**X** adds exploration expense back too.

**[E4-22]'s third flag - trumpeted earnings projections - fires as well**, and with a stated
price assumption: full-year 2026 adjusted EBITDAX guidance of $1,200-$1,300 million, with
footnote 4 disclosing *"Total year 2026 guidance assumes Brent price of $84.51 per barrel."*
**[E5-30]** is the reason this matters beyond the year: *"once you start it, it's all over.
You can't quit … And forecasting earnings, I can't imagine anything more destructive."*

**[E4-27], the incentives, read from the proxy - DEF 14A filed 2026-03-18, accession
0001193125-26-114093.** The 2025 Annual Incentive Program scorecard:

> "Financial Results (40%): **Adjusted EBITDAX ($MM) 20.0%** … **Free Cash Flow ($MM) 20.0%**
> … E&P Cost Management (5%): E&P Capital Efficiency ($k/boepd) 5.0% … Sustainability (30%)"

and the definition the proxy itself gives:

> "**Free Cash Flow is calculated as Adjusted EBITDAX +/- working capital changes for the
> period and minus cash paid for interest, asset retirement obligations and capital
> investments. AIP adjusted FCF is not reduced by income tax payments.**"

So **40% of the cash bonus vests on two measures that both begin by deleting depreciation**,
and the second of them is explicitly *not* reduced by income taxes paid. The scorecard paid
out at **153.6%** for 2025 against an adjusted EBITDAX target of $1,130M and an actual of
$1,252M. Long-term incentives: *"60% of the annual long-term incentives to performance-based
stock awards"*, and those PSUs vest on *"the Company's cumulative Total Shareholder Return"* -
**[E3-50]**'s stock-price premise, recorded as a prompt to read and not as a finding.
*"Never, ever, think about something else when you should be thinking about the power of
incentives"* **[E4-27]**.

### What reads the other way, recorded because [E4-26] requires hunting hardest against the hypothesis I like

- **The adjustment runs in the honest direction.** Q2 2026 GAAP net income was **$514M** and
  the company's own adjusted figure was **$88M** - a $426M reduction, made because the GAAP
  number contains a non-cash derivative mark. A management optimising the headline would have
  done the opposite. **[E2-26]**'s half-owner test is met on that item.
- **The [E2-67] positive pole has a form here and the company supplies it.** Its ARO roll-
  forward prints its own revisions: *"Revisions of estimated cash flows (242) / (32)"*, with a
  stated reason for 2024 (*"efficiencies gained in how we perform our well abandonment"*). A
  filer that prints the direction of its own estimate changes is doing what [E2-67] praises.
  **The $242M downward revision in 2025 is nonetheless a large number created by an estimate
  and is flagged under [E2-50]** - *"Where 'earnings' can be created by the stroke of a pen,
  the dishonest will gather"* - as a prompt to read, never as a finding about these people.
- **Serial share issuance [E5-15]: NO.** The direction is the reverse. Shares outstanding went
  **91.1 million (2024) to 88.8 million (2025)** despite issuing 5,572,115 shares for Berry,
  because **$377M, $192M and $143M of stock was repurchased in 2025, 2024 and 2023**, and
  treasury stock rose from 18.5 million to 21.9 million shares. Since 2021 the release reports
  *"approximately $1,655 million to shareholders, including $1,180 million in share repurchases
  and $475 million in dividends."*
- **[E2-52], dividends funded by issuance: NO.** Cash dividends of $136M / $113M / $81M were
  paid alongside **net repurchases**, not net issuance.
- **[E4-30], the cash-tax tell: not fired, but not testable either.** Deferred tax provision was
  $85M / $71M / $35M against total tax on pre-tax income; CRC has large NOLs from the
  bankruptcy era. A falling cash-tax share here has an innocent mechanism on the face of the
  filing, so the tell does not read.
- **[E2-30], the institutional imperative - two of four would tick.** *"corporate projects or
  acquisitions will materialize to soak up available funds"*: **Aera (2024), Berry (2025),
  Crimson Midstream (announced 2026-08-10, $63 million cash), and a data-centre venture
  (the "Golden Valley Technology Hub" with Beacon Data Centers at Elk Hills, announced the same
  day)**. *"peer behaviour mindlessly imitated"*: the CCS leg and the data-centre leg are both
  sector-wide 2024-2026 behaviours. **[E3-40]**'s loss-of-focus vector is the one to watch here,
  and it is recorded without a verdict.
- **Buyback condition 2 [E5-08]** - repurchase at a material discount to conservatively
  calculated intrinsic value - **cannot be scored**, because this run has no intrinsic value:
  Q2 closed the file and Q5 never opened. Recorded as not scored, rather than guessed.

**No Q3 verdict box is ticked. A strong or weak Q3 could not have changed Q2 in either
direction** - the guardrail, [E2-37] and [E2-38]: *"a good managerial record … is far more a
function of what business boat you get into than it is of how effectively you row."*

---
## Q4 MATERIAL - no verdict box ticked

### The screen's `spread_caveat` rebuilt: EVERY window, BOTH (c) ends, in dollars

The screen row carried *"4-construction width only (3y/5y x two capex ends): CANNOT see
variation older than the 5-year window; rebuild it [E4-25]."* **Rebuilt, from the filed annual
values** (OCF, D&A, capital investments, SBC; 10-K XBRL cross-checked against the FY2025 filed
cash-flow statement for 2023-2025). **Note 2020 is absent from the filed series entirely** -
it is the Chapter 11 year - so every window below jumps that gap silently, which is itself
part of the finding.

| year | OCF | D&A | capex | SBC | **OE at (c)=D&A** | **OE at (c)=capex** |
|---|---|---|---|---|---|---|
| 2012 | 2,223 | 926 | 2,331 | 20 | 1,277 | **(128)** |
| 2013 | 2,476 | 1,144 | 1,669 | 33 | 1,299 | 774 |
| 2014 | 2,371 | 1,198 | 2,020 | 27 | 1,146 | 324 |
| 2015 | 403 | 1,004 | 401 | 34 | **(635)** | **(32)** |
| 2016 | 130 | 559 | 75 | 33 | **(462)** | 22 |
| 2017 | 248 | 544 | 371 | 29 | **(325)** | **(152)** |
| 2018 | 461 | 502 | 690 | 45 | **(86)** | **(274)** |
| 2019 | 676 | 471 | 455 | 32 | 173 | 189 |
| **2020** | - | - | - | - | **not filed - Chapter 11** | |
| 2021 | 660 | 213 | 194 | 19 | 428 | 447 |
| 2022 | 690 | 198 | 379 | 30 | 462 | 281 |
| 2023 | 653 | 225 | 185 | 48 | 380 | 420 |
| 2024 | 610 | 388 | 255 | 40 | 182 | 315 |
| 2025 | 865 | 511 | 322 | 39 | 315 | 504 |

**The screen's `level_note_oe` flag is CONFIRMED and its number is exact.** "EARLY HALF
STRADDLES ZERO - the pre-window years run from $-274.0M to" - **2018 at the capex end is
minus $274 million**, to the dollar. The screen was pointing at a real year and it was right.

| window | years | mean OE, c=D&A | mean OE, c=capex | width, $M | yield range on $4,709M |
|---|---|---|---|---|---|
| 3y | 2023-2025 | $292M | $413M | $121M | 6.21% - 8.77% |
| 5y | 2021-2025 | $353M | $393M | $40M | 7.51% - 8.35% |
| 7y | 2018-2025 | $265M | $269M | **$4M** | 5.62% - 5.71% |
| 9y | 2016-2025 | **$119M** | $195M | $76M | **2.52%** - 4.13% |
| 11y | 2014-2025 | $143M | $186M | $43M | 3.05% - 3.95% |
| 13y | 2012-2025 | $320M | $207M | $113M | 4.39% - 6.79% |

**The screen's caveat was exactly right and the four-construction width understated the
problem.** The screen saw a width of **$292M to $411M**. The full rebuild runs from **$119M
to $413M** - a factor of **3.5** on the same company - and the 7-year window's near-zero width
of $4M is a coincidence of two constructions crossing, not agreement. **[E4-25]**: *"Usually,
the range must be so wide that no useful conclusion can be reached."* This is that range.

**And most of that width is not measurement, it is the perimeter.** The 13-year row's $320M is
lifted by 2012-2014, which are **Occidental carve-out years** at three times today's
production; 2015-2018 are the pre-bankruptcy company; 2021-2023 are post-emergence CRC alone;
2024-2025 are two different mergers deep. **Six of thirteen filed years show negative owner
earnings on at least one construction.** A mean across them is an average of four companies.

### [E5-20] on the filing: the company publishes its own maintenance-capital number

**[E5-20]** asks whether spending depreciation keeps this company in place, and the brief
required the question be answered on the filing rather than from the category. **CRC answers
it itself**, in the 8-K EX-99.1 of 2026-08-10:

> "**Lowered California long-term maintenance capital outlook by reducing drilling, completions
> and workover capital expectations by approximately 5% to a $450 million to $475 million range
> with six drilling rigs**, compared to seven previously"

and, in the CEO's own words on the same page: *"we are now able to maintain flat California
production with fewer rigs and less maintenance capital."* The 2026 guidance table gives the
matching pair: **capital investments $520-$560M against DD&A of $520-$540M.**

**Three consequences, and the first one bites hard:**

1. **The capex end of the 2023-2025 band is INVALID, not merely optimistic.** Actual capital
   investments of **$185M, $255M and $322M** are all far below the company's own stated
   maintenance requirement of **$450-475M for California alone**. The reason is on the face of
   the 10-K - California stopped issuing new-well permits, and the filing records the
   resumption: *"Following the resumption of permitting for new wells in January of this year,
   we expanded our drilling program to include new well development in Kern County."*
   **Under-spending forced by a permit freeze is not owner earnings; it is deferred
   maintenance**, and [E2-23]'s (c) asks for what the business *"requires to fully maintain …
   its unit volume."* Note what this does to `tools/run.py`'s output: its **OE hi of $504M for
   2025 and $413M for the 3-year window** are built on that invalid end. The tool computed
   correctly and concluded nothing, which is its job; **the reader has to know the company's own
   8-K contradicts that end.**
2. **The D&A default [E3-44] happens to hold here, and for once the filing proves it rather
   than assuming it.** Guided 2026 DD&A of $520-540M sits inside guided capex of $520-560M and
   just above disclosed maintenance of $450-475M. CRC is not the railroad case where
   depreciation understates renewal; it is nearer the *"95% of American businesses"* case
   **[E2-41]**. **The shallow decline is why**, and it is a genuine asset-quality fact: the
   filing's own production bridge shows **natural decline of only (4), (7) and (6) MBoe/d** on
   bases of 110, 86 and 91 - roughly **4% to 8% a year**, against the 30%+ first-year declines
   of shale. Recorded as a real strength of these rocks, and it does not touch Q2.
3. **The honest owner-earnings figure, built with the company's own (c):**

   | construction | mean (OCF − SBC) | less (c) | owner earnings | yield on $4,709M cap |
   |---|---|---|---|---|
   | 3y 2023-2025, (c) = $450M | $667M | 450 | **$217M** | **4.61%** |
   | 3y 2023-2025, (c) = $475M | $667M | 475 | **$192M** | **4.08%** |
   | 5y 2021-2025, (c) = $450M | $660M | 450 | **$210M** | **4.47%** |
   | 5y 2021-2025, (c) = $475M | $660M | 475 | **$185M** | **3.94%** |
   | **current perimeter**: H1-2026 OCF $362M × 2 = $724M, less SBC ~$40M | $684M | 520 (2026 guided capital) | **$164M** | **3.48%** |
   | same, at the top of guided capital | $684M | 560 | **$124M** | **2.63%** |

### [E4-41] - the windfall, named and removed

**[E4-41]** requires favourable exogenous breaks to be named and stripped before the mean is
trusted, and this business has one running right now, in the direction that flatters. Realized
oil price without derivative settlements, from the filings:

| | 2023 | 2024 | 2025 | 1Q26 | 2Q26 |
|---|---|---|---|---|---|
| Brent | $82.22 | $79.84 | $68.22 | - | - |
| CRC realized oil, ex-derivatives | $80.41 | $76.92 | $66.52 | **$74.53** | **$91.55** |
| CRC realized oil, with derivatives | $65.97 | $75.66 | $67.51 | $69.37 | **$76.43** |

**2026 is a price spike year.** The company's own guidance assumes **Brent $84.51 for the full
year**, 24% above 2025's realized benchmark. **That is not earning power and the H1-annualised
figures above carry it.** The corpus's own instance is Berkshire stripping a no-megacat year and
a bond tailwind out of its own reported number.
**And the rule runs the other way too, which is why 2025 is not treated as a death:** $68.22
Brent was an ample-supply year on the filing's own reason (*"an increase in global oil
production beginning in later 2025 as both OPEC+ and non-OPEC countries increased production"*),
and a trough is not a death any more than a spike is earning power. **The honest read is the
middle: $185M to $234M of owner earnings across the constructions that use the company's own
maintenance number - roughly 3.9% to 5.0% on today's cap, against a 5.34% sovereign.**
Note also the hedge book: in 2Q26 derivatives gave back **$15.12 a barrel** of the spike
($91.55 to $76.43), so even the spike does not reach the owner in full.

### Great, good or gruesome **[E4-20]** - no box ticked

The evidence points at **gruesome**, and it is recorded as evidence, not as a verdict:
production grew **60% (86 to 138 MBoe/d)**; it cost **$1,293M of cash plus an all-stock merger
that "nearly doubled the size of our asset base"**; and segment profit **fell** across the same
window - **$922M (2023) → $815M (2024) → $688M (2025)** - with return on equity falling
**25.4% → 10.6% → 9.9%**. *"attracted by growth when they should have been repelled by it"*.
**[E4-43]** forbids over-reading this: the *good* class passes, and a business earning ~10% on
equity is not automatically the airline. But [E4-20]'s gruesome test is *"both pays an
inadequate interest rate and requires you to keep adding money"*, and both halves are on the
filings here.

**The carbon-management leg, judged on the filing and not on its promise [E5-40].** Segment
losses of **$(66)M, $(94)M, $(86)M** for 2023-2025 - about **$246 million** consumed - plus
CRC's share of Carbon TerraVault JV losses of **$9M, $12M, $6M**. Against that: *"Achieved
first carbon dioxide (CO2) injection and revenue at Carbon TerraVault I"* (8-K EX-99.1,
2026-08-10) and 2026 guided segment capital of **$10-18M**. **[E5-40]** makes cash consumption
gruesome only *"unless the cash they consume gets to earn a reasonable return"*, and there is
no filed return yet to test. **Recorded as a live question, and it did not travel into Q2.**

### Staying power - all three scored **[E5-11]**

1. **A large and reliable stream of earnings - large yes, reliable no.** The oil price series
   above is the answer. **[E5-29]** is honoured: volatility is not risk, and the coverage
   arithmetic below is what matters. But **[E3-55]**'s carve-out does *not* apply - the
   See's exception is for a business whose *endgame* is certain and whose yearly figure merely
   bounces. CRC's endgame is a price nobody can name.
2. **Massive liquid assets - no, and the ratio is unusual.** **$43 million of available cash**
   at 2026-06-30 against a $4.7 billion company; liquidity of **$1,322 million** is
   **$1,279 million of undrawn revolver** and $43M of cash. **[E5-39]** is the exact objection:
   *"We will never be dependent on **the kindness of strangers**."* A revolver whose borrowing
   base is redetermined against oil prices is precisely that kindness, and it is thinnest when
   it is needed most. **[E2-64]**'s offensive-strength test also fails: this balance sheet is
   not built to buy in the storm.
3. **No significant near-term cash requirements - the one that usually kills, and here it is
   the largest single item on the list.** **Asset retirement obligations of $1,033 million at
   2025 year-end** ($923M non-current plus current at 2026-06-30), of which **$120 million is a
   current liability**, against $43M of cash. CRC settled **$122 million** of ARO in 2025 and
   $94M in 2024, so the run rate is real cash, every year, forever, on wells that no longer
   produce. On top: **$1,281 million of long-term debt**, now at **7.000% (2034) and 7.250%
   (2035)** after the June 2026 refinancing which itself cost a **$28 million loss on
   extinguishment** and paid **104.125%** to call the 2029s.

**[E2-54]'s coverage test, run properly** - *"all interest, both payable and accrued, to be
comfortably met out of current cash flow **net of ample capital expenditures**"*:
H1-2026 OCF **$362M**, less capital investments **$280M**, leaves **$82M** for the half year
against roughly **$46M** of half-year interest on $1,300M at ~7.1%, **plus $60M** of ARO
settlement at the 2025 run rate. **It does not comfortably clear**, and that is in a half-year
with a **$91.55** realized oil price. Leverage is named and quantified rather than screened:
debt **$1,281M**, ARO **$1,033M**, equity **$3,402M** (2026-06-30). **[E3-52]** is the right
distinction and it cuts against CRC here - the ARO is *not* the covenant-free, customer-prepaid
liability Berkshire's float is; it is a legally mandated, regulator-supervised, inflation-linked
obligation with California financial-assurance rules behind it, and the 10-K says so:
*"California law imposes stringent financial assurance requirements on persons who acquire the
right to operate a well or production facility in California."*

### The named way this business dies **[E2-27, E3-24]** - recorded, with no verdict

**The mechanism is not the oil price. It is the customer.** CRC's whole disclosed advantage is
a transportation-cost edge over waterborne imports, which is worth exactly as much as the
California refineries that buy the barrels - and those are closing on a schedule the filing
itself publishes. **Phillips 66 Wilmington closed October 2025. Valero Benicia confirmed
cessation in January 2026. The San Pablo Bay Pipeline's volumes went to zero in December 2025,
which "effectively eliminated our access to Bay Area refineries."** The filing counts what is
left: *"six major petroleum refineries will remain in California … **Five of these refineries
currently purchase California crude oil.**"*

**Quantified from filed figures, and the arithmetic is modelled on [E3-24]'s own worked form.**
CRC produces ~50 MMBoe a year and sells nearly all of its California crude into five remaining
buyers. Take **a 10% widening of the realized discount to Brent** - from 97.5% to 87.5%, which
is *below* where Amplify already sits today at 89.1% and would follow from southbound-only
transport, the higher transportation costs the filing already says it *"expects to
experience"*, and one more refinery leaving. On 40 MMBbl of oil that is **about $270 million a
year of revenue with no offsetting cost reduction** - set against owner earnings of **$185M to
$234M** on the company's own maintenance capital. **A ten-point realization loss erases the
whole of owner earnings and more, while $1,033 million of asset-retirement obligations and
$1,281 million of debt stay exactly where they are.** The company does not dispute the
direction: *"The loss of refineries in the Bay Area and related pipeline transportation capacity
and any additional closures in the future could increase our transportation costs and negatively
impact realizations and materially adversely affect our business, financial condition, results
of operations or cash flow."*

**Likelihood, in the corpus's vocabulary: a real possibility.** Not "likely" - five refineries
still buy, CRC can rail and truck southbound, and 1.1 million barrels a day of California
refining capacity is about four times in-state production. Not "a low-level possibility" -
three of the steps have **already happened inside fifteen months**, and each was announced, not
forecast. **[E4-40]** is the discipline that sets this at "real possibility" rather than lower:
*"focusing on experience, rather than exposure"* is the named failure mode, and CRC's benign
realization history (98%, 96%, 98% of Brent) is experience. The exposure is five buyers and one
suspended pipeline.

**Against the survival shapes index.** The nearest are **#20 THE WAVE** (the record comes from
the price cycle, not from position - [E3-51]) and **#17 THE PERMIT** (the state rations the
right to operate at the supply end). Neither is quite it: this is a death at the **demand** end,
where the only local buyer of a locally-priced product is legislated and economically retired
while the producer's obligations remain. **No new shape is added and no instance is entered in
the index**, following the PAGP and CALM precedents recorded there: *entering a Q2-closed run's
observation as a Q4 instance would make the index say something this run file does not.* The
observation is recorded here and in the fold so the next reader finds it.

---
## Q5 - NOT OPENED

⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 is **OUT**. The arithmetic below is
carried because the yields were already computed at Q4 and because the operator's instruction
is that every run end with a price and a pass/fail. **It carries no entry language and no
ranking position, and no box is ticked.**

### COMPUTATION — NOT A CLEARANCE

- price **$53.02** (2026-09-21, aggregator, flagged) × **88,819,893** shares
  (10-Q cover, acc. 0001609253-26-000130) = **cap $4,708.6M**
- sovereign **5.34%** USD, 09/18/2026, US Treasury daily par yield curve
- owner earnings, on the company's own disclosed maintenance capital of $450-475M:
  **$185M to $234M** → **3.94% to 4.97%**
- owner earnings, current perimeter, H1-2026 annualised less 2026 guided capital:
  **$124M to $164M** → **2.63% to 3.48%**, and that is at a guided **Brent of $84.51**
- the widest honest band across every window and both (c) ends: **$119M to $413M** →
  **2.52% to 8.77%** - **[E4-25]**: a range this wide *is* the conclusion
- **against the sovereign: minus 1.4 to minus 0.4 points** on the constructions that use the
  company's own maintenance number; **the whole band straddles the bond** and the bottom of it
  is **2.6 points below** it.
- **against the ~10% floor [E4-28]: no construction reaches it.** The highest number any
  construction produces is 8.77%, and it is the one built on a capex end the company's own 8-K
  contradicts.

**No margin of safety is applied, no bar is chosen, and no windage is spent, because there is
nothing to apply it to: Q2 closed the file on the business.** Recording the arithmetic is not
a valuation and it is not a ranking. **[E5-42]**: Q2-Q4 judge the business and only Q5 judges
the price, and this run never reached the price.

---
## Q6 - NOT OPENED · THE REVERSAL CONDITION, IN WORDS

A name that failed on the **business** gets no price alert; a price band on CRC would be a
category error (the QLYS ruling). **The reversal condition is written instead, and it is a
condition about the business, not about the quote:**

**CRC's Q2 would have to be re-opened if, and only if, a filed document showed the disclosed
transportation-cost advantage becoming a company advantage rather than a basin one, wide enough
to clear [E2-58]'s exception.** Concretely, all three of:
1. **operating cost per Boe falling below roughly $15** - the level at which CRC's cost stack
   stops being the highest in its own competitor row - and holding there through a full price
   cycle rather than one synergy year;
2. **realized oil price holding at or above ~98% of Brent** *while* the California refinery
   count stops falling - i.e. the rent surviving the loss of the buyers it is measured against;
3. **a disclosed contractual structure** (long-term, priced off something other than Brent)
   that replaces index pricing with an administered one - which, if it appeared, would be
   **[E2-59]**'s regime moat and would belong to the regime, not to CRC.

**None of these is a price.** The thing to watch, per **[E4-32]**, is the *direction* of the
moat, and the direction is currently set by refinery closures.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. **Q1 IN, Q2 OUT, file closed.**
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests
      entirely on figures read off the filed FY2025 10-K.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives - **none was returned.**
- [x] Every UNKNOWABLE verdict states what cannot be known - **none was returned.**
- [x] Step 0: the filing was read, with accession number; **three** figures were cross-checked
      (OCF, capital investments, SBC) against the filed statement and the footnote.
- [x] Owner earnings on a multi-year mean; **six** windows stated; capex band disclosed as a
      judgment **and corrected against the company's own disclosed maintenance figure**.
      *Recorded beneath the close; no Q4 box ticked.*
- [x] Competitor row filled - **seven peers, all filing-sourced. Not PROVISIONAL.**
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury),
      dated 09/18/2026, **struck fresh this run**.
- [x] Value stated as a round-number range, not a point estimate - and headed
      **COMPUTATION — NOT A CLEARANCE**, carrying no entry language.
- [x] One bar chosen, not both - **neither**, because Q5 did not open; windage count **zero**.
- [x] Prices dated; aggregator used for the live quote only and flagged.
- [x] Run committed to git, after every question.
- [x] **Every ledger id cited in this file was checked against `principle_ledger.csv` before
      it was written.**
- [x] **No em dashes in this run's own prose.** Quotations keep whatever the source has
      (PRIME RULE 1), and the Q5 heading is the required literal form.

## REGISTER
- Verdict: **[x] OUT (about the business)**
- One line: **Q1 IN / Q2 OUT. The disclosed proximity-to-refineries advantage is real and was
  measured for the first time against a seven-peer row: CRC realizes the highest share of Brent
  in the row at 97.5%, and carries the highest operating cost at $25.42/Boe, 2.5x to 3.7x the
  shale peers. The rent is worth $1-6 a barrel and the cost gap is $16.52 a barrel. The rent
  belongs to the basin, not to CRC, and the refineries it is measured against are closing.**

### PRIORS, RULED ON

- **REFUTED, in part: "the closest call of any E&P run in this project" (2026-07-16).** With a
  competitor row built, it is not close. The prior recorded a genuine disclosed advantage and
  was right to record it; it could not weigh it, because it measured nothing against anybody.
  **What the row adds is the scale:** the location rent is about $1-6/Bbl of realization and
  the operating-cost gap against the shale peers is $16.52/Boe. **A 2026-07-16 conclusion
  reached on one company's filing is upgraded, not merely repeated, by a 2026-09-21 conclusion
  reached on eight.**
- **CONFIRMED, and now on better evidence: the verdict.** The prior failed CRC on the
  pricing-power prong of [E3-03]. That still fails, and this run adds the [E2-58] exception
  test the prior never ran.
- **REFUTED: "the prior is a v4 run."** It is not. The 2026-07-16 file is a ~40-line v3.0
  four-name note with no perimeter, no competitor row, no owner earnings, no sovereign and no
  price. **It also predates the Aera merger (July 2024 close, but the FY2024 10-K was not
  filed until March 2025) and entirely predates Berry.** It was correctly treated as a
  hypothesis.
- **THE TALLY, COUNTED AND CORRECTED.** The prior claimed *"8 of 8 E&P names run … fail the
  franchise test."* **Counted from `Test Runs/` and the register, not inherited: this project
  has run NINE distinct upstream E&P registrants** - APA, COP, DVN, EOG (all 2026-07-15, all
  closed at Gate 2 on the *"no close substitute"* prong, verified by reading all four files);
  MTDR, CRC, OVV, MGY (2026-07-16, the v3.0 four-pack); and OXY (2026-09-01, register entry
  reads *"FAIL at Q2 (OUT, ON THE BUSINESS)"*). **MTDR was re-decided under v4.1 on 2026-08-31
  and closed Q2 OUT.** So the honest statement is **nine distinct names, nine closed at the
  franchise question**, of which three (MTDR, OXY, and now CRC) were decided under v4/v4.1 with
  a competitor row. **CRC is a re-run of the ninth, not a tenth name.** The prior's "8 of 8"
  was true when written and is now stale by one.
- **RESOLVED: the `deal_note`.** Three Item 1.01 8-Ks since 2026-03-02, opened one by one:
  **2026-03-23 (acc. 0001609253-26-000084)** - $350M add-on of 7.000% notes due 2034 to redeem
  8.250% 2029s; **2026-04-17 (acc. 0001609253-26-000086)** - Ninth Amendment to the credit
  agreement; **2026-06-26 (acc. 0001609253-26-000120)** - $550M of 7.250% notes due 2035 to
  redeem the remaining 2029s at 104.125%. **All three are refinancings. There is no live
  merger agreement and the ROKU finding does not apply: the quote is an owner-earnings price,
  not a deal spread.** The screen's rule of thumb ("open them only if something else is odd")
  was followed and the answer was benign.
  *A fifth perimeter change was found elsewhere, in the 8-K EX-99.1 rather than in an Item 1.01
  filing: the **Crimson Midstream Holdings acquisition, $63 million cash, announced
  2026-08-10.** Small, and it does not change the verdict, but it is the fifth transaction in
  two years and it belongs in the [E2-30] record above.*

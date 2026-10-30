# Company Run — DT Midstream, Inc. (DTM) — 2026-09-28
**WAVE 7, name 91 of 218 (the first name in `Screens/_daily/_wave7_order.txt` not in the done file; the done file held 90 lines, last TCMD, counted from the file). Claimed at dispatch 2026-09-28 by an unattended run agent (the template copied and committed before any fetch).**

**VERDICT: Q2 OUT.** Q1 IN. The file closes at Question 2, permanently, on the business: [E3-03] criterion (3) fails for
the FERC-tariffed third of the profit and criterion (2) is not shown for the unregulated gathering two-thirds. Q3 to Q6
are NOT scored; what was read beneath the close is recorded unscored.
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
a forecast **[E4-15, E3-32]**. DTM bills US customers in dollars under US contracts and FERC tariffs, borrows in
dollars and pays dollar dividends. Its equity-method pipelines NEXUS and Vector reach Ontario; the 10-K's
comprehensive-income line for foreign currency translation is $1M (2025) and $2M (2023), immaterial. Earnings
currency **USD**; no FX step.
- rate **5.49%** · date **09/25/2026** (the last posted business day; 09/26 and 09/27 are a weekend) · source
  **US Treasury daily par yield curve, 30-year, from the issuing authority**. `tools/_cache/sov_USD_treasury.csv`
  was deleted before `python tools/sources.py` ran, so the rate was fetched, not served from cache. FRED was not
  used. Struck fresh; not inherited from the brief or from the TCMD run.
- FX / ADR: not applicable.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes  [x] Item 1  [x] Item 1A
- **Annual report: Form 10-K for the year ended 2025-12-31, filed 2026-02-19, accession 0001842022-26-000003**
  (`dtm-20251231.htm`). Also read for the series and the carve-out: the 10-Ks for FY2021 (0001842022-22-000006),
  FY2022 (0001842022-23-000006), FY2023 (0001842022-24-000003) and FY2024 (0001842022-25-000003).
- **Newest periodic: Form 10-Q for the quarter to 2026-06-30, filed 2026-07-30, accession 0001842022-26-000009**
  (`dtm-20260630.htm`); and the 10-Q to 2026-03-31 (0001842022-26-000006).
- **Furnished releases, for [E4-29]**: 8-K filed 2026-07-30, accession 0001140361-26-030142, EX-99.1 and EX-99.2
  (Q2 2026 results); 8-K filed 2026-02-19, accession 0001140361-26-006115, EX-99.1 and EX-99.2 (FY2025 results).
- **Proxy: DEF 14A filed 2026-03-26, accession 0001140361-26-011280.**
- **Deal-shaped filings read**: 8-K filed 2024-11-19 (0001140361-24-047312, EX-99.1, the $1.2B Midwest pipeline
  purchase from ONEOK), 8-K filed 2024-12-31 (0000947871-24-001058, Item 2.01, the closing), 8-K filed 2021-07-01
  (0001193125-21-205933, the separation from DTE Energy).
- **Figures cross-checked against the filed statement.** The tagged `NetCashProvidedByUsedInOperatingActivities`
  for FY2025 is 867,000,000; the 10-K's Consolidated Statements of Cash Flows print *"Net cash and cash equivalents
  from operating activities | 867 | 763 | 798"* for 2025, 2024, 2023. Also checked line by line: depreciation and
  amortization 258 / 209 / 182, stock-based compensation 26 / 23 / 20, plant and equipment expenditures (426) /
  (350) / (772), and *"Acquisition accounted for as a business combination (and purchase price adjustment) | 10 |
  (1,198) | —"*. Every tag equals the printed figure.

**Price and shares.**
- Price **$122.28**, NYSE close **2026-09-25** (Friday), Yahoo chart endpoint via `tools/sources._chart`,
  `regularMarketTime` 2026-09-25 20:00 UTC checked. **Aggregator, used for the live quote only, flagged.**
- Shares **102,015,296**: the cover of the **10-Q for the quarter to 2026-06-30, filed 2026-07-30, accession
  0001842022-26-000009**, reads *"Number of shares of common stock outstanding as of June 30, 2026: [...] Common
  stock, par value $0.01 | 102,015,296"*; the balance sheet of the same filing reads *"102,015,296 and 101,673,925
  shares issued and outstanding as of June 30, 2026 and December 31, 2025"*. `python Screens/cover_shares.py DTM`
  returned the same count from the same accession. **One class**: 550,000,000 common authorised; preferred
  *"50,000,000 shares authorized, and no shares issued or outstanding"*. Nothing summed.
- **Market cap: $122.28 x 102,015,296 = $12,474.4M.**

**Deal check.** The filer list from 2021 to 2026-09-28 carries no S-4, DEFM14A, SC TO-T or 425. The deal-shaped
filings are DTM buying: the Millennium 26.25% interest from National Grid ($552M, closed 2022-10-07), the Clean
Fuels gathering asset ($12M, 2024-07-01) and the Midwest Pipeline Acquisition from ONEOK ($1.2B, closed
2024-12-31). **The quote is an owner-earnings price, not a spread.**

**Separation and perimeter, established before any window is used.** The FY2021 10-K, Note 1: *"For the periods
prior to the Separation, the Consolidated Financial Statements and Notes to Consolidated Financial Statements were
prepared on a carve-out basis using the consolidated financial statements and accounting records of DTE Energy."*
DTE distributed 96,732,466 DTM shares on 2021-07-01. So **2019, 2020 and the first half of 2021 are carve-out;
2022-2025 are the only four full standalone years.** Two perimeter changes sit inside the series: the Haynesville
gathering business (Blue Union and LEAP, bought 2019-12-04 from Momentum Midstream and Indigo Natural Resources
for a fair value of *"$ 2.74 billion"*, *"$ 2.36 billion paid in cash and an estimated $ 380 million of contingent
consideration"*, $2,296M on the tagged 2019 acquisition line; FY2021 10-K Note 4: *"The acquisition was financed
by DTE Energy."*), and the three ONEOK pipelines, whose cash flows begin
on 2025-01-01. **No cash-flow year before 2025 carries the current perimeter**, and 2019 carries almost none of
the Haynesville business.

---
## THE SCREEN ROW — carried UNLABELLED, a set of claims and not a finding

From `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`: `cap_m 13214 · oe_bottom_m 270 · oe_top_m 570 ·
spread 1.109 · yield_bottom 0.0205 · vs_sovereign -0.033 · growth_required 0.0795 · level_shift 1.42 "no step" ·
best_year_dep 0.048 · level_shift_oe 1.04 · best_year_dep_oe 0.099 · years_filed 7 · acq_note "NET CASH INFLOW on
the acquisition line ($1,208M, 9% of cap) - cash acquired exceeded cash paid, so the CONSID[...]" · spread_caveat
"4-construction width only [...] rebuild it [E4-25]" · newest_periodic 2026-06-30`. Each field used is reproduced
or refuted below; the list of screen errors is gathered at the end of the file.

**The acquisition note is refuted at Step 0, from the filed statement.** The tagged
`PaymentsToAcquireBusinessesNetOfCashAcquired` is **+1,198 for 2024 and −10 for 2025**; the 10-K prints the same
line as *"(1,198)"* in 2024 and *"10"* in 2025. A positive value of a PAYMENTS tag is an outflow. **2024 was a
$1,198M cash payment** (the ONEOK pipelines, financed, in the FY2024 10-K's words, by *"4,168,750 common shares
[...] net proceeds of approximately $406 million"*, *"5.800% senior secured notes due 2034 in aggregate principal
amount of $650 million"* and the revolver), and **2025 was a $10M purchase-price adjustment received**. $1,208M is
the difference of the two tagged values (1,198 − (−10)), which is no quantity at all. There was no net cash inflow,
and no cash acquired exceeding cash paid. **Screen error.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics, in my own words.** DTM owns steel pipe, compressors and one storage field, and rents capacity in
them. It never owns the gas: it is paid to move or hold somebody else's molecule. Two kinds of rent.
- **Pipeline segment (55% of 2025 consolidated revenue; $370M of the $441M 2025 net income attributable to DTM,
  84%).** Long-haul interstate pipe (Guardian, Midwestern, Viking, Birdsboro wholly owned; Millennium 52.5%,
  NEXUS 50%, Vector 40% as equity-method joint ventures), the Washington 10 storage complex in Michigan, an
  intrastate Michigan system, and three "gathering lateral" pipes that carry gas from a producing basin to a
  big pipe (LEAP and Stonewall and Bluestone). Customers reserve capacity for years and pay a fixed monthly
  demand charge whether or not gas flows: *"approximately 92% of our Pipeline revenue was generated under firm
  service revenue contracts and approximately 99% of the revenue of our unconsolidated joint ventures was
  generated under firm service revenue contracts."* The joint ventures' profit reaches DTM as
  *"Earnings from equity method investees"*, $138M in 2025.
- **Gathering segment (45% of revenue; $71M of net income, 16%).** Small-diameter pipe laid into producers'
  acreage in the Haynesville (Blue Union) and the Marcellus/Utica (Susquehanna, Appalachia, Ohio Utica, Tioga)
  that collects gas at the wellhead. *"approximately 57% and 36% of our Gathering segment revenue was generated
  under firm revenue contracts and flowing gas, respectively"* — the flowing-gas part is paid by the unit and
  rises and falls with the producer's volume.
- Revenue = (reserved capacity x a demand charge) + (flowing volume x a fee). Cost = operating the pipe, property
  tax, interest on the debt that built it, and the capital that keeps it running. The commodity price passes
  through except for fuel retained in kind.

**The scarce input this business controls.** Rights of way and FERC certificates for pipe already in the ground
between specific supply basins and specific markets (Chicago, Wisconsin and Minnesota utilities, Michigan and
Ontario, Gulf Coast LNG), plus contractual acreage dedications in the gathering systems. A rival must obtain its
own certificate and right of way to compete for the same path, and the filer says the Northeast approval process
*"has become increasingly challenging"*.

**Will the fundamentals look broadly the same in ten years?** The mechanism will: pipe, reservation charge,
volume fee. The customers who fill the gathering systems drill wells that decline (the filer's own risk factor:
*"If new supplies of natural gas are not obtained to replace the natural decline in volumes from existing supply
basins in our areas of operation [...] the overall volume of natural gas gathered, transported and stored on our
systems would decline"*), and that is a Q2 and Q4 question, as it was for HESM. The business is *"relatively
simple and stable in character"* **[E3-31]** on its mechanism; the magnitudes are not settled here.

**The perimeter is part of understanding it.** The company that trades today has existed as a standalone
registrant since 2021-07-01; its present pipeline perimeter since 2025-01-01. Q1 is answered on the mechanism,
which is the same across both changes; the windows that span them are handled at Q4.

**VERDICT: [x] IN**

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that *"(1) is needed or desired; (2) is thought by its customers to have
> no close substitute and; (3) is not subject to price regulation."* **[E3-03]**

### Where the profit is, before any criterion is scored

A franchise test applied to "DTM" without first asking which assets earn the money would score a blend. The
filer's own furnished reconciliations (8-K 2026-02-19, EX-99.1) split 2025 Adjusted EBITDA of **$1,138M** into
**Pipeline $786M (69%)** and **Gathering $352M (31%)**. Inside Pipeline, the filings let three pieces be named:

| Piece of the 2025 profit | Size, filed | Who sets the price |
|---|---|---|
| Joint-venture interstate pipes (Millennium 52.5%, NEXUS 50%, Vector 40%) | *"EBITDA from equity method investees"* **$276M** (35% of Pipeline Adjusted EBITDA); earnings from them $138M | FERC tariffs: they *"provide interstate natural gas transportation or storage services in accordance with their FERC-approved tariffs"* |
| Guardian, Midwestern, Viking (bought 2024-12-31) | revenue **$212M** of Pipeline's $687M (the MD&A's variance line); about **$114M** EBITDA on the purchase announcement's *"approximately 10.5x 2025 EBITDA multiple"* on $1.2B | FERC cost-of-service, ASC 980 (below) |
| Birdsboro, Washington 10 storage, the Michigan intrastate system, and the gathering laterals LEAP, Stonewall, Bluestone | the remainder of Pipeline, about $396M, not split further in any filing read | Birdsboro FERC tariff; storage FERC *"market-based rate authority"*; Michigan intrastate state-regulated; the laterals *"not subject to FERC jurisdiction"* |
| Gathering (Blue Union in the Haynesville; Susquehanna, Appalachia, Ohio Utica, Tioga in Appalachia) | **$352M** | negotiated with producers; state *"complaint-based rate regulation"* only |

So **at least about a third** of the profit ($276M + about $114M, of $1,138M, 34%) is earned under FERC-set or
FERC-tariffed rates, and **at least 31%** (Gathering) plus an unsplit share of Pipeline is earned from producers
on unregulated gathering pipe. **The PAGP finding ("the majority of our pipeline profits") does NOT transfer on
its proportion; it was tested and DTM's FERC share is a minority.** The verdict therefore cannot rest on criterion
(3) alone, and each part is scored.

### THE STRONGEST EVIDENCE AGAINST THE LEADING READING — written first (operator rule 9, [E4-26], [E3-41])

The leading reading after the filings was OUT. The case against it, as strongly as the filings make it:
1. **Customers pay whether or not gas flows.** *"approximately 92% of our Pipeline revenue was generated under firm
   service revenue contracts and approximately 99% of the revenue of our unconsolidated joint ventures"*; firm
   contracts are *"typically long-term and structured using fixed demand charges or MVCs with fixed deficiency fee
   rates."* Customers also prepay: contract liabilities rose from $129M (2024-01-01) to $185M (2025-12-31), *"prepayment
   amounts from customers under various long-term revenue contracts on Ohio Utica Gathering, Appalachia Gathering,
   Blue Union Gathering and LEAP."*
2. **Customers are asking for more of it, for twenty years.** The Guardian G3 expansion (*"537 MMcf/d or
   approximately 40% from current capacity"*) is *"anchored by 20-year negotiated rate precedent agreements with
   investment-grade utility customers"*; the FY2025 release adds a Viking expansion. A negotiated rate is not a
   cost-of-service rate: *"our interstate pipelines may also charge negotiated rates that may be above or below the
   recourse rate"*, and the storage complex runs on *"market-based rate authority"*.
3. **New pipe is hard to build.** *"The approval process for storage and transportation projects located in the
   Northeast has become increasingly challenging, as such projects in this region tend to face heightened opposition
   and permitting scrutiny."* A certificate and a right of way already in the ground are a barrier to a rival.
4. **The filer says regulation does not bind it competitively**: *"we believe the regulatory burden does not currently
   affect our competitive condition."*
5. **The gathering half is growing again.** 10-Q Q2 2026: six-month gathering revenue *"increased $57 million [...]
   primarily due to higher volumes of $27 million [...] on Blue Union Gathering, higher Appalachia Gathering volumes of
   $16 million"*; LEAP phase 4 took the Haynesville header to 2.1 Bcf/d toward LNG demand.
6. **Pipeline-segment return is near the long-haul peers.** Pipeline operating income plus equity earnings over
   segment total assets: 7.2% (2021), 7.9%, 9.4%, 8.4%, **10.4% (2025)**, against Kinder Morgan 10.4% and Williams
   10.4% on the row's broader metric below.

That is a real case: needed, desired, contracted, hard to duplicate. It is weighed against what follows.

### (3) Not subject to price regulation — FAILS for the FERC third, in the filer's own words

Note 17, 10-K FY2025, verbatim:
> *"Guardian, Midwestern and Viking are subject to rate regulation and accounting requirements of FERC. The regulated
> operations of each of these subsidiaries have rates that are (i) established by independent, third-party regulators,
> (ii) set at levels that will recover our costs when considering the demand and competition for our services and
> (iii) charged to and collectible from our customers."*

And the regulator has used the power, twice, against this filer's price:
> *"The most recent approved rate proceeding for Guardian included a max tariff rate reduction of approximately 13%,
> effective April 1, 2025."* (10-K FY2025) · *"[...] and an additional 5 % reduction effective April 1, 2026."*
> (10-Q Q2 2026, Note on Regulatory Matters)

For every FERC pipe, including the joint ventures: *"Under the NGA, rates charged by interstate pipelines must be just,
reasonable, and not unduly discriminatory or preferential. For interstate pipeline transportation services subject to
cost-of-service regulation, the recourse rate is the maximum rate an interstate pipeline may charge"*; and the negotiated
rate that point 2 above relies on has a condition written into it: *"A prerequisite for allowing the negotiated rates is
that negotiated rate customers must have had the option to take service under the pipeline's recourse rates."* The
customer always holds the regulator's price as its alternative, and *"Existing rates [...] may be challenged by a complaint
filed by interested persons, including customers, state agencies or FERC, under Section 5 of the NGA."* **This is
[E2-59]'s regime, and for this piece it is the CAP**: the framework's rule is *"Regulation caps a franchise ([E3-03]
criterion 3) and floors a commodity business; neither creates the class."* The OTTR precedent (2026-09-19) failed a
cost-of-service electric utility on criterion (3) *"by definition"*; Guardian, Midwestern and Viking are the same kind
of asset under the same accounting (ASC 980), and the PAGP precedent (FERC-indexed liquids tariffs) is followed on
kind, distinguished on proportion.

### (2) No close substitute — NOT SHOWN for the unregulated two-thirds, and the filer says why

**Gathering.** Item 1, verbatim: *"Our Gathering operations compete for customers based on geographic location,
reputation, operating reliability and flexibility, price and service offerings [...] We mitigate the risk of
competition by signing acreage dedications, entering firm revenue contracts [...] Our primary competitors include other
independent midstream companies with gathering operations and producer owned systems."* The substitute is named twice:
a rival gatherer, and the producer's own pipe. What holds the customer is a dedication contract, not a belief that no
substitute exists. **Gathering laterals** (inside Pipeline): *"Our primary competitors [...] in the gathering lateral
pipelines market include major interstate pipelines and midstream companies that can transport and gather natural gas
volumes between interstate systems and between central delivery points within a basin."*

**The price record of the unregulated half says the same.** Gathering revenue per Mcf, from the filed segment revenue and
the filed average throughput (*"average throughput from the Gathering segment was 3.1 Bcf/d and 2.9 Bcf/d"*, and the
same sentence in each 10-K):

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Gathering revenue ($M) | 534 | 581 | 545 | 538 | 556 |
| Average throughput (Bcf/d) | 2.8 | 3.1 | 3.0 | 2.9 | 3.1 |
| Revenue per Mcf ($) | 0.523 | 0.513 | 0.498 | 0.508 | 0.491 |
| Gathering operating income ($M) | 230 | 264 | 229 | 210 | 199 |
| Gathering capex ($M) | 120 | 252 | 517 | 277 | 250 |
| Gathering total assets ($M, year end) | 4,001 | 4,208 | 4,543 | 4,661 | 4,783 |
| Operating income / segment assets | 5.7% | 6.3% | 5.0% | 4.5% | **4.2%** |

- **[E4-55], units before dollars:** volume is flat (2.8 to 3.1 Bcf/d over five years) and the price per unit has
  **fallen** 6% (0.523 to 0.491). The FY2023 10-K names a price cut in the filer's largest system: *"Lower Blue Union
  Gathering revenues were driven primarily by lower deficiency fees of $23 million, lower recovery of production-related
  operating expenses of $12 million, lower rates of $9 million and lower production volumes of $5 million."*
- **[E2-44], the two-characteristic test, fails on both halves:** no price rise with demand flat (the rate fell), and
  no dollar growth with minor capital: **$1,416M of gathering capex 2021-2025** (against $605M of segment depreciation and
  amortization over the same years, which itself includes the amortization of the 2019 purchase's customer intangibles) bought revenue +4% and operating income **−13%**.
- **[E3-46], the number asked of the business:** 4.2-6.3% pre-tax operating return on the segment's assets, falling
  every year since 2022, at or below the 5.49% bond before tax. Segment assets carry the 2019 purchase's goodwill and
  intangibles; on **[E2-73]**'s underlying-asset reading the return is higher, and the direction is the same.

**One customer.** *"We have one key customer, Expand Energy"*: $563M, $596M, $560M, $555M and $560M of revenue in
2021-2025 (67%, 65%, 60%, 56%, 45% of the total; *"Customer A"* and Southwestern Energy in the earlier filings). Its
dollars have not grown in five years; its share falls only because the rest was bought. The volume behind it depletes,
in the filer's words: *"our customers must continually obtain adequate supplies of natural gas. If new supplies of natural
gas are not obtained to replace the natural decline in volumes from existing supply basins [...] the overall volume of
natural gas gathered, transported and stored on our systems would decline."*

### The HESM precedent, followed and distinguished

- **Followed on the depleting basis.** As at HESM (2026-09-20), the gathering earning basis is a column of gas the
  subject neither owns nor drills, replaced only by the customer's drill bit. **[E4-04]**'s scope names *"depleting
  assets"* among the moats whose *"basis must be periodically replaced"*, and **[E3-51]**'s surfing run is the form: the
  advantage lives in the Haynesville and Marcellus wave, not in the pipe. **[E4-36]** asks which cause the record
  comes from; for gathering it is wave-riding.
- **Distinguished on the administrator.** HESM's fee was written by its controlling customer (Chevron owned the general
  partner). DTM's gathering fees are negotiated at arm's length with unaffiliated producers; no related-party pricing
  was found. That makes the gathering price a **market** price, and the market price is the one that fell.

### THE COMPETITOR ROW — required [E3-28]

Metric: **(operating income + earnings from equity-method investees) / (net PP&E + equity-method investments +
intangibles), FY2021-FY2025, sum of numerators over sum of denominators.** Equity earnings are added because a third of
DTM's pipeline profit sits in joint ventures whose investment is in the denominator; the HESM/PAGP metric (operating
income alone) is also shown. Every cell rebuilt in this run from each filer's SEC companyfacts by
`Test Runs/_research 2026-09-28 DTM/peers.py` (output `peers_out.txt`); the subject's numerators and denominators
reconcile to its 10-K statements (operating income 614 / 489 / 471; equity earnings 138 / 162 / 177; net PP&E 5,766;
equity investments 1,253; intangibles 1,862 at 2025).

| Company | (op. income + equity earnings) / base | op. income / base | source |
|---|---|---|---|
| Hess Midstream (HESM) | 25.9% | 25.6% | companyfacts |
| MPLX | 22.5% | 20.1% | companyfacts |
| Western Midstream (WES) | 15.5% | 14.2% | companyfacts |
| Enterprise Products (EPD) | 14.6% | 13.7% | companyfacts |
| Antero Midstream (AM) | 14.5% | 12.4% | companyfacts |
| Targa (TRGP) | 12.3% | 12.3% | companyfacts |
| ONEOK (OKE) | 11.8% | 11.1% | companyfacts |
| Williams (WMB) | 10.4% | 8.8% | companyfacts |
| Kinder Morgan (KMI) | 10.4% | 8.7% | companyfacts |
| Energy Transfer (ET) | 9.4% | 9.0% | companyfacts |
| Equitrans (ETRN, FY2021-2023, acquired 2024) | 8.9% | 8.1% | companyfacts |
| **DTM (subject)** | **7.8%** | **6.0%** | own companyfacts, reconciled to the 10-K |
| Boardwalk Pipelines (BWP, a FERC interstate pipe) | 6.6% | 6.6% | companyfacts |
| Kinetik (KNTK) | 5.8% | 2.6% | companyfacts |

- **Peers named: 13**, the listed US gas and midstream filers with the same statements, plus two gas-pipeline specialists
  (Boardwalk, Equitrans). Buffett says eight; thirteen taken. Not rowed: TC Energy and Enbridge (40-F filers, IFRS, CAD),
  Momentum Midstream and the producer-owned gathering systems (private or unsegmented). **The unrowed are named with their
  obstacle; the class is not PROVISIONAL because thirteen same-statement filers already place the subject.**
- **DTM is twelfth of fourteen, at 7.8% against a peer median of 11.8%**, on the metric most favourable to it. Its best
  year (8.5%, 2025) is below the five-year figure of eleven of the thirteen peers.
- **Limits, stated.** DTM's base carries $1.86-2.08B of intangibles from the 2019 Haynesville purchase; without them the
  2025 figure is 10.7% (752 / 7,019), still below the median of peers that are not so adjusted (Antero Midstream carries
  $1.07-1.36B and would rise too). The equity-investment base fell by $903M from 2022 to 2024 when NEXUS and Millennium borrowed and
  distributed cash (investing-side *"Distributions from equity method investees"* $427M and $472M), which flatters DTM's
  later years. **[E3-61]**: the row shows position, never conduct.

### The other Q2 tests, scored

- **[E3-33] / [E5-28], untapped pricing power:** none. A third of the profit is under a recourse-rate cap the regulator
  lowered in 2025 and 2026; the unregulated gathering rate fell per unit.
- **[E4-37], the agony metric:** the FERC third needs a rate case to raise a price and lost the last one; the gathering
  half gave rate back in 2023. Past agony, into the price being set by someone else.
- **[E2-45], the attacker's test:** for the FERC pipes, the attacker is the regulator and the customer's Section 5
  complaint; for gathering, the filer names the attackers (rival gatherers, producer-owned systems).
- **[E2-53], dominance:** not claimed and not shown; DTM is a small operator (12th of 14) in every basin it serves.
- **[E4-32], direction:** the pipeline piece is widening by purchase and expansion (G3, Viking) at regulated or
  negotiated rates; the gathering piece is **narrowing** (return 6.3% to 4.2% on rising capital, rate per unit down).
- **[E4-23], key-person dependence:** none found. Not the defect here.
- **[E4-04], verdict form:** this is not the perimeter close. The durability of each part can be judged from filings and
  the filings judge it: the FERC part fails (3) on the business, the gathering part fails to show (2) and earns below the
  bond on its own assets. **OUT on the business, not UNKNOWABLE.**

### The three open operator questions, both readings written and not decided (PRIME RULE 5)

- **The ABT question ([E3-03] at the whole company or segment by segment).** *Segment by segment:* Pipeline (69%) is
  needed and contracted, but at least $276M + about $114M of its $786M sits under FERC-set or FERC-tariffed rates and fails
  (3), and its unregulated laterals face named substitutes; Gathering (31%) passes (3) and fails (2) as above, with a
  falling return below the bond. Each segment fails alone. *Whole company:* about a third under price regulation, two-thirds
  unregulated but with named substitutes and a return 12th of 14 among peers. Neither reading reaches IN. **The answer does
  not move this file.**
- **The ABBV question ([E3-03] criterion (3) at the company or the product level).** *Product (asset) level:* each FERC
  pipe fails (3); each gathering system passes (3) and is then scored on (2), where the filer names the substitutes.
  *Company level:* the FERC share is a minority, so (3) alone would not decide it, and the file turns on (2) and returns,
  which fail. **Does not move this file.**
- **The CAT question (whether [E2-58]'s wide-and-sustainable exception is for commodity products only).** The exception
  requires *"a cost advantage that is both wide and sustainable"*; on either reading it would need a measured advantage, and
  the competitor row places DTM twelfth of fourteen on return on deployed capital. **Does not move this file.**

### Class and verdict

- Needed or desired [x] · no close substitute [ ] (not shown for the unregulated two-thirds; the filer names rival
  gatherers and producer-owned systems) · not price-regulated [ ] (fails for the FERC third; Guardian's price cut 13% in
  2025 and 5% in 2026 by the regulator)
- Must the moat be continuously rebuilt? For gathering, yes: the volume basis is a depleting column of gas replaced only by
  the customer's drilling **[E4-04], [E3-51]**. Great manager required? No finding **[E4-23]**.
- Class: **[ ] WIDE  [ ] NARROW  [x] NONE** · Direction: FERC piece enlarged by purchase at a regulated return; gathering
  piece narrowing.

**VERDICT: [x] OUT**

**Asked aloud, per [E4-19]: can I name the document that would resolve this?** Nothing further needs to be fetched. The
10-K's Note 17 names the regulator as the price-setter for the pipes bought in 2024 and records the price cut; Item 1 names
the substitutes for the gathering business; the segment note and the throughput sentence give the gathering return and the
unit price; thirteen peers' filings place the whole company. **OUT on the business, permanent, and not the [E4-04]
perimeter close.** Q3 to Q6 are not scored; what was seen is recorded beneath the close.

---
## Q3 to Q6 — NOT SCORED. The file closed at Q2, OUT on the business.

⛔ Q3, Q4, Q5 and Q6 are not scored; no verdict below. What was read is recorded so a later reader does not have to
refetch it. Nothing here promotes or rescues the file **[E2-37, E2-38, E3-39]**.

---
## THE SCREEN ROW, ANSWERED

| Field | Screen | Finding |
|---|---|---|
| `acq_note` | "NET CASH INFLOW on the acquisition line ($1,208M, 9% of cap)" | **REFUTED** (Step 0): 2024 a $1,198M payment for the ONEOK pipes, 2025 a $10M adjustment received; $1,208M is the difference of the two tagged values |
| `cap_m` | 13,214 | reproduces at the 2026-08-28 close ($129.53 x 102,015,296 = $13,214M); at the 2026-09-25 close $12,474.4M |
| `oe_bottom_m` | 270 | reproduces as the **three-year capex end** (2023-2025: $6M, $390M, $415M) |
| `oe_top_m` | 570 | reproduces only as the three-year end that subtracts **total D&A including acquired-intangible amortization** ($57-60M a year of the 2019 purchase's customer intangibles); on the filed construction the three-year D&A end is **$628M** |
| `spread` | 1.109 | the width between the two ends of ONE window (570 / 270 − 1); the filing's every-window range is $264M to $702M |
| `yield_bottom`, `vs_sovereign` | 2.05%, −3.30% | struck on the stale cap and an older 5.35% sovereign; today the three-year bottom is 2.17% against 5.49% |
| `growth_required` | 7.95% | reproduces as ~10% less 2.05%; a derivative of the two fields above |
| `years_filed` | 7 | reproduces as seven tagged operating-cash years (2019-2025), but **2019, 2020 and the first half of 2021 are DTE carve-out** and 2019 carries almost none of the Haynesville business; standalone full years are four, current-perimeter years one. **The brief's hypothesis that the series pools pre-separation and acquired businesses is CONFIRMED** |
| `level_shift` / `level_shift_oe`, `best_year_dep` | 1.42 / 1.04 "no step", 0.048 | not relied on; the operating-cash series 390 → 867 contains two perimeter changes (the December 2019 purchase and the 2025 pipes) that a step test on the total does not separate |
| (not in the row) | — | the screen's acquisition flag reads only the business-combination tag and so **misses the $552M Millennium purchase of 2022-10-07** (an equity-method interest) |
| `spread_caveat` | "4-construction width only [...] rebuild it" | answered: seven windows and the TTM rebuilt at both (c) ends below |

---
## COMPUTATION — NOT A CLEARANCE

*Operator rule 3. Arithmetic beneath a closed file. It carries no entry language, no value range and no ranking.*

**Construction** (`oe.py`, output `oe_out.txt`): operating cash as filed, less stock compensation in full **[E5-06]**
(the cash-flow add-back; 1.0-3.0% of operating cash every year, so the [E3-70] grant-value question is immaterial here),
less (c) at two ends: **depreciation and amortization less the acquired-intangible amortization** (tagged
`AmortizationOfIntangibleAssets`, $24-60M) and **total plant and equipment expenditures** (which include growth). No
net-income proxy (operator rule 5).

| Year | Operating cash | SBC | D&A ex acquired amortization | Capex | OE, D&A end | OE, capex end |
|---|---|---|---|---|---|---|
| 2019 (carve-out) | 390 | 6 | 69 | 211 | 315 | 173 |
| 2020 (carve-out) | 597 | 6 | 97 | 518 | 494 | 73 |
| 2021 (half carve-out) | 572 | 12 | 108 | 140 | 452 | 420 |
| 2022 | 725 | 17 | 113 | 338 | 595 | 370 |
| 2023 | 798 | 20 | 125 | 772 | 653 | 6 |
| 2024 | 763 | 23 | 152 | 350 | 588 | 390 |
| 2025 (first year of the current perimeter) | 867 | 26 | 198 | 426 | 643 | 415 |

Every window ending 2025, against the cap of $12,474.4M: one year $415-643M (3.33-5.15%); two $402-616M; three
$270-628M (2.17-5.03%); four $295-620M; **five (the corpus default [E2-42]) $320-586M, 2.57-4.70%**; six $279-571M;
seven $264-534M (2.12-4.28%); **TTM to 2026-06-30 $454-702M, 3.64-5.63%** (TTM amortization taken at the 2025 annual
$60M, flagged). **Every window and the TTM: $264M to $702M, 2.12% to 5.63%, against the 5.49% bond.** The best end of
every annual window is below the bond; only the TTM D&A end touches it. None is near the ~10% figure the corpus quits
on **[E4-28]**.

- **(c) is a disclosed guess [E2-09], and the D&A end is suspect here [E5-20].** A pipeline is in the capital-intensive
  class the framework names with utilities; the filer is starting a *"multi-year modernization program for the acquired
  pipelines"* and PHMSA rules *"require the installation of new or modified safety controls and the implementation of new
  capital projects or accelerated maintenance programs"*. Management's own *"Maintenance capital investment"* in the
  furnished DCF reconciliations is **$34M, $22M, $29M, $30M, $62M (2021-2025)**, one-fifth to one-quarter of depreciation;
  it is a management definition (*"capital expenditures used to maintain or preserve assets or fulfill contractual
  obligations that do not generate incremental earnings"*), not a filed measure of what renewal requires, and this run does
  not use it.
- **Customer prepayments sit in operating cash** (contract liabilities +$97M in 2023, +$23M, +$26M), about $29M a year
  across the five-year window; **[E4-41]** would take them out of a judged level.
- **The JV recapitalisations are NOT in these figures**: NEXUS and Millennium borrowed and paid DTM *"the 371 million NEXUS
  financing distribution"* (2023) and *"the 416 million Millennium financing distribution"* (2024) through investing cash.
  They are borrowed money returned, not earnings, and they moved leverage into the joint ventures (DTM's share of JV
  interest expense: $11M in 2022, $56M in 2025).
- **The perimeter caveat binds the yield.** The cap buys the 2025 perimeter; the 2019-2024 years exclude the ONEOK pipes,
  so the long windows understate the current perimeter's cash and the one-year and TTM figures are the only
  like-for-like ones. Even on those, 3.33-5.63%.

---
## BENEATH THE CLOSE — Q3 MATERIAL, RECORDED WITHOUT A VERDICT

- **Weight case, not declared as a verdict:** leverage is the live determinant (long-term debt $3,324M; the Q4 notes below).
- **[E4-29] fires, in the releases and in pay.** Every furnished release headlines Adjusted EBITDA (*"Full year 2025
  Adjusted EBITDA of $1.138 billion, a 17% increase from 2024"*) and guides it two years out (*"Our Adjusted EBITDA
  guidance for 2026 is $1.155 to $1.225 billion [...] Our 2027 Adjusted EBITDA early outlook range is $1.225 to $1.295
  billion"*), which is also **[E4-22]**'s third flag and **[E5-30]**'s ratchet. The DEF 14A (0001140361-26-011280): the 2025
  annual incentive is **60% Adjusted EBITDA** (threshold $1,095M, target $1,125M, maximum $1,155M, result $1,138M, payout
  143.30%); performance shares (70% of the long-term grant) pay on relative TSR and a *"Leverage ratio [...] calculated as
  total Company net debt [...] excluding debt held by unconsolidated investees [...] divided by adjusted EBITDA"*. The
  incentive **[E4-27]**: a purchase at *"approximately 10.5x 2025 EBITDA"* raises the 60% metric the day it closes; the
  leverage metric excludes the JV debt the recapitalisations created. **No return-on-capital measure in pay.**
- **Metric adjusted after the event [E2-49], a prompt:** *"The Board exercised its authority to adjust the Company's leverage
  ratio for 2024 to exclude debt incurred as a result of the Interstate Pipelines acquisition"*, for the 2022-2024 grants.
- **Candor on the other side [E2-26]:** the DCF reconciliation removes both JV financing distributions as non-routine rather
  than counting them as distributable cash; Operating Earnings equalled reported earnings in 2025 with no adjustments.
- **Cash-tax tell [E4-30], a prompt:** cash taxes paid $24M, $22M, $12M, $5M on pre-tax income of $482M, $500M, $504M,
  $598M (5.0%, 4.4%, 2.4%, 0.8%, 2022-2025) while deferred income taxes rose to $1,270M. The FY2024 10-K records the
  Midwest purchase as *"a taxable deemed asset acquisition"*; the cause of the deferral was not traced further. Read, not
  scored.
- **Share count [E5-15]:** 96,732,466 distributed at separation, 102,015,296 at 2026-06-30 (+5.5%), mostly the
  4,168,750-share offering that funded the 2024 purchase. No buyback.
- **[E2-01] / [E2-43]:** return on total DTM equity (net income $441M on $4,736M) about 9.3% in 2025; the goodwill ($781M)
  and intangibles ($1,862M) are the wedge.

## BENEATH THE CLOSE — Q4 MATERIAL, RECORDED WITHOUT A VERDICT

- **Staying power [E5-11]:** the stream is contracted and large; liquid assets are small (cash $54M); near-term cash
  requirements are light: *"We have no debt maturing until 2029"* (the 2029 notes, $1,100M), revolver to December 2029.
- **Coverage [E2-54]:** 2025 operating cash plus cash interest less capex, $867M + $152M − $426M = $593M, against cash
  interest of $152M, **3.9 times**, before the JV-level debt.
- **Great, good or gruesome [E4-20]:** the gathering half carries the gruesome signature (capital added, $1,416M in five
  years, return on segment assets down from 6.3% to 4.2%); the pipeline half is the good class at a regulated return
  **[E4-43]**. Not scored.
- **Survival shape, as a signature WITHOUT a verdict (Q4 was never opened):** **#27 THE LICENCE** for the FERC third (a
  regulator, not the owner, decides the return on the capital it permits: Guardian's 13% and 5% cuts), and **#20 THE WAVE**
  for the gathering half (one customer, $555-596M a year since 2021, drilling a depleting basin).

---
## TOOLING, REPORTED NOT PATCHED (operator rule 8; a tool may never add a number)

- `tools/run.py DTM` (output `runpy_out.txt`) subtracts **total D&A including the acquired-intangible amortization** as its
  "OE hi" end (so its 570 is the screen's 570, not the filed construction's 628), defaults to a **three-year** window and prints
  the corpus's five-year window as "THE OTHER WINDOW"; its five-year figure ($315-534M) differs from this file's filed
  construction ($320M at the capex end; $528M with total D&A) by about $5M a year in opposite directions, source not traced.
- Its *"3. POINTS OVER THE SOVEREIGN -0.72 .. +1.80"* comes from an unprinted growth assumption (`points_over()`), while its own
  printed yield (2.17-4.57%) sits wholly below the 5.49% bond; reported, not used. Its *"2. GROWTH THE PRICE ASSUMES 9.2% (at a
  5.49% rate)"* is struck against the bond, not the ~10% floor [E4-28].
- It carries no perimeter warning: nothing in its output says that 2023-2024 exclude the pipes the cap now buys, or that 2019-2021
  are carve-out years.

---
## Q6 — THE REVERSAL CONDITION, IN WORDS (no band, no alert; FOLD step 4, the QLYS ruling)

The file failed on the business, so a price alert would be a category error. **The file reopens only on a filed change in
what the business is**: (1) the gathering segment showing, for five years in its own segment note, a rising price per Mcf
and a return on its assets well above the bond without capital growth outrunning depreciation; and (2) the FERC-tariffed
share of profit falling to where it no longer decides the whole, or the filings showing negotiated rates earning above
the recourse-rate cap across the interstate book. Neither is a price.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 OUT; Q3-Q6 not scored and labelled so.
- [x] No question marked IN carries an "unverified" or "provisional" caveat.
- [x] No UNRESEARCHED verdict. [x] No UNKNOWABLE verdict; the [E4-04] perimeter close was considered and refused in writing.
- [x] Step 0: the 10-K (0001842022-26-000003) and 10-Q (0001842022-26-000009) read; operating cash, D&A, SBC, capex and the
  acquisition line cross-checked against the filed statements.
- [x] Owner earnings on seven windows and the TTM at both (c) ends, beneath the close, headed COMPUTATION — NOT A
  CLEARANCE; **no net-income proxy**; SBC resolves in every year 2019-2025; the depreciation end excludes acquired-intangible
  amortization.
- [x] Competitor row filled: 13 SEC filers on one metric and one window, the subject reconciled to its 10-K; the unrowed
  named with their obstacle; class NONE, not PROVISIONAL.
- [x] Strongest evidence against the leading reading written first (operator rule 9).
- [x] Precedents read and applied or distinguished in writing: HESM, PAGP, OTTR. The ABT, ABBV and CAT questions written
  both ways and not decided.
- [x] Sovereign for USD from the US Treasury, dated 09/25/2026, struck fresh.
- [x] Value not stated (Q5 not opened). No bar chosen (Q5 not opened).
- [x] Price dated 2026-09-25, aggregator, flagged; shares from the latest periodic cover.
- [x] Every ledger id in this file checked present in `principle_ledger.csv` before writing.
- [x] Run committed to git after Step 0/Q1, after Q2, and at the close.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- One line: **DTM, 2026-09-28, FAIL AT Q2 (OUT on the business).** Price $122.28 (NYSE close 2026-09-25, aggregator,
  flagged) x 102,015,296 shares (10-Q to 2026-06-30 cover, 0001842022-26-000009) = $12,474.4M, against 5.49% (US Treasury
  30-year par, 09/25/2026). At least about a third of the profit is earned under FERC-set or FERC-tariffed rates
  ([E3-03] criterion (3) fails there; Guardian's maximum rate cut about 13% in 2025 and 5% in 2026), and the unregulated
  gathering two-thirds faces named substitutes at a falling unit price and a return on its own assets of 4.2%
  (criterion (2) not shown); DTM is 12th of 14 on return on deployed capital. Beneath the close, owner earnings $264-702M
  (2.12-5.63%) on every window. No band, no PORTFOLIO row.

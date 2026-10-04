# Company Run — Optex Systems Holdings, Inc. (OPXS) — 2026-09-28
**WAVE 7, name 92 of 218 (the first name in `Screens/_daily/_wave7_order.txt` not in the done file; the done file held 91 lines, last DTM, counted from the file). Claimed at dispatch 2026-09-28 by an unattended run agent (the template copied and committed before any fetch, commit 82df4266).**

**VERDICT: Q2 OUT.** Q1 IN. The file closes at Question 2, permanently, on the business: [E3-03] criterion (2) fails in the
filer's own words (its buyers *"have two fairly strong suppliers. It is in their best interest to keep at least two"*; the parts are built
to the buyer's print; a new entrant took periscope demand in 2026 and the 10-Q expects *"pricing concessions"*), and [E3-43]'s
demonstration runs the wrong way (prices fixed at award could not follow cost; returns follow volume, five loss years in fourteen).
Q3 to Q6 are NOT scored; what was read beneath the close is recorded unscored.
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
a forecast **[E4-15, E3-32]**. Optex sells to the US government, US primes and a few foreign buyers, in dollars; *"Approximately
94 % of the total company revenue is generated from domestic customers and 6 % is derived from foreign customers, primarily in Canada
and Israel"* (10-K FY2025, Note 1). Earnings currency **USD**; no FX step.
- rate **5.49%** · date **09/25/2026** (the last posted business day; 09/26 and 09/27 are a weekend) · source **US Treasury daily
  par yield curve, 30-year, from the issuing authority**. `tools/_cache/sov_USD_treasury.csv` was deleted before
  `tools/sources.sovereign()` ran, so the rate was fetched, not served from cache (`step0.py`, output `step0_out.txt`). FRED not used.
  Struck fresh; not inherited from the brief or from the DTM run.
- FX / ADR: not applicable.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes  [x] Item 1  [x] Item 1A
- **Annual report: Form 10-K for the fiscal year ended 2025-09-28, filed 2025-12-17, accession 0001493152-25-028071**
  (`form10-k.htm`). Also read: the 10-Ks for FY2024 (0001493152-24-050771) and FY2023 (0001493152-23-045259), the latter for the
  screen's `wc_note`.
- **Newest periodic: Form 10-Q for the quarter to 2026-06-28, filed 2026-08-11, accession 0001493152-26-037119.**
- **Fiscal calendar, confirmed from Note 2**: *"Optex System Holdings’ fiscal year ends on the Sunday nearest September 30. Fiscal year
  2025 ended on September 28, 2025 and included 52 weeks."* The FY2026 10-K (year to 2026-09-27) is not yet due. **Filer status**: the
  FY2025 cover ticks *"Non-accelerated filer ☒ | Smaller reporting company ☒"*; the EDGAR filer record reads "Non-accelerated filer,
  Smaller reporting company". Registrant **CIK 0001397016**, Delaware, Richardson, Texas; formerly Sustut Exploration Inc (a shell, reverse
  merger March 2009). Listed on the Nasdaq Capital Market from 2023-03-14 (Form 8-A12B, accession 0001493152-23-007551, and the
  exchange certification the same day; Commission File Number 001-41644); registered under Section 12(g) from 2010 (8-A12G).
- **Figures cross-checked against the filed statement.** The tagged `NetCashProvidedByUsedInOperatingActivities` for FY2025 is 6,931,000
  and for FY2023 is −296,000; the 10-K statements print *"Net Cash provided by Operating Activities | 6,931 | 1,781"* (FY2025, FY2024) and
  *"Net Cash (used in) provided by Operating Activities | ( 296 | ) | 2,042"* (FY2023, FY2022). Also checked line by line against the tags:
  depreciation and amortization 515 / 487 / 345 / 307, stock compensation 383 / 425 / 247 / 162, purchases of property and equipment 494 /
  681 / 376 / 257, accounts payable and accrued expenses 725 / 359 / 411 / 313, inventory 541 / (2,710) / (2,941) / (1,629). Every tag equals
  the printed figure.

**Price and shares.**
- Price **$10.42**, Nasdaq Capital Market close **2026-09-25** (Friday), Yahoo chart endpoint via `tools/sources.price`, `regularMarketTime`
  2026-09-25 checked. **Aggregator, used for the live quote only, flagged.**
- Shares **6,959,873**: the cover of the **10-Q for the quarter to 2026-06-28, filed 2026-08-11, accession 0001493152-26-037119**, reads
  *"Indicate the number of shares outstanding of each of the issuer’s classes of common stock, as of August 10, 2026: 6,959,873 shares of
  common stock."* The balance sheet of the same filing: *"Common Stock – ($ 0.001 par, 2,000,000,000 authorized, and issued and outstanding
  shares of 6,959,873 and 6,920,658 as of June 28, 2026 and September 28, 2025, respectively)"*. `python Screens/cover_shares.py OPXS`
  returned the same count from the same accession. **One class; no preferred stock on the balance sheet; no warrants or convertibles
  outstanding found in either filing.** Dilution not in the count, from the 10-Q's EPS note: 63,500 unvested restricted stock units and
  67,500 unvested market-based shares (the CEO and CFO grants of 2025-12-18), about 1.9% together; recorded, not added. Nothing summed.
- **Market cap: $10.42 x 6,959,873 = $72.5M.**

**Deal check (the screen's `deal_note`).** The filer list since 2025-12-17 carries one Item 1.01 8-K, filed 2026-07-20 (accession
0001493152-26-033931), and no S-4, DEFM14A, SC TO-T, SC 13E3 or 425. Its Item 1.01 reads: *"On July 14, 2026, Optex Systems Holdings, Inc.
[...] and its subsidiary, Optex Systems, Inc. [...] entered into a master equipment finance loan and security agreement (the “Master
Agreement”) with Texas Capital Bank [...] the Bank provided interim funding of $246,783 (the “First Interim Loan”) to cover the first
installment of an installment purchase of an approximately $2.1 million high vacuum coating system."* The exhibits are the Master Agreement
(EX-10.1) and the Interim Funding Addendum (EX-10.2); no EX-2.1. **It is an equipment loan, as the screen guessed; the quote is an
owner-earnings price, not a spread.** The only deal-shaped filings in the history are the issuer's own tender offer of 2022 (SC TO-I
filed 2022-08-18; 1,603,773 shares bought at $2.65) and the Speedtracker product-line purchase of 2024-01-18 (Item 1.01 not needed; $1.03M
cash, below).

---
## THE SCREEN ROW: carried UNLABELLED, a set of claims and not a finding

From `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`: `cap_m 70 · oe_bottom_m 1 · oe_top_m 2 · spread 0.397 · deal_note "1 8-K
Item 1.01 filing(s) since 2025-12-17, none carrying a merger agreement" · wc_note "ONE LINE MADE THE CASH: AccountsPayableAndAccruedLiabilities
moved 139% of 2023 OCF" · yield_bottom 0.0198 · vs_sovereign −0.0337 · growth_required 0.0802 · level_shift 2.2 "STEP UP - normalize down
[E4-41]" · best_year_dep 0.36 · level_shift_oe n/a "EARLY HALF STRADDLES ZERO" · best_year_dep_oe 0.481 · flags_disagree · years_filed 16 ·
window_disagree · spread_caveat "4-construction width only [...] rebuild it [E4-25]" · newest_filing 2025-09-28 · newest_periodic
2026-06-28`. Each field used is reproduced or refuted in this file; the list is gathered at the end.

**The `wc_note` is refuted at Step 0, from the filed FY2023 statement: the payables line did not make the cash, because there was no
cash.** FY2023 operating cash was **negative, $(296)K**. The accounts payable and accrued expenses line was **+$411K**, which is 139% of
the ABSOLUTE value of $296K; that is the whole of the screen's arithmetic. The line that decided the year was the other way round:
*"Inventory | ( 2,941 | )"*, an inventory build of $2.9M (inventory $9,212K to $12,153K) against net income of $2,263K. The FY2023 10-K
says why: the delays in key components *"combined with labor shortages experienced in fiscal year 2023, negatively impacted our production
levels and pushed the delivery dates of several of our contracts"* (quoted from the FY2025 10-K, which carries the same history). The
flag's ratio has no sign, so on a year of negative operating cash it reports the payables line as having "made" a cash figure that does
not exist. **Screen error, and a tooling defect in `working_capital_flag()` (reported, not patched).**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics, in my own words.** Optex is a job shop for military optics with two plants in the Dallas area and 132 people. It is
handed a drawing and a quantity, buys the glass, acrylic, aluminium castings, steel and gold coating material, grinds, coats, bonds and
assembles the parts, puts a sample through the customer's first-article and life tests, and ships. The filer's own words, twice in
the 10-K: *"Our products consist primarily of build-to-customer print products that are delivered both directly to the armed services and
to other defense prime contractors."*
- **Optex Richardson (FY2025 revenue $23.8M, 57%; operating income $3.6M).** Periscopes (laser-protected and plain, glass and acrylic;
  $19.2M), sighting systems ($1.5M), howitzer sights (nil delivered), and spares (mirrors, prisms, collimators). Fitted to the Abrams,
  Bradley, Stryker, XM30 and M10 Booker vehicles. Sold to the government direct (DLA Land and Maritime under multi-year IDIQ contracts, the
  Army) and to the primes that build the vehicles (General Dynamics Land Systems, BAE Systems).
- **Applied Optics Center, Dallas (FY2025 external revenue $17.6M, 43%; operating income $3.9M).** Bought in November 2014. Thin-film
  coatings: laser interference filters and laser filter units for night-vision and weapon sights (the XM157 fire-control scope), day
  windows, specialty coatings; plus commercial optical assemblies for rifle-scope makers (Nightforce, Lightforce). It is also the coating
  supplier to Richardson's periscopes.
- Revenue = units ordered x a unit price fixed at award for the life of the contract (*"The majority of the Company’s contracts and
  customer orders originate with fixed determinable unit prices for each deliverable quantity of goods defined by the customer order line
  item"*, 10-Q Note 2). Cost = materials (*"The largest portion of our costs is materials"*), direct labour, and a fixed plant overhead that
  is spread over whatever volume arrives. Profit is therefore a function of volume against a price that was fixed before the costs were
  known: FY2025's 25.5% Richardson gross margin came, in the filer's words, from *"improved manufacturing overhead rates as the fixed
  costs were spread across a higher revenue base"*.
- Customers, FY2025: *"U.S. government agencies (29%) and four U.S. defense contractors (19%, 10%, 6% and 6%)"*; by channel, the
  government 28%, US primes 61%, foreign military 6%, commercial 5%.

**The scarce input this business controls.** Not a design and not a brand. What it holds is **qualification**: approved-source status on
drawings it already builds, first articles already accepted, an ITAR registration, a government-approved accounting system, and the
coating know-how of the Dallas plant. The filer names these as the entry barrier (*"an entrant would need to prove to the government agency
in question the existence of a government approved accounting system for larger contracts. Second, the entrant would need to develop the
processes required to produce the product. Third, the entrant would then need to produce the product and submit successful test
requirements"*). Whether that barrier holds prices up is the Q2 question.

**Will the fundamentals look broadly the same in ten years?** The mechanism will: drawings in, qualified parts out, priced per contract.
The filer expects the vehicle fleet it serves to last (*"We expect that these tanks will continue to be used through approximately 2040"*).
The volumes are not stable (orders for periscopes fell 42.2% in FY2025; backlog fell from $44.2M to $39.1M to $30.1M between 2024-09 and
2026-06) and depend on appropriations the filer does not control, but that is a question for Q2 and Q4, not for whether the business can
be understood. The business is *"relatively simple and stable in character"* **[E3-31]** in its mechanism.

**VERDICT: [x] IN**

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

> *"An economic franchise arises from a product or service that: (1) is needed or desired; (2) is thought by its customers to have no
> close substitute and; (3) is not subject to price regulation. The existence of all three conditions will be demonstrated by a company's
> ability to regularly price its product or service aggressively and thereby to earn high rates of return on capital."* **[E3-03]**

### Where the profit is, before any criterion is scored

Two plants, both selling to the same military buyers. From the filed segment tables (10-K MD&A, FY2023 and FY2025; 10-Q to 2026-06-28):

| Segment operating income, $K (margin) | FY2022 | FY2023 | FY2024 | FY2025 | 9M FY2026 |
|---|---|---|---|---|---|
| Optex Richardson (periscopes, sights) | (380) (−4.0%) | 608 (5.0%) | 1,626 (8.9%) | 3,647 (15.3%) | 2,420 (14.9%) |
| Applied Optics Center (coatings, filters) | 2,189 (15.9%) | 2,426 (16.8%) | 3,620 (21.5%) | 3,868 (20.6%) | 1,522 (11.5%) |
| Unallocated | (162) | (247) | (425) | (383) | (738) |
| **Consolidated** | **1,647 (7.4%)** | **2,787 (10.9%)** | **4,821 (14.2%)** | **7,132 (17.3%)** | **3,204 (11.2%)** |

Both segments sell build-to-print parts to the same government and prime buyers under the same FAR contract forms, so the criteria are
scored for the company and each segment is checked against them.

### THE STRONGEST EVIDENCE AGAINST THE LEADING READING: written first (operator rule 9, [E4-26], [E3-41])

The leading reading after the filings was OUT. The case against it, as strongly as the filings make it:
1. **The return on capital is high, and it is the best in the peer row.** Operating income over tangible operating capital (working
   capital excluding cash and bank debt, plus net plant; rebuilt from companyfacts in `series.py`, the subject's inputs reconciled to its
   statements) was **21.0% (FY2023), 29.4% (FY2024), 44.1% (FY2025)**, and **24.1% over FY2021-FY2025**. **[E3-46]** asks exactly this
   number of the business. Among the eight SEC filers rowed below it is first on the five-year return and level with Espey on margin.
2. **The filer says new entrants face a high wall.** *"Potential Entrants — Low Risk to us. In order to enter this market, potential
   competitors must overcome several barriers to entry. [...] Finally, in many cases, the customer has an immediate need and therefore
   cannot wait for this qualification cycle and therefore must issue the contracts to existing suppliers. Given the expense and time
   commitment of development and qualification testing, the barrier to entry is high for new competitors."* And *"Substitutes — Low Risk
   to us"*: the Abrams, Bradley and Stryker fleets are expected to serve *"through approximately 2040"*, and spares follow the installed base.
3. **Margins have risen for four years, and the latest 10-Q says new orders are priced better:** consolidated gross margin 13.8%
   (FY2021), 21.9%, 25.8%, 28.0%, 29.2% (FY2025), 30.9% (nine months FY2026), the latter *"offset by increased gross profit at the Optex
   Richardson segment with changes in product mix and the replacement of low margin and loss contracts with newer orders at more
   favorable pricing."* The Q3 FY2026 release (EX-99.1, 8-K filed 2026-08-11) repeats it: gross margin improved *"due to the completion of
   legacy loss-making contracts, improved pricing on newer programs, a more favorable product mix, and operational efficiencies"*. **Answered
   below:** the better price arrives only at the next award, after the loss contracts run out, and the same 10-Q expects concessions where
   the new entrant competes.
4. **Some know-how is its own.** Five utility and three design patents; the Dallas coating plant is the laser-filter supplier to the
   Richardson periscopes (*"the backwards integration of a key supplier"*); an exclusive licence from Pratt & Whitney to coat Black Hawk
   exhaust vanes.
5. **Renegotiation has not cut its prices.** Post-award renegotiation: *"Generally, these subsequent negotiations have had an immaterial impact (0% to 5%) on
   the contract price of the affected contracts."*, and *"We have no history of defective pricing claim adjustments"*.

That is a real case: qualified, needed, and earning well on little capital in the last three years. It is weighed against what follows.

### (1) Needed or desired: PASSES

Periscopes, sights and laser filters for fielded combat vehicles and weapon sights, bought by the Army, the DLA and the primes; *"The basic
need to protect the soldier while providing information about the mission environment continues to be the primary driver"*.

### (2) No close substitute: FAILS, in the filer's own words, and the customer arranges it

The customer is not a consumer who cannot find another brand. It is a buyer that owns the drawing and keeps a second shop qualified on
purpose. The 10-K, Item 1, in each of FY2023, FY2024 and FY2025, verbatim:
> *"Buyers — Medium Risk to us. In most cases the buyers (usually government agencies or defense contractors) have two fairly strong
> suppliers. It is in their best interest to keep at least two, and therefore, in some cases, the contracts are split between suppliers."*

- **The design is the buyer's.** *"Our products consist primarily of build-to-customer print products"*. A build-to-print part is, by
  construction, a part a second qualified shop can make from the same print; what Optex holds is its place on the approved list, and the
  buyer's stated practice is to keep two names on it.
- **The rivals are named, and the names change.** FY2025: *"we consider our primary competitor for the Optex Richardson site to be Gus
  Periscopes. The Applied Optics Center thin film and laser coatings products compete primarily with Materion-Barr, G&H Artemis and
  Alluxa. Our competitors are often well entrenched, particularly in the defense markets."* FY2023: *"our primary competitors for the Optex,
  Richardson site to be Kent Periscopes and Synergy International Optronics, LLC"*. Competition is *"primarily on the basis of our ability
  to design and engineer products to meet performance specifications set by our customers"*, with *"Product pricing"* among the factors,
  and *"Increased competitive pressure could lead to lower prices for our products"*.
- **The substitute has arrived.** 10-Q to 2026-06-28, verbatim, twice: *"We are also experiencing lower demand for standard periscopes due
  to new competition affecting several of our periscope products. If and as competition increases, future orders for these products may
  require pricing concessions, which could reduce margins over the next fiscal year."* and *"we are seeing lower demand for our standard
  periscopes attributable to the entrance of new competition for several of our periscope products"*. Periscope orders fell **42.2%** in
  FY2025 (to $11.5M) and periscope backlog **37.3%** in the year to 2026-06-28 (to $10.6M); total backlog $44.2M (2024-09) to $30.1M (2026-06).
  The 10-K's *"Potential Entrants — Low Risk"* (point 2 above) was written nine months before its own 10-Q recorded the entrant.
- **Precedent followed.** ERIC (register): *"Almost all CSPs dual source, giving vendors no pricing power unless they offer some
  technology advantage"* failed criterion (2) on the buyer's sourcing practice; the same practice is written into this filer's own 10-K.
  BUKS (2026-09-27), whose aerospace shop failed criterion (2) on *"others may price their products and services below our selling
  prices"*, is followed on kind (a small defense job shop pricing against named rivals).

### (3) Not subject to price regulation: FAILS in part: where a contract is not bid, the buyer's regulation sets the price

Two regimes run through the book, and the filer describes both:
- **Negotiated, sole-source or non-competitive awards** fall under the Truth in Negotiations Act: *"For these contracts, we must provide a
  vast array of cost and pricing data in addition to certification that our pricing data and disclosure materials are current, accurate and
  complete upon conclusion of the negotiation."* The price is negotiated from Optex's own certified costs, and *"if a post contract award
  audit were to uncover that the pricing data provided was in any way not current, accurate or complete as of the certification date, we
  could be subjected to a defective pricing claim adjustment with accrued interest."* The buyers' side of it: *"In the case of larger
  contracts, the customer can request an open book policy on costs and expects a reasonable margin to have been applied."* And the FAR: *"These regulations also
  subject us to financial audits and other reviews by the government of our costs, performance, accounting and general business
  practices relating to our government contracts, which may result in adjustment of our contract-related costs and fees and [...] impose
  accounting rules that define allowable and unallowable costs"*. A price built from audited cost plus a margin the buyer calls
  reasonable is administered, not set by the seller: **[E2-59]**'s *"prices or costs are administered in some manner"*, through
  *"government intervention"*.
- **Competitively bid firm-fixed-price awards**: *"Obtaining government contracts may also involve long purchase and payment cycles,
  competitive bidding, qualification requirements [...] price negotiations"*. Here the price is not regulated; it is bid against the second
  source, which is criterion (2)'s failure above.
- **The HII precedent (2026-09-26) is followed on kind and distinguished on form and proportion.** HII's price was built from *"allowable
  and allocable costs under the FAR and CAS regulations"* on 96% of revenue under cost-type or incentive contracts. Optex's contracts are
  *"primarily fixed price"*, and the filer does not disclose what share of revenue sits under TINA-certified negotiations; so criterion (3)
  is not scored as failing for the whole book, and **the verdict does not rest on it**. HII passed criterion (2) as the only carrier yard;
  Optex fails it in its own words, which is the decisive difference.

### [E3-43]: the demonstration runs the wrong way on both halves

> *"The existence of all three conditions will be demonstrated by a company’s ability to regularly price its product or service
> aggressively and thereby to earn high rates of return on capital. [...] In contrast, “a business” earns exceptional profits only if it
> is the low-cost operator or if supply of its product or service is tight. Tightness in supply usually does not last long."* **[E3-43]**

**Pricing half: the price is fixed at award for up to five years and cannot follow cost.** The contracts are *"fixed determinable unit
prices"*; *"In the event our actual costs exceed the fixed costs determined under our product contracts, we will not be able to recover the
excess costs"*. The record of what that meant: multi-year IDIQ periscope contracts *"priced in 2019 and 2020, prior to Covid-19"* ran at a
loss through the inflation of 2021-2025, and the filer was *"obligated to accept new task awards against these contracts until the contract
expiration"* (contract loss reserves $259K at FY2024, $132K at FY2025; one legacy contract still *"in a current loss condition due to cost
increases on the price of gold"* at 2026-06-28). That fails **[E2-44]**'s first characteristic (*"an ability to increase prices rather
easily"*) and puts the business on the wrong side of **[E4-47]** (*"retains its earning power in real dollars without commensurate
investment"*): it could not re-price until the contract ran out, and then only at the next bid.

**Returns half: high now, not "regularly".** Consolidated operating margin, every tagged year (companyfacts, the subject's figures
reconciled to its statements): **−2% (FY2012), 2%, −10%, −11%, −1%, 1%, 7%, 13%, 11%, −3% (FY2021), 7%, 11%, 14%, 17% (FY2025)**; return on
tangible operating capital **−19.5% (FY2014), −17.5% (FY2015), −2.5%, 2.5%, 16.6%, 26.7%, 27.3%, −4.9% (FY2021), 16.4%, 21.0%, 29.4%,
44.1%**. Five years in fourteen lost money at the operating line. The filer names the cause of the good years each time, and it is volume,
not price: FY2023, *"higher absorption of the fixed overhead cost base associated with higher revenue levels at both operating segments"*;
FY2025, *"improved manufacturing overhead rates as the fixed costs were spread across a higher revenue base"*. **[E4-55], units before
dollars:** FY2025 periscope revenue rose 58.7% while *"we increased our periscope production levels by approximately 56%"*, so the
FY2025 price-and-mix contribution was about 2 points; the margin came from absorption. That is [E3-43]'s *"a business"* earning
exceptional profits while *"supply of its product or service is tight"* (the 2023-2025 ground-vehicle replenishment, with its own supply
shortages), and the 10-Q of 2026 records the tightness ending (*"new competition"*, *"pricing concessions"*, orders −19.1% for nine months).

### THE COMPETITOR ROW, required [E3-28]

Metric: **operating income over revenue, and operating income over tangible operating capital (current assets less cash and short-term
investments, less current liabilities other than short-term debt, plus net PP&E), each summed over the fiscal years 2021-2025**, from each
filer's SEC companyfacts (`peers.py`, output `peers_out.txt`; ten-year margins in `peers10.py`, output `peers10_out.txt`). The subject's
inputs reconcile to its statements (operating income 7,132 / 4,821 / 2,787 / 1,647 / (494); revenue 41,337 / 33,995 / 25,659 / 22,383 / 18,222).

| Company (SEC filer) | what it makes, for whom | op. margin FY2021-25 | op. margin FY2016-25 | op. income / tangible op. capital FY2021-25 |
|---|---|---|---|---|
| **Optex Systems (OPXS, subject)** | build-to-print military optics and coatings | **11.2%** | **9.4%** | **24.1%** |
| Espey Mfg. & Electronics (ESP) | build-to-print military power supplies and transformers | 11.3% | 10.2% | 22.9% |
| CPI Aerostructures (CVU) | build-to-print aerostructures for defense primes | 4.9% | 3.9% | 23.6% (customer advances shrink the base) |
| Ultralife (ULBI) | military batteries and communications systems | 1.8% | 3.6% | 3.3% |
| Air Industries Group (AIRI) | build-to-print machined flight-critical parts | 0.8% | −5.3% | 1.1% |
| Frequency Electronics (FEIM) | defense and space timing and RF | 0.4% | −6.6% | 0.9% |
| Precision Optics (POCI) | micro-optics, medical and defense | −13.2% | −13.9% | negative |
| LightPath Technologies (LPTH) | infrared lenses and optical assemblies, rising defense share | −15.7% | −6.2% | negative |
| Kopin (KOPN) | microdisplays and optics for military sights | −47.4% | not rowed | negative |

- **Peers named: eight** SEC filers that make build-to-print or specified parts for defense primes and the government, three of them in
  optics. **Not rowed, with the obstacle:** the named rivals Gus Periscopes, Kent Periscopes, Synergy International Optronics and Alluxa
  are private; G&H (Gooch & Housego) files in London, not with the SEC; Materion's Precision Optics business sits inside a large
  materials company whose segment is not comparable at this size; Innovative Solutions & Support and Servotronics did not resolve in the
  SEC ticker map and Sypris returned no annual tags (not chased further). **The named rivals cannot be rowed, so the row places the
  subject among its kind, not against its rivals; the verdict does not rest on the row**, it rests on the filer's own words at criterion (2).
- **What the row shows.** Optex is first on return and level with Espey on margin, and **the two best rose in step**: Espey −1.5% (FY2021)
  to 18.5% (FY2025), Optex −2.7% to 17.3%, on the same procurement cycle. The same shape across two unrelated build-to-print shops is the
  cycle's signature, not a position's (the HII row found the rival yard's margin moving *"in step"*). The limit **[E3-61]**: the row shows position,
  never conduct.

### The other Q2 tests, scored

- **[E3-33] / [E5-28], untapped pricing power:** none. A manager cannot raise a price that is fixed at award for up to five years, bid
  against a second qualified source, or negotiated from certified cost.
- **[E4-37], the agony metric:** the price is not raised at all between awards; at the next award it is bid, and the latest 10-Q expects
  *"pricing concessions"*.
- **[E2-45], the attacker's test:** answered by the filer, which records an attacker entering its largest product line in 2026.
- **[E2-53], dominance:** not claimed and not shown. $41M of revenue against rivals *"often well entrenched"*, some *"substantially
  greater financial and other resources"*.
- **[E4-32], direction:** widened FY2021-FY2025 on volume; **narrowing** from FY2026 (new competition, orders −19.1% and backlog −21.4%
  year on year to 2026-06-28, AOC nine-month margin 23.5% to 11.5%).
- **[E4-23], key-person dependence:** not the defect. The CEO changed in December 2025 (the chairman stays as Facilities Security Officer);
  no filing makes the business depend on a person.
- **[E4-04], verdict form:** not the perimeter close. There is no rapid technology change to judge; the filings judge the franchise
  question themselves. **OUT on the business, not UNKNOWABLE.**

### The three open operator questions, both readings written and not decided (PRIME RULE 5)

- **The ABT question ([E3-03] at the whole company or segment by segment).** *Segment by segment:* Richardson sells build-to-print
  periscopes and sights to buyers who keep two suppliers, and its named rival and the 2026 entrant compete in periscopes; AOC sells filters
  and coatings against three named coaters. Both fail (2). *Whole company:* the same buyers and the same contract forms; fails (2). **Does
  not move this file.**
- **The ABBV question ([E3-03] criterion (3) at the company or the product level).** *Product level:* a sole-source item negotiated under
  TINA fails (3); a competitively bid item passes (3) and fails (2). *Company level:* the TINA share is not disclosed, so (3) is not scored
  for the whole, and the file turns on (2), which fails. **Does not move this file.**
- **The CAT question (whether [E2-58]'s wide-and-sustainable exception is for commodity products only).** The exception needs *"a cost
  advantage that is both wide and sustainable"*; the filer says the opposite of sustainable (*"If and as competition increases [...]
  pricing concessions"*), and the margin record swings with absorption. **Does not move this file.**

### Class and verdict

- Needed or desired [x] · no close substitute [ ] (fails: the buyers *"have two fairly strong suppliers. It is in their best interest to
  keep at least two"*, the parts are built to the buyer's print, and a new entrant took periscope demand in 2026) · not price-regulated [ ]
  (fails for negotiated sole-source awards under TINA certified cost and open-book pricing; the share is not disclosed and the verdict does
  not rest on it)
- Must the moat be continuously rebuilt? The place on the approved list is re-won at each award and each re-bid, against a second source
  the buyer keeps on purpose **[E4-04]**. Great manager required? No finding **[E4-23]**.
- Class: **[ ] WIDE  [ ] NARROW  [x] NONE** · Direction: widened FY2021-FY2025 on volume; narrowing from FY2026.

**VERDICT: [x] OUT**

**Asked aloud, per [E4-19]: can I name the document that would resolve this?** Nothing further needs to be fetched. The 10-K's Item 1
says in the filer's words that its buyers keep two suppliers and names the rivals; the 10-Q records a new entrant and expected pricing
concessions; the MD&A records fixed prices that could not follow cost and margins that follow volume. **OUT on the business, permanent,
and not the [E4-04] perimeter close.** Q3 to Q6 are not scored; what was seen is recorded beneath the close.

---
## Q3 to Q6: NOT SCORED. The file closed at Q2, OUT on the business.

⛔ Q3, Q4, Q5 and Q6 are not scored; no verdict below. What was read is recorded so a later reader does not have to
refetch it. Nothing here promotes or rescues the file **[E2-37, E2-38, E3-39]**.

---
## THE SCREEN ROW, ANSWERED

| Field | Screen | Finding |
|---|---|---|
| `deal_note` | "1 8-K Item 1.01 [...] most likely a credit facility or offering" | **CONFIRMED in kind** (Step 0): a Texas Capital Bank master equipment finance agreement of 2026-07-14, $246,783 interim funding toward a $2.1M coating system; no merger, tender or going-private form |
| `wc_note` | "ONE LINE MADE THE CASH: AccountsPayableAndAccruedLiabilities moved 139% of 2023 OCF" | **REFUTED** (Step 0): FY2023 operating cash was **−$296K**; the payables line (+$411K) is 139% of an absolute value; the year was decided by a $2,941K inventory build. The flag carries no sign |
| `cap_m` | 70 | reproduces at about $10.06 a share on the same count; at the 2026-09-25 close $72.5M |
| `oe_bottom_m`, `oe_top_m` | 1, 2 | reproduce in size as the five-year window ($1.48-1.57M on the filed construction); `yield_bottom` 1.98% implies $1.39M, near the five-year conservative end under the tool rule that counts the $800K intangible tag in FY2025 (below), $1.34M at 1.91%; not exact |
| `yield_bottom`, `vs_sovereign` | 1.98%, −3.37% | struck on the stale cap and an older 5.35%; today the five-year window is 2.04-2.16% against 5.49% |
| `growth_required` | 8.02% | reproduces as ~10% less 1.98%; a derivative of the two fields above |
| `level_shift` 2.2 "STEP UP - normalize down [E4-41]"; `best_year_dep` 0.36, `best_year_dep_oe` 0.481 "ONE YEAR CARRIES THE WINDOW" | | **CONFIRMED**: FY2025 alone is $6.05-6.19M of owner earnings against a five-year mean of $1.48-1.57M; it is 82% of the five-year sum at the capex end, and the trailing twelve months to 2026-06-28 are $0.58-1.29M |
| `level_shift_oe` "EARLY HALF STRADDLES ZERO" | | **CONFIRMED**: owner earnings were negative in eight of the sixteen filed years (FY2010, 2013, 2015, 2016, 2017, 2019, 2021, 2023) at the capex end |
| `years_filed` | 16 | reproduces as FY2010-FY2025; **the operating-cash tag is absent for FY2013-FY2015**, read here from the three 10-Ks (0001571049-13-001285, 0001571049-14-007394, 0001571049-15-009981) |
| `spread_caveat` | "4-construction width only [...] rebuild it" | answered: every trailing window 1-16 years, every rolling five-year window and the TTM, both (c) ends, below |

---
## COMPUTATION — NOT A CLEARANCE

*Operator rule 3. Arithmetic beneath a closed file. It carries no entry language, no value range and no ranking.*

**Construction** (`oe.py`, output `oe_out.txt`): operating cash as filed, less stock compensation in full **[E5-06]** (the cash-flow
add-back, *"Stock Compensation Expense"*, which resolves in every year FY2010-FY2025 and includes the restricted board shares and the
market-based officer awards; the 10-Q says the December 2025 performance shares, *"The fair value of these awards totaled $679 thousand as of
the grant date"*, are amortized through the same line), less (c) at two ends: **depreciation excluding acquired-intangible amortization**
(the AOC backlog intangible in FY2015, $342K, and the Speedtracker intangible in FY2024-FY2025 are left out) and **total purchases of property
and equipment**. No net-income proxy (operator rule 5). Dollars in thousands.

| FY | Operating cash | SBC | Depreciation | Capex | OE, capex end | OE, depreciation end |
|---|---|---|---|---|---|---|
| 2010 | (876) | 97 | 66 | 116 | (1,089) | (1,039) |
| 2011 | 1,114 | 87 | 66 | 31 | 996 | 961 |
| 2012 | 848 | 152 | 165 | 96 | 600 | 531 |
| 2013 | (1,538) | 128 | 69 | 121 | (1,787) | (1,735) |
| 2014 | 1,671 | 105 | 80 | 40 | 1,526 | 1,486 |
| 2015 (AOC bought) | (1,218) | 140 | 334 | 2,100 | (3,458) | (1,692) |
| 2016 | (539) | 192 | 345 | 34 | (765) | (1,076) |
| 2017 | 16 | 220 | 337 | 149 | (353) | (541) |
| 2018 | 1,039 | 153 | 327 | 167 | 719 | 559 |
| 2019 | 160 | 113 | 340 | 143 | (96) | (293) |
| 2020 | 3,911 | 197 | 248 | 152 | 3,562 | 3,466 |
| 2021 | 481 | 228 | 263 | 274 | (21) | (10) |
| 2022 | 2,042 | 162 | 307 | 257 | 1,623 | 1,573 |
| 2023 | (296) | 247 | 345 | 376 | (919) | (888) |
| 2024 | 1,781 | 425 | 387 | 681 | 675 | 969 |
| 2025 | 6,931 | 383 | 359 | 494 | 6,054 | 6,189 |

**Every trailing window ending FY2025, against the cap of $72.5M:** one year **$6,054-6,189K (8.35-8.53%)**; two $3,364-3,579K
(4.64-4.94%); three $1,937-2,090K (2.67-2.88%); four $1,858-1,961K (2.56-2.70%); **five (the corpus default [E2-42]) $1,482-1,567K,
2.04-2.16%**; seven $1,554-1,572K (2.14-2.17%); ten $995-1,048K (1.37-1.44%); **sixteen $454-529K (0.63-0.73%)**, $583K at the capex end with
the AOC fixed assets taken out of FY2015. **Rolling five-year windows** (capex end to depreciation end): to FY2014 $49K/$41K; to FY2015
−$425K/−$90K; to FY2016 −$777K/−$497K; to FY2017 −$967K/−$712K; to FY2018 −$466K/−$253K; to FY2019 −$791K/−$609K; to FY2020 $613K/$423K;
to FY2021 $762K/$636K; to FY2022 $1,157K/$1,059K; to FY2023 $830K/$770K; to FY2024 $984K/$1,022K; to FY2025 $1,482K/$1,567K. **Five of the
twelve rolling five-year windows are negative at both ends, and a sixth (to FY2014) is near zero.** **TTM to 2026-06-28** (FY2025 less nine months FY2025 plus nine months
FY2026): operating cash $2,552K, SBC $874K, capex $1,097K, depreciation about $384K (the nine-month FY2025 amortization estimated at
three-quarters of the year's $156K, flagged): **$581K to $1,294K, 0.80-1.78%**.

- **Only one year, FY2025, clears the bond, and it does not clear the ~10% the corpus quits on [E4-28].** Every multi-year window sits
  between 0.6% and 4.9%, below the 5.49% bond; **the bottom sits below zero on five of twelve rolling five-year windows and near zero on a sixth**. The range
  is wide enough that no useful conclusion could be reached from it **[E4-25]**.
- **(c) is a disclosed guess [E2-09]; here the two ends are close** (depreciation $66-387K, capex $31-681K outside FY2015), because the
  plants are leased and the work is labour-driven (*"As our processes are primarily labor driven"*). The width lives in the operating cash
  itself, which swings with inventory: FY2023 −$2,941K, FY2024 −$2,710K, FY2025 +$541K, nine months FY2026 −$2,126K. **[E2-23]'s
  working-capital increment is required here**: inventory ran at 35-47% of revenue in FY2022-FY2025 ($14.3M against $41.3M in FY2025) and a growing book
  consumes it.
- **[E4-41], normalise down**: FY2025's operating cash carried a working-capital release (inventory +$541K, payables +$725K) at the top of the
  procurement cycle; the TTM figure is a fifth of it.
- **Capital spent outside (c), recorded**: the Speedtracker product line, bought in January 2024 with *"$1 million cash on hand"* plus $30K of
  transaction costs ($1,050K of *"Purchases of Intangible Assets"* in FY2024 investing cash), impaired in full ($804K) on 2025-09-28; the AOC purchase from L-3 in November 2014 for $1,013.1K cash against assets the filer
  valued at $3,123.4K (a bargain purchase). **The FY2015 statement cannot be reconciled to the cash consideration from the filing as read**:
  the investing line shows $2,100K of property purchases while the cash consideration was $1,013.1K and the acquired fixed assets were valued
  at $2,064.7K; FY2015 is carried as filed and flagged, and every window that includes it (eleven years and longer) carries the flag.
- **Net-settlement withholding** ($19-245K a year, *"Cash Paid for Taxes Withheld On Net Settled Restricted Stock Unit Share Issue"*) sits in
  financing; it is the cash form of part of the SBC already subtracted, and is not subtracted twice.

---
## BENEATH THE CLOSE: Q3 MATERIAL, RECORDED WITHOUT A VERDICT

- **Weight case, not declared as a verdict:** daily execution is the live determinant (fixed-price bids, overhead absorption and contract
  execution decide each year **[E3-43]**'s *"a business"* clause); no leverage; no control.
- **[E4-29] fires, in the releases and the 10-K.** The 10-K MD&A and every furnished release carry *"Adjusted EBITDA"* (FY2025 $8,030K
  against net income $5,147K, the impairment added back); the Q3 FY2026 release (8-K filed 2026-08-11, accession 0001493152-26-037114,
  EX-99.1) lists it among its highlights and **guides it**: *"the Company continues to expect full-year fiscal 2026 Adjusted EBITDA to range
  between $7.5 million and $8.5 million"*, with revenue guidance *"of between $43 million and $45 million"*. That is also **[E4-22]**'s third
  flag and **[E5-30]**'s ratchet. The 10-Q adds a *"Non-recurring General and Administrative Expenses"* line ($291K) to its Adjusted EBITDA
  for the CEO overlap.
- **What pay vests on [E4-27]:** DEF 14A filed 2026-01-20 (accession 0001493152-26-002846). The CEO's bonus is *"based upon a one-year
  operating plan adopted by the Company’s Board"*, target 30% of a $300,000 salary, metrics not named; the performance shares granted
  2025-12-17 (50,000 to the CEO, 17,500 to the CFO) *"vest in five equal increments if [...] the average VWAP per share of common stock
  equals or exceeds $17.54, $21.05, $25.26, $30.31, and $36.37"*. **Pay on the stock price is [E3-50]'s eighth-flag prompt** (*"the highest
  stock price possible"*); no return-on-capital measure in pay.
- **Insider ownership and related parties:** directors and officers 27.7% as a group at 2026-01-12 (Dayton Judd 12.4%, Danny Schoening
  11.5%); Topline Capital Partners 10.0%; *"There are no transactions disclosable under Item 404 of Regulation S-K."*
- **Capital allocation, recorded:** the 2022 issuer tender, 1,603,773 shares *"at $ 2.65 , or $ 4.25 million"* (19% of the shares then
  outstanding), plus $371K of open-market purchases the same year; dividends paid in FY2017 ($261K) and FY2018 ($784K); a new $10,000,000
  repurchase authorisation on 2026-02-09 (about 14% of today's cap), unused through 2026-06-28; the Speedtracker purchase written off within
  about 20 months; the AOC purchase of 2014 at about a third of the
  filer's own fair value. **[E5-15], a prompt from the history:** common shares 314,867 at FY2015 year end, after the reverse split of
  2015-10-06 (tagged; ratio not traced), and 8,266,601 at FY2016 year end, through the preferred conversions and the 2016 offering ($4,247K of
  proceeds, tagged); not traced further.
- **[E2-01]:** return on equity FY2025 about 21% ($5,147K on $24,291K); FY2021-FY2025 net income $14,592K on average equity of about $17.2M,
  about 17% a year, with no debt; FY2012-FY2017 near zero or negative.

## BENEATH THE CLOSE: Q4 MATERIAL, RECORDED WITHOUT A VERDICT

- **Staying power [E5-11]:** cash $6.2M and no revolver draw at 2026-06-28; the $3M Texas Capital revolver runs to 2027-05-22 (covenants: fixed
  charge coverage at least 1.25:1, total leverage 3:1, and *"capital expenditures (limited to $1 million per year)"*); the new equipment line
  carries the same two ratios; capital commitments of $2.8M at 2026-06-28 (*"a DLC coater, a prototype metal machining center, a high vacuum
  coating system and a 4D PhaseCam LWIR Interferometer"*) against the loan agreement's $1M capex limit; leases $1.85M at FY2025.
- **Concentration:** *"approximately 70% of our gross business revenue from five major customers"*; *"approximately 83% of our material
  requirements are single-sourced across 104 suppliers"*; *"Approximately 99% of our contracts contain termination clauses for
  convenience"*; a pending termination for convenience on the M10 Booker (*"approximately $1.3 million"* of backlog).
- **Great, good or gruesome [E4-20]:** not scored. The capital needed is small but the stream is not reliable (eight negative years of
  sixteen).
- **Survival shapes, as signatures WITHOUT a verdict (Q4 was never opened):** **#20 THE WAVE** (the FY2023-FY2025 record is the ground-vehicle
  replenishment and its supply-tight years; the 10-Q records the orders slowing and a new entrant), with **#14 THE PATRON** as a feature (the
  buyer that funds the programme sets the terms: appropriations, continuing resolutions, termination for convenience, TINA certified cost)
  and **#11 THE PASS-THROUGH** as a feature (fixed prices absorbed the 2021-2025 cost inflation; the buyer keeps a second source so that the
  next bid passes productivity back). No new shape.

---
## TOOLING, REPORTED NOT PATCHED (operator rule 8; a tool may never add a number)

- **`tools/run.py OPXS`** (output `runpy_out.txt`) defaults to a **three-year** window and prints the corpus's five-year window as "THE
  OTHER WINDOW"; prints its table in **whole millions**, so for a $72M filer SBC and D&A show as 0 and 1 and no row can be checked by eye; and
  **builds FY2025 "D&A" as $1,159K against a filed $515K**, because its component rule adds the `AmortizationOfIntangibleAssets` tag, which
  this filer used for **$800K in FY2025**, to `Depreciation` ($359K). The filed amortization was $156K (D&A $515K less depreciation $359K); the $800K is the Speedtracker write-off
  (tagged separately as `AssetImpairmentCharges` $804K). Its conservative end takes max(D&A, capex) per year, so the impairment enters (c) and
  its three-year yield reads **2.36%** where the filed construction reads 2.67%. **A one-time impairment counted as maintenance capital; the
  third form of the acquired-amortization defect already on record.**
- Its *"3. POINTS OVER THE SOVEREIGN -0.51 .. -0.08"* rests on the unprinted growth assumption in `points_over()`, and its *"2. GROWTH THE
  PRICE ASSUMES 7.2% (at a 5.49% rate)"* is struck against the bond, not the ~10% floor [E4-28]; reported, not used.
- **`working_capital_flag()` (the screen's `wc_note`) carries no sign**: on a year of negative operating cash it divides by the absolute
  value and reports a line as having *"MADE THE CASH"* when the cash was below zero and a different line (inventory) decided it.
- The operating-cash tag is absent for FY2013-FY2015 in companyfacts, so any tool series for this filer silently skips three years.

---
## Q6: THE REVERSAL CONDITION, IN WORDS (no band, no alert; FOLD step 4, the QLYS ruling)

The file failed on the business, so a price alert would be a category error. **The file reopens only on a filed change in what the
business is**: a 10-K whose Item 1 no longer says the buyers keep *"at least two"* suppliers for the products that carry the profit, together
with a multi-year record of the filer raising prices on its own schedule (not at re-bid) while unit volume holds, and operating margins that
stay well above the bond through a year of falling orders. None of these is a price.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 OUT; Q3-Q6 not scored and labelled so.
- [x] No question marked IN carries an "unverified" or "provisional" caveat.
- [x] No UNRESEARCHED verdict. [x] No UNKNOWABLE verdict; the [E4-04] perimeter close was considered and refused in writing.
- [x] Step 0: the 10-K FY2025 (0001493152-25-028071) and the 10-Q to 2026-06-28 (0001493152-26-037119) read, with the FY2024, FY2023, FY2015,
  FY2014, FY2013 and FY2011 10-Ks for the series; operating cash, D&A, SBC, capex and the working-capital lines cross-checked against the filed
  statements.
- [x] Owner earnings on every trailing window 1-16 years, every rolling five-year window and the TTM at both (c) ends, beneath the close,
  headed COMPUTATION — NOT A CLEARANCE; **no net-income proxy**; SBC resolves in every year FY2010-FY2025; the depreciation end excludes
  acquired-intangible amortization.
- [x] Competitor row filled: eight SEC filers on one metric and one window, the subject reconciled to its statements; the named rivals that
  cannot be rowed (private or London-listed) named with their obstacle; the verdict does not rest on the row.
- [x] Strongest evidence against the leading reading written first (operator rule 9).
- [x] Precedents read and applied or distinguished in writing: HII, BUKS, ERIC. The ABT, ABBV and CAT questions written both ways and not
  decided.
- [x] Sovereign for USD from the US Treasury, dated 09/25/2026, struck fresh.
- [x] Value not stated (Q5 not opened). No bar chosen (Q5 not opened).
- [x] Price dated 2026-09-25, aggregator, flagged; shares from the latest periodic cover.
- [x] Every ledger id in this file checked present in `principle_ledger.csv` before writing; ledger rows quoted as stored.
- [x] Run committed to git at the claim, after Step 0/Q1, after Q2, and at the close.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- One line: **OPXS, 2026-09-28, FAIL AT Q2 (OUT on the business).** Price $10.42 (Nasdaq close 2026-09-25, aggregator, flagged) x
  6,959,873 shares (10-Q to 2026-06-28 cover, 0001493152-26-037119) = $72.5M, against 5.49% (US Treasury 30-year par, 09/25/2026). A
  build-to-print maker of military periscopes, sights and laser filters whose buyers, in its own 10-K, *"have two fairly strong suppliers.
  It is in their best interest to keep at least two"*, whose 10-Q records *"new competition"* and possible *"pricing concessions"*
  ([E3-03] criterion (2) fails), and whose fixed prices could not follow cost while its returns followed volume (operating margin −11% to
  +17%, five loss years in fourteen; [E3-43] not demonstrated). Beneath the close, owner earnings $454K-$6,189K (0.63-8.53%) across every
  trailing window, five-year $1.48-1.57M (2.04-2.16%). No band, no PORTFOLIO row.

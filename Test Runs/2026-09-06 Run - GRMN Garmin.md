# Company Run — Garmin Ltd. (GRMN) — 2026-09-06
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

---
## THE ANSWER, FIRST — the queue's output contract

> ### PRICE: **$277.03** (2026-09-04 close, Yahoo aggregator, flagged — live quote only)
> ### **FAIL — the file closes at Q5, ON PRICE, at the [E4-28] floor.**
> **Q1 IN · Q2 IN (NARROW, direction widening at the profit centre) · Q3 IN (overlay, no
> disqualifier) · Q4 IN — the FOURTEENTH name in this queue to clear all four business
> gates, and the first consumer-electronics manufacturer.**
> *(Ordinal settled against the parallel WMT run by the queue's Q4-commit-timestamp rule,
> the CTAS/CMG precedent: WMT 677df9c 12:48:57 vs GRMN 0db1d42 12:50:20. WMT thirteenth.)*

**Value: ~$90 conservative · ~$125 judged · ~$140 optimistic · ~$165 at the most generous
construction in the file (which I refused to carry), all per share and all INCLUDING the
$22.66/share of net cash. The price is $277.03 — 2.2x the judged value.**

**Owner earnings $663M–$1,164M across five windows and both capex ends, judged $1,050M.
Yield 1.24%–2.44% against a 5.24% sovereign — every construction, including the best year in
company history, pays less than half the government bond. Honest pre-tax expectancy ~7.5%
against a 10% floor: quit on, not ranked.**

**The one thing that makes this file interesting:** Garmin's filed decade grew owner earnings
**+8.5%/yr** — *above* the +7.86% the floor requires at this price. It is the second name in
queue history whose record exceeds its required rate. It fails anyway on the decomposition:
the growth was **units +2.5%/yr × real revenue-per-unit +3.8%/yr × inflation**, and the
rev-per-unit lever was the one-time migration from $100 PNDs to $600 watches — **a migration
that is complete, and whose last three filed years read −1.8%.**

---

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
a forecast **[E4-15, E3-32]**:
- rate **5.24%** · date **2026-09-04** · source: **US Treasury daily par yield curve, 30-yr,
  fetched fresh 2026-09-06 from home.treasury.gov (issuing authority)**
- FX: none — NYSE-quoted USD registered shares, no ADR.
- **The Swiss-domicile check the brief ordered (Stage 0 by hand):** Schaffhausen is the
  legal domicile, not the earnings currency. The FY2025 10-K: reporting currency USD; share
  capital changed **CHF → USD at the 2023 AGM** ("aligns the share capital currency with the
  financial statement presentation currency"); Americas 47.7% of FY2025 net sales and the US
  the only >10% country; Switzerland federal+cantonal cash taxes were **$22.8M of $317.0M**
  total paid (Note 5, ASU 2023-09 table). USD is the right sovereign. Stated caveat: EMEA is
  37.8% of net sales (EUR/GBP) and functional currencies include TWD (Garmin Corporation,
  the Taiwan manufacturing entity) and EUR — a multi-currency earnings base with USD the
  largest single leg and the reporting/capital currency.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **10-K for FY2025 (52 weeks ended 2025-12-27), filed
  2026-02-18, accession 0001193125-26-056028**; also read: 10-Q Q2-2026 (26 weeks ended
  2026-06-27, filed 2026-07-29, acc 0001193125-26-322114); 10-K vintages FY2024 / FY2022 /
  FY2019 / FY2016 for the multi-year series; DEF 14A filed 2026-04-22 (acc
  0001308179-26-000318).
- figure cross-checked against the filed statement: **OCF FY2025 $1,633,359K and capex
  $270,446K hand-transcribed from the filed Consolidated Statements of Cash Flows; segment
  note total net sales $7,245,519K ties to the MD&A consolidated table; cash+securities
  $4,134.8M ties to balance sheet lines (2,278,646 + 459,202 + 1,396,929).**
- Research transcriptions: `Test Runs/_research 2026-09-06 GRMN/`.

**Price and cap (Stage 0, by hand):**
- price **$277.03**, close 2026-09-04 (Yahoo aggregator, flagged — live quote only)
- shares **192,852,536** as of 2026-07-24, hand-read off the Q2-2026 10-Q cover; single
  class of registered shares, $0.10 par (the FY2025 10-K cover: 192,480,830 at 2026-02-13 —
  count drifting slightly UP; buybacks smaller than award issuance)
- cap **$53,426M**
- Screen row (2026-09-02 corrected queue) **reproduced by hand**: oe_bottom 892 = the 5-yr
  FY2021-25 capex-end mean (hand: 891.9); oe_top 1,204 = the 3-yr **depreciation-only** end
  (hand: 1,204.0) — run.py's known depreciation-only defect; the true 3-yr D&A end is
  1,163.8. Spread 35% = 1,204/892. growth_required 8.38% = 10% − 1.62% floor arithmetic.
  The brief's "~2.3% yield / ~7.7% growth" is the top end of the same band at the screen's
  $55,091M cap. Verified.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words, no management language:** Garmin designs and builds
  physical devices that know where they are, and sells each one once, at a gross margin of
  **58.7%** (FY2025: $4,256.3M gross profit on $7,245.5M net sales). It sold **20.7 million
  of them in FY2025 at an average $350 each**. It spends **15.5% of revenue on R&D**
  ($1,126.2M) and **17.3% on SG&A** ($1,254.0M), leaving a **25.9% operating margin**
  ($1,876.1M). It owns its factories — Taiwan, Kansas, the Netherlands, the UK, Poland,
  China — which is unusual for consumer electronics and is the reason gross margin holds
  where contract-manufactured rivals' does not. There is no subscription engine of any size:
  Garmin Connect is free, the revenue is the box. Cash conversion is high because the
  customer pays at the till and the factory is already built: FY2025 OCF $1,633.4M on net
  income $1,663.9M. **The money is made on the spread between what a specialist will pay for
  a purpose-built instrument and what it costs Garmin to build it in a plant it owns.**
- **The scarce input this business controls:** Not GPS — the 10-K says the signal is free
  ("Access to and use of the GPS systems commercial signal bands is provided free of
  charge"). The scarce inputs are three, and they are unequal:
  (1) **certification and the installed base** in aviation and marine — an avionics suite
  approved into an airframe cannot be swapped by a competitor's marketing budget;
  (2) **vertical manufacturing** — the 10-K names it as a core competency, and it is what
  lets a 58.7% gross margin survive at 20.7M units;
  (3) **a twenty-year library of sport-specific firmware and the Connect data behind it** —
  the weakest of the three, because it is software and can be replicated.
- **Will the fundamentals look broadly the same in ten years?** **This company already
  answered that question once, in the filings, in the negative — and survived.** The
  Auto/Mobile segment went **$2,538.4M (FY2008) → $882.6M (FY2016)**, from 72.6% of revenue
  to 29%, because the smartphone made the PND free. Garmin's own risk factor called it in
  advance (FY2008 10-K: *"The demand for personal navigation devices (PNDs) may be eroded by
  replacement technologies becoming available on mobile handsets"*). So the honest answer is
  not "yes, obviously": it is that **the durable layer is aviation and marine, and the
  consumer layer has already been destroyed once and rebuilt.** I can understand the
  business; I cannot claim its consumer half is stable in character. That distinction is
  carried into Q2 rather than being resolved here — Q1 asks whether the machine is legible,
  and it is: one product, sold once, at a known margin, built in an owned plant.
- **VERDICT: [x] IN**
  *Legible in Buffett's sense — I can write the unit economics without management's
  language and name what is scarce. The [E3-31] "stable in character" doubt is real and is
  adjudicated at Q2, where the corpus puts it ([E4-04] continuous rebuilding, [E3-51]
  surfing), not here. Recording it at Q1 as an OUT would close the file on a business whose
  filed history is the single most informative thing in this queue about surviving
  substitution.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**
- Needed or desired [x] · no close substitute **[ ] — SPLIT, see below** · not price-regulated [x]

### JUDGED BY SEGMENT [E5-37] — *"different numbers are of different importance … there is not one-size-fits-all"*

**THE PROFIT MIX DECIDES WHICH TAIL WAGS, and it is not the one the brief expected.**
FY2025 segment operating income (10-K FY2025, Note 11):

| segment | net sales | operating income | margin | share of segment OI |
|---|---:|---:|---:|---:|
| Fitness | 2,357.0 | 725.9 | 30.8% | 38.7% |
| Outdoor | 2,054.1 | 690.4 | 33.6% | 36.8% |
| **fitness + outdoor** | **4,411.1** | **1,416.2** | **32.1%** | **75.5%** |
| Aviation | 987.2 | 257.2 | 26.1% | 13.7% |
| Marine | 1,182.6 | 251.3 | 21.2% | 13.4% |
| **aviation + marine** | **2,169.8** | **508.5** | **23.4%** | **27.1%** |
| Auto OEM | 664.7 | (48.6) | (7.3)% | (2.6)% |

**The certification-moat segments are 27% of profit. The contested consumer end is 75%.**
So the brief's decisive question is answered against the aviation/marine tail: **whatever is
true of avionics cannot carry this verdict.** The verdict is decided at the fitness/outdoor
end, and that is where the evidence has to be strongest.

### THE [E2-45] ATTACKER RECORD — the Apple Watch decade, from both companies' filings
*"how I would like, assuming I had ample capital and skilled personnel, to compete with it."*
Apple Watch launched April 2015. What happened to Garmin's wearable business through the
decade of the best-resourced attack in consumer electronics history:

| FY | Garmin fitness net sales | fitness OI | fitness margin | Apple "Wearables, Home & Accessories" |
|---|---:|---:|---:|---:|
| 2015 | 661.6 | n/d | | (category not yet split out) |
| 2016 | 818.5 | 160.6 | 19.6% | |
| 2017 | 762.2 | 146.8 | 19.3% | |
| 2018 | 858.3 | 181.7 | 21.2% | |
| 2019 | 1,047.5 | 191.9 | 18.3% | 24,482 |
| 2020 | 1,317.5 | 305.3 | 23.2% | 30,620 |
| 2021 | 1,533.8 | 359.2 | 23.4% | 38,367 |
| 2022 | 1,109.4 | **104.7** | **9.4%** | **41,241 ← Apple's peak** |
| 2023 | 1,344.6 | 232.2 | 17.3% | 39,845 |
| 2024 | 1,774.5 | 482.7 | 27.2% | 37,005 |
| 2025 | **2,357.0** | **725.9** | **30.8%** | **35,686** |

Sources: Garmin 10-K FY2016/FY2017/FY2019/FY2022/FY2025 segment notes; Apple 10-K FY2019-25
category tables (`row_AAPL_wearables.md`, accessions transcribed there).

**Garmin's fitness revenue is 3.56x its 2015 level (+13.5%/yr for ten years) and its fitness
operating income is 4.52x its 2016 level, with margin up eleven points — while the
attacker's own filed category has declined three consecutive years, −13.5% from its FY2022
peak.** Garmin did not merely survive the Apple Watch decade; its wearable profit compounded
through it, and it is compounding fastest now, at the end of it.

**The honest limits on that row, stated [E3-61]:** (1) Apple's category is not a watch line
— it contains AirPods, Beats, Vision Pro, HomePod and accessories, and Apple's own MD&A
attributes the recent decline to *"Accessories and Wearables"* jointly; **Apple discloses no
Apple Watch revenue and no Apple Watch units in any 10-K vintage checked FY2019-25** (a
verified absence, `row_AAPL_wearables.md`), so the attacker's watch line cannot be isolated
from filings at all. (2) The category is ~5.7x Garmin's entire company revenue; it can fall
13% for reasons that have nothing to do with Garmin. **What the row proves is narrow and
real: the attack did not stop the defender.** It does not prove the attacker retreated.

### THE MECHANISM OF THE DEFENSE, from the filed record
The premium/adventure niche is not a marketing claim here; it is visible in three filed
series simultaneously:
1. **Price point.** Real revenue per unit (2025$) rose from **$236 (2015) to $350 (2025),
   +48%** while Apple pushed the mass smartwatch price toward $250-400. Garmin moved **up**
   into a price band the attacker's general-purpose device does not occupy.
2. **Battery and purpose.** The 10-K's outdoor and fitness product descriptions are
   multi-week-battery, sport-specific instruments (adventure watches, dive computers, cycling
   power, inReach satellite SOS via Iridium with a 24/7 staffed response centre). A device
   charged nightly is not a substitute for a device worn on a seven-day trek.
3. **The niche is not small any more.** Fitness+outdoor is $4.41bn of revenue at a 32.1%
   segment margin — the "niche" out-earns the certified avionics business by 2.8x.

### [E3-03](2) — NO CLOSE SUBSTITUTE: THE SUBJECT'S OWN FILING SAYS OTHERWISE
The FY2025 10-K names its competitors, and the density is the finding. Verbatim:
> *"Garmin believes that its principal competitors for fitness products are **Apple, Bryton,
> Coros, Elite, Google, Huawei, Oura, Polar, Samsung, SRAM, Suunto, Wahoo Fitness, Whoop,
> Xiaomi, Zepp Health, and Zwift**."* (sixteen)
> *"…for outdoor products are **Apple, Casio, Coros, Dogtra, Globalstar, Infinition, Rand
> McNally, Samsung, Shearwater Research, SportDOG, Suunto, TAG Heuer, Tissot, TomTom,
> Trackman, Uneekor, Vista Outdoor, and Zoleo**."* (eighteen)
> *"…principal aviation competitors to be **Aspen Avionics, Avidyne, Dynon Avionics, Jeppesen
> ForeFlight, Genesys Aerosystems, Honeywell Aerospace & Defense, Innovative Aerosystems,
> Collins Aerospace (RTX), Safran, Thales, and Universal Avionics Systems Corporation**."*
> *"For marine products … **Furuno, Johnson Outdoors, Navico (Brunswick), and Raymarine
> (Teledyne)**."*

**Thirty-four named substitutes at the consumer end, including the four largest consumer
electronics companies on earth.** [E3-03](2) — *"thought by its customers to have no close
substitute"* — cannot be written IN on that list. This is the single hardest fact in the
file against a WIDE class, and it comes from the subject's own Item 1.

### [E2-44] — THE TWO-CHARACTERISTIC TEST, both halves, from the filed physical series
Full working: `_research 2026-09-06 GRMN/grmn_unit_series_E4-55.md`.
- **(1) Raise prices with flat demand and unused capacity — NOT PROVEN, and I will not claim
  it.** Garmin files a total unit count every year but **no price/volume split ever**, and it
  attributes the revenue-vs-unit gap to *"shifts in segment and product mix"* every single
  year, **never to price**. The $180→$350 rev/unit move is Garmin exiting $100 PNDs and
  selling $600 watches. Mix is not pricing power. (Same finding shape as the BMI run.)
- **(2) Grow dollar volume with only minor additional capital — PASSES loudly.** Revenue
  +156.9% over ten years on capex averaging **3.4% of revenue**; pre-tax return on net
  tangible assets ~28% (see Q3).
- **[E4-37] the agony test:** no price-increase discussion appears in any vintage read. No
  prayer session — but also no evidence of the yawn. Untestable from these filings; recorded
  as such, not credited.

### [E4-55] — WHERE UNITS EXIST, MONITOR UNITS. **They exist, and they are the run's best instrument.**
The brief predicted an absence finding. **The opposite is true: Garmin has filed total unit
sales in MD&A every year for twenty-one years**, through the boom and through the collapse.

| period | units | revenue | real rev/unit (2025$) | reading |
|---|---|---|---|---|
| FY2008→FY2025 (17y) | +22.5% | +107.4% | +13.2% | more physical units today than at the PND peak |
| **FY2016→FY2022 (6y)** | **−10.7%** | **+61.0%** | **+47.9%** | **the Precision Steel shape — the bear case's home** |
| **FY2022→FY2025 (3y)** | **+38.0%** | **+49.1%** | **−1.8%** | **volume at a flat real price — the healthy shape** |
| FY2015→FY2025 (10y) | **+27.8%** | +156.9% | **+48.0%** | **both halves up together over the corpus's decade** |

The six years FY2016-22 are exactly the [E4-55] warning: *"dollar revenue flattered by
pricing is how a shrinking franchise hides."* But the last three years invert it — **units
+11.3%/yr with real revenue per unit flat**, which is the one pattern a mix-shift story
cannot produce and a price wave cannot produce. Garmin is now selling more things, not
dearer things. That is the strongest single fact for the franchise in this file.

**The absences, checked and recorded:** no segment-level unit series in any of twenty-one
vintages; no Garmin Connect registered-user or actives count in any 10-K; no subscription or
ARPU disclosure. The physical series exists only at the company total.

### [E3-30] / [E4-04] — THE COMPANY ALREADY DIED ONCE, AND ITS OWN FILINGS ARE THE EVIDENCE
This is the only name in the queue whose founding category was destroyed on the record.
Auto/Mobile net revenue, from the segment notes (`grmn_pnd_collapse.md`):
**$2,342.2M (2007) → $2,538.4M (2008, the peak) → $1,590.6M (2011) → $1,302.3M (2013) →
$882.6M (2016)** — from **72.6% of company revenue to 29%**. Garmin's own FY2008 risk factor
named the killer before it arrived: *"The demand for personal navigation devices (PNDs) may
be eroded by replacement technologies becoming available on mobile handsets."* By FY2013:
*"Our financial results are dependent on the automotive/mobile segment, which represents
approximately 50% of our revenues, is maturing and expected to further decline."*

**What that record actually licenses, and what it does not:**
- It **refutes** the claim that Garmin cannot see substitution coming or cannot redeploy. The
  company reallocated an entire manufacturing and engineering base out of a dying category
  into four live ones and came out with 2.4x the revenue and 2.7x the operating income.
- It **is not a moat.** A business that had to rebuild its product base to survive is, in
  [E4-04]'s own words, closer to the class whose *"basis must be periodically replaced."*
  The nüvi franchise — *"approximately 48%, 54%, and 63% of Garmin's total consolidated
  revenues"* in 2011/2010/2009 (FY2011 10-K, Item 1) — is worth zero today.
- **[E3-51] surfing:** the honest reading is that Garmin has now caught **two** waves (PND,
  then wearables/adventure) and got off the first one before it beached. Riding two waves
  well is a statement about the **operator and the manufacturing base**, which [E4-23] says
  is a **moat defect, recorded here at Q2, not a Q3 compliment.**

- **Must the moat be continuously rebuilt? [E4-04]** — **At the consumer end, yes, in part.**
  The product base is replaced on a 2-4 year cycle and the 2008-16 record shows the category
  itself can be replaced under it. What is *not* rebuilt is the vertically integrated plant,
  the aviation certifications, and the brand's meaning inside each sport — a lapse in R&D
  narrows those rather than destroying them. **Does success depend on a great manager?**
  Partly, and it is recorded as a defect: the 2008-16 redeployment was a capital-allocation
  achievement, and [E4-23] requires it be read as *"the moat will go when the surgeon goes"*
  risk, not as a strength.
- **Primary moat metric, filing-sourced, and its trend:** **segment operating margin held
  against a named attacker**, and the filed physical series beside it. Fitness margin
  19.6% (2016) → 30.8% (2025) with units and revenue both rising. **Direction: widening at
  the consumer end since 2022; flat-to-narrowing in aviation (34.4% in 2019 → 26.1% in
  2025).** [E4-32] direction favours the segment the brief expected to be losing.

**THE COMPETITOR ROW — required [E3-28].** A moat is a claim about *relative* position.

**Metric: segment operating margin and segment revenue direction, FY2022→FY2025, each from
the peer's own filed segment note.** Full transcriptions with accession numbers in
`_research 2026-09-06 GRMN/row_*.md`.

### ROW A — MARINE. *The row convicts the attacker with its own filings.*

| Company | segment | FY2022 rev | FY2025 rev | Δ | FY2025 op margin | source |
|---|---|---:|---:|---:|---:|---|
| **GRMN** | **Marine** | **$904.0M** | **$1,182.6M** | **+30.8%** | **21.2%** | 10-K FY2025 Note 11 |
| Brunswick | Navico Group | $1,069.3M | $800.4M | **−25.1%** | **GAAP (42.4)%** | BC 10-K FY2025 Note 5 |
| Brunswick | Navico, *adjusted* | — | — | — | **6.0%** (co's own non-GAAP) | BC FY2025 MD&A |
| Furuno / Raymarine (Teledyne) / Johnson Outdoors | — | — | — | — | not separately segmented | see row limits |

Navico Group — the business Brunswick bought for **$1.094 billion** in 2021 to attack exactly
this market — has gone **$1,069.3M → $800.4M** of revenue and **+$68.2M → −$339.6M** of GAAP
operating earnings in three years, with **$334.5M of restructuring, exit and impairment
charges in FY2025 alone**. Even on Brunswick's own adjusted measure the margin fell
**16.6% → 13.8% → 10.0% → 6.6% → 6.0%** across 2021-25. **Garmin's marine margin is 3.5x
Navico's adjusted margin and Garmin grew 31% while Navico shrank 25%.** [E2-45] answered:
a well-capitalised attacker bought its way in at the top of the cycle and is writing it off.

### ROW B — AVIATION. *The row is inconclusive on scale and honest about it.*

| Company | segment | FY2023 margin | FY2025 margin | direction | source |
|---|---|---:|---:|---|---|
| **GRMN** | **Aviation** | **26.8%** | **26.1%** | **flat; 34.4% in 2019 → down** | 10-K FY2025 |
| Honeywell | Aerospace Technologies | 27.6% (filed) | **24.5%** (filed) | **−310bp in two years** | HON 10-K FY2025 |
| Textron | Textron Aviation (the *customer*) | 12.1% | **11.7%** | flat | TXT 10-K FY2025 |

Honeywell Aerospace is **$17.5bn of revenue to Garmin's $987M** and contains engines, APUs
and defence — **it is not an avionics comparable**, and its segment profit was recast in 2024
to *exclude* acquisition amortization, which flatters it. What the row does show: **both the
incumbent and the challenger are seeing avionics-inclusive margins compress**, and Garmin's
aviation margin has fallen 8.3 points from its 2019 peak. **The certification moat is not
producing widening margins on the filed record.**

**THE ROW'S BEST AVIATION EVIDENCE IS NOT A NUMBER — IT IS WHO NAMES WHOM.** Read across
three filers' own Item 1 competitor lists:
- **Honeywell names Garmin FIRST in its Aerospace competitor list in all five vintages
  FY2021-25** (Garmin, L3Harris, Rolls-Royce/Northrop, RTX, Safran, Thales). A $17.5bn
  incumbent puts a $987M challenger at the head of its list, five years running.
- **Textron names Garmin as a supplier** whose Autoland is *"revolutionary"* — the airframer
  advertises the avionics brand to sell its own jets.
- **Brunswick never names Garmin at all** across five vintages, while its marine-electronics
  segment loses $339.6M.
These are three different relationships to the same company — rival, supplier, and silence —
and the first two are the kind of evidence [E2-45] asks for: what the people with ample
capital and skilled personnel actually say about competing with it.
- **Textron Aviation — the customer-side check, and it landed. Garmin is named by its own
  customer as a selling feature.** Textron Aviation revenues **$5,955M** at a **11.7%**
  segment profit margin FY2025 (vs Garmin aviation's 26.1% — the airframer earns less than
  half the margin of the avionics supplier it installs). And the FY2024 and FY2025 Textron
  10-Ks each name Garmin once, verbatim: *"the Citation M2 Gen3, CJ3 Gen3 and CJ4 Gen3, which
  will include the **revolutionary Garmin Emergency Autoland technology**."* **Garmin is
  absent entirely from the FY2022 and FY2023 vintages** — the mention is new, and it is
  descriptive of designed-in content on three announced models. **What it does not establish,
  stated plainly:** no dollar amount, no purchase commitment, no supply-agreement term, no
  share of avionics content; Garmin appears in no supplier-concentration or related-party
  disclosure. It is one adjective in a customer's Item 1, and it is worth exactly that.
- **Collins Aerospace (RTX), Safran, Thales, Avidyne, Aspen, Dynon, Genesys, Universal —
  none separately segmented** at the avionics level in their filings. Avionics-only peer
  economics are **not obtainable from the filing rung**, and I say so rather than estimating.

### ROW C — FITNESS / OUTDOOR. *The attacker of record, and its limits.*

| Company | line | FY2022 | FY2025 | Δ | source |
|---|---|---:|---:|---:|---|
| **GRMN** | **fitness + outdoor rev** | **$2,604.6M** | **$4,411.1M** | **+69.4%** | 10-K FY2025 |
| **GRMN** | **fitness + outdoor OI** | **$661.2M** | **$1,416.2M** | **+114.2%** | 10-K FY2025 |
| Apple | Wearables, Home & Accessories | $41,241M | $35,686M | **−13.5%** | AAPL 10-Ks FY2022-25 |
| Polar, Suunto, Coros, Whoop, Oura | — | — | — | — | **private; see the work order below** |

**Polar and Suunto — the ladder rung named, and the verdict on them is UNRESEARCHED, not
UNKNOWABLE.** Neither is an SEC registrant (EDGAR company search returns empty Atom feeds for
both; reproduced in `row_private_polar_suunto.md`). Polar Electro appears in SEC filings only
as a co-defendant in Garmin's own patent litigation. The single filing-rung Suunto figure is
inside **Amer Sports' FY2023 Form 20-F** and does not yield a usable year: 2022 revenue of
**$31.3M covers only 1 January to the 6 May 2022 disposal**, and the 2021 figure of **$192.0M
is Suunto and Precor combined with no split given**. Both companies' own sites returned no
financial figures, so **nothing was recorded at a lower rung rather than estimating**.
**Work order: Finnish PRH statutory annual accounts for Polar Electro Oy and Suunto Oy.**
That document exists and is nameable, which is what makes this UNRESEARCHED. It does not
change the verdict — both are small private specialists in the segment where Garmin's margin
is *rising* — but the row is honestly incomplete and is marked so.

- **Peers named: 4 filed (Apple, Brunswick/Navico, Honeywell, and Garmin's own segments read
  against each other per [E5-37]) of a named competitive field of 34+.** Buffett says eight.
  **I got four, and the shortfall is structural, not lazy:** Garmin's most dangerous named
  rivals at the consumer end — **Polar, Suunto, Coros, Whoop, Oura, Wahoo, Zwift** — are
  **private companies with no SEC filings**, and its most direct aviation rivals are
  **unsegmented divisions** of RTX, Safran and Thales. This is stated as the corpus requires:
  where a competitor's data is unavailable, **say so and hold the class PROVISIONAL**.
- **[E3-61] the row's limit, stated:** *"identical structures produce opposite outcomes … you'd
  have to know the people involved."* Navico's collapse is partly Brunswick's own integration
  conduct, not proof of Garmin's moat. The row shows position; it cannot show conduct.
- **Untapped pricing power [E3-33] — NOT CLAIMED, and [E5-28] is why.** Claiming this class
  means claiming *"a monopoly or a near monopoly."* A filer that names 34 competitors in its
  own Item 1 cannot support that. No evidence of deliberately unexercised pricing power was
  found; the filed attribution is mix, never price.

### CLASS AND VERDICT

- **Class: [x] NARROW.** Not WIDE — **[E3-03](2) fails at the consumer end on the subject's
  own filed competitor list** (Apple, Google, Samsung, Huawei, Xiaomi among 34 named), and
  the aviation/marine certification moats that *would* support WIDE are only **27.1% of
  segment profit** and so cannot carry the class [E5-37]. Not NONE — the marine row, the
  ten-year both-halves [E2-44] print, the 32.1% consumer-segment margin, the ~48% pre-tax
  return on net tangible operating assets, and survival through the Apple Watch decade with
  profit up 4.5x are not the numbers of a business without an advantage.
- **Not PROVISIONAL as a verdict**, though the *aviation* sub-class is: the decision rests on
  the 75.5% of profit where I have both the subject's and the attacker's filed data, plus a
  marine row that is complete and decisive. The unobtainable peers are concentrated in the
  segment that cannot swing the verdict.
- **Direction: WIDENING at the consumer end since 2022** (fitness margin 9.4% → 30.8%; units
  +11.3%/yr at a flat real price), **NARROWING in aviation** (34.4% → 26.1% since 2019).
  **[E4-32] direction favours the segment the brief expected to be losing, and disfavours the
  segment the brief expected to be the franchise.** That inversion is the finding of Q2.
- **VERDICT: [x] IN — NARROW, direction widening at the profit centre.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**None ticked → Q3 is a qualitative OVERLAY.** Record findings; manager quality alone does
not stop the run. **Any ticked → Q3 is a BINARY GATE and no price compensates.**

**Case declared: OVERLAY — none of the three ticked, and here is why each fails to tick.**
- **Daily execution — NOT ticked.** [E3-38]/[E2-70]'s magnifier is the undifferentiated
  product whose *"only products are promises."* Garmin's are physical instruments at a 58.7%
  gross margin with a 2-4 year design cycle; the error correction window is a product
  generation, not a day. **The natural experiment is in the filings:** FY2022 fitness
  operating income fell **71%** ($359.2M → $104.7M, margin 23.4% → 9.4%) and the business
  recovered to a record without a change of management or strategy — **[E5-18]**'s *"the
  capacity to stand it, if we stumble into it"* demonstrated on the subject's own record.
- **Control — NOT ticked.** Public minority position, NYSE-listed, single class, freely
  exitable. No dual-class structure; founder families hold 14.7% economically with **no
  super-voting shares**.
- **Leverage — NOT ticked, and this is the strongest not-tick in the queue.** **Zero
  long-term debt.** FY2025 10-K, verbatim: *"We have no outstanding long-term debt as of
  December 27, 2025 and otherwise have no meaningful debt-related interest rate risk."*
  Full-text counts across the FY2025 10-K and the Q2-2026 10-Q: **"revolving credit" 0,
  "credit facility" 0, "notes payable" 0, "borrowings" 0.** There is no lender to magnify a
  balance-sheet error into an equity error.

**The honest qualification:** the product-cycle dependence is real, and the PND history
proves a whole category can die under this management. That finding is recorded **at Q2 as a
moat defect under [E4-23]**, which is where the framework puts it, and it is not re-used here
as a Q3 strength. Q3 stays an overlay and **cannot promote this name** [E2-37, E3-39].

**Honesty — binary, permanent, filings-based [E5-16].** *"understanding about business
mistakes; tolerance for personal misconduct is zero."*
**No disqualifier found.** Item 3 Legal Proceedings in the FY2025 10-K is the ordinary-course
paragraph only — *"In the normal course of business, the Company and its subsidiaries are
parties to various legal claims, actions, and complaints, including matters involving patent
infringement, other intellectual property, product liability, customer claims and various
other risks"* — with no named matter and no accrual disclosed as material. Q2-2026 10-Q:
*"The Company settled or resolved certain matters … that did not individually or in the
aggregate have a material impact."* No restatement in any vintage read (FY2013-FY2025); the
one 10-K/A on file (2024-11-29, acc 0000950170-24-131914) is an amendment to the FY2023
10-K whose purpose was **not extracted — a run defect, logged below**. No SEC enforcement
matter found in the filings read. Auditor **Ernst & Young LLP (PCAOB ID 42)** — continuous
since at least FY2016 (the FY2016 10-K carries E&Y's opinion signed Kansas City,
2017-02-22). **Recorded as the corpus requires it be recorded: the absence of found
disqualifiers, not a finding that the managers are honest [E5-17].**

**STEP 2 — THE FOUR FLAGS [E4-22, E5-15].** *Accounting and disclosure, not litigation. Each
is a prompt to READ, never a verdict.*
- [ ] weak accounting — **not found.** SBC expensed in full ($166.0M FY2025, on the face of
      the cash-flow statement). No pension plan of any size; the 10-K states *"We do not have
      any post-retirement benefit plans"* (proxy) and no defined-benefit assumptions appear.
- [ ] unintelligible footnotes — **not found.** Segment note gives net sales, COGS, gross
      profit, R&D, SG&A and operating income **for each of five segments**, which is more
      granular than most filers give at all. Note 5 adopted ASU 2023-09 early enough to file
      the **cash-taxes-paid-by-jurisdiction table**.
- [ ] trumpeted earnings projections / growth targets — **NOT FOUND IN SEC FILINGS.** No
      revenue or EPS guidance appears in the FY2025 10-K or the Q2-2026 10-Q. *(Scope stated
      honestly: earnings releases and calls were NOT swept; Garmin does issue annual guidance
      in its 8-K earnings releases. The [E5-30] ratchet is therefore **live but unmeasured** —
      a run defect, logged.)*
- [ ] serial share issuance — **not found; the opposite is mild.** Shares outstanding
      192,480,830 (2026-02-13 cover) → 192,852,536 (2026-07-24 cover): **+0.19%**, i.e. equity
      awards slightly exceed buybacks. Not [E5-15]'s promotional issuance; recorded as
      creeping dilution, quantified.
- [x] **EBITDA / adjusted-earnings promotion [E4-29] — THE FLAG DOES NOT FIRE, AND THE
      COUNT IS THE FINDING.** Full-text counts, machine-counted:
      **FY2025 10-K: "EBITDA" 0 · "non-GAAP" 0 · "pro forma" 0 · "adjusted" 0.**
      **2026 DEF 14A (291,773 chars): "EBITDA" 0 · "non-GAAP" 0 · "adjusted" 0 · "pro forma" 0.**
      And the proxy states the pay metric's basis in words, verbatim: *"Operating income, for
      compensation purposes, is presented from the Company's audited financial statements
      **without adjustment**."* **This is the cleanest [E4-29] read in the queue's history —
      cleaner than BMI (which fired on pay design) and cleaner than CTAS.** The box is ticked
      only to record that the test was run and returned zero.
- [ ] filed-figure tells [E4-30] — **the cash-tax tell fires and is ACQUITTED on disclosure.**
      Cash taxes paid as a share of pretax income: FY2024 **18.8%** ($319.4M / $1,695.4M) →
      FY2025 **15.7%** ($317.0M / $2,014.5M) — falling, which is the tell. But the effective
      **rate rose** 16.7% → 17.4% over the same period (the opposite direction from the fraud
      signature), and the fall is located by the company's own new jurisdiction table: **Swiss
      federal tax paid $71,793K → $16,688K**, with US tax paid *rising* $128,863K → $149,701K.
      The 10-K explains the ETR move: *"the U.S. tax legislation enacted in 2025, which, among
      other things, changed capitalization requirements of certain research and development
      costs."* Timing and jurisdiction mix, disclosed in a table Garmin was not required to
      file until this year. Acquitted; monitored at Q6.
      **Unnaturally smooth growth — the opposite is true and it is a candor point:** FY2022
      operating income fell 15.7% and fitness segment OI fell 71%. A filer engineering
      smoothness does not print a 71% segment collapse in a segment note.
- [ ] **metric-switching [E2-49] — none found.** The five-segment decomposition with COGS,
      gross profit, R&D, SG&A and operating income has been filed continuously across every
      vintage checked (FY2016, FY2017, FY2019, FY2020, FY2022, FY2024, FY2025). **The
      21-year unit-sales sentence was never withdrawn — including through the six years when
      units were falling (FY2016-22).** That is the [E2-49] test passed in its hardest form:
      the yardstick kept while yielding unfavourable readings. Recasts that did occur were
      announced with reasons and prior years restated (2016 action-camera move, 2022 SG&A
      allocation, 2024 advertising into SG&A, each stated as immaterial to operating income).

**STEP 3 — THE PRIMARY TEST [E2-01].** Earnings rate on equity capital employed, *without
undue leverage or accounting gimmickry* — **not** EPS growth. Multi-year series, balance
sheet before income statement.

- **Years used, and the series (ROE on book equity, my computation from filed statements):**

| FY | net income | shareholders' equity (year-end) | ROE |
|---|---:|---:|---:|
| 2021 | 1,082.2 | — | |
| 2022 | 973.6 | — | |
| 2023 | 1,289.6 | 7,014.3 | 18.4% |
| 2024 | 1,411.4 | 7,848.4 | 18.0% |
| 2025 | 1,663.9 | 8,972.6 | 18.5% |

- **BUT THE DENOMINATOR IS WRONG AND THE CORPUS SAYS SO [E2-43, E2-73].** Book equity here
  contains **$4,134.8M of cash and marketable securities** earning a market rate, not a
  business return. *"the managers of the units should be judged by the returns they achieve
  on the underlying assets"* **[E2-73]**. Recomputed on **net tangible assets actually
  employed in the business** — equity $8,972.6M less cash and securities $4,134.8M less
  goodwill $760.2M less other intangibles ≈ **$3.88bn** — FY2025 operating income $1,876.1M
  is a **~48% pre-tax return on net tangible operating assets**, and ~43% after tax.
  **That is the second-question-about-the-business number [E3-46], and it is a very high
  one.** It is also the honest reason the reported 18.5% ROE understates the business: a
  third of the balance sheet is a bond portfolio.
- Trend: flat-to-rising on both denominators; no leverage in either (zero debt), and no
  accounting gimmickry found (Step 2 returned zero on every gimmickry flag).

**The half-owner test [E2-26]:** does this reporting tell me what I would want to know if the
positions were reversed? **Yes, and unusually so.** Five segments each with net sales, COGS,
gross profit, R&D, SG&A and operating income; a **21-year physical unit series kept through
the six years it looked bad**; a cash-taxes-by-jurisdiction table; the FY2022 fitness
collapse printed at full depth rather than blended away; segment recasts announced with
reasons and prior years restated; and **no adjusted-earnings layer anywhere in which to bury
anything**. The one thing a half-owner would want and does not get: **any price/volume split,
any segment-level unit count, and any Connect user or subscription metric** — checked absent
across twenty-one vintages. That is a real gap and it is recorded at Q2, not excused here.

**The institutional imperative — score all four [E2-30].** *Not a fraud test: "institutional
dynamics, not venality or stupidity."*
- [ ] resists any change in current direction — **REFUTED ON THE RECORD.** The 2008-16
      redeployment out of PNDs is the largest counter-example in this queue: an entire
      product base, engineering organisation and factory output reallocated while the
      founding category fell from 72.6% of revenue to 29%. Whatever else is true, this
      institution changed direction when the facts changed.
- [x] **projects/acquisitions materialise to soak up available funds — TICKED, and it has a
      name: AUTO OEM.** The segment has lost money **every year for six consecutive years**:
      −$13.0M (2020), −$59.7M (2021), −$61.8M (2022), −$61.1M (2023), −$38.8M (2024),
      −$48.6M (2025) — **cumulative ~−$283M of operating losses**, on rising revenue
      ($460.3M → $664.7M). The company states the commitment plainly in its own risk factor:
      *"We have made and expect to continue making significant investments in the auto OEM
      segment… we have invested significantly in facilities, research and development, and
      other operating expenses and expect to continue doing so."* R&D inside auto OEM was
      **$109.3M in FY2025 alone — 16.4% of that segment's revenue, to produce a loss.**
      **This is the [E2-56] Pro-Am effect in its exact form:** *"Their marvelous core
      businesses … camouflage repeated failures in capital allocation elsewhere."* Judged
      segment-by-segment as [E2-56] requires, the incremental return on the auto OEM
      commitment has been **negative for six years**, and it is invisible in the blended
      18.5% ROE. **This is the live capital-allocation finding of the run.**
      *The counter-case, stated fairly [E4-51]: auto OEM revenue is growing (+57% since
      2020), the losses are front-loaded program investment against multi-year tier-one
      supply contracts, and the segment is 2.6% of profit — an affordable option, not a
      bet-the-company error. Garmin has also not hidden it: the loss is printed in the
      segment note every year and given its own risk factor.*
- [ ] staff studies produced to justify the leader's craving — none found in filings; not
      testable from this rung.
- [ ] peer behaviour mindlessly imitated — **not found; mildly refuted.** No adjusted-EPS
      vocabulary despite universal peer practice; no dual-class despite founder families; no
      buyback ramp at the top despite a 3.4x share price; no leveraged recap despite zero
      debt and free money for a decade.

**Capital allocation — the two buyback conditions [E5-08]:**
- **(1) ample funds for operations and liquidity? YES, overwhelmingly.** $4,134.8M cash and
  marketable securities at FY2025 year-end against **zero debt**.
- **(2) repurchases at a material discount to conservatively calculated IV? NO — but the
  amounts are de minimis and that is the more important fact.** Buybacks under the plan:
  **$99.0M (FY2023), $62.3M (FY2024), $181.0M (FY2025), $81.6M (H1-2026)** — FY2025's is
  **0.34% of the $53.4bn cap**, and the share count *rose* 0.19% over the last two covers.
  Against the Q5 zero-growth band below, these purchases were made above value. **So the
  flag fires — and it is the weakest condition-2 flag the queue has recorded**, because
  Garmin is not shrinking the count at a high price; it is barely buying at all.
  **[E2-51] cuts the other way here and must be stated:** *"A manager who consistently turns
  his back on repurchases, when these clearly are in the interests of owners, reveals more
  than he knows of his motivations."* At today's price the framework does not think buybacks
  are in owners' interests, so the near-abstention is the correct behaviour, not a tell.
  **Flag recorded; it binds position size only [E4-13], never the discount rate.**

**THE DIVIDEND — the [E2-52] and RPM tests, both run:**
- **[E2-52] dividends funded by issuance — PASSES cleanly.** FY2025 dividends $663.9M against
  OCF $1,633.4M (40.6%), with **net share activity a cash OUTFLOW** (proceeds from treasury
  shares $58.0M less award-related purchases $57.2M less buybacks $181.0M = −$180.2M). No
  capital was replaced to fund the distribution.
- **RPM decomposition — PASSES, earnings-driven, and the freeze is the proof:**

| FY | DPS | diluted EPS | payout |
|---|---:|---:|---:|
| 2021 | 2.68 | 5.61 | 47.8% |
| 2022 | 2.92 | 5.04 | 57.9% |
| 2023 | **2.92** | 6.71 | 43.5% |
| 2024 | 3.00 | 7.30 | 41.1% |
| 2025 | 3.60 | 8.59 | 41.9% |

  DPS **+34.3%** over five years on EPS **+53.1%**; the payout ratio **fell** 47.8% → 41.9%.
  **And Garmin FROZE the dividend at $2.92 through FY2023** rather than ratchet it through
  the fitness collapse — the anti-aristocrat behaviour, and evidence against a
  distribution-culture ratchet. The 2026 AGM proposes **$4.20** (+16.7%), a 48.9% payout on
  FY2025 EPS and **~68% of FY2025 capex-end owner earnings per share** — still covered, and
  the first year the payout climbs meaningfully. Monitored at Q6.
  *(Mechanism note: dividends are paid "out of Garmin's reserve from capital contribution"
  and require an annual shareholder vote under Swiss law — a tax structure and a governance
  fact, not an [E2-52] issue. $95.0M of retained earnings is indefinitely restricted from
  distribution under Taiwanese law; disclosed.)*

**PAY VERSUS PERFORMANCE — the brief's test, and it is the cleanest design in the queue:**
- **There is no annual cash bonus plan at all.** Proxy, verbatim: *"Garmin does not pay an
  annual cash incentive award or material annual cash bonuses. In 2025, Garmin's Named
  Executive Officers each received a **$358 annual holiday cash bonus**. This is the same
  annual holiday cash bonus that was paid to other Garmin employees."* **A company with no
  annual bonus plan cannot rig annual bonus targets** — the DG/ULTA failure mode is
  structurally absent.
- Performance RSUs run on **revenue and operating income, GAAP, explicitly unadjusted**.
  FY2025: revenue target $6.300B / max $7.050B, actual **$7.246B**; operating income target
  $1.675B / max $1.800B, actual **$1.876B**. Vested **175% — the maximum — on a genuine beat
  of the maximum.** *Recorded against the DG/ULTA test: the threshold ($6.300B) was set
  essentially AT the prior year's actual ($6.297B), which is a soft floor and is noted; the
  maximum, however, required +12% and was cleared on results.*
- **402(v) table: TSR $190.56 vs peer group (S&P 500 Consumer Discretionary) $153.99** over
  2021-25 — the **[E3-54] retention test passes on the company's own filed series**, unlike
  EFX's. And the table's own honesty is a candor point: CAP to the PEO was **$900,886 in
  2022**, the collapse year, against $18.1M in 2024. Pay tracked the outcome down as well as up.
- CEO Pemble: base salary **$1,400,000**, SCT total **$7,744,354** — on $1.88bn of operating
  income at a $53bn company. **No severance agreements, no change-of-control cash, no SERP,
  no post-retirement plans, no repricing, no benchmarking to a percentile, and an
  anti-hedging AND anti-pledging policy.** Each stated verbatim in the proxy.
- **Ownership:** Min H. Kao (co-founder) **9.7%**, Jonathan Burrell (co-founder's family)
  **5.0%**, directors and officers as a group **14.8%**, BlackRock 8.0%. **Single class of
  registered shares — no super-voting structure.** Founder alignment without founder control.

**[E4-52] — the lollapalooza check, run explicitly because the brief asked for it.** The
convergence test asks whether several flags point the same way. **They do not converge here;
they point in opposite directions.** The one live flag (auto OEM capital absorption) sits
against zero accounting flags, zero EBITDA promotion, no bonus plan to rig, a falling payout
ratio, a frozen dividend through the bad year, a maintained unit disclosure through six bad
years, and pay that fell 95% in the collapse year. **[E4-52] requires flags *"acting in
favor of a particular outcome"*; a single isolated flag surrounded by counter-evidence is
the opposite configuration.** Not fired.
**THE GUARDRAIL — check before writing the verdict.**
- [x] Confirmed: nothing in this Q3 is being used to **promote** the name. The reporting
      quality is exceptional and it earns Garmin **nothing** at Q2 or Q5. [E2-37]'s textile
      company that allocates capital brilliantly is still a textile company.
- [x] **The PND redeployment IS recorded at Q2 as a moat defect [E4-23]**, not here as a
      strength. Written there in those terms.
- [x] A great manager is **not** the reason to act, and no excisable-cancer case is being
      made. The auto OEM drag is a live allocation flag, not a turnaround thesis.

- **VERDICT: [x] IN — as an OVERLAY**
  *No disqualifier found. **NOT a finding that the managers are honest** — "sincerity and
  empathy can easily be faked" **[E5-17]**, and the filed statement itself is not bedrock
  **[E5-32]**. IN never promotes.*
  **Live flags carried forward:** (1) **auto OEM capital absorption**, ~−$283M cumulative
  operating losses over six years, [E2-56] judged incrementally; (2) **buyback condition-2**,
  de minimis in size, binds position size only; (3) **guidance culture [E5-30] live but
  UNMEASURED** — no guidance in SEC filings, but earnings releases were not swept (run
  defect); (4) the 2025 **cash-tax fall**, acquitted on the jurisdiction table, monitored.

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].** *"Using precise numbers is,
in fact, foolish; working with a range of possibilities is the better approach."* Do **not**
pick a window and defend it; carry the spread alongside the capex band.
**Construction:** OE = OCF − stock compensation − (c). Hand-transcribed from the filed cash-flow
statements of five 10-K vintages (FY2016, FY2019, FY2022, FY2024, FY2025) plus the Q2-2026
10-Q. Working-capital increment included by construction inside OCF, the conservative
direction ([E2-23] constraint 3). Full series: `_research 2026-09-06 GRMN/grmn_oe_series_hand.md`.

**Owner earnings by year ($M, capex end):**
425.1 (2014) · **173.6** (2015) · 573.5 (2016) · 476.4 (2017) · 707.4 (2018) · 517.1 (2019) ·
869.0 (2020) · 612.3 (2021) · **467.2** (2022) · 1,081.3 (2023) · 1,101.7 (2024) ·
**1,196.9** (2025). H1-2026: 656.4 (vs H1-2025 425.9).

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25]:**

| window | capex end | D&A end |
|---|---:|---:|
| 3-yr FY2023-25 | 1,126.7 | 1,163.8 |
| **5-yr FY2021-25** | **891.9** | 960.8 |
| 8-yr FY2018-25 | 819.1 | 878.5 |
| 10-yr FY2016-25 | 760.3 | 813.6 |
| 12-yr FY2014-25 | 683.5 | 727.7 |
| **leave-two-out** (10-yr less FY2024, FY2025) | **663.0** | — |
| TTM to Q2-2026 | 1,427.3 | — |

- **Short-window mean** (3-yr FY2023-25): **$1,126.7M**
- **Long-window mean** (10-yr FY2016-25): **$760.3M**
- **Spread, conservative ends: 48.2%** (1,126.7 vs 760.3); against the 5-yr, **26.3%**.
- **Combined range** (window spread × capex band): **$663M to $1,164M**, with the TTM
  $1,427M displayed and NOT carried (six months of a record year annualised is the
  terminal-date selection [E4-38] warns against).
- **Is that range too wide to reach a conclusion? NO — and this is the one place the width
  does not close the file.** The range's top and bottom differ by 1.75x, which is wide; but
  **every construction in it, including the refused TTM, produces a yield far below the
  sovereign** (1.24% to 2.67%). The Q5 answer is the same at both ends of the range, so the
  width does not need resolving to reach a verdict [E4-25]. Where width *would* matter — at
  a price near the band — it is not near.
- **The distorted years, named in both directions [E4-41]:**
  - **FY2015 DOWN, severely:** $173.6M, the lowest in twelve years, on a **$182.8M cash tax
    payment** for the 2014 inter-company restructuring (FY2016 10-K MD&A, verbatim) plus a
    $121.7M inventory build. Roughly $300M of the FY2015 depression is non-recurring.
  - **FY2021-22 DOWN:** COVID-era inventory builds and the FY2021 capex spike ($307.6M, 1.99x
    D&A, facility expansion); FY2022 is the fitness collapse (segment OI −71%).
  - **FY2023-25 UP — the screen's flagged step (level_shift 1.7, "STEP UP — normalize down").
    Decomposed, and it is more durable than a price wave:** FY2023's OCF jump ($788.3M →
    $1,376.3M) is largely the inventory *drawdown* reversing the FY2021-22 build — a
    working-capital swing, not earnings. But **FY2024-25 is volume: units 16.2M → 18.6M →
    20.7M (+27.8% in two years), with real revenue per unit flat.** A working-capital artifact
    cannot produce a 38% three-year unit gain. **Removed as luck [E4-41]: ~$60M of FY2025
    cash-tax timing** (taxes paid flat at $317.0M while pretax rose 18.8%, the Swiss federal
    line falling $71.8M → $16.7M), and the FY2026 IEEPA tariff refunds (~$21M received in
    Q2-2026, more unrecognised) are excluded from any normalised level.
- **Maintenance capex — (c) as a DISCLOSED JUDGMENT [E2-23]:** **(c) judged at TOTAL CAPEX,
  the conservative end, and the [E3-44] D&A default is displayed rather than used.**
  The reasoning, from the filing: Garmin **owns its factories** in Taiwan, Kansas, the
  Netherlands, the UK, Poland and China — the 10-K calls vertical integration *"one of its
  core competencies"* — so the [E5-20] question is live. It is answered by the ratio, not by
  the adjective: **capex/D&A ran 1.09x (2023), 1.08x (2024), 1.43x (2025), 1.99x (2021)** —
  consistently *above* depreciation, which means the D&A end understates renewal and part of
  capex is growth. **This is NOT the railroad case** (where D&A would be invalid by a
  multiple) **and NOT the anti-railroad** (where capex sits below D&A): capex averages
  **3.4% of revenue** and property and equipment net is 19% of revenue. Because Garmin files
  **no maintenance/growth capex split in any vintage checked**, I take the whole of capex as
  (c) rather than guess the split — the conservative direction, and the [E2-23] instruction
  that (c) *"must be a guess"* honoured by disclosing it as one. The band is narrow anyway
  (7.7% at the 5-yr window), so **(c) is not the swing factor in this file** and cannot
  change the verdict.
- **Band used: $663M–$1,164M. JUDGED OWNER EARNINGS: $1,050M.** Sitting above the 5-yr and
  below the 3-yr, because the filed unit series says the business is genuinely ~25% larger
  than the 5-yr window's average company (units 16.6M → 20.7M; revenue $4,983M → $7,246M),
  while the tax timing and the FY2023 working-capital reversal say the 3-yr mean is flattered.
- **Stock compensation subtracted in full [E5-06]:** yes, at the filed charge —
  **$166.0M (FY2025)**, $137.2M (FY2024), $101.4M (FY2023), rising fast (+63.7% in two years,
  faster than revenue). **[E3-70] noted: the reported charge is the floor of the subtraction,
  not the measure**; no market-value-of-options computation is possible from these filings
  (RSUs, not options), so the floor is what is used and the direction of the error is
  disclosed.
- **Software capex — the HAS defect does NOT bite, checked.** Note 1: Garmin **expenses**
  software development costs; *"Costs incurred by the Company subsequent to achievement of
  technological feasibility are generally not significant."* There is no capitalized-software
  line hiding outside the capex caption. Conservative accounting, verified rather than assumed.
- *If the capex band changes the verdict → UNKNOWABLE.* **It does not: at $663M the yield is
  1.24% and at $1,164M it is 2.18%. Both fail Q5 identically.**

### Great, good, or gruesome? **[E4-20]**
- [x] **great — high return, rising, little capital needed** *(the OPERATING business)*
- [ ] good
- [ ] gruesome
- **Evidence:** FY2025 operating income **$1,876.1M on ~$3.88bn of net tangible operating
  assets = ~48% pre-tax**, on capex averaging **3.4% of revenue**. Revenue +156.9% over ten
  years, funded entirely internally, with the dividend paid and cash still accumulating. That
  is [E4-20]'s savings account paying an extraordinarily high rate.
- **BUT STATE THE [E2-63] CEILING, because it is the whole Q5 problem in one sentence:** the
  great rate is earned on the ~$3.88bn actually employed. The **$4,370M of cash and
  securities — 53% as much again — earns a bond rate, not 48%.** Garmin does not have enough
  places to put its own money at its own rate of return, so the marginal dollar of retained
  earnings compounds at roughly the sovereign, not at 48%. *"most operating businesses are
  capped unless more capital is continuously invested"* **[E2-63]**. The consolidated entity
  is a great business bolted to a bond fund, and the bond fund is growing faster.
  *(The one place management HAS tried to redeploy at scale — auto OEM — has produced ~−$283M
  of cumulative operating losses over six years. The Q3 flag and this ceiling are the same
  fact seen from two sides.)*

### Staying power — score all three **[E5-11]**
- **(1) large and reliable stream of earnings — PASS.** Positive owner earnings in **every
  one of twelve filed years**, including the 2015 tax year, the 2020 pandemic and the 2022
  fitness collapse. Range $173.6M–$1,196.9M; never negative.
- **(2) massive liquid assets — PASS, and this is the brief's [E5-11] item, verified.**
  At Q2-2026: cash and cash equivalents **$2,334.2M** + current marketable securities
  **$332.0M** + noncurrent marketable securities **$1,703.7M** = **$4,369.9M**, against
  **zero debt of any kind**. Net cash is **$22.66/share, 8.2% of the market cap.** Confirmed
  from the filed balance sheet, not the screen.
- **(3) no significant near-term cash requirements — PASS. The one that usually kills does
  not bite here.** There are **no debt maturities at all — there is no debt.** The fixed
  claims are: inventory purchase obligations **$1,030.6M ($801.7M within 12 months)**;
  operating lease payments **$235.5M total, $43.5M within 12 months**; and the dividend
  (~$693M/yr, and **discretionary in the strongest sense — it requires an annual shareholder
  vote under Swiss law and was frozen for two years in 2022-23**). Total 12-month fixed
  claims ≈ **$845M** against $4,370M of liquid assets and ~$1.4bn of annual operating cash
  flow. **Coverage ~5.2x on liquid assets alone [E2-54], with no covenants and no lender.**
  **[E5-39] respected: no revolver is counted because none exists** — the full-text search
  returned zero hits for "revolving credit", "credit facility", "notes payable" and
  "borrowings" in both the 10-K and the 10-Q. Garmin does not depend on the kindness of
  strangers because it has never asked them for anything.
- **ASC 842 — immaterial, and stated:** operating lease ROU assets $196.2M, total fixed lease
  obligations $235.5M, annual lease cost $63.9M — **0.9% of revenue.** Nothing like the CMG
  or EAT lease tails.
- **Contingent liabilities — ordinary course only.** Item 3 carries no named matter, no
  quantified accrual, and no persistence across vintages. The one contingent *asset* is
  disclosed and not booked: additional IEEPA tariff refunds after the 2026-02-20 Supreme
  Court ruling, *"which have not been recognized in the Company's consolidated financial
  statements"* — the conservative direction.
- **Leverage, named and quantified [E4-16, E3-29]: ZERO.** Not low — zero. FY2025 10-K,
  verbatim: *"We have no outstanding long-term debt as of December 27, 2025 and otherwise
  have no meaningful debt-related interest rate risk."* **This is the second name in the
  queue's history to pass all three [E5-11] strengths, after BMI — and it does so with a
  larger absolute cushion.**

### Name the specific way THIS business dies **[E2-27, E3-24]**
*Modelled on exposure, not experience [E4-40]. The bar is [E4-51]: a bear case its holders
would accept as fairly stated.*

**DEATH 1 — the platform squeeze finally lands at the consumer end. A REAL POSSIBILITY.**
- **Mechanism:** the general-purpose wrist computer keeps absorbing sport-specific features
  until the premium instrument's price band collapses into it. Garmin's own Item 1 names
  **Apple, Google, Samsung, Huawei and Xiaomi** as fitness competitors — five companies that
  can each fund Garmin's entire $1.13bn R&D budget out of a quarter's profit and give the
  software away to sell something else.
- **Quantified from filed figures:** Garmin has already filed the template. In **FY2022**,
  fitness segment margin went **23.4% → 9.4%** in one year. Apply the FY2022 margin to the
  FY2025 revenue base and hold outdoor at its own FY2022 margin (37.2%): fitness OI
  $2,357.0M × 9.4% = **$221.6M**, outdoor $2,054.1M × 37.2% = **$764.1M**, total **$985.7M**
  against the actual $1,416.2M — **a $430M hit to operating income**, taking judged owner
  earnings to roughly **$770M** and the zero-growth value to roughly **$76/share plus the
  $22.66 of net cash ≈ $99**.
- **Likelihood: [x] a real possibility.** It has happened once already, at that exact depth,
  within the filed record.
- **The evidence against it, stated at full strength [E4-51]:** it happened *and reversed
  within two years to a record*, and it coincided with the post-COVID demand air-pocket
  across the whole category rather than with share loss to Apple. Through the entire Apple
  Watch decade Garmin's fitness profit went **up 4.5x**, and **Apple's own wearables category
  has now declined three consecutive years**. A bear who wants this death has to explain why
  the eleventh year of the attack works when the first ten did not.

**DEATH 2 — the wave ends: the unit surge was a replacement cycle, not a level. A REAL POSSIBILITY.**
- **Mechanism:** units +38% in three years (15.0M → 20.7M) is far above the decade trend of
  +2.5%/yr. If FY2023-25 is a COVID-cohort replacement crest plus the tariff pull-forward,
  units revert toward 16-17M and the mix stops migrating upward.
- **Quantified:** owner earnings revert to the **5-yr mean $892M** or, on the harsher
  leave-two-out construction, **$663M** — zero-growth values of roughly **$110/share** and
  **$88/share** including net cash. **This is not a speculative death; it is what the file's
  own conservative windows already assume.**
- **Likelihood: [x] a real possibility** — and partially the base case, which is why the
  judged $1,050M sits below the 3-yr mean rather than at it.

**DEATH 3 — auto OEM keeps eating. A LOW-LEVEL POSSIBILITY as a solvency matter, a REAL one as a value drag.**
- ~−$283M cumulative over six years, $109.3M of segment R&D in FY2025 alone, and the company
  says in its own risk factor it *"expect[s] to continue doing so."* At the current run rate
  this is ~−$50M/yr against $1.9bn of operating income: an annoyance, not a solvency event.
  The exposure is that tier-one auto programs have **fixed multi-year commitments** and the
  filing warns *"We may incur substantial restructuring costs if we are unable to generate
  profits from auto OEM contracts."* Navico's $334.5M FY2025 write-off is the shape of what
  that looks like at a peer.

**DEATH 4 — solvency. ESSENTIALLY UNNAMEABLE, and I could not construct one.**
- Zero debt, $4.37bn liquid, no covenants, no lender, no maturities, twelve consecutive years
  of positive owner earnings, and a discretionary dividend requiring a shareholder vote.
  To kill Garmin on cash you must first destroy the earnings for many years *and* have
  management refuse to cut a dividend it has already demonstrated it will freeze. **[E2-55]'s
  standard — "acceptable long-term results under extraordinarily adverse conditions" — is met
  as well as any name this queue has run.**
- **[E3-66] jurisdiction, since this is a non-US filer:** Garmin is Swiss-domiciled
  (Schaffhausen) and its shareholders' position is **stronger than the [E3-66] warning
  contemplates, not weaker** — a single class of registered shares, no super-voting founder
  stock, a **binding** annual shareholder vote on dividends and on maximum executive and board
  compensation under Swiss law, and NYSE listing with full SEC reporting. The Swiss structure
  gives holders *more* votes that bind than a Delaware filer would. Recorded as checked, not
  waved past. *(One real jurisdictional item: $95.0M of retained earnings is indefinitely
  restricted from distribution under Taiwanese law — disclosed, immaterial at 1.1% of equity.)*

- **VERDICT: [x] IN**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**Q5 IS OPEN: Q1 IN · Q2 IN · Q3 IN · Q4 IN.**

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."*
**Honest pre-tax expectancy at this price: ~7.5% (range 7.1%–8.1%). BELOW THE ~10% FLOOR.
The name is not ranked — it is quit on, whatever the sovereign is.**
Derivation is below at "what the price already assumes"; it is the 2.14% owner-earnings yield
on the operating business plus an honest ~5-6% perpetual growth rate, against a required
+7.86%.
**No risk premium in the discount rate [E3-42]** — certainty lives at Q1 and in the end
discount, never in the rate. The bare 5.24% is used.

**THE NET CASH IS CREDITED EXPLICITLY, as the brief required [E5-11].** Every figure below
separates the two things the market cap is buying:
- **net cash and marketable securities $4,369.9M = $22.66/share** (Q2-2026 balance sheet,
  zero debt against it), and
- **the operating business, priced at $254.37/share ($49,056M)** — the quote less the cash.
Yields are shown both ways. Crediting the cash **helps by about 0.17 points of yield** and
raises every value by $22.66/share. **The brief's hope (b) is therefore tested and largely
fails:** the fortress is real but it is only 8.2% of the capitalisation, and it does not
change any verdict here.

**One book. Owner earnings against the bond.** A DCF may run as an engine; it casts no
vote **[E3-34]**.

**1. THE YIELD**

| construction | OE ($M) | yield on cap | yield on the operating business |
|---|---:|---:|---:|
| leave-two-out (10-yr less FY24, FY25) | 663.0 | 1.24% | 1.35% |
| 10-yr FY2016-25 | 760.3 | 1.42% | 1.55% |
| 5-yr FY2021-25 *(the screen's row)* | 891.9 | 1.67% | 1.82% |
| **JUDGED** | **1,050.0** | **1.97%** | **2.14%** |
| 3-yr FY2023-25, capex end | 1,126.7 | 2.11% | 2.30% |
| 3-yr FY2023-25, D&A end | 1,163.8 | 2.18% | 2.37% |
| **best single year ever (FY2025)** | **1,196.9** | **2.24%** | **2.44%** |
| TTM to Q2-2026 *(displayed, refused)* | 1,427.3 | 2.67% | 2.91% |

**Sovereign: 5.24%** (US Treasury 30-yr, 2026-09-04, struck fresh from the issuing authority).

**Every construction pays less than half the government bond — including the best year in
the company's history, including the refused TTM, and including the full credit for net
cash.** The best-year-ever yield of 2.44% is **2.80 points below** the 30-year Treasury.

**2. WHAT THE PRICE ALREADY ASSUMES**
- **Growth needed to justify the quote against the bare bond: +3.10%/yr, perpetual.**
- **Growth needed to clear the [E4-28] floor: +7.86%/yr, perpetual.**
- **What the business has actually done — and this is the file's hardest fact against my
  conclusion, stated at full strength [E4-51]:**

| filed series | window | rate |
|---|---|---:|
| owner earnings | FY2016→FY2025 | **+8.52%/yr** |
| owner earnings | FY2014→FY2025 | +9.87%/yr |
| revenue | FY2015→FY2025 | +9.89%/yr |
| operating income | FY2016→FY2025 | **+13.01%/yr** |
| diluted EPS | FY2021→FY2025 | +11.24%/yr |

**Garmin's filed decade EXCEEDS the +7.86% the floor requires.** This is the second name in
the queue's history to do so (after CTAS), and it is why this file is not a routine failure.
**It fails anyway, on the [E4-44]/[E2-63] decomposition:**

The decade's operating income grew **3.01x = revenue 2.40x × margin 1.25x** (op margin 20.7%
→ 25.9%). Revenue's 2.40x decomposes, using the filed unit series, as:
**units 1.23x (+2.5%/yr) × real revenue per unit 1.45x (+3.8%/yr) × inflation 1.34x (+3.3%/yr).**

Each lever, judged forward:
- **The mix lever is arithmetically near-spent, and the filings already show it stopping.**
  The +3.8%/yr real rev-per-unit was the migration from $100 PNDs to $600 watches. **That
  migration is complete — the PND is gone.** And the proof it has stopped is in the filed
  series: **FY2022→FY2025 real revenue per unit is −1.8%, i.e. flat.** You cannot run the
  next decade on a lever whose last three years read zero.
- **The volume lever is the live one but not at the recent rate.** Units +11.3%/yr over three
  years against +2.5%/yr over ten. The three-year rate is a crest (post-COVID replacement
  plus, on the filer's own disclosure, tariff-affected timing); the decade rate is the
  honest one. Call it 2-4%/yr.
- **The margin lever is bounded.** 25.9% today; even 30% is +16% in total and then zero
  **[E2-63]**. It is bounded further by the two segments moving the wrong way — auto OEM at
  −7.3% and aviation down 8.3 points from its 2019 peak.
- **Inflation ~2-3%/yr is not a real return** but does belong in a nominal comparison against
  a nominal bond.

**Honest go-forward perpetual: ~5-6%/yr, not 7.9%.** And the corpus's base rate binds the
other way too **[E4-35]**: *"fewer than 10 of the 200 most profitable companies will attain
15% annual growth in EPS over the next 20 years"* — a floor case needing near-8% forever
carries the burden of proof, and the decomposition does not discharge it.

- **Honest pre-tax expectancy: 2.14% + 5-6% = ~7.1-8.1%, judged ~7.5%.** Below the floor.

**3. WHAT YOU ARE PAID**
- **Return at the current price: 1.97% on the cap (2.14% on the operating business) against a
  5.24% sovereign = MINUS 3.10 to MINUS 3.27 points.** You are paid a little over 2% to own
  the equity risk of a consumer-electronics manufacturer, when the government pays 5.24% for
  taking none.

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- sovereign used **5.24%** — **the bare rate, no per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — a point estimate claims precision this
method cannot support:
**All values are per share and INCLUDE the $22.66 of net cash [E5-11], stated separately:**

| construction | operating business | + net cash | **total value/share** |
|---|---:|---:|---:|
| leave-two-out | $66 | $22.66 | **~$88** |
| 10-yr | $75 | $22.66 | **~$98** |
| 5-yr *(the screen's row)* | $88 | $22.66 | **~$111** |
| **JUDGED** | **$104** | **$22.66** | **~$127** |
| 3-yr | $111-115 | $22.66 | **~$134-138** |
| best year ever | $118 | $22.66 | **~$141** |
| TTM *(refused)* | $141 | $22.66 | **~$164** |

- **conservative ~$90 · judged ~$125 · optimistic ~$140 · most generous refused construction
  ~$165 · CURRENT PRICE $277.03**
- **At the [E4-28] floor rather than the sovereign** (owner earnings capitalised at 10%):
  **~$57 to $97, judged ~$77.**
- **The price is 2.2x the judged zero-growth value and 1.7x the most generous construction
  in the file — the one I refused to carry.** There is no construction, at any window, at
  either capex end, with full net-cash credit, in the best year the company has ever had,
  that reaches today's quote.

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].** *(Corrected 2026-09-03, found by the
HHH run — this block still carried v4.0's "THERE IS NO HURDLE" heading, the SEVENTH
surviving home of the rule the framework rewrote on 2026-08-28. The floor section above at
[E4-28] already governs; this block is the ranking that applies only to what clears it.)*
- **Floor verdict first: honest pre-tax expectancy ~7.5% (7.1-8.1%) vs ~10% [E4-28] —
  BELOW. The name is QUIT ON, NOT RANKED, and the lines below are therefore not filled in.**
- points over sovereign, this name: **−3.1 points** *(recorded for the file, not as a ranking
  input — a name below the floor does not enter the ranking at all)*
- against the rest of the opportunity set: **not run.** [E4-28] is a gate, not a tiebreak.

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [ ] **Normal method [E4-11]** — not used. No margin is subtracted anywhere in this file.
- [x] **Screamer test [E4-01]** — **OUTCOME THREE: the price is above the whole range.**
      The conservative case is ~$88-111; the judged case ~$127; the *most generous
      construction in the file* — the TTM I refused to carry — is ~$164. **The price is
      $277.03.** No margin was added on top; "startlingly low" is what you observe, and what
      is observed here is the opposite.
- **Windage count: 2, and both are disclosed and justified in writing as [E4-11] requires.**
      (1) **(c) taken at total capex** rather than the [E3-44] D&A default; (2) **judged OE
      $1,050M set below the 3-yr mean** of $1,126.7M. **Justification: neither is
      load-bearing.** Spending zero windage — the D&A end of the 3-yr window, $1,163.8M —
      gives a 2.18% yield and a ~$138 value against a $277 price. **The verdict is identical
      with all conservatism removed**, which is the test [E4-48] asks for, and it is why the
      double count does not have to be resolved before ranking.

- **VERDICT: [x] UNKNOWABLE → the price. Not IN. Ranking position: NONE — quit on at the
  [E4-28] floor, below the ranking entirely.**
  *Recorded precisely: this is a verdict about the PRICE, not about the business. Q1-Q4 all
  returned IN. Nothing here is a finding against Garmin as a business; the file closes
  because a good business at 2% does not clear a floor stated at 10%.*

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

*No position is taken, so Q6 is written as the **re-look protocol** — the yardsticks
established "prior to the act" [E1-02] so the next run inherits a pre-registered test rather
than a fresh opinion.*

**Pre-committed before entry [E1-02]:**
- **Thesis-confirming metric: the filed total unit series.** It is the honest series [E4-55],
  it exists, and it has 21 years of history. **Confirming: units continuing above ~19M with
  real revenue per unit not falling.** (FY2025: 20.7M at $350 nominal.)
- **Thesis-breaking metrics and their thresholds:**
  1. **Units below 17M in any full year** — the FY2022 level; would confirm DEATH 2, that the
     FY2023-25 surge was a replacement crest.
  2. **Fitness segment margin below 20%** for a full year (FY2025: 30.8%) — the first hard
     evidence the platform squeeze is landing; below 15% is the FY2022 repeat.
  3. **[E2-49] withdrawal of the unit-sales sentence or of the five-segment decomposition.**
     Garmin kept both through six bad years; dropping either now would be the metric-switch
     the corpus says follows deterioration.
  4. **Aviation margin below 22%** (FY2025: 26.1%, down from 34.4% in 2019) — the
     certification moat eroding on the one series that measures it.
  5. **Auto OEM losses widening beyond ~$100M/yr**, or a restructuring charge in that segment
     — the [E2-56] allocation flag becoming material.
  6. **Buybacks above ~$500M/yr while the price sits above the band**, or the payout ratio
     rising through ~60% of owner earnings.
- **Next catalyst dates:** FY2026 10-K (expected ~2027-02) — the first full year testing
  whether units hold above 20M and whether the mix lever is really flat; the 2027 AGM
  dividend proposal (the $4.20 for 2026 was +16.7%, the first meaningful payout climb);
  Honeywell's Aerospace spin-off, expected Q3 2026, which will for the first time put
  **stand-alone avionics financials on the filing rung** and make Row B answerable.

**THE PRE-COMMITTED RE-LOOK PRICE.** **~$125/share judged zero-growth at a 5.24% sovereign,
including net cash — recomputed at the rate of the day.** The floor clears near **~$77**.
**Re-open the file below ~$140**, where the best-year-ever construction stops being a stretch
and the floor comes within reach of an honest 5-6% growth rate. At $277.03 no re-look is
needed; at $140 the arithmetic changes character.

**The sell rule [E2-28]** — two triggers, three hold conditions. *No position exists; run as
the test a holder would face today:*
- **SELL if the market judges it more valuable than the facts indicate — THIS TRIGGER IS
  LIVE.** At 2.2x the judged zero-growth value with an honest expectancy of ~7.5% against a
  5.24% bond, a holder is in exactly the position [E2-28] describes.
- SELL if funds are needed for something more undervalued or better understood — not
  applicable; no position.
- **HOLD conditions, scored:** return on equity capital **satisfactory (~48% pre-tax on net
  tangible operating assets — emphatically yes)** · management **competent and honest (no
  disqualifier found; Q3 IN)** · market **does not overvalue — FAILS.** Two of three hold,
  the third does not, and the third is the one that fires the trigger.
- *Price appreciation and holding period are explicitly rejected as reasons to sell — and
  neither is being used here. The reason is the yield against the bond.*

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring
question, answered: **Garmin has already run this exact test once, and both answers are on
file.** The FY2016-22 unit decline was NOT an aberrational cycle — it was the PND franchise
permanently dying, and intrinsic value in that segment went to zero. The FY2022 fitness
collapse **was** an aberrational cycle, and recovered to a record within two years. **The
company supplies both worked examples of [E3-30]'s question**, which is why the thresholds
above are set on the physical series rather than on margin alone: **units told the truth in
both cases, and earlier than margin did.**

**Do not trim winners [E5-14].** **Position size — ZERO.** Not a sizing judgment: the name
did not clear the floor and never entered the ranking. Had it cleared, the live buyback
condition-2 flag and the auto OEM allocation flag would each bind size downward [E4-13].

- **VERDICT: [x] IN** — *the exit discipline is specified and pre-registered, and the
  monitoring question is answerable from series the company has filed for 21 years. This
  does not promote the name: Q5 already closed the file on price.*

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN → Q2 IN → Q3 IN → Q4 IN → Q5
      opened legitimately → closed on price → Q6 written as a re-look protocol.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q2 is IN as
      **NARROW**, not as PROVISIONAL. The *aviation sub-class* is explicitly held incomplete,
      but the verdict rests on the 75.5% of profit where both the subject's and the
      attackers' filed data are in hand, and the file says so.
- [x] Every UNRESEARCHED item names the artifact and where it lives — see the work orders in
      the register below.
- [x] The UNKNOWABLE at Q5 states what cannot be known: whether the market will pay a price
      at which this business clears a 10% floor.
- [x] Step 0: filing read with accession number (0001193125-26-056028); figures cross-checked
      against the filed statements (OCF, capex, segment totals, cash + securities).
- [x] Owner earnings on multi-year means; **five windows plus leave-two-out plus a displayed
      and refused TTM**; capex band disclosed as a judgment with the [E3-44] default shown
      and the reason for departing from it stated.
- [x] Competitor row filled with 4 filed peers; the unobtainable peers named with the reason
      and a work order.
- [x] Sovereign for the earnings currency (USD, confirmed against the Swiss domicile from the
      filing), from the issuing authority (US Treasury), dated 2026-09-04, struck fresh.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen (Bar 2, the screamer test, outcome three); **windage count 2, disclosed
      and justified** — the verdict is unchanged with all conservatism removed.
- [x] Prices dated; aggregator (Yahoo) used for the live quote only and flagged.
- [x] Run committed to git after every question, under the write-early protocol.

### RUN DEFECTS, CONFESSED
1. **Earnings releases and calls were NOT swept.** The "no guidance in SEC filings" finding
   is scoped to 10-K and 10-Q only. Garmin does issue annual guidance in its 8-K releases, so
   the **[E5-30] guidance-culture flag is live but unmeasured**, and [E3-48]'s
   guidance-vs-outturn sweep was not run. This is the largest hole in the Q3 read.
2. **The FY2023 10-K/A (2024-11-29, acc 0000950170-24-131914) purpose was never extracted.**
   An amendment inside the owner-earnings window should have been read.
3. **Polar Electro Oy and Suunto Oy statutory accounts (Finnish PRH) not pulled** — the row
   is incomplete at the private-competitor end and is marked UNRESEARCHED, not UNKNOWABLE.
4. **FY2009-FY2013 owner-earnings inputs were not hand-transcribed** — the OE series starts
   at FY2014. The PND-collapse *revenue* history goes back to FY2005, but owner earnings
   through the actual collapse were not rebuilt, so the "how much cash did the dying category
   throw off" question is unanswered.
5. **CPI 2025 annual average (321.943) was carried from the WMT run's BLS fetch** rather than
   re-fetched here; the BLS API returned no M13 for 2025 in this session's call.
6. **Segment operating margins are my computation**, not filed ratios; Garmin files the
   components, not the margins.
7. **The brief's premise that units would be an absence finding was wrong**, and I ran with
   the brief's framing for the first part of the session before testing it. The correction
   became the run's best instrument, but it was found by reading MD&A, not by design.
8. The competitor-row sub-agent was killed once mid-task and relaunched; its first pass lost
   `grmn_segment_history.md`, whose total-units series I rebuilt by hand from the vintages.

---
## REGISTER
- **Verdict: [x] UNKNOWABLE — about the PRICE, not the business.** Q1-Q4 all IN. The business
  gates cleared; the file closed at Q5 on the [E4-28] floor.
- **One line: Garmin is a great operating business — ~48% pre-tax on net tangible assets,
  zero debt, $4.37bn net cash, three [E5-11] strengths passed, and the only company in this
  queue that has already survived the death of its founding category — priced at 2.2x the
  most honest zero-growth value and paying 2% against a 5.24% bond.**
- **THE WORK ORDERS (UNRESEARCHED items, each with its artifact and rung):**
  1. **Garmin 8-K earnings releases FY2021-FY2026** · EDGAR, rung 2 · not blocked, not
     fetched · resolves the [E5-30]/[E3-48] guidance question.
  2. **Garmin 10-K/A, acc 0000950170-24-131914** · EDGAR, rung 2 · not blocked, not read.
  3. **Finnish PRH statutory annual accounts, Polar Electro Oy and Suunto Oy** · Finnish
     registry, below the evidence ladder's SEC rungs · resolves the private-peer row.
  4. **Honeywell Aerospace Form 10 / stand-alone financials** · does not yet exist; expected
     with the Q3-2026 spin-off · would make the aviation row answerable for the first time.
- **What specifically cannot be known (the UNKNOWABLE):** whether Garmin's ~5-6% honest
  perpetual growth is instead the ~8% its filed decade delivered. The decade's record
  supports the higher number; the decomposition says the mix lever that produced most of it
  is spent. **That disagreement is not resolvable from filings — it is a judgment about
  whether a completed migration repeats — and at $277 it does not need resolving, because
  even the 8% case only reaches the floor, never comfortably past it.**

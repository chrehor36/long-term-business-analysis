# Company Run — COGNEX CORPORATION (CGNX) — 2026-09-07
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
cap_m 10107 | oe_bottom_m 98 | oe_top_m 146 | spread 0.493 ($98M to $146M)
yield_bottom 0.97% | vs_sovereign -4.27 pts | growth_required 9.03%
level_shift 0.68   "STEP DOWN - the series has changed level"
level_shift_oe 0.53   "STEP DOWN"           <-- both nine-year series agree, and both say DOWN
level_shift_full 1.05 (18 years filed)      <-- the FULL series says NO step
best_year_dep 0.051 / best_year_dep_oe 0.073
newest_filing 2025-12-31
```

**This is the first STEP DOWN in the reading order, and the three-way split between the
nine-year cash series (0.68), the nine-year owner-earnings series (0.53) and the eighteen-year
series (1.05) is the central question of this run.** `level_shift`'s own docstring names the
low-ratio-tight-spread case as *the dangerous one*: it looks well-determined and is measuring a
business that has already stepped down. Every number above is re-derived below from the filed
statements. Where the re-derivation disagrees with the row, **the filing governs** (operator
rule 4), and it disagrees in four places — all recorded.

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.24 %** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-year
  (the issuing authority; FRED DGS30 is the fallback, not the source)**
- FX: Cognex reports and pays dividends in **USD**. **67% of 2025 revenue came from customers
  based outside the United States** (10-K FY2025, Item 1), denominated in EUR, RMB, JPY, KRW,
  INR, MXN and USD. The functional currency is the US Dollar. The sovereign is therefore USD;
  the currency exposure is recorded as a Q4 finding, not handled by swapping the rate.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- documents · dates · accession numbers:
  - **10-K FY2025**, period 2025-12-31, filed **2026-02-12**, accession **0000851205-26-000012**
  - **10-Q Q2 2026**, period **2026-07-05**, filed 2026-08-06, accession **0000851205-26-000065**
  - **10-K FY2024** accession 0000851205-25-000012 (filed 2025-02-13) · **FY2023**
    0000851205-24-000027 · **FY2022** 0000851205-23-000004 · **FY2021** 0000851205-22-000008 ·
    **FY2020** 0000851205-21-000005 · **FY2019** 0000851205-20-000002
  - **DEF 14A** filed 2026-03-13, accession 0001193125-26-105065
- **Seven consecutive 10-K vintages were read**, not one. The vintage comparison is where this
  run's two sharpest findings came from (Q2), and neither is visible in the newest filing alone.
- figure cross-checked against the filed statement: **see the cross-check block below.**

**SHARE COUNT — read off the cover of the LATEST periodic filing, not the 10-K.**
`python Screens/cover_shares.py CGNX`:
```
CGNX  COGNEX CORP
   10-Q filed 2026-08-06, period 2026-07-05, accession 0000851205-26-000065
   Common Stock, par value $.002 per share             168,223,842
```
**ONE class only** (Common, $0.002 par; preferred authorised, none issued — balance sheet,
10-K FY2025). No dual-class question arises. Note the count is **rising** against the
2025-12-31 balance sheet's 166,997 thousand shares issued and outstanding: option exercises in
H1 2026 outran the $105.2M of buyback. Recorded at Q3.

**Price:** **$62.25**, 2026-09-04 close, Yahoo Finance — *aggregator, used for the live quote
only, and flagged as the protocol requires.*
**Market cap = 168,223,842 × $62.25 = $10,472M.**

**DEFECT IN THE BRIEF'S ROW, #1 — the cap is stale and LOW.** The queue carried `cap_m 10107`,
which implies $60.08. The struck price is **$62.25**, and the cap is **$10,472M, 3.6% higher
than the queue's**. Every yield in the row is therefore 3.6% too generous. Re-struck here as
the brief instructed.

*(Price history, same source, month-end closes, for the record: $87.59 Oct-2021 · $41.45
Sep-2022 · $35.99 Oct-2023 · $35.86 Dec-2024 · **$27.30 Apr-2025 (the low)** · $45.30 Sep-2025 ·
$38.74 Jan-2026 · $54.40 Feb-2026 · $72.42 Jun-2026 · $62.25 Sep-2026. **The quote has roughly
2.3x'd off the April-2025 low in seventeen months.** This is recorded here, not at Q5, because
it is a fact about the price and not about the business.)*

---
## CROSS-CHECK — tagged data against the filed statement (operator rule 4)

Companyfacts XBRL against the **Consolidated Statements of Cash Flows, 10-K FY2025**
(accession 0000851205-26-000012):

| line | XBRL | filed statement | agree |
|---|---|---|---|
| Net cash provided by operating activities 2025 | 245.51 | **$245,514** | yes |
| ... 2024 | 149.08 | **$149,081** | yes |
| ... 2023 | 112.92 | **$112,916** | yes |
| Purchases of PP&E, net of proceeds, 2025 | 8.74 | **$(8,743)** | yes |
| Stock-based compensation expense 2025 | 48.52 | **$48,517** | yes |
| Revenue 2025 | 994.36 | **$994,359** | yes |

**DEFECT IN THE TOOLING, #1 — the D&A tag is DEPRECIATION ONLY, and it silently drops
intangible amortization.** `tools/run.py`'s `DA` list resolved to **$20.3M for 2025**. The filed
statement carries **two** lines: *Depreciation of property, plant, and equipment $20,289* **and**
*Amortization of intangible assets $10,504*. True D&A 2025 is **$30.79M, 52% higher than the tag
returned.** The gap opened in 2024 when Moritex's acquired intangibles began amortising
($11.4M against $3.3M in 2022). Since D&A is the corpus's default (c) **[E3-44, E2-41]**, the
conservative end of every owner-earnings figure `run.py` printed for 2024 and 2025 is **too high
by roughly $10M a year**. Corrected throughout below; the D&A series is rebuilt by hand from six
filed cash-flow statements.

**DEFECT IN THE TOOLING, #2 — the SBC tag returns $1.4M for 2020. The filed figure is
$42,661.** The `SBC` list unions `ShareBasedCompensation` with
`AllocatedShareBasedCompensationExpense`, and for FY2020 the union picked up a component, not
the total. Any window reaching back to 2020 computed from the tags overstates owner earnings by
**$41M in that year**. Caught only because the FY2021 10-K's cash-flow statement was read.
**This is exactly the class of error operator rule 4 exists to catch, and it was caught.**

**The hand-rebuilt series, every figure from a filed Consolidated Statement of Cash Flows
($M).** Sources: 10-K FY2019 (2017-2019), FY2021 (2019-2021), FY2023 (2021-2023),
FY2025 (2023-2025). Overlapping years agree exactly across vintages — no restatement found.

| year | OCF | SBC | Depreciation | Amort. of intangibles | **D&A total** | capex |
|---|---|---|---|---|---|---|
| 2017 | 224.3 | 31.94 | 13.68 | 3.31 | **16.99** | 28.8 |
| 2018 | 223.5 | 41.09 | 18.47 | 3.08 | **21.55** | 37.1 |
| 2019 | 253.31 | 45.59 | 21.53 | 3.37 | **24.90** | 21.75 |
| 2020 | 242.40 | 42.66 | 22.14 | 4.36 | **26.50** | 13.30 |
| 2021 | 314.07 | 43.77 | 16.62 | 3.67 | **20.28** | 15.46 |
| 2022 | 243.41 | 54.51 | 16.35 | 3.27 | **19.62** | 19.67 |
| 2023 | 112.92 | 54.77 | 17.27 | 4.61 | **21.88** | 23.08 |
| 2024 | 149.08 | 52.44 | 21.27 | 11.42 | **32.69** | 15.04 |
| 2025 | 245.51 | 48.52 | 20.29 | 10.50 | **30.79** | 8.74 |
| H1 2026 | 114.25 | 23.15 | — | — | — | 4.29 |

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.**

Cognex sells a camera that decides. The physical object is a small sealed box holding an image
sensor, a lens, a light, a processor and — the part that matters — a library of software that
turns the picture into a yes/no or an x-y coordinate: *is the cap on the bottle, where exactly
is this part so the robot can grab it, what does this barcode say, is this weld cracked.* The
box is bolted to a production line or hung over a parcel conveyor and it fires thousands of
times an hour, forever, without a person.

The money comes from two places and they behave differently.

**The ID readers** (DataMan) are the larger and simpler half by unit count. A parcel sorter
needs a reader above every conveyor lane; a distribution centre buys them by the hundred when
it is built and by the dozen when it is expanded. This is capital equipment sold into somebody
else's construction budget, and the buyer's decision is a horse race on read rate: the reader
that misses fewer barcodes at speed wins, because every no-read is a parcel a human has to
handle. That is a **measurable, benchmarkable** claim, which is both the strength (it can be
proven in a bake-off) and the weakness (it can be *disproven* in a bake-off by anyone who
catches up).

**The vision systems and software** (In-Sight, VisionPro) are the older, stickier half. A vision
application is *programmed* — someone spends days configuring the tools, the lighting, the
fixturing and the accept/reject thresholds for one specific part on one specific line. That
engineering effort is a sunk cost that belongs to Cognex's software, and it is why a plant that
standardises on VisionPro tends to keep buying VisionPro. The switching cost is not in the box;
it is in the thousand hours of application engineering already sitting on the factory floor.

**The cost structure is the striking part, and it is the whole investment case.** Cognex does
not manufacture most of what it sells: *"Most of Cognex's hardware products … are manufactured
utilizing third-party contractors … Cognex's primary contract manufacturers are located in
Indonesia and Malaysia"* (10-K FY2025, Operations). It buys assembled hardware, loads its own
software onto it at its own distribution centres, and ships. That is why **capital expenditure
was $8.7M in 2025 against $994M of revenue — 0.9%** — and why gross margin has historically run
in the low-to-mid seventies. The company is, in economic substance, **a software company with a
hardware delivery mechanism**, and the hardware is rented from Indonesia.

Two consequences follow and both are load-bearing. First, **the operating leverage is enormous
in both directions**: fixed cost is people (2,745 of them at end-2025), and revenue is somebody
else's capex, so a 17% revenue fall takes operating income down 47% (2022 to 2023) and a 20%
revenue rise takes it up 109% (H1 2025 to H1 2026). Second, **there is almost nothing to
depreciate**, which makes the corpus's default (c) proxy *generous* rather than punitive here —
the reverse of the usual case, and it is dealt with explicitly at Q4.

**The scarce input this business controls.**

Not the hardware. The sensors are somebody else's, the processors are somebody else's, the
assembly is a contract manufacturer's. Not the optics either, since 2023, because Cognex had to
**buy** that (Moritex, $296M) rather than own it.

What it controls, if anything, is **the accumulated application library** — three decades of
vision tools already made to work on specific classes of part under specific classes of
lighting, plus the installed base of engineers who know how to drive them. The company's own
words on IP are notably modest: *"we believe that our business as a whole is **not materially
dependent on any particular patent, trademark, copyright, or other intellectual property
right**"* (10-K FY2025, Intellectual Property). That sentence rules the patent estate out as the
moat. **It leaves the scarce input as an accumulated software position, and an accumulated
software position is exactly the asset a step-change in the underlying technology can
devalue.** That question is Q2's, and the company's own risk factors answer it there.

**Will the fundamentals look broadly the same in ten years?**

The *demand* will. Factories will still assemble discrete objects, warehouses will still move
parcels, and looking at things faster and more consistently than a person can will still be
worth paying for. Cognex's served problem is not going away.

**Whether the fundamentals of Cognex's business look the same is a different question, and the
filing itself raises it:** *"The market for our products is characterized by **rapidly changing
technology and increasingly capable competitors**"* (10-K FY2025, Item 1A). I am recording that
sentence **here** and carrying it to Q2 rather than resolving it here, because the framework
splits understanding (Q1) from durability (Q2), and this is a durability claim.

**[E4-46] check** — *"if we can't make a decision in five minutes, we can't make it in five
months."* The business took five minutes. One segment, one share class, no debt, no float, no
percentage-of-completion outside a small application-specific-solutions carve-out, no
capitalised development, no unconsolidated vehicles, no adjusted-earnings bridge in the
statements. Eighteen years of clean tagged data that ties to the filed statements at every year
checked. Whatever closes this file, it will not be that the business is unintelligible.

- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**MY PRIOR, WRITTEN BEFORE THE EVIDENCE SO IT CAN BE READ AGAINST ME [E4-26]:** the brief and
I both leaned **IN NARROW**. Machine vision is specified into production lines, the software is
sticky, gross margin has run near 70% for two decades, and the company has no debt and a long
record of high returns on capital. **That prior was refuted, and it was refuted mostly by
Cognex's own filings rather than by the competitor row.**

### THE STEP DOWN, ADJUDICATED — the question this run exists to answer

The screen's three readings disagree because they are measuring three different things. Here
is the filed series they are all reading, rebuilt from the statements ($M and %):

| year | revenue | gross profit | **GM %** | operating income | **OM %** | net income | **ROE %** | rev/employee ($k) |
|---|---|---|---|---|---|---|---|---|
| 2016 | 529.5 | 398.4 | **75.2** | 154.1 | **29.1** | 143.7 | 16.0 | — |
| 2017 | 766.1 | 578.8 | **75.6** | 258.9 | **33.8** | 176.7 | 17.2 | — |
| 2018 | 806.3 | 600.3 | **74.5** | 221.1 | **27.4** | 219.3 | 19.7 | — |
| 2019 | 725.6 | 535.9 | **73.9** | 142.6 | **19.7** | 203.9 | 16.4 | 320 |
| 2020 | 811.0 | 604.6 | **74.6** | 170.5 | **21.0** | 176.2 | 13.5 | 395 |
| 2021 | **1,037.1** | 759.8 | **73.3** | **315.1** | **30.4** | 279.9 | 20.8 | **460** |
| 2022 | 1,006.1 | 721.9 | **71.8** | 246.2 | **24.5** | 215.5 | 15.0 | 412 |
| 2023 | 837.5 | 601.2 | **71.8** | 130.7 | **15.6** | 113.2 | **7.7** | 280 |
| 2024 | 914.5 | 625.8 | **68.4** | 115.1 | **12.6** | 106.2 | **7.0** | 314 |
| 2025 | 994.4 | 665.4 | **66.9** | 162.6 | **16.4** | 114.4 | **7.6** | 362 |
| **H1 2026** | 559.7 | 396.7 | **70.9** | 145.4 | **26.0** | 124.5 | — | — |
| **TTM to 2026-07-05** | **1,088.9** | 749.9 | **68.9** | **238.4** | **21.9** | — | — | — |

*(ROE on average equity, from the filed balance sheets. H1 2026 and the TTM column come from
the 10-Q, accession 0000851205-26-000065.)*

**1. The nine-year flags have the DIRECTION right and the OBJECT wrong.** `level_shift 0.68`
and `level_shift_oe 0.53` are comparing 2021-2022 to 2023-2024. Both of those are real halves
of a real cycle. What the ratio cannot see is that the 2023-24 trough had already begun
reversing before the flag was struck.

**2. The eighteen-year reading of 1.05 is the more nearly correct one, and here is why.** This
business has always done this. Revenue fell **28% in 2009**, **10% in 2019** and **17% in
2023**; operating margin has printed 33.8%, 19.7%, 30.4%, 12.6% and 16.4% inside nine years.
**[E3-55]** is exactly on point: *"If we have a business about which we're extremely confident
as to the business result, we would prefer that it have high volatility than low volatility."*
Volatility with a known mechanism is not a step. Cognex's revenue is somebody else's capital
budget landing on a cost base that is mostly people, and that arithmetic produces this series
mechanically.

**3. But there IS a step, and it is not in the volume — it is in the MARGIN.** Decompose the
2021-to-2025 fall in operating income, $315.1M to $162.6M, into its three filed causes:

| cause | effect on operating income |
|---|---|
| lower revenue, at 2021 gross margin | **−$31.3M** (21%) |
| **lower gross margin, on 2025 revenue** | **−$63.1M** (41%) |
| higher operating expense | **−$58.0M** (38%) |
| **total** | **−$152.4M** (filed change: −$152.5M) |

**The single largest cause is the gross margin, not the volume.** Revenue is within 4% of its
2021 record. Gross margin is 6.4 points below it, and 8.7 points below the 2017 high.

**4. And the revenue is not what it looks like, because part of it was bought.** The FY2024
10-K quantifies it and the FY2025 10-K does not:

> *"Revenue from the acquisition of Moritex that closed in the fourth quarter of 2023
> represented **approximately 8% of total revenue in 2024 and 1% of total revenue in 2023**.
> **Excluding the contribution of Moritex, revenue increased by 1% in 2024** over the prior
> year."*

Moritex cost **$296.1M** (Note 21, FY2025 10-K) against an **enterprise value of ~$270M**. Eight
percent of 2024 revenue is **$73.2M, and that figure covers THIRTEEN months**, because the
FY2025 MD&A discloses *"recording an additional month of Moritex revenue in 2024 to eliminate
the one-month lag."* Twelve months is therefore **about $67.5M**. Carrying that forward and
removing the **$13M of one-time revenue from the medical-lab channel partnership** the FY2025
MD&A discloses:

> **Organic 2025 revenue is roughly $906M to $916M, against a 2021 peak of $1,037M — down 11%
> to 13% over four years.** *(Derivation shown; the FY2025 10-K does not publish it. The $67.5M
> Moritex carry-forward is MY arithmetic on the FY2024 disclosure, labelled as such.)*

**5. THE ADJUDICATION.** *The step down is REAL, it is in the MARGIN and not in the volume, and
it is PART permanent and PART cyclical. Naming which part is which is the whole job:*

**PERMANENT, on filed evidence:**
- **Mix.** Logistics is Cognex's largest and fastest-growing end market and its own MD&A has
  said since 2021 that logistics *"has relatively lower gross margins."* Moritex optical
  components are lower-margin again — the FY2024 MD&A names *"products with relatively lower
  gross margins from the Moritex acquisition"* and *"the amortization of Moritex acquired
  technologies"* as causes. Both mix shifts are structural, not cyclical.
- **Price.** FY2024 MD&A, in the company's own words: *"**Lower average selling prices due to
  pricing pressures** also contributed to the lower margin in 2024."*
- **The acquired-intangible amortization** ($11.4M and $10.5M in 2024 and 2025 against $3.3M in
  2022) runs for nine to fifteen years on the schedule in Note 21.

**CYCLICAL, on filed evidence:**
- Automotive, about 22% of 2024 revenue, is in a trough the filing names: *"significant
  headwinds in 2025, driven in part by geopolitical and trade uncertainty."*
- The 2023 trough cash flow was worsened by working-capital reversals (accrued expenses
  −$35.3M, accrued income taxes −$16.7M, inventories −$22.6M) that are timing, not earnings.
- **The peer row settles it: EVERY machine-vision peer prints the same shape.** Omron's
  Industrial Automation segment ran 17-18% margins in FY2021-22, **collapsed to 5.4% in FY2023**
  and has recovered only to 10.4%. Basler's EBIT margin went **+13.2% (2021) to −10.8% (2023) to
  +7.9% (2025)** and its gross margin fell 10 points and took back 5. **This was an industry
  event, not a Cognex event.**
- **And H1 2026 reversed a large part of it**: gross margin **back to 71%**, operating margin
  **26%**, revenue **+20%**.

**THE VERDICT ON THE STEP: the owner-earnings step down was CYCLICAL and has substantially
reversed; the gross-margin step is PARTLY PERMANENT and has NOT fully reversed.** Even at H1
2026's recovered 71%, gross margin is **3.5 points below** the 74.5% of 2018 and 2020, and the
10-Q attributes the recovery to *"more favorable end-market mix and higher sales volume, which
improved fixed-cost absorption"* — **to volume and mix, not to price.** A margin that moves with
absorption and mix and not with price is a margin the owner does not control.

**Therefore [E4-41] does NOT apply in its usual direction here.** The corpus's normalization
rule strips *favourable* exogenous breaks out of the mean. Cognex's window contains an
*unfavourable* break (an industry-wide capex trough) and a *favourable* one (the 2020-21
e-commerce warehouse boom, which the 10-K itself describes: *"leading e-commerce customers
invested significantly into floor space capacity in late 2020 through early 2022, then took a
post-pandemic 'time out' to absorb excess capacity"*). **Both must come out. They roughly
cancel, which is why the eighteen-year reading is the honest one and neither nine-year window
is.**

### [E3-03] — the three criteria, against the company's own words

**(1) Needed or desired — YES.** Nothing in the file argues otherwise. Automated inspection and
identification are not discretionary once a line is designed around them.

**(2) "Thought by its customers to have no close substitute" — NO, and Cognex has said so in
every vintage read.** The FY2025 Item 1 Competition section, in its entirety:

> *"Cognex is one of the leading machine vision companies in the world. Our competitors include
> other vendors of machine vision systems, controllers, and components; manufacturers of image
> processing systems, sensors, and components; and system integrators. **We also compete with
> internal engineering departments of current or prospective customers, as well as open-source
> tools available from various companies, including tools using AI.**"*

Three sentences, no company named. But the FY2019 vintage named them:

> *"**Key competitors in geographies worldwide include Keyence Corporation, Sick AG, Datalogic,
> and Omron Corporation.**"* — 10-K FY2019, Item 1, Competition (accession 0000851205-20-000002)

**And that list is independently corroborated by a third party's filing.** Zebra Technologies,
FY2025 10-K (accession 0001628280-26-007668), Item 1, Competition:

> *"**Competitors in our fixed industrial scanning and machine vision business include Cognex,
> Keyence, and SICK.**"*

So the substitutes are named, from both sides, in SEC filings. They are: **four named industrial
rivals, a fifth (Zebra) that bought its way in for $881M in 2022, low-cost Chinese entrants, the
customer's own engineering department, and free open-source software.** Seven classes of
substitute. **Criterion (2) fails, and it fails on the filer's own disclosure, not on my
inference.**

**(3) Not subject to price regulation — YES.** No regulator sets Cognex's prices. No franchise
credit is taken for this; **[E2-59]** governs, and regulation *caps* a franchise rather than
creating one.

### THE PASS-THROUGH TEST — the instrument the brief named, and COGNEX FAILS IT

The brief called this the ACLS/PLPC test: did the company hold price while volume fell? PLPC
passed it, taking back **6.1 points** of US-segment gross margin through its input-cost spike
and passing through **87%** of a 7.7-point tariff shock inside twelve months. **Cognex lost
ground at both ends of the same period.**

| episode | gross margin | what the filing says caused it |
|---|---|---|
| 2021 input-cost spike | **74.6 → 73.3** (−1.3) | *"higher prices paid to purchase inventories … a greater percentage of total revenue coming from the logistics industry, which has relatively lower gross margins"* (FY2021) |
| 2022, cost spike plus the fire | **73.3 → 71.8** (−1.5) | *"higher inventory costs … broker-buy purchases for components at higher-than-normal costs. A more favorable revenue mix and **the Company's price increases partially offset** this decrease"* (FY2022) |
| 2023-24, the volume collapse | **71.8 → 68.4** (−3.4) | *"a less favorable revenue mix … as well as the amortization of Moritex acquired technologies. **Lower average selling prices due to pricing pressures** also contributed"* (FY2024) |
| 2025, tariffs | **68.4 → 66.9** (−1.5) | *"a $13 million charge … for excess and obsolete inventory … Less favorable industry mix and **the impact from tariffs** also contributed"* (FY2025) |

**Four consecutive episodes, four consecutive margin losses, and in exactly one of them does the
filing report a price increase — and there it only *"partially offset"* the cost.** PLPC ended
its cost shock **above** where it started. Cognex ended four years **7.6 points below**.

**[E4-37]'s inverse metric is decisive here:** *"you can almost measure the strength of a
business over time by the agony they go through in determining whether a price increase can be
sustained … it's not a great business when you have to have a prayer session before you raise
your prices a penny."* Cognex's filings never once report a price increase taken and held into a
year of flat or falling volume. What they report instead, in the same paragraph as the margin,
is *"pricing pressures"*, *"price erosion"* and *"reduced pricing power."* **That is the
prayer-session end of the metric.**

### [E2-44] — the two-characteristic test SPLITS, and the split is the whole company

**Half one — can it raise prices *"even when product demand is flat and capacity is not fully
utilized"*? NO.** 2023 and 2024 are exactly that condition, and the filed answer is lower
average selling prices. **This half fails.**

**Half two — can it grow dollar volume *"with only minor additional investment of capital"*?
YES, spectacularly, and this is the best fact in the file.** Capital expenditure was **$8.7M on
$994M of revenue in 2025 — 0.9%** — and **$4.3M in H1 2026 on $559.7M**. Net operating tangible
capital, computed from the FY2025 balance sheet (equity $1,491.9M less goodwill $386.3M less
intangibles $81.1M less the $642.3M cash-and-investment balance less the $383.3M deferred tax
asset plus the $250.5M deferred tax liability) is **about $249M**, and it earned **$162.6M of
operating income — a 65% pre-tax return on the capital actually employed in operations.**
**This half passes emphatically, and it is why the name deserved a full run rather than a
screen-out.**

### [E4-04] — must the moat be REBUILT, or merely DEFENDED?

This is where the file turns, and the company answers it itself:

> *"The market for our products is characterized by **rapidly changing technology** and
> increasingly capable competitors."* — 10-K FY2025, Item 1A

> *"Moreover, **new products, if introduced, may not generate the gross margins that we have
> experienced historically.**"* — same risk factor

**[E4-04]'s excluded class is the moat whose basis must be *periodically replaced*, not the moat
that needs continuous defence [E5-23].** The framework's test: *does a lapse in spending destroy
the structure, or merely narrow it — and does the spending defend the same advantage, or buy its
replacement?*

Cognex's $139M a year of RD&E **buys its replacement**, and the company describes the
replacement cycle in its own strategy section: rule-based vision tools, then *"nearly a decade"*
of deep learning, then edge learning, then in 2025 the **OneVision** cloud platform.
Coca-Cola's advertising defends the same trademark it defended in 1950; **Cognex's R&D buys a
new algorithm library every technology generation, and the old one becomes free.** That is
Mitsui's Rhodes Ridge, not Coca-Cola's advertising. **[E4-04] excludes it.**

### [E4-55] — WHERE ARE THE UNITS? THERE ARE NONE. SEVEN VINTAGES SEARCHED.

*"Dollar revenue flattered by pricing is how a shrinking franchise hides; the physical series is
the honest one."* All seven 10-Ks (FY2019 to FY2025) were searched for **units shipped, unit
volume, units sold, number of units, installed base, average selling price**.

**Result: ZERO hits, in every vintage, on every term except one.** The single exception is the
FY2024 MD&A sentence *"Lower average selling prices due to pricing pressures"* — a direction
with no number attached, appearing once and never repeated.

**Cognex files no unit count, no ASP series, no installed-base figure and no capacity figure.
The honest series does not exist.** It joins PLPC, KLAC and QLYS in that class.

**Two non-dollar series DO exist and both are worth having:**

| year-end | employees (Item 1) | revenue per employee ($k) |
|---|---|---|
| 2019 | 2,267 | 320 |
| 2020 | 2,055 | 395 |
| 2021 | 2,257 | **460** |
| 2022 | 2,441 | 412 |
| 2023 | **2,992** | 280 |
| 2024 | 2,914 | 314 |
| 2025 | 2,745 | 362 |

Headcount **peaked in 2023, the trough year** — the company hired into the top of the cycle and
has cut 8% since. Revenue per head is still **21% below the 2021 peak** four years later. This
is the closest thing to a physical series the filings offer, and it says the same thing the
margin does.

### THE DISCLOSURE TREND — four withdrawals over six vintages, all in one direction

This is a Q2 finding rather than a Q3 one because it bears on whether the moat can be
*measured*, and **[E2-49]** is explicit: *"Yardsticks seldom are discarded while yielding
favorable readings."*

| what was disclosed | last vintage carrying it | still there? |
|---|---|---|
| **Named competitors** (Keyence, Sick, Datalogic, Omron) | FY2019 | **no** |
| **Order backlog** ($74.9M at 2019-12-31 against $65.4M at 2018) | FY2019 | **no** |
| **"reliable estimates of the machine vision market … are not readily available"** | FY2022 | **no** |
| **Revenue % by end market** (logistics 23%, automotive 22%, consumer electronics 17%, semiconductor 11%) and **organic growth ex-Moritex** | FY2024 | **no** |

**The case AGAINST reading this as evasion, stated fairly [E4-51].** The first two dropped
together after FY2019, which is when the SEC's amendments to Regulation S-K Item 101 made
backlog and competitor disclosure principles-based rather than prescribed. That is a complete
and innocent explanation for two of the four, and I accept it for those two.

**It does not cover the fourth, and the fourth is the one that matters.** The FY2024 10-K told
its owners how much revenue was bought and how much was earned. The FY2025 10-K, covering the
first full year of owning Moritex, tells them neither. A reader of the FY2025 filing alone
**cannot compute organic growth**. Under **[E2-26]** — *"tell you the business facts that we
would want to know if our positions were reversed"* — an acquisition quantified separately in
year one and buried in year two does not pass.

**And a fifth item is a wording change rather than a deletion.** The FY2024 competition risk
factor read:

> *"In recent years, advancements in AI … **have lowered the barriers to entry in our market.**
> These tools **enable** new entrants and low-cost providers, **particularly in China**, to
> produce vision systems that **may perform comparably to our offerings.** **This
> commoditization trend intensifies pricing pressures** … This could result in decreased market
> share, **reduced pricing power**, and a material adverse effect on our revenue, gross margins,
> and operating results."*

The FY2025 version of the same paragraph:

> *"Advancements in the availability of sophisticated AI algorithms and open-source machine
> vision platforms **may lower barriers to enter our market in the future.** **A further
> fragmentation of the market could** intensify pricing pressures … This could result in
> decreased market share and have a material adverse effect on our revenue, gross margins, and
> operating results."*

**Six concrete things were deleted in one year:** *have lowered* became *may lower … in the
future*; *particularly in China* is gone; *may perform comparably to our offerings* is gone;
*commoditization trend* is gone; *further eroding market prices* is gone; *reduced pricing
power* is gone. **Every deletion softens, and the year in which they were deleted was a year in
which gross margin fell again, from 68% to 67%.** **[E2-69]** says to judge a disclosure
deviation by its **direction**, and this one runs away from candor. *(The fair counter-reading:
a new CEO arrived in June 2025 and the risk factors were plainly rewritten wholesale; by
February 2026 the business was reaccelerating and the FY2024 language may have looked
overstated. I record that reading and do not dismiss it. It does not change that the FY2024
sentence was the more useful one to an owner.)*

### THE COMPETITOR ROW — REQUIRED **[E3-28]**

*A moat is a claim about relative position and cannot be evidenced from one company's numbers.*
Same metric, same window, filing-sourced. Full working file with every source URL, accession
number and derivation: `Test Runs/_research 2026-09-07 CGNX/competitor-row.md`.

**Operating margin, fiscal years as each company reports them (%):**

| company | source class | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| **COGNEX** | SEC 10-K | 19.7 | 21.0 | **30.4** | 24.5 | 15.6 | **12.6** | 16.4 |
| **Keyence** | audited AR, JGAAP | **50.3** | **51.4** | **55.4** | **54.1** | **51.2** | **51.9** | **51.0** |
| **Zebra** (whole co.) | SEC 10-K | 15.4 | 14.6 | 17.4 | 9.2 | 10.5 | 14.9 | 13.0 |
| **Omron, IAB segment** | TDnet, US GAAP | 15.0 | 16.7 | 17.8 | 17.4 | **5.4** | 9.9 | 10.4 |
| **Basler AG** (EBIT) | audited AR, IFRS | 10.5 | 11.8 | 13.2 | 10.6 | **−10.8** | −5.3 | 7.9 |

**Gross margin, same window (%):**

| company | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | **change 2021 to 2025** |
|---|---|---|---|---|---|---|---|---|
| **COGNEX** | 73.9 | 74.6 | 73.3 | 71.8 | 71.8 | 68.4 | 66.9 | **−6.4** |
| **Keyence** | 81.8 | 81.9 | 82.3 | 81.8 | 83.0 | 83.8 | 83.0 | **+0.7** |
| **Zebra** | 46.8 | 45.0 | 46.7 | 45.4 | 46.3 | 48.4 | 48.1 | +1.4 |
| **Omron** (whole co.) | 44.8 | 45.5 | 45.5 | 45.0 | 42.3 | 44.5 | 45.7 | +0.2 |
| **Basler AG** | 50.6 | 52.0 | 52.4 | 48.4 | 42.2 | 45.1 | 47.4 | **−5.0** |

**R&D as % of revenue:** Cognex **13.1 to 16.6**; Keyence **2.35 to 2.99**; Zebra 9.9 to 11.3;
Basler 12.3 to 16.2 gross, of which Basler *capitalises* 25% to 53% and **Cognex capitalises
none**.

**Peers named: 5, against the 4 real competitors Cognex itself named, plus Zebra which entered
after Cognex stopped naming anyone.** Buffett says eight [E3-28]; this industry does not have
eight public pure-plays. Unavailable, with the obstacle named each time: **SICK AG (private,
German)**; **MVTec (private, German)**; **Hikvision / Hikrobot (Chinese, entity-listed, not
comparably audited)**; **Teledyne DALSA (inside Teledyne's Digital Imaging segment; machine
vision revenue UNAVAILABLE)**; **National Instruments (acquired by Emerson in October 2023, no
standalone reporting since)**; **Datalogic (Borsa Italiana filer, pull incomplete at the time of
writing)**. **Because named competitors are missing, the moat class would be PROVISIONAL if the
row were carrying the verdict. It is not: the verdict below rests on Cognex's own filings and
the row corroborates rather than decides.**

**Two caveats before the reading, because the row is not clean.** Keyence reports under Japanese
GAAP with a **March 20** year end and is a **single segment**, so its 51% is company-wide and
covers sensors, measuring instruments, laser markers and microscopes as well as vision — **nobody
outside Keyence knows its machine-vision margin.** Zebra's segment operating income excludes
share-based compensation and intangible amortization; Cognex's does not, so Zebra's segment
figures are not comparable and only its consolidated line is used above.

**WHAT THE ROW SAYS, in four findings.**

1. **Cognex's gross margin is the second-highest in the industry and that is a real fact in its
   favour.** Its **worst** gross margin ever (66.9%) is higher than Basler's best (52.4%),
   Zebra's best (48.4%) and Omron's best (45.5%). **[E2-58]'s commodity diagnosis does not fit a
   company earning 67% gross margins.** This is not a metal-basher.
2. **But Keyence earns 83% gross and 51% operating in overlapping products, and Cognex named it
   first among its rivals.** Keyence's own audited accounts describe *"imaging system
   equipment"* and *"code readers for logistics and retail"* — Cognex's two product lines.
   Keyence spends **2.8% of revenue on R&D against Cognex's 14%** and earns **three times the
   operating margin.**
3. **THE DECISIVE COMPARISON IS NOT THE LEVEL. IT IS WHAT EACH MARGIN DID THROUGH THE SAME
   CYCLE.** From 2021 to 2025, in one industry, through one downturn: **Keyence's gross margin
   rose 0.7 points and its operating margin fell 4.4 points from a 55% peak. Cognex's gross
   margin fell 6.4 points and its operating margin fell 14.0 points.** Basler, the other
   pure-play, fell with Cognex. **[E2-58]'s one exception to the commodity equation is *"a cost
   advantage that is both wide and sustainable … By definition such exceptions are few."* The
   row says that exception exists in this industry and that it belongs to Keyence, not to
   Cognex.**
4. **The row's own limit, stated [E3-61].** *"In some businesses, the participants behave like a
   demented Kellogg … I think you'd have to know the people involved."* The row shows position.
   It cannot show conduct, and I claim nothing about conduct from it.

### THE REMAINING Q2 TESTS, run and recorded

- **[E3-33] / [E5-28] untapped pricing power — NO, and the opposite is filed.** Claiming that
  class means claiming *"a monopoly or a near monopoly"* [E5-28]. Cognex told its owners for four
  vintages that it could not even size its own market: *"reliable estimates of the machine vision
  market and the number and relative size of competitors are not readily available."*
- **[E2-53] the dominance class — NO.** *"Once dominant, the newspaper itself, not the
  marketplace, determines just how good or how bad the paper will be."* A company whose margin is
  set by end-market mix and fixed-cost absorption, by its own MD&A's account in every year read,
  is having its economics set by the marketplace.
- **[E2-45] the attacker's test — and this is the sharpest single result in the file.** *"How I
  would like, assuming I had ample capital and skilled personnel, to compete with it."* **Two
  attacks are already running, both documented in filings.** Zebra took the capital route: it
  bought **Adaptive Vision (2021, $18M), Fetch Robotics (2021, $301M), Matrox Imaging (2022,
  $881M) and Photoneo (2025, $62M)** and now sells *"smart cameras, vision controllers, frame
  grabbers, input/output cards, and 3D sensors"* — Cognex's product list — into Cognex's largest
  end market. The low-cost entrants took the free route, and Cognex described it in its own
  FY2024 risk factor. **The attacker's test is not hypothetical here. It has been answered by the
  attackers.**
- **[E4-32] direction — NARROWING.** *"the moat widened every year"* is *"the primary criterion
  of a great business."* Every continuous filed instrument points the other way: gross margin
  −6.4 points since 2021, ASPs down by the company's own statement, ROE from 20.8% to 7.6%,
  revenue per employee −21%, a new well-capitalised entrant, and four disclosures withdrawn.
- **[E3-46] the second question is a number.** *"the best businesses … earn very high returns on
  capital employed over time."* **The answer depends entirely on the denominator, and both
  answers are true.** On book equity: **20.8% (2021) falling to 7.0-7.7% (2023-25)** — a
  three-year run below the corpus's own red-light level [E2-42]. On net operating tangible
  capital under **[E2-43]**'s unleveraged-net-tangible-assets rule: **about 65% pre-tax.** The
  gap is $642M of cash, $386M of goodwill and a $383M deferred tax asset sitting inside book
  equity. **The operating business is superb on capital. The corporate entity is not, because a
  third of its equity is parked in securities yielding less than the operating business earns.**
- **[E4-36] which of the four causes of extreme success?** Mostly **wave-riding [E3-51]**. The
  2017-2021 record was built on the e-commerce warehouse build-out, and the filing narrates the
  wave and its end in one sentence: *"leading e-commerce customers invested significantly into
  floor space capacity in late 2020 through early 2022, then took a post-pandemic 'time out' to
  absorb excess capacity."* *"When a surfer gets up and catches the wave … he can go a long, long
  time. But if he gets off the wave, he becomes mired in shallows."* Underneath the wave there is
  a genuine second cause — extreme performance on one variable, four decades of vision software —
  and that part is ownable. The wave part is not.
- **[E4-23] key-person check — no defect found**, but the risk factor is recorded here rather
  than at Q3, as the framework requires, so that a warning about the business cannot be read as a
  compliment to the person: *"With the appointment of our new Chief Executive Officer in June
  2025, we are transitioning to a different management style and strategic focus."*

### THE Q2 VERDICT

- **Class: NARROW.** · **Direction: NARROWING** — the first name in this reading order whose
  direction is negative on every continuous filed instrument at once.
- **VERDICT: [x] OUT — on [E3-03] criterion (2), on [E2-44] half one, and on [E4-04]'s
  replacement test; with [E4-32]'s direction and the competitor row corroborating.**

**THE CASE FOR IN, STATED AS WELL AS I CAN STATE IT [E4-51], because a bull should be able to
accept it as fair.**

> Cognex has earned a gross margin between **66.9% and 75.6% in every one of the last eighteen
> filed years**, including 2009, when revenue fell 28%. Its **worst** margin is above every
> peer's best except Keyence's. It earns roughly **65% pre-tax on the tangible capital actually
> employed in operations**, needs **0.9% of revenue** in capital expenditure to run, carries **no
> debt at all** and **$755M of cash and investments**, and repurchased stock through the trough
> at an average of **$35.72 in 2025** against a $62.25 quote today. Free open-source computer
> vision has existed since 2000 and Cognex's gross margin was **75.6% in 2017**, seventeen years
> later — the "open source will commoditise it" argument has a twenty-five-year record of being
> wrong. Its switching cost is real and lives in the application engineering already installed on
> customers' floors. And **H1 2026 is a 20% revenue increase with gross margin back to 71% and
> operating margin at 26%**, which is not what a permanently impaired franchise looks like.
> **[E4-20]** would call this the *good* account at worst, and **[E4-43]** says the good class
> **passes**.

**Why it still does not carry the gate — five reasons, each tied to a filed fact.**

1. **Criterion (2) asks what customers think, and the only filed answers are Cognex's own and
   Zebra's, and both name substitutes.** Four rivals in FY2019, Cognex named by Zebra in FY2025,
   plus the customer's own engineering department and *"open-source tools available for free …
   including tools using AI"* in every vintage. **A product thought to have no close substitute
   does not have seven classes of substitute listed in its own Item 1.**
2. **[E2-44] half one fails outright, in the company's words, in the exact condition the corpus
   specifies.** 2023 and 2024 were flat-to-falling demand with capacity not fully utilised, and
   the filed result was *"lower average selling prices due to pricing pressures."* [E4-37]'s
   inverse metric fires in four consecutive vintages.
3. **The pass-through test — the one PLPC passed — Cognex fails at four consecutive attempts.**
   Four cost or mix shocks, four margin losses, one partial price offset. That is the cleanest
   discriminator in this file, because it is the same test run on the same instrument on a
   comparable company in the same reading order.
4. **[E4-04] excludes a moat whose basis must be periodically replaced, and Cognex's own strategy
   section describes the replacement schedule** — rule-based, then deep learning, then edge
   learning, then OneVision — while the filing calls its market *"characterized by rapidly
   changing technology"* and warns that *"new products … may not generate the gross margins that
   we have experienced historically."* $139M a year buys the next library. It does not defend the
   last one.
5. **The competitor row makes the position relative, and relatively the wide-and-sustainable
   advantage in this industry sits at Keyence.** Same cycle, same customers, overlapping
   products: Keyence's gross margin **rose**; Cognex's fell 6.4 points. **[E2-58]'s exception
   exists here and it is not Cognex's.**

**WHAT WOULD FLIP THIS VERDICT, NAMED IN ADVANCE SO IT IS FALSIFIABLE.** Any one of:
**(a)** consolidated **gross margin at or above 72% for four consecutive quarters** with the MD&A
attributing it to price or product rather than to volume absorption or mix — that is [E2-44]
half one becoming answerable in the affirmative; **(b)** a **filed unit, ASP or installed-base
series** in any vintage, making [E4-55] runnable; **(c)** a disclosed **list-price increase taken
and held into a year of flat or falling volume**; **(d)** **operating margin at or above 25% for
three consecutive years**, which would mean the 2017-21 economics were the level and not the
wave; or **(e)** Cognex resuming the **named-competitor and organic-growth disclosures** it
withdrew, which would restore the ability to measure the moat at all. **Each is a document I can
name, which is why this is OUT and not UNRESEARCHED: every document that exists has been read,
and they answer the question as it stands.**

**Q2 CLOSES THE FILE. Everything below this line is recorded because the operator's brief asked
for it and because a closed file still owes the register its findings. None of it is a verdict,
and per operator rule 2 none of it can promote the name.**

---

## ADDENDUM TO Q2 — EVIDENCE OBTAINED AFTER THE VERDICT WAS WRITTEN
### Corrected in an addendum, never by editing what was written (operator rule 6)

The competitor row named a resolving document I had not read: **the earnings releases furnished
as Exhibit 99.1 to the Form 8-Ks**, which carry a gross-margin series the 10-Ks do not. I
fetched them. **Three things in them cut against the Q2 verdict and one cuts sharply for it,
and all four are recorded here rather than folded silently into the section above.**

**Documents added:** 8-K EX-99.1, FY2024 results, accession **0000851205-25-000010** (furnished
2025-02-12) · 8-K EX-99.1, FY2025 results, accession **0000851205-26-000009** (furnished
2026-02-11) · 8-K EX-99.1, Q2 2026 results, accession **0000851205-26-000061** (furnished
2026-08-05).

### CORRECTION 1 — the durable margin step is about 3 points, not 7.6

Cognex publishes an **adjusted gross margin** that removes acquired-intangible amortization,
reorganization and acquisition charges, and one-time items. It is the company's number and not
mine, and **[E4-29] and [E5-41] are the reason I do not adopt it** — the Moritex amortization it
removes is money already spent, the *"reverse float"* whose deletion the corpus calls nonsense.
But it is the right instrument for separating **mix and price** from **purchase accounting**,
which is what the step-down question actually asks. Filed series:

| period | **GAAP gross margin** | **adjusted gross margin (company's)** |
|---|---|---|
| FY2023 | 71.8% | **72.5%** |
| FY2024 | 68.4% | **69.3%** |
| FY2025 | 66.9% | **68.9%** |
| Q4 2025 | 65.7% | **71.6%** |
| Q2 2026 | 70.6% | **71.5%** |
| **H1 2026** | 70.9% | **71.7%** |

**On the company's own adjusted basis the decline was 3.2 points (2023 to 2024), then 0.4 points
(2024 to 2025), and H1 2026 has taken back 2.8 of it.** The 7.6-point GAAP figure used in the
section above is a peak-to-trough measurement that mixes in the Moritex purchase accounting and
the $13M Q4-2025 inventory write-down. **The correct statement of the durable step is roughly
three points against the 2018-2020 level, not seven and a half.** Q2's arithmetic overstated
it, and this addendum says so.

### CORRECTION 2 — the company ranks price as the SMALLEST of the three causes

I quoted the FY2024 10-K sentence *"Lower average selling prices due to pricing pressures also
contributed"* and let it carry weight it was not given by its author. The earnings release says
it in a ranked form I should have had:

> *"Adjusted gross margin of 69.3% declined from 72.5% in 2023. The year-on-year decline was
> due to **the addition of Moritex, unfavorable revenue mix, and, to a lesser extent,
> pricing.**"* — FY2024 release, accession 0000851205-25-000010

**Moritex first, mix second, price third and explicitly lesser.** That is the company's ordering
and it is fair to it. **What it does not change is the direction:** the test at **[E2-44]** half
one is whether price can be *raised* when demand is flat and capacity is not full, and in
2023-24 the filed answer is that price *fell*, by however little. And the recovery is attributed
to the same two non-price causes throughout: *"favorable mix and volume"* (Q2 2026 release),
*"volume and favorable mix slightly offset by tariffs"* (Q4 2025 release). **Across five filed
periods, every gross-margin movement Cognex explains is explained by mix, volume, purchase
accounting or tariffs — and the only time price is named, it is named as a subtraction.**

### CORRECTION 3 — a bound on how much of the fall mix could explain

Arithmetic, labelled as arithmetic: gross margin fell 3.4 GAAP points in 2024, the year Moritex
went from 1% to 8% of revenue. If the whole fall were Moritex mix and the rest of the business
had held 71.8%, Moritex's own gross margin would have to be about **29%**
(0.92 × 71.8 + 0.08 × x = 68.4). **Cognex does not disclose Moritex's gross margin, so 29% is
not a finding about Moritex** — it is the answer to *how low would Moritex have to be for mix
alone to explain everything*, and 29% is implausibly low for an optical-components maker. **Mix
alone does not explain it, which is consistent with the company's own three-cause sentence.**
The sub-question *"how much of the step is price"* remains **UNRESEARCHED and resolvable**: the
document that would settle it is a Moritex standalone gross margin or an ex-Moritex gross-margin
series, and neither exists in any filing read. **It is not load-bearing for the verdict**, which
rests on [E3-03](2) and [E4-04], not on the size of the price effect.

### THE EVIDENCE THAT CUTS FOR THE VERDICT — and it is the sharpest Q3 item in the file

**The furnished releases lead on Adjusted EBITDA, and the company's stated corporate objective
is an Adjusted EBITDA margin.** From the FY2025 release, the CFO, verbatim:

> *"Adjusted EBITDA margin, excluding the one-time Commercial Partnership benefit, expanded 360
> basis points year over year to 20.7%. **We surpassed our first execution milestone of 20% a
> full year ahead of plan** driven by focused execution and strong cost discipline. Building on
> the actions we've already completed, **our next milestone is a 25% Adjusted EBITDA margin —
> targeted on a run-rate basis by the end of 2026** — as we focus on creating long-term value for
> shareholders through sustainable margin expansion."*

And the Q2 2026 release headline: *"Operating margin was 29.4%; **delivered an Adjusted EBITDA
margin of 32.2%**, up 1,150 basis points year over year, marking the eighth consecutive quarter
of margin expansion."*

**[E4-29] is the fifth flag and it fires at full strength here:** *"Trumpeting EBITDA … is a
particularly pernicious practice. Doing so implies that depreciation is not truly an expense,
given that it is a 'non-cash' charge. **That's nonsense.**"* Twelve-plus corpus restatements,
ending at *"a banned measurement."* Cognex's FY2025 GAAP operating margin was **16.3%** and its
Adjusted EBITDA margin was **21.5%** — a **5.2-point** headline gap, bought with $30.8M of D&A
and the acquisition and reorganization charges. **[E5-41]** names precisely what that deletes:
*"Depreciation is where you spend the money first … and record the expense later. And it's
reverse float"* — the worst kind of expense, already paid, is exactly the one the milestone
metric removes. **This is recorded at Q2's addendum because I wrote "EBITDA promotion: no" from
the 10-K alone, and the 10-K alone was the wrong document.** The word EBITDA does not appear in
the FY2025 10-K. It appears in the headline of every earnings release the company furnishes.

### THE ROW, COMPLETED — Datalogic added

| company | GM 2022 | GM 2023 | GM 2024 | GM 2025 | **change** | EBIT/OM 2021 | 2023 | 2025 |
|---|---|---|---|---|---|---|---|---|
| **COGNEX** | 71.8 | 71.8 | 68.4 | **66.9** | **−4.9** | 30.4 | 15.6 | 16.4 |
| **Keyence** | 81.8 | 83.0 | 83.8 | 83.0 | **+1.2** | 55.4 | 51.2 | 51.0 |
| **Zebra** | 45.4 | 46.3 | 48.4 | 48.1 | +2.7 | 17.4 | 10.5 | 13.0 |
| **Omron** | 45.0 | 42.3 | 44.5 | 45.7 | +0.7 | 11.7 | 4.2 | 7.8 |
| **Basler AG** | 48.4 | 42.2 | 45.1 | 47.4 | −1.0 | 13.2 | −10.8 | 7.9 |
| **Datalogic** | 40.1 | 40.6 | 42.1 | 42.8 | **+0.9** | 7.9 | 1.2 | 2.0 |

**Six peers now, and the finding sharpens rather than softens: over 2022-2025 Cognex is the
ONLY company in its own peer row whose gross margin fell.** Four rose; Basler fell 1.0 after a
6.2-point collapse it largely won back. Cognex fell 4.9 and, on the company's own adjusted
basis, has won back most of it only in the two most recent quarters.

**And the row gained the single most useful analogue in the file: National Instruments.** Before
Emerson bought it in October 2023, NI ran a **~70% gross margin, ~20% of sales on R&D and a
single-digit-to-low-teens operating margin, because selling and marketing consumed 29% to 35%
of sales.** **NI is the proof that a 70% gross margin does not by itself produce a Keyence
operating margin — the difference is the cost of going to market.** Cognex's SG&A was **37% of
revenue in 2025** against Keyence's 29.3%. That is the mechanism behind the 35-point operating
margin gap, and it is a structural feature of Cognex's model, not a cyclical one.

**Naming correction:** Cognex named its competitors in the **FY2017, FY2018 and FY2019** 10-Ks,
not FY2019 alone. The list was dropped in FY2020. The point is unchanged and slightly stronger:
three consecutive vintages named Keyence, then none did.

### THE VERDICT AFTER THE ADDENDUM

**UNCHANGED: Q2 remains OUT**, and here is why the corrections do not move it. They correct the
*size* of the margin step, which was a supporting fact. **They do not touch either load-bearing
finding.** [E3-03](2) fails because Cognex's own Item 1 and Zebra's own Item 1 between them name
seven classes of substitute including free ones — the adjusted-margin series says nothing about
that. [E4-04] excludes it because the moat's basis must be replaced each technology generation —
and a company whose gross margin recovers on *"favorable mix and volume"* has demonstrated
operating leverage, which is not the same thing as a moat.

**But the corrections do change how close the call is, and the honest record is that it is
closer than the section above reads.** The strongest single fact against my conclusion is now
stronger than when I wrote it: **eight consecutive quarters of margin expansion, an adjusted
gross margin of 71.7% in H1 2026, a 29.4% GAAP operating margin in Q2 2026, and company guidance
beaten at or above the top of the range in the periods checked [E3-48].** A reader who weighted
the recovery more heavily than [E3-03](2) would reach IN NARROW on this evidence, and that
reading is defensible. I have not taken it because **[E3-03]'s second criterion is not a
question about margins, and it is answered in the filings by the filer.**

---

# TESTS RUN BELOW THE CLOSED GATE — RECORDED, NOT VERDICTS

Q2 returned OUT. Per operator rule 2 the file is closed and **nothing below promotes the name.**
It is written because the operator's brief commissioned specific work, because a closed file
still owes the register its findings, and because two of the items below are **defects in the
tooling that will affect other runs.**

## A. OWNER EARNINGS — THE MULTI-WINDOW REBUILD THE BRIEF DEMANDED
### **COMPUTATION — NOT A CLEARANCE**

**The convention** (framework, section VI): owner earnings = operating cash flow less
share-based compensation less the (c) guess. **(c) is a disclosed judgment [E2-23]**, and the
corpus's default is D&A **[E3-44, E2-41]**.

**Which (c) case is this, and it is the UNUSUAL one.** The exception class at **[E5-20]** —
railroads, airlines, anything whose own filing says depreciation understates renewal — makes
the **D&A end INVALID** and forces (c) up toward total capex. **Cognex is the mirror image.**
It outsources manufacturing; capex has run **0.9% of revenue** and has been **below D&A in
seven of the last nine years**. So here the D&A end is the CONSERVATIVE end and the capex end
is the optimistic one, and **both are legitimate** — neither is invalid. *(Judgment disclosed:
I have used total D&A including acquired-intangible amortization at the conservative end.
Excluding the Moritex intangibles would raise the conservative end by about $10M a year. I kept
them in because the amortization is a real charge for a real cash outlay of $296M, and leaving
it out would let an acquisition improve owner earnings by construction.)*

**Owner earnings by year, both (c) ends ($M):**

| year | OCF − SBC | **(c) = D&A** | **(c) = capex** |
|---|---|---|---|
| 2017 | 192.4 | 175.4 | 163.6 |
| 2018 | 182.4 | 160.9 | 145.3 |
| 2019 | 207.7 | 182.8 | 186.0 |
| 2020 | 199.7 | 173.2 | 186.4 |
| 2021 | 270.3 | **250.0** | **254.8** |
| 2022 | 188.9 | 169.3 | 169.2 |
| 2023 | 58.1 | **36.3** | **35.1** |
| 2024 | 96.6 | 63.9 | 81.6 |
| 2025 | 197.0 | 166.2 | 188.3 |

**EIGHT WINDOWS x TWO (c) ENDS = SIXTEEN CONSTRUCTIONS. The brief's mandatory correction #1 is
confirmed and it is the twelfth consecutive run to confirm it.**

| window | n | **mean OE, (c)=D&A** | **mean OE, (c)=capex** | yield at $10,472M cap |
|---|---|---|---|---|
| 2024-2025 | 2 | 115.1 | 134.9 | 1.10% – 1.29% |
| **2023-2025** | 3 | **88.8** | 101.6 | **0.85%** – 0.97% |
| 2022-2025 | 4 | 108.9 | 118.5 | 1.04% – 1.13% |
| **2021-2025** *(corpus default [E2-42])* | **5** | **137.1** | **145.8** | 1.31% – 1.39% |
| 2020-2025 | 6 | 143.2 | 152.6 | 1.37% – 1.46% |
| 2019-2025 | 7 | 148.8 | **157.3** | 1.42% – **1.50%** |
| 2018-2025 | 8 | 150.3 | 155.8 | 1.44% – 1.49% |
| 2017-2025 | 9 | 153.1 | 156.7 | 1.46% – 1.50% |
| *TTM to 2026-07-05* | *1* | *196.4* | *218.9* | *1.88% – 2.09%* |

- **Short-window mean** (3-year, 2023-2025): **$88.8M to $101.6M**
- **Long-window mean** (9-year, 2017-2025): **$153.1M to $156.7M**
- **Spread, conservative end:** (153.1 − 88.8) / 88.8 = **+72.4%**
- **COMBINED RANGE across all sixteen constructions: $88.8M to $157.3M — a width of 77.2%.**

**THE PUBLISHED SPREAD OF 49.3% IS TOO NARROW BY HALF AGAIN.** The queue's figure came from
four constructions (two windows x two (c) ends) computed on a D&A series that was missing the
intangible amortization. The true width over eight windows and both ends, on hand-rebuilt
filed figures, is **77.2%**. *(Not as extreme as LRCX's 87.0% against a published 20.9%, but
in the same direction, for the same reason, and this makes twelve.)*

**Is the range too wide to reach a conclusion [E4-25]?** On the level, no: the whole range is
below 2% against a 5.24% sovereign, so the price fails at every point in it and the width does
not change that answer. On the *business*, the width is itself the finding **[E5-11]** — a
2.8x spread between the best year ($250.0M, 2021) and the worst ($35.1M, 2023) inside five
years is what a business looks like when its revenue is another industry's capital budget and
its cost base is people. **[E3-55]** says volatility with a certain endgame is not a defect;
Q2 found the endgame is not certain, so here the width counts against.

**The distorted years, named [E5-11]:** **2021** is the top of the e-commerce warehouse boom
the 10-K itself narrates, and **2023** carries the destocking trough *plus* $75M of adverse
working-capital reversals *plus* the $257M Moritex cash outflow's first partial year. **2020**
also carries a $19.6M intangible impairment and a $390.5M dividend payment (a special
distribution), neither of which recurs. **[E4-41]** requires favourable breaks out before the
mean is trusted; as Q2 found, this window contains one favourable and one unfavourable break
and they roughly cancel.

**Stock compensation, subtracted in full [E5-06], and the brief was right to ask.** SBC was
**$48.5M in 2025** and has run **$43.8M to $54.8M every year since 2021 — while owner earnings
fell to $36M.** As a share of the owner-earnings mean:

| window | SBC / owner earnings |
|---|---|
| 3-year, conservative end | **55%** |
| 9-year, optimistic end | **31%** |
| TTM, optimistic end | **22%** |

**At the conservative end the company pays its employees more in stock than it earns for its
owners.** And **[E3-70]** says the reported charge is only the **floor** of the subtraction —
the measure is *"what the company could have realized by publicly selling options of like
quantity and structure."* The subtraction above is therefore understated by an unknown amount,
in the owner's disfavour. **SBC is material on a shrunken base. That is a confirmed answer to
the brief's question, and the answer is yes.**

## B. Q3 ITEMS — NO VERDICT IS WRITTEN; THE GATE IS CLOSED

**THE WEIGHT CASE, DECLARED [E3-38, E3-43, E1-16, E3-29].**
- Daily execution — **YES.** [E3-43]'s original wording is the operative one: *"franchises can
  tolerate mis-management … **a business, unlike a franchise, can be killed by poor
  management**."* Q2 found this is not a franchise. A machine-vision company must win a
  read-rate bake-off this quarter and land the next technology generation over three years;
  there is no specification lock-in that runs without being re-earned.
- Control — no. Leverage — no; there is **zero debt.**
- **One ticked, therefore Q3 would be a BINARY GATE and no price would compensate.** Recorded
  for completeness. The gate above is already closed.

**HONESTY — no disqualifier found, and that is not a finding that they are honest [E5-17].**
Grant Thornton LLP, auditor **since 2007**, unqualified opinion, ICFR audited and **effective**
at 2025-12-31 with no material weakness and no change in Q4. Item 3 Legal Proceedings carries
only *"claims and legal proceedings generally incidental to the normal course of business."*
No restatement found in nine years of overlapping cash-flow statements. No related-party
matter beyond three directors whose companies do arm's-length business with Cognex in amounts
the proxy calls immaterial.

**THE FLAGS [E4-22, E5-15, E4-29, E4-30] — each a prompt to read, never a verdict.**

| flag | fires? | what the filing says |
|---|---|---|
| weak accounting | **no** | SBC fully expensed; **no development costs capitalised** (Basler capitalises 25-53% of R&D; Cognex none); no pension assumptions |
| unintelligible footnotes | **no** | 23 notes, plain, one segment |
| trumpeted projections / targets | **YES, and not mildly** | quarterly AND full-year guidance on revenue, **Adjusted EBITDA margin** and adjusted diluted EPS, in every furnished release; plus *"our next milestone is a 25% Adjusted EBITDA margin — targeted on a run-rate basis by the end of 2026"*, *"we aim to double our customer base within five years"*, and *"an additional $35 to $40 million in annualized operating expense reductions by the end of 2026"* |
| serial share issuance | **YES, in substance** | see below |
| **EBITDA promotion [E4-29]** | **FIRES AT FULL STRENGTH — and I got this wrong from the 10-K alone** | see the Q2 addendum. The word EBITDA does not appear in the FY2025 10-K; **Adjusted EBITDA margin is the headline of every earnings release and the company's stated execution milestone.** FY2025 GAAP operating margin 16.3%, Adjusted EBITDA margin 21.5% — a 5.2-point gap bought with $30.8M of D&A. **[E5-41]**: *"Depreciation is where you spend the money first … it's reverse float"* |
| smooth reported growth [E4-30] | **no — the opposite** | operating margin printed 33.8, 19.7, 30.4, 12.6, 16.4 inside nine years. Nobody engineering earnings produces that series |
| cash tax % of pretax falling [E4-30] | **fires numerically, cause named** | 41.8% (2023) → 45.5% (2024) → **23.1% (2025)**. The FY2025 MD&A names the cause: OBBBA's immediate expensing of R&D, *"a full-year cash tax benefit estimated between $12 million and $15 million"*. A legislative change, not a cockroach |

**THE PROJECTIONS FLAG, WORKED AS [E3-48] REQUIRES — and the outturn is the candid direction.**
*"pull the company's own past guidance and set it against outturn."* Done, on the two periods
where guidance and result are both filed:

| guidance, and where it was given | outturn |
|---|---|
| Q1 2025: revenue **$200-220M**, adjusted EBITDA margin **12-15%** (FY2024 release, 2025-02-12) | revenue **$216M**, adjusted EBITDA margin **16.8%** — **above the top of the margin range by 180bp** |
| Q1 2026: revenue **$235-255M**, adj. EBITDA margin **19-22%**, adj. EPS **$0.22-0.26** (FY2025 release, 2026-02-11) | revenue **$268.4M** (from the Q2 10-Q's six-month total less Q2) — **above the top of the revenue range** |

**Cognex has beaten its own guidance, at or above the top of the range, in both periods
checked.** Under [E3-48] that is the direction that earns weight rather than losing it — a
company setting a bar it clears, not one *"tempted to make up the numbers."* **The flag that
survives is [E5-30]'s, and it is structural rather than about this year:** *"once you start it,
it's all over. You can't quit … And forecasting earnings, I can't imagine anything more
destructive."* **A guidance culture is a ratchet, and Cognex has now attached a multi-year
public milestone to a metric that deletes depreciation.** Both halves of that sentence are
findings, and the second is worse than the first.

**And the candid half of the "except-for" test [E2-57, E2-26]:** the $13M one-time Commercial
Partnership revenue is quantified separately, and the FY2025 release reports the Adjusted EBITDA
margin **both with and without it** (21.5% and 20.7%). A one-time item quantified separately at
every line passes [E2-26]; this one does.

**On the issuance flag, the substance rather than the label.** [E5-15] is aimed at
*"promotion-minded management"* raising capital; Cognex is not doing that. What it IS doing is
settling compensation in stock and buying the stock back with cash:

| period | shares repurchased | cash | **average price** | shares outstanding, end |
|---|---|---|---|---|
| 2023 | 1,723k | $79.8M | $46.31 | — |
| 2024 | 1,711k | $67.1M | $39.21 | 170,434k |
| 2025 | 4,234k | $151.2M | **$35.72** | 166,997k |
| H1 2026 | 2,501k | $105.2M | $42.08 | **168,224k** |

**In 2025 the company retired 4,234k shares and the count fell by only 3,437k. In H1 2026 it
retired 2,501k and the count ROSE by 1,227k — implying about 3.7 million shares issued to
employees in six months.** The FY2025 MD&A says this in its own words: the increase in
repurchases was *"to offset dilution from employee stock awards."* **A buyback that only
neutralises dilution is not a return of capital; it is the cash settlement of a compensation
expense**, and it belongs beside the $48.5M SBC charge rather than beside the dividend.

**THE PRIMARY TEST [E2-01] — a number, and the number has stepped down.**
*"The primary test of managerial economic performance is the achievement of a high earnings
rate on equity capital employed … and not the achievement of consistent gains in earnings per
share."* Return on average book equity: **16.0 · 17.2 · 19.7 · 16.4 · 13.5 · 20.8 · 15.0 ·
7.7 · 7.0 · 7.6** (2016-2025). **Three consecutive years at 7.0-7.7%.** **[E2-42]** sets the
comparison: *"Red lights should start flashing if the five-year average annual gain falls much
below the return on equity earned over the period by American industry in aggregate."* The
five-year average to 2025 is **11.6%**, and the last three years are half that.

**Scope it as [E2-43] scopes it, because the denominator changes the answer completely.** Book
equity of $1,491.9M contains $642.3M of cash and investments, $386.3M of goodwill, $81.1M of
intangibles and a $383.3M deferred tax asset. On **net operating tangible capital of about
$249M**, the same $162.6M of operating income is a **65% pre-tax return.** *Both numbers are
true and they answer different questions:* the operating business is excellent on capital; the
**corporate entity is not, because roughly 43% of its book equity is parked in securities
earning 2.6%** ($17.0M of investment income on $642M) while the operating business earns 65%.

**THE HALF-OWNER TEST [E2-26] — the one place Q3 has something real to say, and Q2 already
said it.** Four disclosures withdrawn in six vintages (named competitors, backlog, the
market-unsizeable admission, and the end-market and organic-growth split), plus the softening
of the AI risk factor. Two have an innocent regulatory explanation; **the Moritex one does
not.** A reader of the FY2025 10-K alone cannot compute organic growth in the first full year
of a $296M acquisition. Against *"tell you the business facts that we would want to know if our
positions were reversed"*, that is a miss.

**THE INSTITUTIONAL IMPERATIVE — score all four [E2-30].** *"Institutional dynamics, not
venality or stupidity."*

- [ ] **resists any change in current direction — NO, and emphatically so.** New CEO June 2025,
  a *"comprehensive strategic product portfolio review"*, a $13M write-off of legacy inventory,
  8% headcount reduction, $35-40M of announced opex cuts, and the divestiture of the Moritex
  Japan trading business on 2026-04-01. Whatever else is true, this management is changing
  direction.
- [x] **projects or acquisitions materialise to soak up available funds — FIRES.** $296.1M was
  paid for Moritex, which contributed about **$67M of annual revenue at a lower gross margin**
  and whose amortization now costs $10.5M a year; two and a half years later part of it was
  sold for **$10-12M** at a **$1.5M pre-tax loss**. The FY2025 strategy section then says:
  *"Potential transactions may include smaller acquisitions or **larger opportunities exceeding
  the size of our previous acquisitions**."* A company with $755M of idle cash announcing it
  may buy something bigger than the deal it is currently unwinding is the textbook shape of
  behaviour (2).
- [ ] staff studies produced to justify the leader's craving — not observable from filings.
- [ ] peer behaviour mindlessly imitated — not observable, though note that Zebra bought Matrox
  in 2022 and Cognex bought Moritex in 2023.

**THE RETENTION TEST [E3-54] — $1 of market value per $1 retained, and it fails badly.**
2021-2025: net income **$829.2M**, dividends **$245.2M**, **retained $584.0M**. Market
capitalisation went from **$13,866M** at 2020-12-31 to **$6,009M** at 2025-12-31 and is
**$10,472M** today. **Market value fell by more than three billion dollars while $584M was
retained.** The 10-K's own TSR table prints it: $100 invested at 12/2020 was worth **$46.23**
at 12/2025 against $187.14 for the NASDAQ Composite. **Carry the corpus's own 2009 correction
with this:** the test is violently sensitive to the starting multiple, and 2020-12-31 was near
a peak. It still fails on any starting point inside the window.

**BUYBACKS — the two conditions [E5-08], plus the third [E4-31].**
1. **Ample funds for operations and liquidity — PASSES, without argument.** $755.0M of cash and
   investments at 2026-07-05, **zero debt**, and inventory and lease commitments of $16.3M
   within twelve months.
2. **A material discount to conservatively calculated intrinsic value — FAILS ON MY NUMBERS,
   and the humility clause binds hard.** The 2025 repurchases averaged **$35.72**, against a
   zero-growth band of roughly **$13 to $28 per share** (section D). At $35.72 the company was
   paying 1.3x to 2.7x that band. **[E4-13]:** *"it is natural for CEOs to be optimistic about
   their own businesses. They also know a whole lot more about them than I do"* — and here the
   record supports them: they bought heaviest in 2025 at $35.72 and the quote is $62.25 today.
   **On timing they were right and I would have been wrong.** The flag is that a zero-growth
   value does not reach the price they paid, so the purchases embed the same growth assumption
   the quote does.
3. **[E4-31]'s third condition — *"Shareholders should have been supplied all the information
   they need for estimating that value"* — and this is where it bites.** The company withdrew
   the end-market and organic-growth split in the same filing year in which it quadrupled its
   repurchase. A buyback made against a register that has just been given **less** information
   with which to price the shares fails the earliest full statement of the rule, whatever the
   discount.

**THE GUARDRAIL [E2-37, E2-38, E3-39].** Nothing in this section is used to promote the name,
and there is nothing here that could: the manager findings are neutral-to-negative. Confirmed.

## C. Q4 ITEMS — RECORDED, NOT A VERDICT

**GREAT, GOOD, OR GRUESOME? [E4-20, E4-43] — GOOD, on a level that has been falling.**
Not gruesome: it does not require added capital at disappointing returns; capex is 0.9% of
revenue and the incremental capital requirement is near zero. Not *great* either, because
[E4-20]'s great account pays *"an extraordinarily high interest rate **that will rise as the
years pass**"* — and Cognex's rate has fallen, from a 30.4% operating margin and a 20.8% ROE in
2021 to 16.4% and 7.6% in 2025. **The level is great; the direction is not.** [E4-43] is
explicit that the *good* class passes Q4, and on Q4's own terms it does. Q4 is not where this
file closed.

**STAYING POWER — score all three [E5-11]. Two clean passes and one honest fail.**
1. **A large and reliable stream of earnings — LARGE, NOT RELIABLE.** Operating cash flow of
   **$314.1M (2021), $112.9M (2023), $245.5M (2025)** — a 2.8x range in four years.
2. **Massive liquid assets — PASSES, and this is the strongest fact in Q4.** $755.0M of cash
   and investments at 2026-07-05 against a $10.5bn market capitalisation; **7.2% of the market
   value is cash.**
3. **No significant near-term cash requirements — PASSES CLEANLY, and this is the one that
   usually kills [E5-11, E5-39].** **Zero long-term debt** (the 10-K says so in terms: *"the
   Company has no long-term debt"*). Inventory purchase commitments $66.8M, lease obligations
   $88.1M of which **$16.3M is payable within twelve months**. Nothing depends on the kindness
   of strangers. No bank lines are counted because none are needed.

**Leverage, named and quantified [E4-16, E3-29, E3-52].** Total liabilities $524.7M against
$2,016.6M of assets, and **$250.5M of that is a deferred income tax liability** — a
covenant-free, no-due-date liability of exactly the class [E3-52] distinguishes from
covenanted bank debt. Interest-bearing debt: **none.** [E2-54]'s coverage test does not bind
because there is no interest to cover.

**Foreign exposure [E3-66].** 67% of revenue is from customers outside the United States, and
the FY2025 non-operating line carries a **$4.1M foreign currency loss**. The company is a
Massachusetts corporation listed on NASDAQ, so its shareholders stand where US shareholders
stand; the jurisdiction question [E3-66] raises does not bite. Recorded rather than scored.

**NAME THE SPECIFIC WAY THIS BUSINESS DIES [E2-27, E3-24, E4-40].**

**The mechanism is NOT insolvency and it must be said plainly: with zero debt and $755M of
cash, Cognex cannot go broke.** What dies is the *investment*, not the company, and the
mechanism is **margin death with a fixed cost base**.

Machine vision has two cost curves. The hardware curve is somebody else's (image sensors,
processors) and it falls every year. The software curve was Cognex's private property for four
decades and is now partly public: the FY2024 10-K said, in the company's own words, that AI and
open-source platforms *"have lowered the barriers to entry in our market"* and that new entrants
*"produce vision systems that may perform comparably to our offerings."* If that is true, price
converges toward the hardware curve while Cognex's $503M of annual operating expense — a direct
salesforce and 575 engineers — does not.

**Quantified from filed figures, holding revenue at the FY2025 $994.4M and operating expense at
the FY2025 $502.8M, and moving only the gross margin:**

| gross margin | operating income | operating margin |
|---|---|---|
| **66.9%** (FY2025 actual) | $162.4M | 16.3% |
| 62% | $113.7M | 11.4% |
| 58% | $73.9M | 7.4% |
| 55% | $44.1M | 4.4% |
| **50%** | **−$5.6M** | **−0.6%** |

**The business reaches zero operating income at roughly a 50% gross margin.** That number is
not hypothetical: **Basler operates at 47.4%, Zebra at 48.1% and Omron at 45.7%.** The scenario
is not "something unprecedented happens"; it is "Cognex's gross margin converges on the rest of
the industry's." It has already travelled **7.6 of the 17 points** required, in five years.

**Likelihood: [x] a real possibility** over a decade; **a low-level possibility** over three
years, given that H1 2026 moved 4 points the other way.

**[E4-40] discipline — model exposure, not experience.** The benign reading is that Cognex has
been here before: free open-source computer vision has existed since 2000 and Cognex's gross
margin was **75.6% in 2017**. That is experience, and [E4-40] says experience late in a good
cycle is *"not only useless, but actually dangerous"* as a guide. **The exposure is that 100%
of revenue sits in one product class whose barrier to entry the company itself told the SEC
had been lowered**, and that the company deleted that sentence a year later.

## D. Q5 ITEMS — **COMPUTATION — NOT A CLEARANCE**

⛔ **Q5 did not open. Q2 returned OUT and per operator rule 2 that closes the file.** What
follows carries no entry language and is recorded because the brief asked for the band.

**THE PRICE:** **$62.25**, 2026-09-04 close, Yahoo Finance (aggregator, live quote only,
flagged). **Market capitalisation $10,472M** on 168,223,842 shares from the 10-Q cover.
**Sovereign: 5.24%, USD, US Treasury 30-year par yield curve, 2026-09-04.**

**1. THE YIELD.** Owner earnings **$88.8M to $157.3M** over sixteen constructions ÷ $10,472M =
**0.85% to 1.50%**, against a sovereign of **5.24%**. On the trailing twelve months to
2026-07-05 — the most favourable honest construction available, and the one a bull would
insist on — **$196.4M to $218.9M = 1.88% to 2.09%.**

**2. WHAT THE PRICE ALREADY ASSUMES.** Discounting at the bare sovereign with no risk premium
added **[E3-42]**, the perpetual growth in owner earnings required merely to **match** a 5.24%
government bond is **3.15% to 4.39% forever**. To reach the corpus's **~10% floor [E4-28]** it
is **7.91% to 9.15% forever.** *(The queue's `growth_required 9.03%` sits inside that band and
is confirmed.)* **[E4-35]** sets the base rate against which that must be judged: *"fewer than
10 of the 200 most profitable companies in 2000 will attain 15% annual growth in
earnings-per-share over the next 20 years."* Eight to nine percent forever is a lower bar than
fifteen, but it is a **perpetual** requirement placed on a business whose **organic revenue is
11-13% below its 2021 peak** and whose gross margin is 7.6 points below its 2020 high.

*What the business has actually done:* owner earnings averaged **$153-157M over nine years** and
**$89-102M over three**. Nine-year revenue compound growth is **2.9%** (766.1 → 994.4); the same
figure ex-Moritex is about **2.1%**.

**3. WHAT YOU ARE PAID.** **−4.39 to −3.15 points against the sovereign.** Every one of the
sixteen constructions, and the trailing-twelve-month construction on top, is **below the
government bond.**

**THE FLOOR, FIRST [E4-28].** Honest pre-tax expectancy at this price is the yield plus
growth. At the most favourable construction (TTM owner earnings, capex-end (c)) and a generous
**6%** perpetual growth assumption, expectancy is **8.1%**. At the conservative construction
and 6% growth it is **6.9%**. **Both are below the ~10% figure the corpus quits on, and the
floor does not move with the sovereign.** **THE NAME IS QUIT ON, NOT RANKED. No ranking
position is assigned.**

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01].** Method: capitalise owner earnings at the
sovereign with the **investment income stripped out** (it is portfolio income, not business
income) and **add the $755.0M cash-and-investment balance back at face**, so the cash is
counted once and not twice.

| construction | value | per share |
|---|---|---|
| 3-year window, D&A end (conservative) | ~$2,180M | **~$13** |
| 9-year window, capex end | ~$3,490M | **~$21** |
| trailing twelve months, D&A end | ~$4,235M | **~$25** |
| trailing twelve months, capex end (most generous) | ~$4,665M | **~$28** |

- **conservative ~$13** · **optimistic ~$28** · **current price $62.25**
- **The quote is 2.2x the top of the range and 4.8x the bottom.**

**WHICH BAR [E4-11 / E4-01]: the SCREAMER TEST [E4-01]**, because that is the test that fits a
name whose gate has already closed. Three outcomes; this is the third. **The price sits above
the whole range. The answer is no, and no margin is added on top** — *"startlingly low is what
you observe, not what you subtract."* **Windage count: ONE** — conservatism is applied once, in
the choice of the zero-growth capitalisation, and nowhere else. No risk premium was added to the
5.24% rate **[E3-42]**; certainty was priced at the understanding gate and nowhere else
**[E4-48]**.

**WHAT BOUNDS THE UPSIDE, stated as [E2-63] requires.** Even on the most generous reading —
that the whole margin step reverses, that revenue compounds at 6%, and that the TTM run rate
holds — the yield at this price starts at 2.09%. **The bound is the entry price, not the
business.** At roughly **$25 to $28** the name would clear the sovereign on the TTM
construction; it would still have failed Q2.

## E. Q6 ITEMS — RECORDED FOR THE REGISTER, NOT A VERDICT

Q6 is not opened for a name that failed Q2. The monitoring metrics are written down anyway, in
advance **[E1-02]**, because they are the five falsifiers named at Q2 and the register should
carry them.

- **Thesis-breaking metric (i.e. what would break THIS verdict):** consolidated **gross margin
  at or above 72% for four consecutive quarters** with the MD&A attributing it to **price or
  product**, not to volume absorption or mix. H1 2026 printed 70.9% GAAP and **71.7% adjusted**,
  attributed in both releases to *"favorable mix and volume"* — a near-miss on the level and a
  clean miss on the attribution, which is exactly what makes this the right tripwire.
- **Second:** **operating margin at or above 25% for three consecutive years**, which would
  mean the 2017-2021 economics were the level and not the wave.
- **Third:** any **filed unit, ASP or installed-base series**, which would make [E4-55]
  runnable for the first time.
- **Next catalyst dates:** Q3 2026 results (late October 2026); the FY2026 10-K (mid-February
  2027), which is where the end-market and organic-growth disclosures either return or do not.
- **[E3-30]'s monitoring question, answered:** *is this erosion an aberrational cycle, or has
  the business slipped in a way that permanently reduces intrinsic business value?* **Both, and
  the split is 21/41/38** — twenty-one percent of the operating-income fall was volume
  (aberrational), forty-one percent gross margin (part permanent), thirty-eight percent
  operating expense (management's to reverse, and it is reversing).
- **Position size: ZERO.** No alert band is armed and no PORTFOLIO row is created. Per the QLYS
  ruling of 2026-09-07, a name that failed on the **business** does not get a price alert,
  because a price alert on a Q2 failure is a category error. **The reversal condition is
  recorded in words above, not in `tools/alerts.json`.**

---
## SELF-AUDIT

- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 OUT, file closed. Q3-Q6
      recorded below the gate and explicitly marked as non-verdicts.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is IN on
      filed evidence alone. The competitor row is marked PROVISIONAL where peers are missing,
      and the Q2 verdict is explicitly stated NOT to rest on it.
- [x] Every UNRESEARCHED verdict names the artifact — there are none; no gate returned
      UNRESEARCHED.
- [x] Every UNKNOWABLE verdict states what cannot be known — there are none.
- [x] Step 0: seven 10-K vintages, one 10-Q, one DEF 14A and **three furnished 8-K earnings
      releases** read, with accession numbers; six figures cross-checked against the filed
      statements, and **two tooling defects found in the process.**
- [x] **A finding written from the 10-K alone was wrong and is corrected in an addendum rather
      than by editing history (operator rule 6):** the EBITDA-promotion flag, which reads clean
      in the 10-K and fires at full strength in the furnished releases.
- [x] Owner earnings on a multi-year mean; **eight windows** stated; capex band disclosed as a
      judgment with the [E5-20] exception class explicitly ruled inapplicable and the reason
      given.
- [x] Competitor row filled with five peers and same-metric, same-window, filing-sourced data;
      six further peers named as unavailable with the obstacle stated each time; the moat class
      marked PROVISIONAL on that basis and the verdict placed elsewhere.
- [x] Sovereign is USD, the earnings currency, from the US Treasury (the issuing authority),
      dated 2026-09-04.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen (the screamer test); **windage count = 1**, stated.
- [x] Prices dated; aggregator used for the live quote only and flagged; share count read off
      the 10-Q cover.
- [x] `python tools/check_framework.py` run before the final commit.
- [x] Run committed to git, by filename, after each gate.

## REGISTER

- **Verdict: [x] OUT (about the business), at Q2.**
- **One line:** the second-highest gross margin in machine vision and a 65% pre-tax return on
  the tangible capital it actually employs, but the only company in its own peer row whose
  gross margin fell through the 2021-2025 cycle while the industry leader's rose — and its own
  filings name the average selling price falling, seven classes of substitute including free
  ones, and a technology base that must be rebuilt every generation.
- **The four-verdict line:** **Q1 IN · Q2 OUT · Q3 not opened · Q4 not opened · Q5 not opened
  (computation only) · Q6 not opened.**
- **Price and pass/fail:** **$62.25** at 2026-09-04, market cap **$10,472M** — **FAIL**, and it
  would have failed at Q5 as well: yield **0.85% to 2.09%** against a **5.24%** sovereign,
  **−4.39 to −3.15 points**, requiring **7.9% to 9.2% perpetual growth** merely to reach the
  ~10% floor.
- **Value band:** **roughly $13 to $28 per share**, zero-growth, cash added at face. Price
  $62.25.
- **The STEP DOWN, adjudicated:** the owner-earnings step was **CYCLICAL and has substantially
  reversed**; the **gross-margin step is partly PERMANENT and has not**. The eighteen-year
  `level_shift_full` of 1.05 is the more nearly correct reading and both nine-year windows are
  measuring one cycle against another.
- **Physical/unit series:** **NONE EXISTS.** Seven vintages searched; zero hits on units, unit
  volume, installed base or ASP series. One qualitative ASP sentence, FY2024, never repeated.
- **The strongest single fact against this verdict [E4-51]:** **eight consecutive quarters of
  margin expansion to Q2 2026**, an adjusted gross margin of **71.7% in H1 2026** against 67.8%
  a year earlier, a **29.4% GAAP operating margin in Q2 2026**, and guidance beaten at or above
  the top of the range in both periods checked. A reader who weighted that recovery above
  [E3-03](2) would reach IN NARROW, and that reading is defensible.
- **Priors refuted, mine and the brief's:** (a) *IN NARROW at Q2* — refuted; (b) *"a hardware
  manufacturer will file a unit series"* — refuted, none exists in seven vintages; (c) *"the
  logistics boom is the step"* — refuted, the step is in the margin, not the volume, and the
  volume recovered; (d) *"Keyence's higher margin makes [E2-58] run against Cognex"* — **not
  refuted, confirmed, and by a route the brief did not name**: it is not the level of Keyence's
  margin that decides it but the fact that Keyence's gross margin *rose* through the same cycle
  in which Cognex's fell; (e) *"Q3 should be short, do not pad it"* — **refuted**: Q3 carried the
  single sharpest finding in the file, the Adjusted EBITDA milestone, and it was invisible in
  the 10-K.
- **Defects found:** two in the tooling (the D&A tag drops intangible amortization; the SBC tag
  returns $1.4M for a filed $42.7M in 2020), one in the queue row (the cap is 3.6% stale and
  low), one in the published spread (49.3% against a true 77.2% over sixteen constructions), and
  one in the brief (Q3 was not short, and telling a run to keep a gate short is how a
  [E4-29] flag gets missed).

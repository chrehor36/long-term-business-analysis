# Company Run — Hess Midstream LP (HESM) — 2026-09-20
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md` (as amended 2026-09-20:
the [E4-04] verdict form, the bank door, the CONVENTION clause in PRIME RULE 3, the five-check
acceptance test). Where this file and that document disagree, the document governs.

**WAVE 7, name 6.** Unattended overnight run. Name claimed at file creation, before any fetch.

**VERDICT: Q2 OUT.** Q1 IN. The file closes at Question 2, permanently, on the business.
Q3, Q4, Q5 and Q6 are NOT scored. What was seen at Q3 and Q4 is recorded beneath the close,
unscored, so a later reader is not required to refetch.

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

Asked aloud at Q2: *"Can I name the document that would resolve this?"* The answer is that no
further document is needed. The 10-K's own Item 1, Item 1A and Competition section settle it, in
the registrant's own words. That makes the verdict **OUT**, not UNRESEARCHED and not UNKNOWABLE.
**[E4-19]**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in.** HESM's revenue is fees per Mcf and per
barrel billed to Chevron subsidiaries for services performed in North Dakota; its debt is USD
senior notes and a USD credit facility; it reports in USD and pays USD distributions. The
earnings currency is **USD** and no FX step is required.
- rate **5.34%** · date **09/18/2026** · source **US Treasury daily par yield curve, 30-year,
  from the issuing authority.** `tools/_cache/sov_USD_treasury.csv` was deleted before the call
  so it could not be served stale. FRED DGS30 was not used and was not needed. The rate was
  **struck fresh and not inherited** from this run's brief or from any other run file.
- FX / ADR: not applicable.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes  [x] Item 1  [x] Item 1A
- **Annual report: Form 10-K for the year ended 2025-12-31, filed 2026-02-25, accession
  0001193125-26-071592** (`hesm-20251231.htm`).
- **Newest periodic: Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-06, accession
  0001193125-26-338055** (`hesm-20260630.htm`).
- **Furnished release, per the standing [E4-29] instruction: 8-K filed 2026-08-03, accession
  0001193125-26-329567, EX-99.1** (Q2 2026 results). Also read: 8-K filed 2026-02-02, accession
  0001193125-26-032732, EX-99.1 (FY2025 results), and 8-K filed 2026-03-04, accession
  0001193125-26-091542, Items 1.01 / 7.01 / 8.01 / 9.01.
- **Figure cross-checked against the filed statement:** the tagged
  `NetCashProvidedByUsedInOperatingActivities` FY2025 of 983,800,000 was checked line by line
  against the **Consolidated Statements of Cash Flows** in the 10-K, which shows *"Net cash
  provided by operating activities 983.8"* built from net income 684.6, depreciation 214.1,
  deferred income tax 113.7, equity-based compensation 1.6 and a working-capital drag. Two
  further figures were checked the same way: depreciation expense 214.1 and total long-term
  debt 3,739.5.

**Operator rule 4 note.** Nothing in this file rests on XBRL alone. The competitor row (below)
is built from tagged data for the peers and is labelled as such; the subject's own cell in that
row was recomputed and then reconciled against the 10-K's filed statements.

---
## THE SCREEN ROW — carried UNLABELLED, an input and not a verdict

From `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`:
`cap_m 5078 · oe_bottom_m 650 · oe_top_m 725 · yield_bottom 0.1281 · vs_sovereign 0.0746 ·
growth_required -0.0281 · level_shift 1.56 "no step" · level_shift_oe 1.84 "STEP UP —
normalize down [E4-41]" · years_filed 9 · spread_caveat "4-construction width only" ·
deal_note "1 8-K Item 1.01 ... most likely a credit facility or offering"`

**Four of those cells were work orders. All four are answered below; three of the four are
refuted at their source.** See **THE SCREEN ROW, ANSWERED** after the Q2 verdict.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics, in my own words, without management's language.** HESM owns steel in the
ground in three North Dakota counties: about 1,430 miles of gas and NGL gathering pipe, 615
miles of crude gathering pipe, 360 miles of produced-water pipe, one 400 MMcf/d gas plant at
Tioga, half of a second 200 MMcf/d plant, a rail terminal, a truck terminal and a propane
cavern in Minnesota. Wells are drilled by somebody else. The pipe is connected to the wellhead.
Every Mcf of gas, barrel of oil and barrel of produced water that flows through the pipe earns
a fee fixed in dollars, and HESM never owns the molecule, so the commodity price passes
straight through. Revenue is therefore **(physical volume) x (a contracted fee)**, and both
terms are set by contract with one counterparty.

**The scarce input this business controls.** Rights of way and physical connection to a
particular set of wellheads in the Williston Basin. Once the pipe is laid to a pad, a rival
must trench a second pipe to the same pad to compete for that molecule, which almost never
pays. That is the whole of what HESM owns. It does not own the acreage, the reserves, the
drilling schedule or the fee.

**Will the fundamentals look broadly the same in ten years?** The mechanism will. Pipe, fee,
volume. The framework asks whether the business is *"relatively simple and stable in
character"* **[E3-31]**, and on the mechanism it is. The magnitudes will not look the same,
and that is a Q2 and Q4 matter, not a Q1 one.

**The Up-C structure was established before anything else was reported, per the PAGP lesson.**
Three independent statements in the filings agree:
- Item 1, 10-K FY2025: *"the Company held a 62.3% controlling interest in the Partnership and
  Chevron held a 37.7% noncontrolling economic interest in the Partnership."*
- Balance sheet, 10-Q Q2 2026: Class A shares **128,350,881** and Class B shares **77,827,485**
  issued and outstanding at 2026-06-30. 128,350,881 / 206,178,366 = **62.25%**.
- Income statement, 10-Q Q2 2026: income before income tax 204.8, of which net income
  attributable to noncontrolling interest 77.3, leaves 127.5 to HESM LP = **62.3%** of pre-tax
  income. (Below the tax line the share is 55.5%, because substantially all of the income tax
  is borne at the Class A tier; the release says so: *"Substantially all of income tax expense
  was attributed to earnings of Class A shares reflective of Hess Midstream's organizational
  structure."*)

**The market price buys the Class A share only.** Class B shares carry voting rights and no
economic interest in the Company; the economics sit in the Class B *units* of the Partnership,
which are exchangeable and are held by Chevron through HINDL. **Class A and Class B are not
summed for the market capitalisation.** The look-through percentage used in every number in
this file is **62.25%**, from the cover and balance sheet of the newest periodic filing.

**VERDICT: [x] IN**

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that *"(1) is needed or desired; (2) is thought by its
> customers to have no close substitute and; (3) is not subject to price regulation."*
> **[E3-03]**

### The three criteria, read one at a time from the filings

**(1) Needed or desired — MET, and by exactly one party.** Chevron cannot sell a Bakken
molecule without gathering it. The 10-K: *"For the year ended December 31, 2025, 97% of our
revenues were attributable to our fee-based commercial agreements with Chevron, including
revenues from third-party volumes delivered under these agreements."* The prior two years read
98% and *"substantially all"*. So the answer to "desired by whom" is: by Chevron, and by
almost nobody else. Third-party services were $8.0M of $1,348.6M in 2023 and $33.5M of $789.1M
in H1 2026, a real but small start.

**(2) No close substitute — MET, and the registrant says why in one sentence.** Item 1,
"Competition": *"As a result of our contractual relationship with Chevron under our commercial
agreements and our direct connections to Chevron's production operations in the Williston
Basin, we believe that we will not face significant competition from other midstream service
providers for Chevron's crude oil, natural gas or NGL gathering, processing or terminaling
services."* Note the order of the registrant's own two reasons: **the contract first, the pipe
second.** For volumes it does not already have, the same Item 1A says the opposite: *"our
natural gas and crude oil gathering systems and processing plants are subject to competition
from existing and future third-party natural gas and crude oil gathering systems and natural
gas processing and fractionation plants in the Bakken"*, and *"some of our competitors have
assets in closer proximity to crude oil and natural gas supplies and have available idle
capacity in existing assets that would not require new capital investments for use."*

**(3) Not subject to price regulation — MET, and PAGP's answer does NOT transfer.** This was
the clause PAGP failed on, on FERC-indexed long-haul tariffs. HESM's Item 1 says the opposite
of PAGP's position: *"While most of our facilities and operations are not subject to FERC
jurisdiction, some of them are regulated by FERC"*; *"Section 1(b) of the Natural Gas Act
('NGA') exempts natural gas gathering facilities from regulation by FERC. Most of our natural
gas facilities — those upstream of the Tioga Gas Plant and LM4 processing plant — meet the
traditional tests FERC has used to establish whether a pipeline qualifies as 'gathering' that
is exempt from its jurisdiction"*; and for crude, *"the crude oil and NGL pipelines in our
gathering system similarly are not subject to FERC jurisdiction under the Interstate Commerce
Act."* The one FERC-certificated asset is a single 60.5-mile line out of Tioga, which received
waivers from open-access and tariff requirements because it moves only affiliate gas. What
remains is state *"complaint-based rate regulation."* **Clause (3) passes. The PAGP finding was
not transferred; it was tested and it does not apply.**

### So [E3-03] passes on its face. The verdict turns on what is holding the three criteria up.

**The fee is an administered price, written by the counterparty, and the corpus has a name for
that.** From Item 1, verbatim:

> *"a fee recalculation mechanism that allows fees to be adjusted annually during the Initial
> Term for updated estimates of cumulative throughput volumes and our capital and operating
> expenditures **in order to target a return on capital deployed** over the Initial Term of the
> applicable commercial agreement"*

and on what replaced it:

> *"Year 2023 was the final year of the annual rate redetermination process for the majority of
> our systems. At the end of 2023, the base rate for 2024 was set based on the average of the
> tariff rates from the years 2021 through 2023, adjusted for inflation … **we may not increase
> any fee by more than 3% in any calendar year** solely by reason of an increase in the consumer
> price index, and **no fee will ever be reduced below the amount of the applicable fee payable
> by Chevron in the prior year** as a result of a decrease in the consumer price index."*

A fee set to *target a return on capital deployed*, then frozen at a three-year average and
escalated by a capped, floored index, is not a price a market cleared. It is a price an
administrator set. **[E2-59]** is exactly on point and is the ruling doctrine here: administered
pricing *"could legally price their way to profitability even in the face of substantial
over-capacity"*, but the moat then **belongs to the regime**, and *"That day is gone"* is how it
ends. The framework states the same rule in its own words: *"Regulation caps a franchise
([E3-03] criterion 3) and floors a commodity business; neither creates the class."* Here the
administrator is not a regulator. **It is the customer, and the customer controls the general
partner.**

**The administrator's identity is the finding, and it is in Item 1A:**
- *"Our general partner and its affiliates, including our Sponsor, have conflicts of interest
  with us and limited fiduciary duties and they may favor their own interests to our
  detriment."*
- *"Our partnership agreement replaces our general partner's fiduciary duties to holders of the
  Company's shares with contractual standards governing its duties."*
- *"Our general partner and its affiliates, including our Sponsor, may compete with us and have
  no obligation to present business opportunities to us."*
- *"Holders of our Class A Shares have limited voting rights."*
- 8-K of 2026-03-04: *"GP LLC is wholly owned by Hess Infrastructure Partners GP LLC ('HIP GP'),
  and HIP GP is owned 100% by HINDL"*, HINDL being *"an indirect, wholly owned subsidiary of
  Chevron Corporation."*

So the single counterparty that supplies 97% of revenue also owns the general partner that
negotiates the fee, owns 37.7% of the economics, owes the Class A holders no fiduciary duty,
and is free to compete. **Asked in [E2-59]'s terms — whose moat is it? — the filings answer:
Chevron's.** What HESM holds is a contractual claim on Chevron's Bakken position, good until
2033 and renewable only by agreement.

**And the volume term is the output of a depleting asset that HESM neither owns nor controls.**
Item 1A, verbatim:

> *"Because of the natural decline in production from existing wells in our areas of operation,
> our success depends, in part, on Chevron and other producers replacing declining production …
> The natural gas and crude oil volumes that support our business depend on the level of
> production from natural gas and crude oil wells connected to our facilities, which may be less
> than expected and **will naturally decline over time.** As a result, our cash flows associated
> with these wells will also decline over time. In order to maintain or increase throughput
> levels at our facilities, Chevron and other producers … **must replace declining production** …
> **We have no control over** the level of drilling activity in our areas of operation, the
> amount of reserves associated with wells connected to our systems or the rate at which
> production from a well declines."*

**[E4-04]** — *"A moat that must be continuously rebuilt will eventually be no moat at all"* —
and the framework's own scope paragraph, which names the excluded class as the moat whose
*basis must be periodically replaced*, listing **depleting assets** by name. Applying the scope
test as written: *does a lapse in spending destroy the structure, or merely narrow it, and does
the spending defend the same advantage, or buy its replacement?* The pipe is defended; the
**earning basis** is not, because it is a hydrocarbon column that empties and is replaced only
by somebody else's drill bit. **[E3-51]** gives the exact form: *"when a surfer gets up and
catches the wave and just stays there, he can go a long, long time. But if he gets off the
wave, he becomes mired in shallows."* **A surfing run is not a moat; the advantage lives in the
wave, not the surfer.** HESM has surfed a good wave for nine filed years. It does not own the
wave, does not choose when the wave arrives, and says so in Item 1A.

**[E4-36]** asks which of the four causes of extreme success the record comes from, *"because
only some of them are ownable."* HESM's record comes from two: **wave-riding** (Bakken
development 2017 to 2025) and **an administered price** written by the affiliate. Neither is
ownable by the Class A holder.

### THE COMPETITOR ROW — required, because a moat is a relative claim **[E3-28]**

> *"I can't be an intelligent owner of a business unless I know what all the other businesses in
> that industry are doing."* **[E3-28]**

Metric: **operating income / (net PP&E + net intangibles + equity-method investments), FY2021 to
FY2025, means of numerator and denominator.** Same metric, same window, every cell rebuilt in
this run from each filer's own SEC XBRL company facts and none inherited.

| Company | metric, FY21-25 means | source |
|---|---|---|
| **HESM (subject)** | **25.6%** | own companyfacts; numerator reconciled to 10-K segment table, denominator to the 10-K balance sheet |
| MPLX | 20.1% | MPLX companyfacts |
| WES | 14.2% | WES companyfacts |
| EPD | 13.7% | EPD companyfacts |
| DKL | 13.3% | DKL companyfacts |
| AM (Antero Midstream) | 12.4% | AM companyfacts |
| TRGP | 12.3% | TRGP companyfacts |
| OKE | 11.1% | OKE companyfacts |
| ET | 9.0% | ET companyfacts |
| KMI | 8.7% | KMI companyfacts |
| PAA | 6.1% | PAA companyfacts |
| GEL | 5.3% | GEL companyfacts |

**Peers named: 11, plus the subject.** Buffett says eight; the listed US midstream group has
roughly this many real comparables and eleven were taken. **Peer median 12.3%. HESM is first of
twelve, at 2.1x the peer median.**

**The PAGP cross-run number is REPRODUCED, and that is the point at which [E4-26] had to be
applied.** PAGP's run of this same day reported HESM 25.5% in its own competitor table. This
run rebuilt the cell independently and got **25.56%** (operating income mean $852.5M, capital
base mean $3,335.3M). Every other cell reproduced within 1.2 points of PAGP's figures
(MPLX 20.1 vs 20.1, EPD 13.7 vs 13.7, KMI 8.7 vs 8.7, ET 9.0 vs 9.1, WES 14.2 vs 14.3, OKE 11.1
vs 11.6, TRGP 12.3 vs 11.8, GEL 5.3 vs 4.8, PAA 6.1 vs 5.6, DKL 13.3 vs 14.5). **The number
survives. The inference does not.** Operator rule 9 and **[E4-26]** require the hardest hunt for
disconfirming evidence against the favourite hypothesis, and the disconfirming evidence is the
fee mechanism quoted above: **the return HESM earns on deployed capital is the return its
contract with its own controlling owner was written to deliver.** A number that a related-party
contract was designed to produce is not evidence of a relative position won in a market. The
row I added to PAGP's list makes the point sharpest: **Antero Midstream, the closest structural
analogue in the list — a single-sponsor Appalachian gathering-and-water business with
sponsor-dedicated acreage — earns 12.4%, less than half of HESM's 25.6% on the same metric over
the same window.** The pipes are not twice as good. The contract is.

### [E4-55] — where units exist, monitor units. The physical series is the honest one.

The filings' own throughput table, consolidated, from the FY2023 / FY2024 / FY2025 10-K segment
notes and the Q2 2026 release:

| | 2023 | 2024 | 2025 | Q2 2026 vs Q2 2025 |
|---|---|---|---|---|
| Gas gathering (MMcf/d) | 381 | 437 | 458 | — |
| Crude oil gathering (MBbl/d) | 100 | 114 | 121 | — |
| Gas processing (MMcf/d) | 367 | 420 | 445 | **-4%** |
| Crude oil terminaling (MBbl/d) | 115 | 123 | 129 | **-15%** |
| Water gathering (MBbl/d) | 95 | 125 | 131 | **-12%** |

**2023 to 2025 is volume up and rate up — the exact inverse of PAGP, which was volume up and
rate down.** The FY2025 MD&A attributes the gathering revenue rise of $71.5M to *"$23.7 million
… attributable to higher tariff rates, $12.2 million … attributable to higher gas gathering
physical volumes"*. On the historical record HESM passes [E4-55] where PAGP failed it, and that
prior of the brief is refuted.

**The forward record does not pass.** The Q2 2026 furnished release, verbatim: *"Throughput
volumes decreased 15% for oil terminaling and 12% for water gathering compared with the second
quarter of 2025, **primarily due to lower production as a result of lower new-well activity.**"*
And: *"Second quarter 2026 revenues and other income were down $15.2 million compared with the
prior-year quarter, primarily due to lower throughput volumes, partially offset by higher tariff
rates and third-party services."* That is [E4-55]'s hiding shape appearing for the first time in
this filer: **dollar revenue held up by pricing while the physical series turns down.**

### THE SHARPEST FINDING IN THIS FILE — the MVC vintage panel

Chevron's minimum volume commitments are set at 80% of Chevron's own nominations in each
development plan, three years forward. Each 10-K prints the three-year table. **Setting four
vintages side by side turns a single table into a series, and it is a series nobody had run:**

| 10-K vintage | year 1 | year 2 | year 3 | gas gathering MMcf/d |
|---|---|---|---|---|
| FY2021 (nominated by Hess) | 2022: 363 | 2023: 317 | 2024: **351** | third year **up** 11% |
| FY2023 (nominated by Hess) | 2024: 365 | 2025: 380 | 2026: **412** | third year **up** 8% |
| FY2024 (nominated by Hess) | 2025: 382 | 2026: 418 | 2027: **418** | third year **flat** |
| **FY2025 (nominated by CHEVRON)** | 2026: **419** | 2027: **422** | 2028: **346** | third year **DOWN 18%** |

Same panel, crude oil gathering MBbl/d: FY2021 vintage 117 / 100 / 100; FY2023 vintage
101 / 100 / 105; FY2024 vintage 103 / 110 / 112; **FY2025 vintage 111 / 113 / 89, third year
down 21%.** Terminaling 2028 at 99 against 2027 at 124, **down 20%.** Gas processing 2028 at
336 against 404, **down 17%.** Water 2028 at 94 against 100, down 6%.

**Because MVC = 80% of the nomination, Chevron's own 2028 development plan nominates about 433
MMcf/d of gas against about 528 for 2027.** And the third-year decline is **new**. In the three
earlier vintages the third year rose or held; in the first plan filed after Chevron took control
it falls by a fifth. The 10-K offers no explanation for the step down, and no footnote attaches
to the 2028 column (the FY2024 10-K did footnote its own soft year, for Tioga turnaround
maintenance; there is no such note here). **This was the disconfirming test the brief demanded
be run against the flattering number, and it came back against the company.** The wave [E3-51]
is receding in the filer's own table.

### The other Q2 tests, scored

- **[E3-46]**, the number asked about the business before the manager: 25.6% return on deployed
  capital over five years, first of twelve. Recorded, and discounted for the reason above.
- **[E2-44]**, the two-characteristic test. Can it raise prices with demand flat and capacity
  under-utilised? **No.** The Secondary Term caps the annual increase at CPI and at 3%, whichever
  binds. Can it grow dollar volume with only minor additional capital? On the current asset base
  yes; to reach a new pad, no.
- **[E3-33] / [E5-28]**, untapped pricing power. **None.** Claiming that class is claiming near
  monopoly, and the pricing term is contractually fixed to 2033. The registrant cannot raise the
  fee even if it wished to.
- **[E4-37]**, the agony metric. Not observable: there is no price negotiation to observe,
  because the price is formulaic. The absence of the observation is itself the reading. The
  pricing decision does not belong to this company.
- **[E4-32]**, direction. The moat is **narrowing**: the redetermination mechanism that let fees
  reset to a target return ended in 2023 for the majority of systems and was replaced by a
  capped index; the nominated volumes turn down in 2028; the sole counterparty has changed from
  a Bakken-focused independent to a supermajor for whom the Williston is one basin among many.
- **[E3-61]**, the row's limit. Acknowledged: the row shows position, never conduct, and the
  conduct that matters most here is Chevron's, which no row can show.
- **[E4-23]**, key-person dependence: none found. This business does not require a superstar.
  That is not a credit; it is simply not the defect here.

### Class and verdict

- Class: **[ ] WIDE  [ ] NARROW  [x] NONE**, in the sense [E2-59] defines: the profitability is
  real and it is floored by an administered price, and *"neither creates the class."*
- Direction: **narrowing**, on the fee mechanism, on the 2028 nomination and on Q2 2026 units.

**VERDICT: [x] OUT**

**The OUT is on the business and it is permanent**, and it is deliberately **not** the
[E4-04] perimeter close. The 2026-09-20 ruling reserves **UNKNOWABLE at Q2** for a name that
passes [E3-03] and *"whose durability cannot be judged from filings"*. That is not this case.
HESM's durability **can** be judged from its filings, and the filings judge it: the registrant
states that it has no control over the drilling that produces its volume, that its cash flows
from connected wells *"will also decline over time"*, that its general partner owes it no
fiduciary duty and may compete with it, and that its fee is a formula whose base was frozen in
2023. The question [E2-59] asks — whose moat is it — has a filed answer, and the answer is that
it is not the Class A holder's. **Nothing further needs to be fetched.** That is an OUT.

---
## THE SCREEN ROW, ANSWERED — the four work orders

**1. `deal_note` — REFUTED, and the flag was wrong in the way the PAGP fold predicted.** The
note read *"1 8-K Item 1.01 filing(s) since 2026-02-25, none carrying a merger agreement
(EX-2.1) — most likely a credit facility or offering; open them only if something else is
odd."* The whole 8-K index since `newest_periodic` 2026-06-30 was pulled from `submissions.json`
and the items read by hand, as instructed. Result: **since 2026-06-30 there is exactly one 8-K,
filed 2026-08-03, Items 2.02 and 9.01, the Q2 2026 earnings release, and one Schedule 13G/A.
No financing, no disposal, no acquisition sits after the newest periodic filing.** But the
Item 1.01 the note guessed at was **not** a credit facility or an offering. It is the 8-K of
2026-03-04, accession 0001193125-26-091542: a **Unit Repurchase Agreement with Hess Investments
North Dakota LLC, a wholly owned Chevron subsidiary**, buying back 455,811 Class B units for
about $18 million at $39.49, the Class A closing price of 2026-03-02, alongside a **$42 million
accelerated share repurchase with JPMorgan**, both approved by the Conflicts Committee, and
**both funded with revolver borrowings** (*"The Company funded the Repurchase Price with
borrowings under its existing revolving credit facility."*). It is a related-party capital
transaction with the controlling owner. **The EX-2.1 heuristic would never have found it, and
the note's guess pointed a reader away from the single most structurally revealing filing of
the year.** Second consecutive midstream name on which this note has misdirected.

**2. `spread_caveat` — accepted and NOT discharged, because Q2 closed the file.** The note is
correct that the published band is four constructions of a 3-year and a 5-year window against
two capex ends, and cannot see the nine filed years. The rebuild is a Q4 task and **Q4 does not
open.** Recorded as a task that does not arise, not as a task skipped. For a later reader: the
nine-year operating-cash series is 336.5, 466.9, 470.7, 641.7, 795.5, 861.1, 866.4, 940.3, 983.8
($M, FY2017 to FY2025), nine-year mean **$707.0M** against the five-year mean **$889.4M**.

**3. The two level flags disagreed. The filings say both are describing the same thing and
neither is a finding — and the real normalisation runs the other way.** `level_note` read "no
step" at 1.56 on operating cash while `level_note_oe` read "STEP UP — normalize down [E4-41]" at
1.84 on owner earnings. They differ only because owner earnings subtracts a lumpy capex line
from a smooth cash line. The underlying rise from $336.5M to $983.8M of operating cash across
nine years is a **contracted build-out ramp** — gathering miles, compression, the Tioga
de-bottleneck, the water system — together with the fee redeterminations that ran to 2023, and
**[E4-41]** normalises down for *favourable exogenous breaks* named and removed, which a
completed capital programme is not. So the flag fires for the wrong reason. **It nonetheless
points the right way, for a reason neither flag could see: the recent level is a peak, not a
base.** The expansion programme is finished (2026 capex guided at $105M against $247.5M actually
spent in 2025 and $288.5M in 2024, with Q2 2026 capex of $30.6M *"a 56% decrease resulting mainly
from the completion of Hess Midstream's expansion of its gas compression capacity"*), and the
volume that the completed capacity will carry is nominated 18% lower in 2028. **Normalise down,
on the forward nomination, not on a past windfall.**

**4. `growth_required -0.0281` — REFUTED at source, and it is the PAGP look-through error again,
smaller.** The negative figure is an artefact of dividing a **consolidated** owner-earnings band
by a **Class-A-only** market capitalisation. See the computation block below. Corrected to one
tier, the yield falls by a factor of 1.61 and growth is required rather than not required.

---
## COMPUTATION — NOT A CLEARANCE
*(Operator rule 3. Q2 returned OUT, so no valuation clears anything and no entry language may
appear. This block exists only to discharge the brief's instruction to report the screen's
owner-earnings band against the tier it actually measures, and to refute `growth_required`
at its source. It is arithmetic, it is not a verdict, and it does not reopen the file.)*

**Price.** $40.16, close of **2026-09-18**. **Source: Yahoo Finance chart endpoint via
`tools/sources.py` — an AGGREGATOR, used for a live quote only and FLAGGED as such** per
operator rule 5.

**Shares.** **128,350,881 Class A shares**, from the **cover of the 10-Q for the quarter ended
2026-06-30, accession 0001193125-26-338055**: *"128,350,881 Class A shares representing limited
partner interests ('Class A Shares') in the registrant were outstanding as of July 31, 2026."*
**77,827,485 Class B shares** at 2026-06-30 from the same filing's balance sheet. **The market
price buys the Class A share only.** Class B shares carry votes and no economics in the Company;
the economics are the Class B *units* of the Partnership, held by Chevron. **The two classes are
not summed.**

- Class A market capitalisation = 128,350,881 x $40.16 = **$5,154.6M.** (The screen's `cap_m`
  5078 is the same construction at a slightly earlier price.)
- Whole-group equity value, Class A plus the exchangeable Class B units at the same price =
  206,178,366 x $40.16 = **$8,280.1M.**

**The screen's band measures the WHOLE GROUP.** Both ends were reproduced exactly from the
consolidated statements, which is how the tier was established:
- `oe_bottom_m 650` = 5-year mean operating cash $889.42M less 5-year mean SBC $1.62M less
  5-year mean **total capex** $237.32M = **$650.48M.**
- `oe_top_m 725` = 3-year mean operating cash $930.17M less 3-year mean SBC $1.70M less 3-year
  mean **depreciation** $203.23M = **$725.24M.**

Both are **100% of Hess Midstream Operations LP**, of which the Class A holder owns **62.25%**.

**The screen therefore divided a whole-group numerator by a Class-A-only denominator.**

| | screen, as published | corrected to one tier |
|---|---|---|
| numerator | $650M to $725M (consolidated) | $405M to $451M (62.25% look-through) |
| denominator | $5,078M (Class A only) | $5,155M (Class A only, at 09-18) |
| yield | **12.81%** | **7.85% to 8.76%** |

The same answer from the other side: $650M to $725M over the whole-group $8,280.1M is 7.85% to
8.76%. **The screen's yield is overstated by a factor of 1.61.** That is the PAGP trap in the
same industry and the same week, at a smaller magnitude: PAGP's was roughly four times, HESM's
is 1.6 times, because HESM's public float owns a much larger slice of its own opco.

**`growth_required -0.0281` refuted.** The negative sign came from the overstated 12.81% already
clearing the sovereign with room. At the corrected tier, against the **5.34%** US Treasury
30-year of 09-18-2026, the name is above the bond and **below the ~10% floor [E4-28]** on a
current-earnings basis, so growth **is** required rather than not required. **No floor verdict
is recorded**, because Q1 to Q4 did not all show IN and Q5 never opened. This paragraph is
arithmetic, not a ranking.

**Tag trap checked and NOT present.** PAA/PAGP stopped tagging `PropertyPlantAndEquipmentNet`
after FY2020 and moved to the finance-lease-inclusive element, silently dropping the filer from
any screen keyed to the first tag. **HESM tags `PropertyPlantAndEquipmentNet` continuously from
FY2018 to FY2025** (2,735.3 / 3,010.1 / 3,111.3 / 3,125.0 / 3,172.8 / 3,229.2 / 3,325.4 /
3,369.8, $M). The prior is refuted for this filer. The competitor row above did carry the
dual-tag fallback for the peers, which is why the PAA cell resolved at all.

**Working capital netted by hand, per the PAGP fold.** `working_capital_flag()` reads one line
and never nets its counter-line; HESM's `wc_note` was empty, and the hand check confirms there
is nothing to net: the FY2025 cash-flow detail lines are receivables -3.1 and -8.0, other assets
-0.4, payables -31.0 and -9.4, accrued +6.4, other liabilities -4.3, a net drag of about $49.8M
against $983.8M of operating cash. No single line approaches the flag threshold and no line has
an offsetting twin of the PAGP kind.

---
## BENEATH THE CLOSE — NOT SCORED
*Q2 returned OUT, so Q3 and Q4 were not run and carry no verdict. The framework's standing
instruction from the CGNX run is to pull the furnished release before scoring [E4-29] and
[E4-22]'s third flag, and to record what was seen even when the gate is not reached. What
follows is observation, recorded so a later reader need not refetch. **None of it is a finding
about the managers or about survival, and none of it contributed to the Q2 verdict, which rests
entirely on [E3-03], [E2-59], [E4-04], [E3-51] and the filed volume series.***

**[E4-29], the fifth flag, seen and NOT scored.** *"Trumpeting EBITDA … is a particularly
pernicious practice."* The Q2 2026 furnished release (EX-99.1 to the 8-K of 2026-08-03) uses
**"Adjusted EBITDA" 21 times and "Adjusted Free Cash Flow" 16 times**; the FY2025 release
(EX-99.1 to the 8-K of 2026-02-02) uses "Adjusted EBITDA" **27 times**. Both lead the highlights
bullet list with them. Adjusted Free Cash Flow is defined as *"Adjusted EBITDA less net
interest, excluding amortization of deferred financing costs, cash paid for federal and state
income taxes, capital expenditures and ongoing contributions to equity investments"* — a measure
that deducts capital expenditure but not depreciation, which is [E5-41]'s **reverse float** in
its purest form: the money is already spent and the charge is deleted.

**[E4-22] third flag, seen and NOT scored.** Full-year 2026 numeric guidance is published on
four financial lines and five volume lines (net income $650-700M, Adjusted EBITDA $1,225-1,275M,
capital expenditures $105M, Adjusted Free Cash Flow $910-960M), was *"issued on December 9,
2025"*, was reaffirmed on 2026-02-02 and reaffirmed again on 2026-08-03. A multi-year target is
also published: *"approximately $1 billion of Adjusted Free Cash Flow after Distributions
through 2028."* **[E3-48]**'s action — set past guidance against outturn — was not performed,
because the gate was not reached.

**[E2-60] and [E2-52], seen and NOT scored.** FY2025 financing lines from the filed cash-flow
statement: share and unit repurchases **$400.0M**, distributions to shareholders **$350.2M**,
distributions to noncontrolling interest **$265.5M**, total **$1,015.7M** returned against
$983.8M of operating cash and $255.6M of capital expenditure. Total long-term debt rose from
$3,449.4M to $3,739.5M over the same year. **[E2-60]**: *"restricted earnings"* are those whose
payout costs the business *"its financial strength"*, and where leverage rises to fund the
payout, (c) was understated. The pattern repeats in 2026: the March ASR and the Class B
repurchase were, in the 8-K's own words, funded *"with borrowings under its existing revolving
credit facility."*

**[E5-11] strength 2, seen and NOT scored.** *"massive liquid assets."* **Cash and cash
equivalents at 2025-12-31: $1.9 million**, against $3,800.5M of total debt (fixed-rate senior
notes $3,100.0M, Term Loan A $362.5M, revolver $338.0M; maturities $32.5M in 2026, $668.0M in
2027, $1,350.0M in 2028, $600.0M in 2029, $1,150.0M in 2030). Liquidity is the revolving credit
facility and nothing else. **[E5-39]**'s *"kindness of strangers"* test would have been the
first thing scored at Q4.

**Cash taxes, seen and NOT scored.** FY2025 income tax expense $113.8M of which **$113.7M is
deferred**. The near-zero cash tax is structural to the Up-C and is fully disclosed (the
cash-flow statement carries *"Recognition of deferred tax asset $305.0"*), so it is a read and
not the **[E4-30]** tell; it is recorded so that a later reader does not mistake it for one.

**[E3-70] SBC, seen and NOT scored.** Equity-based compensation is $1.6M to $1.8M a year against
$983.8M of operating cash, about 0.17%. Immaterial either way, and the resume state's grant-date
caveat does not bite here.

---
## WHAT THIS RUN REFUTED, AND WHAT IT CONFIRMED

**Refuted (five):**
1. **`deal_note`'s guess.** The lone Item 1.01 was a related-party Class B unit repurchase from
   Chevron plus a $42M ASR, both revolver-funded. Not a credit facility, not an offering.
2. **PAGP's clause-(3) failure does not transfer.** HESM's gathering assets are NGA-exempt and
   its crude lines are outside the ICA. [E3-03] criterion (3) passes.
3. **PAGP's volume-up / rate-down shape does not transfer.** HESM 2023-2025 is volume up AND
   rate up. The turn shows only in Q2 2026 and in the 2028 nominations.
4. **The `PropertyPlantAndEquipmentNet` tag trap is not present at HESM.** Tagged continuously
   FY2018 to FY2025.
5. **`growth_required -0.0281`.** An artefact of the consolidated-over-Class-A mismatch, exactly
   as PAGP's -0.1381 was. Do not inherit this column in an Up-C.

**Also refuted, from this run's own brief:** the claim that *"the filer segregates expansion
capital expenditures from maintenance in its own capital program disclosure."* **It does not.**
Neither the FY2025 10-K nor either furnished release splits maintenance from expansion capital
expenditure; the 10-K gives one line, *"Total capital expenditures $247.5"*, and reconciles it
to the cash figure. The words *"maintenance capital"* and *"expansion capital"* appear nowhere
in the Q2 2026 release. Had Q4 opened, (c) would have had to be a **disclosed guess** under
**[E2-23]** and **[E3-44]**, with no filer split to lean on.

**Confirmed (two):**
1. **HESM's 25.5% in PAGP's competitor table reproduces**, at 25.56%, rebuilt independently from
   HESM's own filings. First of twelve, at 2.1x the peer median of 12.3%.
2. **The screen's owner-earnings band is a whole-group number** and both ends reproduce exactly
   from the consolidated statements, which establishes the tier and therefore the 1.61x
   overstatement of the published yield.

---
## SELF-AUDIT
- [x] Questions answered in order; stopped at the first that is not IN; no verdict skipped
- [x] No question marked IN carries an "unverified" or "provisional" caveat
- [x] No UNRESEARCHED verdict was returned, so none needs an artifact named
- [x] No UNKNOWABLE verdict was returned
- [x] Step 0: the filing was read, with accession numbers; three figures cross-checked against
      the filed statements (operating cash 983.8, depreciation 214.1, long-term debt 3,739.5)
- [x] The furnished 8-K EX-99.1 was pulled and read before [E4-29] was recorded, per the
      standing CGNX instruction; recorded beneath the close and NOT scored, as PAGP did
- [x] Owner earnings: **not reported as a verdict input.** The only owner-earnings arithmetic in
      this file is inside the COMPUTATION block, headed as operator rule 3 requires, carrying no
      entry language, reproducing the screen's construction to identify its tier. **No
      net-income proxy was used anywhere** (operator rule 5; the addendum of 2026-09-20)
- [x] Competitor row filled: 11 peers plus the subject, same metric, same window, every cell
      rebuilt in this run. Moat is NOT marked provisional; the class is NONE
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury
      daily par yield curve), dated 09/18/2026, struck fresh with the cache deleted first
- [x] No value range stated; Q5 did not open
- [x] No bar chosen; Q5 did not open. Windage: not spent, nothing was valued
- [x] Price dated 2026-09-18 and flagged as an aggregator live quote
- [x] Share count from the cover of the newest periodic filing, with the accession number and
      the as-of date quoted; two classes named; the classes were NOT summed
- [x] `principle_ledger.csv` opened with `encoding="utf-8-sig"`; **the file was counted, not the
      pointer: 311 rows**, not the 267 the stale KEY FILES table records
- [x] Run committed to git with a pathspec and a freshly written message file

## REGISTER
- Verdict: **[x] OUT (about the business)**
- One line: **HESM FAILS at Q2. [E3-03]'s three criteria are met, and every one of them is held
  up by a single contract with the counterparty that owns its general partner, supplies 97% of
  its revenue, owes its Class A holders no fiduciary duty and is free to compete with it; the
  fee under that contract was written "to target a return on capital deployed" and is now frozen
  at a 2021-23 average escalated by a capped, floored CPI, so the 25.6% return that ranks first
  of twelve midstream peers is the number the contract was designed to deliver and not a
  position won in a market [E2-59]; and the volume the fee is applied to is the output of a
  depleting resource the registrant says it has no control over, which makes the run a surfing
  run and not a moat [E4-04, E3-51], with the wave now visibly receding in the filer's own
  table, because Chevron's first three-year development plan nominates 2028 gas volumes 18%
  below 2027 and crude 21% below, the first third-year decline in four filed vintages.**

# RE-LOOK — Salesforce, Inc. (CRM) at the first pre-committed level — 2026-09-21

**This is a RE-LOOK, not a new run and not an entry.** The name was run in full on 2026-09-07
(`Test Runs/2026-09-07 Run - CRM Salesforce.md`): Q1–Q4 all IN, **Q5 NOT IN — quit on at the
[E4-28] floor** at $259.23. That run armed a band in `tools/alerts.json`:

> *"CRM at/below $240: the top of the value band ($80–240, centre ~$150)."*

The band fired. The quote on **2026-09-21** is **$237.50** (aggregator, live quote only,
flagged per operator rule 5). **The band's own instruction is a re-run at this price, and that
is all this file does.** It carries no buy language anywhere; operator rule 9 names the
incentive an analyst has to clear a name that is close, and this name is close — closer than it
was on 2026-09-07, and the closeness is the reason every adjustment below is stated with its
direction.

**Governing documents:** `Framework/THE FRAMEWORK v4.md` (v4.1, Q5 and Q6 as amended
2026-09-20) and `CLAUDE.md`. The name is **not owned**, so `THE HOLDINGS FRAMEWORK.md` does
not apply and no hold question is asked.

---
## STATUS OF THIS FILE
*Written incrementally under the write-early protocol. Sections appear as they close.*

- [x] 1. What has been filed since 2026-09-07 — gate by gate, and the Q6 tripwires
- [x] 2. Q5 re-derived at $237.50
- [x] 3. The verdict
- [x] 4. Q6 re-read
- [x] 5. Self-audit and acceptance test — `python tools/check_framework.py` **PASS**
- [ ] 6. Fold

**THE ANSWER IN ONE LINE, written before the sections so no reader has to hunt for it:
Q1–Q4 stand; no tripwire has fired; and the name is QUIT ON AT THE FLOOR A SECOND TIME —
honest pre-tax expectancy 5.5%–9.3% against ~10%. But the margin is now 0.66 points, not
0.38, and the whole verdict turns on ONE adjustment this re-look makes and the 2026-09-07 run
did not: the $39.5bn debt stack drawn in March 2026 is not yet in the trailing twelve months
of operating cash flow. Left unadjusted, exactly one construction out of forty clears the
floor at 10.06%. That fact is on the page at section 2.**

---
## 1. WHAT HAS BEEN FILED SINCE 2026-09-07

**Source: `https://data.sec.gov/submissions/CIK0001108524.json`, fetched 2026-09-21, saved to
`Test Runs/_research 2026-09-21 CRM/CRM submissions CIK0001108524.json`.** Every filing with a
filing date on or after 2026-09-01 is listed, so that the four items dated between the prior
run's data cut (2026-09-04) and its file date are visible too.

### THE COMPLETE LIST

| filed | form | accession | what it is |
|---|---|---|---|
| **2026-09-11** | **S-8** | `0001108524-26-000204` | Intercom, Inc. (**"Fin"**) acquisition **completed 2026-09-10**; registers **1,325,957** shares for assumed RSUs |
| **2026-09-16** | **4** | `0001108524-26-000208` | **Sabastian Niles**, President and CLO — code **F**, 8,873 sh @ $255.65 on 2026-09-15; 18,164 held after |
| **2026-09-16** | **4** | `0001108524-26-000206` | **Miguel Milano**, President and COO — code **F**, 6,535 sh @ $255.65 on 2026-09-15; 32,219 held after |
| **2026-09-17** | **8-K** | `0001108524-26-000210` | Items **7.01 and 9.01** — the **Investor Day** presentation of 2026-09-16, furnished as **EX-99.1** |
| *2026-09-01* | *S-8* | `0001108524-26-000195` | *Contentful Global, Inc. acquisition **completed 2026-09-01**; registers **600,418** shares* |
| *2026-09-04* | *8-K* | `0001108524-26-000197` | *Item **5.02(e)** — Executive Deferred Compensation Plan, approved 2026-09-02* |
| *2026-09-04* | *4* | `0001108524-26-000199` | ***Craig Conway**, director — code **S**, 1,418 sh @ $260.4958 and 3,082 sh @ $260.6629; 5,437 held after* |
| *2026-09-04* | *144* | `0001950047-26-009121` | *notice of proposed sale* |

*(The four italicised rows carry filing dates on or before 2026-09-04 and are therefore not
"since 2026-09-07". They are read and listed here because the 2026-09-07 run cites none of
them, and two of them — the Contentful closing and the deferred-compensation plan — are facts
about the company that a re-look should not pretend to have already seen.)*

### THE ONE FACT THAT GOVERNS THE WHOLE OF SECTION 2

> **No 10-Q, no 10-K, no 10-K/A, no proxy and no Item 2.02 earnings 8-K has been filed.**

The **latest periodic filing is unchanged**: the 10-Q for the quarter ended **2026-07-31**,
filed **2026-08-27**, accession **`0001108524-26-000190`**, document `crm-20260731.htm`. It
follows that:

- **Every owner-earnings window in the 2026-09-07 run is unchanged.** There is no new quarter
  to fold in, and the TTM construction still runs to 2026-07-31.
- **The share count on the latest cover is unchanged at 823 million** — *"As of August 20,
  2026, there were approximately 823 million shares of the Registrant's Common Stock
  outstanding."* The two S-8s register **future issuance** against assumed awards
  (600,418 + 1,325,957 = **1,926,375 shares, 0.23% of the register**); they are not
  outstanding shares and do not move the cover count.
- **Therefore the only thing that has genuinely moved is the price and the sovereign**, plus
  whatever the Investor Day deck and the two closings say about the business. Those are worked
  below, and Q5 is re-derived at the new price in section 2.

### WHAT THE 2026-09-17 8-K ACTUALLY CONTAINS, AND HOW IT WAS READ

The exhibit is `investorday2026.htm` — **thirty slide images**. It would be unreadable except
that the filer left the source deck's accessibility text under each image in a **one-point
white font**, verbatim from the HTML:

> `<FONT size="1" style="font-size:1pt;color:white">`

That text layer is the slide content, and it is **also the deck's unredacted internal editorial
notes**. Three examples, quoted exactly as they sit in the furnished exhibit:

> *"To be pulled from DF deck - will need to overlay design"* (slide 17)
> *"Design Notes -Most important - doing what we said we would do, nod back to prior year
> -Edits needed:"* (slide 9)
> *"kThan ouy ALL HEADERS LEFT JUSTIFIED"* (slide 2 — transposed characters as filed; **flagged
> as an artifact under PRIME RULE 1, not smoothed**)

**This is recorded, not scored.** A furnished Item 7.01 exhibit that carries its own drafting
comments is a disclosure-hygiene observation about a document the filer expressly states *"shall
not be deemed 'filed' for purposes of Section 18."* It is not a misstatement and it is not a
Q3 disqualifier. It is written down because **[E3-27]** and **[E4-14]** require that the
document be read rather than the summary, and because the next reader should know why the
quotations below can be taken verbatim from a slide deck at all. The full extraction is at
`Test Runs/_research 2026-09-21 CRM/EX991_slides.txt`.

### GATE BY GATE — does anything filed since 2026-09-07 disturb the fact the gate rested on?

#### Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **STANDS IN (narrow). Not disturbed. The recorded doubt is ENLARGED.**

Nothing filed changes the unit economics: seats × price per seat per month × renewal, billed a
year in advance, less an ~8% leak. The 2026-09-07 run passed Q1 **narrowly** and recorded a
**metering-unit doubt** against it. The Investor Day deck does not resolve that doubt — **it
makes it bigger**, in the company's own words:

> *"Consumption flywheel driving usage and unlocking ARR expansion"* … *"Top 100 customers with
> most all-time **AWUs** generated as of Q2 FY27"* … *"Flex credits & more"*

**"AWU" is not defined anywhere in the deck, and it appears in no 10-K or 10-Q.** The same slide
set introduces two further metrics with definitions that exist only in this furnished exhibit:

> *"The Company defines ('ARR') as the annualized recurring value of active subscription
> agreements that were executed at the end of the reporting period. The Company defines Net New
> Annual Order Value ('NNAOV') as the net change in the annual order value of our customer
> subscription agreements during a given period."*

So the monetisation story management tells is increasingly told in **ARR, NNAOV, AOV and AWUs**,
of which the revenue-recognition-linked measures in the filed statements are none. **[E4-29]**'s
class is the concern and **[E4-22]**'s third flag is where it lives; it is carried at Q3, not
here. **Q1's verdict is unchanged, and the ground for its narrowness is firmer than it was.**

#### Q2 — IS IT A FRANCHISE? **STANDS IN · class NARROW · direction flat to narrowing. Not disturbed.**

The moat metric is the attrition disclosure, and **no new filing carries one** — it is an
annual-and-quarterly MD&A item and the newest remains the 10-Q the prior run read:

> *"As of July 31, 2026, our attrition rate, excluding Slack self-service, Informatica, and
> current year acquisitions, was approximately **eight percent**."*

Two things in the Investor Day deck touch Q2 and **neither is a filed fact that can move it**:

1. The deck lists *"Multi-Cloud Pricing & Packaging"* first among *"Growth drivers fuel
   acceleration."* The 2026-09-07 run's Q2 finding was that **price has contributed nothing for
   six consecutive years on the company's own MD&A revenue attribution**. A forward slide naming
   pricing as a driver is a **claim about the future**, not a revision of the filed attribution.
   It becomes a Q2 test at the FY2027 10-K, and it is added to the register at section 4.
2. The deck's own revenue split reproduces the prior run's core finding rather than disturbing
   it. From the 10-Q's subscription table (Q2 FY2027 against Q2 FY2026): **Agentforce Apps
   $7,193M, +8%**; **Data 360, Headless Platform and Other $3,618M, +20%.** The original
   franchise grows at 8; the bought categories grow at 20. That is the same shape the run
   recorded and it is the shape that produced **flat to narrowing**.

One figure moved in the franchise's favour and is recorded because it did: **R&D was 14.87% of
revenue in Q2 FY2027 against 14.47% a year earlier** ($1,687M / $11,345M against $1,481M /
$10,236M). The prior run's competitor row put Salesforce **last on R&D intensity at 14.4%**.
It is now rising. **This is not enough to re-class the moat, and it is written down anyway**
because **[E4-26]** requires the disconfirming evidence for the analyst's own view be hunted
hardest, and the analyst's view here was that the rebuild spend was thin.

#### Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? **STANDS IN. No disqualifier. THE LIVE CAPITAL-ALLOCATION FLAG IS ENLARGED, and this is the one gate where the new filing bites.**

**Honesty first, because it is binary, permanent and filings-based [E5-16].** Nothing filed
since 2026-09-07 is a misstatement of fact. No restatement, no auditor change, no Item 4.02, no
enforcement disclosure. **Honesty: unchanged, clean.**

**Rationality is where the 2026-09-17 exhibit lands, and it lands hard.** The deck reports the
return on the company's largest single capital allocation of the year — the **$25.0 billion**
accelerated share repurchase — as follows, verbatim:

> *"Accelerated Share Repurchase $25B largest ASR ever · **Over 40% return on our investment** ·
> **$182 expected average share price** · ≥14% expected share count reduction"*

And the footnote, on the same slide, states the method:

> *"Expected return on invested capital calculation leverages CRM price as of market close on
> 8/31/2026 over the expected average price of shares to be repurchased through the ASR as of
> 8/31/2026."*

**Read that method against the arithmetic.** The close on 2026-08-31 was approximately $259;
$259 ÷ $182 = 1.423, which is the *"over 40%."* **The company is reporting the return on a
$25bn buyback as its own share quote divided by the price it paid.** Two consequences, and both
belong on the record:

1. **It is not a return.** A buyback's return is the owner earnings per share it buys,
   against the cash spent. The deck's measure is a **mark to the quote**, which no filed
   statement recognises and which **[E4-21]**'s *"We don't formally have discount rates"* has
   nothing to do with — this is not a valuation judgment, it is a price.
2. **It is already 12 points smaller and nothing happened in the business.** At **$237.50
   today**, $237.50 ÷ $182 − 1 = **30.5%.** The company's stated "return on our investment"
   fell from *"over 40%"* to 30.5% in three weeks, on no filing, no event and no change in
   Salesforce's earning power. **A measure that moves like that is a quotation, not a result**,
   and putting it on the capital-allocation slide is exactly the *"scoreboard no auditor
   signs"* that the 2026-09-07 run named as its central Q3 finding under **[E4-52]** and
   **[E4-27]**.

**Two more from the same deck, both measured and both against the company:**

- > *"**190% of Free Cash Flow returned in FY27**"* and *"$60B+ cumulative shareholder returns
  > to date"* and *"**Our biggest bet in FY27 is Salesforce**"*

  Checked against the filings: FY2027 capital returned is the **$25.0bn ASR** plus **$2,145M of
  Q1 open-market repurchase** (10-Q, Note 9) plus roughly **$1,490M of dividends** ($0.440 per
  share quarterly × ~$374M and $373M in H1) = about **$28,635M against FY2027 free cash flow
  guided at roughly $15bn** — **191% of free cash flow, which reproduces the deck's 190% to
  within a point.** The **$13.6bn excess is the borrowing.** This is the **[E5-39]** finding of
  the prior run, restated by the company on its own slide.
- The ASR's *"$182 expected average share price"* is **below the $198.34 the company actually
  paid on the initial delivery of ~103 million shares** (10-Q, Note 9). The forward leg of the
  ASR is therefore expected to settle at a lower average than the front leg — which is a fact
  about the price path in the period, not about management, and is recorded for completeness.

**Verdict on Q3: IN, unchanged.** No filed misstatement, so nothing here is a disqualifier
under **[E5-16]**. But the **capital-allocation flag the prior run left live is now larger**,
and the framework's CONVENTION labelled 2026-09-20 says where a Q3 capital-allocation flag
goes: **it binds position size**, never the discount rate **[E3-42, E4-21]**. That is honoured
at section 3.

#### Q4 — WILL IT SURVIVE? **STANDS IN · GOOD, not great. Not disturbed by a new filing — and the re-look found a figure inside the OLD filing that the prior run did not carry into Q5.**

Nothing filed since 2026-09-07 changes the survival case. The Investor Day deck **confirms**
the prior run's two decisive Q4 findings out of the company's own mouth:

- **The margin lever is spent.** The deck's own GAAP-to-non-GAAP reconciliation puts **FY2027
  guided GAAP operating margin at 20.1%** against FY2026's 20.06% ($8,331M / $41,525M) —
  **flat**, exactly as the run said. Non-GAAP 34.3% against 34.1%.
- **Free cash flow is guided to about $15bn** (*"On track to 3x free cash flow since FY22"*,
  $5B → $15B) against FY2026's **$14,402M** — roughly **4% growth**, which reproduces the 4–5%
  operating-cash-flow guidance the run used and **does not raise it.**

**What the re-look found, and it is the crux of section 2.** The prior run computed interest
coverage correctly — *"interest coverage on OCF-less-(c) **7.3x**"*, and it reproduces exactly:
($14,996M − $1,178M) ÷ $1,892M = **7.30x**, where $1,892M is the Q2 FY2027 reported interest
expense of $473M annualised. **So the run knew the forward interest run-rate and used it at Q4.
It did not use it at Q5.** Owner earnings at Q5 were built from operating cash flow, and
operating cash flow for every window in that table — the TTM included — bears only a fraction
of that interest. The correction is made and counted in section 2.

For completeness, the leverage line as the same figures read on a second basis: **FY2026 GAAP
operating income $8,331M ÷ $1,892M = 4.40x** coverage. Both numbers are true; they measure
different things; the run published the higher one and this file publishes both.

**[E5-11] re-scored: still 3 of 3, and strength (3)'s direction is recorded harder.** Contracted
revenue, self-funding operations and compliance with all covenants are unchanged. What has
changed is only the emphasis the company itself supplies: *"Our biggest bet in FY27 is
Salesforce"* and *"190% of Free Cash Flow returned in FY27."* **[E2-64]**'s offensive balance
sheet — *"the most attractive opportunities may present themselves at a time when credit is
extremely expensive"* — has been spent on the register, and the company now says so in a
slide. **The gate still passes. It passes with the direction written against it.**

**And the acquisition pace is intact, which matters because the prior run excluded acquisitions
from (c).** From the 10-Q and the two S-8s:

| FY2027 to date | consideration | status |
|---|---|---|
| Qualified.com, Inc. (April 2026) | **$1.2bn**, of which *"$1.1 billion in cash"*; $954M goodwill | closed, in the 10-Q |
| Contentful Global, Inc. (agreed May 2026) | *"approximately **$1.5 billion in cash**, net of the value of shares currently owned by Salesforce"* | **closed 2026-09-01** (S-8 `…-000195`) |
| Intercom, Inc. ("Fin", agreed June 2026) | *"approximately **$3.6 billion in cash**"* | **closed 2026-09-10** (S-8 `…-000204`) |

**About $6.3bn of cash acquisitions in the first eight months of FY2027**, against the run's
five-year mean acquisition consideration of **$8,282M a year**. The run put on the page a third
reading of (c) in which acquisitions **are** maintenance capital, computed it (**owner earnings
of −$1,103M, negative**) and declined to adopt it. **The pace has not slowed, so that reading
has not gone away**, and it is restated at section 2 rather than buried.

### THE 2026-09-07 RUN'S OWN Q6 TRIPWIRES, CHECKED ONE BY ONE

| tripwire, as set on 2026-09-07 | test | **fired?** |
|---|---|---|
| **Confirming:** OCF growth above 8% for two consecutive fiscal years with GAAP operating margin ≥20% | Investor Day reaffirms FY2027 free cash flow ≈$15bn (~4% growth) and GAAP operating margin **20.1%, flat** | **NO — and the newest filing pushes it further away, not closer** |
| **Breaking:** disclosed attrition above 9%, or the disclosure dropped or replaced with words | newest disclosure is still *"approximately eight percent"*, still numeric (10-Q, 2026-07-31). No new periodic filing exists to drop it | **NO. Next testable at the FY2027 10-K, ~March 2027** |
| **Breaking:** sales and marketing back above 37% of revenue | Q2 FY2027 **$3,859M / $11,345M = 34.0%**; H1 **33.9%** | **NO — and it improved** |
| **Price:** *"a quotation below about $130 puts this name back on the page"* at the corpus-default window | quote **$237.50** | **NO** |
| **Catalyst:** Q3 FY2027 results, late Nov 2026 — final ASR settlement and *"the first disclosure of terms for the Contentful and Fin acquisitions, neither of which is in any filing read here"* | **PARTIALLY, AND THE TRIPWIRE WAS WRONGLY WORDED.** Both deals **closed** (2026-09-01, 2026-09-10) and their terms — **$1.5bn and $3.6bn in cash** — were **in the 10-Q the run itself read at Step 0**. The final ASR settlement is still owed, in Q3 FY2027 | **NO on the substance; the tripwire's factual premise was already false when written — corrected at section 4** |
| **[E3-40] standing watch:** *"if a fourth large acquisition is announced before the FY2030 targets are tested, that is the [E4-24] exit trigger"* | Contentful $1.5bn and Fin $3.6bn closed; Qualified $1.2bn in April; the deck adds *"Doti"* and an *"AI Labs"* programme. **On the filed record none is "large"**: no Item 2.01 8-K, no Rule 3-05 statements, and the two assumed-award S-8s total **0.23% of the register** | **NO on the filed evidence. Direction recorded: the deck now makes M&A a named pillar — *"Acquisitions for the AI Era"*, *"Recent focus on Data, AI accelerators, and AI Labs"* — which is the [E3-40] watch pointed at by the company itself** |

**NOT ONE TRIPWIRE HAS FIRED.** Three moved *against* reopening the name (the confirming
metric, sales and marketing, the price); two are untestable until a periodic filing arrives; one
was mis-worded by the prior run and is corrected below.

### INSIDER ACTIVITY — READ, AND IT IS CLEAN FOR THE PERIOD

The only Form 4 activity **since 2026-09-07** is **two code-F transactions on 2026-09-15** —
shares withheld by the issuer to settle tax on vesting, not sales into the market: **Sabastian
Niles 8,873** and **Miguel Milano 6,535**, both at **$255.65**. There is **no discretionary
open-market sale by any insider since 2026-09-07.** The one such sale in the window listed
above — **Craig Conway, a director, 4,500 shares at about $260.50** — is dated **2026-09-04**
and predates the prior run. **No signal either way, and the absence is stated rather than left
to be assumed [the absence-claim rule, v4.1].**

### THE ITEM 5.02 8-K OF 2026-09-04, READ BECAUSE THE PRIOR RUN DID NOT CITE IT

Not a departure or an appointment. Item **5.02(e)**: on 2026-09-02 the Compensation Committee
approved the **Salesforce, Inc. Executive Deferred Compensation Plan**, letting executives defer
*"up to a maximum of 75% of base salary and up to 90% of any annual performance bonus,"* with
*"no employer match or similar contribution"* and the obligations *"general unsecured and
unfunded."* **No effect on any gate.** It is a deferral vehicle, not new compensation, and the
plan document itself is promised as an exhibit to the next 10-Q. Recorded so that the next
reader of the pay disclosure — which is where the prior run's sharpest Q3 finding sits — knows
this vehicle now exists.

---
## 2. Q5 RE-DERIVED AT $237.50

**Framework order, and it is not the order a hopeful analyst would choose: the ~10% floor
first [E4-28], then the yield against the bond [E4-21], then the ranking — and only if it
clears the floor.**

### STEP 0 OF THIS SECTION — THE RATE, THE PRICE, AND THE SHARE COUNT

**The sovereign, struck fresh from the issuing authority, not inherited from the brief and not
inherited from the prior run** (operator rule 5; `Screens/RESUME STATE 2026-09-12` section 2:
*"Do not inherit it from any brief"*):

- **5.34% · 2026-09-18 · US Treasury daily par yield curve, 30 Yr, from the issuing authority.**
- Fetched directly from `home.treasury.gov` as CSV and saved to
  `Test Runs/_research 2026-09-21 CRM/treasury_par_yield_2026.csv`. **FRED was not used**;
  `tools/sources.py` reads Treasury first per `CLAUDE.md` as corrected 2026-09-02, and it
  returned the same figure independently.
- **The 2026-09-21 curve had not posted at the time of this run** (the file's newest row is
  09/18/2026; Monday's curve posts after the close). The neighbouring rows read
  **5.29 / 5.35 / 5.36 / 5.34 / 5.35** — a two-basis-point band, so nothing in this file turns
  on the missing day. **Recorded rather than smoothed.**
- **The sovereign has RISEN since the prior run: 5.24% (2026-09-04) → 5.34% (2026-09-18), ten
  basis points against the name.** No per-name risk premium is added **[E3-42]** — *"mathematical
  gibberish."*

**FX:** none. Salesforce reports in USD; 65% of FY2026 revenue was United States (10-K, Note 2).
Earnings currency and quote currency are the same. No ADR ratio.

**The price.** **$237.50**, 2026-09-21, **aggregator, live quote only, flagged**. It is supplied
by the brief as the level at which the band fired; it is used as given and it is labelled, not
laundered. Against the prior run's $259.23 (2026-09-04) that is **−8.38%**.

**The share count — the cover page, not the weighted average.** The largest error the prior run
found in the tooling was `tools/run.py` reporting a **weighted-average** diluted count of 956.0M.
That defect is unchanged and is re-flagged at the self-audit. The count used here is the cover
page of the **latest periodic filing**, verbatim:

> *"As of August 20, 2026, there were approximately **823 million** shares of the Registrant's
> Common Stock outstanding."* — 10-Q, accession `0001108524-26-000190`, cover page

**Issued versus outstanding, checked.** The 10-Q balance sheet carries a treasury-stock line and
the company *"accounts for treasury stock under the cost method"*; the cover figure is the
**outstanding** count, which is the one the market prices, and it is the figure used. One class
of common stock, $0.001 par.

**Post-cover issuance and buybacks, checked in both directions:**

| item | effect on the count after 2026-08-20 | treatment |
|---|---|---|
| **The ASR's final settlement** — *"The initial share delivery represented approximately 80 percent of the total shares expected to be repurchased"*; ~103M delivered at $198.34; *"final settlement … expected to occur in the third quarter of fiscal 2027"* | **about 26 million more shares will be retired**, i.e. the count is heading to roughly **797M** | **not taken.** 823M is the filed number; the 797M case is run as an explicit sensitivity below, and it does not change the verdict |
| **$22.9 billion of authorisation remaining** (10-Q Note 9, as of 2026-07-31, under a **$50.0 billion** February 2026 authorisation) | unknown, at the company's discretion | not taken — an authorisation is not a purchase |
| **The two S-8 registrations** (600,418 + 1,325,957 = **1,926,375** shares against assumed Contentful and Intercom awards) | up to **+0.23%**, over years, as awards vest | not taken — registered capacity is not outstanding stock |
| **Open-market repurchase in Q2 FY2027** | **zero** — the 10-Q's table shows *"Three months ended July 31 · 0 · $— · $0"* | nothing to adjust |

> ### **MARKET CAP USED THROUGHOUT: 823.0M × $237.50 = $195,462M.**
> Against the prior run's $213,346M, the cap has fallen **$17,884M, or 8.38%.**

### THE FILING WAS READ — and the (c) DEFECT CLASS THE BRIEF NAMES WAS ALREADY CLOSED

No new periodic filing exists, so the primary documents are those the prior run read, plus the
four new ones at section 1. **Two figures were re-cross-checked against the filed statement for
this file** (operator rule 4), and both are in the 10-Q for the quarter ended 2026-07-31:

- **Interest expense, three months ended July 31, 2026: $(473)M**, against **$(67)M** in the
  comparable quarter — Condensed Consolidated Statements of Operations, p.4.
- **Cash paid during the period for Interest: $153M (three months) and $240M (six months)**,
  against **$87M** and **$115M** — Supplemental Cash Flow Disclosure, p.8.

Those two lines are the whole of the new arithmetic below, and they are quoted because everything
turns on them.

**The defect class the brief names is already closed, and the re-look confirms it rather than
re-deciding it.** The brief warns that *"acquired-intangible amortisation and lease amortisation
must not sit inside (c), as the IBM and DIS runs found."* **The 2026-09-07 run excluded both,
explicitly and with the filing's own decomposition footnote quoted**, and adopted

> **(c) = capital expenditures + principal payments on financing obligations**

on the ground that the physical renewal spend hides in the **financing** section. Re-read today,
that construction stands and it is the most careful (c) in this queue: FY2026 capex $594M plus
financing-obligation principal $584M = **$1,178M**, against **$1,200M** of fixed-asset
depreciation quoted verbatim from the property note — **0.98x, two independent routes to the
same number.** Acquisition amortisation (46.5% of D&A) is excluded because R&D of $5,993M above
the operating-cash-flow line already renews the technology; ROU amortisation (20.5%) is excluded
because the rent is already netted inside operating cash flow. **Nothing in this re-look changes
that, and all four (c) ends are carried in the grids below so no reader has to take the judged
one on trust.**

**One reconciliation, in the conservative direction, disclosed rather than silently adopted.**
The prior run's TTM row used **(c) = $1,166M**, implying a TTM financing-obligation figure of
$570M. Rebuilt line by line from the 10-Q — FY2026 $584M **+** H1 FY2027 $306M **−** H1 FY2026
$278M = **$612M** — TTM (c) is **$1,208M** and TTM owner earnings at the judged end are
**$10,877M**, not $10,919M. **A $42M difference, 0.4%, and it goes against the name**, so it is
taken.

### THE NEW ADJUSTMENT, AND IT DECIDES THE FILE — THE MARCH-2026 DEBT STACK IS NOT IN THE WINDOW

**The fact.** In March 2026 Salesforce drew a new debt stack to fund the ASR. At 2026-07-31 the
10-Q's Note 8 shows **$39,500M of principal outstanding** against **$14,439M** of carrying value
at 2026-01-31, of which $6,000M was the Informatica credit agreements since repaid. Fourteen
instruments, contractual rates **1.50% to 6.70%**, with every March 2026 tranche at **4.24% to
6.70%**.

**The forward cost of that stack, built two independent ways:**

| route | construction | annual |
|---|---|---|
| **A — the filed principal × the filed contractual rate**, instrument by instrument from Note 8 | 3,500@4.50 + 1,500@3.70 + 1,000@1.50 + 4,250@4.65 + 6,000@4.24 + 1,500@1.95 + 3,750@4.90 + 2,750@5.20 + 4,500@5.55 + 1,250@2.70 + 1,500@6.40 + 2,000@2.90 + 3,750@6.55 + 1,250@3.05 + 1,000@6.70 | **$1,824M** |
| **B — the reported quarterly interest line, annualised** | Q2 FY2027 interest expense **$473M** × 4 | **$1,892M** |

**The two routes agree to 3.7%.** Route A is the lower figure and it is the one used for the
adjustment, because the lower figure is the one that favours the company and windage must be
spent in one direction only **[E4-48]**.

**The defect.** The owner-earnings table in the 2026-09-07 run is built from **operating cash
flow**, and operating cash flow is net of interest **paid**. Here is what the windows actually
bear:

| period | interest **accrued** | interest **paid in cash** |
|---|---|---|
| FY2024 | $283M | $254M |
| FY2025 | $272M | $233M |
| FY2026 | **$324M** | **$276M** |
| H1 FY2026 | $135M | $115M |
| **H1 FY2027** | **$790M** | **$240M** |
| **TTM to 2026-07-31** (FY26 + H1 FY27 − H1 FY26) | **$979M** | **$401M** |
| **forward run-rate** | **$1,892M** | **~$1,824M** |

**Two gaps, and both are real:**

1. **The window gap.** The trailing twelve months contain only **five months** of the new stack.
   Every multi-year window contains **none** of it: the ten-year mean accrued interest is $199M
   and the five-year mean is $280M, against a forward run-rate of $1,824M–$1,892M.
2. **The deferral gap, and this one is the sharper of the two.** H1 FY2027 **accrued $790M** and
   **paid $240M in cash** — a **$550M** difference, because the March 2026 notes' first coupon
   dates had not yet fallen due. **Operating cash flow for the trailing twelve months is
   therefore flattered by more than half a billion dollars of interest that has been incurred and
   will be paid.**

**Why this is a legitimate normalisation and not windage.** **[E4-41]** requires that a
favourable exogenous break inside the measurement window be named and removed. The prior run
applied that rule in one direction — it named the $1,017M of FY2026 strategic-investment gains
and confirmed they were already outside owner earnings. **This is the same rule in the mirror:
the near-absence of eleven months of coupon on $31bn of newly drawn debt is a favourable break
inside the window, and it has to come out.** **[E4-48]** is the general form: *"try to be as
realistic as you can on those numbers, but with any errors being on the conservative side."*
And the 2026-09-07 run had the number in its own hands — it used **$1,892M** to compute interest
coverage of 7.30x at Q4 and then built Q5 off cash flows that bear a fraction of it. **That is
the defect, it is the prior run's, and this file corrects it.**

**Why it is not a double count.** Owner earnings are charged the interest; the market cap is
the equity only; the ~103M shares the borrowing retired are **already out** of the 823M cover
count. Equity earnings against equity value, with the debt service charged once. The one place
the arithmetic is still slightly against the company — the remaining ~26M ASR shares are not
yet out of the count — is run as a sensitivity below, and it does not change the verdict.

**Construction:** for each window, **owner earnings less (forward run-rate − the interest
actually inside that window)**. Cash basis where the cash disclosure exists (FY2026 alone and
the TTM); accrual basis for the multi-year windows, where accrued and cash differ by under $50M
against a step-up of $1,530M–$1,690M and the choice is immaterial.

### GRID A — THE FORTY CONSTRUCTIONS AS THE 2026-09-07 RUN BUILT THEM, RE-YIELDED AT $237.50

*Nothing is adjusted in this grid. It is the prior run's own arithmetic at the new price, and it
is put first because it is the grid that argues against this file's conclusion.*

Owner earnings $M · yield on $195,462M · **expectancy = yield + the company's own guided 4.5%**

| window | (c)=capex *[most generous]* | (c)=capex+fin *[JUDGED]* | (c)=D&A less acq. amort. | (c)=total D&A *[corpus default]* |
|---|---|---|---|---|
| 3yr FY2024-26 | 8,952 · 4.58% · **9.08%** | 8,346 · 4.27% · **8.77%** | 7,661 · 3.92% · 8.42% | 5,925 · 3.03% · 7.53% |
| 4yr FY2023-26 | 7,472 · 3.82% · 8.32% | 6,914 · 3.54% · 8.04% | 6,245 · 3.19% · 7.69% | 4,456 · 2.28% · 6.78% |
| **5yr FY2022-26 — corpus default [E2-42]** | 6,479 · 3.31% · 7.81% | **6,000 · 3.07% · 7.57%** | 5,305 · 2.71% · 7.21% | 3,549 · 1.82% · 6.32% |
| 6yr FY2021-26 | 5,691 · 2.91% · 7.41% | 5,275 · 2.70% · 7.20% | 4,569 · 2.34% · 6.84% | 2,918 · 1.49% · 5.99% |
| 7yr FY2020-26 | 5,150 · 2.63% · 7.13% | 4,769 · 2.44% · 6.94% | 4,088 · 2.09% · 6.59% | 2,560 · 1.31% · 5.81% |
| 8yr FY2019-26 | 4,696 · 2.40% · 6.90% | 4,346 · 2.22% · 6.72% | 3,774 · 1.93% · 6.43% | 2,382 · 1.22% · 5.72% |
| 9yr FY2018-26 | 4,308 · 2.20% · 6.70% | 3,986 · 2.04% · 6.54% | 3,493 · 1.79% · 6.29% | 2,223 · 1.14% · 5.64% |
| 10yr FY2017-26 | 3,965 · 2.03% · 6.53% | 3,665 · 1.88% · 6.38% | 3,238 · 1.66% · 6.16% | 2,072 · 1.06% · 5.56% |
| FY2026 alone | **10,893 · 5.57% · 10.07% ✦** | 10,309 · 5.27% · 9.77% | 9,543 · 4.88% · 9.38% | 7,856 · 4.02% · 8.52% |
| **TTM to 2026-07-31** | **11,489 · 5.88% · 10.38% ✦** | **10,877 · 5.56% · 10.06% ✦** | 10,158 · 5.20% · 9.70% | 8,163 · 4.18% · 8.68% |

> ### **THREE OF FORTY CLEAR THE FLOOR ON THIS BASIS, AND THIS IS THE STRONGEST FACT AGAINST THIS FILE'S CONCLUSION. It is stated here, in full, before the adjustment that removes it.**
>
> | construction | owner earnings | yield | **expectancy** | vs the 5.34% sovereign |
> |---|---|---|---|---|
> | TTM, (c)=capex | $11,489M | 5.88% | **10.38%** | **+0.54 pts** |
> | FY2026 alone, (c)=capex | $10,893M | 5.57% | **10.07%** | **+0.23 pts** |
> | TTM, (c)=capex+fin (judged) | $10,877M | 5.56% | **10.06%** | **+0.22 pts** |
>
> **On 2026-09-07 not one of thirty-three constructions yielded as much as the sovereign — the
> best was 5.12% against 5.24%, 0.12 points short. At $237.50, three now pay MORE than the
> sovereign, and three clear the ~10% floor. That is a genuine change and it is why the band
> was armed at $240 in the first place. Everything below is the case for not stopping here.**

### GRID B — THE SAME FORTY, NORMALISED FOR THE DEBT STACK

Owner earnings less the interest step-up · yield on $195,462M · expectancy = yield + 4.5%

| window | step-up | (c)=capex | (c)=capex+fin *[JUDGED]* | (c)=D&A less acq. | (c)=total D&A |
|---|---|---|---|---|---|
| 3yr FY2024-26 | $1,599M | 7,353 · 3.76% · 8.26% | 6,747 · 3.45% · **7.95%** | 6,062 · 3.10% · 7.60% | 4,326 · 2.21% · 6.71% |
| 4yr FY2023-26 | $1,597M | 5,875 · 3.01% · 7.51% | 5,316 · 2.72% · 7.22% | 4,648 · 2.38% · 6.88% | 2,858 · 1.46% · 5.96% |
| **5yr FY2022-26 — corpus default** | $1,612M | 4,866 · 2.49% · 6.99% | **4,388 · 2.25% · 6.75%** | 3,693 · 1.89% · 6.39% | 1,937 · 0.99% · 5.49% |
| 6yr FY2021-26 | $1,638M | 4,053 · 2.07% · 6.57% | 3,637 · 1.86% · 6.36% | 2,931 · 1.50% · 6.00% | 1,281 · 0.66% · 5.16% |
| 7yr FY2020-26 | $1,655M | 3,494 · 1.79% · 6.29% | 3,113 · 1.59% · 6.09% | 2,433 · 1.24% · 5.74% | 905 · 0.46% · 4.96% |
| 8yr FY2019-26 | $1,666M | 3,030 · 1.55% · 6.05% | 2,680 · 1.37% · 5.87% | 2,109 · 1.08% · 5.58% | 716 · 0.37% · 4.87% |
| 9yr FY2018-26 | $1,681M | 2,627 · 1.34% · 5.84% | 2,304 · 1.18% · 5.68% | 1,812 · 0.93% · 5.43% | 542 · 0.28% · 4.78% |
| 10yr FY2017-26 | $1,693M | 2,272 · 1.16% · 5.66% | 1,972 · 1.01% · **5.51%** | 1,544 · 0.79% · 5.29% | 379 · 0.19% · 4.69% |
| FY2026 alone | $1,548M | 9,345 · 4.78% · 9.28% | 8,761 · 4.48% · 8.98% | 7,995 · 4.09% · 8.59% | 6,308 · 3.23% · 7.73% |
| **TTM to 2026-07-31** | **$1,423M** | **10,066 · 5.15% · 9.65%** | **9,454 · 4.84% · 9.34%** | 8,735 · 4.47% · 8.97% | 6,740 · 3.45% · 7.95% |

> ### **ZERO OF FORTY CLEAR THE FLOOR. The best construction in the file — trailing twelve months, maintenance capex at its most generous reading, the company's own growth guidance — reaches 9.65% and falls 0.35 points short. The judged construction reaches 9.34% and falls 0.66 short.**

**SENSITIVITY — the ASR's remaining ~26 million shares, run because it is the one input still
tilted against the company:**

| shares | cap | TTM judged, as-run | TTM judged, normalised | TTM (c)=capex, normalised |
|---|---|---|---|---|
| **823.0M** (the filed cover) | $195,462M | 10.06% | **9.34%** | **9.65%** |
| 797.0M (post-final-settlement estimate) | $189,288M | 10.25% | **9.49%** | **9.82%** |

**The verdict is robust to it.** Retiring every remaining ASR share moves the most generous
normalised construction to 9.82% — still below the floor, and that construction charges the
company nothing for the interest deferral it has not yet paid.

### 1. THE YIELD **[E4-21]** — *the government bond is "the yardstick at a base"*

- **Corpus-default window [E2-42], judged (c), normalised: $4,388M ÷ $195,462M = 2.25%**,
  against the **5.34%** sovereign — **−3.09 points.**
- Full range across the forty normalised constructions: **0.19% to 5.15%.**
- **Not one of the forty normalised constructions yields as much as the 30-year Treasury.** The
  best is **5.15% against 5.34% — 0.19 points short of the risk-free rate before a single risk
  is priced.** On 2026-09-07 the equivalent gap was 0.12 points; the price fell 8.4% and the
  gap widened, because the sovereign rose 10bp and the debt cost came into the reckoning.
- **On the unadjusted basis, three constructions pay 0.22 to 0.54 points over the sovereign.**
  Both facts are on the page.

### 2. WHAT THE PRICE ALREADY ASSUMES — the growth belief, against the base rate **[E4-35]**

Perpetual owner-earnings growth required to pay the ~10% floor, judged (c):

| window | as-run | **normalised** |
|---|---|---|
| 10-year | 8.12% | **8.99%** |
| **5-year — corpus default** | 6.93% | **7.75%** |
| 3-year | 5.73% | **6.55%** |
| FY2026 alone | 4.73% | **5.52%** |
| **TTM to 2026-07-31** | 4.44% | **5.16%** |

**Is that belief inside the base rate? Yes — and it still fails, which is the finding.**
**[E4-35]** wagers that *"fewer than 10 of the 200 most profitable companies in 2000 will attain
15% annual growth in earnings-per-share over the next 20 years."* Nothing here needs 15%. The
corpus-default window needs **7.75% forever**; the most generous needs **5.16% forever.** Those
are ordinary numbers. **So the name is not refused for absurdity — it is refused on arithmetic,
and the arithmetic is decided by the one comparison that matters:**

> **The company's own guidance for the current year is operating cash flow growth of 4–5%.**
> The most generous construction in this file needs **5.16% in perpetuity.** **Even at the most
> generous reading, the buyer at $237.50 requires Salesforce to beat its own guidance, forever,
> merely to reach the floor — and the corpus-default construction requires it to beat that
> guidance by a factor of 1.7, forever.**

**What bounds the upside, stated because [E2-63] requires it and not only the yield.** Three
bounds, all from the company:

1. **The margin lever is spent, on management's own forecast.** The Investor Day reconciliation
   guides **FY2027 GAAP operating margin to 20.1%** against FY2026's 20.06% — **flat.** Almost
   the whole owner-earnings increment of the last four years came from 2.1% → 20.1%; that engine
   has stopped. **[E2-63]**'s ceiling clause governs: most operating businesses are capped
   *"unless more capital is continuously invested."*
2. **The capital that would be invested is the capital (c) excludes.** Revenue is guided to grow
   11–12% and operating cash flow 4–5%, and the gap is bought growth. **$6.3bn of cash
   acquisitions have closed in the first eight months of FY2027** (Qualified $1.2bn, Contentful
   $1.5bn, Fin $3.6bn) against a five-year mean of $8,282M a year. **The prior run's unadopted
   third reading of (c) — acquisitions as maintenance capital, giving owner earnings of
   −$1,103M — is not refuted by anything filed since. It is simply not adopted, for the reason
   the prior run gave: the core grew 8% with no purchase in it.** The reader who disagrees gets
   a negative number and no expectancy at all, and that reader is not being hidden from.
3. **[E4-44] — multiple expansion is not a perpetual term.** *"The value of an asset … cannot
   over the long term grow faster than its earnings do."* Nothing in this file assumes it does:
   every value below capitalises owner earnings at a fixed rate.

**And the growth input itself is charged in the company's favour twice over.** It is the
company's own number, not the analyst's; it is a **one-year** guide treated as a **perpetuity**;
and it is applied to an owner-earnings stream from which the acquisition spending that sustains
the revenue line has been removed. **No growth estimate in this file is mine.**

### 3. WHAT YOU ARE PAID — points over the sovereign

| construction, judged (c) | as-run | **normalised** |
|---|---|---|
| 10-year | −3.46 | **−4.33** |
| 5-year — corpus default | −2.27 | **−3.09** |
| 3-year | −1.07 | **−1.89** |
| FY2026 alone | −0.07 | **−0.86** |
| TTM to 2026-07-31 | **+0.22** | **−0.50** |
| widest, across all forty normalised | — | **−5.15 to −0.19** |

**Normalised, you are paid nothing over the sovereign at any of forty constructions.
Unadjusted, you are paid up to 0.54 points at three of them.**

### WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE **[E3-42]**

- Sovereign used: **5.34% — the bare rate. No per-name premium added**, which **[E3-42]** calls
  *"mathematical gibberish"* and **[E4-21]** confirms (*"We don't formally have discount rates"*).
- Certainty was handled in the two places the corpus names: at the **understanding gate**, where
  Q1 passed narrowly and the metering-unit doubt is recorded and now enlarged; and in the
  **discount to value demanded at the end** — Bar 1's margin, spent once **[E4-11, E4-48]** —
  which is never reached, because the floor disposes of the name first.
- **The Q3 capital-allocation flag is NOT in the rate either.** It binds position size
  (framework CONVENTION, labelled 2026-09-20), and that is where section 3 puts it.

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-25, E4-01]**

*"Using precise numbers is, in fact, foolish; working with a range of possibilities is the better
approach."* Judged owner earnings capitalised at **the floor less the company's guided growth
(10.0% − 4.5% = 5.5%)**, on 823.0M shares:

| window | as-run $/share | **normalised $/share** |
|---|---|---|
| 10-year | $81 | **$44** |
| 9-year | $88 | $51 |
| 8-year | $96 | $59 |
| 7-year | $105 | $69 |
| 6-year | $117 | $80 |
| **5-year — corpus default** | **$133** | **$97** |
| 4-year | $153 | $117 |
| 3-year | $184 | $149 |
| FY2026 alone | $228 | $194 |
| TTM to 2026-07-31 | $240 | $209 |

> ### **THE RANGE, IN ROUND NUMBERS**
>
> - **As the 2026-09-07 run built it, unchanged: roughly $80 to $240, centre roughly $135.**
>   *(The prior run published the centre as ~$150; rebuilt from its own corpus-default window
>   the centre is $133. Recorded, not edited — the prior run's ordinal and round numbers stay
>   as filed, operator rule 6.)*
> - **Normalised for the debt stack: roughly $45 to $210, centre roughly $100.**
>
> ### **WHERE $237.50 SITS**
>
> - **On the as-run range: inside it, at the very top — 1% below the $240 optimistic end, and
>   1.8x the $133 centre.** This is exactly what the band was armed to detect, and the band was
>   correct to fire.
> - **On the normalised range: ABOVE THE WHOLE RANGE — 13% above the $210 optimistic end, and
>   2.4x the $100 centre.**
> - Either way, **$237.50 is above or at the extreme top of the range on every construction that
>   is not the single best trailing twelve months at the most generous maintenance-capex guess
>   this file can defend.**

**IS THE RANGE TOO WIDE TO CONCLUDE [E4-25]?** The width across the forty is **5.54x**, which
would normally close a file on width alone. **It does not here, for the reason the prior run
gave and this one re-tests: the width is a LEVEL SHIFT, not dispersion.** GAAP operating margin
went 2.1% (FY2022) → 20.1% (FY2026) after a 10% workforce reduction, so every window reaching
back past FY2024 averages a company that no longer exists. **[E3-55]** scopes it: the spread
measures uncertainty about the level, and the mechanism of this level change is known, disclosed
and completed — the company guides the margin flat from here. **So the file does not close on
width. It closes on the floor.**

### WHICH BAR **[E4-01, E4-11]** — one, not both

- [x] **Screamer test [E4-01] / [E5-34].** *"We will buy the stock … if it sells at a reasonable
      price in relation to **the bottom boundary of our estimate**."* Bottom boundary
      **~$45** normalised (**~$80** as-run). Price **$237.50.** **Outcome: the price is above
      the entire range on the normalised construction, and at the top of it on the unadjusted
      one. No.**
- [ ] Normal method [E4-11] — not used. No end margin is applied, because none is needed to
      reach the verdict, and applying one would spend conservatism twice.

### THE WINDAGE COUNT, STATED BECAUSE IT IS THE WHOLE ARGUMENT **[E4-11, E4-48]**

| adjustment | direction | size |
|---|---|---|
| **(c) = $1,178M rather than the corpus default of $3,631M** | **in the company's favour** | **+$2,453M of owner earnings a year** |
| Growth input is the company's own guidance, not the analyst's; a one-year guide treated as a perpetuity | **in the company's favour** | +4.5 points of expectancy, in perpetuity |
| Forward interest taken at the **lower** of the two routes ($1,824M coupon build, not $1,892M annualised accrual) | **in the company's favour** | +$68M a year |
| Remaining ~26M ASR shares **not** removed from the count | in the company's favour | reduces yield by ~3% relative |
| No per-name premium in the sovereign; no end margin applied | neutral by rule | — |
| TTM (c) rebuilt to $1,208M from the prior run's implied $1,166M | **conservative** | −$42M |
| **Interest normalised to the drawn debt stack** | **conservative** | **−$1,423M (TTM) to −$1,693M (10-year)** |

> **ONE material conservative adjustment, and it is the [E4-41] normalisation. FOUR in the
> company's favour, the largest of them worth $2,453M a year. Conservatism is spent ONCE
> [E4-11] and the count is net in the company's favour — and the name still fails the floor on
> every one of forty constructions.** That is stated so no reader can attribute this verdict to
> stacked windage **[E4-48]**.

---
## 3. THE VERDICT

**In the amended Q5 form of the template, one of four:**

- [ ] **IN — RANKED** *(clears the ~10% floor; take its place in the ranking)*
- [x] **NOT IN — QUIT ON, below the [E4-28] floor. Not ranked.**
- [ ] **UNRESEARCHED**
- [ ] **UNKNOWABLE**

> ### **NOT IN. The name is quit on at the floor for the second time, at $237.50 as it was at $259.23.**
>
> **Honest pre-tax expectancy 5.51% to 9.65% across forty constructions, against a floor of
> roughly 10%.** The judged construction over the corpus-default five-year window is **6.75%**.
> The best construction in the file — trailing twelve months, maintenance capex at its most
> generous reading, the company's own guided growth — is **9.65%, 0.35 points short.**
> **[E4-28]**: *"that's the figure we quit on … that's true whether short rates are 6 percent or
> whether short rates are 1 percent."*
>
> **Not one of forty constructions yields as much as the 5.34% sovereign**; the best is 5.15%,
> **0.19 points short of the risk-free rate before a single risk is priced.**
>
> **Judged value roughly $45 to $210, centre roughly $100, against a price of $237.50 — above
> the whole range.** On the prior run's own unadjusted arithmetic the range is roughly $80 to
> $240, centre roughly $133, and $237.50 sits 1% below its optimistic end.

**Because it is quit on, three things follow and this file does all three.**

1. **No ranking.** The framework's order is explicit — the floor first, *"and only then, above
   the floor, the ranking"* **[E4-28, E4-21]**. A candidate below the floor *"is not ranked, it
   is quit on, however it compares with the bond of the day."* **So CRM is not ranked against
   the other thirty-two names in this project's register that cleared all four business gates
   and failed on price.** The comparison was not made and no place in the list is claimed. The
   nothing-option has a location **[E2-74]**: between opportunities the money is parked, and
   *"Mr. Market will offer us opportunities — you can be sure of that."*
2. **No sizing pre-commitment [E3-45].** The template asks for one only where the name clears.
   For completeness of the record: **the position size implied by this verdict is ZERO**, and it
   would be sized down even above the floor, because the Q3 capital-allocation flag binds
   position size (framework CONVENTION, labelled 2026-09-20) and that flag is **larger** after
   the 2026-09-17 exhibit, not smaller. **[E3-45]**'s direction — capital to rank #1, not
   pro-rata down the list — never engages for a name that is not on the list.
3. **THE FILE ARMS NOTHING NEW, and it says so.** One existing level is **moved down** and one
   is **left where it is with a second derivation**; no new band is created. Section 4 carries
   both, with the reasons.

**THIS FILE CONTAINS NO INSTRUCTION TO BUY AND NO ENTRY LANGUAGE.** The operator decides.
Operator rule 9 is the reason the sentence is here: *"the analyst holding a position has an
incentive to clear it; the builder of a framework has an incentive to validate it"* — and the
analyst who re-runs a name because its band fired has an incentive to find that the band was
worth arming. **The one adjustment that decides this file runs against that incentive**, which
is not proof it is right, only a reason the reader should test it first. It is set out in full
at section 2 with both grids, so that a reader who declines the normalisation can see exactly
what they get: three of forty constructions clearing the floor by 0.06 to 0.38 points, on a
trailing twelve months that bears five months of the coupon on $31bn of debt.

### WHAT THE BUYER WOULD BE PAYING FOR, IN WORDS — written although the name does not clear, because the band's instruction was a re-run and a re-run that only produces a number is not a re-run

At $237.50 the buyer pays $195bn for: **a hosted database of other companies' customer records,
rented by the seat and billed a year in advance**, from which about 92% of contract value renews
each year and about 8% leaks away; **a narrow switching-cost moat with no demonstrated pricing
power** — price has contributed nothing to revenue growth for six consecutive years on the
company's own MD&A attribution; **a good, not great, business** that turned $79bn of deployed
capital into $10.0bn of incremental owner earnings over a decade, 12.7% pre-tax and 19.3% over
five years, at or above **[E5-40]**'s *"quite satisfactory"*; **a margin engine that is
finished**, on the company's own guidance of a flat 20.1% GAAP operating margin; **$39.5bn of
newly drawn debt** whose coupon the trailing cash flows do not yet carry; **an acquisition
programme running at $6.3bn in eight months** whose three largest predecessors each showed, in
the company's own filed pro formas, the acquisition **reducing** combined net income; and
**managers with a clean control record who are paid on numbers that appear zero times in any
filed report**, and who now describe the return on their largest capital allocation of the year
as their own share price divided by the price they paid for it. **That is the thing. The price is
above the top of its judged value.**

---
## 4. Q6 RE-READ — THE TRIPWIRES AS SET, WHAT FIRED, AND WHERE THE BANDS SHOULD SIT

*The name is not owned. Q6 remains what the 2026-09-07 run made it: a pre-committed monitoring
register **[E1-02]** — "I believe in establishing yardsticks prior to the act" — so that a future
look is judged against yardsticks set beforehand rather than yardsticks chosen afterwards.*

### WHAT FIRED

**Nothing.** The table at section 1 tests all six items set on 2026-09-07 against everything
filed since. **Three moved AWAY from reopening the name** — the confirming metric (FY2027 free
cash flow reaffirmed at roughly $15bn, about 4% growth, against a threshold of 8% for two
consecutive years), sales and marketing (34.0% against a 37% threshold, improving), and the
price (**$237.50** against *"below about $130"*). **Two are untestable until a periodic filing
arrives** — the attrition disclosure and the sales-and-marketing trend, both annual-and-quarterly
MD&A items with no new filing to carry them. **One was mis-worded when it was written**, and the
correction is below.

### THE ONE CORRECTION TO THE REGISTER AS SET **[PRIME RULE 2, operator rule 6 — corrected here, never by editing the 2026-09-07 file]**

The 2026-09-07 run's catalyst line reads: *"the **first disclosure of terms** for the Contentful
and Fin acquisitions, **neither of which is in any filing read here**."*

**That was false when written.** Both sets of terms were in the 10-Q that the same run recorded
at Step 0 as having read in full:

> *"In May 2026, the Company entered into an agreement to acquire Contentful Global, Inc.
> ('Contentful') … for approximately **$1.5 billion in cash**, net of the value of shares
> currently owned by Salesforce"* … *"In June 2026, the Company entered into an agreement to
> acquire Intercom, Inc. ('Fin') … for approximately **$3.6 billion in cash**"* — 10-Q,
> accession `0001108524-26-000190`, Note 6, *"Pending Acquisitions"*

Both have since closed — **Contentful 2026-09-01, Intercom 2026-09-10** — confirmed by the two
S-8 registrations. **The catalyst that remains real is the purchase accounting and the final ASR
settlement, both of which land in the Q3 FY2027 10-Q.** The error is recorded here rather than
edited into the prior file, and it is counted at the self-audit as a defect of that run found by
this one.

### THE REGISTER AS IT SHOULD NOW READ

**Kept unchanged, because nothing filed since touched them:**

- **Thesis-confirming (would make it wrong to have quit):** operating cash flow growth **above
  8% for two consecutive fiscal years** while GAAP operating margin holds at or above 20%.
- **Thesis-breaking:** disclosed attrition **above 9%**, or any fiscal year in which the
  attrition disclosure is **dropped or replaced with words**. Newest: *"approximately eight
  percent"* at 2026-07-31.
- **Second breaking:** **sales and marketing back above 37% of revenue.** Newest: 34.0%.
- **[E3-40] standing watch:** *"Loss of focus is what most worries Charlie and me."* A **fourth
  large acquisition** announced before the FY2030 targets are tested is the **[E4-24]** trigger.
  On the filed record the three FY2027 deals are not large — no Item 2.01 8-K, no Rule 3-05
  statements, assumed-award registrations of 0.23% of the register — but the company's own deck
  now makes M&A a named pillar (*"Acquisitions for the AI Era"*), so the watch is live.

**ADDED by this re-look, both arising from what it found:**

- **THE INTEREST TEST, and it is now the single most informative item on the register.** The
  whole verdict turns on whether the March-2026 coupon is a permanent charge against owner
  earnings or something the business absorbs. **The test: Q3 FY2027 results (late November 2026)
  are the first period in which the new stack's coupons are fully in CASH.** Compare *"Cash paid
  during the period for: Interest"* in that 10-Q against the **$153M** of Q2 FY2027 and the
  **$1,824M** annual coupon build. **If quarterly cash interest lands near $450M, the
  normalisation in section 2 is confirmed and the value range of roughly $45–210 stands.** If
  full-year FY2027 operating cash flow still reaches the guided ~$15.6bn with the coupon fully
  paid, then the interest has been absorbed out of operations and **the TTM construction's
  unadjusted 10.06% was the better estimate — in which case the file reopens on the arithmetic
  alone, and this re-look was wrong.** That is the disconfirming test for this file's own
  conclusion **[E4-26]**, and it is pre-registered here rather than left to be chosen later.
- **THE PRICING CLAIM.** The Investor Day deck lists *"Multi-Cloud Pricing & Packaging"* first
  among its growth drivers. **The test: the FY2027 10-K MD&A revenue attribution (~March 2027).
  If price appears as a named contributor to revenue growth for the first time in seven years,
  Q2's direction of "flat to narrowing" is re-tested and the moat class may move.** If it does
  not appear, the deck's first growth driver produced nothing measurable and that is a Q3 candor
  datum.

### THE SELL RULE **[E2-28]** — recorded as the standard that would apply; the name is not owned

- SELL if the market judges it more valuable than the underlying facts indicate — **this is the
  current condition**, on all forty constructions in section 2.
- SELL if funds are needed for something more undervalued or better understood — not engaged.
- HOLD while return on equity capital is satisfactory (**ten-year mean ROE 5.7%, five-year 6.5%
  — [E2-42]'s red light is on**), management is competent and honest (**no disqualifier; one
  enlarged capital-allocation flag**), and the market does not overvalue (**fails**).
- Price appreciation and holding period are explicitly rejected as reasons to sell.
- **[E2-40]** is noted for the day the view crystallizes: once it does, delay is the graver
  error. **It has not crystallized. [E4-17] and [E3-30]: the moat question is whether erosion is
  an aberrational cycle or a permanent reduction in intrinsic business value, and on today's
  evidence it is neither — attrition flat at ~8%, the core growing 8%, R&D intensity rising.
  What has changed is the growth RATE, from 24.7% to 8.4% in four years, and "those beliefs
  change quite gradually."**

### THE BANDS — one moved, one left standing with a second derivation, nothing new armed

**A band is a prompt to read, never a verdict** (`tools/alerts.json` header; operator rule 8).

| band | as armed 2026-09-07 | **proposed** | the reason |
|---|---|---|---|
| `CRM-rerun-band` | **$240** — *"the top of the value band"* | **$210** | **The $240 level has fired and produced this file, which quit on the name again. Left at $240 it re-fires on every tick below and generates re-looks whose answer is already computed.** $209 is the price at which the **most generous of forty constructions** (TTM, (c)=capex, normalised) first clears the ~10% floor. **Above $210 no construction clears and a re-run has nothing to decide; at or below it, one does.** That is the level at which a re-run can change the answer, which is the only thing a re-look band is for. |
| `CRM-ranks-band` | **$150** — *"the judged centre"* | **$150, UNCHANGED** | Its original derivation (the as-run centre, ~$150) is superseded, but the level survives on a **second, independent derivation from this file's own arithmetic: $149 is the price at which the three-year window clears the floor, normalised.** So the trigger does not move. **It is deliberately NOT tightened to the new normalised centre of ~$100**, and the reason is operator rule 9: the analyst who has just written the adjustment that keeps a name out has an incentive to set the next look further away. **Leaving it at $150 costs one extra reading and removes that incentive.** The label is updated with the new facts. |

**Nothing else is armed.** No new ticker, no new level, no second band. `PORTFOLIO.md` receives a
dated status line pointing at this file and **nothing else** — the name is not owned, its watch
row is not a holding, and this file has no authority to change it further.

---
## 5. SELF-AUDIT

*Operator rule 6: a run is incomplete until its self-audit is checked.*

- [x] **This is a re-look, and it says so in its first line.** No gate was re-opened from
      scratch; Q1–Q4 were tested only against what has been filed since 2026-09-07, and each
      gate carries an explicit statement of whether anything disturbs it. **None does.**
- [x] **The hard sequence is respected** (operator rule 2). Q5 is reported because Q1–Q4 each
      show IN — as they did on 2026-09-07 and as they still do. **No Q5 output would have been
      published had any gate fallen.**
- [x] **No question marked IN carries an "unverified", "general knowledge" or "provisional"
      caveat.** The one item this file could not resolve is named as what it is: the purchase
      accounting for Contentful and Fin. **Can I name the document that would resolve it? Yes —
      the Q3 FY2027 10-Q, due about December 2026. So it is UNRESEARCHED, not UNKNOWABLE
      [E4-19]** — and it does not bear on any verdict here, because no owner-earnings window
      contains either deal.
- [x] **The filing was read, not the tagged data** (operator rule 4). Eight filings enumerated
      with accession numbers; four read in full (the two S-8s, the Item 5.02 8-K, the Item 7.01
      8-K and its exhibit); three Form 4s parsed from their XML. **Two figures cross-checked
      against the filed statement for this file** — interest expense $(473)M for the three
      months ended 2026-07-31, and cash paid for interest $153M / $240M — both from the 10-Q,
      and both are the figures the verdict turns on.
- [x] **Strict inputs** (operator rule 5). Owner earnings never via a net-income proxy: every
      construction is built from **operating cash flow less stock compensation less (c)**.
      Sovereign for the **earnings currency**, from the **issuing authority** (US Treasury daily
      par yield curve, 30 Yr, 2026-09-18), **struck fresh and not inherited from the brief or
      the prior run**; FRED not used. Primary filings throughout; the aggregator supplies the
      live quote only and **is flagged every time it appears**.
- [x] **Owner earnings on a multi-year mean [E2-42], eight windows plus FY2026 and the TTM, and
      all four (c) ends — forty constructions, published twice** (as-run and normalised) so that
      no reader has to take the adjustment on trust.
- [x] **(c) is disclosed as a judgment** — *"(c) must be a guess"* **[E2-23 via the prior run]**
      — with the filed decomposition quoted, the direction of the choice named (it is in the
      company's favour by $2,453M a year), and the corpus-default end carried in every table.
- [x] **Value stated as a round-number range [E4-25, E4-01]:** roughly **$45 to $210, centre
      roughly $100** normalised; roughly **$80 to $240, centre roughly $133** as-run. **Where
      $237.50 sits is stated for both.**
- [x] **One bar chosen, not both** — the screamer test **[E4-01, E5-34]**. No end margin
      applied. **The windage count is published as a table, and it is net in the company's
      favour.**
- [x] **Conservatism spent once [E4-11].** One material conservative adjustment (the [E4-41]
      interest normalisation) and one immaterial one (the $42M TTM (c) rebuild), against four in
      the company's favour.
- [x] **All six Q6 tripwires tested one by one; none fired; one was found to have been
      mis-worded and is corrected in this file rather than by editing the prior one** (operator
      rule 6).
- [x] **Every ledger id checked against `principle_ledger.csv`.** **311 rows; 35 distinct ids
      cited in this file; 0 phantom.**
- [x] **`python tools/check_framework.py` → PASS.** *311 ledger rows, 311 unique ids, 310/311
      verbatim against the cited source (E5-07 is a declared non-quote), 1148 run files with 0
      phantom citations, 0 unlabelled numbers across all five governed documents.* Run **before**
      the fold commit, as the FOLD rule requires.
- [x] **The market-beating claim is not made anywhere in this file** (operator rule 7).
- [x] **Operator rule 9 applied to myself, twice and on the record:** the strongest fact against
      this file's conclusion is stated **in a block quote inside section 2, before the adjustment
      that removes it**, not buried at the end; and the `CRM-ranks-band` was **deliberately not
      tightened** to the normalised centre, because the analyst who just wrote the adjustment
      that keeps a name out has an incentive to push the next look further away.
- [x] **No buy language, no entry language, and no instruction to act.** The verdict is quit on,
      and the file arms nothing new.
- [x] **Written incrementally under the write-early protocol and committed section by section**
      with pathspec commits: `dfdbdef` (the claim), `5bf1a4a` (section 1), `abeec61` (Q5), and
      the fold commit that follows this section. The hourly wave 7 cycle shares this tree, so
      every commit carries `-- <path>`.

### THE FOUR-VERDICT LINE

| | verdict | one line |
|---|---|---|
| **Q1** | **IN** (narrow) — unchanged | Seats × price × renewal, less an ~8% leak. **The metering-unit doubt is larger: the deck's monetisation story runs on AWUs and flex credits, units in no filed report.** |
| **Q2** | **IN** — NARROW, flat to narrowing — unchanged | Attrition still *"approximately eight percent"*; the core grew 8% and the bought categories 20%. R&D intensity rose to 14.87%, recorded against my own prior. |
| **Q3** | **IN** — no disqualifier — unchanged, **flag enlarged** | The 2026-09-17 deck reports the return on a $25bn buyback as its own share quote ÷ the price paid — *"over 40%"* at 8/31, **30.5% at $237.50, on no filing and no event.** |
| **Q4** | **IN** — **GOOD** — unchanged | Interest coverage 7.30x on OCF-less-(c) reproduces exactly, **and 4.40x on GAAP operating income; both are published.** *"190% of Free Cash Flow returned in FY27"* is the [E5-39] finding in the company's own words. |
| **Q5** | **NOT IN — QUIT ON at the floor, a second time** | Expectancy **5.51%–9.65%** against ~10%; **0 of 40 constructions reach the 5.34% sovereign** (best 5.15%). Value roughly **$45–210**, price **$237.50**. |
| **Q6** | **IN** as a monitoring register | **No tripwire fired; three moved away from reopening.** One mis-worded catalyst corrected; two tripwires added, including the interest test that could refute this file. |

---
## DEFECTS FOUND — IN THE 2026-09-07 RUN, IN THE TOOLING, AND IN THIS BRIEF

*Operator rule 8: tools fetch and compute and are forbidden to conclude. Every item is a place
where something concluded and was wrong, or where a prompt-to-read did not fire.*

### A. IN THE 2026-09-07 RUN — four, and the first one decides this file

**A1 — THE INTEREST DEFECT. The run used the forward interest run-rate at Q4 and then built Q5
from cash flows that do not bear it.** At Q4 it computed *"interest coverage on OCF-less-(c)
**7.3x**"*, which is ($14,996M − $1,178M) ÷ **$1,892M** and reproduces exactly — so **the run
had the $1,892M in its hands.** At Q5 every owner-earnings construction was built from operating
cash flow, and the trailing twelve months bear **$979M accrued and $401M paid in cash** against
that $1,892M. **The most generous construction was therefore overstated by about $1.4bn a year,
and at $237.50 that is the difference between clearing the ~10% floor and missing it.** This is
not a criticism of the arithmetic the run published; every number in it is right on its own
basis. It is a missing step between two of its own sections. **Class: a figure computed at one
gate and not carried to the gate it governs.** Worth looking for in every run in this queue that
values a company which has recently levered up.

**A2 — The Q6 catalyst asserted an absence that was false.** *"the first disclosure of terms for
the Contentful and Fin acquisitions, neither of which is in any filing read here"* — both sets of
terms ($1.5bn and $3.6bn in cash) are in Note 6 of the 10-Q the same run recorded as read in
full at Step 0. **This is exactly the failure mode the v4.1 absence-claim rule exists to catch,
committed in a Q6 tripwire where the acceptance test cannot see it** (an absence claim is not a
phantom citation and not an unlabelled number). Corrected at section 4, not edited into the prior
file.

**A3 — The TTM (c) was $1,166M implied, against $1,208M rebuilt line by line** (financing-
obligation principal FY26 $584M + H1 FY27 $306M − H1 FY26 $278M = $612M, not $570M). $42M,
0.4%, against the name. Taken.

**A4 — The published centre of the value range does not reproduce from the run's own default
window.** It says *"centre ≈ $150"*; its own corpus-default five-year construction gives **$133**
and its table shows it. $150 sits between the 5-year ($133) and 3-year ($184) constructions with
no stated derivation. **Recorded, not edited** (operator rule 6) — and this file publishes $133
as the as-run centre with the arithmetic beside it.

### B. IN THE TOOLING — one unchanged, two new

**B1 — `tools/run.py` still uses `WeightedAverageNumberOfDilutedSharesOutstanding`, and for CRM
the market cap it prints is 16.2% too high.** The prior run's defect A1, unresolved. It prints
its own warning — *"a WEIGHTED AVERAGE, not a cover-page count"* — and then computes the yield
from it anyway. **Every share count in this file comes from the cover page by hand.** Re-flagged
because a defect that has survived one run's report will survive the next one's too.

**B2 — NEW. `tools/alerts.json` has no state for a band that has fired and been answered.** The
`CRM-rerun-band` at $240 fired at $237.50, this file re-ran the name, and the answer is the same
as at $259.23. **With a 24-hour cooldown and the price below the level, that band will fire again
tomorrow, and the day after, each time commissioning a re-look whose arithmetic is already on
disk.** There is no *"fired and answered at $X on DATE"* field, so a band cannot distinguish
between the first crossing of a level and the ninth. **The fix used here is to move the level
(section 4), which is a workaround, not a repair.** The repair — a resolved-at field that
suppresses a band until the price moves materially past it — **removes friction from a step
rather than adding one**, and is the class of change `CLAUDE.md` permits. Not made in this file,
because changing the alert engine is not this file's job.

**B3 — NEW. Nothing in the tooling puts accrued interest beside cash interest paid, and that
comparison decided this file.** `tools/run.py` prefills the arithmetic from the cash-flow tags;
nothing reads the debt note's principal-by-rate table, and nothing compares
`InterestExpense`-class facts against `InterestPaidNet`. Both numbers are in the filing and both
are tagged. **A prompt-to-read that printed them side by side for the newest two periods, and
said nothing more when they diverge sharply, would have got this run to the same number sooner —
which is the only test `CLAUDE.md` allows a tool to pass.** It must print and stop: the divergence
is a reason to open the debt note, never a score, and it has innocent explanations (coupon
timing) as often as not. Proposed, not built.

**B4 — no defect. `tools/sources.py` returned USD 5.34% at 2026-09-18 from the Treasury, and the
Treasury CSV fetched independently for this file agreed to the basis point.** The 2026-09-21 curve
had not posted; recorded at section 2 rather than papered over.

### C. IN THIS BRIEF — one real, two small

**C1 — The brief named the defect to look for, and it was the wrong one.** It said *"the run's
known defect class applies — acquired-intangible amortisation and lease amortisation must not sit
inside (c), as the IBM and DIS runs found."* **That class was already closed by the 2026-09-07
run**, explicitly, with the filing's own decomposition footnote quoted — so the instruction sent
this re-look to re-verify a settled question, while **the defect that actually decided the file
went unnamed.** No harm done here; it is recorded because it is the mirror of the queue's own
standing prohibition (*"NEVER TELL A RUN WHICH GATE WILL BE BORING"*, added 2026-09-07 from
CGNX). **Telling a run which defect to expect can crowd out the search for the one that matters,
for the same reason: it is a conclusion smuggled in as advice.** The right form is the evidence
and the prior, never the finding.

**C2 — The price has thinner provenance than any other input in the file.** The brief supplies
*"$237.50 (aggregator)"* with no aggregator named, no timestamp and no raw response on disk,
while operator rule 5 requires a dated source for the sovereign and an accession number for every
figure. **The price is the input the whole verdict is measured against.** It is used as given and
flagged at every appearance; a future band-fired brief should carry the quote the way the runs
carry a close — source named, time stamped, raw response written to the research folder.

**C3 — The brief asked for a re-look and got one; the deliverable list is exactly right.** It
asked for the strongest fact against the conclusion, which is the request that produced the two
grids at section 2 rather than one. **Recorded as a good brief in the one respect a brief is
usually weakest.**

---

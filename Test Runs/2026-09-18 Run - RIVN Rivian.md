# Company Run — Rivian Automotive, Inc. (RIVN) — 2026-09-18
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs. **This is a NEW NAME, not a
holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.**

Fill top to bottom. **Stop at the first verdict that is not IN.**

Run unattended from scratch on 2026-09-18 (evening, EDT); the template was copied and committed before any fetch
(`e3b4e0d`). No prior run file for RIVN exists. WAVE 5, the fourth of the seven "perimeter or restatement above
threshold" names. Research, scripts and downloaded filings are in `Test Runs/_research 2026-09-18 RIVN/`; the brief is
`_BRIEF.md` there. Sections were written as they closed and committed after each gate.

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
## STEP 0: THE SKIP REASON, THE RATE, THE PRICE, THE COUNT, THE PERIMETER, AND THE FILING

### The skip reason, tested on the filing rather than inherited
The wave 5 row is *"perimeter or restatement above threshold: read the filing first"*; the skipped-reason list
says *"revenue step or cross-accession restatement above threshold."* **A prompt to read, never a verdict.**

Reproduced by the brief-writer with `Screens/floor_screen.py` as it stood at `a8bc84f` (copied as
`floor_screen_a8bc84f.py`) over companyfacts pulled 2026-09-18 and cut to facts filed by 2026-09-01
(`triage_repro.py`, output `triage_repro_out.txt`, re-read by this run):

| guard, in order | value | fires? | what it was reacting to, on the filings |
|---|---|---|---|
| 1. `share_count_shift` | **None** | no, but only because it had nothing to compare | companyfacts carries **no dei share-count element for Rivian at all** (only `EntityPublicFloat`); a None is "not measured", not "stable". The real count moved from 1,237,077,289 Class A (FY2025 10-K cover, 2026-01-29) to 1,443,948,130 (Q2 2026 10-Q cover, 2026-07-21), **+16.7% in six months** (below). |
| **2. `scale_shift`** | **30.1455x** | **YES: THIS IS THE GUARD THAT RETURNED RIVN UNPRICED** | **A REAL STEP, AND IT IS THE START OF PRODUCTION, NOT A PERIMETER.** Revenue $55M (FY2021) to $1,658M (FY2022), on consecutive fiscal years (2021-12-31 and 2022-12-31; the TSLA check for non-consecutive years was run and the pair is consecutive). Deliveries were **920** in FY2021 and **20,332** in FY2022 (FY2023 10-K MD&A: *"Delivery volume | 920 | 20,332 | 50,122"*); the FY2021 10-K says *"the Company began making deliveries of the R1T, R1S, and EDV in the United States in 2021."* The next step, FY2022-23 **2.67x**, is the same ramp (20,332 to 50,122 deliveries). **No acquisition in any year**: the investing section of every 10-K read carries no business-combination line (FY2019-25). FY2019 and FY2020 revenue are true zeros (no product was sold), not a tag hole. |
| 3. `filed_years` | 7 | no | FY2019-25 (FY2019-20 from the FY2021 10-K, the first annual report after the November 2021 IPO) |
| 4. `owner_earnings` | 5y D&A **-$4,489M**, 5y capex **-$5,195M** | no (priced, negative) | the triage stopped at guard 2 |
| (`restatement_shift`, not a guard) | (1.0, FY2021) | n/a | a null, as at SMCI, SNOW and TSLA |

**So the label was, for RIVN: a real organic revenue step, the start of vehicle production in late 2021, measured
off a near-zero base ($55M). Not a perimeter event, not a restatement, not a tag artefact.** Checked on the documents:
the FY2025 10-K cover leaves the error-correction box unticked (*"reflect the correction of an error to previously
issued financial statements. ¨"*); the filing index (`filings_list.txt`, 531 filings) holds **no 10-K/A and no
10-Q/A**; and the FY2021-25 revenue, operating-cash, SBC, D&A and capex figures on the FY2021, FY2023 and FY2025 10-K
faces agree with companyfacts to the million. **The perimeter events that DO matter are newer than the triage's data
and run through the share count** (below), and the guard that would have seen them returned None because the dei
element does not exist.

**What the current screen says behind the label (tagged data, a prompt only):** `owner_earnings()` prices RIVN at
5y D&A end **-$4,489M**, 5y capex end **-$5,195M**; 3y -$4,122M and -$4,527M. `working_capital_flag` fires on 2024
(*"ContractWithCustomerLiability moved 94% of 2024 OCF"*) and `da_discontinuity_flag` on 2021 (D&A $29M to $197M);
both are taken up at Q4. SBC tags FY2019-20 as zero: **the face agrees** (the FY2021 10-K cash-flow statement reads
*"Stock-based compensation | — | — | 570"*), so this is not the SBC-of-zero tag defect of the RESUME STATE note; it is
pre-IPO awards whose expense was deferred until the IPO condition was met (taken up at Q4).

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by
  this run with the cache bypassed (`treasury_out.txt`: *"09/18/2026,3.97,...,5.38,5.34"*). `tools/sources.sovereign("USD")`
  returned the cached **09/17/2026 5.29%** row at 19:12 EDT (`step0_out.txt`), the stale-cache defect SNOW and TSLA
  recorded; the newer issuing-authority figure is used. FRED was not used.
- **Earnings currency: USD.** *"Rivian vehicles are manufactured in the United States and are sold directly to
  consumer and commercial customers"* (Q2 2026 10-Q Note 1); the FY2023 10-K: *"The Company's assets and revenues are
  primarily in the United States."* The quote is in dollars. No FX or ADR conversion applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$14.99, the close of 2026-09-18** (Friday). Source: Yahoo Finance daily chart via `sources._chart("RIVN",
  rng="1mo", max_age_h=0)` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`). Bar: open 15.445,
  high 15.645, low 14.91, close 14.99, volume 37.1M; `regularMarketTime` 1789761600 = 16:00 EDT, so the figure is the
  closing print. `tools/sources.price()` returned the same 14.99 stamped 2026-09-18.
- Recent closes: 09-11 $16.03 · 09-14 $15.86 · 09-15 $15.54 · 09-16 $15.23 · 09-17 $15.40 · 09-18 $14.99. One-month
  range of closes $14.99-$16.97.
- **Primary-filing cross-check of the aggregator:** Form 4 accession `0001262742-26-000014` (Michael John Callahan)
  reports a 10b5-1 sale of 15,000 shares on **2026-09-11 at a weighted $16.2927** (*"prices ranging from $16.175 to
  $16.52"*), inside Yahoo's 09-11 bar (low $16.01, high $16.81); Form 4 `0001890925-26-000025` (Claire McDonough, CFO)
  reports a sale on 2026-08-20 at $16.00, inside that day's bar ($15.54-$16.18). **Corroborated.**
- **The latest primary prices for issuance sit beside it:** the July 2026 underwritten offering at **$15.50** (10-Q Note
  14), Volkswagen's April 2026 tranche at **$15.90** and Uber's May 2026 purchase at **$15.34** (30-day VWAPs, Note 1).
- **Split factor after the count's date: 1.0** (`sources.split_factor_after("RIVN", "2026-07-21")`). `close` used, never
  `adjclose`.

### The share count: from the cover, with the accession, and the classes read before summing
- **1,447,860,630 shares** = **1,443,948,130 Class A + 3,912,500 Class B**, from the cover of the **Q2 2026 Form 10-Q**
  (quarter ended 2026-06-30, filed **2026-07-30**, accession **`0001874178-26-000054`**): *"As of July 21, 2026,
  1,443,948,130 shares of the registrant's Class A common stock were outstanding, and 3,912,500 shares of the
  registrant's Class B common stock were outstanding."* `Screens/cover_shares.py` was not needed: companyfacts carries no
  dei count, so the cover was read directly.
- **Why the two classes are summed (the charter terms as the 10-Q states them, Note 14):** *"Shares of Class A common
  stock and Class B common stock are identical, except with respect to voting and conversion rights"*; *"the rights of the
  holders of Class A and Class B common stock, including liquidation and dividend rights, are identical"*; every Class B
  share *"will automatically convert into one share of Class A common stock upon the earliest to occur of (a) the
  five-year anniversary of the Company's IPO (i.e., November 2026)"*. The CEO holds all 3,912,500 Class B shares (2026
  proxy, `0001874178-26-000023`). Same economic claim, so the sum is the count.
- **The cover already includes the July 2026 offering**: 75M shares plus the 11.25M option, at $15.50, net proceeds
  about $1,317M (10-Q Note 14, *"On July 7, 2026, the Company entered into an underwriting agreement ..."*); 1,362M at
  June 30 plus 86.25M is 1,448M.
- **Instruments outside the cover count, at $14.99, stated either way:**
  1. **Green Convertible Notes, 149M shares if converted** (2029: $1,500M at $20.13; 2030: $1,725M at $23.29, with
     capped calls). **Out of the money at $14.99; excluded**, and carried as debt at Q4.
  2. **Employee awards:** RSUs 85M (unvested, the future SBC charge), options 77M (weighted exercise $12.35 at
     2025-12-31), warrants 12M (Note 14's anti-dilution table: 327M potential shares in total with the converts).
     Unvested RSUs belong to future SBC, which Q4 subtracts; not added to the count.
  3. **Volkswagen's last equity tranche**: *"$ 460 million in exchange for $ 250 million of the Company's Class A common
     stock"* at a 30-day VWAP, due at the Start of Production Milestone or 2028-01-03 (about 16.7M shares at $14.99).
     The other $210M is booked as JV revenue (Note 3). **Not yet issued; excluded.**
  4. **Uber**: up to **$950M** more across four milestones, *"certain of which require the fulfillment of proven autonomy
     quality"*, paid in **$0.001 warrants or shares** at a 30-day VWAP (about 63M shares at $14.99 if all are met).
     **Contingent; excluded, and recorded at Q3 as serial issuance.**
- **The count moved +16.7% in six months** (1,240,989,789 across both classes at 2026-01-29 to 1,447,860,630 at
  2026-07-21), all by issuance: VW 63M, Uber 20M, the offering 86.25M, employees the rest.

### The perimeter between the business and the common holder: stated, not blended
1. **Cash and short-term investments at 2026-06-30: $5,310M** ($3,592M cash, $1,718M short-term), plus about **$1,317M**
   net from the July offering (after the balance-sheet date). **Debt principal $4,475M**: 2029 convertible $1,500M,
   2030 convertible $1,725M, 2031 Green Secured Notes $1,250M at 10% (*"secured ... on a first-priority basis by
   substantially all assets"*). Nothing drawn on the $1,500M ABL (availability $536M). Net cash before the offering
   about $0.8bn; after it about $2.2bn.
2. **Undrawn government and partner loans:** the DOE loan, amended April 2026, up to **$3,355M plus $315M capitalised
   interest (Note A) and $651M plus $179M (Note B)** for the Georgia plant, conditional on, among other things, *"the
   Sponsor maintaining positive gross margin for certain periods prior to the first advance"* and *"the Borrower
   achieving certain vehicle sales metrics"*; and Volkswagen's **$1,000M** term loan, drawable **2026-10-01 to
   2026-10-30** only. **Neither is drawn**; both are taken up at Q4.
3. **A 50% partner inside the consolidated revenue.** Rivian and Volkswagen Group Technologies, LLC is consolidated,
   with Volkswagen's 50% shown as a noncontrolling interest; it produced **$590M of H1 2026 revenue** and most of the
   gross profit (Q1). **Strategic investments $697M**, of which Mind Robotics was remeasured to $569M on deconsolidation
   (a **$506M non-cash gain** in Q1 2026 other income); Also, Inc. at 35.3%.
4. **Holders who are also counterparties:** Amazon (12.9%, 162.1M shares incl. a warrant, 2026 proxy) is the EDV
   customer; Volkswagen (15.9%, 209,769,645 shares, Schedule 13G/A `0001104659-26-054713`, event 2026-04-30) is the JV
   customer and a lender; Uber is a subscriber and robotaxi partner.
5. **No live deal.** `sources.deal_filings("0001874178")` returned no merger filing and two 8-K Item 1.01s since the
   last annual (2026-03-19, the Uber subscription; 2026-04-30, the amended DOE agreement); no SC 13D, SC TO, S-4 or
   DEFM14A in the filing index (Volkswagen and Amazon file 13Gs). The quote is an owner-earnings price, not a spread.

### The market cap
- **$14.99 x 1,447,860,630 = US$21,703M ($21.7bn).** Split factor after 2026-07-21 = 1.0.
- Net cash of about $2.2bn after the July offering (about 10% of the cap) is shown, not netted.

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2025 Form 10-K**, fiscal year ended 2025-12-31, filed **2026-02-12**, accession **`0001874178-26-000008`**
  (`10K_FY2025.txt`); auditor **KPMG LLP**, Detroit, report dated February 12, 2026, unqualified, internal control
  effective, *"We have served as the Company's auditor since 2021."* Critical audit matter: the warranty reserve
  ($463M), *"due to the Company's limited history of vehicle sales."*
- **Q2 2026 Form 10-Q**, quarter ended 2026-06-30, filed **2026-07-30**, accession **`0001874178-26-000054`**; Q1 2026
  10-Q `0001874178-26-000035`.
- Also read: 10-Ks FY2024 (`0001874178-25-000007`), FY2023 (`0001874178-24-000014`), FY2022 (`0001874178-23-000009`),
  FY2021 (`0001874178-22-000008`, which carries FY2019-20); the 2026 DEF 14A (`0001874178-26-000023`, filed 2026-04-27);
  the 8-K EX-99.1 releases named at Q3; Schedule 13G/As; and the Form 4s above. The IPO prospectus is the 424B4 of
  2021-11-12 (`0001193125-21-328239`); the FY2021 10-K states the IPO (*"approximately 176 million shares of Class A
  common stock at a public offering price of $ 78.00 per share"*, November 2021), which settles the brief's first
  unverified belief.
- **Figures cross-checked against the filed statement** (FY2025 consolidated statement of cash flows): *"Net cash used
  in operating activities | ( 4,866 ) | ( 1,716 ) | ( 779 )"*, *"Stock-based compensation expense | 821 | 692 | 741"*,
  *"Capital expenditures | ( 1,026 ) | ( 1,141 ) | ( 1,710 )"* and *"Depreciation and amortization | 937 | 1,031 | 784"*
  match companyfacts to the million. **SBC is complete on the face**: the FY2025 MD&A allocates it $43M + $68M + $306M
  + $324M = $741M across cost of revenues, R&D and SG&A, and no capitalised SBC is disclosed.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### The unit economics, in my own words, without management's language
Rivian builds battery-electric pickups and SUVs (R1T, R1S, and since June 2026 the smaller R2) and delivery vans in one
plant it owns in Normal, Illinois, and sells them itself: the consumer vehicles online and through its own showrooms,
about a third of them through one bank that buys the car and leases it to the driver (*"approximately 37 % and 36 %,
respectively, of the Company's revenues were from new EV sales to Chase Bank"*, FY2025 10-K Note 4), and the vans
mostly to Amazon ($900M of FY2025 revenue; $1,022M in H1 2026, 10-Q Note 12). **It has never sold a vehicle for more
than the vehicle cost to build.** Beside the vehicles it sells three smaller things: **regulatory credits** (permissions
other carmakers buy because the rules fine fleets that pollute), **used cars, repairs and software subscriptions**, and,
since November 2024, **engineering work for Volkswagen** through a 50/50 joint venture that Rivian consolidates: Volkswagen
paid $1,295M for a licence to Rivian's electrical architecture and software and pays most of the joint venture's
development fees, and Rivian books that money as revenue as the work is done (*"over approximately 2.5 years"* from
2025-12-31, FY2025 10-K Note 4).

From the filed faces (FY2021, FY2023 and FY2025 10-Ks; segment note FY2025 Note 18; Q2 2026 10-Q Note 15), $M
(`q1.py`, `q1_out.txt`):

| line | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---:|---:|---:|---:|---:|---:|
| Deliveries (MD&A) | 920 | 20,332 | 50,122 | 51,579 | 42,247 | 22,559 |
| Total revenues | 55 | 1,658 | 4,434 | 4,970 | 5,387 | 3,039 |
| Automotive revenue (incl. credits) | | | 4,132 | 4,486 | 3,830 | 2,051 |
| of which regulatory credits (Note 4) | 0 | 0 | 73 | 333 | 197 | 167 |
| Automotive cost of revenues | | | 6,150 | 5,693 | 4,262 | 2,149 |
| **Automotive gross profit** | | | **(2,018)** | **(1,207)** | **(432)** | **(98)** |
| automotive gross profit per vehicle delivered ($000) | | | (40.3) | (23.4) | (10.2) | (4.3) |
| automotive revenue per vehicle ($000) | | | 82.4 | 87.0 | 90.7 | 90.9 |
| automotive cost per vehicle ($000) | | | 122.7 | 110.4 | 100.9 | 95.3 |
| Software and services revenue | | 104 | 302 | 484 | 1,557 | 988 |
| of which Volkswagen joint-venture services | | | 0 | 73 | 836 | 590 |
| Software and services gross profit | | | (12) | 7 | 576 | 396 |
| **Consolidated gross profit** | **(465)** | **(3,123)** | **(2,030)** | **(1,200)** | **144** | **298** |
| **Loss from operations** | **(4,220)** | **(6,856)** | **(5,739)** | **(4,689)** | **(3,585)** | **(1,717)** |

(FY2021-22 were reported as one segment; the per-vehicle rows start in FY2023, the first year with segment data.)

Read as a car maker that also sells engineering to another car maker:
1. **Every vehicle has been sold at a loss, and the loss is narrowing.** Automotive gross loss per vehicle delivered
   went from about $40k (FY2023) to about $10k (FY2025) and about $4k (H1 2026), because the cost per vehicle fell
   faster than the price rose (the FY2025 MD&A: *"primarily due to the higher average selling prices and reductions in
   the cost per vehicle"*). Without the credits the automotive gross loss is $629M in FY2025 and $265M in H1 2026.
2. **Consolidated gross profit turned positive in FY2025 ($144M) only because of the Volkswagen work.** Software and
   services earned $576M of gross profit in FY2025, and $836M of that segment's $1,557M revenue was joint-venture
   service for Volkswagen, much of it paid in advance in cash in November 2024 and June 2025 (Q4 takes up the cash).
   The company's own words on when that stops: *"we may experience a reduction during 2028 upon the expected
   satisfaction of the Joint Venture's combined performance obligation"* (FY2025 10-K MD&A).
3. **Fixed costs are carried by a plant built for far more than it makes.** *"Our manufacturing facility in Normal,
   Illinois ("Normal Factory") is operating significantly below full vehicle production rate capacity. This lower
   utilization of plant capacity results in the cost of revenues to operate the plant being much higher per unit of
   production than would be the case if we were manufacturing at capacity"* (Q2 2026 10-Q MD&A). The plant was
   *"equipped to produce up to 150,000 vehicles annually"* (FY2023 and FY2024 10-Ks) and produced **57,232, 49,476 and
   42,284** vehicles in FY2023-25 (38%, 33% and 28%); the 2025 paint-shop upgrade for R2 raised the stated capacity to
   215,000.
4. **Below gross profit the business loses about $3.6bn a year** (FY2025), R&D $1.67bn and SG&A $2.06bn, and it has
   lost money at the operating line in every year it has existed (FY2019-25 and H1 2026).
5. **The demand is partly bought by government programmes.** The federal 45W commercial-vehicle credit ended on
   2025-09-30, and FY2025 deliveries fell 18% *"due in part to the expiration of 45W tax credits after September 30, 2025"*
   (FY2025 10-K MD&A); regulatory credits *"have been or may be modified or are being phased out"* (Q2 2026 10-Q Note 3).

### The scarce input this business controls
**Not the plant and not the product category**: every maker in the automaker row built for TSLA and TM builds battery
vehicles in owned plants, and Rivian's 10-K says so (*"we are competing for sales with both EV manufacturers and
traditional automotive companies ... Many of our current and potential competitors have significantly greater
financial, technical, manufacturing, marketing, or other resources than we do"*, Item 1A). **The one input the filings
show someone else paying for is the electrical architecture and software**: Volkswagen paid $1,295M for a licence to
it, a further $250M on a milestone, and has bought 209.8M shares (15.9%) alongside; but that asset now sits in a
joint venture Rivian owns half of, and the 10-K names the cost: *"through the creation of the Joint Venture, the
electrical architecture and vertically integrated software used in our vehicles will be integrated into vehicles
outside of Rivian, which could negatively impact our ability to compete."* Whether any of this is a position is Q2's
question.

### Will the fundamentals look broadly the same in ten years?
**The company says the business it has is not the business it is building.** The FY2025 MD&A: *"we expect automotive
gross profit losses to continue improving over time through the expected margin profile of R2"*; the Q2 2026 10-Q:
*"We believe R2 and our midsize platform will be foundational to our long-term growth and profit potential"*; a second
plant in Georgia is under construction for the midsize platform; and the Uber agreement commits Rivian to design and
build **robotaxis** *"based on the Company's R2 platform, equipped with the Company's Level 4 autonomous driving
system"* (10-Q Note 1). The joint-venture revenue is scheduled to fall in 2028.

**The mechanism, as a mechanism, will look the same**: build a vehicle in an owned plant and sell it for cash or to a
leasing bank. That is the whole of automotive revenue in every 10-K on disk (FY2021-FY2025).

**The honest limit, stated rather than smoothed.** [E3-31] asks for businesses *"relatively simple and stable in
character"*. I can say exactly how Rivian's money moves today: it loses a little on every vehicle and a great deal on
the engineering and selling above it, and it is paid in advance for engineering by a partner. **I cannot say from any
filing how it will make money**, because no filed period shows R2's unit economics (external deliveries began on
2026-06-09, Q2 2026 Earnings Presentation, 8-K `0001874178-26-000053`, and the quarter carried *"approximately $100
million in incremental cost of revenues due to the ramp of R2 production"*), and no filing shows the economics of a
robotaxi, of Autonomy+, or of the equity-accounted robotics and micromobility companies (Mind Robotics, Also). Those are
outside the circle, as TSLA's AI businesses were, and [E4-46] says months of study would not repair it. **But the
question Q1 asks, how this business makes money, has an answer on the filings: it does not yet, and the reasons are
legible.** A loss-making car maker is understandable as a car maker; whether it can ever earn a return against its
competitors is Q2's question and whether it lives to try is Q4's.

- **VERDICT: [x] IN** on the business the filings show (vehicles, regulatory credits, the Volkswagen engineering work,
  used cars, service and subscriptions: the whole of disclosed revenue): the unit economics are stated above from the
  filed statements in my own words and reconcile to the faces of the FY2021, FY2023 and FY2025 10-Ks and the Q2 2026
  10-Q. **Not IN** for R2 as a profit case, the robotaxi programme with Uber, Autonomy+ as a business, Mind Robotics and
  Also, none of which has a filed period of unit economics; they are recorded as outside the circle [E3-31, E4-46] and
  **cannot be counted at any later gate**, including Q5.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

### WHAT IS BEING TESTED
The business Q1 found understandable: vehicles (automotive segment, $3,830M of FY2025 revenue with credits inside it)
and the Volkswagen engineering work, used cars, service and subscriptions (software and services, $1,557M). R2 as a
profit case, the robotaxi programme, Mind Robotics and Also are outside the circle (Q1) and cannot supply the moat here.
**The hypothesis to be refuted, at full strength [E4-26, E4-51]**: Rivian owns something rivals pay for, a vehicle
electrical architecture and software stack that Volkswagen licensed for $1.3bn and backed with equity and loans; a
premium brand whose average selling price rose while discounting fell; and a fleet customer, Amazon, running more
than 40,000 of its vans; and its losses are the start-up cost of a position, not the absence of one.

### THE CASE FOR, AT FULL STRENGTH
1. **A rival paid for the technology.** Volkswagen paid $1,295M for a licence to *"Rivian's existing vehicle
   electrical architecture and software technology"*, $250M on a milestone, and about **$2.75bn of cash for 209.8M shares** in three
   steps (a $1,000M note converted in December 2024, $750M in June 2025, $1,000M at $15.90 in April 2026), with a further $460M and a $1,000M loan committed (10-Q Notes 1
   and 3; Schedule 13G/A `0001104659-26-054713`). Software and services gross margin was **42%** in Q2 2026 (Q2 2026
   Earnings Presentation, 8-K `0001874178-26-000053`).
2. **Price rose while discounting fell.** FY2025 MD&A: *"higher average selling prices and a higher mix of R1
   deliveries. The increase in average selling prices was driven by a consumer shift towards higher performance
   variants along with a decline in discounting."* Automotive revenue per vehicle delivered **$82.4k, $87.0k, $90.7k**
   (FY2023-25).
3. **The cost gap is closing fast.** Automotive cost per vehicle **$122.7k to $95.3k** (FY2023 to H1 2026) and the
   automotive gross loss per vehicle **$40.3k to $4.3k** (Q1).
4. **A large fleet customer.** Amazon has *"over 40,000 Rivian Electric Delivery Vans"* on the road (Q2 2026 Earnings
   Presentation) and *"has ordered an initial volume of 100,000 EDVs globally, subject to modification"* (10-Q MD&A);
   Amazon revenue $900M in FY2025 and $1,022M in H1 2026.
5. **Better than the nearest start-up rival on every line in the row below**, and roughly level with the EV unit of
   Ford, an incumbent with a century of manufacturing.

### THE THREE CONDITIONS **[E3-03]**
- **(1) Needed or desired: YES.** 42,247 vehicles delivered in FY2025; about 187,759 cumulatively by Q2 2026.
- **(3) Not subject to price regulation: YES for the vehicle; but part of the price and part of the cost are set by
  governments.** Regulatory credits ($197M FY2025, $167M H1 2026) exist only because rules fine polluting fleets and
  are being withdrawn (*"Many of the programs governing such tradable credits have been or may be modified or are being
  phased out"*, 10-Q Note 3); cost of revenues is reduced by *"refundable manufacturing-related tax credits accounted
  for as government grants"* (FY2025 10-K Note 2, amount not separately disclosed); and a third of revenue went through
  one bank's lease channel while the federal 45W commercial-vehicle credit was available; it ended on 2025-09-30 and
  deliveries fell (below). **[E2-59]**: where
  administered prices or costs carry the economics, the escape *"belongs to the regime"*.
- **(2) No close substitute: NOT SHOWN, AND CONTRADICTED IN RIVIAN'S OWN FILINGS.**
  - **The company says its customer has substitutes and its rivals are stronger.** *"Both the automobile industry
    generally, and the EV segment in particular, are highly competitive, and we are competing for sales with both EV
    manufacturers and traditional automotive companies, including those who have or have announced consumer and
    commercial vehicles that may be directly competitive to ours, as well as pre-owned vehicle dealers. Many of our
    current and potential competitors have significantly greater financial, technical, manufacturing, marketing, or
    other resources than we do"* (FY2025 10-K Item 1A). Item 1: *"Our competition includes the millions of traditional
    internal combustion engine ("ICE") vehicles and EVs sold each year in the consumer and commercial markets."*
  - **The demand record shows the customer treats them as substitutes when the subsidy goes.** FY2025 deliveries fell
    **18%** (51,579 to 42,247), *"due in part to the expiration of 45W tax credits after September 30, 2025"* (FY2025 10-K
    MD&A); Q4 2025 deliveries were 9,745 against 14,183 a year earlier (8-K EX-99.1 of 2026-02-12, `0001874178-26-000007`).
    A product with no close substitute does not lose a fifth of its unit volume when its buyers lose a credit that the
    FY2024 10-K put at *"between $7,500 and $40,000"* a vehicle.
  - **The price rise of 2022 was a publicity event, not a franchise event.** FY2022 10-K: *"we have increased, and may
    need to continue to increase, the prices of our vehicles in response to these and future cost pressures. Price
    increases and other measures taken by us to offset higher costs could materially and adversely affect our reputation
    and brand, result in negative publicity and loss of customers and sales"*; FY2021 10-K: *"if incidents occur or are
    perceived to have occurred, such as production delays and price increases ... we have in the past and could in the
    future be subject to adverse publicity."* That is **[E4-37]**'s agony end: *"not a great business when you have to
    have a prayer session before you raise your prices a penny."*
  - **The fleet customer is not captive.** *"The EDV Agreement is non-exclusive for Logistics, and Logistics has
    purchased and may continue to purchase EVs, including last mile delivery vehicles, from other manufacturers"*;
    *"it does not include any minimum purchase requirements"* (FY2025 10-K Item 1A). The exclusivity that ran the other
    way (Rivian could not sell vans to anyone else) was loosened in November 2023, with fees to Amazon on third-party
    van sales for five and ten years from 2024-01-01 (2026 proxy, `0001874178-26-000023`).
  - **The one asset a rival paid for is now shared with that rival.** The 10-K: *"through the creation of the Joint
    Venture, the electrical architecture and vertically integrated software used in our vehicles will be integrated into
    vehicles outside of Rivian, which could negatively impact our ability to compete."* Rivian owns 50% of the joint
    venture, and Volkswagen, with the larger vehicle portfolio, will carry the architecture across *"multiple brands"*
    (10-Q MD&A).

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4)*
**Rivian, Lucid, Tesla, GM and Ford recomputed here from their own 10-K faces** (`row.py`, `row_out.txt`): Rivian's
FY2021, FY2023 and FY2025 10-Ks (Step 0); Lucid Group 10-Ks FY2025 (`0001628280-26-011053`), FY2023
(`0001628280-24-007209`) and FY2021 (`0001628280-22-004253`), fetched by this run into `peers/`; Tesla FY2025
(`0001628280-26-003952`) and FY2023 (`0001628280-24-002390`) 10-Ks as downloaded by the TSLA run; GM FY2025
(`0001467858-26-000013`) and FY2023 (`0001467858-24-000031`) and Ford FY2025 and FY2023 10-Ks as downloaded by the TM
run (`Test Runs/_research 2026-09-13 TM/peers/`), each figure re-read from the income statement or segment note text.
**Toyota, Honda, Stellantis, Volkswagen and Hyundai are carried from the TM run's accessioned row without recomputation**
(transcription, a prompt; their accessions are in that file). Same window, calendar 2021-25.

| GAAP operating margin, % | CY21 | CY22 | CY23 | CY24 | CY25 | 5-yr pooled | measure · source |
|---|---:|---:|---:|---:|---:|---:|---|
| **RIVIAN** | **(7,673)** | **(413.5)** | **(129.4)** | **(94.3)** | **(66.5)** | **(152.0)** | loss from operations / total revenues · Rivian 10-Ks |
| Rivian gross margin | (845.5) | (188.4) | (45.8) | (24.1) | 2.7 | | gross profit / revenue; FY2025 positive only on JV services |
| Lucid Group | (5,645) | (426.5) | (520.7) | (373.9) | (258.7) | (405.2) | loss from operations / revenue · Lucid 10-Ks |
| Lucid gross margin | (471.3) | (170.7) | (225.2) | (114.3) | (92.8) | | revenue less cost of revenue |
| Ford Model e (EV segment) | | | (73.2) | (124.1) | (67.1) | (82.5), 3 yrs | segment EBIT / segment revenue · Ford FY2025 10-K segment note |
| Tesla consolidated | 12.1 | 16.8 | 9.2 | 7.2 | 4.6 | 9.5 | income from operations · Tesla 10-Ks |
| GM consolidated | 7.3 | 6.6 | 5.4 | 6.8 | 1.6 | 5.4 | operating income, incl. GM Financial · GM 10-Ks |
| Ford consolidated | 3.3 | 4.0 | 3.1 | 2.8 | (4.9) | 1.5 | operating income/(loss) · Ford 10-Ks |
| Toyota automotive | 7.99 | 6.45 | 11.20 | 9.12 | 6.11 | 8.22 | TM run row, not recomputed |
| Stellantis (vehicle segments, AOI) | 12.54 | 13.67 | 13.65 | 5.90 | 0.49 | 9.61 | TM run row, not recomputed |
| Honda automobile | 2.52 | (0.15) | 4.07 | 1.69 | (9.96) | (0.62) | TM run row, not recomputed |
| BYD | not pulled | | | | | | TM run: obstacle recorded; not re-attempted |

| Other same-window facts | Rivian | Lucid | Ford Model e |
|---|---|---|---|
| Revenue CY25 | $5,387M | $1,354M | $7,166M |
| Operating (or segment) loss CY25 | $(3,585)M | $(3,502)M | $(4,806)M |
| Pre-tax return on capital employed net of cash (`roc_out.txt`) | **(117)% / (86)% / (70)%** FY2023-25 | | |
| Stockholders' equity | $13,799M (2022) to $4,594M (2025); refilled by issuance ($750M VW in 2025; $1,000M VW, $300M Uber and $1,317M net in the July offering in 2026) | | |

- **Peers taken: 11** (Lucid, Ford's Model e segment, Tesla, GM, Ford, Toyota, Stellantis, Honda, Volkswagen and Hyundai
  in the TM row, and BYD named and not pulled), of an industry whose competitors are, in Rivian's words, *"the millions of
  traditional internal combustion engine ("ICE") vehicles and EVs sold each year"*. Seven are complete from SEC filings;
  **BYD is not pulled** (the TM run's recorded obstacle, not re-attempted). **Can I name the document? Yes: BYD's 2025
  annual report on HKEXnews.** It is a work order for any future upgrade and not for this verdict, for the TSLA and FLNC
  runs' directional reason: an absent low-cost rival can only make the attack stronger; it cannot rescue a franchise
  that the row and Rivian's own words already refute.
- **The row's limit [E3-61]:** it shows position, not conduct.

**WHAT THE ROW ESTABLISHES, in both directions.**
1. **Rivian beats Lucid on every line and is level with Ford's EV unit, and that is said first [E4-26].** Its FY2025
   operating margin (-66.5%) is a third of Lucid's (-258.7%) and about Ford Model e's (-67.1%); its gross margin crossed
   zero in FY2025 while Lucid's was -92.8%.
2. **But being the best of the loss-makers is not a position; every profitable maker in the row is a volume maker**:
   Tesla at about 1.64 million battery vehicles a year (and 4.6% in FY2025, falling), the rest with combustion
   businesses that carry their EV losses. The two filers that sell only battery vehicles at under 100,000 units a year
   lost 67 and 259 cents of operating profit on each dollar of FY2025 revenue; Ford loses the same on its EV segment and
   pays for it from Ford Blue and Ford Pro. **No filer in the row shows a battery-vehicle business earning a return at
   Rivian's scale.**
3. **Return on capital, from the balance sheet [E3-46]**: pre-tax return on capital employed net of cash **-117%,
   -86%, -70%** (FY2023-25). *"The best businesses ... earn very high returns on capital employed over time"*; this one
   has not earned a positive return in any year, and equity fell from $13.8bn to $4.6bn in three years before being
   refilled by issuance.

### THE OTHER Q2 TESTS
- **[E3-43], the franchise demonstration, fails on both legs**: the three conditions *"will be demonstrated by a
  company's ability to regularly price its product or service aggressively and thereby to earn high rates of return on
  capital."* Neither is on the record.
- **The two-characteristic test [E2-44], both legs fail.** (1) Price rises *"even when product demand is flat and
  capacity is not fully utilized"*: FY2025 did raise the average selling price with the plant producing 42,284 vehicles against
  a stated capacity of *"up to 150,000 vehicles annually"* (FY2023 and FY2024 10-Ks; 215,000 after the 2025 paint-shop
  upgrade for R2), and lost 18% of unit volume in the same year; a price rise that sheds volume is the case the test excludes (*"without fear
  of significant loss of either market share or unit volume"*). (2) Growth *"with only minor additional investment of
  capital"*: capital expenditure **$1,794M, $1,369M, $1,026M, $1,141M, $1,710M** (FY2021-25) on revenue of $5.4bn, a
  second plant under construction in Georgia with a DOE loan of up to $4.5bn arranged for it, and 2026 capex guided at
  **$1.70-1.80B** (8-K EX-99.1 of 2026-07-30).
- **Untapped pricing power [E3-33]: none**; **[E5-28]** scopes the claim to near-monopoly, which the row refutes.
- **The attacker's test [E2-45]:** with ample capital and skilled people, how would one compete with Rivian? The
  filings say it is being done by stronger firms (*"significantly greater financial, technical, manufacturing,
  marketing, or other resources"*), and Rivian has itself handed its best-evidenced asset, the architecture, to a
  rival with a larger vehicle portfolio.
- **Direction [E4-32] and units [E4-55]: units narrowing, cost gap narrowing.** Deliveries 50,122, 51,579, 42,247
  (FY2023-25), recovering in H1 2026 (22,559, +17%) on vans and R2; the cost per vehicle fell faster than price rose.
  The physical series says demand has not grown for three years at the subsidised price and fell when the subsidy went.
- **[E4-04], and the [E5-23] test (does the spending defend the same advantage or buy its replacement?)**: **it buys
  its replacement, repeatedly, on the company's own record.** The R1 line was retooled in Q2 2024, about two and a half
  years after the start of production, with *"accelerated depreciation that occurred during the prior year"* (FY2025 10-K
  MD&A; automotive D&A $740M in FY2024 against $484M in FY2025); the R2 on a new *"midsize platform"* followed two years
  later with *"Significant capital expenditures ... required to support the integration of R2 into our Normal Factory"*;
  a second plant is being built for the same platform; and the company says future share depends on *"advanced assisted
  driving capabilities"* (Q2 2026 Earnings Presentation). That is **[E4-04]**'s *"industries prone to rapid and
  continuous change"*, named by the company. *(The TSMC corpus tension against [E4-04], raised at the 2023 meeting, is
  an OPEN operator question; v4 is applied as written and the tension is noted, not resolved.)*
- **The four causes of extreme success [E4-36] and the surfing run [E3-51]:** none of the four is on the record; there
  has been no success to explain.
- **Key-person dependence, recorded here as a MOAT DEFECT [E4-23]:** *"We are highly dependent on the services and
  reputation of Robert J. Scaringe, our Founder and CEO. Dr. Scaringe is a significant influence on and driver of our
  business plan and product development roadmap. If Dr. Scaringe were to discontinue his service due to death,
  disability or any other reason ... we would be significantly disadvantaged"* (FY2025 10-K Item 1A). The 10-K adds that
  he chairs Also and Mind Robotics, which *"may compete with his ability to devote a sufficient amount of attention"*.
  *"If a business requires a superstar to produce great results, the business itself cannot be deemed great."*
- **The software and services segment, separately:** its gross profit is real and its margin (42% in Q2 2026) is the
  best line in the file, but $836M of its $1,557M FY2025 revenue is one related-party contract, prepaid, recognised
  over *"approximately 2.5 years"* and expected to fall *"during 2028"*. A contract with a stated end is not a franchise;
  **at most a narrow, PROVISIONAL position in the architecture, 50% of it now held with Volkswagen**. It cannot make the
  whole a franchise: the automotive segment is 71% of FY2025 revenue and has never earned a gross profit.

### CLASS AND VERDICT
- **Class: [ ] WIDE [ ] NARROW [x] NONE for the business as constituted [ ] PROVISIONAL · Direction: losses narrowing,
  units flat to down, position not shown** (automotive: none; software and services: a narrow, provisional position in
  a shared architecture, carried by a contract that ends).

**VERDICT: [ ] IN  [x] OUT**  [ ] UNRESEARCHED  [ ] UNKNOWABLE

**OUT on [E3-03] criterion (2), named precisely: the customer has close substitutes, which Rivian's own 10-K names
(*"highly competitive"*, competitors with *"significantly greater financial, technical, manufacturing, marketing, or
other resources"*), and the proof that the customer treats them as substitutes is in the unit record: deliveries fell
18% in FY2025, in the company's words partly on the expiry of the 45W credit, after three years of flat volume.
Compounded by: no return on capital in any year (pre-tax ROCE -117%, -86%, -70% FY2023-25) and no filer in the
eleven-peer row showing a battery-vehicle business earning a return at this scale [E3-46, E3-43]; both legs of the
two-characteristic test fail, a 2022 price rise recorded as a publicity risk and a 2025 one that shed a fifth of unit
volume [E2-44, E4-37]; credits, a manufacturing tax credit and a lease subsidy administered by governments inside the
price and the cost [E2-59]; a platform replaced about every two to three years, the company buying its replacement
rather than defending a standing advantage [E4-04, E5-23]; and a 10-K that says the plan depends on the founder
[E4-23].** *Evidence is in and the business fails the test; this is a finding about the business as constituted, not
about the price and not about R2 or the robotaxi programme, which Q1 placed outside the circle and which therefore
cannot be scored as a moat here.* **Can I name a document that would reverse it? No filing now on file could**: a
reversal would need a record not yet made (Q6 states it in words).

*The file closes here. Q3, Q4, Q5 and Q6 below are RECORDED, NOT GOVERNING, as at SMCI, SNOW, TSLA and the other Q2
closes in wave 5.*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT, on the business). This section is written because the
> brief asked for Q3 with the 8-K EX-99.1 releases and the proxy, and because what it finds belongs in the Q6
> reopening conditions. Nothing here can promote the name or repair Q2 **[E2-37, E2-38, E3-39]**.

### STEP 1 - THE WEIGHT CASE
- [x] **Daily execution** **[E3-38]**: a sub-scale car maker launching a new platform in an owned plant is
  have-to-be-smart-every-day: the R2 ramp alone carried *"approximately $100 million in incremental cost of revenues"*
  in one quarter (Q2 2026 Earnings Presentation), and Q2 found no franchise to stand a mistake **[E3-43]**: *"a
  business, unlike a franchise, can be killed by poor management."*
- [ ] **Control** **[E1-16]**: a minority purchase of a listed share.
- [ ] **Leverage** **[E3-29]**: net cash of about $2.2bn after the July offering; the debt is named at Q4.

**Case declared: a BINARY GATE**, on daily execution. No price compensates.

### THE BINARY - honesty **[E5-16]**, each matter dated to when it became PUBLIC
1. **2022-03-07 to 2026-05: the IPO securities class action** (*Crews v. Rivian*, C.D. Cal., Securities Act sections
   11, 12(a)(2) and 15 and Exchange Act 10(b) and 20(a)). Dismissed with leave to amend (2023-02-16), motion to dismiss
   the amended complaint denied (2023-07-03), settled by stipulation 2025-10-23 for **$250M** (*"the aggregate net
   settlement payment made by the Company was $ 181 million"* after insurance), final approval and judgment May 2026 (Q2
   2026 10-Q Note 13). The 10-K records the company's position: *"We believe the alleged stockholders' claims are
   meritless."* **A settlement, not an adjudication; no finding of fact is on file.** [E5-22]: the size is not the
   seriousness in either direction; the filings do not state what was alleged beyond the statutes, so no reading of
   seriousness is attempted here.
2. **2024-05-31, open: a second securities class action** (C.D. Cal. 2:24-cv-04566, Exchange Act 10(b) and 20(a));
   *"On January 7, 2025 the defendants filed a Motion to Dismiss, which was denied by Order dated August 20, 2025"*
   (FY2025 10-K Item 3). No adjudication.
3. **2024-02-13 onward, open: derivative suits** (Delaware Chancery and C.D. Cal., ten filed from February 2024 to
   July 2026) alleging
   breach of fiduciary duty; stayed. No adjudication.
4. **No SEC enforcement action, restatement, 10-K/A or auditor change is on file.** KPMG since 2021, unqualified
   opinions and effective internal control at 2025-12-31 (Step 0).
5. **2026-08-27: the CFO announced her departure** effective 2026-10-30 (8-K `0001104659-26-102435`, *"to pursue a new
   opportunity and relocate to the East Coast"*), with an interim successor. Recorded; no reason on file to read it
   otherwise.

**Read on the binary:** no adjudicated integrity finding against the company or its officers is on file. *A Q3 pass is
the absence of found disqualifiers, not a finding that the managers are honest* **[E5-17]**.

### THE INCENTIVE READ **[E4-27]**
**What the CEO's pay vests on is written in the 2026 proxy** (DEF 14A `0001874178-26-000023`):
- **The 2025 CEO Award replaced an underwater one.** *"On November 6, 2025, the Compensation Committee cancelled the
  previously-disclosed performance-based option to purchase up to 20,355,946 shares ... granted to our CEO in January
  2021 ... and granted an option to purchase up to 36,500,000 shares"*, *"a net increase of 16,144,054 shares"*,
  exercise price $15.22. 22,000,000 shares vest on **eleven stock-price hurdles from $40 to $140**; 7,250,000 on
  *"adjusted operating income targets"* and 7,250,000 on *"cash flow from operations targets"* to 2032. The board's
  reason: *"the stock price targets included in the 2025 CEO Award more accurately reflect current market conditions
  and the Company's current stock price, while taking into account the current market reality and the broader economic
  uncertainty and headwinds that were not anticipated at the time the 2021 CEO Performance Award was granted."* The
  10-K puts the incremental fair value of the swap at **$285M**.
- **The 2025 bonus was scored on a free-cash-flow figure the committee adjusted upward.** *"In determining achievement
  for the Free Cash Flow metric, our Compensation Committee increased the results reported in our financial statements
  by $350,000,000 that was expected to be received by Rivian and Volkswagen Group Technologies, LLC in January 2026"*;
  the metric then scored **125%** (target -$2,390M, "actual" -$2,139M), while deliveries scored 69% (42,247 against a
  46,000 target) and gross profit 73% ($144M against $310M); overall 91%, paid in fully vested RSUs.
- **The CEO holds a 10% profits interest in a company Rivian spun out.** *"On November 6, 2025, Mind Robotics, LLC ...
  issued 1,000,000 common units (the "MR Profits Interest Award") to Dr. Scaringe ... up to a 10% economic interest in
  Mind Robotics"*, *"fully vested on the date of issuance"*, approved by a special committee; Mind Robotics was
  deconsolidated in March 2026 at a $506M gain to Rivian (Step 0). He also chairs Also, Inc., another Rivian spin-out
  (35.3% held).

**Three corpus flags fire from the pay documents:**
- **[E2-49], metric-switching, at full strength**: *"when results deteriorate, most managers favor disposition of the
  yardstick rather than disposition of the manager."* The 2021 price goals were cancelled after the stock fell, in
  the board's words because they no longer *"reflect current market conditions"*; the replacement lowers the bar and
  adds 16.1M shares. And the bonus yardstick was re-measured by $350M in the year it was scored, which is the passage's
  own image: *"just shoot the arrow of business performance into a blank canvas and then carefully draw the bullseye
  around the implanted arrow."*
- **[E3-50], stock-price targeting**: 60% of the award's shares vest on share prices alone.
- **[E3-70]**: the corpus measures an option at *"what the company could have realized by publicly selling options of
  like quantity and structure"*; a cancelled-and-replaced option at a lower bar is worth more on that measure, and the
  10-K's own figure for the difference is the $285M incremental fair value, before the 16.1M added shares.

### STEP 2 - THE FLAGS. *Each is a prompt to READ, never a verdict.*
- [ ] **weak accounting** - SBC expensed and complete on the face; no restatement; the $506M Mind Robotics
  remeasurement gain is named on the face and in Note 2 and excluded from adjusted figures. Not fired.
- [ ] **unintelligible footnotes** - the JV revenue, VW and Uber notes are long but legible. Not fired.
- [x] **trumpeted projections / growth targets [E4-22]** - annual guidance on deliveries, Adjusted EBITDA and capex in
  every Q4 release, plus robotaxi numbers (*"10,000 fully autonomous R2 robotaxis ... scaling to 25 cities through
  2031"*, 8-K EX-99.1 `0001104659-26-031794`). **[E3-48]'s remedy, run on the filed guidance:**

  | guided (8-K EX-99.1) | guidance | outturn | scored |
  |---|---|---|---|
  | 2024 production (2024-02-21, `0001874178-24-000005`) | 57,000 | 49,476 | **missed by 13%** |
  | 2024 Adjusted EBITDA | $(2,700)M | $(2,689)M | met |
  | 2024 capex | $1,750M | $1,141M | under |
  | "Path to Q4 Modest Gross Profit" (2024-02-21 headline) | Q4 2024 positive | Q4 2024 **$170M** | **met** |
  | 2025 deliveries (2025-02-20, `0001874178-25-000004`) | 46,000-51,000 | 42,247 | **missed; cut to 41,500-43,500 on 2025-11-04** |
  | 2025 Adjusted EBITDA | $(1,700)-(1,900)M | $(2,063)M (four quarters) | **missed; widened to $(2,000)-(2,250)M** |
  | 2025 capex | $1,600-1,700M | $1,710M | at the top |
  | 2026 deliveries (2026-02-12, then 2026-07-30) | 62,000-67,000, raised to 65,000-70,000 | open | |

  Both scored volume guides were missed (one by 13%, one cut in-year); of the two loss guides one was met and one
  missed and widened in-year; the "modest gross profit" target was met. The record is mixed and on file, which is better
  than an outlook with no numbers to score.
- [x] **serial share issuance [E5-15]** - **900,551,857 shares** (Class A plus B, FY2021 10-K cover, 2022-03-14) to
  **1,447,860,630** (2026-07-21): **+60.8% in four years**, +48% since the FY2023 10-K cover (977,449,611, 2024-02-16).
  Channels: Volkswagen (about 210M shares), Uber (20M, with up to $950M more in shares or $0.001 warrants), a July
  2026 public offering (86.25M), employees, and converted notes. Every share was issued to fund losses; no buyback.
- [x] **EBITDA promotion [E4-29]** - Adjusted EBITDA is one of three guidance lines in every annual guide and a headline
  row of the quarterly *"Summary Financial Performance"* (Q2 2026 Earnings Presentation: *"Adjusted EBITDA (Non-GAAP)
  $(667) $(602) $(465) $(472) $(379)"*), defined as net loss *"before interest expense (income), net, provision for
  income taxes, depreciation and amortization, stock-based compensation, other (expense) income, net, and special
  items"*. The pay plan uses GAAP-adjacent cash-flow and "adjusted operating income" instead. *"Doing so implies that
  depreciation is not truly an expense ... That's nonsense."*
- [ ] **filed-figure tells [E4-30]** - no taxes paid (losses with a full valuation allowance); growth is not smooth.
  Not applicable.
- **Flags that converge [E4-52]:** a repriced CEO award on share-price hurdles, a bonus yardstick adjusted in the
  scoring year, Adjusted EBITDA guidance, and 61% issuance in four years point one way: the equity is the funding and
  the share price is the pay scale.

### STEP 3 - THE PRIMARY TEST **[E2-01]**, scoped by **[E2-43]**
Return on equity is negative in every year: net loss $(4,688)M, $(6,752)M, $(5,432)M, $(4,746)M, $(3,626)M
(FY2021-25) against equity that fell from $13,799M (2022) to $4,594M (2025). Pre-tax return on capital employed net of
cash **-117%, -86%, -70%** (FY2023-25; `roc_out.txt`). **The primary test fails in its own terms on every year filed**,
improving [E2-42].

### CANDOR - THE HALF-OWNER TEST **[E2-26]**
The 10-K and 10-Q pass on the items tested: the JV revenue's source, its prepayment and its expected 2028 fall are
stated plainly; the Mind Robotics gain is quantified and named; R2 ramp costs are quantified (*"approximately $100
million"*); the loss contingencies are sized. **The releases fail it in one respect**: the Q2 2026 highlights page says *"Gross profit was $179 million"*
without saying there that the automotive segment lost $36M and that the positive figure is the Volkswagen work; the
segment split appears nine pages later.

### RATIONALITY IS CAPITAL ALLOCATION
- **Capital into spin-outs chaired by the CEO [E3-40]**: Also (35.3%) and Mind Robotics (32.1%), the latter with a 10%
  profits interest to the CEO. The amounts are small beside the automotive losses; the prompt is focus, and the 10-K
  names it: *"may compete with his ability to devote a sufficient amount of attention toward his obligations to us"*.
- **The institutional imperative [E2-30]:** (1) resists change: not scored; (2) **projects soak up funds: fired as a
  prompt**: a second plant in Georgia (DOE loan up to $4.5bn), in-house silicon (*"RAP1 chip"*), a robotaxi programme,
  and two spin-outs, while the core product has never earned a gross profit; (3) not observable; (4) imitation: not
  scored.
- **Buybacks [E5-08]:** none; the condition is moot for a business issuing shares to fund losses.
- **Stock deals in shares [E5-44]:** the VW and Uber issues are at 30-day VWAPs ($15.90, $15.34) against a Q5 that
  finds no owner-earnings value to set them against.

### THE GUARDRAIL
- [x] Nothing in this Q3 is used to promote the name. [x] "Requires a great manager" is recorded at Q2 as a moat
  defect **[E4-23]**. [x] The manager is the plan in the company's own 10-K (*"highly dependent on the services and
  reputation of Robert J. Scaringe"*), which is the **[E2-36]** corporate-Pygmalion case, not the excisable-cancer one.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary as the filings stand** (no adjudicated disqualifier; the
  IPO class action settled without a finding) [ ] OUT [ ] UNRESEARCHED [ ] UNKNOWABLE. **Four flags converge
  [E4-52]**: [E2-49] and [E3-50] in the repriced CEO award, [E5-15] issuance of 61% in four years, [E4-29] Adjusted
  EBITDA guidance; plus [E4-22] projections with a mixed filed record, and an [E3-40] prompt on the CEO-chaired
  spin-outs. *IN = no disqualifier found, never a promotion.*

---
## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). Written for the reopening conditions at Q6 and because
> the owner-earnings number is what Q5 would need.

### Owner earnings — the one number **[E2-23]**
From the filed cash-flow faces (FY2021, FY2023 and FY2025 10-Ks; Q2 2025 and Q2 2026 10-Qs), `oe.py`, output
`oe_out.txt`, $M. SBC is complete on the face (Step 0) and subtracted in full **[E5-06]**.

| year | OCF | SBC | capex (face) | D&A (face) | **OE, capex end** | **OE, D&A end** | "Deferred revenues" line in OCF | capex / D&A |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| FY2021 | (2,622) | 570 | 1,794 | 197 | **(4,986)** | **(3,389)** | n/a | 9.11 |
| FY2022 | (5,052) | 987 | 1,369 | 652 | **(7,408)** | **(6,691)** | n/a | 2.10 |
| FY2023 | (4,866) | 821 | 1,026 | 937 | **(6,713)** | **(6,624)** | 149 | 1.09 |
| FY2024 | (1,716) | 692 | 1,141 | 1,031 | **(3,549)** | **(3,439)** | **1,619** | 1.11 |
| FY2025 | (779) | 741 | 1,710 | 784 | **(3,230)** | **(2,304)** | **503** | 2.18 |
| TTM Jun-26 | (1,845) | 797 | 1,644 | 819 | **(4,286)** | **(3,461)** | (262) | 2.01 |

- **Five-year default window FY2021-25 [E2-42]: capex end $(5,177)M; D&A end $(4,489)M.** Three-year FY2023-25:
  $(4,497)M to $(4,122)M. TTM: $(4,286)M to $(3,461)M. **No ten-year window exists**: the first filed statements are
  FY2019-21 in the FY2021 10-K, and FY2019-20 were pre-revenue (OCF $(353)M and $(848)M). **Every window, every end,
  every year is negative: in words, the business has consumed between $2.3bn and $7.4bn a year of owners' money, and
  about $4.5-5.2bn a year on average.** The range is wide in dollars and one-signed, so it does not need resolving to
  reach Q4's conclusion **[E4-25]**.
- **The contract-liability line, shown both ways (the `working_capital_flag`).** FY2024 OCF of $(1,716)M contains
  **$1,619M** from the *"Deferred revenues"* line (94% of the OCF figure's size), almost all of it the $1,295M
  Volkswagen licence payment received in November 2024; FY2025 contains $503M, including the $250M milestone of June
  2025. **Is it float in the [E3-52] sense? No.** [E3-52]'s float is a revolving, covenant-free customer liability;
  this is one related party's prepayment for a performance obligation with a stated end (*"through approximately
  mid-2028"*), which unwinds as the work is done: deferred revenues fell from $2,343M (2025-12-31) to $1,981M
  (2026-06-30), and the line took **$362M out** of H1 2026 OCF. **Without it**: FY2024 capex end **$(5,168)M**, FY2025
  **$(3,733)M**, three-year mean **$(5,254)M**; the five-year capex-end mean with the FY2024-25 inflows removed is
  **$(5,602)M**. About half of the FY2024 improvement in operating cash ($3,150M better than FY2023) is the prepayment: the line gave
  $1,470M more than in FY2023.
- **Maintenance capex, a DISCLOSED JUDGMENT [E2-23]. What the D&A is made of, first:** property, plant and equipment
  depreciation is $917M, $1,000M and $740M (FY2023-25, 10-K Note 8) of D&A of $937M, $1,031M and $784M; the rest is
  finance-lease and other amortisation. **The FY2021 step (the `da_discontinuity_flag`, $29M to $197M) is the start of
  production** (the plant began depreciating when it began building cars), and **the FY2025 fall ($1,031M to $784M) is
  the end of an accelerated-depreciation year**: automotive D&A was $740M in FY2024 and $484M in FY2025, and the FY2025
  MD&A names *"accelerated depreciation that occurred during the prior year"* on the R1 line retooled in Q2 2024.
  **[E5-20] asked on the filing: YES, this is the exception class.** Tooling was written off within about two and a half
  years of the start of production, a new platform needed *"Significant capital expenditures"* in the same plant two
  years later, and capex was **1.96x D&A** over FY2021-25 ($7,040M against $3,601M). **The D&A end is optimistic, and
  (c) is judged at or near total capex**; the band is displayed, and both ends are negative.
- **Working capital [E2-23]:** besides the deferred revenue, inventory released $307M (FY2024) and $522M (FY2025) into
  operating cash after absorbing $1,657M and $1,604M in FY2022-23, and took $215M back in H1 2026 for the R2 ramp.
- **Stock compensation [E5-06, E3-70]:** subtracted in full at the charge. **The FY2019-20 zeros are real on the face**
  and not the SBC-of-zero tag defect: pre-IPO awards carried an IPO condition, so their expense fell into FY2021 (the
  FY2021 10-K records modifications raising unrecognised cost by $322M and $275M). **The [E3-70] market measure is
  larger than the charge**: FY2025 grants at grant-date fair value were about **$1,187M** (66M RSUs at $12.07 and 40M
  options at $9.74, FY2025 10-K stock-based compensation note) against $741M expensed, and H1 2026 RSU grants alone were about $861M (57M at $15.10).
- **Look-through [E3-04 convention, v4 section VI]:** Also and Mind Robotics are equity-accounted with results *"not
  material"*; nothing to add.

### Great, good, or gruesome? **[E4-20, E4-43]**
- [ ] great [ ] good [x] **gruesome, at the definition's full strength**: *"grows rapidly, requires significant capital
  to engender the growth, and then earns little or no money."* Revenue grew from $55M to $5.4bn while the business
  consumed about $26bn of owners' money at the capex end over five years; the savings account pays a negative rate and
  requires deposits every year (the July 2026 offering, VW, Uber).

### Staying power — score all three **[E5-11]**
- (1) **Earnings: none.** Operating losses every year FY2019-25 and H1 2026.
- (2) **Liquid assets: $5,310M** of cash and short-term investments at 2026-06-30, plus about $1,317M net from the July
  offering; ABL availability $536M; the company's own *"Total Pro-Forma Available Liquidity"* is **$7,163M** (Q2 2026
  Earnings Presentation).
- (3) **Near-term cash requirements: large, and the one that bites.** 2026 guidance is Adjusted EBITDA of **$(2.00)B to
  $(1.80)B** and capex of **$1.70B to $1.80B** (8-K EX-99.1 of 2026-07-30), before cash interest (FY2025 $222M) and the
  unwinding JV deferred revenue: roughly **$3.7-4.0bn a year** of cash out on the company's own plan, against about
  $6.6bn of cash, or about a year and a half to two years before new money. Named new money: Volkswagen's $1,000M loan
  (drawable only 2026-10-01 to 2026-10-30), Uber's $250M milestone targeted for 2026, VW's $460M at the Start of
  Production Milestone, and the DOE loan, whose first advance requires *"the Sponsor maintaining positive gross margin
  for certain periods"* and *"the funding of certain equity contributions and reserves"* (10-Q Note 8).
- **Leverage [E4-16, E2-54, E3-52]:** debt principal $4,475M: converts of $1,500M (2029, conversion $20.13) and $1,725M
  (2030, $23.29), both out of the money, and $1,250M of 10% secured notes (2031) *"secured ... on a first-priority basis
  by substantially all assets"*; the ABL carries *"a minimum liquidity requirement and fixed charge coverage ratio"*;
  the DOE loan, if drawn, adds *"a maximum 55 % ratio of Debt to Tangible Assets, a minimum Current Ratio of 1.25 :1.00,
  and minimum Liquidity of $ 2,000 million."* **[E2-54]'s coverage test fails outright**: interest cannot be met out of
  current cash flow net of capital expenditure, because that figure is about -$3.2bn to -$4.3bn a year. The business
  is **dependent on the kindness of strangers [E5-39]** by construction.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**
- **The mechanism: shape #8, THE EQUITY IS THE REVENUE, with #14's feature (THE PATRON)** (`Screens/SURVIVAL SHAPES -
  index.md`). Customers pay most of the cost of a vehicle but not all of it and none of the engineering and selling
  above it; new shareholders and partners (Volkswagen, Uber, the public) pay the rest, and the government sets part of
  the price (credits), part of the cost (manufacturing tax credits) and the terms of the next plant's debt (the DOE
  loan's gross-margin condition). The owner dies by dilution before the company dies by insolvency.
- **Quantified from filed figures:** at the 2026 guided burn of $3.7-4.0bn a year, the $6.6bn of cash lasts about
  twenty months; closing that gap at the July offering price ($15.50) needs about **240-260M new shares a year (16-18%
  of the count)**; the count has already risen 61% in four years. The exposure is filed: *"we will require additional
  financings to raise capital to support our business"* (Q2 2026 Earnings Presentation, forward-looking statement
  factors).
- **Likelihood: [x] likely** that the owner's share is diluted materially again before the business earns owner
  earnings (every year on file, and the company's own plan, has it so); **a real possibility** of insolvency-type
  distress if R2 misses the DOE loan's gross-margin condition while partners withhold their milestones; the partners
  and the market have funded every year so far, which is experience, not exposure **[E4-40]**.
- **VERDICT (RECORDED, NOT GOVERNING): [ ] IN [x] OUT on [E4-20]'s gruesome leg and on [E5-11]'s first and third
  strengths** (no earnings; near-term cash requirements that exceed liquid assets within about two years) [ ]
  UNRESEARCHED [ ] UNKNOWABLE.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 is OUT (and Q4, recorded, is OUT). Nothing below is a clearance.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
`oe_out.txt`; cap **$21,703M** ($14.99 x 1,447,860,630); sovereign **5.34%** (US Treasury 30 Yr, 09/18/2026).

| owner earnings case | $M | yield on the cap | vs 5.34% |
|---|---:|---:|---:|
| 5y FY2021-25, capex end | (5,177) | (23.9)% | -29.2 |
| 5y FY2021-25, D&A end | (4,489) | (20.7)% | -26.0 |
| 3y FY2023-25, capex end | (4,497) | (20.7)% | -26.1 |
| TTM to 2026-06-30, D&A end (the most generous figure) | (3,461) | (15.9)% | -21.3 |

- **The floor first [E4-28]:** a 10% pre-tax expectancy at this cap needs about **$2.17bn a year of positive owner
  earnings**, a swing of about **$5.6-7.3bn a year** from the filed windows (TTM D&A end to five-year capex end). No growth rate converts a negative base
  into a yield (the growth-required figure is refused on a negative bottom, as the screen itself does since the MRVL
  fix).
- **What the price already assumes:** that a business which has never earned a gross profit on its product will, on R2,
  a second plant and a robotaxi programme that Q1 placed outside the circle, earn more than $2bn a year for owners, and
  that the dilution needed to get there is smaller than the value created. **[E4-35]** and **[E4-44]** bind: no filed
  period supports any positive figure.

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-01]**
On owner earnings from any filed window, **no positive value can be computed**: the range is below zero at both ends.
Net cash of about $2.2bn (about $1.50 a share) is the only positive figure on the balance sheet and is being spent at
$3.7-4.0bn a year. **Bar 2, the screamer test [E4-01]**: the price ($14.99) is above the whole range; the answer would
be *no*. **Windage count: none spent** (the range is negative before any margin).

- **VERDICT: none. Q5 did not open (Q2 OUT).** Had every gate been IN, the computation shows a negative yield against
  a 5.34% bond and a 10% floor.

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

> **RECORDED, NOT GOVERNING.** Nothing is owned and nothing is armed (the QLYS ruling: a Q2 failure is a failure of
> the business, and a price alert on it would be a category error). These are the conditions on which the file would
> be reopened, written before any reopening **[E1-02]**.

**What would reopen Q2 (the governing gate):**
1. **A product that earns a gross profit on its own**: automotive segment gross profit **less regulatory credits**
   positive for at least three consecutive years, with deliveries flat or rising and no filed attribution of volume to
   a tax credit or subsidy [E3-43, E2-44, E2-59].
2. **A return on capital**: pre-tax return on capital employed net of cash positive and rising for three years with
   capital employed at or above FY2025's $5.1bn, and owner earnings at the capex end positive over a five-year window
   [E3-46, E2-42, E2-23].
3. **Pricing conduct**: a filed price rise held without a filed loss of units or share, in a year when the industry's
   own filings describe excess capacity [E2-44, E4-37].
4. **The outside-the-circle businesses entering it**: R2, Autonomy+ or the robotaxi programme reported with at least
   three years of filed revenue, cost and capital employed, so that Q1 can be asked of them at all [E3-31].
5. **Key-person dependence reduced in the 10-K itself** [E4-23].

**And what would close it harder:** the DOE loan's gross-margin condition missed; the Volkswagen revenue falling in
2028 with no replacement; the count up another fifth.

**The sell rule [E2-28]** does not apply (nothing held). **Position size:** none.
**VERDICT (RECORDED, NOT GOVERNING): not applicable; the file closed at Q2 and Q6 arms nothing.**

---
## SELF-AUDIT
- [x] Questions answered in order; the gate stopped at Q2 (OUT); Q3-Q6 recorded beneath explicit RECORDED, NOT
  GOVERNING banners, with Q5 headed COMPUTATION — NOT A CLEARANCE and carrying no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed statements and
  is scoped in writing to the business the filings show; R2 as a profit case, the robotaxi programme, Autonomy+, Mind
  Robotics and Also are recorded as outside the circle, not as a provisional IN. The software-and-services position is
  PROVISIONAL at Q2, and Q2 is OUT on the automotive business, which the provisional part cannot rescue.
- [x] No UNRESEARCHED or UNKNOWABLE verdict was returned. One document is named as a work order for any future upgrade
  only: BYD's 2025 annual report on HKEXnews (not re-attempted; the TM run recorded the obstacle).
- [x] Step 0: the filing was read with accession numbers; OCF, SBC, capex and D&A cross-checked to the FY2025 10-K face;
  SBC shown complete on the face by the MD&A's line allocation; the skip reason reproduced and explained on the filings.
- [x] Owner earnings on the five-year default window, a three-year window and TTM, both (c) ends; no ten-year window
  exists and that is said; the contract-liability line shown both ways; D&A's composition and both flagged steps
  explained; (c) disclosed as a judgment in the [E5-20] class.
- [x] Competitor row filled: eleven peers named, seven complete from SEC filings (Rivian, Lucid, Ford's Model e
  segment, Tesla, GM and Ford recomputed from their own faces; Toyota, Stellantis and Honda carried from the TM run's
  accessioned row and labelled as not recomputed); Volkswagen and Hyundai carried from that row in the text only; BYD
  named and not pulled.
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated 09/18/2026, fetched uncached.
- [x] Value stated as a range (negative at both ends) under a COMPUTATION — NOT A CLEARANCE heading.
- [x] One bar (the screamer test); windage count none spent.
- [x] Price dated as the 2026-09-18 close, aggregator flagged, corroborated by two Form 4s.
- [x] Share count from the Q2 2026 10-Q cover with its accession; the two classes summed only after the charter terms
  (as Note 14 states them) were read; converts, awards, VW and Uber instruments considered and stated either way.
- [x] Deal check run on EDGAR: no merger, tender or going-private filing; two 8-K Item 1.01s opened (Uber, DOE).
- [x] Run committed after Step 0, Q1, Q2 and Q3-Q6, each with a pathspec.
- [x] Every ledger id cited was looked up in `principle_ledger.csv` (`led.py`) before it was written, and the [E3-70]
  quotation was replaced with the ledger's own text when a first draft carried the framework's paraphrase in quote marks.
- [x] No em dashes in anything this session wrote (the template's own headings and the required
  `COMPUTATION — NOT A CLEARANCE` heading carry them).
- [x] Never presented as proven to beat the market; nothing here claims it.
- [x] No image files committed; the downloaded filings (10-K, 10-Q, DEF 14A text, Lucid 10-Ks, 8-K exhibits) and the
  1.1 MB `companyfacts.json` were left out of every commit.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **Q1 and Q2, corrected before the Q2 commit:** a draft set FY2025 production against the 215,000-unit capacity
   (about 20% utilisation). That capacity arrived with the 2025 paint-shop upgrade for R2; the FY2023 and FY2024 10-Ks
   state *"up to 150,000 vehicles annually"*, so the utilisation is 38%, 33% and 28% (FY2023-25). Q1 was corrected in the
   run file after its own commit (`35cfec9`) and the corrected text went in with the Q2 commit.
2. **Q1 (after its own commit, fixed in the Q2 commit) and Q2 (before commit):** a draft said the bank lease channel *"passed the federal 45W credit to
   drivers"*. No filing read says so; the text now says only what the 10-K says, that deliveries fell *"due in part to
   the expiration of 45W tax credits"*, and the credit's size comes from the FY2024 10-K (*"between $7,500 and
   $40,000"*), replacing a $7,500 figure from memory.
3. **Q2, corrected before commit:** a draft said every profitable maker in the row has a combustion business; Tesla
   sells only battery vehicles and is profitable at about 1.64 million units. The sentence now says every profitable
   maker is a volume maker.
4. **Q2, corrected before commit:** a draft put Volkswagen's equity purchases at $2,745M; the filed steps are a $1,000M
   note converted in December 2024, $750M in June 2025 and $1,000M in April 2026, about $2.75bn, and the text says that.
5. **Q3, corrected before commit:** the FY2023 10-K cover count was mis-summed (976,449,611 for 977,449,611); the
   derivative suits were counted as seven (the filings show ten); the guidance scorecard's summary line was rewritten
   to match its own table; and the [E3-70] line carried framework prose in quotation marks (fixed, item above).
6. **Q5, corrected before commit:** the new shares needed a year were put at 17-18% of the count (16-18% on the
   arithmetic), and the swing to the floor was attributed to the five-year means when its low end is the TTM figure.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **The register-counting instruction gives the wrong number.** The brief says to count entries under `## COMPLETED
   FROM THE QUEUE` *"stopping at the next `##`/`###` heading"*. The next such heading is `### REGISTER BACKFILL
   2026-09-13`, which holds ten entries (GM, F, OXY, AEO, KR, NKE, PLAB, CVX, HHH, GHC); stopping there gives **94**. The
   TSLA fold's 104 counts to `## THE WRITE-EARLY PROTOCOL`, which includes the backfill. Counted that way, with no
   duplicate ticker, RIVN is **105**.
2. **"a Q2 2026 10-Q exists"** and the DEI public-float date: held (filed 2026-07-30, `0001874178-26-000054`). But the
   brief's framing of the count as a dei problem missed that **the cover already includes a July 2026 offering of
   86.25M shares** made after the quarter's balance sheet (1,362M at June 30).
3. **The "unverified beliefs" list, settled:** IPO November 2021: **held** (176M shares at $78.00, FY2021 10-K;
   424B4 `0001193125-21-328239`). Class A and B with a founder-held super-voting class: **held**, and the Class B
   **converts automatically in November 2026** (the five-year anniversary), which the brief did not have. Amazon as a
   large holder and EDV launch customer with a lapsed exclusivity: **held in substance** (12.9%, 2026 proxy); the
   exclusivity was *amended* in November 2023, not simply lapsed, and fees to Amazon on third-party van sales run five and
   ten years from 2024-01-01. VW joint venture of June 2024 with up to about $5.8bn: **partly held**; the JV entity was
   established in **November 2024** (FY2025 10-K Note 19; the June 2024 8-K, `0001193125-24-167944`, Items 1.01, 2.03 and
   3.02, is in the index and was not opened), the filed consideration is a $1,295M licence, a $250M milestone, $210M at start of production,
   equity tranches and a $1,000M loan, and VW now holds 15.9%; this run did not reconcile the total to $5.8bn. DOE loan of
   about $6.6bn: **not settled for January 2025** (the 8-K of 2025-01-16 was not opened), **and superseded**: the
   amended agreement of April 2026 sets **$3,355M plus $315M and
   $651M plus $179M** (about $4.5bn with capitalised interest), undrawn and conditional on positive gross margin.
   Regulatory credits material and gross profit positive around Q4 2024: **held** (Q4 2024 gross profit $170M); but the
   FY2025 positive gross profit is the VW work, not credits. R2 at Normal in 2026: **held** (external deliveries from
   2026-06-09). Securities class actions over the IPO: **held** (settled for $250M, judgment May 2026), plus a second,
   open action from 2024. Large CEO performance award: **held, and it was repriced** (2025 CEO Award, above). Adjusted
   EBITDA headlining: **held**.
4. **"Class B with super-voting rights"**: the voting ratio was not needed and was not read; the 10-Q states the classes
   differ only in voting and conversion, which is what the count needed.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`share_count_shift` returns None when companyfacts carries no dei count**, and the triage reads None as a pass.
  Rivian's count rose 16.7% in six months and 61% in four years without any guard seeing it. A None here means "not
  measured"; a screen could say so in words rather than pass silently.
- **`working_capital_flag` read the FY2024 contract-liability line correctly** and is the reason the Volkswagen
  prepayment was found; its limit (annual facts only) did not bite, because the unwinding shows in the H1 2026 10-Q face.
- **`tools/sources.sovereign()` served the cached 09/17 row at 19:12 EDT** while the Treasury had published 09/18
  (5.34%): the SNOW and TSLA note, reproduced a third time.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**A first positive gross profit can be a partner's prepayment.** Rivian's FY2025 consolidated gross profit ($144M)
and about half of its FY2024 improvement in operating cash came from Volkswagen paying in advance for engineering work
that ends in 2028; the vehicles still lost money. Read the segment note and the deferred-revenue line before a
"turned gross-profit positive" headline is allowed to argue for a business.

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** RIVN FAILS AT Q2 (OUT, on [E3-03] criterion (2) not shown and contradicted in its own 10-K: *"highly
  competitive"*, competitors with *"significantly greater financial, technical, manufacturing, marketing, or other
  resources"*; deliveries fell 18% in FY2025, *"due in part to the expiration of 45W tax credits"*, after three flat
  years; no return on capital in any year (pre-tax ROCE -117%, -86%, -70% FY2023-25) and no filer in an eleven-peer row
  showing a battery-vehicle business earning a return at this scale (Lucid -258.7%, Ford Model e -67.1%, Rivian -66.5%
  operating margin in FY2025) [E3-46, E3-43]; both legs of [E2-44] and [E4-37] fail; credits and manufacturing tax
  credits administered by governments [E2-59]; a platform replaced every two to three years [E4-04, E5-23]; the 10-K says
  the plan depends on the founder [E4-23]). Q1 IN on the business the filings show, with R2's profit case, the Uber
  robotaxi programme, Mind Robotics and Also outside the circle; Q3 IN on the binary (recorded; gate case; [E2-49] and
  [E3-50] in the repriced 2025 CEO award, a $350M upward adjustment to the bonus FCF yardstick, [E5-15] +61% shares in
  four years, [E4-29], [E4-22] with a mixed guidance record); Q4 OUT (recorded; gruesome; five-year owner earnings
  $(5,177)M capex end to $(4,489)M D&A end, negative at every window and end; the FY2024 Volkswagen prepayment is not
  float; shape #8 with #14's feature); price $14.99 x 1,447,860,630 = $21.7bn, headed COMPUTATION — NOT A CLEARANCE:
  yield about -16% to -24% against 5.34%; Q6 arms nothing.
- Work order: none for this verdict. UNKNOWABLE: none.

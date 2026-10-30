# Company Run — MONRO, INC. (MNRO) — 2026-09-21
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

CIK 0000876427 · Nasdaq · SIC 7500 Services-Automotive Repair, Services & Parking ·
fiscal year ends the last Saturday of March (dei `fiscalYearEnd` 0327).
Wave 7, name 15 of 218. Register entry 147.

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
## THE SCREEN ROW — carried UNLABELLED, as arithmetic, never as a verdict

From `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`, line 25, verbatim. Operator
rule 8: tools fetch and compute and are forbidden to conclude; every flag is a prompt to
read, never a score. The two truncated fields are reproduced as truncated, because the CSV
itself is truncated there.

    ticker MNRO · name "MONRO, INC." · cap_m 397 · oe_bottom_m 37 · oe_top_m 107
    spread 1.878 · spread_dollars "$37M to $107M"
    cap_flag: "CAP BELOW FILED PUBLIC FLOAT - cap $397M against a filed float of $541M (1.36x)
      as of 2025-09-27. A cap cannot be smaller than a subset of itself. One of the two is
      wrong - RE-STRIKE THE CAP BY HAND before using any yield on this row [operator rule 4]."
    yield_bottom 0.0935 · vs_sovereign 0.04 · growth_required 0.0065
    level_shift 0.68 · level_note "STEP DOWN - the series has changed level; a tight spread her"
    best_year_dep 0.062 · best_year_note "no single-year dependence (9-yr OCF series)"
    level_shift_oe n/a · level_note_oe "EARLY HALF STRADDLES ZERO - the pre-window years run
      from $-2.8M to $1"
    best_year_dep_oe 0.265
    flags_disagree: "FLAGS DISAGREE - one series refuses the ratio and the other does not; read
      the filing [E4-25]"
    level_shift_full 0.87 · years_filed 17 · window_disagree (blank)
    acq_note: "acquisitions are $90M, 23% of cap, inside the window - the numerator and
      denominator may be different companie"
    spread_caveat: "4-construction width only (3y/5y x two capex ends): CANNOT see variation
      older than the 5-year window; rebuild it [E4-25]"
    newest_filing 2026-03-28 · newest_periodic 2026-03-28

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34 %** · date **2026-09-18** · source **US Treasury, Daily Treasury Par Yield
  Curve Rates, 30-year constant maturity** (issuing authority; saved to
  `Test Runs/_research 2026-09-21 MNRO/treasury_yield_curve_2026.csv`, 180 rows; header
  `Date,"1 Mo",...,"30 Yr"`, first data row `09/18/2026,3.97,...,5.38,5.34`). FRED DGS30 was
  not used; it is the fallback, not the source.
- Currency: **USD**. Monro operates 1,115 stores in 32 US states and files in USD. No FX,
  no ADR ratio.
- **The screen row's `vs_sovereign 0.04` is stale by 134 basis points.** It is carried above
  as arithmetic and is used nowhere below.

**THE HAND-STRUCK CAP — operator rule 4, and the `cap_flag` is an instruction, not a hint.**

| | |
|---|---|
| price | **$12.10**, close of **2026-09-18** (Yahoo Finance via `tools/sources.py`; **aggregator, live quote only, flagged as such**, operator rule 5) |
| shares outstanding | **31,264,060** as of **2026-07-18** |
| from | cover page of the Form 10-Q for the quarter ended 2026-06-27, filed 2026-07-29, **accession 0000876427-26-000010**: *"As of July 18, 2026, 31,264,060 shares of the registrant's common stock, $0.01 par value per share, were outstanding."* |
| splits after the measurement date | **1.0** (checked; `cap = close × shares(measurement) × splits AFTER measurement`) |
| **market capitalisation, struck by hand** | **31,264,060 × $12.10 = $378,295,126 ≈ $378M** |

**THE `cap_flag` IS REFUTED, AND BY EXACT ARITHMETIC, NOT BY ASSERTION.**

The flag says *"A cap cannot be smaller than a subset of itself. One of the two is wrong."*
Neither is wrong. **The two numbers are measured eleven months apart and the stock fell 35%
in between.**

1. The float is a cover-page figure: **$541,400,000 as of 2025-09-27**, taken from the
   FY2026 Form 10-K cover, accession **0000876427-26-000007**. It is the aggregate market
   value of common equity held by non-affiliates *on the last business day of the
   registrant's most recently completed second fiscal quarter*, which for a fiscal-March
   filer is the end of September.
2. 2025-09-27 was a Saturday; the last trading day on or before it was **Friday 2025-09-26,
   close $18.68**.
3. Implied non-affiliate share count: **$541,400,000 ÷ $18.68 = 28,983,940 shares.**
4. Shares outstanding at that date: **30,019,660**, from the cover of the Form 10-Q for the
   quarter ended 2025-09-27, accession **0000876427-25-000005**.
5. **28,983,940 ÷ 30,019,660 = 96.55%** — a plausible non-affiliate fraction, and **below
   100%**, so the float *was* a proper subset of the shares outstanding.
6. Implied capitalisation **at the float date**: 30,019,660 × $18.68 = **$560,767,249**,
   which is **larger** than the $541.4M float. **No contradiction existed on 2025-09-27.**
7. The screen's $397M cap is struck at a 2026 price ($397M ÷ 30.0M shares = $13.22). MNRO
   closed $12.41 on 2026-09-02 and $12.10 on 2026-09-18. The stock is down **35.2%** from
   $18.68.

**Verdict on the flag: FALSE POSITIVE, and the defect is a DATE MISMATCH, not arithmetic.**
The comparison is structurally invalid for every name whose price has fallen by more than
`1 − float/shares` since its float measurement date, which can be up to twelve months before
the cap date. **Tooling fix, recorded in the fold:** compare the filed float against a cap
struck **at the float date** (close on the float date × shares outstanding at that date),
never against the live cap. The current test is not a sanity check; it is a price-decline
detector wearing a sanity check's label.

**A SECOND CAP DEFECT THE FLAG DID NOT CATCH — the share count itself.** The screen's cap
used a pre-conversion share count. The Class C Convertible Preferred Stock **converted
automatically on 2026-06-18**, one business day before the 2026 annual-meeting record date,
under the 2023 Reclassification Agreement: *"A total of 19,664 shares of Class C Preferred
Stock, with a par value of $1.50 per share and a conversion ratio of 61.275 shares of Common
Stock per preferred share, were converted into 1,204,908 shares of Common Stock"*
(10-Q 0000876427-26-000010). Check: 30,025,266 (10-K cover, as of 2026-05-15) + 1,204,908
= 31,230,174 against the 31,264,060 on the 10-Q cover seven weeks later; the 33,886
difference is ordinary equity-plan issuance. **Any cap struck on the 10-K cover count
understates the shares by 4.0%.** This is the mirror of the resume-state source limit at
section 5 (*"Convertible preferred counted in basic EPS is invisible to the cover element"*):
here the preferred stopped being invisible by converting, and only the newest cover sees it.

**`newest_filing` AND `newest_periodic` ARE BOTH WRONG, AND IN TWO DIFFERENT WAYS.** The
brief asked whether their being equal is real or an artifact. It is an artifact, twice over:
- **2026-03-28 is not a filing date. It is a period-end date.** The FY2026 10-K covering the
  year ended 2026-03-28 was **filed 2026-05-27**. A field named `newest_filing` carrying a
  report date will mis-sort every filer whose fiscal year does not end in December.
- **Both fields are also a quarter stale.** As at the CSV's own date of 2026-09-02, the
  newest periodic report was the **10-Q for the quarter ended 2026-06-27, filed 2026-07-29** —
  which is the very filing that carries the share count the cap needed. The fields appear to
  read annual facts only.
- **MNRO is a fiscal-March filer, plainly**: `fiscalYearEnd` 0327; FY2026 ended Saturday
  2026-03-28, FY2025 ended 2025-03-29, FY2024 ended 2024-03-30.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **Form 10-K for the fiscal year ended March 28, 2026;
  filed 2026-05-27; accession 0000876427-26-000007** (primary document
  `mnro-20260328x10k.htm`). Also read: **Form 10-Q for the quarter ended June 27, 2026,
  filed 2026-07-29, accession 0000876427-26-000010**, and the 8-K EX-99.1 earnings releases
  listed at Q3.
- figure cross-checked against the filed statement: **depreciation and amortization of
  $61,674 thousand** for FY2026. The MD&A narrative says *"largely driven by $61.7 million of
  depreciation and amortization"*; the **Consolidated Statements of Cash Flows** (page 43 of
  the 10-K) carries the line `Depreciation and amortization 61,674` for 2026, `69,372` for
  2025 and `72,204` for 2024; the XBRL tag `DepreciationAmortizationAndAccretionNet` carries
  61,674,000. All three agree. **Second cross-check, by hand:** operating income $20,029
  thousand = gross profit $405,261 less OSG&A $385,232, from the MD&A tables, agreeing with
  the filed income statement.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.**

Monro rents or owns about eleven hundred small free-standing buildings, each with a handful
of hydraulic lifts, and staffs them with technicians. A car arrives; Monro sells the owner a
physical part (a tire, a brake pad, a battery, a quart of oil) at a mark-up, and sells the
hours of labour needed to fit it. Roughly half the revenue line is tires, which are bought
from third parties — one vendor supplied about 35% of all stocking purchases in FY2026 and
the ten largest supplied about 88% — and resold. The rest is undercar repair and routine
maintenance.

The economics are therefore: **a mostly fixed cost base (rent, lifts, a technician who is
paid whether or not the next car comes in) against a variable, weather-and-miles-driven
stream of tickets.** Monro's own FY2026 numbers say exactly this out loud: gross margin rose
10 basis points because *"decreased occupancy costs as a percentage of sales, as we gained
leverage on these largely fixed costs"* contributed +60bps, while technician labour cost
−50bps to wage inflation. The business is an operating-leverage machine in both directions.
At $1,157.2M of sales across 1,115 stores that is about **$1.04M of sales per store**, on
which the company earned **$20.0M of operating income — 1.73 cents on the sales dollar.**

Gross margin is 35.0%. Everything between gross profit and operating profit — store payroll
above technician cost, advertising, supervision, corporate — consumes 33.3 of the 35.0
points. **There is almost nothing between the two.**

**The scarce input this business controls.** Two candidates, and both are weak — a Q1
observation, not yet a Q2 verdict:
- **The site.** A service bay must be where the car already is; a driver will not cross a
  city for an oil change. Monro's own language is *"the best place in their neighborhoods"*
  and *"we attempt to cluster stores in market areas to achieve economies of scale in
  advertising and supervision costs."*
- **The certified technician.** The 10-K devotes more space to technician recruitment,
  retention, tool-purchase programmes and ASE certification than to any other operating
  topic, and technician wage inflation is the single named drag on FY2026 gross margin.
  6,270 of 6,440 employees are in the field.

Monro controls neither exclusively. It does not make the tire; it buys from a concentrated
supplier set and, since the June 2022 divestiture of its own wholesale and distribution
operation to American Tire Distributors, it buys distribution as a service from a
counterparty that also supplies its competitors. It does not control the technician, who can
cross the street. It does control its own leases, and closing 145 stores in one quarter says
what that control is worth when the sites are wrong.

**Will the fundamentals look broadly the same in ten years?** **Yes.** This is the part of
the file that is genuinely easy. Cars have tires; tires wear out; brakes wear out; oil is
changed; and the work must be done physically, near where the car is, by a person with a
lift. The electrification question is real but it cuts *toward* this mix rather than away
from it: tires are 48% of Monro's sales and heavier electric vehicles consume them faster,
while the categories electrification removes — exhaust, and much of the oil-change work —
sit inside the 27% "maintenance service" and 1% "other" lines, not the 48%. **Nothing here
is "complex or subject to constant change" [E3-31].**

**[E4-46] check:** this is not a business that would take five months to learn. It is a
storefront service business with one operating segment, one currency, six product categories
and a two-line income statement. The decision does not fail for want of understanding, and
so no fetch is owed here.

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE

*Recorded for Q2, not scored here: the FY2026 operating margin of 1.73% and the store count
falling from 1,260 to 1,115 are claims about competitive position, and a moat is a relative
claim. They belong at Q2, where they can be set against peers.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

> "An economic franchise arises from a product or service that: (1) is needed or desired; (2)
> is thought by its customers to have no close substitute and; (3) is not subject to price
> regulation. **The existence of all three conditions will be demonstrated by a company's
> ability to regularly price its product or service aggressively and thereby to earn high
> rates of return on capital.** Moreover, franchises can tolerate mis-management."
> — **[E3-03]**, 1991 letter

That sentence in bold is the operational test, and it is the one this file turns on.
**Monro has priced aggressively, and its return on capital has gone the other way.**

### The three criteria, run one at a time

- **(1) Needed or desired — MET.** Brakes fail, tires wear, oil degrades. The demand is not
  discretionary in any deep sense and it recurs on a physical schedule.
- **(2) No close substitute — FAILS, and the filing says so in its own words.** The 10-K's
  Competition section: *"Our segment of the retail industry is fragmented and highly
  competitive, and the number, size, and strength of competitors vary widely from region to
  region."* It then names the substitute set: *"service centers operated by national and
  regional undercar, tire specialty and general automotive service chains, both franchised
  and company-operated, mass merchandisers, car dealerships, independent garages, and gas
  stations"*, plus *"online merchandisers of tires and automotive parts, which increasingly
  partner with local service centers to provide installation services."* And it names the
  basis of competition: *"competition in the industry is based primarily on price, store
  location, name awareness and customer service."* A business whose own annual report says it
  competes primarily on **price** against **independent garages and gas stations** is
  describing the absence of criterion (2), not its presence.
- **(3) Not subject to price regulation — MET.** No rate regulator sets what Monro may charge
  for a brake job. Its regulatory burden (EPA, RCRA, Clean Air Act, waste handling) is
  compliance cost, and the 10-K says *"our related compliance costs are not material."*

Two of three met. **[E3-03] requires all three**, and the failure is on the middle one, which
is the one that carries the economics.

### The demonstration test, run on the filings — and it runs backwards

[E3-03] says the three conditions *"will be demonstrated by a company's ability to regularly
price its product or service aggressively and thereby to earn high rates of return on
capital."* Monro discloses both halves of that sentence, every year, and they have moved in
opposite directions for seven years.

**The physical series, because Monro publishes one.** *"Where units exist, monitor units"* —
**[E4-55]**, Wesco 2006, on Precision Steel: *"In 2006, Precision Steel's service center
volume was 46 million pounds, down from 69 million pounds sold as recently as 1999. This
decline in physical volume is a serious reverse, not likely to disappear in some ""bounce
back'' e?ect. Nor do we expect another sharp rise in prices like the approximately 40% rise
that recently occurred, holding dollar volume roughly level despite a precipitous drop in
physical volume."* *(The doubled quotation marks and the corrupted `e?ect` are OCR artifacts
carried in the ledger row itself and are reproduced, not smoothed — PRIME RULE 1.)*

Monro reports **vehicles serviced** in Item 1 of every 10-K. That is the pounds.

| fiscal year | sales $M | op. income $M | **op. margin** | stores at year end | **vehicles serviced** | vehicles per store | **sales per vehicle** |
|---|---|---|---|---|---|---|---|
| 2019 | 1,200.2 | 126.7 | **10.56%** | 1,197 | **6.2M** | 5,180 | **$194** |
| 2020 | 1,256.5 | 101.7 | 8.09% | 1,283 | 6.1M | 4,754 | $206 |
| 2021 | 1,125.7 | 72.2 | 6.41% | 1,263 | 4.8M | 3,800 | $235 |
| 2022 | 1,359.3 | 101.3 | 7.45% | 1,304 | 5.2M | 3,988 | $261 |
| 2023 | 1,325.4 | 79.8 | 6.02% | 1,299 | 5.0M | 3,849 | $265 |
| 2024 | 1,276.8 | 71.4 | 5.59% | 1,288 | 4.7M | 3,649 | $272 |
| 2025 | 1,195.3 | 12.6 | 1.05% | 1,260 | 4.2M | 3,333 | $285 |
| **2026** | **1,157.2** | **20.0** | **1.73%** | **1,115** | **3.8M** | **3,408** | **$305** |

*Sources: sales and operating income from the Consolidated Statements of Income in each Form
10-K (FY2026 hand-checked: $405,261 gross profit less $385,232 OSG&A = $20,029). Vehicles
serviced and store counts from Item 1, Business, of each Form 10-K — FY2026: "we operated
1,115 retail tire and automotive repair stores and serviced approximately 3.8 million
vehicles in fiscal 2026"; FY2019: "Company-operated stores serviced approximately 6.2 million
vehicles in fiscal 2019". FY2022 and one quarter of FY2023 include the wholesale tire
operations divested in June 2022; the FY2023 10-K quantifies that as approximately $90.6
million of the prior-year comparison.*

**Read the ends of that table together.**
- Vehicles serviced: **6.2 million to 3.8 million, −38.7% in seven years.**
- Vehicles per store: **5,180 to 3,408, −34.2%.**
- Sales per vehicle: **$194 to $305, +57.3%.**
- Sales: **−3.6%.** The dollar line is nearly flat *because* the price line rose 57%.
- Operating margin: **10.56% to 1.73%.** Operating income fell **84.2%**.

This is Precision Steel's shape with one difference that makes it worse. At Precision Steel
the price rise *held dollar volume level*, which at least preserved the revenue. Here the 57%
price rise held the dollar line roughly level **and the operating income still fell by
five-sixths.** That was not pricing power. It was cost pass-through that failed to cover its
own costs, bought by giving up more than a third of the units.

**[E2-44], the two-characteristic test, fails on both characteristics.** (1) *"an ability to
increase prices rather easily (even when product demand is flat and capacity is not fully
utilized) **without fear of significant loss of either market share or unit volume**"* —
Monro raised realised price per vehicle 57% and lost 38.7% of its unit volume. (2) *"an
ability to accommodate large dollar volume increases in business (often produced more by
inflation than by real growth) **with only minor additional investment of capital**"* — see
the acquisition record below; Monro's dollar growth was bought, never earned.

**[E4-37], the inverse metric, run honestly and in Monro's favour first.** *"you can almost
measure the strength of a business over time by **the agony they go through in determining
whether a price increase can be sustained**"* — and Monro shows **no agony**: it took 57%
more per car without a visible fight. That reading would flatter the name. It is refuted by
the volume series in the same table, because the same passage asks *"if we raised the price
10 cents a pound, would sales fall off a cliff?"* — and here they did. **The absence of
agony in the narrative is not evidence of pricing power when the physical series shows what
the price cost.**

### Returns on capital, the second question about the business **[E3-46]**

> "the best businesses, by definition, are going to be businesses that earn **very high
> returns on capital employed over time**" — **[E3-46]**, 1995 meeting

Monro is an acquisitive filer carrying $736.4M of goodwill, so **[E2-43]** sets the
denominator: *"What a business can be expected to earn on **unleveraged net tangible
assets**, excluding any charges against earnings for amortization of Goodwill, is the best
guide to the economic attractiveness of the operation."*

| | FY2019 | FY2026 |
|---|---|---|
| total assets | $1,312.3M | $1,568.0M |
| less goodwill | (671.8) | (736.4) |
| less other intangibles | (51.1) | (7.7) |
| **net tangible assets** | **$589.4M** | **$823.9M** |
| operating income | $126.7M | $20.0M |
| **return on net tangible assets** | **21.5%** | **2.4%** |
| same, removing the post-ASC-842 operating-lease ROU asset ($175.9M) so both years sit on one basis | — | **3.1%** |

*Balance-sheet figures from the Consolidated Balance Sheets of the FY2019 and FY2026 10-Ks.
Shareholders' equity is recomputed from assets less liabilities, per **[E5-32]**'s
prescription that the filed statement is not bedrock: $1,568.0M − $976.5M = **$591.5M**. Net
of $736.4M goodwill and $7.7M other intangibles, **tangible book equity is negative
$152.6M**.*

**A business earning 2-3% on its net tangible assets is not earning "very high returns on
capital employed."** In FY2019 it earned 21.5% and had a plausible franchise claim. That
claim has been extinguished by the record, not by an opinion about the future.

### THE COMPETITOR ROW — required **[E3-28]**

> "If we own stock in a company and in an industry, and there are eight other companies that
> are in the same industry, I want to own or be on the mailing list for the reports for the
> other eight … **I can't be an intelligent owner of a business unless I know what all the
> other businesses in that industry are doing.**" — **[E3-28]**, 1996 meeting

A moat is a claim about *relative* position. The claim to be tested is the one the decline
above invites: **that the whole category is in trouble, so Monro's collapse says nothing
about Monro.** That is the hypothesis I would like to be true, because it would keep the file
open, so **[E4-26]** says to hunt it hardest: *"He trained himself, early, to intensively
consider any evidence tending to disconfirm any hypothesis of his, more so if he thought his
hypothesis was a particularly good one."*

**Metric: operating margin — operating income divided by revenue, from each company's own
filed consolidated income statement.** It is the one metric every peer reports on the same
definition, it requires no estimate, and it is the metric that moved at Monro.

**Window: each company's fiscal year ending in calendar 2019 (or the first clean
post-separation year where a corporate event makes 2019 not like-for-like), against its most
recent filed fiscal year.** The fiscal calendars do not align — Monro ends in March, Valvoline
in September, AutoZone in August, the rest in December — and that is stated rather than
hidden. No peer's window is shorter than five years **[E2-42]**.

| Company | what it is | base year | margin | latest year | margin | **change** | source |
|---|---|---|---|---|---|---|---|
| **MONRO (MNRO)** | **1,115 tire and service bays** | FYE 2019-03-30 | **10.56%** | FYE 2026-03-28 | **1.73%** | **−8.83 pts** | 10-K 0000876427-26-000007, hand-computed |
| **Valvoline (VVV)** | quick-lube retail service, ~2,000 locations | FYE 2020-09-30 (first year restated to retail services only) | 22.04% | FYE 2025-09-30 | **22.80%** | **+0.76 pts** | 10-K 0001674910-25-000135, hand-checked |
| Valvoline, longer view | — | FYE 2019-09-30, still including Global Products | 16.65% | — | — | *not like-for-like; shown and discounted* | same |
| **Driven Brands (DRVN)** | Take 5, Meineke, Maaco — auto service, franchised and company-operated | FYE 2019-12-28 | 11.66% | FYE 2025-12-27 | **12.41%** | **+0.75 pts** | SEC XBRL, 10-K series |
| **O'Reilly (ORLY)** | auto parts retail — the neighbouring category | FYE 2019-12-31 | 18.92% | FYE 2025-12-31 | **19.46%** | **+0.54 pts** | SEC XBRL, 10-K series |
| **AutoZone (AZO)** | auto parts retail | FYE 2019-08-31 | 18.68% | FYE 2025-08-30 | **19.06%** | **+0.38 pts** | SEC XBRL, 10-K series |
| **Advance Auto Parts (AAP)** | auto parts retail | FYE 2019-12-28 | 6.97% | FYE 2026-01-03 | **−0.50%** | **−7.47 pts** | SEC XBRL, 10-K series |

*The Valvoline row is hand-checked against the filed statement, per operator rule 4's spirit
applied to the row that carries the argument: VVV's Consolidated Statements of Income in
10-K 0001674910-25-000135 report `Net revenues 1,710.3 / Gross profit 658.5 / Operating
income 389.9` for the year ended September 30, 2025, and the MD&A states `Operating margin
22.8%`. The XBRL agrees.*

**Peers named: 5 with filings, of an industry whose four largest direct competitors do not
file.** Buffett says eight **[E3-28]**; I took five and I name the four I could not get:
- **Mavis Tire Express Services** — private, roughly two thousand locations, the largest
  direct competitor by store count. No SEC filings.
- **Discount Tire / America's Tire (Reinalt-Thomas)** — private. No SEC filings.
- **Les Schwab Tire Centers** — private. No SEC filings.
- **Bridgestone Retail Operations (Firestone Complete Auto Care, Tires Plus)** — a division
  of a Japanese parent that does not file with the SEC and does not report US retail
  operating margin separately.

**Consequence, stated as the template requires: the four largest direct competitors are
unavailable, so a claim that Monro's position is WIDE would have to be held PROVISIONAL.
That does not bind here, because the row is not being used to establish a moat — it is being
used to test whether the category explains the collapse, and for that question the five
filed peers are sufficient and they answer it.**

**The category hypothesis is REFUTED.** Over the same window in which Monro lost 8.83 points
of operating margin:
- the **closest** peer by business model — Valvoline, which also sells labour hours out of
  service bays to walk-in retail customers — **expanded** its margin to 22.80%, thirteen
  times Monro's;
- Driven Brands, the other listed multi-brand auto-service operator, **expanded**;
- both large parts retailers held near 19-20% flat, replicating the ORLY run's own finding
  (19.77% to 19.46% over nine years) on a different window;
- **one** peer also broke — Advance Auto Parts, −7.47 points — and that is the honest caveat.
  AAP is a parts distributor with a documented supply-chain and category-management failure,
  not a service operator, and one broken peer in five does not make a broken category. If
  anything its presence sharpens the point: the two names in this table that collapsed are
  the two that were losing share to better-run competitors, and the three that did not
  collapse did not.

**A whole industry did not fall over. One company did.** That is what a competitor row is
for, and it is the reason [E3-28] sits in the framework.

### The rest of the Q2 battery, each answered

**Untapped pricing power [E3-33]? NO.** *"there are actually businesses that you will find a
few times in a lifetime where any manager could raise the return enormously just by raising
prices, and yet they haven't done it. So they have huge untapped pricing power that they're
not using. That is the ultimate no-brainer."* Monro has already done it — sales per vehicle
+57.3% — and the return fell. The scope clause **[E5-28]** forecloses the claim anyway: *"If
you name some business that has incredible pricing power, you're talking about a business
that's a monopoly or a near monopoly."* Monro's own 10-K calls its segment *"fragmented and
highly competitive."* Claiming the class here would be claiming near-monopoly against the
registrant's own words.

**The attacker's test [E2-45].** *"One question I always ask myself in appraising a business
is how I would like, assuming I had ample capital and skilled personnel, to compete with it.
I'd rather wrestle grizzlies than compete with Mrs. B and her progeny."* I would enjoy
competing with Monro, and four private companies are currently proving it. The entry cost is
one leased building and two lifts. There is no proprietary part, no proprietary data, no
network effect and no switching cost — a customer chooses the nearer or cheaper bay next time
and pays nothing to switch. The one structural asset, **distribution density**, Monro
**sold**: the June 2022 divestiture of its wholesale operations (seven locations) and
internal tire distribution to American Tire Distributors, after which it buys tire supply
*and* category management *and* ordering *and* inventory managed services from ATD under a
managed-services agreement. **This is where the ORLY run's distribution-density moat case is
tested, and it does not transfer.** O'Reilly owns its distribution network; Monro sold its own
and now rents the function from a counterparty that serves the field. No grizzly.

**Which of the four causes of extreme success produced the record? [E4-36]** — *"Extreme
maximization or minimization of one or two variables … Adding success factors so that a
bigger combination drives success, often in nonlinear fashion … An extreme of good
performance over many factors … **Catching and riding some sort of big wave.**"* Monro's good
years were the fourth. It rode the consolidation of a fragmented industry by buying stores:
**937 company-operated stores at FY2013 rising to 1,304 at FY2022**, paid for with
**$859.7 million of acquisition cash across FY2010 to FY2023** (Consolidated Statements of
Cash Flows, line "Acquisitions, net of cash acquired"; two years cross-checked by hand
against the filed statement — FY2020 $104,436 thousand, FY2023 $6,685 thousand). **[E3-51]**
names what that is: *"when a surfer gets up and catches the wave and just stays there, he can
go a long, long time. But if he gets off the wave, he becomes mired in shallows."* The wave
was cheap private-market store prices in a consolidating category. **The acquisition line has
been zero in FY2024, FY2025 and FY2026**, and the store count has gone 1,304 to 1,115. The
surfer is in the shallows. **A surfing run is not a moat; the advantage lived in the wave.**

**The dominance class [E2-53]? NO.** *"Once dominant, the newspaper itself, not the
marketplace, determines just how good or how bad the paper will be. **Good or bad, it will
prosper.**"* Monro runs 1,115 stores in 32 states against Mavis's roughly two thousand,
Discount Tire's twelve hundred, Firestone's seventeen hundred and an uncountable field of
independent garages. It is not dominant in any market it discloses, and it discloses no
market-share figure at all. The marketplace determines Monro's economics, not the reverse.

**Direction outranks existence [E4-32].** *"we think in terms of that moat and the ability to
keep its width and its impossibility of being crossed as the primary criterion of a great
business. And to our managers, we say we want the moat widened every year. You know, that
does not necessarily mean that the profit is more this year than last year, because it won't
be sometimes."* The caveat is honoured: one down year proves nothing. This is not one down
year. It is **seven consecutive years** in which the margin fell from 10.56% to 1.73% with
exactly one up-tick (FY2022, and that year still carried the wholesale business), the unit
series fell in every year but one, and the store count went into reverse. **The direction is
unambiguously narrowing.**

**The row's limit, stated [E3-61].** *"In some businesses, the participants behave like a
demented Kellogg. In other businesses, they don't. Unfortunately, I do not have a perfect
model for predicting how that's going to happen … I think you'd have to know the people
involved to fully understand what was happening."* The competitor row shows relative
position; it cannot show conduct. It is possible that Monro's private competitors are pricing
irrationally and will one day stop. The row is used here only for the narrow claim it can
support — that the category did not fall over — and that claim needs no prediction about
conduct.

**Key-person dependence [E4-23], recorded HERE and not at Q3, as the framework directs.**
*"if a business requires a superstar to produce great results, the business itself cannot be
deemed great … The partnership's moat will go when the surgeon goes. You can count, though,
on the moat of the Mayo Clinic to endure, even though you can't name its CEO."* Monro is
running an "Operational Improvement Plan" on which it spent **$20.3 million of outside
consulting in FY2026 alone** — an amount equal to **101% of the year's entire operating
income** — under a President and Chief Executive Officer, Peter Fitzsimmons, who came from
the turnaround profession. **A business whose current plan is a consultant-led turnaround is
by construction a business that requires a great manager, and [E4-23] makes that a moat
defect.** It is written here so that a warning about the business cannot later be read as a
compliment to the person.

### Management's own moat claim, tested rather than dismissed **[E4-26]**

The standing instruction is to pull the newest 8-K EX-99.1 before scoring the manager. I
pulled it here instead, because what it carries is a **moat claim**, and a moat claim belongs
at Q2. From the Q1 FY2027 release (8-K filed 2026-07-29, EX-99.1, accession
0001193125-26-322170), Peter Fitzsimmons:

> "we were able to **hold our tire unit volumes flat**, and we believe this allowed us to
> **take market share**, both in our tier one tires as well as in our overall tire category
> in the quarter."

**Tested, not dismissed.** Flat tire units in one quarter is a real fact and it is the first
non-negative unit datum in this file. Against it, from the same release:
- **comparable store sales −1.7%** and total sales −4.6% to $287.1 million;
- the quarter is attributed to *"lower store traffic as well as consumers that continued to
  defer higher-ticket spending decisions in tires and brakes and **traded-down to lower-cost
  alternatives** in our tire category"*, with credit given to *"the timely expansion of our
  **tier four** tire offerings"* — the units were held by selling a cheaper tire;
- operating income **$3.7 million on $287.1 million of sales, 1.3%**, and **adjusted**
  operating income **$2.2 million, 0.8% — below the GAAP figure**;
- a **net loss of $2.1 million** and an **adjusted diluted loss of $0.09 per share**.

One flat quarter in tire units, achieved by trading customers down a price tier, against a
seven-year 38.7% decline in vehicles serviced, does not reverse the direction finding. **The
claim is recorded as tested and not sustained** — a different and more honest outcome than
ignoring it.

### THE [E4-04] VERDICT FORM — checked, and it is NOT the form this file takes

The ruling applied in `THE FRAMEWORK v4.md` on 2026-09-20 is explicit. **[E4-04]** — *"Our
criterion of 'enduring' causes us to rule out companies in industries prone to rapid and
continuous change. Though capitalism's 'creative destruction' is highly beneficial for
society, it precludes investment certainty. A moat that must be continuously rebuilt will
eventually be no moat at all. Additionally, this criterion eliminates the business whose
success depends on having a great manager."* — is *"applied as a competence limit, never as a
fourth franchise criterion,"* and a name that passes **[E3-03]** but whose durability cannot
be judged from filings closes **UNKNOWABLE at Q2, without prejudice**.

**That is not this file.** Monro does not pass [E3-03]; it fails criterion (2) on the
registrant's own Competition section, and the [E3-03] demonstration test — aggressive pricing
producing high returns on capital — is documented running in reverse across seven filed
years. The finding is **about the business, from the filings**, not about my perimeter. There
is no document I cannot get. **So the verdict is OUT on the business, and not the perimeter
close.**

Nor is this the **[E2-58]** commodity door or the **[E2-59]** administered-price rescue: the
service is not undifferentiated in the way a physical commodity is — location and trust
differentiate it somewhat — and no regulator administers the price. **[E3-43]** supplies the
right frame instead: *"In contrast, 'a business' earns exceptional profits only if it is the
low-cost operator or if supply of its product or service is tight. Tightness in supply
usually does not last long … And a business, unlike a franchise, can be killed by poor
management."* Monro is *"a business"* in that sense. Its low-cost claim is refuted by
Valvoline's 22.8% against its own 1.7%, and service-bay supply in the United States is not
tight.

### VERDICT

- Needed or desired [x] · no close substitute [ ] **FAILS** · not price-regulated [x]
- Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]** —
  applied as the 2026-09-20 ruling requires, as a competence limit; it does not fire here,
  because the file closes on [E3-03] evidence and not on an unjudgeable perimeter. The
  great-manager half is recorded above at **[E4-23]** as a moat defect: the current plan is a
  $20.3M consultant-led turnaround costing more than the year's operating income.
- Primary moat metric, filing-sourced, and its trend: **operating margin 10.56% (FY2019) to
  1.73% (FY2026)**, and the physical series behind it, **vehicles serviced 6.2M to 3.8M**.
  **Trend: narrowing, in every year but one, for seven years.**
- Peers named: **5 filed, of an industry whose 4 largest direct competitors are private and
  do not file** — all four named above.
- **Untapped pricing power [E3-33]:** no; the price was already taken and the return fell.
- **Class: [x] NONE** · **Direction: NARROWING**

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**One line.** Monro fails **[E3-03]** criterion (2) on its own Competition disclosure, and the
[E3-03] demonstration test runs backwards in its own filings: it took **57.3% more revenue
per vehicle** while losing **38.7% of the vehicles**, and its return on unleveraged net
tangible assets **[E2-43]** fell from **21.5% to 2.4%** — while the closest filed peer selling
the same thing out of the same kind of bay **expanded** its operating margin to **22.80%**.
**The category did not break. This company did.** **[E4-18]**: *"we get paid, not for jumping
over 7-foot bars, but for stepping over 1-foot bars."* This is a seven-foot bar, and there is
no degree-of-difficulty credit for clearing it.

**The file closes here.** Operator rule 2: UNRESEARCHED and UNKNOWABLE both close the file and
neither is a pass; **OUT** closes it permanently. Q3 through Q6 are NOT OPENED.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?

**NOT OPENED. The file closed at Q2 (OUT, on the business).** Operator rule 2: the sequence
is hard, and a gate below a failed gate is not scored. Framework section III: *"Stop at the
first verdict that is not IN."*

**The standing CGNX instruction was nevertheless carried out, and early.** The newest 8-K
EX-99.1 earnings releases were pulled **before** any manager question could be reached:
- **accession 0001193125-26-322170**, furnished 2026-07-29, Q1 FY2027 results;
- **accession 0001193125-26-240509**, furnished 2026-05-27, FY2026 results.

Two things follow, and both are recorded rather than scored:
1. **[E4-29] does not fire, and the negative finding is worth as much as a positive one.**
   *"Trumpeting EBITDA (earnings before interest, taxes, depreciation and amortization) is a
   particularly pernicious practice. Doing so implies that depreciation is not truly an
   expense, given that it is a 'non-cash' charge. That's nonsense."* The word **EBITDA does
   not appear anywhere in either furnished release** (searched case-insensitively: zero
   occurrences in each). The 10-K uses "EBITDAR" only where it is quoting the *lenders'*
   covenant definition, which is the lenders' metric and not the company's public narrative.
   The CGNX pattern — clean in the 10-K, firing at full strength in the furnished release —
   **is absent here.** Monro's non-GAAP headline is adjusted operating income, adjusted net
   income and adjusted diluted EPS, all reconciled line by line to the GAAP measure in both
   the 10-K and the releases.
2. **What the release did carry was a moat claim, and a moat claim belongs at Q2.** It is
   tested there, above, under [E4-26], and is recorded as tested and not sustained.

- **VERDICT: NOT OPENED** *(not IN, not a pass, and not UNRESEARCHED — there is no work order
  here, because no further document changes a Q2 finding made on seven years of the
  registrant's own filed unit and margin series.)*

## Q4 — WILL IT SURVIVE?

**NOT OPENED.** The owner-earnings rebuild the brief commissioned is done, but it is done in
the **COMPUTATION — NOT A CLEARANCE** block below, under the heading operator rule 3
requires, and it carries no entry language and no verdict.

- **VERDICT: NOT OPENED**

## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**NOT OPENED, and it may not be.** Operator rule 2: *"No Q5 output may be reported unless
Q1-Q4 each show IN."* A yield appears once below so the register can carry a number, headed
as a computation and not as a clearance.

- **VERDICT: NOT OPENED**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**NOT OPENED as a gate.** There is no position and no entry, so **[E1-02]**'s *"I believe in
establishing yardsticks prior to the act; retrospectively, almost anything can be made to
look good in relation to something or other"* has nothing to bind. **[E2-28]**'s hold
conditions govern positions held, and none is held.

**But the file owes a reversal condition in words**, because the QLYS ruling (2026-09-07)
bars a price alert on a name that failed on the business and requires the condition be
written instead. It is at the end of this file.

- **VERDICT: NOT OPENED**

---

# COMPUTATION — NOT A CLEARANCE

**Operator rule 3.** Everything below was produced after Q2 returned OUT. **It carries no
entry language, it is not a valuation, and no part of it may be read as a Q5 output.** It
exists because the brief set four explicit reading assignments and because the screen row
carries five diagnostics that the run is obliged to resolve rather than repeat.

## 1. THE SEVENTEEN-YEAR OWNER-EARNINGS REBUILD — what the five-year window could not see

The `spread_caveat` says so itself: *"4-construction width only (3y/5y x two capex ends):
CANNOT see variation older than the 5-year window; rebuild it [E4-25]."* Rebuilt across
**every window the filings support**, which is seventeen fiscal years, FY2010 to FY2026.

**A source note first.** Operating cash flow resolves under two different tags across
Monro's filed history: `NetCashProvidedByUsedInOperatingActivitiesContinuingOperations` for
FY2010-FY2017 and `NetCashProvidedByUsedInOperatingActivities` for FY2016-FY2026. Both are
read. **Cross-checked by hand against the filed statement:** the FY2013 10-K's Consolidated
Statements of Cash Flows reads `Net cash provided by operating activities 84,436 / 82,626 /
65,520` for FY2013 / FY2012 / FY2011, which is exactly the tagged series.

**All figures $ millions. Owner earnings = operating cash flow − stock-based compensation −
(c), per the framework's confessed convention, with three constructions of (c).**

| FY | OCF | SBC | cash capex | D&A | fin. lease principal | **OE, (c)=D&A** | **OE, (c)=cash capex** | **OE, (c)=capex+lease principal** |
|---|---|---|---|---|---|---|---|---|
| 2010 | 86.5 | 2.0 | 21.3 | 22.5 | — | 62.0 | 63.2 | 63.2 |
| 2011 | 65.5 | 2.3 | 17.5 | 22.4 | — | 40.8 | 45.7 | 45.7 |
| 2012 | 82.6 | 2.7 | 28.6 | 23.6 | — | 56.3 | 51.4 | 51.4 |
| 2013 | 84.4 | 3.1 | 34.2 | 27.5 | — | 53.9 | 47.2 | 47.2 |
| 2014 | 93.9 | 3.6 | 32.1 | 31.7 | — | 58.7 | 58.2 | 58.2 |
| 2015 | 126.3 | 3.3 | 34.8 | 35.7 | — | 87.4 | 88.3 | 88.3 |
| 2016 | 126.5 | 2.8 | 36.8 | 39.8 | — | 84.0 | 86.9 | 86.9 |
| 2017 | 129.9 | 2.5 | 34.6 | 44.6 | — | 82.8 | 92.8 | 92.8 |
| 2018 | 121.2 | 2.9 | 39.1 | 49.3 | — | 69.0 | 79.3 | 79.3 |
| 2019 | 152.9 | 4.0 | 44.5 | 55.5 | — | 93.3 | 104.4 | 104.4 |
| 2020 | 121.3 | 3.8 | 55.9 | 65.0 | 27.2 | 52.5 | 61.6 | 34.4 |
| 2021 | 184.9 | 2.4 | 51.7 | 77.3 | 33.0 | 105.2 | 130.8 | 97.8 |
| 2022 | 173.8 | 4.3 | 27.8 | 81.2 | 39.4 | 88.3 | 141.6 | 102.2 |
| 2023 | 215.0 | 5.7 | 39.0 | 77.0 | 39.5 | 132.3 | 170.4 | 130.8 |
| 2024 | 125.2 | 4.3 | 25.5 | 72.2 | 39.0 | 48.7 | 95.4 | 56.4 |
| 2025 | 131.9 | 4.7 | 26.4 | 69.4 | 39.8 | 57.8 | 100.8 | 61.1 |
| **2026** | **70.4** | **3.9** | **31.7** | **61.7** | **38.7** | **4.9** | **34.9** | **−3.8** |

*Finance-lease principal payments are separately tagged only from FY2020. Monro carried
capital leases under the predecessor standard before that (the FY2019 balance sheet already
shows $238.1M of non-current capital-lease obligations), but the annual principal figure is
not separately tagged in those years, so the column is left empty rather than estimated.*

**The window table — every window, per [E4-38]'s remedy** (*"growth-rate presentations can be
significantly distorted by a calculated selection of either initial or terminal dates"*, and
its cure is to publish them all), with the five-year default of **[E2-42]** shown in bold:

| window | (c)=D&A | (c)=cash capex | **(c)=capex + lease principal** |
|---|---|---|---|
| 3 years, FY2024-26 | $37.1M | $77.1M | **$37.9M** |
| **5 years, FY2022-26 [E2-42]** | **$66.4M** | **$108.6M** | **$69.3M** |
| 7 years, FY2020-26 | $70.0M | $105.1M | $68.4M |
| 10 years, FY2017-26 | $73.5M | $101.2M | $75.5M |
| 17 years, FY2010-26 | $69.3M | $85.5M | $70.4M |

**The screen's published band of $37M to $107M is reproduced and explained**: $37M is the
three-year mean at the D&A end and $107M is close to the five-year mean at the capex end.
The construction is exactly what the `spread_caveat` said it was, and the caveat is correct
that it could not see the other thirteen years.

## 2. THE (c) JUDGMENT, DISCLOSED — because **[E2-09]** says it must be a guess

> "Our owner-earnings equation does not yield the deceptively precise figures provided by
> GAAP, since **(c) must be a guess** — and one sometimes very difficult to make. Despite
> this problem, we consider the owner earnings figure, not the GAAP figure, to be the
> relevant item for valuation purposes […] We agree with Keynes's observation: **'I would
> rather be vaguely right than precisely wrong.'**" — **[E2-09]**, 1986 appendix

**My guess, stated: (c) = cash capital expenditures PLUS finance-lease principal payments.**

**Why.** Item 2 of the 10-K: of 1,115 company-operated stores, **783 are leased, 290 are
owned and 42 are owned buildings on leased land.** A large part of the store estate is
financed by **finance** leases, whose principal repayment is a **financing** outflow and
therefore never touches operating cash flow, while the corresponding right-of-use asset
depreciates through D&A. **[E2-23]** defines (c) as *"the average annual amount of
capitalized expenditures for plant and equipment, etc. that the business requires to fully
maintain its long-term competitive position and its unit volume"* — for a store estate that
is two-thirds leased, the cash required to keep the stores standing includes the principal
on the leases that hold them up. Monro paid **$38.7M** of finance-lease principal in FY2026
against **$31.7M** of cash capex; taking the capex line alone as (c) omits more than half
the capital actually consumed.

**The cross-check that gives the guess its confidence.** The corpus's own default for (c) is
D&A — **[E3-44]**: *"by and large, the depreciation charge is not inappropriate in most
companies to use as a proxy for required capital expenditures"*, and **[E2-41]**: *"At 95% of
American businesses, capital expenditures that over time roughly approximate depreciation
are a necessity and are every bit as real an expense as labor or utility costs."* **My
construction and the corpus default agree at every window** — $37.1M against $37.9M, $66.4M
against $69.3M, $70.0M against $68.4M, $73.5M against $75.5M, $69.3M against $70.4M. Two
independently-built estimates of an unobservable landing within a few million of each other
at five different windows is the strongest evidence available that both are pointing at the
same number.

**Which end is therefore INVALID.** **[E5-20]** rules that for the capital-intensive class
*"merely spending their depreciation expense will not keep them in the same place"* and the
D&A end is invalid. **Monro is the mirror case.** Here it is the **cash-capex end that is
invalid**, and for a filed reason: D&A runs consistently *above* cash capex (FY2026: $61.7M
against $31.7M) precisely because the lease-financed assets depreciate without ever
appearing in the capex line. **The $107M top of the screen's published band is not an
optimistic-but-legitimate estimate of owner earnings; it is an arithmetic artifact of
omitting the lease-financed half of the store estate.** The honest band for this filer is the
D&A end and the capex-plus-lease-principal end, which agree.

**Windage count: ONE. [E4-11]** — *"You calculate — I think you take all of the variables and
calculate them reasonably conservatively. But you don't try and put too much windage in at
every level … And then when you get all through, you apply the margin of safety."*
Conservatism is spent once here, on the (c) judgment. **No end margin is applied, and no
margin of safety is taken, because no Bar is in use — the file is closed at Q2.** Publishing
all five windows is display **[E4-38]**, not a second helping of windage.

## 3. THE `acq_note` — RESOLVED, and it understates the roll-up by a factor of nine

The CSV prints, truncated at 110 characters: *"acquisitions are $90M, 23% of cap, inside the
window - the numerator and denominator may be different companie"*. **The function's full
string, recovered by running it:** *"acquisitions are $90M, 24% of cap, inside the window -
the numerator and denominator may be different companies. READ THE FILING."* (24% against the
hand-struck cap of $378M; 23% against the screen's $397M.)

**The finding is correct in kind and wrong in scale, because its window is five years.**
"Acquisitions, net of cash acquired", from the Consolidated Statements of Cash Flows of each
10-K, $ millions:

| FY2010 | FY2011 | FY2012 | FY2013 | FY2014 | FY2015 | FY2016 | FY2017 |
|---|---|---|---|---|---|---|---|
| 46.1 | 10.2 | 39.2 | **163.3** | 27.5 | 84.4 | 49.0 | **142.6** |

| FY2018 | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|---|---|
| 23.4 | 62.4 | **104.4** | 17.2 | 83.3 | 6.7 | **0** | **0** | **0** |

**Total FY2010-FY2026: $859.7 million** — **227% of the hand-struck market capitalisation of
$378.3M**, not 24% of it. Two years cross-checked by hand against the filed statement:
FY2020 `Acquisitions, net of cash acquired (104,436)`, FY2023 `(6,685)`.

**So [E4-25]'s warning about the roll-up is not merely live — it is nine times larger than
the screen could see.** The numerator and denominator of any multi-year mean built across
this history are emphatically different companies: 937 company-operated stores at FY2013,
1,304 at FY2022, 1,115 today. **And the acquisition line has been exactly zero for three
consecutive years**, while the store count fell by 189 from its peak and 145 stores were
closed in a single quarter. The engine that produced the growth has been switched off.

## 4. THE `level_note`, `level_note_oe` AND `flags_disagree` — RESOLVED, AND THE DISAGREEMENT IS AN ARTIFACT

All three CSV strings are truncated in the file. **Recovered in full by running the screen's
own functions against Monro's companyfacts:**

- `level_shift` on the nine-year **operating-cash** series `[121.2, 152.9, 121.3, 184.9,
  173.8, 215.0, 125.2, 131.9, 70.4]` returns **0.676** and the string **"STEP DOWN - the
  series has changed level; a tight spread here is not safety"**. The CSV's 60-character
  slice stops at *"a tight spread her"* — **it cuts the warning off before the word that
  carries it.** The finding is sound: the last three years mean $109.2M against $176.4M for
  the earlier six, and FY2026 alone is $70.4M.
- `level_shift` on the nine-year **owner-earnings-at-the-capex-end** series returns
  **`n/a`** with **"EARLY HALF STRADDLES ZERO - the pre-window years run from $-2.8M to
  $170.3M, crossing zero, so their mean ($79.5M) describes no year that happened and a ratio
  against it is undefined in substance even where it computes (it gives 0.97x). The level HAS
  changed and the multi-year mean is averaging TWO DIFFERENT BUSINESSES. READ THE FILING
  [E4-25]."** The CSV's 70-character slice stops at *"$-2.8M to $1"* — **which reads as if the
  early half ran from minus 2.8 to plus 1, i.e. all of it near zero. The real upper end is
  $170.3M.** The truncation does not merely shorten the diagnosis; it inverts it.
- `flags_disagree` fires because one series refuses the ratio and the other does not.
  **Resolved: the disagreement is an artifact of how the screen builds capex, and the OCF
  series is the reliable one here.**

**THE MECHANISM, and it is a tooling defect worth the operator's attention.**
`floor_screen.capital_acquired()` builds (c) as *"Cash capex PLUS software-development
additions PLUS unambiguous ASC 842 finance-lease additions."* The finance-lease addition it
uses is `RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability` — the **gross right-of-use
asset recognised at lease inception**, which is a **non-cash** entry recorded once when a
lease is signed. For Monro it resolves in **five of seventeen years only**:

| FY2018 | FY2019 | FY2020 | FY2021 | FY2022 | FY2023-26 |
|---|---|---|---|---|---|
| $19.2M | $14.6M | **$64.4M** | **$104.2M** | $8.8M | **nothing** |

Adding those to cash capex produces a (c) of **$120.3M in FY2020** and **$155.9M in FY2021**
against filed cash capex of $55.9M and $51.7M — and drives FY2020 owner earnings to
**−$2.8M**, which is the single negative value that trips the straddle-zero refusal, which in
turn produces `level_shift_oe n/a`, which in turn produces `flags_disagree`. **One non-cash
inception entry, present in five years out of seventeen, cascades into three separate CSV
flags.**

**[E2-23] is explicit that (c) is "the average annual amount of capitalized expenditures …
that the business requires to fully maintain".** A gross lease-inception asset is not an
annual maintenance expenditure; it is a balance-sheet recognition of a multi-year commitment,
and it is recorded in whichever year the lease happened to be signed. **The cash form of the
same idea — the finance-lease principal actually paid each year — is smooth ($27.2M, $33.0M,
$39.4M, $39.5M, $39.0M, $39.8M, $38.7M), available every year from FY2020, and lands within
a few million of the corpus's own D&A default at every window.** *Proposal for the operator,
not applied here:* `capital_acquired()` should take **`FinanceLeasePrincipalPayments`**, not
`RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability`. This is a one-tag change and it
removes a defect that can fire on any lease-heavy filer — which is every retailer, every
restaurant chain and every service-bay operator in the queue.

## 5. THE ASC 842 QUESTION THE BRIEF ASKED — answered, and MNRO is NOT the KBH case

The brief asked whether Monro's operating-cash series carries the discontinuity the KBH run
of 2026-09-21 found. **It does not, and the reason is specific.**
- **Operating leases** were an operating-cash item both before and after adoption: rent
  expense pre-ASC-842, operating-lease payments post-adoption. No break.
- **Capital/finance leases** put principal in financing both before and after — Monro carried
  $238.1M of non-current capital-lease obligations at FY2019, under the predecessor standard.
  No break.
- **So the OCF series is like-for-like across FY2020 and may be averaged across it.**

**What DID break is the balance sheet, and any ratio built on it.** Total assets went
**$1,312.3M (FY2019) to $2,049.5M (FY2020)** on adoption, of which $199.7M is the newly
recognised operating-lease right-of-use asset and much of the rest is the $345.5M of cash
Monro drew on its revolver in March 2020. **Any return-on-assets or return-on-capital series
crossing FY2020 is not like-for-like**, which is why the Q2 return table above shows the
FY2026 figure twice, once with the ROU asset and once without.

## 6. THE YIELD ARITHMETIC — shown once, so the register can carry a number, and **IT IS NOT A Q5 OUTPUT**

**Market capitalisation $378,295,126.** **Sovereign 5.34%**, US 30-year, 2026-09-18, US
Treasury. **No margin of safety is applied and no Bar is in use.**

| owner-earnings window and (c) | OE | ÷ cap | |
|---|---|---|---|
| 3 years, (c)=D&A | $37.1M | **9.8%** | the screen's published bottom, reproduced |
| 3 years, (c)=capex + lease principal | $37.9M | **10.0%** | |
| **5 years [E2-42], (c)=capex + lease principal** | **$69.3M** | **18.3%** | |
| 17 years, (c)=capex + lease principal | $70.4M | **18.6%** | |
| **FY2026 alone, (c)=D&A** | **$4.9M** | **1.3%** | |
| **FY2026 alone, (c)=capex + lease principal** | **−$3.8M** | **negative** | |
| *(5 years, (c)=cash capex — shown only to be refused)* | *$108.6M* | *28.7%* | *the end judged INVALID at §2* |

**Why this number decides nothing.** The spread runs from **negative** to **18.6%** depending
entirely on which years are averaged, and **[E4-25]** is explicit about what that means:
*"Usually, the range must be so wide that no useful conclusion can be reached."* The wide
range is itself the finding. The seventeen-year mean is high **because it averages a company
that no longer exists** — one with 21.5% returns on net tangible assets, 6.2 million vehicles
a year and a working acquisition engine — with the one that filed this year's 10-K. **That is
[E4-25]'s different-companies problem stated in dollars, and it is why the file closed on the
business at Q2 and not on a price.** Operator rule 3: this block is a computation and not a
clearance, and nothing in it may be read as entry language.

---

## SELF-AUDIT

- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 **OUT**, Q3-Q6 recorded
      **NOT OPENED** with the reason, per the hard sequence (operator rule 2).
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the
      only IN and it rests on the filed Item 1, Item 2 and MD&A of the FY2026 10-K.
- [x] Every UNRESEARCHED verdict names the artifact — **none used.** Q2 is OUT on evidence in
      hand, not UNRESEARCHED; there is no document whose absence changes it.
- [x] Every UNKNOWABLE verdict states what cannot be known — **none used.** The [E4-04]
      perimeter close was checked against the 2026-09-20 ruling and explicitly does not apply.
- [x] Step 0: the filing was read, with accession number; two figures cross-checked by hand
      (D&A $61,674 thousand; operating income $20,029 thousand from gross profit less OSG&A).
      Further hand checks at Q2 (FY2020 and FY2023 acquisition outflows; VVV's operating
      income) and in the computation block (FY2011-FY2013 operating cash flow).
- [x] Owner earnings on a multi-year mean; **five windows stated**; capex band disclosed as a
      judgment with the cash-capex end named INVALID and why. Done in the **COMPUTATION**
      block under the operator-rule-3 heading, carrying no entry language.
- [x] Competitor row filled — five filed peers, same metric, same window, each sourced; the
      four largest direct competitors named as private and unavailable, with the consequence
      for the moat class stated.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury
      daily par yield curve), dated 2026-09-18, saved to the research folder.
- [x] Value stated as a round-number range, not a point estimate — and stated to be too wide
      to conclude from **[E4-25]**.
- [x] One bar chosen, not both — **neither**, because Q5 did not open. Windage count **1**,
      stated, and no end margin applied.
- [x] Prices dated; aggregator used for the live quote only and flagged as such.
- [x] Run committed to git, after every question, with a pathspec.
- [x] **PRIME RULE 1:** every ledger id quoted in this file was opened and read against its
      own row before being quoted; the dump is at
      `Test Runs/_research 2026-09-21 MNRO/ledger_rows_read.txt`. The OCR artifacts in
      **[E4-55]** are reproduced, not smoothed.
- [x] **Operator rule 9 / [E4-26]:** the hypothesis I wanted — that the whole category was in
      trouble, which would have kept the file open — was the one I went looking hardest to
      confirm, and the competitor row refuted it.

## REGISTER

- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** Monro fails **[E3-03]** criterion (2) on its own Competition disclosure, and
  the [E3-03] demonstration test runs backwards in its filings — **+57.3% revenue per vehicle
  against −38.7% vehicles serviced over seven years, with the operating margin going 10.56%
  to 1.73% and return on unleveraged net tangible assets [E2-43] going 21.5% to 2.4%** —
  while the closest filed peer selling the same service out of the same kind of bay expanded
  its operating margin to 22.80%. **The category did not break; this company did.**

### THE REVERSAL CONDITION, IN WORDS — no price alert, per the QLYS ruling (2026-09-07)

A name that failed on the **business** gets no price band, because a price alert on it is a
category error. The condition that would reopen this file is therefore written, not armed:

**Reopen if, and only if, the physical series turns and stays turned.** Specifically, **three
consecutive fiscal years in which vehicles serviced rises**, disclosed in Item 1 of the 10-K
as Monro has disclosed it every year, **accompanied by operating margin above 6%** — which is
the level the business last held in FY2023 and roughly a third of what the closest peer earns
today. A recovery in dollar sales alone does not qualify and never has: the last seven years
show exactly how far the dollar line can be carried by price while the business empties out.
A single good quarter does not qualify either — **[E4-17]**'s *"those beliefs change quite
gradually"* cuts both ways, and the FY2027 first quarter, with comparable store sales at
−1.7% and an adjusted operating margin of 0.8%, is not the start of anything yet.

### FINDINGS OWED TO THE PROJECT, not to this name

1. **The `cap_flag` is a price-decline detector, not a sanity check.** Compare the filed float
   against a cap struck **at the float date**, not against the live cap. Full arithmetic at
   Step 0.
2. **`capital_acquired()` uses a non-cash lease-inception entry as if it were annual
   maintenance capex.** Use `FinanceLeasePrincipalPayments`. Full mechanism at §4 above, with
   the cascade into three CSV flags traced.
3. **Three CSV note columns are sliced mid-sentence** — `level_note[:60]`,
   `level_note_oe[:70]`, `acq_note[:110]` in `Screens/regen_queue.py` — while `wc_note` gets
   260 and `cap_flag` is written in full at 252. **The two notes carrying the most
   consequential diagnosis get the shortest slices**, and in Monro's case the truncation
   inverts the meaning ($-2.8M to $1 reads as a near-zero range; the real one ends at
   $170.3M).
4. **`best_year_dep_oe` has no note column at all.** The CSV carries the number 0.265 and
   discards the string the function returned: *"TWO YEARS JOINTLY CARRY THE WINDOW - the exact
   two-year-boom shape leave-one-out cannot see; re-price on a window that excludes both."*
   There is a `best_year_note` for the operating-cash series and no `best_year_note_oe` for
   the series that is actually valued. This is the same defect class the queue's own FOLD
   section names: *a diagnostic that exists but never reaches the reader.*
5. **`newest_filing` carries a period-end date, not a filing date**, and both date columns are
   a quarter stale. Confirmed again here, on a fiscal-March filer where the error is most
   visible.
6. **`principle_ledger.csv` contains 311 rows.** `CLAUDE.md`'s KEY FILES table still says 267.
   Counted from the file, not the pointer, as the thirteenth consecutive fold to record it.
   **`CLAUDE.md` is not edited** — PRIME RULE 5 puts a structural correction to the operator's
   own file in front of the operator first.
7. **Not scored, and recorded only because they were read while reading the filing.** These
   are Q3 and Q4 material and Q3 and Q4 did not open; they are observations, not verdicts,
   and no part of the Q2 verdict rests on them. (a) Monro declared **$35.0M of dividends in
   FY2026 against $2.2M of net income and $4.9M of owner earnings on the corpus's own default
   (c)**. (b) It has entered **six amendments to its credit facility**, the last three being
   consecutive covenant-relief periods that cut the minimum interest-coverage ratio from
   1.55x to 1.15x and then 1.25x, while the facility was permanently reduced from $600M to
   $500M to $400M. (c) It reported **$2.4M of cash on hand as of 2026-05-15** and a **$281.2M
   working-capital deficit** that the MD&A attributes to its supply-chain finance programme.
   (d) The FY2026 10-K discloses **a prior-period error in the financing section of the
   FY2025 and FY2024 cash-flow statements and three FY2026 quarters**. (e) FY2026 adjusted
   operating income excludes **$20.3M of Operational Improvement Plan consulting**, an amount
   larger than the year's entire GAAP operating income. Any future run that reopens this name
   starts at Q3 with these five on the table.
